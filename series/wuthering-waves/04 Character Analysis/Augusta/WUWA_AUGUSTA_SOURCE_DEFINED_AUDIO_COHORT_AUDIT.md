---
series: WUWA
character: Augusta
artifact_type: source_defined_audio_cohort_audit
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

# Augusta — source-defined four-dub audio cohort audit

This is a bounded machine-audio and source-alignment audit, **not** an account of heard acting. Its cohorts were chosen from Augusta's pinned scene actions before looking at their acoustic summaries. The aim is to test whether a proposed contrast among martial address, political challenge, friendship, memory conflict, testimony and shared victory survives elementary measurement controls. The continuous interpretation remains in the [deep dive](WUWA_AUGUSTA_CHARACTER_DEEP_DIVE_PRE_AV.md); the [speech profile](WUWA_AUGUSTA_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md) states which claims this audit can and cannot change.

## Source selection and denominators

The selected 189 semantic voice occurrences are 31.2% of the packet's 605 selected lines. They are **purposive**, not a random or representative sample. They yield 756 four-language render associations and 756 distinct canonical native-PCM objects, all present in the pre-existing measurement table and all passing its stored FLAC-hash and native-PCM-payload integrity checks. The whole selected corpus has 2,420 render associations but 2,399 distinct measured PCM objects; the difference between associations, runtime rows and unique objects must remain visible. This audit did not decode or redistribute any new media. Official-client audio bytes are a raw-evidence authority; the normalized Arikatsu source and character attribution remain the pinned semantic view, not something a waveform establishes independently.

| Cohort | Exact source action or accepted voiced TalkItems | Semantic lines | Why included |
|---|---|---:|---|
| Arena challenge | `flow#/8363/3` | 37 | First martial address, invitation, patience and contest. |
| Angel testimony | `flow#/8402/4` | 25 | Reported Dark Tide encounter and the bounded observation at items 29–30. |
| Iuno plan | `flow#/8408/3` | 10 | Isolation, objection to Iuno's bodily risk, fate question and departure. |
| Memory doubt | `flow#/7741/5` | 18 | Iuno's disappearance from others' recollection, a proposed physical-trace test and the bracelet's failure to convince Augusta. |
| Prophecy address | `flow#/7804/4` | 23 | Augusta questions passive fate while acknowledging what Priestesses can do. |
| Senate rebuke | `flow#/8797/4@5-11` | 7 | Public response to senators' attempted boundary around Iuno. |
| Friend logistics | `flow#/8797/4@13-17+20-23+26+28-29+33` | 13 | Teasing, planning and concern within the same action. |
| Fate/friend exchange | `flow#/8797/4@37-43+46-47+49-51+54+56+58-59` | 16 | Prophecy, a spoken fate challenge, a *separate* laugh, reassurance and thanks. |
| Shared victory | `flow#/8422/2`, `8424/2` | 40 | Post-battle credit, gratitude and an explicitly plural hero title. |

The three `8797/4` partitions cover its 36 accepted voiced Augusta turns exactly once; they were separated because that action changes addressee and purpose. They are not three independent recording sessions. `7804/4/0` bears technical speaker ID `178`, but the local `occurrence_identity_crosswalk.jsonl` accepts it as contextually resolved Augusta: an unnamed opening address to Iuno continues immediately into her first-person recollection at items 1–2. This audit retains that accepted occurrence while keeping the attribution method visible. It does not use technical speaker ID alone as character identity.

The reproducible local artifact is `_research/character_packets/Augusta/audio_work/AUGUSTA_SOURCE_COHORT_AUDIT.json` (SHA-256 `1c2f608c307a028a5c55a711f595937ab452915923a619708a0037039ea0b3b9`). It records exact semantic occurrence IDs, source locators, text keys, render IDs, PCM and FLAC hashes, per-language flags and source/measurement input hashes. It contains no audio. Recreate it from the extraction root with `scripts/audit_character_audio_cohorts.py Augusta`, the nine `--cohort` assignments in the table (drop `flow#/`), and `--output` to that local path. The auditor rejects absent exact TalkItem indices and overlapping semantic selections before writing a report. A byte-identical rerun was verified; `8797/4@999` and overlapping `8797/4@5-11,8797/4@6` each exited nonzero and wrote no negative-test output.

## What the signal measurements actually say

All 756 objects were measured. The qualified-pitch denominators are ZH 188/189, EN 188/189, JA 187/189 and KO 188/189; qualification requires one channel, at least ten voiced frames and no pitch-sensitive or frequent-edge-band flag. A stored F0 estimate on an excluded item is not a usable cohort datum. The analyzer uses the highest-RMS channel, not a separated voice stem; 16-kHz analysis, 20-ms energy gates at −50/−45/−40 dBFS, and Praat autocorrelation pitch follow the [speech profile](WUWA_AUGUSTA_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md). No within-language loudness normalization, text-duration alignment, blind listening or runtime playback adjudication was performed.

