---
title: "RS-AV-R2-GEMINI-CARBON — Track C Post-Freeze Handoff: Canonical V2 Reconciliation Proposal for series/revue-starlight/"
generation: "RS-AV-R2-GEMINI-CARBON"
artifact_type: "analytical_handoff"
project: "series/revue-starlight"
execution_identity: "RS-AV-R2-GEMINI-CARBON"
model: "Gemini 4 Carbon (High reasoning)"
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
existing_corpus_exposure: true
pinned_published_baseline_commit: "0bae19f328c3fdef82047e5753568fbb8478daed"
pinned_published_project_branch_commit: "ff8ebcdacc726b70c1fc30452812b1dec581bb23"
pinned_r2_freeze_commit: "224c52786b9b5a1d5edd6ce203bfb0714305627e"
pinned_r2_comparative_audit_commit: "724f8fb0fd79705fa3f1c558851d29b12dd2de1a"
document_role: "track_c_canonical_v2_reconciliation_handoff"
---

# Track C Post-Freeze Handoff: Canonical `V2` Reconciliation Proposal for `series/revue-starlight/`

> [!IMPORTANT]
> **Post-Freeze Separation, Immutability, & Scope Attestation**:
> 1. **Track Selection**: Per Section 2 ("Track C") of `08_comparative_audit/RS_AV_R2_INTEGRATOR_HANDOFF_AND_PUBLICATION_PROPOSAL.md`, this package specifies the complete **canonical `V2` reconciliation candidate** for `series/revue-starlight/` as a **separate post-freeze handoff** (`status: draft_noncurrent` until owner-merged via `governance/repository-controls/project-initiation-gate.json`).
> 2. **Byte-for-Byte Preservation of `CP16` and `CP17A`**:
>    - **`CP16_IMMUTABLE_FREEZE` (`224c52786b9b5a1d5edd6ce203bfb0714305627e`)**: All `30` pre-exposure independent files in `00_inventory/` through `07_freeze/` remain **100% byte-for-byte unchanged** (`git diff 224c52786b9b5a1d5edd6ce203bfb0714305627e HEAD -- 00_inventory 01_tv_episodes 02_tv_synthesis 03_ovas 04_movie 05_full_synthesis 06_ledgers 07_freeze` = `0` bytes).
>    - **`CP17A` (`724f8fb0fd79705fa3f1c558851d29b12dd2de1a`)**: All `3` initial comparative-audit files in `08_comparative_audit/` remain **100% byte-for-byte unchanged** (`git diff 724f8fb0fd79705fa3f1c558851d29b12dd2de1a HEAD -- 08_comparative_audit` = `0` bytes). Where targeted primary-source rechecking below refines or retracts a `CP17A` sub-claim (`TV05` `16:48–16:53` and `21:57–22:03`), that correction is issued transparently in this `10_track_c_v2_reconciliation/` package and in the companion erratum rather than silently editing `CP17A`.
>    - **Target Repository Untouched**: `anime-manga-ln-games-analysis` remains completely clean (`0` modified or untracked files).
> 3. **Strict Anime-Only Boundary & Deferred Character Modeling**:
>    - Governing corpus scope is strictly **`TV01`–`TV12`**, **`OVA01`–`OVA03`**, and the **2021 theatrical sequel (`『劇場版 少女☆歌劇 レヴュースタァライト』`) through its narrative epilogue** (ending credits `私たちはもう舞台の上` + post-credit audition `本日、今 この時`, matching `01 Source Lock and Inventory/SOURCE_INVENTORY.md` `L58–70`).
>    - Zero *Revue Starlight -Re LIVE-* mobile-game lore, stage plays, manga adaptations, external wikis, or creator interviews are admitted.
>    - Full character-reconstruction artifacts and capability-tier ratings are **explicitly deferred** (`00 Frameworks/RevueStarlight_Anime_Character_Reconstruction_Spec_v1.md` `L24–31`, `L138–166`; `CHARACTER_RECONSTRUCTION_EVALUATION_AND_RATING_METHOD.md`).

---

## 1. Package Inventory (`10_track_c_v2_reconciliation/`)

| File | Role in Track C Handoff |
| :--- | :--- |
| `RS_AV_R2_TRACK_C_V2_RECONCILIATION_HANDOFF.md` *(this file)* | Executive architecture, targeted primary-source rechecks (`TV05`, `OVA01`–`03`, `Movie` `5.1`/credits, `TV06` prior-knowledge disclosure), proposed `02`–`04` unit-reading homes, supersession governance, and retained `V1` core inventory. |
| `RS_AV_R2_V2_CLAIM_BY_CLAIM_RECONCILIATION_LEDGER.md` | Exhaustive `22`-item claim-by-claim reconciliation (`REC-01`–`REC-22`) providing exact `V1` locator, disposition, primary source witness & timestamp, counterevidence, publication-ready `V2` wording, and affected `V2` file(s) for every material change. |
| `RS_AV_R2_V2_SOURCE_INVENTORY_PROPOSAL.md` | Complete proposed `V2` replacement candidate and section-by-section delta for `series/revue-starlight/01 Source Lock and Inventory/SOURCE_INVENTORY.md`. |
| `RS_AV_R2_V1_STRUCTURAL_AND_CHECKSUM_ERRATUM.md` | Standalone structural and checksum erratum covering `V1`'s concatenation/heading defects (`Docs 04, 05, 06, 15`) and `CHECKSUM_AUDIT.md` (`L28`, `L39`) findings, alongside transparent post-freeze errata on `R2`'s untouched `CP16` and `CP17A` records. |

