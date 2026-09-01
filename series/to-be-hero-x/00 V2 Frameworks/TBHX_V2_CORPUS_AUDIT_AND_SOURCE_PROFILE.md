---
title: "To Be Hero X V2 — Corpus Audit and Source Profile"
project: "To Be Hero X V2"
artifact_type: "corpus_audit"
version: "1.0"
created: "2026-08-13"
status: "reference"
primary_spoken_language: "Mandarin Chinese"
primary_subtitle_script: "Simplified Chinese (zh-Hans)"
spoiler_scope: "Season 1, Episodes 1-24"
source_drive_folder_id: "11D1wSxD5OsF3MgRzHuTw9rUZlTHtpVME"
analysis_drive_folder_id: "1pD8ayXzaZpwX4td3Dl559bgm3z-oUSSs"
---

# To Be Hero X V2 — Corpus Audit and Source Profile

## 1. Purpose

This document records the source state that should govern the V2 deep reading before any new interpretive claims are made. It is intentionally descriptive rather than thematic. Its job is to establish what evidence exists, how it was generated, which layers are authoritative, and where the corpus requires additional verification.

The V2 project is designed around the **Mandarin Chinese performance as the primary linguistic object**. The Codex-generated Simplified Chinese subtitle track is a high-quality access and indexing layer reconstructed from the visible Chinese hardsubs and checked against Japanese subtitle references and non-authoritative Mandarin ASR. It is not treated as an independent replacement for the spoken audio.

## 2. Audited Drive locations

- Primary-source folder: `11D1wSxD5OsF3MgRzHuTw9rUZlTHtpVME`
- Analytical-material root: `1pD8ayXzaZpwX4td3Dl559bgm3z-oUSSs`
- Existing metadata folder: `Anime bundle metadata`

At the time of the original audit, the primary-source folder exposed 24 archives named `BHX_s01e01_screenshots.zip` through `BHX_s01e24_screenshots.zip`. **Phase 0 revision (2026-08-14): direct inspection of the attached E01 archive proves that the `screenshots.zip` naming is misleading; the archive is a complete analytical episode bundle containing Mandarin audio, reconstructed Chinese subtitles, paired Japanese-reference subtitles, contact sheets, dense screenshots, indexes, and metadata.** Drive itself cannot browse ZIP members in place, and its raw-download ceiling blocks many archives, so Library attachment/addressability is the preferred analysis path. The user reports all 24 bundles uploaded to the project Library, but File Library search does not currently enumerate the ZIP binaries by exact filename; E01 is directly verified, while E02–E24 remain pending direct addressability rather than pending source creation.

## 3. Corpus-level metadata findings

- Series title: **To Be Hero X**
- Season: **1**
- Episode count: **24**
- Primary spoken language: **Mandarin Chinese**
- Reconstructed subtitle language: **Simplified Chinese / `zh-Hans`**
- Source policy in manifest: **read-only**
- Total source duration represented: **10.30 hours**
- Bundle validation: **24/24 episodes pass**
- Validation errors: **0**
- Validation warnings: **0**
- Total reconstructed Chinese subtitle cues: **6,578**
- Total individual screenshots: **25,439**
- Total contact sheets: **1,282**
- Total screenshot-archive payload represented by manifest: **6.97 GB**
- Accepted reconstructed subtitle events: **6,578**
- Retained low-confidence subtitle events: **4**
- Weighted mean OCR confidence: **0.99236**
- Total semantic alignment anchors: **1,674**
- Mean per-episode semantic-anchor similarity: **0.8007**
- Program/preroll boundary range: **32.25–59.00 seconds into the source files**

The subtitle-reconstruction report describes the method as **8 Hz hardsub boundary detection plus PP-OCRv5 recognition, semantically checked against Japanese captions and non-authoritative Whisper Mandarin ASR**. This is a strong triangulation pipeline, but its components are not interchangeable evidence sources.

## 4. Episode metadata table

