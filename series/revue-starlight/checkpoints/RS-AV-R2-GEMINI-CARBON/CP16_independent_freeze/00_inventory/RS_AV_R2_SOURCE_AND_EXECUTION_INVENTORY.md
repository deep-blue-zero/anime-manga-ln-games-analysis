---
title: "RS-AV-R2-GEMINI-CARBON — Technical Source and Execution Inventory"
artifact_type: "source_inventory"
generation: "RS-AV-R2-GEMINI-CARBON"
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
project: "series/revue-starlight"
execution_identity: "RS-AV-R2-GEMINI-CARBON"
model: "Gemini 4 Carbon (High reasoning)"
corpus_exposure: false
document_role: "technical_source_and_execution_inventory"
---

# Technical Source and Execution Inventory (`RS-AV-R2-GEMINI-CARBON`)

> [!IMPORTANT]
> **Neutrality & Firewall Attestation**: This inventory contains strictly technical provenance, stream specifications, file digests, clock calibration, and multimodal execution parameters. It contains zero literary or interpretive claims. Zero files under `series/revue-starlight/` in `anime-manga-ln-games-analysis` and zero external paratext/notes have been opened (`existing_corpus_exposure: false`).

---

## 1. Execution Environment & Prior-Knowledge Disclosure

| Parameter | Value |
|---|---|
| **Execution Identity** | `RS-AV-R2-GEMINI-CARBON` |
| **Model & Reasoning** | Gemini 4 Carbon (High reasoning) |
| **Operating System & Shell** | Windows (`pwsh`) |
| **Media Tooling** | `ffmpeg` 8.1.1-essentials_build, `ffprobe` 8.1.1, Python 3.12.4 |
| **Run Working Root** | `urn:rs-av-r2:workspace:_rs_av_r2_gemini_carbon` (isolated local Git repository) |
| **Target Repository Clone** | `urn:rs-av-r2:workspace:anime-manga-ln-games-analysis` (untouched during independent phases A–E) |

### Prior-Knowledge Quarantine Disclosure
As required by Section 2 of the assignment specification, pretraining familiarity is disclosed transparently rather than denied:
- The model possesses general pretraining awareness of the *Shōjo Kageki Revue Starlight* animated franchise, including the nine 99th-class Seishō Music Academy students, the underground auditions overseen by the talking giraffe, the existence of Daiba Nana's mid-series temporal-loop revelation, and the 2021 theatrical sequel's post-graduation trajectory.
- **Strict Quarantine Enforcement**: Pretraining familiarity is never treated as evidence. Every prospective episode/unit reading (`TV01`→`TV12`, `TV-Only Synthesis`, `OVA01`→`OVA03`, `Sequel Film`) restricts character knowledge horizons and analytical claims strictly to evidence observed up to that unit boundary. All Japanese dialogue/lyric citations, timestamps, visual compositions, and musical observations are verified directly from local media files. Voice actors are never identified from vocal similarity. Mobile-game material (*Revue Starlight -Re LIVE-*), stage plays, manga, external wikis, and local spoiler notes are strictly excluded.

---

## 2. Corpus Roots, Build Provenance, and Manifest Discrepancies Verified by Direct Inspection

Three primary media roots were inspected on `urn:rs-av-r2:drive-root:`:
1. **Television Series (`TV01`–`TV12`)**: `urn:rs-av-r2:primary-media:Shoujo_Kageki_Revue_Starlight`
2. **OVAs (`OVA01`–`OVA03`)**: `urn:rs-av-r2:primary-media:Shoujo_Kageki_Revue_Starlight_OVA`
3. **2021 Theatrical Sequel Film (`MOVIE`)**: `urn:rs-av-r2:primary-media:Shoujo_Kageki_Revue_Starlight_Movie`

