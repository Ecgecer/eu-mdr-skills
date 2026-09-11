# scope-statement — single-file bundle

Plugin `scope-statement`. Everything needed to run this skill in a tool that cannot
read the repo: paste or upload this whole file, then give it your input.

GENERATED FILE — do not edit. Source:
scope-statement/skills/scope-statement/. Rebuild with `python3 scripts/build-portable.py`.

---

# Scope Statement

A compliance result is read as broader than it is. "Validation passed" becomes "we are
compliant". "Ready to submit" becomes "this will be accepted". The gap between what a
check covered and what a reader infers from it is where the damage happens, and it is
almost never stated.

This produces the block that closes that gap. It is domain-general: use it on an MDR
readiness result, a GDPR assessment, a security scan, a QMS gap analysis, anything that
returns a verdict someone will act on.

---

## The block

```markdown
## Scope of this check

**Checked:** [what was actually evaluated, in the reader's terms]
**Against:** [the rules, schema or version, with source and date]
**Not checked:** [named, specific, and the ones a reader would assume were]
**This does not establish:** [the inference a reader will draw and must not]
**Valid as of:** [date, and what would invalidate it]
```

The last two lines carry the weight. The others are description.

---

## How to fill it

### Checked

Say what was evaluated, not what the tool is called. "Every field flagged mandatory by
the current EUDAMED schema was present and non-empty" is a scope. "Ran validation" is
not.

If the check sampled rather than covered, say the sample.

### Against

Name the authority and pin it. A rule set has a version and a date; a schema has both;
guidance has an issue number. "Against MDR Annex I" is weaker than "Against the 23 GSPR
of MDR Annex I, EUR-Lex consolidated text retrieved 2026-09-09".

If part of the basis is the tool's own opinion rather than a published rule, say which
part. That is the line readers most want and least often get.

### Not checked

**This is the one that earns the block.** Two categories, and both belong:

1. **Deliberate exclusions** — what the check was never designed to cover.
2. **What a reader would reasonably assume was covered and wasn't.** Harder, more
   valuable. If the check validates field presence but not field *correctness*, a
   reader who sees "passed" believes their data is right. Say so.

Be specific. "Other requirements may apply" is not a scope statement, it is a
disclaimer. "Clinical evaluation, PMS planning and labelling artwork were not assessed"
is a scope statement.

### This does not establish

Write the sentence a reader would say to their boss, and negate it. If they would say
"we're compliant", write "This does not establish compliance with [regulation]." If
they would say "we can submit", write "This does not establish that a submission will
be accepted."

One or two lines. Blunt, in plain language, no hedging verbs.

### Valid as of

A date, plus what would invalidate it: the rules changing, the data changing, the
intended purpose changing. A scope statement with no expiry gets quoted a year later.

---

## Workflow

1. **Read the result.** Identify the verdict a reader will take away, in their words.
2. **Find the gap.** What did the check actually do, and what will the reader believe it
   did? The distance between those is the block's content.
3. **Name the gap in prose; never leave a blank.** If the basis, version or coverage is
   not established, write the line with what is actually true and say plainly what is
   missing:

   > **Against:** our own pattern set and name dictionary, version not supplied — not an
   > external standard.

   That is a finished sentence claiming no authority it cannot support. A bracket —
   `[pattern set version + date — fill this in]` — is an unfinished document: asked for a
   scope statement, the reader gets a form to complete. Deliver the block, then ask
   underneath:

   > Tell me the rule set or schema and its version or retrieval date and I will pin the
   > basis line. Without it I can say what was checked but not what it means.

4. **Write the block.** Fill every line. An empty line is a lie of omission — and so is a
   line filled with a placeholder addressed to the reader.
5. **Check the negation.** Read "This does not establish" aloud. If it does not sting
   slightly, it is too soft to do its job.

## When the space is small

A scope statement that does not fit where it has to go does not get used. If the user
says sidebar, footer, tooltip, one line, or "keep it short", **the format bends and the
two load-bearing lines do not.**

Compress in this order:

1. **Drop the labels.** Prose carries the same content. "Runs on this file at upload,
   by pattern matching — so a clean result means nothing matched, not that the file is
   clear" is a complete scope statement in one sentence.
2. **Merge `Checked` and `Against`.** "Pattern-matched against [ruleset v2.1]" does both.
3. **Cut `Not checked` to the two a reader would most wrongly assume were covered.**
   Not the full list — the two that matter. A long list in a small space gets skipped
   entirely, which is worse than a short one that gets read.
4. **Never cut the negation.** "A clean result means nothing matched, not that the file
   is clear" is the line the whole block exists for. If only one sentence survives, it
   is this one.
5. **Never cut the expiry silently.** If there is no room, say "as of [date]" inline.

A three-line prose version that keeps the omission and the negation beats a complete
labelled block that gets cut by whoever pastes it into the sidebar. Offer the long form
too if it would be useful elsewhere, but lead with what was asked for.

## What not to do

**Do not write a disclaimer.** "For informational purposes only", "consult a
professional", "no warranty" — these protect the author and tell the reader nothing.
A scope statement is a description of coverage. If a line would appear unchanged on an
unrelated product, delete it.

**Do not pad "Not checked" with the irrelevant.** Listing thirty things nobody expected
buries the two they did. Ask what a reader would assume, and answer that.

**Do not soften the negation.** "May not be sufficient for all purposes" is noise.
"This does not establish that your technical documentation is complete" is a scope
statement.

**Do not state a basis you have not seen.** If told the check runs against "the current
schema", ask which version. Pinning to an unverified authority is the failure this
block exists to prevent. Asking does not mean withholding the block: write it with the
basis named as far as it is known, and ask underneath.

## Limits

> A scope statement describes what a check covered. It does not make the check correct,
> and it is not a substitute for the check being adequate to its purpose.
