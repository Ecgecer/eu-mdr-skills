# UWG: Gesetz gegen den unlauteren Wettbewerb

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

## § 5: misleading commercial practices

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

- **no. 1 "Zwecktauglichkeit / Verwendungsmöglichkeit"**: fitness for purpose and
  possible use. This is the UWG mirror of MDR Art. 7(d) intended-purpose drift.
- **no. 1 "von der Verwendung zu erwartende Ergebnisse"**: expected results.
  Outcome claims land here.
- **no. 1 "Tests"**: claims about test results and their essential components.
  Cherry-picked clinical or bench data lands here.
- **no. 3, the trader.** "die **Person, Eigenschaften oder Rechte des Unternehmers**
  wie [...] **Status, Zulassung**". This reaches claims about the *company*: its
  qualifications, memberships, authorisations.
- **no. 4, the goods.** "Aussagen oder Symbole, die [...] sich auf eine **Zulassung des
  Unternehmers oder der Waren oder Dienstleistungen** beziehen". This is the CE-marking
  hook: copy implying a class, notified-body involvement, or a certification **the device
  does not hold**.

  The distinction matters when routing a finding. "We are an ISO 13485 certified
  manufacturer" is a claim about the trader (no. 3). "CE marked to Class IIb" is a claim
  about the goods (no. 4). Both are § 5 findings independent of whether the performance
  claims are true.

The § 5(1) materiality filter matters: the statement must be **geeignet**, capable
of causing a commercial decision the reader would not otherwise have made. A
trivially wrong detail nobody buys on is not automatically a § 5 breach.

---

## § 6: comparative advertising

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
banned. The test is cumulative. A comparison must clear every limb.

The two that fail most often on a SaaS/device comparison page:

- **§ 6(2) no. 1, same need or same purpose.** Comparing products with different
  intended purposes fails here before you reach accuracy. Two devices in different
  MDR classes or with different intended purposes are often not comparable at all.
- **§ 6(2) no. 2, objective, essential, relevant, verifiable, typical.**
  "Verifiable" (*nachprüfbar*) is the sharp edge: the reader must be able to check
  the claim. A comparison table cell that cannot be verified from public
  information fails no. 2 even if it is accurate.

**"Erkennbar" in § 6(1) is broad.** A competitor does not need to be named. "Unlike
legacy EUDAMED tools" identifies a competitor if the market can tell who is meant.
Anonymised comparisons are still comparative advertising.

---

## Abmahnung: why this is the expensive failure mode

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
