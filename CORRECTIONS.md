# Corrections

Things this repo published that were wrong, what was wrong with them, and what replaced
them. Kept because a repo whose claim is accuracy should show its errors rather than
quietly fix them, and because the errors are instructive.

Every entry below is a mistake that a person had to catch. Most of them now cannot
recur, because each one was turned into something that fails automatically:

| What went wrong | What stops it now |
|---|---|
| Arm values inferred from a reported delta; the most favourable of several runs published | Tables generated from the stored JSON, every run listed, `report-evals.py` |
| Tables headed "generated, do not hand-edit" and then hand-edited | `--check-tables` fails CI when a published table and its runs disagree |
| A billing failure counted as a score of zero | Errored runs excluded from scoring and marked ⚠ |
| An arm scored from whichever runs survived | An arm needs three valid runs or it reports ", " |
| A single hand-run pass reported as evidence | Three runs per case, enforced by the same rule |
| Numbers describing skill text that had since changed | Content hash of skill **and** eval cases; the table carries a banner until re-measured |
| A retracted claim still live in four other files | Registered strings in this file, checked across all Markdown |
| An eval prompt that leaked its own answer | Grader quotes checked against prompt and skill text |
| A benchmark that listed 23 of its own 30 cases | The generator asserts its buckets sum to the case count |
| Counts and ranges typed into prose, drifting | README, ROADMAP and METHOD figures spliced from the data |

Three things on that list were found by the mechanism built for the one above it. The
retracted-claim register found the claim in three more files each time it was made less
literal, and it found a second retracted claim nobody had looked for.

What is **not** automated: whether a grader is fair, and whether a measurement means what
you say it means. Both have gone wrong here in both directions, graders that failed
correct reasoning and graders that would have passed wrong answers, and both were caught
by reading transcripts, not by reading scores.

---

## 2026-09-10: a false claim about a measured result

**Published:** `mdr-classification/evals/README.md` said the baseline "escalated home
blood-pressure trending to IIb in 3 of 3 runs on the reasoning that blood pressure is a
vital parameter."

**Actually:** all three stored baseline runs answered Class **IIa**, the answer the
grader requires. Zero said IIb. The failure mode was asserted without reading the runs.

**Why it scored 0.00 anyway:** the grader demanded the response "explicitly REJECT the
IIb escalation". The baseline reached IIa by a different, legitimate route and never
proposed the escalation it was required to reject. The grader failed correct answers for
using different words, which makes that suite's only earning case a grader artifact.

---

## 2026-09-10: arm values inferred rather than observed

**Published:** `puffery-restraint` as 1.00 / 0.67, `hwg3a-arzneimittel-only` as
1.00 / 0.33, and "All ten score 1.00 with the skill."

**Actually:** 0.33 / 0.00 and 0.67 / 0.00. The harness printed only a mean delta for
those runs and the arm values were reasoned backwards from it to make the table
consistent. The deltas were right by coincidence; the arms were invented, and two cases
do not score 1.00.

**Fix:** `scripts/report-evals.py` now generates every table from the stored JSON. The
tables are no longer typed.

---

## 2026-09-10: a billing failure counted as a skill failure

**Published:** `no-disclaimer` as 1.00 / 0.67, delta +0.33, and a scope-statement mean
of +0.33.

**Actually:** one baseline run failed with `Credit balance is too low` and was scored
zero. Excluding errored runs, both valid baseline runs scored 1.00. The delta is 0.00 and
the suite mean is +0.22.

---

## 2026-09-10: the most favourable of several runs published

**Published:** one row per case.

**Actually:** several cases had multiple stored runs with different results
`uwg6-comparison` had three, including one where the baseline outscored the skill. Only
the best was published.

**Fix:** the generator lists every stored run.

---

## 2026-09-10: eval prompts that leaked their own answers

**Published:** three device-claims cases whose copy reused, near-verbatim, worked
examples sitting in the reference files the with-skill arm loads. `01-limb-d` used
"athletes tracking recovery" while `mdr-ivdr-art7.md` carries "Great for athletes
tracking recovery" as its own limb (d) example; the entire PASS gate was a lookup.

**Fix:** new copy on unseen material, and each grader now tells the judge not to look for
the reference file's wording.

---

## 2026-09-09: a hand-run pass reported as evidence

**Published:** "7/7 cases pass."

**Actually:** one run per case. Three runs found two cases failing one run in three.
Single runs are not evidence, and the harness default of three exists for a reason.

---

## 2026-09-09: two graders that punished correct reasoning

**Published:** `hwg11-item-scope` and `uwg6-comparison` at 0.67.

**Actually:** grader defects. One could not tell a provision being *used* from a
provision being named in order to *exclude* it. The other demanded an affirmation a
correct analysis has no occasion to make. Both were caught by reading failing
transcripts, not by review, which is why the repo later commissioned an adversarial
pass over all 25 graders and found five more.

