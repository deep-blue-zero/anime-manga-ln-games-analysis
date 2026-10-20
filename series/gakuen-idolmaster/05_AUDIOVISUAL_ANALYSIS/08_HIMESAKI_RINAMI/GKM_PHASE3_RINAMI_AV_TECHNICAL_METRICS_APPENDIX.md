---
series: GKM
artifact_type: audit
scope: CHARACTER_HIMESAKI_RINAMI_PHASE3_AV_TECHNICAL_METRICS
character: Himesaki Rinami / 姫崎莉波
generation: V2
release: R2
status: canonical
source_boundary: ffprobe, SHA-256, preferred-source materialization audit, source-level audio metrics, sparse-frame descriptors, and selected mixed-scene proxies for 27 logical AV objects
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
last_updated: '2026-08-22'
parent_authority: GKM_RINAMI_COMPLETE_AUDIOVISUAL_BASELINE.md
title: Himesaki Rinami Phase-3 AV Technical Metrics Appendix R2
legacy_supersession_notes:
- 'legacy supersedes: GAKUEN_IDOLMASTER_PHASE3_RINAMI_INTEGRATED_AV_R1/GKM_PHASE3_RINAMI_AV_TECHNICAL_METRICS_APPENDIX.md'
---

# HIMESAKI RINAMI — AV TECHNICAL METRICS APPENDIX R2

## 0. Interpretation limits

These measurements support auditability and source comparison. They are not isolated measurements of Yuri Usui's vocal stem, motion-capture quality scores, medical evidence, objective genre labels, or direct measures of charisma, maturity, authenticity, emotion, and skill.

The authoritative byte-level inventory is `GKM_PHASE3_RINAMI_AUDIOVISUAL_SOURCE_MANIFEST.json`.

## 1. Materialization summary

- logical AV objects: **27**;
- preferred physical analysis files: **27**;
- canonical duration: **19341.187 seconds / 5.373 hours**;
- canonical preferred-source bytes: **3,098,241,215 / 3.098 GB decimal**;
- Dear 001-010: **1920x1080 / 30 fps direct upload**;
- Dear 011-020: **1920x1080 / 30 fps direct upload**;
- Dear 021-027: **1280x720 / 60 fps direct upload**;
- Dear 028-037: **1280x720 / 30 fps direct upload**;
- all principal 3DMVs and authored MVs: **1920x1080**.

R2 supersedes the R1 visual fallback boundary. For D03 and D04, the preferred high-resolution files and the R1 low-resolution Drive counterparts have identical copied AAC elementary-stream MD5 values:

| source | R1 fallback | R2 preferred | audio elementary-stream MD5 |
| --- | --- | --- | --- |
| D03 / Dear 021-027 | 854x480 / 30 fps | 1280x720 / 60 fps | `3f7ba36f758b8a56dabceb7250bfd39e` |
| D04 / Dear 028-037 | 640x360 / 30 fps | 1280x720 / 30 fps | `b3c644762b8a966c39049d9a54494330` |

Therefore the R2 revision changes visual evidence and file identity, not dialogue timing or delivered audio content.

## 2. Source inventory

