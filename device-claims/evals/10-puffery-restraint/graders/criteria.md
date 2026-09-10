---
type: llm
weight: 1
---

This is pure puffery. It makes no performance claim, no clinical claim, no
comparison, and no statement about certification. "Surgeons love it" is subjective
preference, not an assertion about what the device does.

The skill's own taxonomy says puffery with no clinical or performance content need
not be listed as a finding.

PASS requires:
(1) No provision is ASSERTED AS BREACHED. Judge how a provision is used, not whether
    its string appears.
      - PASS: `Breach: none`.
      - PASS: a provision under `Also engaged:` with its condition named. That line is
        the skill's mechanism for exactly this situation and must not be marked down.
      - PASS: a provision named in order to exclude it ("§ 11 does not apply —
        Fachkreise").
      - FAIL: a provision on a `Breach:` line, or prose asserting the copy breaches it.
(2) HWG § 11 is not applied (Fachkreise audience, and nothing in the copy engages
    nos. 7-9, 11 or 12 in any case).
(3) The response does not present the copy as breaching anything. `Call: Verify`,
    `Call: Needs substantiation` and `Ready to publish: With changes below` are all
    acceptable and do NOT count as findings for this case.
(4) The `## Limits` block is present and the response does not emit
    "Ready to publish: Yes" — SKILL.md forbids that for a non-lawyer user.

FAIL if any Art. 7 limb, HWG or UWG provision is asserted as breached. This tests
whether the skill can say "nothing here", which the no-skill baseline could not do
on the other clean-copy case.
