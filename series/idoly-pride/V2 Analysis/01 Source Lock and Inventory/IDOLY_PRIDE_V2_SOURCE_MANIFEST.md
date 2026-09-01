---
title: "IDOLY PRIDE V2 Source Manifest"
project: "IDOLY PRIDE"
document_id: "IDOLY_PRIDE_V2_SOURCE_MANIFEST"
version: "1.0"
status: "phase-0-source-lock"
source_snapshot_id: "IP-V2-SNAPSHOT-2026-08-13-A"
source_cutoff: "2026-08-13"
created: "2026-08-13"
updated: "2026-08-13"
framework_version: "2.1"
---

# IDOLY PRIDE V2 SOURCE MANIFEST

## 1. Purpose

This document freezes the initial source state for the IDOLY PRIDE V2 analytical project.

The project is a live-corpus analysis. This manifest therefore describes a dated source snapshot, not a claim that IDOLY PRIDE has permanently ceased publication. Material released or extracted after this snapshot enters the rolling source-delta workflow defined by the V2 frameworks.

Canonical initial snapshot identifier:

`IP-V2-SNAPSHOT-2026-08-13-A`

The governing distinction is:

- source/data storage: primary and derived source material;
- analytical workspace: V2 ledgers, syntheses, audits, and releases;
- frozen release: an immutable analytical package tied to a dated source cutoff.

## 2. Source roots

### 2.1 Game source/data root

Google Drive folder:

`../../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-8c77f28b025f09ed`

Direct children at source lock:

| Layer | Drive ID | Role |
|---|---|---|
| `analysis_bundles` | `1YXaSvw-cxmo4Ud8i6GpJ-X5rkKnjvKMU` | Default LLM analytical reading layer |
| `idoly-ingest` | `1Ow24RCbzh0u664cXy2pKz6jjVKCg847h` | Provenance and exact-context retrieval layer |
| `idoly-ingest-selected-events-core-important` | `1nlzx67folaG2xYpieCCbYbxKlB47tIxr` | Historical triage/preselection aid only |
| `idoly-visual-assets` | `1_aFrIISPJMDGwOTtDY1PhE-hWAsq5Tgc` | Card art, key visuals, photos, and other visual evidence |
| `4koma_archive` | `1r-7cRgIS0S93YbgdHQ6EbolOst6mcAAQ` | Official 4koma archival layer |

Primary-source files remain outside the V2 analysis tree.

### 2.2 Analysis artifact root

V2 analysis folder:

`..`

Phase 0 output folder:

`01 Source Lock and Inventory`

Drive ID: `1qrpj7ZOUOgXVpwMOXK8nfXjbyYJce3GT`

## 3. Game corpus snapshot

The current `idoly-corpus` incremental refresh recorded in `idoly-ingest/_meta/source_snapshot.json` is:

- latest incremental refresh: `2026-08-13T20:13:01+00:00`;
- ingest snapshot generated: `2026-08-13T20:24:41+00:00`;
- source story folders represented in ingest: 3,879;
- derived ingest bundles: 665.

Underlying corpus counts recorded by the source snapshot:

| Corpus component | Count |
|---|---:|
| Story metadata records | 2,067 |
| Bond stories | 160 |
| Card story parts | 1,089 |
| Card story stems | 363 |
| Unique transcript asset IDs discovered | 2,120 |
| Transcript JSON assets cached | 2,088 |
| Normalized story scripts | 2,067 |
| Normalized story utterances | 173,316 |
| Story scripts with no ADV lines | 11 |
| Message groups | 45 |
| Message threads | 1,812 |
| Normalized message lines/items | 44,370 |
| Telephone references | 256 |
| Telephone audio files cached | 211 |
| Approximate telephone ASR transcripts | 211 |

The game corpus is derived from the INFO PRIDE backends through an extraction/normalization pipeline. For ordinary narrative text, the important provenance model is:

`game data -> extracted/normalized corpus -> idoly-ingest -> analysis_bundles`

The dialogue is not treated as a fan-authored summary merely because INFO PRIDE is fan-maintained infrastructure.

## 4. Game analytical reading layer

`analysis_bundles` is the default reading interface.

Its documented structure includes:

- `00_shared`: complete main, unit-origin, and special-story context;
- `characters`: category slices, chronological/category omnibuses, telephone bundles, raw scene indexes, and coverage reports;
- `story_events`, `card_stories`, `bond_stories`, `messages`: grouped full-scene compilations;
- `indices`: character-to-scene and co-occurrence navigation;
- `reports`: validation, coverage, missing assets, and telephone status.

Transformation policy recorded by the bundle README:

- display wrapping is removed for analysis;
- raw title/section values and granular source paths are retained;
- dialogue punctuation is otherwise untouched;
- raw `{user}` placeholders are retained;
- player choices are labeled `Manager (player)`;
- all choice branches are included.

## 5. Game provenance/backstop layer

`idoly-ingest` is the exact-context and provenance backstop.

Use it when:

- a direct quotation is required;
- exact surrounding dialogue matters;
- scene boundaries or ordering are ambiguous;
- source metadata or speaker attribution requires confirmation;
- an omnibus hides relevant setup or payoff;
- a contradiction appears;
- a load-bearing claim needs a canonical locator.

The ingest tree includes main story, unit origins, events, cards, specials/miscellaneous, bond stories, messages, character indexes, relationship indexes, and source maps.

