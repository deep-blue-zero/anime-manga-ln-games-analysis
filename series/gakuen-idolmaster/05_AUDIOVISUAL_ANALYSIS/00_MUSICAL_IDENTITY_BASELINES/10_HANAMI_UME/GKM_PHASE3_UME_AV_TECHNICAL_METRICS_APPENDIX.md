---
series: GKM
artifact_type: technical_appendix
scope: CHARACTER_HANAMI_UME_PHASE3_AV_TECHNICAL
character: "Hanami Ume / 花海佑芽"
generation: V2
release: R1
status: canonical
source_boundary: "Technical metadata and source-level audio/visual measurements for the 21-object canonical Ume AV packet"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
last_updated: "2026-08-19"
title: "Hanami Ume Phase-3 AV Technical Metrics Appendix"
---

# GKM PHASE 3 — HANAMI UME AV TECHNICAL METRICS APPENDIX

## 1. Packet totals

| measure | value |
|---|---:|
| canonical logical objects | 21 |
| directly materialized objects | 21 |
| total duration | 16,654.163 seconds / 4.626 hours |
| total bytes | 2,097,560,948 |
| total decimal GB | 2.098 |
| Dear coverage | 001–037, complete |
| song communications | 5 |
| rendered performances | 7 |
| authored official MVs | 2 |
| official lyric videos | 1 |
| full-song video assets | 2 |

One 2160p60 `The Rolling Riceball` capture—Drive `12UswhS3XfELuboQMZFtUQzXRu9JwUeRE`, 278,393,133 bytes—was retained as a higher-resolution duplicate. It exceeded the connector raw-fetch limit and was not counted as a separate logical source. The matching 1080p60 performance was materialized and inspected.

## 2. Dear route packets

| source | coverage | duration | resolution/fps | bytes | SHA-256 |
|---|---|---:|---|---:|---|
| AV-UME-014 | Dear 001–010 | 3163.510 s | 1280×720 / 30 | 184,038,040 | `64c08030c37e1b76bfffd3d60a65d14385ae43ee1ddf7d3c9e5b3688c7afcd77` |
| AV-UME-013 | Dear 011–020 | 2506.106 s | 1280×720 / 30 | 251,347,768 | `5b37e792d24be394fa48afb9e7b58e8f13c716216dc9898a349204b36e78fc93` |
| AV-UME-012 | Dear 021–027 | 2938.000 s | 854×480 / 30 | 251,441,094 | `596de087dc949b18f6c8ff7fcba4ac73d1e648e91f1d1a82aaf0171410b65da8` |
| AV-UME-010 | Dear 028–037 | 3335.129 s | 854×480 / 29.97 | 143,300,665 | `f88d7d8104d63d4fa5d73b26268012e0a029cc1b0057fab9a95ea392beec046f` |

The 480p packets are sufficient for pose, expression, timing, and framing analysis but should not be treated as fine-detail costume or texture sources when higher-resolution performance media exists.

## 3. Principal performance and authored sources

| source ID | object | role | duration | resolution/fps | bytes |
|---|---|---|---:|---|---:|
| AV-UME-005 | `The Rolling Riceball` | rendered 3DMV | 157.710 s | 1920×1080 / 60 | 101,092,879 |
| AV-UME-020 | `The Rolling Riceball` | authored official MV | 191.936 s | 1920×1080 / 30 | 57,602,206 |
| AV-UME-006 | `グースーピー` | rendered 3DMV | 184.390 s | 1920×1080 / 60 | 109,654,019 |
| AV-UME-021 | `真っ白いページと水彩の主人公` | authored official MV | 226.139 s | 1920×1080 / 24 | 63,651,409 |
| AV-UME-001 | `Campus mode!!` | rendered 3DMV | 160.961 s | 1920×1080 / 60 | 108,063,101 |
| AV-UME-011 | `つよつよ最強エクササイズ` | official lyric video | 143.639 s | 1920×1080 / 24 | 55,240,460 |
| AV-UME-003 | `GO MY WAY!!` | rendered 3DMV | 143.314 s | 1920×1080 / 60 | 88,076,689 |
| AV-UME-002 | `ENDLESS DANCE` | rendered 3DMV | 109.714 s | 1920×1080 / 60 | 63,655,729 |
| AV-UME-004 | `Howling over the World` | rendered 3DMV | 111.758 s | 1920×1080 / 60 | 70,678,987 |
| AV-UME-007 | `ミラクルナナウ(ﾟ∀ﾟ)！` | rendered 3DMV | 115.334 s | 1920×1080 / 60 | 63,265,728 |

