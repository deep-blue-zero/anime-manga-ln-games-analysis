---
title: Manga / Anime Execution Topology and Capability Routing Policy
artifact_id: MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY
artifact_type: execution_topology_capability_policy
version: "1.2"
status: canonical
scope: corpus-wide execution-stage allocation, capability verification, operator responsibilities, and multi-agent analytical participation in source readings
created: 2026-09-13
last_updated: 2026-11-15
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

Owning a stage makes a session its accountable principal and integrator; it does not make a substantive source reading a single-agent task. Section 4.1 sets the analytical participation every such reading requires, in any arrangement.

A Git-capable local integrator is the default ordinary writer for this topology, not a replacement for existing specialized owners. In particular, character discovery and its outputs, the `characters/registry/` partitions plus the generated `CHARACTER_ANALYSIS_INDEX.md` and `characters/index/` pages, remain with the authorized curation agent. Housekeeping-owned outputs remain with their designated maintenance process. The integrator coordinates necessary repairs instead of acquiring those responsibilities silently.

Read-only cloud Git retrieval is optional when reliable and authorized. Prefer a verified snapshot package when connector behavior is unreliable. Cloud synthesis must not depend on the ability to commit.

<a id="multi-agent-source-reading"></a>

### 4.1 Multi-agent source reading

> **Every newly undertaken substantive sequential source reading uses a multi-agent analytical workflow, with an accountable principal analyst and genuinely independent, source-aware analytical participation. No such reading is accepted as complete solely on the basis of a single agent's unreviewed interpretation.**

This is a binding requirement for substantive source readings in every medium and project, regardless of model provider, product name or reasoning configuration. The environment preferences elsewhere in this policy and in the long-series protocol may be varied by task; this section may not, except through the configurations of Section 4.1.2 and the owner route of Section 4.1.7. `LOCAL_ONLY` and `CLOUD_ONLY` arrangements satisfy it through multiple independent agents or sessions; `HYBRID_STAGED` and `HYBRID_PARALLEL` remain available and are not required for it. Other policies refer to this section rather than restating it. Its purpose is better evidence coverage, interpretive scrutiny and durable analytical quality; agent count, output volume and procedural complexity are not ends in themselves.

#### 4.1.1 Scope

A substantive sequential source reading is the analytical core of an atomic sequential operation ([continuation policy](MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) Section 2): the canonical deep reading or equivalent unit artifact for a volume, episode, chapter, event, route, commu or other source unit, together with the interpretive state it advances. The requirement also covers a newly authorized source reread or major reanalysis generation and the source-reading stage of a multi-medium or game project. It does not by itself extend to source inventory, locks and extraction, bootstrap and architecture work, mechanical ledger routing, or retrospective synthesis and monographs, which keep their own review standards (for monographs, initiation Section 5.5.1). Later evidence completion or correction of an accepted reading follows its own route, such as the audiovisual reconciliation protocol or claim revision, unless it is authorized as a reread.

#### 4.1.2 Responsibilities and configuration

| Responsibility | Duties |
|---|---|
| Principal analysis | Complete required inspection of the admitted source unit through its governing inspection lanes; narrative and literary interpretation; prospective analysis where the method requires it; evidence-aware synthesis; the integrated source-facing reading; the project's established analytical responsibilities; final cross-agent reconciliation. The principal is normally the designated analytical integrator, who reconciles contributions and remains accountable for the canonical output; repository publication remains a separate responsibility under this policy and the checklist. |
| Independent specialist contribution | Substantive source-grounded work on an assigned analytical dimension by at least one independently operating agent. |
| Independent critical review | Challenge of material findings: source attribution, locators, temporal boundaries, unsupported inferences, missing counterexamples, character-state errors, conflicting interpretations and information lost during integration. The reviewer inspects diagnostic source evidence directly before accepting the principal's interpretation. |

