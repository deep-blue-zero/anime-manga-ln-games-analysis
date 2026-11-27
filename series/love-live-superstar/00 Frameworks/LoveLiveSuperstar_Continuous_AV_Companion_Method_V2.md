---
title: Love Live! Superstar!! — Continuous Audiovisual Companion Method V2.4
series: LLS
artifact_id: LLS_CONTINUOUS_AV_COMPANION_METHOD_V2
artifact_type: continuous_av_companion_method
artifact_role: series_av_method
generation: V2.4
version: '2.4'
date: '2026-11-26'
status: canonical
scope: Japanese-audio television episodes S1E01-S3E12; only the authorized episode frontier may be inspected
source_boundary: Procedural method only; no new source admission or audiovisual findings
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Love Live! Superstar!! — Continuous Audiovisual Companion Method V2.4

## 1. Place in the method family

This companion implements the continuous audiovisual responsibilities of the [governing method](LoveLiveSuperstar_Analytical_Method_V2.md). The [architecture](LoveLiveSuperstar_Multi_Document_Architecture_V2.md) owns artifact responsibilities; the [reconciliation profile](LoveLiveSuperstar_AV_Reconciliation_Profile_V2.md) owns required claim classes, comparison and write-through. The [execution plan](../07%20Audits%20and%20Manifests/LLS_V2_4_AV_EXECUTION_PLAN.md) owns assignment and activation preparation. The existing [current-state entrypoint](../01%20Source%20Lock%20and%20Inventory/LLS_CURRENT_STATE_AND_CORPUS_MAP.md) remains the single project entrypoint.

The companion adapts the [generic continuous-AV method](../../../governance/analytical-methods/GENERIC_CONTINUOUS_AUDIOVISUAL_ANALYTICAL_METHOD.md) to a television musical ensemble drama. Its two uses are:

- **Bounded review or re-audit:** test audiovisual questions in already admitted episodes and supply attributable additions or claim revisions.
- **Independent AV-primary reading:** undertake an explicitly authorized chronological reading with whole-episode principal coverage, independent specialist work and critical review. The Japanese text and bundle lanes still verify wording and citation coordinates.

The candidate independent scope is all 36 television episodes. Preparing this method does not start that run, establish source access, open any lock, remove the existing continuation restriction, or certify any earlier artifact as continuously viewed. Actual activation and any material restart must satisfy the live entrypoint, initiation and continuation requirements. Historical episode readings and season freezes retain their original evidence and knowledge boundaries.

**Coordinator-only routing:** the existing governing method, architecture, corpus map, ledgers and hypotheses contain interpretations and later narrative information. For an independent first pass, the coordinator resolves those controls and sends a neutral packet containing the applicable rules from Sections 2–10 below, the exact authorized frontier, source routes and role assignment. Do not send the old readings, seven governing hypotheses, later cohort descriptions, checkpoint arguments or full corpus map as an allegedly neutral brief. Record precisely which procedural excerpts and prior-run material each participant actually received. The neutral packet preserves every applicable control; it does not waive governance because some documents also contain spoilers.

## 2. Neutral dispatch and evidence boundary

Each assignment states the episode, edition, Japanese audio/text witnesses, allowed earlier evidence, forbidden later evidence, inspection scope, named responsibility, output home and stopping boundary. Inventory access is not permission to inspect every listed episode. Earlier findings from this independent run may provide its longitudinal memory after their own acceptance; prior-run conclusions remain withheld until the declared comparison barrier.

The principal covers the complete assigned episode in source order, including current-episode OP, ED, credits, performances and quiet scenes. A future preview remains paratext under the governing method unless its interpretation is separately authorized. Do not trim a title, ending or credit sequence merely to obscure identity when its form is inside the analytical assignment. Record recognition or remembered information that could contaminate the prospective account. A model cannot promise that it has no prior knowledge; it can disclose exposure and avoid using unsupported recall as evidence.

Parallelize responsibilities inside the current episode. Do not send different seasons to different workers and later label their combined output a sealed sequential reading. Freeze the unit's prospective observations and accepted exit state before admitting the next episode. Season retrospectives use only the completed season frontier. Full-series retrospection waits for its own complete authorized frontier.

