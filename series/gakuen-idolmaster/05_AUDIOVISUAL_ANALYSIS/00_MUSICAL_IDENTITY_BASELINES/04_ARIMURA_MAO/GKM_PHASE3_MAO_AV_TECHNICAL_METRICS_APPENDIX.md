---
series: GKM
artifact_type: audit
scope: CHARACTER_ARIMURA_MAO_PHASE3_AV_TECHNICAL_METRICS
character: "Arimura Mao / 有村麻央"
generation: V2
status: canonical
source_boundary: "Technical metadata, hashes, source-level measurements, and source-form corrections for 24 directly materialized Mao AV objects"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
last_updated: "2026-08-17"
parent_authority: "GKM_MAO_COMPLETE_AUDIOVISUAL_BASELINE.md"
---

# ARIMURA MAO — PHASE-3 AV TECHNICAL METRICS APPENDIX

## 1. Purpose

This appendix preserves reproducibility and source-class information that would interrupt the reader-facing close readings. Measurements identify files and constrain claims; they do not replace viewing, listening, or textual adjudication.

## 2. Materialization boundary

- Logical staged objects: **24**.
- Locally materialized, probed, hashed, and inspected: **24**.
- Total duration: **18,861.9 seconds / 5.24 hours**.
- Total bytes: **2,265,869,613 / 2.27 GB decimal / 2.11 GiB**.
- Drive-size failures: **none**.

## 3. Source-class inventory

| class | count | use |
| --- | ---: | --- |
| Dear compilations | 4 | longitudinal acted character states |
| Dear bridge | 1 | post-Dear-010 / N.I.A. transition |
| song/idol communications | 8 | artistic negotiation, relationship and voice states |
| authored official MVs | 3 | official symbolic/editorial visual interpretation |
| rendered 3DMV/game performances | 6 | choreography, costume, audience and camera relation |
| static full-song presentations | 2 | complete audio only |

## 4. Important source-form corrections

### 4.1 `Campus mode!!`

`[学マス] 『Campus mode!!』 有村 麻央ver [親愛度10]` remains visually static throughout the sampled timeline. It is classified as **static_full_mix**. It is not an in-story moving live render.

### 4.2 `Feel Jewel Dream`

`Feel Jewel Dream-(1080p25).mp4` is also a static full-song presentation. The separate 1080p60 source is the moving rendered 3DMV.

### 4.3 `ガラクタロード`

The supplied source is approximately 88.4 seconds and labeled A-ending. It is adequate for performance-procedure inspection but not a complete-song form audit.

## 5. Representative metadata

| ID | source | duration | video | fps | audio |
| --- | --- | ---: | --- | ---: | --- |
| D01 | Dear 001–010 | 3100.0 s | 1920×1080 H.264 | 30 | AAC-LC 44.1 kHz ~128 kbps |
| D03 | Dear 011–020 | 3283.3 s | 1280×720 H.264 | 30 | AAC-LC 44.1 kHz ~128 kbps |
| D04 | Dear 021–027 | 2769.5 s | 854×480 H.264 | 30 | AAC-LC 44.1 kHz ~128 kbps |
| D05 | Dear 028–037 | 3127.9 s | 854×480 H.264 | 30 | AAC-LC 44.1 kHz ~128 kbps |
| C07 | `見て` commu | 618.7 s | 1920×1080 H.264 | 60 | AAC-LC 44.1 kHz ~128 kbps |
| M01 | `Fluorite` official MV | 251.2 s | 1920×1080 | 24 | AAC-LC ~256 kbps |
| M03 | FJD static full mix | 202.8 s | 1080×1080 static | 25 | AAC-LC ~256 kbps |
| M05 | `Campus mode!!` 3DMV | 160.1 s | 1920×1080 | 60 | AAC-LC ~128 kbps |
| M07 | `SUGAR FLAVOR` official MV | 188.1 s | 1920×1080 | 24 | AAC-LC ~256 kbps |
| M09 | `ガラクタロード` A-ending | 88.4 s | 1920×1080 | 60 | AAC-LC ~128 kbps |
| M10 | `見て` official MV | 305.4 s | 1920×816 | 24 | AAC-LC ~256 kbps |

