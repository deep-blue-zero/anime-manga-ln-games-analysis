---
title: "FX Fighter Kurumi-chan — Source completion and longitudinal reconciliation (V01–V10)"
artifact_id: FX_KURUMI_SOURCE_COMPLETION_AND_LONGITUDINAL_RECONCILIATION
artifact_type: longitudinal_reconciliation_audit
series: fx-fighter-kurumi-chan
version: "1.2"
status: canonical
authority_generation: FX_KURUMI-INITIAL
authority_scope: "Gate G1 state reconciliation of the completed V01–V10 run: readiness record, exposure regime, state continuity, calculation provenance, claim, forecast and obligation history, ledger navigation, proposed corrections, and the claim transitions decided at G2 (FXK-SYN-C001–C006)"
source_boundary: "Accepted V01–V10 boundary (FXK-JP-V01-W01 to FXK-JP-V10-W01); V10 unit-end knowledge; no later volume"
created: 2026-11-23
last_updated: 2026-11-23
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
synthesis_id: FXK-SYN-20261123-V01-V10
snapshot_commit: bfeede591b04c2652e8cbbba14c1782e8a94f877
recommended_reasoning_class: DEEP_SYNTHESIS
---

# FX Fighter Kurumi-chan — Source completion and longitudinal reconciliation (V01–V10)

**Revision note (version 1.1, 2026-11-23).** Revised by the principal integrator at the G4 close-out of the synthesis (transfer FXK-SYN-T-G4-CLOSE) on findings carried by the [convergence audit](FX_KURUMI_V01_V10_CONVERGENCE.md) (K-22; section 8.5) and the [semantic validation audit](FX_KURUMI_V01_V10_SEMANTIC_VALIDATION.md) (section 9, items 3–5; section 11). K-22: section 4.1 no longer says that no threshold is printed in any volume, since the 2013 notice to Yasuko prints 「証拠金維持率が100%…」 (V10 i0076), and the same statement is corrected in the V01 U-06 row of section 7.1 (U-06 stays OPEN for Kurumi's and Mebuki's brokers); the domestic cap "証拠金25倍まで" is located at V01 i0075, not i0074, wherever this audit locates it (sections 4.1, 4.2, 4.11, 7.1 and 9 item 4). Section 4.10 gives Kizuna's share as 91.75% (10,011,927 ÷ 10,911,942, ANALYST CALCULATION). The navigation index (section 8.2) now covers rows FXK-SYN-C007 to FXK-SYN-C034 at their lines in ledger version 1.16. Nothing else changes: every other line number in section 8 is still that of the base file, and no argument, figure or disposition is altered.

**Revision note (version 1.2, 2026-11-23).** Two lines routed to the run coordinator by the G4 close-out ([semantic validation audit](FX_KURUMI_V01_V10_SEMANTIC_VALIDATION.md), section 11, items 6 and 10) are corrected by the coordinator: section 5.6 now says that only the V06 count matches the rule to the yen and the V05 count is round (ledger FXK-SYN-C033), and section 7.2, row V06-U12, records the door sign as the page prints it and the item as resolved. Nothing else changes.

This audit is gate G1 of the retrospective synthesis FXK-SYN-20261123-V01-V10: the completion audit of the run FXK-RUN-20261119-V01-V10, which read and accepted the ten collected volumes of **FX戦士くるみちゃん** (原作 でむにゃん, 作画 炭酸だいすき) one at a time. It reconciles state, evidence locators, calculation provenance and claim history across V01–V10; records the exposure regime, the forecast history and the open evidence obligations as the accepted records hold them; indexes the [decision and evidence ledger](../FX_KURUMI_DECISION_AND_EVIDENCE_LEDGER.md); lists the corrections it proposes for the coordinator to route; and argues the six claim transitions written in the G2 ledger transaction (section 5.6). The [architecture and role-gap audit](FX_KURUMI_ARCHITECTURE_ROLE_GAP_AUDIT.md) and the [character qualification](FX_KURUMI_CHARACTER_QUALIFICATION.md) complete gate G2; the [synthesis architecture](../FX_KURUMI_SYNTHESIS_ARCHITECTURE.md) records the gates.

- **Base snapshot.** Commit bfeede591b04c2652e8cbbba14c1782e8a94f877, branch `series/fx-fighter-kurumi-chan`.
- **Evidence boundary.** The accepted V01–V10 readings, checkpoints (with the [errata](../checkpoints/FX_KURUMI_CHECKPOINT_ERRATA.md)), entering states, the ledger and the [source register](../FX_KURUMI_SOURCE_REGISTER.md) at the base snapshot, and admitted pages re-opened to settle a load-bearing doubt (section 10). EXTERNAL_REFERENCE is excluded.
- **Labels.** OBSERVATION, SELF_REPORT, NARRATOR_PRESENTATION, INFERENCE, HYPOTHESIS, EVALUATION, UNRESOLVED; HIGH / MODERATE / LOW. "ANALYST CALCULATION" (CALC) marks arithmetic on printed operands, done in the readings or rechecked here.
- **How it was made.** The principal integrator wrote the reconciliation independently, then verified and integrated the financial specialist's and the character specialist's dossiers and the independent reviewer's diagnostics item by item (section 11), and answered the reviewer's challenges (section 13). No reading, checkpoint, entering state, erratum or register entry is edited by this audit; proposed corrections are listed for the coordinator (section 9).

Paths are relative to the project root `series/fx-fighter-kurumi-chan/`.

## 1. Readiness record (long-series protocol §6)

### 1.1 Base, entrypoint and authority

| Field | State at the base snapshot |
| --- | --- |
| Repository, branch, commit | `series/fx-fighter-kurumi-chan`, bfeede591b04c2652e8cbbba14c1782e8a94f877 |
| Canonical entrypoint | [`CURRENT_STATE_AND_CORPUS_MAP.md`](../CURRENT_STATE_AND_CORPUS_MAP.md) v1.13 (last_updated 2026-11-23): run FXK-RUN-20261119-V01-V10 `completed`, committed high-water mark V10 (terminal boundary), no next unit and no next permitted operation (both NONE), SEQUENTIAL_ANALYSIS_LOCK OPEN, supplemental lane `CLOSED_AWAITING_COMPONENT_ADMISSION`, other narrative admission NOT_AUTHORIZED |
| Synthesis authorization | FXK-SYN-20261123-V01-V10, by the owner's instruction of 2026-11-23 (entrypoint, "Authorized retrospective synthesis"). It admits no source. Gates G1–G5; current gate G1 at the base. Not authorized: character reconstruction, the historical-market concordance, supplemental components, any later volume. Release or freeze is the owner's decision. The synthesis also covers the resolution of the open review of PR #695 |
| Method and architecture | [`FX_KURUMI_ANALYTICAL_METHOD.md`](../FX_KURUMI_ANALYTICAL_METHOD.md) v1.0 and the architecture v1.0 (both 2026-11-15, unchanged by the run); the architecture's post-run text is "From volumes to synthesis" |
| Source register | v1.1 (last_updated 2026-11-22): run activation verification plus one coverage section per volume |
| Errata carrier | v1.1 (last_updated 2026-11-23): eleven errata of 2026-11-22 (FXK-ERR-V01-01 to FXK-ERR-V04-03) and two later corrections of 2026-11-23 (FXK-ERR-SUM-01, FXK-ERR-V07-01) |
| Ledger | v1.12 (last_updated 2026-11-23); 859,614 bytes and 3,438 lines at the base, 188,962 bytes under the 1,048,576-byte limit (ANALYST CALCULATION) |
| Integration owner | The principal integrator of FXK-SYN-20261123-V01-V10: sole writer of the synthesis audits, the shared ledger and the published synthesis (entrypoint, "Writers") |
| Publisher | The run coordinator: edits the entrypoint, validates, commits and publishes |
| Mandatory later stages | G2 role-gap review, person qualification and claim stabilization; G3 whole-boundary synthesis (specialist studies, convergence with a recorded full-series readiness check, integrated synthesis, qualified monographs); G4 semantic validation; G5 owner release or freeze (architecture, retrospective amendment) |

### 1.2 Source boundary and knowledge cutoff

- Authorized narrative: the Japanese commercial collected manga in the ten supplied EPUB witnesses FXK-JP-V01-W01 to FXK-JP-V10-W01 (register, "Run activation verification"). One edition per volume, as packaged; no edition comparison is in scope.
- Knowledge cutoff: the end of the V10 main narrative, i0156 (第50話, present time Monday 24 April 2017, evening; register V10 coverage; V10 checkpoint §11). Nothing after i0156 is narrative evidence; V10's post-main pages are classified extras or apparatus.
- Not evidence: the web original, the anime, translations, external summaries, real exchange-rate and market history, the real outcomes of depicted events, authorial paratext (afterwords, bonus essays, jackets, flaps, under-jacket boards, blurbs). Paratext is classified only.
- The boundary is "the V01–V10 collected-manga main narrative", not the full series: V10 ends 「TO BE CONTINUED...」 (i0156), and the forecasts facing events after V10 are frozen as NOT SCOREABLE IN THIS RUN (section 6.4).

### 1.3 Unit coverage and omissions

Every witness was verified as a package (ZIP CRC, one OPF, one raster per spine item, every image referenced, no repeated digest, 1,686 RGB occurrences decoded, right-to-left progression; register, "Run activation verification"). Two package lineages exist: a Kindle unpack at 1350×1920 (V01, V03, V04, V05) and a publisher package at 1441×2048 (V02, V06–V10). In every volume the printed folio equals the occurrence number minus 2, openings are (even | odd), and no missing, duplicated or out-of-order page was found (each register coverage section).

| Vol | Witness | Occ. | Main narrative (count) | Chapters | Colophon date | Apparatus / extras / advertising | Recorded legibility limits (not reconstructed) |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| V01 | FXK-JP-V01-W01 | 171 | i0003–i0162 (160) | 第1–5話; colour prologue i0003 with 「第1集 お祈り」 (its chapter membership unresolved, V01 U-05) | 2021-07-21 | 6 / 4 / 1 (i0165 reclassified as an extra, FXK-ERR-V01-03) | glitched tile i0141 |
| V02 | FXK-JP-V02-W01 | 171 | i0003–i0102, i0105–i0134, i0137–i0162 (156) | 第6–10話; no 「第N集」 strip | 2022-01-21 | 10 / 4 / 1 | glitched memory digits i0105–i0106; i0073 wall lettering; i0162 partial |
| V03 | FXK-JP-V03-W01 | 171 | i0003–i0162 (160) | 第11–15話; 「第3集 火柱」 i0003 | 2022-08-23 | 6 / 4 / 1 | glitched i0104 figure; partial i0037, i0162 |
| V04 | FXK-JP-V04-W01 | 163 | i0003–i0032, i0035–i0062, i0065–i0088, i0091–i0122, i0125–i0150 (140) | 第16–20話; 「第4集 博打」 | 2023-02-22 (package 2023-02-21) | 16 / 6 / 1 | IOU day cut 「2014年11[…]」 i0145 |
| V05 | FXK-JP-V05-W01 | 171 | i0003–i0054, i0057–i0162 (158) | 第21–25話; 「第5集 糸」; i0103–i0104 between 第23話 and 第24話 unresolved | 2023-07-22 | 9 / 3 / 1 | small collage and background fragments (i0070, i0074–i0075, i0105, i0124, i0126, i0153, i0162) |
| V06 | FXK-JP-V06-W01 | 163 | i0003–i0028, i0031–i0055, i0057–i0090, i0093–i0118, i0121–i0154 (145) | 第26–30話; 「第6集 必勝」 | 2024-03-23 | 13 / 4 / 1 | hidden digits 「−18,790,50[…]」 i0079; i0143 hidden reward text; i0158 colour status (V06-U16) |
| V07 | FXK-JP-V07-W01 | 163 | i0003–i0032, i0035–i0066, i0069–i0095, i0097–i0122, i0125–i0150 (141) | 第31–35話; 「第7集 1月15日」 | 2024-09-21 | 16 / 5 / 1 | i0125 overdrawn digit; i0066 middle kana; i0099 field 「201」; i0106 clock |
| V08 | FXK-JP-V08-W01 | 171 | i0003–i0026, i0029–i0060, i0063–i0092, i0095–i0126, i0129–i0158 (148) | 第36–40話; 「第8集 友達」 | 2025-05-22 | 16 / 6 / 1 | glitched strip i0130; partial i0056, i0089, i0152, i0154; six issue designations for five chapters (V08-U10) |
| V09 | FXK-JP-V09-W01 | 171 | i0003–i0044, i0047–i0098, i0101–i0130, i0133–i0158 (150) | 第41–45話; 「第9集 共生」 | 2026-01-22 | 12 / 8 / 1 | imagined bankbook i0029; decorative tiles i0130; printed masks i0104, i0136 |
| V10 | FXK-JP-V10-W01 | 171 | i0003–i0156 (154) | 第46–50話; 「第10集 株式取引」 | 2026-09-23 (package 2026-09-18) | 6 / 10 / 1 | i0113 axis unreadable at full resolution; partial i0052, i0092, i0137, i0140 |

ANALYST CALCULATION: main-narrative occurrences across V01–V10 total 1,512 of 1,686.

Classes of non-narrative material (register coverage sections): apparatus (covers, flaps, wraparound jackets, separators, colophons, and in some volumes the under-jacket boards); authorial extras (afterwords, bonus strips, tutorials and explainers, production diaries, design roughs, a storyboard excerpt, a pre-serialization sample in V10, and in other volumes the under-jacket boards); advertising (one vendor page per volume, excluded). No volume contains a next-volume preview or a blank occurrence. The register's class for under-jacket boards varies by volume (apparatus in V04, V07, V08; extras in V01–V03, V06, V09, V10; mixed in V05). Both classes are non-evidence, so the variance has no analytical consequence; it is recorded here, not corrected.

Known omissions and limits, classified (long-series §6):

| Omission or limit | Class | Consequence |
| --- | --- | --- |
| FXK-SO-005: edition bibliography beyond package metadata (printing, revision state); no publication date in the V02 and V06–V10 packages | Optional enrichment | None for the synthesis; stays OPEN in the register |
| Unreadable-by-design numerals (V01 i0141, V02 i0105–i0106, V03 i0104, V08 i0130) and the V10 i0113 axis | Bounded omission | Recorded, never reconstructed; no claim rests on them |
| Post-main pages of V09 and V10 classified from contact sheets | Bounded omission | Adequate for non-evidence material |
| Reading-copy opening times never logged by any role | Bounded omission | Exposure "first seen" times are lower bounds from file times (errata, "Evidence"); bears on forecast credit, not on content |
| Open evidence obligations (section 7) | Bounded omissions | None is answerable inside the boundary; each is carried with its status |
| Outcomes facing events after V10 (V10-U01 to U04, U14; the frozen beyond-V10 forecasts) | Bounded omissions at the boundary | Never resolved or speculated on (section 6.4) |

No material absence blocks the synthesis.

### 1.4 Current records and revision state

| Record | Versions at the base | Revision state |
| --- | --- | --- |
| Deep readings V01–V04 | 1.1 (2026-11-22) | Revision 1.1 carries the errata's consequences (i0165 removed from §D and §K of V01; exposure and scoring notes in V02–V04) |
| Deep readings V05, V06, V08, V09, V10 | 1.0 | V05's status note and §M were amended before acceptance (V05 checkpoint §2, "Amendment session") |
| Deep reading V07 | 1.1 (2026-11-23) | Evidentiary uses of the bonus essay moved to the page (FXK-ERR-V07-01; ledger FXK-V07-C032) |
| Checkpoints V01–V10 | 1.0 each, frozen | V01–V04 and V07 corrected only through the errata carrier; V05 §2 and §7 were amended before acceptance, not after freezing |
| Entering states V01–V10 | 1.0 each, frozen | — |
| Errata | 1.1 | Append-only; no erratum has been rewritten |
| Ledger | 1.12 | Mutable; D rows, claim and forecast history, person-level qualification |
| Register | 1.1 | Mutable; per-volume coverage |

### 1.5 Unresolved disagreements and limits carried into the synthesis

