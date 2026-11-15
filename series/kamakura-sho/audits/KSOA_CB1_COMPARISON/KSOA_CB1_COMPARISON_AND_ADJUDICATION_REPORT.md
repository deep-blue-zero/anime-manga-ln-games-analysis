---
title: "Kamakura Police Station — KSOA-CB1 independent comparison and adjudication report"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CB1_COMPARISON_AND_ADJUDICATION_REPORT
artifact_type: independent_comparison_and_adjudication_report
generation: KSOA-CB1-COMPARISON
version: "1.0"
created: "2026-11-15"
status: canonical
scope: "Overview of the blind KSOA-CB1 generation, the pre-registered comparison with KSOA-G1, the source-decided adjudication of all 129 records, the integration destinations, and the proposed publication route for the KSOA-CB1 baseline."
source_boundary: "Seven Japanese publisher EPUB witnesses KSOA-JP-V01-W01 to KSOA-JP-V07-W01 (all narrative sections); GPT corpus KSOA-G1 at 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a; KSOA-CB1 blind package frozen 2026-11-15T10:52:54Z, manifest SHA-256 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040."
canonical_home: series/kamakura-sho/audits/KSOA_CB1_COMPARISON/KSOA_CB1_COMPARISON_AND_ADJUDICATION_REPORT.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
compared_generations: [KSOA-G1, KSOA-CB1]
gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
cb1_blind_package_manifest_sha256: 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040
cb1_provenance_manifest_sha256: 52468acec6e0df4dc8fa55bac2b04330ecd10bce66c20c7bbec8110822e395ee
governing_records:
  - audits/KSOA_CB1_COMPARISON/COMPARISON_PROTOCOL.md
  - audits/KSOA_CB1_COMPARISON/COMPARISON_BASIS.md
  - audits/KSOA_CB1_COMPARISON/ADJ_A.md
  - audits/KSOA_CB1_COMPARISON/ADJ_B.md
  - audits/KSOA_CB1_COMPARISON/ADJ_C.md
  - audits/KSOA_CB1_COMPARISON/ADJ_D.md
integrated_by: INT-6
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
---

# KSOA-CB1 independent comparison and adjudication report

**Spoilers for V01–V07.** This report is the entry point to `audits/KSOA_CB1_COMPARISON/`. It summarises the records in this folder; it does not replace them. Where this overview and an adjudication differ, the adjudication governs, and where an adjudication and the Japanese witness differ, the witness governs. Character names follow the project's English order (Asumi Ogasawara 小笠原亜澄, Motoya Kitsukawa 吉川元哉). Locators are `[Vnn SEC pNNNN]` in the witness `KSOA-JP-Vnn-W01`.

Two analyses are compared:
- **GPT**: the canonical repository corpus, generation KSOA-G1, read at commit `7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a`.
- **CB1**: KSOA-CB1, an independent blind analysis of the same seven novels by Claude agents, frozen under manifest SHA-256 `35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040`. CB1 files are cited by package-relative path, for example `KSOA-CB1 05_monographs/CB1_ASUMI_OGASAWARA_MONOGRAPH.md`.

## (a) Purpose and the three-responsibility design

The comparison tests the canonical KSOA-G1 corpus against an analysis that never saw it. The aim is to find what the canonical corpus gets wrong, omits or compresses, and what it gets right that an independent reading misses. Every disputed point is decided on the Japanese text, then the corrections are carried into the canonical corpus through its authorised routes. Three responsibilities were kept apart, each in a different context:

1. **Blind reading (Context A).** Twenty-one Context A agent instances, working from a sanitized intake, produced the KSOA-CB1 package. Each volume analyst read its volume in order. The package comprises seven volume readings with freezes, character evidence and exit states; a longitudinal synthesis; a partnership study; nine monographs; a qualification record; a readiness analysis; and a claim and uncertainty inventory. They had no access to the GPT corpus (§b).
2. **Comparison (Context B reviewers, Phase 3).** After the freeze, nine comparison tasks compared the corpora under the protocol registered before unblinding, and wrote nine registers: one per volume, one for the series layer (`KCMP_SERIES_REGISTER.md`) and one for the lead characters (`KCMP_CHAR_REGISTER.md`). Together they hold 129 discrepancy records. Each register also scores the twelve protocol dimensions, checks a stratified sample of agreements against the source, logs its omission searches and proposes destinations. The registers' proposals are historical and noncurrent (`status: historical_legacy`).
3. **Reconciliation (Phase 4 adjudication, Phase 5 integration).** Four independent adjudicators (ADJ_A for V01–V03, ADJ_B for V04–V05, ADJ_C for V06–V07, ADJ_D for SERIES and CHAR) decided every record against the Japanese passage in context, never on the register's quotation alone, and never by majority, confidence, length or elegance. None of them authored either corpus or any register. Each adjudication confirms, modifies or overturns the register's disposition, assigns a priority and ends with an integration action list grouped by destination type (a)–(h). Phase 5 integrators then applied those actions to the canonical files (§i).

The adjudications, the protocol and the basis are canonical records of this comparison. The KSOA-CB1 baseline itself remains noncurrent: no CB1 statement becomes current authority except through an adjudicated, source-verified integration into the canonical corpus.

## (b) Provenance of the KSOA-CB1 blind generation

This section summarises the custodian's KSOA-CB1 blindness and provenance manifest (SHA-256 `52468acec6e0df4dc8fa55bac2b04330ecd10bce66c20c7bbec8110822e395ee`, 9,113 bytes). That manifest and the custodian's chronological log remain outside Git.

**Source witnesses.** The basis is the seven publisher EPUBs in the owner's local witness collection. The custodian verified each SHA-256 against the project witness map before extraction (2026-11-14), and the extractor verified each digest again before writing.

| Volume | Title | Witness | SHA-256 |
|---|---|---|---|
| V01 | 稲村ヶ崎の落日 | KSOA-JP-V01-W01 | `2b002b1e4854e6d72f6fc24963b50633f4f73d7a8bfcb22031f270afd49f898b` |
| V02 | 由比ヶ浜協奏曲 | KSOA-JP-V02-W01 | `d36084b9e0e5621e2d8d99577519956f69edca5b8c14999cbaf09d6fddd54f31` |
| V03 | 極楽寺逍遙 | KSOA-JP-V03-W01 | `5525f841bb853873386228416725ade9a8fd540dcb9dacc3f52fbaf284886811` |
| V04 | 竹寺の雪 | KSOA-JP-V04-W01 | `bfc818c532bec74d3d7c4344cd39e123e6996e1fe7c8c45c282f3bcb569f2341` |
| V05 | 西御門の館 | KSOA-JP-V05-W01 | `960beee524746bd39f5599f8210d5959b2a56be6a6c2ce34997ed94eec4f7e49` |
| V06 | 佐助ヶ谷の銀雫 | KSOA-JP-V06-W01 | `4851a03670c1306c0c554c6ad353ba1c88a997cde9f793a4b1628fb175764f5b` |
| V07 | 長谷の花舞 | KSOA-JP-V07-W01 | `7702b7eedd36a262998f7cc3a7e5824a5fb45380cde3fd6cd400e6a1df94daf1` |

Each volume analyst read every narrative paragraph of the 36 narrative sections in order. Both narrative images (V03 C02 el[0804], V05 C02 el[0585]) were inspected in place and classified independently; both classifications agree with the project witness map, which the analysts never saw. Covers, title pages, navigation, author biographies, promotion pages and colophons were withheld under the blind identity-minimization rule. The Drive copies of the witnesses and a full EPUBCheck were not re-verified. A structure-only check reproduced the witness map's spine counts, member roles and image ordinals.

**Permitted inputs.** The Context A intake, hashed by the custodian, held:
- the custodian's sanitized intake;
- verbatim copies of the generic novel and character-reconstruction methods;
- the Kamakura analytical method and reconstruction specification, which contain no findings;
- handoff contract §15;
- the §5.5.1 monograph standard, then pending as PR #588 and used as a nonbinding reference;
- the COTE monograph architecture, also nonbinding.

Every copied repository input came from `origin/main` at `d0019f2f149d57a9f817238a899dff9248a2ca9f`.

**Withheld until the freeze.** The seven GPT deep readings, the PR #587 reading introductions, all four cumulative ledgers, all studies and audits, the bootstrap review, the entrypoint, the unsanitized architecture and witness map, Kamakura PRs and commit messages, and the GPT working folders. No Context A agent reported opening any of them, and no brief or intake gave a path to them.

