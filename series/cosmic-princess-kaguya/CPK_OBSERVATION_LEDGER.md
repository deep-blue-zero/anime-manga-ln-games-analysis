---
title: "Cosmic Princess Kaguya! — scene and audiovisual observation ledger"
series: cosmic-princess-kaguya
artifact_id: CPK_OBSERVATION_LEDGER
artifact_type: audiovisual_observation_ledger
generation: CPK-G1
version: "1.0"
status: canonical
authority_scope: "Canonical descriptive-evidence schema and retrieval home; zero film observations"
source_boundary: "No narrative source admitted or inspected"
canonical_home: series/cosmic-princess-kaguya/CPK_OBSERVATION_LEDGER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Scene and audiovisual observations

## Purpose and present controls

This is the descriptive evidence home for the full film, with distinct scene, observation, music-event and coverage records. Interpretive claims belong in [the claim ledger](CPK_CLAIM_REVISION_LEDGER.md); attributed subject/relationship state belongs in [the state ledger](CPK_CHARACTER_RELATIONSHIP_LEDGER.md). IDs below describe allocation rules, not existing observations.

| Control | Current state |
|---|---|
| Admitted/inspected film units | 0 |
| Scene/movement records | 0 |
| Audiovisual/visual observations | 0 |
| Musical-event records | 0 |
| Actual channel/interval coverage records | 0 |
| Clock and media witness binding | None; source inventory owns future records |

## Shared locator and history rules

Allocate stable IDs only from inspected evidence: `CPK-<run>-Snnnn` scenes, `CPK-<run>-Onnnn` observations, `CPK-<run>-Mnnnn` musical events. Run IDs are assigned under the source inventory; no run exists now. Do not recycle deleted/rejected IDs. Cross-run matches are explicit crosswalks, never identity assumed from matching sequence numbers.

Each evidence locator carries `F01 + witness/hash ref + clock/map ID + bounded start/end + cue/frame/shot/audio anchor + achieved precision`. Include derivative/chunk identity where applicable. An observation with only content-based location is marked uncalibrated and cannot support precise cross-object timing. Distributed patterns cite representative bounded occurrences and counterexamples; a whole-film citation alone is inadequate for a consequential claim.

Preserve descriptive original rows and their run context. Corrections append an attributable replacement/revision with old/new locator and reason; current pointers may update. Freeze the primary pre-audit log/snapshot with the candidate. Later observations, including any made after claim exposure, carry that provenance. A blind verifier never reads this populated primary home before freezing its own separate audit log.

## Scene and movement schema

Required fields: `scene_id | run | witness/clock refs | inspected interval | presentation order | movement/sequence membership | boundary basis and confidence | event-time constraints or UNKNOWN | location/frame-of-presentation | source-established participants | entering/exit knowledge-state refs | observed action/change | causal claim refs | disclosure frontier | reading anchor | gaps/limitations`.

Movement/sequence membership is interpretive navigation, not primary fact. Permit overlapping musical/dramatic intervals rather than force a song to equal a scene. Preserve the difference between a mechanically detected cut and a narratively meaningful boundary. Do not create empty scene rows before inspection.

## Observation schema

Required fields: `obs_id | run | scene refs | witness/clock refs | calibrated interval | cue/frame/shot/content anchors | channel(s) | descriptive observation | evidence class | confidence and reason | effective sampling/inspection resolution | actual inspection route | re-viewed and pass reference | second-pass discrepancy | corroboration route/result where required | REPORTED/ANCHORED/disputed provenance | linked claim refs | limits | observer/exposure state`.

Channels include static composition/color/light/compositing, camera/spatial relation, editing, gesture/gaze/facial or bodily motion, voice, music, sound and synchronization. Use method classes `CAV/AO/FRM/TXT/AM/HL`; `INF/INT` explanations route to claims. A descriptive observation must remain readable without importing its proposed interpretation.

`ANCHORED` requires calibrated bounded evidence, an anchor, focused reinspection, resolution adequate to the claim and mandatory corroboration under the continuous-AV method. Repetition by the same model alone is not independent corroboration. A high-confidence REPORTED observation is still REPORTED. A disputed load-bearing observation remains provisional until resolved.

## Musical-event schema

Required fields: `music_id | run | scene/obs refs | witness/clock interval and anchors | significance M0/M1/M2/M3 | cue/track identity or UNKNOWN | attribution evidence/uncertainty | audible/visible internal segment boundaries | diegetic/nondiegetic/ambiguous state and shifts | entry/exit versus cuts/words/actions | development heard with confidence | audience/witness configuration | lyric TXT witness and uncertainty or NOT_USED | recurrence type and occurrence refs | proposed dramatic-function claim refs | affected subject/directed-edge refs | reinspection/corroboration | alternatives/limits`.

M2/M3 need full records; M3 also updates affected state/claims. M0 requires no entry absent a retrieval need; M1 can be compact. Separate observation of musical change from interpretation of its effect. Record uncertain source, instrumentation, lyric allocation or sound diegesis explicitly. Album credits/versions cannot establish the film performance by themselves.

## Coverage records and transactions

Coverage schema: `run | witness/clock refs | interval/channel | REQUIRED/OPTIONAL/OUT_OF_SCOPE | actual inspection method and sampling | inspection state | observation IDs | omitted ranges/reason | required unresolved consequence | next owner and acceptance condition`.

Use handoff inspection states exactly as routed by the source inventory. Coverage and capability are separate: verified continuous-AV access does not certify complete inspection. At primary closeout reconcile coverage against the entire authorized measured film range, credits and musical passages included. Link the inventory's source-level totals rather than count frames as viewed time. No empty record is evidence of absence or no change.

## Actual records

None. This ledger is initialized for later authorized evidence capture; it contains no timestamps, claims or observed scenes.
