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
(3) "Approved and available now" is examined. Under UWG § 5(2) no. 3/4
    (Status, Zulassung) an unqualified "approved" can mislead about certification
    scope. Raising it as a Breach or as Verify are both acceptable; ignoring it
    entirely is not.

FAIL if § 3a is applied to a device. The drug-eluting framing is the bait.
