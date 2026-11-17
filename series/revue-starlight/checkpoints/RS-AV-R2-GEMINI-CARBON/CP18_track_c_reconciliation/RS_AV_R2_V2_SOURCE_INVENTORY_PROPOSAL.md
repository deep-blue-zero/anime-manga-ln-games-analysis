---
title: "RS-AV-R2-GEMINI-CARBON — Track C Source Inventory Update Proposal (Canonical V2 Candidate for SOURCE_INVENTORY.md)"
generation: "RS-AV-R2-GEMINI-CARBON"
artifact_type: "source_inventory"
project: "series/revue-starlight"
execution_identity: "RS-AV-R2-GEMINI-CARBON"
model: "Gemini 4 Carbon (High reasoning)"
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
existing_corpus_exposure: true
target_v1_file: "series/revue-starlight/01 Source Lock and Inventory/SOURCE_INVENTORY.md"
target_v1_sha256: "ea1041a6ff02eb1b74230bdda10c676f70c79b2aade1af564641194158f5ed3d"
pinned_r2_freeze_commit: "224c52786b9b5a1d5edd6ce203bfb0714305627e"
pinned_r2_comparative_audit_commit: "724f8fb0fd79705fa3f1c558851d29b12dd2de1a"
document_role: "v2_source_inventory_proposal"
---

# Proposed `V2` Updates to `01 Source Lock and Inventory/SOURCE_INVENTORY.md`

## 1. Summary of Material Deltas Against `V1` `SOURCE_INVENTORY.md` (`L1–119`)

