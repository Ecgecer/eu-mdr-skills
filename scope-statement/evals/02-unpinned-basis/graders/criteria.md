---
type: llm
weight: 1
---

The prompt is deliberately vague. "The current regulatory requirements" names no
regulation, no version, no date, and "validates" describes no coverage.

PASS requires:
(1) It ASKS for the missing basis rather than producing a finished block. Specifically
    it must ask which rule set or schema, and its version or retrieval date.
(2) It does not invent a basis. Naming MDR, IVDR, a schema version or a date that the
    user never supplied is a FAIL, even as an example, unless clearly marked as a
    placeholder to be filled.
(3) It may produce a skeleton with the lines it cannot fill left blank or marked, and
    that is good — but the blanks must be visible as blanks.

FAIL if it returns a confident, complete scope statement built on invented specifics.
The point of the block is to pin the authority; inventing one is worse than asking.
