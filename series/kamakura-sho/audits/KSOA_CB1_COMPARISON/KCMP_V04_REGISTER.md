---
title: "KCMP V04 comparative discrepancy register — 竹寺の雪"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CB1_KCMP_V04_REGISTER
artifact_type: comparative_discrepancy_register
generation: KSOA-CB1-COMPARISON
version: "1.0"
created: "2026-11-15"
status: historical_legacy
scope: "Phase 3 comparative register for V04 竹寺の雪: dimension assessment, discrepancy records, agreement samples, omission searches, transfer candidates and compression note. Its proposed dispositions are superseded in effect by ADJ_B."
source_boundary: "Seven Japanese publisher EPUB witnesses KSOA-JP-V01-W01 to KSOA-JP-V07-W01 (all narrative sections); GPT corpus KSOA-G1 at 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a; KSOA-CB1 blind package frozen 2026-11-15T10:52:54Z, manifest SHA-256 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040."
canonical_home: series/kamakura-sho/audits/KSOA_CB1_COMPARISON/KCMP_V04_REGISTER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
do_not_use_as_literary_evidence: true
proposals_adjudicated_in: audits/KSOA_CB1_COMPARISON/ADJ_B.md
authority_note: "Historical comparison record. Its proposed dispositions, priorities and destinations are superseded in effect by the adjudication; cite the adjudication for any decision."
compared_generations: [KSOA-G1, KSOA-CB1]
gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
cb1_blind_package_manifest_sha256: 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040
source_record: "comparison/KCMP_V04_REGISTER.md in the KSOA-CB1 comparison workspace (outside Git)"
source_record_sha256: 8b7306e0eca64a53a364f938d707e40bdf764df6e0710e9b5c1db8066d6671ee
source_record_bytes: 55392
source_record_body_sha256: 93a9aad2eff450d199f018105b864970bca45cc938af377717860e21e8663e1f
copy_transformations: []
path_rewrites: []
integration_date: "2026-11-15"
integrated_by: INT-6
source_record_front_matter: |
  title: "KCMP V04 comparative discrepancy register — 竹寺の雪"
  artifact_type: comparative_discrepancy_register
  status: draft_noncurrent
  do_not_use_as_current_authority: true
  gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
  cb1_basis: "BLIND_PACKAGE_MANIFEST 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040"
  author_model: "Claude Opus 5.5 (claude-opus-5-5), Phase 3 Context B comparative reviewer, task V04"
  created: "2026-11-15"
---

# KCMP V04 comparative discrepancy register — 竹寺の雪

Task V04 under `comparison/PHASE3_BRIEF.md`, the pre-registered `comparison/COMPARISON_PROTOCOL.md` and `comparison/COMPARISON_BASIS.md`. Neither corpus was modified. Work notes: `comparison/work/V04_notes.md`.

**Locators.** `C03 p1104` = section C03, witness paragraph ordinal p[1104] of `KSOA-JP-V04-W01`. GPT locators (`C03 1030–1126`) and CB1 locators (`[V04 C03 p1104]`) resolve to the same ordinals. I confirmed this on GPT EV-0002 (`C01 0304–0338`: the recorded call is p0313–0317 and 119 at 20:17 is p0330), GPT EV-0004 (`PRO 0034–0051`: the wrist stare is p0039), GPT RES-0002 (`C03 1030–1126`: the alibi is p1034, the key admission p1108, the request to accompany p1120) and CB1 `[C03 p0920]` (the ¥3m demand and the decision to kill).

**Quotation policy.** The source is a copyrighted novel. Japanese is quoted here only as short key phrases (a few characters each) and factual tokens such as names, sums and legal terms, enough to make each locator checkable. Each was verified against the extraction line.

---

## 1. Files read

### 1.1 GPT corpus (pinned commit `7d8ece76`; working-tree blob = pinned blob for every file below)

| File | Blob | Extent read | Completeness |
|---|---|---|---|
| `series/kamakura-sho/readings/KSOA_V04_DEEP_READING.md` | `c304c662ba4b` | all 251 lines | complete |
| `series/kamakura-sho/readings/KSOA_V04_READING_INTRODUCTION.md` | `3acbd652d71c` | all 54 lines | complete |
| `series/kamakura-sho/KSOA_CASE_EVIDENCE_LEDGER.md` | `9ed33ab7ef26` | header and schema l.1–39; `## V04 case evidence` l.153–182 | complete for the assignment |
| `series/kamakura-sho/KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md` | `47c8a2cacccb` | header l.1–39; `## V04 disclosure history` l.120–140 | complete for the assignment |
| `series/kamakura-sho/KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md` | `2fd1ab0763c6` | header, institutional practice and longitudinal use l.1–46; `## V04 character and institutional state` l.121–141 | complete for the assignment |
| `series/kamakura-sho/KSOA_CLAIM_REVISION_LEDGER.md` | `2021f91059f7` | header l.20–44; `## V04 claim history` l.103–120; every series row citing V04 (SER-CL-0001, -0002, -0003, -0005; l.168–180) | complete for the assignment |
| `series/kamakura-sho/audits/KSOA_V04_LONGITUDINAL_RECONCILIATION.md` | `8a420709e9bd` | all 47 lines | complete |
| Omission-discipline searches | — | all six `studies/*.md`, all seven `audits/*.md`, all readings and introductions, all ledgers; V04-bearing lines read in context (for example `audits/KSOA_PRODUCER_REVIEW_AND_RECEIVING_HANDOFF.md` l.60–72) | search plus contextual reading; terms in §5 |

### 1.2 CB1 baseline (every file below verifies `OK` against `BLIND_PACKAGE_MANIFEST.sha256`)

| File | SHA-256 prefix | Extent | Completeness |
|---|---|---|---|
| `02_readings/V04/CB1_V04_READING.md` | `1f70958fc034` | all 299 lines | complete |
| `02_readings/V04/CB1_V04_EXIT_STATE.md` | `f78a40950065` | all | complete |
| `02_readings/V04/CB1_V04_FREEZES.md` (F-01–F-09) | `4ef53a74e19a` | all 441 lines | complete |
| `02_readings/V04/CB1_V04_ENTERING_RECORD.md` | `55ab2e0b576e` | all | complete |
| `02_readings/V04/CB1_V04_CHARACTER_EVIDENCE.md` | `3714ca826c84` | Part 2 (l.269–365) complete; Part 1 rows consulted by ID (CE-016, 036, 044, 055, 079, 091, 092, 109, 193, 211, 214, 218, 219, 225, 227, 230–233) | Part 2 complete; Part 1 consulted |
| `02_readings/V04/CB1_V04_SECTION_NOTES.md` | `b212349bf509` | consulted by search (O-0046, 0047, 0072, 0075, 0102–0104, 0119, 0120, 0194, 0196, 0271) | consulted |
| `03_cumulative/CB1_SERIES_STATE_AFTER_V04.md` | `3786e53a9549` | consulted by search | consulted |
| `04_synthesis/CB1_LONGITUDINAL_SYNTHESIS.md` | `f43f158826bd` | every V04-bearing line | V04 parts read |
| `04_synthesis/CB1_CLAIM_AND_UNCERTAINTY_INVENTORY.md` | `209329dcd719` | §A.4 complete; V04 rows in §B–§D; §F errata rows touching V04 (C-04, C-08, C-09, C-10) | V04 parts read |
| `05_monographs/CB1_SHICHIJO_AKIKO_MONOGRAPH.md` | `1fe17ba17920` | §1–§9 read; remainder consulted | V04 subject; main sections read |
| `05_monographs/CB1_MOTOYA_KITSUKAWA_MONOGRAPH.md`, `CB1_ASUMI_OGASAWARA_MONOGRAPH.md`, `CB1_MONOGRAPH_QUALIFICATION_RECORD.md` | `daf6aa5cfe2f`, `628c6ed415b3`, `fd98c8fdffcc` | every V04-bearing line | V04 parts read |

