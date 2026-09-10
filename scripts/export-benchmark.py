#!/usr/bin/env python3
"""Export the eval cases as a portable benchmark, with measured baseline difficulty.

The cases here were written to test skills, but what they actually measure is whether a
model over-applies EU medical device regulation — citing a provision against a product,
market or audience it does not reach. That question is not Claude-specific and the cases
should not be locked in one harness's format.

Difficulty comes from the stored runs: the no-skill baseline pass rate. A case where
three of three baseline runs fail is a hard case, and we can say so with evidence rather
than assertion.

Usage:  python3 scripts/export-benchmark.py
"""
import glob, json, re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "benchmark"

def baseline_scores():
    """case -> (baseline pass rate, with-skill pass rate, runs) from the newest full run."""
    latest = {}
    for f in sorted(glob.glob(str(ROOT / "*/evals/results/*/aggregate-result.json"))):
        try: d = json.load(open(f))
        except Exception: continue
        ts = Path(f).parent.name
        for c in d.get("cases", []):
            arms = c.get("arms", {})
            wo = [r for r in arms.get("without", []) if not r.get("error")]
            wi = [r for r in arms.get("with", []) if not r.get("error")]
            if len(wo) < 3: continue
            latest[c["name"]] = (ts,
                                 sum(r.get("score",0) for r in wo)/len(wo),
                                 sum(r.get("score",0) for r in wi)/len(wi) if wi else None,
                                 len(wo))
    return {k: v[1:] for k, v in latest.items()}

def parse_case(prompt_path):
    raw = prompt_path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    fm, body = (m.group(1), m.group(2).strip()) if m else ("", raw.strip())
    name = (re.search(r"^name:\s*(\S+)", fm, re.M) or [None, prompt_path.parent.name])[1]
    tags = re.search(r"^tags:\s*\[(.*?)\]", fm, re.M)
    tags = [t.strip() for t in tags.group(1).split(",")] if tags else []
    grader = prompt_path.parent / "graders" / "criteria.md"
    g = ""
    if grader.exists():
        g = re.sub(r"^---\n.*?\n---\n", "", grader.read_text(), flags=re.S).strip()
    return name, tags, body, g