| ID | source | form | duration | video | Drive ID | analysis provenance |
| --- | --- | --- | --- | --- | --- | --- |
| `RINAMI-C01` | clumsy trick song commu | `song_commu` | 463.3 s | 1920x1080 @ 30/1 | `1y4P4qHcDTSXRh4B0bWRqJb55-Jchtotz` | drive |
| `RINAMI-C02` | L.U.V song commu | `song_commu` | 546.1 s | 1920x1080 @ 30/1 | `1m-xcWHo6ReovioG54sVQpVAg01mwyooK` | drive |
| `RINAMI-C03` | 36℃ U･B･U song commu | `song_commu` | 640.8 s | 854x480 @ 30/1 | `1tVWV_b-8gas9i6082Ka71NSR67mUR4iP` | drive |
| `RINAMI-C04` | Campus mode!! song commu | `song_commu` | 620.2 s | 640x360 @ 30/1 | `1V3pZF4U9IpknhZfONkuPPWSasoRth2Nq` | drive |
| `RINAMI-C05` | ガラクタロード song commu | `song_commu` | 605.5 s | 854x480 @ 30/1 | `1lOJUTIl6n933dF289HqWVnwtZbv1iQu4` | drive |
| `RINAMI-C06` | Howling over the World song commu | `song_commu` | 524.1 s | 1920x1080 @ 30/1 | `18bto1TMmOiIpkUJ3HklvhG-R7Lv4Xeqr` | drive |
| `RINAMI-C07` | SUGAR FLAVOR / RippleSign song commu | `song_commu` | 657.7 s | 854x480 @ 30/1 | `1uBw92jig8Y-DtDZ-kaEUHPCioWjDqomr` | drive |
| `RINAMI-D01` | Dear 001-010 | `dear_compilation` | 3072.3 s | 1920x1080 @ 30/1 | `1UnCKMPc_TD9OWPqE5hpyd234EpwrxheM` | library_direct_upload |
| `RINAMI-D02` | Dear 011-020 | `dear_compilation` | 2976.7 s | 1920x1080 @ 30/1 | `1quvQodKda8W7EUgjyGVnhDfY0P6YqSxD` | library_direct_upload |
| `RINAMI-D03` | Dear 021-027 / STEP3 | `dear_compilation` | 2823.2 s | 1280x720 @ 60/1 | `155A_tELCd-gDsL2Rh5XsmpDbuao6TvmY` | library_direct_upload |
| `RINAMI-D04` | Dear 028-037 / STEP4 H.I.F. | `dear_compilation` | 3613.9 s | 1280x720 @ 30/1 | `1S7_d7iqp2xlwXgOcmG8lD5vO7nl8cC9L` | library_direct_upload |
| `RINAMI-P01` | clumsy trick 3DMV | `3dmv` | 161.6 s | 1920x1080 @ 60/1 | `1ahpWzxQwn_DxOFFxZdLUlYz5v-hOsFid` | drive |
| `RINAMI-P02` | clumsy trick official MV | `official_mv` | 232.2 s | 1920x1080 @ 24/1 | `1GQ8SNx2PcNvqrySRChcRcxBZfA6vc8vY` | drive |
| `RINAMI-P03` | L.U.V 3DMV | `3dmv` | 200.7 s | 1920x1080 @ 60/1 | `1B5AMreNXJurwpf6OJjni3Lbi9uVuEwa9` | drive |
| `RINAMI-P04` | L.U.V full-song presentation | `static_full_mix` | 251.4 s | 1080x1080 @ 25/1 | `1VYqPYkkckcefcKFIMmA6OJzFWDu4lJ2A` | drive |
| `RINAMI-P05` | 36℃ U･B･U 3DMV | `3dmv` | 169.2 s | 1920x1080 @ 60/1 | `1iuVT_uX4l0TSDBuTfgMyXMxIdvUWJQvn` | drive |
| `RINAMI-P06` | 36℃ U･B･U official MV | `official_mv` | 251.6 s | 1920x1080 @ 30/1 | `197jq5Fix5fIGE9SEoet0Rwo4oyIM8ODA` | drive |
| `RINAMI-P07` | Campus mode!! 3DMV | `3dmv` | 160.4 s | 1920x1080 @ 60/1 | `16ZZpI69RLaju1y3-07BRSxm1siPkgqKz` | drive |
| `RINAMI-P08` | ガラクタロード 3DMV | `3dmv` | 164.1 s | 1920x1080 @ 60/1 | `1QaHxLTSvg0fTqr5JeeftelBPTsVuTjnS` | drive |
| `RINAMI-P09` | Howling over the World 3DMV | `3dmv` | 111.4 s | 1920x1080 @ 60/1 | `1kl8_uhs-iLkNXlkPdDpsuA50ryYqc5Z5` | drive |
| `RINAMI-P10` | SUGAR FLAVOR duet 3DMV | `3dmv` | 138.6 s | 1920x1080 @ 60/1 | `1clT7o2Sz9sA8mWpl7Ijz9XJgp9Y9ntsF` | drive |
| `RINAMI-P11` | SUGAR FLAVOR official MV | `official_mv` | 188.1 s | 1920x1080 @ 24/1 | `1jFJxvLA8ExtN-f17o20RPv8eVO0Jahbz` | drive |
| `RINAMI-P12` | 歌声は君いろ official MV | `official_mv` | 278.3 s | 1920x1080 @ 24/1 | `1CdvrQQ1XvvXZkBfyBp74CadKgstkrNeh` | drive |
| `RINAMI-P13` | ENDLESS DANCE 3DMV | `3dmv` | 109.6 s | 1920x1080 @ 60/1 | `106paLOR08gWzHAuNN2hGzASJ0II_ukr0` | drive |
| `RINAMI-P14` | がむしゃらに行こう！ 3DMV | `3dmv` | 116.8 s | 1920x1080 @ 60/1 | `1sP3EhPm7VV6dAE5zrLOnsLBh7l36EsoE` | drive |
| `RINAMI-P15` | ミラクルナナウ(ﾟ∀ﾟ)！ 3DMV | `3dmv` | 109.4 s | 1920x1080 @ 60/1 | `1PY8DFDQnz6miS0QjUH5MXdMlhzm_lq2a` | drive |
| `RINAMI-P16` | 初 [Rinami] song video | `song_video` | 153.9 s | 1084x1080 @ 30/1 | `1jRLY6NWRXIGjvL9njL1IsZJ6NI-5GOn6` | drive |