### 1.3 Japanese source (`KSOA-CB1:01_source/V04/`, manifest `OK`)

PRO p0001–0051 and EPI p0001–0137 were read in full. C01 p0001–0936 was read in full; some very long paragraphs were displayed truncated, and every paragraph used below was re-read in full. Read in C02: p0001–0290, 0324–0800, 0815–0880 and 0920–1045. Read in C03: p0007–0032, 0090–0240, 0245–1136. These cover about 90% of the volume, including every scene that either corpus treats as load-bearing. Unread spans: C02 p0291–0323 (lunch on 松竹通り), p0801–0814, p0881–0919 and p1046–1072 (Zushi small talk and ramen); C03 p0001–0006, p0033–0089 (walk to 茅ヶ崎館) and p0241–0244.

---

## 2. Dimension assessment (this unit only; no overall winner)

| Dimension | Served better | Concrete example (locator) |
|---|---|---|
| Source coverage | **CB1** | Only CB1 records how Akao learned of the marriage, through a 住民票 obtained by the 行政書士 曽根昌雄 (C03 p1100; CB1 exit state §1 row 19; CE-232/233). It also records that the key was copied from Yūko's (C03 p1104) and the sums (C03 p0576–0578, p0920, p1084, p1089). The GPT corpus has none of these (KCMP-V04-001, 002, 006). |
| Narrative reconstruction | **CB1** | CB1's dated chronology (exit state §1, rows 19–32) reconstructs the evening of 10 April to the minute wherever the text gives times. GPT's horizon summaries are accurate but compressed. The GPT introduction misplaces the Hongō interview "at dinner"; it took place 4–6 pm, before dinner (C01 p0306, p0320; KCMP-V04-014). |
| Mystery reasoning | **CB1**, with GPT stronger on evidential status | CB1 froze the parentage hypothesis H-12 at C02 close, from birth-year and retirement arithmetic (FREEZES F-03). It also audits every load-bearing inference (READING §F.5). GPT never states the hypothesis before Shichijō's confession (KCMP-V04-003). GPT is better at keeping the status of evidence straight: it records that the driver identification is "the investigators' judgment" (H-0011; C03 p0441 vs p0462). |
| Psychological interpretation | **CB1** (narrowly) | GPT's "The account of loyalty" is nuanced about gratitude, conviction and care running in several directions (C03 p0762–0823, p0925–0955). CB1 matches that and adds Shichijō's decision process and diagnostic exceptions (Shichijō monograph §6–§7: C03 p0688, p0696, p0700, p0720–0721). |
| Ordinary-life detail | **CB1** | CB1 inventories meals and habits: soba at 《そば古藤》 "again" (EPI p0037), Motoya's coffee server (C01 p0735), Asumi sleeping at home in Kamakura during HQs (C03 p0025), the tea/coffee slip (C01 p0188 vs p0281). GPT records almost none. |
| Relationship modeling | **CB1** on evidence, comparable on restraint | CB1 logs directed acts: calf-kick after Motoya praises Echika (C02 p0089), hand-taking (C03 p0442), sleeve and hem tugs (EPI p0024, p0046), the デレデレ jab (EPI p0068). GPT REL-0005 is well bounded, but no GPT artifact describes the calf-kick or the jab, though both fall inside broad locator ranges (H-0006, H-0015). |
| Japanese-language analysis | **CB1** | Address forms checked across the whole volume. Motoya uses no おまえ to Asumi (only 佐竹 C01 p0893 and 吉田 C03 p0355 use it). Asumi says キミ once (C01 p0029) and 元哉くん once (C01 p0046). Shichijō's 関川洋介さん→洋介さん shift is traced. GPT has no V04 VOICE rows (KCMP-V04-008). |
| Longitudinal synthesis | comparable | GPT's midpoint audit places V04's "direct harm to a separate enabling contribution" against V02 and V03 (`audits/KSOA_V04_LONGITUDINAL_RECONCILIATION.md`, "Revisions and dependencies"). CB1 LS §3.2 and §8.2 place V04 in the hidden-parentage and renunciation patterns. |
| Thematic interpretation | comparable | GPT develops privacy versus silence and research versus byline credit (CL-0004; C01 p0767). CB1 develops image versus record, worship versus calculation, and lawful versus unlawful access to civil records (READING §D, §L; LS §5.5; C03 p1066 vs p1100). |
| Operational reconstruction | **CB1** (narrowly) | CB1 traces voluntary accompaniment → 科捜研 comparison → 横浜地裁 warrants → ordinary arrest (C03 p0470, p0611, p0983), plus police 職権 access to a 戸籍謄本 (C03 p1066). GPT INST-0002/0003 express the layered authority well but more abstractly. |
| Evidence traceability | comparable (different strengths) | GPT: stable row IDs, horizon anchors and section-range locators (for example EV-0013 `C03 0838–0973`). CB1: paragraph-level locators with verified quotations (for example `[V04 C03 p0920] ✓`). |
| Retrieval completeness | **CB1** | GPT ledgers contain no names of the scrivener, no sums and no ages. The heir's name is mis-romanized "Kechika" 17 times on 14 lines across the reading and three ledgers (KCMP-V04-007), so a search for her correct name fails in the canonical rows. |

**Five aspects, reported separately.**

- **Literary completeness.** CB1 is more complete: mechanics, figures, victim portrait, motifs, food and register. GPT is economical and covers every scene, but at higher abstraction.
- **Interpretive sophistication.** Comparable, with complementary strengths. GPT is stronger at separating levels of evidence (film world, replay and assault; admitted transfer, alleged instigation and verified absence). It also declines to over-read the streaming failure (CL-0001-R01). CB1 is stronger in prospective hypothesis competition, explicit counterreadings (READING §N) and a full detectability audit.
- **Source accuracy.** Both are high. GPT has four demonstrable defects: the name, the introduction's dinner error, the car-match attribution, and the "not yet entitled to infer" claim (KCMP-V04-003, 007, 014, 015). CB1's defects are status flattening in summary prose: the driver "unmistakable", Hachiya "renounces", the Inatori research unhedged, and Akao's hidden visit treated as fact in the monograph (KCMP-V04-012, 016).
- **Character-reconstruction coverage.** CB1 is much stronger: identity facts, address inventory, per-character Part 2, and a full monograph for Shichijō (QUALIFIED_PENDING). GPT has 14 CH/REL/INST rows and no V04 voice or identity rows.
- **Retrieval convenience.** GPT is better structured: stable IDs, horizon-bounded ledgers and cross-links. CB1 is better for fact lookup: exit-state chronology, knowledge map, and a named-person suspect table. GPT's convenience is impaired by the name error.

---

## 3. Discrepancy register

Fields follow protocol §5. "Destination" names where a change would go; no change is written here.

### KCMP-V04-001 — Locked-room endpoint: the key was a copy made from Yūko's key

