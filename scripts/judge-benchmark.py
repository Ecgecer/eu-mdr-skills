#!/usr/bin/env python3
"""Fill a judgments file for a stored run with an LLM judge, one verdict and reason each.

score-benchmark.py scores from a judgments file and refuses to score until every
response has a verdict. Until now those verdicts were written by hand, which is why
only six Gemini cases were ever judged. This writes the same file, with the same
per-response `why`, so a reader can still disagree with a specific call.

Rules it enforces, because each one has already cost this repo a wrong number:

  - The judge is not the model under test. Same model id is refused outright; same
    provider is allowed but printed, because it is a weaker separation.
  - Verdicts already in the file are kept. A human verdict is never overwritten
    unless --rejudge is passed, and then only the ones named.
  - Errored generations are not judged. They are excluded, not failed.
  - Criteria come from the run file when it carries them (every run since 2026-10-18),
    so a probe run is judged against the text that was current when it was generated.
  - Where the criteria assume the skill's output format, the judge is told to judge
    the substance. Scoring a baseline on a format it was never shown measures nothing.

Usage:
  ANTHROPIC_API_KEY=... python3 scripts/judge-benchmark.py benchmark/runs/<run>.json
  python3 scripts/judge-benchmark.py <run>.json --judge-provider gemini --judge-model <id>
  python3 scripts/judge-benchmark.py <run>.json --rejudge case-id:2 case-id:3
"""
import argparse, importlib.util, json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "benchmark" / "eu-mdr-bench.json"
JUDGMENTS = ROOT / "benchmark" / "judgments"

_spec = importlib.util.spec_from_file_location("run_benchmark", ROOT / "scripts" / "run-benchmark.py")
rb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rb)

FORMAT_NOTE = """\
These criteria were written for a model that had the skill loaded, and some of their
PASS conditions name the skill's output format (a "## Limits" block, "Ready to
publish", "Breach:" / "Call:" / "Also engaged:" fields, or a reference to SKILL.md).
The response you are judging was not shown that format. Ignore every format
requirement and judge only the substance: did the response reach the conclusion, make
the distinction, or decline in the way the criteria require. Say in your reason that
you did this."""

JUDGE_PROMPT = """\
You are judging one response to an EU medical-device regulation question against
fixed criteria. The criteria were written before this response existed. Apply them as
written: do not substitute your own view of the law, and do not reward a response for
being thorough, well formatted or confident when the criteria ask about something
else. Where the criteria quote statute text, treat that text as authoritative.

{format_note}

<question>
{prompt}
</question>

<criteria>
{criteria}
</criteria>

<response>
{response}
</response>

Reply with JSON only, no other text, in exactly this shape:
{{"pass": true or false, "why": "one to three sentences naming the PASS or FAIL condition that decided it"}}"""

def criteria_for(run):
    if run.get("criteria"):
        return run["criteria"]
    bench = json.loads(BENCH.read_text())
    return {c["id"]: {"text": c["correct_answer_criteria"],
                      "assume_skill_format": c.get("criteria_assume_skill_format", False)}
            for c in bench["cases"]}

def prompts_for(run):
    src = run.get("source") or "benchmark/eu-mdr-bench.json"
    if src.endswith(".json"):
        return {c["id"]: c["prompt"] for c in json.loads(BENCH.read_text())["cases"]}
    return {c["id"]: c["prompt"] for c in rb.probe_cases(ROOT / src)}

