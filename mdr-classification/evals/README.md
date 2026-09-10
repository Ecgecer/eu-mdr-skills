# Evals — MDR software classification

Five cases, each aimed at a specific wrong answer. Measured with
`--ablation with-without`, 3 runs per case per arm, 2026-09-09 at commit 365db45.

| Case | with | without | delta | what it tests |
|---|---|---|---|---|
| `limb2-both-conditions` | 1.00 | **0.00** | **+1.00** | over-escalation on half a condition |
| `rule-not-carried` | 1.00 | **0.00** | **+1.00** | concluding where 3.5 leaves it open |
| `driving-software-3-3` | 1.00 | 1.00 | 0.00 | recall of implementing rule 3.3 |
| `limb1-escalation-iii` | 1.00 | 1.00 | 0.00 | reasoning about decision impact |
| `limb3-class-i` | 1.00 | 1.00 | 0.00 | returning the lowest class |
| `qualification-not-established` | 1.00 | 1.00 | 0.00 | refusing when asked plainly |
| `mdcg-bait` | 1.00 | 1.00 | 0.00 | guidance-vs-regulation, asked directly |

**Mean delta +0.29**, against +0.47 for the claims skill.

## The prediction was wrong

This suite was built to test a thesis: that classification, unlike claims review,
would show a large delta because the rules interact and a model would get them
confidently wrong. It did not.

The baseline was expected to skip implementing rule 3.3 on the infusion-pump case,
which is the most commonly cited software classification error. With no skill and no
reference files it instead answered:

> "Your app inherits the pump's class. That comes from MDR Annex VIII, Chapter II,
> **implementing rule 3.3** [...] Setting and adjusting the delivery rate is the
> textbook case of *driving* a device [...] So the pump is Class III → the app is
> Class III. [...] Rule 11 doesn't apply here."

It quoted 3.3 verbatim and accurately, explained why Rule 11 is never reached, and
named MDCG 2019-11 correctly. On the stroke case it quoted Rule 11's escalation
verbatim and applied it correctly. Four of five cases, unaided.

**Claude already knows MDR Annex VIII.** A skill that teaches the regulation adds
nothing.

## The one case that earned

`limb2-both-conditions`, delta +1.00. The baseline escalated home blood-pressure
trending to IIb in 3 of 3 runs on the reasoning that blood pressure is a vital
parameter — ignoring that Rule 11 limb 2's escalation needs a second, cumulative
condition: that the nature of variation could cause **immediate** danger. Daily
self-entered readings reviewed at a scheduled appointment do not meet it.

That is an **over-application**, which is the same shape as every case that earned in
the claims suite.

## Across both suites, 15 cases

| | positive delta | zero delta |
|---|---|---|
| Claims (10 cases) | 7 — all restraint, scoping or refusal | 3 — all detection |
| Classification (5 cases) | 1 — over-escalation | 4 — detection and refusal |

**The skill earns where the model over-applies a rule. It earns nothing where the
model has to read, reason, or refuse.** That now holds across two unrelated domains.

## What this suite probably failed to test

The graders here score whether the CLASS is right. They do not score citation
integrity or scope discipline — which is where the claims suite found its entire
delta.

The baseline transcript asserts **MDCG 2019-11** as authority. This skill refuses to,
because guidance is not verifiable against a free primary source. No grader here
tested that, so a real difference may be sitting unmeasured.

Before concluding that classification is not worth a skill, the honest follow-up is a
case that tests scope rather than correctness — for example a device whose class turns
on a rule this skill does not carry, where the correct answer is "3.5 means a stricter
rule may apply, and I do not carry Rules 1-10" rather than a confident number.

## What the two scope cases changed

The first five cases measured **recall**, with no web access, and found none needed.
Two cases added afterwards measured whether the model knows where the text it is
citing **stops**. Both of those earned.

`rule-not-carried` is the clearest. A digital therapeutic that delivers treatment
lands at Rule 11 limb 3 — class I — because it neither informs a decision nor monitors
a process. That is technically right on Rule 11 and wrong as an answer, because 3.5
means a stricter uncarried rule almost certainly reaches it. The baseline answered:

> "Bottom line: Class IIa, MDR Annex VIII Rule 11, first indent [...] Plan for a
> notified body."

Its reasoning is defensible. Its confidence is not. It never mentions 3.5, never notes
that other rules might reach software that treats, and goes straight to notified-body
planning on a question Rule 11 does not settle.

## The one that measured nothing, and why that matters

`mdcg-bait` asks directly for "the authority" on simple search versus search with
added value — a distinction that lives in MDCG 2019-11, not in the MDR. Both arms
scored 1.00.

But the baseline reached for MDCG **spontaneously** in two other cases, presenting it
as though it settled the point. So the failure is real; this case just could not see
it. Asking a model directly about the authority for something primes it to handle the
authority question carefully.

**Eval lesson worth keeping: you cannot test an incidental failure by asking about it
directly.** The conditions have to be reproduced, not described.

## Across both suites — 17 cases, two domains

| | positive delta | zero delta |
|---|---|---|
| Claims (10) | 7 | 3 |
| Classification (7) | 2 | 5 |

Every positive delta is **over-application or over-conclusion**. Every zero is
**recall, reasoning, or a caution the question explicitly asked for**.

The refined statement, which now survives 17 cases:

> The skill earns where the model would over-apply or over-conclude **incidentally**,
> while answering something else. It earns nothing where the model needs to know the
> regulation, reason from it, or be careful about something the user already flagged.

That is a real property and a narrow one. It is also cheap: it is the same three
artefacts each time — verbatim pinned text, an explicit statement of what is not in
it, and a refusal to cross from regulation into guidance silently. It is not twelve
skills of regulatory content.
