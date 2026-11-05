---
series: WUWA
character: Zani
artifact_type: source_census_chronology_identity_audit
scope: ZANI_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: ZANI_PRE_AV_V0_1
status: draft_noncurrent
release_state: author_working_draft_pending_owner_review
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
source_generation_frozen: true
source_freeze_metadata: conflicting_collection_and_embedded_lock_fields
text_authority: zh-Hans
localization_witnesses: [en, ja, ko]
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
---

# Zani — source census, chronology, and identity audit

This is a selected-collection audit, not a claim to every future game version or every possible graph path. Its authority is the frozen normalized Arikatsu semantic view, with the installed client supplying separate raw audio evidence. Local private roots are `ANALYSIS/Characters/Zani/` and `_voice_media/character/complete_voice_corpus/Zani/v0_1/`. The source pin is the commit in the front matter. In the locators below, `flow#/N/A/I` expands to `wuwa://353f2eaed119bc9f680eab92807d20ac75a79b40/BinData/flowState/flowstate.json#/N/Actions!/A/Params/TalkItems/I`. `FavorWord_...` and `FavorStory_...` are exact text keys, not quotations. Consult the source JSON and crosswalk for their full locators.

## Denominators and scope

| Scope | Selected count | Meaning / exclusion |
|---|---:|---|
| Raw relevant flow states | 225 | Full selected action/transition records, not 225 unique scenes. |
| Contextual text keys | 2,954 | Includes non-Zani dialogue/context; not 2,954 Zani utterances. |
| Quest-reference records / distinct quest IDs | 123 / 21 | Links for navigation, not separate evidence of 123 episodes. |
| Direct identity candidates | 960 | 938 accepted solo, 18 rejected, four unresolved. |
| Accepted direct occurrences | 938 | 840 source-voiced, 98 source-unvoiced. |
| Favor stories / archive voice entries | 5 / 72 | Story records are prose, not 5 audio lines. |
| Selected semantic voice lines | 912 | 840 voiced direct occurrences plus 72 archive entries. |
| Render associations / runtime object rows | 3,653 / 3,521 | Variants and reused PCM make these different denominators. |
| Distinct PCM/FLAC objects | 3,517 | 794,823,372 FLAC bytes; all 3,517 measured locally with zero failures. |
| Missing normalized text witnesses | 8 | Two semantic lines, each with four language renders, at `flow#/4657/1/0–1`. Audio remains verified; words are **not** supplied by this packet. |
| WavesLine message records | 1 | Metadata shell `shortmessage.json#/78`, chat partner 48; five source-accepted text items at `flow#/14525/1/0–4`. Do not call the shell a fully reconstructed in-game phone exchange. |

The 72 archive words are 72 distinct `BinData/favor/favorword.json` rows, each joined by its exact locator and **actual** raw `Content` key to a complete semantic voice record: 72 events and 288 distinct four-dub PCM-valid objects. The 41 attack/skill/liberation/damage/fallen/traversal/reward rows at `favorword#/2193–2233` contribute 41 events/164 objects inside those archive and full selected totals; they are not additional story-action acoustic cohorts. Seventeen consecutive raw IDs `150737–150753` differ from their actual key suffix by a two-position rotation with wrap. An ID-derived key can name a different valid Zani sound. The [exact source-key and combat-labor profile](../01%20Evidence%20and%20Source-Facing/WUWA_ZANI_ARCHIVE_SKILL_KEY_AND_COMBAT_LABOR_PROFILE.md) lists all 17 locators and event IDs. No combat line alone establishes a dated hit, leave decision or canonical fall.

The source collection's `COLLECTION_AUDIT.json` reports `valid: true`, `collection_integrity_valid: true`, `voice_completeness_valid: true`, `source_generation_frozen: true`, and normalized `status: active_provisional`. This draft's `draft_noncurrent` status refers to *this analytical packet*, not the frozen source. Official-client FLAC verifies bytes and language-specific renders, not independently Zani's semantic assignment.

## Identity decisions that matter

- Playable Zani's role identity is 1507; direct story speaker IDs include 1477 and communication/event variants such as 100070, 1588, 50071, 701106, and 800314. These are explicit crosswalk records, not an assumption that every similar-looking identifier is Zani.
- The hidden opening at `flow#/4204/2/0` is accepted because the same attendant immediately names herself at item 1. The decision is narrow and does not generalize to all anonymous openings.
- `flow#/4242/2/1–5` is the Imperator manifestation; `4246/4/1,3–5` is Masked Reverie/Nyarla context; `4599/1/0` is hostile/chorale context; `4606/3/7–11` is Carlotta's entrance. These eighteen total rejected candidates are not training examples of Zani's speech.
- `8862/2/3–4` and `8864/3/0–1` remain unresolved. The scene contains both Zani and Carlotta, but no exact per-line assignment for those four hidden items. Do not backfill them from gender, proximity, or style.
- The `8864/3/5–9` confrontation belongs to Galbrena/Fenrico context, not Zani. The source crosswalk, not a friendly label or branch-wide presence, controls attribution.

## Source-time reading order

