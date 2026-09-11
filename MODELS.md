# One skill, two models, opposite reasons

Every number elsewhere in this repo comes from one model. Claude Code's CLI default,
which is Opus. That made a finding look simpler than it is: **the skills add discipline,
not knowledge**, because every case that tested recall measured zero.

That was true of a model that already knows EU medical device regulation. It is not a
fact about the skills.

So the three statute-carrying suites were re-run pinned to **Haiku 4.5**, same cases, same
graders, same three runs per arm, no web access. The results are below and they are
generated from the stored runs by `scripts/report-evals.py`; the raw runs are in each
plugin's `evals/model-probes/`, which the published tables never read.

<!-- probe-table:start -->
**`device-claims`**, 10 cases. Mean delta **+0.77** on the CLI default, **+0.43** on `haiku`.

| Case | default baseline | default Δ | haiku baseline | haiku Δ |
|---|---|---|---|---|
| `hwg3a-arzneimittel-only` | 0.33 | +0.33 | 0.00 | +1.00 |
| `puffery-restraint` | 0.00 | +1.00 | 0.00 | +1.00 |
| `limb-d-intended-purpose-drift` | 0.67 | +0.33 | 0.00 | +0.33 |
| `uwg6-comparison` | 0.67 | +0.33 | 0.00 | +0.33 |
| `clean-copy-control` | 0.00 | +1.00 | 0.00 | +0.67 |
| `non-german-eu-market` | 0.00 | +1.00 | 0.00 | +0.67 |
| `no-case-law-supplement` | 0.00 | +0.67 | 0.67 | +0.00 |
| `hwg11-item-scope` | 0.00 | +1.00 | 0.00 | +0.33 |
| `hwg11-wrong-audience` | 0.00 | +1.00 | 0.00 | +0.33 |
| `limb-c-omission` | 0.00 | +1.00 | 0.67 | -0.33 |

**`mdr-classification`**, 7 cases. Mean delta **+0.14** on the CLI default, **+0.67** on `haiku`.

| Case | default baseline | default Δ | haiku baseline | haiku Δ |
|---|---|---|---|---|
| `driving-software-3-3` | 1.00 | +0.00 | 0.00 | +1.00 |
| `limb1-escalation-iii` | 1.00 | +0.00 | 0.00 | +1.00 |
| `limb3-class-i` | 1.00 | +0.00 | 0.33 | +0.67 |
| `mdcg-bait` | 1.00 | +0.00 | 0.00 | +0.67 |
| `limb2-both-conditions` | 1.00 | +0.00 | 0.33 | +0.33 |
| `qualification-not-established` | 1.00 | +0.00 | 1.00 | +0.00 |
| `rule-not-carried` | 0.00 | +1.00 | 0.00 | +1.00 |

**`mdr-transition`**, 5 cases. Mean delta **+0.20** on the CLI default, **+0.80** on `haiku`.

| Case | default baseline | default Δ | haiku baseline | haiku Δ |
|---|---|---|---|---|
| `class-dependent-date` | 1.00 | +0.00 | 0.00 | +1.00 |
| `conditions-not-automatic` | 1.00 | +0.00 | 0.00 | +1.00 |
| `implantable-exception` | 1.00 | +0.00 | 0.00 | +1.00 |
| `superseded-deadline` | 1.00 | +0.00 | 0.00 | +1.00 |
| `ivdr-out-of-scope` | 0.00 | +1.00 | 0.00 | +0.00 |
<!-- probe-table:end -->

## The reference text transfers. The refusal discipline does not.

The two models fail in opposite directions, and each half of a skill answers one of them.

**Where the skill supplies text**, Haiku gains everything and Opus gains nothing.
`mdr-transition`'s four knowledge cases run +0.00 for Opus and **+1.00 for Haiku**,
straight across. Opus quotes Article 120 as amended and cites Regulation (EU) 2023/607 by
number unaided. Haiku, with no reference file, answered the same classification case three
times citing **Rule 1, Rule 2 and Rule 10**, a different wrong rule each run, on a
question that turns on implementing rule 3.3. That is not over-reach. It is invention, and
a verbatim reference file removes it completely.

**Where the skill supplies discipline**, the ordering reverses. `hwg11-item-scope` and
`hwg11-wrong-audience` both measure **+1.00 for Opus and +0.33 for Haiku**: the same
instruction, a third of the benefit. `mdr-transition`'s `ivdr-out-of-scope` is the sharpest
case, **+1.00 for Opus, +0.00 for Haiku**. Haiku with the skill loaded gets the first half
right every time:

> IVDs fall under the **IVDR** (Regulation (EU) 2017/746), not the MDR, so the transition
> deadlines are **different** … the deadline is: **May 26, 2027**

It identifies the boundary and then steps over it, supplying a date from memory that the
skill explicitly forbids it to supply. It reads the rule and breaks it in the same
paragraph.

This is why the suite means move in opposite directions. `device-claims` is the
discipline-heavy suite, and it is the one where Haiku gains **less** than Opus
(+0.43 against +0.63). The knowledge-heavy suites invert it.

## Two results that only appear when you compare models

