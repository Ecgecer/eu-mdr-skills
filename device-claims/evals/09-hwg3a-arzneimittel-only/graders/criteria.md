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
(2) HWG § 11 is NOT applied — the audience is Fachkreise.
(3) "Approved and available now" is examined. The device is stated to be CE marked
    with a notified body involved, so on the supplied material there is no basis to
    assert it misleads. The correct shape is `Breach: none` + `Also engaged: UWG
    § 5(2) no. 4` (a claim about the goods' approval status) + `Call: Verify`.
    A bare `Breach: UWG § 5` with no stated conflict with the supplied facts is a FAIL —
    SKILL.md says "Do not promote it to a breach to make the review look thorough."
    Ignoring the line entirely is also a FAIL.
(4) The Art. 7 limbs are opened on "sustained drug release across the full lesion",
    which is a performance claim. `Breach: none` + `Call: Verify` is acceptable;
    not examining it at all is not.

FAIL if § 3a is applied to a device. The drug-eluting framing is the bait.
