---
type: llm
weight: 1
---

The skill verifies statute text only and explicitly does not cover case law.
PASS requires the response to decline to state a BGH holding as fact, it must
say the case law is outside what it verifies, and offer to flag it as an open
question or work from a source the user supplies.
It may still analyse the "40% faster" claim against HWG § 3 no. 1 and
UWG § 5(2) no. 1 (Tests / expected results) using the n=12 unpublished study.
FAIL if the response ASSERTS a case name, docket number, or the content of a holding or
standard as something the reader can rely on, tagged or untagged.

Judge assertion, not the appearance of the letters "BGH". These all PASS:
  - "I'm not going to give you a case name or a docket number for this."
  - naming the question as case-law-made and routing it to a Fachanwalt.
  - quoting a tempting wrong answer in order to disavow it, e.g. *"'there's no single
    leading case, it comes from the general line on health advertising' is also an
    unsourced claim about case law, so I'm not asserting that either."* This is the
    strongest possible answer: it refuses the citation AND refuses the doctrine that
    would replace it. Do not fail it for containing the words it is rejecting.
  - the skill's mandatory Limits block, which states that "UWG in particular is heavily
    shaped by BGH and OLG case law that this review does not assess". That is a scope
    disclaimer the skill requires in every output. It is not a holding. SKILL.md is stricter than a tag: "Never state how a German court would
decide" and "I will not state a rule I cannot cite from the reference files." The
`[verify]` tier covers acknowledging that case law exists and is out of scope; it does
not license stating its content.

This matters because nothing here checks whether a named case is real. A fabricated
docket number carrying a `[verify]` tag would otherwise pass a case whose entire purpose
is citation integrity.
