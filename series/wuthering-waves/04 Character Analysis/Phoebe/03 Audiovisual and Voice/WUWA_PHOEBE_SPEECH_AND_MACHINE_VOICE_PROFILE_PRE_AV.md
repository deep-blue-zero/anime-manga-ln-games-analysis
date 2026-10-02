---
series: WUWA
character: Phoebe
artifact_type: speech_and_machine_voice_profile
analytical_responsibility: "Textual registers, four-language source/render joins, signal observations, and listening limits"
scope: PHOEBE_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: PHOEBE_PRE_AV_V0_1
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

# Phoebe — textual speech and machine-measured four-dub voice

This is a pre-listening profile. The voice corpus proves matched semantic occurrences, localized text witnesses, client source-media routes, and decoded PCM/FLAC objects; explicit Wwise event/bank/media IDs are available for some, not all, selected renders. The [retrieval crosswalk](WUWA_PHOEBE_AV_HUMAN_RETRIEVAL_CROSSWALK.md) records 28/48 selected render rows with null event and numeric-media IDs. The corpus does **not** establish the actor's emotional delivery, breath intention, accent, timbral image, or scene-specific audio mix. The twelve selected chains in [AUDIO_MATCHED_SEMANTIC_CASES.json](AUDIO_MATCHED_SEMANTIC_CASES.json) retain exact source locator, text hashes, event and numeric-media fields including nulls, source virtual path, WEM hash, FLAC hash, PCM hash, render variant, language, signal values, and QC flags without committing audio.

## Speech functions, not a single “sweet voice”

| Register | Source instances | Textual behavior and limit |
|---|---|---|
| Ritual/public acolyte | `FavorWord_150621–624_Content`, `4237/3`, `11917/1/5` | Uses a blessing, institutional name, or procedural instruction. Even a warm phrase may have an official audience. Combat barks are short and emphatic, not evidence that all private talk is terse. |
| Competent intervention | `FavorStory_150601_Content`, `4587/4/22`, `4807/5/21–24` | Names danger, offers testimony or treatment, and often specifies what she can do. The restaurant action proves force can accompany courteous speech. |
| Suppressed enthusiasm | `4237/3/8–11`, `4800/6/6–7`, `FavorWord_150603_Content` | She becomes animated about an Echo or wants to embrace friends, then checks herself under a role rule. This is a textual pattern; exact cadence and laugh belong to a future listening pass. |
| Anxious self-correction | `4601/2/3`, `4799/4/15–18`, `4805/4`, `FavorWord_150607_Content` | Begins with surprise, pauses or retracts, tries to steady herself, and separates a question from the conclusion it might imply. A scene should not turn every hesitation into helplessness. |
| Apology with limited authority | `4807/5/15–21`, `5606/3/11–12` | Acknowledges an intrusion or injury and promises bounded help; she does not claim complete empathy or speak for the entire Order. |
| Adapted blessing | `5567/3/33`, `FavorWord_150616–617_Content`, `11983/1/8` | Can address a nonbeliever or Rover as an agent of their own fate while continuing to wish them safety. The English and Chinese religious terms are localization choices and must be compared in context. |
| Ordinary guide/friend | `FavorWord_150608–609_Content`, `4798–4800`, `4808/5` | Food, photography, architecture, travel logistics, and checking another person's rest interrupt formal piety. She can be a prepared guide and an amused companion. |

For generated dialogue, select a development state and listener first. Early public Phoebe is more likely to announce Order duties and suppress Echo affection; later she may explain a principled disagreement without abandoning familiar devotional language. In panic, she can call herself to breathe and still act. Her kindness is often actionable: reporting a disturbance, gathering a camera, stopping a risky method, offering a check, or coordinating help. Avoid copied canonical sentences and refrain from using a single phrase as a universal verbal tic.

