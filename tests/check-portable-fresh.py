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
missing_rule, missing_disclaimer = [], []
for skill_md in sorted(_glob.glob(str(ROOT / "*/skills/*/SKILL.md"))):
    d = Path(skill_md).parent
    if not (d / "references").is_dir():
        continue                      # domain-general skills carry no statute
    body = open(skill_md).read()
    if "No silent supplement" not in body:
        missing_rule.append(str(Path(skill_md).relative_to(ROOT)))
    # The disclaimer has to live in the skill, not only in README.md: dist/*.bundle.md
    # is built to be pasted into a chat on its own, and the README does not travel with
    # it. Matched after collapsing blockquote wrapping, because in device-claims the
    # phrase breaks across "not legal" / "> advice" and a line-wise grep reports a false
    # negative -- which is how this check nearly became a fix for a problem that was not
    # there.
    flat = re.sub(r"\s+", " ", re.sub(r"\s*\n>\s*", " ", body))
    if not re.search(r"not legal( or regulatory)? advice", flat, re.I):
        missing_disclaimer.append(str(Path(skill_md).relative_to(ROOT)))
if missing_rule:
    print("\n  Statute-backed skills without the no-silent-supplement rule:")
    for m in missing_rule:
        print(f"    {m}")
    print("  A [verify] tag is not permission to answer from memory. Add the rule.")
    failed = 1
else:
    print("  every statute-backed skill refuses to supplement from memory")
if missing_disclaimer:
    print("\n  Statute-backed skills without a not-legal-advice line in their Limits:")
    for m in missing_disclaimer:
        print(f"    {m}")
    print("  The bundle is pasted on its own; the README does not travel with it.")
    failed = 1
else:
    print("  every statute-backed skill carries its own disclaimer")

# 5. the exported benchmark matches the eval cases it is generated from
rb = subprocess.run([sys.executable, str(ROOT / "scripts" / "export-benchmark.py"), "--check"],
                    capture_output=True, text=True)
print(rb.stdout.rstrip())
if rb.returncode:
    failed = 1

# 6. the published eval tables match the runs they claim to report
#
# The tables said "generated ... do not hand-edit" and were pasted by hand anyway, so
# three drifted from their own stored evidence: mpdg-germany published +0.47 against a
# stored +0.60, scope-statement +0.22 against +0.11, and two cases where the skill
# measured NEGATIVE were published as +0.00. This also enforces the staleness banner,
# which report-evals.py splices into the same region when a skill was edited after the
# runs it is reporting -- so a reader of the table learns it describes older text.
rt = subprocess.run([sys.executable, str(ROOT / "scripts" / "report-evals.py"),
                     "--check-tables"], capture_output=True, text=True)
print(rt.stdout.rstrip())
if rt.returncode:
    failed = 1

# 7. the worked example either matches the skill that produced it, or says it does not
#
# examples/ is the shop window: it is what someone reads before deciding to install.
# Its transcripts are verbatim and must never be edited -- that promise is the only
# reason they are worth anything -- so the drift is handled by disclosure, not by
# rewriting. The stamp records the skill text they were produced from. The warning is
# required while they differ and forbidden once they match, so regenerating the example
# also clears the notice instead of leaving it to rot.
import types as _types
_re = _types.ModuleType("_re")            # exec the source, not a cached .pyc; on macOS
_p = ROOT / "scripts" / "report-evals.py"  # the cache lives outside the repo entirely
_re.__file__ = str(_p)
exec(compile(_p.read_text(), str(_p), "exec"), _re.__dict__)

