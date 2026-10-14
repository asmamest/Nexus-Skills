# Nexus Skills Catalog

This catalog is generated/maintained alongside the skill folders. Every listed skill must exist under `skills/` and contain a valid `SKILL.md`. Run `python scripts/validate_skills.py` after editing skills or this file.

> **Safety note:** Skills are executable instructions for an AI agent, not merely documentation. Read the complete skill before installing it, especially when it requests shell commands, network access, credentials, file edits, or deployment actions.

## Software engineering

### `code-review`
- **Path:** `skills/software-engineering/code-review/SKILL.md`
- **Use when:** Reviewing a diff or pull request for correctness, regressions, security risks, and missing tests.
- **Output:** Prioritized findings with file/line references, evidence, impact, and unresolved questions.

### `debugging`
- **Path:** `skills/software-engineering/debugging/SKILL.md`
- **Use when:** Investigating a bug, failing test, crash, or unexpected behavior.
- **Output:** Reproduction, evidence-backed root-cause hypothesis, minimal fix, and verification results.

### `test-engineering`
- **Path:** `skills/software-engineering/test-engineering/SKILL.md`
- **Use when:** Designing or improving automated tests for existing behavior or a new change.
- **Output:** Risk-based test plan, focused tests, and results.

## AI engineering

### `rag-engineering`
- **Path:** `skills/ai-engineering/rag-engineering/SKILL.md`
- **Use when:** Designing, debugging, or evaluating a retrieval-augmented generation pipeline.
- **Output:** Traceable retrieval/generation design, evaluation plan, and known limitations.

### `llm-evaluation`
- **Path:** `skills/ai-engineering/llm-evaluation/SKILL.md`
- **Use when:** Building evaluations for LLM outputs, prompts, or model changes.
- **Output:** Versioned test set, metrics, failure analysis, and release criteria.

## Agentic engineering

### `agent-evaluation`
- **Path:** `skills/agentic-engineering/agent-evaluation/SKILL.md`
- **Use when:** Evaluating an agent that plans, calls tools, or executes multi-step workflows.
- **Output:** Task suite, tool-use and safety measures, failure taxonomy, and regression report.

### `mcp-development`
- **Path:** `skills/agentic-engineering/mcp-development/SKILL.md`
- **Use when:** Designing, implementing, reviewing, or testing a Model Context Protocol server or client integration.
- **Output:** Protocol-aware implementation plan, tool/resource design, and security/test checklist.

## Security and quality

### `security-review`
- **Path:** `skills/security-quality/security-review/SKILL.md`
- **Use when:** Reviewing code or an architecture for common security weaknesses and unsafe trust boundaries.
- **Output:** Risk-ranked findings, exploit preconditions, mitigations, and verification steps.
