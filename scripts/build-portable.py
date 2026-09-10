#!/usr/bin/env python3
"""Generate the portable artifacts from the canonical skills.

DISCOVERS skills rather than listing them. An earlier version hardcoded one skill's
paths; a second plugin was then added and the generated bundle silently kept covering
only the first, while the freshness check reported everything up to date. The guard
that existed to prevent silent drift could not see the drift, because it had been told
what to look at instead of finding it.

Everything under dist/, plus GEMINI.md, is generated. tests/check-portable-fresh.py
fails if any of it is stale or missing.

Usage:  python3 scripts/build-portable.py [--check]
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def discover():
    """Every skill in the repo: (plugin_name, skill_name, skill_dir)."""
    out = []
    for skill_md in sorted(ROOT.glob("*/skills/*/SKILL.md")):
        skill_dir = skill_md.parent
        out.append((skill_dir.parents[1].name, skill_dir.name, skill_dir))
    return out

def strip_frontmatter(text):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5:].lstrip("\n")
    return text

def refs_of(skill_dir):
    d = skill_dir / "references"
    return sorted(p.name for p in d.glob("*.md")) if d.is_dir() else []

def build_bundle(plugin, skill, skill_dir):
    body = strip_frontmatter((skill_dir / "SKILL.md").read_text())
    refs = refs_of(skill_dir)
    for r in refs:
        body = body.replace(f"`references/{r}`", f'the "{r}" section below')
        body = body.replace(f"references/{r}", f'the "{r}" section below')
    body = body.replace("`references/`", "the reference texts below")
    body = body.replace("outside `references/`", "outside the reference texts below")
    parts = [
        f"# {skill} — single-file bundle",
        "",
        f"Plugin `{plugin}`. Everything needed to run this skill in a tool that cannot",
        "read the repo: paste or upload this whole file, then give it your input.",
        "",
        "GENERATED FILE — do not edit. Source:",
        f"{plugin}/skills/{skill}/. Rebuild with `python3 scripts/build-portable.py`.",
        "", "---", "",
        body.rstrip(),
    ]
    if refs:
        parts += ["", "---", "", "# Reference texts", "",
                  "Verbatim statute text. Every finding must cite a provision that appears here.", ""]
        for r in refs:
            parts += [f"## {r}", "", (skill_dir / "references" / r).read_text().rstrip(), "", "---", ""]
    return "\n".join(parts).rstrip() + "\n"

def build_gemini(skills):
    lines = [
        "# GEMINI.md", "",
        "Statute-verified skills for EU medical device regulation.", "",
        "GENERATED FILE — do not edit. Source: the skills listed below.",
        "Rebuild with `python3 scripts/build-portable.py`.", "",
        "## Skills in this repo", "",
    ]
    for plugin, skill, skill_dir in skills:
        lines += [f"### {skill}", "",
                  f"Load `{plugin}/skills/{skill}/SKILL.md` first, then its references:", ""]
        for r in refs_of(skill_dir):
            lines.append(f"- `{plugin}/skills/{skill}/references/{r}`")
        lines += ["", f"If you cannot read files, use `dist/{skill}.bundle.md`, which "
                      "carries the skill and all its references in one document.", ""]
    lines += [
        "## Invariants any port must preserve", "",
        "Full reasoning in AGENTS.md. The short version:", "",
        "- Statute text stays verbatim, with its source and retrieval date.",
        "- A finding must cite a provision that appears in the references.",
        "- Say what is NOT carried. These skills are deliberately partial, and a",
        "  confident answer outside their scope is the failure they are built to avoid.",
        "- Guidance is not the regulation. Name it as guidance or refuse.",
        "- No case law.",
        "",
    ]
    return "\n".join(lines)

def build_agents(skills):
    lines = [
        "# AGENTS.md", "",
        "Cross-tool entry point. This repo's substance is plain markdown and works in any",
        "agent that can read files; the `.claude-plugin/` wrapper is packaging, not content.",
        "",
        "GENERATED FILE — do not edit. Source: the skills listed below.",
        "Rebuild with `python3 scripts/build-portable.py`.", "",
        f"## The {len(skills)} skills", "",
    ]
    for plugin, skill, skill_dir in skills:
        refs = refs_of(skill_dir)
        lines += [f"### {skill}", "",
                  f"`{plugin}/skills/{skill}/SKILL.md`" +
                  (", then its references:" if refs else " — no reference files; it is domain-general."), ""]
        for r in refs:
            lines.append(f"- `{plugin}/skills/{skill}/references/{r}`")
        if refs: lines.append("")
        lines += [f"Single-file version for tools that cannot read the repo: "
                  f"`dist/{skill}.bundle.md`.", ""]
    lines += [
        "## Per-tool", "",
        "**Codex, Cursor, anything reading AGENTS.md** — this file is enough.",
        "",
        "**Gemini CLI** — see `GEMINI.md`.",
        "",
        "**ChatGPT, Gemini web, Claude.ai, any chat with upload** — use the matching",
        "`dist/*.bundle.md`. Each carries one skill and all its references in one document.",
        "",
        "**No file support** — paste the bundle.",
        "",
        "## Invariants any port must preserve", "",
        "These are not stylistic. Dropping one changes what the skill outputs.", "",
        "1. **Statute text stays verbatim**, with source URL and retrieval date. Bold inside",
        "   a quoted passage is added emphasis and is declared as such in every reference.",
        "   `scripts/verify-sources.py` re-fetches and diffs it.",
        "2. **A finding must cite a provision that appears in the references.** Two tiers:",
        "   `[verified]` for what is carried, `[verify]` for everything else.",
        "3. **Refusal is a first-class output.** `Breach: none` + `Call: Verify`, and",
        "   `Also engaged:` for provisions contingent on facts the reviewer lacks. Without",
        "   these an open question gets inflated into a finding.",
        "4. **A finding must name its basis from supplied material.** Inferring a risk from",
        "   the product category condemns every advertisement ever written.",
        "5. **Say what is not carried.** These skills are deliberately partial, and a",
        "   confident answer outside their scope is the failure they exist to prevent.",
        "6. **Guidance is not the regulation, and no case law.** Name it or refuse.",
        "",
        "## Not portable", "",
        "`.claude-plugin/*.json`, the `argument-hint` frontmatter key, and the eval harness",
        "format (`evals/*/prompt.md` + `evals/*/graders/*.md`) are Claude Code specific.",
        "The eval prompts and graders are reusable text even where the harness is not.",
        "",
    ]
    return "\n".join(lines)


def targets():
    skills = discover()
    t = {ROOT / "GEMINI.md": lambda s=skills: build_gemini(s),
         ROOT / "AGENTS.md": lambda s=skills: build_agents(s)}
    for plugin, skill, skill_dir in skills:
        t[ROOT / "dist" / f"{skill}.bundle.md"] = (
            lambda p=plugin, s=skill, d=skill_dir: build_bundle(p, s, d))
    return skills, t

def main():
    check = "--check" in sys.argv
    skills, tgts = targets()
    print(f"  discovered {len(skills)} skill(s): {', '.join(s for _, s, _ in skills)}")
    # a generated bundle with no matching skill is also drift
    stale = []
    expected = {p.name for p in tgts if p.parent.name == "dist"}
    dist = ROOT / "dist"
    if dist.is_dir():
        for orphan in sorted(p for p in dist.glob("*.bundle.md") if p.name not in expected):
            stale.append(orphan.relative_to(ROOT))
            print(f"  ORPHAN      {orphan.relative_to(ROOT)} — no matching skill")
            if not check:
                orphan.unlink(); print(f"  removed     {orphan.relative_to(ROOT)}")
    for path, fn in tgts.items():
        want, rel = fn(), path.relative_to(ROOT)
        have = path.read_text() if path.exists() else None
        if have == want:
            print(f"  up to date  {rel}")
        elif check:
            stale.append(rel); print(f"  STALE       {rel}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(want); print(f"  wrote       {rel}  ({len(want)} bytes)")
    if check and stale:
        print(f"\n{len(stale)} generated file(s) out of date. Run: python3 scripts/build-portable.py")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
