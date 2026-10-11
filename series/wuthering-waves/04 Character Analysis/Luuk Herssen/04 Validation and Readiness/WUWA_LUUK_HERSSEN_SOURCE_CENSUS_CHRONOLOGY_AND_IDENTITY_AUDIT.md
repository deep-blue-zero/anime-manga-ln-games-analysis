---
series: WUWA
character: Luuk Herssen
artifact_type: source_census_chronology_identity_audit
scope: LUUK_HERSSEN_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: LUUK_HERSSEN_PRE_AV_V0_1
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

# Luuk Herssen — selected-source census, time and identity

This is a census of the **selected pinned generation**, not a declaration of all dialogue in every official game build. `ANALYSIS/Characters/Luuk Herssen` holds the private source package, graph and occurrence crosswalk. Collection validity proves the retained selection's internal integrity; it does not prove there are no unmarked appearances outside the selected scope. Official-client Wwise/PCM is raw sound evidence and does not independently settle Arikatsu-normalized speaker identity or chronology.

| Denominator or witness | Pinned count | What it does not mean |
|---|---:|---|
| Relevant full flow states | 179 | Not 179 linear scenes; states can branch, loop or contain non-Luuk speakers. |
| Context text keys | 2,429 | Not 2,429 lines spoken by Luuk. |
| Quest references / distinct IDs | 68 / 21 | Not a complete client quest catalog. |
| Direct attribution candidates | 834 | Not all accepted. |
| Accepted solo / unresolved / rejected | 830 / 4 / 0 | Not 830 voiced or necessarily 830 narratively substantial utterances. |
| Accepted source-voiced / source-unvoiced | 642 / 188 | Unvoiced text cannot be described as heard. |
| Favor stories / archive voice entries | 5 / 77 | Archive entries and story-flow occurrences are different classes. |
| Selected semantic voice lines | 719 | Not the total of every possible event, branch or language render. |
| Four-dub render associations | 2,889 | Associations may include duplicates or alternatives. |
| Runtime object rows / unique measured FLAC | 2,863 / 2,855 | Eight repeated PCM rows; object counts are not semantic-line counts. |
| Unique FLAC bytes / measurement failures | 790,876,108 / 0 | Local integrity and signal measurement, not human performance interpretation. |
| Phone-message pointers | 11 | All have metadata-only extraction status; linked flow states can still contain readable body text. |

The selected semantic-line arithmetic is `642 accepted source-voiced direct occurrences + 77 favor/archive entries = 719`; the 188 accepted source-unvoiced occurrences are not missing audio by virtue of being unvoiced. The render associations by language are EN 730, JA 721, KO 719 and ZH 719, so the 2,889 associations are not simply `719 × 4`: some languages have additional variant associations. The twenty matched case artifacts are a deliberately small **audit sample** of 80 renders, not a replacement for the 719-line selected corpus. Within that sample, 40/80 render records retain null explicit Wwise event and numeric-media IDs; exact external-source media and WEM/PCM/FLAC joins must not be relabeled as complete event→bank proofs. `AUDIO_MEASUREMENT_SUMMARY.json` records native FLAC and PCM hashes, durations, channel selection, flags and analyzer provenance. No human listening or video review has been performed for this draft.

## Identity boundary

Playable role **1510** is Luuk Herssen / 陆·赫斯. Technical speaker 150065 is the named character, 150103 a communications presentation, 750343 a message presentation and 750540 a past-self presentation. These are render/narrative labels for the same lore person where the exact occurrence supports it, not four personalities. `flow#/10719/5/1–2` displays a generic doctor/speaker 178, but the same uninterrupted appointment immediately names him in `/3`; acceptance is limited to the two exact locators. The four narrator rows `flow#/15064/5/14–17` remain unresolved despite adjacent Luuk material. Do not attribute the “pawn,” staged story or pact exposition to him by adjacency. `IDENTITY_DISCOVERY.json` is a nomination aid, not the accepted registry; the current decisions are `occurrence_adjudication.json` and `occurrence_identity_crosswalk.jsonl`.

No rejected candidates appear in this selected audit; that is not proof all unsearched generic speakers are Luuk. Accepted row `flow#/15474/1/0` has an empty English text witness and should not become a substantive quotation or performed line without source inspection. Five or more message-style companion states are represented both as `WAVESLINE_MESSAGES.jsonl` pointers and in their linked flow dialogue. Do not count a pointer and its body as two independent speech events.

## Temporal and medium partition