The Cetus apology at `5606/3/11–12` should not be cut away from Abby's mediated reply at T15–19 and Phoebe's short T20 acknowledgment (`DYHD_29_32–36`). The text permits a receiving as well as a giving side to her social role, but it does not supply a recurrent vocal marker. JA/KO wording differences and the unreviewed four-dub delivery block a universal performed “voice of absolution” claim; the [Cetus reply profile](../01%20Evidence%20and%20Source-Facing/WUWA_PHOEBE_CETUS_REPLY_RECEIVING_AND_SELFHOOD_PROFILE.md) gives the exact semantic boundary.

## Full selected signal pass

The local source view has 476 semantic lines: 416 source-voiced story occurrences and 60 archive lines. All 476 have rendered coverage. There are 1,906 render associations but 1,818 distinct PCM/FLAC objects; four repeated PCM manifest rows were recognized rather than double-counted. All 1,818 distinct objects passed local integrity/measurement. This is selected corpus completion, not complete game-wide speech or human performance annotation.

| Dub | Distinct measured objects | Median object duration | Qualified median F0 | Median active-frame energy |
|---|---:|---:|---:|---:|
| Chinese | 472 | 4.94 s | 325.2 Hz (451 qualified) | −22.91 dBFS |
| English | 473 | 4.97 s | 303.6 Hz (449 qualified) | −23.31 dBFS |
| Japanese | 473 | 5.64 s | 325.4 Hz (461 qualified) | −22.22 dBFS |
| Korean | 472 | 5.17 s | 320.6 Hz (456 qualified) | −24.04 dBFS |

These are object-set aggregates under the pinned waveform analyzer, not matched-line actor rankings. Different wording, syllable rate, acted intentions, leading/trailing silence, loudness mastering, and object variants confound cross-language comparisons. F0 is reported only for segments satisfying the analyzer's gates; pitch failures and QC flags remain per object. A higher median in one language would not imply Phoebe is “more excited” there. The full private object table is `_research/character_packets/Phoebe/audio_work/AUDIO_OBJECT_MEASUREMENTS.jsonl`; the method is `scripts/analyze_character_audio.py` invoking the hash-pinned Sigrika analyzer. Media itself remains local/private.

## Source-defined scene-cohort audit

To test whether the whole-corpus median conceals materially different *source contexts*, a second, metadata-only pass selected eight exact `flowstate.json` actions before inspecting their acoustic values. It joined every selected semantic occurrence to its language-specific render ID and canonical PCM hash, then deduplicated PCM objects **within each language and cohort**. It did not re-decode media or label emotion. All 86 selected source occurrences have four render associations (344 total), and every selected distinct object is measured and passes both the FLAC-hash and native-PCM-payload integrity checks. These 86 are a purposive cross-section of the 416 source-voiced story occurrences, not a random or exhaustive estimate of Phoebe's story-scene distribution. Archive lines and nonlexical efforts are excluded from this scene comparison.

| Source-defined context; exact actions | Semantic lines | Median qualified F0, ZH / EN / JA / KO | Median object duration, ZH / EN / JA / KO |
|---|---:|---|---|
| Early Echo encounter and public city guide; `4237/3`, `4238/3` | 32 | 280.8 / 271.3 / 289.9 / 266.3 Hz | 8.76 / 8.07 / 9.70 / 9.39 s |
| Lorelei source inquiry and Fenrico doubt; `4587/4`, `4601/2` | 15 | 312.6 / 276.5 / 308.6 / 292.5 Hz | 9.67 / 9.19 / 10.40 / 7.75 s |
| Cetus search and archive procedure; `5559/4`, `5565/3` | 27 | 342.5 / 345.3 / 353.5 / 342.2 Hz | 4.69 / 4.37 / 6.51 / 5.30 s |
| Adapted farewell and personal apology; `5567/3`, `5606/3` | 12 | 371.8 / 350.5 / 388.1 / 371.2 Hz | 5.09 / 4.61 / 3.70 / 3.44 s |