---

## 2. Targeted Primary-Source Rechecks & Methodological Calibrations

### 2.1 `TV05` Primary Recheck I (`16:48–16:53`): Cross-Bout Distraction vs. Within-Bout Strike

- **Pinned Primary Source Witnesses**:
  - Video + Lossless Audio: `Shoujo Kageki Revue Starlight - S01E05.mkv` (`SHA-256: 7168a34c9920d88fc019354999167b9685cdc106e1cb7ecaa723e07703a994c1`; stream `0:v:0` `1920x1080` `23.976 fps` HEVC Main 10; primary Japanese audio stream `#0:1` [mapped `0:a:0` excluding `#0:2` seiyū commentary] `48 kHz` lossless stereo `FLAC`).
  - Japanese Broadcast Caption Witness: `s01e05.analysis.ass` (`SHA-256: 740e3e1c08b95b9a56c6a2ee7be9acdacdbc8144c467006145b89f946b23eb35`, lines `L267`–`L273`).
  - Inspection Method: Synchronized unburned native AV segment (`16:35.000–17:05.000`, `-map 0:v:0 -map 0:a:0 -sn`) + `4.0 fps` timestamped frame grid (`16:47.000–16:53.750`, `28` consecutive `250 ms` frames).
- **Exact Frame-and-Audio Sequence**:
  1. **`16:38.0–16:41.0` (`[AV-FACT]`)**: High on the orange-lit gabled roof ridge of the half-timbered stage set, **Kagura Hikari** and **Saijō Claudine** are actively fighting **their own separate Day-4 Audition bout (`Claudine vs. Hikari`)** (`16:38`: blades clash `ふっ！ うっ！`; `16:40`: wide profile standoff along the roof ridge).
  2. **`16:40.86–16:45.97` (`[AV-FACT]` + `[JP-TXT]` `s01e05.analysis.ass` `[L267]–[L268]`)**: Below them on the ground floor—demarcated by a white chalk boundary line (`16:43.0`)—**Aijō Karen** and **Tsuyuzaki Mahiru** are engaged in **their separate Day-4 bout (`Karen vs. Mahiru`)**, chased by the wheeled `Mr. White` cat cart (`うわ～っ！` / `アハハ…`). Hearing Karen's cry from the neighboring bout below, **Hikari turns her head away from her opponent Claudine to look down over her left shoulder toward Karen** (`16:43.0–16:45.5`) and calls out **`「華恋！」`** (`16:45.0`, `[L268]`).
  3. **`16:45.97–16:52.14` (`[AV-FACT]` + `[JP-TXT]` `[L269]–[L270]`)**: In a two-plane low-angle shot (`16:47.000–16:48.750`), Mahiru giggles with her baton in the foreground (`あっ！ ウフフ…`) while Claudine holds combat guard against distracted Hikari on the illuminated roof behind her. At **`16:48.750–16:50.500`**, **Claudine lunges forward and strikes Hikari inside their own `Claudine vs. Hikari` bout**, explicitly rebuking Hikari for taking her eyes off her own opponent: **`「レヴューの最中に よそみなんてね」`** (`16:48.97–16:52.14`, `[L270]`). From `16:50.750–16:52.000`, medium close-up of Claudine's sword follow-through on the roof edge while Hikari (`ああっ！`) is sent flying off the dark side of the roof.
  4. **`16:52.14–16:56.14` (`[AV-FACT]` + `[JP-TXT]` `[L271]–[L272]`)**: Impact thud (`(ひかりが落ちる)`, `16:52.14–16:54.14`); at `16:54.0`, Hikari sits slumped against the lower stone tower wall in shadow, **still wearing her royal-blue Revue cloak**, as Karen below cries **`「ひかりちゃん！」`** (`16:54.14–16:56.14`, `[L272]`)—creating the opening for Mahiru's quiet cut-in (`元に戻ってよ / 神楽さんが来る前の華恋ちゃんに`, `16:58.41–17:03.71`, `[L274]–[L275]`).
