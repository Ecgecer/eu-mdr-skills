# german-additions — single-file bundle

Plugin `mpdg-germany`. Everything needed to run this skill in a tool that cannot
read the repo: paste or upload this whole file, then give it your input.

GENERATED FILE — do not edit. Source:
mpdg-germany/skills/german-additions/. Rebuild with `python3 scripts/build-portable.py`.

---

# MPDG — the German delta

MDR is not the whole obligation for the German market. MPDG, Germany's implementation
act, **adds** duties that MDR never mentions, and those additions are where a
manufacturer relying on MDR alone gets caught.

This skill answers one question: **does Germany require something here that MDR does
not, and if so what.** Verbatim text is in the "mpdg.md" section below. Read it before
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

- **`[verified]`** — MPDG §§ 4, 8, 73, in the "mpdg.md" section below, retrieved from
  gesetze-im-internet 2026-09-10 and re-checkable there.
- **`[verify]`** — anything else, including MDR and IVDR articles themselves, other MPDG
  sections, MDCG guidance, and BfArM practice.

**No silent supplement.** A `[verify]` tag is not permission to answer from memory. If
the question turns on an MPDG section this skill does not carry, or on MDR/IVDR itself,
**stop and say so**:

> That falls outside the sections I carry. I can flag it as an open question, or you can
> paste the provision and I will work from it. I will not state a requirement I cannot
> cite from the reference file.

Never state a BfArM position, a notified-body view, or how a German court would rule.

## Limits

> This covers MPDG §§ 4, 8 and 73 only, retrieved verbatim from gesetze-im-internet on
> 2026-09-10. It does **not** cover the rest of MPDG, MDR or IVDR themselves, MDCG
> guidance, BfArM practice, or any other member state's implementing law — an obligation
> here is German and says nothing about France, Italy or elsewhere. A first-pass aid for
> spotting German-specific duties, not legal advice, and not a substitute for a
> regulatory professional or a Fachanwalt für Medizinrecht.

---

# Reference texts

Verbatim statute text. Every finding must cite a provision that appears here.

## mpdg.md

# MPDG — what Germany requires on top of MDR

**Source:** gesetze-im-internet.de, Medizinprodukterecht-Durchführungsgesetz (MPDG)
<https://www.gesetze-im-internet.de/mpdg/>
**Retrieved:** 2026-09-10, verbatim German text.

**Emphasis added.** Bold inside quoted passages is mine, to mark the operative
words. It is not in the source. Everything else in a quoted block is verbatim, and
`scripts/verify-sources.py` checks that character for character.

MPDG is Germany's implementation act for MDR and IVDR. It does not restate the
Regulations — it **adds** to them, and the additions are where manufacturers selling
into Germany get caught, because MDR alone does not mention them.

This file carries three sections. It does not carry the rest of the Act.

---

## § 8 — Language (Sprachenregelung)

> **§ 8 Sprachenregelung für die EU-Konformitätserklärung und für Produktinformationen**
>
> (1) Der Hersteller hat für Produkte, die im Geltungsbereich dieses Gesetzes auf dem
> Markt bereitgestellt werden, die EU-Konformitätserklärung nach Artikel 19 Absatz 1 der
> Verordnung (EU) 2017/745 und Artikel 17 Absatz 1 der Verordnung (EU) 2017/746 **in
> deutscher oder in englischer Sprache** zur Verfügung zu stellen.
>
> (2) Produkte dürfen im Geltungsbereich dieses Gesetzes nur dann an Anwender und
> Patienten abgegeben werden, wenn die für Anwender und Patienten bestimmten
> Informationen **in deutscher Sprache** zur Verfügung gestellt werden. In begründeten
> Fällen dürfen die Informationen auch in englischer Sprache oder einer anderen für den
> Anwender des Medizinproduktes leicht verständlichen Sprache zur Verfügung gestellt
> werden, wenn diese Informationen **ausschließlich für professionelle Anwender**
> bestimmt sind und die **sicherheitsbezogenen Informationen auch in deutscher Sprache**
> oder in der Sprache des Anwenders zur Verfügung gestellt werden.
>
> (3) Der Hersteller eines **implantierbaren** Produktes hat die Informationen nach
> Artikel 18 Absatz 1 Unterabsatz 1 der Verordnung (EU) 2017/745 **in deutscher Sprache**
> zur Verfügung zu stellen.

### Read the asymmetry

The rule is not "everything must be German". Getting this wrong in either direction is
a real error:

| Item | Language | Note |
|---|---|---|
| **EU Declaration of Conformity** | German **or English** | § 8(1). English alone is sufficient. Requiring German here is over-application. |
| **Information for users and patients** | **German** | § 8(2) sentence 1. The default, and it is a condition of supply — products may only be handed over if it is met. |
| Same, professional users only | English or another easily understood language | § 8(2) sentence 2, and only **in begründeten Fällen**. Three conditions, all required. |
| **Safety-related** information, even then | **German** or the user's language | § 8(2) sentence 2, final clause. The exception does not reach safety information. |
| **Implant card / implant information**, Art. 18(1) MDR | **German** | § 8(3). No professional-user exception. |