1. **Childhood and experimental household:** `FavorStory_151001_Content` and later recollections establish father/Rhein/Golden Serum before Novialle inheritance. The archive is narration across time, not necessarily a directly performed present scene.
2. **Corporate inheritance, investigation and undercover pursuit:** `FavorStory_151002–151004_Content` and the recalled segments in `flow#/12322/2` place the lab audit, Fractsidus disguises and rain-grave witness before the long Academy period. The exact date of the Architect's substitution as father is not identified by Luuk's childhood observation.
3. **Academy introduction and frostland expedition:** `flow#/10719/5`, `10674/2`, `10816/7`, `10824/2` stage the doctor, student care, scientist-guide and privacy-aware confidant. Flow row order is indexing, not automatically diegetic order.
4. **Renewed Fractsidus/Architect disclosure:** `flow#/12313/3–12335/3` includes consultation, past-self insert, dossier, false-injury test and aftercare. Mark the recalled or dramatized past-self utterances as such; do not make Rover equally knowledgeable at every earlier scene.
5. **Companion/ordinary-life episode:** `flow#/15460/1–15475/5`, plus `15914/1`, follows message invitations, waffles, missing-food investigation, a direct stand-beside request at `15470/4`, cat-placement planning and the later free-return pattern. The `15470/4` three-answer menu and the `15475/5` two-answer menu are different branch points; responses are alternatives, not cumulative lines.
6. **Ecology and later contact:** `flow#/15640/4`, `15641/4`, `16997/1` and `17007/2` show ambient reflection and graduation correspondence. The contemplated Huanglong trip remains a prospect in the witnessed text.
7. **Exostrider permission and Black Shores contact:** `flow#/15731/3` and `15733/2` are two separate linear TalkSequences within quest `121000040`, joined by QuestNodeData `#/20332` and `#/20335` and PlotHandBook `#/77`. Each has a two-caption Rover option menu with empty actions and no transition fork: candy response at `15731/3/0`, exhaustion response at `15733/2/12`. The selected captions are unknown. Luuk's seventeen and twelve voiced turns, respectively, remain his own; Rover's risk case and Shorekeeper's communications briefing are adjacent other-speaker evidence. A meeting is not authorization and the later outcome is not in these two actions.

Within partition 4, `flow#/12327/3` deserves a separate source boundary. Its 42-item `ShowTalk` has a consecutive 1–42 `TalkSequence` and no option list, with twenty-one speaker-`150065` Luuk turns, Lucilla's speaker `150057` and N.A.N.A.'s `750539`. QuestNodeData `#/19167` and PlotHandBook `#/71` join its state `剧情_3_1_拉海洛主线_下半_21_1` to quest `189000000`. Lucilla's trust and declined candy are her judgments, not lines to assign to Luuk. N.A.N.A.'s report of Nivora's abduction is received information; Luuk's repair/security direction, perimeter request and private hypothesis are decisions, not completed outcomes. The selected 21 semantic voice rows have 87 distinct PCM-valid render associations because three EN slots have a second variant, not because there are 24 Luuk lines. No per-render explicit event/media ID or human listening is supplied for this action. The [dedicated study](../01%20Evidence%20and%20Source-Facing/WUWA_LUUK_HERSSEN_LUCILLA_ACADEMY_TRUST_STUDENT_HOPE_AND_NIVORA_PURSUIT_PROFILE.md) keeps these joins and status differences visible [LUK-E37–E38/C36–C37].

The later `15731/3` and `15733/2` actions each have a single linear TalkSequence and one two-caption option menu without an action jump; their 29 Luuk source-voiced semantic lines have 116 distinct four-language PCM-valid render joins inside the existing 719-line selected corpus. Explicit event/bank/numeric-media IDs are null for these story renders. `15731/3` has four Rover TalkItems among its 21 items plus the two unselected candy captions; `15733/2` includes Rover and communications Shorekeeper `750019` among forty items plus two unselected exhaustion captions. The EN Rover “lowest casualty count” at `Zuoyequnxing_52_7` is more specific than ZH/JA/KO loss/damage wording and cannot become a Luuk quotation. All four witnesses mark Chase's possible continuing Ashridge affiliation as uncertain. Rover's physical assessment was submitted, but this source does not show all permission steps; the private Black Shores room is a bounded local context, not proof all later communications are safe [LUK-E39–E40/C38–C39].

