# AI-Native Academic Research Framework

A human-gated, skill-guided research framework for turning research questions, literature, public or local data, and domain expertise into inspectable academic research packages.

This project is designed for researchers who want AI help with planning, data/model execution, research reporting, and review, but do **not** want an opaque fully autonomous research agent. The framework is implemented as a lightweight workflow kit and keeps the human researcher in control through explicit stage packages, evidence checks, and user gates.

## What It Is

The framework is implemented through a four-stage workflow:

1. **Planning**: clarify the research purpose, run Domain Onboarding on user-supplied materials, scan prior work, check feasibility, calibrate venue/output, and produce one Approved Planning Package.
2. **Modeling**: acquire real usable data, run exploratory demos or full execution, validate outputs, produce figures/tables, and write one Modeling Package.
3. **Reporting**: package evidence, provenance, findings, uncertainties, and final deliverables such as reports, papers, slides, dashboards, web pages, software packages, or review packets.
4. **Reviewing**: run reviewer-agent critique, consolidate findings, and route issues back to the correct stage or to finalization.

Each stage ends with a gate. A real research project uses real user gates. A framework test can use synthetic gates, but they must be labeled as synthetic.

Each stage uses a maker-checker loop before the user gate: the researcher agent drafts the stage package, a separate reviewer agent critiques it, the researcher agent responds and fixes or routes the findings, and only then does the user approve, revise, or reject the gate.

When the runtime supports structured choices, gate decisions are presented as
clickable options such as approve, revise, or backtrack. The same gate can still
accept a free-form condition or correction from the user.

Planning is not just a form to fill before execution. For real research, the
researcher agent should do a focused prior-work and novelty calibration before
the full Planning Package is treated as ready. That calibration can be light,
but it should ask whether the idea has already been studied, what adjacent work
did, what gap or value remains, and whether the project is worth framing as a
paper, demo, replication, tool, dataset, or internal report. It may be skipped
or deferred only when the user explicitly chooses that route, and the package
must record the accepted risk and revisit trigger.

Modeling starts only after the Planning Gate is approved. A user confirming the
topic, research interest, or rough direction is not the same as Planning Gate
approval.

The researcher agent is responsible for leading the workflow step by step. It
should state the current stage, active package, next concrete action, and any
needed user decision whenever work begins or pauses. Users provide domain
judgment and gate decisions; they should not have to remind the agent what the
next workflow step is.

## Why This Exists

Many AI research tools can retrieve literature, write text, generate code, or automate agent loops. This framework focuses on a narrower practical problem: helping non-CS domain researchers build a traceable academic research package without losing control of evidence, claims, methods, and responsibility.

The core design choices are:

- human-gated rather than fully autonomous
- evidence-grounded rather than memory-driven
- skill-guided rather than monolithic
- execution-aware rather than prose-only
- route-aware, so problems go back to Planning, Modeling, Reporting, Reviewing, or termination
- domain-aware, so non-CS researchers can supply their own field materials at the start of Planning

## Supported Agent Configurations

This repository supports two role configurations, switchable via [WORKFLOW-CONFIG.md](WORKFLOW-CONFIG.md):

| Config | Researcher agent | Reviewer agent |
|---|---|---|
| **A** | Codex | Claude Code |
| **B** | Claude Code | Codex |

- **Codex** reads [AGENTS.md](AGENTS.md) for its role instructions.
- **Claude Code** reads [CLAUDE.md](CLAUDE.md) for its role instructions.
- To switch configs, edit one line in [WORKFLOW-CONFIG.md](WORKFLOW-CONFIG.md).

If you are a user (not an AI agent), read [USER_NOTE.md](USER_NOTE.md) first.

## Quick Start

**For users:** Read [USER_NOTE.md](USER_NOTE.md). It tells you what to say to the AI at each stage, how to provide domain materials, and how to hand off between agents.

**For the researcher agent (Codex or Claude Code):**

