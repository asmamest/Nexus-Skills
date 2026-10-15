---
name: multi-agent-orchestration
description: "Design and evaluate supervisor, router, handoff, and parallel-worker agent patterns with clear ownership, bounded delegation, structured messages, and conflict resolution."
---

# Multi-Agent Orchestration

## Goal
Use multiple agents only when specialization, parallelism, or isolation creates measurable value. Make delegation bounded, auditable, and recoverable.

## Workflow
1. **Prove the need.** Compare a single-agent or deterministic baseline with the proposed multi-agent design.
2. **Define roles.** Each agent needs a narrow responsibility, input contract, output contract, tool allowlist, and stop condition.
3. **Choose orchestration.** Use a router for classification, a supervisor for dynamic delegation, explicit handoffs for control transfer, or parallel workers for independent tasks.
4. **Bound delegation.** Set maximum depth, number of agents, wall time, token/cost budget, retries, and tool calls. Prevent recursive spawning loops.
5. **Structure messages.** Include task objective, relevant context, constraints, evidence references, expected output schema, and completion criteria. Avoid passing entire conversation histories by default.
6. **Isolate privileges.** Give each agent only the data and tools required. Never assume an agent's identity or assertions establish authorization.
7. **Handle parallel results.** Define merge rules, deduplication, conflict detection, source precedence, and what happens when workers disagree or fail.
8. **Verify outputs.** Validate specialist results against source evidence and task requirements before taking action or presenting conclusions.
9. **Observe the delegation graph.** Trace parent/child calls, costs, failures, retries, and decisions.
10. **Evaluate.** Measure end-to-end success, latency, cost, duplicated work, disagreement rate, and policy violations against the baseline.

## Coordination patterns
- Parallelize independent, bounded research or analysis.
- Keep sequential dependencies explicit.
- Use a reviewer agent only when it has clear criteria and can inspect the actual artifact/evidence.
- Avoid majority voting among agents that share the same model, prompt, or source bias as a substitute for verification.

## Failure handling
Define behavior for worker timeout, malformed output, partial results, contradictory claims, supervisor failure, cancellation, and budget exhaustion. Preserve completed work when safe, but do not repeat external side effects blindly.

## Deliverable
Provide a delegation diagram, role contracts, state transitions, budget limits, permissions, merge/conflict policy, trace fields, and comparative evaluation.

## References
- Microsoft multi-agent design lessons: https://github.com/microsoft/ai-agents-for-beginners/tree/main/08-multi-agent
- LangGraph subgraphs: https://docs.langchain.com/oss/python/langgraph/use-subgraphs
- OpenAI Agents SDK handoffs: https://openai.github.io/openai-agents-python/handoffs/
