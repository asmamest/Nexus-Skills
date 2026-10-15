---
name: llm-observability
description: "Instrument LLM and agent applications with traces, spans, metrics, redaction, cost/latency analysis, and actionable failure diagnosis."
---

# LLM Observability

## Goal
Make AI application behavior inspectable while protecting user data. Observability should answer what happened, where it failed, how much it cost, and whether quality is changing.

## Workflow
1. **Define operational questions.** Identify the failures and service-level objectives the team needs to detect: timeouts, tool errors, retrieval misses, quality regressions, latency, or cost spikes.
2. **Trace one request end to end.** Correlate request, model call, retrieval, reranking, tool invocation, subagent handoff, validation, and final response with trace/span identifiers.
3. **Capture useful metadata.** Record model/provider/version, prompt or template version, tool name, retrieval count, token usage, latency, retry count, status, and error category where available.
4. **Redact by default.** Avoid storing secrets, access tokens, raw personal data, private documents, or full prompts unless there is a documented need and lawful, access-controlled retention policy.
5. **Define metrics.** Track request volume, error rate, p50/p95/p99 latency, token/cost per request, tool failure rate, timeout rate, queue depth, and evaluation-derived quality signals.
6. **Connect traces to evaluations.** Sample traces for human review, run offline evaluations on representative cases, and create regression alerts from stable quality metrics.
7. **Set alerts on actionable conditions.** Use thresholds, baselines, and sustained windows to avoid noisy alerts. Route alerts to an owner and include a diagnostic next step.
8. **Test telemetry itself.** Verify correlation IDs, missing spans, exporter failure behavior, cardinality, sampling, redaction, and retention.

## Safety and privacy
- Treat prompts and tool results as potentially sensitive.
- Do not put user IDs, raw queries, or document contents into high-cardinality metric labels.
- Restrict trace access and define retention/deletion policies.
- Use sampling carefully; retain enough traces for rare high-impact failures.
- Separate application telemetry from model evaluation data and production secrets.

## Debugging procedure
1. Find the failing trace and identify the first incorrect span.
2. Compare expected vs actual input/output at that boundary, using redacted evidence.
3. Reproduce with a sanitized fixture.
4. Fix the underlying layer and add a regression test.
5. Verify telemetry shows the expected recovery and no new privacy leak.

## Deliverable
Provide instrumentation points, trace schema, metric definitions, redaction/retention controls, dashboards/alerts, and a sample diagnostic path.

## References
- OpenTelemetry: https://opentelemetry.io/docs/
- GenAI semantic conventions: https://opentelemetry.io/docs/specs/semconv/gen-ai/
- LangSmith tracing: https://docs.smith.langchain.com/
