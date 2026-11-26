---
title: "Psycho-Pass S1 New Edit — Episode 01 Transaction Checkpoint"
artifact_id: PP_S01NE_E01_CHECKPOINT
artifact_type: unit_transaction_checkpoint
series: psycho-pass
installment: s01-new-edit
unit_id: PP-S01NE-E01
edition: PP-S01NE
version: "1.1"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: PP-INITIAL
source_boundary: "PP-S01NE-E01 (Season 1 New Edit Episode 01 only)"
canonical_home: series/psycho-pass/installments/s01-new-edit/checkpoints/PP_S01NE_E01_CHECKPOINT.md
method_profile: PP_AV_PRIMARY_CHARACTER_AND_FORM
created: 2026-11-23
last_updated: 2026-11-26
---

# Episode 01 Transaction Checkpoint — `PP-S01NE-E01`

- **Run ID:** `PP-S01NE-RUN-20261123-E01-E11`
- **Unit & Edition:** `PP-S01NE-E01` (`PSYCHO-PASS` Season 1 New Edit / Extended Edition)
- **Canonical Reading:** [`PP_S01NE_E01_DEEP_READING.md`](../readings/PP_S01NE_E01_DEEP_READING.md)
- **Published Freeze & Companions:** [`PP_S01NE_PRE_0001.md`](../freezes/PP_S01NE_PRE_0001.md) | [Scene Reconstructions](../PP_S01NE_SCENE_RECONSTRUCTION_LEDGER.md#pp-s01ne-e01) | [Errata & Clarifications](../PP_S01NE_READING_ERRATA_AND_CLARIFICATIONS.md)
- **Coverage Verdict:** `COMPLETE_FOR_DECLARED_SCOPE` (`00:00:00.000–00:45:53.194`, 100% of episode runtime, zero uninspected narrative gaps, zero post-credit scene confirmed, zero E02–E11 narrative exposure).
- **QC Verification:** `14/14` Quality-Control criteria PASS.

---

## 1. Frozen Prospective Entering Boundary (`PP-S01NE-PRE-0001`)

- **Freeze ID:** [`PP-S01NE-PRE-0001`](../freezes/PP_S01NE_PRE_0001.md) (locked prior to narrative inspection; preserved unaltered, SHA-256 `54ed7edfe54cf47990c99349d494d0bfcd01566e1944550c88d84ac1cfb59e12`).
- **Entering Viewer Knowledge:** `NONE` (first unit of `PP-S01NE`).
- **Disclosure of Prior Familiarity:** All participating agents disclosed pretrained familiarity with *Psycho-Pass* (`blind_to_franchise: false`) and quarantined outside-E01 knowledge; blind-first Agent D caught and purged two prospective-contamination leaks prior to acceptance (`DSP-05`).
- **Frozen Pre-Inspection Questions & Hypotheses (`Q1`–`Q5`, `H3a`–`H3c`) Evaluated Honestly:**
  - `Q1` (Extended structure): Confirmed continuous 45:53 New Edit architecture (`SC-01`–`SC-13`, zero post-credit scene).
  - `Q2` (Opening/Middle Block 3/Closing sync): Confirmed linear `0.000s` alignment (`|error| ≤ ±0.4–0.5s`); Block 3 shift isolated to unaligned `TXT-TV01`.
  - `Q3` (`H3a` benign order vs. `H3b` pure dystopian horror vs. `H3c` unresolved ambivalence): **`H3c` retained** — E01 delivers concrete evidence for both `H3a` (real-time downgrade, biometric lock, effective therapy `56.3`, ordinary civilian comfort) and `H3b` (near-execution of innocent hostage, pre-crime juvenile detention, carceral confinement of Enforcers, Kagari's uncorroborated age-5 self-report).
  - `Q4` & `Q5`: Multi-domain character differentiation achieved for Akane, Kōgami, Masaoka, and Kagari; continuous AV + zero-recompression lossless MKV + 1080p `FRM` stills proved mandatory for speaker/action resolution and micro-performance.

---

## 2. Verified Source Identity, Sync Calibration & Scene Coverage

| Witness Role | Witness ID | Bytes | SHA-256 | Calibration & Coverage Notes |
| --- | --- | ---: | --- | --- |
| Primary Video/Audio MKV | `PP-S01NE-E01-AV01` | 2,098,155,274 | `1603b8b0872d4f616a317739dfac060997729b188f62e656123ef271df939f9b` | `video.start_time=0.000s`, `audio.start_time=0.000s`, duration `2753.194s`; 100% watched (`e01_seg01–08`) + 11 zero-recompression lossless MKV clips. |
| Canonical Lossless Audio | `PP-S01NE-E01-AUD-FLAC01` | 225,075,213 | `4005a1e3e83f46f8a48656845edd779c90f472b1f16538532692259b3b604f2f` | Decoded 16-bit PCM (`fdaaf145...`) bit-exact with embedded MKV FLAC; 50 ms `AM` RMS sync & silence checks. |
| Primary Japanese ASS | `PP-S01NE-E01-TXT-BD01` | 64,679 | `e940679bad8022dcfc1214e40eef5ae38c02f767074b647bb9e8fa74fa578358` | `624` cues `00:00:07.530–00:44:31.450`; calibrated linearly (`0.000s` offset, `≤ ±0.4–0.5s` error across opening, Block 3 `00:13:34–00:16:45`, closing). |
| Secondary TV SRT (Text Check) | `PP-S01NE-E01-TXT-TV01` | 54,765 | `ca77a4ea226f50ac3d1e4816522aa2906eef136cbd56a0796b18cec5d4adf59a` | Unaligned TV broadcast clock (5 ad breaks); full wording diffed by Agent B (1 omitted breathing cue `ハァ…ハァ…！`). |
| Complete Episode Bundle | `PP-S01NE-E01-BUNDLE-V1` | — | Validated (9/9 semantic layers, `10/10` unit tests) | `1,350` kept clean 1080p frames, `68` contact sheets, `624` cues, `541` shot changes, `0` broken links (`paired_subtitle_file: null` metadata note disclosed). |

- **Scene Coverage (`SC-01`–`SC-13`):** All 13 scenes (`00:00:00–00:45:53`, including integrated OP *abnormalize*, midpoint utilitarian bridge, rooftop café, Lab No. 2, mall arrest, cafeteria rupture, infirmary confession, CID report, and ED *Namae no Nai Kaibutsu* with confirmed zero post-credit scene) inspected across `CAV` (`1.0 fps` video sampling disclosed), continuous 48 kHz `AO`, `TXT-BD01`, targeted lossless MKV clips, 25+ native 1080p `FRM` stills, and 50 ms `AM` checks (`COMPLETE_FOR_DECLARED_SCOPE`, all load-bearing locators `ANCHORED`).

---

## 3. Independent Multi-Agent Execution & Exposure Registry

| Agent | Role & Model | Blind Order | Inspected Source Scope & Substantive Contributions |
| --- | --- | --- | --- |
| **Agent A** | Principal AV & Narrative Analyst + Integrator — Gemini Neon (Extra reasoning effort) | Principal (`false`) | Full `00:00:00–00:45:53` continuous AV, 11 zero-recompression lossless MKV clips, 25+ 1080p `FRM` stills, full `TXT-BD01`, 50 ms `AM` calibration. Authored `PP-S01NE-PRE-0001`, scene log, working draft, lossless dispute adjudications, and canonical reading. |
| **Agent B** | Japanese-Language, Philosophical & Institutional Specialist — Gemini Neon (Extra reasoning effort, independent subagent) | **`true`** (zero A/C draft exposure) | Full `TXT-BD01` (653 L), full `TXT-TV01` (2,784 L), 7 lossless MKV clips + 2 segments, 5 1080p stills. Contributed Kōgami's lexical triad (`正義`/`役目` vs. `始末をつけなきゃならない役目` vs. `義務を果たした`), `恩寵`/`ご託宣`/`成す` theological-deontic audit, `任意執行対象` bodily-immunity revocation, verified café split (`Kaori` vs. `Yuki`), `2092.04.01` HUD verification, and full BD-vs-TV wording diff. |
| **Agent C** | Character, Relationships & AV Performance Specialist — Gemini Neon (Extra reasoning effort, independent subagent) | **`true`** (zero A/B draft exposure) | Full `00:00:00–00:45:53` continuous AV (`seg01–08`), 5 lossless MKV clips, 5 1080p stills, `TXT-BD01`. Identified Akane tackling Masaoka + Masaoka's articulated metallic prosthetic left hand (`00:19:16–41`), Ginoza's overhead catwalk Paralyzer blast (`00:22:15`), Masaoka speaking through Natsumi's Commissa-chan voice modulator (`00:36:09–42`), inverted eye-opening match cut (`00:24:24` vs. `00:24:51`), ordinary-life CID/apartment baselines, directed `A → B` vs. `B → A` asymmetries, and non-certification of Yayoi↔Shion. |
| **Agent D** | Independent Adversarial Reviewer (Two-Stage) — Gemini Neon (Extra reasoning effort, independent subagent) | **`true`** (Stage 1 frozen blind before draft) | **Stage 1 (blind):** All 8 lossless MKV clips, 14 1080p stills, full `TXT-BD01`, `PP-S01NE-PRE-0001`, alignment QA. **Stage 2:** Audited Agent A draft + Agents B/C findings plus targeted `seg01–05`/`seg08` checks. Caught warehouse/Okura/Ginoza attribution errors, caught and forced purging of two Axis 10 prospective-contamination leaks (`"specimen-like face"`, Makishima link in `CLM-0008`), identified 2112/2113 HUD arithmetic conflict & prop typos, and forced honest adjudication of frozen `PP-S01NE-PRE-0001` (`H3c`). |

---

## 4. Material Dispute Dispositions (`DSP-01`–`DSP-08`)

1. **`DSP-01` (Warehouse `00:19:10–00:19:50` — ACCEPTED / REVISED):** Lossless MKV reinspection confirmed Akane tackles **Masaoka** (not Kōgami), exposing Masaoka's articulated metallic prosthetic left hand (`00:19:41`), and Masaoka delivers `"ドミネーターはシビュラの目だ"` while silent Kōgami goes downstairs after Chika.
2. **`DSP-02` (Warehouse Climax `00:22:11–00:22:30` — ACCEPTED / REVISED):** Lossless MKV reinspection confirmed that right as Chika begins an answering smile at Akane (`00:22:13`), **Ginoza fires a Paralyzer blast from the overhead catwalk** (`00:22:15`, flanked by Yayoi and Kagari), establishing the dual-override structure (`PP-S01NE-CLM-0012`).
3. **`DSP-03` (Okura Stairwell & Warehouse Decoy `00:16:34–00:18:25` — ACCEPTED / REVISED):** Lossless MKV reinspection confirmed Okura mocks Chika in a stairwell with a `STEELBLUE / 110` scanner recommending drone therapy, then **Masaoka slides his biometric-locked Dominator** (red LEDs) across the warehouse floor (`00:17:45`) as a decoy enabling Kōgami's rear Lethal Eliminator shot (`00:18:13`).
4. **`DSP-04` (Akane HUD DOB & Prop Artifacts `00:09:20.0` — ACCEPTED / REVISED):** 1080p `FRM` at `00:09:20.0` confirmed `2092年4月1日生 20歳`, exposing a 1-year internal HUD arithmetic conflict vs. Okura (`2074.04.20 / age 39`, logged as prop artifact in `PP-S01NE-CLM-0010` alongside `11/21`, `10月4日`, `DXSETUP`, and minor text typos).
5. **`DSP-05` (Axis 10 Prospective Contamination — ACCEPTED / PURGED):** Purged `"specimen-like face"` (`00:24:17` → `"pale blood-spattered screaming face"`), purged Makishima link in `PP-S01NE-CLM-0008`, and purged `"gloved hand"` (`00:22:57`), `"Enforcer wrist cuff"` (`00:23:57`), and `"younger Ginoza"` (`00:23:50`).
6. **`DSP-06` (Frozen Prospective Rubric — ACCEPTED / REVISED):** Adjudicated actual frozen `PP-S01NE-PRE-0001` (`Q1`–`Q5`, `H3a`/`H3b`/`H3c` → **`H3c` unresolved ambivalence**).
7. **`DSP-07` (Unvoiced Lips `00:20:59–00:21:02` & Café Speaker Split — ACCEPTED / STRENGTHENED):** Confirmed zero vocal audio on `AO`/`AM`/`TXT` while Kōgami's lips move silently; verified `Kaori` (`メンタル美人` / `友人としての直感`) vs. `Yuki` (Sibyl creed + `なんちてね～`).
8. **`DSP-08` (Commissa-chan Ruse & Yayoi↔Shion Ambiguity — ACCEPTED / STRENGTHENED):** Confirmed Masaoka speaks through Takamori Natsumi's Commissa-chan voice modulator (`00:36:09–00:36:42`); retained strict non-certification of Yayoi↔Shion (`00:30:31`).

---

## 5. Gate Separation & 14-Point Quality Control Summary

- **Sequential-Source Unit (`PP-S01NE-E01`):** `ACCEPTED` (`14/14` QC PASS — verified edition/witness, 9-layer bundle, complete AV/JA routes, preserved prospective freeze & blind review order, substantial source-bounded synopsis, character/relationship/institutional evidence, two independent specialists + two-stage blind reviewer, adjudicated disputes, consistent IDs, §15 named-subject audit PASS, monograph qualification assessed as `DEFERRED_EVIDENCE`, reconciled ledger updates).
- **Longitudinal Reconciliation:** Current through `PP-S01NE-E01` (`PP-DELTA-0001`–`0004` integrated).
- **Specialist / Monograph Readiness:** `DEFERRED_EVIDENCE` (`0` monographs created at single-episode horizon).
- **Full-Series Synthesis Readiness:** `NOT_REACHED` (`1/11` episodes accepted).
- **Next Sequential Operation:** `PP-S01NE-E02` (under active `continuous_sequential` authorization `PP-S01NE-RUN-20261123-E01-E11`; requires fresh prospective freeze `PP-S01NE-PRE-0002` before E02 source inspection).
