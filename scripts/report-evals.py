#!/usr/bin/env python3
"""Generate the eval results table from stored run data.

This exists because the tables were typed by hand, and hand-typing produced two kinds
of error that a repo making accuracy its whole claim cannot have:

  - arm values inferred from a reported delta rather than observed. `puffery-restraint`
    was published as 1.00 / 0.67 because the harness printed only "mean delta +0.33";
    the stored run says 0.33 / 0.00. Same delta, different arms, and the published
    "All ten score 1.00 with the skill" was false.
  - the most favourable of several runs published without the others. `uwg6-comparison`
    has three stored runs; one was published.

Numbers now come from the JSON. Every run is listed, errored runs are excluded from
scoring and shown separately, and the newest run is marked as current.

Usage:  python3 scripts/report-evals.py [plugin]   # markdown to stdout
"""
import json, glob, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def load(plugin):
    runs = defaultdict(list)
    for f in sorted(glob.glob(str(ROOT / plugin / "evals/results/*/aggregate-result.json"))):
        try: d = json.load(open(f))
        except Exception: continue
        ts = Path(f).parent.name[:19].replace("T", " ")
        for c in d.get("cases", []):
            arms = c.get("arms", {})
            rec = {"ts": ts, "arms": {}}
            for a in ("with", "without"):
                rs = arms.get(a, [])
                ok = [r for r in rs if not r.get("error")]
                rec["arms"][a] = {
                    "n": len(rs), "errored": len(rs) - len(ok),
                    "score": (sum(r.get("score", 0) for r in ok) / len(ok)) if ok else None,
                }
            runs[c["name"]].append(rec)
    return runs

def fmt(v): return "—" if v is None else f"{v:.2f}"

def table(plugin):
    runs = load(plugin)
    if not runs:
        return f"_No stored eval runs for `{plugin}`._\n"
    out = ["| Case | with | without | delta | runs | measured |",
           "|---|---|---|---|---|---|"]
    extra = []
    for name in sorted(runs):
        rs = [r for r in runs[name] if r["arms"]["with"]["n"] >= 3]  # ablation runs only
        rs = rs or runs[name]
        cur = rs[-1]
        w, wo = cur["arms"]["with"]["score"], cur["arms"]["without"]["score"]
        delta = "—" if (w is None or wo is None) else f"{w - wo:+.2f}"
        note = ""
        if cur["arms"]["with"]["errored"] or cur["arms"]["without"]["errored"]:
            note = " ⚠"
        out.append(f"| `{name}` | {fmt(w)} | {fmt(wo)} | **{delta}** | "
                   f"{cur['arms']['with']['n']}×2 | {cur['ts'][:10]}{note} |")
        if len(runs[name]) > 1:
            others = "; ".join(
                f"{r['ts'][:10]} {fmt(r['arms']['with']['score'])}/{fmt(r['arms']['without']['score'])}"
                + (f" ({r['arms']['with']['errored'] + r['arms']['without']['errored']} errored)"
                   if (r['arms']['with']['errored'] or r['arms']['without']['errored']) else "")
                for r in runs[name][:-1])
            extra.append(f"- `{name}` — earlier runs: {others}")
    deltas = []
    for name in sorted(runs):
        rs = [r for r in runs[name] if r["arms"]["with"]["n"] >= 3] or runs[name]
        w, wo = rs[-1]["arms"]["with"]["score"], rs[-1]["arms"]["without"]["score"]
        if w is not None and wo is not None: deltas.append(w - wo)
    if deltas:
        out.append("")
        out.append(f"**Mean delta {sum(deltas)/len(deltas):+.2f}** across {len(deltas)} case(s) "
                   f"with both arms measured.")
    if extra:
        out += ["", "### Every other stored run for these cases", ""] + extra + [
            "", "Listed because publishing only the most favourable run of several is how the "
            "earlier tables went wrong."]
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    plugins = sys.argv[1:] or [p.parent.parent.name for p in
                               sorted(ROOT.glob("*/evals/results"))]
    for p in plugins:
        print(f"\n## {p}\n")
        print(table(p))
