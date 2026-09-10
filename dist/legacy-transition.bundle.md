# legacy-transition — single-file bundle

Plugin `mdr-transition`. Everything needed to run this skill in a tool that cannot
read the repo: paste or upload this whole file, then give it your input.

GENERATED FILE — do not edit. Source:
mdr-transition/skills/legacy-transition/. Rebuild with `python3 scripts/build-portable.py`.

---

# MDR Article 120 — the legacy transition

Answer from the **amended** text in the "art120-amended.md" section below. Read it before
answering.

**The single most important thing about this provision:** Article 120 was substantially
rewritten by Regulation (EU) 2023/607 in March 2023. The original 2017 text set one
deadline — **26 May 2024** — for placing legacy devices on the market. That is superseded.
An answer citing 26 May 2024 as the market deadline is quoting law that no longer applies,
and it is the answer a model recalling the 2017 text will give.

---

## Step 0 — Three facts before any date

Ask for whatever is missing. The deadline is class-dependent and condition-dependent, so a
date given without these is a guess.

1. **Class under MDR** — III, IIb, IIa, or I. And if IIb, whether it is **implantable**,
   and if implantable whether it is one of the listed exceptions (sutures, staples, dental
   fillings, dental braces, tooth crowns, screws, wedges, plates, wires, pins, clips,
   connectors). Those exceptions move down a tier.
2. **The certificate basis** — a notified-body certificate under 90/385/EEC or 93/42/EEC
   (paragraph 3a), or formerly self-certified under 93/42 with a DoC before 26 May 2021
   and now requiring a notified body (paragraph 3b). Different routes, different rules.
3. **Whether the 3c conditions were met** — in particular the QMS by 26 May 2024 and the
   application lodged by 26 May 2024, with the written agreement signed by 26 September
   2024.

If 3 is unknown, say the date **conditionally** and name what would remove it:

> On class alone that device runs to [date]. But the extension is conditional, not
> automatic — it applies only if all five conditions in 120(3c) were met, including a
> quality management system in place by 26 May 2024 and a formal application lodged with
> a notified body by the same date, with the written agreement signed by 26 September
> 2024. If any of those was missed, the extension was never available and the answer is
> different. Can you confirm?

---

## The dates

| Device | Deadline |
|---|---|
| Class III | **31 Dec 2027** |
| Class IIb implantable, except the listed items | **31 Dec 2027** |
| Those listed items (sutures, staples, dental fillings, braces, crowns, screws, wedges, plates, wires, pins, clips, connectors) | **31 Dec 2028** |
| Class IIb other | **31 Dec 2028** |
| Class IIa | **31 Dec 2028** |
| Class I sterile or measuring function | **31 Dec 2028** |
| Route 3b — formerly self-certified, DoC before 26 May 2021 | **31 Dec 2028** |

## 26 May 2024 changed job; it did not disappear

Both of these are wrong, and they fail in opposite directions:

- **"The deadline is 26 May 2024."** Superseded as a market deadline by 2023/607.
- **"It moved to 2027/2028, so 2024 no longer matters."** 26 May 2024 is now the date by
  which the QMS had to be in place and the notified-body application lodged — two of the
  conditions the later dates *depend on*. 26 September 2024 was the deadline for the
  signed written agreement.

State both halves. A manufacturer told only the good news will not check whether they
qualified.

## The extension is conditional

120(3c) is cumulative — all five conditions. Continued compliance with the old Directive,
**no significant changes in design and intended purpose**, no unacceptable risk, QMS by
26 May 2024, application by 26 May 2024 plus written agreement by 26 September 2024.

Note **3d**: during the transition, MDR's post-market surveillance, market surveillance,
vigilance and registration requirements apply **in place of** the old Directives'. A
legacy device is not living entirely under the old regime.

What counts as a "significant change" under 3c(b) is dealt with in MDCG guidance, which
this skill does not carry. If the question turns on that, say so and stop.

## Output

```markdown
## [device]

**Class:** [as stated, or NOT SUPPLIED]
**Route:** [120(3a) certificate | 120(3b) formerly self-certified | not established]
**Deadline:** [date] — conditional on 120(3c)

| Question | Answer | Basis |
|---|---|---|
| Which paragraph applies | | `[verified]` |
| Class-dependent date | | `[verified]` |
| 3c conditions met? | | |

**What would change this:** [the fact that moves the date or removes the extension]

## Limits
[the block below]
```

## Citation discipline

- **`[verified]`** — Article 120(3), (3a), (3b), (3c), (3d) as amended, in
  the "art120-amended.md" section below, from OJ L 80, 20.3.2023, retrieved 2026-09-10.
- **`[verify]`** — everything else: Article 120's other paragraphs, IVDR Article 110,
  MDCG guidance, Annex VII, Article 97, national practice.

Never state a notified body's position or how an authority would treat a borderline case.

## Limits

> This covers MDR Article 120(3) and (3a)–(3d) as amended by Regulation (EU) 2023/607,
> retrieved verbatim from the Official Journal on 2026-09-10. It does **not** cover
> Article 120's other paragraphs, **IVDR Article 110** (the parallel IVD transition, whose
> dates differ), MDCG guidance including on what counts as a significant change, Annex VII,
> or national practice. The transition is conditional and fact-specific; this is a
> first-pass aid, not legal or regulatory advice, and not a substitute for your notified
> body or a qualified regulatory professional.

---

# Reference texts

Verbatim statute text. Every finding must cite a provision that appears here.

## art120-amended.md

# MDR Article 120 — the legacy transition, as amended

