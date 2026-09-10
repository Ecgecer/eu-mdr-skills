---
name: legacy-transition
description: >
  Answer whether a legacy medical device can still be placed on the EU market under
  MDR Article 120 as amended by Regulation (EU) 2023/607, and by when. Use when the
  user asks "how long can we keep selling", "MDR transition deadline", "Article 120",
  "legacy device", "our MDD certificate", "do we still have until 2024", "extension",
  or describes a device certified under 90/385/EEC or 93/42/EEC.
argument-hint: "[device class, certificate basis, and what you need to know]"
---

# MDR Article 120 — the legacy transition

Answer from the **amended** text in `references/art120-amended.md`. Read it before
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
  `references/art120-amended.md`, from OJ L 80, 20.3.2023, retrieved 2026-09-10.
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
