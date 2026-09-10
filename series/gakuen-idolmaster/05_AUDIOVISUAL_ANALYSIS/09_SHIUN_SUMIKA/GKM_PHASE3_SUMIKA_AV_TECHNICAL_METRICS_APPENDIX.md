---
series: GKM
artifact_type: audit
scope: CHARACTER_SHIUN_SUMIKA_AV_TECHNICAL_METRICS
character: Shiun Sumika / 紫雲清夏
generation: V2
status: canonical
source_boundary: ffprobe, SHA-256, sampled-frame, and full-mix/source-level measurements for all 22 logical AV objects; Dear 028–037 direct backfill uses an equivalent 720p30 direct-upload materialization while the oversized Drive original remains provenance
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
last_updated: '2026-08-17'
title: Gakuen Idolmaster V2 — Shiun Sumika AV Technical Metrics Appendix
parent_authority: GKM_SUMIKA_COMPLETE_AUDIOVISUAL_BASELINE.md
---

# SHIUN SUMIKA — AV TECHNICAL METRICS APPENDIX

## 0. Interpretation limits

These measurements support auditability and source comparison. They are not isolated measurements of Minato Miya's vocal stem, motion-capture quality scores, medical evidence, objective genre labels, or direct measures of charisma, authenticity, emotion, and dance skill.

The authoritative byte-level inventory is `GKM_PHASE3_SUMIKA_AUDIOVISUAL_SOURCE_MANIFEST.json`.

## 1. Materialization summary

- logical staged AV objects: **22**
- logical AV objects directly inspected at the current boundary: **22**
- oversized Drive originals still requiring connector-local materialization: **0 for analytical completeness**
- Dear 028–037 provenance object in Drive: **549,927,147 bytes**; analysis backfill uses a directly uploaded equivalent 720p30 materialization
- locally inspected source identities and alternate-materialization metadata: recorded in manifest
- static/full-mix `カクシタワタシ`: classified as audio presentation, not authored MV

## 2. Music/performance source metrics

| source | form | duration | probed resolution | integrated loudness | loudness range | true peak |
|---|---|---:|---:|---:|---:|---:|
| `Campus mode!! [Sumika]` | 3DMV | 161.2 s | 1920×1080 | -15.1 LUFS | 3.4 LU | -2.6 dBFS |
| `Howling over the World [Sumika]` | 3DMV | 110.1 s | 1920×1080 | -13.8 | 5.8 | -0.2 |
| `Love & Joy [Sumika]` | 3DMV | 176.6 s | 1920×1080 | -13.5 | 5.8 | 0.0 |
| `Tame-Lie-One-Step [Sumika]` | 3DMV | 158.2 s | 1920×1080 | -13.4 | 7.2 | 0.1 |
| `がむしゃらに行こう！ [Sumika]` | 3DMV | 109.6 s | 1920×1080 | -14.0 | 4.6 | -0.3 |
| `ときめきエモーション` | 3DMV | 160.4 s | 1920×1080 | -12.4 | 3.7 | 0.1 |
| `カクシタワタシ [Sumika]` | 3DMV | 200.6 s | 1920×1080 | -13.6 | 13.8 | 0.3 |
| `ミラクルナナウ(ﾟ∀ﾟ)！ [Sumika]` | 3DMV | 116.7 s | 1920×1080 | -13.7 | 4.4 | -0.4 |
| `カクシタワタシ` | static full mix | 199.9 s | 1080×1080 | -7.6 | 3.8 | 0.2 |
| `Kira Kira` | official MV | 180.0 s | 1920×1080 | -9.1 | 6.3 | 0.2 |
| `Love & Joy` | official MV | 232.2 s | 720×1280 | -10.4 | 4.0 | 0.1 |
| `Tame-Lie-One-Step` | official MV | 240.3 s | 1920×1080 | -8.2 | 3.7 | -0.4 |
| `ときめきエモーション` | official MV | 209.0 s | 1920×1080 | -8.1 | 5.6 | -0.1 |

## 2.1 Dear 028–037 direct-backfill materialization