**Source:** Publications Office, Official Journal L 80, 20.3.2023, p. 24 —
**Regulation (EU) 2023/607**, Article 1, amending Regulation (EU) 2017/745.
<http://publications.europa.eu/resource/oj/JOL_2023_080_R_0002.ENG>
**Retrieved:** 2026-09-10, verbatim from the English OJ text.

**Emphasis added.** Bold inside quoted passages is mine, to mark the operative words.
It is not in the source. Everything else in a quoted block is verbatim, and
`scripts/verify-sources.py` checks that character for character.

> **Read this before anything else.** Article 120 was substantially amended in March
> 2023. The original 2017 text set a single deadline of **26 May 2024** for placing
> legacy devices on the market. That date no longer does that job. Any answer citing
> 26 May 2024 as the market deadline is quoting superseded law — which is exactly what a
> model recalling the 2017 text will do.

---

## The amended text

> **‘3.** By way of derogation from Article 5 and provided the conditions set out in
> paragraph 3c of this Article are met, devices referred to in paragraphs 3a and 3b of
> this Article may be placed on the market or put into service until the dates set out in
> those paragraphs.
>
> **3a.** Devices which have a certificate that was issued in accordance with Directive
> 90/385/EEC or Directive 93/42/EEC and that is valid by virtue of paragraph 2 of this
> Article may be placed on the market or put into service until the following dates:
>
> (a) **31 December 2027**, for all **class III** devices, and for **class IIb
> implantable** devices except sutures, staples, dental fillings, dental braces, tooth
> crowns, screws, wedges, plates, wires, pins, clips and connectors;
>
> (b) **31 December 2028**, for **class IIb** devices other than those covered by point
> (a) of this paragraph, for **class IIa** devices, and for **class I** devices placed on
> the market in **sterile** condition or having a **measuring function**.
>
> **3b.** Devices for which the conformity assessment procedure pursuant to Directive
> 93/42/EEC did not require the involvement of a notified body, for which the declaration
> of conformity was drawn up **prior to 26 May 2021** and for which the conformity
> assessment procedure pursuant to this Regulation requires the involvement of a notified
> body, may be placed on the market or put into service until **31 December 2028**.
>
> **3c.** Devices referred to in paragraphs 3a and 3b of this Article may be placed on the
> market or put into service until the dates referred to in those paragraphs **only if
> the following conditions are met**:
>
> (a) those devices continue to comply with Directive 90/385/EEC or Directive 93/42/EEC,
> as applicable;
>
> (b) there are **no significant changes in the design and intended purpose**;
>
> (c) the devices do not present an unacceptable risk to the health or safety of patients,
> users or other persons, or to other aspects of the protection of public health;
>
> (d) **no later than 26 May 2024**, the manufacturer has put in place a **quality
> management system** in accordance with Article 10(9);
>
> (e) **no later than 26 May 2024**, the manufacturer or the authorised representative has
> lodged a **formal application** with a notified body in accordance with Section 4.3,
> first subparagraph, of Annex VII [...] and, **no later than 26 September 2024**, the
> notified body and the manufacturer have **signed a written agreement** in accordance
> with Section 4.3, second subparagraph, of Annex VII.
>
> **3d.** By way of derogation from paragraph 3 of this Article, the requirements of this
> Regulation relating to **post-market surveillance, market surveillance, vigilance,
> registration of economic operators and of devices** shall apply to devices referred to
> in paragraphs 3a and 3b of this Article in place of the corresponding requirements in
> Directives 90/385/EEC and 93/42/EEC.

---

## The dates, as a table

| Device | Deadline |
|---|---|
| Class III | **31 Dec 2027** |
| Class IIb **implantable**, except the listed items | **31 Dec 2027** |
| The listed exceptions — sutures, staples, dental fillings, dental braces, tooth crowns, screws, wedges, plates, wires, pins, clips, connectors | **31 Dec 2028** |
| Class IIb, other | **31 Dec 2028** |
| Class IIa | **31 Dec 2028** |
| Class I sterile, or with a measuring function | **31 Dec 2028** |
| Formerly self-certified under 93/42, DoC before 26 May 2021, now needs a notified body (3b) | **31 Dec 2028** |

The exception list in 3a(a) moves those items **down** a tier: a class IIb implantable
suture gets 2028, not 2027.

## 26 May 2024 has not disappeared — it changed job

It is no longer the date by which a legacy device must leave the market. It is now the
date by which two of the 3c conditions had to be met: the QMS in place (3c(d)) and the
formal application lodged with a notified body (3c(e)). A further date, **26 September
2024**, was the deadline for the signed written agreement.

So both of these are wrong:

- "The deadline was 26 May 2024" — superseded as a market deadline.
- "The deadline moved to 2027/2028, so 2024 no longer matters" — 2024 and September 2024
  are the conditions on which 2027/2028 depend. Miss them and the extension was never
  available.

## The extension is conditional, not automatic

3c is cumulative: **all five** conditions. A device that met the dates but had no QMS in
place by 26 May 2024, or whose design changed significantly, never qualified.

3d is easy to miss: even during the transition, MDR's post-market surveillance,
vigilance, market surveillance and registration requirements apply **instead of** the old
Directives'.

## What this file does not carry

Article 120's other paragraphs — (1), (2), (4) onward — including the rules on validity of
old certificates and on devices already placed on the market. It does not carry
**IVDR Article 110**, the parallel IVD transition, whose dates differ. It does not carry
MDCG guidance on Article 120, notably on what counts as a "significant change" under
3c(b), which is guidance and unverified here. And it does not carry Article 97, referenced
in the amendment.

Where a question turns on any of those, say so and stop.

---
