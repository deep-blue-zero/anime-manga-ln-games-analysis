---
title: "Cosmic Princess Kaguya! (F01) — blind bundle-verifier input packet and neutral observation queue"
series: cosmic-princess-kaguya
artifact_id: CPK_F01_BLIND_INPUT_PACKET
artifact_type: blind_audit_input_packet
generation: CPK-G1
version: "1.0"
status: draft_noncurrent
authority_scope: "Sanitized pre-exposure technical transfer manifest, exposure allowlist/quarantine rules, and neutral observation queue for the separate BUNDLE_MEDIATED verifier"
source_boundary: "Same-witness F01 technical binding (CPK-W01-NF-WEBRIP-HEVC, 02:22:03.207); zero primary narrative claims, scene labels, or expected answers exposed"
canonical_home: series/cosmic-princess-kaguya/audits/CPK_F01_BLIND_INPUT_PACKET.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
do_not_use_as_literary_evidence: true
---

# Blind bundle-verifier input packet (`F01`)

## 1. Exposure control: pre-freeze allowlist vs withheld primary set

Under [CPK_RECONCILIATION_PROFILE.md](../CPK_RECONCILIATION_PROFILE.md) §§3–4, the independent `BUNDLE_MEDIATED` verifier (owner-requested operational assignment: separate OpenAI auditor in a fresh unexposed context) must complete its independent pass and freeze `audits/CPK_F01_BLIND_OBSERVATIONS.md` by exact byte count and SHA-256 **before** opening any primary narrative artifact. Do **not** run broad repository searches across `series/cosmic-princess-kaguya/` prior to blind freeze.

| Pre-freeze **ALLOWED** inputs (Set 1) | Pre-freeze **STRICTLY WITHHELD** until `CPK_F01_BLIND_OBSERVATIONS.md` is frozen (Set 2) |
|---|---|
| `AGENTS.md`, `governance/AGENT_ROUTING.md`, and live bundle/reconciliation/handoff policies | `series/cosmic-princess-kaguya/readings/CPK_F01_PRIMARY_DEEP_READING.md` |
| `series/cosmic-princess-kaguya/CPK_ANALYTICAL_METHOD.md` (`v1.0`) | `series/cosmic-princess-kaguya/CPK_OBSERVATION_LEDGER.md` (`v1.1` populated) |
| `series/cosmic-princess-kaguya/CPK_SYNTHESIS_ARCHITECTURE.md` (`v1.0`) | `series/cosmic-princess-kaguya/CPK_CHARACTER_RELATIONSHIP_LEDGER.md` (`v1.1` populated) |
| `series/cosmic-princess-kaguya/CPK_RECONCILIATION_PROFILE.md` (`v1.0`) | `series/cosmic-princess-kaguya/CPK_CLAIM_REVISION_LEDGER.md` (`v1.1` populated) |
| **This file:** `series/cosmic-princess-kaguya/audits/CPK_F01_BLIND_INPUT_PACKET.md` (`v1.0`) | `series/cosmic-princess-kaguya/CPK_SOURCE_INVENTORY.md` (`v1.1`, withheld pre-freeze because §4–§5 include primary target labels; sanitized technical specs are provided in §2 below) |
| Private local `F01` film bundle / derivatives verified against the exact hashes in §2 below | `series/cosmic-princess-kaguya/audits/CPK_F01_RECONCILIATION_RECORD.md` (holds withheld adjudication mapping) & `CURRENT_STATE_AND_CORPUS_MAP.md` (`v1.3`) |

**Contamination rule:** If the verifier session reads any Set-2 file, external plot summary, review, or character wiki before freezing `audits/CPK_F01_BLIND_OBSERVATIONS.md`, it must immediately record `blind_order_achieved: false`, list exact exposed paths/timestamps, and refrain from labeling its observations blind. Disclose any pre-existing model familiarity with the work title or *Taketori Monogatari* separately from artifact exposure.

---

## 2. Sanitized `F01` witness, stream, clock, and derivative manifest (annotation-stripped)

All interpretive descriptions have been stripped from the tables below so technical verification introduces zero analytical framing.

### 2.1 Primary witness and language stream bindings

