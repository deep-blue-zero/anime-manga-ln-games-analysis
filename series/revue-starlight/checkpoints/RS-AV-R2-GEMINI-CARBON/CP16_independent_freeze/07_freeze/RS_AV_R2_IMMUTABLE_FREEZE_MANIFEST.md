---
title: "RS-AV-R2-GEMINI-CARBON — Phase E Immutable Pre-Exposure Freeze Manifest (CP16_IMMUTABLE_FREEZE)"
artifact_type: "freeze_manifest"
generation: "RS-AV-R2-GEMINI-CARBON"
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
project: "series/revue-starlight"
execution_identity: "RS-AV-R2-GEMINI-CARBON"
model: "Gemini 4 Carbon (High reasoning)"
existing_corpus_exposure: false
checkpoint_id: "CP16_IMMUTABLE_FREEZE"
timestamp_utc: "2026-11-13T18:06:49.175378+00:00"
---

# Phase E Immutable Freeze Manifest (`RS-AV-R2-GEMINI-CARBON` / `CP16_IMMUTABLE_FREEZE`)

> [!IMPORTANT]
> **Binding Pre-Exposure Freeze Attestation**: Every analytical file listed below (`27` independent deliverables across `00_inventory/` through `06_ledgers/`, spanning `35` major claims `RS-AV-R2-GEMINI-CARBON-CLM-0001`–`0035`) was authored and frozen **prior to opening a single file in `series/revue-starlight/` of `anime-manga-ln-games-analysis`** (`existing_corpus_exposure: false`). From this commit (`CP16_IMMUTABLE_FREEZE`) onward, **zero files in `00_inventory/` through `07_freeze/` may ever be modified**. All Phase F comparative audits and post-exposure self-audits reside exclusively in `08_comparative_audit/` and the noncurrent target-repository candidate package.

---

## 1. Execution Configuration, Inspection Modalities, & Disclosed Limits

- **Execution Identity**: `RS-AV-R2-GEMINI-CARBON`
- **Model & Reasoning**: Gemini 4 Carbon (High reasoning)
- **Authority Classification**: Noncurrent independent experimental candidate (`status: draft_noncurrent`, `do_not_use_as_current_authority: true`)
- **Inspected Corpus Scope**: `16` complete Japanese-original animated units (`TV01`–`TV12`, `OVA01`–`OVA03`, `2021` Sequel Film) = **`25,842.313s` (`07:10:42.313`)**, 100% end-to-end two-pass native AV inspection.
- **Calibrated Inspection Methods & Limits**:
  1. *Pass 1 Native Video (`read_file` MP4)*: Consecutive overlapping H.264/AAC segments with burned millisecond `PTS` clock; empirically calibrated at **`1.000 fps` visual sampling (`t = k + 0.46s`)** + **100% continuous synchronized Japanese audio**.
  2. *Pass 2 High-Density Visual & Acoustic Verification*: Unburned `1920x1080` PNG stills + `4–12 fps` contact sheets around edit/combat boundaries; `cropdetect` aspect-ratio audits; `48 kHz` lossless stereo `FLAC` (`TV`/`OVA`, pinned `-map 0:v:0 -map 0:a:0` to exclude `S01E01`/`05`/`10` seiyū commentary) + upstream `635 kbps` 6-channel `5.1` AAC stem telemetry (`MOVIE` `0:a:1`, `7,222` `1s` bins) + `0.5s` stereo RMS curves.
  3. *Missing / Quarantined Channels*: `OVA01`–`OVA03` carry **0% Japanese subtitle tracks** (transcribed strictly from `FLAC` audio + `1080p` signage, marking uncertain rapid syllables `[聴取不確定]`); *Revue Starlight -Re LIVE-* mobile game, stage plays, manga, external web sources, and local `[SPOILERS] extra fun fact notes.txt` were **0% accessed**. Editorial erratum preserved without back-editing `CP01`: `RS_AV_R2_TV01_DEEP_READING.md` line 15 printed `f4dc5d4b...`; true `S01E01.mkv` SHA-256 is `a6a97c09edc8e69c1d283822afff560a50609775893e3e429e7d310c01852250`.

---

## 2. Inspected Primary Source Media & Verified SHA-256 Digests (`16` Units)

