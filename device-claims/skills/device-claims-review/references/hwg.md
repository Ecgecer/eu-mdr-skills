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