- Evidence obligations still open at V10 are consolidated in section 7. None is answerable inside this run (V10 checkpoint §5).
- Confidence disagreements preserved at V10 (V10 checkpoint §5): the +500 market-buy row as Nana's order (principal MODERATE, financial specialist LOW-MODERATE); whether Kizuna lives alone (not stated; the character specialist asserted it).
- Translation questions: none in scope; the corpus quotes Japanese and glosses it. Register-level uncertainties (for example Yasuko's kanji 私 in asides, V04-U10) are carried as obligations.
- Capability limits: still images only, no text layer; reading copies at 1280 px with crops; a 45-image budget per session; four-page contact sheets for reviewer triage (V01 checkpoint §2, "Remedy").
- Process limits that bound credit, not content: section 2.
- Disagreements among the synthesis roles, kept visible: for the V08 「すみませんでした」 sheet the reviewer leans toward a recalled image and this audit records that lean at INFERENCE MODERATE with the status UNRESOLVED; the financial specialist leans to reading (a) of the V07 parenthetical on parsimony without proposing a transition, and this audit likewise keeps it UNRESOLVED. The reviewer's earlier "refuted" for the outcome strand of FXK-V02-C002 was withdrawn in favour of the DOWNGRADE written as FXK-SYN-C004. Qualification and study disagreements are recorded in the G2 audits.

### 1.6 Intended artifacts and acceptance criteria

The artifact IDs, canonical paths, scopes, authors and acceptance criteria of the later stages are fixed in the role-gap audit: the three studies, the convergence audit with its full-series readiness check, and the integrated synthesis (sections 3.1–3.5), the eight intended monographs (section 6), and the gate table with what passing each gate means (section 5).

## 2. Exposure regime across the run, as recorded

### 2.1 Deferred covers, flaps and jackets

| Volumes | Who deferred the front cover, flap, wraparound and under-jacket images | Where recorded |
| --- | --- | --- |
| V01–V04 | Only the principal, until after its MAIN_EXIT freeze. The financial and character specialists opened the cover and flap first (their briefs said "every page in spine order") and the jacket images last; the reviewer saw the cover and flap on its first contact sheet (s01) | Errata §1 and its four volume tables; root cause: the entrypoint's component scope against role briefs that applied the deferral to the principal alone (errata §1, "Root cause") |
| V05 | Only the principal (same pattern), recorded in the V05 checkpoint itself by an amendment session on 2026-11-22 from 01:20, before acceptance | V05 checkpoint §7, "Deferred covers and jacket: first exposure and dispositions" |
| V06–V10 | Every role: the principal after MAIN_EXIT, the specialists after their last prospective freeze, the reviewer from a separate deferred contact sheet after its Stage 1 write-up | Entrypoint "Component scope"; each checkpoint §7; register coverage, "Occurrences reviewed" |

No volume has a next-volume preview, so no role was exposed to a later volume through apparatus (errata §1; register).

### 2.2 The errata's dispositions (V01–V04, and the two later corrections)

| Erratum | Transition | Disposition |
| --- | --- | --- |
| FXK-ERR-V01-01 | REVISE | V01 checkpoint §7 "covers opened only after the main-narrative exit freeze" holds for the principal only; the specialists opened i0001–i0002 first, the reviewer on s01 |
| FXK-ERR-V01-02 | PRESERVE | No V01 prospective item is qualified. The principal's FX-4 (FXK-V01-F048; disposed of as FXK-V02-F018, CONFIRMED at V02 i0147) keeps its credit; its only outside input was the owner's brief naming a "Yasuko". The financial specialist's B-F02-5 (FXK-V01-F061) credit is unchanged |
| FXK-ERR-V01-03 | REVISE | V01 i0165 「原作者あとがき」 is an authorial extra, not apparatus; it is not cited for any reading; register counts become apparatus 6, extras 4; V01 reading 1.1 removes it from §D and §K; ledger FXK-V01-C017 records the transition |
| FXK-ERR-V02-01 | STRENGTHEN | Adds the reviewer's sheets and the timing against freezes |
| FXK-ERR-V02-02 | DOWNGRADE | FXK-V02-F095 (B-F06a-8, Mebuki meets Kurumi in person, 0.6, CONFIRMED i0048): predictive credit QUALIFIED (page-based credit belongs to the principal's FXK-V02-F025). FXK-V02-F111 (B-F08a-7, Yasuko meets Kurumi, 0.4, CONFIRMED i0147): predictive credit NONE. Outcomes unchanged |
| FXK-ERR-V02-03 | PRESERVE | Every other V02 item and review judgment |
| FXK-ERR-V03-01 | STRENGTHEN | Timing; the principal's freeze kept distinct (entering state 17:52, before any V03 image) |
| FXK-ERR-V03-02 | PRESERVE | All 27 financial-specialist items FXK-V03-F099–F125: the flap's hint about Mebuki had been realized on the page (i0045, i0051) before the first freeze |
| FXK-ERR-V04-01 | STRENGTHEN | Timing |
| FXK-ERR-V04-02 | PRESERVE | All 73 financial-specialist items FXK-V04-F091–F163 |
| FXK-ERR-V04-03 | REVISE | B4-J01 (FXK-V04-F136: "Mochiko's 1,000,000 loan executed", 0.75) is literally NO (IOU 金 2,000,000 円也, i0145; deposit +2,000,000円, i0146). The financial specialist's V04 literal tally 27–46 of 73, Brier 0.20849; relaxed event-only 28–45, Brier 0.20164; a head-clause reading of B4-J10 (26–47, 0.20575) recorded and not adopted |
| FXK-ERR-SUM-01 | REVISE | Narrows errata §1: the financial specialist wrote V04 FREEZE_00 (18 items, FXK-V04-F091–F108) before any V04 image; only FREEZE_01–04 (55 items, F109–F163) followed the cover and flap |
| FXK-ERR-V07-01 | REVISE | V07 checkpoint §7 calls the afterword i0153 "apparatus"; it is an authorial extra (register V07 coverage). The financial specialist's F05 CLOSING followed i0153 and preceded i0154–i0157 and every deferred input; the item-by-item PRESERVE stands. Ledger FXK-V07-C032 aligned |

Not changed by any erratum: every observed outcome on the page, every principal forecast and its disposition, and V01's finding that the cover trio grouping is promotional (errata §1, "Not changed").

### 2.3 V05 dispositions (recorded in its own checkpoint)

- The financial specialist's twelve freeze items (FXK-V05-F111–F122) were all written after the cover and flap and before the jacket images; every credit is PRESERVE (V05 checkpoint §7).
- Reviewer Stage 1 judgments 3 and 10: their sentences linking Mochiko's past to her treatment of Mebuki were written after the blurb (i0166) and carry independent credit QUALIFIED; the observations stand and ledger FXK-V05-C061 does not depend on them.
- The amendment session re-scored every V05 forecast literally; six outcomes changed, none because of exposure: V04-MX-8 (FXK-V05-F023), F04-2 (F051), F04-13 (F062), F05-5 (F069), F05-8 (F072, NOT TRIGGERED), F07-6 (F087).

### 2.4 Page slips and other out-of-frontier events, with their qualified items

| Vol | Role | Event | Items affected and treatment |
| --- | --- | --- | --- |
| V01 | Principal | Three chapter-join slips disclosed inside the freezes (checkpoint §6.1): F01 written after i0051 (第2話 label, FX explainer, "約3カ月" caption), F02 after i0083–i0084 (第3話 label; −98,500 → −105,000 boxes), F03 after i0111 (第4話 label; the 3,811,600円 (+3,000,000入金) box). An unlogged i0137 crop at 02:07 on 11-21 was not relied on (checkpoint §2) | Items marked in the freezes (for example [i0051-EXPOSED]); dispositions in V01 reading §M.2. No V01 tally was computed, so no calibration set exists to exclude them from |
| V02 | Principal | F04-4 judged UNSCORABLE (reviewer C-12 of V02) | Principal freeze tally 27 / 14 / 2 / 1 exposed / 10 unscorable (V02 reading §M.3; ledger FXK-V02-F052) |
| V03 | Principal | F02's slip exposed only i0039, which no F02 item concerns | No item scored on exposed evidence (V03 reading §M.4) |
| V04 | Principal | F06 written after the separator i0089 (disclosed); four sessions over the image cap by one or two | No item affected (V04 reading §Q) |
| V05 | Principal | F04 written after opening i0083; F06 after opening i0103–i0105 | F04-4, F04-15, F06-1, F06-2, F06-4 exposure-sensitive and out of calibration, with V04-MX-4 (V05 checkpoint §7) |
| V05 | Financial specialist | F02 saved 10.7 s before crops were placed on i0141's captions | F02-4 (FXK-V05-F120) out of calibration, with F02-3 and F01-6 (F119, F116; real-history exposure) |
| V06 | Principal | No slip. F09 carries no exposure declaration although a private real-world association at i0108 preceded it; the declaration is first written in F10 | F09-4 EXPOSURE-SENSITIVE; F09-2 outcome CONFIRMED, credit QUALIFIED; MX06-1 credit qualified when resolved (V06 checkpoint §7–§8) |
| V07 | All | No slip; the financial specialist's F05 after the afterword i0153 (FXK-ERR-V07-01) | No credit qualified for out-of-frontier exposure (V07 checkpoint §8) |
| V08 | Principal | Structural slip: an inventory printout with byte sizes and digests for i0116–i0171 (session 4, about 07:57) | F05-1, F06-1, F06-2 QUALIFIED (outcomes CONFIRMED) and out of the primary calibration; F06-3 VOID FOR CALIBRATION (satisfied by i0120 before its freeze) |
| V09 | Principal | Opened i0067 (first page of 第43話) before the 第42話 boundary freeze | F03-2, -3, -4, -5, -6, -8, -9 QUALIFIED, POST-SLIP, out of the primary calibration (outcomes kept) |
| V09 | Financial specialist | F02 CLOSING written after the writer's afterword i0164–i0165 (reviewer C-06 of V09) | F02-1, -16, -17, -18 EXPOSURE-SENSITIVE (paratext); F02-5, -12 QUALIFIED (V09 checkpoint §7–§8; V10 checkpoint §8) |
| V10 | Principal | Opened i0029 (first page of 第47話) before the 第46話 boundary freeze, and i0129 (first page of 第50話) before the 第49話 freeze | F01-2, -3, -9, -10 QUALIFIED; F02-4, F03-2, F03-3 carry the POST-SLIP note; F04-4, -5, -6 QUALIFIED; all out of the primary calibration |
| V10 | Financial specialist | A read-only search of the repository's checkpoints folder; F_CLOSE after i0157–i0158 (disclosed) | F01 and F02 keep full credit (V10 checkpoint §7–§8) |

Declared real-world knowledge (EXTERNAL_REFERENCE, excluded) produced EXPOSURE-SENSITIVE (ES) flags in every volume from V05 on; ES items are excluded from calibration as frozen (each checkpoint §7 and §8).

### 2.5 Image-cap overruns (disclosed; no evidential harm found)

V02 financial specialist session 4 (47); V04 principal sessions 2 and 4 (46 each), financial specialist session 4 (47), character specialist session 3 (47); V09 financial specialist session 1 (47); V10 financial specialist sessions 2 and 4 (46 each), character specialist sessions 1 (46) and 3 (49). No other session exceeded 45 (each checkpoint §2 and §7).

### 2.6 Harness write refusals and the coordinator's verbatim transcriptions

| Vol | What was refused | Route taken |
| --- | --- | --- |
| V02 | Both specialists' findings files (the subagent file-writing tool refused them as report files) | Written by shell append by the roles themselves; both say so (V02 checkpoint §2) |
| V03 | The financial specialist's findings file | Assembled by shell; recorded by the specialist (V03 checkpoint §2) |
| V08 | Both specialists' findings files | No workaround (the financial specialist's one shell attempt was refused by the permission layer); each returned its text; the coordinator copied it verbatim into the role's folder with a note naming the source session. The principal reconciled against the transcriptions (V08 checkpoint §2) |
| V09 | Both specialists' findings files | The coordinator's verbatim copy at 11:31:32; the reading and rows predate it (V09 checkpoint §2) |
| V10 | Both specialists' findings files | The coordinator's verbatim copy (file times 14:06); the reading and rows predate it (V10 checkpoint §2) |

INFERENCE (HIGH): the V02–V03 shell routes predate the run's later rule that a refused write is not worked around; from V08 the coordinator's transcription is the recorded route. No analytical claim depends on the route.

### 2.7 Other execution facts that bound what sessions could see

- V01: the first launch (2026-11-19 21:20) failed on a 30 MB request limit at about 21:23; the partial work was archived unopened and never used. Quota failures and compute restarts interrupted V01 on 11-19, 11-20 and 11-21. The run was handed to a Claude Code coordinator on 2026-11-21 at 13:50 (V01 checkpoint §2; entrypoint "Execution profile").
- V01: the principal ran one read-only repository diff command by mistake; no repository state changed (V01 checkpoint §2).
- V06: a line-ending fault in the first write of the ledger and the reading was corrected before read-back (V06 checkpoint §2).
- Structural metadata (spine identifiers, colour lists, raster sizes) was visible to every role before its first page in every volume; byte-size printouts were seen incidentally in V03, V04, V05 and V08 and used to judge a boundary only in the V08 slip above.

## 3. State continuity: entering states against the previous exit freeze

### 3.1 Method

For each n = 02…10 the "Known states entering Vnn" and "Open questions carried into Vnn" sections of `checkpoints/FX_KURUMI_Vnn_ENTERING_STATE.md` were read side by side with §P of the V(n−1) reading at the base snapshot. Every figure in both texts was checked against the other, and the load-bearing arithmetic was redone on the printed operands (ANALYST CALCULATION). The V01–V04 readings (version 1.1, 2026-11-22) and the V07 reading (version 1.1, 2026-11-23) were revised after the next entering state was frozen; their revision notes concern exposure records (§Q, §M.9, status notes) and one reclassification, not §P, so each entering state was frozen against the §P text that stands today.

Disposition vocabulary: AGREE (no difference in substance); ES WIDER (the entering state adds accepted material from the reading body, §F, §H, §I or the checkpoint exit state, which it cites); ES LABEL (the entering state adds an interpretation not marked as such); LATER CORRECTION (a later accepted record corrects a statement the frozen entering state carries; the frozen file stays unedited by rule).

### 3.2 Finding

No entering state contradicts the previous exit freeze on a position, a balance, a date, a name or an open question. Every entering state is wider than the §P it cites, because by design it also draws on the reading's synopsis, §F, §H and §I and on the checkpoint's exit state, and each says so in its opening line. The arithmetic chains that link the two records close exactly (section 3.3). One statement carried by two frozen entering states and one reading section was later corrected by an accepted claim (Kurumi's university year), and one entering state carries forward a V03 inference that a printed figure is a transposition, which V04's own evidence then contradicts (Mochiko's average). Neither has a downstream effect on a later accepted reading.

### 3.3 Pair by pair

| Pair | Disposition | Detail (locators) |
|---|---|---|
| V01 §P → V02 ES | AGREE; ES WIDER | Balance 5,123,110 (V01 i0157, i0162), the father's 3,000,000 not yet returned, own share 2,123,110 (CALC, from 300,000) agree. The ES adds the AUD/JPY 300枚 average 94.434 closed at 94.872 for +1,311,510 and "about 59× on 50枚 by the narrator's own figure" from the reading body. Its open questions omit four minor V01 carry-overs that §P lists (the 2011年10月 calendar prop, the i0141 digits, the papers in the LOSER panel, the inconsistent home exterior); the V01 checkpoint §5 carries them, so nothing was lost. The ES calls Kurumi "a second-year student" at the end of May 2014: see 3.4 (a) |
| V02 §P → V03 ES | AGREE; ES WIDER | Balances of 15 July 2014 (V02 i0158–i0159): Kurumi 2,656,690 (+556,690 on 2,100,000, CALC), Mochiko 12,014,110, Yasuko 76,573, Mebuki 613,200 (+413,200 on 200,000) agree. Mebuki "20, 大学三年生" is the verified caption (V02 i0004; FXK-V02-C015 reads "先輩" as investment seniority). The father's last present-time scene (V02 i0038) lies inside 第6話 (i0003–i0040), as the ES says. The ES again carries "second-year" for Kurumi: 3.4 (a) |
| V03 §P → V04 ES | AGREE; ES WIDER; one ES LABEL | Mebuki 800,000 = 600,000 tuition + two months' living money of 100,000; short 20枚 at 106.632, last open −258,100; equity ≈266,400 at 109.3 and ≈46,400 at 110.4 (CALC, unprinted) agree. Kurumi 3,611,715 after the 1,000,000 withdrawal; 60枚 long at 106.789, +456,600 open; Mochiko 13,302,630, 50枚 long, +359,000 open; Yasuko 71,052 agree. Yasuko's 76,573 → 71,052 = −5,521, which equals her shown −2,892 plus the off-page −2,629 the ES names (CALC). The ES describes the second printed average 106.382 as "a transposition", following the V03 reading's §F.6 item 2: 3.4 (b) |
| V04 §P → V05 ES | AGREE; ES WIDER | Mebuki 2,600,000 (+2,000,000入金, V04 i0146), borrowed ≈300,000 on cards + 300,000 student loan + 2,000,000 from Mochiko at 109.5%; last open −543,600 (i0068), ≈−747,600 at 115.840 (CALC) agree. "1,000,000 of deposits lost in two forced closes" (§P, i0139) counts deposits (200,000 in V02 + 800,000 in V03), not balances (the 13 August balance was 695,100); the ES keeps the same sense. Kurumi's 180枚 average 110.271 = (60 × 106.789 + 120 × 112.012) / 180, and +7,812,000 = (114.611 − 110.271) × 1,800,000 (CALC) agree with §P (i0112). Mochiko's +4,729,000 at 115.840 is exact for 106.382 on 50枚 (CALC). Interest ≈180,000 a month plus ≈4,200 = ≈184,200 (ES open question 3) agrees |
| V05 §P → V06 ES | AGREE; ES WIDER | Kurumi 3,611,715 + 17,602,200 = 21,213,915 (V05 i0152); (120.05 − 110.271) × 1,800,000 = 17,602,200; the 300枚 short at 119.631 with a take-profit at 118.6 would pay 3,093,000; the "あと300万円" gap = 25,000,000 − 21,213,915 − 1,000,000 = 2,786,085 (all CALC, matching the ES). Mebuki 2,621,530 (i0085), −1,002,120 open (i0091), 43 lots averaging 114.5805, zero equity ≈120.677 agree. Kurumi "21; a third-year of the 2012 intake" now appears in both records (FXK-V05-C064). The ES adds the volume's out-of-sequence caption "2014年10月下旬", kept as printed |
| V06 §P → V07 ES | AGREE; ES WIDER | Kurumi 21,213,915 − 1,743,000 − 1,131,000 = 18,339,915 (V06 i0013, i0046, i0095); "あと566万…とんで85円" = 25,000,000 − 18,339,915 − 1,000,000 = 5,660,085; Mochiko 13,302,630 + 7,691,000 = 20,993,630 (i0052); implied contest standings Kurumi ≥ +628% and Mochiko +74.7% (all CALC) agree. Mebuki's liquidation box −2,610,530 (i0039) against the V05 balance 2,621,530 leaves 11,000, which the ES records as a gap kept as printed. The ES adds Kozue's 2008 figures (forced liquidation "1900万円", a 400× short, the journal ending 23 October 2008) from the V06 body |
| V07 §P → V08 ES | AGREE; ES WIDER | Box −101,534,644 (−120,284,479) (V07 i0118), the e-mail's 不足金 at 16 January 05:00, due 19 January 15:00, then 14.6% a year (i0130) agree; the parenthetical less the balance = 18,749,835 (CALC; reference unstated, V07-U01). Bank 1,005,144 (i0144) agrees. Mebuki's contest figure −3,400,000 with "654.4%減" fits a 613,200 base: (−3,400,000 − 613,200) / 613,200 = −654.47% (CALC; the printed figure truncates). Mochiko's ≈1億2千万 estimate lies within 0.24% of the parenthetical (120,000,000 against 120,284,479) |
| V08 §P → V09 ES | AGREE; ES WIDER | Overseas account 1,000,000 + 1,545,501 + 1,973,674 = 4,519,175 (V08 i0012), then 0円 (i0020) agree. Tax ≈3,807,983 (i0034), 予納金 "150万" (i0034) agree. The ES's "late damages about 4万 a day" matches 101,534,644 × 14.6% / 365 ≈ 40,614 (CALC). Both records keep the method-free recording practice |
| V09 §P → V10 ES | AGREE; ES WIDER | Bankruptcy and discharge (V09 i0104, i0123), the father's 300万 offer and acceptance (i0074–i0075), the lawyer (i0098), father-managed wages (i0107), Kurumi 【事務員】 (i0152), new staff and ages agree. Small wording difference: §P says the tax instalments "were being arranged" with the municipal office in autumn 2015 (i0106); the ES says the tax "was being paid in instalments". The V09 synopsis (i0106–i0107, "地道に") supports payment under way; no substantive conflict. FXK-V07-C075 and FXK-V09-C075 are distinct rows, both cited correctly |

### 3.4 Items needing a disposition

(a) **Kurumi's university year (LATER CORRECTION).** The V02 entering state ("a second-year student at 新都大学", end of May 2014), the V03 entering state ("20, second-year at 新都大学", July 2014) and the V02 reading's §B carry "second-year" for dates after April 2014. The V01 caption "福賀くるみ(20)【大学二年生】" is dated 14 February 2014 (V01 i0040); the 平成24年度 orientation (V05 i0042–i0044) makes her a 2012 entrant, so she is a third-year from April 2014 and 21 by November 2014. Resolved at the V05 reconciliation by FXK-V05-C064 (with FXK-V05-C046, the transition of FXK-V04-C025; V04-U03 RESOLVED). The "TENSION" lines inside the V05 checkpoint §6 belong to principal freeze files reproduced verbatim and are not a defect. Route: none beyond the existing claim; later prose uses C064 (section 9 item 1).

(b) **Mochiko's average, 106.832 or 106.382 (ES LABEL from an accepted V03 inference later contradicted).** The V04 entering state calls the second printing (V03 i0154) "a transposition", following the V03 reading's cross-check (§F.6 item 2, MODERATE-HIGH): in late October Kurumi's tile (+456,600 on 60枚 from 106.789) and Mochiko's (+359,000 on 50枚) both imply 107.550 only if Mochiko's average is 106.832 (V03 i0148, i0154–i0155). The next volume points the other way: Mochiko's "数日後" profit of +4,729,000 at 115.840 (V04 i0144) is exact for 106.382 on 50枚 (V04 §P; CALC). Each printed average is consistent with one printed tile and inconsistent with the other (V04 i0037 still fits 106.832). FXK-V03-C020 ("Mochiko's average is 106.832, not 106.382") was DOWNGRADED from MODERATE-HIGH to MODERATE by FXK-V04-C038; V04-U01 keeps both values, and the V05–V07 entering states print both without the label. Route: none; the ledger carries the transition. The synthesis keeps both values and V04-U01 OPEN, and never repeats "transposition" as settled.

(c) **Wording drift without consequence.** The V03 ES "two months' scholarship living money of 100,000 each" against V03 §P "200,000 scholarship living money" (same sum); the V10 ES "being paid" against V09 §P "being arranged". Both AGREE in substance.

(d) **Carried open questions.** Every §P list of open questions reappears in the next entering state, usually reworded and expanded with obligation IDs; the only omissions are the four minor V01 items noted in the first row, which the V01 checkpoint carries.

## 4. Calculation provenance

Sources: each reading's §F (position tables, "Analyst cross-checks", "Internal inconsistencies and unresolved values (kept as printed)") and the ledger's analyst-arithmetic episode rows (FXK-V01-D031, V02-D031, V03-D035, V04-D022, V05-D031, V06-D031, V07-D033, V08-D031, V09-D033, V10-D035). Provenance classes as the readings use them: BOX (narrator-style account caption), TILE / SCR (on-screen display), SP / TH (speech / thought; a self-report), CAP / NP (narrator caption), DOC (document drawn on the page), CHART (drawn chart: illustrative unless a reading says otherwise), CALC (analyst calculation on printed operands). Every CALC below was rechecked on the printed operands; "conditional" marks a CALC that also needs an unprinted convention or an assumption of no unshown flows.

### 4.1 Conventions the whole run relies on

- **Lot unit.** 1枚 = 10,000 currency units, derived in V01 from Kurumi's "10枚… 1円動けば 10万円" (V01 i0047) and the narrator's "50枚 = … 500,000$(数量)" (i0074), then confirmed exactly by tiles wherever operands are printed (V04 i0057, i0112; V05 and V06 tiles; V08 per-lot gains). It is never assumed for Kozue's 2008 account (V06 §F.7) and is not established for Kizuna's EUR/USD 30枚 or Yasuko's 2013 3枚 (V10 §F.8).
- **Broker rules.** No stop-out level or margin-maintenance threshold is printed for any account but one: the 2013 notice to Yasuko prints 「証拠金維持率が100%…」 (V10 i0076); for Kurumi's and Mebuki's brokers none is printed (V01 U-06, OPEN at V10). The V01 overseas account's margin rate is fixed at 1:500 by calculation from a remembered screen (V02 i0107; V02 §F.4). A domestic cap "証拠金25倍まで" is printed in V01 (i0075) and again for Yasuko's account (V03 i0007, "約17倍" against CALC 17.89×). Forced liquidation is printed as an event (V03 and V06 Mebuki; V06 Kozue; V07 and V08 Kurumi; V10 Yasuko's 2013 flashback), and with a threshold only in that 2013 notice. Yasuko's app screen of V04 i0047 reads 残高 71,052円, クレジット 0円, 有効証拠金 71,052円, 証拠金 0円, 余剰証拠金 71,052円, 証拠金維持率(%) 0円 (OBSERVATION HIGH on three independent crops, the last made for this audit); that the ratio row shows a mock-screen convention for a flat account, not a stop-out level, is INFERENCE, and U-06 stays OPEN.
- **Percentages.** Every printed contest percentage is truncated, not rounded, to one decimal (73.59 → 73.5, V03 i0092; 7.21, 74.74, 643.40, 654.47 → 7.2, 74.7, 643.4, 654.4, V07 i0011–i0020; V07 §F.9). Mebuki's 654.4% fits only truncation.
- **Charts.** Drawn charts are illustrative, not price records, throughout, on internal evidence: a daily chart whose 10/15 low disagrees with the intraday rate a tile implies (V03 §F.7), irregular axis sequences (V06 §F, "schematic; not relied on"), odd and glitched grid values (V07 §F, i0125). The V05 reading also cited the V05 bonus strip (i0165, paratext) for "printed P/L excludes swap" and "short-term charts are altered for drama"; that basis is withdrawn by FXK-SYN-C003 (section 5.6), and the convention stands on the internal evidence alone.

### 4.2 Chain A — Kurumi's capital, positions and debt (V01–V10)

| Point | Figure as printed (provenance) | Locator | Reconciliation (CALC) / accepted ID |
|---|---|---|---|
| 14 Feb 2014 | balance 300,000 (BOX), own savings | V01 i0044 | start of the run's money chain |
| first trade | +24,200 (BOX; a second box prints +24,000) | V01 i0049–i0050 | 0.242 × 100,000 = 24,200; the +24,000 kept as printed |
| May 2014 | 811,600 (BOX, SCR) | V01 i0056, i0067 | streak "累計50万円以上"; tags sum 171,660 (FXK-V01-D010) |
| Day D–D+5 | AUD/JPY 50枚 long at 95.610; −629,000 at ≈94.352 (BOX) | V01 i0068, i0102 | zero equity on her own money ≈93.987 (CALC) |
| D+5 | +3,000,000 deposit (BOX "(+3,000,000入金)"), the father's タンス預金 taken without consent | V01 i0109–i0111 | balance 3,811,600 |
| D+5 night | adds +100枚 at 94.312 and +150枚 at 94.125 → 300枚, average 94.434 (BOX, truncated display) | V01 i0123, i0127 | exact basis 94.43483; P/L(p) = 3,000,000·p − 283,304,500 |
| nadir | −3,251,490 at 93.351 (SCR, BOX) = the cold-open figure | V01 i0137, i0003 | every displayed 300-lot value equals the formula +10円 (FXK-V01-C013, OPEN; U-04); the residue ties i0003 to this night (FXK-V01-C001) |
| close | +1,311,510 at 94.872 → 5,123,110 (BOX, SCR) | V01 i0157, i0162 | 3,811,600 + 1,311,510 ✓; by lot −369,000 / +560,000 / +1,120,500, so the 150枚 add made ≈85% of the profit and the first 50枚 lost (FXK-V01-C014, E043); "+43.8pips" × 3,000,000 ≠ 1,311,510 because the pips use the truncated average |
| own share | 2,123,110 | — | 811,600 + 1,311,510 (CALC; accepted) |
| V02 | the 3,000,000 returns to the father at discovery | V02 i0024–i0026 | U-07 resolved |
| V02 | domestic account funded 2,100,000 (BOX "(210万円入金)"); an unlabelled account at 0円 (BOX, twice) | V02 i0102; i0062, i0101 | 2,123,110 − 2,100,000 = **23,110 unaccounted** (V02-U07, OPEN at V10); the 0円 account is the V01 overseas one by INFERENCE MODERATE at most |
| 30 Jun / 15 Jul 2014 | open +40,550; balance 2,656,690 (BOX) | V02 i0129, i0158 | +556,690 on 2,100,000 if no unshown flows (CALC); no Kurumi pair, size, entry or stop is printed in V02 |
| V03 | 9/1 balance 3,049,015; USD/JPY 30枚 long from 104.221 closed for +1,562,700 → 4,611,715; 1,000,000 withdrawn "税金分" → 3,611,715 (BOX) | V03 i0056, i0092, i0124 | 15 July → 1 September: +392,325 or +329,025 depending on whether the 9/1 box includes open P/L (V03 §F.6 item 7); ≈109.43 at the 9/19 meeting from two independent tiles (FXK-V03-D035); Mebuki's "43万円" for Kurumi's July EUR/USD trade cannot be reconciled exactly (flows and other trades unshown) |
| late Oct 2014 | 60枚 long at 106.789, +456,600 open (TILE) | V03 i0154 | implies 107.550 |
| 31 Oct–5 Nov | +120枚 at 112.012 → 180枚, average 110.271; +7,812,000 open at 114.611 (BOX) | V04 i0006, i0112 | (60 × 106.789 + 120 × 112.012) / 180 = 110.2710 ✓; 1,800,000 × 4.340 = 7,812,000 ✓ (FXK-V04-D022); effective ≈29.9× at the add against the 25× cap printed in V01 i0075 and V03 i0007: a tension, not a proven contradiction (V04-U02) |
| 17 Nov | open +10,695,600 (TILE); stop at 115.4 and limit at 120.05 ordered (SP, DIAG) | V05 i0073, i0077, i0080 | implies 116.213 |
| on/after 2 Dec | limit filled: "1760万円 利益確定", balance 21,213,915 (+17,602,200) (NP, SCR, TILE) | V05 i0152 | (120.05 − 110.271) × 1,800,000 = 17,602,200 ✓; the run's realized peak |
| same | "税金分考えて あと300万円だけ" (TH) | V05 i0153 | 25,000,000 − 21,213,915 − 1,000,000 = 2,786,085 (FXK-V05-C063, revised by FXK-V06-C051). The 2500万 target (V03 i0054) and the 1,000,000 withdrawal (V03 i0124) are printed; only her counting the withdrawal toward the target is inferred, and her own V06 count matches that rule to the yen (row "undated night"); the basis is STRENGTHENED to INFERENCE HIGH by FXK-SYN-C002 (section 5.6) |
| same | 300枚 short at 119.631, take-profit 118.6, no stop shown (BOX, TH) | V05 i0158 | +3,093,000 at 118.6 (CALC) |
| 5 Dec 18:27 | cut by hand, −1,743,000 → 19,470,915 (BOX); no stop order (V05-U05) | V06 i0009, i0013 | exit ≈120.212 (CALC, unprinted) |
| 5 Dec night | a new short at 121.220, cut at 121.597, −1,131,000 → 18,339,915 (BOX, TILE) | V06 i0045–i0046, i0095 | exact; holding the first short to 121.597 would have cost 5,898,000 (counterfactual CALC, V06 §F.1 row 7a); her own counterfactual on the V05 long, 24,998,515 with the withdrawal, is exact |
| undated night | "あと566万…とんで85円" (TH) | V06 i0096 | 25,000,000 − 18,339,915 − 1,000,000 = 5,660,085 ✓ |
| Dec 2014 | EUR/CHF 300枚 long, no stop "あえてしてない" (SP); entry date, rate and fill never printed | V06 i0115, i0148, i0152 | ≈448M yen notional, ≈24.4× on 18,339,915, ≈3.73M yen per 0.01 (FXK-V06-C033, conditional on the lot convention); V06-U01 OPEN at V10 |
| 25 Dec | contest result 19,749,835 (643.4%増) (BOX); "今40万円くらい" (SP) | V07 i0019–i0020 | 19,749,835 − 1,000,000 − 18,339,915 = 409,920 implied open P/L (conditional) |
| 7–8 Jan 2015 | overseas account: 100,000 deposited; "利確9万円プラス" (SP) | V07 i0060, i0063 | balance after 8 January unprinted (V07-U06) |
| 15 Jan | 「FX口座残高 -1億153万4644円 (-1億2028万4479円) 強制ロスカット」 (BOX) | V07 i0118 | 120,284,479 − 101,534,644 = 18,749,835 = 18,339,915 + 409,920: the parenthetical equals the loss from the 25 December equity (reading (a), nothing unprinted needed) or the trade's P/L with an unprinted 409,920 credit (reading (b)); FXK-V07-C018, V07-U01 OPEN |
| 16 Jan | 【不足金】-101,534,644円 due 19 January 15:00, then 年率14.6% (SCR) | V07 i0130 | 14,824,058 a year, ≈40,614 a day (CALC); her later "毎日4万円" rounds down (V08 i0031) |
| 16–18 Jan | bank 1,005,144 (SCR), identical to Kozue's 2008 balance | V07 i0144 | 1,005,144 − 1,000,000 = 5,144 (CALC); that the bank money is the V03 tax reserve is INFERENCE; required growth ≈101×; ladder 100万 × 2⁷ = 1億2800万 (FXK-V07-C025, C068) |
| V08 night 1 | overseas deposit 1,000,000 (BOX); +1,545,501 → 2,545,501; +1,973,674 → 4,519,175; 1000枚 → 0円 (BOX) | V08 i0003, i0009, i0012, i0020 | all exact (FXK-V08-D031); the 190,000 of V07 is not in the box (V07-U06 ADVANCED); that the deposit is the tax reserve is INFERENCE MODERATE-HIGH (V08 E001; the bank screen is not shown in V08) |
| V08 | 2014 tax 「3,807,983」 "およそ380万円" (SCR calculator; basis never printed); 予納金 "150万" (SP) | V08 i0034 | basis unprinted (V05-U04 family); the hypothetical "5500万" tax prints "×0.45%" where 45% is meant (V08 §F.4) |
| V09 | debt spoken as "1億" (round); 任意整理 "166万円以上" a month over five years | V09 i0018 | 100,000,000 / 60 = 1,666,667 ✓; 14.6% × 101,534,644 ≥ 1400万 ✓ (FXK-V09-D033) |
| V09 | bankruptcy: lawyer retained early February 2015; conclusion and discharge dated 平成27年11月 (DOC) | V09 i0098, i0104 | the notice records a 配当 although no assets are stated: UNRESOLVED (V09 §F.2) |
| V09 | 2014 tax survives; "一括じゃ払えないから 役所と相談中", "地道に払っていく"; wages managed by the father | V09 i0106–i0107 | amount not reprinted |
| 3 Apr 2017 | 保有金融資産 22,963円 (CAP) | V10 i0043 | lowest of the four captions |
| Apr 2017 | 2014 national tax still partly unpaid (SP); an inset reprises 「3,807,983」 | V10 i0045 | the amount outstanding in 2017 is not printed |

Whole-chain reading (ANALYST CALCULATION, conditional on no unshown flows and on treating the 23,110 as unaccounted): from 300,000 in February 2014 Kurumi reached 18,339,915 in the account plus the 1,000,000 set aside (V06 i0095; V03 i0124), about 64× her stake, before the EUR/CHF position; the forced liquidation removed 120,284,479 by the parenthetical; the 1,000,000 lost in V08 is, by INFERENCE MODERATE-HIGH, the reserve set aside for tax; and the 2014 tax it was meant to cover was still being paid in April 2017. Each link is a printed figure; the chaining and the identity of the V08 stake are not.

### 4.3 Chain B — the father's 300万

| Point | As printed | Locator | Status |
|---|---|---|---|
| V01 | CAP "300万円" (in quotation marks), three bands; deposited as "+3,000,000入金" | V01 i0109–i0111 | taken without consent; purpose (attack or survival) U-02 |
| V02 | the cash returns to him at discovery | V02 i0024–i0026 | U-07 resolved; whether it went back into the drawer is not shown |
| V09 | a bankbook ("総合口座通帳") holding 300万, "もともとくるみのために貯めてたお金"; offered for the bankruptcy costs; accepted | V09 i0074–i0075 | when the cash was banked (V09-U13) and whether it was used (V09-U14) not shown; INFERENCE MODERATE-HIGH that the costs came from it |

### 4.4 Chain C — Mochiko

| Point | As printed | Locator | Status / CALC |
|---|---|---|---|
| V01 | "少なくとも 1000万円以上" (CAP; Kurumi's belief); a 300万 loan offered, refused | V01 i0065–i0066 | belief only |
| 15 Jul 2014 | domestic 12,014,110 (BOX) | V02 i0158 | first own figure; contest base |
| V03 | 13,302,630 (BOX); USD/JPY 50枚 long, average printed 106.832 (i0148) and 106.382 (i0154); +359,000 open; contest +10.7% while she claims −10% | V03 i0148, i0154–i0155, i0092 | **average unresolved**: the V03 tiles fit 106.832 (FXK-V03-C020), V04 i0144 fits 106.382 exactly; FXK-V04-C038 DOWNGRADE; V04-U01 OPEN at V10 (section 3.4 b) |
| V04 | +3,209,000 (i0037); +4,729,000 at 115.840 (i0144); lender of 2,000,000 at 109.5% (SP), an IOU with thumbprint (DOC; day cut) | V04 i0037, i0088, i0104–i0105, i0144–i0145 | 6,000円 a day, 180,000 a month (CALC exact); exposure ≈3.2× |
| V05 | long by self-report; no figure | V05 i0130, i0145 | the loan as a "hedge" is coherent in direction, overstated in size (V05 §F.3, conditional on 50枚) |
| 8 Dec 2014 | all longs closed, 20,993,630 (+7,691,000) (SP, BOX) | V06 i0052 | 13,302,630 + 7,691,000 ✓; exit ≈121.764 or ≈122.214 depending on the average (conditional); flat from her December close by her own account (close time unprinted) |
| V07 | contest 74.7%増 (BOX); 8 Jan "損切りマイナス3万円" (SP); a company; game HUD 「残高 998万円」 (fiction within the fiction) | V07 i0014, i0063, i0041, i0038 | position on 15 January not shown (V07-U15; FXK-V07-C075) |
| V08–V10 | no figure; "仮に私が 10億円持ってても" (hypothetical) | V08 i0119 | no payment to or for Kurumi shown through V10 |

### 4.5 Chain D — Mebuki

| Point | As printed | Locator | Status / CALC |
|---|---|---|---|
| V02 | 200,000 scholarship stake → 613,200 (BOX), 500× account | V02 i0158 | +413,200 (CALC); no loss shown in V02 |
| 13 Aug 2014 | wiped out from 695,100 on a ≈246× GBP/USD long (NP; CALC consistent); told Yasuko "10万円くらい" | V03 | mechanism of the 0円 unshown (V03-U01); source of the +81,900 between 7/15 and 8/13 unshown |
| Sep–Oct | 800,000 deposited (600,000 tuition + 100,000 × 2 living money); USD/JPY 20枚 short at 106.632 (10 @105.355 + 10 added ≈107.909); +229,700 refused on 15 Oct; −258,100 late Oct; "−673,500 / 余裕" worst case | V03 i0073–i0078, i0130, i0158 | the anger add made the only profit (V03 §F.6 item 3); 100-yen gaps fit an average ≈106.6325; "−178%" irreproducible |
| 31 Oct | forced liquidation to 0円, "−800,000円" (the V04 history graph "累計−1,000,000円" = 200,000 + 800,000 deposits) | V04 i0012, i0139 | price and time unprinted |
| V04 | cards ≈300,000; student loan 300,000 (≈4,200 a month); Mochiko's 2,000,000 at 109.5% → balance 2,600,000 (BOX); 20枚 short from 112.102, −543,600 | V04 i0016–i0020, i0032, i0055–i0056, i0068, i0145–i0146 | zero equity 113.602 → 115.102 → 125.102 as deposits arrive (CALC); interest ≈184,200 a month (CALC) |
| V05 | rescue shorts; 43枚 (18 @112.102 + 25 @116.365), average 114.5805; balance 2,621,530; −1,002,120 open | V05 i0060–i0091 | all tiles exact (FXK-V05-D031); the "救い玉1枚" balloon against the tile kept |
| 5 Dec 2014 | −2,523,890 at 120.450 (BOX); liquidation 0円 "(−2,610,530円 強制ロスカット)" | V06 i0021, i0039 | **11,000 gap** against 2,621,530, kept as printed; implied ≈120.6515 |
| V06 | "今日3万円 振り込みました" | V06 i0051 | interest or principal not stated; 30,000 = five days at the printed 6,000円 a day (CALC), a fit, not a statement |
| 25 Dec | contest −3,400,000 (654.4%減) | V07 i0011–i0012 | 0 − (600,000 + 100,000 + 100,000 + 300,000 + 300,000 + 2,000,000) ✓; all of her 3,600,000 of FX deposits (200,000 + 3,400,000) were lost (CALC) |
| autumn 2015 | "このペースなら来月には完済"; a domestic account; a rand swap position, size and direction unprinted | V09 i0114–i0117 | the amount repaid and the interest paid are never printed |

### 4.6 Chain E — Yasuko

76,573 (BOX, V02 i0159) → −2,892 on her first trade and −2,629 off-page → 71,052 (BOX, V03 i0155; V04 i0047): 76,573 − 71,052 = 5,521 = 2,892 + 2,629 (CALC). Withdrawn by V07 ("全額出金済み", i0011). Comic: 1000 copies printed, 372 sold (SP, V05 i0126); "色々込みで100万円くらい" (SP, V07 i0024); Mochiko's "1300%" fits +1,307% on the 71,052 moved into the comic, not the 76,573 base (+1,206%) (CALC, V07 §F.9). V10 adds her 2013 start (5 November 2013), a 3枚 pound short and a forced liquidation of her "全財産" (V10 i0066–i0076; loss unprinted; lot unit not established); the origin of the 76,573 is still not printed (V02-U05 ADVANCED, not resolved). That she funded an account again after the 2013 liquidation is INFERENCE HIGH, not shown: the pages print the 2013 liquidation and the 2014 balance, not whether the 2014 account is a new one (the ledger's V10 note states it as shown, L2994).

### 4.7 Chain F — taxes

V02: Kurumi says she will file and pay (i0018). V03: 1,000,000 withdrawn "for tax and so as not to overreach" (i0124); target raised to 2500万 with tax in mind (i0054). V05: "税金分考えて あと300万円" (i0153; reconciled by FXK-V05-C063). V07: the bank balance of 1,005,144 becomes war funds (i0144). V08: deposited (INFERENCE MODERATE-HIGH that it is the reserve); the 2014 tax reckoned at 3,807,983 (basis unprinted) and judged undischargeable (i0034). V09: instalments, "地道に" (i0106). V10: still partly unpaid in April 2017 (i0045), amount unprinted. The tax rate and basis are never printed, so no tax figure is recomputed here; a real-world rate would be EXTERNAL_REFERENCE.

### 4.8 Chain G — Kozue (flashback figures)

Kurumi's mother is unnamed in V01–V05 and named 梢 at V06 i0065; the V01 figures below are hers by that later naming. V01: "家のお金 約2000万円" (CAP, i0014; SP i0011). V06 revises the composition and source of the sum, not its amount. V06 (2008): unrealized "マイナス600万円超え" (i0073); passbook to 「*0」 (i0075); savings, household money, insurance, the home down-payment and her parents' cash (i0071–i0077); 6 October 「当日決済損益 −18,790,50[…]」 (SCR, digit hidden, i0079) and "1900万円" (caption, i0080); balance 1,005,144 (TILE, i0082); 「100万円×400倍 = 4億円」 (i0083); 498,302 (i0086). CALC: 20,000,000 − 1,005,144 = 18,994,856 ≈ "1900万" (caption = total loss); the screen's one-day figure leaves ≈204,000 unexplained (INFERENCE MODERATE; V06 §F.10). The 1,005,144 recurs as Kurumi's bank balance (V07 i0144; FXK-V07-C025, C030, C068); whether Kurumi notices is not stated (V07-U12).

### 4.9 Chain H — the contest

Bases: V02-end balances (V02 i0158–i0159; verified as "開始時", V03 i0089–i0092). Rules: to 25 December, percentage growth, winner treats (V03 i0086–i0088); withdrawals counted, open positions at market, false reports banned (V06 i0141–i0144). Results (V07 i0011–i0020): Kurumi 643.4%増, Mochiko 74.7%増, Yasuko 7.2%減 on FX, Mebuki 654.4%減 (reconciled in 4.2–4.6). Yasuko was crowned on the clause "投資で増やすこと" and paid (i0021–i0026); the reward line is partly hidden (V06-U11). Mebuki's box settles that results are balances less post-base deposits.

### 4.10 Chain I — V10's new figures (FXK-V10-D035)

保有金融資産 captions of 3 April 2017: Inago 42,175; Nana 834,877; Kurumi 22,963; Kizuna 10,011,927 (V10 i0036–i0047; Kizuna 91.75% of the four: 10,011,927 ÷ 10,911,942, ANALYST CALCULATION). Nana: 834,877 − 100,000 = 734,877 (passbook i0126) − 300,000 = 434,877; securities 100,000 + 300,000 = 400,000; Kani 500株 @741 = 370,500 (i0142–i0143); −8,000 at 725 (i0145); all exact. Kizuna: 10,178,597 on 21 April, "前回+¥166,670" (exact difference; period and source UNRESOLVED); FX balance 3,972,290; EUR/USD 30枚 short at 1.07230 before a weekend vote (i0122); on Monday a screen in Nana's search shows the pair gapped from about 1.07 to about 1.086–1.091 (SCR, i0140; "adverse to a short", CALC MODERATE, V10 §F), which shows no outcome of her position and states nothing about the vote. The outcome is NOT SHOWN, and the forecasts that face it are beyond V10 and NOT SCOREABLE (section 6.4).

### 4.11 Unresolved or inconsistent figures, and how each stands at V10

| Figure | Locator | Nature | Status at V10 |
|---|---|---|---|
| +10円 residual on every 300-lot value | V01 i0130–i0162 | constant offset (swap, commission or rounding) | OPEN (U-04; FXK-V01-C013); never explained by paratext |
| +24,000 vs +24,200; −105,000 vs diagram 95.410; i0141 glitched digits | V01 i0049–i0050, i0083–i0084, i0141 | lettering / display | kept as printed; i0141 UNREADABLE |
| 23,110 between own share and domestic deposit | V02 i0102 | unshown flow | OPEN (V02-U07) |
| Mebuki's "200万以上" for Kurumi | V02 i0155 | a character's claim | basis unshown; fits cumulative 2,379,800 only if the 23,110 was not lost (CALC) |
| i0133 tiles 2,126,400 / −1,265,300 | V02 i0133 | emblematic | not reconciled |
| Kurumi 15 July → 1 September: +392,325 or +329,025 | V03 i0055–i0056 | box convention | kept; depends on whether the box includes open P/L |
| "−178%"; 100-yen gaps; "169.6" label; "43万円" | V03 i0091, i0137, i0158, i0123 | lettering / unshown flows | kept as printed |
| Mochiko's average 106.832 / 106.382 | V03 i0148, i0154; V04 i0037, i0144 | each fits one tile | OPEN (V04-U01; FXK-V04-C038) |
| Kurumi ≈29.9× against a 25× cap | V04 i0006; V01 i0075; V03 i0007 | rule never printed for her broker | tension, OPEN (V04-U02) |
| IOU day; card terms; student-loan rate | V04 i0145, i0016–i0020, i0032 | cut or unprinted | OPEN (V04-U11, U12, U08) |
| Ratio row 「証拠金維持率(%) 0円」 on Yasuko's app | V04 i0047 | transcription OBSERVATION HIGH (three crops); meaning INFERENCE | U-06 OPEN |
| "2014年10月下旬" caption | V05 i0141 | chronology slip | kept as printed |
| Mebuki's 43枚 after 19 Nov | V05 | unshown | RESOLVED in V06: liquidated 5 December (V06 i0039) |
| 11,000 gap at Mebuki's liquidation | V06 i0039 | box against prior balance | kept as printed |
| Kozue's −18,790,50[…] vs "1900万円" | V06 i0079–i0082 | ≈204,000 | kept; INFERENCE MODERATE that the caption counts the total loss |
| "1・12ドル" vs board 1.22867 | V06 i0105, i0049 | text slip (likelier) | kept |
| EUR/CHF entry date, rate, fill | V06–V07 | never printed | OPEN (V06-U01) |
| Kurumi's start drawn from "30万" in "5月" | V06 i0048 against V01 i0044 (14 February) | her retrospective self-presentation | kept as printed; a reliability flag on her later account |
| The parenthetical −120,284,479's reference | V07 i0118 | two readings | OPEN (V07-U01); reading (a) needs nothing unprinted |
| 1.16880 on two axes | V07 i0095, i0125 | odd grid value | OPEN (V07-U16) |
| Overseas 190,000 after 8 Jan | V07 i0063; V08 i0003 | unshown flow | ADVANCED, not resolved (V07-U06) |
| 5,144 in the bank beyond the 1,000,000 withdrawal | V07 i0144; V03 i0124 | unshown flow; the 1,005,144 equals Kozue's 2008 balance (design) | OPEN (V07 §F.9; V07-U12 for Kurumi's notice) |
| "×0.45%" in the tax formula | V08 i0030 | lettering (45% intended) | kept as printed |
| glitched strip | V08 i0130 | by design | UNREADABLE (V08-U01) |
| bankruptcy 配当 with no stated assets; use of the 300万 | V09 i0104, i0074–i0075 | unshown | OPEN (V09 §F.2; V09-U14) |
| 2014 tax basis and 2017 balance | V08 i0034; V10 i0045 | unprinted | OPEN |
| three wealth terms; a table summing to 98.4%; Kizuna's +166,670 | V10 i0047, i0109, i0108 | lettering / unshown source | kept as printed; source UNRESOLVED |
| Kizuna's EUR/USD short; the outcome of the depicted vote | V10 i0122, i0140 | not shown | NOT SCOREABLE beyond V10 |
| Figures never printed | various | unprinted | Mochiko's source of 12,014,110, her July EUR/USD sell, her stop, whether the 2,000,000 left her account (V06-U15) and her company's capital; Kurumi's pre-shock equity, the liquidation rate, the three V08 fill rates, any payment to the broker, her 2017 pay; Kozue's 2008 lot size; Mebuki's repayment total and interest. All OPEN; none may be supplied by inference or by real-world practice |

Usage rules for G3–G5 prose. The debt owed after 15 January 2015 is 101,534,644 (box and e-mail, V07 i0118, i0130); "1億2千万" is Mochiko's labelled estimate (V07 i0115, i0118) or the parenthetical, never the debt. 3,807,983 is Kurumi's 2014 tax computation (V08 i0034), reprised in V10 only inside a flashback inset; it is never an April 2017 balance. Four distinct 300万 are named by locator: the father's cash taken in V01 (i0109–i0111) and his bankbook offered in V09 (i0074; the same money on his own account, a late revelation), Mochiko's V01 loan offer to Kurumi (V01 i0065; the V07 i0099 montage), and the after-tax shortfall (V05 i0153). "1億" is the debt (V08–V09), Kizuna's yardstick (V10) and the 億 temptation (V05 i0154; V10 i0049); "2000万" is Kozue's loss, Kurumi's target and "母が失った2000万円" (V06 i0095). The 1,000,000 withdrawn and the 1,005,144 in the bank are kept distinct. The V08 stake is "the 1,000,000, by INFERENCE MODERATE-HIGH the V03 tax reserve". Mochiko's December close is "by her own account, flat from her December close (time unprinted)", never "flat on 15 January". Kurumi's V06 cuts are hand cuts; no stop order is shown for the V05 short.

### 4.12 Assessment

Where a trade and its operands are printed, each Kurumi box follows exactly from the previous box (V01; V03 from 1 September; V04–V08), and the cross-character checks (two tiles fixing one rate in V03; Mebuki's deposits composing her contest figure in V07; Nana's passbook in V10) close exactly. Three steps of Kurumi's chain rest on unshown flows or unprinted trades: V01 → V02 (the 23,110), V02 itself (+556,690 with no pair, size or entry printed) and 15 July → 1 September (+392,325 or +329,025). The residue elsewhere is small and of four kinds: lettering slips and truncations; a few unexplained gaps (23,110; 11,000; 190,000; 5,144; ≈204,000); one genuine two-way conflict (Mochiko's average); and figures the pages never print (broker rules, the EUR/CHF entry, the tax basis, Mebuki's repayment, Kizuna's result). No load-bearing claim in the readings rests on an unlabelled calculation. Two calculations carry the most argumentative weight and both are exact: the V01 lot decomposition (FXK-V01-C014) and the V07 composition of the parenthetical (FXK-V07-C018). The later narrative's use of round figures ("1億", V09; the 2017 tax unprinted, V10) is a feature of the pages, not a defect of the record.

## 5. Claim history

### 5.1 Where the claim history lives, and how complete the ledger's copy is

The claim history at V10 is held in two places that must be read together:

- **Ledger C rows.** V01's seventeen rows record V01 claims and their reconciliation states; V01's §D theses have no rows of their own (the governing thesis's core is carried by FXK-V01-C011, with C010 and C012 beside it; the competing thesis had no row until FXK-SYN-C006). V02 records its transitions of V01 claims inside the status cells of new rows (for example FXK-V02-C001: "FXK-V01-C011 → STRENGTHEN (uptake answered)"; FXK-V02-C007 for V01-C005; FXK-V02-C009 for V01-C009) and has no "Transition of" rows. From V03 each volume adds explicit "Transition of FXK-Vnn-Cnnn" rows: V03 9 of 34 C rows, V04 20 of 47, V05 27 of 64, V06 30 of 70, V07 35 of 75, V08 31 of 74, V09 32 of 75, V10 22 of 72 (counted at the base).
- **Each reading's §M claim-transition table.** It is the complete record for its volume. It names every accepted claim it moves and, from V06, ends with a blanket line, "All other accepted claims | PRESERVE (no material change) | No Vnn bearing". Some transitions in these tables have no ledger row (for example V04 §M: V03-C002 PRESERVE and V02-C002 PRESERVE; V05 §M: V04-C002 PRESERVE).

Consequence for retrieval: a claim's state at V10 is its last explicit transition (a ledger row or a §M table), carried forward by the blanket PRESERVE lines, plus any FXK-SYN-C row. Section 5.4 lists the places where a blanket line covered a volume that did bear materially on the claim.

### 5.2 Governing and competing theses, volume by volume

| Vol. | Governing thesis (ID; label) | Later transitions | Competing thesis (ID) | Later transitions | Standing at V10 |
|---|---|---|---|---|---|
| V01 | An education in loss whose plot overturns its own lessons; the win rewards the worst process (§D, EVALUATION MODERATE-HIGH; ledger core FXK-V01-C011) | C011: V02 STRENGTHEN (uptake answered, in FXK-V02-C001); FXK-V03-C033, V04-C047 STRENGTHEN; FXK-V05-C060 REVISE (a bracketed exit rewarded, escalation punished); FXK-V06-C064 REVISE (the stopless EUR/CHF trade as the new test); FXK-V07-C067 REVISE (the test answered by ruin); FXK-V08-C068 REVISE (reward and ruin compressed into one night); V10 §M PRESERVE for Kurumi, the displaced test (Yasuko's 2013 flashback, V10 i0070–i0076) STRENGTHENS the pattern | A black comedy of chance; competence is not what the market rewards (§D, HYPOTHESIS MODERATE). FXK-ERR-V01-03 (FXK-V01-C017) removed the story author's afterword from its support | Registered by FXK-SYN-C006 (OPEN) | Governing core stands in revised form: what the story rewards became a two-sided pattern of reward followed by ruin. The competing thesis is registered; its standing at V10 is argued in the integrated synthesis |
| V02 | FXK-V02-C001: the lesson learned and overruled; the lucky win as a lifelong "呪い" (EVALUATION on NARRATOR_PRESENTATION HIGH) | FXK-V03-C026, V04-C042 STRENGTHEN; FXK-V05-C055 STRENGTHEN with refinement; FXK-V06-C061, V07-C064, V08-C064 STRENGTHEN; FXK-V09-C069 PRESERVE (qualified: V09 locates the pull in innate greed, i0031); FXK-V10-C064 STRENGTHEN (Kurumi's own "たまたま ハイレバFXで 上手くいったから", V10 i0049) | FXK-V02-C002: a chosen return under pressure, partly vindicated by depicted outcomes | V04 §M PRESERVE (no row); FXK-V05-C056 STRENGTHEN for the 180枚, OPEN for the new short; FXK-SYN-C004 DOWNGRADE of the outcome strand; agency strand OPEN pending Study C | Governing: the run's most consistently confirmed claim. Competing: the outcome strand holds for V02–V05 only; the agency strand is argued in G3 |
| V03 | FXK-V03-C001: Mebuki's harm self-authored but socially aggravated (Yasuko's warning dismissed; Mochiko's lie and canary) | FXK-V04-C028, V05-C049 STRENGTHEN; nothing after V05 | FXK-V03-C002: the decisive failure Mebuki's alone (15 October), the final blow exogenous | V04 §M PRESERVE (OPEN, live; no row); nothing after | The pair is OPEN pending G3 (Study B strand iv), argued together with the V05–V07 evidence on both sides |
| V04 | FXK-V04-C001: harm moves into debt and labour; the decisive escalation relational (Mochiko's 2,000,000 at 109.5%; the lie that she is short); two meanings of responsibility | FXK-V05-C034 STRENGTHEN with refinement; the responsibility strand FXK-V04-C015 → V05-C041 REVISE, V06-C052, V07-C059, V08-C061 REVISE (extend) | FXK-V04-C002: Mebuki's course set before Mochiko spoke | V05 §M PRESERVE (OPEN, live; no row); nothing after | The pair is OPEN pending G3 (Study B strand iv); the responsibility strand stands as extended to V08 |
| V05 | FXK-V05-C001: threads of money, concealed information and learned habit bind the four; Mochiko's creed given a biography | FXK-V06-C036 STRENGTHEN with refinement | FXK-V05-C002: a sympathetic origin story; the real danger is Kurumi's grief and restitution drive | FXK-V06-C037 STRENGTHEN (absorbed into V06 C001); FXK-V07-C055, V08-C060 STRENGTHEN; FXK-V09-C068 REVISE (Kurumi re-reads the drive as a pretext for innate greed, V09 i0031–i0032) | Governing stands. Competing absorbed, then revised by Kurumi's own V09 self-account (a SELF_REPORT, not a settled cause) |
| V06 | FXK-V06-C001: losses turned into an inheritance and then a certainty ("必勝") | FXK-V07-C035 STRENGTHEN (resolved by the 15 January ruin) | FXK-V06-C002: two traders learning to take losses; EUR/CHF a reasoned position | FXK-V07-C036 DOWNGRADE; the exogenous-shock strand survives as V07 C002 | Settled by V07 |
| V07 | FXK-V07-C001: a catastrophe narrated as blind to circumstance but legible as the product of a sized, stopless position; the daughter re-enacts the mother; Mochiko silent | FXK-V08-C041 STRENGTHEN (first two strands), REVISE (Mochiko's silence ends in V08) | FXK-V07-C002: an exogenous disaster and a resilient woman; silence as realism or respect | FXK-V08-C042 DOWNGRADE in part (the exogenous strand preserved in a character's voice: Mochiko's "事故", V08 i0153) | Governing stands (revised); competing survives only as a character's view |
| V08 | FXK-V08-C001: debt turned into a question of what responsibility may demand of a life, answered by a friend's question about wanting | FXK-V09-C043 STRENGTHEN (first strand), REVISE (the re-enactment strand) | FXK-V08-C002: a rough, calculated rescue ("投資", "打算付き") that leaves the facts where they were; crisis interrupted | FXK-V09-C044 DOWNGRADE; the melodrama strand carried in V09 C002 | Governing stands (revised). The content of Mochiko's "投資" is largely resolved in V09 (section 7.2, V08-U07) |
| V09 | FXK-V09-C001: debt closed through institutions and family; desire owned, not cured (共生 with greed) | FXK-V10-C048 STRENGTHEN (displacement strand), PRESERVE (debt and desire) | FXK-V09-C002: a restoration comedy that dissolves the crisis too fast and displaces risk onto new characters; alternative FXK-V09-C075: 共生 as the Kurumi–Mochiko workplace symbiosis | FXK-V10-C049 STRENGTHEN; FXK-V10-C060: C075 OPEN (no material test) | Both live; the control claim inside C001 ("支配して コントロールしてみせる", FXK-V09-C032) is OPEN, untested in V10 |
| V10 | FXK-V10-C001: the market moves from Kurumi's body to her workplace; she is a silent witness; the narrator sows "欲望の種" (EVALUATION on OBSERVATION HIGH; design EVALUATION MODERATE-HIGH) | none (boundary) | FXK-V10-C002: a workplace-and-fandom comedy that domesticates investing; outcomes deferred | none (boundary) | Both NEW and OPEN at the knowledge cutoff; any later test lies beyond V10 |

### 5.3 Long-running carried claims (state at V10)

| Claim | Path | State at V10 |
|---|---|---|
| FXK-V01-C005 Mochiko's motive | REVISE (extend) in V02 (in C007), V03-C031, V04-C045, V05-C058, V06-C062, V07-C065, V08-C066, V09-C070 | OPEN in substance: each volume extends the evidence (private contempt V01; steering V02; lies and the canary V03; the loan V04; biography V05; silence V06–V07 and the V07 inner account of use; the "打算付き" rescue V08; the job offer V09) without a settled motive; FXK-V07-C075 (no exploitation or gain shown) preserved in V10. Current wording: 5.5 row 6 |
| FXK-V01-C006 conflict of interest | withdrawn at the V01 reconciliation; REVISE in V03-C032, V04-C046, V05-C059 (extend) | STRENGTHENED by FXK-SYN-C005 on Mochiko's V07 admission to Mebuki (section 5.6) |
| FXK-V01-C010 Kurumi's failure | V03-C034 OPEN for Kurumi, transferred to Mebuki (V03 C005); FXK-V06-C063 REVISE (from incapacity to repudiation of the stop rule); V07-C066, V08-C067 STRENGTHEN (as revised); V10 PRESERVE for Kurumi | stands as revised; untested after V08 because Kurumi does not trade in V09–V10 |
| FXK-V01-C012 the daughter repeats the mother | V06-C065 PRESERVE; V07-C068, V08-C069 STRENGTHEN; FXK-V09-C071 REVISE ("似てるけど違う", V09 i0058, i0061) | stands as revised in V09: repetition owned and distinguished |
| FXK-V03-C012 escalation after success and loss | V05-C054 STRENGTHEN in size, QUALIFIED in words; V06-C059, V07-C062, V08-C062 STRENGTHEN; V10 PRESERVE for Kurumi, the displaced test STRENGTHENS | stands |
| FXK-V05-C029 restraint on any suicide scenario | V06-C048 PRESERVE; V07-C058 PRESERVE with caution; FXK-V08-C059 REVISE (ideation, planning and means shown; no act); FXK-V09-C067 STRENGTHEN | stands as revised in V08 |
| FXK-V07-C023 meanings of responsibility (自己責任 as solitary repayment) | V08-C046 REVISE (extend); FXK-V09-C065 REVISE | stands as revised in V09 (debt shared with institutions and family) |
| FXK-V09-C008 Mochiko's prediction that Kurumi returns to the market | V10 §M OPEN | OPEN; any outcome lies beyond V10 |
| FXK-V01-C013 +10円 residual; FXK-V01-C015 purpose of the deposit | OPEN since V01; V02 OPEN | OPEN |
| FXK-V07-C018 the parenthetical's reference | UNRESOLVED (V07-U01) | UNRESOLVED; reading (a) needs nothing unprinted (section 4.2) |

### 5.4 Claims whose state was unclear, and what was done

(a) **V01's competing thesis (a black comedy of chance) had no ledger row and no recorded transition.** Its natural successors are the exogenous-shock strand of FXK-V07-C002 (DOWNGRADED in part by FXK-V08-C042) and the comedy theses FXK-V09-C002 and FXK-V10-C002, but no record linked them to it. Registered by FXK-SYN-C006 (OPEN); its standing is argued in the integrated synthesis.

(b) **FXK-V02-C002 (a chosen return "partly vindicated by depicted outcomes").** Its last explicit state was "STRENGTHEN for the 180枚; OPEN for the short" (FXK-V05-C056). V06 cut that short by hand at −1,743,000 and a new short at −1,131,000 (V06 i0013, i0046), and V07's next position ended in the −101,534,644 balance (V07 i0118); the V06 and V07 §M tables nonetheless covered it with "PRESERVE (no material change)". The outcome strand is DOWNGRADED by FXK-SYN-C004. The agency strand ("chosen") is a separate question the later volumes keep alive (V09's "堂々と", i0078–i0079; "相場が大好きだから", i0119–i0121); it is OPEN pending its argument in Study C.

(c) **The V03 and V04 thesis pairs on Mebuki's agency.** FXK-V03-C002 and FXK-V04-C002 (the decisive failure hers alone; her course set before Mochiko spoke) were last explicitly PRESERVED in the V04 and V05 §M tables (OPEN, live) with no ledger rows. Their governing counterparts FXK-V03-C001 and FXK-V04-C001 were last STRENGTHENED in V05 (FXK-V05-C049, FXK-V05-C034), and no V06–V10 reading names any of the four. V05 (Mebuki overhears that Mochiko was long, i0144–i0146), V06 (her liquidation, relief and turn to work, i0039, i0051–i0053) and V07 (Mochiko's "私は芽吹を利用して勝ちに行った" and "悪いことしたとは思ってない"; Mebuki's "騙されていた" with gratitude, i0017–i0019) bear on both sides of each pair. Stabilizing one side while the other stays at its V05 state would skew what a reader retrieves, so each pair is routed together to Study B (strand iv), argued with the evidence on both sides and written at G3 integration. Their state is OPEN pending G3.

(d) **FXK-V01-C006 (the conflict-of-interest question).** Last extended in V05; Mochiko's V07 admission to Mebuki is direct self-report on it and was not brought to the claim. STRENGTHENED by FXK-SYN-C005.

(e) **FXK-V01-C007 (the 「FXトレード日誌」 is the mother's; INFERENCE MODERATE-HIGH).** V02 PRESERVE (not tested); V06 then shows Kozue writing 「FXトレード日誌」 on the notebook (V06 i0065; V06 reading §C: "the notebook Kurumi found in V01"; "the notebook's origin is now shown") and Kurumi reading it (i0090, i0093–i0095). The V06 §M blanket PRESERVE left the claim at an inference the pages had made an observation. STRENGTHENED to OBSERVATION HIGH by FXK-SYN-C001.

(f) **Claims revised by errata.** FXK-V01-C017 (FXK-ERR-V01-03: V01 i0165 reclassified as the story author's afterword; §D, §K and L.7 no longer cite it) and FXK-V07-C032 (FXK-ERR-V07-01: the V07 afterword i0153 and bonus essay i0154–i0157 classified as authorial extras). The forecast corrections of the errata are forecast records (section 6). After these corrections no accepted claim depended on a reclassified page except the V05 method use of its bonus strip, now withdrawn by FXK-SYN-C003.

(g) **No contradictory ledger states were found.** Every claim with transitions in more than one volume has a coherent sequence; the defects above are omissions (a state not updated), not conflicts. FXK-V05-C063 was transitioned in V06 by FXK-V06-C051 (REVISE: the gap 5,660,085 by the same formula, i0096); its grade is raised by FXK-SYN-C002. FXK-V08-C072, C073 and C074 read "ADDED AT RECONCILIATION" without a transition word; they are NEW claims (C073 later STRENGTHENED by FXK-V09-C063).

### 5.5 Current wording for chains whose transitions were never consolidated

Several long chains carry REVISE or "REVISE (extend)" rows whose new observations are recorded but whose revised wording is not. The wording below is a reconciliation statement for retrieval; it changes no accepted claim. Where a study or the integrated synthesis changes the grade or scope of one of these chains, it writes an FXK-SYN-C row naming the last explicit transition.

| # | Chain (last explicit transition) | Current wording at V10 | Label and rivals |
| --- | --- | --- | --- |
| 1 | FXK-V01-C011, the outcome rewards the worst process (V10-C065) | True of V01–V04 (V01 i0157–i0162; FXK-V03-C015; V04 i0112); mixed in V05–V06 (a bracketed exit rewarded, V05 i0152; escalation punished, V05 i0091; cuts judged by two clocks, V06 i0015, i0044–i0046, i0098); the no-stop, high-leverage process punished catastrophically in V07–V08 (V07 i0118; V08 i0009–i0020); displaced onto Yasuko's 2013 flashback in V10 (i0070–i0076). What survives across the series is an arc of early reward setting up later ruin, not a moral that the worst process pays | EVALUATION MODERATE-HIGH as an arc. Stating the V01 wording as the series' claim would be the largest available error |
| 2 | FXK-V02-C001, the lucky win as a lifelong "呪い" (V10-C064) | Strong as narrator presentation (V02 i0132–i0134) and as Kurumi's recurring luck attribution (V05 i0153; V10 i0049); as the series' causal psychology it competes with Kurumi's own V09 account, innate greed since childhood (V09 i0031–i0032), which V09 stages by re-presenting a childhood beach memory with the winged figure beside the child (V09 i0031; V05 i0161 has no such figure; both pages re-opened in the synthesis) | Two competing self-accounts kept apart: the narrator's "呪い" and Kurumi's "根っからの欲張り" (SELF_REPORT); the V09 image is a retrospective re-reading (late revelation); INFERENCE MODERATE-HIGH that it re-presents the V05 memory |
| 3 | FXK-V01-C010, inability to cut (V10 PRESERVE) | Changes kind: felt incapacity under loss of family money (V01 i0131, i0135); two realized cuts made by hand with no stop order shown, then repudiation of the rule (V06 i0013, i0046, i0098–i0099); stopless sizing chosen in advance (V06 i0152; V07; V08); transferred intact to Mebuki (FXK-V03-C005 → V06-C055) | Strong only as revised; untested after V08 |
| 4 | FXK-V03-C012, escalation after success (V10 PRESERVE and displaced STRENGTHEN) | Strong in size (V01 50 → 300 lots; V04 +120枚; V05 300; V06 300 EUR/CHF; V08 300 → 600 → 1000); MODERATE in stated motive; no goal raised to 億 in V05 (V05 checkpoint C-01); after V08 the temptation appears only as inner speech (V10 i0049) | Counterexamples: the V03 withdrawal (i0124), the V04 declined add (i0115), the V05 slap memory (i0154) |
| 5 | FXK-V01-C012, V06-C029, V07-C030 re-enactment (V09-C071, V09-C060 REVISE) | OBSERVATION HIGH for the parallels (household money; 1,005,144; "お母さんとおんなじ"; the 「すみませんでした」 sheet of V08 i0042 redrawing the composition of V01 i0030, both pages re-opened in the synthesis); EVALUATION MODERATE-HIGH as design; MODERATE as Kurumi's recognition (V01 i0140; V07 i0147; V08 i0041); WEAK as a cause of her decisions; ends in difference in V09 ("似てるけど違う", i0061; the 300万 offered openly, i0074–i0075) | No page shows Kurumi taking a rule from the journal (V06 checkpoint C-02) |
| 6 | FXK-V01-C005 Mochiko's motive (V09-C070) and FXK-V03-C008 relish (V08-C063) | Toward Mebuki, use for advantage is SELF_REPORT HIGH (V03 i0150; V07 i0017). Toward Kurumi, a watching purpose and private contempt are SELF_REPORT HIGH (V01 i0155–i0159; V05 i0048), and Mochiko's own inner account names use as the origin of the friendship ("利用できると…思ったから 付き合っただけだ", V07 i0045, INFERENCE MODERATE-HIGH that it is unspoken; FXK-V07-C065); no act exploiting Kurumi's vulnerability and no gain from her loss is shown (FXK-V07-C075). Relish at a friend's plight is a V01–V03 private attitude that thins in V04 (i0109, i0145) and is absent from V05 on (FXK-V04-C031, V05-C052, V06-C057, V07-C061, V08-C063). Care-like acts run from V01 (i0116, i0119, i0155, i0162) and V04 (i0100, i0118, i0120) through V05 (i0108–i0112) to the costly V08 intervention and the V09 offer | The motive stays UNRESOLVED; each state is dated, and the V07 account describes how the tie began, not what it became (V07 reading §L, counterreading 8) |
| 7 | FXK-V04-C015 two meanings of responsibility, with FXK-V07-C023 (V09-C065) | A designed motif whose object moves: a disclaimer before advice (V02 i0066) and a licence (V02 i0131); Mochiko's disclaimer against Yasuko's "あたしの責任だよ" (V04 i0052, i0136); in V05 both accept Mebuki's 自己責任 and the contrast becomes whether responsibility ends care (Mochiko; "全部自分の責任だろうが!" in thought, i0132) or coexists with it (Yasuko, i0133–i0139; FXK-V05-C041); a third shape, the salon customer's "責任は僕にあるから" (V06 i0035; FXK-V06-C052); silence (V06 i0154); acceptance of the debt (V07 i0140); a duty converted toward self-harm (V08 i0042–i0047, analysed without method); disclosure, payment "地道に" and accepted external control, with 「自己責任」 absent (V09 i0063, i0106–i0107) | EVALUATION HIGH as a motif (every occurrence lettered) |
| 8 | FXK-V09-C001 debt and desire; FXK-V09-C032 control (V10-C048; V10 §M OPEN) | Debt closed through institutions and family on two captions and an offer whose use is unshown (V09 i0098, i0104; V09-U14); desire owned in Kurumi's own words (SELF_REPORT); the control she resolves on (i0128) is untested because she places no order in V10 | MODERATE; nothing beyond V10 may test it |
| 9 | FXK-V01-C006 conflict of interest (FXK-SYN-C005) | Withdrawn for V01 (no adverse position shown); established for Mebuki from V03 (an undisclosed long while urging a short, V03 i0148), self-described to Yasuko in V05 (i0130–i0131) and admitted to Mebuki in V07 (i0017); none toward Kurumi is recorded | The V01 row's withdrawal stands for V01 only |
| 10 | FXK-V03-C011 Kurumi opposite Mebuki (V06-C058) | Opposite and unknowing in V03–V04 (long against Mebuki's short); on Mebuki's side and unknowing at V05's end (V05 i0158); both short and both losing on 5 December (V06) | OBSERVATION HIGH for positions; Kurumi's knowledge as each row states |
| 11 | FXK-V05-C002 the V05 competing thesis (V09-C068 REVISE) | Splits: the Mochiko half (coldness as self-protection; the loan a disclosed hedge) stands as V05 left it; the Kurumi half (grief and restitution drive as the real danger) was strengthened through V08 and then re-read by Kurumi as a pretext for innate greed (V09 i0031–i0032) | SELF_REPORT revision, not a settled cause |

### 5.6 Claim transitions decided in this reconciliation (FXK-SYN-C001 to FXK-SYN-C006)

Under the rule of the role-gap audit (section 2.4 (a)), a transition of an accepted claim is written at G2 when the evidence on both sides already sits in the accepted readings and no study's argument with rivals is needed. Six records meet that test; each is written in the ledger's claim table with this section as its authority. They are interpretive transitions, argued here; none is a mechanical copy.

**FXK-SYN-C001 — FXK-V01-C007, the 「FXトレード日誌」 is the mother's: STRENGTHEN to OBSERVATION HIGH.**
- Last explicit transition: V01 reconciliation, "PRESERVE as INFERENCE MODERATE-HIGH" (basis V01 i0039, i0062, i0139); V02 PRESERVE (not tested); covered by the V06 §M blanket line.
- Downstream evidence: V06 i0065 shows Kozue writing 「FXトレード日誌」 on a notebook, which the V06 reading identifies as the notebook Kurumi found in V01; the 2008 screen beside the 「FXトレード日誌」 (i0079); Kurumi reading it (i0090, i0093–i0095).
- Contrary evidence and limits: no page shows a second journal or another author; the identity of the V06 notebook with the V01 one rests on its title and design as the V06 reading records them.
- What would overturn it: a page showing another author or a second journal.

**FXK-SYN-C002 — FXK-V05-C063, as revised by FXK-V06-C051, Kurumi's after-tax reckoning: the basis STRENGTHENED to INFERENCE HIGH.**
- Last explicit transition: FXK-V06-C051 (REVISE: the gap 5,660,085 by the same formula, V06 i0096); the V05 row graded the basis "INF MOD-HIGH (tax rate unprinted)".
- Downstream evidence: the 2500万 target is printed ("税金考えると2500万円が本当の目標になる…", V03 i0054) and so is the 1,000,000 withdrawal "税金分" (V03 i0124). Two counts of her own fit one rule: "あと566万…とんで85円" at V06 i0096 matches it to the yen (25,000,000 − 18,339,915 − 1,000,000 = 5,660,085), and the round "あと300万円" at V05 i0153 fits its 2,786,085 (25,000,000 − 21,213,915 − 1,000,000) (ANALYST CALCULATION; ledger FXK-SYN-C033).
- Contrary evidence and limits: only the combination rule — that she counts the withdrawal toward the gross target — is inferred; the tax rate and basis are never printed, and the rule is hers, not a tax computation.
- What would overturn it: a printed count of hers that leaves the withdrawal out.

**FXK-SYN-C003 — FXK-V05-C032, the V05 bonus strip used for method: REVISE (method use withdrawn; the chart convention rests on internal evidence).**
- Last explicit transition: FXK-V05-C032, NEW (OBSERVATION of paratext; "used for method only"), also the basis cited in the V05 reading's §F preamble, its §F.1 row 12, E059 and counterreading L.5, and repeated in the V06 entering state.
- Reason: the synthesis rule makes paratext classification-only and never evidence for design intent; the strip's statements are authorial statements about how the work renders charts and P/L.
- Downstream evidence for the convention without the strip: a daily chart whose 10/15 low disagrees with the intraday rate the tiles imply (V03 §F.7); irregular axis sequences treated as schematic (V06 §F); odd and glitched grid values (V07 §F, i0125). Every accepted reconstruction already uses printed tiles and boxes, not chart shapes.
- Consequences: no accepted reconstruction changes; the V05 counterreading the strip supported (the spike may be a wick; the short may profit) is moot after V06, where both shorts were cut at a loss; the +10円 residual (FXK-V01-C013) is never explained by the strip's remark about swap. The rest of C032 (the blurb not adopted; the under-jacket note excluded) stands. Whether the V05 reading or the register's V05 extras row ("used only as method paratext") should carry a note is the coordinator's decision (section 9 item 3).

**FXK-SYN-C004 — FXK-V02-C002, the competing thesis of V02: the outcome strand DOWNGRADED; the agency strand OPEN pending G3.**
- Last explicit transition: FXK-V05-C056 ("STRENGTHEN for the 180枚; OPEN for the short"); V06–V10 blanket PRESERVE.
- Evidence for the outcome strand: V02's printed outcomes (+556,690, V02 i0158; her calls right, i0072, i0120) and the 180枚 bracket realized for +17,602,200 (V05 i0152).
- Contrary evidence: the V05 short was cut by hand at −1,743,000 and a new short at −1,131,000 (V06 i0013, i0046); the next position ended in the −101,534,644 balance (V07 i0118); the V08 stake went to 0円 (V08 i0020).
- Disposition: "partly vindicated by depicted outcomes" holds for V02–V05 and fails as a cross-volume description; DOWNGRADE, not REJECT, because the V02 and V05 outcomes remain printed. The agency strand ("a chosen return") is a separate question with live evidence (V09 i0078–i0079, i0119–i0121) and rivals (the narrator's "呪い"; innate greed as Kurumi's own account); it is argued in Study C and written at G3 integration.

**FXK-SYN-C005 — FXK-V01-C006, as extended by FXK-V05-C059, the conflict-of-interest question: STRENGTHEN (toward Mebuki).**
- Last explicit transition: FXK-V05-C059 (REVISE, extend: counterparty, creditor and adviser at once, self-described to Yasuko, V05 i0130–i0131); earlier FXK-V03-C032 and V04-C046.
- Downstream evidence: in V07 Mochiko tells Mebuki to her face "私は芽吹を利用して勝ちに行った" and "悪いことしたとは思ってない" (V07 i0017; FXK-V07-C065 records it under her motive).
- Limits: what "利用" covers is unspecified (V07 reading §M); the V01 withdrawal stands for V01; no adverse position toward Kurumi is recorded (FXK-V03-C032; FXK-V07-C075).
- What would overturn it: a page showing that the V03–V05 positions were not hers or not adverse to Mebuki's.

**FXK-SYN-C006 — registration of V01's competing thesis: OPEN.**
- Claim: "V01 is a black comedy of chance in which competence is not what the market rewards" (V01 reading §D, HYPOTHESIS MODERATE); no ledger row before this one; FXK-V01-C017 removed the story author's afterword from its support.
- Successor strands recorded, not argued: the exogenous-shock strand of FXK-V07-C002 (DOWNGRADED in part by FXK-V08-C042; it survives in a character's voice, V08 i0153); the comedy theses FXK-V09-C002 (STRENGTHENED by FXK-V10-C049) and FXK-V10-C002 (NEW, OPEN).
- Disposition: OPEN at HYPOTHESIS MODERATE; its standing at V10 is argued in the integrated synthesis.

Routed to G3 and written at G3 integration, not here: FXK-V03-C001 with FXK-V03-C002, FXK-V04-C001 with FXK-V04-C002 (Study B, strand iv) and the agency strand of FXK-V02-C002 (Study C).

## 6. Forecast history (as recorded; not rescored)

### 6.1 Conventions

- V01–V04: the readings and checkpoints score principal items as CONFIRMED / DISCONFIRMED / PARTIAL / UNSCORABLE without a Brier score; the financial specialist's items carry probabilities, and its own scores were adopted with noted exceptions (V02 checkpoint B-20; V03 checkpoint B-24 and reviewer C-06 on G8 and H10; V04 errata FXK-ERR-V04-03).
- From V05 every forecast is scored literally as frozen, with relaxed or event-only results labelled alongside (entrypoint; V05 reading §M preamble). From V06 the checkpoints carry a §8 "Forecast tallies" with Brier scores under the declared convention (LOW 0.20, LOW-MODERATE 0.35, MODERATE 0.55, MODERATE-HIGH 0.70, HIGH 0.85; outcome 1 or 0; a constant 0.5 forecaster scores 0.250).
- Calibration excludes EXPOSURE-SENSITIVE items; from V08 the principal's primary calibration also excludes slip-qualified items.
- No cumulative cross-volume tally of any role exists in the repository (errata FXK-ERR-V04-03 states this for the financial specialist), and none is computed here. If one is wanted, it is a process record about the run's forecasters, computed only from the recorded literal scores and exclusions, and it belongs in the integrated synthesis's limitations (role-gap audit, section 3.5).
- The character specialist froze no prospects in any volume; the reviewer is not a forecasting role.
- Row-level cautions (verified against the ledger): FXK-V01-F029 reads only "QUALIFIED"; its content is that the first clause occurred and the condition never triggered (Mochiko never learned of the household money), and no V01 tally depends on it. Eleven V07 financial-specialist rows (FXK-V07-F110, F113, F118, F120, F122, F126, F129, F130, F138, F139, F156) read "observed", "not observed" or "record; outside the tallies": they stay outside every tally. Freeze labels repeat across volumes (FXK-V03-F082 and FXK-V04-F076 are both "F09-2"); retrieval uses IDs only (section 8.4).

### 6.2 V01–V05 (as recorded)

| Vol | Set | Recorded result | Source |
| --- | --- | --- | --- |
| V01 | Coordinator entering conjectures (FXK-V01-F001–F002) | Dispositions only (F001 confirmed on Kurumi and Mochiko; the "Yasuko" identification not counted) | V01 reading §M.1 |
| V01 | Principal freezes F00–F05 (FXK-V01-F003–F044) | Item dispositions; no tally computed | V01 reading §M.2 |
| V01 | Principal MAIN_EXIT FX-1 to FX-6 (F045–F050) | Disposed of in V02 (FXK-V02-F015–F020); no tally computed | V02 reading §M.2 |
| V01 | Financial specialist F01–F04 (22 items, F051–F072) | Dispositions in the ledger; no tally computed; credit PRESERVE (FXK-ERR-V01-02) | ledger |
| V02 | Principal entering V02-EN-1 to EN-14 (F001–F014) | Dispositions; no tally computed | V02 reading §M.1 |
| V02 | Principal freezes F01–F06 (54 items, F021–F074) | 27 confirmed or confirmed-qualified, 14 disconfirmed, 2 partial, 1 exposed, 10 unscorable | V02 reading §M.3; V02 checkpoint C-12 |
| V02 | Principal MAIN_EXIT MX-1 to MX-13 (F075–F087) | Disposed of in V03 (FXK-V03-F014–F026); no tally computed | V03 reading §M.2 |
| V02 | Financial specialist (40 items, F088–F127) | Its own scores adopted with three wording differences; F095 credit QUALIFIED and F111 credit NONE (FXK-ERR-V02-02); no tally computed | V02 checkpoint B-20 |
| V03 | Principal entering EN-1 to EN-13 (F001–F013) | Dispositions; no tally computed | V03 reading §M.1 |
| V03 | Principal freezes F01–F09 (53 items, F033–F085) | 36 confirmed, 11 disconfirmed, 5 partial, 1 open (F09-2) | V03 reading §M.4 |
| V03 | Financial specialist (27 items, F099–F125); V02 B-F10a-2 to -7 disposed of as F027–F032 | Its scores adopted except G8 and H10 (CONFIRMED by wording); all credit PRESERVE (FXK-ERR-V03-02) | V03 checkpoint B-24; reading §M.9 |
| V04 | Principal entering EN-1 to EN-15 (F001–F015) | 6 confirmed, 9 disconfirmed | V04 reading §M.1 |
| V04 | V03 MAIN_EXIT MX-1 to MX-13 (F016–F028) | 4 confirmed, 6 disconfirmed, 3 partial | V04 reading §M.2 |
| V04 | Principal freezes F01–F10 (53 items, F029–F081) | 34 confirmed, 17 disconfirmed, 1 partial (F07-2), 1 unscorable (F08-3) | V04 reading §M.3 |
| V04 | Financial specialist FREEZE_00–04 (73 items, F091–F163) | Literal 27–46, Brier 0.20849; relaxed event-only 28–45, Brier 0.20164; head-clause reading of B4-J10 26–47, Brier 0.20575 (recorded in the errata, not adopted); constant 0.5 = 0.250 | FXK-ERR-V04-03; V04 reading §M.8; ledger FXK-V04-F136 |
| V05 | Principal entering EN-1 to EN-15 (F001–F015) | 10 confirmed, 5 disconfirmed | V05 reading §M.1 |
| V05 | V04 MAIN_EXIT MX-1 to MX-9 (F016–F024) | Literal 5–4 (calibration without MX-4: 4–4); relaxed as first reported 6–3 | V05 reading §M.2 |
| V05 | Principal freezes F01–F08 (76 items, F025–F100) | Literal 34 confirmed, 41 disconfirmed, 1 not triggered (F05-8); calibration without the five ES items 31–39–1; relaxed as first reported 37–37–2 | V05 reading §M.3 |
| V05 | Financial specialist F01–F02 (12 items, F111–F122) | Item outcomes in the ledger and V05 checkpoint §7; F116, F119, F120 out of calibration; no tally computed | V05 checkpoint §7 |

The financial specialist also counted its own recorded dispositions where no tally was computed (V01 19 confirmed, 2 disconfirmed, 1 partial of 22; V03 14 confirmed, 8 disconfirmed, 2 split, 3 not shown of 27; V05 6 confirmed, 4 disconfirmed, 1 split, 1 partly untested of 12). These are counts of ledger outcomes, not checkpoint tallies; no Brier score exists for these sets and none is computed.

### 6.3 V06–V10 (checkpoint §8, literal; calibration; labelled alternatives retrievable there)

| Vol | Set | Literal (C–D of n; Brier) | Calibration |
| --- | --- | --- | --- |
| V06 | Principal entering EN-1 to EN-18 | 15–3 of 18; 0.2271 | 14–3 of 17; 0.2285 |
| V06 | V05 MAIN_EXIT MX-1 to MX-10 | 6–4 of 10; 0.2172 | 1–4 of 5; 0.2105 |
| V06 | Principal freezes F01–F13 (72 scored of 79) | 41–31 of 72; 0.2028 | 37–30 of 67; 0.1997 |
| V06 | All V06-made principal forecasts | 56–34 of 90; 0.2077 | 51–33 of 84; 0.2056 |
| V06 | Financial specialist F00–F05 (64) | 43–21 of 64; 0.2256 | 31–19 of 50; 0.2251 |
| V07 | Principal entering EN-1 to EN-17 | 13–4 of 17; 0.1834 | 11–4 of 15; 0.1883 |
| V07 | V06 F13-2 to F13-6 and MX06-1 to MX06-5 | 8–2 of 10; 0.1820 | 6–1 of 7; 0.1846 |
| V07 | V06 financial specialist F06-1 to F06-13 | 8–5 of 13; 0.2073 | 6–5 of 11; 0.2082 |
| V07 | Principal freezes F01–F06 (43) | 27–16 of 43; 0.2077 | 12–10 of 22; 0.2402 |
| V07 | All V07-made principal forecasts | 40–20 of 60; 0.2008 | 23–14 of 37; 0.2192 |
| V07 | Financial specialist F00–F05 (52 scored of 79) | 32–20 of 52; 0.1542 | 31–20 of 51; 0.1533 |
| V08 | Principal entering EN-1 to EN-17 (EN-10 OPEN) | 6–10 of 16; 0.2014 | 6–7 of 13; 0.2058 |
| V08 | V07 MX07-1 to MX07-11 | 10–1 of 11; 0.2216 | 3–0 of 3; 0.2383 |
| V08 | V07 financial specialist F05-1 to F05-15 (11 scored) | 7–4 of 11; 0.2080 | the same |
| V08 | Principal freezes F01–F06 (55 scored of 57) | 30–25 of 55; 0.1669 | primary 25–19 of 44; 0.1689 |
| V08 | All V08-made principal forecasts | 36–35 of 71; 0.1747 | primary 31–26 of 57; 0.1773 |
| V08 | Financial specialist F00–F05 (75 scored of 96) | 35–40 of 75; 0.2044 | 33–36 of 69; 0.2062 |
| V09 | Principal entering EN-1 to EN-16 | 12–4 of 16; 0.2456 | 10–3 of 13; 0.2310 |
| V09 | V08 MX08-1 to MX08-16 | 12–4 of 16; 0.1934 | 8–2 of 10; 0.1752 |
| V09 | V08 financial specialist F05-4 to F05-20 | 12–5 of 17; 0.2062 | 11–4 of 15; 0.1853 |
| V09 | Principal freezes F01–F10 (65) | 38–27 of 65; 0.2224 | primary 26–17 of 43; 0.2400 |
| V09 | All V09-made principal forecasts | 50–31 of 81; 0.2270 | primary 36–20 of 56; 0.2379 |
| V09 | Financial specialist F00–F01 (27) | 16–11 of 27; 0.2252 | 13–7 of 20; 0.2072 |
| V09 | Financial specialist F02-D1 to D4 (deferred covers) | 4–0 of 4; 0.2013 | the same |
| V10 | Principal entering EN-1 to EN-17 | 7–10 of 17; 0.2134 | 4–8 of 12; 0.2325 |
| V10 | V09 MX09-1 to MX09-15 | 6–9 of 15; 0.2308 | 3–6 of 9; 0.2244 |
| V10 | V09 financial specialist F02-1 to F02-20 | 10–10 of 20; 0.2052 | 2–6 of 8; 0.1772 |
| V10 | Principal freezes F01–F05 (48 scoreable) | 23–25 of 48; 0.2108 | primary 8–10 of 18; 0.2542 |
| V10 | Principal MAIN_EXIT MX10-1, MX10-2 | 2–0 of 2; 0.0563 | MX10-1 only 1–0; 0.0225 |
| V10 | All V10-made principal forecasts | 32–35 of 67; 0.2068 | primary 13–18 of 31; 0.2383 |
| V10 | Financial specialist F00–F02 (24) | 13–11 of 24; 0.1649 | 6–4 of 10; 0.1785 |

The V10 checkpoint's own reading of its result: on the primary set the principal's V10 freezes are slightly worse than a constant 0.5 forecaster (0.2542 against 0.250); they over-expected that Kurumi would act, that Mochiko would return and that outcomes would resolve inside V10. EVALUATION (MODERATE): across V06–V10 every recorded literal Brier score of every set lies between 0.0563 and 0.2456, mostly between 0.15 and 0.23, so both forecasting roles beat the constant forecaster on most sets but not by a wide margin; the sets are small and heterogeneous, and no cross-volume aggregate exists to support a stronger statement.

### 6.4 Items facing events after V10: NOT SCOREABLE IN THIS RUN

Frozen and never to be resolved or speculated on (V10 checkpoint §8): the principal's F05-4, F05-5, F05-6 (ledger FXK-V10-F101–F103), MX10-3 (also exposure-tainted) and MX10-4 (F106–F107); the financial specialist's B10-FC-1 to FC-15 (FXK-V10-F132–F146). Earlier items about "the next volume" were all scored in the following volume, up to V09's MAIN_EXIT and the financial specialist's V09 F02 set (disposed of in V10 as FXK-V10-F018–F052).

## 7. Unresolved evidence obligations (consolidated)

Sources: each checkpoint's §5 (V01–V10). From V06 the checkpoints list only new obligations and point to the reading's §M.5–§M.7 for carried statuses; every status below was confirmed against those tables. Status vocabulary as the checkpoints use it: RESOLVED, ADVANCED, NARROWED, OPEN, WITHDRAWN, CLOSED, KEPT AS PRINTED. Where a later page bears on an obligation that a blanket line did not record, the row says so and section 7.3 lists it. None of the open items is answerable inside this run (V10 checkpoint §5).

### 7.1 Obligations opened in V01–V05

| ID | Obligation | Status at V10 | Resolved or advanced by |
| --- | --- | --- | --- |
| V01 U-01 | How and when Kurumi's V01 300枚 were closed | OPEN | Never shown; recalled without the close (V03 i0104; V05 i0158) |
| V01 U-02 | The purpose of taking the father's cash | OPEN (V06 §M OPEN; V09 §M: no bearing — the confession, V09 i0063–i0075, does not revisit the V01 purpose) | V04 adds Kurumi's word "借金" (i0074) |
| V01 U-03 | "Yasuko" as あふぃちゃん's name | RESOLVED in V02 | Caption, V02 i0074 |
| V01 U-04 | Cause of the constant +10円 residual | OPEN (no interpretive consequence) | — |
| V01 U-05 | Whether i0003 belongs to 第1話; the meaning of 「第N集」 | ADVANCED: 「第N集」 numbers the volume and carries a title in V01 and V03–V10; V02 has none (register). i0003's chapter membership stays unresolved | V03–V10 openings |
| V01 U-06 | The broker's stop-out percentage and margin rate | OPEN: no stop-out or maintenance level is printed for Kurumi's or Mebuki's broker (register V01–V10; the one printed ratio, 「証拠金維持率が100%…」, is in the 2013 notice to Yasuko, V10 i0076); the V01 margin rate fixed at 1:500 by calculation (V02 checkpoint §5); the V04 i0047 ratio row is a 0円 display, not a level (section 4.1) | Forced liquidation printed as an event only (V04 i0012; V06 i0039; V07 i0118; V08 i0020) |
| V01 U-07 | Return of the 300万; the father's knowledge | RESOLVED in V02 | V02 reading §M.5 |
| V01 U-08 | Minor specialist items (clocks, hoodie dating, note locator) | Non-material; no owner | — |
| V02-U01 | Date of the 2,100,000円 domestic deposit | OPEN | — |
| V02-U02 | Who recommended the pound to Mebuki | OPEN | V03 and V04 add only her own attachment and "ポンド買い ロスカット" (V04 i0139) |
| V02-U03 | Entry, exit and stop of Kurumi's trades | ADVANCED (V04 adds, the V05 bracket and fill, the V06 hand cuts); the EUR/CHF entry, rate and fill were never printed (V06-U01); no Kurumi trade after V08 | V04 i0006; V05 i0077–i0080, i0152; V06 i0013, i0046 |
| V02-U04 | The ring-wearing woman of V02 i0131 | OPEN (last recorded in V04: no bearing; V06's Kozue flashback does not identify the V02 montage figure on any recorded page) | — |
| V02-U05 | Yasuko's trading history; the origin of 76,573円 | ADVANCED (V03 i0003; V04 i0046, i0136; her 2013 start, escalation and forced liquidation of her "全財産" in V10 i0066–i0079; FXK-V10-C062 reads the 76,573 account as continuity, not contradiction); the 76,573 unexplained. The V10 §M.7 blanket line overlooks this (7.3) | — |
| V02-U06 | How Mochiko knows Kurumi trades "前より"; the other half of her motive | As recorded: partly answered in V03 (shared positions, i0010–i0011, i0053–i0055), "unchanged" in V04, no later record. V05's 2012 thought "いいサンプル" (i0048) bears on the motive half (7.3) | — |
| V02-U07 | The 23,110 gap; the basis of "200万以上"; whether Mebuki follows Kurumi's calls | The last part answered (lapsed in V03, rejected in V04 i0068); the first two OPEN | — |
| V02-U08 – U10 | i0133 tiles and the partial i0106 tile; V02 wall clocks; the V02 cover poster | Non-material; no owner | — |
| V03-U01 | Mechanism of Mebuki's 13 August 0円 | ADVANCED: labelled "ポンド買い ロスカット" (V04 i0139); level and mode never printed | — |
| V03-U02 | Mebuki's account after the 10/31 move | RESOLVED in V04 | "芽吹 FX口座残高 0円 (−800,000円) 強制ロスカット" (V04 i0012) |
| V03-U03 | Mochiko's stop level and exit | ADVANCED: she closes her longs in V06 (i0051–i0052; time unprinted); the stop level is never printed | V05 i0145; V06 |
| V03-U04 | Mochiko's motive for the false "−10%" | ADVANCED (V06 §M: the lie named by Kurumi and banned by the no-lies rule, i0143; Mochiko deflects; no stated motive); V07's admission (i0017) concerns Mebuki, not this lie | — |
| V03-U05 | Whether Mebuki would have closed had Mochiko told the truth | OPEN (V06 §M: Mebuki never closed; liquidated 5 December, i0039); the counterfactual cannot be settled by any page | — |
| V03-U06 | Whether 第15話's first pages are the night of 10/15 | Non-material; OPEN | — |
| V03-U07 | Source of Mebuki's +81,900 | OPEN | — |
| V03-U08 | Yasuko's off-page −2,629; her "同じ失敗" | −2,629 unchanged since V04. "同じ失敗": the V10 2013 flashback (i0070–i0076: an early win, escalation, forced liquidation) supplies a possible content (INFERENCE; not recorded by V10, 7.3) | — |
| V03-U09 | Contest rules for re-funded accounts; the 12/25 result | RESOLVED in V07 (the Christmas results) | V07 i0007–i0025 |
| V03-U10 | Items not re-inspected at V03 | Non-material | — |
| V04-U01 | Mochiko's average (106.832 or 106.382) | OPEN; both kept | — |
| V04-U02 | Kurumi's broker leverage rule | OPEN: no rule printed for her accounts; the V05 checkpoint corrects the V04 note (25× was stated in V01 i0075) | — |
| V04-U03 | Kurumi's university year | RESOLVED in V05 (FXK-V05-C064) | V05 i0042 |
| V04-U04 | Status of the V04 i0148 コミチア panel | RESOLVED in V05 (imagined; the event shown at i0103–i0126) | — |
| V04-U05 | Mebuki's short after V04 i0068 | RESOLVED: open in V05 (i0060, continued as V05-U01), liquidated to 0円 in V06 (i0039) | — |
| V04-U06 | Yasuko's withdrawal of 71,052 | OPEN | — |
| V04-U07 | Why Kurumi's father comes home late | ADVANCED (transfer from 年明け announced, V05 i0069); the lateness itself never explained | — |
| V04-U08, U11, U12 | Student-loan rate basis; the IOU's day and debtor name; card terms | OPEN | — |
| V04-U09 | Who cut Yasuko's call | OPEN (Mebuki, INFERENCE MODERATE-HIGH) | — |
| V04-U10 | Yasuko's kanji 私 in asides | OPEN (あたし throughout V05) | — |
| V04-U13 | Kurumi's change of clothes | Low value; no owner | — |
| V05-U01 | Mebuki's 43-lot short after 19 November | RESOLVED in V06 (forced liquidation to 0円, i0039) | — |
| V05-U02, U03, U15 | "救い玉1枚" against the tile; "2014年10月下旬"; printed anomalies | KEPT AS PRINTED | — |
| V05-U04 | Kurumi's tax basis for "あと300万円" | ADVANCED: ≈3,807,983 by her calculator (V08), owed in instalments (V09 i0106–i0107); the 2017 amount is not printed (V10-U09); her counting rule toward the 2500万 target is now INFERENCE HIGH (FXK-SYN-C002) | — |
| V05-U05 | Whether the 300-lot short has a stop | RESOLVED in V06: no stop order; she cut the 300-lot short by hand at 18:27 on 5 December (i0009, i0013); the second cut (i0046) closes a new short | V06 reading §M |
| V05-U06 | The i0154 inset | CLOSED at the V05 reconciliation (the father's slap) | — |
| V05-U07 | Chapter attribution of i0103–i0104 | Unresolved; no consequence | — |
| V05-U08 | Mebuki's envelopes; repayment | ADVANCED (V06 deferral, i0053; repaying in autumn 2015, "来月には完済", V09 i0114–i0117) | — |
| V05-U09 | Mochiko's size, average and stop | ADVANCED (V06) | — |
| V05-U10 | Yasuko's price and costs | OPEN | — |
| V05-U11 | The man packing Mebuki's "仕送りBOX" | OPEN (HYPOTHESIS MODERATE her father) | — |
| V05-U12 | Mochiko's withheld realization (i0038) | OPEN | — |
| V05-U13 | Mochiko's father; where she lived 2012–14 | OPEN | — |
| V05-U14 | Business status of 毒島's card | OPEN; V10-U15 asks whether Yasuko's editor is 毒島 | — |
| V05-U16 | Kurumi's university year | WITHDRAWN at the V05 reconciliation | — |
| V05-U17, U18 | The white cat as the 2006 kitten; the visitor in the cat-emblem jacket | OPEN | — |
| V05-U19 | Whether the salon offers sexual services | ADVANCED in V06–V07 without change in substance; OPEN | V06 i0018, i0041–i0042 |
| V05-U20 | Whether Yasuko told Kurumi of the loan | OPEN (V06 and V07 §M: unshown; Kurumi shows no knowledge of the loan; the V08 entering state lists the loan among what she does not know) | — |
| V05-U21 | Speaker of "なにそれ" (i0145) | UNRESOLVED (INFERENCE MODERATE Mochiko) | — |
| V05-U22 | Whether Mochiko registered Yasuko's あふぃちゃん identity | OPEN (uptake not shown in V05; no later record) | — |
| V05-U23 | Minor items not re-inspected | Non-material; one sub-item RESOLVED in the synthesis: the child's silhouette at i0161 is a child pitching forward with her bowl and shells flying, toward a woman in a wide hat who reaches for her; no winged figure is drawn (page and crop [330,1530,780,1730] re-opened; section 10). The other sub-items (i0089 dip, i0046 speaker, i0082 object) stay open | V05 i0161 |

### 7.2 Obligations opened in V06–V10

| ID | Obligation | Status at V10 |
| --- | --- | --- |
| V06-U01 | EUR/CHF entry date, moment and rate | OPEN; never printed (V07, V08) |
| V06-U02, U06, U08, U14 | Speakers: "芽・吹・" (i0055); the aborted "あんたさぁ!" (i0043); i0143 lines; "4桁万円" / "簡単" (i0147) | OPEN |
| V06-U03 | Content of Mebuki's call home (i0044) | ADVANCED in V07 (parents opposed her leaving university; INFERENCE MODERATE) |
| V06-U04 | Digits hidden in "−18,790,50[…]" (i0079) | OPEN; not reconstructed |
| V06-U05 | The 11,000 gap in Mebuki's liquidation box (i0039) | KEPT AS PRINTED |
| V06-U07 | Whether Kurumi knew of the narrated 8 December announcement | OPEN |
| V06-U09 | Whether Kozue's parents or her husband learned of her losses before her death | As recorded OPEN (V09 §M: no bearing). The father's "母さんのときは 相談もなかったからな…" over the memory of "お金のことは全部俺に任せて" (V09 i0072; FXK-V09-E029) shows by his self-report that she did not consult him (7.3); her parents remain unaddressed |
| V06-U10 | Mochiko's contest withdrawals | RESOLVED in V07 (INFERENCE MODERATE-HIGH: none counted) |
| V06-U11 | Hidden text after 「ごほうび!: 負」 | ADVANCED in V07; OPEN |
| V06-U12 | Door-sign middle character | Resolved: the V01 sign reads 「ぱぱ・ままのへや♡」 (V01 i0010, enlarged at G4; semantic validation audit, section 9, item 10), as the V06 sign does, so the difference the V06 records note is not on the pages (erratum FXK-ERR-V06-02) |
| V06-U13 | How Kurumi learned that Mebuki has a job | OPEN (V07 §M: no new source; V07 shows Mebuki describing the job and Yasuko already aware, i0007–i0010) |
| V06-U15 | Whether Mochiko's +7,691,000 shows the loan never left her domestic account | OPEN; not re-examined |
| V06-U16 | Whether full-resolution i0158 is a colour page | OPEN; structural only |
| V07-U01 | Reference of the parenthetical −120,284,479 (i0118) | ADVANCED by parallel in V08 (V08's parenthetical is the change from the last printed balance); OPEN |
| V07-U02 | "300万円の融資" in Mochiko's memory | WITHDRAWN (the V01 offer to Kurumi) |
| V07-U03 | The "取り返さなきゃ" face (i0080); the voice at i0147 | OPEN (INFERENCE MODERATE-HIGH / INFERENCE MODERATE Kozue) |
| V07-U04 | Mochiko's invitation "私と一緒に…" | ADVANCED in V09 (completed as "私の会社に来ない?", i0035, INFERENCE MODERATE) |
| V07-U05 | "解決策…はないわけではない" | Continued as V08-U07; largely resolved in V09 (bankruptcy and the company invitation) |
| V07-U06 | Overseas balance after 8 January; the +90,000 | ADVANCED in V08 (prior balance 0 by calculation) |
| V07-U07 | The exam date; the 19 January deadline | RESOLVED in V09 (a date after the deadline; its passing never shown, V08-U11) |
| V07-U08 | Composition of Mebuki's −3,400,000 | CLOSED at the V07 reconciliation (C070) |
| V07-U09, U10, U12, U14, U16 | Mochiko's motive in crowning Yasuko; the light-haired woman; whether Kurumi registers the identical balance; 「まあ い[っ?]か…」; the axis value 1.16880 | OPEN |
| V07-U11 | The 「201」 field (i0099) | ADVANCED (HYPOTHESIS LOW Kurumi's flat, V08); V09 adds the company's room 201 (i0140) without resolving it |
| V07-U13 | Whether the 2014 tax is still owed | ADVANCED: owed and paid in instalments (V09); the 2017 amount unprinted (V10-U09) |
| V07-U15 | Whether Mochiko held a position on 15 January | OPEN |
| V08-U01 | Glitched numeral strip (i0130) | OPEN by design |
| V08-U02 | Whether the たのしいFX notices (i0056) are actual or imagined | OPEN (UNRESOLVED; no lean adopted) |
| V08-U03 | The landline caller | OPEN |
| V08-U04 | Quotative force of the i0123 line | WITHDRAWN (「出ていって?」) |
| V08-U05 | Fate of the letter and the purchases; the 「すみませんでした」 sheet | ADVANCED in V09 (purchases returned; the letter read and drawn as backdrop); the letter's physical fate and the sheet's status OPEN (continued as V09-U07). ADVANCED further in the synthesis: V08 i0042 P1 redraws the composition of V01 i0030 P1 (the sheet, the centred words, a banded pen at lower right, a hatched ground), with no caption, hand or act of writing, before "私も 責任取らなきゃ…" (P4) (both pages re-opened, section 10). This favours a recalled image of Kozue's note over a new note of Kurumi's (INFERENCE MODERATE), but a redraw could also mark repetition in a new note; the status stays UNRESOLVED and no prose may say Kurumi wrote the words |
| V08-U06 | Whether Kurumi read Mebuki's message | ADVANCED in V09 (messages read and answered) |
| V08-U07 | Content of Mochiko's "投資" | ADVANCED, largely resolved in V09 (bankruptcy and the company; Kurumi a clerk in 2017) |
| V08-U08, U09, U12, U13 | "でも" (i0150); the voice "見ないほうがいい"; the bank balance after the deposit; minor objects | OPEN |
| V08-U10 | Five chapters against six issue designations (i0170) | OPEN |
| V08-U11 | V08's dates and the deadline's passing | ADVANCED in V09 (a date after the deadline; its passing never shown) |
| V09-U01 | 「大都大学」 against 新都大学 | OPEN |
| V09-U02, U03, U05 | 新都ビルヂング and room 201; Kizuna's chart; whether Kurumi trades by 2017 and her circumstances | V10 §M.7: U02 ADVANCED (building sign and door plate 「(株)もちもち企画」, no room number, i0061, i0111); U03 ADVANCED, largely resolved (she trades FX and sells short; the V09 chart's instrument unidentified, i0118–i0122); U05 ADVANCED (not trading, "…はい"; 2014 tax still partly owed; office sleeping a stated "趣味"; residence and pay open as V10-U09) |
| V09-U04 | What (株)もちもち企画 does | OPEN |
| V09-U06 | Mebuki's rand position and "作戦" | OPEN (Mebuki absent from V10) |
| V09-U07 | The letter's physical fate; whether the father learns of it | OPEN |
| V09-U08, U09, U12 | Placement-based attributions; the 99 missed calls; why Inago was hired | OPEN |
| V09-U10 | Yasuko's 【漫画家】 status | RESOLVED in part in V10 (a magazine spread, i0092) |
| V09-U11 | Referent of "ずっと小さな姿で現れてた" | NARROWED (INFERENCE MODERATE-HIGH the V02 tempter) |
| V09-U13 | The 300万's route into the bankbook | NARROWED (the cash returned in V02; only the deposit date unshown) |
| V09-U14 | Use of the father's 300万; bankruptcy costs; the trustee's distribution | OPEN |
| V09-U15 | Whether Yasuko's NEET acquaintance is Nana | RESOLVED in V10 ("脱ニート", i0088; shared school) |
| V10-U01 – U15 | Kizuna's short and Monday conduct; the depicted vote's result; Kizuna's カリフラワー intention and answer to Nana; Nana's Kani position and transfer; the "前作のアプリ"; the winged Kurumi of i0033; the i0049 memory figure and the i0043 faces; Nana's household contribution; Kurumi's residence, pay and remaining tax; printed inconsistencies (reading §F.8); placement-based attributions; what Inago counts (i0123); Mochiko's knowledge of her staff's investing; whether Kurumi's stock study leads to an account; Yasuko's pen name and editor | OPEN at the terminal boundary; the outcome items (U01–U04, U14) face events after V10 and are never resolved here |

Confidence disagreements preserved at V10: the +500 market-buy row as Nana's (principal MODERATE, financial specialist LOW-MODERATE); whether Kizuna lives alone (not stated).

### 7.3 Bearings that a later volume's blanket line did not record

From V08 the readings' obligation tables end with a line such as "Other carried obligations | (as listed in the V08 reading §M.7) | No V09 bearing; unchanged" (V09 §M.7; V10 §M.7 likewise). Reading the later pages' recorded observations against the carried list, four obligations turn out to have a later bearing. None is resolved; each status above is the recorded one, with the supported change noted here.

| Obligation | Later page that bears on it | Status the later page supports | Note |
|---|---|---|---|
| V02-U05 (Yasuko's trading history; the 76,573) | V10 i0066–i0079 (2013 start, early win, 3枚 pound short, forced liquidation of her "全財産") | ADVANCED (history shown); the 76,573 still unexplained | FXK-V10-C062 already relates the flashback to the 76,573 account; only the obligation row was not updated |
| V02-U06 (the other half of Mochiko's motive toward Kurumi) | V05 i0048 (her 2012 thought that Kurumi would be "いいサンプル") | ADVANCED for the motive half | The V05 reading records the thought under Mochiko's biography and FXK-V01-C005, not under the obligation |
| V03-U08 ("同じ失敗"; the off-page −2,629) | V10 i0070–i0076 | ADVANCED for "同じ失敗" (INFERENCE: the flashback's escalation and liquidation may be the failure she meant); −2,629 unchanged | Attribution of the V03 phrase to the 2013 events is an inference, not a page statement |
| V06-U09 (whether her husband or her parents learned of Kozue's losses before her death) | V09 i0072 ("母さんのときは 相談もなかったからな…"; FXK-V09-E029) | ADVANCED for the husband (SELF_REPORT that she did not consult him); her parents unaddressed | Whether he learned otherwise before her death is still not shown |

Route: working notes for G3 (the studies cite the later pages directly); a synthesis ledger record is warranted only where an integrated-synthesis argument relies on the advanced status (section 9 item 10).

## 8. Navigation index of the ledger

`FX_KURUMI_DECISION_AND_EVIDENCE_LEDGER.md` at the base snapshot. Line numbers are those of the base file and drift when the ledger is edited; the row IDs are the stable anchors. The ledger has three tables and no HTML anchors inside them: the episode table (header L23), the combined claim and forecast table (heading "Claim and forecast history" L348, header L352) and the "Person-level qualification" section (L2416). Every volume's IDs are contiguous with no gaps (row counts equal the last number). Totals at the base (ANALYST COUNT by row ID): 320 D rows, 549 C rows, 1,510 F rows.

### 8.1 Decision and evidence episodes (D rows)

| Vol | Rows | Start line | End line |
| --- | --- | ---: | ---: |
| V01 | FXK-V01-D001–D031 | 25 | 55 |
| V02 | FXK-V02-D001–D032 | 56 | 87 |
| V03 | FXK-V03-D001–D035 | 88 | 122 |
| V04 | FXK-V04-D001–D022 | 123 | 144 |
| V05 | FXK-V05-D001–D032 | 145 | 176 |
| V06 | FXK-V06-D001–D032 | 177 | 208 |
| V07 | FXK-V07-D001–D034 | 209 | 242 |
| V08 | FXK-V08-D001–D032 | 243 | 274 |
| V09 | FXK-V09-D001–D034 | 275 | 308 |
| V10 | FXK-V10-D001–D036 | 309 | 344 |

### 8.2 Claim history (C rows) and forecast history (F rows)

Each volume's C block precedes its F block in the one table. To read a claim's state at V10, combine its last explicit transition here with the later readings' §M claim-transition tables and their blanket PRESERVE lines (section 5.1), and with any FXK-SYN-C row; V02 records its transitions of V01 claims inside the status cells of new V02 rows.

| Vol | C rows (lines) | F rows (lines) | F sub-blocks (row ranges) |
| --- | --- | --- | --- |
| V01 | C001–C017 (354–370) | F001–F072 (371–442) | coordinator entering conjectures F001–F002; principal freezes F00–F05 F003–F044; MAIN_EXIT FX-1–6 F045–F050; financial specialist F051–F072 (from L421) |
| V02 | C001–C021 (443–463) | F001–F127 (464–590) | entering EN-1–14 F001–F014; V01 FX-1–6 dispositions F015–F020; freezes F01–F06 F021–F074; MX-1–13 F075–F087; financial specialist F088–F127 (from L551) |
| V03 | C001–C034 (591–624) | F001–F125 (625–749) | entering F001–F013; V02 MX dispositions F014–F026; V02 financial-specialist B-F10a-2–7 F027–F032; freezes F01–F09 F033–F085; V03-MX-1–13 F086–F098; financial specialist F099–F125 (from L723) |
| V04 | C001–C047 (750–796) | F001–F163 (797–959) | entering F001–F015; V03-MX dispositions F016–F028; freezes F01–F10 F029–F081; V04-MX-1–9 F082–F090; financial specialist F091–F163 (from L887; FREEZE_00 F091–F108) |
| V05 | C001–C064 (960–1023) | F001–F122 (1024–1145) | entering F001–F015; V04-MX dispositions F016–F024; freezes F01–F08 F025–F100; V05-MX-1–10 F101–F110; financial specialist F111–F122 (from L1134) |
| V06 | C001–C070 (1146–1215) | F001–F190 (1216–1405) | entering F001–F018; V05-MX dispositions F019–F028; freezes F01–F13 F029–F107; MX06-1–5 F108–F112; financial specialist F113–F190 (from L1328) |
| V07 | C001–C075 (1406–1480) | F001–F173 (1481–1653) | entering F001–F017; V06 F13/MX06 dispositions F018–F027; V06 financial-specialist F06 dispositions F028–F040; freezes F01–F06 F041–F083; MX07-1–11 F084–F094; financial specialist F095–F173 (from L1575) |
| V08 | C001–C074 (1654–1727) | F001–F212 (1728–1939) | entering F001–F017; MX07 dispositions F018–F028; V07 financial-specialist F05 dispositions F029–F043; freezes F01–F06 F044–F100; MX08-1–16 F101–F116; financial specialist F117–F212 (from L1844) |
| V09 | C001–C075 (1940–2014) | F001–F180 (2015–2194) | entering F001–F016; MX08 dispositions F017–F032; V08 financial-specialist F05-4–20 dispositions F033–F049; freezes F01–F10 F050–F114; MX09-1–15 F115–F129; financial specialist F130–F180 (from L2144) |
| V10 | C001–C072 (2195–2266) | F001–F146 (2267–2412) | entering F001–F017; MX09 dispositions F018–F032; V09 financial-specialist F02 dispositions F033–F052; freezes F01–F05 F053–F103 (F101–F103 not scoreable); MX10-1–4 F104–F107 (F106–F107 not scoreable); financial specialist F108–F146 (from L2374; FC-1–15 F132–F146 not scoreable) |
| Synthesis | FXK-SYN-C001–C006 (appended after L2412 in the G2 transaction). In ledger version 1.16: C001–C006 (G2) L2413–2418; C007–C028 (G3 convergence) L2419–2440; C029–C032 (the integrated synthesis's transitions, written at the G4 close-out) L2441–2444; C033–C034 (dated corrections of FXK-SYN-C002 and FXK-V07-C026) L2445–2446 | — | — |

In ledger version 1.16 (3,510 lines) the table's closing paragraph is followed by the version's change note (L2450); the "Person-level qualification" heading stands at L2452, the dated correction note in the 高根やす子 entry at L3034 and the qualification table's heading at L3484. The remaining line numbers of this section are those of the base file.

### 8.3 Person-level qualification section (from L2416 at the base)

Entries are bullet items, not headings; each carries per-volume update sub-bullets. Start lines at the base (the six FXK-SYN-C rows inserted after L2412 shift every line below by six):

| Entry | Line |
| --- | ---: |
| 福賀くるみ (Fukuga Kurumi), with V02–V10 updates (V10 update L2644) | 2420 |
| 小金萌智子 (Kogane Mochiko), V02–V10 updates | 2663 |
| あふぃちゃん / 高根やす子 (Takane Yasuko), V02 update naming her at L2875 | 2867 |
| Mother (unnamed until V06: 福賀梢 / Kozue, V06 update L3014) | 2998 |
| Father (unnamed; 郁夫 INFERENCE HIGH from V06, update L3063) | 3040 |
| 優子 (Yūko) | 3089 |
| 芽吹 / 山師芽吹 (Yamashi Mebuki), eligible from V02 (L3103) | 3101 |
| Mebuki's mother (unnamed) | 3238 |
| Mebuki's father (unnamed) | 3258 |
| 健斗 (Kento), Mebuki's brother | 3267 |
| 山口さん | 3276 |
| Minor figures V02, V03, V04 | 3287, 3289, 3292 |
| Mochiko's family and the bespectacled man (V05 flashback): mother L3300, the bespectacled man L3303, paternal grandmother L3308 | 3299 |
| Minor figures V05 (with 毒島☆寿美 and 増尾先生), V06, V07, V08 | 3315, 3322, 3329, 3336 |
| 酒田いなご (Sakata Inago), new in V09; V10 update L3355 | 3344 |
| 善波なな (Zenba Nana), new in V09; V10 update L3374 | 3368 |
| 月森きずな (Tsukimori Kizuna), new in V09; V10 update L3401 | 3395 |
| Minor figures V09, V10 | 3419, 3428 |
| "V01–V10 qualification (FXK-SYN-20261123-V01-V10)": the qualification table, appended in the G2 transaction after the last line (L3438 at the base) | — |

Entries that need care in retrieval: the 山口さん entry (L3276) records "does not appear" for V07, while the V07 minor-figure entry (L3329) holds the convenience-store worker whom FXK-V08-C073 and FXK-V09-C063 identify as 山口さん; several entries open with a V01 "Not eligible" line above a later "now eligible" update (Mebuki L3101; 優子 L3089). Append-only order is correct; the qualification table states the current state and subject IDs (FXK-P001–FXK-P021).

### 8.4 Concordance of forecasts carried to the next volume

A carried forecast reads "OPEN (Vnn+1)" or "OPEN (next admitted volume)" in its own row for ever; its disposition is a separate row in the next volume. Every disposing row links back to the original ("links F0nn", sometimes without the volume prefix, or "linked FXK-Vnn-Fnnn"), but no original row points forward. Checked by script on the base ledger:

| Original rows (volume, IDs) | Disposed in | Count |
| --- | --- | --- |
| FXK-V01-F045–F050 | FXK-V02-F015–F020 | 6 |
| FXK-V02-F075–F087; F122–F127 | FXK-V03-F014–F026; F027–F032 | 19 |
| FXK-V03-F086–F098 | FXK-V04-F016–F028 | 13 |
| FXK-V04-F082–F090 | FXK-V05-F016–F024 | 9 |
| FXK-V05-F101–F110 | FXK-V06-F019–F028 | 10 |
| FXK-V06-F103–F112; F177–F189 | FXK-V07-F018–F027; F028–F040 | 23 |
| FXK-V07-F084–F094; F159–F173 | FXK-V08-F018–F028; F029–F043 | 26 |
| FXK-V08-F101–F116; F196–F212 | FXK-V09-F017–F032; F033–F049 | 33 |
| FXK-V09-F115–F129; F157–F176 | FXK-V10-F018–F032; F033–F052 | 35 |

Total 174 carried rows, all disposed. One further row is carried differently: FXK-V03-F082 (F09-2) stays literally "UNRESOLVED / OPEN at main exit" for V03 and was carried as V03-MX-1 (FXK-V03-F086), scored as FXK-V04-F016. Eight rows are genuinely OPEN inside their own volume, with labelled alternatives and no later disposition: FXK-V06-F082; FXK-V08-F010, F030, F037, F048, F064, F128, F148. The V10 rows read NOT SCOREABLE exactly at FXK-V10-F101–F103, F106–F107 and F132–F146. Freeze labels (F01…F13, MX-n, "F09-2") repeat across volumes; only IDs are unique.

### 8.5 Size of the ledger after the G2 transaction

The G2 transaction appends six FXK-SYN-C rows and the qualification table, and changes the version line. The ledger moves from 859,614 bytes and 3,438 lines to 868,518 bytes and 3,472 lines (8,904 bytes added, of the synthesis's 60,000-byte budget; ANALYST COUNT), under the 1,000,000-byte threshold of the size rule (role-gap audit, section 2.5).

## 9. Proposed corrections

No accepted reading or ledger statement misstates a page fact in a way that changes a governing thesis. The reconciliation found three kinds of defect: frozen or accepted statements that later accepted records have already corrected (items 1, 2, 4); records whose state was not updated when a later volume bore on them (items 6–8, 10, 13, 17); and statements whose basis, wording or certainty a synthesis must not reuse (items 3, 11, 12, 14, 15, 16). No reading, checkpoint, entering state, erratum or register entry is edited by this audit. Every route below is a synthesis ledger record already written (FXK-SYN-C001–C006), a record routed to G3, a usage rule for G3–G5 prose, or a decision for the coordinator.

| # | Statement and locator | Evidence | Assessment | Route |
|---|---|---|---|---|
| 1 | Kurumi is "a second-year" after April 2014: V02 entering state (end of May 2014); V03 entering state (July 2014); V02 reading §B. The V03 and V04 readings' §P label her "Kurumi (20)" at 31 October and early November 2014, and the ledger's V02–V04 person headers say "age 20", though no age caption is printed in V02–V04 | V01 i0040 dates the "(20)【大学二年生】" caption 14 February 2014; the 平成24年度 orientation (V05 i0042–i0044) makes her a third-year from April 2014; by the captions (15 on 24 October 2008, V01 i0008; 20 on 14 February 2014, i0040; 23 on 3 April 2017, V09 i0152) her birthday falls between 4 April and 24 October 1993 (ANALYST CALCULATION) | Already corrected by FXK-V05-C064 and FXK-V05-C046 (V04-U03 RESOLVED). Mebuki's "20" in the ledger headers V03–V08 is carried from V02 i0004, not printed again. All three friends are third-years in 2014 | None for the frozen files; no ledger row is wrong. Usage rule: third-year from April 2014; "20 or 21" from 4 April to 24 October 2014; 21 from 25 October 2014; 23 in April 2017; Mebuki "20 at V02 i0004" |
| 2 | "106.382 … a transposition" (V04 entering state; from V03 §F.6 item 2, FXK-V03-C020) | V04 i0144: +4,729,000 at 115.840 is exact for 106.382 on 50枚 | Already downgraded by FXK-V04-C038; V04-U01 OPEN | None. Usage rule: cite both averages and the open obligation (sections 3.4 b, 4.4) |
| 3 | The V05 reading's §F preamble, §F.1 row 12, E059 and counterreading L.5 cite the V05 bonus strip (i0165, paratext) for "printed P/L excludes swap" and "short-term charts are altered for drama"; the V06 entering state repeats the chart point; ledger FXK-V05-C032 records the use as "method only"; the register's V05 extras row says "used only as method paratext" | Paratext is classification-only; the chart convention is supported by the pages (section 4.1) | A basis error of method, not a factual error; no accepted reconstruction depends on the strip | Written: FXK-SYN-C003 (section 5.6). For the coordinator: whether the V05 reading should carry a revision note on §F, and whether the register row needs a note. Usage rule: the +10円 residual is never explained by the strip |
| 4 | V04 reading §F.6 item 12 and §F.7 (and §Q, claim C016, §P; V04 checkpoint C-12): the 25× maximum "is printed only for Yasuko's account, V03 i0007" | V01 i0075 prints the domestic cap "証拠金25倍まで" | Already recorded by the V05 checkpoint (V04-U02 row), without editing V04 | None further; the synthesis cites both V01 i0075 and V03 i0007, never asserts a 25× rule for Kurumi's broker, and treats her ≈29.9× as a tension, not as proof of an overseas account |
| 5 | The register's class for under-jacket boards varies by volume (section 1.3) | Both classes are non-evidence | Record-level observation, not a defect | None |
| 6 | V01's competing thesis had no ledger row and no transition (section 5.4 a) | V01 §D; FXK-V01-C017 | Omission | Written: FXK-SYN-C006 (registration, OPEN); its standing argued in the integrated synthesis |
| 7 | Carried states left stale by blanket "PRESERVE (no material change)" lines: FXK-V02-C002, FXK-V03-C002, FXK-V04-C002, FXK-V01-C006; and, with them, the governing theses FXK-V03-C001 and FXK-V04-C001 (section 5.4 b–d) | V06 i0013, i0046; V07 i0118; V05 i0144–i0146; V06 i0039, i0051–i0053; V07 i0017–i0019 | Omission; the evidence is in the readings, filed under other claims | Written: FXK-SYN-C004 (V02-C002 outcome strand DOWNGRADE) and FXK-SYN-C005 (V01-C006 STRENGTHEN). Routed to G3 and written at G3 integration: the two V03/V04 pairs together (Study B, strand iv) and the V02-C002 agency strand (Study C); OPEN pending G3 |
| 8 | FXK-V01-C007 (the 「FXトレード日誌」 is the mother's) left at INFERENCE MODERATE-HIGH (section 5.4 e) | V06 i0065, i0079, i0090, i0093–i0095 | Stale state | Written: FXK-SYN-C001 (STRENGTHEN to OBSERVATION HIGH) |
| 9 | Practice note: from V06 the readings' §M tables close with a blanket PRESERVE line, and the ledger carries transition rows for only part of each table (section 5.1) | Counts in 5.1 | Items 7–8 arose this way | For successors: name each claim a volume bears on rather than rely on a blanket line; every FXK-SYN-C row names the last explicit transition (role-gap audit, section 2.6) |
| 10 | Obligation rows left unchanged by blanket "no bearing" lines although a later page bears on them: V02-U05, V02-U06, V03-U08, V06-U09 (section 7.3) | As listed in 7.3 | Omission in the obligation record; no claim is wrong | Working notes for G3; a synthesis record only where an integrated-synthesis argument relies on the advanced status |
| 11 | V04 reading §D.1: "her own borrowed-money win is thrown back at her" | The V01 reading's L.5 classifies the act as an unconsented, concealed use of family savings with repayment intent; the V03 checkpoint (C-11) forbids calling it "borrowing" as fact; 借金 is the characters' word (V03 i0104 Mochiko's inference; V04 i0072 Mebuki; V04 i0074 Kurumi) | Wording drift in the analyst's voice; no page fact misstated | None for the reading. Usage rule: the V01 L.5 classification in the synthesis's own voice; 借金 only as a named speaker's word |
| 12 | Certainty overstated in accepted summaries: V06 reading §P and V07 reading §B ("Mochiko … flat since 8 December"); V08 reading §D.1 ("the last 1,000,000 — the V03 tax reserve") | V06 checkpoint C-12 lowered the chronology to INFERENCE MODERATE (it rests on her self-report "ノーポジ"; close time unprinted); V07 checkpoint C-04: whether she held a position on 15 January is not shown (FXK-V07-C075; V07-U15); V08 E001 grades the tax-reserve identity INFERENCE MODERATE-HIGH | Summaries state as fact what the body grades as inference | None for the readings. Usage rules in section 4.11 |
| 13 | FXK-V01-C011 and the other chains of section 5.5 have REVISE rows without a revised wording | Ledger rows named in 5.5 | Retrieval defect, not a conflict | The 5.5 wordings are retrieval statements in this audit; a row is written at G3 integration only where a study or the integrated synthesis changes a chain's grade or scope (role-gap audit, section 2.4 b) |
| 14 | Person-section and episode rows whose wording a synthesis must not reuse: a clinical-sounding phrase for Kurumi's chart-checking (ledger, Kurumi entry, opening line); the headings "Mother (unnamed)" and "Father (unnamed)"; the 山口さん entry's V07 line "does not appear"; FXK-V01-D005, which transcribes the caption stating how Kozue died | Verified at the cited lines | Append-only records; none is false as a dated record, but each would mislead if quoted as current or reproduced | No edit. The qualification table carries the names, the merged 山口さん identity and the current outcomes; usage rules: "repeated chart-checking (commute, work, walk home)"; the V01 death described as suicide without the caption's detail in any published synthesis or monograph |
| 15 | The V01 reading §D cites the writer's flap note for the series' origin and refers to the writer with a gendered pronoun | SYN_COMMON and handoff §15: real persons by name, role or they/them; paratext classified only, authorial statements about the work not summarized. No other gendered pronoun for either creator was found in the corpus | A named-subject defect in an accepted reading; the sentence says the note "carries no weight", so no thesis depends on it | For the coordinator and the owner: a reading revision note or an erratum; the synthesis never repeats the flap's origin story or the pronoun |
| 16 | FXK-V01-F029 carries no outcome word ("QUALIFIED" only) | Ledger: the first clause occurred; the condition (Mochiko learns of the household money) never triggered | Record-level gap; no tally depends on it | Usage note in section 6.1; for the coordinator, an erratum line if the errata carrier is reopened for other reasons |
| 17 | FXK-V05-C063 graded the "あと300万円" basis INFERENCE MODERATE-HIGH | V06 i0096: Kurumi's own count is exact only with the V03 withdrawal counted toward the 2500万 gross target; FXK-V06-C051 had revised the claim without regrading it | Stale grade | Written: FXK-SYN-C002 (STRENGTHEN to INFERENCE HIGH; only the combination rule inferred) |

## 10. Pages re-opened for this audit

| Page | What was checked | Finding |
| --- | --- | --- |
| V01 i0030 (reading copy) | The note panel, as reference for V08 i0042 | Sheet with 「すみませんでした」, banded pen at lower right, hatched ground; caption "家に帰ると母はこれだけを書き残し" |
| V08 i0042 (reading copy) | Whether P1 redraws V01 i0030 P1 | Same composition, no caption, hand or act of writing; P4 "私も 責任取らなきゃ…" (section 7.2, V08-U05) |
| V09 i0031 (reading copy) | The childhood memory with the winged figure | A shell-gathering child ("きれいな かいがら", "ぜんぶ ひろってないもん") with the small winged figure beside her (section 5.5 row 2) |
| V05 i0161 (reading copy) and crop [330,1530,780,1730] ×2 | The beach memory and its silhouette strip | A child pitching forward, bowl and shells flying, a hatted woman reaching; no winged figure in any panel (section 7.1, V05-U23) |
| Crop V04 i0047 [400,460,620,710] ×2.5 | Yasuko's app screen | Six labels and six values; 証拠金維持率(%) 0円 (section 4.1) |

Six images for this audit across the synthesis's sessions (four reading copies, two crops). Five further pages re-opened to settle the order of subject IDs are listed in the qualification audit, section 8.

## 11. Independent work and how it was verified

The reconciliation was first written without the specialists' dossiers or the reviewer's diagnostics; those were then read in full, and each item was verified against the accepted artifacts or a re-opened page before it was adopted (ADOPT), taken with a changed label, scope or route (QUALIFY), rejected (REJECT), or left to the gate that owns it (OPEN). The table summarizes the dispositions that bear on this audit.

| Source and topic | Disposition | Landed in |
| --- | --- | --- |
| Reviewer: strength of the ten governing theses and the connecting claims (rewards of the worst process; "呪い" against innate greed; inability to cut; escalation; re-enactment; Mochiko's use of her friends; the two meanings of responsibility; the narrator as presentation; withheld warnings; debt closed and desire owned; Mebuki's V09 return) | ADOPT, each chain verified against the ledger rows; the V09 i0031 re-presentation QUALIFIED to INFERENCE MODERATE-HIGH | 5.5 |
| Reviewer: wording drift in accepted summaries (the "borrowed-money win"; the 25× sentence; "flat since 8 December"; the tax reserve stated as fact; a clinical-sounding phrase) | ADOPT, each verified at the cited reading or checkpoint line | 9 items 4, 11, 12, 14 |
| Reviewer: stale claim states (V02-C002 split; V03-C002, V04-C002) | ADOPT (found independently); "refuted" QUALIFIED to DOWNGRADE, later withdrawn by the reviewer | 5.4, 5.6, 9 item 7 |
| Reviewer: figure usage (the debt; 3,807,983; the four 300万; the 1,000,000 and the 1,005,144) | ADOPT | 4.11 usage rules |
| Reviewer: ages and school years | ADOPT, with the character specialist's ledger-header points | 9 item 1 |
| Reviewer: re-inspection findings (V05 i0161 silhouette; V08 i0042 redraw; V09 i0031) | ADOPT the observations after re-opening the pages; the V08 lean QUALIFIED (INFERENCE MODERATE; UNRESOLVED) | 5.5, 7.1, 7.2, 10 |
| Reviewer: paratext in V01 §D and V05 §F; the forecast-row cautions; the carried-forecast hazard | ADOPT; the "175 open rows" QUALIFIED (174 carried rows, all back-linked, plus FXK-V03-F082; eight genuinely open rows) | 6.1, 8.4, 9 items 3, 15, 16 |
| Character specialist: ages, Mebuki's carried "20", same-year students; Yasuko's re-funding stated as shown; Mochiko's enjoyment dated, not a trait; the V01 house frames; the death-caption caution | ADOPT (re-funding at INFERENCE HIGH) | 4.6, 5.5 row 6, 9 items 1, 14 |
| Financial specialist: per-volume figure chains | ADOPT as concordant; no conflicting figure | 4 |
| Financial specialist: the "あと300万円" basis; the 5,144 and the small flows; Kozue's 2000万 composition; the Monday screen; the V06 "30万 in 5月" curve; figures never printed | ADOPT (the 30,000 instalment QUALIFIED as a fit, not a statement) | 4.2, 4.5, 4.8, 4.10, 4.11, 5.6 C002 |
| Financial specialist: V04 i0047 ratio row | ADOPT after a crop made for this audit | 4.1, 4.11 |
| Financial specialist: "43.8 pips against 1,311,510" as unresolved | REJECT (explained by the truncated average) | 4.2 |
| Financial specialist: forecast counts for V01–V05 and the V04 head-clause alternative | QUALIFY (counts, not tallies); ADOPT the alternative as recorded, not adopted | 6.2 |
| Financial specialist: evaluations of the forecast record | OPEN (a process record; integrated synthesis limitations if wanted) | 6.1 |

## 12. Name-and-reference check (handoff contract §15.6)

- **Scope.** The introduction and section 1; the pair table of section 3; sections 4.2–4.8 (where several actors handle the same money); sections 5.2–5.6 (claims about persons); sections 7.2–7.3; section 9; this audit's closing sections.
- **Findings.** KNOWLEDGE_BOUNDARY_REQUIRED, repaired: section 4.8 used "Kozue" for V01 figures without noting that she is unnamed until V06 i0065; the concealment is now stated. KNOWLEDGE_BOUNDARY_REQUIRED, kept: the father is "the father" or "her husband", and his given name is not asserted; あふぃちゃん's naming as Yasuko is dated to V02 i0074. JUSTIFIED_ROLE_REFERENCE: the process roles (principal, financial specialist, character specialist, reviewer, coordinator, owner); "the narrator" as a presentation channel; the husband in V06-U09, where the relation is the point. Attribution checked for speech, thought and inner completion (Mochiko's V07 i0045 line kept as an unspoken inner completion; Kizuna's i0114 lines as thought; Kurumi's V05 and V06 counts as thought). No AMBIGUOUS_REFERENT, UNNECESSARY_GENERICIZATION or INCORRECT_IDENTITY_OR_ATTRIBUTION remains in the sample. The writer and the artist are referred to by role only.

## 13. Disposition of the reviewer's challenges concerning this audit

| Challenge | Point | Disposition | Where it landed |
| --- | --- | --- | --- |
| C-01 (material) | Claim stabilization routed to three gates; validation as the place of decision; "mechanical" for interpretive transitions | ADOPT, after reading initiation §9 and §5.13: transitions decidable on accepted evidence are argued here and written at G2; the rest are argued in G3; G4 decides none | 5.6; 9 items 3, 6, 7, 8, 13, 17; role-gap audit, section 2.4 |
| C-04 (material) | The consolidated wording of Mochiko's motive omitted her V07 inner account of use and skipped V04 | ADOPT, verified in the V07 reading and the ledger rows | 5.5 row 6 |
| C-05 (minor) | The STRENGTHEN of FXK-V05-C063 overlooked FXK-V06-C051 and called the change mechanical | ADOPT, verified at the ledger rows | 4.2; 5.4 g; 5.6 (FXK-SYN-C002) |
| C-06 (minor) | V05-U05 resolved as "cut twice" rather than "no stop; cut by hand" | ADOPT, verified in the V06 reading §M | 4.2; 4.11 usage rules; 5.5 row 3; 7.1 |
| C-07 (minor) | Two overstatements in the calculation assessment | ADOPT, verified in the V03 reading §F.6 item 7 and V08 E001 | 4.2 (whole-chain reading); 4.11; 4.12 |
| C-10 (minor, part) | "Kozue" for V01 figures without the concealment | ADOPT | 4.8; 12 |
| C-11 (minor) | Omissions not classified; no pointer to intended artifacts | ADOPT, after reading long-series §6 | 1.3; 1.6 |
| C-12 (minor, part) | Where a forecast aggregate belongs | ADOPT: a process record in the integrated synthesis's limitations | 6.1 |
| C-14 (minor) | Only the competing theses of V03 and V04 routed | ADOPT: each pair routed together | 5.2; 5.4 c; 9 item 7 |
| C-16 (minor) | The V04 i0047 ratio row can be settled | ADOPT after a crop made for this audit | 4.1; 4.11; 10 |
