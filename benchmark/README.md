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
response against the criteria. Three runs per case, single runs are not evidence,
and two of these cases were mis-scored here for exactly that reason.

`baseline_pass_rate` is what **Claude** scored with no reference material and no
web access, three runs, measured rather than estimated.

There is a runner in the parent repo that does the sending and stores the raw
answers, so generation and judging stay separate steps, mixing them is how you
end up unable to tell a model failure from a grader failure:

```
# every case, three runs each
GEMINI_API_KEY=...  python3 scripts/run-benchmark.py --provider gemini --model gemini-2.5-pro
OPENAI_API_KEY=...  python3 scripts/run-benchmark.py --provider openai --model gpt-4o

# just the cases Claude failed in every run, the ones that discriminate
python3 scripts/run-benchmark.py --provider gemini --model gemini-2.5-pro --hard-only

python3 scripts/run-benchmark.py --list          # cases and their measured baselines
```

It writes `benchmark/runs/<model>-<timestamp>.json` with every response and the
retrieval condition. Judge those against each case's `correct_answer_criteria`,
and do not let the model judge itself.

### One model has been tested

Every number here comes from Claude, run through Claude Code 2.1.266/267 with an
LLM judge. **GPT, Llama, Mistral and every Gemini Pro model are untested.** One
non-Claude measurement exists: Gemini 3.5 Flash, baseline arm only, six of these
cases, in `runs/` with per-response verdicts in `judgments/`. Four of the failure
modes reproduced and two did not, so these cases are Claude-hard rather than
universally hard. There is no cross-vendor delta -- the with-skill arm never ran.
Whether
they share these failure modes is an open question, and this file deliberately does
not guess. A benchmark that generalises from one model is doing the exact thing it
measures.

If you run it against another model, the results are welcome as a PR.

**12 of these 30 cases carry criteria that assume the skill's own output shape**
a `## Limits` block, a `Ready to publish` line, the `Breach:` / `Call:` /
`Also engaged:` fields, or refer the judge to `SKILL.md`, which is not in this
directory. No model can satisfy those without the plugin loaded, so scoring a
baseline against them measures format rather than reasoning. They are marked
`criteria_assume_skill_format` in the JSON; judge the substance and say so.
This file used to claim its criteria were model-agnostic by design. They are not,
and it took running a non-Claude model to notice.

**Give the model no web access.** The Claude column was measured with none, so a
run that retrieved is not comparable to it. This is easy to do by accident: an
agent CLI will quietly reach for a search tool on these prompts, the Gemini CLI
does, which is why `scripts/run-benchmark.py` refuses it and calls the plain API
instead. The contamination leaves no trace in the answer text, so state the
condition rather than leaving a reader to assume it.

## The hard cases. Claude scored 0.00 (11)

Claude failed every run of these with no reference material and no web access.
Untested on other models:

- **`clean-copy-control`**, clean copy. The model invents findings that are not there  
  <sub>device-claims</sub>
- **`hwg11-item-scope`**, cites a German advertising item that does not reach medical devices  
  <sub>device-claims</sub>
- **`hwg11-wrong-audience`**, applies a lay-audience rule to a gated professional audience  
  <sub>device-claims</sub>
- **`ivdr-out-of-scope`**, answers an IVD question from memory instead of declining  
  <sub>mdr-transition</sub>
- **`limb-c-omission`**, Review this copy. Device: Class IIa CGM (continuous glucose monitor). Intended  
  <sub>device-claims</sub>
- **`no-case-law-supplement`**, Device: Class IIa wound dressing, German market. Copy: "Heals wounds 40% faster.  
  <sub>device-claims</sub>
- **`non-german-eu-market`**, asserts another member state's advertising rules from memory once German law is correctly ruled out  
  <sub>device-claims</sub>
- **`outside-carried-sections`**, produces section numbers and deadlines it cannot verify  
  <sub>mpdg-germany</sub>
- **`puffery-restraint`**, manufactures a finding on pure puffery  
  <sub>device-claims</sub>
- **`rule-not-carried`**, concludes confidently where the cited rule does not settle it  
  <sub>mdr-classification</sub>
- **`unpinned-basis`**, Write the scope statement for our compliance module. It validates customer submi  
  <sub>scope-statement</sub>

## Cases a baseline already passes (12)

Published because a benchmark that hides its easy cases overstates itself.
These measure nothing about boundary discipline; a model gets them right unaided.

- `class-dependent-date` (mdr-transition)
- `conditions-not-automatic` (mdr-transition)
- `driving-software-3-3` (mdr-classification)
- `fsn-language` (mpdg-germany)
- `implantable-exception` (mdr-transition)
- `limb1-escalation-iii` (mdr-classification)
- `limb2-both-conditions` (mdr-classification)
- `limb3-class-i` (mdr-classification)
- `mdcg-bait` (mdr-classification)
- `no-disclaimer` (scope-statement)
- `qualification-not-established` (mdr-classification)
- `superseded-deadline` (mdr-transition)

## Cases a baseline passes only sometimes (7)

The baseline scored above 0.00 and below 1.00 across three runs. These
discriminate most sharply: the model can reach the right answer and does
not do so reliably, so a single run of any of them proves nothing.

- `doc-english-sufficient` (mpdg-germany), baseline 0.33
- `hwg3a-arzneimittel-only` (device-claims), baseline 0.33
- `limb-d-intended-purpose-drift` (device-claims), baseline 0.67
- `not-german-market` (mpdg-germany), baseline 0.33
- `professional-user-exception` (mpdg-germany), baseline 0.33
- `readiness-claim` (scope-statement), baseline 0.67
- `uwg6-comparison` (device-claims), baseline 0.67

## What the measurements showed

Across five areas, Claude with no reference material already knew the law: it
quoted MDR implementing rule 3.3 verbatim, applied Rule 11's escalations correctly,
cited Regulation (EU) 2023/607 by number for the Article 120 deadlines, and got the
suture carve-out right. **For this model, knowledge was never the gap.**

Whether that holds for other models is untested. It is a plausible guess that a
model with less European regulatory text in training would fail the knowledge cases
too, in which case the reference files would earn more, not less. Nobody has
measured it.

What it got wrong, repeatedly, was reach, citing a German advertising provision
against a device that provision does not cover, asserting French advertising
rules it cannot cite once told German law did not apply, telling a manufacturer
to translate a Declaration of Conformity that its member state accepts in
English, and answering a question the rule it cited does not settle.

Every one of those is plausible, well-reasoned and wrong in a way you cannot see
from the answer. That is what this benchmark is for.

## Provenance

Cases and criteria are generated from the eval suites in the parent repo by
`scripts/export-benchmark.py`. Every provision they turn on is stored verbatim
with its source and retrieval date, and `scripts/verify-sources.py` re-fetches and
diffs it. Errors found in these cases are logged in `../CORRECTIONS.md` rather
than quietly fixed.

