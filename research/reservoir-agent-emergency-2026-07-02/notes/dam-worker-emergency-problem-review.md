# Dam/Reservoir Worker Emergency Problem Review

- Stage: Planning support note
- Run ID: reservoir-agent-emergency-2026-07-02
- Researcher agent: Codex
- Date: 2026-07-02
- Evidence status: focused planning review, not a systematic review

## Purpose

This note reframes the paper around the operational problems faced by dam owners,
reservoir operators, water managers, dam-safety engineers, and emergency
coordination staff during reservoir operation emergencies. The goal is to define
the human work problem before assigning possible AI-agent support modes.

## Sources Screened

Primary official/guidance sources:

- FEMA/ICODS, *Federal Guidelines for Dam Safety: Emergency Action Planning for
  Dam Owners* (FEMA P-64, hosted by FERC):
  `https://www.ferc.gov/sites/default/files/2020-04/fema-64.pdf`
- FERC, Emergency Action Plan Program:
  `https://www.ferc.gov/emergency-action-plan-eap-program`
- ASDSO, Emergency Action Planning:
  `https://damsafety.org/dam-owners/emergency-action-planning`
- USACE, *Management of Water Control Systems* (EM 1110-2-3600):
  `https://www.publications.usace.army.mil/portals/76/publications/engineermanuals/em_1110-2-3600.pdf`
- USACE, EC 1110-2-6075 on inundation maps and EAPs:
  `https://www.publications.usace.army.mil/Portals/76/Users/182/86/2486/EC%201110-2-6075.pdf?ver=N6pf63wzqYGbRM_XgvRkgw%3D%3D`
- British Columbia, *2026 Drought and Water Scarcity Operations Plan*:
  `https://www2.gov.bc.ca/assets/gov/environment/air-land-water/water/drought-info/drought_and_water_scarcity_operations_plan.pdf`

Selected scholarly/technical sources:

- Shawwash, *Risk Informed Decision-Making Framework for Operating Reservoirs
  Under Flooding Conditions*:
  `https://www.iahr.org/library/info?pid=17734`
- Liu et al., *Real-time reservoir flood control operation enhanced by data
  assimilation*:
  `https://d-nb.info/1214815596/34`

## High-Level Finding

Dam/reservoir emergency work is not one decision. It is a compressed workflow
of detection, classification, forecasting, release or mitigation choice,
coordination, warning, documentation, public communication, and post-event
learning. The worker's central problem is not "find the optimal release" alone.
It is to make time-critical, legally constrained, socially visible, and
safety-critical judgments under uncertainty while coordinating several agencies
that own different pieces of authority.

This matters for the paper: AI agents should be evaluated as support for a
human emergency work system, not as autonomous operators.

## Problem Taxonomy for Dam/Reservoir Workers

### 1. Detecting and Classifying the Emergency

Workers must identify abnormal reservoir levels, structural distress,
instrumentation signals, inspection observations, forecasted inflow threats, or
other triggering events. FEMA P-64 treats timely detection, evaluation, and
classification as a core EAP element. It also distinguishes severe failure
conditions from developing failure conditions and non-failure emergency
conditions.

Operational difficulty:

- Evidence can be partial, noisy, or contradictory.
- Waiting too long can reduce warning and response time.
- Declaring an emergency too early or too late can create operational,
  reputational, and public-safety consequences.
- Terminology has to be shared across dam staff and emergency-management
  agencies, otherwise notifications may not trigger the intended actions.

AI-agent implication:

- Safer support: anomaly triage checklist, evidence collation, EAP
  classification lookup, missing-data prompts, escalation reminder.
- High-risk support: independently declaring emergency status or downgrading an
  emergency classification.

### 2. Maintaining Real-Time Situational Awareness

USACE guidance emphasizes intensive monitoring and reanalysis during
emergencies, including current hydrometeorological conditions, observed versus
forecast conditions, river/reservoir data, and rapidly changing events. Real
operations depend on both models and operators' judgment.

Operational difficulty:

- Operators must keep a live mental model of pool elevation, inflow, outflow,
  gate status, downstream stage, forecasts, and constraints.
- Real-time observations can contain error. A reservoir-operation study notes
  that directly using limited observations can propagate error, including
  unrealistic inflow estimates.
- Information comes from multiple organizations, systems, and formats.

AI-agent implication:

- Safer support: dashboard summarization, source provenance table, discrepancy
  flags, observation/forecast comparison, event timeline.
- High-risk support: hiding uncertainty behind a single confident summary.

### 3. Forecasting Hazard Under Uncertainty

Flood emergencies require meteorological and hydrologic forecasts, sometimes
ensemble forecasts, and may require inundation mapping. USACE guidance notes
that forecasts depend on assumptions about future meteorological inputs and that
ensemble forecasts help represent uncertainty and possible extremes. FEMA/FERC
guidance requires dam-break assumptions such as breach size, formation time,
storage, hydraulic head, fair-weather versus flood-condition breach, and
possible domino effects on downstream dams.

