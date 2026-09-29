---
series: WUWA
character: Augusta
artifact_type: source_census_chronology_identity_audit
scope: AUGUSTA_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: AUGUSTA_PRE_AV_V0_1
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

# Augusta — source census, chronology, and identity audit

This is a bounded selected-collection audit, not a claim to every graph path or later client version. Source shorthand `flow#/N/A/I` expands to `wuwa://353f2eaed119bc9f680eab92807d20ac75a79b40/BinData/flowState/flowstate.json#/N/Actions!/A/Params/TalkItems/I`; favor/profile keys refer to the exact multilingual records in the local `character_source_package.json`. The Chinese text is the semantic anchor; English, Japanese and Korean are witnesses. Raw official-client audio and pinned normalized Arikatsu semantics have distinct authority.

## Denominators

| Selected scope | Count | Meaning / caution |
|---|---:|---|
| Raw relevant flow states | 207 | Full embedded actions and transitions, including other speakers. |
| Contextual text keys | 4,055 | Context, not 4,055 Augusta lines. |
| Quest references / distinct quest IDs | 108 / 18 | Retrieval links, not a count of independent episodes. |
| Direct identity candidates | 660 | 643 accepted solo, 12 rejected, five unresolved. |
| Accepted direct occurrences | 643 | 537 source-voiced and 106 source-unvoiced. |
| Favor stories / archive voice entries | 5 / 68 | Prose stories are not voice objects. |
| Raw archive IDs with different Content-key suffixes | 37 / 68 | Combat/traversal/reward rows need exact locator and actual Content joins; a synthesized key may name another valid bark. |
| Semantic voice lines | 605 | 537 accepted voiced direct plus 68 archive entries. |
| Render associations / runtime rows | 2,420 / 2,400 | All four dub scopes have 605 semantic links; variants/reuse differ. |
| Unique native PCM/FLAC objects | 2,399 | 673,191,997 FLAC bytes; 2,399/2,399 locally measured, zero failures. |
| WavesLine shells | 1 | Five accepted message talk items at `flow#/14526/1`; shell content remains metadata-only and two other items are not hers. |

`COLLECTION_AUDIT.json` reports collection and voice completeness valid, `source_generation_frozen: true` and normalized `status: active_provisional`. This *interpretive draft* is `draft_noncurrent`; source freeze is not an authority-status synonym. The 18 selected matched-audio cases each span four languages (72 renders), but are not the full corpus.

The 37 mismatches are all in raw IDs `130632–130669` except the absent raw `130650`; they occupy `favorword#/2506–2539` and `#/2620–2622`. They join 37 complete four-dub semantic voice rows, 37 event IDs and 148 distinct locally PCM-valid renders. The [exact row/key map](WUWA_AUGUSTA_COMBAT_TRIGGER_AND_ARCHIVE_KEY_IDENTITY_PROFILE.md) is a reverse provenance aid, not a proof that every gameplay trigger was observed. In particular, raw `130645` is key `FavorWord_130632_Content`, while `FavorWord_130645_Content` belongs to another raw row. The voice census of 605 lines already includes these 37; neither the row count nor the 148 renders should be added again to the total.

## Exact identity boundaries

- Playable role 1306 is Augusta; story variants include source speaker 250022, childhood 350015, youth 350093, communications 350092 and message speaker 701107. `ROLE_VARIANTS.json` retains distinctions. The analysis does not globally equate anonymous speaker 178 with her.
- At `flow#/7804/4/0`, an unnamed speaker addresses Iuno and immediately continues as Augusta; accepted **for that occurrence only**. At `9509/2/7`, an unnamed entrance exclamation continues as Augusta and is accepted but explicitly source-unvoiced.
- `8724/2/0–3` is Bruno, and `8793/10/29–37` is Nestor's discussion of Augusta, not Augusta's speech. `9333/1/6–8` belongs to a male hunter; `9491/4/23–26` to Kharon. The selected crosswalk has twelve rejected candidates total; preserve their speaker contexts.
- Five items at `9965/5` are an unnamed relic donor and lack positive Augusta attribution. They remain unresolved, not automatically assigned because Augusta appears nearby. The identity audit is a lower bound on recall beyond marked/nominated candidates.

## Working source-time order and tension points

