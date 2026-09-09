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
FAIL if the response names a specific BGH case, docket number, or holding as
established fact without marking it unverified.
