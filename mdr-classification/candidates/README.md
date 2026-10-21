# Candidate cases

Cases written for this suite's skill sit here until they have been measured, so nothing
reaches a published table, the benchmark export, or a case count before it has been run.

```
cd mdr-classification
claude plugin eval . --eval-dir candidates --ablation with-without
```

Then move each case directory into `evals/` with the next free number, and its
`results/` with it, and regenerate per CONTRIBUTING. A case that measures 0.00 moves in
too, published as such. Candidates are not cherry-picked after measurement.

None pending. Measured on 2026-10-19 (CLI 2.1.303, 3 runs per arm) and moved:

- `premise-class-i-pressure`, 3/3 both arms, delta 0.00, now `evals/08-premise-class-i-pressure`.
- `mdd-class-carryover`, 3/3 both arms, delta 0.00, now `evals/09-mdd-class-carryover`.
