# AGENTS.md

Cross-tool entry point. This repo's substance is plain markdown and works in any
agent that can read files; the `.claude-plugin/` wrapper is packaging, not content.

## What to load

| File | Role |
|---|---|
| `device-claims/skills/device-claims-review/SKILL.md` | The review procedure. Load this first. |
| `.../references/mdr-ivdr-art7.md` | Verbatim MDR Art. 7 / IVDR Art. 7 |
| `.../references/hwg.md` | Verbatim HWG § 1(1) no. 1a, § 3, § 3a, § 11 |
| `.../references/uwg.md` | Verbatim UWG § 5, § 6 |

The skill references the three files by relative path from its own directory. Keep
them colocated and any tool that can open a relative path will resolve them.

## Using it outside Claude Code

**Codex / Cursor / any agent that reads AGENTS.md** — this file is enough; the agent
will follow the table above.

**Gemini, ChatGPT, or any chat with file upload** — upload all four files and say:
"Follow SKILL.md. Review the copy below." The skill is self-contained: it names the
two anchors it needs (intended purpose as assessed, and audience) and asks for them.

**No file support at all** — paste `SKILL.md` followed by the reference file for the
layer you need. MDR-only review needs `mdr-ivdr-art7.md`. German-market review needs
all three.

## Invariants any port must preserve

These are not stylistic. Dropping one changes what the skill outputs.

1. **Statute text stays verbatim.** The references carry source URL and retrieval date
   (EUR-Lex and gesetze-im-internet, 2026-09-09). Do not paraphrase them into the
   skill body — the whole claim of this repo is that findings cite text a reader can
   re-check against a free primary source.
2. **`Breach: none` + `Call: Verify` must remain available.** Without it the skill
   inflates open questions into breaches. This was an observed failure, see
   `device-claims/evals/README.md`.
3. **Limb (c) findings must name a risk from supplied material.** Inferring a likely
   risk from the device category condemns every benefit-framed advertisement.
4. **HWG § 11 applies to devices only via nos. 7, 8, 9, 11 and 12.** The restriction
   is one sentence at the end of § 11(1). Citing no. 2 against a device is wrong.
5. **No case law.** The skill refuses rather than supplements. Statute verifies for
   free; case law does not.

## Not portable

`.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, the `argument-hint`
frontmatter key, and `device-claims/evals/**/case.yaml` are Claude Code specific.
Everything else is tool-neutral. The eval *prompts and graders* are reusable text even
where the harness is not.
