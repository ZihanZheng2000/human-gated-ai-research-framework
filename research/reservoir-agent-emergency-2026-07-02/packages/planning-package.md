# Approved Plan Package

## Planning Workflow Identity

- package status: paused stepwise Planning draft - not ready for Planning Review
- Planning Researcher: Codex
- Planning Reviewer: Claude Code
- reviewer file: `docs/reviewer-agents/planning-reviewer-agent.md`
- reviewer mode: critique-only
- Planning Review status: paused - wait for user stepwise discussion
- researcher-agent response status: pending
- user Planning Gate status: pending - not ready

## Stepwise Collaboration Note

The user clarified after this draft was created that they prefer a gradual,
discussion-first workflow rather than having the full Planning content written
into one package at once. Treat this package as a preliminary scaffold and
source inventory, not as a finished Planning Review draft.

Next Planning unit to discuss: the dam/reservoir worker emergency problem
taxonomy. After user discussion, accepted points should be summarized here
compactly, while detailed notes remain in supporting artifacts such as
`research/reservoir-agent-emergency-2026-07-02/notes/`.

## User-Need Profile

- research area: AI agents for reservoir operation emergency decision support
- intended output: academic paper plan, likely a framework or review-plus-conceptual-model manuscript
- workflow mode: full research project
- idea maturity: partly formed idea
- planning depth: full calibration for literature/gap and light-to-moderate feasibility calibration before Modeling
- intended research product: manuscript package with an emergency-scenario taxonomy, AI-agent role model, and risk-evaluation framework
- research purpose: build method or tool; compare alternatives; evaluate risk of concrete AI-agent support modes
- practical success criterion: produce a defensible paper plan explaining how AI agents can assist reservoir emergency operation across emergency types, how those interventions should be modeled, and how each support mode should be risk-evaluated before use
- target audience or venue: water resources / hydrology / emergency management / AI-for-critical-infrastructure readers; exact venue undecided
- venue/output status: provisional
- preferred citation or formatting style: undecided; use DOI/official URLs during Planning
- available data: none supplied by user
- public data needed: likely yes if Modeling includes case examples; optional if the paper is a conceptual framework with literature-grounded examples
- time/tooling constraints: not specified; assume a staged plan with an inspectable small evidence base first
- runtime or API/token constraints: no paid APIs assumed for Planning; Modeling should avoid uncontrolled LLM calls unless approved
- method-complexity limit: moderate; methods should remain explainable to reservoir-operation and emergency-management audiences
- novelty expectation: scholarly contribution through scenario taxonomy, human-agent task allocation, and risk evaluation rather than a claim that AI can autonomously operate reservoirs
- topics, methods, or data types to avoid: no autonomous release decisions, no unsupported safety claims, no real-time operational recommendation without human approval and validated hydrologic/engineering models
- gate mode: real user gates

## Domain Onboarding

### Material Inventory

| File or folder | Material type | Domain covered | Date or version |
|---|---|---|---|
| none supplied | other | not applicable | not applicable |

### Domain Knowledge Summary

No user-supplied domain materials were provided. Planning uses public literature, official dam-safety guidance, and AI risk-management guidance.

**Key domain concepts and terminology:**

- Reservoir operation emergency includes impending or actual sudden water release caused by dam failure/accident or impending flood conditions, and may endanger human life or downstream property.
- Emergency Action Plans (EAPs) define incidents, potentially affected areas, notification flows, and pre-planned actions for dam incidents.
- Risk-informed reservoir operation considers uncertainty, consequences, multi-criteria tradeoffs, and human operator responsibility.
- AI agents in this plan mean software systems that can perceive inputs, reason over tasks, call tools or models, coordinate subtasks, and produce decision-support outputs. They are not assumed to have autonomous authority over reservoir releases.
- A Planning support review in `research/reservoir-agent-emergency-2026-07-02/notes/dam-worker-emergency-problem-review.md` reframes the domain around the concrete problems dam/reservoir workers face during emergencies: detection/classification, situational awareness, forecast uncertainty, conflicting objectives, coordination, warning/evacuation interface, drought response, multi-reservoir/cascade effects, staff/site safety, and termination/after-action learning.

**Field norms or conventions relevant to this project:**

- Human operators and responsible authorities remain central in high-consequence reservoir operation.
- Emergency operation requires traceable, time-sensitive, protocol-compatible, and auditable decisions.
- Flood, drought, dam-safety, communication, infrastructure, and data-loss emergencies may need different models and controls.

