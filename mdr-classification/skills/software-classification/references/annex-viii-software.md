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
