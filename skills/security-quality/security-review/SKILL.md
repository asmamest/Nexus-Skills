---
name: security-review
description: Assess application code, architecture, dependencies, configuration, and data flows for security weaknesses. Use when reviewing authentication, authorization, APIs, secrets, input handling, infrastructure, or security-sensitive changes.
---

# Security Review

## Objective

Identify exploitable weaknesses, explain their impact, and recommend practical mitigations based on evidence and the application's threat model.

## Workflow

1. **Establish scope**
   - Identify the components, changes, assets, and trust boundaries being reviewed.
   - Understand the application's intended users and deployment environment.
   - Identify sensitive data, privileged operations, and external dependencies.
   - Review relevant security requirements and repository instructions.

2. **Build a threat model**
   - Identify valuable assets and possible attackers.
   - Trace untrusted inputs and data crossing trust boundaries.
   - Identify entry points, privileges, and security assumptions.
   - Consider confidentiality, integrity, availability, and privacy impacts.
   - Prioritize threats according to likelihood and potential consequence.

3. **Review identity and access**
   - Check authentication and session-management behavior.
   - Verify authorization on every sensitive server-side operation.
   - Look for insecure direct object references and cross-tenant access.
   - Check role enforcement, privilege escalation, and default permissions.
   - Confirm that revocation and expiration behavior are appropriate.

4. **Review input and output handling**
   - Inspect validation, normalization, encoding, and parsing.
   - Check for injection, unsafe deserialization, path traversal, and command execution.
   - Review file uploads, redirects, URL handling, and server-side request forgery risks.
   - Verify that output is safely encoded for its destination.
   - Check error messages for sensitive information leakage.

5. **Review secrets and data protection**
   - Look for hardcoded credentials, tokens, private keys, and sensitive configuration.
   - Check whether secrets are logged, returned in responses, or exposed to clients.
   - Review encryption, key management, retention, and deletion requirements.
   - Verify that sensitive information is accessible only to authorized components.
   - If a real secret is exposed, recommend revocation or rotation; removing it from the latest commit alone may not be sufficient.

6. **Review dependencies and infrastructure**
   - Inspect dependency versions, known vulnerabilities, and untrusted packages.
   - Review container privileges, filesystem permissions, and exposed network services.
   - Check environment-specific configuration and debug settings.
   - Examine CI/CD permissions, build provenance, and secret handling.
   - Recommend supported dependency updates and configuration hardening where justified.

7. **Review AI and agent-specific risks**
   - Check for prompt injection through user inputs, documents, and tool outputs.
   - Verify that tools enforce authorization independently of model instructions.
   - Check for unintended data exposure, excessive tool permissions, and unsafe side effects.
   - Validate model outputs before passing them into privileged operations.
   - Test whether retrieved content can influence actions outside its permitted scope.

8. **Validate findings**
   - Support each finding with a concrete code path, configuration, or reproducible test.
   - Distinguish confirmed vulnerabilities from plausible concerns.
   - Use safe, authorized tests only.
   - Do not access real user data, exploit production systems, or perform destructive actions without explicit authorization.
   - Avoid claiming that a system is secure simply because no findings were identified.

## Finding format

For each finding, include:

- **Severity:** Critical, High, Medium, Low, or Informational.
- **Location:** exact file, configuration key, or affected component.
- **Evidence:** the vulnerable behavior or security assumption.
- **Attack scenario:** the conditions under which the weakness could be exploited.
- **Impact:** the potential consequence.
- **Recommendation:** a specific, actionable mitigation.
- **Verification:** how the correction can be tested.

Prioritize findings using actual exploitability and impact. Do not assign severity solely because a weakness belongs to a familiar vulnerability category.

## Final report

Include the scope, assumptions, findings ranked by severity, recommended mitigations, tests performed, and remaining risks. Clearly state what was not reviewed.