ex_readme = ROOT / "examples" / "README.md"
ex_stamp = ROOT / "examples" / ".skill-version.json"
MARK = "produced by an earlier version of the skill"
if ex_stamp.exists() and ex_readme.exists():
    import json as _json
    st = _json.loads(ex_stamp.read_text())
    stale = st.get("sha256") != _re.content_hash(st["plugin"])
    warned = MARK in ex_readme.read_text()
    if stale and not warned:
        print(f"\n  examples/ was produced by a {st['plugin']} version that no longer ships,")
        print("  and README.md does not say so. Regenerate the transcripts and update")
        print("  examples/.skill-version.json, or add the notice. Never edit a transcript.")
        failed = 1
    elif warned and not stale:
        print("\n  examples/ matches the current skill but still carries the staleness")
        print("  notice. Remove the notice from examples/README.md.")
        failed = 1
    else:
        print("  worked example: " + ("current" if not stale else "stale, and says so"))

    # And when it is current, its transcripts must still match the run they cite --
    # otherwise "verbatim, straight from the eval harness" is an assertion, not a fact.
    rex = subprocess.run([sys.executable, str(ROOT / "scripts" / "build-example.py"),
                          "--check"], capture_output=True, text=True)
    if rex.returncode:
        print(rex.stdout.rstrip())
        failed = 1

# 8. a retracted claim must not survive anywhere else
#
# "It escalated a device class on half of a two-part condition in 3 of 3" was retracted
# in CORRECTIONS.md and in the suite's own eval README, and stayed in README.md's opening
# pitch for a day, because retracting a claim where you found it is not retracting it.
# CORRECTIONS.md now registers the exact strings; this refuses to let them come back.
reg = (ROOT / "CORRECTIONS.md").read_text()
retracted = [(p, a, False) for p, a in re.findall(r'<!--\s*retracted:\s*"([^"]+)"\s*(?:\|([^>]*?))?-->', reg)] + \
            [(p, a, True) for p, a in re.findall(r'<!--\s*retracted-re:\s*"([^"]+)"\s*(?:\|([^>]*?))?-->', reg)]
hits = []
for phrase, allow, is_re in retracted:
    allowed = {a.strip() for a in allow.split(",") if a.strip()} if allow else set()
    allowed.add("CORRECTIONS.md")
    for f in sorted(ROOT.rglob("*.md")):
        rel = str(f.relative_to(ROOT))
        if rel in allowed or "/results/" in rel or rel.startswith("dist/"):
            continue
        body = f.read_text()
        # Case-insensitive both ways: the literal register held "escalated a device
        # class ..." and METHOD.md opened a table row with "Escalated", which an exact
        # match walked straight past.
        pat = phrase if is_re else re.escape(phrase)
        found = re.search(pat, body, re.I)
        if found:
            hits.append((rel, phrase))
if hits:
    print("\n  Retracted wording found outside its retraction:")
    for rel, phrase in hits:
        print('    ' + rel + ': ' + repr(phrase))
    print("  A claim withdrawn in CORRECTIONS.md cannot stand anywhere else. Rewrite it,")
    print("  or add the file to that entry's allow list if it is quoting to retract.")
    failed = 1
elif retracted:
    print(f"  {len(retracted)} retracted claim(s) absent outside their retraction")

# 9. every script still parses, and the one nothing else exercises still runs
#
# The other guards call build-portable, export-benchmark, report-evals and
# verify-sources, so a break in those surfaces immediately. run-benchmark.py is called
# by nobody: it is the cross-model runner a contributor reaches for, and it could rot
# unnoticed between uses.
broken = []
for script in sorted((ROOT / "scripts").glob("*.py")):
    try:
        compile(script.read_text(), str(script), "exec")
    except SyntaxError as e:
        broken.append(f"{script.relative_to(ROOT)}: {e}")
rb2 = subprocess.run([sys.executable, str(ROOT / "scripts" / "run-benchmark.py"), "--list"],
                     capture_output=True, text=True)
if rb2.returncode:
    broken.append(f"scripts/run-benchmark.py --list exited {rb2.returncode}: "
                  f"{(rb2.stderr or '').strip()[:200]}")
if broken:
    print("\n  Broken scripts:")
    for b in broken:
        print(f"    {b}")
    failed = 1
else:
    print("  every script parses; run-benchmark --list runs")

