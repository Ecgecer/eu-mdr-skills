# eu-mdr-bench

A benchmark for one question: **does your model apply EU medical device
regulation to things the provision it cites does not reach?**

Not a knowledge test. Every case here is one a competent model can reason about;
what it measures is whether the model knows where the rule stops.

**30 cases**, 30 with measured baseline difficulty. Apache-2.0.
Machine-readable in [`eu-mdr-bench.json`](eu-mdr-bench.json).

## How to run it

Each case has a `prompt` and a `correct_answer_criteria` written for an LLM judge.
Send the prompt to the system under test with no other context, then score the
response against the criteria. Three runs per case — single runs are not evidence,
and two of these cases were mis-scored here for exactly that reason.

`baseline_pass_rate` is what **Claude** scored with no reference material and no
web access, three runs, measured rather than estimated.

### One model has been tested

Every number here comes from Claude, run through Claude Code 2.1.266/267 with an
LLM judge. **GPT, Gemini, Llama, Mistral and everything else are untested.** Whether
they share these failure modes is an open question, and this file deliberately does
not guess — a benchmark that generalises from one model is doing the exact thing it
measures.

If you run it against another model, the results are welcome as a PR. The cases and
criteria are model-agnostic by design; only the measured column is not.

## The hard cases — Claude scored 0.00 (12)

Claude failed every run of these with no reference material and no web access.
Untested on other models:

- **`clean-copy-control`** — clean copy — the model invents findings that are not there  
  <sub>device-claims</sub>
- **`doc-english-sufficient`** — tells a manufacturer to translate a DoC its member state accepts in English  
  <sub>mpdg-germany</sub>
- **`hwg11-item-scope`** — cites a German advertising item that does not reach medical devices  
  <sub>device-claims</sub>
- **`hwg11-wrong-audience`** — applies a lay-audience rule to a gated professional audience  
  <sub>device-claims</sub>
- **`hwg3a-arzneimittel-only`** — applies a medicinal-product provision to a device  
  <sub>device-claims</sub>
- **`ivdr-out-of-scope`** — answers an IVD question from memory instead of declining  
  <sub>mdr-transition</sub>
- **`limb-d-intended-purpose-drift`** — a true claim that still breaches, and cannot be cured by evidence  
  <sub>device-claims</sub>
- **`non-german-eu-market`** — applies German national law to a French-market asset  
  <sub>device-claims</sub>
- **`outside-carried-sections`** — produces section numbers and deadlines it cannot verify  
  <sub>mpdg-germany</sub>
- **`puffery-restraint`** — manufactures a finding on pure puffery  
  <sub>device-claims</sub>
- **`rule-not-carried`** — concludes confidently where the cited rule does not settle it  
  <sub>mdr-classification</sub>
- **`uwg6-comparison`** — mishandles comparative advertising that is lawful when compliant  
  <sub>device-claims</sub>

## Cases a baseline already passes (13)

Published because a benchmark that hides its easy cases overstates itself.
These measure nothing about boundary discipline; a model gets them right unaided.

- `class-dependent-date` (mdr-transition)
- `conditions-not-automatic` (mdr-transition)
- `driving-software-3-3` (mdr-classification)
- `fsn-language` (mpdg-germany)
- `implantable-exception` (mdr-transition)
- `limb-c-omission` (device-claims)
- `limb1-escalation-iii` (mdr-classification)
- `limb2-both-conditions` (mdr-classification)
- `limb3-class-i` (mdr-classification)
- `mdcg-bait` (mdr-classification)
- `no-disclaimer` (scope-statement)
- `qualification-not-established` (mdr-classification)
- `superseded-deadline` (mdr-transition)

## What the measurements showed

Across five areas, Claude with no reference material already knew the law: it
quoted MDR implementing rule 3.3 verbatim, applied Rule 11's escalations correctly,
cited Regulation (EU) 2023/607 by number for the Article 120 deadlines, and got the
suture carve-out right. **For this model, knowledge was never the gap.**

Whether that holds for other models is untested. It is a plausible guess that a
model with less European regulatory text in training would fail the knowledge cases
too — in which case the reference files would earn more, not less. Nobody has
measured it.

What it got wrong, repeatedly, was reach — citing a German advertising provision
against a device that provision does not cover, applying German law to a
French-market asset, telling a manufacturer to translate a Declaration of
Conformity that its member state accepts in English, and answering a question the
rule it cited does not settle.

Every one of those is plausible, well-reasoned and wrong in a way you cannot see
from the answer. That is what this benchmark is for.

## Provenance

Cases and criteria are generated from the eval suites in the parent repo by
`scripts/export-benchmark.py`. Every provision they turn on is stored verbatim
with its source and retrieval date, and `scripts/verify-sources.py` re-fetches and
diffs it. Errors found in these cases are logged in `../CORRECTIONS.md` rather
than quietly fixed.

