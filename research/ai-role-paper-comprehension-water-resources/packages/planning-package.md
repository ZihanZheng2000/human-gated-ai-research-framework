# Approved Plan Package

## Planning Workflow Identity

- package status: approved
- Planning Researcher: Codex
- Planning Reviewer: skipped
- reviewer file: `docs/reviewer-agents/planning-reviewer-agent.md`
- reviewer mode: skipped
- Planning Review status: skipped for now
- researcher-agent response status: not applicable yet
- user Planning Gate status: approved
- workflow mode: step-by-step discussion
- gate mode: real user gates
- run ID: `ai-role-comprehension-plan-v1`

## User-Need Profile

| User-need field | Proposed answer | Common choices | User correction or addition |
|---|---|---|---|
| research area | AI-assisted scholarly reading; water-resources research communication; simulated reader comprehension | water resources / science education / human-AI interaction / bibliometrics | pending user confirmation |
| intended output | research plan first; empirical demo report later | paper / report / demo / tool / manuscript package / proposal | confirmed by user |
| workflow mode | step-by-step discussion | auto-until-needed / step-by-step discussion | confirmed by user |
| intended research product | experimental workflow plus evidence about comprehension differences and hint effects | empirical finding / method / benchmark / workflow demo / manuscript package | confirmed by user |
| research purpose | test whether AI-simulated readers show different comprehension levels across role profiles, and whether explanations improve comprehension | discover pattern / build method / validate intervention / compare alternatives / workflow test | confirmed by user |
| practical success criterion | a reproducible pilot showing role-level differences and hint-related improvement on paper-question tasks | evidence for a claim / reusable workflow / proof of feasibility / publishable package | confirmed by user |
| target audience or venue | academic readers interested in AI, science communication, education, and water-resources research workflows | domain experts / education researchers / HCI readers / internal decision-makers | pending user confirmation |
| data/source direction | use one public open-access water-resources paper for a small demo | public papers / provided papers / literature only / API data / no empirical data | confirmed by user |
| available data | candidate public article identified: Van Loon et al. 2016 in Hydrology and Earth System Sciences | user-provided / public source known / to be found | provisionally selected |
| constraints | avoid overclaiming about real humans unless validated; manage API/model cost; use inspectable scoring rubrics | time / tooling / runtime / API-token / privacy / licensing / language / method complexity | confirmed by user |
| novelty expectation | small demo first; no publication-level novelty claim yet | publication novelty / useful replication / demo / internal evidence | confirmed by user |
| avoid-list | avoid claiming that role-play equals real human cognition without human validation | avoid paid APIs / private data / black-box methods / specific domains | confirmed by user |
| gate mode | real user gates | real user gates / synthetic gates / mixed | inferred from real project |
| reviewer strategy | skip reviewer for now | use reviewer / skip reviewer | confirmed by user |

## Domain Onboarding

- status: skipped for now - no user materials provided yet
- materials read: 0 files
- potential skill patterns noted: 0
- downstream implications flagged: yes

## Resolved Decision-Changing Unknowns

| Unknown or ambiguity | Provisional answer | User correction or resolution | Effect on plan |
|---|---|---|---|
| Whether this studies real humans or AI-simulated personas | Treat as an AI-simulation experiment first, with real-human claims only as future validation | confirmed by user: use AI-simulated readers with different cognitive levels and knowledge reserves | Controls claim level and ethics/validation burden |
| Whether the paper corpus is user-provided or publicly collected | Start with one publicly found water-resources article for a small demo | confirmed by user | Controls acquisition plan, licensing, and feasibility |
| Whether "omniscient author" means actual paper author or a gold-standard evaluator | Treat as a gold-standard author/evaluator role built from the paper text and answer key | pending user confirmation | Controls scoring design and validity risks |

## Demo Scope Confirmed So Far

- Reader roles: four simulated readers, one per audience group.
- Evaluator role: one omniscient author / gold-standard evaluator.
- Corpus scale: one publicly accessible water-resources article for the first demo.
- Task design: ten comprehension questions from simple to difficult.
- Intervention: author-provided explanatory hints, followed by reassessment.
- Claim boundary: demo tests AI-simulated role behavior only; it does not establish real human comprehension differences.

## Planning Reviewer Critique

External reviewer pass skipped for now.

