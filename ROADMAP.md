# Roadmap

Candidates, with the evidence for and against each. Nothing here is committed; the point
is to make the reasoning inspectable so a bad idea can be argued down before it costs a
week.

---

## The evidence any new skill has to answer to

<!-- suite-summary:start -->
Measured across 5 suites, 30 cases:

| Suite | Mean delta | Cases measured | Content |
|---|---|---|---|
| `device-claims` | **+0.84** | 10 | MDR/IVDR Art. 7 **plus HWG and UWG** |
| `mpdg-germany` | **+0.62** | 5 | German national law only |
| `scope-statement` | +0.30 | 3 | domain-general |
| `mdr-classification` | +0.27 | 7 | EU-level only |
| `mdr-transition` | +0.20 | 5 | EU-level only |

**12 of those 30 cases measure a delta of 0.00**, the skill changes nothing. They are published case by case, because a suite that reports only what it earns is not reporting.
<!-- suite-summary:end -->

**The two highest carry German national law.** The EU-only skills trail them because
Claude already knows the Regulations, it quotes implementing rule 3.3 verbatim, cites
2023/607 by number, gets the suture carve-out right.

But the ordering is not simply "national law earns". `scope-statement` carries **no
statute at all** and sits third, above both EU-only suites, after a fix that stopped it
handing back a form instead of a finished statement. It earns by imposing a discipline
name the gap, do not pin to an authority you have not seen, on a task the model
otherwise does loosely. That is the same thing the German skills earn for, reached
without any national law, and it is the better statement of what this repo is for.

So the pattern is not "EU MDR is hard". It is **national law a model reaches for and
misapplies**. The cases measuring +1.00 are exactly that: a German advertising item
cited against a device it does not reach, a lay-audience rule applied to a gated
professional audience, French advertising rules asserted without a citation once German
law was correctly ruled out, and a Declaration of Conformity sent for translation that
Germany accepts in English.

Any sixth skill should be aimed there or it will measure zero.

---

## Candidate: MPBetreibV: who has to do what when operating a device in Germany

**What it is.** The Medizinprodukte-Betreiberverordnung governs *operating and using*
devices in Germany: instruction of users, maintenance, safety and metrological checks
(STK/MTK), the device register a facility must keep.

**Why it might earn, and this is the whole question.** Not because the model does not know
it. It probably does. Because the provision has two boundary traps of exactly the shape
that produced every +1.00 so far:

1. **It binds the *Betreiber*, not the manufacturer.** A manufacturer asking "what do we
   have to do" gets a wrong and expensive answer if operator duties are applied to them.
   That is the same error as applying a lay-audience rule to Fachkreise.
2. **STK and MTK intervals reach only listed device categories.** Applying them to all
   devices is over-application, and it is the shape the model repeats.

**Why it might not.** It is national law, which is the right target, but the audience is
hospitals and clinical engineering rather than manufacturers, further from the users of
everything else here. And if the model handles the Betreiber/Hersteller split cleanly, it
measures zero like the EU-only skills did.

**How to decide.** Write two cases first and measure them before building anything: one
where a manufacturer asks what they must do and the answer is "these are operator duties,
not yours", and one asking whether STK applies to a device outside the listed categories.
If the baseline fails those in 3 of 3 runs, build the skill. If it passes, do not.

### Measured 2026-09-11. The answer is no.

Both cases, three runs each, no plugin carrying MPBetreibV:

| Case | baseline |
|---|---|
| `operator-duties-not-manufacturer` | **1.00**, passes 3 of 3 |
| `stk-listed-categories` | **1.00**, passes 3 of 3 |

The rule set above says build it only if the baseline fails 3 of 3. It passes 3 of 3, on
both traps, and it corrects the premise without being asked:

> **Short answer: MPBetreibV does not land on you.** MPBetreibV is addressed to
> *Betreiber* (operators) and *Anwender* (users), hospitals, clinics, practices.

