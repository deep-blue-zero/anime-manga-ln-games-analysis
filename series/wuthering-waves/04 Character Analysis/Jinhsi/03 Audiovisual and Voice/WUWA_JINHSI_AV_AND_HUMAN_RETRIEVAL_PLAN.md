---
series: WUWA
character: Jinhsi
artifact_type: av_and_human_retrieval_plan
scope: JINHSI_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: JINHSI_PRE_AV_V0_1
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

# Jinhsi — AV retrieval and human-review plan

This is a plan, **not an observation log**. No four-dub listening, clip/contact-sheet inspection or runtime branch traversal was performed for this draft. Three official-client UI rasters are already inventoried in `CHARACTER_VISUAL_REFERENCE_MANIFEST.json`, with an individualized visual profile. Raw images/FLAC/WEM remain local or privately shared; this Git packet contains metadata and short analytical paraphrase only.

1. Pin `source_commit`, source key and exact `flow#/row/action/item` or archive locator. For each candidate, record whether the row is narrative, favor address, message, event barks or a player-choice branch. Keep choices as alternatives.
2. Resolve each render by the established semantic occurrence → event/path → media ID → virtual path → WEM SHA → PCM SHA → FLAC SHA chain. Compare bilingual/four-dub text witness hashes and note where subtitle length/segmentation differs. The 18 case JSON is an initial cross-language calibration, not a completeness sample.
3. Listen to each selected object with nearby context and verify the *heard speaker*, phrase match, split/overlap, room/music bleed and emotional contour. Mark `observed`, `ambiguous` or `mismatch` per render, never infer delivery from F0 or waveform alone. Check all flagged long/multichannel samples with more caution. A later full census should include all 539 resolved semantic lines and track four dubs separately.
4. For the eight `flow#/3722/0/1–8` mother/infant narration lines, treat installed media membership as a lead only. Investigate supported runtime event dispatch and bank/media context; until exact event-to-playable-object proof exists, record `runtime_dispatch_unsupported` and exclude their sound from completion percentages and interpretation. Do not fill them with proximity-matched audio.
5. Visually inspect authored scenes at `1191/3`, `2515/3`, `2516/3`, `3153/4`, `3157/2`, `3209/3`, `3223/3`, `3160/5–3163/2`, Moonlit Fair routes, the `7456/2` first-meeting reprise and both later Xuanfang actions `17181/2` and `17636/6`. Capture source time, scene/branch identity, staging, camera, expression and apparent state/form. Keep `1191/3`'s opening choice graph distinct from the recap's linear ordering. The UI art cannot certify runtime silhouette, gestures or costume material. If creating review clips, keep resolution at or below the owner-approved 1080p, include sound only when requested, and retain them restricted.
6. Compare direct viewing/listening against text-bound claims: Is public composure visibly strained? Does Jué confrontation read as grief, resolve, fear or some combination? Are optional fair choices mutually exclusive? Does a text-labelled Jinhsi line actually play as another voice? Preserve disconfirming observations and revise the matrix claim ID, not merely append praise.

Completion of this plan would require a denominator report for lines/renders/scenes examined, independent reviewer notes or explicit human observations, contradiction handling and owner adoption. None is claimed here. Current source pin and draft status remain separate from the existing `active_provisional` visual artifact authority.

## Exact initial sound cohort

The following eighteen keys are the 72 four-dub render rows already materialized as metadata in [AUDIO_MATCHED_SEMANTIC_CASES.json](AUDIO_MATCHED_SEMANTIC_CASES.json). They are *not* a statistical sample of all 547 selected semantic lines. They contrast office, leisure, intimacy, a life-risking disagreement and the first-alliance choice graph. For each, retain the exact source locator and render/PCM/FLAC hashes from JSON, listen against the localized subtitle, and record whether the source phrase actually fills the decoded object. A discrepancy is `ambiguous` or `mismatch`, not a prompt to rename the audio file.

