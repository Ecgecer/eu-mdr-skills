# AGENTS.md

Cross-tool entry point. This repo's substance is plain markdown and works in any
agent that can read files; the `.claude-plugin/` wrapper is packaging, not content.

GENERATED FILE — do not edit. Source: the skills listed below.
Rebuild with `python3 scripts/build-portable.py`.

## The 4 skills

### device-claims-review

`device-claims/skills/device-claims-review/SKILL.md`, then its references:

- `device-claims/skills/device-claims-review/references/hwg.md`
- `device-claims/skills/device-claims-review/references/mdr-ivdr-art7.md`
- `device-claims/skills/device-claims-review/references/uwg.md`

Single-file version for tools that cannot read the repo: `dist/device-claims-review.bundle.md`.

### software-classification

`mdr-classification/skills/software-classification/SKILL.md`, then its references:

- `mdr-classification/skills/software-classification/references/annex-viii-software.md`

Single-file version for tools that cannot read the repo: `dist/software-classification.bundle.md`.

### german-additions

`mpdg-germany/skills/german-additions/SKILL.md`, then its references:

- `mpdg-germany/skills/german-additions/references/mpdg.md`

Single-file version for tools that cannot read the repo: `dist/german-additions.bundle.md`.

### scope-statement

`scope-statement/skills/scope-statement/SKILL.md` — no reference files; it is domain-general.

Single-file version for tools that cannot read the repo: `dist/scope-statement.bundle.md`.

## Per-tool

**Codex, Cursor, anything reading AGENTS.md** — this file is enough.

**Gemini CLI** — see `GEMINI.md`.

**ChatGPT, Gemini web, Claude.ai, any chat with upload** — use the matching
`dist/*.bundle.md`. Each carries one skill and all its references in one document.

**No file support** — paste the bundle.

## Invariants any port must preserve

These are not stylistic. Dropping one changes what the skill outputs.

1. **Statute text stays verbatim**, with source URL and retrieval date. Bold inside
   a quoted passage is added emphasis and is declared as such in every reference.
   `scripts/verify-sources.py` re-fetches and diffs it.
2. **A finding must cite a provision that appears in the references.** Two tiers:
   `[verified]` for what is carried, `[verify]` for everything else.
3. **Refusal is a first-class output.** `Breach: none` + `Call: Verify`, and
   `Also engaged:` for provisions contingent on facts the reviewer lacks. Without
   these an open question gets inflated into a finding.
4. **A finding must name its basis from supplied material.** Inferring a risk from
   the product category condemns every advertisement ever written.
5. **Say what is not carried.** These skills are deliberately partial, and a
   confident answer outside their scope is the failure they exist to prevent.
6. **Guidance is not the regulation, and no case law.** Name it or refuse.

## Not portable

`.claude-plugin/*.json`, the `argument-hint` frontmatter key, and the eval harness
format (`evals/*/prompt.md` + `evals/*/graders/*.md`) are Claude Code specific.
The eval prompts and graders are reusable text even where the harness is not.
