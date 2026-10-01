---
series: BLUE_ARCHIVE
artifact_type: source_class_crosswalk
scope: Current Japanese source classes, provenance, chronology, and analytical admission
version: "1.0"
status: canonical
source_boundary: "Pinned electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8; corpus generation BA_REFRESH_20260928T032248159554Z; only the 480 main units have admitted deep readings"
do_not_use_as_current_authority: false
created: 2026-09-28
updated: 2026-09-28
---

# Blue Archive source-class crosswalk

## 0. Authority and exact route

This crosswalk distinguishes **available**, **inspected**, and **admitted** evidence. The analytical repository contains the 480 completed main-story readings. The source/ingestion workspace contains the pinned Japanese generation `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z/`, built from `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, recorded game version `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`. The [source reconciliation](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_RECONCILIATION_20260928.md) preserves the earlier V1 witness for its completed readings. This crosswalk is analytical routing; it does not copy source transcripts into Git or substitute the refreshed source wording into V1 readings.

For any new source-facing claim, follow `story_id` → `<canonical_path>` relative to the pinned generation (the value already begins with `02_CANONICAL_STORIES/`) → scene/utterance/choice or message ID → `03_STRUCTURED_DATA/*.jsonl` → the record's `raw_group_ids`, `source_paths`, `source_sha256` and source commit → the immutable raw upstream snapshot recorded by `00_MANIFESTS/SOURCE_MANIFEST.json`. `03_STRUCTURED_DATA/stories.jsonl` supplies the authoritative per-object source class and canonical path for this generation. The `10_READING_INDEXES/STORIES/<CLASS>.md` files are navigation only. A derived person/relationship bundle is a reversible projection, not another primary story witness. The [event index](BLUE_ARCHIVE_EVENT_ANALYTICAL_PRIORITY_INDEX.md) carries all 1,010 event story IDs.

## 1. Complete class inventory at the pinned generation

Counts are canonical **story objects**, not raw rows, distinct people or completed analytical readings. They total **4,864** and were checked against `03_STRUCTURED_DATA/stories.jsonl` and the 4,864-row `00_MANIFESTS/RELEASE_CHRONOLOGY.csv`.

| Source type | Objects | Canonical route under `02_CANONICAL_STORIES/` | Release dates present | Current analytical state and strongest initial use |
|---|---:|---|---:|---|
| `main` | 480 | `MAIN/` | 0 | 480 admitted readings, 26 checkpoints; institutional/crisis and some ordinary evidence. Older readings retain their declared V1 text witness. |
| `group` | 65 | `GROUP/` | 0 | Available, unadmitted; club routine, peer hierarchy, work and ordinary disagreements. |
| `event` | 1,010 | `EVENT/EVENT_*/` | 1,010 | Available, unadmitted; continuity, cross-school, seasonal, comic and ordinary contexts all eligible for reading. |
| `bond` | 1,161 | `BOND/` | 1,161 | Available, unadmitted; bounded private/Sensei dyads, ordinary preferences, and relationship-specific self-presentation. |
| `momotalk` | 1,161 | `MOMOTALK/` | 1,161 | Available, unadmitted; message rhythm, initiation, alternate replies and bond prefaces. |
| `character_data` | 511 | `CHARACTER_DATA/` | 283 | Available, unadmitted; contextual written language, profile and variant conditions; no performed-voice claim. |
| `mini` | 46 | `MINI/` | 0 | Available, unadmitted; short scenes require their own continuity and speaker check. |
| `special_operation` | 96 | `SPECIAL_OPERATION/` | 0 | Available, unadmitted; classify mode and continuity before claim use. |
| `unclassified_scenario` | 334 | `UNCLASSIFIED_SCENARIO/` | 0 | Available, unadmitted; source-class identity remains unresolved, so no automatic narrative use. |

**Release order is documentary order.** `RELEASE_CHRONOLOGY.csv` marks `story_chronology_confidence=unresolved` for **all 4,864** rows. An event release date, event number, bond episode number, file order or main crosswalk order does not establish an in-universe relation among those source classes. Scene-specific before/after claims require explicit narrative anchors or a corroborated later presupposition, with counterevidence recorded. When order remains open, a scene can still support contextual repertoire, ordinary pleasure, voice or relationship behavior; it cannot silently create a state-transition edge. Main-story knowledge boundaries remain those of the source-facing readings and checkpoints.

All 1,010 event objects have an unresolved overarching `event_title_jp` field (`missing_in_current_raw`); their stable `event_content_id` and story IDs remain the route. Twenty-eight event story objects have two `event_contexts` in the structured record, preserving repeat/release contexts under one canonical reading. No event episode has been duplicated merely for its second context. Participant IDs are metadata leads; speaker attribution, role, variant and full cast must be checked in the complete story. `PERSON_REGISTRY.csv`, `STUDENT_VARIANT_REGISTRY.csv` and `STORY_SPEAKER_REGISTRY.csv` provide identity/mapping routes with their recorded uncertainty.

`00_MANIFESTS/MOMOTALK_BOND_CROSSWALK.csv` has **1,189 source-field links**, covering **1,161 distinct MomoTalk thread IDs** and **1,161 distinct bond story IDs**. The join is `AcademyMessanger.FavorScheduleId → AcademyFavorSchedule.ScenarioSriptGroupId`. It routes related material; it does not imply every message has the same audience knowledge as the bond encounter or that a possible Sensei reply occurred alongside its alternatives.

## 2. First retrieval questions, not admissions

The [readiness audit](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_BOOTSTRAP_AUDIT.md#24-pilot-reassessment) proposes a narrow Yuuka council/club decision design and Serika's familiar service/reciprocity contexts as an ordinary alternative. These are **metadata retrieval leads** for an actual source-admission decision, not assertions about unread story plots:

| Question | Available source routes identified by person metadata | What still needs inspection |
|---|---|---|
| Yuuka: council, club and low-pressure contrast | 8 `group` objects (`BA:group:1201`–`:1203`, `:1502`–`:1503`, `:3101`–`:3103`); 31 event objects across event IDs 806, 810, 811, 817, 818, 821, 822, 823, 842; 14 bond and 14 MomoTalk objects linked to `BA_PERSON_YUUKA`. | Complete selected stories, actual speaker/role, ordinary versus emergency setting, event chronology, variant and Sensei-branch limits. Game-club events 825/854 have other Pavane people in metadata; they do not establish Yuuka's appearance. |
| Serika: work, scarcity, peer and Sensei reciprocity | `BA:group:2101` and `:2102`; 57 event objects across IDs 809, 810, 814, 815, 818, 821, 822, 823, 841, 860; 13 bond and 13 MomoTalk objects linked to `BA_PERSON_SERIKA`. | Full service and peer contexts, independent desires/pleasure, recurring versus situational refusal, story order and alternative Sensei replies. |

The first bounded group review packet is the complete two-part `BA:group:2101`/`:2102` Abydos committee group story for the Serika ordinary/peer question. The first inquiry-led event packet is `EVENT_816` (all 17 objects) to test ordinary-context coverage beyond the main-arc cast. The independent rotation begins with `EVENT_80000` (nine separate person-specific objects); `EVENT_814` (all 16 objects) follows for an Abydos/Serika comparison. Yuuka's alternative first group packet is the complete `BA:group:1201`–`:1203` C&C sequence; later Veritas or other group selections must include episode 1 when their numbered sequence begins before the Yuuka-linked episode. These are selection decisions for reading, not admitted evidence or plot descriptions.

An event's person-ID overlap can suggest a reading queue without deciding its analytical value. The index deliberately includes ordinary group, work, food, play and leisure candidates besides main-plot overlaps. Read selected complete stories, including apparently quiet episodes within the chosen package. Recheck all 65 group and all 1,010 event metadata objects as subject questions change; material unselected at one point remains available rather than analytically rejected.

## 3. Admission and chronology record

A supplemental story enters an analysis only through an explicit scoped decision recording:

1. exact `story_id`, source class, canonical path, raw source witness and version;
2. the character/relationship/institution or literary question, including ordinary-life value where relevant;
3. the complete source sequence inspected, choice/message boundaries and label/identity uncertainties;
4. documentary release order **and** separate in-story chronology with evidence/confidence (`located`, `relative`, `unresolved`);
5. the claims the material supports or narrows, counterreadings and excluded transfers;
6. affected [source gaps](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_GAP_IMPACT_REGISTER.md), ledgers and coverage rows;
7. review/acceptance state and an evidence locator back to the Japanese source.

Current supplemental admission ledger: **none**. The event index's intake cues and this crosswalk do not themselves admit any group, event, bond, MomoTalk, mini, character-data, special-operation or unclassified story. A source refresh requires reconciling object IDs, paths, aliases and recorded provenance before carrying this inventory forward. A genuinely prospective model test requires its rule and prediction freeze before exposing the selected unread material; otherwise the comparison is retrospective.