---

## 2026-09-11: "a frontier model" from a sample of one

**Published:** the benchmark and README described the measured baseline as "a frontier
model", and the finding as "models over-apply".

**Actually:** every number in this repo comes from **Claude**, run through Claude Code
2.1.266/267. GPT, Gemini, Llama and everything else are untested. The results files do
not even record which Claude model, only the CLI version.

Generalising from one model to "frontier models" is precisely the defect these skills
measure. A claim applied one step past where the evidence reaches. Caught by the repo's
owner asking whether we were assuming other models know what Claude knows.

**Fix:** every claim narrowed to Claude, with the untested scope stated and results from
other models invited. It is also plausible that a model with less European regulatory
text in training would fail the *knowledge* cases too, in which case the reference files
would earn more rather than less. Nobody has measured it, and the file now says so.

**Measured 2026-09-11, within the Claude family.** Re-running three suites pinned to Haiku
4.5 shows exactly that: the knowledge cases that measure +0.00 against Opus measure
**+1.00** against Haiku, whose baseline cites a different wrong Annex VIII rule on each of
three runs. The guess was right about the references and wrong about the shape, the
*discipline* half does not transfer, so the boundary cases measure +1.00 for Opus and
+0.33 or +0.00 for Haiku. [MODELS.md](MODELS.md) has it. GPT, Gemini and everything
outside the Claude family remain untested, and this does not speak for them.

---

## 2026-09-11: tables that said "generated" and were typed by hand

**Published:** each suite's eval README carried a results table headed "Generated by
`report-evals.py` from the stored run data. Do not hand-edit the table."

**Actually:** the generator printed to stdout and a human pasted the output, so the
tables stopped matching the runs they cited as soon as anything was re-run. Three of five
had drifted:

| Suite | published | stored |
|---|---|---|
| `mpdg-germany` | +0.47 | +0.50 |
| `scope-statement` | +0.22 | +0.11 |
| `mdr-classification` | +0.29 | not measured against current text |

Two cases where the skill measures **negative** were published as +0.00:
`scope-statement/no-disclaimer` is −0.67, and `mpdg-germany/not-german-market` is −0.33.
A repo whose claim is that it publishes the cases where the skill adds nothing had, in
fact, published two cases where the skill actively subtracts as if they were neutral.

**Fix:** the table is spliced between markers by `report-evals.py --write`, and
`--check-tables` fails CI when the file and the stored runs disagree. "Generated" now
means generated on every push rather than generated once.

---

## 2026-09-11: an arm scored from whichever runs survived

**Published:** `mpdg-germany/fsn-language` as a measured delta.

**Actually:** its baseline arm had one surviving run of three; the other two failed on
billing. The generator averaged whatever was left, so one run became a published arm
value, in a repo whose own method file says three runs is the minimum that counts as
evidence. The same averaging briefly turned that case into +1.00.

**Fix:** an arm needs three valid runs or it reports ", ". **Unmeasured is not zero**, and
it is not a small sample either. The row now reads ", " and says the baseline is unknown.

---

## 2026-09-11: numbers describing text the plugin no longer shipped

**Published:** five suites' tables, presented as describing the skills in the repo.

**Actually:** four had been edited after their last measurement, `scope-statement` by a
commit whose entire purpose was changing its behaviour, `mdr-classification` and
`mpdg-germany` by the no-silent-supplement rule, `mdr-transition` by a trim whose own
commit message said UNTESTED. Nothing in the repo disagreed with the stale numbers,
because nothing was comparing them to anything.

Timestamps cannot catch this: the honest workflow is edit, measure, commit, so the commit
is always newer than the run it describes.

**Fix:** `report-evals.py --stamp` records a hash of the skill text a measurement
describes. When it no longer matches, the generated table carries a banner saying so, and
that banner is inside the CI-checked region, so a reader of the table finds out from the
table, not from the commit log. All five suites carry it as this is written.

---

## 2026-09-11: a retracted claim still on the front page

**Published:** the README's opening pitch listed four measured failures, among them "It
escalated a device class on half of a two-part condition in 3 of 3."

**Actually:** that is the same claim this file retracted a day earlier. The stored
baseline runs for `limb2-both-conditions` answer Class **IIa** in all three and score
**1.00**: the baseline gets it right. The correction was written into the suite's eval
README and into this file, and nobody checked whether the sentence it retracted appeared
anywhere else. It did, in the most-read paragraph in the repo.

A second claim in the same paragraph was wrong on its own terms: "It applied German law
to a French-market asset in 2 of 3." The baseline does the opposite. In 3 of 3 runs it
explicitly drops German law. *"The France-only scoping is correct as far as it goes
the German HWG doesn't reach this page"*, and then asserts French advertising rules it
cannot cite, which is what the grader actually fails it for. Same defect family, wrong
country, and published as a different failure than the one measured.

