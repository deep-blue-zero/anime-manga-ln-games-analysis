---
title: "Cosmic Princess Kaguya! (F01) — post-audit erratum and audit-completion notice for primary snapshot CPK-R1"
series: cosmic-princess-kaguya
artifact_id: CPK_F01_R1_ERRATUM
artifact_type: analytical_erratum
generation: CPK-G1
version: "1.2"
status: superseded
authority_scope: "Historical archive-integration erratum and audit-completion notice from PR #542; preserved in body and superseded as current audit-qualification record by CPK_F01_RECONCILIATION_RECORD.md (v1.1) alongside the v1.2 cumulative ledgers and canonical integrated synthesis"
source_boundary: "Admitted Japanese feature witness CPK-W01-NF-WEBRIP-HEVC (F01, 00:00:00.000-02:22:03.207; Japanese Audio Track 1 0:a:0; Japanese [SDH] Subtitle Track 4 0:s:3); records CPK-B1-SOL61 and the CPK-AVRET-R1 bounded return, with official character paratext cited for Iroha’s age"
canonical_home: series/cosmic-princess-kaguya/audits/CPK_F01_R1_ERRATUM.md
supersedes: []
superseded_by:
  - series/cosmic-princess-kaguya/audits/CPK_F01_RECONCILIATION_RECORD.md
do_not_use_as_current_authority: true
do_not_use_as_literary_evidence: true
---

# Post-audit erratum and audit-completion notice (`CPK-R1`, `F01`)

## 1. Purpose and staging boundary ([Pre-Commit Guidance](../../../governance/policies/CHANGE_INTEGRATION_CHECKLIST.md))

This erratum qualifies the pre-audit `CPK-R1` snapshot frozen at commit `7c850af679471b74e36a8458985e448bc8191068` so that [readings/CPK_F01_PRIMARY_DEEP_READING.md](../readings/CPK_F01_PRIMARY_DEEP_READING.md) (`v1.0`, `draft_noncurrent`) and its accompanying pre-audit `v1.1` ledgers ([CPK_SOURCE_INVENTORY.md](../CPK_SOURCE_INVENTORY.md), [CPK_OBSERVATION_LEDGER.md](../CPK_OBSERVATION_LEDGER.md), [CPK_CHARACTER_RELATIONSHIP_LEDGER.md](../CPK_CHARACTER_RELATIONSHIP_LEDGER.md), and [CPK_CLAIM_REVISION_LEDGER.md](../CPK_CLAIM_REVISION_LEDGER.md)) can enter the repository archive with the documented corrections and evidence limits below.