| Ep. | Source min | Program start s | CN cues | OCR mean | OCR min | Semantic anchors | Anchor sim. | Screens | Sheets | Archive MB | Rejected candidates | Low-conf. retained |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 01 | 25.30 | 53.50 | 379 | 0.9928 | 0.8877 | 99 | 0.8022 | 1197 | 60 | 338.8 | 7 | 0 |
| 02 | 25.30 | 53.25 | 307 | 0.9931 | 0.9016 | 74 | 0.8007 | 1049 | 53 | 292.7 | 15 | 0 |
| 03 | 25.29 | 54.50 | 294 | 0.9940 | 0.9140 | 63 | 0.8092 | 1014 | 51 | 341.2 | 29 | 0 |
| 04 | 25.45 | 53.00 | 283 | 0.9933 | 0.9128 | 77 | 0.7889 | 1145 | 58 | 337.3 | 14 | 0 |
| 05 | 25.45 | 59.00 | 338 | 0.9925 | 0.8883 | 78 | 0.7939 | 890 | 45 | 223.5 | 5 | 0 |
| 06 | 25.37 | 54.50 | 314 | 0.9935 | 0.8854 | 72 | 0.7833 | 838 | 42 | 224.6 | 8 | 0 |
| 07 | 25.12 | 39.38 | 235 | 0.9936 | 0.7732 | 73 | 0.7924 | 1145 | 58 | 313.8 | 10 | 1 |
| 08 | 25.20 | 37.50 | 281 | 0.9914 | 0.9197 | 84 | 0.8022 | 909 | 46 | 302.0 | 5 | 0 |
| 09 | 26.41 | 38.25 | 207 | 0.9929 | 0.8523 | 52 | 0.8168 | 1014 | 51 | 297.6 | 2 | 0 |
| 10 | 26.41 | 38.00 | 292 | 0.9931 | 0.8932 | 74 | 0.7995 | 1036 | 52 | 287.2 | 1 | 0 |
| 11 | 25.28 | 47.00 | 288 | 0.9901 | 0.9028 | 85 | 0.7995 | 1063 | 54 | 317.6 | 9 | 0 |
| 12 | 25.28 | 49.25 | 199 | 0.9927 | 0.9255 | 51 | 0.7968 | 1358 | 68 | 356.4 | 9 | 0 |
| 13 | 25.33 | 32.25 | 286 | 0.9910 | 0.8387 | 87 | 0.8104 | 952 | 48 | 255.2 | 2 | 1 |
| 14 | 25.32 | 34.00 | 281 | 0.9936 | 0.9321 | 65 | 0.8017 | 1186 | 60 | 306.7 | 4 | 0 |
| 15 | 25.35 | 41.75 | 280 | 0.9941 | 0.8968 | 63 | 0.7817 | 977 | 49 | 241.1 | 6 | 0 |
| 16 | 25.31 | 33.50 | 264 | 0.9923 | 0.8619 | 83 | 0.7992 | 984 | 50 | 257.9 | 10 | 0 |
| 17 | 25.28 | 46.75 | 274 | 0.9876 | 0.8368 | 58 | 0.8280 | 958 | 48 | 275.6 | 24 | 1 |
| 18 | 25.28 | 47.50 | 323 | 0.9916 | 0.9063 | 74 | 0.7970 | 817 | 41 | 207.1 | 15 | 0 |
| 19 | 25.34 | 32.25 | 301 | 0.9935 | 0.9004 | 82 | 0.7900 | 841 | 43 | 191.9 | 9 | 0 |
| 20 | 27.35 | 47.00 | 191 | 0.9932 | 0.9011 | 54 | 0.8044 | 1251 | 63 | 271.4 | 12 | 0 |
| 21 | 27.32 | 46.75 | 309 | 0.9923 | 0.9306 | 61 | 0.8140 | 976 | 49 | 257.7 | 11 | 0 |
| 22 | 27.32 | 51.50 | 164 | 0.9916 | 0.9364 | 37 | 0.7968 | 1340 | 67 | 315.4 | 4 | 0 |
| 23 | 27.46 | 48.00 | 262 | 0.9914 | 0.9011 | 48 | 0.7943 | 1183 | 60 | 343.2 | 20 | 0 |
| 24 | 25.69 | 43.75 | 226 | 0.9912 | 0.8183 | 80 | 0.8137 | 1316 | 66 | 414.7 | 14 | 1 |

## 5. Reliability interpretation

### 5.1 Reconstructed Chinese subtitle track

The reconstruction quality is unusually high at the corpus level: only four accepted events are marked low-confidence, occurring in Episodes **7, 13, 17, 24**. This supports using the reconstructed ASS files as the default reading/indexing layer.

It does **not** support treating every reconstructed glyph as quotation-grade without review. Any argument that turns on:

- a single lexical choice;
- a proper name or title;
- negation;
- a modal such as obligation, possibility, or permission;
- a pronoun or relationship term;
- an insult or evaluative adjective;
- a slogan, legal/institutional formulation, ranking statement, or Trust/Fear mechanic;
- or a line that appears to contradict visual action

must be checked against the Mandarin audio and visible hardsub evidence. The four retained low-confidence cues are mandatory review points even if they are not central to the episode.

### 5.2 Episodes requiring extra linguistic caution

The retained low-confidence events occur in Episodes 7, 13, 17, and 24. Episode 17 also has the lowest episode-level mean OCR confidence in the manifest, though it remains high in absolute terms. These episodes receive a mandatory dialogue-audit flag.