1. Read [WORKFLOW-CONFIG.md](WORKFLOW-CONFIG.md) to confirm your role.
2. Read [AGENTS.md](AGENTS.md) (Codex) or [CLAUDE.md](CLAUDE.md) (Claude Code).
3. Read [docs/quickstart.md](docs/quickstart.md).
4. Choose full workflow mode or smoke-test mode.
5. At the start of Planning, check for user-supplied domain materials in `artifacts/<run_id>/domain-materials/` and run Domain Onboarding if present.
6. For a real project, run a focused literature/prior-work and novelty check
   before finalizing the Planning Package. Store detailed notes outside the
   package and summarize the implications in [templates/plan-package.md](templates/plan-package.md).
7. Start from [templates/plan-package.md](templates/plan-package.md) for a real project, or [templates/smoke-test-package.md](templates/smoke-test-package.md) for a framework test.
8. Run Planning -> Modeling -> Reporting -> Reviewing using the stage specs in [docs/](docs/).
9. Record every stage output as a package; write a review request for the reviewer agent before each gate.

Researcher agents must lead one active stage at a time. Do not pre-fill
downstream stage packages before their upstream gates are approved, except as
empty scaffold placeholders.

## Repository Map

| Path | Purpose |
|---|---|
| [WORKFLOW-CONFIG.md](WORKFLOW-CONFIG.md) | Switch between Config A (Codex=researcher) and Config B (Claude Code=researcher) |
| [AGENTS.md](AGENTS.md) | Codex instructions — researcher role (Config A) or reviewer role (Config B) |
| [CLAUDE.md](CLAUDE.md) | Claude Code instructions — reviewer role (Config A) or researcher role (Config B) |
| [USER_NOTE.md](USER_NOTE.md) | User guide: how to interact with the agents, gate language, handoff scripts |
| [docs/](docs/) | Stage specifications, handoff rules, skill strategy, reviewer-agent prompts, quick start, and paper draft |
| [templates/](templates/) | Package templates for Planning, Modeling, Reporting, Reviewing, smoke tests, and research-skill cards |
| [skills/](skills/) | Workflow-native skills used inside stages |
| [.claude/commands/](\.claude/commands/) | Claude Code slash commands for all seven workflow-native skills |
| [examples/](examples/) | Worked examples, smoke tests, and per-example run notes |
| [notes/](notes/) | Cross-run open questions and development material |

## Stage Outputs

| Stage | Specification | Main package |
|---|---|---|
| Planning | [docs/plan-stage.md](docs/plan-stage.md) | [templates/plan-package.md](templates/plan-package.md) |
| Modeling | [docs/model-stage.md](docs/model-stage.md) | [templates/model-package.md](templates/model-package.md) |
| Reporting | [docs/reporting-stage.md](docs/reporting-stage.md) | [templates/reporting-package.md](templates/reporting-package.md) |
| Reviewing | [docs/review-stage.md](docs/review-stage.md) | [templates/review-package.md](templates/review-package.md) |
| Smoke-test mode | all stage specs | [templates/smoke-test-package.md](templates/smoke-test-package.md) |

See [docs/stage-handoffs.md](docs/stage-handoffs.md) for package flow, backtracking rules, and gate semantics.

## Skills

The workflow uses small reusable internal skills rather than one all-purpose agent. Each skill has a `SKILL.md` in `skills/` and a matching Claude Code slash command in `.claude/commands/`. External tools and installable skills may still be used for literature search, analysis, citation management, writing, or visualization; the internal skills keep those outputs tied to stage packages, evidence records, review routes, and gates.

