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

# MISUZU technical measurements — current Windows execution

This supplement records work actually executed during the authorized rebuild. Incoming ZIP calculations remain separately labeled in the existing supporting tables, even though both generations bear the date 2026-09-10. Current automated calculations do not establish direct listening, continuous watching, speaker-isolated properties or narrative interpretation. Exact inputs are linked to [current source verification](EXECUTION_SOURCE_VERIFICATION.md).

Current scope in this package: **21 result records; 1,892 scheduled visual samples, 1,892 successful reads, zero omitted reads**. The independent data audit covered all 32 current records across both characters, checked actual input hashes, parameter/cache fingerprints, interval bounds, decoded sample/STFT counts, RMS ratios, silence sums and per-sample visual reductions, and found zero discrepancies in those checks. This data audit is distinct from the final document/package audit.

The 21 current results are a hash-matched M03 whole-source reproduction check and 20 newly bounded chapter-associated intervals: Dear001–010 from M01 and Dear028–037 from M04. Dear011–027 retain 17 incoming measurements on now hash-matched inputs. Thus 37 chapter-associated intervals have documented mixed-source descriptors, with their two calculation generations and boundary methods kept explicit. New intervals were not obtained by equally dividing compilations.

The character reviewer established the new bounds from the first clearly legible chapter-label reference frames in 30-fps sources, inspected on adjacent-frame header sheets. Crossfades make semantic chapter onset ambiguous over a few frames: the frame numbers specify repeatable operational bounds, not original-game narrative boundaries with 1/30-second certainty. Transition frames before the next reference onset remain in the previous interval; the final interval ends at the documented label disappearance before the uploader ending. Exact bounds and evidence locators are copied into each result below. See [chapter review and frame evidence](EXECUTION_EXTENSION_20260910.md) and [all chapter-associated summary rows](DEAR_SEGMENT_MEASUREMENTS.md).

M03 container duration is 2835.0 seconds, but its first audio stream ends at 2834.529523809524 seconds. Audio sample duration correctly follows that stream; no synthetic tail silence was inserted to fill the container. This distinction also appears in the incoming audio sample count.

## Runtime, method and safeguards

The incoming methods document reports Python 3.12.14, FFmpeg/ffprobe 6.1.1-3ubuntu5, NumPy 2.5.3, SciPy 1.18.1, librosa 1.0.0 and OpenCV 5.0.0. These are historical recorded versions, not the current machine or a certified recreation of that environment. Current observed versions follow; full FFmpeg/ffprobe build output is retained in each result’s processing identity.

| Runtime field | Current observed value |
| --- | --- |
| python | 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] |
| platform | Windows-11-10.0.26200-SP0 |
| numpy | 2.1.2 |
| opencv | 4.13.0 |
| librosa | Not invoked for these records |
| scipy | Not invoked for these records |
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
| M03 | loudness | silence_seconds | 139.95256 | 139.895460999999 | 0.0570990000006759 |
| M03 | visual | brightness_mean | 0.507414487514 | 0.50224276388974 | 0.00517172362425999 |
| M03 | visual | saturation_mean | 0.32480968327 | 0.325893834557142 | 0.00108415128714251 |
| M03 | visual | frame_difference_mean | 0.0717275789641 | 0.0720534660142201 | 0.000325887050120141 |


Every common numerical summary field not listed above agrees within the declared comparison tolerance. Audio sample counts, spectral/RMS descriptors and EBU R128 summaries reproduce for the hash-matched M03 source. Music-tracker features were not generated for this check.

| Alias | Incoming visual n | Current visual n | Same requested times | Max reported-time delta s | Max luma delta | At source s | Max saturation delta | At source s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M03 | 567 | 567 | true | 3.33375282934867e-09 | 0.0273167192935591 | 2770 | 0.0519411764701699 | 2770 |


| Alias | Incoming low-level interval n | Current interval n | Max start delta s | Max end delta s |
| --- | --- | --- | --- | --- |
| M03 | 113 | 113 | 0.0046709999999166 | 0.00498900000002322 |


Low-level detector endpoint precision differs between the recorded FFmpeg generations, especially for long timestamps. Corresponding endpoints are within 0.005 seconds in the H03/M03 checks. Totals in this report are sums of current end-minus-start intervals and are not forced to match totals produced from the incoming rounded logs. A source with zero detected intervals has no endpoint delta.

The current and incoming visual samples use identical requested source times; reported times also correspond to the precision shown. Pixel-derived results nonetheless differ. The current Windows/OpenCV runtime and the incoming Linux/OpenCV runtime are separate processing conditions. Exact cause has not been isolated. These differences cannot establish fine changes in acting, choreography, expression, lighting design, shot count or motion speed. The 5-second histogram threshold is a sparse image-change proxy; a value crossing 0.5 can change its count without constituting a newly established edit.

## Bounded decoder-discrepancy inspection

A separate auditor directly viewed one extracted current still at M03 source time 2770 seconds to investigate a maximum-luma discrepancy. Input SHA-256: `5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763`. A wide stage-performance image contains purple lighting and visible beams. This is a technical still-image check, not listening or continuous performance inspection. The same still was decoded with OpenCV default selection and explicit CAP_FFMPEG; both selected the FFMPEG backend and their maximum pixel difference was 0. Therefore merely selecting that backend explicitly does not explain the cross-generation difference. The incoming runtime was not recreated for pixel identity.

| Requested backend | Actual backend | Reported source s | Luma | Saturation |
| --- | --- | --- | --- | --- |
| 0 | FFMPEG | 2770.00056666667 | 0.346262812614441 | 0.66378022875817 |
| 1900 | FFMPEG | 2770.00056666667 | 0.346262812614441 | 0.66378022875817 |


## Near-zero RMS percentiles and threshold sensitivity

RMS P90/P10 is 20 log10(max(P90, ε)/max(P10, ε)) with ε = 10⁻¹². It summarizes complete 2048-sample windows of the entire mixed recording, including silent openings, music, effects and several speakers. It is not EBU LRA or an estimate of an individual performer’s expressive dynamic range. Where P10 is zero or nearly zero, the ratio mainly reflects the denominator and chosen numerical floor.

| Alias | Interval | P10 linear | P90 linear | 10^-12 floor applied | Frames below 10^-8 | Complete RMS frames | Reported ratio dB |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M01 | Dear001 | 0 | 0.137604523632285 | true | 1169 | 8643 | 222.772654223956 |


| Alias | Interval | Hypothetical denominator floor ε | Ratio dB under this floor |
| --- | --- | --- | --- |
| M01 | Dear001 | 1e-12 | 222.772654223956 |
| M01 | Dear001 | 1e-08 | 142.772654223956 |
| M01 | Dear001 | 1e-06 | 102.772654223956 |
| M01 | Dear001 | 0.0001 | 62.772654223956 |


This sensitivity table changes only the numerical floor applied to the already computed percentiles. It is an algebraic diagnostic, not a new signal extraction, accepted replacement estimator or calibrated perceptual measure. The large change demonstrates why near-zero-P10 ratios must not be read as expressive range. No cause is assigned to a specific audible event without separate audio review.

Silence detection is a separate threshold operation: amplitude below −50 dB for at least 0.5 seconds in the combined first audio stream. Changing this threshold or duration would change eligible intervals; this execution did not perform that signal-level threshold sweep. Reported detector intervals therefore cannot be equated with speaker pauses, hesitation, breath or absence of BGM.

## Result inventory and reproduction

| Alias | Label | Input SHA-256 | Working result JSON SHA-256 | Processing fingerprint |
| --- | --- | --- | --- | --- |
| M03 | whole_source_reproduction_check | 5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763 | 1ba82d205181e80588a1b3f6b33c0581560121c50901ea11e466f3ecae145a35 | d3e75a3ac55c7eefae39578d496a0463c4679a9acf8adde76d1b590f3f909126 |
| M01 | Dear001 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be | b4d043a5f4b8fa11a8a5449b2fe807e02f7741b17514b9da37ec03cb07990f3d | a06203131f76bb12597757e8906c5d7ae89f5661da5e9fcf01a99bfc6bdfb0e6 |
| M01 | Dear002 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be | cbd048807a6bd839f2e684c14cb2e3f4aed40effdfb4fc4936ff0b32d966e643 | 46b05bee3f2aaa8d6636c65d7632668ab8a66ac17be5cfd8c90dbc55b2675699 |
| M01 | Dear003 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be | e00b08dce3f9d809fb7447621bc55489ba202b85c392c4ebb0424f145444d7c2 | 759f4b66326a53a130e6a2929e84c4b5104f551aa39daf77285e8f600e643d92 |
| M01 | Dear004 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be | b70e25bdfbcd0e2b3a7ef5e4ed1536546ea6c796ac317f83030fb1b25dbd5a3d | 9f1984a1bedb7de1281cf333e3d2a42735d8c436cc2944daf0f075438eef1e6c |
| M01 | Dear005 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be | ff93ee6ae38cd40c153eb39eecb73e3d93c2e16bdc100ae5e35c92499b1d368d | b8c5eb05f630906055a277c072677627272db5a0959bcb7a21895ae996f82df9 |
| M01 | Dear006 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be | 4b73f95c1f84ce97fe045fe07b5ab9fd563c203ca6f54d909879912367a2934d | 5c8f7cff7155e7404f36e4739e86343f49704c9dc91319a33f2516a007425b7b |
| M01 | Dear007 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be | f965df351bb9891ef56f5767cdf4bfdb1546f56b2d9c330852b2e11a0c75f92f | cd2143022b70901634ca1512acfde9a884d1ec7a91ee54f082e05b655d7a13ee |
| M01 | Dear008 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be | 6171890e9fe9ba23bc0ee6c52329efea6b7d5f60ed26c3f1815fbfec96bd5ab3 | ef1336fa9c69ca5f4613ad0861a7b7334acdedd58084c12fd249a1e67330b08a |
| M01 | Dear009 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be | 7ff2e46fc9a28c92b701753be6a8a3b4eed1dc1916651a51f37996870bb9d5d6 | 971af2fbd1d7f3825b9f15415841cc2ec4f3d31461711a03811cb6e1783feab2 |
| M01 | Dear010 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be | 400dd1afd7baef6379145718fd0dcb3d9357b10ed14f9cce8dd1468f95023f61 | 47f35069062a812b111d6091f57b1edd183b3c01d229b5e1d57e6ff8a3f94958 |
| M04 | Dear028 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a | 2a588cf9a8fc78f9ee9ec89f5f91460d94eaff4ea3cbf8e58737449c120626fb | c002d590f8ce58cbb0efec477f241b58d0c28f7b002c21fa8f2629ff75d3faab |
| M04 | Dear029 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a | 365e29c937b81854b59c9dff43f576141ee18ea5e808f1804e6f95a17c873118 | e29df1b941b2a978afa62b6279b3ebb4ebee7aff1f1b94c674ef3bf9fec1638d |
| M04 | Dear030 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a | a411bddf9649deb4e1f7abf90c4ce0548b8bbef88c12f0c45f1e3ac8fdd303e7 | 58aebe208752d8a04836597c4675f96ab33c0adc5f5bf0f241a8ec12e5555d8d |
| M04 | Dear031 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a | 64fd827a8acd9cef569d3d4b94d1a68b56359f6a1b51bd687c79e9dc50936220 | 999b72a2e89e522050a74dc6a5262f1d784b818cc98b88805a309bd54fca0973 |
| M04 | Dear032 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a | 6a963ce00c894fbd80b1c536c5f858779bf491b92ebb46ffd28cd2c4dd3c2dbb | 8c294cbcf398c620a70622ee479a84a3a5e5ee01be68fb1d26be5bc4eaff1f10 |
| M04 | Dear033 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a | f1b5582131e2e28344cf5f9efd4d819aa6a1b4bca17c5de38092d0c149a168f6 | 61d4c9463058c008c32261af0f1f20a6635bb90cc04977e78b56febe09f8362f |
| M04 | Dear034 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a | ab8d7a927336d44b6629d6ac75bb5dd0a1ed4a96e6e82086bbda0274ba34965c | c8899cdcd50b359959465131717dc6a5a7c013aedeff28bd9bd5b87168bd48a9 |
| M04 | Dear035 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a | b31f421fb66636cb2ce0a266d887fd161b30839f44bf60f2a53aedab13980600 | ec28fc09a2a17093f1ffafbf494914132d861365cd5c4cbeade0c82463c3e592 |
| M04 | Dear036 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a | 9fa89064ea9b30e6eaa19ccaf67ba36282436119a8c7e8131e262cb31c5077c8 | 0a999ee74f41b66123d3ed37e951a3ec0608ee9c9cc10dbbed5c790b7ba5ed5f |
| M04 | Dear037 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a | 72bf0a33135fded01be4182b60a11fe0ffbbc876cfa41ebde80014c2b88bab40 | 97f78b70ad03cd7c99d2974e0f64be1304c6c1391891fd11a99452751125b6a0 |


The raw media, JSON results, Python environment and temporary frames remain outside the Markdown-only delivery. The complete result values and code are preserved below. To reproduce, save the Python block as `measure_current.py` with UTF-8 encoding, no BOM, LF line endings and one final newline; its SHA-256 must match the value above. Save the JSON block as `measurement_specs.json` outside the package and replace only each `path` with the location of that exact source hash. Install the recorded dependencies and provide the recorded FFmpeg tools. Then run the following command in that working directory. A changed runtime or script intentionally creates a different processing identity and must use a fresh result directory.

```text
python -X utf8 measure_current.py --specs measurement_specs.json --output-dir current-results --markdown current-results.md --workers 2
```

```json
[
  {
    "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
    "source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
    "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
    "character": "MISUZU",
    "alias": "M03",
    "label": "whole_source_reproduction_check",
    "start_s": 0.0,
    "end_s": null,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": null
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
    "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "character": "MISUZU",
    "alias": "M01",
    "label": "Dear001",
    "start_s": 1.1666666666666667,
    "end_s": 201.93333333333334,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 35 to 6058 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-001, frames/M01_frame_header_00.jpg, frames/M01_frame_header_01.jpg, adv_dear_hmsz_001.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
    "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "character": "MISUZU",
    "alias": "M01",
    "label": "Dear002",
    "start_s": 201.93333333333334,
    "end_s": 500.3666666666667,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 6058 to 15011 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-002, frames/M01_frame_header_01.jpg, frames/M01_frame_header_02.jpg, adv_dear_hmsz_002.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
    "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "character": "MISUZU",
    "alias": "M01",
    "label": "Dear003",
    "start_s": 500.3666666666667,
    "end_s": 739.2666666666667,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 15011 to 22178 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-003, frames/M01_frame_header_02.jpg, frames/M01_frame_header_03.jpg, adv_dear_hmsz_003.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
    "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "character": "MISUZU",
    "alias": "M01",
    "label": "Dear004",
    "start_s": 739.2666666666667,
    "end_s": 1006.7,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 22178 to 30201 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-004, frames/M01_frame_header_03.jpg, frames/M01_frame_header_04.jpg, adv_dear_hmsz_004.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
    "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "character": "MISUZU",
    "alias": "M01",
    "label": "Dear005",
    "start_s": 1006.7,
    "end_s": 1260.2666666666667,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 30201 to 37808 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-005, frames/M01_frame_header_04.jpg, frames/M01_frame_header_05.jpg, adv_dear_hmsz_005.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
    "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "character": "MISUZU",
    "alias": "M01",
    "label": "Dear006",
    "start_s": 1260.2666666666667,
    "end_s": 1548.2666666666667,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 37808 to 46448 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-006, frames/M01_frame_header_05.jpg, frames/M01_frame_header_06.jpg, adv_dear_hmsz_006.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
    "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "character": "MISUZU",
    "alias": "M01",
    "label": "Dear007",
    "start_s": 1548.2666666666667,
    "end_s": 1790.1333333333334,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 46448 to 53704 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-007, frames/M01_frame_header_06.jpg, frames/M01_frame_header_07.jpg, adv_dear_hmsz_007.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
    "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "character": "MISUZU",
    "alias": "M01",
    "label": "Dear008",
    "start_s": 1790.1333333333334,
    "end_s": 2092.8333333333335,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 53704 to 62785 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-008, frames/M01_frame_header_07.jpg, frames/M01_frame_header_08.jpg, adv_dear_hmsz_008.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
    "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "character": "MISUZU",
    "alias": "M01",
    "label": "Dear009",
    "start_s": 2092.8333333333335,
    "end_s": 2398.366666666667,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 62785 to 71951 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-009, frames/M01_frame_header_08.jpg, frames/M01_frame_header_09.jpg, adv_dear_hmsz_009.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
    "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "character": "MISUZU",
    "alias": "M01",
    "label": "Dear010",
    "start_s": 2398.366666666667,
    "end_s": 2753.2,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 71951 to 82596 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-010, frames/M01_frame_header_09.jpg, frames/M01_frame_header_10.jpg, adv_dear_hmsz_010.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
    "source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
    "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "character": "MISUZU",
    "alias": "M04",
    "label": "Dear028",
    "start_s": 0.9666666666666667,
    "end_s": 329.8,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 29 to 9894 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-028, frames/M04_frame_header_00.jpg, frames/M04_frame_header_01.jpg, adv_dear_hmsz_028.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
    "source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
    "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "character": "MISUZU",
    "alias": "M04",
    "label": "Dear029",
    "start_s": 329.8,
    "end_s": 723.5,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 9894 to 21705 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-029, frames/M04_frame_header_01.jpg, frames/M04_frame_header_02.jpg, adv_dear_hmsz_029.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
    "source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
    "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "character": "MISUZU",
    "alias": "M04",
    "label": "Dear030",
    "start_s": 723.5,
    "end_s": 1010.7333333333333,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 21705 to 30322 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-030, frames/M04_frame_header_02.jpg, frames/M04_frame_header_03.jpg, adv_dear_hmsz_030.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
    "source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
    "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "character": "MISUZU",
    "alias": "M04",
    "label": "Dear031",
    "start_s": 1010.7333333333333,
    "end_s": 1461.3333333333333,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 30322 to 43840 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-031, frames/M04_frame_header_03.jpg, frames/M04_frame_header_04.jpg, adv_dear_hmsz_031.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
    "source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
    "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "character": "MISUZU",
    "alias": "M04",
    "label": "Dear032",
    "start_s": 1461.3333333333333,
    "end_s": 1787.1333333333334,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 43840 to 53614 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-032, frames/M04_frame_header_04.jpg, frames/M04_frame_header_05.jpg, adv_dear_hmsz_032.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
    "source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
    "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "character": "MISUZU",
    "alias": "M04",
    "label": "Dear033",
    "start_s": 1787.1333333333334,
    "end_s": 2162.3333333333335,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 53614 to 64870 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-033, frames/M04_frame_header_05.jpg, frames/M04_frame_header_06.jpg, adv_dear_hmsz_033.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
    "source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
    "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "character": "MISUZU",
    "alias": "M04",
    "label": "Dear034",
    "start_s": 2162.3333333333335,
    "end_s": 2525.9,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 64870 to 75777 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-034, frames/M04_frame_header_06.jpg, frames/M04_frame_header_07.jpg, adv_dear_hmsz_034.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
    "source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
    "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "character": "MISUZU",
    "alias": "M04",
    "label": "Dear035",
    "start_s": 2525.9,
    "end_s": 2748.0333333333333,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 75777 to 82441 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-035, frames/M04_frame_header_07.jpg, frames/M04_frame_header_08.jpg, adv_dear_hmsz_035.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
    "source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
    "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "character": "MISUZU",
    "alias": "M04",
    "label": "Dear036",
    "start_s": 2748.0333333333333,
    "end_s": 3418.1666666666665,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 82441 to 102545 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-036, frames/M04_frame_header_08.jpg, frames/M04_frame_header_09.jpg, adv_dear_hmsz_036.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
  },
  {
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
    "source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
    "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "character": "MISUZU",
    "alias": "M04",
    "label": "Dear037",
    "start_s": 3418.1666666666665,
    "end_s": 3818.8333333333335,
    "music": false,
    "visual_step_s": 5.0,
    "boundary_note": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 102545 to 114565 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-037, frames/M04_frame_header_09.jpg, frames/M04_frame_header_10.jpg, adv_dear_hmsz_037.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
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
| M03 | whole_source_reproduction_check | 0 | 2835 | 2835 | -21.9 | 6.6 | -6.7 | 25.7808219677492 | 2173.83387635258 | 567 |
| M01 | Dear001 | 1.16666666666667 | 201.933333333333 | 200.766666666667 | -20.9 | 7.3 | -4.3 | 222.772654223956 | 1795.65998434929 | 41 |
| M01 | Dear002 | 201.933333333333 | 500.366666666667 | 298.433333333333 | -20.9 | 5.7 | -4.4 | 25.4726400533164 | 2070.61002671376 | 60 |
| M01 | Dear003 | 500.366666666667 | 739.266666666667 | 238.9 | -21.7 | 6.2 | -4.2 | 20.3953049639058 | 2069.0002372452 | 48 |
| M01 | Dear004 | 739.266666666667 | 1006.7 | 267.433333333333 | -20.9 | 6.6 | -3.8 | 21.7662437507769 | 2080.42360019665 | 54 |
| M01 | Dear005 | 1006.7 | 1260.26666666667 | 253.566666666667 | -21.1 | 7.1 | -4.2 | 54.4100674605255 | 1808.49080810476 | 51 |
| M01 | Dear006 | 1260.26666666667 | 1548.26666666667 | 288 | -20.9 | 7.3 | -3.8 | 25.6420768306404 | 2268.48127858573 | 58 |
| M01 | Dear007 | 1548.26666666667 | 1790.13333333333 | 241.866666666667 | -20.5 | 5.4 | -3.7 | 26.5610318894064 | 2358.69810967148 | 49 |
| M01 | Dear008 | 1790.13333333333 | 2092.83333333333 | 302.7 | -20.8 | 6 | -4.2 | 19.0639982249776 | 2418.04246445431 | 61 |
| M01 | Dear009 | 2092.83333333333 | 2398.36666666667 | 305.533333333333 | -20 | 8.6 | -3.2 | 21.132266935485 | 2084.04033529056 | 62 |
| M01 | Dear010 | 2398.36666666667 | 2753.2 | 354.833333333333 | -20.3 | 4.3 | -6.4 | 21.3026633245836 | 1833.04290214292 | 71 |
| M04 | Dear028 | 0.966666666666667 | 329.8 | 328.833333333333 | -19 | 4.5 | -2.7 | 18.282857234222 | 2316.8269620902 | 66 |
| M04 | Dear029 | 329.8 | 723.5 | 393.7 | -19.6 | 5.4 | -2.7 | 17.4863699286512 | 2078.48517595702 | 79 |
| M04 | Dear030 | 723.5 | 1010.73333333333 | 287.233333333333 | -19.5 | 7.4 | -2.9 | 19.1942357552226 | 2282.28163760772 | 58 |
| M04 | Dear031 | 1010.73333333333 | 1461.33333333333 | 450.6 | -19.6 | 7.5 | -4.8 | 19.1235587571626 | 2266.47392905037 | 91 |
| M04 | Dear032 | 1461.33333333333 | 1787.13333333333 | 325.8 | -19.1 | 4.8 | -4.4 | 21.0348960161797 | 1857.40779734679 | 66 |
| M04 | Dear033 | 1787.13333333333 | 2162.33333333333 | 375.2 | -19.7 | 4.8 | -4.3 | 18.6669319324808 | 2066.23685566664 | 76 |
| M04 | Dear034 | 2162.33333333333 | 2525.9 | 363.566666666667 | -19.6 | 6.6 | -4.9 | 19.4852629858442 | 2081.10935117826 | 73 |
| M04 | Dear035 | 2525.9 | 2748.03333333333 | 222.133333333333 | -19.6 | 6 | -5.4 | 19.5826128281592 | 1998.21084623325 | 45 |
| M04 | Dear036 | 2748.03333333333 | 3418.16666666667 | 670.133333333333 | -19.6 | 8.3 | -3.3 | 21.7147297961251 | 1964.48564729628 | 135 |
| M04 | Dear037 | 3418.16666666667 | 3818.83333333333 | 400.666666666667 | -19.3 | 6.7 | -4.3 | 27.8662521751692 | 1627.90050297614 | 81 |

## Record 01 — M03: whole_source_reproduction_check

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | d3e75a3ac55c7eefae39578d496a0463c4679a9acf8adde76d1b590f3f909126 |
| started_utc | 2026-09-10T06:15:18.834502+00:00 |
| completed_utc | 2026-09-10T06:16:21.288026+00:00 |
| source_id | 149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w |
| character | MISUZU |
| alias | M03 |
| label | whole_source_reproduction_check |
| input_path | LOCAL_USER/Downloads\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4 |
| filename | 【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4 |
| size_bytes | 296707894 |
| sha256 | 5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763 |
| start_s | 0 |
| end_s | 2835 |
| duration_s | 2835 |
| boundary_note | Whole container |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763 |
| source_id | 149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w |
| character | MISUZU |
| alias | M03 |
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
| streams[0].r_frame_rate | 60000/1001 |
| streams[0].avg_frame_rate | 60000/1001 |
| streams[0].time_base | 1/60000 |
| streams[0].start_pts | 0 |
| streams[0].start_time | 0.000000 |
| streams[0].duration_ts | 170067898 |
| streams[0].duration | 2834.464967 |
| streams[0].bit_rate | 692287 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 169898 |
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
| streams[1].duration_ts | 125002752 |
| streams[1].duration | 2834.529524 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 122073 |
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
| streams[2].codec_name | bin_data |
| streams[2].codec_long_name | binary data |
| streams[2].codec_type | data |
| streams[2].codec_tag_string | text |
| streams[2].codec_tag | 0x74786574 |
| streams[2].id | 0x3 |
| streams[2].r_frame_rate | 0/0 |
| streams[2].avg_frame_rate | 0/0 |
| streams[2].time_base | 1/1000 |
| streams[2].start_pts | 0 |
| streams[2].start_time | 0.000000 |
| streams[2].duration_ts | 2835000 |
| streams[2].duration | 2835.000000 |
| streams[2].nb_frames | 8 |
| streams[2].extradata_size | 43 |
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
| streams[2].disposition.attached_pic | 0 |
| streams[2].disposition.timed_thumbnails | 0 |
| streams[2].disposition.non_diegetic | 0 |
| streams[2].disposition.captions | 0 |
| streams[2].disposition.descriptions | 0 |
| streams[2].disposition.metadata | 0 |
| streams[2].disposition.dependent | 0 |
| streams[2].disposition.still_image | 0 |
| streams[2].disposition.multilayer | 0 |
| streams[2].tags.language | eng |
| streams[2].tags.handler_name | SubtitleHandler |
| streams[3].index | 3 |
| streams[3].codec_name | png |
| streams[3].codec_long_name | PNG (Portable Network Graphics) image |
| streams[3].codec_type | video |
| streams[3].codec_tag_string | [0][0][0][0] |
| streams[3].codec_tag | 0x0000 |
| streams[3].width | 1280 |
| streams[3].height | 720 |
| streams[3].coded_width | 1280 |
| streams[3].coded_height | 720 |
| streams[3].has_b_frames | 0 |
| streams[3].pix_fmt | rgb24 |
| streams[3].level | -99 |
| streams[3].color_range | pc |
| streams[3].color_space | gbr |
| streams[3].id | 0x0 |
| streams[3].r_frame_rate | 90000/1 |
| streams[3].avg_frame_rate | 0/0 |
| streams[3].time_base | 1/90000 |
| streams[3].start_pts | 0 |
| streams[3].start_time | 0.000000 |
| streams[3].duration_ts | 255150000 |
| streams[3].duration | 2835.000000 |
| streams[3].disposition.default | 0 |
| streams[3].disposition.dub | 0 |
| streams[3].disposition.original | 0 |
| streams[3].disposition.comment | 0 |
| streams[3].disposition.lyrics | 0 |
| streams[3].disposition.karaoke | 0 |
| streams[3].disposition.forced | 0 |
| streams[3].disposition.hearing_impaired | 0 |
| streams[3].disposition.visual_impaired | 0 |
| streams[3].disposition.clean_effects | 0 |
| streams[3].disposition.attached_pic | 1 |
| streams[3].disposition.timed_thumbnails | 0 |
| streams[3].disposition.non_diegetic | 0 |
| streams[3].disposition.captions | 0 |
| streams[3].disposition.descriptions | 0 |
| streams[3].disposition.metadata | 0 |
| streams[3].disposition.dependent | 0 |
| streams[3].disposition.still_image | 0 |
| streams[3].disposition.multilayer | 0 |
| chapters[0].id | 0 |
| chapters[0].time_base | 1/1000 |
| chapters[0].start | 0 |
| chapters[0].start_time | 0.000000 |
| chapters[0].end | 310000 |
| chapters[0].end_time | 310.000000 |
| chapters[0].tags.title | 親愛度コミュ21話 |
| chapters[1].id | 1 |
| chapters[1].time_base | 1/1000 |
| chapters[1].start | 310000 |
| chapters[1].start_time | 310.000000 |
| chapters[1].end | 632000 |
| chapters[1].end_time | 632.000000 |
| chapters[1].tags.title | 親愛度コミュ22話 |
| chapters[2].id | 2 |
| chapters[2].time_base | 1/1000 |
| chapters[2].start | 632000 |
| chapters[2].start_time | 632.000000 |
| chapters[2].end | 943000 |
| chapters[2].end_time | 943.000000 |
| chapters[2].tags.title | 親愛度コミュ23話 |
| chapters[3].id | 3 |
| chapters[3].time_base | 1/1000 |
| chapters[3].start | 943000 |
| chapters[3].start_time | 943.000000 |
| chapters[3].end | 1393000 |
| chapters[3].end_time | 1393.000000 |
| chapters[3].tags.title | 親愛度コミュ24話 |
| chapters[4].id | 4 |
| chapters[4].time_base | 1/1000 |
| chapters[4].start | 1393000 |
| chapters[4].start_time | 1393.000000 |
| chapters[4].end | 1770000 |
| chapters[4].end_time | 1770.000000 |
| chapters[4].tags.title | 親愛度コミュ25話 |
| chapters[5].id | 5 |
| chapters[5].time_base | 1/1000 |
| chapters[5].start | 1770000 |
| chapters[5].start_time | 1770.000000 |
| chapters[5].end | 2135000 |
| chapters[5].end_time | 2135.000000 |
| chapters[5].tags.title | 親愛度コミュ26話 |
| chapters[6].id | 6 |
| chapters[6].time_base | 1/1000 |
| chapters[6].start | 2135000 |
| chapters[6].start_time | 2135.000000 |
| chapters[6].end | 2651000 |
| chapters[6].end_time | 2651.000000 |
| chapters[6].tags.title | 親愛度コミュ27話 |
| chapters[7].id | 7 |
| chapters[7].time_base | 1/1000 |
| chapters[7].start | 2651000 |
| chapters[7].start_time | 2651.000000 |
| chapters[7].end | 2835000 |
| chapters[7].end_time | 2835.000000 |
| chapters[7].tags.title | ED |
| format.filename | LOCAL_USER/Downloads\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4 |
| format.nb_streams | 4 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2835.000000 |
| format.size | 296707894 |
| format.bit_rate | 837270 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】 秦谷美鈴  親愛度コミュ21～27話まとめ【STEP3】 |
| format.tags.artist | 学Pといっしょ |
| format.tags.genre | Gaming |
| format.tags.date | 20260429 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=wt77y0MHvVU |
| format.tags.description | 【注意】この動画には「学園アイドルマスター」のネタバレを含みます。<br><br>【動画内容】<br>親愛度コミュ21話 0:00～<br>親愛度コミュ22話 5:10～<br>親愛度コミュ23話 10:32～<br>親愛度コミュ24話 15:43～<br>親愛度コミュ25話 23:13～<br>親愛度コミュ26話 29:30～<br>親愛度コミュ27話 35:35～<br>ED 44:11～<br><br><br>▼学マス 好評配信中！▼<br>http://app.adjust.com/1ai6ouao<br><br>学マス公式サイト<br>https://gakuen.idolmaster-official.jp/<br>学マス公式X(Twitter)<br>https://x.com/gkmas_official<br><br><br>#学マス<br>#秦谷美鈴 |
| format.tags.synopsis | 【注意】この動画には「学園アイドルマスター」のネタバレを含みます。<br><br>【動画内容】<br>親愛度コミュ21話 0:00～<br>親愛度コミュ22話 5:10～<br>親愛度コミュ23話 10:32～<br>親愛度コミュ24話 15:43～<br>親愛度コミュ25話 23:13～<br>親愛度コミュ26話 29:30～<br>親愛度コミュ27話 35:35～<br>ED 44:11～<br><br><br>▼学マス 好評配信中！▼<br>http://app.adjust.com/1ai6ouao<br><br>学マス公式サイト<br>https://gakuen.idolmaster-official.jp/<br>学マス公式X(Twitter)<br>https://x.com/gkmas_official<br><br><br>#学マス<br>#秦谷美鈴 |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 62501376 |
| analyzed_audio_duration_s | 2834.52952380952 |
| stft_frames | 122070 |
| flux_transitions | 122069 |
| rms_linear | 0.0699509364853757 |
| rms_p10_linear | 0.00639389339872358 |
| rms_p90_linear | 0.124396021194034 |
| rms_p90_p10_db | 25.7808219677492 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 4502 |
| centroid_hz_mean | 2173.83387635258 |
| flatness_mean | 0.0635090111393339 |
| positive_normalized_flux_mean | 0.035262940116329 |
| flux_cv | 0.665791328061186 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -21.9 |
| lra_lu | 6.6 |
| true_peak_dbfs | -6.7 |
| silence_seconds | 139.895460999999 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -21.9 LUFS<br>    Threshold: -33.2 LUFS<br><br>  Loudness range:<br>    LRA:         6.6 LU<br>    Threshold: -43.4 LUFS<br>    LRA low:   -27.4 LUFS<br>    LRA high:  -20.8 LUFS<br><br>  True peak:<br>    Peak:       -6.7 dBFS<br>[out#0/null @ 0000022597ab8640] video:0KiB audio:488292KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:47:14.52 bitrate=N/A speed= 196x elapsed=0:00:14.48 |
| ffmpeg_stderr_sha256 | eadc24cace34dd96c04d41013418b662694bf929dc7bbb8b748707ce2272f0c9 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 0 | 6.995556 | 6.995556 | 6.995556 |
| 131.202245 | 131.836508 | 0.634263000000004 | 0.634263 |
| 133.507211 | 134.250839 | 0.743628000000001 | 0.743628 |
| 134.681746 | 135.231156 | 0.549409999999995 | 0.54941 |
| 135.989138 | 136.780023 | 0.790885000000003 | 0.790884 |
| 137.060635 | 137.837029 | 0.77639400000001 | 0.776395 |
| 140.492177 | 141.421701 | 0.929524000000015 | 0.929524 |
| 230.674558 | 231.401905 | 0.727347000000009 | 0.727347 |
| 232.475215 | 233.246213 | 0.77099800000002 | 0.770998 |
| 235.034195 | 235.745306 | 0.711110999999988 | 0.711111 |
| 237.639116 | 239.592902 | 1.95378600000001 | 1.953787 |
| 310.322857 | 311.034036 | 0.711179000000016 | 0.711179 |
| 316.742562 | 317.300952 | 0.558389999999974 | 0.55839 |
| 321.778753 | 323.084694 | 1.30594100000002 | 1.305941 |
| 403.41034 | 404.314082 | 0.903741999999966 | 0.903741 |
| 406.239796 | 407.844127 | 1.604331 | 1.604331 |
| 409.183333 | 409.807438 | 0.624104999999986 | 0.624104 |
| 541.120385 | 542.734082 | 1.61369699999989 | 1.613696 |
| 544.540363 | 546.264195 | 1.72383200000002 | 1.723832 |
| 588.242086 | 589.755306 | 1.51322000000005 | 1.51322 |
| 590.363605 | 592.643787 | 2.28018199999997 | 2.280181 |
| 594.119478 | 594.733469 | 0.613991000000055 | 0.613991 |
| 596.597914 | 597.207778 | 0.609864000000016 | 0.609864 |
| 601.364036 | 601.943379 | 0.579342999999994 | 0.579342 |
| 607.573424 | 609.704558 | 2.13113399999997 | 2.131134 |
| 774.141746 | 774.996576 | 0.854829999999993 | 0.85483 |
| 775.569683 | 776.1278 | 0.558116999999925 | 0.558118 |
| 777.366871 | 777.955828 | 0.58895700000005 | 0.588957 |
| 779.009841 | 779.536236 | 0.52639499999998 | 0.526395 |
| 780.73644 | 781.418005 | 0.681564999999978 | 0.681565 |
| 783.094082 | 783.727166 | 0.633084000000053 | 0.633084 |
| 860.509637 | 861.113016 | 0.603379000000018 | 0.603379 |
| 862.099819 | 863.662948 | 1.563129 | 1.563129 |
| 866.663129 | 868.297007 | 1.63387799999998 | 1.633878 |
| 870.576236 | 871.885193 | 1.30895699999996 | 1.308957 |
| 872.843084 | 873.465964 | 0.622880000000009 | 0.62288 |
| 875.035896 | 876.276667 | 1.240771 | 1.240771 |
| 877.531406 | 879.858503 | 2.32709700000009 | 2.327098 |
| 880.966712 | 881.642812 | 0.676100000000019 | 0.6761 |
| 882.582404 | 883.339615 | 0.757210999999984 | 0.757211 |
| 885.939683 | 887.266871 | 1.32718800000009 | 1.327188 |
| 887.968549 | 888.55034 | 0.581790999999953 | 0.581791 |
| 1084.532902 | 1086.646961 | 2.114059 | 2.114059 |
| 1164.111882 | 1164.93093 | 0.819048000000066 | 0.819048 |
| 1165.319615 | 1165.900635 | 0.581019999999853 | 0.58102 |
| 1167.283175 | 1169.007596 | 1.72442099999989 | 1.724422 |
| 1237.270907 | 1237.881315 | 0.610408000000007 | 0.610408 |
| 1238.926848 | 1239.870317 | 0.943468999999823 | 0.943469 |
| 1240.400975 | 1240.996508 | 0.595532999999932 | 0.595533 |
| 1241.839955 | 1242.426236 | 0.586281000000099 | 0.586281 |
| 1244.688912 | 1245.505397 | 0.81648499999983 | 0.816485 |
| 1368.727778 | 1370.79805 | 2.07027200000016 | 2.070272 |
| 1371.115329 | 1372.718639 | 1.60330999999996 | 1.603311 |
| 1373.408413 | 1374.099388 | 0.69097499999998 | 0.690975 |
| 1374.699841 | 1376.131995 | 1.43215399999985 | 1.432154 |
| 1377.550998 | 1379.297574 | 1.746576 | 1.746576 |
| 1380.093946 | 1382.096213 | 2.00226700000007 | 2.002268 |
| 1383.208413 | 1384.674762 | 1.46634900000004 | 1.466349 |
| 1386.230317 | 1387.02288 | 0.792562999999973 | 0.792562 |
| 1389.282132 | 1390.376689 | 1.0945569999999 | 1.094558 |
| 1392.353583 | 1392.979955 | 0.626371999999947 | 0.626372 |
| 1445.860635 | 1447.76161 | 1.90097500000002 | 1.900975 |
| 1448.725782 | 1450.702971 | 1.97718899999995 | 1.977188 |
| 1451.986984 | 1452.555646 | 0.568662000000131 | 0.568662 |
| 1453.181383 | 1454.235646 | 1.05426299999999 | 1.054263 |
| 1455.891361 | 1457.117347 | 1.22598600000015 | 1.225986 |
| 1458.154535 | 1459.137098 | 0.982563000000027 | 0.982562 |
| 1459.798481 | 1460.766327 | 0.967846000000009 | 0.967846 |
| 1462.131927 | 1462.886281 | 0.754354000000149 | 0.754354 |
| 1604.870204 | 1605.855646 | 0.985441999999921 | 0.985442 |
| 1607.791383 | 1609.381882 | 1.59049899999991 | 1.590499 |
| 1610.578549 | 1611.415329 | 0.836779999999862 | 0.83678 |
| 1612.630317 | 1617.885374 | 5.25505699999985 | 5.255057 |
| 1732.058413 | 1732.558934 | 0.500520999999935 | 0.500522 |
| 1735.431383 | 1736.604172 | 1.17278899999997 | 1.172789 |
| 1736.781383 | 1737.586916 | 0.805532999999969 | 0.805533 |
| 1823.221678 | 1824.159932 | 0.938253999999915 | 0.938254 |
| 1825.275964 | 1826.340181 | 1.0642170000001 | 1.064218 |
| 1827.432404 | 1828.402132 | 0.969728000000032 | 0.969728 |
| 1828.539615 | 1829.807098 | 1.26748300000008 | 1.267483 |
| 1831.980113 | 1833.291882 | 1.31176899999991 | 1.311769 |
| 1834.576032 | 1835.102086 | 0.526054000000158 | 0.526054 |
| 1977.267347 | 1979.099297 | 1.83195000000001 | 1.83195 |
| 1980.338231 | 1981.452358 | 1.11412700000005 | 1.114127 |
| 1984.39898 | 1987.062653 | 2.66367300000002 | 2.663673 |
| 2055.180567 | 2056.810181 | 1.62961399999995 | 1.629615 |
| 2058.988753 | 2059.658549 | 0.669796000000133 | 0.669796 |
| 2062.071497 | 2062.936599 | 0.865102000000206 | 0.865102 |
| 2065.056485 | 2065.802086 | 0.745601000000079 | 0.745601 |
| 2134.917891 | 2135.733673 | 0.815782000000127 | 0.815782 |
| 2168.131293 | 2169.073311 | 0.942018000000189 | 0.942018 |
| 2198.251633 | 2198.989297 | 0.737664000000223 | 0.737664 |
| 2268.422426 | 2269.922472 | 1.50004600000011 | 1.500045 |
| 2270.56127 | 2271.164989 | 0.603718999999728 | 0.603719 |
| 2273.24059 | 2274.031746 | 0.791156000000228 | 0.791156 |
| 2274.402268 | 2274.998753 | 0.59648500000003 | 0.596485 |
| 2275.504195 | 2276.082676 | 0.578481000000011 | 0.578481 |
| 2276.47 | 2278.283673 | 1.81367300000011 | 1.813673 |
| 2382.346395 | 2383.219229 | 0.872833999999784 | 0.872834 |
| 2385.740998 | 2386.704966 | 0.963967999999568 | 0.963968 |
| 2387.492925 | 2388.296893 | 0.803968000000168 | 0.803968 |
| 2390.298866 | 2391.752857 | 1.45399099999986 | 1.453991 |
| 2392.692857 | 2393.539705 | 0.846848000000136 | 0.846848 |
| 2394.512018 | 2395.398594 | 0.886575999999877 | 0.886576 |
| 2396.631905 | 2397.229388 | 0.597483000000011 | 0.597483 |
| 2397.419048 | 2398.608163 | 1.18911499999967 | 1.189116 |
| 2399.083129 | 2399.696327 | 0.613198000000011 | 0.613197 |
| 2566.498844 | 2567.597007 | 1.09816299999966 | 1.098163 |
| 2568.423832 | 2569.226644 | 0.802811999999903 | 0.802812 |
| 2570.082472 | 2572.022449 | 1.939977 | 1.939977 |
| 2650.568753 | 2652.285283 | 1.71653000000015 | 1.716531 |
| 2802.119819 | 2807.930703 | 5.81088399999999 | 5.810884 |
| 2829.942562 | 2834.529524 | 4.58696199999986 | 4.586961 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 567 |
| samples | 567 |
| brightness_mean | 0.50224276388974 |
| saturation_mean | 0.325893834557142 |
| frame_difference_mean | 0.0720534660142201 |
| histogram_jumps_gt_0_5 | 35 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0.383426755666733 | 0.559161220043573 | N/A | N/A | N/A |
| 5 | 5.005 | 0.513632118701935 | 0.547627723311547 | 0.131183549761772 | 0.616445331371644 | 5 |
| 10 | 9.99331666666667 | 0.56281566619873 | 0.294015795206972 | 0.0861111134290695 | 0.529337416854042 | 5 |
| 15 | 14.9983166666667 | 0.564487993717194 | 0.326278867102397 | 0.0915983095765114 | 0.318755742242138 | 5 |
| 20 | 20.0033166666667 | 0.499326825141907 | 0.345369553376906 | 0.153970032930374 | 0.305190759294943 | 5 |
| 25 | 25.0083166666667 | 0.5902219414711 | 0.30247848583878 | 0.132696345448494 | 0.258719309743777 | 5 |
| 30 | 29.9966333333333 | 0.510714292526245 | 0.330566993464052 | 0.111317537724972 | 0.245152988522938 | 5 |
| 35 | 35.0016333333333 | 0.512406051158905 | 0.32749591503268 | 0.0143180824816227 | 0.0475859138969269 | 5 |
| 40 | 40.0066333333333 | 0.558289229869843 | 0.307981209150327 | 0.104813441634178 | 0.196548671160445 | 5 |
| 45 | 44.99495 | 0.524900913238525 | 0.321166122004357 | 0.0918349623680115 | 0.113497178222714 | 5 |
| 50 | 49.99995 | 0.496876895427704 | 0.337041666666667 | 0.0818376913666725 | 0.118436804545318 | 5 |
| 55 | 55.00495 | 0.542516052722931 | 0.312556917211329 | 0.090336874127388 | 0.212240912399953 | 5 |
| 60 | 59.9932666666667 | 0.561635375022888 | 0.311157952069717 | 0.0692548975348473 | 0.144665999243428 | 5 |
| 65 | 64.9982666666667 | 0.549036741256714 | 0.311559640522876 | 0.0594923682510853 | 0.180375622777975 | 5 |
| 70 | 70.0032666666667 | 0.545482337474823 | 0.310080065359477 | 0.044201523065567 | 0.0625923630596277 | 5 |
| 75 | 75.0082666666667 | 0.518020153045654 | 0.322632352941176 | 0.0870732516050339 | 0.128854054009048 | 5 |
| 80 | 79.9965833333333 | 0.561388075351715 | 0.312509259259259 | 0.0947736948728561 | 0.266874387254529 | 5 |
| 85 | 85.0015833333333 | 0.552360355854034 | 0.31592265795207 | 0.0711143761873245 | 0.13132044500769 | 5 |
| 90 | 90.0065833333333 | 0.611365437507629 | 0.265002450980392 | 0.0721729248762131 | 0.277789481000777 | 5 |
| 95 | 94.9949 | 0.509345352649689 | 0.315608932461874 | 0.115782134234905 | 0.440383295845915 | 5 |
| 100 | 99.9999 | 0.491427540779114 | 0.303665577342048 | 0.0838622003793716 | 0.170148292426494 | 5 |
| 105 | 105.0049 | 0.500187933444977 | 0.306658769063181 | 0.059521246701479 | 0.0896513498710958 | 5 |
| 110 | 109.993216666667 | 0.559109508991241 | 0.314791122004357 | 0.107149235904217 | 0.283616531732874 | 5 |
| 115 | 114.998216666667 | 0.559055268764496 | 0.314843137254902 | 0.00359667744487524 | 0.0224764995416714 | 5 |
| 120 | 120.003216666667 | 0.556460857391357 | 0.314766067538126 | 0.0729419961571693 | 0.133998969816141 | 5 |
| 125 | 125.008216666667 | 0.559184372425079 | 0.313552287581699 | 0.0728820785880089 | 0.144945193274094 | 5 |
| 130 | 129.996533333333 | 0.532653033733368 | 0.312305555555556 | 0.0926919877529144 | 0.197510397499671 | 5 |
| 135 | 135.001533333333 | 0.564707517623901 | 0.314132625272331 | 0.0964438989758492 | 0.198049924117213 | 5 |
| 140 | 140.006533333333 | 0.532714605331421 | 0.323759803921569 | 0.0994161143898964 | 0.216725074314823 | 5 |
| 145 | 144.99485 | 0.528739631175995 | 0.318659041394336 | 0.033039215952158 | 0.0525143376384049 | 5 |
| 150 | 149.99985 | 0.532291948795319 | 0.321977941176471 | 0.0283028334379196 | 0.0555210225322851 | 5 |
| 155 | 155.00485 | 0.52971625328064 | 0.322549836601307 | 0.0270326789468527 | 0.0400305545580922 | 5 |
| 160 | 159.993166666667 | 0.560112774372101 | 0.314650054466231 | 0.0997750535607338 | 0.266170815510721 | 5 |
| 165 | 164.998166666667 | 0.556715130805969 | 0.31439188453159 | 0.00979792978614569 | 0.0291131783789845 | 5 |
| 170 | 170.003166666667 | 0.531181633472443 | 0.321973039215686 | 0.106647320091724 | 0.257330703087945 | 5 |
| 175 | 175.008166666667 | 0.530276417732239 | 0.322003267973856 | 0.0127608934417367 | 0.0319690268746374 | 5 |
| 180 | 179.996483333333 | 0.553853511810303 | 0.321041394335512 | 0.09663425385952 | 0.242319544580758 | 5 |
| 185 | 185.001483333333 | 0.555137574672699 | 0.320855664488017 | 0.00971650239080191 | 0.0289719272265527 | 5 |
| 190 | 190.006483333333 | 0.556647896766663 | 0.319836873638344 | 0.0676922649145126 | 0.117587331741028 | 5 |
| 195 | 194.9948 | 0.56134420633316 | 0.318257080610022 | 0.021645151078701 | 0.0368315479496289 | 5 |
| 200 | 199.9998 | 0.559140026569366 | 0.318503540305011 | 0.021028321236372 | 0.0349113767848008 | 5 |
| 205 | 205.0048 | 0.561533510684967 | 0.314154956427015 | 0.0308886151760817 | 0.0522244688677395 | 5 |
| 210 | 209.993116666667 | 0.557541906833649 | 0.315243736383442 | 0.0726712942123413 | 0.121498144323203 | 5 |
| 215 | 214.998116666667 | 0.562150895595551 | 0.314400326797386 | 0.0691486895084381 | 0.111813060273088 | 5 |
| 220 | 220.003116666667 | 0.5623859167099 | 0.315789760348584 | 0.0133139984682202 | 0.0270101437543247 | 5 |
| 225 | 225.008116666667 | 0.529617667198181 | 0.31800462962963 | 0.0949969962239265 | 0.217296209391426 | 5 |
| 230 | 229.996433333333 | 0.50740772485733 | 0.307773420479303 | 0.0826783776283264 | 0.163668460584678 | 5 |
| 235 | 235.001433333333 | 0.50761216878891 | 0.310918845315904 | 0.0472873076796532 | 0.0504299164329367 | 5 |
| 240 | 240.006433333333 | 0.507296323776245 | 0.309062636165577 | 0.0142445545643568 | 0.0406893205740116 | 5 |
| 245 | 244.99475 | 0.556997299194336 | 0.317029684095861 | 0.105940088629723 | 0.229708120487782 | 5 |
| 250 | 249.99975 | 0.526716768741608 | 0.316193355119826 | 0.0932401940226555 | 0.209000580032243 | 5 |
| 255 | 255.00475 | 0.508458316326141 | 0.315165849673203 | 0.08330038189888 | 0.148584895201453 | 5 |
| 260 | 259.993066666667 | 0.506580352783203 | 0.312195533769063 | 0.0444874726235867 | 0.0676917336623603 | 5 |
| 265 | 264.998066666667 | 0.529150068759918 | 0.320674564270153 | 0.0863905176520348 | 0.147987595164053 | 5 |
| 270 | 270.003066666667 | 0.527867376804352 | 0.319938725490196 | 0.0155876912176609 | 0.0336856049281288 | 5 |
| 275 | 275.008066666667 | 0.561035931110382 | 0.316063997821351 | 0.0994463413953781 | 0.191996327023745 | 5 |
| 280 | 279.996383333333 | 0.529145419597626 | 0.319099673202614 | 0.101685725152493 | 0.200446412867143 | 5 |
| 285 | 285.001383333333 | 0.505088210105896 | 0.309147331154684 | 0.0830975025892258 | 0.161716442468506 | 5 |
| 290 | 290.006383333333 | 0.560308814048767 | 0.315649237472767 | 0.119492918252945 | 0.249844548890369 | 5 |
| 295 | 294.9947 | 0.533051490783691 | 0.321311274509804 | 0.100731201469898 | 0.240576147748498 | 5 |
| 300 | 299.9997 | 0.526960849761963 | 0.318837690631808 | 0.0272426474839449 | 0.0514318358883838 | 5 |
| 305 | 305.0047 | 0.523384034633636 | 0.319020697167756 | 0.034234207123518 | 0.0455590453661385 | 5 |
| 310 | 309.993016666667 | 0.544554233551025 | 0.327743464052288 | 0.103747002780437 | 0.234614609544025 | 5 |
| 315 | 314.998016666667 | 0.511982619762421 | 0.330206699346405 | 0.117658227682114 | 0.26642450107341 | 5 |
| 320 | 320.003016666667 | 0.513509511947632 | 0.330132352941176 | 0.00320288678631186 | 0.0298747189704237 | 5 |
| 325 | 325.008016666667 | 0.507555603981018 | 0.318034586056645 | 0.101656042039394 | 0.248919909951099 | 5 |
| 330 | 329.996333333333 | 0.50898289680481 | 0.320319444444444 | 0.00533197121694684 | 0.0430202449644142 | 5 |
| 335 | 335.001333333333 | 0.516527771949768 | 0.311892973856209 | 0.102693624794483 | 0.166202056687413 | 5 |
| 340 | 340.006333333333 | 0.506513059139252 | 0.321544662309368 | 0.099301740527153 | 0.162210549317879 | 5 |
| 345 | 344.99465 | 0.505851566791534 | 0.323622276688453 | 0.0291249994188547 | 0.0670501755118317 | 5 |
| 350 | 349.99965 | 0.506249785423279 | 0.323547385620915 | 0.0166791938245296 | 0.0220587103935049 | 5 |
| 355 | 355.00465 | 0.50712525844574 | 0.320450163398693 | 0.0271440614014864 | 0.070667428180153 | 5 |
| 360 | 359.992966666667 | 0.526957273483276 | 0.307937091503268 | 0.098896786570549 | 0.168018690765487 | 5 |
| 365 | 364.997966666667 | 0.519663691520691 | 0.3081424291939 | 0.0418180823326111 | 0.0722163502244906 | 5 |
| 370 | 370.002966666667 | 0.5190509557724 | 0.305782407407407 | 0.0179842039942741 | 0.0399412530289453 | 5 |
| 375 | 375.007966666667 | 0.499768495559692 | 0.325895152505447 | 0.0914425328373909 | 0.205397296207515 | 5 |
| 380 | 379.996283333333 | 0.509419441223145 | 0.323035675381264 | 0.0285501070320606 | 0.0558889275825958 | 5 |
| 385 | 385.001283333333 | 0.50936084985733 | 0.320440631808279 | 0.00921377912163734 | 0.0480225705145478 | 5 |
| 390 | 390.006283333333 | 0.52276337146759 | 0.305826252723312 | 0.0980070829391479 | 0.199013058534095 | 5 |
| 395 | 394.9946 | 0.516181111335754 | 0.311258986928105 | 0.0335762538015842 | 0.0780894505836982 | 5 |
| 400 | 399.9996 | 0.515387296676636 | 0.311370642701525 | 0.00721704820170999 | 0.0271747253688756 | 5 |
| 405 | 405.0046 | 0.498833358287811 | 0.324035947712418 | 0.0869351848959923 | 0.176008608447543 | 5 |
| 410 | 409.992916666667 | 0.507755994796753 | 0.32056862745098 | 0.0232636146247387 | 0.0924212490127562 | 5 |
| 415 | 414.997916666667 | 0.505656898021698 | 0.320516067538126 | 0.00553758209571242 | 0.0263246317675055 | 5 |
| 420 | 420.002916666667 | 0.504107892513275 | 0.324393246187364 | 0.0323905237019062 | 0.0714507784366555 | 5 |
| 425 | 425.007916666667 | 0.522965967655182 | 0.305718681917211 | 0.0931152030825615 | 0.199522463254946 | 5 |
| 430 | 429.996233333333 | 0.514634251594543 | 0.310551198257081 | 0.0297870356589556 | 0.0992433813882086 | 5 |
| 435 | 435.001233333333 | 0.507600486278534 | 0.320844498910675 | 0.0949684157967567 | 0.15814234613564 | 5 |
| 440 | 440.006233333333 | 0.501458048820496 | 0.325957788671024 | 0.0292775053530931 | 0.0729364118393222 | 5 |
| 445 | 444.99455 | 0.499856501817703 | 0.326140250544662 | 0.013424564152956 | 0.0365911100690431 | 5 |
| 450 | 449.99955 | 0.508974432945251 | 0.320826252723312 | 0.0269212927669287 | 0.055124832282669 | 5 |
| 455 | 455.00455 | 0.501934945583344 | 0.326062091503268 | 0.0308112744241953 | 0.0573377338112378 | 5 |
| 460 | 459.992866666667 | 0.508118212223053 | 0.320402505446623 | 0.0287088770419359 | 0.0671853160028809 | 5 |
| 465 | 464.997866666667 | 0.525693655014038 | 0.304352668845316 | 0.0947829484939575 | 0.177898500718861 | 5 |
| 470 | 470.002866666667 | 0.522795498371124 | 0.307407407407407 | 0.0279558822512627 | 0.0496655382729412 | 5 |
| 475 | 475.007866666667 | 0.507150828838348 | 0.318710784313725 | 0.0933641046285629 | 0.159916195859771 | 5 |
| 480 | 479.996183333333 | 0.509065389633179 | 0.319448529411765 | 0.0313779935240746 | 0.0530243556905472 | 5 |
| 485 | 485.001183333333 | 0.509433567523956 | 0.321411764705882 | 0.00652832258492708 | 0.041421756430802 | 5 |
| 490 | 490.006183333333 | 0.498052567243576 | 0.325909586056645 | 0.0288564804941416 | 0.0568798051084444 | 5 |
| 495 | 494.9945 | 0.507809400558472 | 0.320918845315904 | 0.0334517955780029 | 0.0640287995600291 | 5 |
| 500 | 499.9995 | 0.516964614391327 | 0.310885893246187 | 0.0966051146388054 | 0.158230687412426 | 5 |
| 505 | 505.0045 | 0.51591557264328 | 0.313084967320261 | 0.0408627390861511 | 0.0521758805958648 | 5 |
| 510 | 509.992816666667 | 0.517597198486328 | 0.311740196078431 | 0.034040030092001 | 0.0353588959986078 | 5 |
| 515 | 514.997816666667 | 0.526172637939453 | 0.305622276688453 | 0.0472627989947796 | 0.06085202530212 | 5 |
| 520 | 520.002816666667 | 0.505157649517059 | 0.318660675381264 | 0.104383714497089 | 0.172592626110314 | 5 |
| 525 | 525.007816666667 | 0.508773446083069 | 0.322604575163399 | 0.0314844772219658 | 0.0835971972686178 | 5 |
| 530 | 529.996133333333 | 0.522709667682648 | 0.309236383442266 | 0.0860942229628563 | 0.166403324958397 | 5 |
| 535 | 535.001133333333 | 0.519887506961823 | 0.30996977124183 | 0.0172829516232014 | 0.031872094021885 | 5 |
| 540 | 540.006133333333 | 0.50839763879776 | 0.318564814814815 | 0.0923924222588539 | 0.159854883523252 | 5 |
| 545 | 544.99445 | 0.507843673229218 | 0.31857788671024 | 0.00374945532530546 | 0.0189873256717688 | 5 |
| 550 | 549.99945 | 0.52703595161438 | 0.310273420479303 | 0.0972047969698906 | 0.160629095061277 | 5 |
| 555 | 555.00445 | 0.515821635723114 | 0.310967592592593 | 0.0405520163476467 | 0.0738166157360354 | 5 |
| 560 | 559.992766666667 | 0.516396760940552 | 0.311181644880174 | 0.00889052264392376 | 0.0298392758865418 | 5 |
| 565 | 564.997766666667 | 0.499012023210526 | 0.323962690631808 | 0.0867371931672096 | 0.176887384974743 | 5 |
| 570 | 570.002766666667 | 0.506643533706665 | 0.32068082788671 | 0.0233036484569311 | 0.0897464786659626 | 5 |
| 575 | 575.007766666667 | 0.508942544460297 | 0.320958605664488 | 0.0223583877086639 | 0.0502847316932898 | 5 |
| 580 | 579.996083333333 | 0.509181916713715 | 0.32085348583878 | 0.00528676435351372 | 0.0236479700131703 | 5 |
| 585 | 585.001083333333 | 0.524931967258453 | 0.307654411764706 | 0.0986857265233994 | 0.155211784071897 | 5 |
| 590 | 590.006083333333 | 0.526816725730896 | 0.305883442265795 | 0.0169180277734995 | 0.0306384792013063 | 5 |
| 595 | 594.9944 | 0.540438711643219 | 0.317425381263617 | 0.10244607925415 | 0.288567298202747 | 5 |
| 600 | 599.9994 | 0.537302017211914 | 0.319883442265795 | 0.0240533761680126 | 0.0507483125804114 | 5 |
| 605 | 605.0044 | 0.542276382446289 | 0.315042755991285 | 0.0769379064440727 | 0.144817743218662 | 5 |
| 610 | 609.992716666667 | 0.510006248950958 | 0.319998366013072 | 0.111958056688309 | 0.258282998033999 | 5 |
| 615 | 614.997716666667 | 0.506592631340027 | 0.320692265795207 | 0.012139705941081 | 0.0287960439768345 | 5 |
| 620 | 620.002716666667 | 0.500150084495544 | 0.32593137254902 | 0.0264959167689085 | 0.0861837720722737 | 5 |
| 625 | 625.007716666667 | 0.525146007537842 | 0.305381808278867 | 0.0884267389774323 | 0.208118337234978 | 5 |
| 630 | 629.996033333333 | 0.521904408931732 | 0.305345315904139 | 0.0295846946537495 | 0.0620717630176007 | 5 |
| 635 | 635.001033333333 | 0.456821888685226 | 0.360105664488017 | 0.100471943616867 | 0.324503849505294 | 5 |
| 640 | 640.006033333333 | 0.465159296989441 | 0.371094226579521 | 0.0860694348812103 | 0.203190201441894 | 5 |
| 645 | 644.99435 | 0.456823527812958 | 0.368513888888889 | 0.0780187919735909 | 0.164171406067605 | 5 |
| 650 | 649.99935 | 0.455511480569839 | 0.36743545751634 | 0.0260206963866949 | 0.0422699133533402 | 5 |
| 655 | 655.00435 | 0.459800153970718 | 0.362750272331155 | 0.0827685222029686 | 0.171899838456431 | 5 |
| 660 | 659.992666666667 | 0.46021243929863 | 0.361438453159041 | 0.0441023930907249 | 0.074888975785886 | 5 |
| 665 | 664.997666666667 | 0.47724837064743 | 0.349169662309368 | 0.0804400816559792 | 0.207891557413853 | 5 |
| 670 | 670.002666666667 | 0.457006841897964 | 0.36979711328976 | 0.0791723802685738 | 0.179139541332841 | 5 |
| 675 | 675.007666666667 | 0.459798216819763 | 0.365776960784314 | 0.0149488020688295 | 0.0496477081885054 | 5 |
| 680 | 679.995983333333 | 0.457004100084305 | 0.368028050108932 | 0.0153801739215851 | 0.0420027475579297 | 5 |
| 685 | 685.000983333333 | 0.453570276498795 | 0.370462418300654 | 0.0221413392573595 | 0.0441672294407681 | 5 |
| 690 | 690.005983333333 | 0.461852699518204 | 0.370404956427015 | 0.0825438424944878 | 0.203087965733245 | 5 |
| 695 | 694.9943 | 0.489552825689316 | 0.31679302832244 | 0.0886228159070015 | 0.316497422022127 | 5 |
| 700 | 699.9993 | 0.45504903793335 | 0.368800108932462 | 0.0851574093103409 | 0.30102024396127 | 5 |
| 705 | 705.0043 | 0.455943048000336 | 0.369320533769063 | 0.0258243456482887 | 0.0443760010856445 | 5 |
| 710 | 709.992616666667 | 0.452843964099884 | 0.369843409586057 | 0.0268529430031776 | 0.0515209782908733 | 5 |
| 715 | 714.997616666667 | 0.482036471366882 | 0.338127450980392 | 0.0897208675742149 | 0.256993967310665 | 5 |
| 720 | 720.002616666667 | 0.494654178619385 | 0.316188997821351 | 0.0662396475672722 | 0.189842314417892 | 5 |
| 725 | 725.007616666667 | 0.455874770879745 | 0.36897385620915 | 0.0874297395348549 | 0.32175762868199 | 5 |
| 730 | 729.995933333333 | 0.461585819721222 | 0.369770697167756 | 0.0807758644223213 | 0.152089472728118 | 5 |
| 735 | 735.000933333333 | 0.457083642482758 | 0.367824618736383 | 0.0819117650389671 | 0.151619789686436 | 5 |
| 740 | 740.005933333333 | 0.456126362085342 | 0.3677151416122 | 0.00489678652957082 | 0.0272901188590674 | 5 |
| 745 | 744.99425 | 0.471418857574463 | 0.348096132897603 | 0.0813954174518585 | 0.185998699286799 | 5 |
| 750 | 749.99925 | 0.5240558385849 | 0.323674564270153 | 0.146328702569008 | 0.412817485936353 | 5 |
| 755 | 755.00425 | 0.521690428256989 | 0.327211873638344 | 0.00346241844817996 | 0.030778761595604 | 5 |
| 760 | 759.992566666667 | 0.494880437850952 | 0.324730392156863 | 0.0389417186379433 | 0.0638654554298779 | 5 |
| 765 | 764.997566666667 | 0.49289870262146 | 0.326381263616558 | 0.00791857298463583 | 0.0423236166808667 | 5 |
| 770 | 770.002566666667 | 0.60004198551178 | 0.264226579520697 | 0.118942260742188 | 0.424390035267684 | 5 |
| 775 | 775.007566666667 | 0.465698301792145 | 0.366687091503268 | 0.147062078118324 | 0.450120338422101 | 5 |
| 780 | 779.995883333333 | 0.462721139192581 | 0.372601851851852 | 0.02179847471416 | 0.0616250495353776 | 5 |
| 785 | 785.000883333333 | 0.472833126783371 | 0.363722222222222 | 0.0260078962892294 | 0.0814199051797344 | 5 |
| 790 | 790.005883333333 | 0.462866544723511 | 0.370906318082789 | 0.0373820774257183 | 0.0875562042147069 | 5 |
| 795 | 794.9942 | 0.48532247543335 | 0.335308278867102 | 0.0761933550238609 | 0.238368893819013 | 5 |
| 800 | 799.9992 | 0.475817263126373 | 0.345343137254902 | 0.085371732711792 | 0.220564228840892 | 5 |
| 805 | 805.0042 | 0.474406063556671 | 0.364269063180828 | 0.0625179782509804 | 0.16882532453981 | 5 |
| 810 | 809.992516666667 | 0.474200159311295 | 0.361330610021786 | 0.0326476022601128 | 0.0532331406805867 | 5 |
| 815 | 814.997516666667 | 0.458364933729172 | 0.362500816993464 | 0.0950040891766548 | 0.205366309165745 | 5 |
| 820 | 820.002516666667 | 0.45542785525322 | 0.363014161220044 | 0.0234882906079292 | 0.0320218148410648 | 5 |
| 825 | 825.007516666667 | 0.476526707410812 | 0.360912037037037 | 0.0940857902169228 | 0.215024401683203 | 5 |
| 830 | 829.995833333333 | 0.468535661697388 | 0.366677015250545 | 0.0291925389319658 | 0.0693505855363797 | 5 |
| 835 | 835.000833333333 | 0.491627186536789 | 0.336076525054466 | 0.0718518495559692 | 0.215817113871645 | 5 |
| 840 | 840.005833333333 | 0.469446092844009 | 0.36570697167756 | 0.0725590959191322 | 0.210854664768635 | 5 |
| 845 | 844.99415 | 0.475898176431656 | 0.362016612200436 | 0.0250147059559822 | 0.0527627724541728 | 5 |
| 850 | 849.99915 | 0.480395168066025 | 0.343033224400871 | 0.0646266266703606 | 0.173825981975052 | 5 |
| 855 | 855.00415 | 0.482354611158371 | 0.339493191721133 | 0.0301958043128252 | 0.0709242565046261 | 5 |
| 860 | 859.992466666667 | 0.478818088769913 | 0.36058660130719 | 0.072847492992878 | 0.168923613005085 | 5 |
| 865 | 864.997466666667 | 0.475725769996643 | 0.360749183006536 | 0.014945806004107 | 0.0304805287073919 | 5 |
| 870 | 870.002466666667 | 0.467843145132065 | 0.367078431372549 | 0.0244763065129519 | 0.0752615517844662 | 5 |
| 875 | 875.007466666667 | 0.484217315912247 | 0.336223039215686 | 0.0747102349996567 | 0.222499378045989 | 5 |
| 880 | 879.995783333333 | 0.479699909687042 | 0.361184368191721 | 0.0768965184688568 | 0.211935227482511 | 5 |
| 885 | 885.000783333333 | 0.465751379728317 | 0.368070261437908 | 0.026113560423255 | 0.0587686423312262 | 5 |
| 890 | 890.005783333333 | 0.480699062347412 | 0.343504357298475 | 0.0672799572348595 | 0.172057651798008 | 5 |
| 895 | 894.9941 | 0.488281071186066 | 0.334357298474945 | 0.0829436257481575 | 0.204936980938385 | 5 |
| 900 | 899.9991 | 0.47334885597229 | 0.360285130718954 | 0.069699615240097 | 0.208516864083517 | 5 |
| 905 | 905.0041 | 0.473254084587097 | 0.365834694989107 | 0.0288986917585135 | 0.0755637830021301 | 5 |
| 910 | 909.992416666667 | 0.475888341665268 | 0.362262527233115 | 0.0245928652584553 | 0.0648677395527535 | 5 |
| 915 | 914.997416666667 | 0.472482025623322 | 0.363897603485839 | 0.029256533831358 | 0.0690374995450429 | 5 |
| 920 | 920.002416666667 | 0.486603230237961 | 0.340727668845316 | 0.0642715096473694 | 0.161081867453031 | 5 |
| 925 | 925.007416666667 | 0.485983967781067 | 0.336788126361656 | 0.0928594768047333 | 0.211274686985847 | 5 |
| 930 | 929.995733333333 | 0.48773717880249 | 0.334942265795207 | 0.0279880184680223 | 0.0589623412160958 | 5 |
| 935 | 935.000733333333 | 0.463699072599411 | 0.359352941176471 | 0.0960882306098938 | 0.265586201049321 | 5 |
| 940 | 940.005733333333 | 0.475367099046707 | 0.34689188453159 | 0.0780656263232231 | 0.200354149211578 | 5 |
| 945 | 944.99405 | 0.485539793968201 | 0.309928921568627 | 0.112108930945396 | 0.306156037030519 | 5 |
| 950 | 949.99905 | 0.44680067896843 | 0.307460511982571 | 0.124626360833645 | 0.209825864227843 | 5 |
| 955 | 955.00405 | 0.323861926794052 | 0.342700980392157 | 0.132733941078186 | 0.400927753893961 | 5 |
| 960 | 959.992366666667 | 0.489836603403091 | 0.307079793028322 | 0.174687087535858 | 0.410528883240892 | 5 |
| 965 | 964.997366666667 | 0.511244595050812 | 0.310403867102396 | 0.0779624208807945 | 0.125801853066667 | 5 |
| 970 | 970.002366666667 | 0.469604283571243 | 0.303569716775599 | 0.0999272838234901 | 0.255421413174546 | 5 |
| 975 | 975.007366666667 | 0.469468146562576 | 0.304800381263617 | 0.0213415026664734 | 0.0453196690010207 | 5 |
| 980 | 979.995683333333 | 0.491535097360611 | 0.303976579520697 | 0.0786971673369408 | 0.14424769052173 | 5 |
| 985 | 985.000683333333 | 0.4799664914608 | 0.310066176470588 | 0.0243916101753712 | 0.0770906654211721 | 5 |
| 990 | 990.005683333333 | 0.470550686120987 | 0.303345860566449 | 0.0783107280731201 | 0.170596197550902 | 5 |
| 995 | 994.994 | 0.476104021072388 | 0.319844498910675 | 0.0828752741217613 | 0.156386879016422 | 5 |
| 1000 | 999.999 | 0.478853225708008 | 0.317876361655773 | 0.0449970029294491 | 0.055486132967186 | 5 |
| 1005 | 1005.004 | 0.494838774204254 | 0.312876633986928 | 0.0766925290226936 | 0.191101335567077 | 5 |
| 1010 | 1009.99231666667 | 0.46745565533638 | 0.304472494553377 | 0.0985324084758759 | 0.18080207742566 | 5 |
| 1015 | 1014.99731666667 | 0.487357050180435 | 0.309084694989107 | 0.083578422665596 | 0.173545659774488 | 5 |
| 1020 | 1020.00231666667 | 0.5084068775177 | 0.310518246187364 | 0.0804523378610611 | 0.198269731713024 | 5 |
| 1025 | 1025.00731666667 | 0.512398660182953 | 0.303201252723312 | 0.0321715660393238 | 0.0713066466787588 | 5 |
| 1030 | 1029.99563333333 | 0.48923122882843 | 0.304575980392157 | 0.0750307738780975 | 0.132811134500449 | 5 |
| 1035 | 1035.00063333333 | 0.489952087402344 | 0.304770424836601 | 0.0290601830929518 | 0.0469231671888312 | 5 |
| 1040 | 1040.00563333333 | 0.520344257354736 | 0.299564270152505 | 0.0907331183552742 | 0.184838104495224 | 5 |
| 1045 | 1044.99395 | 0.492674589157104 | 0.303770424836601 | 0.0929234623908997 | 0.176466483452409 | 5 |
| 1050 | 1049.99895 | 0.493967354297638 | 0.305080337690632 | 0.0290825162082911 | 0.0490310957770117 | 5 |
| 1055 | 1055.00395 | 0.493047684431076 | 0.301603213507625 | 0.0321015790104866 | 0.0511314604947591 | 5 |
| 1060 | 1059.99226666667 | 0.491337448358536 | 0.303432461873638 | 0.0304248370230198 | 0.0541790904314949 | 5 |
| 1065 | 1064.99726666667 | 0.511288404464722 | 0.306865196078431 | 0.0782598033547401 | 0.127787832205434 | 5 |
| 1070 | 1070.00226666667 | 0.505697727203369 | 0.307185729847495 | 0.0321898125112057 | 0.0699348467627826 | 5 |
| 1075 | 1075.00726666667 | 0.511949598789215 | 0.299987472766885 | 0.0484806671738625 | 0.0907704974619383 | 5 |
| 1080 | 1079.99558333333 | 0.47092592716217 | 0.302372276688453 | 0.105117917060852 | 0.249289230134934 | 5 |
| 1085 | 1085.00058333333 | 0.46870943903923 | 0.303222766884532 | 0.0220509245991707 | 0.0379074897599762 | 5 |
| 1090 | 1090.00558333333 | 0.469763308763504 | 0.322816721132898 | 0.082611121237278 | 0.176716624015626 | 5 |
| 1095 | 1094.9939 | 0.466821938753128 | 0.302828976034858 | 0.0850389450788498 | 0.155747927808676 | 5 |
| 1100 | 1099.9989 | 0.468640804290771 | 0.30470697167756 | 0.0277742370963097 | 0.0681085880479588 | 5 |
| 1105 | 1105.0039 | 0.461721420288086 | 0.311346949891068 | 0.0351781025528908 | 0.0599348553364969 | 5 |
| 1110 | 1109.99221666667 | 0.471341788768768 | 0.323243191721133 | 0.0839569717645645 | 0.151496613268528 | 5 |
| 1115 | 1114.99721666667 | 0.469309121370316 | 0.323200163398693 | 0.0188447702676058 | 0.040322089508256 | 5 |
| 1120 | 1120.00221666667 | 0.479546040296555 | 0.318082516339869 | 0.0341421589255333 | 0.0516577219170844 | 5 |
| 1125 | 1125.00721666667 | 0.470380455255508 | 0.306637254901961 | 0.0941857248544693 | 0.13443003886744 | 5 |
| 1130 | 1129.99553333333 | 0.46708557009697 | 0.303658224400871 | 0.0163570251315832 | 0.0580019292274485 | 5 |
| 1135 | 1135.00053333333 | 0.473015546798706 | 0.323035130718954 | 0.0941974371671677 | 0.159748995251106 | 5 |
| 1140 | 1140.00553333333 | 0.466934949159622 | 0.30387091503268 | 0.0762766823172569 | 0.147791382075719 | 5 |
| 1145 | 1144.99385 | 0.461977124214172 | 0.310794389978214 | 0.0281718410551548 | 0.0514659504897307 | 5 |
| 1150 | 1149.99885 | 0.468919664621353 | 0.305238017429194 | 0.0316587686538696 | 0.0713002663774995 | 5 |
| 1155 | 1155.00385 | 0.471506267786026 | 0.323209422657952 | 0.0906165540218353 | 0.152980042181794 | 5 |
| 1160 | 1159.99216666667 | 0.472794115543365 | 0.319102124183007 | 0.0389011465013027 | 0.0626477823489192 | 5 |
| 1165 | 1164.99716666667 | 0.465265244245529 | 0.303782407407407 | 0.0816470608115196 | 0.177661175406656 | 5 |
| 1170 | 1170.00216666667 | 0.466893821954727 | 0.302169662309368 | 0.0191699340939522 | 0.0341936531088238 | 5 |
| 1175 | 1175.00716666667 | 0.469576269388199 | 0.305946078431373 | 0.0753349661827087 | 0.108862372066258 | 5 |
| 1180 | 1179.99548333333 | 0.466916412115097 | 0.303148692810457 | 0.0752143189311028 | 0.105711903094075 | 5 |
| 1185 | 1185.00048333333 | 0.465194195508957 | 0.302865740740741 | 0.02072549238801 | 0.0434372890011192 | 5 |
| 1190 | 1190.00548333333 | 0.480524212121964 | 0.323540305010893 | 0.0813257098197937 | 0.179399708166461 | 5 |
| 1195 | 1194.9938 | 0.475660681724548 | 0.324908496732026 | 0.043861385434866 | 0.0811729395450263 | 5 |
| 1200 | 1199.9988 | 0.473784029483795 | 0.322214869281046 | 0.0386593118309975 | 0.0409253305576773 | 5 |
| 1205 | 1205.0038 | 0.468589335680008 | 0.305094498910675 | 0.0814806595444679 | 0.196407327697947 | 5 |
| 1210 | 1209.99211666667 | 0.465184390544891 | 0.301887254901961 | 0.0820841491222382 | 0.125954650948336 | 5 |
| 1215 | 1214.99711666667 | 0.476582229137421 | 0.319437636165577 | 0.0874136686325073 | 0.160064694093147 | 5 |
| 1220 | 1220.00211666667 | 0.467690646648407 | 0.323505991285403 | 0.0744504407048225 | 0.216193395393479 | 5 |
| 1225 | 1225.00711666667 | 0.469268262386322 | 0.305360838779956 | 0.0843853428959846 | 0.188851405234305 | 5 |
| 1230 | 1229.99543333333 | 0.462285965681076 | 0.30431045751634 | 0.0778129100799561 | 0.110756270046558 | 5 |
| 1235 | 1235.00043333333 | 0.466309636831284 | 0.301818899782135 | 0.0192551761865616 | 0.0332357428303297 | 5 |
| 1240 | 1240.00543333333 | 0.471767157316208 | 0.304636710239651 | 0.0835865959525108 | 0.117877651156781 | 5 |
| 1245 | 1244.99375 | 0.473084986209869 | 0.324667483660131 | 0.080480121076107 | 0.182042832864813 | 5 |
| 1250 | 1249.99875 | 0.467425674200058 | 0.325602396514161 | 0.0724980905652046 | 0.219068039923502 | 5 |
| 1255 | 1255.00375 | 0.477892935276031 | 0.321557734204793 | 0.0758861601352692 | 0.209037873765096 | 5 |
| 1260 | 1259.99206666667 | 0.47282001376152 | 0.324635348583878 | 0.0327799580991268 | 0.0527807407063031 | 5 |
| 1265 | 1264.99706666667 | 0.464596688747406 | 0.302857843137255 | 0.0821889936923981 | 0.172755869404105 | 5 |
| 1270 | 1270.00206666667 | 0.464496999979019 | 0.302243736383442 | 0.0269248373806477 | 0.0394640785293107 | 5 |
| 1275 | 1275.00706666667 | 0.466689318418503 | 0.310723039215686 | 0.0810299515724182 | 0.138556379259685 | 5 |
| 1280 | 1279.99538333333 | 0.470279157161713 | 0.323027233115468 | 0.0727342069149017 | 0.13957075749478 | 5 |
| 1285 | 1285.00038333333 | 0.469816446304321 | 0.305142973856209 | 0.0815727040171623 | 0.138108125722608 | 5 |
| 1290 | 1290.00538333333 | 0.468211859464645 | 0.30516802832244 | 0.00468246173113585 | 0.0245205864726308 | 5 |
| 1295 | 1294.9937 | 0.468103229999542 | 0.305480392156863 | 0.0230770688503981 | 0.0358298981563352 | 5 |
| 1300 | 1299.9987 | 0.476515799760818 | 0.322493736383442 | 0.0871157422661781 | 0.188601104769985 | 5 |
| 1305 | 1305.0037 | 0.475949108600616 | 0.321868191721133 | 0.00641802838072181 | 0.0225385010057261 | 5 |
| 1310 | 1309.99201666667 | 0.46282684803009 | 0.309240196078431 | 0.0797627940773964 | 0.18609797880469 | 5 |
| 1315 | 1314.99701666667 | 0.465616285800934 | 0.301933006535948 | 0.0795432925224304 | 0.140958105688416 | 5 |
| 1320 | 1320.00201666667 | 0.460468947887421 | 0.304156318082789 | 0.0213684625923634 | 0.0439657469668771 | 5 |
| 1325 | 1325.00701666667 | 0.468458384275436 | 0.305493736383442 | 0.0806614831089973 | 0.133658224693961 | 5 |
| 1330 | 1329.99533333333 | 0.469333320856094 | 0.305514705882353 | 0.0386614911258221 | 0.0640117760672044 | 5 |
| 1335 | 1335.00033333333 | 0.424982845783234 | 0.340646786492375 | 0.123637534677982 | 0.320109756420904 | 5 |
| 1340 | 1340.00533333333 | 0.417886972427368 | 0.343279411764706 | 0.0474934652447701 | 0.0603402760994942 | 5 |
| 1345 | 1344.99365 | 0.412201523780823 | 0.343131808278867 | 0.0163804460316896 | 0.0411879084042315 | 5 |
| 1350 | 1349.99865 | 0.459633708000183 | 0.310167483660131 | 0.12150789052248 | 0.327157120135554 | 5 |
| 1355 | 1355.00365 | 0.464652806520462 | 0.309387254901961 | 0.0226988010108471 | 0.0306799218901475 | 5 |
| 1360 | 1359.99196666667 | 0.470038115978241 | 0.321496187363834 | 0.0800318643450737 | 0.140792244754422 | 5 |
| 1365 | 1364.99696666667 | 0.46961709856987 | 0.321191721132898 | 0.0122135076671839 | 0.0227590800985042 | 5 |
| 1370 | 1370.00196666667 | 0.47716748714447 | 0.321422930283224 | 0.0401881821453571 | 0.0523911574317971 | 5 |
| 1375 | 1375.00696666667 | 0.46635103225708 | 0.302742102396514 | 0.092634528875351 | 0.173999957126383 | 5 |
| 1380 | 1379.99528333333 | 0.461051732301712 | 0.310236928104575 | 0.0772208571434021 | 0.139731995598988 | 5 |
| 1385 | 1385.00028333333 | 0.461104869842529 | 0.310213779956427 | 0.00471650343388319 | 0.0294787515612926 | 5 |
| 1390 | 1390.00528333333 | 0.413379609584808 | 0.343352668845316 | 0.119653321802616 | 0.330323490712029 | 5 |
| 1395 | 1394.9936 | 0.472211331129074 | 0.307915577342048 | 0.11599400639534 | 0.339751454550081 | 5 |
| 1400 | 1399.9986 | 0.472282141447067 | 0.305464324618736 | 0.00488888844847679 | 0.0381931371226232 | 5 |
| 1405 | 1405.0036 | 0.412461340427399 | 0.299935185185185 | 0.105010889470577 | 0.252001792784923 | 5 |
| 1410 | 1409.99191666667 | 0.469857037067413 | 0.310348311546841 | 0.0922600775957108 | 0.26255905532664 | 5 |
| 1415 | 1414.99691666667 | 0.47125107049942 | 0.309510620915033 | 0.0290226023644209 | 0.0397439020826266 | 5 |
| 1420 | 1420.00191666667 | 0.471027761697769 | 0.307345043572985 | 0.00581753859296441 | 0.0424058587446748 | 5 |
| 1425 | 1425.00691666667 | 0.479515790939331 | 0.31898720043573 | 0.0792984738945961 | 0.131436986191441 | 5 |
| 1430 | 1429.99523333333 | 0.480121999979019 | 0.318263616557734 | 0.0315718948841095 | 0.0571777598592828 | 5 |
| 1435 | 1435.00023333333 | 0.474713534116745 | 0.307294389978214 | 0.0817859470844269 | 0.118276105714662 | 5 |
| 1440 | 1440.00523333333 | 0.466149508953094 | 0.311981481481481 | 0.0319594219326973 | 0.0678413286503886 | 5 |
| 1445 | 1444.99355 | 0.484205037355423 | 0.315085784313725 | 0.0850931406021118 | 0.1590096073876 | 5 |
| 1450 | 1449.99855 | 0.48828649520874 | 0.321427832244009 | 0.0700133442878723 | 0.109649249933869 | 5 |
| 1455 | 1455.00355 | 0.46503758430481 | 0.310017973856209 | 0.0902946665883064 | 0.208962900521116 | 5 |
| 1460 | 1459.99186666667 | 0.470613330602646 | 0.309584967320261 | 0.0268572978675365 | 0.0544857492806895 | 5 |
| 1465 | 1464.99686666667 | 0.472496211528778 | 0.307255718954248 | 0.0317543558776379 | 0.0617933795557846 | 5 |
| 1470 | 1470.00186666667 | 0.471115171909332 | 0.304981481481481 | 0.00546160154044628 | 0.0367346762743983 | 5 |
| 1475 | 1475.00686666667 | 0.477036505937576 | 0.319901416122004 | 0.0881097391247749 | 0.135912295728901 | 5 |
| 1480 | 1479.99518333333 | 0.479343980550766 | 0.318815631808279 | 0.0163145419210196 | 0.0518329918899208 | 5 |
| 1485 | 1485.00018333333 | 0.477383434772491 | 0.320335784313726 | 0.0334321893751621 | 0.0571711135482361 | 5 |
| 1490 | 1490.00518333333 | 0.46123942732811 | 0.311328703703704 | 0.075632631778717 | 0.131798636112787 | 5 |
| 1495 | 1494.9935 | 0.470923781394958 | 0.305353213507625 | 0.0206554997712374 | 0.0855686923187053 | 5 |
| 1500 | 1499.9985 | 0.486885905265808 | 0.313634531590414 | 0.0802399218082428 | 0.123501738722089 | 5 |
| 1505 | 1505.0035 | 0.484770715236664 | 0.31043545751634 | 0.0343597494065762 | 0.0641591313144655 | 5 |
| 1510 | 1509.99181666667 | 0.464388102293015 | 0.313093409586057 | 0.0839577913284302 | 0.164933679909349 | 5 |
| 1515 | 1514.99681666667 | 0.465051472187042 | 0.30975 | 0.0102870371192694 | 0.0442797806734805 | 5 |
| 1520 | 1520.00181666667 | 0.473260372877121 | 0.304639978213508 | 0.0269686803221703 | 0.0698587355507664 | 5 |
| 1525 | 1525.00681666667 | 0.478864938020706 | 0.320487472766885 | 0.0865196064114571 | 0.122188257233904 | 5 |
| 1530 | 1529.99513333333 | 0.489142179489136 | 0.315456427015251 | 0.0364368185400963 | 0.0525762538789619 | 5 |
| 1535 | 1535.00013333333 | 0.473400056362152 | 0.322442538126362 | 0.0464588776230812 | 0.066751337250975 | 5 |
| 1540 | 1540.00513333333 | 0.469232320785522 | 0.307283769063181 | 0.0763894319534302 | 0.124321883526018 | 5 |
| 1545 | 1544.99345 | 0.470955073833466 | 0.309966775599128 | 0.00589542463421822 | 0.0444554293754923 | 5 |
| 1550 | 1549.99845 | 0.471934914588928 | 0.307153050108932 | 0.0292668826878071 | 0.0607821362309328 | 5 |
| 1555 | 1555.00345 | 0.477940082550049 | 0.319499455337691 | 0.0860601812601089 | 0.119988639164203 | 5 |
| 1560 | 1559.99176666667 | 0.473580896854401 | 0.304775326797386 | 0.0845928639173508 | 0.129534184854819 | 5 |
| 1565 | 1564.99676666667 | 0.473206460475922 | 0.304820261437909 | 0.00666584959253669 | 0.0276840366611613 | 5 |
| 1570 | 1570.00176666667 | 0.472845852375031 | 0.3045348583878 | 0.00559041416272521 | 0.0281149957566147 | 5 |
| 1575 | 1575.00676666667 | 0.479338526725769 | 0.318166666666667 | 0.0786789283156395 | 0.125045245888864 | 5 |
| 1580 | 1579.99508333333 | 0.476419419050217 | 0.318897875816993 | 0.0522361062467098 | 0.0615922546042527 | 5 |
| 1585 | 1585.00008333333 | 0.473554223775864 | 0.307731753812636 | 0.0860547348856926 | 0.125190652863187 | 5 |
| 1590 | 1590.00508333333 | 0.465177863836288 | 0.312154411764706 | 0.0347815901041031 | 0.0962831894697852 | 5 |
| 1595 | 1594.9934 | 0.47129413485527 | 0.307292755991285 | 0.026826523244381 | 0.0520620036729854 | 5 |
| 1600 | 1599.9984 | 0.479487210512161 | 0.31841802832244 | 0.0772715061903 | 0.133835326251867 | 5 |
| 1605 | 1605.0034 | 0.462758988142014 | 0.311246459694989 | 0.0769874751567841 | 0.131489283232951 | 5 |
| 1610 | 1609.99171666667 | 0.485805839300156 | 0.314174291938998 | 0.082206979393959 | 0.157613487817113 | 5 |
| 1615 | 1614.99671666667 | 0.516531586647034 | 0.538351307189542 | 0.0803793519735336 | 0.518613305307746 | 5 |
| 1620 | 1620.00171666667 | 0.497793585062027 | 0.320431644880174 | 0.0887380167841911 | 0.532164735383858 | 5 |
| 1625 | 1625.00671666667 | 0.500663161277771 | 0.315330337690632 | 0.0283466763794422 | 0.0753372750359515 | 5 |
| 1630 | 1629.99503333333 | 0.499153345823288 | 0.315433278867102 | 0.00288834422826767 | 0.0157106924116334 | 5 |
| 1635 | 1635.00003333333 | 0.497779130935669 | 0.314693355119826 | 0.0979357212781906 | 0.15204844610817 | 5 |
| 1640 | 1640.00503333333 | 0.499930858612061 | 0.315552287581699 | 0.0957595333456993 | 0.149895667972007 | 5 |
| 1645 | 1644.99335 | 0.578592598438263 | 0.260666394335512 | 0.0913861617445946 | 0.3555208821433 | 5 |
| 1650 | 1649.99835 | 0.499689847230911 | 0.307887254901961 | 0.119865730404854 | 0.374089485524364 | 5 |
| 1655 | 1655.00335 | 0.496189296245575 | 0.320589052287582 | 0.110997281968594 | 0.25383601992134 | 5 |
| 1660 | 1659.99166666667 | 0.500932455062866 | 0.317206427015251 | 0.0298913381993771 | 0.0701553934194144 | 5 |
| 1665 | 1664.99666666667 | 0.499783486127853 | 0.316966775599129 | 0.0308624710887671 | 0.065434062160918 | 5 |
| 1670 | 1670.00166666667 | 0.499701797962189 | 0.316962690631808 | 0.00419389922171831 | 0.0158650804600532 | 5 |
| 1675 | 1675.00666666667 | 0.499011427164078 | 0.317950980392157 | 0.0407077856361866 | 0.0743736914988211 | 5 |
| 1680 | 1679.99498333333 | 0.49289733171463 | 0.320805555555556 | 0.0928918868303299 | 0.143795330819906 | 5 |
| 1685 | 1684.99998333333 | 0.501196384429932 | 0.31788371459695 | 0.088539220392704 | 0.136524609430013 | 5 |
| 1690 | 1690.00498333333 | 0.497364938259125 | 0.32084068627451 | 0.0193090960383415 | 0.0346815767747993 | 5 |
| 1695 | 1694.9933 | 0.663835227489471 | 0.239449891067538 | 0.167415291070938 | 0.455886061167971 | 5 |
| 1700 | 1699.9983 | 0.663842380046844 | 0.239535130718954 | 0.00101960788015276 | 0.0209046455690926 | 5 |
| 1705 | 1705.0033 | 0.496859222650528 | 0.317044662309368 | 0.167202606797218 | 0.397013019032375 | 5 |
| 1710 | 1710.0083 | 0.496185511350632 | 0.317519880174292 | 0.0381661206483841 | 0.0554704600744084 | 5 |
| 1715 | 1714.99661666667 | 0.497612774372101 | 0.316613017429194 | 0.0405432991683483 | 0.0423663346618788 | 5 |
| 1720 | 1720.00161666667 | 0.494396299123764 | 0.318828159041394 | 0.093884252011776 | 0.136846810004569 | 5 |
| 1725 | 1725.00661666667 | 0.499434679746628 | 0.320648148148148 | 0.0272851306945086 | 0.0531359267562489 | 5 |
| 1730 | 1729.99493333333 | 0.500729858875275 | 0.317380718954248 | 0.0300185177475214 | 0.0562892190521394 | 5 |
| 1735 | 1734.99993333333 | 0.500209152698517 | 0.315311546840959 | 0.00919662229716778 | 0.0402900194544343 | 5 |
| 1740 | 1740.00493333333 | 0.494962424039841 | 0.315940904139434 | 0.097064808011055 | 0.137494747502343 | 5 |
| 1745 | 1744.99325 | 0.495061576366425 | 0.321554738562091 | 0.0882706940174103 | 0.151799074747583 | 5 |
| 1750 | 1749.99825 | 0.494509011507034 | 0.320281862745098 | 0.0174795761704445 | 0.03727939097728 | 5 |
| 1755 | 1755.00325 | 0.491889983415604 | 0.323947984749455 | 0.0286914482712746 | 0.0531389840528756 | 5 |
| 1760 | 1760.00825 | 0.490992367267609 | 0.323188725490196 | 0.0170610006898642 | 0.0344435234988547 | 5 |
| 1765 | 1764.99656666667 | 0.504776418209076 | 0.312157679738562 | 0.0946059301495552 | 0.168711563731155 | 5 |
| 1770 | 1770.00156666667 | 0.491383731365204 | 0.320838507625272 | 0.0461612194776535 | 0.0966606633106873 | 5 |
| 1775 | 1775.00656666667 | 0.504526972770691 | 0.326925108932462 | 0.0923790857195854 | 0.241081590177484 | 5 |
| 1780 | 1779.99488333333 | 0.510240733623505 | 0.32358197167756 | 0.0347039736807346 | 0.0890048935472696 | 5 |
| 1785 | 1784.99988333333 | 0.503877997398376 | 0.324377723311547 | 0.0716960802674294 | 0.159114718971603 | 5 |
| 1790 | 1790.00488333333 | 0.498743504285812 | 0.387624455337691 | 0.0778044611215591 | 0.446490827234445 | 5 |
| 1795 | 1794.9932 | 0.502914011478424 | 0.330049836601307 | 0.0756732001900673 | 0.439489571797995 | 5 |
| 1800 | 1799.9982 | 0.505987465381622 | 0.327911220043573 | 0.0286209154874086 | 0.0475546073395776 | 5 |
| 1805 | 1805.0032 | 0.506107866764069 | 0.326580882352941 | 0.00959586072713137 | 0.0451212541291859 | 5 |
| 1810 | 1810.0082 | 0.504653632640839 | 0.322015250544662 | 0.0631928071379662 | 0.137360928432281 | 5 |
| 1815 | 1814.99651666667 | 0.512326240539551 | 0.325572440087146 | 0.0736247226595879 | 0.145691838959016 | 5 |
| 1820 | 1820.00151666667 | 0.504102349281311 | 0.32831045751634 | 0.0289743971079588 | 0.0728482902876708 | 5 |
| 1825 | 1825.00651666667 | 0.512957513332367 | 0.325837962962963 | 0.0324433520436287 | 0.060932604937441 | 5 |
| 1830 | 1829.99483333333 | 0.509015023708344 | 0.325274782135076 | 0.0224082246422768 | 0.0486362834028944 | 5 |
| 1835 | 1834.99983333333 | 0.508754074573517 | 0.325184640522876 | 0.00550980400294065 | 0.026191198613303 | 5 |
| 1840 | 1840.00483333333 | 0.507105112075806 | 0.320212962962963 | 0.0687393769621849 | 0.148976383858737 | 5 |
| 1845 | 1844.99315 | 0.504005193710327 | 0.324052559912854 | 0.0361358933150768 | 0.0441435421525461 | 5 |
| 1850 | 1849.99815 | 0.503535985946655 | 0.324882080610022 | 0.0117012532427907 | 0.033154627085163 | 5 |
| 1855 | 1855.00315 | 0.501422107219696 | 0.331754357298475 | 0.0609967336058617 | 0.140522620684069 | 5 |
| 1860 | 1860.00815 | 0.501447439193726 | 0.331095315904139 | 0.00964188482612371 | 0.0285344889811813 | 5 |
| 1865 | 1864.99646666667 | 0.510855436325073 | 0.328341230936819 | 0.0295234210789204 | 0.0373635137036422 | 5 |
| 1870 | 1870.00146666667 | 0.509721696376801 | 0.322720860566449 | 0.0371778309345245 | 0.0902871068053904 | 5 |
| 1875 | 1875.00646666667 | 0.508671283721924 | 0.321727396514161 | 0.0728439465165138 | 0.167214454685695 | 5 |
| 1880 | 1879.99478333333 | 0.50970047712326 | 0.318886437908497 | 0.0325079001486301 | 0.0771176127096111 | 5 |
| 1885 | 1884.99978333333 | 0.499681383371353 | 0.331427287581699 | 0.0710501074790955 | 0.154150192659425 | 5 |
| 1890 | 1890.00478333333 | 0.499398112297058 | 0.331346949891068 | 0.00520588224753737 | 0.0290831082459075 | 5 |
| 1895 | 1894.9931 | 0.506287574768066 | 0.328376089324619 | 0.0226356200873852 | 0.0402611971406694 | 5 |
| 1900 | 1899.9981 | 0.501684367656708 | 0.324804738562092 | 0.0746865421533585 | 0.13386719158438 | 5 |
| 1905 | 1905.0031 | 0.505614697933197 | 0.331333061002179 | 0.0710114389657974 | 0.132123157079472 | 5 |
| 1910 | 1910.0081 | 0.508633434772491 | 0.324838779956427 | 0.0400117076933384 | 0.0906564708136709 | 5 |
| 1915 | 1914.99641666667 | 0.511026978492737 | 0.328260076252723 | 0.0351745635271072 | 0.0758551320036202 | 5 |
| 1920 | 1920.00141666667 | 0.510475993156433 | 0.32861165577342 | 0.0072312094271183 | 0.025150320179727 | 5 |
| 1925 | 1925.00641666667 | 0.505667746067047 | 0.330449891067538 | 0.0176851861178875 | 0.0410829387178822 | 5 |
| 1930 | 1929.99473333333 | 0.507516324520111 | 0.321471949891068 | 0.0713932439684868 | 0.14991928505948 | 5 |
| 1935 | 1934.99973333333 | 0.507845878601074 | 0.319963779956427 | 0.0446824617683887 | 0.0454156701045173 | 5 |
| 1940 | 1940.00473333333 | 0.504179239273071 | 0.327888888888889 | 0.0690522864460945 | 0.148090044310666 | 5 |
| 1945 | 1944.99305 | 0.510870337486267 | 0.326997549019608 | 0.0264901947230101 | 0.0495379056237072 | 5 |
| 1950 | 1949.99805 | 0.511364638805389 | 0.326666666666667 | 0.00703839818015695 | 0.0379582011432412 | 5 |
| 1955 | 1955.00305 | 0.512549042701721 | 0.322730392156863 | 0.0264861080795527 | 0.0627777375615775 | 5 |
| 1960 | 1960.00805 | 0.503489911556244 | 0.330590958605665 | 0.025486109778285 | 0.0790728885864073 | 5 |
| 1965 | 1964.99636666667 | 0.500998079776764 | 0.330804738562092 | 0.0211100224405527 | 0.0468876748979278 | 5 |
| 1970 | 1970.00136666667 | 0.505451500415802 | 0.32901688453159 | 0.0208755452185869 | 0.0425111728368268 | 5 |
| 1975 | 1975.00636666667 | 0.512034893035889 | 0.326065904139434 | 0.0250642690807581 | 0.0485610370215625 | 5 |
| 1980 | 1979.99468333333 | 0.510674297809601 | 0.321461328976035 | 0.0853213518857956 | 0.241346703222344 | 5 |
| 1985 | 1984.99968333333 | 0.442758172750473 | 0.298374727668845 | 0.1004918217659 | 0.312161799088008 | 5 |
| 1990 | 1990.00468333333 | 0.50191992521286 | 0.329595315904139 | 0.109558820724487 | 0.309136842964767 | 5 |
| 1995 | 1994.993 | 0.504257082939148 | 0.32313371459695 | 0.0748197138309479 | 0.151500968606529 | 5 |
| 2000 | 1999.998 | 0.511016309261322 | 0.322266339869281 | 0.0797429233789444 | 0.147949074807028 | 5 |
| 2005 | 2005.003 | 0.509153604507446 | 0.326037581699346 | 0.0214041396975517 | 0.0496153459820003 | 5 |
| 2010 | 2010.008 | 0.512043297290802 | 0.319853758169935 | 0.0711429715156555 | 0.150572045482339 | 5 |
| 2015 | 2014.99631666667 | 0.505598545074463 | 0.320364379084967 | 0.0318831689655781 | 0.0673104092193355 | 5 |
| 2020 | 2020.00131666667 | 0.506736636161804 | 0.330859749455338 | 0.0685051754117012 | 0.150426393503876 | 5 |
| 2025 | 2025.00631666667 | 0.505476057529449 | 0.330415032679739 | 0.0067017967812717 | 0.03067647917881 | 5 |
| 2030 | 2029.99463333333 | 0.512661516666412 | 0.325825708061002 | 0.0266990754753351 | 0.0575902999847737 | 5 |
| 2035 | 2034.99963333333 | 0.505577385425568 | 0.329252723311547 | 0.0280857849866152 | 0.0630125313933464 | 5 |
| 2040 | 2040.00463333333 | 0.512137830257416 | 0.32535811546841 | 0.022448256611824 | 0.0477895539538405 | 5 |
| 2045 | 2044.99295 | 0.511156916618347 | 0.321936819172113 | 0.00709858350455761 | 0.0429165553926431 | 5 |
| 2050 | 2049.99795 | 0.501225233078003 | 0.330144335511983 | 0.0266996175050735 | 0.0670739333324701 | 5 |
| 2055 | 2055.00295 | 0.489702880382538 | 0.324683823529412 | 0.0838039144873619 | 0.189059433648671 | 5 |
| 2060 | 2060.00795 | 0.509271025657654 | 0.326307461873638 | 0.0927581712603569 | 0.160679582213613 | 5 |
| 2065 | 2064.99626666667 | 0.513145387172699 | 0.334203703703704 | 0.0875345841050148 | 0.151608521690426 | 5 |
| 2070 | 2070.00126666667 | 0.511335253715515 | 0.330804738562092 | 0.0204256549477577 | 0.0520346290504263 | 5 |
| 2075 | 2075.00626666667 | 0.50952672958374 | 0.329502450980392 | 0.0730901435017586 | 0.137351725911762 | 5 |
| 2080 | 2079.99458333333 | 0.500042796134949 | 0.331231753812636 | 0.123492635786533 | 0.185596698912879 | 5 |
| 2085 | 2084.99958333333 | 0.464101314544678 | 0.339199618736383 | 0.132267698645592 | 0.155470964136802 | 5 |
| 2090 | 2090.00458333333 | 0.509691476821899 | 0.32565522875817 | 0.12928295135498 | 0.215631723653484 | 5 |
| 2095 | 2094.9929 | 0.498159319162369 | 0.336270697167756 | 0.0762848556041718 | 0.149821002586986 | 5 |
| 2100 | 2099.9979 | 0.50455367565155 | 0.324165032679739 | 0.114666663110256 | 0.191555030768121 | 5 |
| 2105 | 2105.0029 | 0.508576512336731 | 0.32256508714597 | 0.0626710206270218 | 0.0477665964304389 | 5 |
| 2110 | 2110.0079 | 0.501038372516632 | 0.330734204793028 | 0.101779408752918 | 0.167582841520412 | 5 |
| 2115 | 2114.99621666667 | 0.496390014886856 | 0.332749183006536 | 0.0265803374350071 | 0.0378646600133026 | 5 |
| 2120 | 2120.00121666667 | 0.491127997636795 | 0.339217047930283 | 0.0963578447699547 | 0.190544286602747 | 5 |
| 2125 | 2125.00621666667 | 0.464527785778046 | 0.406754901960784 | 0.100251637399197 | 0.321763402103704 | 5 |
| 2130 | 2129.99453333333 | 0.472338795661926 | 0.409729575163399 | 0.0395773388445377 | 0.0818621174485879 | 5 |
| 2135 | 2134.99953333333 | 0 | 0 | 0.472338795661926 | 0.980261802328562 | 5 |
| 2140 | 2140.00453333333 | 0.332677274942398 | 0.47949128540305 | 0.332677274942398 | 0.71104625195229 | 5 |
| 2145 | 2144.99285 | 0.255158483982086 | 0.501090413943355 | 0.223506271839142 | 0.700692271012983 | 5 |
| 2150 | 2149.99785 | 0.197983935475349 | 0.617192538126362 | 0.206633701920509 | 0.555931874083658 | 5 |
| 2155 | 2155.00285 | 0.272012799978256 | 0.473813725490196 | 0.187269061803818 | 0.489645758235929 | 5 |
| 2160 | 2160.00785 | 0.19688481092453 | 0.658393790849673 | 0.222110033035278 | 0.607446519823795 | 5 |
| 2165 | 2164.99616666667 | 0.258084714412689 | 0.465876633986928 | 0.166742920875549 | 0.544514841480494 | 5 |
| 2170 | 2170.00116666667 | 0.536698281764984 | 0.316388071895425 | 0.409297674894333 | 0.762564097697183 | 5 |
| 2175 | 2175.00616666667 | 0.536006510257721 | 0.313515250544662 | 0.088456429541111 | 0.132243460792948 | 5 |
| 2180 | 2179.99448333333 | 0.535125017166138 | 0.311320261437909 | 0.0092464592307806 | 0.0452026859988677 | 5 |
| 2185 | 2184.99948333333 | 0.443489640951157 | 0.298947712418301 | 0.116491548717022 | 0.361130621611492 | 5 |
| 2190 | 2190.00448333333 | 0.530075132846832 | 0.320202614379085 | 0.131889969110489 | 0.386160365898165 | 5 |
| 2195 | 2194.9928 | 0.52963924407959 | 0.31502614379085 | 0.0888314247131348 | 0.132743689654437 | 5 |
| 2200 | 2199.9978 | 0.51163786649704 | 0.341550925925926 | 0.106097765266895 | 0.238126797155495 | 5 |
| 2205 | 2205.0028 | 0.50231671333313 | 0.339804738562092 | 0.0785019099712372 | 0.143490819641772 | 5 |
| 2210 | 2210.0078 | 0.503992676734924 | 0.338033224400871 | 0.0371862724423409 | 0.0634314058872456 | 5 |
| 2215 | 2214.99611666667 | 0.514338493347168 | 0.342621459694989 | 0.0816100239753723 | 0.148482907626852 | 5 |
| 2220 | 2220.00111666667 | 0.512975215911865 | 0.340759259259259 | 0.00555337686091661 | 0.0465588938481491 | 5 |
| 2225 | 2225.00611666667 | 0.513559937477112 | 0.342101579520697 | 0.0295748896896839 | 0.063065813461312 | 5 |
| 2230 | 2229.99443333333 | 0.513401448726654 | 0.342301198257081 | 0.00157625274732709 | 0.0128037127379131 | 5 |
| 2235 | 2234.99943333333 | 0.508665919303894 | 0.346312363834423 | 0.0276391599327326 | 0.0714520367066693 | 5 |
| 2240 | 2240.00443333333 | 0.510549604892731 | 0.343888616557734 | 0.0341789200901985 | 0.087985503537016 | 5 |
| 2245 | 2244.99275 | 0.503524482250214 | 0.346133442265795 | 0.0227499976754189 | 0.088774988067971 | 5 |
| 2250 | 2249.99775 | 0.503022313117981 | 0.346183823529412 | 0.00314542488195002 | 0.0327258884877701 | 5 |
| 2255 | 2255.00275 | 0.514421343803406 | 0.341846949891068 | 0.0311233643442392 | 0.0718181082446822 | 5 |
| 2260 | 2260.00775 | 0.513753831386566 | 0.341545751633987 | 0.00397685170173645 | 0.0160292875111604 | 5 |
| 2265 | 2264.99606666667 | 0.514986395835876 | 0.341626906318083 | 0.00463180849328637 | 0.0299134645726923 | 5 |
| 2270 | 2270.00106666667 | 0.506426751613617 | 0.348239923747277 | 0.0303581152111292 | 0.0601771050659577 | 5 |
| 2275 | 2275.00606666667 | 0.495879918336868 | 0.343360566448802 | 0.0670904144644737 | 0.150670402766846 | 5 |
| 2280 | 2279.99438333333 | 0.509849667549133 | 0.345608660130719 | 0.068277508020401 | 0.143906705483992 | 5 |
| 2285 | 2284.99938333333 | 0.50091153383255 | 0.351227941176471 | 0.0300155244767666 | 0.0446933554439942 | 5 |
| 2290 | 2290.00438333333 | 0.501237154006958 | 0.348964324618736 | 0.00594771234318614 | 0.0410810167262656 | 5 |
| 2295 | 2294.9927 | 0.504648685455322 | 0.337133169934641 | 0.0760596394538879 | 0.161055351522344 | 5 |
| 2300 | 2299.9977 | 0.4946149289608 | 0.34551279956427 | 0.0426367111504078 | 0.0711360013153681 | 5 |
| 2305 | 2305.0027 | 0.493642181158066 | 0.346138616557734 | 0.0115555552765727 | 0.0310667004125954 | 5 |
| 2310 | 2310.0077 | 0.504595041275024 | 0.345968409586057 | 0.072494275867939 | 0.148531086213038 | 5 |
| 2315 | 2314.99601666667 | 0.508019626140594 | 0.345941993464052 | 0.0226364396512508 | 0.0485459450746158 | 5 |
| 2320 | 2320.00101666667 | 0.507803082466125 | 0.345835511982571 | 0.00308687379583716 | 0.0296172790532831 | 5 |
| 2325 | 2325.00601666667 | 0.506991565227509 | 0.343926198257081 | 0.00648965081200004 | 0.0401971040158489 | 5 |
| 2330 | 2329.99433333333 | 0.499890238046646 | 0.337601579520697 | 0.0768861621618271 | 0.152488997535025 | 5 |
| 2335 | 2334.99933333333 | 0.493937909603119 | 0.345256808278867 | 0.0208815354853868 | 0.0752504627902097 | 5 |
| 2340 | 2340.00433333333 | 0.513609766960144 | 0.342142973856209 | 0.0817502737045288 | 0.149271228243887 | 5 |
| 2345 | 2344.99265 | 0.501677274703979 | 0.349953159041394 | 0.0209362749010324 | 0.0801470475182714 | 5 |
| 2350 | 2349.99765 | 0.506610333919525 | 0.346424019607843 | 0.0314972773194313 | 0.04223097613091 | 5 |
| 2355 | 2355.00265 | 0.506879866123199 | 0.346647058823529 | 0.00632189540192485 | 0.0242721571685773 | 5 |
| 2360 | 2360.00765 | 0.5102459192276 | 0.343443899782135 | 0.0327587127685547 | 0.0819823427960079 | 5 |
| 2365 | 2364.99596666667 | 0.511296570301056 | 0.341299291938998 | 0.00688670994713902 | 0.0480877226476325 | 5 |
| 2370 | 2370.00096666667 | 0.505539238452911 | 0.336071078431373 | 0.0809970125555992 | 0.154135885874169 | 5 |
| 2375 | 2375.00596666667 | 0.497604876756668 | 0.343434368191721 | 0.0338134504854679 | 0.0487124525924952 | 5 |
| 2380 | 2379.99428333333 | 0.510274231433868 | 0.343695533769063 | 0.0755533799529076 | 0.128569054490512 | 5 |
| 2385 | 2384.99928333333 | 0.50775820016861 | 0.346089869281046 | 0.0244561526924372 | 0.0462347206747305 | 5 |
| 2390 | 2390.00428333333 | 0.514831960201263 | 0.342780773420479 | 0.0234844759106636 | 0.0380020374728256 | 5 |
| 2395 | 2394.9926 | 0.514736652374268 | 0.342393790849673 | 0.00501089310273528 | 0.0287366622676196 | 5 |
| 2400 | 2399.9976 | 0.504161179065704 | 0.34707788671024 | 0.0271881781518459 | 0.0439847194795358 | 5 |
| 2405 | 2405.0026 | 0.508694171905518 | 0.343460784313725 | 0.0273434109985828 | 0.0751766926696663 | 5 |
| 2410 | 2410.0076 | 0.508677542209625 | 0.343515250544662 | 0.00446486892178655 | 0.025018991390953 | 5 |
| 2415 | 2414.99591666667 | 0.505521774291992 | 0.348416666666667 | 0.0380452051758766 | 0.0770492026489739 | 5 |
| 2420 | 2420.00091666667 | 0.503671288490295 | 0.348168845315904 | 0.00593436835333705 | 0.0365416767989395 | 5 |
| 2425 | 2425.00591666667 | 0.4955133497715 | 0.344644063180828 | 0.0730931460857391 | 0.142290350066094 | 5 |
| 2430 | 2429.99423333333 | 0.497984200716019 | 0.344408769063181 | 0.0271342601627111 | 0.0515396285469927 | 5 |
| 2435 | 2434.99923333333 | 0.493961304426193 | 0.3410348583878 | 0.0490196049213409 | 0.087753485873241 | 5 |
| 2440 | 2440.00423333333 | 0.501112461090088 | 0.349645152505447 | 0.0772932916879654 | 0.157147420528076 | 5 |
| 2445 | 2444.99255 | 0.511772871017456 | 0.341625816993464 | 0.022999182343483 | 0.057986769662517 | 5 |
| 2450 | 2449.99755 | 0.514695286750793 | 0.342716230936819 | 0.0113047380000353 | 0.031916368076843 | 5 |
| 2455 | 2455.00255 | 0.507231771945953 | 0.345517973856209 | 0.032773420214653 | 0.0681861506751764 | 5 |
| 2460 | 2460.00755 | 0.507104814052582 | 0.345703431372549 | 0.00148148136213422 | 0.0165268004154673 | 5 |
| 2465 | 2464.99586666667 | 0.512821912765503 | 0.343010348583878 | 0.0234398134052753 | 0.0369915322014999 | 5 |
| 2470 | 2470.00086666667 | 0.508356213569641 | 0.344675653594771 | 0.0217892155051231 | 0.0325464684098301 | 5 |
| 2475 | 2475.00586666667 | 0.489778846502304 | 0.350270697167756 | 0.0722129642963409 | 0.141902384595179 | 5 |
| 2480 | 2479.99418333333 | 0.490354031324387 | 0.35011628540305 | 0.0123981488868594 | 0.0277247192108105 | 5 |
| 2485 | 2484.99918333333 | 0.498034060001373 | 0.342812908496732 | 0.0346451513469219 | 0.0558680983154588 | 5 |
| 2490 | 2490.00418333333 | 0.504184067249298 | 0.336669934640523 | 0.043197438120842 | 0.0534424668559626 | 5 |
| 2495 | 2494.9925 | 0.505990207195282 | 0.344174564270152 | 0.0760533735156059 | 0.156368593086871 | 5 |
| 2500 | 2499.9975 | 0.504062652587891 | 0.347355664488017 | 0.0206868201494217 | 0.0578985162925344 | 5 |
| 2505 | 2505.0025 | 0.499719500541687 | 0.341156862745098 | 0.0781710222363472 | 0.1469877423 | 5 |
| 2510 | 2510.0075 | 0.497695863246918 | 0.343250544662309 | 0.0336696617305279 | 0.0733478032204372 | 5 |
| 2515 | 2514.99581666667 | 0.500213265419006 | 0.33925 | 0.0327581688761711 | 0.0507018012199325 | 5 |
| 2520 | 2520.00081666667 | 0.451788663864136 | 0.308303376906318 | 0.101422920823097 | 0.354964289152167 | 5 |
| 2525 | 2525.00581666667 | 0.514219760894775 | 0.340847222222222 | 0.123861379921436 | 0.358131523305849 | 5 |
| 2530 | 2529.99413333333 | 0.513768553733826 | 0.340681644880174 | 0.00466421572491527 | 0.0265842074025441 | 5 |
| 2535 | 2534.99913333333 | 0.506570279598236 | 0.338578703703704 | 0.0823360532522202 | 0.1487457628462 | 5 |
| 2540 | 2540.00413333333 | 0.504934668540955 | 0.338073529411765 | 0.00972494576126337 | 0.0295787208409548 | 5 |
| 2545 | 2544.99245 | 0.51453161239624 | 0.344150054466231 | 0.0789754912257195 | 0.150396578718514 | 5 |
| 2550 | 2549.99745 | 0.502533495426178 | 0.346385893246187 | 0.026761706918478 | 0.0558192055447911 | 5 |
| 2555 | 2555.00245 | 0.512466788291931 | 0.341746187363834 | 0.0264311004430056 | 0.0729534659060411 | 5 |
| 2560 | 2560.00745 | 0.499259531497955 | 0.341373366013072 | 0.0792747810482979 | 0.145769969494296 | 5 |
| 2565 | 2564.99576666667 | 0.500370919704437 | 0.33875462962963 | 0.0135988555848598 | 0.0450482724487233 | 5 |
| 2570 | 2570.00076666667 | 0.489281624555588 | 0.341757352941176 | 0.0780642703175545 | 0.137720364439436 | 5 |
| 2575 | 2575.00576666667 | 0.502390503883362 | 0.323043572984749 | 0.0758790820837021 | 0.247706655129069 | 5 |
| 2580 | 2579.99408333333 | 0.515929400920868 | 0.341358932461874 | 0.0811097398400307 | 0.283764679099543 | 5 |
| 2585 | 2584.99908333333 | 0.437695562839508 | 0.310827614379085 | 0.114828154444695 | 0.41030846392915 | 5 |
| 2590 | 2590.00408333333 | 0.487447708845139 | 0.342643790849673 | 0.101578429341316 | 0.361097673389303 | 5 |
| 2595 | 2594.9924 | 0.49450820684433 | 0.332850217864924 | 0.0473398678004742 | 0.0988975790463369 | 5 |
| 2600 | 2599.9974 | 0.519042253494263 | 0.328668572984749 | 0.0811233669519424 | 0.164434459662713 | 5 |
| 2605 | 2605.0024 | 0.527078449726105 | 0.319382897603486 | 0.0635917708277702 | 0.0656699343726123 | 5 |
| 2610 | 2610.0074 | 0.50812041759491 | 0.334087962962963 | 0.104053921997547 | 0.172997132514303 | 5 |
| 2615 | 2614.99571666667 | 0.524538695812225 | 0.320218137254902 | 0.0648235306143761 | 0.103020136579864 | 5 |
| 2620 | 2620.00071666667 | 0.505517959594727 | 0.336723311546841 | 0.0971987992525101 | 0.12298999340781 | 5 |
| 2625 | 2625.00571666667 | 0.488723307847977 | 0.344325708061002 | 0.111304454505444 | 0.215328765789532 | 5 |
| 2630 | 2629.99403333333 | 0.499117940664291 | 0.336947440087146 | 0.0556843653321266 | 0.100165646505532 | 5 |
| 2635 | 2634.99903333333 | 0.549286544322968 | 0.30903894335512 | 0.121525324881077 | 0.242583831526265 | 5 |
| 2640 | 2640.00403333333 | 0.480624735355377 | 0.343070261437908 | 0.135318085551262 | 0.229627148578807 | 5 |
| 2645 | 2644.99235 | 0.480697154998779 | 0.343203431372549 | 0.0274907406419516 | 0.0406244889902881 | 5 |
| 2650 | 2649.99735 | 0.174639448523521 | 0.379169389978214 | 0.306779980659485 | 0.80541475147235 | 5 |
| 2655 | 2655.00235 | 0.457466274499893 | 0.124669117647059 | 0.291261464357376 | 0.716215695469395 | 5 |
| 2660 | 2660.00735 | 0.1851696819067 | 0.64999537037037 | 0.290151715278625 | 0.831042086308482 | 5 |
| 2665 | 2664.99566666667 | 0.188752457499504 | 0.657964596949891 | 0.111489661037922 | 0.217458485974274 | 5 |
| 2670 | 2670.00066666667 | 0.387848645448685 | 0.610760348583878 | 0.210126653313637 | 0.731607075771305 | 5 |
| 2675 | 2675.00566666667 | 0.595541179180145 | 0.373142973856209 | 0.45264133810997 | 0.648245305311886 | 5 |
| 2680 | 2679.99398333333 | 0.762275576591492 | 0.188449074074074 | 0.201000288128853 | 0.444866280752336 | 5 |
| 2685 | 2684.99898333333 | 0.820094287395477 | 0.127641339869281 | 0.218858912587166 | 0.568042867028188 | 5 |
| 2690 | 2690.00398333333 | 0.771851599216461 | 0.103520969498911 | 0.182892963290215 | 0.358178687741248 | 5 |
| 2695 | 2694.9923 | 0.809424579143524 | 0.0998510348583878 | 0.149589881300926 | 0.272230695822833 | 5 |
| 2700 | 2699.9973 | 0.582767724990845 | 0.475482298474946 | 0.260310471057892 | 0.670456541787201 | 5 |
| 2705 | 2705.0023 | 0.583400070667267 | 0.479863017429194 | 0.119179204106331 | 0.377666992037127 | 5 |
| 2710 | 2710.0073 | 0.711018800735474 | 0.165405773420479 | 0.171219512820244 | 0.706240175972077 | 5 |
| 2715 | 2714.99561666667 | 0.74624103307724 | 0.111857298474946 | 0.161328434944153 | 0.331903421728056 | 5 |
| 2720 | 2720.00061666667 | 0.639482021331787 | 0.343149509803922 | 0.18549644947052 | 0.674818789863537 | 5 |
| 2725 | 2725.00561666667 | 0.848794102668762 | 0.36174537037037 | 0.25826308131218 | 0.693696675902558 | 5 |
| 2730 | 2729.99393333333 | 0.795103192329407 | 0.165337690631808 | 0.126244828104973 | 0.657329085893484 | 5 |
| 2735 | 2734.99893333333 | 0.786231815814972 | 0.127351579520697 | 0.162928640842438 | 0.483584946626221 | 5 |
| 2740 | 2740.00393333333 | 0.633959710597992 | 0.316660403050109 | 0.192919105291367 | 0.58774584786091 | 5 |
| 2745 | 2744.99225 | 0.795399308204651 | 0.138873638344227 | 0.215282142162323 | 0.590112683148533 | 5 |
| 2750 | 2749.99725 | 0.795910120010376 | 0.138825708061002 | 0.0247630700469017 | 0.0327930374398582 | 5 |
| 2755 | 2755.00225 | 0.750943064689636 | 0.149472494553377 | 0.148642435669899 | 0.249431467509202 | 5 |
| 2760 | 2760.00725 | 0.747136771678925 | 0.154049836601307 | 0.0385389402508736 | 0.0370833314978465 | 5 |
| 2765 | 2764.99556666667 | 0.741683840751648 | 0.185839869281046 | 0.158769875764847 | 0.412223975175809 | 5 |
| 2770 | 2770.00056666667 | 0.346262812614441 | 0.66378022875817 | 0.49703922867775 | 0.865194887073889 | 5 |
| 2775 | 2775.00556666667 | 0.373308300971985 | 0.555376906318083 | 0.259022057056427 | 0.48340697423888 | 5 |
| 2780 | 2779.99388333333 | 0.953420460224152 | 0.0211168300653595 | 0.586345911026001 | 0.969227391930422 | 5 |
| 2785 | 2784.99888333333 | 0.789965391159058 | 0.139564814814815 | 0.184152767062187 | 0.517432669308353 | 5 |
| 2790 | 2790.00388333333 | 0.536455869674683 | 0.184602124183007 | 0.280744820833206 | 0.562252567952677 | 5 |
| 2795 | 2794.9922 | 0.502117395401001 | 0.215205610021786 | 0.243072718381882 | 0.601599452541596 | 5 |
| 2800 | 2799.9972 | 0.746648907661438 | 0.200300925925926 | 0.41252663731575 | 0.769158247418059 | 5 |
| 2805 | 2805.0022 | 0.932400941848755 | 0.0543115468409586 | 0.221554189920425 | 0.681796829019748 | 5 |
| 2810 | 2810.0072 | 0.362738847732544 | 0.430161492374728 | 0.571715414524078 | 0.929616822702021 | 5 |
| 2815 | 2814.99551666667 | 0.624750852584839 | 0.262714324618736 | 0.383291393518448 | 0.623878917680678 | 5 |
| 2820 | 2820.00051666667 | 0.484001666307449 | 0.24315522875817 | 0.281383186578751 | 0.44750450822768 | 5 |
| 2825 | 2825.00551666667 | 0.476128846406937 | 0.552145697167756 | 0.172247007489204 | 0.947919247632847 | 5 |
| 2830 | 2829.99383333333 | 0.418476045131683 | 0.533711328976035 | 0.0616233646869659 | 0.803195726482744 | 5 |


## Record 02 — M01: Dear001

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | a06203131f76bb12597757e8906c5d7ae89f5661da5e9fcf01a99bfc6bdfb0e6 |
| started_utc | 2026-09-10T06:20:01.882755+00:00 |
| completed_utc | 2026-09-10T06:20:06.274093+00:00 |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear001 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| size_bytes | 116784561 |
| sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| start_s | 1.16666666666667 |
| end_s | 201.933333333333 |
| duration_s | 200.766666666667 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 35 to 6058 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-001, frames/M01_frame_header_00.jpg, frames/M01_frame_header_01.jpg, adv_dear_hmsz_001.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear001 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 35 to 6058 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-001, frames/M01_frame_header_00.jpg, frames/M01_frame_header_01.jpg, adv_dear_hmsz_001.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 1.16666666666667 |
| parameters.end_s | 201.933333333333 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 44818944 |
| streams[0].duration | 2917.900000 |
| streams[0].bit_rate | 180317 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 87537 |
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
| streams[1].duration_ts | 128681984 |
| streams[1].duration | 2917.958821 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 125666 |
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
| streams[2].duration_ts | 262616294 |
| streams[2].duration | 2917.958822 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2917.958821 |
| format.size | 116784561 |
| format.bit_rate | 320181 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20250516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=18Eb02aeTH0 |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 4426905 |
| analyzed_audio_duration_s | 200.766666666667 |
| stft_frames | 8643 |
| flux_transitions | 8642 |
| rms_linear | 0.0783720709671422 |
| rms_p10_linear | 0 |
| rms_p90_linear | 0.137604523632285 |
| rms_p90_p10_db | 222.772654223956 |
| rms_p10_floor_applied | true |
| rms_p10_near_zero | true |
| rms_frames_below_1e_minus8 | 1169 |
| centroid_hz_mean | 1795.65998434929 |
| flatness_mean | 0.157426836227303 |
| positive_normalized_flux_mean | 0.0317516507881353 |
| flux_cv | 0.757065104355935 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -20.9 |
| lra_lu | 7.3 |
| true_peak_dbfs | -4.3 |
| silence_seconds | 30.9597260000001 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -20.9 LUFS<br>    Threshold: -31.7 LUFS<br><br>  Loudness range:<br>    LRA:         7.3 LU<br>    Threshold: -42.1 LUFS<br>    LRA low:   -26.9 LUFS<br>    LRA high:  -19.5 LUFS<br><br>  True peak:<br>    Peak:       -4.3 dBFS<br>[out#0/null @ 000001965ebe4ec0] video:0KiB audio:34585KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:03:20.76 bitrate=N/A speed= 168x elapsed=0:00:01.19 |
| ffmpeg_stderr_sha256 | 01c5e90d9ba2514cc4b9444ddd21decd7264f942b1bc37550e7da5765d409693 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 1.617324 | 7.440385 | 5.823061 | 5.823061 |
| 19.01737 | 21.510952 | 2.493582 | 2.493583 |
| 22.117324 | 26.651429 | 4.534105 | 4.534104 |
| 80.617596 | 81.628027 | 1.010431 | 1.010431 |
| 82.544875 | 83.116712 | 0.571837000000002 | 0.571837 |
| 83.661565 | 84.432041 | 0.770476000000002 | 0.770476 |
| 84.970703 | 85.830612 | 0.859909000000002 | 0.859909 |
| 87.086712 | 88.114739 | 1.02802699999999 | 1.028027 |
| 89.742177 | 92.991927 | 3.24975000000001 | 3.249751 |
| 168.426145 | 169.683379 | 1.25723400000001 | 1.257234 |
| 171.484082 | 172.16542 | 0.681338000000011 | 0.681338 |
| 173.08576 | 175.096213 | 2.01045300000001 | 2.010454 |
| 175.903764 | 176.74059 | 0.836826000000002 | 0.836825 |
| 178.294898 | 179.050952 | 0.756054000000006 | 0.756054 |
| 193.281043 | 195.700385 | 2.419342 | 2.419342 |
| 197.187302 | 199.844603 | 2.65730100000002 | 2.657302 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 41 |
| samples | 41 |
| brightness_mean | 0.718351191136895 |
| saturation_mean | 0.167727721983102 |
| frame_difference_mean | 0.050922445836477 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 1.16666666666667 | 1.16666666666667 | 0.802776396274567 | 0.100309640522876 | N/A | N/A | N/A |
| 6.16666666666667 | 6.16666666666667 | 0.595578730106354 | 0.195104030501089 | 0.209191158413887 | 0.355319287147128 | 5 |
| 11.1666666666667 | 11.1666666666667 | 0.701829850673676 | 0.155124727668845 | 0.115937903523445 | 0.413912349536935 | 5 |
| 16.1666666666667 | 16.1666666666667 | 0.738309860229492 | 0.160430010893246 | 0.0986130088567734 | 0.237220262394886 | 5 |
| 21.1666666666667 | 21.1666666666667 | 0.709792196750641 | 0.167834694989107 | 0.0703123658895493 | 0.201889001125665 | 5 |
| 26.1666666666667 | 26.1666666666667 | 0.715403616428375 | 0.165058551198257 | 0.0632186830043793 | 0.197199585118317 | 5 |
| 31.1666666666667 | 31.1666666666667 | 0.723427057266235 | 0.171141339869281 | 0.0666149258613586 | 0.143987583450741 | 5 |
| 36.1666666666667 | 36.1666666666667 | 0.713778913021088 | 0.17425408496732 | 0.0565631799399853 | 0.125758681484226 | 5 |
| 41.1666666666667 | 41.1666666666667 | 0.72159481048584 | 0.173744008714597 | 0.0525904111564159 | 0.12704290366172 | 5 |
| 46.1666666666667 | 46.1666666666667 | 0.726380228996277 | 0.171518518518519 | 0.0162837691605091 | 0.0492659172403385 | 5 |
| 51.1666666666667 | 51.1666666666667 | 0.712990462779999 | 0.174128267973856 | 0.0596941709518433 | 0.111562770191025 | 5 |
| 56.1666666666667 | 56.1666666666667 | 0.728212416172028 | 0.170875544662309 | 0.0596032179892063 | 0.116550157594727 | 5 |
| 61.1666666666667 | 61.1666666666667 | 0.718010067939758 | 0.175763888888889 | 0.0206146519631147 | 0.0638184653821738 | 5 |
| 66.1666666666667 | 66.1666666666667 | 0.718669712543488 | 0.175890795206972 | 0.00777941197156906 | 0.0393552842861058 | 5.00000000000001 |
| 71.1666666666667 | 71.1666666666667 | 0.719912588596344 | 0.174591775599129 | 0.0121247274801135 | 0.0363946963998514 | 5 |
| 76.1666666666667 | 76.1666666666667 | 0.724097788333893 | 0.171768246187364 | 0.024423748254776 | 0.0564199728611669 | 5 |
| 81.1666666666667 | 81.1666666666667 | 0.72560328245163 | 0.170684640522876 | 0.025923203676939 | 0.0722265128271218 | 5 |
| 86.1666666666667 | 86.1666666666667 | 0.716156542301178 | 0.172388071895425 | 0.0595038086175919 | 0.131792971116275 | 5 |
| 91.1666666666667 | 91.1666666666667 | 0.677168130874634 | 0.148153594771242 | 0.0770593658089638 | 0.280018250877395 | 5 |
| 96.1666666666667 | 96.1666666666667 | 0.721154928207397 | 0.173370098039216 | 0.0955708026885986 | 0.273623349957854 | 5 |
| 101.166666666667 | 101.166666666667 | 0.726922690868378 | 0.170044389978214 | 0.0185879617929459 | 0.0558162574153984 | 5 |
| 106.166666666667 | 106.166666666667 | 0.712658286094666 | 0.175449074074074 | 0.0633080005645752 | 0.126251488250625 | 5 |
| 111.166666666667 | 111.166666666667 | 0.715093970298767 | 0.173688453159041 | 0.0211350750178099 | 0.0587306729718299 | 5 |
| 116.166666666667 | 116.166666666667 | 0.71321165561676 | 0.171906862745098 | 0.0126045756042004 | 0.0638127273998407 | 5 |
| 121.166666666667 | 121.166666666667 | 0.723197996616364 | 0.172657952069717 | 0.0579744055867195 | 0.131678411496351 | 5 |
| 126.166666666667 | 126.166666666667 | 0.72665148973465 | 0.170089052287582 | 0.0192802287638187 | 0.0514038914502986 | 5 |
| 131.166666666667 | 131.166666666667 | 0.718894124031067 | 0.174543845315904 | 0.0195520147681236 | 0.0602443925322486 | 4.99999999999999 |
| 136.166666666667 | 136.166666666667 | 0.710379898548126 | 0.17605991285403 | 0.0557543598115444 | 0.121326715080671 | 5 |
| 141.166666666667 | 141.166666666667 | 0.710828721523285 | 0.177071623093682 | 0.0230991281569004 | 0.0443995208488542 | 5 |
| 146.166666666667 | 146.166666666667 | 0.726174056529999 | 0.170257897603486 | 0.0601955316960812 | 0.128307498438319 | 5 |
| 151.166666666667 | 151.166666666667 | 0.724883735179901 | 0.171074891067538 | 0.020428104326129 | 0.0483951188890452 | 5 |
| 156.166666666667 | 156.166666666667 | 0.72693657875061 | 0.168493464052288 | 0.0187440067529678 | 0.0715771475574385 | 5 |
| 161.166666666667 | 161.166666666667 | 0.71470046043396 | 0.172592592592593 | 0.0610846951603889 | 0.135476983550569 | 5 |
| 166.166666666667 | 166.166666666667 | 0.713632106781006 | 0.174239106753813 | 0.01391258276999 | 0.0257662225473901 | 5 |
| 171.166666666667 | 171.166666666667 | 0.72814267873764 | 0.169743736383442 | 0.0590781569480896 | 0.120059954011732 | 5 |
| 176.166666666667 | 176.166666666667 | 0.724166691303253 | 0.171713507625272 | 0.0169052295386791 | 0.0482136263968661 | 5 |
| 181.166666666667 | 181.166666666667 | 0.725522637367249 | 0.170354030501089 | 0.0235133450478315 | 0.0648211205177546 | 5 |
| 186.166666666667 | 186.166666666667 | 0.719559669494629 | 0.17038834422658 | 0.0612140521407127 | 0.127500119921721 | 5 |
| 191.166666666667 | 191.166666666667 | 0.722075998783112 | 0.167852124183007 | 0.0158453155308962 | 0.0344380175813391 | 5 |
| 196.166666666667 | 196.166666666667 | 0.781577408313751 | 0.128584694989107 | 0.0915836021304131 | 0.279617887445098 | 5 |
| 201.166666666667 | 201.166666666667 | 0.676340401172638 | 0.13789651416122 | 0.111474946141243 | 0.320231835398583 | 5 |


## Record 03 — M01: Dear002

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 46b05bee3f2aaa8d6636c65d7632668ab8a66ac17be5cfd8c90dbc55b2675699 |
| started_utc | 2026-09-10T06:20:01.880771+00:00 |
| completed_utc | 2026-09-10T06:20:08.378048+00:00 |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear002 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| size_bytes | 116784561 |
| sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| start_s | 201.933333333333 |
| end_s | 500.366666666667 |
| duration_s | 298.433333333333 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 6058 to 15011 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-002, frames/M01_frame_header_01.jpg, frames/M01_frame_header_02.jpg, adv_dear_hmsz_002.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear002 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 6058 to 15011 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-002, frames/M01_frame_header_01.jpg, frames/M01_frame_header_02.jpg, adv_dear_hmsz_002.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 201.933333333333 |
| parameters.end_s | 500.366666666667 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 44818944 |
| streams[0].duration | 2917.900000 |
| streams[0].bit_rate | 180317 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 87537 |
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
| streams[1].duration_ts | 128681984 |
| streams[1].duration | 2917.958821 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 125666 |
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
| streams[2].duration_ts | 262616294 |
| streams[2].duration | 2917.958822 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2917.958821 |
| format.size | 116784561 |
| format.bit_rate | 320181 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20250516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=18Eb02aeTH0 |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 6580455 |
| analyzed_audio_duration_s | 298.433333333333 |
| stft_frames | 12849 |
| flux_transitions | 12848 |
| rms_linear | 0.0820491490112788 |
| rms_p10_linear | 0.00751168400617196 |
| rms_p90_linear | 0.141048773105266 |
| rms_p90_p10_db | 25.4726400533164 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 854 |
| centroid_hz_mean | 2070.61002671376 |
| flatness_mean | 0.0948979353126589 |
| positive_normalized_flux_mean | 0.0317762478389508 |
| flux_cv | 0.723262258741925 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -20.9 |
| lra_lu | 5.7 |
| true_peak_dbfs | -4.4 |
| silence_seconds | 24.3714059999999 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -20.9 LUFS<br>    Threshold: -31.7 LUFS<br><br>  Loudness range:<br>    LRA:         5.7 LU<br>    Threshold: -41.9 LUFS<br>    LRA low:   -25.2 LUFS<br>    LRA high:  -19.5 LUFS<br><br>  True peak:<br>    Peak:       -4.4 dBFS<br>[out#0/null @ 000001fb4c1a6a80] video:0KiB audio:51410KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:04:58.43 bitrate=N/A speed= 124x elapsed=0:00:02.39 |
| ffmpeg_stderr_sha256 | 77d6d070cd324ad3ce5dcd712c35e6fe7e3ef54076ed3259c2b4fd979fa1d2ad |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 87.268594 | 88.469184 | 1.20059000000001 | 1.20059 |
| 89.473946 | 90.740544 | 1.266598 | 1.266599 |
| 197.435941 | 199.131791 | 1.69584999999998 | 1.69585 |
| 199.939229 | 200.739955 | 0.800725999999997 | 0.800726 |
| 202.524399 | 204.334989 | 1.81059000000002 | 1.81059 |
| 205.972018 | 206.637755 | 0.665737000000007 | 0.665737 |
| 208.667188 | 209.8922 | 1.22501199999999 | 1.225011 |
| 211.039116 | 212.24585 | 1.20673399999998 | 1.206735 |
| 213.07941 | 213.770952 | 0.691541999999998 | 0.691542 |
| 214.507324 | 215.921179 | 1.41385499999998 | 1.413855 |
| 216.312177 | 219.25161 | 2.93943300000001 | 2.939433 |
| 238.977279 | 241.170748 | 2.19346899999999 | 2.193469 |
| 285.499546 | 287.950431 | 2.45088499999997 | 2.450884 |
| 289.427324 | 290.686281 | 1.25895700000001 | 1.258957 |
| 292.90737 | 294.400952 | 1.493582 | 1.493583 |
| 295.437324 | 297.49517 | 2.05784599999998 | 2.057846 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 60 |
| samples | 60 |
| brightness_mean | 0.69851051568985 |
| saturation_mean | 0.158188716412491 |
| frame_difference_mean | 0.0352141295512349 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 201.933333333333 | 201.933333333333 | 0.67321765422821 | 0.171512254901961 | N/A | N/A | N/A |
| 206.933333333333 | 206.933333333333 | 0.692879378795624 | 0.169437636165577 | 0.0374596938490868 | 0.104234362886863 | 5 |
| 211.933333333333 | 211.933333333333 | 0.693748354911804 | 0.168346677559913 | 0.0108009250834584 | 0.046391892705712 | 5 |
| 216.933333333333 | 216.933333333333 | 0.693603813648224 | 0.168705065359477 | 0.0139741292223334 | 0.0447320483251817 | 5 |
| 221.933333333333 | 221.933333333333 | 0.692693114280701 | 0.167380991285403 | 0.0132238557562232 | 0.063301838606814 | 5 |
| 226.933333333333 | 226.933333333333 | 0.694228231906891 | 0.161659041394336 | 0.0671554952859879 | 0.146717678050126 | 5 |
| 231.933333333333 | 231.933333333333 | 0.688836097717285 | 0.165158769063181 | 0.0201279949396849 | 0.0681657634092387 | 5 |
| 236.933333333333 | 236.933333333333 | 0.689059376716614 | 0.163343954248366 | 0.00740740774199367 | 0.0593676654522917 | 5 |
| 241.933333333333 | 241.933333333333 | 0.693854331970215 | 0.16006454248366 | 0.0213101822882891 | 0.0623524763497581 | 5 |
| 246.933333333333 | 246.933333333333 | 0.698029637336731 | 0.157346132897603 | 0.0666677579283714 | 0.152528880331198 | 5 |
| 251.933333333333 | 251.933333333333 | 0.699314773082733 | 0.157914215686275 | 0.0264523420482874 | 0.0495985837193771 | 5 |
| 256.933333333333 | 256.933333333333 | 0.702290296554565 | 0.152535947712418 | 0.0280364900827408 | 0.0623468095441426 | 5 |
| 261.933333333333 | 261.933333333333 | 0.689631521701813 | 0.164694989106754 | 0.0617475472390652 | 0.158141108211994 | 5 |
| 266.933333333333 | 266.933333333333 | 0.693714082241058 | 0.160942538126362 | 0.0210781581699848 | 0.0761966855302349 | 5 |
| 271.933333333333 | 271.933333333333 | 0.69262558221817 | 0.162181917211329 | 0.0260187890380621 | 0.0696221913520794 | 5 |
| 276.933333333333 | 276.933333333333 | 0.695396602153778 | 0.16028894335512 | 0.0201369822025299 | 0.0510602450412784 | 5 |
| 281.933333333333 | 281.933333333333 | 0.694201529026031 | 0.158613562091503 | 0.00760729843750596 | 0.0625604969233012 | 5 |
| 286.933333333333 | 286.933333333333 | 0.697918295860291 | 0.155830882352941 | 0.0607706941664219 | 0.150044392315891 | 5 |
| 291.933333333333 | 291.933333333333 | 0.700827360153198 | 0.155446895424837 | 0.0324041359126568 | 0.0662677760870393 | 5 |
| 296.933333333333 | 296.933333333333 | 0.693914234638214 | 0.160193899782135 | 0.0656625777482986 | 0.136065719722532 | 5 |
| 301.933333333333 | 301.933333333333 | 0.691306173801422 | 0.161596949891068 | 0.0250367652624846 | 0.0699537740107324 | 5 |
| 306.933333333333 | 306.933333333333 | 0.699452042579651 | 0.156777505446623 | 0.0596857294440269 | 0.132737115624602 | 5 |
| 311.933333333333 | 311.933333333333 | 0.698087990283966 | 0.158051470588235 | 0.0147301210090518 | 0.0441284248098227 | 5 |
| 316.933333333333 | 316.933333333333 | 0.692739367485046 | 0.161202614379085 | 0.0624515227973461 | 0.141097851713947 | 5 |
| 321.933333333333 | 321.933333333333 | 0.692790567874908 | 0.160926198257081 | 0.0198801718652248 | 0.0595855749637573 | 5 |
| 326.933333333333 | 326.933333333333 | 0.689967334270477 | 0.165013616557734 | 0.0221560448408127 | 0.0645316712577536 | 5 |
| 331.933333333333 | 331.933333333333 | 0.688395977020264 | 0.164539760348584 | 0.0226040314882994 | 0.0603063018166094 | 5 |
| 336.933333333333 | 336.933333333333 | 0.696646571159363 | 0.157709422657952 | 0.0572570785880089 | 0.138638461421849 | 5 |
| 341.933333333333 | 341.933333333333 | 0.697048485279083 | 0.157547385620915 | 0.0126410676166415 | 0.042597564257048 | 5 |
| 346.933333333333 | 346.933333333333 | 0.685772359371185 | 0.165952614379085 | 0.0577581711113453 | 0.143861795073527 | 5 |
| 351.933333333333 | 351.933333333333 | 0.68541693687439 | 0.164154684095861 | 0.00783796329051256 | 0.0610422599738946 | 5 |
| 356.933333333333 | 356.933333333333 | 0.702106773853302 | 0.153953159041394 | 0.0607061497867107 | 0.153459752425427 | 5 |
| 361.933333333333 | 361.933333333333 | 0.694915354251862 | 0.160329248366013 | 0.0638286992907524 | 0.148923164279917 | 5 |
| 366.933333333333 | 366.933333333333 | 0.690523982048035 | 0.165212962962963 | 0.0182246714830399 | 0.0664803850112412 | 5 |
| 371.933333333333 | 371.933333333333 | 0.697089850902557 | 0.15762908496732 | 0.0591241791844368 | 0.140521329486314 | 5 |
| 376.933333333333 | 376.933333333333 | 0.697365999221802 | 0.159498638344227 | 0.0285626370459795 | 0.0422306519310134 | 5 |
| 381.933333333333 | 381.933333333333 | 0.698481798171997 | 0.158427015250545 | 0.0284643266350031 | 0.0449580099129201 | 5 |
| 386.933333333333 | 386.933333333333 | 0.693125545978546 | 0.160294389978213 | 0.0641819164156914 | 0.15549530326364 | 5 |
| 391.933333333333 | 391.933333333333 | 0.693464636802673 | 0.161494553376906 | 0.0115890521556139 | 0.0511002937024214 | 5 |
| 396.933333333333 | 396.933333333333 | 0.690745174884796 | 0.164262254901961 | 0.0263632871210575 | 0.0684565813746451 | 5 |
| 401.933333333333 | 401.933333333333 | 0.705369353294373 | 0.150825163398693 | 0.0623872540891171 | 0.148526371011126 | 5 |
| 406.933333333333 | 406.933333333333 | 0.698426783084869 | 0.157441993464052 | 0.0305057186633348 | 0.0658634244558837 | 5 |
| 411.933333333333 | 411.933333333333 | 0.697419404983521 | 0.156771241830065 | 0.0181810986250639 | 0.0443509529294772 | 5 |
| 416.933333333333 | 416.933333333333 | 0.698373973369598 | 0.153461328976035 | 0.0209300108253956 | 0.0660786840886479 | 5 |
| 421.933333333333 | 421.933333333333 | 0.688304781913757 | 0.16426334422658 | 0.0564847476780415 | 0.153230340063598 | 5 |
| 426.933333333333 | 426.933333333333 | 0.69188404083252 | 0.163716230936819 | 0.0201271772384644 | 0.0438455540043095 | 5 |
| 431.933333333333 | 431.933333333333 | 0.700986981391907 | 0.15490114379085 | 0.0623050108551979 | 0.143711185920331 | 5 |
| 436.933333333333 | 436.933333333333 | 0.701584219932556 | 0.156549291938998 | 0.0265841502696276 | 0.0639233846237571 | 5 |
| 441.933333333333 | 441.933333333333 | 0.702654480934143 | 0.154706427015251 | 0.0122222220525146 | 0.062574840764729 | 5 |
| 446.933333333333 | 446.933333333333 | 0.694463312625885 | 0.161773420479303 | 0.0612303875386715 | 0.150248068264485 | 5 |
| 451.933333333333 | 451.933333333333 | 0.692202866077423 | 0.162001633986928 | 0.00930228736251593 | 0.0425345559571973 | 5 |
| 456.933333333333 | 456.933333333333 | 0.703982055187225 | 0.153527777777778 | 0.0639218389987946 | 0.161078852976578 | 5 |
| 461.933333333333 | 461.933333333333 | 0.705092072486877 | 0.151992647058824 | 0.0143589330837131 | 0.0483816599214029 | 5 |
| 466.933333333333 | 466.933333333333 | 0.694542229175568 | 0.161400326797386 | 0.0650378465652466 | 0.153030263277449 | 5 |
| 471.933333333333 | 471.933333333333 | 0.694410383701324 | 0.159854302832244 | 0.00576851842924953 | 0.0535604904083007 | 5 |
| 476.933333333333 | 476.933333333333 | 0.6938396692276 | 0.161450708061002 | 0.0100375823676586 | 0.0592001431216548 | 5 |
| 481.933333333333 | 481.933333333333 | 0.698445856571198 | 0.154878267973856 | 0.0623306110501289 | 0.149144208717509 | 5 |
| 486.933333333333 | 486.933333333333 | 0.696902275085449 | 0.156050381263617 | 0.0217309352010489 | 0.0527237600468013 | 5 |
| 491.933333333333 | 491.933333333333 | 0.803023219108582 | 0.0998690087145969 | 0.118815898895264 | 0.267459327655756 | 5 |
| 496.933333333333 | 496.933333333333 | 0.803295791149139 | 0.0997159586056645 | 0.0042453701607883 | 0.0408246324613693 | 5 |


## Record 04 — M01: Dear003

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 759f4b66326a53a130e6a2929e84c4b5104f551aa39daf77285e8f600e643d92 |
| started_utc | 2026-09-10T06:20:07.038117+00:00 |
| completed_utc | 2026-09-10T06:20:12.970666+00:00 |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear003 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| size_bytes | 116784561 |
| sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| start_s | 500.366666666667 |
| end_s | 739.266666666667 |
| duration_s | 238.9 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 15011 to 22178 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-003, frames/M01_frame_header_02.jpg, frames/M01_frame_header_03.jpg, adv_dear_hmsz_003.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear003 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 15011 to 22178 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-003, frames/M01_frame_header_02.jpg, frames/M01_frame_header_03.jpg, adv_dear_hmsz_003.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 500.366666666667 |
| parameters.end_s | 739.266666666667 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 44818944 |
| streams[0].duration | 2917.900000 |
| streams[0].bit_rate | 180317 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 87537 |
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
| streams[1].duration_ts | 128681984 |
| streams[1].duration | 2917.958821 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 125666 |
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
| streams[2].duration_ts | 262616294 |
| streams[2].duration | 2917.958822 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2917.958821 |
| format.size | 116784561 |
| format.bit_rate | 320181 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20250516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=18Eb02aeTH0 |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 5267745 |
| analyzed_audio_duration_s | 238.9 |
| stft_frames | 10285 |
| flux_transitions | 10284 |
| rms_linear | 0.0791077481049682 |
| rms_p10_linear | 0.0116604740087552 |
| rms_p90_linear | 0.122034170489474 |
| rms_p90_p10_db | 20.3953049639058 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 606 |
| centroid_hz_mean | 2069.0002372452 |
| flatness_mean | 0.0866509945008519 |
| positive_normalized_flux_mean | 0.0329994084352609 |
| flux_cv | 0.681155631530637 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -21.7 |
| lra_lu | 6.2 |
| true_peak_dbfs | -4.2 |
| silence_seconds | 16.546234 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -21.7 LUFS<br>    Threshold: -32.1 LUFS<br><br>  Loudness range:<br>    LRA:         6.2 LU<br>    Threshold: -42.3 LUFS<br>    LRA low:   -25.8 LUFS<br>    LRA high:  -19.6 LUFS<br><br>  True peak:<br>    Peak:       -4.2 dBFS<br>[out#0/null @ 00000204b6218500] video:0KiB audio:41154KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:03:58.90 bitrate=N/A speed= 153x elapsed=0:00:01.56 |
| ffmpeg_stderr_sha256 | 9a8a2944a7cc0d047d8cc1b583d635cacede5e98592e94a0390f2b1aa07c021b |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 42.17746 | 42.678254 | 0.500793999999999 | 0.500794 |
| 42.885057 | 43.573492 | 0.688434999999998 | 0.688435 |
| 48.477279 | 50.23102 | 1.753741 | 1.753741 |
| 140.755351 | 142.350884 | 1.59553300000002 | 1.595533 |
| 145.967347 | 147.738753 | 1.77140600000001 | 1.771406 |
| 148.608141 | 149.750567 | 1.142426 | 1.142426 |
| 202.623628 | 203.21941 | 0.595782000000014 | 0.595782 |
| 205.310771 | 206.229456 | 0.918685000000011 | 0.918685 |
| 209.727256 | 211.370839 | 1.64358299999998 | 1.643583 |
| 228.306485 | 230.820385 | 2.51389999999998 | 2.5139 |
| 232.277302 | 233.560952 | 1.28364999999999 | 1.283651 |
| 235.127392 | 235.6578 | 0.530408000000023 | 0.530408 |
| 236.213129 | 237.82102 | 1.607891 | 1.607891 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 48 |
| samples | 48 |
| brightness_mean | 0.72423246751229 |
| saturation_mean | 0.174010416666667 |
| frame_difference_mean | 0.0368458249388223 |
| histogram_jumps_gt_0_5 | 1 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 500.366666666667 | 500.366666666667 | 0.711889266967773 | 0.182686546840959 | N/A | N/A | N/A |
| 505.366666666667 | 505.366666666667 | 0.72148209810257 | 0.271434095860566 | 0.0707982033491135 | 0.506021979039934 | 5 |
| 510.366666666667 | 510.366666666667 | 0.720010101795197 | 0.180303921568627 | 0.0771200880408287 | 0.485759906124374 | 5 |
| 515.366666666667 | 515.366666666667 | 0.719587445259094 | 0.178866830065359 | 0.00527777755632997 | 0.0631908169873531 | 5 |
| 520.366666666667 | 520.366666666667 | 0.72492241859436 | 0.166019063180828 | 0.0572538115084171 | 0.170465431370484 | 5 |
| 525.366666666667 | 525.366666666667 | 0.718956708908081 | 0.178892973856209 | 0.0569482557475567 | 0.16774372278602 | 5 |
| 530.366666666667 | 530.366666666667 | 0.721388101577759 | 0.179891612200436 | 0.0114471670240164 | 0.0729386248902829 | 5 |
| 535.366666666667 | 535.366666666667 | 0.720273792743683 | 0.17992211328976 | 0.00316884508356452 | 0.0230191741263305 | 5 |
| 540.366666666667 | 540.366666666667 | 0.725836038589478 | 0.163782135076253 | 0.0559937283396721 | 0.165703665231002 | 5 |
| 545.366666666667 | 545.366666666667 | 0.719622790813446 | 0.180285675381264 | 0.0580275058746338 | 0.168860405133268 | 5 |
| 550.366666666667 | 550.366666666667 | 0.718849122524261 | 0.179035403050109 | 0.00427968380972743 | 0.0571422635239983 | 5 |
| 555.366666666667 | 555.366666666667 | 0.717845618724823 | 0.181347766884532 | 0.0111576803028584 | 0.0671593397150034 | 5 |
| 560.366666666667 | 560.366666666667 | 0.719086647033691 | 0.178919117647059 | 0.0120460242033005 | 0.0701652322944009 | 5 |
| 565.366666666667 | 565.366666666667 | 0.726708829402924 | 0.161087145969499 | 0.0565792471170425 | 0.166747372050301 | 5 |
| 570.366666666667 | 570.366666666667 | 0.7196906208992 | 0.180378812636166 | 0.0575890503823757 | 0.171217038377772 | 5 |
| 575.366666666667 | 575.366666666667 | 0.720150649547577 | 0.177531590413943 | 0.00728349620476365 | 0.0580339516824415 | 5 |
| 580.366666666667 | 580.366666666667 | 0.719691693782806 | 0.178050925925926 | 0.0104365469887853 | 0.0367418892507773 | 5 |
| 585.366666666667 | 585.366666666667 | 0.724213838577271 | 0.166582516339869 | 0.0562448278069496 | 0.160823774861472 | 5 |
| 590.366666666667 | 590.366666666667 | 0.719544112682343 | 0.177619825708061 | 0.0573352351784706 | 0.161195892102258 | 5 |
| 595.366666666667 | 595.366666666667 | 0.721157073974609 | 0.177367374727669 | 0.0117388339713216 | 0.0388845807662208 | 5 |
| 600.366666666667 | 600.366666666667 | 0.72034615278244 | 0.17618954248366 | 0.00562962936237454 | 0.0399295990913047 | 5 |
| 605.366666666667 | 605.366666666667 | 0.725543081760406 | 0.164990468409586 | 0.056947436183691 | 0.169590352791502 | 5 |
| 610.366666666667 | 610.366666666667 | 0.722515046596527 | 0.166654956427015 | 0.0226075705140829 | 0.0563676595348893 | 5 |
| 615.366666666667 | 615.366666666667 | 0.719059407711029 | 0.178482026143791 | 0.0572023428976536 | 0.166845253979503 | 5 |
| 620.366666666667 | 620.366666666667 | 0.723794758319855 | 0.166847494553377 | 0.0601094774901867 | 0.167272103404648 | 5 |
| 625.366666666667 | 625.366666666667 | 0.720456659793854 | 0.177653322440087 | 0.0595776103436947 | 0.164601834081437 | 5 |
| 630.366666666667 | 630.366666666667 | 0.719834446907043 | 0.177876633986928 | 0.00370016321539879 | 0.0187064084339224 | 5 |
| 635.366666666667 | 635.366666666667 | 0.718419671058655 | 0.180986111111111 | 0.0161794647574425 | 0.0724329939622254 | 5 |
| 640.366666666667 | 640.366666666667 | 0.727490782737732 | 0.1637325708061 | 0.0571277290582657 | 0.153396489522862 | 5 |
| 645.366666666667 | 645.366666666667 | 0.724839925765991 | 0.164392156862745 | 0.0138169936835766 | 0.0669044806353863 | 5 |
| 650.366666666667 | 650.366666666667 | 0.720780253410339 | 0.180049291938998 | 0.0585939548909664 | 0.158736373599306 | 5 |
| 655.366666666667 | 655.366666666667 | 0.718877494335175 | 0.181221949891068 | 0.0113243460655212 | 0.032624115410695 | 5 |
| 660.366666666667 | 660.366666666667 | 0.717986404895782 | 0.180330337690632 | 0.0058142701163888 | 0.0629127207529444 | 5 |
| 665.366666666667 | 665.366666666667 | 0.725550413131714 | 0.166007625272331 | 0.0576168298721313 | 0.166279051326395 | 5 |
| 670.366666666667 | 670.366666666667 | 0.72043240070343 | 0.177460784313725 | 0.0544343702495098 | 0.161777378247598 | 5 |
| 675.366666666667 | 675.366666666667 | 0.718684077262878 | 0.180184912854031 | 0.0116034857928753 | 0.0680354369674707 | 5 |
| 680.366666666667 | 680.366666666667 | 0.726007640361786 | 0.166742374727669 | 0.05746840685606 | 0.15268218463242 | 5 |
| 685.366666666667 | 685.366666666667 | 0.723511934280396 | 0.165411220043573 | 0.0100593687966466 | 0.0692042601631916 | 5 |
| 690.366666666667 | 690.366666666667 | 0.720487177371979 | 0.177185185185185 | 0.0559207499027252 | 0.147363583425163 | 5 |
| 695.366666666667 | 695.366666666667 | 0.718824028968811 | 0.180419662309368 | 0.0159833859652281 | 0.0706709499539127 | 5 |
| 700.366666666667 | 700.366666666667 | 0.71807873249054 | 0.180749455337691 | 0.0056228213943541 | 0.0384117695544675 | 5 |
| 705.366666666667 | 705.366666666667 | 0.723727941513062 | 0.166616013071895 | 0.0570855103433132 | 0.148747717123964 | 5 |
| 710.366666666667 | 710.366666666667 | 0.725138366222382 | 0.164754901960784 | 0.00965168885886669 | 0.0751647588004456 | 5 |
| 715.366666666667 | 715.366666666667 | 0.72148722410202 | 0.178605664488017 | 0.0565781556069851 | 0.158746451313905 | 5 |
| 720.366666666667 | 720.366666666667 | 0.7183478474617 | 0.176983387799564 | 0.0138763608410954 | 0.0673165864856875 | 5 |
| 725.366666666667 | 725.366666666667 | 0.727186799049377 | 0.163630174291939 | 0.0582012534141541 | 0.15796139475503 | 5 |
| 730.366666666667 | 730.366666666667 | 0.782227516174316 | 0.12893137254902 | 0.0961059331893921 | 0.274926158256754 | 5 |
| 735.366666666667 | 735.366666666667 | 0.802615284919739 | 0.0994049564270152 | 0.0621884539723396 | 0.217955940851223 | 5 |


## Record 05 — M01: Dear004

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 9f1984a1bedb7de1281cf333e3d2a42735d8c436cc2944daf0f075438eef1e6c |
| started_utc | 2026-09-10T06:20:08.855822+00:00 |
| completed_utc | 2026-09-10T06:20:15.389349+00:00 |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear004 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| size_bytes | 116784561 |
| sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| start_s | 739.266666666667 |
| end_s | 1006.7 |
| duration_s | 267.433333333333 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 22178 to 30201 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-004, frames/M01_frame_header_03.jpg, frames/M01_frame_header_04.jpg, adv_dear_hmsz_004.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear004 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 22178 to 30201 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-004, frames/M01_frame_header_03.jpg, frames/M01_frame_header_04.jpg, adv_dear_hmsz_004.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 739.266666666667 |
| parameters.end_s | 1006.7 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 44818944 |
| streams[0].duration | 2917.900000 |
| streams[0].bit_rate | 180317 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 87537 |
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
| streams[1].duration_ts | 128681984 |
| streams[1].duration | 2917.958821 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 125666 |
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
| streams[2].duration_ts | 262616294 |
| streams[2].duration | 2917.958822 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2917.958821 |
| format.size | 116784561 |
| format.bit_rate | 320181 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20250516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=18Eb02aeTH0 |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 5896905 |
| analyzed_audio_duration_s | 267.433333333333 |
| stft_frames | 11514 |
| flux_transitions | 11513 |
| rms_linear | 0.085234926196279 |
| rms_p10_linear | 0.0118829636828584 |
| rms_p90_linear | 0.145625341681397 |
| rms_p90_p10_db | 21.7662437507769 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 678 |
| centroid_hz_mean | 2080.42360019665 |
| flatness_mean | 0.0845845540820138 |
| positive_normalized_flux_mean | 0.0361732242336758 |
| flux_cv | 0.667985514584372 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -20.9 |
| lra_lu | 6.6 |
| true_peak_dbfs | -3.8 |
| silence_seconds | 17.1581420000001 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -20.9 LUFS<br>    Threshold: -31.4 LUFS<br><br>  Loudness range:<br>    LRA:         6.6 LU<br>    Threshold: -41.6 LUFS<br>    LRA low:   -25.7 LUFS<br>    LRA high:  -19.1 LUFS<br><br>  True peak:<br>    Peak:       -3.8 dBFS<br>[out#0/null @ 0000029addf78080] video:0KiB audio:46070KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:04:27.43 bitrate=N/A speed=96.1x elapsed=0:00:02.78 |
| ffmpeg_stderr_sha256 | 06904498e456741cdaf0829c7ff03116c3553ed558ea58a4e7273e61fb6ef043 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 37.077279 | 39.078866 | 2.001587 | 2.001587 |
| 58.732426 | 59.37966 | 0.647234000000005 | 0.647234 |
| 63.707347 | 65.17093 | 1.463583 | 1.463583 |
| 66.757279 | 68.44195 | 1.68467100000001 | 1.684671 |
| 133.135714 | 134.500726 | 1.36501199999998 | 1.365011 |
| 137.707324 | 139.223855 | 1.51653099999999 | 1.516531 |
| 202.916689 | 204.63093 | 1.71424100000002 | 1.71424 |
| 206.087302 | 207.731406 | 1.644104 | 1.644104 |
| 257.830635 | 260.23034 | 2.39970500000004 | 2.399705 |
| 261.687279 | 262.96093 | 1.27365100000003 | 1.273651 |
| 265.130272 | 266.578095 | 1.44782300000003 | 1.447823 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 54 |
| samples | 54 |
| brightness_mean | 0.726454595724742 |
| saturation_mean | 0.143652046518196 |
| frame_difference_mean | 0.0379030595638983 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 739.266666666667 | 739.266666666667 | 0.733420789241791 | 0.139546296296296 | N/A | N/A | N/A |
| 744.266666666667 | 744.266666666667 | 0.73396897315979 | 0.141438725490196 | 0.00672576250508428 | 0.0470490505862357 | 5 |
| 749.266666666667 | 749.266666666667 | 0.735692024230957 | 0.138371459694989 | 0.0175590962171555 | 0.0648246678360835 | 5 |
| 754.266666666667 | 754.266666666667 | 0.735222041606903 | 0.138274782135076 | 0.00612200424075127 | 0.0333648500988755 | 5 |
| 759.266666666667 | 759.266666666667 | 0.740535140037537 | 0.131687091503268 | 0.061234749853611 | 0.122861195954878 | 5 |
| 764.266666666667 | 764.266666666667 | 0.740189373493195 | 0.131350762527233 | 0.0102461874485016 | 0.0327906390386193 | 5 |
| 769.266666666667 | 769.266666666667 | 0.736824631690979 | 0.140427015250545 | 0.0607949309051037 | 0.149390622386021 | 5 |
| 774.266666666667 | 774.266666666667 | 0.734992682933807 | 0.140656862745098 | 0.016049837693572 | 0.0449869832665318 | 5 |
| 779.266666666667 | 779.266666666667 | 0.742305934429169 | 0.131567810457516 | 0.0652930289506912 | 0.137191226213716 | 5 |
| 784.266666666667 | 784.266666666667 | 0.742501974105835 | 0.13310348583878 | 0.0167892165482044 | 0.0307694488723826 | 5 |
| 789.266666666667 | 789.266666666667 | 0.735125303268433 | 0.138575980392157 | 0.0623112730681896 | 0.126007266485759 | 5 |
| 794.266666666667 | 794.266666666667 | 0.735274255275726 | 0.138373910675381 | 0.00751606747508049 | 0.0426737374646724 | 5 |
| 799.266666666667 | 799.266666666667 | 0.707713782787323 | 0.149061819172113 | 0.0470092594623566 | 0.132469777527391 | 5 |
| 804.266666666667 | 804.266666666667 | 0.722485899925232 | 0.143948801742919 | 0.0241195522248745 | 0.0834986728392317 | 5 |
| 809.266666666667 | 809.266666666667 | 0.72268682718277 | 0.147388616557734 | 0.0200245101004839 | 0.0784690213768998 | 5 |
| 814.266666666667 | 814.266666666667 | 0.717537820339203 | 0.14944825708061 | 0.0172050651162863 | 0.0295233956166252 | 5 |
| 819.266666666667 | 819.266666666667 | 0.719868421554565 | 0.14711165577342 | 0.0665653571486473 | 0.118680707727236 | 5 |
| 824.266666666667 | 824.266666666667 | 0.717704832553864 | 0.146373910675381 | 0.0308276154100895 | 0.0694174047808908 | 5 |
| 829.266666666667 | 829.266666666667 | 0.718784093856812 | 0.149590413943355 | 0.0630062595009804 | 0.1190976489597 | 5 |
| 834.266666666667 | 834.266666666667 | 0.718228459358215 | 0.148018246187364 | 0.00534967333078384 | 0.0601233755113495 | 5 |
| 839.266666666667 | 839.266666666667 | 0.717542767524719 | 0.150007080610022 | 0.0180849675089121 | 0.0611495189404763 | 5 |
| 844.266666666667 | 844.266666666667 | 0.721369624137878 | 0.148579520697168 | 0.0166988000273705 | 0.0511439466428035 | 5 |
| 849.266666666667 | 849.266666666667 | 0.721785426139832 | 0.143709150326797 | 0.0671974420547485 | 0.120820061220482 | 5 |
| 854.266666666667 | 854.266666666667 | 0.718769371509552 | 0.14630637254902 | 0.0120721664279699 | 0.0501202503647327 | 5 |
| 859.266666666667 | 859.266666666667 | 0.720515549182892 | 0.146615196078431 | 0.0672173202037811 | 0.130410258181189 | 5 |
| 864.266666666667 | 864.266666666667 | 0.717461347579956 | 0.147775326797386 | 0.0666505917906761 | 0.120776665836125 | 5 |
| 869.266666666667 | 869.266666666667 | 0.721938490867615 | 0.145470860566449 | 0.0263834428042173 | 0.0728928501781873 | 5 |
| 874.266666666667 | 874.266666666667 | 0.724528849124908 | 0.145330065359477 | 0.0705337673425674 | 0.129598542898 | 5 |
| 879.266666666667 | 879.266666666667 | 0.720243990421295 | 0.146257897603486 | 0.0713110044598579 | 0.126444031196419 | 5 |
| 884.266666666667 | 884.266666666667 | 0.71871542930603 | 0.144903322440087 | 0.0105509245768189 | 0.0621590899425377 | 5 |
| 889.266666666667 | 889.266666666667 | 0.724475800991058 | 0.145165577342048 | 0.0747423693537712 | 0.134461741505621 | 5 |
| 894.266666666667 | 894.266666666667 | 0.719564020633698 | 0.149783769063181 | 0.0176802817732096 | 0.04056782326205 | 5 |
| 899.266666666667 | 899.266666666667 | 0.720260679721832 | 0.148625272331155 | 0.0204389970749617 | 0.0492502777477802 | 5 |
| 904.266666666667 | 904.266666666667 | 0.718796849250793 | 0.148177015250545 | 0.0108782676979899 | 0.0533949821396907 | 5 |
| 909.266666666667 | 909.266666666667 | 0.722353518009186 | 0.146248366013072 | 0.0694994553923607 | 0.125727489306329 | 5 |
| 914.266666666667 | 914.266666666667 | 0.721849977970123 | 0.143934640522876 | 0.0281255450099707 | 0.0659630978603515 | 5 |
| 919.266666666667 | 919.266666666667 | 0.719517946243286 | 0.149043300653595 | 0.0649463459849358 | 0.121174902220079 | 5 |
| 924.266666666667 | 924.266666666667 | 0.719947755336761 | 0.149764978213508 | 0.012726035900414 | 0.0387605860811832 | 5 |
| 929.266666666667 | 929.266666666667 | 0.721018612384796 | 0.147895152505447 | 0.0245130714029074 | 0.0485216900241356 | 5 |
| 934.266666666667 | 934.266666666667 | 0.720126688480377 | 0.146241830065359 | 0.0672012493014336 | 0.111086818113097 | 5 |
| 939.266666666667 | 939.266666666667 | 0.722439765930176 | 0.145181917211329 | 0.0374537035822868 | 0.0484402365156033 | 5 |
| 944.266666666667 | 944.266666666667 | 0.723661303520203 | 0.144378812636166 | 0.0685405805706978 | 0.129308715555241 | 5 |
| 949.266666666667 | 949.266666666667 | 0.719896256923676 | 0.146550381263617 | 0.0715378522872925 | 0.132586134491756 | 5 |
| 954.266666666667 | 954.266666666667 | 0.722003221511841 | 0.146252995642702 | 0.0649773925542831 | 0.119378471134892 | 5 |
| 959.266666666667 | 959.266666666667 | 0.721719861030579 | 0.146515795206972 | 0.00495179696008563 | 0.0387941538050081 | 5 |
| 964.266666666667 | 964.266666666667 | 0.718237221240997 | 0.149075708061002 | 0.0186100210994482 | 0.0630683565249361 | 5 |
| 969.266666666667 | 969.266666666667 | 0.720385849475861 | 0.148584422657952 | 0.014557734131813 | 0.0438763844206311 | 5 |
| 974.266666666667 | 974.266666666667 | 0.719240725040436 | 0.146477124183007 | 0.0643330588936806 | 0.122127867534393 | 5 |
| 979.266666666667 | 979.266666666667 | 0.718529164791107 | 0.145065904139434 | 0.006819989066571 | 0.0627406065714348 | 5 |
| 984.266666666667 | 984.266666666667 | 0.717486441135406 | 0.149662037037037 | 0.0651402473449707 | 0.132268229532726 | 5 |
| 989.266666666667 | 989.266666666667 | 0.717865169048309 | 0.149346132897603 | 0.00565822422504425 | 0.0427805234111727 | 5 |
| 994.266666666667 | 994.266666666667 | 0.721580386161804 | 0.147724673202614 | 0.0173033755272627 | 0.0518856588869809 | 5 |
| 999.266666666667 | 999.266666666667 | 0.781498670578003 | 0.127398148148148 | 0.0845310464501381 | 0.22605092145184 | 5 |
| 1004.26666666667 | 1004.26666666667 | 0.802158176898956 | 0.100845860566449 | 0.0622456409037113 | 0.207742159766003 | 5 |


## Record 06 — M01: Dear005

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | b8c5eb05f630906055a277c072677627272db5a0959bcb7a21895ae996f82df9 |
| started_utc | 2026-09-10T06:20:13.393024+00:00 |
| completed_utc | 2026-09-10T06:20:19.618312+00:00 |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear005 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| size_bytes | 116784561 |
| sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| start_s | 1006.7 |
| end_s | 1260.26666666667 |
| duration_s | 253.566666666667 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 30201 to 37808 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-005, frames/M01_frame_header_04.jpg, frames/M01_frame_header_05.jpg, adv_dear_hmsz_005.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear005 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 30201 to 37808 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-005, frames/M01_frame_header_04.jpg, frames/M01_frame_header_05.jpg, adv_dear_hmsz_005.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 1006.7 |
| parameters.end_s | 1260.26666666667 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 44818944 |
| streams[0].duration | 2917.900000 |
| streams[0].bit_rate | 180317 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 87537 |
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
| streams[1].duration_ts | 128681984 |
| streams[1].duration | 2917.958821 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 125666 |
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
| streams[2].duration_ts | 262616294 |
| streams[2].duration | 2917.958822 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2917.958821 |
| format.size | 116784561 |
| format.bit_rate | 320181 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20250516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=18Eb02aeTH0 |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 5591145 |
| analyzed_audio_duration_s | 253.566666666667 |
| stft_frames | 10917 |
| flux_transitions | 10916 |
| rms_linear | 0.081715416388386 |
| rms_p10_linear | 0.000267610808273031 |
| rms_p90_linear | 0.140607026085509 |
| rms_p90_p10_db | 54.4100674605255 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 986 |
| centroid_hz_mean | 1808.49080810476 |
| flatness_mean | 0.112177892534078 |
| positive_normalized_flux_mean | 0.0355943408271968 |
| flux_cv | 0.690609437022156 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -21.1 |
| lra_lu | 7.1 |
| true_peak_dbfs | -4.2 |
| silence_seconds | 26.181769 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -21.1 LUFS<br>    Threshold: -31.7 LUFS<br><br>  Loudness range:<br>    LRA:         7.1 LU<br>    Threshold: -42.0 LUFS<br>    LRA low:   -26.4 LUFS<br>    LRA high:  -19.4 LUFS<br><br>  True peak:<br>    Peak:       -4.2 dBFS<br>[out#0/null @ 00000168084e8dc0] video:0KiB audio:43681KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:04:13.56 bitrate=N/A speed= 132x elapsed=0:00:01.92 |
| ffmpeg_stderr_sha256 | 7a53deaa1af9a1935e21ad3e530d036b256a019c1ae6bdfa776ef37f7e2d1051 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 91.147324 | 93.048186 | 1.900862 | 1.900862 |
| 94.243968 | 94.788073 | 0.544105000000002 | 0.544104 |
| 96.040726 | 97.221746 | 1.18101999999999 | 1.18102 |
| 100.427302 | 101.970567 | 1.54326500000001 | 1.543265 |
| 134.72737 | 136.420952 | 1.69358199999999 | 1.693583 |
| 137.577347 | 139.091202 | 1.51385500000001 | 1.513855 |
| 139.4822 | 142.32195 | 2.83974999999998 | 2.839751 |
| 194.338277 | 195.543175 | 1.20489799999999 | 1.204898 |
| 196.14161 | 197.747642 | 1.60603200000003 | 1.606032 |
| 198.412993 | 200.462109 | 2.049116 | 2.049116 |
| 202.026893 | 202.963107 | 0.936214000000007 | 0.936213 |
| 204.254399 | 206.259297 | 2.004898 | 2.004898 |
| 209.427392 | 210.771451 | 1.34405900000002 | 1.344059 |
| 242.152744 | 244.050408 | 1.89766399999999 | 1.897664 |
| 245.527347 | 246.800952 | 1.273605 | 1.273605 |
| 247.901519 | 249.000975 | 1.099456 | 1.099456 |
| 251.159206 | 252.708594 | 1.54938799999999 | 1.549388 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 51 |
| samples | 51 |
| brightness_mean | 0.724169557001077 |
| saturation_mean | 0.144150508351489 |
| frame_difference_mean | 0.0447714863903821 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 1006.7 | 1006.7 | 0.724446058273315 | 0.144819989106754 | N/A | N/A | N/A |
| 1011.7 | 1011.7 | 0.724385917186737 | 0.146097222222222 | 0.00746486894786358 | 0.0458126753187653 | 5 |
| 1016.7 | 1016.7 | 0.724898219108582 | 0.144479575163399 | 0.00641802791506052 | 0.061698068763307 | 5 |
| 1021.7 | 1021.7 | 0.717796087265015 | 0.148665305010893 | 0.0659632310271263 | 0.122749762909598 | 5 |
| 1026.7 | 1026.7 | 0.717802047729492 | 0.146485021786492 | 0.00823747180402279 | 0.0588356914311881 | 5 |
| 1031.7 | 1031.7 | 0.723823308944702 | 0.146316176470588 | 0.0670871511101723 | 0.124698073135433 | 5 |
| 1036.7 | 1036.7 | 0.721619606018066 | 0.147008986928105 | 0.0713627487421036 | 0.110775586882868 | 5 |
| 1041.7 | 1041.7 | 0.718046903610229 | 0.147636982570806 | 0.0719202011823654 | 0.120567611983084 | 5 |
| 1046.7 | 1046.7 | 0.724276483058929 | 0.144185185185185 | 0.0654855668544769 | 0.133414791978607 | 5 |
| 1051.7 | 1051.7 | 0.723972260951996 | 0.143671023965142 | 0.0348869822919369 | 0.0519367750594511 | 5 |
| 1056.7 | 1056.7 | 0.723206162452698 | 0.14611165577342 | 0.0666326209902763 | 0.126882022878348 | 5 |
| 1061.7 | 1061.7 | 0.723828375339508 | 0.144840958605664 | 0.0204588770866394 | 0.0574592461934095 | 5 |
| 1066.7 | 1066.7 | 0.720845341682434 | 0.146316993464052 | 0.0711802840232849 | 0.12862910480465 | 5 |
| 1071.7 | 1071.7 | 0.721626400947571 | 0.146554738562092 | 0.0666350796818733 | 0.126385576731372 | 5 |
| 1076.7 | 1076.7 | 0.723079562187195 | 0.144457516339869 | 0.0233360547572374 | 0.0518536018228489 | 5 |
| 1081.7 | 1081.7 | 0.720143556594849 | 0.14859885620915 | 0.0222284849733114 | 0.0770671364440804 | 5 |
| 1086.7 | 1086.7 | 0.719519019126892 | 0.146188180827887 | 0.0669054985046387 | 0.113619871962593 | 5 |
| 1091.7 | 1091.7 | 0.716647386550903 | 0.149610838779956 | 0.024591775611043 | 0.0513719033703726 | 5 |
| 1096.7 | 1096.7 | 0.717464625835419 | 0.147945806100218 | 0.0639577880501747 | 0.132615087707831 | 5 |
| 1101.7 | 1101.7 | 0.720769107341766 | 0.148247276688453 | 0.0154090402647853 | 0.0682570340980253 | 5 |
| 1106.7 | 1106.7 | 0.720236957073212 | 0.14712037037037 | 0.00590958585962653 | 0.0644381802549195 | 5 |
| 1111.7 | 1111.7 | 0.727192342281342 | 0.145283769063181 | 0.0638649240136147 | 0.120859338881985 | 5 |
| 1116.7 | 1116.7 | 0.725066184997559 | 0.144899237472767 | 0.0675754323601723 | 0.121245941832306 | 5 |
| 1121.7 | 1121.7 | 0.723361670970917 | 0.145731753812636 | 0.0285171568393707 | 0.0693007713197823 | 5 |
| 1126.7 | 1126.7 | 0.722618818283081 | 0.144370642701525 | 0.00367973861284554 | 0.0478757781979269 | 5 |
| 1131.7 | 1131.7 | 0.720118820667267 | 0.145662309368192 | 0.0726203769445419 | 0.129242688116861 | 5 |
| 1136.7 | 1136.7 | 0.722319185733795 | 0.146772331154684 | 0.0323006547987461 | 0.0483522299524639 | 5 |
| 1141.7 | 1141.7 | 0.720641076564789 | 0.145149237472767 | 0.0108469501137733 | 0.0569597292456483 | 5 |
| 1146.7 | 1146.7 | 0.667796015739441 | 0.130285403050109 | 0.0788178071379662 | 0.253371363825245 | 5 |
| 1151.7 | 1151.7 | 0.718672692775726 | 0.147846949891068 | 0.0938804447650909 | 0.244215451657005 | 5 |
| 1156.7 | 1156.7 | 0.723789215087891 | 0.143959967320261 | 0.0195811539888382 | 0.055146611667409 | 5 |
| 1161.7 | 1161.7 | 0.722331702709198 | 0.14603431372549 | 0.0726988017559052 | 0.122482851397752 | 5 |
| 1166.7 | 1166.7 | 0.725470900535583 | 0.146569444444444 | 0.0737622603774071 | 0.116945078299262 | 5 |
| 1171.7 | 1171.7 | 0.723443031311035 | 0.146148420479303 | 0.0228502191603184 | 0.0592283137400211 | 5 |
| 1176.7 | 1176.7 | 0.725714564323425 | 0.14407734204793 | 0.0746636688709259 | 0.125760651044319 | 5 |
| 1181.7 | 1181.7 | 0.725946664810181 | 0.144225217864924 | 0.02632244117558 | 0.0544995516205927 | 5 |
| 1186.7 | 1186.7 | 0.7229043841362 | 0.142246732026144 | 0.0263532120734453 | 0.084684557086826 | 5 |
| 1191.7 | 1191.7 | 0.721526980400085 | 0.148242919389978 | 0.0639891028404236 | 0.115635076379019 | 5 |
| 1196.7 | 1196.7 | 0.721930325031281 | 0.148188180827887 | 0.0165198799222708 | 0.0411914094176353 | 5 |
| 1201.7 | 1201.7 | 0.723986387252808 | 0.146404956427015 | 0.0273932460695505 | 0.063092841211003 | 5 |
| 1206.7 | 1206.7 | 0.724187672138214 | 0.146016067538126 | 0.0717529952526093 | 0.124208415525099 | 5 |
| 1211.7 | 1211.7 | 0.723491072654724 | 0.145665032679739 | 0.00892864819616079 | 0.0367355274496242 | 5 |
| 1216.7 | 1216.7 | 0.720996201038361 | 0.144265522875817 | 0.0304234735667706 | 0.0676626519231363 | 5 |
| 1221.7 | 1221.7 | 0.724815666675568 | 0.146063180827887 | 0.0733946040272713 | 0.12051670673204 | 5 |
| 1226.7 | 1226.7 | 0.724275350570679 | 0.144832516339869 | 0.00605119811370969 | 0.0579952422018767 | 5 |
| 1231.7 | 1231.7 | 0.720504939556122 | 0.147549836601307 | 0.0716119185090065 | 0.133527728140647 | 5 |
| 1236.7 | 1236.7 | 0.718499779701233 | 0.150471949891068 | 0.0672045201063156 | 0.122631925745367 | 5 |
| 1241.7 | 1241.7 | 0.719253897666931 | 0.150044934640523 | 0.00849373638629913 | 0.0192355326971221 | 5 |
| 1246.7 | 1246.7 | 0.718757569789886 | 0.148124455337691 | 0.067203164100647 | 0.117612505612513 | 5 |
| 1251.7 | 1251.7 | 0.802345633506775 | 0.100535130718954 | 0.107331968843937 | 0.24446212078301 | 5 |
| 1256.7 | 1256.7 | 0.802255272865295 | 0.100649509803922 | 0.00386928091756999 | 0.0466793711447893 | 5 |


## Record 07 — M01: Dear006

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 5c8f7cff7155e7404f36e4739e86343f49704c9dc91319a33f2516a007425b7b |
| started_utc | 2026-09-10T06:20:15.789870+00:00 |
| completed_utc | 2026-09-10T06:20:22.879468+00:00 |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear006 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| size_bytes | 116784561 |
| sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| start_s | 1260.26666666667 |
| end_s | 1548.26666666667 |
| duration_s | 288 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 37808 to 46448 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-006, frames/M01_frame_header_05.jpg, frames/M01_frame_header_06.jpg, adv_dear_hmsz_006.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear006 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 37808 to 46448 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-006, frames/M01_frame_header_05.jpg, frames/M01_frame_header_06.jpg, adv_dear_hmsz_006.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 1260.26666666667 |
| parameters.end_s | 1548.26666666667 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 44818944 |
| streams[0].duration | 2917.900000 |
| streams[0].bit_rate | 180317 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 87537 |
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
| streams[1].duration_ts | 128681984 |
| streams[1].duration | 2917.958821 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 125666 |
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
| streams[2].duration_ts | 262616294 |
| streams[2].duration | 2917.958822 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2917.958821 |
| format.size | 116784561 |
| format.bit_rate | 320181 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20250516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=18Eb02aeTH0 |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 6350400 |
| analyzed_audio_duration_s | 288 |
| stft_frames | 12400 |
| flux_transitions | 12399 |
| rms_linear | 0.0805992488797552 |
| rms_p10_linear | 0.00728021717822232 |
| rms_p90_linear | 0.139395314676433 |
| rms_p90_p10_db | 25.6420768306404 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 734 |
| centroid_hz_mean | 2268.48127858573 |
| flatness_mean | 0.0922330101309469 |
| positive_normalized_flux_mean | 0.0312011421253656 |
| flux_cv | 0.689519782145086 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -20.9 |
| lra_lu | 7.3 |
| true_peak_dbfs | -3.8 |
| silence_seconds | 19.7719730000001 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -20.9 LUFS<br>    Threshold: -31.8 LUFS<br><br>  Loudness range:<br>    LRA:         7.3 LU<br>    Threshold: -42.0 LUFS<br>    LRA low:   -26.5 LUFS<br>    LRA high:  -19.2 LUFS<br><br>  True peak:<br>    Peak:       -3.8 dBFS<br>[out#0/null @ 00000260fe024000] video:0KiB audio:49612KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:04:48.00 bitrate=N/A speed=98.3x elapsed=0:00:02.92 |
| ffmpeg_stderr_sha256 | 1d3442ad147ae8d4f2aa8bfed8d5f3dcf8de832be22a4312eec468e1934a8f93 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 88.113333 | 89.449161 | 1.33582800000001 | 1.335828 |
| 94.545079 | 95.843855 | 1.298776 | 1.298776 |
| 155.350204 | 156.306417 | 0.95621300000002 | 0.956213 |
| 157.157483 | 158.307188 | 1.14970499999998 | 1.149705 |
| 160.210136 | 160.943946 | 0.733810000000005 | 0.73381 |
| 162.178254 | 163.110612 | 0.932357999999994 | 0.932358 |
| 165.180113 | 166.1139 | 0.933786999999995 | 0.933787 |
| 236.635692 | 239.105737 | 2.470045 | 2.470045 |
| 239.785147 | 241.552154 | 1.76700700000001 | 1.767007 |
| 243.765533 | 246.045283 | 2.27975000000001 | 2.279751 |
| 278.706689 | 281.323787 | 2.617098 | 2.617098 |
| 282.780045 | 284.044308 | 1.26426300000003 | 1.264263 |
| 285.200658 | 287.233991 | 2.03333300000003 | 2.033333 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 58 |
| samples | 58 |
| brightness_mean | 0.706649714502795 |
| saturation_mean | 0.157731087070844 |
| frame_difference_mean | 0.0468865575211678 |
| histogram_jumps_gt_0_5 | 1 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 1260.26666666667 | 1260.26666666667 | 0.719440639019012 | 0.148377178649237 | N/A | N/A | N/A |
| 1265.26666666667 | 1265.26666666667 | 0.723431646823883 | 0.145630446623094 | 0.025634802877903 | 0.064956646722945 | 5 |
| 1270.26666666667 | 1270.26666666667 | 0.719097495079041 | 0.146800653594771 | 0.0696043074131012 | 0.121197596964081 | 5 |
| 1275.26666666667 | 1275.26666666667 | 0.718565404415131 | 0.146826525054466 | 0.00766176450997591 | 0.0397639771469697 | 5 |
| 1280.26666666667 | 1280.26666666667 | 0.722813427448273 | 0.146321895424837 | 0.0277589838951826 | 0.0554664021058535 | 5 |
| 1285.26666666667 | 1285.26666666667 | 0.713461399078369 | 0.149926198257081 | 0.0382197685539722 | 0.0661992793092293 | 5 |
| 1290.26666666667 | 1290.26666666667 | 0.727733671665192 | 0.143616013071895 | 0.046123094856739 | 0.0722245135932594 | 5 |
| 1295.26666666667 | 1295.26666666667 | 0.723914802074432 | 0.143966230936819 | 0.0738014727830887 | 0.121229887403428 | 5 |
| 1300.26666666667 | 1300.26666666667 | 0.724822998046875 | 0.146197440087146 | 0.0108243469148874 | 0.0586526135847385 | 5 |
| 1305.26666666667 | 1305.26666666667 | 0.721816837787628 | 0.147811274509804 | 0.0204310994595289 | 0.0462921548852991 | 5 |
| 1310.26666666667 | 1310.26666666667 | 0.716882109642029 | 0.149837145969499 | 0.0236813742667437 | 0.0557630134060416 | 5 |
| 1315.26666666667 | 1315.26666666667 | 0.723295509815216 | 0.14433605664488 | 0.0177396517246962 | 0.0772315265554125 | 5 |
| 1320.26666666667 | 1320.26666666667 | 0.675028085708618 | 0.226090958605664 | 0.0875234231352806 | 0.350190871171929 | 5 |
| 1325.26666666667 | 1325.26666666667 | 0.674716234207153 | 0.226109204793028 | 0.00348447682335973 | 0.0425327518905963 | 5 |
| 1330.26666666667 | 1330.26666666667 | 0.72636467218399 | 0.147024782135076 | 0.0863537564873695 | 0.347512271988653 | 5 |
| 1335.26666666667 | 1335.26666666667 | 0.717904448509216 | 0.148448801742919 | 0.019303921610117 | 0.0742303473914387 | 5 |
| 1340.26666666667 | 1340.26666666667 | 0.719263911247253 | 0.146416394335512 | 0.0641623064875603 | 0.134513977685461 | 5 |
| 1345.26666666667 | 1345.26666666667 | 0.719415903091431 | 0.14429765795207 | 0.00741448812186718 | 0.0601375860011032 | 5 |
| 1350.26666666667 | 1350.26666666667 | 0.713427305221558 | 0.166104030501089 | 0.0936252772808075 | 0.258903778124738 | 5 |
| 1355.26666666667 | 1355.26666666667 | 0.519182205200195 | 0.0900803376906318 | 0.196275055408478 | 0.467596983920645 | 5 |
| 1360.26666666667 | 1360.26666666667 | 0.707642674446106 | 0.164079793028322 | 0.188586324453354 | 0.518496130182238 | 5 |
| 1365.26666666667 | 1365.26666666667 | 0.706516921520233 | 0.163976307189542 | 0.00593463983386755 | 0.0587997740920565 | 5 |
| 1370.26666666667 | 1370.26666666667 | 0.711652040481567 | 0.162443899782135 | 0.0254765786230564 | 0.0674692473088333 | 5 |
| 1375.26666666667 | 1375.26666666667 | 0.705802798271179 | 0.163464596949891 | 0.0627576261758804 | 0.135832891539782 | 5 |
| 1380.26666666667 | 1380.26666666667 | 0.706908762454987 | 0.163710784313726 | 0.0308406855911016 | 0.0552099803392969 | 5 |
| 1385.26666666667 | 1385.26666666667 | 0.702461063861847 | 0.165919662309368 | 0.0451269075274467 | 0.0769506873497242 | 5 |
| 1390.26666666667 | 1390.26666666667 | 0.706347763538361 | 0.164289760348584 | 0.0598169937729836 | 0.143471706359305 | 5 |
| 1395.26666666667 | 1395.26666666667 | 0.706346988677979 | 0.164025054466231 | 0.00638861674815416 | 0.0419169272871679 | 5 |
| 1400.26666666667 | 1400.26666666667 | 0.711980104446411 | 0.160270697167756 | 0.0219452604651451 | 0.0709976896382884 | 5 |
| 1405.26666666667 | 1405.26666666667 | 0.710768520832062 | 0.160194444444444 | 0.00683360593393445 | 0.0403270258490356 | 5 |
| 1410.26666666667 | 1410.26666666667 | 0.705610632896423 | 0.16517211328976 | 0.0192805007100105 | 0.0673083474530918 | 5 |
| 1415.26666666667 | 1415.26666666667 | 0.705509006977081 | 0.164557189542484 | 0.0621435195207596 | 0.127021835318298 | 5 |
| 1420.26666666667 | 1420.26666666667 | 0.712648451328278 | 0.161036492374728 | 0.0242380183190107 | 0.0580797340597258 | 5 |
| 1425.26666666667 | 1425.26666666667 | 0.709616839885712 | 0.161673747276688 | 0.0177538115531206 | 0.0419842026677467 | 5 |
| 1430.26666666667 | 1430.26666666667 | 0.710377752780914 | 0.161808823529412 | 0.066655233502388 | 0.135087354346138 | 5 |
| 1435.26666666667 | 1435.26666666667 | 0.704347014427185 | 0.164894607843137 | 0.0169300120323896 | 0.0608458463407138 | 5 |
| 1440.26666666667 | 1440.26666666667 | 0.705502808094025 | 0.164907407407407 | 0.00315196090377867 | 0.0233164877141175 | 5 |
| 1445.26666666667 | 1445.26666666667 | 0.706543624401093 | 0.165237472766885 | 0.0564384534955025 | 0.126832396700051 | 5 |
| 1450.26666666667 | 1450.26666666667 | 0.705857872962952 | 0.165614379084967 | 0.0106601314619184 | 0.0402861287382806 | 5 |
| 1455.26666666667 | 1455.26666666667 | 0.713025093078613 | 0.161788126361656 | 0.0613235309720039 | 0.125905063368354 | 5 |
| 1460.26666666667 | 1460.26666666667 | 0.710601627826691 | 0.162554738562092 | 0.0172780510038137 | 0.0509844394081309 | 5 |
| 1465.26666666667 | 1465.26666666667 | 0.70891010761261 | 0.162056917211329 | 0.019549835473299 | 0.050983475337432 | 5 |
| 1470.26666666667 | 1470.26666666667 | 0.708104372024536 | 0.163998093681917 | 0.0640046298503876 | 0.146346116777877 | 5 |
| 1475.26666666667 | 1475.26666666667 | 0.70817619562149 | 0.163359749455338 | 0.00859967246651649 | 0.0325469201041816 | 5 |
| 1480.26666666667 | 1480.26666666667 | 0.706617951393127 | 0.162637527233115 | 0.029162310063839 | 0.0626091807467312 | 5 |
| 1485.26666666667 | 1485.26666666667 | 0.705227434635162 | 0.165508986928105 | 0.0608006529510021 | 0.129822974936782 | 5 |
| 1490.26666666667 | 1490.26666666667 | 0.711082279682159 | 0.161891067538126 | 0.0192186813801527 | 0.0591202728574974 | 5 |
| 1495.26666666667 | 1495.26666666667 | 0.706954777240753 | 0.166339869281046 | 0.0229809358716011 | 0.0486845765069497 | 5 |
| 1500.26666666667 | 1500.26666666667 | 0.708262264728546 | 0.162738834422658 | 0.060407679527998 | 0.136160412432389 | 5 |
| 1505.26666666667 | 1505.26666666667 | 0.655620098114014 | 0.143923747276688 | 0.0748387798666954 | 0.256193370609176 | 5 |
| 1510.26666666667 | 1510.26666666667 | 0.707326531410217 | 0.16368082788671 | 0.080645427107811 | 0.262673356295158 | 5 |
| 1515.26666666667 | 1515.26666666667 | 0.706795811653137 | 0.165127178649237 | 0.0590601861476898 | 0.129080013671343 | 5 |
| 1520.26666666667 | 1520.26666666667 | 0.707934677600861 | 0.163061274509804 | 0.02729357406497 | 0.0479625697223509 | 5 |
| 1525.26666666667 | 1525.26666666667 | 0.709466457366943 | 0.162560185185185 | 0.0672949403524399 | 0.135488916095809 | 5 |
| 1530.26666666667 | 1530.26666666667 | 0.710105657577515 | 0.162138616557734 | 0.00549428071826696 | 0.0366198049789192 | 5 |
| 1535.26666666667 | 1535.26666666667 | 0.713631510734558 | 0.160037581699346 | 0.0632257610559464 | 0.141798253076158 | 5 |
| 1540.26666666667 | 1540.26666666667 | 0.622731983661652 | 0.132855119825708 | 0.0989784896373749 | 0.358839537644458 | 5 |
| 1545.26666666667 | 1545.26666666667 | 0.802088260650635 | 0.100648148148148 | 0.181794106960297 | 0.352622837481305 | 5 |


## Record 08 — M01: Dear007

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | cd2143022b70901634ca1512acfde9a884d1ec7a91ee54f082e05b655d7a13ee |
| started_utc | 2026-09-10T06:20:20.100433+00:00 |
| completed_utc | 2026-09-10T06:20:27.235054+00:00 |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear007 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| size_bytes | 116784561 |
| sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| start_s | 1548.26666666667 |
| end_s | 1790.13333333333 |
| duration_s | 241.866666666667 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 46448 to 53704 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-007, frames/M01_frame_header_06.jpg, frames/M01_frame_header_07.jpg, adv_dear_hmsz_007.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear007 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 46448 to 53704 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-007, frames/M01_frame_header_06.jpg, frames/M01_frame_header_07.jpg, adv_dear_hmsz_007.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 1548.26666666667 |
| parameters.end_s | 1790.13333333333 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 44818944 |
| streams[0].duration | 2917.900000 |
| streams[0].bit_rate | 180317 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 87537 |
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
| streams[1].duration_ts | 128681984 |
| streams[1].duration | 2917.958821 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 125666 |
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
| streams[2].duration_ts | 262616294 |
| streams[2].duration | 2917.958822 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2917.958821 |
| format.size | 116784561 |
| format.bit_rate | 320181 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20250516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=18Eb02aeTH0 |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 5333160 |
| analyzed_audio_duration_s | 241.866666666667 |
| stft_frames | 10413 |
| flux_transitions | 10412 |
| rms_linear | 0.0811983368792853 |
| rms_p10_linear | 0.00670118586442389 |
| rms_p90_linear | 0.142627496158653 |
| rms_p90_p10_db | 26.5610318894064 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 681 |
| centroid_hz_mean | 2358.69810967148 |
| flatness_mean | 0.102061201217182 |
| positive_normalized_flux_mean | 0.0314230396533653 |
| flux_cv | 0.675253354001952 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -20.5 |
| lra_lu | 5.4 |
| true_peak_dbfs | -3.7 |
| silence_seconds | 20.261656 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -20.5 LUFS<br>    Threshold: -31.3 LUFS<br><br>  Loudness range:<br>    LRA:         5.4 LU<br>    Threshold: -41.5 LUFS<br>    LRA low:   -24.9 LUFS<br>    LRA high:  -19.5 LUFS<br><br>  True peak:<br>    Peak:       -3.7 dBFS<br>[out#0/null @ 00000218634e6780] video:0KiB audio:41665KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:04:01.86 bitrate=N/A speed= 118x elapsed=0:00:02.05 |
| ffmpeg_stderr_sha256 | f5621e366f626f589a9e948bb63b3b068a88f2e5421ac077af91a66671856bd0 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 1.311837 | 2.990181 | 1.678344 | 1.678345 |
| 4.297664 | 6.389705 | 2.092041 | 2.092041 |
| 89.854875 | 91.572834 | 1.71795899999999 | 1.717959 |
| 95.398503 | 95.969002 | 0.570498999999998 | 0.570499 |
| 99.894286 | 100.460408 | 0.566122000000007 | 0.566122 |
| 104.717642 | 105.309365 | 0.591723000000002 | 0.591723 |
| 110.041655 | 110.600998 | 0.559342999999998 | 0.559342 |
| 111.313696 | 112.587007 | 1.27331100000001 | 1.273311 |
| 141.229728 | 142.581746 | 1.35201800000002 | 1.352018 |
| 143.229138 | 144.486871 | 1.257733 | 1.257732 |
| 184.308322 | 185.154558 | 0.846236000000005 | 0.846236 |
| 186.07 | 186.902834 | 0.83283400000002 | 0.832834 |
| 188.640635 | 189.224467 | 0.583832000000001 | 0.583832 |
| 230.240249 | 232.963447 | 2.723198 | 2.723197 |
| 234.420317 | 235.464898 | 1.04458099999999 | 1.04458 |
| 236.065238 | 237.173968 | 1.10873000000001 | 1.10873 |
| 239.363288 | 240.82644 | 1.46315199999998 | 1.463152 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 49 |
| samples | 49 |
| brightness_mean | 0.748452080755818 |
| saturation_mean | 0.151745898359344 |
| frame_difference_mean | 0.0564743484040567 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 1548.26666666667 | 1548.26666666667 | 0.615450441837311 | 0.0976200980392157 | N/A | N/A | N/A |
| 1553.26666666667 | 1553.26666666667 | 0.727513372898102 | 0.164078159041394 | 0.149618461728096 | 0.390267814930266 | 5 |
| 1558.26666666667 | 1558.26666666667 | 0.750681400299072 | 0.146140522875817 | 0.0825661718845367 | 0.134788282628171 | 5 |
| 1563.26666666667 | 1563.26666666667 | 0.743519425392151 | 0.161447167755991 | 0.0656331703066826 | 0.150624901044197 | 5 |
| 1568.26666666667 | 1568.26666666667 | 0.750845074653625 | 0.148768246187364 | 0.0634798407554626 | 0.150368157408479 | 5 |
| 1573.26666666667 | 1573.26666666667 | 0.742761433124542 | 0.144276416122004 | 0.0659746751189232 | 0.165065990961634 | 5 |
| 1578.26666666667 | 1578.26666666667 | 0.746899843215942 | 0.148174564270152 | 0.0655130669474602 | 0.168981259720392 | 5 |
| 1583.26666666667 | 1583.26666666667 | 0.749134540557861 | 0.158547930283224 | 0.0566557720303535 | 0.144516674532702 | 5 |
| 1588.26666666667 | 1588.26666666667 | 0.750854909420013 | 0.159110294117647 | 0.0154850222170353 | 0.0444939016238372 | 5 |
| 1593.26666666667 | 1593.26666666667 | 0.739218711853027 | 0.1454098583878 | 0.0736007615923882 | 0.202955634714838 | 5 |
| 1598.26666666667 | 1598.26666666667 | 0.752759873867035 | 0.162550381263617 | 0.0725721642374992 | 0.239901125203279 | 5 |
| 1603.26666666667 | 1603.26666666667 | 0.749098300933838 | 0.148959694989107 | 0.0749147534370422 | 0.250221687351265 | 5 |
| 1608.26666666667 | 1608.26666666667 | 0.74139130115509 | 0.145270152505447 | 0.0736928135156631 | 0.168431861610751 | 5 |
| 1613.26666666667 | 1613.26666666667 | 0.739376604557037 | 0.144749183006536 | 0.0185566451400518 | 0.0346391704534535 | 5 |
| 1618.26666666667 | 1618.26666666667 | 0.75027722120285 | 0.146898692810458 | 0.0703483074903488 | 0.169207811631843 | 5 |
| 1623.26666666667 | 1623.26666666667 | 0.762333393096924 | 0.155125272331155 | 0.0583033747971058 | 0.1319765840439 | 5 |
| 1628.26666666667 | 1628.26666666667 | 0.742928683757782 | 0.144695806100218 | 0.0675947666168213 | 0.188452570229218 | 5 |
| 1633.26666666667 | 1633.26666666667 | 0.736609816551208 | 0.145642156862745 | 0.0243815332651138 | 0.056683528570359 | 5 |
| 1638.26666666667 | 1638.26666666667 | 0.749015033245087 | 0.15994362745098 | 0.0718943327665329 | 0.211146674859443 | 5 |
| 1643.26666666667 | 1643.26666666667 | 0.767856180667877 | 0.150898148148148 | 0.053821075707674 | 0.147293741046034 | 5 |
| 1648.26666666667 | 1648.26666666667 | 0.765474736690521 | 0.168932734204793 | 0.0390296839177608 | 0.144127036586614 | 5 |
| 1653.26666666667 | 1653.26666666667 | 0.77608197927475 | 0.174247276688453 | 0.0366105660796165 | 0.198438193346583 | 5 |
| 1658.26666666667 | 1658.26666666667 | 0.760347247123718 | 0.175301470588235 | 0.0477216728031635 | 0.214422640399097 | 5 |
| 1663.26666666667 | 1663.26666666667 | 0.741190671920776 | 0.144551470588235 | 0.0673439502716064 | 0.239611986688665 | 5 |
| 1668.26666666667 | 1668.26666666667 | 0.779892981052399 | 0.178486928104575 | 0.0724060386419296 | 0.249589747976447 | 5 |
| 1673.26666666667 | 1673.26666666667 | 0.76378321647644 | 0.171508169934641 | 0.0435612760484219 | 0.201955083730158 | 5 |
| 1678.26666666667 | 1678.26666666667 | 0.755810558795929 | 0.181138888888889 | 0.068761982023716 | 0.307942026246496 | 5 |
| 1683.26666666667 | 1683.26666666667 | 0.745932221412659 | 0.148388071895425 | 0.0734223872423172 | 0.298595506689014 | 5 |
| 1688.26666666667 | 1688.26666666667 | 0.743173539638519 | 0.14799591503268 | 0.0400686301290989 | 0.0606069395570823 | 5 |
| 1693.26666666667 | 1693.26666666667 | 0.750161826610565 | 0.158860294117647 | 0.0625836029648781 | 0.154758456597455 | 5 |
| 1698.26666666667 | 1698.26666666667 | 0.74914824962616 | 0.159013616557734 | 0.0153790852054954 | 0.0485519722521177 | 5 |
| 1703.26666666667 | 1703.26666666667 | 0.747249484062195 | 0.1479825708061 | 0.0573071874678135 | 0.148348075014602 | 5 |
| 1708.26666666667 | 1708.26666666667 | 0.756458342075348 | 0.159217864923747 | 0.0746304392814636 | 0.24604227927609 | 5 |
| 1713.26666666667 | 1713.26666666667 | 0.748960494995117 | 0.158631808278867 | 0.0753839910030365 | 0.159235733840893 | 5 |
| 1718.26666666667 | 1718.26666666667 | 0.748931884765625 | 0.159125272331155 | 0.0068139978684485 | 0.0202505607872306 | 5 |
| 1723.26666666667 | 1723.26666666667 | 0.745144605636597 | 0.161026688453159 | 0.0216789208352566 | 0.0639382033468565 | 5 |
| 1728.26666666667 | 1728.26666666667 | 0.742666125297546 | 0.144244553376906 | 0.0724567025899887 | 0.22145611110919 | 5 |
| 1733.26666666667 | 1733.26666666667 | 0.749550640583038 | 0.148330337690632 | 0.0712124109268188 | 0.175858987566882 | 5 |
| 1738.26666666667 | 1738.26666666667 | 0.737284600734711 | 0.144690359477124 | 0.0757421031594276 | 0.173172126992873 | 5 |
| 1743.26666666667 | 1743.26666666667 | 0.736775040626526 | 0.14663779956427 | 0.0348352417349815 | 0.0511400623053792 | 5 |
| 1748.26666666667 | 1748.26666666667 | 0.744607090950012 | 0.159670206971678 | 0.0664049535989761 | 0.209040378089327 | 5 |
| 1753.26666666667 | 1753.26666666667 | 0.743470311164856 | 0.162136165577342 | 0.0243834424763918 | 0.0592585154712892 | 5 |
| 1758.26666666667 | 1758.26666666667 | 0.748311281204224 | 0.159650871459695 | 0.0213894341140985 | 0.0526850034277119 | 5 |
| 1763.26666666667 | 1763.26666666667 | 0.748706758022308 | 0.158752995642702 | 0.0170855112373829 | 0.0389437208363289 | 5 |
| 1768.26666666667 | 1768.26666666667 | 0.739426255226135 | 0.144723039215686 | 0.0683006569743156 | 0.202364810467714 | 5 |
| 1773.26666666667 | 1773.26666666667 | 0.748981535434723 | 0.146507625272331 | 0.0637867674231529 | 0.172158372227583 | 5 |
| 1778.26666666667 | 1778.26666666667 | 0.745034337043762 | 0.144444716775599 | 0.0714308246970177 | 0.175525237126488 | 5 |
| 1783.26666666667 | 1783.26666666667 | 0.801672458648682 | 0.101234477124183 | 0.0916827321052551 | 0.255650952785715 | 5 |
| 1788.26666666667 | 1788.26666666667 | 0.801397919654846 | 0.10181045751634 | 0.00474782101809978 | 0.058927115321288 | 5 |


## Record 09 — M01: Dear008

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | ef1336fa9c69ca5f4613ad0861a7b7334acdedd58084c12fd249a1e67330b08a |
| started_utc | 2026-09-10T06:20:23.254114+00:00 |
| completed_utc | 2026-09-10T06:20:31.499221+00:00 |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear008 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| size_bytes | 116784561 |
| sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| start_s | 1790.13333333333 |
| end_s | 2092.83333333333 |
| duration_s | 302.7 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 53704 to 62785 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-008, frames/M01_frame_header_07.jpg, frames/M01_frame_header_08.jpg, adv_dear_hmsz_008.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear008 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 53704 to 62785 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-008, frames/M01_frame_header_07.jpg, frames/M01_frame_header_08.jpg, adv_dear_hmsz_008.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 1790.13333333333 |
| parameters.end_s | 2092.83333333333 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 44818944 |
| streams[0].duration | 2917.900000 |
| streams[0].bit_rate | 180317 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 87537 |
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
| streams[1].duration_ts | 128681984 |
| streams[1].duration | 2917.958821 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 125666 |
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
| streams[2].duration_ts | 262616294 |
| streams[2].duration | 2917.958822 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2917.958821 |
| format.size | 116784561 |
| format.bit_rate | 320181 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20250516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=18Eb02aeTH0 |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 6674535 |
| analyzed_audio_duration_s | 302.7 |
| stft_frames | 13033 |
| flux_transitions | 13032 |
| rms_linear | 0.0878396441169075 |
| rms_p10_linear | 0.0168164569105487 |
| rms_p90_linear | 0.15098521094088 |
| rms_p90_p10_db | 19.0639982249776 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 536 |
| centroid_hz_mean | 2418.04246445431 |
| flatness_mean | 0.0741554406836515 |
| positive_normalized_flux_mean | 0.0349854185239659 |
| flux_cv | 0.640934857044404 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -20.8 |
| lra_lu | 6 |
| true_peak_dbfs | -4.2 |
| silence_seconds | 14.4776190000001 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -20.8 LUFS<br>    Threshold: -31.3 LUFS<br><br>  Loudness range:<br>    LRA:         6.0 LU<br>    Threshold: -41.4 LUFS<br>    LRA low:   -25.2 LUFS<br>    LRA high:  -19.2 LUFS<br><br>  True peak:<br>    Peak:       -4.2 dBFS<br>[out#0/null @ 000001a5d4694ec0] video:0KiB audio:52145KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:05:02.70 bitrate=N/A speed= 107x elapsed=0:00:02.83 |
| ffmpeg_stderr_sha256 | 96d15aa67f99d11250862122c9971939df80a821ac14d3128aae09178f54c0e6 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 113.814467 | 114.490726 | 0.676259000000002 | 0.676259 |
| 115.980317 | 117.423424 | 1.443107 | 1.443107 |
| 118.540317 | 120.033265 | 1.492948 | 1.492948 |
| 120.484104 | 121.080726 | 0.596621999999996 | 0.596621 |
| 121.550726 | 122.083719 | 0.532993000000005 | 0.532993 |
| 124.539751 | 125.283673 | 0.743921999999998 | 0.743923 |
| 126.310295 | 127.754626 | 1.44433100000001 | 1.444331 |
| 164.298481 | 164.912653 | 0.614171999999996 | 0.614172 |
| 290.473129 | 292.693356 | 2.22022700000002 | 2.220227 |
| 294.150272 | 295.413923 | 1.26365100000004 | 1.263651 |
| 296.935601 | 298.123673 | 1.18807199999998 | 1.188073 |
| 298.871474 | 299.730771 | 0.859297000000026 | 0.859297 |
| 300.283265 | 301.685283 | 1.40201800000006 | 1.402018 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 61 |
| samples | 61 |
| brightness_mean | 0.733632928035298 |
| saturation_mean | 0.144776353619772 |
| frame_difference_mean | 0.0484127803206017 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 1790.13333333333 | 1790.13333333333 | 0.74669474363327 | 0.125714869281046 | N/A | N/A | N/A |
| 1795.13333333333 | 1795.13333333333 | 0.74576723575592 | 0.126376089324619 | 0.0100648142397404 | 0.0441429308267854 | 5 |
| 1800.13333333333 | 1800.13333333333 | 0.744271516799927 | 0.13028022875817 | 0.0629466250538826 | 0.225702494959534 | 5 |
| 1805.13333333333 | 1805.13333333333 | 0.735205888748169 | 0.157491830065359 | 0.0590193346142769 | 0.162525442793517 | 5 |
| 1810.13333333333 | 1810.13333333333 | 0.745343148708344 | 0.147522331154684 | 0.0705059915781021 | 0.226450256853283 | 5 |
| 1815.13333333333 | 1815.13333333333 | 0.745564579963684 | 0.148287854030501 | 0.0052486383356154 | 0.0178434477198556 | 5 |
| 1820.13333333333 | 1820.13333333333 | 0.747079789638519 | 0.128931917211329 | 0.0792151391506195 | 0.174229197672837 | 5 |
| 1825.13333333333 | 1825.13333333333 | 0.744856476783752 | 0.128381263616558 | 0.0643785372376442 | 0.220185236490153 | 5 |
| 1830.13333333333 | 1830.13333333333 | 0.743206799030304 | 0.147748638344227 | 0.0647706910967827 | 0.225361611904739 | 5 |
| 1835.13333333333 | 1835.13333333333 | 0.745974659919739 | 0.148157135076253 | 0.0194281041622162 | 0.048755514871335 | 5 |
| 1840.13333333333 | 1840.13333333333 | 0.731649875640869 | 0.160597494553377 | 0.0684948265552521 | 0.214581896163671 | 5 |
| 1845.13333333333 | 1845.13333333333 | 0.757362484931946 | 0.144195533769063 | 0.0661467835307121 | 0.165377566489925 | 5 |
| 1850.13333333333 | 1850.13333333333 | 0.757107853889465 | 0.141471405228758 | 0.0192241296172142 | 0.0470281712669919 | 5 |
| 1855.13333333333 | 1855.13333333333 | 0.742749214172363 | 0.130868736383442 | 0.0551642142236233 | 0.159456234350623 | 5 |
| 1860.13333333333 | 1860.13333333333 | 0.746419131755829 | 0.126952614379085 | 0.0683594793081284 | 0.229844439316853 | 5 |
| 1865.13333333333 | 1865.13333333333 | 0.733363032341003 | 0.156803376906318 | 0.0723545774817467 | 0.255356122357788 | 5 |
| 1870.13333333333 | 1870.13333333333 | 0.731144905090332 | 0.161939270152505 | 0.0166968945413828 | 0.0382672528241484 | 5 |
| 1875.13333333333 | 1875.13333333333 | 0.759123921394348 | 0.140372549019608 | 0.0680634528398514 | 0.157084903001879 | 5 |
| 1880.13333333333 | 1880.13333333333 | 0.757877767086029 | 0.142941448801743 | 0.0232723299413919 | 0.0384117354278006 | 5 |
| 1885.13333333333 | 1885.13333333333 | 0.748669445514679 | 0.13032788671024 | 0.0703412294387817 | 0.240801952011485 | 5 |
| 1890.13333333333 | 1890.13333333333 | 0.749030232429504 | 0.13009477124183 | 0.0109283765777946 | 0.0390262295634755 | 5 |
| 1895.13333333333 | 1895.13333333333 | 0.730553925037384 | 0.150095043572985 | 0.0734289214015007 | 0.225823068816431 | 5 |
| 1900.13333333333 | 1900.13333333333 | 0.758859157562256 | 0.142497004357298 | 0.0701783746480942 | 0.223488146446341 | 5 |
| 1905.13333333333 | 1905.13333333333 | 0.690469145774841 | 0.130562908496732 | 0.111526139080524 | 0.271365105212497 | 5 |
| 1910.13333333333 | 1910.13333333333 | 0.690483927726746 | 0.1306424291939 | 0.000222222210140899 | 0.0102558233254022 | 5 |
| 1915.13333333333 | 1915.13333333333 | 0.74129194021225 | 0.146824346405229 | 0.0889294669032097 | 0.220094219741639 | 5 |
| 1920.13333333333 | 1920.13333333333 | 0.724029719829559 | 0.150658496732026 | 0.0768428668379784 | 0.136606223918594 | 5 |
| 1925.13333333333 | 1925.13333333333 | 0.741930544376373 | 0.148247276688453 | 0.0783469453454018 | 0.135332651238746 | 5 |
| 1930.13333333333 | 1930.13333333333 | 0.74286276102066 | 0.14782734204793 | 0.0185133442282677 | 0.0549403025889723 | 5 |
| 1935.13333333333 | 1935.13333333333 | 0.719394147396088 | 0.15312091503268 | 0.0705019012093544 | 0.134471048590431 | 5 |
| 1940.13333333333 | 1940.13333333333 | 0.721936583518982 | 0.152543845315904 | 0.0226737465709448 | 0.0455576524437069 | 5 |
| 1945.13333333333 | 1945.13333333333 | 0.725742638111115 | 0.148067265795207 | 0.0347102396190166 | 0.0922054525174518 | 5 |
| 1950.13333333333 | 1950.13333333333 | 0.742079794406891 | 0.148971132897603 | 0.0759466215968132 | 0.160043149550341 | 5 |
| 1955.13333333333 | 1955.13333333333 | 0.715840995311737 | 0.257037854030501 | 0.0607905760407448 | 0.433862523235071 | 5 |
| 1960.13333333333 | 1960.13333333333 | 0.718582808971405 | 0.149697440087146 | 0.055801197886467 | 0.430314436244717 | 5 |
| 1965.13333333333 | 1965.13333333333 | 0.72426962852478 | 0.147409586056645 | 0.0228284299373627 | 0.0585159624508566 | 5 |
| 1970.13333333333 | 1970.13333333333 | 0.724488854408264 | 0.144662581699346 | 0.0171348042786121 | 0.0616435398728034 | 5 |
| 1975.13333333333 | 1975.13333333333 | 0.719100773334503 | 0.14727614379085 | 0.0701195597648621 | 0.130200023176676 | 5 |
| 1980.13333333333 | 1980.13333333333 | 0.717919647693634 | 0.146744553376906 | 0.0202219504863024 | 0.0684392034116298 | 5 |
| 1985.13333333333 | 1985.13333333333 | 0.724119901657104 | 0.145546023965142 | 0.0687132328748703 | 0.125067625054703 | 5 |
| 1990.13333333333 | 1990.13333333333 | 0.723923563957214 | 0.143819444444444 | 0.0052126906812191 | 0.0614872739209451 | 5 |
| 1995.13333333333 | 1995.13333333333 | 0.720490515232086 | 0.148578976034858 | 0.0235043559223413 | 0.0719146443692164 | 5 |
| 2000.13333333333 | 2000.13333333333 | 0.724464356899261 | 0.144136165577342 | 0.0709967315196991 | 0.123436288859699 | 5 |
| 2005.13333333333 | 2005.13333333333 | 0.724168002605438 | 0.14487037037037 | 0.0256579499691725 | 0.0508583842807638 | 5 |
| 2010.13333333333 | 2010.13333333333 | 0.723751962184906 | 0.146001361655773 | 0.0670811459422112 | 0.113840339569892 | 5 |
| 2015.13333333333 | 2015.13333333333 | 0.717236757278442 | 0.150436819172113 | 0.0191405229270458 | 0.0521842430648937 | 5 |
| 2020.13333333333 | 2020.13333333333 | 0.717149496078491 | 0.149939814814815 | 0.00453975982964039 | 0.0364861779097427 | 5 |
| 2025.13333333333 | 2025.13333333333 | 0.724065065383911 | 0.145625272331155 | 0.0197990201413631 | 0.0539535377447196 | 5 |
| 2030.13333333333 | 2030.13333333333 | 0.723999202251434 | 0.145816176470588 | 0.0048790848813951 | 0.0404231337219682 | 5 |
| 2035.13333333333 | 2035.13333333333 | 0.723611652851105 | 0.144887254901961 | 0.0696729347109795 | 0.12037378748421 | 5 |
| 2040.13333333333 | 2040.13333333333 | 0.721867680549622 | 0.144588235294118 | 0.0368447713553905 | 0.0503763416492272 | 5 |
| 2045.13333333333 | 2045.13333333333 | 0.723086357116699 | 0.145607298474946 | 0.0710961297154427 | 0.1133387268449 | 5 |
| 2050.13333333333 | 2050.13333333333 | 0.718097984790802 | 0.14905582788671 | 0.0242736916989088 | 0.059858753228784 | 4.99999999999977 |
| 2055.13333333333 | 2055.13333333333 | 0.717991292476654 | 0.148838235294118 | 0.00398148177191615 | 0.0332365998557324 | 5 |
| 2060.13333333333 | 2060.13333333333 | 0.717042207717896 | 0.14659477124183 | 0.0634376332163811 | 0.115694829513638 | 5 |
| 2065.13333333333 | 2065.13333333333 | 0.72504585981369 | 0.146082244008715 | 0.0662649720907211 | 0.123315105194593 | 5 |
| 2070.13333333333 | 2070.13333333333 | 0.72126442193985 | 0.147198529411765 | 0.0660078972578049 | 0.118871390774207 | 5 |
| 2075.13333333333 | 2075.13333333333 | 0.72421795129776 | 0.145951525054466 | 0.0722589865326881 | 0.126416409206906 | 5 |
| 2080.13333333333 | 2080.13333333333 | 0.724544942378998 | 0.145415577342048 | 0.0717284828424454 | 0.12077105185694 | 5 |
| 2085.13333333333 | 2085.13333333333 | 0.801504969596863 | 0.101455610021786 | 0.101308539509773 | 0.239122246451283 | 5 |
| 2090.13333333333 | 2090.13333333333 | 0.801664769649506 | 0.10256862745098 | 0.00502532627433538 | 0.0610118472064769 | 5 |


## Record 10 — M01: Dear009

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 971af2fbd1d7f3825b9f15415841cc2ec4f3d31461711a03811cb6e1783feab2 |
| started_utc | 2026-09-10T06:20:27.683975+00:00 |
| completed_utc | 2026-09-10T06:20:36.182294+00:00 |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear009 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| size_bytes | 116784561 |
| sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| start_s | 2092.83333333333 |
| end_s | 2398.36666666667 |
| duration_s | 305.533333333333 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 62785 to 71951 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-009, frames/M01_frame_header_08.jpg, frames/M01_frame_header_09.jpg, adv_dear_hmsz_009.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear009 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 62785 to 71951 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-009, frames/M01_frame_header_08.jpg, frames/M01_frame_header_09.jpg, adv_dear_hmsz_009.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 2092.83333333333 |
| parameters.end_s | 2398.36666666667 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 44818944 |
| streams[0].duration | 2917.900000 |
| streams[0].bit_rate | 180317 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 87537 |
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
| streams[1].duration_ts | 128681984 |
| streams[1].duration | 2917.958821 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 125666 |
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
| streams[2].duration_ts | 262616294 |
| streams[2].duration | 2917.958822 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2917.958821 |
| format.size | 116784561 |
| format.bit_rate | 320181 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20250516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=18Eb02aeTH0 |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 6737010 |
| analyzed_audio_duration_s | 305.533333333333 |
| stft_frames | 13155 |
| flux_transitions | 13154 |
| rms_linear | 0.0858013432965254 |
| rms_p10_linear | 0.0129055280027681 |
| rms_p90_linear | 0.147024301326699 |
| rms_p90_p10_db | 21.132266935485 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 548 |
| centroid_hz_mean | 2084.04033529056 |
| flatness_mean | 0.0701813208582747 |
| positive_normalized_flux_mean | 0.0306566508047263 |
| flux_cv | 0.644254681348855 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -20 |
| lra_lu | 8.6 |
| true_peak_dbfs | -3.2 |
| silence_seconds | 16.264877 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -20.0 LUFS<br>    Threshold: -30.9 LUFS<br><br>  Loudness range:<br>    LRA:         8.6 LU<br>    Threshold: -41.0 LUFS<br>    LRA low:   -25.1 LUFS<br>    LRA high:  -16.5 LUFS<br><br>  True peak:<br>    Peak:       -3.2 dBFS<br>[out#0/null @ 000001c9a8285ac0] video:0KiB audio:52633KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:05:05.53 bitrate=N/A speed=99.4x elapsed=0:00:03.07 |
| ffmpeg_stderr_sha256 | 20f5332a09e1eb408011b44750e3f01eb5511c72faa2dd2bbd8cb26110168471 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 62.796689 | 64.599728 | 1.803039 | 1.803039 |
| 99.31619 | 100.003719 | 0.687528999999998 | 0.687528 |
| 100.146803 | 100.651497 | 0.504694000000001 | 0.504694 |
| 104.333696 | 105.780227 | 1.44653099999999 | 1.446531 |
| 173.471701 | 174.046032 | 0.574331000000001 | 0.574331 |
| 176.120998 | 176.976417 | 0.855419000000012 | 0.85542 |
| 177.732608 | 178.467211 | 0.734602999999993 | 0.734603 |
| 252.946757 | 254.124218 | 1.17746100000002 | 1.17746 |
| 257.007914 | 257.57644 | 0.568525999999963 | 0.568526 |
| 257.847937 | 259.247098 | 1.39916099999999 | 1.399161 |
| 294.937302 | 297.286735 | 2.34943300000003 | 2.349433 |
| 298.224218 | 299.776213 | 1.55199499999998 | 1.551995 |
| 300.485578 | 301.517098 | 1.03152 | 1.031519 |
| 303.023696 | 304.604331 | 1.58063500000003 | 1.580635 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 62 |
| samples | 62 |
| brightness_mean | 0.708428906096566 |
| saturation_mean | 0.170007282662169 |
| frame_difference_mean | 0.073647401013152 |
| histogram_jumps_gt_0_5 | 5 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 2092.83333333333 | 2092.83333333333 | 0.76337069272995 | 0.158136165577342 | N/A | N/A | N/A |
| 2097.83333333333 | 2097.83333333333 | 0.763003826141357 | 0.157635348583878 | 0.00571051193401217 | 0.0616750587732478 | 5 |
| 2102.83333333333 | 2102.83333333333 | 0.767321884632111 | 0.157559640522876 | 0.0156726576387882 | 0.0570734658725342 | 5 |
| 2107.83333333333 | 2107.83333333333 | 0.765907108783722 | 0.149979847494553 | 0.0629349127411842 | 0.15482407100912 | 5 |
| 2112.83333333333 | 2112.83333333333 | 0.762422680854797 | 0.149822167755991 | 0.0134283760562539 | 0.0591529053666201 | 5 |
| 2117.83333333333 | 2117.83333333333 | 0.763555586338043 | 0.15192211328976 | 0.00612745061516762 | 0.0616122874385403 | 5 |
| 2122.83333333333 | 2122.83333333333 | 0.759981274604797 | 0.152079793028322 | 0.0165258701890707 | 0.040792502663098 | 5 |
| 2127.83333333333 | 2127.83333333333 | 0.767734229564667 | 0.150576252723312 | 0.0663929730653763 | 0.165629012363409 | 5 |
| 2132.83333333333 | 2132.83333333333 | 0.764996230602264 | 0.150229847494553 | 0.0657478198409081 | 0.158054558480304 | 5 |
| 2137.83333333333 | 2137.83333333333 | 0.762400031089783 | 0.151677832244009 | 0.0141740180552006 | 0.0423962637220743 | 5 |
| 2142.83333333333 | 2142.83333333333 | 0.760439872741699 | 0.152262254901961 | 0.0137886703014374 | 0.0271880419064567 | 5 |
| 2147.83333333333 | 2147.83333333333 | 0.768425166606903 | 0.150249455337691 | 0.0648965090513229 | 0.161280098094368 | 5 |
| 2152.83333333333 | 2152.83333333333 | 0.768200993537903 | 0.152490196078431 | 0.0291549563407898 | 0.0482103306747915 | 5 |
| 2157.83333333333 | 2157.83333333333 | 0.228724405169487 | 0.407087690631808 | 0.562172114849091 | 0.817391281954001 | 5 |
| 2162.83333333333 | 2162.83333333333 | 0.232749193906784 | 0.368418845315904 | 0.134527519345284 | 0.408131187663405 | 5 |
| 2167.83333333333 | 2167.83333333333 | 0.239445835351944 | 0.265285403050109 | 0.110196083784103 | 0.736942390702815 | 5 |
| 2172.83333333333 | 2172.83333333333 | 0.364720046520233 | 0.241031590413943 | 0.191890254616737 | 0.498792504144132 | 5 |
| 2177.83333333333 | 2177.83333333333 | 0.335991561412811 | 0.265914488017429 | 0.175318360328674 | 0.42809386436194 | 5 |
| 2182.83333333333 | 2182.83333333333 | 0.390585273504257 | 0.252589596949891 | 0.159288123250008 | 0.585309096863833 | 5 |
| 2187.83333333333 | 2187.83333333333 | 0.285383701324463 | 0.343732026143791 | 0.144958600401878 | 0.785747462172567 | 5 |
| 2192.83333333333 | 2192.83333333333 | 0.751236140727997 | 0.160376089324619 | 0.4943006336689 | 0.912575935955935 | 5 |
| 2197.83333333333 | 2197.83333333333 | 0.762806951999664 | 0.151047930283224 | 0.0225561000406742 | 0.0751078890482188 | 5 |
| 2202.83333333333 | 2202.83333333333 | 0.760300993919373 | 0.150598039215686 | 0.0137848574668169 | 0.0455732240470251 | 5 |
| 2207.83333333333 | 2207.83333333333 | 0.768507361412048 | 0.151919662309368 | 0.0634079501032829 | 0.179356563550293 | 5 |
| 2212.83333333333 | 2212.83333333333 | 0.767761766910553 | 0.152529139433551 | 0.0284330043941736 | 0.0426591388225019 | 5 |
| 2217.83333333333 | 2217.83333333333 | 0.763182759284973 | 0.151593137254902 | 0.0653376877307892 | 0.160839774334535 | 5 |
| 2222.83333333333 | 2222.83333333333 | 0.761733949184418 | 0.152364651416122 | 0.00979901943355799 | 0.02715130778335 | 5 |
| 2227.83333333333 | 2227.83333333333 | 0.761353015899658 | 0.150543300653595 | 0.00596160162240267 | 0.0650350993622858 | 5 |
| 2232.83333333333 | 2232.83333333333 | 0.761244058609009 | 0.152050381263617 | 0.0135381268337369 | 0.0587338437802044 | 5 |
| 2237.83333333333 | 2237.83333333333 | 0.766797661781311 | 0.153526960784314 | 0.064616285264492 | 0.164189451023482 | 5 |
| 2242.83333333333 | 2242.83333333333 | 0.767820298671722 | 0.151947167755991 | 0.0298902485519648 | 0.0444397755035475 | 5 |
| 2247.83333333333 | 2247.83333333333 | 0.763787031173706 | 0.149757352941176 | 0.0654025003314018 | 0.166076421281544 | 5 |
| 2252.83333333333 | 2252.83333333333 | 0.762239158153534 | 0.155595043572985 | 0.0672478154301643 | 0.178485553519268 | 5 |
| 2257.83333333333 | 2257.83333333333 | 0.767259001731873 | 0.152402777777778 | 0.0252513606101274 | 0.0616870121011939 | 5 |
| 2262.83333333333 | 2262.83333333333 | 0.756770431995392 | 0.146399782135076 | 0.0182080585509539 | 0.177809442886316 | 5 |
| 2267.83333333333 | 2267.83333333333 | 0.763707518577576 | 0.167135893246187 | 0.0768112689256668 | 0.253455865903515 | 5 |
| 2272.83333333333 | 2272.83333333333 | 0.755008220672607 | 0.146062363834423 | 0.076025053858757 | 0.224394324394379 | 5 |
| 2277.83333333333 | 2277.83333333333 | 0.752550959587097 | 0.157210511982571 | 0.064042754471302 | 0.151002665618539 | 5 |
| 2282.83333333333 | 2282.83333333333 | 0.748233139514923 | 0.146964052287582 | 0.0607192255556583 | 0.170647725732306 | 5 |
| 2287.83333333333 | 2287.83333333333 | 0.762645721435547 | 0.151685185185185 | 0.0775111615657806 | 0.228369518517491 | 5 |
| 2292.83333333333 | 2292.83333333333 | 0.760431110858917 | 0.153363289760349 | 0.0173894334584475 | 0.0419676597844394 | 5 |
| 2297.83333333333 | 2297.83333333333 | 0.75333309173584 | 0.157342047930283 | 0.0622096918523312 | 0.150205818825252 | 5 |
| 2302.83333333333 | 2302.83333333333 | 0.751212418079376 | 0.157007080610022 | 0.0219060461968184 | 0.0626498146074251 | 5 |
| 2307.83333333333 | 2307.83333333333 | 0.769224464893341 | 0.151784586056645 | 0.0754989087581635 | 0.209541268493223 | 5 |
| 2312.83333333333 | 2312.83333333333 | 0.762471914291382 | 0.152850762527233 | 0.057626087218523 | 0.163631376060649 | 5 |
| 2317.83333333333 | 2317.83333333333 | 0.752181947231293 | 0.158610838779956 | 0.0648880749940872 | 0.158939465690452 | 5 |
| 2322.83333333333 | 2322.83333333333 | 0.75160676240921 | 0.157433823529412 | 0.0189302824437618 | 0.0456955869972911 | 5 |
| 2327.83333333333 | 2327.83333333333 | 0.763463795185089 | 0.151736111111111 | 0.06134994328022 | 0.153801995752401 | 5 |
| 2332.83333333333 | 2332.83333333333 | 0.751021265983582 | 0.150084422657952 | 0.0771794617176056 | 0.222712516458472 | 5 |
| 2337.83333333333 | 2337.83333333333 | 0.754481732845306 | 0.156816993464052 | 0.0640590935945511 | 0.158967725661304 | 5 |
| 2342.83333333333 | 2342.83333333333 | 0.762124240398407 | 0.152774782135076 | 0.0589414462447166 | 0.154323208410153 | 5 |
| 2347.83333333333 | 2347.83333333333 | 0.75577700138092 | 0.147784586056645 | 0.076290026307106 | 0.212763770639 | 5 |
| 2352.83333333333 | 2352.83333333333 | 0.75329601764679 | 0.157145152505447 | 0.0633289739489555 | 0.148698554185783 | 5 |
| 2357.83333333333 | 2357.83333333333 | 0.762728452682495 | 0.151299291938998 | 0.061066996306181 | 0.158892567009663 | 5 |
| 2362.83333333333 | 2362.83333333333 | 0.762465119361877 | 0.151611111111111 | 0.0131435180082917 | 0.0427431418390206 | 5 |
| 2367.83333333333 | 2367.83333333333 | 0.767641127109528 | 0.152184912854031 | 0.063446618616581 | 0.160664812655232 | 5 |
| 2372.83333333333 | 2372.83333333333 | 0.76398777961731 | 0.147906318082789 | 0.0663423165678978 | 0.166899961812918 | 5 |
| 2377.83333333333 | 2377.83333333333 | 0.76894611120224 | 0.151617374727669 | 0.0660836026072502 | 0.161813379953845 | 5 |
| 2382.83333333333 | 2382.83333333333 | 0.761976838111877 | 0.156525871459695 | 0.0402693338692188 | 0.0575393527063478 | 5 |
| 2387.83333333333 | 2387.83333333333 | 0.767872333526611 | 0.151818355119826 | 0.0452875830233097 | 0.062117412338009 | 5 |
| 2392.83333333333 | 2392.83333333333 | 0.804939389228821 | 0.106970860566449 | 0.0772211253643036 | 0.267269982775917 | 5 |
| 2397.83333333333 | 2397.83333333333 | 0.681103527545929 | 0.185392973856209 | 0.144282400608063 | 0.319850496321662 | 5 |


## Record 11 — M01: Dear010

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 47f35069062a812b111d6091f57b1edd183b3c01d229b5e1d57e6ff8a3f94958 |
| started_utc | 2026-09-10T06:20:31.890890+00:00 |
| completed_utc | 2026-09-10T06:20:41.857962+00:00 |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear010 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| size_bytes | 116784561 |
| sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| start_s | 2398.36666666667 |
| end_s | 2753.2 |
| duration_s | 354.833333333333 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 71951 to 82596 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-010, frames/M01_frame_header_09.jpg, frames/M01_frame_header_10.jpg, adv_dear_hmsz_010.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be |
| source_id | 1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd |
| character | MISUZU |
| alias | M01 |
| label | Dear010 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 71951 to 82596 at 30 fps. Evidence: EXEC-MZ-M01-BOUNDARY-010, frames/M01_frame_header_09.jpg, frames/M01_frame_header_10.jpg, adv_dear_hmsz_010.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 2398.36666666667 |
| parameters.end_s | 2753.2 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 44818944 |
| streams[0].duration | 2917.900000 |
| streams[0].bit_rate | 180317 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 87537 |
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
| streams[1].duration_ts | 128681984 |
| streams[1].duration | 2917.958821 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 125666 |
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
| streams[2].duration_ts | 262616294 |
| streams[2].duration | 2917.958822 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 2917.958821 |
| format.size | 116784561 |
| format.bit_rate | 320181 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20250516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=18Eb02aeTH0 |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！<br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 7824075 |
| analyzed_audio_duration_s | 354.833333333333 |
| stft_frames | 15278 |
| flux_transitions | 15277 |
| rms_linear | 0.089381980300737 |
| rms_p10_linear | 0.0135256508532155 |
| rms_p90_linear | 0.157141660770199 |
| rms_p90_p10_db | 21.3026633245836 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 453 |
| centroid_hz_mean | 1833.04290214292 |
| flatness_mean | 0.0480409838656202 |
| positive_normalized_flux_mean | 0.0343005332402943 |
| flux_cv | 0.647724961591125 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -20.3 |
| lra_lu | 4.3 |
| true_peak_dbfs | -6.4 |
| silence_seconds | 14.7804089999998 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -20.3 LUFS<br>    Threshold: -31.2 LUFS<br><br>  Loudness range:<br>    LRA:         4.3 LU<br>    Threshold: -41.3 LUFS<br>    LRA low:   -23.8 LUFS<br>    LRA high:  -19.5 LUFS<br><br>  True peak:<br>    Peak:       -6.4 dBFS<br>[out#0/null @ 000001f1ddc54e80] video:0KiB audio:61126KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:05:54.83 bitrate=N/A speed= 121x elapsed=0:00:02.94 |
| ffmpeg_stderr_sha256 | 7ea2cdf621484ef2ca8155ff1d610b0b18d510274fa7e85e58f7168975814ce6 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 144.181247 | 144.749342 | 0.568095 | 0.568095 |
| 165.934467 | 166.473878 | 0.539411000000001 | 0.53941 |
| 168.497846 | 169.172676 | 0.674829999999986 | 0.67483 |
| 169.957007 | 170.72059 | 0.763582999999983 | 0.763583 |
| 172.33068 | 173.150522 | 0.819841999999994 | 0.819841 |
| 288.010023 | 290.111134 | 2.101111 | 2.101111 |
| 290.989025 | 292.880726 | 1.89170099999996 | 1.891701 |
| 294.735624 | 295.592562 | 0.856938000000014 | 0.856939 |
| 297.67746 | 298.25644 | 0.578980000000001 | 0.57898 |
| 300.038005 | 301.509773 | 1.471768 | 1.471769 |
| 302.968526 | 304.928118 | 1.95959199999999 | 1.959592 |
| 306.945125 | 307.498073 | 0.552947999999958 | 0.552948 |
| 309.347619 | 310.321111 | 0.973491999999965 | 0.973492 |
| 353.805215 | 354.833333 | 1.02811800000001 | 1.028118 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 71 |
| samples | 71 |
| brightness_mean | 0.719330592054716 |
| saturation_mean | 0.180216016140415 |
| frame_difference_mean | 0.0399182613057617 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 2398.36666666667 | 2398.36666666667 | 0.726882636547089 | 0.180754901960784 | N/A | N/A | N/A |
| 2403.36666666667 | 2403.36666666667 | 0.694037079811096 | 0.186445261437909 | 0.0626549497246742 | 0.172501254202515 | 5 |
| 2408.36666666667 | 2408.36666666667 | 0.720416486263275 | 0.179779684095861 | 0.065715417265892 | 0.176193925419042 | 5 |
| 2413.36666666667 | 2413.36666666667 | 0.721317827701569 | 0.179052015250545 | 0.00574564235284925 | 0.0539164242422592 | 5 |
| 2418.36666666667 | 2418.36666666667 | 0.725773096084595 | 0.18347385620915 | 0.065721683204174 | 0.130073595525422 | 5 |
| 2423.36666666667 | 2423.36666666667 | 0.698286831378937 | 0.186179193899782 | 0.0626595839858055 | 0.16616865568651 | 5 |
| 2428.36666666667 | 2428.36666666667 | 0.696891903877258 | 0.186492374727669 | 0.0146601302549243 | 0.0473677380300099 | 5 |
| 2433.36666666667 | 2433.36666666667 | 0.719370365142822 | 0.18033605664488 | 0.0646113827824593 | 0.182058866068375 | 5 |
| 2438.36666666667 | 2438.36666666667 | 0.721353232860565 | 0.182056917211329 | 0.0264741275459528 | 0.0497071112032324 | 5 |
| 2443.36666666667 | 2443.36666666667 | 0.68878972530365 | 0.182185185185185 | 0.0684872046113014 | 0.214458021242835 | 5 |
| 2448.36666666667 | 2448.36666666667 | 0.728603541851044 | 0.181765522875817 | 0.0764580592513084 | 0.209385470318199 | 5 |
| 2453.36666666667 | 2453.36666666667 | 0.730089366436005 | 0.182133986928105 | 0.0183404143899679 | 0.0425690770977711 | 5 |
| 2458.36666666667 | 2458.36666666667 | 0.727510631084442 | 0.183793572984749 | 0.0196157414466143 | 0.05252907949598 | 5 |
| 2463.36666666667 | 2463.36666666667 | 0.695278584957123 | 0.186114379084967 | 0.0683137252926826 | 0.172732635685084 | 5 |
| 2468.36666666667 | 2468.36666666667 | 0.694632351398468 | 0.186088779956427 | 0.00512336567044258 | 0.0377598467903207 | 5 |
| 2473.36666666667 | 2473.36666666667 | 0.689250528812408 | 0.182875544662309 | 0.0605947710573673 | 0.120116874788894 | 5 |
| 2478.36666666667 | 2478.36666666667 | 0.716286242008209 | 0.183175108932462 | 0.0671718418598175 | 0.203831032960751 | 5 |
| 2483.36666666667 | 2483.36666666667 | 0.69404149055481 | 0.18644362745098 | 0.0662551745772362 | 0.190216333962816 | 5 |
| 2488.36666666667 | 2488.36666666667 | 0.697260618209839 | 0.185715958605664 | 0.0183815360069275 | 0.0719821973628632 | 5 |
| 2493.36666666667 | 2493.36666666667 | 0.717609226703644 | 0.18090522875817 | 0.0632347464561462 | 0.183052178386018 | 5 |
| 2498.36666666667 | 2498.36666666667 | 0.71688050031662 | 0.183359204793028 | 0.0190038122236729 | 0.0548356049423174 | 5 |
| 2503.36666666667 | 2503.36666666667 | 0.715980410575867 | 0.183571895424837 | 0.00864950940012932 | 0.0359241855401397 | 5 |
| 2508.36666666667 | 2508.36666666667 | 0.691922128200531 | 0.18727559912854 | 0.0633937940001488 | 0.187509081179466 | 5 |
| 2513.36666666667 | 2513.36666666667 | 0.696218132972717 | 0.186138616557734 | 0.0178717337548733 | 0.0507513446863158 | 5 |
| 2518.36666666667 | 2518.36666666667 | 0.727049589157104 | 0.184058006535948 | 0.0666718408465385 | 0.172390402286245 | 5 |
| 2523.36666666667 | 2523.36666666667 | 0.685656070709229 | 0.183773420479303 | 0.0732023417949677 | 0.208995418085376 | 5 |
| 2528.36666666667 | 2528.36666666667 | 0.690817534923553 | 0.181442810457516 | 0.0240699891000986 | 0.0508333797664296 | 5 |
| 2533.36666666667 | 2533.36666666667 | 0.695636749267578 | 0.185511710239651 | 0.0599389970302582 | 0.108274493913238 | 5 |
| 2538.36666666667 | 2538.36666666667 | 0.717505753040314 | 0.180950163398693 | 0.0675776153802872 | 0.172214096590318 | 5 |
| 2543.36666666667 | 2543.36666666667 | 0.705842614173889 | 0.1903401416122 | 0.0836086645722389 | 0.14839922763444 | 5 |
| 2548.36666666667 | 2548.36666666667 | 0.724147975444794 | 0.18371977124183 | 0.0286691151559353 | 0.111936129970796 | 5 |
| 2553.36666666667 | 2553.36666666667 | 0.719852149486542 | 0.18067211328976 | 0.0623594745993614 | 0.106583254345545 | 5 |
| 2558.36666666667 | 2558.36666666667 | 0.719310224056244 | 0.181562908496732 | 0.0326334424316883 | 0.0633186389794776 | 5 |
| 2563.36666666667 | 2563.36666666667 | 0.719715416431427 | 0.180923747276688 | 0.00754302879795432 | 0.040119761217863 | 5 |
| 2568.36666666667 | 2568.36666666667 | 0.729093432426453 | 0.182742919389978 | 0.0678006559610367 | 0.116839408436742 | 5 |
| 2573.36666666667 | 2573.36666666667 | 0.724021553993225 | 0.183683006535948 | 0.0191906318068504 | 0.0489738207953966 | 5 |
| 2578.36666666667 | 2578.36666666667 | 0.724379658699036 | 0.18374128540305 | 0.00590441189706326 | 0.0448622359825579 | 5 |
| 2583.36666666667 | 2583.36666666667 | 0.718731820583344 | 0.181523420479303 | 0.0599283762276173 | 0.110117412827615 | 5 |
| 2588.36666666667 | 2588.36666666667 | 0.720451235771179 | 0.181967320261438 | 0.026136165484786 | 0.0626963353091472 | 5 |
| 2593.36666666667 | 2593.36666666667 | 0.725952446460724 | 0.183436274509804 | 0.0648420453071594 | 0.11518173475628 | 5 |
| 2598.36666666667 | 2598.36666666667 | 0.729937195777893 | 0.182026960784314 | 0.0181236397475004 | 0.0384286664351595 | 5 |
| 2603.36666666667 | 2603.36666666667 | 0.730457305908203 | 0.182044117647059 | 0.00524237425997853 | 0.0412030103943717 | 5 |
| 2608.36666666667 | 2608.36666666667 | 0.721986770629883 | 0.184892973856209 | 0.0205321330577135 | 0.0540625826343132 | 5 |
| 2613.36666666667 | 2613.36666666667 | 0.727294921875 | 0.181654411764706 | 0.0211661234498024 | 0.0546730873917686 | 5 |
| 2618.36666666667 | 2618.36666666667 | 0.722937405109406 | 0.18143137254902 | 0.069766066968441 | 0.115319166758346 | 5 |
| 2623.36666666667 | 2623.36666666667 | 0.723408460617065 | 0.181544934640523 | 0.0130479307845235 | 0.0413179941266077 | 5 |
| 2628.36666666667 | 2628.36666666667 | 0.725111961364746 | 0.182347766884532 | 0.0675514712929726 | 0.126084210621356 | 5 |
| 2633.36666666667 | 2633.36666666667 | 0.723841309547424 | 0.183967320261438 | 0.0168698262423277 | 0.0667260526136586 | 5 |
| 2638.36666666667 | 2638.36666666667 | 0.725513398647308 | 0.183106481481481 | 0.00933932512998581 | 0.0281979323699575 | 5 |
| 2643.36666666667 | 2643.36666666667 | 0.719871938228607 | 0.17978022875817 | 0.0616767443716526 | 0.105061175115982 | 5 |
| 2648.36666666667 | 2648.36666666667 | 0.717407405376434 | 0.180391612200436 | 0.020482026040554 | 0.0539796716737324 | 5 |
| 2653.36666666667 | 2653.36666666667 | 0.717450439929962 | 0.180869553376906 | 0.00767810456454754 | 0.0331159500321577 | 5 |
| 2658.36666666667 | 2658.36666666667 | 0.719792723655701 | 0.179433551198257 | 0.0265078991651535 | 0.050941774997674 | 5 |
| 2663.36666666667 | 2663.36666666667 | 0.720328450202942 | 0.178969498910675 | 0.00844580586999655 | 0.0364157084613283 | 5 |
| 2668.36666666667 | 2668.36666666667 | 0.721847832202911 | 0.18466394335512 | 0.0644038617610931 | 0.11391676132167 | 5 |
| 2673.36666666667 | 2673.36666666667 | 0.72587114572525 | 0.183629901960784 | 0.0178861655294895 | 0.0469142530558053 | 5 |
| 2678.36666666667 | 2678.36666666667 | 0.725333631038666 | 0.183394335511983 | 0.0107091497629881 | 0.0430471946318863 | 5 |
| 2683.36666666667 | 2683.36666666667 | 0.728467345237732 | 0.182615468409586 | 0.0175694450736046 | 0.0446765290998266 | 5 |
| 2688.36666666667 | 2688.36666666667 | 0.727459192276001 | 0.181077614379085 | 0.0233071893453598 | 0.0579904302829971 | 5 |
| 2693.36666666667 | 2693.36666666667 | 0.727341771125793 | 0.181329520697168 | 0.00151770154479891 | 0.0160953072576444 | 5 |
| 2698.36666666667 | 2698.36666666667 | 0.717793405056 | 0.181911220043573 | 0.0648578405380249 | 0.115484143199712 | 5 |
| 2703.36666666667 | 2703.36666666667 | 0.718079030513763 | 0.182162309368192 | 0.00734177604317665 | 0.0211180681296353 | 5 |
| 2708.36666666667 | 2708.36666666667 | 0.721187651157379 | 0.179971677559913 | 0.0275487471371889 | 0.0481444112680445 | 5 |
| 2713.36666666667 | 2713.36666666667 | 0.724663138389587 | 0.184196078431373 | 0.0614297352731228 | 0.112565256458579 | 5 |
| 2718.36666666667 | 2718.36666666667 | 0.724443376064301 | 0.18273720043573 | 0.00229221140034497 | 0.0501804670086822 | 5 |
| 2723.36666666667 | 2723.36666666667 | 0.724915087223053 | 0.183742374727669 | 0.00586873572319746 | 0.056795080570205 | 5 |
| 2728.36666666667 | 2728.36666666667 | 0.720058619976044 | 0.180685185185185 | 0.0637426450848579 | 0.106113724392189 | 5 |
| 2733.36666666667 | 2733.36666666667 | 0.660136222839355 | 0.158873638344227 | 0.0798483118414879 | 0.283097563712766 | 5 |
| 2738.36666666667 | 2738.36666666667 | 0.828611373901367 | 0.103883986928105 | 0.171089574694633 | 0.358735105386542 | 5 |
| 2743.36666666667 | 2743.36666666667 | 0.789208889007568 | 0.13999537037037 | 0.0421879068017006 | 0.257494695226791 | 5 |
| 2748.36666666667 | 2748.36666666667 | 0.788867473602295 | 0.141845043572985 | 0.00703267939388752 | 0.0565786173729222 | 5 |


## Record 12 — M04: Dear028

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | c002d590f8ce58cbb0efec477f241b58d0c28f7b002c21fa8f2629ff75d3faab |
| started_utc | 2026-09-10T06:20:37.177859+00:00 |
| completed_utc | 2026-09-10T06:20:43.785196+00:00 |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear028 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| size_bytes | 193460076 |
| sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| start_s | 0.966666666666667 |
| end_s | 329.8 |
| duration_s | 328.833333333333 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 29 to 9894 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-028, frames/M04_frame_header_00.jpg, frames/M04_frame_header_01.jpg, adv_dear_hmsz_028.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear028 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 29 to 9894 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-028, frames/M04_frame_header_00.jpg, frames/M04_frame_header_01.jpg, adv_dear_hmsz_028.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 0.966666666666667 |
| parameters.end_s | 329.8 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 62185984 |
| streams[0].duration | 4048.566667 |
| streams[0].bit_rate | 243484 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 121457 |
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
| streams[1].duration_ts | 178544640 |
| streams[1].duration | 4048.631293 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 174360 |
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
| streams[2].duration_ts | 364376816 |
| streams[2].duration | 4048.631289 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 4048.631293 |
| format.size | 193460076 |
| format.bit_rate | 382272 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20260516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=Loj480JIDkI |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 7250775 |
| analyzed_audio_duration_s | 328.833333333333 |
| stft_frames | 14158 |
| flux_transitions | 14157 |
| rms_linear | 0.107897841206558 |
| rms_p10_linear | 0.02242238931611 |
| rms_p90_linear | 0.184002935070885 |
| rms_p90_p10_db | 18.282857234222 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 386 |
| centroid_hz_mean | 2316.8269620902 |
| flatness_mean | 0.0571159602044328 |
| positive_normalized_flux_mean | 0.0338202537987399 |
| flux_cv | 0.585087444049618 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -19 |
| lra_lu | 4.5 |
| true_peak_dbfs | -2.7 |
| silence_seconds | 11.780543 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -19.0 LUFS<br>    Threshold: -29.6 LUFS<br><br>  Loudness range:<br>    LRA:         4.5 LU<br>    Threshold: -39.7 LUFS<br>    LRA low:   -22.2 LUFS<br>    LRA high:  -17.7 LUFS<br><br>  True peak:<br>    Peak:       -2.7 dBFS<br>[out#0/null @ 0000022e44208f40] video:0KiB audio:56647KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:05:28.83 bitrate=N/A speed= 133x elapsed=0:00:02.47 |
| ffmpeg_stderr_sha256 | d942625c86d4238feab2eb3b37f111dc143a1bccced3c109b144c3bb147e1a9b |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 104.232472 | 104.844331 | 0.611858999999995 | 0.611859 |
| 107.316735 | 107.861451 | 0.544716000000008 | 0.544717 |
| 190.208231 | 190.906032 | 0.697800999999998 | 0.6978 |
| 193.932698 | 195.596916 | 1.66421800000001 | 1.664218 |
| 196.831406 | 197.423243 | 0.591837000000027 | 0.591837 |
| 199.494853 | 200.027914 | 0.533061000000004 | 0.533061 |
| 200.419773 | 203.268345 | 2.84857200000002 | 2.848571 |
| 263.018481 | 263.97746 | 0.958978999999999 | 0.95898 |
| 264.254014 | 265.633424 | 1.37941000000001 | 1.37941 |
| 266.403651 | 267.599025 | 1.19537399999996 | 1.195374 |
| 268.973447 | 269.728163 | 0.754715999999974 | 0.754717 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 66 |
| samples | 66 |
| brightness_mean | 0.488720617962606 |
| saturation_mean | 0.3469503036905 |
| frame_difference_mean | 0.0482064513704525 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 0.966666666666667 | 0.966666666666667 | 0.487822204828262 | 0.346136982570806 | N/A | N/A | N/A |
| 5.96666666666667 | 5.96666666666667 | 0.481810748577118 | 0.351261710239651 | 0.0211383439600468 | 0.0807052432741596 | 5 |
| 10.9666666666667 | 10.9666666666667 | 0.481900900602341 | 0.350705065359477 | 0.00805964041501284 | 0.0516121287011896 | 5 |
| 15.9666666666667 | 15.9666666666667 | 0.494719237089157 | 0.345360021786492 | 0.0772121399641037 | 0.151662678927791 | 5 |
| 20.9666666666667 | 20.9666666666667 | 0.487215429544449 | 0.347337962962963 | 0.0387570783495903 | 0.058459852781166 | 5 |
| 25.9666666666667 | 25.9666666666667 | 0.489462405443192 | 0.346324618736383 | 0.0210400335490704 | 0.04303528942918 | 5 |
| 30.9666666666667 | 30.9666666666667 | 0.494765520095825 | 0.343313453159041 | 0.0694921016693115 | 0.193898404095333 | 5 |
| 35.9666666666667 | 35.9666666666667 | 0.494559943675995 | 0.343522875816993 | 0.0244354568421841 | 0.057225355261756 | 5 |
| 40.9666666666667 | 40.9666666666667 | 0.493617117404938 | 0.344524237472767 | 0.00705446628853679 | 0.0450423951355913 | 5 |
| 45.9666666666667 | 45.9666666666667 | 0.484091520309448 | 0.344709967320261 | 0.065734751522541 | 0.141739818206835 | 5 |
| 50.9666666666667 | 50.9666666666667 | 0.491837441921234 | 0.347625816993464 | 0.0660416632890701 | 0.148837898258822 | 5 |
| 55.9666666666667 | 55.9666666666667 | 0.491258710622787 | 0.34786628540305 | 0.00483088241890073 | 0.0149975742503676 | 5 |
| 60.9666666666667 | 60.9666666666667 | 0.489113301038742 | 0.34910811546841 | 0.0626988038420677 | 0.157134310036172 | 5 |
| 65.9666666666667 | 65.9666666666667 | 0.488665580749512 | 0.343319989106754 | 0.0736029371619225 | 0.149509715602776 | 5 |
| 70.9666666666667 | 70.9666666666667 | 0.478128522634506 | 0.344194716775599 | 0.0679591447114944 | 0.200187360814933 | 5 |
| 75.9666666666667 | 75.9666666666667 | 0.476703703403473 | 0.344516612200436 | 0.0284793023020029 | 0.0600120166260055 | 5 |
| 80.9666666666667 | 80.9666666666667 | 0.491747558116913 | 0.348178921568627 | 0.0636914521455765 | 0.151277548341002 | 5 |
| 85.9666666666667 | 85.9666666666667 | 0.489692270755768 | 0.344729847494553 | 0.0668167248368263 | 0.144821996020166 | 5 |
| 90.9666666666667 | 90.9666666666667 | 0.488720864057541 | 0.34576334422658 | 0.00686465157195926 | 0.0411124308035879 | 5 |
| 95.9666666666667 | 95.9666666666667 | 0.490324109792709 | 0.347796296296296 | 0.0798929706215858 | 0.133515746042952 | 5 |
| 100.966666666667 | 100.966666666667 | 0.494007915258408 | 0.345898965141612 | 0.0268444959074259 | 0.0476006322543953 | 5 |
| 105.966666666667 | 105.966666666667 | 0.49134749174118 | 0.347313725490196 | 0.0659757629036903 | 0.195010659674023 | 5 |
| 110.966666666667 | 110.966666666667 | 0.491527497768402 | 0.347885893246187 | 0.0162627995014191 | 0.0341984792666694 | 5 |
| 115.966666666667 | 115.966666666667 | 0.487526953220367 | 0.348373910675381 | 0.0227282121777534 | 0.0562811309381663 | 5 |
| 120.966666666667 | 120.966666666667 | 0.490479052066803 | 0.348 | 0.0633578449487686 | 0.1382038669117 | 5 |
| 125.966666666667 | 125.966666666667 | 0.494478493928909 | 0.342280773420479 | 0.0838469415903091 | 0.150573556987639 | 5 |
| 130.966666666667 | 130.966666666667 | 0.489936292171478 | 0.34744825708061 | 0.0840345844626427 | 0.148880946319033 | 5 |
| 135.966666666667 | 135.966666666667 | 0.485458642244339 | 0.352136982570806 | 0.0245974939316511 | 0.0536107720327752 | 5 |
| 140.966666666667 | 140.966666666667 | 0.483240753412247 | 0.352114651416122 | 0.0250136163085699 | 0.0504940201587286 | 5 |
| 145.966666666667 | 145.966666666667 | 0.482495933771133 | 0.350085239651416 | 0.0212393775582314 | 0.0552619177986573 | 5 |
| 150.966666666667 | 150.966666666667 | 0.484780520200729 | 0.350396241830065 | 0.0702758729457855 | 0.136053803639949 | 5 |
| 155.966666666667 | 155.966666666667 | 0.484476864337921 | 0.349917211328976 | 0.0729098618030548 | 0.134829580030454 | 5 |
| 160.966666666667 | 160.966666666667 | 0.490351855754852 | 0.344974128540305 | 0.0737012550234795 | 0.144710295418315 | 5 |
| 165.966666666667 | 165.966666666667 | 0.484874457120895 | 0.34820288671024 | 0.0227377451956272 | 0.0595504359917327 | 5 |
| 170.966666666667 | 170.966666666667 | 0.485940337181091 | 0.337140522875817 | 0.060273963958025 | 0.17548061271873 | 5 |
| 175.966666666667 | 175.966666666667 | 0.497609227895737 | 0.344351579520697 | 0.0632799565792084 | 0.150911020901813 | 5 |
| 180.966666666667 | 180.966666666667 | 0.488002181053162 | 0.346276960784314 | 0.0649207457900047 | 0.149792454666817 | 5 |
| 185.966666666667 | 185.966666666667 | 0.4857497215271 | 0.341317265795207 | 0.07088752835989 | 0.183279852327668 | 5 |
| 190.966666666667 | 190.966666666667 | 0.49280121922493 | 0.348708333333333 | 0.0592464618384838 | 0.137344396580494 | 5 |
| 195.966666666667 | 195.966666666667 | 0.490594744682312 | 0.347695806100218 | 0.0614253804087639 | 0.155871168903632 | 5 |
| 200.966666666667 | 200.966666666667 | 0.496462970972061 | 0.343269880174292 | 0.0806726589798927 | 0.124184617475241 | 5 |
| 205.966666666667 | 205.966666666667 | 0.491393536329269 | 0.346440359477124 | 0.0817382782697678 | 0.128262226975791 | 5 |
| 210.966666666667 | 210.966666666667 | 0.482624709606171 | 0.351929466230937 | 0.0234861113131046 | 0.0670137683635773 | 5 |
| 215.966666666667 | 215.966666666667 | 0.499212443828583 | 0.348092864923747 | 0.0575675368309021 | 0.157771322040858 | 5 |
| 220.966666666667 | 220.966666666667 | 0.487739115953445 | 0.347632625272331 | 0.0686132907867432 | 0.20338835703084 | 5 |
| 225.966666666667 | 225.966666666667 | 0.486228764057159 | 0.346532679738562 | 0.00971241854131222 | 0.0483131013775751 | 5 |
| 230.966666666667 | 230.966666666667 | 0.493752479553223 | 0.345656590413943 | 0.0381642132997513 | 0.040404381319316 | 5 |
| 235.966666666667 | 235.966666666667 | 0.492305040359497 | 0.35205637254902 | 0.0678020119667053 | 0.203804819861941 | 5 |
| 240.966666666667 | 240.966666666667 | 0.493622839450836 | 0.34528894335512 | 0.017080882564187 | 0.0721156542558536 | 5 |
| 245.966666666667 | 245.966666666667 | 0.488914221525192 | 0.348754357298475 | 0.074733667075634 | 0.18323611980861 | 5 |
| 250.966666666667 | 250.966666666667 | 0.492501884698868 | 0.347037309368192 | 0.020855663344264 | 0.0517989441272041 | 5 |
| 255.966666666667 | 255.966666666667 | 0.493074327707291 | 0.343062363834423 | 0.0124308280646801 | 0.0551800035659996 | 5 |
| 260.966666666667 | 260.966666666667 | 0.491925925016403 | 0.348359477124183 | 0.08220124989748 | 0.130299013924339 | 4.99999999999997 |
| 265.966666666667 | 265.966666666667 | 0.48923447728157 | 0.346662581699346 | 0.0772393792867661 | 0.134435683355897 | 5 |
| 270.966666666667 | 270.966666666667 | 0.484606772661209 | 0.351366830065359 | 0.0736565813422203 | 0.143408474229739 | 5 |
| 275.966666666667 | 275.966666666667 | 0.4893679022789 | 0.348706699346405 | 0.0224670469760895 | 0.0541078376608827 | 5 |
| 280.966666666667 | 280.966666666667 | 0.486100494861603 | 0.350721132897603 | 0.0234035961329937 | 0.0430258017614059 | 5 |
| 285.966666666667 | 285.966666666667 | 0.487068355083466 | 0.347564814814815 | 0.0714667737483978 | 0.142285265212442 | 5 |
| 290.966666666667 | 290.966666666667 | 0.486848086118698 | 0.347538671023965 | 0.00934885628521442 | 0.0414943087639214 | 5 |
| 295.966666666667 | 295.966666666667 | 0.482632875442505 | 0.349782952069717 | 0.0738458558917046 | 0.145275544022547 | 5 |
| 300.966666666667 | 300.966666666667 | 0.483623653650284 | 0.351722766884532 | 0.0179232023656368 | 0.0510305296784652 | 5 |
| 305.966666666667 | 305.966666666667 | 0.491889446973801 | 0.348954793028322 | 0.0611241832375526 | 0.157454796336144 | 5 |
| 310.966666666667 | 310.966666666667 | 0.481030225753784 | 0.344963779956427 | 0.0613499507308006 | 0.143765353775977 | 5 |
| 315.966666666667 | 315.966666666667 | 0.484591275453568 | 0.342311274509804 | 0.0263044647872448 | 0.068801239494291 | 5 |
| 320.966666666667 | 320.966666666667 | 0.485243201255798 | 0.339126361655773 | 0.0156781040132046 | 0.0540900639118721 | 5 |
| 325.966666666667 | 325.966666666667 | 0.491728514432907 | 0.348367919389978 | 0.0571900866925716 | 0.175680153759104 | 5 |


## Record 13 — M04: Dear029

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | e29df1b941b2a978afa62b6279b3ebb4ebee7aff1f1b94c674ef3bf9fec1638d |
| started_utc | 2026-09-10T06:20:42.968553+00:00 |
| completed_utc | 2026-09-10T06:20:50.641591+00:00 |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear029 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| size_bytes | 193460076 |
| sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| start_s | 329.8 |
| end_s | 723.5 |
| duration_s | 393.7 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 9894 to 21705 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-029, frames/M04_frame_header_01.jpg, frames/M04_frame_header_02.jpg, adv_dear_hmsz_029.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear029 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 9894 to 21705 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-029, frames/M04_frame_header_01.jpg, frames/M04_frame_header_02.jpg, adv_dear_hmsz_029.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 329.8 |
| parameters.end_s | 723.5 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 62185984 |
| streams[0].duration | 4048.566667 |
| streams[0].bit_rate | 243484 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 121457 |
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
| streams[1].duration_ts | 178544640 |
| streams[1].duration | 4048.631293 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 174360 |
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
| streams[2].duration_ts | 364376816 |
| streams[2].duration | 4048.631289 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 4048.631293 |
| format.size | 193460076 |
| format.bit_rate | 382272 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20260516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=Loj480JIDkI |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 8681085 |
| analyzed_audio_duration_s | 393.7 |
| stft_frames | 16952 |
| flux_transitions | 16951 |
| rms_linear | 0.101389858036237 |
| rms_p10_linear | 0.0229153118190278 |
| rms_p90_linear | 0.171571152152331 |
| rms_p90_p10_db | 17.4863699286512 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 547 |
| centroid_hz_mean | 2078.48517595702 |
| flatness_mean | 0.0582229444468891 |
| positive_normalized_flux_mean | 0.035131852020238 |
| flux_cv | 0.607300618944734 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -19.6 |
| lra_lu | 5.4 |
| true_peak_dbfs | -2.7 |
| silence_seconds | 15.414964 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -19.6 LUFS<br>    Threshold: -30.0 LUFS<br><br>  Loudness range:<br>    LRA:         5.4 LU<br>    Threshold: -40.2 LUFS<br>    LRA low:   -23.1 LUFS<br>    LRA high:  -17.7 LUFS<br><br>  True peak:<br>    Peak:       -2.7 dBFS<br>[out#0/null @ 000002867a6fc8c0] video:0KiB audio:67821KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:06:33.70 bitrate=N/A speed= 191x elapsed=0:00:02.06 |
| ffmpeg_stderr_sha256 | 5514f056aa628a7c7b26bccc99b5073d27ef483b1f7259a6c8bc6882fd797472 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 12.894739 | 13.646576 | 0.751837 | 0.751837 |
| 15.718141 | 16.260431 | 0.542290000000001 | 0.54229 |
| 36.289274 | 36.850998 | 0.561723999999998 | 0.561723 |
| 37.313741 | 38.119025 | 0.805284 | 0.805283 |
| 114.053991 | 115.506757 | 1.452766 | 1.452766 |
| 117.364014 | 118.80678 | 1.44276600000001 | 1.442766 |
| 120.533424 | 121.859932 | 1.326508 | 1.326508 |
| 159.653356 | 161.336893 | 1.683537 | 1.683537 |
| 256.374014 | 259.145306 | 2.77129200000002 | 2.771293 |
| 260.940794 | 262.073129 | 1.13233500000001 | 1.132336 |
| 263.305465 | 264.134626 | 0.829160999999999 | 0.829161 |
| 265.661429 | 267.776893 | 2.11546399999997 | 2.115465 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 79 |
| samples | 79 |
| brightness_mean | 0.489572311881222 |
| saturation_mean | 0.368969705744464 |
| frame_difference_mean | 0.0560148376911783 |
| histogram_jumps_gt_0_5 | 2 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 329.8 | 329.8 | 0.476915031671524 | 0.370425653594771 | N/A | N/A | N/A |
| 334.8 | 334.8 | 0.409263610839844 | 0.34958197167756 | 0.150257617235184 | 0.448601197704504 | 5 |
| 339.8 | 339.8 | 0.4799844622612 | 0.359363834422658 | 0.14810810983181 | 0.436220754670403 | 5 |
| 344.8 | 344.8 | 0.530679166316986 | 0.363320533769063 | 0.141500264406204 | 0.302994244087761 | 5 |
| 349.8 | 349.8 | 0.564760625362396 | 0.338265795206972 | 0.0819795727729797 | 0.263871971044081 | 5 |
| 354.8 | 354.8 | 0.496580332517624 | 0.37065059912854 | 0.0908910632133484 | 0.246646055483494 | 5 |
| 359.8 | 359.8 | 0.497914224863052 | 0.371220860566449 | 0.0204575154930353 | 0.0735651042439247 | 5 |
| 364.8 | 364.8 | 0.48790717124939 | 0.364761982570806 | 0.116338789463043 | 0.359361236330978 | 5 |
| 369.8 | 369.8 | 0.422390282154083 | 0.449254357298475 | 0.156998366117477 | 0.452482195531481 | 5 |
| 374.8 | 374.8 | 0.50716370344162 | 0.439162854030501 | 0.0997516363859177 | 0.382715725106976 | 5 |
| 379.8 | 379.8 | 0.507841825485229 | 0.436916666666667 | 0.0111072985455394 | 0.0310895171076494 | 5 |
| 384.8 | 384.8 | 0.492750316858292 | 0.481998366013072 | 0.0629302784800529 | 0.547850701909945 | 5 |
| 389.8 | 389.8 | 0.486772328615189 | 0.420712418300654 | 0.0623227097094059 | 0.535224925101506 | 5 |
| 394.8 | 394.8 | 0.514712154865265 | 0.395334422657952 | 0.0613951534032822 | 0.211292085203249 | 5 |
| 399.8 | 399.8 | 0.529577612876892 | 0.395497549019608 | 0.0419210232794285 | 0.110696031976047 | 5 |
| 404.8 | 404.8 | 0.477842062711716 | 0.422232298474946 | 0.0757366493344307 | 0.227918858128086 | 5 |
| 409.8 | 409.8 | 0.469771534204483 | 0.424048474945534 | 0.036664217710495 | 0.152698208448469 | 5 |
| 414.8 | 414.8 | 0.527596652507782 | 0.398009259259259 | 0.0812200382351875 | 0.245880854693287 | 5 |
| 419.8 | 419.8 | 0.481094211339951 | 0.422009531590414 | 0.0728646516799927 | 0.230006957835947 | 5 |
| 424.8 | 424.8 | 0.468417227268219 | 0.425860566448802 | 0.0277543570846319 | 0.0970150578277837 | 5 |
| 429.8 | 429.8 | 0.482709139585495 | 0.423626361655773 | 0.0267265792936087 | 0.115292499321821 | 5 |
| 434.8 | 434.8 | 0.51914519071579 | 0.395114106753813 | 0.0680552870035172 | 0.220319851351947 | 5 |
| 439.8 | 439.8 | 0.531772315502167 | 0.394716503267974 | 0.0431533232331276 | 0.127552304610142 | 5 |
| 444.8 | 444.8 | 0.481434404850006 | 0.41963834422658 | 0.076487198472023 | 0.221762953375447 | 5 |
| 449.8 | 449.8 | 0.465926468372345 | 0.420296296296296 | 0.0229899231344461 | 0.142622210680673 | 5 |
| 454.8 | 454.8 | 0.532171308994293 | 0.394911492374728 | 0.088975764811039 | 0.2555974602672 | 5 |
| 459.8 | 459.8 | 0.523809671401978 | 0.395291394335512 | 0.0429547913372517 | 0.109287632406873 | 5 |
| 464.8 | 464.8 | 0.525206446647644 | 0.393669934640523 | 0.0250269584357738 | 0.0522805663349028 | 5 |
| 469.8 | 469.8 | 0.490901976823807 | 0.422414488017429 | 0.0646492317318916 | 0.220964929894388 | 5 |
| 474.8 | 474.8 | 0.465502738952637 | 0.425254901960784 | 0.0375757105648518 | 0.149166229319145 | 5 |
| 479.8 | 479.8 | 0.48428350687027 | 0.425174564270152 | 0.0342644341289997 | 0.163964292232815 | 5 |
| 484.8 | 484.8 | 0.527753591537476 | 0.397124455337691 | 0.0685746148228645 | 0.220888282640879 | 5 |
| 489.8 | 489.8 | 0.482568889856339 | 0.400635620915033 | 0.0557145960628986 | 0.26207088913734 | 5 |
| 494.8 | 494.8 | 0.494297683238983 | 0.348873638344227 | 0.0830980464816093 | 0.320421799809461 | 5 |
| 499.8 | 499.8 | 0.482099413871765 | 0.353222494553377 | 0.0591650307178497 | 0.164314281807933 | 5 |
| 504.8 | 504.8 | 0.475098073482513 | 0.346195806100218 | 0.065081425011158 | 0.193860268174504 | 5 |
| 509.8 | 509.8 | 0.482593685388565 | 0.344116557734205 | 0.0314896516501904 | 0.0612152288190037 | 5 |
| 514.8 | 514.8 | 0.483599662780762 | 0.344143246187364 | 0.014768517576158 | 0.0490474649708238 | 4.99999999999994 |
| 519.8 | 519.8 | 0.491338223218918 | 0.348390795206972 | 0.0726388916373253 | 0.202206663036235 | 5 |
| 524.8 | 524.8 | 0.486216217279434 | 0.351062908496732 | 0.0225326791405678 | 0.0542802522471763 | 5 |
| 529.8 | 529.8 | 0.491330623626709 | 0.34784885620915 | 0.0239183008670807 | 0.0767759514578663 | 5 |
| 534.8 | 534.8 | 0.492011189460754 | 0.345902233115468 | 0.00678785424679518 | 0.0506652165061507 | 5 |
| 539.8 | 539.8 | 0.490972220897675 | 0.345911220043573 | 0.00640332233160734 | 0.0442967572321383 | 5 |
| 544.8 | 544.8 | 0.479641109704971 | 0.345362472766885 | 0.0701165571808815 | 0.177869680708556 | 5 |
| 549.8 | 549.8 | 0.486228227615356 | 0.349347494553377 | 0.0595054440200329 | 0.198121224479941 | 5 |
| 554.8 | 554.8 | 0.486695021390915 | 0.34782788671024 | 0.0274188444018364 | 0.049372754913436 | 5 |
| 559.8 | 559.8 | 0.496708601713181 | 0.348900871459695 | 0.0684586018323898 | 0.196014050643494 | 5 |
| 564.8 | 564.8 | 0.491465121507645 | 0.349190359477124 | 0.0269537009298801 | 0.0534567134884477 | 5 |
| 569.8 | 569.8 | 0.494718432426453 | 0.345377995642702 | 0.0193436816334724 | 0.0634056390814706 | 5 |
| 574.8 | 574.8 | 0.493645429611206 | 0.345468681917211 | 0.00473638344556093 | 0.0232549482133288 | 5 |
| 579.8 | 579.8 | 0.484438747167587 | 0.33967265795207 | 0.0670808851718903 | 0.15109045987977 | 5 |
| 584.8 | 584.8 | 0.486235290765762 | 0.340725762527233 | 0.0322655215859413 | 0.0728999335232492 | 5 |
| 589.8 | 589.8 | 0.45286899805069 | 0.332657407407407 | 0.106629349291325 | 0.334874383856373 | 5 |
| 594.8 | 594.8 | 0.453088790178299 | 0.332344498910675 | 0.00433850754052401 | 0.0409524058617945 | 5 |
| 599.8 | 599.8 | 0.494078427553177 | 0.347633986928105 | 0.100031584501266 | 0.296996818996085 | 5 |
| 604.8 | 604.8 | 0.490027219057083 | 0.349660130718954 | 0.0191704798489809 | 0.0592901042942358 | 5 |
| 609.8 | 609.8 | 0.491051763296127 | 0.347911764705882 | 0.023242374882102 | 0.0572024156286139 | 5 |
| 614.8 | 614.8 | 0.492897599935532 | 0.347397875816993 | 0.0148845324292779 | 0.04319809576436 | 5 |
| 619.8 | 619.8 | 0.496230125427246 | 0.34521105664488 | 0.0207802280783653 | 0.058854167588773 | 5 |
| 624.8 | 624.8 | 0.495269626379013 | 0.345771786492375 | 0.0744899213314056 | 0.194869051251227 | 5 |
| 629.8 | 629.8 | 0.495417207479477 | 0.345490740740741 | 0.0106993466615677 | 0.0418579346567325 | 5 |
| 634.8 | 634.8 | 0.492647379636765 | 0.348952069716776 | 0.030568353831768 | 0.0641842010526114 | 5 |
| 639.8 | 639.8 | 0.497667521238327 | 0.348916938997821 | 0.0681770145893097 | 0.192144059232007 | 5 |
| 644.8 | 644.8 | 0.491721659898758 | 0.349350762527233 | 0.0231756530702114 | 0.070008138181054 | 5 |
| 649.8 | 649.8 | 0.484416097402573 | 0.339407407407407 | 0.0639030486345291 | 0.15874315523877 | 5 |
| 654.8 | 654.8 | 0.494626104831696 | 0.346058006535948 | 0.063898965716362 | 0.154994050201455 | 5 |
| 659.8 | 659.8 | 0.491558015346527 | 0.343729302832244 | 0.0678850710391998 | 0.191322321359528 | 5 |
| 664.8 | 664.8 | 0.496501117944717 | 0.347491557734205 | 0.0625078976154327 | 0.188070256854892 | 5 |
| 669.8 | 669.8 | 0.491461575031281 | 0.347656862745098 | 0.0230623632669449 | 0.0611171605293681 | 5 |
| 674.8 | 674.8 | 0.491970092058182 | 0.344518246187364 | 0.00909558869898319 | 0.0541469233995737 | 5 |
| 679.8 | 679.8 | 0.556043267250061 | 0.302198529411765 | 0.0818592086434364 | 0.307488512103334 | 5 |
| 684.8 | 684.8 | 0.440936833620071 | 0.338787854030501 | 0.150978490710258 | 0.383335265952338 | 5 |
| 689.8 | 689.8 | 0.485672950744629 | 0.345501906318083 | 0.123933814466 | 0.325292527494626 | 5 |
| 694.8 | 694.8 | 0.48832380771637 | 0.347025054466231 | 0.0311541389673948 | 0.0636856170316094 | 5 |
| 699.8 | 699.8 | 0.485225766897202 | 0.3478401416122 | 0.0329896509647369 | 0.0543045701911608 | 5 |
| 704.8 | 704.8 | 0.49152398109436 | 0.345788126361656 | 0.0808592066168785 | 0.139278548235294 | 5 |
| 709.8 | 709.8 | 0.441107869148254 | 0.338425108932462 | 0.113793030381203 | 0.291692996172932 | 5 |
| 714.8 | 714.8 | 0.440108120441437 | 0.340949618736383 | 0.00459885597229004 | 0.0427525655427567 | 5 |
| 719.8 | 719.8 | 0.441317558288574 | 0.337891612200436 | 0.00533959688618779 | 0.0461945935936819 | 5 |


## Record 14 — M04: Dear030

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 58aebe208752d8a04836597c4675f96ab33c0adc5f5bf0f241a8ec12e5555d8d |
| started_utc | 2026-09-10T06:20:44.347246+00:00 |
| completed_utc | 2026-09-10T06:20:51.270246+00:00 |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear030 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| size_bytes | 193460076 |
| sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| start_s | 723.5 |
| end_s | 1010.73333333333 |
| duration_s | 287.233333333333 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 21705 to 30322 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-030, frames/M04_frame_header_02.jpg, frames/M04_frame_header_03.jpg, adv_dear_hmsz_030.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear030 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 21705 to 30322 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-030, frames/M04_frame_header_02.jpg, frames/M04_frame_header_03.jpg, adv_dear_hmsz_030.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 723.5 |
| parameters.end_s | 1010.73333333333 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 62185984 |
| streams[0].duration | 4048.566667 |
| streams[0].bit_rate | 243484 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 121457 |
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
| streams[1].duration_ts | 178544640 |
| streams[1].duration | 4048.631293 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 174360 |
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
| streams[2].duration_ts | 364376816 |
| streams[2].duration | 4048.631289 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 4048.631293 |
| format.size | 193460076 |
| format.bit_rate | 382272 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20260516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=Loj480JIDkI |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 6333495 |
| analyzed_audio_duration_s | 287.233333333333 |
| stft_frames | 12367 |
| flux_transitions | 12366 |
| rms_linear | 0.100289400220931 |
| rms_p10_linear | 0.0195896557009454 |
| rms_p90_linear | 0.178541258153492 |
| rms_p90_p10_db | 19.1942357552226 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 602 |
| centroid_hz_mean | 2282.28163760772 |
| flatness_mean | 0.0795979083401595 |
| positive_normalized_flux_mean | 0.0319507357104718 |
| flux_cv | 0.624524829722643 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -19.5 |
| lra_lu | 7.4 |
| true_peak_dbfs | -2.9 |
| silence_seconds | 15.854376 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -19.5 LUFS<br>    Threshold: -30.0 LUFS<br><br>  Loudness range:<br>    LRA:         7.4 LU<br>    Threshold: -40.1 LUFS<br>    LRA low:   -24.9 LUFS<br>    LRA high:  -17.5 LUFS<br><br>  True peak:<br>    Peak:       -2.9 dBFS<br>[out#0/null @ 000001987b98fa80] video:0KiB audio:49480KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:04:47.23 bitrate=N/A speed= 124x elapsed=0:00:02.32 |
| ffmpeg_stderr_sha256 | 69a586d407911f9beda0d996cff70660fdbb64db586cf94cadef16b33dd8378e |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 68.317392 | 69.585556 | 1.268164 | 1.268163 |
| 94.434762 | 98.711746 | 4.276984 | 4.276984 |
| 113.451134 | 119.536145 | 6.08501100000001 | 6.085011 |
| 157.288912 | 158.098481 | 0.809568999999982 | 0.809569 |
| 216.924853 | 217.952902 | 1.02804899999998 | 1.02805 |
| 218.90839 | 219.741519 | 0.833129000000014 | 0.833129 |
| 222.69678 | 223.551678 | 0.85489800000002 | 0.854898 |
| 224.801088 | 225.49966 | 0.698572000000013 | 0.698571 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 58 |
| samples | 58 |
| brightness_mean | 0.515464722082533 |
| saturation_mean | 0.345144861392833 |
| frame_difference_mean | 0.0526990251484932 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 723.5 | 723.5 | 0.488554745912552 | 0.351135620915033 | N/A | N/A | N/A |
| 728.5 | 728.5 | 0.475888878107071 | 0.343802559912854 | 0.0842159613966942 | 0.150073083305187 | 5 |
| 733.5 | 733.5 | 0.482674837112427 | 0.358164215686274 | 0.0870206952095032 | 0.159134215419273 | 5 |
| 738.5 | 738.5 | 0.469349712133408 | 0.346713507625272 | 0.085544653236866 | 0.168613992109472 | 5 |
| 743.5 | 743.5 | 0.491840153932571 | 0.363791394335512 | 0.0864403620362282 | 0.201770604546322 | 5 |
| 748.5 | 748.5 | 0.486333340406418 | 0.364582788671024 | 0.042193628847599 | 0.0869154333836074 | 5 |
| 753.5 | 753.5 | 0.467898964881897 | 0.350961873638344 | 0.0843052864074707 | 0.19993168197561 | 5 |
| 758.5 | 758.5 | 0.472609490156174 | 0.349316721132898 | 0.0285650882869959 | 0.0494221575923979 | 5 |
| 763.5 | 763.5 | 0.469436585903168 | 0.351275326797386 | 0.0375656299293041 | 0.0584516481404302 | 5 |
| 768.5 | 768.5 | 0.4735327064991 | 0.344856753812636 | 0.0789817497134209 | 0.159355438570565 | 5 |
| 773.5 | 773.5 | 0.477989137172699 | 0.338429738562092 | 0.0408469475805759 | 0.0733794530282729 | 5 |
| 778.5 | 778.5 | 0.488921314477921 | 0.35388371459695 | 0.0899049565196037 | 0.204886557041756 | 5 |
| 783.5 | 783.5 | 0.490055561065674 | 0.361829248366013 | 0.07501170784235 | 0.12435849637047 | 5 |
| 788.5 | 788.5 | 0.500788986682892 | 0.327285675381264 | 0.0847829505801201 | 0.254032030783988 | 5 |
| 793.5 | 793.5 | 0.492827087640762 | 0.326639433551198 | 0.0386154688894749 | 0.115853424785366 | 5 |
| 798.5 | 798.5 | 0.488372534513474 | 0.351693899782135 | 0.076793298125267 | 0.210748456687581 | 5 |
| 803.5 | 803.5 | 0.493122547864914 | 0.353305555555556 | 0.0314493477344513 | 0.0844086896999618 | 5 |
| 808.5 | 808.5 | 0.494768530130386 | 0.351751361655773 | 0.0110239656642079 | 0.0715497072794942 | 5 |
| 813.5 | 813.5 | 0.492054522037506 | 0.355925653594771 | 0.0412500016391277 | 0.0748423966833971 | 5 |
| 818.5 | 818.5 | 0.495006829500198 | 0.326064270152505 | 0.0722213983535767 | 0.201229997120119 | 5 |
| 823.5 | 823.5 | 0.4937464594841 | 0.32668954248366 | 0.0146056637167931 | 0.0384361711840413 | 5 |
| 828.5 | 828.5 | 0.492171287536621 | 0.326681917211329 | 0.0093131810426712 | 0.0412553750983511 | 5 |
| 833.5 | 833.5 | 0.495727956295013 | 0.328841503267974 | 0.0675397589802742 | 0.158607068857881 | 5 |
| 838.5 | 838.5 | 0.535267472267151 | 0.301316448801743 | 0.0754185765981674 | 0.336763592974443 | 5 |
| 843.5 | 843.5 | 0.49318465590477 | 0.329649237472767 | 0.0752401873469353 | 0.346102354257081 | 5 |
| 848.5 | 848.5 | 0.49147766828537 | 0.328330882352941 | 0.00777614396065474 | 0.0369069747775865 | 5 |
| 853.5 | 853.5 | 0.490331739187241 | 0.338942538126362 | 0.0593567527830601 | 0.115153432698518 | 5 |
| 858.5 | 858.5 | 0.48818302154541 | 0.340785947712418 | 0.032950434833765 | 0.0511664847407663 | 5 |
| 863.5 | 863.5 | 0.4927938580513 | 0.322610838779956 | 0.0741282626986504 | 0.166018495671798 | 5 |
| 868.5 | 868.5 | 0.495560497045517 | 0.322863834422658 | 0.0190133452415466 | 0.0633065870838137 | 5 |
| 873.5 | 873.5 | 0.494838804006577 | 0.329092047930283 | 0.0592260360717773 | 0.128602448235641 | 5 |
| 878.5 | 878.5 | 0.498988270759583 | 0.333750816993464 | 0.0669757649302483 | 0.104959316204515 | 5 |
| 883.5 | 883.5 | 0.521193623542786 | 0.349843409586057 | 0.0844210237264633 | 0.244200960280347 | 5 |
| 888.5 | 888.5 | 0.521125257015228 | 0.347891067538126 | 0.00740223284810781 | 0.0564307534624452 | 5 |
| 893.5 | 893.5 | 0.520844757556915 | 0.347739923747277 | 0.00571786519140005 | 0.0414633582638367 | 5 |
| 898.5 | 898.5 | 0.536343693733215 | 0.345008169934641 | 0.080986924469471 | 0.1571601041694 | 5 |
| 903.5 | 903.5 | 0.535999715328217 | 0.345773148148148 | 0.0095683541148901 | 0.0282400118473181 | 5 |
| 908.5 | 908.5 | 0.550702095031738 | 0.362601034858388 | 0.0770138874650002 | 0.168639412045618 | 5 |
| 913.5 | 913.5 | 0.549791097640991 | 0.35749591503268 | 0.0236418843269348 | 0.0539910294042622 | 5 |
| 918.5 | 918.5 | 0.521854043006897 | 0.35120234204793 | 0.0641952604055405 | 0.147610967188867 | 5 |
| 923.5 | 923.5 | 0.545638084411621 | 0.360223583877996 | 0.0636402517557144 | 0.147159595173967 | 5 |
| 928.5 | 928.5 | 0.495871752500534 | 0.342132897603486 | 0.0915560945868492 | 0.244919607827969 | 5 |
| 933.5 | 933.5 | 0.546923816204071 | 0.360114651416122 | 0.0917192250490189 | 0.246596674888503 | 5 |
| 938.5 | 938.5 | 0.548684597015381 | 0.359943355119826 | 0.0194373615086079 | 0.0488081814015145 | 5 |
| 943.5 | 943.5 | 0.55405992269516 | 0.356420751633987 | 0.0181666649878025 | 0.0388587095728843 | 5 |
| 948.5 | 948.5 | 0.591336071491241 | 0.335295479302832 | 0.0649667754769325 | 0.171264424812849 | 5 |
| 953.5 | 953.5 | 0.590392708778381 | 0.335669117647059 | 0.0104684084653854 | 0.0408389875345084 | 5 |
| 958.5 | 958.5 | 0.589964032173157 | 0.335697440087146 | 0.0269738528877497 | 0.0573634405849738 | 5 |
| 963.5 | 963.5 | 0.554591774940491 | 0.354826797385621 | 0.0666309893131256 | 0.163489892824685 | 5 |
| 968.5 | 968.5 | 0.554664790630341 | 0.354550108932462 | 0.00497113261371851 | 0.0445917235700919 | 5 |
| 973.5 | 973.5 | 0.520686566829681 | 0.351109477124183 | 0.0743126347661018 | 0.15424748506737 | 5 |
| 978.5 | 978.5 | 0.552284896373749 | 0.35701688453159 | 0.0669381767511368 | 0.160558434202169 | 5 |
| 983.5 | 983.5 | 0.546317279338837 | 0.361554193899782 | 0.0226533208042383 | 0.0634020073564008 | 5 |
| 988.5 | 988.5 | 0.55227530002594 | 0.35718137254902 | 0.0152303930372 | 0.052466941246212 | 5 |
| 993.5 | 993.5 | 0.582821071147919 | 0.34141339869281 | 0.0660566389560699 | 0.162242626173856 | 5 |
| 998.5 | 998.5 | 0.526366591453552 | 0.349089052287582 | 0.0800901353359222 | 0.225551505258961 | 5 |
| 1003.5 | 1003.5 | 0.547682523727417 | 0.359367647058824 | 0.0634106770157814 | 0.143218180802735 | 5 |
| 1008.5 | 1008.5 | 0.584239661693573 | 0.338275871459695 | 0.0653970614075661 | 0.177994596162461 | 5 |


## Record 15 — M04: Dear031

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 999b72a2e89e522050a74dc6a5262f1d784b818cc98b88805a309bd54fca0973 |
| started_utc | 2026-09-10T06:20:51.305990+00:00 |
| completed_utc | 2026-09-10T06:21:01.262624+00:00 |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear031 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| size_bytes | 193460076 |
| sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| start_s | 1010.73333333333 |
| end_s | 1461.33333333333 |
| duration_s | 450.6 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 30322 to 43840 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-031, frames/M04_frame_header_03.jpg, frames/M04_frame_header_04.jpg, adv_dear_hmsz_031.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear031 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 30322 to 43840 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-031, frames/M04_frame_header_03.jpg, frames/M04_frame_header_04.jpg, adv_dear_hmsz_031.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 1010.73333333333 |
| parameters.end_s | 1461.33333333333 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 62185984 |
| streams[0].duration | 4048.566667 |
| streams[0].bit_rate | 243484 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 121457 |
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
| streams[1].duration_ts | 178544640 |
| streams[1].duration | 4048.631293 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 174360 |
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
| streams[2].duration_ts | 364376816 |
| streams[2].duration | 4048.631289 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 4048.631293 |
| format.size | 193460076 |
| format.bit_rate | 382272 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20260516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=Loj480JIDkI |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 9935730 |
| analyzed_audio_duration_s | 450.6 |
| stft_frames | 19402 |
| flux_transitions | 19401 |
| rms_linear | 0.102689149735433 |
| rms_p10_linear | 0.0194027425880854 |
| rms_p90_linear | 0.175404632834927 |
| rms_p90_p10_db | 19.1235587571626 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 880 |
| centroid_hz_mean | 2266.47392905037 |
| flatness_mean | 0.0747701603454059 |
| positive_normalized_flux_mean | 0.0307476193412677 |
| flux_cv | 0.622049504370852 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -19.6 |
| lra_lu | 7.5 |
| true_peak_dbfs | -4.8 |
| silence_seconds | 24.373492 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -19.6 LUFS<br>    Threshold: -30.1 LUFS<br><br>  Loudness range:<br>    LRA:         7.5 LU<br>    Threshold: -40.2 LUFS<br>    LRA low:   -24.4 LUFS<br>    LRA high:  -16.9 LUFS<br><br>  True peak:<br>    Peak:       -4.8 dBFS<br>[out#0/null @ 00000168677bc000] video:0KiB audio:77623KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:07:30.60 bitrate=N/A speed= 164x elapsed=0:00:02.75 |
| ffmpeg_stderr_sha256 | 6f38192205764c7915b63423610413ece4671aa6203ad87a073b04bcc3e97cbe |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 6.097211 | 7.477914 | 1.380703 | 1.380703 |
| 91.499887 | 92.984422 | 1.48453499999999 | 1.484535 |
| 94.686712 | 95.483628 | 0.796915999999996 | 0.796916 |
| 97.758639 | 99.243265 | 1.48462599999999 | 1.484626 |
| 165.304558 | 166.093107 | 0.788549000000017 | 0.788549 |
| 214.946259 | 215.635828 | 0.689569000000006 | 0.689569 |
| 216.432268 | 217.6361 | 1.20383200000001 | 1.203832 |
| 218.118571 | 219.170272 | 1.05170100000001 | 1.051701 |
| 220.085692 | 220.655578 | 0.569885999999997 | 0.569887 |
| 221.109546 | 221.833107 | 0.723561000000018 | 0.72356 |
| 222.303175 | 227.766485 | 5.46330999999998 | 5.463311 |
| 255.414785 | 257.130907 | 1.71612199999998 | 1.716122 |
| 292.070975 | 293.386417 | 1.31544200000002 | 1.315442 |
| 377.967211 | 379.062381 | 1.09517 | 1.09517 |
| 379.426893 | 384.036463 | 4.60957000000002 | 4.609569 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 91 |
| samples | 91 |
| brightness_mean | 0.384857861877798 |
| saturation_mean | 0.340284654887596 |
| frame_difference_mean | 0.0679989924589689 |
| histogram_jumps_gt_0_5 | 4 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 1010.73333333333 | 1010.73333333333 | 0.373750299215317 | 0.33145288671024 | N/A | N/A | N/A |
| 1015.73333333333 | 1015.73333333333 | 0.319872856140137 | 0.344263616557734 | 0.0836955234408379 | 0.187650630415267 | 5 |
| 1020.73333333333 | 1020.73333333333 | 0.376382648944855 | 0.34927559912854 | 0.0781693980097771 | 0.183211435556606 | 5 |
| 1025.73333333333 | 1025.73333333333 | 0.375330328941345 | 0.347614379084967 | 0.0234493464231491 | 0.0591415871933677 | 5 |
| 1030.73333333333 | 1030.73333333333 | 0.39434477686882 | 0.334343409586057 | 0.080665297806263 | 0.246629747682855 | 5 |
| 1035.73333333333 | 1035.73333333333 | 0.389445245265961 | 0.332769335511983 | 0.0191446077078581 | 0.0487311339228373 | 5 |
| 1040.73333333333 | 1040.73333333333 | 0.380396783351898 | 0.349055010893246 | 0.0795381218194962 | 0.258083602465979 | 5 |
| 1045.73333333333 | 1045.73333333333 | 0.36892893910408 | 0.353865196078431 | 0.0270103476941586 | 0.0650355530819422 | 5 |
| 1050.73333333333 | 1050.73333333333 | 0.370702117681503 | 0.35190522875817 | 0.0267252177000046 | 0.0514682551809099 | 5 |
| 1055.73333333333 | 1055.73333333333 | 0.373522073030472 | 0.350174564270152 | 0.0223112739622593 | 0.0379240085125962 | 5 |
| 1060.73333333333 | 1060.73333333333 | 0.379800945520401 | 0.348171568627451 | 0.024282680824399 | 0.0534909487892846 | 5 |
| 1065.73333333333 | 1065.73333333333 | 0.380518525838852 | 0.349286492374728 | 0.0220797937363386 | 0.0616169029241438 | 5 |
| 1070.73333333333 | 1070.73333333333 | 0.367689549922943 | 0.353707516339869 | 0.0230718944221735 | 0.0700775284947046 | 5 |
| 1075.73333333333 | 1075.73333333333 | 0.438668578863144 | 0.343809640522876 | 0.0928210765123367 | 0.218688018458154 | 5 |
| 1080.73333333333 | 1080.73333333333 | 0.437416672706604 | 0.339333605664488 | 0.0488521233201027 | 0.065592839523596 | 5 |
| 1085.73333333333 | 1085.73333333333 | 0.435890793800354 | 0.342173747276688 | 0.0428728237748146 | 0.0651916802721432 | 5 |
| 1090.73333333333 | 1090.73333333333 | 0.375199109315872 | 0.334218409586057 | 0.0982532650232315 | 0.263505735655203 | 5 |
| 1095.73333333333 | 1095.73333333333 | 0.375858694314957 | 0.33298720043573 | 0.0130866020917892 | 0.0420974167711486 | 5 |
| 1100.73333333333 | 1100.73333333333 | 0.349704802036285 | 0.335374455337691 | 0.0515966787934303 | 0.137000281776818 | 5 |
| 1105.73333333333 | 1105.73333333333 | 0.348520427942276 | 0.336927559912854 | 0.0142061552032828 | 0.0550093502622245 | 5 |
| 1110.73333333333 | 1110.73333333333 | 0.348346412181854 | 0.333348583877996 | 0.0151429744437337 | 0.0480802593016166 | 5 |
| 1115.73333333333 | 1115.73333333333 | 0.356399804353714 | 0.347633986928105 | 0.0432026125490665 | 0.0809075354084004 | 5 |
| 1120.73333333333 | 1120.73333333333 | 0.367857068777084 | 0.349683006535948 | 0.0627927556633949 | 0.178701231173862 | 5 |
| 1125.73333333333 | 1125.73333333333 | 0.375338226556778 | 0.332994008714597 | 0.0684153065085411 | 0.191119801211852 | 5 |
| 1130.73333333333 | 1130.73333333333 | 0.37457600235939 | 0.348379357298475 | 0.0716821998357773 | 0.196025040934286 | 5 |
| 1135.73333333333 | 1135.73333333333 | 0.391948521137238 | 0.334555283224401 | 0.0799684077501297 | 0.245766167170892 | 5 |
| 1140.73333333333 | 1140.73333333333 | 0.391838520765305 | 0.333670206971678 | 0.024471677839756 | 0.0559158078701599 | 5 |
| 1145.73333333333 | 1145.73333333333 | 0.378815919160843 | 0.347290849673203 | 0.075559638440609 | 0.244664330708461 | 5 |
| 1150.73333333333 | 1150.73333333333 | 0.372826844453812 | 0.351309912854031 | 0.024251090362668 | 0.0469756941126329 | 5 |
| 1155.73333333333 | 1155.73333333333 | 0.370097786188126 | 0.353161492374728 | 0.0220950450748205 | 0.0575260952052445 | 5 |
| 1160.73333333333 | 1160.73333333333 | 0.374632358551025 | 0.332385076252723 | 0.0616064816713333 | 0.200231017993325 | 5 |
| 1165.73333333333 | 1165.73333333333 | 0.374130457639694 | 0.332219498910675 | 0.0210558269172907 | 0.0518711453919666 | 5 |
| 1170.73333333333 | 1170.73333333333 | 0.372216254472733 | 0.330111111111111 | 0.00697576208040118 | 0.057749886938343 | 5 |
| 1175.73333333333 | 1175.73333333333 | 0.438919454813004 | 0.415154139433551 | 0.136693358421326 | 0.356375353845298 | 5 |
| 1180.73333333333 | 1180.73333333333 | 0.444949060678482 | 0.402697984749455 | 0.0879419893026352 | 0.427378292782803 | 5 |
| 1185.73333333333 | 1185.73333333333 | 0.360956728458405 | 0.345445806100218 | 0.10670804977417 | 0.420341651611158 | 5 |
| 1190.73333333333 | 1190.73333333333 | 0.369788408279419 | 0.33594008714597 | 0.0905305072665215 | 0.198844328409177 | 5 |
| 1195.73333333333 | 1195.73333333333 | 0.446270436048508 | 0.402205610021786 | 0.112751632928848 | 0.395113060437057 | 5 |
| 1200.73333333333 | 1200.73333333333 | 0.445608109235764 | 0.402576252723312 | 0.00540413893759251 | 0.0419720232484713 | 5 |
| 1205.73333333333 | 1205.73333333333 | 0.326227426528931 | 0.348601579520697 | 0.137084424495697 | 0.452270137141146 | 5 |
| 1210.73333333333 | 1210.73333333333 | 0.396394640207291 | 0.332328703703704 | 0.0946378037333488 | 0.221266036259262 | 5 |
| 1215.73333333333 | 1215.73333333333 | 0.372778862714767 | 0.348778050108932 | 0.0801457017660141 | 0.23757522448113 | 5 |
| 1220.73333333333 | 1220.73333333333 | 0.339863538742065 | 0.323259531590414 | 0.0853918790817261 | 0.17694336953456 | 5 |
| 1225.73333333333 | 1225.73333333333 | 0.376163393259048 | 0.337354575163399 | 0.0709556043148041 | 0.143466576314626 | 5 |
| 1230.73333333333 | 1230.73333333333 | 0.390331417322159 | 0.335506263616558 | 0.0484055019915104 | 0.119325629544702 | 5 |
| 1235.73333333333 | 1235.73333333333 | 0.445696353912354 | 0.402574074074074 | 0.0910833328962326 | 0.371400219823463 | 5 |
| 1240.73333333333 | 1240.73333333333 | 0.477539479732513 | 0.378763071895425 | 0.0626917257905006 | 0.14035481435237 | 5 |
| 1245.73333333333 | 1245.73333333333 | 0.474494844675064 | 0.376425925925926 | 0.0322369262576103 | 0.0569491640993905 | 5 |
| 1250.73333333333 | 1250.73333333333 | 0.471301198005676 | 0.377443082788671 | 0.0342230387032032 | 0.0678250992661304 | 5 |
| 1255.73333333333 | 1255.73333333333 | 0.460890531539917 | 0.385186274509804 | 0.057230394333601 | 0.108667079151126 | 5 |
| 1260.73333333333 | 1260.73333333333 | 0.457861661911011 | 0.388028867102396 | 0.0198600217700005 | 0.0652460727823135 | 5 |
| 1265.73333333333 | 1265.73333333333 | 0.476509004831314 | 0.374214324618736 | 0.0576228201389313 | 0.121967852377911 | 5 |
| 1270.73333333333 | 1270.73333333333 | 0.287654966115952 | 0.415314814814815 | 0.306163936853409 | 0.717723439320061 | 5 |
| 1275.73333333333 | 1275.73333333333 | 0.271293312311172 | 0.451970860566449 | 0.156261444091797 | 0.33077760591654 | 5 |
| 1280.73333333333 | 1280.73333333333 | 0.294917196035385 | 0.43852614379085 | 0.162161499261856 | 0.401766225492783 | 5 |
| 1285.73333333333 | 1285.73333333333 | 0.398516058921814 | 0.226875272331155 | 0.189405515789986 | 0.835548177992771 | 5 |
| 1290.73333333333 | 1290.73333333333 | 0.439782440662384 | 0.142511165577342 | 0.169089868664742 | 0.384075357734406 | 5 |
| 1295.73333333333 | 1295.73333333333 | 0.418536782264709 | 0.115777777777778 | 0.22065195441246 | 0.374193382588373 | 5 |
| 1300.73333333333 | 1300.73333333333 | 0.59232622385025 | 0.175244553376906 | 0.282787322998047 | 0.578116164549274 | 5 |
| 1305.73333333333 | 1305.73333333333 | 0.376365482807159 | 0.348083333333333 | 0.44038999080658 | 0.677374613798299 | 5 |
| 1310.73333333333 | 1310.73333333333 | 0.367504924535751 | 0.352567538126362 | 0.0255653597414494 | 0.0597506796804637 | 5 |
| 1315.73333333333 | 1315.73333333333 | 0.368760913610458 | 0.352403594771242 | 0.0219771228730679 | 0.0538136865927776 | 5 |
| 1320.73333333333 | 1320.73333333333 | 0.368568390607834 | 0.353139433551198 | 0.00287990202195942 | 0.014412674297946 | 5 |
| 1325.73333333333 | 1325.73333333333 | 0.432991564273834 | 0.336146241830065 | 0.0883698239922523 | 0.213301015500705 | 5 |
| 1330.73333333333 | 1330.73333333333 | 0.340815097093582 | 0.316956154684096 | 0.13008987903595 | 0.263583439497023 | 5 |
| 1335.73333333333 | 1335.73333333333 | 0.341550439596176 | 0.317817810457516 | 0.00185403053183109 | 0.0168165284631593 | 5 |
| 1340.73333333333 | 1340.73333333333 | 0.340987205505371 | 0.314300653594771 | 0.00458986917510629 | 0.0424167923160818 | 5 |
| 1345.73333333333 | 1345.73333333333 | 0.340983957052231 | 0.316182734204793 | 0.00445969495922327 | 0.0416665755040673 | 5 |
| 1350.73333333333 | 1350.73333333333 | 0.434957772493362 | 0.334714869281046 | 0.131309911608696 | 0.261139323339476 | 5 |
| 1355.73333333333 | 1355.73333333333 | 0.433008998632431 | 0.339605119825708 | 0.0361078418791294 | 0.0921444402756249 | 5 |
| 1360.73333333333 | 1360.73333333333 | 0.375771284103394 | 0.349024509803922 | 0.0802671536803246 | 0.195363795471463 | 5 |
| 1365.73333333333 | 1365.73333333333 | 0.378071367740631 | 0.348194444444444 | 0.0283905249089003 | 0.0554627235848595 | 5 |
| 1370.73333333333 | 1370.73333333333 | 0.37652912735939 | 0.343877178649237 | 0.00826171040534973 | 0.0729898635979206 | 5 |
| 1375.73333333333 | 1375.73333333333 | 0.435592859983444 | 0.339154956427015 | 0.0807516276836395 | 0.190312667870473 | 5 |
| 1380.73333333333 | 1380.73333333333 | 0.433460533618927 | 0.336886710239651 | 0.03132189437747 | 0.06549743073949 | 5 |
| 1385.73333333333 | 1385.73333333333 | 0.340220600366592 | 0.320063180827887 | 0.131615191698074 | 0.250047175719774 | 5 |
| 1390.73333333333 | 1390.73333333333 | 0.373987227678299 | 0.331867647058824 | 0.0693880692124367 | 0.148288523850236 | 5 |
| 1395.73333333333 | 1395.73333333333 | 0.394506245851517 | 0.333978758169935 | 0.0524509809911251 | 0.133075251008334 | 5 |
| 1400.73333333333 | 1400.73333333333 | 0.3404401242733 | 0.321323801742919 | 0.0788423120975494 | 0.234096457138926 | 5 |
| 1405.73333333333 | 1405.73333333333 | 0.340684145689011 | 0.31729302832244 | 0.00452178623527288 | 0.0407688263309998 | 5 |
| 1410.73333333333 | 1410.73333333333 | 0.341126084327698 | 0.315203431372549 | 0.00479221111163497 | 0.041045764524314 | 5 |
| 1415.73333333333 | 1415.73333333333 | 0.340260893106461 | 0.31523311546841 | 0.00472903018817306 | 0.045818428691323 | 5 |
| 1420.73333333333 | 1420.73333333333 | 0.341067016124725 | 0.317207788671024 | 0.00487962923943996 | 0.0420157489323017 | 5 |
| 1425.73333333333 | 1425.73333333333 | 0.340219259262085 | 0.318242919389978 | 0.00456835469231009 | 0.0433905417466132 | 5 |
| 1430.73333333333 | 1430.73333333333 | 0.340603768825531 | 0.319364923747277 | 0.00226525031030178 | 0.017765289306407 | 5 |
| 1435.73333333333 | 1435.73333333333 | 0.339736670255661 | 0.314520697167756 | 0.00416230922564864 | 0.0441047468740989 | 5 |
| 1440.73333333333 | 1440.73333333333 | 0.395019054412842 | 0.33466802832244 | 0.0819468945264816 | 0.231328638792305 | 5 |
| 1445.73333333333 | 1445.73333333333 | 0.373487740755081 | 0.336673474945534 | 0.0554670467972755 | 0.138285205521401 | 5 |
| 1450.73333333333 | 1450.73333333333 | 0.370151698589325 | 0.335993191721133 | 0.0139602404087782 | 0.0480050625551263 | 5 |
| 1455.73333333333 | 1455.73333333333 | 0.392188221216202 | 0.337122004357298 | 0.0508878044784069 | 0.126192776728869 | 5 |
| 1460.73333333333 | 1460.73333333333 | 0.375906884670258 | 0.431935729847495 | 0.0916734710335732 | 0.344627139083535 | 5 |


## Record 16 — M04: Dear032

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 8c294cbcf398c620a70622ee479a84a3a5e5ee01be68fb1d26be5bc4eaff1f10 |
| started_utc | 2026-09-10T06:20:51.771261+00:00 |
| completed_utc | 2026-09-10T06:21:00.915798+00:00 |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear032 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| size_bytes | 193460076 |
| sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| start_s | 1461.33333333333 |
| end_s | 1787.13333333333 |
| duration_s | 325.8 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 43840 to 53614 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-032, frames/M04_frame_header_04.jpg, frames/M04_frame_header_05.jpg, adv_dear_hmsz_032.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear032 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 43840 to 53614 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-032, frames/M04_frame_header_04.jpg, frames/M04_frame_header_05.jpg, adv_dear_hmsz_032.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 1461.33333333333 |
| parameters.end_s | 1787.13333333333 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 62185984 |
| streams[0].duration | 4048.566667 |
| streams[0].bit_rate | 243484 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 121457 |
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
| streams[1].duration_ts | 178544640 |
| streams[1].duration | 4048.631293 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 174360 |
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
| streams[2].duration_ts | 364376816 |
| streams[2].duration | 4048.631289 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 4048.631293 |
| format.size | 193460076 |
| format.bit_rate | 382272 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20260516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=Loj480JIDkI |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 7183890 |
| analyzed_audio_duration_s | 325.8 |
| stft_frames | 14028 |
| flux_transitions | 14027 |
| rms_linear | 0.100965685644285 |
| rms_p10_linear | 0.0158930268709503 |
| rms_p90_linear | 0.179040556254444 |
| rms_p90_p10_db | 21.0348960161797 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 391 |
| centroid_hz_mean | 1857.40779734679 |
| flatness_mean | 0.049943492185392 |
| positive_normalized_flux_mean | 0.0324973120812677 |
| flux_cv | 0.672635805782756 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -19.1 |
| lra_lu | 4.8 |
| true_peak_dbfs | -4.4 |
| silence_seconds | 12.8642170000001 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -19.1 LUFS<br>    Threshold: -29.9 LUFS<br><br>  Loudness range:<br>    LRA:         4.8 LU<br>    Threshold: -40.0 LUFS<br>    LRA low:   -22.7 LUFS<br>    LRA high:  -17.9 LUFS<br><br>  True peak:<br>    Peak:       -4.4 dBFS<br>[out#0/null @ 000001b42cb4bb00] video:0KiB audio:56124KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:05:25.80 bitrate=N/A speed= 139x elapsed=0:00:02.33 |
| ffmpeg_stderr_sha256 | ac63809af2c5217cd564c4e48e95a30c4e8bf231ade3aad08e334e8cf0bea7e9 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 93.82059 | 95.239501 | 1.41891100000001 | 1.418912 |
| 96.235057 | 97.130408 | 0.895351000000005 | 0.895351 |
| 98.325283 | 99.165283 | 0.840000000000003 | 0.84 |
| 100.182585 | 101.660544 | 1.477959 | 1.477959 |
| 102.164921 | 103.156009 | 0.991087999999991 | 0.991088 |
| 104.241927 | 105.027574 | 0.785646999999997 | 0.785646 |
| 231.329751 | 232.134195 | 0.804444000000018 | 0.804444 |
| 233.340884 | 235.179456 | 1.838572 | 1.838571 |
| 236.511247 | 238.259116 | 1.74786900000001 | 1.747868 |
| 240.367778 | 241.20966 | 0.841882000000027 | 0.841882 |
| 241.364422 | 242.586916 | 1.22249400000001 | 1.222494 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 66 |
| samples | 66 |
| brightness_mean | 0.440390672647592 |
| saturation_mean | 0.42252054862349 |
| frame_difference_mean | 0.0397805348468515 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 1461.33333333333 | 1461.33333333333 | 0.441018283367157 | 0.421860838779956 | N/A | N/A | N/A |
| 1466.33333333333 | 1466.33333333333 | 0.440535128116608 | 0.419212145969499 | 0.0245136171579361 | 0.0567838790703561 | 5 |
| 1471.33333333333 | 1471.33333333333 | 0.443034291267395 | 0.418095860566449 | 0.0241560451686382 | 0.0415999331402707 | 5 |
| 1476.33333333333 | 1476.33333333333 | 0.440651178359985 | 0.422521786492375 | 0.0205776151269674 | 0.0689444921821706 | 5 |
| 1481.33333333333 | 1481.33333333333 | 0.440768003463745 | 0.421415032679739 | 0.019980663433671 | 0.0678650094346737 | 5 |
| 1486.33333333333 | 1486.33333333333 | 0.43920373916626 | 0.406182734204793 | 0.0569934658706188 | 0.177913049339638 | 5 |
| 1491.33333333333 | 1491.33333333333 | 0.442855417728424 | 0.446352668845316 | 0.0639343708753586 | 0.265340540935698 | 5 |
| 1496.33333333333 | 1496.33333333333 | 0.441243499517441 | 0.42101279956427 | 0.056451253592968 | 0.200296627757096 | 5 |
| 1501.33333333333 | 1501.33333333333 | 0.443746745586395 | 0.428714869281046 | 0.0606388859450817 | 0.22226069328465 | 5 |
| 1506.33333333333 | 1506.33333333333 | 0.442107826471329 | 0.431892701525054 | 0.0176100209355354 | 0.0587080364296958 | 5 |
| 1511.33333333333 | 1511.33333333333 | 0.444028049707413 | 0.42062091503268 | 0.0614583343267441 | 0.218249908154388 | 5 |
| 1516.33333333333 | 1516.33333333333 | 0.440242916345596 | 0.419523965141612 | 0.0203085504472256 | 0.0588288244704399 | 5 |
| 1521.33333333333 | 1521.33333333333 | 0.442958652973175 | 0.445553104575163 | 0.0538692809641361 | 0.206841553338624 | 5 |
| 1526.33333333333 | 1526.33333333333 | 0.440013915300369 | 0.447628267973856 | 0.0213815346360207 | 0.0774849644748169 | 5 |
| 1531.33333333333 | 1531.33333333333 | 0.440037578344345 | 0.40504711328976 | 0.0634866580367088 | 0.259802479245781 | 5 |
| 1536.33333333333 | 1536.33333333333 | 0.438416689634323 | 0.405506535947712 | 0.0371067561209202 | 0.0708901456572395 | 5 |
| 1541.33333333333 | 1541.33333333333 | 0.441822171211243 | 0.43018082788671 | 0.0628188997507095 | 0.233288842035687 | 5 |
| 1546.33333333333 | 1546.33333333333 | 0.446617931127548 | 0.426919662309368 | 0.0332919396460056 | 0.0861754694358726 | 5 |
| 1551.33333333333 | 1551.33333333333 | 0.443126887083054 | 0.421076797385621 | 0.0633243471384048 | 0.214110047414503 | 5 |
| 1556.33333333333 | 1556.33333333333 | 0.444399833679199 | 0.445971132897603 | 0.0557554438710213 | 0.197881746236619 | 5 |
| 1561.33333333333 | 1561.33333333333 | 0.443014174699783 | 0.420795751633987 | 0.0559640489518642 | 0.200458233539189 | 5 |
| 1566.33333333333 | 1566.33333333333 | 0.444614946842194 | 0.405680555555556 | 0.055505994707346 | 0.151329275121646 | 5 |
| 1571.33333333333 | 1571.33333333333 | 0.437334418296814 | 0.410331427015251 | 0.0337173193693161 | 0.0901229356361978 | 5 |
| 1576.33333333333 | 1576.33333333333 | 0.437969774007797 | 0.449479847494553 | 0.0596484206616879 | 0.260853019134448 | 5 |
| 1581.33333333333 | 1581.33333333333 | 0.435619562864304 | 0.450358932461874 | 0.0191094782203436 | 0.0475102706987207 | 5 |
| 1586.33333333333 | 1586.33333333333 | 0.435464084148407 | 0.450360566448802 | 0.00699537061154842 | 0.0439591534050805 | 5 |
| 1591.33333333333 | 1591.33333333333 | 0.442358672618866 | 0.421473311546841 | 0.0563238002359867 | 0.202029019565215 | 5 |
| 1596.33333333333 | 1596.33333333333 | 0.440709710121155 | 0.419881808278867 | 0.0225089862942696 | 0.0587504012856379 | 5 |
| 1601.33333333333 | 1601.33333333333 | 0.444363564252853 | 0.445050381263617 | 0.0561048462986946 | 0.203168195500661 | 5 |
| 1606.33333333333 | 1606.33333333333 | 0.446166425943375 | 0.405441993464052 | 0.0664221122860909 | 0.245546820254735 | 5 |
| 1611.33333333333 | 1611.33333333333 | 0.441705077886581 | 0.420161492374728 | 0.0588899776339531 | 0.156567831126219 | 5 |
| 1616.33333333333 | 1616.33333333333 | 0.441013932228088 | 0.420298474945534 | 0.00723365973681211 | 0.0482247872956186 | 5 |
| 1621.33333333333 | 1621.33333333333 | 0.439967304468155 | 0.421863017429194 | 0.0204479862004519 | 0.0635459681755273 | 5 |
| 1626.33333333333 | 1626.33333333333 | 0.438595592975616 | 0.42106862745098 | 0.0178673751652241 | 0.0607974309426494 | 5 |
| 1631.33333333333 | 1631.33333333333 | 0.441789478063583 | 0.420867647058824 | 0.0136138340458274 | 0.044478627464657 | 5 |
| 1636.33333333333 | 1636.33333333333 | 0.441252738237381 | 0.407580610021786 | 0.0563325174152851 | 0.154966890147675 | 5 |
| 1641.33333333333 | 1641.33333333333 | 0.441814571619034 | 0.428802015250545 | 0.0612731501460075 | 0.219186483994523 | 5 |
| 1646.33333333333 | 1646.33333333333 | 0.441318094730377 | 0.419445806100218 | 0.0608908012509346 | 0.224665888449281 | 5 |
| 1651.33333333333 | 1651.33333333333 | 0.437766075134277 | 0.449788671023965 | 0.0539665035903454 | 0.218392204838723 | 5 |
| 1656.33333333333 | 1656.33333333333 | 0.442439258098602 | 0.420385893246187 | 0.05341612175107 | 0.206258087980615 | 5 |
| 1661.33333333333 | 1661.33333333333 | 0.441419124603271 | 0.422095588235294 | 0.0194253791123629 | 0.0710429254695778 | 5 |
| 1666.33333333333 | 1666.33333333333 | 0.441795498132706 | 0.403560729847495 | 0.0612777806818485 | 0.171195938407839 | 5 |
| 1671.33333333333 | 1671.33333333333 | 0.44191586971283 | 0.404148148148148 | 0.0126922661438584 | 0.0472004646602748 | 5 |
| 1676.33333333333 | 1676.33333333333 | 0.437958896160126 | 0.403066721132898 | 0.0277489107102156 | 0.0609681865710278 | 5 |
| 1681.33333333333 | 1681.33333333333 | 0.442053109407425 | 0.427264705882353 | 0.0591737441718578 | 0.219698094373184 | 5 |
| 1686.33333333333 | 1686.33333333333 | 0.44276362657547 | 0.420096405228758 | 0.0656767413020134 | 0.222240782455607 | 5 |
| 1691.33333333333 | 1691.33333333333 | 0.442184120416641 | 0.421279684095861 | 0.0311476048082113 | 0.0579169915038999 | 5 |
| 1696.33333333333 | 1696.33333333333 | 0.440599173307419 | 0.421278867102397 | 0.0205108933150768 | 0.0708454223186562 | 5 |
| 1701.33333333333 | 1701.33333333333 | 0.438329547643661 | 0.422459150326797 | 0.0270844232290983 | 0.0807557630457493 | 5 |
| 1706.33333333333 | 1706.33333333333 | 0.441768795251846 | 0.42050462962963 | 0.0273641068488359 | 0.0733406500813958 | 5 |
| 1711.33333333333 | 1711.33333333333 | 0.43947035074234 | 0.422705337690632 | 0.0217102393507957 | 0.068213033122675 | 5 |
| 1716.33333333333 | 1716.33333333333 | 0.44112554192543 | 0.421289215686274 | 0.0152412857860327 | 0.062842886551211 | 5 |
| 1721.33333333333 | 1721.33333333333 | 0.44207352399826 | 0.421100217864924 | 0.0171478763222694 | 0.0623565016848607 | 5 |
| 1726.33333333333 | 1726.33333333333 | 0.43943464756012 | 0.419731481481481 | 0.0183660127222538 | 0.0741668657808143 | 5 |
| 1731.33333333333 | 1731.33333333333 | 0.438594222068787 | 0.4044651416122 | 0.0542930252850056 | 0.162142595185489 | 5 |
| 1736.33333333333 | 1736.33333333333 | 0.442065894603729 | 0.420603213507625 | 0.0565544627606869 | 0.167426525806477 | 5 |
| 1741.33333333333 | 1741.33333333333 | 0.442216247320175 | 0.421109477124183 | 0.00432570837438107 | 0.0299618805519057 | 5 |
| 1746.33333333333 | 1746.33333333333 | 0.439004123210907 | 0.407150871459695 | 0.0590955913066864 | 0.166400548661823 | 5 |
| 1751.33333333333 | 1751.33333333333 | 0.445133745670319 | 0.445824891067538 | 0.0637875869870186 | 0.258743513354135 | 5 |
| 1756.33333333333 | 1756.33333333333 | 0.437362194061279 | 0.449440631808279 | 0.0226326249539852 | 0.0653125000666331 | 5 |
| 1761.33333333333 | 1761.33333333333 | 0.443343430757523 | 0.421586328976035 | 0.0529768541455269 | 0.204591630915161 | 5 |
| 1766.33333333333 | 1766.33333333333 | 0.441354304552078 | 0.421755991285403 | 0.0153022892773151 | 0.0578846039352219 | 5 |
| 1771.33333333333 | 1771.33333333333 | 0.441480398178101 | 0.418476579520697 | 0.0228771790862083 | 0.0739485094412563 | 5 |
| 1776.33333333333 | 1776.33333333333 | 0.442147076129913 | 0.420755991285403 | 0.0241062082350254 | 0.0567756076176969 | 5 |
| 1781.33333333333 | 1781.33333333333 | 0.439513623714447 | 0.405718954248366 | 0.0578567534685135 | 0.159853647636599 | 5 |
| 1786.33333333333 | 1786.33333333333 | 0.388571113348007 | 0.384480664488017 | 0.0734692290425301 | 0.333119856344308 | 5 |


## Record 17 — M04: Dear033

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 61d4c9463058c008c32261af0f1f20a6635bb90cc04977e78b56febe09f8362f |
| started_utc | 2026-09-10T06:21:01.508677+00:00 |
| completed_utc | 2026-09-10T06:21:10.965666+00:00 |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear033 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| size_bytes | 193460076 |
| sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| start_s | 1787.13333333333 |
| end_s | 2162.33333333333 |
| duration_s | 375.2 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 53614 to 64870 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-033, frames/M04_frame_header_05.jpg, frames/M04_frame_header_06.jpg, adv_dear_hmsz_033.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear033 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 53614 to 64870 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-033, frames/M04_frame_header_05.jpg, frames/M04_frame_header_06.jpg, adv_dear_hmsz_033.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 1787.13333333333 |
| parameters.end_s | 2162.33333333333 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 62185984 |
| streams[0].duration | 4048.566667 |
| streams[0].bit_rate | 243484 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 121457 |
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
| streams[1].duration_ts | 178544640 |
| streams[1].duration | 4048.631293 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 174360 |
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
| streams[2].duration_ts | 364376816 |
| streams[2].duration | 4048.631289 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 4048.631293 |
| format.size | 193460076 |
| format.bit_rate | 382272 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20260516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=Loj480JIDkI |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 8273160 |
| analyzed_audio_duration_s | 375.2 |
| stft_frames | 16155 |
| flux_transitions | 16154 |
| rms_linear | 0.100229792184288 |
| rms_p10_linear | 0.0204298079209641 |
| rms_p90_linear | 0.175230976075074 |
| rms_p90_p10_db | 18.6669319324808 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 226 |
| centroid_hz_mean | 2066.23685566664 |
| flatness_mean | 0.0339545990256067 |
| positive_normalized_flux_mean | 0.0343029529203372 |
| flux_cv | 0.611169835510325 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -19.7 |
| lra_lu | 4.8 |
| true_peak_dbfs | -4.3 |
| silence_seconds | 7.09308300000001 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -19.7 LUFS<br>    Threshold: -30.3 LUFS<br><br>  Loudness range:<br>    LRA:         4.8 LU<br>    Threshold: -40.4 LUFS<br>    LRA low:   -22.9 LUFS<br>    LRA high:  -18.1 LUFS<br><br>  True peak:<br>    Peak:       -4.3 dBFS<br>[out#0/null @ 000002a9a5ef0880] video:0KiB audio:64634KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:06:15.20 bitrate=N/A speed= 135x elapsed=0:00:02.78 |
| ffmpeg_stderr_sha256 | 522360cf63ceb5de23ad9fd95c1a88690d6207be36f309f887bd3e83f1bec22e |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 61.945624 | 62.836372 | 0.890747999999995 | 0.890748 |
| 63.299048 | 63.954354 | 0.655306000000003 | 0.655306 |
| 149.493379 | 150.9861 | 1.49272099999999 | 1.492721 |
| 153.122766 | 154.369274 | 1.24650799999998 | 1.246508 |
| 314.358776 | 315.295215 | 0.936439000000007 | 0.93644 |
| 316.677959 | 317.62542 | 0.947461000000033 | 0.94746 |
| 319.453878 | 320.377778 | 0.923900000000003 | 0.9239 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 76 |
| samples | 76 |
| brightness_mean | 0.485515789766061 |
| saturation_mean | 0.348471036148377 |
| frame_difference_mean | 0.0385613865312189 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 1787.13333333333 | 1787.13333333333 | 0.485001891851425 | 0.348312363834423 | N/A | N/A | N/A |
| 1792.13333333333 | 1792.13333333333 | 0.493292778730392 | 0.344470315904139 | 0.0292440075427294 | 0.0499016571049005 | 5 |
| 1797.13333333333 | 1797.13333333333 | 0.491712182760239 | 0.347650054466231 | 0.038954246789217 | 0.0746648864285719 | 5 |
| 1802.13333333333 | 1802.13333333333 | 0.491818368434906 | 0.345082788671024 | 0.0184989105910063 | 0.0560319231388303 | 5 |
| 1807.13333333333 | 1807.13333333333 | 0.48931673169136 | 0.348402233115468 | 0.0768981426954269 | 0.135625768727688 | 5 |
| 1812.13333333333 | 1812.13333333333 | 0.482327073812485 | 0.352671840958606 | 0.017095860093832 | 0.0796787469004223 | 5 |
| 1817.13333333333 | 1817.13333333333 | 0.48314243555069 | 0.351355119825708 | 0.0158366020768881 | 0.0442856836258061 | 5 |
| 1822.13333333333 | 1822.13333333333 | 0.483284592628479 | 0.351645969498911 | 0.00992320291697979 | 0.0195747909848514 | 5 |
| 1827.13333333333 | 1827.13333333333 | 0.402097225189209 | 0.365191993464052 | 0.135485291481018 | 0.351384175268895 | 5 |
| 1832.13333333333 | 1832.13333333333 | 0.407062113285065 | 0.365248638344227 | 0.0241135619580746 | 0.0569323811389418 | 5 |
| 1837.13333333333 | 1837.13333333333 | 0.4906405210495 | 0.348825980392157 | 0.138459697365761 | 0.344613696396339 | 5 |
| 1842.13333333333 | 1842.13333333333 | 0.488230377435684 | 0.34827559912854 | 0.0312587134540081 | 0.0682870866640484 | 5 |
| 1847.13333333333 | 1847.13333333333 | 0.48657301068306 | 0.347684095860566 | 0.0793562158942223 | 0.142206383298941 | 5 |
| 1852.13333333333 | 1852.13333333333 | 0.491409569978714 | 0.346278050108932 | 0.0781688466668129 | 0.142228795491026 | 5 |
| 1857.13333333333 | 1857.13333333333 | 0.482238560914993 | 0.352123910675381 | 0.0209863837808371 | 0.0658725974174858 | 5 |
| 1862.13333333333 | 1862.13333333333 | 0.489464312791824 | 0.346110838779956 | 0.0188548471778631 | 0.0680289012901806 | 5 |
| 1867.13333333333 | 1867.13333333333 | 0.488818645477295 | 0.345982843137255 | 0.00753839872777462 | 0.0375273251592318 | 5 |
| 1872.13333333333 | 1872.13333333333 | 0.489474684000015 | 0.346033496732026 | 0.0170155223459005 | 0.048701856282427 | 5 |
| 1877.13333333333 | 1877.13333333333 | 0.490041106939316 | 0.346209150326797 | 0.00617211358621716 | 0.0423403214092525 | 5 |
| 1882.13333333333 | 1882.13333333333 | 0.482640564441681 | 0.350785130718954 | 0.0241620372980833 | 0.0983301551661277 | 5 |
| 1887.13333333333 | 1887.13333333333 | 0.483606487512589 | 0.3525348583878 | 0.00980528257787228 | 0.0320158060204579 | 5 |
| 1892.13333333333 | 1892.13333333333 | 0.481214880943298 | 0.351145152505447 | 0.0178627464920282 | 0.0581926541261956 | 5 |
| 1897.13333333333 | 1897.13333333333 | 0.493344217538834 | 0.343667483660131 | 0.0752687901258469 | 0.150970572713784 | 5 |
| 1902.13333333333 | 1902.13333333333 | 0.485912889242172 | 0.346610838779956 | 0.0256263613700867 | 0.0586840890467221 | 5 |
| 1907.13333333333 | 1907.13333333333 | 0.491066724061966 | 0.34770697167756 | 0.0804980918765068 | 0.139613565196965 | 5 |
| 1912.13333333333 | 1912.13333333333 | 0.490745365619659 | 0.346153050108932 | 0.0230435710400343 | 0.0518889122865621 | 5 |
| 1917.13333333333 | 1917.13333333333 | 0.489616304636002 | 0.348725490196078 | 0.0789237469434738 | 0.137260497172613 | 5 |
| 1922.13333333333 | 1922.13333333333 | 0.489382386207581 | 0.345854030501089 | 0.0237584430724382 | 0.0570771721401783 | 5 |
| 1927.13333333333 | 1927.13333333333 | 0.483082503080368 | 0.351570533769063 | 0.0732889473438263 | 0.149439673480859 | 5 |
| 1932.13333333333 | 1932.13333333333 | 0.488803654909134 | 0.347650054466231 | 0.0214319173246622 | 0.0815498399286226 | 5 |
| 1937.13333333333 | 1937.13333333333 | 0.486848056316376 | 0.34606862745098 | 0.0113646509125829 | 0.0526456167111214 | 5 |
| 1942.13333333333 | 1942.13333333333 | 0.503165602684021 | 0.341813997821351 | 0.0794177576899529 | 0.136813770266743 | 5 |
| 1947.13333333333 | 1947.13333333333 | 0.493910700082779 | 0.343940359477124 | 0.0280130710452795 | 0.0490039283559998 | 5 |
| 1952.13333333333 | 1952.13333333333 | 0.49128133058548 | 0.346044389978214 | 0.0771636739373207 | 0.118918195572288 | 5 |
| 1957.13333333333 | 1957.13333333333 | 0.487006574869156 | 0.351506535947712 | 0.0274163950234652 | 0.0886391309529596 | 5 |
| 1962.13333333333 | 1962.13333333333 | 0.486397922039032 | 0.351140522875817 | 0.00618436792865396 | 0.0435000610761132 | 5 |
| 1967.13333333333 | 1967.13333333333 | 0.490995407104492 | 0.348636437908497 | 0.0231525041162968 | 0.0589381167508385 | 5 |
| 1972.13333333333 | 1972.13333333333 | 0.485364645719528 | 0.351654684095861 | 0.0206154678016901 | 0.0568205034251294 | 5 |
| 1977.13333333333 | 1977.13333333333 | 0.489370375871658 | 0.347741830065359 | 0.0749000534415245 | 0.133870812885621 | 5 |
| 1982.13333333333 | 1982.13333333333 | 0.488343983888626 | 0.348550925925926 | 0.0197486374527216 | 0.0210317740003595 | 5 |
| 1987.13333333333 | 1987.13333333333 | 0.485940337181091 | 0.347442538126362 | 0.0254400875419378 | 0.0500381283903784 | 5 |
| 1992.13333333333 | 1992.13333333333 | 0.489125311374664 | 0.346453431372549 | 0.0790432989597321 | 0.146323631854418 | 5 |
| 1997.13333333333 | 1997.13333333333 | 0.485171586275101 | 0.351432461873638 | 0.0188785381615162 | 0.0820051139902781 | 5 |
| 2002.13333333333 | 2002.13333333333 | 0.490833610296249 | 0.348781590413943 | 0.0270607303828001 | 0.0536918382123229 | 5 |
| 2007.13333333333 | 2007.13333333333 | 0.490927010774612 | 0.348985294117647 | 0.00272412854246795 | 0.012953634787887 | 5 |
| 2012.13333333333 | 2012.13333333333 | 0.488003820180893 | 0.347732298474946 | 0.0740653574466705 | 0.134712324729314 | 5 |
| 2017.13333333333 | 2017.13333333333 | 0.490759015083313 | 0.344953976034858 | 0.021745914593339 | 0.0676651657052394 | 5 |
| 2022.13333333333 | 2022.13333333333 | 0.488881796598434 | 0.346274782135076 | 0.00995343085378408 | 0.0378544952396285 | 5 |
| 2027.13333333333 | 2027.13333333333 | 0.486342310905457 | 0.348197440087146 | 0.0761249959468842 | 0.143086093092045 | 5 |
| 2032.13333333333 | 2032.13333333333 | 0.490659594535828 | 0.34793137254902 | 0.0271620340645313 | 0.0704610080396793 | 5 |
| 2037.13333333333 | 2037.13333333333 | 0.485003858804703 | 0.351751906318083 | 0.0221209153532982 | 0.082082576858779 | 5 |
| 2042.13333333333 | 2042.13333333333 | 0.489011973142624 | 0.348215413943355 | 0.0245059933513403 | 0.0842896411314392 | 5 |
| 2047.13333333333 | 2047.13333333333 | 0.483098328113556 | 0.351789215686275 | 0.0209436267614365 | 0.0766328588079313 | 5 |
| 2052.13333333333 | 2052.13333333333 | 0.489940106868744 | 0.349087690631808 | 0.0262464582920074 | 0.057291700767553 | 4.99999999999977 |
| 2057.13333333333 | 2057.13333333333 | 0.48634397983551 | 0.349876361655773 | 0.0176462419331074 | 0.0431322839138463 | 5 |
| 2062.13333333333 | 2062.13333333333 | 0.487295180559158 | 0.349109204793028 | 0.0750204250216484 | 0.136955396712286 | 5 |
| 2067.13333333333 | 2067.13333333333 | 0.484982579946518 | 0.349446623093682 | 0.0129809360951185 | 0.0490015473228354 | 5 |
| 2072.13333333333 | 2072.13333333333 | 0.488273411989212 | 0.348078703703704 | 0.0248823519796133 | 0.0431025106665679 | 5 |
| 2077.13333333333 | 2077.13333333333 | 0.487382352352142 | 0.347875816993464 | 0.00761546846479177 | 0.0409892864032865 | 5 |
| 2082.13333333333 | 2082.13333333333 | 0.42206072807312 | 0.33205637254902 | 0.0886582285165787 | 0.272545221052833 | 5 |
| 2087.13333333333 | 2087.13333333333 | 0.489993751049042 | 0.346846405228758 | 0.107077337801456 | 0.249311572147815 | 5 |
| 2092.13333333333 | 2092.13333333333 | 0.49071678519249 | 0.347880446623094 | 0.0257557164877653 | 0.0661714092897959 | 5 |
| 2097.13333333333 | 2097.13333333333 | 0.490380465984344 | 0.347882080610022 | 0.00706127425655723 | 0.0453636563579969 | 5 |
| 2102.13333333333 | 2102.13333333333 | 0.487065374851227 | 0.350429193899782 | 0.0209011435508728 | 0.0424813360106601 | 5 |
| 2107.13333333333 | 2107.13333333333 | 0.487438172101974 | 0.350324891067538 | 0.00594362802803516 | 0.0439536631463831 | 5 |
| 2112.13333333333 | 2112.13333333333 | 0.490864396095276 | 0.346022875816993 | 0.0725912302732468 | 0.134357170005593 | 5 |
| 2117.13333333333 | 2117.13333333333 | 0.49090576171875 | 0.347819989106754 | 0.0793164372444153 | 0.137683506718129 | 5 |
| 2122.13333333333 | 2122.13333333333 | 0.482107877731323 | 0.352434912854031 | 0.0229673199355602 | 0.0717980749878434 | 5 |
| 2127.13333333333 | 2127.13333333333 | 0.485383152961731 | 0.351549291938998 | 0.0223750006407499 | 0.0487643836358042 | 5 |
| 2132.13333333333 | 2132.13333333333 | 0.490232855081558 | 0.348703976034858 | 0.0237129628658295 | 0.0593733775669495 | 5 |
| 2137.13333333333 | 2137.13333333333 | 0.489313989877701 | 0.348324891067538 | 0.0071835508570075 | 0.0406857414947741 | 5 |
| 2142.13333333333 | 2142.13333333333 | 0.49078157544136 | 0.348779956427015 | 0.0777007043361664 | 0.122597467149247 | 5 |
| 2147.13333333333 | 2147.13333333333 | 0.492339342832565 | 0.348491013071895 | 0.0102347489446402 | 0.0386734336457921 | 5 |
| 2152.13333333333 | 2152.13333333333 | 0.495401680469513 | 0.343912037037037 | 0.0431266315281391 | 0.0850533960344742 | 5 |
| 2157.13333333333 | 2157.13333333333 | 0.494459986686707 | 0.344869008714597 | 0.00947440043091774 | 0.0240502655323884 | 5 |
| 2162.13333333333 | 2162.13333333333 | 0.493731200695038 | 0.346998093681917 | 0.0883556604385376 | 0.226264754426412 | 5 |


## Record 18 — M04: Dear034

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | c8899cdcd50b359959465131717dc6a5a7c013aedeff28bd9bd5b87168bd48a9 |
| started_utc | 2026-09-10T06:21:01.794034+00:00 |
| completed_utc | 2026-09-10T06:21:11.574191+00:00 |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear034 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| size_bytes | 193460076 |
| sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| start_s | 2162.33333333333 |
| end_s | 2525.9 |
| duration_s | 363.566666666667 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 64870 to 75777 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-034, frames/M04_frame_header_06.jpg, frames/M04_frame_header_07.jpg, adv_dear_hmsz_034.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear034 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 64870 to 75777 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-034, frames/M04_frame_header_06.jpg, frames/M04_frame_header_07.jpg, adv_dear_hmsz_034.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 2162.33333333333 |
| parameters.end_s | 2525.9 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 62185984 |
| streams[0].duration | 4048.566667 |
| streams[0].bit_rate | 243484 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 121457 |
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
| streams[1].duration_ts | 178544640 |
| streams[1].duration | 4048.631293 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 174360 |
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
| streams[2].duration_ts | 364376816 |
| streams[2].duration | 4048.631289 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 4048.631293 |
| format.size | 193460076 |
| format.bit_rate | 382272 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20260516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=Loj480JIDkI |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 8016645 |
| analyzed_audio_duration_s | 363.566666666667 |
| stft_frames | 15654 |
| flux_transitions | 15653 |
| rms_linear | 0.0993673332120263 |
| rms_p10_linear | 0.0188850751423073 |
| rms_p90_linear | 0.177984370331699 |
| rms_p90_p10_db | 19.4852629858442 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 367 |
| centroid_hz_mean | 2081.10935117826 |
| flatness_mean | 0.0467324697651562 |
| positive_normalized_flux_mean | 0.0337085945766694 |
| flux_cv | 0.616082730204905 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -19.6 |
| lra_lu | 6.6 |
| true_peak_dbfs | -4.9 |
| silence_seconds | 11.01458 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -19.6 LUFS<br>    Threshold: -30.3 LUFS<br><br>  Loudness range:<br>    LRA:         6.6 LU<br>    Threshold: -40.4 LUFS<br>    LRA low:   -24.4 LUFS<br>    LRA high:  -17.8 LUFS<br><br>  True peak:<br>    Peak:       -4.9 dBFS<br>[out#0/null @ 0000020fdd609e40] video:0KiB audio:62630KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:06:03.56 bitrate=N/A speed= 106x elapsed=0:00:03.41 |
| ffmpeg_stderr_sha256 | 8393dd7797b6afc055252727afdc9ce9ec089b8882b603aa2f1a50264dea1600 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 58.466213 | 59.277846 | 0.811632999999993 | 0.811633 |
| 103.626304 | 104.36161 | 0.735305999999994 | 0.735306 |
| 106.763265 | 107.75483 | 0.991564999999994 | 0.991565 |
| 109.939569 | 113.2839 | 3.344331 | 3.344331 |
| 228.100159 | 229.534308 | 1.43414900000002 | 1.43415 |
| 231.138118 | 231.747755 | 0.609637000000021 | 0.609637 |
| 233.133764 | 233.98449 | 0.85072599999998 | 0.850726 |
| 234.636712 | 236.02449 | 1.387778 | 1.387778 |
| 236.628005 | 237.47746 | 0.849455000000006 | 0.849456 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 73 |
| samples | 73 |
| brightness_mean | 0.495182219433458 |
| saturation_mean | 0.353094737666756 |
| frame_difference_mean | 0.0581617261858709 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 2162.33333333333 | 2162.33333333333 | 0.503968954086304 | 0.340977396514161 | N/A | N/A | N/A |
| 2167.33333333333 | 2167.33333333333 | 0.509044945240021 | 0.339712690631808 | 0.0447077862918377 | 0.0865430533432877 | 5 |
| 2172.33333333333 | 2172.33333333333 | 0.524786531925201 | 0.333055010893246 | 0.0871544033288956 | 0.183736049231705 | 5 |
| 2177.33333333333 | 2177.33333333333 | 0.519995927810669 | 0.336872821350763 | 0.0774430856108665 | 0.106091907555591 | 5 |
| 2182.33333333333 | 2182.33333333333 | 0.528005719184875 | 0.332520969498911 | 0.0247668847441673 | 0.055146997058588 | 5 |
| 2187.33333333333 | 2187.33333333333 | 0.528250575065613 | 0.332373638344227 | 0.00635484699159861 | 0.0433110071135635 | 5 |
| 2192.33333333333 | 2192.33333333333 | 0.503573834896088 | 0.344062091503268 | 0.0781135559082031 | 0.15572950435432 | 5 |
| 2197.33333333333 | 2197.33333333333 | 0.51498281955719 | 0.341087690631808 | 0.0200659055262804 | 0.055595088244116 | 5 |
| 2202.33333333333 | 2202.33333333333 | 0.518182992935181 | 0.338688997821351 | 0.0770797878503799 | 0.155837716768299 | 5 |
| 2207.33333333333 | 2207.33333333333 | 0.521076500415802 | 0.335535130718954 | 0.0770558267831802 | 0.113625578610866 | 5 |
| 2212.33333333333 | 2212.33333333333 | 0.525822222232819 | 0.331146241830065 | 0.0385228767991066 | 0.0679491206630591 | 5 |
| 2217.33333333333 | 2217.33333333333 | 0.521315634250641 | 0.335149237472767 | 0.0302184075117111 | 0.0665224797893485 | 5 |
| 2222.33333333333 | 2222.33333333333 | 0.446907132863998 | 0.407215413943355 | 0.113068073987961 | 0.374117233428184 | 5 |
| 2227.33333333333 | 2227.33333333333 | 0.516864955425262 | 0.345122821350762 | 0.111369013786316 | 0.257929896003827 | 5 |
| 2232.33333333333 | 2232.33333333333 | 0.481333345174789 | 0.363099128540305 | 0.0967325642704964 | 0.29440518324367 | 5 |
| 2237.33333333333 | 2237.33333333333 | 0.449058294296265 | 0.359393518518519 | 0.0806094780564308 | 0.269802896856481 | 5 |
| 2242.33333333333 | 2242.33333333333 | 0.45810866355896 | 0.371730392156863 | 0.0874550640583038 | 0.21403247008436 | 5 |
| 2247.33333333333 | 2247.33333333333 | 0.50951361656189 | 0.351585511982571 | 0.114830881357193 | 0.260013643980267 | 5 |
| 2252.33333333333 | 2252.33333333333 | 0.492767155170441 | 0.366761165577342 | 0.0918134450912476 | 0.206377936602822 | 5 |
| 2257.33333333333 | 2257.33333333333 | 0.490287333726883 | 0.365854030501089 | 0.029562633484602 | 0.0707717299354265 | 5 |
| 2262.33333333333 | 2262.33333333333 | 0.488712698221207 | 0.366062091503268 | 0.0360800623893738 | 0.0608174485790739 | 5 |
| 2267.33333333333 | 2267.33333333333 | 0.505855679512024 | 0.354922930283224 | 0.0885569229722023 | 0.170731481861475 | 5 |
| 2272.33333333333 | 2272.33333333333 | 0.503236711025238 | 0.354333061002179 | 0.0242562629282475 | 0.0487201906834888 | 5 |
| 2277.33333333333 | 2277.33333333333 | 0.505288422107697 | 0.352866013071895 | 0.080097496509552 | 0.163956623290506 | 5 |
| 2282.33333333333 | 2282.33333333333 | 0.484778076410294 | 0.353084694989107 | 0.0837946608662605 | 0.215806647456846 | 5 |
| 2287.33333333333 | 2287.33333333333 | 0.501243770122528 | 0.344240468409586 | 0.074068084359169 | 0.18346846966318 | 5 |
| 2292.33333333333 | 2292.33333333333 | 0.50728839635849 | 0.351101034858388 | 0.0730315819382668 | 0.132246642428997 | 5 |
| 2297.33333333333 | 2297.33333333333 | 0.483048498630524 | 0.353960511982571 | 0.0742344781756401 | 0.18839383428296 | 5 |
| 2302.33333333333 | 2302.33333333333 | 0.475738286972046 | 0.35955582788671 | 0.0808450430631638 | 0.112044497535856 | 5 |
| 2307.33333333333 | 2307.33333333333 | 0.50287252664566 | 0.359212418300654 | 0.0926565900444984 | 0.21185526466482 | 5 |
| 2312.33333333333 | 2312.33333333333 | 0.504980683326721 | 0.356584694989107 | 0.0198804475367069 | 0.0604359920587588 | 5 |
| 2317.33333333333 | 2317.33333333333 | 0.480196088552475 | 0.356529411764706 | 0.0812676995992661 | 0.183955475852721 | 5 |
| 2322.33333333333 | 2322.33333333333 | 0.494552850723267 | 0.365724945533769 | 0.0852592661976814 | 0.176639871951757 | 5 |
| 2327.33333333333 | 2327.33333333333 | 0.490381002426147 | 0.366722222222222 | 0.0254768524318933 | 0.0561585182191087 | 5 |
| 2332.33333333333 | 2332.33333333333 | 0.495348572731018 | 0.365989651416122 | 0.0251609459519386 | 0.0648767418713516 | 5 |
| 2337.33333333333 | 2337.33333333333 | 0.501265823841095 | 0.354601851851852 | 0.0880915001034737 | 0.207903093965051 | 5 |
| 2342.33333333333 | 2342.33333333333 | 0.485178619623184 | 0.353958333333333 | 0.0707047954201698 | 0.181454313891131 | 5 |
| 2347.33333333333 | 2347.33333333333 | 0.48221680521965 | 0.356421296296296 | 0.022726034745574 | 0.0521369706502877 | 5 |
| 2352.33333333333 | 2352.33333333333 | 0.503241837024689 | 0.352928104575163 | 0.0736029371619225 | 0.179973481099033 | 5 |
| 2357.33333333333 | 2357.33333333333 | 0.502301752567291 | 0.353255174291939 | 0.02577287517488 | 0.0545774749458582 | 5 |
| 2362.33333333333 | 2362.33333333333 | 0.485867917537689 | 0.352227941176471 | 0.0734234675765038 | 0.165770573279373 | 5 |
| 2367.33333333333 | 2367.33333333333 | 0.485988020896912 | 0.352514705882353 | 0.00302805006504059 | 0.0135128701126742 | 5 |
| 2372.33333333333 | 2372.33333333333 | 0.485085248947144 | 0.357599128540305 | 0.0791244506835938 | 0.100906528753773 | 5 |
| 2377.33333333333 | 2377.33333333333 | 0.485656887292862 | 0.355964052287582 | 0.0138613851740956 | 0.0426667411713459 | 5 |
| 2382.33333333333 | 2382.33333333333 | 0.49912828207016 | 0.347087145969499 | 0.0826750993728638 | 0.192449318352297 | 5 |
| 2387.33333333333 | 2387.33333333333 | 0.489632099866867 | 0.355218137254902 | 0.0269025042653084 | 0.0484361484919046 | 5 |
| 2392.33333333333 | 2392.33333333333 | 0.480169147253036 | 0.357066176470588 | 0.0689607858657837 | 0.193717348199838 | 5 |
| 2397.33333333333 | 2397.33333333333 | 0.504881799221039 | 0.352041938997821 | 0.0725819766521454 | 0.180985778273911 | 5 |
| 2402.33333333333 | 2402.33333333333 | 0.48620480298996 | 0.353898420479303 | 0.0741791874170303 | 0.181053884030719 | 5 |
| 2407.33333333333 | 2407.33333333333 | 0.503247022628784 | 0.354502450980392 | 0.0719474479556084 | 0.189536452852329 | 5 |
| 2412.33333333333 | 2412.33333333333 | 0.485851585865021 | 0.352388071895425 | 0.0718665570020676 | 0.180508469609803 | 5 |
| 2417.33333333333 | 2417.33333333333 | 0.482230126857758 | 0.355458333333333 | 0.0256879087537527 | 0.0605329642288258 | 5 |
| 2422.33333333333 | 2422.33333333333 | 0.481855392456055 | 0.356110566448802 | 0.0114041389897466 | 0.0491530706310673 | 5 |
| 2427.33333333333 | 2427.33333333333 | 0.500362753868103 | 0.345379357298475 | 0.077920213341713 | 0.18601275033561 | 5 |
| 2432.33333333333 | 2432.33333333333 | 0.483358114957809 | 0.355740196078431 | 0.0805868729948997 | 0.180382976425296 | 5 |
| 2437.33333333333 | 2437.33333333333 | 0.486786782741547 | 0.352297385620915 | 0.0795544609427452 | 0.100562491646252 | 5 |
| 2442.33333333333 | 2442.33333333333 | 0.48007133603096 | 0.357128267973856 | 0.0231348033994436 | 0.0769717576683323 | 5 |
| 2447.33333333333 | 2447.33333333333 | 0.508720874786377 | 0.351248093681917 | 0.0693788155913353 | 0.177712166052445 | 5 |
| 2452.33333333333 | 2452.33333333333 | 0.501378834247589 | 0.345869553376906 | 0.0763349682092667 | 0.11949937547002 | 5 |
| 2457.33333333333 | 2457.33333333333 | 0.5037881731987 | 0.351298202614379 | 0.0778592079877853 | 0.119841355782543 | 5 |
| 2462.33333333333 | 2462.33333333333 | 0.501200199127197 | 0.353629357298475 | 0.0202175937592983 | 0.0373356818340853 | 5 |
| 2467.33333333333 | 2467.33333333333 | 0.50104820728302 | 0.353891067538126 | 0.00956481508910656 | 0.046703206732387 | 5 |
| 2472.33333333333 | 2472.33333333333 | 0.501859188079834 | 0.352943899782135 | 0.0228316988795996 | 0.051175769387557 | 5 |
| 2477.33333333333 | 2477.33333333333 | 0.496049851179123 | 0.348660675381264 | 0.0679439008235931 | 0.12698447483141 | 5 |
| 2482.33333333333 | 2482.33333333333 | 0.480116307735443 | 0.35687091503268 | 0.0742156803607941 | 0.198165455586484 | 5 |
| 2487.33333333333 | 2487.33333333333 | 0.480543583631516 | 0.356987745098039 | 0.00273229856975377 | 0.0178157339886252 | 5 |
| 2492.33333333333 | 2492.33333333333 | 0.485035955905914 | 0.354646241830065 | 0.0218229852616787 | 0.0676441475897697 | 5 |
| 2497.33333333333 | 2497.33333333333 | 0.486896216869354 | 0.353199346405229 | 0.0245400331914425 | 0.0585366545593493 | 5 |
| 2502.33333333333 | 2502.33333333333 | 0.48884779214859 | 0.35440114379085 | 0.0798513144254684 | 0.0868550296789229 | 5 |
| 2507.33333333333 | 2507.33333333333 | 0.480884522199631 | 0.357532407407407 | 0.0305029936134815 | 0.0549954799025924 | 5 |
| 2512.33333333333 | 2512.33333333333 | 0.479614943265915 | 0.358299019607843 | 0.00720152538269758 | 0.0183124320828493 | 5 |
| 2517.33333333333 | 2517.33333333333 | 0.498209446668625 | 0.355821350762527 | 0.0809692293405533 | 0.196100336476671 | 5 |
| 2522.33333333333 | 2522.33333333333 | 0.486156344413757 | 0.35399591503268 | 0.0723488554358482 | 0.183198370581958 | 5 |


## Record 19 — M04: Dear035

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | ec28fc09a2a17093f1ffafbf494914132d861365cd5c4cbeade0c82463c3e592 |
| started_utc | 2026-09-10T06:21:11.592106+00:00 |
| completed_utc | 2026-09-10T06:21:18.010446+00:00 |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear035 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| size_bytes | 193460076 |
| sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| start_s | 2525.9 |
| end_s | 2748.03333333333 |
| duration_s | 222.133333333333 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 75777 to 82441 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-035, frames/M04_frame_header_07.jpg, frames/M04_frame_header_08.jpg, adv_dear_hmsz_035.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear035 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 75777 to 82441 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-035, frames/M04_frame_header_07.jpg, frames/M04_frame_header_08.jpg, adv_dear_hmsz_035.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 2525.9 |
| parameters.end_s | 2748.03333333333 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 62185984 |
| streams[0].duration | 4048.566667 |
| streams[0].bit_rate | 243484 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 121457 |
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
| streams[1].duration_ts | 178544640 |
| streams[1].duration | 4048.631293 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 174360 |
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
| streams[2].duration_ts | 364376816 |
| streams[2].duration | 4048.631289 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 4048.631293 |
| format.size | 193460076 |
| format.bit_rate | 382272 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20260516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=Loj480JIDkI |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 4898040 |
| analyzed_audio_duration_s | 222.133333333333 |
| stft_frames | 9563 |
| flux_transitions | 9562 |
| rms_linear | 0.101936169958516 |
| rms_p10_linear | 0.018739797248471 |
| rms_p90_linear | 0.17860578818472 |
| rms_p90_p10_db | 19.5826128281592 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 426 |
| centroid_hz_mean | 1998.21084623325 |
| flatness_mean | 0.0669714275309378 |
| positive_normalized_flux_mean | 0.0353351694818057 |
| flux_cv | 0.654605900899896 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -19.6 |
| lra_lu | 6 |
| true_peak_dbfs | -5.4 |
| silence_seconds | 11.657777 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -19.6 LUFS<br>    Threshold: -30.2 LUFS<br><br>  Loudness range:<br>    LRA:         6.0 LU<br>    Threshold: -40.3 LUFS<br>    LRA low:   -23.8 LUFS<br>    LRA high:  -17.8 LUFS<br><br>  True peak:<br>    Peak:       -5.4 dBFS<br>[out#0/null @ 000001fed83eadc0] video:0KiB audio:38266KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:03:42.13 bitrate=N/A speed=88.9x elapsed=0:00:02.49 |
| ffmpeg_stderr_sha256 | 1960e8d93c1fb638c05e25b7b4a546b4585670f13a5a1a1dc56277c728a86045 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 54.30449 | 55.21678 | 0.912289999999999 | 0.91229 |
| 55.413946 | 56.833492 | 1.419546 | 1.419546 |
| 58.969819 | 60.052971 | 1.083152 | 1.083152 |
| 61.139773 | 62.672608 | 1.532835 | 1.532834 |
| 63.251361 | 64.215896 | 0.964534999999998 | 0.964535 |
| 66.346032 | 67.659184 | 1.313152 | 1.313152 |
| 70.887506 | 71.537506 | 0.649999999999991 | 0.65 |
| 184.594875 | 185.968571 | 1.373696 | 1.373696 |
| 186.360431 | 188.769002 | 2.40857099999999 | 2.408571 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 45 |
| samples | 45 |
| brightness_mean | 0.381292663017909 |
| saturation_mean | 0.339513102154442 |
| frame_difference_mean | 0.0309975495276211 |
| histogram_jumps_gt_0_5 | 0 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 2525.9 | 2525.9 | 0.374829232692719 | 0.340843681917211 | N/A | N/A | N/A |
| 2530.9 | 2530.9 | 0.375322997570038 | 0.34000462962963 | 0.00986791960895061 | 0.0599007894296564 | 5 |
| 2535.9 | 2535.9 | 0.390817284584045 | 0.335137254901961 | 0.0526827313005924 | 0.102422952659129 | 5 |
| 2540.9 | 2540.9 | 0.389770448207855 | 0.342239379084967 | 0.0291721131652594 | 0.0567167444305312 | 5 |
| 2545.9 | 2545.9 | 0.376555591821671 | 0.338083061002179 | 0.0563052818179131 | 0.0999485499983314 | 5 |
| 2550.9 | 2550.9 | 0.371059894561768 | 0.341941176470588 | 0.0162663403898478 | 0.0492917190026468 | 5 |
| 2555.9 | 2555.9 | 0.371457248926163 | 0.336633986928105 | 0.00712990248575807 | 0.054124831852791 | 5 |
| 2560.9 | 2560.9 | 0.391227424144745 | 0.335203159041394 | 0.0566307231783867 | 0.131134252019145 | 5 |
| 2565.9 | 2565.9 | 0.417188495397568 | 0.365976034858388 | 0.0578799024224281 | 0.19446967413724 | 5 |
| 2570.9 | 2570.9 | 0.37487068772316 | 0.340508169934641 | 0.0783216208219528 | 0.255079998372895 | 5 |
| 2575.9 | 2575.9 | 0.3749760389328 | 0.340151416122004 | 0.00285865995101631 | 0.0155981455188358 | 5 |
| 2580.9 | 2580.9 | 0.391269862651825 | 0.336173747276688 | 0.0537540875375271 | 0.109133539770854 | 5 |
| 2585.9 | 2585.9 | 0.375010102987289 | 0.341846405228758 | 0.0544237419962883 | 0.115492619635973 | 5 |
| 2590.9 | 2590.9 | 0.375809133052826 | 0.341255174291939 | 0.0102271251380444 | 0.0507636129344963 | 5 |
| 2595.9 | 2595.9 | 0.373286247253418 | 0.343182189542484 | 0.0146318087354302 | 0.0633685942485494 | 5 |
| 2600.9 | 2600.9 | 0.372498095035553 | 0.341249455337691 | 0.020245099440217 | 0.0530639008273393 | 5 |
| 2605.9 | 2605.9 | 0.373603254556656 | 0.338421296296296 | 0.016394879668951 | 0.052958807844634 | 5 |
| 2610.9 | 2610.9 | 0.390058875083923 | 0.337497276688453 | 0.0573684647679329 | 0.124250813941999 | 5 |
| 2615.9 | 2615.9 | 0.39245069026947 | 0.333265795206972 | 0.021654412150383 | 0.0483150738205893 | 5 |
| 2620.9 | 2620.9 | 0.39434477686882 | 0.333811819172113 | 0.0214011445641518 | 0.0683081820446877 | 5 |
| 2625.9 | 2625.9 | 0.397876113653183 | 0.331942265795207 | 0.0213401410728693 | 0.0561129808647371 | 5 |
| 2630.9 | 2630.9 | 0.390218943357468 | 0.341557461873638 | 0.0201516896486282 | 0.0803095533331906 | 5 |
| 2635.9 | 2635.9 | 0.376054495573044 | 0.335990740740741 | 0.0575403086841106 | 0.0999285481387201 | 5 |
| 2640.9 | 2640.9 | 0.37522304058075 | 0.340267973856209 | 0.0149474395439029 | 0.076098168822912 | 5 |
| 2645.9 | 2645.9 | 0.374234199523926 | 0.338755991285403 | 0.0175149776041508 | 0.0784262102590916 | 5 |
| 2650.9 | 2650.9 | 0.393977433443069 | 0.337656590413943 | 0.0611887276172638 | 0.123943444541144 | 5 |
| 2655.9 | 2655.9 | 0.37391722202301 | 0.342466503267974 | 0.0587328411638737 | 0.127592031710763 | 5 |
| 2660.9 | 2660.9 | 0.376425117254257 | 0.340456154684096 | 0.016210513189435 | 0.0570555086159319 | 5 |
| 2665.9 | 2665.9 | 0.376077324151993 | 0.336373366013072 | 0.0123880729079247 | 0.0503209389750401 | 5 |
| 2670.9 | 2670.9 | 0.394607871770859 | 0.335365468409586 | 0.0570272319018841 | 0.119881532592647 | 5 |
| 2675.9 | 2675.9 | 0.390687108039856 | 0.334807461873638 | 0.0293287038803101 | 0.066919422935551 | 5 |
| 2680.9 | 2680.9 | 0.371800124645233 | 0.34136628540305 | 0.0557824112474918 | 0.123955483931251 | 5 |
| 2685.9 | 2685.9 | 0.370001941919327 | 0.340122004357298 | 0.0159191191196442 | 0.047756900942317 | 5 |
| 2690.9 | 2690.9 | 0.370395451784134 | 0.338866830065359 | 0.00723883416503668 | 0.0459749607248524 | 5 |
| 2695.9 | 2695.9 | 0.374438464641571 | 0.341255718954248 | 0.0141721135005355 | 0.0224100458888348 | 5 |
| 2700.9 | 2700.9 | 0.374609231948853 | 0.340794389978213 | 0.0109561551362276 | 0.0404225049615248 | 5 |
| 2705.9 | 2705.9 | 0.39056670665741 | 0.333912854030501 | 0.0545735321938992 | 0.110613119083512 | 5 |
| 2710.9 | 2710.9 | 0.389520198106766 | 0.3318401416122 | 0.00408687349408865 | 0.040195050863386 | 5 |
| 2715.9 | 2715.9 | 0.374591499567032 | 0.342308823529412 | 0.0539569742977619 | 0.106228947780298 | 5 |
| 2720.9 | 2720.9 | 0.373206168413162 | 0.342246732026144 | 0.0168837159872055 | 0.0552552600195414 | 5 |
| 2725.9 | 2725.9 | 0.375352948904037 | 0.341509259259259 | 0.0139305563643575 | 0.0565964641593725 | 5 |
| 2730.9 | 2730.9 | 0.375083088874817 | 0.342627178649237 | 0.0136740198358893 | 0.045661836031236 | 5 |
| 2735.9 | 2735.9 | 0.370206713676453 | 0.343555010893246 | 0.0151617657393217 | 0.0522521379055421 | 5 |
| 2740.9 | 2740.9 | 0.394145995378494 | 0.335627178649237 | 0.0570443905889988 | 0.12760543998672 | 5 |
| 2745.9 | 2745.9 | 0.388546049594879 | 0.342992102396514 | 0.0269251111894846 | 0.0348871926580015 | 5 |


## Record 20 — M04: Dear036

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 0a999ee74f41b66123d3ed37e951a3ec0608ee9c9cc10dbbed5c790b7ba5ed5f |
| started_utc | 2026-09-10T06:21:12.098157+00:00 |
| completed_utc | 2026-09-10T06:21:26.181653+00:00 |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear036 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| size_bytes | 193460076 |
| sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| start_s | 2748.03333333333 |
| end_s | 3418.16666666667 |
| duration_s | 670.133333333333 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 82441 to 102545 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-036, frames/M04_frame_header_08.jpg, frames/M04_frame_header_09.jpg, adv_dear_hmsz_036.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear036 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 82441 to 102545 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-036, frames/M04_frame_header_08.jpg, frames/M04_frame_header_09.jpg, adv_dear_hmsz_036.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 2748.03333333333 |
| parameters.end_s | 3418.16666666667 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 62185984 |
| streams[0].duration | 4048.566667 |
| streams[0].bit_rate | 243484 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 121457 |
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
| streams[1].duration_ts | 178544640 |
| streams[1].duration | 4048.631293 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 174360 |
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
| streams[2].duration_ts | 364376816 |
| streams[2].duration | 4048.631289 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 4048.631293 |
| format.size | 193460076 |
| format.bit_rate | 382272 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20260516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=Loj480JIDkI |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 14776440 |
| analyzed_audio_duration_s | 670.133333333333 |
| stft_frames | 28857 |
| flux_transitions | 28856 |
| rms_linear | 0.0941000842680403 |
| rms_p10_linear | 0.014132096824536 |
| rms_p90_linear | 0.172164297216567 |
| rms_p90_p10_db | 21.7147297961251 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 524 |
| centroid_hz_mean | 1964.48564729628 |
| flatness_mean | 0.0441554460585869 |
| positive_normalized_flux_mean | 0.0294006563472597 |
| flux_cv | 0.630314567035401 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -19.6 |
| lra_lu | 8.3 |
| true_peak_dbfs | -3.3 |
| silence_seconds | 15.108274 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -19.6 LUFS<br>    Threshold: -30.3 LUFS<br><br>  Loudness range:<br>    LRA:         8.3 LU<br>    Threshold: -40.4 LUFS<br>    LRA low:   -25.5 LUFS<br>    LRA high:  -17.2 LUFS<br><br>  True peak:<br>    Peak:       -3.3 dBFS<br>[out#0/null @ 000002c670ca93c0] video:0KiB audio:115441KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:11:10.13 bitrate=N/A speed= 117x elapsed=0:00:05.72 |
| ffmpeg_stderr_sha256 | 989909ffc6761ed99b4552cee2a77b6f1b6579716bb560a423d3a527ba367679 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 48.787279 | 49.581859 | 0.794580000000003 | 0.79458 |
| 94.417528 | 95.017846 | 0.600318000000001 | 0.600317 |
| 96.78737 | 97.823401 | 1.03603100000001 | 1.036032 |
| 206.035125 | 208.207256 | 2.17213100000001 | 2.172132 |
| 208.655488 | 210.071406 | 1.415918 | 1.415918 |
| 210.273039 | 211.677868 | 1.40482899999998 | 1.40483 |
| 211.831383 | 212.622041 | 0.790658000000008 | 0.790658 |
| 338.664694 | 339.709909 | 1.04521499999998 | 1.045215 |
| 458.115805 | 460.470726 | 2.35492099999999 | 2.354921 |
| 469.394626 | 469.959546 | 0.564919999999972 | 0.564921 |
| 472.85585 | 473.936531 | 1.08068100000003 | 1.08068 |
| 474.321134 | 475.341497 | 1.02036300000003 | 1.020363 |
| 475.546599 | 476.374308 | 0.82770899999997 | 0.82771 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 135 |
| samples | 135 |
| brightness_mean | 0.431952697921682 |
| saturation_mean | 0.387631271685629 |
| frame_difference_mean | 0.078412971455854 |
| histogram_jumps_gt_0_5 | 1 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 2748.03333333333 | 2748.03333333333 | 0.415537327528 | 0.397559912854031 | N/A | N/A | N/A |
| 2753.03333333333 | 2753.03333333333 | 0.343805581331253 | 0.459825163398693 | 0.111259527504444 | 0.364001431572337 | 5 |
| 2758.03333333333 | 2758.03333333333 | 0.340658515691757 | 0.460587690631808 | 0.0261530503630638 | 0.0637796014336128 | 5 |
| 2763.03333333333 | 2763.03333333333 | 0.412962168455124 | 0.449349945533769 | 0.0951505899429321 | 0.316334014688828 | 5 |
| 2768.03333333333 | 2768.03333333333 | 0.415491849184036 | 0.443595588235294 | 0.0327982045710087 | 0.0688160497071055 | 5 |
| 2773.03333333333 | 2773.03333333333 | 0.415726602077484 | 0.44523311546841 | 0.0160359479486942 | 0.0580673951994732 | 5 |
| 2778.03333333333 | 2778.03333333333 | 0.355439007282257 | 0.469385620915033 | 0.103908494114876 | 0.307843702199856 | 5 |
| 2783.03333333333 | 2783.03333333333 | 0.355315089225769 | 0.466842592592593 | 0.0257747825235128 | 0.0565718854329186 | 5 |
| 2788.03333333333 | 2788.03333333333 | 0.489989101886749 | 0.392167483660131 | 0.141640797257423 | 0.382560373389283 | 5 |
| 2793.03333333333 | 2793.03333333333 | 0.420805305242538 | 0.460005446623094 | 0.089508444070816 | 0.285181977251596 | 5 |
| 2798.03333333333 | 2798.03333333333 | 0.428021520376205 | 0.437636710239651 | 0.0907069742679596 | 0.242012389612209 | 5 |
| 2803.03333333333 | 2803.03333333333 | 0.530166387557983 | 0.362368464052288 | 0.105830602347851 | 0.225029567315047 | 5 |
| 2808.03333333333 | 2808.03333333333 | 0.299422949552536 | 0.586294662309368 | 0.233185186982155 | 0.437597687567749 | 5 |
| 2813.03333333333 | 2813.03333333333 | 0.396121710538864 | 0.404979847494553 | 0.0987543538212776 | 0.3505321733166 | 5 |
| 2818.03333333333 | 2818.03333333333 | 0.419141113758087 | 0.416883442265795 | 0.0668036490678787 | 0.138994715676551 | 5 |
| 2823.03333333333 | 2823.03333333333 | 0.506416380405426 | 0.367216230936819 | 0.14876988530159 | 0.334805632665276 | 5 |
| 2828.03333333333 | 2828.03333333333 | 0.453715413808823 | 0.420507897603486 | 0.109745092689991 | 0.297009624034503 | 5 |
| 2833.03333333333 | 2833.03333333333 | 0.419506013393402 | 0.419979575163399 | 0.112701795995235 | 0.288060079094259 | 5 |
| 2838.03333333333 | 2838.03333333333 | 0.485743463039398 | 0.376872276688453 | 0.11816992610693 | 0.243942766271069 | 5 |
| 2843.03333333333 | 2843.03333333333 | 0.499652773141861 | 0.357693899782135 | 0.098367378115654 | 0.245188206618698 | 5 |
| 2848.03333333333 | 2848.03333333333 | 0.543736934661865 | 0.332933551198257 | 0.0810334980487823 | 0.155800031396317 | 5 |
| 2853.03333333333 | 2853.03333333333 | 0.453022599220276 | 0.38268954248366 | 0.127361923456192 | 0.310036230211025 | 5 |
| 2858.03333333333 | 2858.03333333333 | 0.475594490766525 | 0.380753267973856 | 0.0853828936815262 | 0.194959205341099 | 5 |
| 2863.03333333333 | 2863.03333333333 | 0.487256795167923 | 0.375424564270152 | 0.0567260347306728 | 0.0744130813706631 | 5 |
| 2868.03333333333 | 2868.03333333333 | 0.483858406543732 | 0.366061546840959 | 0.0825945064425468 | 0.125540457797451 | 5 |
| 2873.03333333333 | 2873.03333333333 | 0.484108418226242 | 0.364812091503268 | 0.0523224398493767 | 0.0543008030316706 | 5 |
| 2878.03333333333 | 2878.03333333333 | 0.453008443117142 | 0.405658496732026 | 0.0852960273623466 | 0.202465887164923 | 5 |
| 2883.03333333333 | 2883.03333333333 | 0.489440649747849 | 0.365959967320261 | 0.0926097482442856 | 0.225854473640289 | 5 |
| 2888.03333333333 | 2888.03333333333 | 0.504787862300873 | 0.350360294117647 | 0.095942534506321 | 0.212009510694233 | 5 |
| 2893.03333333333 | 2893.03333333333 | 0.529577314853668 | 0.338540032679739 | 0.0552829504013062 | 0.0716605810319503 | 5 |
| 2898.03333333333 | 2898.03333333333 | 0.470113307237625 | 0.36849537037037 | 0.116163939237595 | 0.25449038394861 | 5 |
| 2903.03333333333 | 2903.03333333333 | 0.488643258810043 | 0.35995697167756 | 0.094030499458313 | 0.20026030725295 | 5 |
| 2908.03333333333 | 2908.03333333333 | 0.484301745891571 | 0.355918572984749 | 0.0661432445049286 | 0.0893459085179715 | 5 |
| 2913.03333333333 | 2913.03333333333 | 0.475670784711838 | 0.358740468409586 | 0.0487682484090328 | 0.0656577836949818 | 5 |
| 2918.03333333333 | 2918.03333333333 | 0.486317276954651 | 0.378298474945534 | 0.0987794175744057 | 0.201905814827453 | 5 |
| 2923.03333333333 | 2923.03333333333 | 0.544256031513214 | 0.34095234204793 | 0.0895770713686943 | 0.216493506239427 | 5 |
| 2928.03333333333 | 2928.03333333333 | 0.549427270889282 | 0.335804466230937 | 0.0637638866901398 | 0.0902672171622905 | 5 |
| 2933.03333333333 | 2933.03333333333 | 0.450072199106216 | 0.383213779956427 | 0.131819173693657 | 0.246160038825613 | 5 |
| 2938.03333333333 | 2938.03333333333 | 0.470616847276688 | 0.357222222222222 | 0.11304248124361 | 0.174191225757079 | 5 |
| 2943.03333333333 | 2943.03333333333 | 0.500433325767517 | 0.354282952069717 | 0.112102940678596 | 0.158067840676378 | 5 |
| 2948.03333333333 | 2948.03333333333 | 0.423161506652832 | 0.453489379084967 | 0.126430824398994 | 0.269789806916615 | 5 |
| 2953.03333333333 | 2953.03333333333 | 0.484967350959778 | 0.363577614379085 | 0.130968138575554 | 0.311250955157919 | 5 |
| 2958.03333333333 | 2958.03333333333 | 0.54393082857132 | 0.335347766884532 | 0.105710789561272 | 0.199734982579336 | 5 |
| 2963.03333333333 | 2963.03333333333 | 0.460238575935364 | 0.410337418300654 | 0.128302827477455 | 0.308347400055684 | 5 |
| 2968.03333333333 | 2968.03333333333 | 0.460628300905228 | 0.408015522875817 | 0.0554038658738136 | 0.0776733006758174 | 5 |
| 2973.03333333333 | 2973.03333333333 | 0.46073579788208 | 0.407369281045752 | 0.0449882932007313 | 0.0684765166013164 | 5 |
| 2978.03333333333 | 2978.03333333333 | 0.474355667829514 | 0.400768790849673 | 0.0692587122321129 | 0.138431476869034 | 5 |
| 2983.03333333333 | 2983.03333333333 | 0.475125789642334 | 0.390976307189543 | 0.0514183007180691 | 0.108090387506126 | 5 |
| 2988.03333333333 | 2988.03333333333 | 0.536496698856354 | 0.34349128540305 | 0.0973513126373291 | 0.238488783834004 | 5 |
| 2993.03333333333 | 2993.03333333333 | 0.49387064576149 | 0.363669117647059 | 0.113185457885265 | 0.244192433167831 | 5 |
| 2998.03333333333 | 2998.03333333333 | 0.495497286319733 | 0.364104575163399 | 0.0285427551716566 | 0.0522604093529372 | 5 |
| 3003.03333333333 | 3003.03333333333 | 0.477014988660812 | 0.378753267973856 | 0.103930547833443 | 0.1435644185896 | 5 |
| 3008.03333333333 | 3008.03333333333 | 0.487113296985626 | 0.358473039215686 | 0.106488831341267 | 0.18952426154594 | 5 |
| 3013.03333333333 | 3013.03333333333 | 0.481329798698425 | 0.364581427015251 | 0.0338227115571499 | 0.05713763527821 | 5 |
| 3018.03333333333 | 3018.03333333333 | 0.432181090116501 | 0.394652233115468 | 0.0958692729473114 | 0.23328973453943 | 5 |
| 3023.03333333333 | 3023.03333333333 | 0.468337178230286 | 0.37390522875817 | 0.101675108075142 | 0.181117592532522 | 5 |
| 3028.03333333333 | 3028.03333333333 | 0.486505746841431 | 0.368349673202614 | 0.0660318657755852 | 0.109687127319265 | 5 |
| 3033.03333333333 | 3033.03333333333 | 0.46847853064537 | 0.366391612200436 | 0.108934089541435 | 0.160287798214002 | 5 |
| 3038.03333333333 | 3038.03333333333 | 0.400129079818726 | 0.42924591503268 | 0.110813446342945 | 0.215435848727073 | 5 |
| 3043.03333333333 | 3043.03333333333 | 0.338714063167572 | 0.46728022875817 | 0.0786944404244423 | 0.256426822913646 | 5 |
| 3048.03333333333 | 3048.03333333333 | 0.474185466766357 | 0.391182189542484 | 0.140442535281181 | 0.333346393165152 | 5 |
| 3053.03333333333 | 3053.03333333333 | 0.469333916902542 | 0.388967047930283 | 0.0606734715402126 | 0.0937679100899639 | 5 |
| 3058.03333333333 | 3058.03333333333 | 0.357823550701141 | 0.42604765795207 | 0.135794654488564 | 0.362637920742979 | 5 |
| 3063.03333333333 | 3063.03333333333 | 0.364867389202118 | 0.4770901416122 | 0.0998646542429924 | 0.235946196097133 | 5 |
| 3068.03333333333 | 3068.03333333333 | 0.389453440904617 | 0.444900326797386 | 0.12069171667099 | 0.195489875279256 | 5 |
| 3073.03333333333 | 3073.03333333333 | 0.455512821674347 | 0.393075435729847 | 0.112957514822483 | 0.296066218853541 | 5 |
| 3078.03333333333 | 3078.03333333333 | 0.425194710493088 | 0.404206427015251 | 0.102175921201706 | 0.25183085603466 | 5 |
| 3083.03333333333 | 3083.03333333333 | 0.503512799739838 | 0.35889651416122 | 0.108061000704765 | 0.257407634696467 | 5 |
| 3088.03333333333 | 3088.03333333333 | 0.480973601341248 | 0.372549291938998 | 0.0770599022507668 | 0.134114409583995 | 5 |
| 3093.03333333333 | 3093.03333333333 | 0.468764185905457 | 0.381441448801743 | 0.0622519105672836 | 0.0661791584948777 | 5 |
| 3098.03333333333 | 3098.03333333333 | 0.485126376152039 | 0.364076525054466 | 0.0720000043511391 | 0.148331357565513 | 5 |
| 3103.03333333333 | 3103.03333333333 | 0.489785701036453 | 0.36065059912854 | 0.0378221683204174 | 0.05569303001365 | 5 |
| 3108.03333333333 | 3108.03333333333 | 0.498343974351883 | 0.359755174291939 | 0.0370560996234417 | 0.0609570071198752 | 5 |
| 3113.03333333333 | 3113.03333333333 | 0.480679750442505 | 0.392063725490196 | 0.0824588760733604 | 0.216549868037697 | 5 |
| 3118.03333333333 | 3118.03333333333 | 0.465515285730362 | 0.393882080610022 | 0.0749951004981995 | 0.193467252819579 | 5 |
| 3123.03333333333 | 3123.03333333333 | 0.466935753822327 | 0.391908224400871 | 0.059687364846468 | 0.0720100104589291 | 5 |
| 3128.03333333333 | 3128.03333333333 | 0.467919647693634 | 0.389299564270152 | 0.0336282663047314 | 0.0626617513221261 | 5 |
| 3133.03333333333 | 3133.03333333333 | 0.488624185323715 | 0.367110838779956 | 0.0864959135651588 | 0.230634639069223 | 5 |
| 3138.03333333333 | 3138.03333333333 | 0.496771246194839 | 0.361876906318083 | 0.0429275594651699 | 0.07234392410732 | 5 |
| 3143.03333333333 | 3143.03333333333 | 0.428402781486511 | 0.445349673202614 | 0.126374468207359 | 0.260096920187017 | 5 |
| 3148.03333333333 | 3148.03333333333 | 0.495792478322983 | 0.364803104575163 | 0.133729577064514 | 0.265879802410101 | 5 |
| 3153.03333333333 | 3153.03333333333 | 0.491095036268234 | 0.369642701525054 | 0.046873364597559 | 0.0611966473012003 | 5 |
| 3158.03333333333 | 3158.03333333333 | 0.495746999979019 | 0.366627723311547 | 0.0345838740468025 | 0.043362585505083 | 5 |
| 3163.03333333333 | 3163.03333333333 | 0.52577805519104 | 0.358125272331155 | 0.111214056611061 | 0.192949659755926 | 5 |
| 3168.03333333333 | 3168.03333333333 | 0.486350774765015 | 0.356567810457516 | 0.0974044129252434 | 0.248514887212359 | 5 |
| 3173.03333333333 | 3173.03333333333 | 0.486658215522766 | 0.363282679738562 | 0.0321353450417519 | 0.096344275033739 | 5 |
| 3178.03333333333 | 3178.03333333333 | 0.488727957010269 | 0.371327069716776 | 0.0883540287613869 | 0.196721847046885 | 5 |
| 3183.03333333333 | 3183.03333333333 | 0.485059142112732 | 0.372618464052288 | 0.0372608937323093 | 0.0787758501736061 | 5 |
| 3188.03333333333 | 3188.03333333333 | 0.478654414415359 | 0.372450163398693 | 0.111021779477596 | 0.265814580367053 | 5 |
| 3193.03333333333 | 3193.03333333333 | 0.493952631950378 | 0.365645152505447 | 0.0692088827490807 | 0.0967090964439638 | 5 |
| 3198.03333333333 | 3198.03333333333 | 0.578937351703644 | 0.323367374727669 | 0.111411213874817 | 0.36097936705027 | 5 |
| 3203.03333333333 | 3203.03333333333 | 0.457255750894547 | 0.368229302832244 | 0.138368457555771 | 0.309469379548982 | 5 |
| 3208.03333333333 | 3208.03333333333 | 0.259323805570602 | 0.288833333333333 | 0.200077891349792 | 0.511022437340533 | 5 |
| 3213.03333333333 | 3213.03333333333 | 0.357023447751999 | 0.431987472766884 | 0.100228488445282 | 0.339839696721309 | 5 |
| 3218.03333333333 | 3218.03333333333 | 0.340015798807144 | 0.427064814814815 | 0.081586055457592 | 0.376640299828147 | 5 |
| 3223.03333333333 | 3223.03333333333 | 0.385511159896851 | 0.39990931372549 | 0.0950977727770805 | 0.373834852776688 | 5 |
| 3228.03333333333 | 3228.03333333333 | 0.359074920415878 | 0.387867919389978 | 0.0754095911979675 | 0.221313681736104 | 5 |
| 3233.03333333333 | 3233.03333333333 | 0.385134816169739 | 0.385054466230937 | 0.0366116538643837 | 0.124164057998605 | 5 |
| 3238.03333333333 | 3238.03333333333 | 0.385566741228104 | 0.382531590413943 | 0.0158006548881531 | 0.0513641002209544 | 5 |
| 3243.03333333333 | 3243.03333333333 | 0.355439275503159 | 0.369054738562091 | 0.0615479312837124 | 0.206070240705495 | 5 |
| 3248.03333333333 | 3248.03333333333 | 0.372348338365555 | 0.3802848583878 | 0.0561644919216633 | 0.27971761771028 | 5 |
| 3253.03333333333 | 3253.03333333333 | 0.374124199151993 | 0.378258442265795 | 0.0318238027393818 | 0.0505306819970542 | 5 |
| 3258.03333333333 | 3258.03333333333 | 0.361584424972534 | 0.376277233115468 | 0.0433758199214935 | 0.156772585102107 | 5 |
| 3263.03333333333 | 3263.03333333333 | 0.34527587890625 | 0.342156590413943 | 0.0500787012279034 | 0.208684021759098 | 5 |
| 3268.03333333333 | 3268.03333333333 | 0.345170766115189 | 0.339282135076253 | 0.00605119811370969 | 0.0421781493563439 | 5 |
| 3273.03333333333 | 3273.03333333333 | 0.364440381526947 | 0.377201797385621 | 0.0474994592368603 | 0.202953001771031 | 5 |
| 3278.03333333333 | 3278.03333333333 | 0.362229317426682 | 0.378430010893246 | 0.0175509266555309 | 0.0517656327240056 | 5 |
| 3283.03333333333 | 3283.03333333333 | 0.3628790974617 | 0.378528867102397 | 0.00814814772456884 | 0.04486760900782 | 5 |
| 3288.03333333333 | 3288.03333333333 | 0.359173744916916 | 0.370598311546841 | 0.0547826811671257 | 0.199831896639625 | 5 |
| 3293.03333333333 | 3293.03333333333 | 0.376144915819168 | 0.380548202614379 | 0.0546922646462917 | 0.256287882645751 | 5 |
| 3298.03333333333 | 3298.03333333333 | 0.3404640853405 | 0.344756263616558 | 0.0577031634747982 | 0.291762617242569 | 5 |
| 3303.03333333333 | 3303.03333333333 | 0.361650854349136 | 0.370658496732026 | 0.0483752712607384 | 0.209676333283888 | 5 |
| 3308.03333333333 | 3308.03333333333 | 0.357394069433212 | 0.3832151416122 | 0.0542137809097767 | 0.211194903258695 | 5 |
| 3313.03333333333 | 3313.03333333333 | 0.360200434923172 | 0.368330065359477 | 0.0572693385183811 | 0.213149287801467 | 5 |
| 3318.03333333333 | 3318.03333333333 | 0.359415888786316 | 0.367907679738562 | 0.0123444981873035 | 0.0509431161764118 | 5 |
| 3323.03333333333 | 3323.03333333333 | 0.360213756561279 | 0.367927015250545 | 0.0171067547053099 | 0.051983561504939 | 5 |
| 3328.03333333333 | 3328.03333333333 | 0.361648142337799 | 0.367464052287582 | 0.0169376377016306 | 0.0556043980662095 | 5 |
| 3333.03333333333 | 3333.03333333333 | 0.362614125013351 | 0.376106753812636 | 0.0171266328543425 | 0.0696347713866167 | 5 |
| 3338.03333333333 | 3338.03333333333 | 0.37652587890625 | 0.374791666666667 | 0.0416378006339073 | 0.136246266125231 | 5 |
| 3343.03333333333 | 3343.03333333333 | 0.357170760631561 | 0.409857026143791 | 0.077799566090107 | 0.225993131713416 | 5 |
| 3348.03333333333 | 3348.03333333333 | 0.380382388830185 | 0.377383169934641 | 0.0762219503521919 | 0.189468445927431 | 5 |
| 3353.03333333333 | 3353.03333333333 | 0.370643228292465 | 0.365087962962963 | 0.0553502142429352 | 0.118857338478925 | 5 |
| 3358.03333333333 | 3358.03333333333 | 0.350954532623291 | 0.398293300653595 | 0.0789016857743263 | 0.137703892538062 | 5 |
| 3363.03333333333 | 3363.03333333333 | 0.39916667342186 | 0.385183006535948 | 0.0879343673586845 | 0.241084472444716 | 5 |
| 3368.03333333333 | 3368.03333333333 | 0.364458352327347 | 0.401444716775599 | 0.0854948237538338 | 0.25213606502419 | 5 |
| 3373.03333333333 | 3373.03333333333 | 0.35429385304451 | 0.401986655773421 | 0.0927129611372948 | 0.224006190903505 | 5 |
| 3378.03333333333 | 3378.03333333333 | 0.352687656879425 | 0.440464869281046 | 0.0527516342699528 | 0.121511119275092 | 5 |
| 3383.03333333333 | 3383.03333333333 | 0.394043028354645 | 0.38530991285403 | 0.0646086558699608 | 0.206527783980247 | 5 |
| 3388.03333333333 | 3388.03333333333 | 0.360984772443771 | 0.435214869281046 | 0.0672047957777977 | 0.214589024068277 | 5 |
| 3393.03333333333 | 3393.03333333333 | 0.387148708105087 | 0.368073801742919 | 0.0542984753847122 | 0.178134590979599 | 5 |
| 3398.03333333333 | 3398.03333333333 | 0.355046033859253 | 0.369264705882353 | 0.0625051707029343 | 0.144958222574311 | 5 |
| 3403.03333333333 | 3403.03333333333 | 0.395893275737762 | 0.389022331154684 | 0.092079259455204 | 0.209385727374156 | 5 |
| 3408.03333333333 | 3408.03333333333 | 0.4005266726017 | 0.391218681917211 | 0.033249456435442 | 0.0602548722314418 | 5 |
| 3413.03333333333 | 3413.03333333333 | 0.374574393033981 | 0.400026416122004 | 0.0776783749461174 | 0.204593313089652 | 5 |
| 3418.03333333333 | 3418.03333333333 | 0.326621770858765 | 0.506502178649238 | 0.0724896490573883 | 0.297669880948072 | 5 |


## Record 21 — M04: Dear037

| Record field | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| generation | current_execution |
| processing_fingerprint | 97f78b70ad03cd7c99d2974e0f64be1304c6c1391891fd11a99452751125b6a0 |
| started_utc | 2026-09-10T06:21:18.577434+00:00 |
| completed_utc | 2026-09-10T06:21:30.891382+00:00 |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear037 |
| input_path | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| filename | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| size_bytes | 193460076 |
| sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| start_s | 3418.16666666667 |
| end_s | 3818.83333333333 |
| duration_s | 400.666666666667 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 102545 to 114565 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-037, frames/M04_frame_header_09.jpg, frames/M04_frame_header_10.jpg, adv_dear_hmsz_037.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
| decode_warnings |  |
| direct_listening | false |
| direct_visual_inspection | false |
| interpretation_limit | Automated measurements of the full mix and whole frame. No isolated voice, emotion, genre, motion-quality or narrative conclusion follows. |


### Processing identity and parameters

| Parameter | Value |
| --- | --- |
| schema | gkm-targeted-av-current-measurement/1.0 |
| input_sha256 | 38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a |
| source_id | 1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE |
| character | MISUZU |
| alias | M04 |
| label | Dear037 |
| boundary_note | directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval. Reference frames 102545 to 114565 at 30 fps. Evidence: EXEC-MZ-M04-BOUNDARY-037, frames/M04_frame_header_09.jpg, frames/M04_frame_header_10.jpg, adv_dear_hmsz_037.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad |
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
| parameters.start_s | 3418.16666666667 |
| parameters.end_s | 3818.83333333333 |
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
| streams[0].mime_codec_string | avc1.4d401f |
| streams[0].width | 1280 |
| streams[0].height | 720 |
| streams[0].coded_width | 1280 |
| streams[0].coded_height | 720 |
| streams[0].has_b_frames | 1 |
| streams[0].sample_aspect_ratio | 1:1 |
| streams[0].display_aspect_ratio | 16:9 |
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
| streams[0].duration_ts | 62185984 |
| streams[0].duration | 4048.566667 |
| streams[0].bit_rate | 243484 |
| streams[0].bits_per_raw_sample | 8 |
| streams[0].nb_frames | 121457 |
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
| streams[1].duration_ts | 178544640 |
| streams[1].duration | 4048.631293 |
| streams[1].bit_rate | 127999 |
| streams[1].nb_frames | 174360 |
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
| streams[2].duration_ts | 364376816 |
| streams[2].duration | 4048.631289 |
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
| format.filename | WORKSPACE/Gakuen Idolmaster\media-inbox\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4 |
| format.nb_streams | 3 |
| format.nb_programs | 0 |
| format.nb_stream_groups | 0 |
| format.format_name | mov,mp4,m4a,3gp,3g2,mj2 |
| format.format_long_name | QuickTime / MOV |
| format.start_time | 0.000000 |
| format.duration | 4048.631293 |
| format.size | 193460076 |
| format.bit_rate | 382272 |
| format.probe_score | 100 |
| format.tags.major_brand | isom |
| format.tags.minor_version | 512 |
| format.tags.compatible_brands | isomiso2avc1mp41 |
| format.tags.title | 【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】 |
| format.tags.artist | 学マスコミュ保管委員会 |
| format.tags.genre | Gaming |
| format.tags.date | 20260516 |
| format.tags.encoder | Lavf60.16.100 |
| format.tags.comment | https://www.youtube.com/watch?v=Loj480JIDkI |
| format.tags.description | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |
| format.tags.synopsis | ※この動画には学園アイドルマスターのネタバレが含まれます。<br><br>↓再生リスト<br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i<br><br>https://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh<br><br><br>#学園アイドルマスター #学マス |


### Audio features

| Audio feature | Value |
| --- | --- |
| sample_rate_hz | 22050 |
| audio_samples | 8834700 |
| analyzed_audio_duration_s | 400.666666666667 |
| stft_frames | 17252 |
| flux_transitions | 17251 |
| rms_linear | 0.094747661559096 |
| rms_p10_linear | 0.00700034891725541 |
| rms_p90_linear | 0.173153907190233 |
| rms_p90_p10_db | 27.8662521751692 |
| rms_p10_floor_applied | false |
| rms_p10_near_zero | false |
| rms_frames_below_1e_minus8 | 848 |
| centroid_hz_mean | 1627.90050297614 |
| flatness_mean | 0.066702901182139 |
| positive_normalized_flux_mean | 0.0325060633300726 |
| flux_cv | 0.714620049762653 |


### Loudness and low-level intervals

| Loudness field | Value |
| --- | --- |
| integrated_lufs | -19.3 |
| lra_lu | 6.7 |
| true_peak_dbfs | -4.3 |
| silence_seconds | 26.09812 |
| unclosed_silence_start_s | N/A |
| ebur128_summary | Summary:<br><br>  Integrated loudness:<br>    I:         -19.3 LUFS<br>    Threshold: -30.5 LUFS<br><br>  Loudness range:<br>    LRA:         6.7 LU<br>    Threshold: -40.7 LUFS<br>    LRA low:   -24.8 LUFS<br>    LRA high:  -18.1 LUFS<br><br>  True peak:<br>    Peak:       -4.3 dBFS<br>[out#0/null @ 0000017f81ec7a80] video:0KiB audio:69021KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown<br>size=N/A time=00:06:40.66 bitrate=N/A speed=88.4x elapsed=0:00:04.53 |
| ffmpeg_stderr_sha256 | c50b0811f326554581365192ddd350692400688cec5d2b2b18dff6995712b3d0 |
| time_origin | segment-local decoded audio origin; add requested start_s for source-relative locator |


| Segment-local start s | End s | Computed duration s | FFmpeg reported duration s |
| --- | --- | --- | --- |
| 70.274739 | 71.086961 | 0.812222000000006 | 0.812222 |
| 72.68102 | 74.03619 | 1.35517 | 1.35517 |
| 74.247052 | 75.391497 | 1.144445 | 1.144444 |
| 76.309365 | 77.905941 | 1.596576 | 1.596576 |
| 79.505601 | 80.281338 | 0.775737000000007 | 0.775737 |
| 81.228254 | 82.83059 | 1.60233599999999 | 1.602336 |
| 83.026463 | 83.796122 | 0.76965899999999 | 0.76966 |
| 84.617029 | 85.250839 | 0.633809999999997 | 0.63381 |
| 213.283673 | 213.816531 | 0.532858000000004 | 0.532857 |
| 225.252789 | 227.477347 | 2.224558 | 2.224558 |
| 230.220023 | 232.160794 | 1.94077100000001 | 1.940771 |
| 236.476122 | 239.231406 | 2.75528399999999 | 2.755283 |
| 326.590748 | 327.6278 | 1.03705199999996 | 1.037052 |
| 329.495125 | 330.297551 | 0.802426000000025 | 0.802426 |
| 331.730726 | 333.251565 | 1.52083900000002 | 1.520839 |
| 335.473651 | 338.119887 | 2.64623599999999 | 2.646236 |
| 340.095329 | 341.047052 | 0.951723000000015 | 0.951723 |
| 341.820023 | 343.321156 | 1.50113299999998 | 1.501134 |
| 344.356689 | 344.981497 | 0.624807999999973 | 0.624807 |
| 399.79619 | 400.666667 | 0.870476999999994 | 0.870476 |


### Sampled visual output

| Visual field | Value |
| --- | --- |
| status | measured |
| sample_step_s | 5 |
| sample_width | 160 |
| sample_height | 90 |
| scheduled_samples | 81 |
| samples | 81 |
| brightness_mean | 0.389541403746899 |
| saturation_mean | 0.459597528174507 |
| frame_difference_mean | 0.0448859913856722 |
| histogram_jumps_gt_0_5 | 1 |


| Requested source s | Decoder reported s | Luma | Saturation | Difference from prior successful sample | Histogram distance | Elapsed from prior sample s |
| --- | --- | --- | --- | --- | --- | --- |
| 3418.16666666667 | 3418.16666666667 | 0.326660692691803 | 0.505580610021786 | N/A | N/A | N/A |
| 3423.16666666667 | 3423.16666666667 | 0.371956706047058 | 0.48155991285403 | 0.0559801235795021 | 0.152955164972741 | 5 |
| 3428.16666666667 | 3428.16666666667 | 0.390015244483948 | 0.457675381263617 | 0.03963752835989 | 0.153025078778634 | 5 |
| 3433.16666666667 | 3433.16666666667 | 0.373358964920044 | 0.482301470588235 | 0.0381432510912418 | 0.148370731232225 | 5 |
| 3438.16666666667 | 3438.16666666667 | 0.369078755378723 | 0.483480119825708 | 0.0144005985930562 | 0.0599062407859021 | 5 |
| 3443.16666666667 | 3443.16666666667 | 0.369001358747482 | 0.48193137254902 | 0.0159787572920322 | 0.0420145830533731 | 5 |
| 3448.16666666667 | 3448.16666666667 | 0.367940932512283 | 0.485721132897603 | 0.0086388885974884 | 0.0451622299663085 | 5 |
| 3453.16666666667 | 3453.16666666667 | 0.371375322341919 | 0.480334694989107 | 0.0141576798632741 | 0.0461352950029379 | 5 |
| 3458.16666666667 | 3458.16666666667 | 0.391200453042984 | 0.451253812636166 | 0.0414281040430069 | 0.148582602401113 | 5 |
| 3463.16666666667 | 3463.16666666667 | 0.370536774396896 | 0.481022875816993 | 0.0404626876115799 | 0.144599911211254 | 5 |
| 3468.16666666667 | 3468.16666666667 | 0.370201289653778 | 0.481271786492375 | 0.00962091516703367 | 0.0594236003680841 | 5 |
| 3473.16666666667 | 3473.16666666667 | 0.369715452194214 | 0.484156590413943 | 0.00811329018324614 | 0.0597284725024214 | 5 |
| 3478.16666666667 | 3478.16666666667 | 0.380472511053085 | 0.373688180827887 | 0.0533872544765472 | 0.304143316313771 | 5 |
| 3483.16666666667 | 3483.16666666667 | 0.371678411960602 | 0.483011165577342 | 0.0525070838630199 | 0.30333622847615 | 5 |
| 3488.16666666667 | 3488.16666666667 | 0.37325194478035 | 0.482304466230937 | 0.013723311945796 | 0.0739983260130832 | 5 |
| 3493.16666666667 | 3493.16666666667 | 0.371786504983902 | 0.479787854030501 | 0.0158297922462225 | 0.0557496233420373 | 5 |
| 3498.16666666667 | 3498.16666666667 | 0.370560735464096 | 0.483032407407407 | 0.0082312086597085 | 0.0492525160396627 | 5 |
| 3503.16666666667 | 3503.16666666667 | 0.39702969789505 | 0.450037854030501 | 0.0438878051936626 | 0.154939932093848 | 5 |
| 3508.16666666667 | 3508.16666666667 | 0.394199341535568 | 0.451818355119826 | 0.0215454772114754 | 0.0588210987833766 | 5 |
| 3513.16666666667 | 3513.16666666667 | 0.388249158859253 | 0.459737472766885 | 0.0456168279051781 | 0.124486497380362 | 5 |
| 3518.16666666667 | 3518.16666666667 | 0.383677035570145 | 0.465320806100218 | 0.0363395996391773 | 0.0635990990315434 | 5 |
| 3523.16666666667 | 3523.16666666667 | 0.385281026363373 | 0.462103213507625 | 0.0302282143384218 | 0.0499909794069273 | 5 |
| 3528.16666666667 | 3528.16666666667 | 0.427349150180817 | 0.391207244008715 | 0.064084418118 | 0.23521143806115 | 5 |
| 3533.16666666667 | 3533.16666666667 | 0.431305885314941 | 0.391323801742919 | 0.0521919913589954 | 0.0884116955037951 | 5 |
| 3538.16666666667 | 3538.16666666667 | 0.392789781093597 | 0.393937363834423 | 0.0738532170653343 | 0.303176944510965 | 5 |
| 3543.16666666667 | 3543.16666666667 | 0.390126883983612 | 0.396379901960784 | 0.0332979299128056 | 0.0659793591819324 | 5 |
| 3548.16666666667 | 3548.16666666667 | 0.399666130542755 | 0.436527505446623 | 0.0535604618489742 | 0.281692858789193 | 5 |
| 3553.16666666667 | 3553.16666666667 | 0.430476874113083 | 0.392002995642702 | 0.0619441717863083 | 0.237334441131318 | 5 |
| 3558.16666666667 | 3558.16666666667 | 0.417493224143982 | 0.404835239651416 | 0.0583649277687073 | 0.130943514345085 | 5 |
| 3563.16666666667 | 3563.16666666667 | 0.502013623714447 | 0.332278050108932 | 0.118867918848991 | 0.281597304922119 | 5 |
| 3568.16666666667 | 3568.16666666667 | 0.35935565829277 | 0.396111928104575 | 0.153355658054352 | 0.40118825084898 | 5 |
| 3573.16666666667 | 3573.16666666667 | 0.370413422584534 | 0.383466503267974 | 0.069686271250248 | 0.260068763328409 | 5 |
| 3578.16666666667 | 3578.16666666667 | 0.331045776605606 | 0.589269880174292 | 0.0781187415122986 | 0.408158600454364 | 5 |
| 3583.16666666667 | 3583.16666666667 | 0.33134400844574 | 0.589648148148148 | 0.00406726589426398 | 0.0438837232413441 | 5 |
| 3588.16666666667 | 3588.16666666667 | 0.332137018442154 | 0.590130991285403 | 0.00411056634038687 | 0.0439341622613199 | 5 |
| 3593.16666666667 | 3593.16666666667 | 0.33244663476944 | 0.589089596949891 | 0.00341421575285494 | 0.0394371124995525 | 5 |
| 3598.16666666667 | 3598.16666666667 | 0.331660956144333 | 0.589343954248366 | 0.000904956366866827 | 0.0263838716473024 | 5 |
| 3603.16666666667 | 3603.16666666667 | 0.331627726554871 | 0.589890522875817 | 0.00320806098170578 | 0.0431718077885297 | 5 |
| 3608.16666666667 | 3608.16666666667 | 0.391396015882492 | 0.45280582788671 | 0.0669942796230316 | 0.345591184593905 | 5 |
| 3613.16666666667 | 3613.16666666667 | 0.370270967483521 | 0.482977941176471 | 0.0393744558095932 | 0.158671111459243 | 5 |
| 3618.16666666667 | 3618.16666666667 | 0.367526680231094 | 0.485828159041394 | 0.0140198795124888 | 0.0507968308617629 | 5 |
| 3623.16666666667 | 3623.16666666667 | 0.369246482849121 | 0.484612472766885 | 0.00517619820311666 | 0.0411427117062518 | 5 |
| 3628.16666666667 | 3628.16666666667 | 0.369301229715347 | 0.480007897603486 | 0.00717510841786861 | 0.0633737561768668 | 5 |
| 3633.16666666667 | 3633.16666666667 | 0.374397575855255 | 0.476128267973856 | 0.0154667757451534 | 0.0788055180964623 | 5 |
| 3638.16666666667 | 3638.16666666667 | 0.398692280054092 | 0.442214869281046 | 0.0433169938623905 | 0.150898439667511 | 5 |
| 3643.16666666667 | 3643.16666666667 | 0.37285241484642 | 0.4855174291939 | 0.0434330068528652 | 0.151394011667296 | 5 |
| 3648.16666666667 | 3648.16666666667 | 0.370968699455261 | 0.488165849673203 | 0.00882216822355986 | 0.0495296325940974 | 5 |
| 3653.16666666667 | 3653.16666666667 | 0.372344493865967 | 0.483203431372549 | 0.0162434633821249 | 0.0797038657551077 | 5 |
| 3658.16666666667 | 3658.16666666667 | 0.494449645280838 | 0.365501089324619 | 0.133155226707458 | 0.370701855586086 | 5 |
| 3663.16666666667 | 3663.16666666667 | 0.636136174201965 | 0.279529139433551 | 0.144248083233833 | 0.388522620102081 | 5 |
| 3668.16666666667 | 3668.16666666667 | 0.374597787857056 | 0.475770697167756 | 0.264153301715851 | 0.48810849644617 | 5 |
| 3673.16666666667 | 3673.16666666667 | 0.371300935745239 | 0.478107026143791 | 0.0167058818042278 | 0.0587854980377906 | 5 |
| 3678.16666666667 | 3678.16666666667 | 0.372725486755371 | 0.477946895424837 | 0.0137753272429109 | 0.0407131604657781 | 5 |
| 3683.16666666667 | 3683.16666666667 | 0.374396800994873 | 0.477055555555556 | 0.0172350220382214 | 0.0652124548814117 | 5 |
| 3688.16666666667 | 3688.16666666667 | 0.373915880918503 | 0.477692538126362 | 0.00553540326654911 | 0.0398994024456222 | 5 |
| 3693.16666666667 | 3693.16666666667 | 0.394825428724289 | 0.449787854030501 | 0.0407603494822979 | 0.148182530913728 | 5 |
| 3698.16666666667 | 3698.16666666667 | 0.393751353025436 | 0.452307461873638 | 0.015246732160449 | 0.0522200012595875 | 5 |
| 3703.16666666667 | 3703.16666666667 | 0.372701019048691 | 0.479924836601307 | 0.0417137816548347 | 0.13691158108116 | 5 |
| 3708.16666666667 | 3708.16666666667 | 0.374461054801941 | 0.481156590413943 | 0.0122322980314493 | 0.0576659096728714 | 5 |
| 3713.16666666667 | 3713.16666666667 | 0.3748559653759 | 0.47908197167756 | 0.0139460787177086 | 0.0578220168819388 | 5 |
| 3718.16666666667 | 3718.16666666667 | 0.394469797611237 | 0.452541394335512 | 0.0423747301101685 | 0.148663213038375 | 5 |
| 3723.16666666667 | 3723.16666666667 | 0.370020985603333 | 0.479536492374728 | 0.0425103455781937 | 0.1534842226806 | 5 |
| 3728.16666666667 | 3728.16666666667 | 0.370636165142059 | 0.480692265795207 | 0.0150694446638227 | 0.0529555800579412 | 5 |
| 3733.16666666667 | 3733.16666666667 | 0.369637548923492 | 0.48195697167756 | 0.00943273399025202 | 0.0497933874680714 | 5 |
| 3738.16666666667 | 3738.16666666667 | 0.392779976129532 | 0.451500272331155 | 0.0414234772324562 | 0.14893203178419 | 5 |
| 3743.16666666667 | 3743.16666666667 | 0.39557409286499 | 0.450789760348584 | 0.0190354026854038 | 0.0552976780523019 | 5 |
| 3748.16666666667 | 3748.16666666667 | 0.394922971725464 | 0.448141067538126 | 0.017160402610898 | 0.0695105267842364 | 5 |
| 3753.16666666667 | 3753.16666666667 | 0.372480392456055 | 0.476782679738562 | 0.0409109480679035 | 0.147152523300753 | 5 |
| 3758.16666666667 | 3758.16666666667 | 0.370574116706848 | 0.48191394335512 | 0.00723311584442854 | 0.0268285794060278 | 5 |
| 3763.16666666667 | 3763.16666666667 | 0.396557480096817 | 0.452171023965142 | 0.0430422127246857 | 0.157235025355289 | 5 |
| 3768.16666666667 | 3768.16666666667 | 0.397604018449783 | 0.445251906318083 | 0.0262116007506847 | 0.0792893189528202 | 5 |
| 3773.16666666667 | 3773.16666666667 | 0.63609915971756 | 0.279822712418301 | 0.23871186375618 | 0.446760013836578 | 5 |
| 3778.16666666667 | 3778.16666666667 | 0.443379104137421 | 0.442104302832244 | 0.195352375507355 | 0.420687010311672 | 5 |
| 3783.16666666667 | 3783.16666666667 | 0.437620103359222 | 0.453263071895425 | 0.0174463503062725 | 0.10988299013242 | 5 |
| 3788.16666666667 | 3788.16666666667 | 0.404343396425247 | 0.400864923747277 | 0.0713774561882019 | 0.315640803292354 | 5 |
| 3793.16666666667 | 3793.16666666667 | 0.437483966350555 | 0.4507674291939 | 0.0680430233478546 | 0.314756059738386 | 5 |
| 3798.16666666667 | 3798.16666666667 | 0.429026424884796 | 0.459616557734205 | 0.0127559918910265 | 0.109495851723501 | 5 |
| 3803.16666666667 | 3803.16666666667 | 0.43632897734642 | 0.458249455337691 | 0.0143265258520842 | 0.0900637809918571 | 5 |
| 3808.16666666667 | 3808.16666666667 | 0.443566501140594 | 0.449257625272331 | 0.0184635072946548 | 0.133064741341988 | 5 |
| 3813.16666666667 | 3813.16666666667 | 0.366865754127502 | 0.499692810457516 | 0.122697979211807 | 0.328877577409017 | 5 |
| 3818.16666666667 | 3818.16666666667 | 0.259287327528 | 0.294584150326797 | 0.107680834829807 | 0.545191300714101 | 5 |