**Domain-specific constraints (data access, measurement, ethics, reporting):**

- Safety-critical decisions require explicit human oversight, validated inputs, uncertainty communication, and audit logs.
- Any case-study or simulation data must distinguish candidate links from usable acquired data.
- The manuscript should not imply that an LLM alone can replace hydrologic, hydraulic, dam-safety, or emergency-management models.

**Conflicts or uncertainties found in the materials:**

- The exact manuscript route is not yet locked: possible routes include conceptual framework, structured literature review, design-science paper, or small case-study demonstration.
- The emergency-scenario taxonomy still needs literature calibration and reviewer critique before approval.

**User resolution for any conflicts:**

- User confirmed the output should be a paper and the scope should cover any reservoir-operation emergency type, modeling different situations and evaluating the risk of concrete approaches.

### Skill Cards Generated from User Materials

| Card ID | Source material | Pattern captured | Status |
|---|---|---|---|
| none | none | none | not applicable |

### Domain Onboarding Status

- status: skipped - no user materials
- materials read: 0 files
- skill cards produced: 0
- downstream implications flagged: yes

## Planning Depth Decision

| Item | Decision | Reason | Downstream implication |
|---|---|---|---|
| idea maturity | partly formed | User has a clear topic and output type, but not yet a fixed manuscript route, dataset, or validation method. | Planning must refine research question, output route, and Model-stage evidence strategy. |
| literature/prior-work scan depth | full | A paper needs a defensible gap and should not overclaim novelty. | Modeling should start only after a focused literature basis is recorded. |
| novelty assessment depth | full | AI agents in reservoir emergency operation is a high-stakes, emerging topic with adjacent work in RL, LLM extraction, decision support, and emergency AI. | Claim level must be conservative and source-backed. |
| venue/output calibration depth | light now, full before Reporting | Exact venue is unknown. | Planning can propose routes; Reporting must revisit venue requirements if a target journal is selected. |
| revisit trigger | before Modeling scale-up and before Reporting | If user chooses empirical case study or target venue. | Add data/source or venue-specific calibration before stronger claims. |

## Clarifications Before Planning

| Question or ambiguity | Resolution | Effect on plan |
|---|---|---|
| Final output type | User selected academic paper. | Plan targets manuscript-quality literature/gap and evidence standards. |
| Emergency scope | User selected any reservoir-operation emergency type, with modeling of different situations and risk evaluation of specific approaches. | Plan should produce an emergency-scenario taxonomy instead of narrowing prematurely to flood-only operation. |
| Domain materials | User selected no materials for now. | Domain onboarding is skipped; public sources are used. |

## Prior Work, Skill Patterns, and Gaps

