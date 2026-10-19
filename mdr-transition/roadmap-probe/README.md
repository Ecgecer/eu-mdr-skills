# Roadmap probe: EUDAMED roll-out, Article 10a, clinical equivalence

Not a suite. Thirteen cases that decide whether up to three new skills get built, by
the rule in [`../../ROADMAP.md`](../../ROADMAP.md): write the boundary cases first,
measure the baseline, and build only if it fails them.

They live outside `evals/` deliberately. `report-evals.py` globs `*/evals/results/`, so
nothing here reaches a published table. `mdr-transition` hosts them only because the
harness needs a plugin directory. It carries Art. 120 and none of this text, so the
with-arm is not a test of anything here. The **without** arm is the measurement.

**Measured 2026-10-19, CLI 2.1.303. None of the three candidates gets built.** The
decision and its reasons are in [`../../ROADMAP.md`](../../ROADMAP.md). What `results/` holds:

| Folder | What ran |
|---|---|
| `2026-10-19T07-17-16-807Z` | All 13 cases, 3 runs per arm, CLI default model |
| `2026-10-19T07-39-18-914Z`, `…07-43-51-286Z`, `…07-47-42-778Z` | Nine runs per arm of `eudamed-mdr-ivdr-anchor`, `eudamed-nb-enters-certificates`, `nb-certificate-number`, CLI default |
| `haiku-4-5-2026-10-19T07-39-18-906Z` | All 13 cases, `--model claude-haiku-4-5` |
| `haiku-5-5-2026-10-19T07-39-18-914Z` | All 13 cases, `--model claude-haiku-5-5`. The harness could not write its own folder (timestamp collision with the nine-run batch), so this is its `--json` output, which is the same record without the HTML report |
| `blind-regrade-2026-10-19` | The second grader's verdicts on every failed nine-run baseline run, the items it saw, and the key it did not |

The harness records the CLI version but not the model, so the folder name is the only
record of which model a pinned run used.

## Run it

Claude, through the harness the published tables use:

```
cd mdr-transition
claude plugin eval . --eval-dir roadmap-probe --ablation with-without
```

Repeat with the model pinned to Haiku for the small-model column (see MODELS.md for
how the probes there were pinned).

Any other model, through the plain API with no retrieval:

```
python3 scripts/run-benchmark.py --provider gemini --model <flash-tier> \
    --probe-dir mdr-transition/roadmap-probe --thinking-level medium
python3 scripts/judge-benchmark.py benchmark/runs/<that run>.json
python3 scripts/score-benchmark.py --score benchmark/runs/<that run>.json
```

## The three candidates and their cases

**`eudamed-mandatory-rollout`**, Art. 123(3)(d) to (ec) MDR and Art. 113(3)(f) to (fd)
IVDR as amended by Regulation (EU) 2024/1860, plus Commission Decision (EU) 2025/2371.
The text post-dates most training data, which is the argument this might measure
something the Art. 120 suite did not.

| Case | Trap |
|---|---|
| `eudamed-legacy-not-placed-after-mandatory` | "every legacy device" when the duty reaches only devices placed on the market from 28 May 2026 |
| `eudamed-successor-registered` | misses the exception where the MDR-certified device is already registered |
| `eudamed-mdr-ivdr-anchor` | one date for both, when MDR counts 12 months from publication and IVDR 6 months from application |
| `eudamed-nb-enters-certificates` | certificate entry is the notified body's duty; no SSCP for Class IIb non-implantables |
| `eudamed-vigilance-not-mandatory` | "EUDAMED is mandatory" applied to a module the Decision did not cover |
| `udi-software-minor-vs-algorithm` | Annex VI Part C 6.5. A knowledge case, expected to measure zero, included to find out |
| `emdn-no-lookup` | a leaf EMDN code from memory, for a registration record |
| `nb-certificate-number` | an invented certificate number "in the usual format" |

**`article-10a-supply-interruption`**, MDR Art. 10a, applicable since 10 January 2025.
The shape that has earned before: a real rule over-applied.

| Case | Trap |
|---|---|
| `art10a-routine-stockout` | notice demanded for a stockout below the serious-harm threshold |
| `art10a-addressees` | manufacturer told to notify every Member State and the Commission, which is the authority's job under 10a(2) |
| `art10a-custom-made-excluded` | applied to custom-made devices, which 10a(1) excludes |

**`clinical-equivalence`**, Art. 61(4) to (6) and Annex XIV Part A Section 3.

| Case | Trap |
|---|---|
| `equivalence-contract-overapplied` | the Art. 61(5) contract demanded for a Class IIa non-implantable |
| `equivalence-510k-predicate` | FDA substantial equivalence imported, and a cage placed on the closed 61(6)(b) list |

## Decision rule, fixed before any result exists

For each candidate, on the **Claude CLI default** baseline:

- **Build** if it fails at least two of its cases in 3 of 3 runs.
- **Do not build** if it passes all its cases in at least 2 of 3 runs. Record the
  result in ROADMAP the way MPBetreibV was recorded.
- **In between**, re-run the ambiguous cases at nine runs before deciding.

**The nine-run step, fixed 2026-10-19 after the three-run result and before any nine-run
result exists.** The three-run rule above did not say how to read nine runs, so this does:

- A case **fails** if its baseline fails at least **6 of 9** runs. At a true failure rate
  of 30% that happens 2% of the time, at 50% 25%, at 70% 73%: it separates "usually
  fails" from an occasional slip without missing a case that usually fails.
- **Build** if at least two of the candidate's cases fail, counting cases that already
  failed 3 of 3. **Do not build** otherwise. Nine runs is final; there is no third zone
  and no further re-run.
- **A run counts as a failure only if two graders agree.** The harness judge's score
  stays the published score. Every failed baseline run is re-graded blind by a separate
  model given only the grader criteria and the response, not the judge's verdict. Where
  they disagree, the run does not count toward the decision and the disagreement is
  reported with its reason. The three-run result showed why: `eudamed-nb-enters-certificates`
  failed two runs that meet both of its criteria on a plain reading.
- Only what a grader tests counts. Errors a case does not grade (wrong dates in a
  certificate case, say) are reported as evidence, not scored.
- The two-case bar stands even where one case fails badly. A single severe miss is
  recorded as its own question, not read as meeting the rule.

Separately, if **Haiku** or a flash-tier model fails the detection cases (`03` and
`06`, the two tagged `detection`) that Opus passes, record it. MODELS.md found that reference text transfers
to small models where discipline does not, so a reference-only skill may be justified
for small models even where Opus measures zero. That is a separate decision, made on
those numbers.

## Before building anything on a result

The graders quote the operative text verbatim, retrieved from EUR-Lex on 2026-10-18,
so they judge against the law rather than against what the author remembers. A skill
built on these cases must still carry that text in `references/`, with entries in
`scripts/verify-sources.py`:

- Regulation (EU) 2024/1860: `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1860`
- Decision (EU) 2025/2371: `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32025D2371`
- Regulation (EU) 2017/745 is already a source.

Both fetched cleanly by script on 2026-10-18.

One judgement call is written into a grader rather than resolved. `eudamed-mdr-ivdr-anchor`
does not fail on the day of the month: the MDR date computes to 27 November 2026 under
Regulation 1182/71, and the IVDR date sits a day either side of it depending on how its
anchor is read. The grader records which day a response gave instead of scoring it.