Select specialist responsibilities by source medium, analytical objectives, evidence density and the project's method. Examples are character behavior and relationships; ordinary-life evidence and personal preferences; Japanese or other original-language analysis; narration and focalization; chronology and information-state tracking; causality and rule enforcement; manga visual grammar and page composition; anime performance, cinematography, sound and editing; game route and state transitions and player-information boundaries; and other source-specific dimensions. No project needs every specialist. Several agents writing redundant general summaries to reach a count do not satisfy this section.

**Default configuration.** A substantial narrative source unit has a principal, at least one independently contributing specialist, and an independent critical reviewer who is normally distinct from that specialist. The same default applies to every other substantive unit unless the reduced configuration is justified. For long or analytically complex units, distribute specialist responsibilities among several agents when this materially improves coverage, accuracy or preservation.

**Reduced configuration.** An unusually bounded unit may combine the specialist and review responsibilities in one separate independent context, only when genuine independence, source verification, review quality and the applicable acceptance criteria remain satisfied, and the reason is recorded in the unit's transaction record. An architecture may name unit types eligible for it, such as a recurring class of very short live-service units; each use still records its reason. A reduced configuration is not a waiver of independence: no substantive reading has less than a principal plus one genuinely independent, source-aware participant who both contributes and reviews.

The project's architecture records its standing configuration (initiation Section 3.7). A unit may depart from that standing configuration with a recorded reason, but only to another configuration this section permits.

#### 4.1.3 Genuine independence

An independent participant works in an execution context separate from the principal's: a native subagent, a separately initialized session of any already authorized provider or product, or an identified human analyst, always within the authorized source and access boundary. Its context does not inherit the principal's interpretive working state (draft, notes or conclusions) beyond what its assignment requires. It has its own access to the authorized source frontier and a stated assignment, and it forms its own observations from the source before adopting the principal's conclusions, as far as its responsibility allows. Where practical, the reviewer examines the decisive source passages before reading the candidate's interpretation of them.

Delegation must produce identifiable analytical or evidentiary contributions. None of these establishes compliance: labeling sections of one agent's output as separate agents; one context playing several analysts; a participant that repeats the principal's conclusions; a review that approves a draft without meaningful inspection. Model or provider diversity is neither required nor sufficient.

#### 4.1.4 Knowledge boundaries

Orchestration never weakens source-admission or prospective controls:

- agents inspect only the currently authorized source frontier;
- no agent uses later, unadmitted narrative information to reinterpret an earlier prospective freeze;
- prospective claims are frozen before exposure to their resolution;
- each contribution states its actual knowledge and exposure boundary;
- a specialist's later finding does not silently alter an earlier frozen judgment; it enters through the claim-revision route;
- independence compromised by an accidental spoiler or handoff contamination is disclosed, and the affected contribution loses independent or prospective credit for whatever the exposure touched;
- an uncontaminated independent agent may provide a separately attributable prospective account, frozen before its own exposure, alongside a principal forecast that exposure has limited.

Parallel work is allowed only when it preserves the actual source and temporal boundaries. Retrospective synthesis may use the full admitted corpus after the applicable sequential boundary is closed.

#### 4.1.5 Durable contributions and reconciliation

Material findings of other participants survive beyond transient chat. From the unit's durable record, the integrator and a later reader can recover each participant's assignment and responsibility; source and temporal boundary; material actually inspected; significant independent observations, with locators; interpretations and rival explanations; corrections and counterexamples; unresolved evidence obligations; and the integrator's final adjudication and disposition of each material finding (the Section 10 transition vocabulary where a claim changes; otherwise whether the finding was adopted, qualified, rejected or left open).

Use existing homes: the checkpoint or transaction record for participation, coverage and reconciliation; the claim-revision and evidence ledgers for changed claims and locators; and the [handoff contract](MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) for transfers that need a packet. This creates no mandatory file per agent, no permanent per-agent character ledger and no competing current reading or monograph; each artifact keeps one identity, analytical responsibility, scope, authority state and canonical home, and each project keeps one current entrypoint. Specialists do not write shared ledgers or the entrypoint concurrently with the integrator (Section 9). Private raw transcripts, source bytes and execution caches stay outside public Git unless separately authorized, so the sanitized public record must itself carry the material findings. The accepted canonical artifact preserves those findings rather than compressing them into a generic summary.

