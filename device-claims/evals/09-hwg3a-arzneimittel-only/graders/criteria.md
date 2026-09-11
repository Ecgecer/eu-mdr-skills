---
type: llm
weight: 1
---

This is a MEDICAL DEVICE that carries a drug. It is not an Arzneimittel.

HWG § 3a prohibits advertising a medicinal product that requires marketing
authorisation and does not have one. It applies to Arzneimittel only, and the
reference file says so explicitly.

PASS requires:
(1) HWG § 3a is NOT applied to this device.
      - PASS: § 3a is not mentioned, or is mentioned only to exclude it
        ("§ 3a covers Arzneimittel, not devices").
      - FAIL: § 3a appears in a Breach: line, or the response says the stent
        needs a marketing authorisation it lacks.
(2) HWG § 11 is NOT applied. The audience is Fachkreise.
(3) "Approved and available now" is examined, and NOT asserted as breached. The device
    is stated to be CE marked with a notified body involved, so on the supplied material
    there is no basis to say it misleads. Any of these pass: `Breach: none`; a provision
    under `Also engaged:` with its condition named; `Call: Verify`; or prose reaching the
    same place. Judge the CONCLUSION and its reasoning, not the format.
    FAIL only if it is asserted as breached with no stated conflict with the supplied
    facts, or if the line is ignored entirely.
(4) The Art. 7 limbs are opened on "sustained drug release across the full lesion".
    Any sound treatment passes, including reasoning that it reads two ways (as a device
    property under 7(a), curable by data; or as an indication under 7(d), not curable).
    FAIL only if the phrase is not examined at all.

Note for the judge: this skill's output format is a guide, not a checklist. A response
that reaches the right conclusion with sound reasoning in prose passes. Do not fail it
for wording a Breach line differently.

FAIL if § 3a is applied to a device. The drug-eluting framing is the bait.
