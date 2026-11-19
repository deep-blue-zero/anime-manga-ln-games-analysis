---
series: WUWA
artifact_type: claim_evidence_index
scope: TITLE_WIDE
source_boundary: "Current WUWA Git analytical corpus and Drive evidence routes"
generation: V0.1
status: active_provisional
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# WUWA claim-evidence index

This index routes major accepted or contested claims to their canonical analytical home and underlying evidence system. It does not duplicate the complete claim ledgers.

## Cross-character visual-design layer

The V0.2 visual layer supplies individualized appearance/design profiles for Aemeath, Augusta, Brant, Cantarella, Cartethyia, Changli, Chisa, Denia, Iuno, Jinhsi, Luuk Herssen, Lynae, Phoebe, Qiuyuan, Shorekeeper, Sigrika, Yinlin, and Zani (`status: active_provisional`). Each character directory contains:

- `CHARACTER_VISUAL_DESIGN_PROFILE.md` — the human-readable individualized summary and dimension-by-dimension analysis;
- `CHARACTER_VISUAL_DESIGN_PROFILE.json` — stable claim IDs, evidence-basis labels, confidence, uncertainty, counterreadings, and form/state limits;
- `CHARACTER_VISUAL_REFERENCE_MANIFEST.json` — stable visual IDs and image-to-client-object/package/container/hash reverse provenance.

Directly observed claims cover silhouette, palette, hair/face, costume construction, rendered material cues, motifs, weapon/role signaling, and pose/body language. Design–narrative relationships are separately marked `direct_visual_and_semantic` and remain interpretive. Form/skin/state completeness is `OPEN`: the bounded denominator is exactly one role-linked head icon, formation image, and activity portrait for the default playable presentation. The layer does not establish runtime geometry, rear construction, animation habits, material truth, complete skin/form coverage, or unique authorial symbolism. Raw images remain restricted outside Git.

## Cartethyia (`status: canonical`)

| Claim ID / area | Current formulation | Status | Canonical analytical route | Evidence route |
|---|---|---|---|---|
| CART-CLAIM-001 | self-authored moral continuity; prefers condemning truth about herself to innocent ignorance | repeated pattern | monograph + claim/counterevidence ledger | exact text keys and `wuwa://` locators in claim ledger / Drive bridge |
| CART-CLAIM-002 | protective ethic is particularist and anti-futility, not a blanket anti-utilitarian doctrine | revised, repeated pattern | claim revision + claim ledger | climactic text keys; bounded AV witness where available |
| CART-CLAIM-003 | freedom means chosen obligation rather than absence of obligation | repeated pattern | monograph + claim ledger | profile and post-Leviathan civic lines |
| CART-CLAIM-004 | self-sacrifice is virtue and recurring failure mode | strong inference with major counterexample structure | monograph + claim ledger + fidelity check | Avinoleum annihilation request and later human-anchor plan |
| CART-CLAIM-005 | public solemnity is role-conditioned; private behavior is warmer, playful, embarrassed, and challenge-responsive | source explicit / repeated pattern | monograph + ordinary-life + speech profile | favor/archive and post-integration story evidence |
| CART-CLAIM-006 | trusted care can require reciprocal defiance of despair-driven self-destruction | directly observed, relationship-scoped | monograph + relationship ledger + claim ledger | Rover rescue/promise evidence |
| CART-CLAIM-007 | post-Leviathan faith is humanistic reinterpretation rather than cynical rejection | directly observed | monograph + claim ledger | Phoebe/civic-faith exchange |
| CART-CLAIM-008 | theatricality is ambivalent: imposed myth can erase her, reclaimed performance can become play and authorship | strong inference | monograph + speech profile | public play, Carnevale, staged-death framing |
| Voice-performance centers | 29-moment (`116`-render) `zh-Hans`/`ja`/`ko`/`en` human-calibrated regimes (`27/786` accepted solo lines + `who=1626` + `who=1633`; `759/786` solo lines still uninspected by ear) | PARTIALLY_RESOLVED | speech/voice/performance profile + [four-dub voice ledger](../08%20Audits%20and%20Manifests/WUWA_RINASCITA_CH2_FOUR_DUB_VOICE_LEDGER.md) | `wuwa_voice_generation_v0_5_1` + restricted `WUWA_RINASCITA_CH2_SHARED_AV_V01` |
| Direct staging claims | `27/33` Chapter II targets reviewed in 1080p60 EN runtime (`AV01`, `AV03`–`AV12`, `AV15`–`AV16`, `AV19`–`AV22`, `V03_CLIP_A`–`J`); full-census four-dub listening beyond the 29-moment cohort and `6` optional/non-main-story targets open | PARTIALLY_RESOLVED | Cartethyia AV crosswalk + prior-generation revision ledger + open-questions ledger | `WUWA_RINASCITA_CH2_SHARED_AV_V01` + Drive selected AV witnesses |