**Exposure record.**

| ID | Scope | Exposure | Effect |
|---|---|---|---|
| Model prior | All analysts | The V01 analyst declared a low-confidence prior that the two leads are childhood acquaintances, which the text confirms at [V01 C01 p0746]. No analyst recognized any plot element; one place-name guess came from morphology | Negligible; declared |
| X-01 | V02, after its exit freeze | A search scoped to V02 source descended into V02's own paratext and displayed two tokens | Immaterial: V02-internal, after closure |
| Listing-1 | V01/V02 analysts | A directory listing showed the file names of the custodian's exposure notes; no file was opened, and the folder was moved before V03 | None |
| Listing-2 | Several analysts | Listings showed earlier CB1 draft-file names (permitted prior-volume CB1 material) | None |
| Listing-3 | Asumi monograph agent | A listing showed paratext file names inside extraction-report hash lists | None |
| Custodian | Context B only | Governance reading exposed the custodian to some GPT-side metadata; none was transmitted, because every brief was templated and content-free | Not transmitted |

**Method deviations (self-reported).**
- *Post-disclosure freezes.* Some freezes were written after a disclosure inside the chunk they close, and each is labelled: V04 F-04; V05 F-09 (partly) and F-10; V06 F-07 (partly) and F-10; V07 F-07 to F-11. Two V04 disclosures fell some distance after the nearest freeze. From V05 on, final-chapter chunks were capped at 150 lines.
- *Append-only verification.* For all 71 freezes and 2 errata rows in V01–V07, the custodian confirmed that the SHA-256 of the freeze-file prefix at the logged length equals the logged digest.
- *Errata, not edits.* Phase 1 errors found later are recorded as errata in Phase 2 documents; the claim inventory consolidates 22. The Phase 1 seal (package manifest `cb1ed3ccf03a4301102152f9761a39fbf86a8aaabfdee7f98a78e123b64be2a6`, 117 files) still verifies.
- *Interruption.* An account usage limit interrupted two Phase 2 agents, which were resumed with their own saved context.

**Freeze and completion.** The blind package was frozen at 2026-11-15T10:52:54Z. Its manifest covers 150 files and has SHA-256 `35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040`. The custodian checked every 「…」 quotation in the fourteen Phase 2 documents against the ruby-normalized source before the freeze, and no genuine misquotation remained. The two lead monographs are v2.0 revisions written after blind acceptance reviews (Asumi: self-containment CONDITIONAL, fidelity REVISE; Motoya: self-containment PASS, fidelity FAIL). The v1 texts are preserved in the package, and the v2.0 texts were not re-reviewed.

**Authority and location.** The KSOA-CB1 baseline is `draft_noncurrent`, an independently authored analysis with no current authority. It is not a validated character model and assigns no capability grade. **It remains outside Git, noncurrent, pending owner authorization of the publication route proposed in §j.** Blind files are never edited after the freeze; corrections to CB1 appear only in the registers and adjudications.

## (c) Comparison basis and protocol

**Basis** ([COMPARISON_BASIS.md](COMPARISON_BASIS.md), pinned 2026-11-15T10:54:32Z). The GPT corpus is `origin/main` `7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a`, which includes the merged PR #587 reading introductions and the PR #588 monograph standard, now in force. The basis lists the blob of each of the 37 GPT files compared: the entrypoint, method, bootstrap review, four ledgers, reconstruction specification, witness map and architecture; seven audits; the seven deep readings and seven introductions; and six studies. The CB1 side is the frozen package manifest.

**Protocol** ([COMPARISON_PROTOCOL.md](COMPARISON_PROTOCOL.md), registered 2026-11-14, before any comparison).
- *Unblinding preconditions.* The GPT corpus is opened only after every blind artifact is written and the package manifest is recorded with a UTC timestamp.
- *Reading.* The GPT readings, ledgers, monographs, studies and audits are read completely, not by search excerpt.
- *Units.* Per volume: the case solution and mechanics, suspect sets, clue detectability, chronology, disclosure order, focalization, setting and institutions, and character facts. Per series: theses, motifs, stability and change, and monograph portraits. Readiness: dispositions, registers, counterexamples and limits.
- *Dimensions.* Twelve, scored qualitatively with examples. Five verdicts are reported separately: literary completeness, interpretive sophistication, source accuracy, character-reconstruction coverage and retrieval convenience. **No overall winner is issued.**
- *Records and dispositions.* Fixed record fields, and eleven dispositions (`AGREE`, `GPT_OMISSION`, `CLAUDE_OMISSION`, `GPT_COMPRESSION`, `CLAUDE_COMPRESSION`, `GPT_ERROR`, `CLAUDE_ERROR`, `BOTH_INCOMPLETE`, `INTERPRETIVE_DISAGREEMENT`, `UNRESOLVED`, `ARCHITECTURAL_DIFFERENCE_ONLY`). An omission claim requires a search of the whole other corpus.
- *Adjudication rule.* The Japanese witness decides. The adjudicator verifies speaker, focalizer, chronology and disclosure boundary; separates the established from the inferred; states the strongest competing explanation; and records residual uncertainty and dependent claims.
- *Agreement sampling.* At least one case-solution, clue, register and ordinary-life claim per volume, plus every load-bearing claim in the two lead monographs.
- *Integration principle.* Preserve source-supported findings from both corpora. Correct errors only through claim revision, errata or superseding artifacts. Never edit frozen readings. Keep one canonical portrait per character. CB1 stays identifiable, noncurrent and of limited authority.

**Adjudication priorities** (adjudication briefs):
- **P1**: a factual or attributional error in current canonical GPT material, or a misleading claim graded too confidently.
- **P2**: a material omission or compression.
- **P3**: an enrichment.
- **CB1-only**: a correction needed only on the CB1 side.

## (d) Totals across the 129 records

All counts are taken from the adjudication tables and count sections. INT-6 re-tallied them from the four §1 tables.

**Verdicts on the registers' dispositions.**

| Group | Records | CONFIRM | MODIFY | OVERTURN |
|---|---|---|---|---|
| ADJ_A (V01–V03) | 45 | 38 | 7 | 0 |
| ADJ_B (V04–V05) | 30 | 25 | 4 | 1 |
| ADJ_C (V06–V07) | 26 | 20 | 6 | 0 |
| ADJ_D (SERIES, CHAR) | 28 | 23 | 5 | 0 |
| **Total** | **129** | **106** | **22** | **1** |

The one overturn, KCMP-V04-015, went in GPT's favour. Of the modifications, ADJ_D resolved both of its interpretive disagreements toward GPT (KCMP-SERIES-005, KCMP-CHAR-008).

**Final disposition (primary dimension only).**

| Final disposition | A | B | C | D | Total |
|---|---|---|---|---|---|
| `GPT_OMISSION` | 11 | 13 | 11 | 11 | **46** |
| `GPT_COMPRESSION` | 14 | 5 | 9 | 7 | **35** |
| `GPT_ERROR` | 6 | 4 | 3 | 4 | **17** |
| `CLAUDE_ERROR` | 6 | 1 | 2 | 2 | **11** |
| `BOTH_INCOMPLETE` | 5 | 3 | 1 | 0 | **9** |
| `CLAUDE_COMPRESSION` | 3 | 1 | 0 | 0 | **4** |
| `CLAUDE_OMISSION` | 0 | 1 | 0 | 2 | **3** |
| `INTERPRETIVE_DISAGREEMENT` | 0 | 1 | 0 | 2 | **3** |
| `AGREE` | 0 | 1 | 0 | 0 | **1** |
| `UNRESOLVED`, `ARCHITECTURAL_DIFFERENCE_ONLY` | 0 | 0 | 0 | 0 | **0** |
| **Total** | 45 | 30 | 26 | 28 | **129** |

Secondary dimensions add to these. For example, ADJ_A counts `GPT_ERROR` on 10 records in any dimension, against 6 as primary. `UNRESOLVED` occurs only as a secondary dimension (the cause of the KCMP-V05-005 contradiction), and so does `ARCHITECTURAL_DIFFERENCE_ONLY` (KCMP-V03-012; the absolute-year aspect of KCMP-V05-008). An `INTERPRETIVE_DISAGREEMENT` dimension also remains on KCMP-V04-003 (salience only) and KCMP-V07-005 (calibration).

**Priority.**

