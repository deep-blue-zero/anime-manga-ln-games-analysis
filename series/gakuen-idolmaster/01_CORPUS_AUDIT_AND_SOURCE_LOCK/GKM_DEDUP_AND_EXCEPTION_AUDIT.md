---
title: "Gakuen Idolmaster V2 Deduplication and Exception Audit"
project: "Gakuen Idolmaster / 学園アイドルマスター"
document_type: "deduplication and exception audit"
version: "2.0"
phase: "0 - Corpus Audit and Source Lock"
source_lock: "GAKUMAS V2 Source Lock 1.0"
created: "2026-08-13"
status: "canonical Phase 0 artifact"
---

# GKM DEDUP AND EXCEPTION AUDIT

## 0. Purpose

This audit resolves two corpus-quality questions before close reading:

1. when multiple bundle views contain the same original script, how many evidence objects exist?;
2. do validation-report "missing" or "unassigned" files conceal meaningful dialogue outside the planned reading layers?

## 1. Deduplication rule

A source script is counted once under its canonical source identity:

`original_name + sorted_relative_path`

Bundle occurrences are **views**, not independent attestations. Repetition across a character bundle, shared bundle, event bundle, or later analytical package must not inflate evidence frequency.

## 2. Verified story-event overlap

The manifests were compared directly.

- `analysis_bundles/00_shared/03_story_events_001-005.dialogue.txt`: **25 unique source scripts / 1,650 messages**
- `analysis_bundles/story_events/event_001-005.dialogue.txt`: **27 unique source scripts / 1,670 messages**
- overlap: **25**
- shared-only: **0**
- dedicated-only: **2**

Dedicated-only sources:

| original_name | sorted_relative_path |
| --- | --- |
| adv_event_highscore_introduction-01.txt | transcripts_raw/06_story_events/event/event_highscore_introduction-01.txt |
| adv_event_highscore_introduction-02.txt | transcripts_raw/06_story_events/event/event_highscore_introduction-02.txt |

Adjudication: the shared view is a **strict 25-source subset** of the dedicated event bundle. Future analysis should read/cite the dedicated event tranche as the complete event 001-005 view while treating shared appearances as aliases.

## 3. "Missing dialogue" audit

Validation report: **374 missing dialogue extracts**.

Direct report check: **374 / 374 have `message_count = 0`**.

Therefore:

> `missing_dialogue_files.tsv` records absence of a dialogue-only derivative, not loss of dialogue-bearing narrative.

The raw A1 files remain in Source Lock 1.0. They may contain camera, motion, timing, system, layout, gacha, or other non-`[message]` commands and must not be deleted merely because they have no A2 derivative.

Notable zero-message categories include all `gasha`, all `pstep`, all `pweek`, `musics`, `warmup`, plus many `produce` and seven `pstory` files.

## 4. Ambiguous/unassigned audit

There are **159 unassigned files**. Their distribution is:

| category | unassigned | dialogue-bearing | message lines |
| --- | --- | --- | --- |
| gasha | 36 | 0 | 0 |
| musics | 1 | 0 | 0 |
| presult | 13 | 13 | 23 |
| produce | 86 | 11 | 13 |
| pstep | 20 | 0 | 0 |
| pstory | 1 | 1 | 14 |
| tower | 1 | 1 | 20 |
| warmup | 1 | 0 | 0 |

Only **26 files contain dialogue, totaling 70 message lines**. Those 26 are the only unassigned items requiring mandatory narrative adjudication in Phase 0.

## 5. All dialogue-bearing unassigned exceptions