## 3. Source-quality boundary

| scope | analysis materialization | safe use | confidence limit |
| --- | --- | --- | --- |
| Dear 001-010 | 1920x1080 / 30 fps | timing, face/body, gaze, posture, reaction sequence, ordinary expression comparison | no laboratory facial-motion claims |
| Dear 011-020 | 1920x1080 / 30 fps | same | same |
| Dear 021-027 | 1280x720 / 60 fps | tears, blush, gaze, hand placement, running/body transition, reaction sequencing | single-frame mind-reading remains unsafe |
| Dear 028-037 | 1280x720 / 30 fps | tears, blush, gaze, hand placement, posture, mode transitions, public/private contrast | same |
| song commus | 360p-1080p | acted context, body state, reaction timing, intended meaning | source-specific resolution applies |
| principal 3DMVs/MVs | 1920x1080 | choreography, camera, costume, stage, authored imagery | rendered/coauthored object, not unaided live-skill proof |

## 4. Whole-mix source metrics

| ID | source | class | duration s | mean dBFS | max dBFS |
| --- | --- | --- | --- | --- | --- |
| `RINAMI-P01` | clumsy trick 3DMV | performance | 161.6 | -18.6 | -0.4 |
| `RINAMI-P02` | clumsy trick official MV | performance | 232.2 | -11.6 | 0.0 |
| `RINAMI-P03` | L.U.V 3DMV | performance | 200.7 | -19.3 | -0.0 |
| `RINAMI-P04` | L.U.V full-song presentation | performance | 251.4 | -12.9 | 0.0 |
| `RINAMI-P05` | 36℃ U･B･U 3DMV | performance | 169.2 | -16.7 | -0.4 |
| `RINAMI-P06` | 36℃ U･B･U official MV | performance | 251.6 | -16.6 | -1.1 |
| `RINAMI-P07` | Campus mode!! 3DMV | performance | 160.4 | -17.3 | -0.4 |
| `RINAMI-P08` | ガラクタロード 3DMV | performance | 164.1 | -18.2 | -0.4 |
| `RINAMI-P09` | Howling over the World 3DMV | performance | 111.4 | -17.8 | -0.2 |
| `RINAMI-P10` | SUGAR FLAVOR duet 3DMV | performance | 138.6 | -15.8 | -0.2 |
| `RINAMI-P11` | SUGAR FLAVOR official MV | performance | 188.1 | -12.6 | -0.0 |
| `RINAMI-P12` | 歌声は君いろ official MV | performance | 278.3 | -12.1 | 0.0 |
| `RINAMI-P13` | ENDLESS DANCE 3DMV | performance | 109.4 | -15.5 | -0.4 |
| `RINAMI-P14` | がむしゃらに行こう！ 3DMV | performance | 109.6 | -17.8 | -0.3 |
| `RINAMI-P15` | ミラクルナナウ(ﾟ∀ﾟ)！ 3DMV | performance | 116.8 | -18.0 | -0.0 |
| `RINAMI-P16` | 初 [Rinami] song video | performance | 153.9 | -19.7 | -6.4 |

