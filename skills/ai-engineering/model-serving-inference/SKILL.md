---
name: model-serving-inference
description: "Design efficient and reliable LLM inference or model-serving systems, including batching, streaming, quantization, caching, capacity planning, and failure handling."
---

# Model Serving and Inference

## Goal
Serve models against explicit quality, throughput, latency, availability, privacy, and cost requirements. Optimize measured bottlenecks rather than assuming one serving stack fits every model.

## Workflow
1. **Specify workload.** Estimate request rates, prompt/output token distributions, concurrency, context lengths, streaming needs, SLA, model size, and hardware constraints.
2. **Establish baseline.** Measure time to first token, inter-token latency, end-to-end p50/p95/p99, throughput, GPU/CPU/memory utilization, error rate, and cost per successful request.
3. **Select deployment mode.** Compare hosted APIs, dedicated endpoints, self-hosted runtimes, and edge/local inference based on control, scale, data residency, and operational capacity.
4. **Tune safely.** Evaluate batching, continuous batching, KV-cache behavior, quantization, speculative decoding, prefix caching, and request limits against representative prompts and outputs.
5. **Preserve quality.** Run task-level and safety evaluations after changing precision, model version, tokenizer, sampling, or serving configuration.
6. **Protect capacity.** Set concurrency limits, queue bounds, timeouts, cancellation, backpressure, and rate limits. Return useful overload errors instead of unbounded queuing.
7. **Handle failures.** Use bounded retries with jitter for transient failures, idempotency for retried actions, and carefully evaluated fallbacks. Do not retry permanent invalid requests indefinitely.
8. **Roll out gradually.** Use canary traffic, shadow comparisons where safe, health checks, rollback criteria, and pinned model/runtime versions.
9. **Monitor drift and cost.** Watch latency, throughput, token distribution, quality, hardware saturation, and provider changes.

## Performance dimensions
- Time to first token (TTFT) and inter-token latency for streaming.
- End-to-end latency and successful tasks per second.
- Tokens per second and cost per successful task.
- Memory headroom, queue time, cache hit rate, and failure/retry rates.

## Avoid
- Reporting throughput without concurrency and workload details.
- Comparing systems with different prompt/output lengths or quality targets.
- Enabling cache reuse across users or tenants when context isolation cannot be guaranteed.
- Using quantization or caching without regression tests and security review.
- Treating a healthy process as proof the model endpoint is serving correct results.

## Deliverable
Document workload assumptions, benchmark methodology, runtime/model versions, capacity limits, rollout/rollback plan, quality impact, and operating metrics.

## References
- vLLM documentation: https://docs.vllm.ai/
- Hugging Face Text Generation Inference: https://huggingface.co/docs/text-generation-inference/index
- NVIDIA TensorRT-LLM: https://nvidia.github.io/TensorRT-LLM/
