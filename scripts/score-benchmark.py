#!/usr/bin/env python3
"""Score stored benchmark responses against each case's criteria, from recorded judgments.

Generation and judging are separate steps on purpose: mixing them is how you end up
unable to tell a model failure from a grader failure. `run-benchmark.py` stores raw
answers; this scores them from a judgments file that a human (or a model that is not the
one under test) has filled in.

The judgments file is the point. A verdict that lives only in a conversation is an
assertion; a verdict with a per-response reason in the repo is something a reader can
disagree with. Every response must be judged before a table is produced -- a missing
judgment is an error, not a zero, for the same reason an errored run is not a failed run.

Usage:
  python3 scripts/score-benchmark.py --emit <run.json>     # blank judgments skeleton
  python3 scripts/score-benchmark.py --score <run.json> [<run2.json> ...]
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "benchmark" / "eu-mdr-bench.json"
JUDGMENTS = ROOT / "benchmark" / "judgments"


def criteria():
    return {c["id"]: c["correct_answer_criteria"] for c in json.loads(BENCH.read_text())["cases"]}


def judgment_path(run_file):
    return JUDGMENTS / (Path(run_file).stem + ".judgments.json")


def emit(run_file):
    d = json.loads(Path(run_file).read_text())
    out = {"run": Path(run_file).name, "model": d.get("model"), "arm": d.get("arm"),
           "judge": None, "judgments": {}}
    for r in d["responses"]:
        if not r.get("response"):
            continue
        out["judgments"].setdefault(r["case"], {})[str(r["run"])] = {"pass": None, "why": ""}
    JUDGMENTS.mkdir(parents=True, exist_ok=True)
    p = judgment_path(run_file)
    p.write_text(json.dumps(out, indent=2) + "\n")
    n = sum(len(v) for v in out["judgments"].values())
    print(f"  wrote {p.relative_to(ROOT)} — {n} response(s) awaiting judgment")
    return 0


def score(run_files):
    arms, problems = {}, []
    for rf in run_files:
        d = json.loads(Path(rf).read_text())
        jp = judgment_path(rf)
        if not jp.exists():
            problems.append(f"{Path(rf).name}: no judgments file; run --emit first")
            continue
        j = json.loads(jp.read_text())
        if not j.get("judge"):
            problems.append(f"{jp.name}: 'judge' is unset — say who or what scored these")
        arm = d.get("arm") or "baseline"
        for r in d["responses"]:
            got = j["judgments"].get(r["case"], {}).get(str(r["run"]))
            if not r.get("response"):
                continue                      # errored generation: excluded, not zero
            if not got or got.get("pass") is None:
                problems.append(f"{Path(rf).name}: {r['case']} run {r['run']} unjudged")
                continue
            arms.setdefault(arm, {}).setdefault(r["case"], []).append(bool(got["pass"]))
    if problems:
        print("  Cannot score:")
        for p in problems[:20]:
            print(f"    {p}")
        return 1

    cases = sorted(set().union(*(set(v) for v in arms.values())) if arms else [])
    print(f"| Case | {' | '.join(sorted(arms))} | delta |")
    print("|---" * (len(arms) + 2) + "|")
    means = {a: [] for a in arms}
    deltas = []
    for c in cases:
        cells, vals = [], {}
        for a in sorted(arms):
            runs = arms[a].get(c, [])
            if len(runs) < 3:
                cells.append(f"— ({len(runs)} runs)")
                vals[a] = None
            else:
                v = sum(runs) / len(runs)
                cells.append(f"{v:.2f}")
                vals[a] = v
                means[a].append(v)
        if vals.get("baseline") is not None and vals.get("with-skill") is not None:
            dl = vals["with-skill"] - vals["baseline"]
            deltas.append(dl)
            cells.append(f"**{dl:+.2f}**")
        else:
            cells.append("—")
        print(f"| `{c}` | {' | '.join(cells)} |")
    print()
    for a in sorted(arms):
        if means[a]:
            print(f"  {a}: mean {sum(means[a])/len(means[a]):.2f} over {len(means[a])} case(s)")
    if deltas:
        print(f"  **mean delta {sum(deltas)/len(deltas):+.2f}** over {len(deltas)} case(s) "
              f"with both arms at three or more judged runs")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", metavar="RUN")
    ap.add_argument("--score", nargs="+", metavar="RUN")
    a = ap.parse_args()
    if a.emit:
        return emit(a.emit)
    if a.score:
        return score(a.score)
    ap.error("--emit or --score")


if __name__ == "__main__":
    sys.exit(main())
