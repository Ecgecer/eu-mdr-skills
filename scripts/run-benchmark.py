#!/usr/bin/env python3
"""Run eu-mdr-bench against a model that is not Claude, and save the responses.

The benchmark's measured column comes from one model. That makes it a report, not a
benchmark. This sends every case prompt to another provider and stores the raw answers
so they can be judged with the same criteria.

Judging is a separate step on purpose: mixing generation and scoring in one pass is how
you end up unable to tell a model failure from a grader failure.

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
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
           f"?key={key}")
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": 4096, "temperature": 1}}
    d, err = post(url, body, {})
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

def ask_openai(prompt, model, key):
    d, err = post("https://api.openai.com/v1/chat/completions",
                  {"model": model, "messages": [{"role":"user","content":prompt}]},
                  {"Authorization": f"Bearer {key}"})
    if err: return None, err
    try: return d["choices"][0]["message"]["content"], None
    except Exception: return None, f"unexpected shape: {json.dumps(d)[:200]}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["gemini","vertex","openai"])
    ap.add_argument("--model", default="gemini-2.5-pro")
    ap.add_argument("--runs", type=int, default=3,
                    help="runs per case; 3 is the minimum that is evidence")
    ap.add_argument("--case", help="only this case id")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    bench = json.loads(BENCH.read_text())
    cases = bench["cases"]
    if a.case: cases = [c for c in cases if c["id"] == a.case]
    if a.list:
        for c in bench["cases"]:
            m = c.get("measured") or {}
            print(f"  {c['id']:<34} {c['area']:<20} claude_baseline="
                  f"{m.get('baseline_pass_rate','—')}")
        return 0
    if not a.provider:
        ap.error("--provider is required unless --list")

    key = os.environ.get("GEMINI_API_KEY") if a.provider=="gemini" else \
          os.environ.get("OPENAI_API_KEY") if a.provider=="openai" else None
    if a.provider in ("gemini","openai") and not key:
        print(f"  set {'GEMINI_API_KEY' if a.provider=='gemini' else 'OPENAI_API_KEY'}")
        return 2

    RUNS.mkdir(parents=True, exist_ok=True)
    out = {"model": a.model, "provider": a.provider, "runs_per_case": a.runs,
           "started": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "responses": []}
    for i, c in enumerate(cases, 1):
        for r in range(a.runs):
            if a.provider == "gemini":   text, err = ask_gemini(c["prompt"], a.model, key)
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
    return 0

if __name__ == "__main__":
    sys.exit(main())
