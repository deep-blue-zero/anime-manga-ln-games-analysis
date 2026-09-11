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

> **Public repository representation.** Machine-specific paths use `WORKSPACE/`, `LOCAL_USER/` or `LOCAL_DRIVE_*` placeholders; configure these roots before reproduction. Direct Drive URLs are represented by source-object IDs. Original execution hashes and exported-byte claims identify the archived originals; public code/data snippets containing these substitutions are explicitly derivatives. The import manifest records their final repository hashes and decoded payload hashes.


> **Repository adoption — 2026-09-10.** This is the owner-requested branch revision of the exported rebuild. Pre-import candidate labels and repository-state statements in preserved records describe their original execution. Current analytical use remains bounded by the stated evidence modalities. The [import record](../../../10_RELEASE_MANIFEST_AND_ARCHIVE/GKM_AVE_FULL_REBUILD_IMPORT_20260910.md) identifies export hashes and repository transformations.

# Methods and reproduction — AVE-FULL-20260910

Toolkit: AV Evidence Toolkit 1.0.0 plus the separately tested native mono/stereo WAV layout patch from the targeted trial. The original 1.0.0 ZIP is unchanged. This revision uses explicit execution adapters for Windows binaries, bounded decoder threads, longer timeouts, verified frame-index reuse, and batch chapter selections. The source measurement formulas remain those of the frozen toolkit; batch selection is separately auditable.

The audio patch preserves known mono/stereo layout in WAVEFORMATEXTENSIBLE without changing PCM payload bytes; unknown layouts stay unknown. It does not add direct listening, voice separation or continuous video perception. The isolated copied suite passed 98 tests on Windows. Linux execution was not repeated.

## Runtime and implementation hashes

```json
{
  "tool_version": "1.0.0",
  "python": "3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]",
  "platform": "Windows-11-10.0.26200-SP0",
  "programs": {
    "ffmpeg": {
      "path": "LOCAL_DRIVE_C\\ProgramData\\chocolatey\\lib\\ffmpeg\\tools\\ffmpeg\\bin\\ffmpeg.EXE",
      "version": "ffmpeg version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers"
    },
    "ffprobe": {
      "path": "LOCAL_DRIVE_C\\ProgramData\\chocolatey\\lib\\ffmpeg\\tools\\ffmpeg\\bin\\ffprobe.EXE",
      "version": "ffprobe version 8.1.1-essentials_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers"
    }
  },
  "packages": {
    "Pillow": "12.2.0",
    "numpy": "2.1.2",
    "soundfile": "0.14.0",
    "librosa": "1.0.0"
  },
  "implementation_sha256": {
    "__init__.py": "a8e8920a4d7ae51a392f7d17d082b7e99015d04317bcd46d84d9208ea371d65a",
    "__main__.py": "935a1c1166b0c1ea35a82256345000bf2c73ded718d77773bc27a71ecce28f7d",
    "audio.py": "7af497132250d3414620525efdf9700d703fab7d2a2388ab6995772887ee7efb",
    "bundle.py": "f14e89ba88451fd254af1368ee50f2f62a9a132bd243af26c761a7200d66539a",
    "cli.py": "6b18397ad979210e8a10780371a960a3f13f528774cc706cb7029e429b521fb0",
    "clips.py": "bbbfcde239f088d21b570d9646f74d91d223a30957909e7dd7770b9217eda550",
    "common.py": "82245b3e182a023ba880c1d90a2fe72cfc91834a19450ec2f4a0863215dab923",
    "inventory.py": "d5f9d404597b73a9a43046930e6b8d5b3bbb09688a96c41fb05a5b9085d1bd02",
    "packaging.py": "fbf100c66e2b802117d47c8b48f8b28adeb6a155411bc9dfddcb4b1bfe7bedd5",
    "reviews.py": "d6bb89d786d12d9c3ad4f512c168c4ce84e4a16749370d241a84e88c7bcbe286",
    "subtitles.py": "34cc46074764e49127db0d4b2fb589b593ef8700949bd18617c54e2ce053c26d",
    "timeline.py": "4237371db68885fc905d0ab5e947d1c67140e5964e64839f3d7429626d7e8f5d",
    "visual.py": "9c6fb339130d67b8202af1c03e39e16ad42c3c52bff1de056bf0a1ce915de51e"
  },
  "perceptual_capabilities": {
    "audio": "NOT_VERIFIED",
    "motion": "NOT_VERIFIED",
    "images": "NOT_VERIFIED"
  }
}
```

## Scope and clocks

All original source IDs, expected input hashes and exact selected streams are retained below. Current preferred H04 is the full original. File paths are acquisition locations and may be replaced during reproduction only with objects of the exact recorded hash. Toolkit admission verifies the bytes again. Every run records command arguments/results, source identity, parameters, output hashes and environment; immutable runs are verified before reuse.

Whole-source audio uses the actual first-to-last decoded sample interval, not a guessed video duration. Native sample count/rate/channel order are preserved. Missing timestamp regions remain explicit. Native PCM is float64; source files are never normalized or overwritten. Caption/analysis interval source binding proves the coordinate system, not an audible speaker or transcript correctness. All new feature F0 is NOT_REQUESTED.

Survey frames: 12 stratum-center requests per source; targeted frames: declared comparison plans. Full source-frame PTS indexing verifies geometry and monotonic timestamps. Exact mode selects the first frame at/after each request, which matters for 60000/1001 fps material. Requested and actual times remain separate. Targeted execution reuses the full survey index by its run and command-record hashes, then selects original PTS after seeking; actual selected PTS must match. Index reuse is explicitly journaled, not a second decoding pass. No HDR conversion, arbitrary rotation or unsupported geometry repair is silently introduced.

Perceptual accounting separates prepared outputs, actual displayed images, authored observations, inherited findings and unavailable modalities. Image tool response files verify presentation artifacts; they do not prove every interpretation. Viewing contact sheets provides sampled still observations, never interval-duration motion coverage. No direct listening or continuous playback is certified in this revision.

## Reproduction inputs

Save the following list as this character’s corpus input. For the joint scripts below, concatenate the two character lists into evidence/corpus.json. The duration_seconds/prior_probe fields are inherited acquisition metadata used to choose nominal survey requests; fresh admission and decoded sample bounds, recorded elsewhere, govern interpretation.

