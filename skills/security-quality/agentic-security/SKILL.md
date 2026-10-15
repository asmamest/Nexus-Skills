---
name: agentic-security
description: "Threat-model and harden LLM applications and agentic systems against prompt injection, excessive agency, data leakage, unsafe tools, and compromised dependencies."
---

# Agentic Security

## Goal
Reduce risk across the full system, not merely the prompt. Assume model outputs can be wrong or manipulated and enforce security controls in deterministic application and infrastructure layers.

## Threat-model workflow
1. Map assets, trust boundaries, actors, data flows, tools, models, retrieval stores, plugins/MCP servers, and external services.
2. Identify direct and indirect prompt injection paths, including retrieved documents, webpages, tool outputs, and messages from other agents.
3. Inventory tool capabilities and permissions. Remove unused tools and split read/write powers.
4. Define data classification, tenant isolation, secret handling, retention, and allowed outbound destinations.
5. Model impacts across confidentiality, integrity, availability, and user safety.
6. Prioritize controls by impact, exploitability, exposure, and feasibility.

## Required controls
- Enforce authorization in trusted code for every data access and side effect.
- Apply least privilege to tools, credentials, filesystem, network, and runtime.
- Validate and constrain tool arguments; use allowlists for operations and destinations.
- Require human approval for high-impact or irreversible actions.
- Treat retrieved text and tool output as untrusted data, not trusted instructions.
- Separate model-generated proposals from execution decisions.
- Use sandboxing and resource limits for code execution and untrusted files.
- Redact secrets and sensitive data from prompts, traces, logs, and error messages.
- Protect model endpoints and MCP integrations with appropriate authentication, authorization, and rate limits.
- Pin and scan dependencies; review third-party tool servers and their permissions.

## Adversarial tests
Test direct/indirect prompt injection, poisoned retrieval, data exfiltration requests, unauthorized cross-tenant lookups, tool argument manipulation, unsafe URL fetches, malicious subagent output, repeated side effects, denial-of-service inputs, and attempts to bypass approval gates.

## Incident readiness
Maintain traceable action logs, kill switches, credential revocation, tool disablement, incident triage, and rollback procedures. Keep logs privacy-aware and access-controlled.

## Security review output
For each finding, include severity, affected boundary, attack preconditions, concrete impact, evidence, mitigation, and residual risk. Distinguish confirmed exploit paths from theoretical concerns. Do not claim a system is secure merely because a prompt says to ignore malicious instructions.

## References
- OWASP GenAI Security Project: https://genai.owasp.org/llm-top-10/
- OWASP Excessive Agency: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
- MCP security best practices: https://modelcontextprotocol.io/specification/draft/basic/security_best_practices
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
