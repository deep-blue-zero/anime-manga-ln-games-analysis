---
title: "Cosmic Princess Kaguya! — source and evidence inventory"
series: cosmic-princess-kaguya
artifact_id: CPK_SOURCE_INVENTORY
artifact_type: source_inventory
generation: CPK-G1
version: "1.2"
status: canonical
authority_scope: "Verified bibliographic metadata, bound F01 witness CPK-W01-NF-WEBRIP-HEVC, calibrated film clock, complete AM-01..AM-06 measurements, CPK-R1 / CPK-B1-SOL61 / CPK-AVRET-R1 derivative provenance, and post-reconciliation source errata"
source_boundary: "Admitted Japanese feature witness CPK-W01-NF-WEBRIP-HEVC (F01, 02:22:03.207); primary continuous-AV run CPK-R1, independent CPK-B1-SOL61 bundle reading/audit, bounded primary AV return CPK-AVRET-R1 (AV-01..AV-10), and Stage-3 reconciliation completed"
canonical_home: series/cosmic-princess-kaguya/CPK_SOURCE_INVENTORY.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Source and evidence inventory

## 1. Identity and metadata reconnaissance

Checked **2026-11-10 (America/New_York)** at bootstrap and verified against on-film credits during authorized run **CPK-R1** on **2026-11-11**. Public bibliographic metadata remains separated from film evidence; on-film end credits (`02:10:33`–`02:22:03.207`, inspected via `SEG-14`/`SEG-15` and `1920x1080` frames `FRM-22`–`FRM-29`) confirm and refine role subdivisions.

| Field | Verified metadata / on-film credit | Evidence |
|---|---|---|
| Japanese title | 超かぐや姫！ | P01, P03; on-film late title card `02:10:26.360`–`02:10:32.500` |
| Official English title | Cosmic Princess Kaguya! | P02, P04; on-film late title card (`COSMIC PRINCESS KAGUYA!`) |
| Medium/year | Original Japanese animated feature, 2026 | P01–P04; on-film copyright notice `02:20:13` |
| Director / storyboard | 山下清悟 / Shingo Yamashita (監督・絵コンテ; 絵コンテ協力: 石田祐康, 刈谷仁美, 永江彰浩) | P01/P03/P04; `FRM-27`, `FRM-29` |
| Screenplay / concept cooperation | 夏生さえり, 山下清悟 (原案協力: フジヤマルリ) | P01 STAFF; `FRM-27` |
| Live sequence directors | ヤチヨライブ＆デュエットライブ 絵コンテ・演出: 中山直哉; 卒業ライブ 絵コンテ・演出: 岩澤亨 | `FRM-28` |
| Animation studios | スタジオコロリド / スタジオクロマト (Studio Colorido / Studio Chromato; アニメーションプロデューサー: 桃原一真) | P01/P03/P05; `FRM-29`, studio bumpers `02:20:15`–`02:20:37` |
| Production | コロリド・ツインエンジンパートナーズ | P01/P03 |
| Character design | ツクヨミキャラクターデザイン: へちま; 現実キャラクターデザイン: 永江彰浩 | P01/P03; `FRM-27`, `FRM-28` |
| Score / sound direction | 音楽・指揮・編曲・オーケストレーション: コーニッシュ (Conisch) / 音響監督: 三好慶一郎 | P01 STAFF; `FRM-26` |
| Song contributors | ryo (supercell), yuigot, Aqu3ra, HoneyWorks (shito, Gom, 中西), EasyPop, 40mP, kz (livetune), 真崎エリカ, 藤原基央, TAKU INOUE, コーニッシュ | P01/P03; `FRM-24`–`FRM-26` |
| Initial streaming release | Netflix worldwide, 2026-01-22 | P01/P03/P05 |
| Published streaming runtime | BBFC 2D VOD record: **142m 3s**, NETFLIX, INC; classified 2026-01-21 | P04 |
| Admitted witness runtime | **8523.207 s (`02:22:03.207` / 142m 03.207s)**, `204,352` video frames at `24000/1001` fps | Bound witness `CPK-W01-NF-WEBRIP-HEVC` |

### Public references and admitted use

