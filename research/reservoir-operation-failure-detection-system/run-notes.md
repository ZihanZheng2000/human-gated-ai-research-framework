# Example Run Notes

## Run Identity

- Run name: reservoir-operation-failure-detection-system
- Date: 2026-07-03
- Mode: real project
- Gate mode: real user gates
- Topic or task: Human-gated reservoir operation failure detection, diagnosis, model building, and reporting system
- Stage coverage: Planning in progress

## Useful Observations

- Observation: The user clarified that ResOpsUS is a public dataset and should be considered.
- Stage: Planning
- Why it helped: It gives a standardized time-series starting point while preserving official operator data as validation/provenance.
- Evidence or example from this run: USGS catalog and Zenodo pages identify ResOpsUS as public daily reservoir operations data.
- Possible permanent home: project planning package

- Observation: The first candidate set was too operationally complex for the user's intended prototype.
- Stage: Planning
- Why it helped: It forced the candidate scan toward small, single-reservoir low-storage cases rather than famous multi-purpose emergency systems.
- Evidence or example from this run: Hords Creek Lake has USGS low-storage anomaly events, TWDB public storage data, and USACE/TWDB official reservoir context.
- Possible permanent home: project planning package

- Observation: The user approved Hords Creek Lake / Hords Creek Dam as the starter problem with the USGS 10th-percentile low-storage label and the 2011-09-30 to 2012-02-17 demo event.
- Stage: Planning
- Why it helped: It fixes the first target event and keeps the Planning route small enough for a transparent prototype.
- Evidence or example from this run: The Planning package now records the label/event as confirmed for the initial study.
- Possible permanent home: project planning package

- Observation: The user clarified that the main project is a human-AI interaction workflow, and the reservoir is only a test example.
- Stage: Planning
- Why it helped: It prevents the Planning package from becoming a single-reservoir case study instead of a reusable gated workflow design.
- Evidence or example from this run: A separate workflow architecture note was added and the Hords Creek method note was demoted to a demo support note.
- Possible permanent home: project planning package

- Observation: An informal reviewer early-look pass found that workflow-level evaluation and prior-work support were weaker than reservoir-demo support.
- Stage: Planning
- Why it helped: It forced the package to define how workflow feasibility, traceability, reproducibility, and claim safety will be assessed.
- Evidence or example from this run: Added `notes/workflow-prior-work-and-evaluation.md` and `notes/informal-reviewer-early-look-triage.md`.
- Possible permanent home: project planning package

- Observation: User approved the revised workflow architecture and workflow-level evaluation design for formal Planning Review.
- Stage: Planning
- Why it helped: It allows the researcher to finalize the Planning package and issue the formal reviewer request without treating the Planning Gate as approved.
- Evidence or example from this run: `artifacts/reservoir-failure-plan-2026-07-03/review-request.md` was prepared for Claude Code.
- Possible permanent home: project planning package

- Observation: User corrected the Modeling route: cause analysis must come from documents before time-series modeling, and the hedging model should focus on reducing shortage/storage losses rather than proving the low-storage situation could be fully avoided.
- Stage: Planning
- Why it helped: It prevents the workflow from treating ML diagnosis as a substitute for documented hydrologic/operational explanation.
- Evidence or example from this run: Added `notes/document-driven-cause-and-loss-reduction-route.md` and inserted document evidence, causal hypothesis, hedging optimization, and loss-reduction gates into the Modeling route.
- Possible permanent home: project planning package

- Observation: User identified demand and shortage/loss as the make-or-break feasibility issue for hedging.
- Stage: Planning
- Why it helped: The hedging literature shows that demand, loss/benefit, and controllability are structural inputs, not optional refinements.
- Evidence or example from this run: Added `notes/hedging-literature-demand-loss-review.md`, tightened `notes/hedging-data-sufficiency-check.md`, and added a Demand-Loss Gate to the Planning package and review request.
- Possible permanent home: project planning package

## Friction or Failures

- Issue: "Reservoir operation failure" can mean drought stress, flood-operation stress, infrastructure/spillway failure, or rule/target deviation.
- Stage: Planning
- What happened: Candidate reservoirs differ sharply by failure type and modeling difficulty.
- Root cause, if known: The project goal combines operational diagnosis, anomaly detection, and automated model selection.
- Fix used during this run: Break Planning into a candidate reservoir/source-selection unit before committing to a method route.
- Should this become a formal rule? unsure

- Issue: Famous reservoir examples such as Lake Mead, Oroville, Folsom, and Mendocino are data-rich but too complex for a first prototype.
- Stage: Planning
- What happened: The user asked for simpler reservoirs after seeing the first shortlist.
- Root cause, if known: Initial scan prioritized documentation strength over operational simplicity.
- Fix used during this run: Added a second scan using USGS low-storage anomaly metrics and metadata to identify smaller reservoirs with simpler stress definitions.
- Should this become a formal rule? yes

## Candidate Formal Updates

| Candidate update | Target file | Reason | Evidence from this example | Decision |
|---|---|---|---|---|
| none yet |  |  |  | keep in example |
