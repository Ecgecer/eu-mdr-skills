---
type: llm
weight: 1
---

This is Publikumswerbung for a MEDICAL DEVICE. Under HWG § 11(1) final
sentence, only nos. 7, 8, 9, 11 and 12 apply to devices.
PASS requires:
(1) "Don't gamble with your heart" IS flagged under § 11(1) no. 7
    (suggesting health is impaired by not using the device).
(2) § 11(1) no. 2 is not APPLIED to this device. Judge how the provision is
    USED, not whether the string appears anywhere in the response.
      - PASS: no. 2 is never mentioned.
      - PASS: no. 2 is mentioned in order to EXCLUDE it, e.g. "§ 11(1) no. 2
        does not apply to Medizinprodukte — only nos. 7-9, 11 and 12 do".
        This is the correct answer. Showing the exclusion is better than
        silence, not worse, and must not be marked down.
      - FAIL: no. 2 is reported as a live finding — the endorsement is said to
        breach it, or it appears in a Breach: line for this device.
    If the endorsement is raised as a finding at all it must be under no. 11, § 3, or
    UWG § 5 — and if under no. 11, the response must APPLY the missbräuchlich /
    abstoßend / irreführend qualifier and say whether it is met. A flat
    "testimonials are prohibited in Publikumswerbung" is a FAIL: references/hwg.md says
    in terms that such a review "is wrong".
(3) No § 11(1) item outside {7, 8, 9, 11, 12} is applied to this device. The closing
    sentence of § 11(1) limits devices to those five; citing no. 3, no. 5 or any other
    is the same error as no. 2.
This is the most important false-positive check in the suite. Read the sentence
around any occurrence of "no. 2" before voting.
