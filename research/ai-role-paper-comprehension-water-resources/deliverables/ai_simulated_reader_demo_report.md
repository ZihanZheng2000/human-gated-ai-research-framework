# AI-Simulated Reader Roles for Testing Water-Resources Paper Comprehension

## Executive Summary

This demo tested a small AI-native workflow for article comprehension
assessment. Four simulated reader roles read one open-access water-resources
article: undergraduate student, master's student, PhD student, and advisor. An
author/evaluator role generated ten comprehension questions, provided hints,
and scored answers before and after hints.

The demo shows a plausible pattern: lower-knowledge simulated roles started
with lower scores and improved more after hints, while higher-knowledge roles
started near ceiling and improved less.

This is a workflow feasibility result, not evidence about real human readers.

## Article Used

Van Loon, A. F. et al. (2016). "Drought in a human-modified world: reframing
drought definitions, understanding, and analysis approaches." Hydrology and
Earth System Sciences, 20, 3631-3650. DOI: 10.5194/hess-20-3631-2016.

Raw XML and PDF were acquired from the official HESS article page and preserved
under project artifacts.

## Experimental Design

The demo used:

- one article;
- four simulated reader roles;
- one author/evaluator role;
- ten comprehension questions from simple to expert-level;
- one hint round;
- a 0-4 component-based scoring rubric.

The workflow was:

```text
Article text
  -> author/evaluator creates question ladder and answer key
  -> simulated readers answer without hints
  -> author/evaluator scores answers
  -> author/evaluator provides hints
  -> simulated readers answer again
  -> author/evaluator scores again
  -> pre/post score comparison
```

## Results

| Role | Pre-hint score | Post-hint score | Change |
|---|---:|---:|---:|
| Undergraduate | 13 / 40 | 26 / 40 | +13 |
| Master's student | 23 / 40 | 33 / 40 | +10 |
| PhD student | 33 / 40 | 40 / 40 | +7 |
| Advisor | 37 / 40 | 40 / 40 | +3 |

The pattern is consistent with the planned hypothesis:

- simulated readers with lower knowledge profiles produced weaker initial
  answers;
- hints were associated with improved answer scores;
- lower-knowledge roles had more room to improve;
- higher-knowledge roles started near ceiling.

## What This Supports

This demo supports a limited claim:

> In a single-article AI-simulation demo, role prompts with different knowledge
> profiles produced different apparent comprehension scores, and author-style
> hints were associated with higher post-hint scores.

## What This Does Not Support

This demo does not support these stronger claims:

- real undergraduate, master's, PhD, and advisor readers would behave the same
  way;
- AI hints improve real human comprehension of water-resources papers;
- one paper represents the difficulty of water-resources journals;
- the role prompts are valid measures of actual knowledge level.

## Interpretation

The demo is useful because it exercises the full experimental loop: article
acquisition, question generation, role definition, pre/post answers, scoring,
and evidence packaging. It also exposes the main validity problem early: if the
same model session acts as author, reader, hint provider, and scorer, results
may partly reflect internal consistency and prompt expectations rather than
independent comprehension differences.

## Main Limitations

1. Single article only.
2. Simulated readers only.
3. Same-session generation and scoring.
4. No independent scorer.
5. No repeated runs to estimate variability.
6. No human-reader validation.
7. Reviewer-agent pass was skipped by user choice.

## Recommended Next Step

For a stronger next cycle, add one of these:

- independent scoring by another model or a human evaluator;
- repeated runs for each role;
- two to five water-resources articles with different difficulty levels;
- a small real-reader validation set.

For the current workflow, the appropriate next stage is Review if the user
approves this Reporting package.