def main():
    scores = baseline_scores()
    cases, by_plugin = [], defaultdict(list)
    for p in sorted(glob.glob(str(ROOT / "*/evals/*/prompt.md"))):
        pp = Path(p)
        plugin = pp.parents[2].name
        name, tags, body, grader = parse_case(pp)
        base, withskill, n = scores.get(name, (None, None, 0))
        cases.append({
            "id": name,
            "area": plugin,
            "tags": tags,
            "prompt": body,
            "correct_answer_criteria": grader,
            "measured": {
                "baseline_pass_rate": base,
                "with_reference_pass_rate": withskill,
                "runs_per_arm": n,
            } if n else None,
        })
        by_plugin[plugin].append(name)

    OUT.mkdir(exist_ok=True)
    (OUT / "eu-mdr-bench.json").write_text(json.dumps({
        "name": "eu-mdr-bench",
        "version": "0.1.0",
        "what_it_measures": ("Whether a model applies EU medical device regulation to "
                             "products, markets and audiences the cited provision does "
                             "not reach. Not knowledge -- boundary."),
        "license": "Apache-2.0",
        "source": "https://github.com/Ecgecer/eu-mdr-skills",
        "cases": cases,
    }, indent=2, ensure_ascii=False) + "\n")

    hard = sorted([c for c in cases if c["measured"] and c["measured"]["baseline_pass_rate"] == 0.0],
                  key=lambda c: c["id"])
    free = sorted([c for c in cases if c["measured"] and c["measured"]["baseline_pass_rate"] == 1.0],
                  key=lambda c: c["id"])
    unmeasured = [c for c in cases if not c["measured"]]

    lines = [
        "# eu-mdr-bench", "",
        "A benchmark for one question: **does your model apply EU medical device",
        "regulation to things the provision it cites does not reach?**", "",
        "Not a knowledge test. Every case here is one a competent model can reason about;",
        "what it measures is whether the model knows where the rule stops.", "",
        f"**{len(cases)} cases**, {len([c for c in cases if c['measured']])} with measured baseline "
        f"difficulty. Apache-2.0.",
        "Machine-readable in [`eu-mdr-bench.json`](eu-mdr-bench.json).", "",
        "## How to run it", "",
        "Each case has a `prompt` and a `correct_answer_criteria` written for an LLM judge.",
        "Send the prompt to the system under test with no other context, then score the",
        "response against the criteria. Three runs per case — single runs are not evidence,",
        "and two of these cases were mis-scored here for exactly that reason.", "",
        "`baseline_pass_rate` is what **Claude** scored with no reference material and no",
        "web access, three runs, measured rather than estimated.", "",
        "### One model has been tested", "",
        "Every number here comes from Claude, run through Claude Code 2.1.266/267 with an",
        "LLM judge. **GPT, Gemini, Llama, Mistral and everything else are untested.** Whether",
        "they share these failure modes is an open question, and this file deliberately does",
        "not guess — a benchmark that generalises from one model is doing the exact thing it",
        "measures.", "",
        "If you run it against another model, the results are welcome as a PR. The cases and",
        "criteria are model-agnostic by design; only the measured column is not.", "",
        f"## The hard cases — Claude scored 0.00 ({len(hard)})", "",
        "Claude failed every run of these with no reference material and no web access.",
        "Untested on other models:", "",
    ]
    WHAT = {
        "clean-copy-control": "clean copy — the model invents findings that are not there",
        "doc-english-sufficient": "tells a manufacturer to translate a DoC its member state accepts in English",
        "hwg11-item-scope": "cites a German advertising item that does not reach medical devices",
        "hwg11-wrong-audience": "applies a lay-audience rule to a gated professional audience",
        "hwg3a-arzneimittel-only": "applies a medicinal-product provision to a device",
        "ivdr-out-of-scope": "answers an IVD question from memory instead of declining",
        "limb-d-intended-purpose-drift": "a true claim that still breaches, and cannot be cured by evidence",
        "non-german-eu-market": "applies German national law to a French-market asset",
        "outside-carried-sections": "produces section numbers and deadlines it cannot verify",
        "puffery-restraint": "manufactures a finding on pure puffery",
        "rule-not-carried": "concludes confidently where the cited rule does not settle it",
        "uwg6-comparison": "mishandles comparative advertising that is lawful when compliant",
    }
    for c in hard:
        what = WHAT.get(c["id"], c["prompt"].splitlines()[0][:80])
        lines.append(f"- **`{c['id']}`** — {what}  \n  <sub>{c['area']}</sub>")
    lines += ["", f"## Cases a baseline already passes ({len(free)})", "",
              "Published because a benchmark that hides its easy cases overstates itself.",
              "These measure nothing about boundary discipline; a model gets them right unaided.", ""]
    for c in free:
        lines.append(f"- `{c['id']}` ({c['area']})")
    if unmeasured:
        lines += ["", f"## Not yet measured ({len(unmeasured)})", ""]
        for c in unmeasured:
            lines.append(f"- `{c['id']}` ({c['area']})")
    lines += [
        "", "## What the measurements showed", "",
        "Across five areas, Claude with no reference material already knew the law: it",
        "quoted MDR implementing rule 3.3 verbatim, applied Rule 11's escalations correctly,",
        "cited Regulation (EU) 2023/607 by number for the Article 120 deadlines, and got the",
        "suture carve-out right. **For this model, knowledge was never the gap.**", "",
        "Whether that holds for other models is untested. It is a plausible guess that a",
        "model with less European regulatory text in training would fail the knowledge cases",
        "too — in which case the reference files would earn more, not less. Nobody has",
        "measured it.", "",
        "What it got wrong, repeatedly, was reach — citing a German advertising provision",
        "against a device that provision does not cover, applying German law to a",
        "French-market asset, telling a manufacturer to translate a Declaration of",
        "Conformity that its member state accepts in English, and answering a question the",
        "rule it cited does not settle.", "",
        "Every one of those is plausible, well-reasoned and wrong in a way you cannot see",
        "from the answer. That is what this benchmark is for.", "",
        "## Provenance", "",
        "Cases and criteria are generated from the eval suites in the parent repo by",
        "`scripts/export-benchmark.py`. Every provision they turn on is stored verbatim",
        "with its source and retrieval date, and `scripts/verify-sources.py` re-fetches and",
        "diffs it. Errors found in these cases are logged in `../CORRECTIONS.md` rather",
        "than quietly fixed.", "",
    ]
    (OUT / "README.md").write_text("\n".join(lines) + "\n")
    print(f"  {len(cases)} cases exported")
    print(f"  hard (baseline 0.00): {len(hard)}   baseline already passes: {len(free)}   unmeasured: {len(unmeasured)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
