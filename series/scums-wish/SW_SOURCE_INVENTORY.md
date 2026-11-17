---
title: "Scum’s Wish — source inventory and horizon controls"
series: scums-wish
artifact_id: SW_SOURCE_INVENTORY
artifact_type: source_inventory
generation: SW-G1
version: "1.0"
status: canonical
authority_scope: "Metadata and source-control authority only; not narrative admission or a source lock"
source_boundary: "Metadata reconnaissance of Japanese main manga volumes 01-08 and decor volume 09; no narrative units admitted or inspected"
canonical_home: series/scums-wish/SW_SOURCE_INVENTORY.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Source inventory and horizon controls

## Verified metadata scope

The 2026-11-07 campaign reconnaissance inspected the title-folder listing and decoded 2026-09-28 import manifest. Nine Japanese EPUB records identify クズの本懐, creator 横槍メンゴ and publisher スクウェア・エニックス. The manifest classifies volumes 01–08 as the main series and volume 09 decor as a supplementary epilogue/spin-off. That classification supports a separate admission horizon; it does not establish the supplement's actual chronology, scenes or continuity through content inspection.

The receipt reports original-byte copies verified by SHA-256 and ZIP/container/resource checks. No new full file integrity audit, page completeness assessment, chapter mapping or narrative inspection occurred in this bootstrap. The recorded owner provenance is a Calibre library and an owner report that almost all ebooks were purchased through Rakuten Kobo; no individual purchase receipt was inspected.

Exact source object identifiers, private paths, hashes and raw receipts remain in the governed private evidence plane. An authorized operator resolves the aliases below through that receipt and binds the actual immutable source before admission. Alias existence is not source locking.

## Source rows

| Alias | Metadata title | Track | Language / edition | Availability | Integrity / mapping | Admission / inspection |
|---|---|---|---|---|---|---|
| SW-JP-M01-W01 | クズの本懐1巻 | MAIN V01 | Japanese digital manga; precise edition pending | LISTED | Historical import checks reported; map pending | NOT_AUTHORIZED / UNINSPECTED |
| SW-JP-M02-W01 | クズの本懐2巻 | MAIN V02 | Japanese digital manga; precise edition pending | LISTED | Historical import checks reported; map pending | NOT_AUTHORIZED / UNINSPECTED |
| SW-JP-M03-W01 | クズの本懐 3巻 | MAIN V03 | Japanese digital manga; precise edition pending | LISTED | Historical import checks reported; map pending | NOT_AUTHORIZED / UNINSPECTED |
| SW-JP-M04-W01 | クズの本懐 4巻 | MAIN V04 | Japanese digital manga; precise edition pending | LISTED | Historical import checks reported; map pending | NOT_AUTHORIZED / UNINSPECTED |
| SW-JP-M05-W01 | クズの本懐 5巻 | MAIN V05 | Japanese digital manga; precise edition pending | LISTED | Historical import checks reported; map pending | NOT_AUTHORIZED / UNINSPECTED |
| SW-JP-M06-W01 | クズの本懐 6巻 | MAIN V06 | Japanese digital manga; precise edition pending | LISTED | Historical import checks reported; map pending | NOT_AUTHORIZED / UNINSPECTED |
| SW-JP-M07-W01 | クズの本懐 7巻 | MAIN V07 | Japanese digital manga; precise edition pending | LISTED | Historical import checks reported; map pending | NOT_AUTHORIZED / UNINSPECTED |
| SW-JP-M08-W01 | クズの本懐 8巻 | MAIN V08 | Japanese digital manga; precise edition pending | LISTED | Historical import checks reported; map pending | NOT_AUTHORIZED / UNINSPECTED |
| SW-JP-D09-W01 | クズの本懐 9巻 decor | DECOR V09 | Japanese digital manga; precise edition pending | LISTED | Historical import checks reported; map pending | SEPARATELY_GATED / UNINSPECTED |

These ranges describe inventory presence. They do not prove every official chapter, apparatus item or edition is present. “MAIN” and “DECOR” are source-track labels; a separate track does not assert an alternate fictional universe.

## Control and gap records

| Control ID | Present state | Analytical consequence | Next owner / acceptance condition |
|---|---|---|---|
| SW-SRC-001 | Nine sources metadata-verified, content unreviewed | No narrative completeness, actor identity or chapter claim | Source operator binds exact witnesses, mapping and legibility under authorized scope |
| SW-SRC-002 | MAIN and DECOR distinct; neither admitted | V09 cannot retrospectively settle an earlier main reading | Integrator records separate authorized boundaries and preserves main-only checkpoint before decor admission |
| SW-SRC-003 | Supplement chronology/continuity unexamined | “Epilogue/spin-off” remains manifest classification, not established story time | Authorized supplement reader verifies source positioning and classifies any retrospective relations |
| SW-SRC-004 | Covers, notes, profiles, extras and previews unclassified | Apparatus may disclose later information | Reader classifies actual components before use and records exclusions |
| SW-SRC-005 | STILL_IMAGE/Japanese inspection not probed for these files | Listing/import validity does not prove readable source access | Executor demonstrates adequate source inspection route before reading |
| SW-SRC-006 | No owner run; CLOSED | Next narrative operation NONE_AWAITING_RUN_AUTHORIZATION | Owner defines units; integrator verifies gate and consistent OPEN transition |
| SW-SRC-007 | Adaptations, translations and outside summaries excluded | No source contamination or performance claims | Separate scope and witness decision if later requested |

## Witness lifecycle and history

Required source fields are alias, track, unit, Japanese title, creator/publisher/edition, immutable private receipt binding, transport/integrity state, ordered image map, apparatus classification, authorization boundary and actual review coverage. Add exact values only when observed; UNKNOWN is preferable to an invented mapping.

Availability, identity binding, admitted scope and inspected scope are independent fields. Progression LISTED → IDENTITY_BOUND → INSPECTION_ROUTE_VERIFIED → ADMITTED → INSPECTED_FOR_DECLARED_SCOPE requires the corresponding evidence and authorization; any missing requirement stays PENDING or BLOCKED with its cause. DECOR must retain its own scope even if the same run later explicitly includes both tracks.

New file bytes or an alternate edition receive a new witness alias. Never overwrite an earlier identity to keep a convenient filename. Patch current rows through dated events with `event_id | date | alias/control | previous_state | new_state | evidence_basis | operator_role`; preserve receipts and prior mappings. Every accepted volume transaction updates actual coverage; no narrative high-water mark follows from a source listing.

| Event ID | Date | Object | Transition | Basis |
|---|---|---|---|---|
| SW-SRC-E001 | 2026-11-07 | MAIN01–08 and DECOR09 inventory | UNRECORDED → METADATA_VERIFIED_CONTENT_UNREVIEWED | Bounded live listing and import metadata reconnaissance; bootstrap author |

No exact source lock, chapter crosswalk or inspection report exists yet. Main-only and supplement-aware retrospective claims must always name their different evidence horizons.