| original source | category | msgs | path | promoted function | continuity | Phase 0 adjudication |
| --- | --- | --- | --- | --- | --- | --- |
| adv_presult_001_final-failure.txt | presult | 2 | transcripts_raw/09_produce_system_and_growth/presult/001_final-failure.txt | SYSTEM / SPINE-adjacent | C3 | Series 1 shared Asari result wrapper; outcome-dependent |
| adv_presult_001_final-normal-01.txt | presult | 2 | transcripts_raw/09_produce_system_and_growth/presult/001_final-normal-01.txt | SYSTEM / SPINE-adjacent | C3 | Series 1 shared Asari result wrapper; outcome-dependent |
| adv_presult_001_final-normal-02.txt | presult | 2 | transcripts_raw/09_produce_system_and_growth/presult/001_final-normal-02.txt | SYSTEM / SPINE-adjacent | C3 | Series 1 shared Asari result wrapper; outcome-dependent |
| adv_presult_001_final-normal-03.txt | presult | 2 | transcripts_raw/09_produce_system_and_growth/presult/001_final-normal-03.txt | SYSTEM / SPINE-adjacent | C3 | Series 1 shared Asari result wrapper; outcome-dependent |
| adv_presult_001_final-true.txt | presult | 2 | transcripts_raw/09_produce_system_and_growth/presult/001_final-true.txt | SYSTEM / SPINE-adjacent | C3 | Series 1 shared Asari result wrapper; outcome-dependent |
| adv_presult_001_mid-failure.txt | presult | 2 | transcripts_raw/09_produce_system_and_growth/presult/001_mid-failure.txt | SYSTEM / SPINE-adjacent | C3 | Series 1 shared Asari result wrapper; outcome-dependent |
| adv_presult_002_failure.txt | presult | 2 | transcripts_raw/09_produce_system_and_growth/presult/002_failure.txt | SYSTEM / SPINE-adjacent | C3 | Series 2 shared Producer result/evaluation wrapper; outcome-dependent |
| adv_presult_002_final-normal-01.txt | presult | 2 | transcripts_raw/09_produce_system_and_growth/presult/002_final-normal-01.txt | SYSTEM / SPINE-adjacent | C3 | Series 2 shared Producer result/evaluation wrapper; outcome-dependent |
| adv_presult_002_final-true-01.txt | presult | 2 | transcripts_raw/09_produce_system_and_growth/presult/002_final-true-01.txt | SYSTEM / SPINE-adjacent | C3 | Series 2 shared Producer result/evaluation wrapper; outcome-dependent |
| adv_presult_003_final-failure.txt | presult | 1 | transcripts_raw/09_produce_system_and_growth/presult/003_final-failure.txt | SYSTEM / SPINE-adjacent | C3 | Series 3 Producer selection/H.I.F. result wrapper; outcome-dependent |
| adv_presult_003_final-true.txt | presult | 2 | transcripts_raw/09_produce_system_and_growth/presult/003_final-true.txt | SYSTEM / SPINE-adjacent | C3 | Series 3 Producer selection/H.I.F. result wrapper; outcome-dependent |
| adv_presult_003_selection-failure.txt | presult | 1 | transcripts_raw/09_produce_system_and_growth/presult/003_selection-failure.txt | SYSTEM / SPINE-adjacent | C3 | Series 3 Producer selection/H.I.F. result wrapper; outcome-dependent |
| adv_presult_003_selection-true.txt | presult | 1 | transcripts_raw/09_produce_system_and_growth/presult/003_selection-true.txt | SYSTEM / SPINE-adjacent | C3 | Series 3 Producer selection/H.I.F. result wrapper; outcome-dependent |
| adv_produce-refresh_001_before-audition-final.txt | produce | 1 | transcripts_raw/09_produce_system_and_growth/produce/refresh_001_before-audition-final.txt | SYSTEM / SPINE-adjacent | C1/C3 | Series 1/2 audition-preparation transition framing |
| adv_produce-refresh_001_before-audition-mid.txt | produce | 1 | transcripts_raw/09_produce_system_and_growth/produce/refresh_001_before-audition-mid.txt | SYSTEM / SPINE-adjacent | C1/C3 | Series 1/2 audition-preparation transition framing |
| adv_produce-refresh_002_before-audition-final.txt | produce | 1 | transcripts_raw/09_produce_system_and_growth/produce/refresh_002_before-audition-final.txt | SYSTEM / SPINE-adjacent | C1/C3 | Series 1/2 audition-preparation transition framing |
| adv_produce-refresh_002_before-audition-mid_01.txt | produce | 1 | transcripts_raw/09_produce_system_and_growth/produce/refresh_002_before-audition-mid_01.txt | SYSTEM / SPINE-adjacent | C1/C3 | Series 1/2 audition-preparation transition framing |
| adv_produce-refresh_002_before-audition-mid_02.txt | produce | 1 | transcripts_raw/09_produce_system_and_growth/produce/refresh_002_before-audition-mid_02.txt | SYSTEM / SPINE-adjacent | C1/C3 | Series 1/2 audition-preparation transition framing |
| adv_produce-refresh_003_final_01.txt | produce | 3 | transcripts_raw/09_produce_system_and_growth/produce/refresh_003_final_01.txt | SPINE / SYSTEM | C0-C1 or C3 by outcome context | Series 3 H.I.F./Selection transition framing; shared Producer/Asari system line(s) |
| adv_produce-refresh_003_final_02.txt | produce | 1 | transcripts_raw/09_produce_system_and_growth/produce/refresh_003_final_02.txt | SPINE / SYSTEM | C0-C1 or C3 by outcome context | Series 3 H.I.F./Selection transition framing; shared Producer/Asari system line(s) |
| adv_produce-refresh_003_selection_01.txt | produce | 1 | transcripts_raw/09_produce_system_and_growth/produce/refresh_003_selection_01.txt | SPINE / SYSTEM | C0-C1 or C3 by outcome context | Series 3 H.I.F./Selection transition framing; shared Producer/Asari system line(s) |
| adv_produce-refresh_003_selection_02.txt | produce | 1 | transcripts_raw/09_produce_system_and_growth/produce/refresh_003_selection_02.txt | SPINE / SYSTEM | C0-C1 or C3 by outcome context | Series 3 H.I.F./Selection transition framing; shared Producer/Asari system line(s) |
| adv_produce-refresh_003_selection_03.txt | produce | 1 | transcripts_raw/09_produce_system_and_growth/produce/refresh_003_selection_03.txt | SPINE / SYSTEM | C0-C1 or C3 by outcome context | Series 3 H.I.F./Selection transition framing; shared Producer/Asari system line(s) |
| adv_produce-week-skip_002_01.txt | produce | 1 | transcripts_raw/09_produce_system_and_growth/produce/week-skip_002_01.txt | SYSTEM / TEXTURE | C3/system state | Series 2 week-skip/recovery system framing |
| adv_pstory_003_reversi_world-explanation-final.txt | pstory | 14 | transcripts_raw/01_produce_main_story/series_003/reversi/world-explanation-final.txt | SPINE | C0-C1 | Misfiled-by-context shared H.I.F. world explanation under REVERSI path; major institutional doctrine |
| adv_tower-001.txt | tower | 20 | transcripts_raw/98_miscellaneous/tower/tower-001.txt | SPINE / TEXTURE | C0/C2 | Hatsuboshi Request System introduction; real work, in-school selection, compensation, Producer/idol growth |