Both the V0.2 baseline and the twelve-document `CARTETHYIA_PRE_AV_REBUILD_V0_1` packet (`E01`–`E60`, `C01`–`C50`) now hold `status: canonical` within their pinned 3.6.0 and Chapter II AV-reconciled boundaries. The owner-retired older standalone ordinary-life profile remains `status: historical_legacy` under Cartethyia's `90 Legacy and Superseded/` folder.

## Chisa, Aemeath, Denia, Lynae, and Sigrika (`status: active_provisional`)

- **Chisa**: `CHISA-C01`–`CHISA-C50` and `CHISA-E01`–`CHISA-E60` in `04 Character Analysis/Chisa/01 Evidence and Source-Facing/WUWA_CHISA_EVIDENCE_AND_FALSIFICATION_MATRIX.md`, with interpretation in `WUWA_CHISA_CHARACTER_DEEP_DIVE_PRE_AV.md`.
- **Aemeath**: `04 Character Analysis/Aemeath/01 Evidence and Source-Facing/WUWA_AEMEATH_EVIDENCE_AND_FALSIFICATION_MATRIX.md` and `WUWA_AEMEATH_CHARACTER_DEEP_DIVE_PRE_AV.md`.
- **Denia**: `04 Character Analysis/Denia/01 Evidence and Source-Facing/WUWA_DENIA_EVIDENCE_AND_FALSIFICATION_MATRIX.md` and `WUWA_DENIA_CHARACTER_DEEP_DIVE_PRE_AV.md`.
- **Lynae**: `04 Character Analysis/Lynae/01 Evidence and Source-Facing/WUWA_LYNAE_EVIDENCE_AND_FALSIFICATION_MATRIX.md` and `WUWA_LYNAE_CHARACTER_DEEP_DIVE_PRE_AV.md`.
- **Sigrika**: `SIG-C01`–`SIG-C50`, `SIG-E01`–`SIG-E60`, and compiled rules `SIG-R01`–`SIG-R16` in `04 Character Analysis/Sigrika/01 Evidence and Source-Facing/WUWA_SIGRIKA_EVIDENCE_AND_FALSIFICATION_MATRIX.md` and `02 Reconstruction/WUWA_SIGRIKA_CHARACTER_MODEL_PACKAGE.json`.

## Chapter II shared AV reconciliation (`WUWA_RINASCITA_CH2_SHARED_AV_V01`)

The historical [Chapter II shared AV reconciliation audit](../08%20Audits%20and%20Manifests/WUWA_RINASCITA_CH2_SHARED_AV_RECONCILIATION_AUDIT.md) routes `483` crosswalk target dispositions (`92` `inspected_resolved`, `13` `not_triggered_optional_in_recording`, `22` `out_of_scope_non_main_story`, `356` `out_of_recording_scope`) and `142` reconciliation items over `WUWA_CH2_FAYATO_1080P60_6076F127` and the companion [Chapter II four-dub voice ledger](../08%20Audits%20and%20Manifests/WUWA_RINASCITA_CH2_FOUR_DUB_VOICE_LEDGER.md) (`107` moments / `428` `zh-Hans`/`ja`/`ko`/`en` renders):

- **Three `canonical` Chapter II main-arc packets (`do_not_use_as_current_authority: false`)**:
  - [Cartethyia](../04%20Character%20Analysis/Cartethyia/WUWA_CARTETHYIA_CURRENT_STATE.md): `27/33` scene-AV targets resolved + `29`-moment / `116`-render four-dub calibration (`ko` midpoint hypothesis falsified; `759/786` solo lines unreviewed by ear).
  - [Augusta](../04%20Character%20Analysis/Augusta/WUWA_AUGUSTA_CURRENT_STATE.md): `AUG-E01`–`E44`, `AUG-C01`–`C40`, `AUG-R01`–`R21`; `19/32` Chapter II scene targets, `8/605` solo lines calibrated across four dubs (`32` renders), bounded Act XI `Galbrena` and `8416` EN runtime revisions (`597/605` lines and `13/32` targets open).
  - [Iuno](../04%20Character%20Analysis/Iuno/WUWA_IUNO_CURRENT_STATE.md): `IUN-E01`–`E47`, `IUN-C01`–`C42`, `IUN-R01`–`R24`; `21/39` Chapter II scene targets, `8/540` solo lines calibrated across four dubs (`32` renders), bounded `350_14` four-dub cough and `7764/3` bandpass vs dry Chaos-remnant revisions (`532/540` lines and `18/39` targets open).
