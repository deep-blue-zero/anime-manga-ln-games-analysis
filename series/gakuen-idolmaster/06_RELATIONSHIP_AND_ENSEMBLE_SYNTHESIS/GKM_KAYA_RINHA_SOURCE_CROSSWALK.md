---
series: GKM
artifact_type: crosswalk
analytical_role: distributed_character_source_crosswalk
scope: KAYA_RINHA
generation: V2
status: canonical
source_boundary: "GAKUMAS V2 Source Lock 1.0 — exhaustive distributed-source entity-resolution pass for Kaya Rinha / 賀陽燐羽 across playable-route bundles, numbered events, support stories, Unit Story, and shared/common negative controls; 118 deduplicated unique canonical source objects"
source_lock: "GAKUMAS V2 Source Lock 1.0"
source_commit: "00d150a069a3ffa723a1ff264752ba242024caad"
source_revision: 32
governing_method: "GAKUEN_IDOLMASTER_FULL_CORPUS_ANALYTICAL_METHOD_V2.md v2.2"
governing_architecture: "GAKUEN_IDOLMASTER_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE_V2.md v2.4"
governing_continuity: "GKM_CONTINUITY_AND_STORY_STATE_MAP.md v2.1"
created: "2026-08-24"
last_updated: "2026-08-24 — direct-speaker parser correction after evidence-matrix preflight audit"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
---

# GKM KAYA RINHA SOURCE CROSSWALK

## 0. Purpose, authority, and non-dossier rule

This is the first mandatory artifact in the Phase-6 distributed reconstruction of **Kaya Rinha / 賀陽燐羽**. It is a source-routing document, not a personality monograph. Its job is to answer, before interpretation: **where does Rinha actually exist in Source Lock 1.0, whose story is each appearance embedded in, what kind of presence is it, what continuity envelope governs it, and which objects can support direct claims about Rinha herself?**

Architecture v2.4 requires this crosswalk because Rinha does not possess a normal playable-character source bundle. Her evidence is distributed through other characters’ routes, events, support cards, and unit-history references. The governing rule is therefore:

> **Reconstruct Rinha from intersections, not reflections. Temari’s Rinha, Misuzu’s Rinha, Saki’s Rinha, remembered Rinha, and Rinha’s own words/actions are distinct evidence surfaces.**

This document is **canonical for source discovery and provenance**. It is **not** the authority for a definitive Rinha personality claim. That authority cannot exist until `GKM_KAYA_RINHA_EVIDENCE_MATRIX.md` separates direct from mediated claims and the later `GKM_KAYA_RINHA_CHARACTER_DOSSIER.md` synthesizes only what survives that audit.

### 0.1 Crosswalk result at a glance

- **118 unique canonical source objects** survive deduplication.
- **92 objects** contain an explicit retrieval alias (`燐羽`, `賀陽`, or the childhood vocative form `りんはぁ`).
- **26 objects** are retained as **SyngUp-only contextual objects** even though Rinha is not named.
- **43 objects contain Rinha’s own dialogue**, totaling **621 logical Rinha dialogue messages/utterances** in the dialogue-only envelopes. A matrix-preflight audit corrected an earlier parser undercount that missed tagged speaker forms such as `燐羽 speaker=...:`.
- The 118 source objects contain **6,709 total source-envelope messages**. **This is not a count of 6,709 Rinha-evidence lines**; it is only the sum of all messages in the containing objects.
- Rinha-own direct-speaking evidence is distributed across **Temari, Misuzu, Saki, Ume, numbered events, support stories, and idol communications**. Tsubame’s recovered route objects are observer/context evidence only.
- No separately acquired Rinha-named or `krnh`-named MP4 was discoverable in the current Drive AV search, but raw ADV metadata proves voiced Rinha assets exist and are individually recoverable.

### 0.2 Parser correction — 2026-08-24

The initial crosswalk release reported **28 direct-speaking objects / 339 Rinha lines**. Before construction of the evidence matrix, all 118 matched source bodies were re-audited by the displayed speaker field. The original counter recognized plain `燐羽:` forms but missed many metadata-tagged forms such as `燐羽 speaker=img_adv_speaker_krnh_000-005:` and `燐羽 ... isInner=true:`. The corrected result is **43 direct-speaking objects / 621 logical Rinha dialogue messages**.

This correction changes **classification and direct-message counts only**. The canonical source boundary remains **118/118 unique objects**, with no source added, removed, or duplicated. Fifteen Dear objects previously mislabeled as observer-only are now correctly marked `R-DIRECT`; `RINHA-XW-041` additionally contains direct Rinha interiority. The evidence matrix must use these corrected values.

## 1. Entity resolution and retrieval aliases

| field | frozen crosswalk value | use |
| --- | --- | --- |
| canonical analytical name | `Kaya Rinha / 賀陽燐羽` | corpus-facing identity |
| displayed speaker name | `燐羽` | dialogue extraction and Japanese quote retrieval |
| surname/full-name alias | `賀陽`, `賀陽燐羽` | narration/report search |
| childhood panic/vocative alias | `りんはぁ` | retrieval alias only; do not normalize it into ordinary address style |
| internal actor code | `krnh` | raw ADV actor/model/voice-asset resolution |
| raw character-setting token | `gkgt` | source-routing token observed in `overwritecharactersetting`; institutional interpretation remains separate |
| voiced asset stem | `..._krnh-*` | confirms scene-level voice recoverability |
| central historical unit | `SyngUp!` | indirect context search; never equate every SyngUp mention with a direct Rinha claim |
| external institutional association | Gokugetsu-linked / `gkgt` routing | relevant contextual tag; exact biographical chronology must be adjudicated in the matrix |

Raw A1 inspection of `transcripts_raw/04_support_card_stories/support_series_3/story_0097/part_01.txt` resolves `actorId=krnh`, `name=燐羽`, `mdl_chr_krnh-*`, `setting=gkgt`, and voice stems such as `sud_vo_adv_csprt-3-0097_01_krnh-001`. This is stronger entity-resolution evidence than filename inference.

## 2. Deduplication and evidence-envelope protocol

The raw corpus contains multiple representations of the same underlying scene: A1 raw ADV, A2 dialogue-only extraction, complete-character bundles, category bundles, support/event tranche bundles, and analytical artifacts. This crosswalk counts **underlying canonical source objects once**. Bundle appearances are retrieval conveniences, not additional evidence.

### 2.1 Authority order

1. **A1 raw ADV path** — exact canonical source object and staging/voice-asset authority.
2. **A2 dialogue-only source object** — convenient textual reading surface for speaker/line analysis.
3. **A3 aggregate bundle** — ingestion/search surface only; never counted as a separate Rinha appearance when it embeds an A1/A2 object already listed.
4. **Analytical artifacts/ledgers** — interpretation/routing surfaces; never counted as primary-source rows.

### 2.2 Inclusion rule

An object is included when at least one of the following is true:
- Rinha speaks or acts directly;
- Rinha is explicitly named or remembered;
- the object contains a distinctive Rinha retrieval alias;
- the object contains SyngUp context necessary to interpret a neighboring Rinha claim, even if Rinha herself is not named;
- the object is a unit/event/support context whose absence would make the Rinha/SyngUp evidence envelope misleading.

### 2.3 Evidence labels used by the next phase

| label | meaning |
| --- | --- |
| `R-DIRECT` | Rinha’s own spoken words in the source object |
| `R-ACTION` | Rinha’s behavior/staging is directly represented |
| `R-LING` | useful evidence for Rinha’s lexical/register model |
| `R-AV` | high-value scene where vocal/performance realization is materially discriminating |
| `OTHER-REPORT` | another character or narrator reports/interprets Rinha |
| `MEMORY` | Rinha occurs inside a remembered scene or internalized relational model |
| `REL-INFERENCE` | relationship/unit context supports only a relational inference, not a person-level fact |
| `META` | structural/unit/institutional context rather than direct characterization |
| `OPEN` | requires matrix-level adjudication before promotion |

## 3. Coverage summary

### 3.1 By source family

