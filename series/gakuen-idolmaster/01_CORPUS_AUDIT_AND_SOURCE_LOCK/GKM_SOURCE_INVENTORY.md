---
title: "Gakuen Idolmaster V2 Source Inventory"
project: "Gakuen Idolmaster / 学園アイドルマスター"
document_type: "source inventory"
version: "2.1"
phase: "0 - Corpus Audit and Source Lock"
source_lock: "GAKUMAS V2 Source Lock 1.0"
created: "2026-08-13"
status: "canonical Phase 0 artifact; external-evidence boundary clarified 2026-08-15"
---

# GKM SOURCE INVENTORY

## 0. Purpose

This document records the corpus actually available to the V2 project before literary interpretation begins. It is an inventory, not a thematic reading. Counts here are source-control facts for **GAKUMAS V2 SOURCE LOCK 1.0**.

## 1. Locked corpus identity

- Primary source root: `../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-fdad681a6d81f903`
- Upstream repository: `DreamGallery/Campus-adv-txts`
- Upstream description: Gakuen Idolmaster original ADV text
- Source commit: `00d150a069a3ffa723a1ff264752ba242024caad`
- Source revision file value: `32`
- Archive generation time: `2026-08-02T22:21:04Z`
- Raw transcript files copied: **3,777**
- Extracted `[message]` lines: **93,924**
- Dialogue-only derived files: **3,403**
- Analysis root: `..`

This is a frozen **2026-08-02 source snapshot**. It must not be described as a continuously current mirror of the live service.

## 2. Source layers

| Layer | Location | Role | Authority |
| --- | --- | --- | --- |
| A1 | `transcripts_raw/` | Byte-preserved ADV scripts after folder placement; dialogue, ruby, voice IDs, BGM, camera, motion, facial state, layout, branch labels | Governing textual/staging source |
| A2 | `transcripts_dialogue_only/` | Readable `[message]` extraction | Convenience derivative; check A1 for exactness |
| A3 | `analysis_bundles/` | Analysis-oriented views: 13 character bundles, shared/common, event tranches, support-card tranches, reports | Primary ingestion layer; not unique evidence identity |
| Context | `00_context/` | Provenance, manifest, category counts, code map, sorting schema | Corpus-control metadata |

Canonical evidence identity is a **source script**, not a bundle appearance. Default identity: `original_name + sorted_relative_path`.

## 3. Category inventory

| category | files | message lines | character | shared | event/support | unassigned | no dialogue extract |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cidol | 321 | 13,616 | 321 | 0 | 0 | 0 | 0 |
| csprt | 498 | 9,777 | 0 | 0 | 498 | 0 | 0 |
| dear | 462 | 31,438 | 462 | 0 | 0 | 0 | 0 |
| event | 136 | 8,507 | 0 | 0 | 136 | 0 | 0 |
| gasha | 36 | 0 | 0 | 0 | 0 | 36 | 36 |
| live | 106 | 194 | 106 | 0 | 0 | 0 | 0 |
| musics | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| pevent | 1101 | 13,716 | 1073 | 28 | 0 | 0 | 0 |
| pgrowth | 39 | 150 | 39 | 0 | 0 | 0 | 0 |
| presult | 13 | 23 | 0 | 0 | 0 | 13 | 0 |
| produce | 86 | 13 | 0 | 0 | 0 | 86 | 75 |
| pstep | 217 | 0 | 0 | 197 | 0 | 20 | 217 |
| pstory | 608 | 11,626 | 588 | 19 | 0 | 1 | 7 |
| pweek | 37 | 0 | 0 | 37 | 0 | 0 | 37 |
| startup | 31 | 215 | 26 | 5 | 0 | 0 | 0 |
| tower | 1 | 20 | 0 | 0 | 0 | 1 | 0 |
| tutorial | 17 | 104 | 0 | 17 | 0 | 0 | 0 |
| unit | 66 | 4,525 | 0 | 66 | 0 | 0 | 0 |
| warmup | 1 | 0 | 0 | 0 | 0 | 1 | 1 |

Totals: **3,777 files / 93,924 message lines**.

Observations relevant to later analysis:

