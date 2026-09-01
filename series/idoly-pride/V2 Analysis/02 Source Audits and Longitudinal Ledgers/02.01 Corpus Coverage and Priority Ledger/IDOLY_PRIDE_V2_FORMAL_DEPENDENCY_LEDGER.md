---
series: IDOLY_PRIDE
artifact_type: formal_dependency_ledger
artifact_role: LEDGER
scope: PHONE_AUDIO_AND_MISSING_FORMAL_ASSETS
generation: V2
version: "1.0"
status: canonical
phase: "2"
source_snapshot_id: IP-V2-SNAPSHOT-2026-08-13-A
source_boundary: "Initialized from analysis_bundles/reports/telephone_transcript_coverage.tsv and missing_transcript_assets.tsv, plus the frozen Phase-1 formal/open-state routing. No missing content is reconstructed."
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
integrity_status: INITIALIZED_EXACT_GAP_LOCATORS_CAPTURED
created: "2026-08-16"
updated: "2026-08-16"
next_operation: "Promote claim-bearing formal dependencies during Phase-2 ledgers; full retrospective formal audit remains Phase 5"
---

# IDOLY PRIDE V2 — FORMAL DEPENDENCY LEDGER

## 0. Governing rule

Formal evidence state is not narrative evidence state.

A transcript can support a textual claim while missing audio/live/visual material prevents a claim about delivery, staging, music, visual composition, or other formal properties.

Do not reconstruct absent media from ASR, metadata, surrounding prose, Tier-H analysis, or fan memory.

---

## 1. Status vocabulary

Telephone source states:

- `PHONE-AUDIO-VERIFIED` — source audio was actually reviewed for the claim at issue.
- `PHONE-ASR-SUPPORTED` — source audio + approximate machine transcript exist, but the exact formal claim is not necessarily manually verified.
- `PHONE-GAP` — upstream source audio is unavailable and no machine transcript exists.

Formal-effect states:

- `NONBLOCKING_TEXT_ONLY_GAP`
- `FORMAL_NUANCE_UNAVAILABLE`
- `LOAD_BEARING_FORMAL_CLAIM_BLOCKED`
- `PHASE5_REVIEW_REQUIRED`
- `RECOVERED`

P2-0 does **not** globally promote any telephone to `PHONE-AUDIO-VERIFIED` merely because its audio file exists.

---

## 2. Telephone corpus state

Source report: `telephone_transcript_coverage.tsv`.

- telephone references: **256**;
- cached source audio + approximate ASR: **211**;
- upstream source audio unavailable: **45**;
- official upstream transcripts: **0 / 256**;
- P2-0 globally certified `PHONE-AUDIO-VERIFIED`: **0** unless an individual later ledger records an actual audio review.

Approximate ASR must not serve as sole support for exact Japanese micro-linguistic claims.

### 2.1 Coverage by speaker code

| Speaker code | Total telephone refs | Audio + approximate ASR | PHONE-GAP |
|---|---:|---:|---:|
| `ai` | 13 | 11 | 2 |
| `aoi` | 12 | 10 | 2 |
| `chs` | 13 | 11 | 2 |
| `hrk` | 12 | 10 | 2 |
| `kan` | 11 | 9 | 2 |
| `kkr` | 12 | 10 | 2 |
| `kor` | 12 | 10 | 2 |
| `ktn` | 12 | 10 | 2 |
| `mei` | 14 | 12 | 2 |
| `mhk` | 11 | 9 | 2 |
| `mna` | 4 | 4 | 0 |
| `ngs` | 14 | 11 | 3 |
| `rei` | 14 | 11 | 3 |
| `rio` | 13 | 10 | 3 |
| `rui` | 14 | 11 | 3 |
| `ski` | 12 | 10 | 2 |
| `skr` | 12 | 10 | 2 |
| `smr` | 12 | 10 | 2 |
| `suz` | 13 | 11 | 2 |
| `szk` | 13 | 11 | 2 |
| `yu` | 13 | 10 | 3 |

