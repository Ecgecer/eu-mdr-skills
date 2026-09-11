# MPDG: what Germany requires on top of MDR

**Source:** gesetze-im-internet.de, Medizinprodukterecht-Durchführungsgesetz (MPDG)
<https://www.gesetze-im-internet.de/mpdg/>
**Retrieved:** 2026-09-10, verbatim German text.

**Emphasis added.** Bold inside quoted passages is mine, to mark the operative
words. It is not in the source. Everything else in a quoted block is verbatim, and
`scripts/verify-sources.py` checks that character for character.

MPDG is Germany's implementation act for MDR and IVDR. It does not restate the
Regulations. It **adds** to them, and the additions are where manufacturers selling
into Germany get caught, because MDR alone does not mention them.

This file carries three sections. It does not carry the rest of the Act.

---

## § 8: Language (Sprachenregelung)

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
| **Information for users and patients** | **German** | § 8(2) sentence 1. The default, and it is a condition of supply n/a products may only be handed over if it is met. |
| Same, professional users only | English or another easily understood language | § 8(2) sentence 2, and only **in begründeten Fällen**. Three conditions, all required. |
| **Safety-related** information, even then | **German** or the user's language | § 8(2) sentence 2, final clause. The exception does not reach safety information. |
| **Implant card / implant information**, Art. 18(1) MDR | **German** | § 8(3). No professional-user exception. |

The § 8(2) sentence 2 exception is cumulative: justified case **and** exclusively
professional users **and** safety information still in German. Missing any one, the
default in sentence 1 applies.

---

## § 4: Supplementary notification duties (Ergänzende Anzeigepflichten)

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
registration. § 4(1) carves out anyone already obliged to register under MDR Art. 31
so this catches parties MDR's own registration does not.

Both duties bite **before the activity starts**, not at first placing on the market.

---

## § 73: Supplementary vigilance duties (Ergänzende Herstellerpflichten)

> **§ 73 Ergänzende Herstellerpflichten im Rahmen der Vigilanz; Sprachenregelung**
>
> (1) Ergreifen Hersteller im Geltungsbereich dieses Gesetzes Sicherheitskorrekturmaßnahmen, sind die Sicherheitsanweisungen im Feld nach Artikel 89 Absatz 8 der Verordnung (EU) 2017/745 oder Artikel 84 Absatz 8 der Verordnung (EU) 2017/746 in deutscher Sprache abzufassen.
>
> (2) Hersteller mit Sitz im Geltungsbereich dieses Gesetzes haben die Durchführung von Sicherheitskorrekturmaßnahmen im Feld zu dokumentieren und regelmäßig auf ihre Wirksamkeit zu überprüfen. Hersteller, Bevollmächtigte und Importeure mit Sitz im Geltungsbereich dieses Gesetzes haben der zuständigen Behörde und der zuständigen Bundesoberbehörde den Abschluss einer Sicherheitskorrekturmaßnahme im Feld mitzuteilen. Importeure mit Sitz im Geltungsbereich dieses Gesetzes haben der zuständigen Behörde und der zuständigen Bundesoberbehörde den Abschluss einer Sicherheitskorrekturmaßnahme im Feld nur dann mitzuteilen, wenn der Bevollmächtigte seinen Sitz außerhalb des Geltungsbereichs dieses Gesetzes hat.

Three additions MDR Art. 89 does not contain:

1. The **FSN must be written in German**, § 73(1). This attaches to the action, not to
   where the manufacturer sits: it applies to manufacturers taking an FSCA *im
   Geltungsbereich dieses Gesetzes*.
2. **Documenting the FSCA and periodically reviewing its effectiveness**, § 73(2)
   sentence 1, for manufacturers established in Germany.
3. **Notifying completion** of an FSCA to both the competent authority and the federal
   higher authority, § 73(2) sentence 2. The importer's duty in sentence 3 is
   conditional: only where the authorised representative sits outside Germany.

---

## What this file does not carry

The rest of MPDG, clinical investigations (§§ 24 ff.), operation and use of devices
(§ 11), special authorisation (§ 7), classification and legal-status determination by
the authority (§ 6), free-sale certificates (§ 10), penalties and fines (§§ 92–94), and
everything else. Where a question touches those, say so and stop.

Nor does it carry MDR or IVDR themselves. This file is only the German delta.

Nor any other member state. An obligation here is German; it says nothing about France,
Italy or anywhere else, each of which has its own implementing act.
