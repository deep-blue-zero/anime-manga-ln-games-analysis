---
series: BLUE_ARCHIVE
artifact_type: character_data_reading
scope: MUTSUKI_CHARACTER_DATA_20059
generation: V1
status: active_provisional
source_story_ids:
  - "BA:character_data:20059:profile_and_dialog"
  - "BA:character_data:event_costume:1900955201:character:20059"
source_boundary: "Complete Japanese source objects named in source_story_ids at pinned BA_REFRESH_20260928T032248159554Z; source-facing contextualization, no performed voice or additional supplemental admission"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Mutsuki — Complete dress written baseline and exact event costume

## Complete source witness

Pinned root: `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z`; `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. Raw acquisition remains outside analytical Git.

| Complete source | Canonical route | Inspected extent and canonical SHA-256 |
|---|---|---|
| `BA:character_data:20059:profile_and_dialog` | `02_CANONICAL_STORIES/CHARACTER_DATA/MUTSUKI/VARIANT_20059.md` | 1 complete profiles; 50 complete written contextual records, including blanks; `4f8dd1c7e10f10b6de7ca128f890b0525aaafdcfc2723da498e52c995779cc62`. |
| `BA:character_data:event_costume:1900955201:character:20059` | `02_CANONICAL_STORIES/CHARACTER_DATA/CONTEXTUAL/BA_character_data_event_costume_1900955201_character_20059.md` | 0 complete profiles; 18 complete written contextual records, including blanks; `9f4374d5a368f17f38ce1ab6c6618336abcbce44b4773a4acb41adedb94dad5e`. |

Raw table provenance:

- `DB/LocalizeCharProfileExcelTable.json` — SHA-256 `f7039fb2bbf78535d4f5aa926cc43a74ddece835d2bea7edc2e46c4bc57b6fe4`.
- `DB/CharacterDialogExcelTable.json` — SHA-256 `dbba21ca2bcdd856498e9eae0c3319309a829e3d0a4ee8d206e9366c28a24b20`.
- `DB/CharacterDialogEventExcelTable.json` — SHA-256 `b630dffc5d86487d1df36bb1f292f78b209e84b435653e5780d73c552b860bb2`.

Positive exact-name identity witness: `浅黄ムツキ` → `BA_PERSON_MUTSUKI` → CharacterId `13006` / DevName `Mutsuki_default`, `浅黄ムツキ` → `BA_PERSON_MUTSUKI` → CharacterId `10032` / DevName `Mutsuki_Newyear`, `浅黄ムツキ` → `BA_PERSON_MUTSUKI` → CharacterId `20059` / DevName `CH0246`. Registry method `exact_full_name_jp`, confidence high; registry SHA-256 `eec81b6e81805bddcadb4b7296c41d877e62585b5501fcc9ccc92e5c552a0da3`. Actual profile and scene context distinguish variants; retrieval identity is not an absolute calendar or transfer of acts between outfits. No counterpart identity is invented. Costume joins require their printed OriginalCharacterId witness, detailed in their own written reading.

## 1. Complete written profile and positive variant route

LocalizeCharProfile DataList271, normalized SHA-256 `8bf36dfcd6056e878a1cbc8ee4d3270f5c62286f632316ac9d4641980f491113`, supplies all Japanese profile fields. Name/family reading, second-year sixteen-year-old status, July29,144cm, bomb collecting, PS68 gacha-club field and credits remain explicit. Club is `None` separately from the named gacha club. DoReMi design/illustration and 大久保瑠美 voice attribution are printed metadata; no performance is admitted. Weapon トリックオアトリック is carried for pranks even in dress, an editorial description rather than a weapon-result test.

Status explicitly says she is playing infiltration; the introduction identifies Gehenna's PS68 action/assault leader changing into a dress for an infiltration mission while her prankishness remains visible, possibly without intending to hide it. That final possibility is editorial hedging, not a verified universal intention. SSR text asks to play more flamboyantly. These fields differ materially from the ordinary and New Year baselines without forcing global time or growth between them.

CharacterId20059/DevNameCH0246 positively joins BA_PERSON_MUTSUKI through 浅黄ムツキ. The selected event costume's18rawrecords all have CostumeUniqueId1900955201 and OriginalCharacterId20059; it has no independent profile. Those exact fields justify this combined reading while preserving two distinct canonical IDs and their actual hashes. Character10032's New Year costume cannot be silently substituted because both belong to the same person.

## 2. All fifty CharacterDialog records, including ordinary pleasure and contrary forms

CharacterDialog raw11698–11747 contains50nonemptyrecords. UITitle and CharacterGet are acquisition/UI forms, the latter offering a transformed appearance and asking what he wants. Cafe lines000001–000005/raw11700–11704 preserve wanting a group dress party, a teasing inference about the adult's taste, looking for someone to play, interest in manipulating an object, and explicitly liking the cafe. The last liking is an independent quiet preference, not proof of an incident in an unadmitted event.

The28complete UILobby lines/raw11705–11732 distinguish entering/waiting welcome and play, a claim to appear more grown up, a dress-reason quiz and conditional present/chair penalty, inviting the adult to choose more grown-up play, being called older sister, and wanting him to use that address. Actual profile age remains sixteen; a dress and quotation-marked adult claim do not change age, authority or relationship status. Lines000016/000017 say she chose the dress with PS68's other members and wants to care for it as a special memory. This ordinary material attachment and collective choice remain positive evidence without inventing a shopping scene or chronology.

Birthday000018–000021 recalls his day and proposes a party, thanks him for her celebration, and asks whether her dress pleased him. Holiday000022–000028 wishes shared New Year fun, wonders about wearing a dress at Christmas and invites investigation, and jokingly says its red colour hides blood before expressly retracting that as a trick. That retained retraction prevents a bloodstained-dress act or casualty record from being inferred. These are occasion-conditioned UI entries, not all holidays occurring in one continuous story. WeaponGet/raw11733 likes the weapon's felt response as written personal evaluation, without ballistic evidence.

The14complete UILobbySpecial/raw11734–11747 parallels dress E005's log-tagged narrator sequence: trust, non-indiscriminate pranks, delegation over money, meaningful use, donation/activity funding/retention for their future, then unresolved teasing about meaning. Preserve it as a written special-context form. It is not a second completed transfer, actual donation or future commitment. Title/Get availability rank1, Cafe15, Weapon25 and lobby/special0 are source gates rather than dates or progress in a heard voice trajectory.

## 3. All eighteen event costume rows and repeated packaging

Raw5020–5025 (834),5094–5099 (10834) and5133–5138 (900834) each contain the same six complete UIEventLobby strings: two Enter and four Idle, all detailNone/value0. The900834 display orders are240–290 instead of600–650; the written strings are unchanged. EventUnlockSeason834 and ScenarioGroupId10032005 accompany all18rows; all are Talk. This exact packaging covers six distinct Japanese lines, not18new events or three in-world performances. No Day/Close/shop rows are present to reconstruct from another student's costume.

The six lines anticipate an entertaining incident, liken practice and performance to pranks, tentatively select an infiltration route, ask whether he wants play and invite opera after work. Route selection remains tentative; no successful infiltration result is independently verified by UI dialogue. The opera invitation is a positive ordinary lead to compare with complete dress E006's explicit earlier work recollection and actual later appreciation. It does not independently admit or summarize the full834event, establish a completed earlier opera visit or assign an absolute year.

## 4. Seven-ledger and gap proposals

Character: group party/cafe pleasure, care for a shared-chosen dress, prank continuity, opera preference and withheld money-joke meaning; relationship: waiting, adult-directed choice invitation, address play and finite trust; institution: exact PS68/Gehenna profile and positively joined event surface without independent mission outcome; Sensei ethics: distinguish prompted adult taste/address from verified intention and keep age/state explicit; Japanese: source forms, occasion lines and literal blood-joke retraction; motifs: dressed persona, valued clothing, opera and E005 trust callback; claim revision: C007/C011/C016 receive limited ordinary reciprocity, while C017 cannot turn identity/provenance or trust into legal legitimacy. Acceptance narrows G01/G05 only for these two written objects. G07 chronology, G08 repeat/event package differences, G09 UI versus scene form, G10 performed voice, G12 state transfer and G13 technical/legal/financial outcomes remain limited. The quiet preferences are retained alongside contrary private conduct.

## Admission and maintained-surface limits

**ADMIT_WITH_LIMITS proposed** for exactly the complete named objects. All formal alternatives, conditional message routes, printed action, source-form labels and blank contextual records are retained in their proper forms; alternatives and duplicated conditional responses are not simultaneous acts. Reader-access inner text does not become other characters' knowledge. Only explicit local message links and recollections establish relative relations. Episode or publication order does not place encounters against main chapters. Written Japanese and supplied records were inspected; performed delivery, visual gestures, image pixels and audio timing were not.

The seven-ledger/coverage/gap changes remain proposals for the integrating owner, with the family checkpoint reconciling their full extent. Quiet enjoyment, humor, personal wishes and mundane labor remain positive evidence regardless of stakes; contrary acts and literal objections are retained. On semantic acceptance these objects can become ANALYZED with limits without promoting a standalone model or erasing existing main history. G01 private breadth reduces locally; G06 cross-school breadth still requires comparison, G07 chronology remains bounded, G08 repeat/costume/UI forms are distinct, G09 speaker/choice/text forms are retained, G10 performed voice is unadmitted, G12 variant identity is explicit, and G13 legal/clinical/technical outcomes remain unverified where not printed. Main, group, event, mini and unclassified material receives no new admission through this packet. No durable claim ID, monograph, reconstruction or prediction is created: **NO_DIAGNOSTIC_OPPORTUNITY**, because no model was frozen with these sources held out. Shared controls remain parent-owned.