| Priority | A | B | C | D | Total |
|---|---|---|---|---|---|
| P1 | 8 | 4 | 4 | 4 | **20** |
| P2 | 21 | 17 | 14 | 11 | **63** |
| P3 | 8 | 6 | 6 | 7 | **27** |
| CB1-only | 8 | 3 | 2 | 6 | **19** |
| **Total** | 45 | 30 | 26 | 28 | **129** |

Records with a combined priority are counted as each adjudication counts them. KCMP-V03-007 ("P3 + CB1") and KCMP-V04-012 ("P3; CB1-only") are counted as P3. KCMP-V07-005 ("CB1-only, GPT secondary P3") is counted as CB1-only. Several records overlap across groups and were applied once (§g). The qualification outcome is that nine characters are `QUALIFIED_PENDING` (§f).

## (e) Comparison by dimension

The table synthesises the registers' dimension tables for the nine units (V01–V07, SERIES, CHAR), as amended by the adjudications. "Stronger" means stronger on that dimension in the registers' judgment. It never implies a winner overall.

| # | Dimension | Stronger analysis | Concrete examples (adjudication IDs) |
|---|---|---|---|
| 1 | Source coverage | **CB1** in all seven volumes and at the character level; comparable at the series level | GPT names none of the following. The will's terms, the cyanide and the 伏龍 background (KCMP-V01-001, -002). The V02 kettlebell, robot arm, alarm log and spare key (KCMP-V02-001). The copied key, the residence-certificate route and every sum in V04 (KCMP-V04-001, -002, -006). The drugged champagne in V06 (KCMP-V06-001, KCMP-SERIES-004). The V07 weapon (KCMP-V07-003). GPT does integrate one scene, the V07 うるか, more fully than CB1 does. |
| 2 | Narrative reconstruction | **CB1** in every unit | CB1 gives the V03 call times 15:07 and 15:09, while GPT mislabels them (KCMP-V03-001). CB1 has a minute-level chronology for V04, while the GPT introduction moves the Hongō interview to dinner (KCMP-V04-014). The V07 introduction's "evening interval" is wrong (KCMP-V07-007). GPT's frozen readings are usually right where they speak. |
| 3 | Mystery reasoning | **Complementary.** CB1 for clue and detectability audits; GPT for evidential status and conditional inference | *CB1:* the paternity clue (KCMP-V01-003); the tuning-clue pair (KCMP-V02-005, -006); Yūko's parentage and the bracelet (KCMP-V04-003, -005); pre-reveal pointers to Eguchi (KCMP-V07-006). *GPT:* the conditional second-assailant inference (KCMP-V03-010); the prologue fall against Asumi's "thrown in" (KCMP-V05-001); the boat strike graded probable, not established (KCMP-V05-010); the V07 homicide attribution, with CB1's misuse of p0574 (KCMP-V07-005, KCMP-SERIES-002). The single overturn credits Asumi with spotting the car (KCMP-V04-015). |
| 4 | Psychological interpretation | **Comparable overall.** CB1 in V06, V07 and CHAR, and narrowly in V04; GPT slightly at the series level | *CB1:* Motoya's stated fear of reprisal and his self-curse (KCMP-V01-012); Shiina already knew of the deafness (KCMP-V02-004); Yakushiji's school-first principle (KCMP-V06-007); sober and drunk self-report kept separate. *GPT:* the "atonement" kept as Motoya's inference (KCMP-V02-011); Yuka's own agency (KCMP-V05-006); third parties' stakes. |
| 5 | Ordinary-life detail | **CB1** everywhere | Meals, venues and the judo-hall futon (KCMP-V05-009, KCMP-V06-013); Motoya's coffee (KCMP-CHAR-012). GPT's one strong instance is the V07 うるか scene. |
| 6 | Relationship modeling | **CB1** for evidence and series claims; comparable in V01, V03 and V05 | *CB1:* the V02 epilogue's intoxication and the verbatim summons (KCMP-V02-008, -009); the V06 address contest (KCMP-V06-005); the V07 finale's addressee and intoxication (KCMP-V07-002, KCMP-SERIES-003, KCMP-CHAR-007); the romance asymmetry (KCMP-CHAR-009). *GPT:* the civilian women's stakes and the audience asymmetry in V07-REL-0005; the weighting of Motoya's independent moves (KCMP-CHAR-008, resolved toward GPT). |
| 7 | Japanese-language analysis | **CB1, decisively** | Address and register censuses: V02 has no Japanese quotation in GPT (KCMP-V02-010); then KCMP-V03-006, KCMP-V04-008, KCMP-V05-007, KCMP-V07-008; Asumi's キミ, Motoya's おまえ and 僕, and Asumi's わたくし (KCMP-CHAR-001 to -004). GPT has the best single lexical argument, the 遺書/告白/告解 distinction (KCMP-V01-014, KCMP-SERIES-012). GPT also romanizes 姥ヶ谷 wrongly (KCMP-V01-015) and 恵智花 as "Kechika" (KCMP-V04-007, KCMP-SERIES-010). |
| 8 | Longitudinal synthesis | **Comparable** in most volumes; **CB1** at the series and character levels | *CB1:* a stable-versus-change table, development separated from late revelation, and the summons recurring from V01 (KCMP-V02-009). *GPT:* variable institutional reception, against CB1's overgeneralized linear licence arc (KCMP-SERIES-005, resolved toward GPT). |
| 9 | Thematic interpretation | **Comparable** in every volume and at the series level; **GPT** at the character level | GPT ties character to institutional permission and to the ethics of witness cost. GPT misses the extortion-and-silencing pattern (KCMP-SERIES-001). CB1 lacks GPT's critical reading of Ichiyō's account (KCMP-CHAR-016). |
| 10 | Operational reconstruction | **CB1** in every unit | Access route, password and alarm log (KCMP-V02-001); the shout test, the 中抜け and the distance and time bounds (KCMP-V06-002, -014); headquarters staffing and warrant sequences. One CB1 error: it says the V07 arrest "enables" the homicide search, though the search has its own warrant (KCMP-V07-005). |
| 11 | Evidence traceability | **Comparable, different modes** | *GPT:* stable IDs, horizon-bound frozen records and successor chains, but wide ranges that can give false assurance (V06 EV-0010 spans the drugging lines without mentioning them). *CB1:* paragraph locators and checked quotations, but summary layers that flatten evidential status (KCMP-V01-011, KCMP-V04-016). |
| 12 | Retrieval completeness | **CB1** for fact lookup; **GPT** for horizon-safe queries | GPT cannot answer what fell in V02 or what the V07 weapon was. A search for 恵智花's correct name fails in GPT (KCMP-V04-007). Stale ledger headers mislead (KCMP-CHAR-014). GPT can answer "what could be known at checkpoint H-nnnn". |

**Literary completeness.** CB1 is more complete in every unit, and by a wide margin in V07 and at the character level. GPT is economical and touches every scene, but drops objects, times, sums, ages and Japanese forms.

**Interpretive sophistication.** Comparable, in different modes. GPT is more integrated and more carefully calibrated. Its strengths are three-layer closure (account, official action, judgment), variable institutional reception, the "conditions of usable perception", and the ethics of disclosure. CB1 states governing and competing theses, counterreadings and falsifiers explicitly, and audits detectability more thoroughly. Interpretive disagreements are few: only three records end with that primary disposition, and ADJ_D resolved two of them toward GPT.

**Source accuracy.** Both high; the errors differ in kind. GPT's 17 primary `GPT_ERROR` records concern attribution, sequence, romanization and presentation, and they cluster in the PR #587 reading introductions (§f). CB1's 11 primary `CLAUDE_ERROR` records concern evidential status and calibration: summary layers state as fact what the text leaves inferential, one line is misread as the "strongest counterevidence", and some non-lead monograph seeds are wrong. No adjudicated record concerns a misidentified culprit in either corpus.

**Character-reconstruction coverage.** CB1, decisively. CB1 has nine monographs, voice and address censuses, conditional operational rules and a qualification record. GPT's two lead studies fall short of §5.5.1 (KCMP-CHAR-010), GPT records no qualification decisions (KCMP-CHAR-011), and its VOICE layer stops after V01 (KCMP-CHAR-014).

**Retrieval convenience.** GPT, according to the V03, V04, V06, V07 and CHAR registers. Its compact studies (about 29 KB for the character layer) and checkpoint-bounded records are easier to navigate than CB1's roughly 400 KB per late volume and 324 KB of lead monographs. The SERIES register splits this verdict: CB1 for direct fact lookup, GPT for versioned, horizon-safe retrieval.

## (f) Principal findings