The full per-object table and SHA-256 values are in `GKM_PHASE3_MAO_AUDIOVISUAL_SOURCE_MANIFEST.json`.

## 6. Dialogue visual-quality judgment

The 480p Dear sources are lower resolution than the 720p/1080p objects, but their character framing is large and relatively static. Direct sampling supports reliable inspection of:

- gaze direction and eye closure;
- blush and broad expression;
- head angle;
- hand position and gestural scale;
- posture contraction/expansion;
- public versus private staging;
- costume and scene changes.

They are not used for claims requiring fine eyelash, lip contour, or high-frequency facial shading.

## 7. Source-level EBU R128 measurements

| ID | form | integrated LUFS | LRA LU | true peak dBFS |
| --- | --- | ---: | ---: | ---: |
| M01 | official MV | -8.1 | 6.7 | 0.9 |
| M02 | 3DMV | -14.4 | 10.4 | -0.3 |
| M03 | static full mix | -10.3 | 6.9 | -2.1 |
| M04 | 3DMV | -13.3 | 11.1 | -0.2 |
| M05 | 3DMV | -12.4 | 3.1 | -0.1 |
| M06 | static full mix | -8.3 | 3.6 | 0.9 |
| M07 | official MV | -10.3 | 4.1 | 0.1 |
| M08 | 3DMV | -12.7 | 5.6 | -0.1 |
| M09 | short game performance | -12.5 | 3.8 | -0.1 |
| M10 | official MV | -18.2 | 5.1 | -3.6 |
| M11 | 3DMV | -11.4 | 3.9 | -0.1 |

### Limits

- official and game-capture sources use different mastering chains;
- positive reported true peaks can reflect source encoding/reconstruction and are not a character-performance judgment;
- applause, effects, intro silence, and capture gain are included;
- loudness cannot be converted into Mao's vocal power.

## 8. Full-mix spectral descriptors

Broad centroid proxies range from approximately 1.37 kHz (`SUGAR FLAVOR` official) to 1.93 kHz (FJD static full mix). These statistics characterize complete source mixes, not isolated singing. They are used only for cautious relative production descriptions.

## 9. Scene-level voice proxies

Fourteen mixed-scene windows were measured for speech activity, broad pitch activity, and intensity. Examples include calm origin narrative, body/category rupture, cute collision, reclaimed prince, Producer-choice conflict, summer defeat, late photo/prince state, Prima Stella, `0番`, `見て` child rupture/theatre grief/flirtation, and Osaka play/parents.

The results broadly align with visible state changes, but speaker overlap and BGM prevent isolation. No precise claim about Mao's vocal fundamental, breathiness, or resonance is promoted.

## 10. Visual sampling

The audit used:

- uniform contact sheets for all 24 sources;
- denser range sheets for principal MVs/3DMVs;
- five-second or twelve/fifteen-second sheets for key Dear chapters;
- targeted keyframes for `Fluorite` and `見て`;
- direct source review after candidate-location sampling.

Contact sheets are locator aids. They are not substitutes for motion chronology.

## 11. Reproducibility files

The release preserves:

- canonical source manifest;
- source SHA-256 sidecar;
- corrected EBU R128 metrics;
- full-mix audio metrics;
- scene-level audio proxies;
- selected FFprobe manifest/supporting JSON.

Working contact sheets and scripts remain outside the canonical reader-facing corpus unless later needed for an audit.

## 12. Technical conclusion

The packet is technically sufficient for a bounded full AV baseline. All core dialogue, communication, and principal performance objects are accessible. Remaining P1/P2 repertoire is enrichment rather than a missing evidentiary foundation.
