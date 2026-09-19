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

Prior EVENT_0010 checkpoint: [EVENT_0010 full reading](03_SEQUENTIAL_EVENT_READINGS/LEO_NEED/PJSK_EVENT_0010_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). Leo/need Honami operative I3 and WxS Emu school I1 are integrated across six ledgers; 15 historical one-time screens remain, next EVENT_0011 under the clarified five-screen authorization. EVENT_0007/0009 complete source screens remain reusable. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0011 checkpoint: [EVENT_0011 full reading](03_SEQUENTIAL_EVENT_READINGS/MMJ/PJSK_EVENT_0011_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). MMJ Shizuku operative I3 and group live-launch I2 are integrated across six ledgers; 14 historical one-time screens remain, next EVENT_0012 under the clarified five-screen authorization. EVENT_0007/0009 complete source screens remain reusable. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0012 checkpoint: [EVENT_0012 full reading](03_SEQUENTIAL_EVENT_READINGS/VBS/PJSK_EVENT_0012_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). VBS Toya operative I3 is integrated across six ledgers; MMJ Minori and N25 Ena-context routes are I1, LN/WxS I0. Thirteen historical one-time screens remain, next EVENT_0013 under the clarified five-screen authorization. EVENT_0007/0009 complete source screens remain reusable. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0013 checkpoint: [EVENT_0013 full reading](03_SEQUENTIAL_EVENT_READINGS/LEO_NEED/PJSK_EVENT_0013_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). Leo/need unresolved I2 and the Ichika–Nene relationship I3 are integrated across six ledgers; Honami–Emu and Tsukasa–Saki are I2, MMJ/VBS I1, N25 I0. Twelve historical one-time screens remain; EVENT_0015 is outside the completed five-screen authorization. EVENT_0007/0009 complete source screens remain reusable. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0015 checkpoint: [EVENT_0015 full reading](03_SEQUENTIAL_EVENT_READINGS/WXS/PJSK_EVENT_0015_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). WxS open park-threat knowledge and planning are integrated at I2; `WXS-EP-PARK-E0015-OPEN` records the unresolved receipt, and existing Ichika–Nene and Tsukasa–Saki relationships receive I2 continuity. Eleven historical screens remain; EVENT_0016 is next, with nineteen operations remaining in the authorized twenty-event queue. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0016 checkpoint: [EVENT_0016 full reading](03_SEQUENTIAL_EVENT_READINGS/LEO_NEED/PJSK_EVENT_0016_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). Saki–Tsukasa corrected shared meaning and Toya–Tsukasa reciprocal support are integrated at I3; Honami and Toya receive bounded I2 refinements. Ten historical screens remain; EVENT_0017 is next, with eighteen operations remaining in the authorized twenty-event queue. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0017 checkpoint: [EVENT_0017 full reading](03_SEQUENTIAL_EVENT_READINGS/MMJ/PJSK_EVENT_0017_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). `MMJ-EP-MN-E0017` records Minori's enacted recipient-specific hope model at I3; the MMJ group and established mentorship dyads receive bounded I2 refinements. Nine historical screens remain; EVENT_0018 is next, with seventeen operations remaining in the authorized twenty-event queue. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0018 checkpoint: [EVENT_0018 full reading](03_SEQUENTIAL_EVENT_READINGS/LEO_NEED/PJSK_EVENT_0018_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). `LN-EP-ICHIKA-E0018` records repeatable listener-oriented performance at I3; `REL-CROSS-ICHIKA-KOHANE-E0018` records a new durable cross-unit relationship at I3. Eight historical screens remain; EVENT_0020 is next, with sixteen operations remaining in the authorized twenty-event queue. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0020 checkpoint: [EVENT_0020 full reading](03_SEQUENTIAL_EVENT_READINGS/LEO_NEED/PJSK_EVENT_0020_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). `LN-REL-G-E0020` records Leo/need's tested common professional direction at I3; all four P04 humans remain, and existing Ichika/Kohane/Nene routes receive bounded refinements. Seven historical screens remain; EVENT_0021 is next, with fifteen operations remaining in the authorized twenty-event queue. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0021 checkpoint: [EVENT_0021 full reading](03_SEQUENTIAL_EVENT_READINGS/VBS/PJSK_EVENT_0021_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). `VBS-EP-AK-E0021`, `VBS-REL-AK-TY-3` and `VBS-REL-AK-ARATA-E0021` record distinct I3 operative, partnership and rivalry changes while all four human IDs remain. Six historical screens remain; EVENT_0022 is next, with fourteen operations remaining in the authorized twenty-event queue. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0022 checkpoint: [EVENT_0022 full reading](03_SEQUENTIAL_EVENT_READINGS/N25/PJSK_EVENT_0022_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). New `REL-CROSS-ENA-AIRI-E0022` records a durable cross-unit relationship I3; `REL-N25-EMZ-1`, Rui–Mizuki, family, MMJ-group and Stage routes receive bounded I1/I2 evidence while Mizuki's disclosure conflict remains unresolved. Five historical screens remain; EVENT_0023 is next, with thirteen operations remaining in the authorized twenty-event queue. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0023 checkpoint: [EVENT_0023 full reading](03_SEQUENTIAL_EVENT_READINGS/MMJ/PJSK_EVENT_0023_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). New `MMJ-EP-HR-E0023` records Haruka's enacted self-directed-rest distinction at I3; Stage MEIKO is integrated locally and established MMJ dyads receive bounded care refinements. Four historical screens remain; EVENT_0024 is next, with twelve operations remaining in the authorized twenty-event queue. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0024 checkpoint: [EVENT_0024 full reading](03_SEQUENTIAL_EVENT_READINGS/WXS/PJSK_EVENT_0024_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). `WXS-EP-RUI-E0024`, `REL-CROSS-TOYA-RUI-E0024` and `VBS-REL-TOYA-FATHER-2` record distinct I3 outsider-cooperation, cross-unit relationship and family de-escalation changes; `REL-CROSS-AKITO-RUI-E0024` records purpose-specific I2 respect/access; all human IDs remain. Three historical screens remain; EVENT_0025 is next, with eleven operations remaining in the authorized twenty-event queue. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0025 checkpoint: [EVENT_0025 full reading](03_SEQUENTIAL_EVENT_READINGS/WXS/PJSK_EVENT_0025_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). `WXS-EP-PARK-E0015-OPEN → WXS-EP-PARK-E0025` records the sole I3 transition from open park threat to a demonstrated, provisionally accepted alternative and official troupe role; founded human, group, park-support, cross-unit and Wonderland records receive bounded I1/I2. Two historical screens remain; EVENT_0027 is next, with ten operations remaining in the authorized twenty-event queue. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0027 checkpoint: [EVENT_0027 full reading](03_SEQUENTIAL_EVENT_READINGS/LEO_NEED/PJSK_EVENT_0027_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). New `LN-EP-SAKI-E0027` records a demonstrated recipient-and-feeling composition method at I3; new local `LN-VS-SCHOOL-RIN-E0027` records Rin's School-local profile at I2; founded LN group/care/sibling routes remain while all human IDs are preserved. One historical screen remains; EVENT_0028 is next, with nine operations remaining in the authorized twenty-event queue. Forward N25 EVENT_0090 / next EVENT_0091 remains separate. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0028 checkpoint: [EVENT_0028 full reading](03_SEQUENTIAL_EVENT_READINGS/VBS/PJSK_EVENT_0028_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). New `VBS-EP-KH-E0028` records Kohane's relational-confidence method at I3; founded An–Kohane and VBS group topology receive strong I2 while An's private comparison remains OPEN. Every historical universal screen is complete. EVENT_0091 is next, with eight operations remaining in the authorized twenty-event queue; forward N25 EVENT_0090 is the inherited boundary. Older import and checkpoint paragraphs retain their historical cutoffs.

