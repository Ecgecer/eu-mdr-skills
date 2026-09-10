# Corrections

Things this repo published that were wrong, what was wrong with them, and what replaced
them. Kept because a repo whose claim is accuracy should show its errors rather than
quietly fix them, and because the errors are instructive.

---

## 2026-09-10 — a false claim about a measured result

**Published:** `mdr-classification/evals/README.md` said the baseline "escalated home
blood-pressure trending to IIb in 3 of 3 runs on the reasoning that blood pressure is a
vital parameter."

**Actually:** all three stored baseline runs answered Class **IIa** — the answer the
grader requires. Zero said IIb. The failure mode was asserted without reading the runs.

**Why it scored 0.00 anyway:** the grader demanded the response "explicitly REJECT the
IIb escalation". The baseline reached IIa by a different, legitimate route and never
proposed the escalation it was required to reject. The grader failed correct answers for
using different words, which makes that suite's only earning case a grader artifact.

---

## 2026-09-10 — arm values inferred rather than observed

**Published:** `puffery-restraint` as 1.00 / 0.67, `hwg3a-arzneimittel-only` as
1.00 / 0.33, and "All ten score 1.00 with the skill."

**Actually:** 0.33 / 0.00 and 0.67 / 0.00. The harness printed only a mean delta for
those runs and the arm values were reasoned backwards from it to make the table
consistent. The deltas were right by coincidence; the arms were invented, and two cases
do not score 1.00.

**Fix:** `scripts/report-evals.py` now generates every table from the stored JSON. The
tables are no longer typed.

---

## 2026-09-10 — a billing failure counted as a skill failure

**Published:** `no-disclaimer` as 1.00 / 0.67, delta +0.33, and a scope-statement mean
of +0.33.

**Actually:** one baseline run failed with `Credit balance is too low` and was scored
zero. Excluding errored runs, both valid baseline runs scored 1.00. The delta is 0.00 and
the suite mean is +0.22.

---

## 2026-09-10 — the most favourable of several runs published

**Published:** one row per case.

**Actually:** several cases had multiple stored runs with different results —
`uwg6-comparison` had three, including one where the baseline outscored the skill. Only
the best was published.

**Fix:** the generator lists every stored run.

---

## 2026-09-10 — eval prompts that leaked their own answers

**Published:** three device-claims cases whose copy reused, near-verbatim, worked
examples sitting in the reference files the with-skill arm loads. `01-limb-d` used
"athletes tracking recovery" while `mdr-ivdr-art7.md` carries "Great for athletes
tracking recovery" as its own limb (d) example; the entire PASS gate was a lookup.

**Fix:** new copy on unseen material, and each grader now tells the judge not to look for
the reference file's wording.

---

## 2026-09-09 — a hand-run pass reported as evidence

**Published:** "7/7 cases pass."

**Actually:** one run per case. Three runs found two cases failing one run in three.
Single runs are not evidence, and the harness default of three exists for a reason.

---

## 2026-09-09 — two graders that punished correct reasoning

**Published:** `hwg11-item-scope` and `uwg6-comparison` at 0.67.

**Actually:** grader defects. One could not tell a provision being *used* from a
provision being named in order to *exclude* it. The other demanded an affirmation a
correct analysis has no occasion to make. Both were caught by reading failing
transcripts, not by review — which is why the repo later commissioned an adversarial
pass over all 25 graders and found five more.

---

## What these have in common

Every one is the same failure: **a claim asserted from something other than the thing it
describes.** From a delta instead of the arms. From a schema instead of the data. From
what a grader was meant to test instead of what it tests. From one run instead of three.

That is the identical defect the skills themselves are built to prevent in a model — a
real rule applied one step past where it reaches. It turns out to be just as easy to do
to your own measurements.