# 10. the marketplace lists exactly the plugins that exist
#
# A skill directory that is not in marketplace.json does not install, and an entry
# pointing at a directory that is gone breaks the marketplace for every plugin in it.
# Neither shows up until someone tries to install, which is the worst time to find out.
# This matters most for the skill that does not exist yet: ROADMAP plans a sixth.
import json as _j
mk = ROOT / ".claude-plugin" / "marketplace.json"
if mk.exists():
    listed, problems = {}, []
    for entry in _j.loads(mk.read_text()).get("plugins", []):
        listed[entry["name"]] = entry.get("source", "")
    # parent is .claude-plugin/; the plugin directory is its parent.
    on_disk = {d.parent.parent.name for d in ROOT.glob("*/.claude-plugin/plugin.json")}
    for name in sorted(on_disk - set(listed)):
        problems.append(f"{name}/ has a plugin.json but is not in marketplace.json")
    for name in sorted(set(listed) - on_disk):
        problems.append(f"marketplace.json lists {name}, which has no plugin.json")
    for name, src in sorted(listed.items()):
        if src and not (ROOT / src.lstrip("./")).is_dir():
            problems.append(f"marketplace.json points {name} at {src}, which is not a directory")
        pj = ROOT / name / ".claude-plugin" / "plugin.json"
        if pj.exists() and _j.loads(pj.read_text()).get("name") != name:
            problems.append(f"{name}/plugin.json declares a different name")
    if problems:
        print("\n  Marketplace and plugin directories disagree:")
        for pr in problems:
            print(f"    {pr}")
        failed = 1
    else:
        print(f"  marketplace lists all {len(on_disk)} plugin(s), sources resolve")

# 11. the rules that turn stored runs into published numbers still behave
#
# Every guard above checks that a generated file matches what report-evals.py currently
# produces. Change a rule and the files change with it, and all of them still pass --
# that is a freshness check, not a correctness one. These pin the behaviour: an arm needs
# three surviving runs, and an aborted run must not supersede a real measurement. Both
# rules exist because of a published error.
rl = subprocess.run([sys.executable, str(ROOT / "tests" / "test-report-logic.py")],
                    capture_output=True, text=True)
if rl.returncode:
    print("\n  The reporting rules changed behaviour:")
    out = rl.stdout.strip().splitlines()
    bad = out[out.index("FAILED:") + 1:] if "FAILED:" in out else out[-8:]
    print("\n".join("  " + l for l in bad))
    failed = 1
else:
    n = sum(1 for l in rl.stdout.splitlines() if l.strip().startswith("ok  "))
    print(f"  {n} reporting-logic assertions hold")

# 12. advisory: provisions a skill cites that its references do not carry
#
# Advisory on purpose, and it must stay that way. Declaring a provision in order to put
# it OUT of scope -- "IVDR Article 110 governs this and I do not carry it" -- is the
# behaviour this repo most wants, and it cites a provision the references need not
# contain. A hard failure here would punish the discipline it is meant to protect, the
# same way an over-strict grader failed three correct refusals. It reports; a human
# decides.
unbacked = []
for skill_md in sorted(_glob.glob(str(ROOT / "*/skills/*/SKILL.md"))):
    d = Path(skill_md).parent
    refs = list(d.glob("references/*.md"))
    if not refs:
        continue
    ref_text = "\n".join(r.read_text() for r in refs)
    body = Path(skill_md).read_text()
    cites = set(re.findall(r'§+\s*\d+[a-z]?(?:\(\d+\))?', body))
    cites |= set(re.findall(r'(?:Art\.|Article)\s*\d+[a-z]?(?:\(\d+\))?', body))
    for c in sorted(cites):
        nums = re.findall(r'\d+', c)
        if not nums:
            continue
        if not re.search(rf'(§|Art\.|Article|Artikel)\s*{re.escape(nums[0])}\b', ref_text):
            unbacked.append(f"{d.parent.parent.name}: {re.sub(r'  +', ' ', c)}")
