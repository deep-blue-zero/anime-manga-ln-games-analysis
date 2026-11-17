---
title: "Look Back — source inventory"
series: look-back
artifact_id: LB_SOURCE_INVENTORY
artifact_type: source_inventory
generation: LB-G1
version: "1.0"
status: canonical
authority_scope: "Bibliographic/source controls only; no page or narrative findings"
source_boundary: "One Japanese standalone manga EPUB, metadata verified; narrative admission and inspection NONE"
canonical_home: series/look-back/LB_SOURCE_INVENTORY.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Look Back source inventory

Metadata reconnaissance on 2026-11-07 identified one Japanese EPUB, ルックバック, creator 藤本タツキ, publisher 集英社. The 2026-11-04 import report and manifest and propagation receipt were inspected, and the live listing agreed with recorded file metadata. Original-byte copy/integrity and package checks are reported prior evidence, not newly rerun content checks.

| Alias | Work / medium | Witness | Present | Admitted | Inspected |
|---|---|---|---|---|---|
| LB-JP-W01 | Look Back / ルックバック; standalone manga | Japanese publisher EPUB; exact edition and layout binding pending | LISTED | NONE | NONE |

One file is not a page-completeness certificate. The source's internal scenes, chapter/section divisions, printed pagination, colour/apparatus content and narrative facts remain unexamined. No adaptation witness is present in this source root. Other Fujimoto works, including the short-story collection and Chainsaw Man, have separate project identities and are excluded here.

The owner import provenance records a Calibre library and an owner report that almost all ebooks came from Rakuten Kobo; individual purchase receipts were not inspected. Exact private Drive identities, raw hashes, local paths and acquisition receipts remain outside public Git. An authorized source operator binds LB-JP-W01 to the private immutable witness receipt before use; inaccessible binding is a blocker, not permission to guess.

## Controls and gaps

| ID | State | Consequence / acceptance duty |
|---|---|---|
| LB-SRC-01 | Metadata verified, content unreviewed | No plot, cast, scene or completeness claim |
| LB-SRC-02 | Immutable witness / ordered image map pending | Source operator binds file identity and maps actual occurrence order before reading |
| LB-SRC-03 | Legibility, facing pages and apparatus uninspected | Reader verifies required pages and separates narrative from spoiler-bearing apparatus |
| LB-SRC-04 | Image/Japanese inspection capability unprobed | Verify actual STILL_IMAGE and lettering route before interpretation |
| LB-SRC-05 | No run; CLOSED | NONE_AWAITING_RUN_AUTHORIZATION; owner defines work/run scope |
| LB-SRC-06 | Adaptation and author-wide comparisons excluded | No remembered adaptation or other work supplies evidence |

## Update contract

The witness record must retain alias, edition/language/publisher, immutable private binding status, ordered-map status, apparatus exclusions, authorized scope and actual inspection coverage independently. Advance LISTED → IDENTITY_BOUND → INSPECTION_ROUTE_VERIFIED → ADMITTED → INSPECTED_FOR_DECLARED_SCOPE only with the relevant evidence and authorization. Keep PENDING or BLOCKED with a precise cause when required.

Append events `event_id | date | alias/control | old_state | new_state | evidence_basis | responsible_role`. Current cells may change only alongside history. Changed bytes or another edition get a new alias; preserve the old map. Public locators carry aliases, not private access details.

| Event | Date | Transition | Basis |
|---|---|---|---|
| LB-SRC-E01 | 2026-11-07 | UNRECORDED → METADATA_VERIFIED_CONTENT_UNREVIEWED | Bounded listing/import/propagation reconnaissance |

This file is an inventory and control record, not a source lock or evidence of sequential reading.
