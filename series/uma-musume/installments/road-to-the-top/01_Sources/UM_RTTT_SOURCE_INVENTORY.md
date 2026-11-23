---
title: Road to the Top source inventory and provenance
artifact_id: UM_RTTT_SOURCE_INVENTORY
artifact_type: source_inventory
series: uma-musume
installment: road-to-the-top
generation: V1
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
source_boundary: pre-analysis/technical and production identity only
created: 2026-11-22
last_updated: 2026-11-22
---

# Source inventory and provenance

Eight local MKV witnesses were located and hashed: two candidate sets covering E01–E04. Four preferred W01 witnesses have content-confirmed work/episode identity, visible episode-title cards and ending credits, and successful complete video/audio decode. All eight passed early/middle/late bounded decode and tiny frame/audio extraction. **Narrative admission remains UNADMITTED; no episode reading or narrative high-water mark exists.** See the [machine manifest](UM_RTTT_SOURCE_MANIFEST.json), [production references](UM_RTTT_PRODUCTION_METADATA.md), [AV workflow](UM_RTTT_AV_WORKFLOW.md), and [current state](../../../CURRENT_STATE_AND_CORPUS_MAP.md).

Operational evidence veto: this inventory is production/technical metadata, not literary evidence. Decode success, extraction availability and title-card scouting cannot support a narrative interpretation or advance narrative exposure/analysis high-water marks.

## Discovery scope and privacy

The configured anime extraction corpus manifest, title directories and filename inventory were checked. That manifest contained sixteen registered titles and 185 items; RTTT was absent and had no prepared title bundle. The local raw anime library filename search located two four-episode sets. A bounded analysis-workspace filename search found no RTTT study; two unrelated AV toolkit subpaths were inaccessible, so this is not a whole-disk absence claim. Source-directory enumeration found no external subtitle sidecars. No matching theatrical re-edit video was located by the bounded raw-library filename search.

Private paths, supplier filenames, command arguments, raw probe reports and tiny technical/identity assets remain in the authorized external AV workspace. Public Git carries portable witness IDs and hashes. On the workstation, the retained `PRIVATE_SOURCE_RECEIPT.json` binds each ID to its actual local source. The resumption checkpoint identifies its private location for the owner; this document deliberately contains no machine-specific source path.

## Witness and version boundary

- `UM-RTTT-2023-ONA-E01-W01` through `E04-W01`: preferred technical candidates, supplier-labelled AMZN WEB-DL. Their embedded title cards confirm four separately numbered RTTT episodes. Container creation tags are in April–May 2023; these tags are supporting metadata, not trusted publication dates. Exact distributor/master and acquisition history remain unknown.
- `UM-RTTT-2023-ONA-E01-W02` through `E04-W02`: alternate supplier-labelled H264-AAC candidates. File availability, hashes and stream decoding were inspected; content/edition correspondence and actual spoken language were not. Do not borrow W01 timestamps or language verification for W02.
- `2024-THEATRICAL`: separate reserved comparison edition. No local video admitted or located in this search. Do not map episodic timestamps onto the film or replace the 2023 corpus with it.
- Other franchise productions and historical racing records remain external context until separately scoped. Their presence elsewhere in the library does not admit them.

W01 is a disclosed, content-confirmed episodic witness; analysis does not require proof of byte identity with an official distributor master. Opening/end sampling plus full technical decode supports readiness but is not a frame-complete editorial-completeness comparison. Any missing or altered narrative content discovered during full inspection becomes a localized source issue.

## Exact witness inventory

Durations are container durations, not asserted narrative running times. Bytes and SHA-256 were calculated from the actual existing files on 2026-11-22.

| Source ID | Bytes | Duration seconds | SHA-256 |
|---|---:|---:|---|
| `UM-RTTT-2023-ONA-E01-W01` | 1065946485 | 1462.496 | `270ae37dcb332fe998b2993b0a3aa45badf45da6316a4fd70f562c33837d92d9` |
| `UM-RTTT-2023-ONA-E01-W02` | 246224263 | 1462.509 | `87ba7673d9efbc709e81f231d103f1fe465bec0ea801be740f1b88ebe1daecbd` |
| `UM-RTTT-2023-ONA-E02-W01` | 1170939665 | 1552.448 | `dbcad37a2a47ecce7dae4784927e4aaef71d7f00a0735d0a629d294f2ce3117d` |
| `UM-RTTT-2023-ONA-E02-W02` | 288213971 | 1552.486 | `e841257595861a1d304239ebeea9ff646a86bbdb645dbbb803d2c07b82eb050d` |
| `UM-RTTT-2023-ONA-E03-W01` | 962068395 | 1462.496 | `e74b86dbacba9995a7251366464a31994fb26ed6d24937736d7eab915d9abf78` |
| `UM-RTTT-2023-ONA-E03-W02` | 209587483 | 1462.509 | `9ce57eb5bc18f05463bfbfbed9c50d45947f863b6f321755ec23efc671a45a18` |
| `UM-RTTT-2023-ONA-E04-W01` | 1309161536 | 1638.464 | `db2927197e20feaf621fc5f1a3a31bb883ff88daf92f44c5726dc9cbbda5fcf6` |
| `UM-RTTT-2023-ONA-E04-W02` | 343252749 | 1638.493 | `2861b7687f7a9c941f9ef81c934bf06b909c99ee23befbcc0ce7e21eaa5365ba` |

## Tracks, languages and text availability

Both sets use Matroska, video stream **0**, H.264, 1920×1080, yuv420p, declared 24000/1001 fps, video start 0.000 s; no chapters were reported. Each has one stereo audio stream **1** and four embedded SubRip text streams. All subtitle streams were successfully decoded to an in-memory SRT stream for technical counting/hashing; full wording was neither reviewed nor retained by that check.

