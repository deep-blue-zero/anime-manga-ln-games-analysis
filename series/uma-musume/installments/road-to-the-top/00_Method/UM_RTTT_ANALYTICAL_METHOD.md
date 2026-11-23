---
title: "Road to the Top — Analytical method"
artifact_id: UM_RTTT_ANALYTICAL_METHOD
artifact_type: analytical_method
series: uma-musume
installment: road-to-the-top
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: UM-RTTT-INITIAL
source_boundary: "Operational method for the original 2023 four-episode anime; no narrative source admitted or episode reading completed by this bootstrap"
canonical_home: series/uma-musume/installments/road-to-the-top/00_Method/UM_RTTT_ANALYTICAL_METHOD.md
created: 2026-11-22
last_updated: 2026-11-22
recommended_reasoning_class: SUBSTANTIVE_ANALYSIS
---

# Road to the Top — Analytical method

This method governs source-grounded analysis of the original four-episode **Uma Musume: Pretty Derby — ROAD TO THE TOP**. It is a canonical procedure, not an account of events already observed. Accepted narrative observations, completed readings and established narrative claims at bootstrap: **zero**. Start at the [current-state entrypoint](../../../CURRENT_STATE_AND_CORPUS_MAP.md), then the [source inventory](../01_Sources/UM_RTTT_SOURCE_INVENTORY.md) and paired [synthesis architecture](UM_RTTT_SYNTHESIS_ARCHITECTURE.md).

## 1. Scope, versions and entering knowledge

Use the original 2023 episodic presentation as the intended primary narrative corpus. Its units are E01–E04, identified by the Japanese titles in the [production metadata register](../01_Sources/UM_RTTT_PRODUCTION_METADATA.md). A filename, translated subtitle title or distributor label does not establish edition identity. Match the actual bytes to the source register and retain the episode's own clock, credits and completeness findings.

Keep these categories separate throughout:

| Category | Permitted role | Boundary |
| --- | --- | --- |
| Original 2023 four-episode anime | Intended primary narrative evidence after source admission | Episode-local sources and clocks; no theatrical substitution |
| 2024 theatrical re-edit | A separately identified version for a future authorized comparison | Additional material and editorial changes need their own locators; no presumed timestamp equivalence |
| Other anime, games, films, manga and supplementary franchise material | Future comparison or explicitly labeled context | Availability does not admit it; do not use it to complete an earlier characterization |
| Actual horses and Japanese racing history | External historical context | Historical outcome, fictional event and inferred adaptation choice are different propositions |

At a sequential run's start, record the authorized start, endpoint, prospective/retrospective mode and existing exposure. Metadata knowledge and the user's proposed research topics are not observations from E01. Quarantine memories of later episodes, historical winners, franchise material and familiar interpretations. If exposed, record the affected knowledge boundary; do not manufacture an unspoiled prediction. No E02–E04 inspection is authorized by an E01-only run.

## 2. Distinguish architecture, source admission and run scope

The architecture lock, source admission, run authorization and actual inspection capability are separate checks. This bootstrap leaves `SEQUENTIAL_ANALYSIS_LOCK = CLOSED`; its existence does not authorize an episode reading. The exact remaining conditions and their resolution actions live in the [readiness audit](../05_Run_State/UM_RTTT_READINESS_AUDIT.md), with the first-run transaction in [E01 next run](../05_Run_State/UM_RTTT_E01_NEXT_RUN.md).

Before the first reading, verify the current source witness, edition/completeness, available Japanese language route, source clock and evidence access; resolve the initialization requirements in the architecture and current-state entrypoint; recover an owner-authorized E01 run; and assign the independent reading roles below. Do not require completion of another Uma Musume installment or any Psycho-Pass-specific prerequisite. If one witness is unusable, inspect an available alternative rather than treating that particular encode as a permanent gate.

## 3. Evidence identity and epistemic discipline

The [scene and evidence ledger](../03_Ledgers/UM_RTTT_SCENE_EVIDENCE_LEDGER.md) is the observation home. IDs are stable, never reused, and never renumbered when rows are rejected or a better source arrives. A corrected locator retains its earlier value and correction reason. The inventory identifies the preferred E01 witness as `UM-RTTT-2023-ONA-E01-W01`, with `UM-RTTT-2023-ONA-E01-W02` the alternative; E02–E04 use the same episode/witness vocabulary. Preserve the inventory's actual edition findings and uncertainty. An unknown upstream master is a provenance limitation, not an automatic prohibition on analysis of identified, content-checked and decodable local bytes; block only a claim whose evidence actually depends on resolving that uncertainty.

