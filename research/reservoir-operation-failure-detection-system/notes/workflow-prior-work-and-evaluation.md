# Workflow Prior Work and Evaluation Design

- Project: reservoir-operation-failure-detection-system
- Stage: Planning
- Planning unit: workflow-level prior work and evaluation design
- Status: lightweight scan and evaluation design approved by user for formal Planning Review
- Date: 2026-07-03

## Why This Note Exists

An informal reviewer early-look pass found that the Planning package had strong
reservoir-demo feasibility work but weak support for the primary research
object: the human-AI interaction workflow. This note adds a first-pass
evaluation design and a light prior-work map. It is not a full novelty review.

## Workflow-Level Evaluation Design

The first study should make a limited claim: the workflow is feasible,
traceable, and human-reviewable on one public-data reservoir demo. It should
not claim that gates improve accuracy or decisions over an ungated workflow
unless a comparator experiment is explicitly added later.

| Workflow claim | Evidence to collect during Modeling/Reporting | Pass criterion | Falsification or downgrade condition |
|---|---|---|---|
| Traceability | Step packages, source manifests, gate decisions, reviewer findings, triage records | Each major decision has an artifact, owner, date, and evidence link | Decisions are made without recorded evidence or gate status |
| Reproducibility | Raw/clean data split, scripts/notebooks, fixed model search space, environment notes | A fresh rerun can reproduce the selected tables/figures/model metrics within documented tolerance | Outputs depend on manual hidden steps or untracked data |
| Human reviewability | Compact gate questions, explicit approval/revision/rejection choices, reviewer critique before major gate | A human can inspect the current state without reconstructing hidden reasoning | Gate package is too scattered, incomplete, or ambiguous for review |
| Claim support | Claim-to-source/model/limitation map in the final report | Every substantive report claim links to source data, model output, figure/table, or limitation | Report contains unsupported causal, operator-fault, or generalized workflow claims |
| Automation safety | Predeclared model candidates, metrics, validation split, and report limitations | Automated model selection cannot change labels, scope, metrics, or claim level without a human gate | Search space or metrics change after seeing results without recorded approval |

## Suggested Workflow Metrics

- artifact completeness rate: required artifacts present / required artifacts planned.
- gate resolution rate: approved, revised, rejected, deferred, or blocked decisions recorded / total decisions.
- reviewer-triage closure rate: fixed, deferred with reason, rejected with reason, or needs-user-decision / total findings.
- reproducibility check: pass/fail plus rerun differences for tables, figures, and metrics.
- claim-support audit: supported, limited, unsupported, or removed for each substantive report claim.
- decision latency: optional descriptive timing between gate package completion and gate decision.

## Prior-Work Map

This lightweight scan identifies adjacent bodies of work that should inform the
workflow design. Full citation verification and a broader novelty review remain
future Planning or Reporting work if the output becomes a manuscript.

| Area | Representative source | What it contributes | Gap for this project |
|---|---|---|---|
| Human-AI interaction guidelines | Amershi et al., "Guidelines for Human-AI Interaction" (CHI 2019), https://doi.org/10.1145/3290605.3300233 | Design principles for human control, feedback, uncertainty, and repair in AI systems | Not specific to agentic research workflows or reservoir modeling |
| AI risk governance | NIST AI Risk Management Framework 1.0, https://www.nist.gov/itl/ai-risk-management-framework | Govern, map, measure, and manage framing for risk-aware AI workflows | Governance framework, not an operational stage package for this domain |
| Tool-using reasoning agents | Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", https://arxiv.org/abs/2210.03629 | Reason/action loop for tool-using LLM agents | Does not by itself define human gates or reviewer ownership |
| Self-feedback and revision loops | Madaan et al., "Self-Refine: Iterative Refinement with Self-Feedback", https://arxiv.org/abs/2303.17651 | Iterative critique and revision pattern | Self-feedback alone is weaker than independent reviewer plus human gate |
| Verification against hallucination | Dhuliawala et al., "Chain-of-Verification Reduces Hallucination in Large Language Models", https://arxiv.org/abs/2309.11495 | Structured verification before final answers | Mainly model self-verification, not full source/provenance and user-gate workflow |
| Multi-agent LLM workflows | Wu et al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", https://arxiv.org/abs/2308.08155 | Multi-agent conversation, tools, and human input patterns | Needs project-specific stage artifacts, gates, and reviewer triage rules |
| LLM judging and reviewer limits | Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", https://arxiv.org/abs/2306.05685 | Evidence that LLM evaluators can be useful but imperfect | Supports reviewer-as-critique, not reviewer-as-approver |

## Planning Implications

- The workflow architecture should separate AI researcher, AI reviewer, human
  owner, and data/model tool responsibilities.
- The report should say "workflow feasibility on one demo" unless a broader
  multi-reservoir or comparator evaluation is approved.
- Model automation safety should be a method guardrail, not a hypothesis.
- The formal Planning Review request should ask the reviewer to assess whether
  these workflow-level evaluation criteria are enough for the intended claim.
