---
name: structured-outputs
description: "Design reliable structured model outputs using schemas, constrained decoding where available, validation, retries, and explicit handling of partial or invalid responses."
---

# Structured Outputs

## Goal
Turn model responses into validated data contracts without trusting that syntactically plausible output is semantically correct.

## Workflow
1. **Define a schema.** Specify required fields, types, enums, bounds, nullability, nested objects, and versioning rules. Avoid ambiguous field names.
2. **Use provider-supported constrained output when available.** Confirm the exact API/model supports the required schema features. Do not assume all JSON modes provide the same guarantees.
3. **Validate at the boundary.** Parse the response and validate it with a schema library or explicit domain checks before any side effect.
4. **Separate syntax from semantics.** Valid JSON can still contain invalid IDs, unauthorized targets, contradictory fields, or fabricated facts.
5. **Handle incomplete responses.** Distinguish refusal, truncation, timeout, tool-call response, parse failure, schema failure, and semantic rejection.
6. **Retry selectively.** Use bounded retries for recoverable format failures; include concise validation feedback if safe. Avoid infinite self-correction loops.
7. **Make side effects idempotent.** Validate the complete request and permissions before writing data, sending messages, or invoking external tools.
8. **Log safely.** Capture schema version, validation category, and redacted diagnostics; avoid logging secrets or sensitive raw payloads unnecessarily.
9. **Test adversarial cases.** Include extra keys, missing fields, invalid enums, boundary values, Unicode, huge strings, nested arrays, refusal, and malicious instructions in fields.

## Design rules
- Keep schema constraints aligned with actual business rules.
- Use strict additional-property policies where appropriate.
- Use explicit discriminators for union types.
- Make unknown or unavailable values explicit rather than guessing.
- Treat all model-produced strings as untrusted input.
- Never rely on schema validity as authorization.

## Deliverable
Provide the schema, validation boundary, failure taxonomy, retry policy, security checks, and tests. State which guarantees come from the provider and which are enforced by application code.

## References
- OpenAI Structured Outputs: https://platform.openai.com/docs/guides/structured-outputs
- Pydantic documentation: https://docs.pydantic.dev/latest/concepts/models/
- JSON Schema: https://json-schema.org/learn/getting-started-step-by-step
