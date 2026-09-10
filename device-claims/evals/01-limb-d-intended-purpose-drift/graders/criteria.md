---
type: llm
weight: 1
---

The response MUST flag "Athletes love it for tracking recovery" as a breach
of MDR Art. 7(d) — suggesting a use outside the assessed intended purpose
(which is clinical arrhythmia detection under HCP supervision).
It MUST NOT treat this as a truthfulness problem or say it can be cured by
evidence/substantiation; the correct cure is narrowing the claim or
extending the conformity assessment.
It should also note the loss of the HCP-supervision element ("just peel,
stick, and train").
PASS only if Art. 7(d) is identified by name.

Additionally, no market is stated in this prompt. The response must either ask which
market applies or refrain from asserting HWG or UWG findings. Applying German national
law to a prompt that never mentions Germany is the error `non-german-eu-market` exists
to catch, and it should not pass here.
