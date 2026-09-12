---
series: GKM
generation: V2
artifact_type: audiovisual_documentation
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
source_boundary: "AVE-FULL-20260910: 27 source recordings computationally processed; 565 sampled still points reviewed; no fresh direct listening or continuous-motion review. Earlier evidence generations retain their stated provenance."
last_updated: '2026-09-10'
---

> **Repository adoption — 2026-09-10.** This is the owner-requested branch revision of the exported rebuild. Pre-import candidate labels and repository-state statements in preserved records describe their original execution. Current analytical use remains bounded by the stated evidence modalities. The [import record](../../../10_RELEASE_MANIFEST_AND_ARCHIVE/GKM_AVE_FULL_REBUILD_IMPORT_20260910.md) identifies export hashes and repository transformations.

# Strict audio identity checks — AVE-FULL-20260910

The toolkit compares native decoded ordered float64 sample bytes, sample rate/count, known channel layout and canonical audio timing. It does not align songs, tolerate gain/codec differences, perform listening or test perceptual similarity. DIFFERENT means these whole recordings fail strict identity; it does not mean the musical passage sounds different. Equal titles and shared repertoire do not make these recordings equivalent or independent replications.

| A | B | Strict result | Native samples equal | Layout | Canonical timing equal | Timing tolerance s |
| --- | --- | --- | --- | --- | --- | --- |
| M10 | M11 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |
| M13 | M14 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |
| M15 | M16 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |
| M17 | M18 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |
| M20 | M25 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |
| H19 | M12 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |

## M10 / M11

```json
{
  "schema": "ave.audio_comparison.v1",
  "comparison_status": "DIFFERENT",
  "a": {
    "pcm_sha256": "3e6b2fb35340ffb245413d80d469e34819e05b5753e1de34659ededd6249929d",
    "pcm_bytes": 125992960,
    "sample_frames": 7874560,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 7874560,
        "source_start_seconds": 0.0,
        "source_end_seconds": 178.56145124716554
      }
    ],
    "source_sha256": "a88ad4fe405de061a3877d53cdbe238910e549a70bee1df9bbf0ef6039a73154",
    "stream_index": 1
  },
  "b": {
    "pcm_sha256": "68e6c05041b788cab305686a2ee1e5993c0d80df62736b41a7dfdcc38f2e5795",
    "pcm_bytes": 200376320,
    "sample_frames": 12523520,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 12523520,
        "source_start_seconds": 0.0,
        "source_end_seconds": 283.9800453514739
      }
    ],
    "source_sha256": "ebb51092cbbe799de4567f50e57a9b202e2c028983d1b3ad7d9c92c666cf9b61",
    "stream_index": 1
  },
  "native_decoded_samples_equal": false,
  "channel_layout_comparison": "MATCH",
  "canonical_timing_equal_within_source_granularity": false,
  "timing_tolerance_seconds": 2.2676736961451246e-05,
  "source_origins_equal": true,
  "encoded_packet_identity": "NOT_ESTABLISHED",
  "audiovisual_equivalence": "NOT_ESTABLISHED",
  "perceptual_review": "NOT_PERFORMED",
  "comparison_scope": "Native f64 decoded ordered samples, known channel layout and canonical audio timing; not matching video or narrative"
}
```

## M13 / M14

