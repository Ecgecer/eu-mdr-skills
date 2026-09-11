# The method

How to build an agent skill for a regulation that is worth trusting. This is what the
three skills here are instances of. Nothing in it is specific to medical devices.

It exists because building the first skill taught us the thing that decides everything
else, and it is not what we expected.

---

## 1. Find out what the model actually gets wrong

We assumed a regulatory skill's job was to supply knowledge the model lacked. We
measured it, and that assumption was wrong.

Across 20 cases in three domains, the model **already knew the law**. It quoted MDR
implementing rule 3.3 verbatim from memory, applied Rule 11's escalations correctly,
refused to classify a non-device, and wrote a good scope statement unprompted when it
had the facts. Every case that tested recall or reasoning measured a delta of **zero**.

What it got wrong was where rules **stop**:

<!-- method-failures:start -->
| It did this | In |
|---|---|
| Cited a German advertising provision against a device that provision does not reach | 3 of 3 runs |
| Asserted another member state's advertising rules from memory, having correctly ruled out German law | 3 of 3 runs |
| Applied a medicinal-product provision to a device | 2 of 3 runs |
| Applied a lay-audience advertising rule to a gated professional audience | 3 of 3 runs |
| Answered "plan for a notified body" to a question the cited rule does not settle | 3 of 3 runs |
| Manufactured findings on clean copy | 3 of 3 runs |
| Invented an authority rather than asking which rule set was meant | 3 of 3 runs |
<!-- method-failures:end -->

Every one is plausible, well-reasoned, and wrong in a way you cannot detect from the
answer. Not a hallucinated rule. **A real rule applied one step past where it reaches.**

**So the first thing to do is not write a skill. It is to find out, by measurement,
which of those two problems you actually have.** If the model already performs at
ceiling on your domain's reasoning, a skill that explains the domain earns nothing, and
you will not discover that by reading its output and being impressed.

## 2. Pin the text, and say what you did not pin

Carry the operative provisions **verbatim**, with source URL and retrieval date, in
files the skill reads. Not paraphrased into the prompt.

Two reasons, and the second is the one people miss.

**The authority is not reliably available.** Over one afternoon EUR-Lex returned an
HTTP 202 stub, then a 403, then began redirecting every document URL to the Official
Journal index, where it displayed "EUR-Lex is temporarily not fully available." A skill
that fetches the law when asked inherits that, at a moment it did not choose.

**Pinned text has an edge, and the edge is the product.** A file containing Rule 11 and
implementing rules 3.1–3.7 and *nothing else* lets the skill say: this is what I carry,
Rules 1–10 are not in it, so under 3.5 a stricter rule may reach your device and I
cannot see it. That sentence is the whole value. A model reasoning from everything it
vaguely knows cannot produce it, because it has no boundary to report.

Write the non-coverage into the reference file itself, not only the skill.

## 3. Make refusal a first-class output

The skill must be able to return "I cannot conclude this" and have that count as
success. If every path leads to an answer, it will produce one.

Concretely, in the skills here:

- A `Breach: none` + `Call: Verify` state, so an open question is not inflated into a
  finding. Without it, the review promoted "check the technical file" into a breach.
- A rule that a finding must name its basis **from supplied material**, inferring a
  likely risk from the product category condemns every advertisement ever written, and
  is unfalsifiable.
- An explicit "this rule is a floor, not the answer" path when another uncarried rule
  might reach higher.
- Guidance named as guidance. If the answer turns on non-binding guidance, say so and
  stop.

## 4. Measure against a baseline, and weight the suite toward restraint

Write eval cases and run them **with and without the skill**. Without the baseline arm
you cannot distinguish "the model is good" from "the skill works", and you will
attribute the model's competence to your prompt.

Weight the suite the way the value actually distributes:

- **False-positive controls**: clean input where the correct answer is "nothing here".
  These produced the largest deltas in every suite. A model with no skill manufactured
  findings on clean copy in 3 of 3 runs.
- **Scope tests**: where a real rule does not reach the thing in front of it.
- **Refusal tests**: where the honest answer is a question.
- **Detection tests**: will mostly measure zero. Include a few anyway; they are how you
  learn which half of your skill is decorative.

**Publish the zeroes.** A suite reporting only its wins is marketing. Half the cases
here measure no benefit, that fact is in every eval README, and it is the strongest
evidence that the other half is real.

## 5. Make the central claim executable