```json
[
  {
    "alias": "M01",
    "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
    "character": "MISUZU",
    "role": "Dear 001-010 acting spine",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "bytes": 116784561,
    "duration_seconds": 2917.958821,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "Main",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.4d401f",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 31,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "30/1",
          "avg_frame_rate": "30/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 44818944,
          "duration": "2917.900000",
          "bit_rate": "180317",
          "bits_per_raw_sample": "8",
          "nb_frames": "87537",
          "extradata_size": 43,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 128681984,
          "duration": "2917.958821",
          "bit_rate": "127999",
          "nb_frames": "125666",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 262616294,
          "duration": "2917.958822",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "2917.958821",
        "size": "116784561",
        "bit_rate": "320181",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】",
          "artist": "学マスコミュ保管委員会",
          "genre": "Gaming",
          "date": "20250516",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=18Eb02aeTH0",
          "description": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n↓再生リスト\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh\n\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス",
          "synopsis": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n↓再生リスト\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh\n\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス"
        }
      }
    }
  },
  {
    "alias": "M02",
    "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
    "character": "MISUZU",
    "role": "Dear 011-020 / N.I.A. and Rinha conflict",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
    "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
    "bytes": 235227290,
    "duration_seconds": 2991.240998,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "Main",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.4d4020",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 32,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 45944576,
          "duration": "2991.183333",
          "bit_rate": "485879",
          "bits_per_raw_sample": "8",
          "nb_frames": "179471",
          "extradata_size": 43,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 131913728,
          "duration": "2991.240998",
          "bit_rate": "127999",
          "nb_frames": "128822",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "bin_data",
          "codec_long_name": "binary data",
          "codec_type": "data",
          "codec_tag_string": "text",
          "codec_tag": "0x74786574",
          "id": "0x3",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/1000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2991000,
          "duration": "2991.000000",
          "nb_frames": "11",
          "extradata_size": 43,
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "eng",
            "handler_name": "SubtitleHandler"
          }
        },
        {
          "index": 3,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 269211690,
          "duration": "2991.241000",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [
        {
          "id": 0,
          "time_base": "1/1000",
          "start": 0,
          "start_time": "0.000000",
          "end": 242000,
          "end_time": "242.000000",
          "tags": {
            "title": "11話"
          }
        },
        {
          "id": 1,
          "time_base": "1/1000",
          "start": 242000,
          "start_time": "242.000000",
          "end": 536000,
          "end_time": "536.000000",
          "tags": {
            "title": "12話"
          }
        },
        {
          "id": 2,
          "time_base": "1/1000",
          "start": 536000,
          "start_time": "536.000000",
          "end": 738000,
          "end_time": "738.000000",
          "tags": {
            "title": "13話"
          }
        },
        {
          "id": 3,
          "time_base": "1/1000",
          "start": 738000,
          "start_time": "738.000000",
          "end": 991000,
          "end_time": "991.000000",
          "tags": {
            "title": "14話"
          }
        },
        {
          "id": 4,
          "time_base": "1/1000",
          "start": 991000,
          "start_time": "991.000000",
          "end": 1226000,
          "end_time": "1226.000000",
          "tags": {
            "title": "15話"
          }
        },
        {
          "id": 5,
          "time_base": "1/1000",
          "start": 1226000,
          "start_time": "1226.000000",
          "end": 1634000,
          "end_time": "1634.000000",
          "tags": {
            "title": "16話"
          }
        },
        {
          "id": 6,
          "time_base": "1/1000",
          "start": 1634000,
          "start_time": "1634.000000",
          "end": 1987000,
          "end_time": "1987.000000",
          "tags": {
            "title": "17話"
          }
        },
        {
          "id": 7,
          "time_base": "1/1000",
          "start": 1987000,
          "start_time": "1987.000000",
          "end": 2177000,
          "end_time": "2177.000000",
          "tags": {
            "title": "18話"
          }
        },
        {
          "id": 8,
          "time_base": "1/1000",
          "start": 2177000,
          "start_time": "2177.000000",
          "end": 2428000,
          "end_time": "2428.000000",
          "tags": {
            "title": "19話"
          }
        },
        {
          "id": 9,
          "time_base": "1/1000",
          "start": 2428000,
          "start_time": "2428.000000",
          "end": 2791000,
          "end_time": "2791.000000",
          "tags": {
            "title": "20話"
          }
        },
        {
          "id": 10,
          "time_base": "1/1000",
          "start": 2791000,
          "start_time": "2791.000000",
          "end": 2991000,
          "end_time": "2991.000000",
          "tags": {
            "title": "ED"
          }
        }
      ],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
        "nb_streams": 4,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "2991.240998",
        "size": "235227290",
        "bit_rate": "629109",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20250630",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=tSpN7L8MlcQ",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n【コミュ一覧】\n11話～ 0:00\n12話～ 4:02\n13話～ 8:56\n14話～ 12:18\n15話～ 16:31\n16話～ 20:26\n17話～ 27:14\n18話～ 33:07\n19話～ 36:17\n20話～ 40:28\nED～ 46:31\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n【コミュ一覧】\n11話～ 0:00\n12話～ 4:02\n13話～ 8:56\n14話～ 12:18\n15話～ 16:31\n16話～ 20:26\n17話～ 27:14\n18話～ 33:07\n19話～ 36:17\n20話～ 40:28\nED～ 46:31\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴"
        }
      }
    }
  },
  {
    "alias": "M03",
    "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
    "character": "MISUZU",
    "role": "Dear 021-027 / STEP3 and summer H.I.F.",
    "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
    "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
    "bytes": 296707894,
    "duration_seconds": 2835.0,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "Main",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.4d4020",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 32,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60000/1001",
          "avg_frame_rate": "60000/1001",
          "time_base": "1/60000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 170067898,
          "duration": "2834.464967",
          "bit_rate": "692287",
          "bits_per_raw_sample": "8",
          "nb_frames": "169898",
          "extradata_size": 42,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 125002752,
          "duration": "2834.529524",
          "bit_rate": "127999",
          "nb_frames": "122073",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "bin_data",
          "codec_long_name": "binary data",
          "codec_type": "data",
          "codec_tag_string": "text",
          "codec_tag": "0x74786574",
          "id": "0x3",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/1000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2835000,
          "duration": "2835.000000",
          "nb_frames": "8",
          "extradata_size": 43,
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "eng",
            "handler_name": "SubtitleHandler"
          }
        },
        {
          "index": 3,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 255150000,
          "duration": "2835.000000",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [
        {
          "id": 0,
          "time_base": "1/1000",
          "start": 0,
          "start_time": "0.000000",
          "end": 310000,
          "end_time": "310.000000",
          "tags": {
            "title": "親愛度コミュ21話"
          }
        },
        {
          "id": 1,
          "time_base": "1/1000",
          "start": 310000,
          "start_time": "310.000000",
          "end": 632000,
          "end_time": "632.000000",
          "tags": {
            "title": "親愛度コミュ22話"
          }
        },
        {
          "id": 2,
          "time_base": "1/1000",
          "start": 632000,
          "start_time": "632.000000",
          "end": 943000,
          "end_time": "943.000000",
          "tags": {
            "title": "親愛度コミュ23話"
          }
        },
        {
          "id": 3,
          "time_base": "1/1000",
          "start": 943000,
          "start_time": "943.000000",
          "end": 1393000,
          "end_time": "1393.000000",
          "tags": {
            "title": "親愛度コミュ24話"
          }
        },
        {
          "id": 4,
          "time_base": "1/1000",
          "start": 1393000,
          "start_time": "1393.000000",
          "end": 1770000,
          "end_time": "1770.000000",
          "tags": {
            "title": "親愛度コミュ25話"
          }
        },
        {
          "id": 5,
          "time_base": "1/1000",
          "start": 1770000,
          "start_time": "1770.000000",
          "end": 2135000,
          "end_time": "2135.000000",
          "tags": {
            "title": "親愛度コミュ26話"
          }
        },
        {
          "id": 6,
          "time_base": "1/1000",
          "start": 2135000,
          "start_time": "2135.000000",
          "end": 2651000,
          "end_time": "2651.000000",
          "tags": {
            "title": "親愛度コミュ27話"
          }
        },
        {
          "id": 7,
          "time_base": "1/1000",
          "start": 2651000,
          "start_time": "2651.000000",
          "end": 2835000,
          "end_time": "2835.000000",
          "tags": {
            "title": "ED"
          }
        }
      ],
      "format": {
        "filename": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
        "nb_streams": 4,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "2835.000000",
        "size": "296707894",
        "bit_rate": "837270",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【学マス】 秦谷美鈴  親愛度コミュ21～27話まとめ【STEP3】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20260429",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=wt77y0MHvVU",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n【動画内容】\n親愛度コミュ21話 0:00～\n親愛度コミュ22話 5:10～\n親愛度コミュ23話 10:32～\n親愛度コミュ24話 15:43～\n親愛度コミュ25話 23:13～\n親愛度コミュ26話 29:30～\n親愛度コミュ27話 35:35～\nED 44:11～\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n【動画内容】\n親愛度コミュ21話 0:00～\n親愛度コミュ22話 5:10～\n親愛度コミュ23話 10:32～\n親愛度コミュ24話 15:43～\n親愛度コミュ25話 23:13～\n親愛度コミュ26話 29:30～\n親愛度コミュ27話 35:35～\nED 44:11～\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴"
        }
      }
    }
  },
  {
    "alias": "M04",
    "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
    "character": "MISUZU",
    "role": "Dear 028-037 / STEP4 and winter H.I.F.",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
    "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "bytes": 193460076,
    "duration_seconds": 4048.631293,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "Main",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.4d401f",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 31,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "30/1",
          "avg_frame_rate": "30/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 62185984,
          "duration": "4048.566667",
          "bit_rate": "243484",
          "bits_per_raw_sample": "8",
          "nb_frames": "121457",
          "extradata_size": 43,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 178544640,
          "duration": "4048.631293",
          "bit_rate": "127999",
          "nb_frames": "174360",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 364376816,
          "duration": "4048.631289",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "4048.631293",
        "size": "193460076",
        "bit_rate": "382272",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】",
          "artist": "学マスコミュ保管委員会",
          "genre": "Gaming",
          "date": "20260516",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=Loj480JIDkI",
          "description": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n↓再生リスト\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh\n\n\n#学園アイドルマスター #学マス",
          "synopsis": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n↓再生リスト\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh\n\n\n#学園アイドルマスター #学マス"
        }
      }
    }
  },
  {
    "alias": "M05",
    "logical_source_id": "1zLIbXE_fU7Me1O3SiDs7GE0nKwRms7zz",
    "character": "MISUZU",
    "role": "Tsuki no Kame song communication",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【ツキノカメ】秦谷美鈴 楽曲コミュまとめ【学マス】-(1080p60).mp4",
    "sha256": "dc76e5fcf5f1e0057424a37e86e7503d26b2ae18607ab029823b090e35f7589d",
    "bytes": 80962522,
    "duration_seconds": 372.912472,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "dc76e5fcf5f1e0057424a37e86e7503d26b2ae18607ab029823b090e35f7589d",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 5726976,
          "duration": "372.850000",
          "bit_rate": "1562516",
          "bits_per_raw_sample": "8",
          "nb_frames": "22371",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 16445440,
          "duration": "372.912472",
          "bit_rate": "128010",
          "nb_frames": "16060",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 33562122,
          "duration": "372.912467",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【ツキノカメ】秦谷美鈴 楽曲コミュまとめ【学マス】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "372.912472",
        "size": "80962522",
        "bit_rate": "1736869",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【ツキノカメ】秦谷美鈴 楽曲コミュまとめ【学マス】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20250516",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=QE6l5TmVZ6Y",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#学園アイドルマスター",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#学園アイドルマスター"
        }
      }
    }
  },
  {
    "alias": "M06",
    "logical_source_id": "1-MzZgO0DWfS-6F6QzyxB8-jVU00MLf2g",
    "character": "MISUZU",
    "role": "Campus mode song communication",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【Campus mode!!】秦谷美鈴 楽曲コミュまとめ【学マス】-(1080p60).mp4",
    "sha256": "bef614ac4b674565522caeec2f4e6e63e3e18e460aae3a1e182df5381c99d4df",
    "bytes": 55694480,
    "duration_seconds": 612.704943,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "bef614ac4b674565522caeec2f4e6e63e3e18e460aae3a1e182df5381c99d4df",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 9410048,
          "duration": "612.633333",
          "bit_rate": "565545",
          "bits_per_raw_sample": "8",
          "nb_frames": "36758",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 27020288,
          "duration": "612.704943",
          "bit_rate": "128005",
          "nb_frames": "26387",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 55143445,
          "duration": "612.704944",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【Campus mode!!】秦谷美鈴 楽曲コミュまとめ【学マス】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "612.704943",
        "size": "55694480",
        "bit_rate": "727194",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【Campus mode!!】秦谷美鈴 楽曲コミュまとめ【学マス】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20250630",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=XMXlHjoQcqo",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴"
        }
      }
    }
  },
  {
    "alias": "M07",
    "logical_source_id": "1nN2PZIV2tV04PlGtsRTmXv3wKHAkVDYq",
    "character": "MISUZU",
    "role": "Superlative song communication",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【Superlative】秦谷美鈴  楽曲コミュまとめ【学マス】-(1080p60).mp4",
    "sha256": "76c9594d4568c4615b7ab115ca0c217940fc4e8b08e89d19c434e092ae4d1fa7",
    "bytes": 51118172,
    "duration_seconds": 496.187211,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "76c9594d4568c4615b7ab115ca0c217940fc4e8b08e89d19c434e092ae4d1fa7",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 7620608,
          "duration": "496.133333",
          "bit_rate": "659919",
          "bits_per_raw_sample": "8",
          "nb_frames": "29768",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 21881856,
          "duration": "496.187211",
          "bit_rate": "128004",
          "nb_frames": "21369",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 44656849,
          "duration": "496.187211",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【Superlative】秦谷美鈴  楽曲コミュまとめ【学マス】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "496.187211",
        "size": "51118172",
        "bit_rate": "824175",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【Superlative】秦谷美鈴  楽曲コミュまとめ【学マス】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20260105",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=tqAzbChk9s8",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴"
        }
      }
    }
  },
  {
    "alias": "M08",
    "logical_source_id": "1Mp9ze1ECRHV99ZKYEbWDF4lPDDonuf8_",
    "character": "MISUZU",
    "role": "VEIL song communication",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【VEIL】秦谷美鈴  楽曲コミュまとめ【学マス】-(1080p60).mp4",
    "sha256": "e5933b3520303f5992f8bda8e49d4dbc7a6da51a522bd90e0db98eac951c8cb5",
    "bytes": 92923066,
    "duration_seconds": 490.219683,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "e5933b3520303f5992f8bda8e49d4dbc7a6da51a522bd90e0db98eac951c8cb5",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 7528960,
          "duration": "490.166667",
          "bit_rate": "1352343",
          "bits_per_raw_sample": "8",
          "nb_frames": "29410",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 21618688,
          "duration": "490.219683",
          "bit_rate": "128002",
          "nb_frames": "21112",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 44119771,
          "duration": "490.219678",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【VEIL】秦谷美鈴  楽曲コミュまとめ【学マス】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "490.219683",
        "size": "92923066",
        "bit_rate": "1516431",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【VEIL】秦谷美鈴  楽曲コミュまとめ【学マス】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20260429",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=m4Wnr8rhCNM",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴"
        }
      }
    }
  },
  {
    "alias": "M09",
    "logical_source_id": "1daR8DowUeKrFiEHPvHfOA_CHkOaZHgoO",
    "character": "MISUZU",
    "role": "Star-mine song communication",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【Star-mine】秦谷美鈴  楽曲コミュまとめ【学マス】-(1080p60).mp4",
    "sha256": "709b8ff2430dd2577453c6cc631bfa1359b8b06035534a0d123f3d9a1ff0e94a",
    "bytes": 82452571,
    "duration_seconds": 702.984127,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "709b8ff2430dd2577453c6cc631bfa1359b8b06035534a0d123f3d9a1ff0e94a",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 10797056,
          "duration": "702.933333",
          "bit_rate": "779032",
          "bits_per_raw_sample": "8",
          "nb_frames": "42176",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 31001600,
          "duration": "702.984127",
          "bit_rate": "128009",
          "nb_frames": "30275",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 63268571,
          "duration": "702.984122",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【Star-mine】秦谷美鈴  楽曲コミュまとめ【学マス】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "702.984127",
        "size": "82452571",
        "bit_rate": "938315",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【Star-mine】秦谷美鈴  楽曲コミュまとめ【学マス】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20250731",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=4auf2r0lV1U",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#秦谷美鈴"
        }
      }
    }
  },
  {
    "alias": "M10",
    "logical_source_id": "1WmrTOKijFtOCAUZeN_T361MXAx6SBgDC",
    "character": "MISUZU",
    "role": "Tsuki no Kame in-game 3DMV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ツキノカメ」 (秦谷美鈴 ソロ SSR)【学マス⧸学園アイドルマスタ⧸(Moon Turtle) Gakuen idolm@ster MV】-(1080p60).mp4",
    "sha256": "a88ad4fe405de061a3877d53cdbe238910e549a70bee1df9bbf0ef6039a73154",
    "bytes": 101462116,
    "duration_seconds": 178.561451,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "a88ad4fe405de061a3877d53cdbe238910e549a70bee1df9bbf0ef6039a73154",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2741504,
          "duration": "178.483333",
          "bit_rate": "4364093",
          "bits_per_raw_sample": "8",
          "nb_frames": "10709",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          },
          "side_data_list": [
            {
              "side_data_type": "Content light level metadata",
              "max_content": 1000,
              "max_average": 200
            }
          ]
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 7874560,
          "duration": "178.561451",
          "bit_rate": "127999",
          "nb_frames": "7690",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 16070531,
          "duration": "178.561456",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ツキノカメ」 (秦谷美鈴 ソロ SSR)【学マス⧸学園アイドルマスタ⧸(Moon Turtle) Gakuen idolm@ster MV】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "178.561451",
        "size": "101462116",
        "bit_rate": "4545756",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「ツキノカメ」 (秦谷美鈴 ソロ SSR)【学マス/学園アイドルマスタ/(Moon Turtle) Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20250516",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=9cES3zJ-Clo",
          "description": "「ツキノカメ」 (#秦谷美鈴  ソロ SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44988243\n\n歌：秦谷美鈴 (CV. 春咲 暖)\n作詞：#ミフメイ\n作曲：ミフメイ\n編曲：ミフメイ\n\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 #学園偶像大師",
          "synopsis": "「ツキノカメ」 (#秦谷美鈴  ソロ SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44988243\n\n歌：秦谷美鈴 (CV. 春咲 暖)\n作詞：#ミフメイ\n作曲：ミフメイ\n編曲：ミフメイ\n\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 #学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "M11",
    "logical_source_id": "1yZf5-OSc870QyVOWvfMrwse1rT3ide5j",
    "character": "MISUZU",
    "role": "Tsuki no Kame official authored MV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「ツキノカメ」Official Music Video (HATSUBOSHI GAKUEN - Moon Turtle)-(1080p24).mp4",
    "sha256": "ebb51092cbbe799de4567f50e57a9b202e2c028983d1b3ad7d9c92c666cf9b61",
    "bytes": 132779690,
    "duration_seconds": 283.980045,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "ebb51092cbbe799de4567f50e57a9b202e2c028983d1b3ad7d9c92c666cf9b61",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.640028",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 40,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "24/1",
          "avg_frame_rate": "24/1",
          "time_base": "1/12288",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 3488768,
          "duration": "283.916667",
          "bit_rate": "3435846",
          "bits_per_raw_sample": "8",
          "nb_frames": "6814",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 12523520,
          "duration": "283.980045",
          "bit_rate": "255999",
          "nb_frames": "12230",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 25558204,
          "duration": "283.980044",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「ツキノカメ」Official Music Video (HATSUBOSHI GAKUEN - Moon Turtle)-(1080p24).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "283.980045",
        "size": "132779690",
        "bit_rate": "3740535",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "初星学園 「ツキノカメ」Official Music Video (HATSUBOSHI GAKUEN - Moon Turtle)",
          "artist": "HATSUBOSHI GAKUEN",
          "genre": "Music",
          "date": "20250206",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=E74wm1P6CPI",
          "description": "[EN Credits.]\nMoon Turtle\n▶Music\nSong by Misuzu Hataya (VA.Non Harusaki)\nLyric written, Composed, Arranged by mifumei\n\nVn.1 Yuki Mukoyama\nVn.2 Shiho Tanaka\nViola Eri Iwane\nCello Masateru Nishikata\n\nRecording Engineer：Naofumi Momota\nMixed by mifumei\nStudio: HeartBeat Ast, Studio Secret Base(Rebrast)\n\n▶Movie\nIllustrator：kiato\nDirector & Storyboard：Yusuke Ishida\nCG Producer：ICHIGORINAHAMU\nCG Artist：haquxx\nCompositor & Motion Graphics：Wakumoto Tomotaka\nCharacter Motion Designer：Heguri Keiko\nTitle & Lyric Design：ZUMA\nPlanner & Coordinator：Takuya Negawa\n\n------------------------------\n[JP Credits.]\nツキノカメ\n▶Music\n歌：秦谷美鈴 (CV. 春咲 暖)\n作詞作曲編曲：ミフメイ\n\nVn.1 向山有輝\nVn.2 田中紫帆\nViola 岩根衣李\nCello 西方正輝\n\nRecording Engineer：百田尚史\nMixed by ミフメイ\nStudio: HeartBeat Ast, Studio Secret Base(Rebrast)\n\n▶Movie\nIllustrator：きあと\nDirector & Storyboard：石田裕亮\nCG Producer：苺りなはむ\nCG Artist：haquxx\nCompositor & Motion Graphics：涌元 トモタカ\nCharacter Motion Designer：平郡啓子\nTitle & Lyric Design：ZUMA\nPlanner & Coordinator： 子川拓哉\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 子川拓哉\nLabel Director : 大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n▶「ツキノカメ」インスト音源データ公開中♬\nhttps://gakuen-label.idolmaster-official.jp/download\n\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2025 Bandai Namco Entertainment Inc.\n\n#秦谷美鈴 #初星学園 #ミフメイ #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen",
          "synopsis": "[EN Credits.]\nMoon Turtle\n▶Music\nSong by Misuzu Hataya (VA.Non Harusaki)\nLyric written, Composed, Arranged by mifumei\n\nVn.1 Yuki Mukoyama\nVn.2 Shiho Tanaka\nViola Eri Iwane\nCello Masateru Nishikata\n\nRecording Engineer：Naofumi Momota\nMixed by mifumei\nStudio: HeartBeat Ast, Studio Secret Base(Rebrast)\n\n▶Movie\nIllustrator：kiato\nDirector & Storyboard：Yusuke Ishida\nCG Producer：ICHIGORINAHAMU\nCG Artist：haquxx\nCompositor & Motion Graphics：Wakumoto Tomotaka\nCharacter Motion Designer：Heguri Keiko\nTitle & Lyric Design：ZUMA\nPlanner & Coordinator：Takuya Negawa\n\n------------------------------\n[JP Credits.]\nツキノカメ\n▶Music\n歌：秦谷美鈴 (CV. 春咲 暖)\n作詞作曲編曲：ミフメイ\n\nVn.1 向山有輝\nVn.2 田中紫帆\nViola 岩根衣李\nCello 西方正輝\n\nRecording Engineer：百田尚史\nMixed by ミフメイ\nStudio: HeartBeat Ast, Studio Secret Base(Rebrast)\n\n▶Movie\nIllustrator：きあと\nDirector & Storyboard：石田裕亮\nCG Producer：苺りなはむ\nCG Artist：haquxx\nCompositor & Motion Graphics：涌元 トモタカ\nCharacter Motion Designer：平郡啓子\nTitle & Lyric Design：ZUMA\nPlanner & Coordinator： 子川拓哉\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 子川拓哉\nLabel Director : 大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n▶「ツキノカメ」インスト音源データ公開中♬\nhttps://gakuen-label.idolmaster-official.jp/download\n\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2025 Bandai Namco Entertainment Inc.\n\n#秦谷美鈴 #初星学園 #ミフメイ #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen"
        }
      }
    }
  },
  {
    "alias": "M12",
    "logical_source_id": "17qwFKYPq9dt5O9O8L-aWnu3d5zhNZRN0",
    "character": "MISUZU",
    "role": "Campus mode in-game 3DMV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Campus mode!!」(秦谷美鈴 フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
    "sha256": "47bbe2204fa5f1a0bf2c371c8788c831b49a6c3b432af19ff233d639bafa0f82",
    "bytes": 109076334,
    "duration_seconds": 159.869388,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "47bbe2204fa5f1a0bf2c371c8788c831b49a6c3b432af19ff233d639bafa0f82",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2454784,
          "duration": "159.816667",
          "bit_rate": "5267880",
          "bits_per_raw_sample": "8",
          "nb_frames": "9589",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          },
          "side_data_list": [
            {
              "side_data_type": "Content light level metadata",
              "max_content": 1000,
              "max_average": 200
            }
          ]
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 7050240,
          "duration": "159.869388",
          "bit_rate": "127999",
          "nb_frames": "6885",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 14388245,
          "duration": "159.869389",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Campus mode!!」(秦谷美鈴 フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "159.869388",
        "size": "109076334",
        "bit_rate": "5458272",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「Campus mode!!」(秦谷美鈴 フェスSSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20250630",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=30uxo0Dgs8M",
          "description": "「Campus mode!!」(#秦谷美鈴 フェスSSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45138574\n歌：秦谷美鈴 (CV. 春咲暖)\n作詞・作曲：田淵智也\n編曲：滝澤俊輔（TRYTONELABO）\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「Campus mode!!」(#秦谷美鈴 フェスSSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45138574\n歌：秦谷美鈴 (CV. 春咲暖)\n作詞・作曲：田淵智也\n編曲：滝澤俊輔（TRYTONELABO）\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "M13",
    "logical_source_id": "1_TvGBz4HD-xZeysP98HQyNKLXH9RtMyD",
    "character": "MISUZU",
    "role": "Superlative in-game 3DMV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Superlative」(秦谷美鈴 ソロ2 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
    "sha256": "9bedc9ad49821d1d13e2d3b9f130f386d51ea5f06cc94ad7339ecf96b6e9c3cb",
    "bytes": 116330741,
    "duration_seconds": 216.549297,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "9bedc9ad49821d1d13e2d3b9f130f386d51ea5f06cc94ad7339ecf96b6e9c3cb",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 3325184,
          "duration": "216.483333",
          "bit_rate": "4120749",
          "bits_per_raw_sample": "8",
          "nb_frames": "12989",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          },
          "side_data_list": [
            {
              "side_data_type": "Content light level metadata",
              "max_content": 1000,
              "max_average": 200
            }
          ]
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 9549824,
          "duration": "216.549297",
          "bit_rate": "127999",
          "nb_frames": "9326",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 19489437,
          "duration": "216.549300",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Superlative」(秦谷美鈴 ソロ2 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "216.549297",
        "size": "116330741",
        "bit_rate": "4297616",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「Superlative」(秦谷美鈴 ソロ2 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20260105",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=O2VI4mS6kfg",
          "description": "「Superlative」(#秦谷美鈴  ソロ2 SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45805506\n\n作詞・作曲・編曲：siqlo\n歌：秦谷美鈴(CV：春咲暖)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「Superlative」(#秦谷美鈴  ソロ2 SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45805506\n\n作詞・作曲・編曲：siqlo\n歌：秦谷美鈴(CV：春咲暖)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "M14",
    "logical_source_id": "1yQv_fbuqPScYz1q8haAT-Bv4HJv-CTNO",
    "character": "MISUZU",
    "role": "Superlative full-mix/static comparison source",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\Superlative-(1080p25).mp4",
    "sha256": "a8ccbeab7e74f6103bfc30839772ef8956f1d0ab971cb4d8064c9bf79a661cc8",
    "bytes": 15376205,
    "duration_seconds": 304.888005,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "a8ccbeab7e74f6103bfc30839772ef8956f1d0ab971cb4d8064c9bf79a661cc8",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.640020",
          "width": 1080,
          "height": 1080,
          "coded_width": 1080,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "1:1",
          "pix_fmt": "yuv420p",
          "level": 32,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "25/1",
          "avg_frame_rate": "25/1",
          "time_base": "1/12800",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 3901952,
          "duration": "304.840000",
          "bit_rate": "125761",
          "bits_per_raw_sample": "8",
          "nb_frames": "7621",
          "extradata_size": 46,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 13445561,
          "duration": "304.888005",
          "bit_rate": "256000",
          "nb_frames": "13132",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 27439920,
          "duration": "304.888000",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\Superlative-(1080p25).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "304.888005",
        "size": "15376205",
        "bit_rate": "403458",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "Superlative",
          "artist": "Hatsuboshi Gakuen, siqlo, Misuzu Hataya, siqlo, siqlo, siqlo",
          "album": "Superlative",
          "genre": "Music",
          "date": "20260105",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=Ie_btWuTW6M",
          "description": "Provided to YouTube by NexTone Inc.\n\nSuperlative · Hatsuboshi Gakuen · siqlo · Misuzu Hataya · siqlo · siqlo · siqlo\n\nSuperlative\n\nReleased on: 2026-01-06\n\nAuto-generated by YouTube.",
          "synopsis": "Provided to YouTube by NexTone Inc.\n\nSuperlative · Hatsuboshi Gakuen · siqlo · Misuzu Hataya · siqlo · siqlo · siqlo\n\nSuperlative\n\nReleased on: 2026-01-06\n\nAuto-generated by YouTube."
        }
      }
    }
  },
  {
    "alias": "M15",
    "logical_source_id": "1IcGLjifbxfTFEeS9T429VS-rJWPIT-60",
    "character": "MISUZU",
    "role": "VEIL in-game STEP3 3DMV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「VEIL」(秦谷美鈴 STEP3 SSR)【学マス⧸学園アイドルマスタ⧸ 学園偶像大師⧸ Gakuen idolm@ster MV】-(1080p60).mp4",
    "sha256": "7a9f3b58287c9a663b591130d2d7cb7554b3be1915731262144f93c03644c7c6",
    "bytes": 96410925,
    "duration_seconds": 161.053605,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "7a9f3b58287c9a663b591130d2d7cb7554b3be1915731262144f93c03644c7c6",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2472960,
          "duration": "161.000000",
          "bit_rate": "4595209",
          "bits_per_raw_sample": "8",
          "nb_frames": "9660",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 7102464,
          "duration": "161.053605",
          "bit_rate": "127999",
          "nb_frames": "6936",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 14494824,
          "duration": "161.053600",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「VEIL」(秦谷美鈴 STEP3 SSR)【学マス⧸学園アイドルマスタ⧸ 学園偶像大師⧸ Gakuen idolm@ster MV】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "161.053605",
        "size": "96410925",
        "bit_rate": "4789010",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「VEIL」(秦谷美鈴 STEP3 SSR)【学マス/学園アイドルマスタ/ 学園偶像大師/ Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20260429",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=C7fmMA7Tpag",
          "description": "「VEIL」(#秦谷美鈴  STEP3 SSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm46242743\n\n作詞：GUCCHO\n作曲：GUCCHO、Dubscribe\n編曲：Dubscribe、GUCCHO\n秦谷美鈴(CV：春咲暖)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「VEIL」(#秦谷美鈴  STEP3 SSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm46242743\n\n作詞：GUCCHO\n作曲：GUCCHO、Dubscribe\n編曲：Dubscribe、GUCCHO\n秦谷美鈴(CV：春咲暖)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "M16",
    "logical_source_id": "1f-LzucKPa0x6XuAN7wvoqwM4FG5Fao11",
    "character": "MISUZU",
    "role": "VEIL official authored MV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「VEIL」Official Music Video (HATSUBOSHI GAKUEN - VEIL)-(1080p24).mp4",
    "sha256": "40950da9822dbb2755d298200668fd42d52f6fddeba0122a6d6ce9f63de76f72",
    "bytes": 86566206,
    "duration_seconds": 213.112744,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "40950da9822dbb2755d298200668fd42d52f6fddeba0122a6d6ce9f63de76f72",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.640028",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 40,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "24/1",
          "avg_frame_rate": "24/1",
          "time_base": "1/12288",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2617856,
          "duration": "213.041667",
          "bit_rate": "2941955",
          "bits_per_raw_sample": "8",
          "nb_frames": "5113",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 9398272,
          "duration": "213.112744",
          "bit_rate": "255999",
          "nb_frames": "9178",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 19180147,
          "duration": "213.112744",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「VEIL」Official Music Video (HATSUBOSHI GAKUEN - VEIL)-(1080p24).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "213.112744",
        "size": "86566206",
        "bit_rate": "3249592",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "初星学園 「VEIL」Official Music Video (HATSUBOSHI GAKUEN - VEIL)",
          "artist": "HATSUBOSHI GAKUEN",
          "genre": "Music",
          "date": "20260429",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=AbxzlgJTM-I",
          "description": "[EN Credits.]\nVEIL\n\n▶Music\nSong by Misuzu Hataya (VA. Non Harusaki)\nLyric written by GUCCHO\nComposed by GUCCHO, Dubscribe\nArranged by Dubscribe, GUCCHO\n\n▶Movie\nDirector: Kosuke Tsukagawa (SIGNIF)\nCharacter Design / Illustrator: match\nAnimator: Kana Kurimoto, Haru Yamao, Amanotou, Souupbox, Akihiko Wakahoi, Sota Fukushima, Ranka, Kyo Tanaka, bibi, tyodendo, aki\n3D Artist: Reika, Ai Ikeda, Akari Kumagai (SIGNIF), Sakura Misawa\nEffects Artist: Ryoma Sanpei (SIGNIF)\nProducer: Musashi Ito (SIGNIF)\nMV Producer:KEISUKE YANO\n\n[JP Credits.]\nVEIL\n\n▶Music\n歌：秦谷美鈴 (CV. 春咲 暖)\n作詞：GUCCHO\n作曲：GUCCHO, Dubscribe\n編曲：Dubscribe, GUCCHO\n\n▶Movie\nディレクター：塚川 功祐（SIGNIF）\nキャラクターデザイン / イラストレーター：match\nアニメーター：栗本 夏奈、山尾 波留、あまのとう、スーープボックス、若穂囲 晶彦、福嶋 颯汰、らんか、田中 響、びび、超電導、aki\n3Dアーティスト：玲架、池田 愛、熊谷 あかり（SIGNIF）、三澤 さくら\nエフェクトアーティスト：三瓶 伶真（SIGNIF）\nプロデューサー：伊藤 夢（SIGNIF）\nMV Producer:矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 尾上和駿、大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2026 Bandai Namco Entertainment Inc.\n\n#秦谷美鈴 #初星学園 #GUCCHO #Dubscribe #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen",
          "synopsis": "[EN Credits.]\nVEIL\n\n▶Music\nSong by Misuzu Hataya (VA. Non Harusaki)\nLyric written by GUCCHO\nComposed by GUCCHO, Dubscribe\nArranged by Dubscribe, GUCCHO\n\n▶Movie\nDirector: Kosuke Tsukagawa (SIGNIF)\nCharacter Design / Illustrator: match\nAnimator: Kana Kurimoto, Haru Yamao, Amanotou, Souupbox, Akihiko Wakahoi, Sota Fukushima, Ranka, Kyo Tanaka, bibi, tyodendo, aki\n3D Artist: Reika, Ai Ikeda, Akari Kumagai (SIGNIF), Sakura Misawa\nEffects Artist: Ryoma Sanpei (SIGNIF)\nProducer: Musashi Ito (SIGNIF)\nMV Producer:KEISUKE YANO\n\n[JP Credits.]\nVEIL\n\n▶Music\n歌：秦谷美鈴 (CV. 春咲 暖)\n作詞：GUCCHO\n作曲：GUCCHO, Dubscribe\n編曲：Dubscribe, GUCCHO\n\n▶Movie\nディレクター：塚川 功祐（SIGNIF）\nキャラクターデザイン / イラストレーター：match\nアニメーター：栗本 夏奈、山尾 波留、あまのとう、スーープボックス、若穂囲 晶彦、福嶋 颯汰、らんか、田中 響、びび、超電導、aki\n3Dアーティスト：玲架、池田 愛、熊谷 あかり（SIGNIF）、三澤 さくら\nエフェクトアーティスト：三瓶 伶真（SIGNIF）\nプロデューサー：伊藤 夢（SIGNIF）\nMV Producer:矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 尾上和駿、大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2026 Bandai Namco Entertainment Inc.\n\n#秦谷美鈴 #初星学園 #GUCCHO #Dubscribe #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen"
        }
      }
    }
  },
  {
    "alias": "M17",
    "logical_source_id": "1UyUsSr7ZUed6Kh6oHtIsmyjo4GiWvLTo",
    "character": "MISUZU",
    "role": "Begrazia Star-mine in-game 3DMV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\4K HDR「Star-mine」(Begrazia SSR ユニット曲)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
    "sha256": "f1143c1aaa2ca5df6c577c1b9d27c88cc19208e0c6218441455547a8e5130430",
    "bytes": 134093200,
    "duration_seconds": 201.433107,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "f1143c1aaa2ca5df6c577c1b9d27c88cc19208e0c6218441455547a8e5130430",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 3092992,
          "duration": "201.366667",
          "bit_rate": "5135404",
          "bits_per_raw_sample": "8",
          "nb_frames": "12082",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          },
          "side_data_list": [
            {
              "side_data_type": "Content light level metadata",
              "max_content": 1000,
              "max_average": 200
            }
          ]
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 8883200,
          "duration": "201.433107",
          "bit_rate": "127999",
          "nb_frames": "8675",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 18128980,
          "duration": "201.433111",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\4K HDR「Star-mine」(Begrazia SSR ユニット曲)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "201.433107",
        "size": "134093200",
        "bit_rate": "5325567",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「Star-mine」(Begrazia SSR ユニット曲)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20250731",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=yrW9mgbk7og",
          "description": "「Star-mine」(Begrazia ユニット曲) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45241662\n作詞・作曲・編曲：じん\n歌：\nBegrazia\n花海佑芽CV：松田彩音、#秦谷美鈴 CV：春咲暖、十王星南 CV：陽高真白\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「Star-mine」(Begrazia ユニット曲) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45241662\n作詞・作曲・編曲：じん\n歌：\nBegrazia\n花海佑芽CV：松田彩音、#秦谷美鈴 CV：春咲暖、十王星南 CV：陽高真白\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "M18",
    "logical_source_id": "1emxDRAvHC46s-v0x4eYFW1pCjdDGvIM9",
    "character": "MISUZU",
    "role": "Begrazia Star-mine official authored MV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\初星学園 「Star-mine」Official Music Video (HATSUBOSHI GAKUEN - Star-mine)-(1080p24).mp4",
    "sha256": "d0ce84afef4bb91d1f20f15ecd02fe459f5a906cd6b64b9abda98e299f837fd6",
    "bytes": 74692261,
    "duration_seconds": 240.047891,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "d0ce84afef4bb91d1f20f15ecd02fe459f5a906cd6b64b9abda98e299f837fd6",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.640028",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 40,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "24/1",
          "avg_frame_rate": "24/1",
          "time_base": "1/12288",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2949120,
          "duration": "240.000000",
          "bit_rate": "2175933",
          "bits_per_raw_sample": "8",
          "nb_frames": "5760",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 10586112,
          "duration": "240.047891",
          "bit_rate": "255999",
          "nb_frames": "10338",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 21604310,
          "duration": "240.047889",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\初星学園 「Star-mine」Official Music Video (HATSUBOSHI GAKUEN - Star-mine)-(1080p24).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "240.047891",
        "size": "74692261",
        "bit_rate": "2489245",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "初星学園 「Star-mine」Official Music Video (HATSUBOSHI GAKUEN - Star-mine)",
          "artist": "HATSUBOSHI GAKUEN",
          "genre": "Music",
          "date": "20250731",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=BLkCR5h_Sv4",
          "description": "[EN Credits.]\nStar-mine\n▶Music\nSong by Begrazia\nLyric written, Composed, Arranged by JIN\n\nLead Guitar：Umi Nonaka\nDrums：Janku\nBass：Yuki Natsume\nPiano：Hiroshi Funatsu（SperioNz）\nRhythm Guitar & All other instruments：JIN\n\n▶Movie\nDirection & Creative Produce & Storyboard：reinou\nCharactor design & Illustration & Paint：Oshima Tsukumo\nAnimation：Aoyama Wasabi / Goru / Kumaneko Yoru\nComposite & Type design：Cymo\nLogo & Credit design：Punch\nMV Producer：KEISUKE YANO\n------------------------------\n[JP Credits.]\nStar-mine\n▶Music\n歌：Begrazia\n作詞作曲編曲：じん\n\nLead Guitar：野中 海\nDrums：ジャンク\nBass：ナツメ ユウキ\nPiano：船津 宏（SperioNz）\nRhythm Guitar & All other instruments：じん\n\n▶Movie\nDirection & Creative Produce & Storyboard：reinou\nCharactor design & Illustration & Paint：大島つくも\nAnimation：葵山わさび / ゴル / 熊猫よる\nComposite & Type design：Cymo\nLogo & Credit design：パンチ\nMV Producer：矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2025 Bandai Namco Entertainment Inc.\n\n#Begrazia #初星学園 #じん #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen",
          "synopsis": "[EN Credits.]\nStar-mine\n▶Music\nSong by Begrazia\nLyric written, Composed, Arranged by JIN\n\nLead Guitar：Umi Nonaka\nDrums：Janku\nBass：Yuki Natsume\nPiano：Hiroshi Funatsu（SperioNz）\nRhythm Guitar & All other instruments：JIN\n\n▶Movie\nDirection & Creative Produce & Storyboard：reinou\nCharactor design & Illustration & Paint：Oshima Tsukumo\nAnimation：Aoyama Wasabi / Goru / Kumaneko Yoru\nComposite & Type design：Cymo\nLogo & Credit design：Punch\nMV Producer：KEISUKE YANO\n------------------------------\n[JP Credits.]\nStar-mine\n▶Music\n歌：Begrazia\n作詞作曲編曲：じん\n\nLead Guitar：野中 海\nDrums：ジャンク\nBass：ナツメ ユウキ\nPiano：船津 宏（SperioNz）\nRhythm Guitar & All other instruments：じん\n\n▶Movie\nDirection & Creative Produce & Storyboard：reinou\nCharactor design & Illustration & Paint：大島つくも\nAnimation：葵山わさび / ゴル / 熊猫よる\nComposite & Type design：Cymo\nLogo & Credit design：パンチ\nMV Producer：矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2025 Bandai Namco Entertainment Inc.\n\n#Begrazia #初星学園 #じん #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen"
        }
      }
    }
  },
  {
    "alias": "M19",
    "logical_source_id": "170-Xv0Fu8C_tZsuJd8zPOD6eMoQzVZie",
    "character": "MISUZU",
    "role": "ENDLESS DANCE Misuzu performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ENDLESS DANCE」(秦谷美鈴 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
    "sha256": "51cd1eec16dab8fb63058e5d3fdc294265a45c44e06e2d3cb76637ab0d8b9192",
    "bytes": 72646397,
    "duration_seconds": 109.482086,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "51cd1eec16dab8fb63058e5d3fdc294265a45c44e06e2d3cb76637ab0d8b9192",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 1680640,
          "duration": "109.416667",
          "bit_rate": "5107631",
          "bits_per_raw_sample": "8",
          "nb_frames": "6565",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          },
          "side_data_list": [
            {
              "side_data_type": "Content light level metadata",
              "max_content": 1000,
              "max_average": 200
            }
          ]
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 4828160,
          "duration": "109.482086",
          "bit_rate": "127999",
          "nb_frames": "4715",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 9853388,
          "duration": "109.482089",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ENDLESS DANCE」(秦谷美鈴 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "109.482086",
        "size": "72646397",
        "bit_rate": "5308367",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「ENDLESS DANCE」(秦谷美鈴 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20260227",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=W2QuyEkuq54",
          "description": "「ENDLESS DANCE」(#秦谷美鈴  SSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45999270\n\n作詞・作曲：首藤義勝\n編曲：藤永龍太郎(Elements Garden)\n歌：秦谷美鈴(CV：春咲暖)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「ENDLESS DANCE」(#秦谷美鈴  SSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45999270\n\n作詞・作曲：首藤義勝\n編曲：藤永龍太郎(Elements Garden)\n歌：秦谷美鈴(CV：春咲暖)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "M20",
    "logical_source_id": "16up-So-St6oIqDkLO8fO5hmDcp675ras",
    "character": "MISUZU",
    "role": "Hajime Misuzu in-game 3DMV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「初〈はじめ〉」 (秦谷美鈴 ソロ)【学マス⧸学園アイドルマスタ⧸ Gakuen idolm@ster MV】-(1080p60).mp4",
    "sha256": "05bfb52fef8398601a86d4db2920cdf8d4670ea2a6c739ece52336249aab0525",
    "bytes": 104693446,
    "duration_seconds": 164.420499,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "05bfb52fef8398601a86d4db2920cdf8d4670ea2a6c739ece52336249aab0525",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2524672,
          "duration": "164.366667",
          "bit_rate": "4893646",
          "bits_per_raw_sample": "8",
          "nb_frames": "9862",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          },
          "side_data_list": [
            {
              "side_data_type": "Content light level metadata",
              "max_content": 1000,
              "max_average": 200
            }
          ]
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 7250944,
          "duration": "164.420499",
          "bit_rate": "127999",
          "nb_frames": "7081",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 14797845,
          "duration": "164.420500",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「初〈はじめ〉」 (秦谷美鈴 ソロ)【学マス⧸学園アイドルマスタ⧸ Gakuen idolm@ster MV】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "164.420499",
        "size": "104693446",
        "bit_rate": "5093936",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「初〈はじめ〉」 (秦谷美鈴 ソロ)【学マス/学園アイドルマスタ/ Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20250516",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=gnywJb1_oBc",
          "description": "「初」 (#秦谷美鈴  ソロ) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44988582\n\n作詞作曲：原口沙輔\n編曲：宮川弾・原口沙輔\n歌：秦谷美鈴 (CV. 春咲暖)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 #学園偶像大師",
          "synopsis": "「初」 (#秦谷美鈴  ソロ) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44988582\n\n作詞作曲：原口沙輔\n編曲：宮川弾・原口沙輔\n歌：秦谷美鈴 (CV. 春咲暖)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 #学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "M21",
    "logical_source_id": "1Dnsksn6TEnzualJKSXeZEkzSMqoylzuv",
    "character": "MISUZU",
    "role": "Yorunite official authored MV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「ヨルニテ」Official Music Video (HATSUBOSHI GAKUEN - yorunite)-(1080p24).mp4",
    "sha256": "142bfc32dcf1e0d09f9fe4472cde7b4e13d8cff993dbefb3c125131b3eb79705",
    "bytes": 93098663,
    "duration_seconds": 220.19483,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "142bfc32dcf1e0d09f9fe4472cde7b4e13d8cff993dbefb3c125131b3eb79705",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.640028",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 40,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "24/1",
          "avg_frame_rate": "24/1",
          "time_base": "1/12288",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2704896,
          "duration": "220.125000",
          "bit_rate": "3065754",
          "bits_per_raw_sample": "8",
          "nb_frames": "5283",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 9710592,
          "duration": "220.194830",
          "bit_rate": "255999",
          "nb_frames": "9483",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 19817535,
          "duration": "220.194833",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「ヨルニテ」Official Music Video (HATSUBOSHI GAKUEN - yorunite)-(1080p24).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "220.194830",
        "size": "93098663",
        "bit_rate": "3382410",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "初星学園 「ヨルニテ」Official Music Video (HATSUBOSHI GAKUEN - yorunite)",
          "artist": "HATSUBOSHI GAKUEN",
          "genre": "Music",
          "date": "20260421",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=X1xcOhkgc4c",
          "description": "[EN Credits.]\nyorunite\n\n▶Music\nSong by Misuzu Hataya (VA. Non Harusaki)\nLyric written, Composed, Arranged by Shogo Nomura(Bandai Namco Studios Inc.)\n\nGuitar/Piano：Shogo Nomura(Bandai Namco Studios Inc.)\nMix Engineer：Shogo Nomura(Bandai Namco Studios Inc.)\n\n▶Movie\nDirector:YYG NT Lab(Fudinoyamai/Kazuma Kanai)\nIllustration & Animation:Iou,Kuroda,kate,Konro,sa(same),JunchukanBonta,shirai_momokichi,temari izon,Nishiuri tsukasa,hige,Kaito Hirose,bonsai,mikan_city,Miyamori She,rerenge\nInterlude Visuals:haruka teramoto\nVideographer:Tamaki Terashima\nLyric Design:Ayu Kimura\nLyric Motion Design:40kl\nMV Producer:KEISUKE YANO\n\n[JP Credits.]\nヨルニテ\n\n▶Music\n歌：秦谷美鈴 (CV. 春咲 暖)\n作詞作曲編曲：Shogo Nomura(Bandai Namco Studios Inc.)\n\nGuitar/Piano：Shogo Nomura(Bandai Namco Studios Inc.)\nMix Engineer：Shogo Nomura(Bandai Namco Studios Inc.)\n\n▶Movie\nディレクター:YYG NT Lab(ふぢのやまい/カナイ カズマ)\nイラストレーション&アニメーション:黒田 硫黄、景都、\nこんろ、さ(さめ)、巡宙艦ボンタ、白井もも吉、手毬依存、西瓜士、ひげ、広瀬海斗、ぼんさい、みかん都市、宮森 しい、れれんげ\n間奏映像:寺本遥\nビデオグラファー:寺嶋環\nリリックデザイン:キムラ アユ\nリリックモーション:40kl\nMV Producer:矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 尾上和駿、大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2026 Bandai Namco Entertainment Inc.\n\n#秦谷美鈴 #初星学園 #ShogoNomura #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen",
          "synopsis": "[EN Credits.]\nyorunite\n\n▶Music\nSong by Misuzu Hataya (VA. Non Harusaki)\nLyric written, Composed, Arranged by Shogo Nomura(Bandai Namco Studios Inc.)\n\nGuitar/Piano：Shogo Nomura(Bandai Namco Studios Inc.)\nMix Engineer：Shogo Nomura(Bandai Namco Studios Inc.)\n\n▶Movie\nDirector:YYG NT Lab(Fudinoyamai/Kazuma Kanai)\nIllustration & Animation:Iou,Kuroda,kate,Konro,sa(same),JunchukanBonta,shirai_momokichi,temari izon,Nishiuri tsukasa,hige,Kaito Hirose,bonsai,mikan_city,Miyamori She,rerenge\nInterlude Visuals:haruka teramoto\nVideographer:Tamaki Terashima\nLyric Design:Ayu Kimura\nLyric Motion Design:40kl\nMV Producer:KEISUKE YANO\n\n[JP Credits.]\nヨルニテ\n\n▶Music\n歌：秦谷美鈴 (CV. 春咲 暖)\n作詞作曲編曲：Shogo Nomura(Bandai Namco Studios Inc.)\n\nGuitar/Piano：Shogo Nomura(Bandai Namco Studios Inc.)\nMix Engineer：Shogo Nomura(Bandai Namco Studios Inc.)\n\n▶Movie\nディレクター:YYG NT Lab(ふぢのやまい/カナイ カズマ)\nイラストレーション&アニメーション:黒田 硫黄、景都、\nこんろ、さ(さめ)、巡宙艦ボンタ、白井もも吉、手毬依存、西瓜士、ひげ、広瀬海斗、ぼんさい、みかん都市、宮森 しい、れれんげ\n間奏映像:寺本遥\nビデオグラファー:寺嶋環\nリリックデザイン:キムラ アユ\nリリックモーション:40kl\nMV Producer:矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 尾上和駿、大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2026 Bandai Namco Entertainment Inc.\n\n#秦谷美鈴 #初星学園 #ShogoNomura #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen"
        }
      }
    }
  },
  {
    "alias": "M22",
    "logical_source_id": "1hoOWfl9Xf-XefaIRyTskrcUdHiQeOrNa",
    "character": "MISUZU",
    "role": "Miracle Nanau Misuzu performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\【学マス】「ミラクルナナウ(ﾟ∀ﾟ)！」秦谷美鈴【MV】4K-(1080p60).mp4",
    "sha256": "e13c304126711786c8bc9efedbc1dbb22c0df7b67a57dcb0676d6ade51a404c8",
    "bytes": 68006584,
    "duration_seconds": 107.972789,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "e13c304126711786c8bc9efedbc1dbb22c0df7b67a57dcb0676d6ade51a404c8",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 1657600,
          "duration": "107.916667",
          "bit_rate": "4829131",
          "bits_per_raw_sample": "8",
          "nb_frames": "6475",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 4761600,
          "duration": "107.972789",
          "bit_rate": "127999",
          "nb_frames": "4650",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 9717551,
          "duration": "107.972789",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\【学マス】「ミラクルナナウ(ﾟ∀ﾟ)！」秦谷美鈴【MV】4K-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "107.972789",
        "size": "68006584",
        "bit_rate": "5038794",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【学マス】「ミラクルナナウ(ﾟ∀ﾟ)！」秦谷美鈴【MV】4K",
          "artist": "Aria",
          "genre": "Gaming",
          "date": "20250829",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=GY7RonZhCdo",
          "description": "歌唱：秦谷美鈴 (CV. 春咲暖)\n作詞作曲編曲：YUC'e\n\nhttps://gakuen.idolmaster-official.jp/\n\n#学マス  #学園アイドルマスター",
          "synopsis": "歌唱：秦谷美鈴 (CV. 春咲暖)\n作詞作曲編曲：YUC'e\n\nhttps://gakuen.idolmaster-official.jp/\n\n#学マス  #学園アイドルマスター"
        }
      }
    }
  },
  {
    "alias": "M23",
    "logical_source_id": "1FD-G-EejV1b4YCNwfXdiTs4MC1y_fh4R",
    "character": "MISUZU",
    "role": "Howling over the World Misuzu solo performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR (秦谷美鈴 ソロ SSR)「Howling over the World」【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
    "sha256": "0fa235b1eb273707fbd33438a79b9b3cff2df3108d713d70c1758efb3c701fec",
    "bytes": 63610676,
    "duration_seconds": 111.293243,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "0fa235b1eb273707fbd33438a79b9b3cff2df3108d713d70c1758efb3c701fec",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 1708544,
          "duration": "111.233333",
          "bit_rate": "4389622",
          "bits_per_raw_sample": "8",
          "nb_frames": "6674",
          "extradata_size": 45,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 4908032,
          "duration": "111.293243",
          "bit_rate": "127999",
          "nb_frames": "4793",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 10016392,
          "duration": "111.293244",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR (秦谷美鈴 ソロ SSR)「Howling over the World」【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "111.293243",
        "size": "63610676",
        "bit_rate": "4572473",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR (秦谷美鈴 ソロ SSR)「Howling over the World」【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20260715",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=2QDyEUtQ3ao",
          "description": "4K HDR「Howling over the World」 (#秦谷美鈴  ソロ SSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm46550869\n\n作詞・作曲・編曲： 烏屋茶房\n歌：秦谷美鈴 (CV. 春咲暖)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "4K HDR「Howling over the World」 (#秦谷美鈴  ソロ SSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm46550869\n\n作詞・作曲・編曲： 烏屋茶房\n歌：秦谷美鈴 (CV. 春咲暖)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "M24",
    "logical_source_id": "14TF8iaQLD4mibJIlLy1UZmx43m4LffTM",
    "character": "MISUZU",
    "role": "Gamushara ni Ikou Misuzu performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「がむしゃらに行こう！」 (秦谷美鈴 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
    "sha256": "af4f7355ac382dce4772a63cf365cda05b20f429a0be573c699a320e867de01b",
    "bytes": 71738288,
    "duration_seconds": 110.318005,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "af4f7355ac382dce4772a63cf365cda05b20f429a0be573c699a320e867de01b",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.64002a",
          "width": 1920,
          "height": 1080,
          "coded_width": 1920,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "16:9",
          "pix_fmt": "yuv420p",
          "level": 42,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "60/1",
          "avg_frame_rate": "60/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 1693440,
          "duration": "110.250000",
          "bit_rate": "4992337",
          "bits_per_raw_sample": "8",
          "nb_frames": "6615",
          "extradata_size": 44,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          },
          "side_data_list": [
            {
              "side_data_type": "Content light level metadata",
              "max_content": 1000,
              "max_average": 200
            }
          ]
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 4865024,
          "duration": "110.318005",
          "bit_rate": "127999",
          "nb_frames": "4751",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 9928620,
          "duration": "110.318000",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「がむしゃらに行こう！」 (秦谷美鈴 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "110.318005",
        "size": "71738288",
        "bit_rate": "5202290",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「がむしゃらに行こう！」 (秦谷美鈴 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20250929",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=ZmZRBbUOapA",
          "description": "「がむしゃらに行こう！」 (#秦谷美鈴 SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45459528\n\n歌：秦谷美鈴(CV：春咲暖)\n作詞：SHOW (Digz, Inc. Group)\n作曲：SHOW (Digz, Inc. Group)、Mitsu.J (Digz, Inc. Group)\n編曲：Mitsu.J (Digz, Inc. Group)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「がむしゃらに行こう！」 (#秦谷美鈴 SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45459528\n\n歌：秦谷美鈴(CV：春咲暖)\n作詞：SHOW (Digz, Inc. Group)\n作曲：SHOW (Digz, Inc. Group)、Mitsu.J (Digz, Inc. Group)\n編曲：Mitsu.J (Digz, Inc. Group)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "M25",
    "logical_source_id": "1vWmkHR3kPkpr5Vu_EVbPbDEtBAzsLW4N",
    "character": "MISUZU",
    "role": "Hajime alternate/full-mix source",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\[学マス] 『初』 秦谷 美鈴ver-(1080p30).mp4",
    "sha256": "97de00fe99a8bd1ba1b94cc367ad941e9714ff80f444e6bafad5e82e61904398",
    "bytes": 7800728,
    "duration_seconds": 154.366259,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "97de00fe99a8bd1ba1b94cc367ad941e9714ff80f444e6bafad5e82e61904398",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.640020",
          "width": 1086,
          "height": 1080,
          "coded_width": 1086,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "181:180",
          "pix_fmt": "yuv420p",
          "level": 32,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "30/1",
          "avg_frame_rate": "30/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2370048,
          "duration": "154.300000",
          "bit_rate": "219366",
          "bits_per_raw_sample": "8",
          "nb_frames": "4629",
          "extradata_size": 46,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 6807552,
          "duration": "154.366259",
          "bit_rate": "127999",
          "nb_frames": "6648",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "jpn",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 13892963,
          "duration": "154.366256",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\[学マス] 『初』 秦谷 美鈴ver-(1080p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "154.366259",
        "size": "7800728",
        "bit_rate": "404271",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "[学マス] 『初』 秦谷 美鈴ver",
          "artist": "グアニル-Guanil-",
          "genre": "People & Blogs",
          "date": "20250516",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=7xPd5U40K4E",
          "description": "〜初 Official Video 〜\nhttps://youtu.be/Mb4ToEslrhI\n\n初星学園:​⁠​⁠@hatsuboshi_gakuen ​⁠​⁠​⁠​⁠​⁠ ​⁠​⁠​⁠ \nアイドルマスター:​⁠​⁠​⁠​⁠​⁠​⁠​⁠@imas-official   ​⁠​⁠​⁠\n\n#学マス #学園アイドルマスター #初星学園 #秦谷美鈴",
          "synopsis": "〜初 Official Video 〜\nhttps://youtu.be/Mb4ToEslrhI\n\n初星学園:​⁠​⁠@hatsuboshi_gakuen ​⁠​⁠​⁠​⁠​⁠ ​⁠​⁠​⁠ \nアイドルマスター:​⁠​⁠​⁠​⁠​⁠​⁠​⁠@imas-official   ​⁠​⁠​⁠\n\n#学マス #学園アイドルマスター #初星学園 #秦谷美鈴"
        }
      }
    }
  },
  {
    "alias": "M26",
    "logical_source_id": "1RKfLuzy0LHXCOwYry2Dtv9XPAnngly55",
    "character": "MISUZU",
    "role": "Ume/Misuzu/Sena ensemble full-mix source",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\Howling over the World (花海佑芽・秦谷美鈴・十王星南 ver.)-(1080p25).mp4",
    "sha256": "4e527d9c1eb85480bfb36cd21998005c3da22e2805894c23ce4f5f46ec0e0efb",
    "bytes": 11917567,
    "duration_seconds": 241.822993,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "4e527d9c1eb85480bfb36cd21998005c3da22e2805894c23ce4f5f46ec0e0efb",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.640020",
          "width": 1080,
          "height": 1080,
          "coded_width": 1080,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "1:1",
          "pix_fmt": "yuv420p",
          "level": 32,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "25/1",
          "avg_frame_rate": "25/1",
          "time_base": "1/12800",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 3095040,
          "duration": "241.800000",
          "bit_rate": "115618",
          "bits_per_raw_sample": "8",
          "nb_frames": "6045",
          "extradata_size": 46,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 10664394,
          "duration": "241.822993",
          "bit_rate": "255999",
          "nb_frames": "10416",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 21764069,
          "duration": "241.822989",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\Howling over the World (花海佑芽・秦谷美鈴・十王星南 ver.)-(1080p25).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "241.822993",
        "size": "11917567",
        "bit_rate": "394257",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "Howling over the World (花海佑芽・秦谷美鈴・十王星南 ver.)",
          "artist": "Hatsuboshi Gakuen, Karasuyasabou, Ume Hanami, Misuzu Hataya, Sena Juo, Karasuyasabou, Karasuyasabou, Karasuyasabou",
          "album": "Howling over the World (Ume Hanami, Misuzu Hataya, Sena Juo ver.)",
          "genre": "Music",
          "date": "20250711",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=bD4mp-DYtFk",
          "description": "Provided to YouTube by NexTone Inc.\n\nHowling over the World (花海佑芽・秦谷美鈴・十王星南 ver.) · Hatsuboshi Gakuen · Karasuyasabou · Ume Hanami · Misuzu Hataya · Sena Juo · Karasuyasabou · Karasuyasabou · Karasuyasabou\n\nHowling over the World (Ume Hanami, Misuzu Hataya, Sena Juo ver.)\n\nReleased on: 2025-07-12\n\nAuto-generated by YouTube.",
          "synopsis": "Provided to YouTube by NexTone Inc.\n\nHowling over the World (花海佑芽・秦谷美鈴・十王星南 ver.) · Hatsuboshi Gakuen · Karasuyasabou · Ume Hanami · Misuzu Hataya · Sena Juo · Karasuyasabou · Karasuyasabou · Karasuyasabou\n\nHowling over the World (Ume Hanami, Misuzu Hataya, Sena Juo ver.)\n\nReleased on: 2025-07-12\n\nAuto-generated by YouTube."
        }
      }
    }
  },
  {
    "alias": "M27",
    "logical_source_id": "1PfUQwi0zPWIIZUqnjfgjigMEhv4mBPx1",
    "character": "MISUZU",
    "role": "Taisetsu na Mono contrast source",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\たいせつなもの-(1080p25).mp4",
    "sha256": "a476cc6f23a46ebb7050bf1e63c58ca7cedce940f43f75bb97e3c8870cd62e83",
    "bytes": 14470503,
    "duration_seconds": 316.381995,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "a476cc6f23a46ebb7050bf1e63c58ca7cedce940f43f75bb97e3c8870cd62e83",
    "materialization_note": "Current bytes match prior source record",
    "prior_probe": {
      "streams": [
        {
          "index": 0,
          "codec_name": "h264",
          "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
          "profile": "High",
          "codec_type": "video",
          "codec_tag_string": "avc1",
          "codec_tag": "0x31637661",
          "mime_codec_string": "avc1.640020",
          "width": 1080,
          "height": 1080,
          "coded_width": 1080,
          "coded_height": 1080,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "1:1",
          "pix_fmt": "yuv420p",
          "level": 32,
          "color_range": "tv",
          "color_space": "bt709",
          "color_transfer": "bt709",
          "color_primaries": "bt709",
          "chroma_location": "left",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "25/1",
          "avg_frame_rate": "25/1",
          "time_base": "1/12800",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 4049408,
          "duration": "316.360000",
          "bit_rate": "85962",
          "bits_per_raw_sample": "8",
          "nb_frames": "7909",
          "extradata_size": 46,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 1,
          "codec_name": "aac",
          "codec_long_name": "AAC (Advanced Audio Coding)",
          "profile": "LC",
          "codec_type": "audio",
          "codec_tag_string": "mp4a",
          "codec_tag": "0x6134706d",
          "mime_codec_string": "mp4a.40.2",
          "sample_fmt": "fltp",
          "sample_rate": "44100",
          "channels": 2,
          "channel_layout": "stereo",
          "bits_per_sample": 0,
          "initial_padding": 0,
          "id": "0x2",
          "r_frame_rate": "0/0",
          "avg_frame_rate": "0/0",
          "time_base": "1/44100",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 13952446,
          "duration": "316.381995",
          "bit_rate": "256000",
          "nb_frames": "13627",
          "extradata_size": 16,
          "disposition": {
            "default": 1,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 0,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          },
          "tags": {
            "language": "und",
            "handler_name": "ISO Media file produced by Google Inc."
          }
        },
        {
          "index": 2,
          "codec_name": "png",
          "codec_long_name": "PNG (Portable Network Graphics) image",
          "codec_type": "video",
          "codec_tag_string": "[0][0][0][0]",
          "codec_tag": "0x0000",
          "width": 1280,
          "height": 720,
          "coded_width": 1280,
          "coded_height": 720,
          "has_b_frames": 0,
          "pix_fmt": "rgb24",
          "level": -99,
          "color_range": "pc",
          "color_space": "gbr",
          "id": "0x0",
          "r_frame_rate": "90000/1",
          "avg_frame_rate": "0/0",
          "time_base": "1/90000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 28474380,
          "duration": "316.382000",
          "disposition": {
            "default": 0,
            "dub": 0,
            "original": 0,
            "comment": 0,
            "lyrics": 0,
            "karaoke": 0,
            "forced": 0,
            "hearing_impaired": 0,
            "visual_impaired": 0,
            "clean_effects": 0,
            "attached_pic": 1,
            "timed_thumbnails": 0,
            "non_diegetic": 0,
            "captions": 0,
            "descriptions": 0,
            "metadata": 0,
            "dependent": 0,
            "still_image": 0,
            "multilayer": 0
          }
        }
      ],
      "chapters": [],
      "format": {
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\たいせつなもの-(1080p25).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "316.381995",
        "size": "14470503",
        "bit_rate": "365899",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "たいせつなもの",
          "artist": "Hatsuboshi Gakuen, fuwari, Misuzu Hataya, フワリ (Dream Monster), フワリ (Dream Monster), フワリ (Dream Monster)",
          "album": "My Precious",
          "genre": "Music",
          "date": "20250205",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=y0QwzMhXK6o",
          "description": "Provided to YouTube by NexTone Inc.\n\nたいせつなもの · Hatsuboshi Gakuen · fuwari · Misuzu Hataya · フワリ (Dream Monster) · フワリ (Dream Monster) · フワリ (Dream Monster)\n\nMy Precious\n\nReleased on: 2025-02-06\n\nAuto-generated by YouTube.",
          "synopsis": "Provided to YouTube by NexTone Inc.\n\nたいせつなもの · Hatsuboshi Gakuen · fuwari · Misuzu Hataya · フワリ (Dream Monster) · フワリ (Dream Monster) · フワリ (Dream Monster)\n\nMy Precious\n\nReleased on: 2025-02-06\n\nAuto-generated by YouTube."
        }
      }
    }
  }
]
```

