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

A published number describes the skill text that produced it. Edit the skill and the
number silently becomes a claim about something that no longer exists -- which happened
here: mdr-transition was trimmed at 00:59 on 2026-09-11 while its published +0.07 table
was measured the evening before. --stamp records which content a measurement describes,
--check-stamps fails when they diverge. Timestamps cannot do this job: the honest
workflow is edit, measure, commit, so the commit is always newer than the measurement.

Usage:  python3 scripts/report-evals.py [plugin]   # markdown to stdout
        python3 scripts/report-evals.py --stamp    # record what the numbers describe
        python3 scripts/report-evals.py --check-stamps
"""
import hashlib, json, glob, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIN_VALID_RUNS = 3      # "three runs per case -- single runs are not evidence"

def plugins():
    """Discovered, not listed -- a hardcoded list goes stale the day a skill is added."""
    return sorted({Path(f).parents[2].name
                   for f in glob.glob(str(ROOT / "*/skills/*/SKILL.md"))})

def content_hash(plugin):
    """Hash of every byte of skill text the evals exercise, path included so that
    renaming or splitting a reference counts as a change."""
    h = hashlib.sha256()
    files = sorted(glob.glob(str(ROOT / plugin / "skills/*/SKILL.md")) +
                   glob.glob(str(ROOT / plugin / "skills/*/references/*.md")))
    if not files:
        return None
    for f in files:
        h.update(str(Path(f).relative_to(ROOT)).encode())
        h.update(Path(f).read_bytes())
    return h.hexdigest()

def newest_results(plugin):
    ds = sorted(glob.glob(str(ROOT / plugin / "evals/results/*/aggregate-result.json")))
    return Path(ds[-1]).parent.name if ds else None

def stamp_path(plugin):
    return ROOT / plugin / "evals" / "measured-content.json"

def do_stamp(names=None, force=False):
    """Record that a measurement describes the current skill text.

    Refuses when a skill file is newer on disk than the results it would be stamped
    against, because that is the error this whole mechanism exists to catch: stamping
    blesses the numbers, and blessing an edit you have not measured publishes a claim
    about text that was never run. mtime is unreliable across clones but exact here --
    this runs on the machine that just executed the eval. The hash is what travels.
    """
    bad = 0
    for pl in (names or plugins()):
        res = newest_results(pl)
        if not res:
            continue
        res_mtime = (ROOT / pl / "evals/results" / res).stat().st_mtime
        newer = [str(Path(f).relative_to(ROOT))
                 for f in glob.glob(str(ROOT / pl / "skills/*/SKILL.md")) +
                          glob.glob(str(ROOT / pl / "skills/*/references/*.md"))
                 if Path(f).stat().st_mtime > res_mtime]
        if newer and not force:
            print(f"  {pl}: REFUSED -- edited after the run it would be stamped against:")
            for n in newer:
                print(f"    {n}")
            print(f"    Re-measure first. Use --force only if the edit cannot change")
            print(f"    behaviour (whitespace, a comment), and say so in the commit.")
            bad = 1; continue
        stamp_path(pl).parent.mkdir(parents=True, exist_ok=True)
        stamp_path(pl).write_text(json.dumps(
            {"results": res, "sha256": content_hash(pl)}, indent=2) + "\n")
        print(f"  stamped {pl} -> {res}")
    return bad

START, END = "<!-- report-evals:start -->", "<!-- report-evals:end -->"

def readme_path(plugin):
    return ROOT / plugin / "evals" / "README.md"

def splice(plugin):
    """Return the eval README with its generated region replaced, or None if unmarked.

    The tables said "generated ... do not hand-edit" and were then pasted by hand, so
    three of them drifted from the runs they claimed to report -- mpdg-germany published
    +0.47 against a stored +0.60, scope-statement +0.22 against +0.11. Generated now
    means generated.
    """
    f = readme_path(plugin)
    if not f.exists():
        return None
    txt = f.read_text()
    if START not in txt or END not in txt:
        return None
    head, rest = txt.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n{table(plugin).rstrip()}\n{END}{tail}"

def do_write():
    for pl in plugins():
        new = splice(pl)
        if new is None:
            print(f"  {pl}: no markers in evals/README.md, skipped"); continue
        f = readme_path(pl)
        if f.read_text() == new:
            print(f"  {pl}: already current")
        else:
            f.write_text(new); print(f"  {pl}: table rewritten from stored runs")
    return 0

def do_check_tables():
    bad = 0
    for pl in plugins():
        new = splice(pl)
        if new is None:
            print(f"  {pl}: evals/README.md has no generation markers"); bad = 1; continue
        if readme_path(pl).read_text() != new:
            print(f"  {pl}: published table does not match the stored runs it cites.")
            print(f"    Run `python3 scripts/report-evals.py --write`.")
            bad = 1
        else:
            print(f"  {pl}: published table matches the stored runs")
    return bad

def do_check():
    bad = 0
    for pl in plugins():
        if not newest_results(pl):
            continue                      # nothing measured yet, nothing to contradict
        sp = stamp_path(pl)
        if not sp.exists():
            print(f"  {pl}: has results but no stamp -- run report-evals.py --stamp")
            bad = 1; continue
        want = json.loads(sp.read_text()).get("sha256")
        if want != content_hash(pl):
            print(f"  {pl}: skill text changed since it was measured.")
            print(f"    The published table describes the old text. Re-measure with")
            print(f"    `claude plugin eval {pl} --ablation with-without`, then --stamp.")
            bad = 1
        else:
            print(f"  {pl}: numbers describe the current skill text")
    return bad

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
                    # An arm needs MIN_VALID_RUNS surviving runs to report a score.
                    # Averaging whatever survived published mpdg-germany's fsn-language
                    # as +1.00 off a single baseline run, in a repo whose stated rule is
                    # that single runs are not evidence. Below the threshold the arm is
                    # unmeasured, which is not the same as zero.
                    "score": (sum(r.get("score", 0) for r in ok) / len(ok))
                             if len(ok) >= MIN_VALID_RUNS else None,
                }
            runs[c["name"]].append(rec)
    return runs

def fmt(v): return "—" if v is None else f"{v:.2f}"

def stale_banner(plugin):
    """A line in the table itself when the skill text moved after it was measured.

    CI colour is for maintainers. Someone reading the published table needs to know
    from the table whether it describes the skill they are about to install.
    """
    if not newest_results(plugin):
        return []
    sp = stamp_path(plugin)
    if sp.exists() and json.loads(sp.read_text()).get("sha256") == content_hash(plugin):
        return []
    return ["> ⚠ **The skill text changed after these runs.** The numbers below describe",
            "> the earlier text, not what this plugin currently ships. Re-measure with",
            f"> `claude plugin eval {plugin} --ablation with-without`.", ""]

def current(case_runs):
    """The newest run that actually measured something.

    A run aborted partway leaves every case after the failure with zero valid runs, and
    such a run carries no information. Letting it supersede a complete earlier run
    replaced a whole suite's table with dashes when a re-measure died on billing.
    Staleness is the banner's job -- it says when the text moved. It is not a reason to
    throw away the last real measurement.
    """
    rs = [r for r in case_runs if r["arms"]["with"]["n"] >= MIN_VALID_RUNS] or case_runs
    scored = [r for r in rs if r["arms"]["with"]["score"] is not None
                            or r["arms"]["without"]["score"] is not None]
    return (scored or rs)[-1]

def table(plugin):
    runs = load(plugin)
    if not runs:
        return f"_No stored eval runs for `{plugin}`._\n"
    out = stale_banner(plugin) + [
           "| Case | with | without | delta | runs | measured |",
           "|---|---|---|---|---|---|"]
    extra = []
    for name in sorted(runs):
        cur = current(runs[name])
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
                for r in runs[name] if r is not cur)
            extra.append(f"- `{name}` — earlier runs: {others}")
    deltas = []
    for name in sorted(runs):
        cur = current(runs[name])
        w, wo = cur["arms"]["with"]["score"], cur["arms"]["without"]["score"]
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
    args = sys.argv[1:]
    if "--stamp" in args:
        force = "--force" in args
        names = [a for a in args if not a.startswith("--")]
        sys.exit(do_stamp(names or None, force))
    if "--check-stamps" in args:
        sys.exit(do_check())
    if "--write" in args:
        sys.exit(do_write())
    if "--check-tables" in args:
        sys.exit(do_check_tables())
    names = args or [d.parent.parent.name for d in sorted(ROOT.glob("*/evals/results"))]
    for name in names:
        print(f"\n## {name}\n")
        print(table(name))
