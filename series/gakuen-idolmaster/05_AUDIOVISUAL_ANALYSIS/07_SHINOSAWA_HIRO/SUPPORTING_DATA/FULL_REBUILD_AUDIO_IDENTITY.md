---
series: GKM
generation: V2
artifact_type: audiovisual_documentation
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
source_boundary: "AVE-FULL-20260910: 33 source recordings computationally processed; 636 sampled still points reviewed; no fresh direct listening or continuous-motion review. Earlier evidence generations retain their stated provenance."
last_updated: '2026-09-10'
---

> **Repository adoption — 2026-09-10.** This is the owner-requested branch revision of the exported rebuild. Pre-import candidate labels and repository-state statements in preserved records describe their original execution. Current analytical use remains bounded by the stated evidence modalities. The [import record](../../../10_RELEASE_MANIFEST_AND_ARCHIVE/GKM_AVE_FULL_REBUILD_IMPORT_20260910.md) identifies export hashes and repository transformations.

# Strict audio identity checks — AVE-FULL-20260910

The toolkit compares native decoded ordered float64 sample bytes, sample rate/count, known channel layout and canonical audio timing. It does not align songs, tolerate gain/codec differences, perform listening or test perceptual similarity. DIFFERENT means these whole recordings fail strict identity; it does not mean the musical passage sounds different. Equal titles and shared repertoire do not make these recordings equivalent or independent replications.

| A | B | Strict result | Native samples equal | Layout | Canonical timing equal | Timing tolerance s |
| --- | --- | --- | --- | --- | --- | --- |
| H12 | H14 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |
| H15 | H16 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |
| H17 | H18 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |
| H28 | H29 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |
| H32 | H33 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |
| H19 | M12 | DIFFERENT | false | MATCH | false | 2.26767369614512e-05 |

## H04 retained passage and WAV preservation

Both materializations were independently clipped at original source seconds [3160, 3205). Each WAV has its own source-to-derivative sample mapping and internal native-sample preservation verification. The resulting derivative clocks span [0, 45). A strict comparison of these WAVs tests the same retained passage; it does not assert whole-object equality. The full original extends beyond the historical trim, so its whole-source population remains different. Prior complete retained encoded-packet prefix equality is carried forward as historical verification.