| Cluster or source | What has been done | Reusable skill or method pattern | Gap or opportunity | Relevance to this plan |
|---|---|---|---|---|
| FEMA/FERC emergency action planning guidance, `https://www.ferc.gov/sites/default/files/2020-04/fema-64.pdf`; FERC EAP program, `https://www.ferc.gov/emergency-action-plan-eap-program` | Defines dam-operation emergencies, EAP contents, inundation maps, notification coordination, and federal consistency efforts. | Treat emergency type, consequence area, notification chain, and pre-planned action as core units for agent task allocation. | EAP guidance is not an AI-agent design or risk-evaluation framework. | Provides authoritative emergency-management baseline and safety boundary. |
| ASDSO EAP overview, `https://damsafety.org/dam-owners/emergency-action-planning` | Defines EAPs as documents identifying incidents, affected areas, and pre-planned actions to reduce loss of life, infrastructure, water resources, and property. | Use incident-to-action mapping as an anchor for scenario taxonomy. | Does not classify AI-assist modes or agent-specific failure risks. | Supports practical framing for operators and emergency managers. |
| Risk-informed decision-making for reservoir flood operation, `https://www.iahr.org/library/info?pid=17734` | Presents reservoir flood operation risk under uncertainty using probabilistic risk analysis and multi-criteria decision analysis; stresses human operator importance. | Evaluate alternatives by uncertainty, consequences, and multicriteria tradeoffs. | Existing risk-informed frameworks do not directly evaluate LLM/agent tool-use risks, hallucination, authority escalation, or human-agent coordination. | Core methodological basis for risk-evaluation framework. |
| Reservoir operation risk under climate change, USGS/Water Resources Research DOI `10.1029/2008WR006941`, `https://pubs.usgs.gov/publication/70034803` | Shows reservoir-operation risk assessment depends on risk metrics, scenario ensembles, and design choices. | Use scenario-based risk metrics and sensitivity to analytical design choices. | Climate-planning risk studies do not answer agent intervention and emergency workflow questions directly. | Helps frame uncertainty and risk attitude in agent-support evaluation. |
| RL in water-resource management systematic review, `https://www.frontiersin.org/journals/water/articles/10.3389/frwa.2025.1537868/pdf` | Reviews RL as sequential decision-making for water management, including uncertainty, weather, and water-level constraints. | Treat reservoir operation as sequential decision-making with constraints and training/evaluation choices. | RL "agent" literature often optimizes policies, while the user's question concerns AI agents assisting emergency human decisions and risk evaluation. | Distinguishes control-policy agents from LLM/tool-using decision-support agents. |
| Stochastic multi-objective flood-control optimization, `https://www.frontiersin.org/journals/water/articles/10.3389/frwa.2025.1606096/full` | Optimizes release policies under many inflow scenarios with scenario clustering and reliability comparisons. | Model emergency alternatives using scenario sets, objective tradeoffs, and constraint satisfaction. | Optimization outputs need human-interpretable risk review and protocol compatibility before emergency use. | Candidate modeling pattern for flood-emergency case examples. |
| LLM reservoir dispatch information extraction, Scientific Reports 2024, `https://www.nature.com/articles/s41598-024-64954-0` | Uses structured prompts to extract reservoir dispatch information and emphasizes terminology, rules, format, examples, and domain persona. | LLMs can assist with regulation/rule extraction if constrained by structured prompts and domain terminology. | Extraction support is narrower than emergency operation decision support; risk of noise and unstable outputs remains. | Candidate low-risk agent role: protocol/rule retrieval and summarization. |
| AI in emergency and crisis management rapid evidence review, `https://scientificadvice.eu/scientific-outputs/artificial-intelligence-in-emergency-and-crisis-management-rapid-evidence-review-report/` | Classifies AI uses in crisis contexts: situational awareness, forecasting, damage assessment, decision support, and human-AI hybrid systems. | Use socio-technical lens and map AI functions to crisis-management phases. | Needs translation to reservoir-specific emergencies and operational constraints. | Supplies broad emergency-management AI taxonomy. |
| Human-AI decision patterns in disaster scenarios, arXiv 2025, `https://arxiv.org/html/2509.12034v1` | Reviews human-AI collaboration patterns for high-stakes disaster decision-making, including decision support, task/resource coordination, trust/transparency, and simulation/training. | Use human-AI interaction patterns to classify agent roles and oversight. | Not reservoir-specific and may include preprint-only evidence; must verify key claims before manuscript citation. | Useful structural pattern for scenario-role taxonomy. |
| NIST AI RMF and GAI Profile, `https://www.nist.gov/itl/ai-risk-management-framework`, `https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf` | Provides AI risk management functions and GAI risk-management considerations across lifecycle. | Map agent risks through governance, mapping, measurement, management, provenance, testing, and incident disclosure. | Generic AI risk guidance needs adaptation to reservoir emergency operation. | Provides authoritative AI-risk vocabulary and governance baseline. |
| Agentic AI risk profile, `https://cltc.berkeley.edu/publication/agentic-ai-risk-profile/` | Highlights human control, accountability, intervention points, escalation pathways, shutdown mechanisms, system-level risk assessment, monitoring, containment, transparency, and documentation. | Use agent-specific risk levers for tool access, autonomy, monitoring, and escalation. | Not water-domain specific and should supplement, not replace, dam-safety risk frameworks. | Helps evaluate agentic-system risks beyond ordinary ML. |
| Planning support review, `research/reservoir-agent-emergency-2026-07-02/notes/dam-worker-emergency-problem-review.md` | Synthesizes official EAP/water-control/drought guidance and selected reservoir operation literature into a dam-worker emergency problem map. | Center the paper on operational work problems before assigning AI-agent roles. | Needs reviewer critique and later source-matrix validation before manuscript claims. | Adds a source-coding dimension: worker problem and authority boundary. |

## External Tool and Skill Scan

