# Evals

Seven cases. Three are **false-positive controls** (`02`, `03`, `07`) — they fail if
the skill invents findings or applies a provision outside its scope. A claims-review
skill that only tests for catches will happily flag everything.

## Running

```
claude plugin eval device-claims
```

**Note:** `claude plugin eval` is currently early-access gated. On an account without
it enabled the command exits with `plugin eval is currently in early access` and runs
nothing. These cases have therefore been validated by running the prompts against the
skill manually rather than through the harness — see the repo README.

To run one manually: give a fresh agent the SKILL.md plus the three reference files,
paste the case `prompt`, and check the output against that case's grader text.

## The case that matters most

`03-hwg11-item-scope`. HWG § 11(1)'s closing sentence limits devices to nos. 7, 8, 9,
11 and 12. Citing no. 2 (professional endorsements) against a medical device is wrong,
and it is the error a model is most likely to make, because no. 2 reads like it should
apply and the restriction lives in a single sentence at the end of a long list.

## Results

Run manually against fresh agents (the native harness is early-access gated), 1 run
per case, 2026-09-09, commit `02c0276`.

| Case | Result | Note |
|---|---|---|
| `01-limb-d-intended-purpose-drift` | **PASS** | Art. 7(d) named; not treated as curable by evidence |
| `02-hwg11-wrong-audience` | **PASS** | § 11 declared inapplicable (Fachkreise); § 3 / § 5 analysis retained |
| `03-hwg11-item-scope` | **PASS** | Caught § 11(1) no. 7; correctly declined to cite no. 2 against a device |
| `04-limb-c-omission` | **PASS** | Art. 7(c) raised from the intended purpose's own rapid-change caveat |
| `05-uwg6-comparison` | **PASS** | § 6(1) recognised without a named competitor; not treated as banned |
| `06-no-case-law-supplement` | **PASS** | Refused to state a BGH holding; kept the statutory analysis |
| `07-clean-copy-control` | **PASS** (after fix) | Failed on first run — see below |

**7/7, one run each.** One run is not three; the harness default is 3 and would catch
nondeterminism this does not.

## Ablation: what the skill actually causes

Case 01 was also run with **no skill and no reference files**, same prompt.

The baseline **found the Art. 7(d) intended-purpose drift correctly** and quoted the
limb accurately. On the headline catch there is **no delta** — a competent model does
not need this skill to notice that selling a clinical ECG patch to athletes is a
problem.

The delta is citation integrity. The baseline asserted:

> "**Heilmittelwerbegesetz (HWG) §11 Abs. 1 Nr. 11**, which prohibits advertising that
> could give the impression that consulting a doctor/healthcare professional is
> unnecessary"

HWG § 11(1) no. 11 is **third-party testimonials** (*Äußerungen Dritter*, Dank-,
Anerkennungs- oder Empfehlungsschreiben). The content the baseline attributed to it
does not appear anywhere in § 11. It also sprawled into MDR Art. 61, Annex I, Art. 20,
Art. 10(6), Art. 95/97 and the UCPD without marking any of it unverified.

**So the value is not finding more. It is not inventing provisions, and saying plainly
where the line is.** That is the claim the repo makes, and this is the evidence for it.

One baseline arm on one case is weak evidence. Treat it as directional until the
harness can run a real ablation across the suite.

### What case 07 caught

On its first run the skill returned three material findings on copy written to be
compliant. The cause was the claim block, not the model: it forced a `Breach:` field
on every entry, so an open question ("is 14 days inside the assessed scope?") was
promoted to an Art. 7(a) breach. It also raised Art. 7(c) by inferring a likely risk
from the device category rather than from supplied material — reasoning that, applied
generally, condemns every benefit-framed device advertisement.

Fixed in `02c0276` by adding `Call: Verify` with `Breach: none`, requiring limb (c)
findings to name a risk from supplied material, and adding an explicit
do-not-manufacture-findings rule.

This is the case that justifies the suite. Both catch-tests passed and would have
supported a claim that the skill worked.