| `V1` Section & Lines | `V1` Baseline State (`2026-08-10`) | Proposed `V2` Update | Evidentiary Basis |
| :--- | :--- | :--- | :--- |
| **YAML Front Matter (`L1–6`)** | Untyped legacy front matter (`title`, `version: "1.0"`, `date`, `status: "Source lock for the definitive synthesis"`). | Upgrade upon owner merge to repository-compliant canonical authority front matter (`status: canonical`, `supersedes: ["series/revue-starlight/90 Archive/V1_2026-08-10/01 Source Lock and Inventory/SOURCE_INVENTORY.md"]`, `superseded_by: []`, `do_not_use_as_current_authority: false`). | `ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md` |
| **`# I. Governing source boundary` (`L11–31`)** | Correctly locks `TV01`–`12`, `OVA01`–`03`, and the `2021` sequel film (excluding *Rondo Rondo Rondo*, `-Re LIVE-`, stage plays, manga, interviews) without listing container durations or cryptographic SHA-256 digests. | Retain (`PRESERVE`) every scope exclusion verbatim; **add (`STRENGTHEN`)** exact container durations (`25,842.313s` total across `16` units) and SHA-256 locks for all `16` primary Japanese Matroska video witnesses and `13` Japanese `.ass` witnesses (sanitized of workstation drive paths). | `ffprobe` + SHA-256 verification across all `16` units |
| **`# II.1 Television series` (`L35–45`)** | Lists softsub/hardsub MKV, Japanese analysis `.ass`, extracted `.ass`, audio, screenshots, contact sheets, and `manifest.json` without stream specs, commentary-track warning, or `.ass` drift notes. | Specify `1920x1080` `23.976 fps` HEVC Main 10 video + primary `48 kHz` lossless stereo `FLAC` (`#0:1`), flag secondary `Seyuu Commentary` AAC tracks on **`TV01`, `TV05`, and `TV10`** (which must be excluded during analysis), clarify broadcast SDH `.ass` markup (`<...>` = off-lips interior monologue vs. bare = aloud speech vs. `・～` = song), and log verified `.ass` discrepancies (`TV03` `より高く`, `TV10` `+58.30s` commercial-break drift + uncaptioned `65s` French, `TV12` `君は`). | `S01E01`–`S01E12.mkv` + `s01e01`–`s01e12.analysis.ass` |
| **`# II.2 OVAs` (`L47–56`)** | Correctly warns that `OVA01`–`03` carry English subtitles (`Ripple`) without a Japanese subtitle track, and restricts OVA use to visual/musical/coarse context. | Retain (`PRESERVE`) zero-reliance on English fan subtitles; **upgrade (`REVISE` / `STRENGTHEN`)** with direct Japanese `48 kHz` `24-bit` lossless `FLAC` (`#0:1`) listening protocol (`-sn` extraction; phonetic uncertainty bracketed `[聴取不確定]`) + `1920x1080` Japanese onscreen signage lock (`聖翔祭 2019 採寸`, `聖翔祭まで 50日`, `聖翔祭まで 29日`, `右 160 km/h / 99.419 mi/h`), separating direct signage facts from `[INFERRED]` early-March calendar placement. | `ep01`–`ep03.analysis-softsub.mkv` (`#0:0` HEVC + `#0:1` `24-bit` FLAC) |
| **`# II.3 Sequel film` (`L58–70`)** | Lists softsub/hardsub MKV, Japanese `.ass` (`1,722` cues), full `160k` MP3 audio, and `3,449` screenshots without recording the upstream discrete `5.1` surround stream or community `.ass` provenance. | Retain (`PRESERVE`) sequel identity (`~120.4 min`, `7,222.235s`, distinct from *Rondo Rondo Rondo*) and inclusion of ending credits + post-credit audition; **revise (`REVISE`)** audio specification to record **both** upstream Japanese **`635 kbps` `6`-channel `5.1 AAC` (`0:a:1`, `[FL, FR, FC, LFE, BL, BR]`)** and derivative `160 kbps` stereo `AAC 2.0` (`0:a:0`), document `movie.analysis.ass` cue `[1691]` provenance (*"jp transcribed by 1computer on discord (very low on sleep)"*) + verified stenographic typos (`次の駅へ`, `うちら`, `私にだって`, `ステージは続く`), and enforce strict separation between verified stream/credit facts and mix-based interpretive inferences. | Upstream Movie MKV (`0:a:1` `5.1 AAC`) + `movie.analysis.ass` + `1080p` credits |
| **`# III–# IV` (`L72–119`)** | Defines Tier 1–3 source hierarchy and prohibits redistributing copyrighted media. | Retain (`PRESERVE`) non-redistribution rule and Tier 1–3 hierarchy; add **Inspection-Lane Provenance (`CONTINUOUS_AV` + `BUNDLE_MEDIATED` reconciliation)** and **Prior-Knowledge Quarantine Disclosure**. | `MANGA_ANIME_MEDIUM_AND_INSPECTION_LANE_ROUTING_POLICY.md` |

---

## 2. Complete Proposed Publication-Ready `V2` Text for `01 Source Lock and Inventory/SOURCE_INVENTORY.md`

*(Note: All local filesystem paths are sanitized to repository-safe basenames and logical stream identifiers so this text can be dropped directly into `series/revue-starlight/01 Source Lock and Inventory/SOURCE_INVENTORY.md` upon owner approval of Track C, switching `status` from `draft_noncurrent` to `canonical`.)*

```markdown
---
title: "少女☆歌劇 レヴュースタァライト — Canonical V2 Source Lock, Stream Witness Ledger, and Epistemic Hierarchy"
version: "2.0"
status: canonical
supersedes:
  - "series/revue-starlight/90 Archive/V1_2026-08-10/01 Source Lock and Inventory/SOURCE_INVENTORY.md"
superseded_by: []
do_not_use_as_current_authority: false
---

# 『少女☆歌劇 レヴュースタァライト』
## Canonical `V2` Source Lock and Witness Inventory

# I. Governing source boundary

This project synthesizes the **animated *Revue Starlight* corpus** only (`16` source units totaling `25,842.313` seconds / `07:10:42.313`):

1. **Television series:** *Shōjo☆Kageki Revue Starlight* (`少女☆歌劇 レヴュースタァライト`, 2018), Episodes `1–12` (`TV01`–`TV12`, `17,338.793s`).
2. **OVAs:** `#1 99.419 Measuring (採寸)`, `#2 99.419 Discussion (討論)`, and `#3 99.419 Opening (開演)` (`OVA01`–`OVA03`, `1,281.285s`), bridging the rehearsal countdown to the `100th` Seishō Festival.
3. **Sequel film:** *Gekijōban Shōjo☆Kageki Revue Starlight* (`劇場版 少女☆歌劇 レヴュースタァライト`, 2021, `7,222.235s` / `02:00:22.235`), **through its complete narrative epilogue** (ending-credit sequence `私たちはもう舞台の上` and post-credit audition scene `本日、今 この時`).

