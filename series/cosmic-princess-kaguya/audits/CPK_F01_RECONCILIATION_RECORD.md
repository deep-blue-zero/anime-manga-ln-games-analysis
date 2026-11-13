---
title: "Cosmic Princess Kaguya! (F01) — primary freeze, stage handoff, and mirror reconciliation record"
series: cosmic-princess-kaguya
artifact_id: CPK_F01_RECONCILIATION_RECORD
artifact_type: audiovisual_reconciliation_record
stage_state: READY_FOR_HANDOFF
generation: CPK-G1
version: "1.0"
status: draft_noncurrent
authority_scope: "Primary CPK-R1 candidate freeze manifest, Handoff Contract transfer record, withheld post-freeze adjudication mapping, and mirror-reconciliation tracking home; zero executed verifier adjudications"
source_boundary: "Admitted Japanese feature witness CPK-W01-NF-WEBRIP-HEVC (F01, 00:00:00.000-02:22:03.207); primary continuous-AV candidate frozen; blind bundle audit not yet executed"
canonical_home: series/cosmic-princess-kaguya/audits/CPK_F01_RECONCILIATION_RECORD.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
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

## 5. Mirror-reconciliation execution log (post-freeze stage tracker)

Per [CPK_RECONCILIATION_PROFILE.md](../CPK_RECONCILIATION_PROFILE.md) §7, zero post-freeze verifier or integrator counts are fabricated prior to actual stage execution:

| Reconciliation stage / metric | Current recorded status |
|---|---|
| Primary `CONTINUOUS_AV` candidate freeze (`CPK-R1`) | **`FROZEN`** (`2026-11-11`; hashes recorded in §2.2 above) |
| Blind verifier receipt & `CPK_F01_BLIND_OBSERVATIONS.md` freeze | `NOT_YET_EXECUTED` (assigned to separate fresh-context OpenAI `BUNDLE_MEDIATED` session) |
| `blind_order_achieved` | `PENDING_VERIFIER_EXECUTION` |
| Post-exposure claim audit (`CPK_F01_CLAIM_AUDIT.md`) | `NOT_YET_EXECUTED` (`claimed: 20`, `audited: 0`, `unaudited: 20`; `PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN` = `UNEXECUTED`) |
| Bounded primary-AV return / independent verification escalations | `NOT_YET_EXECUTED` |
| Integrator write-through & `synthesis/CPK_F01_INTEGRATED_SYNTHESIS.md` | `NOT_YET_EXECUTED` (gated on blind audit, longitudinal reconciliation, and role-gap/convergence review) |
