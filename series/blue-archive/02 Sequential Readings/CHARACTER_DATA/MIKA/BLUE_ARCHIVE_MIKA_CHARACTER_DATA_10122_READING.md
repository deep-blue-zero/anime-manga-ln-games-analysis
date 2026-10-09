---
series: BLUE_ARCHIVE
artifact_type: character_data_reading
scope: MIKA_CHARACTER_DATA_10122
generation: V1
status: active_provisional
source_story_ids:
  - "BA:character_data:10122:profile_and_dialog"
  - "BA:character_data:event_costume:1900940001:character:10122"
source_boundary: "Complete Japanese source objects named in source_story_ids at pinned BA_REFRESH_20260928T032248159554Z; source-facing contextualization, no performed voice or additional supplemental admission"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Mika — Swimsuit written baseline and the positively joined repeated event costume

## Complete source witness

Pinned root: `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z`; `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. Raw acquisition remains outside analytical Git.

| Complete source | Canonical route | Inspected extent and canonical SHA-256 |
|---|---|---|
| `BA:character_data:10122:profile_and_dialog` | `02_CANONICAL_STORIES/CHARACTER_DATA/CH0069/VARIANT_10122.md` | 1 complete profiles; 60 complete written contextual records, including blanks; `b1fbf6775e2ade5d652b44876ca342228ed12bfd26c74941138966599238bcd3`. |
| `BA:character_data:event_costume:1900940001:character:10122` | `02_CANONICAL_STORIES/CHARACTER_DATA/CONTEXTUAL/BA_character_data_event_costume_1900940001_character_10122.md` | 0 complete profiles; 54 complete written contextual records, including blanks; `752d6997cfb425214c2041555e503f2fbfe438004857d1913945c165b712a835`. |

Raw table provenance:

- `DB/LocalizeCharProfileExcelTable.json` — SHA-256 `f7039fb2bbf78535d4f5aa926cc43a74ddece835d2bea7edc2e46c4bc57b6fe4`.
- `DB/CharacterDialogExcelTable.json` — SHA-256 `dbba21ca2bcdd856498e9eae0c3319309a829e3d0a4ee8d206e9366c28a24b20`.
- `DB/CharacterDialogEventExcelTable.json` — SHA-256 `b630dffc5d86487d1df36bb1f292f78b209e84b435653e5780d73c552b860bb2`.

Positive exact-name identity witness: `聖園ミカ` → `BA_PERSON_CH0069` → CharacterId `10059` / DevName `CH0069`, `聖園ミカ` → `BA_PERSON_CH0069` → CharacterId `10122` / DevName `CH0294`. Registry method `exact_full_name_jp`, confidence high; registry SHA-256 `eec81b6e81805bddcadb4b7296c41d877e62585b5501fcc9ccc92e5c552a0da3`. Actual profile and scene context distinguish variants; retrieval identity is not an absolute calendar or transfer of acts between outfits. No counterpart identity is invented. Costume joins require their printed OriginalCharacterId witness, detailed in their own written reading.

## Entire written profile and positive variant/costume routes

The complete LocalizeCharProfile DataList239 record, normalized SHA-256 `33a5e8f03ce105a9f783ced1b3d845fd878e7c7b50ddc438bb4c681e8afa790f`, joins **聖園ミカ** exactly to10122/CH0294/personBA_PERSON_CH0069. Its Japanese recruitment explicitly says swimsuit reappearance and its introduction identifies leadership of the vacation plan. The profile depicts trying to give friends an enjoyable sea visit while efforts partly misfire and apparently increasing sleepless days. These are packaged written assertions with modal limits, not an inspected diagnosis or admission of EVENT848's complete narrative.3rd year,17,5月8日,157cm, name/ruby, status seeking a swimming companion, talk/accessory hobbies, weapon, recruitment and production credits were all read. The Japanese hobby fields remain `おしゃべり、アクセサリー集め`; different Korean hobby wording cannot replace the pinned Japanese baseline.

`Quis ut Deus` is described as carefully maintained and shining like a star even seaside, a written adornment/maintenance motif without technical or image verification. Designer/illustratorkokosando and credited voiceactor東山奈央 are metadata. The swimsuit baseline's use of Tea Party membership differs from the ordinary profile's former-office framing. Preserve the two written contexts; do not infer a reinstatement date or school decree from publication order or a profile packaging difference.

The54-record costume object has a positive join on **every raw record**: CostumeUniqueId1900940001 → OriginalCharacterId10122, with EventID848 or10848, UnlockEventSeason848 and ScenarioGroupId10046005. Costume master DataList2223 names **CH0294_Event_NPC**, CharacterVoiceGroupId10122 and CH0294 resources. Master SHA-256 `70e960a2acb7c7f20dbbfd006bea724bbdf80aae7ca22439228952f7ef80c643`. OriginalCharacterId is the exact identity witness; the master corroborates variant resources but has no OriginalCharacterId field. Its2022 release placeholder is not story chronology. The event-wide Japanese title remains unprovided and no event story is newly read/admitted here.

## All60 baseline contextual records and their modes

The60 records occupy raw CharacterDialog DataList10096–10155: UITitle1, CharacterGet1, Cafe5, UILobby38, WeaponGet1 and UILobbySpecial14. **59 Talk/1 Think**, with no blank Japanese records. Cafe line3/DataList10100 is Think: the supposition others also have their own worries, like her, is private-style written content. The other cafe entries find a strange object funny, notice how students visit Schale, await the teacher and ask whether something may be touched. Independent curiosity and concern for other students coexist with wanting his presence; Think is not automatically knowledge received by others.

Cafe gates use FavorRank15; title/recruitment1; weapon25 with UnlockEquipWeapon true;52 remaining contexts use0. Four lobby entries are UserBDay and four StudentBDay. Holiday-coded wording elsewhere still has raw AnniversaryNone and empty date ranges, so it is not an independently verified game unlock calendar. Asset VoiceIds do not constitute inspected performance.

Lobby lines1–18 volunteer help while admitting uncertain competence; imitate a domestic welcome, immediately disavow it as a joke; admire dull-work persistence; become embarrassed when swimsuit presence is questioned; value an uneventful day because of company; and affirm peace. Domestic formula/`あ・な・た` does not establish marriage, shared residence or a completed bath/meal. The ordinary pleasures remain valuable as written wishes, without becoming a roster of enacted office tasks.

Lobby19–38 address birthdays, a hoped-for memorable duty day, new-year effort, a meaningful day's duty and playful Halloween threat followed by reassurance there is no trick. These are separately gated/reusable addresses, not a consecutive calendar narrative. WeaponGet expresses surprise, gratitude and a wished-for return gift; no completed reciprocity is printed. UILobbySpecial1–14 repeats the night-view exchange: glad shared beauty, continued future worry/anxiety, momentary smaller perspective and chosen happiness. Its same-variant correspondence to10122:E008 u0053–0066 is exact positive text evidence, while the bond retains timed narration/log forms and this object remains reusable Talk. Repetition is not another observed meteor outing or a tested lasting effect.

## All54 event-context records, literal stop request and repeat gates

There are27 records for848 and27 for10848, with the two full Japanese text sequences verified equal. Each has19 UIEventLobby and8 UIEventMission records. Across54 there are **38 Talk/16 UITalk**. The exact gate distribution is40 None-detail records,8 Day records (Day6 andDay13, two per day per event), and6 Close records; none is blank. Original848 lobby offsets7710–7728 and mission7831–7838, and repeat10848 lobby7879–7897 and mission8000–8007, remain separate raw receipts, not new person or outfit IDs.

LobbyEnter1–9 moves through greeting/enjoyment, uncertainty about an unexpected situation, need to stay attentive and Close-conditioned relief/teacher gratitude. Day6 lines2–3 and Day13 lines5–6 are event-display gates; they do not establish the vacation's day count or certify actual narrative completion. LobbyIdle10–19 appreciates company, names absentmindedness, asks whether she is needed, jokes about tickling/retaliation, then explicitly asks that it stop. Her following denial of dislike does not revoke the request: she worries she might misunderstand. This is reusable responsive wording, not an independently witnessed touch or recipient permission to continue.

Mission1–8 dislikes the pile of work during a sea visit, wants a reward, proposes slacking together and praises progress or a good wave. It gives work/pleasure tension and playful temptation; it does not enact canceled duties or a checked surfing feat. Repeat lobby20–38/mission9–16 preserve the same complete semantics. A repeated season's positive identity does not produce54 independent autobiographical episodes.

## Seven proposals and evidence boundaries

Character: care-plan intent with packaged misfires/sleeplessness, curiosity, peace/company wishes and competence qualifications. Relationship: friend-worry Think, teacher gifts/possible reciprocity and an explicit event-context stop request despite positive feeling. Institution: profile membership framing and event-display conditions, no reinstatement or completed duties. Sensei: addressed/echoed audience only, no newly enacted intervention. Japanese: Think/Talk/UITalk, domestic joke/denial, precise `やっ改まって` source wording retained without silent repair, repeated log correspondence and actor/gate locators. Motif: tranquil shared time and uncertain self-authorship, with playful labor avoidance and incomplete reciprocity. Claim revision: BA-C008/C011/C016/C017 keep UI response, source mode and literal objection distinct from narrative acts. The [Tea Party reading](../../GROUP/BLUE_ARCHIVE_GROUP_3601_3603_DEEP_READING.md) supplies separate enacted peer care; [V003 C004](../../MAIN/VOLUME_003_エデン条約編/BLUE_ARCHIVE_MAIN_V003_C004_CHECKPOINT.md) supplies separate accountability. Coverage proposes exactly these two full objects, one full profile/114 contexts total. G01/G06 narrow written/private breadth, G08 narrows positive repeat/costume routing while global event naming/chronology and G07/G09/G10/G12/G13 remain bounded.

## Later main history retained

The earlier V003 C004 comparison above describes that checkpoint's then-open hearing. The later [V100 C001 checkpoint](../../MAIN/VOLUME_100_最終編/BLUE_ARCHIVE_MAIN_V100_C001_CHECKPOINT.md), E004/§1, records a three-session disposition: Tea Party powers/privileges removed, Patar representative authority retained pending replacement, confinement ended and academic return allowed. This printed main history is preserved. The present private/written source neither dates itself against that hearing nor independently supplies a reinstatement, external legal disposition or every lasting consequence.

## Admission and maintained-surface limits

**ADMIT_WITH_LIMITS proposed** for exactly the complete named objects. All formal alternatives, conditional message routes, printed action, source-form labels and blank contextual records are retained in their proper forms; alternatives and duplicated conditional responses are not simultaneous acts. Reader-access inner text does not become other characters' knowledge. Only explicit local message links and recollections establish relative relations. Episode or publication order does not place encounters against main chapters. Written Japanese and supplied records were inspected; performed delivery, visual gestures, image pixels and audio timing were not.

The seven-ledger/coverage/gap changes remain proposals for the integrating owner, with the family checkpoint reconciling their full extent. Quiet enjoyment, humor, personal wishes and mundane labor remain positive evidence regardless of stakes; contrary acts and literal objections are retained. On semantic acceptance these objects can become ANALYZED with limits without promoting a standalone model or erasing existing main history. G01 private breadth reduces locally; G06 cross-school breadth still requires comparison, G07 chronology remains bounded, G08 repeat/costume/UI forms are distinct, G09 speaker/choice/text forms are retained, G10 performed voice is unadmitted, G12 variant identity is explicit, and G13 legal/clinical/technical outcomes remain unverified where not printed. Main, group, event, mini and unclassified material receives no new admission through this packet. No durable claim ID, monograph, reconstruction or prediction is created: **NO_DIAGNOSTIC_OPPORTUNITY**, because no model was frozen with these sources held out. Shared controls remain parent-owned.