Save the following review plan as plans/misuzu-review-plan.json. Only declared timestamp requests feed extraction; purpose text is an analytical plan, not an observation.

```json
{
  "schema": "misuzu.full_rebuild.review_plan.v1",
  "character": "MISUZU",
  "status": "PLANNED_NOT_OBSERVED",
  "groups": [
    {
      "group_id": "MZ-FULL-01",
      "label": "Care and enclosure in one route",
      "claim_ids": [
        "MZ-AV-001",
        "MZ-AV-006",
        "MZ-AV-007",
        "MZ-AV-031"
      ],
      "purpose": "Compare hands, expression, camera distance and captions during service/need and enclosing possession; test continuity without declaring altruism or manipulation from a smile.",
      "passages": [
        {
          "alias": "M01",
          "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
          "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            828,
            832,
            836,
            840,
            844,
            848,
            852,
            856,
            860,
            864
          ],
          "selection_note": "Prior Dear004 care locator; selected readable caption/pose states.",
          "source_alias": "M01",
          "timestamps": [
            828,
            832,
            836,
            840,
            844,
            848,
            852,
            856,
            860,
            864
          ]
        },
        {
          "alias": "M01",
          "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
          "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            1194,
            1198,
            1202,
            1206,
            1210,
            1214,
            1218,
            1222,
            1226,
            1230
          ],
          "selection_note": "Prior Dear005 enclosure locator; compare with care.",
          "source_alias": "M01",
          "timestamps": [
            1194,
            1198,
            1202,
            1206,
            1210,
            1214,
            1218,
            1222,
            1226,
            1230
          ]
        }
      ],
      "locked_or_prior_controls": [
        "Dear004 raw90–112; Dear005 raw176–201 at locked A1 commit00d150a069a3ffa723a1ff264752ba242024caad",
        "Prior EXEC-MZ-M01-CARE/ENCLOSURE; new images must receive new provenance."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    },
    {
      "group_id": "MZ-FULL-02",
      "label": "Reciprocal conflict and non-restoration",
      "claim_ids": [
        "MZ-AV-008",
        "MZ-AV-009",
        "MZ-AV-010",
        "MZ-AV-011"
      ],
      "purpose": "Compare early explicit anger with the later Rinha conflict. The M02 target is discovery within the Dear017 marker interval, not a pre-certified line alignment.",
      "passages": [
        {
          "alias": "M01",
          "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
          "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            1700,
            1704,
            1708,
            1712,
            1716,
            1720,
            1724,
            1728,
            1732,
            1736,
            1740,
            1744
          ],
          "selection_note": "Prior Dear007 explicit anger exchange.",
          "source_alias": "M01",
          "timestamps": [
            1700,
            1704,
            1708,
            1712,
            1716,
            1720,
            1724,
            1728,
            1732,
            1736,
            1740,
            1744
          ]
        },
        {
          "alias": "M02",
          "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
          "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            1660,
            1680,
            1700,
            1720,
            1740,
            1760,
            1780,
            1800,
            1820,
            1840,
            1860,
            1880
          ],
          "selection_note": "Discovery sweep inside inherited Dear017[1634,1987); inspect speaker/caption before making claims.",
          "source_alias": "M02",
          "timestamps": [
            1660,
            1680,
            1700,
            1720,
            1740,
            1760,
            1780,
            1800,
            1820,
            1840,
            1860,
            1880
          ]
        }
      ],
      "locked_or_prior_controls": [
        "Dear007 locked script; Dear017 locked script; M02 embedded chapter markers",
        "Any relation-without-restoration inference remains controlled by exact script/core, not facial expression alone."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    },
    {
      "group_id": "MZ-FULL-03",
      "label": "Stored resentment and retrospective loss of preferred form",
      "claim_ids": [
        "MZ-AV-002",
        "MZ-AV-003",
        "MZ-AV-004",
        "MZ-AV-032",
        "MZ-AV-033"
      ],
      "purpose": "Test visible composure beside stored negative-affect language against the retrospective explanation of hurrying and losing the desired idol form.",
      "passages": [
        {
          "alias": "M03",
          "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
          "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
          "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            490,
            496,
            502,
            508,
            514,
            520,
            526,
            532,
            538,
            544,
            550,
            556
          ],
          "selection_note": "Dear022 resentment/withheld-tear locator.",
          "source_alias": "M03",
          "timestamps": [
            490,
            496,
            502,
            508,
            514,
            520,
            526,
            532,
            538,
            544,
            550,
            556
          ]
        },
        {
          "alias": "M03",
          "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
          "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
          "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            1810,
            1815,
            1820,
            1825,
            1830,
            1835,
            1840,
            1845,
            1850,
            1855,
            1860,
            1865
          ],
          "selection_note": "Dear026 retrospective conversation; do not label this as actual footage of overtraining.",
          "source_alias": "M03",
          "timestamps": [
            1810,
            1815,
            1820,
            1825,
            1830,
            1835,
            1840,
            1845,
            1850,
            1855,
            1860,
            1865
          ]
        }
      ],
      "locked_or_prior_controls": [
        "Dear022 raw159–226, especially182/191/198–202/226",
        "Dear026 raw66–96; prior EXEC-MZ-M03-RESENTMENT/IDENTITY."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    },
    {
      "group_id": "MZ-FULL-04",
      "label": "Promise injury and recovery without abandoned ambition",
      "claim_ids": [
        "MZ-AV-003",
        "MZ-AV-004",
        "MZ-AV-012",
        "MZ-AV-028",
        "MZ-AV-032",
        "MZ-AV-033",
        "MZ-AV-034"
      ],
      "purpose": "Compare apology and request for kindness with return to slower promise-keeping and renewed competitive language; separate textual recovery from audible tempo.",
      "passages": [
        {
          "alias": "M03",
          "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
          "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
          "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            1914,
            1920,
            1926,
            1932,
            1938,
            1944,
            1950,
            1956,
            1962,
            1968,
            1974,
            1980
          ],
          "selection_note": "Dear026 hurt/apology; choices may interrupt caption alignment.",
          "source_alias": "M03",
          "timestamps": [
            1914,
            1920,
            1926,
            1932,
            1938,
            1944,
            1950,
            1956,
            1962,
            1968,
            1974,
            1980
          ]
        },
        {
          "alias": "M03",
          "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
          "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
          "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            2034,
            2037,
            2040,
            2043,
            2046,
            2049,
            2052,
            2055,
            2058,
            2061,
            2064,
            2067
          ],
          "selection_note": "Dear026 recovery/star/yawn/competition captions.",
          "source_alias": "M03",
          "timestamps": [
            2034,
            2037,
            2040,
            2043,
            2046,
            2049,
            2052,
            2055,
            2058,
            2061,
            2064,
            2067
          ]
        }
      ],
      "locked_or_prior_controls": [
        "Dear026 raw137–194 and260–302; prior EXEC-MZ-M03-PROMISE/RECOVERY."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    },
    {
      "group_id": "MZ-FULL-05",
      "label": "Private exclusivity and public title/address",
      "claim_ids": [
        "MZ-AV-001",
        "MZ-AV-005",
        "MZ-AV-009",
        "MZ-AV-012",
        "MZ-AV-013",
        "MZ-AV-015",
        "MZ-AV-034",
        "MZ-AV-035",
        "MZ-AV-036",
        "MZ-AV-044",
        "MZ-AV-045"
      ],
      "purpose": "Compare the early intimate promise/exclusivity ending with public Dear036 address. Integrate the completed prior toolkit tears/yawn trial as inherited precise evidence without re-extracting its refinements.",
      "passages": [
        {
          "alias": "M01",
          "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
          "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            2716,
            2720,
            2724,
            2728,
            2732,
            2736,
            2740,
            2744,
            2748,
            2752
          ],
          "selection_note": "Dear010 early close and exclusive Producer phrase.",
          "source_alias": "M01",
          "timestamps": [
            2716,
            2720,
            2724,
            2728,
            2732,
            2736,
            2740,
            2744,
            2748,
            2752
          ]
        },
        {
          "alias": "M04",
          "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
          "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            2880,
            2910,
            2940,
            2970,
            3000,
            3030,
            3060,
            3090,
            3120,
            3150
          ],
          "selection_note": "Public-title/address discovery points within Dear036 before the previously refined tears ending.",
          "source_alias": "M04",
          "timestamps": [
            2880,
            2910,
            2940,
            2970,
            3000,
            3030,
            3060,
            3090,
            3120,
            3150
          ]
        }
      ],
      "locked_or_prior_controls": [
        "Dear010 raw371–394; Dear036 locked script",
        "Prior trial observations/misuzu.json and misuzu_delta.md:126 source points; no new listening."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    },
    {
      "group_id": "MZ-FULL-06",
      "label": "Song communications and public relationship controls",
      "claim_ids": [
        "MZ-AV-001",
        "MZ-AV-007",
        "MZ-AV-011",
        "MZ-AV-012",
        "MZ-AV-014",
        "MZ-AV-015",
        "MZ-AV-016",
        "MZ-AV-017",
        "MZ-AV-018",
        "MZ-AV-019",
        "MZ-AV-020",
        "MZ-AV-021",
        "MZ-AV-038",
        "MZ-AV-044"
      ],
      "purpose": "Identify actual caption/speaker/setting evidence across all five song communications; use textual core for recipient and non-restoration claims. Do not silently treat whole-source availability as review.",
      "passages": [
        {
          "alias": "M05",
          "logical_source_id": "1zLIbXE_fU7Me1O3SiDs7GE0nKwRms7zz",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【ツキノカメ】秦谷美鈴 楽曲コミュまとめ【学マス】-(1080p60).mp4",
          "sha256": "dc76e5fcf5f1e0057424a37e86e7503d26b2ae18607ab029823b090e35f7589d",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            74.582494,
            130.519365,
            186.456236,
            242.393107,
            298.329978
          ],
          "selection_note": "Exploratory caption/setting points supplement parent survey; no prior exact passage certification.",
          "source_alias": "M05",
          "timestamps": [
            74.582494,
            130.519365,
            186.456236,
            242.393107,
            298.329978
          ]
        },
        {
          "alias": "M06",
          "logical_source_id": "1-MzZgO0DWfS-6F6QzyxB8-jVU00MLf2g",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【Campus mode!!】秦谷美鈴 楽曲コミュまとめ【学マス】-(1080p60).mp4",
          "sha256": "bef614ac4b674565522caeec2f4e6e63e3e18e460aae3a1e182df5381c99d4df",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            122.540989,
            214.44673,
            306.352471,
            398.258213,
            490.163954
          ],
          "selection_note": "Exploratory caption/setting points supplement parent survey; no prior exact passage certification.",
          "source_alias": "M06",
          "timestamps": [
            122.540989,
            214.44673,
            306.352471,
            398.258213,
            490.163954
          ]
        },
        {
          "alias": "M07",
          "logical_source_id": "1nN2PZIV2tV04PlGtsRTmXv3wKHAkVDYq",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【Superlative】秦谷美鈴  楽曲コミュまとめ【学マス】-(1080p60).mp4",
          "sha256": "76c9594d4568c4615b7ab115ca0c217940fc4e8b08e89d19c434e092ae4d1fa7",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            99.237442,
            173.665524,
            248.093605,
            322.521687,
            396.949769
          ],
          "selection_note": "Exploratory caption/setting points supplement parent survey; no prior exact passage certification.",
          "source_alias": "M07",
          "timestamps": [
            99.237442,
            173.665524,
            248.093605,
            322.521687,
            396.949769
          ]
        },
        {
          "alias": "M08",
          "logical_source_id": "1Mp9ze1ECRHV99ZKYEbWDF4lPDDonuf8_",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【VEIL】秦谷美鈴  楽曲コミュまとめ【学マス】-(1080p60).mp4",
          "sha256": "e5933b3520303f5992f8bda8e49d4dbc7a6da51a522bd90e0db98eac951c8cb5",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            98.043937,
            171.576889,
            245.109841,
            318.642794,
            392.175746
          ],
          "selection_note": "Exploratory caption/setting points supplement parent survey; no prior exact passage certification.",
          "source_alias": "M08",
          "timestamps": [
            98.043937,
            171.576889,
            245.109841,
            318.642794,
            392.175746
          ]
        },
        {
          "alias": "M09",
          "logical_source_id": "1daR8DowUeKrFiEHPvHfOA_CHkOaZHgoO",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\03_SONG_COMMUS\\【Star-mine】秦谷美鈴  楽曲コミュまとめ【学マス】-(1080p60).mp4",
          "sha256": "709b8ff2430dd2577453c6cc631bfa1359b8b06035534a0d123f3d9a1ff0e94a",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            140.596825,
            246.044444,
            351.492063,
            456.939683,
            562.387302
          ],
          "selection_note": "Exploratory caption/setting points supplement parent survey; no prior exact passage certification.",
          "source_alias": "M09",
          "timestamps": [
            140.596825,
            246.044444,
            351.492063,
            456.939683,
            562.387302
          ]
        }
      ],
      "locked_or_prior_controls": [
        "Exact locked song-communication/textual-core evidence IDs to be read during analytical preparation; percentages only locate discovery images."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    },
    {
      "group_id": "MZ-FULL-07",
      "label": "Tsuki no Kame performance and authored-image forms",
      "claim_ids": [
        "MZ-AV-016",
        "MZ-AV-024",
        "MZ-AV-025",
        "MZ-AV-029",
        "MZ-AV-040"
      ],
      "purpose": "Compare stage/camera/performer pose states with authored graphic motifs. Test literal stillness and source-form equivalence while leaving sung calmness/danger as separate facets.",
      "passages": [
        {
          "alias": "M10",
          "logical_source_id": "1WmrTOKijFtOCAUZeN_T361MXAx6SBgDC",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ツキノカメ」 (秦谷美鈴 ソロ SSR)【学マス⧸学園アイドルマスタ⧸(Moon Turtle) Gakuen idolm@ster MV】-(1080p60).mp4",
          "sha256": "a88ad4fe405de061a3877d53cdbe238910e549a70bee1df9bbf0ef6039a73154",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            46,
            50,
            54,
            58,
            62,
            66,
            70,
            74
          ],
          "selection_note": "Rendered stage around prior orbital/hand-gesture excerpt.",
          "source_alias": "M10",
          "timestamps": [
            46,
            50,
            54,
            58,
            62,
            66,
            70,
            74
          ]
        },
        {
          "alias": "M11",
          "logical_source_id": "1yZf5-OSc870QyVOWvfMrwse1rT3ide5j",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「ツキノカメ」Official Music Video (HATSUBOSHI GAKUEN - Moon Turtle)-(1080p24).mp4",
          "sha256": "ebb51092cbbe799de4567f50e57a9b202e2c028983d1b3ad7d9c92c666cf9b61",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            90,
            96,
            102,
            108,
            114,
            120,
            126,
            132
          ],
          "selection_note": "Authored-MV form/motif discovery; not synchronized to M10.",
          "source_alias": "M11",
          "timestamps": [
            90,
            96,
            102,
            108,
            114,
            120,
            126,
            132
          ]
        }
      ],
      "locked_or_prior_controls": [
        "Tsuki no Kame communication/core; prior M10 dense visual excerpt; paired-source identity."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    },
    {
      "group_id": "MZ-FULL-08",
      "label": "VEIL stage and authored imagery",
      "claim_ids": [
        "MZ-AV-019",
        "MZ-AV-020",
        "MZ-AV-029",
        "MZ-AV-040",
        "MZ-AV-044",
        "MZ-AV-045"
      ],
      "purpose": "Expand previously sparse VEIL comparison with readable source-specific image states; distinguish celestial scale from proof of benevolence or final closure.",
      "passages": [
        {
          "alias": "M15",
          "logical_source_id": "1IcGLjifbxfTFEeS9T429VS-rJWPIT-60",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「VEIL」(秦谷美鈴 STEP3 SSR)【学マス⧸学園アイドルマスタ⧸ 学園偶像大師⧸ Gakuen idolm@ster MV】-(1080p60).mp4",
          "sha256": "7a9f3b58287c9a663b591130d2d7cb7554b3be1915731262144f93c03644c7c6",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            42,
            50,
            58,
            66,
            74,
            82,
            90,
            98
          ],
          "selection_note": "VEIL3DMV pose/framing/scale discovery.",
          "source_alias": "M15",
          "timestamps": [
            42,
            50,
            58,
            66,
            74,
            82,
            90,
            98
          ]
        },
        {
          "alias": "M16",
          "logical_source_id": "1f-LzucKPa0x6XuAN7wvoqwM4FG5Fao11",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「VEIL」Official Music Video (HATSUBOSHI GAKUEN - VEIL)-(1080p24).mp4",
          "sha256": "40950da9822dbb2755d298200668fd42d52f6fddeba0122a6d6ce9f63de76f72",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            48,
            60,
            72,
            84,
            96,
            108,
            120,
            132
          ],
          "selection_note": "VEIL authored-MV graphic world; source-form comparison only.",
          "source_alias": "M16",
          "timestamps": [
            48,
            60,
            72,
            84,
            96,
            108,
            120,
            132
          ]
        }
      ],
      "locked_or_prior_controls": [
        "CIDOL016 and locked core; prior candidate had four-point VEIL locators."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    },
    {
      "group_id": "MZ-FULL-09",
      "label": "Superlative and intimate-night contrast",
      "claim_ids": [
        "MZ-AV-018",
        "MZ-AV-029",
        "MZ-AV-030",
        "MZ-AV-031"
      ],
      "purpose": "Inspect scale/address and literal scene properties across Superlative and Yorunite. Audio-cover sources M14/M27 are surveyed as form controls, not emotional evidence.",
      "passages": [
        {
          "alias": "M13",
          "logical_source_id": "1_TvGBz4HD-xZeysP98HQyNKLXH9RtMyD",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Superlative」(秦谷美鈴 ソロ2 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
          "sha256": "9bedc9ad49821d1d13e2d3b9f130f386d51ea5f06cc94ad7339ecf96b6e9c3cb",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            66,
            72,
            78,
            84,
            90,
            96
          ],
          "selection_note": "Stage/address states.",
          "source_alias": "M13",
          "timestamps": [
            66,
            72,
            78,
            84,
            90,
            96
          ]
        },
        {
          "alias": "M21",
          "logical_source_id": "1Dnsksn6TEnzualJKSXeZEkzSMqoylzuv",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「ヨルニテ」Official Music Video (HATSUBOSHI GAKUEN - yorunite)-(1080p24).mp4",
          "sha256": "142bfc32dcf1e0d09f9fe4472cde7b4e13d8cff993dbefb3c125131b3eb79705",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            60,
            72,
            84,
            96,
            108,
            120
          ],
          "selection_note": "Yorunite authored images; check daylight/collage versus universal-night shorthand.",
          "source_alias": "M21",
          "timestamps": [
            60,
            72,
            84,
            96,
            108,
            120
          ]
        }
      ],
      "locked_or_prior_controls": [
        "Prior interpretation of dream-possession/non-imperial intimacy remains qualified unless actual modalities support it."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    },
    {
      "group_id": "MZ-FULL-10",
      "label": "Begrazia distributed foregrounding and source forms",
      "claim_ids": [
        "MZ-AV-021",
        "MZ-AV-022",
        "MZ-AV-023",
        "MZ-AV-037",
        "MZ-AV-038",
        "MZ-AV-040",
        "MZ-AV-045"
      ],
      "purpose": "Test local Misuzu foregrounding and redistribution among distinct performers against authored individual portraits/group composition. No total shot-share or universal mediation statistic.",
      "passages": [
        {
          "alias": "M17",
          "logical_source_id": "1UyUsSr7ZUed6Kh6oHtIsmyjo4GiWvLTo",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\4K HDR「Star-mine」(Begrazia SSR ユニット曲)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
          "sha256": "f1143c1aaa2ca5df6c577c1b9d27c88cc19208e0c6218441455547a8e5130430",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            62,
            66,
            70,
            74,
            78,
            82,
            86,
            90
          ],
          "selection_note": "Rendered trio framing, including local Misuzu and subsequent other-member foregrounding.",
          "source_alias": "M17",
          "timestamps": [
            62,
            66,
            70,
            74,
            78,
            82,
            86,
            90
          ]
        },
        {
          "alias": "M18",
          "logical_source_id": "1emxDRAvHC46s-v0x4eYFW1pCjdDGvIM9",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\初星学園 「Star-mine」Official Music Video (HATSUBOSHI GAKUEN - Star-mine)-(1080p24).mp4",
          "sha256": "d0ce84afef4bb91d1f20f15ecd02fe459f5a906cd6b64b9abda98e299f837fd6",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            72,
            76,
            80,
            84,
            88,
            92,
            96,
            100
          ],
          "selection_note": "Authored portrait masks/group composition; not claimed musically synchronized.",
          "source_alias": "M18",
          "timestamps": [
            72,
            76,
            80,
            84,
            88,
            92,
            96,
            100
          ]
        }
      ],
      "locked_or_prior_controls": [
        "Prior EXEC-MZ-M17/M18-PERFORMANCE; M09 communication/core for non-restoration intent."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    },
    {
      "group_id": "MZ-FULL-11",
      "label": "Kinetic and effort-themed repertoire controls",
      "claim_ids": [
        "MZ-AV-002",
        "MZ-AV-024",
        "MZ-AV-025",
        "MZ-AV-026",
        "MZ-AV-028",
        "MZ-AV-039"
      ],
      "purpose": "Compare changing visible pose/set states across ENDLESS DANCE, Howling and Gamushara. Distinguish a depicted effort gesture from a moral ideal and solo performance from static trio audio-cover form.",
      "passages": [
        {
          "alias": "M19",
          "logical_source_id": "170-Xv0Fu8C_tZsuJd8zPOD6eMoQzVZie",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ENDLESS DANCE」(秦谷美鈴 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
          "sha256": "51cd1eec16dab8fb63058e5d3fdc294265a45c44e06e2d3cb76637ab0d8b9192",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            34,
            40,
            46,
            52,
            58,
            64
          ],
          "selection_note": "ENDLESS DANCE performance discovery.",
          "source_alias": "M19",
          "timestamps": [
            34,
            40,
            46,
            52,
            58,
            64
          ]
        },
        {
          "alias": "M23",
          "logical_source_id": "1FD-G-EejV1b4YCNwfXdiTs4MC1y_fh4R",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR (秦谷美鈴 ソロ SSR)「Howling over the World」【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
          "sha256": "0fa235b1eb273707fbd33438a79b9b3cff2df3108d713d70c1758efb3c701fec",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            42,
            46,
            50,
            54,
            58,
            62
          ],
          "selection_note": "Howling solo floor/arm/industrial imagery.",
          "source_alias": "M23",
          "timestamps": [
            42,
            46,
            50,
            54,
            58,
            62
          ]
        },
        {
          "alias": "M24",
          "logical_source_id": "14TF8iaQLD4mibJIlLy1UZmx43m4LffTM",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「がむしゃらに行こう！」 (秦谷美鈴 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
          "sha256": "af4f7355ac382dce4772a63cf365cda05b20f429a0be573c699a320e867de01b",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            40,
            44,
            48,
            52,
            56,
            60
          ],
          "selection_note": "Gamushara desk/standing/graphic-set states.",
          "source_alias": "M24",
          "timestamps": [
            40,
            44,
            48,
            52,
            56,
            60
          ]
        }
      ],
      "locked_or_prior_controls": [
        "Dear026 textual control for authored pace; M26 survey for static-cover form. No sung-softness inference from images."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    },
    {
      "group_id": "MZ-FULL-12",
      "label": "Common and comic repertoire legibility",
      "claim_ids": [
        "MZ-AV-017",
        "MZ-AV-024",
        "MZ-AV-025",
        "MZ-AV-027",
        "MZ-AV-039",
        "MZ-AV-040"
      ],
      "purpose": "Broaden common-song comparisons through visible individual presentation, microphone/hand use, and comic interface/desk imagery. No attribution of heard timing.",
      "passages": [
        {
          "alias": "M12",
          "logical_source_id": "17qwFKYPq9dt5O9O8L-aWnu3d5zhNZRN0",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Campus mode!!」(秦谷美鈴 フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(1080p60).mp4",
          "sha256": "47bbe2204fa5f1a0bf2c371c8788c831b49a6c3b432af19ff233d639bafa0f82",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            42,
            50,
            58,
            66
          ],
          "selection_note": "Campus mode solo presentation.",
          "source_alias": "M12",
          "timestamps": [
            42,
            50,
            58,
            66
          ]
        },
        {
          "alias": "M20",
          "logical_source_id": "16up-So-St6oIqDkLO8fO5hmDcp675ras",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「初〈はじめ〉」 (秦谷美鈴 ソロ)【学マス⧸学園アイドルマスタ⧸ Gakuen idolm@ster MV】-(1080p60).mp4",
          "sha256": "05bfb52fef8398601a86d4db2920cdf8d4670ea2a6c739ece52336249aab0525",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            48,
            56,
            64,
            72
          ],
          "selection_note": "Hajime solo handheld-microphone presentation.",
          "source_alias": "M20",
          "timestamps": [
            48,
            56,
            64,
            72
          ]
        },
        {
          "alias": "M22",
          "logical_source_id": "1hoOWfl9Xf-XefaIRyTskrcUdHiQeOrNa",
          "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\04_MV_3DMV_AND_PERFORMANCE\\【学マス】「ミラクルナナウ(ﾟ∀ﾟ)！」秦谷美鈴【MV】4K-(1080p60).mp4",
          "sha256": "e13c304126711786c8bc9efedbc1dbb22c0df7b67a57dcb0676d6ade51a404c8",
          "video_stream_index": 0,
          "audio_stream_index": 1,
          "times_seconds": [
            36,
            40,
            44,
            48,
            52,
            56
          ],
          "selection_note": "Miracle Nanau graphic/interface/desk states.",
          "source_alias": "M22",
          "timestamps": [
            36,
            40,
            44,
            48,
            52,
            56
          ]
        }
      ],
      "locked_or_prior_controls": [
        "Common repertoire claims; M25 alternate/full-mix survey distinguished from M20 performed3DMV."
      ],
      "modality": "visual_stills",
      "analysis_limit": "Target requests are not observations. Stills do not certify continuous motion or listening. Source percentages/time positions do not imply homologous musical phrases."
    }
  ],
  "target_point_requests": 229,
  "parent_survey": {
    "sources": 27,
    "points_each": 12,
    "total_points": 324,
    "purpose": "Source-form and broad scene survey; not complete motion/audio coverage."
  },
  "inherited_trial": {
    "observation_record": {
      "path": "WORKSPACE/Gakuen Idolmaster/work/ave-targeted-trial-20260910/observations/misuzu.json",
      "sha256": "f9256a41652d11e71eec63a92ea89168f586c586f77261bdcb20ffd1209e20f9",
      "bytes": 412358
    },
    "delta": {
      "path": "WORKSPACE/Gakuen Idolmaster/work/ave-targeted-trial-20260910/observations/misuzu_delta.md",
      "sha256": "02d76f3c7b10828c47a2f6b6c337ba678304a1233af72bf1b739185a1fb42ea2",
      "bytes": 13237
    },
    "reuse_note": "Integrate previously observed tears/refusal/yawn precision with its original provenance. No repeat of identical final-frame refinements is requested."
  },
  "all_claim_ids_preserved": [
    "MZ-AV-001",
    "MZ-AV-002",
    "MZ-AV-003",
    "MZ-AV-004",
    "MZ-AV-005",
    "MZ-AV-006",
    "MZ-AV-007",
    "MZ-AV-008",
    "MZ-AV-009",
    "MZ-AV-010",
    "MZ-AV-011",
    "MZ-AV-012",
    "MZ-AV-013",
    "MZ-AV-014",
    "MZ-AV-015",
    "MZ-AV-016",
    "MZ-AV-017",
    "MZ-AV-018",
    "MZ-AV-019",
    "MZ-AV-020",
    "MZ-AV-021",
    "MZ-AV-022",
    "MZ-AV-023",
    "MZ-AV-024",
    "MZ-AV-025",
    "MZ-AV-026",
    "MZ-AV-027",
    "MZ-AV-028",
    "MZ-AV-029",
    "MZ-AV-030",
    "MZ-AV-031",
    "MZ-AV-032",
    "MZ-AV-033",
    "MZ-AV-034",
    "MZ-AV-035",
    "MZ-AV-036",
    "MZ-AV-037",
    "MZ-AV-038",
    "MZ-AV-039",
    "MZ-AV-040",
    "MZ-AV-041",
    "MZ-AV-042",
    "MZ-AV-043",
    "MZ-AV-044",
    "MZ-AV-045"
  ],
  "source_identity_authority": {
    "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
    "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
    "bytes": 516664
  },
  "new_observation_policy": "Only actually displayed new images will receive fresh observation entries. Computational audio is not listening; still sequences are not continuous-motion review. Source-form, text, measured mix descriptors, perception and interpretation remain separate.",
  "parent_normalization": "Added source_alias/timestamps copies for common extraction schema; original fields retained"
}
```