### Where CB1 was right and GPT wrong or incomplete

1. **The reading introductions are the main error locus.** Six of the eight V01–V03 P1 records sit in a PR #587 introduction (ADJ_A §5). Across the series, the introductions carry the errors in KCMP-V01-004, KCMP-V02-002, -003 and -004, KCMP-V03-001 and -002, KCMP-V04-014, KCMP-V05-012, KCMP-V07-001, -002 and -007, and KCMP-SERIES-011. Several adjudications found the frozen deep readings correct, or only compressed, where the derived synopsis is wrong.
2. **An abstraction policy causes systematic loss** (ADJ_A §5). The GPT readings paraphrase agents, documents, times and Japanese forms functionally: "a later notarized will", "two timed calls", no V02/V03 VOICE rows. This keeps frozen horizon records free of later knowledge, but it leaks into the retrospective sections, the ledgers and the introductions. As a result, case mechanics (KCMP-V02-001, KCMP-V04-001, -006), chronology (KCMP-V02-013, KCMP-V05-008, KCMP-V07-007) and ordinary life cannot be reconstructed from GPT.
3. **Extortion and silencing are a recurring case structure** (KCMP-SERIES-001, P2). The extortionist is killed in V01 and V04, and kills the person who refused to pay in V05 and V07. GPT names the pattern only for V04 and V07, euphemizes V01 and V05, and its integrated synthesis files the V05 assault under "redress". The proposed series claim is `KSOA-SER-CL-0006`, graded moderate–high.
4. **The V07 finale's evidential context.** Asumi's credit to Motoya, 「こいつがいるから捜査やれる」 [V07 EPI p0144], is spoken to Sayaka, about Motoya in the third person, while 酔った二人 [p0143] shake hands. Motoya had blacked out, comes round, overhears, and blacks out again after his private vow. GPT's V07 introduction says Asumi "tells Motoya", and GPT nowhere records the intoxication (KCMP-V07-002, KCMP-CHAR-007, P1; KCMP-SERIES-003, P2). GPT discounts intoxicated speech in V01 but not here. The core claim survives, one spoken commitment and one private, but `KSOA-SER-CL-0004` is downgraded: High for occurrence, moderate as a stable commitment.
5. **The V06 alibi mechanism.** The host's sleep-inducer, the prescription testimony and the shout test are absent from GPT (KCMP-V06-001, -002, KCMP-SERIES-004). The mystery study therefore explains the alibi only abstractly.
6. **Speech and register.** GPT lacks Asumi's キミ and 元哉くん, Motoya's おまえ and its fade, Motoya's 僕 from V05 on, and Asumi's formal and audience registers (KCMP-CHAR-001 to -004). It has two VOICE rows, both for V01.
7. **The monograph standard and qualification.** The GPT lead studies are substantive, canonical, grandfathered and nonconforming under §5.5.1. Speech fails; romance and the operational profile are absent; history, preferences and relationships are thin (KCMP-CHAR-010). No qualification decisions exist (KCMP-CHAR-011). ADJ_D §2B.2 records all nine candidates as `QUALIFIED_PENDING`, each with conditions: Asumi Ogasawara, Motoya Kitsukawa, Sayaka Takigawa (滝川沙也香), Emiri Hatano (波多野英美里), Takasato Gamō (蒲生隆鄕), Yoshihisa Satomi (里見義尚), Ichiyō Wanibuchi (鰐淵一遥), Akiko Shichijō (七条晶子) and Kuniaki Yakushiji (薬師寺国昭). Four further figures remain `DEFERRED_EVIDENCE`.
8. **Mechanical and attribution errors.** 恵智花 is Echika, from the ruby at [V04 C01 p0150], not "Kechika" (KCMP-V04-007, KCMP-SERIES-010). The V06 departure-timing inference is Motoya's, not Asumi's (KCMP-V06-009). Two V05 study summaries are overstated (KCMP-V05-014).

### Where GPT was right and CB1 wrong

1. **The V07 recorded voice.** CB1 uses [V07 C04 p0574], where the menacing voice seems unlike Eguchi's, as the "strongest counterevidence" to the homicide attribution. That recording is the extortion call, and Eguchi's later reactions acknowledge the voice. CB1 also says the attribution "rests on reconstruction alone", ignoring the separate warrant, the collapse and 犯人逮捕 (KCMP-SERIES-002, KCMP-V07-005). GPT's handling (V07-H-0014, ACT-0002, CL-0004) is correct. The calibrated status is "narratively established, legally unadjudicated".
2. **Evidential-status inflation in CB1 summary layers.** In V01, "drugged", "recorded" and "arrested" go beyond the text (KCMP-V01-011). In V04, the driver's nose is called "unmistakable" against 「確定はできません」, and the incitement is graded "established" (KCMP-V04-016). Elsewhere: the V05 boat strike is graded established (KCMP-V05-010); Yakushiji's admission is extended to the colourant switch (KCMP-V06-004); and Miyazaki's retracted story is treated as fact in the Shichijō monograph (KCMP-V04-012). GPT's status vocabulary is the integration standard here.
3. **Inference discipline.** In each of these, GPT is the more source-faithful: the "atonement" is Motoya's free indirect conclusion (KCMP-V02-011); the second-assailant inference is conditional (KCMP-V03-010); Haruto's renunciation is a future declaration (KCMP-V03-014); the V03 anomaly is local, not an unresolved contradiction (KCMP-V03-008); and CB1's absolute claim that Asumi's intentions are never narrated is false (KCMP-V01-016).
4. **Interpretive contributions CB1 lacks.** The 遺書/告白/告解 audience distinction (KCMP-V01-014, KCMP-SERIES-012); the critical reading of Ichiyō's account (KCMP-CHAR-016); and the conflict between the V05 prologue's fall and the disposal of the body (KCMP-V05-001).
5. **Development claims.** CB1's linear arc of institutional licence skips its own V05–V06 rows; GPT's model of variable reception holds (KCMP-SERIES-005). CB1 under-weights Motoya's own route reasoning, interview request and taxi check (KCMP-CHAR-008). The V04 car match was Asumi's find, so GPT's attribution stands (KCMP-V04-015, OVERTURN).
6. **CB1 non-lead monograph seeds contain errors** that must be corrected before any reuse (KCMP-CHAR-015). The Shichijō monograph treats a lie as a detail; the Satomi monograph treats Motoya's inference as fact; the Gamō monograph overstates his attitude to bloodline.
7. **Both corpora wrong.** Both misorder the V03 overpainting scene: Asumi's breach of Maya's confidence and her hint come before Ichiyō states the hypothesis (KCMP-V03-002).

### The V05–V07 compression finding

GPT's deep readings shrink across the series. At the basis commit the frozen readings measure 53.6 KB (V01), 45.8 KB (V02), 37.6 KB (V03), 38.0 KB (V04), 35.8 KB (V05), 25.6 KB (V06) and 25.7 KB (V07).

The SERIES register (§7) finds that GPT's series layer is mostly economical rather than lossy. Its losses, however, cluster in V05–V07 and in cross-volume patterns, because the late readings feed the studies:
- In V05, Hani's extortion becomes "financial demand", and the assault is filed under "redress" (KCMP-SERIES-001).
- In V06, the drugged host and the shout test never reach the case ledger (KCMP-SERIES-004).
- In V07, the finale's intoxication and addressee are dropped, which inflates `KSOA-SER-CL-0004` to High (KCMP-SERIES-003).

The register calls these real evidential losses, not stylistic economy, because each one changes a series claim or its confidence.

