---
series: WUWA
character: Zani
artifact_type: source_defined_audio_cohort_audit
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

# Zani — eight source-defined sound cohorts and two unvoiced controls

Zani's texts offer a tempting vocal shorthand: professional service at the bank, night vigilante severity, then a gentler ability to rest. The machine signal must be tested against exact source actions, speaker decisions, render variants and *which scenes actually have selected voice*. This audit uses the [speech profile](../03%20Audiovisual%20and%20Voice/WUWA_ZANI_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md)'s existing local PCM measurements. It contains metadata only—no recordings, no human listening and no claim about observed delivery. The [deep dive](../01%20Evidence%20and%20Source-Facing/WUWA_ZANI_CHARACTER_DEEP_DIVE_PRE_AV.md) and [efficiency/force specialist](../01%20Evidence%20and%20Source-Facing/WUWA_ZANI_EFFICIENCY_TRAP_SWORD_SHIELD_AND_PROTECTIVE_FORCE_PROFILE.md) carry the literary reading.

## Selection and proof limits

Eight deliberately disjoint source-action selectors yield **142 selected semantic lines** (15.6% of the frozen 912-line selected voice corpus), **571 render associations and 571 distinct canonical-PCM objects** across ZH/EN/JA/KO. All objects are measured and integrity-valid under the stored FLAC/native-PCM checks. The full selected corpus has 3,653 render associations and 3,517 distinct measured FLAC objects; these are different denominators, and this eight-cohort subset is not an exhaustive voiced or literary census. Some source actions contain optional branches, so a set of all accepted lines is not a single executed playthrough.

| Cohort | Exact selector | Semantic lines / render associations | Interpretive test |
|---|---|---:|---|
| Front desk | `flow#/4204/2` | 28 / 115 | Formal bank welcome, staff commands and an offered meal share one action but not one audience or register. |
| Guest sweets | `flow#/7297/7@0–4` | 5 / 20 | She buys varied sweets because she does not know Rover's taste. |
| Minor offenders | `flow#/7297/7@14–27` | 14 / 56 | Investigation and pragmatic restraint toward small offenders occur in the same action as hospitality. |
| Nightwalker disclosure | `flow#/7298/7` | 28 / 112 | Identity admission, nickname discomfort, operational planning and late snack are branch-sensitive, not one fixed confession monologue. |
| Earlier routine error | `flow#/7301/4@0–16` | 17 / 68 | Fragile everyday routines and an earlier too-fast solitary intervention. |
| Safer city | `flow#/7301/4@20–39` | 20 / 80 | Civic stability, less need for a Nightwalker and thanks to Rover; dialogue alternatives remain alternatives. |
| Talos confrontation | `flow#/7556/3@11–12+14–15+17–24+26` | 13 / 52 | Threatening a major organizer is ethically distinct from the minor-offender inquiry. |
| Actual paid leave | `flow#/12439/7` | 17 / 68 | She really receives leave, tries a party, becomes tired and chooses a quiet interval. |

The `4204/2/0` bank welcome is a special case: its displayed speaker is hidden and the technical speaker ID is 178, but the exact source-identity crosswalk accepts it as Zani *contextually*, because the same attendant immediately introduces herself in item 1. That single semantic occurrence has **seven render associations**: two distinct PCM objects in ZH, EN and JA, one in KO. The other 27 selected bank lines have one per dub. The paired level audit excludes the ambiguous multi-PCM occurrence rather than silently selecting a preferred take; its front-desk EN–ZH comparison is 27 pairs, not 28. The 571 associations have 571 distinct PCM hashes within this selection; that does not imply every character occurrence everywhere has unique media.

Two source-relevant negative controls have **no selected playable voice**: `flow#/8585/5` has ten accepted Zani turns about differentiated prosecution, pardons and resettlement stalls, and `flow#/8586/10` has thirteen accepted turns about sea breeze, bread, night-city familiarity and persistent insomnia. All 23 are marked `play_voice: false` in the pinned occurrence crosswalk and are absent from the selected voice-line analysis. Their text remains important; they cannot be used as evidence of a performed restitution tone or heard nocturnal tenderness. This says nothing definitive about every possible client asset outside this selected generation. The missing-selector test for `8585/5` correctly refused to write an audio cohort.