- `dear` is the single largest dialogue category at **31,438 lines** and must be treated as a major characterization layer, not optional texture.
- `pevent`, `cidol`, and `pstory` are also large enough to require source-family separation during character reading.
- `csprt` and numbered `event` stories remain deliberately outside the complete-character bundles; they therefore form required later ensemble/relational passes.
- `gasha`, `pstep`, `pweek`, `musics`, and `warmup` contain no extracted message lines in this snapshot, although their raw ADV/system content remains preserved.

## 4. Character bundle coverage

There are **13 dedicated complete-character bundles**. `nasr` (Asari Neo / 根緒 亜紗里) exists in the character-code map but has no dedicated complete-character bundle; her material must be reconstructed from shared and cross-character sources.

| code | character | Japanese | pstory f | pstory l | pevent f | pevent l | cidol f | cidol l | dear f | dear l | total f | total lines |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| amao | Mao Arimura | 有村 麻央 | 46 | 1036 | 83 | 988 | 24 | 1056 | 38 | 2756 | 204 | 5,875 |
| atbm | Tsubame Amaya | 雨夜 燕 | 42 | 804 | 81 | 1104 | 9 | 365 | 28 | 2093 | 173 | 4,407 |
| fktn | Kotone Fujita | 藤田 ことね | 42 | 884 | 81 | 1017 | 27 | 1142 | 28 | 1666 | 192 | 4,748 |
| hmsz | Misuzu Hataya | 秦谷 美鈴 | 46 | 715 | 83 | 1056 | 18 | 701 | 37 | 2508 | 197 | 5,018 |
| hrnm | Rinami Himesaki | 姫崎 莉波 | 46 | 877 | 83 | 1043 | 30 | 1293 | 38 | 2805 | 210 | 6,057 |
| hski | Saki Hanami | 花海 咲季 | 48 | 864 | 83 | 974 | 33 | 1300 | 38 | 2440 | 215 | 5,616 |
| hume | Ume Hanami | 花海 佑芽 | 46 | 944 | 83 | 1062 | 24 | 1106 | 38 | 2685 | 204 | 5,841 |
| jsna | Sena Juo | 十王 星南 | 42 | 719 | 81 | 1000 | 21 | 876 | 27 | 1880 | 184 | 4,515 |
| kcna | China Kuramoto | 倉本 千奈 | 46 | 995 | 83 | 1029 | 27 | 1097 | 38 | 2398 | 208 | 5,558 |
| kllj | Lilja Katsuragi | 葛城 リーリヤ | 46 | 886 | 83 | 1005 | 30 | 1331 | 38 | 2529 | 210 | 5,791 |
| shro | Hiro Shinosawa | 篠澤 広 | 46 | 979 | 83 | 1072 | 27 | 1096 | 38 | 2471 | 207 | 5,653 |
| ssmk | Sumika Shiun | 紫雲 清夏 | 46 | 893 | 83 | 1023 | 24 | 1116 | 38 | 2613 | 204 | 5,682 |
| ttmr | Temari Tsukimura | 月村 手毬 | 46 | 876 | 83 | 1045 | 27 | 1137 | 38 | 2594 | 207 | 5,686 |

No warning field is populated for these 13 current bundle rows.

## 5. Shared and ensemble bundle inventory

### Shared bundle

| bundle | source files | message lines |
| --- | --- | --- |
| 01_tutorial.dialogue.txt | 17 | 104 |
| 02_unit_story.dialogue.txt | 66 | 4,525 |
| 03_story_events_001-005.dialogue.txt | 25 | 1,650 |
| 04_all_shared_common.dialogue.txt | 294 | 550 |

### Dedicated story-event bundles

| bundle | source files | message lines |
| --- | --- | --- |
| event_001-005.dialogue.txt | 27 | 1,670 |
| event_006-012.dialogue.txt | 35 | 2,409 |
| event_013-020.dialogue.txt | 40 | 2,570 |
| event_021-plus.dialogue.txt | 34 | 1,858 |

The shared `03_story_events_001-005` view is not independent evidence. It is a 25-source subset of the dedicated 27-source `event_001-005` view. See `GKM_DEDUP_AND_EXCEPTION_AUDIT.md`.

