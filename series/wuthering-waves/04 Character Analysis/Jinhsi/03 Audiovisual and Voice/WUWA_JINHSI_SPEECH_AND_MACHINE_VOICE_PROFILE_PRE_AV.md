---
series: WUWA
character: Jinhsi
artifact_type: speech_and_machine_voice_profile
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

# Jinhsi — written registers and machine audio, pre-listening

No human performance judgment has been made. A measured FLAC hash, duration or F0 is evidence of a particular decoded signal under the recorded analyzer, not evidence that a voice sounds warm, strained, authoritative or romantic. The unresolved eight-line origin narration is excluded from heard-voice conclusions even though its WEM membership is installed. [Matched cases](AUDIO_MATCHED_SEMANTIC_CASES.json) retain four-language source/event/media/hash joins without distributing sound.

| Textual register | Source-bounded cues | Limit |
|---|---|---|
| Civic address | Polite welcome, service invitation, explicit responsibility and public reassurance (`FavorWord_130401`, `130420`; `flow#/1191/3`). | Courtesy is not lack of strategic intent; public address differs from intimate speech. |
| Policy/problem solving | Wishes translated to concrete interventions, legal evidence before sanction, and limits of what she knows (`FavorStory_130402`, `130404`; `flow#/2514/6`). | Long archive prose is narrated, not necessarily her spoken wording. |
| Fractured certainty | Questions Jué, distinguishes theories from fact, asks Rover for trust while retaining decision responsibility (`flow#/3155/1`; `3160/5`; `3223/3`). | Do not stage several branch alternatives as one speech. |
| Personal recollection | Snow, sea nightmare, childhood before title, favorite buns and performance at the theater (`FavorWord_130406–130412`; `flow#/3153/4`). | Introspective archive voice is a different medium from live crisis exchanges. |
| Tender invitation | Handmade lantern, alignment of frequencies, fair choices (`FavorWord_130418`, `130428–130429`; `flow#/4130/8–4133/4`). | Text does not force a canon romance or tell us how any dub acted the invitation. |
| Play and short event responses | Card-game prompts and hesitation (`flow#/14714/5–14716/1`, `15295/1`, `15420/1`). | A one-word “hmm” is poor evidence of stable personality or emotion. |

Seven matched archive lines sharpen this register map without adding a performed-voice conclusion. The official welcome (`FavorWord_130401_Content`) apologizes for office demands; the companionship line (`130405`) moves from everyone to a particular “you”; the market and Sanhua lines (`130408`, `130414`) distinguish pleasure in civic food from receiving a colleague's care; and the Jué-prayer line (`130410`) defends those who seek help while arguing for human agency. The birthday lantern (`130418`) is a time-conditional invitation, not an accepted date. Her proposed frequency closeness (`130428`) is speculative and felt, not a measured reciprocal bond. In these cases, EN makes a recommendation, self-rule or alignment more emphatic than the ZH anchor or JA witness; KO sometimes names Rover where ZH says “you.” Those are locale-specific text choices, not evidence that the actors performed different emotions. The [case-by-case retrieval capsules](WUWA_JINHSI_AV_HUMAN_RETRIEVAL_CROSSWALK.md) identify each exact object and the questions a human four-dub pass should test. In particular, EN `130418` carries a long-object subtitle-extent flag, so a whole-object acoustic statistic must not yet be called the birthday sentence's isolated vocal shape.

## Selected-scope measurements and language-dispatch boundary

The eighteen exact matched cases in this packet do **not** include the flagged `TZZNQ_*`/`Side_TZJNSC_*` event family. The broader 547-line selected corpus does. Thirty-one event-family lines have four language-labeled render rows that all reference the same `gl_vo_` WEM and the same canonical PCM hash per line; four of them use a different source basename from their text key. These decoded signals may be valid audio objects, but they cannot furnish a four-dub acting comparison or a proved text→voice match on label alone. Sixteen voiced lines across `7844/1` and `8329/1` carry 64 associations but only fourteen unique PCM identities. Their written ZH/EN/JA/KO text differences can be analyzed separately, with the explicit Tethys-simulated Jinhsi-image caveat. A controlled per-language runtime/container test is still open [JIN-E37–E38; C36–C37].

