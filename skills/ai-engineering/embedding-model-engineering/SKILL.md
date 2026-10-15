---
name: embedding-model-engineering
description: "Select, benchmark, version, and deploy embedding models for semantic search and retrieval using representative data, vector-space compatibility, and task-level metrics."
---

# Embedding Model Engineering

## Goal
Choose and operate embedding models based on retrieval outcomes and system constraints, not benchmark claims alone.

## Workflow
1. Define retrieval tasks, language/domain coverage, corpus size, update rate, latency budget, privacy requirements, and hardware constraints.
2. Build a labeled query-document set with hard negatives, exact-match cases, multilingual cases, and long/short documents.
3. Establish a baseline with the current model and retrieval configuration.
4. Compare candidate models on recall@k, MRR/nDCG, downstream answer quality, latency, throughput, vector dimensions, memory, and cost.
5. Use each model's intended query/document encoding conventions, pooling, normalization, and maximum input length. Verify these details from model documentation.
6. Version model ID, revision, preprocessing, normalization, dimensions, and index configuration together.
7. Re-embed consistently when changing embedding spaces. Do not mix vectors from incompatible models or revisions in one index unless compatibility has been demonstrated.
8. Plan backfill, dual-index migration, rollback, and index freshness for production changes.
9. Monitor retrieval quality and drift as the corpus, query mix, and model evolve.

## Data and evaluation hygiene
- Avoid training/evaluating on duplicated or leaked query-document pairs.
- Split by source or time where needed to reduce leakage.
- Include hard negatives that look similar but are not relevant.
- Evaluate access filters and tenant boundaries as part of retrieval, not as an afterthought.
- Preserve original text and metadata for citation and debugging.

## Deliverable
Provide dataset design, model candidates, benchmark results, preprocessing settings, index migration plan, versioning, and known failure modes.

## References
- Sentence Transformers: https://www.sbert.net/
- Hugging Face embedding models: https://huggingface.co/docs/transformers/tasks/sentence_similarity
- Ragas retrieval metrics: https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/