All counted videos use AAC stereo audio at 44.1 kHz. Detailed codec, bitrate, frame-rate, dimensions, hashes, and Drive identifiers live in `GKM_PHASE3_UME_AUDIOVISUAL_SOURCE_MANIFEST.json`.

## 4. Complete-mix audio envelope

Method: mono decodes were summarized in one-second windows. Values describe entire supplied mixes, including BGM, effects, crowd, dialogue, and mastering.

| source | global RMS | median 1 s RMS | P10–P90 dynamic span | near-silence (< -35 dBFS) |
|---|---:|---:|---:|---:|
| Dear 001–010 | -26.89 dBFS | -27.72 | 12.43 dB | 13.18% |
| Dear 011–020 | -21.66 dBFS | -22.24 | 11.37 dB | 4.79% |
| Dear 021–027 | -24.29 dBFS | -25.14 | 12.87 dB | 7.39% |
| Dear 028–037 | -23.45 dBFS | -24.90 | 13.18 dB | 6.72% |
| `The Rolling Riceball` 3DMV | -16.05 dBFS | -15.67 | 7.30 dB | 6.37% |
| `グースーピー` 3DMV | -15.50 dBFS | -14.88 | 12.96 dB | 7.07% |
| `Campus mode!!` 3DMV | -16.10 dBFS | -15.88 | 8.41 dB | 6.88% |
| `GO MY WAY!!` 3DMV | -14.65 dBFS | -14.16 | 10.88 dB | 6.29% |
| White Page official MV | -8.81 dBFS | -8.49 | 2.47 dB | 1.77% |
| `つよつよ最強エクササイズ` full asset | -9.36 dBFS | -8.90 | 5.59 dB | 1.09% |

These values demonstrate source/master differences and help identify corrupted or anomalous files. They are not evidence of isolated vocal intensity.

## 5. Song-mix descriptors

Automated tempo and chroma estimates are approximate. Arrangement, double-time/half-time interpretation, effects, and source edits can alter results.

| source | tempo estimate | median spectral centroid | median rolloff 85% | dominant mean chroma class |
|---|---:|---:|---:|---|
| Rolling 3DMV | 93.75 BPM | 2211 Hz | 4383 Hz | F |
| Goose 3DMV | 133.93 BPM | 2326 Hz | 4703 Hz | G# |
| Campus 3DMV | 93.75 BPM | 2240 Hz | 4570 Hz | B |
| GO MY WAY 3DMV | 117.19 BPM | 2250 Hz | 4594 Hz | E |
| Tsuyotsuyo full | 133.93 BPM | 2532 Hz | 5000 Hz | C# |
| Rolling official MV | 93.75 BPM | 2422 Hz | 4656 Hz | F |
| White Page official MV | 104.17 BPM | 2037 Hz | 4227 Hz | C# |

Do not cite chroma classes as authoritative musical keys.

## 6. Selected visual envelopes

Method: low-resolution 2 fps HSV, grayscale-frame-difference, and color-histogram summaries. The values include edit and stage design as well as performer motion.

| source | mean value | mean saturation | dark-pixel fraction | mean frame difference | high-transition fraction |
|---|---:|---:|---:|---:|---:|
| Campus 3DMV | 85.85 | 116.37 | 0.402 | 32.44 | 0.312 |
| ENDLESS DANCE 3DMV | 66.72 | 114.97 | 0.533 | 33.86 | 0.422 |
| GO MY WAY 3DMV | 108.31 | 98.14 | 0.367 | 41.98 | 0.325 |
| Howling 3DMV | 82.21 | 114.60 | 0.437 | 33.72 | 0.387 |
| Rolling 3DMV | 81.80 | 127.28 | 0.484 | 36.12 | 0.248 |

Only five sources were processed under this computational visual envelope because exhaustive low-level decoding proved disproportionately expensive relative to analytical value. All principal sources were still directly inspected through full playback, targeted frame sampling, and contact sheets.

## 7. Inspection and provenance limits

- No isolated dialogue or singing stems were available.
- Exact speech wording comes from Source Lock, not automated transcription.
- Audio metrics describe source mixes, not performer physiology.
- Rendered 3DMVs are evidence of official game presentation, not documentary records of a physical live.
- Authored MVs are symbolic/paratextual readings, not literal story chronology.
- The 2160p Rolling duplicate is preserved but not counted.
- `グースーピー` re-authorship lacks a separately rendered late comparator.
- P1/P2 nonblocking breadth remains incomplete by design.
