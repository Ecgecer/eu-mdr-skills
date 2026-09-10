# Contributing

A skill here is accepted on evidence, not on plausibility. Everything below exists
because a skill that *looks* right and adds nothing is worse than no skill: it consumes
tokens, and it lends confidence to output that has not earned it.

Read [METHOD.md](METHOD.md) first. It explains why these rules are what they are.

## What a new skill must ship

**1. Verbatim primary text, with an edge.**
`skills/<name>/references/*.md` carrying the operative provisions word for word, each
with its source URL and retrieval date. Paraphrase in the skill body is fine; paraphrase
in a reference file is not.

Every reference file must also state **what it does not carry**. That sentence is what
lets the skill say "a rule I do not have may reach higher", and that is the product.

**2. A source entry in the verifier.**
Add the file and its source URLs to `SOURCES` in `scripts/verify-sources.py`, then run
it. If the source cannot be fetched by script, the entry still belongs there — the tool
reports it as UNVERIFIED with instructions, which is honest. Silence is not.

**3. An eval suite with a baseline arm.**
`evals/<nn>-<name>/prompt.md` plus `evals/<nn>-<name>/graders/criteria.md`. Run:

```
claude plugin eval . --ablation with-without
```

Three runs per case per arm, which is the default. One run is not evidence — a single
run once reported 7 of 7 here, and three runs found two cases failing one run in three.

**4. Measured results in `evals/README.md`, including the zeroes.**
A case where the skill measures no benefit is a finding, not an embarrassment. Half the
cases in this repo measure zero and every one is published. A PR whose suite reports
only wins will be asked where the losses went.

## What the suite has to contain

Weight it toward what actually earns:

- **False-positive controls.** Clean input where "nothing here" is correct. These
  produced the largest deltas in every suite in this repo.
- **Scope tests.** A real rule that does not reach the thing in front of it.
- **Refusal tests.** Where the honest answer is a question.
- **Detection tests.** A few. They will mostly measure zero, and that is how you find
  out which half of your skill is decorative.

## Writing a grader that works

This is where this repo has made its worst mistakes. Two graders marked correct answers
as failures and both were caught by luck.

- **Judge how a provision is used, not whether its name appears.** `FAIL if X is cited`
  will fail a response that names X in order to rule it out — which is the best possible
  answer.
- **Do not require an utterance the correct answer need not contain.** A grader demanding
  the response affirm something it has no occasion to say will fail correct work.
- **State which alternative answers pass, and why.** If a defensible second answer exists,
  name the reasoning that would make it acceptable.
- **Ask what the laziest passing response looks like.** If a generic answer satisfies
  every PASS condition, the grader is too loose. A grader that cannot fail is decoration.
- **Do not test the model's knowledge.** The finding behind this repo is that the skills
  add boundary discipline, not knowledge. A grader that checks "did it get the right
  answer" measures the model.

## Before opening a PR

```
python3 scripts/build-portable.py        # regenerate bundles (discovers skills)
python3 tests/check-portable-fresh.py    # must exit 0
python3 scripts/verify-sources.py        # must not report DRIFTED
claude plugin eval . --ablation with-without
```

Never hand-edit anything in `dist/` or `GEMINI.md`. They are generated, and CI fails if
they drift from the skills.

## Scope of this repo

EU medical device regulation, plus the national law that enforces it, plus
domain-general tooling that serves those skills. A skill for an unrelated regulation is
better as its own repo using the same method — link it and it will be linked back.

## What will be turned down

- A skill with no eval suite, or a suite with no baseline arm.
- Reference text that is paraphrased, undated, or has no stated edge.
- A suite that reports only positive results.
- Legal advice. These are drafting and triage aids. A skill that tells a user they are
  compliant does not belong here.
- Case law, unless someone solves verifying it against a free primary source. Statute
  verifies for nothing; case law does not, and that line is deliberate.