- **Binding Analytical Decision for `V2` (and Correction of `CP17A`)**:
  - `CP16`'s original `TV05` reading (`01_tv_episodes/RS_AV_R2_TV05_DEEP_READING.md` `L58`, `L140`) described the event accurately, whereas `CP17A` (`08_comparative_audit/RS_AV_R2_SYMMETRIC_COMPARATIVE_CLAIM_AUDIT.md` `L52`, `L94`, `L197`) compressed it into the misleading shorthand *"cross-bout hit"* / *"Claudine's stray blow striking Hikari across bouts."*
  - **What is cross-bout**: **Only the sensory distraction** across the shared subterranean hall (`Karen vs. Mahiru` distracting Hikari into looking down at `16:45`, and Hikari's fall distracting Karen at `16:54`).
  - **What is within-bout**: **Claudine's strike on Hikari (`16:49–16:52`) is an orthodox within-bout attack inside `Claudine vs. Hikari`** punishing Hikari's lapse of attention (`よそみ`).
  - **Point Left Explicitly `[OPEN]`**: No `POSITION ZERO` marker or severed-clasp shot is ever shown onscreen for `Claudine vs. Hikari` (Hikari still wears her blue cloak when shown slumped at `16:54.0`, and the Giraffe terminates Day 4 globally at `19:54.14–20:01.21` `[L314–L315]`: `ゲームセット！ オーディション 4日目 終了します` immediately after `Karen vs. Mahiru`). Whether `Claudine vs. Hikari` formally ended by ring-out/knockdown at `16:52`, concluded offscreen between `16:55` and `19:54`, or stood unfinished at the Day-4 bell is **not resolved by the primary text and remains `[OPEN]`**.

---

### 2.2 `TV05` Primary Recheck II (`21:57–22:03` vs. `22:31`): Spoken Inner Narration vs. Credited `Fly Me to the Star`

- **Pinned Primary Source Witnesses**:
  - `Shoujo Kageki Revue Starlight - S01E05.mkv` (`SHA-256: 7168a34c9920d88fc019354999167b9685cdc106e1cb7ecaa723e07703a994c1`; Matroska `Chapter #0:3 Bパート` `768.851s–1350.891s` [`12:48.85–22:30.89`] and `Chapter #0:4 エンディング` `1350.891s–1440.856s` [`22:30.89–24:00.86`]; video `0:v:0`; audio `#0:1` `48 kHz` lossless `FLAC`).
  - `s01e05.analysis.ass` (`SHA-256: 740e3e1c08b95b9a56c6a2ee7be9acdacdbc8144c467006145b89f946b23eb35`, lines `L339`–`L360`).
  - Inspection Method: Synchronized native AV segment (`21:10.000–22:45.000`, `-map 0:v:0 -map 0:a:0 -sn`) + `2.0 fps` frame grids (`21:55.000–22:09.500` and `22:25.000–22:39.500`) + `0.4 fps` ED credit grid (`22:40.0–23:55.0`).
- **Definitive Classification of `21:57.06–22:03.40` (`<大切な人達を 幸せにしたいと思えば> <何度でも キラめける>`)**:
  - **Result**: Mahiru's line at `21:57.06–22:03.40` is **spoken (non-sung) inner narration / interior monologue (`モノローグ` / `心の声`)**, **NOT** diegetic aloud speech and **NOT** song.
  - **Convergent Three-Modal Proof**:
    1. **Visual Lip-Sync Proof (`[AV-FACT]`)**: From `21:56.5` to `22:00.0`, the camera shows a POV close-up of Mahiru's hands holding the foil-wrapped buttered `まひるいも` (`<大切な人達を 幸せにしたいと思えば>`, `21:57.06–22:00.90`). At `22:00.5–22:03.4` (`<何度でも キラめける>`, `22:00.90–22:03.40`), the camera cuts to a medium front shot of Mahiru: **her mouth stays completely closed in a serene smile (`口パクなし`)** throughout the entire clause. By immediate contrast, after she bites and chews the potato (`22:03.0–22:04.5`), **her lips visibly part and move at `22:05.23–22:07.23`** when she speaks aloud **`「あっ… おいしい」`** (`[L354]`), prompting Karen's audible reply **`「だよね！」`** (`22:07.24`, `[L355]`), before Mahiru reverts to closed-mouth interior monologue (`<やっぱり… 大好き>` … `<私は…>`, `22:10.74–22:28.32`, `[L356]–[L359]`).
    2. **Vocal & Musical Proof (`[AV-FACT]` / `[MUS-FACT]`)**: Iwata Haruki delivers `大切な人達を幸せにしたいと思えば、何度でもキラめける` in intimate, unpitched **spoken prose prosody** (no sung pitch contour, no metrical beat), floating over gentle non-vocal piano-and-strings underscore (`劇伴`) that began under her junior-high broadcast clip (`21:14.42–21:23.82`, `[L339]–[L341]`: `大切な… 大切な人達を笑顔にできるような、温かいスタァになりたいです`).
    3. **Broadcast SDH `.ass` Markup Proof (`[JP-TXT]`)**: In Japanese TV broadcast closed-caption `.ass` files (`s01e05.analysis.ass`), half-width angle brackets **`<...>`** denote **off-lips interior monologue (`心の声`)** (`[L347]–[L353]` and `[L356]–[L359]`), bare text denotes **diegetic aloud speech** (`[L354]` `あっ… おいしい`, `[L355]` `だよね！`), and **`・～`** denotes **sung/musical performance** (`[L360]`).
- **Exact Locator of the Credited `Fly Me to the Star` Sequence**:
  - Matroska `Chapter #0:4` (`エンディング`) opens at **`22:30.891`**; the visual cut to white-ground ED animation (`めばち` illustration of Mahiru with closed eyes) occurs at **`22:31.000`**; the upbeat bossa-pop nylon-guitar/percussion intro (`Stem II`) begins at **`22:31.26`** (`s01e05.analysis.ass` `[L360]` `0:22:31.26 -> 0:23:37.86 | ・～`); Mahiru's **sung vocal** enters at **`22:38.50`** (`♪ 私 ずっと あなたを 見てた…`) alongside the `キャスト` credit block; and the onscreen song credit card appears at **`23:32.5–23:36.0`**: **`エンディングテーマ 「Fly Me to the Star」 / 露崎まひる (CV: 岩田陽葵) / 作詞：中村彼方 / 作曲：尋木ヒロ / 編曲：尋木ヒロ・小高光太郎 / ストリングスアレンジ：加藤達也`**.
- **Binding Analytical Decision for `V2` (and Retraction of `CP17A` Misstatement)**:
  - **`REJECT` `CP17A` Error**: `CP17A` (`RS_AV_R2_SYMMETRIC_COMPARATIVE_CLAIM_AUDIT.md` `L84`, `L168`, `L178` & `RS_AV_R2_INTEGRATOR_HANDOFF_AND_PUBLICATION_PROPOSAL.md` `L80`) misread the `.ass` `<...>` monologue brackets at `21:57–22:03` as song-lyric brackets and falsely claimed those lines were the chorus lyrics of `Fly Me to the Star`. That criticism of `V1` is **formally retracted**.
  - **`PRESERVE` `V1` Monologue Citation + `STRENGTHEN` with `22:31` ED State-Machine**: `V1` (`05_MAHIRU_FUTABA...` `L285`, `14_EPISODE_MOVEMENT...` `L293`, `15_JAPANESE_DIALOGUE...` `L128`) accurately quoted `大切な人達を幸せにしたいと思えば 何度でもキラめける` as Mahiru's Episode 5 closing interior resolution (clarifying its mode in `V2` as **spoken inner narration (`心の声`)** answering her junior-high interview at `21:14`). Meanwhile, `R2`'s independent musical-dramaturgy finding—that `V1` contains **`0` mentions of `Fly Me to the Star`** across all `26` files and misses the `22:31–24:00` Stem II bossa-pop ED state-machine (`TV03`–`TV12`)—stands intact on `22:31–24:00`.
  - **Point Left Explicitly `[OPEN]`**: Whether the warm piano/strings `劇伴` cue under `21:14–22:30.5` is an autonomous Fujisawa Yoshiaki underscore cue or shares any harmonic cell with the standalone song catalog is left **`[OPEN]`** pending score-sheet verification; it is definitively **not** part of the credited `Fly Me to the Star` track (`22:31.26–24:00.86`).

---

### 2.3 `OVA01`–`OVA03` Chronology & `99.419` Epistemic Stratification (`[AV-FACT]` vs. `[INFERRED]`)

Direct inspection of `OVA01` (`SHA-256: 14bcfd93...`), `OVA02` (`SHA-256: 04b35dd4...`), and `OVA03` (`SHA-256: c2152663...`) establishes the following strict separation between **direct onscreen textual/visual anchors** and **calendar inference**:

1. **Direct Primary Anchors (`[AV-FACT]` / `[JP-TXT]`) — Carried Forward as Explicit Corpus Facts**:
   - **Festival Year `2019`**: `OVA01` `01:20.5` (`ova01_0080.5`) Class B `衣装部屋(仮)` whiteboard header reads verbatim **`聖翔祭 2019 採寸 / 舞台創造科`** (with scheduling memo `◎ 愛城さんと神楽さん 採寸時間変更 [OK]` and `#100 聖翔祭 | Character: クレール | Actor: 神楽ひかり | Scenes: 7, 9 ~ 10, 12` on Claire's cloak tag at `01:35.5`).
   - **Explicit Day Countdowns**:
     - `OVA01` `00:09.5` (`ova01_0009.5`) & `06:33.0` (`ova01_0393.0`): Corridor countdown sign beside `第100回 聖翔祭 / STAR LIGHT 100th` poster reads **`聖翔祭まで 50日`**.
     - `OVA02` `00:31.5` (`ova02_0031.5`): Corridor countdown sign reads **`聖翔祭まで 29日`** (corroborated by Class B dialogue at `00:09`: `本番まであと1ヶ月って / 早いよね〜`).
     - `OVA03` `06:00`–`07:03`: Opening Day (`いよいよ記念すべき第100回聖翔祭、本番です！`), splicing directly via `06:57–07:03` live auditorium applause into `TV12` `22:00`.
   - **`99.419` Signage Anchor**: `OVA03` `00:07.5` (`荻窪バッティングセンター`) and `00:16.5` (`ova03_0016.5`) Cage `④` (`[100]周年記念 ホームラン祭`) poster reads verbatim **`ホームラン 挑戦者求ム！ / 右 160 km/h / 99.419 mi/h`** (`160 km/h ÷ 1.609344 km/mi = 99.41939 mi/h`), resolving both the `#1–#3 / 99.419` anthology title prefix and Karen's `50`-day wooden-bat `素振り` cutaways (`OVA01` `03:37–03:45`; `OVA02` `01:41–01:54`) to win the giant `Mr. White` plush (`04:39`).
2. **Inferred Calendar Window (`[INFERRED]`) & Unresolved Exact Date (`[OPEN]`)**:
   - **No direct month-and-day string (`3月X日`) appears onscreen anywhere in `OVA01`–`OVA03`**.
   - Therefore, placing `第100回 聖翔祭` in **early March 2019**—and placing `OVA01` (`-50d`) in **mid-January 2019** and `OVA02` (`-29d`) in **early February 2019**—must be explicitly labeled **`[INFERRED]`** in `V2`, derived from combining: (a) `聖翔祭 2019` (`[JP-TXT]`), (b) `TV07`'s `2018.3.3` `第99回 聖翔祭` precedent (`[JP-TXT]`), (c) winter bare branches (`OVA01` `03:37`) and snowfall (`OVA02` `01:38`) giving way to budding pink `梅` (plum blossoms, `OVA03` `05:50`) (`[AV-FACT]`), and (d) the ~2.5-month rehearsal window following Hikari's late-December 2018 return (`TV12` `21:43`).
   - The **exact calendar date** in `2019` of `第100回 聖翔祭` remains **`[OPEN]`**.

---

### 2.4 `2021` Sequel Film: Verified `5.1` Stream & Composer/Prelude Credits vs. Conclusions Drawn from the Mix

In `V2`, technical audio/credit facts and interpretive readings of the mix are strictly separated into two distinct evidentiary tiers (harmonizing `R2`'s multi-stream discovery with `V1` `09_MUSIC_SONG_JAPANESE_VOICE_AND_MUSICAL_DRAMATURGY.md` `# XIX` `L1960–2008`):

1. **Tier 1 — Verified Primary Facts (`[AV-FACT]` / `[MUS-FACT]` / `[JP-TXT]`)**:
   - **Discrete Japanese `5.1` Audio Stream**: Upstream `[Veggie Sub] Shoujo☆Kageki Revue Starlight Movie.mkv` (`SHA-256: 7b5be2c4a9c6d6b08c6f338411f21a09bc813c5bf3ebca51ee6fbde1995fd38c`) carries a verified `6`-channel Japanese surround stream **`0:a:1` (`48 kHz`, `635 kbps` `AAC LC`, channel layout `5.1 [FL, FR, FC, LFE, BL, BR]`)**, whereas pipeline `movie.analysis-softsub.mkv` (`SHA-256: e2ec8fc8...`) carries a `160 kbps` stereo `AAC 2.0` stream (`0:a:0`).
   - **Verified Onscreen Composer & Prelude Credits (`01:58:46–01:59:05`, `1920x1080` End Roll)**:
     - **`主題歌「私たちはもう舞台の上」`** (`01:57:06–01:59:50`) explicitly credits **`前奏作曲：本多友紀 (Arte Refact)`** (composer of the TV OP `星のダイアローグ`) alongside **`作曲・編曲：佐藤純一 (fhána)`** and **`作詞：中村彼方`**.
     - **`挿入曲「スーパー スタァ スペクタクル」`** (`01:48:27–01:56:15`) carries a **single unified composition credit** (`作詞：中村彼方 / 作曲・編曲：加藤達也 / ストリングス・ブラス追加アレンジ：葛西竜之介`), proving there is no separate song credit for the `01:49:02–01:51:30` `アタシ再生産` rocket-train movement.
   - **Measured `5.1` Channel Telemetry (`7,222` `1s` RMS Bins)**: Descriptive dBFS channel measurements (e.g., `Surr − Front` shifting from `-9.38 dB` in `01:07:04–01:08:03` to `-2.25 dB` in `01:08:09–01:11:30`; full-stream drop to `-99.64 dBFS` at `01:46:32.5`; `LFE` peaking at `-10.83 dBFS` during `01:54:18–01:55:45`; `LFE = -96.00 dBFS` across `01:57:06–02:00:18`; `FC − LR = +13.72 dB` in Act I campus dialogue and `+25.10 dB` in `01:59:56–02:00:18`) are objective descriptive properties of `0:a:1`.
2. **Tier 2 — Interpretive / Corroborative Conclusions Drawn from the Mix (`[INTERPRETATION]` / `[CORROBORATIVE]`)**:
   - Treating the `5.1` soundstage as a deliberate "ontological ruler," or reading `LFE = -96.00 dBFS` during `私たちはもう舞台の上` (`01:57:06–01:59:50`) and `FC`-dominant dialogue (`+13.72 dB` / `+25.10 dB`) as proof of intentional metaphysical demystification, **is an interpretive conclusion (`[INTERPRETATION]`), not a self-proving technical fact**.
   - **Mandatory Counterevidence Weighing**: Under standard Japanese theatrical post-production practice (`Sound Team Don Juan` / `東宝ポストプロダクションセンター`), ordinary dry dialogue scenes routinely route speech exclusively to `FC` with minimal `FL/FR/LFE` activity, and commercial `2.0`-mastered J-pop credit songs (`私たちはもう舞台の上`) are routinely laid into `5.1` theatrical stems without synthesizing dedicated `.1` LFE content. Accordingly, `V2` **downgrades** any standalone ontological claim from `LFE = -96.00 dBFS` on the credits song to a **mix-corroborative observation subject to standard post-production convention**, while retaining high confidence where *within-scene* `5.1` modulation tracks visible staging shifts inside a single `5.1`-mixed sequence (such as the `+7.13 dB` rear-surround expansion at `01:08:09` when Mahiru shifts into backstage pursuit, or the `-99.64 dBFS` digital-zero silence at Karen's onstage death).

---

### 2.5 `TV06` `今回の再演` Forecast (`CLM-0012`) & Preservation of Prior-Knowledge Disclosure

In `00_inventory/RS_AV_R2_SOURCE_AND_EXECUTION_INVENTORY.md` (`L32–36`), `RS-AV-R2-GEMINI-CARBON` recorded the following mandatory **Prior-Knowledge Quarantine Disclosure** before inspecting `TV01`:

> "`Gemini 4 Carbon` possesses general pretraining awareness that *Shōjo Kageki Revue Starlight* (2018, dir. Tomohiro Furukawa, Kinema Citrus) centers on nine `99th` Class students at Seishō Music Academy (`愛城華恋`, `神楽ひかり`, `天堂真矢`, `星見純那`, `露崎まひる`, `大場なな`, `西條クロディーヌ`, `石動双葉`, `花柳香子`), an underground audition overseen by a talking giraffe (`キリン`, `ポジション・ゼロ`), a mid-series temporal-loop revelation involving Daiba Nana, and a 2021 theatrical sequel structured around post-graduation `wi(l)d-screen baroque` Revues."

**Rule Enforced Across `V2`**:
- Whenever `V2` (in `02 Television Series Readings/TV06_DEEP_READING.md`, `05 Full-Series Synthesis/03_JUNNA_NANA...`, or `06 Evidence and Indexes/14_EPISODE_MOVEMENT...`) cites Nana's `TV06` `23:48–23:58` post-credits stinger (`今回の再演、どうしちゃったのかな。初めてのことばっかり。やっぱり、台本どおりじゃなくっちゃね`) as foreshadowing `TV07`'s Giraffe-backed time loop (`CLM-0012`), it **explicitly preserves this prior-knowledge disclosure**, distinguishing:
  1. What `TV06` `23:44–24:01` **explicitly establishes onscreen** to a first-time viewer (`[AV-FACT]` / `[JP-TXT]`: Nana's unhidden nocturnal comfort beside the Giraffe, her `決定稿 戯曲スタァライト 99th` script and Year-1 `8`-girl photo, the lexical anomaly of `今回の再演` + `初めてのことばっかり`, and the `24:01.0` full-screen `大場なな` glitch); from
  2. Why `R2`'s specific `TV06` loop hypothesis (`CLM-0012`) **cannot be cited as blind zero-knowledge prophecy**, because the model operated under quarantined pretraining awareness of Nana's loop twist.

---

## 3. Proposed Canonical `V2` Directory Architecture & Governance Integration Plan

### 3.1 Proposed Home for `TV01`–`TV12`, `OVA01`–`OVA03`, and `2021` Film Readings (`02`–`04` Slots)

In `V1`, `series/revue-starlight/` jumped directly from `01 Source Lock and Inventory/` to `05 Full-Series Synthesis/`, leaving slots **`02`**, **`03`**, and **`04`** vacant. Canonical `V2` populates those exact three architectural slots with reconciled anime-only unit readings while preserving `V1`'s `00`–`01` and `05`–`07` numbering and archiving `V1` cleanly under `90 Archive/`:

```text
series/revue-starlight/
├── CURRENT_STATE_AND_CORPUS_MAP.md                 # Run-closure / authority index routing V2 vs. archived V1 & R2
├── 00 Frameworks/
│   ├── RevueStarlightAnalyticalMethod_v2.md        # Reconciled prospective unit-reading method (artifact_type: analytical_method)
│   ├── RevueStarlightAnalyticalMethod_MusicalDramaturgy_v3.md
│   ├── RevueStarlightMovieAnalyticalMethod_v2.md
│   ├── RevueStarlight_Full_Series_Analytical_Method_v2.md
│   ├── RevueStarlight_Multi_Document_Synthesis_Architecture_v2.md  # (artifact_type: synthesis_architecture)
│   └── RevueStarlight_Anime_Character_Reconstruction_Spec_v1.md    # Preserved; character models & ratings DEFERRED
├── 01 Source Lock and Inventory/
│   └── SOURCE_INVENTORY.md                         # Canonical V2 source lock (see RS_AV_R2_V2_SOURCE_INVENTORY_PROPOSAL.md)
├── 02 Television Series Readings/                  # <-- NEW HOME FOR TV01–TV12 + TV SUB-SYNTHESIS
│   ├── 00_TV_SERIES_SYNTHESIS_TV01_TV12.md
│   ├── TV01_BUTAI_SHOUJO_DEEP_READING.md
│   ├── TV02_UNMEI_NO_BUTAI_DEEP_READING.md
│   ├── TV03_TOP_STAR_DEEP_READING.md
│   ├── TV04_YAKUSOKU_TOWER_DEEP_READING.md
│   ├── TV05_KIRAMEKI_NO_DOKO_DEEP_READING.md       # Incorporates §2.1 & §2.2 TV05 primary rechecks
│   ├── TV06_FUTARI_NO_HANAMICHI_DEEP_READING.md    # Preserves §2.5 prior-knowledge disclosure on 23:48 stinger
│   ├── TV07_DAIBA_NANA_DEEP_READING.md
│   ├── TV08_HIKARI_SASU_HO_E_DEEP_READING.md
│   ├── TV09_HOSHI_MATSURI_NO_YORU_DEEP_READING.md
│   ├── TV10_SAREDO_BUTAI_WA_TSUZUKU_DEEP_READING.md
│   ├── TV11_WATASHITACHI_WA_DEEP_READING.md
│   └── TV12_REVUE_STARLIGHT_DEEP_READING.md
├── 03 OVA Readings and Supplement/                 # <-- NEW HOME FOR OVA01–OVA03 + OVA SUPPLEMENT
│   ├── 00_OVA_99_419_CYCLE_SUPPLEMENT.md           # Incorporates §2.3 [AV-FACT] vs. [INFERRED] March 2019 stratification
│   ├── OVA01_99_419_MEASURING_READING.md
│   ├── OVA02_99_419_DISCUSSION_READING.md
│   └── OVA03_99_419_OPENING_READING.md
├── 04 Sequel Film Monograph/                       # <-- NEW HOME FOR 2021 SEQUEL FILM MONOGRAPH
│   └── 01_GEKIJOUBAN_2021_SEQUEL_FILM_MONOGRAPH.md # Incorporates §2.4 5.1/credits vs. mix-inference stratification + V1 credits relay
├── 05 Full-Series Synthesis/                       # Reconciled Canonical V2 14-document synthesis (00–13)
│   ├── 00_README_AND_CORPUS_MAP.md                 # Registered canonical_entrypoint in series_registry
│   ├── 01_SERIES_ARCHITECTURE_TV_OVAS_FILM_AND_DEVELOPMENT.md
│   ├── 02_KAREN_HIKARI_PROMISE_SELFHOOD_AND_RIVALRY.md
│   ├── 03_JUNNA_NANA_MEMORY_REPLAY_AND_AUTHORSHIP.md
│   ├── 04_MAYA_CLAUDINE_RIVALRY_PERFECTION_AND_EXPOSURE.md         # Deduplicated single-draft V2 (repairs 697-line V1 tail)
│   ├── 05_MAHIRU_FUTABA_KAORUKO_CARE_DEPENDENCE_AND_DIFFERENT_ROADS.md # Deduplicated appendices + verified TV05 inner narration
│   ├── 06_SEISHO_99TH_CLASS_ENSEMBLE_AND_CHARACTER_ECOLOGY.md      # Monotonic Appendix A–F + verified 8→9 & OVA care speakers
│   ├── 07_REVUE_SYSTEM_GIRAFFE_AUDIENCE_POSITION_ZERO_AND_STAGE_ONTOLOGY.md
│   ├── 08_STARLIGHT_INTERTEXT_SCRIPT_REWRITE_REENACTMENT_AND_REPRODUCTION.md
│   ├── 09_MUSIC_SONG_JAPANESE_VOICE_AND_MUSICAL_DRAMATURGY.md
│   ├── 10_VISUAL_CINEMATIC_GRAMMAR_MOTIFS_AND_STAGE_MACHINERY.md
│   ├── 11_ETHICS_PERSONHOOD_DESIRE_MEMORY_AND_SELF_AUTHORSHIP.md
│   ├── 12_ENDINGS_GRADUATION_NEXT_STAGE_AND_REPRODUCTION.md
│   └── 13_COMPARATIVE_REFERENCE_MATRICES_AND_OPEN_QUESTIONS.md
├── 06 Evidence and Indexes/                        # Reconciled Canonical V2 ledgers & indexes (14–15) + R2 specialized ledgers
│   ├── 14_EPISODE_MOVEMENT_AND_REVUE_EVIDENCE_LEDGER.md
│   ├── 15_JAPANESE_DIALOGUE_LYRIC_AND_MOTIF_INDEX.md               # Monotonic # I–# XVIII + subtitle discrepancy table
│   ├── 16_MUSICAL_DRAMATURGY_ED_STEM_AND_5_1_ACOUSTIC_LEDGER.md
│   └── 17_ANIME_CHARACTER_STATE_AND_ADDRESS_REGISTER_LEDGER.md     # Evidence ledger only (models/ratings deferred)
├── 07 Audits and Manifests/
│   ├── CORPUS_MANIFEST.md
│   ├── CHECKSUM_AUDIT.md
│   ├── FILE_CHECKSUMS.sha256
│   └── V1_STRUCTURAL_AND_CHECKSUM_ERRATUM.md       # Separate erratum for V1 structural/checksum findings
├── 10 Gemini Carbon R2/                            # Optional preserved pre-exposure R2 witness (status: draft_noncurrent)
├── 11 Gemini Carbon R2 Comparison/                 # Comparative audit & this Track C V2 reconciliation specification
└── 90 Archive/
    └── V1_2026-08-10/                              # Preserved V1 files marked status: superseded, do_not_use_as_current_authority: true
```

### 3.2 Authority, Supersession, & Repository Validator Compliance (`ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md`)

1. **Two-Step Owner-Authorized Gate**:
   - **Step 1 (`agent/governance` → `main`)**: Add an owner-approved `project-initiation-gate.json` entry authorizing canonical `V2` continuation/supersession on `series/revue-starlight/` (plus the `frozen_generation_publications` grant if `10 Gemini Carbon R2/` is co-published alongside `V2`).
   - **Step 2 (`series/revue-starlight` → `main`)**:
     - Every active `V2` file in `00 Frameworks/` through `07 Audits and Manifests/` carries the canonical authority quartet:
       ```yaml
       status: canonical
       supersedes:
         - "series/revue-starlight/90 Archive/V1_2026-08-10/<prior_file>.md" # or [] for net-new 02–04 readings
       superseded_by: []
       do_not_use_as_current_authority: false
       ```
     - Every archived `V1` file moved into `90 Archive/V1_2026-08-10/` carries the exact reciprocal superseded quartet (no silent deletion of `V1`!):
       ```yaml
       status: superseded
       supersedes: []
       superseded_by:
         - "series/revue-starlight/<v2_replacement_path>.md"
       do_not_use_as_current_authority: true
       ```
     - Run `python tools/validate_repository.py` plus deterministic checks for UTF-8 LF (`\n`), NFC Unicode normalization, zero private workstation paths, zero duplicate `#` headings, and `100%` `FILE_CHECKSUMS.sha256` match.

---

## 4. Retained Supported `V1` Analysis (`PRESERVE` Core Inventory)

Canonical `V2` explicitly **retains (`PRESERVE`)** `V1`'s supported conceptual, structural, and textual achievements rather than replacing `V1` wholesale with `R2` prose:

1. **Credits Song (`私たちはもう舞台の上`) Four-Voice Worn-Script Lyric Relay (`MOV-EPI`, `01:58:11.76–01:58:27.41`)**:
   - Retained from `05 Full-Series Synthesis/09_MUSIC_SONG_JAPANESE_VOICE_AND_MUSICAL_DRAMATURGY.md` (`# XVIII` `L1865–1915`), `06 Evidence and Indexes/14_EPISODE_MOVEMENT_AND_REVUE_EVIDENCE_LEDGER.md` (`# XXVIII` `L2114–2165`), and `15_JAPANESE_DIALOGUE_LYRIC_AND_MOTIF_INDEX.md` (`L176`), paired in `V2` with `R2`'s exact vocal timestamps and `前奏作曲：本多友紀` fanfare discovery:
     - `Maya` (`01:58:11.76`): `折り目をつけた台本には` → `Claudine` (`01:58:15.67`): `新しいことは何もなくて` → `Junna` (`01:58:19.44`): `台詞はとうに馴染んでるから` → **`Nana` (`01:58:23.39`)**: **`閉じてしまってもいっか`** (the former guardian of the `99th` `再演` script singing permission to close it).
2. **Three-Form Taxonomy of Emptiness (`空っぽ`)**:
   - Retained from `05 Full-Series Synthesis/12_ENDINGS_GRADUATION_NEXT_STAGE_AND_REPRODUCTION.md` (`# I` `L154–176` & `# XI` `L879–985`) and `00 Frameworks/RevueStarlight_Full_Series_Analytical_Method_v1.md` (`L1075–1090`):
     - (1) **Destructive / bereft emptiness** (`TV11` Karen & `MOVIE` `01:46:11` `何もない` after losing an externalized relational telos);
     - (2) **Defensive / fraudulent emptiness** (`MOVIE` `01:34:45` Maya's `空っぽの器`, shielding pride and appetite behind perfected neutrality);
     - (3) **Generative theatrical emptiness** (`MOVIE` `01:56:40` Karen's `私今 世界で一番空っぽかも`, the cleared actor's vessel ready to receive `次の役`).
3. **Six-Operation Taxonomy of Theatrical Repetition (`再演` vs. `再生産` and Benign Recurrence)**:
   - Retained from `05 Full-Series Synthesis/08_STARLIGHT_INTERTEXT_SCRIPT_REWRITE_REENACTMENT_AND_REPRODUCTION.md` (`# I` `L104–178`, `# X` `L768–833`, & `# XXIII` `L1697–1822`):
     - Distinguishing **`稽古` (*rehearsal*)**, **ordinary institutional `再演` (*restaging*, e.g., `99th` → `100th` → `101st` *Starlight*)**, **`引用` (*literary/scenic quotation*)**, **`リプライズ` (*musical reprise*)**, **Nana's possessive `私の再演` (*loop replay* erasing the temporal interval)**, and **`再生産` (*co-authored / self-authored transformative re-production* accepting the interval)**.
4. **Nine-Tier Spectatorship / Audience Taxonomy & Three-Level Stage Ontology**:
   - Retained from `05 Full-Series Synthesis/07_REVUE_SYSTEM_GIRAFFE_AUDIENCE_POSITION_ZERO_AND_STAGE_ONTOLOGY.md` (`# V–# VI` `L518–917` & `# XIV` `L1606–1703`):
     - Preserving all nine gaze structures (`1. Institutional Giraffe`, `2. Public theatrical audience`, `3. Ensemble audience`, `4. Fanhood [Futaba & Hikari]`, `5. Archival audience [Nana]`, `6. Intimate rival audience [Claudine & Maya]`, `7. Coercive-confessional audience [Mahiru]`, `8. Karen's audience awakening`, `9. External viewer`), the Giraffe's seven-phase transformation from judge to self-immolating `燃料`, and the three-level metaphysical discipline (`diegetic Revue fact`, `performed theatrical reality`, `poetic/cinematic visualization`).
5. **Core Dyadic, Ensemble, Mix-Caution, & Open-Boundary Insights**:
   - Preserves `V1`'s analysis of Mahiru's `TV05` interior-monologue recovery (`大切な人達を幸せにしたいと思えば 何度でもキラめける`, `Doc 05` `L285`), Junna's protective temporal hedge (`でも 今は、よ`, `Doc 14` `L179`, `L1217`), Maya/Claudine's rivalry-not-couplehood boundary (`Doc 04` `L752–813`), `Doc 09` `# XIX`'s final-mix methodological caution (`L1960–2008`), and `Doc 13`'s strict anime-only `[OPEN]` boundaries (`L440–556`).

---

## 5. Deferred Scope Confirmation (Character Models & Capability Assessment)

In strict accordance with the user's instructions and `00 Frameworks/RevueStarlight_Anime_Character_Reconstruction_Spec_v1.md`:
- **No standalone character-reconstruction persona models** (`characters/...`) are generated in this Track C candidate.
- **No character reconstruction capability tiers, scores, or evaluator grades** are assigned anywhere in `V2` (`CHARACTER_RECONSTRUCTION_EVALUATION_AND_RATING_METHOD.md` remains strictly separate and deferred).
- `V2` confines itself to **source-locked anime analytical synthesis, sequential unit readings, Japanese linguistic/musical ledgers, and verifiable behavioral evidence** inside `series/revue-starlight/`.