The § 8(2) sentence 2 exception is cumulative: justified case **and** exclusively
professional users **and** safety information still in German. Missing any one, the
default in sentence 1 applies.

---

## § 4 — Supplementary notification duties (Ergänzende Anzeigepflichten)

> **§ 4 Ergänzende Anzeigepflichten**
>
> (1) Betriebe und Einrichtungen, die Produkte, die bestimmungsgemäß keimarm oder steril
> zur Anwendung kommen, ausschließlich für andere aufbereiten, oder
> Gesundheitseinrichtungen, die Einmalprodukte nach Artikel 17 Absatz 3 der Verordnung
> (EU) 2017/745 aufbereiten oder aufbereiten lassen, haben dies **vor Aufnahme der
> Tätigkeit** unter Angabe ihrer Anschrift der zuständigen Behörde über das Deutsche
> Medizinprodukteinformations- und Datenbanksystem nach § 86 anzuzeigen, sofern sie nicht
> nach Artikel 31 der Verordnung (EU) 2017/745 zur Registrierung verpflichtet sind.
>
> (2) Betriebe und Einrichtungen, die **implantierbare Sonderanfertigungen der Klasse
> III** herstellen, haben dies **vor Aufnahme der Tätigkeit** unter Angabe ihrer Anschrift
> der zuständigen Behörde über das Deutsche Medizinprodukteinformations- und
> Datenbanksystem nach § 86 anzuzeigen.
>
> (3) Jede Änderung der Angaben, die nach den Absätzen 1 und 2 anzeigepflichtig sind, ist
> der zuständigen Behörde **unverzüglich** über das Deutsche Medizinprodukteinformations-
> und Datenbanksystem nach § 86 anzuzeigen.

These are notifications to the German competent authority through **DMIDS** (Deutsches
Medizinprodukteinformations- und Datenbanksystem, § 86), separate from EUDAMED
registration. § 4(1) carves out anyone already obliged to register under MDR Art. 31 —
so this catches parties MDR's own registration does not.

Both duties bite **before the activity starts**, not at first placing on the market.

---

## § 73 — Supplementary vigilance duties (Ergänzende Herstellerpflichten)

> **§ 73 Ergänzende Herstellerpflichten im Rahmen der Vigilanz; Sprachenregelung**
>
> (1) Ergreifen Hersteller im Geltungsbereich dieses Gesetzes Sicherheitskorrekturmaßnahmen, sind die Sicherheitsanweisungen im Feld nach Artikel 89 Absatz 8 der Verordnung (EU) 2017/745 oder Artikel 84 Absatz 8 der Verordnung (EU) 2017/746 in deutscher Sprache abzufassen.
>
> (2) Hersteller mit Sitz im Geltungsbereich dieses Gesetzes haben die Durchführung von Sicherheitskorrekturmaßnahmen im Feld zu dokumentieren und regelmäßig auf ihre Wirksamkeit zu überprüfen. Hersteller, Bevollmächtigte und Importeure mit Sitz im Geltungsbereich dieses Gesetzes haben der zuständigen Behörde und der zuständigen Bundesoberbehörde den Abschluss einer Sicherheitskorrekturmaßnahme im Feld mitzuteilen. Importeure mit Sitz im Geltungsbereich dieses Gesetzes haben der zuständigen Behörde und der zuständigen Bundesoberbehörde den Abschluss einer Sicherheitskorrekturmaßnahme im Feld nur dann mitzuteilen, wenn der Bevollmächtigte seinen Sitz außerhalb des Geltungsbereichs dieses Gesetzes hat.

Three additions MDR Art. 89 does not contain:

1. The **FSN must be written in German** — § 73(1). This attaches to the action, not to
   where the manufacturer sits: it applies to manufacturers taking an FSCA *im
   Geltungsbereich dieses Gesetzes*.
2. **Documenting the FSCA and periodically reviewing its effectiveness** — § 73(2)
   sentence 1, for manufacturers established in Germany.
3. **Notifying completion** of an FSCA to both the competent authority and the federal
   higher authority — § 73(2) sentence 2. The importer's duty in sentence 3 is
   conditional: only where the authorised representative sits outside Germany.

---

## What this file does not carry

The rest of MPDG — clinical investigations (§§ 24 ff.), operation and use of devices
(§ 11), special authorisation (§ 7), classification and legal-status determination by
the authority (§ 6), free-sale certificates (§ 10), penalties and fines (§§ 92–94), and
everything else. Where a question touches those, say so and stop.

Nor does it carry MDR or IVDR themselves. This file is only the German delta.

Nor any other member state. An obligation here is German; it says nothing about France,
Italy or anywhere else, each of which has its own implementing act.

---