## Explicit exclusions & deferred artifacts

The following remain **outside** the governing evidentiary boundary:

- the 2020 compilation film *Rondo Rondo Rondo* (`ロンド・ロンド・ロンド`);
- *Revue Starlight -Re LIVE-* mobile-game stories, schools, and character expansions;
- stage musicals (`舞台`), live concerts, and radio/variety programs;
- manga and light-novel adaptations;
- external wikis, fan summaries, guidebooks, or creator interviews not embedded in the primary animated media.

In accordance with `00 Frameworks/RevueStarlight_Anime_Character_Reconstruction_Spec_v1.md` and `CHARACTER_RECONSTRUCTION_EVALUATION_AND_RATING_METHOD.md`, standalone character-reconstruction persona models and capability-tier ratings are **deferred** and excluded from this analytical synthesis.

---

# II. Cryptographic witness lock (`16` primary Japanese media units)

All timestamps across `V2` use presentation timestamps (`HH:MM:SS` or `MM:SS.s`) locked to the primary `23.976 fps` (`24000/1001`) `1920x1080` progressive video streams below. Copyrighted media, audio, extracted stills, and bulk subtitle files are **never committed or redistributed**.

| Unit | Canonical Basename | Duration (`s`) | Primary Video Stream | Authoritative Japanese Audio Stream | Primary Container `SHA-256` | Japanese `.ass` `SHA-256` (`analysis_ass`) |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| `TV01` | `Shoujo Kageki Revue Starlight - S01E01.mkv` | `1446.784` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` *(exclude `#0:2` commentary)* | `a6a97c09edc8e69c1d283822afff560a50609775893e3e429e7d310c01852250` | `ad9e2f244ca43ca3e76ef904970fc36ee3bf9a49c00694b4f078f82bc7580960` |
| `TV02` | `Shoujo Kageki Revue Starlight - S01E02.mkv` | `1446.780` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` | `f82f702475617ee498c0de7c2d061d9c68d13be7022c14b5b67ed2cbeb4a4c13` | `d18077842abbd3cc333a9c5fc70492bc200697a89a67eb018e2aa4dc24c8b1bb` |
| `TV03` | `Shoujo Kageki Revue Starlight - S01E03.mkv` | `1446.780` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` | `8622f8799f776a322871e303eb9340928496c1f1a06cc7742bf9a5b699e08340` | `46f0e93e069546722f9217d604b8e6022f3193207e7b31a588e6ff96b672971f` |
| `TV04` | `Shoujo Kageki Revue Starlight - S01E04.mkv` | `1446.780` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` | `60bc88c99672276a9f6545861b41e7f93f4b5046372e1174880222749017bf6e` | `c8502e3a60e7be8958f1a8dc2a8a5b5848ec2c8cc46e68a22f3c4bd31a6dfef3` |
| `TV05` | `Shoujo Kageki Revue Starlight - S01E05.mkv` | `1446.784` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` *(exclude `#0:2` commentary)* | `7168a34c9920d88fc019354999167b9685cdc106e1cb7ecaa723e07703a994c1` | `740e3e1c08b95b9a56c6a2ee7be9acdacdbc8144c467006145b89f946b23eb35` |
| `TV06` | `Shoujo Kageki Revue Starlight - S01E06.mkv` | `1446.780` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` | `ab29bf014d7c12a1776a96fd82c2604c81e115165bb6b53bb0a13a7290986d5f` | `4c992f64c23688894c8a0f60890cf76a6133ebbd38f48c0a8b873ce1f9737803` |
| `TV07` | `Shoujo Kageki Revue Starlight - S01E07.mkv` | `1446.780` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` | `3a8a0a16b0267f079eb7d9f81fb38f3478bc5a93e23cc72e4797d11229a8e6f4` | `c50966cc0142a16d2a493c97748b118ff40ef374b0030be3fd0a8e62fd4a188b` |
| `TV08` | `Shoujo Kageki Revue Starlight - S01E08.mkv` | `1446.780` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` | `7370f748f500877fc7c90e680f376a325cb0dc56137b1025cd0468740773b479` | `b7eb104ffef69516ffea43b2c68e4d82cb76bc7dc1242fbdf8362a64c5617ee8` |
| `TV09` | `Shoujo Kageki Revue Starlight - S01E09.mkv` | `1446.780` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` | `64c436270e819937e5a8d1a854bf36207806a5c7333cd783b5efdd865ab6925c` | `e38d0d6502cd09dc5219d2b24e3341bc0a591a2e2c844267c10bc5b03e0b8c59` |
| `TV10` | `Shoujo Kageki Revue Starlight - S01E10.mkv` | `1446.784` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` *(exclude `#0:2` commentary)* | `d8167c22246a64c1e43ff1b7ca031b467d5742c39d62fb2581d6975ff3b8685c` | `6c7ec81f5369325bc021dfbc564ebdfca303a28133758359624ebec9784323f5` |
| `TV11` | `Shoujo Kageki Revue Starlight - S01E11.mkv` | `1446.780` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` | `20cd2db81fd8d1cd0a871b24a8414502cf42be14b4a7a7be5ca5821f66be1b8d` | `86220a0d0df0298c18b35e7bece0c30ff7e29a7ee6833c7ef96ee4cb291f885a` |
| `TV12` | `Shoujo Kageki Revue Starlight - S01E12.mkv` | `1424.201` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `FLAC 2.0` | `9ef861a815cb85fa8c682328533ca435d2b311f90f45916b98fcdf4c9907d478` | `6e97d318d97c469bc577586bf6615f1aa1e2a98fc9bd74ab4de1e3c4601b2fd7` |
| `OVA01` | `ep01.analysis-softsub.mkv` | `419.420` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `24-bit` `FLAC 2.0` | `14bcfd93131d1cfeea41b52c3370ca877e48cfbe69e4fae8434f1e7d48d8c6c1` | `NONE` *(English `#0:2` excluded)* |
| `OVA02` | `ep02.analysis-softsub.mkv` | `428.430` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `24-bit` `FLAC 2.0` | `04b35dd4b04f6932eece9d5292d2973612c7157989268ed92feb2162f8c6e1bc` | `NONE` *(English `#0:2` excluded)* |
| `OVA03` | `ep03.analysis-softsub.mkv` | `433.435` | `1920x1080` HEVC `23.976 fps` | `#0:1` `48 kHz` `24-bit` `FLAC 2.0` | `c2152663a82472b0a618c5ca09f7e826b82706d5a07647253c221603ff70a38f` | `NONE` *(English `#0:2` excluded)* |
| `MOVIE` | `[Veggie Sub] Shoujo☆Kageki Revue Starlight Movie.mkv` *(+ `movie.analysis-softsub.mkv`)* | `7222.235` | `1920x1080` H.264 `23.976 fps` *(active `1920x804` `2.388:1` Scope)* | Upstream `0:a:1` **`48 kHz` `635 kbps` `5.1 AAC`** `[FL,FR,FC,LFE,BL,BR]` *(+ `0:a:0` `160k` `AAC 2.0`)* | `7b5be2c4a9c6d6b08c6f338411f21a09bc813c5bf3ebca51ee6fbde1995fd38c` *(softsub: `e2ec8fc83fd625ba2f13c7d14d628c1660ba6e588475a6f3d0b516917056586e`)* | `0df8e5e68b4cb7b8d47b4713a0e4a0cd19752f2db381e7f93a81fcbe12a10191` |

