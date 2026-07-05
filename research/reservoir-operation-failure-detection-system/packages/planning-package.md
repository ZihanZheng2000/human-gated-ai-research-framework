# Approved Plan Package

## Planning Workflow Identity

- package status: ready for formal Planning Review after demand-loss update
- Planning Researcher: Codex
- Planning Reviewer: Claude Code
- reviewer file: `docs/reviewer-agents/planning-reviewer-agent.md`
- reviewer mode: critique-only
- Planning Review status: formal review request written
- researcher-agent response status: pending formal reviewer critique
- user Planning Gate status: pending
- workflow mode: step-by-step discussion
- reviewer strategy: use reviewer
- gate mode: real user gates
- run id: reservoir-failure-plan-2026-07-03

## User-Need Profile

| User-need field | Proposed answer | Common choices | User correction or addition |
|---|---|---|---|
| research area | Reservoir operations, hydrologic time-series modeling, AI-assisted diagnostic workflows | water resources / AI systems / decision support | confirmed as reservoir operation failure detection and diagnosis |
| intended output | Human-AI interaction workflow design plus a small reservoir demo/test package | paper / report / demo / skill / dataset / tool / manuscript package / proposal / policy note / internal decision brief | user clarified the workflow/system is primary and the reservoir is only a test example |
| workflow mode | step-by-step discussion | auto-until-needed / step-by-step discussion | confirmed |
| intended research product | Human-gated AI workflow for reservoir operation-stress detection, diagnosis, model building, reviewer critique, and reporting | empirical finding / method / dataset / benchmark / skill / workflow demo / manuscript package | confirmed as primary object |
| research purpose | Design and test a human-AI workflow that can guide reservoir failure/stress detection from source selection through final report | discover pattern / build method or tool / validate intervention / compare alternatives / workflow test | confirmed |
| practical success criterion | The workflow produces traceable stage artifacts, human gates, reviewer critiques, and a bounded demo result from public time-series data | evidence for a claim / reusable workflow / validated dataset / decision support / proof of feasibility | approved for Planning Review |
| target audience or venue | reservoir researchers, water-resource modelers, reservoir operators, and technical reviewers | academic readers / internal decision-makers / policy users / engineering users / domain experts | provisional |
| data/source direction | Public ResOpsUS dataset plus official operator/public-agency data for the demo reservoir validation and event documentation | provided data / public data / API data / literature only | user clarified ResOpsUS is public; public official data should be found |
| available data | ResOpsUS public dataset candidate; official reservoir sources to be checked before Modeling | none known / user-provided / public source known / to be found | ResOpsUS should be included |
| constraints | Public data only; no silent reservoir/dataset/failure-definition assumptions; human gate after each step | time / tooling / runtime / privacy / licensing / method complexity | confirmed |
| novelty expectation | Prototype/feasibility first; stronger claims only after validation | publication novelty / useful replication / demo / internal evidence | provisional |
| avoid-list | Avoid private data, paid APIs, opaque automatic decisions, and unsupported claims about failure cause | avoid specific data / methods / paid APIs / private data / black-box methods | confirmed |
| gate mode | real user gates | real user gates / synthetic gates / mixed | confirmed |
| reviewer strategy | use reviewer | use reviewer / skip reviewer | confirmed |

## Domain Onboarding

- status: skipped - no user-supplied domain materials
- materials read: 0 files
- potential skill patterns noted: 0
- downstream implications flagged: yes

## Resolved Decision-Changing Unknowns

| Unknown or ambiguity | Provisional answer | User correction or resolution | Effect on plan |
|---|---|---|---|
| Specific reservoir | Start by finding simple candidate reservoirs with documented drought/flood/operation-stress events and public daily time series | User asked researcher to find example reservoirs rather than naming one | Planning unit 1 is candidate reservoir/source selection |
| Data source | Use public official data if available; ResOpsUS may be considered if public | User clarified ResOpsUS is public | ResOpsUS becomes the candidate demo dataset, with official sources used for validation and event documentation |
| U.S. scope | U.S. reservoirs are allowed despite ResOps Global default U.S. exclusion | User named ResOpsUS and asked for public official data | Candidate scan focuses on U.S. reservoirs |
| Primary research object | Human-AI interaction workflow, not the reservoir itself | User clarified that the reservoir is just a test example | Planning must prioritize workflow roles, gates, artifacts, and interaction logic |
| Initial reservoir route | Hords Creek Lake / Hords Creek Dam as small single-reservoir low-storage demo fixture | User approved Hords Creek route | Used only to test the workflow on a concrete public-data case |

