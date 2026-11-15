---
title: "KSOA–CB1 comparative discrepancy register — V03 極楽寺逍遙"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CB1_KCMP_V03_REGISTER
artifact_type: comparative_discrepancy_register
generation: KSOA-CB1-COMPARISON
version: "1.0"
created: "2026-11-15"
status: historical_legacy
scope: "Phase 3 comparative register for V03 極楽寺逍遙: dimension assessment, discrepancy records, agreement samples, omission searches, transfer candidates and compression note. Its proposed dispositions are superseded in effect by ADJ_A."
source_boundary: "Seven Japanese publisher EPUB witnesses KSOA-JP-V01-W01 to KSOA-JP-V07-W01 (all narrative sections); GPT corpus KSOA-G1 at 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a; KSOA-CB1 blind package frozen 2026-11-15T10:52:54Z, manifest SHA-256 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040."
canonical_home: series/kamakura-sho/audits/KSOA_CB1_COMPARISON/KCMP_V03_REGISTER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
do_not_use_as_literary_evidence: true
proposals_adjudicated_in: audits/KSOA_CB1_COMPARISON/ADJ_A.md
authority_note: "Historical comparison record. Its proposed dispositions, priorities and destinations are superseded in effect by the adjudication; cite the adjudication for any decision."
compared_generations: [KSOA-G1, KSOA-CB1]
gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
cb1_blind_package_manifest_sha256: 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040
source_record: "comparison/KCMP_V03_REGISTER.md in the KSOA-CB1 comparison workspace (outside Git)"
source_record_sha256: 28d2f4a9b19fcaed1fd65afe375770835b6221634284e064d467f39c1b8cf7d9
source_record_bytes: 52522
source_record_body_sha256: 98c631a56a3a409125f0fa94c1160de3bcfec3d516e06702e38324fa225e477e
copy_transformations: []
path_rewrites: []
integration_date: "2026-11-15"
integrated_by: INT-6
source_record_front_matter: |
  title: "KSOA–CB1 comparative discrepancy register — V03 極楽寺逍遙"
  artifact_type: comparative_discrepancy_register
  status: draft_noncurrent
  do_not_use_as_current_authority: true
  gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
  cb1_basis: "BLIND_PACKAGE_MANIFEST 35f7a16e…"
  author_model: "Claude Opus 5.5 (claude-opus-5-5), Phase 3 comparative reviewer, Context B, TASK V03"
  created: "2026-11-15"
---

# KSOA–CB1 comparative discrepancy register — V03 極楽寺逍遙

Scope: TASK V03 of `comparison/PHASE3_BRIEF.md`, under `COMPARISON_PROTOCOL.md` and `COMPARISON_BASIS.md`. Neither corpus was modified. Work notes: `comparison/work/V03_notes.md`.