| Object | Identifier pattern | Responsibility |
| --- | --- | --- |
| Scene | `RTTT-E01-SC001` | Episode-local segmentation unit with explicit boundaries |
| Observation | `RTTT-E01-OBS0001` | Recoverable descriptive source evidence |
| Character state | `RTTT-E01-CS0001` | Time-bounded state with evidence and uncertainty |
| Directed relationship state | `RTTT-E01-RS0001` | A's attitude/action toward B, distinct from B toward A |
| Analytical claim | `RTTT-CLM0001` | Interpretation with supporting and adverse observations |
| Depicted competition | `RTTT-E01-RACE01` | Narrative race or competition instance, once located |
| Research question/hypothesis | `RTTT-HYP0001` | A testable question, not a conclusion |
| External context | `RTTT-CTX0001` | A separately cited historical or supplementary fact |

Evidence records include installment/episode; scene; source ID and edition; start/end timestamps and declared clock; speaker/subjects; concise scene description; observed visual/audio/text details; inspection route and inspected interval; a short Japanese excerpt and translation when needed; confidence and its reason; limitations/counterevidence; and related state, race and claim IDs. Interpretation belongs in the claim ledger, linked from the observation. Do not hide interpretation in an observation's descriptive field.

| Epistemic state | Admission rule |
| --- | --- |
| Verified production fact | Authoritative production/distribution metadata; source and access date recorded |
| Primary-source observation | Directly recoverable from the identified anime witness in a declared inspection route |
| Grounded interpretation | Argument supported by specific observation IDs, with alternatives and scope |
| Tentative hypothesis | Proposed explanation or question awaiting a test; no evidentiary upgrade from repetition |
| External contextual fact | Independently cited historical/supplementary source; not anime canon |
| Unverified / unavailable | Not independently established or not inspectable through the current route |

These epistemic states differ from confidence. A high-confidence hypothesis remains a hypothesis. Several agents repeating one model's report do not create independent corroboration. Absence claims require adequate coverage: a few sampled frames cannot establish that a character never looks back or that music is absent from a sequence.

## 4. Source-facing episode passes

Use the [episode index and four templates](../02_Episodes/UM_RTTT_EPISODE_ANALYSIS_INDEX.md). Each accepted episode has the following workflow; document interruptions and unfinished coverage instead of treating drafted prose as completion.

1. **Lock and orient.** Read the current entering-state ledgers, freeze unresolved hypotheses before new exposure, identify the admitted witness/streams/clock, verify derivatives and declare the complete assigned unit and inspection limits. Keep E01 prospective knowledge distinct from later retrospective commentary.
2. **Inspect the complete authorized unit.** The principal covers the whole episode through the permitted evidence routes. Record what was actually inspected in each channel; directory enumeration or successful extraction is not perceptual coverage. Independent participants inspect sources according to their bounded responsibilities before adopting the principal's interpretation.
3. **Reconstruct the episode.** Segment scenes when setting, time, focalization or dramatic action changes; preserve uncertainty at dissolves, flashbacks and imagined images. Capture causal chronology, revelations and information withholding. After complete-unit inspection, write the front-of-reading human-facing synopsis within that episode's disclosure boundary. A synopsis enables retrieval but does not replace analysis.
4. **Track people in situations.** For Narita Top Road, Admire Vega and T.M. Opera O, record stated goals, choices, attention, self-presentation, emotional indications, relations and consequences. Add other people only when observed. Preserve ordinary behavior, preferences, linguistic choices and counterexamples as well as conspicuous dramatic events.
5. **Read audiovisual construction.** Examine composition, staging, animation, timing, sound, music and voice through the route each claim needs. Use the companion method below for temporal/performed claims. Log unanswered verification questions neutrally.
6. **Test claims and alternatives.** Build interpretations from observations; seek adverse evidence and the strongest plausible rival reading. Compare a character with herself across situations before assigning a general trait. Resolve translation-sensitive claims against Japanese evidence.
7. **Reconcile and write through.** Preserve independent contributions and critical review; adjudicate significant disagreements; update all affected cumulative ledgers, hypothesis statuses and claim histories; record open required evidence; then update the episode and current-state coverage. Do not advance accepted high-water while acceptance conditions remain unmet.

## 5. Character, rivalry and interpretation lenses

The following prompts are **research responsibilities**, not established character descriptions. The [question register](../04_Research/UM_RTTT_RESEARCH_QUESTIONS.md) carries tests and disconfirming evidence.

