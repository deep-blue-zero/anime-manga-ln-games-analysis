---
title: "Domestic Girlfriend — source inventory and admission controls"
series: domestic-girlfriend
artifact_id: DG_SOURCE_INVENTORY
artifact_type: source_inventory
generation: DG-G1
version: "1.0"
status: canonical
authority_scope: "Metadata and source-control authority only; not a source lock or narrative evidence"
source_boundary: "Metadata reconnaissance of Japanese manga volumes 01-03 only; no narrative units admitted or inspected"
canonical_home: series/domestic-girlfriend/DG_SOURCE_INVENTORY.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Source inventory and admission controls

## Reconnaissance established

Observation date: 2026-11-07. The campaign compared the live title folder with its 2026-09-28 import manifest. Three Japanese EPUBs are represented. The manifest identifies ドメスティックな彼女, creator 流石景 and publisher 講談社. Its coverage note explicitly limits the supplied library to volumes 01–03.

The manifest reports copied bytes verified by SHA-256 and package checks including ZIP/container/resources. Those are historical import receipts, not new byte verification or content inspection in this bootstrap. No pages, chapter text or narrative content were inspected here. Individual purchase receipts were not inspected; the import records an owner-supplied Calibre-library provenance and an owner report that almost all ebooks came from Rakuten Kobo. No per-file purchase claim follows.

Exact Drive identities, hashes, local source paths and raw import receipts remain in the private evidence/campaign plane. Public aliases below are retrieval keys, not claims that witnesses are source-locked. An authorized source operator resolves each alias against the private manifest and binds the exact source revision before use. If that binding is unavailable, admission is blocked rather than guessed from a filename.

## Witness rows

The source inventory is append-preserving. A new file or changed byte identity receives a new witness alias; an edition change never overwrites a prior identity. Each row denotes one available file, not an analytical unit already completed.

| Source alias | Metadata title | Language / edition | Role | Availability | Import integrity | Admission | Inspection / mapping |
|---|---|---|---|---|---|---|---|
| DG-JP-V01-W01 | ドメスティックな彼女（１） | Japanese digital manga; edition particulars pending | Main V01 | LISTED | HISTORICALLY_REPORTED | NOT_AUTHORIZED | UNINSPECTED; chapters, pages and spreads unmapped |
| DG-JP-V02-W01 | ドメスティックな彼女（２） | Japanese digital manga; edition particulars pending | Main V02 | LISTED | HISTORICALLY_REPORTED | NOT_AUTHORIZED | UNINSPECTED; chapters, pages and spreads unmapped |
| DG-JP-V03-W01 | ドメスティックな彼女（３） | Japanese digital manga; edition particulars pending | Main V03 | LISTED | HISTORICALLY_REPORTED | NOT_AUTHORIZED | UNINSPECTED; chapters, pages and spreads unmapped |

“Edition particulars pending” includes colophon, exact collected-edition layout, completeness and any special extras. An inventory listing does not establish the title's official final extent. No volume beyond V03 is available within this verified project inventory; no outside endpoint or publication-status claim is made.

## Gaps and control decisions

| Control ID | Actual present state | Consequence | Next owner / acceptance condition |
|---|---|---|---|
| DG-SRC-001 | Opening acquisition only, V01–03 | Any future accepted tranche remains explicitly partial | Source operator verifies newly supplied units before proposing an inventory extension |
| DG-SRC-002 | Immutable witness binding not performed in this bootstrap | No source is locked or admitted | Source operator matches actual file and private receipt, records hash/revision and alias crosswalk |
| DG-SRC-003 | Narrative pages, chapters, spreads and apparatus uninspected | No chapter numbers, character states or page completeness claims | Authorized reader records ordered map, legibility and apparatus classification within permitted scope |
| DG-SRC-004 | Image-inspection route unprobed for these witnesses | Package availability alone cannot enable manga reading | Authorized executor verifies readable pages and records actual inspection capability |
| DG-SRC-005 | No run authorized; lock CLOSED | Next narrative operation is NONE_AWAITING_RUN_AUTHORIZATION | Owner authorizes exact units; integrator verifies gate and records consistent run fields before admission |
| DG-SRC-006 | Adaptations, translations, serialization and external summaries excluded | No cross-source completion or remembered plot used | Separate source/scope decision and method amendment if comparison is requested |

## Update contract

A source row must record alias, work/track, unit label, language, publisher/edition, private receipt binding status, immutable-identity verification status, availability, admission, ordered-map status, actual inspection coverage and excluded apparatus. The compact table above records the bootstrap subset; add the remaining fields as columns or stable per-witness subheadings when binding is performed, never as invented values.

Allowed progression is LISTED → IDENTITY_BOUND → INSPECTION_ROUTE_VERIFIED → ADMITTED → INSPECTED_FOR_DECLARED_SCOPE, with authorization and coverage recorded independently. A technical check cannot skip admission. A problem uses BLOCKED with its cause; corrected receipts append a dated event referring to the earlier event.

Every update appends an event ID, date, affected alias/control, previous state, new state, basis and responsible role. Current cells may be patched only with the event recorded. History and prior witness mappings survive. Narrative coverage advances only with the accepted reading transaction; file replacement invalidates affected locators until crosswalked.

## Source-control history

| Event ID | Date | Object | Previous → current | Basis / role |
|---|---|---|---|---|
| DG-SRC-E001 | 2026-11-07 | V01–03 inventory and controls | UNRECORDED → METADATA_VERIFIED_CONTENT_UNREVIEWED | Live listing and import metadata reconnaissance; bootstrap author |

No source-lock artifact, chapter crosswalk or page-review report exists yet. Creating one requires actual verification; the method defines its acceptance duties.