```json
{
  "schema": "ave.audio_comparison.v1",
  "comparison_status": "DIFFERENT",
  "a": {
    "pcm_sha256": "5bf3b6cc703460bde5d5d8960c7d58165b7e79857d3eb5498e6ae5d00eab5377",
    "pcm_bytes": 152797184,
    "sample_frames": 9549824,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 9549824,
        "source_start_seconds": 0.0,
        "source_end_seconds": 216.5492970521542
      }
    ],
    "source_sha256": "9bedc9ad49821d1d13e2d3b9f130f386d51ea5f06cc94ad7339ecf96b6e9c3cb",
    "stream_index": 1
  },
  "b": {
    "pcm_sha256": "1587bad83a00fbeaa928866120a3f165fe135a2a96f631defb968f3d51ab2b8c",
    "pcm_bytes": 215129088,
    "sample_frames": 13445568,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 13445568,
        "source_start_seconds": 0.0,
        "source_end_seconds": 304.8881632653061
      }
    ],
    "source_sha256": "a8ccbeab7e74f6103bfc30839772ef8956f1d0ab971cb4d8064c9bf79a661cc8",
    "stream_index": 1
  },
  "native_decoded_samples_equal": false,
  "channel_layout_comparison": "MATCH",
  "canonical_timing_equal_within_source_granularity": false,
  "timing_tolerance_seconds": 2.2676736961451246e-05,
  "source_origins_equal": true,
  "encoded_packet_identity": "NOT_ESTABLISHED",
  "audiovisual_equivalence": "NOT_ESTABLISHED",
  "perceptual_review": "NOT_PERFORMED",
  "comparison_scope": "Native f64 decoded ordered samples, known channel layout and canonical audio timing; not matching video or narrative"
}
```

## M15 / M16

```json
{
  "schema": "ave.audio_comparison.v1",
  "comparison_status": "DIFFERENT",
  "a": {
    "pcm_sha256": "4f2101c2aabbc5f6f5675e43abc9264784803dd542ecce5d1fd6483dfe5a5eb8",
    "pcm_bytes": 113639424,
    "sample_frames": 7102464,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 7102464,
        "source_start_seconds": 0.0,
        "source_end_seconds": 161.05360544217686
      }
    ],
    "source_sha256": "7a9f3b58287c9a663b591130d2d7cb7554b3be1915731262144f93c03644c7c6",
    "stream_index": 1
  },
  "b": {
    "pcm_sha256": "adf1ac2ca69aec1c1eca60765bee1008ce87e5dc0978fb5cfaaf185a075e0c59",
    "pcm_bytes": 150372352,
    "sample_frames": 9398272,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 9398272,
        "source_start_seconds": 0.0,
        "source_end_seconds": 213.11274376417234
      }
    ],
    "source_sha256": "40950da9822dbb2755d298200668fd42d52f6fddeba0122a6d6ce9f63de76f72",
    "stream_index": 1
  },
  "native_decoded_samples_equal": false,
  "channel_layout_comparison": "MATCH",
  "canonical_timing_equal_within_source_granularity": false,
  "timing_tolerance_seconds": 2.2676736961451246e-05,
  "source_origins_equal": true,
  "encoded_packet_identity": "NOT_ESTABLISHED",
  "audiovisual_equivalence": "NOT_ESTABLISHED",
  "perceptual_review": "NOT_PERFORMED",
  "comparison_scope": "Native f64 decoded ordered samples, known channel layout and canonical audio timing; not matching video or narrative"
}
```

## M17 / M18

```json
{
  "schema": "ave.audio_comparison.v1",
  "comparison_status": "DIFFERENT",
  "a": {
    "pcm_sha256": "8a575de9b7184c1b84ca68331b4d806125ef664cfa86c52fad090da1f1d11fca",
    "pcm_bytes": 142131200,
    "sample_frames": 8883200,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 8883200,
        "source_start_seconds": 0.0,
        "source_end_seconds": 201.4331065759637
      }
    ],
    "source_sha256": "f1143c1aaa2ca5df6c577c1b9d27c88cc19208e0c6218441455547a8e5130430",
    "stream_index": 1
  },
  "b": {
    "pcm_sha256": "873ccc7c2b00502cc0aa11d2adf615b8072d51db87d309b8b2d86ee39b32a180",
    "pcm_bytes": 169377792,
    "sample_frames": 10586112,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 10586112,
        "source_start_seconds": 0.0,
        "source_end_seconds": 240.04789115646258
      }
    ],
    "source_sha256": "d0ce84afef4bb91d1f20f15ecd02fe459f5a906cd6b64b9abda98e299f837fd6",
    "stream_index": 1
  },
  "native_decoded_samples_equal": false,
  "channel_layout_comparison": "MATCH",
  "canonical_timing_equal_within_source_granularity": false,
  "timing_tolerance_seconds": 2.2676736961451246e-05,
  "source_origins_equal": true,
  "encoded_packet_identity": "NOT_ESTABLISHED",
  "audiovisual_equivalence": "NOT_ESTABLISHED",
  "perceptual_review": "NOT_PERFORMED",
  "comparison_scope": "Native f64 decoded ordered samples, known channel layout and canonical audio timing; not matching video or narrative"
}
```