| Field | Bound specification |
|---|---|
| Public-safe witness ID | `CPK-W01-NF-WEBRIP-HEVC` |
| Work / authorized unit | `超かぐや姫！` (*Cosmic Princess Kaguya!*) — single feature film `F01` |
| Container & size | Matroska `.mkv` (`46` streams: `1` video, `12` audio, `33` subtitle), `4,916,885,885` bytes |
| Witness SHA-256 | `b940eede5e3ce2e83e507a33e6523516c21e770dbccd8cc9e4461af77b23a42a` |
| Measured duration & frame count | `8523.207000` s (`02:22:03.207`), `204,352` video frames at `24000/1001` fps (`23.976024` fps), `1920x1080` `HEVC Main 10` |
| Global citation clock | `CPK-CLK-F01-GLOBAL`: `t_F01 = 00:00:00.000` at video stream `0:v:0` `PTS = 0.000` (`start_time = 0.000000` s) |
| **Primary audio (`CPK-W01-AUD-JA-T1`)** | Audio Track 1 (`0:a:0`, `ff_idx = 1`, `mkv_track_number = 2`), `opus` `5.1` `48000` Hz, `jpn` (`Japanese`). Raw stream `start_time = 0.138000` s; normalize with `first_pts=0` (`-af aresample=async=1:first_pts=0`) when extracting/transcoding so audio `t=0` matches video `PTS=0` |
| **Supporting Japanese text (`CPK-W01-SUB-JA-T4`)** | Subtitle Track 4 (`0:s:3`, `ff_idx = 16`, `mkv_track_number = 17`), `subrip` UTF-8 `jpn` (`Japanese [SDH]`), `2,716` cues (`[JA#0001]`–`[JA#2716]`); extracted `.srt` = `214,854` bytes, SHA-256 `15ea610f9a63347d66e39770f9c03f78d2e23ec95aaa2c03462747ecc53c89a4` |
| **Optional secondary text (`CPK-W01-SUB-EN-T3`)** | Subtitle Track 3 (`0:s:2`, `ff_idx = 15`, `mkv_track_number = 16`), `subrip` UTF-8 `eng` (`English`), `2,079` cues (`[EN#0001]`–`[EN#2079]`); extracted `.srt` = `150,481` bytes, SHA-256 `811cb0369a10375b40041e8de8ed3f0e5dd4bc1fcc263b7bf0254f306bffdc6a` |

### 2.2 Clock calibration points (`CPK-CLK-F01-GLOBAL`)

| Calibration ID | Source `t_F01` | Segment mapping formula | Verified residual / precision |
|---|---|---|---|
| `CAL-01-BEGIN` | `00:00:30.000` | `SEG-01`: `0.000 + t_local` (`+00:30.000`) | `0.000` s (`±0.042` s frame; `±0.5` s baseline) |
| `CAL-02-EARLY` | `00:10:50.000` | `SEG-02`: `600.000 + t_local` (`+00:50.000`) | `0.000` s (`±0.042` s) |
| `CAL-03-Q1` | `00:35:00.000` | `SEG-04`: `1800.000 + t_local` (`+05:00.000`) | `0.000` s (`±0.042` s) |
| `CAL-04-MID` | `01:15:00.000` | `SEG-08`: `4200.000 + t_local` (`+05:00.000`) | `≤0.041` s (`±0.042` s) |
| `CAL-05-Q3` | `01:44:55.000` | `SEG-11`: `6000.000 + t_local` (`+04:55.000`) | `≤0.041` s (`±0.042` s) |
| `CAL-06-CLIMAX` | `02:05:00.000` | `SEG-13`: `7200.000 + t_local` (`+05:00.000`) | `≤0.041` s (`±0.042` s) |
| `CAL-07-END` | `02:20:00.000` | `SEG-15`: `8220.000 + t_local` (`+03:00.000`) | `0.000` s (`±0.042` s) |

### 2.3 Synchronized derivative hashes (for same-derivative or bundle cross-check)

