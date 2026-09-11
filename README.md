# eu-mdr-skills

[![verify](https://github.com/Ecgecer/eu-mdr-skills/actions/workflows/verify.yml/badge.svg)](https://github.com/Ecgecer/eu-mdr-skills/actions/workflows/verify.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Agent skills for EU medical device regulation that **say where the rules stop.**

The `verify` badge is not decoration. It runs `scripts/verify-sources.py`, which
re-fetches every statute source and diffs each quoted passage against it — so a green
badge means the text in this repo still matches the law it claims to quote, as of the
last run. It runs again every Monday.

Claude already knows MDR. Across this repo's 30 eval cases, the no-plugin baseline
recalls implementing rule 3.3 verbatim, applies Rule 11's escalations correctly, and
refuses to classify a non-device. Knowledge is not the gap.

The gap is **confident over-reach.** In those same measurements it cited HWG § 11(1)
no. 2 against a medical device, when only nos. 7 to 9, 11 and 12 reach devices, in 3 of
3 runs. Told a page was French-market only, it correctly dropped German law and then
asserted French advertising rules it cannot cite, in 3 of 3. It told a Dutch manufacturer
to translate a Declaration of Conformity into German on the authority of MDR Art. 19(4),
when MPDG § 8(1) accepts German **or** English, in 3 of 3. It answered *"Class IIa, plan
for a notified body"* to a question the rule it cited does not settle.

Every one of those is plausible, well-reasoned, and wrong in a way you cannot see from
the answer. Not a hallucinated rule — a real rule applied one step past where it reaches.

These skills pin every finding to verbatim statute text, state what they do **not**
carry, and stop rather than conclude past their own boundary.

| Skill | Answers | Carries |
|---|---|---|
| `device-claims` | "Can we say this in our copy?" | MDR Art. 7, IVDR Art. 7, HWG, UWG |
| `mdr-classification` | "What class is our software?" | Annex VIII impl. rules 3.1–3.7, Rule 11 |
| `mdr-transition` | "How long can we still sell this legacy device?" | Art. 120(3)–(3d) as amended by 2023/607 |
| `mpdg-germany` | "Does Germany want more than MDR?" | MPDG §§ 4, 8, 73 |
| `scope-statement` | "What should this report say it didn't check?" | nothing — domain-general |

Every skill ships an eval suite measured against a **no-plugin baseline**, and every suite
publishes the cases where the skill adds **nothing** — roughly half of them do.

**Measured numbers are deliberately not on this page.** They live in each suite's eval
README, generated from the stored run data by `scripts/report-evals.py`, because
hand-typed figures on a front page are how this repo published three wrong ones. See
[device-claims](device-claims/evals/README.md) ·
[mdr-classification](mdr-classification/evals/README.md) ·
[mdr-transition](mdr-transition/evals/README.md) ·
[mpdg-germany](mpdg-germany/evals/README.md) ·
[scope-statement](scope-statement/evals/README.md).

The pattern across the measured cases: positive delta wherever the model would
over-apply, over-conclude, invent an authority or reach for boilerplate; zero wherever it
already had what it needed. **These skills do not add knowledge. They add the discipline
to stop.**

> **Numbers are being re-measured (2026-09-10).** An adversarial review of all 25 graders
> found defects in both directions — graders failing correct answers, and graders that
> would pass wrong ones — plus three prompts that reused worked examples from the very
> reference files the with-skill arm loads. One published claim was false: the
> classification suite described a baseline failure that the stored runs show never
> happened, and that suite's only earning case is a grader artifact. Graders and prompts
> are fixed; the tables above will change when they re-run. What was wrong, and why, is
> written into each suite's eval README rather than quietly corrected. See
> [CORRECTIONS.md](CORRECTIONS.md).

**Not legal advice.** Drafting and risk-triage aids, not a substitute for a regulatory
professional or a Fachanwalt.

## A benchmark, if you build regulatory AI

[**`benchmark/`**](benchmark/) exports every eval case as a portable, Apache-2.0
benchmark with **measured** baseline difficulty. It answers one question about any model
or tool, not just this one:

> Does it apply EU medical device regulation to products, markets and audiences the
> provision it cites does not reach?

<!-- bench-counts:start -->
Of the 30 cases, **10 are ones Claude failed in every run** with no reference material and no
web access, 12 it passed in every run, and 8 it passed only sometimes. All three
groups are published, because a benchmark that hides its easy cases overstates itself.
<!-- bench-counts:end -->

Those hardest cases are what the benchmark is for — telling a manufacturer to translate a
Declaration of Conformity its member state accepts in English, citing a German advertising
item that does not reach devices, asserting French advertising rules it cannot cite once
told German law does not apply, manufacturing findings on clean copy.

**Only Claude has been tested.** GPT, Gemini and everything else are untested, and the
benchmark says so rather than generalising from one model — which would be the exact
failure it measures. Results from another model are welcome as a PR.

## See it before you install it

[**A worked example.**](examples/) One prompt, run with the skill and without it, both
outputs verbatim from the harness.

The short version: asked to review consumer copy for a Class IIa blood-pressure
monitor, the model without the skill cites **HWG § 11(1) Nr. 2** against the physician
endorsement. That provision is real and it described it accurately — but the closing
sentence of § 11(1) gives medical devices only **nos. 7, 8, 9, 11 and 12.** No. 2 does
not reach devices.

Act on it and you pull a lawful endorsement off a product page. Nothing in the answer
signals it is wrong. That happened in **3 of 3 runs**; with the skill, the correct
answer happened in 3 of 3.

## The method, if you want to copy it

[**METHOD.md**](METHOD.md) is how to build a regulatory skill worth trusting, for any
regulation. Measure before you build; pin the text and publish its edges; let the skill
refuse; test against a baseline or you are measuring the model; publish the cases where
you added nothing; make the claim executable.

It also lists every trap we walked into — graders that punish correct reasoning, a
freshness guard that could not see drift because it had been told what to look at, and
a confident prediction that measurement destroyed.

[CONTRIBUTING.md](CONTRIBUTING.md) turns that into what a new skill has to ship.

## Verify the claim yourself, in one command

Every provision these skills apply is stored **verbatim**, with its source URL and
retrieval date. That is easy to assert and worth nothing unless you can check it, so
checking it is one command:

```
python3 scripts/verify-sources.py
```

It re-fetches each source and confirms every quoted passage still appears, character
for character after whitespace and quote-glyph normalisation. Elided quotes are
verified fragment by fragment, because the joined string is not what the source says.

```
  OK            .../references/hwg.md  (6 fragments across 4 quotes match)
  OK            .../references/uwg.md  (5 fragments across 2 quotes match)
  UNVERIFIED    .../references/mdr-ivdr-art7.md
                fetch failed: HTTP Error 403: Forbidden
                check by hand: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32017R0745
                search the page for: "Article 7 Claims In the labelling, instructions for use..."
```

**It does not pass silently for what it could not read.** EUR-Lex blocks non-browser
clients, so MDR and IVDR text is reported as UNVERIFIED with the exact string to search
for. A verifier that reported success for a source it never fetched would be the same
defect these skills exist to prevent.

**Why the text is pinned locally at all.** EUR-Lex is not a dependable read-through
source. Over one afternoon it returned an HTTP 202 stub to scripted clients, then a
403, and then began redirecting every document URL — including ones that had served
the full text an hour earlier — to the Official Journal index, where it displays:

> EUR-Lex is temporarily not fully available.

That is an outage, not a block on any particular client, which is rather the point: the
authority can be unavailable for reasons that have nothing to do with you, at a moment
you did not choose. A skill that fetches the law when asked inherits that. A skill
carrying the text, dated, with a command to re-check it when the source returns, does
not.

If a quote drifts, it says where:

```
  DRIFTED       .../references/hwg.md  (1 of 6 fragments no longer match)
                quoted: "Unzulässig ist eine irrefuehrende Reklame. Eine Irreführung..."
                on page up to: "...Unzulässig ist eine irref"
```

Exit 0 when every fetched source matches, 1 on drift, 2 if nothing could be fetched.

| Reference | Source | Retrieved | Auto-verifiable |
|---|---|---|---|
| `hwg.md` | gesetze-im-internet.de/heilmwerbg | 2026-09-09 | yes |
| `uwg.md` | gesetze-im-internet.de/uwg_2004 | 2026-09-09 | yes |
| `mdr-ivdr-art7.md` | EUR-Lex, CELEX 32017R0745 / 32017R0746 | 2026-09-09 | no — EUR-Lex blocks scripted clients |
| `annex-viii-software.md` | EUR-Lex, CELEX 32017R0745, Annex VIII | 2026-09-09 | no — same |

The skills use two citation tiers: `[verified]` for provisions in those files, and
`[verify]` for anything else. They are instructed to refuse rather than supplement from
model knowledge.

## Scope limits, stated up front

**Statute text only.** No case law, no MDCG guidance, no notified-body practice, no
national enforcement decisions. UWG in particular is heavily shaped by BGH and OLG case
law this skill does not assess.

That limit is deliberate. Statutory text can be verified against a free primary source
and re-checked by anyone; case law cannot, without paid research access. A tool that
claims case-law coverage it cannot verify is worse than one that draws the line.

This is a drafting and risk-triage aid, **not legal advice**, and not a substitute for a
Fachanwalt für Medizinrecht or Wettbewerbsrecht.

## Which one do you want

| If you are asking | Use | It carries |
|---|---|---|
| "Can we say this in our copy?" | `device-claims` | MDR Art. 7, IVDR Art. 7, HWG, UWG |
| "What class is our software?" | `mdr-classification` | Annex VIII impl. rules 3.1–3.7, Rule 11 |
| "Does Germany want more than MDR?" | `mpdg-germany` | MPDG §§ 4, 8, 73 |
| "What should this report say it didn't check?" | `scope-statement` | nothing — domain-general |

Each is independent. Install only what you need; together they cost about 660 tokens
always-on.

## Install

```
claude plugin marketplace add Ecgecer/eu-mdr-skills

claude plugin install device-claims@eu-mdr-skills         # advertising claims
claude plugin install mdr-classification@eu-mdr-skills    # software classification
claude plugin install mpdg-germany@eu-mdr-skills          # German additions to MDR
claude plugin install scope-statement@eu-mdr-skills       # bound a compliance claim
```

## Use

```
/device-claims:device-claims-review              # review advertising copy
/mdr-classification:software-classification      # classify software under Annex VIII
/mpdg-germany:german-additions                   # what Germany adds on top of MDR
/scope-statement:scope-statement                 # bound a compliance result
```

Each skill establishes its own anchors before answering, and asks rather than guesses.
`device-claims` wants the intended purpose as assessed and the audience (Fachkreise vs.
Publikum, which gates HWG § 11). `mdr-classification` wants the intended purpose and
whether the product is qualified as a device at all. `mpdg-germany` wants confirmation
the German market is actually in play.

## Using it outside Claude Code

The substance is plain markdown. Only the packaging is Claude-specific.

| Tool | What to use |
|---|---|
| **Claude Code** | Install the plugin (above) |
| **Codex, Cursor, anything reading AGENTS.md** | [AGENTS.md](AGENTS.md) — it names the load order |
| **Gemini CLI** | [GEMINI.md](GEMINI.md) |
| **ChatGPT, Gemini web, Claude.ai, any chat** | Upload or paste the matching file in [`dist/`](dist/) — each bundles one skill with all its references |
| **Anything else** | The four source files in `device-claims/skills/device-claims-review/` |

`GEMINI.md` and the bundle are **generated** from the canonical skill:

```
python3 scripts/build-portable.py          # rebuild
python3 tests/check-portable-fresh.py      # fail if stale
```

Never edit them by hand. The freshness check exists because a drifted bundle would
have someone reviewing against an older rule while the repo claimed otherwise — the
exact failure this project is meant to prevent.

[AGENTS.md](AGENTS.md) lists the five invariants any port must preserve.

## Evals

Seven cases in [`device-claims/evals/`](device-claims/evals/), including three
false-positive controls:

| Case | Checks |
|---|---|
| `01-limb-d-intended-purpose-drift` | Catches a true claim that breaches Art. 7(d) |
| `02-hwg11-wrong-audience` | Does **not** apply § 11 to a Fachkreise audience |
| `03-hwg11-item-scope` | Does **not** cite § 11(1) no. 2 against a device (only nos. 7-9, 11, 12 apply) |
| `04-limb-c-omission` | Catches an omission where nothing is false |
| `05-uwg6-comparison` | Treats comparative advertising as lawful-if-compliant, not banned |
| `06-no-case-law-supplement` | Refuses to state a BGH holding as fact |
| `07-clean-copy-control` | Reports no findings on clean copy rather than inventing one |

`claude plugin eval device-claims` runs them where the eval harness is enabled.

## Licence and attribution

Apache-2.0. The review workflow, claim-block format, citation tiering and non-lawyer
approval gate derive from
[`anthropics/claude-for-legal`](https://github.com/anthropics/claude-for-legal)
(`product-legal/skills/marketing-claims-review`), Apache-2.0. See [NOTICE](NOTICE) for
what was changed.