| Candidate tool, package, template, or skill | Workflow task | Maturity or reason to trust | Output to bring back | Cost/access/limits | Decision |
|---|---|---|---|---|---|
| Academic databases and DOI/official-source search | literature | Standard scholarly retrieval | included/excluded source list, verified citation metadata | access limits for paywalled papers | reuse |
| Official dam-safety and emergency-management guidance | domain baseline | FEMA/FERC/ASDSO are authoritative for US dam emergency planning | emergency definitions, EAP components, risk controls | US-centric; may need international supplements | reuse |
| NIST AI RMF / GAI Profile | AI risk framing | Authoritative public AI risk framework | risk categories and governance controls | generic, not water-specific | adapt |
| Reservoir optimization / simulation tools | modeling | Mature in water resources but project-specific choice is undecided | scenario model outputs if empirical case study is selected | data and calibration burden | defer until Planning Gate |
| LLM/agent frameworks | prototype or evaluation | Useful for agent workflow demos | prompts, tool logs, failure cases, human approval events | safety-critical use requires strict containment | defer; do not deploy for real operation |
| Repository workflow-native skills | gate and evidence control | Maintained by this repo | stage packages, review requests, gate records | not domain-specific | reuse |
| `resops-semantic-layer` skill | possible reservoir-data context | Existing local skill for reservoir time-series inventory questions | source coverage and data caveats if ResOps inventory becomes data source | only relevant if chosen as Modeling data source | possible later reuse |

## Skill Construction Decision

| Skill need | External alternative checked | Why external option is sufficient or insufficient | Decision | Promotion status |
|---|---|---|---|---|
| Reservoir emergency AI-agent risk rubric | NIST AI RMF, agentic AI risk profile, EAP guidance, reservoir risk-informed decision literature | External sources provide pieces, but no single inspected source yet gives a reservoir-emergency-specific AI-agent risk rubric. | no repository skill yet; create manuscript framework first | none |
| Scenario taxonomy for emergency operation | EAP guidance, disaster AI reviews, reservoir operation literature | Existing taxonomies are adjacent, not tailored to AI-agent reservoir-operation support. | develop as paper contribution | none |
| Empirical/prototype evaluation | Reservoir optimization tools, public datasets, ResOps inventory | Too early to choose before plan approval. | defer to Modeling contract | none |

## Research Opportunities Considered

| Opportunity | Prior-work basis | Feasibility | Novelty | Decision |
|---|---|---|---|---|
| Scenario-role-risk framework paper | EAP guidance, AI crisis management review, NIST AI RMF, reservoir risk-informed decision literature | high for Planning and Reporting; Modeling can use literature matrix and small illustrative case | moderate to high if reservoir-specific taxonomy is well calibrated | selected |
| Empirical LLM agent prototype for one reservoir emergency | LLM dispatch extraction and decision-support literature | uncertain without dataset, simulator, and safety constraints | potentially high but risky | backup or later Modeling addendum |
| Review paper on AI for reservoir emergency management | disaster AI and RL reviews plus reservoir operation papers | feasible but requires systematic search protocol | moderate | backup |
| RL control policy comparison for flood release | RL/optimization reservoir literature | feasible only with model/data and narrower scope | lower for user's agentic question | rejected for main route, possible case-study component |

## Feasibility and Cost Check

| Item | Assessment | Evidence or test | Fallback |
|---|---|---|---|
| data access | uncertain for empirical case; feasible for framework/literature matrix | No operational dataset has been selected or acquired. | Use literature-grounded scenario taxonomy and optional synthetic examples in Modeling. |
| text/table/image/API extractability | feasible for literature and official guidance; uncertain for case data | Web sources and PDFs are accessible; exact paper full text may vary. | Use abstracts/metadata where full text is inaccessible and flag limitations. |
| candidate sources vs usable acquired data | candidate sources only | Planning has identified candidate literature and guidance; no data counted as usable evidence. | Modeling must define acquisition success for papers, datasets, or case materials. |
| demo scale | 4-6 emergency scenarios, 3-5 agent roles, 1 risk matrix | Enough to test taxonomy and risk-evaluation logic. | Narrow to flood-control emergency if framework becomes too broad. |
| full-study scale | 15-30 core papers/guidance documents plus 1-2 illustrative cases | Feasible for a conceptual/framework manuscript. | Convert to scoping review if literature volume is high. |
| runtime/storage burden | low to moderate | Literature matrix and tables can be handled locally. | No large compute unless an agent prototype or simulator is approved. |
| API/token cost | low for Planning; uncertain for LLM prototype | No paid API required for literature matrix. | Use manual coding of papers and no prototype. |
| external tool or skill feasibility | feasible | Existing workflow and external sources are available. | Keep framework paper without creating new skill. |
| licensing/privacy/ethics | moderate | Safety-critical domain; real operational logs may be sensitive. | Use public sources, synthetic examples, or anonymized historical cases only. |

