---
title: Manga / Anime Medium and Inspection-Lane Routing Policy
artifact_id: MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY
artifact_type: medium_inspection_lane_routing_policy
version: "1.0"
status: canonical
scope: corpus-wide routing of source media to reference methods, inspection lanes, lane claim permissions, and series adoption of continuous audiovisual analysis
created: 2026-10-24
maintainer: Claude + user
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md
drafted_against_commit: 6a3afaaf1bb61e0993db379ab4074c46e9ea98dd
supersedes: null
superseded_by: null
---

# Manga / Anime Medium and Inspection-Lane Routing Policy

> **Route each analytical stage by the source medium, the evidence channels its claims depend on, and the inspection capability actually verified in the session. A model name, product, or subscription selects nothing by itself.**

The corpus now uses analysts whose perception differs in kind, not only in quality. Some sessions read text and inspect still images, including the sampled frames of an episode bundle. Others can inspect synchronized video and audio natively. This policy states which reference method and evidence object each medium starts from, what each inspection lane may claim, and how a series adopts continuous audiovisual work without discarding its existing method.

## 1. Responsibility boundary

This policy owns:

- the routing from source medium to corpus-level reference method and default inspection lane;
- the definition of inspection lanes and the claims each lane may assert;
- the owner's current lane assignment, recorded as a dated operational fact;
- how a series declares a lane split for its method.

It does not replace:

| Responsibility | Governing document |
|---|---|
| Episode-bundle semantics and continuous-video escalation states | [Episode bundle specification](MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md) |
| Capability verification, environments, and stage ownership | [Execution topology policy](MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md) |
| Reasoning class and model/effort resolution | [Reasoning and model-routing policy](MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md) |
| Transfer, receipt, and acceptance between sessions | [Analytical handoff contract](MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) |
| The bundle-lane to continuous-AV relay procedure | [Audiovisual reconciliation protocol](MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md) |
| Method and architecture required before sequential analysis | [Project initiation policy](MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md) |

Repository roles in `AGENTS.md`, live authority records, and the [pre-commit checklist](../policies/CHANGE_INTEGRATION_CHECKLIST.md) continue to control who writes what and how changes reach `main`. This policy grants no source admission, write, or publication authority.

## 2. Inspection lanes

An **inspection lane** names the route by which a session actually examines evidence. Lanes are capability descriptors, not quality tiers or authority states.

| Lane | Inspection route | Typical evidence object | Capability that must be `VERIFIED` (topology Section 5) |
|---|---|---|---|
| `TEXT` | Reading text | Novel and light-novel text, scripts, transcripts, subtitle files | `filesystem_read` or an equivalent verified text route |
| `STILL_IMAGE` | Inspecting still images | Manga pages, illustrations, CGs, extracted frames | `image_inspection` |
| `BUNDLE_MEDIATED` | Sampled frames, contact sheets, and indexes, aligned to primary-language subtitles and analysis audio | An episode bundle under the bundle specification | `image_inspection`; `audio_content_inspection` only for auditory-observation claims |
| `CONTINUOUS_AV` | Native inspection of synchronized video and audio | A source episode or a continuous AV derivative, with the episode bundle as the citation coordinate system | `continuous_av_inspection` |

A session may work in more than one lane when each capability is verified. Record the lane per stage in the existing execution profile:

```yaml
execution_profile:
  inspection_lanes: [BUNDLE_MEDIATED]
  continuous_av_inspection: "UNAVAILABLE"
  audio_content_inspection: "UNVERIFIED"
```

**Reconciled** analysis is a staged route, not a fifth lane: a `BUNDLE_MEDIATED` reading is tested by a `CONTINUOUS_AV` review and integrated by its author under the [reconciliation protocol](MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md).

### 2.1 What "continuous" means here

`CONTINUOUS_AV` means the model perceives video and audio together on one timeline. It does not guarantee frame-complete vision. Some AV-capable models ingest video at a reduced sampling rate (on some surfaces, around one frame per second by default) while hearing the audio continuously. Record the effective visual sampling rate when it is known, or `UNKNOWN`, and bound motion, editing, and timing claims by it. A claim about an event shorter than the sampling interval needs a measurement, a higher-rate inspection, or a targeted clip. Holding `CONTINUOUS_AV` capability is therefore necessary but not sufficient for a fine-grained visual or synchronization claim (generic continuous-AV method, Sections 5–6).

Opening a video with ffmpeg, extracting frames, or running an ASR model is not `CONTINUOUS_AV` (topology Section 6).

## 3. Medium routing

