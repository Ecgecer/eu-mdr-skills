# Roadmap probe — MPBetreibV

Not a suite. Two cases that decide whether the sixth skill gets built, per the rule in
[`../../ROADMAP.md`](../../ROADMAP.md): *"Write two cases first and measure them before
building anything ... If the baseline fails those in 3 of 3 runs, build the skill. If it
passes, do not."*

They live outside `evals/` deliberately. `report-evals.py` globs `*/evals/results/`, so
nothing here reaches a published table, and the marketplace check does not see a plugin
that does not exist yet.

## Run it

```
cd mpdg-germany
claude plugin eval . --eval-dir roadmap-probe --ablation with-without
```

The **without** arm is the measurement. `mpdg-germany` carries MPDG §§ 4, 8 and 73 and
no MPBetreibV at all, so the with-arm is not a test of anything — it is there because the
harness produces the no-plugin baseline as the other half of an ablation.

## What each case tests

**`operator-duties-not-manufacturer`** — a manufacturer asks what MPBetreibV requires of
*them*. It binds the Betreiber, not the Hersteller. Same shape as applying a lay-audience
advertising rule to Fachkreise: a real provision, accurately described, applied to a party
it does not reach.

**`stk-listed-categories`** — a hospital asks to confirm an STK interval and whether it
can be stretched. The obligation reaches listed device categories and devices the
manufacturer prescribes a check for, so "which interval" is the second question. The
first is whether the duty exists.

## Reading the result

Both graders judge whether the boundary was tested, not whether the model knows the
Anlage. That is deliberate: the cases were written without the MPBetreibV text pinned, and
a grader that required a specific legal conclusion would be asserting law this repo has
not verified. **Anyone building the skill must pin and verify the text first** — the
source is on gesetze-im-internet and the existing tooling handles it.

If the baseline passes these, the skill measures zero and should not be built, which is
the outcome three predictions in this repo have already had.
