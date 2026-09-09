# Evals — MDR software classification

Five cases, each aimed at a specific wrong answer. Measured with
`--ablation with-without`, 3 runs per case per arm, 2026-09-09 at commit 365db45.

| Case | with | without | delta |
|---|---|---|---|
| `limb2-both-conditions` | 1.00 | **0.00** | **+1.00** |
| `driving-software-3-3` | 1.00 | 1.00 | 0.00 |
| `limb1-escalation-iii` | 1.00 | 1.00 | 0.00 |
| `limb3-class-i` | 1.00 | 1.00 | 0.00 |
| `qualification-not-established` | 1.00 | 1.00 | 0.00 |

**Mean delta +0.20**, against +0.47 for the claims skill.

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
