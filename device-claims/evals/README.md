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

Measured by `claude plugin eval . --ablation with-without`, 3 runs per case per arm.
42 runs, $10.56, 2026-09-09, commit 8ca1576.

| Case | with | without | delta |
|---|---|---|---|
| `clean-copy-control` | 1.00 | **0.00** | **+1.00** |
| `hwg11-item-scope` | **0.67** | 0.00 | +0.67 |
| `no-case-law-supplement` | 1.00 | 0.33 | +0.67 |
| `hwg11-wrong-audience` | 1.00 | 0.67 | +0.33 |
| `limb-d-intended-purpose-drift` | 1.00 | 1.00 | **0.00** |
| `limb-c-omission` | 1.00 | 1.00 | **0.00** |
| `uwg6-comparison` | **0.67** | 0.67 | **0.00** |

**Mean delta +0.38.**

### Read this honestly

**Two cases fail one run in three even with the skill.** `hwg11-item-scope` and
`uwg6-comparison` score 0.67. An earlier hand-run pass of one run each reported 7/7;
that was one lucky run apiece. The real figure is 5 of 7 at 1.00.

**Half the skill earns nothing.** Both MDR Art. 7 limb cases measure delta 0.00. The
baseline finds intended-purpose drift and the omission unaided.

**The value is restraint and German scoping.** The baseline scores 0.00 on clean copy
across all three runs, so it manufactures findings every time. It cannot keep HWG § 11
off a Fachkreise audience, cannot keep § 11(1) no. 2 off a device, and states BGH
holdings as fact.

The accurate claim is narrow: this stops a model inventing German provisions and
inventing findings. It does not improve Art. 7 reading.

### Where it still fails

`uwg6-comparison` is weakest, 0.67 with delta 0.00, so the § 6 guidance is not carrying
its weight. `hwg11-item-scope` at 0.67 means the most important false-positive guard
fires only two runs in three.

### The case 03 baseline — the decisive one

Case 03 was also run with no skill and no references. It produced the exact error the
case exists to catch, with no hedging:

> "**§ 11 Abs. 1 Satz 1 Nr. 2 HWG** [...] This is one of the most frequently enforced
> provisions of the HWG and **applies with full force here** precisely because there is
> no professional gate."

HWG § 11(1) sentence 2 reads: *"Für Medizinprodukte gilt Satz 1 **Nr. 7 bis 9, 11 und
12** entsprechend."* No. 2 is not among them. It does not apply to medical devices.

The consequence is not academic. Acting on that advice means pulling a lawful
professional endorsement off a product page because a model cited a provision that does
not reach the product.

The same baseline also placed the fear-appeal prohibition under no. 11 (it is no. 7;
no. 11 is third-party testimonials), while noting the numbering "should be checked" —
hedged, but still wrong. And it introduced § 27 MBO-Ä, § 3a UWG and § 12 HWG without
marking any as unverified.

The skill-equipped run on the identical prompt cited **no. 7** for the fear appeal,
explicitly declined to cite no. 2, and routed the endorsement to no. 11 with its
*missbräuchlich / abstoßend / irreführend* qualifier intact.

### What the ablation shows

| | Baseline (no skill) | With skill |
|---|---|---|
| Finds the substantive problem | **Yes** — both cases | Yes |
| Cites provisions that exist and reach the product | **No** — 1 hard error, 1 misnumbering across 2 cases | Yes |
| Marks unverified sources | No | Yes |
| Declines case law | No — asserted MBO-Ä, § 3a UWG, Art. 61, Art. 95/97 | Yes |

The skill does not make the model smarter about advertising. It stops it inventing
German provisions and stops it applying real ones to products they do not cover.

Two baseline arms, one run each. Directional, not conclusive, until the harness can run
a real ablation across the suite.

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