| Text key | Listening question | Relevant claims |
|---|---|---|
| `FavorWord_130401_Content` | Does formal welcome read as administrative distance, genuine hospitality, or both in each dub? | JIN-C03, C18 |
| `FavorWord_130405_Content` | How is shared effort/companionship phrased without assuming an exclusive partnership? | C12, C15 |
| `FavorWord_130408_Content` | What degree of private pleasure accompanies the red-date Loong bun recommendation? | C17, C18 |
| `FavorWord_130410_Content` | Is human self-rule articulated as resolve rather than hostility to Jué? | C09, C18 |
| `FavorWord_130414_Content` | Does Sanhua's meal care elicit surprise, affection or simple description? Listen first. | C14, C17 |
| `FavorWord_130418_Content` | Is the handmade lantern invitation a civic birthday custom, a personal invitation, or both? | C15, C17 |
| `FavorWord_130428_Content` | Compare frequency-closeness wording with delivery; do not infer a canon exclusive bond. | C15, C18 |
| `Huanglong_main_1_5_79_2` (`flow#/1191/3/1`) | What interpersonal weight does keeping the appointment carry after the three-day risk? | C03, C06 |
| `Huanglong_main_1_5_79_80` (`flow#/1191/3/55`) | Does her refusal to await a falling hero sound resolute, defensive or indeterminate? | C09, C12 |
| `Huanglong_main_1_5_79_83` (`flow#/1191/3/58`) | EN says protection should fall on no one else's shoulders; the Chinese anchor stresses personal responsibility without negating delegated help. Compare four witnesses before treating it as a no-delegation rule. | C09, C12 |
| `Chengxiaoshan_main_1_1_360_30` (`flow#/3223/3/24`) | All four text witnesses reject a death-seeking reading. Does performance add strain without cancelling her stated survival aim? | C07, C11 |
| `Chengxiaoshan_main_1_1_380_34` (`flow#/3160/5/30`) | How does she refuse Jué's choice while retaining respect for the parent-like Sentinel? | C07, C09 |
| `Huanglong_main_1_5_79_32` (`flow#/1191/3/24`) | How does the conditional aid request sound before Rover's join/consider choice? | C23 |
| `Huanglong_main_1_5_79_35` (`flow#/1191/3/25`) | Hear the thanks-for-trust reply only on Rover's join route. | C23 |
| `Huanglong_main_1_5_79_36` (`flow#/1191/3/26`) | Hear the respect-for-choice reply only on Rover's consider route. | C23 |
| `Huanglong_main_1_5_79_82` (`flow#/1191/3/57`) | Compare the shared nonbarter norm across dubs after the branch rejoin. | C24 |
| `Huanglong_main_1_5_79_88` (`flow#/1191/3/62`) | Test the postcrisis condition on Rover's freedom to depart. | C24 |
| `Huanglong_main_1_5_79_90` (`flow#/1191/3/64`) | Hear the secrecy request without inventing Rover's answer. | C25 |

The unresolved narrated `flow#/3722/0/1–8` remains outside this *sound* cohort. Its lines are text-known but cannot be treated as missing from a supposedly 547/547 decoded set. Conversely, these eighteen matched cases do not license an assertion that all 539 sound-resolved lines have been perceptually inspected. Any aggregate performance pattern must first give line and language denominators, phrase/room/overlap exclusions, and a review method.

**Next metadata expansion, not yet one of the eighteen cases:** nominate `HuanglongXZ_21_18` (`2948/1/14`) to hear the early public freedom promise, `Huanglong_main_1_7_21_20–21` (`2301/4/11–12`) for pre-Firmament duty and capital aid, and the mutually exclusive defense replies `_29–32` (`2301/4/17–20`). Add `Main_HuangLong_SYYLFML_110_29`, `_31`, `_53`, `_67` (`17181/2/20,31–32,39`) and `Main_HuangLong_XLZHDLY_480_39`, `_47`, `_51` (`17636/6/6,13,17`) to compare the early jurisdiction limit with Yangyang's later requested service. The scene ledger records four media associations for each accepted voiced Jinhsi line in these actions, but their per-render hashes have **not** been copied into the eighteen-case JSON. Retrieval must join the full private voice-line analysis by exact source locator/text key and preserve the route alternative, not infer a sound file from the key alone. These targets test JIN-C29–C33; no listening has occurred.

Further metadata nominations are `Huanglong_main_1_5_82_3–7` at `2515/3` (promise under incomplete knowledge) and `Chengxiaoshan_main_1_1_290_2–3`, `_290_5–8` at `3157/2` (operational shortcut under causal uncertainty). The first action has seven voiced Jinhsi lines/28 distinct localized PCM objects; the second six/24. The memory-handbook `7456/2` has five voiced Jinhsi lines, but its 20 language-labeled rows resolve to only five shared `gl_vo` PCM identities. Do not promote the latter to four-dub performance evidence or treat its recapped hello/projection lines as one original `1191/3` route. Exact render metadata remain in the private complete-voice index, not the eighteen-case JSON [JIN-E39–E41; C38–C40].

