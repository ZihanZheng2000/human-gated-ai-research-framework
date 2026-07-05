# Hords Creek Method Route Proposal

- Project: reservoir-operation-failure-detection-system
- Planning unit: demo method route for the first Hords Creek test fixture
- Status: supporting note; not the main research object
- Date: 2026-07-03

## Scope Note

The primary project is the human-AI interaction workflow. Hords Creek is only a
bounded test fixture used to exercise the workflow on public reservoir data.

## Approved Starting Point

The first demo fixture is Hords Creek Lake / Hords Creek Dam, Texas, framed as
**low-storage operation stress**. The approved label is the USGS
10th-percentile low-storage anomaly for Hords Creek Dam / Dam_ID `1249`. The
approved first demo event is **2011-09-30 to 2012-02-17**.

## Proposed Modeling Route

1. Search and extract official/documented evidence explaining the 2011-2012
   low-storage context: drought, heat, evaporation/runoff, municipal demand,
   curtailment, drought-stage triggers, and conservation/infrastructure issues.
2. Build a document-coded causal hypothesis table before time-series modeling.
   Each candidate cause must have a document source and a proposed time-series
   proxy.
3. Acquire selected-reservoir daily time series from ResOpsUS/USGS low-storage
   files and cross-check with TWDB Hords Creek CSV.
4. Build the reservoir-day table with storage and any available inflow,
   outflow/release, elevation, evaporation, and percent-full variables.
5. Add climate/demand/context variables only when they are source-backed:
   precipitation, temperature, drought category, evaporation, inflow or
   streamflow proxy, withdrawals/releases, and drought-stage indicators.
6. Create event labels from the approved USGS threshold-10 anomaly window.
   Keep a buffer around event boundaries so transition days are not treated as
   clean normal examples.
7. Run a transparent baseline first: seasonal storage percentile, persistence
   below threshold, and storage drawdown-rate checks.
8. Test the documented cause hypotheses with time-series evidence: storage
   decline, inflow deficit, release/withdrawal persistence, evaporation
   pressure, and drought or precipitation context.
9. Classify observed outflows/withdrawals into mandatory, controllable,
   hedgeable, reducible loss, or unknown categories. This answers which water
   could plausibly have been stored.
10. Formulate a hedging / operation optimization problem with approved
   objective, constraints, and foresight assumptions.
11. Design loss-reduction/mitigation scenarios from documents, such as earlier
   demand-reduction triggers, 10/20/30% demand cuts, reduced system loss,
   hedging rules that preserve carryover storage, and a hydrologic-normal
   attribution counterfactual.
12. Run scenario/optimization modeling to estimate reduction in storage loss,
   shortage cost, low-storage duration, low-storage intensity, and threshold
   crossing timing.
13. Run bounded automated model selection after the baseline, document-driven
   diagnosis, and hedging formulation: simple logistic
   regression or tree-based classifier, plus a simple anomaly detector only if
   labels are too sparse for supervised learning.
14. Validate against USGS low-storage labels with reservoir-day and event-level
   metrics: precision, recall, F1, event hit/miss, false alarm windows, and
   lead/lag around event boundaries.
15. Generate an evidence-bound report: detected stress, documented and
   data-supported contributors, hedgeable water classification,
   loss-reduction/mitigation optimization results, model confidence, recommended
   operational review actions, and caveats.

## Proposed Human Gates Inside Modeling

| Modeling step | Human gate question | Must be true before continuing |
|---|---|---|
| document evidence | Are the documents sufficient to define candidate causes and possible response actions? | each candidate cause has a source and claim boundary |
| causal hypothesis setup | Are the cause hypotheses and time-series proxies acceptable? | no cause is modeled without a document/data route |
| data acquisition | Do the acquired files match the approved reservoir, period, variables, and licenses? | raw and cleaned data are separate and provenance is recorded |
| label setup | Is the threshold-10 label acceptable as the event definition for this demo? | label dates match the approved USGS event and ambiguity is documented |
| baseline detection | Is the transparent baseline good enough to compare against auto models? | baseline outputs are reproducible and interpretable |
| diagnosis features | Are the proposed explanatory variables source-backed? | no unsupported causal or operator-fault claim is introduced |
| release classification | Which water was mandatory, controllable, hedgeable, reducible loss, or unknown? | loss reduction is not claimed for mandatory or unknown outflows |
| hedging optimization formulation | Are objective, constraints, hedging policy, and foresight assumptions acceptable? | optimization is predeclared before scenario scoring |
| loss-reduction scenario design | Are the mitigation/counterfactual scenarios realistic and evidence-bound? | scenarios come from drought plans, conservation plans, or clearly labeled hydrologic attribution tests |
| loss-reduction scenario results | How much do tested actions reduce storage loss, shortage cost, duration, intensity, or threshold-crossing timing? | outcome labels are tied to predeclared loss metrics |
| auto model build | Are candidate models constrained and reproducible? | model search space and metrics are fixed before scoring |
| validation | Are results sufficient for the intended feasibility claim? | metrics and failure cases are reported, not hidden |
| report generation | Is the report ready to present as a limited prototype result? | claims map to data, figures, and limitations |

## Proposed Acceptance Criteria For Modeling

- The Hords Creek daily storage series is usable across the approved 2011-2012
  event plus enough baseline years for seasonal comparison.
- The approved USGS low-storage label can be reproduced or joined to the
  reservoir-day table.
- Documented candidate causes are extracted before time-series modeling begins.
- Each modeled driver has both document support and a data proxy, or is marked
  as untestable.
- The baseline flags the approved event with an interpretable rule.
- Outflows/withdrawals are classified before loss-reduction modeling.
- The hedging optimization objective, constraints, and information assumptions
  are approved before scenario scoring.
- Loss-reduction scenarios are predeclared and scored against storage-loss,
  shortage-cost, duration, intensity, and threshold-crossing metrics.
- Any automated model is compared against the baseline and validated on years or
  events not used to tune it.
- The diagnosis section uses terms such as "likely contributor" unless official
  evidence supports stronger causal wording.

## Current Decision Needed

Use this method route as the demo implementation path only after the
workflow architecture is approved.