### 2.2 Exact PHONE-GAP inventory

| Dependency ID | Telephone ID | Message ID(s) | Speaker | Source state | P2-0 effect | Route | Note |
|---|---|---|---|---|---|---|---|
| IP-FORM-PHONE-001 | `tel-card-rui-05-fest-04` | `message-card-rui-05-fest-04` | `rui` | `PHONE-GAP` | `LOAD_BEARING_FORMAL_CLAIM_BLOCKED` | OPEN_RUI_MAKINO_POST_RECOGNITION_OUTCOME |  |
| IP-FORM-PHONE-002 | `tel-hbd-ai-26-0209` | `message-hbd-ai-26-0209` | `ai` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-003 | `tel-hbd-aoi-26-0619` | `message-hbd-aoi-26-0619` | `aoi` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-004 | `tel-hbd-chs-25-1122` | `message-hbd-chs-25-1122` | `chs` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-005 | `tel-hbd-hrk-26-0103` | `message-hbd-hrk-26-0103` | `hrk` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-006 | `tel-hbd-kan-26-0410` | `message-hbd-kan-26-0410` | `kan` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-007 | `tel-hbd-kkr-25-1206` | `message-hbd-kkr-25-1206` | `kkr` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-008 | `tel-hbd-kor-26-0611` | `message-hbd-kor-26-0611` | `kor` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-009 | `tel-hbd-ktn-25-1225` | `message-hbd-ktn-25-1225` | `ktn` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-010 | `tel-hbd-mhk-26-0125` | `message-hbd-mhk-26-0125` | `mhk` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-011 | `tel-hbd-ngs-25-0803` | `message-hbd-ngs-25-0803` | `ngs` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-012 | `tel-hbd-rei-26-0308` | `message-hbd-rei-26-0308` | `rei` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-013 | `tel-hbd-rio-25-0828` | `message-hbd-rio-25-0828` | `rio` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-014 | `tel-hbd-rui-25-1111` | `message-hbd-rui-25-1111` | `rui` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-015 | `tel-hbd-ski-25-0926` | `message-hbd-ski-25-0926` | `ski` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-016 | `tel-hbd-skr-26-0403` | `message-hbd-skr-26-0403` | `skr` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-017 | `tel-hbd-smr-26-0505` | `message-hbd-smr-26-0505` | `smr` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-018 | `tel-hbd-suz-25-0913` | `message-hbd-suz-25-0913` | `suz` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-019 | `tel-hbd-szk-25-1015` | `message-hbd-szk-25-1015` | `szk` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-020 | `tel-hbd-yu-26-0227` | `message-hbd-yu-26-0227` | `yu` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-021 | `tel-message-love-mei-24-0517` | `message-love-mei-24-0517` | `mei` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-022 | `tel-message-love-ngs-23-1114` | `message-love-ngs-23-1114` | `ngs` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-023 | `tel-message-love-rei-23-0514` | `message-love-rei-23-0514` | `rei` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-024 | `tel-message-love-yu-24-1114` | `message-love-yu-24-1114` | `yu` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-025 | `tel-message-love-yu-26-0318` | `message-love-rio-26-0313` | `rio` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed | Potential upstream locator anomaly: telephone_id names `yu` while speaker/message identify Rio. |
| IP-FORM-PHONE-026 | `tel-suntory-ai-22-0801` | `message-suntory-ai-22-0801` | `ai` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-027 | `tel-suntory-aoi-22-0801` | `message-suntory-aoi-22-0801` | `aoi` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-028 | `tel-suntory-chs-22-1101` | `message-suntory-chs-22-1101` | `chs` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-029 | `tel-suntory-hrk-22-1101` | `message-suntory-hrk-22-1101` | `hrk` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-030 | `tel-suntory-kan-23-0110` | `message-suntory-kan-23-0110` | `kan` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-031 | `tel-suntory-kkr-22-0801` | `message-suntory-kkr-22-0801` | `kkr` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-032 | `tel-suntory-kor-23-0110` | `message-suntory-kor-23-0110` | `kor` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-033 | `tel-suntory-ktn-22-1004` | `message-suntory-ktn-22-1004` | `ktn` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-034 | `tel-suntory-mei-22-1004` | `message-suntory-mei-22-1004` | `mei` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-035 | `tel-suntory-mhk-23-0110` | `message-suntory-mhk-23-0110` | `mhk` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-036 | `tel-suntory-ngs-22-1004` | `message-suntory-ngs-22-1004` | `ngs` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-037 | `tel-suntory-rei-22-1101` | `message-suntory-rei-22-1101` | `rei` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-038 | `tel-suntory-rio-22-0801` | `message-suntory-rio-22-0801` | `rio` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-039 | `tel-suntory-rui-22-0630` | `message-suntory-rui-22-0630` | `rui` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-040 | `tel-suntory-ski-22-1004` | `message-suntory-ski-22-1004` | `ski` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-041 | `tel-suntory-skr-22-1101` | `message-suntory-skr-22-1101` | `skr` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-042 | `tel-suntory-smr-22-0630` | `message-suntory-smr-22-0630` | `smr` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-043 | `tel-suntory-suz-22-1004` | `message-suntory-suz-22-1004` | `suz` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-044 | `tel-suntory-szk-22-1101` | `message-suntory-szk-22-1101` | `szk` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |
| IP-FORM-PHONE-045 | `tel-suntory-yu-22-0630` | `message-suntory-yu-22-0630` | `yu` | `PHONE-GAP` | `NONBLOCKING_UNTIL_PROMOTED` | claim-specific / Phase 5 if needed |  |

