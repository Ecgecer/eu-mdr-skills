# Candidate cases

Cases written for this suite's skill sit here until they have been measured, so nothing
reaches a published table, the benchmark export, or a case count before it has been run.

```
cd mdr-transition
claude plugin eval . --eval-dir candidates --ablation with-without
```

Then move each case directory into `evals/` with the next free number, and its
`results/` with it, and regenerate per CONTRIBUTING. A case that measures 0.00 moves in
too, published as such. Candidates are not cherry-picked after measurement.

None pending. `fda-clearance-not-nb-application` was measured on 2026-10-19 (CLI 2.1.303,
3 runs per arm, 3/3 both arms, delta 0.00) and moved to `evals/06-fda-clearance-not-nb-application`.