Prior EVENT_0091 checkpoint: [EVENT_0091 full reading](03_SEQUENTIAL_EVENT_READINGS/LEO_NEED/PJSK_EVENT_0091_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). `LN-EP-SAKI-E0091` and `LN-REL-SOLIS-E0091` are the two new I3 owners; `LN-REL-G-E0020` remains the group owner at strong I2. Prospective Solis affiliation is under review, not signed or debuted. EVENT_0092 is next, with seven operations remaining. The completed historical checkpoint remains EVENT_0028.

Prior EVENT_0092 checkpoint: [EVENT_0092 full reading](03_SEQUENTIAL_EVENT_READINGS/MMJ/PJSK_EVENT_0092_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). `MMJ-EP-AI-E0092` and `MMJ-REL-AIRI-AYUMI-E0092` are the two new I3 owners; `MMJ-VS-STAGE-KAITO-E0092` is local I2; `MMJ-REL-GROUP-06` remains strong I2. Course transfers and lasting schedule/friendship outcomes remain open. EVENT_0093 is next, with six operations remaining. The completed historical checkpoint remains EVENT_0028.

Prior EVENT_0093 checkpoint: [EVENT_0093 full reading](03_SEQUENTIAL_EVENT_READINGS/N25/PJSK_EVENT_0093_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). `MZ-E0093-01` and `REL-FAMILY-MAFUYU-MOTHER-E0093` are the two new I3 owners; `EPI-N25-MF-E0093` and `EPI-N25-G-E0093` are scoped I2; `REL-N25-MZM-3` and `REL-N25-G-7` remain strong I2. The N25 tuple updates only Mizuki. Escape, shelter, computer intent and disclosure outcomes remain open. EVENT_0094 is next, with five operations remaining. The completed historical checkpoint remains EVENT_0028.