### 2.3 High-load dependency — Rui / Makino

`tel-card-rui-05-fest-04` is a `PHONE-GAP` attached to `message-card-rui-05-fest-04`.

Current claim routing:

> **`OPEN_RUI_MAKINO_POST_RECOGNITION_OUTCOME`**

The preceding card/message evidence is sufficient to strongly establish **Rui-side romantic attraction/self-recognition**. The missing telephone blocks claims about:

- exact spoken confession wording;
- whether an explicit confession is actually delivered;
- Makino's response or romantic reciprocity;
- dating/exclusivity;
- changed relationship status;
- any unrecorded “real selfish wish.”

No later ledger may infer the call's content from narrative expectation.

### 2.4 Upstream locator anomaly candidate

The report row with telephone ID:

`tel-message-love-yu-26-0318`

is associated with:

- `message-love-rio-26-0313`;
- speaker code `rio`;
- unavailable audio.

P2-0 preserves this mismatch exactly and flags it as a **technical locator anomaly candidate**. Do not silently rename the source ID. If a future analysis needs this telephone, verify the upstream mapping before using it as a canonical locator.

---

## 3. Missing processed/formal assets

Source report: `missing_transcript_assets.tsv`.

- stories with missing processed assets: **32**;
- missing references: **32**;
- live/performance assets: **31**;
- other processed/ADV asset gaps: **1**.

These are explicit upstream limitations, not evidence of general dialogue-corpus failure.

