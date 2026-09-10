# device-claims-review — single-file bundle

Plugin `device-claims`. Everything needed to run this skill in a tool that cannot
read the repo: paste or upload this whole file, then give it your input.

GENERATED FILE — do not edit. Source:
device-claims/skills/device-claims-review/. Rebuild with `python3 scripts/build-portable.py`.

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

Verbatim statute text, with source URL and retrieval date, is in:

- the "mdr-ivdr-art7.md" section below — MDR Art. 7 and IVDR Art. 7
- the "hwg.md" section below — HWG § 1(1) no. 1a, § 3, § 3a, § 11
- the "uwg.md" section below — UWG § 5, § 6

**Read the "mdr-ivdr-art7.md" section below before the claim-by-claim pass.** It carries
the operative text of the four limbs and the limb-by-limb mapping table. Read the
German files when the copy targets the German market.

Every finding must cite a provision that appears in these files.

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
  § 11 applies, but **only nos. 7, 8, 9, 11 and 12** (see the "hwg.md" section below).

A B2B page that anyone can read is not automatically Fachkreise. If it is ambiguous,
ask. Do not default to Fachkreise because the product is technical — that is the
assumption that produces the most under-flagging.

---

## The review spine: four Art. 7 limbs

Operative text and the mapping table: the "mdr-ivdr-art7.md" section below.

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

**Name the risk from supplied material, or do not raise (c).** The risk must come from
the intended purpose, the IFU, the technical documentation, or something the user told
you. Do **not** infer a likely risk from the device category and then flag the copy for
omitting it — every benefit-framed advertisement omits some inferable risk, so a (c)
finding built that way is unfalsifiable and worthless. If you suspect an omission but
cannot point to the risk in supplied material, raise it as an open question:

> The copy surfaces no limitation. I can't tell from what I have whether the IFU
> records a likely risk that belongs here. Worth checking against the IFU.