**Fix:** both replaced with claims checked against the stored runs one at a time. The
same false French-market sentence was also in `scripts/export-benchmark.py`, so it was
being generated into `benchmark/README.md` on every run; fixed at the generator.

**What this says about the method:** retracting a claim in the file where it was found is
not retracting it. There was no step that asked where else the sentence lived.

---

## 2026-09-11: a benchmark that listed 23 of its own 30 cases

**Published:** `benchmark/README.md` split its cases into "hard" (baseline 0.00) and
"cases a baseline already passes" (baseline 1.00), and the root README said "12 of the 30
... the 13 cases a baseline already passes".

**Actually:** the two generated sections covered 11 and 12 cases. The other **7, the
ones the baseline passes only sometimes, were in no section at all**, so the file
silently omitted a quarter of itself. The root README's hand-typed 12 and 13 matched
neither the generator nor each other: 12 + 13 is not 30.

The omitted group is the most diagnostic one. A baseline that scores 0.33 or 0.67 across
three runs can reach the right answer and does not do so reliably, which is a different
finding from either "knows it" or "does not know it", and it is the group that proves
why three runs is the minimum.

**Fix:** a third section lists them with their baseline rates, an assertion in the
generator fails if the buckets do not sum to the case count, and the root README's counts
are spliced in from the data and checked in CI.

---

## 2026-09-11: one withdrawn claim, five files

**Published:** after retracting "applied German law to a French-market asset" and
correcting README.md, the guard built to enforce that retraction reported the repo
clean.

**Actually:** the claim was in five places, and the guard found three of them only after
being made progressively less literal:

| Where | Phrasing | Why the guard missed it |
|---|---|---|
| `README.md` | applied German law to a French-market asset |, found by hand |
| `scripts/export-benchmark.py` | applying German law to a French-market asset |, found by hand |
| `ROADMAP.md` | German law **applied to** a French-market asset | word order |
| `device-claims/evals/README.md` | applied German **national** law to a French-market asset | one inserted word |
| `METHOD.md` | **Applied** German law to a French-market asset | capital letter |

The same pass found a second withdrawn claim, "escalated a device class on half of a
two-part condition", alive in METHOD.md's summary table with a capital E, retracted on
2026-09-10, corrected in README.md on 2026-09-11, and still published in a third file
because an exact match is case-sensitive.

METHOD.md's table was wrong twice over: it also gave the French-market case as "2 of 3
runs" when the stored baseline fails it 3 of 3.

**Fix:** the register takes regular expressions, matches case-insensitively, and escapes
literals so a "." in "1.00" is not a wildcard. All four phrasings and the capitalised
variant are mutation-tested.

**What this says about the method:** a retraction is not a fact about one file. Each time
the guard was loosened it found another copy, which means the first two versions of it
would have certified the repo clean while three false claims were live. A checker that
only catches the wording you thought of measures your imagination, not the repo.

---

## Retracted wording, enforced

A retraction that only edits the file where the claim was found is not a retraction. The
sentence "it escalated a device class on half of a two-part condition" was withdrawn on
2026-09-10 and was still the opening pitch of README.md a day later, because nothing
asked where else it lived.

These are the strings that must not reappear. `retracted:` is a literal;
`retracted-re:` is a regular expression, which exists because the literal list missed
"German law applied to a French-market asset", the same withdrawn claim with two words
swapped, sitting in ROADMAP.md. Then the widened pattern missed "applied German
**national** law to a French-market asset" in device-claims' eval README, because one
extra word defeats an exact phrase. Three phrasings, three files, one withdrawn claim. A
retraction that only catches the wording you happened to think of is barely a retraction,
so these patterns are written to tolerate the words a writer would naturally vary. `tests/check-portable-fresh.py` fails
if one shows up in any Markdown file other than this one and the listed exceptions, which
are the places that quote the claim in order to retract it.

<!-- retracted: "escalated home blood-pressure trending to IIb" | mdr-classification/evals/README.md -->
<!-- retracted: "escalated a device class on half of a two-part condition" -->
<!-- retracted-re: "German\s+(national\s+)?law\s+(to|applied to)\s+a\s+French-market asset" -->
<!-- retracted-re: "(applying|applied|apply(ing)?)\s+German\s+(national\s+)?law\s+to\s+a\s+French-market asset" -->
<!-- retracted: "All ten score 1.00 with the skill" -->
<!-- retracted: "7/7 cases pass" -->

---

## What these have in common

Every one is the same failure: **a claim asserted from something other than the thing it
describes.** From a delta instead of the arms. From a schema instead of the data. From
what a grader was meant to test instead of what it tests. From one run instead of three.

That is the identical defect the skills themselves are built to prevent in a model, a
real rule applied one step past where it reaches. It turns out to be just as easy to do
to your own measurements.