```json
{
  "strict_bounded_comparison": {
    "schema": "ave.audio_comparison.v1",
    "comparison_status": "MATCH",
    "a": {
      "pcm_sha256": "e358fa9c06a60961b4da1325772122f45ddbe08c065b62603ab77ea9a1ab9684",
      "pcm_bytes": 31752000,
      "sample_frames": 1984500,
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
          "sample_end": 1984500,
          "source_start_seconds": 0.0,
          "source_end_seconds": 45.0
        }
      ],
      "source_sha256": "2d5d1f87367d3f87f8da02d2d2544a3f38a1b6354b6a29a58f197e45f0f0b5c8",
      "stream_index": 0
    },
    "b": {
      "pcm_sha256": "e358fa9c06a60961b4da1325772122f45ddbe08c065b62603ab77ea9a1ab9684",
      "pcm_bytes": 31752000,
      "sample_frames": 1984500,
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
          "sample_end": 1984500,
          "source_start_seconds": 0.0,
          "source_end_seconds": 45.0
        }
      ],
      "source_sha256": "2d5d1f87367d3f87f8da02d2d2544a3f38a1b6354b6a29a58f197e45f0f0b5c8",
      "stream_index": 0
    },
    "native_decoded_samples_equal": true,
    "channel_layout_comparison": "MATCH",
    "canonical_timing_equal_within_source_granularity": true,
    "timing_tolerance_seconds": 2.2676736961451246e-05,
    "source_origins_equal": true,
    "encoded_packet_identity": "NOT_ESTABLISHED",
    "audiovisual_equivalence": "NOT_ESTABLISHED",
    "perceptual_review": "NOT_PERFORMED",
    "comparison_scope": "Native f64 decoded ordered samples, known channel layout and canonical audio timing; not matching video or narrative"
  },
  "source_to_WAV_records": [
    {
      "schema": "ave.audio.v1",
      "parent_source_sha256": "4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468",
      "parent_stream_index": 1,
      "clock": "original_pts_minus_source_origin",
      "origin_seconds": 0.0,
      "artifact_path": "audio.wav",
      "artifact_sha256": "2d5d1f87367d3f87f8da02d2d2544a3f38a1b6354b6a29a58f197e45f0f0b5c8",
      "derivative_stream_index": 0,
      "identity": {
        "pcm_sha256": "e358fa9c06a60961b4da1325772122f45ddbe08c065b62603ab77ea9a1ab9684",
        "pcm_bytes": 31752000,
        "sample_frames": 1984500,
        "sample_rate_hz": 44100,
        "channels": 2,
        "channel_layout": "stereo",
        "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
        "clock": "original_pts_minus_source_origin",
        "origin_seconds": 0.0,
        "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
        "max_timestamp_adjustment_seconds": 0.0,
        "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse"
      },
      "segments": [
        {
          "sample_start": 0,
          "sample_end": 1984500,
          "source_start_seconds": 3160.0,
          "source_end_seconds": 3205.0,
          "sample_rate_hz": 44100,
          "parent_source_sha256": "4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468",
          "parent_stream_index": 1
        }
      ],
      "review_mapping": {
        "modality": "audio",
        "artifact_kind": "audio_clip",
        "artifact_path": "audio.wav",
        "artifact_sha256": "2d5d1f87367d3f87f8da02d2d2544a3f38a1b6354b6a29a58f197e45f0f0b5c8",
        "derivative_stream_index": 0,
        "parent_source_sha256": "4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468",
        "parent_stream_index": 1,
        "clock": "original_pts_minus_source_origin",
        "origin_seconds": 0.0,
        "segments": [
          {
            "parent_start_seconds": 3160.0,
            "parent_end_seconds": 3205.0,
            "derivative_start_seconds": 0.0,
            "derivative_end_seconds": 45.0
          }
        ],
        "parent_start_seconds": 3160.0,
        "parent_end_seconds": 3205.0,
        "derivative_start_seconds": 0.0,
        "derivative_end_seconds": 45.0
      },
      "sample_preservation_verified": true,
      "artifact_channel_layout": "stereo",
      "channel_layout_preservation": "MATCH",
      "wav_layout_policy": "Known mono/stereo native f64 WAV exports use WAVEFORMATEXTENSIBLE masks; source-unknown layouts are not inferred from channel count; exact decoded sample/layout checks still apply",
      "selection": {
        "status": "COMPLETE",
        "requested_start_seconds": 3160.0,
        "requested_end_seconds": 3205.0,
        "covered_seconds": 45.0,
        "missing_seconds": 0.0,
        "parts": [
          {
            "input_sample_start": 139356000,
            "input_sample_end": 141340500,
            "source_start_seconds": 3160.0,
            "source_end_seconds": 3205.0
          }
        ],
        "boundary_rounding": "Sample onsets in the half-open interval; both endpoint indices use ceil",
        "requested_unpadded": {
          "status": "COMPLETE",
          "requested_start_seconds": 3160.0,
          "requested_end_seconds": 3205.0,
          "covered_seconds": 45.0,
          "missing_seconds": 0.0,
          "parts": [
            {
              "input_sample_start": 139356000,
              "input_sample_end": 141340500,
              "source_start_seconds": 3160.0,
              "source_end_seconds": 3205.0
            }
          ],
          "boundary_rounding": "Sample onsets in the half-open interval; both endpoint indices use ceil"
        }
      },
      "storage_policy": "PCM sample indices are compact; source gaps/delays remain explicit in the mapping, never assumed to be silence",
      "perceptual_review": "NOT_PERFORMED",
      "av_synchronization_verified": false
    },
    {
      "schema": "ave.audio.v1",
      "parent_source_sha256": "de92afafb3181342407ab9405f4951e820bfdafaad5b1e9538ec9d7f73ea826e",
      "parent_stream_index": 1,
      "clock": "original_pts_minus_source_origin",
      "origin_seconds": 0.0,
      "artifact_path": "audio.wav",
      "artifact_sha256": "2d5d1f87367d3f87f8da02d2d2544a3f38a1b6354b6a29a58f197e45f0f0b5c8",
      "derivative_stream_index": 0,
      "identity": {
        "pcm_sha256": "e358fa9c06a60961b4da1325772122f45ddbe08c065b62603ab77ea9a1ab9684",
        "pcm_bytes": 31752000,
        "sample_frames": 1984500,
        "sample_rate_hz": 44100,
        "channels": 2,
        "channel_layout": "stereo",
        "encoding": "f64le interleaved native rate and channel order; no normalization or downmix",
        "clock": "original_pts_minus_source_origin",
        "origin_seconds": 0.0,
        "timestamp_quantization_tolerance_seconds": 2.2676736961451246e-05,
        "max_timestamp_adjustment_seconds": 0.0,
        "timestamp_policy": "Contiguous samples within one source time-base tick are joined; larger gaps remain explicit; larger overlaps refuse"
      },
      "segments": [
        {
          "sample_start": 0,
          "sample_end": 1984500,
          "source_start_seconds": 3160.0,
          "source_end_seconds": 3205.0,
          "sample_rate_hz": 44100,
          "parent_source_sha256": "de92afafb3181342407ab9405f4951e820bfdafaad5b1e9538ec9d7f73ea826e",
          "parent_stream_index": 1
        }
      ],
      "review_mapping": {
        "modality": "audio",
        "artifact_kind": "audio_clip",
        "artifact_path": "audio.wav",
        "artifact_sha256": "2d5d1f87367d3f87f8da02d2d2544a3f38a1b6354b6a29a58f197e45f0f0b5c8",
        "derivative_stream_index": 0,
        "parent_source_sha256": "de92afafb3181342407ab9405f4951e820bfdafaad5b1e9538ec9d7f73ea826e",
        "parent_stream_index": 1,
        "clock": "original_pts_minus_source_origin",
        "origin_seconds": 0.0,
        "segments": [
          {
            "parent_start_seconds": 3160.0,
            "parent_end_seconds": 3205.0,
            "derivative_start_seconds": 0.0,
            "derivative_end_seconds": 45.0
          }
        ],
        "parent_start_seconds": 3160.0,
        "parent_end_seconds": 3205.0,
        "derivative_start_seconds": 0.0,
        "derivative_end_seconds": 45.0
      },
      "sample_preservation_verified": true,
      "artifact_channel_layout": "stereo",
      "channel_layout_preservation": "MATCH",
      "wav_layout_policy": "Known mono/stereo native f64 WAV exports use WAVEFORMATEXTENSIBLE masks; source-unknown layouts are not inferred from channel count; exact decoded sample/layout checks still apply",
      "selection": {
        "status": "COMPLETE",
        "requested_start_seconds": 3160.0,
        "requested_end_seconds": 3205.0,
        "covered_seconds": 45.0,
        "missing_seconds": 0.0,
        "parts": [
          {
            "input_sample_start": 139356000,
            "input_sample_end": 141340500,
            "source_start_seconds": 3160.0,
            "source_end_seconds": 3205.0
          }
        ],
        "boundary_rounding": "Sample onsets in the half-open interval; both endpoint indices use ceil",
        "requested_unpadded": {
          "status": "COMPLETE",
          "requested_start_seconds": 3160.0,
          "requested_end_seconds": 3205.0,
          "covered_seconds": 45.0,
          "missing_seconds": 0.0,
          "parts": [
            {
              "input_sample_start": 139356000,
              "input_sample_end": 141340500,
              "source_start_seconds": 3160.0,
              "source_end_seconds": 3205.0
            }
          ],
          "boundary_rounding": "Sample onsets in the half-open interval; both endpoint indices use ceil"
        }
      },
      "storage_policy": "PCM sample indices are compact; source gaps/delays remain explicit in the mapping, never assumed to be silence",
      "perceptual_review": "NOT_PERFORMED",
      "av_synchronization_verified": false
    }
  ]
}
```