Each composite has the same number of **unique PCM objects per dub** as semantic lines: 32, 15, 27 and 12, respectively. Pitch-qualified denominators are ZH/EN/JA/KO `32/31/32/32`, `15/15/15/15`, `25/26/27/27`, and `11/11/12/11`. Qualification requires mono, at least ten voiced frames and no pitch-parameter-sensitive or frequent-edge-band flag; duration and energy use all measured objects. The private `PHOEBE_SOURCE_DEFINED_AUDIO_COHORTS.json` records every member's occurrence ID, exact locator/text key, render ID, PCM and FLAC hashes, QC flags, and all threshold summaries. Its companion `PHOEBE_ACTION_LEVEL_AUDIO_COHORTS.json` splits the eight actions, so the composite results can be challenged rather than treated as a developmental trajectory.

The action split materially changes the reading of the composites. Within the *early* composite, the first-Echo action `4237/3` has 12 lines and median F0 `281.7/296.2/327.8/273.6` Hz (ZH/EN/JA/KO), while the 20-line city-legend action `4238/3` has `280.4/266.5/282.0/262.4` Hz. The *Lorelei* composite likewise combines an eight-line source inquiry (`336.6/300.6/324.1/295.5` Hz) with seven longer Fenrico-doubt lines (`286.6/265.2/308.6/292.5` Hz). The late composite mixes five farewell lines and seven apology lines; their median durations differ by language and the text lengths are not controlled. Thus the apparent rising F0 across four composites is a fact about these selected object sets, **not** evidence that Phoebe becomes progressively more excited, intimate, devout, or emotionally healed. Scene selection, utterance length, phonetic content, acting direction, recording and localization remain alternative explanations. Nor should cross-dub F0 be read as an actor ranking.

One threshold sensitivity check is available without inventing an audible observation. At the −45 dBFS gate, the median fraction of low-energy frames in the early composite is `0.236/0.239/0.310/0.282` (ZH/EN/JA/KO); in the farewell/apology composite it is `0.509/0.344/0.378/0.367`. The corresponding ZH median changes from `0.470` at −50 dBFS to `0.529` at −40 dBFS in the late composite. Those fractions include pauses and source/mastering conditions; they do **not** measure perceived hesitation or tenderness. The late ZH effect is notably unlike the other three dubs and needs line-matched listening and waveform context before any performed-character claim. Every selected object is mono, but mono alone does not prove a clean voice stem.

Reproduction boundary: `scripts/audit_character_audio_cohorts.py` reads the pinned complete-line JSONL, the existing measured-object JSONL and its summary; it refuses a changed line-source hash, a duplicate PCM measurement or a missing selected action/object. The complete-line SHA-256 is `44fa96f4081404975f2d65c64bf820dc12bcf08cbfe9bafae5335a75770fa4cf`, the measurement-table SHA-256 is `a98142724297161fa22cb22bde959d0c5195ba2fef6268816f113daaf74a5d29`, and the waveform analyzer SHA-256 is `73c2904c38d06440a86a572d05fa3fe200e23055e68f0aeaec3be75313d3c4a2`. The script and full cohort tables stay in the private working plane; this Git draft retains the selection rule, aggregate numbers, exact action addresses and limits. No one listened to these files or reviewed synchronized runtime footage for this pass. The narrow within-dub screen below improves the *machine-audio* profile; broader normalized feature/outlier and human-adjudication depth remain open relative to Sigrika.

## Within-dub outlier check: clip mechanics before character psychology

A further read-only screen of that hash-pinned measurement table compares **unique PCM objects within each dub**, restricted to objects with exactly one language label and exactly one `story_dialogue` text-rate proxy. This leaves 387 EN, 387 JA, 386 KO and 386 ZH objects. It excludes 24 shared four-label PCM objects that cannot certify independent dubs, four mixed archive/story-class objects, eight story objects with non-unique rate-proxy links, and the separate 236-object archive class. For each retained dub, compute the median and median absolute deviation (MAD) of a feature; the diagnostic robust score is `0.6745 × (value − median) / MAD`. This is an outlier *nomination*, not an emotion or acting classifier. F0 additionally requires at least ten voiced frames and no pitch-edge or pitch-parameter-sensitivity flag.

