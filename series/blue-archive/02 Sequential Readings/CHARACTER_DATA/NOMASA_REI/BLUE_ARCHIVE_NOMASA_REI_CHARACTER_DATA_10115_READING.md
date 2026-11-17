---
series: BLUE_ARCHIVE
artifact_type: character_data_reading
scope: NOMASA_REI_CHARACTER_DATA_10115
generation: V1
status: canonical
source_story_ids:
  - "BA:character_data:10115:profile_and_dialog"
source_boundary: "Complete canonical Japanese source objects named in source_story_ids at BA_REFRESH_20260928T032248159554Z; source-facing contextualization accepted with limits in cycle005; written text only"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Nomasa Rei — the complete profile and base written repertoire

Complete profile and all 48 contextual written lines. Candidate admission preserves ordinary rest, work, collecting and birthday evidence alongside sporting aims; it does not claim a performed voice reading.

## 1. Complete source witness

Pinned source root is `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z`; upstream `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. Raw acquisition remains outside analytical Git. Each named canonical object, complete structured witness and consequential primary controls were inspected. Source-unit completion is contributor inspection; admission and shared reconciliation remain the parent integrator’s responsibility.

| Exact complete object | Generation-relative canonical path | Extent and canonical SHA-256 |
|---|---|---|
| `BA:character_data:10115:profile_and_dialog` | `02_CANONICAL_STORIES/CHARACTER_DATA/CH0245/VARIANT_10115.md` | 1 profile records plus 48 written dialog/context records; `c60a322f94f0e55ac197384fa714d5d3a5a1b4ecaa64db4e976499fab413dbbc`. |

Raw table provenance, actual file SHA-256:

- `DB/CharacterDialogExcelTable.json`: `dbba21ca2bcdd856498e9eae0c3319309a829e3d0a4ee8d206e9366c28a24b20`.
- `DB/LocalizeCharProfileExcelTable.json`: `f7039fb2bbf78535d4f5aa926cc43a74ddece835d2bea7edc2e46c4bc57b6fe4`.

Canonical anchors preserve `utterance_id`, scene, mode and selection groups; `choices.jsonl` preserves every option and `branch_effect_known=false`; `momotalk_messages.jsonl` preserves complete message IDs, `Answer` alternatives, conditions and schedule links; written data preserve record IDs, categories, conditions, unlocks and source offsets. `DataList` locators are array offsets, not upstream `Id` values. Numeric source IDs, rank unlocks and documentary release are retrieval/provenance, not dates of acts against main chapters.

## 2. Admission and identity scope

Propose **ADMIT_WITH_LIMITS** for the complete written profile/dialog object, pending parent acceptance. The positive route is `BA_PERSON_CH0245` / `BA_VARIANT_10115`. Primary profile `LocalizeCharProfileExcelTable.json DataList[224]` names `野正レイ`, one-year student, age fifteen, birthday August 9, height 159 cm, and hobbies `スポーツ観戦、年鑑分析`. Those are profile assertions, not scene-based measurements or a main-story calendar.

The primary profile also preserves `Club=None` and gacha label `トレーニング部`; its Japanese introduction calls her Millennium’s baseball-loving fourth batter. Registry `TrainingClub` and printed `ミレニアム野球部` therefore coexist at the source pin. Neither permits a merge with diving Rei or an invented replacement club record. The complete base costume is `CostumeUniqueId=1011501`. Event costume `1900936001` has a separate object and separate reading.

The profile introduction says she wants to reform a club occupied with physics/dynamics and that her apparent rapport with Sumire sometimes breaks down in practice. This is a profile account of aims and a relationship, not an accomplished reform or permanent incompatibility. Rei’s own mechanical reasoning in bond E006 remains a contrary case to any simple “baseball versus all analysis” characterization.

## 3. Ambition at a modest starting point

All category locators below use `BA:character_data:10115:<category>:line:<six-digit number>`.

The status `まずは打率1割を！` and `CharacterGet:line:000001` set an initial target, not an observed batting average. Fourth-batter identity should not silently become demonstrated fourth-batter excellence. The New Year set `UILobby:line:000023–000026` moves from a home-run wish to becoming a three-tenths batter, then a one-tenth starting goal. `WeaponGet:line:000001` repeats the correction while linking hoped-for improvement to repaying guidance. The aspiration and qualification are both character evidence; runtime favour rank is not batting proficiency.

The full primary profile’s weapon text names `ムーンショット！`, a recoilless gun carrying her wish for a home run, and explicitly frames sending a ball to the moon as her boast. It does not provide a moon-reaching achievement, weapons-performance test or training prescription. Profile `CharacterSSRNewJp`, `練習は試合のように、試合は練習のように！`, is a stated motto. None of these claims erases the narrated defeat in bond E002 or pitching failures in E003.

## 4. Rest, appetite and limited self-descriptions

The five Café lines are not five stages of one witnessed visit. They are context-bound available utterances. `Cafe:line:000001` wonders whether Sumire is present; Japanese does not supply the Korean wording’s implied pursuit into the café. The line is enough to preserve caution toward a senior without inventing a chase.

`Cafe:line:000002` values rest for effective practice. `Cafe:line:000003` asks whether caffeine raises exercise effects, rather than asserting established efficacy. No dietary or medical recommendation follows from a fictional character’s uncertain question. `Cafe:line:000004` is parenthesized and primary `DialogType=Think`, considering whether skipping practice would be wrong. `Cafe:line:000005` finds whipped cream tempting and restrains the desire. Neither proves actual consumption, a missed practice or a lasting disorder.

The Schale set also gives rest an everyday rationale: `UILobby:line:000009` calls duty a reason to rest properly, and `line:000010` says she soon wants to practise again. This oscillation qualifies both a relentless-training model and a pure-avoidance model. Wanting rest is worth recording without a health crisis.

Her `アウトドア派` claim is immediately narrowed to the practice ground or stadium, followed by a question about whether that counts (`UILobby:line:000007–000008`). The self-description arrives with its own correction. An analyst should not convert it into evidence of hiking, travel or all-purpose outdoor interests.

## 5. Work, numbers and the pleasures she wants to share

`UILobby:line:000001–000002` presents preparation of a ToDo list and an account of past baseball-club schedule management. `line:000005–000006` offers data/statistical help, qualified as less than Seminar seniors’ ability. These are competency claims and available service offers, not a completed independent statistics audit. They connect her sports life with numerical and organisational interests without measuring comparative skill.

Her energetic greeting is explicitly described as a pre-match greeting (`UILobby:line:000003–000004`). No match is thereby played in the lobby. Likewise the offer to go out if work ends early and the report of limited cards at a stadium shop (`line:000011–000012`) establish a wish and reported attraction, not a completed purchase. The cards are ordinary collector pleasure with analytical value.

The batting-centre question and recommendation (`line:000013–000014`) describe the exhilarating feeling she gets from striking a ball and her prediction that Sensei would like it. Sensei’s visit, enjoyment and stress relief are unshown. Preserve the shared activity she proposes without changing it into proof of successful adult treatment.

The user-birthday group `UILobby:line:000015–000018` links numerical memory with an offer to do her best that day. The student-birthday group `line:000019–000022` gives surprise at being remembered, fluster over a possible present, and pleasure in being celebrated. These demonstrate available character address under runtime birthday conditions. They do not prove that a specific gift was given or that all these dates occur consecutively in story time.

Christmas lines (`line:000027–000028`) frame the off-season as preparation and suggest chicken or roast turkey. They do not show a meal. Halloween lines (`line:000029–000031`) report that someone apparently called the baseball club’s results horrifying, then declare reforming resolve. The qualification `言われてたみたい` keeps the insult a report. No identified speaker, audited season record or completed turnaround is supplied.

## 6. The keepsake is a reuse witness

All nine `UILobbySpecial` lines (`line:000001–000009`) were read. They reiterate the caught home-run ball, early carrying, wished-for home run, locker storage and felt return to starting motivation. They are a reuse of the remembered account carried by eleven `[log=레이]` utterances in bond E006 (`BA:bond:10115:006:scene:001:u:0037–u:0047`), with different segmentation.

Record both exact source objects and their available wording, but do not count the repeated account as two independent historical witnesses or a second scene in which she catches the ball. The distinction between **catching** a home-run ball and **hitting** a first home run remains essential. `お守り` and `ような気がして` describe experienced significance, not literal magic or a completed career milestone.

## 7. Complete primary controls and provenance limits

All 48 dialog records occupy `CharacterDialogExcelTable.json DataList[9232–9279]` and were inspected for text, category, condition, group, anniversary, dates, unlocks and voice references. Category extent: one title, one acquisition, five Café, 31 lobby, one weapon-acquisition and nine special-lobby lines. `DisplayOrder` puts WeaponGet at 2600 despite its position before special records in the canonical representation; none of these orders is a story-world date.

| Primary controls | Exact range and interpretation |
|---|---|
| Title / acquisition | `DataList[9232–9233]`, Idle, favour rank 1. Acquisition wording is an available self-introduction, not a unique witnessed recruitment event. |
| Café | `[9234–9238]`, Idle, favour rank 15; `[9237] DialogType=Think`. Group numbers and type do not supply a complete visit or performed interior voice. |
| Ordinary lobby | `[9239–9252]`, Enter/Idle groups with paired continuations. Same category/group text belongs together; all groups are not one chronological conversation. |
| Birthdays | `[9253–9256] Anniversary=UserBDay`; `[9257–9260] Anniversary=StudentBDay`. The condition is runtime context, not independent calendar placement. |
| Seasonal | `[9261–9264]` January 1–3; `[9265–9266]` December 24–25; `[9267–9269]` October 30–31. The annual windows do not establish a particular story year. |
| Weapon / special | `[9270]` favour rank 25 plus `UnlockEquipWeapon=true`; `[9271–9279]` Idle special groups and duration/animation metadata. Unlock rank and presentation duration are not character-development dates or listened pacing. |

Thirty-eight raw records have nonempty `VoiceId` arrays; ten are empty, including the nine special lines and one New Year line. The identifiers and profile performer credit were inspected as provenance only. **No audio was played**, so performed intonation, pacing and actress interpretation remain outside admission. Nonempty references are not evidence that the inspected packet is audio-free; empty references do not prove the franchise lacks a performance.

## 8. Seven-ledger and coverage proposals

| Ledger | Scoped effect |
|---|---|
| Character | Add reform aspiration, low starting target, statistical/schedule interests, qualified rest and appetite, constrained outdoor self-description, collector pleasure, birthday delight and repeats of the keepsake account. Separate all desires, reports and conditional utterances from observed outcomes. |
| Relationship | Add available Rei→Sensei help, invitations and birthday remembrance, plus qualified profile Sumire relation and Café caution. Seminar comparison stays Rei’s statement, not a shown meeting or measured superiority. |
| School / club / institution | Preserve TrainingClub/gacha and baseball textual labels; add profile reform aim and reported physics/dynamics emphasis, schedule-work account and Schale duty’s rest value. No accomplished school reform or complete season dataset. |
| Sensei role / ethics | C007/C016 gain student-offered service and shared interests as available address. No teacher reply, confirmed trip, fulfilled present or therapeutic outcome is inspected here. |
| Japanese voice / address | Add `まずは` goals, self-corrections, tentative `でしたっけ`, birthday stammer and `言われてたみたい` report. Preserve Think/Talk/runtime conditions; G10 remains open. |
| Motif / theme / callback | Practice and rest, data and effort, collected cards and treasured ball are valued ordinary materials. Special-lobby reuse is mapped to E006 without multiplying independent proof. |
| Claim revision | C008 gains source-class and runtime-context bounds. C005/C006 remain rejected; no universal coaching efficacy, batting improvement or fixed personality model follows. No direct C009/C012 test is supplied by this written packet. |

Coverage proposal: **one complete written-data source, admission pending**; profile plus 48 records are its extent, not 49 separately tracked story objects. G01/G06 gain private/ordinary repertoire; G07/G12 retain chronological/variant boundaries; G09/G14 retain context and type limits; G10 retains uninspected performance; G13 retains medical/sporting/technical outcome debt. No global row is closed.

Diagnostic status is **NO_DIAGNOSTIC_OPPORTUNITY**. This packet can enrich a scoped reconstruction later, but cannot itself establish a model or retrospective prediction success.

## Parent acceptance — cycle005

[Cycle005](../../BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_005_CHECKPOINT.md) accepts exactly the source IDs declared by this artifact after complete contributor inspection, full integrator argument review, actual canonical/raw checks and consequential Japanese/source-form verification. The original proposed ledger, coverage and gap sections are retained as the contributor handoff record; the cycle checkpoint and current shared surfaces own accepted effects and counts. No proposal language remaining in that historical record overrides this accepted current boundary.

ADMIT_WITH_LIMITS supplies situated ordinary, relationship and written evidence. Explicit local relations do not establish main placement or a total variant timeline. Choices, reports, inward/private and raw actor modes keep their stated limits; no performed audio, image pixels, model promotion, monograph, frozen forecast or prospective validation is inferred. No unprinted outcome or later warmth repairs an earlier refusal, ignored protest or expressed discomfort.