## Claim-driven runtime route targets

| Exact scene | Observation to retrieve | Possible revision pressure |
|---|---|---|
| `flow#/1191/3` | Reconstruct join and consider routes separately, then their common nonbarter/departure/secrecy sequence; check appointment timing and what Jinhsi does *not* know of Rover. | C03, C06, C15, C23–C26; do not concatenate optional replies or call deferral an outright refusal. |
| `flow#/2515/3` | Trace Black Bloom report, Black Shores inference, possible surveillance and future Jué-disclosure pledge, with locale certainty differences. | C38; a prospective promise is neither recovered knowledge nor fulfilled disclosure. |
| `flow#/2513/3–2516/3` | Track the Scar allegation, Sanhua's tasking and the exact hidden Changli turns. | C03, C13, C20; prevent cross-speaker leakage. |
| `flow#/3144/4–3153/4` | Verify the limited time-stabilization radius, Xinyi delegation and snow-memory framing. | C10–C12; child memory is not a second present actor. |
| `flow#/3157/2` | Inspect still water, proposed shortcut and chamber sightline before inferring cause or successful entry. | C39; practical movement and unresolved mechanism coexist. |
| `flow#/3209/3–3223/3` | View Jué's injury disclosure, Changli's alarm and Jinhsi's survival-intent reply in sequence. | C07, C11; a painful confrontation is not a suicide wish. |
| `flow#/3160/5–3163/2` | Inspect how Second Awakening/time restoration and self-identification are staged, including any branch. | C07–C10; no miracle outside shown scope. |
| `flow#/3722/0` | Determine whether the birth/revival narration has a runtime event route at all; separately inspect any visual presentation. | C08, C21; WEM membership cannot substitute for decoded playback. |
| `flow#/4130/8–4133/4` | Map Moonlit Fair choices, shared play and possible romantic framing by *actual* route. | C15, C17; retain alternatives and no exclusivity claim. |
| `flow#/17181/2` | Check messengers/attempted scout, emergency-key action, decision to remain and jurisdictional limits. | C12/C32; inquiry is not proof of intervention, and possible personal entry is not actual entry or unrestricted deployment. |
| `flow#/17636/6` | Observe Yangyang's request, Qiuhong's welcome, Jinhsi's assent and prospective Jiyan consultation; do not infer an issued transfer order. | C33; distinguish counterpart agency, local authority and future formal arrangement. |
| `flow#/2948/1` | Inspect the one-sequence citywide invitation, including whether a guest is visually identifiable and how the public request is presented. | C29; no private token/guard disclosure or guest response is established by the broadcast text. |
| `flow#/2301/4` | Traverse the prepared, no-choice and willing-help answer routes separately through their TalkID 21 rejoin; confirm Jinhsi's use of capital aid alongside Jué's information. | C30–C31; no stitched reply, no proved categorical refusal and no claim that independence began only at Firmament. |
| `flow#/7844/1` and `8329/1` | Identify the Echo Cube/Tethys simulation in the first action, determine whether and how the related named-event state plays, and test the actual language-specific `gl_vo_` source object for a small set of text keys. Keep the simulated actor/form and exact container/member path in the capture. | C36–C37; no actual Jinhsi promise or four-dub performance follows from technical speaker 186 and four metadata language labels. Four of these lines have a nonmatching text-key/WEM basename. |
| `flow#/7456/2` versus original `1191/3` | Compare the memory-handbook retelling with the original first-meeting opening-choice topology; verify offered-hand depiction and any runtime language dispatch. | C40; no second meeting, both original openings on one route, completed contact or four independent dubs follows from the recap. |

For each viewed interval, keep client build, source state and branch, capture hash, timecode, resolution (at most the owner-approved 1080p), sound-inclusion state, observed gesture/camera, and a separate inference/counterreading. Existing UI rasters cannot answer those temporal questions. If a new observation changes a central civic or Jué reading, revise the continuous analysis and any dependent model rule as well as the matrix; a video footnote alone is insufficient.
