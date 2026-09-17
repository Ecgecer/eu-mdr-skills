# Without the skill

Verbatim output, unedited. Same prompt, no plugin loaded. Run 1 of the baseline arm,
stored run `2026-09-17T18-43-23-939Z`. All three runs of this arm scored 0.00.

---

## Verdict

Both sentences are non-compliant for an ungated German consumer page. I'd treat this as blocking, not fixable by softening the wording — the endorsement has to come out entirely and the fear framing has to be replaced.

Standard caveat: this is a compliance read, not legal advice. Have your German regulatory counsel confirm the paragraph numbering before you rely on it.

## Blocking issue 1 — "Recommended by Professor Schmidt, cardiologist"

The Heilmittelwerbegesetz (HWG) applies to medical devices (§ 1 Abs. 1 Nr. 1a HWG, which references Art. 2 Nr. 1 MDR). For advertising directed at the public — *Publikumswerbung*, which an ungated web page is — § 11 Abs. 1 Nr. 2 HWG prohibits advertising with statements that the product is professionally recommended, tested, or used, or that reference a recommendation by scientists or persons working in healthcare. A named cardiologist's recommendation is the textbook case.

Notes on scope:

- It does not matter whether the recommendation is true, whether Prof. Schmidt is paid, or whether you add a disclosure. The prohibition is per se for the consumer channel.
- If there's an accompanying photo of the professor in a white coat or clinical setting, that's a separate hit under § 11 Abs. 1 Nr. 4 HWG (depiction of healthcare professionals in professional dress / practising their occupation).
- The endorsing physician has their own exposure under § 27 MBO-Ä (berufswidrige Werbung — physicians may not lend their name to product advertising), so this is a risk you're creating for them too.
- If "Professor Schmidt" is a composite or illustrative figure rather than a real consenting person, add misleading advertising under § 5 UWG and MDR Art. 7 to the list. If real, you need documented written consent for name use plus substantiation of the recommendation on file.

**Where it *can* live:** a genuinely gated HCP area addressed to *Fachkreise* (§ 2 HWG) is outside § 11's reach. § 3 HWG and the UWG still apply there, as does the physician's professional-code problem. Gating means real access control, not a "I am a healthcare professional" checkbox.

## Blocking issue 2 — "Don't gamble with your heart"

Two separate problems in six words.

**Fear-based appeal.** § 11 Abs. 1 Nr. 7 HWG prohibits consumer advertising with statements apt to induce or exploit anxiety. "Don't gamble with your heart" works precisely by suggesting that not using the product puts your heart at risk. This is one of the more reliably enforced provisions.

**Claim beyond intended purpose.** The device's intended purpose is non-invasive measurement of blood pressure. The copy implies cardiac protection — that using it safeguards your heart. Measuring is not treating, and a monitor prevents nothing on its own. That's a misleading claim under MDR Art. 7 (text creating a false impression regarding functions the device does not have) and § 3 HWG, and any promotional claim has to be consistent with the intended purpose and supported by your clinical evaluation.

## Secondary issue — "check your pressure daily"

This is a clinical recommendation on measurement frequency, issued by the manufacturer to consumers. Three things to resolve:

1. It must match your IFU. If the IFU doesn't recommend daily measurement, the web page contradicts the accompanying documentation.
2. It isn't what the guidelines say. ESH/ESC home-monitoring guidance centres on structured 7-day schedules (duplicate morning and evening readings, typically around consultations or during titration), not indefinite daily self-measurement. Routine daily measurement in unselected consumers is associated with anxiety and over-consultation.
3. Telling patients how often to measure, rather than deferring to their physician, is you giving medical advice. Refer the frequency decision to the treating physician.

## Suggested rewrite

Substance first — final copy needs to be in German for this market, so treat the English as a brief for the translator, and have the German reviewed rather than the English.

> **Klinisch validiert.** Die Messgenauigkeit ist nach ISO 81060‑2 geprüft.
>
> **Regelmäßig messen, Werte im Blick behalten.** Wie oft Sie zu Hause messen sollten, besprechen Sie am besten mit Ihrer Ärztin oder Ihrem Arzt.

(EN gloss: "Clinically validated — measurement accuracy tested to ISO 81060‑2." / "Measure regularly, keep track of your values. How often you should measure at home is best discussed with your doctor.")

This swaps a prohibited personal endorsement for an objective, product-level, substantiable fact, and swaps the fear appeal for a neutral benefit statement that defers frequency to the clinician.

Only use the ISO 81060‑2 line if you actually hold the validation report — clinical-validation claims are substantiation-bearing. A Deutsche Hochdruckliga *Prüfsiegel*, if you hold one, is widely used in German consumer BP-monitor advertising; I'd still run it past counsel, since § 11 Abs. 1 Nr. 2 reaches "professionally tested" and the permissibility rests on it being an objective institutional test mark rather than a personal recommendation.

## Before publishing

- Sweep the rest of the page and any linked assets for the same two patterns — expert endorsements and "what if you don't" framing tend to recur in headline, meta description, and social cards.
- Check whether Prof. Schmidt appears in imagery, video, or structured data anywhere else in the campaign.
- Confirm all on-page claims trace to the clinical evaluation and the IFU.

Enforcement risk here is real and cheap to trigger: HWG breaches in consumer advertising are routinely pursued by competitors and by bodies like the Wettbewerbszentrale and VSW via *Abmahnung*, and a named-physician endorsement on an open web page is about as visible as it gets.