## Data Source Identity

| Role | Source name or URL | Version/date/access date | License/access status | Notes |
|---|---|---|---|---|
| raw data host | not selected | access date 2026-07-02 for candidate web sources | candidate only | Modeling must decide whether "data" means literature corpus, public reservoir datasets, synthetic scenario set, or case documents. |
| official data source | FEMA/FERC/ASDSO guidance for EAP baseline; NIST for AI risk baseline | accessed 2026-07-02 | public | Official guidance anchors definitions and risk controls. |
| documentation source | same as official sources plus DOI/publisher pages for literature | accessed 2026-07-02 | public/paywalled mix | Exact citation metadata to verify during Modeling. |
| citation source | DOI/publisher/official pages | accessed 2026-07-02 | public/paywalled mix | No citation is final until verified in Modeling/Reporting. |

## Venue or Output Calibration

| Candidate venue/output | Why it fits | Tradeoffs | Decision |
|---|---|---|---|
| Water resources journal conceptual/framework article | Reaches reservoir-operation audience and can emphasize risk-informed decision support. | Needs stronger water-domain literature and possibly case validation. | selected provisional route |
| AI for emergency management / disaster risk journal article | Fits human-AI crisis decision framing. | Reservoir-specific engineering depth may be harder to position. | backup |
| Design-science / decision-support systems paper | Fits framework and AI-agent system architecture. | Requires clearer artifact/evaluation method. | backup |
| Scoping review paper | Feasible if broad evidence is main contribution. | User asked how agents can help and risk-evaluate approaches, so pure review may be less useful. | backup |

If no venue is selected, state the provisional route and when it should be revisited.

The provisional route is a water-resources framework manuscript. Venue should be revisited before Reporting after the literature matrix and Modeling evidence show whether the paper is conceptual, review-based, or prototype/case-based.

### Official Venue Requirements

| Requirement | Official rule or constraint | Effect on plan |
|---|---|---|
| article type and scope | deferred until target venue selected | Planning should avoid venue-specific claims for now. |
| manuscript structure | likely Introduction, Background, Taxonomy/Framework, Risk Evaluation, Discussion, Limitations | Reporting should convert framework into manuscript architecture. |
| word/page limit | deferred | no effect yet |
| abstract format | deferred | no effect yet |
| reference style | deferred | preserve DOI/URL metadata now |
| figure/table rules | deferred | plan for tables and conceptual diagrams only |
| data/code availability | likely needed if an empirical/prototype component is added | Modeling must preserve artifacts. |
| ethics/funding/COI/AI disclosure | AI-use disclosure likely required by many venues | Reporting must include AI-use and safety limitations. |
| reporting checklist or supplement rules | deferred | no effect yet |

### Venue Exemplar Scan

Deferred until the user selects or accepts a target venue. Because the current target is provisional, Planning does not yet inspect venue exemplars.

| Exemplar | Why similar | Structure pattern | Evidence/validation pattern | Figure/table pattern | Citation pattern | Implication for this plan |
|---|---|---|---|---|---|---|
| deferred | target venue not selected | deferred | deferred | deferred | deferred | revisit before Reporting |

### Venue-Derived Plan Constraints

| Constraint from venue or exemplars | Required plan response | Status |
|---|---|---|
| Safety-critical claims require strong limitation language | avoid autonomous-operation claims and preserve human oversight | needs Reporting |
| Framework paper needs clear novelty vs existing decision support and AI crisis frameworks | literature matrix must show gap | needs Modeling |
| If empirical case is included, data and reproducibility artifacts must be inspectable | define acquisition success and validation checks | needs Modeling |

## Candidate Research Plans Considered

