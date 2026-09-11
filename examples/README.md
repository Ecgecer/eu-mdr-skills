# A worked example

One prompt, run twice: once with the skill, once with nothing. Both outputs are
verbatim, straight from the eval harness. Neither has been edited.

> These transcripts are regenerated from the stored eval run by
> `scripts/build-example.py`, never edited. `tests/check-portable-fresh.py` fails if the
> skill moves ahead of them without this file saying so, and fails again if the notice is
> left behind once they match. They came out of run `2026-09-11T05-46-23-760Z`, case
> `hwg11-item-scope`, where all three with-skill runs scored 1.00 and all three baseline
> runs scored 0.00 — so "run 1 of each arm" chooses nothing.

## The prompt

> Review this copy. Device: **Class IIa home blood-pressure monitor.** Audience:
> public consumer web page, no gating. Market: **Germany.**
>
> Copy: *"Recommended by Professor Schmidt, cardiologist. Don't gamble with your heart
> — check your pressure daily."*

Two things in that copy need deciding. Is the fear framing a problem? And is the
physician endorsement a problem?

## What happens without the skill

[Full output.](without-skill.md) It gets the fear line right. On the endorsement it
says:

> **HWG § 11(1) Nr. 2** prohibits consumer advertising stating that a product is
> medically or otherwise professionally recommended, tested, or used.

That is a real provision, accurately described. It just **does not reach medical
devices.** The closing sentence of HWG § 11(1) reads:

> Für Medizinprodukte gilt Satz 1 **Nr. 7 bis 9, 11 und 12** entsprechend.

Devices get five of the fifteen items. No. 2 is not among them.

Act on that answer and you pull a lawful endorsement off a product page. Nothing in
the output tells you it is wrong — the provision is real, the description of it is
correct, and the reasoning reads well. **That is the failure mode this repo exists
for: not a hallucinated rule, but a real rule applied one step past where it reaches.**

Scored 0.00. Three judge votes FAIL. **3 of 3 runs.**

## What happens with the skill

[Full output.](with-skill.md) Same fear line, same finding — correctly under
§ 11(1) no. 7. On the endorsement:

> Third-party endorsements are **not** flatly prohibited for devices. § 11(1) no. 2
> (recommendations by healthcare professionals) does **not** apply to Medizinprodukte —
> only nos. 7, 8, 9, 11 and 12 do, per the closing sentence of § 11(1) `[verified]`.
> The applicable item is **no. 11**, which catches Äußerungen Dritter only where they
> are "missbräuchlich, abstoßender oder irreführender Weise". Nothing in front of me
> establishes that.

It then lists what *would* make it a finding — an undisclosed paid relationship, or a
misstated title — under `Also engaged`, marked as conditional on facts it does not
have.

Scored 1.00. Three judge votes PASS. **3 of 3 runs.**

## What this example is not

It is not evidence the skill makes a model better at reading the regulation. It
doesn't. Measured across 17 cases, the skill adds **nothing** where the model has to
recall a rule, reason from it, or be careful about something the question already
flagged — several cases measure a delta of exactly zero, and they are listed with the
rest in the eval records.

What it adds is the boundary: knowing that a rule it can quote correctly does not
reach the product in front of it.

Numbers, including the zeroes: [claims](../device-claims/evals/README.md) ·
[classification](../mdr-classification/evals/README.md)