The five voiced `Side_TZJNSC_2_*` lines at memory-handbook `7456/2` are part of that 31-line alias set: 20 locale-labeled associations, five shared PCM objects, no proved independent four-dub acting. Two of their WEM basenames recur under later `TZZNQ_7_16–17` text keys, so a friendly key/path association does not authenticate those later utterances. The side action also recaps original first meeting `1191/3` while linearizing Rover's originally exclusive hello/projection openings. The original graph, not side-row order, governs a first-meeting performance reconstruction [JIN-E41; C40].

539 of 547 semantic voice lines have complete selected render resolution; the dataset records 2,209 render associations, 2,042 runtime rows and **2,038 distinct measured FLAC objects**. Four runtime rows repeat PCM; all objects present for measurement passed. The 32 unresolved rows for the eight missing `3722/0/1–8` lines are *not* measurement failures: their runtime dispatch is unsupported, so no corresponding decoded playable object was established.

| Language | Distinct measured objects | Sum duration, s | Median duration, s | Qualified pitch objects | Qualified median F0, Hz | Median active energy, dBFS |
|---|---:|---:|---:|---:|---:|---:|
| EN | 533 | 3,394.58 | 5.21 | 524 | 238.72 | −22.83 |
| JA | 530 | 3,404.48 | 5.11 | 522 | 221.42 | −24.38 |
| KO | 528 | 3,475.46 | 5.51 | 519 | 256.18 | −22.37 |
| ZH | 528 | 3,160.48 | 4.97 | 511 | 223.17 | −22.34 |

These describe different language sets and phrasing, not actor speed, emotional intensity or gender. The analyzer recorded 168 `multichannel_not_isolated_speaker`, 21 `pitch_fewer_than_10_voiced_frames`, six `long_object_check_subtitle_extent`, nine `pitch_parameter_sensitive`, 15 `pitch_edge_band_frequent` and one `full_scale_samples_not_proof_of_audible_clipping` flags; a file can carry more than one. Review flagged objects in context rather than treating machine flags as defects. The instrument is Sigrika `analyze_audio.py` v0.2.0 SHA-256 `73c2904c38d06440a86a572d05fa3fe200e23055e68f0aeaec3be75313d3c4a2`, Python 3.12.4/Windows 11; analysis picks the highest-native-RMS channel and resamples to 16 kHz for derived measures while preserving native hashes.

## Reproduction and failure-path audit

The private measurement source is `_research/character_packets/Jinhsi/audio_work/AUDIO_OBJECT_MEASUREMENTS.jsonl` with the companion `AUDIO_MEASUREMENT_SUMMARY.json`; the reviewed Git packet contains only the selected-case metadata index, not the 2,038 FLACs. The summary records the analyzer hash, version, arguments, input-manifest hash and line-analysis hash. Each object row records FLAC and native PCM hash checks, channel count, analysis channel, gate values, pitch qualification, source/render associations and explicit flags. A `flac_sha256_match` plus `native_pcm_payload_match` shows byte/decoder integrity for that object; it is not an independent re-decode of its WEM or a human assessment. Twenty-seven identical measured objects are members of all four language collections, adding 81 language memberships: the per-language table counts are therefore **not disjoint objects** and must not be summed as independent takes. The summary's zero `failed_objects` applies to the 2,038 objects admitted to measurement. It must not be read as “547/547 voiced lines resolved,” since the eight `flow#/3722/0/1–8` lines lack proven runtime dispatch. Their 32 render rows are **unsupported dispatch**, not failed measurements.

The analysis chooses the native channel with the highest RMS; it does not isolate a vocal stem, average surround channels, infer spatial placement or make four actors comparable. The 168 multichannel flags are 42 objects in each language. Energy-active frames use 20 ms windows and three gates; the displayed active-energy median is threshold-dependent. The local object table gives these whole-object sensitivity checks (median per language, rounded):

| Dub | Median silent fraction at −50 / −40 dBFS | Median change in active duration from −50 to −40 |
|---|---:|---:|
| ZH | 0.375 / 0.435 | 0.26 s |
| EN | 0.271 / 0.342 | 0.32 s |
| JA | 0.333 / 0.396 | 0.28 s |
| KO | 0.338 / 0.382 | 0.20 s |

