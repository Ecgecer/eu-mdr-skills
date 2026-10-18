#!/usr/bin/env python3
"""Run eu-mdr-bench against a model through its plain API, and save the responses.

The benchmark's measured column comes from one model. That makes it a report, not a
benchmark. This sends every case prompt to another provider and stores the raw answers
so they can be judged with the same criteria.

Judging is a separate step on purpose: mixing generation and scoring in one pass is how
you end up unable to tell a model failure from a grader failure.

The harness must be a plain completion endpoint. An agent CLI is not one: the Gemini
CLI answers these prompts by calling its WebSearch tool, so it scores a model plus a
search engine, and the number cannot be compared against the Claude ablation, which had
no retrieval. Measured 2026-09-11, stack frame WebSearchToolInvocation.execute. The same
applies to any wrapper with browsing, RAG or tools enabled. Use the raw API.

Providers, in order of least setup:

  gemini     GEMINI_API_KEY      paid tier: the free quota ran out mid-arm on 2026-09-11
  vertex     gcloud auth         needs aiplatform.googleapis.com enabled on the project
  openai     OPENAI_API_KEY
  anthropic  ANTHROPIC_API_KEY   the plain API, not the Claude Code harness the published
                                 tables used. Comparable to the other providers here, not
                                 to those tables

Usage:
  GEMINI_API_KEY=... python3 scripts/run-benchmark.py --provider gemini --model <id> \\
      --thinking-level medium
  python3 scripts/run-benchmark.py --provider vertex --model <id>
  python3 scripts/run-benchmark.py --provider gemini --model <id> \\
      --probe-dir mdr-transition/roadmap-probe
  python3 scripts/run-benchmark.py --list
"""
import argparse, importlib.util, json, os, re, subprocess, sys, time, urllib.error, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "benchmark" / "eu-mdr-bench.json"
RUNS = ROOT / "benchmark" / "runs"

def _axis_for():
    """export-benchmark.py's classifier, loaded rather than copied, so a probe case and
    a benchmark case with the same tags can never land on different axes."""
    spec = importlib.util.spec_from_file_location("export_benchmark",
                                                  ROOT / "scripts" / "export-benchmark.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.axis_for

def bundle_for(area):
    """The dist bundle a case's plugin ships, or None.

    Prepending it is exactly what README tells a user to do in a tool that cannot read
    the repo: paste the bundle, then ask. So the with-skill arm here measures the
    portable path as documented, not a private variant of it.
    """
    hits = sorted((ROOT / area).glob("skills/*/SKILL.md"))
    if not hits:
        return None
    b = ROOT / "dist" / f"{hits[0].parent.name}.bundle.md"
    return b.read_text() if b.exists() else None

def probe_cases(probe_dir):
    """Cases from a directory in the Claude Code eval layout: <case>/prompt.md plus
    <case>/graders/criteria.md. Same parsing as export-benchmark.py, so a probe run is
    judged against exactly the text the harness grader sees."""
    cases = []
    for pp in sorted(Path(probe_dir).glob("*/prompt.md")):
        raw = pp.read_text()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        fm, body = (m.group(1), m.group(2).strip()) if m else ("", raw.strip())
        name = (re.search(r"^name:\s*(\S+)", fm, re.M) or [None, pp.parent.name])[1]
        tags = re.search(r"^tags:\s*\[(.*?)\]", fm, re.M)
        tags = [t.strip() for t in tags.group(1).split(",")] if tags else []
        g = pp.parent / "graders" / "criteria.md"
        crit = re.sub(r"^---\n.*?\n---\n", "", g.read_text(), flags=re.S).strip() \
            if g.exists() else ""
        cases.append({"id": name, "area": None, "tags": tags,
                      "axis": _axis_for()(tags), "prompt": body,
                      "correct_answer_criteria": crit,
                      "criteria_assume_skill_format": False})
    return cases

RETRY_CODES = {429, 500, 502, 503, 504}

class QuotaExhausted(Exception):
    """A spent quota, not a busy queue. Retrying burns the run's remaining cases on the
    same error, which is how the 2026-09-11 Gemini arm ended at 0 of 33: abort instead,
    and save what exists."""

def post(url, payload, headers, timeout=300, attempts=4):
    """POST with backoff on transient failures.

    503 "experiencing high demand" and 429 are routine on a shared endpoint, and a run
    of 30+ calls will meet them. Without retries a whole arm reports as model failures
    that were really queue failures -- the same confusion that once scored a billing
    error as a skill error.
    """
    body = json.dumps(payload).encode()
    last = None
    for attempt in range(attempts):
        req = urllib.request.Request(url, data=body,
                                     headers={"Content-Type": "application/json", **headers})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode()), None
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read().decode()[:300]}"
            if e.code == 429 and re.search(r"exceeded your current quota|quota exceeded|"
                                           r"insufficient_quota|credit balance", last, re.I):
                raise QuotaExhausted(last)
            if e.code not in RETRY_CODES:
                return None, last
        except Exception as e:
            last = str(e)
        if attempt < attempts - 1:
            wait = 5 * (2 ** attempt)
            print(f"      transient ({last[:40]}...), retrying in {wait}s")
            time.sleep(wait)
    return None, last

