---
name: device-claims-review
description: >
  Review marketing copy for a medical device or IVD against MDR/IVDR Article 7,
  the German Heilmittelwerbegesetz (HWG), and UWG §§ 5 and 6. Use when the user
  says "review this device copy", "can we claim this", "is this claim MDR
  compliant", "check this product page", "Abmahnung risk", or pastes marketing
  content for a device, IVD, or SaMD (landing pages, brochures, ads, trade-show
  panels, sales decks, IFU excerpts used in marketing).
argument-hint: "[paste copy, or file path]"
---

# Device Claims Review

Review advertising and labelling copy for a medical device or IVD against the
statutory prohibitions on misleading claims.

Three layers apply, and they are cumulative. Copy must clear all three:

| Layer | Instrument | Applies |
|---|---|---|
| EU | **MDR Art. 7** / **IVDR Art. 7** | Always, for any device placed on the EU market |
| DE | **HWG** § 3, § 11 | When advertising targets the German market |
| DE | **UWG** § 5, § 6 | Enforcement vehicle; § 6 governs comparisons independently |

Verbatim statute text is in `references/`. Every finding must cite a provision
that appears there.

---

## Step 0 — Establish the two anchors before reviewing anything

**Do not begin the claim-by-claim pass until both are settled.** Guessing either
one produces confident, wrong findings.

### Anchor 1 — The intended purpose as assessed

Ask for, or locate, the device's **intended purpose** exactly as it appears in the
conformity assessment / technical documentation / Declaration of Conformity.

This is the reference point for MDR Art. 7(d). Not what the device can do. Not what
the engineering team says it does. **The intended purpose the conformity assessment
covered.**

If the user cannot supply it, say so and stop the (d) analysis:

> I can review limbs (a), (b) and (c) without the intended purpose, but (d) —
> suggesting uses beyond the assessed intended purpose — is the limb device
> marketing trips most often, and I cannot assess it against a purpose I have not
> seen. Can you paste the intended purpose from the technical documentation or DoC?

Also capture, if available: device class, whether a notified body was involved, and
the certificate scope. Claims about these are UWG § 5(2) no. 3/4 territory.

### Anchor 2 — The audience

HWG § 11 applies **only outside Fachkreise**. Establish which:

- **Fachkreise** — manufacturers, notified bodies, regulatory consultants,
  clinicians, hospital procurement, trade press. § 11 does **not** apply. § 3 does.
- **Publikum** — patients, carers, general public, and any ungated public web page.
  § 11 applies, but **only nos. 7, 8, 9, 11 and 12** (see `references/hwg.md`).

A B2B page that anyone can read is not automatically Fachkreise. If it is ambiguous,
ask. Do not default to Fachkreise because the product is technical — that is the
assumption that produces the most under-flagging.

---

## The review spine: four Art. 7 limbs

Classify every finding under the limb it breaches. A finding that maps to no limb
and no HWG/UWG provision is not a finding — drop it or mark it as a drafting note.

### (a) Ascribing functions or properties the device does not have

Overclaiming capability. Test against the intended purpose and the performance data.

Shapes: "detects all X" when cleared for a subset; absolute performance figures with
no study behind them; capability stated without the qualifying condition.

### (b) Creating a false impression regarding treatment or diagnosis

Implied clinical benefit. This catches copy that never states a false fact but
leaves a clinical impression the device does not support.

