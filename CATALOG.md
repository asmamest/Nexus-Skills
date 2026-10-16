
# Nexus Skills Catalog

This catalog is generated/maintained alongside the skill folders. Every listed skill must exist under `skills/` and contain a valid `SKILL.md`. Run `python scripts/validate_skills.py` after editing skills or this file.

> **Safety note:** Skills are executable instructions for an AI agent, not merely documentation. Read the complete skill before installing it, especially when it requests shell commands, network access, credentials, file edits, or deployment actions.

## Software engineering

### `code-review`
- **Path:** `skills/software-engineering/code-review/SKILL.md`
- **Use when:** Reviewing a diff or pull request for correctness, regressions, security risks, and missing tests.
- **Output:** Prioritized findings with file/line references, evidence, impact, and unresolved questions.

### `debugging`
- **Path:** `skills/software-engineering/debugging/SKILL.md`
- **Use when:** Investigating a bug, failing test, crash, or unexpected behavior.
- **Output:** Reproduction, evidence-backed root-cause hypothesis, minimal fix, and verification results.

### `test-engineering`
- **Path:** `skills/software-engineering/test-engineering/SKILL.md`
- **Use when:** Designing or improving automated tests for existing behavior or a new change.
- **Output:** Risk-based test plan, focused tests, and results.

## AI engineering

### `advanced-retrieval-reranking`
- **Path:** `skills/ai-engineering/advanced-retrieval-reranking/SKILL.md`
- **Use when:** Improving retrieval quality with hybrid search, query expansion, filtering, or reranking.
- **Output:** A retrieval strategy, evaluation plan, and measured quality trade-offs.

### `context-engineering`
- **Path:** `skills/ai-engineering/context-engineering/SKILL.md`
- **Use when:** Designing the context supplied to an LLM, including selection, ordering, compression, and token budgets.
- **Output:** A context strategy with relevance controls, budget constraints, and evaluation criteria.

### `embedding-model-engineering`
- **Path:** `skills/ai-engineering/embedding-model-engineering/SKILL.md`
- **Use when:** Selecting, evaluating, fine-tuning, or deploying embedding models.
- **Output:** Model-selection rationale, retrieval benchmarks, and deployment considerations.

### `llm-evaluation`
- **Path:** `skills/ai-engineering/llm-evaluation/SKILL.md`
- **Use when:** Building evaluations for LLM outputs, prompts, or model changes.
- **Output:** Versioned test set, metrics, failure analysis, and release criteria.

### `llm-observability`
- **Path:** `skills/ai-engineering/llm-observability/SKILL.md`
- **Use when:** Monitoring LLM application latency, token usage, errors, quality, and cost.
- **Output:** An observability plan with useful traces, metrics, logs, and privacy safeguards.

### `model-serving-inference`
- **Path:** `skills/ai-engineering/model-serving-inference/SKILL.md`
- **Use when:** Deploying or optimizing model inference for latency, throughput, reliability, and cost.
- **Output:** A serving architecture, benchmark plan, and documented performance trade-offs.

### `multimodal-ai-pipelines`
- **Path:** `skills/ai-engineering/multimodal-ai-pipelines/SKILL.md`
- **Use when:** Building AI pipelines that process or combine text, images, audio, video, or other modalities.
- **Output:** A modality-aware pipeline design, validation strategy, and failure-handling plan.

### `prompt-engineering`
- **Path:** `skills/ai-engineering/prompt-engineering/SKILL.md`
- **Use when:** Designing, structuring, testing, or improving prompts for language models.
- **Output:** A tested prompt, explicit constraints, representative examples, and evaluation criteria.

### `rag-engineering`
- **Path:** `skills/ai-engineering/rag-engineering/SKILL.md`
- **Use when:** Designing, debugging, or evaluating a retrieval-augmented generation pipeline.
- **Output:** Traceable retrieval/generation design, evaluation plan, and known limitations.

### `rag-pipeline-engineering`
- **Path:** `skills/ai-engineering/rag-pipeline-engineering/SKILL.md`
- **Use when:** Engineering an end-to-end RAG pipeline, from ingestion and chunking to retrieval and answer generation.
- **Output:** Pipeline design, failure handling, and end-to-end evaluation.