| source family | unique objects | direct-speaking objects | continuity default |
| --- | ---: | ---: | --- |
| Produce main story | 8 | 0 | C3 route/branch |
| Produce events | 3 | 0 | C3 route/branch |
| Idol communications | 18 | 3 | C2/C4 modular |
| Dear Idol | 74 | 35 | C1 @ host Dear route |
| Numbered events | 5 | 1 | C1 internal / C2 global |
| Support stories | 8 | 4 | C2/C4 support |
| Unit Story | 2 | 0 | C1 @ U1 |
| **TOTAL** | **118** | **43** | mixed; row-level authority governs |

### 3.2 By primary host/viewpoint

| host/viewpoint | unique objects | direct-speaking objects | Rinha-direct messages | analytical caution |
| --- | ---: | ---: | ---: | --- |
| Temari | 37 | 13 | 225 | largest observer envelope and largest direct Rinha envelope; never treat Temari’s account of dependence/blame as Rinha self-report |
| Misuzu | 31 | 10 | 132 | strong triadic/unit history plus direct conflict/training evidence; distinguish Misuzu’s care philosophy from Rinha’s |
| Saki | 13 | 8 | 119 | contains unusually strong Rinha autobiographical material, but D-SAKI remains route-bounded |
| Ume | 16 | 7 | 109 | substantial direct fan-handoff/training/sister-model evidence; late route state is not a substitute for SyngUp chronology |
| Tsubame | 6 | 0 | 0 | observer/context only in recovered rows; no Rinha direct dialogue in this host envelope |
| Ensemble | 13 | 5 | 36 | events/support can supply cross-route ordinary/public evidence; continuity remains event/support scoped |
| Unit Story | 2 | 0 | 0 | SyngUp context only; no Rinha-name/direct row |

### 3.3 Presence-mode distribution

| presence mode | objects | promotion ceiling before matrix |
| --- | ---: | --- |
| `DISCUSSED_OR_REMEMBERED` | 48 | OTHER-REPORT / MEMORY; person-level motive remains unproven |
| `UNIT_CONTEXT_ONLY` | 26 | REL-INFERENCE / META only |
| `DIRECT_SPEECH` | 37 | R-DIRECT; still continuity-bounded |
| `MEMORY_WITH_DIRECT_SPEECH_ACTION` | 1 | R-DIRECT + R-ACTION inside memory; verify AV where discriminating |
| `AUTOMATIC_VOCATIVE_MEMORY` | 1 | observer attachment evidence only; not Rinha behavior |
| `MEMORY_WITH_DIRECT_SPEECH` | 1 | R-DIRECT inside memory; chronology/source-host caveat retained |
| `PRESENT_INTERIORITY_AND_SPEECH` | 2 | direct Rinha interiority plus speech; continuity scope still governs |
| `PRESENT_TRIAD_SPEECH` | 1 | direct present relational evidence |
| `PRESENT_UME_SPEECH` | 1 | direct present cross-network evidence |

## 4. Full unique-source crosswalk — 118 canonical objects

**Table rule:** each row represents one deduplicated underlying canonical source object. `messages` is the size of the entire source envelope. `R-msgs` counts logical dialogue messages attributed to Rinha in the extraction; embedded game-script line breaks inside one message do not increment the count.