## Signal results that do not establish a personality switch

Under the stored −45 dBFS active-frame gate, median levels for the *front-desk* group are ZH −22.4, EN −23.6, JA −19.7 and KO −23.7 dBFS. The *Talos confrontation* group is ZH −24.3, EN −23.9, JA −20.3 and KO −25.8 dBFS. In this raw comparison the threat group is **not consistently higher-level** than client service; it is lower in three locales and close in EN. The corresponding qualified-F0 medians move in different directions: ZH 176.9→182.0 Hz and EN 163.6→186.0, but JA 187.1→154.0 and KO 198.2→185.8. Different words, clip lengths, gain chains, scene treatment and the small thirteen-line threat group prevent causal attribution. These medians do not say the threat *sounds* mild; they reject a proposed universal loudness/pitch shortcut for intimidation.

The source-matched split within `7297/7` is also not a clean acoustic rule. Guest sweets has five selected lines, minor-offender investigation fourteen. Their qualified median F0 changes in opposite directions across locales (ZH 208.3→181.7 Hz; EN 185.1→200.8 Hz; JA 170.1→173.8 Hz; KO 199.8→193.5 Hz). This is a small, text-unequal descriptive contrast, not proof of deliberate private-versus-professional acting. The EN-minus-ZH paired active-level median is −2.06 dB in the sweets subset, −1.41 in minor-offender inquiry and +0.59 in Talos confrontation, but cross-dub levels are not within-language normalized and cannot be read as strength of feeling. The action may include route alternatives; selected membership alone does not prove the three modes were all heard in one run.

The literary distinctions survive this acoustic non-result. In `7297/7/17`, ZH/JA/KO explicitly mention torture as difficult to use because opponents could exploit it, while EN says “more extreme methods”; it is not a clean universal ethical ban. `7556/3/20–24` threatens a particular organizer after survivor harm. `7301/4` says earlier isolated speed worsened danger and that a safer city may eventually make the Nightwalker unnecessary. `12439/7` establishes real paid leave but also exhaustion after a few hours of festivity. No aggregate signal can turn those source-specific situations into a single permanent “softening” trajectory or convert the unvoiced `8585/5` and `8586/10` scenes into performed evidence.

## Reproduction, failure paths and revision gate

The private metadata artifact is `_research/character_packets/Zani/audio_work/ZANI_SOURCE_COHORT_AUDIT.json`, SHA-256 `2df1ed9251a80c27d474dd5ff7c538798d8ca745b0361adfcea2f0f0090cd288`. It binds the pinned line-analysis table and measurement table hashes and records every member's semantic occurrence, source locator, text key, render-analysis ID, dub, canonical PCM/FLAC hashes and flags. Recreate it with `scripts/audit_character_audio_cohorts.py Zani`, using the eight exact selectors in the table (`@` accepts `+` and `-`, not the typographic en dash) and `--output` to that private path. A rerun was byte-identical. Intra-cohort overlapping selectors `7301/4,7301/4@20` and the source-unvoiced `8585/5` selector failed nonzero without writing their intended negative outputs. The utility *permits* overlapping selections in **different** named cohorts; the eight reported cohorts were checked separately to have 142 distinct occurrence IDs, 571 distinct render IDs and 571 distinct PCM hashes. The separate permitted-overlap demonstration is private diagnostic data, not part of these eight cohorts.

The next decisive work is line-timestamped four-dub listening with route and gain controls for the front-desk introduction and its three doubled dubs, `7297/7/0–4` versus `/14–27`, `7301/4`'s two phases, `7556/3/20–24`, and `12439/7`'s fatigue/rest sequence. Direct runtime review should determine which optional replies were actually played. Until then, **downgrade** any supposed loudness/F0-defined bank-worker→vigilante→resting-person persona arc, while **preserving** the text-grounded ethical differences and explicit source-unvoiced controls. A future observation should revise its exact line, language and state claim; it should not silently upgrade all 912 selected lines to human-performed analysis.
