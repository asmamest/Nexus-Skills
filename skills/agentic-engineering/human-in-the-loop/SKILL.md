---
name: human-in-the-loop
description: "Design human approval and review checkpoints for agent actions, including risk-based policies, review payloads, pause/resume, auditability, and rejection handling."
---

# Human-in-the-Loop Agent Design

## Goal
Put human judgment at decisions where risk, ambiguity, or accountability warrants it, without asking for approval on every harmless step.

## Workflow
1. Classify actions by impact: read-only, reversible write, external communication, financial/legal/production impact, destructive operation, or permission change.
2. Define approval rules outside the model prompt. Tool code or policy middleware must enforce them.
3. Prepare a review payload containing proposed action, normalized arguments, target, expected effect, evidence, risk explanation, and relevant diff. Redact secrets.
4. Pause before execution, not after, for actions requiring approval.
5. Bind approval to the exact action and arguments. If arguments or target change, request approval again.
6. Authenticate the reviewer and check authorization, separation of duties, and approval expiry.
7. Support approve, edit, reject, request-more-information, and timeout outcomes where appropriate.
8. Persist enough state to resume safely. Revalidate permissions and external state after a long pause.
9. Record reviewer, decision, timestamp, action hash/version, and outcome in an access-controlled audit log.
10. Test rejection, edit, expiry, duplicate submissions, reviewer outage, state loss, and changed action arguments.

## UX principles
- Explain what will happen and why it needs approval.
- Show the actual target and material parameters.
- Make reject/cancel as clear as approve.
- Do not use vague approval text for irreversible operations.
- Do not treat silence or timeout as approval.

## Implementation safeguards
- Require server-side authorization at execution time.
- Use idempotency keys for approved side effects.
- Separate policy decision from model recommendation.
- Avoid approving an entire future plan when later actions can materially change.
- Keep emergency stop and cancellation paths available.

## Deliverable
Provide a risk/action matrix, approval UX contract, persistence/resume behavior, audit schema, authorization checks, and failure tests.

## References
- LangGraph human-in-the-loop: https://docs.langchain.com/oss/python/langgraph/interrupts
- OpenAI Agents SDK guardrails: https://openai.github.io/openai-agents-python/guardrails/
- OWASP Excessive Agency: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