## 6. Produce-story macro structure visible in the raw tree

The raw `01_produce_main_story/` tree contains:

- `series_001` - initial Produce Story era with failure/normal/true-labeled and other route-state variants;
- `series_002` - N.I.A. / NEXT IDOL AUDITION era;
- `series_003` - H.I.F.-era material, including shared/common and REVERSI-specific paths.

Series 3 coverage is uneven by character in this snapshot. That is a **live-service source-state fact**, not evidence that omitted characters do not exist in the franchise or lack significance. Phase 1 must reconstruct actual story-state availability rather than infer chronology from directory symmetry.

## 7. Unassigned and no-dialogue-extract inventory

The validation reports contain:

- **159 ambiguous/unassigned files**;
- **374 files without dialogue-only extracts**.

Crucial adjudication: **all 374 no-dialogue-extract rows have `message_count = 0`.** The report label therefore does not mean 374 lost dialogue scenes. It means no dialogue derivative was created because no `[message]` lines were present. Raw files remain part of A1 and may still carry staging/system information.

The 159 unassigned files contain only **26 dialogue-bearing files / 70 message lines**:

| category | unassigned files | dialogue-bearing unassigned |
| --- | --- | --- |
| gasha | 36 | 0 |
| musics | 1 | 0 |
| presult | 13 | 13 |
| produce | 86 | 11 |
| pstep | 20 | 0 |
| pstory | 1 | 1 |
| tower | 1 | 1 |
| warmup | 1 | 0 |

All 26 dialogue-bearing exceptions have been explicitly adjudicated in the Phase 0 exception audit.

## 8. Known scope boundaries

Source Lock 1.0 is strong for:

- Japanese dialogue and script-language analysis;
- branching Produce Story reconstruction;
- character and Producer routes;
- Dear Idol;
- communications;
- produce events;
- support cards;
- numbered story events;
- unit story;
- institutional/system exposition;
- script-visible BGM/voice/camera/motion metadata.

It is **not** an exhaustive audiovisual mirror. Actual vocal delivery, mixing, musical texture, choreography, MV editing, card art, and rendered performance require separately supplied AV evidence. Those sources enter the dedicated audiovisual registry, not the frozen textual Source Lock 1.0 by default.

## 9. V1/V2 corpus discontinuity

Legacy analysis must not be assumed to have used the same source snapshot. The exported V1 conversation records earlier corpus counts and earlier character-bundle sizes; for example, its Saki analysis used a 191-source / 4,582-line bundle, while Source Lock 1.0 contains **215 sources / 5,616 lines** for Saki. This makes some V1 work both interpretively preliminary and **source-incomplete relative to V2**.

## 10. Phase 0 inventory conclusion

The corpus is internally coherent enough to support the V2 project, provided that:

1. bundle appearances are deduplicated to source-script identity;
2. outcome branches are not flattened into chronology;
3. the 26 dialogue-bearing unassigned exceptions are manually promoted/indexed;
4. zero-message raw scripts remain available for staging/system checks;
5. legacy analysis remains outside the evidence hierarchy;
6. later live-service additions are versioned rather than silently merged.


## 11. External paratext and creator-commentary extension

Source Lock 1.0 remains **unchanged**: 3,777 raw ADV scripts / 93,924 messages at the frozen 2026-08-02 revision. Official web pages and interviews are **not merged into that source lock** and do not alter its counts or hashes.

External evidence is versioned separately in:

`GKM_OFFICIAL_PARATEXT_AND_CREATOR_COMMENTARY_REGISTER.md`

The external hierarchy is:

- `S2` official canonical paratext;
- `S3` credited creator/staff commentary;
- `S4` reliable secondary reporting;
- `S5` discovery/reference sources.

The current first integration tranche concerns Hatsuboshi institutional taxonomy and the player Producer's educational position. It records the official `プロデューサー科` terminology, creator-stated `初星学園専門大学` placement, rejected teacher/classmate concepts, and Producer Course production-history rationale.

This extension follows the rule **primary-source priority does not mean primary-source exclusivity** while keeping narrative reality governed by S1.