| ID | Public route | Admitted use |
|---|---|---|
| P01 | [Official film site — title, release, STAFF](https://www.cho-kaguyahime.com/) | Metadata/credits cross-check only; promotional STORY/CHARACTER text quarantined |
| P02 | [Netflix catalog, title 81756595](https://www.netflix.com/title/81756595) | Catalog title ID, release year, and listed track availability |
| P03 | [Studio Colorido release notice, 2025-11-05](https://colorido.co.jp/press/3122/) | Title, director, production/animation and streaming release |
| P04 | [BBFC film/version record](https://www.bbfc.co.uk/release/cosmic-princess-kaguya-q29sbgvjdglvbjpwwc0xmta5njkw) | Classified streaming version and published runtime cross-check |
| P05 | [Netflix Tudum release/production report](https://www.netflix.com/tudum/articles/cosmic-princess-kaguya-release-date-news) | Official English/studio nomenclature |
| P06 | [Official movie announcements](https://www.news.cho-kaguyahime.com/movie/) | Edition-existence notice for later theatrical screenings (`2026-09-18`); not admitted and no cut-equivalence claimed |

## 2. Admitted source classes and post-CPK-R1 status

| Role | Evidentiary/admission boundary | Access in CPK-R1 | Inspection status / consequence |
|---|---|---|---|
| `F01` finished film (`CPK-W01-NF-WEBRIP-HEVC`) | Admitted primary narrative witness for single feature `F01` | Local private Matroska witness inspected via verified synchronized derivatives | REQUIRED / `COMPLETE_FOR_DECLARED_SCOPE` (`00:00:00.000`–`02:22:03.207`) |
| Original Japanese audio (`CPK-W01-AUD-JA-T1`) | Root narrative authority for spoken wording, vocal performance, register, SFX, and music (`0:a:0`, Audio Track 1) | Synchronized AAC 48 kHz stereo transcode across all 15 Pass-1 segments and 6 Pass-2 clips | REQUIRED / `COMPLETE_FOR_DECLARED_SCOPE` |
| Japanese dialogue/onscreen text (`CPK-W01-SUB-JA-T4` + `FRM`) | Supporting Japanese `[SDH]` text witness (`0:s:3`, Subtitle Track 4, `2,716` cues) plus lossless `1920x1080` PNG inspection (`FRM-01`–`FRM-29`) | Full SRT extracted and aligned; spoken-audio vs SDH divergences audited | REQUIRED / `COMPLETE_FOR_DECLARED_SCOPE` |
| Japanese song lyrics | Subtitle Track 4 (`0:s:3`) carries timed `♪` lyric cues for diegetic/insert songs (`Remember`, `星降る海`, `私は、わたしの事が好き。`, `OnyXXX`, `ハッピーシンセサイザ`, `ワールドイズマイン`, `Ex-Otogibanashi`, `瞬間、シンフォニー。`, `Reply`); end-credit songs (`ray`, `メルト`) have credit cards (`FRM-24`) without SDH lyric lines | Verified for subtitled in-film songs; end-credit song lyrics treated as unverified auditory-only (`AO`) | REQUIRED where lyric wording is claimed / `PARTIAL` (end-credit lyrics uncited as exact `TXT`) |
| Official English subtitles (`CPK-W01-SUB-EN-T3`) | Secondary localization witness (`0:s:2`, Subtitle Track 3, `2,079` cues); never overrides Japanese | Extracted locally for secondary translation comparison only | OPTIONAL / `COMPLETE_FOR_DECLARED_SCOPE` |
| Synchronized AV derivatives (`SEG-01`–`SEG-15`, `P2-CLIP-01`–`P2-CLIP-06`, `FRM-01`–`FRM-29`) | Technical analysis derivatives bound to `CPK-W01-NF-WEBRIP-HEVC`; kept strictly outside Git | Generated, SHA-256 hashed, PSNR-calibrated, and inspected in `CPK-R1` | REQUIRED / `COMPLETE_FOR_DECLARED_SCOPE` for `CPK-R1`; auditor bundle handoff prepared |
| Single-film verifier bundle | Restricted blind input set + synchronized derivatives for separate OpenAI `BUNDLE_MEDIATED` audit | Blind packet authored (`audits/CPK_F01_BLIND_INPUT_PACKET.md`); verifier session not yet invoked | REQUIRED for next stage / `PENDING` (separate OpenAI verifier owner) |
| Interviews, soundtrack albums, external commentary | Non-admitted paratext / external commentary; excluded from narrative findings | Quarantined | `OUT_OF_SCOPE` |

## 3. Bound primary witness and stream mapping (`CPK-W01-NF-WEBRIP-HEVC`)

### 3.1 Witness identity record

| Field | Bound value |
|---|---|
| Public-safe witness ID | `CPK-W01-NF-WEBRIP-HEVC` |
| Work / unit ID | `超かぐや姫！` (*Cosmic Princess Kaguya!*) — single feature film `F01` |
| Container format | Matroska (`.mkv`, EBML v1 / Matroska v4, `46` total tracks: `1` video, `12` audio, `33` subtitle) |
| Distribution lineage | Netflix worldwide streaming edition (`2026-01-22` release lineage; closing Netflix dubbing credits `02:20:38`–`02:22:03.207`) |
| Exact file size | `4,916,885,885` bytes (`4.579 GiB`) |
| Exact SHA-256 | `b940eede5e3ce2e83e507a33e6523516c21e770dbccd8cc9e4461af77b23a42a` |
| Measured container duration | `8523.207000` s (`02:22:03.207`) |
| Video stream (`0:v:0`) | FFmpeg index `0`, MKV Track `1` (`UID 16410760573708363331`), `HEVC` (`Main 10`, `yuv420p10le`, `bt709`), `1920x1080` (`16:9`), `24000/1001` fps (`23.976024` fps), time base `1/1000`, `start_time = 0.000000` s, `204,352` frames (`8523.198` s picture stream) |
| Program-start definition | `t_F01 = 00:00:00.000` equals `PTS = 0.000` of video stream `0:v:0`. Zero pre-roll or studio bumper precedes the narrative: frame 0 opens directly on the cosmic Tsukuyomi panorama |
| Storage & rights hygiene | Raw `.mkv`, extracted `.srt`, `.mp4` segments/clips, and `.png` frames reside exclusively in local private storage outside the Git repository |

### 3.2 Explicit stream and language track mapping

Container EBML metadata leaves Track 14 (`0:s:0`, `Chinese (Simplified)`) as the default subtitle stream while marking Track 17 (`0:s:3`, `Japanese [SDH]`) with `flag_default = 0, flag_sdh = 1`. Per owner instruction and project policy, container default flags were ignored in favor of explicit stream binding verified by `ffprobe`, EBML header parsing, and sample inspection:

| Owner / role designation | Type-specific ordinal | FFmpeg stream specifier / index | MKV `TrackNumber` / `TrackUID` | Codec & parameters | Language / title metadata | Extracted text derivative (outside Git) |
|---|---|---|---|---|---|---|
| **Primary audio: Japanese — audio track 1** (`CPK-W01-AUD-JA-T1`) | Audio Track 1 (1st audio stream) | `0:a:0` (`ff_idx = 1`) | `2` / `2220009072891289259` | `opus`, `48000` Hz, `5.1(side)` (`6` ch), `start_time = 0.138000` s | `jpn` (`ja`), title `Japanese` (`flag_default = 1`) | N/A (transcoded synchronously into `SEG-01`–`SEG-15` & `P2-CLIP-01`–`P2-CLIP-06`) |
| Secondary audio (unselected): English..Thai | Audio Tracks 2–12 | `0:a:1`–`0:a:11` (`ff_idx = 2`–`12`) | `3`–`13` | `opus`, `48000` Hz, `5.1` | `en`, `de`, `es-419`, `es`, `fil`, `fr`, `hu`, `it`, `pl`, `pt-BR`, `th` | Not extracted; excluded from analysis |
| Unselected subtitles 1–2 | Subtitle Tracks 1–2 | `0:s:0`–`0:s:1` (`ff_idx = 13`–`14`) | `14`–`15` | `ass` (`S_TEXT/ASS`) | `zh-Hans`, `zh-Hant` | Not extracted; container default overridden |
| **Optional secondary check: English — subtitle track 3** (`CPK-W01-SUB-EN-T3`) | Subtitle Track 3 (3rd subtitle stream) | `0:s:2` (`ff_idx = 15`) | `16` / `8102331218380612976` | `subrip` (`S_TEXT/UTF8`) | `eng` (`en`), title `English` (`flag_default = 0`) | `150,481` bytes, SHA-256 `811cb0369a10375b40041e8de8ed3f0e5dd4bc1fcc263b7bf0254f306bffdc6a`, `2,079` cues (`[EN#0001]`–`[EN#2079]`) |
| **Supporting Japanese text: Japanese — subtitle track 4** (`CPK-W01-SUB-JA-T4`) | Subtitle Track 4 (4th subtitle stream) | `0:s:3` (`ff_idx = 16`) | `17` / `5003112197002342989` | `subrip` (`S_TEXT/UTF8`) | `jpn` (`ja`), title `Japanese [SDH]` (`flag_default = 0`, `flag_sdh = 1`) | `214,854` bytes, SHA-256 `15ea610f9a63347d66e39770f9c03f78d2e23ec95aaa2c03462747ecc53c89a4`, `2,716` cues (`[JA#0001]`–`[JA#2716]`) |
| Unselected subtitles 5–33 | Subtitle Tracks 5–33 | `0:s:4`–`0:s:32` (`ff_idx = 17`–`45`) | `18`–`46` | `subrip` (`S_TEXT/UTF8`) | `ar`, `cs`, `da`, `de`, `el`, `es-419`, `es`, `fi`, `fil`, `fr`, `he`, `hr`, `hu`, `id`, `it`, `ko`, `ms`, `nb`, `nl`, `pl`, `pt-BR`, `pt`, `ro`, `ru`, `sv`, `th`, `tr`, `uk`, `vi` | Not extracted |

**Audio start-offset handling:** Raw container stream `0:a:0` carries `start_time = 0.138000` s (`138` ms) over complete opening silence before Yachiyo's narration enters at `00:00:15.390` (`[JA#0001]`). Every derivative transcode applied `-af aresample=async=1:first_pts=0`, normalizing audio `start_time = 0.000000` s in lockstep with video `PTS = 0.000` without stretching or shifting spoken syllables relative to the source timeline.

## 4. Calibrated F01 clock and derivative provenance

### 4.1 Pass-1 contiguous synchronized AV segments (`CPK-MAP-P1-SEGMENTS`)

Because the `4.58 GiB` HEVC/Opus Matroska container exceeds direct single-call multimodal ingestion limits (`100 MiB` hard ceiling per `read_file` media call), `CPK-W01-NF-WEBRIP-HEVC` was transcoded via `ffmpeg` (`n8.0` / `h264_nvenc`, `1280x720` Lanczos `yuv420p`, `AAC` stereo `48 kHz` `128 kbps` mapped strictly from `0:v:0` and `0:a:0`) into **15 contiguous MP4 segments (`SEG-01`–`SEG-15`)** with **20.000-second boundary overlaps** across every interior seam (`10` segments at standard `cq=28 / maxrate=1800k`; `5` high-motion concert segments `SEG-03`, `SEG-06`, `SEG-07`, `SEG-09`, `SEG-11` re-encoded at `cq=30 / maxrate=1100k` to remain strictly below `100 MiB`).

| Derivative ID | Parent F01 interval (`[start, end]`) | Clock formula (`t_F01`) | Measured duration (s) | Video `start_time` (s) | Bytes | SHA-256 | Overlap check |
|---|---|---|---|---|---|---|---|
| `SEG-01` | `00:00:00.000` – `00:10:20.000` (`0`–`620` s) | `0.000 + t_local` | `620.036` | `0.000` | `90,300,615` | `9e9e334c71ed7ba0297fff2b56a9c6cbc7d6cde54069c48b7a949eaea77f9f92` | `[00:10:00, 00:10:20]` w/ `SEG-02` |
| `SEG-02` | `00:10:00.000` – `00:20:20.000` (`600`–`1220` s) | `600.000 + t_local` | `620.036` | `0.000` | `74,262,479` | `4a2615268f7dc5386bcaaef6c6cabe54e188eca2bda296ceae4edbc93f888df6` | `[00:20:00, 00:20:20]` w/ `SEG-03` |
| `SEG-03` | `00:20:00.000` – `00:30:20.000` (`1200`–`1820` s) | `1200.000 + t_local` | `620.077` | `0.041` | `80,806,094` | `22ebfab7cbd216d630fbac1ef911ef4bfe9864fd328d33ace6af201d37275bda` | `[00:30:00, 00:30:20]` w/ `SEG-04` |
| `SEG-04` | `00:30:00.000` – `00:40:20.000` (`1800`–`2420` s) | `1800.000 + t_local` | `620.036` | `0.000` | `100,271,646` | `dad8c97962439c119dc414572776620ddb4441c61c365b95dcb3a52eaf0362fa` | `[00:40:00, 00:40:20]` w/ `SEG-05` |
| `SEG-05` | `00:40:00.000` – `00:50:20.000` (`2400`–`3020` s) | `2400.000 + t_local` | `620.077` | `0.041` | `99,802,856` | `bdc8f8e209cc1377326ced3f34cc635f4755de2ad006908b71017e0c8e5bcbf0` | `[00:50:00, 00:50:20]` w/ `SEG-06` |
| `SEG-06` | `00:50:00.000` – `01:00:20.000` (`3000`–`3620` s) | `3000.000 + t_local` | `620.077` | `0.041` | `76,178,815` | `68ef467294ce77954e0606a84d976f704563f008fef52e7268909229ba012a8c` | `[01:00:00, 01:00:20]` w/ `SEG-07` |
| `SEG-07` | `01:00:00.000` – `01:10:20.000` (`3600`–`4220` s) | `3600.000 + t_local` | `620.036` | `0.000` | `84,204,823` | `39c9f744e97191ef19cb947de962db93b16bfe237b17fea81ee22539d4bfb8c3` | `[01:10:00, 01:10:20]` w/ `SEG-08` |
| `SEG-08` | `01:10:00.000` – `01:20:20.000` (`4200`–`4820` s) | `4200.000 + t_local` | `620.077` | `0.041` | `103,678,577` | `fdd0bb0f4d1c2080dac59767beea237f67a062da8ab60da7f357ad8a181a80d1` | `[01:20:00, 01:20:20]` w/ `SEG-09` |
| `SEG-09` | `01:20:00.000` – `01:30:20.000` (`4800`–`5420` s) | `4800.000 + t_local` | `620.036` | `0.000` | `79,455,830` | `873f7f894ed3528383b7df38def1173ba63ea843f451b4e704eeeab28d23ea3f` | `[01:30:00, 01:30:20]` w/ `SEG-10` |
| `SEG-10` | `01:30:00.000` – `01:40:20.000` (`5400`–`6020` s) | `5400.000 + t_local` | `620.036` | `0.000` | `72,998,054` | `52eb221b139dd9768226550280a800770b5e7de762359fc78e0ba425075fbb0a` | `[01:40:00, 01:40:20]` w/ `SEG-11` |
| `SEG-11` | `01:40:00.000` – `01:50:20.000` (`6000`–`6620` s) | `6000.000 + t_local` | `620.077` | `0.041` | `76,321,367` | `3f9ce382df3eb984adb2f5344c967016309d5e92c7d23d3ebe3e2b8c049e6fe6` | `[01:50:00, 01:50:20]` w/ `SEG-12` |
| `SEG-12` | `01:50:00.000` – `02:00:20.000` (`6600`–`7220` s) | `6600.000 + t_local` | `620.036` | `0.000` | `85,342,391` | `742ce576c22c229059bbde7cd05e3c0ee32c0de7cac17448ef44873c6876887c` | `[02:00:00, 02:00:20]` w/ `SEG-13` |
| `SEG-13` | `02:00:00.000` – `02:10:20.000` (`7200`–`7820` s) | `7200.000 + t_local` | `620.077` | `0.041` | `85,174,710` | `79295c0d969943575e44018b840abf277dc5a83a706e6b9f2f08cda2300b44be` | `[02:10:00, 02:10:20]` w/ `SEG-14` |
| `SEG-14` | `02:10:00.000` – `02:17:20.000` (`7800`–`8240` s) | `7800.000 + t_local` | `440.023` | `0.000` | `77,452,029` | `efe5d2d2da1b3a4737207183e3d10e96c7c49f4ceabcd136104fd7f4cd56e137` | `[02:17:00, 02:17:20]` w/ `SEG-15` |
| `SEG-15` | `02:17:00.000` – `02:22:03.207` (`8220`–`8523.207` s) | `8220.000 + t_local` | `303.200` | `0.000` | `31,352,654` | `d4e5bb67f50122d468e4092b7e29afe7d4b82062a00cb1e5f7612d331289fd81` | Exact EOF `8523.207` s |

### 4.2 Clock calibration table (`CPK-CLK-F01-GLOBAL`)

Seven distributed calibration anchors across beginning, first quartile, midpoint, third quartile, climax, and end credits were verified directly between `CPK-W01-NF-WEBRIP-HEVC` (scaled to `1280x720` for comparison) and the corresponding `SEG-*` derivative using `ffmpeg` `psnr` plus subtitle/audio alignment:

| Mapping / Anchor ID | Parent & derivative hashes (prefix) | Clock definition | Anchor event / cue | Source `t_F01` | Derivative `t_local` | Offset / piecewise formula | Drift / residual | Achieved precision | Verifier |
|---|---|---|---|---|---|---|---|---|---|
| `CAL-01-BEGIN` | `b940eede` → `SEG-01` (`9e9e334c`) | `PTS=0` program start | Cosmic Tsukuyomi train over pancake-island (`[JA#0003]` vicinity) | `00:00:30.000` (`30.0` s) | `SEG-01` `+00:30.000` | `t_F01 = 0.000 + t_local` | `0.000` s (`PSNR avg 49.35 dB`) | `±0.042` s (`1` frame); `±0.5` s citation | `CPK-R1` (`ffmpeg psnr` + AV) |
| `CAL-02-EARLY` | `b940eede` → `SEG-02` (`4a261526`) | `SEG-02` +600s | Iroha researching Tsukuyomi (`[JA#0185]` vicinity) | `00:10:50.000` (`650.0` s) | `SEG-02` `+00:50.000` | `t_F01 = 600.000 + t_local` | `0.000` s (`PSNR avg 46.94 dB`) | `±0.042` s (`1` frame) | `CPK-R1` (`ffmpeg psnr` + AV) |
| `CAL-03-Q1` | `b940eede` → `SEG-04` (`dad8c979`) | `SEG-04` +1800s | `いろP` logging out from Yachiyo bridge (`[JA#0737]`, `P2-CLIP-02`) | `00:35:00.000` (`2100.0` s) | `SEG-04` `+05:00.000` | `t_F01 = 1800.000 + t_local` | `0.000` s (`PSNR avg 47.16 dB`) | `±0.042` s (`1` frame) | `CPK-R1` (`ffmpeg psnr` + AV) |
| `CAL-04-MID` | `b940eede` → `SEG-08` (`fdd0bb0f`) | `SEG-08` +4200s | Loft apartment horror-film night (`SEG-08` midpoint) | `01:15:00.000` (`4500.0` s) | `SEG-08` `+05:00.000` | `t_F01 = 4200.000 + t_local` | `≤0.041` s (`PSNR max 46.05 dB`) | `±0.042` s (`1` frame) | `CPK-R1` (`ffmpeg psnr` + AV) |
| `CAL-05-Q3` | `b940eede` → `SEG-11` (`3f9ce382`) | `SEG-11` +6000s | High-motion Graduation Live *Raigō* battle (`SEG-11` `1100k` tier) | `01:44:55.000` (`6295.0` s) | `SEG-11` `+04:55.000` | `t_F01 = 6000.000 + t_local` | `≤0.041` s (`PSNR max 31.32 dB`, 1-frame seek offset on rapid particle flash) | `±0.042` s (`1` frame) | `CPK-R1` (`ffmpeg psnr` + AV) |
| `CAL-06-CLIMAX` | `b940eede` → `SEG-13` (`79295c0d`) | `SEG-13` +7200s | Mirror-sea confrontation opening (`SEG-13`) | `02:05:00.000` (`7500.0` s) | `SEG-13` `+05:00.000` | `t_F01 = 7200.000 + t_local` | `≤0.041` s (`PSNR max 43.70 dB`) | `±0.042` s (`1` frame) | `CPK-R1` (`ffmpeg psnr` + AV) |
| `CAL-07-END` | `b940eede` → `SEG-15` (`d4e5bb67`) | `SEG-15` +8220s | Post-credits pancake-island stinger (`[JA#2712]` vicinity) | `02:20:00.000` (`8400.0` s) | `SEG-15` `+03:00.000` | `t_F01 = 8220.000 + t_local` | `0.000` s (`PSNR avg 37.33 dB`) | `±0.042` s (`1` frame) | `CPK-R1` (`ffmpeg psnr` + AV) |

### 4.3 Pass-2 targeted high-bitrate AV clips (`CPK-MAP-P2-CLIPS`) and `1920x1080` PNG frames (`CPK-MAP-P2-FRAMES`)

For focused Pass-2 reinspection of load-bearing scenes and micro-typography, **6 high-bitrate `1280x720` H.264/AAC `192 kbps` clips (`P2-CLIP-01`–`P2-CLIP-06`)** and **29 lossless `1920x1080` PNG frames (`FRM-01`–`FRM-29`)** were extracted directly from `CPK-W01-NF-WEBRIP-HEVC`, alongside **6 deterministic `ffmpeg` `scdet` (`threshold=12`) + `ebur128` measurement windows (`AM-01-OPENING`–`AM-06-COMEBACK-TITLE`)**:

| Clip ID | Parent F01 interval | Duration (s) | Bytes | SHA-256 | Target verification scope |
|---|---|---|---|---|---|
| `P2-CLIP-01` | `00:07:28.000` – `00:07:58.000` | `30.0` | `8,354,183` | `05aabccb13b32e78c0937fcc8a522b42eb606fe0271494fda93d42b960afe0c2` | Iroha *a cappella* `Remember` calming baby Kaguya; `神棚` Yachiyo standee cutaways |
| `P2-CLIP-02` | `00:34:45.000` – `00:35:15.000` | `30.0` | `5,529,132` | `9726d958bbcd69937924c00fd60d5be905805451b6935e792a86d8cedcc4bbc7` | Yachiyo charm handoff, solo piano `Remember`, unheard real-name `彩葉` whisper |
| `P2-CLIP-03` | `01:24:02.000` – `01:25:10.000` | `68.0` | `24,559,266` | `eaf54854d58ce75995db021d176c1c383c18710405f12f8929292691f5aeea9f` | Marriage proposal, expense-split acceptance, wrist bangle glint, `2030/09/12` `月人` intrusion |
| `P2-CLIP-04` | `01:47:34.000` – `01:48:18.000` | `44.0` | `12,014,721` | `6a74497f24a2f5e395cb9b4188cb27198376687b7af81b6aeef192b53db265cd` | Dead-silent real-room `彩葉… 大好き`, `天の羽衣` iris/expression blanking, `犬DOGE` stowaway leap |
| `P2-CLIP-05` | `01:51:20.000` – `01:51:58.000` | `38.0` | `6,097,674` | `29691138c4e0c25106882524f1a69a93a6b9fe3d38291fbf6f0dfd9daef04536` | `めでたし めでたし` fake-out, parody streaming post-play UI shatter, reclaiming `進路希望調査票` |
| `P2-CLIP-06` | `02:05:10.000` – `02:07:14.000` | `124.0` | `18,672,639` | `fdda79b490841456edec7ff3b530ed46dec51386e566519e1172bc65bc6fc476` | 12s silent breakdown, `かぐやと、いたい`, unison `Remember`/`Reply` refrain, interlaced hands, 10-year vow |

| Frame ID | Exact `t_F01` | Bytes | SHA-256 | Verified static `1920x1080` target |
|---|---|---|---|---|
| `FRM-01` | `00:01:23.500` | `6,794,342` | `5622938dcaabe7f0b0deab4d8186e19a0231198177cd680d26cace0de847ee12` | Bookshelf `神棚` housing Yachiyo standee above entrance-exam prep books |
| `FRM-02` | `00:01:34.000` | `7,531,692` | `557709288ad13705178bcac4bfe2680f5e46a30c08a8e7fa13a53209ad9ac55f` | Vertical Kansai-ben calligraphy framing young Iroha & Momiji parting |
| `FRM-03` | `00:09:09.500` | `6,305,438` | `9fce97cb798c65742f70ee7a7a23fe81a4170e7a1fe65896679fc04140e7af1a` | `ふじゅペイ` screen (`23,532円` = `20,532円` + `3,000 pt`) over baby goods basket |
| `FRM-04` | `00:10:10.000` | `4,497,214` | `9c6a1526eb61ac448d21f62b32bbd9d0275467fd559c05f5bec3721755a476ee` | `TukuyomiTube` (`tukuyomitube.com`) `【PR動画】` (`410万回視聴`) |
| `FRM-05` | `00:35:59.000` | `7,239,189` | `7f0d7f86acebf24608849fbb8a03748ff2b7d7805e9a6da6bb78344ed3358484` | Handwritten wall summer chart (`バイト` + `東大文一` Common Test subject load) |
| `FRM-06` | `00:41:40.000` | `4,667,048` | `217151928cf86f8522c1651c8398d5e1fa3fe26310999e244e4fb42ade0e119d` | Waterproof-pouch phone playing `私は、わたしの事が好き。` above `竹取オーバーナイトセンセーション` & `メルト` |
| `FRM-07` | `01:17:23.000` | `2,118,410` | `c57cb8d51b28cbf21106e3ee8d8b4c63295e7aabf7e07548bd9e3b31d34247cb` | `music > tomohisa > タイトル未定 ( 彩葉と共作 ).wav` (`01:45`, `2020/01`) |
| `FRM-08` | `01:24:52.000` | `7,928,295` | `7c8bca03e924db45284f6c1b3cdf9c76e2426901a56073bd04cae37fe19a47fa` | Four lantern-headed `月人` on subway escalator beside unseeing commuter & `SMART SIGHT` ad |
| `FRM-09` | `01:45:56.500` | `7,919,239` | `29e30ade0bf1c23c232e1c6e876a1423329f3cb52677613f657fb45078bdec51` | `SYS_CMND//WARNING` `⚠ CHEAT DETECTION / 不正行為を検出` on Mikado Akira |
| `FRM-10` | `01:49:10.000` | `4,774,123` | `a821788810f5f3d0526e7be5127b219b74e023ded19815497ef2d7698aa3caea` | Fridge notes: `めんつゆ / マヨケチャップ / しおこしょう きんし！！` + `しあわせパンケーキのつくりかた！` |
| `FRM-11` | `01:49:32.000` | `5,355,085` | `1189c0ac5a7cf7fd708c1b4b536f53af38f7fd17180823733047c1cd1dc01157` | `かぐや さんから受け取り` `使っちゃった分、かえす！ ご迷惑かけました！` (`2030年9月12日 22:49`) |
| `FRM-12` | `01:50:22.500` | `3,010,070` | `28a38d0e551029cb4de4179685883281b6154f544acae1f9fdb4f7711380283f` | `進路希望調査票` (`2年3組12番 酒寄彩葉`, 1st: `東京大学 文科一類`, 2nd: `一橋 法 法律`, goal `法科大学院（弁護士）`) |
| `FRM-13` | `01:51:36.000` | `2,462,279` | `959d2c1010d821da685eee24648f77fa192b19f85efdaf3089483f016105bb24` | Parody streaming post-play UI (`SPECIAL BLACK ONYX 3rd LIVE`, `予告編まで9秒`, shrunk `超かぐや姫！` credits) |
| `FRM-14` | `01:56:36.500` | `7,065,761` | `a6dd55e70e517c54f881cd568c2176e8237743f72a55eb747ccb10d1659d90b6` | Boarded-window apartment server tank holding wired ancient bamboo-shoot lunar core (`筍`) |
| `FRM-15` | `01:58:59.000` | `8,681,208` | `c156cbc9d8e884e53384c74923b5d984b1a4895e439ba5534bef2182bf052b84` | Mid-1990s expanding internet node network visualization |
| `FRM-16` | `01:59:01.000` | `11,562,308` | `0d07ad73c4e778acadb30e0e0f3ff69e9e1259806966f56431bf18fffc01996e` | `☽ヤチヨ☾のお部屋` (`2003年10月10日`), sea-bunny art, `★月に帰りたくなるときもあるよ同盟` badge |
| `FRM-17` | `01:59:04.000` | `5,432,116` | `6e008975381cc41a4d6c51330214ebc88c2874fd071ae2b1d80e2fc2a727665f` | `2005/07/28(木) 03:40` BBS post `8 名前：yachi8000◆oCrOwWQM5w` on pre-Yayoi vs Heian food |
| `FRM-18` | `02:07:22.500` | `6,331,361` | `f1d2a2c94f86f9110fb20f5a366c0bd3effaf3b82802136098a87821bbb1c1aa` | Guidance room whiteboard `卒業後の計画` pitched to Momiji and homeroom teacher |
| `FRM-19` | `02:08:48.000` | `7,237,116` | `15c9c8bd0d32d6ca495594a97790ae09610baa6468ed89647bcf1e0a551b8ad5` | 2040 lab monitor `Study of real...` / `tactile sensati...` (`触覚の伝達構造`) & Yachiyo tablet |
| `FRM-20` | `02:09:48.000` | `6,747,900` | `b2300038fd7ca719c9cb8527fc2f036227a10c0530bc4f9aa55adc3abb472b7d` | Backstage lift: weight-bearing shadowed Kaguya & Iroha beside floating self-luminous Yachiyo |
| `FRM-21` | `02:10:13.000` | `8,148,784` | `c9e736f142e910a2a0b90590da8a516df7ac09858c5a5581e1b8a2ecf52f43b1` | Six framed 2040 dining-table photos (`祝★復活ライブ！`, stage selfie, Tsukuyomi cast group shot) |
| `FRM-22` | `02:10:45.000` | `191,424` | `ce19e66a16c00d2726166f1a50b3f67c0dc2c4b7fc856dfb6127e02e50679f43` | End credits Cast 1 (`かぐや` 夏吉ゆうこ, `酒寄彩葉` 永瀬アンナ, `月見ヤチヨ` 早見沙織, `帝アキラ／酒寄朝日` 入野自由, `駒沢雷` 内田雄馬, `駒沢乃依` 松岡禎丞) |
| `FRM-23` | `02:10:56.000` | `271,596` | `26dfc841e1a40270c3ab1bf0f25192e968d456fe434aabc7906888e9eb581c7c` | End credits Cast 2 (`諌山真実` 小原好美, `FUSHI` 釘宮理恵, `乙事照琴` 花江夏樹, `忠犬オタ公` ファイルーズあい, `酒寄紅葉` 坂本真綾, `酒寄朝久` 鈴村健一, `担任の先生` 小林親弘, `音楽の先生` 宮沢きよこ, `犬DOGE` 庄司更紗) |
| `FRM-24` | `02:15:28.000` | `1,233,619` | `ff833f6421bb23ae2bb33c3214eddb54be186caed664af344257a168f90fd6b7` | End credits Ending Theme (`ray 超かぐや姫！Version`) & Special Track (`メルト CPK! Remix`) |
| `FRM-25` | `02:15:39.000` | `1,536,351` | `9c35d98b69669a9b4d83870c93590b36797afc6dd59cde547cc030b7afa846df` | End credits Insert Songs 1 (`Remember`, `星降る海`, `私は、わたしの事が好き。`, `ワールドイズマイン CPK! Remix`, `ハッピーシンセサイザ (COVER)`, `瞬間、シンフォニー。`) |
| `FRM-26` | `02:15:51.000` | `1,237,197` | `dc5c8a8ac61e748a0fa38e66fcccb937e77e4dbe617f5386418a7eb0f8f28dd3` | End credits Insert Songs 2 (`OnyXXX`) & Score (`コーニッシュ`) |
| `FRM-27` | `02:18:05.000` | `1,279,619` | `e1dcc577ebccc86b52e72a70f9c13ead112fc1adba2f7e4317b3228ff53c045a` | End credits Screenplay (`夏生さえり`, `山下清悟`), Concept (`フジヤマルリ`), Storyboard (`山下清悟` et al.) |
| `FRM-28` | `02:18:16.000` | `1,592,232` | `08819704289968668fdc393305da693de600319945d8f6f3f7575a54109516ed` | End credits Reality Character Design (`永江彰浩`) & Live Directors (`中山直哉`, `岩澤亨`) |
| `FRM-29` | `02:19:48.000` | `1,422,525` | `841c6f84353be3a7f94f5c206abf16213d3f9d932f32803ad5f0ae5693ae99d7` | End credits Animation Producer (`桃原一真`) & Director (`山下清悟`) |


### 4.4 Deterministic scene-cut (`scdet`) and loudness (`ebur128`) windows (`AM-01`–`AM-06`, complete `v1.2` table)

> **Post-audit `v1.2` completeness repair:** `CPK_SOURCE_INVENTORY.md` `v1.1` stated in §4.3 that six `AM` windows (`AM-01`–`AM-06`) were measured during `CPK-R1`, while individual `AM-02` and `AM-03` rows were absent from the six delivered `v1.1` homes (verified in [PUBLICATION_REVIEW_RECEIPT.json](audits/CPK-B1-SOL61/PUBLICATION_REVIEW_RECEIPT.json)). All six windows below were verified deterministically with `ffmpeg n8.0` (`scdet=threshold=12` + `ebur128=peak=true`) on the synchronized `CPK-W01-NF-WEBRIP-HEVC` segment derivatives under `CPK-CLK-F01-GLOBAL`:

| Window ID | Derivative source | `F01` interval (`CPK-CLK-F01-GLOBAL`) | Duration (s) | `scdet` cuts (`>= 12.0`) | Peak `scdet` score & timestamp (`t_F01`) | Integrated loudness `I` (`LUFS`) | Loudness range `LRA` (`LU`) | True peak `TP` (`dBFS`) | Structural verification scope |
|---|---|---|---|---|---|---|---|---|---|
| `AM-01-OPENING` | `SEG-01` (`0.0`–`82.0` s) | `00:00:00.000` – `00:01:22.000` | `82.0` | `35` | `78.214` at `00:00:06.006` (`NETFLIX PRESENTS` wallpaper entry; cosmic-to-apartment room transition cut at `00:01:20.956`) | `-20.5` | `12.1` | `-0.4` | Netflix ident (`00:01`–`00:11`), cosmic Tsukuyomi prologue (`[JA#0001]` at `00:00:26.026`), and hard cut into Iroha's Tokyo room |
| `AM-02-KASSEN-CLIMAX` | `SEG-07` (`0.0`–`135.0` s) | `01:00:00.000` – `01:02:15.000` | `135.0` | `79` | `42.596` at `01:00:16.975` | `-19.0` | `8.9` | `-2.5` | High-density `KASSEN` `3対3` arena combat window immediately following Asahi's `00:58:53` sibling recognition (`[JA#1294]`) |
| `AM-03-MOON-HIJACK` | `SEG-09` (`240.0`–`310.0` s) | `01:24:00.000` – `01:25:10.000` | `70.0` | `22` | `38.047` at `01:24:30.145` | `-21.2` | `12.1` | `-5.2` | Loft marriage/expense exchange (`[JA#1850–1857]`), `01:24:16.250` bracelet close-up, and `2030/09/12` `月人` screen/AR intrusion |
| `AM-04-POSTPLAY-SHATTER` | `SEG-12` (`80.0`–`118.0` s) | `01:51:20.000` – `01:51:58.000` | `38.0` | `16` | `42.126` at `01:51:39.433` | `-23.0` | `8.1` | `-5.0` | Storybook `めでたし めでたし`, `~6.0` s source-embedded streaming post-play UI (`01:51:33.3`–`01:51:39.4`, `[JA#2312]`), and Iroha's refusal shatter (`[JA#2313–2318]`) |
| `AM-05-BALCONY-REPLY` | `SEG-12` (`185.0`–`265.0` s) | `01:53:05.000` – `01:54:25.000` | `80.0` | `23` | `59.783` at `01:54:12.961` | `-19.1` | `17.2` | `-3.7` | Completed `Reply` (`[JA#2338]` `できた`) sung from Iroha's night balcony and received by Kaguya & `犬DOGE` on the Moon |
| `AM-06-COMEBACK-TITLE` | `SEG-14` (`0.0`–`40.0` s) | `02:10:00.000` – `02:10:40.000` | `40.0` | `5` | `82.015` at `02:10:33.367` | `-23.7` | `11.4` | `-8.0` | Dining-room photo narration (`[JA#2592–2598]`), silent late title card (`02:10:26.360`–`02:10:33.367`), and cut into `ray` end credits |

### 4.5 Post-audit bounded AV return derivatives (`CPK-AVRET-R1`, external to Git)

To answer the `10` bounded `VIDEO_TARGETED_ESCALATION` requests (`AV-01`–`AV-10`) in [CPK_F01_RECEIVING_HANDOFF.md](audits/CPK_F01_RECEIVING_HANDOFF.md) §6 (`1 of 1` primary-author return), `CPK-AVRET-R1` generated and hashed **`25` synchronized H.264/AAC clips** (`AVRET-01A`–`AVRET-10B` + `AVRET-03B2`, `2,307.2` s total, normalized with `-af aresample=async=1:first_pts=0`), **`32` lossless `1920x1080` PNG frames** (`AVFRM-01A`–`AVFRM-09B`), **`2` `3x` Lanczos crops** (`AVCROP-09B-FULL`, `AVCROP-09B-CENTER`), **`82` native 6-channel (`FL/FR/FC/LFE/SL/SR`) `48 kHz` PCM acoustic windows** directly from `0:a:0`, and a fresh byte-verified SubRip dump of `0:s:3` (`2,716` cues). Every individual filename, interval, byte count, and full 64-character SHA-256 digest is recorded in [CPK_F01_PRIMARY_AV_RETURN.md](audits/CPK_F01_PRIMARY_AV_RETURN.md) §§2.2–2.3 (`72,291` B).

### 4.6 Post-audit `v1.2` source-note errata on preserved `CPK-R1` (`v1.1`) entries

Historical `CPK-R1` rows in §§2–4 above are retained unaltered for auditability; the following source-verified corrections govern downstream citation in `v1.2` ledgers and [CPK_F01_INTEGRATED_SYNTHESIS.md](synthesis/CPK_F01_INTEGRATED_SYNTHESIS.md):

1. **Opening platform ident & `[JA#0001]` onset (corrects §3.1 `Program-start definition` and §3.2 `Audio start-offset handling`):** `t_F01 = 00:00:00.000` begins on black (`00:00:00.0`–`00:00:01.0`), followed by the animated Netflix `N` ribbon/streaks (`00:00:01.0`–`00:00:06.0`, `AVFRM-01A`) and a custom `NETFLIX PRESENTS` wallpaper (`00:00:06.0`–`00:00:11.0`, `AVFRM-01B`, chibi Yachiyo & `FUSHI` with stacked pancakes) before the cosmic Tsukuyomi moon/cloud vista opens at `~00:00:11.5`. `[JA#0001]` begins at **`00:00:26.026`** (`（ＮＡ(ナレーション):月見(るなみ)ヤチヨ）今は昔`), not `00:00:15.390` (where only instrumental/ambient prologue audio sounds). Normalization with `-af aresample=async=1:first_pts=0` remains exact (`0.0` s offset).
2. **End-credit lyric presence in Track 4 `[SDH]` `0:s:3` (corrects §2 `Japanese song lyrics` and §6 `Supporting Japanese text`):** Subtitle Track 4 (`0:s:3`) **does** contain timed Japanese `♪` lyric and vocal cues throughout the end-credit roll (`[JA#2599]`–`[JA#2709]`, `111` total cues across `ray 超かぐや姫！Version` `[JA#2599–2659]` and `メルト CPK! Remix` `[JA#2660–2709]`, including `109` `♪`-marked rows plus spoken interjections `[JA#2662]` `オーケー` and `[JA#2708]` `♪ …なんてね`). `v1.1`'s statement that end-credit songs lack SDH lyric lines is retracted (`CPK-B1-SOL61-P020` `REJECT`, `U0008` resolved).
3. **`FRM-14` (`01:56:36.500`) telemetry labels (corrects `CPK-R1` prose shorthand, `P034`):** The server-room monitor displays four separate telemetry fields — **`CPU load 24`**, **`FPS 89`**, **`Energy usage 53`**, and **`RAM usage 37`** — rather than a combined `CPU 24/89` ratio.
4. **`FRM-19` (`02:08:48.000`) native-crop monitor wording (`AV-09`, `P023`):** Direct `3x` Lanczos inspection (`AVCROP-09B-FULL`, `AVCROP-09B-CENTER`) verifies top tabs `Study of real...` and `tactile sensati...` and Japanese numbered heading **`1. 触覚の伝達経路`** (`tactile transmission pathway`, correcting `v1.1`'s `触覚の伝達構造`); lower numbered subheadings (`2. 触覚セン...`, `3. 触覚フィー...`) are partially occluded at native `1920x1080` resolution and are not reconstructed beyond legible characters.
5. **Available wallet balance vs spent sum (`FRM-03`, `00:09:09.500`, `C0007`):** `ふじゅペイ` displays `23,532円` (`20,532円` balance + `3,000 pt`) as Iroha's available total prior to checkout, not an exact receipt of yen spent in that transaction.

## 5. Run profile (`CPK-R1`) and capability verification

| Field | Verified observation |
|---|---|
| Run ID / role | `CPK-R1` — Primary `CONTINUOUS_AV` full-film author |
| Provider / model identity | Google DeepMind — owner-designated **Gemini 4 Carbon** (high-effort multimodal reasoning configuration; exact internal checkpoint build string not exposed by runtime prompt headers and therefore recorded as `UNKNOWN_INTERNAL_BUILD_ID` rather than guessed) |
| Execution surface | Antigravity IDE agentic harness on Windows (`pwsh`, local `ffmpeg`/`ffprobe` `n8.0`, native multimodal `read_file` ingestion of `.mp4` and `.png`) |
| Prior exposure / familiarity | No prior viewing of *Cosmic Princess Kaguya!* (`2026`) in this context; bootstrap bibliographic metadata (`P01`–`P06`) was read prior to source admission, and general cultural knowledge of classic *Taketori Monogatari* and Vocaloid history (`ryo`, `BUMP OF CHICKEN`, `HoneyWorks`, `40mP`, `kz`, `EasyPop`) is disclosed and strictly subordinated to on-film evidence |
| Capability probe & result | Verified on `SEG-01` (`00:00:00`–`00:10:20`) and `P2-CLIP-01`–`P2-CLIP-06`: `read_file` decodes synchronized visual frames at **`~1.0` fps effective visual sampling** (`1` frame/second displayed in the multimodal inspection stream) paired with **continuous synchronized Japanese audio** (`48 kHz` AAC stereo). `CONTINUOUS_AV` verified |
| Effective resolution & honest limits | Pass-1 MP4 inspection (`1280x720`, `~1.0` fps visual) reliably perceives shot order, staging, continuous voice/music/SFX, and macro-expressions, but **cannot** resolve sub-second (`<1.0` s) visual flashes or tiny `1080p` Japanese UI print on its own. Every load-bearing micro-text (`FRM-01`–`FRM-29` at lossless `1920x1080`), rapid cut boundary (`AM-01`–`AM-06` via `ffmpeg scdet`), and key vocal/staging scene (`P2-CLIP-01`–`P2-CLIP-06`) was verified in Pass 2 |
| Pass-1 → Pass-2 self-corrections | Pass-2 `1920x1080` `FRM` and high-bitrate `P2-CLIP` inspection corrected three Pass-1 approximations: (1) deceased father's kanji refined from phonetic guess to **`酒寄朝久` (`Sakayori Tomohisa`, `FRM-23` + `FRM-07`)**; (2) Iroha's school enrollment refined to **`2年3組12番` (`FRM-12`, 2nd-year high school, age 17)**; (3) Yachiyo's `00:35:06` bridge farewell verified as solo piano `Remember` plus spoken **`「いつも来てくれてありがとね…… 彩葉。」` (`P2-CLIP-02`)** |

## 6. Per-channel and interval coverage summary (`CPK-R1`)

| Channel / modality | Authorized F01 range | Requirement | Inspection status | Method & effective resolution | Uninspected gaps / material limits | Next owner |
|---|---|---|---|---|---|---|
| Synchronized continuous AV (`0:v:0` + `0:a:0`) | `00:00:00.000` – `02:22:03.207` (`SEG-01`–`SEG-15` + `P2-CLIP-01`–`P2-CLIP-06`) | `REQUIRED` | `COMPLETE_FOR_DECLARED_SCOPE` | Native multimodal `.mp4` (`~1.0` fps `1280x720` video + continuous `48 kHz` Japanese audio; `20` s overlaps across all `14` seams) | Visual events `<1.0` s outside `AM`/`FRM` anchors remain bounded to `±0.5` s | OpenAI blind bundle verifier |
| Lossless static `1920x1080` visual frames | `29` targeted timestamps (`00:01:23.500` – `02:19:48.000`, `FRM-01`–`FRM-29`) | `REQUIRED` (for micro-text/credits) | `COMPLETE_FOR_DECLARED_SCOPE` | Lossless `1920x1080` PNG multimodal `read_file` | Static endpoints only | OpenAI blind bundle verifier |
| Supporting Japanese text (`0:s:3` `Japanese [SDH]`) | `00:00:00.000` – `02:22:03.207` (`[JA#0001]`–`[JA#2716]`) | `REQUIRED` | `COMPLETE_FOR_DECLARED_SCOPE` | Full UTF-8 SRT aligned to `t_F01` and cross-checked against Track 1 spoken Japanese | End-credit themes (`ray`, `メルト`) carry credit cards (`FRM-24`) but no SDH lyric lines; spoken vs SDH divergences logged in ledgers | OpenAI blind bundle verifier |
| Secondary English subtitles (`0:s:2` `English`) | `00:00:00.000` – `02:22:03.207` (`[EN#0001]`–`[EN#2079]`) | `OPTIONAL` | `COMPLETE_FOR_DECLARED_SCOPE` | Extracted UTF-8 SRT used strictly for localization contrast | Never used as primary narrative authority | OpenAI blind bundle verifier |
| Deterministic acoustic/cut measurements (`AM`) | `6` structural windows (`AM-01`–`AM-06`) + `7` PSNR calibration points (`CAL-01`–`CAL-07`) | `OPTIONAL` (corroborative) | `COMPLETE_FOR_DECLARED_SCOPE` | `ffmpeg n8.0` `scdet=threshold=12`, `ebur128`, `psnr` | Scoped to `6` load-bearing transitions | Integrator / targeted escalation if needed |

## 7. Independent verifier (`CPK-B1-SOL61`) and post-audit reconciliation (`CPK-INT`) profiles

| Execution / stage | Producer & role | Verified source / derivative scope | Preserved public home |
|---|---|---|---|
| `CPK-B1-SOL61` (Phase A independent + Phase B2 blind + post-exposure comparison) | Codex assistant (`requested Sol 6.1 Max`; `BUNDLE_MEDIATED`, `AO = 0 s`, `CAV = 0 s`) | Bound to exact same `CPK-W01-NF-WEBRIP-HEVC` (`b940eede...`); `5,761`-file local bundle (`5,465` JPEGs, `274` contact sheets), `2,716/2,716` JA cues read, `79` EN pairings, `127` sheets (`2,525` slots) + `29` clean frames in Phase A; `58` PNG + `18` JPEG views in Phase B2; `13` post-exposure `960x540` PNG tiles (`PE01`–`PE16`) | Retrospective noncurrent envelope [independent/CPK-B1-SOL61/](independent/CPK-B1-SOL61/PUBLICATION_README.md) (`16` files, authorized via `frozen_generation_publications`) + verifier audits `audits/CPK_F01_*.md` & receipts `audits/CPK-B1-SOL61/` (`23` files) |
| `CPK-AVRET-R1` (`1 of 1` bounded primary-author AV return) | **Gemini 4 Carbon** (`CONTINUOUS_AV` + native `5.1` PCM + lossless `1920x1080` / `3x` crops; `blind_order_achieved: false` disclosed) | `25` synchronized clips (`2,307.2` s), `32` `1920x1080` PNGs, `2` `3x` crops, `82` 6-channel PCM acoustic windows, raw `0:s:3` SRT (`2,716` cues) across `AV-01`–`AV-10` | [audits/CPK_F01_PRIMARY_AV_RETURN.md](audits/CPK_F01_PRIMARY_AV_RETURN.md) (`v1.0`, `draft_noncurrent`) |
| `CPK-INT` (Stage-3 owner-designated integration) | **Gemini 4 Carbon** (same-session dual-role execution with `CPK-AVRET-R1` explicitly disclosed per [CPK_RECONCILIATION_PROFILE.md](CPK_RECONCILIATION_PROFILE.md) §1) | Full reconciliation across `20` `CPK-R1` claims, `35` `P001`–`P035` assertions, `28` `CPK-B1-SOL61` claims, `SA01`–`SA14`, and `AV-01`–`AV-10` | [audits/CPK_F01_RECONCILIATION_RECORD.md](audits/CPK_F01_RECONCILIATION_RECORD.md) (`v1.1`), `v1.2` ledgers, and canonical [synthesis/CPK_F01_INTEGRATED_SYNTHESIS.md](synthesis/CPK_F01_INTEGRATED_SYNTHESIS.md) (`v1.0`) |

## 8. Registers

Bound narrative witnesses: **1** (`CPK-W01-NF-WEBRIP-HEVC`). Language text derivatives: **2** (`CPK-W01-SUB-JA-T4`, `CPK-W01-SUB-EN-T3`). Synchronized Pass-1 AV segments: **15** (`SEG-01`–`SEG-15`). Targeted Pass-2 AV clips: **6** (`P2-CLIP-01`–`P2-CLIP-06`). Targeted post-audit AV return clips: **25** (`AVRET-01A`–`AVRET-10B` + `AVRET-03B2`). Lossless `1920x1080` PNG frames & crops: **63** (`29` `FRM-01`–`FRM-29` + `32` `AVFRM-01A`–`AVFRM-09B` + `2` `AVCROP-09B-*`). Deterministic `AM` cut/loudness windows: **6** (`AM-01`–`AM-06`, all tabulated in §4.4). Calibration mappings: **7** (`CAL-01-BEGIN`–`CAL-07-END` under `CPK-CLK-F01-GLOBAL`). Analytical executions recorded: **3** (`CPK-R1`, `CPK-B1-SOL61`, `CPK-AVRET-R1` / `CPK-INT`).