**Contiguous segments (`SEG-01`–`SEG-15`, `20.0` s overlaps):**
- `SEG-01` (`00:00:00`–`00:10:20`, `90,300,615` B): `9e9e334c71ed7ba0297fff2b56a9c6cbc7d6cde54069c48b7a949eaea77f9f92`
- `SEG-02` (`00:10:00`–`00:20:20`, `74,262,479` B): `4a2615268f7dc5386bcaaef6c6cabe54e188eca2bda296ceae4edbc93f888df6`
- `SEG-03` (`00:20:00`–`00:30:20`, `80,806,094` B): `22ebfab7cbd216d630fbac1ef911ef4bfe9864fd328d33ace6af201d37275bda`
- `SEG-04` (`00:30:00`–`00:40:20`, `100,271,646` B): `dad8c97962439c119dc414572776620ddb4441c61c365b95dcb3a52eaf0362fa`
- `SEG-05` (`00:40:00`–`00:50:20`, `99,802,856` B): `bdc8f8e209cc1377326ced3f34cc635f4755de2ad006908b71017e0c8e5bcbf0`
- `SEG-06` (`00:50:00`–`01:00:20`, `76,178,815` B): `68ef467294ce77954e0606a84d976f704563f008fef52e7268909229ba012a8c`
- `SEG-07` (`01:00:00`–`01:10:20`, `84,204,823` B): `39c9f744e97191ef19cb947de962db93b16bfe237b17fea81ee22539d4bfb8c3`
- `SEG-08` (`01:10:00`–`01:20:20`, `103,678,577` B): `fdd0bb0f4d1c2080dac59767beea237f67a062da8ab60da7f357ad8a181a80d1`
- `SEG-09` (`01:20:00`–`01:30:20`, `79,455,830` B): `873f7f894ed3528383b7df38def1173ba63ea843f451b4e704eeeab28d23ea3f`
- `SEG-10` (`01:30:00`–`01:40:20`, `72,998,054` B): `52eb221b139dd9768226550280a800770b5e7de762359fc78e0ba425075fbb0a`
- `SEG-11` (`01:40:00`–`01:50:20`, `76,321,367` B): `3f9ce382df3eb984adb2f5344c967016309d5e92c7d23d3ebe3e2b8c049e6fe6`
- `SEG-12` (`01:50:00`–`02:00:20`, `85,342,391` B): `742ce576c22c229059bbde7cd05e3c0ee32c0de7cac17448ef44873c6876887c`
- `SEG-13` (`02:00:00`–`02:10:20`, `85,174,710` B): `79295c0d969943575e44018b840abf277dc5a83a706e6b9f2f08cda2300b44be`
- `SEG-14` (`02:10:00`–`02:17:20`, `77,452,029` B): `efe5d2d2da1b3a4737207183e3d10e96c7c49f4ceabcd136104fd7f4cd56e137`
- `SEG-15` (`02:17:00`–`02:22:03.207`, `31,352,654` B): `d4e5bb67f50122d468e4092b7e29afe7d4b82062a00cb1e5f7612d331289fd81`

**Targeted clips (`P2-CLIP-01`–`P2-CLIP-06`) & lossless `1920x1080` PNG stills (`FRM-01`–`FRM-29`):**
- `P2-CLIP-01` (`00:07:28`–`00:07:58`): `05aabccb13b32e78c0937fcc8a522b42eb606fe0271494fda93d42b960afe0c2`
- `P2-CLIP-02` (`00:34:45`–`00:35:15`): `9726d958bbcd69937924c00fd60d5be905805451b6935e792a86d8cedcc4bbc7`
- `P2-CLIP-03` (`01:24:02`–`01:25:10`): `eaf54854d58ce75995db021d176c1c383c18710405f12f8929292691f5aeea9f`
- `P2-CLIP-04` (`01:47:34`–`01:48:18`): `6a74497f24a2f5e395cb9b4188cb27198376687b7af81b6aeef192b53db265cd`
- `P2-CLIP-05` (`01:51:20`–`01:51:58`): `29691138c4e0c25106882524f1a69a93a6b9fe3d38291fbf6f0dfd9daef04536`
- `P2-CLIP-06` (`02:05:10`–`02:07:14`): `fdda79b490841456edec7ff3b530ed46dec51386e566519e1172bc65bc6fc476`
- `FRM-01` (`00:01:23.500`, `5622938d`) | `FRM-02` (`00:01:34.000`, `55770928`) | `FRM-03` (`00:09:09.500`, `9fce97cb`) | `FRM-04` (`00:10:10.000`, `9c6a1526`) | `FRM-05` (`00:35:59.000`, `7f0d7f86`) | `FRM-06` (`00:41:40.000`, `21715192`) | `FRM-07` (`01:17:23.000`, `c57cb8d5`) | `FRM-08` (`01:24:52.000`, `7c8bca03`) | `FRM-09` (`01:45:56.500`, `29e30ade`) | `FRM-10` (`01:49:10.000`, `a8217888`) | `FRM-11` (`01:49:32.000`, `1189c0ac`) | `FRM-12` (`01:50:22.500`, `28a38d0e`) | `FRM-13` (`01:51:36.000`, `959d2c10`) | `FRM-14` (`01:56:36.500`, `a6dd55e7`) | `FRM-15` (`01:58:59.000`, `c156cbc9`) | `FRM-16` (`01:59:01.000`, `0d07ad73`) | `FRM-17` (`01:59:04.000`, `6e008975`) | `FRM-18` (`02:07:22.500`, `f1d2a2c9`) | `FRM-19` (`02:08:48.000`, `15c9c8bd`) | `FRM-20` (`02:09:48.000`, `b2300038`) | `FRM-21` (`02:10:13.000`, `c9e736f1`) | `FRM-22` (`02:10:45.000`, `ce19e66a`) | `FRM-23` (`02:10:56.000`, `26dfc841`) | `FRM-24` (`02:15:28.000`, `ff833f64`) | `FRM-25` (`02:15:39.000`, `9c35d98b`) | `FRM-26` (`02:15:51.000`, `dc5c8a8a`) | `FRM-27` (`02:18:05.000`, `e1dcc577`) | `FRM-28` (`02:18:16.000`, `08819704`) | `FRM-29` (`02:19:48.000`, `841c6f84`)

