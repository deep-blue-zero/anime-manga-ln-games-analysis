---
series: "THE IDOLM@STER CINDERELLA GIRLS"
year: 2015
artifact_type: "source_lock_and_inventory"
status: "backfill_reconciled_through_E26"
mainline_scope: "E01-E25"
supplementary_scope: "E26 Extra / epilogue-paratext"
created_for: "Google Drive backfill and archival recovery"
---

# CG2015 Source Lock and Inventory — E01-E26

## Purpose

This document records the recoverable source architecture used for the 2015 anime deep reading. It is a provenance artifact, not a redistribution of copyrighted audiovisual material.

The analytical Drive mirror intentionally stores methods, source metadata, source-lock notes, analytical artifacts, ledgers, and audit packages. It does **not** mirror the episode video/audio/screenshot source payloads themselves.

## Governing source pipeline

The File Library source manifest identifies a 26-item `THE_IDOLM@STER_CINDERELLA_GIRLS` analysis corpus produced from the user-managed media-extraction pipeline. For Episodes 01-25, the governing dialogue layer is Japanese Hulu subtitle material retimed to VCB-Studio Blu-ray video/audio sources. The selected program-audio stream is the Japanese main audio; audio commentary is excluded from the analysis bundles.

The timing audit reports fixed source-leader corrections rather than progressive drift:

- E01-E11 and E13-E25: **+0.98 s** subtitle correction.
- E12: **+0.82 s** subtitle correction.
- E26 Extra: **0.00 s**, using the user-specified Nemuri special with embedded **English** amatsuka subtitles because no matching Japanese subtitle was available for the VCB-Studio E26 source.
- Audio-envelope checks were performed at early, middle, and late positions; the report records no progressive drift or mid-episode edit and states that most correlations were approximately 0.98-1.00, with minimum observed correlation 0.871.

For E26, Japanese program audio remains primary for timing, vocal performance, music, silence, and scene transitions. The English subtitle is a semantic/navigation aid and is not treated as quotation-grade Japanese evidence.

## Primary analytical evidence hierarchy

1. Japanese dialogue and program audio where available.
2. Complete visual staging: retained frames, subtitle-linked frames, shot-change frames, contact sheets, silent sequences, blocking, architecture, costume, props, and performance staging.
3. Episode chronology and sealed spoiler horizon.
4. Earlier-established recurrence patterns.
5. Later episodes only during explicitly retrospective synthesis.
6. External franchise or critical material only after the independent close read.

## Episode-bundle identity safeguards

Several identically named archives from other anime coexist in storage. Filename alone is therefore insufficient evidence of source identity.

Known collisions:

- E11: `ep11_screenshots(2).zip` = **Cinderella Girls E11**; `ep11_screenshots(1).zip` = *Lycoris Recoil* E11; unnumbered `ep11_screenshots.zip` = *IDOLY PRIDE* E11.
- E12: `ep12_screenshots(2).zip` = **Cinderella Girls E12**; unnumbered `ep12_screenshots.zip` = *IDOLY PRIDE* E12.
- E13: `ep13_screenshots(1).zip` = **Cinderella Girls E13**; unnumbered `ep13_screenshots.zip` = *Lycoris Recoil* E13.
- E14-E26 unnumbered bundles were independently verified as Cinderella Girls before sequential analysis.

Source identity must be established from internal paths/show metadata and source fingerprints rather than filename inference.

## Later-episode frozen source fingerprints retained by the project

These fingerprints were recorded during the sequential v2 pass and are retained here as provenance anchors:

- E14: SHA-256 `e72c7f79374c2c2745d4d07e5adc5963d9d740b9d3adee77c6bbf5def064f755`
- E15: SHA-256 `8ba2220ef91c6fb6634fd1a49bbcca67e47f044a19dd21a9ff9c0c0975d95546`
- E16: SHA-256 `634468adaf57acdea457347bb8030312f959f71f7c6874bfb3917f7bbe221fe3`
- E17: SHA-256 `8ba838a0a99d0c30f112e7440da18eb685f25884b918fbe2b4c172ef51bff4da`
- E18: inventory fingerprint begins `8faa9b7842ae`; full lock is preserved in the E18 analytical package where generated.
- E19: inventory fingerprint begins `febc61e5aa7b`; full sequential lock was validated during E19 analysis.
- E20: SHA-256 `6a741d497212a8040a850967be345842db1ceacfc0ad7755a33399387f2ed51c`
- E21: SHA-256 `4ac9fab3a9d810c03e4e1ceda9216f7550e8c81407099c44b1ba86b54af236c0`
- E22: SHA-256 `5a6b27f5358a7c91fe196b0d2f9b67eb81a0cdf589cbd2f98e1aeb21a880577a`
- E23: SHA-256 `7c4fb428ea9d3c4826f86490cacd598d607e1f089be769a296cda2afd7e00d5a`
- E24: SHA-256 `fbbacc27e0efedf0b5f8d1106ab069b4e3badb805493f1d33dd584579377dd90`
- E25: SHA-256 `ec019281106cab882572f989c10250ed1b892a50206a1ee9d12dddeced72dd6a`
- E26: SHA-256 `430705cf8a4ec0ddf6aba1fb11fb4f189ef2ea10021655619ef4de2affa3b564`

## E26 dedicated lock

`CG2015_EP26_SOURCE_LOCK.txt` is stored beside this inventory in `01 Source Lock and Inventory`. It records the special's independent bundle verification, including the English-subtitle caveat.

## Copyright/storage boundary

This Drive tree is an **analytical mirror**, not a media mirror. Episode MKVs, extracted audio, screenshots/contact sheets, and source archives remain outside this analytical Drive tree. Their provenance is represented by manifests, source locks, hashes, locators, and analytical packages rather than by redistributing the source payloads.

## Source evidence used for this backfill

- File Library `manifest.json` for `THE_IDOLM@STER CINDERELLA GIRLS`, latest inspected copy dated 2026-08-12.
- File Library `subtitle_timing_report.json`, latest inspected copy dated 2026-08-12.
- Per-episode source locks embedded in the sequential v2 analytical artifacts and packages.
- `CG2015_EP26_SOURCE_LOCK.txt` for the supplementary special.
