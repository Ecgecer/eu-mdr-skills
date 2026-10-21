"""Write every failed baseline run of the nine-run batch as a blind grading item.

Each item holds only the grader criteria and the response. The judge's verdict, the run
index and the arm are kept in a separate key file the blind grader never sees. Passing
runs are mixed in (one per case, chosen deterministically) so the grader cannot infer
that every item it sees is a failure.
"""
import json, sys, hashlib, random
from pathlib import Path

out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
key = {}
items = []
for f in sys.argv[2:]:
    d = json.load(open(f))
    for c in d["cases"]:
        criteria = c["graders"][0]["graderMarkdown"]
        prompt = c["promptMarkdown"]
        runs = c["arms"]["without"]
        passed = [i for i, r in enumerate(runs) if r["passed"]]
        chosen = [i for i, r in enumerate(runs) if not r["passed"]] + passed[:1]
        for i in chosen:
            r = runs[i]
            resp = r["graders"][0]["evidence"]
            iid = hashlib.sha256(f"{c['name']}|{i}|{resp[:200]}".encode()).hexdigest()[:10]
            items.append((iid, c["name"], prompt, criteria, resp))
            key[iid] = {"case": c["name"], "run": i + 1, "judge_passed": r["passed"],
                        "judge_votes": r["graders"][0].get("judgeVotes")}
random.Random(7).shuffle(items)
for iid, name, prompt, criteria, resp in items:
    (out / f"item-{iid}.md").write_text(
        f"# Item {iid}\n\n## The user's question\n\n{prompt}\n\n## Grading criteria\n\n{criteria}\n\n"
        f"## The response to grade\n\n{resp}\n")
(out.parent / "blind-key.json").write_text(json.dumps(key, indent=1))
print(len(items), "items written to", out)