The `15470/4` companion action is a separate graph class: its 34 `ShowTalk` items have no flat `TalkSequence` or `SequenceTransitions`, but `_10_25` holds three explicit `JumpTalk` option actions to distinct Luuk replies followed by a common rejoin. QuestNodeData `#/19182`, key `165800021_4`, reaches the state through `/FinishActions/0/Params`; this is an authored pointer, not proof of a played route. The 23 accepted/source-voiced Luuk items have 92 four-language PCM-valid renders in the authored union, 21 Luuk turns per traversal, all with null explicit event/bank/numeric-media IDs. Rover's `Side_LHSCP_10_14` asks him to stand beside rather than observe; Luuk's `Side_LHSCP_10_17` interprets the earlier Academy invitation, `_10_22` calls Rover a friend and attempts rest, and `_10_32–34` condition a later invitation on cat placement. The later intermittent-return cat state does not resolve whether that exact earlier condition occurred [LUK-E41/C40].

## Multilingual adjudication notes

The normalized Chinese witness is the semantic anchor, but no English sentence should be silently treated as a perfect translation. In `FavorStory_151004_Content`, Chinese says **the great majority** of other Ichor recipients ended like Rhein (`其他绝大部分`); English says “Without exception, the others...” The packet therefore uses *most* or *many* and does not claim every other subject's fate is known. This is a material scope downgrade from the English wording, not grounds to discard the entire localization. The grave visitor's pronouns branch by Rover selection in English/Japanese; Chinese uses `{TA}`. No gendered Rover is imposed as the one canonical route. The companion story's spoof “System Notification” at `flow#/15462/1` is part of Luuk's joke, while `WAVESLINE_MESSAGES.jsonl` is metadata for the message state. Both distinctions matter for scene and voice analysis.

In the `12327/3` Academy conversation, ZH/EN/KO describe faction-placed staff while JA calls the eight-of-ten group spies more directly; the number is Luuk's conversational figure rather than a staffing audit. EN's “gilded cage” is a stronger image for student management than ZH/JA/KO's closed/sealed language. All four witnesses support the different proposition that Luuk thinks students understand the compromises and still hold ideals. On the emergency side, JA's Luuk describes something to check and moving more easily alone, while ZH/EN/KO more explicitly frame solo verification of a conjecture. These distinctions qualify the model's Academy-criticism and investigative-certainty claims, not the fact that he asks for a perimeter [LUK-E37–E38/C36–C37].

The ordinary scenes add two more exact controls. At `flow#/15461/5/5`, the waffle response option jumps to alternative approving and critical Luuk routes; collecting both resolved lines does not make them one performed exchange. At `flow#/15914/1/10`, a message-text warning says sugary/oily waffle pieces may lure the cat but must not be eaten. No selected voice case exists for that exact message key, so no adjacent recording should be assigned to it. In the birthday archive `FavorWord_151018_Content`, Japanese calls Luuk one of Rover's close companions, an explicit nonexclusive scope that an English singular address cannot override. The source's ongoing Fractsidus vow (`FavorWord_151010_Content`) also coexists with his archive claim that he has moved past old days (`151006`); a chronological or psychological resolution is not supplied by the census alone [LUK-E25–E28, C23–C26].

At `15470/4`, ZH/EN/JA/KO preserve the contrast between standing beside Rover and merely observing, while JA's Rover line contains text gender variants without changing the three later option routes. Luuk's across-language friend/advice wording is explicit, but the claim about Rover's two purposes for inviting him to the Academy is Luuk's interpretation. The three `Side_LHSCP_10_26–28` captions and corresponding `_10_29–31` replies should be aligned as alternative branches, and `_10_32–34` is a shared conditional future, not three separate invitations [LUK-E41/C40].

The 77 favor-word rows also contain **22 raw-ID/actual-Content-key mismatches** at `favorword#/3190–3211`. All 22 exact locators match semantic archive voice rows, explicit event paths/IDs, four resolved text witnesses and 88 distinct PCM-valid four-dub objects. This is not 22 missing lines or 88 new objects beyond the 2,855 counted above. In particular, raw `151059` is Hit I with `FavorWord_151078_Content`; deriving `_151059_Content` would fetch the preceding Intro Skill III. The [row-level specialist](../01%20Evidence%20and%20Source-Facing/WUWA_LUUK_HERSSEN_COMBAT_SURGICAL_LANGUAGE_AND_ARCHIVE_KEY_PROFILE.md) distinguishes combat trigger, patient conduct and localization. Event/media integrity does not show which trigger fired in runtime or constitute human listening [LUK-E35–E36; C34–C35].

## Completeness and uncertainty discipline

The machine audit's `valid: true` and `voice_completeness_valid: true` apply to the selected package. They do not prove runtime reachability of every branch, human-heard audio identity, absence of additional client story data, full restitution after Novialle's closure, Rhein's later fate, or permanent Ichor safety. The pending work is exact branch traversal for key Rover choices, full-text JA/KO adjudication on delicate clinical/romantic claims, performance listening and runtime visual staging, then owner review before any current-authority routing change.
