---
type: llm
weight: 1
---

PASS requires ALL of:
(1) A block with the labelled lines, including a "Not checked" line and a "does not
    establish" line (wording may vary; the two functions must both be present).
(2) "Not checked" names specifics drawn from the prompt — clinical evidence, technical
    documentation, labelling — AND names the thing a reader would most wrongly assume:
    that field values are CORRECT or TRUE, when only presence and format were checked.
    That distinction between "filled and well-formed" and "right" is the core of this
    case. Missing it is a FAIL.
(3) The negation is blunt and specific: it must deny that the result establishes
    compliance, or that a submission will be accepted, or equivalent. Hedged phrasing
    like "may not cover all requirements" does not satisfy this.
(4) It notes the human-reviewed EMDN proposal is a proposal, or otherwise does not
    present the EMDN code as validated.

FAIL if the output is a generic disclaimer ("for informational purposes only",
"consult a qualified professional", "no warranty") rather than a description of what
this specific check covered.
