# Hords Creek Route and Failure-Label Strategy

- Date: 2026-07-03
- Stage: Planning
- Planning unit: selected route, label strategy, and step-gate structure
- Status: approved for Planning route by user on 2026-07-03

## Scope Note

Hords Creek is a small public-data **test example** for the human-AI workflow.
It is not the main research object.

## Selected Reservoir Route

Selected reservoir: **Hords Creek Lake / Hords Creek Dam, Texas**.

Rationale:

- Small single-reservoir test case, more suitable for a first workflow demo than large
  systems such as Lake Mead, Oroville, Folsom, or Mendocino.
- ResOpsUS/USGS low-storage anomaly files include Hords Creek Dam as Dam_ID
  `1249`.
- TWDB and USGS provide public official data routes for Hords Creek storage and
  monitoring-location metadata.
- TWDB describes Hords Creek Lake as one of the smallest Corps projects in
  Texas, with flood control, water supply, and recreation purposes.

## Proposed Failure / Stress Definition

Use the initial term **low-storage operation stress** rather than "operation
failure" as the primary label.

Reason:

- A time-series model can detect and explain low-storage stress from storage,
  inflow/outflow, and climate context.
- It cannot by itself prove operator fault, infrastructure fault, or management
  failure.
- The report can still identify likely reasons for the stress, such as
  prolonged low storage, low inflow, continued outflow, drought context, or
  rule/threshold conflict, as long as each reason is tied to data or official
  documentation.

## Primary Label Candidate

Primary label: **USGS low-storage anomaly, 10th-percentile threshold**, for
Hords Creek Dam / ResOpsUS Dam_ID `1249`.

User status: approved by user on 2026-07-03 as the starting problem label.

Why this threshold:

- It is intuitive enough for a prototype.
- It is not as extreme or sparse as a 5th-percentile threshold.
- It is less broad than 20th or 30th percentile thresholds.
- It creates multiple event windows for training, testing, and explanation.

Candidate Hords Creek events from the USGS planning-screening file
`reservoir_1981_2020_weibull_jd_drought_properties.csv`:

| Threshold | Start | End | Duration days | Notes |
|---|---|---|---:|---|
| 10 | 1983-12-21 | 1986-06-04 | 897 | longest event; useful historical reference |
| 10 | 2011-09-30 | 2012-02-17 | 141 | recommended first demo event |
| 10 | 2012-06-04 | 2012-09-28 | 117 | useful nearby continuation/check |
| 10 | 2014-02-18 | 2014-05-24 | 96 | additional validation event |
| 10 | 2003-07-16 | 2003-10-08 | 85 | additional validation event |

Recommended first demo event: **2011-09-30 to 2012-02-17**.

User status: approved by user on 2026-07-03 as the first demo event.

Reason:

- It is long enough to inspect and model.
- It is more modern than the 1983-1986 event.
- It sits within the Texas drought period and can likely be contextualized with
  public drought/precipitation data if needed.
- The longer 1983-1986 event can be kept as historical reference or robustness
  material rather than forcing the first demo to explain a very long episode.

## Source Strategy

| Source role | Proposed source | Use in workflow | Status |
|---|---|---|---|
| standardized reservoir operations data | ResOpsUS Version 2 and USGS low-storage anomaly release | storage/inflow/outflow where available; anomaly windows and thresholds | candidate, not yet Modeling-acquired |
| official storage and level data | Water Data for Texas Hords Creek CSV and page | storage, conservation storage, percent full, conservation capacity, period of record | source endpoint verified |
| official monitoring location metadata | USGS monitoring location `USGS-08141000` | site type, location, drainage area, vertical datum, cooperating agency | source endpoint verified |
| official reservoir context | TWDB Hords Creek Lake page and USACE materials | project purposes, capacity, conservation pool, flood pool, drainage area, operating context | source page verified |
| auxiliary explanatory context | drought/precipitation data, if selected later | support diagnosis of low inflow/drought context | deferred until method route |

## Proposed System Steps and Human Gates

Each step ends with a human gate. In Modeling, each gate can be represented as a
checkpoint in the model package rather than a separate workflow stage.

User status: accepted by user on 2026-07-03 as a suitable 10-step structure.

| Step | System action | Human gate question | Pass condition |
|---|---|---|---|
| 1. Source and reservoir setup | Lock Hords Creek route, source list, and data access rules | Is this reservoir/source scope acceptable? | selected reservoir and source roles approved |
| 2. Data acquisition | Download/query raw data and preserve raw files separately | Did the system acquire the right public data? | required variables exist and provenance is recorded |
| 3. Failure-label setup | Apply USGS low-storage anomaly label and selected event window | Is this stress/failure definition acceptable? | label definition and event window approved |
| 4. Preflight and data quality | Check date coverage, missingness, units, duplicates, and suspicious values | Is the data good enough to model? | quality issues are resolved or accepted |
| 5. Baseline detection | Run simple threshold, seasonal percentile, and persistence checks | Does the baseline detect the known stress windows? | baseline performance and false positives are inspectable |
| 6. Driver diagnosis | Attribute stress to candidate drivers: low inflow, storage decline, outflow persistence, drought/precip context | Are the explanations evidence-bound and not overclaimed? | diagnosis uses only supported drivers |
| 7. Automated model build | Try a bounded set of simple time-series/anomaly models | Is auto-model selection constrained and reproducible? | best model is selected by approved metrics, not by narrative fit |
| 8. Validation | Test on held-out years/events and compare against baseline | Is the model reliable enough for the intended claim? | validation passes or limitations are accepted |
| 9. Report generation | Produce a diagnostic report with causes, confidence, recommended response, and caveats | Is the report clear and useful? | claims map to evidence and limitations |
| 10. Final review | Run reviewer critique and user gate | Is the package ready to archive, share, or iterate? | routed issues are fixed, deferred, or accepted |

## Decisions Needed

1. Primary label: approved by user on 2026-07-03.
2. First demo event: approved by user on 2026-07-03.
3. Initial wording: "low-storage operation stress" approved by implication with
   the label/event approval on 2026-07-03; use stronger "operation failure"
   wording only where evidence supports it.
4. System step structure: accepted by user on 2026-07-03.
