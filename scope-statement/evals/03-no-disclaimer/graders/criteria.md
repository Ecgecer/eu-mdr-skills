---
type: llm
weight: 1
---

PASS requires:
(1) The block is short, as asked, and still carries a "Not checked" line and a
    negation. Brevity must not cost the two load-bearing lines.
(2) "Not checked" reflects the actual mechanism: regex and dictionary matching misses
    personal data it has no pattern for, and the check covers the uploaded file at
    upload time only, not data entered later, not other systems.
(3) The negation denies the inference a reader draws: that a clean result means the
    file contains no personal data, or that they are GDPR compliant.
(4) It is NOT generic legal boilerplate. No "for informational purposes only", no
    "consult a data protection officer" as a substitute for describing coverage.
    A pointer to a DPO is acceptable IN ADDITION to a real scope description, never
    instead of it.

FAIL if brevity is used as an excuse to drop the negation, or if the output is a
disclaimer wearing a scope statement's name.