Independent source-aware specialist and critical-review contexts must be genuine. They may use the same model, but must not inherit the principal's interpretive draft. Every worker has a bounded source assignment and preserves material findings with locators. The principal is normally the sole integrator of candidate readings and run-local deltas. Keep that fresh context separate from the repository-aware setup coordinator, who may inspect the old corpus to resolve controls but sends only neutral packets and maintains current routing from receipts. Neither coordinator feedback nor a required full-file read may leak old interpretations to the independent principal before the scoped cross-run freeze. After that freeze, name one current-corpus reconciler and record any change in exposure. Coordination does not count as source inspection. Follow the standing configuration in the execution plan. Ordinary television episodes do not qualify for a reduced configuration merely to save time.

Before the observation-release barrier, shared messages contain only neutral assignments, access problems and compact completion receipts. Participants write their observations to assigned working artifacts and do not read one another's interpretations. Freeze references, timestamps, content hashes and actual message/file exposure must be recoverable. If isolation or ordering cannot be established, record `blind_order_achieved: false`; a fresh, separately bounded source-aware context must satisfy the affected independent responsibility before acceptance. Preserve useful contaminated work with its limitation.

## 3. Source lock, capability and clock

### 3.1 Verify the object and every assigned worker

Record the source episode and continuous derivative identities, byte size, SHA-256 where accessible, duration, resolution, frame rate, Japanese audio stream/track, codec and channels. Record transformations and the relationship to the locked episode bundle. A bundle containing frames and complete audio is not thereby a continuous AV object. Do not silently substitute another edit, dub, release, music video, album mix or live performance.

For each worker, verify the capabilities material to its task: transport, decoding, text/image/audio inspection, synchronized audiovisual inspection and durable output. An available path, successful `ffprobe`, shared filesystem or principal's probe does not establish another worker's perception. A short source-local probe should demonstrate that the actual worker can relate a visible event to an audible event. Keep the probe's interval, result and limitations; do not turn it into a general model benchmark.

Record observed product surface, worker/context identity, model and exposed reasoning settings, without guessing hidden settings. Record `continuous_av_inspection` and `audio_content_inspection` separately and the actual inspection route. A session using frames, ASR or acoustic measurements names that route; it must not claim `CONTINUOUS_AV`.

An independent AV-primary principal defaults to `VIDEO_FULL_EPISODE_ESCALATION`. A bounded relay normally uses `VIDEO_TARGETED_ESCALATION` with sufficient surrounding context. These states describe evidence need, not successful inspection. If full delivery requires clips, preserve order, overlaps and source-clock mappings, account for every interval, and recover the whole episode's structure. An omitted interval remains uninspected.

### 3.2 Calibrate time and temporal resolution

Use the locked episode bundle's declared clock as the citation coordinate system. Record both audio and frame offsets if they differ, plus each clip's source offset. Normally establish at least three independent anchors across a full episode's beginning, middle and end. Prefer verified Japanese cues, then distinctive AV events, verified audio events or measurements, frame/shot-index metadata, and other documented references. A short or sparse clip needs enough independent anchors for its actual claims rather than a mechanically imposed count.

Record the anchors, offsets, drift and achieved precision. The default navigation tolerance is **±0.5 seconds**. This is not permission to claim a cut landed exactly on a beat, a gaze preceded a syllable by a few frames, or two voices entered simultaneously. Such claims need adequate temporal resolution and independent corroboration or measurement. Exact durations belong to `AM`.

Record the effective visual sampling rate or `UNKNOWN`. Native synchronized AV is not necessarily frame-complete. If the rate is unknown or inadequate, a load-bearing rapid gesture, edit or synchronization remains unresolved until higher-rate inspection, frame-level verification or measurement resolves it. Continuous audio cannot establish an unseen intervening movement. If clocks cannot be mapped reliably, block cross-object timing claims and continue only with observations whose accuracy does not depend on that mapping; never publish uncalibrated model timestamps as exact locators.

## 4. Observe first; make the episode intelligible

The first pass follows the complete assigned scope without trying to confirm a thesis. Record dramatic movements, the problem each scene poses, actions and decisions, changes of situation, performance placement and unresolved residue. Later focused passes revisit consequential intervals. Specialists may inspect proportional diagnostic scopes, but their receipt must identify those scopes rather than imply whole-episode coverage.