### Provenance & Structural Discrepancies Caught by File-Level Verification
1. **Directory Relocation**: All three `00_metadata/manifest.json` files record earlier pipeline build paths under `urn:rs-av-r2:primary-media:Anime...`, whereas the live roots reside under `urn:rs-av-r2:primary-media:Anime and donghua...`. Upstream source MKVs traced in `99_logs/*.log` (`urn:rs-av-r2:primary-media:[Ripple] Shoujo Kageki☆Revue Starlight [BD 1080p FLAC]\...`) remain present on disk and match recorded SHA-256 digests; note that `urn:rs-av-r2:primary-media:[Ripple]...\...` also contains an external text note (`[SPOILERS] extra fun fact notes.txt`) and CD audio folders, which are strictly quarantined and left unopened.
2. **TV `softsub_mkv` Omission vs. Clean `_pipeline/inputs` Recovery**:
   - The TV root underwent an initial English-subtitled build on `2026-08-07` (`ep01`–`ep12`, preserved only as historical metadata in OVA/Movie `final_validation.json`) and was rebuilt on `2026-10-08` (`s01e01`–`s01e12`) with time-corrected Japanese subtitles and `--skip softsub`. Consequently, `TV\02_media\softsub_mkv\` is **empty**, while `TV\02_media\hardsub_mkv\s01e01..12.analysis-hardsub.mkv` has Japanese subtitles permanently burned into the video stream.
   - Direct inspection of `TV\_pipeline\inputs\Shoujo Kageki Revue Starlight - S01E01.mkv` through `S01E12.mkv` confirmed that all twelve **unburned, original BD 1080p HEVC Main 10 + lossless 48 kHz stereo FLAC (`jpn`)** source MKVs reside inside the TV root and match `00_metadata/source_episode_identity.json` byte-for-byte across all 12 SHA-256 digests. These clean inputs serve as our primary native audiovisual witness for `TV01`–`TV12`.
3. **Non-Diegetic Seiyū Commentary Tracks on `S01E01`, `S01E05`, and `S01E10`**:
   - `ffprobe` stream enumeration of `TV\_pipeline\inputs\` revealed that `S01E01.mkv`, `S01E05.mkv`, and `S01E10.mkv` contain a second Japanese audio stream (`index 2`, `aac`, 48 kHz stereo, `title="Seyuu Commentary"`), whereas the remaining nine episodes contain only the primary `FLAC` Japanese broadcast/BD audio (`index 1`). All FFmpeg segment/audio extractions explicitly pin `-map 0:v:0 -map 0:a:0` (`index 0` video + `index 1` primary `FLAC` audio) so cast commentary is never accessed during the independent run.
4. **False `"burned_subtitles": false` Flag in `analysis_stats.json`**:
   - In `TV\03_ai_analysis\s01eXX_screenshots\analysis_stats.json`, the pipeline recorded `"burned_subtitles": false`. Direct visual inspection of `000788_auto-visual-interval_00-14-32.000.jpg` confirmed that the `s01eXX_screenshots` JPEGs were extracted from `s01eXX.analysis-hardsub.mkv` and **do** carry burned-in Japanese subtitles at bottom center. Unburned 1080p frames are therefore extracted directly from `TV\_pipeline\inputs\S01EXX.mkv` whenever clean bottom-frame visual inspection is required.
5. **Sequel Film Identity & Multichannel Audio Downmix Provenance**:
   - `MOVIE\02_media\softsub_mkv\[Veggie_Sub]_Shoujo☆Kageki_Revue_Starlight_Movie.analysis-softsub.mkv` has duration `7222.235s` (`02:00:22.235`), confirming it is the **2021 theatrical sequel** (『劇場版 少女☆歌劇 レヴュースタァライト』) and not the compilation film *Rondo Rondo Rondo*.
   - Its single audio stream (`index 1`, `aac`, 48 kHz, 2 channels, `stereo`, 160 kbps) carries metadata `title="Surround 5.1 (2 ch)"`. Inspection of the upstream source MKV (`[Veggie Sub] Shoujo☆Kageki Revue Starlight Movie.mkv`, SHA-256 `8674bf5ec2192fe0ff77e7b8d9644231da6e9444964a09cdda17d9182492685a`) confirmed that the upstream container holds both `index 1` (`aac` stereo downmix, 160 kbps) and `index 2` (`aac` 6-channel `5.1`, 635 kbps, `title="Surround 5.1 (5.1 ch)"`); `build_anime_analysis_pipeline.py` copied only `0:a:0` into `analysis-softsub.mkv`. Where mix-fidelity or center/surround stem separation matters in Phase C, the 6-channel `5.1` AAC stream (`index 2`) in the upstream container is documented and available for deterministic acoustic verification.

---

## 3. Complete Unit-by-Unit Media & Digest Inventory

### 3.1 Television Series (`TV01`–`TV12`)
- **Primary AV Witness**: `TV\_pipeline\inputs\Shoujo Kageki Revue Starlight - S01E01..12.mkv` — Matroska, Video `#0:0` `hevc` (Main 10, `yuv420p10le`, `1920x1080`, `24000/1001` = `23.976` fps, `start_time=0.000000s`); Primary Audio `#0:1` `flac` (`jpn`, `48000 Hz`, `2 ch` `stereo`, `start_time=0.000000s`); Embedded Subtitles (English localization only: `Ripple`, `Ripple - No Romaji`, `Chyuu-PAS` ASS tracks + font attachments).
- **Hardsub Derivative**: `TV\02_media\hardsub_mkv\s01e01..12.analysis-hardsub.mkv` — `hevc` 10-bit `1920x1080` `24000/1001` fps (Japanese ASS burned in) + `flac` `48000 Hz` stereo `jpn`, 0 subtitle streams.
- **Japanese Text Witness**: `TV\01_subtitles\analysis_ass\s01e01..12.analysis.ass` (byte-identical to `extracted_ass\s01e01..12.ass`) — Japanese closed-caption SRTs converted to ASS after deterministic timing alignment (`00_metadata/subtitle_timing_corrections.json`) against `faster-whisper` Japanese speech anchors and `Ripple - No Romaji` BD cue boundaries. Note: broadcast-caption conventions occasionally summarize insert/ending songs as `♪♪～` (e.g., `s01e01.analysis.ass` line 358, `0:22:32.38–0:23:59.67`), requiring direct Japanese audio transcription for uncaptioned sung lyrics.
- **Audio Derivative**: `TV\03_ai_analysis\audio\s01e01..12.complete-audio.mp3` — `mp3`, `48000 Hz`, `stereo`, `160 kbps` (`start_time=0.023021s` encoder delay).

