---
series: BLUE_ARCHIVE
artifact_type: source_class_crosswalk
scope: Current Japanese source classes, provenance, chronology, and analytical admission
version: "1.5"
status: canonical
source_boundary: "Pinned electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8; corpus generation BA_REFRESH_20260928T032248159554Z; 480 main units plus180 supplemental objects admitted with limits in cycles001–005"
do_not_use_as_current_authority: false
created: 2026-09-28
updated: 2026-10-01
---

# Blue Archive source-class crosswalk

## 0. Authority and exact route

This crosswalk distinguishes **available**, **inspected**, and **admitted** evidence. The analytical repository contains the 480 completed main-story readings and the180 supplemental objects accepted in cycles001–005; [cycle005](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_005_CHECKPOINT.md) supplies the latest scoped addition. The source/ingestion workspace contains the pinned Japanese generation `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z/`, built from `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, recorded game version `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`. The [source reconciliation](../01%20Source%20Lock%20and%20Inventory/BLUE_ARCHIVE_SOURCE_RECONCILIATION_20260928.md) preserves the earlier V1 witness for its completed readings. This crosswalk is analytical routing; it does not copy source transcripts into Git or substitute the refreshed source wording into V1 readings.

For any new source-facing claim, follow `story_id` → `<canonical_path>` relative to the pinned generation (the value already begins with `02_CANONICAL_STORIES/`) → scene/utterance/choice or message ID → `03_STRUCTURED_DATA/*.jsonl` → the record's `raw_group_ids`, `source_paths`, `source_sha256` and source commit → the immutable raw upstream snapshot recorded by `00_MANIFESTS/SOURCE_MANIFEST.json`. `03_STRUCTURED_DATA/stories.jsonl` supplies the authoritative per-object source class and canonical path for this generation. The supplemental CSV records the global witness once through this document rather than repeating it in every row. Its `canonical_path` and SHA-256 preserve exact per-object recovery; `stories.jsonl` at the pinned generation retains raw group IDs, raw table paths/hashes, person/variant joins and release metadata. The whole-phase audit records that inventory hash and selection scope. Removing repeated columns changes neither an object ID nor an admission decision. The `10_READING_INDEXES/STORIES/<CLASS>.md` files are navigation only. A derived person/relationship bundle is a reversible projection, not another primary story witness. The [event index](BLUE_ARCHIVE_EVENT_ANALYTICAL_PRIORITY_INDEX.md) carries all 1,010 event story IDs.

## 1. Complete class inventory at the pinned generation

Counts are canonical **story objects**, not raw rows, distinct people or completed analytical readings. They total **4,864** and were checked against `03_STRUCTURED_DATA/stories.jsonl` and the 4,864-row `00_MANIFESTS/RELEASE_CHRONOLOGY.csv`.

| Source type | Objects | Canonical route under `02_CANONICAL_STORIES/` | Release dates present | Current analytical state and strongest initial use |
|---|---:|---|---:|---|
| `main` | 480 | `MAIN/` | 0 | 480 admitted readings, 26 checkpoints; institutional/crisis and some ordinary evidence. Older readings retain their declared V1 text witness. |
| `group` | 65 | `GROUP/` | 0 | 65 ADMITTED with limits; complete group-content intake closed; club routine, peer hierarchy, work and ordinary disagreements. |
| `event` | 1,010 | `EVENT/EVENT_*/` | 1,010 | 43 ADMITTED with limits,967 AVAILABLE_NOT_REVIEWED; continuity, cross-school, seasonal, comic and ordinary contexts all eligible for reading. |
| `bond` | 1,161 | `BOND/` | 1,161 | 30 ADMITTED with limits,1131 unadmitted; bounded private/Sensei dyads, ordinary preferences, and relationship-specific self-presentation. |
| `momotalk` | 1,161 | `MOMOTALK/` | 1,161 | 30 ADMITTED with limits,1131 unadmitted; message rhythm, initiation, alternate replies and bond prefaces. |
| `character_data` | 511 | `CHARACTER_DATA/` | 283 | 12 ADMITTED with limits,499 unadmitted; contextual written language, profile and variant conditions; no performed-voice claim. |
| `mini` | 46 | `MINI/` | 0 | Available, unadmitted; short scenes require their own continuity and speaker check. |
| `special_operation` | 96 | `SPECIAL_OPERATION/` | 0 | Available, unadmitted; classify mode and continuity before claim use. |
| `unclassified_scenario` | 334 | `UNCLASSIFIED_SCENARIO/` | 0 | Available, unadmitted; source-class identity remains unresolved, so no automatic narrative use. |

**Release order is documentary order.** `RELEASE_CHRONOLOGY.csv` marks `story_chronology_confidence=unresolved` for **all 4,864** rows. An event release date, event number, bond episode number, file order or main crosswalk order does not establish an in-universe relation among those source classes. Scene-specific before/after claims require explicit narrative anchors or a corroborated later presupposition, with counterevidence recorded. When order remains open, a scene can still support contextual repertoire, ordinary pleasure, voice or relationship behavior; it cannot silently create a state-transition edge. Main-story knowledge boundaries remain those of the source-facing readings and checkpoints.

All 1,010 event objects have an unresolved overarching `event_title_jp` field (`missing_in_current_raw`); their stable `event_content_id` and story IDs remain the route. Twenty-eight event story objects have two `event_contexts` in the structured record, preserving repeat/release contexts under one canonical reading. No event episode has been duplicated merely for its second context. Participant IDs are metadata leads; speaker attribution, role, variant and full cast must be checked in the complete story. `PERSON_REGISTRY.csv`, `STUDENT_VARIANT_REGISTRY.csv` and `STORY_SPEAKER_REGISTRY.csv` provide identity/mapping routes with their recorded uncertainty.

`00_MANIFESTS/MOMOTALK_BOND_CROSSWALK.csv` has **1,189 source-field links**, covering **1,161 distinct MomoTalk thread IDs** and **1,161 distinct bond story IDs**. The join is `AcademyMessanger.FavorScheduleId → AcademyFavorSchedule.ScenarioSriptGroupId`. It routes related material; it does not imply every message has the same audience knowledge as the bond encounter or that a possible Sensei reply occurred alongside its alternatives.

## 2. First retrieval questions, not admissions

The [current readiness audit](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_CHARACTER_RECONSTRUCTION_BOOTSTRAP_AUDIT.md#33-current-cycle005-readiness-reassessment--2026-10-01) retains bounded Yuuka/Serika design leads and now incorporates all65 complete group readings. Earlier pilot suggestions are historical retrieval decisions. Remaining private/event material needs its own actual content acceptance; no broad package or model is certified by metadata.

The following rows preserve the initial retrieval questions. Current accepted pools and remaining obligations are recorded in the admission summary and exact object crosswalk.

| Question | Available source routes identified by person metadata | What still needs inspection |
|---|---|---|
| Yuuka: council, club and low-pressure contrast | 8 `group` objects (`BA:group:1201`–`:1203`, `:1502`–`:1503`, `:3101`–`:3103`); 31 event objects across event IDs 806, 810, 811, 817, 818, 821, 822, 823, 842; 14 bond and 14 MomoTalk objects linked to `BA_PERSON_YUUKA`. | Complete selected stories, actual speaker/role, ordinary versus emergency setting, event chronology, variant and Sensei-branch limits. Game-club events 825/854 have other Pavane people in metadata; they do not establish Yuuka's appearance. |
| Serika: work, scarcity, peer and Sensei reciprocity | `BA:group:2101` and `:2102`; 57 event objects across IDs 809, 810, 814, 815, 818, 821, 822, 823, 841, 860; 13 bond and 13 MomoTalk objects linked to `BA_PERSON_SERIKA`. | Full service and peer contexts, independent desires/pleasure, recurring versus situational refusal, story order and alternative Sensei replies. |

The first bounded group review packet is the complete two-part `BA:group:2101`/`:2102` Abydos committee group story for the Serika ordinary/peer question. The first inquiry-led event packet is `EVENT_816` (all 17 objects) to test ordinary-context coverage beyond the main-arc cast. The independent rotation begins with `EVENT_80000` (nine separate person-specific objects); `EVENT_814` (all 16 objects) follows for an Abydos/Serika comparison. Yuuka's alternative first group packet is the complete `BA:group:1201`–`:1203` C&C sequence; later Veritas or other group selections must include episode 1 when their numbered sequence begins before the Yuuka-linked episode. These were initial selection decisions. GROUP2101–2102, GROUP1201–1203, GROUP1501–1503, EVENT816 and EVENT80000 are now accepted in cycle 001; cycle002 accepts Serika31 and GROUP1101–1104; cycle005 accepts all16 EVENT814 objects.

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

Current supplemental admission: **180 objects —65 group,43 event,30 bond,30 MomoTalk and12 character_data, ADMIT_WITH_LIMITS**. [Cycle005](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_005_CHECKPOINT.md) owns the latest accepted questions, evidence and exclusions. The [3682-row object crosswalk](BLUE_ARCHIVE_SUPPLEMENTAL_SOURCE_TO_ANALYSIS_CROSSWALK.csv) records exact IDs, hashes, requirements, reading/admission routes, priority and separate chronology. [Scope extension001](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_PRINCIPAL_SCOPE_EXTENSION_001.md) adds227 private obligations and three mini leads, without new private or mini content admission. Mini/special-operation/unclassified remain unadmitted. Source refresh still requires identity/provenance reconciliation; already exposed comparisons are retrospective.

## Cycle002 admission and attribution — 2026-10-01

[35 newly accepted objects](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_002_CHECKPOINT.md):4 group,13 bond,13 complete MomoTalk files and5 character_data. Three Serika variants and two exact OriginalCharacterId costume joins remain distinct;229 written records include one blank title. Full-thread postscenes and Answer alternatives are material. Event packaging is not event plot. Current total69; no event-class admission added here.

[Fourteen raw-command receipts](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_SUPPLEMENTAL_ATTRIBUTION_REVIEW_20261001.md) show that canonical speaker labels can select an earlier actor-only command rather than a later text-bearing actor. Preserve Japanese wording, IDs/hashes and raw witnesses; distinguish derivation from upstream error. The two EVENT818 samples are diagnostic only and do not change event admission. Rebuild/refresh is a separate governed operation.

## Cycle003 admission and source-mode review — 2026-10-01

[31 newly accepted group objects](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_003_CHECKPOINT.md) brings the current total to100. Fourteen full packet arguments preserve raw display/text actor receipts, independent or local-relative ordering, quote/report/video layers, branch responses and private audience. Marina/Yuzu empty joins and locally explicit Nodoka costume remain separate from registry repair. Automatic forecast output and collective voices retain their modes, not extra biographies. All3452 tracked IDs/canonical hashes remain intact.22 group,984 event,1148 bond,1148 MomoTalk and506 data objects are still unadmitted; principal-required remainders differ from full-class totals as recorded by the Phase2 audit.

## Cycle004 admission and scope extension — 2026-10-01

[22 newly accepted group objects](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_004_CHECKPOINT.md) closes complete group-content intake at65/65 and brings supplemental admission to122. All22 have full contributor/parent literary review, exact hash checks and consequential Japanese/raw/choice tests. Embedded fiction, quoted ns formulations, independent vignettes, unjoined named identities, separate anonymous roles and automated/collective modes retain their limits. All3452 prior CSV identities/hashes are preserved; [scope extension001](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_PRINCIPAL_SCOPE_EXTENSION_001.md) adds230 separately unadmitted rows for3682 total. Full-class unadmitted remainders are0 group/984 event/1148 bond/1148 MomoTalk/506 data. Required principal remainders are narrower:1048 bond/1048 MomoTalk/429 data. Group intake alone does not complete an arc or wholePhase2.

## Cycle005 admission and separate source contexts — 2026-10-01

[Exact58-source acceptance](../02%20Sequential%20Readings/BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_005_CHECKPOINT.md) admits17 bond/17 full MomoTalk/7 written-data and17 event objects, for180 total. The3682 tracked identities/canonical hashes and allunaffectedCSV rows stay exact. Full-class unadmitted totals are0G/967E/1131B/1131M/499D; principal-required remainders1031B/1031M/422D differ from those full-class totals. Mini/special/unclassified remain unadmitted.

Local holiday, yesterday/this-morning, crash, middle-school and explicit remembered-event relations have their actual scope. EVENT814 packet order and2022 release, EVENT8072021 release, family episode numbers and costume release gates do not place acts on the main timeline. One canonical object retains all its original contexts. Raw art employee/vendors do not gain baseball-Rei appearance credit; written costume repetitions and source-form changes do not multiply independent observations. Audio, photo pixels, total chronology and unprinted outcomes remain outside acceptance.

The [accepted group relevance audit](../08%20Audits%20and%20Manifests/BLUE_ARCHIVE_PHASE2_GROUP_ARC_RELEVANCE_AUDIT.md) supplies the question-specific all12-arc reuse/absence route for the existing65 group admissions, without a new source count, source chronology or full-arc completion.