| ID | host | family | original source name | exact A1 path | messages | R-msgs | continuity | presence mode | evidence labels | relation/context tags | public retrieval nomenclature | AV routing |
| --- | --- | --- | --- | --- | ---: | ---: | --- | --- | --- | --- | --- | --- |
| `RINHA-XW-001` | Temari | Produce main story | `adv_pstory_002_ttmr_after-audition-a-normal-03.txt` | `transcripts_raw/01_produce_main_story/series_002/ttmr=Temari_Tsukimura/after-audition-a-normal-03.txt` | 15 | 0 | C3 route/branch | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU | 月村手毬 Produce Story S002 / after-audition-a-normal-03 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-002` | Temari | Produce main story | `adv_pstory_002_ttmr_after-audition-final-normal-01.txt` | `transcripts_raw/01_produce_main_story/series_002/ttmr=Temari_Tsukimura/after-audition-final-normal-01.txt` | 14 | 0 | C3 route/branch | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, SYNGUP | 月村手毬 Produce Story S002 / after-audition-final-normal-01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-003` | Temari | Produce main story | `adv_pstory_002_ttmr_ending-normal-02.txt` | `transcripts_raw/01_produce_main_story/series_002/ttmr=Temari_Tsukimura/ending-normal-02.txt` | 8 | 0 | C3 route/branch | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU | 月村手毬 Produce Story S002 / ending-normal-02 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-004` | Ume | Produce main story | `adv_pstory_002_hume_after-audition-a-normal-03.txt` | `transcripts_raw/01_produce_main_story/series_002/hume=Ume_Hanami/after-audition-a-normal-03.txt` | 22 | 0 | C3 route/branch | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | UME | 花海佑芽 Produce Story S002 / after-audition-a-normal-03 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-005` | Ume | Produce main story | `adv_pstory_002_hume_before-audition-a-normal-01.txt` | `transcripts_raw/01_produce_main_story/series_002/hume=Ume_Hanami/before-audition-a-normal-01.txt` | 21 | 0 | C3 route/branch | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | UME, GOKUGETSU | 花海佑芽 Produce Story S002 / before-audition-a-normal-01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-006` | Ume | Produce main story | `adv_pstory_002_hume_before-audition-b-normal-01.txt` | `transcripts_raw/01_produce_main_story/series_002/hume=Ume_Hanami/before-audition-b-normal-01.txt` | 13 | 0 | C3 route/branch | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | UME, SHION, GOKUGETSU | 花海佑芽 Produce Story S002 / before-audition-b-normal-01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-007` | Tsubame | Produce main story | `adv_pstory_002_atbm_after-audition-b-normal-02.txt` | `transcripts_raw/01_produce_main_story/series_002/atbm=Tsubame_Amaya/after-audition-b-normal-02.txt` | 15 | 0 | C3 route/branch | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TSUBAME | 雨夜燕 Produce Story S002 / after-audition-b-normal-02 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-008` | Tsubame | Produce main story | `adv_pstory_002_atbm_before-audition-b-normal-01.txt` | `transcripts_raw/01_produce_main_story/series_002/atbm=Tsubame_Amaya/before-audition-b-normal-01.txt` | 26 | 0 | C3 route/branch | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TSUBAME, GEKKA, GOKUGETSU | 雨夜燕 Produce Story S002 / before-audition-b-normal-01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-009` | Temari | Produce events | `adv_pevent_001_ttmr_school_007.txt` | `transcripts_raw/02_produce_events/event_001/ttmr=Temari_Tsukimura/school_007.txt` | 18 | 0 | C3 route/branch | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | SYNGUP | 月村手毬 Produce Event 001 / school_007 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-010` | Misuzu | Produce events | `adv_pevent_002_hmsz_sales_4-003-01.txt` | `transcripts_raw/02_produce_events/event_002/hmsz=Misuzu_Hataya/sales_4-003-01.txt` | 9 | 0 | C3 route/branch | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | MISUZU, SYNGUP | 秦谷美鈴 Produce Event 002 / sales_4-003-01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-011` | Misuzu | Produce events | `adv_pevent_002_hmsz_sales_4-003-02.txt` | `transcripts_raw/02_produce_events/event_002/hmsz=Misuzu_Hataya/sales_4-003-02.txt` | 9 | 0 | C3 route/branch | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | MISUZU, SYNGUP | 秦谷美鈴 Produce Event 002 / sales_4-003-02 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-012` | Temari | Idol communications | `adv_cidol-ttmr-3-007_02.txt` | `transcripts_raw/03_idol_communications/ttmr=Temari_Tsukimura/rank_3/episode_007/part_02.txt` | 43 | 0 | C2/C4 modular | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SYNGUP | 月村手毬 アイドルコミュ EP007-02 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-013` | Temari | Idol communications | `adv_cidol-ttmr-3-007_03.txt` | `transcripts_raw/03_idol_communications/ttmr=Temari_Tsukimura/rank_3/episode_007/part_03.txt` | 33 | 0 | C2/C4 modular | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU | 月村手毬 アイドルコミュ EP007-03 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-014` | Temari | Idol communications | `adv_cidol-ttmr-3-009_01.txt` | `transcripts_raw/03_idol_communications/ttmr=Temari_Tsukimura/rank_3/episode_009/part_01.txt` | 37 | 0 | C2/C4 modular | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SYNGUP, HIF | 月村手毬 アイドルコミュ EP009-01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-015` | Temari | Idol communications | `adv_cidol-ttmr-3-009_02.txt` | `transcripts_raw/03_idol_communications/ttmr=Temari_Tsukimura/rank_3/episode_009/part_02.txt` | 38 | 4 | C2/C4 modular | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SYNGUP | 月村手毬 アイドルコミュ EP009-02 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-016` | Temari | Idol communications | `adv_cidol-ttmr-3-009_03.txt` | `transcripts_raw/03_idol_communications/ttmr=Temari_Tsukimura/rank_3/episode_009/part_03.txt` | 55 | 0 | C2/C4 modular | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SYNGUP | 月村手毬 アイドルコミュ EP009-03 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-017` | Temari | Idol communications | `adv_cidol-ttmr-3-011_01.txt` | `transcripts_raw/03_idol_communications/ttmr=Temari_Tsukimura/rank_3/episode_011/part_01.txt` | 43 | 0 | C2/C4 modular | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, SAKI, SYNGUP | 月村手毬 アイドルコミュ EP011-01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-018` | Temari | Idol communications | `adv_cidol-ttmr-3-011_03.txt` | `transcripts_raw/03_idol_communications/ttmr=Temari_Tsukimura/rank_3/episode_011/part_03.txt` | 56 | 0 | C2/C4 modular | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, SYNGUP | 月村手毬 アイドルコミュ EP011-03 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-019` | Temari | Idol communications | `adv_cidol-ttmr-3-016_01.txt` | `transcripts_raw/03_idol_communications/ttmr=Temari_Tsukimura/rank_3/episode_016/part_01.txt` | 41 | 0 | C2/C4 modular | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SYNGUP | 月村手毬 アイドルコミュ EP016-01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-020` | Temari | Idol communications | `adv_cidol-ttmr-3-018_02.txt` | `transcripts_raw/03_idol_communications/ttmr=Temari_Tsukimura/rank_3/episode_018/part_02.txt` | 49 | 0 | C2/C4 modular | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI | 月村手毬 アイドルコミュ EP018-02 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-021` | Misuzu | Idol communications | `adv_cidol-hmsz-3-005_01.txt` | `transcripts_raw/03_idol_communications/hmsz=Misuzu_Hataya/rank_3/episode_005/part_01.txt` | 52 | 0 | C2/C4 modular | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SYNGUP | 秦谷美鈴 アイドルコミュ EP005-01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-022` | Misuzu | Idol communications | `adv_cidol-hmsz-3-005_02.txt` | `transcripts_raw/03_idol_communications/hmsz=Misuzu_Hataya/rank_3/episode_005/part_02.txt` | 49 | 3 | C2/C4 modular | `DIRECT_SPEECH` | R-DIRECT, R-LING | MISUZU, SYNGUP | 秦谷美鈴 アイドルコミュ EP005-02 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-023` | Misuzu | Idol communications | `adv_cidol-hmsz-3-005_03.txt` | `transcripts_raw/03_idol_communications/hmsz=Misuzu_Hataya/rank_3/episode_005/part_03.txt` | 36 | 0 | C2/C4 modular | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | MISUZU, SYNGUP | 秦谷美鈴 アイドルコミュ EP005-03 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-024` | Misuzu | Idol communications | `adv_cidol-hmsz-3-010_02.txt` | `transcripts_raw/03_idol_communications/hmsz=Misuzu_Hataya/rank_3/episode_010/part_02.txt` | 40 | 0 | C2/C4 modular | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | MISUZU, UME, SENA, SYNGUP | 秦谷美鈴 アイドルコミュ EP010-02 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-025` | Misuzu | Idol communications | `adv_cidol-hmsz-3-010_03.txt` | `transcripts_raw/03_idol_communications/hmsz=Misuzu_Hataya/rank_3/episode_010/part_03.txt` | 60 | 0 | C2/C4 modular | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | MISUZU, UME, SENA, SYNGUP | 秦谷美鈴 アイドルコミュ EP010-03 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-026` | Misuzu | Idol communications | `adv_cidol-hmsz-3-015_02.txt` | `transcripts_raw/03_idol_communications/hmsz=Misuzu_Hataya/rank_3/episode_015/part_02.txt` | 39 | 0 | C2/C4 modular | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | MISUZU, UME, SENA, RINAMI, SYNGUP | 秦谷美鈴 アイドルコミュ EP015-02 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-027` | Saki | Idol communications | `adv_cidol-hski-3-017_03.txt` | `transcripts_raw/03_idol_communications/hski=Saki_Hanami/rank_3/episode_017/part_03.txt` | 44 | 11 | C2/C4 modular | `DIRECT_SPEECH` | R-DIRECT, R-LING | SAKI, SENA, SYNGUP | 花海咲季 アイドルコミュ EP017-03 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-028` | Ume | Idol communications | `adv_cidol-hume-3-006_03.txt` | `transcripts_raw/03_idol_communications/hume=Ume_Hanami/rank_3/episode_006/part_03.txt` | 76 | 0 | C2/C4 modular | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | SAKI, UME | 花海佑芽 アイドルコミュ EP006-03 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-029` | Tsubame | Idol communications | `adv_cidol-atbm-3-012_02.txt` | `transcripts_raw/03_idol_communications/atbm=Tsubame_Amaya/rank_3/episode_012/part_02.txt` | 70 | 0 | C2/C4 modular | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | MISUZU, TSUBAME, GEKKA, SYNGUP | 雨夜燕 アイドルコミュ EP012-02 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-030` | Temari | Dear Idol | `adv_dear_ttmr_010-01.txt` | `transcripts_raw/05_dear_idol/dear/dear_ttmr_010-01.txt` | 30 | 0 | C1 @ D-TEMARI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, KUROI, SHION, GEKKA, GOKUGETSU, HIF | 月村手毬 親愛度コミュ / dear_ttmr_010-01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-031` | Temari | Dear Idol | `adv_dear_ttmr_004.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_004.txt` | 79 | 0 | C1 @ D-TEMARI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SYNGUP | 月村手毬 親愛度コミュ 004 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-032` | Temari | Dear Idol | `adv_dear_ttmr_007.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_007.txt` | 63 | 0 | C1 @ D-TEMARI | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SYNGUP | 月村手毬 親愛度コミュ 007 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-033` | Temari | Dear Idol | `adv_dear_ttmr_008.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_008.txt` | 79 | 0 | C1 @ D-TEMARI | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SYNGUP | 月村手毬 親愛度コミュ 008 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-034` | Temari | Dear Idol | `adv_dear_ttmr_009.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_009.txt` | 82 | 0 | C1 @ D-TEMARI | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SYNGUP | 月村手毬 親愛度コミュ 009 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-035` | Temari | Dear Idol | `adv_dear_ttmr_011.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_011.txt` | 56 | 0 | C1 @ D-TEMARI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SYNGUP, GOKUGETSU | 月村手毬 親愛度コミュ 011 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-036` | Temari | Dear Idol | `adv_dear_ttmr_014.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_014.txt` | 72 | 22 | C1 @ D-TEMARI | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, KUROI, SHION, SYNGUP, GOKUGETSU | 月村手毬 親愛度コミュ 014 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-037` | Temari | Dear Idol | `adv_dear_ttmr_015.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_015.txt` | 53 | 18 | C1 @ D-TEMARI | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SYNGUP | 月村手毬 親愛度コミュ 015 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-038` | Temari | Dear Idol | `adv_dear_ttmr_016.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_016.txt` | 74 | 37 | C1 @ D-TEMARI | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, KUROI, GOKUGETSU | 月村手毬 親愛度コミュ 016 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-039` | Temari | Dear Idol | `adv_dear_ttmr_017.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_017.txt` | 74 | 26 | C1 @ D-TEMARI | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SYNGUP, HIF | 月村手毬 親愛度コミュ 017 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-040` | Temari | Dear Idol | `adv_dear_ttmr_018.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_018.txt` | 60 | 0 | C1 @ D-TEMARI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SHION, GOKUGETSU | 月村手毬 親愛度コミュ 018 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-041` | Temari | Dear Idol | `adv_dear_ttmr_020.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_020.txt` | 57 | 7 | C1 @ D-TEMARI | `PRESENT_INTERIORITY_AND_SPEECH` | R-DIRECT, R-LING, R-AV | TEMARI, MISUZU, SAKI, SYNGUP, GOKUGETSU | 月村手毬 親愛度コミュ 020 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-042` | Temari | Dear Idol | `adv_dear_ttmr_023.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_023.txt` | 107 | 0 | C1 @ D-TEMARI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SENA, SYNGUP, HIF | 月村手毬 親愛度コミュ 023 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-043` | Temari | Dear Idol | `adv_dear_ttmr_024.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_024.txt` | 82 | 32 | C1 @ D-TEMARI | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SENA, GOKUGETSU, HIF | 月村手毬 親愛度コミュ 024 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-044` | Temari | Dear Idol | `adv_dear_ttmr_025.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_025.txt` | 80 | 20 | C1 @ D-TEMARI | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, KUROI, SYNGUP, GOKUGETSU, HIF | 月村手毬 親愛度コミュ 025 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-045` | Temari | Dear Idol | `adv_dear_ttmr_026.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_026.txt` | 84 | 17 | C1 @ D-TEMARI | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, KUROI, SHION, SYNGUP, GOKUGETSU | 月村手毬 親愛度コミュ 026 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-046` | Temari | Dear Idol | `adv_dear_ttmr_027.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_027.txt` | 65 | 2 | C1 @ D-TEMARI | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SENA, SYNGUP, GOKUGETSU, HIF | 月村手毬 親愛度コミュ 027 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-047` | Temari | Dear Idol | `adv_dear_ttmr_028.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_028.txt` | 61 | 0 | C1 @ D-TEMARI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SENA, SYNGUP, HIF | 月村手毬 親愛度コミュ 028 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-048` | Temari | Dear Idol | `adv_dear_ttmr_030.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_030.txt` | 63 | 18 | C1 @ D-TEMARI | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SAKI | 月村手毬 親愛度コミュ 030 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-049` | Temari | Dear Idol | `adv_dear_ttmr_031.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_031.txt` | 62 | 0 | C1 @ D-TEMARI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, SAKI, SENA, HIF | 月村手毬 親愛度コミュ 031 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-050` | Temari | Dear Idol | `adv_dear_ttmr_032.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_032.txt` | 79 | 9 | C1 @ D-TEMARI | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SAKI, UME, SENA, SYNGUP, HIF | 月村手毬 親愛度コミュ 032 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-051` | Temari | Dear Idol | `adv_dear_ttmr_033.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_033.txt` | 66 | 0 | C1 @ D-TEMARI | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SAKI, SENA, SYNGUP | 月村手毬 親愛度コミュ 033 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-052` | Temari | Dear Idol | `adv_dear_ttmr_034.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_034.txt` | 59 | 0 | C1 @ D-TEMARI | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SENA, SYNGUP | 月村手毬 親愛度コミュ 034 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-053` | Temari | Dear Idol | `adv_dear_ttmr_035.txt` | `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_035.txt` | 83 | 13 | C1 @ D-TEMARI | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SAKI, SENA, SHION | 月村手毬 親愛度コミュ 035 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-054` | Misuzu | Dear Idol | `adv_dear_hmsz_002.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_002.txt` | 71 | 0 | C1 @ D-MISUZU | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU | 秦谷美鈴 親愛度コミュ 002 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-055` | Misuzu | Dear Idol | `adv_dear_hmsz_005.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_005.txt` | 63 | 0 | C1 @ D-MISUZU | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SYNGUP | 秦谷美鈴 親愛度コミュ 005 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-056` | Misuzu | Dear Idol | `adv_dear_hmsz_011.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_011.txt` | 57 | 0 | C1 @ D-MISUZU | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | MISUZU, SYNGUP, GOKUGETSU | 秦谷美鈴 親愛度コミュ 011 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-057` | Misuzu | Dear Idol | `adv_dear_hmsz_012.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_012.txt` | 62 | 18 | C1 @ D-MISUZU | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SYNGUP, GOKUGETSU | 秦谷美鈴 親愛度コミュ 012 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-058` | Misuzu | Dear Idol | `adv_dear_hmsz_013.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_013.txt` | 47 | 0 | C1 @ D-MISUZU | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SYNGUP | 秦谷美鈴 親愛度コミュ 013 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-059` | Misuzu | Dear Idol | `adv_dear_hmsz_014.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_014.txt` | 53 | 13 | C1 @ D-MISUZU | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SAKI, UME | 秦谷美鈴 親愛度コミュ 014 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-060` | Misuzu | Dear Idol | `adv_dear_hmsz_015.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_015.txt` | 55 | 0 | C1 @ D-MISUZU | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | MISUZU, UME, SYNGUP, GOKUGETSU | 秦谷美鈴 親愛度コミュ 015 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-061` | Misuzu | Dear Idol | `adv_dear_hmsz_016.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_016.txt` | 80 | 27 | C1 @ D-MISUZU | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SYNGUP | 秦谷美鈴 親愛度コミュ 016 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-062` | Misuzu | Dear Idol | `adv_dear_hmsz_017.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_017.txt` | 80 | 0 | C1 @ D-MISUZU | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SYNGUP | 秦谷美鈴 親愛度コミュ 017 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-063` | Misuzu | Dear Idol | `adv_dear_hmsz_018.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_018.txt` | 43 | 0 | C1 @ D-MISUZU | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SHION, SYNGUP | 秦谷美鈴 親愛度コミュ 018 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-064` | Misuzu | Dear Idol | `adv_dear_hmsz_019.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_019.txt` | 54 | 0 | C1 @ D-MISUZU | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SYNGUP | 秦谷美鈴 親愛度コミュ 019 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-065` | Misuzu | Dear Idol | `adv_dear_hmsz_020.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_020.txt` | 78 | 19 | C1 @ D-MISUZU | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SYNGUP, GOKUGETSU, HIF | 秦谷美鈴 親愛度コミュ 020 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-066` | Misuzu | Dear Idol | `adv_dear_hmsz_021.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_021.txt` | 63 | 2 | C1 @ D-MISUZU | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SENA, SYNGUP, GOKUGETSU, HIF | 秦谷美鈴 親愛度コミュ 021 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-067` | Misuzu | Dear Idol | `adv_dear_hmsz_022.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_022.txt` | 62 | 0 | C1 @ D-MISUZU | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | MISUZU, SENA, SYNGUP | 秦谷美鈴 親愛度コミュ 022 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-068` | Misuzu | Dear Idol | `adv_dear_hmsz_023.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_023.txt` | 60 | 16 | C1 @ D-MISUZU | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SENA, SYNGUP, HIF | 秦谷美鈴 親愛度コミュ 023 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-069` | Misuzu | Dear Idol | `adv_dear_hmsz_024.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_024.txt` | 88 | 27 | C1 @ D-MISUZU | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SAKI, UME, TSUBAME, SENA, HIF | 秦谷美鈴 親愛度コミュ 024 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-070` | Misuzu | Dear Idol | `adv_dear_hmsz_025.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_025.txt` | 82 | 1 | C1 @ D-MISUZU | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SYNGUP, HIF | 秦谷美鈴 親愛度コミュ 025 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-071` | Misuzu | Dear Idol | `adv_dear_hmsz_030.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_030.txt` | 70 | 0 | C1 @ D-MISUZU | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SENA, SYNGUP, HIF | 秦谷美鈴 親愛度コミュ 030 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-072` | Misuzu | Dear Idol | `adv_dear_hmsz_031.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_031.txt` | 94 | 0 | C1 @ D-MISUZU | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SENA, SYNGUP, HIF | 秦谷美鈴 親愛度コミュ 031 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-073` | Misuzu | Dear Idol | `adv_dear_hmsz_032.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_032.txt` | 60 | 0 | C1 @ D-MISUZU | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SYNGUP, HIF | 秦谷美鈴 親愛度コミュ 032 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-074` | Misuzu | Dear Idol | `adv_dear_hmsz_034.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_034.txt` | 67 | 6 | C1 @ D-MISUZU | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SENA, HIF | 秦谷美鈴 親愛度コミュ 034 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-075` | Misuzu | Dear Idol | `adv_dear_hmsz_035.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_035.txt` | 47 | 0 | C1 @ D-MISUZU | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SYNGUP | 秦谷美鈴 親愛度コミュ 035 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-076` | Misuzu | Dear Idol | `adv_dear_hmsz_037.txt` | `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_037.txt` | 70 | 0 | C1 @ D-MISUZU | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | MISUZU, SYNGUP | 秦谷美鈴 親愛度コミュ 037 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-077` | Saki | Dear Idol | `adv_dear_hski_014.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_014.txt` | 71 | 18 | C1 @ D-SAKI | `DIRECT_SPEECH` | R-DIRECT, R-LING | SAKI, UME, SYNGUP, GOKUGETSU | 花海咲季 親愛度コミュ 014 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-078` | Saki | Dear Idol | `adv_dear_hski_015.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_015.txt` | 23 | 0 | C1 @ D-SAKI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | SAKI, UME | 花海咲季 親愛度コミュ 015 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-079` | Saki | Dear Idol | `adv_dear_hski_016.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_016.txt` | 55 | 14 | C1 @ D-SAKI | `DIRECT_SPEECH` | R-DIRECT, R-LING | SAKI, UME | 花海咲季 親愛度コミュ 016 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-080` | Saki | Dear Idol | `adv_dear_hski_017.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_017.txt` | 41 | 1 | C1 @ D-SAKI | `DIRECT_SPEECH` | R-DIRECT, R-LING | SAKI, UME | 花海咲季 親愛度コミュ 017 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-081` | Saki | Dear Idol | `adv_dear_hski_024.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_024.txt` | 81 | 13 | C1 @ D-SAKI | `DIRECT_SPEECH` | R-DIRECT, R-LING | SAKI, UME, SENA, HIF | 花海咲季 親愛度コミュ 024 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-082` | Saki | Dear Idol | `adv_dear_hski_025.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_025.txt` | 106 | 20 | C1 @ D-SAKI | `DIRECT_SPEECH` | R-DIRECT, R-LING | MISUZU, SAKI, UME, SENA, HIF | 花海咲季 親愛度コミュ 025 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-083` | Saki | Dear Idol | `adv_dear_hski_026.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_026.txt` | 60 | 26 | C1 @ D-SAKI | `DIRECT_SPEECH` | R-DIRECT, R-LING | SAKI, UME, SENA, HIF | 花海咲季 親愛度コミュ 026 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-084` | Saki | Dear Idol | `adv_dear_hski_027.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_027.txt` | 83 | 0 | C1 @ D-SAKI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | SAKI, SENA, HIF | 花海咲季 親愛度コミュ 027 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-085` | Saki | Dear Idol | `adv_dear_hski_028.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_028.txt` | 72 | 0 | C1 @ D-SAKI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | SAKI, UME, SENA, HIF | 花海咲季 親愛度コミュ 028 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-086` | Saki | Dear Idol | `adv_dear_hski_029.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_029.txt` | 87 | 0 | C1 @ D-SAKI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | SAKI, UME, TSUBAME, SENA, SYNGUP | 花海咲季 親愛度コミュ 029 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-087` | Saki | Dear Idol | `adv_dear_hski_030.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_030.txt` | 69 | 0 | C1 @ D-SAKI | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | SAKI, UME, TSUBAME, SENA | 花海咲季 親愛度コミュ 030 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-088` | Saki | Dear Idol | `adv_dear_hski_034.txt` | `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_034.txt` | 49 | 16 | C1 @ D-SAKI | `DIRECT_SPEECH` | R-DIRECT, R-LING | SAKI, TSUBAME, SENA, HIF | 花海咲季 親愛度コミュ 034 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-089` | Ume | Dear Idol | `adv_dear_hume_012.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_012.txt` | 79 | 14 | C1 @ D-UME | `DIRECT_SPEECH` | R-DIRECT, R-LING | MISUZU, SAKI, UME, SYNGUP, GOKUGETSU | 花海佑芽 親愛度コミュ 012 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-090` | Ume | Dear Idol | `adv_dear_hume_013.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_013.txt` | 72 | 12 | C1 @ D-UME | `DIRECT_SPEECH` | R-DIRECT, R-LING | SAKI, UME | 花海佑芽 親愛度コミュ 013 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-091` | Ume | Dear Idol | `adv_dear_hume_014.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_014.txt` | 50 | 0 | C1 @ D-UME | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | SAKI, UME | 花海佑芽 親愛度コミュ 014 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-092` | Ume | Dear Idol | `adv_dear_hume_015.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_015.txt` | 63 | 17 | C1 @ D-UME | `DIRECT_SPEECH` | R-DIRECT, R-LING | MISUZU, SAKI, UME | 花海佑芽 親愛度コミュ 015 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-093` | Ume | Dear Idol | `adv_dear_hume_016.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_016.txt` | 60 | 16 | C1 @ D-UME | `DIRECT_SPEECH` | R-DIRECT, R-LING | SAKI, UME, KUROI, GOKUGETSU | 花海佑芽 親愛度コミュ 016 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-094` | Ume | Dear Idol | `adv_dear_hume_017.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_017.txt` | 59 | 0 | C1 @ D-UME | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | SAKI, UME | 花海佑芽 親愛度コミュ 017 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-095` | Ume | Dear Idol | `adv_dear_hume_019.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_019.txt` | 63 | 1 | C1 @ D-UME | `DIRECT_SPEECH` | R-DIRECT, R-LING | SAKI, UME, SENA, HIF | 花海佑芽 親愛度コミュ 019 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-096` | Ume | Dear Idol | `adv_dear_hume_021.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_021.txt` | 81 | 0 | C1 @ D-UME | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | SAKI, UME, SENA, HIF | 花海佑芽 親愛度コミュ 021 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-097` | Ume | Dear Idol | `adv_dear_hume_024.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_024.txt` | 95 | 27 | C1 @ D-UME | `DIRECT_SPEECH` | R-DIRECT, R-LING | TEMARI, MISUZU, SAKI, UME, SENA, HIF | 花海佑芽 親愛度コミュ 024 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-098` | Ume | Dear Idol | `adv_dear_hume_025.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_025.txt` | 83 | 0 | C1 @ D-UME | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | SAKI, UME, SENA, HIF | 花海佑芽 親愛度コミュ 025 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-099` | Ume | Dear Idol | `adv_dear_hume_027.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_027.txt` | 103 | 0 | C1 @ D-UME | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | SAKI, UME, SENA, HIF | 花海佑芽 親愛度コミュ 027 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-100` | Ume | Dear Idol | `adv_dear_hume_029.txt` | `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_029.txt` | 64 | 22 | C1 @ D-UME | `DIRECT_SPEECH` | R-DIRECT, R-LING | SAKI, UME, SENA | 花海佑芽 親愛度コミュ 029 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-101` | Tsubame | Dear Idol | `adv_dear_atbm_012.txt` | `transcripts_raw/05_dear_idol/atbm=Tsubame_Amaya/dear_012.txt` | 89 | 0 | C1 @ D-TSUBAME | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | MISUZU, UME, TSUBAME, SENA, KUROI, SHION, GEKKA, GOKUGETSU | 雨夜燕 親愛度コミュ 012 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-102` | Tsubame | Dear Idol | `adv_dear_atbm_013.txt` | `transcripts_raw/05_dear_idol/atbm=Tsubame_Amaya/dear_013.txt` | 97 | 0 | C1 @ D-TSUBAME | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | MISUZU, TSUBAME, SENA, GEKKA | 雨夜燕 親愛度コミュ 013 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-103` | Tsubame | Dear Idol | `adv_dear_atbm_017.txt` | `transcripts_raw/05_dear_idol/atbm=Tsubame_Amaya/dear_017.txt` | 53 | 0 | C1 @ D-TSUBAME | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | MISUZU, TSUBAME, SENA, SHION, GEKKA, GOKUGETSU | 雨夜燕 親愛度コミュ 017 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-104` | Ensemble | Numbered events | `adv_event_005_main-03.txt` | `transcripts_raw/06_story_events/event_005/main-03.txt` | 72 | 0 | C1 internal / C2 global | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, TSUBAME, SENA, RINAMI, SYNGUP | イベントストーリー EVENT_005 / main-03 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-105` | Ensemble | Numbered events | `adv_event_008_main-02.txt` | `transcripts_raw/06_story_events/event_008/main-02.txt` | 72 | 0 | C1 internal / C2 global | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SAKI, SYNGUP | イベントストーリー EVENT_008 / main-02 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-106` | Ensemble | Numbered events | `adv_event_016_main-03.txt` | `transcripts_raw/06_story_events/event_016/main-03.txt` | 62 | 5 | C1 internal / C2 global | `MEMORY_WITH_DIRECT_SPEECH_ACTION` | MEMORY, R-DIRECT, R-ACTION, R-LING | TEMARI, SAKI | イベントストーリー EVENT_016 / main-03 | P0_AV_QUEUE; Rinha voiced memory |
| `RINHA-XW-107` | Ensemble | Numbered events | `adv_event_023_main-01.txt` | `transcripts_raw/06_story_events/event_023/main-01.txt` | 39 | 0 | C1 internal / C2 global | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU, SYNGUP | イベントストーリー EVENT_023 / main-01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-108` | Ensemble | Numbered events | `adv_event_023_main-04.txt` | `transcripts_raw/06_story_events/event_023/main-04.txt` | 49 | 0 | C1 internal / C2 global | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SYNGUP | イベントストーリー EVENT_023 / main-04 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-109` | Ensemble | Support stories | `adv_csprt-3-0021_02.txt` | `transcripts_raw/04_support_card_stories/support_series_3/story_0021/part_02.txt` | 20 | 0 | C2/C4 support | `AUTOMATIC_VOCATIVE_MEMORY` | MEMORY, OTHER-REPORT | TEMARI, MISUZU | サポートコミュ story_0021 part_02 | P0_AV_QUEUE; Temari vocative only |
| `RINHA-XW-110` | Ensemble | Support stories | `adv_csprt-3-0032_01.txt` | `transcripts_raw/04_support_card_stories/support_series_3/story_0032/part_01.txt` | 20 | 0 | C2/C4 support | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | MISUZU, UME, TSUBAME, SENA, RINAMI, SYNGUP | サポートコミュ story_0032 part_01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-111` | Ensemble | Support stories | `adv_csprt-3-0058_01.txt` | `transcripts_raw/04_support_card_stories/support_series_3/story_0058/part_01.txt` | 18 | 0 | C2/C4 support | `DISCUSSED_OR_REMEMBERED` | OTHER-REPORT | TEMARI, MISUZU | サポートコミュ story_0058 part_01 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-112` | Ensemble | Support stories | `adv_csprt-3-0096_02.txt` | `transcripts_raw/04_support_card_stories/support_series_3/story_0096/part_02.txt` | 20 | 2 | C2/C4 support | `MEMORY_WITH_DIRECT_SPEECH` | MEMORY, R-DIRECT, R-LING | TEMARI, MISUZU | サポートコミュ story_0096 part_02 | VOICED_IN_ADV; dedicated Rinha AV mapping not yet frozen |
| `RINHA-XW-113` | Ensemble | Support stories | `adv_csprt-3-0097_01.txt` | `transcripts_raw/04_support_card_stories/support_series_3/story_0097/part_01.txt` | 19 | 10 | C2/C4 support | `PRESENT_INTERIORITY_AND_SPEECH` | R-DIRECT, R-ACTION, R-LING, R-AV | TEMARI, MISUZU, SAKI, KUROI, HIF | サポートコミュ story_0097 part_01 | P0_AV_QUEUE; Rinha voiced |
| `RINHA-XW-114` | Ensemble | Support stories | `adv_csprt-3-0097_02.txt` | `transcripts_raw/04_support_card_stories/support_series_3/story_0097/part_02.txt` | 19 | 10 | C2/C4 support | `PRESENT_TRIAD_SPEECH` | R-DIRECT, R-ACTION, R-LING, R-AV | TEMARI, MISUZU | サポートコミュ story_0097 part_02 | P0_AV_QUEUE; Rinha voiced |
| `RINHA-XW-115` | Ensemble | Support stories | `adv_csprt-3-0097_03.txt` | `transcripts_raw/04_support_card_stories/support_series_3/story_0097/part_03.txt` | 20 | 9 | C2/C4 support | `PRESENT_UME_SPEECH` | R-DIRECT, R-ACTION, R-LING, R-AV | UME | サポートコミュ story_0097 part_03 | VOICED_IN_ADV; add to Rinha AV baseline candidate |
| `RINHA-XW-116` | Ensemble | Support stories | `adv_csprt-3-0102_03.txt` | `transcripts_raw/04_support_card_stories/support_series_3/story_0102/part_03.txt` | 20 | 0 | C2/C4 support | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, SAKI, UME, SYNGUP | サポートコミュ story_0102 part_03 | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-117` | Unit Story | Unit Story | `adv_unit_01-04_13.txt` | `transcripts_raw/12_unit_story/unit_01/episode_04/part_13.txt` | 71 | 0 | C1 @ U1 | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, SAKI, UME, SYNGUP, HIF | ユニットストーリー Re;IRIS episode_04 part_13 / SyngUp! context | NO_RINHA_VOICE; host-scene AV may exist |
| `RINHA-XW-118` | Unit Story | Unit Story | `adv_unit_01-04_17.txt` | `transcripts_raw/12_unit_story/unit_01/episode_04/part_17.txt` | 73 | 0 | C1 @ U1 | `UNIT_CONTEXT_ONLY` | REL-INFERENCE, META | TEMARI, MISUZU, SAKI, SENA, RINAMI, SYNGUP | ユニットストーリー Re;IRIS episode_04 part_17 / SyngUp! context | NO_RINHA_VOICE; host-scene AV may exist |