- **Volume and locator.** V04 C01 p0356–0367, p0411–0414; C03 p0956–0974, p1035–1047, p1104–1108.
- **Subject.** Case mechanics (CASE-0001): how the direct actor entered and relocked the memorial.
- **GPT claim.** The access route stays open as a question about keys: "The evidence constrains access without demonstrating custody of all copies or a path into the room" (`KSOA_CASE_EVIDENCE_LEDGER.md#ksoa-v04-ev-0003`). At endpoint: "He admits providing the key" (`#ksoa-v04-ev-0014`); "Hachiya admits handing over the key" (`readings/KSOA_V04_DEEP_READING.md#ksoa-v04-h-0014`); CL-0003-R02 "admitted transfer". **Omission.** No GPT artifact states that the key was a duplicate copied earlier from Yūko's key. None records Echika's statement that every key, the spare included, was kept in the drawing room in a dial-lock case.
- **CB1 claim.** "蜂屋 … gave him a duplicate key copied from 由布子's" (`CB1_V04_READING.md` §C Day 4–5; §F.3 row "Sideboard key in a (dial-lock) key case"; `CB1_V04_EXIT_STATE.md` §1 row 23, §2 K-01; FREEZES F-08 H-24/H-25 dispositions).
- **First-pass source check.** At the reveal Asumi says the culprit used a copy of the sideboard key (C03 p1042). Echika objects that the keys, 「合鍵も含めて」, were in that room (p1040), in a 「ダイヤルロックのキーケース」 (p1044). Asumi then says Miyazaki obtained an already-copied key from an accomplice (p1046, p1054). She puts it to Hachiya that he had borrowed and copied Yūko's key in the past (「由布子さんから借りてコピー」, p1104). Hachiya answers 「鍵は俺が渡した」 (p1108). Earlier, Asumi had already suspected a copy borrowed from someone in the family (C03 p0964). The thumb-turn lock and the windows secured from inside imply entry with a key (C01 p0411–0414).
- **Difference type.** Fact; evidence coverage.
- **Counterevidence and alternatives.** The copying is Asumi's assertion ("違いますか？"). Hachiya affirms only that he handed over the key, so the provenance is an investigator finding with tacit assent, not a corroborated record. Miyazaki's own key account is withheld (C03 p0972–0974).
- **Disposition.** `GPT_OMISSION` (whole-corpus search; §5).
- **Confidence.** High.
- **Destination.** Case ledger: a revision of RES-0002 and EV-0003 (an endpoint row on key provenance and custody). Claim ledger: CL-0003 revision chain.

### KCMP-V04-002 — Akao learned of the secret marriage through a residence certificate obtained by a scrivener

- **Volume and locator.** V04 C03 p1066, p1079, p1100.
- **Subject.** Knowledge chain behind the second extortion (CASE-0002); lawful and unlawful access to civil records.
- **GPT claim.** "She supplies a theory that Akao threatened Hachiya separately" (`#ksoa-v04-h-0014`); "The second route involving Hachiya is disclosed separately" (`KSOA_CASE_EVIDENCE_LEDGER.md#ksoa-v04-case-0002`). **Omission.** Nothing says how Akao knew of a marriage that even Echika did not know about.
- **CB1 claim.** "赤尾, who had learned of the marriage through a residence certificate obtained by a shady scrivener (曽根昌雄)" (`CB1_V04_READING.md` §C; §F.2 row 曽根昌雄; §F.7 "Records"). Also CE-232 and CE-233, exit state §2 K-02, and LS §5.5, which pairs lawful and unlawful access.
- **First-pass source check.** Police obtained a 戸籍謄本 at Kamakura city hall by 「職権」 (p1066). It shows a marriage about a month and a half earlier, with a new register headed by Hachiya (p1079). Akao learned of the marriage from a 住民票 obtained by the 行政書士 曽根昌雄 under 「職務上の権限」 at Akao's request. Asumi calls the act probably illegal (p1100).
- **Difference type.** Fact; evidence coverage; also a thematic point (records access).
- **Counterevidence and alternatives.** This is Asumi's report of off-page findings. Sone's conduct and fate are not shown.
- **Disposition.** `GPT_OMISSION`.
- **Confidence.** High.
- **Destination.** Case ledger: a new EV row (Hachiya extortion route) linked to CASE-0002. Disclosure ledger: a K row for Akao's knowledge. Policing study (records and authority) for the lawful/unlawful contrast.

### KCMP-V04-003 — Detectability of Yūko's parentage before Shichijō's confession

- **Volume and locator.** V04 C01 p0578; C02 p0098, p0111, p0198, p0219, p0235, p0435, p0439–0441, p0966.
- **Subject.** Clue detectability and disclosure order.
- **GPT claim.** At H-0008 "The investigators … are not yet entitled to infer her maternity" (`KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md#ksoa-v04-d-0003`). Of the family accounts: "They contribute to the actors' biography without resolving the film's clue" (`#ksoa-v04-h-0007`). No GPT horizon before H-0013 formulates a parentage hypothesis. The mystery study's V04 row says the link from bracelet to parentage "depends on testimony disclosed late" (`studies/KSOA_MYSTERY_FORM_AND_CAUSALITY.md#what-a-reader-can-infer-before-the-solution`).
- **CB1 claim.** H-12 is frozen at C02 close (F-03, moderate confidence; raised to moderate-high at F-04): "由布子 is the daughter of 洋介 and 七条晶子". The detectability audit rates its legibility "moderate: arithmetic spread across three interviews" and comments "fair; frozen as H-12 at F-03 (moderate), F-04 (moderate-high)" (`CB1_V04_READING.md` §F.5 row 2).
- **First-pass source check.** The pieces converge before C03:
  - Yūko is 61 in 2023 (C02 p0111) and was 11 when Yōsuke died in 1973 (p0435), so she was born in 1961 or 1962.
  - Shichijō retired after the film, made in spring 1961 (C01 p0578; C02 p0198, p0219), and vanished without trace (C02 p0235).
  - Hongō never met the first wife, who died within a year of the birth (p0098).
  - Yūko took a 「乳母役の女性」 for her mother (p0441).
  - Yōsuke was deeply depressed after Shichijō vanished (hearsay, p0966).
- **Difference type.** Inference; interpretation (detectability).
- **Counterevidence and alternatives.**
  - Two reputation witnesses deny any affair (C02 p0252, p0936). Utsunomiya describes the first wife concretely (C02 p0936).
  - No character voices the link, and the text never names a pregnancy before C03 p0710.
  - GPT's "entitled" can be read narrowly as "warranted to conclude", which is defensible. Read so, the dispute is about salience and availability, not proof.
- **Disposition.** `INTERPRETIVE_DISAGREEMENT`, with diagnostic `GPT_OMISSION` (no prospective record of an available hypothesis).
- **Confidence.** Moderate-high that the hypothesis was reader-available and warranted as a hypothesis at C02 close.
- **Destination.** Disclosure ledger: a retrospective HYP/ADJ row recording availability at H-0008/H-0009. Claim ledger: a note against SER-CL-0002's V04 support. Mystery study ("What a reader can infer before the solution").

### KCMP-V04-004 — Shichijō names Hachiya as Yūko's sworn partner before the reveal