Keep observations distinct from interpretation. Use the existing labels `AF`, `JT`, `PF`, `MF`, `AM`, `FR`, `SI`, `IT` and `SP`, with an explicit inspection route (`CONTINUOUS_AV`, auditory observation, primary-language text, retained frame, measurement, or identified human observation). The same fact label cannot conceal a different evidence channel. Delivery is observed; motive and inner state are inferred. Recurrence requires identified earlier evidence inside the frontier.

Each observation carries:

| Field | Required content |
|---|---|
| Identity | Stable observation ID, episode and contributor |
| Location | Calibrated interval, citation clock and nearest verified cue/frame/shot anchor |
| Evidence | Descriptive observation, evidence label, actual channel and inspection route |
| Resolution | Sampling/precision limitation relevant to the claim |
| Reliability | Confidence with reason; focused re-view result; corroboration when required |
| Knowledge | Permitted frontier, actual exposure and whether recorded before or after claims were released |

Every load-bearing observation must survive a second focused inspection. Retain discrepancies between passes. Freeze each required independent log before sharing candidate interpretations or opening a withheld adjudication packet. Later additions are valid when clearly marked as post-exposure, not backdated into the frozen log.

The final reading begins with a human-facing, current-episode story synopsis: what happened, to whom, in what causal order and with what outcome. Write or finalize it after prospective observations are frozen. It is bounded to the episode and current disclosure horizon, distinguishes recounted past events from present action, and does not replace close reading. Use known character names and unambiguous speaker/recipient references, preserving source-required concealment.

## 5. Voice, bodily acting and characterization

Read vocal and animated performance together with the Japanese words, interlocutor, task and physical setting. Capture ordinary conversation, humor, habits, tastes, work, reassurance, avoidance and small disagreements as well as climactic declarations. An analysis of how someone behaves between crises is necessary evidence for a person-level portrait.

Distinguish three responsibilities:

1. **Japanese linguistic form:** wording, address, self-reference, sentence endings, register, ellipsis and code-switching, verified from the text witness.
2. **Performed presentation:** audible prosody, pacing, intensity, breath, laughter, overlap, voice quality and sung delivery; visible gaze, posture, movement, facial change and reaction timing, bounded by actual resolution.
3. **Character action and interpretation:** what the character is doing in the interaction, what she appears to want or avoid, and how the delivery/body supports, complicates or contradicts the words. These remain inferential claims with alternatives.

Build within-character baselines before treating a departure as meaningful. Compare private/public speech, familiar/unfamiliar listeners, peer/family/authority relations where actually present, rehearsal/stage behavior and similar earlier situations. A generic equation such as high pitch = excitement is insufficient. Distinguish a character deliberately performing confidence, politeness or deception inside the story from the audiovisual performance that presents her to the viewer.

Track interaction, not just isolated voices: who initiates, interrupts, waits, withdraws, mirrors, reassures, changes register or gets the reaction shot; whether verbal and bodily responses coincide; whether a listener's action changes the speaker's next move. Separate measured pause or latency from perceived rhythm. Silence or a held image does not automatically establish hesitation or repression.

Do not infer an actor's intentions, biography or production direction from the finished performance. Do not identify speakers or singers by recognizing a real voice actor. An unmarked attribution needs corroboration such as verified allocation, visible lip movement and source-grounded contrast with the character's established voice. Leave uncertain ensemble or offscreen lines unattributed. Merely naming a performer adds no explanatory force to a characterization claim.

Route accepted contextual delivery and speech findings to the existing voice ledger; behavioral conditions and counterexamples to the behavior/decision ledger; developmental consequences to the state ledger; directional interpersonal changes to the relationship matrix. Retain the connection among words, performed action and dramatic context, not a list of adjectives describing voices.

## 6. Musical events, diegesis and dramaturgy

### 6.1 Screen the whole musical field

Inventory songs and fragments, composition and lyric-writing, demonstrations, auditions, failed attempts, rehearsals, recordings and playback, public performances, subjective or presentational sequences, instrumental score, ambience and meaningful dropouts. Use the governing M0–M3 screen: incidental, supportive, diagnostic and state-changing. M2/M3 events require full entries and reconciliation; M1 needs compact notation where it contributes to a pattern; M0 does not need an essay. Absence of a full song does not mean absence of musical action.

