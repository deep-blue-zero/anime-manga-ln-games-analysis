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

The analysis uses the [frozen source lock](01_SOURCE_LOCK_AND_INVENTORY/PJSK_ANALYTICAL_SOURCE_LOCK.md), `PJSK_SOURCE_20260822T184634Z_EVENT_0213`. The [corpus map's current state](PJSK_ANALYTICAL_CORPUS_MAP.md#current-state) owns recovery and continuation. All five human main-story foundations and historical EVENT_0001–0005 dispositions are integrated. [EVENT_0005](03_SEQUENTIAL_EVENT_READINGS/MMJ/PJSK_EVENT_0005_DEEP_READING.md) changes MMJ’s operating model at I3 while preserving its four MS-04 human states. This single-event operation is complete; EVENT_0006 is the next historical candidate and 18 older universal screens remain. EVENT_0090 / next EVENT_0091 remains the separate forward frontier. Character packages, deferred later routes and final syntheses remain unfinished; the earlier continuous campaign is paused.

The governing [analytical method](00_FRAMEWORKS_AND_METHODS/PJSK_ANALYTICAL_METHOD.md) and [synthesis architecture](00_FRAMEWORKS_AND_METHODS/PJSK_SYNTHESIS_ARCHITECTURE.md) remain current. The [character reconstruction method](00_FRAMEWORKS_AND_METHODS/PJSK_CHARACTER_RECONSTRUCTION_METHOD.md) and [live-service integration method](00_FRAMEWORKS_AND_METHODS/PJSK_LIVE_SERVICE_INTEGRATION_METHOD.md) govern their respective later layers.

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

Prior EVENT_0006 checkpoint: [EVENT_0006 full reading](03_SEQUENTIAL_EVENT_READINGS/VBS/PJSK_EVENT_0006_DEEP_READING.md) and its [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). VBS An–Kohane relationship I3 and MMJ cross-unit I1 are integrated across all six ledgers; 17 older universal screens remain, next EVENT_0008. The separate forward N25 frontier remains EVENT_0090, next EVENT_0091. The earlier import table above is a preserved import snapshot.

Prior EVENT_0008 checkpoint: [EVENT_0008 full reading](03_SEQUENTIAL_EVENT_READINGS/WXS/PJSK_EVENT_0008_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). WxS Nene's operative I3 and Leo/need mediated I1 are integrated across all six ledgers; 16 earlier universal screens remain, next EVENT_0010 under the authorized five-screen continuation. EVENT_0007/0009 complete source screens remain reusable; the separate forward N25 frontier is EVENT_0090, next EVENT_0091. Historical import and EVENT5/6 paragraphs above retain their own cutoffs.

Current historical checkpoint: [EVENT_0010 full reading](03_SEQUENTIAL_EVENT_READINGS/LEO_NEED/PJSK_EVENT_0010_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). Leo/need Honami operative I3 and WxS Emu school I1 are integrated across six ledgers; 15 historical one-time screens remain, next EVENT_0011 under the clarified five-screen authorization. EVENT_0007/0009 complete source screens remain reusable. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.
