---
title: Manga / Anime Execution Topology and Capability Routing Policy
artifact_id: MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY
artifact_type: execution_topology_capability_policy
version: "1.0"
status: canonical
scope: corpus-wide execution-stage allocation, capability verification, and operator responsibilities
created: 2026-09-13
maintainer: ChatGPT + user
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md
drafted_against_commit: b331a3b746622760db394ac1a79367263236336f
supersedes: null
superseded_by: null
---

# Manga / Anime Execution Topology and Capability Routing Policy

> **Route stages to environments that can actually perform them. Cloud and local are capability profiles, not quality or authority tiers.**

This policy governs where work runs, which session owns a responsibility, and how multiple environments cooperate. It does not replace reasoning classes, analytical methods, evidence standards, continuation authorization, or repository publication controls.

## 1. Responsibility boundary

The [reasoning/model policy](MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md) selects a cognitive workload and model resolution. This file selects an execution arrangement. The [long-series protocol](MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md) defines the preferred phase sequence for long projects. The [handoff contract](MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) defines transfer and acceptance. The [episode bundle specification](MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md) continues to own bundle semantics and continuous-video evidence escalation.

The live authority records and [pre-commit checklist](../policies/CHANGE_INTEGRATION_CHECKLIST.md) control all repository mutation. This file grants no additional access, publication rights, or automation authority.

## 2. Vocabulary

An **artifact** has a stable identity, analytical responsibility, source scope, authority state, and canonical home. A **stage** is a bounded operation contributing to one or more artifacts. A **session** is a temporary execution context. An **execution topology** is the arrangement of stages and their owners. A **handoff** transfers responsibility and evidence state, not authority merely by moving files.

Distinguish four technical dimensions:

| Dimension | Examples of what to record |
|---|---|
| Product surface | Chat, Work, Codex, API, another identified application |
| Tool-runtime location | Hosted sandbox, owner workstation, authorized remote workstation, GPU worker |
| Model execution | Observed model/provider or explicitly unknown; locally hosted model only when actually used |
| Evidence/transport route | Local file, pinned Git snapshot, Drive object, attachment, derivative bundle, authenticated service |

A locally controlled EC2 workstation belongs to the owner-controlled tool-runtime profile even though its hardware is hosted remotely. A local terminal does not imply local LLM inference, offline operation, or absence of data transmission. A remote GPU worker is a capability provider, not automatically a new model or allowance pool.

## 3. Supported arrangements

| Arrangement | Meaning |
|---|---|
| `LOCAL_ONLY` | All stages use an adequate owner-controlled tool environment. |
| `CLOUD_ONLY` | All stages use an adequate hosted environment under the authorized source/access boundary. |
| `HYBRID_STAGED` | Stages pass a developing artifact or evidence state between environments in sequence. |
| `HYBRID_PARALLEL` | Distinct scoped contributions run independently against an agreed snapshot and converge through a designated integrator. |

These are execution descriptors, not analytical authority states. They do not require new folders or duplicate monographs. A single artifact may pass through multiple sessions under the same ID and intended canonical path.

A project may use a staged overall lifecycle and bounded parallel specialist work inside one phase. Do not create more topology categories merely to describe every product name or host.

## 4. Default ownership

For long-series work, the owner's preferred arrangement is:

- Local Work/Codex owns primary-source sequential analysis, synchronized longitudinal ledgers, source tooling, checkpoints, and ordinary project Git operations.
- Fresh cloud Pro Chat preferentially authors frameworks/architectures, major monographs, and substantial retrospective synthesis.
- Local Work/Codex receives and integrates these outputs, completes required source/AV work, verifies semantic and structural consistency, and performs authorized repository publication.

The detailed phase gates are owned by the long-series protocol rather than duplicated here. Either environment can design architecture when adequately supplied. A cloud session is not restricted to outlining or drafting summaries; it may be the substantive analytical author.

A Git-capable local integrator is the default ordinary writer for this topology, not a replacement for existing specialized owners. In particular, character discovery and `characters/registry.jsonl` plus `CHARACTER_ANALYSIS_INDEX.md` remain with the authorized curation agent. Housekeeping-owned outputs remain with their designated maintenance process. The integrator coordinates necessary repairs instead of acquiring those responsibilities silently.

