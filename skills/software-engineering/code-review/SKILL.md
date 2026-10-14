
---
name: code-review
description: Review code changes for correctness, security, reliability, maintainability, performance, and test coverage. Use when reviewing pull requests, diffs, or proposed code changes.
---

# Code Review

## Objective

Identify actionable defects introduced by a code change. Prioritize correctness, security, data integrity, reliability, and regressions. Base findings on evidence, not speculation or personal style preferences.

## Workflow

### 1. Establish context

- Read the requirements, acceptance criteria, and relevant documentation.
- Inspect the complete diff and surrounding implementation.
- Identify affected components, dependencies, interfaces, and data flows.
- Check repository conventions and existing tests.
- State when the available context is incomplete.

### 2. Review correctness and reliability

Check relevant risks:

- Incorrect logic, assumptions, conditions, and state transitions.
- Boundary cases, malformed inputs, and unexpected values.
- Error handling, retries, timeouts, cancellation, and resource cleanup.
- Race conditions, transactions, and data consistency.
- API contracts, backward compatibility, and migration behavior.
- Performance regressions and excessive resource consumption.
- Missing or ineffective tests for important behavior.

Apply checks proportionally to the change.

### 3. Review security

When relevant, examine:

- Authentication, authorization, and privilege boundaries.
- Input validation, injection, and unsafe deserialization.
- Exposed secrets, sensitive logging, and personal data.
- File uploads, path traversal, and command execution.
- Cryptography and key management.
- Dependency risks and insecure configuration.
- Server-side request forgery and unsafe outbound requests.
- Trust boundaries involving users, services, tools, and external content.

Explain the vulnerable path and realistic impact. Do not claim a vulnerability without supporting evidence.

### 4. Verify suspected defects

- Trace each suspected issue to the affected code.
- Determine whether the change introduced the defect.
- Identify the conditions required to reproduce it.
- Run relevant tests or safe checks when feasible.
- Distinguish verified facts from hypotheses.
- Never claim checks passed unless they were actually run.

Do not perform destructive operations or modify files without authorization.

### 5. Assign priority

Follow repository conventions when available. Otherwise:

- **P0 — Critical:** Catastrophic impact or an immediately severe vulnerability.
- **P1 — High:** Significant security, correctness, availability, or data-integrity impact.
- **P2 — Medium:** Meaningful defect affecting specific conditions or workflows.
- **P3 — Low:** Limited-impact but actionable defect.

Consider impact and likelihood. Do not elevate an issue merely because the code looks unfamiliar.

## Findings Format

List actionable findings first, ordered from highest to lowest priority.

Use this format for each finding:

### [P1] Specific description of the defect

- **Location:** `path/to/file.ext:line`
- **Issue:** Explain what is wrong.
- **Trigger:** Describe the conditions or input that cause it.
- **Impact:** Explain the practical consequence.
- **Evidence:** Reference the relevant code path or actual test result.
- **Recommendation:** Suggest the smallest appropriate correction.

Use the actual file and line number when available. Do not invent locations, duplicate findings for the same root cause, or report unrelated pre-existing problems as regressions.

Omit unsupported details rather than guessing. Do not report optional refactoring or stylistic preferences as defects.

## Final Review Summary

After the findings, provide:

- **Verdict:** Approve, approve with non-blocking issues, or request changes, following repository conventions.
- **Scope reviewed:** Files and behaviors examined.
- **Validation:** Checks actually run and their results.
- **Limitations:** Important areas not verified.

If no actionable findings are identified, say so explicitly. Do not claim the change is completely defect-free or fully secure.

## Constraints

- Never invent defects, line numbers, test results, or security claims.
- Explain the impact and triggering conditions of every finding.
- Prefer concise, actionable, evidence-based feedback.
- Separate defects from optional improvements.
- Do not silently modify code or commit changes during a review.