| Skill | Slash command | Used mainly in | Responsibility | External relationship |
|---|---|---|---|---|
| [venue-calibration](skills/venue-calibration/SKILL.md) | `/venue-calibration` | Planning, Reporting | Calibrate target journal, conference, preprint, policy note, or other output route | Wraps venue pages, templates, and exemplars |
| [research-skill-card-distiller](skills/research-skill-card-distiller/SKILL.md) | `/research-skill-card-distiller` | Planning | Convert retrieved papers or user-supplied domain materials into reusable research-skill cards | Uses external literature/deep-research outputs as input when useful |
| [model-contract-runner](skills/model-contract-runner/SKILL.md) | `/model-contract-runner` | Modeling | Execute the approved modeling contract with acquisition checks and bounded loops | Orchestrates Python, R, Jupyter, APIs, containers, or domain packages |
| [figure-table-narrative](skills/figure-table-narrative/SKILL.md) | `/figure-table-narrative` | Reporting | Decide visual purpose, evidence status, claim alignment, and caption limits | Hands method/conceptual visuals to CCF-Figure or diagram tools; hands empirical visuals to Model/plotting tools |
| [claim-evidence-mapper](skills/claim-evidence-mapper/SKILL.md) | `/claim-evidence-mapper` | Reporting, Reviewing | Tie research-output claims to citations, artifacts, results, or limitations | May use citation/retrieval tools, but keeps the final map internal |
| [route-aware-reviewer](skills/route-aware-reviewer/SKILL.md) | `/route-aware-reviewer` | Reviewing | Stress-test the research output and route findings to the correct stage | May use external reviewer simulation or checklists |
| [gate-manager](skills/gate-manager/SKILL.md) | `/gate-manager` | All stages | Record gate decisions and stage transitions | Mostly framework-native |

See [docs/skill-strategy.md](docs/skill-strategy.md) for when to use external tools versus internal skills, and for Claude Code built-in capability coverage when Claude Code is the researcher (Config B).

## Domain Onboarding

Non-CS researchers often have domain materials the AI has not seen: institutional reports, field-specific papers, data dictionaries, or policy documents. The Planning stage begins with a **Domain Onboarding** step that reads user-supplied materials, extracts a Domain Knowledge Summary, and produces skill cards — before any literature scan or plan writing begins.

Place domain materials in `artifacts/<run_id>/domain-materials/` and tell the researcher agent at the start of Planning. See [USER_NOTE.md](USER_NOTE.md) for the exact prompt to use.

## Cross-Agent Handoff

The researcher and reviewer agents communicate through two files written to `artifacts/<run_id>/`:

- `review-request.md` — written by the researcher when a stage package is ready for critique
- `reviewer-critique.md` — written by the reviewer with a structured findings table

See [docs/reviewer-agents/cross-agent-handoff.md](docs/reviewer-agents/cross-agent-handoff.md) for the full protocol and file formats.

This repository also includes optional one-command wrappers for single-window
workflows:

- `scripts/run_reviewer_claude.ps1` lets a Codex researcher call Claude Code as reviewer under Config A.
- `scripts/run_reviewer_codex.ps1` lets a Claude Code researcher call Codex as reviewer under Config B.

Both wrappers preserve the same file protocol: the researcher still writes
`review-request.md`, the reviewer writes `reviewer-critique.md`, and the
researcher remains responsible for triage and gate presentation.

## Examples

Example folders should follow [docs/example-organization.md](docs/example-organization.md). The public v0.1 repository keeps examples lightweight so private notes, large generated artifacts, and copyright-sensitive materials are not accidentally published.

- [examples/](examples/): example organization notes and planned case-study slots.

## Paper

> **A Human-Gated, Skill-Guided Framework for AI-Native Academic Research**

A companion paper is in preparation. It positions the repository as a practical, inspectable framework rather than a claim of full scientific automation. The draft is not yet public.

## Current Status

This is an early research-framework repository. The workflow docs, templates, skills, and examples are present. The next milestone is a cleaner public v0.1 release with:

- polished paper draft
- one reproducible smoke test
- one domain case study
- repository-level citation and license metadata
- clearer evaluation plan

## License

MIT License. See [LICENSE](LICENSE).