## Prior Work Scan

Status: targeted but not complete. Planning unit 1 is a focused source and candidate-reservoir scan, recorded in `../notes/candidate-reservoir-source-scan.md`. Planning unit 2 records the approved Hords Creek label and gate strategy in `../notes/hords-creek-route-and-label-strategy.md`. Planning unit 3 reframes the work around the human-AI workflow architecture in `../notes/human-ai-workflow-architecture.md`; the Hords Creek method route in `../notes/hords-creek-method-route.md` is a demo-specific support note. A targeted hedging literature check in `../notes/hedging-literature-demand-loss-review.md` establishes demand and shortage/loss as mandatory inputs for meaningful hedging optimization.

## Research Opportunities and Routes Considered

| Opportunity or route | Prior-work/source basis | Gap or value | Initial feasibility | Decision |
|---|---|---|---|---|
| Hords Creek Lake low-storage/drought stress | ResOpsUS/USGS low-storage anomaly release; TWDB Water Data for Texas; USACE/TWDB reservoir context | Small single-reservoir demo fixture with clear low-storage anomaly labels and official public storage data | high | selected as test example |
| Clark Canyon Reservoir drought allocation stress | ResOpsUS/USGS low-storage anomaly release; USBR RISE daily storage/inflow/release; Reclamation drought testimony and project pages | Single Reclamation reservoir with long official daily records and documented drought-management implications | medium-high | backup candidate |
| Gillham Lake low-storage anomaly | ResOpsUS/USGS low-storage anomaly release; USACE Little Rock District pages and water-level data | Small USACE reservoir, used as a ResOpsUS low-storage example; simpler than large western systems | medium | backup candidate |
| Pactola Reservoir municipal restriction trigger | ResOpsUS/USGS low-storage anomaly release; USACE/USBR data; Rapid City public restriction thresholds | Clear human-action trigger based on storage/inflow, but paired storage system and municipal rules add complexity | medium | backup candidate |
| Lake Abilene current severe low-storage stress | TWDB Water Data for Texas; TPWD reservoir report | Ultra-simple public storage-only drought case | medium; may be outside ResOpsUS and lacks inflow/outflow | optional non-ResOpsUS demo |
| Lake Mendocino drought/flood-operation stress | ResOpsUS candidate; Sonoma Water FIRO documentation; CDEC/USACE data | Well-documented drought/flood tradeoff and operational modernization case | medium; more complex than first prototype needs | deferred |
| Lake Oroville 2017 spillway incident | DWR incident timeline and forensic documentation; CDEC operational data | Strong failure documentation with inflow/outflow/storage context | medium; event is severe and complex | backup candidate |
| Lake Mead drought shortage operation | USBR RISE and Lower Colorado River operations documentation | Strong drought/shortage documentation and long daily data | medium; multi-reservoir/legal context may be complex | backup candidate |
| Folsom Lake flood/drought releases and gate failure history | USBR Folsom FAQ; USBR RISE data; USACE water data | Good official daily data and clear flood-operation rules; infrastructure failure is documented | medium | backup candidate |

## Planning Depth Decision

| Item | Decision | Reason | Downstream implication |
|---|---|---|---|
| idea maturity | exploratory but reviewable | workflow architecture, gate design, workflow evaluation criteria, and first demo fixture are fixed for the Planning Review | use stepwise Planning |
| literature/prior-work scan depth | light first, then targeted | reservoir-demo sources and a light workflow prior-work map are available, but no full novelty review exists | use `../notes/workflow-prior-work-and-evaluation.md` before formal review; expand only if manuscript claims are planned |
| novelty assessment depth | deferred | workflow feasibility is the initial claim; novelty is not yet claimed | revisit before claiming research contribution |
| venue/output calibration depth | deferred | output is currently system/prototype/report, not a venue-targeted paper | revisit if manuscript route is chosen |
| revisit trigger | before Modeling | workflow architecture and demo test path are stable enough for formal Planning Review | revisit after reviewer critique and Planning Gate |

## Candidate Research Plans Considered

Current route options after scope correction:

