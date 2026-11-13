---
title: "Cosmic Princess Kaguya! (F01) — primary freeze, stage handoff, and mirror reconciliation record"
series: cosmic-princess-kaguya
artifact_id: CPK_F01_RECONCILIATION_RECORD
artifact_type: audiovisual_reconciliation_record
stage_state: RECONCILED_AND_INTEGRATED
generation: CPK-G1
version: "1.1"
status: canonical
authority_scope: "Canonical mirror-reconciliation record for F01: preserved CPK-R1 freeze manifest, Stage-2 CPK-B1-SOL61 receiver acceptance & freeze hashes, bounded 1-of-1 AV return receipt (CPK-AVRET-R1), Protocol §5.4 av_reconciliation summary, §15.6 checks, and complete Stage-3 write-through manifest"
source_boundary: "Admitted Japanese feature witness CPK-W01-NF-WEBRIP-HEVC (F01, 00:00:00.000-02:22:03.207); primary run CPK-R1, independent bundle/audit benchmark CPK-B1-SOL61, bounded AV return CPK-AVRET-R1, and Stage-3 integration CPK-INT completed"
canonical_home: series/cosmic-princess-kaguya/audits/CPK_F01_RECONCILIATION_RECORD.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Primary candidate freeze, stage handoff, and reconciliation record (`F01`)

> **Quarantine warning (Set 2 — Withheld Before Blind Freeze):** Because §§3–5 of this record contain the frozen hashes of primary narrative outputs, primary analytical conclusions, and the **withheld adjudication table** mapping neutral queue IDs `Q-F01-0001`–`Q-F01-0024` to primary claims `CPK-R1-C0001`–`CPK-R1-C0020`, **a blind `BUNDLE_MEDIATED` verifier must NOT open this file prior to freezing `audits/CPK_F01_BLIND_OBSERVATIONS.md`.** Use [audits/CPK_F01_BLIND_INPUT_PACKET.md](CPK_F01_BLIND_INPUT_PACKET.md) exclusively for pre-freeze blind inspection.

---

## 1. Stage handoff and transfer envelope ([Handoff Contract](../../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) §3)