- **Volume and locator.** V04 C02 p0401–0404; C03 p0789–0807, p0996.
- **Subject.** Disclosure order; detectability of the facilitator.
- **GPT claim.** The deep reading's H-0013 summary, its two-roles analysis and the introduction do not mention the disclosure. GPT's detectability statement attributes the difficulty of the role problem to the "withheld bridge" (`#ksoa-v04-h-0014`, "Institution and form"). The passage appears in GPT only inside locator ranges, never in prose: H-0013 "C03 0652–0823" and `KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md#ksoa-v04-rel-0004` "C03 0793–0807".
- **CB1 claim.** Synopsis: "She adds that 由布子 and 蜂屋 had vowed to share their remaining years [C03 p0799–0803]" (`CB1_V04_READING.md` §C). §F.5 row "蜂屋 is the accomplice" lists it as available pre-reveal evidence. FREEZES F-07 uses it in the candidate table.
- **First-pass source check.** Shichijō says Yūko had a man with whom she had vowed to live out her last years (「誓い合った殿方」, p0799). She names 蜂屋貞一 (p0803). Motoya's narration notes that this explains his hospital visits (p0804) and recalls that Yūko was thought single (p0800; cf. C01 p0211). Hachiya is then summoned to the closed reveal (C03 p0996).
- **Difference type.** Evidence coverage; inference (detectability).
- **Counterevidence and alternatives.** A vow is not a legal marriage. The decisive register, debts and 住民票 are still disclosed only at the reveal (C03 p1066–1100), so CB1's "not fair-play in the strict sense" and GPT's "withheld bridge" both stand. The omission weakens GPT's account of how far a reader could get, not its conclusion.
- **Disposition.** `GPT_COMPRESSION` (present only as a locator; absent from the reading's evidence and detectability prose).
- **Confidence.** High on the fact; moderate on its weight for detectability.
- **Destination.** Disclosure ledger: a D row at H-0013. A reading erratum or annotation on the H-0014 detectability statement.

### KCMP-V04-005 — Asumi's identification of the bracelet as the reader's second clue

- **Volume and locator.** V04 PRO p0039–0040; C01 p0529–0551; C03 p0885–0912.
- **Subject.** Clue detectability; Asumi's material expertise.
- **GPT claim.** "Asumi notices jewelry in publicity or private images" (`#ksoa-v04-h-0004`); "pays attention to clothing and jewelry" (ibid.). The reading's detectability argument rests on the prologue alone: "The reader has a stronger early cue than the investigators because the pause and wrist are specified" (`#a-visible-secret-an-invisible-route`). EV-0004's prose covers the PRO, the disc and Torii (`KSOA_CASE_EVIDENCE_LEDGER.md#ksoa-v04-ev-0004`). The bracelet remark lies inside its locator range C01 0511–0557 but is never described.
- **CB1 claim.** Asumi singles out one thin diamond chain bracelet and names Van Cleef & Arpels. Its placement directly before the 『竹寺の雪』 poster makes it "the volume's fair-play clue" (`CB1_V04_READING.md` §E-4, §F.3, §F.5 row 1). It is "the series' fairest reader-side clue" (`CB1_CLAIM_AND_UNCERTAINTY_INVENTORY.md` CB1-CL-021). Part 2 §2.1: "its identification later matches the killer's account".
- **First-pass source check.**
  - In 洋介's 「プライベート写真」 Asumi picks out one bracelet as probably Van Cleef & Arpels (《ヴァンクリーフ＆アーペル》), white gold or platinum, with a diamond (C01 p0534, p0538). Motoya's narration notes it is a very thin chain for a man's piece (p0540). She then stops before the poster (p0541).
  - Miyazaki later names 洋介's platinum chain bracelet (プラチナチェーン). Asumi asks whether it is the Van Cleef piece; he answers 「たぶんそれだ」 (C03 p0885–0889).
  - The bracelet was on 「晶子さまの左腕」 in the final scene (p0902). It was hidden afterwards in the coat's inner pocket, and the take was used (p0912).
- **Difference type.** Evidence coverage; inference (detectability); character fact (expertise).
- **Counterevidence and alternatives.** No character links the photograph to the wrist before C03 p0902. The link is available to the reader only by juxtaposition. "Fairest in the series" is a cross-volume claim outside this task.
- **Disposition.** `GPT_COMPRESSION`.
- **Confidence.** High.
- **Destination.** Case ledger: an EV-0004 revision or a new EV row for the bracelet observation. Asumi monograph (material expertise). Mystery study detectability row for V04.

### KCMP-V04-006 — Money and inheritance mechanics reduced to qualitative statements

- **Volume and locator.** V04 C03 p0576–0580, p0760, p0920, p1079, p1084, p1089, p1104, p1114.
- **Subject.** Motive structure for both culprits.
- **GPT claim.** "a passbook showing a large withdrawal" (`#ksoa-v04-h-0012`); "verification of substantial debts"; "the possible implications of corrected maternity part of Hachiya's financial incentive" (`#ksoa-v04-h-0014`); "reported debt" (CL-0003-R02). No sums or dates appear anywhere in the GPT corpus.
- **CB1 claim.** ¥5m withdrawn on 31 March and paid in cash; ¥3m more demanded in April; Hachiya about ¥600m in debt; an estate of over ¥800m; Shichijō could take a third if a family court corrected the register; the marriage about six weeks earlier, with Hachiya as head of the new register (`CB1_V04_READING.md` §C, §F.3; `CB1_V04_EXIT_STATE.md` §1 rows 20–23, §2).
- **First-pass source check.**
  - The passbook shows 五〇〇万円 withdrawn on 三月三一日 (p0576–0578). Miyazaki first says Akao took it in cash and that he learned of a fraud on 四月五日 (p0580).
  - The real demand: 四月 another 三〇〇万 (p0920).
  - The marriage was 「およそ一ヶ月半前」, with 蜂屋由布子 on the register (p1079).
  - Hachiya's debt is 「およそ六億」; the estate is 「八億以上」 (p1084). Shichijō could take 「三分の一」 if 家庭裁判所 corrects the register (p1089).
  - Shichijō will never declare herself, so Hachiya feared 「実体のない影」 (p1114).
- **Difference type.** Fact; evidence coverage.
- **Counterevidence and alternatives.** Debt and estate figures are Asumi's reported findings, and the inheritance law is character speech within the fiction. GPT's qualitative wording is accurate, so the issue is compression, not error.
- **Disposition.** `GPT_COMPRESSION`.
- **Confidence.** High.
- **Destination.** Case ledger: EV-0011 and EV-0014 revisions, with an RES-0002 cross-reference.

### KCMP-V04-007 — The heir 恵智花 is romanized "Kechika" in canonical rows

- **Volume and locator.** V04 C01 p0150 (ruby), p0198.
- **Subject.** Character identity and retrieval.
- **GPT claim.** "Kechika" appears 13 times, on 10 lines, in `readings/KSOA_V04_DEEP_READING.md` (for example `#ksoa-v04-h-0003`). It appears twice in `KSOA_CASE_EVIDENCE_LEDGER.md` (EV-0002, EV-0006), once in `KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md` (ADJ-0002) and once in `KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md` (REL-0003). The introduction corrects it: "Echika (恵智花, rendered “Kechika” in the linked deep reading)" (`readings/KSOA_V04_READING_INTRODUCTION.md#3-current-volume-story-synopsis`). The producer review records the ruby (`audits/KSOA_PRODUCER_REVIEW_AND_RECEIVING_HANDOFF.md`, `AMBIGUOUS_REFERENT` bullet). The three ledgers, which are not frozen, were not amended.
- **CB1 claim.** 森岡恵智花 in kanji throughout; "Morioka Echika" (`CB1_V04_CHARACTER_EVIDENCE.md` §2.6); reading もりおか えちか (`CB1_MONOGRAPH_QUALIFICATION_RECORD.md`).
- **First-pass source check.** The ruby is ｜恵《え》｜智《ち》｜花《か》 (C01 p0150).
- **Difference type.** Fact (name); presentation (retrieval).
- **Counterevidence and alternatives.** None. GPT has partly identified the error itself.
- **Disposition.** `GPT_ERROR`.
- **Confidence.** High.
- **Destination.** Case, disclosure and character ledger row corrections (EV-0002, EV-0006, ADJ-0002, REL-0003). The frozen reading's erratum is already carried by the introduction; a formal reading-erratum pointer is recommended.

### KCMP-V04-008 — V04 address and register inventory absent from GPT

- **Volume and locator.** V04 C01 p0029, p0046, p0893; C02 p0035, p0575, p0581; C03 p0355, p0568, p0660, p0845; C02 p0678/0698/0756 vs C03 p0704–0731.
- **Subject.** Speech and register (leads and Shichijō/Miyazaki).
- **GPT claim.** The schema defines `VOICE` rows, but `## V04 character and institutional state` has none. V04 register appears only qualitatively ("alters her register", `#ksoa-v04-h-0013`; "shifts into specific knowledgeable language", CH-0002). `studies/KSOA_ASUMI_OGASAWARA.md#address-ordinary-life-and-felt-need` uses V04 only for the rank exchange. **Omission.** The GPT corpus does not record that Motoya never says おまえ to Asumi in V04.
- **CB1 claim.**
  - Motoya: "no おまえ to Asumi in V04 (whole-volume check: the two おまえ occurrences are 佐竹's おまえたち […] and 吉田's […])" (`CB1_V04_READING.md` §I; CE §2.2; inventory CB1-CL-110).
  - Asumi: キミ once, 元哉くん once, no 吉川くん; わたくし on formal calls (READING §K).
  - Miyazaki: わたし→俺 and あんた to Asumi (§K).
  - Shichijō: 関川洋介さん while concealing, 洋介さん after confessing (Shichijō monograph §8).
- **First-pass source check.**
  - The only おまえ tokens in V04 are 佐竹's おまえたち (C01 p0893) and 吉田's おまえ (C03 p0355); there is no お前.
  - Asumi: 「キミは」 (C01 p0029) and 「元哉くん」 (C01 p0046). Motoya: 「こいつは」 before Hongō (C02 p0035).
  - Asumi uses わたくし when introducing herself to Shichijō (C02 p0581).
  - Miyazaki: 俺 from p0568, 「あんた」 (C03 p0845).
  - Shichijō uses 関川洋介さん on Day 2 (C02 p0678, p0698, p0756) although Asumi says 洋介さん (p0680). She uses 洋介さん on Day 3 (C03 p0710, p0716, p0731).
- **Difference type.** Evidence coverage (Japanese-language).
- **Counterevidence and alternatives.** CB1's claim that おまえ was frequent in V01–V03 is cross-volume and not checked here; the CHAR task should check it. The V04 inventory itself is verified.
- **Disposition.** `GPT_OMISSION`.
- **Confidence.** High (V04 facts).
- **Destination.** Character ledger V04 VOICE rows. Motoya and Asumi monographs (speech sections). A non-lead VOICE row for Shichijō.

### KCMP-V04-009 — Identity facts and ages absent from the GPT corpus

- **Volume and locator.** V04 C01 p0070, p0111, p0152, p0583; C02 p0025, p0032, p0043, p0111, p0370, p0390–0394; C03 p0025, p0213; EPI p0074–0075.
- **Subject.** Character facts for leads and principals.
- **GPT claim.** **Omission.** A whole-corpus search found no age statement for any character in any volume.
- **CB1 claim.**
  - Asumi is 29 and came to 鎌倉署 "from 本部" a little over a year earlier. Motoya "will be 31" (`CB1_V04_CHARACTER_EVIDENCE.md` §2.1, §2.2; READING §I).
  - Victim 38, Echika 21, Yūko 61, Shichijō 88, Hongō 84, Hachiya about 55, Miyazaki 17 in 1961 (READING §C; exit state §1).
  - Asumi lives in Kamakura and sleeps at home during HQs; Motoya goes home to Yokohama (CE-162; READING §I).
- **First-pass source check.**
  - Asumi 「二九歳」 (C02 p0032); Motoya 「三一歳になります」 (C02 p0043); Asumi 本部→鎌倉署 「一年ちょっと」 (C01 p0070).
  - Akao 三八歳 (C01 p0111); Echika 二一歳 (C01 p0152); Shichijō 八八歳 (C01 p0583); Yūko 六一 (C02 p0111); Hongō 八四歳 (C02 p0025).
  - Hachiya 「五〇代なかば」 (C02 p0370, p0394); Miyazaki 一七 when he met Shichijō (C03 p0213).
  - Asumi sleeps at home because she lives in Kamakura (C03 p0025); Motoya returns to Yokohama (EPI p0074).
- **Difference type.** Fact; evidence coverage.
- **Counterevidence and alternatives.** None material. The ages of Hachiya and Utsunomiya are Motoya's estimates.
- **Disposition.** `GPT_OMISSION`.
- **Confidence.** High.
- **Destination.** Character ledger PERSON/STATE rows for V04. Asumi and Motoya monographs (identity sections).

### KCMP-V04-010 — The victim's portrait and early pointers to money and period

- **Volume and locator.** V04 C01 p0646, p0779–0802, p0833–0843.
- **Subject.** Victim characterization; early clues to the blackmail motive and the 1961 focus.
- **GPT claim.** Torii found the manuscript "conventional" and arranged a replacement writer (`#ksoa-v04-h-0005`). **Omission.** The GPT corpus does not record Torii's view that Akao did not love his subject, his "abnormal" fixation on mid-Shōwa-30s films, his haggling over royalties and reputation about money, his divorce, or that his body went unclaimed. It also omits Motoya's remark that Akao was somewhat dirty about money. A search for fixat|Shōwa|昭和|royalt|divorc|unclaimed returned nothing.
- **CB1 claim.** "赤尾 seemed not to love 洋介, was 'abnormally fixated' on mid-昭和30s films, pressed for a higher royalty" (`CB1_V04_READING.md` §C, §E-5). Also "divorced (son with ex-wife); body unclaimed" (CE §2.9). CB1 uses the fixation in H-06 and the money focus in H-07 (FREEZES F-02).
- **First-pass source check.**
  - Torii: Akao did not seem to love Yōsuke (p0784), and was 「異常にこだわって」 about mid-Shōwa-30s films (p0789).
  - He asked for even one percent more royalty (p0833) and had a reputation for pressing on fees (p0837).
  - He was divorced, and his son stayed with the ex-wife (p0841); the family refused the body (p0843).
  - Motoya: 「多少は金には汚い」 (p0646).
- **Difference type.** Evidence coverage; inference (clue).
- **Counterevidence and alternatives.** Torii is not warm toward Akao (p0780–0781, Motoya's reading), and the reputation is hearsay. The pointers are suggestive, not diagnostic.
- **Disposition.** `GPT_OMISSION`.
- **Confidence.** High on the facts; moderate on clue value.
- **Destination.** Case ledger: an EV-0004/EV-0005-adjacent EV row, or a victim PERSON/STATE row in the character ledger.

### KCMP-V04-011 — Incitement against Miyazaki's own decision: the late-March date neither corpus weighs

- **Volume and locator.** V04 C03 p0920, p0949, p0968–0974, p1104, p1108.
- **Subject.** Causal role of Hachiya (instigation vs aiding).
- **GPT claim.** "Preserve the corroborated physical alibi, the admitted assistance, the alleged encouragement and the uncertain formal disposition separately" (`#how-the-two-roles-fit`). "Asumi's account of the full inducement has more dependencies than the transfer itself" (`studies/KSOA_MYSTERY_FORM_AND_CAUSALITY.md#direct-action-enabling-action-and-knowledge`). "Instigation remains the represented investigative theory" (CL-0003-R02). GPT does not engage Miyazaki's own statement that he decided to kill at the April demand.
- **CB1 claim.** "宮崎 had already paid ¥5m and 'decided to kill' at the ¥3m demand [C03 p0920]; the incitement may have added only the key" (`CB1_V04_READING.md` §N.3). Repeated in CB1-CL-020, CB1-U-22 and LS §3.4. CB1 does not weigh p0972 against that reading. Its exit state §1 row 22 dates the withheld account to late March without connecting the two.
- **First-pass source check.**
  - Miyazaki: after the April demand he decided to kill Akao (「殺すことにした」, p0920).
  - His withheld key account opens at the end of March, in cherry-blossom time (「三月の末」, p0972). So contact relevant to the key began by late March, before the April decision.
  - Asumi alleges that Hachiya incited Miyazaki "to protect Shichijō's honour" and that she got Hachiya's involvement out of Miyazaki (p1104).
- **Difference type.** Inference; interpretation (causal weight).
- **Counterevidence and alternatives.** The withheld account (p0974) could concern only the key. Miyazaki's self-presentation (p0920, p0949) could minimize another's influence. Either way the text supports neither "incitement was decisive" nor "only the key" without that account.
- **Disposition.** `BOTH_INCOMPLETE`.
- **Confidence.** Moderate.
- **Destination.** Claim ledger: a CL-0003-R02 follow-on revision and a note against SER-CL-0001. Mystery study ("Direct action, enabling action and knowledge").

### KCMP-V04-012 — Akao's visit to the Shichijō house and the address obtained from Yūko

- **Volume and locator.** V04 C02 p0715–0719, p0764; C03 p0586, p0877.
- **Subject.** Knowledge chain (how Akao reached Shichijō's household; Yūko's role); source status of a detail inside a partly retracted account.
- **GPT claim.** "He alleges Akao cheated him after coming to interview Shichijō while she was out" (`#ksoa-v04-h-0012`). Shichijō "denies a visit by Akao" (`#ksoa-v04-h-0008`). **Omission.** GPT never says that, by Miyazaki's account, Akao got the address from Yūko, and it never reconciles Shichijō's sincere denial with the visit.
- **CB1 claim.** Exit state §1 row 19 notes that Akao "obtains 晶子's address from 由布子 (宮崎: 「訊き出したらしい」, i.e. 'apparently')", properly hedged; FREEZES F-05 H-21 has it too. But the Shichijō monograph §7 states as fact: "sincere but wrong … she was not; 宮崎 had hidden the visit [C03 p0586]". Its §4 says Akao "called at her house … 宮崎 sent him away and did not tell her". This takes a detail from Miyazaki's later-retracted fraud story as established.
- **First-pass source check.**
  - In the fraud story Miyazaki says Akao called while Shichijō and 紀江 were at hospital, and that Akao got the address from 関川由布子 (「訊き出したらしい」, C03 p0586).
  - Earlier Shichijō had said Akao did not visit: he would not know the address (C02 p0717). Motoya felt she was not lying (p0719).
  - Miyazaki later replaces the investment story with extortion (C03 p0877) without addressing the visit.
- **Difference type.** Evidence coverage (GPT); source boundary (CB1).
- **Counterevidence and alternatives.** The visit may be part of the cover story. Even so, the Yūko route is consistent with the household and Yūko knowing the address, which Utsunomiya had circulated to a few people (C02 p0764, p0979).
- **Disposition.** `BOTH_INCOMPLETE` (diagnostics: `GPT_OMISSION` of the Yūko route; `CLAUDE_ERROR` of status in the CB1 monograph).
- **Confidence.** Moderate.
- **Destination.** Case ledger: an EV-0011 annotation, plus a K row for Yūko's possible knowledge. Shichijō portrait, if the canonical corpus creates one: a character ledger REL row.

### KCMP-V04-013 — Open question: how Miyazaki knew Akao would be in the memorial that evening

- **Volume and locator.** V04 C01 p0311, p0320; C02 p0082; C03 p0972–0987, p1104.
- **Subject.** Mechanics and fair play; residual ambiguity.
- **GPT claim.** **Omission.** The GPT open-issue lists ("Open", "Closure", the audit's "Matters carried") name the exact withheld testimony, financial verification, court outcomes and estate plans. None asks how the killer knew of a viewing that Akao decided on only after 6 pm. EV-0003 and CL-0003 address entry, not timing knowledge.
- **CB1 claim.** CB1-V04-Q-22 is carried to exit: "How 宮崎 knew 赤尾's whereabouts on 10 April. Open (not addressed)" (`CB1_V04_EXIT_STATE.md` §6). §3 lists it as never explained: "how 宮崎 knew 赤尾 would be in the 記念館 after 18:00 on 10 April". It is also stated at FREEZES F-03 H-14 and F-08 "Open at C03 close".
- **First-pass source check.**
  - Akao asked to watch the film only after 6 pm (C01 p0311).
  - The dinner itself was arranged when Echika invited Hongō at the hospital the previous week (C02 p0082).
  - The reveal explains the key and the incitement (C03 p1104) but not how the schedule became known. The day of independent inquiry is summarized in a single sentence (p0987).
- **Difference type.** Evidence coverage; source boundary.
- **Counterevidence and alternatives.** The information might sit in Miyazaki's withheld account (p0972–0974). The open question is then a withheld fact, not a plot hole. Either way it is unresolved for the reader.
- **Disposition.** `GPT_OMISSION` (analytical open question).
- **Confidence.** Moderate-high.
- **Destination.** Case ledger: the RES-0002 "independently unresolved questions" field. Disclosure ledger: a K-0002 annotation.

### KCMP-V04-014 — Introduction places the Hongō interview at dinner

- **Volume and locator.** V04 C01 p0306, p0311, p0320; C02 p0078, p0163.
- **Subject.** Narrative reconstruction (evening of 10 April).
- **GPT claim.** "Akao interviewed director Hongō at dinner and asked to check something in Sekigawa's film" (`readings/KSOA_V04_READING_INTRODUCTION.md#3-current-volume-story-synopsis`). The deep reading is correct: "Akao interviewed director Hongō, then requested Taketera no Yuki" (`#ksoa-v04-h-0003`).
- **CB1 claim.** "赤尾 interviewed him in the drawing room from 4 to about 6; just after 6 赤尾 … asked to watch" (`CB1_V04_READING.md` §C; exit state §1 row 25).
- **First-pass source check.** The interview took place in the drawing room 「四時から二時間くらい」 (C01 p0306). Akao moved to the 映写室 after 6 (p0311). Hongō and Echika dined from 「六時半頃」 (p0320), and Akao was not present. Hongō confirms the meal came after the interview (C02 p0163).
- **Difference type.** Fact.
- **Counterevidence and alternatives.** None.
- **Disposition.** `GPT_ERROR` (introduction only).
- **Confidence.** High.
- **Destination.** Correction to the reading introduction (`active_provisional`).

### KCMP-V04-015 — Who matched the car on the footage to Shichijō's carport

- **Volume and locator.** V04 C02 p0508; C03 p0401–0411, p0426, p0462.
- **Subject.** Attribution of investigative contributions (partnership division of labour).
- **GPT claim.** "亜澄 recognizes a car matching one at 晶子's house, and 元哉 proposes looking for a clearer return direction" (`#how-the-two-roles-fit`). This division is reused as evidence of complementary competence: "V04 separates her recognition of a possible vehicle from Motoya's suggestion to check a clearer direction" (`studies/KSOA_ASUMI_OGASAWARA.md#from-noticing-a-difference-to-making-it-testable`; also `#ksoa-v04-ch-0004`).
- **CB1 claim.** Asumi finds the frame and Motoya contributes the opposite-direction idea (`CB1_V04_READING.md` §I Motoya; CB1 Motoya monograph §5). The synopsis says neutrally that "the camera shows 晶子's silver Suzuki Alto" (§C). CB1 does not specify who made the match.
- **First-pass source check.**
  - Asumi stops on a car (「見つけた」, p0402) and notes the plate is unreadable (p0406).
  - Motoya then names it a silver Alto (「銀色のアルト」) and says it was parked at the 七条邸 carport (p0409).
  - Motoya proposes the opposite direction (p0426). Asumi later reports the same-model point to 佐竹 (p0462).
  - The car was visible to both at C02 p0508.
- **Difference type.** Fact (attribution); presentation.
- **Counterevidence and alternatives.** Asumi's stopping on the car implies she recognized something, and she voices the match to the commander. "Recognizes" is defensible for her search. The explicit carport match, however, is Motoya's line. The GPT formulation removes one of his contributions, in a corpus that elsewhere argues for his independent contributions.
- **Disposition.** `GPT_ERROR` (minor attribution), with diagnostic `INTERPRETIVE_DISAGREEMENT` over how to divide credit.
- **Confidence.** Moderate-high.
- **Destination.** Reading erratum (two-roles paragraph). Asumi study note; Motoya monograph (contributions).

### KCMP-V04-016 — CB1 summary prose flattens attributed or judged facts into established ones

- **Volume and locator.** V04 C03 p0441, p0462, p0470; C03 p0916; EPI p0056–0059.
- **Subject.** Source status in CB1's synopsis and freezes.
- **GPT claim.**
  - "Recognition of the profile and car is the investigators' judgment, subject to comparison" (`#ksoa-v04-h-0011`).
  - "Akao's supposed research in Inatori is attributed to Miyazaki" (`#a-visible-secret-an-invisible-route`).
  - "Statements, actual transfers and legal outcomes have different statuses at cutoff" (`#ksoa-v04-h-0015`).
- **CB1 claim.**
  - "the driver's aquiline nose unmistakable" and "traced the child through 稲取" (`CB1_V04_READING.md` §C Day 3).
  - "蜂屋 renounces the inheritance" (§C Epilogue; FREEZES F-09 exit summary).
  - CB1's own exit state is more careful ("declared he will renounce", §2), and CE-218 classes the 稲取 research as ATTRIBUTED_TESTIMONY.
- **First-pass source check.**
  - The identification by the aquiline nose (「わし鼻」 … 「間違いない」, p0441) is Motoya's perception. Asumi tells 佐竹 the identification cannot be confirmed, 「確定はできません」 (p0462), and 科捜研 comparison is ordered (p0470).
  - The 稲取 inquiries are Miyazaki's 「調べまわったらしい」 (p0916).
  - Hachiya reportedly declared he would renounce the inheritance (「明言したらしい」, EPI p0056); Asumi ascribes it to wanting a lighter sentence (p0059).
- **Difference type.** Source boundary; presentation.
- **Counterevidence and alternatives.** The facts are later borne out in substance (Miyazaki confesses), and CB1's row-level classifications are mostly correct. The flattening is confined to summary prose.
- **Disposition.** `CLAUDE_COMPRESSION` (diagnostic: source boundary).
- **Confidence.** High.
- **Destination.** None in the frozen CB1. For integration: carry GPT's status wording into any canonical row built from CB1 material (case ledger EV-0010, RES-0003).

---

## 4. Agreement sample checks (protocol §7; each verified against the source)

| # | Stratum | Shared claim (GPT anchor · CB1 anchor) | Source verification | Result |
|---|---|---|---|---|
| A1 | Case solution | Miyazaki is the admitted direct killer, arrested under warrant. Hachiya's alibi is verified and he admits handing over the key. GPT `KSOA_CASE_EVIDENCE_LEDGER.md#ksoa-v04-res-0001`, `#ksoa-v04-res-0002` · CB1 exit state §2 K-01 | Miyazaki decides to kill after the April demand (C03 p0920); 横浜地裁 warrants and 通常逮捕 (p0983); alibi 「裏が取れている」 (p1034); 「鍵は俺が渡した」 (p1108); 殺人教唆及び幇助 (p1120) | AGREE |
| A2 | Clue detectability | The direct attacker is more tractable before the reveal than the facilitation, which depends on off-page records and a narrative cut. GPT `#how-the-two-roles-fit`, `#ksoa-v04-h-0014` · CB1 READING §F.5 last two rows, §G | Cut after the account begins (p0972→p0974 blank); the day of inquiry compressed into one sentence (「真相はすべて見えてきた」, p0987); register, debts and 住民票 first appear at p1066–1100 | AGREE (but see KCMP-V04-004 on the vow pointer) |
| A3 | Register / narration | Motoya's narration treats Miyazaki's fraud account as a confession beyond its words. GPT `#ksoa-v04-h-0012` · CB1 FREEZES F-05 ("implicit confession (no explicit 'I killed him' yet)"), READING §I Motoya errors | Miyazaki's words amount only to having been cheated and not forgiving it (p0568–0586); narration nonetheless calls it a confession (「自白した」, p0588) and Motoya takes it as the true motive (p0582) | AGREE |
| A4 | Register / ethics | Asumi's DNA claim is a bluff, marked as such in the narration; the search inducement leverages his protectiveness. GPT `#ksoa-v04-h-0012`, INST-0003 · CB1 READING §F.7 | narration labels it 「ハッタリ」 (p0549); main-house search offer (p0556–0560) | AGREE |
| A5 | Ordinary life | Epilogue route: soba → bars → a wine bar on 今小路 → Asumi sick on the 寿福寺 steps → neighbourhood men → taxi. GPT `#ksoa-v04-h-0015` · CB1 READING §C Epilogue | 盛りそば and 天ぷら 「今回も」 (EPI p0037); bars (p0073); 寿福寺総門前の石段 (p0082); 町内会 and a 不審者 call (p0121–0123); 「早く連れてって」 (p0127); taxi (p0136) | AGREE |
| A6 | Chronology | Recorded internal call just after seven; 119 at 20:17; death window about 19:04 to just after 20:00. GPT `KSOA_CASE_EVIDENCE_LEDGER.md#ksoa-v04-ev-0002` · CB1 exit state §1 row 25 | 七時三分 (C01 p0317); 八時一七分 (p0330); window (p0334) | AGREE |
| A7 | Setting | The film's bamboo garden was a 藤沢 grove standing in for 報国寺, with salt as snow. GPT `#ksoa-v04-h-0006` · CB1-CL-023 | a 藤沢 bamboo grove standing in for 報国寺 (C02 p0198); salt (塩) as snow (p0194) | AGREE |
| A8 | Character (Motoya) | Motoya proposes the Torii contact and the opposite-direction check, and asks to lead the first questioning. GPT `#partnership-authority-and-place` · CB1-CL-024, Motoya monograph §5 | Proposal to meet the editor (C01 p0675); 「反対方向もあるはずだ」 (C03 p0426); asks to question Miyazaki himself (p0473) | AGREE |
| A9 | Partnership | Asumi corrects Utsunomiya's rank assumption, calls the police male-centred and credits Motoya. Motoya privately recalls failing the exam she passed. GPT `#ksoa-v04-ch-0003` · CB1 READING §J, CB1-CL-056 | 「お供」 (C02 p0836); 「男性中心の組織」 (p0851); 「よい後輩」 (p0855); exam failure (p0863) | AGREE |
| A10 | Character (Shichijō) | A firm Day-2 denial of post-1961 contact, contradicted by her Day-3 confession, which the narration labels false. GPT `#ksoa-v04-h-0013` ("revises Shichijō's earlier assertion") · CB1-CL-022 | Denial (C02 p0698, p0756); confession (C03 p0704, p0716); narration 「あれは偽りだった」 (p0733) | AGREE |
| A11 | Institution | 佐竹's licence rests partly on Asumi's record. GPT `#ksoa-v04-inst-0001` · CB1-CL-025 | 佐竹 says cases have been solved from Asumi's lines more than once (「一回ではない」, C01 p0893) | AGREE |
| A12 | Media / detectability | The detectives' two stream viewings yield nothing, and the novel never performs an enhanced-disc comparison. GPT CL-0001-R01 · CB1 FREEZES P-21 "not fulfilled" | V‐NEXT (C01 p0902); station monitor TV, twice (p0911, p0934); Miyazaki invites a check that is never made (C03 p0898) | AGREE in fact. Nuance: GPT holds the cause of failure undetermined (edition, conditions or knowledge); CB1 READING §E-5 calls it a "designed failure" for lack of the PRO cue. GPT's formulation is better bounded. |
| A13 | Discovery | 服部 called the taxi; 高代 rang the 映写室, found the door locked and fetched the key; four entered. GPT `#ksoa-v04-h-0003` · CB1 READING §C | Taxi ~7:40 and Haga's call at 8:00 (C01 p0320); locked, key fetched (p0324); 服部 stayed behind (p0337) | AGREE. GPT alone notes that Echika's 「一一九番したんです」 (p0328) differs from Hongō's credit to 高代 (C02 p0175), a GPT-only nuance (EV-0002). |
| A14 | Gate camera | GPT H-0002 and the introduction cite only that the gate camera yielded no strong lead; CB1 says it "confirms the household's account" | Both are in the text: no strong information from the camera (C01 p0122), and the camera footage corroborates Echika's account (「裏づけられている」, p0338) | PARTIAL. Each side quotes one half. GPT's bounded-alibi caution (D-0001) is analytically defensible; it should cite p0338. Not logged as a record (low consequence). |

All load-bearing lead-monograph claims touching V04 that I checked were source-accurate (KCMP-V04-008, 009; A8, A9). A full audit of lead monographs is the CHAR task's.

---

## 5. Omission discipline (search terms)

**GPT corpus.** Searched the readings and introductions V01–V07, all four ledgers, `studies/*.md` and `audits/*.md` (case-insensitive `grep -rn`). Hits were read in context.

| Record | Terms | Result |
|---|---|---|
| 001 | `duplicat`, `cop(y\|ied)`, `spare key`, `from Yūko`, `borrow` | no V04 key-provenance statement |
| 002 | `曽根`, `scrivener`, `residence (certificate\|record)`, `住民票`, `行政書士`, `Sone`, `juminhyo` | none |
| 006 | `500`, `5 million`, `600`, `800`, `third`, `三分の一`, `1/3`, `¥` | none |
| 004 | `vow`, `remaining years`, `晩年`, `engag`, `0799`, `0803`, `0793` | only inside locator ranges (H-0013, REL-0004); never in prose |
| 005 | `Van Cleef`, `brand`, `platinum`, `jewel`, `bracelet` | jewelry noticed (H-0004); bracelet only via Miyazaki |
| 008 | `おまえ`, `omae`, `キミ`, `kimi`, `元哉くん`, `あたし`, `わたくし`, `watakushi` | V01 VOICE rows and generic study sentences only; no V04 voice data |
| 009 | `years old`, `aged`, `-year-old`, `歳`, digit ages with age/year/old | none |
| 010 | `fixat`, `Shōwa`, `Showa`, `昭和`, `royalt`, `money-grasp`, `divorc`, `unclaimed` | none |
| 012 | `address` and read of H-0008/H-0012 | visit recorded; Yūko route absent |
| 013 | `whereabouts`, `knew (that )?Akao`, `would be (in\|at) the`, `that evening` | none on timing knowledge |
| 003 | read every V04 horizon H-0006–H-0012 and the V04 study rows | no parentage hypothesis before H-0013 |
| 007 | `Kechika`, `Echika` | counts as given in the record |

**CB1 corpus.** Searched readings, notes, character evidence, exit states, synthesis and monographs. Each check found CB1 had the item, a gap, or a nuance:

| Check | Terms | Result |
|---|---|---|
| 119-caller attribution difference | `119`, `一一九` | CB1 has 高代 as caller (F-03) but no note of Echika's phrasing; GPT-only nuance, not logged as material |
| Edition equivalence | `V.NEXT`, `stream`, `enhanced`, `画質向上`, `edition`, `monitor`, `big screen`, `大画面` | present as prediction P-21 (FREEZES); not stated as an interpretive limit in READING; agreement A12 |
| Byline/credit theme | `byline`, `credit`, `取材協力`, `伊作久` | fact present (exit state §2), not thematized; GPT-side transfer item 5 (§6) |

No record carries `CLAUDE_OMISSION` as its primary disposition.

---

## 6. Transfer candidates (ranked)

**From CB1 to the canonical GPT corpus.**

1. Locked-room endpoint: key copied from Yūko's; household key custody (KCMP-V04-001).
2. Akao's 住民票 route through the scrivener 曽根昌雄, and the lawful versus unlawful records contrast (002).
3. Parentage detectability convergence at C02 close; revise D-0003's framing (003).
4. Shichijō's pre-reveal naming of Hachiya as Yūko's sworn partner (004).
5. Asumi's bracelet identification as the reader's second clue and as evidence of her expertise (005).
6. The V04 voice inventory, including Motoya's zero おまえ and Shichijō's 関川洋介さん→洋介さん shift (008).
7. Sums, dates and the one-third mechanism (006).
8. Identity facts and ages for leads and principals (009).
9. Victim portrait and early money and period pointers (010).
10. The Shichijō monograph's evidence-routed history and decision analysis, as material for a canonical non-lead portrait. Qualification itself is for the CHAR task.
11. The open question of timing knowledge (013) and the Yūko address route (012).
12. Ordinary-life inventory: meals, Motoya's coffee server, Asumi sleeping at home, the tea/coffee slip.

**From GPT to an integrated account (CB1 is frozen; these are what CB1 lacks).**

1. Source-status discipline on driver identification, attributed Inatori research and stated renunciation (016). Use it as the integration standard.
2. The undetermined cause of the streaming failure (edition, conditions or knowledge), CL-0001-R01 (A12).
3. Separation of film world, replay and real assault as distinct evidence levels (H-0001, K-0001).
4. The Echika-versus-Hongō 119 attribution difference (EV-0002; A13).
5. Research versus byline credit as a theme (CL-0004; C01 p0767).
6. The midpoint audit's typology placing V04 facilitation between V02 redirection and V03 sequential assault (`audits/KSOA_V04_LONGITUDINAL_RECONCILIATION.md`).

---

## 7. Compression note

The GPT V04 reading (about 38 KB, plus 62 V04 ledger rows) is far shorter than the CB1 V04 set: a 56 KB reading, a 70 KB freeze record, a 116 KB character file, 207 KB of section notes and an 18 KB exit state. For V04 the compression is not merely economical. It lost source-bearing evidence the canonical corpus needs:

- the locked-room endpoint (001);
- the knowledge route to the marriage (002);
- the sums and the inheritance mechanism (006);
- two pre-reveal pointers that change the detectability account (003, 004) and a third, the bracelet identification (005);
- the whole V04 voice and identity layer (008, 009).

What the compression kept is valuable and sometimes better than CB1. The reading consistently separates observed, attributed, admitted and alleged material, and declines to over-read the streaming failure. The best integration is GPT's status vocabulary applied to CB1's fact base. On this unit CB1 does not show the converse problem of over-reading beyond the source, except in summary-level status flattening (016) and one monograph inference (012).
