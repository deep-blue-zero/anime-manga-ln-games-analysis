---
title: "To Be Hero X V2 — Phase 0 Source Lock and Locator Control"
series: "To Be Hero X"
version: "2.1"
phase: 0
status: "conditional_corpus_lock_e01_multimodal_verified"
date: "2026-08-14"
primary_language: "Mandarin Chinese"
subtitle_access_language: "Simplified Chinese (zh-Hans)"
---

# Purpose

This document freezes the **Phase 0 source contract** for the V2 deep reading of *To Be Hero X*. It defines what the project may treat as primary evidence, how time and dialogue are to be located, what has been validated, what remains an access exception, and what must be reverified before a claim can become quotation-grade.

This lock remains **corpus-conditionally closed**, but the reason has changed. Direct inspection of the attached Library copy of `BHX_s01e01_screenshots.zip` proves that the files named `BHX_s01e##_screenshots.zip` are **complete analytical episode bundles**, not screenshot-only archives. Episode 1 contains Mandarin complete audio, reconstructed Chinese subtitles, paired Chinese/Japanese subtitles, contact sheets, dense screenshots, dialogue/scene indexes, and metadata inside the ZIP. The remaining corpus-level condition is **Library enumeration/addressability**: File Library search does not currently surface the ZIP binaries by exact filename, so E02–E24 cannot yet be individually opened and checksum-verified from this chat even though the user reports that all 24 have been uploaded to the project Library.

# 1. Corpus identity

- Title: **To Be Hero X**
- Season: **1**
- Episode count: **24**
- Spoken language: **Mandarin Chinese**
- Principal subtitle/access layer: **Simplified Chinese (`zh-Hans`)**
- Source policy in extraction manifest: **read-only**
- Total source duration: **10.304 hours**
- Accepted reconstructed Chinese subtitle cues: **6,578**
- Screenshots: **25,439**
- Contact sheets: **1,282**
- Screenshot-archive bytes: **6,970,550,437 bytes** (~6.49 GiB)
- Bundle validation: **PASS — 24/24 episodes passed, 0 errors, 0 warnings**

The current primary-source Drive folder directly exposes `BHX_s01e01_screenshots.zip` through `BHX_s01e24_screenshots.zip`. Despite the filename suffix, direct inspection of the attached Episode 1 copy establishes that these are **self-contained episode-analysis bundles**. The analytical root separately exposes the extraction metadata under `Anime bundle metadata`.

# 2. Source-authority hierarchy

For V2, evidence authority is frozen as follows:

1. **Mandarin program audio** — governing source for spoken wording, delivery, hesitation, interruption, paralinguistic information, and voice performance.
2. **Visible Chinese hardsubs / verified reconstructed zh-Hans ASS** — governing written access layer for dialogue transcription and cue indexing, subject to manual verification when wording matters.
3. **Program frames / screenshot sequences** — governing source for composition, gesture, staging, on-screen text, visual causality, editing, and animation-form claims.
4. **Japanese aligned subtitle reference** — semantic/timing witness only. It may expose ambiguity or reconstruction errors but may not override Mandarin wording, register, pronoun behavior, particles, or voice.
5. **Mandarin Whisper ASR** — diagnostic witness only; never a governing transcript.
6. **V1 analysis** — historical hypothesis source only; never primary evidence.

No downstream synthesis may silently promote a lower-tier witness over a higher-tier source.

# 3. Reconstruction and validation state

The subtitle reconstruction report states the method as:

> 8 Hz hardsub boundary detection plus PP-OCRv5 recognition, semantically checked against Japanese captions and non-authoritative Whisper Mandarin ASR.

The validated corpus contains **6,578 accepted events**, **4 retained low-confidence events**, and a **weighted mean OCR confidence of 0.99236**.

The four retained low-confidence episodes are:

- E07 — one event; episode minimum OCR confidence 0.773176
- E13 — one event; episode minimum OCR confidence 0.838677
- E17 — one event; episode minimum OCR confidence 0.836785
- E24 — one event; episode minimum OCR confidence 0.818342

These episodes carry a mandatory **manual dialogue-verification flag** whenever exact wording, a proper name, modality, negation, or address term materially affects interpretation.

Semantic alignment scores are **cross-language diagnostic signals, not truth scores**. Lower values therefore trigger care rather than automatic distrust. The most alignment-sensitive episodes are E15 (0.781709), E06 (0.783346), E04 (0.788866), E19 (0.789969), and E07 (0.792399).

# 4. Episode source profile

