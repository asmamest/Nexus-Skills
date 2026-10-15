---
name: agent-architecture-design
description: "Choose agent patterns and boundaries for a task, comparing deterministic workflows, single-agent loops, routers, planners, supervisors, and multi-agent systems."
---

# Agent Architecture Design

## Goal
Select the simplest architecture that meets the task's reliability and flexibility requirements. An agent is not automatically better than a deterministic workflow.

## Architecture selection
- **Deterministic pipeline:** preferred when steps and decisions are known and stable.
- **Single tool-using agent:** suitable when a model must choose among a small set of tools dynamically.
- **Router:** use when input categories can be identified and routed to specialized paths.
- **Planner-executor:** use when a task benefits from explicit decomposition, but validate plans and constrain execution.
- **Supervisor with specialists:** use when independent domains need different prompts, tools, or context boundaries.
- **Parallel workers:** use for independent research or analysis whose outputs can be merged and checked.
- **Stateful graph/workflow:** use for long-running tasks, checkpoints, approval pauses, retries, or branching state transitions.

## Design workflow
1. Define user outcomes, constraints, risk level, latency budget, and failure tolerance.
2. Draw the simplest baseline workflow before adding agents.
3. Identify exactly which decisions require model flexibility.
4. Define state, transitions, tool contracts, error paths, and terminal conditions.
5. Keep permissions and data access least-privilege per component.
6. Decide whether agents share context, exchange structured summaries, or use isolated state.
7. Add human checkpoints at irreversible or high-impact boundaries.
8. Define independent verification of outputs and side effects.
9. Evaluate the architecture against a baseline for success, cost, latency, and failure recovery.

## Multi-agent trade-offs
Delegation can improve parallelism and specialization, but adds coordination overhead, context loss, duplicated work, nondeterminism, and a larger security surface. Use subagents only when the work can be decomposed cleanly and their results can be independently assessed.

## Required design artifacts
- Component diagram and responsibility boundaries.
- State schema and transition table.
- Tool and inter-agent message schemas.
- Permission matrix and approval rules.
- Retry, timeout, cancellation, and stop policies.
- Evaluation cases for happy paths, ambiguity, failure, and abuse.

## Anti-patterns
- Multi-agent architecture without a measurable need.
- Unbounded recursive delegation.
- Shared unrestricted credentials across all agents.
- Treating another agent's output as trusted fact.
- No terminal state or independent completion check.
- Hiding deterministic business logic inside prompts.

## References
- LangGraph overview: https://docs.langchain.com/oss/langgraph/overview
- Microsoft agent design lessons: https://github.com/microsoft/ai-agents-for-beginners
- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
