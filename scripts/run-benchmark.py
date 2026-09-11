#!/usr/bin/env python3
"""Run eu-mdr-bench against a model that is not Claude, and save the responses.

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

  gemini   GEMINI_API_KEY   free key from aistudio.google.com
  vertex   gcloud auth      needs aiplatform.googleapis.com enabled on the project
  openai   OPENAI_API_KEY

Usage:
  GEMINI_API_KEY=... python3 scripts/run-benchmark.py --provider gemini --model gemini-2.5-pro
  python3 scripts/run-benchmark.py --provider vertex --model gemini-2.5-pro
  python3 scripts/run-benchmark.py --list
"""
import argparse, json, os, subprocess, sys, time, urllib.error, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "benchmark" / "eu-mdr-bench.json"
RUNS = ROOT / "benchmark" / "runs"

def post(url, payload, headers, timeout=120):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json", **headers})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode()), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}: {e.read().decode()[:300]}"
    except Exception as e:
        return None, str(e)

def ask_gemini(prompt, model, key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": 4096, "temperature": 1}}
    # Header, not ?key= -- a query-string key is logged by every proxy in the path.
    d, err = post(url, body, {"x-goog-api-key": key})
    if err: return None, err
    try:
        return "".join(p.get("text", "") for p in d["candidates"][0]["content"]["parts"]), None
    except Exception:
        return None, f"unexpected shape: {json.dumps(d)[:200]}"

def ask_vertex(prompt, model):
    proj = subprocess.run(["gcloud","config","get-value","project"],
                          capture_output=True, text=True).stdout.strip()
    tok = subprocess.run(["gcloud","auth","print-access-token"],
                         capture_output=True, text=True).stdout.strip()
    if not proj or not tok: return None, "gcloud not configured"
    loc = os.environ.get("VERTEX_LOCATION", "us-central1")
    url = (f"https://{loc}-aiplatform.googleapis.com/v1/projects/{proj}/locations/{loc}"
           f"/publishers/google/models/{model}:generateContent")
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": 4096}}
    d, err = post(url, body, {"Authorization": f"Bearer {tok}"})
    if err: return None, err
    try:
        return "".join(p.get("text","") for p in d["candidates"][0]["content"]["parts"]), None
    except Exception:
        return None, f"unexpected shape: {json.dumps(d)[:200]}"

def ask_gemini_cli(prompt, model):
    """Refused. The gemini CLI is an agent, not a completion endpoint.

    Given these prompts it reaches for WebSearch, so the answer reflects a model plus
    whatever it retrieved. The Claude column was measured with no retrieval, so the two
    are not comparable, and the contamination is invisible in the stored text.
    """
    return None, ("gemini-cli retrieves (WebSearch) -- not comparable to the no-retrieval "
                  "Claude column. Use --provider gemini with GEMINI_API_KEY.")


def ask_openai(prompt, model, key):
    d, err = post("https://api.openai.com/v1/chat/completions",
                  {"model": model, "messages": [{"role":"user","content":prompt}]},
                  {"Authorization": f"Bearer {key}"})
    if err: return None, err
    try: return d["choices"][0]["message"]["content"], None
    except Exception: return None, f"unexpected shape: {json.dumps(d)[:200]}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["gemini","gemini-cli","vertex","openai"])
    ap.add_argument("--model", default="gemini-2.5-pro")
    ap.add_argument("--runs", type=int, default=3,
                    help="runs per case; 3 is the minimum that is evidence")
    ap.add_argument("--case", help="only this case id")
    ap.add_argument("--hard-only", action="store_true",
                    help="only cases where the measured baseline scored 0.00 -- the ones "
                         "that actually discriminate between models")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    bench = json.loads(BENCH.read_text())
    cases = bench["cases"]
    if a.case: cases = [c for c in cases if c["id"] == a.case]
    if a.hard_only:
        cases = [c for c in cases
                 if (c.get("measured") or {}).get("baseline_pass_rate") == 0.0]
    if a.list:
        for c in bench["cases"]:
            m = c.get("measured") or {}
            r = m.get("baseline_pass_rate")
            print(f"  {c['id']:<34} {c['area']:<20} claude_baseline="
                  f"{'—' if r is None else format(r, '.2f')}")
        return 0
    if not a.provider:
        ap.error("--provider is required unless --list")

    if a.provider == "gemini-cli":
        print("  gemini-cli is an agent: it answers these prompts with WebSearch, so its")
        print("  scores measure a model plus a search engine and cannot be compared with")
        print("  the Claude column, which had no retrieval.")
        print("  Use: GEMINI_API_KEY=... --provider gemini --model gemini-2.5-pro")
        return 2

    key = os.environ.get("GEMINI_API_KEY") if a.provider=="gemini" else \
          os.environ.get("OPENAI_API_KEY") if a.provider=="openai" else None
    if a.provider in ("gemini","openai") and not key:
        print(f"  set {'GEMINI_API_KEY' if a.provider=='gemini' else 'OPENAI_API_KEY'}")
        return 2

    RUNS.mkdir(parents=True, exist_ok=True)
    out = {"model": a.model, "provider": a.provider, "runs_per_case": a.runs,
           # The Claude column had no retrieval. A run that did is not comparable, so
           # every run file states its own condition rather than leaving it assumed.
           "retrieval": "none",
           "started": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "responses": []}
    for i, c in enumerate(cases, 1):
        for r in range(a.runs):
            if a.provider == "gemini-cli": text, err = ask_gemini_cli(c["prompt"], a.model)
            elif a.provider == "gemini": text, err = ask_gemini(c["prompt"], a.model, key)
            elif a.provider == "vertex": text, err = ask_vertex(c["prompt"], a.model)
            else:                        text, err = ask_openai(c["prompt"], a.model, key)
            out["responses"].append({"case": c["id"], "run": r+1,
                                     "response": text, "error": err})
            print(f"  [{i}/{len(cases)}] {c['id']} run {r+1}: "
                  f"{'ok, ' + str(len(text)) + ' chars' if text else 'ERROR ' + (err or '')[:70]}")
            time.sleep(1)
    f = RUNS / f"{a.model}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}.json"
    f.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    ok = sum(1 for x in out["responses"] if x["response"])
    print(f"\n  {ok}/{len(out['responses'])} responses saved -> {f.relative_to(ROOT)}")
    print("  Judge them against each case's correct_answer_criteria, then add a column")
    print("  to benchmark/README.md. Do not let the model judge itself.")
    print("  Runs are only comparable if the model had no web access.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