## Execute

Reconstruct the frozen modules from [the toolkit source document](TOOLKIT_SOURCE_AND_LICENSE.md), or use the existing tested toolkit source directory in the working evidence workspace. Save the fenced scripts below as UTF-8/LF files in a scripts directory beside toolkit/, evidence/, plans/, audit/ and candidate/. The complete original execution workspace, including command journals and actual image-tool receipt files, remains local alongside the Markdown delivery; raw artifacts are not embedded as media in these Markdown-only ZIPs. For a joint rerun use both character input lists/plans. For a character-only run select its aliases for source processing and omit operations involving absent sources. Set AVE_FFMPEG_BIN to your installed native FFmpeg directory. Changed runtime or code creates a new processing generation and must use new output directories.

The commands below describe the joint two-character execution and must be run one at a time, checking each result. Create evidence/, plans/, audit/ and candidate/ first, including candidate/07_SHINOSAWA_HIRO/SUPPORTING_DATA/ and candidate/11_HATAYA_MISUZU/SUPPORTING_DATA/. Install the frozen toolkit and its audio dependencies in a Python environment first (for example, python -m pip install -e "./toolkit[audio]"). The execution adapters use the recorded sources and plans; they are not a new general-purpose CLI.

```text
python scripts/process_corpus.py inventory
python scripts/process_corpus.py loudness --workers 3
python scripts/process_corpus.py features --workers 2
python scripts/process_corpus.py survey --workers 2
python scripts/targeted_frames.py hiro --workers 2
```