Read-only cloud Git retrieval is optional when reliable and authorized. Prefer a verified snapshot package when connector behavior is unreliable. Cloud synthesis must not depend on the ability to commit.

## 5. Capability verification before assignment

Do not classify a task as executable solely because the application accepts the extension or the file appears in a listing. Distinguish:

1. **Transport:** can the object be retrieved or delivered intact?
2. **Processing:** can it be opened, decoded, indexed, or transformed at adequate fidelity?
3. **Inspection:** which actual model or human process examines the relevant content?
4. **Interpretation:** what claims can that inspection support?
5. **Persistence:** can the evidence routes and results survive session loss and reach their proper durable home?

Verify only capabilities material to the assigned stage. A short practical probe should check the intended source type, language, scale, and access route, without claiming to benchmark the entire model.

Suggested profile fields:

```yaml
execution_profile:
  product_surface: "<observed surface>"
  tool_runtime_location: "<hosted or owner-controlled runtime>"
  observation_date: "<date>"
  capability_scope: "<source types and limits actually checked>"
  source_transport: "<verified route>"
  filesystem_read: "VERIFIED | UNVERIFIED | UNAVAILABLE"
  filesystem_write: "VERIFIED | UNVERIFIED | UNAVAILABLE"
  image_inspection: "VERIFIED | UNVERIFIED | UNAVAILABLE"
  audio_content_inspection: "VERIFIED | UNVERIFIED | UNAVAILABLE"
  continuous_av_inspection: "VERIFIED | UNVERIFIED | UNAVAILABLE"
  git_write: "NOT_ASSIGNED | VERIFIED | UNVERIFIED | UNAVAILABLE"
  inspection_method: "<actual model/tool/human route, not a capability guess>"
```

This is documentation vocabulary, not a new executable repository schema. Put a shared profile in the existing current-state or execution record; do not copy a full capability inventory into every reading.

## 6. Audio and audiovisual evidence discipline

Small audio objects can be good cloud inputs when the session has a verified audio-inspection route. Their small size alone proves neither perceptual capability nor interpretive adequacy. An ASR transcript does not establish timbre, breath, prosody, or performed emotional delivery. Signal measurements can support bounded acoustic observations; they do not independently establish a character's emotion or intention.

Likewise, local access to a 1080p or 2160p video and the ability to run ffmpeg do not establish native continuous-video perception. Record whether the actual route used continuous AV, bounded clips, frame sequences plus aligned audio, transcript-only analysis, numerical measurements, or human observations.

Preserve timestamps, language/track identity, source/derivative relationships, and sampling limitations. Never label a sampled reconstruction as direct continuous inspection. Where evidence only establishes endpoints, do not infer the movement between them.

Use the existing `VIDEO_NOT_REQUIRED`, `VIDEO_TARGETED_ESCALATION`, and `VIDEO_FULL_EPISODE_ESCALATION` decisions. They describe evidence need, not capability success. An escalation remains unresolved until the required evidence has actually been inspected or the claim/scope has been explicitly and legitimately narrowed.

## 7. File size, transport, and runtime limits

The owner reports that hosted Chat environments have been less suitable for large source videos and more fragile for GitHub operations, while useful for many smaller objects and substantial synthesis. Treat this as an owner-reported operational profile, not a universal platform law or a claim that every cloud system rejects 1080p video.

Routing depends on bytes, duration, codec, frame rate, image detail, object counts, decode/tool resources, supported modalities, permissions, and connector behavior. Resolution alone is not the deciding variable.

The OpenAI File Uploads FAQ checked on 2026-09-13 lists a 512 MB per-file upload limit and other type/rate/storage limits. That upload ceiling does not certify connector transfer, media decoding, context ingestion, or video comprehension. [O5]

Do not duplicate an asserted universal Drive limit here. Apply the episode-bundle specification's dated transport guidance within its scope and reverify actual routes when material. A policy preference for local processing does not authorize access to the owner's computer during a cloud-only task.

Prefer the smallest faithful evidence object that preserves the question. Chunking must retain chronology, source mappings, overlap where needed, and cross-clip context. Supplying many small files does not guarantee that all were read; account for retrieval and inspection coverage.

