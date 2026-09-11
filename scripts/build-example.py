#!/usr/bin/env python3
"""Rebuild examples/ from stored eval runs.

examples/ is the shop window: the one place a visitor reads what the skill actually
does before deciding to install. Its transcripts were pasted in by hand on 2026-09-10
and by the next day they demonstrated an Anchor 1 template the skill no longer shipped,
because nothing connected them to the skill that produced them.

They are not edited to fix that. "Both outputs are verbatim, straight from the eval
harness. Neither has been edited" is the only reason they are worth reading, and editing
a transcript to match a changed skill is manufacturing evidence -- the exact failure this
repo exists to prevent. They are regenerated from the stored run instead.

The case is `hwg11-item-scope`, whose prompt is byte-identical to the example's, and
whose contrast is the sharpest in the repo: with the skill the model gets it right in
every run, without it the model cites HWG § 11(1) no. 2 against a device that provision
does not reach, in every run.

Selection rule, stated because a chosen transcript invites the question: the first run of
each arm. Both arms are unanimous -- every with-run passes and every without-run fails --
so there is nothing to cherry-pick. If that ever stops being true this script says so and
refuses, rather than quietly showing the flattering run.

Usage:  python3 scripts/build-example.py [--check]
"""
import hashlib, glob, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN, CASE = "device-claims", "hwg11-item-scope"
EX = ROOT / "examples"


def content_hash(plugin):
    """Same hash report-evals.py stamps with: skill text plus the cases that score it."""
    h = hashlib.sha256()
    for f in sorted(glob.glob(str(ROOT / plugin / "skills/*/SKILL.md")) +
                    glob.glob(str(ROOT / plugin / "skills/*/references/*.md")) +
                    glob.glob(str(ROOT / plugin / "evals/*/prompt.md")) +
                    glob.glob(str(ROOT / plugin / "evals/*/graders/*.md"))):
        h.update(str(Path(f).relative_to(ROOT)).encode())
        h.update(Path(f).read_bytes())
    return h.hexdigest()


def newest_run_with_case():
    for f in sorted(glob.glob(str(ROOT / PLUGIN / "evals/results/*/aggregate-result.json")),
                    reverse=True):
        d = json.loads(Path(f).read_text())
        for c in d.get("cases", []):
            if c["name"] != CASE:
                continue
            arms = {a: [r for r in c["arms"].get(a, []) if not r.get("error")]
                    for a in ("with", "without")}
            if len(arms["with"]) >= 3 and len(arms["without"]) >= 3:
                return Path(f).parent.name, arms
    return None, None


def transcript(run):
    graders = run.get("graders") or [{}]
    return (graders[0].get("evidence") or "").strip()


def main():
    check = "--check" in sys.argv
    stamp = EX / ".skill-version.json"
    ts, arms = newest_run_with_case()
    if not ts:
        print(f"  no stored run has 3 valid runs in both arms for {CASE}")
        return 0 if check else 1

    # Unanimity is what makes "the first run" an honest choice.
    with_scores = [r.get("score") for r in arms["with"]]
    without_scores = [r.get("score") for r in arms["without"]]
    if not (all(s == 1 for s in with_scores) and all(s == 0 for s in without_scores)):
        print(f"  {CASE} is no longer unanimous in {ts}: "
              f"with={with_scores} without={without_scores}")
        print("  Showing one run would be a choice about which to flatter. Pick the case")
        print("  deliberately and record why, or fix the case.")
        return 1

    # The stamp records the text these transcripts came from. Computing it from the
    # current files would make it match by construction, which is the exact failure the
    # stamp exists to catch -- it would certify transcripts produced by older text as
    # current. mtime is exact here: this runs on the machine that stored the run.
    res_mtime = (ROOT / PLUGIN / "evals/results" / ts).stat().st_mtime
    newer = [str(Path(f).relative_to(ROOT))
             for f in glob.glob(str(ROOT / PLUGIN / "skills/*/SKILL.md")) +
                      glob.glob(str(ROOT / PLUGIN / "skills/*/references/*.md")) +
                      glob.glob(str(ROOT / PLUGIN / "evals/*/prompt.md")) +
                      glob.glob(str(ROOT / PLUGIN / "evals/*/graders/*.md"))
             if Path(f).stat().st_mtime > res_mtime]
    if newer:
        # Not an examples/ failure, so --check does not fail on it: the staleness notice
        # is what covers this state, and check-portable-fresh.py already requires it.
        # Only regeneration is refused, because regenerating would stamp transcripts
        # produced by older text as current.
        print(f"  {PLUGIN} was edited after the run these transcripts come from ({ts}):")
        for n in newer[:6]:
            print(f"    {n}")
        print("  examples/ keeps its staleness notice until the suite is re-run.")
        return 0 if check else 1

    prompt = (ROOT / PLUGIN / "evals" / "03-hwg11-item-scope" / "prompt.md").read_text()
    body = prompt.split("---\n", 2)[-1].strip()

    files = {
        EX / "prompt.md": f"# The prompt\n\n{body}\n",
        EX / "with-skill.md": (
            f"# With the skill\n\n"
            f"Verbatim output, unedited. Case `{CASE}`, run 1 of the with-plugin arm, "
            f"stored run `{ts}`.\nAll three runs of this arm scored 1.00.\n\n---\n\n"
            f"{transcript(arms['with'][0])}\n"),
        EX / "without-skill.md": (
            f"# Without the skill\n\n"
            f"Verbatim output, unedited. Same prompt, no plugin loaded. Run 1 of the "
            f"baseline arm,\nstored run `{ts}`. All three runs of this arm scored 0.00.\n\n"
            f"---\n\n{transcript(arms['without'][0])}\n"),
        stamp: json.dumps({
            "plugin": PLUGIN,
            "case": CASE,
            "results": ts,
            "sha256": content_hash(PLUGIN),
            "note": ("Skill and eval text these transcripts were produced from. "
                     "tests/check-portable-fresh.py requires a visible staleness note in "
                     "README.md while this differs from the current text. Regenerate with "
                     "scripts/build-example.py -- never by editing a transcript."),
        }, indent=2) + "\n",
    }

    stale = [p for p, c in files.items() if (not p.exists() or p.read_text() != c)]
    if check:
        for p in stale:
            print(f"  STALE       {p.relative_to(ROOT)}")
        if stale:
            print("  Run: python3 scripts/build-example.py")
            return 1
        print("  worked example matches the stored run it cites")
        return 0
    for p, c in files.items():
        p.write_text(c)
    print(f"  examples/ rebuilt from {ts} ({len(files)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