| Unit | Clean Primary MKV (`_pipeline/inputs/`) Bytes & SHA-256 | Duration (s) | Hardsub MKV SHA-256 | Japanese `analysis.ass` Cues & SHA-256 | Timing Correction Mode (`subtitle_timing_corrections.json`) | Bundle JPEGs / Sheets / Shots |
|---|---|---:|---|---|---|---:|
| `TV01` (`s01e01`) | `1,167,641,893`<br>`a6a97c09edc8e69c1d283822afff560a50609775893e3e429e7d310c01852250` | `1446.784` | `5058d8ab8436a48856b4a2ec6c3aee199cc295423ad2b816bc59f24c59d32d61` | 344 cues<br>`06c35606770414ff4e4bde6225c6d853ba5f27c8eed992d0208cb6f9e78a8e4e` | Constant offset `-0.985s` | 962 / 49 / 462 |
| `TV02` (`s01e02`) | `1,073,255,013`<br>`899a91f16b01ffcd00f91ded0cb5e27cd9254c0225afa3920270820a6ad36eda` | `1445.615` | `00235cb62253f525fc90afd919e9866fd051319395aeb387eb12c3cbf72b02c6` | 318 cues<br>`9fdd1039588b5ef6675482ee7711a992e14e7951c8b46759ab33b73e2f82a1fb` | Piecewise step (`-1.0s` → `-12.0s` commercial-break knot) | 957 / 48 / 459 |
| `TV03` (`s01e03`) | `995,626,610`<br>`f8ebfcb4a48f3ca32ce2e303e77c58c8a4eea3e066aca985e1274736faf20aa1` | `1445.780` | `12cb58eda17bfcd8e1293603d320504360eabf995781c52e7b72e747d4499dd6` | 279 cues<br>`236353e6bc06bca90ef4c9e2eb2271c4816ddaaff3c48f48f9386b1aab511396` | Piecewise step | 922 / 47 / 444 |
| `TV04` (`s01e04`) | `1,026,276,103`<br>`b2d2bcf99d7111e3436d49df21383e330402366d35522122b4335c6e9be97d9d` | `1445.655` | `ef737120177d7350c4662a0d0c1132c35372f2dacd0607cb29813f347e70cc89` | 317 cues<br>`2e5b611a95e14a6e6cd98ae5e8bbed614beebf21b4378956904d2e0ecbe8d263` | Piecewise step | 737 / 37 / 385 |
| `TV05` (`s01e05`) | `884,638,742`<br>`7168a34c9920d88fc019354999167b9685cdc106e1cb7ecaa723e07703a994c1` | `1446.784` | `842a2d7f92d1973b17edd9397ae08495840ff44f239959590aac37ec8c1eae15` | 346 cues<br>`740e3e1c08b95b9a56c6a2ee7be9acdacdbc8144c467006145b89f946b23eb35` | Piecewise step | 893 / 45 / 420 |
| `TV06` (`s01e06`) | `910,448,052`<br>`84abc1e3e49868adbbd6adb77f5a6bfc63fa681f055a11eaf0434517ea30679d` | `1445.780` | `0425fd687245a90d5ece6f9fc7cea737d0f9747aa88b9bb3a43238cb112c6dc7` | 318 cues<br>`f13bdbd8c8e2de51e09b45a70ce65b6e55738a0ea06c35f422f77d771264da38` | Linear drift | 826 / 42 / 431 |
| `TV07` (`s01e07`) | `780,050,926`<br>`6bf41ce89db359ef18a6bc88ad0799363e96565bf7a92dd9ac584cc4620c6e46` | `1445.630` | `9d865829c41e35402edc2ee09dadab6b2aceb3a6b1a546728377f3ed28d607a8` | 331 cues<br>`67903a213ff2e89095031f0ece062517f7b51ded9363b3da51234cf0e200e9b8` | Piecewise step | 599 / 30 / 346 |
| `TV08` (`s01e08`) | `920,070,911`<br>`a8dce7414bd1e09d1e56f2f25f088c739e2fce48b0fefc7bab5cdd7496245ce3` | `1445.670` | `7852ec49d663ae8adbf4a974e76d08bb15865c07bf29777b0e5c93f0209d77db` | 273 cues<br>`8ec6c7a6b907748cc609d6d4c86206b57070f6ab29a3a2066d4aa9ce92409187` | Piecewise step | 1006 / 51 / 490 |
| `TV09` (`s01e09`) | `994,274,149`<br>`ff53750e4d26305afabd06af8c752166d4289cf7d32c7d48abc2989a417bc375` | `1447.110` | `e5e6d6085404644951c287c4640221d17d1cb7844d0502b84facf1f0379015d8` | 333 cues<br>`5c2962acaa09211abd614525ee76b285bd0d3652cffd055c7853ee51ad1f2008` | Linear drift | 776 / 39 / 374 |
| `TV10` (`s01e10`) | `1,028,296,171`<br>`78d4c66f73ccb1d51dd24a2058bf42d8005dab8d207ba634b5b65e66ecd0c8b4` | `1447.400` | `64be3df9950b96a5f4f2ab324ad009c83094738a9aefa76a865cedfdc6004967` | 288 cues<br>`631304ff21efeec341b4627fab3854372836029c98fdeff0db8106a4daf487fe` | Linear drift | 929 / 47 / 467 |
| `TV11` (`s01e11`) | `914,083,229`<br>`7b279ba1efb60a9d63cf43f88940a1e0c31d49cf77f6d4076af72bc002d996df` | `1445.780` | `8161321ce4402180fa870d7fcc8527d0034384b6b15b0c4370f21e1686ceb403` | 306 cues<br>`9c394734966462d16f5a4a9b39b8e5eef3ae23c659ded7980e3589c46e5b8ec3` | Constant offset | 723 / 37 / 360 |
| `TV12` (`s01e12`) | `895,844,595`<br>`887501ca140a02c40da82faebd09ee9795d2de9e9dfb0864af8da1ef23261b85` | `1430.805` | `d742c0202acd7745ce7df53e2ae061b2b78e20c83d89613fd562e7c3dc617118` | 281 cues<br>`6e25d70372949508d19462bbff44f349d783b2fd237596396cf9e1770f8f810b` | Piecewise step | 833 / 42 / 363 |

