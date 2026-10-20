---
series: WUWA
character: Luuk Herssen
artifact_type: audio_qc_and_comparability_audit
analytical_responsibility: "Separate verified decoded-object coverage, estimator selection effects, and future human performance claims"
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

# Luuk Herssen — audio quality, comparability and observation gate

This audit covers the **measured object plane**, not a performed-voice verdict. The [speech profile](../03%20Audiovisual%20and%20Voice/WUWA_LUUK_HERSSEN_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md) owns the textual registers and summary statistics; the [claim-driven crosswalk](../03%20Audiovisual%20and%20Voice/WUWA_LUUK_HERSSEN_AV_HUMAN_RETRIEVAL_CROSSWALK.md) names exact sound and scene targets. Private evidence is `_research/character_packets/Luuk Herssen/audio_work/AUDIO_MEASUREMENT_SUMMARY.json` and `AUDIO_OBJECT_MEASUREMENTS.jsonl`, joined by FLAC SHA-256 to the [twenty-case metadata sample](../03%20Audiovisual%20and%20Voice/AUDIO_MATCHED_SEMANTIC_CASES.json). The private corpus is pinned to Arikatsu commit `353f2eaed119bc9f680eab92807d20ac75a79b40`; normalized source text and official-client-derived media are distinct authorities.

## Denominators and what actually passed

The collection has **719 selected semantic voice lines** and **2,889 language/render associations**. They point to 2,863 runtime rows and 2,855 distinct measured FLAC objects; eight runtime rows repeat a PCM object. All 2,855 local objects passed the current acquisition, FLAC-byte and native interleaved s16le PCM-payload checks, with zero decode/measurement failures. This is not a statement that every chosen subtitle spans exactly one sound, that every source WEM was independently re-decoded here, or that all four dubs depict identical performances. The local analyzer records `source_wem_redecoded: false`; the WEM/hash mapping is inherited from the earlier extraction plane and retained as provenance, not retested by this pass.

For analysis only, the analyzer chooses the highest native-RMS channel, resamples it to 16 kHz, and estimates energy, pitch and related signal properties. It does not isolate a speaker. Sixty-seven objects carry `multichannel_not_isolated_speaker`; do not use their signal summaries as single-actor baselines. The 20-case crosswalk contains 80 exact render rows; **40/80 have both explicit `event_id` and `numeric_media_id` null**. Exact external-source WEM and decoded FLAC/PCM identity still exist for these rows, but the missing event/media IDs cannot be filled from a friendly filename or bank assumption. This gap is especially visible in the fully selected two-route waffle exchange at `flow#/15461/5/6–11`.

## The language-dependent estimator problem

The same pitch settings do not produce equally usable cohorts in each dub. A “qualified” object here means the analyzer's conservative F0 gate accepted it; it is not a quality rating for the actor, recording or dub. The object counts and overlapping flags, recomputed from the private object JSONL, are:

| Dub | Measured | Qualified F0 | Qualified share | Frequent pitch edge-band | Parameter-sensitive | Multichannel | Long-caption check |
|---|---:|---:|---:|---:|---:|---:|---:|
| EN | 722 | 694 | 96.1% | 21 | 0 | 19 | 4 |
| JA | 712 | 580 | 81.5% | 129 | 2 | 16 | 9 |
| KO | 711 | 184 | 25.9% | 524 | 5 | 16 | 5 |
| ZH | 710 | 151 | 21.3% | 553 | 21 | 16 | 5 |

The primary Praat autocorrelation pass uses a 75–650 Hz range and a 10 ms time step; the sensitivity pass uses 100–750 Hz. The edge-band flag marks objects with frequent selected values below 90 or above 600 Hz; parameter sensitivity tests matched voiced frames under the two ranges. The table's flags overlap. KO and ZH have 524/711 and 553/710 edge-band objects respectively, so their “qualified median F0” samples select a small, nonrepresentative remainder compared with EN. It would be unsound to read EN 115.24 Hz, JA 147.61 Hz, KO 116.77 Hz and ZH 133.86 Hz as a four-actor emotional, vocal-maturity or authenticity ranking. The selection process itself differs materially by language. The cause of this skew—performance range, mix, pitch-tracking behavior, or other factors—has **not** been adjudicated by listening or an independent tracker.

