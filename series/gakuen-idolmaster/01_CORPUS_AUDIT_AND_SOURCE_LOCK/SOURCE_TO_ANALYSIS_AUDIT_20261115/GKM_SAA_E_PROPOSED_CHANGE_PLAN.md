---
title: "GKM Source-to-Analysis Audit — Proposed Change Plan"
series: GKM
artifact_type: audit
scope: SOURCE_LOCK_1_2_SOURCE_TO_ANALYSIS_AUDIT
generation: V2
status: active_provisional
audit_nature: "non-authoritative retrospective audit; does not itself revise any canonical conclusion (corrections are applied separately through the claim-revision route and recorded in GKM_SOURCE_TO_ANALYSIS_AUDIT_DISPOSITIONS_20261115.md)"
audit_id: GKM-SAA-20261115
source_boundary: "GAKUMAS V2 Source Lock 1.2 — DreamGallery/Campus-adv-txts @ f8ff5ef7b243f2f7e3b2723def31072874539ca9, revision 88; 4,052 raw objects / 103,355 extracted messages; manifest.csv SHA-256 10ad24271fbf7d322284a8364af09ba3551635ea4e793f2046dbdb491ce2c423"
source_lock: GAKUMAS V2 Source Lock 1.2
source_commit: f8ff5ef7b243f2f7e3b2723def31072874539ca9
source_revision: 88
audit_baseline_commit: "176d472a2df2b325f0c54e1c589f7f5e8a89ada9"
created: "2026-11-15"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# E. Proposed Change Plan — GKM source-to-analysis audit (2026-11-15)

Drafter: integration drafter E. Status: **proposal for owner approval**. No repository file was edited. This plan creates no new finding: every change below comes from a row of the final register, as qualified by its reviewer and the integrator. Where a reviewer narrowed a proposal, only the narrowed form appears here.

Baseline: PR #600 head `176d472a` for `series/gakuen-idolmaster/` (open, unmerged), A1 Source Lock 1.2 (revision 88). All canonical paths below are relative to `series/gakuen-idolmaster/`.

## Files read

Audit records (AUDIT = the local audit workspace (owner workstation)):

- `audit workspace\04_final\B_FINDINGS_REGISTER.jsonl`: all 292 rows. Fields used: final severity, integrator disposition, final coverage disposition, claim transition, proposed change, canonical destination, dependencies, owner-adjudication flag, reviewer decision and reasoning, integrator notes, AV dependency, existing canonical claim, A1 object and lines, HSCA relation.
- `audit workspace\04_final\B_FINDINGS_INDEX.md` and `F_review_table.md` (headers and format only); `audit workspace\04_final\G_LIMITATIONS_AND_COMPLETION_STATEMENT.md` (in full).
- `audit workspace\03_adversarial_review\integrator_adjustments.tsv` (in full); `review_assignments_wave1.tsv` (one row checked).
- `audit workspace\checkpoints\CHECKPOINT_3_CANONICAL_COMPARISON_COMPLETED.md` and `CHECKPOINT_4_ADVERSARIAL_REVIEW_COMPLETED.md` (in full); `RESUME_STATE.md`; two lines of `CHECKPOINT_1_BASELINE_LOCKED.md`.
- `audit workspace\briefs\STAGE_D_DRAFTING_BRIEF.md` and `STAGE_B_ASSIGNMENTS.tsv`.
- `audit workspace\02_stageB_comparison\CMP01`–`CMP18\comparison_report.md`: headings, plus the "Cross-track integration problems" and "Proposed additions" sections of all 18. CMP14 §4 and §6–§7 and CMP18 §7–§9 were read in full.
- `audit workspace\02_stageB_comparison\CMP01`–`CMP18\hsca_reconciliation.jsonl`: all rows, read programmatically. `CMP04\hsca_reconciliation.md` and `CMP14\hsca_reconciliation.md` were read in full.
- `audit workspace\02_stageB_comparison\CMP06\candidates.jsonl`: the item lists for C006, C008, C010 and C016. The register keeps only the lead sentence of these four proposals.
- `audit workspace\02_stageB_comparison\_inputs\hsca_index.tsv`; `_inputs\hsca_sealed\SEALED_README.txt` and the first 30 lines of `GKM_HISTORICAL_AUDIT_DISPOSITIONS_20261112.md`, read as the precedent for a correction tranche.

Canonical snapshot (`audit workspace\02_stageB_comparison\canonical_snapshot\series\gakuen-idolmaster\`):

- `SNAPSHOT_PROVENANCE.txt` and the full file list.
- `CURRENT_STATE_AND_CORPUS_MAP.md`: front matter, the first 60 lines and all headings.
- Section headings of the Mao, Hiro, Rinami and Misuzu cores and of Relationship Systems I (RS-I).
- `GKM_LEGACY_CLAIM_REVISION_LEDGER.md`: headings and the "Historical-source claim revisions — 2026-11-12" rows.
- `05_AUDIOVISUAL_ANALYSIS/GKM_CARBON_AV_OBSERVATION_PACKET.md`: front matter, YAML block and headings.
- `04_CUMULATIVE_LEDGERS_AND_INDICES/GKM_AUDIOVISUAL_VERIFICATION_QUEUE.md`: headings.

Repository (local checkout the local repository checkout):

- `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md` (in full) and `governance/policies/BRANCH_LIFECYCLE.md` (first 80 lines).
- Git refs only: `refs/audit/pr600` = `176d472a`; `origin/series/gakuen-idolmaster` = `176d472a`; the **local** `series/gakuen-idolmaster` is at `cc671973` (see §Closing).

No A1 file was opened by this drafter. Every A1 locator below is quoted from the register, from a reviewer's reasoning, or from an integrator note.

---

## How to read this plan

**Identifiers.** `SAA-nnn` is short for the register's `GKM-SAA-nnn`. The comparator candidate ID follows it, then final severity, final coverage disposition, review status and the owner-adjudication flag.

- Review status: `R0n S` = sustained by reviewer R0n; `R0n Q` = qualified; `—` = not sampled (`ACCEPTED_SPECIALIST_ONLY`).
- `OA` = owner adjudication required (35 findings).

**Abbreviations for canonical homes.**

| Short form | Canonical file |
| --- | --- |
| CORE-Mao, CORE-Hiro … | `03_SOURCE_FACING_READINGS/01_CHARACTER_CORE_READINGS/<NN>_<NAME>/GKM_CORE_<NN>_<NAME>.md` |
| EVM-x | the same folder's `*_EVIDENCE_MATRIX.md` |
| AVA-x | the same folder's `*_AV_REVISION_ADDENDUM.md` |
| RS-I | `06_RELATIONSHIP_AND_ENSEMBLE_SYNTHESIS/GKM_RELATIONSHIP_SYSTEMS_I_HANAMI_REVERSI_AND_SYNGUP.md` |
| RS-II | `06_…/GKM_RELATIONSHIP_SYSTEMS_II_RIVALRY_FRIENDSHIP_CLASS_AND_SUCCESSION.md` |
| SIDE | `06_…/GKM_SIDE_CHARACTERS_FAMILIES_STAFF_GOKUGETSU_AND_EXTERNAL_PRESSURES.md` |
| SPINE | `03_SOURCE_FACING_READINGS/00_SHARED_AND_INSTITUTIONAL/GKM_SHARED_AND_INSTITUTIONAL_SPINE_DEEP_READING.md` |
| CSL / RSL / CONT / BRL | `04_CUMULATIVE_LEDGERS_AND_INDICES/` character-state / relationship-state / continuity-and-story-state / branch-divergence ledgers |
| JVR / VPL / PSL / NPC / INST / THEME / SONG / LEG / PIX | same folder: Japanese voice-and-register / voice-performance-state / primary-source-locator / NPC-and-side-character / institution-and-idol-system / theme-and-motif / song / legacy-claim-revision ledgers / support-and-event participant index |
| E001–005, E006–012, E013–020, E021+ | `03_SOURCE_FACING_READINGS/02_STORY_EVENT_READINGS/GKM_EVENTS_*_DEEP_READING.md` |
| S01, S02a/b/c, S03a/b/c/d, R86 | `03_SOURCE_FACING_READINGS/03_SUPPORT_CARD_READINGS/` Series 1; Series 2 parts 001–025 / 026–050 / 051–074; Series 3 parts 001–025 / 026–050 / 051–075 / 076–102; revision-86 reading |
| KANAE | `03_…/14_HIWATARI_KANAE/GKM_HIWATARI_KANAE_SOURCE_LOCK_12_READING.md` |
| XW / RMX | `06_…/GKM_KAYA_RINHA_SOURCE_CROSSWALK.md` / `GKM_KAYA_RINHA_EVIDENCE_MATRIX.md` |
| AVB-x | `05_AUDIOVISUAL_ANALYSIS/<NN>_<NAME>/GKM_<NAME>_COMPLETE_AUDIOVISUAL_BASELINE.md` |
| CARBON-OBS / CARBON-ADJ | `05_AUDIOVISUAL_ANALYSIS/GKM_CARBON_AV_OBSERVATION_PACKET.md` / `GKM_CARBON_AV_ADJUDICATION.md` |

**Track labels** follow the corpus: D-x (Dear route), P1/P2/P3-C (Produce series), M-x (communication episodes), U1 (Unit Story 01), E (numbered events), S (support stories). C1–C4 are the corpus's continuity classes.

**Entry fields.** Each detailed entry (all P1 and P2 changes) gives:

1. Target: canonical file and section.
2. Existing claim affected.
3. Evidence: A1 object and lines.
4. Change, with its claim transition (PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN).
5. Expected analytical benefit.
6. Dependencies and competing changes. ⚠ marks a section that two or more findings target.
7. Owner adjudication.

P3 changes carry the same fields in compact form.

**Reliability gates before landing anything.**

1. **Unreviewed findings.** 207 of 292 findings are `ACCEPTED_SPECIALIST_ONLY`. In the reviewed sample, 39% of P1/P2 findings were downgraded (Checkpoint 4). Before landing an unreviewed P2, re-read its cited A1 lines. This applies the checklist's rule to "show an error, not a preference" (CHANGE_INTEGRATION_CHECKLIST, *Correcting analysis* §2).
2. **Unverified side-claims, excluded until checked in A1** (integrator notes):
   - SAA-009: the E001 / D-SENA 016 add-on.
   - SAA-011: the "P2 a-01" father link.
   - SAA-151: the `school_003` L24 baseline.
   - SAA-147: both voice-actress names. These need an official credit (A4), not A1.
3. **Specialist errata already applied in the register:**
   - SAA-237 is P3. Its cross-track component was over-rated.
   - SAA-104 drops the Saki/Sena-pamphlet example. The Saki core already has Sena as Saki's idol origin; only the E005 locator is missing.
4. **Register hygiene note (resolved by the principal).** An integrator note was first misfiled under SAA-192 (CMP04-C005). It was R04's correction of **CMP09-C005 (SAA-131)**: the Producer initiates Sumika's costume step (cidol-ssmk-3-012_03 L11). The register has since been rebuilt with the note on SAA-131 only, and this plan applies it there.

## Summary of batches

| Batch | Content | Findings | OA flags | Suggested PR (see §Closing) |
| --- | --- | ---: | ---: | --- |
| 0 | Factual, attribution, locator, branch-label and ledger-fact corrections | 59 (10 P2, 49 P3) | 2 | PR-1 |
| 1 | The four P1 integrations, with proposed passages | 4 (P1) | 4 | PR-2 |
| 2 | Cross-track propagation, by target file | 61 (30 P2, 31 P3) | 15 | PR-3a / PR-3b |
| 3 | Other P2 additions and narrowings, by target file | 73 (P2) | 10 | PR-3a / PR-3b |
| 4 | P3 traceability, locator, wording and minor additions | 89 (P3) | 2 | with PR-3a / PR-3b |
| 5 | AV escalation list (no AV review) and the PR #600 AV-documentation item | 4 primary (P3) + 45 cross-listed | 1 | PR #600 (5-B) / PR-4 (5-A) |
| 6 | Historical audit: 49 HSCA findings still holding; HSCA-001 and HSCA-005 residuals | 2 register findings + HSCA items | 1 | PR-1 (factual) / PR-3 |
| **Total** | | **292** | **35** | |

Each register finding is assigned to exactly one batch. Batch 5-A cross-lists AV notes without reassigning findings.

---

## Batch 0 — Factual and attribution errors (cheap, high value)

Batch 0 corrects what the source plainly contradicts. In most entries the analytical conclusion survives, and only the speaker, locator, sequence, branch scope or ledger fact changes. Every Batch 0 finding with a corrective disposition was independently reviewed. Twelve traceability items here were not reviewed and need the A1 re-read gate before landing: SAA-168, 169, 204, 211, 240, 247, 250, 252, 256, 261, 264 and 279.

### 0-A. Misgendering of Mao (one change set)

**SAA-013 · CMP04-C012 · P2 · ATTRIBUTION_ERROR · R04 S · OA: no**, merged with **SAA-031 · CMP16-C001 · P2 · ATTRIBUTION_ERROR · R08 S · OA: no**

- **Target:**
  - S02b, S02c, S03a, S03b, S03c: every sentence that refers to Mao with he/him/his. SAA-031 counts about 57 sentences: S02b 7, S02c 28, S03a 8, S03b 5, S03c 9. Examples: S02c §28.4 "Rinami recognized him as cool"; S03a L244 "he respects Rinami's service but admits that he wants the spotlight".
  - CSL L600, "Phase 5 — Support Series 3 Part 001–025" row 'Arimura Mao' ("mature Mao declines council because he wants the spotlight").
  - RSL L546, row 'Mao ↔ Lilja' ("Lilja reads him as prince-like senior").
  - `GKM_LEDGER_INDEX_AND_SCHEMAS.md`: a new style note.
- **Existing claim:** masculine pronouns for Mao in those homes. The Mao core, its matrix, S01, S02a §22 and S03d all use she/her, and MAO-C14 forbids gender-identity diagnosis.
- **Evidence:** adv_dear_amao_003 L81; adv_cidol-amao-3-015_02 L147 (Mao describes herself as a girl who uses ボク); adv_csprt-2-0020_01 L51, L105, L121–L143, L160.
- **Change (REVISE, wording only):**
  - Use she/her for Mao. Do not alter quoted Japanese (ボク).
  - Add to the ledger schema and the support-reading method note: "Mao's ボク and prince register are not grounds for masculine English pronouns; pronouns follow the character, not the persona (see MAO-C14)."
  - Editorial cautions (R04): correct sentence by sentence, not by keyword, because a nearby "he" usually means the Producer.
  - R08 caution on the secondary dance-trainer pronoun fix in S02b §14: present it as consistency with SIDE and S03d, not as an A1 finding, because A1 dialogue does not establish the trainer's gender.
- **Benefit:** removes a systematic error that has spread from five readings into two ledgers. The schema note prevents recurrence.
- **Dependencies:** none. This also closes HSCA-015, which both comparators rediscovered.
- **Owner adjudication:** no.

### 0-B. Speaker, referent and perspective attribution

**SAA-006 · CMP02-C001 · P2 · ATTRIBUTION_ERROR · R02 S · OA: no**

- **Target:**
  - AVA-Temari §6 (agency evidence list).
  - AVB-Temari §5.9.
  - CORE-Temari §2.5 and §10.4.
  - JVR Phase 3 Temari table: the dear 035 row, plus a new dear 037 手毬 row.
  - VPL T-DIA-04.
  - `GKM_TEMARI_AUDIOVISUAL_BASELINE_AND_REQUESTS.md` AV-DIA-TEMARI-012.
  - CSL D-TEMARI winter victory row.
- **Existing claim:** Temari "asks the Producer to call her 手毬" and "requests ramen". The 呼び捨て request "turns given-name address into a chosen pre-performance ritual".
- **Evidence:** adv_dear_ttmr_035 L632–L650 (her 呼び捨て request; his sole-choice 月村 at L647; plain imperative at L650); adv_dear_ttmr_037 L242, L396 (she calls the meeting), L417, L428 (sole-choice 手毬), L432 (ramen), L441, L450.
- **Change (REVISE):**
  - Keep her de-honorification request as agency.
  - Add the Producer's self-initiated escalation 月村さん → 月村 → 手毬 to the reciprocity model, parallel to his 俺 slips.
  - In the CSL, read: "calls the meeting; accepts the Producer's ramen proposal".
  - R02 cautions: do not cite L424 as proof the name was unexpected, because it precedes the name; use the L441 silence. Call the ramen line mixed register (食う + ましょう), not casual. Present the alternative reading ("呼び捨て" could mean 手毬) as ambiguity in her wish.
- **Benefit:** the given name becomes evidence of the Producer's reciprocal move rather than a second request by Temari.
- **Dependencies:** ⚠ CORE-Temari §2.5 is also touched by SAA-121 (§2.4). They are adjacent paragraphs, so land them together.
- **AV:** optional AV-D on L441/L450.
- **Owner adjudication:** no.

**SAA-017 · CMP07-C002 · P2 · ATTRIBUTION_ERROR · R07 S · OA: no**

- **Target:** CORE-Hiro §14, §21 item 4, §27.3 and §27.6; EVM-Hiro HIRO-C18 and HIRO-C19; CSL D-HIRO crisis strategy; INST ("crisis as production technology"); RSL Hiro ↔ Producer H.I.F.
- **Existing claim:** the Producer "explicitly makes the relationship itself part of the motivational wager" (§21.4; HIRO-C19 "relationship wager").
- **Evidence:** adv_dear_shro_028 L200–L283 (the relationship stake is spoken by Hiro, `name=広`, at L244; the Producer accepts it tacitly at L248; he confirms he is cornering her at L226); adv_pstory_003_shro_final-failure-01 L16–L82 (P3-C payout); adv_dear_shro_037 L186–L216 (the one-time limit at L194–L209).
- **Change:**
  - REVISE the wager wording. He stakes his producer career and says that "our dream and fun hobby time" end if she fails. Hiro infers that he would stake "even our relationship", and he accepts being hated for it.
  - STRENGTHEN with the P3-C final-failure state, labelled C3: the stake is paid and the hobby and dream end, but the partnership continues with Hiro's consent.
  - Cross-reference the Dear 037 one-time limit from AVA-Hiro §2/§4 (L117). It is not new material.
  - PRESERVE §14's separation-pressure line (Dear 037 L130–L165 shows the stake was credible to both) and the ethical OPEN.
- **Benefit:** corrects who voices the relationship stake. That matters for every reading of manipulation in this dyad.
- **Dependencies:** ⚠ HIRO-C19 is also targeted by SAA-067 (Batch 3), and §21 by SAA-068 and SAA-070. Edit §21 once.
- **Owner adjudication:** no.

**SAA-018 · CMP07-C003 · P2 · ATTRIBUTION_ERROR (requalified from MISINTERPRETED) · R07 Q · OA: no**

- **Target:** CORE-Hiro §11, §13 and §28; EVM-Hiro HIRO-C15 and HIRO-C17; INST (measurable ability vs charisma); RSL Hiro ↔ Sena.
- **Existing claim:** "Sena's 神格 analysis" (HIRO-C17). "Sena … gives Hiro an extremely low current evaluation. That assessment is not portrayed as wrong" (§13).
- **Evidence:** adv_dear_shro_012 L116 (fans deify her); dear_021 L263–L361, L337–L342 (the Producer's fitness data, 0% odds, his coinage 神格 / 雰囲気トップアイドル); dear_022 L257–L420 (Sena's '4 → 400' scouter, played in a comic register); dear_023 L203–L239, L282–L387, L444; dear_024 L31–L35 (Sena converges).
- **Change (REVISE):**
  - Trace 神格 in order: fans, then the Producer, then Sena.
  - Describe Sena's numbers as a personal 特技 in a comic, half-occult register, not an institutional verdict.
  - Rest the premise of low conventional skill on the Producer's fitness test, the 0% odds and Sena's earnest それ passage.
  - PRESERVE the conclusion that measurement is real but incomplete.
  - Fix the misquote '夢見るアイドル'.
  - Per R07, the Dear 032/036 godhood-rejection item is only a P3 cross-reference, because §17, §26 and THEME L305 already cover it.
- **Benefit:** a misattributed genealogy becomes the right one, and the comic register is no longer read as an institutional ruling.
- **Dependencies:** ⚠ §11 is also edited by SAA-002 (Batch 1). PR-1 lands first (see §Closing), so PR-2 re-reads §11 at the new head and builds on the corrected genealogy. Compatible with AVA-Hiro §2 (神格 QUALIFY).
- **Owner adjudication:** no.

**SAA-019 · CMP08-C003 · P2 · ATTRIBUTION_ERROR · R06 S · OA: no**

- **Target:** CORE-Rinami §7; JVR Rinami textual-register baseline row; EVM-Rinami RINAMI-C04 (C03 needs no change per R06); AVB-Rinami §5.
- **Existing claim:** "Dear 020 … arrive[s] at the better reconstruction: きみと私、お互いがお互いの手を引っぱりあってたんだ". JVR attributes the line to Dear 020.
- **Evidence:** adv_cidol-hrnm-3-013_03 L171–L207 (the resolving line at L197); adv_dear_hrnm_020 L313–L383 (L339–L367: each credits the other; "まあいっか"); adv_cidol-hrnm-3-017_01 L212 (Rinami's own version, in inner speech).
- **Change (REVISE):**
  - Relocate the resolving line to CIDOL 013_03 L197 and scope it C4.
  - State that Dear 020 supplies mutual crediting (each remembers being led by the other) and an unstable hierarchy, and that the explicit synthesis exists only in the communication episode (R06 refinement, replacing "rests on Dear 026, not Dear 020").
  - Correct AVB §5: mutual credit, not each remembering herself as the leader.
  - RSL row 157 is already accurate.
- **Benefit:** restores track scope to a "very high confidence" line.
- **Dependencies:** ⚠ CORE-Rinami §7 is also edited by SAA-129 (one §7 wording slip). Land together. Related to SAA-003.
- **Owner adjudication:** no.

**SAA-030 · CMP15-C004 · P2 · ATTRIBUTION_ERROR · R06 S · OA: no**

- **Target:** E021+ §2.5; E013–020 §2.4 and §12 (Sena↔Tsubame row); RS-II §5.5.
- **Existing claim:** "At the observation deck years later, Sena reminds her of the story" (E021+ §2.5). The relationship is said to include "unusually accurate mood detection".
- **Evidence:** adv_event_021_main-05 L237–L274 (Tsubame recites the exchange at L258–L265; Sena says 'そこまでは覚えていない' at L274), L170–L182, L345–L363; event_013 main-05 L167–L253, L260–L322 (Sena substitutes an explanation and apologises inwardly at L312–L322), L597–L625; event_021 main-04 L47–L99, L340–L353; event_021 main-03 L207–L243.
- **Change:**
  - REVISE §2.5. Sena recalls only that Tsubame taught her the word, and the opening memory is Tsubame's dream (021-01).
  - STRENGTHEN the asymmetry in E013–020 §2.4, its promotion row and RS-II §5.5: Tsubame's reading of Sena is real but bounded. Sena hides her growth-limit belief, confides the pressure to Rinami (021-04), and keeps her envy of Tsubame's "wings" unspoken. Tsubame's claim that Sena can rely only on her (021-05 L175) is Tsubame's statement.
  - This complements RS-II §5.7.
- **Benefit:** stops a key event memory being given to the wrong character and bounds an over-strong mutual-knowledge claim.
- **Dependencies:** ⚠ RS-II §5.4/§5.5 is also touched by SAA-251 (Batch 4). AV: 021-05 is already AV P0; nothing new.
- **Owner adjudication:** no.

**P3 attribution corrections (compact).** All were reviewed. Each line gives the target; the error; the evidence; the change (transition); the benefit; and any dependency.

- **SAA-122 · CMP03-C012 · R03 S.**
  - Target: CORE-Kotone §3.2.17; EVM-Kotone KOTO-C09; CSL row 98 ("luck anxiety").
  - Error: "she describes herself as both highly confident and highly unconfident", under the heading "luck anxiety".
  - Evidence: adv_dear_fktn_023 L43 (the fluke reading is the internet's); L49–L59; L171, L188, L194; L196 (the Producer's formula); L204 (her assent).
  - Change: REVISE. Attribute 超自信…超自信がない to the Producer, with Kotone's assent. Retitle §3.2.17 (for example "comparative doubt, not luck anxiety"). PRESERVE the domain-split conclusion.
  - Benefit: correct speaker; correct heading.
- **SAA-126 · CMP07-C010 · R07 S.**
  - Target: CORE-Hiro §16 and §26; HIRO-C22; SIDE §7.4.
  - Error: "The Producer tells her… Hiro protests".
  - Evidence: adv_dear_shro_035 L233, L291–L311 (Hiro recalls his Dear 010 line and concedes; L310 is his redefinition 'それはもう、素手のうち'); cidol-shro-3-012_02 L26–L133; 012_03 L91–L155; 001_03 L106–L129; P2 ending-normal-02 L42–L45.
  - Change: REVISE the speaker. STRENGTHEN by inserting the CIDOL 012 disclosure-and-severance stage, labelled **M-HIRO** (not C-HIRO).
  - Benefit: inverts a misreported exchange.
  - Dependency: ⚠ §16 is also rewritten by SAA-002 (the Dear 035 letter). PR-2 builds its §16 rewrite on 126's corrected text.
- **SAA-127 · CMP07-C017 · R07 S, + SAA-136 · CMP10-C009 · R05 S, + SAA-280 · CMP17-C017 (—): one RS-II §4.1 change.**
  - Target: RS-II §4.1 and §4.11 (PROMOTE row); CORE-Ume §12; U1 placement doc §2.3.
  - Error: "Ume proposes the self-authored Worst Three identity" and "a story they will someday tell".
  - Evidence: adv_event_002_main-01 L293–L342 (Hiro names 'ワーストスリー' at L300–L302; Ume's propulsion '3人で、這い上がっていこうね！' at L323); unit_01-03_02 L338 (China's label in U1); pevent_001_hume_activity_008 choices 1–3 (L34–L41 / L49–L58 / L71–L80); unit_01-03_03 L335–L494.
  - Change: REVISE.
    - The label is Hiro's in E002 and China's in U1.
    - Ume supplies the shared climb.
    - The "weakness becomes a story" framing is the Producer's in activity_008 choices 2–3, which Ume adopts. Her own contribution is the debut promise in choice 1.
    - Keep "self-authored" as a trio-level description, matching E001–005 §4.1, which is already correct.
    - SAA-280 adds: in U1 the trio disperses, and China and Hiro model their rivalry on the Hanami sisters. Track-label this.
  - Benefit: three findings converge on one sentence; fix it once.
  - Dependency: SAA-136 asks CMP15/CMP17 to confirm the host-object readings. R05 did so from the raw name fields.
- **SAA-135 · CMP10-C008 · R05 S.**
  - Target: CORE-Ume §6.4; UME-C25.
  - Error: アイドルはアイドルを導ける… is quoted as Ume's line, and the matrix misquotes it as 導く.
  - Evidence: adv_dear_hume_027 L554–L566 (L566 `name={user}`); Ume's firewood reformulation at L611–L640.
  - Change: REVISE. Attribute to the Producer, restore 導けると, and keep Ume's L617–L640 as her endorsement. A cross-track motif note on D-SENA 033 L220 is allowed, but do not import that line into D-UME.
  - Benefit: co-authored thesis; correct quotation.
- **SAA-142 · CMP11-C010 · R01 S.**
  - Target: CORE-Misuzu §11; EVM-Misuzu C17.
  - Error: Rinha's departure "was partly enabled by Misuzu…", stated in the narrator's voice.
  - Evidence: adv_dear_hmsz_016 L124–L135, L188–L225 (Misuzu's counterfactual regret; Rinha's rejection at L215–L218).
  - Change: REVISE to Misuzu's belief, contested by Rinha, and route causal weighting to RINHA-C033.
  - Benefit: removes unattributed causation.
  - Dependency: SAA-084 (Batch 3).
- **SAA-144 · CMP12-C009 · R02 S.**
  - Target: CORE-Sena §24.
  - Error: "She calls the juniors 可愛い妹たち".
  - Evidence: adv_dear_jsna_023 L330–L407 (L381 `name=ことねの妹たち`); care evidence at L57–L88.
  - Change: REVISE. The phrase refers to Kotone's sisters. Rest the care claim on L57–L88, and keep the sibling scene for Sena's pleasure in fan reception.
  - Benefit: correct referent.
  - Dependency: ⚠ §24 is also qualified by SAA-145 ("debt structure").
- **SAA-148 · CMP13-C004 · R03 Q (UNDERWEIGHTED, perspective attribution).**
  - Target: CORE-Tsubame §5, §6, §22; TSB-012/013; RS-II.
  - Error: §22's narrator-voiced "idol role imposed upon her".
  - Evidence: adv_dear_atbm_024 L485–L517 (Sena: 'also my own will', L512); 008 L43–L52; 009 L266–L273; 012 L304–L314; event_021 main-03 L230–L243; D-SENA 026 L84–L90.
  - Change: REVISE to "what Tsubame perceived as", and add Sena's contesting voice. §6 already says "Young Tsubame perceived".
  - Benefit: separates one character's interpretation from fact.
  - Dependency: ⚠ §6 and §20–22 are also targeted by SAA-029 and SAA-093.
- **SAA-149 · CMP13-C006 · R03 Q.**
  - Target: CORE-Tsubame §19 (and §33 note); TSB-046; RSL Tsubame ↔ Sena delta.
  - Error: "The answer is love".
  - Evidence: adv_cidol-atbm-3-018_02 L85–L96 (L87 Tsubame, 'help her, show her the way'; L93 the Producer, 'つまり、愛ですよね'; L96 her reluctant acceptance); dear_010 L348–L353; dear_024 L225–L229.
  - Change: REVISE. The Producer names love, and Tsubame accepts it with reservation. Record her rescue/guidance wording. PRESERVE the bounded-love conclusion (TSB-047). §33's "the text itself does so" is literally true and stays.
  - Benefit: correct speaker of a thesis-level word.
- **SAA-166 · CMP17-C015 · R03 S.**
  - Target: RS-I §3.5.1 table, "actual Ume" column.
  - Error: `1勝1敗` is attributed to Ume.
  - Evidence: adv_unit_01-04_21 L522 (Saki's line); Ume's own lines at L527–L534 (R03 corrected the proposal's L573–L664).
  - Change: REVISE. Either attribute the line to Saki or quote Ume at L527–L534.
  - Benefit: correct speaker in a table cell.
- **SAA-256 · CMP13-C010 (—).**
  - Target: CORE-Tsubame §25; TSB-062; Tsubame refresh.
  - Error: the hypothesis that attraction intensifies while Tsubame is saving someone is presented as the analyst's inference.
  - Evidence: adv_dear_atbm_022 L457–L514 (the Producer's theory at L478–L492, citing Shion; Tsubame '四音の時のように……か？'); SL1.1 dear_029 L23–L80 (he bounds it).
  - Change: REVISE. Attribute the hypothesis to the Producer and keep TSB-062 OPEN.
  - Benefit: attribution.
- **SAA-128 · CMP08-C004 · R06 Q (inner-speech status).**
  - Target: CORE-Rinami §12 heading and quotations, §27.9; RINAMI-C19/C20 wording; JVR AV R2 row.
  - Error: "desire becomes speakable only after…"; "She is saying".
  - Evidence: adv_dear_hrnm_027 L376 and L402 (isInner); L414 and L514–L557 (relational outward claim); dear_012 L325; dear_017 L138; dear_018 L393–L400.
  - Change (narrowed by R06):
    - REVISE the §12 heading to something like "re-owned" or "re-voiced without apology".
    - Mark L376 and L402 as inner speech, and replace "She is saying" with "She tells herself".
    - Optionally add Dear 018 L400 'ごめんね、わがままで' and Dear 012 L325 as the before-state.
    - PRESERVE the hinge status (§27.9).
  - Benefit: epistemic accuracy.
  - Dependency: SAA-003.
- **SAA-133 · CMP09-C007 · R04 S.**
  - Target: CORE-Sumika §8 (the CIDOL 007 sentence).
  - Error: "after seeing how much her weakness hurts Lilja", stated as fact.
  - Evidence: adv_cidol-ssmk-3-007_02 L272–L313 (Lilja asks to be told and relied on); L322–L349 (Sumika's inference); L369–L374.
  - Change: REVISE. Make the paradox explicit: a plea for reliance is answered with deeper concealment. Mark the time layering, because the resolve belongs to the present crisis frame (L56–L69, L139, L351–L374). SUMIKA-C13 already holds the correct reading.
  - Benefit: one character's inference is no longer narrated as fact.
  - Dependency: distinct from the HSCA-005 box in §8.
- **SAA-132 · CMP09-C006 · R04 S.**
  - Target: CORE-Sumika §10; SUMIKA-C16 counter-pressure column.
  - Error: "Sumika nevertheless insists on rebuilding dance".
  - Evidence: adv_dear_ssmk_021 L125–L245 (she requests at L133, presses once at L144, defers at L212–L218; the Producer reverses himself at L221–L235); dear_031 L510–L523.
  - Change: REVISE. She asks and presses once, then defers, and the Producer authorises. Record his L523 denial of foresight. The link to the Dear 025 good-girl diagnosis depends on SAA-078.
  - Benefit: shared decision; visible deference.

### 0-C. Sequence, anchor and locator errors

**SAA-005 · CMP01-C001 · P2 · CONTINUITY_ERROR · R01 S · OA: no**

- **Target:** CSL Phase 3 Saki row 'D-SAKI first direct Ume contest' (and trim the 008–010 row); RSL Phase 3 row 'Saki ↔ Ume | first direct stable contest'; RS-I §12.1 (Hanami bullet 2; a secondary TRACEABILITY_GAP) and §3.3 routing.
- **Existing claim:** the first direct win is placed at adv_dear_hski_011–012 and explained as "preparation, strategy, and total competitive construction".
- **Evidence:** adv_dear_hski_009 L145 (win); L267–L287 (single choice L287 '今日はあなたの方が、魅力的なアイドルだった'); L313 '辛勝'; L340 (H.I.F. still ahead). adv_dear_hski_012 L186–L205 (tied ranking contest) and L281–L289 (L285 looks back).
- **Change (REVISE):**
  - Relocate the first direct win to Dear 009. Saki wins narrowly on idol appeal and desperate effort while conceding total technical inferiority.
  - Describe Dear 011–012 as N.I.A. set-up plus a tied contest after which the sisters fix the FINALE, won in Dear 019.
  - Use CORE-Saki §3.2.4, which is already correct, as the model. RS-I §3.3 prose stays.
- **Benefit:** three homes stop mislocating and mis-explaining Saki's first win over Ume.
- **Dependencies:** ⚠ RS-I §12.1 and the RSL Saki ↔ Ume rows are also extended by SAA-109 (U1 Episodes 01–03), which builds on this correction in PR-3a.
- **Owner adjudication:** no.

**SAA-012 · CMP04-C002 · P2 · MISINTERPRETED · R04 S · OA: no**

- **Target:** CORE-Mao §2.9; EVM-Mao MAO-C20; CSL D-MAO summer H.I.F. loss; JVR Phase 3 Mao Dear 027 row; **PSL MAO-L009** (integrator note).
- **Existing claim:** "Mao can frame the loss publicly as a step and still break down privately: > 負けたあああああああああっ！". The same sequence is repeated in MAO-C20, the CSL ("then privately cries 負けた") and the JVR.
- **Evidence:** adv_dear_amao_027:
  - L10, L16: the immediate cry, in the waiting room with the Producer.
  - L29–L57: framing ('ボクたちが最後に勝つための、大切なステップ', L52–L57).
  - L61–L67: a separate 100Pro-exterior Juo scene, after a white fade.
  - L79–L86: winter declaration.
  - L336, L430–L434: party composure.
  - L501, L516: inner grief, isInner.
  - L580–L598: collapse with Rinami in the shared space after the party.
- **Change (REVISE the anchor and sequence; PRESERVE MAO-C20's conclusion):**
  - Sequence: unguarded cry, then composed framing, then inner grief, then collapse at Rinami's praise.
  - Add that the inner grief is about going pro with the Producer now ('今すぐキミとプロになれるって、言いたかったんだ', L516).
  - Name Rinami, her 戦友, as the person in front of whom she collapses, cross-referencing the RSL Mao–Rinami row.
  - R04 corrections: Juo is not present at L16; the collapse happens after the party, not at it.
- **Benefit:** corrects a "very high" claim's anchor in five homes.
- **Dependencies:** links to SAA-001 (the L516 grief ties to going pro with the Producer). ⚠ CORE-Mao §2.8/§2.9 is also edited by SAA-001, so land 012 inside PR-2 or before it.
- **Owner adjudication:** no.

**P3 sequence and locator corrections (compact).**

- **SAA-129 · CMP08-C012 · R06 S.** Target: CORE-Rinami §6, §7, §11, §12, §21. Six slips, each with the A1 fix:
  - (a) §11: the father had surgery but "命に別状はない" (adv_dear_hrnm_023 L362). Keep "badly injured" and add "not life-threatening". The deteriorated stage is implied (Mao's "調子が――", L400).
  - (b) §11: the doubt is voiced to the Producer in the homecoming arc (027 L524–L531). The explicit re-attribution of the loss to Sena is in Dear 029 L209–L238.
  - (c) §12: the "live together" test takes place in Dear 026 L387–L449, and Dear 027 replays it as a colour-graded flashback (L209–L252). Add his "office in your hometown" answer.
  - (d) §6: Dear 010 L39 is spoken alone, not isInner.
  - (e) §7: "私とはぐれないように" follows his objection at Dear 020 L410.
  - (f) §21: Rinami asks to choose (cidol-018_01 L180) and he agrees (L184).
  - Change: REVISE (wording). Benefit: six factual slips in one core. Dependency: ⚠ §6/§12 also carry SAA-003 and SAA-128; §7 carries SAA-019.
- **SAA-168 · CMP01-C009 (—).** Target: CORE-Saki §16.7 and §26 SAKI-L046; CSL Phase 3 Saki rows.
  - Error: SAKI-L046 labels 017_01–03 as one 'post-loss' block.
  - Evidence: adv_cidol-hski-3-017_01 L4, L85; 018_01 L71, L88, L112, L134; 018_02 L12; 012_03 L152; dear_023 L392, L481–L491.
  - Change: REVISE. Split SAKI-L046: 017_01 is the day after the N.I.A. win, and 017_02–03 follow the summer loss. Record the anchors: 018_01 L134 quotes dear_023 L392; 018_01 L88 gives the Producer's private judgement, useful for §7.3.
  - Benefit: placement precision.
- **SAA-169 · CMP01-C010 (—).** Target: CORE-Saki §3.1.3, §16.1, §26 SAKI-L029–L030.
  - Error: the 'starting line' and 'restraint' readings point to final-normal-03/04, and §16.1 merges the mid- and final-audition ladders.
  - Evidence: after-audition-mid-normal-03 L72–L85 (choice branch, L80); mid-normal-04 L14–L27; final-normal-03 L1–L40; final-normal-04 L1–L60 (ruby 試合《ゲーム》 at L32).
  - Change: REVISE the locators, and label §16.1 rows by audition.
  - Benefit: wrong-locator fix.
- **SAA-211 · CMP06-C011 (—).** Target: CORE-China s2.
  - Error: "Produce Event texture supports this".
  - Evidence: adv_dear_kcna_010 L287–L289; dear_017 L197–L208; P1 ending-true-01 L104–L121. Reader B06 read all 83 China Produce Events and found no instance.
  - Change: REVISE. Replace the phrase with the actual locators.
  - Benefit: the claim's evidence route becomes true.
- **SAA-240 · CMP11-C011 (—).** Target: CORE-Misuzu §2.2, §2.3, §4, §29.2.
  - Error: the §2.3 line is attributed to a Produce Event, and school_004's three player-selected rationales are merged.
  - Evidence: pstory_001_hmsz_after-step-2-normal-01 L91–L99 (L95); pevent_001_hmsz_school_004 L26–L56 (choices at L29–L33, L48–L56, L67); pstory_002 after-audition-a-normal-03 L25–L74.
  - Change: REVISE. Relabel the source, and present the school_004 rationales as alternatives. Choice 2 diverges from Misuzu's self-report that she is bad at doing things alone.
  - Benefit: locator and branch accuracy.
- **SAA-247 · CMP11-C019 (—).** Target: CORE-Misuzu §21 and §30 (M-MISUZU placement).
  - Error: the Ume–Rinha resemblance is placed in CIDOL 010.
  - Evidence: adv_cidol-hmsz-3-015_01 L72–L160; dear_014 L242–L254 (inner); dear_012 L227–L233; cidol 005_01 L14–L34.
  - Change: REVISE. Relocate the resemblance to CIDOL 015_01 (matrix C37 is already correct), and add the D-MISUZU inner lines as the source of the realization.
  - Benefit: wrong locator.
- **SAA-250 · CMP12-C007 (—).** Target: CORE-Sena §4 and §40 OPEN-SENA-03; SENA-C51; SIDE.
  - Error: "a clarity inherited or shared within the Juo family".
  - Evidence: D-CHINA adv_dear_kcna_003 L97 (principal), L109; adv_dear_jsna_002 L140, L162–L170 (choice-3 hearsay).
  - Change: REVISE. Cite D-CHINA 003 L97 as principal evidence, and phrase the similarity as claimed by Sena and the headmaster, a reading that the Producer and the trainer doubt. Use "reportedly shared" instead of "inherited".
  - Benefit: the evidence route matches the claim's strength.
- **SAA-264 · CMP13-C020 (—).** Target: TSB-026/027; CORE-Tsubame §9 and §11.
  - Error: the evidence is "P2/N.I.A. post-competition reflection", but no 勝者 line exists in any series_002 or Produce Event atbm file.
  - Evidence: adv_cidol-atbm-3-012_03 L57–L71 ('それが勝者の責務だからな'); 000_03 L19, L45, L97–L116; 000_02 L72; 018_03 L111; SL1.1 dear_036 L1018.
  - Change: REVISE. Re-route to CIDOL 012_03 (M-track), qualify §9's "earliest" claim, and note the track variance on the private クライアイ live.
  - Benefit: wrong source family corrected.
- **SAA-279 · CMP17-C014 (—).** Target: CORE-Saki §26 SAKI-L056 and SAKI-L057.
  - Error: the rows are mislabelled.
  - Evidence: adv_unit_01-03_01 L24–L708; 01-02_15 L91–L535.
  - Change: REVISE. SAKI-L057 → rotating center and Kotone chosen as leader. SAKI-L056 → the cooking-duel resolution and Temari's food requests. Worst Three is 01-03_02, Begrazia 01-03_12; roles and centers are 01-02_02 and 01-03_01.
  - Benefit: wrong locator gloss.

### 0-D. Branch-label and track-scope errors

These are all P3 and reviewed, except SAA-204. One label error inside a P2 is folded in from SAA-014.

- **SAA-125 · CMP07-C009 · R07 S.** Target: CORE-Hiro §10; HIRO-C12/C13; JVR; RSL N.I.A. row.
  - Error: the formula '趣味のまま、夢を見たっていいでしょう' and the パートナー line are presented as one scene.
  - Evidence: adv_dear_shro_020 L234–L405. Branch 1 carries the formula and the それ deferral (L280, L303–L314); branch 2 carries the partner language and Hiro's dream-sharing (L329, L365).
  - Change: REVISE the labels and PRESERVE the invariant (shared dream; the hobby continues). Editor's extra: '新鮮で、苦しくて、ままならない' is the Producer's phrase (dear_005 L254; dear_008 L238), not the partnership's.
- **SAA-130 · CMP08-C013 · R06 S.** Target: CORE-Rinami §5.
  - Error: "she eventually jokes … and asks to sit beside him" reads three choices as one sequence.
  - Evidence: adv_pevent_001_hrnm_activity_020 L14–L20 (branch-free trunk); choice group n=3 at L25 (choice 1 L30; choice 2 L59/L69; choice 3 L84/L95).
  - Change: REVISE. The trunk carries the claim, and the three continuations are alternatives. RINAMI-C07 is unaffected.
- **SAA-134 · CMP09-C009 · R04 Q.** Target: SUMIKA-C10 and C28; BRL Phase 3 Sumika; CORE-Sumika §6.
  - Error: C10 says "P1 endpoint is willingness to stop fleeing valued things" without branch scope.
  - Evidence: ending-normal-04 L36–L49, L96–L114; ending-normal-05 L26–L31, L122–L131; true ending L92; ssmk final-failure L59–L129 (L108–L112); kllj final-failure L45–L59.
  - Change: REVISE, as qualified by R04.
    - Scope C10 and the BRL P1 line to the true ending and normal-01/-03, which are also further support.
    - Record the face-saving stance of -04/-05 as an alternative state, bounded to -04/-05.
    - Drop normal-02 as a counterexample.
    - Label C28's evidence P3-C[SUMIKA], and note the P3-C[LILJA] shared-dream rally.
  - Dependency: SAA-021.
- **SAA-138 · CMP10-C011 · R05 S.** Target: CORE-Ume §8; UME-C13 (a "P2 vs D-UME" note at most).
  - Error: under the heading 'Series 2 / N.I.A.', the P2 dream-and-review response is merged with D-UME's win, fan entrustment and sister-play.
  - Evidence: pstory_002_hume_after-audition-a-normal-03 L50–L118; dear_012 L124–L199; dear_015 L116–L289; dear_016 L76–L243; dear_029 L410–L432.
  - Change: REVISE. Add P2 and D-UME track labels, as §24 requires.
- **SAA-141 · CMP11-C009 · R01 S.** Target: CORE-Misuzu §16; BRL 'Phase 3 — Misuzu branch divergence'.
  - Error: "Producer reveals his own huge dream: to achieve something history-making".
  - Evidence: adv_dear_hmsz_027 L323–L355 (three-way choice; 'history-making' is branch 3, L354–L355) and L376–L440 (shared tail).
  - Change: REVISE. Name the player-selected root, and keep as invariant the shared dream 'あなたをトップアイドルにする'. C30/C31 stand.
- **SAA-143 · CMP11-C015 · R01 Q.** Target: CONT 'Misuzu story-state additions — Phase 3' (STATE-MISUZU-P1); core §30 P1 caution.
  - Error: 'post-SyngUp! depression → …' is presented as the P1 state.
  - Evidence: P1 opening-normal-01 L4–L39; mid-normal-04 L78–L108 (branch); adv_dear_hmsz_037 L244–L311 (L305–L327 retrospective).
  - Change: REVISE, in R01's wording: "post-SyngUp! solo start → self-paced development → solo ambition". Note that solo-transition loneliness and the mediator habit appear only in selected branches, and that depression is D-MISUZU retrospective, not imported into P1. Apply the same caution to §30 P1[MISUZU].
- **SAA-145 · CMP12-C010 · R02 S.** Target: CORE-Sena §34, §8 (and §24 "debt structure").
  - Error: §34 says Sena "interprets his near-absence of leisure as evidence of dedication", and §8 faults her for not accounting for "family debt" in Dear 003.
  - Evidence: pevent_001_jsna_activity_011 L25, L79–L96 (branch 3); activity_008 branch 2 L58–L63; adv_dear_jsna_003 L305, L361–L397; adv_dear_jsna_023 L91, L104 (the optional recap).
  - Change: REVISE. Mark §34's reading as player-selected. Drop the debt from the Dear 003 list or mark it as later, cross-route knowledge.
- **SAA-151 · CMP13-C012 · R03 S.** Target: CORE-Tsubame §8 and §34; TSB-018 is already correctly scoped.
  - Error: "Her endpoint is personally specific…" for the P1 true end, without branch scope.
  - Evidence: pstory_001_atbm_ending-true-01 L213–L252; ending-normal-05 L80–L100 (conditional trust); dear_020 L328 ('貴様がいなければ、私は空に輝けんからな').
  - Change: REVISE. Scope the line to the true ending, and cite D020 L328 as the C1 Dear witness. **Do not adopt the school_003 L24 baseline** without an A1 check (integrator note).
- **SAA-157 · CMP15-C008 · R06 S (transition OPEN).** Target: E013–020 §1.2, §6.5, §12 (Sena↔Mao row); RSL Sena↔Mao (row 388).
  - Error: "E013/E017 … old failure to promise pursuit becomes present challenge" implies a progression.
  - Evidence: adv_event_017_main-04 L433–L472 (L472 'ずっと、目をそらしてきたんだ'); event_013 main-05 L462–L469 (the vow '今度こそ', no season anchor); event_022 main-05 L277–L289, L429–L460.
  - Change: add a bounded continuity note. Do not narrate the E013 vow as preceding the E017 advice; one economical order is E017/E022 → E022 resolution → E013 vow. Keep the order OPEN.
- **SAA-164 · CMP17-C012 · R03 S.** Target: RSL Phase 3 Sena deltas, row 'Sena – Misuzu' (row 228).
  - Error: "sovereign slow-tempo genius who resists Sena's kinetic norm; Begrazia partner" fuses two tracks.
  - Evidence: adv_unit_01-04_02 L169–L183, L242–L272 (Misuzu runs by choice, L272); 04_14 L214–L220; 04_22 L746–L785.
  - Change: REVISE. Split the row by track: in U1 Begrazia, Misuzu adopts the running tempo and returns to walking only after defeat, while "resists Sena's kinetic norm" is a D-MISUZU/event state. Phrase Sena's part as her statement.
- **SAA-167 · CMP17-C016 · R03 S.** Target: CORE-Temari §2.6 bullet.
  - Error: "nearly exits when center order triggers insecurity".
  - Evidence: adv_unit_01-03_12 L40–L302 (the comic tonkatsu-batter exit threat); 03_01 L150–L188 (centre order leads to Temari's rotation proposal).
  - Change: REVISE. Remove the bullet, or rewrite it as "stages a comic exit threat over Saki's health-policing of her food (03_12)".
  - Dependency: ⚠ §2.6 is also rescoped by SAA-032 (Batch 2), which builds on this edit in PR-3a.
- **SAA-204 · CMP05-C013 (—), plus the branch-label component of SAA-014 (CMP05-C001, R05 Q).** Target: CORE-Lilja §12 and §12.2.
  - Error: ending-true-01 is quoted as one statement, and §12.2 gives 'わたしの夢が終わっても……わたしと一緒にいてください' to Lilja without branch scope.
  - Evidence: pstory_001_kllj_ending-true-01 L71–L73 (choice), L95–L99 (branch 1), L101–L117 (branch 2), L118–L125 (shared tail); adv_dear_kllj_037 L321–L354 (choice at L321; in branch 1 the wording is the Producer's choice; in branch 2, at L348, it is Lilja's demand; the branches converge at L368–L406).
  - Change: REVISE the labels. Per R05 this component is P3-level; the remainder of SAA-014 is in Batch 3.

### 0-E. Ledger and reading factual errors

**SAA-033 · CMP18-C002 · P2 · CROSS_REFERENCE_GAP (identity) / OMITTED in kind (N.I.A. origin) · R08 Q · OA: yes**, merged with **SAA-252 · CMP12-C011 · P3 · CROSS_REFERENCE_GAP (—; OA: no)**

- **Target:**
  - SIDE §2.4, §5.1, §12 (OPEN list) and §13 (tiers).
  - NPC ledger: the Phase 2 '100 Pro head / 十王龍正' row, the D-MAO 'Ryuusei' row, the 'Sena's father' row and the R86 President Juo rows.
  - SPINE §4.2, §13.3 and §14.
  - INST: INST-NIA and INST-100PRO-NETWORK.
- **Existing claim:**
  - SIDE splits 'Sena's father' from 'Ryuusei Juo'.
  - The NPC ledger: "connected to Kunio through company transfer; exact personal relationship not established here … Reading/romanization and exact H.I.F. authority are not established". The D-MAO row leaves the relation to Kunio unresolved.
- **Evidence (SL1.0):**
  - adv_cidol-jsna-3-002_02 L192, L196 (Sena's father is 十王社長; the headmaster is her grandfather, L173); L200, L207, L243–L249.
  - adv_dear_amao_021 L381 (十王社長 = 十王龍正, 100プロ代表取締役).
  - adv_dear_jsna_012 L15–L17, L49–L52 (the headmaster attributes N.I.A.'s planning to Kuroi and his son; L205 親子喧嘩).
  - adv_dear_atbm_003 L196 and adv_dear_ttmr_011 L22 (ruby 100プロ = じゅうおうプロ).
  - adv_cidol-kllj-3-018_03 L45 (『ガラクタロード』 is '100プロの代表曲').
- **Change, qualified by R08:**
  1. REVISE: merge 'Sena's father', '十王社長', 'President Juo' and 'Ryuusei Juo / 十王龍正 (son of 十王邦夫)' into one entity across SIDE and the NPC rows, with jsna-3-002_02 L192 as the SL1.0 anchor. This also carries SAA-252's cross-link and brings the D-MAO conduct into Sena's family model and vice versa.
  2. STRENGTHEN SPINE §4.2/§14 and INST-NIA with the N.I.A. origin. Word it as the headmaster's C1 @ D-SENA account that N.I.A. was **co-planned** (not "co-founded") by Kuroi and his son, outside his own control. Add his remark that Hatsuboshi is "not fully monolithic". The identification of "his son" with 十王社長 is high-probability, not explicit, so label it as inference.
  3. Record the じゅうおうプロ ruby. Treat ガラクタロード's 100 Pro status as a cross-reference to the SL1.1 Sena refresh, which already has it.
  4. Qualify SIDE §5.1 with observer evidence: Ryuusei's offer to Mao stays professionally rational, while Sena observes him as capable, cunning and unwilling to release favoured idols (L243–L249). Keep 冷血漢 branch-bound and unnamed.
- **Benefit:** removes a split-entity error that affects Sena's family, Mao's 100 Pro arc and the institutional map, and records an omitted N.I.A. origin.
- **Dependencies:** SAA-034 and SAA-035 (Batch 3, institutions) build on it. ⚠ SIDE §2.4 is also targeted by SAA-089 and SAA-090. Sequence 033 first.
- **Owner adjudication: yes.** Components 2–4 may be deferred to PR-3 if the owner wants PR-1 limited to the identity fact.

**P3 ledger and reading facts (compact; all reviewed).**

- **SAA-121 · CMP02-C010 · R02 Q.** Targets and changes, as narrowed by R02:
  - (c) CSL D-TEMARI summer H.I.F. row: "agrees to SyngUp training/disbandment-live plan" **inverts a veto**. REVISE to "accepts SyngUp training; agrees with the Producer's veto to defer the dissolution live until after winter H.I.F." (adv_dear_ttmr_023 L468–L514).
  - (b) CORE-Temari §2.4: keep Temari's own tentative acknowledgement (L257). Delete the unsupported clause "the Producer's work may have helped produce the winning conditions". Add Sena's testimony as corroboration (dear_027 L113–L120). Do not move the whole causal point to the Producer.
  - (d) TMR-S03 reads "Rinha's tears". REVISE to "Rinha's apparent tears (Temari's question; see RINHA-C057)" (dear_016 L409–L423). This is a cross-reference, not a misreading.
- **SAA-146 · CMP12-C012 · R02 S.** Target: CSL 'Phase 3 Character 12 — Juo Sena' item 4.
  - Error: "Producing Kotone, Ume, China, Misuzu, Saki…".
  - Evidence: dear_jsna_025 L99–L131; 026 L50–L71; 022 L369; 028 L84; CORE-Sena §21 and §25.
  - Change: REVISE to "producing Kotone, Ume, China and Misuzu, and being challenged by Saki and the wider golden generation".
- **SAA-147 · CMP12-C013 · R02 Q · OA: yes.** Target: JVR 'Juo Sena — Phase 3 textual register baseline' (L260); CORE-Sena §0 (L46); AV-HYP-SENA-09 (L1229).
  - Error: the Sena baseline names the performer whom VPL assigns to Misuzu, and the core names another performer. Neither name is verified within the admitted record.
  - Change: REVISE all three to a neutral formulation ("Sena's voice performance") until an official credit (A4) is entered in the paratext register. Do not substitute one ledger's name for another. Also mark the item SOURCE_SCOPE_LIMITED.
- **SAA-150 · CMP13-C011 · R03 S.** Target: CORE-Tsubame §27 and §47 OQ#4.
  - Error: "Tsubame can now imagine professional life beyond school".
  - Evidence: adv_dear_atbm_003 L196 (a taken-for-granted plan at 100プロ, ruby じゅうおうプロ); dear_010 L338; SL1.1 cidol 015_03 L30–L36.
  - Change: REVISE. The wager binds Sena to Tsubame's long-standing plan. For OQ#4, add the baseline fact without resolving the question.
- **SAA-153 · CMP14-C003 · R07 Q.** Target: LEG SL1.2 row 2 (L334); NPC SL1.2 Kanae row (L525); KANAE §Dear 001–010 (D010 paragraph).
  - Error: "independent idol aspiration" and "emerging independent ambition".
  - Evidence: adv_dear_hkne_010 L243–L247, L369–L378; P1 ending-true-01 L191–L209; ending-normal-02 L117.
  - Change: REVISE "independent" to "own" or "self-declared, China-referenced". Add L247 and the L369–L373 dream content to the D010 paragraph. PRESERVE KANAE-R88-C02.
  - Note: this ledger edit touches PR #600's own SL1.2 rows (see §Closing).
- **SAA-154 · CMP14-C007 · R07 Q.** Target: KANAE §Produce Series 001 table, §Admission, §Dear 001–010.
  - Change: REVISE three repairs and narrow the fourth.
    - (1) "protects China's access to supplies" → "tastes the lozenge before China does", the taster reflex (after-step-2-normal-03 L84; cf. activity_007 L126 毒見).
    - (2) "stay from the headmaster" → "stay hidden from the headmaster".
    - (3) "screen potential" → "visual appeal" (ビジュアル, D001 L310).
    - (4) Narrowed by R07: **do not** gloss {user}様 as a servant's honorific for a master, because 様 is her default address to peers (D002 L35/L217; D006 L264/L457; JVR L620). At most add a cross-reference to JVR L623.
  - Note: this edits PR #600's own new reading.
- **SAA-159 · CMP16-C005 · R08 S (DOWNGRADE).** Target: S03b §17 (and its claim transition).
  - Error: "transparently maintaining Temari in her mental world"; "estrangement does not eliminate…".
  - Evidence: adv_csprt-3-0041_03 L131, L141 (あの子 unnamed), L176, L182; 3-0033_01 L83 (the earlier reconciliation).
  - Change: DOWNGRADE to "probably Temari; unnamed in the source". Drop the estrangement framing unless the scene's state is anchored, consistent with S03c §20 and S03d §9.
- **SAA-160 · CMP16-C006 · R08 S.** Target: S03b §1.1 table (story_0045) and the §21 heading.
  - Error: "second-year ensemble" and "the second-year layer".
  - Evidence: adv_csprt-3-0045_02 L44, L52, L115, L136; csprt-3-0015_02 L75, L83, L154 (1年2組 self-identification).
  - Change: REVISE to "Class 1-2 ensemble" and "the Class 1-2 layer".
- **SAA-261 · CMP13-C017 (—).** Target: CORE-Tsubame (global), EVM-Tsubame, RSL, NPC, SIDE.
  - Error: 'Tsukika' is used throughout for 白草月花.
  - Evidence: actorId=sgka and voice sud_vo_adv_dear_atbm_004_sgka-001, 013_sgka-001..002; no ruby on 月花 in the atbm Dear files.
  - Change: REVISE. Harmonise on the Japanese identity 白草月花 with one working romanization across homes. The actor code supports 'Gekka', and the Stage A readers used it independently. Record the metadata basis.
  - Note: the current form is an unattested reading, so this is cheap and global.

### 0-F. Misreadings correctable by rewording

All reviewed. Each conclusion survives; only the description of the mechanism changes.

- **SAA-119 · CMP01-C016 · R01 Q.** Target: CORE-Saki §3.2.9; echo only in §3.2.7 and §10.8.
  - Error: "the strongest version of his ideal might be the Saki who remains unsupported and unbroken".
  - Evidence: adv_dear_hski_023 L128–L133 (the plan presupposes defeat); L285 ('心折れ、ひとり強がる'); dear_020 L293–L294, L305, L314, L392–L549.
  - Change: REVISE. Read "unaided even when broken". Add only the echo between option 1's '共に終わればいい' and Dear 020 '一緒に終わりましょう'. Per R01, keep §3.2.7 and §10.8's over-identification warning in full, because Dear 023 rejects the burn-out legend but not the Producer's vow.
  - Note: hsca_exposure; no rediscovery credit.
- **SAA-131 · CMP09-C005 · R04 S.** Target: CORE-Sumika §14.3 (and the same scoping in §7); AVA-Sumika Love & Joy row; CSL artistic-coauthor row.
  - Error: "Now she wants to coauthor: lyrics; choreography; … styling; hair; fanservice".
  - Evidence: adv_cidol-ssmk-3-012_02 L55–L84 (choreography is hers), L112–L125, L148–L179; 012_03 L11 (**the Producer initiates the costume step**), L75–L93 (outfit chosen at her request for his taste), L97–L114 (ponytail at his request), L183–L192 (fanservice proposed by him and co-designed).
  - Change: REVISE to domain-split authorship. Note the omitted subject at 012_03 L221; read "she had come to rely too much on him" as primary and do not build on either reading.
- **SAA-137 · CMP10-C010 · R05 S.** Target: CORE-Ume §6.1; UME-C19.
  - Error: "not because a scoreboard can be gamed".
  - Evidence: adv_dear_hume_004 L197–L229 ('お互いが納得しないとダメ', L215; L221–L224).
  - Change: REVISE to "a measured superiority outside a mutually accepted contest does not count". PRESERVE the relational-legitimacy thesis.

**Batch 0 co-landing note.** Batch 6-A lists HSCA findings that are also plain factual or locator errors and that comparators confirmed still hold: HSCA-052, -097, -123, -128, -149, -157 and -165. They fit PR-1 and are listed there.

---

## Batch 1 — The four P1 integrations

All four were independently reviewed and checked in A1 by the principal, and all four carry the owner-adjudication flag. Each entry states the change in its post-review form. The ≤120-word **PROPOSAL** passages are drafting aids for the owner; they are not canonical text. Supplementary passages enter as a new subsection or dated note, with the existing text kept recoverable, following the 2026-11-12 correction precedent.

### 1-A. SAA-001 · CMP04-C001 · Mao: the promise as relational contract; the Dear 022–026 crisis · P1 · OMITTED · R04 Q · ADOPTED_QUALIFIED · OA: yes

- **Target:**
  - CORE-Mao §2.8 "Professional transition and H.I.F.: the question moves from self-acceptance to coauthorship".
  - A new §8 subsection after §8.4 "Producer as first fan".
  - §8.5 "Coauthorship can empower and enclose".
  - EVM-Mao MAO-C24, C25, C27 and a new MAO-C31.
  - RSL Mao–Producer rows; CSL D-MAO 100Pro transition.
  - SIDE §3.1 (Asari).
  - RS-II §9.2 and §9.5.
- **Existing claim:**
  - §2.8: "Mao refuses the replacement of her student Producer because the relationship itself has become part of the desired work."
  - §8.5: the coauthorship can be "enabling" or "enclosing"; "The text currently favors the enabling interpretation but does not eliminate the second."
  - MAO-C25: "autonomy-enhancing but power-asymmetric". Its falsifier is "Later sources showing Producer routinely accepts Mao's refusal/revision"; matrix §3 target 3 asks for "Any source where Mao refuses Producer interpretation or schedule authority".
  - No home mentions the 約束, the Dear 022 outburst, the Producer's acquiescence or Asari's Dear 024 lesson.
- **Evidence:**
  - adv_dear_amao_004 L100–L102.
  - dear_020 L230–L231, L284, L290.
  - dear_022 L365, L372–L377 (the anchor '約束したじゃないですか。／ボクを――可愛くて、カッコイイ、無敵の王子様にしてくれるって！'), L381–L414, L439, L453, L496.
  - dear_023 L489–L493, L574.
  - dear_024 L19–L27 ('決めるのは、麻央さんです。／プロデューサーとして――'), L83–L90 (Asari: 'アイドルの夢に、／きみ自身の夢を託すこと。'), L114–L120, L255–L269.
  - dear_025 L361, L522.
  - dear_026 L47, L74–L75, L95–L115.
  - dear_027 L712–L733.
  - P1 after-audition-mid-failure-01 L46–L73.
  - P3 selection-failure-01 L20–L35; P3 final-failure-01 L21, L34–L35, L44, L65.
  - The principal checked dear_022 L372–L377, dear_024 L19–L22 and dear_026 L74–L75.
- **Change, in the form qualified by R04:**
  1. STRENGTHEN: add the §8 subsection "The promise as relational contract" (passage below).
     - Bound the enforcement claim. Mao invokes the promise in D-MAO Dear 022 (C1) and only in P1 mid-failure **choice 1** (L52–L59) and P3 selection-failure (L29–L35). P1 mid-failure choice 2 shows the Producer's self-blame without an invocation.
     - Record the drift in the promise's content: 好きにならせる → 無敵の王子様 → トップアイドル / トッププロデューサー. Mao's Dear 022 wording is her own restatement, built on the Producer's Dear 004 vision.
     - Treat the P3 'トッププロデューサー' line as a cross-track echo, not a sequel to Dear 027.
  2. REVISE §2.8 to make the 100Pro arc two-sided:
     - The Producer presents his removal and calls the replacement '申し分のない' (L414).
     - Mao invokes the promise, insults him in Kansai and flees.
     - She recalls the promise and storms 100Pro alone (dear_023 L493, L574; dear_024 L255).
     - The Producer defers (dear_024 L19–L22) until Asari reframes the producer's first duty (L83–L90).
     - He admits '即答するべきだった' (dear_026 L74–L75).
  3. REVISE §8.5 and the MAO-C25 counter-pressure: Dear 022–025 **strengthens the evidence on both sides**. Mao acts first and refuses the Producer's interpretation, which satisfies matrix §3 target 3. Her stated need for him also deepens. Do **not** say it simply "narrows" the enclosing reading.
  4. PRESERVE §8.5's shared endpoint. Do not re-add mutualisation as new; cite dear_027 L712–L733 as its anchor.
  5. STRENGTHEN: add MAO-C31 ("the promise is the relational contract; Mao invokes it, branch-bound outside D-MAO; its content drifts toward a shared goal"), matching RSL/CSL rows, Asari's lesson in SIDE §3.1, and Mao in RS-II §9.2/§9.5 as the clearest test case for, and against, the "monopoly of interpretation" risk.
- **PROPOSAL (CORE-Mao §8, new subsection after §8.4, "The promise as relational contract"; 104 words):**

  > In D-MAO the Producer's single-option vow in Dear 004 ('俺があなたを、好きにならせます', L100–L102) becomes a 約束 renewed in Dear 020 (L230–L290). In Dear 022 Mao restates it in her own words ('無敵の王子様にしてくれるって', L374–L377), so its content drifts toward the prince ideal and later toward a shared top-idol goal. When the Producer calls his replacement '申し分のない' (L414) and then defers ('決めるのは、麻央さんです', Dear 024 L19–L22), Mao invokes the promise and acts before he does. Asari's lesson (Dear 024 L83–L90) and his admission '即答するべきだった' (Dear 026 L74–L75) close the rupture. Outside D-MAO, comparable invocations are branch-bound (P1 mid-failure choice 1; P3 selection-failure). The episode strengthens both readings in §8.5.

- **Benefit:** the most significant Mao–Producer omission in the corpus. It answers the matrix's own falsification target, it shows the Producer willing to step aside, and it gives RS-II §9 its clearest test case for the risk of interpretive monopoly.
- **Dependencies and competing changes:**
  - SAA-012 (Batch 0): MAO-C20 and §2.9 re-anchor; L516 ties the grief to going pro with the Producer.
  - SAA-057 (Batch 3): the Kansai distress register in Dear 022. Co-land with the §2.8 edit.
  - SAA-058 (Batch 2): Mao absent from RS-II §9.
  - ⚠ §8.5 is also the destination of SAA-194, the OPEN romance-coded evidence base (Batch 4). Keep 194's OPEN note in a separate paragraph.
  - ⚠ RS-II §9.2/§9.5 is a hotspot shared with SAA-014, 024, 044, 045, 058, 111, 114, 115 and 237 and with HSCA-038. Make one coordinated RS-II §9 edit (see §Closing).
  - This finding extends HSCA-011. Merge HSCA's "abandonment by adults" ground (dear_025 L347; P1 true L99) at adjudication, as CMP04 recommends.
- **AV:** optional. The Mao AV baseline could calibrate whether the Dear 022 outburst reads as comic or serious; the textual finding does not depend on it.
- **Owner adjudication: yes.**

### 1-B. SAA-002 · CMP07-C001 · Hiro: the owl origin and longing line · P1 · OMITTED · R07 S · ADOPTED · OA: yes

- **Target:**
  - CORE-Hiro §1 "Executive thesis — chosen impossibility becoming accountable attachment".
  - §9 (wording); §11 "The hidden かわいい motive…"; §12 "owl and the rejection of simplistic 'persona = lie' authenticity"; §16 "Dear 035: 'bare hands' are redefined"; §17–§18; §26.
  - EVM-Hiro HIRO-C01, C14, C22, C30.
  - SIDE §7.3 and §7.4.
  - NPC rows for owl and the former classmates; RSL Hiro ↔ owl and Hiro ↔ former university peers.
- **Existing claim:**
  - §1: Hiro "first enters idolhood because bodily unsuitability … offer[s] an escape from the boredom of effortless competence".
  - §11: かわいくなりたかった is admitted "in the communication crosswalked to her early idol motive".
  - HIRO-C14 counter-pressure: "Motive is disclosed retrospectively and was initially secondary".
  - §12 and SIDE §7.3 treat owl only as a persona theorist.
  - §16: the former classmates "write to her" and had "regarded her as a friend".
- **Evidence:**
  - adv_dear_shro_024 L155–L214 ('それが、きっかけ。', L203; the father to the Producer at L171–L177).
  - dear_010 L163–L205 (L183–L199, '…………かわいくなりたかった。').
  - dear_019 L31–L61.
  - dear_034 L562–L587 ('憧れを胸に、不可能に挑む。', L582).
  - dear_035 L128–L140, L189–L243 (the nameless isInner letter, L189 and L198), L265–L287.
  - dear_036 L631–L728 (L660), with the antecedent dear_025 L205–L209.
  - P1 after-audition-final-normal-03 L36–L46.
  - cidol-shro-3-018_01 L156–L162.
  - The principal verified dear_024 L185–L214, dear_035 L189–L212 and dear_036 L660.
  - Use A1 for dear_shro_035: SL1.1 source refresh L102 records an A2 omission.
- **Change, with R07's cautions applied:**
  1. STRENGTHEN §1/§11 and HIRO-C30 with an **added** origin and longing layer. Hiro names owl's summer H.I.F. live, glimpsed by chance on someone's device, as the trigger (dear_024 L185–L203). PRESERVE HIRO-C01's central claim that she had no pre-formed top-idol dream, and do not demote unsuitability, which cidol 018_01 L162 calls "not a single lie".
  2. REVISE the HIRO-C14 locator and its "retrospective" wording. The primary in-sequence anchor is dear_010 L183–L199; CIDOL 018 becomes the inner-speech retelling. Record Dear 019 branch 1 as the closure.
  3. REVISE §16 from the A1 letter text. The letter-writer's video was the trigger, the classmates held secret viewing parties, and their fandom became their own 趣味.
  4. STRENGTHEN §17–§18 with Hiro's formula (dear_034 L582) and the Dear 036 origin loop.
  5. REVISE §9's "Ume becomes the first idol Hiro sees" to "the first idol she sees perform live" (dear_008 L26 vs dear_024 L195).
  6. Flag P1 final-normal-03 L41–L43 and dear_019 L34–L44 as choice-1 only.
- **PROPOSAL (CORE-Hiro §1 and §11, origin layer; 117 words):**

  > Unsuitability remains Hiro's prepared and truthful account (CIDOL 018_01 L156–L162), and the core's claim that she had no pre-formed top-idol dream stands. D-HIRO adds a longing beneath it. In Dear 010 she answers the Producer's question about why idolhood at all with '…かわいくなりたかった' (L183–L199); CIDOL 018 later retells this in inner speech. In Dear 024 she names a chance glimpse of owl's summer H.I.F. live as 'それが、きっかけ' (L185–L203). Dear 034 gives her own formula, '憧れを胸に、不可能に挑む' (L582). In Dear 035 a letter from her former classmates identifies the video one of them was watching as that trigger (L189–L212), and Dear 036 returns to owl's defeat (L631–L728). P1 final-normal-03 L41–L43 and Dear 019 L34–L44 corroborate in choice 1 only.

- **Benefit:** the Hiro core can explain why she chose idolhood at all, not only why difficulty attracts her. It also corrects the §16 misreading of the letter and removes the "retrospective" qualifier where an in-sequence scene exists.
- **Dependencies and competing changes:**
  - ⚠ §11 and §13: SAA-018 (Batch 0, 神格 genealogy).
  - ⚠ §16: SAA-126 (Batch 0, speaker inversion and CIDOL 012 stage). Merge into one §16 edit.
  - ⚠ §17 and §20: SAA-066 (Batch 3, dream deferral and 不純).
  - SIDE §7.4 also receives SAA-126 and SAA-218.
  - AV H-AV-008 (cute desire) remains documentation-only.
  - Rediscovers HSCA-087, -089 and -163.
- **AV:** the delivery of dear_010 L199 and dear_024 L197 is optional AV-D.
- **Owner adjudication: yes.**

### 1-C. SAA-003 · CMP08-C001 · Rinami: the Producer's side of the romance · P1 · UNDERWEIGHTED · R06 Q · ADOPTED_QUALIFIED · OA: yes

- **Target:**
  - CORE-Rinami §6 "Romance is explicit, but its professional fusion is the real analytical problem": a new subsection.
  - §27 "Phase-3 bounded conclusions", items 11–12.
  - §28 "Open questions for later phases": a new OQ, next to OQ-RINAMI-03 "Producer/romance governance".
  - EVM-Rinami RINAMI-C10, plus a new OPEN row for the Producer-side asymmetry.
  - AVB-Rinami §12 (mature ethical formulation).
  - RSL Phase-3 AV R2 row Rinami ↔ Producer (row 316).
- **Existing claim:**
  - §6: "Rinami herself chooses to fuse romantic confession, lifelong mutual aid, and professional production into one vow".
  - RINAMI-C10 (VERY STRONG): fusion "by Rinami herself".
  - AVB §12: "Genuine mutual love and meaningful professional authority can coexist".
  - RSL: "explicit lover".
  - No home describes how the Producer answers her bids.
- **Evidence:**
  - adv_dear_hrnm_037 L433, L451, L453 (◆選択肢 [1] ――はい, hideMessage=true; the principal verified L433–L453).
  - dear_009 L307, L317, L324, L344, L349, L365.
  - dear_010 L347, L362, L385, L390.
  - dear_020 L410, L414, L429, L436, L437.
  - dear_026 L405, L412, L420, L421, L437.
  - dear_027 L13, L18.
  - cidol-000_02 L120; cidol-001_01 L206; cidol-008_02 L153.
  - P2 before-audition-a-normal-01 L58, L60, L68.
  - pevent_001 activity_010 L36, L71, L75.
  - P1 ending-true-01 L150, L156.
- **Change, in the form qualified by R06:**
  1. STRENGTHEN: add a §6 subsection on the bilateral mechanics (passage below): bid → professional reframing → deflation, with occasional correction; and the sibling/training frame as a shared pretext until Dear 020 retires it.
  2. REVISE RINAMI-C10 and §6/§27.11 by **supplementing**, not replacing, "by Rinami herself". The fusion is co-produced in idiom and authored by Rinami in voice.
  3. REVISE AVB §12 and RSL row 316 by **scoping, not downgrading**: "Rinami's explicit love; his acceptance through a hidden one-option はい; his romantic reciprocity strongly implied (dear_009 L307, 008_02 L153, dear_020 L436–L437, tears at dear_037 L65–L85) but never voiced". Leave out "suggested". Anything stronger is AV-dependent.
  4. OPEN: add a new OQ on the Producer's side. His motive may be obliviousness, restraint or both; cidol-001_01 L206 shows sincere obliviousness in at least one scene.
  5. Label branch-only lines in any ledger entry: activity_010 choices 1 and 3; dear_009 choice 1.
- **PROPOSAL (CORE-Rinami §6, new subsection, "How the Producer answers"; 117 words):**

  > In the Dear chain, Rinami's intimacy bids are repeatedly answered in professional terms; she deflates or protests; sometimes he corrects course (Dear 009 L307–L365, partly choice 1; 010 L347–L390; 020 L410–L437; 026 L405–L437; 027 L13–L18). The sibling and training frame serves both as a pretext until Dear 020 retires it. Her vow's wording is hers, but takes up the production idiom he kept supplying: training toward Prima Stella, an office in her hometown, 'トップアイドルにします'. His romantic reciprocity is strongly implied (Dear 009 L307; CIDOL 008_02 L153; Dear 020 L436–L437; Dear 037 L65–L85) but never voiced; he accepts her lifelong request through a hidden single-option '――はい' (Dear 037 L453). Whether his reframing is obliviousness, restraint or both stays OPEN.

- **Benefit:** the core explains the romance–production fusion, which it treats as central, through the mechanism that actually builds it. The "explicit lover" overstatement is scoped without being lost.
- **Dependencies and competing changes:**
  - Depends on SAA-071 (promise arc, §8/§11/§24), SAA-128 (§12 inner speech, Batch 0) and SAA-020 (Shion's scandal and governance).
  - ⚠ §6 also receives SAA-129(d). ⚠ §27 item 9 is in SAA-128. ⚠ OQ-RINAMI-03 is adjacent, so keep the new OQ distinct or fold it into OQ-RINAMI-03.
  - Related HSCA-044 (covert Producer interventions, Batch 6) and HSCA-038 (Rinami absent from RS-II §9).
- **AV:** the tone of cidol-002_02 L190, the pauses at dear_020 L419/L436, the tears at dear_037 L65–L85 and the facial staging on "ばか" (dear_009 L359–L364) all need AV. The textual finding does not depend on them.
- **Owner adjudication: yes.**

### 1-D. SAA-004 · CMP11-C001 · Misuzu: reciprocal jealousy origin; Kayo ranking; disclosure · P1 (narrowed) · OMITTED · R01 Q · ADOPTED_QUALIFIED with dissent · OA: yes

- **Target:**
  - CORE-Misuzu §7 "Idol origin: she watched Temari watching someone else"; §28.1 "Temari — first warmth / moon / rival / irreplaceable difference".
  - §3 "The V2 correction: her calm beginning contains real depression", §14 "Defeat: resentment is not absence of pain" and §25 (carry the disclosure arc).
  - EVM-Misuzu: a new claim and the C23 wording.
  - RS-I §5: a new subsection after §5.9. Number it §5.9.2, because §5.9.1 "Begrazia as a U1 counter-track (HSCA-001)" already exists. Also extend the §12.3 SyngUp routing to Misuzu Dear 021–037.
  - RSL Misuzu–Temari row; CSL 'Temari reconfiguration' row.
- **Existing claim:**
  - §7: "The mature route … teaches her how to turn this private wound into a professional aesthetic."
  - §3/§14: Misuzu is "skilled at governing exposure"; Dear 032 "adds retrospective evidence that young Misuzu has cried privately after major defeat and concealed it from Temari".
  - RS-I §12.3 routes only Misuzu Dear 001–020.
- **Evidence:**
  - adv_dear_hmsz_032 L186–L369 (L286, 'あの日の私は……燐羽と継さんに、／美鈴を取られたみたいに感じてた。'; L317–L327; L339–L343; L356–L369; L398).
  - dear_010 L264–L294 (L275, '大好きな友達の心が、／奪われてしまったように感じて。').
  - dear_034 L557–L635 (L594, '継さんよりも？　／燐羽よりも……ですか？'; L601–L612; L629–L635).
  - dear_036 L1047–L1276 (L1240–L1276, bare 手毬).
  - dear_022 L226–L246; dear_021 L299–L310; dear_009 L302.
  - The principal checked dear_032 L286, dear_010 L275 and dear_034 L594.
- **Change, in the form narrowed by R01:**
  1. STRENGTHEN §7 and §28.1: the founding triangle is reciprocal.
  2. STRENGTHEN with limiting evidence: the Kayo-ranking insecurity (L594) and Temari's refusal to rank (L601–L612) remain an unresolved asymmetry at the D endpoint.
  3. STRENGTHEN: the origin is told to Temari herself, in bare 手毬 (dear_036 L1240–L1276).
  4. REVISE §3, §14 and §25 **narrowly**. The concealment-to-disclosure arc is already recorded in AVB-Misuzu §6, the RSL AV delta and the CSL, so carry it into the core; do not claim total omission. In doing so:
     - Present 'あなたが言ったんですよ……目の前で泣いていいよ' as Misuzu's paraphrase of Temari's Dear 032 challenge (L339–L343, L398), which Temari only half-concedes.
     - Keep the Producer as a co-equal exception ('あなたと同じくらいに', L369).
     - Label D-TEMARI 018/022 as cross-track corroboration.
     - Cite dear_009 L302, where she cries before Temari when recognised. What develops is frustration tears and the disclosure of the origin, not tears as such.
  5. STRENGTHEN: add a matrix claim, the RS-I §5.9.2 subsection and the §12.3 routing to Dear 021–037.
- **PROPOSAL (CORE-Misuzu §7 and §28.1, reciprocal origin; 119 words):**

  > The founding triangle runs both ways. Misuzu felt her friend's heart 'stolen' by the sun idol (Dear 010 L275–L294); in Dear 032 Temari says she felt Misuzu 'taken' by Rinha and Kei, who moved Misuzu to tears that Temari's songs could not (L286, L317–L327). Dear 034 leaves an asymmetry open: Misuzu asks whether Temari ranks her above Kei and Rinha (L594), and Temari declines to rank (L601–L612). In Dear 036 Misuzu tells Temari, in bare 手毬, that her idol origin was watching Temari admire an idol (L1240–L1276). She had already cried before Temari when recognised (Dear 009 L302); what develops is open frustration and disclosure of the origin, with the Producer kept as an equal confidant (Dear 032 L369).

- **Benefit:** the Misuzu home and RS-I gain the reciprocal half of the founding triangle and the late Dear arc that RS-I has never routed.
- **Dependencies and competing changes:**
  - SAA-085 (§3/§14 crying context), SAA-140 (origin scope, C09/§7, Batch 2) and SAA-087 (bare 手毬 and plain register).
  - ⚠ RS-I §5.2/§5.9.1/§12.3 is a hotspot shared with SAA-032, 048, 049, 084, 106 and 110 and with the HSCA-001 residuals. Edit RS-I §5 in one pass (see §Closing).
  - ⚠ §14 also receives SAA-086 and SAA-249.
  - Dissent preserved: after reading HSCA-121, the specialist judged the finding borderline P2. R01 kept P1 in narrowed form, and the integrator adopted P1 (narrowed).
  - hsca_exposure is true, but Stage A readers A11 and A02 recorded the same scenes independently.
- **AV:** the delivery of the Dear 032/036 tears and the plain-register lines is optional AV-D.
- **Owner adjudication: yes**, including the severity dissent.

---

## Batch 2 — Cross-track propagation, by target file

Batch 2 carries evidence that lives in another character's route, in events, in support stories or in U1 to the home of the subject it concerns. Every addition keeps its track label, either C1 @ D-[host idol] or U1, so that host-track states are not merged into the subject's own track. P2s are given in full; P3s in compact form. Of the 61 findings here, only SAA-009, 022, 026, 032 and the P3s 120, 140, 156, 158, 162 and 163 were independently reviewed. Apply the reliability gate to the rest.

### 2-0. Structural owner decisions (decide before 2-1 to 2-19)

Three findings ask one architectural question: **do host-track and SL1.0 event or support states enter the Phase-3 cores, or only the syntheses and ledgers?** SAA-048 and SAA-113 depend on the same answer. Deciding this first fixes the destination of about a third of Batch 2.

**SAA-104 · CMP15-C001 · P2 · CROSS_REFERENCE_GAP · — · OA: yes**

- **Target:** each core, as a new dated "Phase-4 numbered-event integration" pointer section, **or** a scope statement in the `CURRENT_STATE_AND_CORPUS_MAP.md` Phase-4 checkpoint. Cross-reference the CSL Phase-4 rows.
- **Existing claim:** E001–005 §8 says "Phase 4 should not silently rewrite the character cores", and the same routing appears in E006–012 §9/§17, E013–020 §11/§18 and E021+ §10/§18. No SL1.0 numbered event is cited in any core, yet SL1.1 events 027/028/030 were inserted as dated supplements.
- **Evidence (examples):** event_012 main-02 L255, L721; event_010 main-04 L506–L509; event_022 main-01 L88–L92; event_014 main-05 L793–L807; event_020 main-03 L194–L211.
- **Change (STRENGTHEN, or OPEN until decided):** either per-core pointer tables or the scope statement. The pointer tables would cover, for example:
  - Lilja: E012 effort-as-免罪符 and the Saki 師匠 relation.
  - Hiro: E010-04 success no longer empty when the result has recipients; E014 suffering refused when friends bear the cost.
  - Mao: E022 and E028.
  - Kotone: E022 and E012.
  - Sumika: E003, E012, E018 and E020-03.
  - Misuzu: E014, E023 and the E013 hearsay.
  - Temari: E007, E016 and E023.

  The alternative is a corpus-map statement that the cores hold Phase-3 and SL1.1 material only, and that SL1.0 event deltas live in the event readings and the CSL until the monograph. **Erratum applied:** drop the Saki/Sena-pamphlet example; the Saki core already has Sena as Saki's idol origin and lacks only the E005-04 locator.
- **Benefit:** removes the "inverted integration": SL1.1 events reach the cores while SL1.0 events do not.
- **Dependencies:** SAA-105, SAA-156 and SAA-267 supply contents.
- **Owner adjudication: yes.**

**SAA-108 · CMP16-C004 · P2 · CROSS_REFERENCE_GAP (transition OPEN) · — · OA: yes**

- **Target:**
  - The verification-target sections of all 13 cores and their EVM R86 rows.
  - R86 "Core and ledger integration".
  - `CURRENT_STATE_AND_CORPUS_MAP.md` (Phase 5 status).
- **Existing claim:** S03d §33.4 makes integration of "durable character/relationship/… deltas" a Phase-5 exit condition, and the corpus map reports Phase 5 COMPLETE. R86's own core routing was executed only for the Saki, Mao, Rinami, Hiro and Lilja cores.
- **Evidence (examples):** csprt-2-0057_01 L31–L52; csprt-3-0113_02 L18–L36; csprt-3-0122_01 L77–L99.
- **Change (OPEN; owner decision).** Minimum:
  - (a) Execute R86's routing for the missing families: Misuzu 2-0055 and 2-0057; Temari 3-0106 and 3-0112; Kotone §2.4 and Sena, 3-0113; China §19, 3-0122; Sumika 3-0111.
  - (b) Add a forward-pointer block to each Phase-3 core listing which support-card verification questions Phase 5 answered, with the support-reading section and CSL row.

  Full SL1.0 integration can remain a Phase-7 monograph task.
- **Benefit:** the cores stop presenting answered questions as open.
- **Dependencies:** SAA-275 (Temari 3-0106), SAA-061 (China 3-0122) and SAA-243 (Misuzu CIDOL 020 R86 routing) execute parts of (a). Narrows HSCA-178.
- **Owner adjudication: yes.**

### 2-1. CORE-Saki and RS-I §3 (Hanami system)

**SAA-039 · CMP01-C006 · P2 · CROSS_REFERENCE_GAP · — · OA: yes**

- **Target:** CORE-Saki §3.2.13, §5.2–§5.3, §12.1, §12.5, §15.3; EVM-Saki SAKI-C02, C18, C26.
- **Existing claim:**
  - §3.2.13: "Tsubame's criticism—that an all-rounder may lack a singular weapon—forces Saki to revisit her repertoire".
  - §5.3: "Breadth can become indistinction".
  - §12.5 models Sena only as "summit and vacancy".
- **Evidence:** adv_dear_hski_025 L576–L654; adv_cidol-hski-3-018_03 L86–L145 (L98–L123); 019_02 L273–L316; dear_hski_030 L296–L471; unit_01-04_16 L318–L415.
- **Change:**
  - STRENGTHEN by crediting Sena as co-author of Saki's talent model. In Project Stardust, Sena reframes Saki's rapid acquisition, which Saki herself called a weakness in Dear 003, as the talent of increasing her usable cards (Dear 025). Saki cites this when she reinterprets her "life of running away" (018_03).
  - Add Sena's self-identification as a logic-driven all-rounder without a standout weapon (019_02) and the mirror readings: U1 04_16; E005 "enemy, not successor"; Sena core §25 "another me".
  - REVISE the Tsubame wording: her lesson ("自分の魅力を知れ") is an affirmative diagnosis that sets a task, not a rejection of breadth.
- **Benefit:** a co-author of Saki's self-model becomes visible in Saki's home.
- **Dependencies:** ⚠ CORE-Sena §25 / SENA-C40 is narrowed by SAA-027 (Batch 3; reciprocal inspiration), so coordinate the wording. Apply the SAA-104 erratum on the idol-origin example.
- **Owner adjudication: yes.**

**SAA-109 · CMP17-C001 · P2 · CROSS_REFERENCE_GAP · — · OA: no**

- **Target:** RS-I §3.2, §3.10, §12.1; RSL new U1 Saki ↔ Ume rows for Episodes 01–03; a CORE-Saki §3.2.3 cross-reference.
- **Existing claim:** 勝ち逃げ is routed only to Saki Dear 008–010, and RS-I §3.5.1 begins U1 coverage at 04_04.
- **Evidence:** adv_unit_01-02_09 L537–L554; 02_10 L169–L180; 04_12 L258; 04_24 L451; 01_03 L300; 04_21 L385–L390; 03_05 L455; 01_02.
- **Change (STRENGTHEN):**
  - U1 shows a managed unbeaten record by a different mechanism: pre-practising every contest Ume might choose, and a footrace already lost and concealed.
  - Saki stays in a contest after being overtaken for the first time in her life (04_12), and the concealment ends (04_21).
  - She counts 04_24 as her first real win over her sister, although she had said she had never lost (01_03 L300).
  - Record the sisters' mirror misperception (03_05 L455).
  - Promote 勝ち逃げ, the protected hierarchy, to a cross-track invariant (D-SAKI + U1) with a track-specific mechanism.
  - 1勝1敗 is Saki's line (SAA-166).
- **Benefit:** a central Hanami mechanism gains an independent track.
- **Dependencies:** ⚠ RS-I §12.1 and the RSL Saki ↔ Ume rows are also corrected by SAA-005 (Batch 0, PR-1); build on that correction. Rediscovers HSCA-056/135; narrows HSCA-134.
- **Owner adjudication:** no.

**SAA-114 · CMP17-C009 · P2 · UNDERWEIGHTED · — · OA: no**

- **Target:** CORE-Saki H-SAKI-05 (the U1 partial test); RS-II §9.2 ("Saki: witness to collapse").
- **Existing claim:** "Kotone, not the Producer, is the witness before whom Saki admits fear and sleeplessness… Kotone and Temari provide evidence of other kinds of witness."
- **Evidence:** adv_unit_01-04_07 L765–L824; 04_24 L268–L279, L436–L451.
- **Change (REVISE the partial test):** U1 also confirms the Producer's privileged witness function. Saki checks that Ume has gone before breaking down to the Producer (04_07), and only his permission lets her cry after victory (04_24). The witnesses are plural, but the Producer keeps exclusive access to the collapse. The causal question stays OPEN.
- **Benefit:** stops the U1 test reading as counterevidence to the witness hypothesis.
- **Dependencies:** ⚠ H-SAKI-05 also receives SAA-037 (Batch 3) and already carries the HSCA-002 D-UME paragraph; edit once. ⚠ RS-II §9 hotspot. Extends HSCA-049.
- **Owner adjudication:** no.

**P3 (compact):**

- **SAA-120 · CMP01-C021 · R01 Q · OA: yes.** Target: CORE-Saki §8.1 and §24 notes (rows 5 and 10).
  - Change: STRENGTHEN as cross-track corroboration, for example "motive-level shift voiced explicitly in D-MAO 031; role persists" (adv_dear_amao_031 L343–L404; in-track support dear_hski_021 and dear_hski_028 L234 'わたしの意志で').
  - Per R01, **do not** relabel the §24 rows as restored on D-MAO evidence alone.
  - Benefit: the strongest statement of Saki's own ambition reaches her home.
- **SAA-162 · CMP17-C002 · R03 Q.** Target: RS-I §3.5 and §3.10; CORE-Saki §8.4.
  - Change: REVISE the formula to something like "Saki can celebrate Ume sincerely while hiding how much it hurts".
  - Note that U1 frames the front as self-aware 強がり, a recurring U1 mode that ends in despair (04_10 L450; 04_16 L518), while D-SAKI frames it as truthful and ending in resolve.
  - Drop the proposal's "track-dependent concealment" thesis, because D-SAKI 023 L35 asks the same question.
  - Evidence: unit_01-04_07 L765–L824 (L802–L824); 04_20 L833/L837; 04_18 L270/L300.
- **SAA-176 · CMP01-C018 (—).** Target: CORE-Saki §3.6.1, §9, §3.2.5.
  - Change: REVISE §3.6.1. Saki refuses the supporter identity as a *substitute* for winning but embraces it as a complement ("future top idol and first-class idol supporter", support 0057_01 L137). Add the D-SAKI counterpart: Dear 010 L373–L394 (the Producer: she is not that 潔く) and Dear 023 L180. U1 01-02_09 L242–L313.
  - Benefit: removes a contradiction with the support layer.
- **SAA-177 · CMP01-C019 (—).** Target: CORE-Saki §15, §3.6, H-SAKI-03; U1 placement doc.
  - Change: STRENGTHEN. Saki voices the school credo that opens the tutorial (tutorial_first_cmmn-00 L110–L147), U1 (01-01_01 L129–L155) and Ume's Dear 001 (L106–L116). U1 04_25 L245–L304 reveals it as her Prima Stella speech.
  - AV-D: the audible voice is unchecked; the identification rests on script voice IDs.
  - Dependency: shares a destination with SAA-283 (Batch 4).
- **SAA-178 · CMP01-C020 (—).** Target: RS-I §3.1, §3.6, §3.7; cross-references in CORE-Saki §9.4 and §13.4.
  - Change: STRENGTHEN. Saki co-authors Ume's challenge song (cidol-hume-3-009_01 L233–L310; 009_03 L145–L286), co-commissions つよつよ最強エクササイズ with Sena, says the sisters made each other (dear_hume_028 L292–L459; 030 L339–L358), and makes the pre-final mutual fear confession (dear_hume_033 L225–L264).
  - Dependency: ⚠ RS-I §3.7 also receives SAA-023 (Batch 3, Ume receiving care); write one §3.7 edit.

### 2-2. CORE-Temari and RS-I §5 (SyngUp)

⚠ **Hotspot.** RS-I §5.2, §5.9.1 and §12.3 are targeted by SAA-004 (P1), 032, 048, 049, 084, 106, 110 and 140, and by the HSCA-001 residuals. Draft one consolidated RS-I §5 edit.

**SAA-032 · CMP17-C004 · P2 · CONTINUITY_ERROR · R03 S · OA: yes**

- **Target:** CORE-Temari §2.6; RS-I §5.2 and §5.9.1.
- **Existing claim:** §2.6 says the unit "threatens … the unresolved memory of being the weak center supported by stronger members". RS-I §5.2 says "Temari's core remembers SyngUp through inferiority".
- **Evidence:** adv_unit_01-01_11 L172–L221 (L181–L201, members asking her to slow down), L496–L536 (L496, a public lie blaming them); 01_13 L125–L160 (her own verdict of selfish overdrive); 01_12 L469–L480 (inner); 01_10 L550–L561; 04_17 L710–L798 (reputation cost; 'マイナス').
- **Change:**
  - REVISE: scope the "weak center" phrase to D-TEMARI. It arises from the Producer's reframe in Dear 004 (L159–L168) and from Temari's Dear 015 account.
  - STRENGTHEN RS-I §5.2/§5.9.1 with the U1 counter-account, including the 04_17 'マイナス' liability self-image, so that U1 is not presented as free of self-deprecation.
  - Note that §3.2.4's "not simply selfish rejection" is a D-track conclusion that U1 Temari contests in her own voice.
  - Keep OPEN whether the two self-accounts are compatible facets.
- **Benefit:** prevents a D-track reading from being stated as Temari's universal memory.
- **Dependencies:** ⚠ §2.6 is also edited by SAA-167 (Batch 0, PR-1); build on that edit. A02/B02 agreement on Temari is not independent. Rediscovers HSCA-100.
- **Owner adjudication: yes.**

**SAA-047 · CMP02-C013 · P2 · CROSS_REFERENCE_GAP · — · OA: no**

- **Target:** CORE-Temari §5.1, §25 Q19, §3.3.5; SIDE §2 (a new Temari family subsection, or an extension of §2.10); NPC.
- **Existing claim:** §5.1 says the childhood self-account "should not be accepted as a neutral objective profile". Q19 is open, and SIDE has no Temari family subsection.
- **Evidence:** adv_dear_ttmr_035 L206–L268; cidol-ttmr-3-009_01 L110–L126; adv_dear_hmsz_027 L141–L297 (D-MISUZU); SL1.1 event_027 main-02 L280–L404; csprt-3-0112_03 L49–L176.
- **Change (STRENGTHEN):**
  - Temari is from Kyoto, and her parents are close to the Hataya family.
  - Her parents attend H.I.F. and plan a book on raising a top idol, which she wants stopped.
  - The Producer reserves his barbs for her alone.
  - D-MISUZU 027 gives Misuzu's portrait of the child Temari as warm and disruptive, the one who "restored goodness" to her. This partly answers Q19 and supports §5.1.
  - Mark the SL1.1 items.
- **Benefit:** fills a missing family home.
- **Dependencies:** ⚠ SIDE §2.10 is also extended by SAA-245.
- **Owner adjudication:** no.

**SAA-048 · CMP02-C017 · P2 · CROSS_REFERENCE_GAP · — · OA: yes**

- **Target:** CORE-Temari §1.3/§16 (track note), §10.5, §17.4, §25 Q10/Q17; TMR-P03/P04 later tests; RS-I §5.13, §10 OPEN-RS1-08, §12.3.
- **Existing claim:** the core lists Temari-owned tracks plus U1 only. Q10 ("What happens when Temari is not the Producer's only assigned idol…?") is open. RS-I §5.13 and OPEN-RS1-08 rest on support 0097 alone.
- **Evidence:**
  - adv_dear_hmsz_017 L166–L229; 028 L39–L110; 033 L22–L356; 007 L93–L256.
  - dear_kcna_031 L92–L119, L505–L637.
  - dear_amao_030 L344.
  - dear_ssmk_025 L218–L523.
  - SL1.1: dear_atbm_033 L60–L112; dear_jsna_034 L51–L169.
- **Change (STRENGTHEN, strictly track-labelled):**
  - (a) D-MISUZU: the Producer keeps Temari fit for Misuzu's sake, then produces her "temporarily" and tells her she is secondary. Temari answers 'お互い様', offers him all three solos, admits early-SyngUp jealousy, loses to Misuzu and heads for 100 Pro.
  - (b) D-CHINA, D-MAO, and SL1.1 D-TSUBAME and D-SENA: once all three have reconciled, Temari and Misuzu skip winter H.I.F. to prepare the dissolution live ('二兎を追う'). Temari coaches China, Ume and Hiro and declares herself China's fan.
  - (c) D-SUMIKA: she advises against self-erasure ('自分を殺したら……輝けない').
  - These give partial answers to Q10, Q17 and OPEN-RS1-08.
- **Benefit:** RS-I's dissolution-live claim gets more than one witness.
- **Dependencies:** **the 2-0 architecture decision**; SAA-046, SAA-049; ⚠ RS-I §12.3. Extends HSCA-032.
- **Owner adjudication: yes.**

**SAA-049 · CMP02-C018 · P2 · UNDERWEIGHTED · — · OA: no**

- **Target:** CORE-Temari §2.3, §3.2.4, §3.2.12; TMR-S01; RS-I §5.2.
- **Existing claim:** §2.3 calls Misuzu "a singer Temari underestimated because Misuzu rarely exerted herself visibly".
- **Evidence:** adv_cidol-ttmr-3-007_02 L118–L155; dear_ttmr_022 L204–L231; dear_004 L62–L70, L159–L176; dear_011 L174–L182; dear_009 L274–L284; dear_hmsz_032 L186–L327.
- **Change:**
  - REVISE §2.3: Temari always judged Misuzu's ability "far greater" (dear_004; dear_009); she misread Misuzu's pace as laziness.
  - STRENGTHEN with the hierarchy's chronology: Temari was "the clumsiest" at formation; in Kei's heyday SyngUp was called Rinha's one-woman unit; later the public saw a Temari one-man unit.
  - Add to RS-I §5.2, as other-route memory, Temari's childhood jealousy that Rinha and Kei "took" Misuzu's tears (D-MISUZU 032).
- **Benefit:** corrects a misdescribed asymmetry inside the founding triangle.
- **Dependencies:** ⚠ RS-I §5.2 carries the same Dear 032 scene as SAA-004 (P1), so write them together. "One-woman unit" is shared with SAA-085 and SAA-290. Rediscovers HSCA-031/099.
- **Owner adjudication:** no.

**SAA-110 · CMP17-C005 · P2 · UNDERWEIGHTED · — · OA: no**

- **Target:** RS-I §5.9.1; the RSL 'Historical source corrections' Misuzu ↔ Temari row.
- **Existing claim:** §5.9.1 (the HSCA-001 correction) records the recruitment and run/walk resolution, but not the pact, Temari's prior belief or her "only me" inference.
- **Evidence:** adv_unit_01-04_08 L127–L153, L176–L215 (L193–L212), L452–L482; 04_04 L511–L527 (choice 2); 04_05 L406–L409; 04_14 L117–L148; 04_15 L425–L430.
- **Change (STRENGTHEN):**
  - (a) Temari's belief that Misuzu resents her (C3 at 04_04, shared at 04_05) is one character's reading, corrected by the other.
  - (b) The correction opens a new wound: Temari infers that the dream was only hers.
  - (c) Misuzu adopts Temari's old vocabulary and tempo (役に立ちます; 合わせてみた).
  - (d) Misuzu lobbies Sena to add Temari to Begrazia (04_14).
  - (e) The H.I.F. pact gives the rivalry explicit stakes.
- **Benefit:** completes HSCA-001's residual (a); see Batch 6-B.
- **Dependencies:** ⚠ RS-I §5.9.1.
- **Owner adjudication:** no.

**P3 (compact):**

- **SAA-275 · CMP16-C009 (—).** Target: EVM-Temari R86 rows; R86 row 3-0106.
  - Change: STRENGTHEN. Add a TMR-R86 row for 3-0106: reporting craft learned from Rinha, candour about weakness, and self-blame for burdening and holding back her 仲間 while crying daily (adv_csprt-3-0106_03 L122–L159). Replace "her own hardship" with that self-account, and leave the 仲間 referent unassigned.
  - Dependency: part of the SAA-108 (a) routing.
- **SAA-277 · CMP17-C010 (—).** Target: RS-I §5.7 and §5.12; RS-II §10.7.
  - Change: STRENGTHEN with U1 as an independent track. Kotone fetches Temari's hot-water bottle from the estranged former roommate, who still keeps it and asks "what are you to Mari-chan?" (01-02_07 L325–L515). Misuzu's jealousy turns into open hostility (04_01 L357, L392–L415) and resolves only at 04_17 L559.
  - Note the state dependence against support 3-0001_02.
  - Benefit: carries HSCA-001 residual (b); see 6-B.
- **SAA-281 · CMP17-C018 (—).** Target: RSL (a new U1 Sena ↔ Temari row); JVR.
  - Change: STRENGTHEN. Sena apologises for having accepted other producers' judgement that Temari is a minus to any unit (04_17 L710–L798). Temari deflects with "I'm the one loved one-sidedly", Saki's phrase about Ume (02_08 L643–L660), which recurs in C-TEMARI 015. Record it as a shared deflection register.

### 2-3. CORE-Misuzu

- **SAA-140 · CMP11-C005 · P3 · R01 Q.** Target: EVM-Misuzu C09/C10; CORE-Misuzu §7; RS-I §5.2.
  - Change: REVISE by scoping C09 and RS-I §5.2 to "@ D-MISUZU". Cite the P1 true ending (L113–L131) as the non-triangular telling of the same invariant: not admiration but the wish to be seen alone. Add Temari CIDOL 009_01–02 as outside corroboration (L110–L159, L167–L198; 'わたし<em>も</em>').
  - R01 nuance: Dear 010 L288–L294 makes the venue-wide wish simultaneous with the Temari wish. Soften the sequential reading in §7/C10 to "Temari first and foremost, the venue at once, the world later" (L356).
  - Dependency: ⚠ §7 is the destination of SAA-004 (P1), so land in PR-2 with 004.
- **SAA-245 · CMP11-C017 (—).** Target: SIDE §2.10; CORE-Misuzu §28.7.
  - Change: STRENGTHEN.
    - The Producer met her parents on signing day, and they attend her talk show (cidol-hmsz-3-014_03 L59–L116).
    - The parents' tea ritual reaches her through the Producer (dear_035 L200–L249).
    - She is an only child, with Temari as "big sister" (dear_027 L141–L200).
    - Her mother supplied the H.I.F. tickets that began both girls' idol dreams (Temari cidol 009_01 L110–L126).
    - E013 reports her as a Kyoto native (hearsay).
  - Dependency: ⚠ SIDE §2.10 is also extended by SAA-047.

### 2-4. CORE-Kotone

**SAA-009 · CMP03-C001 · P2 (P1 → P2) · CROSS_REFERENCE_GAP · R03 Q · OA: yes**

- **Target:**
  - CORE-Kotone §3.2, a new subsection after §3.2.13; §3.2.14; §9.2–§9.3; §11.2.
  - EVM-Kotone KOTO-C06/C08, with a cross-reference to CORE-Sena §24.
  - SIDE §2.2.
  - RSL Kotone ↔ family and Kotone ↔ Producer N.I.A. rows; CSL D-KOTONE Sena/N.I.A. row.
- **Existing claim:** §3.2.14 says that when the Producer brings family into the performance environment, "Kotone becomes emotionally unstable in a way that pure ranking pressure does not produce". §9.3 leaves open whether the Producer always tells her the truth or sometimes manages her through omission.
- **Evidence:** adv_dear_fktn_010 L102–L112; dear_012 L384–L422 (L403, L407); dear_013 L48–L63 (audience-only flashback, L53–L62); dear_018 L106–L176 (L116, L135–L136, L148, L153, L159, L170), L221–L231; dear_020 L14–L97 (L68–L97). D-SENA: jsna dear_023 L151–L192, L475–L528.
- **Change, narrowed by R03:**
  1. STRENGTHEN with a short spine paragraph, not a full subsection: D010 self-blame → D012 withheld trip, which Kotone consents not to ask about → D013 audience-only clue → D018 the family in the front row as the Producer's removal of 心労 ("best condition") → D020 "見つけられて、よかった".
  2. REVISE §3.2.14 narrowly: "emotionally unstable" becomes a composure break followed by release into resolve (L170, L221–L231). This is not an "opposite" function.
  3. REVISE §9.3 narrowly: the omission is temporary, consented to and disclosed on request, so it *partly* answers the OPEN without closing it.
  4. Cross-reference Sena §24 and the ledger rows; add a Producer-side counter-case to SIDE §2.2.

  **Exclude** the unverified E001 / D-SENA 016 add-on unless it is checked in A1.
- **Benefit:** Kotone's home gains the Producer's agency in the father arc, which today exists only in the Sena home.
- **Dependencies:** CMP12 framing (Sena §24). ⚠ CORE-Sena §24 also receives SAA-144/145 (Batch 0). Rediscovers HSCA-023.
- **AV:** optional AV-C staging (013 flashback L59–L62; 018 BGM change L138).
- **Owner adjudication: yes.**

**SAA-050 · CMP03-C002 · P2 · CROSS_REFERENCE_GAP · — · OA: no**

- **Target:** CORE-Kotone §0, §2.1, §3.2.9, §10.1; KOTO-C27, plus a new row; the claim implications in `GKM_KOTONE_TRANSCRIPT_REFRESH_20261112.md`; RSL Kotone ↔ Sena.
- **Existing claim:** §0/§2.1 frame Kotone's starting state as precarity, and 成り上がる as "vertical movement out of a material position". No home gives admiration of Sena as an origin of her decision to become an idol.
- **Evidence:** adv_dear_fktn_010 L58–L84; dear_013 L369–L467 (L467); D-SENA jsna dear_018 L213–L289 (L284); jsna dear_035 L311–L335; event_022 main-02 L118–L132; SL1.1 dear_fktn_031 L403–L426, dear_033 L256–L272, dear_037 L180; dear_030 L432.
- **Change (STRENGTHEN):**
  - Model a dual, text-stated origin: family rescue ('あたしがなんとかしなきゃ') and admiration of Sena, as coexisting explanations. E022 fuses the two.
  - Add the competing-motivation tension: her self-account ("money, fans and praise", D031 L335) against her frustration at not being Sena's No. 1 rival (D-SENA 027).
  - Cross-reference Sena §19.
- **Benefit:** corrects a one-factor origin.
- **Dependencies:** CMP12.
- **Owner adjudication:** no.

**SAA-051 · CMP03-C004 · P2 · CROSS_REFERENCE_GAP · — · OA: no**

- **Target:** KOTO-C13 and the EVM §4 Sena table; CORE-Kotone §10.2 and §18.5; RSL Kotone ↔ Sena.
- **Existing claim:** KOTO-C13 (moderate): "Kotone accepts Producer projection more readily than Sena projection; this difference remains ethically unresolved."
- **Evidence:** D-SENA: jsna dear_003 L230–L469 (the failed scout); jsna dear_013 L30–L37 (Sena's inner self-revision), L135–L250, L296, L328; jsna dear_016 L342–L425 (L355). SL1.1: support 3-0113.
- **Change:**
  - REVISE by scoping KOTO-C13 to D-KOTONE.
  - STRENGTHEN with the D-SENA counter-state. Sena revises her method and offers concrete material terms (a non-repayable scholarship tied to N.I.A.), and Kotone accepts her as producer. This supports §18.5's hypothesis that acceptance tracks method, consent and material context rather than the person.
  - Keep Kotone's resistance to being "known too well" (L355).
- **Benefit:** a claim stated as general becomes correctly scoped.
- **Dependencies:** ⚠ KOTO-C13 is also targeted by SAA-052 (Batch 3), so edit once. Rediscovers HSCA-116.
- **Owner adjudication:** no.

**SAA-112 · CMP17-C007 · P2 · OMITTED · — · OA: no**

- **Target:** RSL (a new U1 Kotone ↔ Sena row); cross-references in RS-II §8.1/§8.6; CORE-Kotone §3.6.
- **Existing claim:** the Kotone ↔ Sena rows cover D-KOTONE, E005 and support only.
- **Evidence:** adv_unit_01-04_22 L240–L252, L376–L391, L446; 04_01 L482–L582; 04_02 L371.
- **Change (STRENGTHEN):**
  - Sena noticed Kotone during spring break and kept scouting her at her workplace; Kotone took it as jokes.
  - Sena resents the Producer for taking "my Kotone".
  - After H.I.F., Sena calls Kotone her rival and herself a poor scout.
  - Keep Kotone's inner counterfactual (Sena would have been her saviour) attributed to her.
  - Note the cross-track invariant of repeated scouting, which D-KOTONE shares.
- **Benefit:** a U1 dyad absent from every home.
- **Dependencies:** ⚠ Kotone §3.6 also receives SAA-282.
- **Owner adjudication:** no.

**P3 (compact):**

- **SAA-156 · CMP15-C005 · R06 Q.** Target: E021+ §3 (and §11 promotions); RSL Sena ↔ Kotone (event-scoped row).
  - Change: STRENGTHEN. Kotone credits Sena with unspecified help that lets her cut part-time shifts, and Mao notes her curfew compliance (adv_event_022_main-04 L45–L76).
  - Per R06: keep the help unspecified; drop the proposed qualification of RSL row 474; keep "first explicit easing" tentative.
- **SAA-191 · CMP03-C016 (—).** Target: CORE-Kotone §1.4, §3.2.7, §11.1–§11.2; KOTO-C07/C08; INST.
  - Change: REVISE §1.4 with in-track SL1.0 evidence:
    - Students with a producer receive eased scholarship terms (dear_fktn_003 L102–L104; the same rule as U1 01-01_07).
    - The refinancing combined the academy's system with an expert and depended on her results (dear_011 L182–L187); the Producer acknowledges overstepping (L124).
    - P-course grades depend on the idol's success (dear_001 L102–L111).
  - Benefit: answers a declared open question.
- **SAA-282 · CMP17-C019 (—).** Target: CORE-Kotone §3.6; RS-II §3.3.
  - Change: STRENGTHEN with the U1 Kotone ↔ Saki arc:
    - Hidden instrumental contempt (01-01_05 L155–L178).
    - The お姉ちゃん lever.
    - The leader choice, whose real reason (trust) is spoken only after Kotone leaves (03_01 L678–L708).
    - "I'm glad I formed a unit with you" (03_11 L554).

### 2-5. CORE-Mao

**SAA-056 · CMP04-C004 · P2 · UNDERWEIGHTED · — · OA: no**

- **Target:** CORE-Mao §2.3, §3.1, §9.3; EVM-Mao MAO-C01, C13, C23; RSL Mao–Sena.
- **Existing claim:** §2.3 says Mao "avoids the later acting career of the former prince she idolized because the woman's transformation feels like betrayal of the fixed image". The matrix cites cidol 015 only as "origin memory".
- **Evidence:** adv_cidol-amao-3-015_01 L9–L37; 015_02 L147–L206; 015_03 L62–L109; event_013 main-04 L225–L514; event_017 main-04 L383–L686; event_022 main-05 L277–L289; csprt-3-0078_03 L136–L154; cidol-amao-3-018_01 L218–L261.
- **Change (STRENGTHEN):**
  1. Add the cidol 015 arc:
     - In the nightmare, the child says 'ママ…わたしも王子様になるっ！'. As ボク she then renounces plush toys, sweets and 'あの人も――もう、イラナイ'.
     - She resents the idol who left the revue just as her own work collapsed.
     - She reclaims the failure years as her own ('ボクのものだから').
  2. Strengthen MAO-C23 with the mechanism: Mao avoided Sena partly because Sena re-embodied the lost idol (E017 inner speech; E022 avoidance; cidol 018_01). Support 3-0078_03 shows the wound persisting in ordinary scenes.
  3. Keep the C2/C4 scoping explicit.
- **Benefit:** a stated avoidance becomes an explained one.
- **Dependencies:** SAA-055 (Batch 3, the §2.3a pre-Producer story state) and SAA-192 (the revue star's name, Batch 4). ⚠ The E013/E017/E022 order is bounded OPEN (SAA-157), so do not narrate "a delayed answer to E013" as a fixed sequence. HSCA-008's narrower point is listed in 6-C.
- **Owner adjudication:** no.

**SAA-058 · CMP04-C010 · P2 · UNDERWEIGHTED · — · OA: no**

- **Target:** CORE-Mao §2.6, §9 (§9.1, §9.3, §9.7), §19; MAO-C18; RS-II §9.2 and §9.5; referrals to CORE-Sena and CORE-Tsubame.
- **Existing claim:**
  - §9.7: "Full support-card and event passes are still required".
  - §19: "How do Tsubame and other third-years describe Mao outside her own route?"
  - §2.6 narrates the Fluorite reframing without Rinami.
- **Evidence:**
  - csprt-2-0075_02 L132–L165.
  - event_013 main-04 L225–L514; event_021 main-04 L181–L288.
  - SL1.1: dear_atbm_031 L189–L285; dear_jsna_031 L286.
  - dear_hrnm_030 L186–L398; cidol-hrnm-3-018_02 L11–L271.
  - dear_amao_012 L330–L432; dear_amao_015 L78–L99; cidol-amao-3-000_02 L144–L178.
- **Change:** STRENGTHEN §9 from already-canonical event, support and other-route readings:
  - Tsubame: a rival-friend since first year, with Rinami as mediator. In E021, Mao, who did not reach the main stage, comforts the second-placed Tsubame. In D-TSUBAME 031 Mao admits she looked away from "you two", and Tsubame names her a rival.
  - Rinami: their first-year origin. Mao is the reason Rinami did not quit (D-RINAMI 030), and comforts her at her lowest. Rinami works as Mao's catalyst (cidol 000_02 Fluorite reframing; Dear 015; E003).
  - Juniors: Lilja (Dear 012), Kotone (E022), Temari (E011), and the repair of the Sumika overreach (E003).

  Also:
  - REVISE MAO-C18 narrowly: correction comes through rivalry, learned circumstances and self-correction.
  - Add Mao to RS-II §9.2/§9.5.
  - Flag the Sena and Tsubame owners.
- **Benefit:** Mao's cohort relations get a home; RS-II §9 gains a missing test case.
- **Dependencies:** SAA-001, 055, 056. ⚠ The RS-II §9 hotspot. ⚠ Mao §9.1 also receives SAA-076. ⚠ Tsubame §44 target #7 is also SAA-097. Rediscovers HSCA-036.
- **Owner adjudication:** no.

### 2-6. CORE-Lilja

- **SAA-197 · CMP05-C006 (—).** Target: CORE-Lilja §3, §7, §12.1; SIDE §14.2.
  - Change: STRENGTHEN. Saki is the generous counter-pole to Shion. Her respect rests on Lilja's resilience ('この子は、折れない'), and her words converge with the Producer's (adv_cidol-kllj-3-008_02 L91–L159, L171–L182, L262–L307; 008_01 L116–L128). D031 returns the respect (L41–L206).
  - Add Mao's D-MAO 012 reframing of persistence as talent (dear_amao_012 L325–L487) and E012-02 L592–L734.
  - This qualifies the Producer's near-monopoly on interpretation in §12.
- **SAA-200 · CMP05-C009 (—).** Target: the CORE-Lilja SL1.1 supplement and matrix SL1.1 table; RSL Lilja ↔ Producer.
  - Change: STRENGTHEN with a C022 row: role-inhabiting under a brief; buying with her own money; the Producer as self-declared fan '兼任'; Misuzu's wagashi (cidol-kllj-3-022_01 L49–L95, L166–L209; 022_02 L37–L161; 022_03 L109–L197). Cross-link E030 as a separately scoped campaign variant.
  - This executes COMMU86's own routing.
- **SAA-206 · CMP05-C015 (—).** Target: E001–005 §6.7; S03b §25; PSL (a new LOC-HSCA-006E or a note).
  - Change: STRENGTHEN. Link csprt-3-0049_02 L33 ('…雑魚がって？') to the E001 misattribution thread (event_001 main-02 L341–L382; main-05 L90–L102). Temari's image of Lilja as a harsh judge, authored by Sumika's dub, persists into ordinary life, and Lilja keeps disavowing it.

### 2-7. CORE-China

**SAA-062 · CMP06-C003 · P2 · CROSS_REFERENCE_GAP · — · OA: no**

- **Target:** CORE-China s4 (talent taxonomy) and s24 (counterpressure register); CHINA-C02/C05.
- **Existing claim:** s1 says "She is not secretly Sena-level at singing or dancing". The head's appraisal sits only in E001–005 s7.5.
- **Evidence:** adv_dear_kcna_003 L97, L109; dear_020 L240; dear_032 L164; P1 after-step-2-normal-03 L97, L109, L114, L118; P2 after-audition-b-normal-02 L23, L42.
- **Change (STRENGTHEN, as a labelled counterpressure):**
  - The head judges China's latent talent roughly equal to Sena's (D003).
  - The Producer first calls the comparison meaningless (L109), later concedes "the head's eye was right" (D020 L240), and P2 endorses it.
  - The head later ranks China above Sena "as an entertainer" (D032 L164).
  - PRESERVE C02 (her technique is genuinely weak) and the distinction between technique and latent talent. Note the appraiser's stake.
- **Benefit:** an authoritative in-text appraisal reaches China's home.
- **Dependencies:** CMP12, CMP15. Rediscovers HSCA-152.
- **Owner adjudication:** no.

**SAA-065 · CMP06-C016 · P2 · CROSS_REFERENCE_GAP · — · OA: no**

- **Target:** CORE-China s18, s22, s24.4; RSL China ↔ Sena; CSL China cross-track rows.
- **Existing claim:**
  - s18: "China repeatedly imagines her career as functionally impossible without him", with the Phase-7 test "Can China continue if this Producer is absent?".
  - s22 models China–Sena as aspiration, inheritance and rivalry only.
- **Evidence:** D-SENA dear_jsna_017 L226, L244, L253, L275; jsna_019 L162, L171, L179, L187; jsna_024 L105. D-HIRO dear_shro_027 L226, L347, L358; shro_033 L11, L139. Support 3-0015, 3-0032, 3-0066.
- **Change** (items recovered from `CMP06\candidates.jsonl`; the register keeps only the lead sentence):
  - REVISE by scoping s18's dependency claims to China-owned tracks.
  - STRENGTHEN with a cross-track paragraph:
    - TV work from the first day (D-SENA 017 L244–L275), the opposite of D-CHINA's slow-basics plan, which produces a variant tension ("I sometimes forget I am an idol").
    - Kuramoto-funded songs (D-SENA 024 L105; D-HIRO 033 Tokimeki no Solfege).
    - The support doctrine, voiced by Sena to China (D-SENA 019 L162–L187).
    - Hiro publicly names her top rival (D-HIRO 033 L139).
  - Record that the corpus answers "can China continue without this Producer" with track-separated states in which her core traits recur. Counterevidence: these states are mutually exclusive with D-CHINA and say nothing about separating from a producer she has bonded with.
- **Benefit:** an open Phase-7 test gains bounded cross-track evidence.
- **Dependencies:** CMP12, CMP07. ⚠ s18 is also narrowed by SAA-015 (Batch 3), so edit s18 once. Extends HSCA-077/166.
- **Owner adjudication:** no.

**SAA-102 · CMP14-C008 · P2 · CROSS_REFERENCE_GAP · — · OA: no**

- **Target:** CORE-China §22 and the SL1.2 supplement; CHINA-R88-C01; RS-II §8; JVR.
- **Existing claim:** the SL1.2 supplement says "she invites Kanae to aim for Prima Stella", and R88-C01 says "The new rivalry is an ambition". §22 and RS-II §8 do not mention Kanae.
- **Evidence:** adv_dear_hkne_002 L466–L474; dear_hkne_009 L557–L589; dear_hkne_001 L264–L282; adv_dear_kcna_011 L181–L241; dear_hkne_005 L423; csprt-3-0115_02 L45–L165.
- **Change (STRENGTHEN):**
  1. China explicitly models her role for Kanae on Sena's role for her (D002), and acts it out in the summit promise (D009). Register this as a succession case for RS-II §8.
  2. Link her refusal to command Kanae into a dream (D001) with her refusal to command fans' votes (D-CHINA 011) as one non-command principle.
  3. Note China's envy of Kanae's appearance (D005 L423).
  4. Note the relaxed plain and imperative register China reserves for Kanae, in the JVR.
- **Benefit:** the China side of the China–Kanae system.
- **Dependencies:** ⚠ R88-C01 is also edited by SAA-215. RS-II §8 is next revised under SAA-286. This touches PR #600's own SL1.2 supplement (see §Closing).
- **Owner adjudication:** no.

- **SAA-215 · CMP06-C015 (P3, —).** Target: CHINA-R88-C01, CHINA-C09; CORE-China s16, s3 and the SL1.2 supplement.
  - Change: STRENGTHEN by linking R88-C01 to C09/C08. China once ran her idol path through a household command to Kanae ("run the idol road with me", hkne_000-04 L264–L268, 言いつけ). At SL1.2 she refuses to command Kanae because obedience would turn a dream into duty (D001 L264–L282). Add D002 L466–L474 to s16.

### 2-8. CORE-Hiro

- **SAA-219 · CMP07-C014 (P3, —).** Target: CORE-Hiro §0, §9 and the SL1.1 supplement; BRL; RS-II.
  - Change: STRENGTHEN.
    - Outside her own tracks, Hiro is semi-produced by Sena, and China's Producer claims part of the credit (dear_kcna_014 L39–L98; dear_ttmr_029 L69–L109), so the Producer-relationship conclusions should be scoped to Hiro's tracks.
    - Link the Dear 030 mutual "left behind" (dear_shro_030 L341–L394) to CIDOL 022's 'また' (022_02 L193–L212).
    - Treat the Dear 013 goods-hoarder and D-CHINA's Nadeshiko (dear_kcna_013 L110–L203) as a parallel only.

### 2-9. CORE-Rinami

**SAA-075 · CMP08-C008 · P2 · CROSS_REFERENCE_GAP · — · OA: no**

- **Target:** CORE-Rinami §22; RINAMI-C12; CORE-Sena (a new Rinami subsection in its relationship section); RSL Rinami ↔ Sena.
- **Existing claim:** §22 models Sena only as pedestal and peerization, and RINAMI-C12 says "The Producer's childhood memory provides privileged access to a relational capacity". The Sena core contains no Rinami evidence.
- **Evidence:** adv_cidol-hrnm-3-007_02 L171–L191; dear_hrnm_012 L236, L245, L252, L256 (Sena inner speech); dear_018 L194; dear_023 L203–L220; dear_027 L723; support 0038_02 L96–L126; support 0053_01 L111–L129.
- **Change (STRENGTHEN):**
  - Sena, the institution's talent-reader and an aspiring producer, says she could not see or draw out Rinami's charm ('不明を恥じる'; '私に見えないなにか'; '私の眼では測れない').
  - Support material shows her privately predicting latent potential and reading Rinami's deference ('私に勝つことに遠慮してない？').
  - Rinami credits Sena with that ability (D018 L194).
  - Scope each perspective to its track.
- **Benefit:** Sena's voice on Rinami reaches both homes.
- **Dependencies:** SAA-074; SENA-C05 / SAA-091 ("truth exceeds legibility"). Rediscovers HSCA-037; extends HSCA-071.
- **Owner adjudication:** no.

**SAA-076 · CMP08-C017 · P2 · CROSS_REFERENCE_GAP · — · OA: yes**

- **Target:**
  - CORE-Rinami §21 and OQ-RINAMI-07.
  - CORE-Mao §9.1.
  - RSL Rinami ↔ Mao RippleSign row.
  - SONG ledger SUGAR FLAVOR rows; AV source crosswalk, SUGAR FLAVOR communication row.
- **Existing claim:**
  - Rinami §21: "Rinami herself chooses Mao…". Mao §9.1: "Later she asks Rinami."
  - AVA: "PHASE-3 BILATERAL CLOSE". RSL AV R2: "very high Phase-3 bilateral".
  - The AV crosswalk maps SUGAR FLAVOR to amao 017, while the Rinami song delta uses CIDOL 018.
- **Evidence:** hrnm cidol-018_01 L172–L221 (L180, L192, L209, L213); 018_02 L11–L94 (L29, L55, L60); amao cidol-017_01 L127–L198 (L176, L193); 017_02 L8–L131 (L17, L21, L50, L67, L98), L160–L238.
- **Change:**
  - REVISE: record two non-additive C4 origin scenes with opposite initiators, and scope "Rinami herself chooses" and "Mao asks" to their own versions. The invariant is an earlier Rinami proposal that Mao refused, followed by an eventual mutual choice.
  - OPEN: reopen OQ-RINAMI-07's bilateral close at the level of origin narrative.
  - AV agreement on the performance is unaffected.
- **Benefit:** stops one origin version being stated as fact in two cores.
- **Dependencies:** ⚠ Mao §9.1 also receives SAA-058. ⚠ Rinami §21 also receives SAA-129(f). Rediscovers HSCA-014.
- **Owner adjudication: yes.**

- **SAA-227 · CMP08-C018 (P3, —).** Target: CORE-Rinami (a new cross-track index) or the CONT Rinami delta.
  - Change: STRENGTHEN with track-bound states:
    - D-MAO: Rinami loses QUARTET to Shion, steers Mao toward the fans, and recovers through Mao's FINALE.
    - D-KOTONE: cheer squad; reaches the winter H.I.F. main event.
    - D-TSUBAME (SL1.1): qualifies after Tsubame's push at the festival.
    - D-SENA: a relaunch with Mao.
    - U1 01-03_04, branch 3.
  - RSL rows L793/L795 already hold two of these.
- **SAA-284 · CMP17-C021 (P3, —, transition OPEN).** Target: RSL Rinami rows.
  - Change: record the branch-only U1 line that implies prior acquaintance (unit_01-03_04 L104–L147, L248–L315) as C3 corroboration of the D-RINAMI childhood link. Leave the unasked question open.

### 2-10. CORE-Sumika and SIDE §2.9

**SAA-022 · CMP09-C004 · P2 · CROSS_REFERENCE_GAP · R04 S · OA: no**

- **Target:** SIDE §2.9; NPC Phase 3 Sumika side-character deltas and the SL1.1 block (L131); CORE-Sumika §2 and the SL1.1 refresh.
- **Existing claim:** SIDE §2.9 calls the family evidence "less individually interior" and concludes "It is provenance". The NPC row says "family interiority limited".
- **Evidence:** SL1.0: adv_dear_ssmk_010 L169; cidol-ssmk-3-014_02 L141–L154; event_020 main-03 L194–L211; dear_032 L414; csprt-3-0093_01 L164–L169; dear_026 L15–L82. SL1.1: cidol-ssmk-3-018_03 L62–L335.
- **Change (STRENGTHEN):**
  - Record the SL1.0 family strain:
    - Ballet began at the parents' instruction.
    - She falls silent when asked about cramped home life.
    - Gyaru style as rebellion against her mother.
    - Fear of telling the parents she wanted idolhood.
    - The mother's "she skips" warning and Sumika's rebuff.
  - Propagate the SL1.1 repair, which already reached the core, matrix, CSL and RSL, to SIDE and the NPC ledger. R04 adds two conditions: label the Dear 032 link as a cross-track identification, and record the father's support as mother-reported.
  - Reframe the family from "provenance" alone to provenance plus a conflict over who authors her assigned future. Keep the SL1.1 facts labelled to the Sumika-winning state.
- **Benefit:** the side synthesis and NPC ledger catch up with the core.
- **Dependencies:** SAA-078 uses the same E020 line. Rediscovers HSCA-170.
- **Owner adjudication:** no.

- **SAA-232 · CMP09-C013 (P3, —).** Target: RS-I §2, §4.1, §6.1; CORE-Sumika §8 and §20.
  - Change: STRENGTHEN with Sumika-side evidence that the courage at the origin was mutual. Lilja's agreement gave Sumika the courage to enter Hatsuboshi (dear_ssmk_036 L1044–L1053), and Lilja was her refuge from loneliness in Sweden (dear_032 L339–L356).
  - Note that the cause of Sumika's return is track-dependent: Lilja's live in D-LILJA (dear_kllj_010 L192–L241), the Producer in D-SUMIKA.
  - Note that 寄り添う is inherited from the Producer's stance.

### 2-11. CORE-Ume

**SAA-113 · CMP17-C008 · P2 · SOURCE_SCOPE_LIMITED (transition OPEN) · — · OA: yes**

- **Target:** CORE-Ume (scope statement and §22), **or** RS-I §3.5.1 together with the RSL Sena–Ume row.
- **Existing claim:** the Ume core's source boundary is the 204-object bundle, with no unit_01. RS-I §3.5.1 says the Ume core "is deliberately unchanged".
- **Evidence:** adv_unit_01-03_05 L419–L602; 03_08 L82–L191; 04_14 L617–L700; 04_19 L187; 04_23 L823.
- **Change (OPEN until the 2-0 decision):** either admit U1 Ume scenes to the Ume core under a U1 label, or give them an explicit home in the relationship layer. The content:
  - Ume initiates the Sena relation, and Sena demands proof she is not "just talk".
  - The Producer's half-month production, and his statement that he wanted to produce her.
  - Ume's belief that she loses to Saki in talent.
  - Ume reorients Sena from numbers to emotion, and adopts keeping Sena on stage as her first self-authored dream.
  - "Producer-chan".

  Close the ledger's Sena–Ume test for U1.
- **Benefit:** ends a scope decision that keeps Ume's U1 development out of every home.
- **Dependencies:** the 2-0 architecture decision; CMP10, CMP12. Extends HSCA-140.
- **Owner adjudication: yes.**

- **SAA-236 · CMP10-C014 (P3, —).** Target: SIDE §4.5 and open question 12; CORE-Ume §19.
  - Change: STRENGTHEN with the D-UME evidence: Kuroi is 理事長 of 極月学園; the Gekka/Shion cluster; his direct invitation of Ume to 961; the Producer's refusal, which is invariant across a three-way choice (dear_hume_010-01 L104–L129; dear_016 L8–L60); and standing poaching offers (dear_035 L148–L263).
  - Note in core §19 that 961 is a live alternative Ume weighs.
  - Dependency: ⚠ SIDE §4.5/§4.6/Q12 is also targeted by SAA-035 (Batch 3), so write one Gokugetsu/961 edit.
- **SAA-237 · CMP10-C015 (P3 after erratum, —) · OA: yes.** Target: CORE-Ume §22.5; RS-II §9.2/§9.9; RSL.
  - Change: STRENGTHEN. In D-UME Sena is Ume's would-be producer: she scouted Ume, lost the debate, frames H.I.F. as "producer versus producer", offers the physical-maximisation counterfactual (dear_032 L432–L441, L552–L570) and concedes (dear_036 L396, L465–L477; cidol-hume-3-012_01 L92–L204; dear_027 L243–L244).
  - In other tracks Sena is Ume's producer.
  - Dependency: ⚠ the RS-II §9 hotspot.

### 2-12. CORE-Sena

**SAA-026 · CMP12-C001 · P2 (P1 → P2) · CROSS_REFERENCE_GAP · R02 Q · OA: yes**

- **Target:**
  - CORE-Sena: a new sibling subsection after "U1 counter-track — Begrazia retirement and reversal", and §40 OPEN-SENA-12.
  - AVA-Sena §2, claim transition SN-R18.
  - RS-II §13.7 (Sena).
  - CSL "Phase 3 Character 12 — Juo Sena".
- **Existing claim:**
  - OPEN-SENA-12: "Phase 3 contains branch losses and fear, but not the full mature consequence of losing the reformed crown."
  - SN-R18 (OPEN): "Current route verifies fear and victory, not a later major defeat."
  - RS-II §13.7 omits every defeat and hollowing state.
- **Evidence:** adv_dear_hski_024 L336–L382 (to L430); adv_dear_amao_036 L302–L306; adv_dear_kllj_036 L583; D-HIRO 036 L757–L805. The other states are in the owning cores.
- **Change, qualified by R02:**
  1. REVISE OPEN-SENA-12 and SN-R18 from "evidence absent" to cite the SL1.1 P3-SENA final-failure test and the cross-route Dear 036 states, keeping integration open.
  2. STRENGTHEN with a short, scoped cross-route note after the U1 counter-track, giving each route's state separately.
  3. Treat D-SAKI 024 as its own counter-state to §15 and SENA-C03: success as a producer hollows the idol, who then re-ignites as challenger. Cross-reference Saki §3.2.10.
  4. Add one bullet to RS-II §13.7.
  5. Drop the counterevidence claim that D-HIRO is "brief and formulaic".
- **Benefit:** an "evidence absent" statement that is no longer true is corrected.
- **Dependencies:** the owning cores and BRL result rows. ⚠ §40 also receives SAA-254 (an OPEN entry on the romance reading). Rediscovers HSCA-069; extends HSCA-013.
- **AV:** the delivery of the defeat responses (AV-HYP-SENA-09) remains AV-dependent.
- **Owner adjudication: yes.**

- **SAA-285 · CMP17-C022 (P3, —).** Target: RS-II §5.9, §8.6, §8.7.1.
  - Change: STRENGTHEN by naming a cross-track invariant. Sena plans to retire into producing and is turned back by a junior or partner whose agency differs by track: Ume and Re;IRIS in U1 (01-04_14 L342–L506, L617–L700; 04_23 L93), Tsubame in D-TSUBAME, the Producer in D-SENA.

### 2-13. CORE-Tsubame

**SAA-097 · CMP13-C009 · P2 · CROSS_REFERENCE_GAP · — · OA: no**

- **Target:** CORE-Tsubame §44 (a resolution note) and §39 falsifier #6; RSL rows L166 and L181 (remove "Tsubame core pending"); RS-II §7.4.
- **Existing claim:** §44 targets #1–2 and #7, and §39 falsifier #6 ("She systematically blocks juniors from surpassing or correcting her"), are left as future tests. The RSL rows say "Tsubame core pending".
- **Evidence:** adv_dear_ssmk_032 L23–L177; dear_hski_032 L31–L127; dear_hrnm_032 L20–L92; SL1.1 dear_fktn_032 L22–L116; dear_amao_022 L203–L276; dear_atbm_000 L389–L435.
- **Change (STRENGTHEN):**
  - In four other Dear routes Tsubame is the senior obstacle at Selection who loses and then publicly blesses the winner.
  - In D-SUMIKA the reflex 'この私が、星南以外に負けるだと' persists late in the year, which shows that D-TSUBAME's individuation is route-specific.
  - Add the Mao relation evidence: the D000 witness, and Tsubame's relief at Mao's 100プロ entry (D-AMAO 022).
- **Benefit:** answers the core's own falsifier and clears stale "pending" flags.
- **Dependencies:** the SAA-058 referral. Rediscovers HSCA-022.
- **Owner adjudication:** no.

- **SAA-262 · CMP13-C018 (P3, —).** Target: RSL SL1.1 table; RS-II SL1.1 section; JVR; the CONT-013 annotation; `GKM_TSUBAME_WINTER_HIF_SOURCE_REFRESH.md`.
  - Change: STRENGTHEN by executing the refresh's own routing: D-TSUBAME rows for Mao (031–032), Kotone (033), Shion/Gekka (034) and the Producer (034–037); 殻/牙 and Kotone's 貴様 in the JVR; mark CONT-013 as superseded by the R86 row.
  - Add three omitted SL1.1 details to the refresh body: dear_atbm_028 L47–L82, dear_033 L937–L979 and dear_035 L288–L320.

### 2-14. KANAE reading (SL1.2; PR #600 content)

**SAA-098 · CMP14-C001 · P2 · CROSS_REFERENCE_GAP · — · OA: yes**

- **Target:** KANAE §Entering boundary, or a new section after it; NPC L96 row and SL1.2 Kanae row; JVR L612 (蕭何 row).
- **Existing claim:** the reading's source boundary cites only the previously admitted Kanae horizontal chapters. §Admission cites L376–L425 only for the scholarship essay, and the 直訴 at L425 is left uninterpreted.
- **Evidence:** adv_dear_hkne_001 L421–L425; cidol-kcna-3-009_02 L120–L204 (L162); adv_dear_kcna_024 L21–L26, L46–L48, L118–L123, L136–L157; dear_kcna_023 L353; dear_kcna_011 L153; cidol-shro-3-016_03 L117–L121.
- **Change (STRENGTHEN):**
  1. Interpret D001 L425 through cidol 009_02. D001 is the first explicit textual support for identifying the commu's same-age maid apprentice as Kanae.
  2. Record dear_kcna_024 L21–L48 as the first attestation of Kanae casting herself as China's 蕭何 within the 漢の三傑 model she proposes, with her Han Xin warning to the Producer (L118–L123).
  3. Record the earlier attestations of the vow formula (dear_kcna_023 L353) and of fan-club member No. 9.
  4. List the ordinary-life witnesses 0072_03, 0074_02, 0088_02, 0103_03 (SL1.0) and 3-0122 (SL1.1).
  5. Back-link NPC L96 to D001 L425.
- **Benefit:** PR #600's new reading gains its SL1.0/1.1 entering evidence.
- **Dependencies:** SAA-103, 101, 212. Per CMP14's HSCA reconciliation, this chain makes HSCA-151's "inference only" label too weak.
- **Owner adjudication: yes.**

**SAA-103 · CMP14-C009 · P2 · CROSS_REFERENCE_GAP · — · OA: yes**

- **Target:** KANAE claim table KANAE-R88-C03 and §Admission; RSL SL1.2 Kanae ↔ Producer row.
- **Existing claim:** RSL: "provisional trainer and trainee become collaborators in the Dear chain". KANAE-R88-C03: "Kanae moves from an agreement to acquire knowledge under threat of reporting…".
- **Evidence:** adv_dear_kcna_024 L118–L151; cidol-kcna-3-016_01 L82–L89, L171–L198; SL1.1 cidol-kcna-3-018_03 L68–L70; dear_kcna_023 L353–L385; dear_kcna_021 L247–L323, L421; cidol-kcna-3-014_03 L82.
- **Change (REVISE, qualifying the claim):** the Dear chain is not the start of the relationship. Four earlier stages exist:
  - She vetted him at their first meeting and stayed prickly for more than half a year.
  - She was a co-member of China's 仲間 and joined him in restraining the grandfather.
  - She competed with him openly over China.
  - At SL1.1 she revalues him: 見直しました.

  D001's conditional contract therefore restarts the guardian stance in a new role, and D010 is a second, closer cycle. Keep the D-CHINA and Kanae Dear tracks separately classified.
- **Benefit:** stops PR #600's claim reading as a first encounter.
- **Dependencies:** SAA-098. ⚠ KANAE-R88-C03 also receives SAA-152 (Batch 4, residual scope).
- **Owner adjudication: yes.**

### 2-15. RS-II structure (U1 Producer node; the trio; China–Kanae)

**SAA-111 · CMP17-C006 · P2 · OMITTED · — · OA: yes**

- **Target:** RS-II §9.2, §9.5, §9.11.
- **Existing claim:** §1.2 says the Producer "cannot be treated as one simultaneous multi-idol manager unless the source explicitly creates that shared state". §9.2 and §9.5 do not use U1, the track that creates that state.
- **Evidence:** adv_unit_01-01_03 L409–L543; 03_04 L402; 03_08 L40–L276, L292–L681; 04_01 L120–L132; 04_11 L221–L333; 04_12 L464–L486.
- **Change (STRENGTHEN):** add a U1 subsection.
  - Three exclusive bonds were cultivated in secret and revealed as a unit; each girl had believed she was the only one.
  - Jealousy across a shared Producer: Temari's "cheater"; Saki's "you can't have her".
  - Concealed strategy: raising Ume as the strongest rival; filming Ume as a boost item; a secret contingency duo shared only with Kotone, which angers Saki.
  - The Producer is framed as a fourth member (4 vs 3).
  - The institutional verdict names "an idol who nurtures idols".
- **Benefit:** §9.5's interpretive-monopoly risk gets its clearest concealment-based instance, in the one track with a shared multi-idol state.
- **Dependencies:** CMP18. ⚠ The RS-II §9 hotspot. Extends HSCA-026, including the Kotone branch of 04_04.
- **Owner adjudication: yes.**

- **SAA-163 · CMP17-C003 (P3) · R03 Q.** Target: RS-II §3.3 or §3.9; the CORE-Saki §3.6.1 table; RSL U1 Saki ↔ Temari.
  - Change: STRENGTHEN with a short note: "Temari revives Saki by returning Saki's own recruitment speech ('あのときの言葉、そのまま返してやる', 04_09 L482) while denying that it is encouragement (L548)". Evidence: 01_11 L645–L653; 01_12 L469–L602; 04_09 L348–L517, with a replay at L373–L386.
  - Optionally enrich Temari §2.6's "provocation".
- **SAA-278 · CMP17-C011 (P3, —).** Target: RSL U1 formation-row note; RS-II §3.2.
  - Change: STRENGTHEN by closing the open question for U1. Temari names the unit "hated, worst-compatible… reliable enemies" (04_18 L729), and Kotone denies friendship (04_17 L475–L491). Add to §3.2 the founding contract: mutual dislike frees Temari from SyngUp guilt (01_13 L529–L672; 01_14 L196–L331).
- **SAA-286 · CMP17-C023 (P3, —; SOURCE_SCOPE_LIMITED, OPEN).** Target: RS-II §4, or a new subsection at its next revision beyond SL1.0.
  - Change: link §4.5 (hospitality modelled on the recipient) and §8 (succession) to China's refusal to command Kanae (hkne_000-03 L962, L1009; hkne_001 L264–L282).
  - This is not an error, because RS-II's boundary is SL1.0. It can share the edit with SAA-102.

### 2-16. Events into RS-I and the cores

**SAA-105 · CMP15-C002 · P2 · UNDERWEIGHTED · — · OA: no**

- **Target:** RS-I §4.3, §4.12, §12.2 (or §6); pointers from CORE-Lilja (courage circulation) and CORE-Saki (pedagogy).
- **Existing claim:** E006–012 §8.7 ("One system, two opposite errors") promotes Saki as "a major peer-development node". RS-I §12.2 lists only "Event 012 — bilateral support / temporary-unit evidence", and RS-I §4.3 builds REVERSI concealment without E012.
- **Evidence:** adv_event_012_main-02 L126–L255 (L255), L592–L734 (L721); 012-03 L475, L501, L555–L697 (L561 '嘘つきの目'); 012-04 L500–L506; 012-05 L151, L195–L200; 012-01 L120; 030-05 L650–L655.
- **Change (STRENGTHEN):**
  - The same concealment structure appears in event continuity, where a third party, Saki, breaks it.
  - It is paired with Lilja's mirror error: continuing to run as her 免罪符 for standing beside Sumika (012-02 L255).
  - The bilateral contract (012-05) is the event-continuity precursor of the §4.4 care reversal.
  - Add a §4.12 row, and give Saki ↔ Lilja (師匠) and Saki ↔ Sumika a synthesis home.
- **Benefit:** an event the event reading treats as among the strongest evidence reaches the synthesis.
- **Dependencies:** SAA-104. ⚠ RS-I §4.3 also carries the HSCA-005 bilateral-concealment residual (SAA-123, Batch 6). HSCA-045, Saki's "lying to fight" (Batch 6-A), concerns the same E012-04 exchange; co-land them. The AV queue already holds P0 targets for 012-02/-03/-05. Rediscovers HSCA-078.
- **Owner adjudication:** no.

**SAA-106 · CMP15-C003 · P2 · CROSS_REFERENCE_GAP · — · OA: no**

- **Target:** E001–005 §4.6, §7.6, §9.2, §13.10; RSL L341 and L348; CSL L424; PIX E002 row; RS-I §5.7–§5.8 and §12.3.
- **Existing claim:** §4.6: "Temari is the leading identification of this unnamed friend … should therefore remain an explicit analytical inference … until cross-source confirmation is cited."
- **Evidence:** adv_event_002_main-05 L85–L101; 005-03 L145–L176, L402–L446; 008-02 L25–L30, L99; 010-01 L164–L178; 014-04 L463, L476; 023-01 L250–L272. SL1.1: 027-01 L117–L145; 027-05 L234–L280.
- **Change:**
  - STRENGTHEN by attaching the SL1.0 locators and upgrading the identification to "strongly supported by cross-event evidence; unnamed in E002".
  - Keep the motive OPEN, but add the bearing evidence: Sena could scout only one SyngUp member and set Temari aside (005-03 L151–L176); Misuzu's repeated council invitations, as 「また」 shows (SL1.1 E027-01 L130–L145); Temari's later understanding (E027-05 L268–L273).
  - Record the competing readings.
  - Add E002, E005, E010 and E014 to RS-I §12.3 and §5.7–§5.8.
- **Benefit:** completes the event reading's own condition for the identification ("until cross-source confirmation is cited").
- **Dependencies:** ⚠ the RS-I §12.3 hotspot. Rediscovers HSCA-117; extends HSCA-155.
- **Owner adjudication:** no.

### 2-17. Support readings

- **SAA-274 · CMP16-C007 (P3, —).** Target: S01 §6.1; S02a §6.
  - Change: STRENGTHEN. Identify the trainer's "circumstances" as most probably Rinami's assigned little-sister persona from Love☆しすたぁず (csprt-1-0004_01 L51, L57, L65; 3-0064_03 L115, L123). Reword the REVISE so that "little-sister" names an assigned persona, not an identity.
  - Add 2-0004_02 L71 as Rinami's own report of failing that persona.

### 2-18. SIDE and NPC

- **SAA-287 · CMP18-C004 (P3, —).** Target: NPC Asari row; SIDE §3.1.
  - Change: STRENGTHEN. Link the C4 dream pair to E029 and support 0019–20 as one recurring motif: the 2026 dream repeats E029's 'わたしの――プロデューサーくん' (startup_2025_ef-01_cmmn-02 L36–L88; 2026 cmmn-02 L85, L108–L117). Keep it explicitly non-biographical.
  - Add Asari's claim to have watched several past 一番星 winners (school_2-004 L22).
  - Dependency: ⚠ SIDE §3.1 also receives Asari's Dear 024 lesson (SAA-001).

### 2-19. Kaya Rinha crosswalk and matrix (support-route evidence)

- **SAA-158 · CMP16-C002 (P3) · R08 Q · OA: yes (dissent preserved).** Target: S03a §13; XW support-story rows (XW-109 onward); RMX; PIX rows S3-0011 and S3-0033.
  - Change: STRENGTHEN, as narrowed by R08:
    - In S03a §13, record that Misuzu names estranged 大切なお友達 in both class 1-1 and class 1-3 (csprt-3-0011_01 L81, L107–L112). The class-3 referent is probably Rinha, who is 元1年3組 (atbm_012 L445; hume_012 L151). Keep this as inference.
    - S03b §9 already covers 3-0033_02 interpretively, so for that object only the crosswalk row is missing.
    - Base the matrix claim on XW-030 (explicit), with 3-0011_01 as corroboration. Place it relationally (before the Temari reconciliation, while Rinha was still in 1-3), not as "early first-year".
    - Add supplementary crosswalk rows **without reopening the 118-object denominator**.
    - Mark the PIX additions, Temari included, as probable or unnamed references.
  - Dissent: HSCA-119 disputes the identification on transfer timing. R08 finds that it holds by inference only. The integrator adopted it at P3 with an explicit inference label.
  - Dependencies: ⚠ the XW counts are also touched by SAA-117 (Batch 3), SAA-242 (Batch 4) and SAA-165 (Batch 6), and by HSCA-159 (Batch 6-A). Edit XW once, keeping the 620-message display-name count and any actor-resolved count as separate figures.

---

## Batch 3 — Other P2 additions and narrowings, by target file

This batch covers the 73 P2s not handled in Batches 0–2. Seventeen were reviewed: those numbered between SAA-007 and SAA-035. The other 56 are `ACCEPTED_SPECIALIST_ONLY`, so apply the reliability gate. Each entry has four lines:

1. **T/C:** target, then the existing claim.
2. **A1:** evidence.
3. **Change:** with its claim transition.
4. **Benefit · Deps · OA.**

### 3-1. CORE-Saki

**SAA-036 · CMP01-C003 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Saki §4.1, §7.5, §17.1; SAKI-C03. §4.1 lists five functions of confidence; §7.5 treats only the "loser's duty"; §17.1 reads Saki's gloating as "humiliating Ume playfully".
- **A1:** adv_dear_hski_027 L257–L294; P1 after-audition-mid-normal-04 L17–L27; adv_dear_hume_006 L173–L186; P2-UME final-normal-01 L34–L55.
- **Change (STRENGTHEN):** add a sixth function, answerability to opponents. Saki's habitual rule, as the Producer recalls it ('あなたはいつも言っていました'), is that she owes those she has beaten a proud stance, so she performs confidence over real doubt (Dear 027). The same ethic appears in:
  - her restraint before failed entrants (P1);
  - her lesson to Ume to know her own level out of respect for the day's opponents (D-UME 006);
  - in Ume's account, her full celebration of wins as "competition manners" that let the loser grieve cleanly (P2-UME; Ume §6.3).

  Pair with §7.5 and qualify §17.1.
- **Benefit:** the winner's and the loser's duties are modelled together. **Deps:** Ume §6.3 already holds the Ume side; SAA-023. **OA:** no.

**SAA-037 · CMP01-C004 · OMITTED · — · OA: yes**

- **T/C:** CORE-Saki §19 H-SAKI-05; §26 (a new dear_033 locator); an EVM row for the H-SAKI-05 test. H-SAKI-05 says: "The mature Saki can be broken and continue because the Producer provides a stable witness … Test needed: evidence of continuation without the Producer". The partial tests cite only U1 and D-UME.
- **A1:** adv_dear_hski_021 L419–L481 (L468–L474); dear_033 L258–L307 (isInner at L258, L262, L286, L290, L294, L300, L307).
- **Change (STRENGTHEN):** add a D-SAKI partial-test paragraph.
  - Before the summer H.I.F., Saki says that without the Producer she would have lost somewhere in N.I.A. and "shattered". He answers that she would have gone on, perhaps with someone else's support.
  - After the loss, her inner monologue concludes that without him she would still have watched Ume's success with the same face and sung with her feelings turned to flame.
  - In Saki's own model, the Producer is necessary for the competitive outcome but not for the indomitable response.
  - H-SAKI-05 remains OPEN as a causal claim.
- **Benefit:** the hypothesis gets an in-track test. **Deps:** ⚠ H-SAKI-05 also receives SAA-114 and carries the HSCA-002 paragraph, so edit once. hsca_exposure: no independent-rediscovery credit. AV-D optional. **OA: yes.**

**SAA-038 · CMP01-C005 · OMITTED · — · OA: no**

- **T/C:** CORE-Saki §3.2.3, §3.2.14, §4.3, §26 SAKI-L018; SAKI-C04 later-falsification target. 勝ち逃げ is read as protecting the sister hierarchy; SAKI-L018 indexes Dear 037 only for "title responsibility".
- **A1:** adv_dear_hski_036 L431–L525; dear_037 L308–L400; dear_008 L180–L193; unit_01-04_24 L436–L451.
- **Change (STRENGTHEN):** add a closure beat.
  - (a) Dear 036 'わたしの勝ちよ！！ … やっと……言えたわ。遅くなって、ごめんなさい' answers Dear 008's "I have never once truly beaten my sister". U1 04_24 has "for the first time in my life".
  - (b) In Dear 037 the athletes from Saki's former sports watch her. She expects the grudge "you ran away from our contest"; their message is "our contest wasn't over" and "not bad", and she cannot stop crying. This widens 勝ち逃げ beyond the sister race and reframes flight as an unfinished contest.
- **Benefit:** the 勝ち逃げ arc gains its endpoint. **Deps:** ⚠ §3.2.3 is also edited by SAA-040 and cross-referenced by SAA-109. Extends HSCA-134. **OA:** no.

**SAA-040 · CMP01-C007 · OMITTED · — · OA: no**

- **T/C:** CORE-Saki §10.1, §3.2.3; RS-I §3.1; SAKI-C13. §10.1 lists praise without completion, challenge to the self-model, external perspective, body protection, usable stages and witnessing. RS-I §3.1 argues mutual construction mainly from Ume's side.
- **A1:** adv_dear_hski_006 L205–L284 (choice at L246; branch 2 at L254–L262); dear_008 L145–L161, L277.
- **Change (STRENGTHEN):** add the Producer's explicit theory of Saki's plateau.
  - What Ume has and Saki lacks is "a big sister": a reliable relative, a skilled trainer and a superior rival at her side. 'There aren't two of me' / 'that is why there is a Producer' (Dear 006).
  - In branch 2 only, Saki mutters that he already is a reliable relative.
  - Dear 008 completes the theory: the missing ingredient is a serious match with a superior rival she cannot bear to lose to.
  - This explains why being overtaken is framed as growth, why Saki later recruits Tsubame as a stand-in Prima Stella (Dear 029), and why Project Stardust is built from superior rivals.
- **Benefit:** a core mechanism stated by the text itself. **Deps:** ⚠ §3.2.3 (SAA-038). Rediscovers HSCA-050. **OA:** no.

**SAA-041 · CMP01-C008 · UNDERWEIGHTED · — · OA: yes**

- **T/C:** CORE-Saki §10.4, §10.6, §10.8, §17.5, §21; SAKI-C15. §10.8 says "The pair may become self-sealing"; §21 asks "Does the Producer's exclusive dream burden Saki in scenes outside the core route?"; SAKI-L044 indexes 012 only as "pair exclusivity".
- **A1:** adv_cidol-hski-3-012_01 L165–L271 (single choice at L230); 012_03 L42–L74, L106–L169.
- **Change (STRENGTHEN):**
  - In C-SAKI 012 a P-course simulation shows Saki has very high aptitude for unit work.
  - The Producer recalls that he scouted only her because he wanted to monopolise her (single option). Saki reciprocates, orders him to keep producing only her, and turns the counterfactual into another self to beat.
  - The aptitude is then rechannelled into joint lessons with Temari and Kotone (012_03).
  - Record this as the clearest case of exclusivity shaping a career-structure choice, together with its mitigation.
- **Benefit:** answers §21's own question. **Deps:** ⚠ §10.6 also receives SAA-173 (Batch 4). Extends HSCA-137. **OA: yes.**

### 3-2. CORE-Temari

**SAA-007 · CMP02-C004 · OMITTED · R02 Q · OA: no**

- **T/C:** CORE-Temari §6.2 (with a cross-reference from §3.1.1) and §2.4; TMR-C09, extended or as a new row; CSL D-TEMARI winter preparation row. §6.2 says: "High variance is the central technical problem … pacing, stamina, emotional regulation, and repertoire matter more".
- **A1:** adv_dear_ttmr_025 L376, L432–L444; dear_026 L23–L40, L245–L246; dear_027 L207–L251 (L231, L240–L251); dear_035 L613; cf. dear_004 L105–L127, dear_006 L290.
- **Change (STRENGTHEN, as qualified by R02):** attach the STEP3 technical turn to §3.1.1's existing "preserve the peak" strategy as route evidence, not as a freestanding claim.
  - (1) The Producer shifts from cutting the downside through stamina to raising the upside through giant-killing bouts at 961.
  - (2) He sets an "unlosable" three-bout series that forces efficient stamina use, a format signalled only by an emphasised たち (dear_025 L376), not "a format change she was not told about". Coordinate with SAA-044.
  - (3) Her "could control myself" is a one-series self-report, bounded by the Producer's doubt at L231.
  - (4) Frame the turn as variance embraced and the ceiling raised, not as "resolution" (dear_026 L245–L246; dear_035 L613 上ブレした月村手毬).
  - Link to TMR-C09 as a second strand.
- **Benefit:** the "central technical problem" gets its route evidence. **Deps:** ⚠ §2.4 is also edited by SAA-121(b) and SAA-043; SAA-044. Extends HSCA-098. **OA:** no.

**SAA-008 · CMP02-C006 · MISINTERPRETED · R02 Q · OA: no**

- **T/C:** CORE-Temari §3.2.10, §11.1, §11.2, §26; TMR-F02; the EVM §0 source-family note.
  - §3.2.10 sits under "Dear Idol", but its scene is Event 008, and it reads Temari as nearly treating a fan's attachment as invalid.
  - §11.1: "plural attachment is an important corrective to her own possessive instincts".
  - The §26 locator reads "dear_016–020; related fan dialogue".
- **A1:** adv_dear_ttmr_016 L181–L246 (L217–L246); dear_035 L520–L540 (L528–L536); event_008 main-02 L90–L99, L262, L310; event_011 main-03 L207, L229.
- **Change (REVISE, as qualified by R02):**
  - Credit Temari with the D-TEMARI articulation of plural, non-transferable fandom. She draws it from her own history as a fan (Kei retires, she grieves, she comes to love Rinha) and uses it to rebut Rinha's plan to hand her fans to "someone". Rinha adopts it at Dear 035.
  - Retain her competitive possessiveness (E008 L310). The accurate model is that she articulates plural fandom about her own fandom, discounts herself as an object of fandom (E008 L99), and competes possessively for fans.
  - Ground the "inability to show delight" in E011 L207/L229, and read E008 L262 as denial of an authored image.
  - Cross-reference E006–012 §4.2 instead of re-deriving E008.
  - Relabel §3.2.10 as Event 008, and fix the §26 locator: dear_017–020 contain no fan scene.
  - Keep §11.2's critique of asset logic, now with Temari as its in-text counter-voice.
- **Benefit:** reverses an authorship error on Temari's key ethic. **Deps:** HSCA-096/178. **OA:** no.

**SAA-042 · CMP02-C002 · CROSS_REFERENCE_GAP · — · OA: no**

- **T/C:** CORE-Temari §3.2.9, §9.1, §17.5; TMR-S05; RSL Temari ↔ Rinha "SyngUp past"; PSL TEM-L006 (add the denial locator); the Temari core pass report finding 15, by annotation only (see §Closing on frozen reports). §9.1 gives Rinha's distortion as "self-erasing protection", and §17.5 cites "Rinha's reputational sacrifice".
- **A1:** adv_dear_ttmr_015 L116–L143 (Temari's account) and L146–L185 (Rinha's on-the-spot denial); cidol-ttmr-3-007_02 L118–L136.
- **Change (DOWNGRADE motive language to effect language):**
  - Public hostility shifted onto Rinha. The protective motive is contested and OPEN.
  - Record in §3.2.9 that Rinha rejects the "good person" reading on the spot.
  - Model Temari's idealising memory ('私が覚えていれば'; '美化しすぎ') as characterisation of Temari.
  - Cross-reference RINHA-C034/C035.
- **Benefit:** stops an unconfirmed motive being stated as fact. **Deps:** the delivery of the denial is already in the Rinha AV queue; the Rinha gate is unaffected. **OA:** no.

**SAA-043 · CMP02-C003 · CROSS_REFERENCE_GAP · — · OA: no**

- **T/C:** CORE-Temari §3.2 (a new subsection between §3.2.13 and §3.2.14, or within §3.2.7/§3.2.9), §2.4 and the §26 locator row; the EVM §7 sun row; PSL Phase 3 Temari locators. §26 says "Temari surpasses Rinha as origin model | dear_025–027", and §3.2.7 never names the childhood Prima Stella as Kei.
- **A1:** adv_cidol-ttmr-3-009_02 L103–L119; dear_011 L151–L162; dear_016 L196–L209 (L203); dear_025 L155–L289 (L155–L179); dear_026 L331–L374 (L340–L364); dear_037 L301–L322; cidol 018_02 L126–L140.
- **Change (STRENGTHEN):**
  1. Kei is the H.I.F. Prima Stella of Temari's childhood origin. Her admiration moved to Rinha after Kei's implied retirement.
  2. Rinha's present stage is a complete copy of Kei that she refuses to train beyond, and the subject is taboo.
  3. Temari surpasses her "first idol" through that copy, winning in the auditorium where she first watched, and then demands that Rinha overtake her again.
  4. Dear 037 closes the loop: the Producer likens her to "the songstress of the sun", and she imagines becoming someone else's origin.
  5. REVISE the EVM §7 sun row: the sun's referent shifts by track.
- **Benefit:** names the hidden third figure in Temari's origin. **Deps:** ⚠ §2.4 (SAA-007, SAA-121). HSCA-159 (a past Prima Stella named 賀陽 in D-MAO, Batch 6-A) is adjacent. **OA:** no.

**SAA-044 · CMP02-C005 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Temari §10.2, §21 (Temari ↔ Producer), §25 Q9; TMR-P05 (exact sources), TMR-P04; RS-II §9.5. §10.2 says: "At least one later strategy involving 961/Gokugetsu stakes is arranged without Temari's advance consent."
- **A1:** adv_cidol-ttmr-3-002_02 L91, L98; 002_03 L22–L38; dear_025 L376–L428; dear_026 L23–L40; dear_023 L468–L514; dear_027 L186–L200; P1 ending-normal-04 L39–L48, ending-normal-05 L19–L53; pevent activity_010 L48–L82.
- **Change (STRENGTHEN):** replace "at least one" with the located pattern.
  - He overrides an explicit request by using footage she asked him to cut (3-002).
  - He reports a binding transfer stake after the fact. She protests '事後報告やめてください'; he answers that it is already promised (dear_025).
  - He signals a format change only in wording (dear_026; see SAA-007 for the たち cue).
  - He vetoes the farewell live, but gives reasons and gains her assent (dear_023).
  - P1 meals impose disliked foods as a substitute penalty.

  Her refusals typically run protest → ratification ('それだけ…信頼してる'). Add the counter-pattern: she readily accepts trainers' authority. Use this to give a provisional answer to §21's "How does Temari refuse him?".
- **Benefit:** a vague concession becomes a located pattern. **Deps:** ⚠ the RS-II §9 hotspot; SAA-045 (Misuzu co-arranged the 961 stake); SAA-007. **OA:** no.

**SAA-045 · CMP02-C007 · UNDERWEIGHTED · — · OA: no**

- **T/C:** TMR-B04, TMR-S02, TMR-P04; CORE-Temari §7.2, §10.5; RS-I §5.3; RS-II §9.2/§9.5; PSL TEM-L004. TMR-B04 says: "Misuzu and Producer compete through bodily care … may be comic surface over complementary roles".
- **A1:** adv_dear_ttmr_009 L324–L375; cidol-ttmr-3-016_01 L180–L208; dear_025 L326–L358; dear_033 L66–L76; dear_034 L280–L321 (L288); cidol 011_03 L85–L89.
- **Change (REVISE):** add the three-stage Misuzu ↔ Producer arc as Temari's route shows it.
  - (1) Handover: Misuzu calls SyngUp a cage that Temari broke and formally entrusts Temari to the Producer, who accepts "ruin together" (dear_009).
  - (2) Rivalry over care (3-016).
  - (3) Coordination: the joint 961 trip that set the stake; a vegetable report; trading anecdotes about Temari ("Win-Win"), which she protests; the Producer's growing identification with Misuzu's indulgence.

  Revise TMR-B04 to "compete, then pool knowledge". Use dear_009 as the textual locus of RS-II's "containment-transfer point", and cite Misuzu's cage metaphor as Misuzu-side support for TMR-S02.
- **Benefit:** a comic pairing becomes a dated arc. **Deps:** ⚠ RS-I §5.3 and the RS-II §9 hotspot; SAA-084 ("birdcage"). **OA:** no.

**SAA-046 · CMP02-C008 · UNDERWEIGHTED · — · OA: no**

- **T/C:** TMR-C04; CORE-Temari §5.2, §5.4, §17.4, H-TEMARI-03; AVA-Temari §10; THEME "present-tense self-love". §17.4 says: "Her strongest positive self-statements occur after major achievement".
- **A1:** adv_dear_ttmr_027 L382–L427; dear_034 L160–L191; dear_037 L452–L477; unit_01-04_20 L662–L678; P1 before-audition-mid-normal-01 L60–L86 (choice 2).
- **Change (REVISE):** keep "present-tense, not unconditional", and add:
  - (a) Her self-belief is mediated by others: "because someone believes in me, I can believe in myself" (Dear 027). Dear 037 rests on the Producer's "we're alike". She now accepts Misuzu's belief (Dear 034).
  - (b) In U1 the self-love line comes after full effort and before the verdict ('過去最高の私を出せた…こういう私が好き').
  - (c) A rank-independent anchor: she loves her own singing "even if called self-praise" (P1, choice 2).

  Remove "only after major achievement" from §17.4.
- **Benefit:** corrects an overstated conditionality. **Deps:** SAA-048. This also carries the HSCA-001 residual on the Temari side of U1 04_20 (see 6-B). Rediscovers HSCA-098. **OA:** no.

### 3-3. CORE-Kotone

**SAA-010 · CMP03-C003 · UNDERWEIGHTED · R03 S · OA: no**

- **T/C:** CORE-Kotone §3.2.10, §10.3–§10.5, §18.5; KOTO-C12, C13; the claim implications in the Kotone refresh; a cross-reference to RS-II §8. KOTO-C12 (very high) says "Kotone rejects successor hierarchy in favor of reciprocal rivalry"; the §10.3 heading says she "refuses inheritance".
- **A1:** adv_dear_fktn_017 L470–L477 (L474); dear_033 L239–L292 (L256); P3 final-failure-01 L60–L76 (L70); SL1.1 dear_037 L180–L222 (L197–L214).
- **Change (REVISE, narrowing §10.3; PRESERVE C12's core):**
  - She refuses *designated* succession, that is, being made the answer to Sena's problem. D033's 'その言葉' is an inference from D017, not a spoken word.
  - She embraces *earned* inheritance: she wants to inherit by winning (P3 L70) and, having won, takes up Sena's pride and duties (D037).
  - This matches RS-II §8.2/§8.5, "function transfer without identity replacement".
  - The C-MAO 007 parallel and the §18.5 link (D033 L266) are optional.
- **Benefit:** a heading that overstates the refusal is corrected. **Deps:** ⚠ KOTO-C13 is also edited by SAA-051 and SAA-052. Extends HSCA-116. **OA:** no.

**SAA-011 · CMP03-C008 · UNDERWEIGHTED · R03 S · OA: no**

- **T/C:** CORE-Kotone §3.1.1, §3.1.4, §11.6; KOTO-C10 (pressure column); a BRL P1 note. No through-line of a performance-conditioned fear of being given up on.
- **A1:** adv_dear_fktn_002 L54–L119 (L93); P1 mid-failure-01 L49–L80 (L62); final-failure-01 L70–L105 (L91); ending-normal-05 L24–L65 (L36 契約解除); after-step-2-normal-03 choice 3 (L133); before-audition-final-normal-01 choice 2 L80–L116; true end L54; cidol 3-013_02 L136–L216; unit_01-01_05 L425–L430.
- **Change (STRENGTHEN):**
  - Add a recurring, branch-scoped fear that poor results will make the Producer give up on her (見捨て/見限; 契約解除). It spans four continuity classes; present the P1 items as possibility space.
  - Keep it distinct from the father association, which §3.1.4 already handles as association, not causation.
  - R03: phrase before-final choice 2 as a release of tension that she jokingly protests, not as harm to her performance.
  - **Exclude the "P2 a-01" father link** until it is checked in A1.
- **Benefit:** a lexically stable pattern gets named. **Deps:** rediscovers HSCA-024. **OA:** no.

**SAA-052 · CMP03-C005 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Kotone §3.2.22, §11.4, §11.6, §23; EVM §3.3, KOTO-C13, C22; AVA-Kotone §6.1; Kotone refresh.
  - §3.2.22 asks whether the relation "eventually allows gifts that do not need repayment".
  - §11.6 asks whether she can "later refuse him without feeling morally bankrupt".
- **A1:** SL1.1 adv_dear_fktn_037 L265–L311, L380–L419 (L406, both branches), L597–L611, L655–L664; dear_031 L93–L173; dear_028 L441; dear_027 L413–L490; supports 3-0024, Rinami 0058, Saki 0000/0024.
- **Change (REVISE, narrowing the OPENs):**
  - (a) D037 closes the career-as-payment account inside the grammar of exchange: "have I repaid?" becomes "enough to need change". The Producer names what she gave him, so payment becomes mutual gift.
  - (b) She sets terms over him: she rescinds the no-partner demand and forbids a verbal reply in both branches.
  - (c) She reverses the provider role (L655).
  - (d) In D031 the Producer forbids answers calibrated to his face; support 3-0024 shows the same habit with Saki.
  - (e) The support ledgers already show debt-free care accepted.

  Keep the institutional asymmetry OPEN.
- **Benefit:** the core stops presenting answered questions as untested. **Deps:** ⚠ KOTO-C13 (SAA-010, 051); SAA-185 (D037 romance coding, Batch 4). AV-D optional (L506–L517). **OA:** no.

**SAA-053 · CMP03-C006 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Kotone §7.2–§7.3, §3.3.8; KOTO-C28; a cross-reference to RS-II §3.3. The §7 heading is "Talent: social intelligence before technical supremacy".
- **A1:** adv_cidol-fktn-3-011_02 L111–L166 (L116, L147, L166); dear_005 L163–L237 ('歌が下手です' in every branch, L173/L189); dear_007 L54–L95; 3-001_02 L113; P1 after-step-2-normal-01 L43; pgrowth_001_fktn_01/03; school_011 L40–L52; sales_4-005.
- **Change (REVISE):** specify the uneven profile.
  - Her persistent weakness is vocal: the running joke; '歌が下手です' in every branch; years of scolding; the Producer's estimate of 0.4 → 2 and its formal retraction.
  - Dance and visual are rated strengths: the Producer's 100/100; P1 "top of academy"; the dance trainer; the U1 dance duel; peer testimony.
  - Her own dance self-rating varies with condition, consistent with KOTO-C03.
  - Align with RS-II §3.3.
- **Benefit:** removes an inconsistency between the core and RS-II. **Deps:** CMP01/CMP02 (the RS-II §3.3 trio domain model). Rediscovers HSCA-027. **OA:** no.

**SAA-054 · CMP03-C007 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Kotone §13.5, §17.5, §11.3; KOTO-C22; JVR Kotone rows. §17.5 says "Money is both comic surface and real dream-content".
- **A1:** adv_cidol-fktn-3-001_01 L138–L165 (L147, L152, L154, L165); 3-011_02 L61; dear_022 L175–L180; dear_013 L381; dear_021 L211; P1 ending-true-01 L178–L208; support 3-0065; cidol hski 015_03; U1.
- **Change (STRENGTHEN):**
  - Add a third function of money talk: deflection when sincerity is noticed.
  - Add the cross-track pattern of rationed or displaced affection: respect, gratitude and love voiced to third parties or in her absence.
  - Mark SL1.1 D037 as the reversal: a direct confession, then sealed.
- **Benefit:** a register mechanism gets named. **Deps:** ⚠ KOTO-C22 (SAA-052). HSCA-175 (Kotone's inner/outer split in support 2-0001, Batch 6-A) is adjacent. **OA:** no.

### 3-4. CORE-Mao

**SAA-055 · CMP04-C003 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Mao §2.2 (wording), a new §2.3a, §13.3; CSL Phase 3 Mao (a new pre-Producer row); PSL MAO-L021.
  - §2.2: "She is no longer selected for the same work and eventually leaves the child-actor path".
  - §2.3–§2.4 move directly from defensive princehood to the Producer's intervention.
  - MAO-L021: "threatened abandonment".
- **A1:** adv_cidol-amao-3-007_01 L96–L157; cidol 015_03 L72–L81, L235; dear_001 L260 (inner); dear_002 L225–L230; dear_003 L92; dear_010 L39–L45; dear_011 L18–L30; dear_021 L108–L124 (inner; dance trainer); P1 final-failure L51–L60 (choice 1); ending-normal-04 L69–L83; event_021 L199; support 3-0044, 3-0051; E013.
- **Change (STRENGTHEN, plus REVISE of wording):** insert §2.3a, "Hatsuboshi years 1–2: substitute vocation and stalled ambition".
  - She was dismissed from the troupe (お払い箱); revise "left" accordingly.
  - She enrolled "clinging", with guilt toward serious aspirants, until she saw the seniors' Campus mode!!.
  - Her first-year aim was top star / Prima Stella (E013; support 3-0051).
  - She failed the previous N.I.A. (Dear 011 L18) and did not reach the second-year H.I.F. main stage (E021 L199). She never performed Campus mode in three years (support 3-0044).
  - "Three years smouldering" (Dear 010 L39); the self-label "落ちこぼれ" (015_03 L235).
  - Every scout refused her (Dear 002 L225–L230).
  - She nearly abandoned idolhood before the Producer (P1 choice 1; Dear 001 L260, inner).
  - Third-party testimony: the dance trainer (D021) and Sena (D024; SL1.1 D-SENA 031). Her SL1.1 D-TSUBAME 031 admission.

  Revise MAO-L021 to "retrospective pre-Producer near-abandonment". Link to cidol 015_03, where she reclaims these years.
- **Benefit:** fills a missing developmental state. **Deps:** SAA-056, 058. Rediscovers HSCA-007/009. **OA:** no.

**SAA-057 · CMP04-C006 · OMITTED · — · OA: no**

- **T/C:** CORE-Mao §12.4; JVR Phase 3 Mao; an AV-owner referral for `05_AUDIOVISUAL_ANALYSIS/04_ARIMURA_MAO/GKM_MAO_DIALOGUE_VOICE_ACTING_CLOSE_READING.md` §10.
  - §12.4: "The Osaka communication shows Mao playfully using Kansai speech … gives the polished prince a regional/childhood texture".
  - AVD §10 says the Dear spine could not supply this register.
- **A1:** adv_dear_amao_022 L339, L439, L453, L496; cidol 013_01 L11–L34; 013_02 L210; 015_03 L291; dear_032 L183, L302; dear_033 L281 (choice 3); event_003 main-02 L371–L377; event_022 main-03 L256–L273.
- **Change (REVISE):** Kansai is Mao's emotional home register.
  - Home is Hyogo (Dear 022 L339); Osaka is her 地元 (Dear 032 L183); a peer knows she is from Kansai (E003 L377).
  - It slips out under embarrassment ('そんなに泣いてへんし'; 'いけず').
  - It serves as tsukkomi (Dear 033 L281, choice 3).
  - It erupts under maximal distress, aimed at the Producer (Dear 022 L439–L496).
  - It marks childhood and family.

  Ask the AV owner to correct AVD §10. Keep native-versus-acquired OPEN.
- **Benefit:** corrects a documented misstatement in the AV documentation. **Deps:** land with SAA-001's §2.8 outburst text; SAA-193 (register map, Batch 4). AV-D optional. **OA:** no.

### 3-5. CORE-Lilja

**SAA-014 · CMP05-C001 · UNDERWEIGHTED (P1 → P2) · R05 Q · OA: yes**

- **T/C:** CORE-Lilja §12 (a new §12.3), §18 LILJA-V1-07, §20; EVM C25, C30; RSL Lilja ↔ Producer rows; JVR Lilja map ("romantic-professional ambiguity"); RS-II §9.2. §12.2: "The Producer knowingly deflects the romance-adjacent implication… and postpones a direct answer until she is no longer an idol". §12's conclusion: "…long-term emotional enclosure remains unresolved".
- **A1:** adv_dear_kllj_037 L121, L297–L305, L314–L354, L368–L375, L380–L406; cidol C001_02 L21; C001_03 L111–L117, L185–L205, L216–L222; C005_01 L25–L60 (L32); C005_02 L279–L293; C012_03 L297–L339 (L339); dear_022 L342, L392; dear_023 L172, L197–L216; dear_026 L249–L253; activity_022; C022.
- **Change (STRENGTHEN + REVISE, narrowed by R05; the romance label stays OPEN):** add a bounded §12.3.
  - Lilja's own idol-time barrier ('アイドルなので', C005_01 L32; 'アイドルなので、今はまだ', C012_03 L339) is mirrored from the Producer's side at D037 L374–L375.
  - Her private signals; the jealousy ambiguity, which runs both ways (D022 L392 vs D026 L253); '責任を取ってください' (D037).
  - The Producer's signals: his Tanabata wish, the D027 blush, the self-declared fan (C022).

  R05 removals and relabels:
  - Drop "secret visit to Sweden" and "family slot at Christmas"; these are professional or family-surrogate care (C005_01 L127; C005_02 L124).
  - Replace "mutually acknowledged" with "bilaterally signalled, explicitly deferred".
  - Label C001/C005/C012/C022 as C4 (C012 is a dream) and activity_022 as C3, not as a linear precursor arc.

  The branch-label component is in Batch 0 (SAA-204). Mirror in V1-07, C25/C30, RSL, JVR and RS-II §9.2, where Lilja is absent.
- **Benefit:** a Lilja-specific mechanism that no home records. **Deps:** SAA-059 (C25), SAA-200 (C022); CMP09/CMP17 on REVERSI symmetry; ⚠ the RS-II §9 hotspot; the romance-coding policy (SAA-068). AV partial. Rediscovers HSCA-080. **OA: yes.**

**SAA-059 · CMP05-C004 · UNDERWEIGHTED (REVISE OPEN → bounded) · — · OA: no**

- **T/C:** CORE-Lilja §12.2, §22; AVA-Lilja §5; C25. §22 asks: "Can Lilja disagree with or refuse her Producer without experiencing it as betrayal?"
- **A1:** cidol-kllj-3-008_01 L29–L38; dear_013 L162; dear_014 L11–L59; P1 after-step-1-normal-01 L132–L146; after-step-2-normal-03 L96–L122; sales_4-001-01 L34–L43 (choice 2); after-audition-mid-normal-02 L72–L84; activity_009 L80–L88 (choice 3); dear_023 L197–L293; dear_037 L368.
- **Change (REVISE):** record a graded repertoire already present in SL1.0, labelling the branch items.
  - Covert or bodily refusal: training against instruction (D014); refusing to explain (D013); '善処します'; 'ひとりじゃなければ'.
  - Challenge to his method: she asks to be scolded (C008_01).
  - Rejection of unfounded reassurance (sales choice 2).
  - Claim-making: praise demands (D023); accusing him of evasion (D037).

  Keep OPEN only sustained disagreement over a production decision, and separation.
- **Benefit:** narrows an over-broad OPEN. **Deps:** ⚠ C25 (SAA-014). Rediscovers HSCA-081. **OA:** no.

**SAA-060 · CMP05-C005 · OMITTED (STRENGTHEN, branch-labelled) · — · OA: no**

- **T/C:** CORE-Lilja §14, §20; BRL P1[LILJA]. §20 lists her fears without the fear of losing the Producer's production.
- **A1:** P1 ending-normal-05 L37–L85 (branch 2 L40–L55; shared tail L56+); after-audition-mid-failure-01 L24–L60 (choice 1, L49); after-audition-final-failure-01 L96–L121 (choice 3, L114); ending-normal-04 L41–L52 (choice 1); before-audition-final-normal-01 L96–L114 (choice 3); ending-normal-01 ('いつも').
- **Change (STRENGTHEN):**
  - In several P1 failure branches Lilja fears the Producer will stop producing her. The shared tail of ending-normal-05 treats this as invariant and answers with a formal renewed request.
  - She wishes a failing performance would end, and admits performed confidence.
  - Note that shared tails sometimes treat branch-only states as habitual.
- **Benefit:** fills a fear list. **Deps:** HSCA-081. **OA:** no.

### 3-6. CORE-China

**SAA-015 · CMP06-C001 · UNDERWEIGHTED · R06 Q · OA: no**

- **T/C:** CORE-China s18, s24.4; CHINA-C29; AVA-China "Claims not closed" and Producer row. The core asks, as an untested Phase-7 question, "Can she reject his strategic interpretation…?"
- **A1:** adv_dear_kcna_033 L344, L348, L353, L357, L358, L366; dear_029 L456; dear_012 L75, L76, L84, L86, L94.
- **Change (REVISE, narrowing the OPEN, as qualified by R06):**
  - Record Dear 033 L344–L366 as a bounded instance: China declines the Producer's correct strategy and apologises (L344, a perceived breach), and he accepts.
  - Add D029 L456 ("accept anything") as the before-state.
  - File Dear 012 L75–L94 with s18's dependency evidence, **not** as counterpressure. There he disclaims being indispensable (L76), and China re-centres him (L86).
  - Record that his assent is scripted (a one-option choice) and immediate, so this is refusal without relational cost.
  - The narrowed open item is refusal under risk, or sustained disagreement and separation.
- **Benefit:** the core's own test question gets its answer text. **Deps:** ⚠ s18 is also edited by SAA-065 and SAA-016. **OA:** no.

**SAA-016 · CMP06-C005 · UNDERWEIGHTED (transition OPEN) · R06 Q · OA: yes**

- **T/C:** CORE-China s18, s19; RSL China ↔ Producer and China ↔ Kanae; SIDE s2.3. Household gatekeeping of the Producer and China's proprietary wishes are recorded in pieces but never connected, and the core says nothing about romance coding.
- **A1:** adv_cidol-kcna-3-005_01 L106, L114; 005_03 L80–L183; 014_03 L54–L85; 016_01 L171, L190, L198; adv_dear_kcna_024 L118, L123, L136–L151; school_006 L72; activity_022 L52; dear_037 L371.
- **Change (OPEN note, as qualified by R06).** Record these markers without asserting romance:
  - The household polices the boundary: silent chaperoning (C005_03); Kanae's vetting and Han Xin warning (D024); the Kanae–Producer rivalry (C016_01); the Producer's parenthetical thought that Hiwatari would forbid things (activity_022 L52, C3 choice 1 only).
  - China's long-horizon wishes: the deferred plan to give the Producer a room in the house; the two-person onsen proposal; peers calling her talk のろけ.
  - Producer-side markers: 016_01 L190 (he competes with Kanae as a jealous judge) and D037 L371 (affection of unspecified kind).

  R06 also asks to drop D001 L25, which is etiquette, not a warning, and to mark school_006 L72 as C3 choice 1. Note that SL1.2 resolves the Kanae–Producer rivalry into partnership (hkne D010).
- **Benefit:** connects a pattern the core records only in pieces. **Deps:** SAA-103 (CMP14), CMP18; ⚠ s18; the romance-coding policy (SAA-068). Rediscovers HSCA-075. **OA: yes.**

**SAA-061 · CMP06-C002 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-China s2, s19, s25; CHINA-C01, C13; CSL C-CHINA family-roots row. s2 says she "has grown up materially secure, loved, served, and protected", which "must not be read literally as deprivation".
- **A1:** adv_cidol-kcna-3-009_02 L43–L204; support 0075_02 L60–L74; SL1.1 3-0122_01 L77–L182; SL1.2 hkne D008 L54, L59.
- **Change (REVISE; PRESERVE C01):** qualify s2/s25 with a clause on her emotional history.
  - In early childhood her parents and relatives were mostly away on Kuramoto Group duty, and she cried from loneliness. She framed that need as わがまま.
  - The family's present lavish attention began with the apprentice's petition and the grandfather's change of heart.
  - Do not claim blanket emotional deprivation.

  Integrate AVB-China s6.3/s13.3 and execute R86's routing of 3-0122 into s19. Link to C13 (愛された責任).
- **Benefit:** an executed routing and a more accurate childhood. **Deps:** SAA-212, SAA-098; part of SAA-108(a). Rediscovers HSCA-073. **OA:** no.

**SAA-063 · CMP06-C004 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-China s19; AVA-China "Claims not closed"; AVB-China s18 Q3; RSL China ↔ grandfather. The AVA open item asks "whether family love can be resisted when the family interest conflicts with public duty".
- **A1:** adv_dear_kcna_009 L151, L155, L157, L163, L168, L173; dear_010-01 L12, L14.
- **Change (REVISE):**
  - D-CHINA records China's first open defiance of her grandfather (D009).
  - By D010-01 L14 he has stopped his unreasonable requests after being scolded by her.
  - In D011 she refuses commanded votes.
  - Narrow the AV open items: resistance to family will is attested; resistance in a sustained conflict with public duty remains open.
- **Benefit:** two open items are narrowed by in-track text. **Deps:** HSCA-073/076. **OA:** no.

**SAA-064 · CMP06-C006 · OMITTED · — · OA: no**

- **T/C:** CORE-China s2 or s20; CSL China ordinary-life rows. s0 assigns Produce Events the role of "ordinary life", but s2/s20 use them mainly for work.
- **A1:** activity_005 L13, L16, L76, L80; activity_014 L20, L62; activity_003 L53; activity_009 L14, L56; activity_017-02 L92; activity_016 L60; P1 after-step-1-normal-03 L56, L89; sales_3-006-01 L41, L56.
- **Change (STRENGTHEN):** add a short ordinary-life paragraph that instantiates the self-authorship deficit. The items, recovered from `CMP06\candidates.jsonl`:
  - living with maids in a nearby villa; the dorm wish, including her resolve to petition her grandfather herself;
  - clothes chosen by her maid, and her secret wish to choose them;
  - nutrition-managed meals and a chauffeured commute;
  - overnight freedom contingent on household supervision;
  - preferences: rain by the window with milk tea; milkshake over coffee; the hamburger as a rare treat; hot springs; hamsters; an aversion to shooting, even in games;
  - habits: promise-keeping; last-minute work; felt-dog and painting hobbies.

  Cross-reference the support rows that already record dorm longing.
- **Benefit:** s0's stated role for Produce Events is fulfilled. **Deps:** none. Counterevidence: CSL rows 513/535 carry some of this. **OA:** no.

### 3-7. CORE-Hiro

**SAA-066 · CMP07-C004 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Hiro §10, §17, §20; HIRO-C23, C27; THEME (hobby/dream; purity/impurity). §20 says that by the end the route allows Hiro "to say the dream as hers"; §17 reads "impure" as a list of plural motives.
- **A1:** adv_dear_shro_021 L211–L246; dear_029 L358–L392 (L377); cidol-shro-3-018_03 L143–L160 (L149); dear_036 L369–L448.
- **Change (PRESERVE HIRO-C27 as the first clean declaration; STRENGTHEN):**
  - Hiro holds 'この新しい夢' from Dear 021 but treats it as unsayable for an idol until she becomes No. 1. This is a self-imposed legitimacy test (資格, Dear 029 L377), linked to her envy of real idols' dreams (CIDOL 018_03 L149).
  - Anchor 不純 in Hiro's own definition: Ume has become a true idol, while Hiro did not believe she could win and "just reached out".
  - The Dear 037 declaration ('今度こそ、ちゃんと言えた') is then the gaining of permission to speak.
- **Benefit:** grounds a key term in the character's own definition. **Deps:** ⚠ §17 (SAA-002) and §10 (SAA-125). Rediscovers HSCA-088. **OA:** no.

**SAA-067 · CMP07-C005 · OMITTED · — · OA: no**

- **T/C:** CORE-Hiro §12, §21; HIRO-C19 and the EVM list "AV-dependent claims intentionally withheld"; THEME (body). The EVM withholds "whether camera/choreography aestheticizes bodily fragility" as AV-dependent.
- **A1:** adv_cidol-shro-3-012_03 L186–L315.
- **Change (STRENGTHEN HIRO-C19's OPEN with textual evidence; REVISE the attribution of the aestheticisation risk, which is not Sena's alone):**
  - The text already shows the Producer designing public promotion around a "fragile girl leaping into fire of her own accord", with fans meant to share his own stomach-ache "hell".
  - Spectators' anxiety about her danger is an explicit product strategy, not only an AV question.
  - Hiro reports it with excitement ('熱い気持ちで、いっぱい').
- **Benefit:** moves a question from AV-withheld to textual. **Deps:** ⚠ HIRO-C19 (SAA-017) and the §21 hotspot (SAA-017, 068, 070). AV may show how it is realised. **OA:** no.

**SAA-068 · CMP07-C006 · UNDERWEIGHTED · — · OA: yes**

- **T/C:** CORE-Hiro §21, §27.6; RSL Hiro ↔ Producer rows. §21 records intimacy built through harshness and teasing, with no romance coding, withheld-feeling layer or precarity. The RSL AV addendum lists the "romance/profession boundary" as open.
- **A1:** adv_cidol-shro-3-018_01 L115–L122, L320–L332; 018_02 L135–L148; dear_010 L211–L263 (L234); dear_020 L303–L314; P1 ending-true-01 L154–L168; dear_003 L177; dear_006 L31; P1 ending-normal-04.
- **Change (STRENGTHEN the register and layering; OPEN the romance/profession boundary):**
  - (a) A pervasive romance-coded teasing register, always deflected by the Producer, with one reversal (CIDOL 018_02).
  - (b) An inner layer: "my feelings", untold even to him, and a private "forever together" (CIDOL 018_01). The deferred それ (Dear 020 branch 1) resolves as the dream in Dear 037 but leaves the inner feeling unstated.
  - (c) The trial-contract fiction as manufactured precarity that she both enjoyed and feared.

  Pair each with counterevidence, and do not convert any of it into a romance claim.
- **Benefit:** a register the core omits. **Deps:** **the corpus policy on romance-coded material** (cf. the Saki core; GKM_LEGACY_ANALYSIS_INVENTORY's "romance-coded inference" item). One owner ruling should govern SAA-003, 014, 016, 068, 082, 094, 185, 194, 231 and 254. ⚠ The §21 hotspot. AV-D for tone. **OA: yes.**

**SAA-069 · CMP07-C007 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Hiro §2, §7, §23, §27.1; HIRO-C09; JVR Hiro baseline. §27.1 asks whether Hiro "must continually escalate danger to preserve interest". §23 lists ふふ but not the sigh of deflation.
- **A1:** adv_dear_shro_007 L85–L190 (L155–L185); dear_009 L185–L207 (L197); dear_017 L401–L436; P1 after-audition-mid-normal-01 L15–L27; dear_018; P2 joke.
- **Change (STRENGTHEN the mechanism; REVISE by narrowing §27.1):**
  - Name the success-deflation sigh as a mechanism, together with the Producer's resulting "nightmare" (Dear 007).
  - Record the text's own answer: idol work never stabilises (Dear 007), and "as long as you are an idol it will always be a pinch" (Dear 009 L197).
  - Her friends read the sigh as fulfilment (Dear 017), and she later controls it strategically (Dear 018).
  - §27.1 should note that the text offers intrinsic instability as an alternative to manufactured crisis (cf. SAA-017).
- **Benefit:** answers an open question from the text. **Deps:** rediscovers HSCA-164. **OA:** no.

**SAA-070 · CMP07-C008 · OMITTED · — · OA: no**

- **T/C:** CORE-Hiro §5, §7, §20, §21; HIRO-C05, C08; BRL P1[HIRO]. HIRO-C05 makes Dear 008 the hinge. §21 speaks of "a promise to remain together through the top-idol pursuit".
- **A1:** P1 after-audition-mid-failure-01 L39–L71; final-failure-01 L55–L73, L135–L149; ending-true-01 L127–L168.
- **Change (STRENGTHEN HIRO-C05 with track variants; REVISE by scoping §21's endpoint to D-HIRO):**
  - P1 has its own branch-conditional frustration hinge: at mid-failure she cannot understand 悔しさ; at final failure she has her first tears and says '負けてばかりじゃ、いられない'.
  - At the P1 true ending the Producer says she will never be a top idol and that the days with her outweigh his dream, and Hiro answers 'ずっと、一緒にいようね'. This is the inverse of D-HIRO's shared-dream fulfilment.
- **Benefit:** prevents a D-track endpoint from being stated as general. **Deps:** ⚠ the §21 hotspot. **OA:** no.

### 3-8. CORE-Rinami

**SAA-020 · CMP08-C009 · OMITTED · R06 S · OA: no**

- **T/C:** CORE-Rinami §9, §10; RINAMI-C14/C16; SIDE §4.1 ("Against Rinami") and §4.3. §9 treats Shion only as archive or provenance pressure.
- **A1:** adv_dear_hrnm_014 L101–L162 (L111, L138, L141, L162); dear_015 L162–L262 (L171, L251, L257); dear_016 L54–L190 (L99–L152, L182); dear_018 L97–L283; dear_031 L44–L259 (L142–L224, L209); dear_033 L42–L225; P2 after-audition-b-normal-02 L84–L104.
- **Change (STRENGTHEN):**
  - (a) N.I.A. stages counter-models of sisterhood, against which Rinami's relational, age-independent sisterhood is defined (Dear 014 L162):
    - Shion's "sister as oppressor". Her attack on the "deceitful onee-san idol" (L138) is motivated in the text by her sister wound (L101–L122).
    - Gekka's "愚妹" (018 L97–L177; 031 L142–L224). Add this to SIDE §4.3.
    - Nadeshiko's exclusive "四音お姉さま" (P2, labelled as a C3 outcome file).
    - The real older sisters at H.O.F.
    - Rinami applies her ethic to Gekka herself (031 L209).
  - (b) Shion's fake scandal makes the in-world stigma of a producer–idol romance explicit, which bears on §6 governance. Per R06 this is UNDERWEIGHTED: recorded but not interpreted.
  - (c) Her first will to win comes as protective anger on the Producer's behalf (015 L257–L262). Scope "first" to the Dear chain, where 015 L251 is the first explicit '絶対勝つよ'. His sibling-idiom anger mirrors it (016 L182). Note his bluff or threat (016 L99–L152) as an ethically relevant protective act for §6.
- **Benefit:** a missing frame for the core's onee-san question. **Deps:** SAA-003; ⚠ SIDE §4.3 is also extended by SAA-096. Rediscovers HSCA-042. **OA:** no.

**SAA-071 · CMP08-C002 · OMITTED · — · OA: no**

- **T/C:** CORE-Rinami §8, §11, §24, §29 locator table; RINAMI-C18 evidence; THEME (a new promise/一番星 row); JVR Rinami baseline (a ruby row). §8 says she "wants Prima Stella. She wants the summit with the others."
- **A1:** adv_dear_hrnm_010 L421, L441, L449; dear_017 L138, L154, L158, L166, L175; dear_023 L74, L79, L517; dear_025 L499, L507; dear_027 L179, L402, L764; dear_028 L166; dear_035 L393, L447, L491; dear_036 L357, L518; dear_037 L226, L396; P3 final-normal-02 L11, L17.
- **Change (STRENGTHEN):** add the promise arc in sequence.
  - Dear 010: her confession is conditional on becoming Prima Stella.
  - Dear 017: a reciprocal promise.
  - Dear 023: 'きみとの約束……守れなかった', which also voids the condition on the confession.
  - Dear 025: a parallel broken promise to her father.
  - Dear 027: his notebook reverses the promise, and she makes her own 一番星《いちばんぼし》宣言.
  - Dear 028: renewal. Dear 035: '一緒に見よう'. Dear 036: her inner 'これが一番星の景色'. Dear 037: the promise is linked to the confession.

  Record the ruby's double reading (the title プリマステラ vs the view いちばんぼし) as the lexical carrier of the career/relationship fusion. Strengthen C18: the crisis of dream ownership is partly a crisis of debt.
- **Benefit:** the idiom that SAA-003 relies on gets its own record. **Deps:** SAA-003; ⚠ §11 (SAA-129) and §24 (SAA-224). AV: stills at dear_010 L434–L435 and dear_037 L441–L442. **OA:** no.

**SAA-072 · CMP08-C005 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Rinami, a new subsection after §8; CSL Phase-3 Rinami rows (add P1/P2); BRL Rinami P1/P2. The body uses Produce material only for opponents' fans and produced naturalness.
- **A1:** P1 after-audition-final-failure-01 L51, L68, L95, L111, L117, L139; final-normal-03 L59, L89; ending-normal-05 L17, L35, L64; before-audition-mid-normal-01 L117; P2 after-audition-b-normal-03 L68; P2 final-failure-01 L67; P3.
- **Change (STRENGTHEN):** add a P-track section in three steps.
  - series_001: failure branches open with self-removal ('ほかの子をプロデュースしたほうが') or 私なんか. Recommitment is invariant and always triggered by the Producer's words. Failure is measured against "みんなのお姉さん".
  - series_002: her resolve is partly self-sourced (悔しい), while inner speech still confirms borrowed belief.
  - series_003: a dream she has owned since first year, and a claimed title.

  Model the P-track as borrowed belief → self-felt frustration → owned ambition: parallel to D-RINAMI, not identical with it.
- **Benefit:** the P-track gets analysed. **Deps:** SAA-073. **OA:** no.

**SAA-073 · CMP08-C006 · OMITTED · — · OA: no**

- **T/C:** CORE-Rinami §3, §14; SONG Rinami R2; RINAMI-C21. §3 places her origin in Dear 026/027. No home records singing as her self-assessed weakness, or the first-fan motif.
- **A1:** P1 ending-true-01 L94, L98–L132, L138, L150, L156; after-step-2-normal-01 L47, L57; ending-normal-02 L36; P3 final-failure-01 L66; dear_006 L320–L335; dear_034 L5–L125; event_002 sales_4-003-01 L57; SL1.1 event_028 main-05 L5–L26, L66–L83; support 0045_02 L52.
- **Change (STRENGTHEN):**
  - Singing is both her root (the crying boy; the TV 歌のお姉さん; "best in class at music", SL1.1 E028) and a self-assessed weak skill ('歌は、ちょっと苦手'; 'へたっぴな歌').
  - The first-fan motif recurs: Dear 006; the Dear 034 dream; 'ファン1号さん' at the P1 true ending; the handshake '最初のお客さん'.
  - In P3 final-failure the Producer names her song as one that makes everyone smile.
- **Benefit:** sharpens C21. **Deps:** SAA-072; SAA-003 cites 'ファン1号さん'. AV: whether her singing reads as weak is a performance question; the self-assessment is textual. Extends HSCA-041. **OA:** no.

**SAA-074 · CMP08-C007 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Rinami §2, §11; RINAMI-C01/C07; SIDE §7.2 (a cross-link). §10's mention of Gekka is the sole reference to "support role".
- **A1:** adv_cidol-hrnm-3-017_02 L114–L209; 013_03 L54–L74; dear_022 L40–L109; event_013 main-03 L135–L161, L498–L503; support 0005_03 L104–L113; SL1.1 event_028 main-02 L235–L250; support 0106_03 L103–L159.
- **Change (STRENGTHEN):**
  - Rinami's actual pre-route exit path was becoming a supporter, not leaving school. Council work, into which Sena recruited her, was '楽しくて、充実してて', and Kana took exactly that path.
  - Her survivor's doubt ('一番の落ちこぼれだった、私だけが') feeds the summer crisis.
  - Keep the two-sided valuation of support: a positive vocation, and a temptation to self-erasure.
  - Link C07/C08 and OQ-RINAMI-06.
- **Benefit:** a concrete before-state. **Deps:** SAA-075. Rediscovers HSCA-034. **OA:** no.

### 3-9. CORE-Sumika

**SAA-021 · CMP09-C001 · UNDERWEIGHTED · R04 Q · OA: no**

- **T/C:** CORE-Sumika §7; SUMIKA-C22; RSL Phase 3 Sumika deltas. The canon has only "persistent witness" and "stayed beside her".
- **A1:** adv_dear_ssmk_001 L307; dear_002 L52–L58; dear_004 L41–L62, L282–L322 (L288–L297); dear_010 L257–L290 (L261–L273); cidol-ssmk-3-010_02 L102–L116 (inner L114); P1 opening-normal-01 L32–L42; mid- and final-failure choices 2–3; ending-normal-04 L36–L49; ending-normal-05 L26–L31; E001 activity_020 L19–L25.
- **Change (STRENGTHEN, with R04's scope):**
  - Non-abandonment is the founding term of the production relationship: an exit-offer test, then a contract sealed on the condition that he never abandons her midway, renewed in Dear 010 and named as permanence in her inner speech.
  - Scope: "recurrent across separate P1 result states (opening-normal-01 only among the openings; mid-failure choices 2–3; final-failure choices 2–3; ending-normal-04/-05 before the branch); C4 in E001".
  - **Drop** the claim that the canon makes dependence late-only, since C22 already cites Dear 007–010.
  - Add the RSL row "Sumika ↔ Producer | founding | exit-offer test → non-abandonment bargain".
  - Keep the expectation thesis primary, with permanence as a second axis.
- **Benefit:** names the founding bargain. **Deps:** SAA-134. Rediscovers HSCA-093. **OA:** no.

**SAA-077 · CMP09-C002 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Sumika §6, §13, §22.4; SUMIKA-C09, C22, C23; INST SYS-SUMIKA-04; RSL Sumika ↔ Producer. §22.4 says "Producer authority works partly through controlled distance" (citing CIDOL 012 only). §6 says "The Producer's contribution is not an anti-avoidance command".
- **A1:** adv_dear_ssmk_009 L25–L41; dear_024 L71–L104 (L104); dear_026 L121–L126; dear_027 L37–L141; dear_031 L510–L533; P1 after-audition-mid-normal-03 L24–L35; opening-normal-03 L15; after-step-2-normal-03 L138–L148; ending-true-01 L177; cidol 017_03 L32–L170.
- **Change (STRENGTHEN):** beyond controlled distance, the Producer stage-manages her crises.
  - He withholds the first live (Dear 009).
  - He re-arms the expectation trap ('期待に応えてあげましょう', Dear 024 L104).
  - He concedes that the sudden live was scheduled to make her face her fear (Dear 026).
  - He foresees her H.I.F. wish and pre-arranges Lilja (Dear 027), which recontextualises Dear 023.
  - In P1 he admits that the promise is a lever.

  Qualify C23: the wish is hers, but formed inside conditions he designed. Narrow §6: he never forces the feared act, but he enforces routine. "Did not tell me not to run" is Sumika's view at the true ending. REVERSI / 表裏一体 is his coinage in both tracks.
- **Benefit:** strengthens an under-evidenced governance claim. **Deps:** ⚠ C22 (SAA-021) and §6 (SAA-134). **OA:** no.

**SAA-078 · CMP09-C003 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Sumika §3, §12; SUMIKA-C04, C05, C19; E013–020 §9; RS-I §4.13; THEME. §3 says her brightness "is authentic, but she learns to deploy casualness strategically".
- **A1:** adv_dear_ssmk_025 L67–L93, L392–L432; event_020 main-03 L186–L211; dear_024 L200–L222; dear_032 L334–L356.
- **Change (REVISE to a three-function, historically formed account):**
  1. History: the gyaru style was adopted after the ballet loss, in rebellion against a nagging mother, and became natural (E020). The prodigy-era Sumika is remembered as serious, tense and unapproachable (Dear 024), and lonely in Sweden (Dear 032). "Authentic" therefore should not imply "original".
  2. Function: the Producer's diagnosis '良い子すぎる … ギャルだからこそ … ずっと、そういうふうに生きてきた' (Dear 025 L67–L93), and Temari's independent observation (L392–L432), show her sociability also working as habitual attunement to others that feeds over-fitting to expectations.

  Link this to the friction-reduction-as-care rows as their cost side.
- **Benefit:** the persona gets a history. **Deps:** SAA-022 (the same E020 line); SAA-132. **OA:** no.

### 3-10. CORE-Ume and RS-I §3.7

**SAA-023 · CMP10-C006 · OMITTED · R05 S · OA: no**

- **T/C:** RS-I §3.7; CORE-Ume §6.2. Neither models how Ume receives Saki's comfort.
- **A1:** P1 after-audition-final-failure-01 choice 3 L106–L183 (L125–L163); final-normal-04 choice 3 L68–L94; mid-normal-01 choice 1 L35–L62; adv_dear_hume_012 L237; mid-failure-01 choice 3 L122; ending-true-01 choice 2 L70–L73.
- **Change (STRENGTHEN):** add a "receiving care" sub-point.
  - Ume experiences Saki's post-loss comfort and early praise as another defeat, and accepts them instrumentally ('勝利への一番の近道').
  - Saki's full celebration of her own wins frees Ume to grieve.
  - R05 notes: cite mid-failure-01 L122 as a general rule from the Producer, not as Saki's care. Pair with ending-true-01 choice 2 and core §6.3. Keep the "no resentment" boundary.
- **Benefit:** RS-I §3.7 gets its receiving side. **Deps:** ⚠ RS-I §3.7 (SAA-178); SAA-036. Rediscovers HSCA-062. **OA:** no.

**SAA-024 · CMP10-C007 · UNDERWEIGHTED · R05 S · OA: yes**

- **T/C:** CORE-Ume §10, §22.2, §26 OPEN-UME-05; UME-C35; RS-II §9.5. §10: "Dear 023's counterfactual anxiety makes this especially visible". UME-C35 says the route "provides less evidence for durable disagreement".
- **A1:** adv_dear_hume_023 L87–L94, L123–L217 (L186–L217); dear_022 L56, L142–L187; dear_021 L478–L513; dear_037 L208–L271; dear_014 L201–L211; dear_030 L478–L508; cidol 006_02 L39–L46; 018_01 L64; P1 mid-normal-01 choice 2 L75–L90; ending-normal-04 L66–L109; P2 final-normal-01 L70; P3 selection-failure-01 L44–L66.
- **Change (REVISE, narrowing §10's use of Dear 023; keep OPEN-UME-05 open):**
  - Dear 023 resolves with the Producer refusing any counterfactual that loses "this Ume", and with Ume declining to learn it.
  - Add the reverse direction of influence: Ume makes him combative; teaches him to laugh at defeat; corrects his priorities; he adopts her intuition; friends observe the convergence.
  - R05: enter the convergence items in **both** columns of UME-C35, because they evidence two-way influence and are also compatible with the merger risk.
- **Benefit:** a bidirectional relation. **Deps:** ⚠ the RS-II §9 hotspot; SAA-080. CMP10 records this as contradicting HSCA-063 (not rediscovered), so read HSCA-063 alongside. **OA: yes.**

**SAA-079 · CMP10-C001 · OMITTED · — · OA: no**

- **T/C:** CORE-Ume, a new §6.5; §24 P3-C; §26 OPEN-UME-01/02; a new UME row. The core never mentions the 負けた ban, 敗北のプロフェッショナル, the D-UME summer H.I.F. loss or the P3-C "refreshing defeat".
- **A1:** adv_dear_hume_005 L54–L110; P1 ending-normal-05 L40–L54 (choice 2); dear_022 L297–L309; dear_028 L96–L105; P3 final-failure-01 L18–L61; cidol 006_02; dear_036.
- **Change (STRENGTHEN):** add §6.5, "Loss habituation and the language of defeat".
  - (a) The Producer diagnoses her habituation to losing and bans 負けた, which she obeys comically; she reclaims 敗北のプロフェッショナル (CIDOL 006_02).
  - (b) In D-UME she openly admits her first loss after beating Saki (Dear 022 L297), while Saki reframes it as a draw (cite RS-I §3.9.1). The refrain returns (Dear 028 L105). The Prima Stella speech retires the defensiveness (Dear 036).
  - (c) In the P3-C fragment she breaks the promise and fears a peaceful defeat. Route this to OPEN-UME-01/02.
- **Benefit:** fills a gap in the Ume home. **Deps:** RS-I §3.9.1 already holds the Dear 022 result. This carries the open Ume-side residual of HSCA-059 (see 6-C). AV-D for tone. **OA:** no.

**SAA-080 · CMP10-C002 · OMITTED · — · OA: no**

- **T/C:** CORE-Ume §10, §21, §22.2; a new UME row; RSL Ume ↔ Producer origin. No home mentions intuition, or that Ume chose the Producer.
- **A1:** adv_dear_hume_001 L191–L228; dear_010 L95–L101; dear_018 L23; dear_025 L300; dear_031 L322–L336; dear_030 L507–L508; dear_035; P1 ending-normal-03 L95–L97; ending-true-01 L125–L143; school_003 L50–L63; U1 01-01_01.
- **Change (STRENGTHEN):**
  - Ume initiates the partnership by intuition, and treats intuition as decisive at hinges ("by my own will and intuition").
  - The Producer comes to adopt it ('勘です', Dear 030), a sign of convergence.
  - Her agency works as quick intuitive commitment followed by reasoned elaboration (Dear 035).
- **Benefit:** a decision style. **Deps:** CMP17 (U1); SAA-024; SAA-091. **OA:** no.

**SAA-081 · CMP10-C003 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Ume §18, §20; UME-C29, C34. §18 says the wish to be seen as cute "reveals a gap in the Producer's gaze". UME-C29 cites CIDOL 012 only.
- **A1:** adv_cidol-hume-3-012_03 L413–L443; dear_010-01 L87–L101; dear_010 L292–L315; dear_021 L472–L543; dear_035 L82–L103; P1 final-normal-03 choice 2 L70–L109; step-1-normal-01 L17–L26; dear_034 L116–L169; dear_037 L324–L402; 016_01.
- **Change:**
  - STRENGTHEN UME-C29 with the recurrence (Dear 010-01, 021, 035, 037) and its P1 starting point.
  - REVISE §18's "gap". The Producer's founding goal already includes 最高の美貌 (Dear 010); he answers 同感です and calls her 面白かわいい. The gap is one of register and timing, and of Ume's difficulty receiving praise, not of what he sees.
  - Note Dear 034 (the trainers: "an idol, not a fighter") and Dear 037 (世界最強 chosen as a substitute for an earned title).
- **Benefit:** corrects a misplaced deficiency. **Deps:** consistent with the AV addendum's "integrated" finding. **OA:** no.

**SAA-082 · CMP10-C004 · UNDERWEIGHTED · — · OA: yes**

- **T/C:** CORE-Ume §5, §22.2; RS-I §3.8 and §1.3; a new UME row (coding only). Ume §5 lists "open jealousy" once; RS-I §3.8 models only Saki's jealousy.
- **A1:** adv_cidol-hume-3-009_03 L75–L99; 009_02 L469–L519; 012_02 L34–L86, L272; dear_010-01 L45–L76; activity_021 choice 3 L81–L93; activity_018-02 condition 1 L66–L69; dear_002 L167; dear_017 L114–L142; dear_027 L73–L83; 018_03 L84–L93; P1 ending-true-01 L148–L158; P3 selection-normal-02 L11–L22.
- **Change (STRENGTHEN):**
  - Ume has a recurring, mostly comic exclusivity reflex: "my Producer"; "my sister only"; the hypothetical hated rival "a girl like me". It coexists with her plural social world.
  - Record the attraction-coded cluster as coding only and OPEN, under RS-I §1.3 and OPEN-RS1-09.
  - Counterweights: series_003 folds 大好き into fan address, and Ume habitually reads romance into other people's bonds.
- **Benefit:** fills a gap in RS-I's jealousy model. **Deps:** the romance-coding policy (SAA-068). HSCA-139 (Batch 6-A) is adjacent. AV-D. **OA: yes.**

**SAA-083 · CMP10-C005 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Ume §7, §11; UME-C06, extended or as a new row. §7 models only equality fear and the weight of the dream. §11 gives the father's answer but not the question that prompted it.
- **A1:** adv_dear_hume_003 L194–L228; dear_008 L256–L287; dear_012 L245–L254; dear_026 L714–L760 (L722–L729); cidol 006_01 L38–L44; P1 mid-normal-03 choice 3 L129–L133; P2 final-failure-01 L46.
- **Change (STRENGTHEN):** add a relational fear series. Ume fears:
  - being the lesser substitute for Saki (Dear 003);
  - having disappointed Saki by never being a real competitor (Dear 008), a fear Saki rejects without Ume hearing it (Dear 012);
  - lowering Saki's standing by losing (CIDOL 006_01);
  - having betrayed her athlete parents by choosing idols (Dear 026).

  Each is voiced late and privately. Re-anchor the §11 father exchange to Ume's question (L722–L729).
- **Benefit:** a fear structure the core does not have. **Deps:** HSCA-144 (Batch 6-A) is the UME-C06 counterpressure; co-land. **OA:** no.

### 3-11. CORE-Misuzu and RS-I §5

**SAA-025 · CMP11-C006 · UNDERWEIGHTED · R01 Q · OA: no**

- **T/C:** CORE-Misuzu §4, §9, §28.3 and the SL1.1 refresh; a new EVM claim. §9 traces the Temari reconciliation through Dear 006, 007 and CIDOL 010, but not Dear 009.
- **A1:** adv_dear_hmsz_001 L116–L138; dear_003 L28–L51; dear_009 L119–L157, L249–L394 (L302, L367, L378); SL1.1 cidol-hmsz-3-018_01 L279–L322; 018_03 L172–L233; dear_037 L244–L441; P1 after-audition-mid-normal-01 choice 2.
- **Change (STRENGTHEN):** add a recognition and acceptance subsection.
  - Dear 001 makes "understand and accept me" the entry condition. Dear 003 records how rarely she hears that she works hard.
  - In Dear 009 Temari's 'がんばったね' reconciles the pair, and Misuzu answers in plain 'うん' and cries.
  - SL1.1 CIDOL 018_01: "for the first time in my life". Dear 037 thanks him for "always valuing and praising my effort".

  Add Dear 009 to §9. **R01 correction:** do **not** say that Misuzu "names the Producer the second one". His cue (L378) points at Temari, and 'ふたりめ' most plausibly counts Temari as the second recogniser after him. Record that, or flag the referent as ambiguous. Add the P1 praise branches as branch-scoped corroboration.
- **Benefit:** a longitudinal need. **Deps:** SAA-087; Dear 009 L302 is cited in SAA-004. **OA:** no.

**SAA-084 · CMP11-C002 · UNDERWEIGHTED · — · OA: no**

- **T/C:** RS-I §5.2, §5.6, §12.3; CORE-Misuzu §9 and §30 (P1); RSL row 66, open item. RSL row 66 leaves "Misuzu-side motives and consent practices" open.
- **A1:** P1 after-audition-mid-normal-04 L78–L108; final-normal-04 L25–L56; final-normal-02 L18–L42; adv_dear_hmsz_002 L82–L149; dear_005 L47–L84; dear_016 L183–L225; dear_024 L606–L610 (inner); dear_025 L150–L170; dear_ttmr_009 L324–L341; dear_ttmr_017 L226–L242; U1.
- **Change (STRENGTHEN):** add a Misuzu-side SyngUp paragraph.
  - In P1 she was the mediator who never formed her own reactions (a branch).
  - She remembers quarrels, and still hears internalised reproaches ('意識低いんじゃない？').
  - She calls supporting Temari's centre position her happiness, framed as a deliberate concession: Temari is "the only idol I allowed to sing in front of me" (Dear 025).
  - Her teammates scolded her for low effort (Dear 002).
  - She enjoyed the trio to the end; attribute her reasoning about Rinha's distress as *her belief* (see SAA-142).
  - She kept a private two-person promise with Temari that Rinha "cut into".
  - She calls her old role a birdcage.

  Close or narrow RSL row 66.
- **Benefit:** the Misuzu side of the triangle. **Deps:** ⚠ the RS-I §5 hotspot; SAA-142, SAA-045. Rediscovers HSCA-031. **OA:** no.

**SAA-085 · CMP11-C003 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Misuzu §3, §14; C23, C24; the Misuzu core pass report, "Strongest V2 corrections" item 5, by erratum. §14 says Dear 032 shows she "has cried privately after major defeat".
- **A1:** adv_dear_hmsz_022 L67–L145; dear_032 L186–L270 (L190).
- **Change (REVISE):**
  - The hidden crying happened in the earliest SyngUp period, in Kei's heyday, when the unit was called Rinha's one-woman unit. It was frustration at being outclassed, not a reaction to a defeat.
  - Add the Dear 022 self-report that she "lost every day" to Kei and Rinha from middle-school entry and was frustrated "the whole time". This is the origin of her habit of stored resentment.
  - Qualify §3: her confidence coexists with a long private history of losing.
- **Benefit:** the crying context is corrected. **Deps:** SAA-004 narrows §3/§14 in PR-2. ⚠ The §14 hotspot (SAA-004, 086, 249). The pass report is a completion artifact, so use an erratum (see §Closing). **OA:** no.

**SAA-086 · CMP11-C004 · OMITTED · — · OA: no**

- **T/C:** CORE-Misuzu §14, §16, §18, §29.3, §30, §32 (OPEN-03/04); SIDE §5.1; NPC (Shuka). Shuka and 100 Pro are absent from every Misuzu home.
- **A1:** adv_dear_hmsz_017 L166–L293; dear_029 L272–L299; dear_030 L62–L439; dear_031 L124–L132; dear_033 L132–L150, L326–L356; dear_025; dear_028.
- **Change (STRENGTHEN):** add a Dear 028–033 subsection.
  1. The Shuka unofficial live and its narrow loss.
  2. Her explicit refusal of the growth-from-defeat narrative (Dear 031), which is counterevidence to §14's model of defeat as fuel.
  3. The Producer's admitted strategy of selling Misuzu and Temari to 100 Pro (Dear 033), plus his earlier covert production of the rival Temari "to keep Misuzu in top shape". Both are relevant to §29.3 and OPEN-03/04.
  4. Her definition of top idol as "a rainbow stairway we walk leisurely".
  5. The integrated world statement (Dear 033).

  Cross-reference SIDE §5.1.
- **Benefit:** a phase the core skips. **Deps:** ⚠ §14; SAA-048. Rediscovers HSCA-033. **OA:** no.

**SAA-087 · CMP11-C007 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Misuzu §27.3, §27.6 and a new §27.8; JVR "Hataya Misuzu — Phase-3 written-register baseline". §27.6 says "まりちゃん and りんちゃん preserve childhood intimacy even when the relationships become competitive".
- **A1:** adv_dear_hmsz_012 L90, L140; dear_014 L298; dear_016 L309; dear_019 L111, L142; dear_034 L702; dear_036 L1078, L1266; dear_009 L277, L296; dear_027 L312; cidol 010_03 L193; cidol 014_03 L176; school_005 L36–L57; activity_010 L17; E014.
- **Change (REVISE, narrowing §27.6):**
  - At peaks of confrontation she drops the nickname: bare 燐羽, or リーダー to challenge rank.
  - She uses bare 手毬 at the two summits with Temari.
  - Add: the single {user}さん; third-person self-reference by full name; 星南会長 → 星南先輩 at her confession; polite register in her inner speech, which supports "politeness is not a mask"; waka; まりちゃん as her only non-surname address among peers.
- **Benefit:** a fuller address system. **Deps:** SAA-004. Rediscovers HSCA-120. AV-pending (AV-HYP-MISUZU-04). **OA:** no.

**SAA-088 · CMP11-C008 · UNDERWEIGHTED · — · OA: yes**

- **T/C:** CORE-Misuzu §18, §26; C33; THEME (celestial). §18 says "Temari is repeatedly moon-coded … Misuzu's own late image is night sky / heavens / space".
- **A1:** adv_dear_hmsz_037 L56–L76; dear_002 L238–L245.
- **Change (REVISE):**
  - Add the opening wish of Dear 037: under a large moon in a cloudless sky she says "I want to be an idol like that", and the Producer answers "you were".
  - This reuses the image she gave Temari in Dear 002, a light that shines strongly when supported, so it qualifies the core's assignment of moon to Temari and night sky to Misuzu at the endpoint.
  - Keep the meaning open.
- **Benefit:** corrects an endpoint motif assignment. **Deps:** AV-C (stills). **OA: yes.**

### 3-12. CORE-Sena

**SAA-027 · CMP12-C004 · MISINTERPRETED · R02 S · OA: no**

- **T/C:** CORE-Sena §25 (Saki); SENA-C40; RS-II §13.7. §25 says "A rival can emerge outside Sena's authorship"; C40 says "independently formed", citing Dear 025.
- **A1:** adv_dear_jsna_025 L489–L511 (L504–L511); dear_026 L196–L218 (L203); cidol-jsna-3-011_02 L115–L130; dear_004 L109; SL1.1 dear_030 L97–L147; D-SAKI 026 L420–L425 (cross-route parallel only).
- **Change (REVISE, narrowing):**
  - Sena did not produce Saki, and Saki's central engine is Ume.
  - But in D-SENA, Saki credits Sena's wall-breaking with teaching her that idols have no limits (L504–L511). The inspiration runs both ways ("another me" on each side); it is not independence.
  - Correct the locator: the "another me / saviour" evidence is Dear 026 L196–L218 and CIDOL 011_02 L115, not Dear 025.
  - Keep "outside authorship" only in the narrow sense of "not produced".
  - R02 addition: 救世主 recycles Sena's term for her intended successor (dear_004 L109).
- **Benefit:** fixes an overstated independence and a wrong locator. **Deps:** ⚠ coordinate with SAA-039 (Sena as co-author of Saki's talent model). Rediscovers HSCA-148; extends HSCA-058. **OA:** no.

**SAA-028 · CMP12-C006 · OMITTED · R02 S · OA: no**

- **T/C:** CORE-Sena §35 (Japanese register); JVR Juo Sena baseline. §35.5 says the rank terms "gradually make them overlap", without the mechanism.
- **A1:** adv_dear_jsna_008 L186; 009 L383; 020 L91 (choice branch), L236; 021 L137; 037 L250, L364; cidol 000_01 L80; dear_016 L279; dear_017 L393; dear_027 L304; dear_028 L428; P1 after-audition-final-failure-01 L96; activity_008 L58 (choice branch); cidol 002_03 L31; 011_02 L203; 020_02 L189; fktn dear_027 L151; hmsz dear_029 L151; atbm dear_026 L139.
- **Change (STRENGTHEN):**
  - The stable formula 勉強になる, which meets praise and comfort as technique, and its single explicit failure at Dear 037 L250.
  - The ruby system on 一番星: 《私》, 《トップアイドル》, 《アイドル》.
  - Register by addressee: keigo to staff, with a locator, and an SL1.1 sub-entry for 十王社長.
  - R02: mark the choice-branch instances. Tsubame also uses 一番星《トップアイドル》, so present the system as route-level and Sena-centred.
- **Benefit:** the mechanism behind §35.5's claim. **Deps:** rediscovers HSCA-126. **OA:** no.

**SAA-089 · CMP12-C002 · UNDERWEIGHTED · — · OA: no**

- **T/C:** the D-SENA interpretation and the per-object gloss in `GKM_SENA_TRANSCRIPT_REFRESH_20261112.md`; CORE-Sena §33 (a 1.1 pointer); SIDE §2.4; RSL Sena–family; NPC SL1.1 President Juo row. The gloss reads "She recalls the President's earlier refusal to admit her".
- **A1:** SL1.1 adv_dear_jsna_034 L291–L421 (L323, L349, L361, L369, L378, L385–L401, L413); cidol-jsna-3-017_03 L124, L139–L148, L186–L209 (L205).
- **Change (STRENGTHEN):**
  - After her first Prima Stella, the 100 Pro president told Sena she would not make it as a pro. She took this as confirmation, did not contest it, and drifted for a long time before meeting the Producer.
  - Link this to the father's account of the laid rail and the mother's warning (CIDOL 017_03), to "misunderstandings pile up" (L205), and to Misuzu's "せっかちな親子".
  - Correct the per-object gloss and propagate.
- **Benefit:** a misread SL1.1 scene. **Deps:** ⚠ SIDE §2.4 after SAA-033; SAA-090. Flashback staging AV-C, optional. Extends HSCA-070. **OA:** no.

**SAA-090 · CMP12-C003 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Sena §33, §5; SIDE §2.4. §33 says "Her father appears colder and more indirect… care expressed through practical, restrained gestures". §5 reads her upbringing as "both achievement and evidence of deprivation".
- **A1:** adv_cidol-jsna-3-002_02 L167–L185, L192–L205, L243–L284; 002_03 L76, L95–L106; dear_005 L197–L206 (L204); dear_012 L15–L17.
- **Change (STRENGTHEN):**
  1. Set Sena's claim of "good relations" against her own account of rare contact. The Producer engineers the reunion.
  2. Her portrait of the father as possessive of favoured idols ('決して手放さない'), which the Producer privately reads as describing Sena.
  3. Her own valuation of the laid rail as happiness (Dear 005 L204), beside the analyst's "deprivation".
  4. Grandfather and son on opposite sides of N.I.A. planning, labelled as in SAA-033.
- **Benefit:** text-grounded family claims. **Deps:** ⚠ SIDE §2.4 (SAA-033, 089). Rediscovers HSCA-150. **OA:** no.

**SAA-091 · CMP12-C005 · UNDERWEIGHTED · — · OA: no**

- **T/C:** CORE-Sena §4 (stat vision); SENA-C05. §4 says "The route never reveals the measurements to be fraudulent", and the only counterpressure is "some values are partly comic or approximate".
- **A1:** adv_cidol-jsna-3-016_01 L136–L150; 016_02 L54–L55; dear_jsna_003 L194–L198.
- **Change (STRENGTHEN):**
  - The eye can return nothing at all: with Ume she "saw nothing", a first for her.
  - Her best scouts were made on intuition (Ume) and on a "click" (Misuzu).
  - Affect inflates her figures (100,000).
  - Cite the Hiro anomaly that the ledger already records.
- **Benefit:** records the limits of her vision and her decision style. **Deps:** SAA-018, SAA-075. Rediscovers HSCA-071. **OA:** no.

### 3-13. CORE-Tsubame

**SAA-029 · CMP13-C001 · UNDERWEIGHTED (P1 → P2) · R03 Q · OA: yes**

- **T/C:** CORE-Tsubame §6 and §20 (a cross-reference); a new TSB row after TSB-054; the LEG row "Tsubame saves Sena because she needs rivalry to survive"; RS-II §5.3. §6 says: "Tsubame never truly wants Sena imprisoned by idolhood… why the late retirement conflict cannot be reduced to possessive refusal".
- **A1:** adv_dear_atbm_003 L196, L261, L305, L311, L360–L364, L374–L394, L425, L440; dear_010 L317–L343 (L326, L338); dear_024 L239–L250, L305, L452–L466.
- **Change (REVISE, as narrowed by R03; the MISINTERPRETED label is dropped):**
  - Add D003 as the first retirement thread, cross-referenced from §20: Sena announces she will quit; Tsubame answers '……私は、嫌だ' (L364); the Producer converts the grief into wounded pride; her goal becomes blocking the retirement (L440).
  - Quote D010 L326 'だから、アイドルは辞めさせない' with its "make her realise" clause. It works through the joy of rivalry, consistent with §6.
  - Narrow §6's "never truly wants" so that it concerns imprisonment by idolhood, not acceptance of retirement.
  - LEG: note that the V1 claim fits the D003–D010 stage.
  - The new TSB row: "early Tsubame refuses Sena's retirement; acceptance is a late development she herself calls ego" (D024 L250 'ただの私のエゴ'; L305).
- **Benefit:** a developmental stage is restored. **Deps:** SAA-093, SAA-148; ⚠ the §6/§20–22 hotspot. HSCA-019 (Batch 6-A: Tsubame binds Sena's career by a contest after D024) is adjacent; co-land. **OA: yes.**

**SAA-092 · CMP13-C002 · UNDERWEIGHTED (OQ#6 open although answered) · — · OA: no**

- **T/C:** CORE-Tsubame §4, §34, §47 OQ#6; TSB-017; the Tsubame refresh, "Common repertoire and voluntary rest". OQ#6 asks: "Does Producer ever recognize the ethical cost of engineering humiliating encounters…?"
- **A1:** adv_dear_atbm_006 L206–L247 (L221–L225, L238); dear_010 L113–L148 (L122–L130); dear_020 L45–L58; dear_016 L346–L369; P1 final-failure choice 1 L48–L55, choice 3 L110; ending-normal-05 L16–L17; SL1.1 cidol 015_01 L100–L143; dear_028 L233.
- **Change (REVISE, closing or narrowing OQ#6):**
  - In D006 he immediately discloses that he set Misuzu on Tsubame, accepts the cost and apologises (L238).
  - In D010 Tsubame ratifies it.
  - In D020 he admits deliberately choosing an enemy she could not yet beat.
  - P1 has apologies; SL1.1 has self-critique.
  - Reformulate the asymmetry finding: the manipulation is disclosed, apologised for and ratified. The residual question is whether disclosure after the fact suffices.
- **Benefit:** stops an answered question being posed as open. **Deps:** ⚠ §34 (SAA-094, 151). Rediscovers HSCA-110. **OA:** no.

**SAA-093 · CMP13-C003 · OMITTED · — · OA: no**

- **T/C:** CORE-Tsubame §20–§22; TSB-037, TSB-050; RS-II §5.4. §20 says Sena "concludes that her own growth has ended and that Tsubame can carry the future".
- **A1:** adv_dear_atbm_019 L366, L378, L387; dear_020 L166–L172 (L170); dear_021 L579–L594 (L594); dear_024 L571–L641 (L578, L633).
- **Change (STRENGTHEN):**
  - The trigger is a misheard heroic offer. Tsubame's "I will carry your burden" (019 L366), meant as sharing ('私も一緒に、背負ってやれる', 020 L170), is heard as succession ('燕になら、任せられるわ', 019 L387).
  - Sena cites it as her reason (021 L594). At D024 Tsubame clarifies, and Sena admits she used Tsubame's words.
  - Tie this to the paternalism question in TSB-037.
- **Benefit:** a crisis mechanism. **Deps:** SAA-029; ⚠ RS-II §5.4 (SAA-030, 251). Rediscovers HSCA-018. **OA:** no.

**SAA-094 · CMP13-C005 · OMITTED · — · OA: yes**

- **T/C:** CORE-Tsubame §34; RSL Tsubame ↔ Producer (Phase-3 and SL1.1 tables); the Tsubame refresh, "Star quality and reciprocal help". §33 bounds romance language for Sena only.
- **A1:** adv_dear_atbm_017 L226–L252 (L241); dear_026 L476–L482 (L482); dear_027 L87–L114 (isInner L87, L92, L114); P1 ending-true-01 L187–L200 (L198); SL1.1 dear_037 L102–L119, L312–L330.
- **Change (STRENGTHEN):** add a bounded paragraph.
  - Tsubame claims the Producer as hers before a third party.
  - She vows that he will never again say he will leave her side, then privately disowns the line as "a figure of speech" (inner).
  - She mutters 'まるで愛の告白だな' at his confession at the P1 true ending.
  - In SL1.1 she claims him "for all eternity".

  Apply the corpus's caution (Sena §33; Hiro): possessive, romance-coded attachment, without formalising romance.
- **Benefit:** applies a consistent standard across subjects. **Deps:** the romance-coding policy (SAA-068); ⚠ §34. Rediscovers HSCA-020. **OA: yes.**

**SAA-095 · CMP13-C007 · OMITTED (in the SL1.1 refresh) · — · OA: no**

- **T/C:** the Tsubame refresh, "Star quality and reciprocal help" and "Integration proposals"; TSB-066 SL1.1 note. The refresh does not report D029 L191–L195.
- **A1:** SL1.1 adv_dear_atbm_029 L171–L210 (L191–L195); dear_031 L13–L50.
- **Change (REVISE):**
  - The Producer explicitly subordinates rivalry to rescue: she wanted to beat Sena in order to save her, and her essence is "not an idol for fighting". Tsubame accepts this as the explanation for her summer loss.
  - In D031 he tells her to keep the fang of pride alongside gratitude.
  - Qualify "heroic rivalry" so that in SL1.1 rescue and gratitude are primary, and rivalry is instrumental but retained.
  - Keep this attributed to the Producer.
- **Benefit:** completes the refresh. **Deps:** SAA-256. **OA:** no.

**SAA-096 · CMP13-C008 · OMITTED (outcome) / CROSS_REFERENCE_GAP (SIDE §4.3) · — · OA: no**

- **T/C:** CORE-Tsubame §14, §15, §47 OQ#1; SIDE §4.1 ("Through Tsubame") and §4.3. OQ#1 asks whether Tsubame's hero ideal can accommodate someone who refuses to be saved. SIDE §4.3 builds Gekka/Shion from story_0105 only.
- **A1:** adv_dear_atbm_016 L129–L170, L278; dear_018 L121–L123; dear_019 L54–L75, L117–L161; dear_023 L245–L264, L416–L420; SL1.1 dear_034 L117–L124, L248–L272; cross-track dear_jsna_025 L565–L689.
- **Change (STRENGTHEN):**
  - Record the result of the D018 wager: Gekka concedes and takes Shion home; by D023 she trains Shion daily and credits Tsubame.
  - Record the refusal evidence that narrows OQ#1: Shion rejects pity; Tsubame concedes that her present self "cannot reach her heart", without coercion.
  - Cross-route: in D-SENA 025, Saki never let Tsubame help.
  - Route the D-TSUBAME evidence into SIDE §4.3 as a second witness of sister repair, separate from story_0105.
- **Benefit:** answers OQ#1 in part. **Deps:** ⚠ SIDE §4.3 (SAA-020); the Gekka naming (SAA-261). Rediscovers HSCA-021/161. **OA:** no.

### 3-14. KANAE reading and the SL1.2 ledgers (PR #600 content)

**SAA-099 · CMP14-C004 · UNDERWEIGHTED · — · OA: no**

- **T/C:** the THEME SL1.2 section (new THEM-R88-VIEW and shadow/light rows); KANAE §Admission (the D002 paragraph) and §Dear 001–010 (the D010 paragraph). THEME has no row for the shared view or for shadow and light.
- **A1:** hkne_000-05-horizontal L255–L346; D002 L223, L277; D005 L572, L607; D007 L443; D010 L369; P1 ending-true-01 L209 (C3); D004 L503; D006 L290; cidol-hkne-3-000_03 L146–L151; H01 L143; H03 L665; D009 L130–L135.
- **Change (STRENGTHEN):**
  - Add a theme row for "same height / same view": from Misuzu's image (H05) to Kanae's resolve, her declaration addressed back to Misuzu (D002 L223), the night fantasy, her wish, the closing dream and the P1 parallel.
  - Add a shadow/light row.
  - Add a clause to the D002 paragraph noting that Kanae reuses Misuzu's image.
- **Benefit:** two motifs of PR #600's new reading gain theme-ledger rows. **Deps:** SAA-153 (the D010 paragraph). **OA:** no.

**SAA-100 · CMP14-C005 · UNDERWEIGHTED · — · OA: no**

- **T/C:** KANAE §Produce Series 001, after the table; BRL BR-R88-HKNE-RESULT (invariant column). The P1 table treats the stakes "in passing".
- **A1:** P1 after-audition-final-failure-01 L18 (shared); before-audition-final-normal-01 L114–L119 (option 3); after-audition-mid-normal-03 L29–L46 (option 1), L105 (option 3); ending-normal-04 L80–L83 (option 2); ending-normal-02 L59–L65, L87–L95.
- **Change (STRENGTHEN):** add a note on stakes that recur across states.
  - (1) Shared: her first fear is losing her place beside China (L18); the Han Xin option names the stake as her position as 近侍.
  - (2) Option-bound: she derives her standard from the hierarchy of "tops" in the Kuramoto Group and around China.
  - (3) Option-bound: idol failure would bar her return to China's side.
  - (4) Option-bound: Kanae makes 欲/エゴ conditional, unfit for a servant but admissible for an idol.
- **Benefit:** the invariant becomes visible. **Deps:** none. **OA:** no.

**SAA-101 · CMP14-C006 · UNDERWEIGHTED · — · OA: no**

- **T/C:** the JVR SL1.2 section; an optional register paragraph in KANAE. The JVR has five SL1.2 Kanae rows and one SL1.1 row.
- **A1:** D002 L26; H01 L898; H04 L1189; adv_dear_kcna_023 L353; activity_017-01 L54; csprt-3-0122_03 L31; school_005 L50; D005 L607, L676; P1 final-normal-02 L138; after-step-2-normal-01 L166; D008 L722; cidol-hkne-3-000_02 L6; D010 L8, L302; activity_016 L83; D007 L102; pgrowth_01 L28; activity_017-02 L89.
- **Change (STRENGTHEN):** add register rows.
  - (a) Her own name as first person (香名江は…) is reserved for China; she uses 私 elsewhere.
  - (b) The ruby アイドル《お嬢様》.
  - (c) Imperatives addressed to herself, and the vocative ……香名江。
  - (d) A proverb and classical-maxim idiolect.
  - (e) Feudal hyperbole.
  - (f) The gap between formal outer speech and gushing inner speech.
  - (g) The late adoption of China's ごきげんよう.
  - (h) 誤解しないでください turning playful.
- **Benefit:** register coverage for a new character. **Deps:** SAA-098. **OA:** no.

### 3-15. JVR: addressee speech levels

**SAA-107 · CMP16-C003 · UNDERWEIGHTED · — · OA: no**

- **T/C:** JVR "Katsuragi Lilja — Japanese voice/register AV refinement"; the AVA-Lilja open-question list (L167); S03c §31. The JVR says that "Lilja's polite わたし-based register is stable across many states".
- **A1:** csprt-3-0042_01 L17; 3-0054_01 L65; 3-0059_02 L22; 3-0063_01 L125; 3-0049_01 L52, L76; 3-0049_03 L84; 3-0040_02 L95, L101; 2-0053_02 L81.
- **Change (REVISE, narrowing):**
  - The polite register holds for Producer-facing, senior and some same-year addressees. With Sumika, Saki, Kotone and China, Lilja speaks plainly.
  - Add an addressee speech-level map: Lilja; Rinami→Sena; Saki→Sena/Tsubame; China→Kanae.
  - Record address-term transitions: Lilja 月村さん→手毬ちゃん; Temari あなた→清夏.
  - Close the AVA open question by cross-reference.
- **Benefit:** refines the model without reversing it. **Deps:** ⚠ the same JVR block as SAA-198; SAA-102(4). **OA:** no.

### 3-16. Institutions, the Producer, continuity and Kaya Rinha

**SAA-034 · CMP18-C007 · OMITTED · R08 Q · OA: no**

- **T/C:** SPINE §4.2 (a pointer only); INST-NIA (a new convention row) and a new INST-CLASS3 row; CONT MAP §3.2. The N.I.A. rules are listed without any eligibility limit.
- **A1:** adv_dear_hume_012 L75; adv_dear_ttmr_011 L5–L34, L114–L124; adv_dear_jsna_011 L12–L26; dear_jsna_012 L79.
- **Change (STRENGTHEN, as qualified by R08):**
  - Add INST-CLASS3: each idol-course year's class 3 gathers students with special circumstances (active idols, idols of agencies other than 100 Pro, scouted special students), with Rinha as the one non-active member (D-TEMARI 011).
  - Add route-scoped notes on N.I.A. conventions:
    - In the D-routes N.I.A. is framed as a rookie tournament from which top idols abstain by **暗黙の了解**, an unwritten understanding that is breached in D-SENA and absent in P2-SENA.
    - The exclusion of class 3 is a single Producer expectation.
    - The link between Rinha's transfer and her N.I.A. entry is the Producer's reading of 961's intent.
  - Keep SPINE §4.2's P2-common rule statement unchanged apart from a pointer.
- **Benefit:** fills an institutional gap without overstating unwritten conventions as rules. **Deps:** SAA-033; SAA-225 (INST-NIA, Batch 4), the same row. **OA:** no.

**SAA-035 · CMP18-C008 · OMITTED · R08 Q · OA: no**

- **T/C:** SIDE §4.5, §4.6, §15 Q12; NPC Kuroi row; INST (new external-institution rows). Q12 asks "What exactly is Kuroi's institutional role and authority?", and "961" occurs 0 times in SIDE, SPINE, INST, NPC and RS-II.
- **A1:** adv_dear_atbm_012 L125; adv_dear_amao_013 L180; dear_amao_018 L250, L284; adv_dear_hume_016 L10–L60 (L30, L38, L45–L49); adv_dear_kcna_010-01 L83, L112 (a cutaway shared by ten Dear 010-01 objects).
- **Change (STRENGTHEN, with R08's continuity hygiene):**
  - 極月学園 is a small elite school funded by 961 Pro (Sena, atbm_012 L125) or founded by it (Mao, amao_013 L180). Keep the variance between 出資 and 設立 as attributed statements.
  - Kuroi is its 理事長 (kcna_010-01 L112).
  - 961 does not employ "producers" (hume_016 L38). This is choice-branch content (C3), asserted by the Producer or by Kuroi.
  - Gekka claims 961 as N.I.A.'s organiser (D-MAO, route-scoped).
  - Hatsuboshi teaches a critical course on 961-style production.
  - Kuroi's 'あの老いぼれと冷血漢' (hume_016 L45–L49) leaves the referents unnamed (C3).
  - Rinha's 終活 is already covered (RMX C023/C024).
  - CMP02's report adds Kuroi's D-TEMARI scenes (dear_010-01; dear_026 L225), routed to the institutional comparator; include them.
- **Benefit:** answers an open question and fills the rival institution's entry. **Deps:** SAA-033; ⚠ SIDE §4.5/Q12 with SAA-236. Extends HSCA-150. **OA:** no.

**SAA-115 · CMP18-C001 · OMITTED (PRESERVE §9.2 + STRENGTHEN) · — · OA: no**

- **T/C:** RS-II §9 (a new §9.13, "Producer invariants"); NPC Producer row; JVR Producer baseline. §9.2: "These functions rhyme, but they are not one simultaneous biography".
- **A1:** adv_presult_003_final-failure L3; startup_2024_user-bd-01_hmsz-01 L19–L22; tower-001 L27–L32; tutorial_first_cmmn-00 L164; pstory_001_amao_after-audition-mid-failure-01 L46.
- **Change:**
  - PRESERVE §9.2's differentiation by branch.
  - STRENGTHEN with an invariant layer, each trait carrying its source family:
    - he takes responsibility for every failure (C3 results files);
    - he sets himself aside about his own life, for example forgetting his birthday (C4 startup);
    - he cares through research;
    - his baseline is です/ます + さん to idols, with 俺 in parenthesised thought surfacing at moments of exposure;
    - he has a wry inner voice;
    - he hides grief from the idol and admits uncertainty only to his teacher, which is Producer-side evidence for Asari's "reliable magician" (§9.8);
    - he is a fan of idols, including rivals.
- **Benefit:** a monograph can distinguish route function from character. **Deps:** SAA-287; ⚠ the RS-II §9 hotspot; SAA-189, SAA-006. **OA:** no.

**SAA-116 · CMP18-C003 · CROSS_REFERENCE_GAP · — · OA: no**

- **T/C:** CONT MAP §3.3/§8; `02_CONTINUITY_AND_STORY_STATE/GKM_BRANCH_TOPOLOGY_AND_RESULT_STATE_MODEL.md` §5.5; CONT; BRL; SPINE §16.2 and Appendix A LOC-INST-020. These say: "No individual Series 3 pstory fragments exist for Kotone, Sena, or Tsubame in Source Lock 1.0 … NOT PRESENT IN LOCK".
- **A1:** pevent_003_cmmn_school_1-006-02 L5, L13; school_3-005-02 L5, L13, L22–L25.
- **Change (STRENGTHEN the continuity map; REVISE the scope of LOC-INST-020):**
  - Add rows: the SL1.0 pevent_003 variants -02 presuppose a P3-C[SENA] run, with the Producer as Sena's 担当 and a 4連覇 defence.
  - The P3-C world state is unchanged, and Sena's P3 Produce Story remains absent.
  - Scope LOC-INST-020 as a lesson variant for Sena's producer.
  - Note that SL1.1 P3-SENA material now supplies fragments.
- **Benefit:** corrects a "not present" statement. **Deps:** SAA-026. **OA:** no.

**SAA-117 · CMP18-C009 · TRACEABILITY_GAP (REVISE classification and counts) · — · OA: no**

- **T/C:** XW §0.1–§0.2 counts, rows RINHA-XW-014 and RINHA-XW-064, and the SL1.1 addendum; RMX C058 (observer/direct columns). XW-064 and XW-014 read "UNIT_CONTEXT_ONLY … 0 … NO_RINHA_VOICE". §0.2 counts by displayed speaker, while §1 freezes the actor code krnh as the entity identifier.
- **A1:** adv_dear_hmsz_019 L101–L108 (voices krnh-001..003); adv_cidol-ttmr-3-009_01 L176 (voice krnh-001); SL1.1 adv_dear_fktn_035, a group line (voices sson/andk/krnh).
- **Change (REVISE):**
  - Re-resolve Rinha's speech by actor and voice stem as well as by display name.
  - Reclassify XW-064 and XW-014 as voice-attributed Rinha objects with a masked speaker, adding 4 messages (620 → 624 under actor resolution). Keep the displayed-name count as a separate figure.
  - Record the SL1.1 group line.
  - Route hmsz_019 to RMX C058/C045 as possible care-by-presence, with diegetic presence OPEN.
- **Benefit:** the crosswalk follows its own entity rule. **Deps:** **the Rinha AV gate stays open**. ⚠ XW is also touched by SAA-158, 242 and 165 and by HSCA-159. ⚠ The 620 figure also appears in `CURRENT_STATE_AND_CORPUS_MAP.md` ("Current Rinha AV execution"): update it there by targeted edit, showing both counts. AV_DEPENDENT for diegetic presence and delivery. **OA:** no.

---

## Batch 4 — P3 traceability, locator, wording and minor additions, by target file

This batch holds the 89 remaining P3s. SAA-118, 124, 139, 152 and 161 were reviewed and appear in their qualified form; the rest are specialist-only. Every row is a targeted edit. Land each row together with the Batch 2/3 edits to the same file, so that each file is opened once per PR.

Transition codes: S = STRENGTHEN, R = REVISE, P = PRESERVE, O = OPEN. "Ev." is the A1 evidence.

### 4-1. CORE-Saki

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-118 (C002; R01 Q) | §11.2, §17.4; JVR Saki row | §0 "speaks of fans as 外付けの筋肉"; §11.2 "Saki accepts…" | dear_hski_013 L83–L109 (L93); 015 L76–L95; 020 L50–L79, L111–L115 | **R** (narrowed by R01): add the origin, which the Producer coins for her ('咲季さん向けに言うなら'), and her re-readings 力の源 / 外付けの勇気 / 勇気の源; revise §11.2 so the "real ability" claim is the Producer's; JVR note "P coins; Saki adopts"; keep the §0 and §20.4 lists | origin of a signature metaphor | **OA: yes** |
| SAA-170 (C011) | §14.3, §14.7, §14.8, §3.2.3; JVR | §14.7 address table covers five addressees; §14.8 asks for ruby constructions to be collected | dear_001 L239–L264; 008 L274; 009 L133; 010 L368, L390; 018 L72; 023 L180; 024 L546–L557; cidol 015/017/019; school_006; activity_021 | **S**: register to trainers, Tsubame and Minase Iori; 星南会長 → 星南 (Dear 024); お姉ちゃん self-address (school_006); rubies 未来《さき》, 試合《ゲーム》, 敵《ライバル》, 理《ことわり》, 根源《ルーツ》; the 悪あがき lexical arc | answers §14.8's own request | — |
| SAA-171 (C012) | SIDE §2.1; CORE §3.4, §6.4 | the Hanami household is modelled without grandparents | dear_010 L298–L302; unit_01-02_02 L399; 02_03 L500–L519; dear_037 L231; cidol 018_01 L35–L66; supports 2-0034, 3-0074/78/81/112 | **S**: raised largely by grandparents (Dear 010); a farming grandfather; Halloween costumes; §3.4 items (2 April; Minase Iori; aromas; untidy room) | family synthesis completed | ⚠ SIDE §2.1 with SAA-239 |
| SAA-172 (C013) | SAKI-C05, C31 (counterevidence column); RS-I §3.11 | C05 "deepest fear is loss of the older-sister relation" | P1 after-audition-final-failure-01 choice 3 L84–L119; dear_014 L222–L240 | **S** (limiting evidence): one loss could not disillusion Ume, so the burden is an admiration she cannot shake; Dear 014 reassurance she cannot apply to herself; branch-scoped | bounds a fear claim | — |
| SAA-173 (C014) | §10.6, §6.4, §21 | "the Producer still controls access, schedule, body-management…" | cidol 011_03 L99–L135; dear_010-01 L6–L11; school_009 L121–L127; dear_007 L234–L255 | **S** both ways: report sessions with her parents since scouting, learned by rumour (asymmetry); Saki keeps nutrition and body control; refuses harsher training | body authority shown as shared and disputed | ⚠ §10.6 with SAA-041 |
| SAA-174 (C015) | §3.2.5, §3.3.5, §12.5, §13.2 (ENDLESS DANCE row); CONT support note | origins treated singly; CONT keeps the identity OPEN | cidol 008_01 L144–L220; 008_03 L106–L123; dear_008 L203–L211; 010 L355–L368; 021 L209–L279; 026 L420–L425; dear_amao_031; support 3-0052_03 | **S**: layered disclosures by audience (public; fans; the Producer; Sena; Mao), kept secret from Ume; cross-reference the CONT note to Dear 021/026 | origin model | — |
| SAA-175 (C017) | §5.1–§5.2; SL1.1 supplement | "relinquishes his former 大器晩成 explanation" has no SL1.0 anchor | dear_009 L357–L368; cidol 022_03 L161–L186 | **S**: anchor to Dear 009, where the Producer wonders whether Saki is the true late bloomer and she cuts him off | missing anchor | — |

### 4-2. CORE-Temari

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-179 (C009) | §3.1, §3.2.3; PSL TEM-L025; RSL early-route row | "trust begins as debt" with no P1 locator | P1 opening-normal-03 L11–L22; final-normal-01 L121–L126 (choice 3); ending-true-01 L177–L201 | **S**: P1 utility-idiom locators; the sequence "only using you" → "stay with me" → "our dream" (with an order caveat); D-MISUZU 028 'お互い様' as an echo | traceability | — |
| SAA-180 (C011) | RS-I §5.5, §6.8; CORE §3.2.9/§4.1; NPC | RS-I §5.5 rests on E016 only | dear_ttmr_024 L390–L399; 029 L491 = 015 L272; 030 L338–L389; dear_hmsz_016 L90–L114 | **S**: Dear demonstrations of Rinha's language in Temari (copying; reused lines; Misuzu's testimony) | adds witnesses | — |
| SAA-181 (C012) | §4.2, §10.5, §20; TMR-P04 | "childish dependence" | dear_007 L84–L100; 008 L112; 019 L30; cidol 000_02 L220–L225; 011_01 L159–L181; dear_016 L325–L333 | **S**: attachment repertoire ('怒ってる？' checks; P2 'どうか、一緒にいて'; crying as a lever; E016) | support for TMR-P04 | — |
| SAA-182 (C014) | BRL (a new Temari section); §3.1.2, §16 | BRL has no Temari section | dear_005 L138–L161; 010 L156–L223; 013 L403–L467 vs L818–L875; P1 ending-true-01 choice 2 | **S**: Temari branch divergence (dear_010 choice 1 is the only branch with "Misuzu is currently better"; partner reactions vary while Temari's acts do not; sales pairs) | ledger completeness | — |
| SAA-183 (C015) | §3.2.1/§3.2.3, §10.3; JVR | the 目標/夢 device is unrecorded | dear_003 L203–L235; 020 L233–L251; 034 L343–L369; 037 L136–L151 (L151 = 003 L231); cidol 009_03 L214–L228 | **S**: 目標 → her correction → 私たちの夢 → verbatim callback; the Producer's own dream is bound to her | a lexical arc | — |
| SAA-184 (C016) | §18 obs. 3, §20; TMR-P06 | "wants criticism when it is specific and actionable" | cidol 015_01 L25–L59; P2 mid-failure-01 L40–L59; P1 mid-failure-01 L21–L43 | **R** (qualify): she also asks for empathy and delicacy, conceding she once stated the opposite; add to §20 | contradiction recorded | — |

### 4-3. CORE-Kotone

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-185 (C009) | §3.2.15, §11.5, §5.1; KOTO-C23/C24; refresh | "strong reciprocal romantic coding" | dear_fktn_037 L120–L160, L380–L419 (L406, L411), L465; cidol 006_01 L34–L67; 006_03 L184–L249; dear_018 L183–L231; 021 L268–L549 | **R** (qualify "reciprocal"): initiated by Kotone and routed through the idol prohibition; the Producer's feelings are never verbalised; his reactions are partly player-selected; he keeps boundaries | proportion | romance policy (SAA-068); ⚠ D037 with SAA-052; AV-D optional |
| SAA-186 (C010) | refresh claim implications; §5.2, §3.1 | refresh items not connected to §5.2 / KOTO-C21 | P3 selection-failure-01 L50–L83 (L68); dear_036 L476; 035 L108–L253; cidol 001_01 L53–L79 | **S**: P3 L68 confirms "ordinary risk"; D036 names performed reciprocity; the comfort-bearer shifts across failure states | refresh integration | — |
| SAA-187 (C011) | §2.1, §3.2.3, §1.4; CONT | "real poor results" without time depth | cidol 013_02 L61; dear_036 L873; dear_008 L21; 006_03 L215; P2 b-normal-03 L94; 006_01 L68–L98 | **S**: three unrewarded middle-division years; first live in her fourth year; '4年目'; hard placement anchors | chronology | SAA-267 |
| SAA-188 (C013) | §3.3.8–§3.3.9, §12; RS-II §3.9 | 3-016 fear read as fan comparison | cidol 016_01 L137–L163; 019_02 L359–L388; SL1.1 dear_034 L282–L468 | **S**: the biggest reason is not disappointing two peers (L159–L163); D034 partly answers the RS-II §3.9 OPEN; route Misuzu's maxim to §3.3.9 | answers an OPEN | — |
| SAA-189 (C014) | JVR; §13 | no Producer 俺 shifts; no ことねさん endpoint; partial Sena ladder | dear_037 L612; 027 L452–L453; cidol 011_02 L103, L187; 013_01 L72; dear_012 L192; 020 L249; 025 L99; 028 L67 | **S**: 俺 as an exposure marker; 藤田さん → ことね → ことねさん; Sena ladder 十王会長 → … → アンタ | register | SAA-115 |
| SAA-190 (C015) | KOTO-C10; §3.2.4; AV "manufactured confidence" row | C10 cites Dear 007 and P1 only | cidol 006_02 L66; dear_007 L206–L207; 026 L256; 016_01 L190; 019_03 L59; dear_015 L225; 037 L577 | **S**: locators for the affirmation ritual (his policy; her recognition; she requests it; Sena names it; he admits calculation) | traceability | — |

### 4-4. CORE-Mao

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-192 (C005) | NPC Phase 3 Mao; SIDE §7.5; CORE §2.3 | "former theatre prince/top star … exact identity"; the name appears only in AV documents | cidol 015_01 L114–L123, L155; dear_010 L267–L291, L320–L333; P1 after-step-2-normal-02 L101–L125; sales_4-004-02 L8, L34 | **S**: name 龍月真希; record the track variants (D-MAO 010 / C-MAO 015 / P1 / PE); possible 'あれから' sequence | identity | the integrator note on this row belongs to SAA-131 (see How to read §4) |
| SAA-193 (C007) | §12; JVR Phase 3 Mao | §12.1–§12.3; the JVR's Dear 025 rendering drops base text | dear_001 L135, L246, L265; 004 L13; 006 L241, L337; 008 L108; 009 L46; 019 L41; 024 L299; 025 L248, L361; cidol 009_02 | **S**: register map (あなた → キミ from Dear 006; mixed キミ + です/ます; slips and the 'こほん' reset; prince peer register; role-reversal play); correct the Dear 025 rendering against A1 | register | SAA-057 |
| SAA-194 (C008) | §1.4, §8.5 (or a §9 note); RSL late row | romantic status deliberately unsettled | cidol 015_03 L227–L303; 009_03 L534; dear_010 L106–L130, L221; 014 L98; 020 L290; 023 L508; 026 L115; 037 L302–L308 | **O**: record the evidence base without adjudicating (Mao as initiator; the unfinished jealousy line; the double readings at D020 L290 and D026 L115) | evidence base | ⚠ §8.5 with SAA-001 (separate paragraph); romance policy; AV valence |
| SAA-195 (C009) | BRL BR-MAO-COMMU; CONT STATE-MAO-C; COMMU86 reading | "invariant-only unless internally dated" | cidol 018_03 L17, L174; dear_023 L574; 024 L255–L269; 026 L95, L143; 022 L174; cidol 001_01 L58; dear_032 L197 | **S**: anchors (018_03 L17 presupposes 023/024; L174 quotes 026 L95, so it is anchored after Dear 026); the somen-machine callback; variant naming of the welcome party | placement | — |
| SAA-196 (C011) | §14; CSL Phase 3 Mao | §14 lists sweets, plush history, schooling | cidol 009_02 L163–L201; dear_031 L287–L304; E022 main-01 L339–L344; csprt-3-0078_03 L83–L128; 0072_03 L148; 0078_02 L12 | **S**: only-child childhood; handicraft gifts; theatre-going and the revue motto; flour-food expertise; secret tastes | ordinary life | HSCA-102 residual (6-C) |

### 4-5. CORE-Lilja

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-124 (C003; R05 Q) | §9.2, §20; SIDE §2.6, §2.11; NPC and RSL rows | "Her mother initially worries about the idol plan" | cidol-kllj-3-018_02 L147–L152, L173–L195, L201–L206, L226–L245; C005_02 L279; E020 | **R** (narrowed): "kept opposing (ずっと反対してた), out of unfamiliarity with Japanese idol culture and worry that no one could accompany Lilja, until Lilja's own presentation"; do not reduce it to health; keep it non-hostile; add a family addressee to §20 as a gratitude/obligation hybrid ('無茶を通したからには…', L240–L245), **not** on the principal proof-obligation risk list | accuracy | — |
| SAA-198 (C007) | §17; JVR Lilja map | "センパイ as the central Producer address" | dear_kllj_001 L114–L129; C010_03 L125; C018_01 L252; D033 L413; D010 L336; D022 L623; D027 L315; C015_03; activity_020 | **S**: センパイ began as a learner's assumption he let stand; あなた at peak moments; 'わたしなんか' handled divergently; plain register with Sumika/Saki/Kotone/China | register | ⚠ same JVR block as SAA-107 |
| SAA-199 (C008) | §2, §3, §12 | "Her formal idol skills are not what the Producer notices" | cidol 010_01 L199–L277, L391–L411 (L402, L406); dear_001 L12, L191; dear_025 L416–L420 | **S**: he pre-selected her from the student files; first praise for her eyes; '惹き込まれた…あなたの目に', Shion's later verb; her trust as a deliberate choice; Dear vs communication focalisation | precision | — |
| SAA-201 (C010) | §3, §8; C16 | "Shion points to a born visual substrate…" | dear_kllj_025 L416–L463; C015_02 L94–L111 | **R** (wording): quote '日本人離れした' and '北欧の雪妖精', so the anti-exoticism rule reads as an analytical stance | transparency | — |
| SAA-202 (C011) | §11; RS-I §4.7; THEME | the stream is described as consented | dear_kllj_031 L306–L464 | **R** (narrow): disclosures went out on a stream left running; consent covers the format, not every disclosure | bounds a consent claim | — |
| SAA-203 (C012) | §4, §20 | overwork as deficit compensation | P1 opening-normal-03 L13–L23; final-normal-04 L63–L74; ending-normal-03 L17–L22; after-step-2-normal-02 L144–L166 | **S**: anxiety regulation ('なにかしていないと、不安で'; stress baking); literal uptake of instructions | mechanism | — |
| SAA-205 (C014) | §13; CSL Lilja ordinary-life row | ordinary life at synthesis level only | C005_01 L88–L191; C005_02 L145–L171; C005_03 L43–L104; C018_02 L21–L42; C022_01 L82–L95; activity_004 | **S**: a labelled inventory (Swedish customs; Drömmar; fears; childhood fevers; mother's perfume; origins of シルヴェスタ/つむじちゃん); C3 items kept C3 | monograph inventory | — |

### 4-6. CORE-China

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-207 (C007) | CHINA-C08; s5/s6 | "mature privilege ethic is stewardship" | cidol 005_02 L142, L150; sales_4-002-01 L20, L34; dear_016 L54, L67; dear_032 L175 | **R** (narrow C08 to the competitive and affective domain); record the counterexamples (Kuramoto power "without hesitation" for the Producer's welfare; a safety net in one choice; the Aoi resolution on his advice) | scope | — |
| SAA-208 (C008) | JVR China table; s8, s22 | the JVR's open question on distribution | dear_kcna_035 L179, L385; 009 L139; P3 final-normal-02 L22; 037 L399; 034 L106; C001_03 L17, L69; C018_01 L17 | **S** (items from `candidates.jsonl`): the single break to given names (D035 L385); one {user}様 and one あなた; Sena's honorific dropped (D035 L179); お姉さま vs 雨夜先輩; bare name to Kanae; わたくしのトッププロデューサー | answers an open question | — |
| SAA-209 (C009) | s3, s25 | humility as a "learning technology" | P1 mid-normal-04 L95–L108; ending-normal-02 L83–L114 | **S**: the 学園最下位 label hid hurt and served as a refuge; leaving the bottom brought a fear of being overtaken | defence model | — |
| SAA-210 (C010) | s17, s18, s24.8; BRL China | P3/P2 fragments treated as texture only | P3 selection-normal-02 L15, L23; final-failure-01 L8, L54; selection-failure-01 L38, L92–L98; P2 ending-normal-02 L29, L34; P1 final-normal-01 L45–L71 | **S** (items from `candidates.jsonl`): 立派なアイドル redefined as striving; frustration as growth; apology first; P3 failure states; P2 "believe in me"; the P1 せんせい variant | branch invariants | SAA-213 |
| SAA-212 (C012) | NPC China-side additions; RSL China ↔ Kanae; CSL family root | the identification rests on "cidol 009" | cidol 009_02 L122–L162; hkne_000-01 L564–L609; hkne D001 L425; D008 L54 | **S**: keep the identification and add D001 L425 ('幼い頃の、お爺様への直訴') and SL1.1 000-01; mark the SL1.0-era rows as inference | traceability | SAA-098; HSCA-151 |
| SAA-214 (C014) | s10, s14 | the ambition is traced through Dear 021/027/029 and Sena | dear_kcna_019 L154–L244; 020 L252–L283 | **S**: the winter ambition is first born as a promise to Hiro; the Producer's support doctrine corrects Hiro's belief | horizontal origin | — |

### 4-7. CORE-Hiro

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-216 (C011) | HIRO-C06; §8, §21 | C06 evidence is "P1 live/final states" only | cidol 016_01 L60–L78, L130–L142; 016_02 L152–L171; dear_009 L55–L62 | **S**: Dear 009 as her pre-debut statement of responsibility; the CIDOL 016 asymmetry (she spares partners but places unlimited burden on the Producer) | §21 enclosure evidence | ⚠ §21 hotspot |
| SAA-217 (C012) | §22–§23; JVR; CONT | §23 omits the catchphrase and other markers | dear_shro_020 L185–L226; 007 L155–L187; 013 L379; 010 L175; 025 L64; cidol 000_02 L65–L78; dear_017 L120–L149 | **S**: そういうところが好き; comma-set particles; impressions of the Producer; owl-only keigo; the address shift; fandom of China and owl | register | — |
| SAA-218 (C013) | SIDE §2.7; CORE §21; NPC | SIDE §2.7 records only an opportunity-cost concern | dear_shro_020 L60–L144; 024 L171–L177; 001 L166–L192; cidol 001_02 L235–L260 | **S**: the Producer's undisclosed first home visit; the father's anger; the father as the source on owl; the Chairman's intuitive admission; the hidden visit as a benign asymmetry | family evidence | SAA-002 |
| SAA-220 (C015) | SL1.1 supplement; EVM SL1.1 rows | no 037-01 interstitial, unlike the other refreshed cores | dear_shro_037-01 L14–L124 | **S**: a short, institution-scoped note (Shuka, Oboro, Serina; the 100 Pro "project"; an unnamed figure) | parity | — |
| SAA-221 (C016) | BRL (Hiro branch control) | no pair, crowdless or 模擬演習 structure | sales_1-001-01 L13–L32; live end-04-01 L1–L21; P1 ending-normal-04 L14–L71; ending-normal-05 L20–L119 | **S**: sales pairs differ only in the Producer's closing line; live-04 has no crowd commands; ending-normal-04/05 follow a 模擬演習 | structure | AV for the live-04 setting (Batch 5) |

### 4-8. CORE-Rinami

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-222 (C010) | §5; CSL Rinami ordinary-life row | §5 list; many items only in ledgers | dear_hrnm_006 L160–L205; 010-01 L26; 020 L72–L85, L241–L268; cidol 004_02/03; 017_03 L26–L60; school_007 L4 | **S**: an inventory (Fukuoka rural home; family recipes; appetite and calorie discipline; often-absent parents) | ordinary life | — |
| SAA-223 (C011) | JVR Rinami rows; CORE §22, OQ-RINAMI-08 | the JVR lacks the proposed items | cidol 017_01 L282; 017_03 L85, L104; dear_012 L509; 032 L264; P1 final-normal-02 L57; dear_036 L445 | **S**: mock-formal お姉さん rulings; わね only on demand; address variants by setting; 星南ちゃん completed at Dear 036 L445 | register | AV prosody |
| SAA-224 (C014) | §24, §25, SL1.1 supplement; NPC President Juo | the endpoint stops at the summit speech | dear_hrnm_037 L226–L375; 034 L5–L257; 030 L458–L495; SL1.1 037-01 L14–L126 | **S**: the D-endpoint professional horizon (homecoming live; a 100 Pro offer; Juo watching since N.I.A.); a pointer to 037-01; E028's exam path kept separate | endpoint | ⚠ §24 with SAA-071; HSCA-044 (6-A) |
| SAA-225 (C015) | §0; INST-NIA; metrics JSON (annotate only) | "210 source objects / 6,057 messages"; INST-NIA rule | dear_hrnm_012 L413; 011 L15, L48, L69; P2 mid-failure-01 L37 | **R** (annotation): note the count basis (6,058 raw, one nameless caption excluded); INST-NIA: N.I.A. is the gateway to H.I.F. (Dear 011 L15); **do not rewrite the metrics JSON** | traceability | ⚠ INST-NIA with SAA-033 and 034 |
| SAA-226 (C016) | §2, §9; NPC Kana row | "she alone failed to gain comparable popularity" | dear_hrnm_002 L63; 010-01 L70; 032 L295; cidol 017_02 L83; dear_013 L26–L97; 033 L192–L218; support 0005_02 L75–L79 | **S**: removed from the unit; her three framings (外された / 辞めた / 解散); the stage fear afterwards; the old unit returns as supporters at H.O.F. | before-state | — |

### 4-9. CORE-Sumika

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-228 (C008) | CONT Sumika; SONG CIDOL 007 row; CORE | "assign chronologically only when internally anchored" | cidol 007_02 L56–L139 = dear_013 L298–L373; 007_02 L148–L158 = dear_006 L418–L439; cidol 010_01–03 | **S**: verbatim anchors (Campus mode!! inside the N.I.A. rumour crisis; Lilja learns of the trauma right after Dear 006); CIDOL 010 retells Dear 001–007 | placement | — |
| SAA-229 (C010) | §9, §16; C14/C15 counterpressure | the persona "remains strong" until Dear 031–032 | dear_ssmk_016 L113–L150, L200–L247; 017 L32–L44 | **S**: the persona was porous during N.I.A.; the route to Dear 032 is graded | development | — |
| SAA-230 (C011) | §9; SIDE §4.1 (Against Sumika) | Shion as "genuine incompatibility" | dear_ssmk_018 L111; 019 L57–L89; 013 L76–L109; 014 L229 | **S**: she thanks the defeated Shion and says またね; her self-blame pattern | answer to Shion | — |
| SAA-231 (C012) | RSL Sumika ↔ Producer; RS-I §4.10; CORE | no romance-coding status line | dear_ssmk_033 L334–L398; 026 L246–L299; 027 L147–L190; 028 L385–L419 | **O**: a status line (attraction effectively conceded to Lilja; the "proposal" reading the Producer disowns); triangle coding under RS-I §4.10 | consistency | romance policy (SAA-068) |
| SAA-233 (C014) | JVR Sumika; §21 | register states listed | cidol 002_01 L138, L158; dear_026 L164–L174; cidol 000_03 L106–L119; 012_03 L254–L291; dear_037 L390–L468 | **S**: the ruby self-split answered by the Producer's 紫雲清夏《じぶん》; なんてね; 節穴; the pre-stage ritual; the address system | register | — |
| SAA-234 (C015) | §6 (a new P2 paragraph); CSL Sumika | P2 "coherent progression", not analysed | P2 before-audition-b-normal-01 L17–L41; final-failure-01 L19–L71; a-normal-03 L37–L39 | **S**: loud regret; discomfort at being watched; unspoken bodily strain ('あたしは、まだ踊れる'); state-scoped | P2 coverage | — |

### 4-10. CORE-Ume

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-139 (C013; R05 S) | §24 M-UME; CONT Ume | anchors are required but none are recorded | cidol 006_01 L134–L145; 006_02 L10–L11; 006_03 L56, L90; 017_01 L4; 017_02 L139; 018_03 L174; dear_028 L309–L348 | **S** (graded by R05): unique event reference (006_03 L90; the 017_01 caption) / explicit recall (006_02; 018_03; Dear 028 → CIDOL 009) / verbal echo; license a D-UME reading only for the first two grades | placement licence | **OA: yes** |
| SAA-235 (C012) | UME-C07; §5 | VERY HIGH on one P1 passage | P1 mid-normal-02 choice 3 L92–L144; mid-normal-04 L56; ending-normal-03 L87–L89; ending-normal-05 L61–L71; dear_033 L185 | **S**: label it choice 3 only; corroborate with Dear 033 L185; widen the coping repertoire | evidence route | — |
| SAA-238 (C016) | §21 (or a new §21.7); JVR Ume | the core omits Ume's own ordinary texture | cidol 009_02 L207–L227; dear_010 L34–L47; 017 L230–L238; 030 L29–L36; 007 L134–L264; 024 L650–L712 | **S**: inventory (forbidden-love manga; running when worried; Saki fan-club number; impressions; full-name self-announcement) | ordinary life | fold in HSCA-141 (6-A) |
| SAA-239 (C017) | §11; SIDE §2.1 | "elite athlete/professional parents" | dear_hume_021 L356–L403 (L396); 025 L333–L539; 026 L659–L775; 027 L467–L472; 034 L310–L358 | **R**: differentiate the mother (hero athlete, renowned trainer) from the father (company president; comically shaky standing; "value your enemies"); the Producer had a hand in the facility | family accuracy | ⚠ SIDE §2.1 with SAA-171; HSCA-145 (6-A) |

### 4-11. CORE-Misuzu

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-241 (C012) | source-identity ledger or PSL (Misuzu block); C10/C20 | the anomaly is unrecorded | live_hmsz_001_start-03-01 L1, L21–L24 | **S**: `name=佑芽` on hmsz-voiced lines is a probable copy error; attribute to Misuzu; add as live-level evidence | attribution | AV-D confirmation (Batch 5); SAA-291(b) |
| SAA-242 (C013) | XW RINHA-XW-064; AV queue | "0 Rinha messages; NO_RINHA_VOICE" | dear_hmsz_019 L101–L111, L142, L155 | **R**: "speaker label withheld; Rinha voice assets; identity left open in text"; queue for AV | classification | ⚠ the same row as SAA-117; the Rinha gate stays open |
| SAA-243 (C014) | SL1.1 refresh; §3; EVM SL1.1 | the refresh covers 018_01/03 only; R86's routing of 020 not executed | cidol 018_02 L71–L204; 020_02 L17–L194; 020_03 L161–L249 | **S**: CIDOL 020 appearance doubt and her "only complex" (referent open); 018_02 laziness as cover | counterweight to §3 | part of SAA-108(a) |
| SAA-244 (C016) | §25, §32 OPEN-MISUZU-05 | OPEN-05 says fixation costs may appear later | dear_hmsz_036 L324–L379 | **S**: cite the revenge-joy beat ("could become a habit") under OPEN-05 | open-item evidence | — |
| SAA-248 (C020) | §16, §28.3; RSL Misuzu–Producer | the Producer as the steering party | activity_001 L29–L94; activity_018-01 L8–L54; activity_009 L17–L80; P1 final-normal-03 L48–L68; final-normal-04 L84–L111 | **S**: the reverse direction: she reads and narrates his tactics, steers outings, and offers to co-author his "magic words" | bidirectionality | — |
| SAA-249 (C021) | §14 | "Misuzu loses to Sena", with no causal reading | dear_hmsz_021 L299–L310; 023 L255–L279 | **S**: the loss is framed through her chosen tunnel vision on Temari; her later concession | causal reading | ⚠ §14 hotspot |

### 4-12. CORE-Sena

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-251 (C008) | §26 (Tsubame); RS-II §5.4 | Tsubame "developed enough to exceed earlier expectations"; RS-II: rivalry fails when the rival is unreachable | dear_jsna_026 L84–L115; 025 L264–L294; dear_atbm_009 | **S**: Sena's view that Tsubame overtook her long ago and stalled by aiming at Sena; from Sena's side the target was set too low; the first-year selection failure | Sena-side voice | ⚠ RS-II §5.4/§5.5 with SAA-030, 093 |
| SAA-253 (C014) | CONT Juo Sena continuity map | communications "remain M-SENA" | cidol 021_01 L53–L63; dear_jsna_029 L317 | **S**: hard anchors (002_01 after Dear 011; 006_03 after 009; 015_02 replays 005; 017_01 quotes 008; 021_01 after 029–033; 赤裸々 sung in Dear 027); 003 and 011 unanchored | placement | — |
| SAA-254 (C015) | §40 | possessive exclusivity; Dear 037 as a "stylized agreement" | cidol 015_03 L63–L93; 016_03 L233; 003_03 L77–L90; dear_jsna_037 L435–L461 | **O**: an OPEN entry: the juniors read the bond as romantic, Sena deflects, and the closing contract is professional; no romance asserted | consistency | ⚠ §40 with SAA-026; romance policy |
| SAA-255 (C016) | §5, §31 | an existing ordinary-life list | activity_012 L5; activity_018-01 L32–L36; P1 ending-normal-01 L17; cidol 015_02 L20–L26 | **S**: commutes from home; tea in the council room; wants to drive; rooftop talks; cooking weakness (Tsubame's report); rationed self-pity | ordinary life | — |

### 4-13. CORE-Tsubame

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-257 (C013) | JVR Tsubame tables; §18 | six register tables | dear_atbm_019 L13, L20, L25; 004 L46; 024 L462; SL1.1 033 L697; 028 L236–L243 | **S**: the child register in the D019 flashback; the performed cute register; the address system (お前 vs 貴様; Kotone promoted to 貴様) | register | ⚠ same rows as SAA-262 |
| SAA-258 (C014) | §17; CSL Tsubame | §17 "ordinary self" list | P1 ending-normal-01 L99–L117; ending-normal-02 L35–L41; activity_010 L23–L48; activity_011 L17–L141; support 0098_02 L138 | **S**: loves cuteness as a spectator; academic first place as escapism; refuses the dorm to avoid Mao's orders; pre-performance routines; 父君/母君 | ordinary life | — |
| SAA-259 (C015) | §42 P2[TSUBAME] | a general P2 summary | P2 after-audition-final-normal-01 L44–L76 | **S**: P2 names inferiority as fuel ('無理だと思います', L44) and grows against '以前の私' | P2 witness | — |
| SAA-260 (C016) | Tsubame refresh, "Rivalry survives the title"; BRL BR-R86-HIF-RESULT | the P3 failure is called "the counterfactual control" | P3 final-failure-01 L15–L37 (L37); dear_037 L181 | **S**: add L37: in the loss state she judges she cannot be a hero; her hero self-evaluation depends on the outcome | omitted detail | — |
| SAA-263 (C019) | §13; TSB-032 | the hero ideal is "not generated by adult rivalry with Sena" | dear_atbm_019 L19–L39; 018 L182–L183; 008 L290–L307 | **S** (keep the claim): the childhood plan to become idols "together with Sena-chan"; the Producer first names the hero ideal and her inner voice then claims it | origin precision | — |

### 4-14. KANAE reading

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-152 (C002; R07 Q) | §Admission; §From taking the assessment; KANAE-R88-C01/C03 residual scope | "multiple sponsors and Kanae's own assent" | dear_hkne_001 L264–L282, L288–L310, L476–L488, L538, L547, L557; school_002 L43; D002 L192; D008 L332, L433–L445 | **S** (narrowed to one sentence): the Producer's pitch to Kanae used the dual-support frame and the masters' approval; quote D008 L440–L445; residual: China's origination of the transfer stays undisclosed to Kanae through D010 | knowledge state | ⚠ R88-C03 with SAA-103 |
| SAA-265 (C010) | §Other Produce and live objects (pstep paragraph); AV crosswalk R88-05 | staging "survives…" | pstep before-rest-01-hkne L1–L2; after-odekake-01-d-02 L1 | **S**: her rest variant uses the exterior of China's house; her outing ends on the school road; consistent with live-in status (H01 L623); AV-C | staging evidence | — |

### 4-15. Event readings

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-267 (C006) | CORE-Kotone (biographical facts); CSL Kotone; E001–005 §3.1 | the internal/external divide framed through Temari and Saki | event_012 main-02 L108–L117; event_005 main-02 L62–L95 | **S**: Kotone is internal-progression (L117); Tsubame dealt with her as a 中等部 student working without permission | biography | SAA-187 |
| SAA-268 (C007) | E006–012 §3.4, §10.4 | "Temari then tells China…" | event_007 main-04 L450–L496; event_011 main-01 L208–L215, L279–L290 | **R** (wording): the recognition is spoken but cut off by the blackout in E007; it is received in E011 L215 | marker precision | — |
| SAA-269 (C009) | E013–020 §1.2, §13.1, §17 Q8; CONT | E019 "likely after prior installments" | event_018 main-01 L179–L216; event_019 main-01 L96–L113 | **S** (E015 ∥ E018) + **O** (E019 relation, now with a locator; inference-labelled) | continuity | — |
| SAA-270 (C010) | E027/028/030 refresh (E028); E021+ §1.3; CONT | "before September intake" | event_024 main-02 L4, L175; event_028 main-01 L9, L35–L43; 028-03 L203–L214; 028-05 L522 | **S** (E024 → E028 are one festival) + **O** (the late-September vs "September exam" dating) | continuity | SAA-291(e) |
| SAA-271 (C011) | E021+ §2.1, §10; CSL Rinami | "reversible hospitality includes protective command" | event_022 main-03 L11–L32; event_021 main-01 L294–L316 | **S** (a boundary condition): Rinami does not command the feverish Mao to rest, because she shares the ambition | bounds a rule | — |
| SAA-272 (C012) | PSL LOC-HSCA-006A; E001–005 §3 AV requests and §14; AV queue L459 | the AV question framed as "voice ownership" | event_001 main-02 L334–L382 (voice command L342, actorId=ssmk) | **P** (attribution) + **R** (AV scope): cite the voice-command metadata; narrow the request to delivery, timing and Temari's reaction | AV hygiene | Batch 5-A |
| SAA-273 (C013) | E021+ §1.3, §8; PIX E029 row | "branch-gated" | event_029 main-01 L97–L124 (empty branch groups) | **P** (gating) + **R** (terminology note: continuity gating; E029-01 is choice-invariant) | terminology | — |

### 4-16. Support readings and the participant index

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-161 (C008; R08 Q) | S03c §26 | "she now has age-near family" | csprt-3-0075_02 L60–L117 (L108, em-tagged 家族); cidol-kcna-3-009_02 L122–L236 | **R** (qualified): note the emphasis; anchor on SL1.0 cidol 009_02, not SL1.1; Kanae's name stays inference; do not read Kotone's silence beyond AV-C staging | local cross-reference | — |
| SAA-276 (C010) | PIX Phase 5 support sections | reduced column sets | csprt-3-0011_01 L107; 3-0033_02 L141; 3-0041_03 L131, L141, L182; 3-0069_01 | **R**: backfill a "mentioned/referenced (named or unnamed)" column where an absent figure carries the scene | index completeness | SAA-158; fold in HSCA-147 (6-A) |

### 4-17. Continuity, U1 placement and source identity

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-283 (C020) | U1 placement doc §2.1, §2.4 | the opening is described as the Producer meeting Ume | unit_01-01_01 L128–L155 (voice hski-001..009); 04_25 L245–L304 | **S**: U1 is framed retrospectively by Saki's voice and her Prima Stella speech | frame | SAA-177; AV-C asset IDs |
| SAA-291 (C011) | source-identity and dedup ledger; CONT SL1.1 rows; a method note in `00_ANALYSIS_FRAMEWORKS` | anomalies unrecorded | unit_01-01_05 L13; live_hmsz start-03-01 L21–L24; kcna selection-failure L90–L98; event_024 main-02 L4; the corpus-wide {user} parenthesis count | **S/O**: an anomaly table: (a) duplicated '6話' title card; (b) `name=佑芽` on Misuzu lines; (c) hkne voice assets in China narration; (d) the parenthesised-{user} convention; (e) the E024/E028 dating tension | source hygiene | the framework method note is a framework edit, so get owner confirmation; SAA-241, 213, 270 |
| SAA-292 (C012) | CONT MAP §3.4; CONT | "no shared line explicitly says after N.I.A." | P2 hrnm after-audition-mid-failure-01 L33, L37 | **S** (supporting witness only): in P2[RINAMI] H.I.F. lies ahead after N.I.A.; the P2 → P3 bridge stays provisional | continuity | — |

### 4-18. Institutions and register

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-288 (C005) | JVR; NPC trainer rows and Kunio | SIDE says relation-specific register is needed | pevent_003 school_2-003 L50, L57; 1-003 L53, L64; 3-003 L20, L42; tutorial cmmn-01 L6–L39 | **S**: idiolects of the dance, vocal and visual trainers and the headmaster; none uses the Producer's name, unlike Asari | register | — |
| SAA-289 (C006) | INST (new AV-C staging rows) | no staging-level curriculum facts | produce_lesson star-da-fanservice-small-001 L1, L17, L40; sp-star-da-big-001 L2, L19; pstep before-rest-01-atbm L1 | **S** (tentative, AV-C labelled): P3 public "star" lessons; silent trainers; the P1 activity calendar; dorm-gate vs home rest staging | institutional texture | SAA-265 |

### 4-19. Kaya Rinha evidence matrix

| ID (cand.) | Target | Existing claim | Ev. | Change | Benefit | Deps · OA |
|---|---|---|---|---|---|---|
| SAA-290 (C010) | RMX §6.1 / C001; XW route note | no shift in public perception recorded | dear_hmsz_032 L190; dear_ttmr_004 L68 | **S**: "Rinha's one-woman unit" (Kei's heyday) later seen as Temari's one-man unit | frames Rinha's withdrawal | SAA-049, 085 |

---

## Batch 5 — AV escalation list for the existing Carbon queue, and the PR #600 AV-documentation item

**No audiovisual review was performed by the audit or by this drafter.** Direct listening and continuous-motion review remain 0 seconds. This batch lists what to hand to the existing Carbon observation queue. It changes no claim. The Rinha perceptual gate and Phase 7 stay gated.

### 5-A. Escalation list

**Escalation rules.**

- Add the rows as a new dated supplement in CARBON-OBS, after the handoff-versioning fix in 5-B, so that the supplement carries its own handoff ID and version.
- Add matching "claims under test" rows to CARBON-ADJ. This avoids repeating the scope mismatch of SAA-266.
- Cross-reference the rows from new dated sections of `GKM_AUDIOVISUAL_VERIFICATION_QUEUE.md`. Several character queue sections there are marked CLOSED (China, Sumika, Ume, Lilja, Rinami); add a new dated section rather than editing a closure.
- Freeze observations before opening adjudication, as CARBON-OBS instructs.
- For every textual finding listed below, the textual claim stands without AV. AV can only calibrate or extend it.

**Group A — questions that need AV to settle.** Primary findings are in bold.

| Finding | Object and lines | Question for the reviewer | Textual change it would complete |
|---|---|---|---|
| **SAA-213** · CMP06-C013 · P3 · AV_DEPENDENT · OA no | adv_pstory_003_kcna_selection-failure-01 L92–L98 (narration with voice sud_vo_…_hkne-001..003, actorId=kcna) | Is the documentary narration Kanae's voice? | If yes, record in the China P3 note (BRL China delta) and in the Kanae evidence that Kanae narrates China's failure documentary already under SL1.0. Related: SAA-291(c). |
| **SAA-246** · CMP11-C018 · P3 · AV_DEPENDENT · OA no | pevent_003_hmsz_activity_021 L31–L34 (anchor) and about 11 loci (per B11-0098); cidol 018_01 L250 | Render facial-all-unique-egao3 and compare it with egao1/egao2 | Test EVM-Misuzu C42 (polite register with menacing semantics) visually; route to `GKM_MISUZU_AUDIOVISUAL_BASELINE_AND_REQUESTS.md`. |
| SAA-117 + SAA-242 | dear_hmsz_019 L101–L108 (krnh-001..003); cidol-ttmr-3-009_01 L176 (krnh-001) | Is the "やさしい声" Rinha's present voice, or a memory or dream frame? What is the delivery of child Rinha's first words? (CMP18 AV-RINHA-Q1/Q2) | Diegetic presence for XW-064/XW-014 and RMX C058/C045. **Does not open or close the Rinha gate.** |
| SAA-241 | live_hmsz_001_start-03-01 L21–L24 | Confirm by ear that the `name=佑芽` lines are Misuzu's voice | Source-identity anomaly; Misuzu attribution. |
| SAA-221 | live_shro_001 start-04 / end-04 | Is the crowdless live-04 setting real (no crowd commands)? | Hiro BRL structure note. |
| SAA-177, SAA-283 | tutorial_first_cmmn-00 L110–L147; unit_01-01_01 L128–L155 (hski voice IDs); 04_25 L245–L304 | Confirm audibly that the credo and U1 opening narration are Saki's | Saki §15 / H-SAKI-03; U1 placement doc. |

**Group B — optional delivery or staging calibrations.** None is required for the textual change.

- **P1s:**
  - SAA-001: the comic versus serious valence of the Dear 022 outburst. The Mao AV baseline already inspected Dear 021–027. SAA-057's Kansai prosody is the same scene.
  - SAA-002: dear_shro_010 L199; dear_024 L197.
  - SAA-003: cidol-hrnm-3-002_02 L190; the pauses at dear_020 L419 and L436; the Producer's tears at dear_037 L65–L85; the facial staging on "ばか" at dear_009 L359–L364.
  - SAA-004: the Dear 032/036 tears and plain-register lines.
- **P2s:**
  - SAA-006: dear_ttmr_037 L441, L450.
  - SAA-009 (AV-C): the 013 flashback L59–L62; the 018 BGM change L138.
  - SAA-014: the D027 blush; the D037 condition-branch stills; D037 L332/L368; C022_02 L102.
  - SAA-026: AV-HYP-SENA-09 (Sena's defeat responses).
  - SAA-037: the dear_hski_033 inner monologue.
  - SAA-042: Rinha's denial at dear_ttmr_015, already in the Rinha AV queue.
  - SAA-052 / SAA-185: dear_fktn_037 L506–L541.
  - SAA-053: Kotone's performed dance and vocal quality. SAA-054: the cover lines.
  - SAA-067: how the danger promotion is realised.
  - SAA-068: the teases at cidol-shro 007_02 L91 and 018_02 L143.
  - SAA-071 (AV-C): the stills at dear_hrnm_010 L434–L435 and 037 L441–L442.
  - SAA-073: whether Rinami's singing reads as weak.
  - SAA-079: Ume's "refreshing" line and the comic refrain. SAA-082: the jealousy and attraction-coded beats. SAA-081: the AV addendum is already REVISE (integration).
  - SAA-087: AV-HYP-MISUZU-04 (register shifts). SAA-088 (AV-C): the Dear 037 moon stills.
  - SAA-089 (AV-C): the dear_jsna_034 L349–L363 hide=true flashback.
  - SAA-115: delivery of the results lines.
- **P3s:**
  - SAA-121: Rinha's face at dear_ttmr_016 L409–L419 (RINHA-C057 / Rinha AV P0-002).
  - SAA-128: the voiced inner lines at dear_hrnm_027 L376/L402.
  - SAA-162 (AV-C): U1 04_07 facial and BGM commands L345–L420, L760–L831.
  - SAA-187: flashback staging already present in A1.
  - SAA-189: the Producer's 俺 delivery. SAA-194: Mao's romance-coded valence. SAA-223: Rinami's mock-formal prosody.
  - SAA-265 (AV-C): Kanae's pstep asset identity. SAA-287 (AV-C): the Asari dream staging. SAA-289 (AV-C): the lesson and rest staging layer.

**Group C — narrow an existing queue item.**

- SAA-272: narrow the E001 request (E001–005 §3 AV P0 and §14; AV queue L459), and the CARBON-OBS question "Who appears to speak before the dub is disclosed?", from voice ownership to delivery, timing and Temari's reaction. The A1 voice command (event_001 main-02 L342, ssmk-018, actorId=ssmk) and Sumika's アテレコ admission already settle ownership.

**Group D — already queued; no new dependency.**

- SAA-030: event 021-05 is already AV P0.
- SAA-105: 012-02/-03/-05 are already AV P0.

(SAA-019 and SAA-076 carry a "None" AV note and are not escalated.)

### 5-B. PR #600 AV-documentation item (a separate documentation fix, not analysis)

These two findings concern files that PR #600 itself changed on 2026-11-15. They record documentation inconsistencies only; the Kanae rows themselves are accurate against A1.

**SAA-155 · CMP14-C011 · P3 · TRACEABILITY_GAP · R07 S · OA: yes**

- **Target:** CARBON-OBS (YAML handoff block; §Current scope limits); CARBON-ADJ (front matter).
- **Existing state:**
  - The YAML block still reads `handoff_id: GKM-AV-CARBON-20261112`, `handoff_version: "1"`, with an owner authorization for "candidate selection and packet preparation" as a `single_operation`. Meanwhile the front matter says `last_updated: '2026-11-15'` and a §Source Lock 1.2 Kanae section has been added.
  - §Current scope limits still says 35 rows.
  - CARBON-ADJ carries no handoff identity, so a reviewer cannot confirm the pairing.
- **Change (REVISE):**
  - Mark the 2026-11-15 change as a new handoff version (for example "2") or give the Kanae rows a supplement ID.
  - Record the 2026-11-15 release-delta operation and its authorization, with the producer and runtime given in the SL1.2 receipt.
  - State the current total (35 + 5 = 40 rows).
  - Put the same handoff ID and version in CARBON-ADJ.
  - R07 optional extras: name the SL1.2 manifest or delta in the locator-resolution sentence. The entrypoint's "35-row selection" sits in the **dated 2026-11-12 section**; keep that historical sentence and state the current count in the 2026-11-15 entry instead (CHANGE_INTEGRATION_CHECKLIST: preserve history).
- **Benefit:** a later Carbon reviewer can verify which selection and authorization a row belongs to.
- **Owner adjudication: yes.** The authorization record is the owner's.

**SAA-266 · CMP14-C012 · P3 · TRACEABILITY_GAP · — · OA: no**

- **Target:** CARBON-ADJ §Source Lock 1.2 — Kanae candidates (with the paired CARBON-OBS row).
- **Existing state:** CARBON-OBS row AV-HKNE-R88-04 covers "Stand-in, admission gift and mirror, commitment and sprint", including D005 L272–L355 (the gift) and L532–L613 (the night fantasy). The adjudication row tests a narrower set of claims.
- **Evidence:** adv_dear_hkne_004 L373–L485; D005 L272–L355, L389–L510, L532–L613; D008 L504–L541, L613–L722.
- **Change (REVISE):** either add KANAE-R88-C03 (China's gift) and the D005 fantasy layer to the adjudication's claims under test, or narrow the packet row to the scenes that have a claim under test.
- **Benefit:** packet and adjudication scopes match.

**Relation to the PR #600 review.** The unresolved P2 "versioning" review comment on PR #600's AV handoff was **not read**: the GitHub connector failed and no agent had web access (G-statement §2.7). Whether SAA-155 and SAA-266 match that comment is unverified. Recommendation: the PR #600 author compares them with the comment and, if they match, fixes both in PR #600 before it integrates. They are defects of PR #600's own supplement and documentation-only. If PR #600 integrates first, carry them into PR-1.

---

## Batch 6 — Historical audit (HSCA) items

### 6-A. HSCA findings that no comparator rediscovered, but which comparators checked and report as still holding

By this drafter's tally of all `hsca_reconciliation.jsonl` rows, **49 HSCA IDs** have only NOT_REDISCOVERED relations. Checkpoint 3 first reported 50 before ID normalization. Its erratum, after normalizing to `HSCA-\d{3}`, confirms **49** (20 P2, 29 P3), matching this tally. Per Checkpoint 3, the comparators checked the P2 items in A1. The P3 items were checked in A1, against Stage A anchors or against the snapshot, as marked below. **These are HSCA findings, not register findings.** They enter the canon only through the ordinary claim-revision route, citing the HSCA ID, as was done for HSCA-001–006 and 046 on 2026-11-12.

"Check" column: **A1** = re-checked in A1 by at least one comparator; **St.A** = consistent with A1-verified Stage A anchors; **Snap** = checked against the canonical snapshot only; **pl.** = plausible, not re-checked.

**6-A-1. Factual, speaker and locator items: co-land with Batch 0 in PR-1** (11)

| HSCA | Sev. (comparator view) | Target | Issue and evidence | Check | Change |
|---|---|---|---|---|---|
| 052 | P2 (CMP01: P3) | CORE-Saki §3.2.6 | the 'アイドルじゃない' line comes after the contest, in answer to Rinha's request, hedged; Rinha answers 'ふふ' (dear_hski_016 L125–L209) | A1 | **R** context; cross-reference RINHA-C009 |
| 097 | P2 (agree) | S03b §9 | 'なにもかも元通りになったわけじゃない' is Temari's line (`name=手毬`, csprt-3-0033_01 L114), not Misuzu's; Misuzu affirms 'しましたよ' (L109) | A1 ×3 | **R** speaker |
| 108 | P3 | E021+ §2.4; CSL | E021 labelled a REVISE of an "uninterrupted heroic rivalry" trait that the Tsubame core never claimed | pl. (CMP13 agrees) | **R** label to "qualify / origin datum", after checking the core |
| 115 | P3 | S02/S03 reading of support 3-0024 | only Saki predicts that Temari would help; parts 1 and 2 are out of order | pl. (CMP16 holds) | **R** stance, after checking A1 |
| 123 | P3 | S03c (about L511) | the fan-art submission belongs to 0074_01, not story_0071 | Snap | **R** locator |
| 128 | P3 | support reading (Saki) | the enrolment-reason claim is in 3-0003_02, not story_0023 | St.A | **R** locator |
| 130 | P3 | S03 reading of S0089 | vague provenance for the Event 005 main-04 vow | pl. | **R** provenance |
| 149 | P3 | CORE-Sena §30; SENA-C47 | the statement is in hmsz cidol 015_02 L125/L145, not Sena's CIDOL 016 | A1 | **R** locator |
| 157 | P3 | RS-I §12.2/§12.3 (L1532, L1547) | "Support Series 3" should read Series 2 for story_0036 and story_0042 | Snap | **R** locators (a small edit; ⚠ RS-I §12 hotspot) |
| 165 | P3 | JVR Hiro row | 瞬間最大風速 is the Producer's line (dear_shro_037 L113 {user}), not Hiro's register term | A1 | **R** speaker |
| 168 | P3 | S03c §15 | the injury link for 0064_03 is stated as text, but the scene summarises it off-page ('――そんな感じで') | St.A | **R** to inference |

**6-A-2. Additions and narrowings: co-land with the subject's Batch 2–4 edits in PR-3a/3b** (38)

| HSCA | Sev. (comparator view) | Target | Issue and evidence | Check | Change · co-land |
|---|---|---|---|---|---|
| 010 | P2 (CMP04: P3) | CORE-Mao §2.4; MAO-C08 | D-MAO Dear 020 self-account 'もともと、理想の王子様を演じるためにやっていたことだから' (L75, L90, L107) qualifies "already cool before any stage pose" | A1 | **R** · Mao cluster |
| 019 | P2 | CORE-Tsubame §22; RS-II §5.9 | after accepting retirement (D024), Tsubame binds Sena's career by a contest while distrusting her word (dear_atbm_027 L285, L290–L308, L385–L391, L424–L433) | A1 ×4 | **R** "frees choice, not outcome" · SAA-029 |
| 025 | P2 (CMP03: P3) | KOTO-C02; CORE-Kotone §4.3 | ownership of 成り上がる is partly produced by the Producer's endorsement (dear_fktn_001 L219 inner; 006 L199 self-cut, L262 'ヒきました？', L265 one-option) | A1 | **R** add a developmental qualifier |
| 028 | P2 (CMP15: P3) | E021+ §5.4; CORE-Misuzu §23; CORE-Sena §30 | contested ownership of ENDLESS DANCE (event_024 main-04 L368, L372; main-05 L410–L414) | A1 | **S/R** the "commons" framing |
| 038 | P2 (CMP08: P3) | RS-II §9.2 | Rinami absent from the Producer-node synthesis; the magician motif (dear_hrnm_022 L484; 027 L162; 037 L139) | A1 | **S** · ⚠ RS-II §9 coordinated edit |
| 040 | P2 | CORE-Rinami §8 | "Competitive ambition is new" vs the first-year vow with Mao (dear_hrnm_030 L350; P3 final-normal-02 L11) | A1 | **R** to "revived and re-licensed" · SAA-128 |
| 043 | P2 | SIDE §7.1 | Shiori's direct voice (dear_hrnm_021 L242, L254; 025 L121) | A1 | **S** |
| 044 | P2 | CORE-Rinami §6 governance; RINAMI-C25 | covert Producer interventions (dear_hrnm_037 L311: the 100 Pro offer concealed; P1 ending-normal-04 L50; 027 L34 inner) | A1 | **S** · SAA-003, SAA-224 |
| 045 | P2 (P3 ×3) | CORE-Saki §4.1 | Sumika on Saki's "lying to fight" (event_012 main-04 L738–L768) | A1 | **S** (Saki side) · SAA-105 |
| 060 | P2 | CORE-Ume; OPEN-UME-02/08 | Ume as reigning Prima Stella in D-SAKI 033 (L345, L451, L544) | A1 | **S** (C1 @ D-SAKI) |
| 067 | P2 (P3 ×2) | S02c §20; the Phase-6 warning | support 2-0071: concealed authorship, not "authority to decide for Kotone" (L71, L136, L140) | A1 | **R** (narrow) |
| 068 | P2 (CMP16: P3) | S02b §25; Sena–Tsubame RSL rows | Sena's deliberate superiority teasing (support 2-0049 L32, L44, L102; Tsubame L113) | A1 | **R** the "semantic mismatch" framing |
| 079 | P2 | RS-I §4.8, §4.11 | REVERSI role inversion between D-LILJA 032 and D-SUMIKA 033 (dear_ssmk_033 L81, L101–L191, L255; dear_kllj_032 L475) | A1 ×3 | **R** with track labels |
| 082 | P2 | CORE-Lilja §3 | the founding creed is a self-command sustained for the Producer (C010_02 L194–L217, isInner) | A1 | **R** |
| 083 | P2 (P2/P3) | RS-I §4.7; CORE-Sumika §15 | in D-SUMIKA, REVERSI publicity is the Producer's remedy for negative fan reaction to Lilja (dear_ssmk_029 L149–L239) | A1 ×2 | **S** (track-labelled) |
| 085 | P2 (P3/P2) | RS-II OPEN-RS2-05 (L1551–L1553); §4.4 | E014 answers the "limit" question (event_014 main-03 L300–L331, L459) | A1 ×2 | **R** (narrow the OPEN) |
| 086 | P2 (CMP07: P3) | CORE-Hiro §21 | the Producer's professional cost for choosing Hiro (Dear 010-01 L52–L63; 019 L49–L61; 031) | A1 (partial) | **S** locators · ⚠ §21 hotspot |
| 092 | P2 (P3 ×2) | CORE-Sumika (expectation thesis) | sequencing of support 3-0093_02 L23–L36 and 3-0108_03 L101–L200 ('戻った' is Tsubame's observer claim) | A1 (partial) | **S** (a bounded cross-reference) |
| 105 | P3 | MAO-C06 | the child Mao enjoyed being called cute; the cute-aversion comes after the rupture | St.A | **S** · SAA-056 |
| 109 | P3 | support reading 3-0038_01; PIX | the unvoiced 副会長 is identifiable as Tsubame (3-0046_01; 3-0015_02) | pl. (CMP16 holds) | **S** (inference-labelled) |
| 111 | P3 | CORE-Tsubame §17/§34 | an asymmetry of care: health enforced on juniors, her own minimised | St.A | **S** |
| 112 | P3 | TSB-040 counterpressure | Sena's half-conceded promise-keeping inference (dear_atbm_027 L385–L391) | A1 | **S** |
| 118 | P3 | E013–020; the Misuzu note | in E014 Misuzu twice names the motivated state as nostalgic | pl. (CMP15 holds) | **S** |
| 129 | P3 | S03b §11; CORE-Saki | Saki's side of support 3-0035 ('最高に嬉しくて――……悩ましい') | St.A | **S** |
| 131 | P3 | H-SAKI-05 (P-route note, C3) | in P-route failures, Saki negotiates grief witnessed by the Producer | St.A | **S** · ⚠ H-SAKI-05 |
| 136 | P3 | RS-II §3.3; CORE-Saki | Saki coaches Kotone's self-love in an older-sister register (C-FKTN 000_02) | St.A | **S** |
| 139 | P3 | S03d §23; CORE-Ume | Ume's worry about Saki's "everyone's big sister" stance (S0097-03) | St.A | **S** · SAA-082 |
| 141 | P3 | the CORE-Ume idiolect | full-name address to Saki at challenge peaks | St.A | fold into SAA-238 |
| 144 | P3 | UME-C06 counterpressure | Ume's retrospective account in D-MAO 031 | pl. | **S** · SAA-083 |
| 145 | P3 | SIDE §2.1; CORE-Ume | the Hanami facility serves rivals across tracks (D-SENA 014/025; D-SAKI 032) | pl. | **S** · SAA-239 |
| 147 | P3 | PIX | the imagined Kotone voice in support 2-0042 is indexed as participation | St.A | fold into SAA-276 |
| 156 | P3 | E006–012 §5.4 | the repair begins with Kotone standing in for Sumika ('ゴメンね♪――清夏じゃなくて') | St.A | **S** |
| 159 | P3 | XW (OTHER-REPORT) | an alumna in D-MAO 025 recalls a past Prima Stella named 賀陽 | St.A | **S** · the XW edit (SAA-117/158/165) |
| 169 | P3 | CORE-Sumika §1, proposition 2 | the trajectory of the trauma's status (Dear 010-01 knee; Dear 020) vs "deepest persistent barrier" | St.A | **R** (qualify) |
| 171 | P3 | BRL; CORE-Sumika | Sumika reaches for resignation in both P3 selection-failure fragments | St.A | **S** · SAA-134 |
| 172 | P3 | CORE-Sumika | her pre-injury self as a performance of invincibility ('思い込もうとしてた'; kllj dear_013 L241) | St.A | **S** |
| 174 | P3 | E006–012 §13.4; CSL | Temari's inner/outer split is self-monitored, not static (event_011 main-03 L320) | St.A | **S** · SAA-008 |
| 175 | P3 | S02a §3 | Kotone's inner lines in support 2-0001 contradict her spoken agreement | St.A | **S** · SAA-054 |

### 6-B. HSCA-001, the Begrazia arc: correction only partly adequate (missing Rinha-crosswalk routing)

The 2026-11-12 correction STRENGTHENED HSCA-001 (RS-I §5.9.1; Misuzu C26/C45; CSL/RSL rows; LOC-HSCA-001A–D). CMP02, CMP03 and CMP11 judged it adequate for their subjects. CMP17 judged it partly adequate overall, and **not** adequate on the Rinha-crosswalk routing. The residuals, with their vehicles:

1. **Rinha-crosswalk routing of U1 04_08 was not done.** Vehicle: **SAA-165 · CMP17-C013 · P3 · TRACEABILITY_GAP · R03 S · OA: yes.**
   - Target: XW Unit Story rows and counts. Today: "2 | 0 | 0 | SyngUp context only; no Rinha-name/direct row"; only XW-117 (04_13) and XW-118 (04_17).
   - Evidence: adv_unit_01-04_08 L178 (りんちゃん, in Misuzu's report that Rinha does not resent Temari); 01-01_11 L181–L182.
   - Change (REVISE): add 04_08 as an observer-report row. List 01_11 L181–L182 only as a possible but unestablished memory line of a SyngUp member (unvoiced ？？？). Neither supports any claim about Rinha's motive.
   - This also removes the internal inconsistency with RS-I §5.9.1. ⚠ Make it part of the single XW edit with SAA-117, 158, 242 and HSCA-159.
2. **Temari's belief that Misuzu resents her** (merged member ttmr-B-F02 (a)) → SAA-110 (Batch 2).
3. **Misuzu's possessive hostility toward Kotone.** The correction added only the 04_17 resolution row. → SAA-277 (Batch 2) adds the 01-02_07 precedent.
4. **The Temari side of U1 04_20** (her pre-verdict 'こういう私が好き') → SAA-046 (Batch 3).
5. **The U1 Ume ↔ Misuzu RSL row is missing.** CMP17 found no such row by grep (`hsca_reconciliation.jsonl`, CMP17 ALREADY_CORRECTED note). No register finding carries it; add it in the same RSL edit as item 2, or record it as an open residual.

Transition: PRESERVE the 2026-11-12 STRENGTHEN and complete the residual routing. Record in the dispositions crosswalk (§Closing) "HSCA-001 — STRENGTHENED 2026-11-12; residual routing completed <date> (SAA-110, 165, 277, 046)".

### 6-C. HSCA-005, Lilja and the prodigy charge: correction only partly adequate (legacy wording)

The 2026-11-12 correction (Sumika core §8 box and §23; SUMIKA-C07; RS-I §4.2/§4.12; RSL row 174) matches A1 (CMP09, CMP17). Two residuals remain:

1. **Legacy wording (CMP09).**
   - The LEG Phase-3 Sumika row still reads "this is Sumika's fear; Lilja rejects it".
   - Gain #3 of the Sumika core pass report still reads "expectation problem inside Sumika".
   - Both stand next to the new HSCA-005 row.
   - Change: in LEG, add an erratum cross-reference from the Phase-3 row to the 2026-11-12 HSCA-005 row. If the ledger's history model treats the Phase-3 row as historical, do not rewrite its text. If it is a current-state row, revise it and keep the earlier formulation recoverable.
   - For the pass report, a Phase-3 completion artifact, record an attributable erratum and do not edit its bytes (CHANGE_INTEGRATION_CHECKLIST, *Correcting analysis* §1). No owner flag is recorded for this; it is procedural.
2. **Bilateral concealment was not carried into RS-I §4.3/§4.13** (CMP05; merged member kllj-B-F01). Vehicle: **SAA-123 · CMP05-C002 · P3 · CROSS_REFERENCE_GAP · R05 Q · OA: no.**
   - Target: RS-I §4.3, §4.13 rules 1–2, §6.6; CORE-Lilja §10.2 (pointing to core §4) and §20.
   - Existing claim (RS-I §4.3): "Sumika's old care strategy is to protect Lilja by hiding weakness… Sumika stops treating reliance as betrayal… and Lilja stops accepting secrecy".
   - Evidence: dear_kllj_013 L162, L210–L241; dear_014 L81; C006_02 L57; C017_01 L111–L145; D033 L83–L126; C010_03 L189–L230 (isInner); D-SUMIKA 014 L344–L363.
   - Change (REVISE, narrowed by R05): one sentence plus cross-references.
     - (a) Keep D013 L162, D014 L81 and C006_02 L57 as Lilja's own concealment.
     - (b) Re-describe D033 L83–L126 as performed steadiness, directed at the Producer, which she discloses in the same scene.
     - (c) Route C010_03 L200–L230 to core §12.1, where the Producer conceals his fallibility and Lilja keeps the secret.
     - (d) Label D-SUMIKA 014 L344–L363 as a cross-track counter-charge about overwork, not proof of a mirrored concealment.
   - Notes: CMP05 had hsca_exposure. ⚠ RS-I §4.3 is also extended by SAA-105.

### 6-D. Still-open components of HSCA findings that were rediscovered

Recorded in CMP04's and CMP17's reconciliations. No register finding carries them; they are small factual fixes that suit PR-1.

- **HSCA-008:** the S03d paraphrase "remains physically present" (S3 076–102, L179) misstates 'ずっと憧れで、目標であり続けてくれる'. REVISE the wording.
- **HSCA-013:** the CORE-Mao §9.3 heading "institutional senior" (L672) mislabels a same-year classmate. REVISE the heading, together with SAA-058's §9 edit.
- **HSCA-102:** only partly open. Mao being an only child is already recorded; the E022 specifics and the height device are not (with SAA-196).
- **HSCA-059:** the Ume-side relational turn of D-UME Dear 022 remains open (CMP01). Carried by SAA-079.
- **HSCA-162:** the Worst Three attribution; "still present in baseline" (CMP17). Carried by SAA-127/136/280 (Batch 0).

---

## Closing — Recommended PR structure

### Repository position

- PR #600 is **open** on the continuing branch `series/gakuen-idolmaster`, at head `176d472a`. That head is the audit's baseline.
- A branch can carry only one open PR into `main`. Anything pushed to `series/gakuen-idolmaster` before PR #600 integrates therefore becomes part of PR #600.
- A temporary branch must not carry this analytical content (BRANCH_LIFECYCLE: "Do not route unrelated analytical content through a temporary branch").
- The local checkout's `series/gakuen-idolmaster` is at `cc671973`, which is an ancestor of `176d472a` and 496 commits behind it. Fetch and fast-forward before authoring; never edit from the stale checkout.

### Sequence

1. **PR #600, before it integrates: Batch 5-B only** (SAA-155, SAA-266), as a review-response commit, if the owner confirms it answers the unresolved AV-versioning comment. It is documentation-only and corrects PR #600's own supplement. Keep all analytical corrections out of PR #600, so that the SL1.2 tranche validates and integrates as a unit. The other edits to PR #600's own content (SAA-153, 154, 098–103, 152, 265) wait for PR-1 and PR-3b.
2. **After PR #600 integrates** (merge commit): merge current `main` into the series branch, starting from both current heads (*Stable analytical publication sequence*, step 5). Then publish the correction tranches **one at a time**, each waiting for its exact-head `Repository integration audit`:
   - **PR-1, "Source-to-analysis audit: factual and attribution corrections".** Contents:
     - Batch 0 (59 findings).
     - Batch 6-A-1 (11 HSCA items); 6-C(1) (HSCA-005 legacy erratum); 6-D (HSCA-008, 013, 102 components).
     - Batch 5-B, if it did not go into PR #600.
     - Optionally Batch 5-A, documentation only. It must follow the 5-B versioning fix.
     - The audit's registration in the entrypoint and ledgers (below).

     Two owner-flagged items can be limited: SAA-033 (land only the identity merge if the owner prefers) and SAA-147 (neutral wording only, pending an official credit).
   - **PR-2, "P1 integrations"** (Batch 1), after owner adjudication of all four findings, including the Misuzu severity dissent. It carries the cores, matrices, CSL/RSL rows and SIDE §3.1, plus SAA-057 (Mao §12.4, the same Dear 022 scene) and SAA-140 (Misuzu §7).

     **Defer the P1s' synthesis components** (SAA-001's RS-II §9.2/§9.5 entry; SAA-004's RS-I §5.9.2 and §12.3) to the coordinated synthesis edits in PR-3a and PR-3b. RS-I §5 and RS-II §9 are each targeted by about ten findings and should be edited once.
   - **PR-3a, the Hanami / REVERSI / SyngUp cluster:** Batches 2–4 and 6-A-2 for the Saki, Temari, Kotone, Lilja, Sumika, Ume and Misuzu cores; RS-I, edited once for §3.7, §4.3, §5 and §12.3; and the event and support readings they cite. This includes 6-B and 6-C(2).
   - **PR-3b, the third-year / 1-2 trio / institutions cluster:** Batches 2–4 and 6-A-2 for the Mao, China, Hiro, Rinami, Sena and Tsubame cores; KANAE; RS-II, with **one coordinated §9 edit** covering SAA-001, 014, 024, 044, 045, 058, 111, 114, 115, 237 and HSCA-038; and SPINE, SIDE, INST, NPC, CONT, XW and RMX. The XW edit covers SAA-117, 158, 165, 242 and HSCA-159 together.
   - **PR-4 (if 5-A was not in PR-1):** the Carbon supplement and AV-queue cross-references. Documentation only; no AV review.
3. **Owner decisions to take before PR-3:**
   - (a) The architecture question in 2-0 (SAA-104, 108; governs 048 and 113).
   - (b) One corpus policy on romance-coded material (SAA-068; governs 003, 014, 016, 082, 094, 185, 194, 231 and 254).
   - (c) The remaining owner-flagged items listed per entry, including SAA-158 (dissent from HSCA-119) and SAA-139.

   Unreviewed P2s should each pass the A1 re-read gate before they land.

### Integration discipline for every tranche (CHANGE_INTEGRATION_CHECKLIST.md)

- **Targeted edits only.**
  - Read each complete current file at a known commit.
  - Patch verified old text, and preserve everything else byte-for-byte: front matter, IDs, anchors, table columns, history, line endings.
  - Never regenerate a maintained document.
  - Review the complete diff and the size of each file.
  - Stage exact paths; never `git add .`.
  - Run author preflight `python tools/validate_repository.py --phase current --snapshot index --routing-preflight series/gakuen-idolmaster --repo .`, and in local clone mode `python tools/prepare_commit.py --base origin/main --write-generated` then `--check`.
  - Push without force.
  - Housekeeping owns the routing outputs; analysis authors do not edit the character or reconstruction files.
- **Claim revisions.**
  - Record every change through the PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN vocabulary, keeping claim IDs and earlier formulations recoverable.
  - Show the error with locators, counterevidence and remaining uncertainty, not a preference.
  - Keep reviewer dissent as dissent: SAA-004 severity; SAA-158 versus HSCA-119.
- **Frozen artifacts** are corrected by attributable erratum or superseding note, never by editing their bytes. This applies to phase completion and pass reports (SAA-042: the Temari pass report, finding 15; SAA-085: the Misuzu pass report, item 5; HSCA-005: the Sumika pass report, gain #3), to source-metrics JSON (SAA-225), to checksum manifests, to the HSCA register and coverage ledger, and to historical dated sections of the entrypoint (SAA-155's "35-row" sentence).
- **Blocked corrections** are recorded, not left as unqualified authority: SAA-147 (the credit), and the unverified side-claims of SAA-009, 011 and 151. Record them in the audit/current-state home.
- **Entrypoint and ledgers, by targeted edit.**
  - In `CURRENT_STATE_AND_CORPUS_MAP.md`, add a dated "First-read status" entry for this audit, marked non-authoritative like the 2026-11-08 HSCA entry, and a dated corrections entry per tranche, like the 2026-11-12 entry. Update `last_updated` in the front matter. Phase states and the Carbon/Rinha "Next operation" stay as they are, apart from a reference to the 5-A rows.
  - In `GKM_LEGACY_CLAIM_REVISION_LEDGER.md`, append a section "Source-to-analysis audit claim revisions — <date>" with one row per claim ID and transition, following the "Historical-source claim revisions — 2026-11-12" section.
  - Add `LOC-SAA-nnnX` locators to `GKM_PRIMARY_SOURCE_LOCATOR_LEDGER.md`.
  - Update CSL, RSL, JVR, BRL, CONT, NPC and INST rows under each ledger's own append or current-state rules.
  - Add a dispositions crosswalk in `01_CORPUS_AUDIT_AND_SOURCE_LOCK/`, modelled on `GKM_HISTORICAL_AUDIT_DISPOSITIONS_20261112.md`.
  - Whether to route the audit deliverables themselves into the repository as a non-authoritative folder, as was done for HSCA, is an owner decision, subject to `ARTIFACT_ELIGIBILITY.md` (not read by this drafter).