Those differences are large enough that a claim such as “she pauses more in dub X” cannot be derived from one arbitrary silence gate, especially when object lengths, localization and channel layouts differ. The pitch estimator is Praat autocorrelation at 10 ms, nominal 75–650 Hz with a 100–750 Hz sensitivity rerun; only qualified voiced frames contribute to the displayed F0. Twenty-one objects have fewer than ten voiced frames, nine are parameter-sensitive, and fifteen hit an edge band often. Those flags are not a diagnosis of actor technique. The single full-scale-sample flag likewise is not proof of audible clipping. The six long-object checks require subtitle/voice extent review before treating one object's duration as one isolated speech turn.

## Source-defined contrast that remains a negative result

Two exact four-dub cases appear tempting as an “accepts death” versus “chooses life” acoustic contrast: `Chengxiaoshan_main_1_1_360_30` at `flow#/3223/3/24` states she is not seeking death; `Chengxiaoshan_main_1_1_380_34` at `flow#/3160/5/30` refuses Jué's proposed freezing choice. The first lasts 10.83 s in ZH and 11.85 s in EN; the second lasts 3.42 s and 5.25 s respectively. The qualified median F0 changes from 211.7 to 216.4 Hz in ZH, 236.6 to 254.4 in EN, 216.1 to 221.7 in JA, and 239.5 to 322.8 in KO. These are not matched utterances of equal text or scene acoustics. The four dubs do not give one clean, language-invariant pitch shift that would license a generalized “more resolute” or “more frightened” performance claim. Nor does duration tell us whether Jué's immediately preceding warning is heard with trepidation. The safe present result is **no promotion** from script-based survival/choice claims to actor-delivery claims. A future matched-phrase, channel-reviewed and human-listened cohort could revise that, but should report the full line context and each locale separately.

The eighteen selected sound cases are a calibration/retrieval sample, not a random or exhaustive analysis of the 539 technically resolved semantic lines. They overrepresent claim-critical archive intimacy and major decisions. They cannot establish the proportion of Jinhsi's complete performed corpus that is tender, formal or strained. Source prose, quest dialogue, short event responses and player-branch alternatives are different surfaces. A model of her voice should currently use the written-register table above with explicit source and state limits; it should not synthesize a performed mannerism from aggregate F0, energy or a single dubbed example.

## Source-action cohorts and a scene-specific level shift

The whole-corpus table above mixes archive and story, different sound contexts and repeated runtime variants. A second, private metadata-only audit therefore selected exact pinned `flowstate.json` actions *by narrative question*, joined each accepted Jinhsi semantic occurrence to its four-language render IDs and canonical PCM hashes, and deduplicated each language's objects. It read the existing measurements; it did not re-decode media, listen, or assign feelings. All selected distinct objects passed both FLAC-hash and native-PCM integrity tests. These cohorts are purposive diagnostic groups, not representative samples of Jinhsi's entire speech distribution.

| Source question; exact actions | Semantic occurrences / render associations | Distinct measured objects, ZH / EN / JA / KO | Median −45 dBFS active-frame energy, ZH / EN / JA / KO |
|---|---:|---|---|
| First Rover alliance, including join/consider fork; `1191/3` | 61 / 248 | 61 / 62 / 61 / 61 | −22.2 / −21.4 / −22.7 / −21.5 dBFS |
| Jué's absence, uncertainty and counsel; `2514/6`, `2516/3` | 54 / 228 | 54 / 56 / 56 / 54 | −21.9 / −22.3 / −22.2 / −21.3 dBFS |
| Mt. Firmament choice arc; `3144/4`, `3153/4`, `3155/1`, `3160/5`, `3161/3`, `3163/2`, `3209/3`, `3223/3` | 114 / 488 | 114 / 114 / 114 / 114 | −22.3 / −22.6 / −29.0 / −22.7 dBFS |
| Later Xuanfang jurisdiction action; `17181/2` | 18 / 72 | 18 / 18 / 18 / 18 | −22.0 / −22.9 / −21.9 / −23.9 dBFS |

