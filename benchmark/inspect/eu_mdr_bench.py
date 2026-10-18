"""eu-mdr-bench as an inspect_ai task.

    pip install inspect-ai
    inspect eval benchmark/inspect/eu_mdr_bench.py --model google/<id> \
        --model-role grader=anthropic/claude-opus-5-5

    # only the cases Claude failed in every run, the ones that discriminate
    inspect eval benchmark/inspect/eu_mdr_bench.py -T hard_only=true --model ...

Same cases, same criteria and same three runs per case as scripts/run-benchmark.py,
for anyone who already runs evals in inspect. The rules that make a number here
comparable to the published Claude column are the same too:

  - No tools and no retrieval. The task gives the model none; do not add any.
  - The grader is not the model under test. Pass a different model as the grader role.
  - Three epochs, averaged. A single run is not evidence.
  - Results are reported per axis (boundary / detection) as well as overall, because
    the two move in opposite directions across models (MODELS.md).

Where a case's criteria assume the skill's output format, the grader is told to judge
the substance only, as scripts/judge-benchmark.py does.
"""
import json
from pathlib import Path

from inspect_ai import Epochs, Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.scorer import accuracy, grouped, model_graded_qa, stderr
from inspect_ai.solver import generate

BENCH = Path(__file__).resolve().parent.parent / "eu-mdr-bench.json"

FORMAT_NOTE = (
    "\n\nNote for the grader: these criteria were written for a model that had the "
    "skill loaded, and some PASS conditions name its output format (a '## Limits' "
    "block, 'Ready to publish', 'Breach:' / 'Call:' / 'Also engaged:' fields, or "
    "SKILL.md). The submission was not shown that format. Ignore every format "
    "requirement and judge only the substance.")

INSTRUCTIONS = (
    "The criteria were written before this submission existed. Apply them as written: "
    "do not substitute your own view of the law, and do not reward thoroughness, "
    "formatting or confidence the criteria do not ask for. Where the criteria quote "
    "statute text, treat that text as authoritative. A PASS under the criteria is "
    "GRADE: C, a FAIL is GRADE: I. Explain which condition decided it in one to three "
    "sentences, then end with the grade line, exactly 'GRADE: C' or 'GRADE: I'.")


@task
def eu_mdr_bench(hard_only: bool = False, area: str | None = None):
    cases = json.loads(BENCH.read_text())["cases"]
    if hard_only:
        cases = [c for c in cases
                 if (c.get("measured") or {}).get("baseline_pass_rate") == 0.0]
    if area:
        cases = [c for c in cases if c["area"] == area]
    samples = [
        Sample(
            id=c["id"],
            input=c["prompt"],
            target=c["correct_answer_criteria"]
            + (FORMAT_NOTE if c.get("criteria_assume_skill_format") else ""),
            metadata={"area": c["area"], "axis": c.get("axis"), "tags": c.get("tags"),
                      "claude_baseline_pass_rate":
                          (c.get("measured") or {}).get("baseline_pass_rate")},
        )
        for c in cases
    ]
    return Task(
        dataset=MemoryDataset(samples, name="eu-mdr-bench"),
        solver=generate(),
        scorer=model_graded_qa(instructions=INSTRUCTIONS, model_role="grader"),
        metrics=[accuracy(), stderr(), grouped(accuracy(), "axis", all=False),
                 grouped(accuracy(), "area", all=False)],
        epochs=Epochs(3, "mean"),
    )