- **Competing excellence:** compare what winning, improvement, duty, reputation and self-worth mean to Narita Top Road, Admire Vega and T.M. Opera O. Do not assign fixed psychological archetypes. Distinguish explicit speech, observed decisions, public persona, inferred motives and viewer interpretation.
- **Narita Top Road:** investigate effort, supporters' expectations, trainer interaction, encouragement, belonging and whether determination becomes a burden. Test whether deserving success and obtaining it are kept distinct. Do not infer an obligation solely because supporters cheer.
- **Admire Vega:** investigate the source's treatment of memory, absence, grief, guilt, obligation, happiness and self-denial only as evidence warrants. Keep expressed beliefs separate from behavioral implications and speculative explanations. Avoid clinical diagnosis and do not assume every isolated composition signifies grief.
- **T.M. Opera O:** compare verbal theatricality with observed preparation, choices, reactions and treatment of competitors. Ask whether flamboyance organizes a competitive philosophy, comic contrast or several functions; actively retain moments that complicate confidence or consideration.
- **Rivalry and recognition:** track directed gestures, acknowledgment, proximity, shared work, support and responses to another's difficulty. Separate friendship, admiration, intimacy, strategic attention and possible romantic subtext. Emotional intensity alone establishes none of these; preserve alternative readings and their unequal evidentiary strengths.

Every state row names whose knowledge and interpretation it records. A spectator's impression is not the runner's motive. A later explanation does not retroactively become what a character or first-time viewer knew earlier. Use canonical names once identity is established; retain anonymity where the source withholds it. Check synopsis, a substantial middle section and exit state for ambiguous referents, speaker attribution and knowledge leakage before acceptance.

## 6. AV companion: racing, performance and musical form

This method family adopts a `BUNDLE_MEDIATED` governing lane with `TEXT` for Japanese wording and `STILL_IMAGE` for exact compositions. Its `CONTINUOUS_AV` companion covers channels that require temporal inspection. A verified audio-content route may support auditory observations within its actual scope, but stills plus audio do not become native continuous AV. The [AV workflow](../01_Sources/UM_RTTT_AV_WORKFLOW.md) owns technical extraction commands, selected streams and artifact locations. Prefer the existing ffprobe/ffmpeg workflow; no new chunking or hosted service is required by this method.

Use source clock `HH:MM:SS.mmm` and retain stream start times, pre-roll, trim and subtitle offsets. Derivatives map back to source time. For full-episode clock calibration normally use at least three anchors across beginning, middle and end, prioritizing verified Japanese cues, then shared audiovisual events or independently measured timing. Record offset, drift and achieved precision. ±0.5 s is a navigation baseline, never authority for subsecond synchronization. Frame- or sample-accurate claims need deterministic measurements of the relevant source.

| Channel | Capture and question | Evidentiary limit |
| --- | --- | --- |
| Race space and simulated camera | Runner order, viewpoint, depth, occlusion, distance cues, angles and camera path | A still supports composition; movement and spatial continuity need temporal evidence |
| Animation and pace | Posture, expressions, stride changes, acceleration/deceleration, held poses and contrast baselines | Do not infer speed, exertion or movement from separated endpoint frames |
| Editing | Cut order, shot duration, subjective/objective switches, withheld reactions and replay | Sampling can miss cuts; exact lengths need shot/source verification |
| Voice and exertion | Words versus delivery; breath, effort sounds, pauses and changes within a voice | Transcript/ASR does not establish timbre, prosody, breath or emotion |
| Environment and crowds | Hooves/footfalls, space, commentator/crowd placement, sound bridges and quiet | A soundtrack change is an observation; its emotional effect is interpretation |
| Music and silence | Cue entrance/exit, texture, perceived intensity, vocal placement, overlap and aftermath | Do not identify a cue, singer, instrument or lyric by guess; measure claimed alignment |
| OP and vocal sequences | Position, repetition/variation, who/what is represented and relation to episode trajectories | A recurring OP is not proof of narrative intention or a character's private knowledge |

For every located race, separate tactical chronology and depicted outcome from viewer experience. Map competitive stakes before, during and after; ask how framing, temporal dilation, sound and perspective make a stretch feel urgent or restrained. Track who perceives whom and whether commentary supplies information absent from the image. Do not reduce a race reading to the finishing order. Trace visual motifs, light, recurring compositions and musical cues with individual observations before assigning a pattern; include contrary occurrences and production-convention explanations.

### Reconciliation profile

Queue by episode, with each item an interval and neutral observable question. Required classes are load-bearing claims about race movement/spatial continuity, editorial pacing, music-image timing, performed voice/breath, sound perspective and any temporally dependent character/relationship change. Decorative enrichment is optional and cannot silently replace a required item.

Use `VIDEO_NOT_REQUIRED` when adequate evidence supports the actual claim without video; `VIDEO_TARGETED_ESCALATION` for a diagnostic interval that existing derivatives cannot resolve; and `VIDEO_FULL_EPISODE_ESCALATION` only when the material temporal question is genuinely distributed across the episode. Targeted escalation is the normal default for located temporal questions. These states describe evidence need, not successful inspection.

