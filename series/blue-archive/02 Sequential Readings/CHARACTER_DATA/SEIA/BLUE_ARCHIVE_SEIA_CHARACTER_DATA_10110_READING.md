---
series: BLUE_ARCHIVE
artifact_type: character_data_reading
scope: SEIA_CHARACTER_DATA_10110
generation: V1
status: active_provisional
source_story_ids:
  - "BA:character_data:10110:profile_and_dialog"
  - "BA:character_data:event_costume:1900934001:character:10110"
source_boundary: "Complete Japanese source objects named in source_story_ids at pinned BA_REFRESH_20260928T032248159554Z; source-facing contextualization, no performed voice or additional supplemental admission"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Seia — The complete ordinary written baseline and positively joined event interface

## Complete source witness

Pinned root: `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z`; `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. Raw acquisition remains outside analytical Git.

| Complete source | Canonical route | Inspected extent and canonical SHA-256 |
|---|---|---|
| `BA:character_data:10110:profile_and_dialog` | `02_CANONICAL_STORIES/CHARACTER_DATA/CH0070/VARIANT_10110.md` | 1 complete profiles; 41 complete written contextual records, including blanks; `486f8cd0dbd2aaf1c5f9515dc11a146c93de2e0367010ee16db001663d1cccf0`. |
| `BA:character_data:event_costume:1900934001:character:10110` | `02_CANONICAL_STORIES/CHARACTER_DATA/CONTEXTUAL/BA_character_data_event_costume_1900934001_character_10110.md` | 0 complete profiles; 76 complete written contextual records, including blanks; `152a8536c2159222611645b0c5a535adcdb5562da1c94c78a86843ce49fac290`. |

Raw table provenance:

- `DB/LocalizeCharProfileExcelTable.json` — SHA-256 `f7039fb2bbf78535d4f5aa926cc43a74ddece835d2bea7edc2e46c4bc57b6fe4`.
- `DB/CharacterDialogExcelTable.json` — SHA-256 `dbba21ca2bcdd856498e9eae0c3319309a829e3d0a4ee8d206e9366c28a24b20`.
- `DB/CharacterDialogEventExcelTable.json` — SHA-256 `b630dffc5d86487d1df36bb1f292f78b209e84b435653e5780d73c552b860bb2`.

Positive exact-name identity witness: `百合園セイア` → `BA_PERSON_CH0070` → CharacterId `10110` / DevName `CH0070`, `百合園セイア` → `BA_PERSON_CH0070` → CharacterId `10123` / DevName `CH0295`. Registry method `exact_full_name_jp`, confidence high; registry SHA-256 `eec81b6e81805bddcadb4b7296c41d877e62585b5501fcc9ccc92e5c552a0da3`. Actual profile and scene context distinguish variants; retrieval identity is not an absolute calendar or transfer of acts between outfits. No counterpart identity is invented. Costume joins require their printed OriginalCharacterId witness, detailed in their own written reading.

## Full Japanese profile, distinct from a performed biography

The complete LocalizeCharProfile DataList214 record was read, including fields omitted by the abbreviated canonical page. It identifies **百合園セイア / ゆりぞの**, third year,17,149cm,birthday9/29, hobbies puzzles and reading, Tea Party recruitment affiliation and leadership of Trinity's Sanctus student union. Club=`None` in this profile is retained alongside the explicit recruitment/introductory affiliation; no empty raw field cancels the latter. The introduction describes a pedantic/elusive way of speaking, bookworm visits to the great library, and more childlike behavior after her injury healed. **That is a written profile assertion with a relative before/after phrase, not an independently verified clinical examination, complete rehabilitation or a date for every bond.**

The status message describes difficulty weaving words. Full weapon text names`鋭き光彩`, calls it her preferred pistol and says its loaded state resembles her sometimes sharp tongue. This written metaphor/description is not a separately observed armed encounter or proof of current ammunition in a particular room. The additional recruitment text`いずれ――道は繋がるだろう。` is prospective rhetoric, not verified destiny. Designer/illustratorkokosando and voice credit種﨑敦美 are production metadata; credits do not admit a performed voice. Normalized full-profile SHA-256`64f0ddff67d3c9bf774ddfaff9dd8158b6d616d0edb337fcd487a8ca09a3f333` preserves the record rather than replacing full intake with a profile summary.

## All41 ordinary contextual records and what their forms permit

Raw CharacterDialog8729–8769 contains41 **Talk** records and **no blank Japanese text**: one title, one acquisition, five Cafe,22UILobby, one weapon and11UILobbySpecial. Acquisition/title unlock1, Cafe15 and weapon25 are game-access gates; ordinary lobby and Special0 do not date intimacy or simulate41 chronological meetings. VoiceId arrays, animation fields and raw duration were read as provenance, not heard or watched.

Title/acquisition names the game and a long-awaited reunion. Cafe1–5 observes orderly arrangement, decoration lifting spirits, contrast with her room, teacher-invited company and curiosity about composition. These give aesthetic attention, interest and variety beyond prophecy, without an independently surveyed cafe or guarantee everyone present responded to the teacher. UILobby1–11 greets him, examines unfamiliar objects and his place, comments on slow familiarity and rarely leaving her room, and wonders whether the scene might become familiar, conditional on him. Offering her own room and leaving interpretation to him is indirect invitation with acknowledged recipient freedom; it is not a fixed exclusive relationship or unconditional consent.

UILobby12–22 contains the adult-birthday congratulation, her own birthday thanks after teasing his interest, New Year desire to reach a new self, a Christmas box-surprise joke and unfamiliar Halloween mischief. Anniversary forms preserve occasion-specific written possibilities without placing five holidays in a main-story year. The weapon line expresses an unexpected gift and the absence of words yet current positive feeling. These are wishes, play and gratitude at small stakes, not completion of a new personality state.

Special1–11 reproduces the ordinaryE002 surprise/world-expansion, unexpected gaze, remembered invitation and being drawn to his words. Actual bond timed/log narration divides the same written material into12 records (including split recognition); contextual reuse remains41-line written intake, not a second event or another11 personality observations. AllSpecial raw modes are Talk; canonical bond narration/log modes remain unchanged. Reuse supplies a positive written correspondence while leaving performance and other-character knowledge bounded.

## Positive same-variant event costume join and every76 record

Every selected CharacterDialogEvent row explicitly supplies **OriginalCharacterId10110 → CostumeUniqueId1900934001**. Costume master DataList2202 isCH0070_Event_NPC, ordinaryCH0070 resources and CharacterVoiceGroupId10110. Its master resource/release fields corroborate the packaging but do not alone provide an OriginalCharacterId; the dialog rows do. Thus this is an ordinary-family event presentation, not a third person, swimsuit variant or an independent profile. Costume master SHA-256`70e960a2acb7c7f20dbbfd006bea724bbdf80aae7ca22439228952f7ef80c643` is additional provenance.

All 76 records are present with no blanks:34 **Talk** lobby records,28 **UITalk** shop and14 **UITalk** mini-game mission. Each Event843/10843 contains38 Japanese records:17lobby,14shop,7mission. Positive repeated text does not create two lived repetitions. Exact raw spans are843lobby6786–6802/shop6851–6864/mission6873–6879;10843lobby6903–6919/shop6968–6981/mission6990–6996. Both sets carry UnlockEventSeason equal to their ownEventID and ScenarioGroupId10041005. **A display-linked group is not a newly read/admitted main or unclassified scene.** Of76 conditions,60 areNone,8Close,4Day6 and4Day13. Display gates are interface conditions, not dates against Eden Treaty or a proven two-week event biography.

Lobby1–17 (repeated18–34) offers greeting, awareness of busyness, welcome/desire, rising atmosphere with a deferred explanation, approaching finale, and gratitude whatever the adult may have seen. It also asks whether he needs her physical presence, welcomes an exception, and finds the environment different from ordinary Trinity and ticklish/unfamiliar while explicitly denying that this is a negative evaluation. Vague knowing phrasing does not authenticate the hidden event, an unseen vision or prophecy; the explicit qualification prevents unfamiliarity being reduced to dislike.

Shop1–14 (repeated15–28) invites browsing and naming desire, jokes about something disappearing before a blink, rejects the idea of being domesticated by money, interprets an outstretched hand as not refusing her own, welcomes a choice and asks whether what was found equals what was obtained. These are written interface-address metaphors and requests, not observed customer purchases, automatic bodily consent or proof that all choices are good. Her interpretation of a hand gesture remains her assertion. Mini-game1–7 (repeated8–14) says tasks need the adult's eye, calls waiting a kind of hunch, asks him not to unsettle her interpretation of him, takes comfort in lack of change and thanks/praises effort. A hunch is not an independently measured foreknowledge method; gratitude/praise is interface speech, not verification of completed mission details.

## Comparison, contradictions and seven proposals

The complete ordinary bonds add wanted nap, reciprocal sweets, book conversation and a chosen gratitude song. The [accepted Tea Party group reading](../../GROUP/BLUE_ARCHIVE_GROUP_3601_3603_DEEP_READING.md) adds direct practical care, purchases and peer company, so rarely leaving her room is contextual self-description rather than literal never-leaving. The [V100 C004 E005 reading](../../MAIN/VOLUME_100_最終編/BLUE_ARCHIVE_MAIN_V100_C004_E005_DEEP_READING.md) retains actual early rescue preparedness with uncertain foreboding. Neither interface hunch nor profile healed-injury wording measures foresight or retrospectively supplies the undisclosed main daydream deal.

Character: aesthetic curiosity, puzzles/books, humor, desire for familiarity/new self and positive unfamiliar environment; declared healed injury remains profile-sourced. Relationship: invitations, thanks, recipient freedom and an assertive hand interpretation whose truth is unverified. Institution: Sanctus/Tea Party identity and exact ordinary event packaging, no law/cafe/event-policy or new source admission. Sensei: recipient of gifts, attention and expected effort, without unrestricted consent or proven unchanged identity. Japanese: complete full-profile JP fields and41 Talk/34 Talk+42 UITalk forms, Special correspondence, all76repeat/gated records and no blanks. Motif: words, expansion/novelty, familiarity and chosen desire, including rejection of being bought. Claim revision: BA-C008/C016/C017 preserve report/mode/consent distinctions; profile rhetoric and interface praise do not supply a model. Coverage proposes exactly these two complete objects. G01/G06 narrow ordinary written breadth; G07/G08/G09/G10/G12/G13 retain local order, repeat/UI/gate, performance, positive identity and clinical/outcome limits. Event843/10843 and unclassified queues are not admitted by their context object.

## Admission and maintained-surface limits

**ADMIT_WITH_LIMITS proposed** for exactly the complete named objects. All formal alternatives, conditional message routes, printed action, source-form labels and blank contextual records are retained in their proper forms; alternatives and duplicated conditional responses are not simultaneous acts. Reader-access inner text does not become other characters' knowledge. Only explicit local message links and recollections establish relative relations. Episode or publication order does not place encounters against main chapters. Written Japanese and supplied records were inspected; performed delivery, visual gestures, image pixels and audio timing were not.

The seven-ledger/coverage/gap changes remain proposals for the integrating owner, with the family checkpoint reconciling their full extent. Quiet enjoyment, humor, personal wishes and mundane labor remain positive evidence regardless of stakes; contrary acts and literal objections are retained. On semantic acceptance these objects can become ANALYZED with limits without promoting a standalone model or erasing existing main history. G01 private breadth reduces locally; G06 cross-school breadth still requires comparison, G07 chronology remains bounded, G08 repeat/costume/UI forms are distinct, G09 speaker/choice/text forms are retained, G10 performed voice is unadmitted, G12 variant identity is explicit, and G13 legal/clinical/technical outcomes remain unverified where not printed. Main, group, event, mini and unclassified material receives no new admission through this packet. No durable claim ID, monograph, reconstruction or prediction is created: **NO_DIAGNOSTIC_OPPORTUNITY**, because no model was frozen with these sources held out. Shared controls remain parent-owned.