Safe observations:

- source/mastering levels differ between official MVs and game captures;
- `L.U.V` 3DMV and full-song presentation differ because they are different delivered forms;
- no source-level level measurement ranks singing skill, emotion, or intrinsic vocal power.

## 5. Sparse whole-frame visual descriptors

| ID | source | frames | mean luma | mean saturation | inter-sample change |
| --- | --- | --- | --- | --- | --- |
| `RINAMI-P01` | clumsy trick 3DMV | 16 | 46.3 | 129.6 | 43.5 |
| `RINAMI-P02` | clumsy trick official MV | 16 | 187.8 | 50.6 | 69.2 |
| `RINAMI-P03` | L.U.V 3DMV | 16 | 79.7 | 126.5 | 55.4 |
| `RINAMI-P04` | L.U.V full-song presentation | 16 | 79.9 | 87.3 | 0.3 |
| `RINAMI-P05` | 36℃ U･B･U 3DMV | 16 | 84.1 | 103.5 | 65.6 |
| `RINAMI-P06` | 36℃ U･B･U official MV | 16 | 187.1 | 56.7 | 71.2 |
| `RINAMI-P07` | Campus mode!! 3DMV | 16 | 56.9 | 115.2 | 48.4 |
| `RINAMI-P08` | ガラクタロード 3DMV | 16 | 70.0 | 168.5 | 58.7 |
| `RINAMI-P09` | Howling over the World 3DMV | 16 | 61.5 | 124.8 | 50.8 |
| `RINAMI-P10` | SUGAR FLAVOR duet 3DMV | 16 | 48.2 | 120.4 | 42.9 |
| `RINAMI-P11` | SUGAR FLAVOR official MV | 16 | 117.8 | 132.9 | 80.6 |
| `RINAMI-P12` | 歌声は君いろ official MV | 16 | 107.0 | 86.6 | 64.3 |
| `RINAMI-P13` | ENDLESS DANCE 3DMV | 16 | 50.8 | 102.6 | 46.1 |
| `RINAMI-P14` | がむしゃらに行こう！ 3DMV | 16 | 96.8 | 120.7 | 56.4 |
| `RINAMI-P15` | ミラクルナナウ(ﾟ∀ﾟ)！ 3DMV | 16 | 113.8 | 96.2 | 51.4 |
| `RINAMI-P16` | 初 [Rinami] song video | 4 | 108.3 | 28.6 | 0.4 |

### 5.1 R2 late-route preferred-materialization descriptors

| ID | preferred source | frames | mean luma | mean saturation | inter-sample change |
| --- | --- | --- | --- | --- | --- |
| `RINAMI-D03` | 1280x720 @ 60/1 | 16 | 179.0 | 59.1 | 25.6 |
| `RINAMI-D04` | 1280x720 @ 30/1 | 16 | 116.2 | 102.1 | 33.2 |

These figures include UI, typography, scenery, effects, cuts, and other characters. Their safe use is broad source comparison and reproducibility. They do not quantify warmth, seductiveness, charisma, maturity, or acting quality.