1. **Fabianum, childhood and Forte.** `FavorRoleInfo_1306_TalentDoc` describes a near-childhood Resonance history, hand Tacet Mark and magnetism over roughly ten meters, with an observed developmental ceiling. The examiner initially dismisses its combat value; this is an in-world judgment, not an objective cap on her overall competence. `FavorStory_130601_Content` records repeated defeats by Cato, fear, and a whisper encouraging her to rise. Later story reveals the Dark Tide/Sovereign voice's cruel aspect; do not treat every whispered “lesson” as benign self-talk.
2. **Arena ethic and anti-entitlement choice.** In `FavorStory_130602_Content`, the whisper tempts her to treat the weak as fuel while nobles arrange a lethal free-for-all. She enters the arena herself, recognizes opponents by name, invites direct challenge rather than a restricted right, and wins without killing. Archive `FavorWord_130611_Content` says she took defeated blades to spare their owners and later reformed lethal arena practice. These are bounded facts, not a general no-kill oath in every battlefield.
3. **Magno, Fabianum and rule.** `FavorStory_130603–130604_Content` moves from admiring Magno's heroic image to seeing exhaustion and institutional failure; Magno admits withholding help from Fabianum. His poisoned death has competing accounts, while Augusta *imagines* a particular final toast. Do not report suicide or Senate assassination as proven. She accepts Ephor's crown as both honor and shackle, intending to face Senate opponents beyond the arena.
4. **Septimont mainline, prophecy and shared heroism.** First major Rover encounter at `flow#/8363/3` combines martial respect, a delayed-appointment apology, hunt risk, a political exception and trust. The exact `311000001` action chain `8371/3 → 8380/3 → 8388/4` moves from Wedge-range and intelligent-prey constraints, through a *planned* three-stone drive and revised walking route, to a failed Iuno–Augusta strategy, conditional Black Shores/Buling consultation and offered Gladiator support. The hunt's later joint victory is retrospective `QuestTree_Summary_210080`, not an already observed result of the three-stone instructions. `8402/4` addresses prejudice against her modest Forte, Senate manipulation and childhood disadvantage; at `/29–30` Augusta reports finding Angel after Oak Hollow, seeing intensified Resonance and an uncontrolled monstrous transformation, and never seeing her again. The inside-hollow mechanism and later outcome remain open. `8797/4` shows assertive handling of senators and a familiar, protective rapport with Iuno. `7804/4` is a prophecy/fate debate with Iuno; `8422/2` later credits companions and generations, offers a non-exclusive Hero of Heroes reading and admits a gamble around Rover's “unwritten fate.” Quest state labels and direct node joins, not numeric flow-row order alone, govern chronology.
4a. **Whisper-guidance and adversarial prophecy test within the named 2.6 flow family.** `8413/1` has an exact quest-node condition for `311000002` and a handbook pointer; its thirteen accepted Augusta turns after one single Rover prompt disclose intermittent battle guidance, noisy return after assuming office and her plan to test apparent prophetic proof. `8415/1` is a later-numbered state in the same named flow-list but has no retained exact quest-node/handbook join. It separates the Chinese-table-named speaker “Whisper” (350005, six items) from Augusta (250022, eleven), who questions the speaker's contradictory incentives and asks about Angel. Neither the name nor the text proves Angel's state or the voice's full mechanism. The nearby `8416/1/3` Augusta retort is accepted **source-unvoiced**; do not attach a heard delivery from the 24 preceding selected voice turns. `8879/4` is later-labeled 2.7 dialogue with living Augusta, not a record of fatal fulfillment of her “blood” image. The fourteen-plus-seventeen TalkItem actions have no stored divergent TalkSequence paths; 8413's single Rover option has empty actions. These source-state distinctions are detailed in the [whisper study](WUWA_AUGUSTA_WHISPER_GUIDANCE_PROPHETIC_TEST_AND_ANGEL_IDENTITY_PROFILE.md).
5. **Iuno memory disturbance is not stable relationship state.** At `7741/5`, Augusta struggles to recall Iuno while Rover insists Iuno exists; she explicitly considers Dark Tide deception and looks for traces. This belongs to a memory/perception-conflict state, not proof that she never knew her. Keep the prior friendship and later recovery/uncertainty separated, and inspect branch reachability before joining all reactions.
6. **After victory / broader world / future self.** `FavorStory_130605_Content` asks who she might be when Septimont no longer needs its Hero of Heroes and ends with an optional friend encounter in the empty arena. `FavorWord_130631_Content` offers more possibilities, including a quiet town, weaponsmithing or age-silvered sparring; none is a decided retirement plan. At `flow#/11364/2`, a later quiet arena/walk conversation can disclose her old denied access to training and permit sentimentality, but it is **source-unvoiced** in the selected audio mapping. `9931/4` shows later trade/political work and gratitude for Qiuyuan's frontline aid, not abandonment of Septimont.

## Graph, genre and source limits

The five favor stories are authored prose with shifts between perspective, reported rumor, Augusta's interpretation and direct speech. Magno's death and childhood whisper origin must be held at their actual evidentiary level; Augusta's `8402/4/29–30` Angel testimony is more specific than the archive's unresolved *later* fate, while `7741/5` is a separately contested memory state. The selected flow rows preserve choices and sequence transitions in `RAW_RELEVANT_FLOW_STATES.jsonl` and `SCENE_AND_EVIDENCE_LEDGER.jsonl`. Several reflective or ordinary-life lines—including `11364/2`—are source-unvoiced and cannot be described as heard performances. One bankable route to retrieval is `AUDIO_MATCHED_SEMANTIC_CASES.json`, which joins 18 selected exact text/occurrence keys to 72 render records. No human listening or runtime video review has been done for this draft. The visual profile's three official-client UI rasters have separate previously active provisional authority and do not prove runtime gesture or model construction.