## H12 / H14

```json
{
  "schema": "ave.audio_comparison.v1",
  "comparison_status": "DIFFERENT",
  "a": {
    "pcm_sha256": "9518fd6d7cb3662fb1aee3504ee6c85a3dcbd960dc1c4ea595e7f7ed0b3002fd",
    "pcm_bytes": 123666432,
    "sample_frames": 7729152,
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
        "sample_end": 7729152,
        "source_start_seconds": 0.0,
        "source_end_seconds": 175.26421768707482
      }
    ],
    "source_sha256": "346649b3c41f8cf987125c344e09d29f1818187240132acfbc5eed89d854462c",
    "stream_index": 1
  },
  "b": {
    "pcm_sha256": "3e59b2ed8312ad9103150f7403cbea9f89cc625b5030ae55a7a7ca018fde3aa2",
    "pcm_bytes": 191873024,
    "sample_frames": 11992064,
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
        "sample_end": 11992064,
        "source_start_seconds": 0.0,
        "source_end_seconds": 271.9288888888889
      }
    ],
    "source_sha256": "ff7023355616a3f1f40328f8e899e6805b899919bfff67b1ead1578100ceccc6",
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

## H15 / H16

```json
{
  "schema": "ave.audio_comparison.v1",
  "comparison_status": "DIFFERENT",
  "a": {
    "pcm_sha256": "bdcaf13fb393637208915c3e07207d53af2fd1d8ab8da506ed4add037cb16ea6",
    "pcm_bytes": 141672448,
    "sample_frames": 8854528,
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
        "sample_end": 8854528,
        "source_start_seconds": 0.0,
        "source_end_seconds": 200.78294784580498
      }
    ],
    "source_sha256": "ea62087e203b892295f6bb27f68426779b1d0c37ceb83c522977942e1c7bf2aa",
    "stream_index": 1
  },
  "b": {
    "pcm_sha256": "a06aef0fb95faba3575702a1e35a3b8cbb12de7d8cd8982fbbb3b5f8e16c639e",
    "pcm_bytes": 153476096,
    "sample_frames": 9592256,
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
        "sample_end": 9592256,
        "source_start_seconds": 0.0,
        "source_end_seconds": 217.5114739229025
      }
    ],
    "source_sha256": "4c1188dac2851da6d2a945ca3690fd95f1012b7cdf46d0a2c65f4084737b6d68",
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

