# software-classification — single-file bundle

Plugin `mdr-classification`. Everything needed to run this skill in a tool that cannot
read the repo: paste or upload this whole file, then give it your input.

GENERATED FILE — do not edit. Source:
mdr-classification/skills/software-classification/. Rebuild with `python3 scripts/build-portable.py`.

---

# MDR Software Classification (Annex VIII)

Determine the class of software under **MDR Annex VIII**, using the verbatim text in
the "annex-viii-software.md" section below. Read that file before answering.

This covers **software only**, and only the rules that bear on software: implementing
rules 3.1–3.7 and Rule 11. It does not carry Rules 1–10 or 12–22.

---

## Step 0 — Two prior questions, settled before any rule is applied

### Is the product a medical device at all?

Classification presumes qualification. If it is not established that the software meets
the Art. 2(1) device definition, that is the prior question and this skill does not
answer it. Say so:

> Before class, the product has to be a medical device under Art. 2(1). Nothing I have
> settles that, and it is a separate analysis. If qualification is already established,
> tell me and I will classify. If not, that comes first.

Do not classify a wellness app, a hospital administration tool, or a general-purpose
analytics product just because the question was asked in those terms.

### What is the intended purpose, as stated?

Implementing rule **3.1** anchors classification to the **intended purpose**, not to what
the software can technically do. Ask for it if it is not supplied:

> Classification runs on the intended purpose as you state it, not on capability. Can
> you give me the intended purpose as written in your technical documentation?

A capability outside the intended purpose does not raise the class. It raises a
different question — whether the intended purpose is stated correctly — and that is
worth flagging when you see it, as a note rather than a classification finding.

---

## Gate 1 — Does it drive or influence another device? (3.3)

**Run this before Rule 11. Every time.** It is the step most often skipped, and skipping
it produces a confident wrong answer.

> **3.3.** Software, which drives a device or influences the use of a device, shall fall
> within the same class as the device. If the software is independent of any other
> device, it shall be classified in its own right.

- **Drives or influences another device** → it takes **that device's class**. Rule 11 is
  not reached. Say which device, and that its class governs. If the driven device's class
  is unknown, the answer is "same class as X, which I need from you", not a Rule 11 class.
- **Independent** → continue to Gate 2.

Beware the middle case. Software that merely *displays* output from a device, without
driving it or influencing its use, is usually independent. Software that sets a
parameter, gates an alarm, or changes how the device is operated is not. Where it is
genuinely unclear, say which way it turns and what fact would settle it.

---

## Gate 2 — Rule 11, in order

Apply the limbs in this order. Stop at the first that matches.

### Limb 1 — information used to take diagnostic or therapeutic decisions → IIa, escalating

Base class **IIa**. Then test the **impact of the decision**, not the severity of the
disease:

- may cause **death or an irreversible deterioration** of health → **III**
- may cause **serious deterioration** of health, or **a surgical intervention** → **IIb**
- otherwise → **IIa**

The escalation asks what a wrong decision may cause. Software informing decisions in a
serious condition is not automatically III. Software whose output routinely triggers
surgery is IIb even if the condition is not itself life-threatening.

### Limb 2 — monitoring physiological processes → IIa, escalating

Base class **IIa**. Escalation to **IIb** requires **both**:

1. the parameters monitored are **vital** physiological parameters, **and**
2. the nature of their variation is such that it **could result in immediate danger**

Both. Monitoring a vital parameter that varies slowly and without urgency does not reach
IIb on this limb. Do not collapse "physiological process" into "vital parameter".

### Limb 3 — all other software → I

If neither limb 1 nor limb 2 is engaged on the stated intended purpose, the class is
**I**. Say so plainly. A class I answer is a real answer, not a failure to find something.

---

## Gate 3 — Could another rule reach it? (3.5)

> **3.5.** If several rules [...] apply to the same device [...] the strictest rule and
> sub-rule resulting in the higher classification shall apply.

Rule 11 sets a **floor, not a ceiling**. Before concluding, ask whether the intended
purpose also engages a rule this skill does not carry — for example software that is
itself an active therapeutic function, or that controls administration of a substance.

If it might, **do not conclude**. Say:

> Rule 11 gives class [X]. But 3.5 means the strictest applicable rule wins, and the
> intended purpose here may also engage [rule / concept], which I do not carry. That
> could raise the class. Worth checking Rules [n] before treating [X] as settled.

