---
type: llm
weight: 1
---

MDR Annex VI, Part C, Sections 6.5.2 and 6.5.3, verbatim (Regulation (EU) 2017/745, OJ
L 117, 5.5.2017, retrieved from EUR-Lex 2026-10-18):

> 6.5.2. A new UDI-DI shall be required whenever there is a modification that changes:
> (a) the original performance; (b) the safety or the intended use of the software;
> (c) interpretation of data. Such modifications include new or modified algorithms,
> database structures, operating platform, architecture or new user interfaces or new
> channels for interoperability.
>
> 6.5.3. Minor software revisions shall require a new UDI-PI and not a new UDI-DI.
> Minor software revisions are generally associated with bug fixes, usability
> enhancements that are not for safety purposes, security patches or operating
> efficiency. [...]

PASS requires:
(1) 4.2.1, security patch plus bug fixes: new UDI-PI, not a new UDI-DI, and
(2) 4.3, retrained model with changed sensitivity: new UDI-DI. It changes the original
    performance and is a modified algorithm. Being an improvement does not make it
    minor; the dev lead's reasoning must be rejected.

Noting that whether 4.3 is also a significant change for conformity-assessment
purposes is a separate question PASSES. Discussing the Basic UDI-DI is not required.

FAIL if 4.3 is treated as a minor revision (UDI-PI only). FAIL if 4.2.1 is said to need
a new UDI-DI.

This case is expected to measure 1.00 unaided on frontier models. It is here to find
out, per ROADMAP: a knowledge case that measures zero delta is the expected result.