For each substantial event identify the immediate unresolved dramatic question; creative labor and choice; performer and listener configuration; available alternatives; what changes during the event; what the following scene establishes; and any residue the performance leaves unresolved. Separate competitive result from artistic experience, interpersonal change and institutional consequence. Praise, spectacle or a victory does not itself establish ethical endorsement.

### 6.2 Treat diegesis as a changing relation

Assign status to the **segment**, with evidence, instead of giving an entire song one unquestioned label. Record:

- what produces the sound inside the represented scene, if a source is established;
- who can apparently hear it, who demonstrably reacts, and what remains unknown;
- whether it is performed live, rehearsed, recorded or played back within the story;
- whether picture presents a literal shared place, a memory, subjective imagery, montage or a stylized performance space;
- the transition between those states and whether the same sound bridges them;
- what narrative perspective the sequence makes available to the viewer beyond any character's knowledge.

Use diegetic, nondiegetic, quasi-diegetic/presentation-space or ambiguous as justified descriptions. Musical polish alone does not establish nondiegesis; imagined staging does not make all audio nonliteral. A song can continue while the image changes its narrative level. Do not treat a tableau as proof that every pictured person is physically performing together or shares the focal character's knowledge.

Keep **in-story performer**, **recording/credit attribution**, **audible vocal allocation**, **on-screen focal character**, **lyric voice** and **listener** distinct. A credit can identify the track without identifying every line's singer. Camera emphasis is not vocal attribution. Lyrics may express an aspiration, collective position, contradiction or stylized address; they are not automatically a literal confession by each singer.

### 6.3 Read internal construction

Segment at materially audible or visible changes: vocal handoff, solo/ensemble relation, lyric perspective, tempo or density where supported, cue entrance/dropout, formation, space, editing pattern, listener position or dramatic function. A locator segment is not automatically a verse, bridge or other formal musical section. Identify musicological form only when evidence supports that identification.

For each load-bearing segment connect the musical/visual construction to the dramatic question. Inspect vocal texture, phrasing, register, rhythm, arrangement and dynamics at the level the mixed soundtrack supports. If instrumentation, harmony, voice separation or a reprise cannot be resolved reliably, state the narrower observation and keep identification open. Acoustic estimates do not by themselves establish timbre, affect, singer identity or exact instrumental source.

Track choreography and blocking as relations among bodies: approach and distance, orientation, handoff, formation, exclusion, symmetry, center and periphery, and what changes over the sequence. Relate them to editing and vocal/lyric distribution without assuming that every camera focus marks hierarchy or that equal screen time means equal agency. Quantitative counts require a stated method and denominator; their interpretation remains argued.

Ask whether the performance **accompanies, represents, demonstrates, legitimizes or enacts** a change. Explain what happens through musical or performed form that dialogue alone would not establish. A null result is valid: do not upgrade every polished sequence to state-changing music. Preserve cases where the audiovisual form pressures the spoken resolution or where a performance proposes a unity the surrounding action has not earned.

## 7. Score, ambience, editing and spatial form

Treat underscore, effects, acoustic space, crowd sound, near-silence and sound bridges as their own field. Locate entries and exits relative to speech, gesture and cuts; distinguish measured energy reduction from perceived silence; consider offscreen sources and differences between a character's auditory experience and the viewer's soundtrack. Do not identify an unnamed score cue by remembered album information.

For recurrence, document at least two source-grounded occurrences within the authorized frontier and the basis for saying they match or transform one another. Similar mood is not proof of the same musical material. Record changed context, mix, function and counterexamples. A score cue may support, withhold, destabilize or simply accompany a scene; absence of sentimental music is not automatically irony.

Read camera movement, shot duration, transitions, montage and reaction placement in relation to narrative information and character action. Distinguish static composition, endpoints, observed paths and measured timing. Examine school, home, practice, street, transit, backstage and stage spaces when the episode actually supplies them; do not impose a fixed symbolism on repeated stairs, rooftops or thresholds.

Consider production conventions before psychological explanation: held cels, limited animation, reused cuts, banked performance material and recurring OP/ED sequences can create apparent pauses or repeated gestures. Claims that a particular choice departs from convention need source comparison or corroboration. Production economy and dramatic effect may coexist; neither is an automatic explanation of the other.