---

## 3. Verifier blind-pass procedure

1. **Verify bundle and capabilities**: Check witness `CPK-W01-NF-WEBRIP-HEVC` (or supplied bundle layers) against [MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md](../../../governance/source-policies/MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md) §5. Record actual model/version/surface/effort, image inspection capability, Japanese text availability, and whether verified audio inspection (`AO`) is available or `UNAVAILABLE` (possessing audio files or running `ffmpeg` metrics is `AM`, not `AO` listening).
2. **Survey full `F01` independently first**: Traverse `[00:00:00.000, 02:22:03.207]` via contact sheets, clean frames, Japanese text crosswalks, and any verified audio route, logging independent structural divisions, descriptive observations, and initial questions **before** answering §4's queue so question selection does not bias initial coverage.
3. **Answer the neutral observation queue (§4)**: Inspect surrounding context for `Q-F01-0001`–`Q-F01-0024`. Report what is observable in accessible channels, mark bundle-inaccessible continuous motion or audio honestly as `UNAVAILABLE` / escalation-needed, and never guess unseen motion between static frames.
4. **Freeze `audits/CPK_F01_BLIND_OBSERVATIONS.md`**: Record its exact byte count and SHA-256 hash prior to opening Set-2 artifacts (`readings/CPK_F01_PRIMARY_DEEP_READING.md`, populated ledgers, and `audits/CPK_F01_RECONCILIATION_RECORD.md`) to perform `audits/CPK_F01_CLAIM_AUDIT.md`.

---

## 4. Neutral observation queue (`Q-F01-0001` – `Q-F01-0024`)

Queue order is strictly chronological along `CPK-CLK-F01-GLOBAL` (`origin: CPK-R1 post-reading neutral extraction`). Every question asks for descriptive observation rather than agreement with an unstated thesis.