## 5. Direct-evidence priority map

The corrected crosswalk contains **43 direct-speaking objects / 621 logical Rinha dialogue messages**. The evidence matrix should not weight them equally. The following objects are the most discriminating for person-level reconstruction because they contain self-report, interiority, current-state action, care, aspiration, rivalry, ordinary behavior, or cross-network relations rather than only exposition.

| priority source | row | R-msgs | why it is discriminating | AV priority |
| --- | --- | ---: | --- | --- |
| `transcripts_raw/04_support_card_stories/support_series_3/story_0097/part_01.txt` | `RINHA-XW-113` | 10 | Present-tense Rinha interiority: changed relationship to H.I.F., public recognition, privacy request, and explicit future-return promise to a fan. | P0 |
| `transcripts_raw/04_support_card_stories/support_series_3/story_0097/part_02.txt` | `RINHA-XW-114` | 10 | Present Temari–Misuzu–Rinha triad, public attention, familiar blame/banter, and dissolution-live coordination. | P0 |
| `transcripts_raw/04_support_card_stories/support_series_3/story_0097/part_03.txt` | `RINHA-XW-115` | 9 | Present Rinha–Ume exchange: playful support plus direct admission of an unresolved worry she wants Ume’s song to affect. | P0 |
| `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_015.txt` | `RINHA-XW-037` | 18 | Direct denial of benevolent blame-absorption framing; breakup/public-fallout self-report and refusal to explain continued idol activity. | P0 |
| `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_016.txt` | `RINHA-XW-038` | 37 | Direct account of intended retirement, fan farewell, Kuroi recruitment, fan handoff, and Temari’s successful disruption of that closure plan. | P0 |
| `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_017.txt` | `RINHA-XW-039` | 26 | Direct promise/contract ethic, anti-restoration boundary, conditional return, and explicit willingness to become a target/model again. | P0/P1 |
| `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_020.txt` | `RINHA-XW-041` | 7 | Rare Dear-route Rinha interiority: remembers SyngUp’s founding reason as Temari/Misuzu being the only people who did not reject singing beside her. | P0 |
| `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_026.txt` | `RINHA-XW-083` | 26 | Long autobiographical disclosure: older-sister idol history, joy of pursuit, overtaking, self-blame, non-substitutability, and wish for a better Hanami ending. | P0 |
| `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_016.txt` | `RINHA-XW-061` | 27 | Rinha’s own claim that her idolhood ended with SyngUp and that she stands onstage for unfinished business; tests Misuzu’s interpretation of the wound. | P0 |
| `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_024.txt` | `RINHA-XW-069` | 27 | Direct professional ontology: she disqualifies herself as an idol for lack of consciousness/resolve/heart while remaining an active idol fan. | P0 |
| `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_016.txt` | `RINHA-XW-093` | 16 | Direct affection for Ume, fan handoff, counterfactual regret about the Hanami sisters arriving earlier, and reluctant vulnerability around her fans. | P0/P1 |
| `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_024.txt` | `RINHA-XW-097` | 27 | Fan stewardship plus explicit concern about Saki burning out and direct future-return language. | P0 |
| `transcripts_raw/05_dear_idol/hume=Ume_Hanami/dear_029.txt` | `RINHA-XW-100` | 22 | Rinha’s investment in Saki’s new song, urgency to help, acceptance of Ume’s boundary, and mentor/critic role. | P0/P1 |
| `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_024.txt` | `RINHA-XW-043` | 32 | Rivalry, nostalgia, embarrassment defense, dissolution-live boundary, and resumed training in one triadic scene. | P1 |
| `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_025.txt` | `RINHA-XW-044` | 20 | Explicit “no idol passion” assertion, promise-based motivation, and warning against inventing her causal history. | P0 |
| `transcripts_raw/05_dear_idol/ttmr=Temari_Tsukimura/dear_026.txt` | `RINHA-XW-045` | 17 | Temari overtakes Rinha; direct approval, concern, and renewed training despite prior closure language. | P1 |
| `transcripts_raw/05_dear_idol/hmsz=Misuzu_Hataya/dear_023.txt` | `RINHA-XW-068` | 16 | Abrasive praise, performance assessment, and accurate reading of Misuzu’s concealed frustration. | P1 |
| `transcripts_raw/05_dear_idol/hski=Saki_Hanami/dear_016.txt` | `RINHA-XW-079` | 14 | Rinha solicits Saki’s explanation for beating her, expresses envy, endorses unplated Saki, and shifts into tactile/playful intimacy. | P1 |
| `transcripts_raw/06_story_events/event_016/main-03.txt` | `RINHA-XW-106` | 5 | Childhood pedagogical pattern: provocation → concrete technique → persistence → experiential payoff. | P0/P1 |
| `transcripts_raw/03_idol_communications/ttmr=Temari_Tsukimura/rank_3/episode_009/part_02.txt` | `RINHA-XW-015` | 4 | First-meeting memory: pride in her idol older sister and explicit childhood desire to sing like her. | P1 |
| `transcripts_raw/04_support_card_stories/support_series_3/story_0096/part_02.txt` | `RINHA-XW-112` | 2 | Mundane food teasing/partial intake intervention; ordinary-life evidence whose care motive remains bounded. | P1 |
| `transcripts_raw/04_support_card_stories/support_series_3/story_0021/part_02.txt` | `RINHA-XW-109` | 0 | Rinha absent; Temari automatically calls `りんはぁ` during thunder panic. High-value observer attachment evidence, not Rinha behavior. | P0 relationship comparator |

