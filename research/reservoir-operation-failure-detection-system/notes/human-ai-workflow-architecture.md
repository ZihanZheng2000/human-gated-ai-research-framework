# Human-AI Workflow Architecture Proposal

- Project: reservoir-operation-failure-detection-system
- Planning unit: workflow architecture
- Status: approved by user for formal Planning Review
- Date: 2026-07-03

## Scope Correction

The main project is a **human-AI interaction workflow** for reservoir
operation-stress/failure analysis. The reservoir is not the main research
object. Hords Creek Lake / Hords Creek Dam is the first small public-data test
example used to exercise the workflow.

## Core Workflow Roles

| Role | Responsibility | Cannot do alone |
|---|---|---|
| Human owner | Sets problem scope, approves labels, accepts risks, decides whether gates pass | Cannot silently skip evidence or reviewer gates |
| AI researcher | Finds sources, drafts artifacts, builds data/model/report outputs, proposes next steps | Cannot approve gates or strengthen claims without evidence |
| AI reviewer | Critiques each stage package and flags blockers, risks, and unsupported claims | Cannot own the package or approve gates |
| Data/model tools | Retrieve data, run checks, fit bounded models, produce metrics and figures | Cannot decide meaning, causality, or release readiness |

## Proposed Human-AI Interaction Loop

1. AI researcher proposes a compact next-step package.
2. Human approves, revises, or rejects the proposed step.
3. AI researcher executes only the approved scope.
4. AI researcher records evidence, limitations, and open decisions.
5. AI reviewer critiques the package before a major stage gate.
6. AI researcher triages reviewer findings.
7. Human makes the gate decision.

## Proposed System Steps

| Step | AI researcher action | Human gate | Reviewer role |
|---|---|---|---|
| 1. Problem framing | Propose failure/stress type, claim level, and demo fixture | Approve scope and wording | Check whether scope is too broad or underspecified |
| 2. Source strategy | Identify public raw data, documentation, labels, and licenses | Approve source route | Check whether candidate links are mistaken for data |
| 3. Label/event setup | Define failure/stress labels and ambiguity rules | Approve label semantics | Check overclaiming and label leakage |
| 4. Document cause analysis | Extract documented causes, response rules, and possible interventions | Approve cause hypotheses before modeling | Check whether causes are source-backed |
| 5. Data acquisition | Retrieve raw data, preserve provenance, create cleaned table | Approve acquired data and exclusions | Check source identity and data quality |
| 6. Preflight checks | Audit missingness, units, time coverage, joins, and anomalies | Approve whether data are usable | Check whether evidence is sufficient to proceed |
| 7. Detection baseline | Run transparent baseline rules before auto modeling | Approve baseline interpretability | Check reproducibility and baseline fairness |
| 8. Time-series diagnosis | Test document-derived candidate drivers against data | Approve explanation boundaries | Check unsupported causal claims |
| 9. Loss-reduction scenarios | Test how much approved interventions reduce storage loss, shortage cost, duration, intensity, or threshold-crossing timing | Approve scenario realism and claim wording | Check counterfactual overclaiming |
| 10. Automated model build | Run bounded model selection with fixed metrics | Approve model search space and metric priorities | Check leakage, overfitting, and hidden tuning |
| 11. Report generation | Produce evidence-linked findings and recommended actions | Approve report claim level | Check claim-source alignment |
| 12. Final review/archive | Package artifacts, review findings, and gate decisions | Approve release, iterate, or terminate | Check unresolved blockers |

## Hords Creek Test Fixture

Hords Creek is used only to test whether the workflow can run end to end on a
simple public-data case. The approved demo label is the USGS 10th-percentile
low-storage anomaly for Hords Creek Dam / Dam_ID `1249`, with first demo event
2011-09-30 to 2012-02-17.

## Workflow Evaluation

The first evaluation should measure whether the workflow is feasible,
traceable, reproducible, human-reviewable, and claim-safe on the Hords Creek
demo. It should not claim superiority over an ungated workflow unless a
comparator evaluation is approved later. Detailed criteria are recorded in
`workflow-prior-work-and-evaluation.md`.

## Planning Decision Needed

Approved by user on 2026-07-03 for formal Planning Review.
