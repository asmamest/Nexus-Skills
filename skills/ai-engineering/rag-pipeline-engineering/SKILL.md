---
name: rag-pipeline-engineering
description: "Build or improve retrieval-augmented generation pipelines, from document ingestion and chunking to retrieval, grounding, citations, and production evaluation."
---

# RAG Pipeline Engineering

## Goal
Build a retrieval-augmented generation (RAG) pipeline that retrieves authorized, relevant evidence and uses it to answer questions with traceable support. RAG reduces some knowledge gaps; it does not guarantee correctness.

## Workflow
1. **Define the knowledge task.** Identify query types, source systems, freshness requirements, access controls, languages, document types, and answerability criteria.
2. **Inventory and ingest.** Extract text and structure from supported formats. Preserve headings, tables, page/section identifiers, source URI, timestamp, tenant/ACL metadata, and document version.
3. **Clean carefully.** Remove boilerplate and duplicates without deleting qualifications, table relationships, code, or critical context. Record extraction failures.
4. **Chunk semantically.** Prefer section-aware boundaries and preserve parent/child relationships. Tune chunk size and overlap using evaluation rather than defaults alone.
5. **Select retrieval.** Compare lexical search, dense vectors, hybrid retrieval, metadata filters, and domain-specific query expansion. Enforce authorization filters before returning content.
6. **Rerank when justified.** Rerank a bounded candidate set if measured gains outweigh latency and cost. Preserve source metadata through every transformation.
7. **Construct grounded context.** Deduplicate, order evidence, cap token budget, and instruct the model to distinguish supported claims from missing evidence.
8. **Generate with citations.** Make citations refer to actual retrieved chunks or stable document locations. Validate citation IDs before returning them.
9. **Handle insufficient evidence.** Ask a clarifying question, search again under a bounded policy, or abstain. Do not fabricate a citation or answer merely to appear helpful.
10. **Evaluate end to end.** Test ingestion, retrieval, answer quality, permissions, latency, and cost separately and together.

## Evaluation dimensions
- Retrieval: recall@k, precision@k, MRR/nDCG where appropriate.
- Answer: correctness, faithfulness to evidence, relevance, completeness, citation validity.
- Operations: index freshness, ingestion errors, p95 latency, token use, cost, and failure rate.
- Security: cross-tenant retrieval, ACL enforcement, poisoned documents, prompt injection, sensitive-data exposure.

## Design decisions
- Use metadata filtering for tenant, time, type, and access scope.
- Reindex or incrementally update documents with idempotent jobs and deletion handling.
- Version chunking, embedding model, index configuration, and prompt together.
- Consider reranking, query rewriting, multi-query, or agentic retrieval only when a baseline demonstrates a gap.
- Keep a deterministic baseline before adding agent loops.

## Avoid
- Assuming vector similarity equals relevance.
- Treating retrieved text as trusted instructions.
- Losing provenance during chunking or reranking.
- Evaluating only a few hand-picked happy paths.
- Exposing documents because the model was asked to respect permissions; permissions must be enforced by the retrieval layer.

## Deliverable
Provide a pipeline diagram or sequence, ingestion/chunking choices, retrieval configuration, citation strategy, evaluation dataset and results, access-control design, and known limitations.

## References
- Microsoft AI Agents for Beginners, Agentic RAG: https://github.com/microsoft/ai-agents-for-beginners/tree/main/05-agentic-rag
- Ragas metrics: https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/
- Anthropic contextual retrieval: https://www.anthropic.com/news/contextual-retrieval
