---
title: "Astra Lost in Space — omnibus source and unit map"
series: astra-lost-in-space
artifact_id: ALS_SOURCE_AND_UNIT_MAP
artifact_type: source_inventory
generation: ALS-G1
version: "1.0"
status: canonical
authority_scope: "Omnibus metadata, unit-mapping schema and admission controls only"
source_boundary: "One Japanese 彼方のアストラ 全巻合本版 omnibus EPUB; internal units unverified; no narrative admission or inspection"
canonical_home: series/astra-lost-in-space/ALS_SOURCE_AND_UNIT_MAP.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Omnibus source and unit map

The 2026-11-07 campaign inspected November 4 import/report and propagation metadata and the live listing for one Japanese EPUB, 彼方のアストラ 全巻合本版, creator 篠原健太, publisher 集英社. The report labels it a complete combined omnibus. That is a source-metadata assertion, not independently inspected completeness.

| Alias | Source object | Availability | Integrity / mapping | Admission / inspection |
|---|---|---|---|---|
| ALS-JP-OMNI-W01 | Japanese complete-omnibus EPUB as labeled | LISTED | Historical copy/package checks reported; internal mapping pending | NONE / NONE |

No internal volume/chapter labels, story facts, reading spans, page completeness or rendered legibility were inspected. One file must not become one opaque whole-series reading transaction. Nor may an analyst create synthetic individual EPUB volumes and present them as original sources.

Exact Drive IDs, file hashes, local paths and raw receipts remain private. An authorized operator binds the public alias to the immutable witness before use. The import records owner-supplied Calibre provenance and an owner report that almost all ebooks were bought through Rakuten Kobo; individual purchase receipts were not inspected.

## Unit map to populate only from source verification

Required row fields are `unit_key | actual_internal_label | unit_type | verified_presentation_order | start/end_global_image_occurrence | printed_page_resets | verified_chapter_labels/crosswalk | apparatus/exclusions | legibility/completeness | authorization | inspection | receipt_basis`.

Use internal collected-volume units if the witness visibly supplies them. Otherwise use verified chapter boundaries and record that decision before a run is authorized. Unit type and exact scope cannot be guessed from remembered publication structure or file-processing chunks. This map presently has **zero unit rows**.

## Controls

| ID | Current condition | Consequence / next acceptance duty |
|---|---|---|
| ALS-SRC-01 | Omnibus “complete” is metadata only | No series/source completeness claim without actual coverage audit |
| ALS-SRC-02 | Immutable identity and ordered image map unbound | Verify actual witness and global occurrence coordinates |
| ALS-SRC-03 | Internal volumes/chapters unknown | Map natural units before defining first run; do not invent volume count |
| ALS-SRC-04 | Covers, internal title pages, notes and previews unclassified | Separate apparatus and spoiler horizons at each internal boundary |
| ALS-SRC-05 | STILL_IMAGE/Japanese route unprobed | Verify adequate page/lettering access before interpretation |
| ALS-SRC-06 | No run; CLOSED | NONE_AWAITING_RUN_AUTHORIZATION |
| ALS-SRC-07 | Adaptations, translations and separate editions excluded | No outside knowledge fills mapping or narrative gaps |

## History

Availability, identity, mapping, authorization and actual inspection are separate fields. Progress LISTED → IDENTITY_BOUND → UNIT_MAP_VERIFIED → INSPECTION_ROUTE_VERIFIED → ADMITTED → INSPECTED_FOR_DECLARED_SCOPE requires its own evidence and scope. Any failure stays PENDING/BLOCKED with cause.

Append `event_id | date | witness/unit/control | old_state | new_state | basis | role` before changing current cells. New source bytes get a new alias; retain old unit maps and crosswalk changes. A corrected internal boundary invalidates affected locators until reconciled; do not silently renumber global image occurrences.

| Event | Date | Transition | Basis |
|---|---|---|---|
| ALS-SRC-E01 | 2026-11-07 | UNRECORDED → METADATA_VERIFIED_CONTENT_UNREVIEWED | Bounded import/propagation/listing reconnaissance |

No source lock or sequential reading exists.