Record actual execution facts: the separation of contexts, roles and, only where observed, model and reasoning settings ([reasoning policy](MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md) Section 12). Never invent model identity, reasoning effort, token use or runtime statistics.

#### 4.1.6 Acceptance

A substantive source-reading transaction is not semantically complete merely because the principal produced prose. Within the existing atomic completion (continuation Section 2) and the handoff contract's semantic acceptance (Section 11), acceptance establishes:

1. complete required primary-source coverage;
2. actual independent analytical participation;
3. source-grounded specialist contributions;
4. independent critical examination of material claims;
5. reconciliation of significant disagreements;
6. preservation of useful evidence and counterexamples;
7. consistent cumulative state, checkpoints and claim histories;
8. accurate source, authority and exposure boundaries.

Only the principal is required to inspect the whole unit; each other participant's source inspection is proportional to its assigned responsibility. Publication follows the existing procedures. A multi-agent review receipt is evidence of process, not proof of literary correctness, and neither it nor a passing validator substitutes for semantic acceptance.

#### 4.1.7 Unavailable capability and exceptions

A nominal multi-agent workflow is not acceptable where the runtime provides no genuine independent execution contexts. Without native subagent support, separately initialized analytical sessions qualify when their separation, source access, assignments and handoffs are verifiable. If no adequate independent route exists:

- do not fabricate participation or mark unreviewed analysis as satisfying this section;
- preserve valid completed work, and leave the unit's acceptance and high-water advance pending as a required-capability stop (continuation Section 9);
- record the capability blocker where the project's current state is read; and
- seek any justified deviation by requesting owner direction ([routing](../AGENT_ROUTING.md) Section 12). An owner authorization names its exact scope, including whether acceptance and high-water advance may proceed, and is recorded with the blocker. A reading accepted under such an authorization is recorded as a deviation, never as satisfying this section.

Do not relax the requirement silently to achieve throughput. This section authorizes no new paid service, API expenditure, account or external transmission of source material.

#### 4.1.8 Applicability and historical preservation

This section applies prospectively from its integration on `main` to newly initiated projects; to every future substantive source reading in an existing project, including later units and source-unit extensions of an ongoing run, even when the project's architecture predates it; to newly authorized rereads and major reanalysis generations; and to substantive source-reading stages of multi-medium and game projects. A unit whose reading was already under way at that point may close under its earlier arrangement if its transaction record says so.

It requires no retrospective change to completed analyses, frozen readings, historical checkpoints or published monographs. Do not reopen a completed reading to add participation records, and never add fictional agent provenance. Existing work may receive targeted independent reanalysis under separate authorization, and no corpus-wide sweep is required. An established project records its configuration through a targeted architecture or entrypoint amendment no later than the transaction of its next source reading, not a restructuring; an already OPEN sequential lock is unaffected. A bootstrap-only project records it before its first reading.

#### 4.1.9 Character evidence