## M20 / M25

```json
{
  "schema": "ave.audio_comparison.v1",
  "comparison_status": "DIFFERENT",
  "a": {
    "pcm_sha256": "0dc6dd60be3f33f8483dc23d60a16479cf317b9262c92d91d20fd90dfa9e6ad4",
    "pcm_bytes": 116015104,
    "sample_frames": 7250944,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 7250944,
        "source_start_seconds": 0.0,
        "source_end_seconds": 164.42049886621317
      }
    ],
    "source_sha256": "05bfb52fef8398601a86d4db2920cdf8d4670ea2a6c739ece52336249aab0525",
    "stream_index": 1
  },
  "b": {
    "pcm_sha256": "fb7acbe1d2f691a17e88833237d62bddff5a773bb21d1483db54f70bc8dee169",
    "pcm_bytes": 108920832,
    "sample_frames": 6807552,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 6807552,
        "source_start_seconds": 0.0,
        "source_end_seconds": 154.36625850340135
      }
    ],
    "source_sha256": "97de00fe99a8bd1ba1b94cc367ad941e9714ff80f444e6bafad5e82e61904398",
    "stream_index": 1
  },
  "native_decoded_samples_equal": false,
  "channel_layout_comparison": "MATCH",
  "canonical_timing_equal_within_source_granularity": false,
  "timing_tolerance_seconds": 2.2676736961451246e-05,
  "source_origins_equal": true,
  "encoded_packet_identity": "NOT_ESTABLISHED",
  "audiovisual_equivalence": "NOT_ESTABLISHED",
  "perceptual_review": "NOT_PERFORMED",
  "comparison_scope": "Native f64 decoded ordered samples, known channel layout and canonical audio timing; not matching video or narrative"
}
```

## H19 / M12

```json
{
  "schema": "ave.audio_comparison.v1",
  "comparison_status": "DIFFERENT",
  "a": {
    "pcm_sha256": "08e4b5668af42c64628b2e756bdd4cad0cf9d9ed26fda1c6d6aaf8cd3160a31f",
    "pcm_bytes": 113410048,
    "sample_frames": 7088128,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 7088128,
        "source_start_seconds": 0.0,
        "source_end_seconds": 160.7285260770975
      }
    ],
    "source_sha256": "a692b45cc3ee31ff957c0199bae17c1c2f143c2271f3c1e19abf4d77a8e634ef",
    "stream_index": 1
  },
  "b": {
    "pcm_sha256": "3071fdec94accc5113e0ef6a5065a6b16465a05075fb2b055e715260c83b0f60",
    "pcm_bytes": 112803840,
    "sample_frames": 7050240,
    "sample_rate_hz": 44100,
    "channels": 2,
    "channel_layout": "stereo",
    "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
    "clock": "original_pts_minus_source_origin",
    "origin_seconds": 0.0,
    "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
    "max_timestamp_adjustment_seconds": 0.0,
    "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse",
    "segments": [
      {
        "sample_start": 0,
        "sample_end": 7050240,
        "source_start_seconds": 0.0,
        "source_end_seconds": 159.86938775510205
      }
    ],
    "source_sha256": "47bbe2204fa5f1a0bf2c371c8788c831b49a6c3b432af19ff233d639bafa0f82",
    "stream_index": 1
  },
  "native_decoded_samples_equal": false,
  "channel_layout_comparison": "MATCH",
  "canonical_timing_equal_within_source_granularity": false,
  "timing_tolerance_seconds": 2.2676736961451246e-05,
  "source_origins_equal": true,
  "encoded_packet_identity": "NOT_ESTABLISHED",
  "audiovisual_equivalence": "NOT_ESTABLISHED",
  "perceptual_review": "NOT_PERFORMED",
  "comparison_scope": "Native f64 decoded ordered samples, known channel layout and canonical audio timing; not matching video or narrative"
}
```
