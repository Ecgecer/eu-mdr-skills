#!/usr/bin/env python3
"""Generate the portable artifacts from the canonical skill.

One source of truth: device-claims/skills/device-claims-review/SKILL.md plus its
references/. Everything else in dist/ and GEMINI.md is generated from it, so a
change to the skill cannot silently leave a stale copy behind for Gemini or GPT
users. tests/check-portable-fresh.py fails if it does.

Usage:  python3 scripts/build-portable.py [--check]
        --check exits 1 if any generated file is out of date, writing nothing.
"""
import sys, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "device-claims" / "skills" / "device-claims-review"
SKILL = SKILL_DIR / "SKILL.md"
REFS = ["mdr-ivdr-art7.md", "hwg.md", "uwg.md"]

def strip_frontmatter(text):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5:].lstrip("\n")
    return text

def build_bundle():
    skill_body = strip_frontmatter(SKILL.read_text())
    # The skill points at references/ by relative path. In a single file those
    # paths resolve to nothing, so rewrite them to the in-document headings.
    for r in REFS:
        skill_body = skill_body.replace(f"`references/{r}`", f'the "{r}" section below')
        skill_body = skill_body.replace(f"references/{r}", f'the "{r}" section below')
    # Bare directory mentions name nothing in a single file.
    skill_body = skill_body.replace("`references/`", "the reference texts below")
    skill_body = skill_body.replace("outside `references/`", "outside the reference texts below")
    parts = [
        "# Device Claims Review — single-file bundle",
        "",
        "Everything needed to run a medical device / IVD claims review against",
        "MDR Art. 7, IVDR Art. 7, HWG and UWG. Paste or upload this whole file,",
        "then give it the copy to review.",
        "",
        "GENERATED FILE — do not edit. Source:",
        "device-claims/skills/device-claims-review/. Rebuild with",
        "`python3 scripts/build-portable.py`.",
        "",
        "---",
        "",
        skill_body.rstrip(),
        "",
        "---",
        "",
        "# Reference texts",
        "",
        "Verbatim statute text. Every finding must cite a provision that appears here.",
        "",
    ]
    for r in REFS:
        parts += [f"## {r}", "", (SKILL_DIR / "references" / r).read_text().rstrip(), "", "---", ""]
    return "\n".join(parts).rstrip() + "\n"

def build_gemini():
    return """# GEMINI.md

Device claims review for medical devices and IVDs under MDR Art. 7, IVDR Art. 7,
HWG and UWG.

GENERATED FILE — do not edit. Source: device-claims/skills/device-claims-review/.
Rebuild with `python3 scripts/build-portable.py`.

## Load these, in this order

1. `device-claims/skills/device-claims-review/SKILL.md` — the review procedure
2. `device-claims/skills/device-claims-review/references/mdr-ivdr-art7.md`
3. `device-claims/skills/device-claims-review/references/hwg.md`
4. `device-claims/skills/device-claims-review/references/uwg.md`

Read 1 first. Read 2 before any claim-by-claim pass. Read 3 and 4 when the copy
targets the German market.

If you cannot read files, use `dist/device-claims-review.bundle.md`, which
contains all four in one document.

## Do not skip these

Full list and reasoning in AGENTS.md. The short version:

- Statute text stays verbatim. Findings cite text the reader can re-check.
- `Breach: none` + `Call: Verify` must stay available, or open questions get
  inflated into breaches.
- A limb (c) finding must name a risk from supplied material. Inferring one from
  the device category condemns every benefit-framed advertisement.
- HWG § 11 reaches devices only through nos. 7, 8, 9, 11 and 12.
- No case law. Refuse rather than supplement.
"""

TARGETS = {
    ROOT / "dist" / "device-claims-review.bundle.md": build_bundle,
    ROOT / "GEMINI.md": build_gemini,
}

def main():
    check = "--check" in sys.argv
    stale = []
    for path, fn in TARGETS.items():
        want = fn()
        have = path.read_text() if path.exists() else None
        rel = path.relative_to(ROOT)
        if have == want:
            print(f"  up to date  {rel}")
            continue
        if check:
            stale.append(rel)
            print(f"  STALE       {rel}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(want)
            print(f"  wrote       {rel}  ({len(want)} bytes)")
    if check and stale:
        print(f"\n{len(stale)} generated file(s) out of date. Run: python3 scripts/build-portable.py")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
