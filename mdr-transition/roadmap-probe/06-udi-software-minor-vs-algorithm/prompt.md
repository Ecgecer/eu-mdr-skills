---
name: udi-software-minor-vs-algorithm
tags: [udi, annex-vi-part-c-6.5, detection]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our standalone software device (MDR Class IIa) already has a UDI-DI. Two releases are
coming:

- 4.2.1: a security patch plus fixes for two crash bugs.
- 4.3: the detection model is retrained on new data. Sensitivity goes from 91% to 94%.
  No change to the intended purpose or the user interface.

Which of these need a new UDI-DI, and which only a new UDI-PI? Our dev lead says 4.3 is
minor too, because it is an improvement and the intended use has not changed.
