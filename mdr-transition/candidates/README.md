# Candidate cases: not yet measured

Cases written for this suite's skill on 2026-10-18 and not yet run. They sit outside
`evals/` so nothing reaches a published table, the benchmark export, or a case count
before it has been measured.

```
cd mdr-transition
claude plugin eval . --eval-dir candidates --ablation with-without
```

Then move each case directory into `evals/` with the next free number, and its
`results/` with it, and regenerate per CONTRIBUTING. A case that measures 0.00 moves in
too, published as such. Candidates are not cherry-picked after measurement.

- `fda-clearance-not-nb-application`: an FDA clearance offered as meeting the Art. 120
  notified-body conditions.