The AV reviewer first receives only source/clock context and neutral questions. The reviewer inspects, logs and freezes observations before receiving the principal's claims and disconfirmation tests. Record whether this order was achieved. Verify continuous picture-and-sound perception, actual inspected scope and effective sampling rate (`UNKNOWN` if not established). Re-view load-bearing observations; sparse/unknown sampling cannot support rapid visual claims without finer inspection or measurement. Wording/lyrics still use the Japanese text route; suspected divergence is a translation issue, not permission to replace text by a listening guess.

The integrator records `PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT` or `OPEN`, and writes adopted observations into the AV ledger. A model report is not the underlying source. Follow the [corpus reconciliation protocol](../../../../../governance/source-policies/MANGA_ANIME_AUDIOVISUAL_RECONCILIATION_PROTOCOL.md) for contest grounds, one bounded return, possible independent verification and unresolved provisional items. Required unresolved items block the corresponding completion claim; preserve supported bounded findings while the missing route is resolved.

## 7. Japanese dialogue and translation

Prefer identified original-language subtitles or verified transcript material where available. Record source/track, language tags versus actual language verification, cue IDs, timing and any corrections. ASR, OCR and listening transcription are derivatives with explicit uncertainty. Record only brief evidentiary Japanese excerpts in Git, with literal/contextual translation and the point at issue; full subtitle dumps and raw language derivatives stay outside Git.

When an English subtitle compresses a pronoun, obligation, modality, politeness choice or emotional force, preserve its brief relevant rendering alongside the Japanese, identify the competing translations, and leave the affected claim open until checked. Distinguish spoken dialogue, commentary, onscreen text, lyrics and nonverbal vocalization. Do not attribute a speaker by recognizing a performer or infer a singer from character presence in a shot.

## 8. Historical adaptation pathway

Create external context entries only when needed, beginning with authoritative JRA race records and other primary racing accounts for the 1999 classics. Verify each source, date, participants, results and relevant rule instead of copying remembered history. Keep Satsuki Sho, Tokyo Yushun/Japanese Derby and Kikuka Sho as research targets until the anime's relevant material is observed and matched.

Every comparison has three fields: independently verified historical fact (`RTTT-CTX...`); what this version actually depicts (`RTTT-E..-OBS...`/race ID); and the argued relationship (`RTTT-CLM...`). Classify preservation, compression, rearrangement, personification, fictional addition or unresolved mapping with evidence. Similarity does not establish creator intention. Where historical results are known before prospective anime analysis, disclose that exposure and do not import the result into episode evidence or forecast scoring.

## 9. Independent execution and atomic acceptance

The standing episode configuration is principal/integrator, an independently source-aware Japanese-dialogue/character specialist, and a distinct independent critical reviewer. Add an AV specialist when required temporal/performed channels need that capability; the AV specialist may fill an independent role when scope, separation and capability are adequate. The principal must inspect the complete authorized unit. Other participants inspect the decisive source material proportional to their assignments. Four ordinary episodes do not qualify automatically for the reduced very-short-unit configuration.

Independent contexts receive governing method, authorized source frontier and a neutral assignment; they do not inherit the principal's working interpretation. Specialists return source-located observations, rival explanations and limits before integration. A reviewer tests material claims against the source, including underrepresented evidence and alternative explanations. The unit's durable record preserves roles/context separation, exposure, coverage, significant contributions, disagreements and every material disposition. A label such as “agent review passed” is insufficient.

The integrator alone writes cumulative ledgers and current state. Acceptance requires complete required source coverage, real independent contributions and critical examination, reconciled material findings, preserved counterexamples, consistent ledgers/claims, accurate bounds and no concealed required-channel gap. If a required capability is unavailable, leave acceptance/high-water pending and record the exact missing route. Do not invent participation or a new external service.

## 10. Governing references and maintenance

This adapted method uses the corpus [anime reference method](../../../../../governance/analytical-methods/GENERIC_ANIME_EPISODE_ANALYTICAL_METHOD.md), [continuous-AV reference](../../../../../governance/analytical-methods/GENERIC_CONTINUOUS_AUDIOVISUAL_ANALYTICAL_METHOD.md), [episode-bundle specification](../../../../../governance/source-policies/MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md), [inspection-lane policy](../../../../../governance/source-policies/MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md), [execution topology](../../../../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md) and [handoff contract](../../../../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md). They retain their own scope; this method opens no source or publication permission.

Amend only where source experience shows a material need; record version, reason, affected responsibilities and any necessary bounded backfill. Preserve prior observations and prospective freezes, correcting through the claim ledger or an attributable erratum. No corpus-wide reformatting, extra installment or full franchise synthesis is implied.

| Version | Change |
| --- | --- |
| 1.0 | Bootstrap procedure and method family established; no narrative interpretation accepted |