### `structured-outputs`
- **Path:** `skills/ai-engineering/structured-outputs/SKILL.md`
- **Use when:** Making LLM responses conform to JSON schemas, typed models, or other machine-readable formats.
- **Output:** A validated output contract, parsing strategy, and handling for invalid or incomplete responses.

## Agentic engineering

### `agent-architecture-design`
- **Path:** `skills/agentic-engineering/agent-architecture-design/SKILL.md`
- **Use when:** Designing an AI agent's responsibilities, control flow, tools, state, and boundaries.
- **Output:** An agent architecture with component responsibilities, execution flow, and failure modes.

### `agent-evaluation`
- **Path:** `skills/agentic-engineering/agent-evaluation/SKILL.md`
- **Use when:** Evaluating an agent that plans, calls tools, or executes multi-step workflows.
- **Output:** Task suite, tool-use and safety measures, failure taxonomy, and regression report.

### `agent-harness-engineering`
- **Path:** `skills/agentic-engineering/agent-harness-engineering/SKILL.md`
- **Use when:** Engineering the runtime, tools, context, feedback loops, and safeguards surrounding an AI agent.
- **Output:** A harness design with execution controls, verification loops, observability, and reliability checks.

### `agent-memory-design`
- **Path:** `skills/agentic-engineering/agent-memory-design/SKILL.md`
- **Use when:** Designing an agent's short-term state, persistent memory, retrieval, and memory updates.
- **Output:** A memory architecture with lifecycle rules, retrieval policies, and privacy safeguards.

### `agentic-workflow-testing`
- **Path:** `skills/agentic-engineering/agentic-workflow-testing/SKILL.md`
- **Use when:** Testing multi-step agent workflows, tool interactions, state transitions, and recovery behavior.
- **Output:** Workflow test scenarios, failure-injection cases, and regression criteria.

### `browser-computer-use`
- **Path:** `skills/agentic-engineering/browser-computer-use/SKILL.md`
- **Use when:** Designing or operating agents that interact with websites or graphical interfaces.
- **Output:** A controlled interaction plan with state checks, action verification, and safety boundaries.

### `durable-agent-workflows`
- **Path:** `skills/agentic-engineering/durable-agent-workflows/SKILL.md`
- **Use when:** Building long-running agent workflows that must survive retries, failures, restarts, or interruptions.
- **Output:** A durable execution design with checkpointing, idempotency, retry policies, and recovery paths.

### `human-in-the-loop`
- **Path:** `skills/agentic-engineering/human-in-the-loop/SKILL.md`
- **Use when:** Defining when an agent should request human approval, clarification, or intervention.
- **Output:** Approval gates, escalation rules, and clear boundaries for autonomous actions.

### `mcp-development`
- **Path:** `skills/agentic-engineering/mcp-development/SKILL.md`
- **Use when:** Designing, implementing, reviewing, or testing a Model Context Protocol server or client integration.
- **Output:** Protocol-aware implementation plan, tool/resource design, and security/test checklist.

### `mcp-server-development`
- **Path:** `skills/agentic-engineering/mcp-server-development/SKILL.md`
- **Use when:** Building or maintaining an MCP server that exposes tools, resources, or prompts to AI clients.
- **Output:** A server implementation plan with schema validation, transport considerations, and security checks.

### `multi-agent-orchestration`
- **Path:** `skills/agentic-engineering/multi-agent-orchestration/SKILL.md`
- **Use when:** Coordinating multiple AI agents, their responsibilities, shared state, and handoffs.
- **Output:** An orchestration design with coordination rules, failure handling, and evaluation criteria.

### `tool-calling-design`
- **Path:** `skills/agentic-engineering/tool-calling-design/SKILL.md`
- **Use when:** Designing agent tools, argument schemas, execution policies, and error responses.
- **Output:** A tool interface design with validation, authorization, and failure-handling rules.

## Security and quality

### `agentic-security`
- **Path:** `skills/security-quality/agentic-security/SKILL.md`
- **Use when:** Assessing AI-agent risks such as prompt injection, unsafe tool use, excessive agency, and untrusted data.
- **Output:** Threat model, prioritized mitigations, and security verification steps.

### `security-review`
- **Path:** `skills/security-quality/security-review/SKILL.md`
- **Use when:** Reviewing code or an architecture for common security weaknesses and unsafe trust boundaries.
- **Output:** Risk-ranked findings, exploit preconditions, mitigations, and verification steps.
