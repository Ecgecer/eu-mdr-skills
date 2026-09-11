---
type: llm
weight: 1
---

Independent software (3.3 does not divert it), so Rule 11 applies. It provides
information used to take a decision with diagnostic/therapeutic purpose, limb 1,
base class IIa. The escalation test is the IMPACT OF THE DECISION: a missed or wrong
large-vessel-occlusion triage decision may cause death or irreversible neurological
deterioration. That is the class III trigger.

PASS requires:
(1) The stated class is **III**.
(2) It reaches III through **Rule 11 limb 1's escalation**, on the basis that the
    decision may cause death or irreversible deterioration, not merely because
    stroke is a serious disease.
(3) It addresses 3.3. That the software is independent, so 3.3 does not divert it to
    another device's class. Merely reaching Rule 11 without mentioning 3.3 does not
    satisfy this; 3.3 runs first and skipping it is the error `driving-software-3-3`
    exists to catch.

Accept IIb ONLY if the response explicitly reasons that the relevant impact is
serious deterioration or a surgical intervention rather than death/irreversible harm,
AND acknowledges the III trigger and explains why it does not apply. A bare IIb with
no such reasoning is a FAIL.

FAIL if the answer is IIa or I, or if the escalation is justified by disease severity
alone rather than by what the decision may cause.