On the STK case it declines to supply an interval it cannot verify, flags that web access
was blocked, and names the sections to check. That is the behaviour the skill would have
been built to produce.

**So the sixth skill does not get built**, and that is the fourth prediction this repo has
made about where a skill would earn and lost. The prior three were classification, Article
120 and the two limb cases. The decision cost **$5.25** and forty minutes. Building the
skill and discovering it measured zero would have cost a week.

The cases stay in the repo. They are the evidence for the decision, and if a future model
regresses on either trap they are already written.

---

**The two cases.** [`mpdg-germany/roadmap-probe/`](mpdg-germany/roadmap-probe/) holds them,
outside `evals/` so nothing here reaches a published table. One command reproduces the
decision:

```
cd mpdg-germany && claude plugin eval . --eval-dir roadmap-probe --ablation with-without
```

The **without** arm is the measurement. Both graders judge whether the boundary was
tested rather than whether the model knows the Anlage, because the cases were written
without the MPBetreibV text pinned and a grader demanding a specific legal conclusion
would assert law this repo has not verified. Pin the text before building anything on
the result.

Source is available: gesetze-im-internet serves MPBetreibV, and it verifies with the
existing tooling.

---

## Candidates: EUDAMED roll-out, Article 10a, clinical equivalence

**Unmeasured. Written 2026-10-18, decided by the probe, not by this section.**

These came out of an external review of the repo: a model-written roadmap proposing
five skills, four new kinds of test, three distribution channels and a cross-vendor
cost study. Each idea was checked against the evidence above. Most were turned down
(see Rejected); three skills survive as probes, because they have the shape that has
earned here before, a real rule over-applied, and because their text post-dates most
training data, which the Art. 120 suite's text did not.