| Cohort | ZH median qualified F0 | EN | JA | KO | JA–ZH paired median active-frame level, −45 dBFS gate |
|---|---:|---:|---:|---:|---:|
| Arena challenge | 210.6 Hz | 174.4 | 211.9 | 210.7 | +2.74 dB (37 pairs) |
| Angel testimony | 191.9 | 172.9 | 206.7 | 191.0 | +2.62 dB (25) |
| Iuno plan | 191.0 | 178.2 | 214.7 | 180.1 | +3.25 dB (10) |
| Memory doubt | 184.1 | 188.7 | 201.6 | 189.2 | +3.01 dB (18) |
| Prophecy address | 197.0 | 194.7 | 206.1 | 205.8 | +4.28 dB (23) |
| Senate rebuke | 221.4 | 206.4 | 228.5 | 208.3 | +0.66 dB (7) |
| Friend logistics | 190.4 | 197.6 | 199.8 | 212.0 | +3.05 dB (13) |
| Fate/friend exchange | 199.5 | 187.6 | 192.4 | 194.0 | +0.84 dB (16) |
| Shared victory | 186.5 | 186.6 | 216.5 | 196.0 | +4.18 dB (40) |

Within `8797/4`, the Senate segment's qualified F0 median exceeds the friend-logistics segment's in ZH (221.4 versus 190.4 Hz), EN (206.4 versus 197.6) and JA (228.5 versus 199.8), but not KO (208.3 versus 212.0). Nor is “the public scene is louder” a four-dub result: its median active-frame energy is **lower** than friend logistics in EN, JA and KO, and slightly **higher** in ZH. Those medians also compare different sentences and unequal groups of seven and thirteen lines. The audit therefore leaves an enacted public/private register contrast for listening; it does not promote a diagnostic acoustic personality rule. The same-action partition is a useful *question generator*, not a controlled actor experiment.

The gate is consequential. Changing the active-frame threshold from −50 to −40 dBFS changes median active duration in the seven Senate objects by 1.42 s ZH, 1.28 s EN, 1.92 s JA and 1.10 s KO. The corresponding friend-logistics changes are 0.62, 0.36, 0.24 and 0.42 s. A claimed pause or speaking-rate difference based on one threshold could therefore be largely a gate choice; no syllable-level timing or intentional pause annotation exists. Paired JA–ZH active levels also vary substantially by scene, from +0.66 dB in Senate rebuke to +4.18 dB in shared victory. These are matched *semantic* occurrences, not identical scripts, microphone chains or loudness-mastering conditions. They establish signal differences, not one dub's stronger conviction.

The item-level negative case is `flow#/8797/4/46–47`. Item 46 is the spoken commitment to sever a disastrous fate; item 47 is a short laugh. They have four separate render objects each. The laugh is pitch-unqualified in JA and KO for fewer than ten voiced frames (the JA object is 0.32 s), so neither its F0 nor a merged “fate challenge” value should be used to assert fearlessness. Likewise `8408/3/19` is a very short “No!” whose ZH object has too few voiced frames; the longer objection at item 20 is a distinct utterance. In the Angel account, items 29–30 have clean measured objects in four languages, but measurements cannot identify what happened *inside* Oak Hollow or whether Angel survived after the witnessed change. In the memory scene, the measured question at `7741/5/12` is source evidence for Augusta seeking an external trace, not acoustic proof that Iuno was illusory.

## Multilingual and model boundary

The source-defined prophecy cohort exposed a small but model-relevant localization fork at `flow#/7804/4/6`: ZH `鬣狗`, JA `ハイエナ` and KO `하이에나` make the untamed animal a **hyena**, whereas EN substitutes **wolf**; all oppose it to a domesticated rabbit. The claim is fate's attempted taming of agency, not an invariant “wolf nature.” A hypothetical Augusta monologue should not elevate the EN animal to a Chinese-source character symbol. This is a textual alignment finding, not an audio finding.

The quiet optional `flow#/11364/2` material and the accepted anonymous `9509/2/7` entrance are source-unvoiced in this selected semantic corpus. Neither is made audible by nearby measured lines. The 189-line cohort does not cover the archive, all actions, all routes or all possible runtime variants. It cannot prove a continuous playthrough, character ownership, actor intention, genuine warmth, civic sincerity or a resolved event→bank chain where IDs are null. Next review should listen to paired same-action items 6–11, 13–23 and 37–59 in each dub with actual timing annotations; separately inspect `7804/4/6`, `8402/4/29–30`, `7741/5/5–12`, and `8424/2/23–24` against the Chinese text and reachable runtime context. Every finding should identify its line, dub, timestamp and possible counterexample before changing the model.