### 3.2 OVAs (`OVA01`–`OVA03`)
- **Primary AV Witness**: `OVA\02_media\softsub_mkv\ep01..03.analysis-softsub.mkv` — Matroska, Video `#0:0` `hevc` (Main 10, `yuv420p10le`, `1920x1080`, `24000/1001` fps, `start_time=0.000000s`); Audio `#0:1` `flac` (`jpn`, `48000 Hz`, `2 ch` `stereo`, `start_time=0.000000s`); Subtitle `#0:2` `ass` (`eng`, `title="Ripple"`).
- **Missing Channel — No Verified Japanese Text Layer**: Both `OVA\01_subtitles\` (`ep01..03.ass` and `.analysis.ass`) and the upstream `[Ripple]` BD MKVs contain **0% Japanese characters** (100% English localization/typesetting events). In Phase B, all Japanese dialogue and lyrics must be established strictly via direct native listening to the lossless `FLAC` Japanese audio stream, marking uncertain syllables/words rather than back-translating English subtitles.

| Unit | Softsub MKV Bytes & SHA-256 | Duration (s) | Hardsub MKV SHA-256 | English `analysis.ass` Events & SHA-256 | Upstream Source MKV SHA-256 | Bundle JPEGs / Sheets / Shots |
|---|---|---:|---|---|---|---:|
| `OVA01` (`ep01`) | `150,123,066`<br>`14bcfd93131d1cfeea41b52c3370ca877e48cfbe69e4fae8434f1e7d48d8c6c1` | `419.420` | `cf008e2dc4a5adf3b03bb42dc515dcc53d4f47baa86bb3a4a4a67bdb8bda4878` | 1,229 ASS events (374 dialogue cues, `eng`)<br>`15e3ba989e70e4be9c1a6cb69b636d26007fd251cfc9d4e945a2c1623a88dda6` | `0d5a7dbaf50490ea36f8578ccf51bf91e7638003039dec8baefacdf5bf7f1c8f` | 190 / 10 / 88 |
| `OVA02` (`ep02`) | `191,076,179`<br>`04b35dd4b04f6932eece9d5292d2973612c7157989268ed92feb2162f8c6e1bc` | `428.430` | `ed7550b8cb64838de6b3f2856f74e029f323bdf3866cf556a0d6622569f18c83` | 108 ASS events (106 dialogue cues, `eng`)<br>`606d7d9c4e190d50dbc53191f62c164057ec61cfa722f843f8c45d62bcc5169e` | `e8abacd9a9b3c52d926d6399720895d243c3481089d0383947c23eff06527cfe` | 180 / 9 / 101 |
| `OVA03` (`ep03`) | `237,179,855`<br>`c2152663a82472b0a618c5ca09f7e826b82706d5a07647253c221603ff70a38f` | `433.435` | `8fc015718b9b601a191534f1fa856d47440943a13a4e8a3e33e9cb4f1c3a0ff7` | 469 ASS events (131 dialogue cues, `eng`)<br>`d2b89339ff33c3c0466fe0566455a3f78625647f555ca8835592170a5270022f` | `2ebb6cff5cc44a9ec7ac9c6b219c9330dd160f077c2c826bfb70ab4843ff310b` | 212 / 11 / 113 |

### 3.3 2021 Theatrical Sequel Film (`MOVIE`)
- **Primary AV Witness**: `MOVIE\02_media\softsub_mkv\[Veggie_Sub]_Shoujo☆Kageki_Revue_Starlight_Movie.analysis-softsub.mkv` — `1,479,553,837` bytes, SHA-256 `dd3c3858effe78bfdc4f67b588ec23f274460a33fc3968c8c83a745e71a41099`.
  - Video `#0:0`: `h264` (High, `yuv420p`, `1920x1080`, `24000/1001` fps, `173,160` frames, `start_time=0.021000s`, stream duration `7222.215s`, container duration `7222.235s`).
  - Audio `#0:1`: `aac` (LC, `jpn`, `48000 Hz`, `2 ch` `stereo`, `160 kbps`, `start_time=0.000000s`, `title="Surround 5.1 (2 ch)"`, duration `7222.229s`).
  - Upstream 6-Channel Reference (`[Veggie Sub] Shoujo☆Kageki Revue Starlight Movie.mkv`, `2,053,224,668` bytes, SHA-256 `8674bf5ec2192fe0ff77e7b8d9644231da6e9444964a09cdda17d9182492685a`): Stream `#0:2` `aac` (`jpn`, `48000 Hz`, `6 ch` `5.1`, `635 kbps`, `start_time=0.000000s`).
  - Subtitle `#0:2` (`analysis.ass` byte-identical): `159,207` bytes, SHA-256 `5992b2b769783b558886e024cf119769af7403d668ac85483bb4a2f555341783` (`jpn`, 1,691 dialogue events across 37 character-coded styles; 1,666 lines [98.5%] contain Japanese script).
