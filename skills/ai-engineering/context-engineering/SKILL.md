---
name: context-engineering
description: "Design context selection, packing, isolation, and compaction for LLM applications and agents when token limits, stale history, or noisy retrieval degrade results."
---

# Context Engineering

## Goal
Supply the model with the smallest, highest-value, correctly scoped context needed for the current decision. Context engineering covers selection and lifecycle, not only prompt wording.

## Workflow
1. **Map context sources.** Separate system/developer policy, current user request, conversation state, retrieved evidence, tool results, persistent memory, and generated intermediate artifacts.
2. **Define trust labels.** Mark untrusted user content, web pages, retrieved files, and tool outputs as data. Never promote their embedded instructions into trusted policy.
3. **Prioritize by utility.** Include task requirements, relevant facts, constraints, and evidence first. Remove unrelated history, duplicate passages, verbose tool output, and obsolete state.
4. **Choose a context strategy.** Use retrieval for large knowledge collections, summaries for long histories, structured state for workflow facts, and references/files for details that need not be in every model call.
5. **Preserve provenance.** Keep source identifiers, timestamps, access scope, and enough surrounding evidence to verify important claims.
6. **Control context growth.** Set budgets for history, retrieved chunks, tool output, and intermediate notes. Truncate or summarize deliberately, not silently.
7. **Prevent cross-task leakage.** Scope context by user, tenant, project, task, and authorization. Do not reuse another user's private state.
8. **Evaluate the assembled context.** Test whether needed facts survive packing and whether irrelevant or malicious content can alter behavior.

## Context lifecycle
- **Collect:** fetch only sources authorized for this request.
- **Normalize:** remove boilerplate, preserve structure, and record metadata.
- **Rank:** order by relevance, freshness, trust, and task-specific utility.
- **Pack:** fit a token budget with room for the response and tool calls.
- **Use:** ask the model to cite or reference evidence where appropriate.
- **Update:** persist only validated state that will be useful later.
- **Expire:** remove stale, sensitive, or no-longer-authorized context.

## Common failure modes
- Lost constraints after summarization.
- Too much low-quality retrieval diluting relevant evidence.
- Stale memory treated as current truth.
- Prompt injection hidden in retrieved text or tool output.
- Unbounded tool output consuming the context window.
- Context assembled across tenants or permission boundaries.

## Evaluation
Track task success against context budget, evidence coverage, retrieval noise, truncation rate, and latency/cost. Create adversarial tests where malicious instructions appear in otherwise relevant documents. Compare full-history, summarized-history, and structured-state approaches on the same cases.

## Deliverable
Document context sources, trust boundaries, ranking/packing rules, token budgets, retention policy, and tests for omissions, stale facts, injection, and isolation.

## References
- Microsoft AI Agents for Beginners, context engineering: https://github.com/microsoft/ai-agents-for-beginners
- LangGraph persistence and memory: https://docs.langchain.com/oss/python/langgraph/add-memory
- Anthropic context engineering overview: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