Checkpoint: the recorded Hiro targeted pass failed only for H24. If that failure recurs, retain the failed staging evidence, verify that the final H24 output directory was not admitted, and run the explicit full-origin recovery below. If the original targeted command succeeds on a different runtime, do not invent a recovery event or overwrite that successful run. Any other failure requires investigation before proceeding.

```text
python scripts/recover_targeted.py H24
```

After all planned Hiro outputs pass their source/PTS checks, continue with the Misuzu pass, its separately recorded locator repair, chapter calculations and audio comparisons. The audio-identity operation also needs the historical H04 trim input described in the Hiro packet.

```text
python scripts/targeted_frames.py misuzu --workers 2
python scripts/supplemental_frames.py
python scripts/measure_segments.py loudness --workers 2
python scripts/measure_segments.py features --workers 2
python scripts/audio_identity.py
python scripts/build_technical.py
```

The original execution scheduled dependent operations as prerequisite immutable runs became available. run_ready.py records that optional orchestration. build_technical.py expects the completed joint run families and renders their outputs; it does not create perceptual observations or audit results. A character-only run can use process_corpus.py --aliases and the matching targeted plan, but the joint audio-comparison and document-rendering helpers must be adapted for omitted sources. Any such adaptation belongs to a new recorded generation.

The fenced build_technical.py is the final documentation and reproduction generator, revised after the initial numerical render to improve these instructions. Its hash identifies this final file, not an archived snapshot of the initial renderer execution. The measurement and extraction adapters were unchanged; an independent audit separately recomputed every displayed pixel descriptor and recording-group reduction against the retained outputs.

The completed data audit verifies parameters against the source inventory and plans as well as checking hashes. The execution resume helper alone checks integrity of existing runs; it does not establish that their parameters match a changed request. Use fresh output directories after changing inputs, plans, parameters or code.

## Full chapter interval plan

Save as plans/misuzu-segments.json.