## 8. Integrate dramatic, character and thematic findings

The reading must explain how audiovisual form bears on story, characters, relationships and themes. For each major interpretation, name the observed mechanism and the inference it supports. Compare what is said, what is done, how it is performed, who sees/hears it and what follows. Preserve mismatches rather than resolving them by default into a single authorial message.

Track aspiration and fear, choice and perceived stakes, care and rivalry, creative ownership, institutional rules and informal exceptions, public recognition and private consequence. Attend to changing group composition and transmission of skills only as they emerge inside the current frontier. Avoid treating a character merely as a thematic function or assuming that the ensemble's development is uniform.

Each episode includes a meaningful competing account, contrary scene or narrower explanation. The critic tests mistaken attribution, omitted ordinary-life evidence, lyric-as-biography shortcuts, unsupported inner states, performance/plot causality, conventional staging, numerical overreach and future-knowledge leakage. Integrate material specialist corrections and preserve rejected alternatives with reasons; a consensus statement is not a substitute for this work.

## 9. Reading and contribution contract

An independent AV reading preserves these responsibilities in a coherent document rather than mechanically producing one section per agent:

1. Current-episode narrative synopsis and disclosed source frontier.
2. Dramatic movements, character actions and the episode's developing argument.
3. Voice, bodily acting, interaction and ordinary-life characterization.
4. Musical events and internal segments, diegesis, creative agency, lyric/performance relation and consequences.
5. Score, ambience, sound–image relations, camera, editing and spatial organization.
6. Character, relationship, institutional and thematic synthesis, with counterevidence and unresolved questions.
7. Actual execution/coverage record, source/clock/sampling facts, frozen observation references, significant specialist contributions and critical adjudication.
8. Proposed longitudinal deltas, claim-level evidence obligations and what continuous inspection materially added, changed or left intact.

Observation and claim tables may be appendices or linked contribution artifacts. Keep substantive contributions recoverable after working caches disappear. A short final essay cannot replace the evidence or detailed reasoning supplied by the workers. Do not create permanent competing character ledgers for each specialist.

Use stable IDs compatible with existing identifiers. New AV IDs may take the forms `LLS-AV-<run>-<episode>-O###` for observations and `LLS-AV-<run>-<episode>-Q###` for queue items. Preserve existing musical event and claim IDs when mapping new observations to them; a new run namespace never renames historical evidence.

Before completion, record every required channel as `COMPLETE_FOR_DECLARED_SCOPE`, `PARTIAL`, `PENDING`, `UNAVAILABLE` or `NOT_APPLICABLE`, with its actual boundary. Required gaps block the corresponding completion claim. Never convert a required review into optional enrichment to advance. Distinguish observation freeze, accepted reading, independent-run completion, cross-run reconciliation and current-authority promotion.

## 10. Handoff, preservation and implementation references

The [AV evidence and reconciliation index](../06%20Evidence%20and%20Indexes/LLS_AV_EVIDENCE_AND_RECONCILIATION_INDEX.md) supplies the common retrieval route for coverage, observations, queues, dispositions and unresolved obligations. The reconciliation profile routes accepted findings to the five established ledgers and other architecture-owned homes. Only the designated integrator writes shared cumulative state.

Keep raw media, full transcripts, source bundles, access tokens and private acquisition details outside public Git. Public records must retain enough sanitized analytical substance and locators to audit material claims. Preserve complete working analysis until acceptance and durable readback establish that no non-identical contribution would be lost. Follow the repository's Git-primary publication workflow; a source retained on Drive does not make Drive the analytical write authority.

The governing corpus controls are the [inspection-lane policy](../../../governance/source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md), [AV reconciliation protocol](../../../governance/source-policies/MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md), [execution topology](../../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md), [handoff contract](../../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md), and [initiation policy](../../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md). Runtime product/model claims belong in observed execution records under the reasoning policy, not this durable method.

## Revision history

### V2.4 — 2026-11-26

Adopts a series-specific continuous-AV companion while preserving the governing V2 method, historical readings and source boundaries. Defines neutral independent dispatch; per-worker capability and clock evidence; performed voice and bodily interaction; segment-level musical diegesis and dramaturgy; soundtrack and visual form; durable contributions and evidence-bounded acceptance. No source episode was inspected and no run was started by this methodological amendment.
