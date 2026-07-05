# Run Summary

## What This Modeling Run Did

This run executed a single-article AI-simulated reader comprehension demo using
Van Loon et al. (2016), "Drought in a human-modified world."

The run created four simulated reader roles:

- undergraduate student
- master's student
- PhD student
- advisor / senior researcher

It also created one author/evaluator role grounded in the article text. The
author/evaluator generated 10 easy-to-hard comprehension questions, hints, and
a 0-4 scoring rubric. Simulated readers answered before and after hints.

## Main Result

| Role | Pre-hint total | Post-hint total | Delta |
|---|---:|---:|---:|
| Undergraduate | 13 / 40 | 26 / 40 | +13 |
| Master's student | 23 / 40 | 33 / 40 | +10 |
| PhD student | 33 / 40 | 40 / 40 | +7 |
| Advisor | 37 / 40 | 40 / 40 | +3 |

## Interpretation

Within this AI-simulation demo, the role prompts produced a plausible gradient:
lower-knowledge roles scored lower before hints and improved more after hints,
while higher-knowledge roles started high and improved less.

## Limits

This is generated simulation evidence, not human-subject evidence. The same
Codex session produced roles, questions, answers, hints, and scoring, so model
self-consistency and evaluator bias are major limitations. The result should be
reported as a feasibility demo only.

