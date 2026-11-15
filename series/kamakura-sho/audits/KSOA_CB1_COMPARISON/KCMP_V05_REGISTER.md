---
title: "KCMP V05 comparative discrepancy register — 西御門の館"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CB1_KCMP_V05_REGISTER
artifact_type: comparative_discrepancy_register
generation: KSOA-CB1-COMPARISON
version: "1.0"
created: "2026-11-15"
status: historical_legacy
scope: "Phase 3 comparative register for V05 西御門の館: dimension assessment, discrepancy records, agreement samples, omission searches, transfer candidates and compression note. Its proposed dispositions are superseded in effect by ADJ_B."
source_boundary: "Seven Japanese publisher EPUB witnesses KSOA-JP-V01-W01 to KSOA-JP-V07-W01 (all narrative sections); GPT corpus KSOA-G1 at 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a; KSOA-CB1 blind package frozen 2026-11-15T10:52:54Z, manifest SHA-256 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040."
canonical_home: series/kamakura-sho/audits/KSOA_CB1_COMPARISON/KCMP_V05_REGISTER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
do_not_use_as_literary_evidence: true
proposals_adjudicated_in: audits/KSOA_CB1_COMPARISON/ADJ_B.md
authority_note: "Historical comparison record. Its proposed dispositions, priorities and destinations are superseded in effect by the adjudication; cite the adjudication for any decision."
compared_generations: [KSOA-G1, KSOA-CB1]
gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
cb1_blind_package_manifest_sha256: 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040
source_record: "comparison/KCMP_V05_REGISTER.md in the KSOA-CB1 comparison workspace (outside Git)"
source_record_sha256: f121c2caa75eaa766c720b7c51937cfad5b824eeb77badfb5d2c6dd0b95eeba6
source_record_bytes: 53181
source_record_body_sha256: b01619ad71dfb4b62b595a8b56b941362326f04f1a14b61bd6c633a3459c94c2
copy_transformations:
  - "line endings normalized CRLF to LF (341 lines); repository validators reject carriage returns"
path_rewrites: []
integration_date: "2026-11-15"
integrated_by: INT-6
source_record_front_matter: |
  title: "KCMP V05 comparative discrepancy register — 西御門の館"
  artifact_type: comparative_discrepancy_register
  status: draft_noncurrent
  do_not_use_as_current_authority: true
  gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
  cb1_basis: "BLIND_PACKAGE_MANIFEST 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040"
  author_model: "Claude Opus 5.5 (claude-opus-5-5), Phase 3 comparative reviewer (Context B), task V05"
  created: "2026-11-15"
---

# KCMP V05 comparative discrepancy register — 西御門の館

Task V05 under `comparison/PHASE3_BRIEF.md`, applying `comparison/COMPARISON_PROTOCOL.md` (§4 dimensions, §5 record fields, §6 adjudication, §7 sampling) on the basis pinned in `comparison/COMPARISON_BASIS.md`. Neither corpus was modified. The repository working tree was checked clean at the pinned commit (`git rev-parse HEAD` = `7d8ece76…`; `git status --short` empty). Work notes: `comparison/work/V05_notes.md`.

**Locators.** GPT locators of the form `SEC NNNN` and CB1 locators `[V05 SEC pNNNN]` resolve to the same `p[NNNN]` ordinals in `KSOA-CB1:01_source/V05/V05_<SEC>.txt`. Checked on several examples before use: GPT `C02 0234` (the raster) = source `p[0234]` carrying `el[0585]`; GPT `C03 0947–0966` = finances p0947, marina p0951, confession p0954, arrest p0962, Motoya's prediction p0966; CB1 `[C03 p0954]` = the confession. Japanese quotations below were copied from the extraction lines and re-checked.

---

## 1. Files read

### GPT corpus (blob prefixes verified with `git hash-object` against `HEAD`)

