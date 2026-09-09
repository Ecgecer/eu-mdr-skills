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

### Two harness gotchas

`--case` matches the **frontmatter `name`**, not the directory. `--case '03*'` finds
nothing; `--case 'hwg11-item-scope'` works.

`--case` is **not repeatable**. Passing it twice silently runs only the last one —
a run given `--case 'hwg11-item-scope' --case 'uwg6-comparison'` reported
`1 case(s)`. Use a glob that covers both, or run the whole suite.

## The case that matters most

`03-hwg11-item-scope`. HWG § 11(1)'s closing sentence limits devices to nos. 7, 8, 9,
11 and 12. Citing no. 2 (professional endorsements) against a medical device is wrong,
and it is the error a model is most likely to make, because no. 2 reads like it should
apply and the restriction lives in a single sentence at the end of a long list.

## Results

`claude plugin eval . --ablation with-without`, 3 runs per case per arm.
Six cases measured 2026-09-09 at commit 8ca1576; four re-measured at 0a520dd after
two grader fixes and three new cases.

| Case | with | without | delta | kind |
|---|---|---|---|---|
| `clean-copy-control` | 1.00 | 0.00 | **+1.00** | restraint |
| `hwg11-item-scope` | 1.00 | 0.00 | **+1.00** | scoping |
| `no-case-law-supplement` | 1.00 | 0.33 | +0.67 | refusal |
| `non-german-eu-market` | 1.00 | 0.33 | +0.67 | scoping |
| `hwg3a-arzneimittel-only` | 1.00 | 0.33 | +0.67 | scoping |
| `hwg11-wrong-audience` | 1.00 | 0.67 | +0.33 | scoping |
| `puffery-restraint` | 1.00 | 0.67 | +0.33 | restraint |
| `limb-d-intended-purpose-drift` | 1.00 | 1.00 | 0.00 | detection |
| `limb-c-omission` | 1.00 | 1.00 | 0.00 | detection |
| `uwg6-comparison` | 1.00 | 1.00 | 0.00 | detection |

**Mean delta +0.47. All ten score 1.00 with the skill.**

### The pattern is clean, and it is one-sided

Every case with a positive delta is a false-positive control, a scoping test, or a
refusal test. Every case with zero delta asks the model to FIND something.

A competent model already reads MDR Art. 7 and UWG § 6 at ceiling. What it cannot do
unaided is stop: it cites HWG § 11(1) no. 2 against a medical device in 3 of 3 runs,
applies German law to a French-market asset in 2 of 3, applies HWG § 3a to a device
in 2 of 3, and manufactures findings on clean copy in 3 of 3.

So this skill does not make a model better at reading the regulation. It stops it
over-applying provisions to products, markets and audiences they do not reach.

### Two earlier results were wrong, both mine

`hwg11-item-scope` and `uwg6-comparison` first measured 0.67 because the graders
punished correct reasoning. One could not tell "§ 11(1) no. 2 does not apply to
Medizinprodukte" from citing no. 2 against a device. The other demanded an explicit
affirmation that lawful comparisons exist, which a correct analysis of three
defective claims never has occasion to make. Fixed; `hwg11-item-scope` then measured
+1.00 rather than +0.67.

An earlier hand-run pass reported 7/7 from one run per case. Three runs found
nondeterminism it could not. Single runs are not evidence.

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