if unbacked:
    print("\n  NOTE: provisions cited in a skill that its references do not mention:")
    for u in unbacked:
        print(f"    {u}")
    print("  Fine when the skill names it to exclude it. Not fine when it is applied as a")
    print("  finding -- the skill would be asserting a rule it cannot cite. Check which.")
else:
    print("  every provision cited in a skill is carried by its references")

# 13. README's install block offers every plugin the marketplace ships
#
# It listed four of five: mdr-transition was installable and undocumented, so the only
# way to find it was to read marketplace.json. An install list is the one part of a
# README a reader copies verbatim rather than reads.
rm_txt = (ROOT / "README.md").read_text()
mk_file = ROOT / ".claude-plugin" / "marketplace.json"
if mk_file.exists():
    import json as _j2
    shipped = {e["name"] for e in _j2.loads(mk_file.read_text()).get("plugins", [])}
    offered = set(re.findall(r'claude plugin install ([a-z0-9-]+)@', rm_txt))
    missing = sorted(shipped - offered)
    extra = sorted(offered - shipped)
    if missing or extra:
        print("\n  README install block and marketplace disagree:")
        for m in missing:
            print(f"    {m} ships but README never offers it")
        for e in extra:
            print(f"    README offers {e}, which the marketplace does not ship")
        failed = 1
    else:
        print(f"  README offers all {len(shipped)} shipped plugin(s)")

# 14. stored results were measured against this working tree, not an installed copy
#
# `claude plugin eval <name>` resolves the name to the INSTALLED plugin and runs that.
# The install is a cache built from a GitHub clone, so it is whatever was last pushed
# and synced -- on 2026-09-17 that cache was 67 commits behind and still carried the
# pre-em-dash text, 13 em dashes where the repo has 1. A run against it would have
# scored text that is not in this repo, and --stamp would then have recorded those
# numbers as describing the current skill. The stamp compares the worktree hash to the
# results timestamp; it never sees which files actually ran.
#
# `claude plugin eval ./<name>` (a path) is the form that measures the repo. This guard
# reads the path each run recorded and refuses a cached one. Paths from the predecessor
# repo (device-claims-review) are working trees too and stay valid.
import json as _j3
cached = []
# A bare-name target writes results to ./evals/results/ at the repo root, which is no
# plugin's eval dir -- report-evals.py never reads it, so the run leaves no trace in any
# published table but does leave that directory behind. Its existence is the tell.
_stray_dir = (ROOT / "evals").is_dir()
for _f in sorted(ROOT.glob("*/evals/results/*/aggregate-result.json")):
    try:
        _plugins = _j3.loads(_f.read_text()).get("suite", {}).get("plugins", [])
    except (ValueError, OSError):
        continue
    for _pl in _plugins:
        _path = _pl.get("path") or ""
        if "/plugins/cache/" in _path or "/plugins/marketplaces/" in _path:
            cached.append(f"{_f.relative_to(ROOT)}: {_path}")
if _stray_dir:
    cached.append("evals/ exists at the repo root. Only a bare-name target creates it, "
                  "and report-evals.py never reads it, so runs land there unnoticed. "
                  "Delete it and re-measure with a path target.")
if cached:
    print("\n  results measured against an INSTALLED plugin, not this repo:")
    for c in cached:
        print(f"    {c}")
    print("  Those numbers describe whatever was last pushed and synced, not the text here.")
    print("  Re-measure with a path target: claude plugin eval ./<plugin> --ablation with-without")
    failed = 1
else:
    _n = len(list(ROOT.glob("*/evals/results/*/aggregate-result.json")))
    print(f"  all {_n} stored run(s) measured a working tree, not an installed copy")