### 5.1 What the direct pool can potentially answer

The direct pool is broad enough to test, rather than assume, at least the following dimensions:
- **aspiration and origin:** childhood admiration of an idol older sister and desire to sing;
- **self-blame and attachment:** the Saki-route autobiographical disclosure about chasing an older sister and seeing one’s own role in relational damage;
- **competition:** repeated direct rivalry with Temari, Saki, Ume, and others;
- **technical pedagogy:** direct training/correction of Temari or Misuzu;
- **care under abrasive language:** food regulation, stretching/training, fan handoff, concern about Saki, and explicit support requests;
- **fandom:** idol merchandise, live attendance, favorite-idol language, and reactions to other performers;
- **ordinary sociality:** teasing, food, waiting, public attention, embarrassment, jokes, and logistical coordination;
- **future orientation:** returning to idol activity, dissolution-live planning, new opponents, and later cross-network relations.

These are **questions the direct pool is capable of adjudicating**, not conclusions this crosswalk is authorized to freeze.

## 6. Observer matrix — keep the Rinhas separate until evidence adjudication

| evidence surface | source-object envelope | what it can safely establish | principal distortion risk | matrix instruction |
| --- | ---: | --- | --- | --- |
| **Rinha herself** | 43 direct-speaking objects | words, directly represented action, current/local motive, linguistic register; `story_0097/part_01` additionally exposes Rinha interiority | route/memory staging may still be local; direct speech is not automatically a cross-route invariant | highest person-level evidentiary weight; code claim as `R-DIRECT`/`R-ACTION`/`R-LING` with continuity |
| **Temari’s Rinha** | 37 objects; 13 direct-speaking | SyngUp history as Temari experiences it, teacher/rival/leader significance, attachment and rivalry | Temari’s shame, dependence, and self-worth filters causal attribution | separate reported motive from observed Rinha conduct |
| **Misuzu’s Rinha** | 31 objects; 10 direct-speaking | triadic dynamics, training, ordinary familiarity, mutual observation | Misuzu’s care/control philosophy can be projected onto Rinha | compare against Rinha’s own speech and Temari sources |
| **Saki’s Rinha** | 13 objects; 8 direct-speaking | unusually rich autobiographical Rinha disclosures, sister analogy, Project Stardust/rival collaboration | Saki-route continuity can make Rinha more accessible than elsewhere | retain `C1 @ D-SAKI`; use as self-report, not universal chronology |
| **Ume’s Rinha** | 16 objects; 7 direct-speaking | fan handoff, concern for Saki, support/teasing, current idol ambitions | late-route state may presuppose developments absent elsewhere | model as Ume-envelope relation state |
| **Tsubame’s Rinha** | 6 objects; 0 direct-speaking | external ranking/context and how Rinha figures in Tsubame-facing competition talk | entirely observer/contextual for Rinha in recovered set | no person-level Rinha claim without corroboration |
| **Ensemble Rinha** | 13 event/support objects; 5 direct-speaking | public memory, ordinary history, present triad interaction, cross-network relation with Ume | event/support chronology is modular; memory scenes can be compressed | retain event/support continuity tag and memory/present distinction |
| **SyngUp-only context** | 26 objects | unit history, public memory, or relational setting | highest risk of silently attributing unit-level facts to Rinha personally | `REL-INFERENCE` / `META` only until matrix corroboration |

