# GEMINI.md

Statute-verified skills for EU medical device regulation.

GENERATED FILE — do not edit. Source: the skills listed below.
Rebuild with `python3 scripts/build-portable.py`.

## Skills in this repo

### device-claims-review

Load `device-claims/skills/device-claims-review/SKILL.md` first, then its references:

- `device-claims/skills/device-claims-review/references/hwg.md`
- `device-claims/skills/device-claims-review/references/mdr-ivdr-art7.md`
- `device-claims/skills/device-claims-review/references/uwg.md`

If you cannot read files, use `dist/device-claims-review.bundle.md`, which carries the skill and all its references in one document.

### software-classification

Load `mdr-classification/skills/software-classification/SKILL.md` first, then its references:

- `mdr-classification/skills/software-classification/references/annex-viii-software.md`

If you cannot read files, use `dist/software-classification.bundle.md`, which carries the skill and all its references in one document.

### german-additions

Load `mpdg-germany/skills/german-additions/SKILL.md` first, then its references:

- `mpdg-germany/skills/german-additions/references/mpdg.md`

If you cannot read files, use `dist/german-additions.bundle.md`, which carries the skill and all its references in one document.

### scope-statement

Load `scope-statement/skills/scope-statement/SKILL.md` first, then its references:


If you cannot read files, use `dist/scope-statement.bundle.md`, which carries the skill and all its references in one document.

## Invariants any port must preserve

Full reasoning in AGENTS.md. The short version:

- Statute text stays verbatim, with its source and retrieval date.
- A finding must cite a provision that appears in the references.
- Say what is NOT carried. These skills are deliberately partial, and a
  confident answer outside their scope is the failure they are built to avoid.
- Guidance is not the regulation. Name it as guidance or refuse.
- No case law.