| Candidate plan | Primary object | Demo fixture | Decision |
|---|---|---|---|
| Human-AI workflow feasibility demo | workflow architecture, gates, reviewer triage, provenance, model guardrails | Hords Creek low-storage stress event | selected for Planning |
| Single-reservoir case study | Hords Creek low-storage diagnosis and model performance | Hords Creek only | rejected as too narrow after user clarified workflow is primary |
| Multi-reservoir benchmark | general workflow and model comparison across reservoirs | multiple ResOpsUS reservoirs | deferred until first workflow demo is validated |
| Manuscript-style novelty study | contribution against human-AI/agentic workflow literature | one or more demos | deferred until output route and novelty claim are approved |

## Feasibility and Cost Check

| Item | Assessment | Evidence or test | Fallback |
|---|---|---|---|
| data access | feasible but not yet Modeling-acquired | ResOpsUS public dataset exists; USGS low-storage anomaly release exists; Water Data for Texas Hords Creek CSV endpoint returned HTTP 200 with about 1.17 MB text/csv-like content | use USGS anomaly release plus TWDB CSV as first route; fall back to USGS monitoring data or USACE if needed |
| text/table/image/API extractability | feasible | Water Data for Texas CSV header includes date, water_level, surface_area, reservoir_storage, conservation_storage, percent_full, conservation_capacity, dead_pool_capacity; USGS API provides Hords Creek monitoring metadata | use ResOpsUS/USGS static files if official CSV parsing is easier than live APIs |
| candidate sources vs usable acquired data | candidate only | USGS low-storage metadata and event summaries were downloaded only for Planning source-screening; no selected-reservoir Modeling data have been acquired | Modeling must download/read selected reservoir time series and check variables |
| hedging data sufficiency | enough for storage/hydrologic diagnosis; not yet enough for meaningful hedging optimization | preliminary source check found TWDB storage and USACE HORT2 daily inflow, outflow, gated outflow, spillway outflow, precipitation, evaporation, and elevation; hedging literature requires demand and shortage/loss; event-period demand, pumpage/withdrawal, mandatory-release classification, and shortage penalty are not yet confirmed | add Demand-Loss Gate before optimization; switch reservoir or downgrade claim if it fails |
| demo scale | Hords Creek Lake, one low-storage stress label, daily data | recommended first event is 2011-09-30 to 2012-02-17, with 1983-12-21 to 1986-06-04 as historical reference | revise event window if user prefers longest event |
| full-study scale | one reservoir initially; multi-reservoir extension future work | reduces scope risk | expand after demo gate |
| runtime/storage burden | likely modest; ResOpsUS zip is hundreds of MB | Zenodo lists compressed zip size around 307 MB for Version 2 | download only required reservoir if possible |
| API/token cost | none expected for data; LLM/reporting use not yet costed | public sources available | keep analysis standard Python/R first |
| external tool or skill feasibility | ResOpsUS, official agency data portals, time-series anomaly/modeling packages | needs tool scan after route selection | use simple baseline before automated model selection |
| licensing/privacy/ethics | public/open candidate; no private operator data planned | ResOpsUS Zenodo lists CC-BY 4.0 | verify each official source access terms before Modeling |

## Data Source Identity

Current status: candidate sources only. Usable data will count only after Modeling downloads/queries data and verifies required variables.

| Role | Source name or URL | Version/date/access date | License/access status | Notes |
|---|---|---|---|---|
| raw data host | ResOpsUS Zenodo, `https://zenodo.org/records/6612040`; USGS low-storage anomaly ScienceBase release, `https://doi.org/10.5066/P9PIEH9Y`; official source portals depending on selected reservoir | accessed 2026-07-03 | ResOpsUS CC-BY 4.0; USGS public domain; official terms pending | candidate |
| official data source | Recommended Hords Creek route: TWDB Water Data for Texas Hords Creek CSV/page and USGS monitoring location `USGS-08141000`; USACE/TWDB official reservoir pages for project context | accessed 2026-07-03 | public official pages; exact terms pending | candidate |
| documentation source | Recommended Hords Creek route: USGS low-storage event metrics plus TWDB/USACE project context; water-control manual if needed | accessed 2026-07-03 | public; TWDB/USGS data are provisional where stated | candidate |
| citation source | ResOpsUS Scientific Data article; USGS low-storage data release; TWDB/USACE pages | accessed 2026-07-03 | public/open where available | candidate |

## Selected or Confirmed Research Route

Primary route: design a human-AI interaction workflow for reservoir operation-stress detection, diagnosis, model building, reviewer critique, and reporting. Hords Creek Lake / Hords Creek Dam, Texas is the approved small demo fixture. The initial low-storage stress label and demo event window are approved only as the first test case.