| `queue_id` | Neutral observation question | Target channel(s) | Film interval (`t_F01`) | Nearby cue / frame | Escalation class if bundle-inaccessible | Requirement |
|---|---|---|---|---|---|---|
| `Q-F01-0001` | What visual setting, objects, spoken narration, and onscreen text (including presence or absence of studio logos or a main title card) appear from container start to the first scene transition? | `FRM`, `TXT`, `AO`, `AM` | `00:00:00.000`–`00:01:22.000` | `[JA#0001]`–`[JA#0008]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0002` | Transcribe all legible Japanese/English text on the bookshelf and its top ornament at `00:01:23.500`, and transcribe the vertical border text and character staging at `00:01:34.000`, noting any dialect features. | `FRM`, `TXT` | `00:01:22.000`–`00:01:37.000` | `FRM-01`, `FRM-02` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0003` | In `00:07:28.000`–`00:07:58.000`, what objects does the speaker look at, what exact Japanese words/melody are sung or spoken, is instrumental accompaniment present or absent, and how does the infant react? | `AO`, `TXT`, `CAV`/`FRM` | `00:07:28.000`–`00:07:58.000` | `[JA#0119]`–`[JA#0124]`, `P2-CLIP-01` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0004` | Transcribe the exact numerical balances/items on the smartphone screen at `00:09:09.500` and the browser URL, video title, view count, and visual imagery at `00:10:10.000`. | `FRM`, `TXT` | `00:09:08.000`–`00:10:14.000` | `FRM-03`, `FRM-04` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0005` | In `00:20:05.000`–`00:24:05.000`, what book is being read, how does Kaguya describe its ending in Japanese, and what speech register/particles does she use? | `TXT`, `AO`, `FRM` | `00:20:05.000`–`00:24:05.000` | `[JA#0420]`–`[JA#0472]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0006` | In `00:33:35.000`–`00:35:15.000`, record Yachiyo's exact Japanese reaction at `~00:33:59`, then describe the bridge interaction (`00:34:45`–`00:35:15`), any background instrument, when `いろP` exits, and the exact Japanese words spoken after `いろP`'s exit. | `CAV`, `AO`, `TXT` | `00:33:35.000`–`00:35:15.000` | `[JA#0703]`–`[JA#0739]`, `P2-CLIP-02` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0007` | Transcribe the scheduled activities and academic subjects on the wall chart at `00:35:59.000`, and list all song titles/artists visible on the smartphone playlist at `00:41:40.000`. | `FRM`, `TXT` | `00:35:56.000`–`00:41:43.000` | `FRM-05`, `FRM-06` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0008` | Compare household food preparation and caregiving roles between `00:44:10`–`00:48:30` and `01:15:30`–`01:17:10`: who prepares food or tends illness in each passage, and under what physical conditions? | `FRM`, `TXT`, `CAV` | `00:44:10.000`–`00:48:30.000` & `01:15:30.000`–`01:17:10.000` | `[JA#0945]`–`[JA#1030]`, `[JA#1630]`–`[JA#1665]` | `VIDEO_FULL_EPISODE_ESCALATION` | `REQUIRED` |
| `Q-F01-0009` | What is the match score of the `KASSEN` battle (`00:50:12`–`01:02:15`), what song follows in `01:02:15`–`01:06:30`, what happens to the overall Yachiyo Cup standings, and what personal relationship is disclosed in `01:06:30`–`01:10:15`? | `TXT`, `FRM`, `AO`, `CAV` | `00:50:12.000`–`01:10:15.000` | `[JA#1120]`–`[JA#1510]` | `VIDEO_FULL_EPISODE_ESCALATION` | `REQUIRED` |
| `Q-F01-0010` | At `01:17:20.000`–`01:18:30.000`, transcribe the full folder path, filename, duration, and modification date at `01:17:23.000`, and describe the audio heard when the file is played alongside any comparison to earlier music in the film. | `FRM`, `TXT`, `AO` | `01:17:20.000`–`01:18:30.000` | `FRM-07`, `[JA#1670]`–`[JA#1695]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0011` | In `01:24:02.000`–`01:25:10.000`, trace the shot-by-shot sequence across real room, virtual stage, and Tokyo transit: exact Japanese dialogue (`[JA#1826]`–`[JA#1836]`), any close-up object inserts, how white-suited figures are seen vs unseen at `01:24:42`–`01:24:55`, and any projected date. | `CAV`, `FRM`, `TXT`, `AO` | `01:24:02.000`–`01:25:10.000` | `P2-CLIP-03`, `FRM-08` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0012` | During `01:45:40.000`–`01:46:10.000`, what action does `帝アキラ` take against the descending overhead beam, what exact English/Japanese warning text appears at `01:45:56.500`, and what happens to his avatar? | `FRM`, `TXT`, `CAV` | `01:45:40.000`–`01:46:10.000` | `FRM-09` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0013` | In `01:47:34.000`–`01:48:18.000`, describe (a) the audio mix and room blocking at `01:47:36`–`01:47:46`, (b) any change in Kaguya's eye color and facial expression at `01:47:50`–`01:47:55`, and (c) any secondary character/mascot movement or sound at `01:47:55`–`01:48:05`. | `CAV`, `AO`, `TXT` | `01:47:34.000`–`01:48:18.000` | `P2-CLIP-04`, `[JA#2196]`–`[JA#2205]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0014` | Transcribe the handwritten refrigerator notes (including cooking tips) at `01:49:10.000` and the full mobile remittance timestamp, sender, message, and register at `01:49:32.000`. | `FRM`, `TXT` | `01:49:08.000`–`01:49:36.000` | `FRM-10`, `FRM-11` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0015` | Transcribe the student grade, class, number, full name, first/second university choices, and stated post-graduation career on the form at `01:50:22.500`, then record the exact Japanese exchange on the phone call in `01:52:05`–`01:53:02`. | `FRM`, `TXT`, `AO` | `01:50:20.000`–`01:50:26.000` & `01:52:05.000`–`01:53:02.000` | `FRM-12`, `[JA#2260]`–`[JA#2288]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0016` | Describe the exact screen layout, onscreen text, background audio, timestamps, and character actions across `01:51:25.000`–`01:51:58.000`, including the exact Japanese wording spoken immediately after the screen layout changes back. | `CAV`, `FRM`, `TXT`, `AO`, `AM` | `01:51:25.000`–`01:51:58.000` | `P2-CLIP-05`, `FRM-13` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0017` | In `01:53:05.000`–`01:55:15.000`, trace the parallel editing between Earth and the Moon: what object near Kaguya reacts to the song, what happens to Kaguya's eyes/actions, and what happens to her craft in space? | `CAV`, `AO`, `TXT`, `AM` | `01:53:05.000`–`01:55:15.000` | `[JA#2290]`–`[JA#2335]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0018` | Inspect `01:56:20.000`–`02:00:10.000`: describe the organisms/objects and telemetry labels in `FRM-14` (`01:56:36.500`), list the historical eras depicted in the montage, and transcribe the exact dates, badges, handles, and post text in `FRM-16` (`01:59:01`) and `FRM-17` (`01:59:04`). | `FRM`, `TXT`, `CAV` | `01:56:20.000`–`02:00:10.000` | `FRM-14`–`FRM-17`, `[JA#2360]`–`[JA#2450]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0019` | In `02:05:10.000`–`02:07:14.000`, measure any extended pause without dialogue after `[JA#2527]`, record who sings `[JA#2534]`–`[JA#2535]` and whether instruments are present, and record the exact Japanese wishes/vows exchanged afterward. | `CAV`, `AO`, `TXT` | `02:05:10.000`–`02:07:14.000` | `P2-CLIP-06`, `[JA#2525]`–`[JA#2541]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0020` | Across `02:07:20.000`–`02:09:04.000`, note any accessibility tag at `[JA#2543]` (`FRM-18`), identify who meets Iroha in `02:07:53`–`02:08:33`, transcribe all English/Japanese research headings on the widescreen monitor at `02:08:48.000` (`FRM-19`), and record Iroha's exact Japanese parting phrase at `02:09:01`. | `FRM`, `TXT`, `AO` | `02:07:20.000`–`02:09:04.000` | `FRM-18`, `FRM-19`, `[JA#2543]`–`[JA#2572]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0021` | In `02:09:04.000`–`02:09:32.000`, record the exact Japanese lines spoken upon awakening (`[JA#2574]`–`[JA#2582]`), including any model/prototype designation mentioned and any remark about sensory capabilities. | `TXT`, `AO`, `FRM` | `02:09:04.000`–`02:09:32.000` | `[JA#2573]`–`[JA#2582]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0022` | Inspect `FRM-20` (`02:09:48.000`) and surrounding dialogue (`[JA#2585]`–`[JA#2591]`): how many characters are on the lift, how do they address each other, and how do foot-to-floor contact, lighting/glow, and cast shadows compare across the three figures? | `FRM`, `TXT`, `CAV` | `02:09:33.000`–`02:10:02.000` | `FRM-20`, `[JA#2583]`–`[JA#2591]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0023` | In `02:10:03.000`–`02:10:34.000`, compare speaker tags in Subtitle Track 4 (`[JA#2592]`–`[JA#2596]`) against the actual voice(s) heard on Japanese Audio Track 1, and record the exact text and timestamps of any title card before the credits begin. | `AO`, `TXT`, `FRM`, `AM` | `02:10:03.000`–`02:10:34.000` | `FRM-21`, `[JA#2592]`–`[JA#2596]` | `VIDEO_TARGETED_ESCALATION` | `REQUIRED` |
| `Q-F01-0024` | From `02:10:33.367` to `02:22:03.207`, verify cast kanji in `FRM-22`–`23` (especially all members of the `酒寄` family), song/staff credits in `FRM-24`–`29`, whether Track 4 carries end-credit song lyrics, any left-window `原画` vignettes, and the exact visual setting and Japanese dialogue of `02:19:53`–`02:20:15`. | `FRM`, `TXT`, `AO`, `CAV` | `02:10:33.367`–`02:22:03.207` | `FRM-22`–`FRM-29`, `[JA#2710]`–`[JA#2716]` | `VIDEO_TARGETED_ESCALATION` | `OPTIONAL` (vignettes) / `REQUIRED` (credits & coda) |