The [self-contained character monograph standard](MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md#self-contained-character-monograph-standard) remains binding and separate. Specialist and review work deliberately retains the evidence future monographs need: ordinary-life characterization, distinctive personal preferences, speech and linguistic behavior, cognition and decision-making, longitudinal development, and counterexamples and limits. The reviewer checks for meaningful evidence lost between specialist observations, cumulative infrastructure and the reading's integrated character account. Multi-agent process compliance is neither monograph completeness nor validated reconstruction capability.

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

The [medium and inspection-lane routing policy](MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md) names the inspection lanes these capabilities enable (`TEXT`, `STILL_IMAGE`, `BUNDLE_MEDIATED`, `CONTINUOUS_AV`) and the claims each lane may assert. A verified `continuous_av_inspection` capability should also record the effective visual sampling rate when it is known, because a model that hears audio continuously may still sample video sparsely.

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

Use the simplest adequate arrangement. For a substantive source reading, adequacy includes the independent analytical participation of Section 4.1, which a local-only or cloud-only arrangement can provide through multiple independent agents or sessions; hybrid or parallel execution is not required to meet it. Prefer local-only when source access dominates, the artifact is bounded, or transfer overhead exceeds the expected benefit. Prefer cloud-only when all required evidence and capabilities are available and the authorized publication route can be completed separately or is not in scope. Use hybrid parallel work when independence or throughput has a defined value and integration capacity exists.

Where anchoring is a concern, an AV reviewer can record bounded observations before reading the prior interpretation, then compare them. This is an optional evaluation design, not a requirement to duplicate all analysis. The [audiovisual reconciliation protocol](MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md) applies this design to the bundle-mediated to continuous-AV relay.

No environment preference may waive evidence requirements, silently alter the source boundary, or create unapproved API spend. Insufficient capability should produce bounded progress and an explicit unresolved requirement, not a false completion claim.

## 12. Maintenance and evaluation

Keep durable topology semantics here; keep volatile model/billing facts in the reasoning policy's dated snapshot and runtime observations in the stage record. Evaluate the arrangement by accepted analytical quality, missing-evidence rate, transfer defects, retrieval failures, integration/rework effort, and actual resource use.

For multi-agent source readings (Section 4.1), track in the existing stage or transaction record, where actual runtime observations exist: material specialist findings adopted, omissions recovered, incorrect claims detected or corrected, source and locator errors, information-boundary violations, evidence lost in handoff, analytical depth preserved in downstream synthesis, and resource and integration cost. Distinguish demonstrated improvements from hypotheses about why they occurred. Do not claim an advantage of multi-agent over single-agent work without an adequately controlled comparison ([reasoning policy](MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md) Section 17). The Shiboyugi V01–V10 Japanese source run, integrated through PR #597 with its checkpoints under `series/shiboyugi/checkpoints/`, is an implementation precedent whose checkpoints record specialist corrections, an independently frozen prospective account and adversarial review; it is not proof that delegation improves every analytical task.

Changes to source fidelity, stage ownership, or promotion responsibility require explicit review. A product-name change alone does not require restructuring mature series. No new automation, validator, or public workflow is established by this prose policy. Section 4.1 deliberately adds no machine check: a role field or agent count cannot show that participation was genuine or independent, so that remains a semantic-acceptance judgment.

## Reference

- [O5] OpenAI Help Center, *File Uploads FAQ*, checked 2026-09-13: `https://help.openai.com/en/articles/8555545-file-uploads-faq`

## Changelog

### v1.2 - 2026-11-15 - Multi-agent source reading

Adds Section 4.1 as the canonical home of a binding, model-agnostic requirement: every newly undertaken substantive sequential source reading uses an accountable principal, genuinely independent source-aware specialist contribution and independent critical review, with a proportional reduced configuration for unusually bounded units that never waives independence. Defines genuine independence, preserves prospective and exposure boundaries, keeps contributions durable in existing checkpoint, claim-revision and handoff homes without per-agent files, states acceptance criteria and capability-blocker behavior with deviations only by owner direction, applies prospectively without retrofitting completed or frozen work or affecting an OPEN lock, and keeps the character monograph standard separate. Sections 4, 11 and 12 now recognize independent participation in the simplest adequate arrangement and in topology evaluation. No validator, CI workflow, paid service or source transmission is added.

### v1.1 - 2026-10-24 - Inspection lanes

Links capability verification to the inspection lanes of the medium and inspection-lane routing policy, asks verified continuous-AV capability to record its effective visual sampling rate, and points the anchoring-aware AV review design to the audiovisual reconciliation protocol.

### v1.0 - 2026-09-13 - Proposed initial policy

Defines stage-level environment allocation, verified capability profiles, cloud/local complementarity, single-owner integration, and evidence/working/analytical plane separation. The owner's long-series workflow is implemented in the companion protocol rather than treated as a universal ranking of environments.