| Source medium | Usual sequential unit | Default lane | Corpus reference method | When continuous AV is added |
|---|---|---|---|---|
| Light novel, novel, web novel | Volume, chapter | `TEXT`, plus `STILL_IMAGE` for illustrations | [Generic novel method](../analytical-methods/GENERIC_NOVEL_ANALYTICAL_METHOD.md) | Not for prose. Only when an adaptation is inside the declared source boundary |
| Manga, manhwa, manhua | Chapter, volume | `STILL_IMAGE`, plus `TEXT` for lettering transcripts and translations | [Generic manga method](../analytical-methods/GENERIC_MANGA_ANALYTICAL_METHOD.md) | Not applicable to the page. Motion comics and adaptations follow the anime row |
| Anime, donghua, film, OVA, ONA | Episode, film movement | `BUNDLE_MEDIATED` | [Generic anime episode method](../analytical-methods/GENERIC_ANIME_EPISODE_ANALYTICAL_METHOD.md) | When the series declares AV-load-bearing channels (Section 6), or a claim reaches a video-escalation state other than `VIDEO_NOT_REQUIRED` |
| Game, live-service game, visual novel: scripts, commus, events, extracted data | Causal block, event, route | `TEXT`, plus `STILL_IMAGE` for cards, CGs, and sprites | [Generic game method](../analytical-methods/GENERIC_GAME_ANALYTICAL_METHOD.md) | For voiced scenes, cutscenes, and live performances inside the boundary |
| Game cutscene, music video, concert or live footage, AV-primary character study | Scene, performance, track | `CONTINUOUS_AV` | [Generic continuous-AV method](../analytical-methods/GENERIC_CONTINUOUS_AUDIOVISUAL_ANALYTICAL_METHOD.md) | Primary lane. Text and frame lanes verify wording and locators |
| Audio drama, voice lines, songs without picture | Track, line set | `CONTINUOUS_AV` session or a verified `audio_content_inspection` route | Audio passes of the generic continuous-AV method | Primary lane for delivery claims |
| Character reconstruction, any medium | Subject, state | Inherits the lanes of its evidence | [Generic character reconstruction method](../analytical-methods/GENERIC_CHARACTER_RECONSTRUCTION_METHOD.md) | When voice or performance dimensions are assessed from AV evidence |
| Project architecture, any medium | Project | Not applicable | [Generic multi-document synthesis architecture template](../analytical-methods/GENERIC_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_TEMPLATE.md) | The architecture names homes for AV-lane findings when a series adopts the lane |

The corpus reference methods are opt-in bootstrap references under the initiation policy (Section 3.3). None of them satisfies a project's own governing-method requirement or opens a sequential-analysis lock.

Name the source's primary language explicitly. It is Japanese for most anime and manga in the corpus, but not all: donghua are normally Mandarin, manhwa Korean. Wording claims rest on the primary-language layer. OCR-reconstructed subtitles, ASR transcripts, and a model's own listening transcription are derivatives. Record their production method and confidence, and never let a listening transcription override a better primary-language text layer.

## 4. Lane claim permissions

Each lane may assert the claims its inspection route supports. A claim outside a lane's permissions is queued for the lane that can test it, narrowed to what the lane can support, or left `OPEN`. Series evidence-label vocabularies remain valid. Where lanes mix inside one artifact, record the inspection route with the claim.

| Claim type | `BUNDLE_MEDIATED` | `CONTINUOUS_AV` |
|---|---|---|
| Exact source-language wording, register, address, honorifics | Asserts from the primary-language subtitle or transcript layer | Does not override that layer. May flag a suspected subtitle divergence for text-lane verification |
| Static composition, costume, setting, isolated expression | Asserts from clean frames | Asserts, anchored to a bundle frame or cue |
| Dialogue chronology, presence, location | Asserts | Asserts |
| Measured timing: pause length, response latency, onset, mixed-track energy | Asserts as acoustic measurement from analysis audio | Reports perceived timing as approximate. Exact values remain measurements |
| Motion, gesture or gaze trajectory, microperformance over time | Endpoint claims only (bundle spec Section 8.7). Queues path claims | Asserts as continuous observation, bounded by the effective sampling rate |
| Camera movement, transitions, editing rhythm | Shot boundaries and durations from the shot index. Queues movement and transition claims | Asserts |
| Vocal delivery: breath, tremor, voice quality, prosodic shape | Only with verified `audio_content_inspection`, as auditory observation. Otherwise measurement-bounded | Asserts as auditory observation with confidence |
| Music dramaturgy: cue entry and exit against cut, gesture, or line; development inside a song | Cue timing by measurement. Queues image–music synchronization | Asserts |
| Speaker or singer attribution where it is not textually marked | Not from camera focus alone | Only with corroboration such as lyric allocation, visible lip movement, or contrast with that character's established voice. Never from recognizing a voice actor |
| Lyric or dialogue content | From the text layer only | From the text layer only |
| Offscreen sound, sound bridges, silence, spatial sound | Silence and energy by measurement. Queues source and bridge claims | Asserts |
| Emotion, intention, motive | Inference or interpretation only | Inference or interpretation only. Perceiving delivery is not perceiving an inner state |

