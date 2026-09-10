---
name: no-disclaimer
tags: [scope, restraint, anti-boilerplate]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We run an automated check that scans a customer's uploaded device spreadsheet for
personal data — names, emails, phone numbers, national ID patterns — and flags any
cell that matches, so they can strip it before the file goes anywhere. It uses regex
patterns plus a name dictionary. It runs on the uploaded file only, at upload time.

Give me the scope statement. Keep it short — it goes in a narrow sidebar.
