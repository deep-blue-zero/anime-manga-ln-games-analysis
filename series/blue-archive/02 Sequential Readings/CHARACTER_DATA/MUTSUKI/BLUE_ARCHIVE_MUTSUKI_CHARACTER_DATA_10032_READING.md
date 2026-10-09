---
series: BLUE_ARCHIVE
artifact_type: character_data_reading
scope: MUTSUKI_CHARACTER_DATA_10032
generation: V1
status: active_provisional
source_story_ids:
  - "BA:character_data:10032:profile_and_dialog"
  - "BA:character_data:event_costume:1900902401:character:10032"
source_boundary: "Complete Japanese source objects named in source_story_ids at pinned BA_REFRESH_20260928T032248159554Z; source-facing contextualization, no performed voice or additional supplemental admission"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Mutsuki — Complete New Year written baseline and positively joined event costume

## Complete source witness

Pinned root: `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z`; `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. Raw acquisition remains outside analytical Git.

| Complete source | Canonical route | Inspected extent and canonical SHA-256 |
|---|---|---|
| `BA:character_data:10032:profile_and_dialog` | `02_CANONICAL_STORIES/CHARACTER_DATA/MUTSUKI/VARIANT_10032.md` | 1 complete profiles; 38 complete written contextual records, including blanks; `fb319f96260e3e258799b18742c1007bf33ecf5e4c2365068562888a8dc7c674`. |
| `BA:character_data:event_costume:1900902401:character:10032` | `02_CANONICAL_STORIES/CHARACTER_DATA/CONTEXTUAL/BA_character_data_event_costume_1900902401_character_10032.md` | 0 complete profiles; 68 complete written contextual records, including blanks; `36b21739c843e6a1043dda91eb34e19dded87ec7fdac4bad69a06a84c209c8e3`. |

Raw table provenance:

- `DB/LocalizeCharProfileExcelTable.json` — SHA-256 `f7039fb2bbf78535d4f5aa926cc43a74ddece835d2bea7edc2e46c4bc57b6fe4`.
- `DB/CharacterDialogExcelTable.json` — SHA-256 `dbba21ca2bcdd856498e9eae0c3319309a829e3d0a4ee8d206e9366c28a24b20`.
- `DB/CharacterDialogEventExcelTable.json` — SHA-256 `b630dffc5d86487d1df36bb1f292f78b209e84b435653e5780d73c552b860bb2`.

Positive exact-name identity witness: `浅黄ムツキ` → `BA_PERSON_MUTSUKI` → CharacterId `13006` / DevName `Mutsuki_default`, `浅黄ムツキ` → `BA_PERSON_MUTSUKI` → CharacterId `10032` / DevName `Mutsuki_Newyear`, `浅黄ムツキ` → `BA_PERSON_MUTSUKI` → CharacterId `20059` / DevName `CH0246`. Registry method `exact_full_name_jp`, confidence high; registry SHA-256 `eec81b6e81805bddcadb4b7296c41d877e62585b5501fcc9ccc92e5c552a0da3`. Actual profile and scene context distinguish variants; retrieval identity is not an absolute calendar or transfer of acts between outfits. No counterpart identity is invented. Costume joins require their printed OriginalCharacterId witness, detailed in their own written reading.

## 1. Complete profile, explicit identity and written publication state

LocalizeCharProfile DataList86 is the complete profile, normalized SHA-256 `d36452853fa3933f3674feb354b4955845550e29ccafb0d99ab19296a194ccea`. All Japanese fields, including family reading, SSR introduction, weapon description, status and credits, were inspected. It names 浅黄ムツキ, family reading あさぎ, second year, sixteen, July29,144cm and bomb collecting. Profile Club is `None`, while ClubNameForGacha explicitly says 便利屋68; these are different fields, not contradictory memberships resolved by inventing a club transfer. DoReMi's design/illustration and 大久保瑠美's voice credit are metadata, not performed evidence.

The complete introduction identifies Gehenna PS68's action/assault leader, newly dressed to visit and play at New Year with Aru and the others. It describes continuity of trouble and amusement, a front-row place beside Aru's misadventures, and her own independent enjoyment of the season. This is editorial characterization, not a transcript proving that every described incident happened in every main arc. The status wishes a more enjoyable year; SSR text explicitly invites much play together. The weapon remains トリックオアトリック, stored in her bag with immediate availability and unimpeded pranks attributed to Mutsuki herself. Costume or stored weapon does not independently certify practical capability.

The registry's10032 / Mutsuki_Newyear route positively distinguishes this written baseline from ordinary13006 and dress20059. The event costume has no separate profile: every one of its68raw records has CostumeUniqueId1900902401 and OriginalCharacterId10032. That exact positive witness, plus the registered person, supports co-location here while keeping both canonical IDs separate. No guessed resemblance, erased whitespace or cross-variant merge supplies identity.

## 2. All thirty-eight ordinary contextual records

CharacterDialog DataList3217–3254 covers IDs3178–3215, all38records nonempty. UITitle3178 and Get3179 are separate acquisition/title forms, not an extra story greeting. Cafe3180–3184 retains wanting group hanetsuki, considering play with the adult, a laughter/luck saying, attraction to a toy and teasing consideration of New Year money if she acts affectionate. These personal tastes are positive evidence independently of plot stakes.

UILobby3185–3196 includes recognition of the adult's New Year work, waiting welcome, rock-paper-scissors/can-kicking/hide-and-seek invitations, and a contrary acknowledgment that adults cannot only play and must work. She offers help and encourages finishing work so they can play. Her idea that a long acquaintance might be fate is speculation in this written context, not measured relationship duration. These lines preserve useful effort and consideration without making the later bond timer's alarm informed consent.

Birthday3197–3201 preserves remembering his day and the alleged play promise, asking for celebration of hers, then selecting a shared prank. Holiday3202–3207 includes a deliberately wrong final New Year greeting, acknowledged as wrong when corrected; Christmas-before-New-Year context and further play; a Halloween threat to eat the adult followed by questioning a refusal. They are conditional holiday surfaces rather than one sequential calendar transcript or a performed act. WeaponGet3208 links stronger equipment to more enjoyable play as her expectation. Special3209–3215 names her victory, recognizes his effort, asks what to draw, offers to hear him, changes her mind and decides to cover the face. These seven records closely parallel New Year bond E005's narrator-form0067–0078; retain that form/callback without counting a second independently enacted game.

Unlock fields distinguish Title/Get rank1, Cafe15, Weapon25 and the remaining lobby/special entries0. These are source availability gates, not proof of a chronological development or actual successive speeches. No blank title record exists in this variant; the ordinary13006 blank remains separately preserved.

## 3. Complete event costume: sixty-eight records, not sixty-eight new incidents

All costume records were read with complete Japanese text, category, condition, detail/value, group/order and original identity. Raw indices1098–1113 and1148–1160 form Event809's16lobby+13box-shop lines;1247–1262 and1297–1309 repeat those29lines in10809.1388–1397 supplies ten lobby lines in900809. Across68records there are29distinct Japanese strings. The809/10809 Day6 gate selects two seasonal-game lines, Day13 selects two about becoming bored and playing with the adult as the toy, and Close selects two retrospective pleasure lines.900809 has only the ten ungated lobby lines, not an omitted reconstruction of those gated talks. All use Event season809/scenario group10008005 metadata. `Talk` and `UITalk`, collection and voice identifiers or timing fields are packaging metadata; none is audio listened to here.

Lobby lines greet the working teacher, call for a high five, enjoy Aru's trouble and react to an offertory-box thief. They report a situation and her pleasure; they do not independently establish the event's perpetrator, act sequence or outcome. The peer-reliance passage names Aru, Kayoko and Haruka as relying on him, then answers a question about her own reliance by posing it back and withholding a direct answer. This is deliberately unsettled written reciprocity, not proof she either never relies or has made a full confession. Day-gated hanetsuki, fukuwarai and daruma-otoshi are ordinary play preferences; the shift from toys to playing with the adult remains a potential boundary issue, not a harmlessness certificate.

The entire box-shop set welcomes exchange, urges opening lucky bags, enjoys watching repeated openings, expresses surprise and personal desire for an item, credits her own luck only as a possibility, and asks him to treasure an obtained item as if it were her. Its close lines retain that the event has ended while remaining bags can still be opened. No specific inventory, paid transaction, odds or gambling/financial outcome is supplied. Repetition changes available UI packages without showing new in-world years or additional gratitude episodes.

## 4. Integration proposals and limits

Character: seasonal/group tastes, toy attraction and literal work recognition; relationship: waiting, help offer, peer-reliance claim and unanswered own reliance; institution: exact PS68/Gehenna profile, Schale work addressed, shop context without full event admission; Sensei ethics: preserve the acknowledged need to work and UI refusal question; Japanese: text/metadata, speculative fate and deliberate wrong greeting, distinct special forms; motifs: seasonal play, gift/opening anticipation and E005 face drawing; claim revision: ordinary support for C007/C011 remains finite, C016 must preserve asymmetry and withheld reciprocity. After semantic acceptance these two objects narrow G01/G05 private/written breadth. G07 chronology, G08 repeat/event layers, G09 textual forms, G10 delivery, G12 variant transfer and G13 event/legal/technical/financial outcomes remain open. These lines provide a full written baseline, not a heard voice model or admission of the809 event story package.

## Admission and maintained-surface limits

**ADMIT_WITH_LIMITS proposed** for exactly the complete named objects. All formal alternatives, conditional message routes, printed action, source-form labels and blank contextual records are retained in their proper forms; alternatives and duplicated conditional responses are not simultaneous acts. Reader-access inner text does not become other characters' knowledge. Only explicit local message links and recollections establish relative relations. Episode or publication order does not place encounters against main chapters. Written Japanese and supplied records were inspected; performed delivery, visual gestures, image pixels and audio timing were not.

The seven-ledger/coverage/gap changes remain proposals for the integrating owner, with the family checkpoint reconciling their full extent. Quiet enjoyment, humor, personal wishes and mundane labor remain positive evidence regardless of stakes; contrary acts and literal objections are retained. On semantic acceptance these objects can become ANALYZED with limits without promoting a standalone model or erasing existing main history. G01 private breadth reduces locally; G06 cross-school breadth still requires comparison, G07 chronology remains bounded, G08 repeat/costume/UI forms are distinct, G09 speaker/choice/text forms are retained, G10 performed voice is unadmitted, G12 variant identity is explicit, and G13 legal/clinical/technical outcomes remain unverified where not printed. Main, group, event, mini and unclassified material receives no new admission through this packet. No durable claim ID, monograph, reconstruction or prediction is created: **NO_DIAGNOSTIC_OPPORTUNITY**, because no model was frozen with these sources held out. Shared controls remain parent-owned.