Prior EVENT_0094 checkpoint: [EVENT_0094 full reading](03_SEQUENTIAL_EVENT_READINGS/MMJ/PJSK_EVENT_0094_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). `MMJ-EP-HR-E0094` is the one new I3 owner; `MMJ-EP-HR-E0023` remains separate; `REL-CROSS-LN-MMJ-SCHOOL-E0001` and `REL-CROSS-ICHIKA-NENE-E0013` receive the only strong-I2 relationship increments. MMJ group, LN states and Stage topology remain preserved, with no singer ID. Course implementation/disclosure, uploader identity and post-transfer durability remain open. EVENT_0095 is next, with four operations remaining. The completed historical checkpoint remains EVENT_0028.

Prior EVENT_0095 checkpoint: [EVENT_0095 full reading](03_SEQUENTIAL_EVENT_READINGS/WXS/PJSK_EVENT_0095_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). `WXS-EP-NENE-E0095` is the sole new I3 owner; `WXS-EP-NENE-E0008` remains separate; new `WXS-REL-NENE-YUKA-E0095` is bounded high I2; the WxS group, Rui, Sakurako and Wonderland relations remain strong I2, with no dedicated KAITO ID. Unsafe preparation, permanent mastery and unresolved troupe direction remain open. EVENT_0096 is next, with three operations remaining. The completed historical checkpoint remains EVENT_0028.

Prior EVENT_0096 checkpoint: [EVENT_0096 full reading](03_SEQUENTIAL_EVENT_READINGS/LEO_NEED/PJSK_EVENT_0096_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). EVENT_0096 creates no I3 owner; `REL-CROSS-KANADE-HONAMI-E0002` is very strong I2, `LN-EP-HONAMI-E0010` strong I2, and new `REL-CROSS-HONAMI-MIZUKI-E0096` bounded I2. Kanade, Honami–Emu, School and WxS owners remain I2 without successors. Crisis disclosure, health, care-labor and performed-fiction limits remain open. EVENT_0097 is next, with two operations remaining. The completed historical checkpoint remains EVENT_0028.

Current forward checkpoint: [EVENT_0097 full reading](03_SEQUENTIAL_EVENT_READINGS/VBS/PJSK_EVENT_0097_DEEP_READING.md) and [corpus map](PJSK_ANALYTICAL_CORPUS_MAP.md). New `VBS-EP-AN-E0097` records grief-aware informed pursuit; `VBS-REL-AN-KEN-E0097` succeeds the supportive baseline with forgiveness/repair open; new `VBS-REL-AN-NAGI-E0097` is bounded high I2. Founded VBS and Street owners remain without successors; coercive testing, victory, grief, coalition, rematch, and manifestation limits remain open. EVENT_0098 is next, with one operation remaining. The completed historical checkpoint remains EVENT_0028.