| Ep | Source duration | Program start | Analysis start | CN cues | Mean OCR | Low-conf | Screenshots | Sheets | ZIP size |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 01 | 25:18.058 | 53.500s | 53.250s | 379 | 0.992799 | 0 | 1197 | 60 | 323.1 MiB |
| 02 | 25:18.272 | 53.250s | 53.000s | 307 | 0.993086 | 0 | 1049 | 53 | 279.2 MiB |
| 03 | 25:17.269 | 54.500s | 54.250s | 294 | 0.993971 | 0 | 1014 | 51 | 325.4 MiB |
| 04 | 25:27.253 | 53.000s | 52.750s | 283 | 0.993319 | 0 | 1145 | 58 | 321.6 MiB |
| 05 | 25:27.253 | 59.000s | 58.750s | 338 | 0.992490 | 0 | 890 | 45 | 213.1 MiB |
| 06 | 25:22.261 | 54.500s | 54.250s | 314 | 0.993451 | 0 | 838 | 42 | 214.2 MiB |
| 07 | 25:07.050 | 39.375s | 39.125s | 235 | 0.993644 | 1 | 1145 | 58 | 299.2 MiB |
| 08 | 25:12.000 | 37.500s | 37.250s | 281 | 0.991402 | 0 | 909 | 46 | 288.0 MiB |
| 09 | 26:24.768 | 38.250s | 38.000s | 207 | 0.992870 | 0 | 1014 | 51 | 283.8 MiB |
| 10 | 26:24.725 | 38.000s | 37.750s | 292 | 0.993080 | 0 | 1036 | 52 | 273.9 MiB |
| 11 | 25:17.013 | 47.000s | 46.750s | 288 | 0.990139 | 0 | 1063 | 54 | 302.9 MiB |
| 12 | 25:17.013 | 49.250s | 49.000s | 199 | 0.992653 | 0 | 1358 | 68 | 339.9 MiB |
| 13 | 25:20.000 | 32.250s | 32.000s | 286 | 0.991001 | 1 | 952 | 48 | 243.3 MiB |
| 14 | 25:18.976 | 34.000s | 33.750s | 281 | 0.993599 | 0 | 1186 | 60 | 292.5 MiB |
| 15 | 25:20.768 | 41.750s | 41.500s | 280 | 0.994076 | 0 | 977 | 49 | 229.9 MiB |
| 16 | 25:18.677 | 33.500s | 33.250s | 264 | 0.992338 | 0 | 984 | 50 | 246.0 MiB |
| 17 | 25:17.013 | 46.750s | 46.500s | 274 | 0.987556 | 1 | 958 | 48 | 262.9 MiB |
| 18 | 25:17.013 | 47.500s | 47.250s | 323 | 0.991560 | 0 | 817 | 41 | 197.5 MiB |
| 19 | 25:20.682 | 32.250s | 32.000s | 301 | 0.993487 | 0 | 841 | 43 | 183.0 MiB |
| 20 | 27:21.002 | 47.000s | 46.750s | 191 | 0.993177 | 0 | 1251 | 63 | 258.9 MiB |
| 21 | 27:19.210 | 46.750s | 46.500s | 309 | 0.992312 | 0 | 976 | 49 | 245.8 MiB |
| 22 | 27:19.381 | 51.500s | 51.250s | 164 | 0.991643 | 0 | 1340 | 67 | 300.8 MiB |
| 23 | 27:27.466 | 48.000s | 47.750s | 262 | 0.991391 | 0 | 1183 | 60 | 327.3 MiB |
| 24 | 25:41.674 | 43.750s | 43.500s | 226 | 0.991225 | 1 | 1316 | 66 | 395.5 MiB |

The varying program boundaries are material. V2 must not assume that source time zero equals narrative program time zero.

# 5. Locator contract

Every claim that may later support a specialist synthesis should, where practicable, carry both clocks:

`S01E## | source HH:MM:SS.mmm | program +HH:MM:SS.mmm | CN cue ### | frame/screenshot reference | evidence code`

Definitions:

- **source time** = timestamp on the complete episode extraction timeline;
- **program time** = timestamp relative to the detected program boundary;
- **CN cue** = reconstructed Chinese ASS event number when available;
- **frame reference** = screenshot filename/frame or contact-sheet cell used to navigate to the evidentiary image;
- **evidence code** = `F-DLG`, `F-VIS`, `F-AUD`, `F-MECH`, `F-INST`, `INF`, `INT`, `HYP`, `ALT`, `REV`, or `UNR`.

The first frozen locator for an important claim should retain enough information to re-open the source without searching the episode from scratch.

# 6. Prospective-reading control

Phase 1 proceeds in **broadcast order**. For each episode:

1. write the prospective interpretation using only evidence available through that episode;
2. freeze it;
3. allow later episodes to append retrospective revisions without rewriting the earlier audience-state record.

This control is mandatory because the series repeatedly reorders chronology, revisits public events from private perspectives, and transforms the meaning of earlier scenes.

# 7. Quote-grade dialogue rule

A Mandarin line may be quoted or used for fine-grained linguistic interpretation only when:

- the reconstructed Chinese text is high-confidence or manually checked;
- the Mandarin audio is directly accessible and consistent with the transcription;
- material proper nouns or unusual terms are checked against the visible hardsub where possible;
- Japanese-reference disagreement, when material, is described rather than silently harmonized;
- any low-confidence reconstruction event has been manually resolved.

A line may not be called quote-grade solely from corpus metadata or V1 prose. For an episode whose Library bundle is directly addressable, the embedded Mandarin audio and ASS layers satisfy the source-access requirement. E01 now meets that requirement.

# 8. Drive and Library access-state lock

## Drive state

