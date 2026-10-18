# Candidate cases: not yet measured

Cases written for this suite's skill on 2026-10-18 and not yet run. They sit outside
`evals/` so nothing reaches a published table, the benchmark export, or a case count
before it has been measured.

```
cd mdr-classification
claude plugin eval . --eval-dir candidates --ablation with-without
```

Then move each case directory into `evals/` with the next free number, and its
`results/` with it, and regenerate per CONTRIBUTING. A case that measures 0.00 moves in
too, published as such. Candidates are not cherry-picked after measurement.

- `premise-class-i-pressure`: the user supplies the conclusion and asks for
  justification text. Measures whether the skill holds limb 1 under pressure.
- `mdd-class-carryover`: an MDD-era Class I carried into an MDR question.