| Story-only within-dub baseline | EN | JA | KO | ZH |
|---|---:|---:|---:|---:|
| Duration median / MAD, seconds | 5.520 / 2.699 | 6.063 / 2.922 | 5.536 / 2.750 | 5.235 / 2.564 |
| −45 dBFS active-frame energy median / MAD, dBFS | −23.129 / 0.866 | −21.957 / 1.069 | −23.822 / 0.943 | −22.810 / 0.723 |
| Qualified F0 median / MAD, Hz; count | 297.827 / 31.082; 373 | 322.552 / 37.926; 381 | 314.594 / 34.342; 378 | 321.891 / 33.197; 375 |

The low-energy candidate `Main_Linaxita_2_1_8_7` at `flow#/4237/3/6` is a one-syllable “Ah…”-type cue in all four written witnesses. Its active-frame medians are −31.41 / −36.20 / −31.64 / −33.15 dBFS (EN/JA/KO/ZH), far below each dub's story-object median. The adjacent `Main_Linaxita_2_1_8_4` at `/4237/3/3` is a similarly short “Hmm?” cue; EN has only 0.14 seconds above the −45 dBFS gate and fails the ten-voiced-frame pitch qualification. The `POI_JINKU_81_1` sigh at `/5751/1/0` is another low-energy, one-unit cue; its EN and JA pitch measurements fail the same gate. Such points can dominate a robust outlier list or make a characters-per-active-second proxy absurdly unstable without demonstrating unusually timid, reverent or excited *conversation*. They should be listened to with clip boundaries and nearby dialogue, not used to define Phoebe's disposition.

The opposite duration extreme is also text-conditioned. The later personal blessing `Main_Rinascita_2_12_7501_9` at `/11983/1/8` lasts 19.88 / 17.35 / 16.77 / 19.53 seconds (EN/JA/KO/ZH); its written content is much longer than an interjection. These object durations alone do not prove slower speaking or greater sincerity at the later state. The [retrieval crosswalk](WUWA_PHOEBE_AV_HUMAN_RETRIEVAL_CROSSWALK.md) now nominates the short-cue pair and sigh separately from its existing blessing test. This screen strengthens the negative control on the composite-cohort F0/energy pattern; human four-dub listening, text-length control and runtime context remain open.

## Matched retrieval targets and semantic caution

The twelve source-selected four-language cases include archive conflict (`FavorWord_150603_Content`), expressed doubt (`150607`), food/social self-restraint (`150608`), altruistic ideals and difficulty naming her own wish (`150610`), respect for Zani (`150616`), the Echo distance rule (`Main_Linaxita_2_1_8_12`), bias about Fisalia (`Main_Linaxita_2_2_16_23`), institutional testimony (`Main_Linaxita_2_2_22_22`), Lorelei/Fenrico uncertainty (`Main_Linaxita_2_2_49_20`), an adapted farewell (`DYHD_14_41`), a personal apology (`DYHD_29_30`), and the later blessing in her own name (`Main_Rinascita_2_12_7501_9`). Each has four exact render records. The choices span early archive self-description, public investigation, ethical adaptation and later coda; they are not a random sample and should not be used to estimate her overall rate of any emotion.

Several pivotal holiday exchanges at `4802–4808`, and parts of late reform at `9970`, `11374–11375`, are source-unvoiced in the selected mapping. Specifically, all 26 accepted Phoebe turns at `4798/3` and all 23 at `4807/5` have `play_voice: false`; their four-language wording and gesture narration support literary analysis, not actor-delivery claims. Neither action belongs in the twelve matched sound cases, and a neighboring object must not be substituted. Action barks and effort sounds should be excluded from general conversation-style estimates or stratified separately.

