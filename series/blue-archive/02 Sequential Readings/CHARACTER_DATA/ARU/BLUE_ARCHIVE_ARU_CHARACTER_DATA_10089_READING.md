---
series: BLUE_ARCHIVE
artifact_type: character_data_reading
scope: ARU_CHARACTER_DATA_10089
generation: V1
status: active_provisional
source_story_ids:
  - "BA:character_data:10089:profile_and_dialog"
source_boundary: "Complete Japanese source objects named in source_story_ids at pinned BA_REFRESH_20260928T032248159554Z; source-facing contextualization, no performed voice or additional supplemental admission"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Aru — dress complete written profile and contextual baseline

## Complete source witness

Pinned root: `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z`; `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. Raw acquisition remains outside analytical Git.

| Complete source | Canonical route | Inspected extent and canonical SHA-256 |
|---|---|---|
| `BA:character_data:10089:profile_and_dialog` | `02_CANONICAL_STORIES/CHARACTER_DATA/ARU/VARIANT_10089.md` | 1 complete profiles; 42 complete written contextual records, including blanks; `c9bfaad3bef1e1178fe227fbe97f0844c265b585f987c4815ffece7489685362`. |

Raw table provenance:

- `DB/LocalizeCharProfileExcelTable.json` — SHA-256 `f7039fb2bbf78535d4f5aa926cc43a74ddece835d2bea7edc2e46c4bc57b6fe4`.
- `DB/CharacterDialogExcelTable.json` — SHA-256 `dbba21ca2bcdd856498e9eae0c3319309a829e3d0a4ee8d206e9366c28a24b20`.

Positive exact-name identity witness: `陸八魔アル` → `BA_PERSON_ARU` → CharacterId `10000` / DevName `Aru_default`, `陸八魔アル` → `BA_PERSON_ARU` → CharacterId `10031` / DevName `Aru_Newyear`, `陸八魔アル` → `BA_PERSON_ARU` → CharacterId `10089` / DevName `CH0240`. Registry method `exact_full_name_jp`, confidence high; registry SHA-256 `eec81b6e81805bddcadb4b7296c41d877e62585b5501fcc9ccc92e5c552a0da3`. Actual profile and scene context distinguish variants; retrieval identity is not an absolute calendar or transfer of acts between outfits. No counterpart identity is invented. Costume joins require their printed OriginalCharacterId witness, detailed in their own written reading.

## Complete profile and positive dress context

The complete Japanese profile is `LocalizeCharProfile` DataList179, normalized SHA-256 `d57fb7651974416fe191f17ad260cccad2ae106491214fb52eb58f5caccdeb6d`; all 42 contextual records at `CharacterDialog` DataList7376–7417 are nonempty. The full profile, rather than the shortened canonical list alone, supplies status, weapon, acquisition and creator fields. Registry `CH0240`, the infiltration introduction and dress-specific scenes provide the positive local-person context. Same name supports retrieval, not transference of every ordinary/New-Year act.

It preserves 陸八魔アル / `りくはちま`, Gehenna/便利屋68, second-year/sixteen, March12/160 cm and management study, with ClubNone separate from the positive club labels. Its editorial introduction describes a president who accepted an **infiltration commission**, wears uncommon clothing well, is excited by a wished-for hard-boiled job but does not show it on her face. Those are profile characterizations, not inspected performance, completed mission or proof of an unchanging concealed emotion. This profile uses president rather than mechanically reusing the ordinary “self-styled” qualification; source language is retained rather than harmonized.

Status calls it an important commission, and the SSR line anticipates the day finally arriving. The cherished **ワインレッド・アドマイアー** is a sniper rifle retained even in a special assignment, its beauty rhetorically brighter in a gorgeous setting. No mechanism, exact mission result or lethal capability test follows. DoReMi and 近藤玲奈 remain designer/actor metadata, not admitted audio.

## Complete contextual partitions

| Partition | Exact IDs / raw indices / conditions | Positive written evidence and limits |
|---|---|---|
| Title/acquisition |Title000001 / CharacterGet000001;7376–7377; Idle/rank1 | Nonempty title; asks commission versus business proposal and explicitly says the visit itself makes her happy. Not a completed commission or performed greeting. |
| Café |Cafe000001–000005;7378–7382; Idle/rank15 | Unidentified-person worry, liking the atmosphere, wanting a sizeable job/good trading partner and asking how to meet monthly operating costs. The unknown figure is not silently identified as Hina, a target or another guest; no audited insolvency. |
| Core lobby |UILobby000001–000014;7383–7396; first4 Enter / rest Idle; rank0 | Work/escort invitations, “special” context, wanted outing, mediated dress compliment, cost worry over cleaning with denial of having said it, and **permission to discuss subjects other than work**. No actual escort/date, cleaning bill or independent spoken compliment. |
| Birthdays |UILobby000015–000019;7397–7401; adult-greeting first3 Enter / own reply last 2 Idle; rank0 | Adult birthday remembered; her own birthday recognition surprises her and prompts thanks. Not a verified attended celebration or mutual romance declaration. |
| Seasonal lobby |UILobby000020–000025;7402–7407; Enter/rank0 | New-Year cooperation assertion, an otherwise ordinary day made meaningful with Sensei, festive-city observation and party question. Invitation and projected meaning are not a completed party, all-year contract or absolute outfit calendar. |
| Weapon |WeaponGet000001;7408; Idle/rank25 | Long acquaintance/trust, continued association and saying these words are enough. Relational expression is not a narrated new weapon test or actual signed commitment. |
| Special |UILobbySpecial000001–000009;7409–7417; Idle/rank0 | Nine written ramen/after-work entries parallel dress E003: unexpected but welcome outcome, tentative understanding of well-dressed adults' ordinary eating and wondering whether she has drawn nearer to Sensei. Not a second outing or independent audio/gesture performance. |

## Wants beyond the work role, and contrary concerns retained

The written pool explicitly allows nonwork conversation while keeping finance, work and client wishes present. Atmosphere, direct company, dress pleasure and a possible party are positive ordinary evidence; an interpretation that she only speaks in business purposes cannot absorb the actual “other than work” line. Conversely, enjoyment does not erase monthly-cost worry, cleaning expense or the unnamed-person concern. Questions and denials remain in the record without being converted to a ledger balance or full event.

The Special comparison with the paired complete E003 preserves tentative “a little” understanding rather than adult status attained. Its source-level first-person words do not provide universal adult motives or a new separate complaint transcript. Her earlier scene can refuse consolation while the contextual pool offers company; the two situations are retained rather than collapsed into a permanent preference always to be praised.

## Proposed maintained deltas

Character and relationship proposals add atmosphere/taste, nonwork discussion, desired visits/outings and specific recognition alongside cost/identity concerns. Institution proposals keep expenses and trading-partner wishes as questions with unresolved solvency, and the infiltration introduction as editorial provenance rather than whole-plot admission. Sensei ethics receives situated written invitations and mediated replies, no new enacted job or date. Japanese voice/motif proposals retain work footing, direct enjoyment of a visit, financial vulnerability, denials and tentative after-work understanding.

Coverage proposal is exactly one complete written object, one profile/42 nonempty entries, with all conditions/ranks preserved. G08 profile/UI/Special contexts remain separate from event admission; G09 unidentified referent and mediated forms, G10 performed voice and G13 legal/financial/technical outcomes remain bounded. No reconstruction or model-state upgrade follows.

## Admission and maintained-surface limits

**ADMIT_WITH_LIMITS proposed** for exactly the complete named objects. All formal alternatives, conditional message routes, printed action, source-form labels and blank contextual records are retained in their proper forms; alternatives and duplicated conditional responses are not simultaneous acts. Reader-access inner text does not become other characters' knowledge. Only explicit local message links and recollections establish relative relations. Episode or publication order does not place encounters against main chapters. Written Japanese and supplied records were inspected; performed delivery, visual gestures, image pixels and audio timing were not.

The seven-ledger/coverage/gap changes remain proposals for the integrating owner, with the family checkpoint reconciling their full extent. Quiet enjoyment, humor, personal wishes and mundane labor remain positive evidence regardless of stakes; contrary acts and literal objections are retained. On semantic acceptance these objects can become ANALYZED with limits without promoting a standalone model or erasing existing main history. G01 private breadth reduces locally; G06 cross-school breadth still requires comparison, G07 chronology remains bounded, G08 repeat/costume/UI forms are distinct, G09 speaker/choice/text forms are retained, G10 performed voice is unadmitted, G12 variant identity is explicit, and G13 legal/clinical/technical outcomes remain unverified where not printed. Main, group, event, mini and unclassified material receives no new admission through this packet. No durable claim ID, monograph, reconstruction or prediction is created: **NO_DIAGNOSTIC_OPPORTUNITY**, because no model was frozen with these sources held out. Shared controls remain parent-owned.