| Route element | Selected value | Evidence or reason | User confirmation status |
|---|---|---|---|
| working research question | How can a human-AI gated workflow coordinate document-based cause analysis, public-data acquisition, stress/failure labeling, time-series diagnosis, demand and shortage-loss specification, hedging/operation optimization, loss-reduction scenario modeling, automated model building, reviewer critique, and report generation, using Hords Creek as a bounded test example? | matches clarified user goal: workflow first, reservoir demo second; includes user correction that causes must be document-analyzed before modeling and hedging must be modeled as an operation optimization problem with demand/loss defined first | revised after user correction |
| intended output and claim level | workflow specification plus demo evidence package; feasibility claim only until Modeling validates the workflow on Hords Creek | avoids overclaiming either operator failure or generalized workflow performance | approved for Planning Review |
| data/source strategy | ResOpsUS plus USGS low-storage anomaly release, cross-checked with TWDB Water Data for Texas and USGS/USACE official sources | public and source-backed | confirmed as current route; exact acquired files pending Modeling |
| method family | human-AI gate architecture, maker-checker review loop, document-driven cause analysis, provenance-first data handling, transparent baseline, Demand-Loss Gate, release/withdrawal controllability classification, hedging/operation optimization, bounded loss-reduction scenario modeling, bounded automated model selection, evidence-bound driver diagnosis | focuses on interaction workflow while preserving a realistic demo and preventing empty optimization claims | revised after user correction |
| feasibility status and fallback | feasible candidate; fallback to storage-only TWDB/USGS route if ResOpsUS variables are incomplete | source endpoints verified enough for Planning | provisional |
| target venue/audience/output mode | technical workflow/prototype package for researchers building human-gated AI systems, with reservoir operators as an applied audience | user wants a system with gates, not only a reservoir report | provisional |
| future-work boundary | multi-reservoir generalization, catastrophic infrastructure failure, and strong causal/operator-fault claims | too complex for first prototype | provisional |
| system step structure | 10-step human-gated workflow from source setup through final review | user said the 10-step structure is acceptable | confirmed |
| initial label and event | USGS 10th-percentile low-storage anomaly for Hords Creek Dam / Dam_ID `1249`; first demo event 2011-09-30 to 2012-02-17 | user approved this as the starter demo event | confirmed |
| failure wording | low-storage operation stress | keeps the prototype evidence-bound without implying operator fault | confirmed for initial study |

## External Tool and Skill Scan

| Candidate tool, package, template, or skill | Workflow task | Maturity or reason to trust | Output to bring back | Cost/access/limits | Decision |
|---|---|---|---|---|---|
| ResOpsUS | standardized reservoir time-series data | peer-reviewed Scientific Data descriptor; USGS catalog; Zenodo public dataset | reservoir-specific storage/inflow/outflow/elevation/evaporation series | static dataset through 2020; not always official live source | reuse as candidate demo dataset |
| Official operator data portals: CDEC, USBR RISE, USACE water data | validation and event-specific data | official agency sources | station variables, time windows, provenance, event documents | APIs/pages vary; may need parsing | reuse for selected reservoir |
| USGS low-storage anomaly data release | drought/anomalously low storage labels and metrics | USGS data release based on ResOpsUS reservoirs | low-storage thresholds, anomaly event summaries, annual stats | drought-focused only; not flood/spillway failure | reuse for low-complexity drought route |
| Official drought, climate, water-control, and water-conservation documents | document-driven cause analysis, demand/loss specification, and loss-reduction scenarios | NWS/NOAA/TWDB/USACE/City of Coleman official sources | documented drivers, drought-response triggers, demand-reduction targets, conservation/infrastructure actions, rate/proxy loss data | documents may not perfectly align to daily data or the 2011-2012 event | required before time-series diagnosis and hedging optimization |
| USACE CWMS HORT2 time series | water-balance variables for diagnosis and hedging preconditions | official USACE water data platform | daily inflow, outflow, gated/spillway outflow, elevation, precipitation, evaporation where available | demand/mandatory-rule classification still missing | use for storage diagnosis; not sufficient for hedging optimization without Demand-Loss Gate inputs |
| Local resops-semantic-layer skill | ResOps inventory context and caveats | local skill references and source inventory | source caveats and inventory notes | ResOps Global excludes U.S. by default unless user changes scope | use for caveats only |

## Skill Construction Decision

Deferred until route selection. A project-specific skill may be useful later for reservoir-failure step gating, but external data/model tools should be checked first.

