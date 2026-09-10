# eu-mdr-skills

Agent skills for EU medical device regulation that **say where the rules stop.**

Claude already knows MDR. Measured across 17 cases, it recalls implementing rule 3.3
verbatim, applies Rule 11's escalations correctly, and refuses to classify a non-device.
Knowledge is not the gap.

The gap is **confident over-reach.** In those same measurements it cited a German
advertising provision against a medical device that provision does not reach, in 3 of 3
runs. It applied German law to a French-market asset in 2 of 3. It escalated a device
class on half of a two-part condition in 3 of 3. It answered *"Class IIa, plan for a
notified body"* to a question the rule it cited does not settle.

Every one of those is plausible, well-reasoned, and wrong in a way you cannot see from
the answer. Not a hallucinated rule — a real rule applied one step past where it reaches.

These skills pin every finding to verbatim statute text, state what they do **not**
carry, and stop rather than conclude past their own boundary.

| Skill | Does | Instruments |
|---|---|---|
| `device-claims` | Reviews device and IVD marketing copy | MDR Art. 7, IVDR Art. 7, HWG, UWG |
| `mdr-classification` | Classifies software under Annex VIII | Implementing rules 3.1–3.7, Rule 11 |

**Not legal advice.** Drafting and risk-triage aids, not a substitute for a regulatory
professional or a Fachanwalt.

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

## Install

```
claude plugin marketplace add Ecgecer/eu-mdr-skills
claude plugin install device-claims@eu-mdr-skills          # advertising claims
claude plugin install mdr-classification@eu-mdr-skills     # software classification
```

## Use

```
/device-claims:device-claims-review     # review advertising copy
/mdr-classification:software-classification   # classify software under Annex VIII
```

The skill establishes two anchors before reviewing: the **intended purpose as assessed**
(the reference point for Art. 7(d)) and the **audience** (Fachkreise vs. Publikum, which
gates HWG § 11). It will ask for them rather than guess.

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