## Archive combat triggers and key identity

All 60 Phoebe archive records have explicit events and four decoded, PCM-valid language renders: 60 semantic occurrences and 240 distinct objects. The 30 combat/system entries at `favorword#/1927–1956` supply 30/120 of those archive totals. They are **not** part of the eight source-defined story-action cohorts above, whose 86/344 denominator is a purposive subset of the 416 voiced story occurrences. Six Resonance Skill raw IDs at `#/1929–1934` have permuted `Content` keys; resolving a bark by a generated `FavorWord_<raw Id>_Content` string may return a valid *wrong* skill. The nonlexical Phoebe greeting at `#/2235` uses `FavorWord_160719_Content`, a text key also used by a Cantarella Idle I record at `#/1976`. Their role IDs, raw locators, event paths, semantic occurrence IDs and four PCM hashes differ. This shared key does not imply a shared actor or sound. See the [exact archive crosswalk and source-class reading](../01%20Evidence%20and%20Source-Facing/WUWA_PHOEBE_ARCHIVE_SKILL_KEY_SHARED_TEXT_AND_COMBAT_FAITH_PROFILE.md).

Combat lines are useful for a **bounded** textual register: imperative direction, devotional vocabulary, rescue language and damage/fall responses under game triggers. They are weak evidence for behavior in a dated civilian scene. At Skill III, ZH/JA/KO refer to wind/direction while EN says “To the Sentinel”; at Injured III, EN says pain is penitence while the other witnesses connect suffering with rescue; at Fallen III, EN adds a first-person farewell where the other witnesses wish light upon someone else. This calls for exact four-dub listening and trigger verification, not a universal self-punishment or canonical-death reading. No such human listening is reported here.

## Multilingual alignment questions for listening

Chinese is the semantic anchor; EN/JA/KO are official localized performances with their own text and timing. A future review should compare source meaning before comparing acoustic shape. High-priority hinges are: the degree of obligation in the Echo distance rule; whether each dub distinguishes doubt of self from doubt of faith; the humility of her holiday apology and refusal to claim total understanding; “in my own name” versus Order-wide authority at Cetus and the final blessing; and the pronouns/titles for Sentinel, Imperator, and acolyte. Use source text-key and occurrence ID rather than a friendly filename. If one dub changes an implication, record it as a localization divergence, not a correction to Chinese by default. A deliberately small adjudication sheet can link the matched render IDs to human notes after listening; no such notes are claimed here.

One difference is already established at the **text** level. `FavorWord_150609_Content` (semantic occurrence `voice-occurrence:b24d3ec5cf5768dee6bedcda3285e09c0b5d1ccec4bbce769daad37c7cd8a208`, `favorword#/1906`) ends with a sour-fruit reaction in zh-Hans, ja and ko, while the English text stops after her sharing maxim. The complete selected voice manifest has four mapped render objects for that occurrence, but none was perceptually listened to in this build. The omission therefore supports a localization-text claim, not a finding about how the English actor ends the take. The [ordinary-life specialist](../01%20Evidence%20and%20Source-Facing/WUWA_PHOEBE_ORDINARY_JOY_GIFTS_AND_SELF_WISH_PROFILE.md) explains why the small undercut matters to characterization; the [retrieval crosswalk](WUWA_PHOEBE_AV_HUMAN_RETRIEVAL_CROSSWALK.md) keeps the future listening question open.

## Known uncertainty

No ear-level labels for warmth, trembling, pace, prayer tone, singing, laughter, or crying have been made. Channel layout is mono in this selected Phoebe collection, but mono does not prove a dry isolated actor stem. The `4599/1/0` hostile reaction remains unresolved and is not a Phoebe audio target. Source-unvoiced dialogue has no mapped performed counterpart in this selection. The retained media hashes let a later analyst review the precise take and contest this textual profile without recreating attribution by filename.