- **Frozen `CPK-R1` records.** [CPK_RECONCILIATION_PROFILE.md](../CPK_RECONCILIATION_PROFILE.md) §§2, 7 and the [Archive Authority Policy](../../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md) govern subsequent reconciliation. The primary candidate (SHA-256 `cf7c64d7f4e70d8bfbbc8d97652e40c99de115e5bd9958e4f620197c70a47c3c`) and the snapshot hashes in [CPK_F01_RECONCILIATION_RECORD.md](CPK_F01_RECONCILIATION_RECORD.md) §2.2 remain fixed at their `comparison_v1_boundary`.
- **Stage-3 publication.** Review of the prepared `v1.2` ledgers, `CPK-B1-SOL61` artifacts, bounded AV return and integrated synthesis is a subsequent step. Import requires this primary `F01` completion and the owner-approved publication-envelope binding ([PR #549](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/549)) on `main`.

---

## 2. Completed independent audit (`CPK-B1-SOL61`) and bounded AV return (`CPK-AVRET-R1`)

Both post-freeze passes recorded below were completed on 2026-11-12 against `CPK-W01-NF-WEBRIP-HEVC` (SHA-256 `b940eede5e3ce2e83e507a33e6523516c21e770dbccd8cc9e4461af77b23a42a`). The `CPK-B1-SOL61` execution profile records Sol6.1 with Max reasoning as the requested configuration. The actual backend model and reasoning setting were unverified.

| Independent phase | Scope | Original local freeze manifest (SHA-256) |
|---|---|---|
| A, packet-free benchmark | The independent reading froze before exposure to the question packet or the primary interpretation. | `2026-11-12T04:50:06.676495Z` · `INDEPENDENT_FREEZE_MANIFEST.json` · `67d16bc1a88fa6672f24c0f7cdf9c3002a0bd946aeafc8d7058c1c407d1448e7` |
| B2, question-directed observations | The verifier answered 24 questions before reading the primary claims. Q22 supplied the figure count and Q13, Q16 and Q17 presupposed events. | `2026-11-12T05:11:59.269628Z` · `BLIND_FREEZE_MANIFEST.json` · `19b5c74de3ad47317d2de11f50f798fa6d25965cc79426835b7980ca54bd184a` |
| Post-exposure comparison | The verifier audited all 20 registered claims, 35 additional prose assertions and 14 self-audit items. | `2026-11-12T05:54:23.345950Z` · `COMPARISON_FREEZE_MANIFEST.json` · `5b76d0dd186080860bbe3e854feec7297634424f3d51697155f8a6697e1c96d7` |

The B2 observations in that freeze are 39,179 bytes (SHA-256 `859ab1a0b5c6004fdafaff44d5c2d8bbe1c98517c5dea3f6b1079b09b90cbebe`). The publication inventory and the publication copy of the observations have their own digests. The [historical question packet](CPK_F01_BLIND_INPUT_PACKET.md) also uses legacy `00_governance/` paths and prefix-only hashes for some derivatives. Consequential static checks used exact file/time locators and source re-extractions.

**Actual `BUNDLE_MEDIATED` inspection.** Phase A examined 127 of 274 contact sheets (2,525 displayed thumbnail slots) and opened 29 source frames individually. The verifier read all 2,716 Japanese SDH cues (`0:s:3`) and cross-checked 79 selected pairings with English (`0:s:2`). B2 added 58 source PNG views and 18 bundle JPEG views. The post-exposure comparison checked 13 further PNGs in 960×540 tiles. These views overlap in source time. The execution record flags 326 late cue-to-sheet index mismatches. Audio heard and continuous video viewed were both 0 seconds (`audio_inspection = UNAVAILABLE`). The verifier sent ten bounded `CONTINUOUS_AV` requests (`AV-01`–`AV-10`).

**Self-audit and comparison.** The verifier recorded its own bracelet omission (`SA01`), missed family-name pattern (`SA03`), possible late speaker change (`SA06`), coda ambiguity (`SA08`), and limits of B2 cueing (`SA13`) and runtime provenance (`SA14`). The fever scene preceding `KASSEN` is a correction to the primary chronology (`PE02`, revisited by `AV-03`). The independent comparison proposed 3 `PRESERVE`, 1 `STRENGTHEN`, 12 `REVISE`, 1 `DOWNGRADE`, 1 `REJECT` and 2 `OPEN` dispositions for the 20 registered claims.

**Bounded primary AV return (`CPK-AVRET-R1`).** The primary analyst reported results for `AV-01`–`AV-10` using 25 clips, 32 stills and two crops, Japanese SDH and 82 sampled native 5.1 PCM windows from `0:a:0`. The clips use a file encoding rate of `24000/1001` fps. The independent follow-up checked selected stills and PCM measurements. The reported AV findings and the independent proposals inform the later reconciliation. The closing speaker and other unresolved questions retain the limits stated in §3.

---

## 3. Source corrections and qualifications on `CPK-R1` (`v1.0` / `v1.1`)

Readers consulting [CPK_OBSERVATION_LEDGER.md](../CPK_OBSERVATION_LEDGER.md), [CPK_CHARACTER_RELATIONSHIP_LEDGER.md](../CPK_CHARACTER_RELATIONSHIP_LEDGER.md), [CPK_CLAIM_REVISION_LEDGER.md](../CPK_CLAIM_REVISION_LEDGER.md), [CPK_SOURCE_INVENTORY.md](../CPK_SOURCE_INVENTORY.md) (all `v1.1`) or the [frozen primary reading](../readings/CPK_F01_PRIMARY_DEEP_READING.md) (`v1.0`) should apply the following corrections and limits. `JA#` denotes a cue from Japanese SDH (`0:s:3`).

| Affected `CPK-R1` records | Correction or qualification |
|---|---|
| `S0031`, `O0031`, `K0021`, `C0009`, `C0010`, `C0019` | The flashback reports that the craft struck a large rock (`JA#2408`). At `01:58:27–01:58:39`, `JA#2414–2417` distinguish `犬DOGE`, who acquired a body, from Kaguya, who could interact with the world through the `ウミウシ`. The cues leave any fusion mechanism and its relation to `FUSHI` unestablished. |
| `S0030`, `O0030`, `M0011`, `C0010`, `C0019`, `U0002` | `AV-06` reports Kaguya holding `犬DOGE` in the Moon sequence (`01:53:48–01:54:25`), with no visible bamboo tube there. How `Reply` reaches her remains `OPEN` (`U0002`). |
| `S0035`, `O0039`, `M0014`, `C0017`, `U0008`, source inventory §3.1 | The Track 4 extract has 111 consecutive credit-music cues (`JA#2599–2709`), including four standalone music markers. The cues carry timed Japanese lyrics for both songs (`AV-10`). Withdraw `U0008`'s missing-subtitle premise. Reassess `C0017`'s broader cultural claim independently of that premise. |
| `S0001`, `O0001`, `O0038`, `J0001`, `J0017`, `C0001`, `C0015`, `C0018` | Netflix cards precede the first scene (`AV-01`). `JA#0001` (`00:00:26`) glosses `月見(るなみ)ヤチヨ`. `JA#2592` tags Kaguya, while the subsequent untagged closing address and title prompt (`JA#2595–2598`, `02:10:13–02:10:26`) leave speaker identity `OPEN` under [the analytical method](../CPK_ANALYTICAL_METHOD.md) §6. The film title card follows (`AV-08`). |
| `M0002`, `M0008`, `M0010`, `M0012`, `C0004`, `C0016`, `U0003` | `AV-02` reports a centre-dominant opening vocal and soft backing in the unfinished `Reply` segment. The one-chorus decision (`JA#2136`, `01:38:44`) and the melodic recognition (`JA#2144`, `01:39:09`) precede completion (`JA#2338`, `01:53:04`). The `.wav` discovery alone leaves the melodic first origin `OPEN` (`U0003`). The reprise around `02:05:48` has successive lines, including a spoken Yachiyo aside (`JA#2530`) before Iroha's singing (`JA#2531–2533`). Sampled centre-channel dominance supports vocal isolation at the measured points. |
| `S0005`, `O0010`, `K0019`, `C0002`, `C0003`, `C0005` | Kaguya reads *Taketori* on a tablet (`00:13:38`). Iroha describes reaching a compromise by paying her own tuition and living costs (`JA#1092–1093`). Her later account distinguishes what she wanted to say from what she held back (`JA#2027–2029`). Roka and Mami share the work of care. Kaguya's spending breaches coexist with the rice-porridge fever care, which precedes `KASSEN` (`PE02`, `AV-03`). |
| `S0014`–`S0016`, `O0016`–`O0017`, `C0006`, `C0008` | The rules specify 3-on-3 (`JA#1206`) and Yachiyo substitutes for Mami (`JA#1240–1244`). Black onyX wins the match (`JA#1546`, `01:10:28`). The separate Cup award goes to Kaguyairo-P for gaining the most fans during the event (`JA#1565`, `JA#1570`, `01:11:15–01:11:37`). The later domestic `Happy Synthesizer` montage cannot explain that earlier award (`AV-03`). |
| `S0025`, `O0023`, `C0008`, `U0007` | `帝アキラ` is visible again in Tsukuyomi (`AVFRM-04D`, `02:07:40`). That reappearance bounds the earlier `CHEAT DETECTION` outcome. The warning is visible at `01:45:56` (`FRM-09`). The duration and terms of the penalty remain unclear. `JA#2548` concerns the investment request. |
| Iroha's age, source inventory §5 and the character timeline | The film's school roll `2年3組12番` establishes year, class and roster position. The production's official character profile gives Iroha's age as 17 (`17歳の女子高生。`). This is production metadata for the main-story character. Ages 7 and 27 at the other points in the timeline are inferences. [Official character profile](https://www.cho-kaguyahime.com/#character) |
| `S0033`, `O0035`, `O0036`, `C0013`–`C0015`, `U0005` | The epilogue shows `10年後` (`AVFRM-04E`, `02:07:50`). Retain the relative interval. Exact dates within the epilogue remain inferred. `YC型` (`JA#2578`) is unexpanded (`U0005` `OPEN`). `FRM-19` shows a tactile-research screen. Fine text requires a clearer witness. |
| `C0012`, `C0020`, observation ledger header and source inventory §4.4 | In the farewell, some half-second windows approach `−107.45 dBFS`, with higher levels around the voiced `JA#2266` (`01:47:40.620`). Treat these as sampled quiet and vocal windows. `AV-07` records the false-ending UI interval and `FRM-20` (`02:09:48.55`) supports the stage-lift shadow/glow distinction. The 40 observation rows total 28 `ANCHORED` and 12 `REPORTED`. The inventory omits `AM-02` and `AM-03`, which the bounded return discusses. |