The excess associations are not automatically extra *lines*. In `1191/3`, `Huanglong_main_1_5_79_53` has eight render associations rather than four, yielding one additional **distinct EN PCM** but no additional distinct object in ZH, JA or KO. In `2516/3`, `Huanglong_main_1_5_83_8`, `_9` and `_15` each have eight associations; three distinct EN and two distinct JA alternatives affect the object counts. The Firmament arc also has eight occurrences at `3209/3` with doubled associations, but they resolve to the same PCM within each language. A matched-line comparison must not silently choose among distinct render variants. The private audit excludes such occurrences from that comparison while retaining all variants in the object-set summaries; it reports exact occurrence IDs, text keys, locators, render IDs, PCM/FLAC hashes and exclusions.

The Japanese Firmament energy difference is robust *within this selected signal set*, but its meaning is narrower than a performance adjective. For 114 line-matched occurrences with one distinct PCM per language, the median Japanese-minus-Chinese active-energy difference is **−6.8 dB**, and Japanese is lower on **108/114** pairs. The corresponding EN-minus-ZH and KO-minus-ZH medians are −0.4 and −0.5 dB. Outside this selected Firmament arc, the measured JA object-set median is −23.4 dBFS, rather than the arc's −29.0 dBFS. A three-action subset focused on snow memory, Jué confrontation and self-description (`3153/4`, `3223/3`, `3163/2`) has 50/50 Japanese objects lower than their ZH line matches, with a median paired difference of −7.6 dB. Conversely, in the first-alliance cohort the paired JA-minus-ZH median is only −0.6 dB across 61 eligible lines; in the later Xuanfang action it is +0.3 dB across 18. These comparisons identify a **scene/locale-associated level shift to investigate**, not why it occurred. Recording, mastering, gain and mix are live alternatives to any acted-character explanation. Equal PCM-hash integrity and mono layout do not eliminate them; no listening or client playback-level measurement has been performed.

The contrast also shows why the global JA median active energy (−24.38 dBFS) must not be presented as a stable dub-wide personality trait. The first-alliance cohort and Firmament arc differ in source context, and all four languages may have different wording, phonetics and production. F0 medians in the three-action Firmament subset are ZH/EN/JA/KO `214.1/226.6/207.5/235.5` Hz, versus `209.0/223.5/217.8/246.4` Hz in the first-alliance group, with pitch-qualified denominators `49/50/50/50` and `58/61/61/60` respectively. That is no clean, four-dub invariant “resolute voice” signature. The action-level private report further separates the ten-line snow memory, 31-line confrontation and nine-line self-description, so their differing texts are not hidden in one average.

Reproduction: `scripts/audit_character_audio_cohorts.py` refuses a changed pinned line-source hash, duplicate PCM measurement or missing action/object. Its private `JINHSI_SOURCE_DEFINED_AUDIO_COHORTS.json`, `JINHSI_ACTION_LEVEL_AUDIO_COHORTS.json` and `JINHSI_FIRMAMENT_ARC_AUDIO_COHORT.json` contain the complete member and threshold tables. The pinned complete-line SHA-256 is `d3813c417de2f5c43af32a68b87ef0d6d5b7dc5a9824cda86165aef84d695af5`; the measured-object table SHA-256 is `93b44e60c591dd1f20ab951f5d025d20335e4d01297b11b144a0fa6bb3d2c082`; the waveform analyzer SHA-256 is `73c2904c38d06440a86a572d05fa3fe200e23055e68f0aeaec3be75313d3c4a2`. No raw audio or full private object table enters this Git draft. The eight text-known origin-narration lines at `3722/0/1–8` remain outside these decoded-audio cohorts and **runtime-dispatch unresolved**, not implicitly audible because other Firmament material is measured.

Listening priority: compare the four dubs for public welcome, join versus consider replies, her shared nonbarter and postcrisis-departure promises, the unanswered secrecy request, the wish-policy conflict, wage confrontation, uncertainty around Jué, the explicit “not planning on dying” line, a birthday/fair invitation, and the comic short event response. Record exact object/render ID, language, matched text key, phrase time range, background bleed and human confidence. Resolve the eight missing origin narration lines by runtime path before they enter any listening census. Full 539-line human pass is a future task, not implied by eighteen calibration cases.
