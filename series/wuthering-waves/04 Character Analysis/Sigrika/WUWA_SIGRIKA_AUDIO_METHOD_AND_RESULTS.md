---
series: WUWA
character: Sigrika
artifact_type: audio_method_and_results
analytical_responsibility: "Own the reproducible native-waveform method, corpus quality, quantitative results, normalization, and evidence-stage completion gate."
scope: SIGRIKA_COMMIT_PINNED_3_6_0_PRE_AV
analysis_generation: SIGRIKA_PRE_AV_V0_2
revises_local_generation: SIGRIKA_PRE_AV_V0_1
audio_revision: native_waveform_pass_completed
video_stage: deferred_owner_requested_local_1080p_or_larger
status: active_provisional
release_state: current_provisional_pre_video
analysis_authority_state: owner_adopted_current_provisional
source_commit: 353f2eaed119bc9f680eab92807d20ac75a79b40
source_generation: arikatsu-3.6.0-353f2eae-expanded-v0.3.0-ko
text_authority: zh-Hans
localization_witnesses: [en, ja, ko]
source_freeze_metadata: conflicting_collection_and_embedded_lock_fields
intended_canonical_home: "series/wuthering-waves/04 Character Analysis/Sigrika/"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_current_git_authority: false
authority_adoption: owner_2026_09_23_text_audio_baseline
created: 2026-09-11
---

# Sigrika — native audio method and results, V0.2

This is the technical home for the **completed machine-audio pass**, not a human voice-performance review. The interpretive speech profile owns what these results can and cannot change in the character reconstruction. The [revision ledger](WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md) owns explicit claim dispositions. The [README](WUWA_SIGRIKA_ANALYSIS_PACKET_README.md) remains the packet’s single entrypoint.

## 1. What was acquired and verified