The CHAR register (§7) finds that GPT's V05–V07 character rows keep the important structure: witness channels, discretion, witness costs and Motoya's misreading of Emiri. They lose three things: register in the private plot (Sayaka's forms toward Asumi, Asumi's あんた, the return of キミ, Motoya's 僕), context qualifiers on intimate-sounding lines, and ordinary life. With four to five CH and four to five REL rows per volume and no VOICE rows, they are adequate for case interpretation but insufficient for the speech, preference and romance responsibilities of §5.5.1.

The volume registers agree:
- V05 §7: the compression "lost genuinely useful evidence, not just words".
- V06 §7: "economical framing, lossy on evidence".
- V07 §7: GPT is "not merely more economical"; its unchecked introduction phrasing followed from the gaps.

The V04 register reports a parallel loss, so compression is not confined to V05–V07. The volume registers compare within one volume only; the cross-volume clustering is the series and character registers' finding.

## (g) Every P1 item and its disposition

Twenty records carry P1. They describe 17 distinct defects, because three pairs describe the same defect and were applied once: KCMP-V04-007 with KCMP-SERIES-010, KCMP-V02-002 with KCMP-CHAR-013, and KCMP-V07-002 with KCMP-CHAR-007. Every P1 concerns GPT material.

| ID | Final disposition | Defect (source) | Correction route |
|---|---|---|---|
| KCMP-V01-004 | `GPT_ERROR` (introduction) + `GPT_COMPRESSION` (H-0010) + `CLAUDE_COMPRESSION` | The introduction has 盛雄 and 里見貴子 "meet" at 姥ヶ谷ホテル in 1945. The priest dates their first meeting three years earlier, at 鎌倉海浜ホテル [V01 C03 p0329]. The detectives, not the priest, supply the hotel and the names [C03 p0334, p0344, p0357] | Introduction; erratum to H-0010; ledgers |
| KCMP-V01-015 | `GPT_ERROR` (low consequence) | "Ubagayatsu" against the ruby うばがや [V01 C02 p0269]; "researcher" for the facility manager [C02 p0400]; H-0006's "June 7" for a killing on the night of 6 June | Policing study; introduction; erratum |
| KCMP-V02-002 | `GPT_ERROR` | The introduction's "complaint about Asumi". Ayane files a 被害届 over the embezzlement, on condition that the promise is kept [V02 C03 p0480–p0482] | Introduction |
| KCMP-V02-003 | `GPT_ERROR` (introduction only) + `GPT_OMISSION` | The speech-to-text is the smart glasses' function [V02 C03 p0398]; Ayane only rephrases. The device is absent from the GPT corpus | Introduction; case ledger |
| KCMP-V02-004 | `GPT_COMPRESSION` + `GPT_ERROR` (introduction) | Shiina already knew of the deafness; "distressed" misreads his elation [V02 C02 p0893] | Introduction; ledgers |
| KCMP-V02-014 | `GPT_ERROR` (low consequence) | EV-0002's "rehearsal-night check": the inspection was at Friday noon [V02 C01 p0444] | Case-ledger correction row |
| KCMP-V03-001 | `GPT_OMISSION` + `GPT_ERROR` | Calls at 15:07 and 15:09, inside working hours [V03 C02 p0762]. "Shortly after work" is wrong, and Keiko asked the other party to name the time and place [C03 p0395], so the introduction's "called Takaharu to the reservoir" is wrong | Introduction; erratum; ledgers |
| KCMP-V03-002 | `GPT_ERROR` + `CLAUDE_ERROR` | Asumi's breach and hint [V03 C03 p0186–p0197] precede Ichiyō's categorical statement [p0203]; both corpora misorder the scene | Erratum; introduction; CB1 correction recorded |
| KCMP-V04-007 | `GPT_ERROR` | 恵智花 is Echika [V04 C01 p0150], not "Kechika", in the frozen reading and four ledger rows | Erratum; ledger correction rows |
| KCMP-V04-014 | `GPT_ERROR` | The introduction places the Hongō interview at dinner; it ran from 4 to 6 pm in the drawing room | Introduction |
| KCMP-V05-012 | `GPT_ERROR` | The introduction's "student friends" named by Hani. Yuka names them, as office colleagues. The coverage table says "five architects" where four are present | Introduction |
| KCMP-V05-014 | `GPT_ERROR` | The Motoya study says he asked basic questions "deliberately", but the interview was Sayaka's design. The partnership study implies an apology to Motoya; the only apology is to the room [V05 C03 p0973] | Studies |
| KCMP-V06-009 | `GPT_ERROR` (speaker attribution) | The departure-timing inference is Motoya's [V06 C02 p0525], credited to Asumi | Erratum; ledgers |
| KCMP-V07-001 | `GPT_ERROR` | The introduction calls Aonuma Kawamura's "former teacher"; they were fellow apprentices, Aonuma the senior | Introduction |
| KCMP-V07-002 | `GPT_ERROR` (introduction) + `GPT_COMPRESSION` | Addressee, intoxication and overhearing at the finale [V07 EPI p0131–p0149] | Introduction; erratum; ledgers; claim revision of `KSOA-SER-CL-0004`; studies |
| KCMP-V07-007 | `GPT_COMPRESSION` + `GPT_ERROR` (introduction), low consequence | The introduction's "evening interval" against 01:00–03:00 on 1 August; inquiry calendar and arrest time absent | Introduction; case ledger |
| KCMP-SERIES-010 | `GPT_ERROR` (low severity) | Same defect as KCMP-V04-007, applied once | As KCMP-V04-007 |
| KCMP-SERIES-011 | `GPT_ERROR` (V07 introduction only, low severity) | The introduction calls the ungendered prologue agent "He…His" | Introduction |
| KCMP-CHAR-007 | `GPT_ERROR` + `GPT_OMISSION` | Same defect as KCMP-V07-002, applied once | As KCMP-V07-002 |
| KCMP-CHAR-013 | `GPT_ERROR` | Same defect as KCMP-V02-002, applied once | As KCMP-V02-002 |

**Divergence between adjudications.** ADJ_C classifies the same V07 pronoun defect as KCMP-V07-011, `GPT_OMISSION` with a presentation dimension, at P3, and removes the error label. ADJ_D classifies it as KCMP-SERIES-011, `GPT_ERROR`, at P1 with low severity. Both require the same correction: an ungendered reference to the prologue agent in the V07 introduction. The P1 count above follows ADJ_D's classification of the series record. ADJ_C §5 also folds two trivial P1-level observations from its agreement samples into its actions: the V06 reading overstates Asumi's prompting about the news anchor, and the Motoya study gives Masaki's manpower reason to Motoya.

## (h) Unresolved and interpretive items with residual uncertainty

**Interpretive disagreements (final).**
- **KCMP-V05-006** (P3). Does Yuka's silence express her own reasons and agency, or concealment? Is "stealing" her a conjecture? Moderate.
- **KCMP-SERIES-005** (CB1-only), resolved toward GPT. With so few data points, "a trend with exceptions" and "case-dependent variation" cannot be cleanly separated. Moderate.
- **KCMP-CHAR-008** (CB1-only), resolved toward GPT. How much independent agency Motoya has. Low.
- **KCMP-V07-005** (secondary dimension). Calibration of the homicide attribution: no confession or forensic result is shown.
- **KCMP-V04-003** (residual dimension). How salient the convergence on Shichijō's maternity is to an ordinary reader.

**Unresolved cause.** **KCMP-V05-005**: Asumi's dating of the marriage contradicts three witnesses. Is it her error or an authorial slip? The contradiction is certain; its cause is open.

**Both corpora incomplete.**
- **KCMP-V01-009.** Who proposed the killing, and was the act planned or impulsive? 和枝's account is self-exculpatory, and the text never adjudicates. High.
- **KCMP-V01-013.** Do Asumi's disclosure to the priest and her chapel statement breach her promise of confidentiality? Moderate.
- **KCMP-V02-007.** GPT omits Motoya's misreading; CB1 under-credits his observation. Low.
- **KCMP-V03-003.** Suicidal ideation in the prologue and the farewell note against the police premise of luring. Moderate on the premise's weight.
- **KCMP-V03-009.** Keiko's shifting account of hardship. Moderate.
- **KCMP-V03-013.** Cues to Maya before the reveal; a half-truth that neither corpus's cue audit uses. Moderate.
- **KCMP-V04-011.** Did the incitement precede or follow Miyazaki's own decision? His withheld account opens in late March. Moderate.
- **KCMP-V04-012.** Did Akao's visit to the Shichijō house happen? It rests on a retracted story. Moderate.
- **KCMP-V05-011.** Enomoto's Tuesday statements against his Thursday admission. Moderate.
- **KCMP-V06-012.** Headquarters had not researched Yakushiji's family, and neither corpus cites the line. Level not stated.

**Other moderate residuals on confirmed records.**
- How fair the V01 paternity clue is (KCMP-V01-003).
- Whether Asumi's false legal claim was knowing (KCMP-V01-005).
- The weight of fear against care in Motoya's epilogue motive (KCMP-V01-012).
- How to classify focalized narration of Asumi's intentions (KCMP-V01-016).
- How discriminating the V02 hearing-loss cues were (KCMP-V02-006).
- Whether Satomi's first-interview praise was deliberate cover (KCMP-V02-012).
- How salient the V03 alibi-span clue is (KCMP-V03-001).
- Whether the V03 brushwork praise is an authorial loose end (KCMP-V03-008).
- Whether Asumi knew Motoya was awake at the V07 finale, and how far drink discounts the line (KCMP-V07-002, KCMP-CHAR-007).
- The thematic weight of "silencing" outside the four extortion volumes (KCMP-SERIES-001).
- How central the bluff device is to the series ethic (KCMP-SERIES-006).
- The romance asymmetry (KCMP-CHAR-009). Motoya's attraction to Asumi is "not established", with affirmative counterevidence. Asumi's attachment to Motoya stays open: six of her nineteen attachment data come while she is drinking, and none is a sober, private, unprovoked statement.
- Why Motoya's おまえ fades (KCMP-CHAR-002).
- Whether 僕's absence before V05 reflects only missing occasions (KCMP-CHAR-003).
- How far Asumi's わたくし runs (KCMP-CHAR-004).

## (i) Integration record

The orchestrator assigned these destinations. Each is applied in this change by the named integrator, from the adjudications' action lists of types (a)–(h).

| Destination | Action types | Status |
|---|---|---|
| `audits/KSOA_DEEP_READING_ERRATA.md`: new errata carrier for the frozen deep readings, one table per volume | (a) | Applied in this change by the named integrator (INT-2) |
| `readings/KSOA_V01_READING_INTRODUCTION.md` to `readings/KSOA_V07_READING_INTRODUCTION.md`: the seven reading introductions | (b) | Applied in this change by the named integrator (INT-2) |
| `KSOA_CASE_EVIDENCE_LEDGER.md`, `KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md` and `KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md`: the case, disclosure and character ledgers | (c), (d), (e) | Applied in this change by the named integrator (INT-1) |
| `KSOA_CLAIM_REVISION_LEDGER.md`: the claim ledger | (f) | Applied in this change by the named integrator (INT-2) |
| `studies/KSOA_ASUMI_OGASAWARA.md`, rewritten to v2.0 under the §5.5.1 standard | (g) and ADJ_D §2B | Applied in this change by the named integrator (INT-3) |
| `studies/KSOA_MOTOYA_KITSUKAWA.md`, rewritten to v2.0 under the §5.5.1 standard | (g) and ADJ_D §2B | Applied in this change by the named integrator (INT-4) |
| `studies/KSOA_PARTNERSHIP.md`, `studies/KSOA_INTEGRATED_SERIES_SYNTHESIS.md`, `studies/KSOA_MYSTERY_FORM_AND_CAUSALITY.md` and `studies/KSOA_POLICING_PLACE_AND_NARRATION.md`: the four studies | (g) | Applied in this change by the named integrator (INT-5) |
| `studies/KSOA_MONOGRAPH_QUALIFICATION_RECORD.md`: the qualification record | ADJ_D §2B.2, KCMP-CHAR-011 | Applied in this change by the named integrator (orchestrator) |
| `KSOA_SYNTHESIS_ARCHITECTURE.md` and `CURRENT_STATE_AND_CORPUS_MAP.md`: architecture and entrypoint | ADJ_D, KCMP-CHAR-011 | Applied in this change by the named integrator (orchestrator) |
| `audits/KSOA_CB1_COMPARISON/`: these records and this report | Record keeping | Applied in this change by the named integrator (INT-6) |

Type (h) actions, the CB1-only corrections, are not applied to the KSOA-CB1 baseline, which stays frozen. They are recorded in each adjudication's §3(h) and bind any future reuse of CB1 material, including the non-lead monograph seeds (KCMP-CHAR-015).

### Integration outcomes

This subsection is the decision trail for integration. It records what was applied, merged or declined in each destination, and where the Japanese source overrode an adjudication's wording. Row IDs written in the adjudications (for example `KSOA-V01-EV-0023`) were provisional proposals. The authoritative IDs are those assigned in the ledgers. No adjudicated action was declined.

| Destination | Applied | Merged or restructured | Source-resolved deviations and notes |
|---|---|---|---|
| Errata carrier (INT-2) | 36 type-(a) actions became 33 errata | 4 merged; 1 split | The V02 filing is a victim's report (被害届), conditional on the detectives' promise [V02 C03 p0480–0482], and is accepted by the fraud squad [p0525]. The V06 drugging is Asumi's accusation, covered only by the confession summary at [V06 EPI p0005] |
| Reading introductions (INT-2) | 22 type-(b) actions | 4 merged | In the V06 epilogue, バディ [EPI p0019] precedes the rank jab [p0021], so actions B-04 and F-03 were reordered. The V04 introduction was already at v1.2 and moved to v1.3 |
| Claim revision ledger (INT-2) | 29 type-(f) actions became 26 entries; count line 74 to 94 | 3 merged | KCMP-CHAR-010 was entered as a note, not a claim row. `KSOA-V03-CL-0001-R02` PRESERVEs probable homicide and keeps the suicidal ideation OPEN. `KSOA-SER-CL-0004-R01` DOWNGRADEs the claim to moderate–high |
| Case, disclosure and character ledgers (INT-1) | All 134 type-(c)–(e) actions (A 37, B 39, C 32, D 26); 161 rows added (53 case, 25 disclosure, 83 character) | 17 duplicates merged; rows spanning volumes split by horizon | Corrections are `-R01` rows that name the row they correct. Horizons were recomputed from locators. V04–V07 state rows use the `CH` kind. Provisional IDs were renumbered (Group D's V01 `VOICE` rows, V02 `VOICE-0008`, V03 `ADJ-0005`). Source resolutions: the V01 extortion reaches the reader only through 三村和枝's quotation [V01 C03 p0977]; the V02 clue is the pianist 椎名慶一, not "piano" [V02 C01 p0643]; "sideboard" is Asumi's word [V04 C03 p1042]; "1961" was dropped for 宮崎隆之 because [V04 C03 p0213] gives no year; no reading for 薬師寺 is attested; "Mitsuki's father" first appears at [V06 C03 p0426] |
| Asumi monograph v2.0 (INT-3) | 12 type-(g) actions and 10 KSOA-CB1-binding corrections | Address forms, methods and confidences, and the V07 credit consolidated | The V05 promise to 榎本 appears both unconditional (KCMP-CHAR-006) and in a later conditional restatement [V05 C03 p0754] (KCMP-V05-013). Both are shown, and whether she broke the confidence is left as a judgment. The 小寺 remark is an insinuation, not a bluff. Links to the new ledger rows cite adjudication IDs, since row IDs were still being reconciled. Acceptance review: 1 MAJOR and 15 MINOR defects, all fixed |
| Motoya monograph v2.0 (INT-4) | About 19 type-(g) actions | Finale context merged (KCMP-CHAR-007, -SERIES-003, -V07-002); register actions merged into KCMP-CHAR-002 and -003 | KSOA-CB1's misjudgment tallies were not carried over, as unreliable after correction. A KSOA-CB1 claim that Motoya never considers Asumi's hostility toward him is contradicted at [V06 C01 p0297]. Acceptance review: 1 MAJOR and 13 MINOR defects, all fixed |
| Four studies (INT-5) | All 20 type-(g) actions (A 5, B 4, C 6, D 5) | V07 finale (C G-07 with D); V06 drugging (C G-01 with KCMP-SERIES-004); bluffs and the V05 confidence (KCMP-SERIES-006, -CHAR-006, -V05-013) | Motoya's おまえ continues through V03, not V01 only. V05 public use cites both [V05 C03 p0842] and [p0900]. G-04's "below its cliff" became "a lane below a cliff". 宮崎隆之's withheld account concerns the accomplice, not "the instigation". Motoya's appraisal of Asumi is "qualified" only for appearance. Because C and D graded `KSOA-SER-CL-0004` differently, the studies say only "downgraded from high"; the claim ledger holds the grade |
| Qualification record, architecture, entrypoint (orchestrator) | ADJ_D §2B.2; KCMP-CHAR-011 | — | **Not applied:** the entrypoint name-reuse note proposed under KCMP-SERIES-009 (P3), which is deferred as enrichment |

**Unreconciled adjudication grading.** KCMP-V07-011 (ADJ_C, a P3 omission) and KCMP-SERIES-011 (ADJ_D, a P1 error) grade the V07 prologue "He" item differently. Both records stand. The integrators applied the substance once, and the higher grading governs any later audit.

## (j) Proposed publication route for the KSOA-CB1 baseline

**This is a proposal awaiting owner decision.** Nothing here publishes, imports or authorizes anything. The baseline stays outside Git until the owner decides.

**Precedent and rule.** §3.9.5 of `governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md` permits retrospective publication of a completed, independently frozen noncurrent generation, provided two things are in place. First, the owner must have merged an exact `frozen_generation_publications` binding into `governance/repository-controls/project-initiation-gate.json` through the reserved governance route; a binding added on the publication candidate itself has no admission effect. Second, the publication must be a byte-bound derivative whose manifest maps every original digest to its publication digest. Technical normalization must be recorded as derivative, never presented as the original freeze. The validator also requires every published Markdown file to keep `status: draft_noncurrent`, `do_not_use_as_current_authority: true`, empty supersession lists and a generation listed in the binding. The envelope must be exact: no file added, missing or altered.

**The two existing bindings.**

| Element | Silent Witch G2 | Cosmic Princess Kaguya CPK-B1-SOL61 | KSOA-CB1 (proposed) |
|---|---|---|---|
| Envelope | `series/silent-witch/10 Codex G2/` and `11 Codex G2 Comparison/` (72 files) | `series/cosmic-princess-kaguya/independent/CPK-B1-SOL61/` (16 files) | One prefix, for example `series/kamakura-sho/independent/KSOA-CB1/`. The canonical comparison stays in `audits/KSOA_CB1_COMPARISON/`, outside the envelope |
| Original identity | Frozen analytical commit and corpus tree in the original Git history | Byte-exact archival Git originals. The binding records that "the original local freeze predates exposure and the archival Git commits do not" | The original is a local SHA-256 freeze (manifest `35f7a16e…`, 150 files), with no Git commit. Following the CPK precedent, a byte-exact archival commit of the publishable originals would supply `frozen_commit`, `frozen_corpus_tree` and each `original_blob`. The binding would state that the freeze predates the archival commit |
| Comparison identity | Separate comparison commit and V1 boundary commit | Comparison commit and V1 boundary commit | `comparison_commit`: the commit that lands this folder. `comparison_v1_boundary`: `7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a`, the pinned GPT basis |
| Source boundary | `SOURCE_BOUNDARY.json` in the envelope, with its digest | `provenance/SOURCE_BOUNDARY.json`, with its digest | A `provenance/SOURCE_BOUNDARY.json` recording the seven witness digests, the blind-package and Phase 1 manifest digests and the excluded paths |
| Authorization | Owner-authorized publication of the completed freeze and comparison; original and publication digests verified for all artifacts; no source admission, authority promotion, literary correction or publication of original history | Owner-requested bounded publication, operative only after separate owner review and merge | To be written by the owner. It should grant no source admission, authority promotion, canonical correction or publication of private history |

**Proposed derivative.**
- **Exclude** the extracted source text: all of `KSOA-CB1 01_source/` (per-paragraph Japanese text and images). Also exclude the paratext the custodian holds, and the verbatim copies of repository documents in `KSOA-CB1 00_intake/verbatim/`, which already exist in the repository.
- **Include** the analytical layers: `KSOA-CB1 02_readings/`, `03_cumulative/`, `04_synthesis/` and `05_monographs/`, including the blind acceptance reviews and superseded v1 texts. Also include a path-scrubbed publication copy of the blindness and provenance manifest. Whether the custodian-authored sanitized intake, the `work/` drafts and `tools/` belong in the envelope is for the owner to decide.
- **Path-scrub** every derivative file and record each rewrite in the manifest. A scan of the frozen package at this writing found no drive-letter paths, but the custodian's own records do contain local paths. Any custodian record that is published needs scrubbing.
- **Normalize front matter** where the validator requires it, recording each change as derivative:
  - Add `supersedes: []`, `superseded_by: []` and `generation: KSOA-CB1` where missing. At this writing, 77 of the package's 90 Markdown files lack supersession lists, 4 of them having no front matter at all.
  - Convert to LF every file that contains carriage returns; at least 3 Markdown files do.
- **Review quotation density.** CB1's section notes and character-evidence files quote the source extensively. Before publication they should be checked against the repository's third-party notices and quotation limits. Excluding or abridging the section notes is one option.
- **Publish manifest and README** in the envelope, mapping each original path, blob and SHA-256 to its publication path and SHA-256, with byte counts.

The binding must be merged by the owner before any envelope file appears on a candidate branch. Until then the baseline remains outside Git as a noncurrent, independently authored analysis, and this folder cites it only as `KSOA-CB1 <package-relative path>`.

## (k) Limitations

- **Independence is by role, not by model family.** The CB1 analysts, the comparison reviewers and the adjudicators were all instances of one Claude model, in separated contexts with templated briefs. The GPT corpus came from a different provider. The source-decision rule and the requirement to state the strongest competing explanation limit, but cannot exclude, a shared model affinity.
- **Agreement checks were sampled.** They were stratified per protocol §7, not exhaustive. Omission claims depend on the recorded search terms (each register's §5).
- **CB1 acceptance is partial.** The v2.0 lead monographs were not re-reviewed after revision, and the non-lead monographs were never reviewed. CB1's "Full" coverage ratings under §5.5.1 were confirmed only structurally (ADJ_D §2B.1).
- **Integration outcomes are recorded elsewhere.** This report records adjudicated decisions and assigned destinations, not the integrated outcome. That is recorded in the orchestrator's verification report (§i).
- **Paths in the copied bodies stay as written.** The bodies are byte-preserved, so their workspace-relative paths remain. `KSOA-CB1:…` (20 occurrences in 13 files) denotes the KSOA-CB1 package root, that is `KSOA-CB1 <package-relative path>`. `comparison/…` denotes the comparison workspace whose records now live in this folder. `comparison/work/…` working notes are not in Git. None of these is a local absolute path, and none resolves in the repository.
- **Provisional IDs.** The adjudications contain proposed row IDs and anchors for the ledgers. A whole-project search for an ID will also find these records, and the ledgers' assigned IDs prevail.
- **How this overview was prepared.** INT-6 re-tallied the counts and P1 set directly from the four adjudication tables, and read the count, residual and compression sections and the entries cited for the inter-adjudication divergence. The dimension synthesis and residual inventory were also compiled from structured digests of complete readings of all nine registers and four adjudications. Read-only helper agents produced those digests under INT-6's direction.
- **The source governs.** Short Japanese quotations here were checked against the extraction lines of the source witness. The source text itself is not in Git.

## Appendix A. Folder inventory, copy record and path rewrites

Each record below was copied from the comparison workspace with its body preserved and its front matter replaced by repository-valid front matter. The new front matter carries the complete authority quartet, the project's standard fields, `source_record_sha256`, the original body digest, `copy_transformations`, `path_rewrites` and the original header verbatim (`source_record_front_matter`). Statuses: registers `historical_legacy`, `do_not_use_as_current_authority: true`; protocol, basis and adjudications `canonical`, `do_not_use_as_current_authority: false`. All have `do_not_use_as_literary_evidence: true`.

| File | Status | Source SHA-256 | Repository copy SHA-256 | Transformation beyond front matter |
|---|---|---|---|---|
| [COMPARISON_PROTOCOL.md](COMPARISON_PROTOCOL.md) | canonical | `978e97f27ed0c49bb6d724c0dfc6080a75a553617814e761998210e566f8364a` | `3e425e39dd1caed11875bb66ccab02aa0cde86523dcf274f18004d1a0afd7709` | none |
| [COMPARISON_BASIS.md](COMPARISON_BASIS.md) | canonical | `ef089aa99c8f7d1dcbdb78d05a3b55039ead224c82c318f7e500d9da30a265dc` | `c7b9b848173173dfe1de44a7129a163ca6f1adbcd9ab77bc7510658563b0124c` | none. The source had no front matter; the new front matter is followed by one blank separator line |
| [KCMP_V01_REGISTER.md](KCMP_V01_REGISTER.md) | historical_legacy | `95d14324e13490ac775fb611418b49387ec8f1253a56a56015331ce341db81ce` | `ca37bb2b781a192480278206e4fa33e5e45b1a27a563e72d2b85c03a55fdab1a` | none |
| [KCMP_V02_REGISTER.md](KCMP_V02_REGISTER.md) | historical_legacy | `7b44bb1a257cffca9ed0cedcdbdd071cb72e463bb325eb3c558af4e95d6f3192` | `1166dcf85ceedebb9f5b8e650c8be1dfe1e0b7aa3b026c9882863ebb3027d0a3` | none |
| [KCMP_V03_REGISTER.md](KCMP_V03_REGISTER.md) | historical_legacy | `28d2f4a9b19fcaed1fd65afe375770835b6221634284e064d467f39c1b8cf7d9` | `e7d55a8b0b6b3c7f0b30ec6c46827b3e84420e2b4b8003a649ff4acf4abcd9d5` | none |
| [KCMP_V04_REGISTER.md](KCMP_V04_REGISTER.md) | historical_legacy | `8b7306e0eca64a53a364f938d707e40bdf764df6e0710e9b5c1db8066d6671ee` | `9e663c32aa5582c8abca64a5d45f509359190e4bd4456c0917f5645edd4ed09d` | none |
| [KCMP_V05_REGISTER.md](KCMP_V05_REGISTER.md) | historical_legacy | `f121c2caa75eaa766c720b7c51937cfad5b824eeb77badfb5d2c6dd0b95eeba6` | `45912cd773595a5951a5ef9d3664a20a523c66254309a7b98ae892bca3d74d69` | CRLF line endings (341 lines) normalized to LF, because the repository validators reject carriage returns. No other byte changed |
| [KCMP_V06_REGISTER.md](KCMP_V06_REGISTER.md) | historical_legacy | `4e911b32394fa8f1579a985fa046fa426418a113b3cc57613301dc79f75a20e0` | `1eb75b9ed0bf40991db048f41958c943f66a155b3e176ba5af1c9edb664040cb` | none |
| [KCMP_V07_REGISTER.md](KCMP_V07_REGISTER.md) | historical_legacy | `92d28984d4e6a0d125f62c5edbbac45067d0dcc57839813d6817c84040e7d0b1` | `4e728809bdd4a1b600e1633aae4efd37fab3624d21dd0c36ba0e9912cd12405f` | none |
| [KCMP_SERIES_REGISTER.md](KCMP_SERIES_REGISTER.md) | historical_legacy | `d5f0979cb7ab5045716d545d1224705491873442bf06a7d258c69790e8b1bb54` | `89676102aa1c95ab87b9c072ff722761515986c0d91294cd428f7269b525b8be` | none |
| [KCMP_CHAR_REGISTER.md](KCMP_CHAR_REGISTER.md) | historical_legacy | `91b69e40ce78687c68599176e6c12280f13bcf7fd147adcb818a256e65b1d8d8` | `dc0c4b15a353a1f4343f5ac8c03a4e1f5e2dd366addb328f538bad0651061be0` | none |
| [ADJ_A.md](ADJ_A.md) | canonical | `17018b0884d36cd313230a2b865be0dcbec8f7a4b448dba3d002a6453ed441ce` | `dfb7bc120c7b347118b00be85e335ab77cb6955f009c42b87624dc5c00650440` | 16 Markdown link targets re-based (below) |
| [ADJ_B.md](ADJ_B.md) | canonical | `f17ee5b8a965d06efa15a033887fc567e2c1ec9017f3d004d3b68a3fe77556b0` | `2fc3b159d34d55c34ce6592d0d6bcc4c0203af61cb5ef32c744ab0f908f5628a` | none |
| [ADJ_C.md](ADJ_C.md) | canonical | `998cf568e85e70f243bafbde7f034e9cc0c636e276ca57429c0f1fc4e66ce720` | `defa5d3311fcfb12a3fa2a24a4c175096375569b9706e993e31c3f24022d8f0a` | none |
| [ADJ_D.md](ADJ_D.md) | canonical | `f3ec0a4ac22189437323965678feb0c5a2dc3d966d5f8be74a02447c3946dff8` | `6ede4279d9ed31e6a99be0c752d188d4aed6734359f5ce5c937a0e89c043d630` | none |

**Local-absolute-path scan.** Every copy was scanned for drive-letter paths (a letter, a colon, then a slash or backslash), file-scheme URLs and drive-mount paths of the form slash, drive letter, slash. **No local absolute path occurs in any of the fifteen records, so no path was rewritten into the `KSOA-CB1 <package-relative path>` or `audits/KSOA_CB1_COMPARISON/<file>` forms.** The only path edits are the link re-basings below.

**Path rewrites (ADJ_A.md only).** ADJ_A §3(c) and §3(d) propose ledger rows that contain Markdown links written relative to the project root, of the form `readings/KSOA_Vnn_DEEP_READING.md#…`. From this folder those targets would not resolve, and unresolved links fail the repository audit. Each target was therefore given a `../../` prefix. It points to the same frozen reading and anchor; no other byte changed. The sixteen rewrites, by source line, are:

1. line 608: `readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0011` → `../../readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0011`
2. line 610: `readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0004` → `../../readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0004`
3. line 612: `readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0012` → `../../readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0012`
4. line 615: `readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0003` → `../../readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0003`
5. line 616: `readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0006` → `../../readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0006`
6. line 617: `readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0013` → `../../readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0013`
7. line 621: `readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0014` → `../../readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0014`
8. line 629: `readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0009` → `../../readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0009`
9. line 631: `readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0010` → `../../readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0010`
10. line 633: `readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0012` → `../../readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0012`
11. line 635: `readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0010` → `../../readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0010`
12. line 637: `readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0012` → `../../readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0012`
13. line 639: `readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0012` → `../../readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0012`
14. line 641: `readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0009` → `../../readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0009`
15. line 643: `readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0011` → `../../readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0011`
16. line 645: `readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0012` → `../../readings/KSOA_V03_DEEP_READING.md#ksoa-v03-h-0012`

The same list appears in the `path_rewrites` field of the ADJ_A copy. To recover the original body exactly, strip the `../../` prefix from these sixteen targets, or for the V05 register restore CRLF. Each result reproduces the `source_record_body_sha256` recorded in that file's front matter.

**Custodian scrub (2026-11-15, after the copy above).** The copied bodies contained 20 workspace-relative mentions of the local KSOA-CB1 working folder name, mostly locating the extracted witness text the reviewers read. To avoid publishing a local evidence location, the orchestrator replaced each mention of that folder name, followed by a slash or backslash, with the package identifier `KSOA-CB1:`. A bare mention was replaced with `KSOA-CB1`. No other bytes changed. To recover the pre-scrub body, reverse this substitution. Each affected record also declares the scrub in its own `copy_transformations` front matter. The affected files and their resulting SHA-256:

| File | SHA-256 after scrub |
|---|---|
| ADJ_A.md | `439c616baea089e411deb3467af1d5acd8abf9c55b12b57767257ee3381e192a` |
| ADJ_B.md | `07a2b5e7cbef487c07b131fd8da64a076044197d3345dbb46da79e76a15dcbc5` (also 11 whitespace-only lines reduced to empty lines; both transformations declared in its front matter) |
| ADJ_C.md | `62dbd1a6bef9be7c076444365f1203ab3984d34a49f10b30f042067c425a1033` |
| ADJ_D.md | `cfbebbe1111896449f4e1784988f68f6d1ad723928fcaadabf54d26a436f68f9` |
| KCMP_CHAR_REGISTER.md | `cd549abf1a4d22580436ded3ffc41bd4bbdbc1bd19b2662266bbb916adaf61e8` |
| KCMP_SERIES_REGISTER.md | `30249c429e9851ff5a1265475ebfc7bc1ce3fc79ed1666617f3ed9618b54748d` |
| KCMP_V01_REGISTER.md | `16fce2795ad9d82408671831b0852390c5c8da8c52df9c4dd90f4f096da43ea4` |
| KCMP_V02_REGISTER.md | `f53bbd68c199eed770a5d2df91769a99a51872f60ad2d8285a55f3d202fd0e3b` |
| KCMP_V03_REGISTER.md | `be8ad4a66506819d7a68af706937bde895c9352f05b71c30b5dbaa5a5dd3bbb4` |
| KCMP_V04_REGISTER.md | `501ad7524b51341afcdd86c74c274b3494ff9a0fe87fe411d95b77beba094918` |
| KCMP_V05_REGISTER.md | `69b6c395ada77ad43e9a39aa137754e6e9d6ab684a84dcf50a4c6e53a0de8de4` |
| KCMP_V06_REGISTER.md | `00195f80a6c9ec3218aa2350ad17dcda9510305fe93620a5e52551e057fb36a1` |
| KCMP_V07_REGISTER.md | `119b959a5d342d81408ba655b9855eb67229d86d3d51a56d5d6d2a4d5c1be3d4` |
| KSOA_CB1_COMPARISON_AND_ADJUDICATION_REPORT.md | this file (self-referential; not recorded) |