Better an incomplete answer than a confident floor presented as the class.

---

## Output

```markdown
# MDR Software Classification: [name]

**Intended purpose (as stated):** [quoted, or NOT SUPPLIED]
**Qualified as a device:** [established | not established — see note]

## Class: [I | IIa | IIb | III | cannot conclude]

**Route:** [3.3 → same class as driven device] or [3.3 independent → Rule 11 limb N]

## Reasoning
| Step | Question | Answer | Basis |
|---|---|---|---|
| 3.1 | Intended purpose | [quoted] | `[verified]` |
| 3.3 | Drives or influences another device? | [yes/no] | `[verified]` |
| Rule 11 | Which limb | [1/2/3] | `[verified]` |
| Rule 11 | Escalation | [none / IIb / III] and why | `[verified]` |
| 3.5 | Could a stricter rule apply? | [no / possibly — which] | `[verified]` |

## What would change this
[the specific facts that would move the class, named]

## Limits
[the block below, verbatim]
```

---

## Citation discipline

- **`[verified]`** — the provision is in the "annex-viii-software.md" section below: Rule 11,
  implementing rules 3.1–3.7, and the Chapter I definitions carried there. Retrieved
  from EUR-Lex 2026-09-09 and re-checkable there.
- **`[verify]`** — anything else. Rules 1–10 and 12–22, Art. 2(1) qualification,
  Annex XVI, national practice.

**MDCG 2019-11 is guidance, not the rule.** It is not verified here and must never be
stated as binding. If an answer turns on it:

> This turns on MDCG 2019-11, which is Commission guidance rather than the regulation,
> and which I do not verify. The Annex VIII text takes me to [X]. I can flag the
> guidance question, or you can point me at the passage.

Never state how a notified body would decide. Never invent a rule number.

## Limits

> This classifies software under MDR Annex VIII implementing rules 3.1–3.7 and Rule 11,
> retrieved verbatim from EUR-Lex on 2026-09-09. It does **not** cover Art. 2(1)
> qualification, Rules 1–10 or 12–22, Annex XVI, IVDR, MDCG guidance, notified-body
> practice, or national interpretation. Rule 11 is a floor: under 3.5 a stricter rule
> this skill does not carry may raise the class. A structured first pass and an audit
> aid, not legal or regulatory advice, and not a substitute for your notified body or a
> qualified regulatory professional.

## Before stating a class as settled

If the user is not a qualified regulatory professional, do not present the class as
final. Give the class, the route, and then:

> This is the Annex VIII text applied to the intended purpose as you stated it. The class
> drives your conformity route, whether you need a notified body, and the depth of your
> technical documentation, so it should be confirmed by your regulatory lead or notified
> body before you build on it. The three things to put in front of them: [the 3.3 call,
> the limb and escalation, and any 3.5 rule that might reach higher].

---

# Reference texts

Verbatim statute text. Every finding must cite a provision that appears here.

## annex-viii-software.md

# MDR Annex VIII — the parts that decide a software device's class

**Source:** EUR-Lex, Regulation (EU) 2017/745, CELEX 32017R0745, Annex VIII
<https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32017R0745>
**Retrieved:** 2026-09-09, verbatim from the consolidated EN text.

This file carries **Rule 11**, the **implementing rules** that govern how any rule is
applied, and the **definitions** those rules depend on. It does not carry Rules 1–10
or 12–22; where one of those may apply, say so and stop rather than guess.

---

## Rule 11 — software

> **Rule 11**
>
> Software intended to provide information which is used to take decisions with
> diagnosis or therapeutic purposes is classified as class IIa, except if such
> decisions have an impact that may cause:
>
> — death or an irreversible deterioration of a person's state of health, in which
> case it is in class III; or
>
> — a serious deterioration of a person's state of health or a surgical intervention,
> in which case it is classified as class IIb.
>
> Software intended to monitor physiological processes is classified as class IIa,
> except if it is intended for monitoring of vital physiological parameters, where the
> nature of variations of those parameters is such that it could result in immediate
> danger to the patient, in which case it is classified as class IIb.
>
> All other software is classified as class I.

### The three limbs, as a structure

| Limb | Trigger | Base class | Escalation |
|---|---|---|---|
| 1 | Provides information **used to take decisions with diagnosis or therapeutic purposes** | **IIa** | **III** if such decisions may cause death or irreversible deterioration; **IIb** if serious deterioration or a surgical intervention |
| 2 | Intended to **monitor physiological processes** | **IIa** | **IIb** if monitoring **vital** physiological parameters whose variation could cause **immediate danger** |
| 3 | Everything else | **I** | — |