The lowest semantic-anchor similarities are:

- Episode 15: `0.7817`
- Episode 6: `0.7833`
- Episode 4: `0.7889`
- Episode 19: `0.7900`
- Episode 7: `0.7924`

The semantic score is **not a truth score or translation-quality score**. It measures the alignment behavior of the Japanese-reference cross-check. Low values therefore signal that translation-dependent interpretation deserves extra attention, not that the Chinese reconstruction is necessarily wrong. Episodes 15 and 6 are particularly important under this rule because they have the two lowest mean anchor similarities.

The largest numbers of rejected OCR candidate events occur in:

- Episode 3: 29 rejected candidates
- Episode 17: 24 rejected candidates
- Episode 23: 20 rejected candidates
- Episode 18: 15 rejected candidates
- Episode 2: 15 rejected candidates

Rejected candidates are pipeline cleanup, not automatically missing dialogue. They should only be investigated when scene continuity or the audio suggests an omitted hardsub line.

### 5.3 Visual layer

The screenshot corpus is dense enough for shot-by-shot reconstruction rather than contact-sheet-only inference. Contact sheets are reconnaissance tools. Individual frames, and where necessary adjacent-frame sequences, are the evidence layer.

Screenshot density varies considerably by episode. This should not be interpreted as a measure of narrative importance. It may reflect cut frequency, extraction heuristics, animation density, or longer sequences needing more retained frames.

### 5.4 Preroll and timecode policy

The source files include variable preroll before the detected program boundary. Visual analysis therefore begins at the per-episode detected program boundary, while complete audio retains the source timeline.

Every locator in the V2 corpus should record **both**:

1. `source_time` — timestamp in the original source/extracted audio; and
2. `program_time` — timestamp relative to the detected program start.

This prevents later confusion when comparing subtitles, screenshots, audio, and external copies with different preroll handling.

## 6. Evidence hierarchy to carry into V2

### Tier A — governing primary evidence

1. Mandarin Chinese source audio for spoken wording, delivery, pauses, emphasis, voice quality, and paralinguistic evidence.
2. Original video-derived imagery / individual screenshots for visual fact, composition, on-screen text, gesture, editing, color, and formal evidence.
3. Visible Chinese hardsubs as the strongest textual witness to intended written Chinese dialogue where they can be inspected directly.

### Tier B — high-quality derived access layer

4. Reconstructed Simplified-Chinese ASS generated from hardsub OCR. Use for navigation, indexing, quotation search, and ordinary dialogue reading. Re-verify high-stakes wording.

### Tier C — cross-check and disambiguation layers

5. Japanese aligned subtitles. Useful for semantic triangulation and timing, but **not authoritative for Mandarin register, syntax, word choice, relationship language, or ambiguity**.
6. Mandarin ASR transcript. Useful as an independent acoustic hypothesis when OCR is unclear, but explicitly non-authoritative.

### Tier D — secondary/historical analysis

7. Existing V1 *To Be Hero X* analysis. Valuable as a hypothesis bank and revision target, never as primary evidence.
8. External interviews, official production notes, websites, or secondary criticism, only when deliberately introduced and labeled as external context.

## 7. Source-lock requirements before Episode 1

Before the first V2 episode deep reading is considered canonical, Phase 0 should verify:

- direct addressability of each episode bundle in the project Library (the bundle itself contains Mandarin complete audio and the reconstructed Chinese/Japanese subtitle layers);
- direct verification of the embedded audio/subtitle schema when each episode is first opened;
- direct retrievability of the aligned Japanese reference subtitle where retained;
- stable mapping between screenshot archive and episode number;
- SHA-256 or provider-level identity for all archived source assets if available;
- the program-start offset for each episode;
- the four low-confidence reconstructed cues;
- any subtitle line with unresolved OCR-refinement alternatives;
- and a canonical source-locator convention.

If an asset is temporarily unavailable, the episode may be inspected provisionally but should not be frozen as a V2 canonical reading until the missing evidence stream is restored or the limitation is recorded.

## 8. Bottom-line assessment

The episode metadata supports proceeding with a V2 deep reading. The corpus is much stronger for linguistic analysis than a normal fan-subtitle workflow because it preserves three partially independent witnesses to dialogue: **Mandarin audio, Chinese hardsub reconstruction, and Japanese semantic reference**, with ASR available as a fourth diagnostic layer. The visual archive is also sufficiently dense for formal analysis.

The main methodological danger is therefore not source scarcity. It is **overconfidence in derived text** and **retrospective overfitting**. V2 should exploit the precision of the corpus while keeping the Mandarin performance authoritative, preserving broadcast-order uncertainty, and forcing later revelations to revise earlier claims explicitly rather than silently rewriting them.
