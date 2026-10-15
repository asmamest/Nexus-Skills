---
name: prompt-engineering
description: "Design and improve prompts for LLM applications, including instruction hierarchy, examples, structured outputs, injection resistance, and measurable prompt iteration."
---

# Prompt Engineering

## Goal
Create prompts that reliably produce the required behavior across realistic inputs and model variations. Treat prompts as versioned application components, not magic wording.

## Workflow
1. **Define the task contract.** Specify audience, input shape, desired output schema, constraints, prohibited behavior, and what success means.
2. **Separate instructions from data.** Delimit user content, retrieved documents, tool output, and examples. Explicitly state that untrusted content is data, not instructions.
3. **Use the smallest sufficient prompt.** Remove duplicated rules, vague adjectives, irrelevant context, and instructions the model cannot follow.
4. **Specify output.** Prefer a schema, field definitions, allowed values, and a clear missing-information policy over vague formatting requests.
5. **Add examples selectively.** Use representative positive, negative, boundary, and ambiguous examples. Ensure examples do not accidentally teach unwanted shortcuts.
6. **Design abstention.** Define when to ask a question, return an explicit unknown, escalate, or decline an unsupported claim.
7. **Evaluate changes.** Compare the candidate prompt with a baseline on a fixed, representative dataset. Change one major variable at a time where possible.
8. **Version and document.** Store prompt templates, model settings, dataset version, evaluation results, and known failure modes together.

## Quality checklist
- Are instructions concrete, non-contradictory, and ordered by importance?
- Are factual claims grounded in supplied evidence or an explicitly permitted source?
- Are output fields, types, limits, and error cases defined?
- Are examples diverse and free of sensitive or production data?
- Are prompt injection and instruction-conflict cases tested?
- Is the prompt robust to empty, long, malformed, multilingual, and adversarial inputs?

## Iteration protocol
- Establish a baseline before editing.
- Build a small evaluation set from real task patterns, edge cases, and known failures.
- Score task success, format validity, factuality, safety, latency, and cost as relevant.
- Inspect failures individually; aggregate scores can hide catastrophic cases.
- Keep a prompt change only when evidence shows a net improvement and no unacceptable regression.

## Avoid
- Repeatedly adding prose without testing.
- Treating chain-of-thought disclosure as a requirement; ask for concise rationale or evidence instead.
- Relying on prompt wording as the only security boundary.
- Embedding secrets, credentials, or personal data in prompts.
- Claiming a prompt is robust based on one successful example.

## Deliverable
Return the final prompt, its expected input/output contract, key assumptions, evaluation method, measured results if actually run, and unresolved limitations.

## References
- OpenAI prompting guide: https://platform.openai.com/docs/guides/prompt-engineering
- Anthropic prompt engineering: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- OWASP LLM risks: https://genai.owasp.org/llm-top-10/