| Set | Audio stream 1 | Embedded text streams, global indices | Japanese recovery status |
|---|---|---|---|
| W01 | E-AC3, 48,000 Hz, stereo, 224 kb/s, `jpn` tag | 2 English (`eng`); 3 Chinese Simplified (`chi`, titled); 4 Chinese Traditional (`chi`, titled); 5 Korean (`kor`) | Japanese tag and successful PCM extraction verified; intelligibility/wording still requires actual listening. No Japanese subtitle track located |
| W02 | AAC LC, 44,100 Hz, stereo, `zho` tag | 2 and 3 `zho` (variants untitled); 4 English (`eng`); 5 Korean (`kor`) | Actual spoken language unverified; do not reinterpret a conflicting tag as Japanese. No Japanese text track located |

Language tags are container assertions. Neither English subtitles nor another translation can independently establish exact Japanese wording. Missing Japanese captions do not require a full transcript before any analysis: a verified Japanese listening route can supply brief, source-timed quotations with translation notes. ASR may assist navigation, with uncertainty and original audio retained.

## Production identity checks actually performed

The source-discovery agent viewed sparse first-five-minute and ending contact sheets and then clean full-resolution episode-title frames for W01. The work logo read `ウマ娘 プリティーダービー ROAD TO THE TOP`; ending samples showed production credits. The following requested source seek positions yielded visible Japanese identifiers. Exact selected frame PTS was not measured; these are navigation locators, not fine timing measurements.

| Witness | Requested source position | Visible title |
|---|---:|---|
| E01-W01 | 00:03:35.000 | 第1話 夢のはじまり |
| E02-W01 | 00:03:02.000 | 第2話 栄光の舞台 |
| E03-W01 | 00:03:02.000 | 第3話 走る理由 |
| E04-W01 | 00:03:15.000 | 第4話 想いはひとつ |

These are production identity observations only. Sparse imagery across E01–E04 exposed the source-discovery agent to later-unit pictures; that agent must not later be described as an unexposed prospective reader. No dialogue, motive, race result, motion, performance, music or narrative interpretation was recorded from those samples.

## Executed technical checks and capability limits

For every witness: FFprobe metadata; SHA-256; five seconds of video/audio decode at source 10 s, midpoint, and six seconds before container end; one 96×54 frame at 10 s; one second of native-rate stereo PCM at 10 s; and decoding/counting all four embedded subtitle tracks. Every executed command passed. W01 additionally passed complete video/audio decode using FFmpeg `-xerror`, exit 0 and empty error output. Complete W02 decode was not run. These checks are nondestructive to source files.

FFmpeg and FFprobe 8.1.1 were executed. The existing AV Evidence Toolkit 1.6.0a3 launcher/probe help and `doctor` ran; prerequisites were available. Doctor reported audio/motion/image perception `NOT_VERIFIED`, which accurately does not certify this model's perception. This session inspected still images for identity only; it did not listen or perceive continuous AV.

The default Python lacks faster-whisper. A pre-existing dedicated local runtime successfully resolved/imported faster-whisper 1.2.1, ctranslate2 4.9.0 and av 16.1.0; its cached large-v3 model file exists. No RTTT ASR inference, quality validation, model installation, upload or hosted expenditure occurred. Existing title-specific ASR scripts contain hardcoded neighboring-title paths and are references, not safe RTTT launch commands.

## Admission actions

| Requirement | Actual state | Concrete resolution |
|---|---|---|
| Work and episode identity | Satisfied for all W01 title-card witnesses | Bind the selected W01 hash in the E01 run; preserve disclosed provenance |
| Technical availability | Satisfied for W01 E01–E04 | Rehash only if files may have changed; use tested stream mapping |
| Exact distributor master | Unknown | Disclose this limitation; seek better provenance only if a claim depends on a cut difference |
| Japanese dialogue reliability | Not yet listened to | Verify representative Japanese speech and exact intervals for quotations through an adequate listening route; optional local ASR is an aid |
| Subtitle/AV clock alignment | Unverified | Calibrate early/middle/late anchors for E01, recording measured offsets and residual error |
| Actual AV route | Unverified | Verify CONTINUOUS_AV on the episode or bounded synchronized clips for motion and image–music timing, and verified audio-content inspection for voice-only delivery; queue unsupported channels |
| Run authorization and sequential lock | Bootstrap does not grant either | Follow the [readiness audit](../05_Run_State/UM_RTTT_READINESS_AUDIT.md) and [E01 plan](../05_Run_State/UM_RTTT_E01_NEXT_RUN.md) |

No fresh acquisition is presently necessary merely to start E01 readiness QA. Acquire a replacement only for a demonstrated source deficiency. Do not download unauthorized copies or circumvent DRM. No complete Japanese transcript or full-episode upload is an automatic gate.

## Retained receipts

- `PRIVATE_SOURCE_RECEIPT.json` SHA-256 `d5ef2b2bd464f78bebc5bef72f284c52b2fa100a4b3d330b92f3fdb460a0f41d`: actual paths, original hashes, probes, decode/extraction results.
- `PRIVATE_SOURCE_SUPPLEMENT.json` SHA-256 `8a95a529a24817c9ed39101f7efe960c03d9287c982dd7b73204d89d58b9a725`: viewed title-card identities, subtitle technical extraction, observed runtime availability and exposure declaration.

Raw sources, copyrighted subtitles, frames and audio stay external. Later source changes get a new witness ID and receipt; never overwrite an earlier binding. A future 2023/2024 comparison requires separate admitted witnesses and an explicit interval crosswalk, not a numbering assumption.