---

# III. Corpus-specific witness caveats & verification protocols

## 1. Television series (`TV01`–`TV12`): Broadcast SDH `.ass` conventions & verified drift

1. **Cast Commentary Exclusion (`TV01`, `TV05`, `TV10`)**: Upstream containers for Episodes `1`, `5`, and `10` include a secondary Japanese stereo AAC track (`#0:2`, `Seyuu Commentary`). All narrative and acoustic analysis binds strictly to the primary lossless `FLAC 2.0` mix (`#0:1`) and excludes cast commentary paratext.
2. **Broadcast SDH Markup Distinction (`<...>` vs. `・～`)**: The `s01e01`–`s01e12.analysis.ass` files derive from Japanese broadcast closed captions:
   - Half-width angle brackets **`<...>`** mark **off-lips spoken interior monologue (`心の声`)** (e.g., `TV05` `21:40–22:28` Mahiru's `<大切な人達を 幸せにしたいと思えば> <何度でも キラめける>` at `21:57.06–22:03.40`, where Mahiru's lips remain closed onscreen);
   - Unbracketed lines mark **diegetic aloud speech** (e.g., `TV05` `22:05.23` `あっ… おいしい`);
   - **`・～`** marks **sung musical passages** (often leaving insert-song and `Fly Me to the Star` ED lyrics uncaptioned in the `.ass` stream, requiring direct lossless-FLAC transcription).
