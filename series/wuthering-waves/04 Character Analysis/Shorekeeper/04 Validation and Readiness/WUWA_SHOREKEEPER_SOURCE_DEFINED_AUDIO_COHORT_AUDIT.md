---
series: WUWA
character: Shorekeeper
artifact_type: source_defined_audio_cohort_audit
scope: SHOREKEEPER_PINNED_3_6_0_TEXT_AUDIO_PRE_AV
analysis_generation: SHOREKEEPER_PRE_AV_V0_1
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

# Shorekeeper — nine source-defined audio cohorts, pre-listening

The source script marks a change in Shorekeeper's ability to name desires and act on them, but it does not follow that aggregate F0 or loudness will map neatly to “machine,” “person,” “lover,” or “free.” This audit selects exact story actions that could test such a claim later, joins them to already measured four-dub PCM, and records what the machine evidence can currently say. It contains no audio and no human listening result. The [deep dive](../01%20Evidence%20and%20Source-Facing/WUWA_SHOREKEEPER_CHARACTER_DEEP_DIVE_PRE_AV.md) and [self-exclusion specialist](../01%20Evidence%20and%20Source-Facing/WUWA_SHOREKEEPER_SELF_EXCLUSION_SOUL_AND_SHARED_WORLD_PROFILE.md) carry the interpretive argument; the [speech profile](../03%20Audiovisual%20and%20Voice/WUWA_SHOREKEEPER_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md) records the wider measurement method.

## Pinned selection, identity and reproduction

These nine actions contain 208 accepted Shorekeeper semantic voice occurrences, 38.3% of the packet's 543 selected voice lines. Each has exactly one selected render per ZH/EN/JA/KO occurrence–language cell: **832 render associations and 832 distinct native-PCM objects**, all passing stored FLAC-hash and native-PCM-payload integrity checks and all measured. This no-reuse result applies only to the selected cohorts; the whole corpus has 2,172 associations, 2,052 runtime rows, 2,048 distinct measured objects and four repeated PCM manifest rows. An action set is not a complete graph traversal, nor is a machine-measured line a line heard by a human analyst.

| Cohort | Exact pinned action | Lines | Why this state is material |
|---|---|---:|---|
| Core post | `flow#/3446/3` | 19 | Body/projection account, core duty and her claim then that she cannot leave her post. |
| Garden change | `flow#/3756/2` | 31 | Names a change in the garden part of herself and tests feeling vocabulary. |
| Tethys confession | `flow#/3804/3` | 17 | Explains the system's emotional fuel and admits deceiving Rover. |
| History and desire | `flow#/3824/1` | 23 | History, loss, uncertainty and a first-person wish to know. |
| Reunion apology | `flow#/4020/4` | 31 | Welcomes Rover, apologizes for acting without consultation and asks for future stories. |
| Deep-shore cost | `flow#/4198/2` | 31 | A shared no-more-harm promise, her proposed sole core cost and a question about love coexist. |
| Postrepair | `flow#/4081/3` | 18 | Continued work after repair alongside shared sun/sea language. |
| Later Lahai-Roi aid | `flow#/15733/2` | 17 | Support to Rover and the Black Shores' larger mission in a later crisis. |
| Tunnel decision | `flow#/10100/2` | 21 | Coordinates and a one-way route; later cooperation is not a permanent departure from duties. |

The private metadata-only artifact is `_research/character_packets/Shorekeeper/audio_work/SHOREKEEPER_SOURCE_COHORT_AUDIT.json`, SHA-256 `8ffdfc8197f0fd1cc176a9780273e6e4c29fc5e003e9e357c61a0ce113c57303`. Its input hashes bind the pinned voice-line table and measurement table; each member carries semantic occurrence, source locator, text key, render analysis ID, language, PCM/FLAC hashes and QC flags. Recreate it from the extraction root with `scripts/audit_character_audio_cohorts.py Shorekeeper`, one `--cohort` for each exact table action (drop `flow#/`), and `--output` to the private path. A rerun was byte-identical. An absent action `999999/999` and an overlapping `4198/2,4198/2@24` selection both failed nonzero before writing their negative-test outputs. Exact source selection matters because a nearby line or friendly filename cannot establish ownership, route or playback.

## Scene-level signal result—and why it is not an emotional arc

The −45 dBFS gate's median *paired* EN-minus-ZH active-frame levels vary sharply by source action. In core post, garden change, history/desire, reunion and tunnel decision they are −0.10, +0.04, +0.24, −0.80 and −0.49 dB respectively. Tethys confession is +4.28 dB (EN higher in 16/17 exact semantic pairs), deep-shore cost +3.73 dB (higher in all 31), and postrepair +4.10 dB (higher in 17/18). Later Lahai-Roi aid is +1.61 dB (14/17 higher). This is not a monotonic chronology: a later tunnel action returns near zero. The data show action-dependent localized signal levels under the selected gate; they do **not** identify whether the cause is performance, recording, in-engine gain, media mastering, text length/phonemes or mix. Without within-language level normalization, phrase alignment and listening, a claim that a new “person” or “lover” voice emerged would be overfit to these numbers.

Qualified F0 coverage is ZH 196/208, EN 204/208, JA 202/208 and KO 199/208 selected objects under the stored mono/voiced-frame/parameter gates. Cohort qualified-F0 medians in ZH range from 216.2 Hz in history/desire to 264.7 Hz in later Lahai-Roi aid; EN ranges from 190.8 in deep-shore cost to 228.7 in later aid. Some lines are very short or carry edge/parameter flags. Nothing in these medians labels an actor's tenderness, “robotic” quality or grief. The −50-to−40 dBFS threshold changes median active duration by 0.72–0.98 s across the four dubs in the core-post cohort and by 0.16–0.38 s in deep-shore cost. The detected inactive frames are not phrase-aligned intentional pauses; the different text and scene production are substantial confounds.

The source itself supplies the important state distinctions independently of waveform shape. At `flow#/3446/3/2` she says the Tethys core position prevents departure *then*. At `4198/2/24` the Chinese wording invokes a shared promise against further harm; item 26 proposes that **she alone** bear a price; item 30 asks whether what she feels is love. These are separate exact semantic and render IDs within one action. One must not merge the promise into a proven self-protection outcome or make the question a mutually agreed relationship. At `flow#/3804/3/11`, English adds a best-for-both rationale to her admission of deception that Chinese does not equally state. At `4020/4/2`, apology for unilateral action does not mean her earlier whole life was unconstrained; at `4081/3/12`, Chinese emphasizes continuing the old work while English emphasizes having to stay to watch over Black Shores. The later aid actions show continuing participation, not an unlimited ability to leave or a return to old core confinement. No sound-level pattern adjudicates these textual differences.

## Revision gate

Preserve the source-grounded progression from assigned instrument to self-naming participant, but **downgrade** any proposed single acoustic switch that supposedly proves personhood, freedom or reciprocal romance. The next useful review is line-timestamped listening within each dub for `3446/3/2`, `3804/3/11`, `4020/4/2`, `4198/2/24–30`, `4081/3/12` and the later support actions, with checks for voice/background separation, dialogue route, gain processing and phrase match. The full 543-line selected audio corpus remains outside this purposive 208-line audit and has not received a human-performed analysis. A later observed delivery should revise its exact line/state claim, not silently upgrade every neighboring scene or the entire character model.
