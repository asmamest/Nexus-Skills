```markdown
---
name: example-skill
description: Describe what this skill does and when an agent should use it.
---

# Example Skill

## Purpose

Describe the engineering problem this skill solves and the outcome it should produce.

## When to use

Use this skill when:

- The user requests a specific, relevant engineering task.
- The current project context matches the skill's intended purpose.

Do not use it when the task falls outside its scope.

## Inputs and assumptions

Identify:

- Required inputs and project context.
- Assumptions the workflow relies on.
- Constraints, dependencies, and limitations.
- Information that must be clarified before proceeding.

Never invent missing requirements, test results, or project facts.

## Workflow

1. Inspect the existing project and understand the requirements.
2. Identify the relevant files, tools, dependencies, and constraints.
3. Choose an approach appropriate to the task.
4. Execute the necessary steps while following existing project conventions.
5. Verify the result using relevant tests or checks.
6. Report the outcome, limitations, and any remaining work.

Adapt these steps to the specific task. Avoid unnecessary actions.

## Quality checks

Define how to determine whether the task was completed successfully.

Include relevant checks such as:

- Correctness and completeness.
- Unit, integration, or regression tests.
- Error handling and edge cases.
- Security and performance considerations, where relevant.

Never claim that a check passed unless it was actually performed.

## Safety and constraints

Document relevant safety requirements, permissions, and side effects.

- Do not expose secrets or sensitive data.
- Do not perform destructive actions without appropriate authorization.
- Do not introduce dependencies without a clear reason.
- Ask for confirmation before consequential actions when required.

Remove or adapt rules that are irrelevant to this particular skill.

## Examples

### Example 1: Typical use

Describe a realistic request and the expected approach or outcome.

### Example 2: Edge case

Describe an important boundary condition and how the workflow should handle it.

## References

List relevant authoritative documentation or supporting files, if needed.

- [Reference title](https://example.com)

## Limitations

Describe known limitations, unsupported cases, or situations requiring human review.
```
