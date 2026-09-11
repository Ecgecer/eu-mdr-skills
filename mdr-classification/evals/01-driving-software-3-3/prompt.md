---
name: driving-software-3-3
tags: [implementing-rule-3.3, trap, detection]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

What MDR class is our software?

It's a control application that runs on a tablet and sets the infusion rate on our
own infusion pump. The pump is a Class III device. The app doesn't diagnose anything
it just lets the clinician set and adjust the rate, and it shows the current rate.
Intended purpose: "to set and adjust the delivery rate of the [X] infusion pump under
clinician control."
