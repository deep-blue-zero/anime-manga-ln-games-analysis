---
series: BLUE_ARCHIVE
artifact_type: character_data_reading
scope: SERIKA_CHARACTER_DATA_20036
generation: V1
status: canonical
source_story_ids:
  - "BA:character_data:20036:profile_and_dialog"
  - "BA:character_data:event_costume:1900926201:character:20036"
source_boundary: "Complete canonical Japanese source objects named in source_story_ids at pinned BA_REFRESH_20260928T032248159554Z; source-facing contextualization, no performed voice or additional supplemental admission"
source_generation: BA_REFRESH_20260928T032248159554Z
source_commit: a038020f1f5ac02dcfe76962426d38f86414cdd8
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-10-01
updated: 2026-10-01
---

# Serika — swimsuit written baseline and costume1900926201 — serious leisure with limits

## Complete source witness

Pinned generation root: `blue-archive-corpus-pipeline/corpus/GENERATIONS/BA_REFRESH_20260928T032248159554Z`; `electricgoat/ba-data@jp a038020f1f5ac02dcfe76962426d38f86414cdd8`, game `v1.73.459696-r96_3cpn8ebtdjiqi6y9qtn1`, parser `0.2.0`. Raw acquisition remains outside analytical Git.

| Complete source | Canonical route | Inspected extent and canonical SHA-256 |
|---|---|---|
| `BA:character_data:20036:profile_and_dialog` | `02_CANONICAL_STORIES/CHARACTER_DATA/SERIKA/VARIANT_20036.md` | 1 complete profile; 36 complete written contextual records; `423797f965e025e393d0eeabcc3c0bc8b5158a20bef4ca4647027a45031251fb`. |
| `BA:character_data:event_costume:1900926201:character:20036` | `02_CANONICAL_STORIES/CHARACTER_DATA/CONTEXTUAL/BA_character_data_event_costume_1900926201_character_20036.md` | 0 complete profile; 18 complete written contextual records; `f6350e7d8e43fcc05fb30aa1159b51481031b4c21a64b8a142dd96413878e029`. |

Raw table provenance:

- `DB/LocalizeCharProfileExcelTable.json` — SHA-256 `f7039fb2bbf78535d4f5aa926cc43a74ddece835d2bea7edc2e46c4bc57b6fe4`.
- `DB/CharacterDialogExcelTable.json` — SHA-256 `dbba21ca2bcdd856498e9eae0c3319309a829e3d0a4ee8d206e9366c28a24b20`.
- `DB/CharacterDialogEventExcelTable.json` — SHA-256 `b630dffc5d86487d1df36bb1f292f78b209e84b435653e5780d73c552b860bb2`.

Exact scene/choice IDs retain source-record keys and route in `03_STRUCTURED_DATA/utterances.jsonl` and `choices.jsonl`; message IDs retain `Answer` alternatives, conditions, schedule and raw record in `momotalk_messages.jsonl`; written data retain contextual category and record identity. Every source object above was read in full, including all later messages and all alternative routes.

## Two complete objects and exact same-variant identity

Both complete objects are explicitly retained in the source table and front matter: one profile with36 nonempty contextual records, plus a separate18-record event-costume object with no profile. The profile/master resolves `BA_PERSON_SERIKA`, `BA_VARIANT_20036`, devCH0189 and 黒見セリカ. The opaque dev code does not itself mean swimsuit. Actual profile introduction, dialogue about `この水着` and swimsuit log strings in bond 20036:003 establish that condition. Costume1900926201 is independently resolved by `OriginalCharacterId exact profile match` to20036 in `stories.jsonl`; for example its first lobby line routes to `CharacterDialogEventExcelTable.json:DataList[1928]`, event 814. Combining the readings does not merge the objects or omit any record.

The profile retains first-year status, age15, June25 birthday, height153cm and saving/work hobbies while changing the status message to emphatic vacation. It says she faces leisure as seriously as employment, persists despite repeated failures and enjoys time with the committee despite appearing driven. This editorial framing agrees with primary scenes' intense preparation and actual enjoyment, but cannot decide every disputed adult action or prove enduring relaxation. Documentary playable release 2024-06-05 does not timestamp all event-costume triggers, whose documentary date is not given here.

## All 36 profile/dialog records

All shorthand in the following table expands to `BA:character_data:20036`; each category keeps its own `line` numbering and conditional availability.

| Complete profile/dialog category | Exact anchors and repertoire |
|---|---|
| Title/acquisition | `UITitle:line:000001`, `CharacterGet:line:000001`: title phrase and refusal to compromise on a best holiday. |
| Cafe | `Cafe:line:000001–000005`: busy peers, desire for water-gun play, barbecue possibility, possible cleaning, bodily ease. These are distinct conditional utterances, not evidence that every proposed activity happens. |
| Lobby leisure/work | `UILobby:line:000001–000008`: welcome in cool surroundings, complaint about waiting, sea coolness, emphatic group enjoyment, all-out play, fatigue, unwillingness to lose time resting, request for swimsuit appraisal. Real pleasure and self-imposed pressure coexist. |
| Birthdays | `UILobby:line:000009–000012`: proposed shared play, recognition of her own birthday, desire for whole-day company, open question about activity. |
| Annual/seasonal settings | `UILobby:line:000013–000018`: recollection of New Year attire and greeting, question about having been a good child this year and adult appraisal, Halloween distinction between swimsuit and costume qualified by viewpoint. Do not impose all triggers on one summer calendar day. |
| Weapon condition | `WeaponGet:line:000001`: doubt about so much play, attribution of permission to Sensei and demand for responsibility. This is not an executed legal duty. |
| Special lobby | `UILobbySpecial:line:000001–000010`: proposed end/getting off, qualification, rocking protest, overturn warning/stop, rejection of being played with, exasperated recognition, then claim to a reciprocal turn. All ten written records inspected. |

