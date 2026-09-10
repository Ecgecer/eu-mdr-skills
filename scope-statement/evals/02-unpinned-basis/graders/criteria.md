---
type: llm
weight: 1
---

The prompt is deliberately vague. "The current regulatory requirements" names no
regulation, no version, no date, and "validates" describes no coverage.

PASS requires:
(1) It ASKS for the missing basis rather than producing a finished block. Specifically
    it must ask which rule set or schema, and its version or retrieval date.
(2) It does not present an INVENTED basis as the pinned one. Judge how the authority
    is used, not whether its name appears.
      - PASS: named inside a question about which applies ("MDR Annex I GSPRs? an
        EUDAMED schema version? your own internal ruleset?"). Offering candidates is
        asking, not inventing.
      - PASS: named as a bracketed placeholder to be filled.
      - FAIL: named on an `Against:` line as the established basis of a finished block.
(3) It produces the block skeleton with the unfillable lines visibly marked. A bare
    clarifying question with no skeleton is a partial answer — acceptable but weaker,
    since the skill can still deliver the structure and say which values are missing.

FAIL if it returns a confident, complete scope statement built on invented specifics.
The point of the block is to pin the authority; inventing one is worse than asking.
