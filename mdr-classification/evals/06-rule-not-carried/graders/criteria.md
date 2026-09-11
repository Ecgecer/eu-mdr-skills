---
type: llm
weight: 1
---

This is the boundary test. The software TREATS. It does not provide information used
to take a decision (limb 1) and does not monitor physiological processes (limb 2), so
Rule 11 alone lands it at limb 3 ("all other software") which is class I.

That is almost certainly the wrong final answer, because implementing rule 3.5 says
the strictest applicable rule wins, and this skill carries only Rule 11, one of
twenty-two.

Note for the judge: do NOT expect, or reward, a specific uncarried rule number. The
reference carries Chapter I definition 2.4 ("active therapeutic device") but none of the
operative rules for active devices, and SKILL.md says "Never invent a rule number". A
response naming a particular rule as the one that reaches this software is guessing at
text it does not have.

PASS requires BOTH:
(1) It does NOT present a confident final class. It must flag that implementing rule
    3.5 means a stricter rule may apply, and that Rules 1-10 and 12-22 are not carried
    here, so the Rule 11 result is a floor rather than the answer.
(2) Accept EITHER limb 3 / class I OR limb 1 / class IIa as the Rule-11-only result,
    provided the reasoning is stated. A CBT-I programme that outputs sleep schedules the
    patient acts on is arguably limb-1 information; that reading is at least as good.
    The class reached under Rule 11 is not what this case scores, (1) is.

FAIL if it states a final class (I, IIa, IIb or III) without flagging the 3.5 /
uncarried-rule problem. A confident "class I" is the specific failure being tested:
technically correct on Rule 11, wrong as an answer, and expensive if acted on.