## 7. Continuity segmentation

Rinha is unusually vulnerable to false biography because the same relationship cluster appears inside several route-conditioned futures. The crosswalk therefore freezes **routing**, not one universal timeline.

### 7.1 Non-collapse rules

- `D-TEMARI`, `D-MISUZU`, `D-SAKI`, `D-UME`, and Tsubame-route states remain distinct unless an invariant is independently supported across them.
- Cidol/support material may establish repeatable relational grammar without fixing one exact position in a universal calendar.
- Numbered events are longitudinally strong within their event context but must not be used to force every route endpoint into one biography.
- Unit Story SyngUp references establish a shared historical/social fact only to the degree the unit context itself is stable; they do not prove Rinha motive.
- Memories preserve both direct utterance evidence and a viewpoint/staging problem. `R-DIRECT` inside a memory is stronger than pure report, but weaker than present-tense Rinha interiority for current motive.
- `story_0097` is currently the strongest late support envelope because it moves from **Rinha interiority → present triad interaction → present Ume interaction** across three adjacent parts. It still does not authorize merging every Dear-route outcome around it.

## 8. Indirect-only evidence and negative controls

The crosswalk deliberately retains indirect context while preventing it from masquerading as direct characterization.

### 8.1 High-value indirect rows

- `event_005/main-03`: Rinha is discussed as a former SyngUp member/leader with strong fixed fans during succession/recruitment analysis. This establishes how other institutional actors classify her, not why she chose any action.
- `event_008/main-02`: public/fan SyngUp memory; useful for afterlife of the unit in audience consciousness.
- `event_023/main-01`: Temari internally predicts what Rinha would tell her about a Misuzu problem. This is evidence of Temari’s **internalized model of Rinha**, not direct Rinha advice.
- `support story_0021/part_02`: Temari’s thunder panic produces `りんはぁ……雷とめてぇ……`. This is high-value attachment/safety-reflex evidence about Temari and their relational history, but contains **zero Rinha behavior**.
- `support story_0058/part_01`: remembered three-person ramen routine adds ordinary-life SyngUp ecology.
- the 26 `UNIT_CONTEXT_ONLY` objects prevent SyngUp history from being under-specified while keeping their promotion ceiling low.

