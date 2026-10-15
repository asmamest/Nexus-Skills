---
name: tool-calling-design
description: "Design safe, clear, typed tool interfaces for LLM agents, including schema validation, authorization, error semantics, idempotency, and tool-result handling."
---

# Tool-Calling Design

## Goal
Expose external capabilities to an agent through narrow, predictable interfaces. Tool selection may be model-driven; authorization and execution must remain application-controlled.

## Tool contract
For each tool, define:
- A precise name and one-sentence purpose.
- Typed arguments, required/optional fields, bounds, enums, and examples.
- A structured success response with stable fields.
- Explicit error categories and whether retry is safe.
- Required permissions, tenant scope, and data classification.
- Side-effect level and approval requirement.
- Timeout, rate limit, idempotency key, and audit behavior where relevant.

## Workflow
1. Start from a user task and expose only capabilities required for that task.
2. Keep each tool narrow; split unrelated read/write powers.
3. Validate arguments server-side even if the model uses a schema.
4. Authenticate the caller and authorize every operation using trusted identity/context, never model-generated claims.
5. Enforce resource ownership and tenant filtering inside the tool implementation.
6. Use least privilege and avoid generic shells, unrestricted SQL, arbitrary URLs, or unrestricted filesystem access where a narrower API works.
7. Return bounded, structured results with source/provenance and clear error codes.
8. Treat tool output as untrusted data; it may contain prompt injection or malformed content.
9. Apply timeout, cancellation, rate limits, retry budgets, and circuit breakers.
10. Use idempotency or deduplication for side effects and record action status before retrying after ambiguous failures.
11. Add human approval for consequential or irreversible actions.
12. Test denied permissions, invalid arguments, duplicate calls, partial failures, timeouts, oversized output, and malicious tool results.

## Error semantics
Distinguish invalid input, unauthorized access, not found, conflict, rate limit, transient dependency failure, timeout, and permanent failure. Give the agent enough information to recover safely without exposing secrets, stack traces, or internal infrastructure details.

## Result shaping
Return only fields needed for the next decision. Paginate large outputs, cap payload size, and include stable identifiers. Do not return raw secrets or entire database records by default.

## Deliverable
Produce tool schemas, permission matrix, error taxonomy, retry/idempotency policy, approval policy, audit fields, and contract tests.

## References
- OpenAI function calling: https://platform.openai.com/docs/guides/function-calling
- Anthropic tool use: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview
- OWASP Excessive Agency: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
