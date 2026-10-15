---
name: mcp-server-development
description: "Design, implement, and review Model Context Protocol servers exposing tools, resources, or prompts with clear schemas, least privilege, safe transport, and robust error handling."
---

# MCP Server Development

## Goal
Build an MCP server that exposes a narrow, documented capability surface to compatible clients. MCP standardizes context/tool exchange; it does not automatically make a server or its tools safe.

## Workflow
1. Define the use case and choose tools, resources, and prompts deliberately. Do not expose capabilities that clients do not need.
2. Write clear names and descriptions, typed input schemas, bounded outputs, and explicit error behavior.
3. Keep tool implementations small and validate all arguments server-side.
4. Enforce authentication and authorization for every protected resource/action. Derive identity from trusted credentials, not model-generated arguments.
5. Apply least privilege to filesystem paths, databases, APIs, network access, and credentials.
6. Select transport and authentication appropriate to the deployment. Protect remote endpoints with TLS and follow current MCP authorization guidance where applicable.
7. Treat tool results, resource contents, and prompt arguments as untrusted. Avoid returning secrets and unnecessary records.
8. Add timeouts, cancellation, bounded output, rate limiting, and safe logging.
9. Test malformed messages, unknown methods, invalid arguments, unauthorized requests, oversized output, dependency failures, and repeated side effects.
10. Document installation, configuration, required permissions, data handling, supported protocol/client versions, and operational limitations.

## Tool design
- Use read-only tools by default where they meet the task.
- Separate read and write operations.
- Require confirmation or a server-side policy gate for destructive or consequential actions.
- Use idempotency for writes that clients may retry.
- Return structured, concise results with stable identifiers and provenance.
- Never treat a tool description as an authorization boundary.

## Security review
Check path traversal, command injection, SSRF, secret leakage, overly broad OAuth scopes, token audience/issuer validation, confused-deputy risks, cross-tenant access, and prompt injection via resources. Validate origin and transport assumptions for the actual client/server topology.

## Deliverable
Provide the capability inventory, schemas, auth/permission model, transport configuration, error taxonomy, tests, setup documentation, and a threat model.

## References
- MCP specification: https://modelcontextprotocol.io/specification
- MCP security best practices: https://modelcontextprotocol.io/specification/draft/basic/security_best_practices
- Anthropic MCP overview: https://docs.anthropic.com/en/docs/agents-and-tools/mcp
