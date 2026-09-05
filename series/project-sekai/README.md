---
series: PJSK
artifact_type: repository_entrypoint
scope: DRIVE_ANALYTICAL_CORPUS_IMPORT
generation: V1_import_2026_09_05
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Project SEKAI analytical corpus

This tree imports all 58 analytical documents from the owner-supplied Drive folder, preserving its 23-subfolder hierarchy. The original corpus was omitted from the initial repository bootstrap because it was stored outside that bootstrap's directory scope.

Start with the [analytical corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md), then the relevant foundation, event reading, or longitudinal ledger. The [import report](09_EVIDENCE_AUDITS_AND_MANIFESTS/PJSK_IMPORT_REPORT.md) and [source/path/hash manifest](09_EVIDENCE_AUDITS_AND_MANIFESTS/PJSK_IMPORT_MANIFEST.json) describe coverage, mechanical conversions, and source provenance.

The populated narrative analysis centers on N25 foundations and later event readings, including documents through EVENT_0072. This is a snapshot of the supplied folder, not a claim that every unit, release, or reconstruction stage is complete. Keep each artifact's analytical and source boundary explicit; publication does not reconcile differences among those boundaries.

Source statuses remain `canonical`. Empty supersession fields are represented as repository-compatible empty arrays; native text exports use UTF-8 without BOM and LF line endings. Analytical body text is preserved. Both identical EVENT_0054 source documents are retained with an explicit filename collision suffix.

## Directory map

| Directory | Direct source documents | Role at import |
|---|---:|---|
| [00_FRAMEWORKS_AND_METHODS](00_FRAMEWORKS_AND_METHODS/) | 4 | populated |
| [01_SOURCE_LOCK_AND_INVENTORY](01_SOURCE_LOCK_AND_INVENTORY/) | 3 | populated |
| [02_MAIN_STORY_FOUNDATIONS](02_MAIN_STORY_FOUNDATIONS/) | 0 | contains subfolders |
| [02_MAIN_STORY_FOUNDATIONS/LEO_NEED](02_MAIN_STORY_FOUNDATIONS/LEO_NEED/) | 0 | empty source folder preserved |
| [02_MAIN_STORY_FOUNDATIONS/MMJ](02_MAIN_STORY_FOUNDATIONS/MMJ/) | 0 | empty source folder preserved |
| [02_MAIN_STORY_FOUNDATIONS/N25](02_MAIN_STORY_FOUNDATIONS/N25/) | 7 | populated |
| [02_MAIN_STORY_FOUNDATIONS/VBS](02_MAIN_STORY_FOUNDATIONS/VBS/) | 0 | empty source folder preserved |
| [02_MAIN_STORY_FOUNDATIONS/WXS](02_MAIN_STORY_FOUNDATIONS/WXS/) | 0 | empty source folder preserved |
| [03_SEQUENTIAL_EVENT_READINGS](03_SEQUENTIAL_EVENT_READINGS/) | 0 | contains subfolders |
| [03_SEQUENTIAL_EVENT_READINGS/LEO_NEED](03_SEQUENTIAL_EVENT_READINGS/LEO_NEED/) | 0 | empty source folder preserved |
| [03_SEQUENTIAL_EVENT_READINGS/MIXED](03_SEQUENTIAL_EVENT_READINGS/MIXED/) | 3 | populated |
| [03_SEQUENTIAL_EVENT_READINGS/MMJ](03_SEQUENTIAL_EVENT_READINGS/MMJ/) | 0 | empty source folder preserved |
| [03_SEQUENTIAL_EVENT_READINGS/N25](03_SEQUENTIAL_EVENT_READINGS/N25/) | 34 | populated |
| [03_SEQUENTIAL_EVENT_READINGS/VBS](03_SEQUENTIAL_EVENT_READINGS/VBS/) | 0 | empty source folder preserved |
| [03_SEQUENTIAL_EVENT_READINGS/WXS](03_SEQUENTIAL_EVENT_READINGS/WXS/) | 0 | empty source folder preserved |
| [04_LONGITUDINAL_LEDGERS](04_LONGITUDINAL_LEDGERS/) | 6 | populated |
| [05_CHARACTER_RECONSTRUCTION](05_CHARACTER_RECONSTRUCTION/) | 0 | empty source folder preserved |
| [06_SPECIALIST_AND_UNIT_SYNTHESIS](06_SPECIALIST_AND_UNIT_SYNTHESIS/) | 0 | empty source folder preserved |
| [07_FULL_SERIES_SYNTHESIS](07_FULL_SERIES_SYNTHESIS/) | 0 | empty source folder preserved |
| [08_CURRENT_RELEASE](08_CURRENT_RELEASE/) | 0 | empty source folder preserved |
| [09_EVIDENCE_AUDITS_AND_MANIFESTS](09_EVIDENCE_AUDITS_AND_MANIFESTS/) | 0 | empty in Drive; Git import report and manifest added |
| [90_LEGACY_AND_SUPERSEDED](90_LEGACY_AND_SUPERSEDED/) | 0 | contains subfolders |
| [90_LEGACY_AND_SUPERSEDED/Conversation Archives](90_LEGACY_AND_SUPERSEDED/Conversation%20Archives/) | 0 | empty source folder preserved |

The source Drive root ID is `1-W8fHu560i-B9Lg1c0MOhHFgULhNXzga`. The external source/extraction pipeline and raw media retain their existing authority. This import changes the Git analytical tree only.