Shapes: wellness framing that reads as diagnosis; reassurance language ("know your
heart is healthy"); outcome implication from a monitoring-only device.

### (c) Failing to inform of a likely risk

**An omission test, not a truthfulness test.** Copy containing nothing false can
still breach (c).

Shapes: benefit-only copy with no mention of a known limitation, contraindication,
or the fact that results require clinical interpretation.

Ask: is there a **likely** risk associated with use in line with the intended
purpose that this copy does not surface? "Likely" is the statutory word — not every
theoretical risk belongs in an ad.

### (d) Suggesting uses beyond the assessed intended purpose

**Not a truthfulness test either.** A true claim breaches (d) if the use it suggests
falls outside what the conformity assessment covered.

Shapes: new user population ("also great for athletes"); new setting ("use at home"
for a clinical device); new indication; adjacent-use suggestion in a testimonial or
image.

This limb is the reason a generic marketing review is insufficient for a device.
Check it explicitly on every asset, including images and captions.

---

## German overlay

Apply when the copy targets the German market. Details and verbatim text in
`references/hwg.md` and `references/uwg.md`.

### HWG § 3 — adds two prohibitions Art. 7 does not have

- **§ 3 no. 2(a) — guaranteed success.** "Erfolg mit Sicherheit". Any promise that
  an outcome is certain. Art. 7 has no explicit guarantee limb; this is additive.
- **§ 3 no. 2(b) — no harmful effects.** Claiming that proper or prolonged use
  produces no harmful effects. Additive.
- **§ 3 no. 3(b)** — overstating the maker's credentials, qualifications or track
  record.

### HWG § 11 — only if the audience is Publikum

For devices, **only nos. 7, 8, 9, 11, 12 apply.** Citing any other § 11 item against
a device is a false positive.

- **no. 7** (highest frequency): copy suggesting health is impaired by *not* using
  the device, or improved by using it.
- **no. 9**: advertorial or native content whose promotional purpose is not clearly
  recognisable.
- **no. 11**: third-party testimonials **where abusive, repulsive or misleading**.
  Testimonials are not flatly prohibited for devices — do not report them as such.

### UWG § 5 — certification and status claims

Beyond general misleadingness, § 5(2) nos. 3 and 4 cover **Status, Zulassung** —
approval and certification status. Copy implying a class, notified-body involvement,
or a certificate the device does not hold is a finding here independently of whether
the performance claims are accurate.

### UWG § 6 — comparisons

Comparative advertising is **lawful** in Germany when it clears every limb of
§ 6(2). Do not report comparisons as prohibited. Test:

1. **no. 1** — same need or same intended purpose? Devices with different intended
   purposes often are not comparable at all, which fails before accuracy is reached.
2. **no. 2** — objective, and on **essential, relevant, verifiable, typical**
   characteristics. *Verifiable* is the sharp edge: can the reader check it from
   public information?

A competitor need not be named. "Unlike legacy tools" is comparative advertising if
the market can tell who is meant.

---

## Workflow

### Step 1 — Extract every claim

List every phrase asserting a fact, making a comparison, promising an outcome, or
implying a clinical benefit. Include image captions, alt text, headline claims, and
badge/seal graphics. Pure puffery with no clinical or performance content need not
be listed.

### Step 2 — Classify and call

For each claim:

```markdown
**Claim:** "[exact quote]"
**Breach:** [MDR Art. 7(a)|(b)|(c)|(d) | HWG § 3 no. X | HWG § 11(1) no. X | UWG § 5(2) no. X | UWG § 6(2) no. X | none]
**Why:** [one line tying the quote to the provision's operative words]
**Evidence needed:** [what would substantiate it, or "n/a — cannot be cured by evidence"]
**Call:** [OK | Needs substantiation | Needs rewording | Cut]
**Suggested fix:** "[revised phrasing that keeps the intent]"
```

Distinguish the two cure paths. A limb (a) overclaim can often be cured by
**evidence**. A limb (d) intended-purpose breach usually **cannot** — it is cured by
narrowing the claim or by extending the conformity assessment, not by data.

### Step 3 — Output

```markdown
# Device Claims Review: [asset]

**Reviewed:** [date]
**Device / IVD:** [name] — [class if known]
**Intended purpose (as assessed):** [quoted, or "NOT SUPPLIED — limb (d) not assessed"]
**Audience:** [Fachkreise | Publikum | ambiguous — assumed X, confirm]
**Markets:** [EU | DE | other]

## Summary

[N] claims reviewed. [N] cut, [N] reword, [N] substantiate, [N] OK.

**Ready to publish:** [Yes | With changes below | No — rewrite needed]

## Findings
[claim blocks, ordered Cut > Reword > Substantiate > OK]

## Evidence to gather before publishing
| Claim | Evidence needed | From whom |

## Provisions cited
[list, each with its reference file]

## Limits
[the block from § Limits below, verbatim]
```

For assets under 50 words, the fix block must contain the **actual revised copy**,
paste-ready, not a description of what to change.

---

## Citation discipline

Two tiers only. Do not invent others.

- **`[verified]`** — the provision appears verbatim in `references/`. MDR Art. 7,
  IVDR Art. 7, HWG §§ 1, 3, 3a, 11, UWG §§ 5, 6. These were retrieved from EUR-Lex
  and gesetze-im-internet on 2026-09-09 and can be re-checked against those sources.
- **`[verify]`** — anything else. Case law, MDCG guidance, national enforcement
  decisions, notified-body practice, other statutes. Tag it and say it is unverified.

**No silent supplement.** If the analysis needs a source outside `references/`, stop
and say so:

> This turns on [case law / MDCG guidance / a provision] that this skill does not
> verify. I can flag it as an open question, or you can point me at the source.
> I will not state a rule I cannot cite from the reference files.

Never state how a German court would decide. The references are statute text; the
case law that shapes their application is out of scope.

---

## Limits

Include this in every output.

> This review checks copy against the verbatim text of MDR Art. 7, IVDR Art. 7,
> HWG §§ 3 and 11, and UWG §§ 5 and 6, retrieved from EUR-Lex and
> gesetze-im-internet on 2026-09-09. It does **not** cover case law, MDCG guidance,
> notified-body practice, national enforcement decisions, or any market outside the
> EU and Germany. UWG in particular is heavily shaped by BGH and OLG case law that
> this review does not assess. It is a drafting and risk-triage aid, not legal
> advice, and it is not a substitute for a Fachanwalt für Medizinrecht or
> Wettbewerbsrecht.

## Before answering "Ready to publish: Yes"

Approving device copy for publication is a legal act. Art. 7 breaches attach to the
manufacturer, and UWG exposure arrives as an Abmahnung with costs.

If the user is not a qualified lawyer, do not emit "Ready to publish: Yes". Emit
instead:

> I can say the copy has no findings I can identify against the provisions I verify.
> I can't clear it for publication — that call needs someone qualified, because
> case law I don't assess can change the analysis. Here's a one-page brief to take
> to counsel: [asset, claims cleared, provisions checked, open questions, the three
> things to ask].

"With changes below" and "No — rewrite needed" are review calls, not approvals, and
do not require this gate.