## Planning Reviewer Critique

Pending. Formal review request written at `../artifacts/reservoir-failure-plan-2026-07-03/review-request.md`. An informal early-look critique was provided before the formal review request; triage is recorded in `../notes/informal-reviewer-early-look-triage.md`.

## Researcher-Agent Response to Planning Review

Pending.

## Approved Research Question

Provisional: How can a human-AI gated workflow coordinate document-based cause analysis, public-data acquisition, stress/failure labeling, time-series diagnosis, demand and shortage-loss specification, hedging/operation optimization, loss-reduction scenario modeling, automated model building, reviewer critique, and report generation, using Hords Creek as a bounded test example?

## Working Title

Human-AI Gated Workflow for Reservoir Operation-Stress Detection and Diagnosis

## Hypotheses or Expected Claims

- A structured human-AI workflow can make reservoir stress/failure analysis more traceable and human-reviewable on one public-data demo by separating source selection, label definition, data checks, detection, diagnosis, model building, reviewer critique, and reporting into gated steps.
- Hords Creek can serve as a bounded public-data test fixture for checking whether the workflow produces reproducible artifacts and human-reviewable decisions.
- Document-driven cause analysis before time-series modeling can keep diagnosis and loss-reduction claims tied to official evidence instead of post-hoc model interpretation.
- Hedging should be treated as an operation optimization problem that first defines demand, shortage/loss, and controllability, then separates mandatory releases from controllable or hedgeable outflows and minimizes shortage/storage losses.
- If demand and shortage/loss cannot be found or approved for Hords Creek, the workflow should surface that as a Demand-Loss Gate failure rather than produce an unsupported hedging result.

Workflow-level evaluation plan: use `../notes/workflow-prior-work-and-evaluation.md` to assess traceability, reproducibility, human reviewability, claim support, and automation safety. Do not claim superiority over an ungated workflow unless a comparator evaluation is explicitly added later.

## Data Plan

- primary data source: ResOpsUS public dataset and/or the USGS low-storage anomaly release for Hords Creek Dam / Dam_ID `1249`.
- backup data source: TWDB Water Data for Texas Hords Creek CSV, USGS monitoring location data, and USACE water data/context.
- exact raw data host: ResOpsUS Zenodo; USGS ScienceBase low-storage release; TWDB Water Data for Texas Hords Creek CSV endpoint.
- official data source: TWDB Water Data for Texas and USGS monitoring location `USGS-08141000`; USACE/TWDB official project pages for context.
- documentation source: USGS low-storage event summaries plus TWDB/USACE reservoir context.
- cause-analysis document sources: NWS/NOAA/Texas climate summaries, TWDB reservoir condition reports, USACE water-control/drought-contingency materials, City of Coleman drought contingency and water conservation plans.
- hedging literature source: targeted literature review in `../notes/hedging-literature-demand-loss-review.md` establishes demand and shortage/loss as mandatory for hedging optimization.
- data version or access date: access date 2026-07-03 for candidate source scan.
- license/access status: ResOpsUS CC-BY 4.0; official terms to verify.
- acquisition success rule: Hords Creek counts only when daily storage can be read for the target event period, the selected USGS low-storage anomaly label can be linked to the same dates, and at least one explanatory driver or operational variable can be checked from ResOpsUS, official data, or approved auxiliary data.
- Demand-Loss Gate success rule: hedging optimization counts as meaningful only when Modeling acquires or the user approves (1) event-period demand, policy-scenario demand, or explicitly synthetic demand, (2) an official, proxy, or explicitly synthetic shortage/loss function, and (3) a controllability classification for releases/withdrawals.
- minimum viable data scale: Hords Creek, one documented low-storage stress period, daily data around the event window plus baseline years.
- full-study data scale: one workflow exercised on one reservoir test fixture first; multi-reservoir or multi-failure-mode generalization is future work.
- key variables: storage, inflow, outflow/release, elevation, evaporation if available, precipitation, temperature, drought labels, demand/withdrawal, drought-stage trigger indicators, conservation/loss variables, mandatory-release indicators, hedgeable-outflow classification, and hedging policy variables if available.
- unit of analysis: reservoir-day.
- time/spatial coverage: Hords Creek candidate has USGS low-storage events from 1981-2020 and current TWDB public storage status; recommended first demo event is 2011-09-30 to 2012-02-17.
- selected label/event: USGS 10th-percentile low-storage anomaly for Hords Creek Dam / Dam_ID `1249`, with first demo event 2011-09-30 to 2012-02-17; approved by user on 2026-07-03.
- access or licensing concerns: ResOpsUS is static through 2020; official live data may be provisional and subject to revision.