- **Six `active_provisional` partial-AV Chapter II packets (`do_not_use_as_current_authority: false`)**:
  - [Brant](../04%20Character%20Analysis/Brant/WUWA_BRANT_CURRENT_STATE.md): `BRA-E01`–`E46`, `BRA-C01`–`C43`, `BRA-R01`–`R21`; `5/38` Chapter II scene targets, `6/606` four-dub solo lines (`24` renders).
  - [Cantarella](../04%20Character%20Analysis/Cantarella/WUWA_CANTARELLA_CURRENT_STATE.md): `CAN-E01`–`E46`, `CAN-C01`–`C44`, `CAN-R01`–`R21`; `4/36` Chapter II scene targets, `6/845` four-dub solo lines (`24` renders).
  - [Phoebe](../04%20Character%20Analysis/Phoebe/WUWA_PHOEBE_CURRENT_STATE.md): `PHO-E01`–`E42`, `PHO-C01`–`C36`, `PHO-R01`–`R20`; `7/24` Chapter II scene targets, `6/476` four-dub solo lines (`24` renders; EN spoken sour-berry coda and harbor blessing revisions).
  - [Qiuyuan](../04%20Character%20Analysis/Qiuyuan/WUWA_QIUYUAN_CURRENT_STATE.md): `QIU-E01`–`E38`, `QIU-C01`–`C36`, `QIU-R01`–`R16`; `5/27` Chapter II Act XI scene targets, `5/255` four-dub solo lines (`20` renders).
  - [Shorekeeper](../04%20Character%20Analysis/Shorekeeper/WUWA_SHOREKEEPER_CURRENT_STATE.md): `SHK-E01`–`E39`, `SHK-C01`–`C39`, `SHK-R01`–`R24`; `2/14` Chapter II Prologue scene targets, `4/543` four-dub solo lines (`16` renders).
  - [Zani](../04%20Character%20Analysis/Zani/WUWA_ZANI_CURRENT_STATE.md): `ZAN-E01`–`E44`, `ZAN-C01`–`C43`, `ZAN-R01`–`R21`; `2/12` Chapter II Act I scene targets, `5/912` four-dub solo lines (`20` renders).

## Newly promoted `active_provisional` pre-AV character routes (owner adoption 2026-11-19)

Under [WUWA_CH2_AV_CHARACTER_PACKET_ADOPTION_2026_11_18.md](../08%20Audits%20and%20Manifests/WUWA_CH2_AV_CHARACTER_PACKET_ADOPTION_2026_11_18.md), the four remaining non-Chapter-II reconstruction packets are owner-adopted as current `active_provisional` authority within their pinned 3.6.0 text and machine-audio scopes (`0` `draft_noncurrent` character packets remain in WUWA):

- [Changli](../04%20Character%20Analysis/Changli/WUWA_CHANGLI_CURRENT_STATE.md): `CHL-E01`–`E44`, `CHL-C01`–`C39`, `CHL-R01`–`R19` in `01 Evidence and Source-Facing/WUWA_CHANGLI_EVIDENCE_AND_FALSIFICATION_MATRIX.md` and `02 Reconstruction/WUWA_CHANGLI_CHARACTER_MODEL_PACKAGE.json` (`0/39` Chapter II targets in scope; `18` `flow#/3688/0` narration lines `runtime_dispatch_unsupported`; scene AV and human listening open).
- [Jinhsi](../04%20Character%20Analysis/Jinhsi/WUWA_JINHSI_CURRENT_STATE.md): `JIN-E01`–`E43`, `JIN-C01`–`C42`, `JIN-R01`–`R17` in `01 Evidence and Source-Facing/WUWA_JINHSI_EVIDENCE_AND_FALSIFICATION_MATRIX.md` and `02 Reconstruction/WUWA_JINHSI_CHARACTER_MODEL_PACKAGE.json` (`0/35` spoken Chapter II targets in scope; `8` `flow#/3722/0` narration lines `runtime_dispatch_unsupported`; scene AV and human listening open).
- [Luuk Herssen](../04%20Character%20Analysis/Luuk%20Herssen/WUWA_LUUK_HERSSEN_CURRENT_STATE.md): `LUK-E01`–`E41`, `LUK-C01`–`C40`, `LUK-R01`–`R19` in `01 Evidence and Source-Facing/WUWA_LUUK_HERSSEN_EVIDENCE_AND_FALSIFICATION_MATRIX.md` and `02 Reconstruction/WUWA_LUUK_HERSSEN_CHARACTER_MODEL_PACKAGE.json` (`0/31` Chapter II targets in scope; `719/719` semantic lines decoded; `3.x` scene AV and human listening open).
- [Yinlin](../04%20Character%20Analysis/Yinlin/WUWA_YINLIN_CURRENT_STATE.md): `YIN-E01`–`E42`, `YIN-C01`–`C40`, `YIN-R01`–`R21` in `01 Evidence and Source-Facing/WUWA_YINLIN_EVIDENCE_AND_FALSIFICATION_MATRIX.md` and `02 Reconstruction/WUWA_YINLIN_CHARACTER_MODEL_PACKAGE.json` (`0/33` Chapter II targets in scope; `439/439` semantic lines decoded; Companion Story scene AV and human listening open).
