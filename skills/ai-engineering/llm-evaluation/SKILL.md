---
name: llm-evaluation
description: Evaluate large language model applications using representative datasets, explicit criteria, automated metrics, human review, and regression tests. Use when comparing models, prompts, RAG pipelines, agents, or production LLM behavior.
---

# LLM Evaluation

## Objective

Measure whether an LLM application meets its requirements and identify regressions through repeatable, evidence-based evaluation.

## Workflow

1. **Define success**
   - Translate product requirements into observable criteria.
   - Identify unacceptable failures, such as fabricated facts, unsafe outputs, or incorrect tool use.
   - Define quality, latency, cost, and reliability targets before comparing systems.

2. **Build an evaluation dataset**
   - Collect representative inputs from expected usage patterns.
   - Include common cases, edge cases, ambiguous requests, and known failure examples.
   - Include multilingual or domain-specific examples when relevant.
   - Remove or protect sensitive information and verify that test data can be used appropriately.
   - Separate development examples from held-out evaluation examples to reduce overfitting.

3. **Choose evaluation methods**
   - Exact match or structured-output validation for constrained tasks.
   - Task-specific metrics such as precision, recall, or F1 when appropriate.
   - Human assessment for subjective or high-impact outcomes.
   - Model-based judging when useful, with documented rubrics and known limitations.
   - Operational measurements for latency, token consumption, cost, timeouts, and failure rates.

4. **Design reliable scoring**
   - Write explicit rubrics with observable scoring criteria.
   - Use the same test set and comparable conditions for competing configurations.
   - Fix or record model versions, prompts, parameters, tools, and retrieval settings.
   - Repeat stochastic evaluations when variation could change conclusions.
   - Validate model-based judges against human-reviewed examples.

5. **Analyze failures**
   - Group failures by category, severity, and frequency.
   - Distinguish data problems, retrieval failures, model reasoning errors, formatting errors, and infrastructure failures.
   - Inspect individual examples rather than relying only on aggregate scores.
   - Investigate regressions in important subsets, not just overall averages.

6. **Compare changes**
   - Establish a baseline before changing a model, prompt, dataset, or architecture.
   - Report absolute performance and change relative to the baseline.
   - Consider sample size, uncertainty, and practical significance.
   - Check whether improvements in one metric degrade another.

7. **Automate regression evaluation**
   - Run fast, high-value checks in development and CI.
   - Schedule broader evaluations when their cost makes every-commit execution impractical.
   - Use thresholds justified by the task and baseline.
   - Store dataset versions, results, configurations, and evaluation code.

## Judge limitations

LLM judges can be biased by answer length, presentation, model family, or position. They may also miss subtle factual errors. Do not treat a judge score as ground truth without validation.

## Safety and robustness

Test prompt injection, sensitive-data disclosure, harmful requests, unsupported claims, and attempts to bypass intended behavior. Assess these risks in the context of the application and its access boundaries.

## Final report

Include:
- Evaluation objective and dataset version.
- Models and configurations compared.
- Metrics, rubric, and scoring method.
- Results with uncertainty where feasible.
- Representative failures and trade-offs.
- Limitations and recommended next experiments.