Read the escalation in limb 1 against the **impact of the decision**, not the severity
of the disease. Software informing a decision in a serious condition is not
automatically class III; the question is what the decision, if wrong, may cause.

Limb 2's escalation has two cumulative conditions: the parameters must be **vital**,
**and** the nature of their variation must be such that it could cause **immediate**
danger. Monitoring a vital parameter slowly and non-urgently does not reach IIb on
this limb alone.

---

## Implementing rules (Chapter II) — these govern before Rule 11 does

> **3.1.** Application of the classification rules shall be governed by the intended
> purpose of the devices.
>
> **3.2.** If the device in question is intended to be used in combination with another
> device, the classification rules shall apply separately to each of the devices.
> Accessories for a medical device and for a product listed in Annex XVI shall be
> classified in their own right separately from the device with which they are used.
>
> **3.3.** Software, which drives a device or influences the use of a device, shall fall
> within the same class as the device.
>
> If the software is independent of any other device, it shall be classified in its own
> right.
>
> **3.4.** If the device is not intended to be used solely or principally in a specific
> part of the body, it shall be considered and classified on the basis of the most
> critical specified use.
>
> **3.5.** If several rules, or if, within the same rule, several sub-rules, apply to the
> same device based on the device's intended purpose, the strictest rule and sub-rule
> resulting in the higher classification shall apply.
>
> **3.6.** In calculating the duration referred to in Section 1, continuous use shall
> mean:
>
> (a) the entire duration of use of the same device without regard to temporary
> interruption of use during a procedure or temporary removal for purposes such as
> cleaning or disinfection of the device. Whether the interruption of use or the removal
> is temporary shall be established in relation to the duration of the use prior to and
> after the period when the use is interrupted or the device removed; and
>
> (b) the accumulated use of a device that is intended by the manufacturer to be
> replaced immediately with another of the same type.
>
> **3.7.** A device is considered to allow direct diagnosis when it provides the
> diagnosis of the disease or condition in question by itself or when it provides
> decisive information for the diagnosis.

### 3.3 is the one most often skipped

**3.3 runs before Rule 11.** Software that drives a device or influences its use takes
**that device's class**, whatever Rule 11 would have said on its own. Only *independent*
software is classified in its own right, and only then does Rule 11 apply.

So the first question is never "which Rule 11 limb". It is: **does this software drive
or influence another device?**

### 3.5 means Rule 11 is a floor, not a ceiling

If another rule also applies on the intended purpose, the **higher** class wins. Rule 11
producing class I does not settle the matter if, say, a rule on active therapeutic
devices also reaches the same software. This file does not carry those rules, so where
another rule may apply, say so rather than concluding.

### 3.1 anchors everything to intended purpose

Not to what the software can technically do. A capability outside the intended purpose
does not raise the class; it raises a different question, about whether the intended
purpose is stated correctly.

---

## Definitions the rules depend on (Chapter I)

> **1.1.** 'Transient' means normally intended for continuous use for less than 60 minutes.
>
> **1.2.** 'Short term' means normally intended for continuous use for between 60 minutes and 30 days.
>
> **1.3.** 'Long term' means normally intended for continuous use for more than 30 days.
>
> **2.4.** 'Active therapeutic device' means any active device used, whether alone or in
> combination with other devices, to support, modify, replace or restore biological
> functions or structures with a view to treatment or alleviation of an illness, injury
> or disability.
>
> **2.5.** 'Active device intended for diagnosis and monitoring' means any active device
> used, whether alone or in combination with other devices, to supply information for
> detecting, diagnosing, monitoring or treating physiological conditions, states of
> health, illnesses or congenital deformities.
>
> **2.7.** 'Central nervous system' means the brain, meninges and spinal cord.

---

## What this file does not cover

**MDCG 2019-11** is the Commission guidance on qualification and classification of
software. It is guidance, not the rule, it is not verified here, and it must not be
stated as binding. Where an answer turns on it, say so and stop.

Rules 1–10 and 12–22 are not carried here. Neither is Art. 2(1) qualification — whether
the product is a medical device at all — nor Annex XVI. A classification answer assumes
the product has already been qualified as a device; if that is unsettled, it is the
prior question.

---