Operational difficulty:

- Forecast uncertainty expands over time and can alter release timing,
  warning urgency, and evacuation consequences.
- Inundation results depend on scenario assumptions.
- Workers must communicate not just "what will happen" but what could happen
  under plausible alternatives.

AI-agent implication:

- Safer support: scenario inventory, assumption tracker, "what changed since
  last forecast" summary, uncertainty-language drafting.
- High-risk support: treating one forecast or one inundation layer as definitive.

### 4. Choosing or Advising Operations Under Conflicting Objectives

Reservoirs are usually multi-purpose systems: flood-risk management, navigation,
hydropower, water supply, irrigation, recreation, water quality, ecosystem
flows, and public safety can conflict. USACE explicitly shifted from "flood
control" language toward "flood risk management" because structures reduce risk
but cannot eliminate it. Emergency releases may protect the dam or upstream
pool while increasing downstream impacts.

Operational difficulty:

- The worker may need to balance upstream dam safety, downstream flood risk,
  water supply, power, environmental flows, and legal operating constraints.
- Deviations from approved water-control plans may require review or approval.
- The "best" technical alternative can be unacceptable if it violates authority,
  public-warning timing, or downstream constraints.

AI-agent implication:

- Safer support: compare alternatives against approved constraints, list tradeoffs,
  identify which objective each alternative sacrifices, prepare decision logs.
- High-risk support: recommending a release as "optimal" without authority,
  uncertainty, and consequence framing.

### 5. Coordinating Roles, Authorities, and Chains of Command

EAP guidance divides responsibilities across dam owners, local/state emergency
managers, public information officers, warning authorities, evacuation
authorities, engineers, and regulators. Dam owners generally notify and support;
local authorities usually own warning and evacuation. FEMA/FERC guidance says
coordination is essential to avoid over- or under-reaction.

Operational difficulty:

- Many actors have partial authority.
- Notification priority matters.
- Night, weekend, holiday, or backup-staff conditions can change who can be
  reached.
- Emergency Operations Centers and Incident Command structures may need
  project-specific technical interpretation.

AI-agent implication:

- Safer support: notification checklist, contact-role mapping, status-update
  drafting, meeting/action-item tracker.
- High-risk support: bypassing official notification hierarchy or contacting
  public channels without authorization.

### 6. Warning, Evacuation Interface, and Public Communication

Dam workers may not be the evacuation authority, but they provide the technical
information that makes evacuation planning possible. Inundation maps show
areas, travel times, depths, and flood peaks used by emergency managers.
Guidance also stresses media/public information and misinformation control.

Operational difficulty:

- The public may not know they are downstream of a dam.
- Inundation maps must be accurate enough for action and communicated in usable
  terms.
- Some map/supporting data may involve security restrictions.
- False rumors or inconsistent messages can harm response.

AI-agent implication:

- Safer support: convert technical status into approved message drafts for PIO
  review, produce plain-language summaries, track message consistency.
- High-risk support: issuing public warnings, evacuation instructions, or map
  interpretations without official approval.

### 7. Handling Drought and Water-Supply Emergencies

Drought emergencies are slower than dam-breach emergencies but still operationally
hard. USACE requires drought contingency plans for projects with controlled
storage. B.C.'s drought plan emphasizes timely, clear communication with water
users, conservation, regulatory measures, and local authority responsibility.

Operational difficulty:

- Decisions unfold over weeks or months, but consequences accumulate.
- Operators face competing rights, water-supply needs, ecological requirements,
  and public expectations.
- Communication and cooperation are central because voluntary conservation and
  regulatory measures depend on trust.

AI-agent implication:

- Safer support: water-scarcity status synthesis, stakeholder-message matrix,
  trigger-condition monitoring, conservation-measure option tables.
- High-risk support: making allocation or restriction decisions without legal and
  authority checks.

### 8. Managing Multi-Reservoir and Cascading System Effects

Reservoir systems and river basins can include upstream and downstream dams,
hydropower dispatchers, multiple jurisdictions, and potentially domino effects.
FEMA/FERC dam-break guidance says downstream dams may need to be considered
case-by-case if failure of one dam could cause failure downstream.

Operational difficulty:

- An action at one reservoir may shift risk to another reach or project.
- Systemwide storage and releases can interact with hydropower, navigation,
  environmental, and local flood constraints.
- The emergency can propagate faster than coordination channels.

AI-agent implication:

- Safer support: dependency graph, cascade checklist, upstream/downstream status
  monitor, cross-reservoir constraint table.
- High-risk support: optimizing one project without accounting for downstream
  authority and consequences.