# Every ask_* returns (text, error, meta). meta records why generation stopped and what
# it cost in thinking, because a thinking model that spends its output cap on reasoning
# returns empty or truncated text, and that must not be scored as a model failure.

def gemini_body(prompt, a):
    gen = {"maxOutputTokens": a.max_output_tokens,
           # Google's guidance for Gemini 3 is to keep temperature at 1.0; lower values
           # can loop. Runs are repeated three times precisely because output varies.
           "temperature": 1}
    if a.thinking_level:
        gen["thinkingConfig"] = {"thinkingLevel": a.thinking_level}
    elif a.thinking_budget is not None:
        gen["thinkingConfig"] = {"thinkingBudget": a.thinking_budget}
    return {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": gen}

def gemini_parse(d):
    try:
        cand = d["candidates"][0]
        parts = (cand.get("content") or {}).get("parts") or []
        text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    except Exception:
        return None, f"unexpected shape: {json.dumps(d)[:200]}", {}
    u = d.get("usageMetadata") or {}
    meta = {"finish": cand.get("finishReason"), "model_version": d.get("modelVersion"),
            "output_tokens": u.get("candidatesTokenCount"),
            "thinking_tokens": u.get("thoughtsTokenCount")}
    if meta["finish"] == "MAX_TOKENS":
        return None, f"truncated at max_output_tokens ({len(text)} chars kept)", meta
    if not text:
        return None, f"empty response, finishReason={meta['finish']}", meta
    return text, None, meta

def ask_gemini(prompt, model, key, a):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    # Header, not ?key= -- a query-string key is logged by every proxy in the path.
    d, err = post(url, gemini_body(prompt, a), {"x-goog-api-key": key})
    if err: return None, err, {}
    return gemini_parse(d)

def ask_vertex(prompt, model, a):
    proj = subprocess.run(["gcloud","config","get-value","project"],
                          capture_output=True, text=True).stdout.strip()
    tok = subprocess.run(["gcloud","auth","print-access-token"],
                         capture_output=True, text=True).stdout.strip()
    if not proj or not tok: return None, "gcloud not configured", {}
    loc = os.environ.get("VERTEX_LOCATION", "us-central1")
    host = "aiplatform.googleapis.com" if loc == "global" else f"{loc}-aiplatform.googleapis.com"
    url = (f"https://{host}/v1/projects/{proj}/locations/{loc}"
           f"/publishers/google/models/{model}:generateContent")
    d, err = post(url, gemini_body(prompt, a), {"Authorization": f"Bearer {tok}"})
    if err: return None, err, {}
    return gemini_parse(d)

def ask_gemini_cli(prompt, model, a):
    """Refused. The gemini CLI is an agent, not a completion endpoint.

    Given these prompts it reaches for WebSearch, so the answer reflects a model plus
    whatever it retrieved. The Claude column was measured with no retrieval, so the two
    are not comparable, and the contamination is invisible in the stored text.
    """
    return None, ("gemini-cli retrieves (WebSearch) -- not comparable to the no-retrieval "
                  "Claude column. Use --provider gemini with GEMINI_API_KEY."), {}

def ask_openai(prompt, model, key, a):
    body = {"model": model, "messages": [{"role":"user","content":prompt}],
            "max_completion_tokens": a.max_output_tokens}
    if a.thinking_level:
        body["reasoning_effort"] = a.thinking_level
    d, err = post("https://api.openai.com/v1/chat/completions", body,
                  {"Authorization": f"Bearer {key}"})
    if err: return None, err, {}
    try:
        ch = d["choices"][0]
        text = ch["message"]["content"] or ""
    except Exception:
        return None, f"unexpected shape: {json.dumps(d)[:200]}", {}
    u = d.get("usage") or {}
    meta = {"finish": ch.get("finish_reason"), "model_version": d.get("model"),
            "output_tokens": u.get("completion_tokens"),
            "thinking_tokens": (u.get("completion_tokens_details") or {}).get("reasoning_tokens")}
    if meta["finish"] == "length":
        return None, f"truncated at max_output_tokens ({len(text)} chars kept)", meta
    if not text:
        return None, f"empty response, finish_reason={meta['finish']}", meta
    return text, None, meta

def ask_anthropic(prompt, model, key, a):
    """Messages API, raw HTTP like the other providers. No server-side refusal fallback:
    a silent switch to another model mid-run would put a second model's answers in this
    model's column. A refusal is recorded as an error and excluded, like any other."""
    body = {"model": model, "max_tokens": a.max_output_tokens,
            "messages": [{"role": "user", "content": prompt}]}
    if a.thinking_level:
        body["output_config"] = {"effort": a.thinking_level}
    d, err = post("https://api.anthropic.com/v1/messages", body,
                  {"x-api-key": key, "anthropic-version": "2023-06-01"})
    if err: return None, err, {}
    try:
        text = "".join(b.get("text", "") for b in d["content"] if b.get("type") == "text")
    except Exception:
        return None, f"unexpected shape: {json.dumps(d)[:200]}", {}
    u = d.get("usage") or {}
    meta = {"finish": d.get("stop_reason"), "model_version": d.get("model"),
            "output_tokens": u.get("output_tokens"), "thinking_tokens": None}
    if meta["finish"] == "max_tokens":
        return None, f"truncated at max_output_tokens ({len(text)} chars kept)", meta
    if meta["finish"] == "refusal":
        return None, f"refusal: {json.dumps(d.get('stop_details'))[:200]}", meta
    if not text:
        return None, f"empty response, stop_reason={meta['finish']}", meta
    return text, None, meta

KEYS = {"gemini": "GEMINI_API_KEY", "openai": "OPENAI_API_KEY",
        "anthropic": "ANTHROPIC_API_KEY"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["gemini","gemini-cli","vertex","openai","anthropic"])
    ap.add_argument("--model", default="gemini-2.5-pro")
    ap.add_argument("--runs", type=int, default=3,
                    help="runs per case; 3 is the minimum that is evidence")
    ap.add_argument("--case", help="only this case id")
    ap.add_argument("--with-skill", action="store_true",
                    help="prepend the case's dist bundle, the way README tells a user to "
                         "paste it into a chat. Without this the run measures the "
                         "baseline: the model unaided, which is what baseline_pass_rate "
                         "is. Run both to get a delta")
    ap.add_argument("--hard-only", action="store_true",
                    help="only cases where the measured baseline scored 0.00 -- the ones "
                         "that actually discriminate between models")
    ap.add_argument("--probe-dir", metavar="DIR",
                    help="run the cases in DIR (eval layout: <case>/prompt.md + "
                         "graders/criteria.md) instead of the benchmark, e.g. "
                         "mdr-transition/roadmap-probe. Baseline arm only")
    ap.add_argument("--thinking-level", metavar="LEVEL",
                    help="pin reasoning depth, and record it: Gemini thinkingLevel, OpenAI "
                         "reasoning_effort, Anthropic output_config.effort. Unpinned, each "
                         "model runs at its own default and two columns differ by a setting "
                         "nobody chose")
    ap.add_argument("--thinking-budget", type=int, metavar="N",
                    help="Gemini 2.5-generation models only, which take a token budget "
                         "rather than a level")
    ap.add_argument("--max-output-tokens", type=int, default=16384,
                    help="thinking counts against this on thinking models; the old 4096 cap "
                         "could leave nothing for the answer")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    bench = json.loads(BENCH.read_text())
    if a.list:
        for c in bench["cases"]:
            m = c.get("measured") or {}
            r = m.get("baseline_pass_rate")
            print(f"  {c['id']:<34} {c['area']:<20} claude_baseline="
                  f"{', ' if r is None else format(r, '.2f')}")
        return 0
    if not a.provider:
        ap.error("--provider is required unless --list")
    if a.thinking_level and a.thinking_budget is not None:
        ap.error("--thinking-level and --thinking-budget are alternatives")
    if a.thinking_budget is not None and a.provider not in ("gemini", "vertex"):
        ap.error("--thinking-budget is a Gemini 2.5 setting")
    if a.probe_dir and a.with_skill:
        ap.error("--probe-dir runs the baseline only: a probe measures a skill that does "
                 "not exist yet, so there is no bundle to prepend")

    if a.probe_dir:
        cases = probe_cases(ROOT / a.probe_dir)
        if not cases:
            ap.error(f"no <case>/prompt.md under {a.probe_dir}")
    else:
        cases = bench["cases"]
    if a.case: cases = [c for c in cases if c["id"] == a.case]
    if a.hard_only:
        cases = [c for c in cases
                 if (c.get("measured") or {}).get("baseline_pass_rate") == 0.0]

    if a.provider == "gemini-cli":
        print("  gemini-cli is an agent: it answers these prompts with WebSearch, so its")
        print("  scores measure a model plus a search engine and cannot be compared with")
        print("  the Claude column, which had no retrieval.")
        print("  Use: GEMINI_API_KEY=... --provider gemini --model <id>")
        return 2

    key = os.environ.get(KEYS[a.provider]) if a.provider in KEYS else None
    if a.provider in KEYS and not key:
        print(f"  set {KEYS[a.provider]}")
        return 2

    RUNS.mkdir(parents=True, exist_ok=True)
    arm = "with-skill" if a.with_skill else "baseline"
    out = {"model": a.model, "provider": a.provider, "runs_per_case": a.runs,
           "arm": arm,
           # The Claude column had no retrieval. A run that did is not comparable, so
           # every run file states its own condition rather than leaving it assumed.
           "retrieval": "none",
           "source": a.probe_dir or "benchmark/eu-mdr-bench.json",
           "thinking_level": a.thinking_level, "thinking_budget": a.thinking_budget,
           "max_output_tokens": a.max_output_tokens,
           "started": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "aborted": None,
           # The criteria travel with the answers, so judge-benchmark.py judges a probe
           # run without a second source of truth that could drift from what was asked.
           "criteria": {c["id"]: {"text": c["correct_answer_criteria"],
                                  "assume_skill_format": c.get("criteria_assume_skill_format", False),
                                  "axis": c.get("axis")}
                        for c in cases},
           "responses": []}
    try:
        for i, c in enumerate(cases, 1):
            for r in range(a.runs):
                prompt = c["prompt"]
                if a.with_skill:
                    bundle = bundle_for(c["area"])
                    if not bundle:
                        print(f"  [{i}/{len(cases)}] {c['id']}: no bundle for {c['area']}, skipped")
                        continue
                    prompt = f"{bundle}\n\n---\n\n{c['prompt']}"
                if a.provider == "gemini":   text, err, meta = ask_gemini(prompt, a.model, key, a)
                elif a.provider == "vertex": text, err, meta = ask_vertex(prompt, a.model, a)
                elif a.provider == "openai": text, err, meta = ask_openai(prompt, a.model, key, a)
                else:                        text, err, meta = ask_anthropic(prompt, a.model, key, a)
                out["responses"].append({"case": c["id"], "run": r+1,
                                         "response": text, "error": err, "meta": meta})
                print(f"  [{i}/{len(cases)}] {c['id']} run {r+1}: "
                      f"{'ok, ' + str(len(text)) + ' chars' if text else 'ERROR ' + (err or '')[:70]}")
                time.sleep(1)
    except QuotaExhausted as e:
        out["aborted"] = f"quota exhausted: {str(e)[:200]}"
        print(f"\n  ABORTED, quota exhausted. Saving the {len(out['responses'])} response(s) "
              "collected. Re-run with a funded key; a partial arm is not a measurement.")
    f = RUNS / f"{a.model}-{arm}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}.json"
    f.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    ok = sum(1 for x in out["responses"] if x["response"])
    print(f"\n  {ok}/{len(out['responses'])} responses saved -> {f.relative_to(ROOT)}")
    print("  Judge them: python3 scripts/judge-benchmark.py <that file>, or by hand with")
    print("  score-benchmark.py --emit. Do not let the model judge itself.")
    print("  Runs are only comparable if the model had no web access.")
    return 1 if out["aborted"] else 0

if __name__ == "__main__":
    sys.exit(main())