Length is context. Trade-press copy is not expected to carry patient-facing safety
text; an IFU pointer is usually the proportionate fix where (c) genuinely bites.

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
the "hwg.md" section below and the "uwg.md" section below.

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
**Breach:** [MDR Art. 7(a)|(b)|(c)|(d) | HWG § 3 no. X | HWG § 11(1) no. X | UWG § 5(2) no. X | UWG § 6(2) no. X | **none**]
**Why:** [one line tying the quote to the provision's operative words]
**Evidence needed:** [what would substantiate it, or "n/a — cannot be cured by evidence"]
**Also engaged:** [optional — provisions contingent on a fact you lack, with the condition]
**Call:** [OK | Verify | Needs substantiation | Needs rewording | Cut]
**Suggested fix:** "[revised phrasing that keeps the intent]"
```

**`Also engaged:`** is an optional fourth line for provisions that would bite only if
a fact you do not have goes the wrong way — the market is Germany, the count is stale,
the certificate is narrower. Put them there with the condition named, not in `Breach:`.
`Breach:` is for what the copy breaches on the material in front of you.

```markdown
**Breach:** none
**Also engaged:** HWG § 3 no. 3(b), UWG § 5(2) no. 3 — if the "40 hospitals" count is
not current, or counts pilots as customers
**Call:** Verify
```

**`Breach: none` with `Call: Verify` is a valid and frequently correct combination.**
Use it when a claim is not misleading on the material supplied but rests on something
you have not seen — a duration, a performance figure, a certificate scope. That is an
open question for the technical file, **not** a breach. Do not promote it to a breach
to make the review look thorough.

A `Breach:` entry requires a specific provision **and** a specific reason the copy
conflicts with its operative words. "This might not be substantiated" is not a breach;
it is `Call: Verify`.

**Do not manufacture findings.** Clean copy exists. Copy that tracks the intended
purpose, states its limits, and makes no unsubstantiated performance claim should come
back with no breaches, and saying so is a useful answer. A review that always finds
something trains the reader to ignore it. If the only honest output is "no breaches
identified; two items to verify against the technical file", that is the output.

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

- **`[verified]`** — the provision appears verbatim in the reference texts below. MDR Art. 7,
  IVDR Art. 7, HWG §§ 1, 3, 3a, 11, UWG §§ 5, 6. These were retrieved from EUR-Lex
  and gesetze-im-internet on 2026-09-09 and can be re-checked against those sources.
- **`[verify]`** — anything else. Case law, MDCG guidance, national enforcement
  decisions, notified-body practice, other statutes. Tag it and say it is unverified.

**No silent supplement.** If the analysis needs a source outside the reference texts below, stop
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

---

# Reference texts

Verbatim statute text. Every finding must cite a provision that appears here.

## hwg.md

# HWG — Heilmittelwerbegesetz (German advertising law for health products)

**Source:** gesetze-im-internet.de, `heilmwerbg`
<https://www.gesetze-im-internet.de/heilmwerbg/>
**Retrieved:** 2026-09-09, verbatim German text.

**Emphasis added.** Bold inside quoted passages is mine, to mark the operative
words. It is not in the source. Everything else in a quoted block is verbatim, and
`scripts/verify-sources.py` checks that character for character.

HWG applies **in addition to** MDR/IVDR Art. 7 when the advertising is directed at
the German market. It is enforced privately through UWG (see `uwg.md`), which is
why an HWG breach usually arrives as an **Abmahnung** from a competitor or a
Wettbewerbsverband rather than as a regulator's letter.

---

## § 1(1) no. 1a — devices are in scope

> (1) Dieses Gesetz findet Anwendung auf die Werbung für
> [...]
> 1a. **Medizinprodukte im Sinne von Artikel 2 Nummer 1 der Verordnung (EU)
> 2017/745** [...] und im Sinne von **Artikel 2 Nummer 2 der Verordnung (EU)
> 2017/746** [...]

This is the hook. A product that is a device under MDR Art. 2(1) or an IVD under
IVDR Art. 2(2) is automatically inside HWG's scope for German-market advertising.
No separate qualification test.

---

## § 3 — misleading advertising (the core prohibition)

> **Unzulässig ist eine irreführende Werbung.** Eine Irreführung liegt insbesondere
> dann vor,
>
> 1. wenn Arzneimitteln, Verfahren, Behandlungen, Gegenständen oder anderen Mitteln
> eine **therapeutische Wirksamkeit oder Wirkungen beigelegt werden, die sie nicht
> haben**,
>
> 2. wenn fälschlich der Eindruck erweckt wird, daß
>    a) **ein Erfolg mit Sicherheit erwartet werden kann**,
>    b) **bei bestimmungsgemäßem oder längerem Gebrauch keine schädlichen Wirkungen
>    eintreten**,
>    c) die Werbung nicht zu Zwecken des Wettbewerbs veranstaltet wird,
>
> 3. wenn unwahre oder zur Täuschung geeignete Angaben
>    a) über die Zusammensetzung oder Beschaffenheit von Arzneimitteln, Gegenständen
>    oder anderen Mitteln oder über die Art und Weise der Verfahren oder Behandlungen
>    oder
>    b) über die Person, Vorbildung, Befähigung oder Erfolge des Herstellers,
>    Erfinders oder der für sie tätigen oder tätig gewesenen Personen
>    gemacht werden.

### Mapping to MDR Art. 7

| HWG § 3 | Overlaps MDR Art. 7 | Adds beyond Art. 7 |
|---|---|---|
| no. 1 (effects it does not have) | (a), (b) | — essentially the same test |
| no. 2(a) **guaranteed success** | — | **Yes.** Art. 7 has no explicit guarantee limb |
| no. 2(b) **no harmful effects** | (c), loosely | **Yes.** Explicit no-side-effects prohibition |
| no. 3(b) claims about the maker | — | **Yes.** Overstating credentials or track record |

**no. 2(a) and no. 2(b) are the two most commonly tripped in device marketing** and
neither has a clean MDR Art. 7 equivalent. Copy that promises certainty of outcome,
or that reassures about the absence of side effects, is an HWG finding even where
Art. 7 is arguably satisfied.

---

## § 11(1) — advertising outside professional circles (Publikumswerbung)

§ 11 restricts advertising directed at the general public rather than **Fachkreise**
(healthcare professionals, trade).

**Critical scoping rule — read this before applying § 11 to a device.** The closing
sentence of § 11(1) states:

> **Für Medizinprodukte gilt Satz 1 Nr. 7 bis 9, 11 und 12 entsprechend.**

So for medical devices, **only nos. 7, 8, 9, 11 and 12 apply.** The remaining items
in § 11(1) — including no. 2 (professional endorsements) and no. 5 (depictions of
bodily change) — do **not** apply to devices. Applying them to a device is a false
positive, and it is the single easiest way to discredit a review.

The five that do apply to devices:

| No. | Verbatim (abridged) | What it catches in device copy |
|---|---|---|
| **7** | "mit Werbeaussagen, die nahelegen, dass die Gesundheit durch die **Nichtverwendung** des Arzneimittels beeinträchtigt oder durch die **Verwendung verbessert** werden könnte" | Fear-of-not-using framing, and health-improvement-by-use framing |
| **8** | "durch **Werbevorträge**, mit denen ein Feilbieten oder eine Entgegennahme von Anschriften verbunden ist" | Webinars/talks that collect addresses or sell in the room |
| **9** | "mit Veröffentlichungen, deren **Werbezweck mißverständlich oder nicht deutlich erkennbar** ist" | Native advertising, unlabelled sponsored content, advertorial |
| **11** | "mit **Äußerungen Dritter**, insbesondere mit Dank-, Anerkennungs- oder Empfehlungsschreiben [...] wenn diese in missbräuchlicher, abstoßender oder irreführender Weise erfolgen" | Testimonials — but only where abusive, repulsive, or misleading |
| **12** | "mit Werbemaßnahmen, die sich **ausschließlich oder überwiegend an Kinder unter 14 Jahren** richten" | Copy targeted at under-14s |

Note the qualifier on no. 11: testimonials are **not** flatly banned for devices.
They are banned where they are missbräuchlich, abstoßend, or irreführend. A review
that says "testimonials are prohibited" is wrong.

No. 7 is the high-frequency one. "Don't leave your health to chance" and "improve
your heart health with X" are both no. 7 shapes.

---

## § 3a — not usually relevant to devices

> Unzulässig ist eine Werbung für **Arzneimittel**, die der Pflicht zur Zulassung
> unterliegen und die nicht [...] zugelassen sind [...]

§ 3a is limited to **Arzneimittel** (medicinal products requiring marketing
authorisation). It does not apply to devices. Do not cite it in a device review.

---

## Fachkreise vs. Publikum

§ 11 applies only **außerhalb der Fachkreise**. Before raising a § 11 finding,
establish the audience:

- **Fachkreise** — manufacturers, notified bodies, regulatory consultants,
  clinicians, procurement. § 11 does not apply. § 3 still does.
- **Publikum** — patients, carers, general public, and any public-facing web page
  with no gating. § 11 applies (nos. 7-9, 11, 12 only).

A B2B page that anyone can read is not automatically Fachkreise. Ask.

## What this file does not cover

No case law, no BGH/OLG interpretation, no Abmahnung precedent. HWG's contours in
practice are shaped by case law this reference does not verify.
See `../SKILL.md` § Limits.

---

## mdr-ivdr-art7.md

# MDR Article 7 / IVDR Article 7 — Claims

**Source:** EUR-Lex, Regulation (EU) 2017/745 (MDR), CELEX 32017R0745
<https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32017R0745>
**Retrieved:** 2026-09-09, verbatim from the consolidated EN text.

**Emphasis added.** Bold inside quoted passages is mine, to mark the operative
words. It is not in the source. Everything else in a quoted block is verbatim, and
`scripts/verify-sources.py` checks that character for character.

IVDR Article 7 (Regulation (EU) 2017/746, CELEX 32017R0746, retrieved same date)
is **textually identical** except that it governs in-vitro diagnostic devices.
Cite whichever regulation applies to the device; the analysis is the same.

---

## Verbatim text

> **Article 7**
>
> **Claims**
>
> In the labelling, instructions for use, making available, putting into service
> and advertising of devices, it shall be prohibited to use text, names,
> trademarks, pictures and figurative or other signs that may mislead the user or
> the patient with regard to the device's intended purpose, safety and performance
> by:
>
> (a) ascribing functions and properties to the device which the device does not have;
>
> (b) creating a false impression regarding treatment or diagnosis, functions or
> properties which the device does not have;
>
> (c) failing to inform the user or the patient of a likely risk associated with
> the use of the device in line with its intended purpose;
>
> (d) suggesting uses for the device other than those stated to form part of the
> intended purpose for which the conformity assessment was carried out.

---

## What each limb catches

Art. 7 is the operative test. Every finding in a review maps to one of these four
limbs or it is not an Art. 7 finding.

| Limb | The failure | Typical marketing shape |
|---|---|---|
| **(a)** functions/properties the device does not have | Overclaiming capability | "Detects all arrhythmias" when the device is cleared for atrial fibrillation only |
| **(b)** false impression re treatment or diagnosis | Implied clinical benefit the device does not deliver | Wellness-framed copy that reads as diagnosis; "know your heart is healthy" |
| **(c)** failing to inform of a likely risk | Omission, not commission | Benefit-only copy with no mention of a known limitation or contraindication |
| **(d)** uses beyond the intended purpose assessed | Intended-purpose drift | "Great for athletes tracking recovery" when the intended purpose is clinical monitoring |

**Limb (d) is the one generic marketing review misses.** It is not a truthfulness
test. A claim can be entirely true and still breach (d) if the use it suggests
falls outside the intended purpose that the conformity assessment covered. The
anchor is the **intended purpose as assessed**, not what the device can factually do.

Limb (c) is likewise not a truthfulness test — it is an **omission** test. Copy
that says nothing false can still breach (c).

## Scope note

Art. 7 covers "labelling, instructions for use, making available, putting into
service and advertising". It is **not** limited to advertising. Product pages,
IFU excerpts reproduced in marketing, sales decks, and trade-show panels are all
in scope.

## What this file does not cover

No case law. No national enforcement decisions. No MDCG guidance interpretation.
Those exist and can change the analysis; they are outside what this reference
verifies. See `../SKILL.md` § Limits.

---

## uwg.md

# UWG — Gesetz gegen den unlauteren Wettbewerb

**Source:** gesetze-im-internet.de, `uwg_2004`
<https://www.gesetze-im-internet.de/uwg_2004/>
**Retrieved:** 2026-09-09, verbatim German text.

**Emphasis added.** Bold inside quoted passages is mine, to mark the operative
words. It is not in the source. Everything else in a quoted block is verbatim, and
`scripts/verify-sources.py` checks that character for character.

UWG matters here for two reasons:

1. It is the **enforcement vehicle**. MDR Art. 7 and HWG have no private right of
   action of their own in the usual case; a competitor or a Wettbewerbsverband
   enforces them through UWG, typically by **Abmahnung** with a
   strafbewehrte Unterlassungserklärung attached. This is why a device-marketing
   breach shows up as a cease-and-desist letter with costs, not a regulator's notice.
2. **§ 6** independently governs comparative advertising, which MDR Art. 7 and HWG
   do not address at all.

---

## § 5 — misleading commercial practices

> **(1)** Unlauter handelt, wer eine **irreführende geschäftliche Handlung** vornimmt,
> die geeignet ist, den Verbraucher oder sonstigen Marktteilnehmer zu einer
> geschäftlichen Entscheidung zu veranlassen, die er andernfalls nicht getroffen
> hätte.
>
> **(2)** Eine geschäftliche Handlung ist irreführend, wenn sie unwahre Angaben
> enthält oder sonstige zur Täuschung geeignete Angaben über folgende Umstände
> enthält:
>
> 1. die **wesentlichen Merkmale** der Ware oder Dienstleistung wie Verfügbarkeit,
> Art, Ausführung, **Vorteile, Risiken**, Zusammensetzung, Zubehör, Verfahren oder
> Zeitpunkt der Herstellung, Lieferung oder Erbringung, **Zwecktauglichkeit,
> Verwendungsmöglichkeit**, Menge, Beschaffenheit, Kundendienst und
> Beschwerdeverfahren, geographische oder betriebliche Herkunft, **von der Verwendung
> zu erwartende Ergebnisse** oder die Ergebnisse oder wesentlichen Bestandteile von
> **Tests** der Waren oder Dienstleistungen;
>
> 2. den Anlass des Verkaufs wie das Vorhandensein eines besonderen Preisvorteils,
> den Preis oder die Art und Weise, in der er berechnet wird [...];
>
> 3. die **Person, Eigenschaften oder Rechte des Unternehmers** wie Identität,
> Vermögen einschließlich der Rechte des geistigen Eigentums, den Umfang von
> Verpflichtungen, Befähigung, **Status, Zulassung**, Mitgliedschaften oder
> Beziehungen, Auszeichnungen oder Ehrungen [...];
>
> 4. **Aussagen oder Symbole**, die im Zusammenhang mit direktem oder indirektem
> Sponsoring stehen oder sich auf eine **Zulassung des Unternehmers oder der Waren
> oder Dienstleistungen** beziehen;
>
> 5. die Notwendigkeit einer Leistung, eines Ersatzteils, eines Austauschs oder
> einer Reparatur.

### The device-specific hooks in § 5(2)

- **no. 1 "Zwecktauglichkeit / Verwendungsmöglichkeit"** — fitness for purpose and
  possible use. This is the UWG mirror of MDR Art. 7(d) intended-purpose drift.
- **no. 1 "von der Verwendung zu erwartende Ergebnisse"** — expected results.
  Outcome claims land here.
- **no. 1 "Tests"** — claims about test results and their essential components.
  Cherry-picked clinical or bench data lands here.
- **no. 3 / no. 4 "Status, Zulassung"** — **certification and approval status.**
  This is the CE-marking misrepresentation hook. Copy implying a class, a notified
  body involvement, or a certification the device does not hold is a § 5 finding
  independent of whether the performance claims are true.

The § 5(1) materiality filter matters: the statement must be **geeignet**, capable
of causing a commercial decision the reader would not otherwise have made. A
trivially wrong detail nobody buys on is not automatically a § 5 breach.

---

## § 6 — comparative advertising

> **(1)** Vergleichende Werbung ist jede Werbung, die unmittelbar oder mittelbar
> einen **Mitbewerber** oder die von einem Mitbewerber angebotenen Waren oder
> Dienstleistungen **erkennbar** macht.
>
> **(2)** Unlauter handelt, wer vergleichend wirbt, wenn der Vergleich
>
> 1. sich nicht auf Waren oder Dienstleistungen für den **gleichen Bedarf oder
> dieselbe Zweckbestimmung** bezieht,
>
> 2. nicht **objektiv** auf eine oder mehrere **wesentliche, relevante,
> nachprüfbare und typische** Eigenschaften oder den Preis dieser Waren oder
> Dienstleistungen bezogen ist,
>
> 3. im geschäftlichen Verkehr zu einer **Gefahr von Verwechslungen** zwischen dem
> Werbenden und einem Mitbewerber [...] führt,
>
> 4. den **Ruf** des von einem Mitbewerber verwendeten Kennzeichens in unlauterer
> Weise **ausnutzt oder beeinträchtigt**,
>
> 5. die Waren, Dienstleistungen, Tätigkeiten oder persönlichen oder geschäftlichen
> Verhältnisse eines Mitbewerbers **herabsetzt oder verunglimpft** [...]

### How to apply § 6 to a comparison page

Comparative advertising is **lawful in Germany** when it satisfies § 6(2). It is not
banned. The test is cumulative — a comparison must clear every limb.

The two that fail most often on a SaaS/device comparison page:

- **§ 6(2) no. 1 — same need or same purpose.** Comparing products with different
  intended purposes fails here before you reach accuracy. Two devices in different
  MDR classes or with different intended purposes are often not comparable at all.
- **§ 6(2) no. 2 — objective, essential, relevant, verifiable, typical.**
  "Verifiable" (*nachprüfbar*) is the sharp edge: the reader must be able to check
  the claim. A comparison table cell that cannot be verified from public
  information fails no. 2 even if it is accurate.

**"Erkennbar" in § 6(1) is broad.** A competitor does not need to be named. "Unlike
legacy EUDAMED tools" identifies a competitor if the market can tell who is meant.
Anonymised comparisons are still comparative advertising.

---

## Abmahnung — why this is the expensive failure mode

A UWG breach is typically enforced by a competitor sending an **Abmahnung**
demanding a **strafbewehrte Unterlassungserklärung** (a cease-and-desist undertaking
backed by a contractual penalty) plus reimbursement of legal costs. Signing one
creates a standing penalty exposure for any repeat. This is a private-party
mechanism, fast, and it does not require a regulator to act.

Practical consequence for review priority: a claim that is **verifiable and
narrow** is cheap to defend; a claim that is broad and unverifiable is expensive
even when it happens to be true.

## What this file does not cover

UWG's practical contours are heavily case-law-driven (BGH and OLG), and comparative
advertising in particular shifts. This reference verifies **statute text only**.
Do not assert how a court would rule. See `../SKILL.md` § Limits.

---