The [exact-action cohort audit](WUWA_LUUK_HERSSEN_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md) confirms that this is not merely a full-corpus averaging problem. The clinic subset qualifies 1/12 ZH and 0/12 KO renders, and the after-shock-care subset qualifies none of six in either dub. The selected eleven cohorts include 127 distinct lines and 512 exact render/PCM joins; their action-level active levels also fail to establish a universal physician→opponent→domestic acoustic progression. Four semantic-language slots have a second PCM variant and are excluded where a one-object-per-dub paired statistic would otherwise silently choose a take. These checks deepen the signal gate, not human performance knowledge.

Object duration is also not an articulation-rate comparison. The JA median is 6.81 s, versus EN 5.81, KO 6.20 and ZH 5.66 s, but text length, phrasing, leading/trailing sound and mix may differ. Written-unit proxies use unlike units across scripts, with no word-to-audio forced alignment. Likewise median energy around -23 to -25 dBFS is a measurement of these files and gates, not a claim that one actor is calmer or more forceful. Twenty-three long objects require checking whether one subtitle covers the whole recording; two ZH objects have exact full-scale samples, a clipping investigation cue rather than proof of audible damage. None of these flags is a missing line.

## Paired review that could change the model

An exact four-dub listen should use the case ID, source text key and object hash together, not whichever nearby sound seems narratively apt. Start with two graph-sensitive controls: `Side_LHSCP_2_9`–`2_11` are the approving route, and `2_12`–`2_14` the critical route. The raw flow option at `flow#/15461/5/5` jumps to TalkId 7 or 10, and each three-line route jumps to TalkId 13 after its final line. A reviewer may compare both possible performances while recording that they are **alternative traversals**, not a six-line conversation. The EN `Side_LHSCP_2_11` “official taste tester” phrasing is more role-like than the zh-Hans/JA/KO invitation; any cross-dub intimacy judgment must first account for that textual shift.

Next use `MAIN_RGLC_36_39` (support after loss) and `FavorWord_151010_Content` (long anti-Fractsidus wish) as a *textual tension*, not a predetermined “vengeful tone” classification. The ZH object for the former is both pitch-edge and parameter-sensitive, so its automated F0 must not decide the acting contrast. `FavorWord_151001_Content` (gold-color/bodily constraint) and `FavorWord_151018_Content` (birthday companionship) are longer archive objects in several languages; check caption extent and any nonverbal tail before coding pauses or promises. Japanese birthday wording explicitly places Luuk among Rover's close companions; a warm delivery cannot turn that into an exclusive pact.

For each observed sound, log language, semantic occurrence ID, selected render ID, WEM/FLAC/PCM hashes, proven event/media IDs or nulls, channel count, start/end timecodes, audible speaker(s), subtitle extent, performed delivery *as heard*, and a contrary reading. Keep machine signal estimates, human perceptual notes, and relationship/psychological inference in separate fields. A second independent listener or adjudication pass would be warranted before promoting especially consequential performance claims. An eighty-render sample can calibrate this procedure but cannot substitute for complete voice-line analysis of all 719 selected semantic lines.

## Current disposition

**PRESERVE** decoded-object coverage and exact hashes. **STRENGTHEN** branch and medium controls in the selected review. **DOWNGRADE** cross-language F0 comparisons to diagnostic-only because the qualification shares diverge sharply. **OPEN** human performance interpretation, source-WEM re-decode parity in this pass, subtitle extent for flagged long objects, and runtime video/choice observation. No claim about Luuk's voice acting or physical performance is promoted by this audit alone.
