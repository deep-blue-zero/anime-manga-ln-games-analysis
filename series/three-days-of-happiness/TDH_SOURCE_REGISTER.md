---
title: "Three Days of Happiness — Source identity and admission register"
artifact_id: TDH_TDH_SOURCE_REGISTER
artifact_type: source_and_coverage_register
series: three-days-of-happiness
version: "1.0"
generation: INITIAL_BOOTSTRAP
status: canonical
scope: "Source identity and admission register"
authority_scope: initial_project_design_and_empty_analytical_frontier_only
source_boundary: "One Japanese standalone novel EPUB inventoried; historical technical audit reviewed; no narrative admitted or read"
canonical_home: series/three-days-of-happiness/TDH_SOURCE_REGISTER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Three Days of Happiness — source and coverage register

## Observed witness

| Public alias | Bibliographic/source metadata | Observation basis | Admission / coverage |
|---|---|---|---|
| `TDH-JP-01` (reserved, not yet fingerprint-bound) | 三日間の幸福; 三秋 縋; Japanese MediaWorks Bunko standalone EPUB | Live folder/file presence on 2026-11-07; historical audit dated 2026-08-30 reports 333,787 bytes, 40 archive entries, five images and passed CRC/container checks | `INVENTORIED`; `NOT_ADMITTED`; `NOT_READ`; chapter/spine map `UNRESOLVED` |

The earlier audit labels the main novel complete. This is a reported provenance claim, not independently verified page coverage. Its digest and restricted source location are retained in the private campaign/source records; no private identifiers or receipts belong in public Git. No remote checksum, byte comparison, rendered page inspection or narrative inspection was performed for this bootstrap. Five reported images do not prove five narrative illustrations. Technical packaging validity does not certify textual correctness, publication completeness or interpretive readiness.

## Admission obligations

| ID | Open obligation | Required resolution | Effect |
|---|---|---|---|
| SRC-01 | Immutable source binding | Retrieve the governed witness; verify content digest and bibliographic/language metadata; bind reserved alias to that identity and receipt | Blocks reliable source citation |
| SRC-02 | Internal unit/locator map | Enumerate spine resources, chapters/sections and stable paragraph convention without silently changing order; distinguish body, afterword and image resources | Blocks reading schedule and exact locators |
| SRC-03 | Completeness and perception | Check missing resources, textual continuity and legible rendering within proposed scope; record remaining uncertainty rather than assume the historical audit settles it | Blocks affected unit admission |
| SRC-04 | Edition/paratext boundary | Record edition/printing identifiers available, source publication order, paratext exposure and any translation/adaptation exclusions | Blocks unqualified whole-work or cross-source claims |

These are future admission tasks, not authorization to read narrative now. Metadata reconnaissance is complete for design; full source admission is not complete.

## Coverage transaction contract

On admission, add one row per mapped source unit with `unit_id`, witness alias/fingerprint, native start/end, published heading if safe, body/paratext classification, disclosure ordinal, depicted time if known, admission authority, inventory/inspection/read/integration states, reading path, unresolved gaps and next operation. Preserve distinct fields: an inventoried unit is not a read unit, and a read unit is not integrated until its notebook transaction is accepted.

Current unit rows: **none**. No chapter count or ordinal is invented from EPUB resource count. `ANALYSIS_CURRENT = EMPTY` and `RECONSTRUCTION_CURRENT = EMPTY`; observed source availability is a single unadmitted witness, not an open horizon.

Record each changed source identity as an appended witness event with predecessor/successor alias, reason, digest comparison, affected locators and reinspection obligations. Do not silently update a bound alias. The source register is mutable control state with append-only events; frozen receipts remain intact. Source-related contradictions link to Notebook Claims if they change an analytical assertion, but technical defects alone do not create fictional events.

## Locator grammar

Text: `TDH-JP-01::<spine-href>#<stable-fragment-or-paragraph>::<chapter/section>`. Use actual XHTML member names; one-based paragraph indices only under a recorded normalization rule. Preserve paragraph offsets and short context anchors in the private locator map when needed, without uploading bulk text. A public brief quotation may resolve an ambiguity when necessary.

Images: `TDH-JP-01::<image-resource>@<spine-position>` with inspection lane `STILL_IMAGE` and actual inspection status. Record printed pages where observed, but never treat reflow-reader page numbers as edition-stable. A unit-only locator can route work but cannot bear a precise linguistic claim. Unresolved coordinates stay explicitly unresolved until mapped.

## Control history

| Date | Event | Scope / consequence |
|---|---|---|
| 2026-11-07 | Metadata-only reconnaissance recorded | One prior-audited Japanese EPUB present; four admission obligations open; no source unit admitted |
