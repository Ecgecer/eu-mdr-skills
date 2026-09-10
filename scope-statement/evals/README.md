# Evals — scope statement

Three cases, measured with `--ablation with-without`, 3 runs per case per arm,
2026-09-10.

| Case | with | without | delta | what it tests |
|---|---|---|---|---|
| `unpinned-basis` | 1.00 | 0.33 | **+0.67** | asking instead of inventing an authority |
| `no-disclaimer` | 1.00 | 0.67 | **+0.33** | describing coverage instead of boilerplate |
| `readiness-claim` | 1.00 | 1.00 | 0.00 | writing the block when fully briefed |

**Mean delta +0.33.**

## The zero is the informative one

`readiness-claim` hands the model everything: what the tool checks, what it explicitly
does not, and the claim being made. Given that, the baseline writes a good scope
statement on its own — it names the presence-versus-correctness gap and negates the
compliance inference without being told to. Delta 0.00.

The two that earn are the ones where the model has to **decline** something.

`unpinned-basis` says only "validates against the current regulatory requirements". The
correct move is to ask which rule set and which version, because pinning the authority
is the entire point of the block. The baseline instead produced a finished, confident
scope statement built on invented specifics in 2 of 3 runs.

`no-disclaimer` asks for something short. The baseline used brevity as licence to fall
back on "for informational purposes only" — which protects the author and tells the
reader nothing about what was checked.

## Same shape, third domain

This suite is not about medical devices at all, which makes it the cleanest test of
whether the finding generalises. It does.

| Suite | Cases | Mean delta | Positive | Zero |
|---|---|---|---|---|
| Claims (MDR/IVDR Art. 7, HWG, UWG) | 10 | +0.47 | 7 | 3 |
| Classification (Annex VIII) | 7 | +0.29 | 2 | 5 |
| Scope statement (domain-general) | 3 | +0.33 | 2 | 1 |
| **Total** | **20** | | **11** | **9** |

Across 20 cases in three domains, without exception:

> **Positive delta wherever the model would over-apply, over-conclude, invent an
> authority, or reach for boilerplate. Zero wherever it already has what it needs and
> only has to use it.**

The skills do not add knowledge. They add the discipline to stop.