Special-lobby text corresponds to bond 20036:003's narrator-coded/log-tagged sequenceu0031–0048; matching written text and `log=세리카 수영복` support identity while retaining the raw form. They are neither another boat trip nor audio inspection. The hesitation around quitting does not negate direct `やめて` or `人で遊ばないで`. Desire for water-gun play and barbecue are intrinsic positive leads; the profile is not merely a register of defects in vacation management.

## All 18 event-costume lines

The distinct costume object has exactly three six-line blocks: event 814 `UIEventLobby:line:000001–000006`,10814 `000007–000012`,900814 `000013–000018`. Each includes urgent departure, beckoning, enquiry about tasks, questioning what Sensei is doing/whether it is funny and an instruction to stop strange behavior and act. The repeated texts are reused conditional packaging, not eighteen enacted acts or three different development stages. The activity requiring haste and the adult's exact strange behavior are unprinted in these lines. They support written impatience and requested task focus, not an independently reconstructed event plot. No event-class episode is admitted by this two-object reading.

## Deltas, contrary cases and maintained limits

**STRENGTHEN** positive group leisure, freely desired play and familiarity; **REVISE** a purely dutiful persona, effortless relaxation and automatic acceptance of adult play; **PRESERVE** literal stops and role-specific task demands; **OPEN** enacted seasonal outings, rest behavior and performance. Character/relationship proposals add pleasure, appraisal wishes, fatigue, play intensity and desired reciprocity. Institution adds editorial committee vacation and conditional task focus, not event restoration outcomes. Sensei ethics records responsibility requests and stop text without inferring exact hidden actions. Japanese/motif deltas preserve emphatic vacation, conditional jokes, serious leisure and refusals. Claim revision keeps the objects' multiple registers rather than ranking leisure below crisis evidence.

G01/G03 receive this complete written breadth; G08 gains exact event 814/10814/900814 packaging leads, still requiring event plot admission; G12 costume-to20036 identity is positively verified, without asserting every20036 scene depicts current swimwear. G07 retains only explicit internal recollections from the paired primary readings; G09 keeps trigger/log/narrator differences; G10 remains written-only. Exact character_data coverage is two objects, with profile 36 plus costume 18, not one merged54-line source object. New Year and ordinary baselines stay separately bounded.

## Admission and maintained-surface limits

**ADMIT_WITH_LIMITS accepted** for exactly the source objects above. Local explicit recollections and message/scene continuities support the stated relative relations; documentary release, episode number and variant order do not timestamp the acts against main chapters. Context expands repertoire; it does not establish a chronological development edge. Alternative choices and MomoTalk `Answer` records are not cumulative statements. Parenthetical thought gives reader access without automatically giving Sensei or peers the same knowledge. Written Japanese, source-form tags and printed action are inspected; actor delivery, audio timing and image pixels are not.

Inherited comparisons are the V001 C001 checkpoint §§3.2/14.2 and Serika subject section (ordinary boundary, emergency rescue, restored reciprocity), V001 C002 checkpoint (labor/community continuity and criticism of solitary exceptions), V001 C003 E043 (actual customer service at Shiba Seki), and complete group 2101/2102 reading (fallible checking, apology and attempted restraint). Those witnesses remain at their own main/group boundary. Private affection does not erase main E005 refusal, justify pursuit after it, or prove that every rebuke is a concealed invitation. No main or group source is newly admitted by this file.

The source-bounded character/relationship, institution, Sensei ethics, written Japanese, motif and claim deltas are reconciled through cycle002. Coverage is `ANALYZED` for precisely these complete objects; it does not establish whole-character completion. G01 ordinary/private breadth and G03 Serika contextual evidence reduce locally. G07 chronology and G10 performed voice remain open; G09 preserves the stated speaker/choice/form limits. No new durable claim ID, reconstruction model, monograph or prediction: `NO_DIAGNOSTIC_OPPORTUNITY`, because no model was frozen with this source held out. Shared ledgers, indexes, map and gap register remain parent-owned.

## Parent acceptance — cycle 002

[Cycle 002](../../BLUE_ARCHIVE_PHASE2_CONTEXTUALIZATION_CYCLE_002_CHECKPOINT.md) accepts exactly the source IDs declared above after complete contributor inspection, integrator analysis review, canonical/raw witness checks and consequential Japanese/branch tests. Applicable proposals are now reconciled in all seven ledgers and the current contextual coverage/control surfaces. This acceptance supplies contextual repertoire; no main chronology, performed voice, model promotion or prospective validation is inferred. The cycle owns admission; this packet is not a second admission count.