- skipped reason: user selected `Skip reviewer` during Pre-Planning Session Setup.
- risk accepted: the Planning package may miss methodological risks that a separate reviewer would flag.
- revisit trigger: before Planning Gate approval if the plan is intended for publication, human-subject inference, or costly full-scale execution.

## Researcher-Agent Response to Planning Review

Not applicable yet because reviewer pass is skipped for now.

## Planning Gate Decision

- decision: approve for Modeling
- gate mode: real user gate
- decision maker: user
- date: 2026-07-04
- required changes before Modeling: none
- accepted limitations: single-paper demo; AI-simulated readers only; reviewer pass skipped; no publication-level novelty claim
- unresolved user decisions: none blocking Modeling

## Planning Work Queue

1. Confirm user-need profile and claim boundary. Completed for demo scope.
2. Decide source strategy for pilot papers. Completed provisionally: one public open-access HESS article.
3. Define reader-role taxonomy. Drafted for user confirmation.
4. Define question-generation and answer-scoring design. Drafted for user confirmation.
5. Run focused prior-work scan on AI personas, paper comprehension, automated assessment, and water-resources literature difficulty. Deferred for demo; required before publication-scale claims.
6. Select route, feasibility plan, and Modeling acceptance rubric. Drafted for Planning Gate.

## Prior Work Scan

A focused Planning scan was completed after the user correctly pointed out that
the idea should be checked against existing work before Modeling. Detailed notes
are in `research/ai-role-paper-comprehension-water-resources/notes/focused-literature-scan.md`.

This was not a systematic review. It is sufficient for a small demo, but not
sufficient for a publication-level novelty claim.

| Cluster or source | What has been done | Method or evidence pattern | Relevance to this project |
|---|---|---|---|
| Multi-perspective scientific machine reading comprehension | SciMRC constructs beginner, student, and expert scientific-paper QA perspectives across 741 papers and 6,057 QA pairs | Perspective-specific QA, evidence annotation, full-text scientific MRC | Closest prior work; shows our core premise is already recognized, but our role-play + hint demo remains distinct |
| LLMs simulating human participants/personas | Argyle et al. and Aher et al. use LLMs to simulate human samples or human-subject studies | Prompt-conditioned simulated respondents; comparison to human-study patterns | Supports AI-simulation approach but requires distortion and validity warnings |
| Risks of replacing humans with LLM personas | Wang et al. and Cheng et al. warn that LLM personas can flatten, misportray, or stereotype groups | Critical analysis and empirical persona-prompt tests | Requires strict claim boundary: simulated readers are not real readers |
| Automated short-answer scoring with LLMs | AutoSCORE and related work show promise but warn about prompt sensitivity, rubric mismatch, and interpretability | Rubric/component-based grading | Supports structured component scoring rather than free-form evaluator impressions |
| Hints, explanations, and accessible summaries | ITS and education work studies adaptive hints, explanations, and accessible summaries for research-literature engagement | Hint/explanation interventions; pre/post or perception/learning measures | Supports testing author hints but suggests effects may vary by prior knowledge |

## Planning Depth Decision

| Item | Decision | Reason | Downstream implication |
|---|---|---|---|
| idea maturity | partly formed | User has a clear experimental concept but source selection, scoring, and validity design need calibration | Use demo-first Modeling |
| literature/prior-work scan depth | light completed for demo | User requested a simple test, then asked to check prior work before Modeling | Enough for demo; full scan needed before manuscript-scale claims |
| novelty assessment depth | light completed for demo | Closest prior work exists, especially SciMRC; exact water-resources role-play + hint design not found in focused scan | Frame as method/workflow demo, not broad novelty claim |
| venue/output calibration depth | deferred | No target venue selected yet | Treat output as internal demo report |
| revisit trigger | before scale-up | Literature scan required before adding more papers, journals, or stronger claims | Planning addendum before full-scale study |

## Candidate Research Plans Considered

| Plan | RQ | Data | Method | Venue/output fit | Decision |
|---|---|---|---|---|---|
| Small single-paper demo | In an AI-simulated reading experiment, do role profiles with different knowledge levels show different apparent comprehension, and do author hints improve answers? | One open-access water-resources paper | 4 reader roles + 1 author/evaluator, 10 questions, pre/post hint scoring | Internal demo / feasibility report | selected |
| Multi-paper journal-difficulty study | How does simulated reader comprehension vary across journal/article difficulty levels? | Corpus across water-resources journals | Multi-paper sampling, difficulty coding, role evaluation | Manuscript-scale empirical study | future work |
| SciMRC-style benchmark adaptation | Can a water-resources scientific-MRC benchmark be built with novice/student/expert/advisor perspectives? | Multiple water-resources articles plus perspective-specific QA | Dataset construction and model evaluation | Stronger NLP/education research route | future work after demo |

