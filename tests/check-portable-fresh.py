#!/usr/bin/env python3
"""Fail if a generated artefact is stale, or a reference hides added emphasis.

Two checks, both about the same thing: what this repo publishes must match what it
claims. A drifted bundle means someone reviews against an older rule while the repo says
the text is current. Undeclared bold inside a quoted statute means text labelled verbatim
is not quite verbatim.
"""
import glob, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
failed = 0

# 1. generated artefacts match the canonical skills
r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build-portable.py"), "--check"],
                   capture_output=True, text=True)
print(r.stdout.rstrip())
if r.stderr.strip():
    print(r.stderr.rstrip(), file=sys.stderr)
if r.returncode:
    failed = 1

# 2. added emphasis is declared
#
# Bold inside a quoted passage is editorial. Presented inside text labelled verbatim and
# left undeclared, it is a small dishonesty the rest of this repo's claims cannot afford.
missing = []
for f in sorted(glob.glob(str(ROOT / "*/skills/*/references/*.md"))):
    body = open(f).read()
    quoted = [l for l in body.splitlines() if l.lstrip().startswith(">")]
    if any("**" in l for l in quoted) and "Emphasis added" not in body:
        missing.append(str(Path(f).relative_to(ROOT)))
if missing:
    print("\n  Reference files add emphasis inside quotes without declaring it:")
    for m in missing:
        print(f"    {m}")
    print("  Add the 'Emphasis added.' note, or remove the bold from quoted passages.")
    failed = 1
else:
    print(f"  emphasis declared in every reference that adds it")

# 3. graders must not quote text that is not in their prompt
#
# Three eval prompts were rewritten to remove answer leakage. One grader kept quoting the
# OLD copy -- "just peel, stick, and train" -- so a judge looked for wording the response
# could not contain and failed correct answers for three runs. Invisible until someone
# read a transcript.
#
# Heuristic: a quoted phrase of four or more words in a grader should appear in its own
# prompt, or in a skill or reference file (graders legitimately quote statute). Anything
# else is probably stale.
import glob as _glob
stale = []
for grader in sorted(_glob.glob(str(ROOT / "*/evals/*/graders/*.md"))):
    case_dir = Path(grader).parent.parent
    prompt_f = case_dir / "prompt.md"
    if not prompt_f.exists():
        continue
    corpus = prompt_f.read_text()
    plugin = case_dir.parent.parent
    for extra in list(plugin.glob("skills/*/SKILL.md")) + list(plugin.glob("skills/*/references/*.md")):
        corpus += extra.read_text()
    corpus_n = re.sub(r"\s+", " ", corpus)
    for phrase in re.findall(r'"([^"\n]{20,120})"', open(grader).read()):
        if len(phrase.split()) < 4:
            continue
        if re.sub(r"\s+", " ", phrase) not in corpus_n:
            stale.append((str(Path(grader).relative_to(ROOT)), phrase))
if stale:
    # Advisory, not a gate. Graders legitimately quote model answers and illustrative
    # phrasing, and no heuristic separates those from a stale prompt quote. Printing is
    # enough -- the point is that a human sees the list when a prompt changes.
    print(f"\n  NOTE: {len(stale)} grader quote(s) not found in the prompt or skill.")
    print("  Usually illustrative model answers, which is fine. But if you just rewrote a")
    print("  prompt, check these -- a stale quote makes judges look for wording the")
    print("  response cannot contain, and fails correct answers silently.")
    for g, ph in stale[:8]:
        print(f'    {g.split("/evals/")[-1]:<44} "{ph[:52]}"')
else:
    print("  every grader quote traces to its prompt or the skill")

# 4. every statute-backed skill carries the no-silent-supplement rule
#
# It existed in one skill of four. The three without it answered from memory when a
# question fell outside their references, tagging the output [verify] and calling that
# discipline. A tag is not permission to answer. mdr-transition produced a full set of
# IVDR Article 110 dates that way, on a case whose correct answer was "I do not carry
# that" -- and IVDR is not what it carries.
missing_rule = []
for skill_md in sorted(_glob.glob(str(ROOT / "*/skills/*/SKILL.md"))):
    d = Path(skill_md).parent
    if not (d / "references").is_dir():
        continue                      # domain-general skills carry no statute
    if "No silent supplement" not in open(skill_md).read():
        missing_rule.append(str(Path(skill_md).relative_to(ROOT)))
if missing_rule:
    print("\n  Statute-backed skills without the no-silent-supplement rule:")
    for m in missing_rule:
        print(f"    {m}")
    print("  A [verify] tag is not permission to answer from memory. Add the rule.")
    failed = 1
else:
    print("  every statute-backed skill refuses to supplement from memory")

# 5. the exported benchmark matches the eval cases it is generated from
r2 = subprocess.run([sys.executable, str(ROOT / "scripts" / "export-benchmark.py")],
                    capture_output=True, text=True)
before = (ROOT / "benchmark" / "eu-mdr-bench.json").read_text() if (ROOT / "benchmark" / "eu-mdr-bench.json").exists() else ""
r3 = subprocess.run(["git", "diff", "--quiet", "--", "benchmark/"], cwd=str(ROOT))
if r3.returncode != 0:
    print("\n  benchmark/ is out of date — run: python3 scripts/export-benchmark.py")
    failed = 1
else:
    print("  exported benchmark matches its eval cases")

sys.exit(failed)