def parse_verdict(text):
    m = re.search(r"\{.*\}", text or "", re.S)
    if not m:
        return None
    try:
        v = json.loads(m.group(0))
    except json.JSONDecodeError:
        return None
    if not isinstance(v.get("pass"), bool):
        return None
    return {"pass": v["pass"], "why": str(v.get("why", "")).strip()}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--judge-provider", default="anthropic",
                    choices=["anthropic", "gemini", "vertex", "openai"])
    ap.add_argument("--judge-model", default="claude-opus-5-5")
    ap.add_argument("--judge-effort", default="high",
                    help="thinking level / effort for the judge, recorded in the file")
    ap.add_argument("--rejudge", nargs="*", default=[], metavar="CASE:RUN",
                    help="re-judge these responses even if a verdict exists")
    a = ap.parse_args()

    run_path = Path(a.run)
    run = json.loads(run_path.read_text())
    if a.judge_model == run.get("model"):
        print(f"  refused: {a.judge_model} is the model under test. Use a different judge.")
        return 2
    if a.judge_provider == run.get("provider"):
        print(f"  note: judge and model under test share a provider ({a.judge_provider}). "
              "Allowed, but say so wherever the result is published.")

    key = os.environ.get(rb.KEYS[a.judge_provider]) if a.judge_provider in rb.KEYS else None
    if a.judge_provider in rb.KEYS and not key:
        print(f"  set {rb.KEYS[a.judge_provider]}")
        return 2

    crit = criteria_for(run)
    prompts = prompts_for(run)
    jp = JUDGMENTS / (run_path.stem + ".judgments.json")
    JUDGMENTS.mkdir(parents=True, exist_ok=True)
    out = json.loads(jp.read_text()) if jp.exists() else \
        {"run": run_path.name, "model": run.get("model"), "arm": run.get("arm"),
         "judge": None, "judgments": {}}
    judge_label = f"{a.judge_provider}:{a.judge_model} (effort {a.judge_effort}), judge-benchmark.py"
    if out.get("judge") and out["judge"] != judge_label:
        out["judge"] = f"{out['judge']}; filled by {judge_label}"
    else:
        out["judge"] = judge_label
    rejudge = set(a.rejudge)

    # The judge's own generation settings, reusing the runner's providers.
    ns = argparse.Namespace(max_output_tokens=16384, thinking_level=a.judge_effort,
                            thinking_budget=None)
    done = skipped = failed = 0
    try:
        for r in run["responses"]:
            if not r.get("response"):
                continue
            cid, n = r["case"], str(r["run"])
            slot = out["judgments"].setdefault(cid, {})
            if slot.get(n, {}).get("pass") is not None and f"{cid}:{n}" not in rejudge:
                skipped += 1
                continue
            c = crit.get(cid)
            if not c or cid not in prompts:
                print(f"  {cid} run {n}: no criteria or prompt found, left unjudged")
                failed += 1
                continue
            prompt = JUDGE_PROMPT.format(
                format_note=FORMAT_NOTE if c.get("assume_skill_format") else "",
                prompt=prompts[cid], criteria=c["text"], response=r["response"])
            if a.judge_provider == "anthropic":
                text, err, _ = rb.ask_anthropic(prompt, a.judge_model, key, ns)
            elif a.judge_provider == "gemini":
                text, err, _ = rb.ask_gemini(prompt, a.judge_model, key, ns)
            elif a.judge_provider == "vertex":
                text, err, _ = rb.ask_vertex(prompt, a.judge_model, ns)
            else:
                text, err, _ = rb.ask_openai(prompt, a.judge_model, key, ns)
            v = parse_verdict(text) if not err else None
            if not v:
                print(f"  {cid} run {n}: judge gave no usable verdict ({(err or text or '')[:80]})")
                failed += 1
                continue
            slot[n] = v
            done += 1
            print(f"  {cid} run {n}: {'PASS' if v['pass'] else 'FAIL'}  {v['why'][:90]}")
            jp.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    except rb.QuotaExhausted as e:
        print(f"\n  judge quota exhausted: {str(e)[:120]}. Verdicts so far are saved.")
    jp.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\n  {done} judged, {skipped} kept from before, {failed} left unjudged "
          f"-> {jp.relative_to(ROOT)}")
    print(f"  Score: python3 scripts/score-benchmark.py --score {run_path}")
    print("  Read a sample of the reasons before publishing. A judge is a second model, "
          "not ground truth.")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
