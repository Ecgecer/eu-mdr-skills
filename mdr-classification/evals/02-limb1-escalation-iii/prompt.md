---
name: limb1-escalation-iii
tags: [rule-11, limb-1, escalation, detection]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Classify this under MDR please.

Standalone software, no connection to any other device. It analyses CT angiography
images and flags suspected large-vessel occlusion strokes, and the output is used by
the on-call neurointerventionalist to decide whether to take the patient straight to
thrombectomy or not. Intended purpose: "to provide triage information to support the
decision to proceed to mechanical thrombectomy in suspected acute ischaemic stroke."