| Plan | RQ | Data | Method | Venue/output fit | Decision |
|---|---|---|---|---|---|
| Framework paper | How can AI agents assist reservoir operation emergencies across scenario types, and how should the risk of each agent support mode be evaluated before use? | Literature/guidance corpus plus optional illustrative scenarios | Emergency taxonomy, agent role model, risk matrix, human oversight controls | strong for water-resources or decision-support article | selected |
| Scoping review | What does existing literature say about AI/agent support for reservoir emergency management? | Systematic/scoping literature corpus | Search protocol, inclusion/exclusion, thematic synthesis | strong if user wants review article | backup |
| Prototype/case study | Can a constrained AI agent improve situational awareness or protocol retrieval in one reservoir emergency scenario? | EAP/case documents and synthetic or public reservoir scenario | Agent prototype, task evaluation, failure/risk analysis | strong but higher risk and data needs | backup |

## Planning Reviewer Critique

| Finding ID | Reviewer concern | Severity | Evidence or reasoning | Route |
|---|---|---|---|---|
| pending | pending reviewer critique | pending | pending | pending |

If external Planning Review was skipped, record why:

- skipped reason: not skipped
- risk accepted: not applicable
- revisit trigger: not applicable

## Researcher-Agent Response to Planning Review

| Finding ID | Response status | Change made or planned | Blocks Planning Gate? | Notes |
|---|---|---|---|---|
| pending | pending | pending | pending | pending |

## Approved Research Question

`How can AI agents assist human decision makers during reservoir operation emergencies across different emergency scenarios, and how can the risks of each concrete agent-supported action be evaluated before operational use?`

## Working Title

`AI Agents for Reservoir Operation Emergencies: Scenario Modeling, Human-Agent Task Allocation, and Risk Evaluation`

## Hypotheses or Expected Claims

- AI agents are most defensible in reservoir emergencies when assigned to bounded decision-support tasks such as situational awareness, protocol retrieval, scenario comparison, uncertainty communication, documentation, and coordination support, rather than autonomous release control.
- Different reservoir emergency types require different models of state, uncertainty, timing, stakeholders, and consequences; a single generic agent workflow is unsafe.
- A useful risk-evaluation framework should combine reservoir risk-informed decision principles, emergency action planning constraints, AI risk-management controls, and human-agent oversight mechanisms.
- Agent-supported emergency operation should be evaluated by failure modes, consequence severity, uncertainty, human review points, tool/data provenance, and protocol compatibility.

## Data Plan

- primary data source: literature and guidance corpus covering reservoir emergency action planning, risk-informed reservoir operation, reservoir optimization/RL, LLM/agent support in reservoir dispatch, AI in emergency management, and AI risk management
- backup data source: narrower flood-operation corpus if the all-emergency taxonomy is too broad
- exact raw data host: publisher/DOI pages, official FEMA/FERC/ASDSO/NIST pages, and downloaded PDFs where allowed
- official data source: FEMA/FERC/ASDSO for dam emergency planning; NIST for AI risk management; peer-reviewed publisher pages for scholarly studies
- documentation source: official guidance pages and article metadata pages
- data version or access date: initial candidate access date 2026-07-02; exact corpus to be locked during Modeling
- license/access status: public for official guidance; mixed for literature; use metadata/abstracts when full text is unavailable
- acquisition success rule: a source counts only when bibliographic metadata, source type, relevance category, and at least one inspectable abstract/full-text/guidance passage can be recorded in a literature matrix
- minimum viable data scale: 12-15 core sources spanning at least four clusters: EAP/emergency planning, reservoir risk/operation modeling, AI/agent emergency decision support, and AI risk governance
- full-study data scale: 25-40 screened sources with 15-30 included sources, depending on manuscript route
- key variables: emergency type, worker problem, decision task, authority boundary, agent role, input data/tools, human approval point, output, failure mode, consequence pathway, risk-control measure, evidence type
- unit of analysis: one agent-supported emergency task within one reservoir emergency scenario type
- time/spatial coverage: global literature, with US official guidance as initial emergency-planning baseline unless international sources are added
- access or licensing concerns: paywalled literature may limit full-text coding; real reservoir operational data may be sensitive

## Method Blueprint