## Feasibility and Cost Check

| Item | Assessment | Evidence or test | Fallback |
|---|---|---|---|
| data access | feasible for pilot | HESS article page exposes PDF and XML, DOI, license, and citation metadata | choose another open-access HESS or MDPI Water article |
| text/table/image/API extractability | feasible | Article has full-text XML and PDF download links | use article webpage text if PDF extraction fails |
| candidate sources vs usable acquired data | candidate only until Modeling acquisition succeeds | Candidate article identified but not yet acquired into project artifacts | acquire XML/PDF during Modeling |
| demo scale | 1 article, 4 reader roles, 1 author/evaluator, 10 questions, two answer rounds | User requested simple test | reduce to 5 questions if runtime/cost is high |
| full-study scale | deferred | Not needed for first demo | plan addendum before scaling |
| runtime/storage burden | low | One article and generated answer tables | no special fallback |
| API/token cost | moderate but bounded | Five role passes plus scoring and hint pass; exact cost depends on model and article length | use article sections or abstract-only pilot |
| external tool or skill feasibility | feasible | Use existing workflow package discipline; no new skill needed yet | create project-specific prompt/rubric artifact if repeated |
| licensing/privacy/ethics | low risk for open-access article; human-subject claims prohibited | HESS page reports Creative Commons license | use only openly licensed article text |

## Data Source Identity

| Role | Source name or URL | Version/date/access date | License/access status | Notes |
|---|---|---|---|---|
| raw data host | `https://hess.copernicus.org/articles/20/3631/2016/` plus linked PDF/XML | published 2016-09-08; access date 2026-07-04 | HESS page states Creative Commons Attribution 3.0 for article | Candidate source until acquired in Modeling |
| official data source | Hydrology and Earth System Sciences / Copernicus Publications | HESS 20, 3631-3650, 2016 | open access | Journal article page |
| documentation source | HESS article page and metadata | access date 2026-07-04 | public | Includes DOI, citation, PDF/XML links |
| citation source | DOI `10.5194/hess-20-3631-2016` | 2016 | public citation metadata | Use for reporting citation |

## Selected or Confirmed Research Route

| Route element | Selected value | Evidence or reason | User confirmation status |
|---|---|---|---|
| working research question | In an AI-simulated reading experiment, do role profiles with different knowledge levels show different apparent comprehension of a water-resources paper, and do author hints improve their answers? | Matches user-stated goals and demo request | approved |
| intended output and claim level | Small internal demo report with limited AI-simulation claim | User requested simple test; no human generalization | approved |
| data/source strategy | One public open-access HESS article: Van Loon et al. 2016 | Open-access, water-resources/hydrology, suitable conceptual difficulty | approved |
| method family | Role-prompted LLM reader simulation with author-generated question ladder, rubric scoring, hints, and pre/post comparison | Directly implements user concept | approved |
| feasibility status and fallback | Feasible; fallback to another open-access article or abstract-only pilot | PDF/XML available | approved |
| target venue/audience/output mode | Internal demo / feasibility report | No venue selected yet | approved |
| future-work boundary | Multi-journal corpus, real-human validation, and publication-level novelty claims are out of first demo scope | Prevents overclaiming | approved |

## External Tool and Skill Scan

| Candidate tool, package, template, or skill | Workflow task | Maturity or reason to trust | Output to bring back | Cost/access/limits | Decision |
|---|---|---|---|---|---|
| HESS article PDF/XML | source acquisition | Official journal-hosted open-access article | article text and metadata | open access; extraction must be logged | reuse |
| Current repository workflow | stage control | Explicit package and gate rules | planning/model/report packages | local workflow only | reuse |
| Academic Research Suite for Codex | research workflow support | Available Codex skill for academic workflow reasoning | notes only; not a gate substitute | must not replace repository gates | adapt lightly |

## Skill Construction Decision