Locator convention. Japanese source lines are cited `[SEC pNNNN]` on `KSOA-CB1:01_source/V03/V03_<SEC>.txt`. In each file, paragraph p[N] sits on line N+4. GPT native locators (`C02 0762`) and CB1 locators (`[C02 p0762]`) resolve to the same paragraph. I confirmed this on C02 p0762 (the call-box report), C03 p0339 (the hidden message) and EPI p0124 (Motoya's reason for staying), and on the section totals: PRO 35, C01 1058, C02 778, C03 560 and EPI 128 paragraphs, matching GPT's coverage table and CB1 §A.

---

## 1. Files read

### 1.1 GPT corpus (repository HEAD verified `7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a`; blobs verified with `git hash-object`)

| File | Blob | Read |
|---|---|---|
| `series/kamakura-sho/readings/KSOA_V03_DEEP_READING.md` | c753cb64d9ef | Complete, all 231 lines |
| `series/kamakura-sho/readings/KSOA_V03_READING_INTRODUCTION.md` | 9a4166370728 | Complete, all 51 lines |
| `series/kamakura-sho/KSOA_CASE_EVIDENCE_LEDGER.md` | 9ed33ab7ef26 | Header (l.1–39) and the whole of `## V03 case evidence` (l.121–152) |
| `series/kamakura-sho/KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md` | 47c8a2cacccb | Header (l.1–39) and the whole of `## V03 disclosure history` (l.99–119) |
| `series/kamakura-sho/KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md` | 2fd1ab0763c6 | Header, institutional practice and longitudinal use (l.1–46); the whole of `## V03 character and institutional state` (l.101–120) |
| `series/kamakura-sho/KSOA_CLAIM_REVISION_LEDGER.md` | 2021f91059f7 | Header (l.1–44); `## V03 claim history` (l.85–102); every other row citing V03 (V04 CL-0003-R02 and CL-0005, l.117 and l.119; SER-CL-0001 to SER-CL-0005, l.168–180) |
| Studies, audits, method and entrypoint | per basis table | Searched in full for V03 content and for the omission terms in §5. Read: every V03-bearing passage of `studies/KSOA_ASUMI_OGASAWARA.md`, `KSOA_MOTOYA_KITSUKAWA.md`, `KSOA_PARTNERSHIP.md`, `KSOA_MYSTERY_FORM_AND_CAUSALITY.md`, `KSOA_POLICING_PLACE_AND_NARRATION.md` and `KSOA_INTEGRATED_SERIES_SYNTHESIS.md`, and the V03 rows of `audits/KSOA_SOURCE_COMPLETION_AND_LONGITUDINAL_RECONCILIATION.md` and `audits/KSOA_V04_LONGITUDINAL_RECONCILIATION.md`. These were not read line by line; the brief does not assign them to TASK V03. |

### 1.2 CB1 baseline (SHA-256 prefixes match `BLIND_PACKAGE_MANIFEST.sha256`; manifest `35f7a16eddf0…`)

| File | SHA-256 prefix | Read |
|---|---|---|
| `02_readings/V03/CB1_V03_READING.md` | 4f66795d9d71 | Complete, all 377 lines |
| `02_readings/V03/CB1_V03_EXIT_STATE.md` | 552a4911eb22 | Complete |
| `02_readings/V03/CB1_V03_CHARACTER_EVIDENCE.md` | b3d5868d0486 | Part 2 complete (l.261–350); Part 1 rows consulted (CE-125, 126, 143, 201 and others) |
| `02_readings/V03/CB1_V03_SECTION_NOTES.md` | 319af6682ed1 | Consulted (O-0116, O-0120, O-0130, O-0148, O-0162, O-0170 to O-0181, K-02 summary) |
| `02_readings/V03/CB1_V03_FREEZES.md` | bcd107c1b86b | Structure and dispositions consulted (F-01 to F-07; P-24; Q-19) |
| `02_readings/V03/CB1_V03_ENTERING_RECORD.md` | be09cfb8d76d | Structure consulted |
| `04_synthesis/CB1_LONGITUDINAL_SYNTHESIS.md` | f43f158826bd | Every line mentioning V03, located by search; §4.3 (l.222–236) and errata E1–E5 read in full |
| `04_synthesis/CB1_CLAIM_AND_UNCERTAINTY_INVENTORY.md` | 209329dcd719 | §A.3 complete; V03 rows of §B–§E by search; errata register §F complete |
| `05_monographs/CB1_WANIBUCHI_ICHIYO_MONOGRAPH.md` | be1033758190 | l.1–180 (§1–§6) and l.272–471 (§9–§17) read; §7–§8 (behaviour, speech) not read line by line |
| `05_monographs/CB1_ASUMI_OGASAWARA_MONOGRAPH.md` | 628c6ed415b3 | Every passage with a V03 locator, located by search |
| Motoya monograph, partnership study, qualification record | per manifest | V03 claims checked through the inventory (CL-110 and others) and by search |

### 1.3 Japanese source read directly

- PRO p0004–0035, complete.
- C01 p0007–1058, complete. A few long lines of p0262–0706 were read truncated and then re-read in full where cited.
- C02 p0007–0778, complete.
- C03 p0007–0560, complete.
- EPI p0004–0128, complete.
- File prefixes: PRO bbfa80a88501, C01 bc03a2584eed, C02 26cfa98345fd, C03 88a7c980ae03, EPI c9e1bf333c3e.

**Completeness statement.**
- Every assigned GPT file and section was read completely.
- The CB1 main reading and exit state were read completely; the other CB1 files were consulted as cited.
- The whole V03 narrative text was read in the Japanese.
- Every quotation below was checked against the source lines.

---

## 2. Dimension assessment

| # | Dimension | Better served by | Concrete example (locator) |
|---|---|---|---|
| 1 | Source coverage | **CB1** | CB1 keeps about 204 paragraph-level observations and 240 character rows with verified quotations. It records, for example, that Keiko asked 貴遥 to name the time and place of the meeting (O-0181; source [C03 p0395] 「時間と場所を指定してほしい」). GPT's ledgers cite ranges and do not carry this. |
| 2 | Narrative reconstruction | **CB1** | CB1 §C gives a dated, named, located synopsis: 1 Dec, 2 Dec and 9 Dec, with every venue and price. GPT's synopsis is accurate in outline but misstates who chose the meeting place (KCMP-V03-001). Both synopses misorder the hedge-colour scene (KCMP-V03-002). |
| 3 | Mystery reasoning | **CB1** for detectability coverage. GPT is stronger in evidential logic. | CB1 F.5 links Keiko's volunteered 15:00–17:00 alibi to the 15:07 and 15:09 calls ([C02 p0646, p0762]) and audits the cues pointing to Maya. GPT keeps the second-assailant inference conditional on Keiko's truthfulness (HYP-0004), as the source does ([C03 p0459]). |
| 4 | Psychological interpretation | Comparable | GPT reads Ichiyō's 羽衣 myth as a projection that displaces Mariko's creative gifts (§"Walking, watching and caring"; [C03 p0046, p0051]). CB1 offers three competing readings of Ichiyō's candour, including Asumi's strategic reading ([C01 p1016–1025]; Ichiyō monograph §16). |
| 5 | Ordinary-life detail | **CB1** | CB1 records meals, prices and transit: A定食 at ¥1,200 [C02 p0012], apple pie and a chiffon cake [C02 p0527, p0684], 新橋牛飯 and pork curry [C02 p0734], 《大しま》 and 《フレッシュ・ハーブ》 [EPI p0010]. GPT has "their cheap lunch" (H-0005). |
| 6 | Relationship modeling | Comparable | GPT CL-0007 and REL-0005 assign distinct reasons to Motoya's staying ([EPI p0124]). CB1 §J and the exit state §5 cover more directed edges (一遥→遥人, 圭子→野中, 真矢→圭子). |
| 7 | Japanese-language analysis | **CB1** | CB1 §K gives a register table. Its counts hold in the source: あたし ×28, キミ ×5, 吉川くん ×3, 元哉くん ×0, わたくし on formal calls [C01 p0586, p1054], and Motoya's おまえ to Asumi ×3 [C01 p0619; EPI p0058, p0065]. GPT has no V03 register evidence (KCMP-V03-006). |
| 8 | Longitudinal synthesis | Comparable | GPT SER-CL-0001 places V03's successive assaults between V02's redirection and V04's facilitation. CB1's synthesis §3.4 and §5.2 trace bluffs and drunk codas across volumes. CB1's §4.3 contains a misattribution (KCMP-V03-007). |
| 9 | Thematic interpretation | Comparable | GPT asks who may interpret, own and disclose the work, and treats consent and discretion as separate variables (CL-0006). CB1 argues a "palimpsest" thesis and states a competing "procedure, not painting" thesis (§D). |
| 10 | Operational reconstruction | **CB1** | CB1 §H records the investigation teams (鑑取り, 地取り, 遺留品), the outsourcing through 科捜研 to the firm 《アート・アナリシス》 paid by 一遥 [C03 p0209–0217, p0247], the judo-hall lodging [C02 p0687–0691] and the absence of handcuffs [C03 p0437]. |
| 11 | Evidence traceability | **CB1** for paragraph exactness. GPT for structured IDs. | CB1 cites exact paragraphs with marked verified quotations. GPT's rows cite ranges such as "C03 0436–0539" under stable IDs and disclosure horizons. |
| 12 | Retrieval completeness | **CB1** | Several V03 facts are retrievable only from CB1: the call times, Asumi's 材木座 apartment and her 逮捕術 qualification, and a portrait of 一遥. See §5 for the searches. |

**The five aspects, reported separately.**

- **Literary completeness: CB1 is higher.** It covers every movement, ordinary life, place lore, the embedded narratives and the counterreadings.
- **Interpretive sophistication: comparable, with different strengths.**
  - GPT is more rigorous about what an admission covers. It keeps declarations apart from completed acts, and the bluff apart from evidence.
  - CB1 states its competing theses explicitly and keeps more counterreadings in view, such as suicide against homicide for Mariko.
- **Source accuracy: both are high, and each has errors.**
  - GPT: the order of the hypothesis scene (002); the "shortly after work" label for the calls and the "called Takaharu to the reservoir" phrasing (001); the soft rendering "wish for escape" for Mariko (003).
  - CB1: Nikaidō's words attributed to Fukushima (007); an unresolved contradiction asserted where the source resolves it (008); "prove another hand" (010); "renounces" (014); the same misordering of the hedge scene in reading §C (002).
- **Character-reconstruction coverage: CB1 is much higher.** It records Asumi's V03 identity facts, gives a full bounded monograph of 一遥, profiles Keiko, Maya, Haruto and Nonaka, and analyses register. GPT has no V03 PERSON, STATE or VOICE rows.
- **Retrieval convenience: GPT is higher.** Stable row IDs, anchored disclosure horizons and separate case, disclosure, character and claim homes make bounded retrieval easy. CB1's material is richer but spread over six files per volume.

No overall winner is named.

---

## 3. Discrepancy register

Fields follow protocol §5. "Search" lines record the omission searches; the full list is in §5.

### KCMP-V03-001 — The timed calls, Keiko's alibi span and who chose the meeting place

- **Volume and locator:** V03 C02 p0642–0650, p0762; C03 p0373–0398.
- **Subject:** Case and clue detectability: the decisive clue to the first assailant.
- **GPT claim or omission:**
  - The times of the calls (15:07 and 15:09) and the call box (鎌倉駅西口, beside the 横浜銀行 ATM) appear nowhere in the GPT corpus. D-0004 says only "Police know two times and one public phone"; EV-0007 says "Two timed calls from one station phone".
  - The deep-reading timeline labels the calls with the wrong valid time: "| November 29, shortly after work | Call records and station footage place 圭子 making two calls to arrange the meeting." (`readings/KSOA_V03_DEEP_READING.md`, §"A painting with two legacies", table).
  - No GPT file connects Keiko's alibi span to the call times.
  - The introduction says Keiko "called Takaharu to the reservoir" (`KSOA_V03_READING_INTRODUCTION.md` §3 ¶5).
- **CB1 claim:**
  - `CB1_V03_READING.md` §F.5, row 4: "her alibi covers 15:00–17:00 exactly [C02 p0646]; Motoya's 'camera footage could prove it' [C02 p0649] … Lightly flagged (Motoya's dismissal is itself a hint)".
  - Exit state row 19 gives the times and the call box.
  - Section notes O-0181 record the time-and-place request. The reading's synopsis says only "met him at the plaza".
- **Primary Japanese evidence:**
  - [C02 p0762] 「事件当日の午後三時七分と三時九分に掛かってきた二本の電話は、鎌倉駅西口の横浜銀行ＡＴＭ横に設置してある公衆電話ボックスからのものであることが判明した。両方とも貴遥は鎌倉美術館で執務中の時間であった」.
  - [C02 p0642] the police ask about 「四時半から六時半頃」. Keiko answers beyond that window [C02 p0646]: 「三時から五時頃まではたしか丸善本店さんで…」.
  - [C02 p0649–0650] Motoya: 「いま名前の出た店の防犯カメラの映像をすべて集めれば、圭子が写っている可能性はある。」「もっともそんな捜査は必要ないはずだ。」
  - [C03 p0379] 「事件当日の午後三時七分と三時九分に、あなたが電話を掛けている姿が映っていました」.
  - [C03 p0395] Keiko: 「貴遥さんの退勤後に話し合いをしたいから時間と場所を指定してほしいって連絡しました」.
- **First-pass source check:**
  - The calls were made during working hours, not "shortly after work".
  - Keiko's volunteered alibi covers both the call time and the meeting time. The reader can set the two side by side from the C02 close onward.
  - The camera that breaks her alibi is the call-box camera, not the Tokyo bookshop cameras Motoya imagines.
  - The plaza on the victim's commute was 貴遥's choice of place, not Keiko's.
- **Difference type:** Evidence coverage; fact (time label); presentation.
- **Counterevidence and alternatives:**
  - GPT's "station phone" and "two times" show awareness that a time and place exist.
  - The timeline cell may intend the meeting rather than the calls, but the row's text says the calls.
  - Keiko's 15:00 start could be innocent precision, but it falls outside the window the police asked about.
- **Disposition:** `GPT_OMISSION` (the times and the alibi-span inference), with `GPT_ERROR` (the timeline label; the introduction's "called Takaharu to the reservoir"). CB1 is source-faithful in F.5 and the exit state; it compresses the meeting-place point in §C.
- **Confidence:** High.
- **Proposed destination:** GPT V03 reading erratum (timeline row; introduction §3 ¶5); case ledger EV-0007 revision (times, box location, Takaharu's choice of place); disclosure ledger D-0004 revision or a new detectability row; the V03 row of `studies/KSOA_MYSTERY_FORM_AND_CAUSALITY.md`.
- **Search (GPT):** `15:07`, `3:07`, `15:09`, `west exit`, `西口`, `Maruzen`, `丸善`, `three to five`, `three o`, `designat`, `time and place`. No V03 hits.

### KCMP-V03-002 — How the overpainting hypothesis arose: order and attribution

- **Volume and locator:** V03 C03 p0141–0229.
- **Subject:** Scene and case mechanics: the step that turns the painting into evidence.
- **GPT claim:**
  - H-0010, "Testing and ethics": "Ichiyō first explains it as a new paint mixture, then accepts an underlying image as a testable hypothesis. Asumi reveals the intended examination to the owner despite the earlier assurance to Hino."
  - Introduction §3 ¶4: "Ichiyō sees it too and agrees that an underlying image could explain it. Asumi tells him about the proposed examination even though she had offered Maya discretion."
  - EV-0009 ("Ichiyō verifies its appearance and proposes explanations") is consistent with the source.
- **CB1 claim:**
  - Ichiyō monograph §6: "Prompted by Asumi, he leaps to the investigative reading himself … [C03 p0199–0203]".
  - Reading §C: "he concludes 宗二郎 painted something underneath. Asumi then tells him of 貴遥's analysis plan". The second clause of §C also misorders the scene; the monograph's account is correct.
- **Primary Japanese evidence:**
  - [C03 p0155] Asumi points out the colour difference.
  - [C03 p0159] Ichiyō: 「まったく気づいていなかった……」.
  - [C03 p0168] his first explanation is remixed paint: 「言ってみれば宗二郎の雑な仕事だ」.
  - [C03 p0186–0193] Asumi breaks Maya's confidence and discloses the analysis plan.
  - [C03 p0197] she adds a hint: 「貴遥さんがこの調査にこだわった理由は、いまのイヌツゲの色の違いに気づいていたからではないでしょうか」, and the narration calls it 「含みを残した」.
  - [C03 p0203] Ichiyō: 「宗二郎は、このイヌツゲの下に別のなにかを描いている。…ほかにはない」, said 断定的に.
  - [C03 p0205] Asumi: 「わたしもそう思っています」.
- **First-pass source check:**
  - The disclosure and Asumi's hint come before the hypothesis and prompt it.
  - Ichiyō states the hypothesis himself, categorically. He does not "accept" or "agree that it could explain".
- **Difference type:** Fact (sequence); inference (agency).
- **Counterevidence and alternatives:** In substance Asumi steered him there, so "accepts" captures her authorship of the idea. But the text attributes the formulation to him, and the order matters: the breach of Maya's confidence is the instrument that elicits the hypothesis, not only a cost paid later to obtain consent.
- **Disposition:** `GPT_ERROR` (sequence and attribution), with a secondary `CLAUDE_ERROR` (CB1 reading §C misorders the scene in the same way; CB1's Ichiyō monograph §6 is correct). The dependent claim CL-0006 needs only a note that the breach also triggered the inference.
- **Confidence:** High.
- **Proposed destination:** GPT V03 reading erratum (H-0010; introduction §3 ¶4); claim ledger CL-0006 annotation; the Asumi study's V03 sentence in §"From noticing a difference to making it testable".

### KCMP-V03-003 — Mariko's last night: suicidal ideation, the farewell note and the police premise of luring

- **Volume and locator:** V03 PRO p0031–0035; C03 p0124, p0339, p0349, p0357.
- **Subject:** Case K-02, the 1992 death, and the reach of its reclassification.
- **GPT claim:**
  - H-0001: "The end expresses a wish for escape and gives no observed outcome."
  - H-0010: "The prologue expresses despair". §"A painting with two legacies": "Her intention and the cause of her death are independent questions."
  - CL-0001-R01: "Preserve the cause and agency limits of the prologue itself."
  - Suicidal ideation is never named anywhere in the GPT corpus.
- **CB1 claim:**
  - Reading §N.1 ("茉莉子's death as suicide"); inventory CL-016 ("The text never reconciles the two") and U-19.
  - But the exit state §3 and Q-19 render Asumi's remark as "how 宗二郎 found 茉莉子 on the stairs (Asumi: 'unknowable')". Section notes O-0178 correctly have "lured her from the atelier".
- **Primary Japanese evidence:**
  - [PRO p0034–0035] 「いっそすべてを終わりにしたい。」「今夜、この峠から澄んだ夜空に舞い上がりたい。」
  - [C03 p0124] the note: 「これ以上、あなたを苦しめてはなりません。探さないでください」.
  - [C03 p0339] 「わたしは右手で茉莉子に罪を償わせ」.
  - [C03 p0349] Asumi: 「湯原画伯が犯人であると推定してもよいと思います」.
  - [C03 p0357] Asumi: 「湯原がどうやって茉莉子さんをアトリエから誘い出したのか、いまとなってはわかりません」.
- **First-pass source check:**
  - The prologue expresses a wish to end everything that night. That is ideation, not only escape.
  - The police reconstruction assumes Yuhara lured her out of the atelier. The note and the prologue show her leaving of her own accord out of guilt.
  - Neither analysis records that conflict. CB1 records the ideation-against-homicide tension. GPT keeps the questions "independent" without naming the ideation.
- **Difference type:** Interpretation; evidence coverage; source boundary.
- **Counterevidence and alternatives:**
  - Both can be true. A woman contemplating death could be met or followed and pushed; CB1 CL-016 says so.
  - 償わせ could also mean driving her to her death.
  - Asumi's 誘い出した may be a loose phrase rather than a considered premise.
- **Disposition:** `BOTH_INCOMPLETE` (neither notes that the luring premise conflicts with the note), with `GPT_COMPRESSION` (the ideation is unnamed; "wish for escape" under-reads p0034). CB1's paraphrase "found" in the exit state is a minor `CLAUDE_COMPRESSION`.
- **Confidence:** High on the facts; moderate on how much weight the luring premise carries.
- **Proposed destination:** GPT V03 reading erratum (H-0001 wording); claim ledger CL-0001-R02 (OPEN: ideation coexists with the attributed homicide, and the luring premise is unsupported by the note); case ledger RES-0001 residuals.
- **Search (GPT):** `suicid` (V01 only), `end everything`, `終わりにしたい`, `lure`, `誘い出`.

### KCMP-V03-004 — Asumi identity facts first disclosed in V03

- **Volume and locator:** V03 C02 p0577, p0689; C03 p0175; EPI p0063, p0066, p0074.
- **Subject:** Character: Asumi.
- **GPT claim or omission:**
  - Her mother's death appears only in the H-0009 freeze ("The remembered loss of Asumi's mother comes through Motoya…").
  - The student-days boyfriend appears only as "a former partner" (H-0013).
  - No character-ledger row and no passage of `studies/KSOA_ASUMI_OGASAWARA.md` records the mother, the apartment, the shop's generations or the arrest-technique qualification. CH-0005 and the study (l.45) capture the grievance about being treated as self-sufficient, but not who the boyfriend was or what he said.
  - Absent from the whole GPT corpus: the 材木座 apartment, the three-generation shop, and the arrest-technique qualification with judo.
- **CB1 claim:** CE §2.1, "Identity facts" (★ new in V03); inventory CL-019; Asumi monograph §§4–5 ([C02 p0577]; [C02 p0689]; [C03 p0175]; [EPI p0066]; [EPI p0074]).
- **Primary Japanese evidence:**
  - [C02 p0577] 「亜澄は学生時代に母親を病気で失っている。」
  - [C02 p0689] 「ちなみに亜澄は、鎌倉署に至近の材木座にアパートを借りている。」
  - [C03 p0175] 「平塚の駅前商店街で三代続く呉服屋の娘なんです」.
  - [EPI p0066] the requirement for women candidates for sergeant: 「逮捕術及び救急法の技能検定の有級者」, with 「亜澄は当然ながら、逮捕術も修得しているのだ」.
  - [EPI p0074] 「スーパーの店長…七歳ばかり年上…『おまえは強いから一人でも大丈夫だろ』」.
- **First-pass source check:** All verified. Four of the facts are narration, through Motoya's knowledge; the boyfriend story is a drunk self-report.
- **Difference type:** Evidence coverage.
- **Counterevidence and alternatives:**
  - These facts carry no case weight.
  - GPT may judge them background. But the reconstruction spec requires ordinary-life and identity facts, and CB1 CL-091 shows the mother fact bears on the open question of her hospital phobia.
- **Disposition:** `GPT_OMISSION` (apartment, shop generations, arrest-technique qualification), with `GPT_COMPRESSION` (the mother and the ex-partner are present in the reading only).
- **Confidence:** High.
- **Proposed destination:** character ledger V03 PERSON or STATE row for Asumi; the Asumi study's identity and ordinary-life sections.
- **Search (GPT):** `mother`, `Zaimokuza`, `材木座`, `apartment`, `generation`, `逮捕術`, `arrest tech`, `judo`, `boyfriend`, `supermarket`, `student`.

### KCMP-V03-005 — Asumi's repertoire of small deceptions in V03

- **Volume and locator:** V03 C01 p0325–0327; C02 p0325–0327, p0399–0403; C03 p0269–0270, p0480–0482.
- **Subject:** Character: Asumi's interview ethics and technique.
- **GPT claim:**
  - Only the DNA bluff is recorded as deception (EV-0016; CH-0004; INST-0003).
  - C01 p0325 appears as "solicits consent with self-deprecation" (H-0003), without the narration's verdict that it is untrue.
  - C02 p0325 appears as "presents the association more confidently" (H-0006).
  - The surname bluff (C02 p0399) is absent; H-0008 has Nonaka "introduce" Keiko.
- **CB1 claim:** CE-033, CE-138, CE-143, CE-219; reading §F.7 and §I ("bluffing [C02 p0325, p0399; C03 p0480]"); Asumi monograph §6 ("falsely claims a bad memory in order to justify recording").
- **Primary Japanese evidence:**
  - [C01 p0326] 「亜澄は低姿勢で頼んだが、真実ではないことを言っている。」
  - [C02 p0325, p0327] 「犯人はあの絵に関心を持っている人物のなかにいると考えています」, with Motoya: 「そんな根拠はどこにもない。」
  - [C02 p0399] 「亜澄はいきなり圭子の名前を持ちだした。本当は名字は知らないのだが。」
  - [C03 p0482] 「元哉は亜澄のハッタリに驚いた。」
- **First-pass source check:** All verified. Four separate deceptions in one volume (repeated, so a disposition rather than an incident), plus an implied threat.
- **Difference type:** Evidence coverage; interpretation (disposition-level).
- **Counterevidence and alternatives:** Each instance is minor and none is illegal. GPT's frame of consent and discretion (CL-0006) covers the ethics in general.
- **Disposition:** `GPT_COMPRESSION`.
- **Confidence:** High.
- **Proposed destination:** a character ledger V03 STATE row for Asumi; a strengthened CL-0006; the Asumi study's section on interviews and ethics.

### KCMP-V03-006 — V03 register and address evidence

- **Volume and locator:** V03, whole volume.
- **Subject:** Japanese-language analysis for both leads and for case figures.
- **GPT claim or omission:**
  - No V03 VOICE row and no V03 claim about register beyond CH-0002 ("Asumi's register moves through warmth, consent, boundary-setting and judgment").
  - The study-level generalizations cite only V01 VOICE rows and later volumes.
- **CB1 claim:** Reading §K, which covers self-reference, address in both directions, characteristic expressions, Maya's shift of register in her confession and Ichiyō's 小笠原くん, 君 and あなた. Also CE §2.1 and §2.2, and partnership-study counts (おまえ 14 / 4 / 3 across V01–V03).
- **Primary Japanese evidence (counts and quotations verified in the source):**
  - あたし ×28.
  - キミ ×5 ([C02 p0243, p0721]; [EPI p0018, p0097, p0117]); the EPI p0097 instance is addressed to the patrol officer.
  - 吉川くん ×3; 元哉くん ×0.
  - わたくし on formal calls [C01 p0586, p1054].
  - Motoya → Asumi おまえ ×3 [C01 p0619; EPI p0058, p0065].
  - Motoya to a junior officer: 「本部の捜査一課、吉川だ」 [EPI p0093].
  - Maya in confession: 「あ～あ、バレちゃった」 [C03 p0483]; 「あなたはわたしの妹なんだよ」 [C03 p0491].
- **First-pass source check:** All of CB1's sampled counts and forms are confirmed.
- **Difference type:** Evidence coverage.
- **Counterevidence and alternatives:** GPT's architecture puts register in VOICE rows, and V03 simply has none. This is a gap in coverage, not a difference of interpretation.
- **Disposition:** `GPT_OMISSION`.
- **Confidence:** High.
- **Proposed destination:** character ledger V03 VOICE rows (Asumi, Motoya, Ichiyō, Maya); the register sections of the Asumi and Motoya studies.
- **Search (GPT):** `キミ`, `おまえ`, `あたし`, `わたくし`, `吉川くん`, `元哉くん`, `VOICE`.

### KCMP-V03-007 — Who licensed the painting line: Fukushima's intervention and Nikaidō's grudging consent

- **Volume and locator:** V03 C02 p0765–0777.
- **Subject:** Institutions; the characterization of Nikaidō and Fukushima.
- **GPT claim:**
  - INST-0001: "Fukushima weighs early uncertainty against resource discipline and permits two investigators to continue."
  - `studies/KSOA_POLICING_PLACE_AND_NARRATION.md` l.31: "In V03 Fukushima allows bounded work".
  - H-0009 is accurate: "The personnel limits Nikaidō raises are real inside the story. Fukushima gives the pair room to test the weaker line".
- **CB1 claim:**
  - `04_synthesis/CB1_LONGITUDINAL_SYNTHESIS.md` §4.3 table, V03 row: "二階堂: 「根拠が希薄だ…捜査員の数は限られているんだぞ」; 福島 overrules him: 「ふたりだけですから、好きにさせましょうか」".
  - The reading §C compresses the same way ("福島 lets 'only the two of them' pursue it"). Section notes O-0148 attribute the line correctly to 二階堂.
- **Primary Japanese evidence:**
  - [C02 p0772] 福島: 「二階堂くん、少しでも可能性のある線は追いかけてもいいじゃないか。…方向性を絞り込むのはまだ早いんじゃないか」.
  - [C02 p0774–0775] 「ふたりだけですから、好きにさせましょうか」 / 「二階堂管理官は渋々認めた。」
- **First-pass source check:** The quoted permission is Nikaidō's. Fukushima argues for keeping lines open. Resource discipline is Nikaidō's argument, not something Fukushima weighs.
- **Difference type:** Fact (speaker attribution); presentation.
- **Counterevidence and alternatives:** Fukushima's intervention is decisive in substance, so "Fukushima allows" is defensible as a summary. Attaching Nikaidō's quotation to Fukushima is not.
- **Disposition:** `CLAUDE_ERROR` (the synthesis §4.3 quotation misattributed; reading §C compressed), with `GPT_COMPRESSION` (INST-0001 and the Policing study fold Nikaidō's consent into Fukushima).
- **Confidence:** High.
- **Proposed destination:** the CB1 errata register (adjudication report); GPT character ledger INST-0001 wording revision; one sentence of the Policing study. This bears on Nikaidō's cross-volume portrait: sceptical, but he yields.

### KCMP-V03-008 — Nonaka's praise of the brushwork: contradiction or a localized anomaly?

- **Volume and locator:** V03 C02 p0173, p0367; C03 p0155–0168, p0255, p0409.
- **Subject:** Mystery form; whether the novel is internally consistent.
- **GPT claim:** GPT does not raise the point. It does register that Maya's C02 depiction of 貴遥's purely scientific interest is later revised (H-0012).
- **CB1 claim:** Reading §E, M7: "His testimony also creates a contradiction the novel never fully resolves: he praises the painting's gate and hydrangeas as typical late 湯原 touch (p0367), whereas 貴遥 thought its brushwork unlike other 湯原 works (p0173)."
- **Primary Japanese evidence:**
  - [C02 p0367] 野中: 「わたしも一度しか拝見したことがない。ですが、背景の極楽寺山門や前景の紫陽花の描写には晩年の湯原宗二郎の代表的な筆致がよく出ています」.
  - [C02 p0173] 真矢's report of 貴遥: 「あの絵の筆致がほかの湯原作品とは大きく異なる」.
  - [C03 p0155] the difference lies in 「中景のイヌツゲ」.
  - [C03 p0255] Asumi: 「作品表面の一部分には不自然な色塗り」.
  - [C03 p0409] Keiko: 貴遥 felt 「表面に違和感」.
- **First-pass source check:**
  - The anomaly is local, in the right-hand midground hedge. Nonaka praises other areas, the gate and the hydrangeas, from a single viewing.
  - The "brushwork" framing is Maya's, and she later reveals that she suspected the hidden content [C03 p0521].
  - The novel does reconcile the two accounts.
- **Difference type:** Interpretation.
- **Counterevidence and alternatives:** An author-level loose end remains possible, because 真矢 says 「大きく異なる」 about the whole work. But the text offers a coherent reading.
- **Disposition:** `CLAUDE_ERROR` (an interpretive overreach about the novel's consistency).
- **Confidence:** Moderate.
- **Proposed destination:** CB1 errata register only. No GPT change is needed; optionally, a disclosure-ledger note that Maya's C02 account of 貴遥's motive was a cover.

### KCMP-V03-009 — Keiko's shifting account of hardship

- **Volume and locator:** V03 C02 p0569, p0633; C03 p0421, p0515.
- **Subject:** Character: Keiko's motive weights and self-presentation.
- **GPT claim or omission:** Not recorded. CL-0004 holds the motive weights OPEN without this evidence. REL-0004 notes the mothers' labour.
- **CB1 claim:** Both statements are recorded separately: section notes O-0130 (C02: "financially secure enough to raise her … 'never lonely'") and the C03 note ("圭子 (shrinking): she too suffered poverty"). No comparison is drawn in the reading, the CE file or the synthesis.
- **Primary Japanese evidence:**
  - [C02 p0569] 「母は経済的には恵まれていましたので、わたしを育てることができました。…だから、ちっとも淋しいことはありませんでした」.
  - [C02 p0633] 「七万円台の家賃だって必死で払っています」.
  - [C03 p0421] 「わたしは人格劣弱な宗二郎の娘だから、母ともどもずっとずっと苦労してきた」.
  - [C03 p0515] 「わたしなんて……貧乏に苦しんできました」.
- **First-pass source check:** Verified. In the friendly interview Keiko presents a secure and loving childhood. In her confession, and in answering Maya's envy, she presents lifelong hardship.
- **Difference type:** Evidence coverage; interpretation.
- **Counterevidence and alternatives:**
  - The two need not contradict. Emotional hardship and stigma differ from money, and her present rent pressure is real.
  - The confession framing may be rhetorical, a plea for mitigation, or a response to Maya.
- **Disposition:** `BOTH_INCOMPLETE`.
- **Confidence:** Moderate.
- **Proposed destination:** claim ledger CL-0004 revision (motive weights and self-positioning); a new character ledger STATE row for Keiko.

### KCMP-V03-010 — The force of the second-assailant inference

- **Volume and locator:** V03 C03 p0442–0463.
- **Subject:** Mystery reasoning; evidential logic.
- **GPT claim:**
  - HYP-0004: "A second actor explains count and disposition if Keiko is truthful about the first intervention."
  - Deep reading §"Detectability and the second confession": "the contradiction between counts and the stone's location has force conditional on what the first speaker actually did."
- **CB1 claim:** Reading §E, M13: the two withheld facts, "set against 圭子's sincere 'only once' and 'dropped it there', prove another hand."
- **Primary Japanese evidence:**
  - [C03 p0459] Asumi: 「ともあれ、いまの圭子さんの発言を事実とすれば、きわめて重要なことになります」.
  - [C03 p0463] 「それ以外には考えられないのです」.
- **First-pass source check:** Asumi first conditions the inference on Keiko's truthfulness, then asserts that it is necessary. CB1's "prove" follows the assertion and drops the condition.
- **Difference type:** Interpretation; source boundary.
- **Counterevidence and alternatives:** CB1's word "sincere" builds in the condition, and Maya's confession then confirms the inference.
- **Disposition:** `INTERPRETIVE_DISAGREEMENT`. GPT is the more source-faithful.
- **Confidence:** Moderate.
- **Proposed destination:** No GPT change; preserve HYP-0004. Note in the adjudication report against CB1 §E M13.

### KCMP-V03-011 — The withholding in C03's one-week summary while Motoya is focalizer

- **Volume and locator:** V03 C03 p0239–0246, p0362, p0482.
- **Subject:** Focalization and detectability.
- **GPT claim:** "The route from an apparent dearth of evidence to a solution is unevenly shared with the reader" (§"Detectability and the second confession"). GPT does not identify the paradox that the focalizer evidently holds facts the narration withholds.
- **CB1 claim:** Reading §G: "The narration withholds procedural results … from both Motoya's narrated awareness and the reader until the reveal, although Motoya presumably knew some of them during the week; this is a focalization gap the text does not flag." Section notes O-0170: "地取り had some results (unspecified yet)".
- **Primary Japanese evidence:**
  - [C03 p0240] 「地取り捜査には一定の成果があった。」
  - [C03 p0241] 「凶器は発見されたが、現場付近のただの石であって…」 (where it was found is withheld until p0459).
  - [C03 p0482] 「元哉は亜澄のハッタリに驚いた。」 (he knows what physical evidence exists).
- **First-pass source check:** Verified. The summary flags that results exist but withholds what they are: the footage, the sighting, the blow count and where the stone was found.
- **Difference type:** Interpretation (narration); evidence coverage.
- **Counterevidence and alternatives:** Motoya may not have known every result, since Asumi presented the hypothesis to HQ [C03 p0245]. The gap may then be partly in-world.
- **Disposition:** `GPT_COMPRESSION`.
- **Confidence:** Moderate.
- **Proposed destination:** disclosure ledger (a K row separating investigator knowledge from reader knowledge at H-0011); the narration section of `studies/KSOA_POLICING_PLACE_AND_NARRATION.md`.

### KCMP-V03-012 — Portraits of case-local characters, especially 鰐淵一遥

- **Volume and locator:** V03 C01 p0707–1058; C03 p0007–0229, p0533–0558; EPI p0024–0041.
- **Subject:** Character-reconstruction coverage: Ichiyō, Keiko, Maya, Haruto, Nonaka.
- **GPT claim or omission:**
  - Ichiyō appears only in reading prose and in REL-0002 and REL-0003. There are no PERSON or STATE rows for any V03 case figure.
  - No study or audit treats them, and the GPT corpus records no qualification decision for them.
- **CB1 claim:**
  - `05_monographs/CB1_WANIBUCHI_ICHIYO_MONOGRAPH.md`, a bounded monograph (identity, history with corroboration, decisions, register, directed relationships, a conditional profile, uncertainty and errata W-1 to W-3), with qualification QUALIFIED_PENDING.
  - CE §2.3 to §2.9 profile 遥人, 貴遥, 圭子, 真矢, 野中 and the absent figures.
- **Primary Japanese evidence (spot-checked):**
  - [C01 p0890] the will drawn the previous night: 「急きょ弁護士の酒巻を呼んで、昨夜、遺言書を作らせた」.
  - [C01 p0986] the painting is to pass to 遥人: 「この部屋と一緒に遥人に相続させるよ」.
  - [C03 p0191] 「遺言状では遥人に相続させると書いてしまったな。貴遥の遺志を優先すべきかな」.
  - [C03 p0355] his retelling to the gathering is shorter and omits his wife, the note and his cowardice, as the CB1 monograph observes.
- **First-pass source check:** The CB1 portrait's load-bearing claims I sampled are accurate, including the self-corrections W-1 to W-3. On W-3, 「先月」 at [C01 p0864] in an interview on 1 December dates the diagnosis to November.
- **Difference type:** Evidence coverage; architecture.
- **Counterevidence and alternatives:** GPT's architecture reserves monographs for subjects with "sufficient independent evidence". Ichiyō appears in one volume only. Whether he qualifies is the CHAR task's question.
- **Disposition:** `GPT_COMPRESSION`, with an element of `ARCHITECTURAL_DIFFERENCE_ONLY` for the monograph question.
- **Confidence:** High on the coverage difference.
- **Proposed destination:** character ledger V03 PERSON and STATE rows for 一遥, 圭子, 真矢 and 遥人; a monograph or qualification record entry per the CHAR task.

### KCMP-V03-013 — Cues to Maya before the reveal

- **Volume and locator:** V03 C02 p0105, p0127, p0165, p0207, p0216–0222, p0762; C03 p0521.
- **Subject:** Clue detectability for the second assailant.
- **GPT claim:**
  - H-0005 records p0207 (Maya "identifies her own earlier conversation as a possible source of his awareness").
  - The detectability section gives no audit of cues to Maya: "Maya's undisclosed relation and private reasoning become available in her speech, giving the volume stronger retrospective integration than advance identifiability".
- **CB1 claim:**
  - Reading §F.5, row 6, lists no alibi, closeness to the calls ("staff 'didn't notice'"), vehemence and the secrecy request, and audits the calibration failure (§O).
  - It omits p0207, which CE-125 records but the audit does not use.
- **Primary Japanese evidence:**
  - [C02 p0207] 「なにかの雑談のときに、わたしは『極楽寺逍遙』の話を野中さんにしました。それがきっかけかもしれません」.
  - [C03 p0521] 「だから野中さんをそそのかしたのよ」.
  - [C02 p0762] 「その電話に気づいたと証言したスタッフはいなかった」.
  - [C02 p0105] 「わたしは実物を見ていないんです」.
  - [C02 p0220] 「四時半から五時くらいの間にアリバイのある人はいないんじゃないんでしょうか」.
- **First-pass source check:**
  - p0207 is a planted half-truth: Maya incited Nonaka.
  - Her silence about the calls, when she had overheard one [C03 p0527], is a second retrospective cue.
- **Difference type:** Evidence coverage; inference.
- **Counterevidence and alternatives:** None of the cues discriminates before the reveal, and both analyses agree that the solution depends on the reveal.
- **Disposition:** `BOTH_INCOMPLETE`. CB1 is the more complete; neither uses p0207.
- **Confidence:** Moderate.
- **Proposed destination:** a disclosure-ledger row (an adjudication or knowledge row on cues to Maya); an addendum to the detectability section of the GPT V03 reading.

### KCMP-V03-014 — Haruto's renunciation: declaration or completed act

- **Volume and locator:** V03 C03 p0545–0551.
- **Subject:** Case outcome; estate.
- **GPT claim:** H-0012: "Haruto announces an intention to renounce inheritance"; RES-0003 says the same. Accurate.
- **CB1 claim:**
  - Reading §C: "遥人 renounces his inheritance"; §E M14 "遥人 renounces"; §I "renounces his inheritance".
  - The exit state §2 is accurate: "遥人 declares he will renounce all inheritance".
- **Primary Japanese evidence:** [C03 p0547] 「祖父になにかあったとき、すべての財産を僕は相続放棄します」.
- **First-pass source check:** This is a future conditional declaration. An inheritance can be renounced only after 一遥 dies.
- **Difference type:** Fact (status of an act); presentation.
- **Counterevidence and alternatives:** The compression is harmless in a synopsis, and CB1's own exit state carries the correct status.
- **Disposition:** `CLAUDE_COMPRESSION`.
- **Confidence:** High.
- **Proposed destination:** a note in the adjudication report only. GPT needs no change.

**Tally by disposition (primary):**

| Disposition | Count | Records |
|---|---|---|
| `GPT_OMISSION` | 3 | 001, 004, 006 |
| `GPT_ERROR` | 1 | 002 |
| `GPT_COMPRESSION` | 3 | 005, 011, 012 |
| `BOTH_INCOMPLETE` | 3 | 003, 009, 013 |
| `CLAUDE_ERROR` | 2 | 007, 008 |
| `CLAUDE_COMPRESSION` | 1 | 014 |
| `INTERPRETIVE_DISAGREEMENT` | 1 | 010 |
| **Total** | **14** | |

Secondary dimensions: `GPT_ERROR` also in 001; `CLAUDE_ERROR` also in 002 (CB1 reading §C); `GPT_COMPRESSION` also in 003, 004 and 007; `CLAUDE_COMPRESSION` also in 003; `ARCHITECTURAL_DIFFERENCE_ONLY` in part of 012.

---

## 4. Agreement sample checks (protocol §7)

Each claim below is made by both analyses and was verified against the source. All are `AGREE`.

| # | Stratum | Shared claim | GPT anchor | CB1 anchor | Source verification |
|---|---|---|---|---|---|
| A1 | Case solution | Two independent, successive assailants: Keiko struck once and fled; Maya found 貴遥 alive, struck twice and carried off the stone; there was no joint plan | RES-0002; EV-0014; EV-0017; CL-0003-R02 | K-01; CL-014 | [C03 p0421] 「後ろから殴りつけてしまいました」; [C03 p0448] 「三回殴られて絶命」; [C03 p0527] 「虫の息」, 「もう一度殴った」 |
| A2 | Case solution (historical) | 17 July 1992, a fall on the 成就院 stairs, ruled an accident at the time; homicide by Yuhara presumed from the hidden text and Keiko's reported letter | RES-0001; CL-0001-R01 | K-02 | [C03 p0349] 「当時、鎌倉署はこの一件を事故として扱いました」; [C03 p0407] 「父が若尾茉莉子さんを成就院の階段から突き落としたことが書き残されていました」. KCMP-V03-003 notes a caveat. |
| A3 | Clue detectability | "Several blows" is available to the reader from C01 and becomes diagnostic only against Keiko's "once" | §"Detectability…" ("Police see the plurality of blows provisionally") | F.5, row 5 | [C01 p0168] 「それも複数回殴ってるって」; [C03 p0443] 「一回だけですけど」 |
| A4 | Clue detectability | The lunch restaurant is a plant: its manager later places Maya | §"Detectability…" ("A restaurant visited as ordinary background") | §E M6; §H | [C02 p0007] 《五彩楼》; [C03 p0477] 「《五彩楼》の店長さんが見ているんです」 |
| A5 | Register | Asumi shifts register with the handsome son: a high formal self-introduction, a nasal politeness, then a firm refusal | CH-0002 | §K; CE-030 and CE-032 | [C01 p0279] 「頭のてっぺんから声を出して」; [C01 p0315] 「いいえぇ」 with 「鼻に掛かった声」; [C01 p0438] 「顔をしかめて亜澄は断った」 |
| A6 | Ordinary life | A cheap lunch at Hiratsuka prices near 長谷 | H-0005 ("their cheap lunch") | §C | [C02 p0012] 「Ａ定食…一二〇〇円」; [C02 p0017] 「まるっきり平塚価格だな」 |
| A7 | Ordinary life / institution | Motoya sleeps in the station judo hall; local woman officer Asumi goes home | H-0009 ("Motoya's differing lodging burden") | §H, "Housing" | [C02 p0687–0691] |
| A8 | Character | Asumi's mother died during her student days, conveyed through Motoya; the link to her tears is speculative | H-0009 | CE-155; CL-019 | [C02 p0577] 「そのときの悲しみを思い出しているのかもしれない」 |
| A9 | Relationship / epilogue | A resident's report brings a patrol officer; Motoya stays because he has identified himself | REL-0005; CL-0007 | §C; CE-240 | [EPI p0091] 「不審者がこの公園にいるって通報があった」; [EPI p0124] 「警察手帳を見せて名乗ってしまったからには」 |
| A10 | Estate mechanics | Will made the night of 30 Nov; his own works go to 鎌倉芸術協会; the Yuhara painting stays in the estate for 遥人 | H-0004; H-0005; EV-0003 | §C; exit state §2 | [C01 p0890, p0898]; [C01 p0986]; [C03 p0191] |
| A11 | Lead study load-bearing (GPT) | Asumi asks Ichiyō to check her colour observation, and the lab work makes it testable | `studies/KSOA_ASUMI_OGASAWARA.md` l.31 | Asumi monograph §6 | [C03 p0161] 「間違っていませんよね」; [C03 p0209–0213] |
| A12 | Lead monograph load-bearing (CB1) | Motoya's おまえ to Asumi in V03 is 3 (part of 14 / 4 / 3 across V01–V03); her last direct 元哉くん is not in V03 | — | Inventory CL-110 (partnership study §5.2; Motoya monograph §8.2) | Source search: おまえ to Asumi at [C01 p0619] and [EPI p0058, p0065]; 元哉くん ×0 |

One more agreement on epistemic restraint. Both say that which blow killed 貴遥 is not established: GPT ("Evidence for the fatal point … is less direct"); CB1 §N.3 and U-19. The source supports both: [C03 p0448] gives the order and number of blows without naming the lethal one, and Maya says 「たぶんそれで絶命したと思う」 [C03 p0527].

---

## 5. Omission discipline

**GPT corpus searched.** All Markdown under `series/kamakura-sho/`: the root ledgers, method, architecture, spec and map; `readings/*`; `studies/*`; `audits/*`.

| Term group | Terms | Result |
|---|---|---|
| Call times | `15:07`, `3:07`, `15:09`, `west exit`, `西口`, `three o` | No hits |
| Keiko's alibi | `Maruzen`, `丸善`, `three to five` | No hits |
| Meeting arrangement | `designat`, `time and place` | No hits |
| Asumi identity | `Zaimokuza`, `材木座`, `apartment`, `逮捕術`, `arrest tech`, `judo`, `generation` (non-metadata) | No hits |
| Asumi's mother and past partner | `mother`, `boyfriend`, `supermarket` | V03 reading only ("mother"; "former partner") |
| Mariko's death | `suicid`, `lure`, `誘い出` | `suicid` in V01 contexts only |
| The painting | `holly`, `イヌツゲ`, `hedge` | No hits |
| Deception | `bluff`, `self-deprecat`, `untrue`, `pretend`, `feign`, `decept` | V03: DNA bluff only, plus "self-deprecation" in H-0003 |
| Register | `キミ`, `おまえ`, `あたし`, `わたくし`, `吉川くん`, `元哉くん`, `VOICE` | V01 VOICE rows and study generalizations only |
| Case figures | `Ichiy`, `Keiko`, `Maya`, `Haruto` in studies and audits | Mentions only; no portraits |
| Venues | `Gosair`, `五彩楼`, `Ofuna`, `大船`, `Katsuraya`, `かつらや` | No hits |

**CB1 corpus searched.** `02_readings/V03/*`, `03_cumulative/*`, `04_synthesis/*` and `05_monographs/*`.

| Terms | Result |
|---|---|
| `時間と場所`, `designate` | Found in O-0181 |
| `雑談`, `chat` | Found in CE-125 |
| `誘い出`, `lured` | O-0178 has "lured"; the reading and exit state have "found" |
| `p0207` | Not in the §F.5 audit |
| `一定の成果` | O-0170 |
| `ふたりだけですから` | O-0148 correct; synthesis §4.3 misattributed |
| `純粋に学術`, `purely academic` | CE-122, attributed to 真矢 |
| `貧乏に苦しんで`, `苦労してきた`, `never lonely`, `financially secure` | Both Keiko statements found separately, never compared |

No `CLAUDE_OMISSION` is claimed. Every item first checked as a possible CB1 omission turned out to be present somewhere in the CB1 corpus.

---

## 6. Transfer candidates (ranked)

**From CB1 to the GPT canon.**
1. The call times and call box, Keiko's 15:00–17:00 alibi span, Motoya's thought about the bookshop cameras, and 貴遥's choice of the meeting place (001). This is the volume's most discriminating pre-reveal clue.
2. V03 VOICE rows: the counts and forms for Asumi, Motoya, Ichiyō and Maya (006).
3. Asumi's V03 identity facts into the ledger and the study: her mother, the 材木座 apartment, the three-generation shop, the 逮捕術 qualification and the boyfriend's words (004).
4. A bounded portrait of 鰐淵一遥: the CB1 monograph's corroboration table, the four changes of decision within the volume, the conditional profile and the self-corrections W-1 to W-3 (012).
5. Asumi's repertoire of deceptions as a recurring disposition (005).
6. The tension in Mariko's death: suicidal ideation against the attributed homicide (003, which also needs the luring premise that neither side has).
7. An audit of cues to Maya and the calibration failure (013), plus the focalization gap (011).
8. Ordinary-life and operational texture: venues, prices and transit; 《アート・アナリシス》; the investigation teams; voluntary accompaniment without handcuffs.

**From GPT to CB1 (for the adjudication record; CB1 itself stays frozen).**
1. Keeping the second-assailant inference conditional on Keiko's truthfulness (010; HYP-0004).
2. Exact status of declarations: Haruto "announces an intention"; the donation is decided but not completed (014; RES-0003).
3. The correct institutional split, Nikaidō's personnel limit and Fukushima's room for the pair (H-0009), against CB1's misattribution (007).
4. Maya's C02 account of 貴遥's "purely scientific" motive is later revised (H-0012). CB1 records it as attributed but does not flag the revision.
5. Consent, the breach of an assurance, bounded circulation and deception as separate claims to legitimacy (CL-0006), with Maya's protest [C03 p0249] as the anchor.
6. Bounded-retrieval architecture: horizon-anchored rows that let a prospective query stop at H-0009 without exposure.

---

## 7. Compression note (V03)

GPT's V03 deep reading is about 37 KB. CB1's V03 reading is about 67 KB, backed by about 177 KB of section notes and about 110 KB of character evidence.

For V03, GPT's brevity is not simply economy. It is economical and careful on case logic, disclosure discipline and evidential conditionality. But it lost genuinely useful evidence in four areas:
- the times of the decisive calls and the alibi inference that depends on them (001);
- all Japanese register evidence (006);
- Asumi's V03 identity and ordinary-life facts (004);
- any portrait of the volume's most developed case figure, 一遥 (012).

The compression also produced one sequencing error (002) and one wrongly labelled timeline row (001).

Interpretively, GPT's prose is dense and well bounded. What was lost is mainly retrievable fact and character material, not argument.