| Unit | Primary Media Path | Size (Bytes) | Duration (s) | Primary Media SHA-256 | Auxiliary `.ass` / `5.1` Witness SHA-256 |
| :--- | :--- | ---: | ---: | :--- | :--- |
| `TV01` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E01.mkv` | `1,167,641,893` | `1446.784` | `a6a97c09edc8e69c1d283822afff560a50609775893e3e429e7d310c01852250` | ASS: `06c35606770414ff…` |
| `TV02` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E02.mkv` | `1,073,255,013` | `1445.615` | `899a91f16b01ffcd00f91ded0cb5e27cd9254c0225afa3920270820a6ad36eda` | ASS: `9fdd1039588b5ef6…` |
| `TV03` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E03.mkv` | `995,626,610` | `1445.780` | `f8ebfcb4a48f3ca32ce2e303e77c58c8a4eea3e066aca985e1274736faf20aa1` | ASS: `236353e6bc06bca9…` |
| `TV04` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E04.mkv` | `1,026,276,103` | `1445.655` | `b2d2bcf99d7111e3436d49df21383e330402366d35522122b4335c6e9be97d9d` | ASS: `2e5b611a95e14a6e…` |
| `TV05` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E05.mkv` | `884,638,742` | `1446.784` | `7168a34c9920d88fc019354999167b9685cdc106e1cb7ecaa723e07703a994c1` | ASS: `740e3e1c08b95b9a…` |
| `TV06` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E06.mkv` | `910,448,052` | `1445.780` | `84abc1e3e49868adbbd6adb77f5a6bfc63fa681f055a11eaf0434517ea30679d` | ASS: `f13bdbd8c8e2de51…` |
| `TV07` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E07.mkv` | `780,050,926` | `1445.630` | `6bf41ce89db359ef18a6bc88ad0799363e96565bf7a92dd9ac584cc4620c6e46` | ASS: `67903a213ff2e890…` |
| `TV08` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E08.mkv` | `920,070,911` | `1445.670` | `a8dce7414bd1e09d1e56f2f25f088c739e2fce48b0fefc7bab5cdd7496245ce3` | ASS: `8ec6c7a6b907748c…` |
| `TV09` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E09.mkv` | `994,274,149` | `1447.110` | `ff53750e4d26305afabd06af8c752166d4289cf7d32c7d48abc2989a417bc375` | ASS: `5c2962acaa09211a…` |
| `TV10` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E10.mkv` | `1,028,296,171` | `1447.400` | `78d4c66f73ccb1d51dd24a2058bf42d8005dab8d207ba634b5b65e66ecd0c8b4` | ASS: `631304ff21efeec3…` |
| `TV11` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E11.mkv` | `914,083,229` | `1445.780` | `7b279ba1efb60a9d63cf43f88940a1e0c31d49cf77f6d4076af72bc002d996df` | ASS: `9c394734966462d1…` |
| `TV12` | `urn:rs-av-r2:primary-media:Shoujo Kageki Revue Starlight - S01E12.mkv` | `895,844,595` | `1430.805` | `887501ca140a02c40da82faebd09ee9795d2de9e9dfb0864af8da1ef23261b85` | ASS: `6e25d70372949508…` |
| `OVA01` | `urn:rs-av-r2:primary-media:ep01.analysis-softsub.mkv` | `150,123,066` | `419.420` | `14bcfd93131d1cfeea41b52c3370ca877e48cfbe69e4fae8434f1e7d48d8c6c1` | None (`0%` JP subs) |
| `OVA02` | `urn:rs-av-r2:primary-media:ep02.analysis-softsub.mkv` | `191,076,179` | `428.430` | `04b35dd4b04f6932eece9d5292d2973612c7157989268ed92feb2162f8c6e1bc` | None (`0%` JP subs) |
| `OVA03` | `urn:rs-av-r2:primary-media:ep03.analysis-softsub.mkv` | `237,179,855` | `433.435` | `c2152663a82472b0a618c5ca09f7e826b82706d5a07647253c221603ff70a38f` | None (`0%` JP subs) |
| `MOVIE` | `urn:rs-av-r2:primary-media:[Veggie_Sub]_Shoujo☆Kageki_Revue_Starlight_Movie.analysis-softsub.mkv` | `1,479,553,837` | `7222.235` | `dd3c3858effe78bfdc4f67b588ec23f274460a33fc3968c8c83a745e71a41099` | ASS: `5992b2b769783b55…`<br>5.1 MKV: `8674bf5ec2192fe0…` |

---

## 3. Complete SHA-256 Digest Table of Frozen Independent Artifacts (`27` Files)

| Relative Artifact Path | Size (Bytes) | SHA-256 Digest |
| :--- | ---: | :--- |
| `00_inventory/RS_AV_R2_SOURCE_AND_EXECUTION_INVENTORY.md` | `20,820` | `b5b8ddc6af1cb1c8423395b6db2e6f544ada9e3abda37aa60525d3aa3af86970` |
| `00_inventory/RS_AV_R2_SOURCE_INVENTORY_DATA.json` | `215,733` | `91bb3ec5e639e7c1354ba6b554d9f14e96210f95f2e783197fb26c7d2b635912` |
| `01_tv_episodes/RS_AV_R2_TV01_DEEP_READING.md` | `54,820` | `4943af4a7becb1fe55c6b742ba32b90a99d1aebd236f47d7b0d47d547c56e36e` |
| `01_tv_episodes/RS_AV_R2_TV02_DEEP_READING.md` | `54,126` | `a1257bd046996dab464c92b539c94b366a1c98a45a3f0c7ba9d57d161164ca16` |
| `01_tv_episodes/RS_AV_R2_TV03_DEEP_READING.md` | `49,099` | `9f1a1a1d6b29a34ddec3dca324745fde7f1d8857f380935c642137517f6dc609` |
| `01_tv_episodes/RS_AV_R2_TV04_DEEP_READING.md` | `50,388` | `9d13564d0d6882c749ab15e84f6f0e5c3175a283862c21bebfc38f6152118172` |
| `01_tv_episodes/RS_AV_R2_TV05_DEEP_READING.md` | `47,808` | `34bc306cebf40d1bcf02792d029d4f17bf5ddc91116d88aa91f6db22cb61756a` |
| `01_tv_episodes/RS_AV_R2_TV06_DEEP_READING.md` | `46,281` | `047c93d3f89d7506684850f4532953445ba5c1d1a734efc6e4827ac020bb1342` |
| `01_tv_episodes/RS_AV_R2_TV07_DEEP_READING.md` | `47,353` | `2a8859fd02563e3c30d7b12bcf5c46680175ec023c72bcd62ab67bb6e2b6f1b1` |
| `01_tv_episodes/RS_AV_R2_TV08_DEEP_READING.md` | `43,079` | `0d196add269696623b16b286ae57cfb67d95d174f391009da3a29acfc2bd13f3` |
| `01_tv_episodes/RS_AV_R2_TV09_DEEP_READING.md` | `45,810` | `20bc0218c7c940b0437edde33bd43d249a399c0c6941789b0b1eeafe340b8b17` |
| `01_tv_episodes/RS_AV_R2_TV10_DEEP_READING.md` | `57,087` | `e6e009368d3c86727bae409b46e366f2ac07bbdca947ad52747a4d34d55e8327` |
| `01_tv_episodes/RS_AV_R2_TV11_DEEP_READING.md` | `48,058` | `f21ed8730f7634601024b4fb10bf73f8b01c72e43a568159b69396a0f5c458cd` |
| `01_tv_episodes/RS_AV_R2_TV12_DEEP_READING.md` | `54,936` | `105c26cb9a535bc721e9598a78ff02a65acf18974549a7e348e5252626d0a75d` |
| `02_tv_synthesis/RS_AV_R2_TV_ONLY_SYNTHESIS.md` | `67,048` | `a4262c89390e089fefbf62592c06802b5ee40e8321afb4cfe0d2bad5bf159f1d` |
| `03_ovas/RS_AV_R2_OVA01_READING.md` | `19,781` | `83f2646714c79d38d5b348a57a109a1c117d6dc1eba6b9a8e477a10ac1e9b6a3` |
| `03_ovas/RS_AV_R2_OVA02_READING.md` | `17,160` | `26eaa34a6a2329eb3bb7ab286b0ea6e7b30ada34b22c34e76e98c3f95ef00ab7` |
| `03_ovas/RS_AV_R2_OVA03_READING.md` | `17,478` | `67669d88d9373f4d95bbec723cbb003e3646b2e69fb9e13253741bc23821f5a2` |
| `03_ovas/RS_AV_R2_OVA_TO_TV_SUPPLEMENT.md` | `8,971` | `51d60de9d1d321911fb8183c77b032d9f6093bd4601b2400b08a322943606898` |
| `04_movie/RS_AV_R2_MOVIE_MONOGRAPH.md` | `74,948` | `2e36cc38ea487b035406cad200e49e3d36e90fa0269546a15c3a356d73f24506` |
| `05_full_synthesis/RS_AV_R2_FULL_ANIMATED_CORPUS_SYNTHESIS.md` | `54,918` | `5fb0fcc201f186a3184d87b31518203d26b761a8f3095d4ceec4a35542aaa3c9` |
| `06_ledgers/RS_AV_R2_CHARACTER_STATES_AND_KNOWLEDGE_LEDGER.md` | `73,394` | `2d90ebabd148022cd968370349f4d77bb36ed48c4942ca0fbb51e5bc6ebe1b1a` |
| `06_ledgers/RS_AV_R2_DIRECTED_RELATIONSHIPS_LEDGER.md` | `49,931` | `4e6420ed95d7de4e72e697b4320e4b96358b370d1ba44471e61b5f18d539131a` |
| `06_ledgers/RS_AV_R2_JAPANESE_SPEECH_AND_VOCAL_LEDGER.md` | `57,808` | `77d6c872d5af4d68b8c26189b1e33f229ee18d0c698b6828d6870e8ab445ae21` |
| `06_ledgers/RS_AV_R2_MAJOR_CLAIM_AND_REVISION_REGISTER.md` | `106,857` | `f038dbf5bbb3f020a6fff324ced0418f20f1898e122f5a2067babf024cd6db53` |
| `06_ledgers/RS_AV_R2_MUSICAL_DRAMATURGY_LEDGER.md` | `48,544` | `7c1b5cf24d413d0b60ae9acced1fb81c39e0f10a808610045a008ef8fd96fabc` |
| `06_ledgers/RS_AV_R2_VISUAL_AND_THEATRICAL_FORM_LEDGER.md` | `50,476` | `ad2984c7f6a4a1ace89d16761dcc72578bd782a8ed94295c57402aa8d170680e` |

**JSON Machine Manifest (`07_freeze/RS_AV_R2_IMMUTABLE_FREEZE_MANIFEST.json`) SHA-256**: `268ba49b85d782924a773513abb885e5a44de336c1cb8a36f2783eb858ffbfaa`

---

## 4. Frozen Independent Claim, Revision, & Open-Question Index

- **Major Analytical Claims (`35`)**: `RS-AV-R2-GEMINI-CARBON-CLM-0001` through `RS-AV-R2-GEMINI-CARBON-CLM-0035` (complete 6-part counterinterpretation records locked in `06_ledgers/RS_AV_R2_MAJOR_CLAIM_AND_REVISION_REGISTER.md`).
- **Retrospective Horizon Revisions (`32`)**: `[REV-MOV-01]`, `[REV-MOV-02]`, `[REV-MOV-03]`, `[REV-MOV-04]`, `[REV-OVA01-01]`, `[REV-OVA02-01]`, `[REV-OVA03-01]`, `[REV-TV02-01]`, `[REV-TV02-02]`, `[REV-TV03-01]`, `[REV-TV03-02]`, `[REV-TV04-01]`, `[REV-TV04-02]`, `[REV-TV05-01]`, `[REV-TV05-02]`, `[REV-TV06-01]`, `[REV-TV06-02]`, `[REV-TV07-01]`, `[REV-TV07-02]`, `[REV-TV08-01]`, `[REV-TV08-02]`, `[REV-TV09-01]`, `[REV-TV09-02]`, `[REV-TV10-01]`, `[REV-TV10-02]`, `[REV-TV10-03]`, `[REV-TV11-01]`, `[REV-TV11-02]`, `[REV-TV11-03]`, `[REV-TV12-01]`, `[REV-TV12-02]`, `[REV-TV12-03]`.
- **Tracked/Resolved Open Questions (`23`)**: `[OPEN-MOV-01]`, `[OPEN-OVA03-01]`, `[OPEN-TV01-01]`, `[OPEN-TV01-02]`, `[OPEN-TV01-03]`, `[OPEN-TV01-04]`, `[OPEN-TV01-05]`, `[OPEN-TV03-01]`, `[OPEN-TV04-01]`, `[OPEN-TV05-01]`, `[OPEN-TV05-02]`, `[OPEN-TV06-02]`, `[OPEN-TV06-03]`, `[OPEN-TV07-01]`, `[OPEN-TV07-02]`, `[OPEN-TV07-03]`, `[OPEN-TV08-01]`, `[OPEN-TV08-02]`, `[OPEN-TV09-01]`, `[OPEN-TV09-02]`, `[OPEN-TV10-01]`, `[OPEN-TV11-01]`, `[OPEN-TV12-01]` (with `[OPEN-MOV-01]` preserved as end-of-corpus ontological boundary).

---

## 5. Sequential Checkpoint Git Commit Chain (`CP00` → `CP15_MOVIE_FREEZE`)

| Commit SHA | Timestamp | Checkpoint Subject |
| :--- | :--- | :--- |
| `5ef61997ec88c7e5e256640158414d63f51be363` | `2026-11-12 20:45:07 -0500` | CP00: Technical source & execution inventory, multimodal calibration, and initialized ledgers |
| `d0365cb46c4e4e0fb530b374d6afb1eeba4838b6` | `2026-11-12 21:04:30 -0500` | CP01: Freeze TV01 independent reading, cumulative ledgers, and checkpoint manifest |
| `054e51ad817233e6926aeff69fc260ad6cab32ef` | `2026-11-12 21:26:53 -0500` | CP02: Freeze TV02 independent reading, cumulative ledgers, and checkpoint manifest |
| `bb4a0bc3c811a316feade9100f39dd838229cd6e` | `2026-11-12 21:53:03 -0500` | CP03: Freeze TV03 independent reading, cumulative ledgers, and checkpoint manifest |
| `4ad2fdf2f11cd44164bffdde47894c5ff4353f96` | `2026-11-12 22:21:56 -0500` | CP04: Freeze TV04 independent reading, cumulative ledgers, and checkpoint manifest |
| `633f952311349f49d6212fcdf54ca33ed9ccf6cc` | `2026-11-12 22:44:13 -0500` | CP05: Freeze TV05 independent reading, cumulative ledgers, and checkpoint manifest |
| `2edbaedcd6c6e205c0a4c4edbd42addbfdab0dac` | `2026-11-12 23:01:57 -0500` | CP06: Freeze TV06 independent reading, cumulative ledgers, and checkpoint manifest |
| `a22db1a9dfde814c1a7774c5c2060900a08ee4c5` | `2026-11-12 23:19:54 -0500` | CP07: Freeze TV07 independent reading, cumulative ledgers, and checkpoint manifest |
| `53a29a79312d7d5648a5d7c4cc07572ac5a26103` | `2026-11-12 23:40:21 -0500` | CP08: Freeze TV08 independent reading, cumulative ledgers, and checkpoint manifest |
| `43deb0e1beb8ea17f3562406e2ee352f911c8438` | `2026-11-13 00:03:42 -0500` | CP09: Freeze TV09 independent reading, cumulative ledgers, and checkpoint manifest |
| `8a4a3fa48818ab27bcfa8df98591f056788d8312` | `2026-11-13 00:27:14 -0500` | CP10: Freeze TV10 independent reading, cumulative ledgers, and checkpoint manifest |
| `bc67aab046a294770235783b41c98c57611b929a` | `2026-11-13 00:52:45 -0500` | CP11: Freeze TV11 independent reading, cumulative ledgers, and checkpoint manifest |
| `409ad975cf821cb716b2c0e3df0ce1bd3a895d4b` | `2026-11-13 01:16:11 -0500` | CP12: Freeze TV12 independent reading, cumulative ledgers, and checkpoint manifest |
| `c0e0559c72ab13f7ce87b3d381d4b4fcf1150e91` | `2026-11-13 11:30:50 -0500` | CP13_TV_SYNTHESIS_FREEZE: Freeze TV_SYNTHESIS independent reading, cumulative ledgers, and checkpoint manifest |
| `849d4b0c2b253324854d0a8558660d072d8be605` | `2026-11-13 11:52:31 -0500` | CP14_OVA_FREEZE: Freeze OVA01_OVA03 independent reading, cumulative ledgers, and checkpoint manifest |
| `279a3737e1cded918616908e3da28e2edd86a44a` | `2026-11-13 12:57:47 -0500` | CP15_MOVIE_FREEZE: Freeze 2021 Sequel Film monograph and update 6 cumulative ledgers to MOVIE horizon (existing_corpus_exposure=false) |
