# Planning Package

- Project: agent-call-smoke-test
- Stage: Planning
- Gate mode: synthetic
- Planning Researcher: Codex
- Planning Reviewer: Claude Code
- Status: smoke test only

## User Need

Validate whether the repository can invoke Claude Code as reviewer from a Codex-led workflow without manually switching chat windows.

## Proposed Route

Use the existing file-based reviewer handoff:

- researcher writes `review-request.md`
- reviewer writes `reviewer-critique.md`
- researcher reads and triages the critique

## Evidence Status

No real evidence is included. This file is only for testing the reviewer invocation wrapper.

## Gate Readiness

Not ready for a real Planning Gate. The expected reviewer finding is that this is only a synthetic smoke test.
