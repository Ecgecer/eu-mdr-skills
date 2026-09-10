---
type: llm
weight: 1
---

This is the boundary test. The software TREATS. It does not provide information used
to take a decision (limb 1) and does not monitor physiological processes (limb 2), so
Rule 11 alone lands it at limb 3 — "all other software" — which is class I.

That is almost certainly the wrong final answer, because implementing rule 3.5 says
the strictest applicable rule wins, and a rule this skill does not carry (the active
therapeutic device rule, Rule 9) plausibly reaches software that delivers treatment.

PASS requires BOTH:
(1) It does NOT present a confident final class. It must flag that implementing rule
    3.5 means a stricter rule may apply, and that Rules 1-10 and 12-22 are not carried
    here, so the Rule 11 result is a floor rather than the answer.
(2) It correctly works Rule 11 to limb 3 / class I as the Rule-11-only result, or
    explains why limbs 1 and 2 are not engaged.

Naming Rule 9 or "active therapeutic device" specifically is a bonus, not required —
the skill does not carry that rule, so it cannot be expected to name it. What IS
required is recognising that the question is not settled by Rule 11.

FAIL if it states a final class (I, IIa, IIb or III) without flagging the 3.5 /
uncarried-rule problem. A confident "class I" is the specific failure being tested:
technically correct on Rule 11, wrong as an answer, and expensive if acted on.
