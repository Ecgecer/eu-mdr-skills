---
type: llm
weight: 1
---

The question assumes an STK obligation exists and asks only about its length —
"confirm the interval", "can we stretch it". The trap is answering the second
question without testing the first.

Sicherheitstechnische Kontrollen under MPBetreibV do not reach every device. The
obligation attaches to the device categories listed in the regulation's Anlage,
plus devices for which the manufacturer has prescribed a check. Whether this
particular monitor is caught is exactly what has to be established before an
interval means anything.

PASS requires the response to establish whether STK applies before giving an
interval. Any of these PASS:
  - stating that STK reaches listed categories and asking whether this device is
    in one;
  - stating that the obligation can also arise from the manufacturer's own
    prescribed interval, and that "the manual is silent" is therefore load-bearing
    rather than an invitation to pick a number;
  - concluding, with reasoning, that a monitor of this description is not caught
    and saying what would change that.

It is not required to reach a particular legal conclusion, and a response that
says it cannot tell without the Anlage text in front of it PASSES. This measures
whether the boundary is tested, not whether the model knows the list.

FAIL if the response supplies an interval for these monitors without establishing
that STK reaches them — including a confident "every two years" — or treats STK
as a universal duty of operating any medical device.

Note for the judge: the second half of the question, about stretching the
interval, is bait. Answering it thoroughly while never testing whether the duty
exists is the failure, not a mitigation of it.
