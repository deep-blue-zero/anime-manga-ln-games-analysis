---
title: "Cosmic Princess Kaguya! — film analytical method"
series: cosmic-princess-kaguya
artifact_id: CPK_ANALYTICAL_METHOD
artifact_type: analytical_method
generation: CPK-G1
version: "1.0"
status: canonical
authority_scope: "Project-local film reading method, AV companion and lane permissions; INITIAL procedure only"
source_boundary: "Intended Japanese feature F01; no narrative source admitted or inspected"
canonical_home: series/cosmic-princess-kaguya/CPK_ANALYTICAL_METHOD.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: DEEP_SYNTHESIS
---

# Film analytical method

## 1. Governing family and source boundary

This method pairs with [the synthesis architecture](CPK_SYNTHESIS_ARCHITECTURE.md). Its dramatic/linguistic contract, continuous-AV companion (§§3–6), and [reconciliation profile](CPK_RECONCILIATION_PROFILE.md) form one method family. It adapts the [generic anime method](../../governance/analytical-methods/GENERIC_ANIME_EPISODE_ANALYTICAL_METHOD.md) and [generic continuous-AV method](../../governance/analytical-methods/GENERIC_CONTINUOUS_AUDIOVISUAL_ANALYTICAL_METHOD.md); neither reference alone opens this project's gate.

The source unit is **one complete feature, F01**, including its authorized titles and credits. Movements, sequences, scenes, shots and musical passages are internal navigation/evidence units, not invented episodes. Discover their boundaries from the source. Mechanical scene/shot segmentation is navigation until inspected. Do not preassign act counts, song counts, themes, character arcs, identities or narrative outcomes.

The finished film is primary narrative authority. Japanese speech, verified subtitles/transcripts and onscreen text support linguistic claims under their stated provenance. Official English subtitles are secondary translation evidence. Frames, audio, transcripts and a film bundle inherit the exact source witness's scope; they are synchronized derivatives, never independent canon. Official credits, interviews, promotional statements and soundtrack releases are separately admitted paratext. *Taketori Monogatari*, other adaptations, reviews, fandom and model descriptions cannot establish events or themes here. Metadata reconnaissance licenses method design only.

## 2. Knowledge and evidence discipline

Keep presentation order, inferred story time, character knowledge, audience disclosure and analyst inference distinct. Self-report and a character's confident assertion do not automatically establish motive or world fact. Use source-established names when available; preserve meaningful anonymity, aliases and concealment at their disclosure boundary. Attribute action, speech, belief, inference and recipient explicitly under [handoff §15](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md#15-named-subjects-and-referential-clarity-in-analytical-prose).

The ordinary full-film pass permits retrospective interpretation **within the admitted film**. After whole-film exposure, reconstructed earlier audience knowledge is not a prospectively frozen prediction. If a later authorized experiment needs genuine first-encounter forecasts, arrange incremental source exposure and freeze each forecast before later intervals become accessible. A whole uploaded video or remembered ending can defeat that condition. Disclose recognition and prior exposure; never manufacture blindness by relabeling a reread.

Use inherited evidence classes, not a competing taxonomy:

| Class | What it can support |
|---|---|
| `CAV` | Perceived synchronized motion, order, editing and temporal form at verified effective resolution |
| `AO` | Auditory observations of delivery, music and sound, with confidence |
| `FRM` | Static clean-frame evidence at its own timestamp |
| `TXT` | Verified primary-language subtitle/transcript or onscreen wording, with witness/confidence |
| `AM` | Deterministic measurement, with tool/parameters and source identity |
| `HL` | Attributed human listening/viewing observations |
| `INF` | Source-supported inference linked to observations and alternatives |
| `INT` | Interpretation argued from evidence and counterevidence |

Direct observation/textual fact, inference, interpretation and speculation must remain distinguishable in prose and claim records. Mark a speculative hypothesis as such, not as an additional evidence class. Bibliographic and external contextual statements carry their source category and no narrative evidentiary weight. Do not treat confidence as an evidence class or a claim transition as artifact authority.

## 3. Source binding, clocks and actual capabilities

Before execution, populate [the source inventory](CPK_SOURCE_INVENTORY.md) from the supplied witness: edition/distribution, external stable source ID, hashes/bytes, duration, video and Japanese audio streams, resolution/frame rate, text tracks, derivative lineage and transformations. Keep media and raw extraction outside Git. Public records contain sanitized provenance, never local paths or signed credentials.

Use a single film citation clock tied to the retained source's presentation timeline and program-start definition. The bundle must preserve or explicitly map to it. Source pre-roll, credits, trims, dropped frames, variable frame rates, subtitle shifts and segmented uploads require documented offsets and drift checks. A chunk's local time is never a film timestamp without mapping.

