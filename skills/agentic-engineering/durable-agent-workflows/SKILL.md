---
name: durable-agent-workflows
description: "Build long-running, stateful agent workflows with checkpoints, resumability, idempotent side effects, retries, cancellation, and recovery after failure."
---

# Durable Agent Workflows

## Goal
Ensure a workflow can pause, fail, resume, or wait for human input without losing state or repeating irreversible actions unexpectedly.

## Workflow
1. Model the process as explicit states and transitions, including success, failure, waiting-for-approval, cancelled, and exhausted-budget states.
2. Define a serializable state schema with task ID, owner/tenant, checkpoint version, progress, artifacts, pending action, and budget counters.
3. Persist checkpoints at meaningful boundaries. Choose durability/latency trade-offs based on the consequences of losing progress.
4. Put external side effects in explicit tasks with idempotency keys or an action ledger.
5. Make retries bounded and classify transient vs permanent errors.
6. Ensure resumption revalidates permissions and relevant external state; authorization can change while a workflow is paused.
7. Add cancellation and deadlines. Stop future tool calls when cancellation is confirmed, and document limits for already-started external actions.
8. Use transactional outbox, deduplication, or reconciliation patterns when a database update and external side effect cannot be atomic.
9. Version state schemas and define migration/compatibility behavior for long-lived checkpoints.
10. Test process crashes between every side effect and checkpoint boundary, duplicate resume requests, expired credentials, and partial failures.

## Critical correctness rules
- A checkpoint does not make an external API call exactly-once by itself.
- Resuming a workflow may replay code; isolate side effects and make them safe to repeat.
- Store secrets outside serialized state; store references to secret managers instead.
- Use unique thread/run IDs and validate access before loading a checkpoint.
- Do not resume from untrusted or tampered state without integrity checks.

## Operational signals
Track age of pending runs, checkpoint failures, resume success, duplicate actions, retry counts, stuck workflows, queue depth, and completion latency. Provide operator tools to inspect, cancel, retry, or safely abandon a run.

## Deliverable
Provide state diagram, checkpoint boundaries, idempotency plan, retry matrix, schema versioning, recovery runbook, and fault-injection tests.

## References
- LangGraph durable execution: https://docs.langchain.com/oss/python/langgraph/durable-execution
- LangGraph overview: https://docs.langchain.com/oss/langgraph/overview
- Temporal documentation: https://docs.temporal.io/
