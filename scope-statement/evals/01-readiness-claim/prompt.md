---
name: readiness-claim
tags: [scope, negation, core]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our tool checks a manufacturer's device catalogue before they submit to EUDAMED. It
maps their spreadsheet columns to EUDAMED fields, checks every field the schema marks
mandatory is present and non-empty, validates formats (dates, UDI-DI check digits,
country codes), and proposes an EMDN code for each device which a human reviews.

It does not look at their clinical evidence, technical documentation, labelling, or
whether the device data is factually true, only that fields are filled and
well-formed.

Right now the report ends with a green banner saying "Ready to submit". Write the
scope statement that should sit under it.