## 6. Historical selected-events layer

`idoly-ingest-selected-events-core-important` is retained for historical provenance and discovery.

It is not the V2 authority on analytical importance.

V2 importance is determined by the Corpus Coverage and Priority Ledger after broad corpus reconnaissance. Historical selections can be confirmed, weakened, superseded, or ignored when the new ledger supports a different priority model.

## 7. Visual source layer

`idoly-visual-assets/resized` contains at least the following source classes at lock time:

- `cards`;
- `key_visuals`;
- `photos`.

These materials may establish visible facts, recurring visual motifs, costume/design evidence, public-image construction, and card-specific body language. They must not be used to invent narrative claims unsupported by either the visible evidence or the text.

## 8. Official 4koma source layer

The official 4koma archive is generated from a source manifest dated 2026-08-09.

Locked counts:

| Series | Images |
|---|---:|
| Main 4koma | 113 |
| Back STAGE | 20 |
| First Step Extra | 1 |
| Aipura Bside | 11 |
| Aipura Bside Specials | 6 |
| **Total** | **151** |

The archive download manifest preserves source URLs, byte sizes, and SHA-256 hashes for the individual source images.

Analytical weight: supplementary characterization, social texture, visual comedy, editorial emphasis, and recurring motifs. It is not automatically equivalent in dramatic weight to main story or major event narratives.

## 9. Anime audiovisual snapshot

The anime source lock consists of all twelve TV episodes in analysis-bundle ZIP form as supplied in the current project conversation:

- `ep01_screenshots.zip`
- `ep02_screenshots.zip`
- `ep03_screenshots.zip`
- `ep04_screenshots.zip`
- `ep05_screenshots.zip`
- `ep06_screenshots.zip`
- `ep07_screenshots.zip`
- `ep08_screenshots.zip`
- `ep09_screenshots.zip`
- `ep10_screenshots.zip`
- `ep11_screenshots.zip`
- `ep12_screenshots.zip`

The extraction manifest identifies the source set as the 12-episode IDOLY PRIDE Blu-ray release, Japanese FLAC audio, and sidecar ASS subtitles. The analysis bundles contain screenshots, contact sheets, subtitle material, and bundled complete-audio MP3 files.

Aggregate locked visual extraction counts:

- screenshots: 9,052;
- contact sheets: 458;
- episodes represented: 12/12.

Per-episode visual counts:

| Episode | Screenshots | Contact sheets |
|---:|---:|---:|
| 01 | 727 | 37 |
| 02 | 749 | 38 |
| 03 | 752 | 38 |
| 04 | 754 | 38 |
| 05 | 700 | 35 |
| 06 | 872 | 44 |
| 07 | 684 | 35 |
| 08 | 679 | 34 |
| 09 | 662 | 34 |
| 10 | 896 | 45 |
| 11 | 752 | 38 |
| 12 | 825 | 42 |

The subtitle timing audit covers all 12 episodes and reports an overall PASS with 36 early/middle/late visual spot checks.

## 10. Exact anime archive identity

The exact ZIP files supplied for Phase 0 are identified by SHA-256 in:

`IDOLY_PRIDE_V2_ANIME_BUNDLE_SHA256SUMS.txt`

Those hashes, rather than the byte-size fields in the earlier extraction manifest, define the locked audiovisual bundle identity for `IP-V2-SNAPSHOT-2026-08-13-A`.

This explicitly accommodates minor archive-size changes caused by screenshot deduplication or repacking while keeping the analytical snapshot reproducible.

## 11. Anime provenance companion files

The following supplied files are part of the Phase 0 provenance package:

- `manifest(20260813-230720).json`;
- `README(3).md`;
- `subtitle_timing_audit(1).json`.

The manifest content records a generation timestamp of `2026-08-07T02:20:54.320806+00:00` despite the later filename assigned on upload. The subtitle timing audit records `2026-08-07T02:07:33.725222+00:00`.

A small Episode 1 subtitle-snapshot difference was observed between the current uploaded bundle copy and the timing-audit record. It is source-locked as a known non-blocking discrepancy rather than silently normalized away.

## 12. Telephone source status

Telephone material is a special evidentiary class.

At lock time:

- telephone references: 256;
- source audio cached: 211;
- telephone audio unavailable upstream: 45;
- approximate ASR transcripts: 211.

Telephone audio is primary evidence when available. ASR text is derived, approximate, and unreviewed. It must not serve as the sole basis for subtle claims about Japanese particles, pronouns, sentence endings, exact quotations, or micro-delivery without audio verification.

## 13. Historical analytical corpus

Prior IDOLY PRIDE chats, old unit deep dives, transcript summaries, and earlier synthesis documents remain available as historical analytical material.

Their role is:

- hypothesis recovery;
- source discovery;
- provenance of earlier interpretations;
- revision tracking.

They never override primary evidence and do not define V2 analytical priority.

## 14. Snapshot boundary

Initial V2 game source cutoff:

`2026-08-13T20:13:01+00:00` incremental game-corpus refresh.

Initial V2 anime source cutoff:

complete 12-episode TV anime analysis-bundle set supplied and hashed on 2026-08-13.

Initial V2 4koma source cutoff:

archive manifest dated 2026-08-09.

New live-game material after this baseline enters the source-delta ledger and does not silently rewrite this snapshot.