## Method Blueprint

Draft system/workflow steps with human gates, accepted as the working structure. Hords Creek instantiates these steps but does not define the workflow itself:

1. Candidate reservoir and failure-mode selection gate.
2. Document evidence and cause-hypothesis gate.
3. Data acquisition and provenance gate.
4. Failure/event definition and label strategy gate.
5. Preflight and data-quality gate.
6. Baseline anomaly detection gate.
7. Time-series cause-diagnosis feature/rule design gate.
8. Demand and shortage-loss evidence gate.
9. Release/withdrawal controllability classification gate.
10. Hedging/operation optimization formulation gate.
11. Loss-reduction/mitigation scenario-design gate.
12. Automated model selection/build gate.
13. Model and scenario validation gate.
14. Report-generation gate.
15. Final review and release/archive gate.

Automation guardrail: before any automated model selection runs, the model
candidates, metrics, validation split, and permitted report claims must be
fixed in the Model package and approved through a human gate. The automated
step cannot change labels, scope, metrics, or claim level without a new gate.

## Expected Manuscript Package

Not active yet. Reporting mode is expected to be a technical diagnostic report/prototype package unless the user later selects a manuscript route.

## Risks and Gate Notes

| Risk | Severity | Mitigation |
|---|---|---|
| Failure definition may be too broad | high | choose one failure/stress type first |
| ResOpsUS may not include the best candidate reservoir or all required variables | medium | verify reservoir-specific coverage before Modeling |
| Official sources may be provisional or hard to parse | medium | use official sources for validation and documentation, ResOpsUS for standardized modeling |
| Cause diagnosis could become unsupported causal inference | high | start with evidence-linked diagnostic categories and avoid causal claims beyond data |
| Cause analysis may be skipped or made post-hoc after modeling | high | require document-coded causal hypotheses before time-series modeling |
| Hedging optimization may treat mandatory releases as if they were optional | high | classify outflows as mandatory, controllable, hedgeable, reducible loss, or unknown before optimization |
| Data may support only diagnosis or toy scenarios, not true optimal hedging | high | add Demand-Loss Gate; default to data-insufficiency or explicitly labeled policy/synthetic scenario unless demand, loss, rule, and withdrawal data are found |
| Demand and shortage/loss may be unavailable for Hords Creek | high | require Demand-Loss Gate before hedging optimization; if it fails, switch reservoir, use a clearly labeled policy/synthetic scenario, or report data insufficiency |
| A synthetic loss function could make the research look more substantive than it is | high | require user approval of claim level and sensitivity analysis; label synthetic loss as illustrative only |
| Optimization may use perfect hindsight and overstate loss-reduction potential | high | predeclare foresight assumptions; separate perfect-hindsight diagnostic scenarios from realistic forecast-based policies |
| Loss-reduction claim may overstate what operations could control during an extreme drought | high | report storage improvement, peak shortage reduction, duration reduction, cumulative low-storage intensity reduction, or no material reduction; separate climate attribution scenarios from operator-controlled actions |
| Automated model building may overfit or chase performance | high | require baseline, validation, and human gate before reporting |
| Project/folder naming may imply "failure" when the approved demo label is "operation stress" | medium | use "stress/failure" in package text and reserve stronger failure/operator-fault claims for evidence-supported cases |

## Planning Gate Decision

Pending formal reviewer critique, researcher triage, and user gate decision.

## Acceptance Rubric for Model Stage

The Model stage can begin only if:

- one reservoir and one initial failure/stress type are selected;
- the primary research object is the human-AI workflow, with Hords Creek only as a test fixture;
- document-driven cause analysis, demand/loss specification, release classification, hedging optimization, and loss-reduction scenario design are included before automated modeling;
- the Demand-Loss Gate is accepted as a hard Modeling checkpoint: no substantive hedging claim without approved demand, shortage/loss, and controllability inputs;
- ResOpsUS or official data access is verified enough to define an acquisition success rule;
- candidate sources are distinguished from usable acquired data;
- event/failure documentation is linked to a defined time window;
- workflow architecture, workflow evaluation criteria, demo method route, and validation rubric are approved;
- Planning Reviewer findings are triaged;
- the user approves the Planning Gate.