1. Build a literature and guidance matrix from official dam-safety guidance, reservoir risk-informed operation papers, reservoir AI/optimization/RL studies, LLM/agent dispatch studies, disaster AI studies, and AI risk-management frameworks.
2. Code each source first by the dam/reservoir worker problem it addresses: detection/classification, situational awareness, forecasting/uncertainty, operation tradeoff, coordination, warning/evacuation interface, drought response, multi-reservoir/cascade effects, staff/site safety, or termination/after-action learning.
3. Derive a reservoir emergency scenario taxonomy, initially including flood-control emergency, drought/water-supply emergency, dam-safety/failure-risk emergency, downstream communication/evacuation emergency, sensor/data outage or conflicting forecast emergency, and multi-reservoir coordination emergency.
4. For each scenario type, model the decision context: time pressure, state variables, uncertainty sources, stakeholders, allowed actions, consequences, and required human authority.
5. Classify AI-agent support modes: monitor/summarize, retrieve protocols, extract rules, compare scenarios, coordinate tasks, draft communications, audit decisions, and simulate or recommend alternatives under constraints.
6. Build a risk-evaluation matrix for each support mode: plausible failure modes, likelihood/uncertainty, consequence severity, detectability, reversibility, authority boundary, human oversight point, data/tool provenance, and required containment.
7. Define a human-agent task-allocation principle: agent outputs remain advisory unless the task is low-consequence and pre-approved; high-consequence release, evacuation, public-warning, or dam-safety decisions require human authority and validated domain models.
8. Produce manuscript-ready tables and conceptual figures: worker-problem taxonomy, emergency taxonomy, agent role/task map, risk-control matrix, and a workflow diagram for human-gated agent support.
9. Decide during Modeling whether the paper remains framework-only or adds a small illustrative case/prototype, based on data availability and reviewer feedback.

## Expected Manuscript Package

- figures: conceptual workflow for human-gated AI-agent support in reservoir emergencies; scenario-to-agent-role map; risk evaluation workflow
- tables: dam/reservoir worker emergency problem taxonomy; emergency scenario taxonomy; agent support modes; risk/failure-mode matrix; literature cluster summary
- likely method/conceptual visuals: layered architecture showing reservoir data/models, AI agent, human operator, emergency protocols, and audit/risk controls
- claim-evidence map: every claim about agent usefulness, limitations, and risk controls mapped to literature/guidance or marked as proposed framework logic
- limitations to acknowledge: initial guidance is US-centric; framework may need validation with operators; no autonomous operational deployment; LLM/agent performance claims require empirical evaluation; real emergency data may be inaccessible
- reproducibility artifacts: literature matrix, source list, coding rubric, risk-matrix template, package paths

## Risks and Gate Notes

| Risk | Severity | Mitigation |
|---|---|---|
| Topic remains too broad across all reservoir emergencies. | major | Use taxonomy route first; narrow to flood-control emergency if literature or reviewer shows scope is unmanageable. |
| Paper could overclaim AI-agent capability in safety-critical operation. | blocker if unresolved | State human oversight and advisory-only boundary; use AI risk frameworks and EAP constraints. |
| Literature basis may not support a reservoir-specific agent novelty claim. | major | Frame contribution as integration/framework unless stronger empirical gap is verified. |
| Lack of case data could weaken manuscript. | major | Use framework or scoping-review route; add illustrative synthetic case only if clearly labeled. |
| Emergency guidance may be US-centric. | minor to major depending venue | Add international guidance if target venue requires broader applicability. |
| LLM/agent terminology may be confused with reinforcement-learning agents. | major | Define agent types explicitly and distinguish RL control-policy agents from LLM/tool-using decision-support agents. |

## Planning Gate Decision

- decision: pending Planning Reviewer critique and researcher response
- gate mode: real user gate
- decision maker: user
- date: pending
- required changes before Modeling: pending reviewer critique and user approval
- accepted limitations: pending
- unresolved user decisions: accept provisional framework-paper route; decide whether to narrow to flood-control emergency if reviewer flags overbreadth; decide whether Modeling should include a small illustrative case/prototype or remain literature/framework-based

## Acceptance Rubric for Model Stage

The Model stage can begin only if:

- the research purpose and final product are clear
- the planning depth decision is explicit
- the prior-work scan supports the proposed gap or opportunity, or its skip/defer decision is recorded with a revisit trigger
- useful prior-work patterns or skill candidates have been captured
- the required data can be accessed or a fallback data source is approved
- candidate sources have been distinguished from actually usable data
- the selected method is feasible under the user's constraints
- expected runtime and API/token cost are acceptable or capped
- the core assumptions are explicit
- expected figures or tables are defined
- unresolved risks are either mitigated or accepted by the user
- Planning Reviewer findings are fixed, deferred with triggers, rejected with reasons, or escalated for user decision
- the user has approved the Planning Gate after the researcher-agent response to Planning Review