### 9. Site Security, Staff Safety, and Continuity of Operations

EAP guidance includes security provisions at and around the dam during an
emergency, on-site monitoring, status reports, and continuity of communication.
The affected operational area may be dangerous to staff.

Operational difficulty:

- Staff may need to inspect or operate under hazardous physical conditions.
- Communications, power, access roads, and equipment may be degraded.
- The operator must protect staff while maintaining enough observation and
  control capability.

AI-agent implication:

- Safer support: staff-safety checklist, access/status tracker, communication
  redundancy log.
- High-risk support: asking staff to collect data or inspect areas without
  safety authority and local conditions.

### 10. Termination, Recovery, and Learning

Ending an emergency is also a decision problem. FEMA/FERC guidance separates
termination of the dam-safety condition from termination of evacuation or
disaster response, and calls for after-action review covering actions,
deficiencies, staffing, equipment, materials, and leadership.

Operational difficulty:

- Conditions may stabilize at the dam while evacuation or response continues.
- Recovery responsibilities can outlast the immediate operation.
- Lessons learned must be captured before staff memory fades.

AI-agent implication:

- Safer support: after-action evidence organizer, timeline reconstruction,
  unresolved-issue tracker, EAP revision checklist.
- High-risk support: declaring emergency termination without authority.

## Cross-Cutting Worker Burdens

Across the scenarios, the same burdens recur:

| Burden | What it means in practice | Why it matters for AI-agent design |
|---|---|---|
| Time pressure | Some decisions must be made before full information is available. | Agent must surface uncertainty and escalation, not wait for perfect data. |
| Authority boundaries | Dam owner, emergency manager, NWS, regulator, and public information roles differ. | Agent must know who can decide, notify, warn, evacuate, or speak publicly. |
| Data uncertainty | Forecasts, gauges, inspections, models, and maps can conflict. | Agent must preserve provenance and confidence, not merge all inputs into one voice. |
| Multi-objective conflict | Flood risk, dam safety, water supply, ecology, hydropower, and public safety compete. | Agent should expose tradeoffs rather than optimize a hidden objective. |
| Consequence severity | A small mistake can endanger life downstream or damage trust. | High-consequence tasks need human approval, logs, and conservative defaults. |
| Communication load | Technical status must move through many people quickly. | Agent can help draft, route, and track messages, but not replace authorized communication. |
| Preparedness gap | EAPs and exercises can become outdated or unfamiliar. | Agent can support drills, retrieval, role rehearsal, and after-action updates. |

## Implications for the Paper

The paper should not start from the question "what can AI agents automate?" It
should start from "what emergency work problems do dam/reservoir workers face?"
Then it can assign agent support modes by risk tier.

Suggested paper framework:

1. **Emergency scenario layer**: flood operation, drought supply, dam-safety
   failure risk, warning/evacuation interface, sensor/forecast conflict,
   multi-reservoir coordination.
2. **Worker problem layer**: detect/classify, monitor, forecast, compare
   alternatives, coordinate, communicate, document, terminate/recover.
3. **Agent support layer**: retrieve, summarize, check, compare, draft, audit,
   simulate under human-gated constraints.
4. **Risk-control layer**: human authority, source provenance, uncertainty
   display, role boundary, audit log, escalation threshold, fallback procedure.

## Preliminary Risk Tiering for Agent Support

| Agent support mode | Worker problem helped | Risk tier | Rationale |
|---|---|---|---|
| EAP/protocol retrieval | Classification, notification, role lookup | low to moderate | Useful if source-cited and reviewed; dangerous if it cites outdated plan text. |
| Situation summary | Monitoring, shift handoff, EOC briefing | moderate | Can reduce cognitive load, but must preserve uncertainty and source provenance. |
| Forecast/observation discrepancy flag | Situational awareness | moderate | Helpful as a warning; should not decide which source is correct without validation. |
| Scenario comparison table | Release/mitigation alternatives | high | Directly influences high-consequence decisions; must be advisory and reviewed. |
| Public message draft | Public communication | high | Must be approved by PIO/authorized authority. |
| Evacuation recommendation | Warning/evacuation interface | very high | Usually outside dam-owner authority and life-safety critical. |
| Autonomous gate/release command | Physical operation | unacceptable for this paper's scope | User explicitly excludes autonomous open/close/release decisions; requires validated control and authority not assumed here. |

## Planning Package Changes Recommended

- Make "dam worker emergency problem taxonomy" a first Modeling output.
- Treat "AI agent role" as secondary to worker problem and authority boundary.
- Add a source-coding variable for `worker_problem`.
- Add a source-coding variable for `authority_boundary`.
- Add a risk-matrix row for communication/public-warning tasks, not only release-operation tasks.
- Preserve the explicit boundary: AI agent is decision support under human supervision, not autonomous release control.
