---
name: agent-memory-design
description: "Design short-term and long-term memory for AI agents with explicit write policies, provenance, retrieval, privacy, expiration, correction, and deletion."
---

# Agent Memory Design

## Goal
Persist only information that improves future tasks and is appropriate to retain. Memory is an application data system, not an unlimited transcript dump.

## Memory categories
- **Working state:** temporary variables, plan status, current tool results, and task artifacts.
- **Conversation memory:** recent interaction needed for continuity.
- **Long-term memory:** validated preferences, stable project facts, or user-approved facts useful across sessions.
- **Knowledge store:** external documents and records retrieved on demand; do not confuse this with personal memory.

## Workflow
1. Define what the agent must remember and why. Avoid adding memory because it is easy to store.
2. Establish user/tenant/project scopes and data classification before choosing a store.
3. Define write rules: explicit user request, validated extraction, confidence threshold, or human approval.
4. Store structured records with source, timestamp, scope, confidence, version, and expiration where useful.
5. Retrieve selectively using relevance, freshness, access control, and task context.
6. Resolve conflicts. Prefer explicit corrections and authoritative recent sources; preserve uncertainty when facts disagree.
7. Let users inspect, correct, export, and delete memory where applicable.
8. Enforce retention and deletion across caches, indexes, backups, and derived summaries according to policy.
9. Evaluate whether memory improves task outcomes and whether stale or incorrect memory causes harm.

## Security and privacy
- Do not store credentials, secrets, or sensitive personal data by default.
- Do not infer sensitive traits from incidental conversation.
- Keep tenant and user boundaries enforced in storage queries.
- Treat recalled memory as potentially stale and confirm high-impact facts before acting.
- Protect memory writes from prompt injection or malicious documents that try to persist instructions.
- Log access and changes without copying sensitive contents into broad telemetry.

## Memory quality tests
Test stale preferences, user corrections, contradictory facts, deleted records, cross-user retrieval, prompt-injection attempts, and memory unavailable scenarios. Include a no-memory baseline to verify the feature actually helps.

## Deliverable
Specify memory schema, write/read rules, retention/deletion, permission boundaries, conflict handling, and measured benefit/risks.

## References
- LangGraph memory: https://docs.langchain.com/oss/python/langgraph/add-memory
- Microsoft AI Agents for Beginners, agent memory: https://github.com/microsoft/ai-agents-for-beginners/tree/main/13-agent-memory
- NIST Privacy Framework: https://www.nist.gov/privacy-framework
