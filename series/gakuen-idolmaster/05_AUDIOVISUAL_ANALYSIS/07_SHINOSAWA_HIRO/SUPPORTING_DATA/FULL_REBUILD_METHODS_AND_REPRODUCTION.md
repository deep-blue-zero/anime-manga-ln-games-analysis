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
    "alias": "H01",
    "logical_source_id": "1UELlTgEu9lKMysQKjnLbt4MEUg9XWcbi",
    "character": "HIRO",
    "role": "Dear 001–010 / STEP1",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\01_DEAR_ROUTE\\【学マス】篠澤広　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
    "sha256": "d0d161a97a05993a3cb85e33b6b6c0c3c9aa9dba10eb4a26bdfb12ae651d23e3",
    "bytes": 147467932,
    "duration_seconds": 2660.472744,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "d0d161a97a05993a3cb85e33b6b6c0c3c9aa9dba10eb4a26bdfb12ae651d23e3",
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
          "mime_codec_string": "avc1.64001f",
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
          "duration_ts": 40863744,
          "duration": "2660.400000",
          "bit_rate": "304569",
          "bits_per_raw_sample": "8",
          "nb_frames": "79812",
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
          "duration_ts": 117326848,
          "duration": "2660.472744",
          "bit_rate": "127999",
          "nb_frames": "114577",
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
          "duration_ts": 239442547,
          "duration": "2660.472744",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\01_DEAR_ROUTE\\【学マス】篠澤広　親愛度１～１０話【アイドルコミュ】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "2660.472744",
        "size": "147467932",
        "bit_rate": "443433",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【学マス】篠澤広　親愛度１～１０話【アイドルコミュ】",
          "artist": "学マスコミュ保管委員会",
          "genre": "Gaming",
          "date": "20240619",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=Sj2iwbQFTB8",
          "description": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス",
          "synopsis": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス"
        }
      }
    }
  },
  {
    "alias": "H02",
    "logical_source_id": "15PC5cF8TmNAP9vi2ccO6M4Zw476JYWE8",
    "character": "HIRO",
    "role": "Dear 011–020 / N.I.A.",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\01_DEAR_ROUTE\\【学マス】篠澤広　親愛度１１～２０話【アイドルコミュ】-(720p30).mp4",
    "sha256": "0edca8ea666835eb621ffd0e088cf4cf2b1a0811eb0562c609ed911e98487554",
    "bytes": 84952481,
    "duration_seconds": 2077.953741,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "0edca8ea666835eb621ffd0e088cf4cf2b1a0811eb0562c609ed911e98487554",
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
          "duration_ts": 31916544,
          "duration": "2077.900000",
          "bit_rate": "186486",
          "bits_per_raw_sample": "8",
          "nb_frames": "62337",
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
          "duration_ts": 91637760,
          "duration": "2077.953741",
          "bit_rate": "128000",
          "nb_frames": "89490",
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
          "duration_ts": 187015837,
          "duration": "2077.953744",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\01_DEAR_ROUTE\\【学マス】篠澤広　親愛度１１～２０話【アイドルコミュ】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "2077.953741",
        "size": "84952481",
        "bit_rate": "327062",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【学マス】篠澤広　親愛度１１～２０話【アイドルコミュ】",
          "artist": "学マスコミュ保管委員会",
          "genre": "Gaming",
          "date": "20241228",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=-rnNcxJF4EI",
          "description": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n↓再生リスト\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh\n\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス",
          "synopsis": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n↓再生リスト\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh\n\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス"
        }
      }
    }
  },
  {
    "alias": "H03",
    "logical_source_id": "1EDx0YyXW11f6CNg2Too0fh-7jpaEVU9Q",
    "character": "HIRO",
    "role": "Dear 021–027 / STEP3",
    "path": "LOCAL_USER/Downloads\\【学マス】篠澤広 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
    "sha256": "3b533ccfdfa1d4a284c660f8f3ab5f87c7ca18d52e5f6a4e758f7197493e6989",
    "bytes": 279435246,
    "duration_seconds": 2687.454331,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "3b533ccfdfa1d4a284c660f8f3ab5f87c7ca18d52e5f6a4e758f7197493e6989",
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
          "duration_ts": 41278464,
          "duration": "2687.400000",
          "bit_rate": "688405",
          "bits_per_raw_sample": "8",
          "nb_frames": "161244",
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
          "duration_ts": 118516736,
          "duration": "2687.454331",
          "bit_rate": "127999",
          "nb_frames": "115739",
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
          "duration_ts": 241870890,
          "duration": "2687.454333",
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
        "filename": "LOCAL_USER/Downloads\\【学マス】篠澤広 親愛度コミュ21～27話まとめ【STEP3】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "2687.454331",
        "size": "279435246",
        "bit_rate": "831821",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【学マス】篠澤広  親愛度コミュ21～27話まとめ【STEP3】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20250717",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=PKkBQRBGljI",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#篠澤広",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#篠澤広"
        }
      }
    }
  },
  {
    "alias": "H04",
    "logical_source_id": "1Toi0yHcoq0jV0GMcA4JalcrlLMbnFxQO",
    "character": "HIRO",
    "role": "Dear 028–037 / H.I.F.",
    "path": "LOCAL_USER/Downloads\\【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】-(720p60).mp4",
    "sha256": "4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468",
    "bytes": 545587232,
    "duration_seconds": 3516.615692,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "de92afafb3181342407ab9405f4951e820bfdafaad5b1e9538ec9d7f73ea826e",
    "materialization_note": "Full original replaces preferred trim for NEW whole-source calculations; prefix packet equivalence retained as prior verified evidence",
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
          "duration_ts": 210992782,
          "duration": "3516.546367",
          "bit_rate": "1098603",
          "bits_per_raw_sample": "8",
          "nb_frames": "210782",
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
          "duration_ts": 155082752,
          "duration": "3516.615692",
          "bit_rate": "127999",
          "nb_frames": "151448",
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
          "duration_ts": 316495412,
          "duration": "3516.615689",
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
        "filename": "LOCAL_USER/Downloads\\【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "3516.615692",
        "size": "545587232",
        "bit_rate": "1241164",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20260526",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=F4QAgB54B-g",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#篠澤広",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#篠澤広"
        }
      }
    }
  },
  {
    "alias": "H05",
    "logical_source_id": "10ZYoYqUEiQu4D5CllwOkhiEg0tsV4Kn4",
    "character": "HIRO",
    "role": "光景 song communication",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【楽曲コミュ】光景【篠澤広】【学マス】-(720p30).mp4",
    "sha256": "538e20ac3ec50b58237a6d01bd0ca06172479ce76d4e418b4c002ab4cf6bb09a",
    "bytes": 36824684,
    "duration_seconds": 430.753379,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "538e20ac3ec50b58237a6d01bd0ca06172479ce76d4e418b4c002ab4cf6bb09a",
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
          "mime_codec_string": "avc1.64001f",
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
          "duration_ts": 6615040,
          "duration": "430.666667",
          "bit_rate": "521329",
          "bits_per_raw_sample": "8",
          "nb_frames": "12920",
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
          "duration_ts": 18996224,
          "duration": "430.753379",
          "bit_rate": "127999",
          "nb_frames": "18551",
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
          "duration_ts": 38767804,
          "duration": "430.753378",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【楽曲コミュ】光景【篠澤広】【学マス】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "430.753379",
        "size": "36824684",
        "bit_rate": "683912",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【楽曲コミュ】光景【篠澤広】【学マス】",
          "artist": "学マスコミュ保管委員会",
          "genre": "Gaming",
          "date": "20240627",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=y-mKAoII4Uc",
          "description": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス",
          "synopsis": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス"
        }
      }
    }
  },
  {
    "alias": "H06",
    "logical_source_id": "1SefKMkVth430vm0qAh4xzLcK_N0mbRrt",
    "character": "HIRO",
    "role": "コントラスト song communication",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【楽曲コミュ】コントラスト【篠澤広】【学マス】-(720p30).mp4",
    "sha256": "782a54da98a07d5c95d17bf0c759bff6458b39138c2909e242018713a9babb91",
    "bytes": 47826938,
    "duration_seconds": 498.277007,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "782a54da98a07d5c95d17bf0c759bff6458b39138c2909e242018713a9babb91",
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
          "mime_codec_string": "avc1.64001f",
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
          "duration_ts": 7652352,
          "duration": "498.200000",
          "bit_rate": "608230",
          "bits_per_raw_sample": "8",
          "nb_frames": "14946",
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
          "duration_ts": 21974016,
          "duration": "498.277007",
          "bit_rate": "127999",
          "nb_frames": "21459",
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
          "duration_ts": 44844931,
          "duration": "498.277011",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【楽曲コミュ】コントラスト【篠澤広】【学マス】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "498.277007",
        "size": "47826938",
        "bit_rate": "767877",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【楽曲コミュ】コントラスト【篠澤広】【学マス】",
          "artist": "学マスコミュ保管委員会",
          "genre": "Gaming",
          "date": "20240722",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=Pu22J-gPQgM",
          "description": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス",
          "synopsis": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス"
        }
      }
    }
  },
  {
    "alias": "H07",
    "logical_source_id": "1DkdQlnwXXpyg-raVxgn3Hve7IBIhGBpS",
    "character": "HIRO",
    "role": "Campus mode!! song communication",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【Campus mode!!】篠澤広 楽曲コミュまとめ【学マス】-(720p30).mp4",
    "sha256": "421b77248be17e3bdac3c6f07fbfcadf1562b635687ae6495092906c9a99f1d6",
    "bytes": 47160792,
    "duration_seconds": 551.984762,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "421b77248be17e3bdac3c6f07fbfcadf1562b635687ae6495092906c9a99f1d6",
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
          "mime_codec_string": "avc1.64001f",
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
          "duration_ts": 8477696,
          "duration": "551.933333",
          "bit_rate": "525541",
          "bits_per_raw_sample": "8",
          "nb_frames": "16558",
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
          "duration_ts": 24342528,
          "duration": "551.984762",
          "bit_rate": "128006",
          "nb_frames": "23772",
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
          "duration_ts": 49678629,
          "duration": "551.984767",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【Campus mode!!】篠澤広 楽曲コミュまとめ【学マス】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "551.984762",
        "size": "47160792",
        "bit_rate": "683508",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【Campus mode!!】篠澤広 楽曲コミュまとめ【学マス】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20250109",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=dDqI5_e1zbE",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#学園アイドルマスター",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#学園アイドルマスター"
        }
      }
    }
  },
  {
    "alias": "H08",
    "logical_source_id": "1vo_bb3APWI46ouyP8gBLDT6IKYtEoKrD",
    "character": "HIRO",
    "role": "サンフェーデッド song communication",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【サンフェーデッド】篠澤広 楽曲コミュまとめ【学マス】-(720p60).mp4",
    "sha256": "c7ba97d26e9b75ea5aba937067018987d9f29f9ae072e622681278d384283676",
    "bytes": 22033827,
    "duration_seconds": 479.190204,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "c7ba97d26e9b75ea5aba937067018987d9f29f9ae072e622681278d384283676",
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
          "duration_ts": 7359488,
          "duration": "479.133333",
          "bit_rate": "203793",
          "bits_per_raw_sample": "8",
          "nb_frames": "28748",
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
          "duration_ts": 21132288,
          "duration": "479.190204",
          "bit_rate": "128001",
          "nb_frames": "20637",
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
          "duration_ts": 43127118,
          "duration": "479.190200",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【サンフェーデッド】篠澤広 楽曲コミュまとめ【学マス】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "479.190204",
        "size": "22033827",
        "bit_rate": "367851",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【サンフェーデッド】篠澤広 楽曲コミュまとめ【学マス】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20250717",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=EeQeFYe98KQ",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#篠澤広",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#篠澤広"
        }
      }
    }
  },
  {
    "alias": "H09",
    "logical_source_id": "1bFRSUu8i-L7iU9OWTQa_9HJPEDmf08ul",
    "character": "HIRO",
    "role": "ガラクタロード song communication / CIDOL 018",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【ガラクタロード】篠澤広  楽曲コミュまとめ【学マス】-(720p60).mp4",
    "sha256": "479d2926eca4eddb1157b49091054f9229eb48a253de9cdb0ac1658f2f667370",
    "bytes": 46726213,
    "duration_seconds": 508.795646,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "479d2926eca4eddb1157b49091054f9229eb48a253de9cdb0ac1658f2f667370",
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
          "duration_ts": 30524494,
          "duration": "508.741567",
          "bit_rate": "569034",
          "bits_per_raw_sample": "8",
          "nb_frames": "30494",
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
          "duration_ts": 22437888,
          "duration": "508.795646",
          "bit_rate": "128006",
          "nb_frames": "21912",
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
          "duration_ts": 45791608,
          "duration": "508.795644",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【ガラクタロード】篠澤広  楽曲コミュまとめ【学マス】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "508.795646",
        "size": "46726213",
        "bit_rate": "734695",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【ガラクタロード】篠澤広  楽曲コミュまとめ【学マス】",
          "artist": "学Pといっしょ",
          "genre": "Gaming",
          "date": "20260526",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=ejLLL3PgeMU",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#篠澤広",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#篠澤広"
        }
      }
    }
  },
  {
    "alias": "H10",
    "logical_source_id": "1F9TUHsTmutf8wzxJjCRLwiTXa1CKfEUf",
    "character": "HIRO",
    "role": "ハッピーミルフィーユ song communication",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【楽曲コミュ】ハッピーミルフィーユ（花海佑芽ボイス実装版）【篠澤広】【学マス】-(720p30).mp4",
    "sha256": "38d6edc157236e3eab904bad79fec85d3b1c1051e1181765d5b5c742389a4374",
    "bytes": 50538304,
    "duration_seconds": 423.230113,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "38d6edc157236e3eab904bad79fec85d3b1c1051e1181765d5b5c742389a4374",
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
          "mime_codec_string": "avc1.64001f",
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
          "duration_ts": 6499840,
          "duration": "423.166667",
          "bit_rate": "787393",
          "bits_per_raw_sample": "8",
          "nb_frames": "12695",
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
          "duration_ts": 18664448,
          "duration": "423.230113",
          "bit_rate": "127999",
          "nb_frames": "18227",
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
          "duration_ts": 38090710,
          "duration": "423.230111",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【楽曲コミュ】ハッピーミルフィーユ（花海佑芽ボイス実装版）【篠澤広】【学マス】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "423.230113",
        "size": "50538304",
        "bit_rate": "955287",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【楽曲コミュ】ハッピーミルフィーユ（花海佑芽ボイス実装版）【篠澤広】【学マス】",
          "artist": "学マスコミュ保管委員会",
          "genre": "Gaming",
          "date": "20251129",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=3z_oBVjELCM",
          "description": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n↓再生リスト\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh\n\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス",
          "synopsis": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n↓再生リスト\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_exvCZ6FunP_7hUbK4Qysj\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8x8qlEhliEXkG8y3iaIOw6\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_-chcOj1fw5Wos3x7cY4PQ\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_pncUG6lNsFHWBs0I55fIh\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8epfQE9PdEsiSTUJSUl1F7\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR8d0FQJq8GY8Xy4ThdK2D8i\n\nhttps://www.youtube.com/playlist?list=PLbJbZ3rhccR_kezyuO6AIvVHz15JUNlVh\n\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス"
        }
      }
    }
  },
  {
    "alias": "H11",
    "logical_source_id": "13-Fh37KmKFvRLhWFaskIJE5royX6XZh1",
    "character": "HIRO",
    "role": "仮装狂騒曲 song communication",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【楽曲コミュ】仮装狂騒曲【篠澤広】【学マス】-(720p30).mp4",
    "sha256": "baf9cd720ad9845ff07db09f270a675f8b6031061c9484737951053f98b16745",
    "bytes": 43619611,
    "duration_seconds": 439.669841,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "baf9cd720ad9845ff07db09f270a675f8b6031061c9484737951053f98b16745",
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
          "mime_codec_string": "avc1.64001f",
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
          "duration_ts": 6752256,
          "duration": "439.600000",
          "bit_rate": "627823",
          "bits_per_raw_sample": "8",
          "nb_frames": "13188",
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
          "duration_ts": 19389440,
          "duration": "439.669841",
          "bit_rate": "127999",
          "nb_frames": "18935",
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
          "duration_ts": 39570286,
          "duration": "439.669844",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\03_SONG_COMMUS\\【楽曲コミュ】仮装狂騒曲【篠澤広】【学マス】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "439.669841",
        "size": "43619611",
        "bit_rate": "793679",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【楽曲コミュ】仮装狂騒曲【篠澤広】【学マス】",
          "artist": "学マスコミュ保管委員会",
          "genre": "Gaming",
          "date": "20241008",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=sMwPNprUZ7s",
          "description": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス",
          "synopsis": "※この動画には学園アイドルマスターのネタバレが含まれます。\n\n動画内容や構成に関するアドバイス、今後出して欲しい動画等があればコメントで教えてください！\n\n#学園アイドルマスター #学マス"
        }
      }
    }
  },
  {
    "alias": "H12",
    "logical_source_id": "1Y5zbtbMqqZw8K12HjP5Up_54Ce3jWjBk",
    "character": "HIRO",
    "role": "光景 Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「光景」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "sha256": "346649b3c41f8cf987125c344e09d29f1818187240132acfbc5eed89d854462c",
    "bytes": 57565410,
    "duration_seconds": 175.264218,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "346649b3c41f8cf987125c344e09d29f1818187240132acfbc5eed89d854462c",
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
          "duration_ts": 2691072,
          "duration": "175.200000",
          "bit_rate": "2419182",
          "bits_per_raw_sample": "8",
          "nb_frames": "10512",
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
          "duration_ts": 7729152,
          "duration": "175.264218",
          "bit_rate": "127999",
          "nb_frames": "7548",
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
          "duration_ts": 15773780,
          "duration": "175.264222",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「光景」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "175.264218",
        "size": "57565410",
        "bit_rate": "2627594",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「光景」 (篠澤広 ソロ SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20241127",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=9jzNYNVwThU",
          "description": "「光景」 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44367089\n歌：#篠澤広  (CV. 川村玲奈) \n作詞、作曲、編曲：長谷川白紙\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「光景」 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44367089\n歌：#篠澤広  (CV. 川村玲奈) \n作詞、作曲、編曲：長谷川白紙\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H13",
    "logical_source_id": "1BJxsuu7p4m4eUFOgXlstQI9AgWGnyWbC",
    "character": "HIRO",
    "role": "Fan comparative montage: progressively improving 光景",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\【アイマスMV】どんどん上手くなる光景  篠澤 広　学園アイドルマスター　学マス-(720p60).mp4",
    "sha256": "2de772e4600435305195d845da1c63bf27dff5776f2a125d66fc048f3a830a59",
    "bytes": 48167387,
    "duration_seconds": 153.925079,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "2de772e4600435305195d845da1c63bf27dff5776f2a125d66fc048f3a830a59",
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
          "duration_ts": 2363392,
          "duration": "153.866667",
          "bit_rate": "2296654",
          "bits_per_raw_sample": "8",
          "nb_frames": "9232",
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
          "duration_ts": 6788096,
          "duration": "153.925079",
          "bit_rate": "127999",
          "nb_frames": "6629",
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
          "duration_ts": 13853257,
          "duration": "153.925078",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\【アイマスMV】どんどん上手くなる光景  篠澤 広　学園アイドルマスター　学マス-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "153.925079",
        "size": "48167387",
        "bit_rate": "2503419",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【アイマスMV】どんどん上手くなる光景  篠澤 広　学園アイドルマスター　学マス",
          "artist": "きっかーP",
          "genre": "Gaming",
          "date": "20240625",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=ztfHw7kvZ-M",
          "description": "学園アイドルマスターはアイドルがどんどんMVでも成長する感じなので、篠澤 広の光景で上手くなってる様子を動画にしました\n\n光景\n歌：篠澤広(川村玲奈)\n作詞：長谷川白紙\n作曲：長谷川白紙\n\n公式さんの動画\n初星学園 「光景」Official Music Video (HATSUBOSHI GAKUEN - Koukei)\nhttps://youtu.be/VJk2etK8I1w?si=UfV6dLAiu3A6dVO3\n\n【学マス】篠澤 広 紹介PV【アイドルマスター】\nhttps://youtu.be/8ol7-APhqFY?si=LddZQDb5IM27_5Jm",
          "synopsis": "学園アイドルマスターはアイドルがどんどんMVでも成長する感じなので、篠澤 広の光景で上手くなってる様子を動画にしました\n\n光景\n歌：篠澤広(川村玲奈)\n作詞：長谷川白紙\n作曲：長谷川白紙\n\n公式さんの動画\n初星学園 「光景」Official Music Video (HATSUBOSHI GAKUEN - Koukei)\nhttps://youtu.be/VJk2etK8I1w?si=UfV6dLAiu3A6dVO3\n\n【学マス】篠澤 広 紹介PV【アイドルマスター】\nhttps://youtu.be/8ol7-APhqFY?si=LddZQDb5IM27_5Jm"
        }
      }
    }
  },
  {
    "alias": "H14",
    "logical_source_id": "14mm43MjBvXxqXvEfgpxdgpzO_hYSyvLn",
    "character": "HIRO",
    "role": "光景 authored official MV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「光景」Official Music Video (HATSUBOSHI GAKUEN - Koukei)-(720p30).mp4",
    "sha256": "ff7023355616a3f1f40328f8e899e6805b899919bfff67b1ead1578100ceccc6",
    "bytes": 38569146,
    "duration_seconds": 271.928889,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "ff7023355616a3f1f40328f8e899e6805b899919bfff67b1ead1578100ceccc6",
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
          "duration_ts": 4175872,
          "duration": "271.866667",
          "bit_rate": "834169",
          "bits_per_raw_sample": "8",
          "nb_frames": "8156",
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
          "duration_ts": 11992064,
          "duration": "271.928889",
          "bit_rate": "255999",
          "nb_frames": "11711",
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
          "duration_ts": 24473600,
          "duration": "271.928889",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「光景」Official Music Video (HATSUBOSHI GAKUEN - Koukei)-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "271.928889",
        "size": "38569146",
        "bit_rate": "1134683",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "初星学園 「光景」Official Music Video (HATSUBOSHI GAKUEN - Koukei)",
          "artist": "HATSUBOSHI GAKUEN",
          "genre": "Music",
          "date": "20240506",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=VJk2etK8I1w",
          "description": "光景 (Koukei)\n------------------------------\nEN Credits.\n▶Music \nSong by Hiro Shinosawa (VA. Reina Kawamura)\nLyric written, Composed, Arranged by Hakushi Hasegawa\n\nARRANGEMENTS, PROGRAM & KEY : Hakushi Hasegawa\nSTRINGS AND HORN ARRANGEMENTS : Arthur Verocai\nVIOLINS : Ana de Oliveira / Angélica Alves / Caroline Santa Rosa / Clóvis Pereira Filho / Daniel Passuni / Gabriela Queiroz / Joyce Veiga / Luisa de Castro / Michel Bessler / Nikolay Sapoundjiev / Ubiratã Rodrigues / William Isaac\nVIOLAS : Bernardo Fantini / Diego Silva / Ivan Zandonade / Victor Botene\nCELLOS : Alceu Reis / Emilia / Glenda Carvalho / Lisiane de Los Santos\nTRUMPETS : José Arimatéa / Diogo Gomes\nALTO SAX : Idriss Boudrouia\nTENOR SAX and PICCOLO : Edu Neves\nTROMBONE : Aldivas Ayres\nORCHESTRA FIXER : Paulo Guimarães\nRECORDING ENGINEER : William Luna at studio Cia dos Técnicos (RJ)\nRJ RECORDING COORDINATORS : Tamara Emy / Nick Dwyer / Ayano Kondo\nPANDEIRO : Leo Nanjo\nCO-DIRECTION : Go Yamazaki\nMIX ENGINEER : Masashi Uramoto at Soi Studio\n\n▶Movie\ndirector & animator : Wataru Uekusa\nanimators : Hiroshi Sakai / Fujishima Kei\nbackground artists : Hikagami Hinami / moge\nlogo & prop design : Hikagami Hinami\ntext design : Totorika\n------------------------------\nJP Credits.\n▶Music\n歌：篠澤 広 (CV. 川村玲奈)\n作詞作曲編曲：長谷川白紙\n\nARRANGEMENTS, PROGRAM & KEY : 長谷川白紙\nSTRINGS AND HORN ARRANGEMENTS : Arthur Verocai\nVIOLINS : Ana de Oliveira / Angélica Alves / Caroline Santa Rosa / Clóvis Pereira Filho / Daniel Passuni / Gabriela Queiroz / Joyce Veiga / Luisa de Castro / Michel Bessler / Nikolay Sapoundjiev / Ubiratã Rodrigues / William Isaac\nVIOLAS : Bernardo Fantini / Diego Silva / Ivan Zandonade / Victor Botene\nCELLOS : Alceu Reis / Emilia / Glenda Carvalho / Lisiane de Los Santos\nTRUMPETS : José Arimatéa / Diogo Gomes\nALTO SAX : Idriss Boudrouia\nTENOR SAX and PICCOLO : Edu Neves\nTROMBONE : Aldivas Ayres\nORCHESTRA FIXER : Paulo Guimarães\nRECORDING ENGINEER : William Luna at studio Cia dos Técnicos (RJ)\nRJ RECORDING COORDINATORS : Tamara Emy / Nick Dwyer / 近藤彩乃\nPANDEIRO : 南條レオ\nCO-DIRECTION : 山崎ごう\nMIX ENGINEER : 浦本雅史 at Soi Studio\n\n▶Movie\ndirector & animator : 植草航 \nanimators : 酒井浩史 / フジシマケイ \nbackground artists : ひかがみひなみ / moge \nlogo & prop design : ひかがみひなみ \ntext design : ととりか\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 子川拓哉\nLabel Director : 大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\n▶「光景」インスト音源データ公開中！ぜひご利用ください。\nhttps://gakuen-label.idolmaster-official.jp/download\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2024 Bandai Namco Entertainment Inc.\n\n#篠澤広 #初星学園 #長谷川白紙 #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen",
          "synopsis": "光景 (Koukei)\n------------------------------\nEN Credits.\n▶Music \nSong by Hiro Shinosawa (VA. Reina Kawamura)\nLyric written, Composed, Arranged by Hakushi Hasegawa\n\nARRANGEMENTS, PROGRAM & KEY : Hakushi Hasegawa\nSTRINGS AND HORN ARRANGEMENTS : Arthur Verocai\nVIOLINS : Ana de Oliveira / Angélica Alves / Caroline Santa Rosa / Clóvis Pereira Filho / Daniel Passuni / Gabriela Queiroz / Joyce Veiga / Luisa de Castro / Michel Bessler / Nikolay Sapoundjiev / Ubiratã Rodrigues / William Isaac\nVIOLAS : Bernardo Fantini / Diego Silva / Ivan Zandonade / Victor Botene\nCELLOS : Alceu Reis / Emilia / Glenda Carvalho / Lisiane de Los Santos\nTRUMPETS : José Arimatéa / Diogo Gomes\nALTO SAX : Idriss Boudrouia\nTENOR SAX and PICCOLO : Edu Neves\nTROMBONE : Aldivas Ayres\nORCHESTRA FIXER : Paulo Guimarães\nRECORDING ENGINEER : William Luna at studio Cia dos Técnicos (RJ)\nRJ RECORDING COORDINATORS : Tamara Emy / Nick Dwyer / Ayano Kondo\nPANDEIRO : Leo Nanjo\nCO-DIRECTION : Go Yamazaki\nMIX ENGINEER : Masashi Uramoto at Soi Studio\n\n▶Movie\ndirector & animator : Wataru Uekusa\nanimators : Hiroshi Sakai / Fujishima Kei\nbackground artists : Hikagami Hinami / moge\nlogo & prop design : Hikagami Hinami\ntext design : Totorika\n------------------------------\nJP Credits.\n▶Music\n歌：篠澤 広 (CV. 川村玲奈)\n作詞作曲編曲：長谷川白紙\n\nARRANGEMENTS, PROGRAM & KEY : 長谷川白紙\nSTRINGS AND HORN ARRANGEMENTS : Arthur Verocai\nVIOLINS : Ana de Oliveira / Angélica Alves / Caroline Santa Rosa / Clóvis Pereira Filho / Daniel Passuni / Gabriela Queiroz / Joyce Veiga / Luisa de Castro / Michel Bessler / Nikolay Sapoundjiev / Ubiratã Rodrigues / William Isaac\nVIOLAS : Bernardo Fantini / Diego Silva / Ivan Zandonade / Victor Botene\nCELLOS : Alceu Reis / Emilia / Glenda Carvalho / Lisiane de Los Santos\nTRUMPETS : José Arimatéa / Diogo Gomes\nALTO SAX : Idriss Boudrouia\nTENOR SAX and PICCOLO : Edu Neves\nTROMBONE : Aldivas Ayres\nORCHESTRA FIXER : Paulo Guimarães\nRECORDING ENGINEER : William Luna at studio Cia dos Técnicos (RJ)\nRJ RECORDING COORDINATORS : Tamara Emy / Nick Dwyer / 近藤彩乃\nPANDEIRO : 南條レオ\nCO-DIRECTION : 山崎ごう\nMIX ENGINEER : 浦本雅史 at Soi Studio\n\n▶Movie\ndirector & animator : 植草航 \nanimators : 酒井浩史 / フジシマケイ \nbackground artists : ひかがみひなみ / moge \nlogo & prop design : ひかがみひなみ \ntext design : ととりか\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 子川拓哉\nLabel Director : 大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\n▶「光景」インスト音源データ公開中！ぜひご利用ください。\nhttps://gakuen-label.idolmaster-official.jp/download\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2024 Bandai Namco Entertainment Inc.\n\n#篠澤広 #初星学園 #長谷川白紙 #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen"
        }
      }
    }
  },
  {
    "alias": "H15",
    "logical_source_id": "1JbU-ssxlwCzUGTnq4i2JLO-fw3EaPBxR",
    "character": "HIRO",
    "role": "コントラスト Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「コントラスト」 (篠澤広 ソロ2 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "sha256": "ea62087e203b892295f6bb27f68426779b1d0c37ceb83c522977942e1c7bf2aa",
    "bytes": 63692806,
    "duration_seconds": 200.782948,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "ea62087e203b892295f6bb27f68426779b1d0c37ceb83c522977942e1c7bf2aa",
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
          "duration_ts": 3083008,
          "duration": "200.716667",
          "bit_rate": "2375155",
          "bits_per_raw_sample": "8",
          "nb_frames": "12043",
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
          "duration_ts": 8854528,
          "duration": "200.782948",
          "bit_rate": "127999",
          "nb_frames": "8647",
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
          "duration_ts": 18070465,
          "duration": "200.782944",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「コントラスト」 (篠澤広 ソロ2 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "200.782948",
        "size": "63692806",
        "bit_rate": "2537777",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「コントラスト」 (篠澤広 ソロ2 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20240722",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=X7egVXrwKpI",
          "description": "「コントラスト」 4K #HDR 60fps\n\n歌：#篠澤広  (CV. 川村玲奈) \n作詞：佐々木恵梨 \n作曲：佐々木恵梨、鵜飼大幹、中村ヒロ \n編曲：中村ヒロ\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「コントラスト」 4K #HDR 60fps\n\n歌：#篠澤広  (CV. 川村玲奈) \n作詞：佐々木恵梨 \n作曲：佐々木恵梨、鵜飼大幹、中村ヒロ \n編曲：中村ヒロ\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H16",
    "logical_source_id": "11LEGW6hntUwu7GhljqYbqWzcO2lZFwDz",
    "character": "HIRO",
    "role": "コントラスト full/static presentation",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\コントラスト-(720p25).mp4",
    "sha256": "4c1188dac2851da6d2a945ca3690fd95f1012b7cdf46d0a2c65f4084737b6d68",
    "bytes": 8971837,
    "duration_seconds": 217.510998,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "4c1188dac2851da6d2a945ca3690fd95f1012b7cdf46d0a2c65f4084737b6d68",
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
          "width": 720,
          "height": 720,
          "coded_width": 720,
          "coded_height": 720,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "1:1",
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
          "r_frame_rate": "25/1",
          "avg_frame_rate": "25/1",
          "time_base": "1/12800",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2783744,
          "duration": "217.480000",
          "bit_rate": "45741",
          "bits_per_raw_sample": "8",
          "nb_frames": "5437",
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
          "duration_ts": 9592235,
          "duration": "217.510998",
          "bit_rate": "256000",
          "nb_frames": "9369",
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
          "duration_ts": 19575990,
          "duration": "217.511000",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\コントラスト-(720p25).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "217.510998",
        "size": "8971837",
        "bit_rate": "329981",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "コントラスト",
          "artist": "Hatsuboshi Gakuen, Eri Sasaki, Daiki Ukai, Hiro Nakamura, Hiro Shinosawa, Eri Sasaki, Eri Sasaki, Daiki Ukai, Hiro Nakamura, Hiro Nakamura",
          "album": "Contrast",
          "genre": "Music",
          "date": "20240722",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=4a6oeXjh8-E",
          "description": "Provided to YouTube by NexTone Inc.\n\nコントラスト · Hatsuboshi Gakuen · Eri Sasaki · Daiki Ukai · Hiro Nakamura · Hiro Shinosawa · Eri Sasaki · Eri Sasaki · Daiki Ukai · Hiro Nakamura · Hiro Nakamura\n\nContrast\n\nReleased on: 2024-07-23\n\nAuto-generated by YouTube.",
          "synopsis": "Provided to YouTube by NexTone Inc.\n\nコントラスト · Hatsuboshi Gakuen · Eri Sasaki · Daiki Ukai · Hiro Nakamura · Hiro Shinosawa · Eri Sasaki · Eri Sasaki · Daiki Ukai · Hiro Nakamura · Hiro Nakamura\n\nContrast\n\nReleased on: 2024-07-23\n\nAuto-generated by YouTube."
        }
      }
    }
  },
  {
    "alias": "H17",
    "logical_source_id": "11Sf_pH-3JhiLcAUT4xLkm8rbzYL84f8E",
    "character": "HIRO",
    "role": "サンフェーデッド Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「サンフェーデッド」 (篠澤広 ソロ3 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "sha256": "be3709652b63a93a30bba202dc06296169262af269b84b77109335d65e5bd8cd",
    "bytes": 67395136,
    "duration_seconds": 183.275102,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "be3709652b63a93a30bba202dc06296169262af269b84b77109335d65e5bd8cd",
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
          "duration_ts": 2814208,
          "duration": "183.216667",
          "bit_rate": "2768838",
          "bits_per_raw_sample": "8",
          "nb_frames": "10993",
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
          "duration_ts": 8082432,
          "duration": "183.275102",
          "bit_rate": "127999",
          "nb_frames": "7893",
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
            "language": "eng",
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
          "duration_ts": 16494759,
          "duration": "183.275100",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「サンフェーデッド」 (篠澤広 ソロ3 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "183.275102",
        "size": "67395136",
        "bit_rate": "2941813",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「サンフェーデッド」 (篠澤広 ソロ3 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20250717",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=tRqueI07-nI",
          "description": "「サンフェーデッド」 (#篠澤広  ソロ3 SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45195427\n作詞・作曲・編曲：長谷川白紙\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「サンフェーデッド」 (#篠澤広  ソロ3 SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45195427\n作詞・作曲・編曲：長谷川白紙\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H18",
    "logical_source_id": "14gD5uR2AdNK274Z8Juh6u5pY3pWYpMfF",
    "character": "HIRO",
    "role": "サンフェーデッド authored official MV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「サンフェーデッド」Official Music Video (HATSUBOSHI GAKUEN - SUNFADED)-(720p24).mp4",
    "sha256": "1e3bffcab0e7d0131eda8875e22c5d421570050612f2606751944d6d9d1f9292",
    "bytes": 34895654,
    "duration_seconds": 209.304671,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "1e3bffcab0e7d0131eda8875e22c5d421570050612f2606751944d6d9d1f9292",
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
          "r_frame_rate": "24/1",
          "avg_frame_rate": "24/1",
          "time_base": "1/12288",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2571264,
          "duration": "209.250000",
          "bit_rate": "1033450",
          "bits_per_raw_sample": "8",
          "nb_frames": "5022",
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
          "duration_ts": 9230336,
          "duration": "209.304671",
          "bit_rate": "256001",
          "nb_frames": "9014",
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
            "language": "eng",
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
          "duration_ts": 18837420,
          "duration": "209.304667",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「サンフェーデッド」Official Music Video (HATSUBOSHI GAKUEN - SUNFADED)-(720p24).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "209.304671",
        "size": "34895654",
        "bit_rate": "1333774",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "初星学園 「サンフェーデッド」Official Music Video (HATSUBOSHI GAKUEN - SUNFADED)",
          "artist": "HATSUBOSHI GAKUEN",
          "genre": "Music",
          "date": "20250717",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=XLwmEuM0dIw",
          "description": "[EN Credits.]\nSUNFADED\n▶Music\nSong by Hiro Shinosawa (VA. Reina Kawamura)\nLyric written, Composed, Arranged by Hakushi Hasegawa\n\nGuitar: Tokutaro Hosoi\nBass: Kei Ariizumi\nDrums: Yasuhiro Yoshigaki\n\nRecording Engineer: Daiki Iimura\nRecording Studio: STUDIO SUNSHINE\nMix Engineer: Taiji Okuda\nMix Studio: studio MSR\n\n▶Movie\nDirection : Shun Yamaguchi\nIllustration：sowiti\nDigi↔Ana FX： Frog96\nGraphic Design：SawaiShingo\nCG：Chie Fujimura , LISO\nMV Producer：Keisuke Yano\n------------------------------\n[JP Credits.]\nサンフェーデッド\n▶Music\n歌：篠澤 広 (CV. 川村玲奈)\n作詞作曲編曲：長谷川白紙\n\nGuitar: 細井徳太郎\nBass: 有泉慧\nDrums: 芳垣安洋\n\nRecording Engineer: 飯村大貴\nRecording Studio: STUDIO SUNSHINE\nMix Engineer: 奥田泰次\nMix Studio: studio MSR\n\n▶Movie\n監督 : 山口駿\nイラスト：そゐち\nDigi↔Ana FX： フロクロ\nグラフィックデザイン：サワイシンゴ\nCG：藤村千枝 , リソ\nMV Producer：矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2025 Bandai Namco Entertainment Inc.\n\n#篠澤広 #初星学園 #長谷川白紙 #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen",
          "synopsis": "[EN Credits.]\nSUNFADED\n▶Music\nSong by Hiro Shinosawa (VA. Reina Kawamura)\nLyric written, Composed, Arranged by Hakushi Hasegawa\n\nGuitar: Tokutaro Hosoi\nBass: Kei Ariizumi\nDrums: Yasuhiro Yoshigaki\n\nRecording Engineer: Daiki Iimura\nRecording Studio: STUDIO SUNSHINE\nMix Engineer: Taiji Okuda\nMix Studio: studio MSR\n\n▶Movie\nDirection : Shun Yamaguchi\nIllustration：sowiti\nDigi↔Ana FX： Frog96\nGraphic Design：SawaiShingo\nCG：Chie Fujimura , LISO\nMV Producer：Keisuke Yano\n------------------------------\n[JP Credits.]\nサンフェーデッド\n▶Music\n歌：篠澤 広 (CV. 川村玲奈)\n作詞作曲編曲：長谷川白紙\n\nGuitar: 細井徳太郎\nBass: 有泉慧\nDrums: 芳垣安洋\n\nRecording Engineer: 飯村大貴\nRecording Studio: STUDIO SUNSHINE\nMix Engineer: 奥田泰次\nMix Studio: studio MSR\n\n▶Movie\n監督 : 山口駿\nイラスト：そゐち\nDigi↔Ana FX： フロクロ\nグラフィックデザイン：サワイシンゴ\nCG：藤村千枝 , リソ\nMV Producer：矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2025 Bandai Namco Entertainment Inc.\n\n#篠澤広 #初星学園 #長谷川白紙 #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen"
        }
      }
    }
  },
  {
    "alias": "H19",
    "logical_source_id": "1NZfazcL67wDoVoFa5nuQp-y3E2-Edzmd",
    "character": "HIRO",
    "role": "Campus mode!! Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Campus mode!!」(篠澤広 フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "sha256": "a692b45cc3ee31ff957c0199bae17c1c2f143c2271f3c1e19abf4d77a8e634ef",
    "bytes": 63464478,
    "duration_seconds": 160.728526,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "a692b45cc3ee31ff957c0199bae17c1c2f143c2271f3c1e19abf4d77a8e634ef",
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
          "duration_ts": 2467584,
          "duration": "160.650000",
          "bit_rate": "2973259",
          "bits_per_raw_sample": "8",
          "nb_frames": "9639",
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
          "duration_ts": 7088128,
          "duration": "160.728526",
          "bit_rate": "127999",
          "nb_frames": "6922",
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
          "duration_ts": 14465567,
          "duration": "160.728522",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Campus mode!!」(篠澤広 フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "160.728526",
        "size": "63464478",
        "bit_rate": "3158840",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「Campus mode!!」(篠澤広 フェスSSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20250111",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=1EJOn0vf-Fo",
          "description": "「Campus mode!!」(#篠澤広  フェスSSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44527247\n歌：篠澤広 (CV. 川村玲奈)\n作詞・作曲：田淵智也\n編曲：滝澤俊輔（TRYTONELABO）\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「Campus mode!!」(#篠澤広  フェスSSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44527247\n歌：篠澤広 (CV. 川村玲奈)\n作詞・作曲：田淵智也\n編曲：滝澤俊輔（TRYTONELABO）\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H20",
    "logical_source_id": "1zPxR0JyPp4JhLxWS_zfENcC9znXerQIj",
    "character": "HIRO",
    "role": "初 Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\【学マス】篠澤広「初」 3DMV-(592p30).mp4",
    "sha256": "3ae933080d1da33631c2f491aea6969b0b2801cc48442c4023290632ae22aed0",
    "bytes": 37265987,
    "duration_seconds": 155.178957,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "3ae933080d1da33631c2f491aea6969b0b2801cc48442c4023290632ae22aed0",
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
          "mime_codec_string": "avc1.64001f",
          "width": 1280,
          "height": 592,
          "coded_width": 1280,
          "coded_height": 592,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "80:37",
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
          "duration_ts": 2382848,
          "duration": "155.133333",
          "bit_rate": "1729468",
          "bits_per_raw_sample": "8",
          "nb_frames": "4654",
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
          "duration_ts": 6843392,
          "duration": "155.178957",
          "bit_rate": "128019",
          "nb_frames": "6683",
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
          "duration_ts": 13966106,
          "duration": "155.178956",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\【学マス】篠澤広「初」 3DMV-(592p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "155.178957",
        "size": "37265987",
        "bit_rate": "1921187",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【学マス】篠澤広「初」 3DMV",
          "artist": "篠澤広 大好きマン",
          "genre": "Gaming",
          "date": "20241011",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=ivNDdkumEl4",
          "description": "広可愛いね\n\n著作元\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\n\n#学園アイドルマスター \n#学マス \n#篠澤広",
          "synopsis": "広可愛いね\n\n著作元\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\n\n#学園アイドルマスター \n#学マス \n#篠澤広"
        }
      }
    }
  },
  {
    "alias": "H21",
    "logical_source_id": "1OXLlFgDZOfdom_Sywd_lF_j-dimUZeqp",
    "character": "HIRO",
    "role": "Howling over the World Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Howling over the World」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "sha256": "cbfae7e9f90821d0c70a16201a9ba462603548f899fa93b5ab94fb76c0e248f7",
    "bytes": 42489463,
    "duration_seconds": 110.225125,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "cbfae7e9f90821d0c70a16201a9ba462603548f899fa93b5ab94fb76c0e248f7",
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
          "duration_ts": 1691904,
          "duration": "110.150000",
          "bit_rate": "2896660",
          "bits_per_raw_sample": "8",
          "nb_frames": "6609",
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
          "duration_ts": 4860928,
          "duration": "110.225125",
          "bit_rate": "127999",
          "nb_frames": "4747",
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
          "duration_ts": 9920261,
          "duration": "110.225122",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「Howling over the World」 (篠澤広 ソロ SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "110.225125",
        "size": "42489463",
        "bit_rate": "3083831",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「Howling over the World」 (篠澤広 ソロ SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20250601",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=t4jb8WFheCM",
          "description": "「Howling over the World」 (#篠澤広   ソロ SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45042393\n\n作詞・作曲・編曲： 烏屋茶房\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 #学園偶像大師",
          "synopsis": "「Howling over the World」 (#篠澤広   ソロ SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45042393\n\n作詞・作曲・編曲： 烏屋茶房\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 #学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H22",
    "logical_source_id": "1tdzAna_WcWmo9RzC5lyLnliiyJaoDGpy",
    "character": "HIRO",
    "role": "がむしゃらに行こう！ Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「がむしゃらに行こう！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "sha256": "42ddef86a794641182d2b3ae143b5afd2a6b68bf2f08a5f989e373c45cd70ee9",
    "bytes": 41525073,
    "duration_seconds": 110.457324,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "42ddef86a794641182d2b3ae143b5afd2a6b68bf2f08a5f989e373c45cd70ee9",
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
          "duration_ts": 1695488,
          "duration": "110.383333",
          "bit_rate": "2799915",
          "bits_per_raw_sample": "8",
          "nb_frames": "6623",
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
          "duration_ts": 4871168,
          "duration": "110.457324",
          "bit_rate": "127999",
          "nb_frames": "4757",
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
          "duration_ts": 9941159,
          "duration": "110.457322",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「がむしゃらに行こう！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "110.457324",
        "size": "41525073",
        "bit_rate": "3007501",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「がむしゃらに行こう！」 (篠澤広 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20250929",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=_Yjg5ewXZXo",
          "description": "「がむしゃらに行こう！」 (#篠澤広 SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45460155\n\n歌：篠澤広 (CV. 川村玲奈)\n作詞：SHOW (Digz, Inc. Group)\n作曲：SHOW (Digz, Inc. Group)、Mitsu.J (Digz, Inc. Group)\n編曲：Mitsu.J (Digz, Inc. Group)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「がむしゃらに行こう！」 (#篠澤広 SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45460155\n\n歌：篠澤広 (CV. 川村玲奈)\n作詞：SHOW (Digz, Inc. Group)\n作曲：SHOW (Digz, Inc. Group)、Mitsu.J (Digz, Inc. Group)\n編曲：Mitsu.J (Digz, Inc. Group)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H23",
    "logical_source_id": "1P75Wv4Qu1W_R6lmZRs0fGmv4VOxoXcmG",
    "character": "HIRO",
    "role": "ミラクルナナウ(ﾟ∀ﾟ)！ Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ミラクルナナウ(ﾟ∀ﾟ)！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "sha256": "6761642adfb3ba089aa286cb147002decc2151e1b30471910afbef84946d9db6",
    "bytes": 44918957,
    "duration_seconds": 116.657052,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "6761642adfb3ba089aa286cb147002decc2151e1b30471910afbef84946d9db6",
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
          "duration_ts": 1790976,
          "duration": "116.600000",
          "bit_rate": "2885180",
          "bits_per_raw_sample": "8",
          "nb_frames": "6996",
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
          "duration_ts": 5144576,
          "duration": "116.657052",
          "bit_rate": "127999",
          "nb_frames": "5024",
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
          "duration_ts": 10499135,
          "duration": "116.657056",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ミラクルナナウ(ﾟ∀ﾟ)！」 (篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "116.657052",
        "size": "44918957",
        "bit_rate": "3080410",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「ミラクルナナウ(ﾟ∀ﾟ)！」 (篠澤広 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20250908",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=V3cPA2Sa8T4",
          "description": "「ミラクルナナウ(ﾟ∀ﾟ)！」 (#篠澤広  SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45383286\n\n作詞・作曲・編曲：YUC'e\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「ミラクルナナウ(ﾟ∀ﾟ)！」 (#篠澤広  SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45383286\n\n作詞・作曲・編曲：YUC'e\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H24",
    "logical_source_id": "1oSoTZTGZNYN4Oq3R1Lwym0cZ8jWHtvxe",
    "character": "HIRO",
    "role": "コンテンポラリのダンス authored official MV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「コンテンポラリのダンス」Official Music Video (HATSUBOSHI GAKUEN - contemporary dance)-(720p30).mp4",
    "sha256": "0b2e22aaf5e227019c734c2341214ec60e64c77ec24ba39cb986f5972ab2859e",
    "bytes": 27025702,
    "duration_seconds": 205.05542,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "0b2e22aaf5e227019c734c2341214ec60e64c77ec24ba39cb986f5972ab2859e",
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
          "r_frame_rate": "30000/1001",
          "avg_frame_rate": "30000/1001",
          "time_base": "1/30000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 6150144,
          "duration": "205.004800",
          "bit_rate": "779107",
          "bits_per_raw_sample": "8",
          "nb_frames": "6144",
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
          "duration_ts": 9042944,
          "duration": "205.055420",
          "bit_rate": "255999",
          "nb_frames": "8831",
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
          "duration_ts": 18454988,
          "duration": "205.055422",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「コンテンポラリのダンス」Official Music Video (HATSUBOSHI GAKUEN - contemporary dance)-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "205.055420",
        "size": "27025702",
        "bit_rate": "1054376",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "初星学園 「コンテンポラリのダンス」Official Music Video (HATSUBOSHI GAKUEN - contemporary dance)",
          "artist": "HATSUBOSHI GAKUEN",
          "genre": "Music",
          "date": "20260528",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=82SGsHkhySg",
          "description": "[EN Credits.]\ncontemporary dance\n\n▶Music\nSong by Hiro Shinosawa（VA.Reina Kawamura）\nLyrics written, Composed, Arranged by mashima yuro\n\n▶Movie\nMV TOKICHIAKI\nMV asst. Mei yokoyama\nMV Producer：KEISUKE YANO\n\n[JP Credits.]\nコンテンポラリのダンス\n\n▶Music\n歌：篠澤 広（CV.川村玲奈）\n作詞・作曲・編曲：真島ゆろ\n\n▶Movie\nMV トキチアキ\nMV asst. Mei yokoyama\nMV Producer：矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 尾上和駿、大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2026 Bandai Namco Entertainment Inc.\n\n#篠澤広 #初星学園 #真島ゆろ #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen",
          "synopsis": "[EN Credits.]\ncontemporary dance\n\n▶Music\nSong by Hiro Shinosawa（VA.Reina Kawamura）\nLyrics written, Composed, Arranged by mashima yuro\n\n▶Movie\nMV TOKICHIAKI\nMV asst. Mei yokoyama\nMV Producer：KEISUKE YANO\n\n[JP Credits.]\nコンテンポラリのダンス\n\n▶Music\n歌：篠澤 広（CV.川村玲奈）\n作詞・作曲・編曲：真島ゆろ\n\n▶Movie\nMV トキチアキ\nMV asst. Mei yokoyama\nMV Producer：矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 尾上和駿、大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2026 Bandai Namco Entertainment Inc.\n\n#篠澤広 #初星学園 #真島ゆろ #ASOBINOTES #Hatsuboshi_Gakuen #idolmaster_Gakuen"
        }
      }
    }
  },
  {
    "alias": "H25",
    "logical_source_id": "1K9In8GKh9pP041E6A0zg3hyX-lKdug7G",
    "character": "HIRO",
    "role": "ENDLESS DANCE Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ENDLESS DANCE」(篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
    "sha256": "2599c7b4d83b267a76204cd8a463f47f2ebf2bcf995d7305be7b74b311d2f855",
    "bytes": 44652220,
    "duration_seconds": 109.435646,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "2599c7b4d83b267a76204cd8a463f47f2ebf2bcf995d7305be7b74b311d2f855",
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
          "duration_ts": 1679872,
          "duration": "109.366667",
          "bit_rate": "3034304",
          "bits_per_raw_sample": "8",
          "nb_frames": "6562",
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
          "duration_ts": 4826112,
          "duration": "109.435646",
          "bit_rate": "127999",
          "nb_frames": "4713",
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
          "duration_ts": 9849208,
          "duration": "109.435644",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ENDLESS DANCE」(篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p60).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "109.435646",
        "size": "44652220",
        "bit_rate": "3264181",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「ENDLESS DANCE」(篠澤広 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20260227",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=lKA4swUcuNE",
          "description": "「ENDLESS DANCE」(#篠澤広  SSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm46000445\n\n作詞・作曲：首藤義勝\n編曲：藤永龍太郎(Elements Garden)\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「ENDLESS DANCE」(#篠澤広  SSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm46000445\n\n作詞・作曲：首藤義勝\n編曲：藤永龍太郎(Elements Garden)\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H26",
    "logical_source_id": "1laiDZzcPX6UA-Hz9NHaoAvdc8bX2Q6nW",
    "character": "HIRO",
    "role": "標 China/Hiro duet rendering",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\標　倉本千奈&篠澤広(ゆめぱしー)ver-(720p30).mp4",
    "sha256": "2507b558c9997147a2aee961d9c1efcd24e0f903761c3a825e42485e75469902",
    "bytes": 28997967,
    "duration_seconds": 228.182494,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "2507b558c9997147a2aee961d9c1efcd24e0f903761c3a825e42485e75469902",
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
          "mime_codec_string": "avc1.64001f",
          "width": 1040,
          "height": 720,
          "coded_width": 1040,
          "coded_height": 720,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "13:9",
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
          "duration_ts": 3504128,
          "duration": "228.133333",
          "bit_rate": "857622",
          "bits_per_raw_sample": "8",
          "nb_frames": "6844",
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
          "duration_ts": 10062848,
          "duration": "228.182494",
          "bit_rate": "127999",
          "nb_frames": "9827",
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
          "duration_ts": 20536424,
          "duration": "228.182489",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\標　倉本千奈&篠澤広(ゆめぱしー)ver-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "228.182494",
        "size": "28997967",
        "bit_rate": "1016658",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "標　倉本千奈&篠澤広(ゆめぱしー)ver",
          "artist": "てるよし",
          "genre": "People & Blogs",
          "date": "20260811",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=yKtHmE68mS4",
          "description": "初星学園校歌 標(しるべ)\n歌：初星学園  作詞： 十王邦夫  作曲：佐藤貴文\n\n初星きらめく 新たな夜が明ける\n暁星仰ぎ見て 日々がはじまる\n\n文化の街の傍らに\n我が学び舎の門はあり\n陽光(ひかり)浴びて 星の種よ 芽吹け\n\n大空に夢を 今託してはばたけ\n遥かな未来へ 憧れを響かせて\n友と 今高らかに歌おう\n心を照らして\n\nああ 若人よ 世界へ挑め\n総喝采\n\n初星もとめる 新たな挑戦の刻\n白星仰ぎ見て 布を染める\n\n我らが研鑽積み上げ\n富士より絢爛(けんらん)纏(まと)いて\n光集め星の花よ輝け\n\n星々の夢よ 今気高くはばたけ\n遥かな宙へと 手を伸ばし咲き誇れ\n光 見失うそのときには\n寄り添う心を\n\nああ 若人よ 信じて笑え\n総喝采\n\n倉本千奈 3rd Single「空と約束」\n2. 標 [倉本千奈 Solo Ver.]\n\n篠澤広 3rd Single「サンフェーデッド」\n2.標 [篠澤 広 Solo Ver.]\n\n#学マス \n#学園アイドルマスター \n#倉本千奈 \n#篠澤広 \n#ゆめぱしー\n＃標",
          "synopsis": "初星学園校歌 標(しるべ)\n歌：初星学園  作詞： 十王邦夫  作曲：佐藤貴文\n\n初星きらめく 新たな夜が明ける\n暁星仰ぎ見て 日々がはじまる\n\n文化の街の傍らに\n我が学び舎の門はあり\n陽光(ひかり)浴びて 星の種よ 芽吹け\n\n大空に夢を 今託してはばたけ\n遥かな未来へ 憧れを響かせて\n友と 今高らかに歌おう\n心を照らして\n\nああ 若人よ 世界へ挑め\n総喝采\n\n初星もとめる 新たな挑戦の刻\n白星仰ぎ見て 布を染める\n\n我らが研鑽積み上げ\n富士より絢爛(けんらん)纏(まと)いて\n光集め星の花よ輝け\n\n星々の夢よ 今気高くはばたけ\n遥かな宙へと 手を伸ばし咲き誇れ\n光 見失うそのときには\n寄り添う心を\n\nああ 若人よ 信じて笑え\n総喝采\n\n倉本千奈 3rd Single「空と約束」\n2. 標 [倉本千奈 Solo Ver.]\n\n篠澤広 3rd Single「サンフェーデッド」\n2.標 [篠澤 広 Solo Ver.]\n\n#学マス \n#学園アイドルマスター \n#倉本千奈 \n#篠澤広 \n#ゆめぱしー\n＃標"
        }
      }
    }
  },
  {
    "alias": "H27",
    "logical_source_id": "1obrkIYn5VQl-7hkwnbC0Jck6ILDQH7Tv",
    "character": "HIRO",
    "role": "ガラクタロード Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ガラクタロード」(篠澤広フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4",
    "sha256": "e86e19219cb8613f0b923b27c7ddeff7060e98e5acade63fb2abef2341c99edd",
    "bytes": 47060211,
    "duration_seconds": 163.86322,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "e86e19219cb8613f0b923b27c7ddeff7060e98e5acade63fb2abef2341c99edd",
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
          "chroma_location": "topleft",
          "field_order": "progressive",
          "is_avc": "true",
          "nal_length_size": "4",
          "id": "0x1",
          "r_frame_rate": "30/1",
          "avg_frame_rate": "30/1",
          "time_base": "1/15360",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2516480,
          "duration": "163.833333",
          "bit_rate": "2091379",
          "bits_per_raw_sample": "8",
          "nb_frames": "4915",
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
          "duration_ts": 7226368,
          "duration": "163.863220",
          "bit_rate": "127999",
          "nb_frames": "7057",
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
          "duration_ts": 14747690,
          "duration": "163.863222",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ガラクタロード」(篠澤広フェスSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "163.863220",
        "size": "47060211",
        "bit_rate": "2297536",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「ガラクタロード」(篠澤広フェスSSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20260526",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=D8UJjnGzFV0",
          "description": "「ガラクタロード」(#篠澤広  フェスSSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm46357657\n\n作歌：篠澤広 (CV. 川村玲奈)\n作詞：Rou-hou\n作曲：佐藤貴文\n編曲：鈴木俊介、大澤めい (Bandai Namco Studios Inc.)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「ガラクタロード」(#篠澤広  フェスSSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm46357657\n\n作歌：篠澤広 (CV. 川村玲奈)\n作詞：Rou-hou\n作曲：佐藤貴文\n編曲：鈴木俊介、大澤めい (Bandai Namco Studios Inc.)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H28",
    "logical_source_id": "19ZDDv3IlyKBryQL9U9Xi7akxuW_ZJ5zt",
    "character": "HIRO",
    "role": "みちなるひろがる Hiro/China rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「みちなるひろがる」 (篠澤広・倉本千奈 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4",
    "sha256": "938bfd03b2b0c613425875cc8ab6cf27ea95e776b69dc6c31e4e76da6f3ffc91",
    "bytes": 42848893,
    "duration_seconds": 154.505578,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "938bfd03b2b0c613425875cc8ab6cf27ea95e776b69dc6c31e4e76da6f3ffc91",
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
          "duration_ts": 2372096,
          "duration": "154.433333",
          "bit_rate": "2021197",
          "bits_per_raw_sample": "8",
          "nb_frames": "4633",
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
          "duration_ts": 6813696,
          "duration": "154.505578",
          "bit_rate": "127999",
          "nb_frames": "6654",
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
          "duration_ts": 13905502,
          "duration": "154.505578",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「みちなるひろがる」 (篠澤広・倉本千奈 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "154.505578",
        "size": "42848893",
        "bit_rate": "2218632",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「みちなるひろがる」 (篠澤広・倉本千奈 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20260127",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=SZSQ1ZngnVg",
          "description": "「みちなるひろがる」 (#篠澤広 ・倉本千奈 SSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45881359\n\n作詞・作曲・編曲：いよわ\n歌：篠澤広 (CV. 川村玲奈)・倉本千奈 (CV. 伊藤舞音)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「みちなるひろがる」 (#篠澤広 ・倉本千奈 SSR) 4K HDR 60fps\nhttps://www.nicovideo.jp/watch/sm45881359\n\n作詞・作曲・編曲：いよわ\n歌：篠澤広 (CV. 川村玲奈)・倉本千奈 (CV. 伊藤舞音)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H29",
    "logical_source_id": "1S15fh_ENDBLtY8IhjdsHo1D4B8YjKp3E",
    "character": "HIRO",
    "role": "みちなるひろがる authored official MV",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「みちなるひろがる」Official Music Video (HATSUBOSHI GAKUEN - Unknown Unbound)-(720p30).mp4",
    "sha256": "d65297b2725bc3216ae071773e83b698bbabdb785a2b56b279485f1d4be291ef",
    "bytes": 13270085,
    "duration_seconds": 205.334059,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "d65297b2725bc3216ae071773e83b698bbabdb785a2b56b279485f1d4be291ef",
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
          "duration_ts": 3152896,
          "duration": "205.266667",
          "bit_rate": "230070",
          "bits_per_raw_sample": "8",
          "nb_frames": "6158",
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
          "duration_ts": 9055232,
          "duration": "205.334059",
          "bit_rate": "255999",
          "nb_frames": "8843",
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
          "duration_ts": 18480065,
          "duration": "205.334056",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\初星学園 「みちなるひろがる」Official Music Video (HATSUBOSHI GAKUEN - Unknown Unbound)-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "205.334059",
        "size": "13270085",
        "bit_rate": "517014",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "初星学園 「みちなるひろがる」Official Music Video (HATSUBOSHI GAKUEN - Unknown Unbound)",
          "artist": "HATSUBOSHI GAKUEN",
          "genre": "Music",
          "date": "20260127",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=qwfpgEhngVI",
          "description": "[EN Credits.]\nUnknown Unbound\n\nSong by China Kuramoto (VA. Mao Ito), Hiro Shinosawa (VA. Reina Kawamura)\nLyric written, Composed, Arranged, Movie created by Iyowa\n\nMV Producer：KEISUKE YANO\n\n[JP Credits.]\nみちなるひろがる\n\n歌：倉本千奈 (CV. 伊藤舞音) 、篠澤広 (CV. 川村玲奈) \n作詞・作曲・編曲・動画：いよわ\n\nMV Producer：矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 尾上和駿、大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2026 Bandai Namco Entertainment Inc.\n\n#初星学園 #いよわ #ASOBINOTES\n#倉本千奈 #篠澤広  \n#Hatsuboshi_Gakuen #idolmaster_Gakuen",
          "synopsis": "[EN Credits.]\nUnknown Unbound\n\nSong by China Kuramoto (VA. Mao Ito), Hiro Shinosawa (VA. Reina Kawamura)\nLyric written, Composed, Arranged, Movie created by Iyowa\n\nMV Producer：KEISUKE YANO\n\n[JP Credits.]\nみちなるひろがる\n\n歌：倉本千奈 (CV. 伊藤舞音) 、篠澤広 (CV. 川村玲奈) \n作詞・作曲・編曲・動画：いよわ\n\nMV Producer：矢野圭将\n\n------------------------------\nMusic Label : ASOBINOTES\nLabel & MV Producer : 矢野圭将\nLabel Director : 尾上和駿、大石和馬\nSound Producer : 佐藤貴文\nSound Director : 大澤めい\n------------------------------\n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2026 Bandai Namco Entertainment Inc.\n\n#初星学園 #いよわ #ASOBINOTES\n#倉本千奈 #篠澤広  \n#Hatsuboshi_Gakuen #idolmaster_Gakuen"
        }
      }
    }
  },
  {
    "alias": "H30",
    "logical_source_id": "1UaOzLCa1P0Yd0Npw86Tj65NFGubgbbhw",
    "character": "HIRO",
    "role": "ハッピーミルフィーユ Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ハッピーミルフィーユ」(篠澤広 バレンタインSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4",
    "sha256": "3ea6272131f70b2382e1908b45378de821eb4ff4cf6759eae2b2c6e504534991",
    "bytes": 26195006,
    "duration_seconds": 101.169342,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "3ea6272131f70b2382e1908b45378de821eb4ff4cf6759eae2b2c6e504534991",
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
          "duration_ts": 1552896,
          "duration": "101.100000",
          "bit_rate": "1856588",
          "bits_per_raw_sample": "8",
          "nb_frames": "3033",
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
          "duration_ts": 4461568,
          "duration": "101.169342",
          "bit_rate": "127999",
          "nb_frames": "4357",
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
          "duration_ts": 9105241,
          "duration": "101.169344",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「ハッピーミルフィーユ」(篠澤広 バレンタインSSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "101.169342",
        "size": "26195006",
        "bit_rate": "2071378",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「ハッピーミルフィーユ」(篠澤広 バレンタインSSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20250204",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=NRP105m5BgY",
          "description": "「ハッピーミルフィーユ」(#篠澤広 バレンタインSSR)4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44613443\n\n作詞・編曲：ナナホシ管弦楽団\n作曲 ：岩見 陸\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「ハッピーミルフィーユ」(#篠澤広 バレンタインSSR)4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44613443\n\n作詞・編曲：ナナホシ管弦楽団\n作曲 ：岩見 陸\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H31",
    "logical_source_id": "16urNa641Iy6wsq-EWxQaqYgyFX4r1sfM",
    "character": "HIRO",
    "role": "仮装狂騒曲 Hiro rendered performance",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「仮装狂騒曲」(篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4",
    "sha256": "7122d7dd6aa4a193a7a021f05d2ac8f68efffa7f630ac129f653f95eb5830925",
    "bytes": 25770491,
    "duration_seconds": 105.674014,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "7122d7dd6aa4a193a7a021f05d2ac8f68efffa7f630ac129f653f95eb5830925",
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
          "duration_ts": 1622528,
          "duration": "105.633333",
          "bit_rate": "1749067",
          "bits_per_raw_sample": "8",
          "nb_frames": "3169",
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
          "duration_ts": 4660224,
          "duration": "105.674014",
          "bit_rate": "127999",
          "nb_frames": "4551",
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
          "duration_ts": 9510661,
          "duration": "105.674011",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\4K HDR「仮装狂騒曲」(篠澤広 SSR)【学マス⧸学園アイドルマスタ⧸Gakuen idolm@ster MV】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "105.674014",
        "size": "25770491",
        "bit_rate": "1950942",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "4K HDR「仮装狂騒曲」(篠澤広 SSR)【学マス/学園アイドルマスタ/Gakuen idolm@ster MV】",
          "artist": "十六夜カズヤP / 16KazuyaP",
          "genre": "Gaming",
          "date": "20241008",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=I3_A_WOPuFQ",
          "description": "「仮装狂騒曲」(#篠澤広  SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44191347\n\n作詞：TOPHAMHAT-KYO (FAKE TYPE.)\n作曲：FAKE TYPE.\n編曲：DYES IWASAKI (FAKE TYPE.)\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師",
          "synopsis": "「仮装狂騒曲」(#篠澤広  SSR) 4K #HDR 60fps\nhttps://www.nicovideo.jp/watch/sm44191347\n\n作詞：TOPHAMHAT-KYO (FAKE TYPE.)\n作曲：FAKE TYPE.\n編曲：DYES IWASAKI (FAKE TYPE.)\n歌：篠澤広 (CV. 川村玲奈)\n\nゲーム内レコード:\nアイドルマスター #学園アイドルマスター #学マス #アイマス\nrecorded from game:\nGakuen iDOLM@STER\nhttps://gakuen.idolmaster-official.jp/\n#偶像大師 学園偶像大師"
        }
      }
    }
  },
  {
    "alias": "H32",
    "logical_source_id": "1K1pfcfYCj7Xgs1Z5z0bbjwoo3Go7YRiq",
    "character": "HIRO",
    "role": "メクルメ official Game Size lyric video",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\【学マス】篠澤 広 誕生日記念Single「メクルメ」- Game Sizeリリックビデオ CD予約受付中！【アイドルマスター】-(720p30).mp4",
    "sha256": "75d8ede001bf0ba7fc78938a80fdede712237073eea20a6647b896cdcb5475ff",
    "bytes": 25653028,
    "duration_seconds": 152.137143,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "75d8ede001bf0ba7fc78938a80fdede712237073eea20a6647b896cdcb5475ff",
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
          "r_frame_rate": "30000/1001",
          "avg_frame_rate": "30000/1001",
          "time_base": "1/30000",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 4562558,
          "duration": "152.085267",
          "bit_rate": "1151916",
          "bits_per_raw_sample": "8",
          "nb_frames": "4558",
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
          "duration_ts": 6709248,
          "duration": "152.137143",
          "bit_rate": "127999",
          "nb_frames": "6552",
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
          "duration_ts": 13692343,
          "duration": "152.137144",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\【学マス】篠澤 広 誕生日記念Single「メクルメ」- Game Sizeリリックビデオ CD予約受付中！【アイドルマスター】-(720p30).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "152.137143",
        "size": "25653028",
        "bit_rate": "1348942",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【学マス】篠澤 広 誕生日記念Single「メクルメ」- Game Sizeリリックビデオ CD予約受付中！【アイドルマスター】",
          "artist": "アイドルマスターチャンネル",
          "genre": "Gaming",
          "date": "20241220",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=DLkNQgh4Ons",
          "description": "『篠澤広誕生日記念セット』アソビストアにて受注受付中！\n購入ページ： https://shop.asobistore.jp/products/detail/211255-00-00-00\n\n受注期間：2024年12月21日（土）～2025年1月13日（月・祝）\n商品詳細：\n＜篠澤広　誕生日記念セット＞\n・学園アイドルマスター篠澤広 CD「メクルメ」\n・学園アイドルマスター篠澤広 アクリルキーホルダー\n・学園アイドルマスター篠澤広 缶バッジ\n・学園アイドルマスター篠澤広 アクリルパネル\n\n------------------------------\nCredits.\n▶キャラクター原案\n南野あき\n\n▶Music\n歌：篠澤 広 (CV. 川村玲奈)\n作詞・作曲・編曲：フロクロ\n\n▶Movie \nDirector：YCM\nComposite：Riesz\nLive2D：HOSHIMIYA MIZUKI\nIntro lyric design：CON\n\n------------------------------ \nMusic Label：ASOBINOTES \nMV Producer：子川拓哉 \n------------------------------ \n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2024 Bandai Namco Entertainment Inc.\n#学マス #初星学園 #ASOBINOTES\n \n\n◆アイドルマスターチャンネルとは？\n「YouTubeでプロデュースがもっと楽しくなる！\nすべての「アイドルマスター」プロデューサーさんたちの集う場所。」を掲げ、\nプロデューサーさんたちのプロデュース活動を推進できるようなコンテンツをお届けしていきます！\n\n= = = = = = = = = = =\n【アイドルマスターチャンネル公式SNS】\nhttps://x.com/imas_ch\n【アイドルマスター公式SNS】\nhttps://x.com/imas_official\n【シリーズポータルサイトはこちら】\nhttps://idolmaster-official.jp/\n【アイドルマスター関連グッズ情報はこちらから！- アソビストア】\nhttps://shop.asobistore.jp/category/10107\n= = = = = = = = = = =\n#アイマスch",
          "synopsis": "『篠澤広誕生日記念セット』アソビストアにて受注受付中！\n購入ページ： https://shop.asobistore.jp/products/detail/211255-00-00-00\n\n受注期間：2024年12月21日（土）～2025年1月13日（月・祝）\n商品詳細：\n＜篠澤広　誕生日記念セット＞\n・学園アイドルマスター篠澤広 CD「メクルメ」\n・学園アイドルマスター篠澤広 アクリルキーホルダー\n・学園アイドルマスター篠澤広 缶バッジ\n・学園アイドルマスター篠澤広 アクリルパネル\n\n------------------------------\nCredits.\n▶キャラクター原案\n南野あき\n\n▶Music\n歌：篠澤 広 (CV. 川村玲奈)\n作詞・作曲・編曲：フロクロ\n\n▶Movie \nDirector：YCM\nComposite：Riesz\nLive2D：HOSHIMIYA MIZUKI\nIntro lyric design：CON\n\n------------------------------ \nMusic Label：ASOBINOTES \nMV Producer：子川拓哉 \n------------------------------ \n\n「学マス」で検索！\n▶学マスアプリのDLはこちら！\nhttps://app.adjust.com/19512hnz\n\nTHE IDOLM@STER™& ©Bandai Namco Entertainment Inc.\nⓅ2024 Bandai Namco Entertainment Inc.\n#学マス #初星学園 #ASOBINOTES\n \n\n◆アイドルマスターチャンネルとは？\n「YouTubeでプロデュースがもっと楽しくなる！\nすべての「アイドルマスター」プロデューサーさんたちの集う場所。」を掲げ、\nプロデューサーさんたちのプロデュース活動を推進できるようなコンテンツをお届けしていきます！\n\n= = = = = = = = = = =\n【アイドルマスターチャンネル公式SNS】\nhttps://x.com/imas_ch\n【アイドルマスター公式SNS】\nhttps://x.com/imas_official\n【シリーズポータルサイトはこちら】\nhttps://idolmaster-official.jp/\n【アイドルマスター関連グッズ情報はこちらから！- アソビストア】\nhttps://shop.asobistore.jp/category/10107\n= = = = = = = = = = =\n#アイマスch"
        }
      }
    }
  },
  {
    "alias": "H33",
    "logical_source_id": "10pmdSfOxpvp5x_zUh8KwmtgzZ9ALNI5C",
    "character": "HIRO",
    "role": "メクルメ full/static presentation",
    "path": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\メクルメ-(720p25).mp4",
    "sha256": "f294b9bb1c3c1ab3113d2e96c038d3e7b3e584287b4e3180a66d18d01677da32",
    "bytes": 8185374,
    "duration_seconds": 196.891995,
    "video_stream": 0,
    "audio_stream": 1,
    "prior_expected_sha256": "f294b9bb1c3c1ab3113d2e96c038d3e7b3e584287b4e3180a66d18d01677da32",
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
          "width": 720,
          "height": 720,
          "coded_width": 720,
          "coded_height": 720,
          "has_b_frames": 1,
          "sample_aspect_ratio": "1:1",
          "display_aspect_ratio": "1:1",
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
          "r_frame_rate": "25/1",
          "avg_frame_rate": "25/1",
          "time_base": "1/12800",
          "start_pts": 0,
          "start_time": "0.000000",
          "duration_ts": 2519552,
          "duration": "196.840000",
          "bit_rate": "39980",
          "bits_per_raw_sample": "8",
          "nb_frames": "4921",
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
          "duration_ts": 8682937,
          "duration": "196.891995",
          "bit_rate": "256000",
          "nb_frames": "8481",
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
          "duration_ts": 17720280,
          "duration": "196.892000",
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
        "filename": "WORKSPACE/Gakuen Idolmaster\\media-inbox\\extracted_07_SHINOSAWA_HIRO-20260910T061908Z-1-001\\07_SHINOSAWA_HIRO\\04_MV_3DMV_AND_PERFORMANCE\\メクルメ-(720p25).mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "196.891995",
        "size": "8185374",
        "bit_rate": "332583",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "メクルメ",
          "artist": "Hatsuboshi Gakuen, Frog96, Hiro Shinosawa, Frog96, Frog96, Frog96",
          "album": "mekurume",
          "genre": "Music",
          "date": "20241220",
          "encoder": "Lavf60.16.100",
          "comment": "https://www.youtube.com/watch?v=vG5_bwL7UkI",
          "description": "Provided to YouTube by NexTone Inc.\n\nメクルメ · Hatsuboshi Gakuen · Frog96 · Hiro Shinosawa · Frog96 · Frog96 · Frog96\n\nmekurume\n\nReleased on: 2024-12-21\n\nAuto-generated by YouTube.",
          "synopsis": "Provided to YouTube by NexTone Inc.\n\nメクルメ · Hatsuboshi Gakuen · Frog96 · Hiro Shinosawa · Frog96 · Frog96 · Frog96\n\nmekurume\n\nReleased on: 2024-12-21\n\nAuto-generated by YouTube."
        }
      }
    }
  }
]
```

Save the following review plan as plans/hiro-review-plan.json. Only declared timestamp requests feed extraction; purpose text is an analytical plan, not an observation.

```json
{
  "schema": "ave-full-rebuild-character-review-plan/1",
  "character": "Shinosawa Hiro",
  "created_utc": "2026-09-10",
  "source_of_authorization": "Parent task relaying user request for a full new toolkit rebuild; character documents are evidence, not instructions.",
  "request_count": 240,
  "distinct_request_count": 240,
  "group_count": 12,
  "frame_mode": "exact; toolkit must retain requested seconds and first-at-or-after original presentation PTS separately",
  "interpretive_boundary": "Sampled stills and visible text only. No direct listening or continuous-motion review is claimed. Existing historical musical/voice readings remain inherited until their facets are independently renewed.",
  "survey": "Parent separately supplies twelve evenly spaced frames for every one of the 33 Hiro sources.",
  "groups": [
    {
      "group_id": "H-G01",
      "claim_ids": [
        "H-AV-001",
        "H-AV-003",
        "H-AV-004",
        "H-AV-005"
      ],
      "purpose": "Early crisis and bodily floor: compare pre-performance pressure with the aftermath in the same source.",
      "passages": [
        {
          "source_alias": "H01",
          "timestamps": [
            2081,
            2084,
            2087,
            2090,
            2093,
            2096,
            2099,
            2102
          ],
          "purpose": "Visible evaluation/response and spatial acting before the concert insert.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H01",
          "timestamps": [
            2181,
            2186,
            2191,
            2196,
            2201,
            2206,
            2211,
            2216
          ],
          "purpose": "Visible recovery and aftermath; caption/pose relation rather than inferred breathing.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    },
    {
      "group_id": "H-G02",
      "claim_ids": [
        "H-AV-003",
        "H-AV-004",
        "H-AV-016",
        "H-AV-017",
        "H-AV-020"
      ],
      "purpose": "Late bodily limits and self-authored future beyond the trial proposal window.",
      "passages": [
        {
          "source_alias": "H04",
          "timestamps": [
            2908,
            2911,
            2914,
            2917,
            2920,
            2923,
            2926,
            2929
          ],
          "purpose": "Dear036 bodily-limit passage; identify who states the limitation and how the body is framed.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H04",
          "timestamps": [
            3246,
            3249,
            3252,
            3255,
            3258,
            3261,
            3264,
            3267
          ],
          "purpose": "Dear037 own-dream/future passage; separate aspiration from a demonstrated sustainable floor.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    },
    {
      "group_id": "H-G03",
      "claim_ids": [
        "H-AV-007",
        "H-AV-008",
        "H-AV-014"
      ],
      "purpose": "Goddess reception and ordinary cute desire in nearby Dear-route scenes.",
      "passages": [
        {
          "source_alias": "H03",
          "timestamps": [
            1048,
            1051,
            1054,
            1057,
            1060,
            1063,
            1066,
            1069
          ],
          "purpose": "Reception-category scene: visible attribution and small expression changes.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H03",
          "timestamps": [
            1128,
            1130,
            1132,
            1134,
            1136,
            1138,
            1140,
            1142
          ],
          "purpose": "Cute-image scene: framing/caption relation without a voice-register claim.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    },
    {
      "group_id": "H-G04",
      "claim_ids": [
        "H-AV-008",
        "H-AV-012",
        "H-AV-017",
        "H-AV-018"
      ],
      "purpose": "CIDOL018 origin confession and Producer/shared-dream bridge.",
      "passages": [
        {
          "source_alias": "H09",
          "timestamps": [
            137,
            139,
            141,
            143,
            145,
            147,
            149,
            151
          ],
          "purpose": "Cuteness motive versus prepared unsuitability answer; verify captions against frozen script.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H09",
          "timestamps": [
            488,
            490,
            492,
            494,
            496,
            498,
            500,
            502
          ],
          "purpose": "Late hobby/dream bridge; distinguish Hiro and Producer text and retained authority asymmetry.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    },
    {
      "group_id": "H-G05",
      "claim_ids": [
        "H-AV-007",
        "H-AV-015",
        "H-AV-018",
        "H-AV-020"
      ],
      "purpose": "Middle/late responsibility and ambition outside the exact trial ending.",
      "passages": [
        {
          "source_alias": "H03",
          "timestamps": [
            1559,
            1561,
            1563,
            1565,
            1567,
            1569,
            1571,
            1573
          ],
          "purpose": "Image/audience relation around prior goddess-register landmark; inspect actual captions before interpreting.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H04",
          "timestamps": [
            946,
            949,
            952,
            955,
            958,
            961,
            964,
            967
          ],
          "purpose": "Dear031 dream/future landmark: locate explicit commitment and its limits.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    },
    {
      "group_id": "H-G06",
      "claim_ids": [
        "H-AV-001",
        "H-AV-002",
        "H-AV-008",
        "H-AV-014"
      ],
      "purpose": "Seasonal dialogue control for deliberate play, peer reaction and cute sociality.",
      "passages": [
        {
          "source_alias": "H10",
          "timestamps": [
            266,
            268,
            270,
            272,
            274,
            276,
            278,
            280
          ],
          "purpose": "Happy Millefeuille commu peer scene; read visible comedy/social context.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H11",
          "timestamps": [
            279,
            281,
            283,
            285,
            287,
            289,
            291,
            293
          ],
          "purpose": "Costume commu role-play scene; compare visible responses without judging audible deadpan.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    },
    {
      "group_id": "H-G07",
      "claim_ids": [
        "H-AV-009",
        "H-AV-011",
        "H-AV-015",
        "H-AV-018"
      ],
      "purpose": "Song-commu control for the proposed principal-work developmental sequence.",
      "passages": [
        {
          "source_alias": "H05",
          "timestamps": [
            283,
            285,
            287,
            289,
            291,
            293,
            295,
            297
          ],
          "purpose": "Koukei commu neighbourhood: identify concrete audience or self-presentation stakes.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H06",
          "timestamps": [
            316,
            318,
            320,
            322,
            324,
            326,
            328,
            330
          ],
          "purpose": "Contrast commu neighbourhood: identify concrete relational/developmental caption content.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H08",
          "timestamps": [
            301,
            303,
            305,
            307,
            309,
            311,
            313,
            315
          ],
          "purpose": "Sunfaded commu neighbourhood: inspect responsibility or attachment framing.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    },
    {
      "group_id": "H-G08",
      "claim_ids": [
        "H-AV-004",
        "H-AV-009",
        "H-AV-010",
        "H-AV-011",
        "H-AV-018"
      ],
      "purpose": "Principal rendered performances in previously unreviewed bounded sections.",
      "passages": [
        {
          "source_alias": "H12",
          "timestamps": [
            101,
            103,
            105,
            107,
            109,
            111,
            113,
            115
          ],
          "purpose": "Koukei stage geometry, posture, audience/camera scale.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H15",
          "timestamps": [
            143,
            145,
            147,
            149,
            151,
            153,
            155,
            157
          ],
          "purpose": "Contrast stage geometry, posture and graphic framing.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H17",
          "timestamps": [
            63,
            65,
            67,
            69,
            71,
            73,
            75,
            77
          ],
          "purpose": "Sunfaded stage/body relation; compare staging rather than technical skill chronology.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    },
    {
      "group_id": "H-G09",
      "claim_ids": [
        "H-AV-009",
        "H-AV-010",
        "H-AV-011",
        "H-AV-018"
      ],
      "purpose": "Authored graphic forms beyond previous close-reading windows.",
      "passages": [
        {
          "source_alias": "H14",
          "timestamps": [
            147,
            149,
            151,
            153,
            155,
            157,
            159,
            161
          ],
          "purpose": "Koukei authored montage: graphic/editorial motifs, no literal continuity inference.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H24",
          "timestamps": [
            143,
            145,
            147,
            149,
            151,
            153,
            155,
            157
          ],
          "purpose": "Contemporary Dance authored form: represented body/action and textual composition.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H32",
          "timestamps": [
            101,
            103,
            105,
            107,
            109,
            111,
            113,
            115
          ],
          "purpose": "Mekurume lyric-video form: graphic transformations and character imagery.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    },
    {
      "group_id": "H-G10",
      "claim_ids": [
        "H-AV-004",
        "H-AV-009",
        "H-AV-010",
        "H-AV-014"
      ],
      "purpose": "Common and seasonal controls against principal-only novelty and goddess exclusivity.",
      "passages": [
        {
          "source_alias": "H25",
          "timestamps": [
            71,
            73,
            75,
            77,
            79,
            81,
            83,
            85
          ],
          "purpose": "ENDLESS DANCE common repertoire visual construction.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H23",
          "timestamps": [
            23,
            25,
            27,
            29,
            31,
            33,
            35,
            37
          ],
          "purpose": "Miracle Nanau comic/cute bodily and graphic range.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H30",
          "timestamps": [
            51,
            53,
            55,
            57,
            59,
            61,
            63,
            65
          ],
          "purpose": "Happy Millefeuille seasonal framing and pose.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H31",
          "timestamps": [
            51,
            53,
            55,
            57,
            59,
            61,
            63,
            65
          ],
          "purpose": "Kasou Kyousoukyoku theatrical/costume framing; do not interpret RMS ratio as expression.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    },
    {
      "group_id": "H-G11",
      "claim_ids": [
        "H-AV-013",
        "H-AV-014",
        "H-AV-017"
      ],
      "purpose": "Hiro/China duet bodies versus authored and scenery-only source forms.",
      "passages": [
        {
          "source_alias": "H28",
          "timestamps": [
            125,
            127,
            129,
            131,
            133,
            135,
            137,
            139
          ],
          "purpose": "Rendered mutual orientation and allocation of frame space.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H29",
          "timestamps": [
            145,
            147,
            149,
            151,
            153,
            155,
            157,
            159
          ],
          "purpose": "Authored unit imagery and individual/shared focality.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H26",
          "timestamps": [
            91,
            93,
            95,
            97,
            99,
            101,
            103,
            105
          ],
          "purpose": "Test whether this passage supplies bodies at all; retain scenery/lyric distinction.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    },
    {
      "group_id": "H-G12",
      "claim_ids": [
        "H-AV-004",
        "H-AV-019"
      ],
      "purpose": "Derivative improvement montage as reception argument, paired with public Garakuta presentation.",
      "passages": [
        {
          "source_alias": "H13",
          "timestamps": [
            89,
            91,
            93,
            95,
            97,
            99,
            101,
            103
          ],
          "purpose": "Record visible edit/state changes without treating montage ordering as canonical development.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        },
        {
          "source_alias": "H27",
          "timestamps": [
            115,
            117,
            119,
            121,
            123,
            125,
            127,
            129
          ],
          "purpose": "Public cute/celebratory staging counterpart to private CIDOL018 confession; no assumed matching chronology.",
          "locator_basis": "Targeted neighbourhood of a prior documented landmark; new images must be inspected before making any fresh observation."
        }
      ]
    }
  ],
  "import_prior_evidence": [
    {
      "artifact": "WORKSPACE/Gakuen Idolmaster/work/ave-targeted-trial-20260910/observations/hiro.json",
      "sha256": "3ab6bc2f5c3104948457e4dcc6ef0cc2c0e825f4413c0d75749d03cd8ff06ad1",
      "claims": [
        "H-AV-002",
        "H-AV-005",
        "H-AV-006"
      ],
      "scope": "Exact trial H03 performance/interruption and H04 one-time proposal; carried-forward observations, not new full-rebuild perception."
    },
    {
      "artifact": "WORKSPACE/Gakuen Idolmaster/work/ave-targeted-trial-20260910/observations/hiro_delta.md",
      "sha256": "74bc8dcb0a908b62ea2ebe395b1691db00ac331153dd31e1d3e1ffe8a800e273",
      "scope": "Carry local deliberate-teasing refinement and pressure/performance/return staging; apply the independently locked-text Producer attribution correction."
    }
  ],
  "prior_trial_no_repeat_primary_windows": {
    "H03": [
      [
        1970,
        2016
      ],
      [
        2192,
        2224
      ]
    ],
    "H04": [
      [
        3160,
        3205
      ]
    ]
  },
  "source_constraints": {
    "H04": "Use full original SHA256 4dc80d8f2431fe8780faf59fa6b9f372f0fafcb599607ce9e04ead81bc4d4468, not old trim; old trim metrics retain their historical scope.",
    "H26": "Historical duet_performance classification does not certify choreographic bodies.",
    "H23_H31": "Near-zero/zero-P10 ratio artifacts; H31 applies numerical floor, H23 does not."
  }
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

## Optional H04 trim comparison input

Only the bounded original/trim comparison needs this earlier derivative. audio_identity.py reads this list from the sibling targeted-av-execution-20260910/work/local_identity.json; reconstruct that small input or explicitly adapt the lookup to your retained derivative. Replace the path only after checking its exact hash. Omitting the derivative leaves this comparison unperformed and does not block original-source measurements.

```json
[
  {
    "character": "HIRO",
    "alias": "H04",
    "id": "1Toi0yHcoq0jV0GMcA4JalcrlLMbnFxQO",
    "size": 519296380,
    "path": "LOCAL_USER/Downloads\\【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】-(720p60)-00.00.00.000-00.55.16.003.mp4",
    "sha256": "de92afafb3181342407ab9405f4951e820bfdafaad5b1e9538ec9d7f73ea826e",
    "probe": {
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
          "duration_ts": 198961763,
          "duration": "3316.029383",
          "bit_rate": "1111304",
          "bits_per_raw_sample": "8",
          "nb_frames": "198763",
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
          "duration_ts": 146236416,
          "duration": "3316.018503",
          "bit_rate": "128001",
          "nb_frames": "142809",
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
          "duration_ts": 298442644,
          "duration": "3316.029378",
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
        "filename": "LOCAL_USER/Downloads\\【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】-(720p60)-00.00.00.000-00.55.16.003.mp4",
        "nb_streams": 3,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "3316.029383",
        "size": "519296380",
        "bit_rate": "1252814",
        "probe_score": 100,
        "tags": {
          "major_brand": "isom",
          "minor_version": "512",
          "compatible_brands": "isomiso2avc1mp41",
          "title": "【学マス】 篠澤広 親愛度コミュ28～37話まとめ【H.I.F編】【STEP4】",
          "artist": "学Pといっしょ",
          "date": "20260526",
          "encoder": "Lavf62.3.100",
          "comment": "https://www.youtube.com/watch?v=F4QAgB54B-g",
          "genre": "Gaming",
          "description": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#篠澤広",
          "synopsis": "【注意】この動画には「学園アイドルマスター」のネタバレを含みます。\n\n\n▼学マス 好評配信中！▼\nhttp://app.adjust.com/1ai6ouao\n\n学マス公式サイト\nhttps://gakuen.idolmaster-official.jp/\n学マス公式X(Twitter)\nhttps://x.com/gkmas_official\n\n\n#学マス\n#篠澤広"
        }
      }
    },
    "generation": "current_execution",
    "source": "user_workspace"
  }
]
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