- **Hardsub Derivative**: `2,378,350,712` bytes, SHA-256 `449667f0445af4182bb46ad2392f40f7f7d1f8135b8b7f0dc32bde1759d5bd2d` (`hevc`, `start_time=0.042000s`).
- **Bundle Navigation Objects**: `3,449` JPEGs, `173` contact sheets, `1,272` detected shot changes, `82` scene-index clusters, complete MP3 (`144,446,467` bytes, SHA-256 `a4d99cd77ae735369a2f0e5a711efcedfe4263a42fbd5197aac58e48bcf2b60c`).

---

## 4. Presentation-Time Clock Specification & Anchor Verification

1. **Canonical Clock Definition**: For every source unit (`TV01`–`TV12`, `OVA01`–`OVA03`, `MOVIE`), the canonical presentation-time clock is the primary Matroska container's zero-based presentation timestamp (`PTS`, `HH:MM:SS.mmm`, `00:00:00.000` origin).
2. **Packet & Derivative Offsets Verified**:
   - **TV (`S01E01`–`S01E12`) & OVA (`ep01`–`ep03`)**: Both video (`v:0`) and primary `FLAC` audio (`a:0`) begin at `first_pts = 0.000000s` (`start`/`mid`/`end` packet anchors verified across `S01E01`, `S01E07`, `S01E12`, `OVA01`–`03`). Complete MP3 derivatives have `+0.023021s` LAME/FFmpeg encoder padding (`23 ms`, sub-frame at `23.976` fps).
   - **Sequel Film (`MOVIE`)**: Primary `softsub_mkv` audio (`a:0`) starts at `0.000000s` and video (`v:0`) starts at `+0.021000s` (`half-frame`), remaining locked across `start` (`0.021s`), `mid` (`3608.835s`), and `end` (`7219.525s` video / `7221.716s` audio). Note `hardsub_mkv` shifts video `start_time` to `+0.042000s` (`1 frame`); using `softsub_mkv` avoids that 1-frame shift.
   - **TV Japanese Subtitle Alignment**: Verified empirically on `TV01` (`00:00:00`–`00:04:05`): spoken onsets, onscreen Japanese typography, and `s01e01.analysis.ass` cue timestamps co-align within `±0.15s`. Episode-by-episode speech-onset checks will still be performed at beginning/middle/end of every unit to guard against residual cue drift.

