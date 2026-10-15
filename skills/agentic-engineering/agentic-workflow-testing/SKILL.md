---
name: agentic-workflow-testing
description: "Test complete agent workflows with unit, contract, integration, trajectory, fault-injection, and regression tests while controlling nondeterminism and external side effects."
---

# Agentic Workflow Testing

## Goal
Test agent systems as stateful programs with model variability, external tools, and side effects. A successful final response alone is insufficient evidence that the workflow behaved safely.

## Test layers
1. **Unit tests:** deterministic policies, schemas, reducers, ranking logic, state transitions, and argument validators.
2. **Contract tests:** tool request/response schemas, error categories, authorization, and compatibility.
3. **Integration tests:** model/provider adapters, retrieval, persistence, tool server, and checkpoint store.
4. **Trajectory tests:** expected tool sequence or allowed path, state changes, approvals, and terminal conditions.
5. **Evaluation tests:** semantic success, groundedness, tool choice, and rubric-based behavior on a versioned dataset.
6. **Fault-injection tests:** timeout, rate limit, malformed output, unavailable tool, partial side effect, cancellation, and resume.
7. **Security tests:** prompt injection, unauthorized data access, cross-tenant leakage, excessive agency, and approval bypass.

## Workflow
1. Define observable acceptance criteria and forbidden outcomes.
2. Use fake tools and deterministic fixtures for fast tests; reserve real external integrations for selected integration tests.
3. Stub or record model calls where appropriate, but keep a smaller live-model evaluation suite for behavior changes that mocks cannot reveal.
4. Assert final state and side effects, not only text output.
5. Make tests isolated, resettable, and safe to rerun. Use unique test identities and idempotency keys.
6. Keep flaky tests visible; do not hide failures with unbounded retries.
7. Store representative failed trajectories as regression fixtures, with sensitive data removed.
8. Run tests at the right gates: quick checks locally, broader suites in CI, and live smoke tests after deployment.

## Determinism and tolerance
Model outputs can vary. Prefer invariant-based assertions, schema checks, and allowed tool-path sets over brittle exact-text matches. For semantic graders, use calibrated thresholds and human spot checks. Do not loosen assertions merely to make a broken behavior pass.

## Deliverable
Provide test layers, fixtures, environment controls, side-effect assertions, fault matrix, CI gates, and coverage gaps.

## References
- OpenAI evals: https://platform.openai.com/docs/guides/evals
- LangGraph testing: https://docs.langchain.com/oss/python/langgraph/test
- Superpowers testing methodology: https://github.com/obra/superpowers