```json
{
  "schema": "misuzu.full_rebuild.chapter_intervals.v1",
  "character": "MISUZU",
  "count": 37,
  "clock": "Source-relative seconds under recorded origin0; these are inherited operational intervals, not new source-PTS speech alignment.",
  "label_cycle_intervals": 20,
  "container_marker_intervals": 17,
  "intervals": [
    {
      "character": "MISUZU",
      "alias": "M01",
      "chapter": 1,
      "label": "Dear001",
      "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
      "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1.1666666666666667,
      "end_s": 201.93333333333334,
      "start_seconds": 1.1666666666666667,
      "end_seconds": 201.93333333333334,
      "historical_start_frame": 35,
      "historical_end_frame": 6058,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M01-BOUNDARY-001",
        "frames/M01_frame_header_00.jpg",
        "frames/M01_frame_header_01.jpg",
        "adv_dear_hmsz_001.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M01",
      "chapter": 2,
      "label": "Dear002",
      "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
      "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 201.93333333333334,
      "end_s": 500.3666666666667,
      "start_seconds": 201.93333333333334,
      "end_seconds": 500.3666666666667,
      "historical_start_frame": 6058,
      "historical_end_frame": 15011,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M01-BOUNDARY-002",
        "frames/M01_frame_header_01.jpg",
        "frames/M01_frame_header_02.jpg",
        "adv_dear_hmsz_002.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M01",
      "chapter": 3,
      "label": "Dear003",
      "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
      "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 500.3666666666667,
      "end_s": 739.2666666666667,
      "start_seconds": 500.3666666666667,
      "end_seconds": 739.2666666666667,
      "historical_start_frame": 15011,
      "historical_end_frame": 22178,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M01-BOUNDARY-003",
        "frames/M01_frame_header_02.jpg",
        "frames/M01_frame_header_03.jpg",
        "adv_dear_hmsz_003.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M01",
      "chapter": 4,
      "label": "Dear004",
      "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
      "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 739.2666666666667,
      "end_s": 1006.7,
      "start_seconds": 739.2666666666667,
      "end_seconds": 1006.7,
      "historical_start_frame": 22178,
      "historical_end_frame": 30201,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M01-BOUNDARY-004",
        "frames/M01_frame_header_03.jpg",
        "frames/M01_frame_header_04.jpg",
        "adv_dear_hmsz_004.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M01",
      "chapter": 5,
      "label": "Dear005",
      "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
      "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1006.7,
      "end_s": 1260.2666666666667,
      "start_seconds": 1006.7,
      "end_seconds": 1260.2666666666667,
      "historical_start_frame": 30201,
      "historical_end_frame": 37808,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M01-BOUNDARY-005",
        "frames/M01_frame_header_04.jpg",
        "frames/M01_frame_header_05.jpg",
        "adv_dear_hmsz_005.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M01",
      "chapter": 6,
      "label": "Dear006",
      "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
      "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1260.2666666666667,
      "end_s": 1548.2666666666667,
      "start_seconds": 1260.2666666666667,
      "end_seconds": 1548.2666666666667,
      "historical_start_frame": 37808,
      "historical_end_frame": 46448,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M01-BOUNDARY-006",
        "frames/M01_frame_header_05.jpg",
        "frames/M01_frame_header_06.jpg",
        "adv_dear_hmsz_006.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M01",
      "chapter": 7,
      "label": "Dear007",
      "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
      "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1548.2666666666667,
      "end_s": 1790.1333333333334,
      "start_seconds": 1548.2666666666667,
      "end_seconds": 1790.1333333333334,
      "historical_start_frame": 46448,
      "historical_end_frame": 53704,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M01-BOUNDARY-007",
        "frames/M01_frame_header_06.jpg",
        "frames/M01_frame_header_07.jpg",
        "adv_dear_hmsz_007.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M01",
      "chapter": 8,
      "label": "Dear008",
      "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
      "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1790.1333333333334,
      "end_s": 2092.8333333333335,
      "start_seconds": 1790.1333333333334,
      "end_seconds": 2092.8333333333335,
      "historical_start_frame": 53704,
      "historical_end_frame": 62785,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M01-BOUNDARY-008",
        "frames/M01_frame_header_07.jpg",
        "frames/M01_frame_header_08.jpg",
        "adv_dear_hmsz_008.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M01",
      "chapter": 9,
      "label": "Dear009",
      "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
      "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 2092.8333333333335,
      "end_s": 2398.366666666667,
      "start_seconds": 2092.8333333333335,
      "end_seconds": 2398.366666666667,
      "historical_start_frame": 62785,
      "historical_end_frame": 71951,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M01-BOUNDARY-009",
        "frames/M01_frame_header_08.jpg",
        "frames/M01_frame_header_09.jpg",
        "adv_dear_hmsz_009.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M01",
      "chapter": 10,
      "label": "Dear010",
      "logical_source_id": "1Fw_4i3PsiFG-qE3FcpTNPQEH7ZwcVEkd",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
      "sha256": "f7b7c8e6dbdb7199a6ef99429bdf4380d5f7dae9d4e194338d5b398f2ee3f8be",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 2398.366666666667,
      "end_s": 2753.2,
      "start_seconds": 2398.366666666667,
      "end_seconds": 2753.2,
      "historical_start_frame": 71951,
      "historical_end_frame": 82596,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M01-BOUNDARY-010",
        "frames/M01_frame_header_09.jpg",
        "frames/M01_frame_header_10.jpg",
        "adv_dear_hmsz_010.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M02",
      "chapter": 11,
      "label": "Dear011",
      "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
      "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 0.0,
      "end_s": 242.0,
      "start_seconds": 0.0,
      "end_seconds": 242.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 0,
        "time_base": "1/1000",
        "start": 0,
        "start_time": "0.000000",
        "end": 242000,
        "end_time": "242.000000",
        "tags": {
          "title": "11話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M02.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M02",
      "chapter": 12,
      "label": "Dear012",
      "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
      "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 242.0,
      "end_s": 536.0,
      "start_seconds": 242.0,
      "end_seconds": 536.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 1,
        "time_base": "1/1000",
        "start": 242000,
        "start_time": "242.000000",
        "end": 536000,
        "end_time": "536.000000",
        "tags": {
          "title": "12話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M02.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M02",
      "chapter": 13,
      "label": "Dear013",
      "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
      "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 536.0,
      "end_s": 738.0,
      "start_seconds": 536.0,
      "end_seconds": 738.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 2,
        "time_base": "1/1000",
        "start": 536000,
        "start_time": "536.000000",
        "end": 738000,
        "end_time": "738.000000",
        "tags": {
          "title": "13話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M02.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M02",
      "chapter": 14,
      "label": "Dear014",
      "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
      "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 738.0,
      "end_s": 991.0,
      "start_seconds": 738.0,
      "end_seconds": 991.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 3,
        "time_base": "1/1000",
        "start": 738000,
        "start_time": "738.000000",
        "end": 991000,
        "end_time": "991.000000",
        "tags": {
          "title": "14話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M02.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M02",
      "chapter": 15,
      "label": "Dear015",
      "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
      "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 991.0,
      "end_s": 1226.0,
      "start_seconds": 991.0,
      "end_seconds": 1226.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 4,
        "time_base": "1/1000",
        "start": 991000,
        "start_time": "991.000000",
        "end": 1226000,
        "end_time": "1226.000000",
        "tags": {
          "title": "15話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M02.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M02",
      "chapter": 16,
      "label": "Dear016",
      "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
      "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1226.0,
      "end_s": 1634.0,
      "start_seconds": 1226.0,
      "end_seconds": 1634.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 5,
        "time_base": "1/1000",
        "start": 1226000,
        "start_time": "1226.000000",
        "end": 1634000,
        "end_time": "1634.000000",
        "tags": {
          "title": "16話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M02.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M02",
      "chapter": 17,
      "label": "Dear017",
      "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
      "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1634.0,
      "end_s": 1987.0,
      "start_seconds": 1634.0,
      "end_seconds": 1987.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 6,
        "time_base": "1/1000",
        "start": 1634000,
        "start_time": "1634.000000",
        "end": 1987000,
        "end_time": "1987.000000",
        "tags": {
          "title": "17話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M02.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M02",
      "chapter": 18,
      "label": "Dear018",
      "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
      "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1987.0,
      "end_s": 2177.0,
      "start_seconds": 1987.0,
      "end_seconds": 2177.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 7,
        "time_base": "1/1000",
        "start": 1987000,
        "start_time": "1987.000000",
        "end": 2177000,
        "end_time": "2177.000000",
        "tags": {
          "title": "18話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M02.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M02",
      "chapter": 19,
      "label": "Dear019",
      "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
      "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 2177.0,
      "end_s": 2428.0,
      "start_seconds": 2177.0,
      "end_seconds": 2428.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 8,
        "time_base": "1/1000",
        "start": 2177000,
        "start_time": "2177.000000",
        "end": 2428000,
        "end_time": "2428.000000",
        "tags": {
          "title": "19話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M02.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M02",
      "chapter": 20,
      "label": "Dear020",
      "logical_source_id": "1NyhdO7zo56LTuHdfmfV2kznkr7o8IEqD",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\秦谷美鈴  親愛度コミュ11～20話まとめ【学マス】-(720p60).mp4",
      "sha256": "5b5ab02b99076f25cd428e381e5809392b31ae187c5f09788a2a468f11c70972",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 2428.0,
      "end_s": 2791.0,
      "start_seconds": 2428.0,
      "end_seconds": 2791.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 9,
        "time_base": "1/1000",
        "start": 2428000,
        "start_time": "2428.000000",
        "end": 2791000,
        "end_time": "2791.000000",
        "tags": {
          "title": "20話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M02.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M03",
      "chapter": 21,
      "label": "Dear021",
      "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
      "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
      "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 0.0,
      "end_s": 310.0,
      "start_seconds": 0.0,
      "end_seconds": 310.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 0,
        "time_base": "1/1000",
        "start": 0,
        "start_time": "0.000000",
        "end": 310000,
        "end_time": "310.000000",
        "tags": {
          "title": "親愛度コミュ21話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M03.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M03",
      "chapter": 22,
      "label": "Dear022",
      "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
      "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
      "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 310.0,
      "end_s": 632.0,
      "start_seconds": 310.0,
      "end_seconds": 632.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 1,
        "time_base": "1/1000",
        "start": 310000,
        "start_time": "310.000000",
        "end": 632000,
        "end_time": "632.000000",
        "tags": {
          "title": "親愛度コミュ22話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M03.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M03",
      "chapter": 23,
      "label": "Dear023",
      "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
      "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
      "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 632.0,
      "end_s": 943.0,
      "start_seconds": 632.0,
      "end_seconds": 943.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 2,
        "time_base": "1/1000",
        "start": 632000,
        "start_time": "632.000000",
        "end": 943000,
        "end_time": "943.000000",
        "tags": {
          "title": "親愛度コミュ23話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M03.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M03",
      "chapter": 24,
      "label": "Dear024",
      "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
      "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
      "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 943.0,
      "end_s": 1393.0,
      "start_seconds": 943.0,
      "end_seconds": 1393.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 3,
        "time_base": "1/1000",
        "start": 943000,
        "start_time": "943.000000",
        "end": 1393000,
        "end_time": "1393.000000",
        "tags": {
          "title": "親愛度コミュ24話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M03.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M03",
      "chapter": 25,
      "label": "Dear025",
      "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
      "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
      "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1393.0,
      "end_s": 1770.0,
      "start_seconds": 1393.0,
      "end_seconds": 1770.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 4,
        "time_base": "1/1000",
        "start": 1393000,
        "start_time": "1393.000000",
        "end": 1770000,
        "end_time": "1770.000000",
        "tags": {
          "title": "親愛度コミュ25話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M03.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M03",
      "chapter": 26,
      "label": "Dear026",
      "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
      "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
      "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1770.0,
      "end_s": 2135.0,
      "start_seconds": 1770.0,
      "end_seconds": 2135.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 5,
        "time_base": "1/1000",
        "start": 1770000,
        "start_time": "1770.000000",
        "end": 2135000,
        "end_time": "2135.000000",
        "tags": {
          "title": "親愛度コミュ26話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M03.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M03",
      "chapter": 27,
      "label": "Dear027",
      "logical_source_id": "149ubZq2LgWA1zuE4U8dICF0X9bZvWv5w",
      "path": "LOCAL_USER/Downloads\\【学マス】 秦谷美鈴 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
      "sha256": "5d78050758fecdf8b961926ee2f1dbdaa7bea9894983d378fff40585a5125763",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 2135.0,
      "end_s": 2651.0,
      "start_seconds": 2135.0,
      "end_seconds": 2651.0,
      "boundary_method": "INHERITED_EMBEDDED_CONTAINER_CHAPTER_MARKERS",
      "historical_marker": {
        "id": 6,
        "time_base": "1/1000",
        "start": 2135000,
        "start_time": "2135.000000",
        "end": 2651000,
        "end_time": "2651.000000",
        "tags": {
          "title": "親愛度コミュ27話"
        }
      },
      "boundary_note": "Uploader/container chapter markers identify reproducible compilation segments. They are not freshly visually certified narrative starts, dialogue-only intervals or speech alignment. The next ED marker closes the final chapter.",
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/ave-full-rebuild-20260910/evidence/corpus.json",
        "sha256": "ebd5234c5ae45a08431222ddaa74e46e126e1fea3069b9c0be54c5057c19237e",
        "bytes": 516664
      },
      "provenance_field": "M03.prior_probe.chapters",
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M04",
      "chapter": 28,
      "label": "Dear028",
      "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
      "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 0.9666666666666667,
      "end_s": 329.8,
      "start_seconds": 0.9666666666666667,
      "end_seconds": 329.8,
      "historical_start_frame": 29,
      "historical_end_frame": 9894,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M04-BOUNDARY-028",
        "frames/M04_frame_header_00.jpg",
        "frames/M04_frame_header_01.jpg",
        "adv_dear_hmsz_028.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M04",
      "chapter": 29,
      "label": "Dear029",
      "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
      "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 329.8,
      "end_s": 723.5,
      "start_seconds": 329.8,
      "end_seconds": 723.5,
      "historical_start_frame": 9894,
      "historical_end_frame": 21705,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M04-BOUNDARY-029",
        "frames/M04_frame_header_01.jpg",
        "frames/M04_frame_header_02.jpg",
        "adv_dear_hmsz_029.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M04",
      "chapter": 30,
      "label": "Dear030",
      "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
      "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 723.5,
      "end_s": 1010.7333333333333,
      "start_seconds": 723.5,
      "end_seconds": 1010.7333333333333,
      "historical_start_frame": 21705,
      "historical_end_frame": 30322,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M04-BOUNDARY-030",
        "frames/M04_frame_header_02.jpg",
        "frames/M04_frame_header_03.jpg",
        "adv_dear_hmsz_030.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M04",
      "chapter": 31,
      "label": "Dear031",
      "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
      "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1010.7333333333333,
      "end_s": 1461.3333333333333,
      "start_seconds": 1010.7333333333333,
      "end_seconds": 1461.3333333333333,
      "historical_start_frame": 30322,
      "historical_end_frame": 43840,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M04-BOUNDARY-031",
        "frames/M04_frame_header_03.jpg",
        "frames/M04_frame_header_04.jpg",
        "adv_dear_hmsz_031.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M04",
      "chapter": 32,
      "label": "Dear032",
      "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
      "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1461.3333333333333,
      "end_s": 1787.1333333333334,
      "start_seconds": 1461.3333333333333,
      "end_seconds": 1787.1333333333334,
      "historical_start_frame": 43840,
      "historical_end_frame": 53614,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M04-BOUNDARY-032",
        "frames/M04_frame_header_04.jpg",
        "frames/M04_frame_header_05.jpg",
        "adv_dear_hmsz_032.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M04",
      "chapter": 33,
      "label": "Dear033",
      "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
      "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 1787.1333333333334,
      "end_s": 2162.3333333333335,
      "start_seconds": 1787.1333333333334,
      "end_seconds": 2162.3333333333335,
      "historical_start_frame": 53614,
      "historical_end_frame": 64870,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M04-BOUNDARY-033",
        "frames/M04_frame_header_05.jpg",
        "frames/M04_frame_header_06.jpg",
        "adv_dear_hmsz_033.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M04",
      "chapter": 34,
      "label": "Dear034",
      "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
      "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 2162.3333333333335,
      "end_s": 2525.9,
      "start_seconds": 2162.3333333333335,
      "end_seconds": 2525.9,
      "historical_start_frame": 64870,
      "historical_end_frame": 75777,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M04-BOUNDARY-034",
        "frames/M04_frame_header_06.jpg",
        "frames/M04_frame_header_07.jpg",
        "adv_dear_hmsz_034.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M04",
      "chapter": 35,
      "label": "Dear035",
      "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
      "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 2525.9,
      "end_s": 2748.0333333333333,
      "start_seconds": 2525.9,
      "end_seconds": 2748.0333333333333,
      "historical_start_frame": 75777,
      "historical_end_frame": 82441,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M04-BOUNDARY-035",
        "frames/M04_frame_header_07.jpg",
        "frames/M04_frame_header_08.jpg",
        "adv_dear_hmsz_035.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M04",
      "chapter": 36,
      "label": "Dear036",
      "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
      "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 2748.0333333333333,
      "end_s": 3418.1666666666665,
      "start_seconds": 2748.0333333333333,
      "end_seconds": 3418.1666666666665,
      "historical_start_frame": 82441,
      "historical_end_frame": 102545,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M04-BOUNDARY-036",
        "frames/M04_frame_header_08.jpg",
        "frames/M04_frame_header_09.jpg",
        "adv_dear_hmsz_036.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    },
    {
      "character": "MISUZU",
      "alias": "M04",
      "chapter": 37,
      "label": "Dear037",
      "logical_source_id": "1zZaheh3YRcrXMFCcWQIS-_Pxd32m3ChE",
      "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_11_HATAYA_MISUZU-20260910T061923Z-1-001\\11_HATAYA_MISUZU\\01_DEAR_ROUTE\\【学マス】秦谷美鈴　親愛度２８～３７話【アイドルコミュ STEP4 HIF】-(720p30).mp4",
      "sha256": "38500c9908eee6a44ab630fd6bf317ca1d37e3f4282995a2fb3d45ee2621638a",
      "video_stream_index": 0,
      "audio_stream_index": 1,
      "start_s": 3418.1666666666665,
      "end_s": 3818.8333333333335,
      "start_seconds": 3418.1666666666665,
      "end_seconds": 3818.8333333333335,
      "historical_start_frame": 102545,
      "historical_end_frame": 114565,
      "historical_fps": 30,
      "boundary_method": "INHERITED_PRIOR_EXECUTION_VISUALLY_SELECTED_CHAPTER_LABEL_CYCLE",
      "boundary_note": "Label fade has a few ambiguous low-opacity frames. Canonical reference selects earliest clearly legible chapter numeral in enlarged crop; do not interpret 1/30 s locator precision as semantic boundary certainty. Interchapter transitions up to next label are retained in preceding interval.",
      "historical_boundary_method": "directly inspected on-screen chapter-label onset reference frame to next onset reference; final end at label disappearance before uploader ending; frame-selected reproducible compilation segment, not original-game narrative frame boundary",
      "historical_evidence_locators": [
        "EXEC-MZ-M04-BOUNDARY-037",
        "frames/M04_frame_header_09.jpg",
        "frames/M04_frame_header_10.jpg",
        "adv_dear_hmsz_037.txt at locked commit 00d150a069a3ffa723a1ff264752ba242024caad"
      ],
      "provenance_file": {
        "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/work/misuzu/validated_intervals.json",
        "sha256": "94fafa8ab6d6759d58b51d4143c5513c81a2cb2ee45c3293c71b83210b63c4c1",
        "bytes": 27719
      },
      "review_status": "INHERITED_BOUNDARY_NOT_FRESHLY_REFINED_IN_FULL_REBUILD"
    }
  ],
  "boundary_authority": {
    "path": "WORKSPACE/Gakuen Idolmaster/work/targeted-av-execution-20260910/candidate/11_HATAYA_MISUZU/SUPPORTING_DATA/DEAR_SEGMENT_MEASUREMENTS.md",
    "sha256": "faed77347bd13569fcf3565d2fb8019f47626f2233bd834fe01b67386d440aab",
    "bytes": 242991
  },
  "exclusions": [
    {
      "alias": "M01",
      "intervals_seconds": [
        [
          0,
          1.1666666666666667
        ],
        [
          2753.2,
          2917.958821
        ]
      ]
    },
    {
      "alias": "M02",
      "intervals_seconds": [
        [
          2791,
          2991.240998
        ]
      ]
    },
    {
      "alias": "M03",
      "intervals_seconds": [
        [
          2651,
          2835.0
        ]
      ]
    },
    {
      "alias": "M04",
      "intervals_seconds": [
        [
          0,
          0.9666666666666667
        ],
        [
          3818.8333333333335,
          4048.631293
        ]
      ]
    }
  ],
  "metric_limits": "Every interval includes the selected mixed audio stream and compilation material: other speakers, BGM, choices, UI, transitions and possible performance inserts. Rerunning the new toolkit does not turn inherited boundaries into fresh observations or isolated actor measurements."
}
```

## Adaptive locator repair

A separate 12-point M02 selection repairs the original conflict window, which landed on the Temari/temporary-unit discussion. The original 229-point plan is preserved. Run supplemental_frames.py after the M02 survey index exists; its new frames are separately labeled, not silently substituted for the first selection.

```json
{
  "alias": "M02",
  "timestamps": [
    738,
    760,
    781,
    804,
    827,
    850,
    873,
    900,
    922,
    946,
    970,
    990
  ],
  "reason": "Initial M02 targeted choice landed on Temari/temporary-unit discussion; new bounded request uses documented Dear014 nonrestoration conflict locator",
  "not_a_new_general_pass": true,
  "script_sha256": "2711c93929b2424986885b6e2d58cb28cf992d44ff7987bd50bb1664641c244a",
  "original_targeted_plan_unchanged": true
}
```

### runtime.py

SHA-256: `28dde808ab8de80f7933801ce2c166166eb521d1908375cc43baf140ed49d1a3`.

```python
"""Explicit Windows execution adapter; no measurement algorithm changes."""
from pathlib import Path
import os, sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'toolkit'))
sys.dont_write_bytecode=True
sys.stdout.reconfigure(encoding='utf-8')
NATIVE=Path(os.environ.get('AVE_FFMPEG_BIN','LOCAL_DRIVE_C/ProgramData/chocolatey/lib/ffmpeg/tools/ffmpeg/bin'))
if NATIVE.is_dir(): os.environ['PATH']=str(NATIVE)+os.pathsep+os.environ.get('PATH','')
from avevidence import common
native_run=common.run
POLICY={'schema':'ave.full_rebuild.runtime.v1','timeout_seconds':1800,'ffprobe_frame_threads':8,
        'ffmpeg_decode_threads':4,'binary_directory':str(NATIVE),
        'changes':'Native binaries, bounded decoder threads and longer command timeout only; toolkit measurement and validation logic unchanged',
        'review_rule':'Computation is not listening; generated frames are not reviewed until actually presented and inspected'}
def run(argv,**kwargs):
    args=[str(x) for x in argv]
    name=Path(args[0]).stem.lower()
    if name in ['ffmpeg','ffprobe']:
        binary=NATIVE/(name+('.exe' if os.name=='nt' else ''))
        if binary.is_file(): args[0]=str(binary)
        if name=='ffprobe' and '-show_frames' in args: args[1:1]=['-threads','8']
        if name=='ffmpeg' and '-i' in args: args[1:1]=['-threads','4']
    kwargs['timeout']=max(kwargs.get('timeout',180),1800)
    return native_run(args,**kwargs)
common.run=run
native_finish=common.finish_run
def finish(stage,operation,sources,parameters=None,metadata=None):
    common.write_json(Path(stage)/'execution-adapter.json',dict(POLICY,script_sha256=common.sha256(__file__)))
    return native_finish(stage,operation,sources+[common.file_record(__file__,'execution_adapter')],parameters,metadata)
common.finish_run=finish
```

### process_corpus.py

SHA-256: `7824f9d10027ec15b0cf87fd41cc1c20a17da2f7e5830a029804a10fb7a7ab6c`.

```python
"""Run toolkit operations on the frozen 60-source scope; fresh immutable runs.

Full-source feature cues are analysis intervals, not subtitles or speech turns.
All output provenance is original-media bound. Resumption verifies existing runs.
"""
import argparse, csv, json, math, traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from datetime import datetime, timezone
import runtime
from runtime import ROOT
from avevidence import common, audio, visual, inventory
E=ROOT/'evidence'
def read(p): return common.read_json(p)
def note(event,**kw): print(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(),event=event,**kw)),flush=True)
def exists(out):
    if out.exists():
        inventory.verify_run(out,verify_sources=True)
        note('verified_existing_run',path=str(out)); return True
    return False
def run_one(source,mode):
    alias=source['alias']; note('start',alias=alias,mode=mode)
    if mode=='loudness':
        out=E/'loudness'/alias
        if not exists(out): audio.measure_audio(source['path'],out,stream_index=source['audio_stream'])
    elif mode=='features':
        out=E/'features'/alias
        if not exists(out):
            metric=read(E/'loudness'/alias/'metrics.json')
            sel=metric['selection']; assert sel['status']=='COMPLETE'
            cue=E/'feature-inputs'/(alias+'.csv'); cue.parent.mkdir(exist_ok=True)
            rows=[{'cue_index':'whole_source','start_seconds':sel['requested_start_seconds'],'end_seconds':sel['requested_end_seconds'],'name':'complete_final_mix','text_plain':'Whole decoded audio interval; not a speech cue','parent_source_sha256':source['sha256'],'clock':audio.CLOCK,'origin_seconds':metric['origin_seconds']}]
            with cue.open('w',encoding='utf-8',newline='') as f:
                w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader();w.writerows(rows)
            audio.cue_features(source['path'],cue,out,stream_index=source['audio_stream'],profile='music',pitch=False,confirm_isolated_speech=False)
    elif mode=='survey':
        out=E/'survey-frames'/alias
        times=[round(source['duration_seconds']*(i+.5)/12,6) for i in range(12)]
        if not exists(out): visual.extract_frames(source['path'],out,mode='exact',timestamps=times,width=1280,stream_index=source['video_stream'])
        contacts=E/'survey-contacts'/alias
        if not exists(contacts): visual.contact_sheets(out,contacts,columns=3,rows=4,thumb_width=640)
    note('complete',alias=alias,mode=mode)
def admit():
    sources=read(E/'corpus.json'); rows=[]
    for r in sources:
        rows.append(dict(logical_source_id=r['logical_source_id'],materialization_id=r['alias']+'_CURRENT',path=r['path'],expected_sha256=r['sha256'],selected_streams={'video':r['video_stream'],'audio':r['audio_stream']},required_modalities=['audio','motion','visual_stills'],required_points_seconds=[round(r['duration_seconds']*(i+.5)/12,6) for i in range(12)],preferred=True,evidence_weight_group=r['alias'],title=r['role'],notes=r['materialization_note']))
    config=E/'inventory-config.json'; common.write_json(config,{'schema':'ave.inventory.config.v1','sources':rows,'required_logical_source_ids':[r['logical_source_id'] for r in sources]})
    if not exists(E/'inventory'): inventory.inventory(config,E/'inventory')
    note('inventory_complete',sources=len(sources))
def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['inventory','loudness','features','survey']);p.add_argument('--workers',type=int,default=2);p.add_argument('--aliases',nargs='*');a=p.parse_args()
    if a.mode=='inventory': return admit()
    sources=read(E/'corpus.json');sources=[s for s in sources if not a.aliases or s['alias'] in a.aliases]
    errors=[]
    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        fs={pool.submit(run_one,s,a.mode):s for s in sources}
        for f in as_completed(fs):
            try:f.result()
            except Exception as exc:
                row=dict(alias=fs[f]['alias'],mode=a.mode,error=str(exc),traceback=traceback.format_exc());errors.append(row);note('ERROR',**row)
    common.write_json(ROOT/'audit'/('processing-'+a.mode+'.json'),dict(mode=a.mode,count=len(sources),errors=errors))
    if errors: raise SystemExit(1)
if __name__=='__main__':main()
```

### run_ready.py

SHA-256: `e550e6be0a4c6fa627945885b60d45a3b665a3629bff3c03a86ad774dd22d555`.

```python
"""Schedule dependent operations only after prerequisite immutable runs exist."""
import argparse, time, traceback
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import runtime
from runtime import ROOT
from avevidence import common
from process_corpus import run_one, note
def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['features','targeted']);p.add_argument('--character',choices=['hiro','misuzu']);p.add_argument('--workers',type=int,default=2);a=p.parse_args()
    corpus={r['alias']:r for r in common.read_json(ROOT/'evidence/corpus.json')}
    times=defaultdict(set)
    if a.mode=='targeted':
        from targeted_frames import one
        plan=common.read_json(ROOT/'plans'/(a.character+'-review-plan.json'))
        for g in plan['groups']:
            for r in g['passages']:times[r['source_alias']].update(r['timestamps'])
        pending=set(times);prereq='survey-frames'
    else: pending=set(corpus);prereq='loudness'
    errors=[];finished=[];deadline=time.monotonic()+7200
    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        active={}
        while pending or active:
            for f,alias in list(active.items()):
                if f.done():
                    try:f.result();finished.append(alias)
                    except Exception as exc:
                        row={'alias':alias,'error':str(exc),'traceback':traceback.format_exc()};errors.append(row);note('ERROR',**row)
                    del active[f]
            ready=[alias for alias in sorted(pending) if (ROOT/'evidence'/prereq/alias/'run.json').is_file()]
            for alias in ready[:max(0,a.workers-len(active))]:
                f=pool.submit(one,corpus[alias],sorted(times[alias])) if a.mode=='targeted' else pool.submit(run_one,corpus[alias],'features')
                active[f]=alias;pending.remove(alias)
            if time.monotonic()>deadline and pending:
                errors.append({'missing_prerequisites':sorted(pending)});pending.clear()
            if pending or active:time.sleep(10)
    common.write_json(ROOT/'audit'/('ready-'+a.mode+('-'+a.character if a.character else '')+'.json'),{'completed':sorted(finished),'errors':errors})
    if errors:raise SystemExit(1)
if __name__=='__main__':main()
```

### targeted_frames.py

SHA-256: `c4ef201df1957422abc94f9aa5cd1cee6d552cb6a5a9d27309ca421b3d63788f`.