| Field | Recorded value |
|---|---|
| `transfer_id` | `CPK-XFER-R1-PRIMARY-FREEZE-20261111` |
| `stage_state` | `READY_FOR_HANDOFF` (primary `CONTINUOUS_AV` candidate & pre-audit snapshot complete for `F01`; blind audit & integration unexecuted) |
| Repository & continuing branch | `deep-blue-zero/anime-manga-ln-games-analysis` — branch `series/cosmic-princess-kaguya` |
| Canonical project root & entrypoint | `series/cosmic-princess-kaguya/` — `series/cosmic-princess-kaguya/CURRENT_STATE_AND_CORPUS_MAP.md` (`v1.3`) |
| Merged bootstrap baseline (`main`) | `f9a284e66943ce007d31e899f88074a17900d3cf` (PR #541 merge commit incorporating housekeeping child `535c970e9643774abbe74e602fd5563dee2bf983`) |
| Active run-admission base commit | `502d1dd3029dde0959fa5f7af7c84469fe799cc9` (`run_state: active`, `sequential_analysis_lock: open`, `next_permitted_operation: F01`) |
| Governing method / profile versions | `CPK_ANALYTICAL_METHOD.md` `v1.0`, `CPK_SYNTHESIS_ARCHITECTURE.md` `v1.0`, `CPK_RECONCILIATION_PROFILE.md` `v1.0`; Handoff Contract `v1.2`, Audiovisual Reconciliation Protocol `v1.0` |
| Owner instruction & scope boundary | Authorized complete Japanese-primary `CONTINUOUS_AV` source analysis of single feature unit `F01` (`超かぐや姫！ / Cosmic Princess Kaguya!`), primary candidate freeze, ledger population, validation, branch publication, and PR creation (no merge to `main`, no other works, no raw media in Git) |
| Producer role & verified runtime | `CPK-R1`: **Gemini 4 Carbon** (`High` thinking effort; `UNKNOWN_INTERNAL_BUILD_ID` runtime checkpoint string) on Antigravity Windows harness (`ffmpeg`/`ffprobe` `n8.0` + native `.mp4`/`.png` `read_file` inspection; `~1.0` fps visual sampling paired with continuous `48 kHz` Japanese audio) |
| Assigned next receiver roles | **Stage 2 Receiver:** Separate fresh-context OpenAI `BUNDLE_MEDIATED` blind verifier (reads Set-1 allowlist only → freezes `audits/CPK_F01_BLIND_OBSERVATIONS.md` → opens Set 2 → writes `audits/CPK_F01_CLAIM_AUDIT.md`). **Stage 3 Receiver:** Capability-qualified integrator (performs targeted `CAV` return if needed, updates cumulative homes, and authors `synthesis/CPK_F01_INTEGRATED_SYNTHESIS.md`) |
| Primary witness & clock binding | `CPK-W01-NF-WEBRIP-HEVC` (`4,916,885,885` B, SHA-256 `b940eede5e3ce2e83e507a33e6523516c21e770dbccd8cc9e4461af77b23a42a`, `8523.207` s / `02:22:03.207`) + `CPK-CLK-F01-GLOBAL` (`0:a:0` Japanese Track 1 root authority; `0:s:3` Japanese `[SDH]` Track 4 supporting text; `138` ms audio `start_pts` normalized to `0.000` s across `CAL-01`–`CAL-07`) |

---

## 2. Exact deliverable & exposure-set freeze manifest (`CPK-R1`)

All text deliverables are UTF-8 (no BOM), Unicode NFC, LF-only, with zero trailing line whitespace. Self-referential hash of this `CPK_F01_RECONCILIATION_RECORD.md` is recoverable directly from the Git completion commit tree.

### 2.1 Set 1 — Pre-freeze **ALLOWED** project artifacts for blind verifier

| Repository path | Artifact ID & version | Authority status | Exact bytes | Exact SHA-256 | Exposure rule |
|---|---|---|---|---|---|
| `series/cosmic-princess-kaguya/CPK_ANALYTICAL_METHOD.md` | `CPK_ANALYTICAL_METHOD` `v1.0` | `canonical` | `17631` | `1441dbe736dd48a9fa34d63ddccd81522341bab6607a505f2440d2b6425e1cba` | `ALLOWED_PRE_FREEZE` |
| `series/cosmic-princess-kaguya/CPK_SYNTHESIS_ARCHITECTURE.md` | `CPK_SYNTHESIS_ARCHITECTURE` `v1.0` | `canonical` | `21618` | `92cc7545bab5f7fc3caf9cae4e87987c5e7a76006b4d0f22a6f1314204fba89a` | `ALLOWED_PRE_FREEZE` |
| `series/cosmic-princess-kaguya/CPK_RECONCILIATION_PROFILE.md` | `CPK_RECONCILIATION_PROFILE` `v1.0` | `canonical` | `14289` | `9ad9036df3d460acb6264e7411ffafdbddf4b5a883943542ca15e8d1dd8ef309` | `ALLOWED_PRE_FREEZE` |
| `series/cosmic-princess-kaguya/CPK_BOOTSTRAP_REVIEW.md` | `CPK_BOOTSTRAP_REVIEW` `v1.0` | `canonical` | `7381` | `a0a03765bc2c4d4f9c4230d3015ef89aff6b46afdd2c74c2c168b355b8f8b613` | `ALLOWED_PRE_FREEZE` (contains zero film findings) |
| `series/cosmic-princess-kaguya/audits/CPK_F01_BLIND_INPUT_PACKET.md` | `CPK_F01_BLIND_INPUT_PACKET` `v1.0` | `draft_noncurrent` | `21403` | `807784579986a87afea5da5ce0bdf1921d803a6be5e81baed72662da91b7c2a2` | **`START_HERE_BLIND_VERIFIER`** |

### 2.2 Set 2 — Pre-freeze **WITHHELD** primary candidate & pre-audit snapshot (frozen byte-for-byte)

| Repository path | Artifact ID & version | Authority status | Exact bytes | Exact SHA-256 | Preservation & exposure rule |
|---|---|---|---|---|---|
| `series/cosmic-princess-kaguya/readings/CPK_F01_PRIMARY_DEEP_READING.md` | `CPK_F01_PRIMARY_DEEP_READING` `v1.0` | `draft_noncurrent` (`do_not_use_as_current_authority: true`) | `86421` | `cf7c64d7f4e70d8bfbbc8d97652e40c99de115e5bd9958e4f620197c70a47c3c` | **`FROZEN_IMMUTABLE_CANDIDATE` / `WITHHELD_PRE_FREEZE`** — never edit bytes to add audit revisions |
| `series/cosmic-princess-kaguya/CPK_SOURCE_INVENTORY.md` | `CPK_SOURCE_INVENTORY` `v1.1` | `canonical` | `33190` | `51d50099349a8c799990fb6091a6146b033e0bb5769f7ad8f10f649e14322c77` | `WITHHELD_PRE_FREEZE` (§4–§5 include primary target labels); mutable by integrator only |
| `series/cosmic-princess-kaguya/CPK_OBSERVATION_LEDGER.md` | `CPK_OBSERVATION_LEDGER` `v1.1` | `canonical` | `77806` | `76f4cd8d6aa5ffab5dc3d7540a913a04f1a59391ee663f7be3c2c1da8a184c2e` | `WITHHELD_PRE_FREEZE`; append-preserving `CPK-R1` snapshot (`S0001`–`S0036`, `O0001`–`O0040`, `M0001`–`M0014`) |
| `series/cosmic-princess-kaguya/CPK_CHARACTER_RELATIONSHIP_LEDGER.md` | `CPK_CHARACTER_RELATIONSHIP_LEDGER` `v1.1` | `canonical` | `64307` | `8f6aea5a65f96a9bb8a3fa9d4742514c238ed0e86f7232353be6a6b1b6ea4626` | `WITHHELD_PRE_FREEZE`; append-preserving `CPK-R1` snapshot (`15` subjects, `K0001`–`K0024`, `E0001`–`E0020`, `J0001`–`J0018`) |
| `series/cosmic-princess-kaguya/CPK_CLAIM_REVISION_LEDGER.md` | `CPK_CLAIM_REVISION_LEDGER` `v1.1` | `canonical` | `40216` | `aee13ff18e30f8729d165cdf4c4bbc762d9fa56667ee403a82ea766fcca75f20` | `WITHHELD_PRE_FREEZE`; holds exact `CPK-R1` formulations (`C0001`–`C0020`) & `U0001`–`U0008` |
| `series/cosmic-princess-kaguya/CURRENT_STATE_AND_CORPUS_MAP.md` | `CURRENT_STATE_AND_CORPUS_MAP` `v1.3` | `canonical` | `8106` | `037242b754a74b9039ce61db532bd48abfb1ff2b7539a0857bb5e49a652a9ad3` | Mutable sole entrypoint (`run_state: completed`, `committed_high_water_mark: F01`) |

---

## 3. Coverage, obligations, preservation constraints, and §15.6 receipt

1. **Modality and interval closure (`CPK-R1`)**:
   - `F01` continuous audiovisual (`SEG-01`–`SEG-15`, `[00:00:00.000, 02:22:03.207]`): `REQUIRED` / `COMPLETE_FOR_DECLARED_SCOPE` (`~1.0` fps visual + continuous `48 kHz` Japanese Track 1 audio).
   - High-bitrate reinspection clips (`P2-CLIP-01`–`06`, `334.0` s) & lossless `1920x1080` frames (`FRM-01`–`29`): `REQUIRED` / `COMPLETE_FOR_DECLARED_SCOPE`.
   - Japanese `[SDH]` text (`CPK-W01-SUB-JA-T4`, `2,716` cues): `REQUIRED` / `COMPLETE_FOR_DECLARED_SCOPE` for dialogue and subtitled insert songs; `PARTIAL` (`OPTIONAL` debt `U0008`) for unsubtitled end-credit song lyrics (`ray 超かぐや姫！Version` & `メルト CPK! Remix`), where zero exact lyric-line strings are asserted.
   - Deterministic cut/loudness/PSNR checks (`AM-01`–`06`, `CAL-01`–`07`): `OPTIONAL` / `COMPLETE_FOR_DECLARED_SCOPE`.
2. **Unresolved `REQUIRED` vs `OPTIONAL` obligations**:
   - **Unresolved `REQUIRED` obligations for primary candidate completion**: **`0`** (`NONE`).
   - **Stage-2 `REQUIRED` obligation (owned by separate OpenAI blind verifier)**: Execute independent `BUNDLE_MEDIATED` pass via `audits/CPK_F01_BLIND_INPUT_PACKET.md`, freeze `audits/CPK_F01_BLIND_OBSERVATIONS.md`, and audit `CPK-R1-C0001`–`C0020` in `audits/CPK_F01_CLAIM_AUDIT.md`.
   - **Bounded `OPTIONAL` / source-open items**: `CPK-R1-U0001`–`U0008` (see `CPK_CLAIM_REVISION_LEDGER.md` §4).
3. **Preservation rules (work that must NOT be redone or mutated)**:
   - Never modify `readings/CPK_F01_PRIMARY_DEEP_READING.md` (`cf7c64d7...`)—neither its prose nor its frontmatter quartet—even after `synthesis/CPK_F01_INTEGRATED_SYNTHESIS.md` is authored.
   - Preserve all `CPK-R1-*` IDs (`S0001`–`S0036`, `O0001`–`O0040`, `M0001`–`M0014`, `K0001`–`K0024`, `E0001`–`E0020`, `J0001`–`J0018`, `C0001`–`C0020`, `U0001`–`U0008`) intact across audit and integration.
4. **Handoff §15.6 editorial verification summary**:
   - Sampled `readings/CPK_F01_PRIMARY_DEEP_READING.md` across `§2.1`–`§2.6`, `§3.1`–`§3.3` (all nine consequential directed dyads), `§4.1`, and `§8.1`–`§8.3`.
   - Confirmed `KNOWLEDGE_BOUNDARY_REQUIRED` preservation for `いろP` (`S0006`–`S0013`), `帝アキラ` = `酒寄朝日` (`S0009`–`S0015`), and `月見ヤチヨ` = 8,000-yr `かぐや` (`S0001`–`S0030`); `SOURCE_REQUIRED_ANONYMITY` for `担任の先生`; `JUSTIFIED_ROLE_REFERENCE` where institutional roles perform analytical work; and **`0`** defects of `UNNECESSARY_GENERICIZATION`, `AMBIGUOUS_REFERENT`, or `INCORRECT_IDENTITY_OR_ATTRIBUTION`.

---

## 4. Withheld post-freeze adjudication packet (`Q-F01-0001`–`Q-F01-0024` → `CPK-R1-C0001`–`C0020`)

Open this table **only after** `audits/CPK_F01_BLIND_OBSERVATIONS.md` is frozen. Each neutral queue ID from `audits/CPK_F01_BLIND_INPUT_PACKET.md` §4 maps to the exact `CPK-R1` claim(s), expected source-grounded observation, disconfirmation threshold, and primary reading section:

| `queue_id` | Target `claim_id`(s) | Primary observation / assertion under test (`CPK-R1`) | Disconfirmation threshold | `PDR` & ledger anchors |
|---|---|---|---|---|
| `Q-F01-0001` | `C0001`, `C0015` | Frame 0 opens without logos/title on kimono-train & floating two-stack pancake island; Yachiyo VO `これは、ハッピーエンドのその先の物語` (`00:00:15`); hard cut (`scdet` `71.0`) at `00:01:20.956` | Presence of an opening main title card before `00:01:21` or absence of pancake-island framing | `PDR §2.1`, `§5.1`; `O0001`, `J0001` |
| `Q-F01-0002` | `C0002`, `C0018` | `FRM-01`: `神棚` Yachiyo standee above `即読英単語` / `やっておきたい英語長文` / `Vintage`; `FRM-02`: Momiji's Kansai-ben vertical text (`気張って無理し… すぐに泣いて帰ってくる思ってます`) | Absence of exam manuals / `神棚` in `FRM-01`, or non-Kansai / non-protective wording in `FRM-02` | `PDR §3.1`, `§7.2`; `O0002`–`0003`, `J0002` |
| `Q-F01-0003` | `C0004`, `C0016`, `C0018` | Looking at `神棚` Yachiyo standee, Iroha sings *a cappella* (`0` instruments) `大切なメロディは 流れてるよ あなたのハートに` (`00:07:33`–`00:07:49`), calming baby Kaguya (`ヤチヨパワー、すげぇ…`) | Instrumental backing present under `00:07:33`–`00:07:49`, or different sung refrain | `PDR §2.1`, `§6.1`; `O0006`, `M0002`, `J0003` |
| `Q-F01-0004` | `C0002`, `C0007`, `C0015` | `FRM-03`: `ふじゅペイ` `23,532円` (`20,532円` + `3,000 pt`) over baby basket; `FRM-04`: `tukuyomitube.com` `【PR動画】` (`410万回視聴`) `いま ツクヨミへ` | Contradictory yen figures in `FRM-03` or non-`TukuyomiTube` UI in `FRM-04` | `PDR §2.1`, `§3.1`; `O0007`–`0008` |
| `Q-F01-0005` | `C0003`, `C0006`, `C0018` | Kaguya shuts *Taketori Monogatari* picture book and denounces memory-wiping lunar return in gyaru speech as `超バッドエンドじゃん！` | Kaguya praising *Taketori*'s ending or speaking in formal/classical register | `PDR §2.2`, `§7.1`; `O0010`, `J0004` |
| `Q-F01-0006` | `C0009`, `C0016`, `C0018` | Yachiyo says classical `いと かわゆし` (`00:33:59`); on bridge (`P2-CLIP-02`), hands `いろP` charms over solo piano `Remember`, then **after `いろP` logs out (`00:35:01`), whispers real name `いつも来てくれてありがとね…… 彩葉`** (`00:35:06`) | Audio at `00:35:06` saying `いろP` instead of `彩葉`, or `いろP` still present onscreen during the whisper | `PDR §2.2`, `§4.1`, `§7.3`; `O0011`–`0012`, `M0006`, `J0005`–`0006` |
| `Q-F01-0007` | `C0002`, `C0016`, `C0017` | `FRM-05`: packed `バイト` + `東大文一` 6-subject Common Test wall schedule; `FRM-06`: `私は、わたしの事が好き。` playing above queued `竹取オーバーナイトセンセーション` & `メルト` | Absence of `東大文一`-aligned humanities+science distribution in `FRM-05` or absence of `メルト` on `FRM-06` | `PDR §2.2`, `§3.1`, `§6.5`; `O0013`–`0014` |
| `Q-F01-0008` | `C0005`, `C0007` | Caregiver inversion: Kaguya bans tired Iroha's `めんつゆ` pancakes to cook `しあわせパンケーキ` (`S0013`) and nurses feverish Iroha overnight (`S0018`) | Unilateral caregiving by Iroha without domestic/illness reversal by Kaguya | `PDR §2.2`–`§2.3`, `§3.2`; `O0015`, `O0018`, `E0001`–`0002` |
| `Q-F01-0009` | `C0006`, `C0008` | `Black onyX` wins `KASSEN` `2–1` (`S0014`), yet Kaguya's joyful `ハッピーシンセサイザ` encore wins Yachiyo Cup overall (`S0015`); `帝アキラ` revealed as brother `酒寄朝日` (`S0016`) | Kaguya winning `KASSEN` combat outright, or `帝アキラ` not being Iroha's brother `酒寄朝日` | `PDR §2.3`, `§3.3`; `O0016`–`0017`, `K0012`–`0014` |
| `Q-F01-0010` | `C0004`, `C0010`, `C0016` | `FRM-07`: `music > tomohisa > タイトル未定 ( 彩葉と共作 ).wav` (`01:45`, `2020/01`) plays the identical core melody as Yachiyo's `Remember` | Post-`2030` file timestamp or distinct non-`Remember` melody | `PDR §2.3`, `§4.1`, `§6.1`; `O0019`, `M0008` |
| `Q-F01-0011` | `C0007`, `C0011`, `C0015`, `C0018` | `結婚しよっかなぁ〜` → `01:24:16` silver wrist-bangle glint → `生活費折半してくれるなら…` → `01:24:27` hijack; AR-only `月人` visibility in Tokyo subway (`FRM-08`) projecting `2030/09/12` | Unaugmented commuters seeing `月人` in `FRM-08`, or absence of the `01:24:16` bangle insert / `生活費折半` vow | `PDR §2.4`, `§5.2`–`§5.3`, `§7.1`; `O0021`–`0022`, `J0008` |
| `Q-F01-0012` | `C0008`, `C0015` | `帝アキラ` activates red-eye illegal shield mod against lunar beam, triggering `SYS_CMND//WARNING — ⚠ CHEAT DETECTION / 不正行為を検出` (`FRM-09`) and forced despawn | Ordinary combat defeat without `CHEAT DETECTION` rule-breaking sacrifice | `PDR §2.4`, `§3.3`; `O0023`, `K0019` |
| `Q-F01-0013` | `C0007`, `C0010`, `C0015`, `C0019` | `6.5` s dead silence (`01:47:37`–`01:47:43`) as real-room Kaguya leans on Iroha's back (`彩葉……大好き`); `天の羽衣` turns amber irises cyan-blue (`01:47:54`); **`犬DOGE` leaps onto her skirt (`01:47:56`)** | Continuous concert audio over `01:47:37`–`43`, unchanged eye color, or `犬DOGE` remaining behind in Tokyo | `PDR §2.4`, `§4.2`, `§5.3`; `O0024`–`0025`, `J0009` |
| `Q-F01-0014` | `C0007`, `C0018` | `FRM-10` all-hiragana fridge notes (`めんつゆ…きんし！！` & `かたくりこ`+`れもんじる` pancake tip) contrasted with `FRM-11` `2030/09/12 22:49` polite-keigo remittance `使っちゃった分、かえす！ ご迷惑かけました！` | Absence of debt repayment or absence of register shift into `ご迷惑かけました` | `PDR §2.4`, `§3.2`, `§7.1`; `O0026`, `J0010` |
| `Q-F01-0015` | `C0002`, `C0013`, `C0018` | `FRM-12`: **`2年 3組 12番 酒寄 彩葉`** (`高2`), 1st `東京大学 文科一類`, 2nd `一橋 法 法律` (`法科大学院（弁護士）`); `S0029` phone call: Momiji answers in warm Kansai-ben `ええよ。やってみ。` (`01:52:48`) | `FRM-12` showing 3rd-year (`3年`) enrollment, or Momiji opposing Iroha's change of heart in `S0029` | `PDR §2.5`, `§3.1`, `§7.2`; `O0027`, `O0029`, `J0012` |
| `Q-F01-0016` | `C0002`, `C0012`, `C0015`, `C0018` | `めでたし めでたし` shrinks at `01:51:33.353` into **parody Netflix post-play UI** (`SPECIAL BLACK ONYX 3rd LIVE`, `10秒→6秒`, `FRM-13`); shattered at `01:51:38.650` by Kaguya-inflected `そんなふうに終われるわけ……ないっしょ！！` as Iroha reclaims her career form | Absence of streaming post-play UI shrink or Iroha leaving her Todai law form submitted | `PDR §2.5`, `§5.4`, `§7.1`; `O0028`, `J0011` |
| `Q-F01-0017` | `C0010`, `C0016`, `C0019` | Balcony `Reply` (`AM-05`, `41` cuts) resonates via `犬DOGE`'s bamboo tube on the monochrome Moon; amber-gold returns to Kaguya's eyes; stolen bamboo time-pod strikes meteor shower (`01:54:55`) | Kaguya regaining memory without `Reply`/`犬DOGE`, or landing safely in `2030` without meteor collision | `PDR §2.5`, `§4.2`, `§6.4`; `O0030`, `M0011` |
| `Q-F01-0018` | `C0009`, `C0010`, `C0018`, `C0019` | `FRM-14`: sea-bunny + wired bamboo-shoot lunar core (`CPU/ENERGY/RAM`); 8,000-yr Jōmon→modern montage revealing **Yachiyo = bodiless Kaguya** & **`FUSHI` = sea-bunny + `犬DOGE`**; `FRM-16` (`2003/10/10` `★月に帰りたくなるときもあるよ同盟`) & `FRM-17` (`2005/07/28` `yachi8000` `自分で調べろカス…弥生時代以前の飯くえねえ`) | `S0031` identifying Yachiyo as someone other than crashed Kaguya, or misreading `FRM-14`/`16`/`17` | `PDR §2.5`, `§4.2`, `§7.3`; `O0031`–`0032`, `J0013` |
| `Q-F01-0019` | `C0004`, `C0007`, `C0013`, `C0016` | `12.0` s silent weeping (`02:05:29`–`02:05:41`) → `かぐやと、いたい` → **zero-instrument *a cappella* unison** `大切なメロディは、流れてるよ……あなたの、ハートに……` (`この曲で、生き残れた`) → Yachiyo's wish for warmth (`触れたら、あったかいかな`) & pancakes | Instrumental backing under `02:06:10`–`25`, or absence of Yachiyo's tactile/pancake wish | `PDR §2.5`, `§3.2`, `§6.4`; `O0033`–`0034`, `M0012`, `J0014` |
| `Q-F01-0020` | `C0002`, `C0008`, `C0013`, `C0018` | `[JA#2543]` `（無音のセリフ）` (`FRM-18`); Asahi, Rai & Noi invest (`02:07:53`–`02:08:33`); `FRM-19` lab monitor reads **`Study of real...` / `tactile sensati...` (`触覚の伝達構造`)**; adult Iroha clocks out on time (`休むも仕事！`) | `FRM-19` lacking `触覚` / tactile research text, or adult Iroha still overworked/isolated | `PDR §2.6`, `§3.1`, `§7.4`; `O0035`, `M0013`, `J0015` |
| `Q-F01-0021` | `C0013`, `C0014` | Embodied Kaguya wakes (`うっ、うわ、重〜！`), Iroha notes **`YC型のボディより適合するね`** (`Yachiyo-type` prototype), and says taste awaits next update (`味覚はもうちょいお待ちあれ`) | Absence of `YC型` comparison or Kaguya remaining purely virtual in `2040` | `PDR §2.6`, `§4.2`, `§8.1`; `O0036`, `J0016`, `U0005` |
| `Q-F01-0022` | `C0014`, `C0015`, `C0020` | `FRM-20` (`02:09:48`): **three figures** on lift—weight-bearing **Kaguya & Iroha casting dark floor/wall contact shadows** vs **self-luminous Yachiyo (`ヤッチョは先週ぶり〜`) floating inches above deck without a foot-contact floor shadow** | Yachiyo absent/replaced on the lift, or identical floor-contact shadows across all three | `PDR §2.6`, `§5.5`, `§8.2`; `O0037`, `J0016`, `U0001` |
| `Q-F01-0023` | `C0001`, `C0018` | **Audio Track 1 overrides Track 4 `[SDH]`:** Kaguya (`夏吉ゆうこ`) speaks `[JA#2592]`–`[JA#2594]`, then **Yachiyo (`早見沙織`) speaks `[JA#2595]`–`[JA#2596]` at `02:10:13.722`** despite missing SDH speaker tag; **late title card `超かぐや姫！ COSMIC PRINCESS KAGUYA!`** at `02:10:26.360`–`02:10:33.367` | Single voice actor speaking all of `02:10:03`–`02:10:21`, or different title timestamp | `PDR §2.6`, `§5.1`, `§7.4`; `O0038`, `J0017` |
| `Q-F01-0024` | `C0001`, `C0017`, `C0018` | `FRM-23` confirms **`酒寄朝久 — 鈴村健一`** (completing `朝久`/`朝日` vs `紅葉`/`彩葉` kanji symmetry); `FRM-24` credits `ray 超かぐや姫！Version` & `メルト CPK! Remix` (unsubtitled lyrics in `T4`); post-credits pancake island (`02:19:54`–`02:20:12`) ends on Iroha's **`蛇足ぅ〜！！`** | Different kanji for Tomohisa in `FRM-23`, or omitted post-credits stinger | `PDR §2.6`, `§6.5`, `§7.2`, `§8.3`; `O0039`–`0040`, `M0014`, `J0018` |

---

## 5. Stage-3 receiver acceptance and freeze-integrity receipt (`CPK-B1-SOL61` → `CPK-INT`)

Per [Handoff Contract](../../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) §§3–4 and [CPK_RECONCILIATION_PROFILE.md](../CPK_RECONCILIATION_PROFILE.md) §§1, 7, Stage-3 integration formally accepts the incoming `CPK-B1-SOL61` audit package and bounded `CPK-AVRET-R1` return on the following verified integrity record:

| Field | Verified value |
|---|---|
| Incoming `transfer_id` | `CPK-B1-SOL61-TO-INTEGRATOR-20261112` ([CPK_F01_RECEIVING_HANDOFF.md](CPK_F01_RECEIVING_HANDOFF.md)) |
| Stage-2 producer | OpenAI `gpt-5.4` (owner-designated `"Sol 6.1"`) at `xhigh` / Max reasoning (`BUNDLE_MEDIATED`: `3,006` frames, `372` sheets, complete Japanese `0:s:3` `[SDH]` + English `0:s:0` subtitles; `audio_inspection = UNAVAILABLE`) |
| Stage-3 roles & explicit owner disclosure | Under explicit owner authorization (`A1`), **Gemini 4 Carbon** (`High` thinking effort, Antigravity Windows harness) executed both **Stage 3A** (`1 of 1` bounded primary continuous-AV return `CPK-AVRET-R1` in [CPK_F01_PRIMARY_AV_RETURN.md](CPK_F01_PRIMARY_AV_RETURN.md)) and **Stage 3B** (Owner-Designated Integrator `CPK-INT`), disclosed per [CPK_RECONCILIATION_PROFILE.md](../CPK_RECONCILIATION_PROFILE.md) §1 |
| Three-way commit comparison | Reviewed `main`: `46c341663e7e0b78d75fe9e2b3dc6e83859f85db`; `CPK-R1` primary freeze commit (`comparison_v1_boundary` / PR #542): `7c850af679471b74e36a8458985e448bc8191068`; retrospective publication-envelope governance commit (PR #549 on `agent/governance`): `75457666e714a59b0c3e4f7d2b57203bd1cd84b8`; **`baseline_drift: false`** |
| Witness & clock parity | Identical `CPK-W01-NF-WEBRIP-HEVC` (`4,916,885,885` B, SHA-256 `b940eede5e3ce2e83e507a33e6523516c21e770dbccd8cc9e4461af77b23a42a`, `8523.207` s) and `CPK-CLK-F01-GLOBAL` (`0.000` s drift across `CAL-01`–`CAL-07` and `AV-01`–`AV-10`) |
| **Phase A blind benchmark freeze** | Frozen `2026-11-12T04:50:06.676495+00:00` (archival commit `e4caeb931dbb91c9b926638cf511f50637b0bb79`, `12` archival files / `16` published envelope files; `blind_to_gemini: true`, `blind_to_neutral_queue: true`). Archival manifest SHA-256 `67d16bc1a88fa6672f24c0f7cdf9c3002a0bd946aeafc8d7058c1c407d1448e7`; content-tree SHA-256 `9934c0f4a0309a134bea39bf62a52db8016b95291cc4e817f90b380a1cdde643`; standalone monograph ([CPK_B1_SOL61_MONOGRAPH.md](../independent/CPK-B1-SOL61/readings/CPK_B1_SOL61_MONOGRAPH.md)) original `34,010` B (`8577bf06ded087b10bde23872e4598cba16c842c7ee5b6e753623f7ec1e89491`) → sanitized repo derivative `34,063` B (`bd7ea4ccc1ad586fbce015338ffee4a54690b8e88e9f9b0084107018db1ec828`, `100%` body-identical after frontmatter normalization) |
| **Phase B2 blind observation freeze** | Frozen `2026-11-12T05:11:59.269628+00:00` (`5` files, `blind_order_achieved: true`, prior to Set-2 exposure). Freeze manifest SHA-256 `19b5c74de3ad47317d2de11f50f798fa6d25965cc79426835b7980ca54bd184a`; content-tree SHA-256 `a60c3890bb150fa15a32347a579c084eddf03654436985ca1509c16bd452cff0`; `CPK_F01_BLIND_OBSERVATIONS.md` original `39,179` B (`859ab1a0b5c6004fdafaff44d5c2d8bbe1c98517c5dea3f6b1079b09b90cbebe`) → sanitized repo derivative `39,210` B (`82aa915cec6f440a6d9f0660a40ee05a3c124039d23a4ba128007769636725be`) |
| **Post-exposure comparison freeze** | Frozen `2026-11-12T05:54:23.345950+00:00` (archival commit `8ed04470ecd9f7adaf0a130728748dec6da6c314`, `20` files, `614,204` B). Freeze manifest SHA-256 `5b76d0dd186080860bbe3e854feec7297634424f3d51697155f8a6697e1c96d7` (`4,604` B); content-tree SHA-256 `302c15f20e357a4aee38645432d8a644376a03f98e245a167aa47c5d97a01f54`; all `39` non-entrypoint repo payload files (`16` under `independent/CPK-B1-SOL61/` + `23` under `audits/`) verified byte-for-byte |
| Steward note on frozen `CPK_F01_BLIND_INPUT_PACKET.md` (`v1.0`) | Preserved byte-for-byte at `21,403` B (`807784579986a87afea5da5ce0bdf1921d803a6be5e81baed72662da91b7c2a2`). Two non-mutating errata are recorded here: (1) §1's allowlist text displayed legacy `00_governance/` path strings instead of live `governance/` paths; (2) as audited in `SA13`, listing primary-selected `FRM-01`–`FRM-29` targets and event-specific phrasing in `Q-F01-0008`/`0018` carried partial thematic cueing, which `CPK-B1-SOL61` neutralized by freezing Phase A prior to reading the packet |

---

## 6. Bounded `1 of 1` primary continuous-AV return receipt (`CPK-AVRET-R1`)

All `10` continuous-AV verification requests queued in [CPK_F01_RECEIVING_HANDOFF.md](CPK_F01_RECEIVING_HANDOFF.md) §3 (`AV-01`–`AV-10`) were executed in a single pass (`1 of 1`) in [CPK_F01_PRIMARY_AV_RETURN.md](CPK_F01_PRIMARY_AV_RETURN.md) (`v1.0`) across `25` full-frame-rate (`24000/1001 fps`) clips (`AVRET-01A`–`10A`), `32` lossless `1920x1080` frames (`AVFRM-01A`–`10B`), `2` `3x` crops (`AVCROP-09B-1/2`), stream-complete raw `0:s:3` cues (`[JA#0001–2716]`), and `82` native `5.1` PCM acoustic windows (`AM-01`–`AM-06`):

| Request ID | Target interval & question | Verified outcome (`CPK-AVRET-R1`) | Downstream impact |
|---|---|---|---|
| `AV-01` | `00:00:00–00:01:25` pre-roll & cut | Netflix distributor/original animation cards (`00:00:01–00:00:11`, no film title); diegetic world-disc at `00:00:13.013`; `[JA#0001]` `月見(るなみ)ヤチヨ` (`00:00:26.026`); hard cut at `00:01:20.956` (`scdet = 71.0`); main title card silent at `02:10:26.360–02:10:33.367` | Revises `C0001`, `C0015`, `C0018` (`P001`) |
| `AV-02` | `00:07:33–00:07:49` vs `01:38:44–01:39:15` | `00:07:33–00:07:49` confirmed **true unaccompanied `FC` solo** (`-31.98 dBFS`; `FL/FR = -61.82/-62.55 dBFS`, `AM-02`); `01:38:44–01:39:10` has **sustained keyboard/synth pad** (`FL/FR = -29.88/-30.25 dBFS`) where Kaguya first says `[JA#2083]` `同じメロ？` (`01:39:09.61`) | Preserves `M0002`; revises `C0004`, `C0016` |
| `AV-03` | `01:53:48–01:54:25` Moon-side `Reply` | **Refutes `CPK-R1` Moon-side bamboo tube**: `AVFRM-03A/B/C` show Kaguya holding **only `犬DOGE`** directly in both arms; `Reply` arrives by unstated cross-spatial resonance (`U0002` `OPEN`) | Revises `C0010`, `C0019` (`P024`); updates `U0002` |
| `AV-04` | `01:25:10–01:25:34` subway AR visibility | Confirmed (`AVFRM-04A`): unaugmented subway commuters show zero reaction to overhead `月人` fleet (`2030/09/12`), proving Tsukuyomi smart-contact AR selectivity | Preserves `O0022`, `C0011` (`P017`) |
| `AV-05` | `01:44:24–01:44:38` & `02:07:38–02:07:45` `帝アキラ` | `CHEAT DETECTION` (`01:44:27`) forces raid-session ejection only; **`帝アキラ` appears intact in Tsukuyomi at `02:07:40.285` (`AVFRM-05A`, `[JA#2548]`)** | Revises `C0008` (`P015`); resolves `U0007` |
| `AV-06` | `01:47:30–01:48:05` & `01:51:32–01:52:55` | `01:47:38–01:47:42` drops to **`-107.45 dBFS` all-channel digital silence** (`4.1 s` strict / `~6.05 s` perceptual hush between `[JA#2266]` and `[JA#2267]`); post-play UI runs **`~6.006 s` (`144` frames, `01:51:33.353–01:51:39.359`, `10→5 s`)**; `[JA#2333]` is muted under wind (`U0009`) before `[JA#2334]` `ええよ やってみ` | Preserves `C0012` (`~6.0 s`); refines `C0015`; logs `U0009` |
| `AV-07` | `01:17:15–01:18:10`, `01:38:35–01:39:25`, `01:52:55–01:53:20` | `01:17:23` `.wav` (`2020/01`) has **no verbalized recognition**; `01:38:44` is **unfinished `1コーラス` `Reply`** (`[JA#2083]` `同じメロ？`); `Reply` is **completed at `01:53:04.74`** (`[JA#2340]` `できた`, `AVFRM-07C`) | Revises `C0004`, `C0016` (`P018`, `P023`); keeps `U0003` `OPEN` |
| `AV-08` | `02:10:34–02:19:53` end-credit cues & visuals | Retracts `CPK-R1`'s `"unsubtitled"` premise: raw `0:s:3` carries **`111` timed lyric cues (`[JA#2599–2709]`)** (`63` `ray` + `48` `メルト`) over `28` + `27` monochrome `原画` key drawings | Rejects/repairs `C0017` (`P029`–`P031`); resolves `U0008` |
| `AV-09` | `02:05:45–02:06:30` & `02:09:44–02:09:58` | `02:05:48.5–02:06:16.5` is **zero-instrument `FC` solo call-and-response** (`Iroha` `[JA#2528–2530]` → `Yachiyo` `[JA#2531–2533]`, `FL/FR = -59.58/-58.88 dBFS`), NOT simultaneous unison; piano enters at `02:06:16.5` (`[JA#2534]`). `FRM-20` (`02:09:48.55`) confirms `Iroha`/`Kaguya` floor-contact shadows vs self-luminous floating `Yachiyo` | Revises `C0016` (`P032`); **strengthens `C0020`** (`P033`) |
| `AV-10` | `02:10:02–02:10:34` closing narration & title | `[JA#2592–2594]` tagged `（かぐや）`; `[JA#2595–2597]` (`02:10:13.722–02:10:21.359`) **untagged in Track 4** (`ひとまず めでたし めでたしってことで`) — speaker held **`OPEN` (`CPK-INT-U0010`)** per Method §6; silent title card `02:10:26.360–02:10:33.367` | Revises `C0001`, `C0018` (`P034`); logs `U0010` |

---

## 7. Protocol §5.4 machine-readable reconciliation summary

```yaml
av_reconciliation:
  protocol_route: MIRROR_PRIMARY_CONTINUOUS_AV_TO_BLIND_BUNDLE_VERIFIER
  witness_id: CPK-W01-NF-WEBRIP-HEVC
  witness_sha256: b940eede5e3ce2e83e507a33e6523516c21e770dbccd8cc9e4461af77b23a42a
  duration_seconds: 8523.207
  clock_id: CPK-CLK-F01-GLOBAL
  residual_clock_drift_seconds: 0.000
  calibration_anchors_verified: 7
  primary_run:
    run_id: CPK-R1
    model: "Gemini 4 Carbon (High thinking effort)"
    lane: CONTINUOUS_AV
    frozen_commit: 7c850af679471b74e36a8458985e448bc8191068
    candidate_sha256: cf7c64d7f4e70d8bfbbc8d97652e40c99de115e5bd9958e4f620197c70a47c3c
    effective_visual_sampling_fps: 1.0
    targeted_reinspection_fps: 23.976
  verifier_run:
    run_id: CPK-B1-SOL61
    model: "OpenAI gpt-5.4 (Sol 6.1, xhigh reasoning)"
    lane: BUNDLE_MEDIATED
    audio_inspection: UNAVAILABLE
    bundle_clean_frames: 3006
    bundle_contact_sheets: 372
    subtitle_cues_ja_sdh: 2716
    phase_a_blind_to_gemini: true
    phase_a_blind_to_neutral_queue: true
    phase_b2_blind_order_achieved: true
    phase_a_publication_manifest_sha256: 8c70dffeb953fc222706c9585df38e1cd3128d0395a9f0f268ce7c21645cadfc
    phase_b2_blind_observations_sha256: 82aa915cec6f440a6d9f0660a40ee05a3c124039d23a4ba128007769636725be
  bounded_av_return:
    run_id: CPK-AVRET-R1
    pass_count: "1 of 1"
    requests_queued: 10
    requests_resolved: 10
    clips_inspected: 25
    lossless_frames_extracted: 34
    pcm_5_1_windows_measured: 82
    second_independent_escalation_required: false
  integrator_run:
    run_id: CPK-INT
    dual_role_owner_authorized: true
    baseline_drift: false
  registered_claim_denominators:
    total_claimed: 20
    audited: 20
    unaudited: 0
    transitions:
      PRESERVE: 3
      STRENGTHEN: 1
      REVISE: 14
      DOWNGRADE: 1
      REJECT: 1
      OPEN: 0
  scoped_prose_assertion_denominators:
    total_scoped: 35
    audited: 35
    transitions:
      PRESERVE: 12
      STRENGTHEN: 1
      REVISE: 16
      DOWNGRADE: 2
      REJECT: 3
      OPEN: 1
  verifier_own_claim_denominators:
    total_sol61_claims: 28
    self_audit_items_applied: 14
    accepted_into_synthesis_with_sa_bounds: 28
  contested_convergences_adjudicated: 10
  integrated_canonical_claims_registered: 12
  open_and_bounded_questions:
    total_tracked: 10
    open_source_unspecified: 8
    resolved_by_av_return: 2
  unresolved_required_debts: 0
```

---

## 8. Handoff §15.6 editorial and referential-clarity verification (`CPK_F01_INTEGRATED_SYNTHESIS.md`)

Prior to accepting [synthesis/CPK_F01_INTEGRATED_SYNTHESIS.md](../synthesis/CPK_F01_INTEGRATED_SYNTHESIS.md) (`v1.0`), a bounded name, pronoun, speaker, and disclosure-horizon check ([Handoff Contract](../../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md) §15.6) was executed across `§§2.1–2.3` (opening/false-ending/coda framing), `§§3.1–3.3` (all consequential family, peer, fraternal, and administrative dyads), `§§4.1–4.3` (virtual/real and `2040` three-figure staging), `§5` (six-stage musical trajectory), and `§§6–8` (registers, governing thesis, and rival readings):

- **`KNOWLEDGE_BOUNDARY_REQUIRED`**: Preserved `いろP` prior to `00:35:06`, `帝アキラ` distinct from `酒寄朝日` prior to `00:58:53`, and `月見(るなみ)ヤチヨ` distinct from crashed `8,000`-year `かぐや` prior to `01:57:04`.
- **`SOURCE_REQUIRED_ANONYMITY` & `OPEN` speaker discipline**: Preserved uncredited subway commuters (`AVFRM-04A`) and held untagged closing narrator `[JA#2595–2597]` (`02:10:13.722–02:10:21.359`) explicitly `OPEN` (`CPK-INT-U0010`) rather than assigning speaker identity from vocal timbre alone.
- **Defect counts**: `UNNECESSARY_GENERICIZATION = 0`, `AMBIGUOUS_REFERENT = 0`, `INCORRECT_IDENTITY_OR_ATTRIBUTION = 0`.

---

## 9. Complete post-reconciliation write-through and immutable preservation manifest

Self-referential SHA-256 of this `CPK_F01_RECONCILIATION_RECORD.md` (`v1.1`) is recorded directly by the enclosing Git commit tree. Every other canonical, return, and frozen file in `series/cosmic-princess-kaguya/` has been verified on disk at the exact byte counts and SHA-256 digests below:

### 9.1 Created and updated Stage-3 canonical & return files (`10` files + this record)

| Repository path | Artifact ID & version | Status | Exact bytes | Exact SHA-256 |
|---|---|---|---|---|
| `series/cosmic-princess-kaguya/CURRENT_STATE_AND_CORPUS_MAP.md` | `CURRENT_STATE_AND_CORPUS_MAP` `v1.5` | `canonical` | `10516` | `f556fb1150c53956a556ec17dddd2e11d4b2134f981df7a28ad8768942a3d7f3` |
| `series/cosmic-princess-kaguya/audits/CPK_F01_R1_ERRATUM.md` | `CPK_F01_R1_ERRATUM` `v1.1` | `superseded` | `12607` | `6bdf460e2bd0bc0799d422af3660a20f05be8b2d5c74eccdabfbba5b293d5242` |
| `series/cosmic-princess-kaguya/CPK_ANALYTICAL_METHOD.md` | `CPK_ANALYTICAL_METHOD` `v1.1` | `canonical` | `21325` | `2ccd972d504f1115630791e4efee8494e458ce60d6d7415760bbedfb83826d0a` |
| `series/cosmic-princess-kaguya/CPK_SYNTHESIS_ARCHITECTURE.md` | `CPK_SYNTHESIS_ARCHITECTURE` `v1.1` (`MATURE`) | `canonical` | `29745` | `56f41f4312676ae60dd3c9d2f34171be5e3d4b6dab1fa057ea643a65f90d1df2` |
| `series/cosmic-princess-kaguya/CPK_RECONCILIATION_PROFILE.md` | `CPK_RECONCILIATION_PROFILE` `v1.1` | `canonical` | `18252` | `c974764b1f1da51b3a2f6188a4ab3920f907d02546cdb5e6ce856c2b6287a63a` |
| `series/cosmic-princess-kaguya/CPK_SOURCE_INVENTORY.md` | `CPK_SOURCE_INVENTORY` `v1.2` | `canonical` | `42354` | `8fd473cf1f042d5aa782fbc43a78ef1e5cafe08fe9ae2bddde539d02f56d70fc` |
| `series/cosmic-princess-kaguya/CPK_OBSERVATION_LEDGER.md` | `CPK_OBSERVATION_LEDGER` `v1.2` | `canonical` | `113976` | `5f50d2ebb38d9c5f71c569c43735ff1476affada4822bbdedba724c369e83b77` |
| `series/cosmic-princess-kaguya/CPK_CHARACTER_RELATIONSHIP_LEDGER.md` | `CPK_CHARACTER_RELATIONSHIP_LEDGER` `v1.2` | `canonical` | `86662` | `2a74553acad827cf1511e5ae2cf5ecd82eb89852b71277e2fa4e58c6d325f04c` |
| `series/cosmic-princess-kaguya/CPK_CLAIM_REVISION_LEDGER.md` | `CPK_CLAIM_REVISION_LEDGER` `v1.2` | `canonical` | `94490` | `f1448521986c58bf75f081b8c386270f755295468e098d40b98e0d630f5a8f64` |
| `series/cosmic-princess-kaguya/audits/CPK_F01_PRIMARY_AV_RETURN.md` | `CPK_F01_PRIMARY_AV_RETURN` `v1.0` | `draft_noncurrent` | `72291` | `5f942482993d37ef3a1a9abf098a30b309450f9adecefd5db1e55bfa5636e64f` |
| `series/cosmic-princess-kaguya/synthesis/CPK_F01_INTEGRATED_SYNTHESIS.md` | `CPK_F01_INTEGRATED_SYNTHESIS` `v1.0` | `canonical` | `42714` | `ce42935ff75c0b891824ed6f73ef3ba6bfc2998c33c2d187798ca3e0cfe48319` |

### 9.2 Key preserved noncurrent `CPK-B1-SOL61` benchmark & audit files (`39` total files verified unchanged; key index below)

*(Frozen `CPK-R1` files in §§2.1–2.2—`readings/CPK_F01_PRIMARY_DEEP_READING.md` at `86,421` B / `cf7c64d7...`, `audits/CPK_F01_BLIND_INPUT_PACKET.md` at `21,403` B / `80778457...`, and `CPK_BOOTSTRAP_REVIEW.md` at `7,381` B / `a0a03765...`—remain byte-for-byte identical to `7c850af679471b74e36a8458985e448bc8191068`.)*

| Repository path | Artifact & scope | Status | Exact bytes | Exact SHA-256 |
|---|---|---|---|---|
| `series/cosmic-princess-kaguya/independent/CPK-B1-SOL61/PUBLICATION_MANIFEST.json` | `PUBLICATION_MANIFEST` (`16`-file Phase A envelope) | `draft_noncurrent` | `12111` | `8c70dffeb953fc222706c9585df38e1cd3128d0395a9f0f268ce7c21645cadfc` |
| `series/cosmic-princess-kaguya/independent/CPK-B1-SOL61/readings/CPK_B1_SOL61_MONOGRAPH.md` | `CPK_B1_SOL61_MONOGRAPH` `v1.0` | `draft_noncurrent` | `34063` | `bd7ea4ccc1ad586fbce015338ffee4a54690b8e88e9f9b0084107018db1ec828` |
| `series/cosmic-princess-kaguya/audits/CPK_F01_BLIND_OBSERVATIONS.md` | `CPK_F01_BLIND_OBSERVATIONS` `v1.0` | `draft_noncurrent` | `39210` | `82aa915cec6f440a6d9f0660a40ee05a3c124039d23a4ba128007769636725be` |
| `series/cosmic-princess-kaguya/audits/CPK_F01_CLAIM_AUDIT.md` | `CPK_F01_CLAIM_AUDIT` `v1.0` | `draft_noncurrent` | `79054` | `87e0ae0b5443f2870f4fee6d040ab0f16282ec59f9e37553d367e13461e88778` |
| `series/cosmic-princess-kaguya/audits/CPK_F01_SELF_AUDIT.md` | `CPK_F01_SELF_AUDIT` `v1.0` | `draft_noncurrent` | `14702` | `4cb2823dbaa25512c0be4e469be92a1984ecf9eafeecb4ef9675f10298eb49fc` |
| `series/cosmic-princess-kaguya/audits/CPK_F01_COMPARATIVE_EVALUATION.md` | `CPK_F01_COMPARATIVE_EVALUATION` `v1.0` | `draft_noncurrent` | `13265` | `0579b2e6b93fd43bc16c6baad9a1d8a37eaa8135eff318170ca7b8c20336d95e` |
| `series/cosmic-princess-kaguya/audits/CPK_F01_RECEIVING_HANDOFF.md` | `CPK_F01_RECEIVING_HANDOFF` `v1.0` | `draft_noncurrent` | `19440` | `0ee24fdef2addfc2f8d9a5bf4bb1219b75eea5cea45b14816bd1e5f32abc7246` |
| `series/cosmic-princess-kaguya/audits/CPK-B1-SOL61/CPK_F01_AUDIT_DECISIONS.json` | `CPK_F01_AUDIT_DECISIONS` (`20` claims) | `draft_noncurrent` | `31100` | `af2bd388b71dc1f5b434e595c2fcbb668c6829c90195498b3aa155e51a0b0c47` |
| `series/cosmic-princess-kaguya/audits/CPK-B1-SOL61/CPK_F01_PROSE_AUDIT_DECISIONS.json` | `CPK_F01_PROSE_AUDIT_DECISIONS` (`P001`–`P035`) | `draft_noncurrent` | `26999` | `4ee202b1b0924271c138edaee0c65f532484c702edb0695cb5a89bc6cc70ddaa` |
| `series/cosmic-princess-kaguya/audits/CPK-B1-SOL61/PUBLICATION_REVIEW_RECEIPT.json` | `PUBLICATION_REVIEW_RECEIPT` | `draft_noncurrent` | `6635` | `1517f36e9ae6edd8ae75d62d1e9f15c6f6a0693efc72365d7052705a03d2a84b` |
