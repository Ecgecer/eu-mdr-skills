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
| `device-claims` | **+0.77** | 10 | MDR/IVDR Art. 7 **plus HWG and UWG** |
| `mpdg-germany` | **+0.53** | 5 | German national law only |
| `scope-statement` | +0.44 | 3 | domain-general |
| `mdr-transition` | +0.20 | 5 | EU-level only |
| `mdr-classification` | +0.14 | 7 | EU-level only |

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
cd mpdg-germany && claude plugin eval. --eval-dir roadmap-probe --ablation with-without
```

The **without** arm is the measurement. Both graders judge whether the boundary was
tested rather than whether the model knows the Anlage, because the cases were written
without the MPBetreibV text pinned and a grader demanding a specific legal conclusion
would assert law this repo has not verified. Pin the text before building anything on
the result.

Source is available: gesetze-im-internet serves MPBetreibV, and it verifies with the
existing tooling.

---

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

---

## Not a skill, and possibly the most valuable thing here

**Run the benchmark against more models.** Every number is from Claude. If another model
fails the *knowledge* cases Claude passes, the reference files earn more than measured,
and the repo's central finding narrows from "models know EU MDR" to "Claude does". That is
one afternoon of API calls and it changes what everything else means.