```python
"""Claim-directed exact frames, reusing a verified survey decoder index.

Index reuse is explicitly journaled, hash bound, and never counted as a new
decoder pass. Input seek retains original PTS, checked by the toolkit.
"""
import argparse, contextvars, json, subprocess, traceback
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import runtime
from runtime import ROOT
from avevidence import common, visual, inventory
from process_corpus import note, exists
E=ROOT/'evidence'
CTX=contextvars.ContextVar('frame_index_reuse',default=None)
native=visual.run
def run(argv,**kwargs):
    args=[str(x) for x in argv];c=CTX.get()
    if c and '-show_frames' in args:
        journal=common._journal.get()
        if journal is not None:journal.append({'argv':args,'execution':'REUSED_VERIFIED_SURVEY_FRAME_INDEX','returncode':0,'parent_commands_sha256':c['commands_sha256'],'parent_run_sha256':c['run_sha256'],'stdout':c['index']['stdout'],'stderr':''})
        return subprocess.CompletedProcess(args,0,c['index']['stdout'],'')
    if c and '-filter_script:v' in args:
        k=args.index('-i');args[k:k]=['-ss',str(c['seek'])]
    return native(args,**kwargs)
visual.run=run
def member(indices):
    pts=CTX.get()['pts']
    if len(indices)==1:return f'eq(pts,{pts[indices[0]]})'
    mid=len(indices)//2
    return f'if(lt(pts,{pts[indices[mid]]}),{member(indices[:mid])},{member(indices[mid:])})'
visual._membership=member
finish=visual.finish_run
def with_reuse(stage,operation,sources,parameters=None,metadata=None):
    c=CTX.get()
    if c:
        common.write_json(Path(stage)/'index-reuse.json',{'parent_run_sha256':c['run_sha256'],'parent_commands_sha256':c['commands_sha256'],'source_sha256':c['source_sha256'],'input_seek_seconds':c['seek'],'frame_index_entries':len(c['pts']),'script_sha256':common.sha256(__file__),'policy':'Verified prior complete frame index reused; original integer PTS selector; expected/actual frame PTS and image counts asserted by toolkit'})
        sources=sources+[common.file_record(c['base']/'run.json','cached_frame_index_manifest'),common.file_record(c['base']/'commands.json','cached_frame_index_commands')]
    return finish(stage,operation,sources,parameters,metadata)
visual.finish_run=with_reuse
def one(source,times):
    alias=source['alias'];out=E/'targeted-frames'/alias;base=E/'survey-frames'/alias
    note('targeted_start',alias=alias,points=len(times))
    if not exists(out):
        inventory.verify_run(base,verify_sources=True)
        manifest=common.read_json(base/'run.json');assert manifest['sources'][0]['sha256']==source['sha256']
        commands=common.read_json(base/'commands.json');index=next(x for x in commands if '-show_frames' in x['argv'])
        pts=[int(x['pts']) for x in json.loads(index['stdout'])['frames']]
        c={'base':base,'run_sha256':common.sha256(base/'run.json'),'commands_sha256':common.sha256(base/'commands.json'),'source_sha256':source['sha256'],'index':index,'pts':pts,'seek':max(0,min(times)-1)}
        token=CTX.set(c)
        try:visual.extract_frames(source['path'],out,mode='exact',timestamps=times,width=1280,stream_index=source['video_stream'])
        finally:CTX.reset(token)
    contacts=E/'targeted-contacts'/alias
    if not exists(contacts):visual.contact_sheets(out,contacts,columns=3,rows=4,thumb_width=640)
    note('targeted_complete',alias=alias,points=len(times))
def main():
    p=argparse.ArgumentParser();p.add_argument('character',choices=['hiro','misuzu']);p.add_argument('--workers',type=int,default=2);p.add_argument('--aliases',nargs='*');a=p.parse_args()
    plan=common.read_json(ROOT/'plans'/(a.character+'-review-plan.json'));by=defaultdict(set)
    for group in plan['groups']:
        for passage in group['passages']:by[passage['source_alias']].update(passage['timestamps'])
    corpus={r['alias']:r for r in common.read_json(E/'corpus.json')};errors=[]
    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        fs={pool.submit(one,corpus[alias],sorted(times)):alias for alias,times in by.items() if not a.aliases or alias in a.aliases}
        for f in as_completed(fs):
            try:f.result()
            except Exception as exc:
                row={'alias':fs[f],'error':str(exc),'traceback':traceback.format_exc()};errors.append(row);note('ERROR',**row)
    common.write_json(ROOT/'audit'/('processing-targeted-'+a.character+'.json'),{'errors':errors,'character':a.character})
    if errors:raise SystemExit(1)
if __name__=='__main__':main()
```

### recover_targeted.py

SHA-256: `8a50ccba5d8614c5c4405b6f533d3afbd8d1b811b7e4faca90e9e18196c79816`.

```python
"""Explicit full-decode retry when a sought targeted extraction fails."""
import argparse
from pathlib import Path
import runtime
from runtime import ROOT
from avevidence import common, visual
from process_corpus import exists, note
def main():
    p=argparse.ArgumentParser();p.add_argument('alias');a=p.parse_args();alias=a.alias
    char='hiro' if alias.startswith('H') else 'misuzu';plan=common.read_json(ROOT/'plans'/(char+'-review-plan.json'))
    times=sorted({t for g in plan['groups'] for r in g['passages'] if r['source_alias']==alias for t in r['timestamps']})
    src=next(r for r in common.read_json(ROOT/'evidence/corpus.json') if r['alias']==alias)
    out=ROOT/'evidence/targeted-frames'/alias
    finish=visual.finish_run
    def with_recovery(stage,operation,sources,parameters=None,metadata=None):
        common.write_json(Path(stage)/'recovery.json',{'alias':alias,'method':'Fresh full source frame index and decode from origin, without input seek or index reuse; all toolkit strict decoder and PTS checks retained','reason':'Earlier sought extraction failed; exact codec cause not inferred from the truncated error record','script_sha256':common.sha256(__file__)})
        return finish(stage,operation,sources+[common.file_record(__file__,'full_decode_recovery_adapter')],parameters,metadata)
    visual.finish_run=with_recovery
    if not exists(out):visual.extract_frames(src['path'],out,mode='exact',timestamps=times,width=1280,stream_index=src['video_stream'])
    contacts=ROOT/'evidence/targeted-contacts'/alias
    if not exists(contacts):visual.contact_sheets(out,contacts,columns=3,rows=4,thumb_width=640)
    note('full_decode_recovery_complete',alias=alias,points=len(times))
if __name__=='__main__':main()
```

### supplemental_frames.py

SHA-256: `2711c93929b2424986885b6e2d58cb28cf992d44ff7987bd50bb1664641c244a`.

```python
"""Adaptive locator repair: M02 Dear014 after the first selection missed it."""
import json
from pathlib import Path
import runtime
from runtime import ROOT
from avevidence import common, visual, inventory
import targeted_frames as tf
from process_corpus import exists, note
def main():
    alias='M02';times=[738,760,781,804,827,850,873,900,922,946,970,990]
    src=next(r for r in common.read_json(ROOT/'evidence/corpus.json') if r['alias']==alias)
    base=ROOT/'evidence/survey-frames'/alias;out=ROOT/'evidence/supplemental-frames'/alias
    if not exists(out):
        inventory.verify_run(base,verify_sources=True)
        assert common.read_json(base/'run.json')['sources'][0]['sha256']==src['sha256']
        commands=common.read_json(base/'commands.json');index=next(x for x in commands if '-show_frames' in x['argv'])
        c={'base':base,'run_sha256':common.sha256(base/'run.json'),'commands_sha256':common.sha256(base/'commands.json'),'source_sha256':src['sha256'],'index':index,'pts':[int(x['pts']) for x in json.loads(index['stdout'])['frames']],'seek':min(times)-1}
        token=tf.CTX.set(c)
        try:visual.extract_frames(src['path'],out,mode='exact',timestamps=times,width=1280,stream_index=src['video_stream'])
        finally:tf.CTX.reset(token)
    contacts=ROOT/'evidence/supplemental-contacts'/alias
    if not exists(contacts):visual.contact_sheets(out,contacts,columns=3,rows=4,thumb_width=640)
    common.write_json(ROOT/'evidence/supplemental-selection.json',{'alias':alias,'timestamps':times,'reason':'Initial M02 targeted choice landed on Temari/temporary-unit discussion; new bounded request uses documented Dear014 nonrestoration conflict locator','not_a_new_general_pass':True,'script_sha256':common.sha256(__file__),'original_targeted_plan_unchanged':True})
    note('supplemental_complete',alias=alias,points=len(times))
if __name__=='__main__':main()
```

### measure_segments.py

SHA-256: `da5333b7d4552ced0fbbbaf81a2f56bb568cf39f01651ee79c0f379764f6f0fe`.

```python
"""Batch toolkit-defined measurements on inherited operational chapter windows.

One native decode per source is shared across independent selections. Each row
uses unchanged toolkit _selection/_slice/_loudness, and records both identities.
This explicitly versioned batch adapter is not a shipped toolkit command.
"""
import argparse, csv, traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import runtime
from runtime import ROOT
from avevidence import audio, common
from process_corpus import note, exists
E=ROOT/'evidence';PLAN=ROOT/'plans/misuzu-segments.json'
def one(alias,mode):
    corpus={r['alias']:r for r in common.read_json(E/'corpus.json')};src=corpus[alias]
    windows=[r for r in common.read_json(PLAN)['intervals'] if r['alias']==alias]
    assert all(r['sha256']==src['sha256'] for r in windows)
    note('segment_start',alias=alias,mode=mode,count=len(windows))
    if mode=='loudness':
        out=E/'segment-loudness'/alias
        if not exists(out):
            with common.output_transaction(out,[src['path'],PLAN]) as stage:
                source=common.probe_source(src['path']);stream=common.select_stream(source,'audio',src['audio_stream'])
                assert source['sha256']==src['sha256'];results=[]
                with audio._scratch(stage) as scratch:
                    decoded=audio._decode(source,stream,scratch,'source')
                    for window in windows:
                        a,b=window['start_seconds'],window['end_seconds']
                        common.interval(a,b,decoded['segments'][-1]['source_end_seconds'])
                        selection=audio._selection(decoded,a,b);measurements=None;identity=None
                        if selection['status']=='COMPLETE':
                            selected=audio._slice(decoded,selection,scratch/'selected.f64le')
                            measurements=audio._loudness(selected);identity=audio._identity(selected)
                            selected['raw_path'].unlink()
                        results.append({'chapter':window['chapter'],'label':window['label'],'alias':alias,'parent_source_sha256':source['sha256'],'parent_stream_index':stream['index'],'clock':audio.CLOCK,'origin_seconds':source['origin_seconds'],'selection':selection,'selected_identity':identity,'measurements':measurements,'boundary_method':window['boundary_method'],'boundary_note':window['boundary_note'],'perceptual_review':'NOT_PERFORMED'})
                        note('segment_row_complete',alias=alias,chapter=window['chapter'],status=selection['status'])
                    common.write_json(stage/'segments.json',{'schema':'ave.full_rebuild.segment_metrics.v1','parent_source_sha256':source['sha256'],'parent_stream_index':stream['index'],'clock':audio.CLOCK,'origin_seconds':source['origin_seconds'],'parent_identity':audio._identity(decoded),'parent_segments':decoded['segments'],'rows':results,'adapter_policy':'Single original decode; unchanged toolkit selection, native slicing and independent loudness filtering per window; inherited compilation windows not speech turns','perceptual_review':'NOT_PERFORMED'})
                common.finish_run(stage,'measure_audio_regions',[source,common.file_record(PLAN,'inherited_chapter_interval_plan'),common.file_record(__file__,'batch_segment_adapter')],{'stream_index':stream['index'],'interval_count':len(windows)},{'result_file':'segments.json'})
    else:
        out=E/'segment-features'/alias
        if not exists(out):
            source=common.probe_source(src['path']);cue=E/'feature-inputs'/(alias+'-chapters.csv');cue.parent.mkdir(exist_ok=True)
            rows=[{'cue_index':r['label'],'start_seconds':r['start_seconds'],'end_seconds':r['end_seconds'],'name':'chapter_final_mix','text_plain':r['boundary_method'],'parent_source_sha256':src['sha256'],'clock':audio.CLOCK,'origin_seconds':source['origin_seconds']} for r in windows]
            with cue.open('w',encoding='utf-8',newline='') as f:
                w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
            audio.cue_features(src['path'],cue,out,stream_index=src['audio_stream'],profile='music',pitch=False,confirm_isolated_speech=False)
    note('segment_complete',alias=alias,mode=mode)
def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['loudness','features']);p.add_argument('--workers',type=int,default=2);a=p.parse_args();errors=[]
    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        fs={pool.submit(one,alias,a.mode):alias for alias in ['M01','M02','M03','M04']}
        for f in as_completed(fs):
            try:f.result()
            except Exception as exc:
                row={'alias':fs[f],'error':str(exc),'traceback':traceback.format_exc()};errors.append(row);note('ERROR',**row)
    common.write_json(ROOT/'audit'/('processing-segments-'+a.mode+'.json'),{'errors':errors})
    if errors:raise SystemExit(1)
if __name__=='__main__':main()
```

### audio_identity.py

SHA-256: `ce28a88b7be8c8e4c4803f2ffd15949e22c49e896cc7305a9422a5f0dcda8b06`.

```python
"""Strict audio object tests; no perceptual or near-equivalence inference."""
from pathlib import Path
import json, traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
import runtime
from runtime import ROOT
from avevidence import audio, common
from process_corpus import exists, note
E=ROOT/'evidence'
PAIRS=[('H12','H14'),('H15','H16'),('H17','H18'),('H28','H29'),('H32','H33'),('M10','M11'),('M13','M14'),('M15','M16'),('M17','M18'),('M20','M25'),('H19','M12')]
def one(pair):
    corpus={r['alias']:r for r in common.read_json(E/'corpus.json')};a,b=pair;out=E/'audio-comparisons'/(a+'-'+b)
    if not exists(out):audio.compare_audio(corpus[a]['path'],corpus[b]['path'],out,a_stream=corpus[a]['audio_stream'],b_stream=corpus[b]['audio_stream'])
    report=common.read_json(out/'comparison.json');note('audio_comparison',a=a,b=b,status=report['comparison_status'])
def h04_check():
    full=next(r for r in common.read_json(E/'corpus.json') if r['alias']=='H04')
    old=common.read_json(ROOT.parent/'targeted-av-execution-20260910/work/local_identity.json');trim=next(r for r in old if r['alias']=='H04')
    assert common.sha256(trim['path'])==trim['sha256']
    for label,path in [('H04-original',full['path']),('H04-trim',trim['path'])]:
        out=E/'audio-preservation'/label
        if not exists(out):audio.clip_audio(path,out,stream_index=1,start=3160,end=3205,pad=0)
    waves=[]
    for label in ['H04-original','H04-trim']:
        folder=E/'audio-preservation'/label
        files=list(folder.glob('*.wav'));assert len(files)==1;waves.append(files[0])
    out=E/'audio-comparisons/H04-original-trim-bounded'
    if not exists(out):audio.compare_audio(waves[0],waves[1],out,a_stream=0,b_stream=0)
    note('h04_bounded_comparison',status=common.read_json(out/'comparison.json')['comparison_status'])
    common.write_json(E/'audio-identity-plan.json',{'same_title_pairs':PAIRS,'h04_check':{'full_source_sha256':full['sha256'],'trim_source_sha256':trim['sha256'],'source_window':[3160,3205],'derivative_window':[0,45],'scope':'Revalidate native sample/channel preservation in a retained late passage; prior whole retained packet prefix audit remains inherited','full_object_equivalence':'NOT_CLAIMED'},'review_rule':'No listening; DIFFERENT is strict object inequality, not perceptual difference; MATCH is bounded native audio identity only'})
def main():
    errors=[]
    with ThreadPoolExecutor(max_workers=2) as pool:
        fs={pool.submit(one,p):p for p in PAIRS}
        for f in as_completed(fs):
            try:f.result()
            except Exception as exc:errors.append({'pair':fs[f],'error':str(exc),'traceback':traceback.format_exc()})
    h04_check()
    common.write_json(ROOT/'audit/processing-audio-identity.json',{'errors':errors})
    if errors:raise SystemExit(1)
if __name__=='__main__':main()
```

### build_technical.py

SHA-256: `99ca3d61586e6d101360e68cac3533ad3c94d241a550510f454597214e9cbf5f`.