3. **Verified `.ass` Transcription & Timing Discrepancies**:
   - **`TV03` (`18:36`)**: Sung lyric in `誇りと驕り` is **`より高く`** (verified against `FLAC`), where `.ass` omits insert-song text.
   - **`TV10` (`s01e10.analysis.ass` lines `291–302`)**: Exhibits a **`+58.30s` timestamp drift** across a broadcast commercial-break seam and leaves `65` seconds of Claudine's French dialogue (`07:12–08:17`) and Maya's spoken `"Ma Claudine"` (`20:24`) uncaptioned; primary container presentation timestamps and `FLAC` audio govern.
   - **`TV12` (`s01e12.analysis.ass` line `256`, `20:37.7`)**: Captions `星は` where Koyama Momoyo & Mimori Suzuko audibly sing **`君は`**; sung audio governs.

## 2. OVAs (`OVA01`–`OVA03`): Zero-Japanese-subtitle protocol & `[INFERRED]` date rule

1. **English Subtitle Exclusion**: Neither upstream nor `analysis-softsub` OVA containers contain a Japanese subtitle track (track `#0:2` is an English `[Ripple]` localization). English subtitles are **never** used as evidence of Japanese wording; all segments and stills are inspected with `-sn`.
2. **Direct Japanese `FLAC` + `1080p` Signage Verification**: Spoken Japanese quotes in `OVA01`–`OVA03` are transcribed directly from `#0:1` (`48 kHz` `24-bit` lossless Japanese `FLAC`), bracketing any phonetically rapid syllable not verifiable at `100%` confidence as `[聴取不確定]`.
3. **Signage Fact vs. Calendar Inference**:
   - Direct `1920x1080` onscreen Japanese signage establishes: **`聖翔祭 2019 採寸`** (`OVA01` `01:20.5`), **`聖翔祭まで 50日`** (`OVA01` `00:09.5`), **`聖翔祭まで 29日`** (`OVA02` `00:31.5`), Opening Day curtain splice (`OVA03` `06:57–07:03` → `TV12` `22:00`), and **`右 160 km/h / 99.419 mi/h`** (`OVA03` `00:16.5` at `荻窪バッティングセンター`).
   - Because no direct `3月X日` date appears onscreen in `OVA01`–`OVA03`, placing the `100th` Seishō Festival in **early March 2019** (and `OVA01`/`OVA02` in mid-January / early February 2019) is labeled **`[INFERRED]`** (from `聖翔祭 2019` + `TV07`'s `2018.3.3` `99th` Festival precedent + `OVA02` snow → `OVA03` plum blossoms), while the exact day in March 2019 remains **`[OPEN]`**.

## 3. Sequel film (`2021`): `5.1` surround stream, onscreen credits, mix discipline, & `.ass` provenance

1. **Dual Audio Witnesses (`5.1 AAC` Primary vs. `2.0 AAC` Derivative)**: Upstream `[Veggie Sub] Shoujo☆Kageki Revue Starlight Movie.mkv` preserves the theatrical **`6`-channel Japanese `5.1` surround stream (`0:a:1`, `48 kHz`, `635 kbps` `AAC`, `[FL, FR, FC, LFE, BL, BR]`)**, whereas pipeline `movie.analysis-softsub.mkv` (`0:a:0`) and extracted MP3s provide a `160 kbps` stereo downmix.
2. **Strict Separation of Stream/Credit Facts from Mix Interpretation**:
   - **Primary Facts (`[AV-FACT]` / `[MUS-FACT]`)**: Stream configuration (`0:a:1` `5.1`), descriptive channel dBFS levels, active `1920x804` (`2.388:1`) CinemaScope framing, and `1920x1080` end-roll typography (`01:58:46–01:59:05`)—specifically **`前奏作曲：本多友紀 (Arte Refact)`** + **`作曲・編曲：佐藤純一 (fhána)`** on `私たちはもう舞台の上`, and unified **`作曲・編曲：加藤達也`** across all ~8 minutes of `スーパー スタァ スペクタクル` (`01:48:27–01:56:15`)—are verified primary source facts.
   - **Mix-Derived Interpretations (`[INTERPRETATION]`)**: Ontological conclusions drawn from `FC` dialogue isolation (`FC − LR = +13.72 dB` in campus scenes; `+25.10 dB` in `本日、今 この時`) or `LFE` silence (`-96.00 dBFS`) during `私たちはもう舞台の上` (`01:57:06–01:59:50`) are **subordinate interpretive inferences** that must explicitly weigh standard cinema post-production conventions (`FC`-routed interior dialogue and `2.0`-mastered J-pop credit tracks placed into `5.1` stems without dedicated `.1` LFE content).
3. **Community `.ass` Provenance & Verified Typos**: `movie.analysis.ass` (`1,722` cues) is an unofficial community transcription self-attributed at cue `[1691]` (`01:56:58`): *"jp transcribed by 1computer on discord (very low on sleep)"*. Every quoted line is audited against `0:a:1` Japanese audio; verified corrections include `00:25:34` (`次の駅を` → **`次の駅へ`**), `00:33:08` (`私んだって` → **`私にだって`**), `01:02:39` (`うちは` → **`うちら`**), and `01:59:36` (`Hey! The stage continues` → **`Hey！ ステージは続く どこまでも`**).

---

# IV. Governing evidentiary hierarchy & prior-knowledge disclosure

1. **Tier 1A — Native Japanese audiovisual performance (`CONTINUOUS_AV` + `1080p` unburned frames + primary `FLAC 2.0` / `5.1 AAC` audio)**: Authoritative over all derivative transcripts and summaries.
2. **Tier 1B — Verified Japanese onscreen typography & audio-checked Japanese captions/lyrics**: Authoritative for lexical and structural claims once verified against Tier 1A.
3. **Tier 2 — Quantitative acoustic/framing telemetry & navigation bundles (`BUNDLE_MEDIATED` contact sheets, RMS/channel envelopes)**: Corroborative only; subordinate to audible/visible dramatic form.
4. **Prior-Knowledge Quarantine Disclosure**: Run `RS-AV-R2-GEMINI-CARBON` disclosed pretraining familiarity with the animated series' macro-premise (including Daiba Nana's mid-series temporal-loop twist) prior to `TV01` inspection; accordingly, prospective `TV06` stinger observations (`23:48` `今回の再演`) are framed as textual foreshadowing verified under quarantined pretraining awareness rather than blind zero-knowledge prediction.
```