| Candidate | Text | Why it might earn | Why it might not |
|---|---|---|---|
| `eudamed-mandatory-rollout` | Art. 123(3)(d)-(ec) MDR, Art. 113(3)(f)-(fd) IVDR as amended by 2024/1860; Decision (EU) 2025/2371 | the Decision is from November 2025; "every legacy device", "EUDAMED is mandatory" for modules it does not cover, one date for MDR and IVDR | `superseded-deadline` showed Opus tracks amended transition law well |
| `article-10a-supply-interruption` | Art. 10a MDR, applicable since 10 January 2025 | a gated duty (serious harm, not custom-made, the manufacturer's own authority only) that invites over-application | one short article; a frontier model may simply know it |
| `clinical-equivalence` | Art. 61(4)-(6), Annex XIV Part A Section 3 | the 61(5) contract over-applied to Class IIa; FDA substantial equivalence imported | the 61(5) contract rule is the best-known change MDR made |

The external review got two dates wrong by a day (registration and certificate entry
both put on the 28th, where the MDR counts to the 27th), placed the well-established
technology exemption in 61(4) rather than 61(6), and described the 61(5) contract as
blocking equivalence when it governs only whether equivalence lets an implantable or
Class III device skip a clinical investigation. Those are the errors the candidate
skills would exist to catch, made by the document proposing them.

**The probe.** Thirteen cases in [`mdr-transition/roadmap-probe/`](mdr-transition/roadmap-probe/),
graders quoting the operative text verbatim from EUR-Lex. The decision rule is written
there before any result exists: build where the CLI-default baseline fails two of a
candidate's cases in 3 of 3 runs, do not build where it passes them all.

**Three candidate cases for existing suites**, outside `evals/` until measured:
`premise-class-i-pressure` and `mdd-class-carryover` in
[`mdr-classification/candidates/`](mdr-classification/candidates/), and
`fda-clearance-not-nb-application` in [`mdr-transition/candidates/`](mdr-transition/candidates/).
Pressure and jurisdiction-bleed are the shapes of `mdcg-bait` and `non-german-eu-market`,
the repo's strongest cases.

### The order to run it in

```
# 1. the probe, Claude, harness the tables use (~$5-10, as MPBetreibV was)
cd mdr-transition && claude plugin eval . --eval-dir roadmap-probe --ablation with-without

# 2. the candidates, both arms, since these skills exist
cd mdr-classification && claude plugin eval . --eval-dir candidates --ablation with-without
cd mdr-transition && claude plugin eval . --eval-dir candidates --ablation with-without

# 3. the probe on a second vendor, baseline only, thinking pinned
python3 scripts/run-benchmark.py --provider gemini --model <flash-tier> \
    --probe-dir mdr-transition/roadmap-probe --thinking-level medium
python3 scripts/judge-benchmark.py benchmark/runs/<run>.json
python3 scripts/score-benchmark.py --score benchmark/runs/<run>.json

# 4. the cross-vendor matrix the section below asks for: both arms, every case
for arm in "" "--with-skill"; do
  python3 scripts/run-benchmark.py --provider gemini --model <flash-tier> --thinking-level medium $arm
  python3 scripts/run-benchmark.py --provider gemini --model <pro-tier>   --thinking-level medium $arm
done
```

Steps 1 and 2 decide what gets built. Step 3 says whether a small model needs the
reference text even where Opus does not. Step 4 is the first cross-vendor delta this repo
will have; publish it per suite and per axis (`score-benchmark.py` prints both), not as a
single "cheap model plus skills beats frontier" line, because MODELS.md already predicts
the answer splits: detection transfers, boundary discipline does not.

---

## Paid: nine runs for every number three could not carry

Done 2026-09-18, $40.46, all on one pinned CLI version.

<!-- run-counts:start -->
11 case(s) are measured at nine runs per arm and 19 at three. **Every one of those has a delta of exactly 0.00 or 1.00, so none is ambiguous at its own sample size.**
<!-- run-counts:end -->

  implantable-exception          +0.33 ->  0.00     9/9 vs 9/9
  readiness-claim                -0.67 ->  0.00     8/9 vs 8/9
  fsn-language                   +0.33 -> +0.11     9/9 vs 8/9
  limb-d-intended-purpose-drift  +0.67 -> +0.56     8/9 vs 3/9
  limb-c-omission                +0.33 -> +0.56     9/9 vs 4/9
  uwg6-comparison                +0.33 -> +0.56     9/9 vs 4/9
  clean-copy-control             +0.67 -> +0.78     7/9 vs 0/9
  hwg3a-arzneimittel-only        +0.67 -> +1.00     9/9 vs 0/9
  professional-user-exception    +0.67 -> +1.00     9/9 vs 0/9
  mdcg-bait                      +1.00 -> +0.89     9/9 vs 1/9

Four down, six up. Three-run figures were not systematically inflated, they were simply
noise. `limb-c-omission` is the clearest case: its baseline across seven earlier runs
read 3/3, 3/3, 2/3, 1/3, 0/3, 2/3, and at nine runs it is 4/9. The true rate is near 44%,
so any three-run sample could land anywhere, and historically it landed at both extremes.

## What is still owed, and it is not more runs

**`readiness-claim` is unmeasurable, not zero.** At nine runs it read -0.33 on CLI 2.1.276
and 0.00 on 2.1.277, two consecutive point releases, identical skill text and grader. The
variance between releases exceeds the effect. Buying more runs would buy precision about
a target that moves faster than the samples accumulate. It is published as 0.00 because
that is what the current version measures, and this paragraph is the caveat.

**Every number here describes CLI 2.1.277 and nothing else.** Three versions passed
through this repo in 24 hours and each one moved results: a baseline went 1/9 to 3/3 on
one case, 9/9 to 1/9 on another, 0/3 to 8/9 on a third. The tables carry a CLI column per
row so this is visible rather than inferred, but no amount of sampling makes a number
survive the next release. Re-measure when the answer matters, not when the table looks old.

**`mpdg-germany` has a known blind spot**, disclosed in its own Limits block: ask it about
a non-German market and the answer is not governed by the skill at all. Measured three
times across three CLI versions, before and after an attempted fix. Any real fix has to
reach what the model reads before deciding relevance, which is not the skill body.

## Rejected, with reasons

**Another member state's national law**: France, Italy, Spain. The target is right and
the evidence supports it. Blocked on sourcing: gesetze-im-internet has no equivalent that
`verify-sources.py` can diff, and EUR-Lex's national-implementing-measures pages have been
unreachable. A reference nobody can verify is the thing this repo exists not to ship.

**More EU-level MDR**: qualification, GSPRs, technical documentation, clinical
evaluation. The two EU-only suites sit at the bottom of the table above, and the
prediction that classification and Article 120 would be different was wrong both times.

The sharper version of that rule is visible in *which* of their cases earn. In both
suites every case that supplies knowledge measures **0.00**, the baseline quotes
implementing rule 3.3 verbatim, cites 2023/607 by number, gets the suture carve-out
right. The entire delta of each suite comes from one case, and in both it is a boundary
case: `rule-not-carried`, where the baseline answers a question the rule it cites does
not settle, and `ivdr-out-of-scope`, where it answers an IVD question from memory instead
of declining.

So a third EU-level skill is not doomed. It is doomed *if it is built to inform*. Write
the boundary cases first, measure the baseline against them, and build only if it fails
them. The knowledge cases will measure zero whatever you do.

**A general "which jurisdiction applies" skill**: the highest-earning cases are
jurisdiction errors, so this looks attractive. But each existing skill already opens by
establishing market and audience, and `non-german-eu-market` (+1.00) shows that machinery
works where it exists. A standalone version would duplicate it.

**From the 2026-10-18 external review, turned down:**

- *An MDR and AI Act skill* (Art. 6(1) high-risk via notified-body involvement, Art.
  43(3) single conformity assessment). The traps are real and boundary-shaped, but the
  law is moving: the Digital Omnibus proposal to change the AI Act's high-risk dates was
  in the legislature at the last check, and harmonised standards are not published. A
  skill pinned to text that may be amended within months breaks the promise
  `verify-sources.py` makes. Revisit once the Omnibus outcome is in the Official Journal.
- *IVDR classification and companion diagnostics.* Knowledge-heavy, the shape that
  measures zero on the default model. The one boundary piece, the Art. 5(5) in-house
  justification date, was attributed by the review to 2024/1860; the delay comes from
  Regulation (EU) 2022/112 as best this repo can tell, unverified here. Hospital labs are
  also the MPBetreibV audience problem again.
- *A GitHub Action that comments regulatory verdicts on pull requests.* It applies the
  skills to a task none of their evals cover, code diffs, and its false positives would
  train engineers to ignore it. That is the opposite of what this repo is for.
- *An MCP server with a statute lookup tool.* `dist/` already serves every tool that
  cannot read the repo. Build it when someone asks, not before.
- *Multi-skill routing tests.* Real, `mpdg-germany`'s blind spot is one, but they
  measure the harness's skill selection more than the skills.
- *Context caching, OpenRouter, temperature 0.* Caching saves cents on a ~180-call matrix
  and adds a variable between arms; OpenRouter's failover hides which backend answered;
  temperature 0 is against Google's guidance for Gemini 3 and against the three-run
  method. The review's latency diagnosis was also wrong for this repo: the 2026-09-11
  Gemini arm died of a spent quota, not of reasoning loops. `run-benchmark.py` now aborts
  on quota exhaustion instead of failing every remaining case.

---

## Not a skill, and possibly the most valuable thing here

**Run the benchmark against more models.** Every number is from Claude. If another model
fails the *knowledge* cases Claude passes, the reference files earn more than measured,
and the repo's central finding narrows from "models know EU MDR" to "Claude does". That is
one afternoon of API calls and it changes what everything else means.