---

## 5. Empirical Multimodal Inspection Calibration

Two calibration probes were executed via native `read_file` (`video/mp4` multimodal ingestion):
1. **Deterministic Synthetic FPS & A/V Sync Ruler** (`scratch\calib_clips\fps_ruler_10s.mp4`, `10.01s`, `240` frames at `24000/1001` fps, burned frame index + millisecond `PTS`, yellow visual flashes at `2.00–2.25s`, `5.00–5.25s`, `8.00–8.25s`, and stereo sine bursts: `440 Hz` Left at `2.00–2.25s`, `880 Hz` Right at `5.00–5.25s`, `1320 Hz` Center at `8.00–8.25s`).
2. **Clean Native TV01 Segments** (`tv01_calib_45s_clean.mp4` [`00:00:30`–`00:01:15`, un-overlaid] and `tv01_seg01_0000_0245.mp4` [`00:00:00`–`00:04:05`, `245s`, `1280x720` H.264 + `192 kbps` `48 kHz` stereo AAC with burned top-left `EP01 HH:MM:SS.mmm` clock]).

### Measured Capabilities & Operational Protocol
- **Synchronized Audio Perception**: **Confirmed continuous (100% temporal coverage)**. All three `250 ms` tone bursts (`Left-only 440 Hz`, `Right-only 880 Hz`, `Both 1320 Hz`), spoken Japanese syllables, breaths, sound effects, and instrumental underscore were perceived continuously and synchronized to the exact 1-second timestamp bins (`±0.05s` alignment). Both Left and Right channels are audible without channel drop, though stereo panning claims will be corroborated with deterministic L/R RMS measurements from primary `FLAC`/`AAC` streams.
- **Effective Visual Sampling Rate of Native Video `read_file`**: **Exactly `1.000 fps` (`1 frame per container second`, stride = `24` frames at `23.976` fps)**, sampled deterministically at `t = k + 0.46s` (`Frames 11, 35, 59, 83, 107, 131, 155, 179, 203, 227` for `k = 0..9`). Consequently, sub-second visual events (`250 ms` flash boxes between `k+0.00s` and `k+0.25s`, rapid sword exchanges, micro-expressions, and exact cut boundaries between `k+0.46s` samples) are **not** visible in `1 fps` native video pass alone, even though their accompanying audio is heard continuously.
- **Segment Operational Envelope**: `4m 05s` (`245s`, `~23 MB` at `1280x720` CRF 22) ingested cleanly in a single `read_file` call with full synchronized audio and readable top-left millisecond `PTS` overlay (`%{pts\:hms\:OFFSET}`). Full 24-minute TV episodes will therefore be inspected in **6 consecutive, 5-second-overlapping segments** (`~245s` each) for Pass 1 (100% continuous native AV coverage).
- **Mandatory Pass 2 High-Density Visual & Acoustic Protocol**:
  - Whenever cut timing, gesture/choreography trajectory, facial microperformance, onscreen text flash, or music-to-cut synchronization is analytically load-bearing, Pass 2 extracts **high-density `1920x1080` frame sequences / contact sheets (`4–12 fps` or frame-exact `23.976 fps` around edit boundaries)** directly from the unburned primary MKV, alongside lossless `FLAC` acoustic inspection where musical/vocal detail is consequential.
