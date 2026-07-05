# Agent Group API Addendum

## Purpose

Upgrade the first single-session role simulation into a more defensible isolated
agent-group experiment.

## Implemented Design

Script:

`research/ai-role-paper-comprehension-water-resources/artifacts/code/run_openai_agent_group_demo.py`

The script implements:

- one independent API call per reader role per round;
- one independent evaluator API call per role per round;
- no shared conversation history between reader agents;
- separate system prompts for undergraduate, master's, PhD, advisor, and evaluator;
- role-specific knowledge boundaries;
- role-specific error rates:
  - undergraduate: 0.35
  - master's: 0.22
  - PhD: 0.10
  - advisor: 0.04
- a fixed random seed (`20260705`) to mark some questions as likely mistakes;
- reuse of the same article, question ladder, hints, and scoring rubric as the
  first demo;
- output files for raw agent responses, scores, summary, and API usage logs.

## Credential Setup

- OpenAI API key name: `ai-role-comprehension-demo`
- Organization shown by connector: `Water Resourse`
- Project shown by connector: `water`
- Local env file: `.env.local`
- Env var: `OPENAI_API_KEY`
- Plaintext key was not printed in tool output.

## Execution Status

The first sandboxed run failed before reaching OpenAI because outbound network
access was blocked.

The approved network run reached OpenAI but failed with:

```text
HTTP 429 insufficient_quota
```

This indicates exhausted or unavailable API quota/billing for the selected
OpenAI organization/project, not a normal transient rate limit.

After the user updated billing, additional diagnostics showed:

- `GET /v1/models` returned 200, so the key is valid and can access the project.
- A tiny `gpt-4o-mini` JSON-mode generation request succeeded once after fixing
  a test parameter error (`max_output_tokens` must be at least 16).
- The full isolated-agent script was updated to use `gpt-4o-mini`, JSON-mode
  output, a shorter article packet, and lower output token limits.
- The smaller full run got past the first reader call but failed on the
  evaluator call with `HTTP 429 insufficient_quota`.
- A later tiny diagnostic generation request also returned
  `HTTP 429 insufficient_quota`.

Current interpretation: model access and authentication work, but generation
quota for the selected organization/project is not reliably available yet. This
may be project-level budget/limit propagation, billing-credit activation delay,
or a project mismatch between the API key target and the dashboard page being
inspected.

## Current Blocker

No isolated agent-group results were generated because the API project has no
usable quota. The existing single-session demo remains the only completed
empirical artifact.

## Next Action

Confirm API billing/credits and project usage limits for the exact key target
(`Water Resourse` / `water`), wait for any billing update to propagate, then
rerun:

```powershell
python research\ai-role-paper-comprehension-water-resources\artifacts\code\run_openai_agent_group_demo.py
```

The script defaults to `gpt-5.4-nano`. To change model:

```powershell
$env:OPENAI_AGENT_GROUP_MODEL = "gpt-5.4-mini"
python research\ai-role-paper-comprehension-water-resources\artifacts\code\run_openai_agent_group_demo.py
```

## Methodological Note

This addendum directly addresses the user's concern that the first demo's
single-session role simulation had shared context and weak knowledge boundaries.
The new design uses isolated API calls and records role-specific mistake
tendencies, but it still remains an AI-simulation experiment rather than
human-subject evidence.