### 8.2 Negative controls completed

- **Support Series 1:** no Rinha/SyngUp row survived the entity/indirect search.
- **Support Series 2:** no Rinha/SyngUp row survived across all three architecture-defined bundles.
- **Shared/common dialogue surface:** explicit searches for `燐羽` and `SyngUp` returned no matching shared/common object.
- **Dedicated/named AV files:** current Drive searches for `krnh` + MP4 and `賀陽燐羽` + MP4 returned no separately acquired Rinha-named video object.
- The frozen inventory’s playable-route hosts are **Temari, Misuzu, Saki, Ume, and Tsubame**. No additional playable-route host contributes a unique row to this crosswalk after deduplication; other core characters may still encounter Rinha through the event/support ensemble rows listed here.

These are source-lock/Drive retrieval negatives, not metaphysical claims that no future game release or separately acquired AV source can contain Rinha.

## 9. Audiovisual routing and baseline warrant

### 9.1 What is already known

- Raw A1 scripts resolve Rinha as actor `krnh` and expose scene-level voiced assets (`..._krnh-*`).
- The corrected textual crosswalk has **43 direct-speaking source objects / 621 logical Rinha dialogue messages**, spanning multiple hosts and interaction registers.
- Existing AV infrastructure already contains P0 targets for `event_016/main-03`, the `story_0021/part_02` panic vocative, and `story_0097` present-tense material.
- No separately acquired Rinha-named/code-named MP4 was found by current Drive search, so **textual voice-asset availability must not be confused with completed AV acquisition**.