```python
"""Render the complete fresh technical results as Markdown only.

This generator leaves analytical documents to the character reviewers. Tables
retain source identities, clocks, decoder sample counts and methodological scope.
"""
from pathlib import Path
import hashlib, json, statistics, sys
import numpy as np
from PIL import Image
import runtime
from runtime import ROOT
from avevidence import common
E=ROOT/'evidence'
FOLDERS={'HIRO':'07_SHINOSAWA_HIRO','MISUZU':'11_HATAYA_MISUZU'}
def read(p):return common.read_json(p)
def cell(x):
    if x is None:return 'unavailable'
    if isinstance(x,float):return format(x,'.15g')
    if isinstance(x,bool):return str(x).lower()
    return str(x).replace('|','\\|').replace('\n',' ')
def table(headers,rows):return '\n'.join(['| '+' | '.join(map(cell,headers))+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(map(cell,r))+' |' for r in rows])
def write(p,lines):p.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
def block(x):return ['```json',json.dumps(x,ensure_ascii=False,indent=2),'```','']
def visual_results(corpus):
    all_rows=[]
    for src in corpus:
        for mode in ['survey','targeted','supplemental']:
            folder=E/(mode+'-frames')/src['alias']
            if not folder.exists():
                assert mode in ['targeted','supplemental']
                continue
            manifest=read(folder/'frames.json');prior=None
            for r in manifest['rows']:
                path=folder/r['path'];assert common.sha256(path)==r['sha256']
                with Image.open(path) as im:a=np.asarray(im.convert('RGB'),dtype=np.float64)/255
                high=a.max(axis=2);low=a.min(axis=2);sat=np.divide(high-low,high,out=np.zeros_like(high),where=high>0)
                difference=None if prior is None or prior.shape!=a.shape else float(np.mean(np.abs(a-prior)))
                row=dict(alias=src['alias'],mode=mode,source_sha256=src['sha256'],frame_id=r['frame_id'],source_seconds=r['source_seconds'],requested_seconds=r['requested_seconds'],source_pts=r['source_pts'],source_time_base=r['source_time_base'],source_frame_index=r['source_frame_index'],frame_sha256=r['sha256'],brightness_mean=float(a.mean()),hsv_saturation_mean=float(sat.mean()),adjacent_selected_rgb_difference=difference,generated_review_status='NOT_INFERRED_FROM_EXTRACTION')
                all_rows.append(row);prior=a
    common.write_json(E/'visual-measurements.json',{'schema':'ave.full_rebuild.visual_point_metrics.v1','method':'Whole PNG RGB channel arithmetic mean/255; HSV saturation=(max-min)/max with black0; whole RGB absolute difference between consecutive selected images within same source/run. No motion or cut inference.','rows':all_rows})
    return all_rows
def metrics_table(sources,metrics):
    rows=[]
    for s in sources:
        a=s['alias'];m=metrics[a];v=m['measurements']['loudnorm_input'];sel=m['selection'];identity=m['identity']
        rows.append([a,sel['requested_start_seconds'],sel['requested_end_seconds'],identity['sample_frames'],identity['sample_rate_hz'],identity['channels'],identity['channel_layout'],v['integrated_lufs'],v['loudness_range_lu'],v['true_peak_dbtp'],v['integrated_gating_threshold_lufs']])
    return table(['Alias','Audio start s','Audio end s','Native sample frames','Hz','Channels','Layout','Integrated LUFS','LRA LU','True peak dBTP','Gate LUFS'],rows)
def feature_tables(sources,features):
    rows=[];counts=[]
    for s in sources:
        f=features[s['alias']];r=f['rows'][0];assert r['status']=='COMPLETE'
        for c in r['per_channel']:
            rows.append([s['alias'],c['channel_index'],c['rms_dbfs'],c['sample_peak_dbfs'],c['zero_crossing_rate'],c['spectral_centroid_hz_median'],c['spectral_rolloff85_hz_median'],c['low_energy_frame_fraction']])
            counts.append([s['alias'],c['channel_index'],c['sample_frames'],c['frame_length'],c['hop_length'],c['analysis_frames'],c['nonempty_spectral_frames'],c['pitch']['status']])
    return [table(['Alias','Channel index','RMS dBFS','Sample peak dBFS','Zero-crossing fraction','Median centroid Hz','Median 85% rolloff Hz','Frame fraction below -45 dBFS'],rows),'',table(['Alias','Channel','Samples','Frame samples','Hop samples','Complete frames','Nonempty spectral frames','F0 status'],counts),'']
def source_document(sources,admitted,dest):
    rows=[]
    for s in sources:
        a=admitted[s['alias']];v=next(x for x in a['streams'] if x['index']==s['video_stream']);au=next(x for x in a['streams'] if x['index']==s['audio_stream'])
        rows.append([s['alias'],s['logical_source_id'],s['sha256'],a['size_bytes'],a['origin_seconds'],a['duration_seconds'],v.get('width'),v.get('height'),v.get('avg_frame_rate'),v.get('time_base'),au.get('sample_rate'),au.get('channels'),au.get('channel_layout')])
    lines=['# Current source verification — AVE-FULL-20260910','',f'{len(sources)} configured source IDs were freshly hashed and admitted with the toolkit. Byte identity binds these inputs to prior recorded retrieval identities; it does not authenticate the underlying upload or prove inspection. No new Drive metadata fetch is claimed. The checked-out repository baseline remains `400234a42d5811847367de94e6e8229fe816e99b`; no repository integration was performed.','',
        'H04 uses the full original for this revision. Earlier trimmed-object measurements retain their original population and are historical. Retained packet-prefix equivalence was established previously; it does not make whole-object durations or whole-source measurements equal. Attached pictures are excluded from moving-video selection.','',table(['Alias','Recorded Drive ID','Current SHA-256','Bytes','Clock origin s','Canonical end s','Width','Height','Average fps','Video time base','Audio Hz','Channels','Layout'],rows),'',
        'Canonical seconds = original presentation timestamp minus the recorded source origin. Container duration, stream presentation bounds and decoded audio endpoints are distinct. All selected indices are absolute stream indices. Full fresh source metadata follows; the original filenames, classes and historical status fields remain in the source manifest.','']
    for s in sources:
        a=admitted[s['alias']]
        lines += ['## '+s['alias']+' — '+s['role'],'']+block({'alias':s['alias'],'recorded_drive_id':s['logical_source_id'],'current_path':s['path'],'filename':Path(s['path']).name,'current_sha256':s['sha256'],'size_bytes':a['size_bytes'],'prior_expected_sha256':s['prior_expected_sha256'],'materialization_note':s['materialization_note'],'origin_seconds':a['origin_seconds'],'origin_basis':a['origin_basis'],'canonical_duration_seconds':a['duration_seconds'],'format_duration_seconds':a['format_duration_seconds'],'duration_basis':a['duration_basis'],'duration_uncertainty':a['duration_uncertainty'],'stream_timeline_bounds':a['stream_timeline_bounds'],'selected_streams':a['selected_streams'],'streams':a['streams']})
    write(dest/'FULL_REBUILD_SOURCE_VERIFICATION.md',lines)
def measurements_document(sources,metrics,features,dest):
    lines=['# Whole-source native-channel measurements — AVE-FULL-20260910','',f'Fresh toolkit measurements cover all {len(sources)} authorized source records for this character. Each row measures the full decoded final mix. These are computational observations, not direct listening or isolated character-voice measurements.','',
        'Integrated loudness, LRA, true peak and gating threshold come from FFmpeg loudnorm input reports; no normalized output was saved. Source timings and native PCM hashes are checked independently. The `music` feature profile specifies a common window length (2048/22050 seconds) for every source, including dialogue; it is not a genre label. Native channels are measured separately, without resampling or downmix. The whole-source analysis cue is not a transcript cue.','',metrics_table(sources,metrics),'',
        'LRA is a gated measure of this final mix and interval. It is not the retired RMS P90/P10 ratio, a performer’s expressive range, a comparison of physical capacities or an experimentalism score. Different source lengths, BGM, stage inserts, effects, mastering, uploader openings and other speakers affect these results.','',
        '## Per-channel full-mix descriptors','',
        'RMS and sample peak use native float64 PCM. Spectral medians use complete uncentered Hann windows and exclude zero-energy spectra. Zero crossings do not identify speech. The low-energy fraction counts complete windows below −45 dBFS; it is not a silence, breath or pause duration. F0 is deliberately not requested because no speaker-isolated signal was established.','']+feature_tables(sources,features)+['## PCM and run identity','',table(['Alias','Decoded native PCM SHA-256','PCM bytes','Coverage','Missing s','Loudness result SHA-256','Feature result SHA-256'],[[s['alias'],metrics[s['alias']]['identity']['pcm_sha256'],metrics[s['alias']]['identity']['pcm_bytes'],metrics[s['alias']]['selection']['status'],metrics[s['alias']]['selection']['missing_seconds'],common.sha256(E/'loudness'/s['alias']/'metrics.json'),common.sha256(E/'features'/s['alias']/'features.json')] for s in sources]),'',
        '## Complete numerical records','',
        'The following records preserve declared versus actual sample boundaries, raw nonfinite filter strings, the signed-16-bit conversion used only by FFmpeg volumedetect, and exact counts. Null is unavailable, not a zero measurement. The float64 per-channel sample peak above is separate from the quantized volumedetect peak.','']
    for s in sources:
        a=s['alias'];lines+=['### '+a,'']+block({'loudness':metrics[a],'native_channel_features':features[a]})
    write(dest/'FULL_REBUILD_MEASUREMENTS.md',lines)
def visual_document(sources,rows,dest):
    subset=[r for r in rows if r['alias'] in {s['alias'] for s in sources}]
    lines=['# Source-PTS visual samples — AVE-FULL-20260910','',
        'Survey requests use twelve equal-duration strata and select each stratum center. The first decoded source frame at or after the request is retained, with its actual integer PTS, time base and global frame index. Targeted requests come from the declared claim review plan. They are deliberately selected examples, not a random sample or continuous review. Extraction checks every selected output against the decoded index. Targeted runs reuse the hash-verified survey index except H24, whose sought extraction failed and whose successful retry freshly decoded/indexed from source origin. No failed output is counted.','',
        'The following pixel descriptors are automated whole-frame measurements. Brightness is the arithmetic mean of all encoded RGB channel values divided by 255. Saturation is per-pixel HSV (max−min)/max, with black 0, then averaged. These are not color-managed physical luminance. Selected-frame differences compare whole PNG RGB arrays; spacing and frame dimensions are part of the input. UI, backgrounds and uploader additions remain included. No motion speed, pose quality, scene-cut count or acting judgment is inferred.','',table(['Alias','Survey requests','Targeted requests','Supplemental requests','Distinct source PTS','Survey mean RGB brightness','Survey mean HSV saturation'],[[s['alias'],len([r for r in subset if r['alias']==s['alias'] and r['mode']=='survey']),len([r for r in subset if r['alias']==s['alias'] and r['mode']=='targeted']),len([r for r in subset if r['alias']==s['alias'] and r['mode']=='supplemental']),len({r['source_pts'] for r in subset if r['alias']==s['alias']}),statistics.mean(r['brightness_mean'] for r in subset if r['alias']==s['alias'] and r['mode']=='survey'),statistics.mean(r['hsv_saturation_mean'] for r in subset if r['alias']==s['alias'] and r['mode']=='survey')] for s in sources]),'',
        'Actual presentation and observation accounting is recorded separately in [review accounting](FULL_REBUILD_REVIEW_ACCOUNTING.md) and [claim review](FULL_REBUILD_CLAIM_REVIEW.md). A generated sample remains unreviewed unless that separate record establishes presentation and a bounded observation.','']
    for s in sources:
        a=s['alias'];lines+=['## '+a,'',f'Original source SHA-256: `{s["sha256"]}`.','',table(['Run','Frame ID','Requested s','Actual source s','PTS','Time base','Source frame index','PNG SHA-256','RGB mean','HSV S mean','Prior selected RGB difference'],[[r['mode'],r['frame_id'],r['requested_seconds'],r['source_seconds'],r['source_pts'],r['source_time_base'],r['source_frame_index'],r['frame_sha256'],r['brightness_mean'],r['hsv_saturation_mean'],r['adjacent_selected_rgb_difference']] for r in subset if r['alias']==a]),'']
    write(dest/'FULL_REBUILD_VISUAL_SAMPLES.md',lines)
def comparison_document(char,sources,metrics,dest):
    groups={'principal_3dmv':['H12','H15','H17'],'common_3dmv':['H19','H20','H21','H22','H23','H25']} if char=='HIRO' else {'principal_3dmv':['M10','M13','M15'],'common_3dmv':['M12','M19','M20','M22','M23','M24']}
    lines=['# Recording-form comparisons — AVE-FULL-20260910','',
        'These comparisons preserve the separation of in-game 3DMV, authored MV, static/full-mix presentation, song communication and derivative montage. Each complete recording is a different measurement population. Same title does not establish matched singing, temporal alignment, independent performance or audio equivalence.','',
        ('Hiro’s existing three principal and six common 3DMV groups are retained exactly. ' if char=='HIRO' else 'For descriptive organization, three principal solo 3DMVs are compared with six solo common-repertoire recordings. Star-mine is excluded from these solo groups because it is a shared ensemble source. These are new explicit groups, not recovered historical calculations. ')+
        'Each group statistic gives equal weight to recording-level descriptors; these are arithmetic summaries of displayed decibel/LU measures, not pooled loudness, significance tests, independent performances or artist rankings. The small selected corpus and varying edits prevent causal claims.','']
    rows=[]
    for group,aliases in groups.items():
        for feature in ['integrated_lufs','loudness_range_lu','true_peak_dbtp']:
            values=[metrics[a]['measurements']['loudnorm_input'][feature] for a in aliases];assert all(v is not None for v in values)
            rows.append([group,', '.join(aliases),len(aliases),feature,statistics.mean(values),statistics.median(values),min(values),max(values)])
    lines += [table(['Group','Members','n','Recording-level field','Equal-source mean','Median','Minimum','Maximum'],rows),'',
        'The undefined experimental proxy remains retired. RMS P90/P10 ratios in earlier records are retained as historical values, with their silence/floor problem documented; they are not used here. The new LRA column has a different estimator and population definition and cannot retroactively validate that ratio or a genre claim. Beat/chroma/tonnetz results were not regenerated by this toolkit and remain explicitly inherited.','']
    pairs=[('H12','H14'),('H15','H16'),('H17','H18'),('H28','H29'),('H32','H33')] if char=='HIRO' else [('M10','M11'),('M13','M14'),('M15','M16'),('M17','M18'),('M20','M25')]
    lines+=['## Same-title different-form records','',table(['Source A','Source B','Decoded duration A s','Decoded duration B s','Integrated LUFS A','Integrated LUFS B','LRA A LU','LRA B LU'],[[a,b,metrics[a]['decoded_audio_seconds'],metrics[b]['decoded_audio_seconds'],metrics[a]['measurements']['loudnorm_input']['integrated_lufs'],metrics[b]['measurements']['loudnorm_input']['integrated_lufs'],metrics[a]['measurements']['loudnorm_input']['loudness_range_lu'],metrics[b]['measurements']['loudnorm_input']['loudness_range_lu']] for a,b in pairs]),'',
        'The duration differences alone make these whole-recording populations unequal. They neither prove nor disprove shared musical passages. No automatic speech/song alignment or near-equivalence is claimed. Visual form observations are discussed in the music close reading. Strict native-sample comparisons, where executed, are recorded separately in [audio identity tests](FULL_REBUILD_AUDIO_IDENTITY.md).','']
    common.write_json(E/('group-reductions-'+char.lower()+'.json'),{'groups':groups,'rows':rows,'same_title_pairs':pairs})
    write(dest/'FULL_REBUILD_COMPARISONS.md',lines)
def segment_document(dest):
    plan=read(ROOT/'plans/misuzu-segments.json');rows=[];details=[]
    for alias in ['M01','M02','M03','M04']:
        report=read(E/'segment-loudness'/alias/'segments.json');features=read(E/'segment-features'/alias/'features.json')
        for r in report['rows']:
            v=r['measurements']['loudnorm_input'];s=r['selection'];p=next(p for p in plan['intervals'] if p['chapter']==r['chapter']);f=next(x for x in features['rows'] if x['cue_index']==r['label'])
            rows.append([r['label'],alias,s['requested_start_seconds'],s['requested_end_seconds'],s['parts'][0]['source_start_seconds'],s['parts'][-1]['source_end_seconds'],r['selected_identity']['sample_frames'],v['integrated_lufs'],v['loudness_range_lu'],v['true_peak_dbtp'],r['boundary_method']])
            details+=['## '+r['label'],'']+block({'operational_boundary':p,'loudness':r,'native_channel_features':f})
    assert len(rows)==37
    write(dest/'FULL_REBUILD_DEAR_SEGMENTS.md',['# All 37 chapter-associated intervals — AVE-FULL-20260910','',
        'The new toolkit generation freshly measures all 37 operational intervals. Twenty boundaries retain the prior visually chosen label-cycle convention (M01/M04); seventeen retain embedded compilation-marker windows (M02/M03). No equal-duration chapter division is used. These are not fresh semantic chapter onsets or aligned speech turns. Exact stored decimal bounds make the calculation repeatable; ambiguous fades and compilation editing limit their narrative precision.','',
        'One native decode per source feeds independent half-open selections. Both endpoint sample indices use ceil; tables distinguish requested bounds from actual retained sample-onset bounds. Only complete audio coverage is measured. BGM, other speakers, effects and uploader matter within each operational window remain in the mix; no acoustic component is isolated or inferred from caption labels. Chapter features use the same native-channel profile as whole-source features.','',table(['Chapter','Alias','Requested start s','Requested end s','Retained start s','Retained end s','Sample frames','Integrated LUFS','LRA LU','True peak dBTP','Inherited boundary method'],rows),'']+details)
def identity_document(char,dest):
    pairs=read(E/'audio-identity-plan.json')['same_title_pairs'];prefix='H' if char=='HIRO' else 'M';rows=[];details=[]
    for a,b in pairs:
        if not (a.startswith(prefix) or b.startswith(prefix)):continue
        report=read(E/'audio-comparisons'/(a+'-'+b)/'comparison.json')
        rows.append([a,b,report['comparison_status'],report['native_decoded_samples_equal'],report['channel_layout_comparison'],report['canonical_timing_equal_within_source_granularity'],report['timing_tolerance_seconds']])
        details+=['## '+a+' / '+b,'']+block(report)
    lines=['# Strict audio identity checks — AVE-FULL-20260910','',
        'The toolkit compares native decoded ordered float64 sample bytes, sample rate/count, known channel layout and canonical audio timing. It does not align songs, tolerate gain/codec differences, perform listening or test perceptual similarity. DIFFERENT means these whole recordings fail strict identity; it does not mean the musical passage sounds different. Equal titles and shared repertoire do not make these recordings equivalent or independent replications.','',table(['A','B','Strict result','Native samples equal','Layout','Canonical timing equal','Timing tolerance s'],rows),'']
    if char=='HIRO':
        report=read(E/'audio-comparisons/H04-original-trim-bounded/comparison.json');records=[]
        for label in ['H04-original','H04-trim']:records.append(read(E/'audio-preservation'/label/'audio.json'))
        lines+=['## H04 retained passage and WAV preservation','',
            'Both materializations were independently clipped at original source seconds [3160, 3205). Each WAV has its own source-to-derivative sample mapping and internal native-sample preservation verification. The resulting derivative clocks span [0, 45). A strict comparison of these WAVs tests the same retained passage; it does not assert whole-object equality. The full original extends beyond the historical trim, so its whole-source population remains different. Prior complete retained encoded-packet prefix equality is carried forward as historical verification.','']+block({'strict_bounded_comparison':report,'source_to_WAV_records':records})
    lines+=details
    write(dest/'FULL_REBUILD_AUDIO_IDENTITY.md',lines)
def toolkit_source(dest):
    paths=sorted((ROOT/'toolkit/avevidence').glob('*.py'))
    for name in ['pyproject.toml','README.md','LICENSE','LICENSE.md']:
        p=ROOT/'toolkit'/name
        if p.exists():paths.append(p)
    paths += sorted((ROOT/'toolkit/LICENSES').glob('*.txt'))
    lines=['# Frozen toolkit runtime source and license','',
        'Reconstruct each file at the indicated relative path under toolkit/. Exact SHA-256 values bind UTF-8 source bytes; save with LF line endings and the final newline shown in the original source. This is AV Evidence Toolkit 1.0.0 plus the explicitly identified trial WAV layout patch, not an unmodified copy of the published 1.0.0 release. The required runtime modules, package metadata, README and licenses are embedded below. The tested source tree, including tests and additional documentation, remains in the working evidence directory. The previously published AV_Evidence_Toolkit_1.0.0.zip has SHA-256 646110fe05f1fed908dbc1388a72c51e7015b440b161dac87b353c5348f4eb6b and does not include this trial patch; no new standalone toolkit ZIP is implied by this character-packet delivery.','']
    for p in paths:
        source=p.read_text(encoding='utf-8');fence='````' if p.suffix=='.md' else '```'
        lines+=['## '+p.relative_to(ROOT/'toolkit').as_posix(),'',f'SHA-256: `{common.sha256(p)}`.','',fence+('python' if p.suffix=='.py' else 'toml' if p.suffix=='.toml' else 'markdown' if p.suffix=='.md' else 'text'),source.removesuffix('\n'),fence,'']
    write(dest/'TOOLKIT_SOURCE_AND_LICENSE.md',lines)
def methods_document(sources,dest):
    env=read(E/'inventory/run.json')['environment'];scripts=['runtime.py','process_corpus.py','run_ready.py','targeted_frames.py','recover_targeted.py','supplemental_frames.py','measure_segments.py','audio_identity.py','build_technical.py']
    lines=['# Methods and reproduction — AVE-FULL-20260910','',
        'Toolkit: AV Evidence Toolkit 1.0.0 plus the separately tested native mono/stereo WAV layout patch from the targeted trial. The original 1.0.0 ZIP is unchanged. This revision uses explicit execution adapters for Windows binaries, bounded decoder threads, longer timeouts, verified frame-index reuse, and batch chapter selections. The source measurement formulas remain those of the frozen toolkit; batch selection is separately auditable.','',
        'The audio patch preserves known mono/stereo layout in WAVEFORMATEXTENSIBLE without changing PCM payload bytes; unknown layouts stay unknown. It does not add direct listening, voice separation or continuous video perception. The isolated copied suite passed 98 tests on Windows. Linux execution was not repeated.','',
        '## Runtime and implementation hashes','']+block(env)+['## Scope and clocks','',
        'All original source IDs, expected input hashes and exact selected streams are retained below. Current preferred H04 is the full original. File paths are acquisition locations and may be replaced during reproduction only with objects of the exact recorded hash. Toolkit admission verifies the bytes again. Every run records command arguments/results, source identity, parameters, output hashes and environment; immutable runs are verified before reuse.','',
        'Whole-source audio uses the actual first-to-last decoded sample interval, not a guessed video duration. Native sample count/rate/channel order are preserved. Missing timestamp regions remain explicit. Native PCM is float64; source files are never normalized or overwritten. Caption/analysis interval source binding proves the coordinate system, not an audible speaker or transcript correctness. All new feature F0 is NOT_REQUESTED.','',
        'Survey frames: 12 stratum-center requests per source; targeted frames: declared comparison plans. Full source-frame PTS indexing verifies geometry and monotonic timestamps. Exact mode selects the first frame at/after each request, which matters for 60000/1001 fps material. Requested and actual times remain separate. Targeted execution reuses the full survey index by its run and command-record hashes, then selects original PTS after seeking; actual selected PTS must match. Index reuse is explicitly journaled, not a second decoding pass. No HDR conversion, arbitrary rotation or unsupported geometry repair is silently introduced.','',
        'Perceptual accounting separates prepared outputs, actual displayed images, authored observations, inherited findings and unavailable modalities. Image tool response files verify presentation artifacts; they do not prove every interpretation. Viewing contact sheets provides sampled still observations, never interval-duration motion coverage. No direct listening or continuous playback is certified in this revision.','',
        '## Reproduction inputs','',
        'Save the following list as this character’s corpus input. For the joint scripts below, concatenate the two character lists into evidence/corpus.json. The duration_seconds/prior_probe fields are inherited acquisition metadata used to choose nominal survey requests; fresh admission and decoded sample bounds, recorded elsewhere, govern interpretation.','']+block(sources)+[
        'Save the following review plan as plans/'+sources[0]['character'].lower()+'-review-plan.json. Only declared timestamp requests feed extraction; purpose text is an analytical plan, not an observation.','']+block(read(ROOT/'plans'/(sources[0]['character'].lower()+'-review-plan.json')))+[
        '## Execute','',
        'Reconstruct the frozen modules from [the toolkit source document](TOOLKIT_SOURCE_AND_LICENSE.md), or use the existing tested toolkit source directory in the working evidence workspace. Save the fenced scripts below as UTF-8/LF files in a scripts directory beside toolkit/, evidence/, plans/, audit/ and candidate/. The complete original execution workspace, including command journals and actual image-tool receipt files, remains local alongside the Markdown delivery; raw artifacts are not embedded as media in these Markdown-only ZIPs. For a joint rerun use both character input lists/plans. For a character-only run select its aliases for source processing and omit operations involving absent sources. Set AVE_FFMPEG_BIN to your installed native FFmpeg directory. Changed runtime or code creates a new processing generation and must use new output directories.','',
        'The commands below describe the joint two-character execution and must be run one at a time, checking each result. Create evidence/, plans/, audit/ and candidate/ first, including candidate/07_SHINOSAWA_HIRO/SUPPORTING_DATA/ and candidate/11_HATAYA_MISUZU/SUPPORTING_DATA/. Install the frozen toolkit and its audio dependencies in a Python environment first (for example, python -m pip install -e "./toolkit[audio]"). The execution adapters use the recorded sources and plans; they are not a new general-purpose CLI.','',
        '```text','python scripts/process_corpus.py inventory','python scripts/process_corpus.py loudness --workers 3','python scripts/process_corpus.py features --workers 2','python scripts/process_corpus.py survey --workers 2','python scripts/targeted_frames.py hiro --workers 2','```','',
        'Checkpoint: the recorded Hiro targeted pass failed only for H24. If that failure recurs, retain the failed staging evidence, verify that the final H24 output directory was not admitted, and run the explicit full-origin recovery below. If the original targeted command succeeds on a different runtime, do not invent a recovery event or overwrite that successful run. Any other failure requires investigation before proceeding.','',
        '```text','python scripts/recover_targeted.py H24','```','',
        'After all planned Hiro outputs pass their source/PTS checks, continue with the Misuzu pass, its separately recorded locator repair, chapter calculations and audio comparisons. The audio-identity operation also needs the historical H04 trim input described in the Hiro packet.','',
        '```text','python scripts/targeted_frames.py misuzu --workers 2','python scripts/supplemental_frames.py','python scripts/measure_segments.py loudness --workers 2','python scripts/measure_segments.py features --workers 2','python scripts/audio_identity.py','python scripts/build_technical.py','```','',
        'The original execution scheduled dependent operations as prerequisite immutable runs became available. run_ready.py records that optional orchestration. build_technical.py expects the completed joint run families and renders their outputs; it does not create perceptual observations or audit results. A character-only run can use process_corpus.py --aliases and the matching targeted plan, but the joint audio-comparison and document-rendering helpers must be adapted for omitted sources. Any such adaptation belongs to a new recorded generation.','',
        'The fenced build_technical.py is the final documentation and reproduction generator, revised after the initial numerical render to improve these instructions. Its hash identifies this final file, not an archived snapshot of the initial renderer execution. The measurement and extraction adapters were unchanged; an independent audit separately recomputed every displayed pixel descriptor and recording-group reduction against the retained outputs.','',
        'The completed data audit verifies parameters against the source inventory and plans as well as checking hashes. The execution resume helper alone checks integrity of existing runs; it does not establish that their parameters match a changed request. Use fresh output directories after changing inputs, plans, parameters or code.','']
    if sources[0]['character']=='MISUZU':
        lines+=['## Full chapter interval plan','', 'Save as plans/misuzu-segments.json.','']+block(read(ROOT/'plans/misuzu-segments.json'))
        lines+=['## Adaptive locator repair','',
            'A separate 12-point M02 selection repairs the original conflict window, which landed on the Temari/temporary-unit discussion. The original 229-point plan is preserved. Run supplemental_frames.py after the M02 survey index exists; its new frames are separately labeled, not silently substituted for the first selection.','']+block(read(E/'supplemental-selection.json'))
    else:
        trim=next(r for r in read(ROOT.parent/'targeted-av-execution-20260910/work/local_identity.json') if r['alias']=='H04')
        lines+=['## Optional H04 trim comparison input','',
            'Only the bounded original/trim comparison needs this earlier derivative. audio_identity.py reads this list from the sibling targeted-av-execution-20260910/work/local_identity.json; reconstruct that small input or explicitly adapt the lookup to your retained derivative. Replace the path only after checking its exact hash. Omitting the derivative leaves this comparison unperformed and does not block original-source measurements.','']+block([trim])
    for name in scripts:
        p=ROOT/'scripts'/name
        if p.exists():lines+=['### '+name,'',f'SHA-256: `{common.sha256(p)}`.','', '```python',p.read_text(encoding='utf-8').rstrip(),'```','']
    write(dest/'FULL_REBUILD_METHODS_AND_REPRODUCTION.md',lines)
def main():
    corpus=read(E/'corpus.json');admitted={s['materialization_id'].removesuffix('_CURRENT'):s for s in read(E/'inventory/inventory.json')['sources']}
    for char in ['hiro','misuzu']:
        wanted={}
        for group in read(ROOT/'plans'/(char+'-review-plan.json'))['groups']:
            for passage in group['passages']:
                wanted.setdefault(passage['source_alias'],set()).update(passage['timestamps'])
        for alias,times in wanted.items():
            result=read(E/'targeted-frames'/alias/'frames.json')
            assert sorted(times)==[r['requested_seconds'] for r in result['rows']],alias
    for source in corpus:assert len(read(E/'survey-frames'/source['alias']/'frames.json')['rows'])==12
    assert len(read(E/'supplemental-frames/M02/frames.json')['rows'])==12
    metrics={s['alias']:read(E/'loudness'/s['alias']/'metrics.json') for s in corpus}
    features={s['alias']:read(E/'features'/s['alias']/'features.json') for s in corpus}
    for s in corpus:
        assert metrics[s['alias']]['parent_source_sha256']==s['sha256']==features[s['alias']]['parent_source_sha256']
        assert metrics[s['alias']]['selection']['status']=='COMPLETE'
    vr=visual_results(corpus)
    for char,folder in FOLDERS.items():
        sources=[s for s in corpus if s['character']==char];dest=ROOT/'candidate'/folder/'SUPPORTING_DATA'
        source_document(sources,admitted,dest);measurements_document(sources,metrics,features,dest);visual_document(sources,vr,dest);comparison_document(char,sources,metrics,dest);identity_document(char,dest);toolkit_source(dest)
        if char=='MISUZU':segment_document(dest)
        methods_document(sources,dest)
    common.write_json(E/'technical-render.json',{'sources':len(corpus),'whole_source_metrics':len(metrics),'whole_source_features':len(features),'visual_request_rows':len(vr),'status':'RENDERED_AWAITING_INDEPENDENT_FINAL_AUDIT'})
if __name__=='__main__':main()
```