| field | value |
|---|---|
| logical object | Dear 028–037 / STEP4 H.I.F. |
| provenance Drive ID | `1GDVAt5evYW4KoNAxLcZW5r3-u8qkW1Vn` |
| Drive-original size | 549,927,147 bytes |
| analysis materialization | direct ChatGPT upload, 720p30 |
| analysis size | 195,093,333 bytes |
| duration | 4147.548299 s (69:07.5) |
| video | H.264, 1280×720, 30/1 fps, ~237,615 bps |
| audio | AAC-LC, 44.1 kHz, stereo, ~127,999 bps |
| SHA-256 | `d95d80b4df9e104b4ed8a9c6f1c3c612f5907260f2e7b426eecafb537601a591` |

The direct upload is treated as an **analysis materialization of the existing logical source**, not a 23rd story object. Source Lock 1.0 remains the authority for exact wording and route semantics.

### Mixed-scene late-state probes

| segment | approximate state | RMS dB | F0-proxy median Hz | F0-proxy IQR Hz |
|---|---|---:|---:|---:|
| Dear 032 trauma start | explicit trauma naming | -21.39 | 288.1 | 43.3 |
| Dear 032 strength claim | `あたし、強くなったんだよ！` | -22.82 | 331.0 | 128.6 |
| Dear 032 public promise | audience-directed courage | -21.91 | 365.1 | 91.6 |
| Dear 032 thanks | tearful gratitude | -23.44 | 308.8 | — |
| Dear 032 humor restore | social continuity returns | -21.85 | 406.3 | — |
| Dear 034 fear/self-doubt | private fear | -21.71 | 267.3 | — |
| Dear 034 hand/thanks | accepted support | -23.62 | 305.2 | — |
| Dear 036 strength/directive | Prima Stella public address | -21.51 | 409.8 | — |
| Dear 036 final address | summit promise | -22.14 | 383.5 | — |
| Dear 037 win uncertainty | private aftermath | — | 264.2 | — |
| Dear 037 truth request | role-suspension / reciprocity | — | 314.2 | — |
| Dear 037 future | renewed future-facing brightness | — | 373.6 | wide |

These are **mixed-source proxies**, not speaker-isolated measurements. The safe use is only the broad observation that several public-promise/summit/future-facing segments show higher pitch/projection proxies than private fear/trauma segments, in agreement with the directly visible and semantically controlled expansion.

## 3. Safe technical inferences

- Official released sources are generally mastered hotter than game-capture 3DMVs. This is a source-presentation difference.
- `カクシタワタシ` 3DMV has a larger source-level loudness-range value than the other 3DMV captures, consistent with a broader mix-level quiet/loud contrast; it does not isolate Sumika's voice.
- The official `Love & Joy` MV is vertical 720×1280, confirming that the phone/social interface is part of its delivered format rather than an incidental crop.
- All principal rendered performances are available at 1920×1080 and 60 fps in the staged captures, sufficient for broad body-line, blocking, gesture, and camera analysis.
- Dear/song commu sources are 1280×720/30 fps and adequate for acted timing, expression, and blocking, but not laboratory facial-motion analysis.

## 4. Unsafe technical inferences

Do not use these measurements to:

- rank Sumika against other characters by singing or dance talent;
- claim a pure vocal pitch, timbre, breathiness, or dynamic range;
- infer emotion directly from LUFS;
- treat greater movement as better movement;
- treat the official MV mix as a louder in-story performance;
- claim medical recovery from visual smoothness;
- convert mixed-scene F0/loudness proxies into claims about Sumika's pure vocal timbre, pitch, breath, or intrinsic emotional intensity.

## 5. Reproducibility assets

Working assets retained locally during analysis included:

- ffprobe manifest;
- SHA-256 inventory;
- source-level audio metric CSV/JSON;
- 22 logical-source visual inspections, including dedicated late Dear 032/034/036/037 contact sheets;
- selected performance-pose montages;
- source-form classification map.

Only the canonical manifest, appendix, and analytical findings are promoted to Drive. Temporary frame extraction and scratch data are not required as current authority.
