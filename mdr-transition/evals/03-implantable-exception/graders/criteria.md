---
type: llm
weight: 1
---

This is the exception-list trap. Art. 120(3a)(a) gives class IIb IMPLANTABLE devices
31 December 2027, "except sutures, staples, dental fillings, dental braces, tooth
crowns, screws, wedges, plates, wires, pins, clips and connectors". Sutures are named.
So this device falls to 3a(b) and gets **31 December 2028**, not 2027.

PASS requires:
(1) The stated deadline is **31 December 2028**.
(2) The reasoning names the exception. That sutures are excluded from the IIb implantable
    tier and therefore take the later date.

FAIL if the answer is 31 December 2027. That is what applying "class IIb implantable →
2027" without reading the exception produces, and it is the specific error this case
tests. FAIL also if it is 26 May 2024.
