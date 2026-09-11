#!/usr/bin/env python3
"""Unit tests for the two rules that decide every published number.

report-evals.py is the only thing standing between the stored runs and the figures in
README, ROADMAP, METHOD and five eval READMEs. Both of its rules were written in response
to a published error, and both are the kind of thing a later edit could quietly undo:

  MIN_VALID_RUNS  an arm needs three surviving runs or it reports nothing. Averaging
                  whatever survived published fsn-language as +1.00 off one baseline run.
  current()       the newest run that actually scored something. Taking the newest run
                  unconditionally let an aborted run replace two suites' tables with
                  dashes, reporting "unmeasured" where a real measurement existed.

Neither is exercised by the guards, which only check that generated files match what the
script currently produces -- if the rule changes, the files change with it and everything
still passes. These tests pin the behaviour instead of the output.

Usage:  python3 tests/test-report-logic.py
"""
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("re_", ROOT / "scripts" / "report-evals.py")
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)

failures = []


def check(name, got, want):
    if got != want:
        failures.append(f"{name}: got {got!r}, want {want!r}")
    else:
        print(f"  ok  {name}")


def rec(ts, with_score, without_score, n=3):
    """One run's record in the shape load() produces."""
    return {"ts": ts, "arms": {
        "with": {"n": n, "errored": 0, "score": with_score},
        "without": {"n": n, "errored": 0, "score": without_score},
    }}


def arms_from(with_runs, without_runs):
    return {"with": with_runs, "without": without_runs}


def run(case_arms, ts="2026-09-11T00-00-00-000Z"):
    """Write a synthetic results tree and read it back through load()."""
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp) / "plug" / "evals" / "results" / ts
        d.mkdir(parents=True)
        (d / "aggregate-result.json").write_text(json.dumps(
            {"cases": [{"name": "c", "arms": case_arms}]}))
        old_root = R.ROOT
        R.ROOT = Path(tmp)
        try:
            return R.load("plug")["c"][0]["arms"]
        finally:
            R.ROOT = old_root


ok = {"score": 1, "error": None}
bad = {"score": 0, "error": None}
err = {"score": 0, "error": "Credit balance is too low"}

# --- an arm needs MIN_VALID_RUNS surviving runs to report a score -------------------
check("three valid runs score",
      run(arms_from([ok, ok, bad], [bad, bad, bad]))["with"]["score"], 2 / 3)

check("one valid run reports nothing, not its own score",
      run(arms_from([ok, err, err], [bad, bad, bad]))["with"]["score"], None)

check("two valid runs still report nothing",
      run(arms_from([ok, ok, err], [bad, bad, bad]))["with"]["score"], None)

check("errored runs are excluded from the mean, not counted as zero",
      run(arms_from([ok, ok, ok, err], [bad, bad, bad]))["with"]["score"], 1.0)

check("a billing failure is not a skill failure",
      run(arms_from([err, err, err], [bad, bad, bad]))["with"]["score"], None)

check("errored count is reported so the row can be marked",
      run(arms_from([ok, ok, ok, err], [bad, bad, bad]))["with"]["errored"], 1)

# --- current(): the newest run that actually measured something --------------------
complete = rec("2026-09-10 12:00:00", 1.0, 0.0)
aborted = rec("2026-09-11 12:00:00", None, None)
partial = rec("2026-09-11 13:00:00", 1.0, None)

check("an aborted run does not supersede a real measurement",
      R.current([complete, aborted])["ts"], complete["ts"])

check("a run that scored one arm does supersede",
      R.current([complete, partial])["ts"], partial["ts"])

check("newest scorable wins among several",
      R.current([complete, aborted, partial])["ts"], partial["ts"])

check("with nothing scorable anywhere, the newest is still reported",
      R.current([aborted])["ts"], aborted["ts"])

check("a single complete run is itself",
      R.current([complete])["ts"], complete["ts"])

# --- the delta only exists when both arms do ---------------------------------------
both = R.current([rec("2026-09-11 12:00:00", 1.0, 0.0)])
check("both arms measured gives a delta",
      both["arms"]["with"]["score"] - both["arms"]["without"]["score"], 1.0)

one = R.current([rec("2026-09-11 12:00:00", 1.0, None)])
check("one arm unmeasured leaves the other intact",
      (one["arms"]["with"]["score"], one["arms"]["without"]["score"]), (1.0, None))

if failures:
    print("\nFAILED:")
    for f in failures:
        print(f"  {f}")
    sys.exit(1)
print("\nreport-evals logic holds")
sys.exit(0)