"Verbatim from the official source, retrieved on this date" is an assertion. Ship the
command that tests it.

`scripts/verify-sources.py` re-fetches each source and confirms every quoted passage
still appears, character for character after normalising whitespace and quote glyphs.
It reports drift with the point of divergence. Where a source cannot be fetched it says
so and prints what to search for by hand. **It never counts an unread source as a
pass.** Run it in CI, and on a schedule, because law changes.

---

## Traps, all of which we walked into

**A grader that punishes correct reasoning.** `FAIL if § 11(1) no. 2 is cited` marked
down a response that named no. 2 *in order to exclude it*, because the grader
pattern-matched a string instead of judging how the provision was used. Two graders had
this defect and both were caught by chance. Judge the use, not the mention. And have
someone else read your graders. A suite written by the skill's author tests what the
author thought to test.

**One run is not evidence.** A hand-run pass reported 7 of 7 from a single run per case.
Three runs found two cases that fail one run in three. Use at least three.

**Testing an incidental failure by asking about it directly.** Asked point-blank "what
is the authority for X?", the model handled non-binding guidance correctly, delta zero.
It nonetheless reached for that same guidance *unprompted*, as though it settled the
point, while answering unrelated questions. **The conditions have to be reproduced, not
described.** That case measured nothing and the failure is real.

**Generated artefacts with a hardcoded file list.** The freshness check listed the files
it knew about. A second skill was added, its bundle was never generated, and the check
reported everything up to date. The guard against silent drift could not see the drift
because it had been told what to look at. Discover, do not enumerate.

**Verifying elided quotes as one string.** A quote containing `[...]` is not contiguous
in the source. Matching it whole fails by construction, and the verifier reported four
false drifts on text that was perfectly correct. Split on the elision and verify each
fragment.

**Detecting a stub by response size.** EUR-Lex serves a ~2 KB shell to scripted clients,
so a size threshold seemed reasonable, and it flagged every good source as a bot check,
because gesetze-im-internet legitimately serves each section as its own 3–8 KB page. Key
on status code and extracted-text length.

**Predicting where a skill will earn.** Four times now: classification would show a large
delta because the rules interact (it did not), Article 120 would because the model's
recall was stale (it was not), the two Art. 7 limb cases would because the limbs are
subtle (they did not), and MPBetreibV would because it binds the operator rather than the
manufacturer (the model corrects that premise unasked, 3 of 3). Every prediction was
plausible, argued from the structure of the law, and wrong. The fourth one cost $5.25 to
settle because two cases were written before anything was built; the first three cost a
suite each. **Write the two hardest cases first and run them against no plugin at all.**
It is the cheapest question in this method and it has changed the answer every time.

**Propagating a fix by pattern-match.** A demand for information ate the deliverable in
three places. A missing intended purpose stopped a claims review instead of narrowing
it, a declined case-law citation still supplied the doctrine, a missing schema version
turned a scope statement into a fill-in form. Having named the pattern, the obvious next
move was to grep every skill for templates ending in a question and fix those too. Two
turned up. Neither was a defect: `mdr-transition` already delivers the date and *then*
asks to confirm the conditions, and `mdr-classification` asks for an intended purpose it
genuinely cannot classify without, its two cases that supply none both score 1.00, so
the gate costs nothing. A pattern that is a defect in one place is a hypothesis
everywhere else. Check what it costs before you fix it, or you will spend a measurement
undoing your own tidying.

**Believing your own prediction.** We predicted classification would show a large delta
because the rules interact and models get them confidently wrong. It measured +0.20 on
the five cases that suite then had (run of 2026-09-09), lower than the skill we thought
was weaker, with the baseline getting four of five right unaided. The suite has grown
since; its current figure is in its own eval README rather than restated here. The measurement is the point. If you are confident enough not to run it, run it.

---

## What it costs

<!-- eval-cost:start -->
**$155 of eval spend so far**, across 40 stored runs of 5 suites and 30 cases, at 3 runs per case per arm. The largest single run (`device-claims`, 10 cases, both arms) was **$16.39** and took 97 minutes.
<!-- eval-cost:end -->

Budget for re-running after every substantive change, because that is when a suite earns
its keep, and for re-running after a **grader** change too, which is easy to forget and
invalidates the numbers just as thoroughly.

## The shortest version

Measure before you build. Pin the text and publish its edges. Let the skill refuse.
Test with a baseline or you are measuring the model. Publish the cases where you added
nothing. Make the claim executable.