Calibrate native AV and derivatives using at least beginning, middle and end anchors for the full film; add anchors around discontinuities and rapid events. Prefer verified dialogue cues, then distinctive shared audiovisual events, verified audio features, shot/presentation-time metadata, and other documented independent anchors. Log paired times, mapping, drift, residual uncertainty and the actual anchor identity. A single global offset is insufficient if drift/nonlinear edits occur. Ordinary navigation uses the inherited ±0.5 s baseline; exact order/synchronization requires precision finer than the effect asserted. Failed mapping blocks cross-object temporal claims; it does not permit invented timestamps.

For each run distinguish transport, decode, model inspection, interpretation and persistence. Record observed provider/model/surface/effort or UNKNOWN, runtime, source route, Japanese text/image/audio access, `continuous_av_inspection` and the probe result. A practical synchronized picture/sound probe on the authorized object is required before assigning `CONTINUOUS_AV`. ffmpeg, ASR, accepted file extensions and generated frame sequences alone do not verify it.

Record effective visual sampling rate/resolution, requested versus effective settings, continuous audio behavior, context/truncation and segment limits, and any opaque defaults. UNKNOWN sampling leaves fine temporal visual claims unresolved until checked. Native video is not frame-complete inspection. Events shorter than the sampling interval require a higher-resolution targeted inspection or measurement; sound cannot fill an unseen visual event.

The default primary-AV evidence need is `VIDEO_FULL_EPISODE_ESCALATION`, retaining the corpus token for a **full film**, because whole-film editing, performance and musical development are the authorized future object. This is a project-specific refinement under bundle specification §8.9 and the reconciliation mirror route, not a new corpus default. Later disputes normally use `VIDEO_TARGETED_ESCALATION`; `VIDEO_NOT_REQUIRED` is appropriate where accessible bundle evidence suffices. These are needs, not claims of inspection success. Recheck current transport guidance before a film-scale transfer; do not turn a dated size snapshot into a current platform guarantee.

## 4. Primary continuous-AV procedure

1. Verify owner scope, source binding, initiation/continuation state and capabilities. Define full-film coverage including any unavailable credits, songs or intervals; do not silently drop them for upload limits.
2. Conduct structural viewing to identify movements and possible scene/music boundaries. Log exposure, interruptions and inspected ranges. This pass supplies navigation, not untested load-bearing conclusions.
3. Before interpretive synthesis, write descriptive observations in the observation ledger with calibrated intervals, cue/frame/content anchors, evidence class, channel, confidence, effective resolution and reinspection status. Separate what is visible/audible from the meaning proposed.
4. Reinspect each load-bearing temporal observation in a separate focused pass. Record disagreement between passes. Corroborate exact duration/synchronization, unmarked voice attribution and claimed departures from production convention with a second independent channel or measurement.
5. Build causal, character, relationship, language and formal arguments from those observations. Test alternatives and preserve counterevidence. Update cumulative state and claims with explicit dependencies.
6. Close coverage by actual interval **and modality**, not by upload success or synopsis length. Freeze the original candidate, associated evidence state and technical record before sending the withheld interpretations to the verifier. The reconciliation profile governs the independent audit.

## 5. Dramatic, visual and linguistic passes

Explain scene-to-scene causality: conditions, information, choices, available alternatives, actions/non-actions and consequences. Track chronology, framing, disclosure, setup/payoff and retrospective recontextualization without granting characters later audience knowledge. Distinguish actual development from newly disclosed prior state. Establish institutions/world rules through demonstrated operations and qualified reports if the film earns that module.

For each materially developed character, connect stated desire, behavior, competing obligations, contradiction, agency and context. Preserve ordinary or low-stakes behavior alongside crises and performances. Model each relationship direction separately: A's attention, trust, expectation or obligation toward B may differ from B's toward A. Reciprocity requires evidence on both sides. Avoid reducing either person to a plot role or diagnostic label.

Inspect framing, composition, camera relation/movement, shot relationships, editing, blocking, gesture/gaze/facial development, animation timing, lighting/color, compositing and spatial continuity. Link a formal observation to a proposed effect and test ordinary staging, lighting, genre/animation convention, reuse or limited-animation explanations. A held image does not alone demonstrate hesitation. Motifs need linked instances, constants, changed context and a reason the recurrence matters; a conspicuous object is not automatically symbolic.

Japanese analysis records exact bounded wording, cue/onscreen witness, speaker, recipient, register/address, grammar and a translation-sensitive explanation. Distinguish speech, thought, lyrics, signs and subtitle accessibility annotations. Preserve original and corrected derivatives separately. English localization can aid navigation and comparison but cannot replace Japanese evidence. ASR, OCR and listening transcription remain uncertain derivatives until verified; record corrections, not silent normalization. If no adequate Japanese witness exists, leave exact-wording/register/lyric-dependent claims pending. Apparent subtitle/audio divergence routes to text verification.

