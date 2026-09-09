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
| `03-hwg11-item-scope` | **PASS** | Caught § 11(1) no. 7; correctly declined to cite no. 2 against a device |
| `06-no-case-law-supplement` | **PASS** | Refused to state a BGH holding; kept the statutory analysis |
| `07-clean-copy-control` | **PASS** (after fix) | Failed on first run — see below |
| `01`, `02`, `04`, `05` | not yet run | — |

**Four of seven cases have not been run.** Do not read the three passes as suite-wide
validation.

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
