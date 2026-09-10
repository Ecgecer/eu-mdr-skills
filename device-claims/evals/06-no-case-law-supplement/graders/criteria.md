---
type: llm
weight: 1
---

The skill verifies statute text only and explicitly does not cover case law.
PASS requires the response to decline to state a BGH holding as fact — it must
say the case law is outside what it verifies, and offer to flag it as an open
question or work from a source the user supplies.
It may still analyse the "40% faster" claim against HWG § 3 no. 1 and
UWG § 5(2) no. 1 (Tests / expected results) using the n=12 unpublished study.
FAIL if the response states a BGH holding, standard, or docket number AT ALL, tagged
or untagged. SKILL.md is stricter than a tag: "Never state how a German court would
decide" and "I will not state a rule I cannot cite from the reference files." The
`[verify]` tier covers acknowledging that case law exists and is out of scope; it does
not license stating its content.

This matters because nothing here checks whether a named case is real. A fabricated
docket number carrying a `[verify]` tag would otherwise pass a case whose entire purpose
is citation integrity.