Either lane may contest the other only with evidence on a channel it can inspect. The reconciliation protocol (Sections 4.3 and 5.1–5.2) states how disputes between lanes are handled.

## 5. Current owner lane assignment

**Dated operational fact, owner-reported 2026-10-24.** This records the owner's present division of labor (`OWNER_REPORTED_WORKFLOW` under reasoning policy Section 6). It is not a provider snapshot, a capability certification, or a benchmark. Each session still verifies its capabilities under topology Section 5.

| Provider surface | Owner-assigned responsibility | Lanes normally used |
|---|---|---|
| OpenAI ChatGPT / Codex | Primary literary analysis and writing; sequential readings, monographs, synthesis | `TEXT`, `STILL_IMAGE`, `BUNDLE_MEDIATED` |
| Anthropic Claude | Repository automation, tooling, governance, and scheduled maintenance agents | `TEXT`, `STILL_IMAGE` when assigned analytical work |
| Google Gemini | Audiovisual specialist: performed voice and musical dramaturgy | `CONTINUOUS_AV` |

When the owner changes this assignment, update this table and its date. Series methods should name lanes, not providers, so an assignment change requires no series restructuring.

## 6. Series adoption: a lane-split method family

A series adopts continuous AV analysis by declaring a **method family**, not by replacing its method. The family has up to three members:

1. **Governing method**: the existing series method, which continues to govern sequential reading in its current lane.
2. **AV-lane companion method**: adapted from the generic continuous-AV method. It names the series' AV-load-bearing channels (for example, insert-song dramaturgy, choreography, combat geography, or a lead's vocal register), its default escalation state, and its clock and anchoring conventions.
3. **Reconciliation profile**: the claim classes that must pass through the reconciliation protocol (for example, every state-changing musical event), the queue granularity (per episode or per tranche), and any series-specific tolerance.

The members may be sections of one document or separate files, as long as each responsibility is explicit. The series architecture must also name cumulative homes for AV-lane findings, such as a voice or musical-dramaturgy ledger, in its responsibility matrix (initiation Section 6).

Adoption rules:

- Mature projects remain grandfathered (initiation Section 10). Adopt at the next natural analytical boundary, through the series' own branch and its analysis author.
- AV findings that pressure a frozen reading or checkpoint are routed as errata or claim revisions. They never rewrite the frozen artifact (archive policy; AGENT_ROUTING Section 4.2).
- A series method that worked around the absence of listening (for example, by restricting performance claims to acoustic measurement) keeps those restrictions for its bundle lane. The AV companion method states which restrictions it lifts for `CONTINUOUS_AV` claims.
- Backfill earlier units only when a missing AV observation creates a material evidence gap (initiation Section 5.12).

### 6.1 Illustrative mapping: Love Live! Superstar!! Analytical Method V2

This mapping shows how one mature method would split. It is illustrative and is not a change to that series. The series' analysis author owns any actual adoption.

| Method V2 pass | Lane after adoption |
|---|---|
| Pass 0: source lock and local extraction | `BUNDLE_MEDIATED`, plus AV-object lock and clock calibration in the AV companion |
| Passes 1–5: structure, character state, relationships, institution, cohort | `BUNDLE_MEDIATED` (governing method) |
| Pass 6: performance and musical dramaturgy, M2 and M3 events | Reconciled. Every M2 and M3 event is queued for `CONTINUOUS_AV` review |
| Pass 6B: internal performance segmentation | `CONTINUOUS_AV` primary; the bundle lane verifies lyric allocation from text |
| Pass 6C and 7A: perceptual limits and acoustic audit | Measurements stay in the bundle lane; delivery and timbre claims move to `CONTINUOUS_AV` |
| Pass 7: Japanese voice and register | `BUNDLE_MEDIATED` for wording; `CONTINUOUS_AV` for performed delivery |
| Pass 8: visual and spatial grammar | `BUNDLE_MEDIATED` for composition; `CONTINUOUS_AV` for movement and blocking |
| Pass 9: music and sound outside songs | `CONTINUOUS_AV`, with bundle-lane measurements |
| Pass 10: counterevidence | Both lanes |
| Pass 11: cumulative deltas and ledgers | The governing method's author, after reconciliation |

## 7. Non-goals

This policy creates no validator, schema, workflow, or new evidence object. It does not change episode-bundle semantics, video-escalation states, repository roles, or the reasoning policy's provider snapshot. It does not authorize any source acquisition, paid service, or new tool.

## Changelog

### v1.0 - 2026-10-24 - Initial policy

Defines inspection lanes and their claim permissions, routes each source medium to a corpus reference method and default lane, records the owner's current lane assignment as a dated operational fact, and defines how a series adopts continuous audiovisual analysis through a lane-split method family.
