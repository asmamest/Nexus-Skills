
---
name: code-review
description: Review code changes for correctness, security, maintainability, performance, and test coverage. Use when reviewing a diff, pull request, or proposed code change.
---

# Code Review

## Objective

Review code changes systematically. Prioritize correctness, security,
regressions, and maintainability over stylistic preferences.

## Workflow

1. **Understand the change**
   - Read the relevant requirements and surrounding code.
   - Inspect the complete diff and identify the intended behavior.
   - Check repository conventions and existing tests.

2. **Identify defects**
   - Look for logic errors, unhandled edge cases, incorrect assumptions,
     race conditions, resource leaks, and backward-compatibility issues.
   - Check input validation, authorization, authentication, and sensitive
     data handling where relevant.
   - Assess performance only where the change creates a plausible risk.

3. **Verify findings**
   - Trace each suspected defect to the affected code.
   - Run relevant tests or checks when possible.
   - Distinguish confirmed defects from questions or speculative concerns.
   - Never claim that a test passed unless you actually ran it.

4. **Report actionable findings**
   - Prioritize findings by severity.
   - Explain the impact and conditions required to reproduce each issue.
   - Reference the affected file and line when available.
   - Suggest a concrete fix without rewriting unrelated code.

## Severity

- **Critical:** A severe vulnerability or failure with major impact.
- **High:** A significant security, correctness, or data-integrity issue.
- **Medium:** A meaningful defect affecting particular cases or workflows.
- **Low:** A limited-impact defect or improvement worth addressing.

Use the repository's own severity conventions if they exist.

## Output

Start with findings, ordered from highest to lowest severity. For each finding,
include:

- Severity
- Location
- Problem
- Impact and reproduction conditions
- Recommended correction

If no actionable defects are found, state that clearly and mention what was
and was not verified.

## Constraints

- Do not invent findings to fill a report.
- Do not treat personal style preferences as correctness defects.
- Do not modify files or commit changes unless explicitly requested.
- Keep recommendations proportional to the actual risk.