## 6. Source-Lock-derived textual register metrics

| tranche | Rinami lines | ellipsis | questions | apology | want/desire | love | win | stammer marker |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Dear 001-010 | 435 | 50.8% | 21.15% | 1.38% | 0.69% | 1.15% | 1.15% | 11.49% |
| Dear 011-020 | 281 | 45.55% | 17.79% | 0.71% | 0.71% | 0.71% | 5.69% | 6.05% |
| Dear 021-027 | 303 | 45.87% | 18.48% | 2.31% | 1.98% | 1.65% | 3.96% | 5.28% |
| Dear 028-037 | 342 | 25.44% | 14.91% | 1.17% | 2.34% | 4.39% | 9.65% | 7.31% |

The safe longitudinal result is that late text makes love, victory, desire, and completed address more available while ellipsis density falls. Punctuation is not emotion and cannot replace scene reading.

## 7. Selected mixed-scene audio proxies

| segment | source | state | RMS dBFS | F0 proxy Hz | locator confidence |
| --- | --- | --- | --- | --- | --- |
| `RINAMI-S01` | `RINAMI-D01` | Dear 001 reencounter / near-retirement hesitation | -28.33 | 318.1 | high |
| `RINAMI-S02` | `RINAMI-D01` | Dear 003 produced-naturalness rehearsal | -26.36 | 286.0 | medium-high |
| `RINAMI-S03` | `RINAMI-D01` | Dear 009-010 private romantic self-recognition | -28.97 | 330.1 | medium-high |
| `RINAMI-S04` | `RINAMI-D01` | Dear 010 public performance threshold | -29.12 | 370.4 | medium |
| `RINAMI-S05` | `RINAMI-D02` | Dear 013-016 old persona / Shion pressure | -22.86 | 307.9 | medium |
| `RINAMI-S06` | `RINAMI-D02` | N.I.A. performance pressure / competitive escalation | -23.12 | 359.3 | medium |
| `RINAMI-S07` | `RINAMI-D02` | Dear 019-020 calibrated victory / reciprocal closeness | -23.04 | 354.6 | medium-high |
| `RINAMI-S08` | `RINAMI-D03` | Dear 023 summer H.I.F. disruption and loss | -26.56 | 381.5 | high |
| `RINAMI-S09` | `RINAMI-D03` | Dear 025-026 home / dream-ownership crisis | -27.98 | 174.6 | medium-high |
| `RINAMI-S10` | `RINAMI-D03` | Dear 027 優勝したかった / self-authored desire | -25.63 | 229.2 | high |
| `RINAMI-S11` | `RINAMI-D04` | Dear 031 technique as love / full-body fanservice | -21.87 | 257.0 | medium-high |
| `RINAMI-S12` | `RINAMI-D04` | Dear 033 H.O.F. result / audience love to self-love | -23.20 | 371.9 | high |
| `RINAMI-S13` | `RINAMI-D04` | Dear 036 Prima Stella public acceptance | -22.37 | 300.4 | high |
| `RINAMI-S14` | `RINAMI-D04` | Dear 037 explicit confession / lifelong production vow | -25.62 | 294.9 | high |

D03 and D04 acoustic proxies are preserved from R1 because the preferred and fallback audio elementary streams are identical. These windows include BGM, UI, effects, other speakers, and pauses; they corroborate only broad distinctions already grounded by text and direct inspection.

## 8. Reproducibility assets

The frozen package retains under `SUPPORTING_DATA/`:

- machine-readable source manifest and inventory TSV;
- source SHA-256 list;
- whole-mix song metrics JSON/TSV;
- sparse-frame visual metrics JSON/TSV, including R2 D03/D04 samples;
- selected mixed-scene prosody proxies JSON/TSV;
- textual-register metrics JSON/TSV.

Temporary decoded frames, contact sheets, and atlases are not current authority. They may be regenerated from the hashed sources.
