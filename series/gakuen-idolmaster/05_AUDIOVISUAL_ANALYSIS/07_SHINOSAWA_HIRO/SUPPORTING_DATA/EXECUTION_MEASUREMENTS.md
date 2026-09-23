---
series: GKM
generation: V2
artifact_type: historical_supporting_record
status: historical_legacy
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
source_boundary: "Preserved earlier-generation supporting record; not fresh AVE-FULL evidence."
last_updated: '2026-09-10'
---

> **Public repository representation.** Machine-specific paths use `WORKSPACE/`, `LOCAL_USER/` or `LOCAL_DRIVE_*` placeholders; configure these roots before reproduction. Direct Drive URLs are represented by source-object IDs. Original execution hashes and exported-byte claims identify the archived originals; public code/data snippets containing these substitutions are explicitly derivatives. The import manifest records their final repository hashes and decoded payload hashes.

> Historical record retained from the previous packet. “New/current” in this document refers to that earlier execution, not AVE-FULL-20260910. Fresh results are in [the current measurements](FULL_REBUILD_MEASUREMENTS.md) and [current claim review](FULL_REBUILD_CLAIM_REVIEW.md).

# HIRO technical measurements — current Windows execution

This supplement records work actually executed during the authorized rebuild. Incoming ZIP calculations remain separately labeled in the existing supporting tables, even though both generations bear the date 2026-09-10. Current automated calculations do not establish direct listening, continuous watching, speaker-isolated properties or narrative interpretation. Exact inputs are linked to [current source verification](EXECUTION_SOURCE_VERIFICATION.md).

Current scope in this package: **11 result records; 1,513 scheduled visual samples, 1,513 successful reads, zero omitted reads**. The independent data audit covered all 32 current records across both characters, checked actual input hashes, parameter/cache fingerprints, interval bounds, decoded sample/STFT counts, RMS ratios, silence sums and per-sample visual reductions, and found zero discrepancies in those checks. This data audit is distinct from the final document/package audit.

The 11 current results are the full original H04, a hash-matched H03 whole-source reproduction check, and all nine inputs in the principal/common 3DMV comparison. Other source rows are retained incoming measurements on newly recovered matching inputs; they are not silently relabeled as reruns. The H04 original uses alias `H04_ORIGINAL` here so it cannot be confused with the incoming trimmed H04 measurement object.

H04 original SHA-256 `4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468`, 545587232 bytes, container 3516.615692 seconds; incoming derivative SHA-256 `de92afafb3181342407ab9405f4951e820bfdafaad5b1e9538ec9d7f73ea826e`, 519296380 bytes, container 3316.029383 seconds. The separate packet audit establishes identical retained compressed payloads and PTS/DTS/duration for 198763 video and 142809 audio packets. Retained source-clock locators transfer without an offset. The full original’s additional tail changes whole-source measurement populations; its results below are not a replacement for the derivative’s historical values. See the packet evidence and executable procedure in [source verification](EXECUTION_SOURCE_VERIFICATION.md).

## Runtime, method and safeguards

The incoming methods document reports Python 3.12.14, FFmpeg/ffprobe 6.1.1-3ubuntu5, NumPy 2.5.3, SciPy 1.18.1, librosa 1.0.0 and OpenCV 5.0.0. These are historical recorded versions, not the current machine or a certified recreation of that environment. Current observed versions follow; full FFmpeg/ffprobe build output is retained in each result’s processing identity.

| Runtime field | Current observed value |
| --- | --- |
| python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| platform | Windows-11-10.0.26200-SP0 |
| numpy | 2.1.2 |
| opencv | 4.13.0 |
| librosa | 1.0.0 |
| scipy | 1.18.0 |
| ffmpeg_command | ffmpeg |
| ffprobe_command | ffprobe |
| FFmpeg/ffprobe version | 8.1.1-essentials_build-www.gyan.dev |
| Executed helper SHA-256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


Custom audio features use the first audio stream, decoded to mono float32 at 22050 Hz; FFT 2048, hop 512, periodic Hann, no centered padding, incomplete final windows discarded. R128 and low-level detection use native channel layout. For bounded intervals, decoded timestamps are reset and atrim is applied before feature filters or resampling; the resulting interval is reset to local time zero. This prevents an output seek from allowing earlier samples to contaminate interval loudness. All supplied measured inputs have zero-start first audio streams. Unusual nonzero-start media would require a separately reviewed clock mapping.

The full mix is retained; there is no normalization, denoising, source separation or diarization. Formulas and music options are fully specified in the executable code below and the per-result parameter tables. No F0, speaker-specific breathiness, structural-novelty proxy or pose-quality value is manufactured. [Incoming methods and retained history](MEASUREMENT_METHODS_AND_REPRODUCTION.md) remain available for comparison.

Visual sampling is at start + 5k seconds while the requested time is before the interval end. One moving video stream at index 0 is required; attached cover images do not count as that stream. OpenCV CAP_FFMPEG decodes the whole frame, resized to 160×90 with INTER_AREA; luma uses BGR2GRAY/255, saturation uses HSV S/255, differences are means of absolute consecutive gray values, and histogram jumps use 8×8×8 BGR bins with L1 normalization and Bhattacharyya distance strictly greater than 0.5. These measures include UI, uploader matter and background; they do not isolate the character.

Some OpenCV H.264 reads emitted `mmco: unref short failure` while continuing. Every scheduled read in these runs returned a frame, but success does not prove artifact-free decoding. The per-record `decode_warnings` field captures the separate FFmpeg audio-feature decode stderr only; an empty value there does not erase the observed OpenCV stderr warnings.

The helper requires an explicit input or an input directory containing exactly one media file, plus an expected SHA-256 and source ID. It hashes the actual file before accepting a cache, binds source/parameters/software/script to the cache fingerprint, rejects mismatches by default, writes under an exclusive lock and atomic commit, and verifies the input hash again after processing. Reuse never relies only on filenames. Integration checks used a known tone followed by silence to verify independent interval loudness, sample counts, silent true peak, hash mismatch rejection, parameter mismatch rejection and ambiguous directory rejection; the helper passed those checks.

Numerical tables use 15 significant digits for reproducibility. This display precision does not imply equivalent perceptual, temporal or cross-runtime accuracy.

## Comparison with byte-identical incoming inputs

These are independent runs on the exact recorded input hashes. The supplied numerical tables remain the incoming generation; this report records the Windows generation. Equality here is evaluated at the incoming 12-significant-digit display precision, with a comparison tolerance of max(2×10⁻⁹ absolute, 2×10⁻¹⁰ relative). A disagreement is recorded even where it is too small to support a substantive interpretation.

| Alias | Family | Field | Incoming value | Current value | Absolute delta |
| --- | --- | --- | --- | --- | --- |
| H03 | loudness | silence_seconds | 122.96711 | 122.950403000001 | 0.0167069999992435 |
| H03 | visual | brightness_mean | 0.674519683127 | 0.672457406761256 | 0.00206227636574363 |
| H03 | visual | saturation_mean | 0.233767810862 | 0.225861321180682 | 0.00790648968131791 |
| H03 | visual | frame_difference_mean | 0.0680930444141 | 0.0683752938400905 | 0.000282249425990547 |
| H12 | loudness | silence_seconds | 15.101901 | 15.101859 | 4.2000000007647e-05 |
| H12 | visual | brightness_mean | 0.246434858276 | 0.246693721144564 | 0.000258862868563609 |
| H12 | visual | saturation_mean | 0.381766370128 | 0.384452009198741 | 0.00268563907074121 |
| H12 | visual | frame_difference_mean | 0.232700391327 | 0.234545046516827 | 0.00184465518982718 |
| H15 | audio | chroma_entropy_bits_mean | 3.02042245865 | 3.02042269706726 | 2.38417260600698e-07 |
| H15 | loudness | silence_seconds | 8.635475 | 8.63510300000002 | 0.000371999999980943 |
| H15 | visual | brightness_mean | 0.15353175707 | 0.154454547366718 | 0.000922790296717962 |
| H15 | visual | saturation_mean | 0.436602941176 | 0.430133362559116 | 0.00646957861688424 |
| H15 | visual | frame_difference_mean | 0.145980019681 | 0.147859859094024 | 0.00187983941302372 |
| H17 | loudness | silence_seconds | 9.102526 | 9.10251800000001 | 7.99999999223644e-06 |
| H17 | visual | brightness_mean | 0.335903769208 | 0.338472130934934 | 0.00256836172693431 |
| H17 | visual | saturation_mean | 0.354279448566 | 0.346821181475593 | 0.00745826709040681 |
| H17 | visual | frame_difference_mean | 0.213435724585 | 0.216328020104104 | 0.00289229551910364 |
| H19 | loudness | silence_seconds | 10.20131 | 10.201111 | 0.000199000000025151 |
| H19 | visual | brightness_mean | 0.248944518871 | 0.246706733602051 | 0.00223778526894916 |
| H19 | visual | saturation_mean | 0.439282168086 | 0.440363727140688 | 0.00108155905468788 |
| H19 | visual | frame_difference_mean | 0.22234274447 | 0.22229598229751 | 4.67621724900835e-05 |
| H20 | audio | tonnetz_motion_mean | 0.151006129917 | 0.151006131921803 | 2.00480279599624e-09 |
| H20 | visual | brightness_mean | 0.311191211455 | 0.302199866622686 | 0.00899134483231362 |
| H20 | visual | saturation_mean | 0.501937363834 | 0.511921900531046 | 0.0099845366970458 |
| H20 | visual | frame_difference_mean | 0.243805308976 | 0.240365489596321 | 0.00343981937967927 |
| H20 | visual | histogram_jumps_gt_0_5 | 16 | 17 | 1 |
| H21 | loudness | silence_seconds | 9.37132 | 9.371157 | 0.000162999999997027 |
| H21 | visual | brightness_mean | 0.251804765049 | 0.252902740914736 | 0.00109797586573646 |
| H21 | visual | saturation_mean | 0.436908461211 | 0.428721878848158 | 0.00818658236284231 |
| H21 | visual | frame_difference_mean | 0.225604869087 | 0.227845540439541 | 0.00224067135254069 |
| H22 | loudness | silence_seconds | 10.383517 | 10.383764 | 0.000246999999996333 |
| H22 | visual | brightness_mean | 0.37687754631 | 0.374764359515646 | 0.00211318679435374 |
| H22 | visual | saturation_mean | 0.416030465568 | 0.412970351425594 | 0.00306011414240559 |
| H22 | visual | frame_difference_mean | 0.200773966075 | 0.205169625918974 | 0.00439565984397358 |
| H23 | loudness | silence_seconds | 16.561174 | 16.561406 | 0.000231999999989796 |
| H23 | visual | brightness_mean | 0.447385093818 | 0.439929566035668 | 0.00745552778233194 |
| H23 | visual | saturation_mean | 0.35637092638 | 0.36827269426289 | 0.0119017678828903 |
| H23 | visual | frame_difference_mean | 0.208920065152 | 0.214205447260452 | 0.00528538210845234 |
| H25 | audio | chroma_entropy_bits_mean | 2.94575667381 | 2.94575691223145 | 2.38421445253323e-07 |
| H25 | loudness | silence_seconds | 12.773562 | 12.773583 | 2.10000000038235e-05 |
| H25 | visual | brightness_mean | 0.176351338695 | 0.170975287938213 | 0.0053760507567871 |
| H25 | visual | saturation_mean | 0.476087059319 | 0.490925009902951 | 0.0148379505839511 |
| H25 | visual | frame_difference_mean | 0.173745768056 | 0.17034180781671 | 0.00340396023929021 |


Every common numerical summary field not listed above agrees within the declared comparison tolerance. Basic audio sample counts, spectral/RMS descriptors and EBU R128 summaries reproduce on these sources. Small music-feature disagreements listed above are retained; software versions alone do not isolate their cause.

| Alias | Incoming visual n | Current visual n | Same requested times | Max reported-time delta s | Max luma delta | At source s | Max saturation delta | At source s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H03 | 538 | 538 | true | 0 | 0.0260318517686284 | 2635 | 0.0360626361655622 | 1100 |
| H12 | 36 | 36 | true | 0 | 0.0163230597968938 | 110 | 0.0399961873640282 | 10 |
| H15 | 41 | 41 | true | 0 | 0.0150555521247359 | 100 | 0.0310939542479063 | 75 |
| H17 | 37 | 37 | true | 0 | 0.0179166793822849 | 110 | 0.0322783224403007 | 60 |
| H19 | 33 | 33 | true | 0 | 0.0202475637194426 | 10 | 0.0437753267973639 | 10 |
| H20 | 32 | 32 | true | 0 | 0.0220484733583745 | 45 | 0.0564259259261699 | 40 |
| H21 | 23 | 23 | true | 0 | 0.0202075243000177 | 85 | 0.0364547930284184 | 60 |
| H22 | 23 | 23 | true | 0 | 0.0282783508302852 | 95 | 0.0464964596948432 | 95 |
| H23 | 24 | 24 | true | 0 | 0.0239204168322266 | 60 | 0.0505468409583726 | 30 |
| H25 | 22 | 22 | true | 0 | 0.0282333940271972 | 80 | 0.0848499455341264 | 45 |


| Alias | Incoming low-level interval n | Current interval n | Max start delta s | Max end delta s |
| --- | --- | --- | --- | --- |
| H03 | 94 | 94 | 0.00494299999991199 | 0.00498900000002322 |
| H12 | 3 | 3 | 0.000258999999999787 | 0.000217999999989615 |
| H15 | 3 | 3 | 0.000323999999977787 | 5.19999999823995e-05 |
| H17 | 3 | 3 | 0.00011299999999892 | 0.00010199999999827 |
| H19 | 3 | 3 | 0.000273999999990338 | 0.000474000000025399 |
| H20 | 0 | 0 | N/A | N/A |
| H21 | 2 | 2 | 0.000281000000001086 | 0.000125000000011255 |
| H22 | 3 | 3 | 7.30000000004338e-05 | 0.000324000000006208 |
| H23 | 3 | 3 | 0.000180999999997766 | 5.19999999966103e-05 |
| H25 | 3 | 3 | 0.000365000000002169 | 0.00035400000000152 |


Low-level detector endpoint precision differs between the recorded FFmpeg generations, especially for long timestamps. Corresponding endpoints are within 0.005 seconds in the H03/M03 checks. Totals in this report are sums of current end-minus-start intervals and are not forced to match totals produced from the incoming rounded logs. A source with zero detected intervals has no endpoint delta.

The current and incoming visual samples use identical requested source times; reported times also correspond to the precision shown. Pixel-derived results nonetheless differ. The current Windows/OpenCV runtime and the incoming Linux/OpenCV runtime are separate processing conditions. Exact cause has not been isolated. These differences cannot establish fine changes in acting, choreography, expression, lighting design, shot count or motion speed. The 5-second histogram threshold is a sparse image-change proxy; a value crossing 0.5 can change its count without constituting a newly established edit.

## Bounded decoder-discrepancy inspection

A separate auditor directly viewed one extracted current still at H03 source time 2635 seconds to investigate a maximum-luma discrepancy. Input SHA-256: `3b533ccfdfa1d4a284c660f8f3ab5f87c7ca18d52e5f6a4e758f7197493e6989`. A close stage-performance portrait occupies the frame amid saturated pink/blue lighting. This is a technical still-image check, not listening or continuous performance inspection. The same still was decoded with OpenCV default selection and explicit CAP_FFMPEG; both selected the FFMPEG backend and their maximum pixel difference was 0. Therefore merely selecting that backend explicitly does not explain the cross-generation difference. The incoming runtime was not recreated for pixel identity.

| Requested backend | Actual backend | Reported source s | Luma | Saturation |
| --- | --- | --- | --- | --- |
| 0 | FFMPEG | 2635 | 0.539433598518372 | 0.497052832244009 |
| 1900 | FFMPEG | 2635 | 0.539433598518372 | 0.497052832244009 |


## Near-zero RMS percentiles and threshold sensitivity

RMS P90/P10 is 20 log10(max(P90, ε)/max(P10, ε)) with ε = 10⁻¹². It summarizes complete 2048-sample windows of the entire mixed recording, including silent openings, music, effects and several speakers. It is not EBU LRA or an estimate of an individual performer’s expressive dynamic range. Where P10 is zero or nearly zero, the ratio mainly reflects the denominator and chosen numerical floor.

| Alias | Interval | P10 linear | P90 linear | 10^-12 floor applied | Frames below 10^-8 | Complete RMS frames | Reported ratio dB |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H23 | whole_song_reproduction_check | 7.37756150278584e-12 | 0.263534618656358 | false | 503 | 5021 | 211.058496695705 |


The incoming H31 whole-source record, not rerun here, likewise has P10 = 0 and RMS P90/P10 = 230.283647623 dB. Its input hash is now independently recovered, but its ratio remains an incoming calculation with the same denominator limitation.

| Alias | Interval | Hypothetical denominator floor ε | Ratio dB under this floor |
| --- | --- | --- | --- |
| H23 | whole_song_reproduction_check | 1e-12 | 211.058496695705 |
| H23 | whole_song_reproduction_check | 1e-08 | 148.416753469065 |
| H23 | whole_song_reproduction_check | 1e-06 | 108.416753469065 |
| H23 | whole_song_reproduction_check | 0.0001 | 68.416753469065 |


This sensitivity table changes only the numerical floor applied to the already computed percentiles. It is an algebraic diagnostic, not a new signal extraction, accepted replacement estimator or calibrated perceptual measure. The large change demonstrates why near-zero-P10 ratios must not be read as expressive range. No cause is assigned to a specific audible event without separate audio review.

Silence detection is a separate threshold operation: amplitude below −50 dB for at least 0.5 seconds in the combined first audio stream. Changing this threshold or duration would change eligible intervals; this execution did not perform that signal-level threshold sweep. Reported detector intervals therefore cannot be equated with speaker pauses, hesitation, breath or absence of BGM.

## Current equal-weight song-group reductions

The same pre-existing membership is retained: three principal solo 3DMVs and six common 3DMVs. These are equal-weight arithmetic means of source-level results, not pooled frame estimates, significance tests or a sample of independent performances. Track duration, mix, uploader packaging and common assets differ.

| Group | Members | Source n | Feature | Mean from incoming displayed values | Current mean | Current minus incoming |
| --- | --- | --- | --- | --- | --- | --- |
| Principal solo 3DMV | H12, H15, H17 | 3 | tempo_bpm | 127.550743869667 | 127.550743869617 | -4.94253526994726e-11 |
| Principal solo 3DMV | H12, H15, H17 | 3 | beat_interval_cv | 0.0441366917508333 | 0.0441366917508298 | -3.53189699708878e-15 |
| Principal solo 3DMV | H12, H15, H17 | 3 | local_tempo_cv | 0.167536577561 | 0.167536577561241 | 2.40807374041196e-13 |
| Principal solo 3DMV | H12, H15, H17 | 3 | chroma_entropy_bits_mean | 2.93582479159 | 2.93582487106323 | 7.94732324393976e-08 |
| Principal solo 3DMV | H12, H15, H17 | 3 | tonnetz_motion_mean | 0.120182258196333 | 0.120182259070542 | 8.74208316847813e-10 |
| Principal solo 3DMV | H12, H15, H17 | 3 | rms_p90_p10_db | 23.7780588130567 | 23.7780588135808 | 5.24131849033438e-10 |
| Principal solo 3DMV | H12, H15, H17 | 3 | flatness_mean | 0.0814987114914 | 0.0814987114892364 | -2.16363038596512e-12 |
| Principal solo 3DMV | H12, H15, H17 | 3 | positive_normalized_flux_mean | 0.0246880769777667 | 0.0246880769777599 | -6.72725763983806e-15 |
| Principal solo 3DMV | H12, H15, H17 | 3 | flux_cv | 0.441073066434 | 0.441073066467116 | 3.3116176467729e-11 |
| Common 3DMV | H19, H20, H21, H22, H23, H25 | 6 | tempo_bpm | 128.340889038333 | 128.340889038389 | 5.58486590307439e-11 |
| Common 3DMV | H19, H20, H21, H22, H23, H25 | 6 | beat_interval_cv | 0.0437059404835333 | 0.0437059404835255 | -7.83401121751126e-15 |
| Common 3DMV | H19, H20, H21, H22, H23, H25 | 6 | local_tempo_cv | 0.194384630085167 | 0.194384630085264 | 9.74220704108575e-14 |
| Common 3DMV | H19, H20, H21, H22, H23, H25 | 6 | chroma_entropy_bits_mean | 2.92573281129333 | 2.92573285102844 | 3.97351089809206e-08 |
| Common 3DMV | H19, H20, H21, H22, H23, H25 | 6 | tonnetz_motion_mean | 0.134923419038833 | 0.134923419793062 | 7.54228984822802e-10 |
| Common 3DMV | H19, H20, H21, H22, H23, H25 | 6 | rms_p90_p10_db | 60.5825248388483 | 60.5825248384049 | -4.43407088823733e-10 |
| Common 3DMV | H19, H20, H21, H22, H23, H25 | 6 | flatness_mean | 0.112836087598417 | 0.112836087608255 | 9.8378388768694e-12 |
| Common 3DMV | H19, H20, H21, H22, H23, H25 | 6 | positive_normalized_flux_mean | 0.0234667866101667 | 0.0234667866099956 | -1.711096542234e-13 |
| Common 3DMV | H19, H20, H21, H22, H23, H25 | 6 | flux_cv | 0.457609683264333 | 0.457609683233125 | -3.1208813311423e-11 |


The common-group RMS P90/P10 mean is 60.5825248384049 dB; removing H23 solely as a sensitivity diagnostic yields 30.4873304669449 dB across the other five sources. This is not a revised primary group result. H23’s near-zero P10 drives the original mean; neither group ratio supplies evidence for greater or lesser expressive dynamic range. The undefined historical composite proxy and its nan group means remain retired.

## Result inventory and reproduction

| Alias | Label | Input SHA-256 | Working result JSON SHA-256 | Processing fingerprint |
| --- | --- | --- | --- | --- |
| H04_ORIGINAL | full_original_source | 4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468 | fff40c2c8c89333e9c266f74461fb897c533c4f34309baf69c674a4212d5834e | 5952bf3f0c8c06053192ed89e2ac7d7cc1f074dd309a1f6a65bd24332fd961fe |
| H03 | whole_source_reproduction_check | 3b533ccfdfa1d4a284c660f8f3ab5f87c7ca18d52e5f6a4e758f7197493e6989 | cead87a0581a86285c882c9f0b5287367188a2d8d6780f415dba59cdf41e2ef8 | 55e2cb3f1549def9dc11a7c3292de50486ce84dc972cc078499ee94e277879c4 |
| H12 | whole_song_reproduction_check | 346649b3c41f8cf987125c344e09d29f1818187240132acfbc5eed89d854462c | 8bc65bf47ab4620590a23792a845b5e05d365d82d89d9125973a9f7d11884d5a | 5c3cdac2904206f45996397dd0d4226912fb85bd10f8ae941bfe6283ed0121fd |
| H15 | whole_song_reproduction_check | ea62087e203b892295f6bb27f68426779b1d0c37ceb83c522977942e1c7bf2aa | c30534f84d71dceef1127c2ac402509336ef369576bafd64e5ff1da41c4658ee | fba2c32ac358bca18acc233a4a20d75a920c42523740f2fa638c3d2d0474b4f3 |
| H17 | whole_song_reproduction_check | be3709652b63a93a30bba202dc06296169262af269b84b77109335d65e5bd8cd | 560fa64fdfbc6fa3484e37492b5b704e816dee79a28d27ed628397d5e765b046 | 3a858b0397373f05eba200aaf6ec33a3930a54d0b3ccba05a390c62694a719fc |
| H19 | whole_song_reproduction_check | a692b45cc3ee31ff957c0199bae17c1c2f143c2271f3c1e19abf4d77a8e634ef | 90bbe9ce249af2942b146493a9c3b092e908832f68c78b4343ba839f46fbe3fd | 9f580bfb429f79383da074929385c29510035c2768a5c79f6a787922f5d7db65 |
| H20 | whole_song_reproduction_check | 3ae933080d1da33631c2f491aea6969b0b2801cc48442c4023290632ae22aed0 | 0c8a5cffdac1e29506fbe78cd9fc38814bf92bf7da6cee505c25cfaefe30e841 | 3ec52c974fc776736ee8d7f3d1fb759e501e35ae95bbf18ce38c1ee6ff68f622 |
| H21 | whole_song_reproduction_check | cbfae7e9f90821d0c70a16201a9ba462603548f899fa93b5ab94fb76c0e248f7 | c4a6421ab8230069a590b958de43fc52f8585317045d6a38882750c6b656901f | 6b1150a4db70662f9fba6ec10333189495c2d3747a690d86c9466e45bb9c6417 |
| H22 | whole_song_reproduction_check | 42ddef86a794641182d2b3ae143b5afd2a6b68bf2f08a5f989e373c45cd70ee9 | 06c6ec62c251be6e262818f6d84a017ce4028ad7f3bf98918b1a58915127e9fa | 5d912092dcb470a9a3f76e7f1817197093e68180357339f0e2119a8aa8923047 |
| H23 | whole_song_reproduction_check | 6761642adfb3ba089aa286cb147002decc2151e1b30471910afbef84946d9db6 | 05e8d2f7a2dc9069d970e9dc97262dbad1e1dbce8443dd65e2c1a276f610b1a6 | a29126a3563810b06a19f52e1f910077a3b36e5977f8dc17c9810ff644f2ee36 |
| H25 | whole_song_reproduction_check | 2599c7b4d83b267a76204cd8a463f47f2ebf2bcf995d7305be7b74b311d2f855 | 123a63b3982519503b5ecdf4f073f50a8e0c8fa1ad4431a6d546c74ebcaf6768 | 04c7b5f89c2c51be4e5c3ab4265ce4b1eac312ddaa52a7052a9926b470463410 |


The raw media, JSON results, Python environment and temporary frames remain outside the Markdown-only delivery. The complete result values and code are preserved below. To reproduce, save the Python block as `measure_current.py` with UTF-8 encoding, no BOM, LF line endings and one final newline; its SHA-256 must match the value above. Save the JSON block as `measurement_specs.json` outside the package and replace only each `path` with the location of that exact source hash. Install the recorded dependencies and provide the recorded FFmpeg tools. Then run the following command in that working directory. A changed runtime or script intentionally creates a different processing identity and must use a fresh result directory.

```text
python -X utf8 measure_current.py --specs measurement_specs.json --output-dir current-results --markdown current-results.md --workers 2
```

```json
[
  {
    "path": "LOCAL_USER/Downloads\\【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】-(720p60).mp4",
    "source_id": "1Toi0yHcoq0jV0GMcA4JalcrlLMbnFxQO",
    "sha256": "4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468",
    "character": "HIRO",
    "alias": "H04_ORIGINAL",
    "label": "full_original_source",
    "start_s": 0.0,
    "end_s": null,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": null
  },
  {
    "path": "LOCAL_USER/Downloads\\【学マス】篠澤広 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
    "source_id": "1EDx0YyXW11f6CNg2Too0fh-7jpaEVU9Q",
    "sha256": "3b533ccfdfa1d4a284c660f8f3ab5f87c7ca18d52e5f6a4e758f7197493e6989",
    "character": "HIRO",
    "alias": "H03",
    "label": "whole_source_reproduction_check",
    "start_s": 0.0,
    "end_s": null,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": null
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「光景」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "source_id": "1Y5zbtbMqqZw8K12HjP5Up_54Ce3jWjBk",
    "sha256": "346649b3c41f8cf987125c344e09d29f1818187240132acfbc5eed89d854462c",
    "character": "HIRO",
    "alias": "H12",
    "label": "whole_song_reproduction_check",
    "start_s": 0.0,
    "end_s": null,
    "music": true,
    "visual_step_s": 5.0,
    "boundary_note": null
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「コントラスト」 (篠澤広 ソロ2 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "source_id": "1JbU-ssxlwCzUGTnq4i2JLO-fw3EaPBxR",
    "sha256": "ea62087e203b892295f6bb27f68426779b1d0c37ceb83c522977942e1c7bf2aa",
    "character": "HIRO",
    "alias": "H15",
    "label": "whole_song_reproduction_check",
    "start_s": 0.0,
    "end_s": null,
    "music": true,
    "visual_step_s": 5.0,
    "boundary_note": null
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「サンフェーデッド」 (篠澤広 ソロ3 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "source_id": "11Sf_pH-3JhiLcAUT4xLkm8rbzYL84f8E",
    "sha256": "be3709652b63a93a30bba202dc06296169262af269b84b77109335d65e5bd8cd",
    "character": "HIRO",
    "alias": "H17",
    "label": "whole_song_reproduction_check",
    "start_s": 0.0,
    "end_s": null,
    "music": true,
    "visual_step_s": 5.0,
    "boundary_note": null
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Campus mode!!」(篠澤広 フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "source_id": "1NZfazcL67wDoVoFa5nuQp-y3E2-Edzmd",
    "sha256": "a692b45cc3ee31ff957c0199bae17c1c2f143c2271f3c1e19abf4d77a8e634ef",
    "character": "HIRO",
    "alias": "H19",
    "label": "whole_song_reproduction_check",
    "start_s": 0.0,
    "end_s": null,
    "music": true,
    "visual_step_s": 5.0,
    "boundary_note": null
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\【学マス】篠澤広「初」 3DMV-(592p30).mp4",
    "source_id": "1zPxR0JyPp4JhLxWS_zfENcC9znXerQIj",
    "sha256": "3ae933080d1da33631c2f491aea6969b0b2801cc48442c4023290632ae22aed0",
    "character": "HIRO",
    "alias": "H20",
    "label": "whole_song_reproduction_check",
    "start_s": 0.0,
    "end_s": null,
    "music": true,
    "visual_step_s": 5.0,
    "boundary_note": null
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Howling over the World」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "source_id": "1OXLlFgDZOfdom_Sywd_lF_j-dimUZeqp",
    "sha256": "cbfae7e9f90821d0c70a16201a9ba462603548f899fa93b5ab94fb76c0e248f7",
    "character": "HIRO",
    "alias": "H21",
    "label": "whole_song_reproduction_check",
    "start_s": 0.0,
    "end_s": null,
    "music": true,
    "visual_step_s": 5.0,
    "boundary_note": null
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「がむしゃらに行こう！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "source_id": "1tdzAna_WcWmo9RzC5lyLnliiyJaoDGpy",
    "sha256": "42ddef86a794641182d2b3ae143b5afd2a6b68bf2f08a5f989e373c45cd70ee9",
    "character": "HIRO",
    "alias": "H22",
    "label": "whole_song_reproduction_check",
    "start_s": 0.0,
    "end_s": null,
    "music": true,
    "visual_step_s": 5.0,
    "boundary_note": null
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ミラクルナナウ(ﾟ∀ﾟ)！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "source_id": "1P75Wv4Qu1W_R6lmZRs0fGmv4VOxoXcmG",
    "sha256": "6761642adfb3ba089aa286cb147002decc2151e1b30471910afbef84946d9db6",
    "character": "HIRO",
    "alias": "H23",
    "label": "whole_song_reproduction_check",
    "start_s": 0.0,
    "end_s": null,
    "music": true,
    "visual_step_s": 5.0,
    "boundary_note": null
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ENDLESS DANCE」(篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "source_id": "1K9In8GKh9pP041E6A0zg3hyX-lKdug7G",
    "sha256": "2599c7b4d83b267a76204cd8a463f47f2ebf2bcf995d7305be7b74b311d2f855",
    "character": "HIRO",
    "alias": "H25",
    "label": "whole_song_reproduction_check",
    "start_s": 0.0,
    "end_s": null,
    "music": true,
    "visual_step_s": 5.0,
    "boundary_note": null
  }
]
```

## Executed measurement helper

```python
"""Hash-bound mixed-source AV measurements for the authorized 2026-09-10 rebuild.

No perceptual inspection is implied. Input identity and time boundaries must be
established separately. Uses FFmpeg for decoding and OpenCV for sampled frames.
Unseparated mixes cannot yield character-isolated acoustic measurements.

Single input:
  python measure_current.py --input media.mp4 --source-id DRIVE_ID \
    --expected-sha256 HASH --output result.json
Bounded interval: add --start 10 --end 30 --label 'review window'.
Batch: --specs specs.json --output-dir results [--workers 2]. JSON is a list of
objects with path, source_id, sha256; optional character, alias, label, start_s,
end_s, music, visual_step_s, skip_visual, boundary_note. JSON stays outside ZIPs.
Add --markdown OUTPUT.md to render all results as Markdown tables.

The cache fingerprint includes input SHA-256, source ID, all parameters, software
version output, and this script's SHA-256. A cache mismatch fails unless --force
is explicitly supplied. A current input is always hashed before a cache hit.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import threading

import numpy as np

SCHEMA = 'gkm-targeted-av-current-measurement/1.0'
METHOD_VERSION = '2026-09-10-v1'
SR = 22050
NFFT = 2048
HOP = 512
_RUNTIME_LOCK = threading.Lock()
_RUNTIME_CACHE = {}
_NUMBER = r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?|[-+]?inf'


def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def run(command):
    result = subprocess.run([str(x) for x in command], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, check=False)
    if result.returncode:
        message = result.stderr.decode('utf-8', errors='replace')[-6000:]
        raise RuntimeError(f'Command failed ({result.returncode}): {command[0]}\n{message}')
    return result


def coefficient_of_variation(values):
    values = np.asarray(values, dtype=np.float64)
    return float(values.std(ddof=0) / values.mean()) if values.size and values.mean() > 1e-12 else None


def runtime_info(ffmpeg, ffprobe, music, skip_visual):
    key = (ffmpeg, ffprobe, bool(music), bool(skip_visual))
    with _RUNTIME_LOCK:
        if key in _RUNTIME_CACHE:
            return _RUNTIME_CACHE[key]
        info = {'python': sys.version, 'platform': platform.platform(),
                'numpy': np.__version__, 'ffmpeg_command': str(ffmpeg),
                'ffprobe_command': str(ffprobe),
                'ffmpeg_version': run([ffmpeg, '-version']).stdout.decode('utf-8', errors='replace').strip(),
                'ffprobe_version': run([ffprobe, '-version']).stdout.decode('utf-8', errors='replace').strip()}
        if not skip_visual:
            import cv2
            info['opencv'] = cv2.__version__
        if music:
            try:
                import librosa
                import scipy
            except ImportError as exc:
                raise RuntimeError('Music features require librosa and scipy in the selected Python environment.') from exc
            info.update(librosa=librosa.__version__, scipy=scipy.__version__)
        _RUNTIME_CACHE[key] = info
        return info


def select_input(path=None, directory=None):
    if (path is None) == (directory is None):
        raise ValueError('Specify exactly one explicit input file or an input directory.')
    if directory is not None:
        directory = Path(directory).expanduser().resolve(strict=True)
        extensions = {'.mp4', '.mkv', '.mov', '.webm', '.m4a', '.wav', '.flac', '.mp3', '.ogg'}
        candidates = sorted(p for p in directory.iterdir() if p.is_file() and p.suffix.lower() in extensions)
        if len(candidates) != 1:
            raise ValueError(f'Input directory requires exactly one media file; found {len(candidates)}: {directory}')
        path = candidates[0]
    path = Path(path).expanduser().resolve(strict=True)
    if not path.is_file():
        raise ValueError(f'Input is not a regular file: {path}')
    return path


def audio_filter(start, end):
    # Reset to decoded-audio origin before trim. The supplied game recordings have
    # zero-start audio; offsets in unusual files remain explicitly recorded by probe.
    chain = ['asetpts=PTS-STARTPTS']
    if start > 0 or end is not None:
        trim = f'atrim=start={start:.12g}'
        if end is not None:
            trim += f':end={end:.12g}'
        chain += [trim, 'asetpts=PTS-STARTPTS']
    return ','.join(chain)


def decode_audio(path, ffmpeg, start, end, threads):
    command = [ffmpeg, '-hide_banner', '-v', 'error', '-threads', str(threads), '-i', str(path),
               '-map', '0:a:0', '-vn', '-af', audio_filter(start, end), '-ac', '1', '-ar', str(SR),
               '-f', 'f32le', 'pipe:1']
    output = run(command)
    if len(output.stdout) % 4:
        raise ValueError('Decoded float32 audio byte count is not divisible by four.')
    samples = np.frombuffer(output.stdout, dtype='<f4')
    if len(samples) < NFFT:
        raise ValueError(f'Only {len(samples)} samples: interval is too short for FFT{NFFT}.')
    if not np.isfinite(samples).all():
        raise ValueError('Decoded PCM contains nonfinite values.')
    return samples, output.stderr.decode('utf-8', errors='replace')


def audio_features(samples, music=False):
    rms = []; centroid = []; flatness = []; flux = []
    previous = None
    window = np.hanning(NFFT + 1)[:-1]
    frequencies = np.fft.rfftfreq(NFFT, 1 / SR)
    for offset in range(0, max(0, len(samples) - NFFT + 1), HOP * 1024):
        block = samples[offset:min(len(samples), offset + HOP * 1024 + NFFT - HOP)]
        frames = np.lib.stride_tricks.sliding_window_view(block, NFFT)[::HOP].astype(np.float64)
        rms.extend(np.sqrt(np.mean(frames ** 2, axis=1)).tolist())
        magnitude = np.abs(np.fft.rfft(frames * window, axis=1)); power = magnitude ** 2
        centroid.extend((np.sum(magnitude * frequencies, axis=1) / np.maximum(magnitude.sum(axis=1), 1e-20)).tolist())
        flatness.extend((np.exp(np.mean(np.log(np.maximum(power, 1e-10)), axis=1)) / np.maximum(np.mean(power, axis=1), 1e-10)).tolist())
        normalized = magnitude / np.maximum(magnitude.sum(axis=1, keepdims=True), 1e-20)
        sequence = np.vstack([previous, normalized]) if previous is not None else normalized
        flux.extend(np.sqrt(np.sum(np.maximum(np.diff(sequence, axis=0), 0) ** 2, axis=1)).tolist())
        previous = normalized[-1]
    p10, p90 = (float(x) for x in np.percentile(rms, [10, 90], method='linear'))
    energy = 0.0
    for offset in range(0, len(samples), 1_048_576):
        block = samples[offset:offset + 1_048_576].astype(np.float64)
        energy += float(np.dot(block, block))
    result = {
        'sample_rate_hz': SR, 'audio_samples': len(samples),
        'analyzed_audio_duration_s': len(samples) / SR,
        'stft_frames': len(rms), 'flux_transitions': len(flux),
        'rms_linear': float(math.sqrt(energy / len(samples))),
        'rms_p10_linear': p10, 'rms_p90_linear': p90,
        'rms_p90_p10_db': float(20 * math.log10(max(p90, 1e-12) / max(p10, 1e-12))),
        'rms_p10_floor_applied': p10 < 1e-12,
        'rms_p10_near_zero': p10 < 1e-8,
        'rms_frames_below_1e_minus8': sum(x < 1e-8 for x in rms),
        'centroid_hz_mean': float(np.mean(centroid)),
        'flatness_mean': float(np.mean(flatness)),
        'positive_normalized_flux_mean': float(np.mean(flux)) if flux else None,
        'flux_cv': coefficient_of_variation(flux),
    }
    expected_frames = max(0, 1 + (len(samples) - NFFT) // HOP)
    if result['stft_frames'] != expected_frames or result['flux_transitions'] != expected_frames - 1:
        raise AssertionError('Audio window-count invariant failed.')
    if music:
        import librosa
        onset = librosa.onset.onset_strength(y=samples, sr=SR, hop_length=HOP, n_fft=NFFT,
                                              center=True, aggregate=np.mean)
        tempo, beats = librosa.beat.beat_track(onset_envelope=onset, sr=SR, hop_length=HOP,
                                              start_bpm=120, tightness=100, trim=True)
        local = librosa.feature.tempo(onset_envelope=onset, sr=SR, hop_length=HOP,
                                      start_bpm=120, std_bpm=1, ac_size=8, max_tempo=320, aggregate=None)
        chroma = librosa.feature.chroma_stft(y=samples, sr=SR, n_fft=NFFT, hop_length=HOP,
                                            tuning=0, norm=1, center=True)
        probabilities = chroma / np.maximum(chroma.sum(axis=0, keepdims=True), 1e-20)
        entropy = -np.sum(probabilities * np.log2(np.maximum(probabilities, 1e-20)), axis=0)
        tonnetz = librosa.feature.tonnetz(chroma=chroma, sr=SR)
        motion = np.linalg.norm(np.diff(tonnetz, axis=1), axis=0)
        result.update(tempo_bpm=float(np.asarray(tempo).ravel()[0]), beat_count=len(beats),
                      beat_interval_count=max(0, len(beats) - 1),
                      beat_interval_cv=coefficient_of_variation(np.diff(beats) * HOP / SR),
                      local_tempo_count=len(local), local_tempo_cv=coefficient_of_variation(local),
                      chroma_frames=chroma.shape[1], chroma_entropy_bits_mean=float(entropy.mean()),
                      tonnetz_transition_count=len(motion), tonnetz_motion_mean=float(motion.mean()))
    return result


def loudness_features(path, ffmpeg, start, end, threads):
    filters = audio_filter(start, end) + ',ebur128=peak=true,silencedetect=noise=-50dB:d=0.5'
    command = [ffmpeg, '-hide_banner', '-nostats', '-threads', str(threads), '-i', str(path),
               '-map', '0:a:0', '-vn', '-af', filters, '-f', 'null', '-']
    stderr = run(command).stderr.decode('utf-8', errors='replace')
    position = stderr.rfind('Summary:')
    if position < 0:
        raise ValueError('FFmpeg returned no EBU R128 summary.')
    summary = stderr[position:]
    def value(pattern):
        match = re.search(pattern, summary)
        if not match: raise ValueError(f'EBU R128 summary field absent: {pattern}')
        parsed = float(match.group(1))
        return parsed if math.isfinite(parsed) else ('-inf' if parsed < 0 else 'inf')
    intervals = []; opened = None
    for line in stderr.splitlines():
        match = re.search(r'silence_start:\s*(' + _NUMBER + r')', line)
        if match:
            if opened is not None: raise ValueError('Nested silence starts in FFmpeg output.')
            opened = float(match.group(1))
        match = re.search(r'silence_end:\s*(' + _NUMBER + r')', line)
        if match and opened is not None:
            closed = float(match.group(1))
            duration = re.search(r'silence_duration:\s*(' + _NUMBER + r')', line)
            intervals.append({'start_s': opened, 'end_s': closed, 'duration_s': closed - opened,
                              'ffmpeg_reported_duration_s': float(duration.group(1)) if duration else None})
            opened = None
    return {'integrated_lufs': value(r'LOCAL_DRIVE_I\s+(' + _NUMBER + r') LUFS'),
            'lra_lu': value(r'LRA:\s+(' + _NUMBER + r') LU'),
            'true_peak_dbfs': value(r'Peak:\s+(' + _NUMBER + r') dBFS'),
            'silence_intervals_s': intervals,
            'silence_seconds': sum(x['duration_s'] for x in intervals),
            'unclosed_silence_start_s': opened,
            'ebur128_summary': summary.strip(),
            'ffmpeg_stderr_sha256': hashlib.sha256(stderr.encode('utf-8')).hexdigest(),
            'time_origin': 'segment-local decoded audio origin; add requested start_s for source-relative locator'}


def visual_features(path, start, end, step, probe):
    import cv2
    moving = [x for x in probe['streams'] if x.get('codec_type') == 'video'
              and not x.get('disposition', {}).get('attached_pic')]
    if not moving:
        return {'status': 'not_applicable', 'reason': 'No moving video stream; attached pictures are excluded.'}
    if len(moving) != 1 or moving[0]['index'] != 0:
        raise ValueError('Visual sampling requires one moving video at stream index0; ambiguous stream selection is rejected.')
    capture = cv2.VideoCapture(str(path), cv2.CAP_FFMPEG)
    if not capture.isOpened(): raise ValueError('OpenCV could not open the moving-video source.')
    rows = []; omitted = []; previous = None; previous_histogram = None; previous_time = None
    scheduled = np.arange(start, end, step)
    try:
        for timestamp in scheduled:
            seek_ok = capture.set(cv2.CAP_PROP_POS_MSEC, float(timestamp) * 1000)
            ok, frame = capture.read()
            if not ok:
                omitted.append({'requested_time_s': float(timestamp), 'seek_returned': bool(seek_ok), 'reason': 'read_failed'})
                continue
            frame = cv2.resize(frame, (160, 90), interpolation=cv2.INTER_AREA)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            histogram = cv2.calcHist([frame], [0, 1, 2], None, [8, 8, 8], [0, 256] * 3)
            histogram = cv2.normalize(histogram, histogram, alpha=1, norm_type=cv2.NORM_L1)
            difference = float(np.abs(gray - previous).mean()) if previous is not None else None
            distance = float(cv2.compareHist(previous_histogram, histogram, cv2.HISTCMP_BHATTACHARYYA)) if previous_histogram is not None else None
            rows.append({'requested_time_s': float(timestamp), 'reported_time_s': capture.get(cv2.CAP_PROP_POS_MSEC) / 1000,
                         'brightness': float(gray.mean()), 'saturation': float(hsv[:, :, 1].mean() / 255),
                         'frame_difference': difference, 'histogram_distance': distance,
                         'elapsed_from_previous_sample_s': float(timestamp) - previous_time if previous_time is not None else None})
            previous = gray; previous_histogram = histogram; previous_time = float(timestamp)
    finally:
        capture.release()
    return {'status': 'measured', 'sample_step_s': step, 'sample_width': 160, 'sample_height': 90,
            'scheduled_samples': len(scheduled), 'samples': len(rows), 'omitted_reads': omitted,
            'brightness_mean': float(np.mean([x['brightness'] for x in rows])) if rows else None,
            'saturation_mean': float(np.mean([x['saturation'] for x in rows])) if rows else None,
            'frame_difference_mean': float(np.mean([x['frame_difference'] for x in rows[1:]])) if len(rows) > 1 else None,
            'histogram_jumps_gt_0_5': sum(x['histogram_distance'] > 0.5 for x in rows[1:]), 'rows': rows}


def parameters(spec):
    return {'method_version': METHOD_VERSION, 'audio_sr_hz': SR, 'nfft': NFFT, 'hop': HOP,
            'fft_window': 'periodic Hann', 'custom_spectral_center': False, 'rms_percentile_method': 'linear',
            'rms_floor': 1e-12, 'flatness_power_floor': 1e-10, 'cv_ddof': 0,
            'audio_stream': 'first (0:a:0)', 'audio_signal': 'full unseparated mix, mono for features; native channels for R128',
            'trim_order': 'decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim',
            'loudness_filter': 'ebur128=peak=true', 'silence_filter': 'silencedetect=noise=-50dB:d=0.5',
            'start_s': spec['start_s'], 'end_s': spec['end_s'], 'music': spec['music'],
            'visual_step_s': spec['visual_step_s'], 'skip_visual': spec['skip_visual'],
            'visual_size': [160, 90], 'visual_resize': 'INTER_AREA, whole frame with aspect distortion',
            'visual_grayscale': 'OpenCV BGR2GRAY /255', 'visual_saturation': 'OpenCV HSV S/255',
            'histogram': '8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5',
            'ffmpeg_threads': spec.get('threads', 1),
            'music_parameters': {'onset': 'librosa onset_strength; center=True; aggregate=mean',
                                 'beat': 'start_bpm120, tightness100, trim=True',
                                 'local_tempo': 'start_bpm120,std_bpm1,ac_size8,max_tempo320,aggregate=None',
                                 'chroma': 'chroma_stft,tuning0,norm1,center=True',
                                 'tonnetz': '6D coordinates from chroma_stft, adjacent Euclidean distance'} if spec['music'] else None}


def atomic_json(path, value):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=path.parent, prefix='.measure-', suffix='.json', delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None and temporary.exists(): temporary.unlink()


def measure(spec, output, ffmpeg='ffmpeg', ffprobe='ffprobe', force=False):
    spec = dict(spec)
    path = select_input(spec.get('path'), spec.get('input_dir'))
    expected = spec.get('sha256', '').lower()
    if not re.fullmatch('[0-9a-f]{64}', expected): raise ValueError('A complete expected input SHA-256 is required.')
    if not spec.get('source_id'): raise ValueError('A recorded source ID is required.')
    spec['start_s'] = float(spec.get('start_s', 0))
    spec['end_s'] = float(spec['end_s']) if spec.get('end_s') is not None else None
    spec['visual_step_s'] = float(spec.get('visual_step_s', 5))
    spec['music'] = bool(spec.get('music', False)); spec['skip_visual'] = bool(spec.get('skip_visual', False))
    if not math.isfinite(spec['start_s']) or spec['start_s'] < 0: raise ValueError('start_s must be finite and nonnegative.')
    if spec['end_s'] is not None and (not math.isfinite(spec['end_s']) or spec['end_s'] <= spec['start_s']): raise ValueError('end_s must be finite and greater than start_s.')
    if not math.isfinite(spec['visual_step_s']) or spec['visual_step_s'] <= 0: raise ValueError('visual_step_s must be positive.')
    actual = sha256_file(path)
    if actual != expected: raise ValueError(f'Input hash mismatch for {path.name}: expected {expected}, observed {actual}')
    output = Path(output).expanduser().resolve()
    if output == path or output.suffix.lower() != '.json': raise ValueError('Output must be a separate .json working file.')
    output.parent.mkdir(parents=True, exist_ok=True)
    runtime = runtime_info(ffmpeg, ffprobe, spec['music'], spec['skip_visual'])
    method = parameters(spec)
    identity = {'schema': SCHEMA, 'input_sha256': actual, 'source_id': spec['source_id'],
                'character': spec.get('character'), 'alias': spec.get('alias'), 'label': spec.get('label'),
                'boundary_note': spec.get('boundary_note'), 'parameters': method, 'software': runtime,
                'script_sha256': sha256_file(Path(__file__).resolve())}
    fingerprint = hashlib.sha256(json.dumps(identity, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()
    if output.exists():
        old = json.loads(output.read_text(encoding='utf-8'))
        if old.get('processing_fingerprint') == fingerprint:
            print(json.dumps({'status': 'cache_hit_hash_checked', 'output': str(output), 'sha256': actual}), flush=True)
            return old
        if not force: raise ValueError(f'Cache input/method/runtime mismatch: {output}. Use a new path or explicit --force.')
    lock = output.with_suffix(output.suffix + '.lock')
    lock_fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.close(lock_fd)
    try:
        probe = json.loads(run([ffprobe, '-v', 'error', '-show_format', '-show_streams', '-show_chapters', '-of', 'json', str(path)]).stdout)
        audio_streams = [x for x in probe.get('streams', []) if x.get('codec_type') == 'audio']
        if not audio_streams: raise ValueError('No audio stream.')
        duration = float(probe['format']['duration'])
        if spec['start_s'] >= duration or (spec['end_s'] is not None and spec['end_s'] > duration + 1e-6): raise ValueError('Requested interval exceeds container duration.')
        actual_end = spec['end_s'] if spec['end_s'] is not None else duration
        begun = datetime.now(timezone.utc).isoformat()
        samples, decode_notes = decode_audio(path, ffmpeg, spec['start_s'], spec['end_s'], spec.get('threads', 1))
        features = audio_features(samples, spec['music'])
        del samples
        loudness = loudness_features(path, ffmpeg, spec['start_s'], spec['end_s'], spec.get('threads', 1))
        visual = {'status': 'not_run', 'reason': 'Explicit skip_visual parameter'} if spec['skip_visual'] else visual_features(path, spec['start_s'], actual_end, spec['visual_step_s'], probe)
        if sha256_file(path) != actual: raise ValueError('Input bytes changed during measurement; output not committed.')
        result = {'schema': SCHEMA, 'generation': 'current_execution', 'processing_fingerprint': fingerprint,
                  'processing_identity': identity, 'started_utc': begun, 'completed_utc': datetime.now(timezone.utc).isoformat(),
                  'source_id': spec['source_id'], 'character': spec.get('character'), 'alias': spec.get('alias'),
                  'label': spec.get('label', 'whole source' if spec['start_s'] == 0 and spec['end_s'] is None else 'bounded interval'),
                  'input_path': str(path), 'filename': path.name, 'size_bytes': path.stat().st_size, 'sha256': actual,
                  'start_s': spec['start_s'], 'end_s': actual_end, 'duration_s': actual_end - spec['start_s'],
                  'boundary_note': spec.get('boundary_note', 'Whole container' if spec['start_s'] == 0 and spec['end_s'] is None else 'Explicit caller interval; chapter/content identity not verified by this processor'),
                  'probe': probe, 'audio_metrics': features, 'loudness': loudness, 'visual': visual,
                  'decode_warnings': decode_notes, 'direct_listening': False, 'direct_visual_inspection': False,
                  'interpretation_limit': 'Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows.'}
        atomic_json(output, result)
        print(json.dumps({'status': 'measured', 'output': str(output), 'source_id': spec['source_id'], 'seconds': result['duration_s']}), flush=True)
        return result
    finally:
        lock.unlink(missing_ok=True)


def flatten(value, prefix=''):
    if isinstance(value, dict):
        for key, child in value.items(): yield from flatten(child, f'{prefix}.{key}' if prefix else str(key))
    elif isinstance(value, list):
        if not value: yield prefix, '[]'
        for index, child in enumerate(value): yield from flatten(child, f'{prefix}[{index}]')
    else: yield prefix, value


def cell(value):
    if value is None: return 'N/A'
    if isinstance(value, bool): return 'true' if value else 'false'
    text = format(value, '.15g') if isinstance(value, float) else str(value)
    return text.replace('&', '&amp;').replace('|', '\\|').replace('\r', '').replace('\n', '<br>')


def markdown_table(headers, rows):
    lines = ['| ' + ' | '.join(cell(x) for x in headers) + ' |', '| ' + ' | '.join('---' for _ in headers) + ' |']
    lines += ['| ' + ' | '.join(cell(x) for x in row) + ' |' for row in rows]
    return '\n'.join(lines) + '\n'


def render_markdown(results, path):
    lines = ['# Current execution mixed-source measurement record', '',
             'New automated technical processing; no direct listening or visual interpretation is asserted. Source and chapter identities require the separately recorded acquisition and content review. Numerical values retain 15 significant digits; this is computational precision, not measurement accuracy.', '',
             'The custom spectral/RMS definitions follow the supplied independently specified estimator family. Runtime versions, hash-bound inputs, and exact operational intervals are recorded below. Whole-source and interval results are separate observations; segments can contain several speakers, BGM, effects and silence.', '']
    overview = []
    for result in results:
        a = result['audio_metrics']; l = result['loudness']; v = result['visual']
        overview.append([result.get('alias'), result['label'], result['start_s'], result['end_s'], result['duration_s'],
                         l['integrated_lufs'], l['lra_lu'], l['true_peak_dbfs'], a['rms_p90_p10_db'], a['centroid_hz_mean'], v.get('samples')])
    lines += [markdown_table(['Alias', 'Interval label', 'Start s inclusive', 'End s exclusive', 'Duration s', 'I LUFS', 'LRA LU', 'True peak dBFS', 'RMS P90/P10 dB', 'Centroid Hz', 'Visual n'], overview)]
    for index, result in enumerate(results, 1):
        lines += [f'## Record {index:02} — {result.get("alias") or result["source_id"]}: {result["label"]}', '']
        metadata = {k: v for k, v in result.items() if k not in {'probe', 'processing_identity', 'audio_metrics', 'loudness', 'visual'}}
        lines += [markdown_table(['Record field', 'Value'], list(flatten(metadata))), '',
                  '### Processing identity and parameters', '',
                  markdown_table(['Parameter', 'Value'], list(flatten(result['processing_identity']))), '',
                  '### Source probe', '', markdown_table(['Probe field', 'Value'], list(flatten(result['probe']))), '',
                  '### Audio features', '', markdown_table(['Audio feature', 'Value'], list(result['audio_metrics'].items())), '',
                  '### Loudness and low-level intervals', '']
        loudness = {k:v for k,v in result['loudness'].items() if k != 'silence_intervals_s'}
        lines += [markdown_table(['Loudness field', 'Value'], list(loudness.items())), '',
                  markdown_table(['Segment-local start s', 'End s', 'Computed duration s', 'FFmpeg reported duration s'],
                                 [[row[k] for k in ('start_s', 'end_s', 'duration_s', 'ffmpeg_reported_duration_s')] for row in result['loudness']['silence_intervals_s']]), '',
                  '### Sampled visual output', '']
        v = result['visual']; summary = {k:val for k,val in v.items() if k not in {'rows','omitted_reads'}}
        lines += [markdown_table(['Visual field', 'Value'], list(summary.items())), '']
        if v.get('omitted_reads'):
            lines += [markdown_table(['Omission field', 'Value'], list(flatten(v['omitted_reads']))), '']
        if v.get('rows'):
            lines += [markdown_table(['Requested source s', 'Decoder reported s', 'Luma', 'Saturation', 'Difference from prior successful sample', 'Histogram distance', 'Elapsed from prior sample s'],
                                     [[row[k] for k in ('requested_time_s', 'reported_time_s', 'brightness', 'saturation', 'frame_difference', 'histogram_distance', 'elapsed_from_previous_sample_s')] for row in v['rows']]), '']
    path = Path(path).expanduser().resolve()
    if path.suffix.lower() != '.md': raise ValueError('Markdown rendering requires a .md destination.')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--input', type=Path); group.add_argument('--input-dir', type=Path); group.add_argument('--specs', type=Path)
    parser.add_argument('--source-id'); parser.add_argument('--expected-sha256'); parser.add_argument('--character'); parser.add_argument('--alias'); parser.add_argument('--label')
    parser.add_argument('--start', type=float, default=0); parser.add_argument('--end', type=float); parser.add_argument('--boundary-note')
    parser.add_argument('--music', action='store_true'); parser.add_argument('--skip-visual', action='store_true'); parser.add_argument('--visual-step', type=float, default=5)
    parser.add_argument('--output', type=Path); parser.add_argument('--output-dir', type=Path); parser.add_argument('--markdown', type=Path)
    parser.add_argument('--ffmpeg', default='ffmpeg'); parser.add_argument('--ffprobe', default='ffprobe'); parser.add_argument('--force', action='store_true'); parser.add_argument('--workers', type=int, default=1)
    args = parser.parse_args()
    if args.workers < 1 or args.workers > 8: parser.error('--workers must be between1 and8.')
    if args.specs:
        if not args.output_dir: parser.error('--specs requires --output-dir.')
        specs = json.loads(args.specs.read_text(encoding='utf-8-sig'))
        if not isinstance(specs, list) or not specs: parser.error('--specs must contain a nonempty JSON list.')
        jobs = []
        for number, spec in enumerate(specs):
            name = re.sub(r'[^A-Za-z0-9_.-]+', '_', f'{number+1:03}_{spec.get("character","")}_{spec.get("alias") or spec.get("source_id", "input")}_{spec.get("label", "measurement")}')
            jobs.append((spec, args.output_dir / f'{name}.json'))
        results = [None] * len(jobs)
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(measure, spec, output, args.ffmpeg, args.ffprobe, args.force): index for index, (spec, output) in enumerate(jobs)}
            for future in as_completed(futures): results[futures[future]] = future.result()
    else:
        if not args.output: parser.error('Single input requires --output.')
        spec = {'path': str(args.input) if args.input else None, 'input_dir': str(args.input_dir) if args.input_dir else None,
                'source_id': args.source_id, 'sha256': args.expected_sha256, 'character': args.character, 'alias': args.alias,
                'start_s': args.start, 'end_s': args.end, 'music': args.music, 'skip_visual': args.skip_visual,
                'visual_step_s': args.visual_step}
        if args.label: spec['label'] = args.label
        if args.boundary_note: spec['boundary_note'] = args.boundary_note
        results = [measure(spec, args.output, args.ffmpeg, args.ffprobe, args.force)]
    if args.markdown: render_markdown(results, args.markdown)


if __name__ == '__main__':
    main()
```

## Complete current result values

# Detailed records

New automated technical processing; no direct listening or visual interpretation is asserted. Source and chapter identities require the separately recorded acquisition and content review. Numerical values retain 15 significant digits; this is computational precision, not measurement accuracy.

The custom spectral/RMS definitions follow the supplied independently specified estimator family. Runtime versions, hash-bound inputs, and exact operational intervals are recorded below. Whole-source and interval results are separate observations; segments can contain several speakers, BGM, effects and silence.

| Alias | Interval label | Start s inclusive | End s exclusive | Duration s | I LUFS | LRA LU | True peak dBFS | RMS P90/P10 dB | Centroid Hz | Visual n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H04_ORIGINAL | full_original_source | 0 | 3516.615692 | 3516.615692 | -20.7 | 10.1 | -4.9 | 25.9478152667697 | 2083.80577195724 | 704 |
| H03 | whole_source_reproduction_check | 0 | 2687.454331 | 2687.454331 | -22.6 | 8 | -8.1 | 25.1885860688991 | 2081.88901658777 | 538 |
| H12 | whole_song_reproduction_check | 0 | 175.264218 | 175.264218 | -14.3 | 9.5 | -0.4 | 33.6979113992567 | 2077.69079737181 | 36 |
| H15 | whole_song_reproduction_check | 0 | 200.782948 | 200.782948 | -12.9 | 13.9 | 0.2 | 30.124918093061 | 2085.16715298758 | 41 |
| H17 | whole_song_reproduction_check | 0 | 183.275102 | 183.275102 | -12.2 | 3.2 | -0.1 | 7.51134694842469 | 2379.63773127389 | 37 |
| H19 | whole_song_reproduction_check | 0 | 160.728526 | 160.728526 | -12.4 | 3 | -0 | 10.9453120908471 | 2655.47495901444 | 33 |
| H20 | whole_song_reproduction_check | 0 | 155.178957 | 155.178957 | -20.3 | 5.8 | -6.3 | 8.64234414965983 | 2354.76419184442 | 32 |
| H21 | whole_song_reproduction_check | 0 | 110.225125 | 110.225125 | -13.5 | 6.6 | -0 | 35.2961981571966 | 2575.71005638518 | 23 |
| H22 | whole_song_reproduction_check | 0 | 110.457324 | 110.457324 | -14.1 | 5.1 | 0.1 | 30.9498908615111 | 2349.37192778531 | 23 |
| H23 | whole_song_reproduction_check | 0 | 116.657052 | 116.657052 | -13.3 | 5.2 | 0 | 211.058496695705 | 3029.11715119712 | 24 |
| H25 | whole_song_reproduction_check | 0 | 109.435646 | 109.435646 | -11.6 | 2.2 | -0.2 | 66.6029070755097 | 2618.43000955922 | 22 |

## Record 01 — H04_ORIGINAL: full_original_source

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 5952bf3f0c8c06053192ed89e2ac7d7cc1f074dd309a1f6a65bd24332fd961fe |
| started_utc | 2026-09-10T06:14:15.184658+00:00 |
| completed_utc | 2026-09-10T06:15:42.809581+00:00 |
| source_id | 1Toi0yHcoq0jV0GMcA4JalcrlLMbnFxQO |
| character | HIRO |
| alias | H04_ORIGINAL |
| label | full_original_source |
| input_path | LOCAL_USER/Downloads\【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】-(720p60).mp4 |
| filename | 【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】-(720p60).mp4 |
| size_bytes | 545587232 |
| sha256 | 4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468 |
| start_s | 0 |
| end_s | 3516.615692 |
| duration_s | 3516.615692 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468 |
| source_id | 1Toi0yHcoq0jV0GMcA4JalcrlLMbnFxQO |
| character | HIRO |
| alias | H04_ORIGINAL |
| label | full_original_source |
| boundary_note | N/A |
| parameters.method_version | 2026-09-10-v1 |
| parameters.audio_sr_hz | 22050 |
| parameters.nfft | 2048 |
| parameters.hop | 512 |
| parameters.fft_window | periodic Hann |
| parameters.custom_spectral_center | false |
| parameters.rms_percentile_method | linear |
| parameters.rms_floor | 1e-12 |
| parameters.flatness_power_floor | 1e-10 |
| parameters.cv_ddof | 0 |
| parameters.audio_stream | first (0:a:0) |
| parameters.audio_signal | full unseparated mix, mono for features; native channels for R128 |
| parameters.trim_order | decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim |
| parameters.loudness_filter | ebur128=peak=true |
| parameters.silence_filter | silencedetect=noise=-50dB:d=0.5 |
| parameters.start_s | 0 |
| parameters.end_s | N/A |
| parameters.music | false |
| parameters.visual_step_s | 5 |
| parameters.skip_visual | false |
| parameters.visual_size[0] | 160 |
| parameters.visual_size[1] | 90 |
| parameters.visual_resize | INTER_AREA, whole frame with aspect distortion |
| parameters.visual_grayscale | OpenCV BGR2GRAY /255 |
| parameters.visual_saturation | OpenCV HSV S/255 |
| parameters.histogram | 8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5 |
| parameters.ffmpeg_threads | 1 |
| parameters.music_parameters | N/A |
| software.python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| software.platform | Windows-11-10.0.26200-SP0 |
| software.numpy | 2.1.2 |
| software.ffmpeg_command | ffmpeg |
| software.ffprobe_command | ffprobe |
| software.ffmpeg_version | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101<br><br>Exiting with exit code 0 |
| software.ffprobe_version | ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101 |
| software.opencv | 4.13.0 |
| script_sha256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


### Source probe

| Probe field | Value |
| --- | --- |
| streams[0].index | 0 |
| streams[0].codec_name | h264 |
| streams[0].codec_long_name | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 |
| streams[0].profile | High |
| streams[0].codec_type | video |
| streams[0].codec_tag_string | avc1 |
| streams[0].codec_tag | 0x31637661 |
| streams[0].mime_codec_string | avc1.640020 |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
| streams[0].pix_fmt | yuv420p |
| streams[0].level | 32 |
| streams[0].color_range | tv |
| streams[0].color_space | bt709 |
| streams[0].color_transfer | bt709 |
| streams[0].color_primaries | bt709 |
| streams[0].chroma_location | left |
| streams[0].field_order | progressive |
| streams[0].is_avc | true |
| streams[0].nal_length_size | 4 |
| streams[0].id | 0x1 |
| streams[0].r_frame_rate | 60000/1001 |
| streams[0].avg_frame_rate | 60000/1001 |
| streams[0].time_base | 1/60000 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 210992782 |
| streams[0].duration | 3516.546367 |
| streams[0].bit_rate | 1098603 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 210782 |
| streams[0].extradata_size | 42 |
| streams[0].disposition.default | 1 |
| streams[0].disposition.dub | 0 |
| streams[0].disposition.original | 0 |
| streams[0].disposition.comment | 0 |
| streams[0].disposition.lyrics | 0 |
| streams[0].disposition.karaoke | 0 |
| streams[0].disposition.forced | 0 |
| streams[0].disposition.hearing_impaired | 0 |
| streams[0].disposition.visual_impaired | 0 |
| streams[0].disposition.clean_effects | 0 |
| streams[0].disposition.attached_pic | 0 |
| streams[0].disposition.timed_thumbnails | 0 |
| streams[0].disposition.non_diegetic | 0 |
| streams[0].disposition.captions | 0 |
| streams[0].disposition.descriptions | 0 |
| streams[0].disposition.metadata | 0 |
| streams[0].disposition.dependent | 0 |
| streams[0].disposition.still_image | 0 |
| streams[0].disposition.multilayer | 0 |
| streams[0].tags.language | und |
| streams[0].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[1].index | 1 |
| streams[1].codec_name | aac |
| streams[1].codec_long_name | AAC (Advanced Audio Coding) |
| streams[1].profile | LC |
| streams[1].codec_type | audio |
| streams[1].codec_tag_string | mp4a |
| streams[1].codec_tag | 0x6134706d |
| streams[1].mime_codec_string | mp4a.40.2 |
| streams[1].sample_fmt | fltp |
| streams[1].sample_rate | 44100 |
| streams[1].channels | 2 |
| streams[1].channel_layout | stereo |
| streams[1].bits_per_sample | 0 |
| streams[1].initial_padding | 0 |
| streams[1].id | 0x2 |
| streams[1].r_frame_rate | 0/0 |
| streams[1].avg_frame_rate | 0/0 |
| streams[1].time_base | 1/44100 |
| streams[1].start_pts | 0 |
| streams[1].start_time | 0.000000 |
| streams[1].duration_ts | 155082752 |
| streams[1].duration | 3516.615692 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 151448 |
| streams[1].extradata_size | 16 |
| streams[1].disposition.default | 1 |
| streams[1].disposition.dub | 0 |
| streams[1].disposition.original | 0 |
| streams[1].disposition.comment | 0 |
| streams[1].disposition.lyrics | 0 |
| streams[1].disposition.karaoke | 0 |
| streams[1].disposition.forced | 0 |
| streams[1].disposition.hearing_impaired | 0 |
| streams[1].disposition.visual_impaired | 0 |
| streams[1].disposition.clean_effects | 0 |
| streams[1].disposition.attached_pic | 0 |
| streams[1].disposition.timed_thumbnails | 0 |
| streams[1].disposition.non_diegetic | 0 |
| streams[1].disposition.captions | 0 |
| streams[1].disposition.descriptions | 0 |
| streams[1].disposition.metadata | 0 |
| streams[1].disposition.dependent | 0 |
| streams[1].disposition.still_image | 0 |
| streams[1].disposition.multilayer | 0 |
| streams[1].tags.language | jpn |
| streams[1].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[2].index | 2 |
| streams[2].codec_name | png |
| streams[2].codec_long_name | PNG (Portable Network Graphics) image |
| streams[2].codec_type | video |
| streams[2].codec_tag_string | [0][0][0][0] |
| streams[2].codec_tag | 0x0000 |
| streams[2].width | 1280 |
| streams[2].height | 720 |
| streams[2].coded_width | 1280 |
| streams[2].coded_height | 720 |
| streams[2].has_b_frames | 0 |
| streams[2].pix_fmt | rgb24 |
| streams[2].level | -99 |
| streams[2].color_range | pc |
| streams[2].color_space | gbr |
| streams[2].id | 0x0 |
| streams[2].r_frame_rate | 90000/1 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/90000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 316495412 |
| streams[2].duration | 3516.615689 |
| streams[2].disposition.default | 0 |
| streams[2].disposition.dub | 0 |
| streams[2].disposition.original | 0 |
| streams[2].disposition.comment | 0 |
| streams[2].disposition.lyrics | 0 |
| streams[2].disposition.karaoke | 0 |
| streams[2].disposition.forced | 0 |
| streams[2].disposition.hearing_impaired | 0 |
| streams[2].disposition.visual_impaired | 0 |
| streams[2].disposition.clean_effects | 0 |
| streams[2].disposition.attached_pic | 1 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| chapters | [] |
| format.filename | LOCAL_USER/Downloads\【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】-(720p60).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 3516.615692 |
| format.size | 545587232 |
| format.bit_rate | 1241164 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】 |
| format.tags.artist | 学Pといっしょ |
| format.tags.genre | Gaming |
| format.tags.date | 20260526 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=F4QAgB54B-g |
| format.tags.description | 【注意】この動画には「学園アイドルマスター」のネタバレを含みます。<br><br><br>▼学マス 好評配信中！▼<br>http://app.adjust.com/1ai6ouao<br><br>学マス公式サイト<br>https://gakuen.idolmaster-official.jp/<br>学マス公式X(Twitter)<br>https://x.com/gkmas_official<br><br><br>#学マス<br>#篠澤広 |
| format.tags.synopsis | 【注意】この動画には「学園アイドルマスター」のネタバレを含みます。<br><br><br>▼学マス 好評配信中！▼<br>http://app.adjust.com/1ai6ouao<br><br>学マス公式サイト<br>https://gakuen.idolmaster-official.jp/<br>学マス公式X(Twitter)<br>https://x.com/gkmas_official<br><br><br>#学マス<br>#篠澤広 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 77541376 |
| analyzed_audio_duration_s | 3516.61569160998 |
| stft_frames | 151445 |
| flux_transitions | 151444 |
| rms_linear | 0.0731229311224287 |
| rms_p10_linear | 0.00655535116040359 |
| rms_p90_linear | 0.130012983508813 |
| rms_p90_p10_db | 25.9478152667697 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 4948 |
| centroid_hz_mean | 2083.80577195724 |
| flatness_mean | 0.0615282978092988 |
| positive_normalized_flux_mean | 0.0345938613645265 |
| flux_cv | 0.666380599572715 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -20.7 |
| lra_lu | 10.1 |
| true_peak_dbfs | -4.9 |
| silence_seconds | 164.752725 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -20.7 LUFS<br>    Threshold: -32.3 LUFS<br><br>  Loudness range:<br>    LRA:        10.1 LU<br>    Threshold: -42.4 LUFS<br>    LRA low:   -28.1 LUFS<br>    LRA high:  -18.0 LUFS<br><br>  True peak:<br>    Peak:       -4.9 dBFS<br>[out#0/null @ 000001e4f21a8380] video:0KiB audio:605792KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:58:36.61 bitrate=N/A speed= 149x elapsed=0:00:23.55 |
| ffmpeg_stderr_sha256 | e86c4b6219eab73cfbdbdaeb61c38a6f14467b8bec42af9de4fbb9f84fe118d2 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 33.712676 | 35.229161 | 1.516485 | 1.516485 |
| 40.132472 | 41.267506 | 1.135034 | 1.135034 |
| 44.915442 | 45.648639 | 0.733197000000004 | 0.733197 |
| 55.172109 | 56.362449 | 1.19034 | 1.19034 |
| 58.990295 | 59.795578 | 0.805282999999996 | 0.805283 |
| 71.117982 | 71.719116 | 0.601134000000002 | 0.601134 |
| 72.91941 | 73.656259 | 0.736849000000007 | 0.736848 |
| 74.694172 | 75.260952 | 0.566780000000008 | 0.56678 |
| 76.816644 | 77.612585 | 0.795940999999999 | 0.795941 |
| 80.204354 | 80.871383 | 0.667028999999999 | 0.667029 |
| 187.065669 | 187.667052 | 0.601382999999998 | 0.601383 |
| 188.317619 | 189.546168 | 1.22854899999999 | 1.228549 |
| 190.318322 | 190.931293 | 0.612971000000016 | 0.612971 |
| 192.432426 | 193.572925 | 1.14049900000001 | 1.140499 |
| 194.041678 | 195.023741 | 0.982063000000011 | 0.982063 |
| 195.925714 | 196.732086 | 0.80637200000001 | 0.806372 |
| 258.562063 | 260.77678 | 2.21471699999995 | 2.214717 |
| 262.965351 | 263.62585 | 0.660499000000016 | 0.660499 |
| 267.146236 | 269.224966 | 2.07873000000001 | 2.07873 |
| 304.904875 | 305.605238 | 0.700362999999982 | 0.700363 |
| 308.450862 | 309.023651 | 0.572789 | 0.572789 |
| 346.054014 | 346.693855 | 0.63984099999999 | 0.639841 |
| 347.231746 | 348.154717 | 0.922971000000018 | 0.922971 |
| 349.286712 | 349.94517 | 0.658457999999996 | 0.658458 |
| 369.925805 | 370.665488 | 0.739682999999957 | 0.739683 |
| 372.020317 | 373.384286 | 1.363969 | 1.363968 |
| 374.187256 | 375.459433 | 1.272177 | 1.272177 |
| 375.847324 | 377.093469 | 1.24614500000001 | 1.246145 |
| 377.525238 | 378.310907 | 0.785668999999984 | 0.785669 |
| 425.303605 | 426.198163 | 0.894558000000018 | 0.894558 |
| 428.99229 | 429.643628 | 0.651337999999953 | 0.651338 |
| 429.887687 | 430.496689 | 0.609001999999975 | 0.609002 |
| 431.448753 | 432.087438 | 0.638685000000009 | 0.638685 |
| 433.62551 | 434.223333 | 0.597823000000005 | 0.597823 |
| 524.033311 | 525.681655 | 1.64834399999995 | 1.648345 |
| 526.987052 | 527.602426 | 0.615374000000088 | 0.615374 |
| 528.363288 | 529.312132 | 0.948844000000008 | 0.948844 |
| 530.226803 | 530.866621 | 0.639817999999991 | 0.639819 |
| 531.827098 | 533.021814 | 1.19471599999997 | 1.194717 |
| 535.234263 | 535.853946 | 0.619682999999895 | 0.619683 |
| 537.734286 | 538.520567 | 0.786281000000031 | 0.786281 |
| 685.669002 | 686.247959 | 0.578957000000059 | 0.578957 |
| 688.053696 | 689.428322 | 1.37462600000003 | 1.374626 |
| 712.843469 | 715.080181 | 2.23671200000001 | 2.236712 |
| 719.467551 | 720.299569 | 0.832018000000062 | 0.832018 |
| 797.196304 | 797.920794 | 0.724489999999946 | 0.72449 |
| 798.580454 | 799.842472 | 1.26201800000001 | 1.262018 |
| 800.821927 | 801.628617 | 0.806690000000003 | 0.806689 |
| 802.600975 | 803.434399 | 0.833424000000036 | 0.833424 |
| 804.344444 | 805.186916 | 0.842472000000043 | 0.842472 |
| 808.15 | 808.678617 | 0.528617000000054 | 0.528617 |
| 851.391655 | 852.054263 | 0.662607999999977 | 0.662608 |
| 852.750975 | 854.078957 | 1.32798199999991 | 1.327982 |
| 856.17712 | 857.153719 | 0.976599000000078 | 0.976599 |
| 858.4878 | 859.165828 | 0.67802800000004 | 0.678027 |
| 859.398118 | 859.975646 | 0.577528000000029 | 0.577528 |
| 860.371043 | 861.410023 | 1.03898000000004 | 1.03898 |
| 965.532789 | 966.041179 | 0.508390000000077 | 0.50839 |
| 969.272902 | 969.870544 | 0.597641999999951 | 0.597642 |
| 972.212721 | 973.014603 | 0.801881999999978 | 0.801882 |
| 973.408345 | 974.611746 | 1.20340099999999 | 1.203401 |
| 1013.538254 | 1014.217166 | 0.678911999999968 | 0.678912 |
| 1017.723333 | 1019.008005 | 1.284672 | 1.284671 |
| 1076.553333 | 1078.337846 | 1.78451299999983 | 1.784512 |
| 1078.795329 | 1079.446372 | 0.651043000000072 | 0.651043 |
| 1169.679342 | 1170.89941 | 1.22006800000008 | 1.220068 |
| 1173.033673 | 1173.644875 | 0.611202000000048 | 0.611202 |
| 1175.835692 | 1178.230045 | 2.39435299999991 | 2.394354 |
| 1179.456145 | 1180.371088 | 0.914942999999994 | 0.914943 |
| 1180.859909 | 1181.544422 | 0.684512999999924 | 0.684512 |
| 1182.745215 | 1184.562562 | 1.81734700000015 | 1.817347 |
| 1185.30966 | 1185.885011 | 0.575351000000182 | 0.575351 |
| 1186.525873 | 1187.718957 | 1.193084 | 1.193084 |
| 1239.301791 | 1239.881315 | 0.579523999999992 | 0.579524 |
| 1240.156372 | 1241.051882 | 0.895510000000058 | 0.89551 |
| 1288.958073 | 1289.469841 | 0.511768000000075 | 0.511769 |
| 1290.321247 | 1291.082834 | 0.761586999999963 | 0.761587 |
| 1292.827279 | 1293.611224 | 0.783944999999903 | 0.783946 |
| 1294.261565 | 1295.005896 | 0.744330999999875 | 0.744331 |
| 1297.110227 | 1297.729229 | 0.619002000000137 | 0.619002 |
| 1297.976168 | 1298.971429 | 0.995261000000028 | 0.995261 |
| 1401.222472 | 1401.793741 | 0.571269000000029 | 0.57127 |
| 1405.266757 | 1405.839592 | 0.572834999999941 | 0.572834 |
| 1408.921497 | 1410.059456 | 1.13795899999991 | 1.137959 |
| 1410.921497 | 1411.697483 | 0.775985999999875 | 0.775986 |
| 1411.880363 | 1413.047823 | 1.16746000000012 | 1.16746 |
| 1413.894104 | 1414.806621 | 0.91251699999998 | 0.912517 |
| 1415.063424 | 1415.781746 | 0.718322000000171 | 0.718322 |
| 1462.780612 | 1463.344127 | 0.563515000000052 | 0.563515 |
| 1463.950476 | 1464.811406 | 0.860930000000053 | 0.86093 |
| 1466.069184 | 1466.810385 | 0.741201000000046 | 0.741202 |
| 1468.321383 | 1468.831315 | 0.509931999999935 | 0.509932 |
| 1469.722358 | 1470.951701 | 1.22934299999997 | 1.229342 |
| 1499.832744 | 1500.61458 | 0.781835999999885 | 0.781837 |
| 1504.628957 | 1505.208617 | 0.579660000000104 | 0.57966 |
| 1564.303583 | 1573.800658 | 9.49707500000022 | 9.497075 |
| 1634.323265 | 1634.951497 | 0.628232000000025 | 0.628231 |
| 1747.52093 | 1748.255714 | 0.734783999999991 | 0.734785 |
| 1769.686644 | 1770.548889 | 0.86224500000003 | 0.862245 |
| 1776.14458 | 1777.993764 | 1.84918400000015 | 1.849184 |
| 1865.240385 | 1866.115397 | 0.87501199999997 | 0.875011 |
| 1866.923832 | 1867.561927 | 0.638095000000021 | 0.638095 |
| 1869.053311 | 1870.483379 | 1.43006800000012 | 1.430068 |
| 1871.431587 | 1872.099025 | 0.667437999999947 | 0.667438 |
| 1872.323175 | 1873.122744 | 0.79956900000002 | 0.799569 |
| 1873.425261 | 1874.743719 | 1.31845799999996 | 1.318458 |
| 1877.3178 | 1878.01585 | 0.698049999999967 | 0.69805 |
| 1971.609864 | 1972.387914 | 0.778049999999894 | 0.77805 |
| 1974.875351 | 1976.184535 | 1.30918400000019 | 1.309184 |
| 1977.932268 | 1978.722154 | 0.789886000000024 | 0.789887 |
| 1979.582245 | 1980.272925 | 0.690679999999929 | 0.69068 |
| 2068.369456 | 2069.909002 | 1.53954599999997 | 1.539546 |
| 2070.553605 | 2071.384943 | 0.83133799999996 | 0.831338 |
| 2072.022358 | 2073.317166 | 1.29480799999965 | 1.294807 |
| 2074.236417 | 2075.04932 | 0.812903000000006 | 0.812902 |
| 2076.832245 | 2077.338481 | 0.506235999999717 | 0.506236 |
| 2077.371905 | 2077.948957 | 0.577052000000094 | 0.577052 |
| 2078.940385 | 2079.570635 | 0.63025000000016 | 0.630249 |
| 2163.487914 | 2164.330952 | 0.843037999999979 | 0.843039 |
| 2167.853197 | 2172.921474 | 5.06827700000031 | 5.068277 |
| 2326.847506 | 2327.444785 | 0.597279000000071 | 0.597279 |
| 2330.184354 | 2331.548503 | 1.364149 | 1.36415 |
| 2383.763039 | 2385.362902 | 1.59986299999991 | 1.599864 |
| 2385.969705 | 2386.687324 | 0.717619000000013 | 0.717619 |
| 2388.03415 | 2388.835011 | 0.800861000000168 | 0.800862 |
| 2389.147279 | 2390.405397 | 1.2581180000002 | 1.258118 |
| 2391.597007 | 2393.619524 | 2.02251700000033 | 2.022517 |
| 2394.586054 | 2396.767166 | 2.18111200000021 | 2.181111 |
| 2398.12356 | 2399.964694 | 1.84113399999978 | 1.841134 |
| 2401.369048 | 2403.321882 | 1.95283400000017 | 1.952834 |
| 2502.374694 | 2503.653447 | 1.27875300000005 | 1.278753 |
| 2504.990635 | 2506.39644 | 1.40580499999987 | 1.405805 |
| 2507.303356 | 2508.080317 | 0.776961000000028 | 0.776961 |
| 2508.737823 | 2509.819116 | 1.08129300000019 | 1.081293 |
| 2865.538776 | 2866.162857 | 0.624080999999933 | 0.624082 |
| 2866.626644 | 2868.268209 | 1.6415649999999 | 1.641565 |
| 2869.396893 | 2871.613968 | 2.21707500000002 | 2.217075 |
| 3055.600385 | 3057.693447 | 2.09306199999992 | 2.093061 |
| 3058.396122 | 3059.256349 | 0.860226999999668 | 0.860227 |
| 3059.659705 | 3060.445034 | 0.78532899999982 | 0.785329 |
| 3060.784558 | 3061.531134 | 0.746576000000005 | 0.746576 |
| 3133.593243 | 3134.172834 | 0.579591000000164 | 0.579592 |
| 3134.487415 | 3135.579637 | 1.09222199999977 | 1.092222 |
| 3136.336259 | 3137.1739 | 0.837640999999621 | 0.837642 |
| 3137.720045 | 3138.54288 | 0.822834999999941 | 0.822834 |
| 3142.706553 | 3143.580136 | 0.873583000000053 | 0.873583 |
| 3147.108027 | 3147.96966 | 0.861632999999983 | 0.861633 |
| 3201.566621 | 3203.341111 | 1.77449000000024 | 1.77449 |
| 3203.728435 | 3205.181882 | 1.45344699999987 | 1.453447 |
| 3206.466621 | 3207.500544 | 1.03392299999996 | 1.033923 |
| 3286.87619 | 3289.27746 | 2.40126999999984 | 2.40127 |
| 3514.146417 | 3516.615692 | 2.46927499999993 | 2.469274 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 704 |
| samples | 704 |
| brightness_mean | 0.619776054281498 |
| saturation_mean | 0.287193819320658 |
| frame_difference_mean | 0.0628066981565022 |
| histogram_jumps_gt_0_5 | 16 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.559396028518677 | 0.246112745098039 | N/A | N/A | N/A |
| 5 | 5.005 | 0.668994843959808 | 0.244915849673203 | 0.11817891150713 | 0.37389251893406 | 5 |
| 10 | 9.99331666666667 | 0.676906049251556 | 0.245176198257081 | 0.0490626357495785 | 0.0892353873804139 | 5 |
| 15 | 14.9983166666667 | 0.646367371082306 | 0.25176279956427 | 0.0858262479305267 | 0.205474119761676 | 5 |
| 20 | 20.0033166666667 | 0.640480399131775 | 0.256389978213508 | 0.0209730379283428 | 0.0542089325114202 | 5 |
| 25 | 25.0083166666667 | 0.665873348712921 | 0.241417483660131 | 0.0733537524938583 | 0.147614358234226 | 5 |
| 30 | 29.9966333333333 | 0.786352694034576 | 0.179593137254902 | 0.12139867991209 | 0.353219961428935 | 5 |
| 35 | 35.0016333333333 | 0.652846932411194 | 0.278886165577342 | 0.134289488196373 | 0.432367422381174 | 5 |
| 40 | 40.0066333333333 | 0.676927924156189 | 0.271183278867102 | 0.0740002617239952 | 0.180802022774077 | 5 |
| 45 | 44.99495 | 0.676430284976959 | 0.282505174291939 | 0.0654272809624672 | 0.134206862206781 | 5 |
| 50 | 49.99995 | 0.643058896064758 | 0.254075708061002 | 0.0899259150028229 | 0.268304323008045 | 5 |
| 55 | 55.00495 | 0.660935759544373 | 0.26706045751634 | 0.103101305663586 | 0.222509025219145 | 5 |
| 60 | 59.9932666666667 | 0.68913209438324 | 0.281886982570806 | 0.0937638878822327 | 0.212107169467149 | 5 |
| 65 | 64.9982666666667 | 0.642747282981873 | 0.249293572984749 | 0.0832017958164215 | 0.293620179481176 | 5 |
| 70 | 70.0032666666667 | 0.641849935054779 | 0.255595315904139 | 0.0206854566931725 | 0.0684307281655545 | 5 |
| 75 | 75.0082666666667 | 0.64742648601532 | 0.250757625272331 | 0.0204735826700926 | 0.0508805644876309 | 5 |
| 80 | 79.9965833333333 | 0.663450479507446 | 0.248479575163399 | 0.0699586048722267 | 0.156366792962618 | 5 |
| 85 | 85.0015833333333 | 0.671308577060699 | 0.241641067538126 | 0.037405502051115 | 0.0800441796209371 | 5 |
| 90 | 90.0065833333333 | 0.654351890087128 | 0.247022331154684 | 0.0731811001896858 | 0.149975421427259 | 5 |
| 95 | 94.9949 | 0.664755165576935 | 0.241773148148148 | 0.0699986293911934 | 0.142136788578346 | 5 |
| 100 | 99.9999 | 0.64816689491272 | 0.246412854030501 | 0.0668523982167244 | 0.145708761631687 | 5 |
| 105 | 105.0049 | 0.646997094154358 | 0.252279956427015 | 0.01895697042346 | 0.0723572087926358 | 5 |
| 110 | 109.993216666667 | 0.641690135002136 | 0.254863562091503 | 0.0185759793967009 | 0.0429816878344474 | 5 |
| 115 | 114.998216666667 | 0.642238557338715 | 0.249593681917211 | 0.00525326747447252 | 0.064641742831113 | 5 |
| 120 | 120.003216666667 | 0.667496740818024 | 0.242007352941176 | 0.0710844174027443 | 0.157305019408157 | 5 |
| 125 | 125.008216666667 | 0.665296375751495 | 0.243459150326797 | 0.0415675342082977 | 0.0575201704471282 | 5 |
| 130 | 129.996533333333 | 0.646465659141541 | 0.251509531590414 | 0.0720294117927551 | 0.142433664448205 | 5 |
| 135 | 135.001533333333 | 0.645021021366119 | 0.25173665577342 | 0.00852314848452806 | 0.0265248954360241 | 5 |
| 140 | 140.006533333333 | 0.648905575275421 | 0.245342047930283 | 0.0210359487682581 | 0.0726842517667063 | 5 |
| 145 | 144.99485 | 0.663477957248688 | 0.244690631808279 | 0.0685806125402451 | 0.129216374167446 | 5 |
| 150 | 149.99985 | 0.666235566139221 | 0.245065904139434 | 0.0284602399915457 | 0.0809046763420966 | 5 |
| 155 | 155.00485 | 0.648805797100067 | 0.251293300653595 | 0.0696078389883041 | 0.132647954558371 | 5 |
| 160 | 159.993166666667 | 0.646604061126709 | 0.247437908496732 | 0.0223346967250109 | 0.0715172309726309 | 5 |
| 165 | 164.998166666667 | 0.667050361633301 | 0.241007897603486 | 0.0709076747298241 | 0.154608627033125 | 5 |
| 170 | 170.003166666667 | 0.646114885807037 | 0.253137254901961 | 0.0707611665129662 | 0.148636988465098 | 5 |
| 175 | 175.008166666667 | 0.642266571521759 | 0.253774782135076 | 0.0153826251626015 | 0.038000378750319 | 5 |
| 180 | 179.996483333333 | 0.640633225440979 | 0.256867919389978 | 0.0209025051444769 | 0.039026510501256 | 5 |
| 185 | 185.001483333333 | 0.648797154426575 | 0.250864106753813 | 0.0198425929993391 | 0.0522629347740671 | 5 |
| 190 | 190.006483333333 | 0.647020101547241 | 0.25116802832244 | 0.0115100750699639 | 0.0320606074897026 | 5 |
| 195 | 194.9948 | 0.66959011554718 | 0.241298474945534 | 0.0715563744306564 | 0.147518942950968 | 5 |
| 200 | 199.9998 | 0.643617630004883 | 0.254134259259259 | 0.0724632367491722 | 0.150832041833857 | 5 |
| 205 | 205.0048 | 0.646553695201874 | 0.250984204793028 | 0.0272328425198793 | 0.0505615131571403 | 5 |
| 210 | 209.993116666667 | 0.664351880550385 | 0.242450708061002 | 0.0684267431497574 | 0.138859676850838 | 5 |
| 215 | 214.998116666667 | 0.664038717746735 | 0.241335784313725 | 0.0234537031501532 | 0.046316056542598 | 5 |
| 220 | 220.003116666667 | 0.656219184398651 | 0.307973583877996 | 0.0851228162646294 | 0.406613163170234 | 5 |
| 225 | 225.008116666667 | 0.624607622623444 | 0.290144880174292 | 0.0870125219225883 | 0.369396556547121 | 5 |
| 230 | 229.996433333333 | 0.630601346492767 | 0.284928104575163 | 0.0664616078138351 | 0.238409432964831 | 5 |
| 235 | 235.001433333333 | 0.695139408111572 | 0.296236111111111 | 0.0841051116585732 | 0.309849824578796 | 5 |
| 240 | 240.006433333333 | 0.618842661380768 | 0.291513071895425 | 0.096915028989315 | 0.398718310292611 | 5 |
| 245 | 244.99475 | 0.643630504608154 | 0.273601579520697 | 0.0603139996528625 | 0.280985132581966 | 5 |
| 250 | 249.99975 | 0.633272111415863 | 0.269697440087146 | 0.0656290799379349 | 0.190720375582399 | 5 |
| 255 | 255.00475 | 0.631576538085938 | 0.286843954248366 | 0.0616857260465622 | 0.213762549781088 | 5 |
| 260 | 259.993066666667 | 0.786426544189453 | 0.179382080610022 | 0.155746445059776 | 0.464250161749556 | 5 |
| 265 | 264.998066666667 | 0.644284307956696 | 0.266022875816993 | 0.143077343702316 | 0.382152689105065 | 5 |
| 270 | 270.003066666667 | 0.640119552612305 | 0.273656862745098 | 0.107871174812317 | 0.320225081063634 | 5 |
| 275 | 275.008066666667 | 0.62530529499054 | 0.284132625272331 | 0.0663469508290291 | 0.227480041716917 | 5 |
| 280 | 279.996383333333 | 0.623949408531189 | 0.286585239651416 | 0.0185836050659418 | 0.0525673880202685 | 5 |
| 285 | 285.001383333333 | 0.633732080459595 | 0.282250544662309 | 0.0607734210789204 | 0.234258547133448 | 5 |
| 290 | 290.006383333333 | 0.627563774585724 | 0.288648692810458 | 0.0159558821469545 | 0.0704083635287094 | 5 |
| 295 | 294.9947 | 0.631198227405548 | 0.286441993464052 | 0.0119471680372953 | 0.0334691502163237 | 5 |
| 300 | 299.9997 | 0.632394313812256 | 0.283115468409586 | 0.0183605663478374 | 0.0577847493615412 | 5 |
| 305 | 305.0047 | 0.641460239887238 | 0.274443899782135 | 0.0554526150226593 | 0.130734106539517 | 5 |
| 310 | 309.993016666667 | 0.626626133918762 | 0.300081154684096 | 0.0432606153190136 | 0.129165933738906 | 5 |
| 315 | 314.998016666667 | 0.622751951217651 | 0.274417211328976 | 0.0694591552019119 | 0.235036651546677 | 5 |
| 320 | 320.003016666667 | 0.625175356864929 | 0.285653867102397 | 0.0779414549469948 | 0.222430521434311 | 5 |
| 325 | 325.008016666667 | 0.630184412002563 | 0.286410403050109 | 0.0640808790922165 | 0.248301959692868 | 5 |
| 330 | 329.996333333333 | 0.625941455364227 | 0.274633169934641 | 0.0628197118639946 | 0.20663479047953 | 5 |
| 335 | 335.001333333333 | 0.624722480773926 | 0.274683551198257 | 0.00527614401653409 | 0.0291658866996123 | 5 |
| 340 | 340.006333333333 | 0.694680869579315 | 0.265625544662309 | 0.102888606488705 | 0.325850903481235 | 5 |
| 345 | 344.99465 | 0.706897914409637 | 0.262673474945534 | 0.0702971071004868 | 0.134094680177939 | 5 |
| 350 | 349.99965 | 0.681181669235229 | 0.268574346405229 | 0.0640141516923904 | 0.168073122855512 | 5 |
| 355 | 355.00465 | 0.626277506351471 | 0.273996732026144 | 0.0867603495717049 | 0.263997889350677 | 5 |
| 360 | 359.992966666667 | 0.626485049724579 | 0.272686002178649 | 0.0169858392328024 | 0.0368643581341354 | 5 |
| 365 | 364.997966666667 | 0.627149522304535 | 0.272803649237473 | 0.0110059911385179 | 0.0324737153643821 | 5 |
| 370 | 370.002966666667 | 0.645615756511688 | 0.260227396514161 | 0.0711067542433739 | 0.176499769687204 | 5 |
| 375 | 375.007966666667 | 0.64456182718277 | 0.261074618736383 | 0.0131764700636268 | 0.0377339910541746 | 5 |
| 380 | 379.996283333333 | 0.647637248039246 | 0.250383169934641 | 0.0787110552191734 | 0.176751661365556 | 5 |
| 385 | 385.001283333333 | 0.642793595790863 | 0.253971949891068 | 0.0140778860077262 | 0.0404512940312191 | 5 |
| 390 | 390.006283333333 | 0.662160933017731 | 0.249373638344227 | 0.0703069120645523 | 0.148660462763199 | 5 |
| 395 | 394.9946 | 0.641722798347473 | 0.254051198257081 | 0.0713875219225883 | 0.145934333483117 | 5 |
| 400 | 399.9996 | 0.645991563796997 | 0.252438453159041 | 0.0187214054167271 | 0.0412493052349465 | 5 |
| 405 | 405.0046 | 0.650328159332275 | 0.251391339869281 | 0.0203747265040874 | 0.0417967469217008 | 5 |
| 410 | 409.992916666667 | 0.662809669971466 | 0.244685729847495 | 0.0667543560266495 | 0.134643116572325 | 5 |
| 415 | 414.997916666667 | 0.639485001564026 | 0.252243464052288 | 0.0718829035758972 | 0.157140035407675 | 5 |
| 420 | 420.002916666667 | 0.644423246383667 | 0.246806100217865 | 0.0182295739650726 | 0.0465182098821192 | 5 |
| 425 | 425.007916666667 | 0.644217312335968 | 0.252662037037037 | 0.022809911519289 | 0.0750466703853713 | 5 |
| 430 | 429.996233333333 | 0.644043624401093 | 0.252196895424837 | 0.00718082766979933 | 0.0304882145394772 | 5 |
| 435 | 435.001233333333 | 0.663899183273315 | 0.242214869281046 | 0.0686759278178215 | 0.129358301704186 | 5 |
| 440 | 440.006233333333 | 0.641985893249512 | 0.249277505446623 | 0.0722429230809212 | 0.154706156218213 | 5 |
| 445 | 444.99455 | 0.663619577884674 | 0.251307461873638 | 0.0729904696345329 | 0.166222722441552 | 5 |
| 450 | 449.99955 | 0.650497317314148 | 0.250226034858388 | 0.0724637806415558 | 0.15547520499982 | 5 |
| 455 | 455.00455 | 0.648627817630768 | 0.250183551198257 | 0.0134093137457967 | 0.0338069392037581 | 5 |
| 460 | 459.992866666667 | 0.646856188774109 | 0.24581045751634 | 0.023005174472928 | 0.0718502690703724 | 5 |
| 465 | 464.997866666667 | 0.665023446083069 | 0.240734204793028 | 0.0690904185175896 | 0.147198984944525 | 5 |
| 470 | 470.002866666667 | 0.663886725902557 | 0.245800108932462 | 0.0236977133899927 | 0.0486296155712449 | 5 |
| 475 | 475.007866666667 | 0.649011731147766 | 0.250852124183007 | 0.0690950453281403 | 0.144915112297705 | 5 |
| 480 | 479.996183333333 | 0.645775377750397 | 0.250859477124183 | 0.0134618738666177 | 0.0380747299463238 | 5 |
| 485 | 485.001183333333 | 0.643641114234924 | 0.254615468409586 | 0.0206092037260532 | 0.0493445769950966 | 5 |
| 490 | 490.006183333333 | 0.64395809173584 | 0.249600762527233 | 0.00534694967791438 | 0.0645337495779037 | 5 |
| 495 | 494.9945 | 0.666889250278473 | 0.242283769063181 | 0.0734523385763168 | 0.151407468599716 | 5 |
| 500 | 499.9995 | 0.666394352912903 | 0.242483660130719 | 0.0160716231912374 | 0.0264489018657496 | 5 |
| 505 | 505.0045 | 0.663443088531494 | 0.242380718954248 | 0.0297666098922491 | 0.05102315449026 | 5 |
| 510 | 509.992816666667 | 0.642508506774902 | 0.248636982570806 | 0.0720272287726402 | 0.152708995864375 | 5 |
| 515 | 514.997816666667 | 0.663973569869995 | 0.241672930283224 | 0.0748246163129807 | 0.160252111982378 | 5 |
| 520 | 520.002816666667 | 0.641635596752167 | 0.250776416122004 | 0.0726838186383247 | 0.162324295776529 | 5 |
| 525 | 525.007816666667 | 0.645874500274658 | 0.25210348583878 | 0.0222121477127075 | 0.0720871581115056 | 5 |
| 530 | 529.996133333333 | 0.643108189105988 | 0.252572167755991 | 0.0154226580634713 | 0.0413278478438898 | 5 |
| 535 | 535.001133333333 | 0.648889422416687 | 0.250360838779956 | 0.0230759792029858 | 0.0397218943347334 | 5 |
| 540 | 540.006133333333 | 0.645589351654053 | 0.251485838779956 | 0.02859041467309 | 0.0413604456613982 | 5 |
| 545 | 544.99445 | 0.663762032985687 | 0.245002723311547 | 0.0709183067083359 | 0.139996608716419 | 5 |
| 550 | 549.99945 | 0.667166411876678 | 0.241703703703704 | 0.0288826245814562 | 0.0499031504580146 | 5 |
| 555 | 555.00445 | 0.647445797920227 | 0.250462418300654 | 0.0707499980926514 | 0.145814005271414 | 5 |
| 560 | 559.992766666667 | 0.647866010665894 | 0.25048311546841 | 0.00975027214735746 | 0.0322851601439032 | 5 |
| 565 | 564.997766666667 | 0.667014181613922 | 0.241088507625272 | 0.0674406364560127 | 0.142833987685347 | 5 |
| 570 | 570.002766666667 | 0.665153622627258 | 0.241196895424837 | 0.0191889982670546 | 0.0373502829733723 | 5 |
| 575 | 575.007766666667 | 0.639775931835175 | 0.252380718954248 | 0.0738325193524361 | 0.162583548895194 | 5 |
| 580 | 579.996083333333 | 0.663678646087646 | 0.244360294117647 | 0.0724490731954575 | 0.147292789131671 | 5 |
| 585 | 585.001083333333 | 0.693869888782501 | 0.258627723311547 | 0.0725985765457153 | 0.19628483591257 | 5 |
| 590 | 590.006083333333 | 0.693766355514526 | 0.256423474945534 | 0.0175239648669958 | 0.0677345198101498 | 5 |
| 595 | 594.9944 | 0.706768274307251 | 0.257376089324619 | 0.0679458007216454 | 0.121659036988579 | 5 |
| 600 | 599.9994 | 0.6884526014328 | 0.25958660130719 | 0.069412037730217 | 0.122713356494347 | 5 |
| 605 | 605.0044 | 0.713347852230072 | 0.251104575163399 | 0.0678641051054001 | 0.133570199437438 | 5 |
| 610 | 609.992716666667 | 0.709696412086487 | 0.253839596949891 | 0.0304553341120481 | 0.0480014392633237 | 5 |
| 615 | 614.997716666667 | 0.694749474525452 | 0.259288671023965 | 0.0657568126916885 | 0.110065334892979 | 5 |
| 620 | 620.002716666667 | 0.696287035942078 | 0.258368191721133 | 0.0135473851114511 | 0.0312793714246046 | 5 |
| 625 | 625.007716666667 | 0.687224388122559 | 0.264852396514161 | 0.0195925924926996 | 0.0504512863262569 | 5 |
| 630 | 629.996033333333 | 0.709535717964172 | 0.251613834422658 | 0.0691876336932182 | 0.12227514125473 | 5 |
| 635 | 635.001033333333 | 0.699744820594788 | 0.263125272331155 | 0.0356045737862587 | 0.0717160227877865 | 5 |
| 640 | 640.006033333333 | 0.691433310508728 | 0.257843409586057 | 0.068813718855381 | 0.120182838984736 | 5 |
| 645 | 644.99435 | 0.706862449645996 | 0.255389161220044 | 0.0676966160535812 | 0.127374746614106 | 5 |
| 650 | 649.99935 | 0.708305239677429 | 0.254302832244009 | 0.0164814814925194 | 0.0347051837643812 | 5 |
| 655 | 655.00435 | 0.69167160987854 | 0.256982026143791 | 0.0664196610450745 | 0.120995317522378 | 5 |
| 660 | 659.992666666667 | 0.697918295860291 | 0.25614651416122 | 0.0194079503417015 | 0.0750413164387195 | 5 |
| 665 | 664.997666666667 | 0.708076596260071 | 0.253557734204793 | 0.0648559331893921 | 0.100698780943519 | 5 |
| 670 | 670.002666666667 | 0.696582019329071 | 0.252479302832244 | 0.0670468360185623 | 0.119933058231024 | 5 |
| 675 | 675.007666666667 | 0.695910632610321 | 0.257987745098039 | 0.0146440621465445 | 0.0683719909432154 | 5 |
| 680 | 679.995983333333 | 0.70911169052124 | 0.252740196078431 | 0.0668273344635963 | 0.10804755717015 | 5 |
| 685 | 685.000983333333 | 0.695798218250275 | 0.25829711328976 | 0.0661919862031937 | 0.107264920300815 | 5 |
| 690 | 690.005983333333 | 0.711819708347321 | 0.250536764705882 | 0.0666217282414436 | 0.107824561721415 | 5 |
| 695 | 694.9943 | 0.705458283424377 | 0.257533496732026 | 0.0311222746968269 | 0.0635824559395577 | 5 |
| 700 | 699.9993 | 0.687054693698883 | 0.259769607843137 | 0.0701791867613792 | 0.123011517468654 | 5 |
| 705 | 705.0043 | 0.689876973628998 | 0.261558278867102 | 0.0206342600286007 | 0.0665229066754304 | 5 |
| 710 | 709.992616666667 | 0.709789752960205 | 0.248984204793028 | 0.0666350722312927 | 0.128803986895789 | 5 |
| 715 | 714.997616666667 | 0.591356217861176 | 0.312434368191721 | 0.135272338986397 | 0.334320026297519 | 5 |
| 720 | 720.002616666667 | 0.589040577411652 | 0.315601034858388 | 0.023748092353344 | 0.085947609421317 | 5 |
| 725 | 725.007616666667 | 0.586936056613922 | 0.318126361655773 | 0.0215713493525982 | 0.0503633482788005 | 5 |
| 730 | 729.995933333333 | 0.616473853588104 | 0.260945533769063 | 0.0865427479147911 | 0.265121247186332 | 5 |
| 735 | 735.000933333333 | 0.612149000167847 | 0.261778867102397 | 0.0375471152365208 | 0.0707344986243232 | 5 |
| 740 | 740.005933333333 | 0.592011451721191 | 0.313262527233115 | 0.0760345831513405 | 0.273719173060317 | 5 |
| 745 | 744.99425 | 0.588659346103668 | 0.315541938997821 | 0.0247813165187836 | 0.0569344079164939 | 5 |
| 750 | 749.99925 | 0.609646022319794 | 0.313040849673203 | 0.0682208612561226 | 0.182340792502292 | 5 |
| 755 | 755.00425 | 0.612286806106567 | 0.310144335511983 | 0.0327268540859222 | 0.0626195046231602 | 5 |
| 760 | 759.992566666667 | 0.606791436672211 | 0.311477941176471 | 0.038445807993412 | 0.0651135442723444 | 5 |
| 765 | 764.997566666667 | 0.650886714458466 | 0.257710239651416 | 0.0884645953774452 | 0.257924729961655 | 5 |
| 770 | 770.002566666667 | 0.63683009147644 | 0.266721677559913 | 0.0271584950387478 | 0.0575481928113632 | 5 |
| 775 | 775.007566666667 | 0.594808638095856 | 0.254530501089325 | 0.117751359939575 | 0.271642360149759 | 5 |
| 780 | 779.995883333333 | 0.597058832645416 | 0.29694825708061 | 0.114184364676476 | 0.337570116007688 | 5 |
| 785 | 785.000883333333 | 0.615734815597534 | 0.259938725490196 | 0.0833954215049744 | 0.198561615333557 | 5 |
| 790 | 790.005883333333 | 0.648662030696869 | 0.258580882352941 | 0.0801778361201286 | 0.181059577232265 | 5 |
| 795 | 794.9942 | 0.592754900455475 | 0.312540849673203 | 0.0864436253905296 | 0.268672528177404 | 5 |
| 800 | 799.9992 | 0.608901143074036 | 0.311349128540305 | 0.0643346905708313 | 0.183591081000951 | 5 |
| 805 | 805.0042 | 0.595128834247589 | 0.311324891067538 | 0.0688050091266632 | 0.188878035688082 | 5 |
| 810 | 809.992516666667 | 0.590149998664856 | 0.316213235294118 | 0.0196672100573778 | 0.0559615118037692 | 5 |
| 815 | 814.997516666667 | 0.589313745498657 | 0.315819444444444 | 0.00619035912677646 | 0.0365415021493496 | 5 |
| 820 | 820.002516666667 | 0.590587437152863 | 0.315416394335512 | 0.016055827960372 | 0.048342413957296 | 5 |
| 825 | 825.007516666667 | 0.595764696598053 | 0.314164760348584 | 0.0234572440385818 | 0.0509069230385017 | 5 |
| 830 | 829.995833333333 | 0.607047379016876 | 0.313979575163399 | 0.0668137297034264 | 0.185881088266903 | 5 |
| 835 | 835.000833333333 | 0.611154675483704 | 0.313353758169935 | 0.0309460796415806 | 0.0735622206627629 | 5 |
| 840 | 840.005833333333 | 0.587666690349579 | 0.317393790849673 | 0.0702641606330872 | 0.195189929556954 | 5 |
| 845 | 844.99415 | 0.591956973075867 | 0.313752450980392 | 0.0234351865947247 | 0.0713083687256824 | 5 |
| 850 | 849.99915 | 0.597959637641907 | 0.293977396514161 | 0.0760424807667732 | 0.227473930217458 | 5 |
| 855 | 855.00415 | 0.686091244220734 | 0.250539215686275 | 0.10581398755312 | 0.259979569284087 | 5 |
| 860 | 859.992466666667 | 0.617148697376251 | 0.26165931372549 | 0.0986636728048325 | 0.215514687021887 | 5 |
| 865 | 864.997466666667 | 0.586773157119751 | 0.31873720043573 | 0.0861222743988037 | 0.274051202973248 | 5 |
| 870 | 870.002466666667 | 0.647159576416016 | 0.259082244008715 | 0.0858390554785728 | 0.274813131257264 | 5 |
| 875 | 875.007466666667 | 0.59540718793869 | 0.292035130718954 | 0.080926202237606 | 0.17854993585958 | 5 |
| 880 | 879.995783333333 | 0.610483109951019 | 0.263592320261438 | 0.0755890607833862 | 0.154538013474147 | 5 |
| 885 | 885.000783333333 | 0.60814106464386 | 0.267609204793028 | 0.0254384521394968 | 0.0609734200898582 | 5 |
| 890 | 890.005783333333 | 0.64292186498642 | 0.261340413943355 | 0.0804234743118286 | 0.186831940487083 | 5 |
| 895 | 894.9941 | 0.588423788547516 | 0.317800108932462 | 0.0847301259636879 | 0.267928899660777 | 5 |
| 900 | 899.9991 | 0.688243746757507 | 0.25262962962963 | 0.120660945773125 | 0.298881216144939 | 5 |
| 905 | 905.0041 | 0.664702713489532 | 0.239928376906318 | 0.0872617065906525 | 0.206090407811864 | 5 |
| 910 | 909.992416666667 | 0.663132131099701 | 0.238264161220044 | 0.0221337154507637 | 0.0776181186460905 | 5 |
| 915 | 914.997416666667 | 0.661954522132874 | 0.238077614379085 | 0.00489705847576261 | 0.0257024677861906 | 5 |
| 920 | 920.002416666667 | 0.693026661872864 | 0.232579793028322 | 0.0742213949561119 | 0.153724987511291 | 5 |
| 925 | 925.007416666667 | 0.66381561756134 | 0.238860294117647 | 0.0729959085583687 | 0.13790458119975 | 5 |
| 930 | 929.995733333333 | 0.664985835552216 | 0.238635620915033 | 0.00413807202130556 | 0.0215313669909262 | 5 |
| 935 | 935.000733333333 | 0.668065309524536 | 0.237705610021786 | 0.0206034854054451 | 0.0430952571091835 | 5 |
| 940 | 940.005733333333 | 0.666744232177734 | 0.235354575163399 | 0.0235525574535131 | 0.072194312418433 | 5 |
| 945 | 944.99405 | 0.663608133792877 | 0.239421840958606 | 0.0251056626439095 | 0.0751950739822037 | 5 |
| 950 | 949.99905 | 0.686606228351593 | 0.231751361655773 | 0.0707747787237167 | 0.12511177447886 | 5 |
| 955 | 955.00405 | 0.689699351787567 | 0.239469226579521 | 0.0340359471738338 | 0.0754669588931446 | 5 |
| 960 | 959.992366666667 | 0.68863046169281 | 0.233680283224401 | 0.0319773964583874 | 0.063709888554313 | 5 |
| 965 | 964.997366666667 | 0.685797691345215 | 0.259654411764706 | 0.0882652476429939 | 0.265018803349728 | 5 |
| 970 | 970.002366666667 | 0.715398490428925 | 0.257278594771242 | 0.06753159314394 | 0.164493121269688 | 5 |
| 975 | 975.007366666667 | 0.71703428030014 | 0.256830882352941 | 0.0330057181417942 | 0.0433628535902171 | 5 |
| 980 | 979.995683333333 | 0.661012530326843 | 0.241837418300654 | 0.0907614305615425 | 0.269439600599538 | 5 |
| 985 | 985.000683333333 | 0.660077333450317 | 0.237121732026144 | 0.00618137186393142 | 0.0591978369892866 | 5 |
| 990 | 990.005683333333 | 0.691024601459503 | 0.236398420479303 | 0.0753142684698105 | 0.147129242907287 | 5 |
| 995 | 994.994 | 0.666935741901398 | 0.241360566448802 | 0.0698371455073357 | 0.126858143077906 | 5 |
| 1000 | 999.999 | 0.662319719791412 | 0.241740196078431 | 0.0190958604216576 | 0.0451182062094095 | 5 |
| 1005 | 1005.004 | 0.66317754983902 | 0.238736383442266 | 0.0201258175075054 | 0.0455388038983808 | 5 |
| 1010 | 1009.99231666667 | 0.652609467506409 | 0.23328839869281 | 0.0694678649306297 | 0.15442169084248 | 5 |
| 1015 | 1014.99731666667 | 0.664607882499695 | 0.238993191721133 | 0.0683741793036461 | 0.159457666471872 | 5 |
| 1020 | 1020.00231666667 | 0.666677057743073 | 0.238960511982571 | 0.0184689536690712 | 0.0442229453600546 | 5 |
| 1025 | 1025.00731666667 | 0.687853991985321 | 0.232296840958606 | 0.068433552980423 | 0.123997352762897 | 5 |
| 1030 | 1029.99563333333 | 0.686532378196716 | 0.228999183006536 | 0.0312655232846737 | 0.0719853183403394 | 5 |
| 1035 | 1035.00063333333 | 0.663566768169403 | 0.241168845315904 | 0.0670196041464806 | 0.139301958312328 | 5 |
| 1040 | 1040.00563333333 | 0.664486646652222 | 0.240944989106754 | 0.0241966210305691 | 0.0409341089592811 | 5 |
| 1045 | 1044.99395 | 0.688876688480377 | 0.232355119825708 | 0.0727036967873573 | 0.129965654944299 | 5 |
| 1050 | 1049.99895 | 0.683751881122589 | 0.23408660130719 | 0.0239526126533747 | 0.0425533411916058 | 5 |
| 1055 | 1055.00395 | 0.685712933540344 | 0.234989379084967 | 0.0236043017357588 | 0.0461786545837806 | 5 |
| 1060 | 1059.99226666667 | 0.689239919185638 | 0.233183278867102 | 0.0302273947745562 | 0.0508726299860198 | 5 |
| 1065 | 1064.99726666667 | 0.662022352218628 | 0.238172930283224 | 0.0712535381317139 | 0.139433141145157 | 5 |
| 1070 | 1070.00226666667 | 0.664835453033447 | 0.238982298474946 | 0.0201541390269995 | 0.0764434479890024 | 5 |
| 1075 | 1075.00726666667 | 0.68928188085556 | 0.227741830065359 | 0.0690416619181633 | 0.140152155111359 | 5 |
| 1080 | 1079.99558333333 | 0.649164199829102 | 0.243176470588235 | 0.0871759206056595 | 0.164875214134166 | 5 |
| 1085 | 1085.00058333333 | 0.662737786769867 | 0.236831427015251 | 0.0357037000358105 | 0.094803120584025 | 5 |
| 1090 | 1090.00558333333 | 0.670610547065735 | 0.231822984749455 | 0.0217067003250122 | 0.0443569894661339 | 5 |
| 1095 | 1094.9939 | 0.668698787689209 | 0.232331427015251 | 0.00615032622590661 | 0.0287980911710732 | 5 |
| 1100 | 1099.9989 | 0.660776615142822 | 0.237016612200436 | 0.0278545748442411 | 0.0585085500340612 | 5 |
| 1105 | 1105.0039 | 0.684370636940002 | 0.233936002178649 | 0.0713733583688736 | 0.138974200443172 | 5 |
| 1110 | 1109.99221666667 | 0.660450994968414 | 0.237113289760349 | 0.0702960193157196 | 0.139808230808404 | 5 |
| 1115 | 1114.99721666667 | 0.664836287498474 | 0.235415032679739 | 0.0191685743629932 | 0.0462465850245026 | 5 |
| 1120 | 1120.00221666667 | 0.663744330406189 | 0.235590958605664 | 0.00414433516561985 | 0.0261739777399437 | 5 |
| 1125 | 1125.00721666667 | 0.690629601478577 | 0.23281862745098 | 0.0729381740093231 | 0.144544963643617 | 5 |
| 1130 | 1129.99553333333 | 0.692340672016144 | 0.233141339869281 | 0.0113586597144604 | 0.039324302603745 | 5 |
| 1135 | 1135.00053333333 | 0.668248951435089 | 0.232232298474946 | 0.0722066983580589 | 0.133865734781944 | 5 |
| 1140 | 1140.00553333333 | 0.664146542549133 | 0.238609204793028 | 0.0261377971619368 | 0.0729795878127157 | 5 |
| 1145 | 1144.99385 | 0.664776146411896 | 0.233873910675381 | 0.00455283233895898 | 0.0582032759707633 | 5 |
| 1150 | 1149.99885 | 0.68694281578064 | 0.231989651416122 | 0.0679324567317963 | 0.128448890097882 | 5 |
| 1155 | 1155.00385 | 0.659590899944305 | 0.242499455337691 | 0.0697984769940376 | 0.145244211160437 | 5 |
| 1160 | 1159.99216666667 | 0.666092693805695 | 0.239145697167756 | 0.0183992367237806 | 0.0457319424316173 | 5 |
| 1165 | 1164.99716666667 | 0.687865793704987 | 0.239761710239651 | 0.06998610496521 | 0.134741045859284 | 5 |
| 1170 | 1170.00216666667 | 0.663454532623291 | 0.239020969498911 | 0.0720996707677841 | 0.136340140512628 | 5 |
| 1175 | 1175.00716666667 | 0.663796067237854 | 0.238874183006536 | 0.00533169927075505 | 0.027097249381616 | 5 |
| 1180 | 1179.99548333333 | 0.660788714885712 | 0.241818899782135 | 0.0222448222339153 | 0.0434525889738787 | 5 |
| 1185 | 1185.00048333333 | 0.687743723392487 | 0.236315359477124 | 0.0725890547037125 | 0.130594385345702 | 5 |
| 1190 | 1190.00548333333 | 0.671372354030609 | 0.233519335511983 | 0.0713447704911232 | 0.14013511350413 | 5 |
| 1195 | 1194.9938 | 0.690484762191772 | 0.230979575163399 | 0.0685117095708847 | 0.136237012373512 | 5 |
| 1200 | 1199.9988 | 0.68756103515625 | 0.236611928104575 | 0.0235958602279425 | 0.0614307511081654 | 5 |
| 1205 | 1205.0038 | 0.669152557849884 | 0.234868736383442 | 0.0666350722312927 | 0.139959773728242 | 5 |
| 1210 | 1209.99211666667 | 0.667252480983734 | 0.234957516339869 | 0.00670506479218602 | 0.0330577491163708 | 5 |
| 1215 | 1214.99711666667 | 0.66370016336441 | 0.23877614379085 | 0.0261781010776758 | 0.0745740603812436 | 5 |
| 1220 | 1220.00211666667 | 0.663234710693359 | 0.233726307189542 | 0.00666748359799385 | 0.0648290519450536 | 5 |
| 1225 | 1225.00711666667 | 0.689308822154999 | 0.232674291938998 | 0.0706846341490746 | 0.13838705914311 | 5 |
| 1230 | 1229.99543333333 | 0.687398135662079 | 0.232939270152505 | 0.0174520686268806 | 0.034182910578667 | 5 |
| 1235 | 1235.00043333333 | 0.69013237953186 | 0.236759531590414 | 0.0248796287924051 | 0.068068153905272 | 5 |
| 1240 | 1240.00543333333 | 0.64813369512558 | 0.255927559912854 | 0.0856255441904068 | 0.250781288849244 | 5 |
| 1245 | 1244.99375 | 0.674110293388367 | 0.250206699346405 | 0.0733360424637794 | 0.167746464094307 | 5 |
| 1250 | 1249.99875 | 0.65358030796051 | 0.260186274509804 | 0.0734297335147858 | 0.145874987185294 | 5 |
| 1255 | 1255.00375 | 0.644217848777771 | 0.260562908496732 | 0.033831425011158 | 0.0620979261352916 | 5 |
| 1260 | 1259.99206666667 | 0.664802014827728 | 0.248909041394336 | 0.0700432956218719 | 0.129775853109683 | 5 |
| 1265 | 1264.99706666667 | 0.645706474781036 | 0.262291394335512 | 0.0690454766154289 | 0.136165699621539 | 5 |
| 1270 | 1270.00206666667 | 0.646878778934479 | 0.259168572984749 | 0.0149942804127932 | 0.0362514639283651 | 5 |
| 1275 | 1275.00706666667 | 0.647032499313354 | 0.259235021786492 | 0.00622276682406664 | 0.0323845154623454 | 5 |
| 1280 | 1279.99538333333 | 0.644036531448364 | 0.258654684095861 | 0.0224866550415754 | 0.079267604830747 | 5 |
| 1285 | 1285.00038333333 | 0.664291441440582 | 0.253221949891068 | 0.0665076225996017 | 0.169527692430661 | 5 |
| 1290 | 1290.00538333333 | 0.647651374340057 | 0.270470043572985 | 0.10345097631216 | 0.235394129412425 | 5 |
| 1295 | 1294.9937 | 0.637696146965027 | 0.27665522875817 | 0.0241002179682255 | 0.0524456047816785 | 5 |
| 1300 | 1299.9987 | 0.662942588329315 | 0.250744825708061 | 0.108947440981865 | 0.235935462062718 | 5 |
| 1305 | 1305.0037 | 0.635451793670654 | 0.273430555555556 | 0.10889433324337 | 0.238175600827051 | 5 |
| 1310 | 1309.99201666667 | 0.643860816955566 | 0.275029684095861 | 0.0184880178421736 | 0.0715433099775801 | 5 |
| 1315 | 1314.99701666667 | 0.701448559761047 | 0.249455337690632 | 0.0964711233973503 | 0.207602099510669 | 5 |
| 1320 | 1320.00201666667 | 0.694160401821136 | 0.253868736383442 | 0.0400610007345676 | 0.0524963772287566 | 5 |
| 1325 | 1325.00701666667 | 0.644233405590057 | 0.272898420479303 | 0.0921116471290588 | 0.189426412554468 | 5 |
| 1330 | 1329.99533333333 | 0.648336052894592 | 0.262714596949891 | 0.0910356715321541 | 0.213527286924434 | 5 |
| 1335 | 1335.00033333333 | 0.644685208797455 | 0.274295751633987 | 0.0915114358067513 | 0.220690579742133 | 5 |
| 1340 | 1340.00533333333 | 0.639957845211029 | 0.275130446623094 | 0.019908769056201 | 0.0461470344755339 | 5 |
| 1345 | 1344.99365 | 0.652271509170532 | 0.25946105664488 | 0.0942440032958984 | 0.208242991760122 | 5 |
| 1350 | 1349.99865 | 0.667942821979523 | 0.255208061002179 | 0.068386435508728 | 0.133024747624676 | 5 |
| 1355 | 1355.00365 | 0.701942026615143 | 0.24684940087146 | 0.0759795755147934 | 0.2082843038035 | 5 |
| 1360 | 1359.99196666667 | 0.648228466510773 | 0.258938725490196 | 0.0831633806228638 | 0.242077198103571 | 5 |
| 1365 | 1364.99696666667 | 0.645578384399414 | 0.269261165577342 | 0.0978793576359749 | 0.22018330193357 | 5 |
| 1370 | 1370.00196666667 | 0.651071667671204 | 0.270498366013072 | 0.0352704226970673 | 0.0857048513182226 | 5 |
| 1375 | 1375.00696666667 | 0.65101283788681 | 0.270654411764706 | 0.00598583836108446 | 0.0303245573584067 | 5 |
| 1380 | 1379.99528333333 | 0.639310479164124 | 0.276418845315904 | 0.0309496186673641 | 0.0739569131771024 | 5 |
| 1385 | 1385.00028333333 | 0.670658230781555 | 0.250174291938998 | 0.106802009046078 | 0.233509680676125 | 5 |
| 1390 | 1390.00528333333 | 0.668512225151062 | 0.2563401416122 | 0.0231176465749741 | 0.0629936074913791 | 5 |
| 1395 | 1394.9936 | 0.695229887962341 | 0.249240468409586 | 0.0771778374910355 | 0.218115342801305 | 5 |
| 1400 | 1399.9986 | 0.6322380900383 | 0.277542483660131 | 0.0930964052677155 | 0.237529174192591 | 5 |
| 1405 | 1405.0036 | 0.630824625492096 | 0.277640250544662 | 0.00521840946748853 | 0.0319167449942677 | 5 |
| 1410 | 1409.99191666667 | 0.649250268936157 | 0.268629357298475 | 0.0309005975723267 | 0.0744964934631472 | 5 |
| 1415 | 1414.99691666667 | 0.642446637153625 | 0.270957516339869 | 0.0345383957028389 | 0.061704112339674 | 5 |
| 1420 | 1420.00191666667 | 0.698212504386902 | 0.250294389978214 | 0.0825795158743858 | 0.241484469556736 | 5 |
| 1425 | 1425.00691666667 | 0.698199570178986 | 0.248803376906318 | 0.0544610545039177 | 0.0846136703114955 | 5 |
| 1430 | 1429.99523333333 | 0.65509831905365 | 0.261773692810457 | 0.0834972634911537 | 0.231478675996414 | 5 |
| 1435 | 1435.00023333333 | 0.646852970123291 | 0.272206699346405 | 0.0950302258133888 | 0.192231173501759 | 5 |
| 1440 | 1440.00523333333 | 0.695359230041504 | 0.250655773420479 | 0.0903858914971352 | 0.209683943999956 | 5 |
| 1445 | 1444.99355 | 0.643871188163757 | 0.265984749455338 | 0.0869939997792244 | 0.257404966673841 | 5 |
| 1450 | 1449.99855 | 0.636083126068115 | 0.276921568627451 | 0.0952707007527351 | 0.20865488079514 | 5 |
| 1455 | 1455.00355 | 0.701861143112183 | 0.248354302832244 | 0.0981266275048256 | 0.217400101505879 | 5 |
| 1460 | 1459.99186666667 | 0.701562881469727 | 0.247883169934641 | 0.0333178080618382 | 0.0487902334465231 | 5 |
| 1465 | 1464.99686666667 | 0.654537379741669 | 0.257835511982571 | 0.0820277780294418 | 0.236157070779596 | 5 |
| 1470 | 1470.00186666667 | 0.646848082542419 | 0.258894063180828 | 0.02291040122509 | 0.0781388166258298 | 5 |
| 1475 | 1475.00686666667 | 0.641710817813873 | 0.273395152505447 | 0.0953164473176003 | 0.204209004097342 | 5 |
| 1480 | 1479.99518333333 | 0.670361638069153 | 0.258790305010893 | 0.105331152677536 | 0.229655283578112 | 5 |
| 1485 | 1485.00018333333 | 0.649293541908264 | 0.262427287581699 | 0.078696072101593 | 0.145611258707581 | 5 |
| 1490 | 1490.00518333333 | 0.643733203411102 | 0.264814270152505 | 0.0198948793113232 | 0.0570940461381729 | 5 |
| 1495 | 1494.9935 | 0.649983644485474 | 0.259954248366013 | 0.020494008436799 | 0.0521730721019363 | 5 |
| 1500 | 1499.9985 | 0.695680618286133 | 0.254296296296296 | 0.0752960219979286 | 0.245101238017789 | 5 |
| 1505 | 1505.0035 | 0.702722251415253 | 0.247302015250545 | 0.0442655198276043 | 0.075201968063902 | 5 |
| 1510 | 1509.99181666667 | 0.650594532489777 | 0.270630446623094 | 0.0904103964567184 | 0.20075389033369 | 5 |
| 1515 | 1514.99681666667 | 0.638437628746033 | 0.276099945533769 | 0.0288916099816561 | 0.0723302510873844 | 5 |
| 1520 | 1520.00181666667 | 0.705567896366119 | 0.247716230936819 | 0.0971285328269005 | 0.214130570070961 | 5 |
| 1525 | 1525.00681666667 | 0.645878851413727 | 0.260770969498911 | 0.0823126286268234 | 0.248186231207143 | 5 |
| 1530 | 1529.99513333333 | 0.647694528102875 | 0.260453703703704 | 0.00646432442590594 | 0.0334419342259248 | 5 |
| 1535 | 1535.00013333333 | 0.645935714244843 | 0.266711328976035 | 0.0291830059140921 | 0.0552613965618763 | 5 |
| 1540 | 1540.00513333333 | 0.676766633987427 | 0.258977668845316 | 0.0831021219491959 | 0.160885506432342 | 5 |
| 1545 | 1544.99345 | 0.669309914112091 | 0.255565087145969 | 0.0317312106490135 | 0.0669656690612352 | 5 |
| 1550 | 1549.99845 | 0.650318384170532 | 0.269699891067538 | 0.0966947078704834 | 0.22183500972782 | 5 |
| 1555 | 1555.00345 | 0.694864928722382 | 0.254140795206972 | 0.0883412286639214 | 0.185164778716558 | 5 |
| 1560 | 1559.99176666667 | 0.667227149009705 | 0.256224945533769 | 0.0792641565203667 | 0.21182931967818 | 5 |
| 1565 | 1564.99676666667 | 0.639080107212067 | 0.477876633986928 | 0.0829433500766754 | 0.505347920194948 | 5 |
| 1570 | 1570.00176666667 | 0.637220025062561 | 0.478658769063181 | 0.0037178648635745 | 0.0324926566120074 | 5 |
| 1575 | 1575.00676666667 | 0.550793051719666 | 0.31793954248366 | 0.108151413500309 | 0.539827925995656 | 5 |
| 1580 | 1579.99508333333 | 0.573454320430756 | 0.318867374727669 | 0.0421334430575371 | 0.116328666502302 | 5 |
| 1585 | 1585.00008333333 | 0.571134328842163 | 0.317657407407407 | 0.0263248905539513 | 0.0543696185304359 | 5 |
| 1590 | 1590.00508333333 | 0.572143018245697 | 0.316441448801743 | 0.025513069704175 | 0.0558208795247845 | 5 |
| 1595 | 1594.9934 | 0.595042765140533 | 0.305657407407407 | 0.0689940080046654 | 0.15737556100156 | 5 |
| 1600 | 1599.9984 | 0.593179523944855 | 0.305836328976035 | 0.0164684113115072 | 0.0348199610544213 | 5 |
| 1605 | 1605.0034 | 0.571333646774292 | 0.316511982570806 | 0.069966234266758 | 0.155611097083546 | 5 |
| 1610 | 1609.99171666667 | 0.570115685462952 | 0.317063453159041 | 0.00719389971345663 | 0.0296548676560229 | 5 |
| 1615 | 1614.99671666667 | 0.572176218032837 | 0.31888371459695 | 0.0211574081331491 | 0.0500165782279894 | 5 |
| 1620 | 1620.00171666667 | 0.569640040397644 | 0.319306917211329 | 0.0214310977607965 | 0.0431042416945379 | 5 |
| 1625 | 1625.00671666667 | 0.574079275131226 | 0.315842320261438 | 0.015668572857976 | 0.0516828154032736 | 5 |
| 1630 | 1629.99503333333 | 0.591204285621643 | 0.305083605664488 | 0.0651674792170525 | 0.154115702799119 | 5 |
| 1635 | 1635.00003333333 | 0.59101414680481 | 0.306125 | 0.0337238572537899 | 0.0426338740421639 | 5 |
| 1640 | 1640.00503333333 | 0.592783987522125 | 0.306458333333333 | 0.0222894884645939 | 0.0439737062670498 | 5 |
| 1645 | 1644.99335 | 0.591008722782135 | 0.305934095860566 | 0.0158314276486635 | 0.0400560225238932 | 5 |
| 1650 | 1649.99835 | 0.572371482849121 | 0.316395969498911 | 0.0686394348740578 | 0.160481655976222 | 5 |
| 1655 | 1655.00335 | 0.573085010051727 | 0.316860021786492 | 0.0148839866742492 | 0.0545431390617083 | 5 |
| 1660 | 1659.99166666667 | 0.57049971818924 | 0.317075435729847 | 0.0155073525384068 | 0.0538381517897375 | 5 |
| 1665 | 1664.99666666667 | 0.575830638408661 | 0.316422385620915 | 0.0217829514294863 | 0.0592330340076253 | 5 |
| 1670 | 1670.00166666667 | 0.593013346195221 | 0.307312636165577 | 0.0697807744145393 | 0.162956287606659 | 5 |
| 1675 | 1675.00666666667 | 0.595124185085297 | 0.305837690631808 | 0.019416393712163 | 0.055787638819704 | 5 |
| 1680 | 1679.99498333333 | 0.572772085666656 | 0.318417211328976 | 0.068552553653717 | 0.163919795149292 | 5 |
| 1685 | 1684.99998333333 | 0.570403635501862 | 0.318454793028322 | 0.0294332783669233 | 0.050596319562063 | 5 |
| 1690 | 1690.00498333333 | 0.577199339866638 | 0.31759068627451 | 0.0180375818163157 | 0.0456945091485538 | 5 |
| 1695 | 1694.9933 | 0.575721681118011 | 0.317515522875817 | 0.0100582791492343 | 0.0318336402177643 | 5 |
| 1700 | 1699.9983 | 0.572417557239532 | 0.316604302832244 | 0.0214986372739077 | 0.0462748954990793 | 5 |
| 1705 | 1705.0033 | 0.592540800571442 | 0.305084694989107 | 0.0669087693095207 | 0.15830919140597 | 5 |
| 1710 | 1710.0083 | 0.71194988489151 | 0.2623575708061 | 0.139220044016838 | 0.406681913019687 | 5 |
| 1715 | 1714.99661666667 | 0.703497052192688 | 0.261740468409586 | 0.0260977689176798 | 0.051091294969277 | 5 |
| 1720 | 1720.00161666667 | 0.699720859527588 | 0.262294117647059 | 0.0298191700130701 | 0.0350442015289039 | 5 |
| 1725 | 1725.00661666667 | 0.702752947807312 | 0.253442810457516 | 0.0595539174973965 | 0.179217346548639 | 5 |
| 1730 | 1729.99493333333 | 0.704451203346252 | 0.253375 | 0.0183382350951433 | 0.0319644414332551 | 5 |
| 1735 | 1734.99993333333 | 0.593772351741791 | 0.304514978213508 | 0.12770614027977 | 0.387352288035907 | 5 |
| 1740 | 1740.00493333333 | 0.594462931156158 | 0.307679466230937 | 0.0248888861387968 | 0.0465268031939539 | 5 |
| 1745 | 1744.99325 | 0.594289481639862 | 0.306962418300654 | 0.0263287033885717 | 0.0531689221201565 | 5 |
| 1750 | 1749.99825 | 0.703139960765839 | 0.264807734204793 | 0.129522606730461 | 0.400188419131173 | 5 |
| 1755 | 1755.00325 | 0.70308119058609 | 0.264645152505447 | 0.00840904098004103 | 0.0291196555335876 | 5 |
| 1760 | 1760.00825 | 0.70827579498291 | 0.258191448801743 | 0.0562949329614639 | 0.107322964785529 | 5 |
| 1765 | 1764.99656666667 | 0.709037065505981 | 0.253800381263617 | 0.0239855665713549 | 0.046858528815903 | 5 |
| 1770 | 1770.00156666667 | 0.702410936355591 | 0.266119825708061 | 0.0561696626245975 | 0.123472271040802 | 5 |
| 1775 | 1775.00656666667 | 0.701406300067902 | 0.261067538126362 | 0.0056778322905302 | 0.0643606888100178 | 5 |
| 1780 | 1779.99488333333 | 0.712573230266571 | 0.2514825708061 | 0.056502990424633 | 0.139416338066063 | 5 |
| 1785 | 1784.99988333333 | 0.708029985427856 | 0.255257897603486 | 0.0363673754036427 | 0.0672395591915594 | 5 |
| 1790 | 1790.00488333333 | 0.714738786220551 | 0.251584422657952 | 0.0368858948349953 | 0.0791728794508452 | 5 |
| 1795 | 1794.9932 | 0.706871747970581 | 0.255926198257081 | 0.0562521740794182 | 0.129244031652994 | 5 |
| 1800 | 1799.9982 | 0.705835521221161 | 0.255851307189542 | 0.00489733042195439 | 0.0216428208318355 | 5 |
| 1805 | 1805.0032 | 0.702519357204437 | 0.265841230936819 | 0.0216315351426601 | 0.0704269987895947 | 5 |
| 1810 | 1810.0082 | 0.710424065589905 | 0.258468954248366 | 0.0573796294629574 | 0.105862109512412 | 5 |
| 1815 | 1814.99651666667 | 0.623046576976776 | 0.28695234204793 | 0.112127989530563 | 0.317028213375093 | 5 |
| 1820 | 1820.00151666667 | 0.651258230209351 | 0.275402233115468 | 0.100225210189819 | 0.265432732572769 | 5 |
| 1825 | 1825.00651666667 | 0.428767442703247 | 0.352964869281046 | 0.226420477032661 | 0.451943560850455 | 5 |
| 1830 | 1829.99483333333 | 0.618273437023163 | 0.27746568627451 | 0.192316994071007 | 0.437190202607801 | 5 |
| 1835 | 1834.99983333333 | 0.602776169776917 | 0.26305174291939 | 0.111205875873566 | 0.272551926615968 | 5 |
| 1840 | 1840.00483333333 | 0.647434651851654 | 0.252988562091503 | 0.119452618062496 | 0.324779364229241 | 5 |
| 1845 | 1844.99315 | 0.645817041397095 | 0.257795751633987 | 0.0236198250204325 | 0.0666616402145266 | 5 |
| 1850 | 1849.99815 | 0.6760134100914 | 0.219268518518519 | 0.0830830559134483 | 0.218493557943092 | 5 |
| 1855 | 1855.00315 | 0.676142454147339 | 0.219071078431373 | 0.00499564269557595 | 0.0190548408765473 | 5 |
| 1860 | 1860.00815 | 0.690206408500671 | 0.224468681917211 | 0.062857560813427 | 0.134477617929786 | 5 |
| 1865 | 1864.99646666667 | 0.690256774425507 | 0.223750544662309 | 0.0120661752298474 | 0.0406544109593846 | 5 |
| 1870 | 1870.00146666667 | 0.689494550228119 | 0.230177832244009 | 0.0258575696498156 | 0.0607595096765609 | 5 |
| 1875 | 1875.00646666667 | 0.644443929195404 | 0.258562363834423 | 0.0736601278185844 | 0.225083502130947 | 5 |
| 1880 | 1879.99478333333 | 0.650717914104462 | 0.255852396514161 | 0.0317429192364216 | 0.0559178941540137 | 5 |
| 1885 | 1884.99978333333 | 0.691544413566589 | 0.223037309368192 | 0.0751211866736412 | 0.218136603687399 | 5 |
| 1890 | 1890.00478333333 | 0.647737503051758 | 0.249618736383442 | 0.0730841383337975 | 0.212032397362488 | 5 |
| 1895 | 1894.9931 | 0.648357093334198 | 0.252641067538126 | 0.0228853486478329 | 0.0898624273352599 | 5 |
| 1900 | 1899.9981 | 0.667101621627808 | 0.226489379084967 | 0.0859711319208145 | 0.199022707230941 | 5 |
| 1905 | 1905.0031 | 0.666979312896729 | 0.226794389978214 | 0.00861791893839836 | 0.0383215819246554 | 5 |
| 1910 | 1910.0081 | 0.695303976535797 | 0.226299564270152 | 0.0647919401526451 | 0.13410305568132 | 5 |
| 1915 | 1914.99641666667 | 0.638019323348999 | 0.268478213507625 | 0.0980247855186462 | 0.257580568935771 | 5 |
| 1920 | 1920.00141666667 | 0.667235553264618 | 0.227411492374728 | 0.0918736457824707 | 0.233759430624936 | 5 |
| 1925 | 1925.00641666667 | 0.705054819583893 | 0.226867919389978 | 0.0854651406407356 | 0.212294106570985 | 5 |
| 1930 | 1929.99473333333 | 0.664195001125336 | 0.22943954248366 | 0.0863602980971336 | 0.213862847322221 | 5 |
| 1935 | 1934.99973333333 | 0.629642188549042 | 0.275264161220044 | 0.0896759256720543 | 0.242318997107796 | 5 |
| 1940 | 1940.00473333333 | 0.662992358207703 | 0.230905501089325 | 0.0883812606334686 | 0.241713034289776 | 5 |
| 1945 | 1944.99305 | 0.663157165050507 | 0.230073529411765 | 0.0153303379192948 | 0.042953259598992 | 5 |
| 1950 | 1949.99805 | 0.68688702583313 | 0.237166938997821 | 0.0651214495301247 | 0.139239472976567 | 5 |
| 1955 | 1955.00305 | 0.665869295597076 | 0.227993736383442 | 0.0654436275362968 | 0.142911811729937 | 5 |
| 1960 | 1960.00805 | 0.639048278331757 | 0.274265250544662 | 0.0866674780845642 | 0.240556627483535 | 5 |
| 1965 | 1964.99636666667 | 0.628695249557495 | 0.277693355119826 | 0.0198867097496986 | 0.0502639431872137 | 5 |
| 1970 | 1970.00136666667 | 0.629608154296875 | 0.276766612200436 | 0.0195196066051722 | 0.0376408846352486 | 5 |
| 1975 | 1975.00636666667 | 0.642934620380402 | 0.269313453159041 | 0.0304044112563133 | 0.0581993458621955 | 5 |
| 1980 | 1979.99468333333 | 0.709354877471924 | 0.222265522875817 | 0.10121051222086 | 0.22865036719571 | 5 |
| 1985 | 1984.99968333333 | 0.685536742210388 | 0.230829793028322 | 0.0676421523094177 | 0.169178067501599 | 5 |
| 1990 | 1990.00468333333 | 0.688343167304993 | 0.232542483660131 | 0.0314436256885529 | 0.0451063326499359 | 5 |
| 1995 | 1994.993 | 0.631241321563721 | 0.275802015250545 | 0.106302827596664 | 0.245056644804174 | 5 |
| 2000 | 1999.998 | 0.632689535617828 | 0.27762091503268 | 0.0198801718652248 | 0.0425432623826331 | 5 |
| 2005 | 2005.003 | 0.686414241790771 | 0.231902777777778 | 0.104561820626259 | 0.246610649125755 | 5 |
| 2010 | 2010.008 | 0.637499988079071 | 0.268397603485839 | 0.101856485009193 | 0.234576133303665 | 5 |
| 2015 | 2014.99631666667 | 0.643709182739258 | 0.2692151416122 | 0.028133986517787 | 0.0564365460827569 | 5 |
| 2020 | 2020.00131666667 | 0.711318373680115 | 0.222377450980392 | 0.103593952953815 | 0.234580413028651 | 5 |
| 2025 | 2025.00631666667 | 0.685495376586914 | 0.23182325708061 | 0.0784498825669289 | 0.168468618752251 | 5 |
| 2030 | 2029.99463333333 | 0.659929215908051 | 0.231139978213508 | 0.0693799033761024 | 0.1210626998199 | 5 |
| 2035 | 2034.99963333333 | 0.627342104911804 | 0.364379357298475 | 0.0861094668507576 | 0.407544937331871 | 5 |
| 2040 | 2040.00463333333 | 0.786392986774445 | 0.179724128540305 | 0.159898415207863 | 0.513428227816402 | 5 |
| 2045 | 2044.99295 | 0.663704037666321 | 0.229406590413943 | 0.123550109565258 | 0.335474736791047 | 5 |
| 2050 | 2049.99795 | 0.684734284877777 | 0.231583605664488 | 0.0659327283501625 | 0.121306835665393 | 5 |
| 2055 | 2055.00295 | 0.682949721813202 | 0.240297930283224 | 0.0284937340766191 | 0.0722801716983988 | 5 |
| 2060 | 2060.00795 | 0.631087422370911 | 0.276076525054466 | 0.105111099779606 | 0.260299217407384 | 5 |
| 2065 | 2064.99626666667 | 0.638373374938965 | 0.268285130718954 | 0.0255773421376944 | 0.0449699957415057 | 5 |
| 2070 | 2070.00126666667 | 0.629464626312256 | 0.275957516339869 | 0.0274675916880369 | 0.0442982561893255 | 5 |
| 2075 | 2075.00626666667 | 0.629738032817841 | 0.271398420479303 | 0.00625653518363833 | 0.067770443706939 | 5 |
| 2080 | 2079.99458333333 | 0.667433023452759 | 0.229438725490196 | 0.088711328804493 | 0.236489290990863 | 5 |
| 2085 | 2084.99958333333 | 0.663805544376373 | 0.225608932461874 | 0.0182472765445709 | 0.072369209047188 | 5 |
| 2090 | 2090.00458333333 | 0.696052491664886 | 0.22569362745098 | 0.0661010295152664 | 0.154026042338873 | 5 |
| 2095 | 2094.9929 | 0.696042776107788 | 0.225930010893246 | 0.00428594788536429 | 0.0319702913853728 | 5 |
| 2100 | 2099.9979 | 0.638446927070618 | 0.272022058823529 | 0.0975544601678848 | 0.251838225548676 | 5 |
| 2105 | 2105.0029 | 0.643305838108063 | 0.269634259259259 | 0.0293894317001104 | 0.0497486523006173 | 5 |
| 2110 | 2110.0079 | 0.642482280731201 | 0.265617374727669 | 0.00814869254827499 | 0.0664061555711974 | 5 |
| 2115 | 2114.99621666667 | 0.711809635162354 | 0.222106753812636 | 0.105037577450275 | 0.24521238929929 | 5 |
| 2120 | 2120.00121666667 | 0.709084987640381 | 0.223445533769063 | 0.0333178080618382 | 0.0458820452962944 | 5 |
| 2125 | 2125.00621666667 | 0.708227694034576 | 0.219979575163399 | 0.0219814814627171 | 0.0741773054187601 | 5 |
| 2130 | 2129.99453333333 | 0.642299890518188 | 0.271235566448802 | 0.104256801307201 | 0.243865628294924 | 5 |
| 2135 | 2134.99953333333 | 0.632781028747559 | 0.275858660130719 | 0.0269670486450195 | 0.0487464309365597 | 5 |
| 2140 | 2140.00453333333 | 0.630033493041992 | 0.271339324618736 | 0.00664733164012432 | 0.0669515470352808 | 5 |
| 2145 | 2144.99285 | 0.697536468505859 | 0.232050925925926 | 0.0972704216837883 | 0.256539345298246 | 5 |
| 2150 | 2149.99785 | 0.692247807979584 | 0.236186274509804 | 0.0406476035714149 | 0.0504057263866846 | 5 |
| 2155 | 2155.00285 | 0.695226311683655 | 0.228800108932462 | 0.0390852391719818 | 0.0770471179517187 | 5 |
| 2160 | 2160.00785 | 0.66834944486618 | 0.223056644880174 | 0.0699008703231812 | 0.151114402226923 | 5 |
| 2165 | 2164.99616666667 | 0.664990246295929 | 0.23023720043573 | 0.0187867656350136 | 0.067647552684028 | 5 |
| 2170 | 2170.00116666667 | 0.66529393196106 | 0.225503812636166 | 0.0056516882032156 | 0.0609053276217872 | 5 |
| 2175 | 2175.00616666667 | 0.692865192890167 | 0.230093409586057 | 0.0655217841267586 | 0.152110501482558 | 5 |
| 2180 | 2179.99448333333 | 0.664486706256866 | 0.225804738562091 | 0.0617815852165222 | 0.149348653223599 | 5 |
| 2185 | 2184.99948333333 | 0.666984975337982 | 0.224380174291939 | 0.0193011965602636 | 0.0431927962857328 | 5 |
| 2190 | 2190.00448333333 | 0.663213491439819 | 0.233701797385621 | 0.0242295749485493 | 0.0765621861500466 | 5 |
| 2195 | 2194.9928 | 0.664519608020782 | 0.230109749455338 | 0.0235789734870195 | 0.0444539908469033 | 5 |
| 2200 | 2199.9978 | 0.695430040359497 | 0.225367102396514 | 0.0606478713452816 | 0.131128940682348 | 5 |
| 2205 | 2205.0028 | 0.695210516452789 | 0.225484477124183 | 0.0074526141397655 | 0.0311570665880105 | 5 |
| 2210 | 2210.0078 | 0.694262802600861 | 0.231570806100218 | 0.0190593674778938 | 0.0551834451460985 | 5 |
| 2215 | 2214.99611666667 | 0.691514134407043 | 0.229851307189542 | 0.0264980923384428 | 0.050666627802163 | 5 |
| 2220 | 2220.00111666667 | 0.674143016338348 | 0.270890522875817 | 0.0727807730436325 | 0.257096747977441 | 5 |
| 2225 | 2225.00611666667 | 0.689861953258514 | 0.268785675381264 | 0.0280833300203085 | 0.104007063063151 | 5 |
| 2230 | 2229.99443333333 | 0.686025142669678 | 0.265052287581699 | 0.018775325268507 | 0.0690471430002425 | 5 |
| 2235 | 2234.99943333333 | 0.700689852237701 | 0.265412309368192 | 0.0655438452959061 | 0.140665874971975 | 5 |
| 2240 | 2240.00443333333 | 0.699430048465729 | 0.265954520697168 | 0.00796241778880358 | 0.0375962887014201 | 5 |
| 2245 | 2244.99275 | 0.705449879169464 | 0.262453431372549 | 0.0242382902652025 | 0.0491796396535052 | 5 |
| 2250 | 2249.99775 | 0.692830860614777 | 0.261885893246187 | 0.0649256557226181 | 0.124896504544153 | 5 |
| 2255 | 2255.00275 | 0.687749683856964 | 0.270229030501089 | 0.0179896503686905 | 0.0718799697558861 | 5 |
| 2260 | 2260.00775 | 0.686629354953766 | 0.26559885620915 | 0.00802614353597164 | 0.0655422956551924 | 5 |
| 2265 | 2264.99606666667 | 0.686213791370392 | 0.265585239651416 | 0.00532080559059978 | 0.0296790468306452 | 5 |
| 2270 | 2270.00106666667 | 0.701611399650574 | 0.260075708061002 | 0.0653649196028709 | 0.121902652768231 | 5 |
| 2275 | 2275.00606666667 | 0.686626374721527 | 0.27093082788671 | 0.0651582255959511 | 0.129229258715073 | 5 |
| 2280 | 2279.99438333333 | 0.687742650508881 | 0.265807734204793 | 0.00570016354322433 | 0.0668154733694573 | 5 |
| 2285 | 2284.99938333333 | 0.704326570034027 | 0.2635901416122 | 0.0650686249136925 | 0.13074907515185 | 5 |
| 2290 | 2290.00438333333 | 0.706338047981262 | 0.263827614379085 | 0.0259090401232243 | 0.0466445933183728 | 5 |
| 2295 | 2294.9927 | 0.705924093723297 | 0.263593681917211 | 0.0100735295563936 | 0.0405684865404342 | 5 |
| 2300 | 2299.9977 | 0.687686860561371 | 0.265863017429194 | 0.0649310946464539 | 0.137415771469247 | 5 |
| 2305 | 2305.0027 | 0.68646514415741 | 0.265957788671024 | 0.016264159232378 | 0.0400191476967369 | 5 |
| 2310 | 2310.0077 | 0.686751663684845 | 0.270964324618736 | 0.00453812582418323 | 0.0677878726085662 | 5 |
| 2315 | 2314.99601666667 | 0.703555762767792 | 0.264027777777778 | 0.0657039731740952 | 0.120764374379186 | 5 |
| 2320 | 2320.00101666667 | 0.690891563892365 | 0.263862472766885 | 0.0639163851737976 | 0.129885465156204 | 5 |
| 2325 | 2325.00601666667 | 0.708431661128998 | 0.258665032679739 | 0.0642110556364059 | 0.125028550243311 | 5 |
| 2330 | 2329.99433333333 | 0.696214318275452 | 0.261432734204793 | 0.025313725695014 | 0.0768724418013971 | 5 |
| 2335 | 2334.99933333333 | 0.684679508209229 | 0.265865468409586 | 0.0667309314012527 | 0.118957543862043 | 5 |
| 2340 | 2340.00433333333 | 0.683916091918945 | 0.265626633986928 | 0.00678404048085213 | 0.0313302179104883 | 5 |
| 2345 | 2344.99265 | 0.684289216995239 | 0.270560185185185 | 0.00460566394031048 | 0.0628866470944768 | 5 |
| 2350 | 2349.99765 | 0.684759020805359 | 0.270470315904139 | 0.00759613234549761 | 0.0344548082931761 | 5 |
| 2355 | 2355.00265 | 0.697268784046173 | 0.26546105664488 | 0.0650702565908432 | 0.121317565580728 | 5 |
| 2360 | 2360.00765 | 0.696550130844116 | 0.266386165577342 | 0.0203848015516996 | 0.0482165495827549 | 5 |
| 2365 | 2364.99596666667 | 0.69536817073822 | 0.266540032679739 | 0.00939270108938217 | 0.0473052370937311 | 5 |
| 2370 | 2370.00096666667 | 0.684005439281464 | 0.265961873638344 | 0.0660528242588043 | 0.130068152741082 | 5 |
| 2375 | 2375.00596666667 | 0.685054540634155 | 0.270541938997821 | 0.00741230975836515 | 0.0658446116517773 | 5 |
| 2380 | 2379.99428333333 | 0.6960569024086 | 0.266235838779956 | 0.0657497271895409 | 0.116911177061338 | 5 |
| 2385 | 2384.99928333333 | 0.685521602630615 | 0.270020697167756 | 0.0646884515881538 | 0.111984498072002 | 5 |
| 2390 | 2390.00428333333 | 0.632455110549927 | 0.268485021786492 | 0.062714047729969 | 0.313505259093761 | 5 |
| 2395 | 2394.9926 | 0.689521610736847 | 0.265986383442266 | 0.0595479272305965 | 0.320469511643071 | 5 |
| 2400 | 2399.9976 | 0.689518213272095 | 0.265847766884532 | 0.00309749436564744 | 0.0225096295671701 | 5 |
| 2405 | 2405.0026 | 0.642532408237457 | 0.459830337690632 | 0.0915767922997475 | 0.514202393674712 | 5 |
| 2410 | 2410.0076 | 0.642671585083008 | 0.460497821350763 | 0.00177641620393842 | 0.0232637517143068 | 5 |
| 2415 | 2414.99591666667 | 0.642420172691345 | 0.460548747276688 | 0.00305147073231637 | 0.0217016611765051 | 5 |
| 2420 | 2420.00091666667 | 0.642857313156128 | 0.46033605664488 | 0.00347957503981888 | 0.0232879913634073 | 5 |
| 2425 | 2425.00591666667 | 0.642016410827637 | 0.460471677559913 | 0.00395261403173208 | 0.0236584486308224 | 5 |
| 2430 | 2429.99423333333 | 0.643539786338806 | 0.460482843137255 | 0.00360566424205899 | 0.0243319275344507 | 5 |
| 2435 | 2434.99923333333 | 0.643604338169098 | 0.460511437908497 | 0.00260321353562176 | 0.0230521633262727 | 5 |
| 2440 | 2440.00423333333 | 0.642391085624695 | 0.460518246187364 | 0.00335974968038499 | 0.0231760431000659 | 5 |
| 2445 | 2444.99255 | 0.64348042011261 | 0.460692265795207 | 0.00329139409586787 | 0.0252364319543715 | 5 |
| 2450 | 2449.99755 | 0.642659664154053 | 0.460309368191721 | 0.00237037055194378 | 0.0271775787217526 | 5 |
| 2455 | 2455.00255 | 0.641730964183807 | 0.460386437908497 | 0.00187037012074143 | 0.00634793654708763 | 5 |
| 2460 | 2460.00755 | 0.638328731060028 | 0.478723583877996 | 0.00764624169096351 | 0.0959554973887045 | 5 |
| 2465 | 2464.99586666667 | 0.704601109027863 | 0.254724128540305 | 0.10019226372242 | 0.530621187769519 | 5 |
| 2470 | 2470.00086666667 | 0.64416778087616 | 0.460200163398693 | 0.100000813603401 | 0.506907052533197 | 5 |
| 2475 | 2475.00586666667 | 0.642495095729828 | 0.460187908496732 | 0.00345751619897783 | 0.0315078160067427 | 5 |
| 2480 | 2479.99418333333 | 0.642378568649292 | 0.460505991285403 | 0.00303867110051215 | 0.0265207539451015 | 5 |
| 2485 | 2484.99918333333 | 0.644378244876862 | 0.460381535947712 | 0.00355201517231762 | 0.0244276536240847 | 5 |
| 2490 | 2490.00418333333 | 0.64382404088974 | 0.460519607843137 | 0.00211574067361653 | 0.0230715150917422 | 5 |
| 2495 | 2494.9925 | 0.643604576587677 | 0.46037091503268 | 0.00225980393588543 | 0.0245378787974038 | 5 |
| 2500 | 2499.9975 | 0.725703477859497 | 0.241983932461874 | 0.100916385650635 | 0.487224556327048 | 5 |
| 2505 | 2505.0025 | 0.688218712806702 | 0.270485021786492 | 0.0635228753089905 | 0.259074933932035 | 5 |
| 2510 | 2510.0075 | 0.704849720001221 | 0.264376906318083 | 0.0650639981031418 | 0.121383585979748 | 5 |
| 2515 | 2514.99581666667 | 0.703997015953064 | 0.257833877995643 | 0.027356481179595 | 0.0758996622510532 | 5 |
| 2520 | 2520.00081666667 | 0.687771022319794 | 0.265333605664488 | 0.0679460763931274 | 0.125435122229777 | 5 |
| 2525 | 2525.00581666667 | 0.689508736133575 | 0.268005174291939 | 0.0207562632858753 | 0.0699287922491026 | 5 |
| 2530 | 2529.99413333333 | 0.689071655273438 | 0.268691176470588 | 0.0187584403902292 | 0.0355881651539831 | 5 |
| 2535 | 2534.99913333333 | 0.699973285198212 | 0.265083333333333 | 0.0644485279917717 | 0.122760181956904 | 5 |
| 2540 | 2540.00413333333 | 0.70032787322998 | 0.265591503267974 | 0.00854629557579756 | 0.0387587567237046 | 5 |
| 2545 | 2544.99245 | 0.701148927211761 | 0.264704793028322 | 0.00900462921708822 | 0.0390848697636749 | 5 |
| 2550 | 2549.99745 | 0.704616010189056 | 0.263407679738562 | 0.0302976574748755 | 0.0561748234906065 | 5 |
| 2555 | 2555.00245 | 0.686712980270386 | 0.265533769063181 | 0.0671726539731026 | 0.130268574497943 | 5 |
| 2560 | 2560.00745 | 0.704531669616699 | 0.259890522875817 | 0.0656105652451515 | 0.123641917135517 | 5 |
| 2565 | 2564.99576666667 | 0.690777003765106 | 0.267474128540305 | 0.0638739094138145 | 0.132337008070892 | 5 |
| 2570 | 2570.00076666667 | 0.689458072185516 | 0.268199891067538 | 0.0181582234799862 | 0.0389091719232197 | 5 |
| 2575 | 2575.00576666667 | 0.689995646476746 | 0.263466230936819 | 0.00553594809025526 | 0.0654725098087353 | 5 |
| 2580 | 2579.99408333333 | 0.68703430891037 | 0.269940359477124 | 0.01863126270473 | 0.068418252767667 | 5 |
| 2585 | 2584.99908333333 | 0.705542266368866 | 0.264065359477124 | 0.066104844212532 | 0.13471224047711 | 5 |
| 2590 | 2590.00408333333 | 0.648451268672943 | 0.296062363834423 | 0.095081701874733 | 0.460119040049486 | 5 |
| 2595 | 2594.9924 | 0.464209735393524 | 0.375316721132898 | 0.186810716986656 | 0.457826196253951 | 5 |
| 2600 | 2599.9974 | 0.463834702968597 | 0.379420751633987 | 0.0297105107456446 | 0.0629156097417668 | 5 |
| 2605 | 2605.0024 | 0.530307769775391 | 0.365385348583878 | 0.0956979766488075 | 0.369091006902177 | 5 |
| 2610 | 2610.0074 | 0.539434134960175 | 0.35361165577342 | 0.0331230908632278 | 0.0854160504732406 | 5 |
| 2615 | 2614.99571666667 | 0.532394886016846 | 0.364829248366013 | 0.0176345314830542 | 0.0836520647183826 | 5 |
| 2620 | 2620.00071666667 | 0.476852416992188 | 0.386366557734205 | 0.10522385686636 | 0.367858958622971 | 5 |
| 2625 | 2625.00571666667 | 0.62277889251709 | 0.302064814814815 | 0.155383974313736 | 0.443372984666676 | 5 |
| 2630 | 2629.99403333333 | 0.543146252632141 | 0.368874455337691 | 0.10009340941906 | 0.365264845854108 | 5 |
| 2635 | 2634.99903333333 | 0.541207253932953 | 0.375808006535948 | 0.0381312631070614 | 0.107142688794812 | 5 |
| 2640 | 2640.00403333333 | 0.669413626194 | 0.272525871459695 | 0.13513670861721 | 0.349728162695021 | 5 |
| 2645 | 2644.99235 | 0.712614953517914 | 0.243350490196078 | 0.073921836912632 | 0.405730889960555 | 5 |
| 2650 | 2649.99735 | 0.506295502185822 | 0.253675381263617 | 0.229201793670654 | 0.432580414917118 | 5 |
| 2655 | 2655.00235 | 0.555728197097778 | 0.328596405228758 | 0.128682732582092 | 0.369778010626751 | 5 |
| 2660 | 2660.00735 | 0.582432448863983 | 0.310379357298475 | 0.0978066474199295 | 0.128406435379023 | 5 |
| 2665 | 2664.99566666667 | 0.417246729135513 | 0.50694417211329 | 0.166169390082359 | 0.413800820196919 | 5 |
| 2670 | 2670.00066666667 | 0.576736390590668 | 0.324328703703704 | 0.160021245479584 | 0.499947127315713 | 5 |
| 2675 | 2675.00566666667 | 0.548835277557373 | 0.314906318082789 | 0.124143518507481 | 0.36164363714761 | 5 |
| 2680 | 2679.99398333333 | 0.602755665779114 | 0.260732298474946 | 0.132432997226715 | 0.252530810982157 | 5 |
| 2685 | 2684.99898333333 | 0.644401967525482 | 0.266453159041394 | 0.126812890172005 | 0.22634833692261 | 5 |
| 2690 | 2690.00398333333 | 0.609390258789062 | 0.296383986928105 | 0.0883798971772194 | 0.195007738230939 | 5 |
| 2695 | 2694.9923 | 0.610594511032104 | 0.295544662309368 | 0.0577636174857616 | 0.0640907298026722 | 5 |
| 2700 | 2699.9973 | 0.621866345405579 | 0.276290032679739 | 0.0817124098539352 | 0.209529861217238 | 5 |
| 2705 | 2705.0023 | 0.665590405464172 | 0.230097222222222 | 0.132284581661224 | 0.234899525023564 | 5 |
| 2710 | 2710.0073 | 0.635524809360504 | 0.272145697167756 | 0.127827063202858 | 0.232522536063875 | 5 |
| 2715 | 2714.99561666667 | 0.625971436500549 | 0.278324891067538 | 0.0980871394276619 | 0.183418862051521 | 5 |
| 2720 | 2720.00061666667 | 0.647123634815216 | 0.267299291938998 | 0.0977344736456871 | 0.227152351794207 | 5 |
| 2725 | 2725.00561666667 | 0.599448263645172 | 0.288735294117647 | 0.0998856201767921 | 0.199077073095916 | 5 |
| 2730 | 2729.99393333333 | 0.649278879165649 | 0.250957244008715 | 0.085667759180069 | 0.235524428363226 | 5 |
| 2735 | 2734.99893333333 | 0.635164499282837 | 0.283677832244009 | 0.105573527514935 | 0.282638743666082 | 5 |
| 2740 | 2740.00393333333 | 0.646247267723083 | 0.259069444444444 | 0.124856203794479 | 0.177641064195667 | 5 |
| 2745 | 2744.99225 | 0.623035132884979 | 0.281203159041394 | 0.073479026556015 | 0.186079612823002 | 5 |
| 2750 | 2749.99725 | 0.620091021060944 | 0.283423747276688 | 0.0308406874537468 | 0.0827474230455949 | 5 |
| 2755 | 2755.00225 | 0.633386969566345 | 0.252665032679739 | 0.125097215175629 | 0.209911364405952 | 5 |
| 2760 | 2760.00725 | 0.636914193630219 | 0.252402505446623 | 0.046660128980875 | 0.0785871777811521 | 5 |
| 2765 | 2764.99556666667 | 0.67738538980484 | 0.236109477124183 | 0.124284856021404 | 0.191812031978591 | 5 |
| 2770 | 2770.00056666667 | 0.656353235244751 | 0.264330065359477 | 0.103930272161961 | 0.206338523235506 | 5 |
| 2775 | 2775.00556666667 | 0.6557377576828 | 0.260673202614379 | 0.0679754838347435 | 0.0735993073765242 | 5 |
| 2780 | 2779.99388333333 | 0.53778487443924 | 0.31238779956427 | 0.134413123130798 | 0.298348053189798 | 5 |
| 2785 | 2784.99888333333 | 0.506519913673401 | 0.332868191721133 | 0.0606462433934212 | 0.223128205013974 | 5 |
| 2790 | 2790.00388333333 | 0.657278060913086 | 0.276380446623094 | 0.156836032867432 | 0.435165056627896 | 5 |
| 2795 | 2794.9922 | 0.633392989635468 | 0.267992374727669 | 0.133400321006775 | 0.324380760035948 | 5 |
| 2800 | 2799.9972 | 0.653531849384308 | 0.260653594771242 | 0.104980923235416 | 0.184327828396583 | 5 |
| 2805 | 2805.0022 | 0.607678711414337 | 0.26676279956427 | 0.102671295404434 | 0.203378463972911 | 5 |
| 2810 | 2810.0072 | 0.628166139125824 | 0.265799564270152 | 0.127149239182472 | 0.218514196124307 | 5 |
| 2815 | 2814.99551666667 | 0.589479029178619 | 0.295148420479303 | 0.12933686375618 | 0.188423519552163 | 5 |
| 2820 | 2820.00051666667 | 0.534655511379242 | 0.380992374727669 | 0.116452619433403 | 0.279246890539396 | 5 |
| 2825 | 2825.00551666667 | 0.619959473609924 | 0.271285130718954 | 0.151361122727394 | 0.365964726140922 | 5 |
| 2830 | 2829.99383333333 | 0.545462727546692 | 0.288386982570806 | 0.102205336093903 | 0.298687156651002 | 5 |
| 2835 | 2834.99883333333 | 0.612224400043488 | 0.361821078431373 | 0.104151681065559 | 0.433446190743646 | 5 |
| 2840 | 2840.00383333333 | 0.68327122926712 | 0.252794662309368 | 0.113525591790676 | 0.430026540474605 | 5 |
| 2845 | 2844.99215 | 0.659257352352142 | 0.257617102396514 | 0.0845215171575546 | 0.226193603720656 | 5 |
| 2850 | 2849.99715 | 0.655894637107849 | 0.265396241830065 | 0.0793115422129631 | 0.179412150536811 | 5 |
| 2855 | 2855.00215 | 0.655476868152618 | 0.236084422657952 | 0.0839493423700333 | 0.214029236158776 | 5 |
| 2860 | 2860.00715 | 0.633285403251648 | 0.248183823529412 | 0.108135342597961 | 0.187171933787703 | 5 |
| 2865 | 2864.99546666667 | 0.650645673274994 | 0.254744281045752 | 0.107721395790577 | 0.17882915668574 | 5 |
| 2870 | 2870.00046666667 | 0.629870355129242 | 0.2697151416122 | 0.088218130171299 | 0.266641321617557 | 5 |
| 2875 | 2875.00546666667 | 0.50992077589035 | 0.409467864923747 | 0.14434939622879 | 0.406214374665637 | 5 |
| 2880 | 2879.99378333333 | 0.630123436450958 | 0.264504357298475 | 0.134673744440079 | 0.432089939262444 | 5 |
| 2885 | 2884.99878333333 | 0.672912061214447 | 0.249879357298475 | 0.104440629482269 | 0.21541465197188 | 5 |
| 2890 | 2890.00378333333 | 0.629672467708588 | 0.255097766884532 | 0.102303363382816 | 0.213134062261732 | 5 |
| 2895 | 2894.9921 | 0.642814040184021 | 0.291241557734205 | 0.133007615804672 | 0.242557277259543 | 5 |
| 2900 | 2899.9971 | 0.617504894733429 | 0.271912309368192 | 0.135268241167068 | 0.291472175799232 | 5 |
| 2905 | 2905.0021 | 0.66131591796875 | 0.25602559912854 | 0.112574614584446 | 0.247420446175923 | 5 |
| 2910 | 2910.0071 | 0.651589632034302 | 0.238560729847495 | 0.125099942088127 | 0.203560600775176 | 5 |
| 2915 | 2914.99541666667 | 0.533920228481293 | 0.304037037037037 | 0.13581807911396 | 0.315181540630452 | 5 |
| 2920 | 2920.00041666667 | 0.672300696372986 | 0.248523965141612 | 0.164718672633171 | 0.378045441052994 | 5 |
| 2925 | 2925.00541666667 | 0.610795497894287 | 0.263171296296296 | 0.130608662962914 | 0.241204267899064 | 5 |
| 2930 | 2929.99373333333 | 0.545700192451477 | 0.359752178649237 | 0.121969506144524 | 0.316772753143373 | 5 |
| 2935 | 2934.99873333333 | 0.654635071754456 | 0.261292755991285 | 0.159548744559288 | 0.370052239394394 | 5 |
| 2940 | 2940.00373333333 | 0.637493193149567 | 0.285114923747277 | 0.0881190076470375 | 0.254037276834774 | 5 |
| 2945 | 2944.99205 | 0.54538893699646 | 0.287035675381264 | 0.101674027740955 | 0.34733444765106 | 5 |
| 2950 | 2949.99705 | 0.634517967700958 | 0.292477941176471 | 0.102466225624084 | 0.359001434321007 | 5 |
| 2955 | 2955.00205 | 0.542832255363464 | 0.377615740740741 | 0.128937363624573 | 0.349941635165702 | 5 |
| 2960 | 2960.00705 | 0.630162596702576 | 0.282285947712418 | 0.121243186295033 | 0.315487979818169 | 5 |
| 2965 | 2964.99536666667 | 0.635484218597412 | 0.281889978213508 | 0.0637883916497231 | 0.0685556460017769 | 5 |
| 2970 | 2970.00036666667 | 0.636517941951752 | 0.286960239651416 | 0.0942118689417839 | 0.247916560325434 | 5 |
| 2975 | 2975.00536666667 | 0.547317862510681 | 0.375456154684096 | 0.122641891241074 | 0.324413289906411 | 5 |
| 2980 | 2979.99368333333 | 0.65069717168808 | 0.270619825708061 | 0.138310715556145 | 0.306501007875048 | 5 |
| 2985 | 2984.99868333333 | 0.619157731533051 | 0.307830065359477 | 0.103213772177696 | 0.322970685862254 | 5 |
| 2990 | 2990.00368333333 | 0.612760126590729 | 0.309247276688453 | 0.0900479331612587 | 0.339264622746958 | 5 |
| 2995 | 2994.992 | 0.615523397922516 | 0.313029956427015 | 0.0821625739336014 | 0.232039772269462 | 5 |
| 3000 | 2999.997 | 0.686371982097626 | 0.265522058823529 | 0.130383983254433 | 0.39113027454351 | 5 |
| 3005 | 3005.002 | 0.668838500976562 | 0.25030582788671 | 0.10148011893034 | 0.281526154893171 | 5 |
| 3010 | 3010.007 | 0.631063461303711 | 0.301036764705882 | 0.10480173677206 | 0.273668202330255 | 5 |
| 3015 | 3014.99531666667 | 0.622581124305725 | 0.283958877995643 | 0.0927513614296913 | 0.250187655539504 | 5 |
| 3020 | 3020.00031666667 | 0.587377429008484 | 0.346212418300654 | 0.0904618725180626 | 0.274153183135667 | 5 |
| 3025 | 3025.00531666667 | 0.609297156333923 | 0.299179738562092 | 0.0878395959734917 | 0.231621957916778 | 5 |
| 3030 | 3029.99363333333 | 0.656029462814331 | 0.252753812636166 | 0.152298733592033 | 0.302952685024141 | 5 |
| 3035 | 3034.99863333333 | 0.64753133058548 | 0.249264705882353 | 0.136455059051514 | 0.290883617631846 | 5 |
| 3040 | 3040.00363333333 | 0.664271771907806 | 0.228740740740741 | 0.0791609361767769 | 0.218204583322854 | 5 |
| 3045 | 3044.99195 | 0.668209612369537 | 0.229591230936819 | 0.0262293014675379 | 0.0520456536521074 | 5 |
| 3050 | 3049.99695 | 0.646416127681732 | 0.250920479302832 | 0.0804444402456284 | 0.209272672533041 | 5 |
| 3055 | 3055.00195 | 0.653555929660797 | 0.230986111111111 | 0.0680503770709038 | 0.215906787750148 | 5 |
| 3060 | 3060.00695 | 0.707616209983826 | 0.261540849673203 | 0.0871318057179451 | 0.343475226117018 | 5 |
| 3065 | 3064.99526666667 | 0.688513576984406 | 0.263851034858388 | 0.0657312124967575 | 0.130494189296178 | 5 |
| 3070 | 3070.00026666667 | 0.686539173126221 | 0.263990196078431 | 0.00658823503181338 | 0.0288256539216825 | 5 |
| 3075 | 3075.00526666667 | 0.705786526203156 | 0.262700708061002 | 0.0678071901202202 | 0.132199951331208 | 5 |
| 3080 | 3079.99358333333 | 0.702675104141235 | 0.266881535947712 | 0.0169697701931 | 0.0461339347713139 | 5 |
| 3085 | 3084.99858333333 | 0.691201865673065 | 0.267868191721133 | 0.0645201429724693 | 0.116395005861933 | 5 |
| 3090 | 3090.00358333333 | 0.686603248119354 | 0.269949891067538 | 0.0184226594865322 | 0.0450285018441405 | 5 |
| 3095 | 3094.9919 | 0.704868972301483 | 0.26363371459695 | 0.0651819184422493 | 0.119714071661237 | 5 |
| 3100 | 3099.9969 | 0.703624188899994 | 0.264147058823529 | 0.0286435168236494 | 0.0531001654980391 | 5 |
| 3105 | 3105.0019 | 0.69099622964859 | 0.263219498910675 | 0.0637064278125763 | 0.125913458072196 | 5 |
| 3110 | 3110.0069 | 0.687427580356598 | 0.264502723311547 | 0.00765141611918807 | 0.0373244041372121 | 5 |
| 3115 | 3114.99521666667 | 0.702194392681122 | 0.264735566448802 | 0.0644907355308533 | 0.131963933955393 | 5 |
| 3120 | 3120.00021666667 | 0.686297655105591 | 0.265699074074074 | 0.0658766329288483 | 0.127076420425827 | 5 |
| 3125 | 3125.00521666667 | 0.6871258020401 | 0.270747004357298 | 0.0152873089537024 | 0.0692040950492551 | 5 |
| 3130 | 3129.99353333333 | 0.700761735439301 | 0.265349128540305 | 0.0655874162912369 | 0.12904925071725 | 5 |
| 3135 | 3134.99853333333 | 0.700569272041321 | 0.264882080610022 | 0.0161456950008869 | 0.0454993233469129 | 5 |
| 3140 | 3140.00353333333 | 0.687530815601349 | 0.269796840958606 | 0.0656141042709351 | 0.115928956509287 | 5 |
| 3145 | 3144.99185 | 0.688342809677124 | 0.269057189542484 | 0.0162701513618231 | 0.0361338031171555 | 5 |
| 3150 | 3149.99685 | 0.704767465591431 | 0.264418300653595 | 0.0663875266909599 | 0.112890229620619 | 5 |
| 3155 | 3155.00185 | 0.68967217206955 | 0.26380174291939 | 0.0674330070614815 | 0.122428343356598 | 5 |
| 3160 | 3160.00685 | 0.68690824508667 | 0.26447385620915 | 0.0199665036052465 | 0.0366724449450277 | 5 |
| 3165 | 3164.99516666667 | 0.600888967514038 | 0.242144335511983 | 0.122207775712013 | 0.384986085777465 | 5 |
| 3170 | 3170.00016666667 | 0.689001083374023 | 0.269047385620915 | 0.123712956905365 | 0.398239946325102 | 5 |
| 3175 | 3175.00516666667 | 0.702729642391205 | 0.266131263616558 | 0.0653325170278549 | 0.125634519149667 | 5 |
| 3180 | 3179.99348333333 | 0.70214706659317 | 0.266934368191721 | 0.0132600767537951 | 0.0410907476770213 | 5 |
| 3185 | 3184.99848333333 | 0.690659046173096 | 0.262769880174292 | 0.0651840940117836 | 0.131558204775313 | 5 |
| 3190 | 3190.00348333333 | 0.688914239406586 | 0.270380991285403 | 0.0149049554020166 | 0.0694551139869474 | 5 |
| 3195 | 3194.9918 | 0.690876603126526 | 0.268529956427015 | 0.0144656859338284 | 0.0371878182417363 | 5 |
| 3200 | 3199.9968 | 0.702599704265594 | 0.260350490196078 | 0.0639474391937256 | 0.132201738790481 | 5 |
| 3205 | 3205.0018 | 0.591017186641693 | 0.245419389978214 | 0.12864676117897 | 0.410468330138481 | 5 |
| 3210 | 3210.0068 | 0.687356233596802 | 0.270735838779956 | 0.12291094660759 | 0.412135303180784 | 5 |
| 3215 | 3214.99511666667 | 0.702913701534271 | 0.265071078431373 | 0.0654452592134476 | 0.123240041877453 | 5 |
| 3220 | 3220.00011666667 | 0.686442852020264 | 0.265599128540305 | 0.0663831681013107 | 0.137120121796182 | 5 |
| 3225 | 3225.00511666667 | 0.687758207321167 | 0.268446350762527 | 0.0215691719204187 | 0.0750811673010851 | 5 |
| 3230 | 3229.99343333333 | 0.687773168087006 | 0.264304466230937 | 0.0160547383129597 | 0.0687420977576969 | 5 |
| 3235 | 3234.99843333333 | 0.690913081169128 | 0.267372276688453 | 0.0217042453587055 | 0.0714242306635612 | 5 |
| 3240 | 3240.00343333333 | 0.686649799346924 | 0.26968137254902 | 0.0168766342103481 | 0.0373982725139479 | 5 |
| 3245 | 3244.99175 | 0.687451303005219 | 0.270256535947712 | 0.0142170460894704 | 0.0357244130535718 | 5 |
| 3250 | 3249.99675 | 0.687451839447021 | 0.270319989106754 | 0.00379792996682227 | 0.0295950905367289 | 5 |
| 3255 | 3255.00175 | 0.689646005630493 | 0.268671568627451 | 0.011917483061552 | 0.0442552131497382 | 5 |
| 3260 | 3260.00675 | 0.700864136219025 | 0.265529684095861 | 0.0648613795638084 | 0.119356974719613 | 5 |
| 3265 | 3264.99506666667 | 0.655974388122559 | 0.249423474945534 | 0.0857339203357697 | 0.36004653611253 | 5 |
| 3270 | 3270.00006666667 | 0.680258750915527 | 0.241573801742919 | 0.0294689536094666 | 0.109607845751036 | 5 |
| 3275 | 3275.00506666667 | 0.679401397705078 | 0.246455610021786 | 0.00972440093755722 | 0.0691416787972569 | 5 |
| 3280 | 3279.99338333333 | 0.680992066860199 | 0.239976034858388 | 0.00811192765831947 | 0.0717076937469147 | 5 |
| 3285 | 3284.99838333333 | 0.679201006889343 | 0.242055555555556 | 0.0101729305461049 | 0.0691807776811751 | 5 |
| 3290 | 3290.00338333333 | 0.0677971169352531 | 0.968464869281046 | 0.611423492431641 | 0.945682698233459 | 5 |
| 3295 | 3294.9917 | 0.391707807779312 | 0.846884259259259 | 0.323910683393478 | 1 | 5 |
| 3300 | 3299.9967 | 0.400855362415314 | 0.829938725490196 | 0.0633469447493553 | 0.0731608547451846 | 5 |
| 3305 | 3305.0017 | 0.38587611913681 | 0.861329248366013 | 0.0523164458572865 | 0.105556277486466 | 5 |
| 3310 | 3310.0067 | 0.455690383911133 | 0.752203431372549 | 0.100100219249725 | 0.207517352133008 | 5 |
| 3315 | 3314.99501666667 | 0.486255168914795 | 0.695664488017429 | 0.0649373605847359 | 0.11073271681797 | 5 |
| 3320 | 3320.00001666667 | 0.0102756004780531 | 0.54800871459695 | 0.47779768705368 | 0.999499103544028 | 5 |
| 3325 | 3325.00501666667 | 0.0211102981120348 | 0.522930283224401 | 0.0198902506381273 | 0.0626615211490351 | 5 |
| 3330 | 3329.99333333333 | 0.0219817571341991 | 0.500139705882353 | 0.0209275614470243 | 0.0174011264860907 | 5 |
| 3335 | 3334.99833333333 | 0.0182924848049879 | 0.512162581699346 | 0.0232328437268734 | 0.025686317070961 | 5 |
| 3340 | 3340.00333333333 | 0.0133812641724944 | 0.519558823529412 | 0.0205708052963018 | 0.0326546394547962 | 5 |
| 3345 | 3345.00833333333 | 0.0128681920468807 | 0.529651960784314 | 0.0165974944829941 | 0.0276901176958338 | 5 |
| 3350 | 3349.99665 | 0.0164150334894657 | 0.494178649237473 | 0.0201083887368441 | 0.0342161185992723 | 5 |
| 3355 | 3355.00165 | 0.018281864002347 | 0.506723583877996 | 0.0230808854103088 | 0.0253538378327089 | 5 |
| 3360 | 3360.00665 | 0.0151179200038314 | 0.510584967320261 | 0.0193366017192602 | 0.0261591209050845 | 5 |
| 3365 | 3364.99496666667 | 0.0144147612154484 | 0.518662581699346 | 0.0205299574881792 | 0.0207562608820714 | 5 |
| 3370 | 3369.99996666667 | 0.0154095869511366 | 0.495764978213508 | 0.0202568080276251 | 0.0216985350483782 | 5 |
| 3375 | 3375.00496666667 | 0.0162549037486315 | 0.51892211328976 | 0.0182450991123915 | 0.0281932027994528 | 5 |
| 3380 | 3379.99328333333 | 0.0188153609633446 | 0.519595588235294 | 0.021016338840127 | 0.0264228053596412 | 5 |
| 3385 | 3384.99828333333 | 0.0209575183689594 | 0.514010076252723 | 0.0282200444489717 | 0.0223200102359429 | 5 |
| 3390 | 3390.00328333333 | 0.0207423754036427 | 0.521936002178649 | 0.0299210250377655 | 0.0247438255233659 | 5 |
| 3395 | 3395.00828333333 | 0.017918573692441 | 0.504757080610022 | 0.0247393790632486 | 0.0229431627742866 | 5 |
| 3400 | 3399.9966 | 0.0176854580640793 | 0.525869008714597 | 0.0222026146948338 | 0.028968491918423 | 5 |
| 3405 | 3405.0016 | 0.0156868193298578 | 0.525180555555556 | 0.0216827355325222 | 0.0235254195297483 | 5 |
| 3410 | 3410.0066 | 0.014840142801404 | 0.53052559912854 | 0.0198592059314251 | 0.017320814774262 | 5 |
| 3415 | 3414.99491666667 | 0.0179215706884861 | 0.516331154684096 | 0.022391339763999 | 0.0271360724572441 | 5 |
| 3420 | 3419.99991666667 | 0.0236587692052126 | 0.509691176470588 | 0.0257382914423943 | 0.0322444660938612 | 5 |
| 3425 | 3425.00491666667 | 0.205701544880867 | 0.750369553376906 | 0.199008449912071 | 0.592188903691458 | 5 |
| 3430 | 3429.99323333333 | 0.295882374048233 | 0.752217592592593 | 0.248453170061111 | 0.299280888644457 | 5 |
| 3435 | 3434.99823333333 | 0.33844119310379 | 0.457386982570806 | 0.256361126899719 | 0.665319213277595 | 5 |
| 3440 | 3440.00323333333 | 0.258367657661438 | 0.518809095860566 | 0.236175924539566 | 0.737039255507433 | 5 |
| 3445 | 3445.00823333333 | 0.47501665353775 | 0.38141394335512 | 0.315077602863312 | 0.622567540809229 | 5 |
| 3450 | 3449.99655 | 0.00819716788828373 | 0.42909940087146 | 0.467085808515549 | 0.925634741607142 | 5 |
| 3455 | 3455.00155 | 0.0214989129453897 | 0.413081699346405 | 0.0197957530617714 | 0.0794317940659183 | 5 |
| 3460 | 3460.00655 | 0.0190631821751595 | 0.41737962962963 | 0.0200528334826231 | 0.0289392557072099 | 5 |
| 3465 | 3464.99486666667 | 0.0179104022681713 | 0.417938180827887 | 0.0242557190358639 | 0.0265933770539466 | 5 |
| 3470 | 3469.99986666667 | 0.025219501927495 | 0.397931100217865 | 0.0244501661509275 | 0.0401113109599071 | 5 |
| 3475 | 3475.00486666667 | 0.0205452088266611 | 0.411636437908497 | 0.0253534875810146 | 0.0298248327456789 | 5 |
| 3480 | 3479.99318333333 | 0.0246598608791828 | 0.405784041394336 | 0.0198265258222818 | 0.0338354665360514 | 5 |
| 3485 | 3484.99818333333 | 0.0154063180088997 | 0.424944989106754 | 0.0211478769779205 | 0.0505464833063915 | 5 |
| 3490 | 3490.00318333333 | 0.0254395436495543 | 0.402142973856209 | 0.0249362736940384 | 0.0486942775803022 | 5 |
| 3495 | 3495.00818333333 | 0.0283330623060465 | 0.392526688453159 | 0.0264387279748917 | 0.0243407807185462 | 5 |
| 3500 | 3499.9965 | 0.014519882388413 | 0.506879357298475 | 0.0285713504999876 | 0.0650915584387273 | 5 |
| 3505 | 3505.0015 | 0.0180258732289076 | 0.506366830065359 | 0.0217930283397436 | 0.0984223757804407 | 5 |
| 3510 | 3510.0065 | 0.996011674404144 | 0.00425190631808279 | 0.978016912937164 | 0.962010603636598 | 5 |
| 3515 | 3514.99481666667 | 0.752699375152588 | 0.147066993464052 | 0.24331234395504 | 0.872398310604879 | 5 |


## Record 02 — H03: whole_source_reproduction_check

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 55e2cb3f1549def9dc11a7c3292de50486ce84dc972cc078499ee94e277879c4 |
| started_utc | 2026-09-10T06:14:14.852558+00:00 |
| completed_utc | 2026-09-10T06:15:17.374355+00:00 |
| source_id | 1EDx0YyXW11f6CNg2Too0fh-7jpaEVU9Q |
| character | HIRO |
| alias | H03 |
| label | whole_source_reproduction_check |
| input_path | LOCAL_USER/Downloads\【学マス】篠澤広 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4 |
| filename | 【学マス】篠澤広 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4 |
| size_bytes | 279435246 |
| sha256 | 3b533ccfdfa1d4a284c660f8f3ab5f87c7ca18d52e5f6a4e758f7197493e6989 |
| start_s | 0 |
| end_s | 2687.454331 |
| duration_s | 2687.454331 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 3b533ccfdfa1d4a284c660f8f3ab5f87c7ca18d52e5f6a4e758f7197493e6989 |
| source_id | 1EDx0YyXW11f6CNg2Too0fh-7jpaEVU9Q |
| character | HIRO |
| alias | H03 |
| label | whole_source_reproduction_check |
| boundary_note | N/A |
| parameters.method_version | 2026-09-10-v1 |
| parameters.audio_sr_hz | 22050 |
| parameters.nfft | 2048 |
| parameters.hop | 512 |
| parameters.fft_window | periodic Hann |
| parameters.custom_spectral_center | false |
| parameters.rms_percentile_method | linear |
| parameters.rms_floor | 1e-12 |
| parameters.flatness_power_floor | 1e-10 |
| parameters.cv_ddof | 0 |
| parameters.audio_stream | first (0:a:0) |
| parameters.audio_signal | full unseparated mix, mono for features; native channels for R128 |
| parameters.trim_order | decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim |
| parameters.loudness_filter | ebur128=peak=true |
| parameters.silence_filter | silencedetect=noise=-50dB:d=0.5 |
| parameters.start_s | 0 |
| parameters.end_s | N/A |
| parameters.music | false |
| parameters.visual_step_s | 5 |
| parameters.skip_visual | false |
| parameters.visual_size[0] | 160 |
| parameters.visual_size[1] | 90 |
| parameters.visual_resize | INTER_AREA, whole frame with aspect distortion |
| parameters.visual_grayscale | OpenCV BGR2GRAY /255 |
| parameters.visual_saturation | OpenCV HSV S/255 |
| parameters.histogram | 8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5 |
| parameters.ffmpeg_threads | 1 |
| parameters.music_parameters | N/A |
| software.python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| software.platform | Windows-11-10.0.26200-SP0 |
| software.numpy | 2.1.2 |
| software.ffmpeg_command | ffmpeg |
| software.ffprobe_command | ffprobe |
| software.ffmpeg_version | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101<br><br>Exiting with exit code 0 |
| software.ffprobe_version | ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101 |
| software.opencv | 4.13.0 |
| script_sha256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


### Source probe

| Probe field | Value |
| --- | --- |
| streams[0].index | 0 |
| streams[0].codec_name | h264 |
| streams[0].codec_long_name | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 |
| streams[0].profile | Main |
| streams[0].codec_type | video |
| streams[0].codec_tag_string | avc1 |
| streams[0].codec_tag | 0x31637661 |
| streams[0].mime_codec_string | avc1.4d4020 |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
| streams[0].pix_fmt | yuv420p |
| streams[0].level | 32 |
| streams[0].color_range | tv |
| streams[0].color_space | bt709 |
| streams[0].color_transfer | bt709 |
| streams[0].color_primaries | bt709 |
| streams[0].chroma_location | left |
| streams[0].field_order | progressive |
| streams[0].is_avc | true |
| streams[0].nal_length_size | 4 |
| streams[0].id | 0x1 |
| streams[0].r_frame_rate | 60/1 |
| streams[0].avg_frame_rate | 60/1 |
| streams[0].time_base | 1/15360 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 41278464 |
| streams[0].duration | 2687.400000 |
| streams[0].bit_rate | 688405 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 161244 |
| streams[0].extradata_size | 43 |
| streams[0].disposition.default | 1 |
| streams[0].disposition.dub | 0 |
| streams[0].disposition.original | 0 |
| streams[0].disposition.comment | 0 |
| streams[0].disposition.lyrics | 0 |
| streams[0].disposition.karaoke | 0 |
| streams[0].disposition.forced | 0 |
| streams[0].disposition.hearing_impaired | 0 |
| streams[0].disposition.visual_impaired | 0 |
| streams[0].disposition.clean_effects | 0 |
| streams[0].disposition.attached_pic | 0 |
| streams[0].disposition.timed_thumbnails | 0 |
| streams[0].disposition.non_diegetic | 0 |
| streams[0].disposition.captions | 0 |
| streams[0].disposition.descriptions | 0 |
| streams[0].disposition.metadata | 0 |
| streams[0].disposition.dependent | 0 |
| streams[0].disposition.still_image | 0 |
| streams[0].disposition.multilayer | 0 |
| streams[0].tags.language | und |
| streams[0].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[1].index | 1 |
| streams[1].codec_name | aac |
| streams[1].codec_long_name | AAC (Advanced Audio Coding) |
| streams[1].profile | LC |
| streams[1].codec_type | audio |
| streams[1].codec_tag_string | mp4a |
| streams[1].codec_tag | 0x6134706d |
| streams[1].mime_codec_string | mp4a.40.2 |
| streams[1].sample_fmt | fltp |
| streams[1].sample_rate | 44100 |
| streams[1].channels | 2 |
| streams[1].channel_layout | stereo |
| streams[1].bits_per_sample | 0 |
| streams[1].initial_padding | 0 |
| streams[1].id | 0x2 |
| streams[1].r_frame_rate | 0/0 |
| streams[1].avg_frame_rate | 0/0 |
| streams[1].time_base | 1/44100 |
| streams[1].start_pts | 0 |
| streams[1].start_time | 0.000000 |
| streams[1].duration_ts | 118516736 |
| streams[1].duration | 2687.454331 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 115739 |
| streams[1].extradata_size | 16 |
| streams[1].disposition.default | 1 |
| streams[1].disposition.dub | 0 |
| streams[1].disposition.original | 0 |
| streams[1].disposition.comment | 0 |
| streams[1].disposition.lyrics | 0 |
| streams[1].disposition.karaoke | 0 |
| streams[1].disposition.forced | 0 |
| streams[1].disposition.hearing_impaired | 0 |
| streams[1].disposition.visual_impaired | 0 |
| streams[1].disposition.clean_effects | 0 |
| streams[1].disposition.attached_pic | 0 |
| streams[1].disposition.timed_thumbnails | 0 |
| streams[1].disposition.non_diegetic | 0 |
| streams[1].disposition.captions | 0 |
| streams[1].disposition.descriptions | 0 |
| streams[1].disposition.metadata | 0 |
| streams[1].disposition.dependent | 0 |
| streams[1].disposition.still_image | 0 |
| streams[1].disposition.multilayer | 0 |
| streams[1].tags.language | jpn |
| streams[1].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[2].index | 2 |
| streams[2].codec_name | png |
| streams[2].codec_long_name | PNG (Portable Network Graphics) image |
| streams[2].codec_type | video |
| streams[2].codec_tag_string | [0][0][0][0] |
| streams[2].codec_tag | 0x0000 |
| streams[2].width | 1280 |
| streams[2].height | 720 |
| streams[2].coded_width | 1280 |
| streams[2].coded_height | 720 |
| streams[2].has_b_frames | 0 |
| streams[2].pix_fmt | rgb24 |
| streams[2].level | -99 |
| streams[2].color_range | pc |
| streams[2].color_space | gbr |
| streams[2].id | 0x0 |
| streams[2].r_frame_rate | 90000/1 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/90000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 241870890 |
| streams[2].duration | 2687.454333 |
| streams[2].disposition.default | 0 |
| streams[2].disposition.dub | 0 |
| streams[2].disposition.original | 0 |
| streams[2].disposition.comment | 0 |
| streams[2].disposition.lyrics | 0 |
| streams[2].disposition.karaoke | 0 |
| streams[2].disposition.forced | 0 |
| streams[2].disposition.hearing_impaired | 0 |
| streams[2].disposition.visual_impaired | 0 |
| streams[2].disposition.clean_effects | 0 |
| streams[2].disposition.attached_pic | 1 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| chapters | [] |
| format.filename | LOCAL_USER/Downloads\【学マス】篠澤広 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2687.454331 |
| format.size | 279435246 |
| format.bit_rate | 831821 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】篠澤広  親愛度コミュ21～27話まとめ【STEP3】 |
| format.tags.artist | 学Pといっしょ |
| format.tags.genre | Gaming |
| format.tags.date | 20250717 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=PKkBQRBGljI |
| format.tags.description | 【注意】この動画には「学園アイドルマスター」のネタバレを含みます。<br><br><br>▼学マス 好評配信中！▼<br>http://app.adjust.com/1ai6ouao<br><br>学マス公式サイト<br>https://gakuen.idolmaster-official.jp/<br>学マス公式X(Twitter)<br>https://x.com/gkmas_official<br><br><br>#学マス<br>#篠澤広 |
| format.tags.synopsis | 【注意】この動画には「学園アイドルマスター」のネタバレを含みます。<br><br><br>▼学マス 好評配信中！▼<br>http://app.adjust.com/1ai6ouao<br><br>学マス公式サイト<br>https://gakuen.idolmaster-official.jp/<br>学マス公式X(Twitter)<br>https://x.com/gkmas_official<br><br><br>#学マス<br>#篠澤広 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 59258368 |
| analyzed_audio_duration_s | 2687.45433106576 |
| stft_frames | 115736 |
| flux_transitions | 115735 |
| rms_linear | 0.0638812457483088 |
| rms_p10_linear | 0.00616669168925748 |
| rms_p90_linear | 0.112067978819375 |
| rms_p90_p10_db | 25.1885860688991 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 3870 |
| centroid_hz_mean | 2081.88901658777 |
| flatness_mean | 0.0643373730933683 |
| positive_normalized_flux_mean | 0.0352425394204931 |
| flux_cv | 0.667883935907765 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -22.6 |
| lra_lu | 8 |
| true_peak_dbfs | -8.1 |
| silence_seconds | 122.950403000001 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -22.6 LUFS<br>    Threshold: -33.9 LUFS<br><br>  Loudness range:<br>    LRA:         8.0 LU<br>    Threshold: -44.0 LUFS<br>    LRA low:   -28.9 LUFS<br>    LRA high:  -20.9 LUFS<br><br>  True peak:<br>    Peak:       -8.1 dBFS<br>[out#0/null @ 000001e390961580] video:0KiB audio:462956KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:44:47.45 bitrate=N/A speed= 197x elapsed=0:00:13.63 |
| ffmpeg_stderr_sha256 | 603e4cb6a732c42c8e617dee00f22fcaf09f1516d3d3ef876afafd057111db26 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 0 | 3.202109 | 3.202109 | 3.202109 |
| 143.471791 | 144.295215 | 0.823424000000017 | 0.823424 |
| 206.167551 | 206.935215 | 0.767663999999996 | 0.767664 |
| 235.318435 | 236.159773 | 0.841338000000007 | 0.841338 |
| 237.018322 | 237.918073 | 0.899750999999981 | 0.899751 |
| 238.93737 | 240.516735 | 1.57936500000002 | 1.579365 |
| 397.532336 | 398.583764 | 1.05142799999999 | 1.051429 |
| 399.238844 | 400.033719 | 0.794875000000047 | 0.794875 |
| 400.682653 | 401.824172 | 1.14151899999996 | 1.141519 |
| 403.450113 | 403.995805 | 0.545692000000031 | 0.545692 |
| 404.895374 | 405.706848 | 0.811473999999976 | 0.811474 |
| 407.51229 | 408.266757 | 0.754466999999977 | 0.754467 |
| 488.512404 | 490.236213 | 1.72380900000002 | 1.72381 |
| 513.377098 | 514.921701 | 1.54460299999994 | 1.544603 |
| 579.24 | 580.748866 | 1.50886600000001 | 1.508866 |
| 581.0478 | 583.066327 | 2.01852699999995 | 2.018526 |
| 583.521655 | 585.656327 | 2.13467200000002 | 2.134671 |
| 598.771497 | 599.872562 | 1.10106500000006 | 1.101066 |
| 602.85771 | 605.406689 | 2.54897900000003 | 2.54898 |
| 647.759025 | 649.166531 | 1.40750600000001 | 1.407506 |
| 770.33712 | 771.040726 | 0.703605999999922 | 0.703605 |
| 906.546599 | 907.19263 | 0.646030999999994 | 0.646032 |
| 938.75288 | 940.9261 | 2.17322000000001 | 2.17322 |
| 1003.913288 | 1004.443175 | 0.529887000000031 | 0.529887 |
| 1007.443787 | 1009.551859 | 2.10807199999999 | 2.108073 |
| 1009.977188 | 1011.551474 | 1.57428600000003 | 1.574286 |
| 1013.523696 | 1014.118413 | 0.59471700000006 | 0.594717 |
| 1015.586077 | 1016.726667 | 1.14058999999997 | 1.14059 |
| 1120.264898 | 1121.426599 | 1.16170099999999 | 1.161701 |
| 1122.089002 | 1123.660317 | 1.57131500000014 | 1.571315 |
| 1125.640567 | 1126.593696 | 0.95312899999999 | 0.953129 |
| 1127.506281 | 1128.249388 | 0.743107000000009 | 0.743107 |
| 1131.853583 | 1132.675918 | 0.822334999999839 | 0.822336 |
| 1233.463628 | 1234.391451 | 0.927822999999989 | 0.927823 |
| 1236.517166 | 1238.211837 | 1.69467099999997 | 1.694671 |
| 1271.559002 | 1272.233696 | 0.674694000000045 | 0.674694 |
| 1273.4422 | 1274.543401 | 1.10120099999995 | 1.101202 |
| 1275.369932 | 1276.227642 | 0.857709999999997 | 0.85771 |
| 1276.84449 | 1277.382766 | 0.538275999999996 | 0.538277 |
| 1278.101905 | 1278.994354 | 0.892448999999942 | 0.892449 |
| 1317.731519 | 1318.712494 | 0.980975000000171 | 0.980975 |
| 1320.598685 | 1321.736009 | 1.13732400000004 | 1.137324 |
| 1322.842902 | 1323.409048 | 0.56614599999989 | 0.566145 |
| 1326.567188 | 1328.213265 | 1.6460770000001 | 1.646077 |
| 1354.530204 | 1355.178299 | 0.648095000000012 | 0.648095 |
| 1359.672698 | 1360.320227 | 0.647528999999849 | 0.647528 |
| 1418.462109 | 1419.535011 | 1.07290199999989 | 1.072902 |
| 1420.060816 | 1421.44678 | 1.38596400000006 | 1.385964 |
| 1422.310227 | 1423.295488 | 0.985261000000037 | 0.985261 |
| 1425.203628 | 1425.791293 | 0.587665000000015 | 0.587664 |
| 1475.115465 | 1475.81542 | 0.699954999999818 | 0.699955 |
| 1477.054331 | 1478.383991 | 1.32965999999988 | 1.32966 |
| 1478.91093 | 1479.694444 | 0.783513999999968 | 0.783515 |
| 1481.042358 | 1482.137075 | 1.09471700000017 | 1.094717 |
| 1482.28093 | 1483.043719 | 0.762789000000112 | 0.762789 |
| 1483.516803 | 1484.307506 | 0.790703000000121 | 0.790703 |
| 1485.256054 | 1487.327914 | 2.07186000000002 | 2.071859 |
| 1487.785125 | 1488.495442 | 0.710316999999804 | 0.710317 |
| 1490.599864 | 1494.901814 | 4.30195000000003 | 4.30195 |
| 1555.265488 | 1558.198435 | 2.93294700000001 | 2.932948 |
| 1651.209252 | 1653.389456 | 2.180204 | 2.180204 |
| 1654.303673 | 1656.099478 | 1.7958050000002 | 1.795805 |
| 1677.929161 | 1678.615442 | 0.686281000000008 | 0.686281 |
| 1761.190726 | 1762.362812 | 1.17208600000004 | 1.172086 |
| 1792.232086 | 1793.876372 | 1.64428599999997 | 1.644286 |
| 1795.252109 | 1797.126485 | 1.87437599999998 | 1.874376 |
| 1898.335351 | 1899.728957 | 1.39360600000009 | 1.393605 |
| 1901.231519 | 1901.827506 | 0.59598700000015 | 0.595986 |
| 1904.555238 | 1905.502404 | 0.947166000000152 | 0.947166 |
| 1907.601542 | 1908.231882 | 0.630339999999933 | 0.63034 |
| 1910.850771 | 1912.141723 | 1.29095200000006 | 1.290952 |
| 1913.656236 | 1914.298957 | 0.642720999999938 | 0.642721 |
| 1916.836395 | 1918.479433 | 1.64303799999993 | 1.643039 |
| 1921.772063 | 1923.094512 | 1.32244900000001 | 1.322449 |
| 1923.536803 | 1925.205828 | 1.66902500000015 | 1.669025 |
| 1926.000068 | 1927.423946 | 1.42387799999983 | 1.423878 |
| 1928.529751 | 1929.602449 | 1.07269799999995 | 1.072698 |
| 1930.364853 | 1931.399274 | 1.03442100000007 | 1.034422 |
| 1977.816531 | 1978.490975 | 0.674443999999994 | 0.674444 |
| 2000.988866 | 2002.117392 | 1.12852600000019 | 1.128526 |
| 2066.12229 | 2067.746553 | 1.62426300000016 | 1.624263 |
| 2068.65229 | 2069.876893 | 1.22460300000012 | 1.224603 |
| 2278.688073 | 2279.710136 | 1.02206300000034 | 1.022063 |
| 2281.109002 | 2282.132834 | 1.02383199999986 | 1.023832 |
| 2283.639048 | 2284.261746 | 0.622698000000128 | 0.622698 |
| 2284.425828 | 2285.115215 | 0.689386999999897 | 0.689388 |
| 2285.519841 | 2286.591746 | 1.07190500000024 | 1.071905 |
| 2287.610363 | 2288.18483 | 0.574467000000368 | 0.574467 |
| 2336.914558 | 2337.891247 | 0.976689000000079 | 0.976689 |
| 2338.642472 | 2339.522177 | 0.879704999999831 | 0.879705 |
| 2479.872449 | 2480.791655 | 0.919206000000031 | 0.919206 |
| 2635.862766 | 2636.505261 | 0.642494999999599 | 0.642494 |
| 2652.845057 | 2657.921587 | 5.07652999999982 | 5.076531 |
| 2679.420363 | 2687.454331 | 8.03396799999973 | 8.033968 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 538 |
| samples | 538 |
| brightness_mean | 0.672457406761256 |
| saturation_mean | 0.225861321180682 |
| frame_difference_mean | 0.0683752938400905 |
| histogram_jumps_gt_0_5 | 37 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.547988831996918 | 0.217651416122004 | N/A | N/A | N/A |
| 5 | 5 | 0.666667461395264 | 0.226098039215686 | 0.122702613472939 | 0.369242959842164 | 5 |
| 10 | 10 | 0.713131248950958 | 0.201165577342048 | 0.0957083329558372 | 0.235774144178499 | 5 |
| 15 | 15 | 0.556590676307678 | 0.202734477124183 | 0.160517156124115 | 0.397631173515551 | 5 |
| 20 | 20 | 0.577686846256256 | 0.208739379084967 | 0.0609822981059551 | 0.141457455032181 | 5 |
| 25 | 25 | 0.698844254016876 | 0.197836328976035 | 0.135193899273872 | 0.276658323548962 | 5 |
| 30 | 30 | 0.739253282546997 | 0.186227124183007 | 0.07655119150877 | 0.1457517579012 | 5 |
| 35 | 35 | 0.703651964664459 | 0.204657952069717 | 0.069476030766964 | 0.150569477411442 | 5 |
| 40 | 40 | 0.728980720043182 | 0.204405773420479 | 0.0861898139119148 | 0.216008787432394 | 5 |
| 45 | 45 | 0.706525087356567 | 0.20124591503268 | 0.0732671543955803 | 0.213332515068157 | 5 |
| 50 | 50 | 0.700107038021088 | 0.201625816993464 | 0.0790405794978142 | 0.158734124080917 | 5 |
| 55 | 55 | 0.729133188724518 | 0.190586873638344 | 0.0909950956702232 | 0.21537837857609 | 5 |
| 60 | 60 | 0.718438148498535 | 0.192830610021787 | 0.0903992354869843 | 0.174427891987181 | 5 |
| 65 | 65 | 0.70530778169632 | 0.196840413943355 | 0.0307001620531082 | 0.0906039631358547 | 5 |
| 70 | 70 | 0.715877115726471 | 0.199002723311547 | 0.0712715163826942 | 0.113440987488735 | 5 |
| 75 | 75 | 0.710656881332397 | 0.203915305010893 | 0.022628266364336 | 0.0509232365760001 | 5 |
| 80 | 80 | 0.710288941860199 | 0.200319716775599 | 0.0151685727760196 | 0.0670233817571223 | 5 |
| 85 | 85 | 0.712637543678284 | 0.195308278867102 | 0.0750615447759628 | 0.126333067175863 | 5 |
| 90 | 90 | 0.714936077594757 | 0.201288126361656 | 0.0724035874009132 | 0.104595042558233 | 5 |
| 95 | 95 | 0.713602185249329 | 0.20225462962963 | 0.0200936812907457 | 0.0410213927257132 | 5 |
| 100 | 100 | 0.710284292697906 | 0.198284586056645 | 0.0767115950584412 | 0.111196922180295 | 5 |
| 105 | 105 | 0.708112478256226 | 0.197235294117647 | 0.0329795740544796 | 0.0559774633186294 | 5 |
| 110 | 110 | 0.707970321178436 | 0.192746732026144 | 0.00818845350295305 | 0.0725451510152473 | 5 |
| 115 | 115 | 0.710576593875885 | 0.203729575163399 | 0.0742287561297417 | 0.127757185879988 | 5 |
| 120 | 120 | 0.710101306438446 | 0.204224945533769 | 0.00886682979762554 | 0.0296306455436737 | 5 |
| 125 | 125 | 0.712537586688995 | 0.201397331154684 | 0.023566447198391 | 0.044553601446084 | 5 |
| 130 | 130 | 0.706767737865448 | 0.206880991285403 | 0.0221865456551313 | 0.0528939818707312 | 5 |
| 135 | 135 | 0.708311855792999 | 0.197198801742919 | 0.0765234231948853 | 0.117421524292253 | 5 |
| 140 | 140 | 0.713455975055695 | 0.195364106753813 | 0.0333728231489658 | 0.0628081544706435 | 5 |
| 145 | 145 | 0.642796277999878 | 0.269854302832244 | 0.123222216963768 | 0.29725313237779 | 5 |
| 150 | 150 | 0.661873638629913 | 0.256828159041394 | 0.0400915034115314 | 0.13589592036931 | 5 |
| 155 | 155 | 0.661477446556091 | 0.258092592592593 | 0.036900594830513 | 0.102679115686703 | 5 |
| 160 | 160 | 0.681735575199127 | 0.238480664488017 | 0.091013066470623 | 0.187751430584098 | 5 |
| 165 | 165 | 0.660826563835144 | 0.259056917211329 | 0.088456965982914 | 0.178275469426478 | 5 |
| 170 | 170 | 0.664467394351959 | 0.257133442265795 | 0.0274033229798079 | 0.0962467802214636 | 5 |
| 175 | 175 | 0.664510607719421 | 0.252245098039216 | 0.00681236386299133 | 0.0710402208093816 | 5 |
| 180 | 180 | 0.681508719921112 | 0.237632897603486 | 0.089808002114296 | 0.18440223574343 | 5 |
| 185 | 185 | 0.68121349811554 | 0.232714869281046 | 0.0111922658979893 | 0.0772596421942241 | 5 |
| 190 | 190 | 0.65994668006897 | 0.264784586056645 | 0.0910087078809738 | 0.191350244683489 | 5 |
| 195 | 195 | 0.659405529499054 | 0.260210511982571 | 0.00742728775367141 | 0.0682153875709281 | 5 |
| 200 | 200 | 0.680140256881714 | 0.236104575163399 | 0.0909275487065315 | 0.192241007472016 | 5 |
| 205 | 205 | 0.684314548969269 | 0.231556917211329 | 0.0366633981466293 | 0.0798078611620753 | 5 |
| 210 | 210 | 0.649389147758484 | 0.283387527233115 | 0.092625267803669 | 0.295025827512323 | 5 |
| 215 | 215 | 0.667498886585236 | 0.284699618736383 | 0.0214937385171652 | 0.132907544649733 | 5 |
| 220 | 220 | 0.678382635116577 | 0.261967047930283 | 0.061010617762804 | 0.202974532101233 | 5 |
| 225 | 225 | 0.673841774463654 | 0.27785348583878 | 0.0601584948599339 | 0.197469866817543 | 5 |
| 230 | 230 | 0.66687935590744 | 0.284372549019608 | 0.022781589999795 | 0.0595446710467173 | 5 |
| 235 | 235 | 0.664988875389099 | 0.268575708061002 | 0.0591007620096207 | 0.210434600251984 | 5 |
| 240 | 240 | 0.692018210887909 | 0.269723039215686 | 0.048552829772234 | 0.169025950497811 | 5 |
| 245 | 245 | 0.667095363140106 | 0.284710784313725 | 0.0613074563443661 | 0.178102632777315 | 5 |
| 250 | 250 | 0.651093482971191 | 0.287978758169935 | 0.0345999449491501 | 0.162081872528101 | 5 |
| 255 | 255 | 0.687032759189606 | 0.270455337690632 | 0.0677622556686401 | 0.2096040621335 | 5 |
| 260 | 260 | 0.669796884059906 | 0.267772603485839 | 0.0420833341777325 | 0.159807917858627 | 5 |
| 265 | 265 | 0.666153311729431 | 0.283214324618736 | 0.0637916624546051 | 0.195747588404657 | 5 |
| 270 | 270 | 0.687519133090973 | 0.267403594771242 | 0.0597475469112396 | 0.182715973418994 | 5 |
| 275 | 275 | 0.674536764621735 | 0.263576797385621 | 0.019937090575695 | 0.157780376783403 | 5 |
| 280 | 280 | 0.673055827617645 | 0.286199346405229 | 0.0593589320778847 | 0.201927452364913 | 5 |
| 285 | 285 | 0.66606730222702 | 0.288449618736383 | 0.0169929191470146 | 0.0691328323263598 | 5 |
| 290 | 290 | 0.647101104259491 | 0.287399237472767 | 0.0346034839749336 | 0.141186924348256 | 5 |
| 295 | 295 | 0.673363864421844 | 0.283420206971678 | 0.0381413400173187 | 0.143322890794018 | 5 |
| 300 | 300 | 0.654557466506958 | 0.283232298474946 | 0.0279180277138948 | 0.131229235687419 | 5 |
| 305 | 305 | 0.664467632770538 | 0.286452069716776 | 0.0305746179074049 | 0.120683229869598 | 5 |
| 310 | 310 | 0.683463275432587 | 0.269501633986928 | 0.0602461844682693 | 0.151847279420963 | 5 |
| 315 | 315 | 0.625471413135529 | 0.27945234204793 | 0.0841268971562386 | 0.426083720156463 | 5 |
| 320 | 320 | 0.621405839920044 | 0.277245642701525 | 0.0342905782163143 | 0.0860515003787748 | 5 |
| 325 | 325 | 0.595045804977417 | 0.336351034858388 | 0.0709389969706535 | 0.177354237678046 | 5 |
| 330 | 330 | 0.594026446342468 | 0.331075435729847 | 0.00711083831265569 | 0.0577735712328177 | 5 |
| 335 | 335 | 0.594582498073578 | 0.336206154684096 | 0.00539379101246595 | 0.0530961524107029 | 5 |
| 340 | 340 | 0.59437769651413 | 0.331084150326797 | 0.00546786515042186 | 0.0551285476950433 | 5 |
| 345 | 345 | 0.62154495716095 | 0.281891612200436 | 0.0697728767991066 | 0.171278252207565 | 5 |
| 350 | 350 | 0.588999152183533 | 0.345137254901961 | 0.070600762963295 | 0.174385990590587 | 5 |
| 355 | 355 | 0.586978733539581 | 0.339814270152505 | 0.0164637807756662 | 0.0611967450505114 | 5 |
| 360 | 360 | 0.613995611667633 | 0.291058006535948 | 0.0692663416266441 | 0.148194374977123 | 5 |
| 365 | 365 | 0.596563816070557 | 0.335116557734205 | 0.067933551967144 | 0.148703498947325 | 5 |
| 370 | 370 | 0.619735836982727 | 0.282727668845316 | 0.0671704858541489 | 0.162730451677334 | 5 |
| 375 | 375 | 0.619713246822357 | 0.283058278867102 | 0.0124272871762514 | 0.03704595824743 | 5 |
| 380 | 380 | 0.597655475139618 | 0.325512527233115 | 0.0699025020003319 | 0.169746158950809 | 5 |
| 385 | 385 | 0.591802597045898 | 0.338156318082789 | 0.0337178632616997 | 0.0715933091173837 | 5 |
| 390 | 390 | 0.593271732330322 | 0.333481209150327 | 0.00876770168542862 | 0.0534925915236284 | 5 |
| 395 | 395 | 0.592989683151245 | 0.337601851851852 | 0.0224117636680603 | 0.0597311841436536 | 5 |
| 400 | 400 | 0.619005739688873 | 0.277272058823529 | 0.0675934106111526 | 0.179298746343319 | 5 |
| 405 | 405 | 0.625665843486786 | 0.27794825708061 | 0.0452222190797329 | 0.0963559911998277 | 5 |
| 410 | 410 | 0.596405804157257 | 0.33976334422658 | 0.0687470063567162 | 0.171187478898571 | 5 |
| 415 | 415 | 0.589081704616547 | 0.345740740740741 | 0.0284858383238316 | 0.0681467530522708 | 5 |
| 420 | 420 | 0.592989921569824 | 0.33823311546841 | 0.0267083346843719 | 0.0728613352934329 | 5 |
| 425 | 425 | 0.590468943119049 | 0.342256535947712 | 0.0197775065898895 | 0.0614460812225751 | 5 |
| 430 | 430 | 0.629306614398956 | 0.269209150326797 | 0.0749161168932915 | 0.19665831598563 | 5 |
| 435 | 435 | 0.618541419506073 | 0.286720588235294 | 0.0373175404965878 | 0.0752915590309416 | 5 |
| 440 | 440 | 0.594910681247711 | 0.338040032679739 | 0.0658730939030647 | 0.171010135888635 | 5 |
| 445 | 445 | 0.588282942771912 | 0.345955610021786 | 0.0231288131326437 | 0.0694488143633139 | 5 |
| 450 | 450 | 0.587297677993774 | 0.345653867102397 | 0.00571568589657545 | 0.0313267482097732 | 5 |
| 455 | 455 | 0.596666932106018 | 0.3348575708061 | 0.0273513067513704 | 0.062888444943454 | 5 |
| 460 | 460 | 0.618326008319855 | 0.28655991285403 | 0.0632156878709793 | 0.155525493915672 | 5 |
| 465 | 465 | 0.616922378540039 | 0.279834150326797 | 0.0366367101669312 | 0.0821672060477293 | 5 |
| 470 | 470 | 0.598393559455872 | 0.334770969498911 | 0.0676742941141129 | 0.17827703569637 | 5 |
| 475 | 475 | 0.597635090351105 | 0.331041666666667 | 0.0234398134052753 | 0.0799436098385648 | 5 |
| 480 | 480 | 0.591196358203888 | 0.338553921568627 | 0.032809641212225 | 0.0522552192383392 | 5 |
| 485 | 485 | 0.625134289264679 | 0.271122004357298 | 0.0721029415726662 | 0.181884643126253 | 5 |
| 490 | 490 | 0.623817265033722 | 0.26603022875817 | 0.0193224400281906 | 0.0729729859473812 | 5 |
| 495 | 495 | 0.593743741512299 | 0.34313834422658 | 0.0705272406339645 | 0.196022014159949 | 5 |
| 500 | 500 | 0.593425989151001 | 0.338046568627451 | 0.00488916132599115 | 0.0517411888621248 | 5 |
| 505 | 505 | 0.596003830432892 | 0.334853758169935 | 0.0211198255419731 | 0.0638140557957899 | 5 |
| 510 | 510 | 0.622514963150024 | 0.277691448801743 | 0.0693161711096764 | 0.175954628322392 | 5 |
| 515 | 515 | 0.704375028610229 | 0.247811274509804 | 0.110881261527538 | 0.409880660633291 | 5 |
| 520 | 520 | 0.692526459693909 | 0.241860021786492 | 0.0694613307714462 | 0.140714032368944 | 5 |
| 525 | 525 | 0.701401948928833 | 0.238849945533769 | 0.0269229300320148 | 0.0458892291076688 | 5 |
| 530 | 530 | 0.705047607421875 | 0.252050653594771 | 0.0681424289941788 | 0.137081092022859 | 5 |
| 535 | 535 | 0.702770173549652 | 0.25271568627451 | 0.0159185733646154 | 0.0334599579719166 | 5 |
| 540 | 540 | 0.742865204811096 | 0.219810185185185 | 0.0727660655975342 | 0.195104748547352 | 5 |
| 545 | 545 | 0.705818951129913 | 0.240499727668845 | 0.0726279988884926 | 0.146850940904115 | 5 |
| 550 | 550 | 0.705142438411713 | 0.249237745098039 | 0.0631726607680321 | 0.135986900394829 | 5 |
| 555 | 555 | 0.691576838493347 | 0.238618191721133 | 0.0756663903594017 | 0.149545876197943 | 5 |
| 560 | 560 | 0.740569412708282 | 0.219507897603486 | 0.0805596336722374 | 0.175914281796529 | 5 |
| 565 | 565 | 0.743068158626556 | 0.219859749455338 | 0.0325727090239525 | 0.0352616147328989 | 5 |
| 570 | 570 | 0.703819990158081 | 0.252868191721133 | 0.0720912218093872 | 0.198010098434353 | 5 |
| 575 | 575 | 0.701414525508881 | 0.23895697167756 | 0.0663902461528778 | 0.137383309296908 | 5 |
| 580 | 580 | 0.694304227828979 | 0.24070234204793 | 0.0289441719651222 | 0.0496836797786371 | 5 |
| 585 | 585 | 0.741156697273254 | 0.222561546840959 | 0.0798932388424873 | 0.172194032215809 | 5 |
| 590 | 590 | 0.709261476993561 | 0.24996568627451 | 0.0653809979557991 | 0.176297461392965 | 5 |
| 595 | 595 | 0.705451250076294 | 0.240427287581699 | 0.0675253197550774 | 0.126100435499653 | 5 |
| 600 | 600 | 0.722510993480682 | 0.224968954248366 | 0.0833134427666664 | 0.201251337470134 | 5 |
| 605 | 605 | 0.720779418945312 | 0.239066448801743 | 0.0656650364398956 | 0.170662711196759 | 5 |
| 610 | 610 | 0.741809666156769 | 0.22102151416122 | 0.0652393773198128 | 0.170699942447857 | 5 |
| 615 | 615 | 0.741940081119537 | 0.220799564270153 | 0.0309120360761881 | 0.0357858198960608 | 5 |
| 620 | 620 | 0.712991833686829 | 0.247712690631808 | 0.0665130689740181 | 0.172865774347049 | 5 |
| 625 | 625 | 0.701979577541351 | 0.254296568627451 | 0.0231941733509302 | 0.0469162556337334 | 5 |
| 630 | 630 | 0.70240706205368 | 0.238993736383442 | 0.0650288686156273 | 0.138031543064762 | 5 |
| 635 | 635 | 0.69288557767868 | 0.241005991285403 | 0.023901142179966 | 0.0459553738433388 | 5 |
| 640 | 640 | 0.743914246559143 | 0.219218954248366 | 0.081707239151001 | 0.169189432324575 | 5 |
| 645 | 645 | 0.71929144859314 | 0.240539760348584 | 0.0648183524608612 | 0.172349755473148 | 5 |
| 650 | 650 | 0.594946682453156 | 0.337509259259259 | 0.138722777366638 | 0.451514698139586 | 5 |
| 655 | 655 | 0.586670756340027 | 0.344500544662309 | 0.0235705338418484 | 0.0693730630321978 | 5 |
| 660 | 660 | 0.617366015911102 | 0.28393545751634 | 0.0687916651368141 | 0.158985498173732 | 5 |
| 665 | 665 | 0.599173963069916 | 0.248378812636166 | 0.128215402364731 | 0.419862179436609 | 5 |
| 670 | 670 | 0.693466007709503 | 0.238756263616558 | 0.10203268378973 | 0.284363949514124 | 5 |
| 675 | 675 | 0.705232858657837 | 0.238019335511983 | 0.0789629593491554 | 0.166848645035444 | 5 |
| 680 | 680 | 0.703771233558655 | 0.236686546840959 | 0.0177301187068224 | 0.0416777624185423 | 5 |
| 685 | 685 | 0.688722491264343 | 0.239787037037037 | 0.0779931843280792 | 0.169814618597006 | 5 |
| 690 | 690 | 0.743635952472687 | 0.201975217864924 | 0.0871868133544922 | 0.194270478379523 | 5 |
| 695 | 695 | 0.736490190029144 | 0.204365740740741 | 0.0332546271383762 | 0.0473805547315499 | 5 |
| 700 | 700 | 0.742971181869507 | 0.202101579520697 | 0.0346797332167625 | 0.0566801198516805 | 5 |
| 705 | 705 | 0.704336881637573 | 0.239368736383442 | 0.0760035365819931 | 0.203210745507563 | 5 |
| 710 | 710 | 0.695227146148682 | 0.234130174291939 | 0.0818406865000725 | 0.185146492283277 | 5 |
| 715 | 715 | 0.697797119617462 | 0.237474128540305 | 0.025340685620904 | 0.0453366851875538 | 5 |
| 720 | 720 | 0.692751944065094 | 0.236877178649237 | 0.0256977118551731 | 0.0508487153948925 | 5 |
| 725 | 725 | 0.719614148139954 | 0.218841775599129 | 0.0885849669575691 | 0.202317254754673 | 5 |
| 730 | 730 | 0.726829588413239 | 0.212611928104575 | 0.0295068062841892 | 0.0484956009108467 | 5 |
| 735 | 735 | 0.696787595748901 | 0.236973583877996 | 0.081857293844223 | 0.197223835626402 | 5 |
| 740 | 740 | 0.706198871135712 | 0.239388071895425 | 0.0711682960391045 | 0.173773120437815 | 5 |
| 745 | 745 | 0.700757384300232 | 0.244022331154684 | 0.0225857831537724 | 0.0512039364334466 | 5 |
| 750 | 750 | 0.687311887741089 | 0.242972222222222 | 0.0760577321052551 | 0.173209185086551 | 5 |
| 755 | 755 | 0.692281067371368 | 0.23854765795207 | 0.0275356713682413 | 0.0448738573031409 | 5 |
| 760 | 760 | 0.698694169521332 | 0.235405501089325 | 0.0307312067598104 | 0.0475269144430034 | 5 |
| 765 | 765 | 0.739948272705078 | 0.204307461873638 | 0.081050381064415 | 0.199186775698773 | 5 |
| 770 | 770 | 0.687564551830292 | 0.295090958605665 | 0.0917764082551003 | 0.305102530167804 | 5 |
| 775 | 775 | 0.711508452892303 | 0.230369008714597 | 0.101110570132732 | 0.390670131706474 | 5 |
| 780 | 780 | 0.748265326023102 | 0.198617919389978 | 0.0755601823329926 | 0.198750889961713 | 5 |
| 785 | 785 | 0.747621774673462 | 0.19957788671024 | 0.0107595315203071 | 0.0364798984459912 | 5 |
| 790 | 790 | 0.723172903060913 | 0.221256808278867 | 0.0687069669365883 | 0.178348278179872 | 5 |
| 795 | 795 | 0.722987711429596 | 0.221598039215686 | 0.00805228762328625 | 0.029463103645087 | 5 |
| 800 | 800 | 0.712995886802673 | 0.206493736383442 | 0.0736111104488373 | 0.170102133476753 | 5 |
| 805 | 805 | 0.722579181194305 | 0.221096405228758 | 0.0745806023478508 | 0.166526660601528 | 5 |
| 810 | 810 | 0.706277251243591 | 0.237209422657952 | 0.068399503827095 | 0.189367490771256 | 5 |
| 815 | 815 | 0.716968178749084 | 0.227970043572985 | 0.0291440617293119 | 0.0596317168312946 | 5 |
| 820 | 820 | 0.747985303401947 | 0.196365740740741 | 0.0727889314293861 | 0.17995065705186 | 5 |
| 825 | 825 | 0.74961930513382 | 0.192061819172113 | 0.0319738537073135 | 0.0514436545865694 | 5 |
| 830 | 830 | 0.748123645782471 | 0.196412854030501 | 0.0351650305092335 | 0.0673477149304361 | 5 |
| 835 | 835 | 0.714718699455261 | 0.210050108932462 | 0.0713902488350868 | 0.189316814899313 | 5 |
| 840 | 840 | 0.715797662734985 | 0.226802559912854 | 0.0827342048287392 | 0.22588087630241 | 5 |
| 845 | 845 | 0.710031032562256 | 0.229328976034858 | 0.0318314246833324 | 0.0465311091140843 | 5 |
| 850 | 850 | 0.722656905651093 | 0.220132352941176 | 0.068319708108902 | 0.17018468271994 | 5 |
| 855 | 855 | 0.712116539478302 | 0.207737745098039 | 0.071178637444973 | 0.150842191780421 | 5 |
| 860 | 860 | 0.704534351825714 | 0.211213235294118 | 0.042967863380909 | 0.0699352210753495 | 5 |
| 865 | 865 | 0.725677311420441 | 0.217459150326797 | 0.0713929757475853 | 0.174665518646844 | 5 |
| 870 | 870 | 0.71962308883667 | 0.2249098583878 | 0.0194109473377466 | 0.0567864535599221 | 5 |
| 875 | 875 | 0.719739735126495 | 0.225593954248366 | 0.0629041343927383 | 0.171549152201764 | 5 |
| 880 | 880 | 0.707850217819214 | 0.230833333333333 | 0.03460294008255 | 0.0625648638598527 | 5 |
| 885 | 885 | 0.71313887834549 | 0.206415305010893 | 0.093919925391674 | 0.231060890395175 | 5 |
| 890 | 890 | 0.71696925163269 | 0.207856753812636 | 0.0400073491036892 | 0.0585002869197369 | 5 |
| 895 | 895 | 0.747565090656281 | 0.194195261437909 | 0.0742810368537903 | 0.173071352525551 | 5 |
| 900 | 900 | 0.711176216602325 | 0.229614379084967 | 0.0768502131104469 | 0.212555900272527 | 5 |
| 905 | 905 | 0.715722501277924 | 0.229710239651416 | 0.0289678629487753 | 0.0510253732872462 | 5 |
| 910 | 910 | 0.730857610702515 | 0.202809095860566 | 0.0762859433889389 | 0.202355509148788 | 5 |
| 915 | 915 | 0.724292993545532 | 0.219337145969499 | 0.0721331611275673 | 0.232426504881156 | 5 |
| 920 | 920 | 0.710640013217926 | 0.230790849673203 | 0.0666759237647057 | 0.168805224130845 | 5 |
| 925 | 925 | 0.711290001869202 | 0.231749183006536 | 0.0309583321213722 | 0.0469489749388068 | 5 |
| 930 | 930 | 0.71369856595993 | 0.210038126361656 | 0.0824112221598625 | 0.228539524136411 | 5 |
| 935 | 935 | 0.744782984256744 | 0.19762037037037 | 0.0747755914926529 | 0.172933059729916 | 5 |
| 940 | 940 | 0.8193638920784 | 0.127837962962963 | 0.0755274966359138 | 0.286833969583525 | 5 |
| 945 | 945 | 0.574270129203796 | 0.194488017429194 | 0.245327889919281 | 0.446580394645107 | 5 |
| 950 | 950 | 0.574247598648071 | 0.195776688453159 | 0.00224972749128938 | 0.0240319569594991 | 5 |
| 955 | 955 | 0.575055241584778 | 0.195684640522876 | 0.00356045714579523 | 0.0291863548256111 | 5 |
| 960 | 960 | 0.650427222251892 | 0.230641067538126 | 0.129598572850227 | 0.311934382563731 | 5 |
| 965 | 965 | 0.575355887413025 | 0.194718681917211 | 0.129690617322922 | 0.313616523326061 | 5 |
| 970 | 970 | 0.57363349199295 | 0.194741557734205 | 0.00202804990112782 | 0.0240175254448963 | 5 |
| 975 | 975 | 0.575139403343201 | 0.195578431372549 | 0.00325653585605323 | 0.030277734455008 | 5 |
| 980 | 980 | 0.712743997573853 | 0.230482843137255 | 0.166132360696793 | 0.435989284975056 | 5 |
| 985 | 985 | 0.723842322826385 | 0.218578703703704 | 0.0659877359867096 | 0.164228865058944 | 5 |
| 990 | 990 | 0.70965301990509 | 0.23375871459695 | 0.064236655831337 | 0.166111196167107 | 5 |
| 995 | 995 | 0.713260114192963 | 0.204967864923747 | 0.088737741112709 | 0.249431041903115 | 5 |
| 1000 | 1000 | 0.707518756389618 | 0.209108387799564 | 0.0412783212959766 | 0.0665339994458975 | 5 |
| 1005 | 1005 | 0.706243515014648 | 0.229746187363834 | 0.0973728150129318 | 0.239280153948247 | 5 |
| 1010 | 1010 | 0.706216752529144 | 0.233995098039216 | 0.0251230914145708 | 0.0567829520291044 | 5 |
| 1015 | 1015 | 0.709484159946442 | 0.228409041394336 | 0.0273028314113617 | 0.0632604591509017 | 5 |
| 1020 | 1020 | 0.741304457187653 | 0.203722222222222 | 0.0711949840188026 | 0.192068798324814 | 5 |
| 1025 | 1025 | 0.741031885147095 | 0.202227941176471 | 0.0271418839693069 | 0.0578424543332445 | 5 |
| 1030 | 1030 | 0.741597235202789 | 0.202458877995643 | 0.0149330049753189 | 0.0347288011384529 | 5 |
| 1035 | 1035 | 0.705566227436066 | 0.235286764705882 | 0.0747276619076729 | 0.193441935887569 | 5 |
| 1040 | 1040 | 0.705666124820709 | 0.235419662309368 | 0.00484395399689674 | 0.0310938099366402 | 5 |
| 1045 | 1045 | 0.717722535133362 | 0.227578703703704 | 0.0334169380366802 | 0.0607112204879881 | 5 |
| 1050 | 1050 | 0.716912925243378 | 0.227716503267974 | 0.00696868170052767 | 0.0363633796727799 | 5 |
| 1055 | 1055 | 0.746440947055817 | 0.201319444444444 | 0.0708107277750969 | 0.184729738611018 | 5 |
| 1060 | 1060 | 0.706353783607483 | 0.232072984749455 | 0.0720048919320107 | 0.204662264983622 | 5 |
| 1065 | 1065 | 0.72011935710907 | 0.223711328976035 | 0.0686647519469261 | 0.190272720363903 | 5 |
| 1070 | 1070 | 0.708441436290741 | 0.232927015250545 | 0.0649980902671814 | 0.183712295214868 | 5 |
| 1075 | 1075 | 0.712877452373505 | 0.230697984749455 | 0.0242529939860106 | 0.04575309050535 | 5 |
| 1080 | 1080 | 0.746810495853424 | 0.199225217864924 | 0.0752990245819092 | 0.194210773427384 | 5 |
| 1085 | 1085 | 0.689062654972076 | 0.191488562091503 | 0.0883153453469276 | 0.267245276982589 | 5 |
| 1090 | 1090 | 0.691774249076843 | 0.192377723311547 | 0.021092863753438 | 0.0521676011878221 | 5 |
| 1095 | 1095 | 0.706977963447571 | 0.186794117647059 | 0.0731938928365707 | 0.144663690764769 | 5 |
| 1100 | 1100 | 0.644587397575378 | 0.520342320261438 | 0.0939618647098541 | 0.485606750599338 | 5 |
| 1105 | 1105 | 0.686728000640869 | 0.197709967320261 | 0.0907559916377068 | 0.494614835874642 | 5 |
| 1110 | 1110 | 0.691066682338715 | 0.197646786492375 | 0.0249743983149529 | 0.0606397760752422 | 5 |
| 1115 | 1115 | 0.690616607666016 | 0.192901416122004 | 0.00671922694891691 | 0.0659941114975605 | 5 |
| 1120 | 1120 | 0.70309042930603 | 0.188136982570806 | 0.0776938945055008 | 0.144018824504348 | 5 |
| 1125 | 1125 | 0.682317018508911 | 0.202041666666667 | 0.0764994546771049 | 0.133279291644875 | 5 |
| 1130 | 1130 | 0.690543353557587 | 0.196135893246187 | 0.0187933016568422 | 0.044134804826809 | 5 |
| 1135 | 1135 | 0.687861979007721 | 0.196574618736383 | 0.0170533768832684 | 0.0489843669704 | 5 |
| 1140 | 1140 | 0.703288972377777 | 0.191638888888889 | 0.072442814707756 | 0.116712000203503 | 5 |
| 1145 | 1145 | 0.706744492053986 | 0.189940631808279 | 0.0268101841211319 | 0.0485467239723924 | 5 |
| 1150 | 1150 | 0.686986446380615 | 0.196817265795207 | 0.0728518515825272 | 0.134701380146174 | 5 |
| 1155 | 1155 | 0.688569188117981 | 0.19200871459695 | 0.00511383404955268 | 0.0661166306390642 | 5 |
| 1160 | 1160 | 0.693748891353607 | 0.198242102396514 | 0.0267510861158371 | 0.0783046802673502 | 5 |
| 1165 | 1165 | 0.694866240024567 | 0.193380718954248 | 0.00588807230815291 | 0.0675942427637617 | 5 |
| 1170 | 1170 | 0.70082950592041 | 0.196110838779956 | 0.0725525617599487 | 0.143477452415079 | 5 |
| 1175 | 1175 | 0.702711880207062 | 0.191692810457516 | 0.00668518478050828 | 0.0690052383364169 | 5 |
| 1180 | 1180 | 0.685258746147156 | 0.199412309368192 | 0.0741486921906471 | 0.146125572194351 | 5 |
| 1185 | 1185 | 0.689017713069916 | 0.19628839869281 | 0.0139839323237538 | 0.0396905247032069 | 5 |
| 1190 | 1190 | 0.684689521789551 | 0.20113779956427 | 0.0199659578502178 | 0.0535602656720127 | 5 |
| 1195 | 1195 | 0.685514450073242 | 0.19756045751634 | 0.0181010328233242 | 0.049624154470987 | 5 |
| 1200 | 1200 | 0.686554789543152 | 0.197670479302832 | 0.00461710197851062 | 0.0256544396944422 | 5 |
| 1205 | 1205 | 0.689752459526062 | 0.198688725490196 | 0.0225876905024052 | 0.0438211843294486 | 5 |
| 1210 | 1210 | 0.705522298812866 | 0.189259531590414 | 0.0701772794127464 | 0.127354639745194 | 5 |
| 1215 | 1215 | 0.703498661518097 | 0.183549564270153 | 0.0292181354016066 | 0.0744757527078159 | 5 |
| 1220 | 1220 | 0.68427312374115 | 0.195752723311547 | 0.0721693933010101 | 0.133093578508893 | 5 |
| 1225 | 1225 | 0.689205586910248 | 0.196210511982571 | 0.0230822414159775 | 0.0852043380761068 | 5 |
| 1230 | 1230 | 0.699404716491699 | 0.190782679738562 | 0.0692938417196274 | 0.107646787940549 | 5 |
| 1235 | 1235 | 0.688780546188354 | 0.192121732026144 | 0.0714101344347 | 0.133689470143136 | 5 |
| 1240 | 1240 | 0.690021276473999 | 0.196203159041394 | 0.0218376908451319 | 0.0775426685623579 | 5 |
| 1245 | 1245 | 0.689974427223206 | 0.196315631808279 | 0.00675054453313351 | 0.0273909116539403 | 5 |
| 1250 | 1250 | 0.707916378974915 | 0.186268790849673 | 0.0737028867006302 | 0.13225191888676 | 5 |
| 1255 | 1255 | 0.702597498893738 | 0.193946350762527 | 0.031798742711544 | 0.0610577428780519 | 5 |
| 1260 | 1260 | 0.700867652893066 | 0.187709694989107 | 0.0366361662745476 | 0.0615399450205358 | 5 |
| 1265 | 1265 | 0.689721703529358 | 0.191688453159041 | 0.0709531530737877 | 0.132355736330345 | 5 |
| 1270 | 1270 | 0.685450434684753 | 0.194846405228758 | 0.0181465148925781 | 0.0386354432502308 | 5 |
| 1275 | 1275 | 0.703845620155334 | 0.190565631808279 | 0.074358657002449 | 0.145793460599175 | 5 |
| 1280 | 1280 | 0.700302243232727 | 0.193478213507625 | 0.0256751086562872 | 0.0434763928283907 | 5 |
| 1285 | 1285 | 0.687423229217529 | 0.196702614379085 | 0.0710789710283279 | 0.112677241140711 | 5 |
| 1290 | 1290 | 0.687830626964569 | 0.196921840958606 | 0.0063284314237535 | 0.0281732104511025 | 5 |
| 1295 | 1295 | 0.704375267028809 | 0.195823801742919 | 0.0717352852225304 | 0.134024318527258 | 5 |
| 1300 | 1300 | 0.703799843788147 | 0.188815631808279 | 0.0399458073079586 | 0.0855859957775136 | 5 |
| 1305 | 1305 | 0.69057160615921 | 0.19708197167756 | 0.0704079493880272 | 0.119960032013005 | 5 |
| 1310 | 1310 | 0.689625024795532 | 0.197169934640523 | 0.00477287545800209 | 0.0316408940191575 | 5 |
| 1315 | 1315 | 0.686472237110138 | 0.192700163398693 | 0.0164507068693638 | 0.0693319390459711 | 5 |
| 1320 | 1320 | 0.704031825065613 | 0.187287581699346 | 0.0735710710287094 | 0.145160195846594 | 5 |
| 1325 | 1325 | 0.686781644821167 | 0.194011710239651 | 0.0753989592194557 | 0.143779224807261 | 5 |
| 1330 | 1330 | 0.682985842227936 | 0.200702069716776 | 0.0216334406286478 | 0.0718286517807446 | 5 |
| 1335 | 1335 | 0.687855660915375 | 0.196756808278867 | 0.0239978190511465 | 0.048118500926328 | 5 |
| 1340 | 1340 | 0.703830540180206 | 0.188073529411765 | 0.071700431406498 | 0.121140496984497 | 5 |
| 1345 | 1345 | 0.705358684062958 | 0.189001906318083 | 0.0184174831956625 | 0.0385617370710326 | 5 |
| 1350 | 1350 | 0.698647320270538 | 0.195856209150327 | 0.0266535952687263 | 0.0452640111623728 | 5 |
| 1355 | 1355 | 0.644658744335175 | 0.520190904139434 | 0.0920767858624458 | 0.48806220354745 | 5 |
| 1360 | 1360 | 0.647222220897675 | 0.513060729847495 | 0.00321269035339355 | 0.0723093063975921 | 5 |
| 1365 | 1365 | 0.559413135051727 | 0.248242919389978 | 0.124909855425358 | 0.586285655034182 | 5 |
| 1370 | 1370 | 0.56100058555603 | 0.248365196078431 | 0.00429820222780108 | 0.0238365629142647 | 5 |
| 1375 | 1375 | 0.530296623706818 | 0.28368082788671 | 0.0555738024413586 | 0.152026939670761 | 5 |
| 1380 | 1380 | 0.530579268932343 | 0.276714596949891 | 0.0195206981152296 | 0.0784888997543673 | 5 |
| 1385 | 1385 | 0.557987987995148 | 0.256351034858388 | 0.0566228218376637 | 0.144944488130508 | 5 |
| 1390 | 1390 | 0.556816220283508 | 0.257299019607843 | 0.00821432564407587 | 0.0350460191009571 | 5 |
| 1395 | 1395 | 0.560061514377594 | 0.253951797385621 | 0.0188330616801977 | 0.0543552626083687 | 5 |
| 1400 | 1400 | 0.558211326599121 | 0.25427559912854 | 0.0281546842306852 | 0.0703570994061519 | 5 |
| 1405 | 1405 | 0.52612829208374 | 0.281552559912854 | 0.0572535395622253 | 0.149515330474186 | 5 |
| 1410 | 1410 | 0.529432773590088 | 0.283799291938998 | 0.0287211332470179 | 0.0946053834499412 | 5 |
| 1415 | 1415 | 0.529555559158325 | 0.278929466230937 | 0.00376388872973621 | 0.0662109787165413 | 5 |
| 1420 | 1420 | 0.560784339904785 | 0.257366013071895 | 0.0568676516413689 | 0.139794687082601 | 5 |
| 1425 | 1425 | 0.555592060089111 | 0.26031862745098 | 0.0163605660200119 | 0.0326185268090482 | 5 |
| 1430 | 1430 | 0.52556973695755 | 0.283165305010893 | 0.0576078407466412 | 0.147388653898408 | 5 |
| 1435 | 1435 | 0.564624190330505 | 0.253181644880174 | 0.0641421526670456 | 0.163896340133996 | 5 |
| 1440 | 1440 | 0.557725191116333 | 0.259334694989107 | 0.0191446095705032 | 0.0504091206833096 | 5 |
| 1445 | 1445 | 0.45470866560936 | 0.311076797385621 | 0.109299831092358 | 0.319273884859337 | 5 |
| 1450 | 1450 | 0.528324365615845 | 0.284404956427015 | 0.0771075785160065 | 0.299006501456176 | 5 |
| 1455 | 1455 | 0.522398710250854 | 0.291734204793028 | 0.0214463528245687 | 0.0766401550641723 | 5 |
| 1460 | 1460 | 0.524546325206757 | 0.283168300653595 | 0.0132020693272352 | 0.0755761346722233 | 5 |
| 1465 | 1465 | 0.557510077953339 | 0.259136710239651 | 0.0583085529506207 | 0.145481490610118 | 5 |
| 1470 | 1470 | 0.561913967132568 | 0.256363834422658 | 0.0186680313199759 | 0.0429705181576375 | 5 |
| 1475 | 1475 | 0.644586563110352 | 0.520393246187364 | 0.128448262810707 | 0.558084542335591 | 5 |
| 1480 | 1480 | 0.696618974208832 | 0.1787848583878 | 0.0794468894600868 | 0.493587525900174 | 5 |
| 1485 | 1485 | 0.716525077819824 | 0.180034586056645 | 0.0621315352618694 | 0.129446383506823 | 5 |
| 1490 | 1490 | 0.728857040405273 | 0.207076525054466 | 0.0631636679172516 | 0.166671058368387 | 5 |
| 1495 | 1495 | 0.746215164661407 | 0.200188725490196 | 0.0605236887931824 | 0.0940661796069118 | 5 |
| 1500 | 1500 | 0.742254614830017 | 0.204091503267974 | 0.0307845827192068 | 0.0504474710257633 | 5 |
| 1505 | 1505 | 0.741931617259979 | 0.201795751633987 | 0.0247859489172697 | 0.0426902692512813 | 5 |
| 1510 | 1510 | 0.742008984088898 | 0.197110566448802 | 0.0125800650566816 | 0.0727523727688047 | 5 |
| 1515 | 1515 | 0.73140549659729 | 0.205010348583878 | 0.0643747225403786 | 0.106415447365991 | 5 |
| 1520 | 1520 | 0.72394722700119 | 0.206560185185185 | 0.0216881800442934 | 0.0764438757204218 | 5 |
| 1525 | 1525 | 0.650631606578827 | 0.202541666666667 | 0.122320540249348 | 0.262659497560483 | 5 |
| 1530 | 1530 | 0.723782956600189 | 0.206436546840959 | 0.122123636305332 | 0.262515845903715 | 5 |
| 1535 | 1535 | 0.725200474262238 | 0.211457788671024 | 0.00575680797919631 | 0.0698182054039251 | 5 |
| 1540 | 1540 | 0.727513372898102 | 0.203488562091503 | 0.0166691169142723 | 0.0722600539675889 | 5 |
| 1545 | 1545 | 0.746686041355133 | 0.199309368191721 | 0.0627461820840836 | 0.117156821257713 | 5 |
| 1550 | 1550 | 0.746158242225647 | 0.200174019607843 | 0.0120964050292969 | 0.0409518131213453 | 5 |
| 1555 | 1555 | 0.724797368049622 | 0.205535947712418 | 0.0640351250767708 | 0.120727529457679 | 5 |
| 1560 | 1560 | 0.725006520748138 | 0.205204793028322 | 0.0181563161313534 | 0.023098388478951 | 5 |
| 1565 | 1565 | 0.728745102882385 | 0.202006263616558 | 0.0241127442568541 | 0.0377765111418101 | 5 |
| 1570 | 1570 | 0.726718962192535 | 0.204156862745098 | 0.0178159028291702 | 0.0402017505031807 | 5 |
| 1575 | 1575 | 0.741382896900177 | 0.203103758169935 | 0.0632015243172646 | 0.108531504112072 | 5 |
| 1580 | 1580 | 0.742011725902557 | 0.203327614379085 | 0.00744144851341844 | 0.0258914330237469 | 5 |
| 1585 | 1585 | 0.725837409496307 | 0.204822712418301 | 0.0642450898885727 | 0.110562405868535 | 5 |
| 1590 | 1590 | 0.730196118354797 | 0.205220315904139 | 0.0247290302067995 | 0.076759856084837 | 5 |
| 1595 | 1595 | 0.728418290615082 | 0.204024509803922 | 0.0202761441469193 | 0.0738533023814138 | 5 |
| 1600 | 1600 | 0.743355453014374 | 0.20139188453159 | 0.0635825172066689 | 0.104007267229519 | 5 |
| 1605 | 1605 | 0.746652245521545 | 0.197376906318083 | 0.028531588613987 | 0.0778428664272647 | 5 |
| 1610 | 1610 | 0.739932775497437 | 0.207082788671024 | 0.033594224601984 | 0.0803846280548329 | 5 |
| 1615 | 1615 | 0.725852131843567 | 0.204998366013072 | 0.0661661252379417 | 0.106986051913046 | 5 |
| 1620 | 1620 | 0.724781274795532 | 0.205071078431373 | 0.00969662237912416 | 0.0272630452729779 | 5 |
| 1625 | 1625 | 0.741744220256805 | 0.203294117647059 | 0.065307728946209 | 0.11068051729666 | 5 |
| 1630 | 1630 | 0.728359758853912 | 0.202385348583878 | 0.0613779947161674 | 0.106915811931832 | 5 |
| 1635 | 1635 | 0.724697768688202 | 0.206568899782135 | 0.0197214037179947 | 0.0396498394630657 | 5 |
| 1640 | 1640 | 0.729031026363373 | 0.206714324618736 | 0.02122494392097 | 0.072872292406419 | 5 |
| 1645 | 1645 | 0.72810971736908 | 0.201932734204793 | 0.00590658979490399 | 0.0676625281050032 | 5 |
| 1650 | 1650 | 0.744224905967712 | 0.200692265795207 | 0.0638935118913651 | 0.11146484171559 | 5 |
| 1655 | 1655 | 0.744525015354156 | 0.207813453159041 | 0.0691928043961525 | 0.151255121739802 | 5 |
| 1660 | 1660 | 0.729665338993073 | 0.207720860566449 | 0.0840863212943077 | 0.202648171812399 | 5 |
| 1665 | 1665 | 0.748052299022675 | 0.195494008714597 | 0.0621053911745548 | 0.113975866293416 | 5 |
| 1670 | 1670 | 0.742252767086029 | 0.198025871459695 | 0.031355120241642 | 0.0527235491938507 | 5 |
| 1675 | 1675 | 0.745304763317108 | 0.201687908496732 | 0.0273292474448681 | 0.0787768541218207 | 5 |
| 1680 | 1680 | 0.697449624538422 | 0.174536220043573 | 0.0820969492197037 | 0.232620664705743 | 5 |
| 1685 | 1685 | 0.703964293003082 | 0.177180555555556 | 0.0272156856954098 | 0.0744907002614927 | 5 |
| 1690 | 1690 | 0.693378269672394 | 0.179618464052288 | 0.0266715660691261 | 0.0488857149999036 | 5 |
| 1695 | 1695 | 0.692987203598022 | 0.179759531590414 | 0.00372712407261133 | 0.0230371316533796 | 5 |
| 1700 | 1700 | 0.724102735519409 | 0.176505174291939 | 0.0667107850313187 | 0.12651994402916 | 5 |
| 1705 | 1705 | 0.721196889877319 | 0.178934640522876 | 0.0249291937798262 | 0.0440844303895591 | 5 |
| 1710 | 1710 | 0.699904084205627 | 0.177495098039216 | 0.0635776147246361 | 0.124426996841093 | 5 |
| 1715 | 1715 | 0.697339057922363 | 0.177858932461874 | 0.0173575691878796 | 0.0356450457447128 | 5 |
| 1720 | 1720 | 0.698964297771454 | 0.177093409586057 | 0.0172859467566013 | 0.0398881072012444 | 5 |
| 1725 | 1725 | 0.700495660305023 | 0.172487745098039 | 0.00554275559261441 | 0.0668391916205357 | 5 |
| 1730 | 1730 | 0.69620156288147 | 0.179843137254902 | 0.0184520687907934 | 0.0776456580135327 | 5 |
| 1735 | 1735 | 0.724912583827972 | 0.177328431372549 | 0.0655525624752045 | 0.121866751268791 | 5 |
| 1740 | 1740 | 0.726452350616455 | 0.177726034858388 | 0.0349008701741695 | 0.0412992276668866 | 5 |
| 1745 | 1745 | 0.726763665676117 | 0.177903050108932 | 0.00952641572803259 | 0.0256626087234869 | 5 |
| 1750 | 1750 | 0.701514482498169 | 0.173358932461874 | 0.0630373060703278 | 0.138441694884903 | 5 |
| 1755 | 1755 | 0.696986079216003 | 0.179172930283224 | 0.0267478208988905 | 0.0760684682755279 | 5 |
| 1760 | 1760 | 0.594868421554565 | 0.209645152505447 | 0.121972769498825 | 0.303665204814179 | 5 |
| 1765 | 1765 | 0.5963374376297 | 0.208032679738562 | 0.0150288669392467 | 0.0823690021773035 | 5 |
| 1770 | 1770 | 0.702086091041565 | 0.176091503267974 | 0.122426740825176 | 0.311852189978682 | 5 |
| 1775 | 1775 | 0.708567023277283 | 0.183125 | 0.0763769000768661 | 0.173662336266385 | 5 |
| 1780 | 1780 | 0.713744580745697 | 0.183876089324619 | 0.0518235266208649 | 0.0583377287801799 | 5 |
| 1785 | 1785 | 0.723943710327148 | 0.172300108932462 | 0.0631195530295372 | 0.13795112002995 | 5 |
| 1790 | 1790 | 0.663587093353271 | 0.17816339869281 | 0.0898935124278069 | 0.173947368942803 | 5 |
| 1795 | 1795 | 0.69881534576416 | 0.172977124183007 | 0.0382287539541721 | 0.140405516885095 | 5 |
| 1800 | 1800 | 0.718491077423096 | 0.185455065359477 | 0.0677154064178467 | 0.14529029766327 | 5 |
| 1805 | 1805 | 0.721321880817413 | 0.178654956427015 | 0.0267279408872128 | 0.0519991477598501 | 5 |
| 1810 | 1810 | 0.7262943983078 | 0.176955065359477 | 0.0278325136750937 | 0.0415488239780859 | 5 |
| 1815 | 1815 | 0.702087223529816 | 0.170623093681917 | 0.0639583319425583 | 0.136560287404188 | 5 |
| 1820 | 1820 | 0.700901687145233 | 0.17601688453159 | 0.00499754911288619 | 0.0626925560757 | 5 |
| 1825 | 1825 | 0.721108138561249 | 0.184912037037037 | 0.0649803951382637 | 0.136467729468929 | 5 |
| 1830 | 1830 | 0.701112747192383 | 0.178458333333333 | 0.0651729255914688 | 0.137846665650708 | 5 |
| 1835 | 1835 | 0.703498661518097 | 0.17171105664488 | 0.0211544129997492 | 0.0755654628261985 | 5 |
| 1840 | 1840 | 0.703606784343719 | 0.170824346405229 | 0.00724645936861634 | 0.030610354215874 | 5 |
| 1845 | 1845 | 0.722105979919434 | 0.176811819172113 | 0.0629093125462532 | 0.140636369340103 | 5 |
| 1850 | 1850 | 0.698106229305267 | 0.174192265795207 | 0.064489372074604 | 0.145705429416162 | 5 |
| 1855 | 1855 | 0.699951529502869 | 0.175980664488017 | 0.0181176457554102 | 0.0739551135934023 | 5 |
| 1860 | 1860 | 0.701964139938354 | 0.171511437908497 | 0.0054411762394011 | 0.0628465027951896 | 5 |
| 1865 | 1865 | 0.717799544334412 | 0.177717864923747 | 0.0597472712397575 | 0.149120652923021 | 5 |
| 1870 | 1870 | 0.719548523426056 | 0.180476579520697 | 0.0296356193721294 | 0.0677092802391732 | 5 |
| 1875 | 1875 | 0.697565078735352 | 0.17863371459695 | 0.0640291348099709 | 0.129321546532694 | 5 |
| 1880 | 1880 | 0.697537302970886 | 0.178564270152505 | 0.00394716765731573 | 0.0231021159483816 | 5 |
| 1885 | 1885 | 0.697702884674072 | 0.17298311546841 | 0.0203714575618505 | 0.0683491097749 | 5 |
| 1890 | 1890 | 0.725699067115784 | 0.176650326797386 | 0.067474402487278 | 0.14138090608714 | 5 |
| 1895 | 1895 | 0.718964040279388 | 0.18473311546841 | 0.0222840420901775 | 0.0553162249588461 | 5 |
| 1900 | 1900 | 0.735968172550201 | 0.192317810457516 | 0.0704724863171577 | 0.127571698706975 | 5 |
| 1905 | 1905 | 0.736041665077209 | 0.193587418300654 | 0.0431356206536293 | 0.087394675942353 | 5 |
| 1910 | 1910 | 0.728637278079987 | 0.195720315904139 | 0.0794365406036377 | 0.171442814489025 | 5 |
| 1915 | 1915 | 0.730190932750702 | 0.207025871459695 | 0.0751446038484573 | 0.096159448748796 | 5 |
| 1920 | 1920 | 0.720171570777893 | 0.206936819172113 | 0.0416282638907433 | 0.0893834826796004 | 5 |
| 1925 | 1925 | 0.740635633468628 | 0.188168572984749 | 0.0609547942876816 | 0.159801348768486 | 5 |
| 1930 | 1930 | 0.733682990074158 | 0.18566802832244 | 0.0472358353435993 | 0.115463849061475 | 5 |
| 1935 | 1935 | 0.734980463981628 | 0.188337690631808 | 0.0583164468407631 | 0.129415289772231 | 5 |
| 1940 | 1940 | 0.726599097251892 | 0.173377995642702 | 0.0678965076804161 | 0.144216412714143 | 5 |
| 1945 | 1945 | 0.728594481945038 | 0.194977668845316 | 0.0716075673699379 | 0.159465114563318 | 5 |
| 1950 | 1950 | 0.693654716014862 | 0.228692810457516 | 0.0910133346915245 | 0.216764699487046 | 5 |
| 1955 | 1955 | 0.703542470932007 | 0.218686002178649 | 0.0333823524415493 | 0.0573869901422962 | 5 |
| 1960 | 1960 | 0.731635093688965 | 0.174953976034858 | 0.0680762454867363 | 0.208636313831605 | 5 |
| 1965 | 1965 | 0.740089654922485 | 0.183149237472767 | 0.0672186762094498 | 0.151564493931334 | 5 |
| 1970 | 1970 | 0.740198314189911 | 0.183053104575163 | 0.0121533228084445 | 0.0271094802384687 | 5 |
| 1975 | 1975 | 0.726065695285797 | 0.174911492374728 | 0.0676386207342148 | 0.131014042923732 | 5 |
| 1980 | 1980 | 0.142785400152206 | 0.512897603485839 | 0.601441502571106 | 0.951132093762428 | 5 |
| 1985 | 1985 | 0.387635856866837 | 0.223954793028322 | 0.290087401866913 | 0.562718936446606 | 5 |
| 1990 | 1990 | 0.414459973573685 | 0.153603758169935 | 0.135211318731308 | 0.407359895932835 | 5 |
| 1995 | 1995 | 0.452006578445435 | 0.280121459694989 | 0.204219773411751 | 0.496003643425122 | 5 |
| 2000 | 2000 | 0.364091783761978 | 0.329617647058824 | 0.215191453695297 | 0.477586691046126 | 5 |
| 2005 | 2005 | 0.559089303016663 | 0.193925653594771 | 0.421319454908371 | 0.564905343277222 | 5 |
| 2010 | 2010 | 0.600030243396759 | 0.19515522875817 | 0.073794387280941 | 0.151740192594313 | 5 |
| 2015 | 2015 | 0.595116019248962 | 0.198953703703704 | 0.0538766346871853 | 0.0836148821745224 | 5 |
| 2020 | 2020 | 0.563317000865936 | 0.188804193899782 | 0.0726111084222794 | 0.148189407342486 | 5 |
| 2025 | 2025 | 0.562822997570038 | 0.191574891067538 | 0.033887255936861 | 0.0868172551827689 | 5 |
| 2030 | 2030 | 0.559845566749573 | 0.185822984749455 | 0.0219893772155046 | 0.0702688642844254 | 5 |
| 2035 | 2035 | 0.593422651290894 | 0.190287309368192 | 0.0693434104323387 | 0.137530172485316 | 5 |
| 2040 | 2040 | 0.557571053504944 | 0.184877450980392 | 0.0713537633419037 | 0.141691892262929 | 5 |
| 2045 | 2045 | 0.559855699539185 | 0.183903322440087 | 0.00699373614042997 | 0.0312562953509102 | 5 |
| 2050 | 2050 | 0.591709196567535 | 0.200173474945534 | 0.0725032687187195 | 0.137726005343214 | 5 |
| 2055 | 2055 | 0.55987149477005 | 0.191377450980392 | 0.069960243999958 | 0.125698704891838 | 5 |
| 2060 | 2060 | 0.560325741767883 | 0.191756535947712 | 0.0200364887714386 | 0.0385561515216078 | 5 |
| 2065 | 2065 | 0.559499502182007 | 0.184822440087146 | 0.00590577349066734 | 0.0684779176042982 | 5 |
| 2070 | 2070 | 0.561488032341003 | 0.19039188453159 | 0.00657407380640507 | 0.0666099070595954 | 5 |
| 2075 | 2075 | 0.560630738735199 | 0.190643246187364 | 0.0188235305249691 | 0.0382833386890514 | 5 |
| 2080 | 2080 | 0.591932773590088 | 0.194837145969499 | 0.0688815414905548 | 0.135222518879572 | 5 |
| 2085 | 2085 | 0.595309913158417 | 0.193528322440087 | 0.0250727124512196 | 0.0809220205036409 | 5 |
| 2090 | 2090 | 0.591561913490295 | 0.196148692810458 | 0.0333080068230629 | 0.0904339604971121 | 5 |
| 2095 | 2095 | 0.561559081077576 | 0.186061274509804 | 0.0679809376597404 | 0.135754163084683 | 5 |
| 2100 | 2100 | 0.559512794017792 | 0.189074074074074 | 0.0137287583202124 | 0.0381564164422308 | 5 |
| 2105 | 2105 | 0.58983963727951 | 0.200110294117647 | 0.067168302834034 | 0.132330012384792 | 5 |
| 2110 | 2110 | 0.590833902359009 | 0.196145152505447 | 0.0289855655282736 | 0.0510867422977519 | 5 |
| 2115 | 2115 | 0.590225517749786 | 0.193930283224401 | 0.0311274509876966 | 0.046729656043556 | 5 |
| 2120 | 2120 | 0.558774530887604 | 0.191555555555556 | 0.0689433515071869 | 0.133384956801487 | 5 |
| 2125 | 2125 | 0.559658765792847 | 0.189336873638344 | 0.00707652466371655 | 0.0324821820074305 | 5 |
| 2130 | 2130 | 0.561752438545227 | 0.191976307189542 | 0.0251748356968164 | 0.0404379132113661 | 5 |
| 2135 | 2135 | 0.562422096729279 | 0.188406590413943 | 0.0271190088242292 | 0.0888657680722491 | 5 |
| 2140 | 2140 | 0.587504923343658 | 0.190923474945534 | 0.0624003261327744 | 0.101890106309774 | 5 |
| 2145 | 2145 | 0.557937443256378 | 0.185328703703704 | 0.0656241849064827 | 0.122523202919411 | 5 |
| 2150 | 2150 | 0.561970055103302 | 0.191220588235294 | 0.0252015236765146 | 0.0706445753035713 | 5 |
| 2155 | 2155 | 0.561134278774261 | 0.192699074074074 | 0.00587336625903845 | 0.0330948975107971 | 5 |
| 2160 | 2160 | 0.562050104141235 | 0.187815631808279 | 0.00630364846438169 | 0.069491301067761 | 5 |
| 2165 | 2165 | 0.591802597045898 | 0.197108387799564 | 0.0694463551044464 | 0.149915706900285 | 5 |
| 2170 | 2170 | 0.588428676128387 | 0.195440087145969 | 0.0275236926972866 | 0.0453471625317603 | 5 |
| 2175 | 2175 | 0.700030267238617 | 0.196667211328976 | 0.153933271765709 | 0.361968198676478 | 5 |
| 2180 | 2180 | 0.719668090343475 | 0.195804466230937 | 0.0506933517754078 | 0.0998045491140745 | 5 |
| 2185 | 2185 | 0.719420433044434 | 0.188970043572985 | 0.0354528836905956 | 0.0786799287920434 | 5 |
| 2190 | 2190 | 0.694397389888763 | 0.186544389978214 | 0.0782159566879272 | 0.134810689031394 | 5 |
| 2195 | 2195 | 0.697012543678284 | 0.220216503267974 | 0.0981603935360909 | 0.26832259735371 | 5 |
| 2200 | 2200 | 0.70115464925766 | 0.212778594771242 | 0.0686105638742447 | 0.160595355876066 | 5 |
| 2205 | 2205 | 0.703464925289154 | 0.186804193899782 | 0.0861157402396202 | 0.249635859943862 | 5 |
| 2210 | 2210 | 0.705890595912933 | 0.190835784313725 | 0.0329005979001522 | 0.0577024101593451 | 5 |
| 2215 | 2215 | 0.702407717704773 | 0.18714651416122 | 0.0329452604055405 | 0.0609871186360949 | 5 |
| 2220 | 2220 | 0.685383975505829 | 0.214962418300654 | 0.071828156709671 | 0.233475828819697 | 5 |
| 2225 | 2225 | 0.701413989067078 | 0.198976307189542 | 0.0845833346247673 | 0.202858445906508 | 5 |
| 2230 | 2230 | 0.679497539997101 | 0.205029684095861 | 0.074113555252552 | 0.160404190854815 | 5 |
| 2235 | 2235 | 0.698893487453461 | 0.203188180827887 | 0.0677663385868073 | 0.173993395754463 | 5 |
| 2240 | 2240 | 0.68425053358078 | 0.201097766884532 | 0.0681004822254181 | 0.17594196641116 | 5 |
| 2245 | 2245 | 0.683249533176422 | 0.201259531590414 | 0.0182930286973715 | 0.029166306756955 | 5 |
| 2250 | 2250 | 0.681188225746155 | 0.203593681917211 | 0.0212600752711296 | 0.0340141385832069 | 5 |
| 2255 | 2255 | 0.703314006328583 | 0.190869281045752 | 0.0668540224432945 | 0.149872149410816 | 5 |
| 2260 | 2260 | 0.684054791927338 | 0.204647331154684 | 0.0794591456651688 | 0.190495912908464 | 5 |
| 2265 | 2265 | 0.680790066719055 | 0.203175925925926 | 0.0709123089909554 | 0.185999781875284 | 5 |
| 2270 | 2270 | 0.686676144599915 | 0.199252178649237 | 0.0237761437892914 | 0.0527312035911297 | 5 |
| 2275 | 2275 | 0.68315851688385 | 0.218149237472767 | 0.0738412290811539 | 0.188449308158217 | 5 |
| 2280 | 2280 | 0.695918023586273 | 0.201763616557734 | 0.07112717628479 | 0.145004303874525 | 5 |
| 2285 | 2285 | 0.693890273571014 | 0.206535130718954 | 0.0272194966673851 | 0.0390815418532683 | 5 |
| 2290 | 2290 | 0.685981214046478 | 0.199558006535948 | 0.0690566450357437 | 0.180751823385118 | 5 |
| 2295 | 2295 | 0.688156306743622 | 0.216863834422658 | 0.0713003799319267 | 0.19811592008386 | 5 |
| 2300 | 2300 | 0.685329794883728 | 0.216828431372549 | 0.0153875285759568 | 0.0471818105264208 | 5 |
| 2305 | 2305 | 0.683049023151398 | 0.221474128540305 | 0.0200182441622019 | 0.0494506792062121 | 5 |
| 2310 | 2310 | 0.689788401126862 | 0.196562363834423 | 0.0721239075064659 | 0.197613223861446 | 5 |
| 2315 | 2315 | 0.711195886135101 | 0.183668572984749 | 0.0603899769484997 | 0.134502325858226 | 5 |
| 2320 | 2320 | 0.706302642822266 | 0.182681644880174 | 0.0380326770246029 | 0.0653947515105952 | 5 |
| 2325 | 2325 | 0.682650089263916 | 0.219661220043573 | 0.0720996707677841 | 0.234557272520441 | 5 |
| 2330 | 2330 | 0.688162863254547 | 0.213424836601307 | 0.024665305390954 | 0.0687238164640704 | 5 |
| 2335 | 2335 | 0.687900364398956 | 0.213575435729847 | 0.00291176489554346 | 0.0171446023987607 | 5 |
| 2340 | 2340 | 0.690461814403534 | 0.203183278867102 | 0.0726209059357643 | 0.13334258669813 | 5 |
| 2345 | 2345 | 0.695340692996979 | 0.201800108932462 | 0.0452671572566032 | 0.06121361001435 | 5 |
| 2350 | 2350 | 0.687446713447571 | 0.215453431372549 | 0.0707519054412842 | 0.14271699828047 | 5 |
| 2355 | 2355 | 0.682515501976013 | 0.219904139433551 | 0.0271604023873806 | 0.0654659166993304 | 5 |
| 2360 | 2360 | 0.688607037067413 | 0.213599945533769 | 0.026437908411026 | 0.0758596142207791 | 5 |
| 2365 | 2365 | 0.703494012355804 | 0.189239106753813 | 0.071745365858078 | 0.196251483406049 | 5 |
| 2370 | 2370 | 0.709822475910187 | 0.186080337690632 | 0.0390876866877079 | 0.0499545107180102 | 5 |
| 2375 | 2375 | 0.684016942977905 | 0.218871187363834 | 0.0737303867936134 | 0.224401200776618 | 5 |
| 2380 | 2380 | 0.685808539390564 | 0.216139705882353 | 0.0165618192404509 | 0.0476445917818191 | 5 |
| 2385 | 2385 | 0.686749458312988 | 0.218885076252723 | 0.0165138877928257 | 0.0470436722593834 | 5 |
| 2390 | 2390 | 0.688289999961853 | 0.197641067538126 | 0.0697649791836739 | 0.196109457533647 | 5 |
| 2395 | 2395 | 0.693847000598907 | 0.206186819172113 | 0.0712856724858284 | 0.180673433123146 | 5 |
| 2400 | 2400 | 0.70727813243866 | 0.181653594771242 | 0.0705525577068329 | 0.199002428073358 | 5 |
| 2405 | 2405 | 0.685977637767792 | 0.217659041394336 | 0.0738662779331207 | 0.226455099798332 | 5 |
| 2410 | 2410 | 0.695345342159271 | 0.195988834422658 | 0.0776971653103828 | 0.241554658781273 | 5 |
| 2415 | 2415 | 0.720126688480377 | 0.196083061002179 | 0.0740269646048546 | 0.180884575828821 | 5 |
| 2420 | 2420 | 0.730723857879639 | 0.212850490196078 | 0.0655427575111389 | 0.221822860223527 | 5 |
| 2425 | 2425 | 0.70306807756424 | 0.199298202614379 | 0.0883736312389374 | 0.16618996666168 | 5 |
| 2430 | 2430 | 0.703940391540527 | 0.202197167755991 | 0.0796391665935516 | 0.105086471542292 | 5 |
| 2435 | 2435 | 0.683480679988861 | 0.20939188453159 | 0.0881998836994171 | 0.161161138253449 | 5 |
| 2440 | 2440 | 0.685104846954346 | 0.228288671023965 | 0.064855121076107 | 0.137943027649503 | 5 |
| 2445 | 2445 | 0.719807803630829 | 0.191253540305011 | 0.0745351314544678 | 0.279786874752361 | 5 |
| 2450 | 2450 | 0.687792181968689 | 0.200642701525054 | 0.0654038637876511 | 0.24002520777033 | 5 |
| 2455 | 2455 | 0.719830632209778 | 0.178805283224401 | 0.0769501551985741 | 0.194741609281996 | 5 |
| 2460 | 2460 | 0.705087184906006 | 0.209851034858388 | 0.0690217837691307 | 0.16516657629406 | 5 |
| 2465 | 2465 | 0.712950706481934 | 0.198475762527233 | 0.0758918821811676 | 0.160803478037477 | 5 |
| 2470 | 2470 | 0.700527191162109 | 0.191226307189543 | 0.0782747715711594 | 0.194814934544249 | 5 |
| 2475 | 2475 | 0.721048772335052 | 0.201638616557734 | 0.0858156308531761 | 0.199119474905631 | 5 |
| 2480 | 2480 | 0.444851845502853 | 0.237627450980392 | 0.276196926832199 | 0.55515345573616 | 5 |
| 2485 | 2485 | 0.169778868556023 | 0.651056644880174 | 0.381312668323517 | 0.808764073848106 | 5 |
| 2490 | 2490 | 0.473164469003677 | 0.164022058823529 | 0.323936849832535 | 0.761709050857123 | 5 |
| 2495 | 2495 | 0.498586088418961 | 0.374684912854031 | 0.243703156709671 | 0.758263712434253 | 5 |
| 2500 | 2500 | 0.654072463512421 | 0.352343681917211 | 0.237826809287071 | 0.658919982518262 | 5 |
| 2505 | 2505 | 0.304103523492813 | 0.428342047930283 | 0.372100234031677 | 0.733526043535727 | 5 |
| 2510 | 2510 | 0.787759900093079 | 0.1506598583878 | 0.537752747535706 | 0.838191517352912 | 5 |
| 2515 | 2515 | 0.828527569770813 | 0.12091802832244 | 0.179707780480385 | 0.523672145342529 | 5 |
| 2520 | 2520 | 0.820119261741638 | 0.176154956427015 | 0.138516068458557 | 0.519333233904821 | 5 |
| 2525 | 2525 | 0.830008685588837 | 0.180322440087146 | 0.0740604549646378 | 0.144155518004772 | 5 |
| 2530 | 2530 | 0.656977951526642 | 0.236444444444444 | 0.203836873173714 | 0.694307872627432 | 5 |
| 2535 | 2535 | 0.69920426607132 | 0.182748093681917 | 0.158138066530228 | 0.632149799395118 | 5 |
| 2540 | 2540 | 0.885349929332733 | 0.0762785947712418 | 0.213237196207047 | 0.579630133269048 | 5 |
| 2545 | 2545 | 0.853798031806946 | 0.0960645424836601 | 0.0949969962239265 | 0.174107182355056 | 5 |
| 2550 | 2550 | 0.833505988121033 | 0.155545479302832 | 0.130176469683647 | 0.498261499236862 | 5 |
| 2555 | 2555 | 0.827418863773346 | 0.111095315904139 | 0.109901413321495 | 0.575848974091432 | 5 |
| 2560 | 2560 | 0.904849171638489 | 0.0808145424836601 | 0.116126358509064 | 0.502126655520612 | 5 |
| 2565 | 2565 | 0.898662328720093 | 0.0840697167755991 | 0.0646002143621445 | 0.103257275145176 | 5 |
| 2570 | 2570 | 0.704874217510223 | 0.214876089324619 | 0.231458604335785 | 0.561952547144654 | 5 |
| 2575 | 2575 | 0.734753310680389 | 0.217132080610022 | 0.142232045531273 | 0.348943271695677 | 5 |
| 2580 | 2580 | 0.694506824016571 | 0.202489106753813 | 0.0918820798397064 | 0.344541039772339 | 5 |
| 2585 | 2585 | 0.73921126127243 | 0.220499183006536 | 0.159067809581757 | 0.518732675606998 | 5 |
| 2590 | 2590 | 0.856192290782928 | 0.101835511982571 | 0.182126358151436 | 0.433343314945929 | 5 |
| 2595 | 2595 | 0.870705962181091 | 0.0986350762527233 | 0.100468412041664 | 0.202187964708486 | 5 |
| 2600 | 2600 | 0.573204815387726 | 0.375330337690632 | 0.334486395120621 | 0.624182564441465 | 5 |
| 2605 | 2605 | 0.723162829875946 | 0.244019063180828 | 0.209539219737053 | 0.689080811204299 | 5 |
| 2610 | 2610 | 0.633930504322052 | 0.32606862745098 | 0.339780211448669 | 0.854153385731913 | 5 |
| 2615 | 2615 | 0.743171334266663 | 0.240054193899782 | 0.219543039798737 | 0.911689108759388 | 5 |
| 2620 | 2620 | 0.72587251663208 | 0.213043300653595 | 0.225004062056541 | 0.526707667594357 | 5 |
| 2625 | 2625 | 0.604157686233521 | 0.341259531590414 | 0.309617906808853 | 0.582327123717702 | 5 |
| 2630 | 2630 | 0.735575139522552 | 0.474043572984749 | 0.224989384412766 | 0.80038393984835 | 5 |
| 2635 | 2635 | 0.539433598518372 | 0.497052832244009 | 0.271906852722168 | 0.989431306381204 | 5 |
| 2640 | 2640 | 0.740260362625122 | 0.144759803921569 | 0.255651950836182 | 0.908686748304846 | 5 |
| 2645 | 2645 | 0.705845355987549 | 0.286294117647059 | 0.214844763278961 | 0.611470576624065 | 5 |
| 2650 | 2650 | 0.694646537303925 | 0.288190631808279 | 0.120264165103436 | 0.299002126189844 | 5 |
| 2655 | 2655 | 0.852175354957581 | 0.110684640522876 | 0.22680501639843 | 0.770888609134288 | 5 |
| 2660 | 2660 | 0.352659851312637 | 0.423338779956427 | 0.508422911167145 | 0.910829754488935 | 5 |
| 2665 | 2665 | 0.61379873752594 | 0.246794662309368 | 0.381844788789749 | 0.608965371794846 | 5 |
| 2670 | 2670 | 0.504920542240143 | 0.229407407407407 | 0.293101578950882 | 0.394036913102154 | 5 |
| 2675 | 2675 | 0.477899223566055 | 0.543971949891068 | 0.1834896504879 | 0.949045864012256 | 5 |
| 2680 | 2680 | 0.341923773288727 | 0.551525871459695 | 0.137573525309563 | 0.933149892979587 | 5 |
| 2685 | 2685 | 0 | 0 | 0.341923773288727 | 1 | 5 |


## Record 03 — H12: whole_song_reproduction_check

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 5c3cdac2904206f45996397dd0d4226912fb85bd10f8ae941bfe6283ed0121fd |
| started_utc | 2026-09-10T06:24:46.985751+00:00 |
| completed_utc | 2026-09-10T06:25:13.230335+00:00 |
| source_id | 1Y5zbtbMqqZw8K12HjP5Up_54Ce3jWjBk |
| character | HIRO |
| alias | H12 |
| label | whole_song_reproduction_check |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「光景」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| filename | 4K HDR「光景」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| size_bytes | 57565410 |
| sha256 | 346649b3c41f8cf987125c344e09d29f1818187240132acfbc5eed89d854462c |
| start_s | 0 |
| end_s | 175.264218 |
| duration_s | 175.264218 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 346649b3c41f8cf987125c344e09d29f1818187240132acfbc5eed89d854462c |
| source_id | 1Y5zbtbMqqZw8K12HjP5Up_54Ce3jWjBk |
| character | HIRO |
| alias | H12 |
| label | whole_song_reproduction_check |
| boundary_note | N/A |
| parameters.method_version | 2026-09-10-v1 |
| parameters.audio_sr_hz | 22050 |
| parameters.nfft | 2048 |
| parameters.hop | 512 |
| parameters.fft_window | periodic Hann |
| parameters.custom_spectral_center | false |
| parameters.rms_percentile_method | linear |
| parameters.rms_floor | 1e-12 |
| parameters.flatness_power_floor | 1e-10 |
| parameters.cv_ddof | 0 |
| parameters.audio_stream | first (0:a:0) |
| parameters.audio_signal | full unseparated mix, mono for features; native channels for R128 |
| parameters.trim_order | decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim |
| parameters.loudness_filter | ebur128=peak=true |
| parameters.silence_filter | silencedetect=noise=-50dB:d=0.5 |
| parameters.start_s | 0 |
| parameters.end_s | N/A |
| parameters.music | true |
| parameters.visual_step_s | 5 |
| parameters.skip_visual | false |
| parameters.visual_size[0] | 160 |
| parameters.visual_size[1] | 90 |
| parameters.visual_resize | INTER_AREA, whole frame with aspect distortion |
| parameters.visual_grayscale | OpenCV BGR2GRAY /255 |
| parameters.visual_saturation | OpenCV HSV S/255 |
| parameters.histogram | 8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5 |
| parameters.ffmpeg_threads | 1 |
| parameters.music_parameters.onset | librosa onset_strength; center=True; aggregate=mean |
| parameters.music_parameters.beat | start_bpm120, tightness100, trim=True |
| parameters.music_parameters.local_tempo | start_bpm120,std_bpm1,ac_size8,max_tempo320,aggregate=None |
| parameters.music_parameters.chroma | chroma_stft,tuning0,norm1,center=True |
| parameters.music_parameters.tonnetz | 6D coordinates from chroma_stft, adjacent Euclidean distance |
| software.python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| software.platform | Windows-11-10.0.26200-SP0 |
| software.numpy | 2.1.2 |
| software.ffmpeg_command | ffmpeg |
| software.ffprobe_command | ffprobe |
| software.ffmpeg_version | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101<br><br>Exiting with exit code 0 |
| software.ffprobe_version | ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101 |
| software.opencv | 4.13.0 |
| software.librosa | 1.0.0 |
| software.scipy | 1.18.0 |
| script_sha256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


### Source probe

| Probe field | Value |
| --- | --- |
| streams[0].index | 0 |
| streams[0].codec_name | h264 |
| streams[0].codec_long_name | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 |
| streams[0].profile | High |
| streams[0].codec_type | video |
| streams[0].codec_tag_string | avc1 |
| streams[0].codec_tag | 0x31637661 |
| streams[0].mime_codec_string | avc1.640020 |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
| streams[0].pix_fmt | yuv420p |
| streams[0].level | 32 |
| streams[0].color_range | tv |
| streams[0].color_space | bt709 |
| streams[0].color_transfer | bt709 |
| streams[0].color_primaries | bt709 |
| streams[0].chroma_location | left |
| streams[0].field_order | progressive |
| streams[0].is_avc | true |
| streams[0].nal_length_size | 4 |
| streams[0].id | 0x1 |
| streams[0].r_frame_rate | 60/1 |
| streams[0].avg_frame_rate | 60/1 |
| streams[0].time_base | 1/15360 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 2691072 |
| streams[0].duration | 175.200000 |
| streams[0].bit_rate | 2419182 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 10512 |
| streams[0].extradata_size | 43 |
| streams[0].disposition.default | 1 |
| streams[0].disposition.dub | 0 |
| streams[0].disposition.original | 0 |
| streams[0].disposition.comment | 0 |
| streams[0].disposition.lyrics | 0 |
| streams[0].disposition.karaoke | 0 |
| streams[0].disposition.forced | 0 |
| streams[0].disposition.hearing_impaired | 0 |
| streams[0].disposition.visual_impaired | 0 |
| streams[0].disposition.clean_effects | 0 |
| streams[0].disposition.attached_pic | 0 |
| streams[0].disposition.timed_thumbnails | 0 |
| streams[0].disposition.non_diegetic | 0 |
| streams[0].disposition.captions | 0 |
| streams[0].disposition.descriptions | 0 |
| streams[0].disposition.metadata | 0 |
| streams[0].disposition.dependent | 0 |
| streams[0].disposition.still_image | 0 |
| streams[0].disposition.multilayer | 0 |
| streams[0].tags.language | und |
| streams[0].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[0].side_data_list[0].side_data_type | Content light level metadata |
| streams[0].side_data_list[0].max_content | 1000 |
| streams[0].side_data_list[0].max_average | 200 |
| streams[1].index | 1 |
| streams[1].codec_name | aac |
| streams[1].codec_long_name | AAC (Advanced Audio Coding) |
| streams[1].profile | LC |
| streams[1].codec_type | audio |
| streams[1].codec_tag_string | mp4a |
| streams[1].codec_tag | 0x6134706d |
| streams[1].mime_codec_string | mp4a.40.2 |
| streams[1].sample_fmt | fltp |
| streams[1].sample_rate | 44100 |
| streams[1].channels | 2 |
| streams[1].channel_layout | stereo |
| streams[1].bits_per_sample | 0 |
| streams[1].initial_padding | 0 |
| streams[1].id | 0x2 |
| streams[1].r_frame_rate | 0/0 |
| streams[1].avg_frame_rate | 0/0 |
| streams[1].time_base | 1/44100 |
| streams[1].start_pts | 0 |
| streams[1].start_time | 0.000000 |
| streams[1].duration_ts | 7729152 |
| streams[1].duration | 175.264218 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 7548 |
| streams[1].extradata_size | 16 |
| streams[1].disposition.default | 1 |
| streams[1].disposition.dub | 0 |
| streams[1].disposition.original | 0 |
| streams[1].disposition.comment | 0 |
| streams[1].disposition.lyrics | 0 |
| streams[1].disposition.karaoke | 0 |
| streams[1].disposition.forced | 0 |
| streams[1].disposition.hearing_impaired | 0 |
| streams[1].disposition.visual_impaired | 0 |
| streams[1].disposition.clean_effects | 0 |
| streams[1].disposition.attached_pic | 0 |
| streams[1].disposition.timed_thumbnails | 0 |
| streams[1].disposition.non_diegetic | 0 |
| streams[1].disposition.captions | 0 |
| streams[1].disposition.descriptions | 0 |
| streams[1].disposition.metadata | 0 |
| streams[1].disposition.dependent | 0 |
| streams[1].disposition.still_image | 0 |
| streams[1].disposition.multilayer | 0 |
| streams[1].tags.language | jpn |
| streams[1].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[2].index | 2 |
| streams[2].codec_name | png |
| streams[2].codec_long_name | PNG (Portable Network Graphics) image |
| streams[2].codec_type | video |
| streams[2].codec_tag_string | [0][0][0][0] |
| streams[2].codec_tag | 0x0000 |
| streams[2].width | 1280 |
| streams[2].height | 720 |
| streams[2].coded_width | 1280 |
| streams[2].coded_height | 720 |
| streams[2].has_b_frames | 0 |
| streams[2].pix_fmt | rgb24 |
| streams[2].level | -99 |
| streams[2].color_range | pc |
| streams[2].color_space | gbr |
| streams[2].id | 0x0 |
| streams[2].r_frame_rate | 90000/1 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/90000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 15773780 |
| streams[2].duration | 175.264222 |
| streams[2].disposition.default | 0 |
| streams[2].disposition.dub | 0 |
| streams[2].disposition.original | 0 |
| streams[2].disposition.comment | 0 |
| streams[2].disposition.lyrics | 0 |
| streams[2].disposition.karaoke | 0 |
| streams[2].disposition.forced | 0 |
| streams[2].disposition.hearing_impaired | 0 |
| streams[2].disposition.visual_impaired | 0 |
| streams[2].disposition.clean_effects | 0 |
| streams[2].disposition.attached_pic | 1 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| chapters | [] |
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「光景」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 175.264218 |
| format.size | 57565410 |
| format.bit_rate | 2627594 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 4K HDR「光景」 (篠澤広 ソロ SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】 |
| format.tags.artist | 十六夜カズヤP / 16KazuyaP |
| format.tags.genre | Gaming |
| format.tags.date | 20241127 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=9jzNYNVwThU |
| format.tags.description | 「光景」 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm44367089<br>歌：#篠澤広  (CV. 川村玲奈) <br>作詞、作曲、編曲：長谷川白紙<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |
| format.tags.synopsis | 「光景」 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm44367089<br>歌：#篠澤広  (CV. 川村玲奈) <br>作詞、作曲、編曲：長谷川白紙<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 3864576 |
| analyzed_audio_duration_s | 175.264217687075 |
| stft_frames | 7545 |
| flux_transitions | 7544 |
| rms_linear | 0.166806635004425 |
| rms_p10_linear | 0.00523048286970913 |
| rms_p90_linear | 0.253184639606176 |
| rms_p90_p10_db | 33.6979113992567 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 609 |
| centroid_hz_mean | 2077.69079737181 |
| flatness_mean | 0.104590364411937 |
| positive_normalized_flux_mean | 0.0246392657039926 |
| flux_cv | 0.47827554314584 |
| tempo_bpm | 129.19921875 |
| beat_count | 338 |
| beat_interval_count | 337 |
| beat_interval_cv | 0.0412258416347944 |
| local_tempo_count | 7549 |
| local_tempo_cv | 0.218777184039284 |
| chroma_frames | 7549 |
| chroma_entropy_bits_mean | 2.68107795715332 |
| tonnetz_transition_count | 7548 |
| tonnetz_motion_mean | 0.121605091063794 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -14.3 |
| lra_lu | 9.5 |
| true_peak_dbfs | -0.4 |
| silence_seconds | 15.101859 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -14.3 LUFS<br>    Threshold: -24.5 LUFS<br><br>  Loudness range:<br>    LRA:         9.5 LU<br>    Threshold: -34.6 LUFS<br>    LRA low:   -21.1 LUFS<br>    LRA high:  -11.6 LUFS<br><br>  True peak:<br>    Peak:       -0.4 dBFS<br>[out#0/null @ 0000016592bcc580] video:0KiB audio:30192KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:02:55.26 bitrate=N/A speed= 190x elapsed=0:00:00.92 |
| ffmpeg_stderr_sha256 | 7c1c7cc1475e1c1ce1602981caa7ac3f627ed748faa0a3d0050004fd4f84e9dc |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 0 | 0.550771 | 0.550771 | 0.550771 |
| 2.110023 | 9.333152 | 7.223129 | 7.223129 |
| 167.936259 | 175.264218 | 7.32795899999999 | 7.327959 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 36 |
| samples | 36 |
| brightness_mean | 0.246693721144564 |
| saturation_mean | 0.384452009198741 |
| frame_difference_mean | 0.234545046516827 |
| histogram_jumps_gt_0_5 | 24 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | N/A | N/A | N/A |
| 5 | 5 | 0.282767981290817 | 0.431827069716776 | 0.282767981290817 | 0.662056256915402 | 5 |
| 10 | 10 | 0.0403387807309628 | 0.679984204793028 | 0.26473531126976 | 0.680142307509169 | 5 |
| 15 | 15 | 0.083931103348732 | 0.494331699346405 | 0.0740672722458839 | 0.345901530559489 | 5 |
| 20 | 20 | 0.307472229003906 | 0.345571078431373 | 0.233811855316162 | 0.648531423492782 | 5 |
| 25 | 25 | 0.159771531820297 | 0.411991013071895 | 0.202372282743454 | 0.551716638465616 | 5 |
| 30 | 30 | 0.296494543552399 | 0.419602668845316 | 0.189000815153122 | 0.562999509170342 | 5 |
| 35 | 35 | 0.215028613805771 | 0.497262527233115 | 0.179017707705498 | 0.470072641862182 | 5 |
| 40 | 40 | 0.226992383599281 | 0.401497549019608 | 0.178524240851402 | 0.600306590491078 | 5 |
| 45 | 45 | 0.14534804224968 | 0.484839052287582 | 0.215299561619759 | 0.377952148632698 | 5 |
| 50 | 50 | 0.317076832056046 | 0.453821350762527 | 0.24107900261879 | 0.401990548476203 | 5 |
| 55 | 55 | 0.210451811552048 | 0.476347494553377 | 0.207065090537071 | 0.719141435369858 | 5 |
| 60 | 60 | 0.178202882409096 | 0.514438453159041 | 0.205515816807747 | 0.378226670015495 | 5 |
| 65 | 65 | 0.282525062561035 | 0.48401279956427 | 0.1794343739748 | 0.538643377548688 | 5 |
| 70 | 70 | 0.358146488666534 | 0.351168572984749 | 0.185015261173248 | 0.736272847319897 | 5 |
| 75 | 75 | 0.326902270317078 | 0.375006263616558 | 0.164943620562553 | 0.309706655282185 | 5 |
| 80 | 80 | 0.15279059112072 | 0.423458605664488 | 0.222192287445068 | 0.506456296940286 | 5 |
| 85 | 85 | 0.348097264766693 | 0.378170479302832 | 0.244185745716095 | 0.498699141633251 | 5 |
| 90 | 90 | 0.209242656826973 | 0.39912037037037 | 0.211879640817642 | 0.367217554605307 | 5 |
| 95 | 95 | 0.241496190428734 | 0.331342320261438 | 0.177158772945404 | 0.469697642208346 | 5 |
| 100 | 100 | 0.129725500941277 | 0.549838779956427 | 0.186133995652199 | 0.592458862006946 | 5 |
| 105 | 105 | 0.304199904203415 | 0.366692810457516 | 0.275464057922363 | 0.585934031234388 | 5 |
| 110 | 110 | 0.444965183734894 | 0.50246568627451 | 0.24385567009449 | 0.597144719681507 | 5 |
| 115 | 115 | 0.12803541123867 | 0.336196350762527 | 0.352210819721222 | 0.707262892337925 | 5 |
| 120 | 120 | 0.244605675339699 | 0.294809640522876 | 0.170705884695053 | 0.291246028473014 | 5 |
| 125 | 125 | 0.485541373491287 | 0.196127995642702 | 0.300909042358398 | 0.523630859713535 | 5 |
| 130 | 130 | 0.136996179819107 | 0.399821623093682 | 0.368017971515656 | 0.613981621767646 | 5 |
| 135 | 135 | 0.431808292865753 | 0.27695234204793 | 0.303849160671234 | 0.532507417512051 | 5 |
| 140 | 140 | 0.125815913081169 | 0.411733932461874 | 0.322881251573563 | 0.61646257075218 | 5 |
| 145 | 145 | 0.226737484335899 | 0.379418300653595 | 0.165699362754822 | 0.648569764976631 | 5 |
| 150 | 150 | 0.132956713438034 | 0.396147331154684 | 0.127370655536652 | 0.535956241446921 | 5 |
| 155 | 155 | 0.246372297406197 | 0.415179193899782 | 0.179336622357368 | 0.614138264664137 | 5 |
| 160 | 160 | 0.33892947435379 | 0.428419389978213 | 0.133355125784874 | 0.530101164824571 | 5 |
| 165 | 165 | 0.264849960803986 | 0.47273720043573 | 0.100013069808483 | 0.360164692165043 | 5 |
| 170 | 170 | 0 | 0.000138888888888889 | 0.264849960803986 | 0.684178991075424 | 5 |
| 175 | 175 | 0.856357336044312 | 0.0597992919389978 | 0.856357336044312 | 1 | 5 |


## Record 04 — H15: whole_song_reproduction_check

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | fba2c32ac358bca18acc233a4a20d75a920c42523740f2fa638c3d2d0474b4f3 |
| started_utc | 2026-09-10T06:24:46.981287+00:00 |
| completed_utc | 2026-09-10T06:25:14.339202+00:00 |
| source_id | 1JbU-ssxlwCzUGTnq4i2JLO-fw3EaPBxR |
| character | HIRO |
| alias | H15 |
| label | whole_song_reproduction_check |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「コントラスト」 (篠澤広 ソロ2 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| filename | 4K HDR「コントラスト」 (篠澤広 ソロ2 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| size_bytes | 63692806 |
| sha256 | ea62087e203b892295f6bb27f68426779b1d0c37ceb83c522977942e1c7bf2aa |
| start_s | 0 |
| end_s | 200.782948 |
| duration_s | 200.782948 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | ea62087e203b892295f6bb27f68426779b1d0c37ceb83c522977942e1c7bf2aa |
| source_id | 1JbU-ssxlwCzUGTnq4i2JLO-fw3EaPBxR |
| character | HIRO |
| alias | H15 |
| label | whole_song_reproduction_check |
| boundary_note | N/A |
| parameters.method_version | 2026-09-10-v1 |
| parameters.audio_sr_hz | 22050 |
| parameters.nfft | 2048 |
| parameters.hop | 512 |
| parameters.fft_window | periodic Hann |
| parameters.custom_spectral_center | false |
| parameters.rms_percentile_method | linear |
| parameters.rms_floor | 1e-12 |
| parameters.flatness_power_floor | 1e-10 |
| parameters.cv_ddof | 0 |
| parameters.audio_stream | first (0:a:0) |
| parameters.audio_signal | full unseparated mix, mono for features; native channels for R128 |
| parameters.trim_order | decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim |
| parameters.loudness_filter | ebur128=peak=true |
| parameters.silence_filter | silencedetect=noise=-50dB:d=0.5 |
| parameters.start_s | 0 |
| parameters.end_s | N/A |
| parameters.music | true |
| parameters.visual_step_s | 5 |
| parameters.skip_visual | false |
| parameters.visual_size[0] | 160 |
| parameters.visual_size[1] | 90 |
| parameters.visual_resize | INTER_AREA, whole frame with aspect distortion |
| parameters.visual_grayscale | OpenCV BGR2GRAY /255 |
| parameters.visual_saturation | OpenCV HSV S/255 |
| parameters.histogram | 8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5 |
| parameters.ffmpeg_threads | 1 |
| parameters.music_parameters.onset | librosa onset_strength; center=True; aggregate=mean |
| parameters.music_parameters.beat | start_bpm120, tightness100, trim=True |
| parameters.music_parameters.local_tempo | start_bpm120,std_bpm1,ac_size8,max_tempo320,aggregate=None |
| parameters.music_parameters.chroma | chroma_stft,tuning0,norm1,center=True |
| parameters.music_parameters.tonnetz | 6D coordinates from chroma_stft, adjacent Euclidean distance |
| software.python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| software.platform | Windows-11-10.0.26200-SP0 |
| software.numpy | 2.1.2 |
| software.ffmpeg_command | ffmpeg |
| software.ffprobe_command | ffprobe |
| software.ffmpeg_version | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101<br><br>Exiting with exit code 0 |
| software.ffprobe_version | ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101 |
| software.opencv | 4.13.0 |
| software.librosa | 1.0.0 |
| software.scipy | 1.18.0 |
| script_sha256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


### Source probe

| Probe field | Value |
| --- | --- |
| streams[0].index | 0 |
| streams[0].codec_name | h264 |
| streams[0].codec_long_name | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 |
| streams[0].profile | High |
| streams[0].codec_type | video |
| streams[0].codec_tag_string | avc1 |
| streams[0].codec_tag | 0x31637661 |
| streams[0].mime_codec_string | avc1.640020 |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
| streams[0].pix_fmt | yuv420p |
| streams[0].level | 32 |
| streams[0].color_range | tv |
| streams[0].color_space | bt709 |
| streams[0].color_transfer | bt709 |
| streams[0].color_primaries | bt709 |
| streams[0].chroma_location | left |
| streams[0].field_order | progressive |
| streams[0].is_avc | true |
| streams[0].nal_length_size | 4 |
| streams[0].id | 0x1 |
| streams[0].r_frame_rate | 60/1 |
| streams[0].avg_frame_rate | 60/1 |
| streams[0].time_base | 1/15360 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 3083008 |
| streams[0].duration | 200.716667 |
| streams[0].bit_rate | 2375155 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 12043 |
| streams[0].extradata_size | 43 |
| streams[0].disposition.default | 1 |
| streams[0].disposition.dub | 0 |
| streams[0].disposition.original | 0 |
| streams[0].disposition.comment | 0 |
| streams[0].disposition.lyrics | 0 |
| streams[0].disposition.karaoke | 0 |
| streams[0].disposition.forced | 0 |
| streams[0].disposition.hearing_impaired | 0 |
| streams[0].disposition.visual_impaired | 0 |
| streams[0].disposition.clean_effects | 0 |
| streams[0].disposition.attached_pic | 0 |
| streams[0].disposition.timed_thumbnails | 0 |
| streams[0].disposition.non_diegetic | 0 |
| streams[0].disposition.captions | 0 |
| streams[0].disposition.descriptions | 0 |
| streams[0].disposition.metadata | 0 |
| streams[0].disposition.dependent | 0 |
| streams[0].disposition.still_image | 0 |
| streams[0].disposition.multilayer | 0 |
| streams[0].tags.language | und |
| streams[0].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[0].side_data_list[0].side_data_type | Content light level metadata |
| streams[0].side_data_list[0].max_content | 1000 |
| streams[0].side_data_list[0].max_average | 200 |
| streams[1].index | 1 |
| streams[1].codec_name | aac |
| streams[1].codec_long_name | AAC (Advanced Audio Coding) |
| streams[1].profile | LC |
| streams[1].codec_type | audio |
| streams[1].codec_tag_string | mp4a |
| streams[1].codec_tag | 0x6134706d |
| streams[1].mime_codec_string | mp4a.40.2 |
| streams[1].sample_fmt | fltp |
| streams[1].sample_rate | 44100 |
| streams[1].channels | 2 |
| streams[1].channel_layout | stereo |
| streams[1].bits_per_sample | 0 |
| streams[1].initial_padding | 0 |
| streams[1].id | 0x2 |
| streams[1].r_frame_rate | 0/0 |
| streams[1].avg_frame_rate | 0/0 |
| streams[1].time_base | 1/44100 |
| streams[1].start_pts | 0 |
| streams[1].start_time | 0.000000 |
| streams[1].duration_ts | 8854528 |
| streams[1].duration | 200.782948 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 8647 |
| streams[1].extradata_size | 16 |
| streams[1].disposition.default | 1 |
| streams[1].disposition.dub | 0 |
| streams[1].disposition.original | 0 |
| streams[1].disposition.comment | 0 |
| streams[1].disposition.lyrics | 0 |
| streams[1].disposition.karaoke | 0 |
| streams[1].disposition.forced | 0 |
| streams[1].disposition.hearing_impaired | 0 |
| streams[1].disposition.visual_impaired | 0 |
| streams[1].disposition.clean_effects | 0 |
| streams[1].disposition.attached_pic | 0 |
| streams[1].disposition.timed_thumbnails | 0 |
| streams[1].disposition.non_diegetic | 0 |
| streams[1].disposition.captions | 0 |
| streams[1].disposition.descriptions | 0 |
| streams[1].disposition.metadata | 0 |
| streams[1].disposition.dependent | 0 |
| streams[1].disposition.still_image | 0 |
| streams[1].disposition.multilayer | 0 |
| streams[1].tags.language | jpn |
| streams[1].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[2].index | 2 |
| streams[2].codec_name | png |
| streams[2].codec_long_name | PNG (Portable Network Graphics) image |
| streams[2].codec_type | video |
| streams[2].codec_tag_string | [0][0][0][0] |
| streams[2].codec_tag | 0x0000 |
| streams[2].width | 1280 |
| streams[2].height | 720 |
| streams[2].coded_width | 1280 |
| streams[2].coded_height | 720 |
| streams[2].has_b_frames | 0 |
| streams[2].pix_fmt | rgb24 |
| streams[2].level | -99 |
| streams[2].color_range | pc |
| streams[2].color_space | gbr |
| streams[2].id | 0x0 |
| streams[2].r_frame_rate | 90000/1 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/90000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 18070465 |
| streams[2].duration | 200.782944 |
| streams[2].disposition.default | 0 |
| streams[2].disposition.dub | 0 |
| streams[2].disposition.original | 0 |
| streams[2].disposition.comment | 0 |
| streams[2].disposition.lyrics | 0 |
| streams[2].disposition.karaoke | 0 |
| streams[2].disposition.forced | 0 |
| streams[2].disposition.hearing_impaired | 0 |
| streams[2].disposition.visual_impaired | 0 |
| streams[2].disposition.clean_effects | 0 |
| streams[2].disposition.attached_pic | 1 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| chapters | [] |
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「コントラスト」 (篠澤広 ソロ2 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 200.782948 |
| format.size | 63692806 |
| format.bit_rate | 2537777 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 4K HDR「コントラスト」 (篠澤広 ソロ2 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】 |
| format.tags.artist | 十六夜カズヤP / 16KazuyaP |
| format.tags.genre | Gaming |
| format.tags.date | 20240722 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=X7egVXrwKpI |
| format.tags.description | 「コントラスト」 4K #HDR 60fps<br><br>歌：#篠澤広  (CV. 川村玲奈) <br>作詞：佐々木恵梨 <br>作曲：佐々木恵梨、鵜飼大幹、中村ヒロ <br>編曲：中村ヒロ<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |
| format.tags.synopsis | 「コントラスト」 4K #HDR 60fps<br><br>歌：#篠澤広  (CV. 川村玲奈) <br>作詞：佐々木恵梨 <br>作曲：佐々木恵梨、鵜飼大幹、中村ヒロ <br>編曲：中村ヒロ<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 4427264 |
| analyzed_audio_duration_s | 200.782947845805 |
| stft_frames | 8644 |
| flux_transitions | 8643 |
| rms_linear | 0.204398925827346 |
| rms_p10_linear | 0.0101138549481276 |
| rms_p90_linear | 0.324461091912978 |
| rms_p90_p10_db | 30.124918093061 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 325 |
| centroid_hz_mean | 2085.16715298758 |
| flatness_mean | 0.0596543685508358 |
| positive_normalized_flux_mean | 0.0277538344477684 |
| flux_cv | 0.492392700726006 |
| tempo_bpm | 117.453835227273 |
| beat_count | 344 |
| beat_interval_count | 343 |
| beat_interval_cv | 0.0420315967416625 |
| local_tempo_count | 8648 |
| local_tempo_cv | 0.147949412601213 |
| chroma_frames | 8648 |
| chroma_entropy_bits_mean | 3.02042269706726 |
| tonnetz_transition_count | 8647 |
| tonnetz_motion_mean | 0.126025858031729 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -12.9 |
| lra_lu | 13.9 |
| true_peak_dbfs | 0.2 |
| silence_seconds | 8.63510300000002 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -12.9 LUFS<br>    Threshold: -23.8 LUFS<br><br>  Loudness range:<br>    LRA:        13.9 LU<br>    Threshold: -33.8 LUFS<br>    LRA low:   -24.5 LUFS<br>    LRA high:  -10.6 LUFS<br><br>  True peak:<br>    Peak:        0.2 dBFS<br>[out#0/null @ 00000187ca5d0c80] video:0KiB audio:34588KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:03:20.78 bitrate=N/A speed= 200x elapsed=0:00:01.00 |
| ffmpeg_stderr_sha256 | 01ef92d54e57bc3f23f08a1b6633cf5410a5e1e28690c5d78126b86e37e97134 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 0 | 0.512585 | 0.512585 | 0.512585 |
| 2.070045 | 4.756939 | 2.686894 | 2.686893 |
| 195.347324 | 200.782948 | 5.43562400000002 | 5.435624 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 41 |
| samples | 41 |
| brightness_mean | 0.154454547366718 |
| saturation_mean | 0.430133362559116 |
| frame_difference_mean | 0.147859859094024 |
| histogram_jumps_gt_0_5 | 11 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.0572290346026421 | 0.407074618736383 | N/A | N/A | N/A |
| 5 | 5 | 0.0411535985767841 | 0.597863562091503 | 0.0721037611365318 | 0.463188591221365 | 5 |
| 10 | 10 | 0.0988436862826347 | 0.431824074074074 | 0.0802162364125252 | 0.369206638510942 | 5 |
| 15 | 15 | 0.110103487968445 | 0.311781862745098 | 0.0924150422215462 | 0.215278418449574 | 5 |
| 20 | 20 | 0.145625278353691 | 0.336304738562091 | 0.105612196028233 | 0.218824453599803 | 5 |
| 25 | 25 | 0.140564277768135 | 0.357308551198257 | 0.14556972682476 | 0.133443165430695 | 5 |
| 30 | 30 | 0.129689827561378 | 0.309841775599129 | 0.12265769392252 | 0.217036368029703 | 5 |
| 35 | 35 | 0.140131548047066 | 0.461942538126362 | 0.111214600503445 | 0.456324210520421 | 5 |
| 40 | 40 | 0.198189541697502 | 0.491602668845316 | 0.137567818164825 | 0.320763305794245 | 5 |
| 45 | 45 | 0.0707946717739105 | 0.557641339869281 | 0.152606204152107 | 0.673744726782274 | 5 |
| 50 | 50 | 0.172872826457024 | 0.446443355119826 | 0.126442551612854 | 0.377674410044426 | 5 |
| 55 | 55 | 0.204251646995544 | 0.475915849673203 | 0.176075980067253 | 0.420904238153053 | 5 |
| 60 | 60 | 0.0934166610240936 | 0.519479847494553 | 0.162575721740723 | 0.397339396257249 | 5 |
| 65 | 65 | 0.123912587761879 | 0.592328159041394 | 0.0954093188047409 | 0.396010271445423 | 5 |
| 70 | 70 | 0.0933232605457306 | 0.547574346405229 | 0.123990751802921 | 0.47340977593017 | 5 |
| 75 | 75 | 0.167253285646439 | 0.538505446623094 | 0.120463237166405 | 0.412401017406351 | 5 |
| 80 | 80 | 0.487805038690567 | 0.32103894335512 | 0.328529417514801 | 0.803907084893325 | 5 |
| 85 | 85 | 0.220451802015305 | 0.376563453159041 | 0.288978517055511 | 0.709881230415539 | 5 |
| 90 | 90 | 0.366514176130295 | 0.304979030501089 | 0.229693084955215 | 0.363901013972746 | 5 |
| 95 | 95 | 0.17253677546978 | 0.464363834422658 | 0.229462698101997 | 0.485747488915838 | 5 |
| 100 | 100 | 0.222283497452736 | 0.492914488017429 | 0.121793046593666 | 0.490005422823552 | 5 |
| 105 | 105 | 0.218924298882484 | 0.383852941176471 | 0.181601598858833 | 0.736711995435403 | 5 |
| 110 | 110 | 0.130909323692322 | 0.520398965141612 | 0.166327610611916 | 0.345011763877678 | 5 |
| 115 | 115 | 0.0912385731935501 | 0.541433006535948 | 0.103404425084591 | 0.263359206678701 | 5 |
| 120 | 120 | 0.370905756950378 | 0.291116557734205 | 0.293286502361298 | 0.703735707886488 | 5 |
| 125 | 125 | 0.156486377120018 | 0.285514705882353 | 0.249217867851257 | 0.486278913647548 | 5 |
| 130 | 130 | 0.216282680630684 | 0.374741830065359 | 0.15431372821331 | 0.503401621738095 | 5 |
| 135 | 135 | 0.0666345357894897 | 0.563721132897604 | 0.175372555851936 | 0.712070549272307 | 5 |
| 140 | 140 | 0.14078514277935 | 0.49819417211329 | 0.0929354652762413 | 0.386594020918825 | 5 |
| 145 | 145 | 0.232901692390442 | 0.393206154684096 | 0.168133437633514 | 0.637083777544954 | 5 |
| 150 | 150 | 0.165723040699959 | 0.4279098583878 | 0.135011434555054 | 0.397093656821644 | 5 |
| 155 | 155 | 0.210884556174278 | 0.417786764705882 | 0.146134808659554 | 0.398197558373374 | 5 |
| 160 | 160 | 0.182558834552765 | 0.448432461873638 | 0.142072454094887 | 0.72758967590676 | 5 |
| 165 | 165 | 0.149433001875877 | 0.393203703703704 | 0.1396514326334 | 0.572528163869948 | 5 |
| 170 | 170 | 0.0412178635597229 | 0.643042483660131 | 0.125625818967819 | 0.522341594375849 | 5 |
| 175 | 175 | 0.115794129669666 | 0.33664188453159 | 0.0994564294815063 | 0.38808285672223 | 5 |
| 180 | 180 | 0.13802070915699 | 0.295579793028322 | 0.145673766732216 | 0.104126004376415 | 5 |
| 185 | 185 | 0.0795324221253395 | 0.420360021786492 | 0.134842872619629 | 0.202249256798286 | 5 |
| 190 | 190 | 0.102218419313431 | 0.514851034858388 | 0.101892985403538 | 0.28246937021771 | 5 |
| 195 | 195 | 0.0652385726571083 | 0.542187908496732 | 0.0708229914307594 | 0.245069135162619 | 5 |
| 200 | 200 | 0 | 0 | 0.0652385726571083 | 0.449878568259184 | 5 |


## Record 05 — H17: whole_song_reproduction_check

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 3a858b0397373f05eba200aaf6ec33a3930a54d0b3ccba05a390c62694a719fc |
| started_utc | 2026-09-10T06:25:14.390974+00:00 |
| completed_utc | 2026-09-10T06:25:27.835576+00:00 |
| source_id | 11Sf_pH-3JhiLcAUT4xLkm8rbzYL84f8E |
| character | HIRO |
| alias | H17 |
| label | whole_song_reproduction_check |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「サンフェーデッド」 (篠澤広 ソロ3 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| filename | 4K HDR「サンフェーデッド」 (篠澤広 ソロ3 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| size_bytes | 67395136 |
| sha256 | be3709652b63a93a30bba202dc06296169262af269b84b77109335d65e5bd8cd |
| start_s | 0 |
| end_s | 183.275102 |
| duration_s | 183.275102 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | be3709652b63a93a30bba202dc06296169262af269b84b77109335d65e5bd8cd |
| source_id | 11Sf_pH-3JhiLcAUT4xLkm8rbzYL84f8E |
| character | HIRO |
| alias | H17 |
| label | whole_song_reproduction_check |
| boundary_note | N/A |
| parameters.method_version | 2026-09-10-v1 |
| parameters.audio_sr_hz | 22050 |
| parameters.nfft | 2048 |
| parameters.hop | 512 |
| parameters.fft_window | periodic Hann |
| parameters.custom_spectral_center | false |
| parameters.rms_percentile_method | linear |
| parameters.rms_floor | 1e-12 |
| parameters.flatness_power_floor | 1e-10 |
| parameters.cv_ddof | 0 |
| parameters.audio_stream | first (0:a:0) |
| parameters.audio_signal | full unseparated mix, mono for features; native channels for R128 |
| parameters.trim_order | decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim |
| parameters.loudness_filter | ebur128=peak=true |
| parameters.silence_filter | silencedetect=noise=-50dB:d=0.5 |
| parameters.start_s | 0 |
| parameters.end_s | N/A |
| parameters.music | true |
| parameters.visual_step_s | 5 |
| parameters.skip_visual | false |
| parameters.visual_size[0] | 160 |
| parameters.visual_size[1] | 90 |
| parameters.visual_resize | INTER_AREA, whole frame with aspect distortion |
| parameters.visual_grayscale | OpenCV BGR2GRAY /255 |
| parameters.visual_saturation | OpenCV HSV S/255 |
| parameters.histogram | 8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5 |
| parameters.ffmpeg_threads | 1 |
| parameters.music_parameters.onset | librosa onset_strength; center=True; aggregate=mean |
| parameters.music_parameters.beat | start_bpm120, tightness100, trim=True |
| parameters.music_parameters.local_tempo | start_bpm120,std_bpm1,ac_size8,max_tempo320,aggregate=None |
| parameters.music_parameters.chroma | chroma_stft,tuning0,norm1,center=True |
| parameters.music_parameters.tonnetz | 6D coordinates from chroma_stft, adjacent Euclidean distance |
| software.python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| software.platform | Windows-11-10.0.26200-SP0 |
| software.numpy | 2.1.2 |
| software.ffmpeg_command | ffmpeg |
| software.ffprobe_command | ffprobe |
| software.ffmpeg_version | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101<br><br>Exiting with exit code 0 |
| software.ffprobe_version | ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101 |
| software.opencv | 4.13.0 |
| software.librosa | 1.0.0 |
| software.scipy | 1.18.0 |
| script_sha256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


### Source probe

| Probe field | Value |
| --- | --- |
| streams[0].index | 0 |
| streams[0].codec_name | h264 |
| streams[0].codec_long_name | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 |
| streams[0].profile | Main |
| streams[0].codec_type | video |
| streams[0].codec_tag_string | avc1 |
| streams[0].codec_tag | 0x31637661 |
| streams[0].mime_codec_string | avc1.4d4020 |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
| streams[0].pix_fmt | yuv420p |
| streams[0].level | 32 |
| streams[0].color_range | tv |
| streams[0].color_space | bt709 |
| streams[0].color_transfer | bt709 |
| streams[0].color_primaries | bt709 |
| streams[0].chroma_location | left |
| streams[0].field_order | progressive |
| streams[0].is_avc | true |
| streams[0].nal_length_size | 4 |
| streams[0].id | 0x1 |
| streams[0].r_frame_rate | 60/1 |
| streams[0].avg_frame_rate | 60/1 |
| streams[0].time_base | 1/15360 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 2814208 |
| streams[0].duration | 183.216667 |
| streams[0].bit_rate | 2768838 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 10993 |
| streams[0].extradata_size | 43 |
| streams[0].disposition.default | 1 |
| streams[0].disposition.dub | 0 |
| streams[0].disposition.original | 0 |
| streams[0].disposition.comment | 0 |
| streams[0].disposition.lyrics | 0 |
| streams[0].disposition.karaoke | 0 |
| streams[0].disposition.forced | 0 |
| streams[0].disposition.hearing_impaired | 0 |
| streams[0].disposition.visual_impaired | 0 |
| streams[0].disposition.clean_effects | 0 |
| streams[0].disposition.attached_pic | 0 |
| streams[0].disposition.timed_thumbnails | 0 |
| streams[0].disposition.non_diegetic | 0 |
| streams[0].disposition.captions | 0 |
| streams[0].disposition.descriptions | 0 |
| streams[0].disposition.metadata | 0 |
| streams[0].disposition.dependent | 0 |
| streams[0].disposition.still_image | 0 |
| streams[0].disposition.multilayer | 0 |
| streams[0].tags.language | und |
| streams[0].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[0].side_data_list[0].side_data_type | Content light level metadata |
| streams[0].side_data_list[0].max_content | 1000 |
| streams[0].side_data_list[0].max_average | 200 |
| streams[1].index | 1 |
| streams[1].codec_name | aac |
| streams[1].codec_long_name | AAC (Advanced Audio Coding) |
| streams[1].profile | LC |
| streams[1].codec_type | audio |
| streams[1].codec_tag_string | mp4a |
| streams[1].codec_tag | 0x6134706d |
| streams[1].mime_codec_string | mp4a.40.2 |
| streams[1].sample_fmt | fltp |
| streams[1].sample_rate | 44100 |
| streams[1].channels | 2 |
| streams[1].channel_layout | stereo |
| streams[1].bits_per_sample | 0 |
| streams[1].initial_padding | 0 |
| streams[1].id | 0x2 |
| streams[1].r_frame_rate | 0/0 |
| streams[1].avg_frame_rate | 0/0 |
| streams[1].time_base | 1/44100 |
| streams[1].start_pts | 0 |
| streams[1].start_time | 0.000000 |
| streams[1].duration_ts | 8082432 |
| streams[1].duration | 183.275102 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 7893 |
| streams[1].extradata_size | 16 |
| streams[1].disposition.default | 1 |
| streams[1].disposition.dub | 0 |
| streams[1].disposition.original | 0 |
| streams[1].disposition.comment | 0 |
| streams[1].disposition.lyrics | 0 |
| streams[1].disposition.karaoke | 0 |
| streams[1].disposition.forced | 0 |
| streams[1].disposition.hearing_impaired | 0 |
| streams[1].disposition.visual_impaired | 0 |
| streams[1].disposition.clean_effects | 0 |
| streams[1].disposition.attached_pic | 0 |
| streams[1].disposition.timed_thumbnails | 0 |
| streams[1].disposition.non_diegetic | 0 |
| streams[1].disposition.captions | 0 |
| streams[1].disposition.descriptions | 0 |
| streams[1].disposition.metadata | 0 |
| streams[1].disposition.dependent | 0 |
| streams[1].disposition.still_image | 0 |
| streams[1].disposition.multilayer | 0 |
| streams[1].tags.language | eng |
| streams[1].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[2].index | 2 |
| streams[2].codec_name | png |
| streams[2].codec_long_name | PNG (Portable Network Graphics) image |
| streams[2].codec_type | video |
| streams[2].codec_tag_string | [0][0][0][0] |
| streams[2].codec_tag | 0x0000 |
| streams[2].width | 1280 |
| streams[2].height | 720 |
| streams[2].coded_width | 1280 |
| streams[2].coded_height | 720 |
| streams[2].has_b_frames | 0 |
| streams[2].pix_fmt | rgb24 |
| streams[2].level | -99 |
| streams[2].color_range | pc |
| streams[2].color_space | gbr |
| streams[2].id | 0x0 |
| streams[2].r_frame_rate | 90000/1 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/90000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 16494759 |
| streams[2].duration | 183.275100 |
| streams[2].disposition.default | 0 |
| streams[2].disposition.dub | 0 |
| streams[2].disposition.original | 0 |
| streams[2].disposition.comment | 0 |
| streams[2].disposition.lyrics | 0 |
| streams[2].disposition.karaoke | 0 |
| streams[2].disposition.forced | 0 |
| streams[2].disposition.hearing_impaired | 0 |
| streams[2].disposition.visual_impaired | 0 |
| streams[2].disposition.clean_effects | 0 |
| streams[2].disposition.attached_pic | 1 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| chapters | [] |
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「サンフェーデッド」 (篠澤広 ソロ3 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 183.275102 |
| format.size | 67395136 |
| format.bit_rate | 2941813 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 4K HDR「サンフェーデッド」 (篠澤広 ソロ3 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】 |
| format.tags.artist | 十六夜カズヤP / 16KazuyaP |
| format.tags.genre | Gaming |
| format.tags.date | 20250717 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=tRqueI07-nI |
| format.tags.description | 「サンフェーデッド」 (#篠澤広  ソロ3 SSR) 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm45195427<br>作詞・作曲・編曲：長谷川白紙<br>歌：篠澤広 (CV. 川村玲奈)<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |
| format.tags.synopsis | 「サンフェーデッド」 (#篠澤広  ソロ3 SSR) 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm45195427<br>作詞・作曲・編曲：長谷川白紙<br>歌：篠澤広 (CV. 川村玲奈)<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 4041216 |
| analyzed_audio_duration_s | 183.275102040816 |
| stft_frames | 7890 |
| flux_transitions | 7889 |
| rms_linear | 0.222911675471625 |
| rms_p10_linear | 0.117825980903924 |
| rms_p90_linear | 0.279774682385654 |
| rms_p90_p10_db | 7.51134694842469 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 340 |
| centroid_hz_mean | 2379.63773127389 |
| flatness_mean | 0.0802514015049359 |
| positive_normalized_flux_mean | 0.0216711307815188 |
| flux_cv | 0.352550955529503 |
| tempo_bpm | 135.999177631579 |
| beat_count | 369 |
| beat_interval_count | 368 |
| beat_interval_cv | 0.0491526368760324 |
| local_tempo_count | 7894 |
| local_tempo_cv | 0.135883136043225 |
| chroma_frames | 7894 |
| chroma_entropy_bits_mean | 3.10597395896912 |
| tonnetz_transition_count | 7893 |
| tonnetz_motion_mean | 0.112915828116102 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -12.2 |
| lra_lu | 3.2 |
| true_peak_dbfs | -0.1 |
| silence_seconds | 9.10251800000001 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -12.2 LUFS<br>    Threshold: -22.3 LUFS<br><br>  Loudness range:<br>    LRA:         3.2 LU<br>    Threshold: -32.3 LUFS<br>    LRA low:   -14.4 LUFS<br>    LRA high:  -11.2 LUFS<br><br>  True peak:<br>    Peak:       -0.1 dBFS<br>[out#0/null @ 00000193a517be40] video:0KiB audio:31572KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:03:03.27 bitrate=N/A speed=86.6x elapsed=0:00:02.11 |
| ffmpeg_stderr_sha256 | 2de35cf8b206a0284fd3cf25c355a732a9006e481d50b60511c7e1a97b0e8d72 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 0 | 0.581066 | 0.581066 | 0.581066 |
| 2.114966 | 4.801429 | 2.686463 | 2.686463 |
| 177.440113 | 183.275102 | 5.83498900000001 | 5.834989 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 37 |
| samples | 37 |
| brightness_mean | 0.338472130934934 |
| saturation_mean | 0.346821181475593 |
| frame_difference_mean | 0.216328020104104 |
| histogram_jumps_gt_0_5 | 20 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.13639298081398 | 0.467807461873638 | N/A | N/A | N/A |
| 5 | 5 | 0.121756814420223 | 0.449644880174292 | 0.223946630954742 | 0.483215559308498 | 5 |
| 10 | 10 | 0.225383728742599 | 0.528411492374728 | 0.212247282266617 | 0.558051215493469 | 5 |
| 15 | 15 | 0.336441993713379 | 0.268352396514161 | 0.234117671847343 | 0.754943483421578 | 5 |
| 20 | 20 | 0.393982857465744 | 0.306580882352941 | 0.21273584663868 | 0.474483792373103 | 5 |
| 25 | 25 | 0.406724721193314 | 0.350119008714597 | 0.149854570627213 | 0.590327503899919 | 5 |
| 30 | 30 | 0.348053127527237 | 0.316764978213508 | 0.216478750109673 | 0.695207135231942 | 5 |
| 35 | 35 | 0.322207272052765 | 0.354493736383442 | 0.183782681822777 | 0.597972560716838 | 5 |
| 40 | 40 | 0.286191463470459 | 0.344337145969499 | 0.108697712421417 | 0.226500620425425 | 5 |
| 45 | 45 | 0.409199625253677 | 0.289441448801743 | 0.168497279286385 | 0.338153912125543 | 5 |
| 50 | 50 | 0.253353506326675 | 0.39746568627451 | 0.236637532711029 | 0.672424425782316 | 5 |
| 55 | 55 | 0.221499741077423 | 0.401984477124183 | 0.134354844689369 | 0.30302696959006 | 5 |
| 60 | 60 | 0.284749209880829 | 0.464302287581699 | 0.124918848276138 | 0.445769169320371 | 5 |
| 65 | 65 | 0.248647049069405 | 0.345662037037037 | 0.136390805244446 | 0.369863323386037 | 5 |
| 70 | 70 | 0.320861905813217 | 0.450208333333333 | 0.197172924876213 | 0.447747614673913 | 5 |
| 75 | 75 | 0.440538674592972 | 0.215735566448802 | 0.176893517374992 | 0.767195769558792 | 5 |
| 80 | 80 | 0.31088399887085 | 0.255727124183007 | 0.190538123250008 | 0.456258007679948 | 5 |
| 85 | 85 | 0.257853209972382 | 0.304124727668845 | 0.154105395078659 | 0.277893923943594 | 5 |
| 90 | 90 | 0.391440659761429 | 0.295654684095861 | 0.204029157757759 | 0.378738278523696 | 5 |
| 95 | 95 | 0.348707288503647 | 0.347525871459695 | 0.165598854422569 | 0.261939225818444 | 5 |
| 100 | 100 | 0.452052295207977 | 0.322433006535948 | 0.231493726372719 | 0.482533255356385 | 5 |
| 105 | 105 | 0.379044383764267 | 0.292582516339869 | 0.148874446749687 | 0.421003921307587 | 5 |
| 110 | 110 | 0.271593153476715 | 0.422391067538126 | 0.183232858777046 | 0.741046402184543 | 5 |
| 115 | 115 | 0.352268010377884 | 0.48633660130719 | 0.138038128614426 | 0.627332703982267 | 5 |
| 120 | 120 | 0.0622222274541855 | 0.480744825708061 | 0.313907414674759 | 0.680827030935113 | 5 |
| 125 | 125 | 0.620260953903198 | 0.282061546840959 | 0.558459758758545 | 0.635085328915951 | 5 |
| 130 | 130 | 0.269514173269272 | 0.419972222222222 | 0.361281603574753 | 0.630825679562826 | 5 |
| 135 | 135 | 0.313623666763306 | 0.414782135076253 | 0.231868207454681 | 0.706259784207142 | 5 |
| 140 | 140 | 0.488300383090973 | 0.374988289760349 | 0.252644628286362 | 0.730621030778397 | 5 |
| 145 | 145 | 0.586534261703491 | 0.153741830065359 | 0.198922395706177 | 0.6111557924718 | 5 |
| 150 | 150 | 0.261230945587158 | 0.384425653594771 | 0.364123642444611 | 0.632947214956808 | 5 |
| 155 | 155 | 0.28805747628212 | 0.498956427015251 | 0.146769881248474 | 0.635069663935123 | 5 |
| 160 | 160 | 0.507050395011902 | 0.279975490196078 | 0.279318630695343 | 0.843160734999897 | 5 |
| 165 | 165 | 0.555238306522369 | 0.264273148148148 | 0.201021239161491 | 0.603478858710033 | 5 |
| 170 | 170 | 0.521194458007812 | 0.304134531590414 | 0.125591769814491 | 0.321805535105209 | 5 |
| 175 | 175 | 0.530413925647736 | 0.296240196078431 | 0.0908480361104012 | 0.214462231159944 | 5 |
| 180 | 180 | 0 | 0 | 0.530413925647736 | 0.708433858759485 | 5 |


## Record 06 — H19: whole_song_reproduction_check

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 9f580bfb429f79383da074929385c29510035c2768a5c79f6a787922f5d7db65 |
| started_utc | 2026-09-10T06:25:15.082808+00:00 |
| completed_utc | 2026-09-10T06:25:29.534365+00:00 |
| source_id | 1NZfazcL67wDoVoFa5nuQp-y3E2-Edzmd |
| character | HIRO |
| alias | H19 |
| label | whole_song_reproduction_check |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「Campus mode!!」(篠澤広 フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| filename | 4K HDR「Campus mode!!」(篠澤広 フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| size_bytes | 63464478 |
| sha256 | a692b45cc3ee31ff957c0199bae17c1c2f143c2271f3c1e19abf4d77a8e634ef |
| start_s | 0 |
| end_s | 160.728526 |
| duration_s | 160.728526 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | a692b45cc3ee31ff957c0199bae17c1c2f143c2271f3c1e19abf4d77a8e634ef |
| source_id | 1NZfazcL67wDoVoFa5nuQp-y3E2-Edzmd |
| character | HIRO |
| alias | H19 |
| label | whole_song_reproduction_check |
| boundary_note | N/A |
| parameters.method_version | 2026-09-10-v1 |
| parameters.audio_sr_hz | 22050 |
| parameters.nfft | 2048 |
| parameters.hop | 512 |
| parameters.fft_window | periodic Hann |
| parameters.custom_spectral_center | false |
| parameters.rms_percentile_method | linear |
| parameters.rms_floor | 1e-12 |
| parameters.flatness_power_floor | 1e-10 |
| parameters.cv_ddof | 0 |
| parameters.audio_stream | first (0:a:0) |
| parameters.audio_signal | full unseparated mix, mono for features; native channels for R128 |
| parameters.trim_order | decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim |
| parameters.loudness_filter | ebur128=peak=true |
| parameters.silence_filter | silencedetect=noise=-50dB:d=0.5 |
| parameters.start_s | 0 |
| parameters.end_s | N/A |
| parameters.music | true |
| parameters.visual_step_s | 5 |
| parameters.skip_visual | false |
| parameters.visual_size[0] | 160 |
| parameters.visual_size[1] | 90 |
| parameters.visual_resize | INTER_AREA, whole frame with aspect distortion |
| parameters.visual_grayscale | OpenCV BGR2GRAY /255 |
| parameters.visual_saturation | OpenCV HSV S/255 |
| parameters.histogram | 8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5 |
| parameters.ffmpeg_threads | 1 |
| parameters.music_parameters.onset | librosa onset_strength; center=True; aggregate=mean |
| parameters.music_parameters.beat | start_bpm120, tightness100, trim=True |
| parameters.music_parameters.local_tempo | start_bpm120,std_bpm1,ac_size8,max_tempo320,aggregate=None |
| parameters.music_parameters.chroma | chroma_stft,tuning0,norm1,center=True |
| parameters.music_parameters.tonnetz | 6D coordinates from chroma_stft, adjacent Euclidean distance |
| software.python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| software.platform | Windows-11-10.0.26200-SP0 |
| software.numpy | 2.1.2 |
| software.ffmpeg_command | ffmpeg |
| software.ffprobe_command | ffprobe |
| software.ffmpeg_version | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101<br><br>Exiting with exit code 0 |
| software.ffprobe_version | ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101 |
| software.opencv | 4.13.0 |
| software.librosa | 1.0.0 |
| software.scipy | 1.18.0 |
| script_sha256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


### Source probe

| Probe field | Value |
| --- | --- |
| streams[0].index | 0 |
| streams[0].codec_name | h264 |
| streams[0].codec_long_name | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 |
| streams[0].profile | High |
| streams[0].codec_type | video |
| streams[0].codec_tag_string | avc1 |
| streams[0].codec_tag | 0x31637661 |
| streams[0].mime_codec_string | avc1.640020 |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
| streams[0].pix_fmt | yuv420p |
| streams[0].level | 32 |
| streams[0].color_range | tv |
| streams[0].color_space | bt709 |
| streams[0].color_transfer | bt709 |
| streams[0].color_primaries | bt709 |
| streams[0].chroma_location | left |
| streams[0].field_order | progressive |
| streams[0].is_avc | true |
| streams[0].nal_length_size | 4 |
| streams[0].id | 0x1 |
| streams[0].r_frame_rate | 60/1 |
| streams[0].avg_frame_rate | 60/1 |
| streams[0].time_base | 1/15360 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 2467584 |
| streams[0].duration | 160.650000 |
| streams[0].bit_rate | 2973259 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 9639 |
| streams[0].extradata_size | 43 |
| streams[0].disposition.default | 1 |
| streams[0].disposition.dub | 0 |
| streams[0].disposition.original | 0 |
| streams[0].disposition.comment | 0 |
| streams[0].disposition.lyrics | 0 |
| streams[0].disposition.karaoke | 0 |
| streams[0].disposition.forced | 0 |
| streams[0].disposition.hearing_impaired | 0 |
| streams[0].disposition.visual_impaired | 0 |
| streams[0].disposition.clean_effects | 0 |
| streams[0].disposition.attached_pic | 0 |
| streams[0].disposition.timed_thumbnails | 0 |
| streams[0].disposition.non_diegetic | 0 |
| streams[0].disposition.captions | 0 |
| streams[0].disposition.descriptions | 0 |
| streams[0].disposition.metadata | 0 |
| streams[0].disposition.dependent | 0 |
| streams[0].disposition.still_image | 0 |
| streams[0].disposition.multilayer | 0 |
| streams[0].tags.language | und |
| streams[0].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[0].side_data_list[0].side_data_type | Content light level metadata |
| streams[0].side_data_list[0].max_content | 1000 |
| streams[0].side_data_list[0].max_average | 200 |
| streams[1].index | 1 |
| streams[1].codec_name | aac |
| streams[1].codec_long_name | AAC (Advanced Audio Coding) |
| streams[1].profile | LC |
| streams[1].codec_type | audio |
| streams[1].codec_tag_string | mp4a |
| streams[1].codec_tag | 0x6134706d |
| streams[1].mime_codec_string | mp4a.40.2 |
| streams[1].sample_fmt | fltp |
| streams[1].sample_rate | 44100 |
| streams[1].channels | 2 |
| streams[1].channel_layout | stereo |
| streams[1].bits_per_sample | 0 |
| streams[1].initial_padding | 0 |
| streams[1].id | 0x2 |
| streams[1].r_frame_rate | 0/0 |
| streams[1].avg_frame_rate | 0/0 |
| streams[1].time_base | 1/44100 |
| streams[1].start_pts | 0 |
| streams[1].start_time | 0.000000 |
| streams[1].duration_ts | 7088128 |
| streams[1].duration | 160.728526 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 6922 |
| streams[1].extradata_size | 16 |
| streams[1].disposition.default | 1 |
| streams[1].disposition.dub | 0 |
| streams[1].disposition.original | 0 |
| streams[1].disposition.comment | 0 |
| streams[1].disposition.lyrics | 0 |
| streams[1].disposition.karaoke | 0 |
| streams[1].disposition.forced | 0 |
| streams[1].disposition.hearing_impaired | 0 |
| streams[1].disposition.visual_impaired | 0 |
| streams[1].disposition.clean_effects | 0 |
| streams[1].disposition.attached_pic | 0 |
| streams[1].disposition.timed_thumbnails | 0 |
| streams[1].disposition.non_diegetic | 0 |
| streams[1].disposition.captions | 0 |
| streams[1].disposition.descriptions | 0 |
| streams[1].disposition.metadata | 0 |
| streams[1].disposition.dependent | 0 |
| streams[1].disposition.still_image | 0 |
| streams[1].disposition.multilayer | 0 |
| streams[1].tags.language | jpn |
| streams[1].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[2].index | 2 |
| streams[2].codec_name | png |
| streams[2].codec_long_name | PNG (Portable Network Graphics) image |
| streams[2].codec_type | video |
| streams[2].codec_tag_string | [0][0][0][0] |
| streams[2].codec_tag | 0x0000 |
| streams[2].width | 1280 |
| streams[2].height | 720 |
| streams[2].coded_width | 1280 |
| streams[2].coded_height | 720 |
| streams[2].has_b_frames | 0 |
| streams[2].pix_fmt | rgb24 |
| streams[2].level | -99 |
| streams[2].color_range | pc |
| streams[2].color_space | gbr |
| streams[2].id | 0x0 |
| streams[2].r_frame_rate | 90000/1 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/90000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 14465567 |
| streams[2].duration | 160.728522 |
| streams[2].disposition.default | 0 |
| streams[2].disposition.dub | 0 |
| streams[2].disposition.original | 0 |
| streams[2].disposition.comment | 0 |
| streams[2].disposition.lyrics | 0 |
| streams[2].disposition.karaoke | 0 |
| streams[2].disposition.forced | 0 |
| streams[2].disposition.hearing_impaired | 0 |
| streams[2].disposition.visual_impaired | 0 |
| streams[2].disposition.clean_effects | 0 |
| streams[2].disposition.attached_pic | 1 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| chapters | [] |
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「Campus mode!!」(篠澤広 フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 160.728526 |
| format.size | 63464478 |
| format.bit_rate | 3158840 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 4K HDR「Campus mode!!」(篠澤広 フェスSSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】 |
| format.tags.artist | 十六夜カズヤP / 16KazuyaP |
| format.tags.genre | Gaming |
| format.tags.date | 20250111 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=1EJOn0vf-Fo |
| format.tags.description | 「Campus mode!!」(#篠澤広  フェスSSR) 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm44527247<br>歌：篠澤広 (CV. 川村玲奈)<br>作詞・作曲：田淵智也<br>編曲：滝澤俊輔（TRYTONELABO）<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |
| format.tags.synopsis | 「Campus mode!!」(#篠澤広  フェスSSR) 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm44527247<br>歌：篠澤広 (CV. 川村玲奈)<br>作詞・作曲：田淵智也<br>編曲：滝澤俊輔（TRYTONELABO）<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 3544064 |
| analyzed_audio_duration_s | 160.728526077098 |
| stft_frames | 6919 |
| flux_transitions | 6918 |
| rms_linear | 0.191301480049956 |
| rms_p10_linear | 0.0697707644367925 |
| rms_p90_linear | 0.246002253717671 |
| rms_p90_p10_db | 10.9453120908471 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 399 |
| centroid_hz_mean | 2655.47495901444 |
| flatness_mean | 0.112384329087346 |
| positive_normalized_flux_mean | 0.0232079849946001 |
| flux_cv | 0.375024324509489 |
| tempo_bpm | 123.046875 |
| beat_count | 304 |
| beat_interval_count | 303 |
| beat_interval_cv | 0.0516120629189752 |
| local_tempo_count | 6923 |
| local_tempo_cv | 0.164607768207651 |
| chroma_frames | 6923 |
| chroma_entropy_bits_mean | 2.89765429496765 |
| tonnetz_transition_count | 6922 |
| tonnetz_motion_mean | 0.165536707064631 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -12.4 |
| lra_lu | 3 |
| true_peak_dbfs | -0 |
| silence_seconds | 10.201111 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -12.4 LUFS<br>    Threshold: -22.6 LUFS<br><br>  Loudness range:<br>    LRA:         3.0 LU<br>    Threshold: -32.6 LUFS<br>    LRA low:   -14.1 LUFS<br>    LRA high:  -11.1 LUFS<br><br>  True peak:<br>    Peak:       -0.0 dBFS<br>[out#0/null @ 0000018b57009780] video:0KiB audio:27688KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:02:40.72 bitrate=N/A speed=89.2x elapsed=0:00:01.80 |
| ffmpeg_stderr_sha256 | b675a0bf75bc713cf59d5a5053f41a6e80db58223ad0a3b4d653aeb727b96ab4 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 0 | 0.54 | 0.54 | 0.54 |
| 2.121315 | 6.274626 | 4.153311 | 4.153311 |
| 155.220726 | 160.728526 | 5.50779999999997 | 5.5078 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 33 |
| samples | 33 |
| brightness_mean | 0.246706733602051 |
| saturation_mean | 0.440363727140688 |
| frame_difference_mean | 0.22229598229751 |
| histogram_jumps_gt_0_5 | 21 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.0948031097650528 | 0.435243736383442 | N/A | N/A | N/A |
| 5 | 5 | 0.290455907583237 | 0.434970860566449 | 0.19640277326107 | 0.519115862086344 | 5 |
| 10 | 10 | 0.245180562138557 | 0.516018246187364 | 0.357439815998077 | 0.613251214462052 | 5 |
| 15 | 15 | 0.365086048841476 | 0.381102396514161 | 0.289610862731934 | 0.56841804460849 | 5 |
| 20 | 20 | 0.147107303142548 | 0.382019607843137 | 0.295368731021881 | 0.71349010252439 | 5 |
| 25 | 25 | 0.193180307745934 | 0.435442810457516 | 0.139235854148865 | 0.576735039106512 | 5 |
| 30 | 30 | 0.284560203552246 | 0.364314814814815 | 0.217481210827827 | 0.445954378760687 | 5 |
| 35 | 35 | 0.221458062529564 | 0.465908224400871 | 0.188285693526268 | 0.528390100064215 | 5 |
| 40 | 40 | 0.255701541900635 | 0.477514433551198 | 0.135946616530418 | 0.318301665329809 | 5 |
| 45 | 45 | 0.169418036937714 | 0.466974945533769 | 0.123423479497433 | 0.366435177291101 | 5 |
| 50 | 50 | 0.397556900978088 | 0.466333605664488 | 0.269543051719666 | 0.518900009438532 | 5 |
| 55 | 55 | 0.166634261608124 | 0.508781862745098 | 0.263771772384644 | 0.571625999307545 | 5 |
| 60 | 60 | 0.243742093443871 | 0.467387527233115 | 0.221909046173096 | 0.319675891750366 | 5 |
| 65 | 65 | 0.186013624072075 | 0.53568954248366 | 0.179596155881882 | 0.341286144600334 | 5 |
| 70 | 70 | 0.324552536010742 | 0.476357843137255 | 0.212111935019493 | 0.738336830269589 | 5 |
| 75 | 75 | 0.244778335094452 | 0.494523692810458 | 0.185346677899361 | 0.749098032824673 | 5 |
| 80 | 80 | 0.146664500236511 | 0.491351851851852 | 0.133409053087234 | 0.384015923393486 | 5 |
| 85 | 85 | 0.186771526932716 | 0.522708877995643 | 0.162703454494476 | 0.463223814747515 | 5 |
| 90 | 90 | 0.219176217913628 | 0.513087145969499 | 0.168459698557854 | 0.463654686915805 | 5 |
| 95 | 95 | 0.198418036103249 | 0.485789760348584 | 0.175019070506096 | 0.654924187677963 | 5 |
| 100 | 100 | 0.19008906185627 | 0.523969498910675 | 0.168671026825905 | 0.736978990197742 | 5 |
| 105 | 105 | 0.22745019197464 | 0.400686546840959 | 0.211606755852699 | 0.426196739568077 | 5 |
| 110 | 110 | 0.255605131387711 | 0.520645152505447 | 0.235037878155708 | 0.648973553643386 | 5 |
| 115 | 115 | 0.263025611639023 | 0.476434368191721 | 0.212840422987938 | 0.69727844236043 | 5 |
| 120 | 120 | 0.236051470041275 | 0.440031318082789 | 0.142016619443893 | 0.66162507041542 | 5 |
| 125 | 125 | 0.224701538681984 | 0.475738562091503 | 0.151973038911819 | 0.49437214636705 | 5 |
| 130 | 130 | 0.238285422325134 | 0.536607026143791 | 0.125634551048279 | 0.783216953330566 | 5 |
| 135 | 135 | 0.286993205547333 | 0.432247004357298 | 0.151042774319649 | 0.811018573132164 | 5 |
| 140 | 140 | 0.229232043027878 | 0.450023148148148 | 0.21704275906086 | 0.762068700841535 | 5 |
| 145 | 145 | 0.182958617806435 | 0.544342864923747 | 0.107808820903301 | 0.426359188714332 | 5 |
| 150 | 150 | 0.368032693862915 | 0.350061274509804 | 0.249105125665665 | 0.612408191137252 | 5 |
| 155 | 155 | 1.47058826769353e-05 | 0.000555555555555556 | 0.368017971515656 | 0.619230129549945 | 5 |
| 160 | 160 | 0.857623398303986 | 0.0591388888888889 | 0.857608735561371 | 1 | 5 |


## Record 07 — H20: whole_song_reproduction_check

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 3ec52c974fc776736ee8d7f3d1fb759e501e35ae95bbf18ce38c1ee6ff68f622 |
| started_utc | 2026-09-10T06:25:28.518214+00:00 |
| completed_utc | 2026-09-10T06:25:34.317759+00:00 |
| source_id | 1zPxR0JyPp4JhLxWS_zfENcC9znXerQIj |
| character | HIRO |
| alias | H20 |
| label | whole_song_reproduction_check |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\【学マス】篠澤広「初」 3DMV-(592p30).mp4 |
| filename | 【学マス】篠澤広「初」 3DMV-(592p30).mp4 |
| size_bytes | 37265987 |
| sha256 | 3ae933080d1da33631c2f491aea6969b0b2801cc48442c4023290632ae22aed0 |
| start_s | 0 |
| end_s | 155.178957 |
| duration_s | 155.178957 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 3ae933080d1da33631c2f491aea6969b0b2801cc48442c4023290632ae22aed0 |
| source_id | 1zPxR0JyPp4JhLxWS_zfENcC9znXerQIj |
| character | HIRO |
| alias | H20 |
| label | whole_song_reproduction_check |
| boundary_note | N/A |
| parameters.method_version | 2026-09-10-v1 |
| parameters.audio_sr_hz | 22050 |
| parameters.nfft | 2048 |
| parameters.hop | 512 |
| parameters.fft_window | periodic Hann |
| parameters.custom_spectral_center | false |
| parameters.rms_percentile_method | linear |
| parameters.rms_floor | 1e-12 |
| parameters.flatness_power_floor | 1e-10 |
| parameters.cv_ddof | 0 |
| parameters.audio_stream | first (0:a:0) |
| parameters.audio_signal | full unseparated mix, mono for features; native channels for R128 |
| parameters.trim_order | decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim |
| parameters.loudness_filter | ebur128=peak=true |
| parameters.silence_filter | silencedetect=noise=-50dB:d=0.5 |
| parameters.start_s | 0 |
| parameters.end_s | N/A |
| parameters.music | true |
| parameters.visual_step_s | 5 |
| parameters.skip_visual | false |
| parameters.visual_size[0] | 160 |
| parameters.visual_size[1] | 90 |
| parameters.visual_resize | INTER_AREA, whole frame with aspect distortion |
| parameters.visual_grayscale | OpenCV BGR2GRAY /255 |
| parameters.visual_saturation | OpenCV HSV S/255 |
| parameters.histogram | 8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5 |
| parameters.ffmpeg_threads | 1 |
| parameters.music_parameters.onset | librosa onset_strength; center=True; aggregate=mean |
| parameters.music_parameters.beat | start_bpm120, tightness100, trim=True |
| parameters.music_parameters.local_tempo | start_bpm120,std_bpm1,ac_size8,max_tempo320,aggregate=None |
| parameters.music_parameters.chroma | chroma_stft,tuning0,norm1,center=True |
| parameters.music_parameters.tonnetz | 6D coordinates from chroma_stft, adjacent Euclidean distance |
| software.python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| software.platform | Windows-11-10.0.26200-SP0 |
| software.numpy | 2.1.2 |
| software.ffmpeg_command | ffmpeg |
| software.ffprobe_command | ffprobe |
| software.ffmpeg_version | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101<br><br>Exiting with exit code 0 |
| software.ffprobe_version | ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101 |
| software.opencv | 4.13.0 |
| software.librosa | 1.0.0 |
| software.scipy | 1.18.0 |
| script_sha256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


### Source probe

| Probe field | Value |
| --- | --- |
| streams[0].index | 0 |
| streams[0].codec_name | h264 |
| streams[0].codec_long_name | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 |
| streams[0].profile | High |
| streams[0].codec_type | video |
| streams[0].codec_tag_string | avc1 |
| streams[0].codec_tag | 0x31637661 |
| streams[0].mime_codec_string | avc1.64001f |
| streams[0].width | 1280 |
| streams[0].height | 592 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 592 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 80:37 |
| streams[0].pix_fmt | yuv420p |
| streams[0].level | 31 |
| streams[0].color_range | tv |
| streams[0].color_space | bt709 |
| streams[0].color_transfer | bt709 |
| streams[0].color_primaries | bt709 |
| streams[0].chroma_location | left |
| streams[0].field_order | progressive |
| streams[0].is_avc | true |
| streams[0].nal_length_size | 4 |
| streams[0].id | 0x1 |
| streams[0].r_frame_rate | 30/1 |
| streams[0].avg_frame_rate | 30/1 |
| streams[0].time_base | 1/15360 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 2382848 |
| streams[0].duration | 155.133333 |
| streams[0].bit_rate | 1729468 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 4654 |
| streams[0].extradata_size | 43 |
| streams[0].disposition.default | 1 |
| streams[0].disposition.dub | 0 |
| streams[0].disposition.original | 0 |
| streams[0].disposition.comment | 0 |
| streams[0].disposition.lyrics | 0 |
| streams[0].disposition.karaoke | 0 |
| streams[0].disposition.forced | 0 |
| streams[0].disposition.hearing_impaired | 0 |
| streams[0].disposition.visual_impaired | 0 |
| streams[0].disposition.clean_effects | 0 |
| streams[0].disposition.attached_pic | 0 |
| streams[0].disposition.timed_thumbnails | 0 |
| streams[0].disposition.non_diegetic | 0 |
| streams[0].disposition.captions | 0 |
| streams[0].disposition.descriptions | 0 |
| streams[0].disposition.metadata | 0 |
| streams[0].disposition.dependent | 0 |
| streams[0].disposition.still_image | 0 |
| streams[0].disposition.multilayer | 0 |
| streams[0].tags.language | und |
| streams[0].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[1].index | 1 |
| streams[1].codec_name | aac |
| streams[1].codec_long_name | AAC (Advanced Audio Coding) |
| streams[1].profile | LC |
| streams[1].codec_type | audio |
| streams[1].codec_tag_string | mp4a |
| streams[1].codec_tag | 0x6134706d |
| streams[1].mime_codec_string | mp4a.40.2 |
| streams[1].sample_fmt | fltp |
| streams[1].sample_rate | 44100 |
| streams[1].channels | 2 |
| streams[1].channel_layout | stereo |
| streams[1].bits_per_sample | 0 |
| streams[1].initial_padding | 0 |
| streams[1].id | 0x2 |
| streams[1].r_frame_rate | 0/0 |
| streams[1].avg_frame_rate | 0/0 |
| streams[1].time_base | 1/44100 |
| streams[1].start_pts | 0 |
| streams[1].start_time | 0.000000 |
| streams[1].duration_ts | 6843392 |
| streams[1].duration | 155.178957 |
| streams[1].bit_rate | 128019 |
| streams[1].nb_frames | 6683 |
| streams[1].extradata_size | 16 |
| streams[1].disposition.default | 1 |
| streams[1].disposition.dub | 0 |
| streams[1].disposition.original | 0 |
| streams[1].disposition.comment | 0 |
| streams[1].disposition.lyrics | 0 |
| streams[1].disposition.karaoke | 0 |
| streams[1].disposition.forced | 0 |
| streams[1].disposition.hearing_impaired | 0 |
| streams[1].disposition.visual_impaired | 0 |
| streams[1].disposition.clean_effects | 0 |
| streams[1].disposition.attached_pic | 0 |
| streams[1].disposition.timed_thumbnails | 0 |
| streams[1].disposition.non_diegetic | 0 |
| streams[1].disposition.captions | 0 |
| streams[1].disposition.descriptions | 0 |
| streams[1].disposition.metadata | 0 |
| streams[1].disposition.dependent | 0 |
| streams[1].disposition.still_image | 0 |
| streams[1].disposition.multilayer | 0 |
| streams[1].tags.language | und |
| streams[1].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[2].index | 2 |
| streams[2].codec_name | png |
| streams[2].codec_long_name | PNG (Portable Network Graphics) image |
| streams[2].codec_type | video |
| streams[2].codec_tag_string | [0][0][0][0] |
| streams[2].codec_tag | 0x0000 |
| streams[2].width | 1280 |
| streams[2].height | 720 |
| streams[2].coded_width | 1280 |
| streams[2].coded_height | 720 |
| streams[2].has_b_frames | 0 |
| streams[2].pix_fmt | rgb24 |
| streams[2].level | -99 |
| streams[2].color_range | pc |
| streams[2].color_space | gbr |
| streams[2].id | 0x0 |
| streams[2].r_frame_rate | 90000/1 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/90000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 13966106 |
| streams[2].duration | 155.178956 |
| streams[2].disposition.default | 0 |
| streams[2].disposition.dub | 0 |
| streams[2].disposition.original | 0 |
| streams[2].disposition.comment | 0 |
| streams[2].disposition.lyrics | 0 |
| streams[2].disposition.karaoke | 0 |
| streams[2].disposition.forced | 0 |
| streams[2].disposition.hearing_impaired | 0 |
| streams[2].disposition.visual_impaired | 0 |
| streams[2].disposition.clean_effects | 0 |
| streams[2].disposition.attached_pic | 1 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| chapters | [] |
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\【学マス】篠澤広「初」 3DMV-(592p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 155.178957 |
| format.size | 37265987 |
| format.bit_rate | 1921187 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】篠澤広「初」 3DMV |
| format.tags.artist | 篠澤広 大好きマン |
| format.tags.genre | Gaming |
| format.tags.date | 20241011 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=ivNDdkumEl4 |
| format.tags.description | 広可愛いね<br><br>著作元<br>THE IDOLM@STER™&amp; ©Bandai Namco Entertainment Inc.<br><br>#学園アイドルマスター <br>#学マス <br>#篠澤広 |
| format.tags.synopsis | 広可愛いね<br><br>著作元<br>THE IDOLM@STER™&amp; ©Bandai Namco Entertainment Inc.<br><br>#学園アイドルマスター <br>#学マス <br>#篠澤広 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 3421696 |
| analyzed_audio_duration_s | 155.1789569161 |
| stft_frames | 6680 |
| flux_transitions | 6679 |
| rms_linear | 0.0845763161398835 |
| rms_p10_linear | 0.0429808929928329 |
| rms_p90_linear | 0.116249914422186 |
| rms_p90_p10_db | 8.64234414965983 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 0 |
| centroid_hz_mean | 2354.76419184442 |
| flatness_mean | 0.0285001797681828 |
| positive_normalized_flux_mean | 0.0257893717284197 |
| flux_cv | 0.292487753708619 |
| tempo_bpm | 112.34714673913 |
| beat_count | 282 |
| beat_interval_count | 281 |
| beat_interval_cv | 0.048073734870249 |
| local_tempo_count | 6684 |
| local_tempo_cv | 0.202736073314351 |
| chroma_frames | 6684 |
| chroma_entropy_bits_mean | 3.00636959075928 |
| tonnetz_transition_count | 6683 |
| tonnetz_motion_mean | 0.151006131921803 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -20.3 |
| lra_lu | 5.8 |
| true_peak_dbfs | -6.3 |
| silence_seconds | 0 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -20.3 LUFS<br>    Threshold: -30.4 LUFS<br><br>  Loudness range:<br>    LRA:         5.8 LU<br>    Threshold: -40.3 LUFS<br>    LRA low:   -23.9 LUFS<br>    LRA high:  -18.1 LUFS<br><br>  True peak:<br>    Peak:       -6.3 dBFS<br>[out#0/null @ 000001abca707400] video:0KiB audio:26732KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:02:35.17 bitrate=N/A speed= 106x elapsed=0:00:01.46 |
| ffmpeg_stderr_sha256 | 72098ca4ed1541e6b39a8d4d8ba4144714aa065188cb0a04f24b2ddac3023493 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 32 |
| samples | 32 |
| brightness_mean | 0.302199866622686 |
| saturation_mean | 0.511921900531046 |
| frame_difference_mean | 0.240365489596321 |
| histogram_jumps_gt_0_5 | 17 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.259940892457962 | 0.401324074074074 | N/A | N/A | N/A |
| 5 | 5 | 0.0962317585945129 | 0.820181644880174 | 0.222176477313042 | 0.763013977599931 | 5 |
| 10 | 10 | 0.366644889116287 | 0.656368736383442 | 0.274036228656769 | 0.701802109311389 | 5 |
| 15 | 15 | 0.202990755438805 | 0.648164760348584 | 0.209744572639465 | 0.714062050637598 | 5 |
| 20 | 20 | 0.486161261796951 | 0.365895697167756 | 0.318926453590393 | 0.797628286751022 | 5 |
| 25 | 25 | 0.549483418464661 | 0.360479847494553 | 0.184079796075821 | 0.310826862308973 | 5 |
| 30 | 30 | 0.410943955183029 | 0.462232298474946 | 0.216020435094833 | 0.403603166594477 | 5 |
| 35 | 35 | 0.32487964630127 | 0.450316721132898 | 0.275648713111877 | 0.480867698465108 | 5 |
| 40 | 40 | 0.23030012845993 | 0.56615522875817 | 0.20885893702507 | 0.42954829295539 | 5 |
| 45 | 45 | 0.290639996528625 | 0.631416122004357 | 0.252953171730042 | 0.553963007408007 | 5 |
| 50 | 50 | 0.206070557236671 | 0.467614651416122 | 0.335061848163605 | 0.638839322109432 | 5 |
| 55 | 55 | 0.229930832982063 | 0.661123093681917 | 0.209738835692406 | 0.876938978129998 | 5 |
| 60 | 60 | 0.321281343698502 | 0.63506917211329 | 0.244180575013161 | 0.579187406795853 | 5 |
| 65 | 65 | 0.351892977952957 | 0.702244825708061 | 0.237697184085846 | 0.944919303560878 | 5 |
| 70 | 70 | 0.312708050012589 | 0.646348039215686 | 0.207513898611069 | 0.387716569339012 | 5 |
| 75 | 75 | 0.550769865512848 | 0.332020969498911 | 0.321244835853577 | 0.635781351450614 | 5 |
| 80 | 80 | 0.456931084394455 | 0.397753812636166 | 0.190710246562958 | 0.438838578778311 | 5 |
| 85 | 85 | 0.352832227945328 | 0.37346568627451 | 0.351554214954376 | 0.501368384009493 | 5 |
| 90 | 90 | 0.228368729352951 | 0.403974128540305 | 0.226952075958252 | 0.616224184950454 | 5 |
| 95 | 95 | 0.328933537006378 | 0.4525 | 0.35809588432312 | 0.503425467761994 | 5 |
| 100 | 100 | 0.135546565055847 | 0.551148965141612 | 0.240680038928986 | 0.46843547604054 | 5 |
| 105 | 105 | 0.256110310554504 | 0.491521786492375 | 0.169217333197594 | 0.431487592439056 | 5 |
| 110 | 110 | 0.276206701993942 | 0.521946078431373 | 0.234760373830795 | 0.330630218287197 | 5 |
| 115 | 115 | 0.154713243246078 | 0.397587418300654 | 0.208505988121033 | 0.71970551568875 | 5 |
| 120 | 120 | 0.166159331798553 | 0.732634259259259 | 0.172504380345345 | 0.450786205994232 | 5 |
| 125 | 125 | 0.221026688814163 | 0.598105936819172 | 0.114915855228901 | 0.441941548356774 | 5 |
| 130 | 130 | 0.24213345348835 | 0.373123910675381 | 0.142196625471115 | 0.708739305801091 | 5 |
| 135 | 135 | 0.403691202402115 | 0.353989651416122 | 0.328306138515472 | 0.486058770781926 | 5 |
| 140 | 140 | 0.416627466678619 | 0.395472766884532 | 0.299450993537903 | 0.496701078243659 | 5 |
| 145 | 145 | 0.351580321788788 | 0.429699618736383 | 0.256402224302292 | 0.58138524276706 | 5 |
| 150 | 150 | 0.303373664617538 | 0.499066448801743 | 0.217723056674004 | 0.48336181721649 | 5 |
| 155 | 155 | 0.18529087305069 | 0.602554466230937 | 0.221472784876823 | 0.544324603361606 | 5 |


## Record 08 — H21: whole_song_reproduction_check

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 6b1150a4db70662f9fba6ec10333189495c2d3747a690d86c9466e45bb9c6417 |
| started_utc | 2026-09-10T06:25:29.928515+00:00 |
| completed_utc | 2026-09-10T06:25:36.143224+00:00 |
| source_id | 1OXLlFgDZOfdom_Sywd_lF_j-dimUZeqp |
| character | HIRO |
| alias | H21 |
| label | whole_song_reproduction_check |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「Howling over the World」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| filename | 4K HDR「Howling over the World」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| size_bytes | 42489463 |
| sha256 | cbfae7e9f90821d0c70a16201a9ba462603548f899fa93b5ab94fb76c0e248f7 |
| start_s | 0 |
| end_s | 110.225125 |
| duration_s | 110.225125 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | cbfae7e9f90821d0c70a16201a9ba462603548f899fa93b5ab94fb76c0e248f7 |
| source_id | 1OXLlFgDZOfdom_Sywd_lF_j-dimUZeqp |
| character | HIRO |
| alias | H21 |
| label | whole_song_reproduction_check |
| boundary_note | N/A |
| parameters.method_version | 2026-09-10-v1 |
| parameters.audio_sr_hz | 22050 |
| parameters.nfft | 2048 |
| parameters.hop | 512 |
| parameters.fft_window | periodic Hann |
| parameters.custom_spectral_center | false |
| parameters.rms_percentile_method | linear |
| parameters.rms_floor | 1e-12 |
| parameters.flatness_power_floor | 1e-10 |
| parameters.cv_ddof | 0 |
| parameters.audio_stream | first (0:a:0) |
| parameters.audio_signal | full unseparated mix, mono for features; native channels for R128 |
| parameters.trim_order | decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim |
| parameters.loudness_filter | ebur128=peak=true |
| parameters.silence_filter | silencedetect=noise=-50dB:d=0.5 |
| parameters.start_s | 0 |
| parameters.end_s | N/A |
| parameters.music | true |
| parameters.visual_step_s | 5 |
| parameters.skip_visual | false |
| parameters.visual_size[0] | 160 |
| parameters.visual_size[1] | 90 |
| parameters.visual_resize | INTER_AREA, whole frame with aspect distortion |
| parameters.visual_grayscale | OpenCV BGR2GRAY /255 |
| parameters.visual_saturation | OpenCV HSV S/255 |
| parameters.histogram | 8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5 |
| parameters.ffmpeg_threads | 1 |
| parameters.music_parameters.onset | librosa onset_strength; center=True; aggregate=mean |
| parameters.music_parameters.beat | start_bpm120, tightness100, trim=True |
| parameters.music_parameters.local_tempo | start_bpm120,std_bpm1,ac_size8,max_tempo320,aggregate=None |
| parameters.music_parameters.chroma | chroma_stft,tuning0,norm1,center=True |
| parameters.music_parameters.tonnetz | 6D coordinates from chroma_stft, adjacent Euclidean distance |
| software.python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| software.platform | Windows-11-10.0.26200-SP0 |
| software.numpy | 2.1.2 |
| software.ffmpeg_command | ffmpeg |
| software.ffprobe_command | ffprobe |
| software.ffmpeg_version | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101<br><br>Exiting with exit code 0 |
| software.ffprobe_version | ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101 |
| software.opencv | 4.13.0 |
| software.librosa | 1.0.0 |
| software.scipy | 1.18.0 |
| script_sha256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


### Source probe

| Probe field | Value |
| --- | --- |
| streams[0].index | 0 |
| streams[0].codec_name | h264 |
| streams[0].codec_long_name | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 |
| streams[0].profile | High |
| streams[0].codec_type | video |
| streams[0].codec_tag_string | avc1 |
| streams[0].codec_tag | 0x31637661 |
| streams[0].mime_codec_string | avc1.640020 |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
| streams[0].pix_fmt | yuv420p |
| streams[0].level | 32 |
| streams[0].color_range | tv |
| streams[0].color_space | bt709 |
| streams[0].color_transfer | bt709 |
| streams[0].color_primaries | bt709 |
| streams[0].chroma_location | left |
| streams[0].field_order | progressive |
| streams[0].is_avc | true |
| streams[0].nal_length_size | 4 |
| streams[0].id | 0x1 |
| streams[0].r_frame_rate | 60/1 |
| streams[0].avg_frame_rate | 60/1 |
| streams[0].time_base | 1/15360 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 1691904 |
| streams[0].duration | 110.150000 |
| streams[0].bit_rate | 2896660 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 6609 |
| streams[0].extradata_size | 43 |
| streams[0].disposition.default | 1 |
| streams[0].disposition.dub | 0 |
| streams[0].disposition.original | 0 |
| streams[0].disposition.comment | 0 |
| streams[0].disposition.lyrics | 0 |
| streams[0].disposition.karaoke | 0 |
| streams[0].disposition.forced | 0 |
| streams[0].disposition.hearing_impaired | 0 |
| streams[0].disposition.visual_impaired | 0 |
| streams[0].disposition.clean_effects | 0 |
| streams[0].disposition.attached_pic | 0 |
| streams[0].disposition.timed_thumbnails | 0 |
| streams[0].disposition.non_diegetic | 0 |
| streams[0].disposition.captions | 0 |
| streams[0].disposition.descriptions | 0 |
| streams[0].disposition.metadata | 0 |
| streams[0].disposition.dependent | 0 |
| streams[0].disposition.still_image | 0 |
| streams[0].disposition.multilayer | 0 |
| streams[0].tags.language | und |
| streams[0].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[0].side_data_list[0].side_data_type | Content light level metadata |
| streams[0].side_data_list[0].max_content | 1000 |
| streams[0].side_data_list[0].max_average | 200 |
| streams[1].index | 1 |
| streams[1].codec_name | aac |
| streams[1].codec_long_name | AAC (Advanced Audio Coding) |
| streams[1].profile | LC |
| streams[1].codec_type | audio |
| streams[1].codec_tag_string | mp4a |
| streams[1].codec_tag | 0x6134706d |
| streams[1].mime_codec_string | mp4a.40.2 |
| streams[1].sample_fmt | fltp |
| streams[1].sample_rate | 44100 |
| streams[1].channels | 2 |
| streams[1].channel_layout | stereo |
| streams[1].bits_per_sample | 0 |
| streams[1].initial_padding | 0 |
| streams[1].id | 0x2 |
| streams[1].r_frame_rate | 0/0 |
| streams[1].avg_frame_rate | 0/0 |
| streams[1].time_base | 1/44100 |
| streams[1].start_pts | 0 |
| streams[1].start_time | 0.000000 |
| streams[1].duration_ts | 4860928 |
| streams[1].duration | 110.225125 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 4747 |
| streams[1].extradata_size | 16 |
| streams[1].disposition.default | 1 |
| streams[1].disposition.dub | 0 |
| streams[1].disposition.original | 0 |
| streams[1].disposition.comment | 0 |
| streams[1].disposition.lyrics | 0 |
| streams[1].disposition.karaoke | 0 |
| streams[1].disposition.forced | 0 |
| streams[1].disposition.hearing_impaired | 0 |
| streams[1].disposition.visual_impaired | 0 |
| streams[1].disposition.clean_effects | 0 |
| streams[1].disposition.attached_pic | 0 |
| streams[1].disposition.timed_thumbnails | 0 |
| streams[1].disposition.non_diegetic | 0 |
| streams[1].disposition.captions | 0 |
| streams[1].disposition.descriptions | 0 |
| streams[1].disposition.metadata | 0 |
| streams[1].disposition.dependent | 0 |
| streams[1].disposition.still_image | 0 |
| streams[1].disposition.multilayer | 0 |
| streams[1].tags.language | jpn |
| streams[1].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[2].index | 2 |
| streams[2].codec_name | png |
| streams[2].codec_long_name | PNG (Portable Network Graphics) image |
| streams[2].codec_type | video |
| streams[2].codec_tag_string | [0][0][0][0] |
| streams[2].codec_tag | 0x0000 |
| streams[2].width | 1280 |
| streams[2].height | 720 |
| streams[2].coded_width | 1280 |
| streams[2].coded_height | 720 |
| streams[2].has_b_frames | 0 |
| streams[2].pix_fmt | rgb24 |
| streams[2].level | -99 |
| streams[2].color_range | pc |
| streams[2].color_space | gbr |
| streams[2].id | 0x0 |
| streams[2].r_frame_rate | 90000/1 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/90000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 9920261 |
| streams[2].duration | 110.225122 |
| streams[2].disposition.default | 0 |
| streams[2].disposition.dub | 0 |
| streams[2].disposition.original | 0 |
| streams[2].disposition.comment | 0 |
| streams[2].disposition.lyrics | 0 |
| streams[2].disposition.karaoke | 0 |
| streams[2].disposition.forced | 0 |
| streams[2].disposition.hearing_impaired | 0 |
| streams[2].disposition.visual_impaired | 0 |
| streams[2].disposition.clean_effects | 0 |
| streams[2].disposition.attached_pic | 1 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| chapters | [] |
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「Howling over the World」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 110.225125 |
| format.size | 42489463 |
| format.bit_rate | 3083831 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 4K HDR「Howling over the World」 (篠澤広 ソロ SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】 |
| format.tags.artist | 十六夜カズヤP / 16KazuyaP |
| format.tags.genre | Gaming |
| format.tags.date | 20250601 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=t4jb8WFheCM |
| format.tags.description | 「Howling over the World」 (#篠澤広   ソロ SSR) 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm45042393<br><br>作詞・作曲・編曲： 烏屋茶房<br>歌：篠澤広 (CV. 川村玲奈)<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 #学園偶像大師 |
| format.tags.synopsis | 「Howling over the World」 (#篠澤広   ソロ SSR) 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm45042393<br><br>作詞・作曲・編曲： 烏屋茶房<br>歌：篠澤広 (CV. 川村玲奈)<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 #学園偶像大師 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 2430464 |
| analyzed_audio_duration_s | 110.225124716553 |
| stft_frames | 4744 |
| flux_transitions | 4743 |
| rms_linear | 0.188500659003573 |
| rms_p10_linear | 0.00465108368461183 |
| rms_p90_linear | 0.2706225995536 |
| rms_p90_p10_db | 35.2961981571966 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 317 |
| centroid_hz_mean | 2575.71005638518 |
| flatness_mean | 0.10739499008123 |
| positive_normalized_flux_mean | 0.0236632586495361 |
| flux_cv | 0.478744188173194 |
| tempo_bpm | 135.999177631579 |
| beat_count | 230 |
| beat_interval_count | 229 |
| beat_interval_cv | 0.0392858787074563 |
| local_tempo_count | 4748 |
| local_tempo_cv | 0.21471669144538 |
| chroma_frames | 4748 |
| chroma_entropy_bits_mean | 3.04579186439514 |
| tonnetz_transition_count | 4747 |
| tonnetz_motion_mean | 0.110332674934412 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -13.5 |
| lra_lu | 6.6 |
| true_peak_dbfs | -0 |
| silence_seconds | 9.371157 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -13.5 LUFS<br>    Threshold: -23.8 LUFS<br><br>  Loudness range:<br>    LRA:         6.6 LU<br>    Threshold: -33.9 LUFS<br>    LRA low:   -18.3 LUFS<br>    LRA high:  -11.7 LUFS<br><br>  True peak:<br>    Peak:       -0.0 dBFS<br>[out#0/null @ 0000021f6ed88940] video:0KiB audio:18988KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:01:50.22 bitrate=N/A speed= 100x elapsed=0:00:01.10 |
| ffmpeg_stderr_sha256 | db948857e8392693e773af973fe2928cfbd98f2775bf161049466ef26ac2d56b |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 1.716984 | 4.509297 | 2.792313 | 2.792313 |
| 103.646281 | 110.225125 | 6.578844 | 6.578844 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 23 |
| samples | 23 |
| brightness_mean | 0.252902740914736 |
| saturation_mean | 0.428721878848158 |
| frame_difference_mean | 0.227845540439541 |
| histogram_jumps_gt_0_5 | 19 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.134972497820854 | 0.473797930283224 | N/A | N/A | N/A |
| 5 | 5 | 0.122561819851398 | 0.462165577342048 | 0.196276679635048 | 0.514741722043701 | 5 |
| 10 | 10 | 0.171041935682297 | 0.517733932461874 | 0.0818848088383675 | 0.274801994414907 | 5 |
| 15 | 15 | 0.251875549554825 | 0.483103758169935 | 0.158992111682892 | 0.760724844038503 | 5 |
| 20 | 20 | 0.195043042302132 | 0.478163671023965 | 0.135980665683746 | 0.680233686122153 | 5 |
| 25 | 25 | 0.323103785514832 | 0.378482843137255 | 0.170011714100838 | 0.544549710393095 | 5 |
| 30 | 30 | 0.337794929742813 | 0.403269063180828 | 0.222668841481209 | 0.285887387495342 | 5 |
| 35 | 35 | 0.177558824419975 | 0.515589052287582 | 0.234381541609764 | 0.740881530702916 | 5 |
| 40 | 40 | 0.333437353372574 | 0.419537037037037 | 0.234027773141861 | 0.746507037835163 | 5 |
| 45 | 45 | 0.19619582593441 | 0.470225762527233 | 0.222914755344391 | 0.743934924466714 | 5 |
| 50 | 50 | 0.319420516490936 | 0.425034586056645 | 0.210235565900803 | 0.751137609488786 | 5 |
| 55 | 55 | 0.129145979881287 | 0.491928376906318 | 0.212915033102036 | 0.82867606463324 | 5 |
| 60 | 60 | 0.12871977686882 | 0.629035947712418 | 0.112346142530441 | 0.575670282450344 | 5 |
| 65 | 65 | 0.125505730509758 | 0.627568082788671 | 0.131823539733887 | 0.14900564606024 | 5 |
| 70 | 70 | 0.242999449372292 | 0.466690087145969 | 0.175724148750305 | 0.807035718463229 | 5 |
| 75 | 75 | 0.219788685441017 | 0.538041666666667 | 0.116200983524323 | 0.611523951514032 | 5 |
| 80 | 80 | 0.250260353088379 | 0.502257625272331 | 0.125598579645157 | 0.514258078306015 | 5 |
| 85 | 85 | 0.447038680315018 | 0.378966503267974 | 0.274577885866165 | 0.772096777686691 | 5 |
| 90 | 90 | 0.299110591411591 | 0.279787037037037 | 0.309192299842834 | 0.715621723803909 | 5 |
| 95 | 95 | 0.206565648317337 | 0.352477124183007 | 0.272546023130417 | 0.645690575336954 | 5 |
| 100 | 100 | 0.353172689676285 | 0.416372549019608 | 0.209794372320175 | 0.568809583623108 | 5 |
| 105 | 105 | 3.78540353267454e-05 | 0.0896527777777778 | 0.353134751319885 | 0.708778323780239 | 5 |
| 110 | 110 | 0.851411521434784 | 0.0607222222222222 | 0.851373672485352 | 1 | 5 |


## Record 09 — H22: whole_song_reproduction_check

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 5d912092dcb470a9a3f76e7f1817197093e68180357339f0e2119a8aa8923047 |
| started_utc | 2026-09-10T06:25:34.819370+00:00 |
| completed_utc | 2026-09-10T06:25:42.871378+00:00 |
| source_id | 1tdzAna_WcWmo9RzC5lyLnliiyJaoDGpy |
| character | HIRO |
| alias | H22 |
| label | whole_song_reproduction_check |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「がむしゃらに行こう！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| filename | 4K HDR「がむしゃらに行こう！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| size_bytes | 41525073 |
| sha256 | 42ddef86a794641182d2b3ae143b5afd2a6b68bf2f08a5f989e373c45cd70ee9 |
| start_s | 0 |
| end_s | 110.457324 |
| duration_s | 110.457324 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 42ddef86a794641182d2b3ae143b5afd2a6b68bf2f08a5f989e373c45cd70ee9 |
| source_id | 1tdzAna_WcWmo9RzC5lyLnliiyJaoDGpy |
| character | HIRO |
| alias | H22 |
| label | whole_song_reproduction_check |
| boundary_note | N/A |
| parameters.method_version | 2026-09-10-v1 |
| parameters.audio_sr_hz | 22050 |
| parameters.nfft | 2048 |
| parameters.hop | 512 |
| parameters.fft_window | periodic Hann |
| parameters.custom_spectral_center | false |
| parameters.rms_percentile_method | linear |
| parameters.rms_floor | 1e-12 |
| parameters.flatness_power_floor | 1e-10 |
| parameters.cv_ddof | 0 |
| parameters.audio_stream | first (0:a:0) |
| parameters.audio_signal | full unseparated mix, mono for features; native channels for R128 |
| parameters.trim_order | decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim |
| parameters.loudness_filter | ebur128=peak=true |
| parameters.silence_filter | silencedetect=noise=-50dB:d=0.5 |
| parameters.start_s | 0 |
| parameters.end_s | N/A |
| parameters.music | true |
| parameters.visual_step_s | 5 |
| parameters.skip_visual | false |
| parameters.visual_size[0] | 160 |
| parameters.visual_size[1] | 90 |
| parameters.visual_resize | INTER_AREA, whole frame with aspect distortion |
| parameters.visual_grayscale | OpenCV BGR2GRAY /255 |
| parameters.visual_saturation | OpenCV HSV S/255 |
| parameters.histogram | 8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5 |
| parameters.ffmpeg_threads | 1 |
| parameters.music_parameters.onset | librosa onset_strength; center=True; aggregate=mean |
| parameters.music_parameters.beat | start_bpm120, tightness100, trim=True |
| parameters.music_parameters.local_tempo | start_bpm120,std_bpm1,ac_size8,max_tempo320,aggregate=None |
| parameters.music_parameters.chroma | chroma_stft,tuning0,norm1,center=True |
| parameters.music_parameters.tonnetz | 6D coordinates from chroma_stft, adjacent Euclidean distance |
| software.python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| software.platform | Windows-11-10.0.26200-SP0 |
| software.numpy | 2.1.2 |
| software.ffmpeg_command | ffmpeg |
| software.ffprobe_command | ffprobe |
| software.ffmpeg_version | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101<br><br>Exiting with exit code 0 |
| software.ffprobe_version | ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101 |
| software.opencv | 4.13.0 |
| software.librosa | 1.0.0 |
| software.scipy | 1.18.0 |
| script_sha256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


### Source probe

| Probe field | Value |
| --- | --- |
| streams[0].index | 0 |
| streams[0].codec_name | h264 |
| streams[0].codec_long_name | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 |
| streams[0].profile | High |
| streams[0].codec_type | video |
| streams[0].codec_tag_string | avc1 |
| streams[0].codec_tag | 0x31637661 |
| streams[0].mime_codec_string | avc1.640020 |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
| streams[0].pix_fmt | yuv420p |
| streams[0].level | 32 |
| streams[0].color_range | tv |
| streams[0].color_space | bt709 |
| streams[0].color_transfer | bt709 |
| streams[0].color_primaries | bt709 |
| streams[0].chroma_location | left |
| streams[0].field_order | progressive |
| streams[0].is_avc | true |
| streams[0].nal_length_size | 4 |
| streams[0].id | 0x1 |
| streams[0].r_frame_rate | 60/1 |
| streams[0].avg_frame_rate | 60/1 |
| streams[0].time_base | 1/15360 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 1695488 |
| streams[0].duration | 110.383333 |
| streams[0].bit_rate | 2799915 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 6623 |
| streams[0].extradata_size | 43 |
| streams[0].disposition.default | 1 |
| streams[0].disposition.dub | 0 |
| streams[0].disposition.original | 0 |
| streams[0].disposition.comment | 0 |
| streams[0].disposition.lyrics | 0 |
| streams[0].disposition.karaoke | 0 |
| streams[0].disposition.forced | 0 |
| streams[0].disposition.hearing_impaired | 0 |
| streams[0].disposition.visual_impaired | 0 |
| streams[0].disposition.clean_effects | 0 |
| streams[0].disposition.attached_pic | 0 |
| streams[0].disposition.timed_thumbnails | 0 |
| streams[0].disposition.non_diegetic | 0 |
| streams[0].disposition.captions | 0 |
| streams[0].disposition.descriptions | 0 |
| streams[0].disposition.metadata | 0 |
| streams[0].disposition.dependent | 0 |
| streams[0].disposition.still_image | 0 |
| streams[0].disposition.multilayer | 0 |
| streams[0].tags.language | und |
| streams[0].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[0].side_data_list[0].side_data_type | Content light level metadata |
| streams[0].side_data_list[0].max_content | 1000 |
| streams[0].side_data_list[0].max_average | 200 |
| streams[1].index | 1 |
| streams[1].codec_name | aac |
| streams[1].codec_long_name | AAC (Advanced Audio Coding) |
| streams[1].profile | LC |
| streams[1].codec_type | audio |
| streams[1].codec_tag_string | mp4a |
| streams[1].codec_tag | 0x6134706d |
| streams[1].mime_codec_string | mp4a.40.2 |
| streams[1].sample_fmt | fltp |
| streams[1].sample_rate | 44100 |
| streams[1].channels | 2 |
| streams[1].channel_layout | stereo |
| streams[1].bits_per_sample | 0 |
| streams[1].initial_padding | 0 |
| streams[1].id | 0x2 |
| streams[1].r_frame_rate | 0/0 |
| streams[1].avg_frame_rate | 0/0 |
| streams[1].time_base | 1/44100 |
| streams[1].start_pts | 0 |
| streams[1].start_time | 0.000000 |
| streams[1].duration_ts | 4871168 |
| streams[1].duration | 110.457324 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 4757 |
| streams[1].extradata_size | 16 |
| streams[1].disposition.default | 1 |
| streams[1].disposition.dub | 0 |
| streams[1].disposition.original | 0 |
| streams[1].disposition.comment | 0 |
| streams[1].disposition.lyrics | 0 |
| streams[1].disposition.karaoke | 0 |
| streams[1].disposition.forced | 0 |
| streams[1].disposition.hearing_impaired | 0 |
| streams[1].disposition.visual_impaired | 0 |
| streams[1].disposition.clean_effects | 0 |
| streams[1].disposition.attached_pic | 0 |
| streams[1].disposition.timed_thumbnails | 0 |
| streams[1].disposition.non_diegetic | 0 |
| streams[1].disposition.captions | 0 |
| streams[1].disposition.descriptions | 0 |
| streams[1].disposition.metadata | 0 |
| streams[1].disposition.dependent | 0 |
| streams[1].disposition.still_image | 0 |
| streams[1].disposition.multilayer | 0 |
| streams[1].tags.language | jpn |
| streams[1].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[2].index | 2 |
| streams[2].codec_name | png |
| streams[2].codec_long_name | PNG (Portable Network Graphics) image |
| streams[2].codec_type | video |
| streams[2].codec_tag_string | [0][0][0][0] |
| streams[2].codec_tag | 0x0000 |
| streams[2].width | 1280 |
| streams[2].height | 720 |
| streams[2].coded_width | 1280 |
| streams[2].coded_height | 720 |
| streams[2].has_b_frames | 0 |
| streams[2].pix_fmt | rgb24 |
| streams[2].level | -99 |
| streams[2].color_range | pc |
| streams[2].color_space | gbr |
| streams[2].id | 0x0 |
| streams[2].r_frame_rate | 90000/1 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/90000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 9941159 |
| streams[2].duration | 110.457322 |
| streams[2].disposition.default | 0 |
| streams[2].disposition.dub | 0 |
| streams[2].disposition.original | 0 |
| streams[2].disposition.comment | 0 |
| streams[2].disposition.lyrics | 0 |
| streams[2].disposition.karaoke | 0 |
| streams[2].disposition.forced | 0 |
| streams[2].disposition.hearing_impaired | 0 |
| streams[2].disposition.visual_impaired | 0 |
| streams[2].disposition.clean_effects | 0 |
| streams[2].disposition.attached_pic | 1 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| chapters | [] |
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「がむしゃらに行こう！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 110.457324 |
| format.size | 41525073 |
| format.bit_rate | 3007501 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 4K HDR「がむしゃらに行こう！」 (篠澤広 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】 |
| format.tags.artist | 十六夜カズヤP / 16KazuyaP |
| format.tags.genre | Gaming |
| format.tags.date | 20250929 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=_Yjg5ewXZXo |
| format.tags.description | 「がむしゃらに行こう！」 (#篠澤広 SSR) 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm45460155<br><br>歌：篠澤広 (CV. 川村玲奈)<br>作詞：SHOW (Digz, Inc. Group)<br>作曲：SHOW (Digz, Inc. Group)、Mitsu.J (Digz, Inc. Group)<br>編曲：Mitsu.J (Digz, Inc. Group)<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |
| format.tags.synopsis | 「がむしゃらに行こう！」 (#篠澤広 SSR) 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm45460155<br><br>歌：篠澤広 (CV. 川村玲奈)<br>作詞：SHOW (Digz, Inc. Group)<br>作曲：SHOW (Digz, Inc. Group)、Mitsu.J (Digz, Inc. Group)<br>編曲：Mitsu.J (Digz, Inc. Group)<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 2435584 |
| analyzed_audio_duration_s | 110.457324263039 |
| stft_frames | 4754 |
| flux_transitions | 4753 |
| rms_linear | 0.168668882251691 |
| rms_p10_linear | 0.0068449946505165 |
| rms_p90_linear | 0.24147248759445 |
| rms_p90_p10_db | 30.9498908615111 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 388 |
| centroid_hz_mean | 2349.37192778531 |
| flatness_mean | 0.114155520217756 |
| positive_normalized_flux_mean | 0.0244208803991586 |
| flux_cv | 0.492264588155156 |
| tempo_bpm | 129.19921875 |
| beat_count | 220 |
| beat_interval_count | 219 |
| beat_interval_cv | 0.0519744416255759 |
| local_tempo_count | 4758 |
| local_tempo_cv | 0.123285691095489 |
| chroma_frames | 4758 |
| chroma_entropy_bits_mean | 2.87870287895203 |
| tonnetz_transition_count | 4757 |
| tonnetz_motion_mean | 0.134461925389724 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -14.1 |
| lra_lu | 5.1 |
| true_peak_dbfs | 0.1 |
| silence_seconds | 10.383764 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -14.1 LUFS<br>    Threshold: -24.6 LUFS<br><br>  Loudness range:<br>    LRA:         5.1 LU<br>    Threshold: -34.7 LUFS<br>    LRA low:   -17.3 LUFS<br>    LRA high:  -12.2 LUFS<br><br>  True peak:<br>    Peak:        0.1 dBFS<br>[out#0/null @ 0000022946b383c0] video:0KiB audio:19028KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:01:50.45 bitrate=N/A speed=91.8x elapsed=0:00:01.20 |
| ffmpeg_stderr_sha256 | 5dfc8ca4ee2f51c5e21214c901ba53e4f58ae5fe61f7cc708551134b1a808e96 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 0 | 0.561497 | 0.561497 | 0.561497 |
| 2.02771 | 5.000726 | 2.973016 | 2.973016 |
| 103.608073 | 110.457324 | 6.849251 | 6.849252 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 23 |
| samples | 23 |
| brightness_mean | 0.374764359515646 |
| saturation_mean | 0.412970351425594 |
| frame_difference_mean | 0.205169625918974 |
| histogram_jumps_gt_0_5 | 13 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.134949624538422 | 0.47416802832244 | N/A | N/A | N/A |
| 5 | 5 | 0.283938199281693 | 0.343667755991285 | 0.364284873008728 | 0.618216124183156 | 5 |
| 10 | 10 | 0.371929466724396 | 0.353491557734205 | 0.116764709353447 | 0.467392117866743 | 5 |
| 15 | 15 | 0.36570206284523 | 0.374276688453159 | 0.0464915558695793 | 0.158087442533656 | 5 |
| 20 | 20 | 0.496823251247406 | 0.453997276688453 | 0.235141351819038 | 0.35050643933477 | 5 |
| 25 | 25 | 0.544437408447266 | 0.511468954248366 | 0.172788396477699 | 0.520041772854639 | 5 |
| 30 | 30 | 0.479172438383102 | 0.440363017429194 | 0.178499177098274 | 0.46576151169371 | 5 |
| 35 | 35 | 0.434664785861969 | 0.489407952069717 | 0.133208602666855 | 0.323321859912389 | 5 |
| 40 | 40 | 0.540499150753021 | 0.410717592592593 | 0.179776132106781 | 0.44324686082908 | 5 |
| 45 | 45 | 0.344773709774017 | 0.537957516339869 | 0.23560619354248 | 0.687782326466973 | 5 |
| 50 | 50 | 0.509868443012238 | 0.409348039215686 | 0.230870366096497 | 0.697406354251928 | 5 |
| 55 | 55 | 0.449314802885056 | 0.289470588235294 | 0.177790582180023 | 0.766980165541829 | 5 |
| 60 | 60 | 0.37868058681488 | 0.475367647058824 | 0.197842329740524 | 0.569873381327187 | 5 |
| 65 | 65 | 0.493949115276337 | 0.465071895424837 | 0.208534315228462 | 0.522521027170691 | 5 |
| 70 | 70 | 0.62637197971344 | 0.365218954248366 | 0.16659939289093 | 0.838212749555568 | 5 |
| 75 | 75 | 0.432880491018295 | 0.449880174291939 | 0.243199601769447 | 0.734811158748699 | 5 |
| 80 | 80 | 0.363442540168762 | 0.484093409586057 | 0.222477674484253 | 0.424747842554566 | 5 |
| 85 | 85 | 0.247009813785553 | 0.552581154684096 | 0.203489944338799 | 0.454965285627375 | 5 |
| 90 | 90 | 0.386023432016373 | 0.574195806100218 | 0.217422112822533 | 0.506995279921573 | 5 |
| 95 | 95 | 0.246710777282715 | 0.549674019607843 | 0.208980947732925 | 0.616113340023001 | 5 |
| 100 | 100 | 0.488438189029694 | 0.493900054466231 | 0.285525321960449 | 0.831454087130507 | 5 |
| 105 | 105 | 0 | 0 | 0.488438189029694 | 0.711046250819028 | 5 |
| 110 | 110 | 0 | 0 | 0 | 0 | 5 |


## Record 10 — H23: whole_song_reproduction_check

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | a29126a3563810b06a19f52e1f910077a3b36e5977f8dc17c9810ff644f2ee36 |
| started_utc | 2026-09-10T06:25:36.479713+00:00 |
| completed_utc | 2026-09-10T06:25:44.570069+00:00 |
| source_id | 1P75Wv4Qu1W_R6lmZRs0fGmv4VOxoXcmG |
| character | HIRO |
| alias | H23 |
| label | whole_song_reproduction_check |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「ミラクルナナウ(ﾟ∀ﾟ)！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| filename | 4K HDR「ミラクルナナウ(ﾟ∀ﾟ)！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| size_bytes | 44918957 |
| sha256 | 6761642adfb3ba089aa286cb147002decc2151e1b30471910afbef84946d9db6 |
| start_s | 0 |
| end_s | 116.657052 |
| duration_s | 116.657052 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 6761642adfb3ba089aa286cb147002decc2151e1b30471910afbef84946d9db6 |
| source_id | 1P75Wv4Qu1W_R6lmZRs0fGmv4VOxoXcmG |
| character | HIRO |
| alias | H23 |
| label | whole_song_reproduction_check |
| boundary_note | N/A |
| parameters.method_version | 2026-09-10-v1 |
| parameters.audio_sr_hz | 22050 |
| parameters.nfft | 2048 |
| parameters.hop | 512 |
| parameters.fft_window | periodic Hann |
| parameters.custom_spectral_center | false |
| parameters.rms_percentile_method | linear |
| parameters.rms_floor | 1e-12 |
| parameters.flatness_power_floor | 1e-10 |
| parameters.cv_ddof | 0 |
| parameters.audio_stream | first (0:a:0) |
| parameters.audio_signal | full unseparated mix, mono for features; native channels for R128 |
| parameters.trim_order | decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim |
| parameters.loudness_filter | ebur128=peak=true |
| parameters.silence_filter | silencedetect=noise=-50dB:d=0.5 |
| parameters.start_s | 0 |
| parameters.end_s | N/A |
| parameters.music | true |
| parameters.visual_step_s | 5 |
| parameters.skip_visual | false |
| parameters.visual_size[0] | 160 |
| parameters.visual_size[1] | 90 |
| parameters.visual_resize | INTER_AREA, whole frame with aspect distortion |
| parameters.visual_grayscale | OpenCV BGR2GRAY /255 |
| parameters.visual_saturation | OpenCV HSV S/255 |
| parameters.histogram | 8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5 |
| parameters.ffmpeg_threads | 1 |
| parameters.music_parameters.onset | librosa onset_strength; center=True; aggregate=mean |
| parameters.music_parameters.beat | start_bpm120, tightness100, trim=True |
| parameters.music_parameters.local_tempo | start_bpm120,std_bpm1,ac_size8,max_tempo320,aggregate=None |
| parameters.music_parameters.chroma | chroma_stft,tuning0,norm1,center=True |
| parameters.music_parameters.tonnetz | 6D coordinates from chroma_stft, adjacent Euclidean distance |
| software.python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| software.platform | Windows-11-10.0.26200-SP0 |
| software.numpy | 2.1.2 |
| software.ffmpeg_command | ffmpeg |
| software.ffprobe_command | ffprobe |
| software.ffmpeg_version | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101<br><br>Exiting with exit code 0 |
| software.ffprobe_version | ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101 |
| software.opencv | 4.13.0 |
| software.librosa | 1.0.0 |
| software.scipy | 1.18.0 |
| script_sha256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


### Source probe

| Probe field | Value |
| --- | --- |
| streams[0].index | 0 |
| streams[0].codec_name | h264 |
| streams[0].codec_long_name | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 |
| streams[0].profile | High |
| streams[0].codec_type | video |
| streams[0].codec_tag_string | avc1 |
| streams[0].codec_tag | 0x31637661 |
| streams[0].mime_codec_string | avc1.640020 |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
| streams[0].pix_fmt | yuv420p |
| streams[0].level | 32 |
| streams[0].color_range | tv |
| streams[0].color_space | bt709 |
| streams[0].color_transfer | bt709 |
| streams[0].color_primaries | bt709 |
| streams[0].chroma_location | left |
| streams[0].field_order | progressive |
| streams[0].is_avc | true |
| streams[0].nal_length_size | 4 |
| streams[0].id | 0x1 |
| streams[0].r_frame_rate | 60/1 |
| streams[0].avg_frame_rate | 60/1 |
| streams[0].time_base | 1/15360 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 1790976 |
| streams[0].duration | 116.600000 |
| streams[0].bit_rate | 2885180 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 6996 |
| streams[0].extradata_size | 43 |
| streams[0].disposition.default | 1 |
| streams[0].disposition.dub | 0 |
| streams[0].disposition.original | 0 |
| streams[0].disposition.comment | 0 |
| streams[0].disposition.lyrics | 0 |
| streams[0].disposition.karaoke | 0 |
| streams[0].disposition.forced | 0 |
| streams[0].disposition.hearing_impaired | 0 |
| streams[0].disposition.visual_impaired | 0 |
| streams[0].disposition.clean_effects | 0 |
| streams[0].disposition.attached_pic | 0 |
| streams[0].disposition.timed_thumbnails | 0 |
| streams[0].disposition.non_diegetic | 0 |
| streams[0].disposition.captions | 0 |
| streams[0].disposition.descriptions | 0 |
| streams[0].disposition.metadata | 0 |
| streams[0].disposition.dependent | 0 |
| streams[0].disposition.still_image | 0 |
| streams[0].disposition.multilayer | 0 |
| streams[0].tags.language | und |
| streams[0].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[0].side_data_list[0].side_data_type | Content light level metadata |
| streams[0].side_data_list[0].max_content | 1000 |
| streams[0].side_data_list[0].max_average | 200 |
| streams[1].index | 1 |
| streams[1].codec_name | aac |
| streams[1].codec_long_name | AAC (Advanced Audio Coding) |
| streams[1].profile | LC |
| streams[1].codec_type | audio |
| streams[1].codec_tag_string | mp4a |
| streams[1].codec_tag | 0x6134706d |
| streams[1].mime_codec_string | mp4a.40.2 |
| streams[1].sample_fmt | fltp |
| streams[1].sample_rate | 44100 |
| streams[1].channels | 2 |
| streams[1].channel_layout | stereo |
| streams[1].bits_per_sample | 0 |
| streams[1].initial_padding | 0 |
| streams[1].id | 0x2 |
| streams[1].r_frame_rate | 0/0 |
| streams[1].avg_frame_rate | 0/0 |
| streams[1].time_base | 1/44100 |
| streams[1].start_pts | 0 |
| streams[1].start_time | 0.000000 |
| streams[1].duration_ts | 5144576 |
| streams[1].duration | 116.657052 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 5024 |
| streams[1].extradata_size | 16 |
| streams[1].disposition.default | 1 |
| streams[1].disposition.dub | 0 |
| streams[1].disposition.original | 0 |
| streams[1].disposition.comment | 0 |
| streams[1].disposition.lyrics | 0 |
| streams[1].disposition.karaoke | 0 |
| streams[1].disposition.forced | 0 |
| streams[1].disposition.hearing_impaired | 0 |
| streams[1].disposition.visual_impaired | 0 |
| streams[1].disposition.clean_effects | 0 |
| streams[1].disposition.attached_pic | 0 |
| streams[1].disposition.timed_thumbnails | 0 |
| streams[1].disposition.non_diegetic | 0 |
| streams[1].disposition.captions | 0 |
| streams[1].disposition.descriptions | 0 |
| streams[1].disposition.metadata | 0 |
| streams[1].disposition.dependent | 0 |
| streams[1].disposition.still_image | 0 |
| streams[1].disposition.multilayer | 0 |
| streams[1].tags.language | jpn |
| streams[1].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[2].index | 2 |
| streams[2].codec_name | png |
| streams[2].codec_long_name | PNG (Portable Network Graphics) image |
| streams[2].codec_type | video |
| streams[2].codec_tag_string | [0][0][0][0] |
| streams[2].codec_tag | 0x0000 |
| streams[2].width | 1280 |
| streams[2].height | 720 |
| streams[2].coded_width | 1280 |
| streams[2].coded_height | 720 |
| streams[2].has_b_frames | 0 |
| streams[2].pix_fmt | rgb24 |
| streams[2].level | -99 |
| streams[2].color_range | pc |
| streams[2].color_space | gbr |
| streams[2].id | 0x0 |
| streams[2].r_frame_rate | 90000/1 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/90000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 10499135 |
| streams[2].duration | 116.657056 |
| streams[2].disposition.default | 0 |
| streams[2].disposition.dub | 0 |
| streams[2].disposition.original | 0 |
| streams[2].disposition.comment | 0 |
| streams[2].disposition.lyrics | 0 |
| streams[2].disposition.karaoke | 0 |
| streams[2].disposition.forced | 0 |
| streams[2].disposition.hearing_impaired | 0 |
| streams[2].disposition.visual_impaired | 0 |
| streams[2].disposition.clean_effects | 0 |
| streams[2].disposition.attached_pic | 1 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| chapters | [] |
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「ミラクルナナウ(ﾟ∀ﾟ)！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 116.657052 |
| format.size | 44918957 |
| format.bit_rate | 3080410 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 4K HDR「ミラクルナナウ(ﾟ∀ﾟ)！」 (篠澤広 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】 |
| format.tags.artist | 十六夜カズヤP / 16KazuyaP |
| format.tags.genre | Gaming |
| format.tags.date | 20250908 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=V3cPA2Sa8T4 |
| format.tags.description | 「ミラクルナナウ(ﾟ∀ﾟ)！」 (#篠澤広  SSR) 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm45383286<br><br>作詞・作曲・編曲：YUC'e<br>歌：篠澤広 (CV. 川村玲奈)<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |
| format.tags.synopsis | 「ミラクルナナウ(ﾟ∀ﾟ)！」 (#篠澤広  SSR) 4K #HDR 60fps<br>https://www.nicovideo.jp/watch/sm45383286<br><br>作詞・作曲・編曲：YUC'e<br>歌：篠澤広 (CV. 川村玲奈)<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 2572288 |
| analyzed_audio_duration_s | 116.657052154195 |
| stft_frames | 5021 |
| flux_transitions | 5020 |
| rms_linear | 0.175061698147749 |
| rms_p10_linear | 7.37756150278584e-12 |
| rms_p90_linear | 0.263534618656358 |
| rms_p90_p10_db | 211.058496695705 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | true |
| rms_frames_below_1e_minus8 | 503 |
| centroid_hz_mean | 3029.11715119712 |
| flatness_mean | 0.170948281397704 |
| positive_normalized_flux_mean | 0.022957527459082 |
| flux_cv | 0.589226878127598 |
| tempo_bpm | 117.453835227273 |
| beat_count | 199 |
| beat_interval_count | 198 |
| beat_interval_cv | 0.0477612482638053 |
| local_tempo_count | 5025 |
| local_tempo_cv | 0.250775712435991 |
| chroma_frames | 5025 |
| chroma_entropy_bits_mean | 2.78012156486511 |
| tonnetz_transition_count | 5024 |
| tonnetz_motion_mean | 0.141968576454606 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -13.3 |
| lra_lu | 5.2 |
| true_peak_dbfs | 0 |
| silence_seconds | 16.561406 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -13.3 LUFS<br>    Threshold: -23.7 LUFS<br><br>  Loudness range:<br>    LRA:         5.2 LU<br>    Threshold: -33.8 LUFS<br>    LRA low:   -15.9 LUFS<br>    LRA high:  -10.7 LUFS<br><br>  True peak:<br>    Peak:        0.0 dBFS<br>[out#0/null @ 000001a64caa8400] video:0KiB audio:20096KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:01:56.65 bitrate=N/A speed=75.3x elapsed=0:00:01.54 |
| ffmpeg_stderr_sha256 | 2231af9ecdfb2009f0a151d32e3f1ba27ac87c81b2f9579202925c35c45ce27c |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 0.101859 | 0.611043 | 0.509184 | 0.509184 |
| 2.107596 | 6.002585 | 3.894989 | 3.894989 |
| 104.499819 | 116.657052 | 12.157233 | 12.157234 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 24 |
| samples | 24 |
| brightness_mean | 0.439929566035668 |
| saturation_mean | 0.36827269426289 |
| frame_difference_mean | 0.214205447260452 |
| histogram_jumps_gt_0_5 | 21 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.134962156414986 | 0.474588235294118 | N/A | N/A | N/A |
| 5 | 5 | 0.28578132390976 | 0.459544389978214 | 0.153575167059898 | 0.466642200500155 | 5 |
| 10 | 10 | 0.638856172561646 | 0.160322984749455 | 0.539662599563599 | 0.718489294776028 | 5 |
| 15 | 15 | 0.543754875659943 | 0.320472222222222 | 0.132092580199242 | 0.703370565243877 | 5 |
| 20 | 20 | 0.611724436283112 | 0.333049836601307 | 0.102970041334629 | 0.503104908410343 | 5 |
| 25 | 25 | 0.527108371257782 | 0.317129357298475 | 0.156355112791061 | 0.588195520454901 | 5 |
| 30 | 30 | 0.268726319074631 | 0.613946078431373 | 0.315624445676804 | 0.555566875544716 | 5 |
| 35 | 35 | 0.320915311574936 | 0.414714052287582 | 0.188549026846886 | 0.494033290255612 | 5 |
| 40 | 40 | 0.482933014631271 | 0.379433551198257 | 0.284422397613525 | 0.550209930412381 | 5 |
| 45 | 45 | 0.425912022590637 | 0.435039215686275 | 0.288881570100784 | 0.553132899353969 | 5 |
| 50 | 50 | 0.473761439323425 | 0.446365740740741 | 0.234458342194557 | 0.508790208108297 | 5 |
| 55 | 55 | 0.580158233642578 | 0.444505174291939 | 0.172054201364517 | 0.708057026904173 | 5 |
| 60 | 60 | 0.589330673217773 | 0.282206154684096 | 0.0557644329965115 | 0.821884562996671 | 5 |
| 65 | 65 | 0.554403364658356 | 0.281241830065359 | 0.13293382525444 | 0.68119198958419 | 5 |
| 70 | 70 | 0.617335259914398 | 0.422127450980392 | 0.138159587979317 | 0.601833226185957 | 5 |
| 75 | 75 | 0.456442803144455 | 0.38197848583878 | 0.188145697116852 | 0.756903128459743 | 5 |
| 80 | 80 | 0.508625566959381 | 0.286945806100218 | 0.195988297462463 | 0.528456757178644 | 5 |
| 85 | 85 | 0.535032987594604 | 0.343300381263617 | 0.138363286852837 | 0.55925114278148 | 5 |
| 90 | 90 | 0.601049304008484 | 0.41026334422658 | 0.116602391004562 | 0.538248282400339 | 5 |
| 95 | 95 | 0.407315939664841 | 0.34982325708061 | 0.217209964990616 | 0.655009349904158 | 5 |
| 100 | 100 | 0.53479790687561 | 0.323394607843137 | 0.197152510285378 | 0.650339397562367 | 5 |
| 105 | 105 | 0.132088527083397 | 0.574039760348584 | 0.409619003534317 | 0.722273592150576 | 5 |
| 110 | 110 | 0.327293574810028 | 0.384112745098039 | 0.240847229957581 | 0.50897116625422 | 5 |
| 115 | 115 | 0 | 0 | 0.327293574810028 | 0.705341212694394 | 5 |


## Record 11 — H25: whole_song_reproduction_check

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 04c7b5f89c2c51be4e5c3ab4265ce4b1eac312ddaa52a7052a9926b470463410 |
| started_utc | 2026-09-10T06:25:43.659447+00:00 |
| completed_utc | 2026-09-10T06:25:51.603510+00:00 |
| source_id | 1K9In8GKh9pP041E6A0zg3hyX-lKdug7G |
| character | HIRO |
| alias | H25 |
| label | whole_song_reproduction_check |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「ENDLESS DANCE」(篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| filename | 4K HDR「ENDLESS DANCE」(篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| size_bytes | 44652220 |
| sha256 | 2599c7b4d83b267a76204cd8a463f47f2ebf2bcf995d7305be7b74b311d2f855 |
| start_s | 0 |
| end_s | 109.435646 |
| duration_s | 109.435646 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 2599c7b4d83b267a76204cd8a463f47f2ebf2bcf995d7305be7b74b311d2f855 |
| source_id | 1K9In8GKh9pP041E6A0zg3hyX-lKdug7G |
| character | HIRO |
| alias | H25 |
| label | whole_song_reproduction_check |
| boundary_note | N/A |
| parameters.method_version | 2026-09-10-v1 |
| parameters.audio_sr_hz | 22050 |
| parameters.nfft | 2048 |
| parameters.hop | 512 |
| parameters.fft_window | periodic Hann |
| parameters.custom_spectral_center | false |
| parameters.rms_percentile_method | linear |
| parameters.rms_floor | 1e-12 |
| parameters.flatness_power_floor | 1e-10 |
| parameters.cv_ddof | 0 |
| parameters.audio_stream | first (0:a:0) |
| parameters.audio_signal | full unseparated mix, mono for features; native channels for R128 |
| parameters.trim_order | decoded PCM timestamps reset; atrim before feature filters/resampling; reset after trim |
| parameters.loudness_filter | ebur128=peak=true |
| parameters.silence_filter | silencedetect=noise=-50dB:d=0.5 |
| parameters.start_s | 0 |
| parameters.end_s | N/A |
| parameters.music | true |
| parameters.visual_step_s | 5 |
| parameters.skip_visual | false |
| parameters.visual_size[0] | 160 |
| parameters.visual_size[1] | 90 |
| parameters.visual_resize | INTER_AREA, whole frame with aspect distortion |
| parameters.visual_grayscale | OpenCV BGR2GRAY /255 |
| parameters.visual_saturation | OpenCV HSV S/255 |
| parameters.histogram | 8x8x8 BGR, L1 norm, Bhattacharyya distance >0.5 |
| parameters.ffmpeg_threads | 1 |
| parameters.music_parameters.onset | librosa onset_strength; center=True; aggregate=mean |
| parameters.music_parameters.beat | start_bpm120, tightness100, trim=True |
| parameters.music_parameters.local_tempo | start_bpm120,std_bpm1,ac_size8,max_tempo320,aggregate=None |
| parameters.music_parameters.chroma | chroma_stft,tuning0,norm1,center=True |
| parameters.music_parameters.tonnetz | 6D coordinates from chroma_stft, adjacent Euclidean distance |
| software.python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| software.platform | Windows-11-10.0.26200-SP0 |
| software.numpy | 2.1.2 |
| software.ffmpeg_command | ffmpeg |
| software.ffprobe_command | ffprobe |
| software.ffmpeg_version | ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101<br><br>Exiting with exit code 0 |
| software.ffprobe_version | ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers<br>built with gcc 15.2.0 (Rev13, Built by MSYS2 project)<br>configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-cairo --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-zlib --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-sdl2 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libaom --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-openal --enable-libgme --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libtheora --enable-libvo-amrwbenc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-librubberband<br>libavutil      60. 26.101 / 60. 26.101<br>libavcodec     62. 28.101 / 62. 28.101<br>libavformat    62. 12.101 / 62. 12.101<br>libavdevice    62.  3.101 / 62.  3.101<br>libavfilter    11. 14.101 / 11. 14.101<br>libswscale      9.  5.101 /  9.  5.101<br>libswresample   6.  3.101 /  6.  3.101 |
| software.opencv | 4.13.0 |
| software.librosa | 1.0.0 |
| software.scipy | 1.18.0 |
| script_sha256 | 576c0780c4ea23b033b02395e6b325fb6dfe078ef95045255ac5058f7b20dbf7 |


### Source probe

| Probe field | Value |
| --- | --- |
| streams[0].index | 0 |
| streams[0].codec_name | h264 |
| streams[0].codec_long_name | H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10 |
| streams[0].profile | High |
| streams[0].codec_type | video |
| streams[0].codec_tag_string | avc1 |
| streams[0].codec_tag | 0x31637661 |
| streams[0].mime_codec_string | avc1.640020 |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
| streams[0].pix_fmt | yuv420p |
| streams[0].level | 32 |
| streams[0].color_range | tv |
| streams[0].color_space | bt709 |
| streams[0].color_transfer | bt709 |
| streams[0].color_primaries | bt709 |
| streams[0].chroma_location | left |
| streams[0].field_order | progressive |
| streams[0].is_avc | true |
| streams[0].nal_length_size | 4 |
| streams[0].id | 0x1 |
| streams[0].r_frame_rate | 60/1 |
| streams[0].avg_frame_rate | 60/1 |
| streams[0].time_base | 1/15360 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 1679872 |
| streams[0].duration | 109.366667 |
| streams[0].bit_rate | 3034304 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 6562 |
| streams[0].extradata_size | 43 |
| streams[0].disposition.default | 1 |
| streams[0].disposition.dub | 0 |
| streams[0].disposition.original | 0 |
| streams[0].disposition.comment | 0 |
| streams[0].disposition.lyrics | 0 |
| streams[0].disposition.karaoke | 0 |
| streams[0].disposition.forced | 0 |
| streams[0].disposition.hearing_impaired | 0 |
| streams[0].disposition.visual_impaired | 0 |
| streams[0].disposition.clean_effects | 0 |
| streams[0].disposition.attached_pic | 0 |
| streams[0].disposition.timed_thumbnails | 0 |
| streams[0].disposition.non_diegetic | 0 |
| streams[0].disposition.captions | 0 |
| streams[0].disposition.descriptions | 0 |
| streams[0].disposition.metadata | 0 |
| streams[0].disposition.dependent | 0 |
| streams[0].disposition.still_image | 0 |
| streams[0].disposition.multilayer | 0 |
| streams[0].tags.language | und |
| streams[0].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[0].side_data_list[0].side_data_type | Content light level metadata |
| streams[0].side_data_list[0].max_content | 1000 |
| streams[0].side_data_list[0].max_average | 200 |
| streams[1].index | 1 |
| streams[1].codec_name | aac |
| streams[1].codec_long_name | AAC (Advanced Audio Coding) |
| streams[1].profile | LC |
| streams[1].codec_type | audio |
| streams[1].codec_tag_string | mp4a |
| streams[1].codec_tag | 0x6134706d |
| streams[1].mime_codec_string | mp4a.40.2 |
| streams[1].sample_fmt | fltp |
| streams[1].sample_rate | 44100 |
| streams[1].channels | 2 |
| streams[1].channel_layout | stereo |
| streams[1].bits_per_sample | 0 |
| streams[1].initial_padding | 0 |
| streams[1].id | 0x2 |
| streams[1].r_frame_rate | 0/0 |
| streams[1].avg_frame_rate | 0/0 |
| streams[1].time_base | 1/44100 |
| streams[1].start_pts | 0 |
| streams[1].start_time | 0.000000 |
| streams[1].duration_ts | 4826112 |
| streams[1].duration | 109.435646 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 4713 |
| streams[1].extradata_size | 16 |
| streams[1].disposition.default | 1 |
| streams[1].disposition.dub | 0 |
| streams[1].disposition.original | 0 |
| streams[1].disposition.comment | 0 |
| streams[1].disposition.lyrics | 0 |
| streams[1].disposition.karaoke | 0 |
| streams[1].disposition.forced | 0 |
| streams[1].disposition.hearing_impaired | 0 |
| streams[1].disposition.visual_impaired | 0 |
| streams[1].disposition.clean_effects | 0 |
| streams[1].disposition.attached_pic | 0 |
| streams[1].disposition.timed_thumbnails | 0 |
| streams[1].disposition.non_diegetic | 0 |
| streams[1].disposition.captions | 0 |
| streams[1].disposition.descriptions | 0 |
| streams[1].disposition.metadata | 0 |
| streams[1].disposition.dependent | 0 |
| streams[1].disposition.still_image | 0 |
| streams[1].disposition.multilayer | 0 |
| streams[1].tags.language | jpn |
| streams[1].tags.handler_name | ISO Media file produced by Google Inc. |
| streams[2].index | 2 |
| streams[2].codec_name | png |
| streams[2].codec_long_name | PNG (Portable Network Graphics) image |
| streams[2].codec_type | video |
| streams[2].codec_tag_string | [0][0][0][0] |
| streams[2].codec_tag | 0x0000 |
| streams[2].width | 1280 |
| streams[2].height | 720 |
| streams[2].coded_width | 1280 |
| streams[2].coded_height | 720 |
| streams[2].has_b_frames | 0 |
| streams[2].pix_fmt | rgb24 |
| streams[2].level | -99 |
| streams[2].color_range | pc |
| streams[2].color_space | gbr |
| streams[2].id | 0x0 |
| streams[2].r_frame_rate | 90000/1 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/90000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 9849208 |
| streams[2].duration | 109.435644 |
| streams[2].disposition.default | 0 |
| streams[2].disposition.dub | 0 |
| streams[2].disposition.original | 0 |
| streams[2].disposition.comment | 0 |
| streams[2].disposition.lyrics | 0 |
| streams[2].disposition.karaoke | 0 |
| streams[2].disposition.forced | 0 |
| streams[2].disposition.hearing_impaired | 0 |
| streams[2].disposition.visual_impaired | 0 |
| streams[2].disposition.clean_effects | 0 |
| streams[2].disposition.attached_pic | 1 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| chapters | [] |
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\07_SHINOSAWA_HIRO\04_MV_3DMV_AND_PERFORMANCE\4K HDR「ENDLESS DANCE」(篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 109.435646 |
| format.size | 44652220 |
| format.bit_rate | 3264181 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 4K HDR「ENDLESS DANCE」(篠澤広 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】 |
| format.tags.artist | 十六夜カズヤP / 16KazuyaP |
| format.tags.genre | Gaming |
| format.tags.date | 20260227 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=lKA4swUcuNE |
| format.tags.description | 「ENDLESS DANCE」(#篠澤広  SSR) 4K HDR 60fps<br>https://www.nicovideo.jp/watch/sm46000445<br><br>作詞・作曲：首藤義勝<br>編曲：藤永龍太郎(Elements Garden)<br>歌：篠澤広 (CV. 川村玲奈)<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |
| format.tags.synopsis | 「ENDLESS DANCE」(#篠澤広  SSR) 4K HDR 60fps<br>https://www.nicovideo.jp/watch/sm46000445<br><br>作詞・作曲：首藤義勝<br>編曲：藤永龍太郎(Elements Garden)<br>歌：篠澤広 (CV. 川村玲奈)<br><br>ゲーム内レコード:<br>アイドルマスター #学園アイドルマスター #学マス #アイマス<br>recorded from game:<br>Gakuen iDOLM@STER<br>https://gakuen.idolmaster-official.jp/<br>#偶像大師 学園偶像大師 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 2413056 |
| analyzed_audio_duration_s | 109.435646258503 |
| stft_frames | 4710 |
| flux_transitions | 4709 |
| rms_linear | 0.220781423836353 |
| rms_p10_linear | 0.000139161054284965 |
| rms_p90_linear | 0.297620652217413 |
| rms_p90_p10_db | 66.6029070755097 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 442 |
| centroid_hz_mean | 2618.43000955922 |
| flatness_mean | 0.143633225097308 |
| positive_normalized_flux_mean | 0.0207616964291769 |
| flux_cv | 0.517910366724691 |
| tempo_bpm | 151.999080882353 |
| beat_count | 241 |
| beat_interval_count | 240 |
| beat_interval_cv | 0.0235282765150912 |
| local_tempo_count | 4714 |
| local_tempo_cv | 0.210185844012723 |
| chroma_frames | 4714 |
| chroma_entropy_bits_mean | 2.94575691223145 |
| tonnetz_transition_count | 4713 |
| tonnetz_motion_mean | 0.106234502993197 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -11.6 |
| lra_lu | 2.2 |
| true_peak_dbfs | -0.2 |
| silence_seconds | 12.773583 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -11.6 LUFS<br>    Threshold: -21.8 LUFS<br><br>  Loudness range:<br>    LRA:         2.2 LU<br>    Threshold: -31.9 LUFS<br>    LRA low:   -12.8 LUFS<br>    LRA high:  -10.6 LUFS<br><br>  True peak:<br>    Peak:       -0.2 dBFS<br>[out#0/null @ 000001cf7c0cbec0] video:0KiB audio:18852KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:01:49.43 bitrate=N/A speed= 119x elapsed=0:00:00.91 |
| ffmpeg_stderr_sha256 | 55f1a11c03fb49e39beef3dc736802e578183badd42018f4b1a2294ad3b4a315 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 0 | 0.564172 | 0.564172 | 0.564172 |
| 2.105215 | 6.959615 | 4.8544 | 4.854399 |
| 102.080635 | 109.435646 | 7.355011 | 7.355011 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 22 |
| samples | 22 |
| brightness_mean | 0.170975287938213 |
| saturation_mean | 0.490925009902951 |
| frame_difference_mean | 0.17034180781671 |
| histogram_jumps_gt_0_5 | 16 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.132792755961418 | 0.496854575163399 | N/A | N/A | N/A |
| 5 | 5 | 0.279151976108551 | 0.467362472766885 | 0.149285688996315 | 0.463736362905035 | 5 |
| 10 | 10 | 0.0803341493010521 | 0.521775326797386 | 0.25381726026535 | 0.622858870969645 | 5 |
| 15 | 15 | 0.194401428103447 | 0.585791666666667 | 0.155296042561531 | 0.663691276262822 | 5 |
| 20 | 20 | 0.175822451710701 | 0.216782135076253 | 0.199260354042053 | 0.737565524915262 | 5 |
| 25 | 25 | 0.0878570377826691 | 0.548221949891068 | 0.131556376814842 | 0.378378968206682 | 5 |
| 30 | 30 | 0.184014722704887 | 0.443136710239651 | 0.156681656837463 | 0.349550431754158 | 5 |
| 35 | 35 | 0.156531885266304 | 0.675440631808279 | 0.172304213047028 | 0.772781648298618 | 5 |
| 40 | 40 | 0.177921578288078 | 0.432464324618736 | 0.19268710911274 | 0.774018643780144 | 5 |
| 45 | 45 | 0.134335801005363 | 0.700891067538126 | 0.18263153731823 | 0.743451570411826 | 5 |
| 50 | 50 | 0.115641891956329 | 0.717605664488017 | 0.108715139329433 | 0.440440811243107 | 5 |
| 55 | 55 | 0.15520615875721 | 0.424243464052288 | 0.1522516310215 | 0.461070422609633 | 5 |
| 60 | 60 | 0.197010636329651 | 0.453390795206972 | 0.150124177336693 | 0.717849293601773 | 5 |
| 65 | 65 | 0.205279961228371 | 0.380192265795207 | 0.147462695837021 | 0.590888381899162 | 5 |
| 70 | 70 | 0.427209943532944 | 0.35393082788671 | 0.271961063146591 | 0.758061442717768 | 5 |
| 75 | 75 | 0.284387826919556 | 0.550985838779956 | 0.2351925522089 | 0.608410135818421 | 5 |
| 80 | 80 | 0.170913949608803 | 0.685032135076253 | 0.162083879113197 | 0.567535028239902 | 5 |
| 85 | 85 | 0.164046853780746 | 0.672429466230937 | 0.151203691959381 | 0.738052543796901 | 5 |
| 90 | 90 | 0.171849936246872 | 0.565160130718954 | 0.168103769421577 | 0.603288370213721 | 5 |
| 95 | 95 | 0.10436874628067 | 0.666347494553377 | 0.147258460521698 | 0.513132327243775 | 5 |
| 100 | 100 | 0.162375554442406 | 0.242033496732026 | 0.126926198601723 | 0.714923648468857 | 5 |
| 105 | 105 | 1.08932465536782e-06 | 0.000277777777777778 | 0.162374466657639 | 0.59404632720309 | 5 |