Drive exposes all 24 `BHX_s01e##_screenshots.zip` archives plus the corpus-level metadata. The Drive connector cannot browse ZIP members in place and rejects raw downloads above its 256 MiB transfer ceiling, so many bundles cannot be inspected directly through Drive despite being stored there.

## Project Library state

The user reports that all 24 `BHX_` episode bundles have been uploaded to the project Library. File Library search, however, does not enumerate the ZIP binaries by exact filename, so corpus-wide binary presence cannot be independently certified through the search surface in this chat. This is an **enumeration/addressability limitation**, not evidence of missing uploads.

## Directly verified attached bundle: E01

`BHX_s01e01_screenshots.zip` was attached to the current conversation and inspected directly. Verification results:

- archive SHA-256: `f6b8c4214248f5f595bd20e2c41824e36189fbe48bc4e578370b4d103e02d776`
- ZIP members: **1,272**
- uncompressed bytes: **350,678,735**
- JPEG members: **1,256**
- contact sheets declared: **60**
- Mandarin complete audio: `audio/s01e01.complete-audio.mp3` — **30,362,612 bytes**, duration **1518.059s**
- reconstructed Chinese subtitle access layer: `subtitles/selected_subtitles.ass`
- paired Mandarin/Japanese reference layer: `subtitles/paired_subtitles.ass`
- metadata/index layer includes `bundle_metadata.json`, `analysis_stats.json`, `dialogue_index.*`, `scene_index.*`, `manifest.*`, and contact-sheet metadata
- E01 Chinese cues: **379**; mean OCR confidence **0.992799**; low-confidence accepted events **0**

The `paired_subtitles.ass` file contains aligned `Japanese_Reference` dialogue events, while `selected_subtitles.ass` contains the reconstructed `Mandarin_Hardsub_Reconstruction` events. Therefore E01 is **full multimodal/quote-grade-source ready** subject to ordinary cue-level verification rules.

## E02–E24 status

E02–E24 remain `USER_REPORTED_LIBRARY_UPLOADED / NOT_YET_DIRECTLY_ADDRESSABLE`. Their expected filenames, metadata, cue counts, screenshot counts, sheet counts, and archive sizes are frozen from the validated manifest. They should be promoted to `DIRECTLY_VERIFIED` when an archive becomes attached/addressable for its episode pass. This does **not** require preloading all 24 into the active workspace simultaneously.

**Readiness consequence:** Phase 1 Episode 1 is now fully open. Later episodes may proceed as soon as their corresponding Library archive is addressable in the working conversation.

# 9. Storage policy

Google Drive remains the durable source repository. ChatGPT working storage should use a rolling episode cache:

- fetch the current episode's minimum working set;
- extract only the screenshot/frame subsets required for close reading;
- retain canonical Markdown analysis and locator ledgers as durable analytical memory;
- evict bulky episode working assets after freeze unless an unresolved claim requires them;
- re-fetch exact source moments later through locators rather than keeping all 24 episodes resident.

This prevents the V2 project from duplicating ~6.5 GiB of screenshot archives plus audio and subtitle assets in the active workspace.

# 10. Phase 0 metadata snapshot hashes

These hashes identify the metadata/V1 snapshot actually used to establish this lock:

| File | SHA-256 |
|---|---|
| `manifest.json` | `c7d55bafa377c33aaa2e55d02a3f4e38edbb5d77a8db222d57ef5b4ee464efb8` |
| `bundle_validation.json` | `bb674d6c2cc61d57e23f458f155ea137324b5d7d102e0aec7e5b5aecc2d7dc5e` |
| `subtitle_reconstruction_report.json` | `176ad2b35cca46c1482f1d0431b13aa9ea698c57c39e03864a599fb3c5356d95` |
| `semantic_subtitle_alignment.json` | `3492a3eebc7b76525267f568a4e9433fbb4e4cf6b1ef455b49b9e327fd102abb` |
| `visual_preroll_detection.json` | `461101965e79831506b7fecec7a4ca6947ec4a75a5ebd209bdae45536624d51d` |
| `suspicious_ocr_refinement_candidates.json` | `1f30b531da475e69275b9a477ea08cfdc767bbacc918b23507076825855d5d84` |
| `To Be Hero X Understanding.txt` | `ab35123ddeab7a222d561c438441f56fa07ea845e0c91f93ca7efcf9fc8e527a` |

The screenshot ZIPs were **not downloaded solely for checksum generation**; the Phase 0 lock identifies them through the Drive folder, episode filename, and manifest-recorded byte size. When an archive is fetched for analysis, its checksum may be added to the episode artifact without requiring global prefetch.

# 11. Lock status

**Phase 0 source lock status: CONDITIONAL CORPUS LOCK / E01 FULLY VERIFIED.**

The corpus identity, validation profile, source hierarchy, temporal locator model, evidence rules, archive semantics, and storage policy are frozen. The prior assumption that the Drive ZIPs were screenshot-only is withdrawn. The remaining condition is operational: E02–E24 are not individually enumerable/addressable through the current File Library search surface. This does not block E01 Phase 1 analysis and does not require redesigning the method.
