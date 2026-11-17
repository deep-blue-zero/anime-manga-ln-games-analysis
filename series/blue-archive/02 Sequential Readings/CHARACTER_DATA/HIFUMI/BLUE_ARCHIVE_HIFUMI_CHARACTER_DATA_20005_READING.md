---
series: BLUE_ARCHIVE
artifact_type: character_data_reading
scope: HIFUMI_CHARACTER_DATA_20005
generation: V1
status: active_provisional
source_story_ids:
  - "BA:character_data:20005:profile_and_dialog"
  - "BA:character_data:event_costume:1900900601:character:20005"
source_boundary: "Complete Japanese source objects named in source_story_ids at pinned BA_REFRESH_20260928T032248159554Z; source-facing contextualization, no performed voice or additional supplemental admission"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Hifumi — Swimsuit written baseline and exact event-costume context

## Complete source witness

Pinned root: `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z`; `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. Raw acquisition remains outside analytical Git.

| Complete source | Canonical route | Inspected extent and canonical SHA-256 |
|---|---|---|
| `BA:character_data:20005:profile_and_dialog` | `02_CANONICAL_STORIES/CHARACTER_DATA/HIHUMI/VARIANT_20005.md` | 1 complete profiles; 31 complete written contextual records, including blanks; `6acd1497fefcfecd765700ededcf17b848b61e87f2dfd5bdccbc28c9e4b2e7d5`. |
| `BA:character_data:event_costume:1900900601:character:20005` | `02_CANONICAL_STORIES/CHARACTER_DATA/CONTEXTUAL/BA_character_data_event_costume_1900900601_character_20005.md` | 0 complete profiles; 18 complete written contextual records, including blanks; `0e0ff095ead6b5c1f3f9b481757fa1f4c45cc2dc61d4670ff23adcfe023e8b6a`. |

Raw table provenance:

- `DB/LocalizeCharProfileExcelTable.json` — SHA-256 `f7039fb2bbf78535d4f5aa926cc43a74ddece835d2bea7edc2e46c4bc57b6fe4`.
- `DB/CharacterDialogExcelTable.json` — SHA-256 `dbba21ca2bcdd856498e9eae0c3319309a829e3d0a4ee8d206e9366c28a24b20`.
- `DB/CharacterDialogEventExcelTable.json` — SHA-256 `b630dffc5d86487d1df36bb1f292f78b209e84b435653e5780d73c552b860bb2`.

Positive exact-name identity witness: `阿慈谷ヒフミ` → `BA_PERSON_HIHUMI` → CharacterId `10003` / DevName `Hihumi_default`, `阿慈谷ヒフミ` → `BA_PERSON_HIHUMI` → CharacterId `20005` / DevName `Hihumi_Swimsuit`. Registry method `exact_full_name_jp`, confidence high; registry SHA-256 `eec81b6e81805bddcadb4b7296c41d877e62585b5501fcc9ccc92e5c552a0da3`. Actual profile and scene context distinguish variants; retrieval identity is not an absolute calendar or transfer of acts between outfits. No counterpart identity is invented. Costume joins require their printed OriginalCharacterId witness, detailed in their own written reading.

## Full profile, variant and positive costume witness

The full Japanese profile is `LocalizeCharProfileExcelTable:DataList[66]`, normalized SHA-256 `f520d3e9f379b62c20240d32d909e19c0efb41f5b1fc5e34512bfd94fb8ef7a8`. Exact `阿慈谷ヒフミ` joins source person `BA_PERSON_HIHUMI`, ordinary `10003/Hihumi_default`, and summer `20005/Hihumi_Swimsuit`. The display directory HIFUMI is a spelling alias only. The profile retains second year, 16, 158cm, birthday 11/27, Peroro/cute-goods collecting, shopping and listening to consultations. `Club=None` remains alongside Japanese recruitment and introduction explicitly naming the Remedial Class. Credits YutokaMizu/本渡楓 are metadata, not a performance analysis. The complete weapon description calls the pink, cute-engraved rifle a beach necessity; the contextual weapon question asks whether it is waterproof. Neither proves use at every outing or actual waterproofing.

The introduction explicitly names **Azusa** as the friend who has not visited the sea. It calls acquiring Trinity's Crusader **stealing**, qualified by Hifumi's own 'borrowing', and says the Justice Task Force discovers it. This is written profile context, not a reread or admission of the entire event, and cannot be softened into proved permission because she later cleans school equipment. The profile's general clumsiness/snowballing account is description with particular private evidence both supporting and complicating it, not a mechanism that predicts every future act.

Costume `1900900601` has eighteen raw event rows `548–553/592–597/636–641`, each explicitly **OriginalCharacterId=20005**. `CostumeExcelTable:DataList[2064]` identifies `Hihumi_Event_NPC`, CharacterVoiceGroupId 20005 and resources CH0058; its SHA-256 is `70e960a2acb7c7f20dbbfd006bea724bbdf80aae7ca22439228952f7ef80c643`. The direct event join licenses the identity; matching resources alone would not. Master release/2099 visibility dates are packaging, not chronology.

## Every written context and its mode

All **31** main contextual rows `CharacterDialog:DataList[2474–2504]` were read: one title, one acquisition, five cafe, seventeen lobby, one weapon, six Special. There are **28 Talk and three Think**, no blanks. Cafe `2439–2441` are Think: perceived attention, comfortable warm sunlight and a question about seasonal Peroro goods. Retain reader-access inward text without making other cafe occupants hear it. Talk cafe `2437/2438` gives outfit embarrassment and summer furnishings. Title/acquisition gate rank 1, cafe 15, weapon 25, other contexts 0; these are unlocks, not elapsed time.

Lobby `2442–2448` offers beach/walk enthusiasm, asks about plainness, insists on the toy and its waterproof protection, then cannot find the parked tank. No tank recovery is printed. User birthday `2449/2450` offers the Peroro float; student birthday `2451–2453` declines an additional material wish and values the shared vacation. Such offers and preferences are written conditions, not universally enacted gifts. New Year `2454/2455`, Christmas `2456/2457`, and Halloween `2458` keep season-specific humor: the Halloween reply explicitly says it is an ordinary swimsuit and perhaps out of season. Their raw Anniversary fields are None despite seasonal wording. No one summer date absorbs all of them.

Special `2460–2465` gives humming cleaning, rust concern, shared-equipment return responsibility, spray warning and future swimming. It positively matches E005's timed narrative-shaped lines, without rewriting canonical mode or multiplying one outing into six new encounters. The event object's six contents repeat across EventIDs **803/10803/900803**: sea scent, hoped-for fun, prepared float, missing changing-room key, embarrassment under staring, and arrival excitement. All are Talk, no blanks; original rows are collection-visible, repeats not, all keep UnlockEventSeason803 and ScenarioGroupId10002005. Three appearances in packaging are not three proven new days. The staring objection remains literal; no recovered key or performed delivery is invented.

## Comparison and seven proposals

The ordinary baseline shares tastes and consultation habits; summer adds Azusa-directed action and explicit theft/borrowing tension, outfit audience, sunlight and sea pleasure, common equipment care and boundary requests. Main certified 94 and peer gift to Azusa remain independent accepted evidence. The profile does not return Hifumi to an objective 'ordinary' incapacity or erase institutional limits.

Character adds variants' specific preferences and written self-description; relationship preserves Azusa as named peer, adult invitations and conditional birthday offers; institution retains the theft wording, Justice detection and common-use duty without absolution; Sensei retains audience-sensitive invitations and no claim of completed future help; voice distinguishes Think/Talk, season conditions and the source Special match; motif records Peroro, plainness, sea, tea and return-care as pleasures as well as relational practices; claim revision bounds G08/G09/G10/G12/G13 and rejects automatic repetition/authorization/performance claims. These are **written Japanese baselines**, not audio or a new event-story admission.

## Admission and maintained-surface limits

**ADMIT_WITH_LIMITS proposed** for exactly the complete named objects. All formal alternatives, conditional message routes, printed action, source-form labels and blank contextual records are retained in their proper forms; alternatives and duplicated conditional responses are not simultaneous acts. Reader-access inner text does not become other characters' knowledge. Only explicit local message links and recollections establish relative relations. Episode or publication order does not place encounters against main chapters. Written Japanese and supplied records were inspected; performed delivery, visual gestures, image pixels and audio timing were not.

The seven-ledger/coverage/gap changes remain proposals for the integrating owner, with the family checkpoint reconciling their full extent. Quiet enjoyment, humor, personal wishes and mundane labor remain positive evidence regardless of stakes; contrary acts and literal objections are retained. On semantic acceptance these objects can become ANALYZED with limits without promoting a standalone model or erasing existing main history. G01 private breadth reduces locally; G06 cross-school breadth still requires comparison, G07 chronology remains bounded, G08 repeat/costume/UI forms are distinct, G09 speaker/choice/text forms are retained, G10 performed voice is unadmitted, G12 variant identity is explicit, and G13 legal/clinical/technical outcomes remain unverified where not printed. Main, group, event, mini and unclassified material receives no new admission through this packet. No durable claim ID, monograph, reconstruction or prediction is created: **NO_DIAGNOSTIC_OPPORTUNITY**, because no model was frozen with these sources held out. Shared controls remain parent-owned.
