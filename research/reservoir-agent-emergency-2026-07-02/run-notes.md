# Run Notes

## Run Identity

- Run name: reservoir-agent-emergency-2026-07-02
- Date: 2026-07-02
- Mode: real project
- Gate mode: real user gates
- Topic or task: AI agents for reservoir operation emergencies
- Stage coverage: Planning in progress

## Useful Observations

- Observation: The user prefers stepwise discussion over one-shot package filling.
- Stage: Planning
- Why it helped: It keeps the research collaborative and prevents the Planning package from becoming a large undiscussed document.
- Evidence or example from this run: The first Planning draft and domain review were paused and reclassified as preliminary scaffold/supporting notes.
- Possible permanent home: AGENTS.md, docs/plan-stage.md, docs/stage-handoffs.md

## Friction or Failures

- Issue: Initial project files were created in root-level `packages/` and `artifacts/`.
- Stage: Planning
- What happened: The project did not yet have a dedicated `research/<name>/` folder.
- Root cause, if known: The workflow had example organization rules but not a clear real-research project folder rule.
- Fix used during this run: Added `docs/research-organization.md` and migrated this project under `research/reservoir-agent-emergency-2026-07-02/`.
- Should this become a formal rule? yes

## Candidate Formal Updates

| Candidate update | Target file | Reason | Evidence from this example | Decision |
|---|---|---|---|---|
| Create one folder per real research project under `research/<research-name>/` | `docs/research-organization.md` | Keeps packages, notes, artifacts, and deliverables project-scoped | Reservoir project migration | update formal docs |
| Prefer stepwise Planning for broad topics | `AGENTS.md`, `docs/plan-stage.md` | Better matches user collaboration preference | User feedback after one-shot Planning draft | update formal docs |

## After-Action Review

- What should be repeated next time? Create the `research/<research-name>/` skeleton before substantive Planning.
- What should be avoided next time? Do not send a full Planning package to reviewer before stepwise user discussion.
- What needs another test before becoming a formal rule? Whether `notes/` should hold all discussion notes or whether some run-scoped notes should remain under `artifacts/<run_id>/notes/`.
- What should be updated now? The real-project organization docs and researcher startup rules.