All **19** archives named by the character audio crosswalk were fetched from the canonical Drive audio-object shard folder. Their SHA-256 values match the retained release manifest. The crosswalk’s **2,809 unique FLAC objects** were extracted by exact member path, without treating a friendly filename as identity. Each full FLAC digest and each native signed-16-bit, little-endian, interleaved PCM payload digest matched its expected value. There were **zero acquisition, decode, or native-payload validation failures**. The [acquisition manifest](AUDIO_ACQUISITION_MANIFEST.json) gives observed Drive IDs, exact archive names, bytes, and hashes. [SIG-AF-01](WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md#sig-af-01)

| Scope | Semantic lines | Render associations | Unique objects | Native FLAC bytes | Sum of object durations |
|---|---:|---:|---:|---:|---:|
| Direct Sigrika | 666 | 2,668 | 2,652 | 618,972,763 | 14,851.212 s |
| Dark Side counterpart | 38 | 169 | 157 | 46,929,188 | 911.503 s |
| Both, without merging their identities | 704 | 2,837 | 2,809 | 665,901,951 | 15,762.714 s |

Summed object time is approximately four hours and eight minutes for the direct set, across all four languages. It is not four hours of independent story, a chronological timeline, or a listening log. The 827 direct story/message occurrences still include 234 source-unvoiced occurrences. The audio stage does not convert those into missing files.

The original WEM containers were **not** fetched or re-decoded. The canonical framed PCM identifier was used as the source identity key; its framing algorithm was not independently reimplemented. Verification of native payload SHA and FLAC SHA is a distinct, actually executed check. This also does not establish official-client semantic parity or settle the existing source-freeze metadata discrepancy. [SIG-E54](WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md#sig-e54)

## 2. Signal path and channel discipline

Every acquired object is native 48 kHz, PCM-16 FLAC. The direct set contains **2,648 mono and four stereo** recordings. The counterpart contains **121 mono, four stereo, and 32 three-channel** recordings. All native ordered samples are retained in the extracted objects. For analysis only, the highest-native-RMS channel is selected and its zero-based index recorded; no channels are averaged or assigned inferred spatial labels. Per-channel levels and correlations are retained for multichannel material.

That selection is a reproducible track choice, not speaker separation. A mono file may still contain breaths, effects, music, or more than the captioned words. In particular, the counterpart’s three-channel recordings are not silently converted into a clean Sigrika vocal stem. Multichannel recordings are excluded from the principal pitch and normalization cohorts, though their channel-local measurements remain available. Counterpart objects never enter direct-character baselines. [SIG-AF-09](WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md#sig-af-09)

The selected track is resampled to 16 kHz with `scipy.signal.resample_poly`, using the exact greatest-common-divisor ratio and the library’s default Kaiser window, beta 5.0. Whole-object integrity, frame counts, duration, RMS, and peak use native samples, not the resampled track. All derived times are **object-relative seconds**. None is a game clock, video timestamp, subtitle-word timestamp, or retiming correction.

## 3. Measurement definitions

### Energy and timing

Native non-overlapping 20 ms RMS windows use the actual length of the final partial window. Three absolute gates, **-50, -45, and -40 dBFS**, classify energy-active versus lower-energy windows. The central tables use -45 dBFS. Recorded outputs include active/low-energy duration, leading and trailing low-energy duration, internal low-energy gaps of at least 100 ms, gap count and density, window-energy distributions, and a twelve-bin object-relative energy contour.

“Low-energy” is deliberately not synonymous with silent, unvoiced, hesitant, or emotionally restrained. Quiet consonants and breaths may fall below a gate; background effects may exceed it. A contiguous internal gap is a signal interval, not a linguistic pause annotation. Leading/trailing gaps are kept out of internal-gap totals.

**Active-frame level** means the median of RMS-derived dBFS values among active windows. It is not the RMS of all active samples pooled together. It can therefore be lower than the whole-object RMS when high-energy peaks dominate the latter. The JSON field is `active_frame_median_dbfs`; this name prevents conflating different energy statistics.

### Pitch and harmonicity

Pitch uses Praat autocorrelation via Parselmouth: 10 ms step, 75–650 Hz range, 15 candidates, voicing threshold .45, silence threshold .03, octave cost .01, octave-jump cost .35, voiced/unvoiced cost .14, and `very_accurate=false`. A second pass changes the range to **100–750 Hz**. Results retain voiced-frame fraction, estimated voiced-frame duration, F0 quantiles and variability, P10–P90 range in semitones, candidate strength, large adjacent jumps, twelve-bin contours, a global slope, and first/last-third contrast.

The two configurations are compared at nearest frame times within 5 ms. A recording is flagged as parameter-sensitive when more than 20% of matched voiced frames differ by over three semitones. Additional flags identify fewer than ten voiced frames or more than 10% of voiced frames near the primary estimator’s edge bands, below 90 or above 600 Hz. These tests do not prove estimator accuracy; they expose specific failure risks.

Harmonicity uses Praat cross-correlation, 10 ms step, 75 Hz minimum pitch, .1 silence threshold, and one period per window. Undefined floor values are excluded. HNR is treated as a signal periodicity estimate, **not perceived breathiness, emotional vulnerability, vocal health, or actor intent**.

### Spectral shape and text-normalized duration

Spectral measurements use 40 ms Hann windows, 10 ms hop, a band from 80 Hz to the 8 kHz analysis Nyquist limit, and energy-active frames. They include power-weighted centroid, spectral flatness, low-to-high band power, and a least-squares slope of dB power against log2 frequency over 500–4,000 Hz. These are recording-dependent proxies, not a timbre judgment detached from source mix or language.

Written-unit proxies use English orthographic words, Chinese Han characters, Japanese kana-plus-Han characters, and Korean Hangul syllable blocks. Markup is removed. Wholly parenthetical annotation captions and zero-unit captions do not receive lexical-rate values. These definitions are not interchangeable syllable counts. Neither total-duration nor active-duration normalization is a true articulation rate, because words and phonemes have not been aligned to the recording. No automatic transcript was substituted for the canonical source wording.

## 4. Quality and completion denominators

The conservative principal pitch gate requires a mono object, at least ten estimated voiced frames, and absence of the parameter-sensitivity and edge-band flags. **2,531 of 2,652 direct objects** pass. **121** remain outside the pitch-comparison denominator; they are not missing, silently deleted, or declared corrupt. Direct flag counts overlap: 79 edge-band, 38 parameter-sensitive, 19 short-voicing, four multichannel. Sixteen direct objects exceed 40 seconds and retain a caption-extent review flag.

There were no exact-full-scale-sample flags in this collection. That limited result does not establish that every recording is free of all audible distortion. Similarly, a high-quality decode says nothing about whether a subtitle covers every sound in the file.

| Witness | Unique objects | Pitch-QC objects | Median F0 (Hz) | Median within-object P10–P90 range (semitones) | Median duration (s) | Median active-frame level (dBFS) |
|---|---:|---:|---:|---:|---:|---:|
| Chinese | 663 | 618 | 334.1 | 7.73 | 4.036 | -23.51 |
| English | 664 | 635 | 301.2 | 8.61 | 4.028 | -23.22 |
| Japanese | 662 | 641 | 339.7 | 8.27 | 4.531 | -21.40 |
| Korean | 663 | 637 | 319.8 | 9.84 | 4.664 | -22.59 |

These pitch values describe the particular localized recordings and estimator gate. Differences between actors/languages are **not rankings of character authenticity**. The range column first computes each object’s voiced F0 P10–P90 semitone range, then takes its median across qualified objects. It is not the entire corpus’s pitch span. Duration and active-frame level use their own stated object denominators, not the pitch-only denominator.

## 5. Reproducibility and threshold sensitivity

New native duration exactly reproduces the older measurement values; maximum absolute RMS and peak deviations are below 10^-14 dB, numerical roundoff. This independently verifies the earlier basic fields against the acquired samples. It does not turn the older acoustic tables into a performed-listening study.

The new gate uses exact sample-weighted partial-window handling, whereas the old supplied low-energy fraction uses its own 20 ms implementation. Their low-energy fractions are retained as **different definitions**, not asserted byte-identical. Threshold sensitivity is visible:

| Witness | Median low-energy fraction at -50 / -45 / -40 dBFS | Median active-duration change, -50 to -40 (s) |
|---|---|---:|
| Chinese | 0.2919 / 0.3286 / 0.3664 | 0.30 |
| English | 0.2904 / 0.3218 / 0.3640 | 0.26 |
| Japanese | 0.2818 / 0.3073 / 0.3371 | 0.24 |
| Korean | 0.2520 / 0.2890 / 0.3284 | 0.36 |

The choice of threshold changes the apparent amount of low-energy time. This prevents a precise-looking gap total from being treated as an objectively annotated hesitation duration. The baseline is reproducible, but the interpretation of a gap still requires context and often listening.

All 2,809 objects passed duration-partition, internal-gap-bound, and gate-monotonicity checks. An additional deterministic remeasurement selected one mono object in each language and one three-channel counterpart object; **all five reproduced every top-level result field exactly**. This is a reproducibility spot-check after full-corpus identity and measurement validation, not a claim that all 2,809 objects were independently remeasured twice. See [the executed reproduction report](AUDIO_REPRODUCTION_CHECK.json).

## 6. Normalization without false comparability

Models are fitted separately within each language and source subclass. The source subclasses are story dialogue; archive conversation/favor topics 01–18; archive idle/self-introduction 19–22; archive greeting/team/ascension 23–31; and archive gameplay triggers 32–73. These labels are checked against the archive menu titles. They are task/context bins, not inferred emotional states or a chronology of development.

For groups with at least eight suitable unique mono objects and at least two written units, a Huber regression predicts log duration from log written-unit count. A separate fit predicts log energy-active duration. Settings are epsilon 1.35, alpha zero, and maximum 1,000 iterations. The analytical output is an observed-minus-predicted **log-duration residual**, with coefficients and fit denominator retained. It controls one aspect of text length, not all phonetic, syntactic, recording, or performance differences. The four-item idle/introduction bin does not receive a fabricated adequately powered fit.

Within-language percentiles use unique mono direct objects; pitch percentiles additionally use the pitch gate. Reused PCM is deduplicated within a comparison, while all semantic/render associations remain in the evidence supplement. No counterpart is used as a baseline for Sigrika. Broad within-language percentiles remain source-mixed; the additional source-class tables and residuals make that limitation inspectable rather than claiming a perfect actor-normalized causal comparison.

## 7. Source-defined contrasts

The eight cohorts were selected through literal source addresses and the prior textual reading, not by guessing emotion from sound. Complete denominators, source IDs, and values are in [the cohort table](AUDIO_CONTEXT_COHORTS.json).

| Source-defined cohort | Semantic lines | Pitch percentile medians ZH / EN / JA / KO | Active-frame level percentile medians ZH / EN / JA / KO |
|---|---:|---|---|
| SIG-AC-01 — After-nightmare self-blame and request for help | 17 | 74.9 / 73.2 / 57.5 / 70.1 | 11.3 / 11.5 / 19.7 / 16.5 |
| SIG-AC-02 — Admitting the weight of expectations and choosing action | 10 | 35.8 / 27.0 / 28.4 / 27.5 | 33.7 / 50.8 / 45.4 / 17.2 |
| SIG-AC-03 — Rooftop retreat and request for company | 11 | 3.1 / 14.4 / 2.3 / 7.1 | 24.8 / 66.4 / 22.0 / 26.7 |
| SIG-AC-04 — Later rooftop break and chosen activities | 10 | 24.9 / 41.6 / 23.6 / 48.7 | 42.6 / 83.2 / 63.5 / 59.9 |
| SIG-AC-05 — Birdwatching, photographic mistakes, and return to training | 13 | 32.3 / 47.0 / 47.5 / 43.4 | 35.7 / 61.5 / 70.7 / 75.2 |
| SIG-AC-06 — Denia birthday: noticing differences and asking about next year | 11 | 57.4 / 50.3 / 44.4 / 61.9 | 49.6 / 60.9 / 27.3 / 43.1 |
| SIG-AC-07 — Earlier childhood game converted to repeated victory | 5 | 9.8 / 6.5 / 36.7 / 22.8 | 46.6 / 67.5 / 85.2 / 77.1 |
| SIG-AC-08 — Post-resolution festival thanks, candy, birds, and photograph | 13 | 62.5 / 43.5 / 64.8 / 86.6 | 43.1 / 41.0 / 54.8 / 57.0 |

### Rooftop contrast

The retreat cohort at `15255/6` contains eleven semantic lines; the later chosen-break cohort at `15256/4` contains ten. The direction of four aggregate measures agrees across the four witnesses:

| Witness | Retreat / later pitch (Hz) | Retreat / later range (semitones) | Retreat / later active-frame level (dBFS) | Retreat / later low-energy fraction |
|---|---:|---:|---:|---:|
| Chinese | 274.5 / 303.7 | 5.29 / 9.76 | -24.75 / -23.75 | 0.415 / 0.342 |
| English | 242.8 / 285.9 | 4.62 / 9.17 | -22.54 / -21.80 | 0.398 / 0.282 |
| Japanese | 274.8 / 309.4 | 6.43 / 9.52 | -23.17 / -20.93 | 0.400 / 0.311 |
| Korean | 269.7 / 319.0 | 8.31 / 12.87 | -23.57 / -22.28 | 0.325 / 0.260 |

This is analytically useful because the ordinary-life model already distinguishes retreat from a self-chosen holiday. The audio supplies a new recording-level contrast compatible with that distinction. It does not prove causality, permanent recovery, or a fixed formula for expressing rest. The Chinese single-line counterexample in cases 09 and 10 forbids treating this cohort tendency as an invariant. [SIG-AF-04](WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md#sig-af-04)

### Aftermath, birthday, and gold

The aftermath at `12423/4` combines relatively high pitch-percentile medians with low active-frame level percentiles, unlike the very low pitch percentile of the rooftop retreat. “Distress means lower pitch” therefore fails even within the source-defined examples. [SIG-AF-03](WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md#sig-af-03)

The Denia birthday cohort does not uniformly occupy the low-energy or low-pitch tail. Its next-year request has substantially different within-language pitch positions. The underlying recognition and concern remain text-supported; their audible affect and relationship meaning are not read directly from the percentile values. [SIG-AF-05](WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md#sig-af-05)

The gold passage’s weight-of-expectation line and later even-if-I-cannot line show different median-F0 movement across languages. English does not repeat the upward change seen in the other three particular pairs. This is not grounds for choosing a more authentic dub; wording, contour, and event context must remain separate. [SIG-AF-06](WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md#sig-af-06)

## 8. Clusters, representatives, and outliers

Exploratory K-means uses seven features: log median F0, within-object pitch range, active-frame median level, low-energy fraction, text-length log-duration residual, HNR, and spectral centroid. Each feature is centered and scaled by its within-language median and interquartile range, clipped to [-5, 5]. Runs use three clusters, 30 initializations, seed 7; seed 19 and a four-cluster run test sensitivity. Silhouette uses up to 500 samples, seed 7.

| Witness | Qualified objects used | Three-cluster silhouette | Seed-7 vs seed-19 adjusted Rand index | Three- vs four-cluster adjusted Rand index |
|---|---:|---:|---:|---:|
| Chinese | 614 | 0.168 | 1.000 | 0.857 |
| English | 630 | 0.173 | 0.807 | 0.332 |
| Japanese | 634 | 0.290 | 0.972 | 0.766 |
| Korean | 632 | 0.253 | 1.000 | 0.485 |

The limited silhouette separation, English seed variation, and sensitivity to cluster count mean the partition cannot responsibly be named three personality states. The numerical regimes and actual nearest-centroid representatives are preserved in [the cluster results](AUDIO_CLUSTER_RESULTS.json), including source-class and source-state mixtures. They organize review; they do not label feelings. [SIG-AF-10](WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md#sig-af-10)

Sixteen new nominations select each language’s longest recording, lowest whole-object RMS, greatest positive duration residual, and widest QC-qualified pitch range. All are already acquired and measured. The longest clip is not automatically the most informative; the lowest-level clip may contain nonlexical content. Twenty separate **same-semantic-occurrence** cases preserve all four localized texts and recording identities. The case set is not a certification of equivalent audiovisual edits or a human listening worksheet marked complete.

## 9. Source-mapped absences and Stage 2

The final declaration action `12967/1` has six accepted direct occurrences with `play_voice=false` and zero resolved line-level media associations. The later call action `16901/4` has eighteen; `16826/2` has nineteen. These are source-mapping boundaries, not failed members of the 666-line voiced denominator. Nearby gold-speech recordings and the voiced archive retrospective about a call cannot be substituted for the missing exact occurrences. [SIG-AF-08](WUWA_SIGRIKA_AUDIO_REVISION_LEDGER.md#sig-af-08)

Video acquisition and analysis are **deferred by the owner** to a local environment using full-size 1080p or larger source video. The future stage should check cinematic/event audio, exact subtitle-to-dialogue routing, branch identity, turn-taking, and synchronization before interpreting delivery or gesture. An absent line mapping does not prove an eventual video witness is silent. No video was fetched, downscaled, viewed, or used to claim completion in this audio stage.

## 10. Completion and reproduction contract

`machine_voice_profiled` is now claimed **for the entire declared usable audio-object collection under the documented signal methods and QC restrictions**. This is more than metadata aggregation: samples were acquired, decoded, newly measured, normalized, compared, and placed in source-linked review cohorts. A claim-driven speech revision and twelve additional non-blind audio-constraint probes propagate the findings downstream.

Still not claimed: human-performance review, validated word/phoneme alignment, isolated clean stems, true articulation rate, audiovisual hardening, or integrated audiovisual reconstruction. Source text supplies scene semantics. Signal analysis supplies measurements. A listener would supply a separate perceptual judgment. None silently replaces the others.

The analysis ZIP contains aggregate results, selected-case metadata, method parameters, and reproducible scripts. The separate local **audio evidence supplement** contains all object-level and association-level measurements. Neither ZIP contains raw FLAC, source WEM, or downloaded game archives. No Drive or Git write occurred; the supplement is locally staged for a future separately authorized evidence publication.

Reproduction uses the same canonical source JSONL, exact nineteen archives, Python dependencies recorded in `AUDIO_METHOD_PARAMETERS.json`, and the scripts in `audio_tools/`. The tools perform no network requests. Their command contract is in `AUDIO_REPRODUCTION_INSTRUCTIONS.txt`. Every output can be traced to an exact source occurrence, render, native payload, FLAC object, archive member, and source generation. Mechanical reproduction cannot independently prove the literary interpretation.
