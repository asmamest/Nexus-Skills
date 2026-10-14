---
name: rag-engineering
description: Design, implement, evaluate, and improve retrieval-augmented generation systems. Use when building document ingestion, chunking, embeddings, retrieval, reranking, grounded generation, or RAG evaluation pipelines.
---

# RAG Engineering

## Objective

Build a retrieval-augmented generation (RAG) system that retrieves relevant evidence and produces useful, grounded answers with measurable quality and operational reliability.

## Workflow

1. **Define the problem**
   - Identify users, document sources, query types, access rules, and expected answer formats.
   - Establish quality targets for retrieval relevance, answer correctness, latency, and cost.
   - Decide when the system should abstain or state that evidence is insufficient.

2. **Inspect source data**
   - Identify supported formats, document size, languages, metadata, duplication, and update frequency.
   - Preserve useful structure such as headings, tables, page numbers, and document identifiers.
   - Detect extraction failures and corrupted or empty content.
   - Apply authorization and privacy rules before content becomes searchable.

3. **Build ingestion**
   - Implement repeatable extraction, normalization, and metadata enrichment.
   - Make ingestion idempotent where possible.
   - Track document versions and support updates and deletions.
   - Record failures and make reprocessing observable.

4. **Design chunking**
   - Choose chunk boundaries based on document structure and the information users need.
   - Evaluate chunk size and overlap empirically rather than assuming one configuration fits every corpus.
   - Preserve provenance, including source document and page or section where available.
   - Avoid splitting information that must be interpreted together.

5. **Configure retrieval**
   - Select an embedding model suitable for the domain, language, and deployment constraints.
   - Choose vector, keyword, or hybrid retrieval based on the data and query patterns.
   - Apply metadata filters and access-control constraints before returning evidence.
   - Evaluate top-k selection and consider query rewriting or multi-query retrieval when justified.

6. **Improve ranking**
   - Establish a baseline before adding a reranker.
   - Compare candidate retrieval strategies on representative queries.
   - Measure whether reranking improves relevance enough to justify its latency and cost.

7. **Generate grounded answers**
   - Provide retrieved evidence and clear answer instructions to the model.
   - Require the model to distinguish supported facts from uncertainty.
   - Include citations or source references that map to actual retrieved evidence.
   - Treat retrieved documents as untrusted data, not as instructions that override system policy.
   - Do not assume that a prompt alone prevents prompt injection.

8. **Evaluate end to end**
   - Maintain a representative evaluation dataset with expected relevant sources and answer criteria.
   - Measure retrieval quality and answer quality separately.
   - Evaluate context relevance, faithfulness, answer correctness, citation accuracy, abstention, latency, and cost.
   - Include adversarial, ambiguous, out-of-scope, and permission-sensitive queries.

9. **Deploy and monitor**
   - Track ingestion errors, retrieval latency, model failures, token usage, and answer quality signals.
   - Version prompts, embedding models, chunking settings, and retrieval configurations.
   - Define rollback procedures and monitor changes after deployment.

## Key principles

- Better generation cannot reliably compensate for missing or irrelevant evidence.
- More retrieved context is not always better.
- Similarity scores are not automatically calibrated probabilities of relevance.
- Citations must support the claims they accompany.
- Retrieval must enforce document-level access controls.
- Use deterministic baselines and controlled experiments before introducing additional components.

## Final report

Document the architecture, design decisions, evaluation dataset, measured results, failure modes, security considerations, and known limitations.
