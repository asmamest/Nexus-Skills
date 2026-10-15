---
name: agent-harness-engineering
description: "Design the harness around an AI agent: tool interfaces, execution loop, context management, policy checks, budgets, state, verification, and recovery."
---

# Agent Harness Engineering

## Goal
Build the reliable control layer around a model-driven agent. The harness governs how the model receives context, requests actions, observes results, retries, verifies completion, and stops.

## Core components
- **Input contract:** task, constraints, user permissions, and expected deliverable.
- **Context manager:** selects evidence, trims history, tracks artifacts, and preserves provenance.
- **Policy layer:** validates tool access, arguments, sensitive actions, and human-approval requirements.
- **Tool adapter:** typed inputs/outputs, timeouts, cancellation, error normalization, and idempotency.
- **Execution loop:** model call → validated action request → policy check → tool execution → observation → progress assessment.
- **State store:** explicit task status, checkpoints, artifacts, budgets, and resumable progress.
- **Verifier:** checks results against acceptance criteria and evidence.
- **Telemetry:** traces, cost, latency, tool errors, safety events, and final outcome.

## Design workflow
1. Write the task contract and acceptance criteria before building an autonomous loop.
2. Separate deterministic business rules from model decisions.
3. Expose the smallest set of tools needed, each with narrow permissions and typed schemas.
4. Define maximum steps, wall-clock time, token/cost budget, retries, and tool-call limits.
5. Normalize tool results and label them as untrusted observations.
6. Require approval for consequential actions such as external messages, destructive writes, purchases, deployments, or permission changes.
7. Make side effects idempotent or persist an action ledger so resumed runs do not repeat them accidentally.
8. Verify final artifacts independently of the model's claim that it succeeded.
9. Test timeout, malformed tool arguments, empty results, tool denial, repeated calls, prompt injection, cancellation, and resume behavior.

## Loop design
A safe loop must have explicit continuation and stop conditions. Stop when the goal is verified, the task is impossible with available permissions/evidence, the budget is exhausted, or a human decision is required. Do not continue merely because the model keeps requesting another step.

## Harness vs prompt
Prompts guide model behavior; the harness enforces operational boundaries. Authorization, filesystem boundaries, budgets, approval gates, schema validation, and idempotency must live in code or infrastructure, not only in natural-language instructions.

## Evaluation
Measure goal success, unnecessary steps, tool-call precision, recovery from tool errors, budget adherence, policy violations, and verification accuracy. Compare against a simpler deterministic workflow before increasing autonomy.

## Deliverable
Provide an architecture diagram, state model, tool contracts, policy matrix, stop conditions, verification plan, observability fields, and failure-injection tests.

## References
- LangGraph runtime concepts: https://docs.langchain.com/oss/langgraph/overview
- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
- Microsoft AI Agents for Beginners: https://github.com/microsoft/ai-agents-for-beginners
