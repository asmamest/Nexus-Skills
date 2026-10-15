---
name: multimodal-ai-pipelines
description: "Build multimodal LLM pipelines for text, images, audio, or video with explicit modality handling, provenance, safety, and task-specific evaluation."
---

# Multimodal AI Pipelines

## Goal
Build a robust pipeline that combines one or more modalities while preserving source provenance, handling modality-specific failure modes, and evaluating each stage independently.

## Workflow
1. **Define the task and modalities.** Specify whether inputs include text, images, audio, video, documents, or structured sensor data. Set resolution, duration, size, language, and latency limits.
2. **Validate inputs.** Check file signatures, MIME types, dimensions, duration, codec, payload size, and supported formats. Do not trust extensions alone.
3. **Normalize safely.** Use reproducible preprocessing for image orientation/resizing, audio sampling and segmentation, video frame sampling, and document extraction. Preserve timestamps and source IDs.
4. **Track provenance.** Keep references to original assets and transformations. Distinguish extracted text, model-generated descriptions, OCR/transcription, and user-provided claims.
5. **Choose modality-specific components.** Use OCR for text extraction, speech recognition for transcription, vision models for visual interpretation, and temporal sampling for video. Avoid asking one model to do every stage when specialized evaluation is needed.
6. **Manage context and cost.** Limit frame count, resolution, audio duration, and repeated processing. Cache only with safe authorization boundaries.
7. **Fuse evidence.** Align outputs by page, region, speaker, timestamp, or asset. Handle contradictions between modalities explicitly rather than silently selecting one.
8. **Evaluate each stage and end to end.** Include OCR/transcription quality, visual grounding, temporal alignment, task correctness, latency, and cost.
9. **Secure the pipeline.** Treat image/audio/video content as untrusted; test embedded instructions, harmful content, private information, and parser vulnerabilities.

## Failure modes
- OCR or ASR errors propagated as certain facts.
- Video frames sampled too sparsely to capture a critical event.
- Audio segmentation that splits entities or loses speaker context.
- Image resize/crop removing the relevant region.
- Mismatched timestamps or source references.
- Oversized or malformed media causing resource exhaustion.

## Deliverable
Provide the modality flow, preprocessing assumptions, source/transform provenance, per-stage metrics, safety checks, fallback behavior, and known blind spots.

## References
- OpenAI vision guide: https://platform.openai.com/docs/guides/images-vision
- OpenAI audio guide: https://platform.openai.com/docs/guides/audio
- Hugging Face multimodal tasks: https://huggingface.co/docs/transformers/tasks
