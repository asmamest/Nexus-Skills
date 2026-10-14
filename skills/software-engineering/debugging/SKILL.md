---
name: debugging
description: Diagnose and fix software defects through reproducible experiments, root-cause analysis, and regression testing. Use when investigating exceptions, failing tests, unexpected behavior, or production incidents.
---

# Debugging

## Objective

Find the underlying cause of a defect, verify it with evidence, and implement the smallest reliable correction.

## Workflow

1. **Understand the symptom**
   - Record the expected and actual behavior.
   - Capture the error message, stack trace, logs, environment, and reproduction steps.
   - Identify when the problem started and whether it is intermittent.

2. **Reproduce the failure**
   - Build the smallest reliable reproduction.
   - Identify relevant inputs, configuration, dependencies, and runtime conditions.
   - If the issue cannot be reproduced, state that limitation and investigate available evidence.

3. **Form hypotheses**
   - List plausible causes based on the evidence.
   - Prioritize hypotheses by likelihood and impact.
   - Change one relevant variable at a time where practical.

4. **Investigate systematically**
   - Trace execution through the affected functions and dependencies.
   - Inspect state transitions, input validation, exceptions, network calls, and database operations.
   - Use logs, a debugger, targeted instrumentation, or a minimal test.
   - Distinguish the first causal failure from downstream symptoms.

5. **Fix the root cause**
   - Prefer the smallest change that addresses the demonstrated cause.
   - Preserve existing interfaces and expected behavior unless a change is required.
   - Avoid broad rewrites and unrelated cleanup.

6. **Verify the correction**
   - Run the reproduction against the fixed implementation.
   - Add a regression test that fails before the fix and passes afterward.
   - Run relevant existing tests and inspect for unintended side effects.

## Common failure categories

- Incorrect assumptions about inputs or state.
- Boundary conditions and off-by-one errors.
- Missing error handling or incorrect exception propagation.
- Configuration and environment mismatches.
- Dependency or version incompatibilities.
- Concurrency, ordering, and timing issues.
- Authentication, authorization, and data-validation defects.
- Resource exhaustion, leaks, and retry loops.

## Constraints

- Never claim a root cause without supporting evidence.
- Do not suppress exceptions simply to make an error disappear.
- Do not remove failing tests or weaken assertions to obtain a green build.
- Avoid destructive production operations.
- Redact credentials, tokens, personal information, and other sensitive log data.

## Final report

Include:
- The observed symptom.
- The confirmed or suspected root cause.
- The correction made or recommended.
- Tests performed and their actual results.
- Remaining risks or unresolved questions.
