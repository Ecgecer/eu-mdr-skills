#!/usr/bin/env python3
"""Export the measured figures a published guide needs, as JSON.

A guide that retypes these numbers goes stale the moment anything is re-measured, and
this repo has already published three wrong figures that way. Linking to the tables
instead is worse in a different direction: almost nobody clicks through, so the evidence
never reaches the reader it was written for.

So the guide renders from this file, and the consuming site fails its build when the
file drifts from the runs it claims to describe. Same contract as facts.json.

Usage:
  python3 scripts/export-guide-data.py                      # print to stdout
  python3 scripts/export-guide-data.py --out <path.json>    # write it
"""
import argparse
import json
import sys
import types
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

_m = types.ModuleType("report_evals")
_m.__file__ = str(ROOT / "scripts" / "report-evals.py")
exec(compile((ROOT / "scripts" / "report-evals.py").read_text(),
             str(ROOT / "scripts" / "report-evals.py"), "exec"), _m.__dict__)

# Reader-facing labels. The plugin names mean nothing to a regulatory audience, and the
# guide should not be the place where someone learns our directory structure.
SUITE_LABEL = {
    "device-claims": "Marketing copy under MDR/IVDR Art. 7, HWG and UWG",
    "mpdg-germany": "German national additions to MDR",
    "scope-statement": "Bounding what a compliance check actually establishes",
    "mdr-classification": "Software classification under Annex VIII",
    "mdr-transition": "Legacy device transition under Art. 120 as amended",
}


def collect():
    suites, cases, versions = [], [], set()
    zeros = both_perfect = 0
    for pl in _m.plugins():
        runs = _m.load(pl)
        deltas = []
        for name, rs in sorted(runs.items()):
            cur = _m.current(rs)
            w, o = cur["arms"]["with"], cur["arms"]["without"]
            if w["score"] is None or o["score"] is None:
                continue
            d = w["score"] - o["score"]
            deltas.append(d)
            versions.add(cur.get("ver") or "unknown")
            if abs(d) < 0.01:
                zeros += 1
                if w["score"] > 0.99 and o["score"] > 0.99:
                    both_perfect += 1
            cases.append({
                "suite": pl, "case": name,
                "with": round(w["score"], 2), "without": round(o["score"], 2),
                "delta": round(d, 2), "runsPerArm": w["n"],
                "cli": cur.get("ver") or "unknown", "measured": cur["ts"][:10],
            })
        if deltas:
            suites.append({
                "suite": pl, "label": SUITE_LABEL.get(pl, pl),
                "delta": round(sum(deltas) / len(deltas), 2), "cases": len(deltas),
            })
    suites.sort(key=lambda s: -s["delta"])
    return suites, cases, sorted(versions), zeros, both_perfect


def cross_model():
    """The inversion rows, read from the stored probe runs rather than retyped."""
    rows = []
    for pl in _m.plugins():
        probe = sorted((ROOT / pl / "evals" / "model-probes").glob("*/aggregate-result.json")) \
            if (ROOT / pl / "evals" / "model-probes").is_dir() else []
        if not probe:
            continue
        d = json.loads(probe[-1].read_text())
        default_runs = _m.load(pl)
        for c in d.get("cases", []):
            def mean(arm, src):
                v = [r.get("score") for r in src.get(arm, []) if not r.get("error")]
                return sum(v) / len(v) if v else None
            h_w, h_o = mean("with", c["arms"]), mean("without", c["arms"])
            if h_w is None or h_o is None or c["name"] not in default_runs:
                continue
            cur = _m.current(default_runs[c["name"]])
            d_w, d_o = cur["arms"]["with"]["score"], cur["arms"]["without"]["score"]
            if d_w is None or d_o is None:
                continue
            rows.append({
                "suite": pl, "case": c["name"],
                "defaultDelta": round(d_w - d_o, 2),
                "haikuDelta": round(h_w - h_o, 2),
            })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    a = ap.parse_args()
    suites, cases, versions, zeros, both_perfect = collect()
    payload = {
        "_generated": {
            "by": "eu-mdr-skills/scripts/export-guide-data.py",
            "from": "*/evals/results/*/aggregate-result.json",
            "note": "Do not edit by hand. Regenerate with "
                    "`python3 scripts/export-guide-data.py --out <path>` in the "
                    "eu-mdr-skills repo.",
            "at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        },
        "cliVersions": versions,
        "totalCases": len(cases),
        "zeroCases": zeros,
        "zeroCasesWhereBothArmsPerfect": both_perfect,
        "casesAtNineRuns": sum(1 for c in cases if c["runsPerArm"] >= 9),
        "suites": suites,
        "cases": cases,
        "crossModel": cross_model(),
    }
    text = json.dumps(payload, indent=2) + "\n"
    if a.out:
        Path(a.out).write_text(text)
        print(f"  wrote {a.out}: {len(cases)} case(s), {len(suites)} suite(s), "
              f"CLI {', '.join(versions)}")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