| File | Blob | Read |
|---|---|---|
| `readings/KSOA_V05_DEEP_READING.md` | 49c57da846fd | Complete, all 242 lines |
| `readings/KSOA_V05_READING_INTRODUCTION.md` | 23d47f4cb4f0 | Complete, all 52 lines |
| `KSOA_CASE_EVIDENCE_LEDGER.md` | 9ed33ab7ef26 | Header (l.1–39) and `## V05 case evidence` (l.183–206), complete |
| `KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md` | 47c8a2cacccb | Header (l.1–39) and `## V05 disclosure history` (l.141–158), complete |
| `KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md` | 2fd1ab0763c6 | Header and institutional-practice preamble (l.1–46) and `## V05 character and institutional state` (l.142–158), complete |
| `KSOA_CLAIM_REVISION_LEDGER.md` | 2021f91059f7 | Whole file (180 lines). Rows citing V05: KSOA-V05-CL-0001 … CL-0006 with revisions, KSOA-SER-CL-0001, SER-CL-0004, SER-CL-0005 |
| `studies/KSOA_ASUMI_OGASAWARA.md`, `KSOA_MOTOYA_KITSUKAWA.md`, `KSOA_PARTNERSHIP.md`, `KSOA_MYSTERY_FORM_AND_CAUSALITY.md`, `KSOA_POLICING_PLACE_AND_NARRATION.md`, `KSOA_INTEGRATED_SERIES_SYNTHESIS.md` | fcce3dbf5021, be1d259f6cca, a6e995a9127c, 94522dbf9f01, a6729bb726da, e5134916143f | Every V05-bearing paragraph and every register paragraph read in full; whole-file term searches for omission discipline (§5). Not read end to end (outside this task's mandatory list) |
| `audits/*` (all seven), `CURRENT_STATE_AND_CORPUS_MAP.md`, `KSOA_SOURCE_AND_WITNESS_MAP.md` | per basis table | Every V05-bearing line read; whole-file term searches |

### CB1 baseline (SHA-256 prefixes)

| File | SHA-256 prefix | Read |
|---|---|---|
| `02_readings/V05/CB1_V05_READING.md` | 6ec5c900ab917060 | Complete, 312 lines |
| `02_readings/V05/CB1_V05_CHARACTER_EVIDENCE.md` | 303ff858db3a71ee | Complete, Part 1 CE-001…CE-166 and Part 2 |
| `02_readings/V05/CB1_V05_EXIT_STATE.md` | 44d1d8ea46922de8 | Complete |
| `02_readings/V05/CB1_V05_SECTION_NOTES.md` | cf8e1ce4c416f001 | Consulted (C01 chunk-3 notes; C03 O-0189…O-0198 and chunk-7 notes; EPI) and searched in full |
| `02_readings/V05/CB1_V05_FREEZES.md` | ac1c0eb57906d6c7 | Searched; F-01, F-09…F-11 passages consulted |
| `02_readings/V05/CB1_V05_ENTERING_RECORD.md` | 817430075b7c704f | Not needed beyond the reading's §B summary |
| `03_cumulative/CB1_SERIES_STATE_AFTER_V05.md` | e033127d4caaeebf | Searched (V05 loose ends) |
| `04_synthesis/CB1_CLAIM_AND_UNCERTAINTY_INVENTORY.md` | 209329dcd719396e | §A.5 and every V05-bearing row; §F errata register complete |
| `04_synthesis/CB1_LONGITUDINAL_SYNTHESIS.md` | f43f158826bd200b | Every V05-bearing line |
| `04_synthesis/CB1_ASUMI_MOTOYA_PARTNERSHIP.md` | 6a7aaac40133ddaf | V05-bearing lines |
| `05_monographs/CB1_ASUMI_OGASAWARA_MONOGRAPH.md`, `CB1_MOTOYA_KITSUKAWA_MONOGRAPH.md`, `CB1_HATANO_EMIRI_MONOGRAPH.md`, `CB1_TAKIGAWA_SAYAKA_MONOGRAPH.md` | 628c6ed415b32166, daf6aa5cfe2fc87d, f9b2e72caafa7133, 5e758454cc4193ed | V05-bearing lines |

### Japanese source

`01_source/V05/V05_PRO.txt` (24a69d5d…), `V05_C01.txt` (f4531588…), `V05_C02.txt` (ef98d4ae…), `V05_C03.txt` (1b2d0990…), `V05_EPI.txt` (34b8247b…). **Read in full**, every paragraph, PRO p0001 to EPI p0044. All 2,767 narrative paragraphs (PRO 87, C01 757, C02 902, C03 977, EPI 44) were read in order of verification need, not story order; each record's quotations come from that pass.

---

## 2. Dimension assessment

| # | Dimension | Better for V05 | Concrete example (locator) |
|---|---|---|---|
| 1 | Source coverage | **CB1** | CB1 records the prologue's 木刀 「若尾を脅すために持ってきた木刀」 [PRO p0045] and the bag 「そばに残された若尾のバッグの中身も海に投じた。」 [p0075]. Neither appears anywhere in the GPT corpus (KCMP-V05-002). |
| 2 | Narrative reconstruction | **CB1** | CB1 §C gives the five investigative days with times and places, and its appendix registers 18 scenes. GPT's chronology table stops at "Sunday and inquiry" and "Next Sunday" and omits the Thursday 15:00 gathering [C03 p0782] (KCMP-V05-008). |
| 3 | Mystery reasoning | **Comparable, complementary** | GPT is better at calibrating evidential levels: admission, reconstruction and charge are kept apart, and it alone flags the fall/disposal tension [PRO p0064; C03 p0952] (KCMP-V05-001). CB1 is better on the clue inventory: the boat anecdote [C02 p0461], Motoya's misjudgment [C02 p0370] and the marriage contradiction [C03 p0943 vs p0224] (KCMP-V05-003, -004, -005). |
| 4 | Psychological interpretation | **Comparable** | GPT keeps Asumi's motive open and Yuka's agency distinct (H-0009; CL-0005). CB1 is finer on Motoya's thought–speech gap (§G; [C02 p0559], [C03 p0415–0417]) and on Hani's performed devotion (CE-062, CE-159). |
| 5 | Ordinary-life detail | **CB1** | CB1 §H lists meals and drinks (burrito with iced coffee [C01 p0725], lemon squash [C02 p0727], gyokuro-like tea [C03 p0117], green tea at the memorial [p0832]), ready-made suits [C03 p0617–0619] and the judo-hall futon [p0591]. The GPT V05 files contain none of these (KCMP-V05-009). |
| 6 | Relationship modeling | **Comparable** | GPT's REL-0002 and CL-0004-R01 give Sayaka and Emiri independent agency. CB1's directed table (§J; exit §5) carries address forms and third-party pairing labels [C01 p0482, p0691; EPI p0035]. |
| 7 | Japanese-language analysis | **CB1** | CB1 §K: あんた ×7 in the café quarrel, おまえ ×1 from Motoya [C02 p0789], and Hani's 僕 → 俺 at the confession [C03 p0954]. GPT has no V05 register row (KCMP-V05-007). |
| 8 | Longitudinal synthesis | **Comparable** | GPT ties V05 to SER-CL-0001 (single assailant as a counterexample) and to SER-CL-0004 (partnership revision). CB1 disposes the carried V04 predictions and records pattern breaks, notably the only volume without a drunk coda (§O; erratum C-11). |
| 9 | Thematic interpretation | **Comparable** | CB1's thesis is appropriation against forgiveness, display against humility [C03 p0177–0182, p0883]. GPT's "Design, recognition and care" adds care labour and households as conditions of creative work [C03 p0164, p0216]. |
| 10 | Operational reconstruction | **CB1** | CB1 records the 06:07 call and 06:19 arrival [C01 p0592], the 検視官 and 刑事部長 decision [p0655–0656], three-quarters of the team on 鑑取り [p0754], the canvass block 材木座五丁目14–15 [p0695] and the promised corroboration routes [C03 p0952]. GPT INST-0001 and INST-0002 are sound but thin. |
| 11 | Evidence traceability | **Comparable, different modes** | GPT has stable row IDs, horizon-bound freezes and anchored ledgers, but locators are ranges without quotation. CB1 gives an exact, verified Japanese quotation for nearly every row, so it is faster to verify against the source. |
| 12 | Retrieval completeness | **CB1** for fact lookup; **GPT** for cutoff-safe retrieval | Names, times, places and food can be found in CB1 by search (scene register; CE rows). GPT's prospective records H-0000…H-0015 support bounded queries that CB1's freezes support less cleanly. |

**The five aspects, reported separately.**
- **Literary completeness: CB1.** It covers every scene, the whole cast, setting and local history, and all three motif strands (sea glass, wind and flow, hototogisu). GPT is selective.
- **Interpretive sophistication: comparable.** GPT's discipline on the limits of evidence is superior: the three levels of conclusion, the fall against the disposal, and Yuka's agency. CB1 offers a stated thesis with a live competing thesis and five counterreadings (§D, §N), and a more precise ethical ledger.
- **Source accuracy: both high.** Every GPT factual claim checked held except one slip in the introduction (KCMP-V05-012) and two overstated summaries in the studies (KCMP-V05-014). CB1's Phase 1 V05 files held on every item checked beyond its own recorded errata. Its synthesis overstates the status of the boat route (KCMP-V05-010).
- **Character-reconstruction coverage: CB1.** It has 166 direct rows with class labels, per-character synthesis, register and ordinary life. GPT has 4 CH, 5 REL and 2 INST rows and no VOICE row.
- **Retrieval convenience: split.** CB1 is quicker for "what happened, who said what, when". GPT is better for "what could be known by checkpoint X".

No overall winner is named.

---

## 3. Discrepancy register

Records are ordered by consequence. Each carries the protocol §5 fields, a first-pass source check, a proposed disposition with confidence, and a canonical destination. Destinations are named only; no change is written here.

### KCMP-V05-001 — Prologue fall versus Asumi's "thrown into the sea"

- **Volume / locator:** V05 PRO p0044–p0069; C03 p0952, p0954, p0966.
- **Subject:** case mechanics; intent; legal characterization.
- **GPT claim:** `readings/KSOA_V05_DEEP_READING.md` #ksoa-v05-h-0014, Adjudication: "It also leaves a tension between her claim of disposal and PRO's depiction of a fall." The same file, §"A single assault amid several projects of redress", says: "PRO describes a fall. Asumi's accusation includes an act of disposal and subsequent verification in the future tense." `KSOA_CLAIM_REVISION_LEDGER.md` #ksoa-v05-cl-0001-r01: "OPEN the exact position and discrepancy between fall and alleged disposal."
- **CB1 claim:** `CB1_V05_READING.md` §C reports Asumi's account as "struck him and threw him into the sea". `CB1_V05_SECTION_NOTES.md` O-0195 records the same, and the chunk-7 analyst note says "PRO now legible: the boat explains … the splash". `CB1_V05_EXIT_STATE.md` row 26 and K-01 adopt the prologue's version ("若尾 falls into the sea and sinks"). The difference between the two is never flagged.
- **Primary Japanese evidence (verified):** In the prologue the victim turns to face the sea: 「くるりと身体をひねって、若尾は海へと向きなおった。」 [PRO p0044]. The blow is followed at once by the splash, 「バシャーンという水音が響いた。」 [p0064], then 「しまった！」 [p0065] and 「こんなつもりじゃなかった。」 [p0068]. Asumi: 「あなたは若尾さんを殴って倒し、その身体を海に放り込んで伊東に戻ったのでしょう。」 [C03 p0952]. Hani admits 「殺すつもりはなかったんだ。」 [p0954]. Motoya: 「この犯行は計画性が高く、殺人で起訴される可能性が高いと元哉は睨んでいた。」 [p0966].
- **First-pass source check:** Confirmed. The reader-only prologue shows no deliberate act of throwing, while Asumi's speech asserts one. The official forensic view also describes a fall: 「後頭部を殴られて意識不明の状態で海中に転落し溺死した見込みが強い」 [C01 p0746], and 渡辺 says 「殴られて海に落ちて溺死した」 [p0526]. The difference matters for intent. Deliberately putting an unconscious man into the sea supports a murder theory. A fall fits the arrest charge of 傷害致死 [C03 p0962].
- **Difference type:** inference; evidence coverage.
- **Counterevidence and alternatives:** 「殴って倒し」 could be loose speech for "knocked him down [into the sea]". The prologue narrator's own account is interested. The text never adjudicates. Motoya's murder expectation rests on planning (the boat, the alibi), not on the act of throwing.
- **Disposition:** `CLAUDE_OMISSION`. CB1 holds both statements but misses the analytical point. **Confidence:** high that the tension exists in the text; moderate on how much it weighs legally.
- **Destination:** no GPT change needed. The verified quotations could be added to case ledger rows KSOA-V05-EV-0012 and RES-0002. The CB1 correction belongs in the adjudication report.

### KCMP-V05-002 — Reader-only physical facts: the 木刀, the bag, the deserted place, and the forensic match

- **Volume / locator:** PRO p0045, p0058, p0074–p0077, p0082; C01 p0511, p0554, p0563; C03 p0952.
- **Subject:** case evidence; reader-side detectability.
- **GPT claim or omission:** No V05 mention of the weapon or the bag anywhere in the corpus. `KSOA_V05_DEEP_READING.md` #ksoa-v05-h-0001 says only "The narrator strikes him, sees him fall into the water and treats concealment as preferable to seeking help". Case ledger #ksoa-v05-ev-0001 says "Watanabe reports injuries". The deep reading (§"A single assault…") says "The exact agreed route, demand amount, disposition of belongings and forensic confirmation remain open in the final text."
- **CB1 claim:** `CB1_V05_READING.md` §E1 and §F2 ("Reader-only: 木刀; bag contents [PRO p0045, p0075]"); CE-004, CE-005; exit state §3 ("No investigator mentions the 木刀 or the bag; Asumi says only 'struck'"). The section notes, chunk 3, add that the wallet and phone were in zipped pockets, so they were not in the bag.
- **Primary Japanese evidence (verified):** 「俺の右手には若尾を脅すために持ってきた木刀があるのだ。」 [PRO p0045]; 「もともと若尾と話をつけるために、誰もいない場所を選んだのだ。」 [p0074]; 「そばに残された若尾のバッグの中身も海に投じた。」 [p0075]; 「目的は達せられなかった。」 [p0082]. 渡辺: 「木刀くらいの棒で背後から殴られた場合にできる裂傷とよく似ている」 [C01 p0511]. The licence and wallet survived in a zipped pocket [p0554, p0563].
- **First-pass source check:** Confirmed. 渡辺's 木刀-sized estimate is the strongest reader-side link between the prologue and the beach body. The prologue settles where the bag's contents went. What stays open is whether the investigators ever recover them, so GPT's "disposition of belongings … open" blurs what the text establishes with what the investigation has verified.
- **Difference type:** evidence coverage; presentation.
- **Counterevidence and alternatives:** GPT's abstract phrasing ("one act", "claim of intending intimidation") preserves the inferential point without the objects. The objects do not alter the solution.
- **Disposition:** `GPT_OMISSION`, with a `GPT_COMPRESSION` dimension for "disposition of belongings". **Confidence:** high.
- **Destination:** GPT V05 reading erratum. A new case-ledger EV row for the reader-only weapon and bag. An amendment noting the rod size in KSOA-V05-EV-0001. A disclosure-ledger K row recording that the reader alone holds these facts.

### KCMP-V05-003 — The focalizer's misjudgments: Motoya rules Hani out

- **Volume / locator:** C02 p0187–p0188, p0370, p0397; C03 p0403, p0567.
- **Subject:** focalization; clue detectability; Motoya's judgment.
- **GPT omission:** No GPT file records Motoya's judgments of the witnesses' honesty. Searched the whole corpus (§5). The deep reading's detectability paragraph (§"A single assault…") lists clues but not the focal steering away from Hani.
- **CB1 claim:** `CB1_V05_READING.md` §E4: "Motoya's judgment that 羽仁 is no suspect [p0370] is the volume's key misreading". §I, Motoya, "Judgments and errors"; CE-064; claim inventory CB1-CL-102.
- **Primary Japanese evidence (verified):** 「いままでのようすから羽仁が被疑者である可能性は皆無だと、元哉には感じられた。」 [C02 p0370]; 「羽仁のアリバイも問題がなさそうだ。」 [p0397]; on Yuka, 「だが、一昨日の夜のアリバイは完璧ということになる。」 [p0187]; on Tanaka, 「大きなウソをついているようには見えなかったな」 [C03 p0403]; on Kodera, 「元哉は小寺の目を見て真実を語っていると思った。」 [p0567].
- **First-pass source check:** Confirmed. The only consciousness the reader shares actively discounts the eventual culprit. This is a structural device of misdirection and bears directly on any detectability judgment.
- **Difference type:** evidence coverage; interpretation.
- **Counterevidence and alternatives:** Motoya's judgments of Tanaka and Kodera are right on the killing, so his record is mixed, not uniformly wrong (CB1 §I says as much).
- **Disposition:** `GPT_OMISSION`. **Confidence:** high.
- **Destination:** disclosure ledger (a K row for Motoya's belief at KSOA-V05-H-0007, with an ADJ at H-0014); character ledger (a Motoya STATE row); the Motoya study.

### KCMP-V05-004 — Clue inventory for the boat route and the culprit

- **Volume / locator:** C01 p0172, p0465–p0467, p0536; C02 p0264, p0395, p0461, p0864; C03 p0644, p0951.
- **Subject:** clue placement and detectability.
- **GPT claim:** `KSOA_V05_DEEP_READING.md` §"A single assault…": "It prepares a personal one through Hani's closeness to Yuka, Enomoto's narrower judgment of the friendship and Hani's defensiveness at an alibi question… The fully specified route, financial account and exact motive remain late or underdetermined." Nothing on maritime seeding.
- **CB1 claim:** `CB1_V05_READING.md` §F4, row "The alibi is broken by a boat": "Only indirect … 羽仁's own boat anecdote attached to 田中 [C02 p0461] … Very low". Hani's partial design of the inn is recorded only as a fact (CE-068; exit row 20), not weighed as a clue. Asumi's remark about who rushed over first is recorded in CE-101 but not weighed. Q-12, the "noon news", is in §F5.
- **Primary Japanese evidence (verified):** 「そんで田中は船を出すって騒いでた。」 [C02 p0461]; 「僕は伊豆高原のホテルに泊まっていました。一部の設計に携わったことがある宿でね。」 [p0395]; the medieval port 和賀江島 「鎌倉へ荷物を運ぶ船を係留する場所」 [C01 p0467]; 渡辺's 「逗子マリーナからでも」 [p0536]; Asumi's 「いち早く駆けつけたのは羽仁さんと波多野さんなんだよ」 [C02 p0864]; Hani's 「お昼のニュースで若尾先輩のことを知って、取るものも取りあえず駆けつけた」, said on Monday morning [p0264; p0577]. The Itō marina first appears at C03 p0951.
- **First-pass source check:** Confirmed. A search of the source for マリーナ, ボート, 船 and ヨット finds no boat attached to Hani before p0951. The only pre-reveal boat talk around the suspects is attached to Tanaka, so it misdirects. Hani's partial design of the inn is a fair, underweighted signal of his familiarity with the place.
- **Difference type:** evidence coverage; inference.
- **Counterevidence and alternatives:** These hints do not make the route inferable. Both corpora rightly judge the route late, and CB1 judges it "not inferable as unique".
- **Disposition:** `GPT_OMISSION`, with the diagnostic note that CB1 records the inn detail but does not weigh it. **Confidence:** moderate to high.
- **Destination:** disclosure ledger (a D or HYP row at KSOA-V05-H-0007 for the maritime references; ADJ-0003 to cite them); the detectability row of the mystery study.

### KCMP-V05-005 — Contradiction in Asumi's reconstruction of when Wakao married

- **Volume / locator:** C03 p0943 against C03 p0224, C02 p0424–p0433 and C02 p0639.
- **Subject:** chronology; reliability of the detective's account.
- **GPT omission:** Absent from the whole GPT corpus (§5). The GPT text comes closest at `KSOA_V05_DEEP_READING.md` chronology row "Early 2000s": "The reasons for her later choice remain a detective's inference." It also says, under §"Design, recognition and care", "Asumi labels part of the story her own speculation."
- **CB1 claim:** `CB1_V05_READING.md` §F5, "Marriage timing … CONTRADICTION (Asumi's conjecture loose, or authorial slip); not adjudicated"; exit state §6; section notes O-0193.
- **Primary Japanese evidence (verified):** Asumi: 「そして、日本建築家連盟賞の受賞をきっかけに若尾さんは跡部事務所を去り、結花さんと結婚した。」 [C03 p0943]. 恵美子: 「でも、若尾さんは結婚して奥さんと扇ガ谷に家を借りたから早くアパートを出ていきましたね。うちをやめたのはもっと後だけど。」 [C03 p0224]. 結花 recalls 「前の扇ガ谷の家のときには飲みに来たし」 [C02 p0424], with mid-2000s film titles [p0426–0428] and Atobe's Christmas champagne at 「うち」 [p0433]. 英美里's hearsay: 「共働きで大変なんて結花さんが言ってたらしいですから。」 about the Atobe-office years [C02 p0639].
- **First-pass source check:** Confirmed, with three independent witnesses against Asumi's dating. Asumi prefaces the passage with 「これはわたしの想像ですから、間違っているかもしれません。」 [C03 p0943].
- **Difference type:** fact (internal to the text); evidence coverage.
- **Counterevidence and alternatives:** It may be an authorial slip rather than a characterized error. The contradiction does not touch the culprit, and it stays unresolved.
- **Disposition:** `GPT_OMISSION`. **Confidence:** high on the textual contradiction; `UNRESOLVED` on its cause.
- **Destination:** claim ledger (a revision of KSOA-V05-CL-0005, or a new CL row); a case-ledger EVT for the marriage, with alternative chronology.

### KCMP-V05-006 — Yuka and the "stolen girlfriend" analogy

- **Volume / locator:** C02 p0231, p0280; C03 p0932, p0936, p0943.
- **Subject:** theme; Yuka's agency; authorial parallel.
- **GPT claim:** `KSOA_CLAIM_REVISION_LEDGER.md` #ksoa-v05-cl-0005: "OPEN the analogy between taking designs and taking a partner. The detective's rhetorical use exposes Hani's resentment while obscuring Yuka's independent decisions if taken literally." The deep reading, #ksoa-v05-h-0014: "The idea that Yuka herself was stolen is an interested framing and does not establish her reasons or agency."
- **CB1 claim:** `CB1_V05_READING.md` §D thesis: "built on a mirrored pair of thefts — 若尾's theft of his master's drawings and (in the victim's own life) his taking of his friend's girlfriend". §I: 結花 "omitted that 羽仁 was her student boyfriend (finding)". §F1: "omitted her student romance with 羽仁". The Motoya section reads "her omission of the romance was real".
- **Primary Japanese evidence (verified):** Asumi stages the parallel: 「若尾さんから跡部先生は製図を盗まれた。あなたは若尾さんになにを盗まれたのですか」 [C03 p0932]; 「あなたは若尾さんに、恋人の結花さんを盗まれたのです」 [p0936]. She then qualifies it: 「これはわたしの想像ですから」 and 「あなたからしたら、若尾さんに結花さんを盗まれたようなものでしょう。」 [p0943]. Yuka is never asked about the student romance on the page. Her account of the photo circle is 「同じ写真サークルに入っていたんで知り合いました」 [C02 p0231].
- **First-pass source check:** Both positions have support. The author deliberately builds the parallel into Asumi's question [p0932], which supports CB1's structural reading. The same speech marks the "theft" of Yuka as conjecture and as Hani's point of view [p0943], which supports GPT's caution. Calling Yuka's silence an "omission" outruns the page, because no scene shows her asked.
- **Difference type:** interpretation.
- **Counterevidence and alternatives:** A reader may hold that Yuka knowingly concealed a fact relevant to motive. The text neither supports nor refutes this.
- **Disposition:** `INTERPRETIVE_DISAGREEMENT`, with a minor `CLAUDE_ERROR` dimension: "omitted" should read "did not volunteer; was not asked". **Confidence:** moderate.
- **Destination:** a claim-ledger revision of KSOA-V05-CL-0005, keeping GPT's agency qualification and adding the authorial staging at p0932; character ledger KSOA-V05-REL-0004.

### KCMP-V05-007 — Japanese register for V05 is absent from GPT

- **Volume / locator:** C01 p0213, p0227, p0313, p0337, p0344, p0647; C02 p0015, p0549, p0571, p0712–p0894, p0789; C02 p0258 (Hani 僕); C03 p0417, p0760, p0930, p0949, p0954, p0959.
- **Subject:** speech and register (Asumi, Motoya, Hani).
- **GPT omission:** There is no V05 VOICE row in the character ledger. `studies/KSOA_ASUMI_OGASAWARA.md` (register paragraph) cites あんた only for V06. `studies/KSOA_MOTOYA_KITSUKAWA.md` cites `僕` only for V07. There is no V05 おまえ and no mention of Hani's pronoun switch.
- **CB1 claim:** `CB1_V05_READING.md` §K; CE-016, CE-092, CE-097, CE-159; claim inventory CB1-CL-082, CL-110, CL-111; errata C-04 and C-20.
- **Primary Japanese evidence (verified by full-source grep):** Asumi says あんた to Motoya seven times, all in C02 (p0712 「あんたのアリバイを訊きたいよ」, then p0756, p0777, p0785, p0808, p0883, p0894); C01's two あんた are 渡辺's. Her あたし occurs only with Motoya [C01 p0647; C02 p0015; C03 p0760]. 「元哉くんっ」 [C01 p0313]; 「吉川くん、事件だよ。来て」 [p0344]; in-group 「吉川がお世話になっております」 [p0337]; bare 「吉川、手錠掛けて、宣告して」 [C03 p0959]. Motoya says おまえ to Asumi once, 「おい、小笠原、おまえ頭大丈夫か？」 [C02 p0789]. He uses 僕 with civilians: 「僕の名前は出さないでくださいね」 [C01 p0227]. Hani shifts from 「僕にはアリバイがあるんですよ」 [C03 p0949] to 「若尾が俺を馬鹿にするから」 [p0954], which echoes the prologue's 「この男はどこまでも俺を馬鹿にしているのだ。」 [PRO p0028].
- **First-pass source check:** CB1's counts were confirmed exactly. Hani's switch to 俺 is a textual identity link between the prologue voice and the confessor, and it goes beyond style.
- **Difference type:** evidence coverage (Japanese-language analysis).
- **Counterevidence and alternatives:** GPT's general caution that register needs its audience ("Japanese register places similar limits on inference", in the policing study) is sound, but it has no V05 data behind it.
- **Disposition:** `GPT_OMISSION`. **Confidence:** high.
- **Destination:** character ledger (V05 VOICE rows for Asumi, Motoya and Hani); the register sections of the Asumi and Motoya studies; a case-ledger note on 俺 as an identity link (KSOA-V05-ADJ-0003).

### KCMP-V05-008 — Anchoring the chronology

- **Volume / locator:** C01 p0599, p0719, p0738; C02 p0125, p0451, p0459; C03 p0224, p0501, p0595, p0782, p0788, p0962; EPI p0004–p0005.
- **Subject:** chronology.
- **GPT claim:** The `KSOA_V05_DEEP_READING.md` chronology table has rows "Early 2000s", "2005 and 2007", "2008 and later", "Saturday evening", "Sunday and inquiry" and "Next Sunday". No story year, month or weekday sequence appears beyond Saturday and Sunday. The "Early 2000s" row includes the student-era relationship. The GPT corpus contains no story-year dating for any volume.
- **CB1 claim:** `CB1_V05_EXIT_STATE.md` §1: "Story year **2023** by arithmetic … Month **June**", with a 37-row chronology covering the five investigative days, 16:02 and the 18:30 wake.
- **Primary Japanese evidence (verified):** 「主人は七九歳で引退しましたので、一三年前までですね。二〇一〇年の秋です。」 [C03 p0224], giving 2023. 「梅雨の晴れ間」 [C03 p0779]; 「梅雨の中休み」 [EPI p0005]. 「榎本と会った翌々日の午後三時だった。」 [C03 p0782], Thursday. The 18:30 wake [p0788]; 16:02 arrest [p0962]. The student era is 「二〇世紀終わり頃」 [C02 p0234]; independence years 2008/2009/2010 [C03 p0501]; Atobe dead 「五年前」 [C02 p0125]; the house built 「六年前」 [p0459]; Enomoto in Lyon 「四ヶ月前から」 [p0451].
- **First-pass source check:** Confirmed. CB1's derivations are sound and labelled. GPT's "Early 2000s" row puts the student relationship about five years late.
- **Difference type:** evidence coverage; presentation.
- **Counterevidence and alternatives:** Relative chronology serves GPT's horizon logic. Absolute dates are derived, not printed.
- **Disposition:** `GPT_COMPRESSION`. **Confidence:** high.
- **Destination:** a GPT V05 reading erratum for the chronology table; case-ledger EVT rows.

### KCMP-V05-009 — Ordinary life, setting, local history and named institutions

- **Volume / locator:** C01 p0011, p0462, p0465–p0468, p0647, p0725, p0739, p0745; C02 p0021–p0040, p0405, p0413, p0727; C03 p0013–p0015, p0107, p0115–p0117, p0150, p0512–p0514, p0570–p0575, p0591, p0600, p0616–p0619, p0832; EPI p0016.
- **Subject:** ordinary life; setting; institutional practice.
- **GPT omission:** The V05 deep reading, introduction and ledgers contain no meal, drink, clothing, sleeping arrangement, local-history note, named HQ officer (二階堂, 福島) or absent superior (吉田). Searched the whole corpus (§5). GPT names Nanako, Watanabe, Nakagawa and Koizumi, and covers the house as "a house he did not design" (#ksoa-v05-h-0010).
- **CB1 claim:** `CB1_V05_READING.md` §H (setting, police practice, food and drink); §I ordinary life; CE-043, CE-111, CE-129, CE-132; LS setting table.
- **Primary Japanese evidence (verified, a sample):** 「昼食は亜澄の教えてくれた担当地区の近くのカフェで、ブリトーをアイスコーヒーで流し込んだ。」 [C01 p0725]; 「レモンスカッシュ」 [C02 p0727]; 「吊るしのスーツが恥ずかしくて」 [C03 p0617]; 「鎌倉署の武道場の薄っぺらい布団」 [p0591]; Asumi's father 「コスプレ衣装の制作者として名を馳せている」 [p0512]; Asumi's apartment 「北欧デザインのもの」 [p0150]; 吉田係長 at 「修善寺の温泉旅館」 [C01 p0647], which is why 正木 sets the pairs: 「鎌倉署の強行犯係長もいないんで、俺が勝手に…」 [p0683]; 二階堂行夫管理官 [p0745]; 福島捜査一課長 [p0739]; 西御門 named after the west gate of 大倉御所 [C03 p0013]; the Atobe house 「昭和三年の建物」 by 「遠藤新の高弟」 [p0107].
- **First-pass source check:** Confirmed for every sampled item.
- **Difference type:** evidence coverage.
- **Counterevidence and alternatives:** Much of this is texture, not plot. It does bear on the brief's ordinary-life and institutional focus and on character reconstruction (`MUNDANE_BEHAVIOR`). The absence of 吉田 explains why 正木 could pair the two.
- **Disposition:** `GPT_OMISSION`. **Confidence:** high.
- **Destination:** character ledger (STATE rows for mundane behaviour); character ledger INST (an amendment to KSOA-V05-INST-0001 for the 吉田 absence and the 二階堂/福島 command); the policing and place study.

### KCMP-V05-010 — CB1 synthesis labels the boat strike "established"

- **Volume / locator:** C03 p0951–p0958, p0965.
- **Subject:** solution status; calibration.
- **GPT claim:** Consistent three-level calibration: the case ledger #ksoa-v05-res-0002 ("Hani is the single admitted assailant … His prediction of a homicide prosecution and forensic plans remain unverified at the cutoff"), #ksoa-v05-adj-0003 ("Assent about a blow does not ratify the whole route"), and the source-completion audit ("The full water journey and exact fall remain less independently specified").
- **CB1 claim:** `CB1_CLAIM_AND_UNCERTAINTY_INVENTORY.md` CB1-CL-026: "羽仁直人 struck 若尾 with a wooden sword from a boat after 若尾 refused a blackmail demand…", status **established**. `CB1_LONGITUDINAL_SYNTHESIS.md` §3.2 table: "Struck with a wooden sword from a pleasure boat off Kamakura about 23:00". The same LS says elsewhere: "A reader can treat several solutions as probable rather than established: … V05's route". `CB1_V05_READING.md` ("Shown vs reported") and the exit state label the boat as a **reconstruction**.
- **Primary Japanese evidence (verified):** The boat exists only in Asumi's speech: 「あなたはあのマリーナに前もって自分のプレジャーボートを係留しておいたのですね。」 [C03 p0951]. Hani admits intent and provocation [p0954] and nods to 「認めるのですね」 [p0956–0958]. Motoya: 「あとは亜澄が言った筋書きを立証する物証を集めればいい。」 [p0965].
- **First-pass source check:** Confirmed. By CB1's own vocabulary, "established" means directly represented or a confession corroborated in the text, and the boat is neither. The novel does treat Asumi's scenario as the solution.
- **Difference type:** presentation; inference (status).
- **Counterevidence and alternatives:** Genre convention and Motoya's acceptance make the route the in-world solution. Hani's nod could be read as assent to the whole account.
- **Disposition:** `CLAUDE_ERROR` in the synthesis status labels, internally inconsistent with CB1 Phase 1. **Confidence:** moderate.
- **Destination:** no GPT change; GPT RES-0002 and CL-0001-R01 already state the correct calibration. The CB1 correction is recorded in the adjudication report.

### KCMP-V05-011 — Enomoto's Tuesday statements contradicted by his Thursday admission

- **Volume / locator:** C03 p0722–p0730, p0745–p0754 against p0870–p0881, p0918–p0924.
- **Subject:** witness reliability; disclosure mechanics.
- **GPT claim:** `KSOA_CASE_EVIDENCE_LEDGER.md` #ksoa-v05-ev-0009: "Enomoto attributes the story of absent drawings and intended forgiveness to Kodera's overhearing. He distinguishes confirmed absence from a hypothesized taking." The deep reading, #ksoa-v05-h-0013, reads: "He doubts a relationship to the current case and asks the pair to limit circulation". Under §"Design, recognition and care" it says Enomoto "revises the account of professional admiration when he admits trying to expose Wakao". Neither flags that his Tuesday claims of ignorance were false.
- **CB1 claim:** CE-135 ("excludes 小寺 and himself"), CE-140 ("Believes the widow doesn't know the thief"), CE-157 (the confession). The contradiction is not flagged.
- **Primary Japanese evidence (verified):** Tuesday: 「いったい誰が製図を盗んだのでしょうか」 is answered 「わかりません。」 [C03 p0722–0724]; on whether the widow knows, 「たぶんご存じないと思います。」 [p0747]. Thursday: 「犯人は若尾しかあり得ないんです。」 and 「だからヤツの不正義が、どうにか立証できないかと小寺さんとさまざまな資料を集めていました。」 [p0918]. The widow did know: 「盗んだ人がわかったのは、二〇〇七年一〇月一日です」 [p0870].
- **First-pass source check:** Confirmed. On Tuesday Enomoto withheld both his belief about who the thief was and the exposure project.
- **Difference type:** evidence coverage; inference.
- **Counterevidence and alternatives:** 「わかりません」 might mean "I can't prove it". His statement about the widow may have been sincere hearsay from Kodera [p0747].
- **Disposition:** `BOTH_INCOMPLETE`. **Confidence:** moderate.
- **Destination:** an amendment to case-ledger KSOA-V05-EV-0009 (reliability limits); disclosure ledger ADJ-0002.

### KCMP-V05-012 — GPT introduction slip ("student friends") and a coverage-table miscount

- **Volume / locator:** C02 p0414–p0422; C03 p0308, p0784.
- **Subject:** character identity; presentation.
- **GPT claim:** `readings/KSOA_V05_READING_INTRODUCTION.md` §3: "He remembers Wakao as his senior and mentor and names their student friends and colleagues Masayuki Tanaka, Kenzō Enomoto and Takanori Kodera." The `KSOA_V05_DEEP_READING.md` coverage table, row C03: "元哉, with accounts from the five architects and the mentor's widow".
- **CB1 claim:** CE-072 and CE-075 identify the three as Atobe-office colleagues and record that 結花 names them first.
- **Primary Japanese evidence (verified):** 結花 raises the names: 「田中さんや小寺さん、榎本くんにも連絡しなくっちゃね……」 [C02 p0414], then 「若尾の跡部事務所時代の同僚です。」 [p0420]. Hani: 「僕に続けて跡部事務所に入ったヤツらです。」 [p0422]. Tanaka is 東大 and Enomoto 東京藝大 [C03 p0308], so they were not fellow students. Only four living architects are present in C03: 「田中正行、羽仁直人、榎本賢三、小寺隆則の四人」 [C03 p0784].
- **First-pass source check:** Confirmed. The deep reading's #ksoa-v05-h-0007 has this right ("Yuka and Hani recall the former five-person circle and give the names").
- **Difference type:** fact; presentation.
- **Counterevidence and alternatives:** "Five architects" may mean the 跡部五人衆 as a group whose history is recounted. It is still loose.
- **Disposition:** `GPT_ERROR` (minor). **Confidence:** high.
- **Destination:** GPT V05 reading-introduction erratum; a coverage-table note in the deep-reading erratum.

### KCMP-V05-013 — Asumi's broken confidence and bluff at the reveal

- **Volume / locator:** C03 p0691–p0694, p0754, p0900, p0904–p0908.
- **Subject:** ethics of method; institutional practice.
- **GPT omission:** The case ledger's #ksoa-v05-act-0002 notes that "Her alternative accusations and the subsequent admission are distinct evidence events". The deep reading notes the cost "to witnesses with already corroborated alibis". The GPT corpus does not record Asumi's promise of secrecy to Enomoto, her later public use of his story, or her bluff about Kodera's alibi witness (§5).
- **CB1 claim:** `CB1_V05_READING.md` §H ("Ethics: Asumi's bluff about 小寺's witness [p0904]; confidentiality promised to 榎本 [p0693] and then used publicly"); CE-154; CB1-CL-076, CL-077.
- **Primary Japanese evidence (verified):** 「ここだけの話にしてくれますか」 is answered 「もちろんです」 [C03 p0691–0693]. Enomoto later makes it conditional: 「今回の事件に関係がないならば、この話はお二人の胸にしまっておいてください。」 [p0754]. In public, to Kodera: 「跡部先生と奥さまの会話を偶然耳にしたそうですね。」 [p0900]; 「裏はとっています。でも、たとえば、その証言が真実でないとしたら……」 [p0904]; 「たとえばの話です。気にしないでください」 [p0908].
- **First-pass source check:** Confirmed. The first promise was unconditional. The later restatement was conditional, and the condition (relevance) was met, so whether the confidence was "breached" is arguable. The bluff is unambiguous.
- **Difference type:** evidence coverage; interpretation.
- **Counterevidence and alternatives:** GPT's general treatment of the gathering's audience cost covers the spirit, though not these acts.
- **Disposition:** `GPT_OMISSION`. **Confidence:** moderate to high.
- **Destination:** an amendment to case-ledger KSOA-V05-ACT-0002; character ledger KSOA-V05-CH-0004; the ethics paragraph of the Asumi study.

### KCMP-V05-014 — Two overstated V05 summaries in GPT lead studies

- **Volume / locator:** C01 p0134–p0141, p0217; C02 p0712–p0902; C03 p0411, p0973.
- **Subject:** Motoya's intention; resolution of the partnership conflict.
- **GPT claim:** `studies/KSOA_MOTOYA_KITSUKAWA.md`: "In V05, outside duty, he deliberately asks basic questions on behalf of readers unfamiliar with Emiri’s craft and asks that his name stay out of the piece." `studies/KSOA_PARTNERSHIP.md`, directed-states row V05: "The ensuing confrontation and her apology show an ability to register another cost."
- **CB1 claim:** CE-012 and CE-015 (Motoya "unnaturally playing the good boy"; "Ignorant of sea glass"); CB1-CL-120, "Conflicts end without apology or explicit settlement".
- **Primary Japanese evidence (verified):** Sayaka designed the interview: 「わたしが訊くよりナチュラルなインタビューになると思う」 [C01 p0134]. Motoya meant to show professional skill but knew nothing: 「よし、それならプロの質問者の腕を見せてやろう…だが、元哉はシーグラスについてなにもわからなかった。」 [p0137–0138]; 「すみません、実はシーグラスってよくわかってなくて……」 [p0139]. Afterwards Sayaka: 「吉川さんはシーグラスのことをなにも知らないから、いいインタビューになった。」 [p0217]. The only apology is to the room at the memorial: 「心よりお詫びいたします。」 [C03 p0973]. The café quarrel ends with work and Asumi's mood recovering: 「午後に入っての亜澄はふだんの姿を取り戻している。」 [p0411].
- **First-pass source check:** Confirmed. "Deliberately … on behalf of readers" credits Motoya with Sayaka's design. The partnership row can be read as an apology for the private-life confrontation, which never occurs. The Asumi study states the memorial apology correctly.
- **Difference type:** inference; presentation.
- **Counterevidence and alternatives:** "Another cost" may be meant to point at the memorial. The GPT deep reading (#ksoa-v05-h-0002) phrases the interview correctly: "His lack of domain knowledge gives the interview an audience-facing route."
- **Disposition:** `GPT_ERROR` (minor, interpretive). **Confidence:** moderate.
- **Destination:** Motoya study; partnership study.

**Record counts by disposition.** GPT_OMISSION 7 (002, 003, 004, 005, 007, 009, 013); GPT_COMPRESSION 1 (008); GPT_ERROR 2 (012, 014); CLAUDE_OMISSION 1 (001); CLAUDE_ERROR 1 (010); INTERPRETIVE_DISAGREEMENT 1 (006); BOTH_INCOMPLETE 1 (011). Total 14.

---

## 4. Agreement sample checks (protocol §7)

| Stratum | Shared claim | GPT anchor | CB1 anchor | Source check | Verdict |
|---|---|---|---|---|---|
| Case solution | Hani admits the blow and denies intent to kill. Motoya makes an emergency arrest on suspicion of 傷害致死 and privately expects a murder prosecution | Case ledger #ksoa-v05-res-0002 | CB1 READING §C, §F5; exit K-01 | 「殺すつもりはなかったんだ。」 [C03 p0954]; 「午後四時二分。羽仁直人、あなたを傷害致死の疑いで緊急逮捕します」 [p0962]; 「殺人で起訴される可能性が高いと元哉は睨んでいた。」 [p0966] | AGREE, verified. CB1 adds the time and Motoya's stated reason (計画性) |
| Case solution | Wakao took Atobe's drawings (2005). Atobe recognized his work on the day of the 2007 competition result and forgave him | Case ledger #ksoa-v05-res-0001, #ksoa-v05-ev-0010 | CB1 exit K-02 | 「あれは二〇〇五年の今頃のことです」 [C03 p0850]; 「盗んだ人がわかったのは、二〇〇七年一〇月一日です」 [p0870]; 「言ってくれれば、図面なんぞくれてやったのに。」 [p0883]; Asumi names the thief: 「製図盗難事件の犯人は、若尾さんでした。」 [p0888] | AGREE, verified. Both note that no document is shown |
| Clue detectability | The alibi-breaking facts (romance, finances, marina) arrive only at the reveal; the shape of the motive is available earlier | Deep reading §"A single assault…"; disclosure ledger #ksoa-v05-adj-0003 | CB1 READING §F4 "Assessment" | Marina first at [C03 p0951]; romance [p0936]; finances [p0947]; a source search finds no Hani boat or marina earlier | AGREE, verified. CB1 more granular (see KCMP-V05-004) |
| Register | Asumi presents herself as Motoya's 指導係, and Motoya silently denies the office | Deep reading #ksoa-v05-h-0008 ("instructor") | CB1 §K; CE-081, CE-082 | 「吉川の指導係です」 [C02 p0549]; 「ただ、亜澄は上司ではないし、指導係というのも正確ではない。」 [p0556]; 「あえて訂正するのも大人げないので、元哉は黙っていた。」 [p0559] | AGREE, verified |
| Ordinary life | Off duty, Motoya asks to be kept out of the article (no fee); Asumi turns up equipped for the beach | Deep reading #ksoa-v05-h-0002, #ksoa-v05-h-0003 ("Asumi's practical equipment") | CE-016, CE-025; §H | 「僕の名前は出さないでくださいね」 [C01 p0227]; 「ギャラも公務員には払えないんで」 [p0230]; 「亜澄はと見ると、しっかりハイカットのスニーカーを履いている。」 [p0462] | AGREE, verified. CB1 more specific |
| Character, both leads | Asumi apologizes at the end of the reveal, and Motoya privately questions how much needed to be exposed | Character ledger #ksoa-v05-ch-0004; Asumi study | CE-161, CE-153; CB1-CL-077 ("never for the deception") | 「いろいろと失礼なことを申しあげました。心よりお詫びいたします。」 [C03 p0973]; 「ここまですべてを明らかにする必要があるのだろうか。」 [p0927] | AGREE, verified. CB1's scope (an apology for rudeness, not for deception) is the more exact |
| Character | 恵美子 withholds what she knows at the Day 2 interview | Case ledger #ksoa-v05-ev-0006 | CB1 §E6; CE-112 | 「いえ、とくにありません」 [C03 p0254] against p0870 | AGREE, verified |
| Lead monograph (CB1 Asumi) | Unconditional promise of secrecy to Enomoto, followed by public use | — (GPT silent; KCMP-V05-013) | CB1 Asumi monograph §5.1 and §6.4; CL-076 | p0693, p0754, p0900 | Verified, with the nuance of the conditional restatement at p0754 |
| Lead monograph (GPT Motoya) | He credits Asumi's estimate of Watanabe | Motoya study ("articulates why he trusts Asumi’s estimate of the medical examiner") | CE-037 | 「ドンピシャだって小笠原が言ってましたよ」 [C01 p0543] | AGREE, verified |

---

## 5. Omission discipline

**GPT_OMISSION searches** covered the whole GPT corpus under `series/kamakura-sho/`: all seven deep readings and introductions, all four ledgers, the reconstruction spec, all six studies, all seven audits and the maps. They used `grep -rl` and `grep -rn -i` on English and Japanese terms. A term counts as absent when it has no V05-bearing hit.

- KCMP-V05-002: `木刀`, `wooden`, `sword`, `weapon` (hits only in V03/V06/V07 readings), `bag` (hits only in V01 material), `belongings` (one hit, quoted), `parka`, `Suica`, `50,000`.
- KCMP-V05-003: `皆無`, `zero chance`, `no suspect`, and every `Hani` hit in the studies, ledgers and audits; Motoya's judgments in the V05 deep reading (`honest|truth|lie|candor|sincer|judg` near `Motoya`).
- KCMP-V05-004: `boat` (one hit: "reported boat"), `marina`, `partly designed`, `designed the hotel`, `rushed`, `first to arrive`, `noon`, `news`.
- KCMP-V05-005: `扇ガ谷`, `Ōgigayatsu`, `Ogigayatsu`, `marri*`, `wedding` (every hit checked; none concerns the Wakao marriage).
- KCMP-V05-007: `僕`, `俺`, `あんた`, `おまえ`, `omae`, `キミ`, `あたし`, `元哉くん`, `吉川くん`, `self-reference`, `VOICE` rows by volume.
- KCMP-V05-009: `food`, `lunch`, `meal`, `coffee` (one hit, V07), `lemon`, `burrito`, `tea`, `champagne`, `curry`, `sake`, `suit`, `futon`, `judo`, `dojo`, `sneaker`, `Hiratsuka` and `kimono` (hits only in other volumes), `かつらや`, `cosplay`, `Nikaidō`, `Nikaido`, `Fukushima`, `Yoshida`, `Wright`, `Endō`, `Taliesin`, `Pritzker`, `生生流転`, `Taut`, `Lyon`, `Bach`, `ホトトギス`, `hototogisu`, `angel`, `kite`, `あっかんべー`.
- KCMP-V05-008: `2023`, `2022`, `story year`, `story time`, `June`, `Tuesday`, `Thursday`, `thirteen`, `retire`.
- KCMP-V05-013: `bluff` (no V05 hit), `promise`, `in confidence`, `confid*`, `secrecy`, `hypothetical`, `testimony were`.

**CLAUDE_OMISSION search** for KCMP-V05-001 covered the whole CB1 corpus (`02_readings/V05/*`, `03_cumulative/*`, `04_synthesis/*`, `05_monographs/*` including work dossiers). Terms: `放り込`, `threw him`, `thrown into`, `throws him`, `threw 若尾`, `pushed`, `突き落`, `fell into`, `falls into`, `discrepan`, `contradict`, `tension`, `inconsisten`. CB1 carries both versions (O-0195; exit row 26) but has no passage that notes their difference.

**BOTH_INCOMPLETE** (KCMP-V05-011) used both corpora: GPT `Enomoto`, `榎本`, `know*`, `withh*`; CB1 `榎本` combined with `lie|withh|conceal|knew|わかりません|disingenu|hid`, across the section notes, freezes, character evidence and the reading.

---

## 6. Transfer candidates (ranked)

**What CB1 has and GPT lacks (candidates for the canonical corpus):**
1. The prologue's 木刀 brought "to threaten", the disposal of the bag's contents, the chosen deserted place, and 渡辺's matching 木刀-sized estimate, kept as reader-only evidence (KCMP-V05-002).
2. V05 register data: Asumi's あんた ×7 and last direct 元哉くん; Motoya's single おまえ and his 僕 with civilians; Hani's 僕 → 俺 at the confession as a link to the prologue voice (KCMP-V05-007).
3. The focalizer's misdirection (Motoya's 「可能性は皆無」 about Hani) and the clue inventory for the boat: the Tanaka boat anecdote, Hani's partial design of the inn, 和賀江島 and the marinas (KCMP-V05-003, -004).
4. The contradiction in Asumi's reconstruction of when Wakao married (KCMP-V05-005).
5. The anchored chronology: 2023, June, Sunday to Thursday, 16:02, the 18:30 wake, the atelier and independence years (KCMP-V05-008).
6. Ethics of method: the promise to Enomoto and its use, and the bluff to Kodera (KCMP-V05-013).
7. Ordinary life, setting, local history and named HQ officers (KCMP-V05-009).

**What GPT has and CB1 lacks (to preserve when integrating):**
1. The tension between the prologue's fall and Asumi's 「放り込んで」, with its bearing on intent and charge (KCMP-V05-001).
2. Consistent three-level calibration of the ending (admission, reconstruction, arrest charge) where CB1's synthesis overstates the boat (KCMP-V05-010).
3. The caution that "stealing" Yuka is the detective's conjecture and Hani's point of view, which obscures Yuka's own choices (KCMP-V05-006).
4. Care labour and households as conditions of the atelier's creativity: 恵美子's curry, onigiri and upkeep, and the separation of the atelier from the Tokyo office (GPT KSOA-V05-REL-0003; deep reading §"Design, recognition and care").
5. Kodera's staircase story as an interpretive model of the gap between a stated request and the wish beneath it (GPT #ksoa-v05-h-0012; CB1 records the story but does not use it).
6. Horizon-bounded prospective records (H-0000…H-0015) that let cutoff-safe questions be answered.

---

## 7. Compression note

The GPT V05 deep reading runs 242 lines against CB1's 312-line reading, 453-line section notes, 306-line character evidence and 123-line exit state. The shorter reading is economical in one real respect. Its interpretive claims are carefully bounded, and it catches one inference CB1 misses (KCMP-V05-001). But its compression has **lost genuinely useful evidence**, not just words. Its abstract register ("one act", "a demand", "a route on water", "an evening window") drops checkable particulars that matter to the brief's focus:
- reader-only physical evidence (the weapon and the bag);
- the clue inventory and the focalizer's misdirection, which bear directly on any detectability judgment;
- an internal contradiction in the detective's reconstruction;
- all of V05's Japanese register;
- the absolute chronology;
- almost all ordinary-life and institutional detail.

These losses are not repaired anywhere else in the GPT corpus (§5). A reader who has only the GPT files cannot reconstruct who said what, when, or in what register, and cannot assess how fairly the novel plants its solution. The losses are therefore substantive, though they leave the case outcome and the main interpretive lines intact.