### 5.1 `presult`: 13 files / 23 messages

All 13 dialogue-only derivatives were inspected.

- Series 1 uses Asari to frame final/mid outcomes, recording the idol's result and stage.
- Series 2 switches primarily to `{user}` and frames final evaluation, public-stage eligibility, and FINALE result.
- Series 3 frames Selection/H.I.F. outcomes, including explicit Prima Stella staging in the true-labeled final result.

Adjudication: preserve as **shared route/result wrappers**. They are valuable to continuity, branch, Producer, and institutional analysis but are not hidden character-route scenes. Outcome-coded variants are C3 by default.

### 5.2 `produce`: 11 files / 13 messages

Inspected lines are shared Producer/Asari transition cues:

- Series 1/2 audition-preparation reminders;
- Series 3 Selection and H.I.F. preparation;
- one Series 2 week-skip/recovery line.

Several Series 3 lines are strong story-state locators (Selection sequence and H.I.F. main-tournament transition). The `selection_02/03` scripts also preserve ruby where written `選抜試験` is read as `セレクション`.


Adjudication: manually index them under shared/system exceptions; use as C0/C1/C3 according to the specific state, never as character ownership merely because they sit inside Produce infrastructure.

### 5.3 `adv_pstory_003_reversi_world-explanation-final.txt`: 14 messages

Original path:

`transcripts_raw/01_produce_main_story/series_003/reversi/world-explanation-final.txt`

Despite its `reversi` path, the scene is overwhelmingly **Asari institutional exposition** and applies beyond a narrow pair reading. It establishes:

- clearing H.I.F. Selection and moving to the main tournament;
- the revised H.I.F. rule structure;
- unified solo/unit judging;
- the winner becoming `プリマステラ / 一番星` (Prima Stella);
- intra-unit comparative evaluation;
- a prescribed-song round and a free-song round;
- prescribed song as differentiated performance of the same song;
- free song as evidence of how well idol and Producer discovered/refined a song suited to the idol;
- explicit evaluation of both idol ability and accumulated production;
- H.I.F. as the culmination of the Producer/idol partnership to that point.


Adjudication: **manual promotion to shared institutional SPINE**, while retaining the canonical original path as provenance. Default continuity: C0/C1.

### 5.4 `adv_tower-001.txt`: 20 messages

Original path:

`transcripts_raw/98_miscellaneous/tower/tower-001.txt`

This is not disposable miscellaneous dialogue. It introduces the `初星依頼制度 / はつぼしリクエスト` (Hatsuboshi Request System), including selection of recipients and explicit compensation, and frames external work as part of Producer/idol development.


Adjudication: **manual promotion to institutional SPINE/TEXTURE**. Preserve `98_miscellaneous` path as source provenance rather than reorganizing A1.

## 6. Exception-promotion policy

Promotion is analytical, not physical. Do **not** move the raw files. Instead create index aliases containing:

- canonical source ID;
- original filename/path;
- category;
- message count;
- promoted narrative function;
- continuity class;
- reason for promotion;
- later analytical documents that consume the source.

## 7. Remaining non-dialogue unassigned files

The remaining **133 unassigned files** have zero message lines. They remain in A1 and may be revisited when:

- branch topology depends on system commands;
- staging/timing matters;
- gacha/live behavior needs reconstruction;
- a script ID is referenced by another source;
- Phase 1 discovers an unexplained continuity transition.

They are **not a Phase 0 blocker**.

## 8. Audit conclusion

Phase 0 closes the exception question with no evidence of silently lost dialogue in the validation-report "missing" set. The significant risk was instead **classification**, not extraction: 26 small dialogue-bearing sources sat outside the planned bundles, and two of them contain major institutional exposition. They are now explicitly promoted through the index/ledger layer.