## H17 / H18

```json
{
  "schema": "ave.audio_comparison.v1",
  "comparison_status": "DIFFERENT",
  "a": {
    "pcm_sha256": "db9b89a142dff1bdcee2b9f12d7ba7a104755e30444ddd7ebe2f4b40070db3b7",
    "pcm_bytes": 129318912,
    "sample_frames": 8082432,
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
        "sample_end": 8082432,
        "source_start_seconds": 0.0,
        "source_end_seconds": 183.27510204081634
      }
    ],
    "source_sha256": "be3709652b63a93a30bba202dc06296169262af269b84b77109335d65e5bd8cd",
    "stream_index": 1
  },
  "b": {
    "pcm_sha256": "9b7ee02e15478e9c552e343dd083c066ce14a10b2fc01b95c816b264d997a63e",
    "pcm_bytes": 147685376,
    "sample_frames": 9230336,
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
        "sample_end": 9230336,
        "source_start_seconds": 0.0,
        "source_end_seconds": 209.30467120181405
      }
    ],
    "source_sha256": "1e3bffcab0e7d0131eda8875e22c5d421570050612f2606751944d6d9d1f9292",
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

## H28 / H29

```json
{
  "schema": "ave.audio_comparison.v1",
  "comparison_status": "DIFFERENT",
  "a": {
    "pcm_sha256": "1b5f09e810cb89f3ba43d96e78b00ccfc81465432378f4da79ad4f07fc369e82",
    "pcm_bytes": 109019136,
    "sample_frames": 6813696,
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
        "sample_end": 6813696,
        "source_start_seconds": 0.0,
        "source_end_seconds": 154.5055782312925
      }
    ],
    "source_sha256": "938bfd03b2b0c613425875cc8ab6cf27ea95e776b69dc6c31e4e76da6f3ffc91",
    "stream_index": 1
  },
  "b": {
    "pcm_sha256": "41c41dba787f3eaf88af18019c3ba660602249f90b00799f0492422eaa769667",
    "pcm_bytes": 144883712,
    "sample_frames": 9055232,
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
        "sample_end": 9055232,
        "source_start_seconds": 0.0,
        "source_end_seconds": 205.3340589569161
      }
    ],
    "source_sha256": "d65297b2725bc3216ae071773e83b698bbabdb785a2b56b279485f1d4be291ef",
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

## H32 / H33

```json
{
  "schema": "ave.audio_comparison.v1",
  "comparison_status": "DIFFERENT",
  "a": {
    "pcm_sha256": "e7eac80a546d833f0768474240115f932f48e65d106e900fdd9b15b197fde921",
    "pcm_bytes": 107347968,
    "sample_frames": 6709248,
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
        "sample_end": 6709248,
        "source_start_seconds": 0.0,
        "source_end_seconds": 152.13714285714286
      }
    ],
    "source_sha256": "75d8ede001bf0ba7fc78938a80fdede712237073eea20a6647b896cdcb5475ff",
    "stream_index": 1
  },
  "b": {
    "pcm_sha256": "18c270e14f80ec477fade19295a4478e3d628027537258259bfa8d2e642448b5",
    "pcm_bytes": 138927104,
    "sample_frames": 8682944,
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
        "sample_end": 8682944,
        "source_start_seconds": 0.0,
        "source_end_seconds": 196.89215419501133
      }
    ],
    "source_sha256": "f294b9bb1c3c1ab3113d2e96c038d3e7b3e584287b4e3180a66d18d01677da32",
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