| Skill need | External alternative checked | Why external option is sufficient or insufficient | Decision | Promotion status |
|---|---|---|---|---|
| Role-reader experiment prompts and scoring rubric | Existing workflow plus project notes | Sufficient for one demo; may become reusable if repeated across papers | no core skill yet; create project-specific artifacts during Modeling if needed | project-specific candidate |

## Approved Research Question

`In an AI-simulated reading experiment, do role profiles with different knowledge levels show different apparent comprehension of a water-resources research article, and do author-provided hints improve their answers?`

## Working Title

`AI-Simulated Reader Roles for Testing Water-Resources Paper Comprehension: A Single-Article Demo`

## Hypotheses or Expected Claims

- Higher-knowledge simulated roles will produce more complete and accurate answers before hints.
- Author-provided hints will improve answer quality, especially for lower-knowledge simulated roles.
- Any result will be limited to AI-simulated role behavior and will not be treated as direct evidence about real human readers.

## Data Plan

- primary data source: Van Loon et al. 2016 HESS article on drought in a human-modified world
- backup data source: another open-access HESS or water-resources article with PDF/XML
- exact raw data host: `https://hess.copernicus.org/articles/20/3631/2016/`
- official data source: Hydrology and Earth System Sciences / Copernicus Publications
- documentation source: HESS article page
- data version or access date: published 2016-09-08; accessed 2026-07-04
- license/access status: article page states Creative Commons Attribution 3.0 License
- acquisition success rule: article text counts only after PDF or XML is saved under project artifacts and readable enough to generate grounded questions and scoring keys
- minimum viable data scale: one article, 10 questions, 4 reader roles, 2 answer rounds
- full-study data scale: deferred
- key variables: reader role, question difficulty, pre-hint answer score, hint content, post-hint answer score, score delta, evaluator notes
- unit of analysis: role-question attempt
- time/spatial coverage: not applicable for demo analysis; article topic concerns drought in the Anthropocene
- access or licensing concerns: cite and retain source/license metadata; do not treat candidate link as acquired data

## Method Blueprint

1. Acquire and preserve the article text from the selected HESS article.
2. Create five role prompts: undergraduate, master's student, PhD student, advisor/senior researcher, and omniscient author/evaluator.
3. Author/evaluator creates 10 ordered comprehension questions and an answer key, using difficulty tiers informed by SciMRC-style perspective differences.
4. Each simulated reader answers the 10 questions without hints.
5. Author/evaluator scores each answer using a fixed component-based rubric.
6. Author/evaluator provides targeted hints/explanations.
7. Each simulated reader answers again.
8. Score post-hint answers using the same rubric and summarize pre/post score changes.
9. Record limitations, especially that role prompts do not validate real human comprehension.

## Expected Manuscript Package

- figures: small role-by-score comparison chart; optional pre/post delta chart
- tables: question ladder; role definitions; pre/post answer scores; evaluator notes
- likely method/conceptual visuals: workflow diagram of author-question-reader-hint-scoring loop
- claim-evidence map: demo claims tied to score table and generated answer logs
- limitations to acknowledge: single article, simulated readers, possible model self-consistency bias, evaluator and readers may share model family, no human validation
- reproducibility artifacts: article source record, prompts, answer logs, scoring rubric, run log

## Risks and Gate Notes

| Risk | Severity | Mitigation |
|---|---|---|
| LLM role-play may reflect prompt compliance rather than real knowledge differences | high | Keep claim boundary to AI-simulated readers; no human generalization |
| Same model may generate questions, hints, answers, and scoring, creating evaluator bias | medium | Preserve prompts and logs; in future use independent model or human scoring |
| One article cannot represent water-resources literature difficulty | medium | Label as demo only; scale later with explicit corpus sampling |
| Article extraction may fail | low | Use XML, PDF, or another open-access article fallback |
| Prior work already covers part of the idea | medium | Cite SciMRC and LLM-persona literature; position demo as water-resources workflow adaptation with hint intervention |

## Acceptance Rubric for Model Stage

The Model stage can begin only if:

- the user approves the single-paper demo route;
- the article is acquired as usable text, not just linked;
- the four reader roles and author/evaluator role are fixed before answer generation;
- the 10-question ladder and scoring rubric are produced before reader answers are judged;
- the Planning notes acknowledge closest prior work, especially SciMRC and LLM human-simulation studies;
- pre-hint and post-hint answer logs are preserved;
- score changes are summarized without claiming real human-reader validity;
- limitations are carried into Reporting.