| Dependency ID | Story/scene ID | Missing asset ID | Asset type | State | P2-0 effect | Route |
|---|---|---|---|---|---|---|
| IP-FORM-ASSET-001 | `st-card-kkr-05-casl-04-02` | `card_kkr_16_02` | `adv_segment` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-002 | `st-eve-2209-contest-005` | `adv-live-eve-2209-contest-005` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-003 | `st-eve-2210-race-005` | `adv-live-eve-2210-race-005` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-004 | `st-eve-2212-race-004` | `adv-live-eve-2212-race-004` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-005 | `st-eve-2301-contest-005` | `adv-live-eve-2301-contest-005` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-006 | `st-eve-2303-race-005` | `adv-live-eve-2303-race-005` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-007 | `st-eve-2307-race-005` | `adv-live-eve-2307-race-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-008 | `st-eve-2308-marathon-raid-005` | `adv-live-eve-2308-marathon-raid-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-009 | `st-eve-2309-backside-004` | `adv-live-eve-2309-backside-04` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-010 | `st-eve-2311-marathon-raid-004` | `adv-live-eve-2311-marathon-raid-04` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-011 | `st-eve-2312-contest-005` | `adv-live-eve-2312-contest-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-012 | `st-eve-2402-contest-005` | `adv-live-eve-2402-contest-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-013 | `st-eve-2403-race-005` | `adv-live-eve-2403-race-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-014 | `st-eve-2404-dice-005` | `adv-live-eve-2404-dice-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-015 | `st-eve-2405-race-005` | `adv-live-eve-2405-race-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-016 | `st-eve-2408-race-005` | `adv-live-eve-2408-race-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-017 | `st-eve-2410-dice-005` | `adv-live-eve-2410-dice-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-018 | `st-eve-2411-race-005` | `adv-live-eve-2411-race-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-019 | `st-eve-2412-contest-005` | `adv-live-eve-2412-contest-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-020 | `st-eve-2502-marathon-raid-005` | `adv-live-eve-2502-marathon-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-021 | `st-eve-2508-free-005` | `adv-live-eve-2508-event-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-022 | `st-eve-2509-contest-005` | `adv-live-eve-2509-contest-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-023 | `st-eve-2510-marathon-raid-005` | `adv-live-eve-2510-marathon-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-024 | `st-eve-2601-race-005` | `adv-live-eve-2601-race-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-025 | `st-eve-2602-dice-005` | `adv-live-eve-2602-dice-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-026 | `st-eve-2603-race-005` | `adv-live-eve-2603-race-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-027 | `st-eve-2604-dice-005` | `adv-live-eve-2604-dice-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-028 | `st-eve-2606-dice-005` | `adv-live-eve-2606-dice-05` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-029 | `st-ex-story-part-anniversary-01-23-0624-02` | `adv-live-anniversary-01-23-0624-01` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-030 | `st-ex-story-part-special-01-24-0401-april-03` | `adv-live-eve-2404-april-03` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-031 | `st-main-cmn-02-01-63` | `adv-live-main-cmn-02-01-61` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |
| IP-FORM-ASSET-032 | `st-main-cmn-03-01-53` | `adv-live-main-cmn-03-01-53` | `live_performance` | `ASSET-GAP` | textual source remains usable; formal payload unavailable | Phase 5 / claim-specific |

The single non-live entry, `card_kkr_16_02` attached to `st-card-kkr-05-casl-04-02`, remains a formal/processed-asset limitation; do not infer the missing visual/segment from card metadata alone.

---

## 4. Phase-2 promotion rule

The full 77-gap inventory above is **not** automatically 77 blocked literary claims.

During a character/relationship/unit/theme ledger:

1. identify whether the source is actually load-bearing;
2. classify whether the text is sufficient for the claim being made;
3. if the missing formal source matters, link the claim to the relevant `IP-FORM-*` ID;
4. assign the formal effect;
5. if audio/asset is later recovered, record `RECOVERED` without silently altering prior frozen checkpoints.

---

## 5. Phase-5 route registry

Phase 2 should accumulate evidence needs for later retrospective formal analysis:

- character performed voice and delivery;
- telephone audio verification;
- live/performance staging;
- song/3DMV form;
- anime visual/aural formal claims;
- card visual composition;
- formal interaction between spoken text, music, editing, gesture, and staging.

Phase 5 owns exhaustive retrospective audiovisual adjudication. Phase 2 owns the dependency map that tells Phase 5 what is analytically load-bearing.
