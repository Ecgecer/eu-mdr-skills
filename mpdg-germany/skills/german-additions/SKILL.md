---
name: german-additions
description: >
  Answer what Germany requires ON TOP OF MDR/IVDR for a device placed on the German
  market — language rules for the Declaration of Conformity and product information
  (MPDG § 8), supplementary DMIDS notifications (§ 4), and supplementary vigilance
  duties including German-language FSNs (§ 73). Use when the user asks "do we need
  German labelling", "what does Germany require", "MPDG", "is English enough",
  "Sprachenregelung", "DMIDS", or asks about German-market obligations that MDR alone
  does not answer.
argument-hint: "[the German-market question]"
---

# MPDG — the German delta

MDR is not the whole obligation for the German market. MPDG, Germany's implementation
act, **adds** duties that MDR never mentions, and those additions are where a
manufacturer relying on MDR alone gets caught.

This skill answers one question: **does Germany require something here that MDR does
not, and if so what.** Verbatim text is in `references/mpdg.md`. Read it before
answering.

It carries **three sections only** — § 8 (language), § 4 (supplementary notifications),
§ 73 (supplementary vigilance). Everything else in MPDG is out of scope and must be
said so rather than guessed.

---

## Step 0 — Establish two things

**Is the German market actually in play?** MPDG applies *im Geltungsbereich dieses
Gesetzes*. If the product is not made available in Germany, none of this applies, and
saying so is the answer. Do not apply German rules to an EU-wide or other-member-state
question:

> MPDG is German national law. If you are asking about the EU generally, or another
> member state, this does not apply — each member state has its own implementing act,
> and I do not carry them.

**Who is asking, and in what role?** Several duties turn on it. § 73(2) separates
manufacturers established in Germany from authorised representatives and importers, and
the importer's notification duty applies only where the authorised representative sits
outside Germany.

---

## The three areas

### § 8 — Language

**Do not answer "everything must be in German".** That is wrong, and it is the more
common error of the two. The rule is asymmetric:

- **EU Declaration of Conformity** — German **or English**. § 8(1). English alone is
  compliant. Telling a manufacturer to translate the DoC is over-application.
- **Information for users and patients** — **German**. § 8(2) sentence 1, and it is a
  condition of supply: products may only be handed over if it is met.
- **The professional-user exception** — § 8(2) sentence 2 permits English or another
  easily understood language, but only where **all three** hold: it is a justified case
  (*begründeter Fall*), the information is **exclusively** for professional users, and
  **safety-related information is still provided in German** or the user's language.
  Missing any one, sentence 1 applies.
- **Implant information** under MDR Art. 18(1) — **German**, § 8(3). No professional-user
  exception reaches it.

When someone asks "is English enough?", the answer depends entirely on which of those
they mean. Ask if it is not clear.

### § 4 — Supplementary notifications

Notifications to the German competent authority through **DMIDS** (§ 86), which is
separate from EUDAMED registration. Two triggers:

- Reprocessing sterile or low-germ devices exclusively for others, or a health
  institution reprocessing single-use devices under MDR Art. 17(3) — **unless** already
  obliged to register under MDR Art. 31.
- Manufacturing **class III custom-made implantable** devices.

Both bite **before the activity begins**, not at first placing on the market. Changes
must be notified **unverzüglich**.

The Art. 31 carve-out in § 4(1) is the point: this catches parties MDR's own
registration does not.

### § 73 — Supplementary vigilance

Three things MDR Art. 89 does not say:

1. The **Field Safety Notice must be in German** — § 73(1), attaching to FSCAs taken in
   Germany.
2. Manufacturers established in Germany must **document the FSCA and periodically review
   its effectiveness** — § 73(2) sentence 1.
3. **Completion** of an FSCA must be notified to both the competent authority and the
   federal higher authority — § 73(2) sentence 2. For importers this applies only where
   the authorised representative is outside Germany.

---

## When the question is outside these three

Say so plainly and stop. MPDG has around 100 sections; this carries three.

> That falls under MPDG but outside the sections I carry — I have § 8 (language), § 4
> (supplementary notifications) and § 73 (supplementary vigilance). [Topic] is dealt
> with in [area], which I cannot quote, so I would be guessing. Worth checking the Act
> directly or asking someone who works with it.

Common questions that are **outside** scope: clinical investigations, operation and use
of devices, special authorisation, classification determinations by the authority,
free-sale certificates, penalties and fines.

## Output

```markdown
## [the question]

**German market:** [confirmed | not established — see note]
**Answer:** [the obligation, in one line]

| Item | MDR requires | Germany adds | Basis |
|---|---|---|---|
| ... | ... | ... | MPDG § X `[verified]` |

**What would change this:** [the fact that flips it]

## Limits
[the block below]
```

Where MDR's own requirement is not something this skill carries, say "not carried here"
in that column rather than stating it from memory.

## Citation discipline

- **`[verified]`** — MPDG §§ 4, 8, 73, in `references/mpdg.md`, retrieved from
  gesetze-im-internet 2026-09-10 and re-checkable there.
- **`[verify]`** — anything else, including MDR and IVDR articles themselves, other MPDG
  sections, MDCG guidance, and BfArM practice.

Never state a BfArM position, a notified-body view, or how a German court would rule.

## Limits

> This covers MPDG §§ 4, 8 and 73 only, retrieved verbatim from gesetze-im-internet on
> 2026-09-10. It does **not** cover the rest of MPDG, MDR or IVDR themselves, MDCG
> guidance, BfArM practice, or any other member state's implementing law — an obligation
> here is German and says nothing about France, Italy or elsewhere. A first-pass aid for
> spotting German-specific duties, not legal advice, and not a substitute for a
> regulatory professional or a Fachanwalt für Medizinrecht.