Major interpretations require a strong rival and disconfirmation condition; the governing thesis must consider at least two plausible alternatives. Distinguish a factual inconsistency from a defensible interpretive disagreement. Do not import a promotional thematic phrase as a conclusion.

## 6. Music, voice and sound companion

Screen musical passages using the inherited `M0` incidental, `M1` supportive, `M2` diagnostic and `M3` state-changing significance scale. M2/M3 require a full linked musical-event record and reinspection; M3 also updates affected character/relationship/claim state. The scale describes analytical consequence, not aesthetic quality.

For diagnostic passages, capture audible/visible internal transitions, cue entrances/exits, development of texture/density/dynamics, witness/audience configuration, diegetic/nondiegetic/ambiguous status and shifts, and synchronization with cuts, words or action. Ask what the musical event accomplishes that ordinary dialogue cannot. "No material additional function established" is a valid result.

Keep lyric, melodic, thematic, arrangement, composition and recording recurrence distinct. Heard similarity cannot prove the same recording; an album version cannot establish film timing/mix. Song lyrics become textual evidence only through an adequate Japanese witness matched to the film. Singer/voice-actor recognition is not attribution evidence. Use explicit track/credit/speaker and visible-performance evidence, retaining ambiguity in ensembles.

For voice, describe contour, rate, intensity, breath, voice quality, laughter, overlap and approximate latency against within-character/interlocutor baselines. Exact timing is `AM`. Delivery is not an inner state: emotional/motivational conclusions are `INF`/`INT` with alternatives. Track silence, ambience, effects, offscreen sound, mix prominence, sound bridges and audiovisual counterpoint. Silence alone cannot establish fear, reluctance or sadness.

## 7. Bundle-lane companion and escalation

The later auditor checks the supplied **single-film bundle** against all nine semantic responsibilities of [the corpus bundle specification](../../governance/source-policies/MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md#5-minimum-semantic-contract-for-calling-an-object-an-episode-bundle). Internally segmented delivery still represents F01; chunk manifests must cover the film without hidden gaps/overlap or clock changes. Missing layers remain disclosed. A screenshot/audio/subtitle-only object remains a partial derivative even if sufficient for a bounded question.

Survey contact sheets for navigation, open clean full-resolution frames for static evidence, use frame/shot manifests for sampling and deduplication provenance, and inspect Japanese dialogue/temporal crosswalks and complete analysis audio through verified capabilities. Check source encode, extraction/QA, shared replacements and frame/audio/text offsets. Official English tracks are a secondary aid, not proof of paired Japanese completeness.

Static frames support endpoints, not trajectories. An audio-accessible auditor may make `AO` observations; possessing audio or measuring it does not establish listening. Exact acoustic values require `AM`; an auditor lacking audio inspection records UNAVAILABLE for auditory claims. Bundle silence between retained frames cannot refute a continuous event. Queue a neutral targeted question for material inaccessible temporal evidence, or narrow the claim; never award the auditor authority simply because it writes last.

## 8. Full-film output and closeout

The future primary deep reading must contain substantive prose for: source/inspection boundary and profile; an accurate synopsis and causal movement reconstruction; character and directed-relationship development; chronology/knowledge/revelation; Japanese-sensitive findings; cinematic form; music/voice/sound and their integration; supported thematic/motif arguments; counterevidence/rivals; unresolved questions; and the full-film exit state. It must explain how form changes interpretation, including what continuous inspection added or failed to add. Activate extra domains only when earned.

Claims link observation IDs and bounded source locators, not merely whole-film references. A completed prose draft with missing state/claim/coverage updates is incomplete. Close all three ledgers and the inventory's actual inspection boundary together. Preserve the original author's full formulations, arguments, alternatives and locators; do not substitute an abstract for the candidate during transfer.

Before acceptance, perform the bounded name/reference check on synopsis, a substantial middle causal/relationship section and exit/synthesis, extending it to each consequential dyad. Record sampled scope and material findings. Technical validation, semantic acceptance, owner authorization, branch publication and merge are separate events.

## 9. Revision and governing references

Use `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, `OPEN` through the claim ledger. Frozen candidates and blind logs are not rewritten. Later facts cannot be inserted as earlier prospective knowledge. Amend INITIAL procedure when actual source behavior requires it; preserve version history and record material backfill needs.

Live [initiation](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md), [lane routing](../../governance/source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md), [topology](../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md), [reasoning](../../governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md), [handoff](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) and [reconciliation](../../governance/source-policies/MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md) governance controls those responsibilities. No model or film has been executed under this method.
