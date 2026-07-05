# Research Project Organization

This document defines the default layout for real research projects. Each new
research workflow should get its own folder under `research/` before substantive
Planning work begins.

## Default Layout

Use a descriptive, stable slug:

```text
research/<research-name>/
  README.md
  run-notes.md
  packages/
    planning-package.md
    modeling-package.md
    reporting-package.md
    reviewing-package.md
  deliverables/
  notes/
  artifacts/
    <run_id>/
      review-request.md
      reviewer-critique.md
      run_manifest.json
      run_log.md
      run_summary.md
      agent/
    input/
    data/
    code/
    logs/
    tables/
    figures/
    validation/
  archive/
```

## What Belongs Where

| Location | Purpose |
|---|---|
| `README.md` | Short orientation: research question, current stage, status, important paths |
| `run-notes.md` | Provisional lessons, decisions, friction, and after-action notes |
| `packages/` | Compact stage handoff packages only |
| `deliverables/` | Reader-facing outputs such as manuscript drafts, reports, slides, dashboards, or software packages |
| `notes/` | Discussion notes, literature reviews, problem taxonomies, source notes, method sketches |
| `artifacts/<run_id>/` | Run-scoped review requests, critiques, manifests, logs, summaries, and agent artifacts |
| `artifacts/input/` | User-supplied files and route-defining inputs |
| `artifacts/data/` | Raw and cleaned datasets or literature/source matrices |
| `artifacts/code/` | Scripts and notebooks |
| `artifacts/logs/` | Command logs, environment repair logs, execution traces |
| `artifacts/tables/` | Generated analytical tables |
| `artifacts/figures/` | Generated figures and diagrams |
| `artifacts/validation/` | Validation inputs and outputs |
| `archive/` | Superseded files kept for traceability |

## Startup Rule

At the beginning of a new real research project, the researcher agent should:

1. propose a `research/<research-name>/` slug;
2. create the default folder skeleton after the user confirms or when the slug is safe to infer;
3. create `README.md` and `run-notes.md`;
4. create or revise only the active stage package in `packages/`;
5. put detailed stepwise discussion artifacts in `notes/`;
6. put review requests and reviewer critiques under `artifacts/<run_id>/`.

For framework tests or tiny smoke tests, a shorter layout is acceptable, but the
run must still record where packages, notes, artifacts, and deliverables live.

## Root Directory Rule

Do not create new real-project packages directly under the repository-level
`packages/` or new real-project run artifacts directly under the repository-level
`artifacts/` unless the user explicitly requests a legacy layout. Those root
folders may remain for older runs, templates, or migration staging, but new
research projects should live under `research/<research-name>/`.

## Stepwise Work Rule

The project folder supports gradual collaboration:

- draft long reviews and source scans in `notes/`;
- discuss one unit with the user;
- summarize only accepted decisions back into `packages/planning-package.md`;
- send the package for reviewer critique only after the major Planning units
  are discussed or accepted.
