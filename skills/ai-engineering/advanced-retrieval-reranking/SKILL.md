---
name: advanced-retrieval-reranking
description: "Improve search relevance with hybrid retrieval, query rewriting, metadata filtering, reranking, and measurable retrieval experiments for RAG and agent tools."
---

# Advanced Retrieval and Reranking

## Goal
Improve retrieval quality through controlled experiments. Choose retrieval complexity based on observed failure patterns, not trend-following.

## Workflow
1. **Build a query set.** Include common, rare, ambiguous, multi-hop, typo-heavy, multilingual, and unanswerable queries. Label relevant documents or passages.
2. **Measure a baseline.** Record recall@k, precision@k, MRR or nDCG as appropriate, latency, index cost, and query cost.
3. **Diagnose the failure.** Distinguish missing corpus coverage, bad parsing, chunk-boundary loss, lexical mismatch, semantic mismatch, stale data, and ACL filtering mistakes.
4. **Choose a retrieval method.** Use lexical search for exact terms/identifiers, dense retrieval for semantic similarity, and hybrid fusion when both matter. Keep filters server-side and authorization-aware.
5. **Try query transformations.** Rewrite unclear queries, generate alternate queries, or decompose multi-part questions only when evaluations show benefit. Keep original query and transformations in traces.
6. **Rerank candidates.** Retrieve a sufficiently broad candidate set, rerank with a cross-encoder or model-based ranker when useful, then pass a small evidence set to generation.
7. **Preserve diversity and provenance.** Avoid many near-duplicate chunks from one source. Keep source IDs and exact evidence spans.
8. **Test failure handling.** Include no-result, conflicting-source, stale-source, and permission-filtered cases.
9. **Ship behind an evaluation gate.** Compare to the baseline on a held-out set before replacing the production strategy.

## Practical considerations
- Tune top-k and chunk sizes jointly; they are not independent knobs.
- Query expansion can increase recall but also introduce drift and latency.
- Rerankers can improve ordering but cannot recover documents that initial retrieval never found.
- Metadata filters must not be removed merely to increase recall.
- Use source freshness and authority as explicit ranking signals when the task requires them.
- Avoid scoring the same model's output with a circular metric without calibration or human spot checks.

## Deliverable
Summarize baseline, diagnosed error classes, experiments, metric deltas, latency/cost tradeoffs, security constraints, and the chosen configuration.

## References
- Ragas metrics: https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/
- Elasticsearch hybrid search: https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html
- OpenSearch hybrid search: https://opensearch.org/docs/latest/search-plugins/hybrid-search/
