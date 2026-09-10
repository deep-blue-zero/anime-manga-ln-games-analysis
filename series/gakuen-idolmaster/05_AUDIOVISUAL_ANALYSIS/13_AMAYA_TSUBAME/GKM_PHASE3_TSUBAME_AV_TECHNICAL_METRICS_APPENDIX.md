---
series: GKM
artifact_type: audit
scope: CHARACTER_AMAYA_TSUBAME_PHASE3_AV_TECHNICAL
character: Amaya Tsubame / 雨夜燕
generation: V2
release: R1
status: canonical
source_boundary: Technical probe, hashes, source-envelope measurements, frame/contact-sheet inspection, and source-class audit for 14 canonical AV objects plus seven supplemental excerpts
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
last_updated: '2026-08-18'
title: GKM Phase 3 — Amaya Tsubame AV Technical Metrics Appendix
---

# GKM PHASE 3 — AMAYA TSUBAME AV TECHNICAL METRICS APPENDIX

## 1. Canonical packet totals

- Canonical logical objects: **14**
- Canonical duration: **14,965.243 seconds / 4.157 hours**
- Canonical size: **1,347,835,563 bytes / 1.348 GB decimal / 1.255 GiB**
- Supplemental duplicate Dear excerpts: **7**
- All materialized duration including duplicates: **17,138.886 seconds / 4.761 hours**
- All materialized size including duplicates: **1,567,933,574 bytes**

The duplicates exist for inspection convenience and are not separate story evidence.

## 2. Encoding profile

All canonical videos are **1280×720**. Most use H.264 at 30 fps. The authored `理論武装して` MV is 24 fps. Audio is AAC-LC 44.1 kHz stereo, predominantly around 128 kbps; the official MV carries a higher-rate track around 256 kbps.

This is adequate for:

- face and broad micro-expression;
- gaze direction;
- posture;
- hand position and gesture;
- scene blocking;
- subtitle/UI reading;
- timing, pause, stammer, and broad voice-performance contrast;
- choreography and virtual-camera analysis.

It is not equivalent to:

- isolated vocal stems;
- lossless master audio;
- full facial-capture data;
- high-resolution frame-by-frame production inspection.

## 3. Source-layout issue

Several uploaded dialogue compilations use a landscape layout with the vertical game frame centered between decorative side panels. The game image remains readable, but the effective horizontal resolution devoted to Live2D acting is lower than the nominal 1280-pixel container width. This was accounted for by using targeted frame extraction and individual high-load clips where available.

The source does not prevent the character-acting conclusions in the canonical baseline.

## 4. Mixed-source audio envelope metrics

The accompanying `audio_envelope_metrics.json` was calculated from complete audio decoded to mono 16 kHz PCM. Statistics include dialogue, BGM, effects, and silence. They are source-engineering descriptors only.

| Source | Global RMS dBFS | 1-second p90–p10 span | Near-silence < −45 dBFS |
|---|---:|---:|---:|
| Dear 000 | −24.51 | 11.25 dB | 2.16% |
| Dear 001–010 | −26.84 | 11.57 dB | 3.59% |
| Dear 011–020 | −23.66 | 10.13 dB | 2.18% |
| Dear 021–027 | −22.53 | 12.50 dB | 2.46% |
| 20 outings | **−40.24** | 8.35 dB | 11.76% |
| `理論武装して` commu | −27.21 | 10.93 dB | 0.84% |
| `クライアイ` commu | −26.96 | 11.29 dB | 1.04% |
| `Campus mode!!` commu | −26.63 | 11.78 dB | 0.77% |
| `クライアイ` 3DMV | −16.77 | 8.05 dB | 5.13% |
| `Campus mode!!` 3DMV | −17.88 | 8.31 dB | 6.21% |
| `理論武装して` official MV | −12.20 | 7.73 dB | 3.27% |
| `理論武装して` 3DMV | −18.21 | 9.53 dB | 5.73% |
| `星南と燕の日常` | −26.36 | 9.65 dB | 1.46% |
| `やっと見つけたぞ！` | −25.43 | 9.56 dB | 0.33% |

The outing compilation is markedly quieter than the rest. It remained usable after non-destructive listening normalization; no character-performance claim depends on comparing its raw loudness with another source.

## 5. Why no numerical “Tsubame pitch profile” is promoted

The sources contain:

- music beds;
- sound effects;
- alternating speakers;
- uploader-side processing;
- no isolated dialogue stems;
- no guaranteed consistent mastering across uploads.

A numerical pitch/timbre profile would therefore create false precision. The voice specialist instead relies on repeated scene-level contrasts corroborated by face/body timing and exact text.

## 6. Frame inspection

Inspection materials created locally include:

- uniform contact sheets for all canonical objects;
- high-density Dear 002, 006, 009, 010, 019, 024, 025–027 sequences;
- 20-second pages for Dear 011–020;
- 15-second pages for Dear 021–027;
- 5-second inspection around the Dear 026 loss and Producer-separation exchange;
- source hashes and ffprobe manifests.

These inspection derivatives are working materials, not independent canonical sources and are not redistributed in the release ZIP unless explicitly listed.

## 7. Integrity

Every materialized source has a SHA-256 entry in `GKM_PHASE3_TSUBAME_AUDIOVISUAL_SOURCE_MANIFEST.json`. The release package contains artifact checksums and a separate ZIP checksum.
