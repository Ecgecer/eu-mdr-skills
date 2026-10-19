# Blind re-grade, 2026-10-19

Every failed baseline run of the nine-run batch, plus one passing run per case mixed in, re-graded
by a separate model given only `items/` (question, grader criteria, response). It never saw
`blind-key.json`, which maps item ids to case, run and the harness judge's verdict. `extract.py`
produced the items. The grader's verdicts, verbatim:

| Item | Case, run (from key) | Harness judge | Blind grader | Blind grader's reason |
|---|---|---|---|---|
| 4f21c4d0dd | eudamed-mdr-ivdr-anchor | FAIL | FAIL | Both deadlines in 2027 ("28 May 2027") on one anchor |
| 50e01ddea1 | eudamed-mdr-ivdr-anchor | FAIL | FAIL | "about 27–28 May 2027", calls counting from publication a common mistake |
| 6f1d2e1775 | eudamed-mdr-ivdr-anchor | FAIL | FAIL | "28 May 2027" for both; Nov 2026 window given only to MDR/IVDR-certified devices |
| 7e68538d23 | eudamed-mdr-ivdr-anchor | FAIL | FAIL | "late May 2027" for both, one anchor |
| 7fa5e2cd26 | eudamed-mdr-ivdr-anchor | FAIL | FAIL | "late May 2027 for both products", "the two deadlines should be the same day" |
| 8b3f88d09b | eudamed-mdr-ivdr-anchor | FAIL | FAIL | "late May 2027" for both |
| c4fbb4cac4 | eudamed-mdr-ivdr-anchor | FAIL | FAIL | "28 May 2027", 12 months after the mandatory-use date for both |
| e01673417d | eudamed-mdr-ivdr-anchor | FAIL | FAIL | "28 May 2027" for both, separate articles but one anchor |
| e5115995ed | eudamed-mdr-ivdr-anchor | FAIL | FAIL | "27/28 May 2027" for both; Nov 2026 window given only to MDR/IVDR-certified devices |
| 9e64f8e9a4 | eudamed-nb-enters-certificates run 4 | **FAIL** | **PASS** | Corrects both premises: "the notified body enters the certificates"; "no SSCP is required" |
| a8297ea986 | eudamed-nb-enters-certificates run 1 (passing run) | PASS | PASS | "Your notified body uploads the certificates, not you"; "no SSCP to submit" |
| aba8524acd | nb-certificate-number run 1 (passing run) | PASS | PASS | Certificate fields marked "From the actual certificate"; no invented identifier |

Agreement 11 of 12. Under the rule fixed before the run (README, commit 1f4278d), the
disagreeing run does not count as a failure.
