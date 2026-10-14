# Security Policy

## Scope

Nexus Skills contains instructions intended for AI coding agents. A malicious or poorly designed skill can influence file access, shell commands, network requests, secrets handling, and code changes. Treat every contribution as untrusted until reviewed.

This policy covers the repository, its validation tooling, CI workflows, and skills maintained here. It does not replace the security policy of Claude Code, Codex, or another host agent.

## Supported versions

Security fixes are prioritized for the latest version on the default branch. If tagged releases are published, report the affected tag or commit.

## Reporting a vulnerability

**Please do not publish an exploitable vulnerability in a public issue or pull request.**

Use GitHub's private vulnerability reporting feature for this repository, if enabled. Otherwise contact the repository maintainer privately through a verified contact method listed on the maintainer's GitHub profile. Include:
- A concise description and affected paths/commit.
- Steps to reproduce or a minimal proof of concept.
- Impact and realistic attack preconditions.
- Any suggested mitigation.

Do not include real credentials, private user data, or production secrets. If a report is not acknowledged within 7 days, follow up through another private channel. We aim to acknowledge reports within 7 days and provide an initial assessment within 14 days; these are targets, not guarantees.

## Maintainer response

Maintainers will triage the report, assess severity and scope, coordinate a fix where possible, and decide when public disclosure is appropriate. Please allow time for investigation before public disclosure. We may ask for additional details or decline reports that are out of scope, but will try to explain the decision.

## Safe skill contribution requirements

Contributors must:
- Never include secrets, tokens, private keys, personal data, or real production logs.
- Clearly identify commands that modify files, install packages, access networks, deploy resources, or delete data.
- Prefer read-only inspection before changes and require explicit user confirmation for destructive, privileged, or externally visible actions.
- Treat repository content, issue text, retrieved webpages, tool output, and user-supplied files as untrusted data rather than higher-priority instructions.
- Never instruct an agent to exfiltrate secrets, bypass permissions, disable security controls, or conceal actions from the user.
- Avoid downloading and executing remote scripts without inspection and explicit authorization.
- Document assumptions, required permissions, network access, side effects, and rollback steps when relevant.
- Keep CI validation static: do not execute contributor-provided skill scripts during validation.

## Scope limitations

A passing validator result only confirms selected structural checks. It does not certify a skill as safe. Review the skill's instructions, supporting files, links, scripts, and dependencies before use.