# 15. every documented eval invocation targets a path, not a plugin name
#
# Two ways to get this wrong, both of which happened:
#   `claude plugin eval device-claims`   resolves to the INSTALLED plugin, a cache of the
#                                        last pushed+synced commit. It runs and reports,
#                                        so nothing looks wrong (see 14).
#   `claude plugin eval. --ablation ...` the punctuation rewrite of 2026-09-11 ate the
#                                        space in `eval .`, in CONTRIBUTING twice, ROADMAP
#                                        once and roadmap-probe once. Falls through to
#                                        generic help and runs nothing.
#
# The first version of this guard globbed ROOT/*.md, which is not recursive: it never
# reached */evals/README.md or */roadmap-probe/README.md, so it reported clean while a
# live instance of the bug sat in mpdg-germany/roadmap-probe/README.md. It now recurses.
#
# A bare name is recognised by matching the shipped plugin list rather than by "any word
# that is not a path", so ordinary prose ("run claude plugin eval carefully") is not a
# finding. An f-string placeholder must carry the ./ itself: `{pl}` alone is precisely
# what this guard exists to catch, since that was the defect in report-evals.py.
_SKIP = ("dist", "results", "node_modules", ".git")
_shipped = set()
_mk = ROOT / ".claude-plugin" / "marketplace.json"
if _mk.exists():
    import json as _j4
    _shipped = {e["name"] for e in _j4.loads(_mk.read_text()).get("plugins", [])}

_bad_invocations = []
# This file quotes both broken forms in its own comments and regex, so it is skipped.
_self = Path(__file__).resolve()
_files = [f for f in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.py"))
          if not any(part in _SKIP for part in f.relative_to(ROOT).parts)
          and f.resolve() != _self]
for _f in sorted(_files):
    for _i, _line in enumerate(_f.read_text().splitlines(), 1):
        for _m in re.finditer(r"claude plugin eval(\S*)(.*)$", _line):
            _rel = _f.relative_to(ROOT)
            if _m.group(1):
                _bad_invocations.append(
                    f"{_rel}:{_i}: `eval{_m.group(1)}` -- the space before the path is gone")
                continue
            for _tok in _m.group(2).split():
                _t = _tok.strip("`'\"),.")
                if _t.startswith((".", "/")):
                    break                      # a path target: correct, stop looking
                if _t.startswith("{"):
                    _bad_invocations.append(
                        f"{_rel}:{_i}: `{_t}` is a bare placeholder; emit ./{_t}")
                    break
                if _t in _shipped:
                    _bad_invocations.append(
                        f"{_rel}:{_i}: `{_t}` is a plugin name, which resolves to the "
                        f"installed copy; use ./{_t}")
                    break
if _bad_invocations:
    print("\n  documented eval invocations that do not target this repo:")
    for _b in _bad_invocations:
        print(f"    {_b}")
    failed = 1
else:
    print(f"  every documented eval invocation targets a path ({len(_files)} file(s))")

# 16. no grader justifies a criterion by citing the skill's current wording
#
# scope-statement's criterion 5 read "that is the pinning discipline SKILL.md teaches".
# The skill then reversed position (30b933e taught the opposite, deliberately) and the
# grader was not touched, so for six days it scored responses against a contract the
# skill no longer had. A grader is the independent side of the measurement. The moment
# it defers to the skill's wording, the two can drift apart silently and the delta is
# measuring the drift rather than the skill.
_deferring = []
for _f in sorted(ROOT.rglob("graders/*.md")):
    if any(part in _SKIP for part in _f.relative_to(ROOT).parts):
        continue
    for _i, _line in enumerate(_f.read_text().splitlines(), 1):
        if re.search(r"(SKILL\.md|the skill)\s+(teaches|says|requires|instructs)", _line, re.I):
            _deferring.append(f"{_f.relative_to(ROOT)}:{_i}: {_line.strip()[:90]}")
if _deferring:
    print("\n  grader(s) justifying a criterion by what the skill currently says:")
    for _d in _deferring:
        print(f"    {_d}")
    print("  State the requirement directly. A grader that cites the skill goes stale")
    print("  the moment the skill changes, and nothing fails when it does.")
    failed = 1
else:
    print("  no grader defers to the skill's wording")

sys.exit(failed)