## 8. Three storage and authority planes

Maintain the distinction established by the project source map and live authority records:

- **Evidence plane:** primary and derived source objects, ordinarily retained/routed in the designated Drive evidence surface. Deterministic transformation does not by itself turn evidence into interpretation.
- **Analytical plane:** integrated Git interpretations, methods, monographs, readings, ledgers, and routing information within declared authority scope.
- **Working/build plane:** temporary session outputs, caches, extraction databases, local media copies, transport bundles, and intermediate candidates.

A local path, cloud attachment, or downloaded ZIP is not canonical merely because it is accessible. Promote only the proper objects through the existing authority process. Do not place raw media, large transcript dumps, credentials, private source inventories, or unreviewed binaries into the public repository.

A temporary transfer archive is not a second analytical corpus and is not to be committed merely to prove that a handoff occurred. Keep sanitized provenance sufficient to recover adopted changes.

## 9. Ownership and concurrency

Assign one active mutable owner per artifact or cumulative state surface. Different sessions may own distinct specialist documents against the same frozen snapshot; they may not concurrently overwrite the same monograph, ledger, or entrypoint without explicit reconciliation.

The designated integration owner records input base commit, named output paths, proposed revisions, and final disposition. Snapshot-based analysis may proceed while the series branch advances, but publication requires checking what changed and whether it affects the draft.

Use a three-way comparison where applicable: handed-off base, returned candidate, current target. A changed head is not automatic rejection, but it prohibits blind replacement. Preserve concurrent work and route substantive conflicts to evidence-based adjudication. The handoff contract specifies the receipts.

After an ambiguous write or timeout, inspect actual remote state before retrying. Connector instability is a reason to change the execution route or emit a proposal, not to reconstruct an existing document from memory. Follow the checklist's exact-head, blob, full-diff, and readback requirements.

## 10. Environment changes do not authorize reinterpretation

Preserve supported analysis across a relay. A receiving session should not replace extensive prose with a shorter generic summary, drop counterarguments, rename the artifact, or repeat the source run merely to make the work feel locally authored.

Preservation is not immunity from criticism. Revise claims when new evidence, stronger counterevidence, a demonstrated error, or a governing scope distinction warrants it. Use the established `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, and `OPEN` vocabulary rather than silently overwriting intellectual history.

A local AV stage can change a central interpretation, not merely decorate it. Conversely, visual completion need not disturb well-supported textual findings unrelated to that channel.

## 11. Choosing exceptions

Use the simplest adequate arrangement. Prefer local-only when source access dominates, the artifact is bounded, or transfer overhead exceeds the expected benefit. Prefer cloud-only when all required evidence and capabilities are available and the authorized publication route can be completed separately or is not in scope. Use hybrid parallel work when independence or throughput has a defined value and integration capacity exists.

Where anchoring is a concern, an AV reviewer can record bounded observations before reading the prior interpretation, then compare them. This is an optional evaluation design, not a requirement to duplicate all analysis.

No environment preference may waive evidence requirements, silently alter the source boundary, or create unapproved API spend. Insufficient capability should produce bounded progress and an explicit unresolved requirement, not a false completion claim.

## 12. Maintenance and evaluation

Keep durable topology semantics here; keep volatile model/billing facts in the reasoning policy's dated snapshot and runtime observations in the stage record. Evaluate the arrangement by accepted analytical quality, missing-evidence rate, transfer defects, retrieval failures, integration/rework effort, and actual resource use.

Changes to source fidelity, stage ownership, or promotion responsibility require explicit review. A product-name change alone does not require restructuring mature series. No new automation, validator, or public workflow is established by this prose policy.

## Reference

- [O5] OpenAI Help Center, *File Uploads FAQ*, checked 2026-09-13: `https://help.openai.com/en/articles/8555545-file-uploads-faq`

## Changelog

### v1.0 - 2026-09-13 - Proposed initial policy

Defines stage-level environment allocation, verified capability profiles, cloud/local complementarity, single-owner integration, and evidence/working/analytical plane separation. The owner's long-series workflow is implemented in the companion protocol rather than treated as a universal ranking of environments.