**The restraint case is easier for the model with less to be tempted by.**
`no-case-law-supplement` asks for a BGH holding that must be refused. Opus's baseline
scores **0.00**; Haiku's scores **0.67**. Haiku refuses because it cannot do otherwise
*"inventing a case name … I don't have reliable access"*, while Opus knows enough German
competition law to produce a confident, checkable-looking answer and does. Fabrication
risk is not inversely proportional to capability. On this case it rises with it.

**A skill can hand a weaker model the format without the substance.**
`limb-c-omission` measures **−0.33** on Haiku: the skill makes it worse. Its outputs carry
the full review structure (device, intended purpose, findings table, limits block) and
miss the omission finding the case exists to test in two runs of three. The template
travels more easily than the reasoning, and a well-structured wrong answer is harder to
catch than a badly structured one.

## A second vendor: Gemini 3.5 Flash, baseline only

Everything above is Claude on both sides. The first non-Claude measurement is narrower
than planned. The key's Pro-tier quota was already spent, and the free flash quota ran
out partway, but it answers a question nothing else here can.

**Six of the eleven hard cases** got three valid runs before the 429s started. The
with-skill arm returned **0 of 33**, so there is **no delta for Gemini**: what follows is
the baseline only, the model unaided.

| Case | Claude baseline | Gemini 3.5 Flash baseline |
|---|---|---|
| `clean-copy-control` | 0.00 | 0.00 |
| `hwg11-item-scope` | 0.00 | 0.00 |
| `no-case-law-supplement` | 0.00 | 0.00 |
| `non-german-eu-market` | 0.00 | 0.00 |
| `hwg11-wrong-audience` | 0.00 | **1.00** |
| `limb-c-omission` | 0.00 | **1.00** |

**Four failure modes reproduce across vendors.** These cases are in the benchmark because
Claude failed every run of them, and Gemini fails them too, in the same shapes:

- *Manufacturing findings on clean copy.* All three runs fault the copy for omitting
  "adults", one asserting outright: "Under MDR Article 7 … you must not omit limitations
  of use."
- *Citing items that do not reach devices.* Three runs, three different numbers for the
  same sentence (§ 11(1) no. 1, no. 1, no. 2) where the closing sentence of § 11(1)
  gives devices only nos. 7, 8, 9, 11 and 12. The same different-wrong-rule-each-time
  signature Haiku produced on Annex VIII.
- *Supplying case law on request.* "Here is the exact legal standard established by the
  BGH", no hedge, in all three runs.
- *Substituting another member state's law.* Gemini avoids the German-law trap cleanly and
  then asserts "Article L. 5213-3 of the CSP" and ANSM guidance as controlling, never
  reaching MDR Art. 7. Claude made the same error in prose; Gemini makes it with a
  specific article number, which is worse, because it is checkable-looking.

**Two do not reproduce.** `hwg11-wrong-audience` and `limb-c-omission` measure 1.00
unaided on Gemini and 0.00 on Claude. Gemini states that a gated Fachkreise page is
outside HWG § 11's reach, and it catches the CGM copy inviting a use the intended purpose
carves out. Claude's baseline does neither reliably.

So **the "hard cases" are Claude-hard, not universally hard**, and the benchmark had no
way to know that until a model from another vendor ran against it.

### What the judging cost in confidence

These verdicts are mine, recorded per response with reasons in
[`benchmark/judgments/`](benchmark/judgments/). Two things about them:

Twelve of the thirty cases carry criteria that assume the skill's output shape, so a
baseline cannot satisfy them on format regardless of its reasoning. Those criteria were
disregarded and substance judged instead; the protocol is written into the judgments file.
That defect was invisible while only Claude ran the benchmark.

And I am not a neutral judge. These are the repo's own skills. The guard is that the
criteria were fixed before any Gemini response existed and every verdict carries its
reason in text, so a reader can disagree with a specific call. On `limb-c-omission` the
call went against the repo.

## What this does not show

- **n=3 per arm.** The Claude comparison is one family, Opus against Haiku. The Gemini
  measurement is one tier (flash), one arm (baseline), six cases, and no delta at all
  it shows which failure modes are shared, not whether the skills help Gemini. GPT,
  Llama, Mistral and every Gemini Pro model remain untested.
- **2 of 36 Haiku baseline runs (6%)** declined on harness-identity grounds, "outside my
  scope as Claude Code, which is designed for software engineering tasks", rather than on
  the substance. Small, but it is in the denominator, and it may not reproduce outside
  Claude Code.
- **The probes ran against the skill text as it stood on 2026-09-11.** They are not
  re-run automatically and will drift; the stamps that protect the published tables do not
  cover this file.

## Why it matters anyway

The repo's headline claim was "these skills do not add knowledge, they add the discipline
to stop". That holds for a frontier model and is the wrong summary for a small one, where
the reference files are worth +1.00 a case and the discipline is worth a third of what it
is worth to Opus.

There is a cost note attached. On `mdr-classification` the whole suite ran for **$1.19** on
Haiku against **$7.91** on Opus, and Haiku-with-skill reached 1.00 on five of seven cases.
Where the work is knowledge-bound rather than judgement-bound, a small model carrying
verbatim statute is a real option. Where it turns on knowing when to stop, it is not.
