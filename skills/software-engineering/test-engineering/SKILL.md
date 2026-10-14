---
name: test-engineering
description: Design, implement, and improve automated tests for application behavior, regressions, integrations, and edge cases. Use when adding features, fixing defects, reviewing test coverage, or diagnosing failing tests.
---

# Test Engineering

## Objective

Build a trustworthy test suite that detects regressions and verifies observable behavior without becoming unnecessarily slow, brittle, or difficult to maintain.

## Workflow

1. **Understand the behavior**
   - Read the feature requirements, acceptance criteria, and existing tests.
   - Identify inputs, outputs, state changes, side effects, and failure modes.
   - Clarify ambiguous requirements before encoding assumptions in tests.

2. **Choose the appropriate test level**
   - Unit tests: isolated functions, classes, and business rules.
   - Integration tests: interactions between modules, databases, APIs, and services.
   - End-to-end tests: critical user workflows across the running system.
   - Contract tests: compatibility at service or API boundaries.
   - Performance and resilience tests: latency, throughput, resource use, and failure recovery where relevant.

3. **Cover meaningful scenarios**
   - Normal and successful cases.
   - Empty, missing, malformed, and boundary inputs.
   - Invalid state transitions and business-rule violations.
   - Permission failures and unauthenticated access.
   - Dependency timeouts, errors, and unavailable services.
   - Duplicate requests, retries, and concurrency where applicable.

4. **Write maintainable tests**
   - Use descriptive names that express the behavior being verified.
   - Keep arrange, act, and assert steps clear.
   - Prefer deterministic inputs and controlled dependencies.
   - Use mocks only when they clarify a boundary or isolate an external dependency.
   - Test externally observable behavior instead of private implementation details where practical.

5. **Verify the tests**
   - Run the new tests first.
   - Run the relevant existing test suite.
   - Confirm that a regression test fails when the defect is reintroduced, where practical.
   - Inspect failures instead of automatically updating expected results.
   - Report skipped tests and environmental limitations honestly.

## Test quality rules

- A test should fail when the behavior it protects becomes incorrect.
- Avoid dependence on execution order, wall-clock timing, or external services unless intentional.
- Isolate shared state and clean up resources.
- Avoid broad exception assertions that allow unrelated failures to pass.
- Do not assert implementation details that are irrelevant to the contract.
- Keep fixtures small, explicit, and reusable only when reuse improves clarity.

## Coverage

Use coverage reports to discover untested paths, not as the sole measure of quality. Prioritize high-risk business logic, security boundaries, critical workflows, and known regression areas.

## Final report

Summarize the behaviors covered, test levels used, commands executed, results, and important coverage gaps. Never claim that the entire suite passed if only a subset was executed.