The following is a narrative *working order*, not a timestamp proof. Profile/favor unlock order, optional player choices, and later version insertions do not necessarily match strict diegetic time.

1. **Prior assault / awakening / early employment.** `FavorRoleInfo_1507_TalentDoc` says she was severely injured in an assault by redacted perpetrators and awakened her Forte while repelling them; exact origin and assailants remain unknown. The in-world document describes horns, tail, diagonal Tacet Mark and healed energy-focusing marks. `FavorStory_150703_Content` is partly workplace rumor about an initially inexperienced, forceful employee who quickly mastered procedure. Its speculation about hidden pay, ambition or a Montelli surname is not narrator-confirmed motive.
2. **Bank reception and Ragunna case.** `flow#/4204/2` starts formally with account/service and guide duties, includes an efficient internal-command register, then permits relaxed address. `4241/5`, `4243/3`, `4245/2` and `4577–4609` show food knowledge, investigation of Echo harm and the Fisalia/Order problem, and a cautious mix of loyalty, inference, and self-correction. At `4245/2`, Fulmine's projected record cannot solve the broad outside-city search, while a masked figure and Montelli-looking clothing support inquiry, not a verified culprit. Her statements about Montelli innocence or particular suspects are situated beliefs, not omniscient verdicts [ZAN-E44, C43].
3. **Averardo Vault / Lorelei.** `flow#/5600–5665` places her in security/investigative work alongside Rover and Phoebe. She can tease Phoebe's prayer, yet herself invokes the Sentinel in danger at `5651/1`; “secular” must not be flattened into never praying. She recognizes Noah as more than disposable transport and revises assumptions as the Vault case unfolds. Four-language `QuestTree_Summary_230301` retrospectively reports that an Order-supplied “relic” is an evidence-erasure device and **Phoebe** resolves the immediate crisis; Zani's participation is not sole power-action attribution or proof of prior knowledge. EN alone calls the device a bomb.
4. **Black Alley / Blazing Nightwalker.** Her character quest `flow#/7295–7557` exposes the vigilante identity, her critique of its name, a self-admitted earlier overreaction and Montelli intervention (`7301/4`), differentiated culpability for Colleen (`7300/3`), Colleen's right to suspect a Montelli-supplied Terminal and Zani's duty to prevent misuse (`7411/7`), a fabricated employee “Protocol 8” pretext (`7435–7436`), a pressured missing-person inquiry and contested Colleen guide decision (`7552/2`), rescue delegation (`7555/4`), and deliberately frightening Talos (`7556/3`). Do not make this either spotless heroism or unbounded cruelty. At `7411/7` Rover, not Zani, states the conditional-help ultimatum; the feared supplier is not confirmed. At `7552/2` Rover, not Zani, offers Colleen a safety guarantee, and the listed sequence does not prove a completed rescue or Zani-inflicted injury to the gang member.
5. **Aftermath and non-identical later states.** `7953/1` recalls wishing as a child that someone would stand up for her. In `8585/5`, convicted leaders are distinguished from coerced or minor members; Zani helps secure a family support fund and stalls. `8586/10` and `8819/10` duplicate the night-city exchange: one text witness duplicated in the selected collection, not two independent episodes. `9930/4` puts people above Vault collections, `9950/2` lets a colleague rest, and `9968/2`/`11786/2` repeat a voluntary overtime line for Carlotta. `12439/7` then explicitly says promised paid leave has happened, while rest remains psychologically difficult. This is state evolution, not proof she is permanently unable to change.

## Graph and uncertainty controls

The local `RAW_RELEVANT_FLOW_STATES.jsonl`, `SCENE_AND_EVIDENCE_LEDGER.jsonl`, and `occurrence_identity_crosswalk.jsonl` preserve graph actions and per-occurrence assignments. Branch alternatives within `4245`, `7298`, `7300`, `7301`, `8586`, and `12439` should be treated as alternatives where the graph says so; this packet does not combine every optional player response into one witnessed conversation. In `4245/2`, two two-way player forks produce alternative celebrity/business and masked-suspect remarks, with shared rejoins; sixteen accepted Zani source occurrences mean twelve or fourteen on a listed route, not sixteen in one. The two alternative investigation-request keys have the same wording and per-dub WEM/PCM, reducing 64 render associations to 60 unique PCM objects. Quest `114000027` points to the state, but no route is watched [ZAN-E44]. In the mixed-speaker `7411/7` action, seventeen accepted Zani turns are source-voiced with 68 PCM-valid render associations already inside the selected denominator. The three Rover response options at TalkID 31 have empty action arrays, so their exact executed reply mapping is not proved by this row. The two missing text keys are `Main_Linaxita_2_2_91_1` and `_91_2`, at `4657/1/0–1`, in **all four** normalized languages. The private waveform adapter marks source-linked written rates `missing_source_text_witness`; the verified audio is not a license to invent a transcript.

The selected 15-case metadata audio join has 63 render records because some semantic cases have additional render variants; it is not an assertion of 63 distinct narrative lines. It exists to retrieve exact text → semantic occurrence → runtime variant → WEM → PCM/FLAC and to support claim-targeted human listening later. No human listening or runtime video inspection is represented here.