### 9.2 Warrant decision

**Dedicated Rinha AV baseline: `WARRANTED — DEFERRED UNTIL EVIDENCE MATRIX`.**

The warrant is positive because the direct textual corpus is large and varied enough that vocal delivery could materially distinguish competing hypotheses: playful cruelty versus hostile contempt; teasing affection versus ownership; professional severity versus performance; older-sister wounds versus competitive bravado; current vulnerability versus remembered persona. However, creating an AV artifact *before* the evidence matrix would violate proportional architecture by acquiring many redundant scenes.

The correct sequence is:

1. this crosswalk freezes the complete candidate pool;
2. `GKM_KAYA_RINHA_EVIDENCE_MATRIX.md` identifies claims whose truth materially depends on performance;
3. a targeted Rinha AV baseline/backfill may then be created from the smallest discriminating scene set;
4. the character dossier incorporates those AV findings without treating audiovisual intensity as license to override textual continuity.

### 9.3 Initial AV discrimination pool

- `support story_0097 parts 01–03` — interior monologue, public self-management, Temari/Misuzu banter, and Ume-facing softness/teasing.
- `event_016/main-03` — childhood pedagogical sharpness and transmitted technical care.
- `Temari Dear 024–027` — rivalry, dissolution-live framing, restored skill, closure, and residual attachment.
- `Saki Dear 026` — long autobiographical disclosure; essential for distinguishing performative mockery from exposed shame/grief.
- `Misuzu Dear 023–024` — training, praise, mockery, fandom, professional judgments, and ordinary conversational range.
- `Ume Dear 024/029` — fan responsibility, concern for Saki, admiration, motivation to return, and critic/mentor register.
- `support story_0021/part_02` — Rinha absent, but Temari’s voiced panic-vocative is a relationship-performance discriminator.

## 10. Public-facing retrieval nomenclature

Rinha lacks one convenient official/playable-character retrieval tree. Future searches should therefore combine **person + host + scene family**. Preferred query grammar:

- `賀陽燐羽 月村手毬 親愛度コミュ 024`
- `賀陽燐羽 秦谷美鈴 親愛度コミュ 024`
- `賀陽燐羽 花海咲季 親愛度コミュ 026`
- `賀陽燐羽 花海佑芽 親愛度コミュ 024`
- `賀陽燐羽 サポートコミュ story_0097`
- `賀陽燐羽 EVENT_016`
- `燐羽 SyngUp`
- internal acquisition/debug only: `krnh` + raw object/voice stem.

Do **not** route public retrieval by `krnh` alone; it is an internal corpus/asset key, not the preferred reader-facing name.

## 11. Evidence-matrix questions created by this crosswalk

The next artifact should adjudicate claims, not continue inventory expansion unless a demonstrable missing source is found. Priority questions are:

1. **What does Rinha want for herself?** Separate childhood older-sister imitation, promises to Temari, return-to-idol language, competition, and any independent ambition.
2. **How much of Rinha’s harshness is ordinary register, competitive play, technical pedagogy, defensive performance, or genuine hostility?**
3. **What forms of care does Rinha reliably perform?** Test food/body regulation, training, fan handoff, concern, support, and future coordination against counterevidence.
4. **What is the exact causal role of Rinha in SyngUp’s failure?** Separate Rinha’s own statements from Temari/Misuzu attribution and public blame.
5. **What is the older-sister history?** Use the Saki-route disclosure and Temari first-meeting memory without overgeneralizing unobserved family facts.
6. **When and why does Gokugetsu matter?** Distinguish raw setting/affiliation routing, Kuroi recruitment memory, competitive environment, and any unsupported chronology.
7. **Does Rinha want SyngUp restored?** Current evidence strongly distinguishes dissolution-live/future coordination from permanent-unit restoration, but the matrix must state the exact claim boundary.
8. **How does Rinha model Temari, Misuzu, Saki, and Ume differently?** Relationship-specific models must survive before any global personality adjective is promoted.
9. **What does Rinha do when competition is absent?** Ordinary food, fandom, teasing, waiting, public interaction, and support scenes are necessary counterweights to tournament behavior.
10. **Which apparent contradictions are continuity differences rather than personality contradictions?**
11. **Which person-level claims require AV adjudication?** Feed only those into the targeted Rinha AV acquisition/backfill.
12. **What remains genuinely open after the matrix?** The dossier must preserve unresolved gaps rather than force symmetry with playable-core monographs.

## 12. Crosswalk invariants and forbidden shortcuts

### 12.1 Safe source-level invariants

- Rinha is not a one-route hallucination: her source footprint spans multiple character hosts and ensemble surfaces.
- Direct Rinha evidence is substantial enough for a dedicated reconstruction, but mediated evidence still numerically dominates the crosswalk.
- Rinha is structurally tied to SyngUp history, but **SyngUp context is not interchangeable with Rinha personhood**.
- The corpus contains both competitive/high-pressure and ordinary/noncompetitive Rinha material.
- Later support material supplies rare present-tense Rinha evidence that is methodologically distinct from route memories/reports.
- Raw source metadata proves voiced `krnh` recoverability; a dedicated AV baseline is warranted but should be targeted after claim adjudication.

### 12.2 Forbidden shortcuts

- Do not infer a personality trait from a SyngUp-only row.
- Do not count the same raw object again because it appears in a complete-character bundle, category bundle, or analysis document.
- Do not merge all Dear routes into one chronological biography.
- Do not treat Temari’s fear/dependence or Misuzu’s interpretations as Rinha’s own motive.
- Do not treat Rinha’s direct remembered dialogue as identical in evidentiary function to present-tense interiority.
- Do not convert Gokugetsu association into an all-purpose ideological explanation.
- Do not use the 6,709 envelope-message total as a character dialogue count.
- Do not create a “definitive” dossier before the evidence matrix and targeted AV decision are complete.

## 13. Phase-6 handoff

### Completed by this artifact

- unique-source inventory frozen at **118 objects**;
- direct-speaking subset corrected and frozen at **43 objects / 621 logical Rinha dialogue messages**;
- host/viewpoint separation established;
- continuity envelope attached to every row;
- direct/report/memory/unit-context modes separated;
- public retrieval nomenclature established;
- raw entity code `krnh` and voice-asset routing confirmed;
- AV baseline warrant adjudicated as **WARRANTED, DEFERRED UNTIL MATRIX**;
- negative controls recorded for support Series 1–2, shared/common, and separately acquired named Rinha AV.

### Next canonical operation

**`GKM_KAYA_RINHA_EVIDENCE_MATRIX.md`**

The matrix should convert this crosswalk from **where the evidence is** into **what each source can actually prove**, using `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`, explicit counterevidence, viewpoint ownership, continuity class, and AV-discrimination requirements. The character dossier remains blocked until that matrix is complete.
