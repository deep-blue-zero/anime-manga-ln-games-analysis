---
title: "KSOA-CB1 Phase 4 discrepancy adjudication — Group D (KCMP SERIES and KCMP CHAR registers)"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CB1_ADJ_D
artifact_type: discrepancy_adjudication
generation: KSOA-CB1-COMPARISON
version: "1.0"
created: "2026-11-15"
status: canonical
scope: "Source-decided Phase 4 adjudication of the 28 KCMP-SERIES and KCMP-CHAR records, the monograph-standard findings and nine qualification verdicts, with integration actions grouped by destination type (a)-(h)."
source_boundary: "Seven Japanese publisher EPUB witnesses KSOA-JP-V01-W01 to KSOA-JP-V07-W01 (all narrative sections); GPT corpus KSOA-G1 at 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a; KSOA-CB1 blind package frozen 2026-11-15T10:52:54Z, manifest SHA-256 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040."
canonical_home: series/kamakura-sho/audits/KSOA_CB1_COMPARISON/ADJ_D.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
compared_generations: [KSOA-G1, KSOA-CB1]
gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
cb1_blind_package_manifest_sha256: 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040
source_record: "comparison/ADJ_D.md in the KSOA-CB1 comparison workspace (outside Git)"
source_record_sha256: f3ec0a4ac22189437323965678feb0c5a2dc3d966d5f8be74a02447c3946dff8
source_record_bytes: 89288
source_record_body_sha256: cd45ad357091385d1fc95459f7c5d487c1f4633759c7a7e25cc3cb80eded8d8b
copy_transformations: []
path_rewrites: []
integration_date: "2026-11-15"
integrated_by: INT-6
source_record_front_matter: |
  title: "KSOA-CB1 Phase 4 discrepancy adjudication — Group D (KCMP SERIES and KCMP CHAR registers)"
  artifact_type: discrepancy_adjudication
  status: draft_noncurrent
  do_not_use_as_current_authority: true
  gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
  cb1_basis: "BLIND_PACKAGE_MANIFEST 35f7a16e… (35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040, frozen 2026-11-15T10:52:54Z)"
  author_model: "Claude Opus 5.5 (claude-opus-5-5), Context B independent adjudicator, Group D"
  created: "2026-11-15"
  registers_adjudicated: "comparison/KCMP_SERIES_REGISTER.md (12 records); comparison/KCMP_CHAR_REGISTER.md (16 records, plus its §2A monograph-standard and qualification findings)"
  work_notes: "comparison/work/ADJ_D_notes.md"
---

# Phase 4 adjudication — Group D

*Spoilers for all seven volumes.* I authored neither corpus nor either register. Each record was decided against the Japanese witness text in `KSOA-CB1:01_source/`, not by majority, confidence, length or elegance.

## 0. Basis and method

- **Binding documents read in full:** `comparison/PHASE4_BRIEF.md`, `comparison/COMPARISON_PROTOCOL.md`, `comparison/PHASE3_BRIEF.md`, both assigned registers. For the monograph standard: `repository/governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md` §5.5 and §5.5.1 (l.464–550) and §10 (l.834–868).
- **GPT corpus.** The repository was confirmed at `HEAD 7d8ece76…` with a clean working tree. I read in full `studies/KSOA_ASUMI_OGASAWARA.md` and `studies/KSOA_MOTOYA_KITSUKAWA.md`, which the monograph-standard verdicts require. Every other GPT claim a record cites was checked at its anchor or line, and every omission claim I relied on was re-run as a whole-corpus search over `series/kamakura-sho/**/*.md`.
- **CB1 corpus.** The cited rows were checked at their source: `CB1-CL-038`, `CB1-CL-054`, `CB1-U-18`, LS §3.2 (V07 row) and LS §4.3. I also checked the lead-monograph section structure, the v1 review verdicts, the qualification record (§3–§6) and the specific non-lead monograph sentences under dispute (Satomi l.180, Gamō l.28, Shichijō l.93).
- **Locator equivalence.** Confirmed on independent examples: GPT `KSOA-V07-REL-0005` "EPI 0135–0151" resolves to the Sayaka–Asumi exchange at `V07 EPI p0135–p0151`; GPT `KSOA-V06-EV-0010` "C03 0684–0727" resolves to the shouting test through 糟屋's denial; the CB1 ruby locator `[V04 C01 p0150]` resolves to ｜恵《え》｜智《ち》｜花《か》.
- **Source checks.** About 110 passages were re-read in context. The log is in the work notes. Japanese quotations below are short and were copied from the source lines.
- **Read-only.** No file in `repository/` or `KSOA-CB1:` was modified, and no git command that changes the working tree was run.

Locators: `Vnn SEC pNNNN`. GPT anchors: `path#anchor` or `path` l.N at the pinned commit. Priorities follow the brief: P1, P2, P3 or CB1-only.

---

## 1. Adjudication table

| ID | Register disposition | Verdict | Final disposition | Priority | One-line rationale (locators) |
|---|---|---|---|---|---|
| KCMP-SERIES-001 | GPT_OMISSION; secondary GPT_COMPRESSION | CONFIRM | GPT_OMISSION (series theme); GPT_COMPRESSION (V01 motive, V05 extortion euphemized) | P2 | Extortion recurs in four killings: V01 C03 p0897, p0977; V04 C03 p0918–p0920; V05 PRO p0022–p0026, C03 p0947–p0952; V07 C04 p0598–p0601, p0615. GPT names it only for V04 and V07 and never at series level |
| KCMP-SERIES-002 | CLAUDE_ERROR | CONFIRM | CLAUDE_ERROR | CB1-only | V07 C04 p0574 doubts the voice on an extortion call, and p0575 defers the question to voiceprint analysis; 江口's reactions at p0578–p0589 amount to acknowledgement. The passage is no evidence about the stabbing |
| KCMP-SERIES-003 | GPT_OMISSION | MODIFY | GPT_OMISSION (intoxication, both blackouts); GPT_COMPRESSION (addressee) | P2 | V07 EPI p0131–p0149. GPT does record an audience asymmetry (V07 DEEP l.156) but never the drinking, the blackouts or 沙也香 as the addressee. `KSOA-SER-CL-0004` "High" needs a downgrade |
| KCMP-SERIES-004 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | The sleep-inducer in the host's champagne and the prescription testimony (V06 C03 p0711, p0717–p0721) and the shouting test (p0684–p0687) appear nowhere in the GPT corpus |
| KCMP-SERIES-005 | INTERPRETIVE_DISAGREEMENT | CONFIRM | INTERPRETIVE_DISAGREEMENT, resolved toward GPT (CB1 overgeneralizes) | CB1-only | V06 C02 p0718–p0719 shows HQ indifference after 佐竹's V04-only remark (V04 C01 p0893). `CB1-CL-054`'s trajectory skips V05–V06 of its own table |
| KCMP-SERIES-006 | GPT_COMPRESSION; secondary GPT_OMISSION (credo) | MODIFY | GPT_COMPRESSION only | P2 | The credo is paraphrased in frozen V02 DEEP l.173, minus its 「人倫にもとる」 clause. The habitual bluff (V06 C03 p0681 「お得意のハッタリ」) is absent from every study |
| KCMP-SERIES-007 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P3 | V03 PRO p0034–p0035 states a wish to end everything; GPT glosses it "a wish for escape" (V03 DEEP l.81). The homicide grade survives, since the reported letter says 突き落とした (C03 p0407) |
| KCMP-SERIES-008 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P3 | The focalization rule (Motoya outside the prologues; V02 C01 p0014–p0170 the exception; Asumi's interior only inferred, e.g. V05 C02 p0843–p0845) is never stated or linked to detectability |
| KCMP-SERIES-009 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P3 | No motif inventory or name-reuse guard. 「悪魔が囁」 occurs at V02 C03 p1019 and V03 C03 p0527; reused names include 野中兼司/野中重之 and 若尾茉莉子/宇都宮茉莉子/若尾昌史 |
| KCMP-SERIES-010 | GPT_ERROR | CONFIRM | GPT_ERROR | P1 | Ruby ｜恵《え》｜智《ち》｜花《か》 (V04 C01 p0150) reads Echika; "Kechika" persists in the V04 reading and three ledgers |
| KCMP-SERIES-011 | GPT_ERROR | MODIFY | GPT_ERROR (V07 introduction only) | P1 (low severity) | The V07 prologue (PRO p0004–p0036) carries no gender marker, yet the introduction l.36 uses "He… His". The producer review certifies only that the voices remain *unnamed*, which still holds |
| KCMP-SERIES-012 | CLAUDE_OMISSION | CONFIRM | CLAUDE_OMISSION (interpretation) | CB1-only | 遺書/告白/告解 (V01 C01 p0705; C02 p0539; C03 p0263) as distinct audiences is GPT's analysis (synthesis l.30; policing l.37); CB1 has only the scene facts |
| KCMP-CHAR-001 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | Asumi's キミ (dialogue lines 11/10/5/1/0/0/2; e.g. V01 C01 p0776, V02 C01 p0236, V07 C01 p0012) and 元哉くん (V02 C01 p0327) have 0 and 1 GPT hits respectively |
| KCMP-CHAR-002 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | Motoya's おまえ to Asumi (V01 C01 p0040, p0778) has a single later use, in anger (V05 C02 p0789). Every other おまえ in V04–V07 belongs to a superior. 0 GPT hits |
| KCMP-CHAR-003 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P2 | 僕 begins in V05 with the civilian women (V05 C01 p0091, p0213). GPT's two V07 "contexts" are one utterance (V07 C03 p0493) |
| KCMP-CHAR-004 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | わたくし/わたくしども with 猫なで声 (V02 C01 p0943–p0949), よそゆき声 (V01 C02 p0473) and 甘ったるい声 (V02 C03 p0845–p0846): 0 GPT hits |
| KCMP-CHAR-005 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P3 | 「亜澄はイケメンに弱い。」 (V01 C01 p0899; V03 C01 p0280; denial V03 C02 p0724) is Motoya-focalized narration and is absent from GPT |
| KCMP-CHAR-006 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P2 | The promise 「もちろんです」 (V05 C03 p0691–p0694) and the public use of the rumour (p0842) are both in GPT (V05 DEEP l.183; policing l.39), but never linked. The credo is only paraphrased |
| KCMP-CHAR-007 | GPT_ERROR; GPT_OMISSION | CONFIRM | GPT_ERROR (V07 introduction addressee); GPT_OMISSION (intoxication) | P1 | V07 EPI p0135–p0145: the line is said to 沙也香, about Motoya (こいつ), by two drunk women (p0143). The introduction l.48 says "tells Motoya" |
| KCMP-CHAR-008 | INTERPRETIVE_DISAGREEMENT; minor CLAUDE_ERROR | CONFIRM | INTERPRETIVE_DISAGREEMENT, resolved toward GPT; minor CLAUDE_ERROR | CB1-only | The V04 direction proposal and its reasoning are Motoya's own (V04 C03 p0426–p0432), as are the interview request (p0473–p0474) and the V06 taxi check (V06 C03 p0303). CB1 MM's "prompted" fits only the Alto identification |
| KCMP-CHAR-009 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P3 | Same conclusion in both corpora. GPT omits that Motoya disowns his one bodily response (V01 EPI p0067) and that his appraisals of Asumi are always qualified (V01 C01 p0024) |
| KCMP-CHAR-010 | GPT_COMPRESSION | MODIFY | GPT_COMPRESSION; GPT_OMISSION (responsibility 9 for Asumi, 12 for both) | P2 | Both studies are typed `character_monograph` and `status: canonical`, so they are substantive monographs, grandfathered under §10. The "different responsibility" exemption does not cleanly apply |
| KCMP-CHAR-011 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | No qualification record, outcome or named home. `KSOA_SYNTHESIS_ARCHITECTURE.md` l.73 and the role-gap audit l.47 are pre-standard and cannot exclude qualified characters (§5.5) |
| KCMP-CHAR-012 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P3 | 「元哉は実はコーヒーにはちょっとうるさい。」 (V04 C01 p0734); shared bean-café pleasure (V07 C03 p0481). "coffee" occurs once in GPT |
| KCMP-CHAR-013 | GPT_ERROR | CONFIRM | GPT_ERROR | P1 | 彩音 files a 被害届 against 石川's embezzlement (V02 C03 p0480–p0482, p0525), not a complaint about Asumi (V02 intro l.42) |
| KCMP-CHAR-014 | GPT_OMISSION; presentation | MODIFY | GPT_OMISSION (VOICE layer V02–V07); presentation (`CH` kind undefined) | P3 | The stale initialization headers were preserved deliberately (producer review l.46), so they need a note, not a fix. The substantive speech gap is carried by 001–004 |
| KCMP-CHAR-015 | CLAUDE_ERROR | CONFIRM | CLAUDE_ERROR (minor) | CB1-only | Shichijō's 「一二年ぶり」 is part of the lie (V04 C02 p0698, C03 p0733 「あれは偽りだった」). Satomi l.180 states Motoya's inference as fact (V02 C03 p0932). Gamō §1 overreaches (V01 C03 p1066, p1084) |
| KCMP-CHAR-016 | CLAUDE_OMISSION | CONFIRM | CLAUDE_OMISSION (interpretation) | CB1-only | GPT reads 一遥's account as a projection that displaces 茉莉子's gifts and choices (V03 DEEP l.163, l.226; V03 C03 p0111, p0124). CB1 lacks this reading |

---

## 2. Full adjudication entries

Full entries are given for every P1 and P2 record, every INTERPRETIVE_DISAGREEMENT, every MODIFY and every CLAUDE_ERROR. Short notes for the remaining records follow in §2C. The adjudication of the monograph standard and the nine qualification verdicts are in §2B.

### 2A. Record entries

#### KCMP-SERIES-001 — Extortion and silencing as a recurring case structure

1. **Passages.**
   - V01 C03 p0897: 上原's threat about the staff's embezzlement, as 麻里奈 reports it.
   - V01 C03 p0977: 和枝 quotes 富田, 「一生食いつかれて｜強《ゆ》｜請《す》られるんだ。殺すしかない」.
   - V04 C03 p0918–p0920: 宮崎 paid 500万, was asked for 300万 more, and decided to kill: 「何度でも金をせびってくるに違いない」.
   - V05 PRO p0022 and p0026: 若尾 calls the speaker's demand 卑劣 and protests 「わたしの過去をほじくり返して、そんな要求をするなんて」. At p0045 the speaker carries a wooden sword 「脅すために」.
   - V05 C03 p0947 and p0952: Asumi charges extortion over the hotel secret (「その秘密をバラすと言って若尾さんを恐喝していた」). At p0954 羽仁 admits only the blow.
   - V07 C04 p0598 and p0601 (「脅すつもりだったのか…刃物を持ってきていた」); p0615, the arrest for 恐喝.
2. **Speaker, focalizer, chronology, disclosure.**
   - The V01 and V04 lines are confessions or accusations made inside a confrontation, focalized through Motoya.
   - The V05 prologue is the killer's first-person account, before disclosure. Its "demand about my past" is the victim's own wording.
   - The V05 and V07 extortion-killing sequences are Asumi's reconstructions at the reveal. Only the extortion half is corroborated: a recording in V07 (C04 p0572–p0589) and the prologue's "demand" in V05.
3. **Established and inferred.**
   - *Established:* extortion as a motive or immediate cause in V01 (fear of lifelong extortion, as 和枝 reports it), V04 (a confessed motive), V05 (the prologue's demand and the accusation; the admission covers only the blow) and V07 (extortion established; the killing reconstructed).
   - *Inferred:* the wider "silencing a would-be discloser" pattern across V02, V03 and V06 is CB1's thematic generalization. I did not re-verify it beyond the register's citations.
4. **Strongest competing explanation.** Extortion is a convenient plot engine, not a theme. GPT's thesis about care, credit and who carries truth already absorbs these cases as "exposure" motives (for example, V06 DEEP l.129, "Exposure provides a current motive"). This explains the GPT emphasis, but it does not explain the absence of any series-level statement about a structure recurring in four of seven killings.
5. **Verdict.** CONFIRM.
   - **Final disposition:** `GPT_OMISSION` (series theme); `GPT_COMPRESSION` (V01 H-0012 "the latter's pressure on household staff"; V05 introduction l.46 "press him about the hotel design").
   - The register slightly overstates one point. The integrated synthesis (l.40) does not simply "file" the assault under redress; it says the community's ways of seeking redress "are wider than the central assault". The sentence still frames 羽仁's blow as a form of redress and omits its money motive. V05 DEEP l.193 itself keeps "historical resentment, financial demand and moment of escalation distinct".
6. **Residual uncertainty.**
   - The V05 extortion rests on Asumi's reconstruction plus the prologue's unspecified "demand". The V01 motive is 和枝's report of 富田's words.
   - The thematic weight of "silencing" outside the four extortion volumes is moderate.
7. **Implications.**
   - `KSOA-SER-CL-0001` (causal roles) and `KSOA-SER-CL-0005` (selective accounts).
   - `studies/KSOA_INTEGRATED_SERIES_SYNTHESIS.md#the-work-people-leave-behind` and `studies/KSOA_MYSTERY_FORM_AND_CAUSALITY.md#direct-action-enabling-action-and-knowledge`.
   - `KSOA-V01-RES-0003`, `KSOA-V05-RES-0002`; CB1 `CB1-CL-045`–`047` (supported for the extortion half).
8. **Priority.** P2.
9. **Integration.**
   - (f) new `KSOA-SER-CL-0006`.
   - (c) correction notes on `KSOA-V01-RES-0003` and `KSOA-V05-RES-0002`.
   - (b) V05 introduction l.46.
   - (g) integrated synthesis l.40.
   - Wording in §3.

#### KCMP-SERIES-002 — CB1 uses the V07 recorded voice as counterevidence to the homicide attribution

1. **Passage.**
   - V07 C04 p0572: the recording is the extortion call, 「…月曜までに一〇〇万円を振り込めよ」.
   - p0574: 「ドスの利いた声は江口のものとは思えなかった。」
   - p0575: 「だが、声紋鑑定に出せば、すぐにわかる話だ。」
   - p0578: 「くそっ、あの女め」; p0583: 「まさかこんな録音が残っているなんて……」.
   - p0587–p0589: asked 「あなたの声と認めるのですね」, 江口 justifies the extortion and does not deny the voice.
2. **Focalizer.** Motoya's close third person: an auditory impression, immediately bounded by the voiceprint remark. The scene comes after the extortion recording surfaces and before the arrest (p0615).
3. **Established and inferred.** It is established that the voice is on an extortion call and that 江口's reactions acknowledge it. CB1's paraphrase of p0574 ("did not sound like 江口's") is literally close. The error is in relevance and weight: CB1 enters the line in `CB1-CL-038`'s "strongest counterevidence or competing reading" column, in `CB1-U-18`, and in LS §3.2 (V07 row, "Proof status") as a reason to doubt that 江口 killed 河村.
4. **Strongest competing explanation.** Read alone, p0574 could imply a second voice. p0575 and 江口's conduct rule this out, and even that reading would bear on the extortion rather than the stabbing.
5. **Verdict.** CONFIRM. **Final disposition:** `CLAUDE_ERROR`. It is an error of evidential weight; the quotation itself is not misread.
6. **Residual uncertainty.** None on this point. The legitimate limits on the homicide attribution stand: no confession on the page, an unnamed prologue agent (PRO p0030), and the forensic results promised but not shown (C04 p0605).
7. **Implications.** CB1 `CB1-CL-038`, `CB1-U-18`, LS §3.2 V07 row. No GPT dependency: GPT `KSOA-V07-H-0014` and `KSOA-V07-ACT-0002` ("substantiated through recordings and his acknowledgment") are correct.
8. **Priority.** CB1-only.
9. **Integration.** (h): record the erratum in the adjudication report (§3(h)).

#### KCMP-SERIES-003 — The V07 finale's evidential context

1. **Passage.**
   - V07 EPI p0131: 「そのうちに元哉の意識はなくなっていた。」 p0132: he comes to after eleven.
   - p0133–p0134: 泉田 and 英美里 are asleep.
   - p0135–p0142: 沙也香, drunk (p0136 「ろれつの怪しい舌で亜澄に」), and Asumi agree on a truce.
   - p0143: 「酔った二人は楽しそうに握手している。」
   - p0144: 「…あたし、こいつがいるから捜査やれるんだ」; p0145: 「まじめな顔で」.
   - p0146–p0148: Motoya's vow. p0149: 「元哉の意識はふたたび飛んでいた。」
2. **Speaker, focalizer, chronology, disclosure.**
   - Asumi speaks to 沙也香 in an ongoing two-person exchange. こいつ refers to Motoya in the third person.
   - The scene is focalized through Motoya, who has just come out of a blackout. Nothing says whether Asumi knows he is awake.
   - This is the last scene of the series, so no later evidence exists.
3. **Established and inferred.**
   - *Established:* both women are drunk; the statement is addressed to 沙也香; it is marked 「まじめな顔で」; Motoya overhears it, vows privately and blacks out again.
   - *Inferred:* the durability of either commitment, and whether Asumi meant to be overheard.
4. **Strongest competing explanation.** 「まじめな顔」 and the sincerely narrated vow make the line a sincere professional appraisal, and the drink makes it more candid, not less. This sustains a positive reading but does not remove the discount GPT itself applies to the V01 drunken epilogue (`KSOA-V01-CL-0005-R01`: "intoxication limit[s] projection").
5. **Verdict.** MODIFY. **Final disposition:** `GPT_OMISSION` (intoxication; both blackouts) plus `GPT_COMPRESSION` (addressee).
   - The register says nothing in GPT records the addressee. In fact V07 DEEP l.156 says "The two speech acts have different audiences", and `KSOA_PARTNERSHIP.md` l.25 says "Asumi tells those still awake at the counter".
   - GPT does register an audience asymmetry, but never names 沙也香 or records the drink. Its V07 introduction (l.48) also states the addressee wrongly (see KCMP-CHAR-007).
6. **Residual uncertainty.** How far the drink discounts the line is a judgment call. The sincere professional reading remains the best-supported one.
7. **Implications.**
   - `KSOA-SER-CL-0004` ("**High.** … Asumi's appreciation is spoken").
   - `KSOA-V07-CL-0006` ("voiced in company"); `KSOA-V07-REL-0005`.
   - `KSOA_PARTNERSHIP.md` l.25, and l.51 ("the explicit wording of their final exchange").
   - `KSOA_ASUMI_OGASAWARA.md` l.47 ("direct evidence about her estimate"); `KSOA_MOTOYA_KITSUKAWA.md` l.47 ("after hearing her explicit appreciation").
8. **Priority.** P2. The core claim survives, but its confidence and context are overstated. The factual error in the introduction is graded P1 under KCMP-CHAR-007.
9. **Integration.**
   - (f) `KSOA-SER-CL-0004-R01` (DOWNGRADE) and `KSOA-V07-CL-0006-R01` (REVISE).
   - (e) new `KSOA-V07-REL-0006`.
   - (a) V07 DEEP erratum.
   - (g) partnership study l.25 and l.51 and both lead monographs. Wording in §3.

#### KCMP-SERIES-004 — V06: the host's drugged sleep and the shouting test

1. **Passage.**
   - V06 C03 p0684–p0687: Asumi shouts for 小杉 without response. 「この部屋でかなり大声を出しても、二階の小杉さんの部屋には聞こえません」.
   - p0695: the alibi built on 小杉's and the taxi firm's arrival and departure times.
   - p0711: 薬師寺, 「八時頃から眠くて眠くて仕方なくなった。一二時過ぎまで寝ていて」.
   - p0717: 「薬師寺先生のシャンパンに睡眠導入剤を混入させましたね」.
   - p0721: the treating doctor's testimony on 久米's prescription has been obtained. p0722: 久米 denies any link.
   - EPI p0005: 「糟屋と久米はすべてを自供」.
2. **Speaker, focalizer, chronology, disclosure.** Asumi's charge at the confrontation, focalized through Motoya. The drug is disclosed only at the reveal. Before p0717 the reader has 薬師寺's claimed continuous presence; the epilogue reports confessions.
3. **Established and inferred.** It is established that 薬師寺 became overwhelmingly sleepy at about eight, that 久米 held a prescription, and that the shouting test shows the upstairs room cannot hear. The drugging is the investigation's charge and the novel's explanation, and the epilogue's summary confession covers it by implication. It is not separately confirmed.
4. **Strongest competing explanation.** 薬師寺 simply fell asleep from drink, and the prescription is coincidental (久米's denial, p0722). Then the alibi rests on a "common unsupported middle", as GPT has it (mystery study l.49). The novel's framing and the confessions favour the drugging.
5. **Verdict.** CONFIRM. **Final disposition:** `GPT_OMISSION`. Searches for drug, sedat, 睡眠, champagne, シャンパン, prescri, shout and 大声 return nothing relevant. `KSOA-V06-EV-0010` mentions "circumstantial support" without its content.
6. **Residual uncertainty.** The drugging is not independently confirmed on the page.
7. **Implications.**
   - `KSOA-SER-CL-0001`: the drugging is an enabling act missing from its support list.
   - The mystery study (l.43–49).
   - V06 DEEP l.129 and the introduction l.46 ("He slept").
   - The assessment of 薬師寺's culpability: drugged concealment differs from witnessing (`KSOA-V06-ACT-0004`). It also bears on the 薬師寺 qualification profile (§2B).
8. **Priority.** P2.
9. **Integration.**
   - (c) `KSOA-V06-ACT-0005`, `KSOA-V06-EV-0011`, and a note on `EV-0010`.
   - (a) V06 DEEP erratum.
   - (b) V06 introduction l.46.
   - (d) `KSOA-V06-ADJ-0003`.
   - (f) `KSOA-SER-CL-0001-R01`.
   - (g) mystery study.

#### KCMP-SERIES-005 — Institutional licence: linear development or variable reception

1. **Passage.**
   - V04 C01 p0889–p0893: 佐竹 says the line is off the 常道 but adds 「小笠原が読んだ筋から事件が解決したことは一回ではない」.
   - V06 C02 p0718–p0719: 「捜査幹部をはじめたいして興味を持つ捜査員はいなかった」, and the money line is preferred.
   - V07 C03 p0757: Asumi avoids a formal 意見具申. p0763–p0764: 「二階堂管理官は亜澄の考えに乗ってきた」. p0792: 「亜澄の考えは二つとも実現した」.
2. **Speaker and chronology.** Briefing scenes focalized through Motoya. 佐竹 appears only in V04 (36 occurrences there, none elsewhere). 二階堂 commands in V01–V03, V05 and V07, and 正木 is prominent in V05–V06.
3. **Established and inferred.** It is established that reception differs by commander and by case: V06's headquarters is uninterested after V04's wager, and V07 adopts her ideas. CB1's linear arc (`CB1-CL-054`; LS §4.3 trajectory sentence) is an inference that skips the V05–V06 rows of its own table. Its other conclusion, "each licence remains a personal decision", converges with GPT.
4. **Strongest competing explanation (for CB1).** 佐竹's remark shows a reputation built on seen cases, and V07 ends in adoption. A net upward trend is defensible as a tendency, though not as a stage sequence.
5. **Verdict.** CONFIRM. **Final disposition:** `INTERPRETIVE_DISAGREEMENT`, resolved toward GPT's variable-reception model (`studies/KSOA_POLICING_PLACE_AND_NARRATION.md#who-can-act-on-a-question`). CB1 overgeneralizes.
6. **Residual uncertainty.** Moderate. With so few data points, "trend with exceptions" against "case-dependent variation" cannot be settled.
7. **Implications.** CB1 `CB1-CL-054`, LS §4.3. The GPT position is already supported by `KSOA-V04-INST-0001` and `KSOA-V06-INST-0002`.
8. **Priority.** CB1-only. An optional P3 enrichment is to cite 佐竹's reputation remark in the policing study.
9. **Integration.** (h) CB1 erratum. (g) optional sentence in the policing study (§3).

#### KCMP-SERIES-006 — The bluff device and Asumi's credo at series level

1. **Passage.**
   - V02 C03 p0376–p0379: 彩音's 「卑劣だわ」, then the credo 「…違法でない手段はなんでも使います。たとえそれが人倫にもとるような行為であってもわたしは迷いません…」, at p0378.
   - Narrated bluffs: V01 C03 p0970 「亜澄のハッタリだ」; V03 C03 p0482 「元哉は亜澄のハッタリに驚いた」; V04 C03 p0549 「いわば亜澄のハッタリだ」; V06 C03 p0681 「これは亜澄お得意のハッタリだろう」.
   - Insinuation without a bluff: V05 C03 p0904.
   - Evidence threats that are not bluffs: V06 C03 p0726 and V07 C04 p0605–p0606 (「亜澄の言うことは間違いない」).
2. **Speaker and focalizer.** The credo is Asumi's own speech. The "bluff" labels are Motoya's focalized narration; at V06 「お得意の」 makes the habit explicit.
3. **Established and inferred.** It is established that Asumi states a means-justify ethic bounded by legality, and that the narration labels bluffs in four volumes, calling the move habitual in V06. That the device is a "series ethic of method" is analytical synthesis.
4. **Strongest competing explanation.** GPT treats the bluffs as local tactics properly recorded where they occur, in the readings and ledgers (`KSOA-V01-EV-0020`, `KSOA-V03-EV-0016`, V04 H-0012). V02 and V07 are not strictly bluffs.
5. **Verdict.** MODIFY. **Final disposition:** `GPT_COMPRESSION` only.
   - The register's secondary `GPT_OMISSION` for the credo does not hold. Frozen V02 DEEP l.173 paraphrases it: "Asumi defends an intrusive method as lawful in her view and necessary to get an answer."
   - What is lost is the clause accepting acts 「人倫にもとる」, its self-definition as a detective (「わたしは刑事なのです」), and any study-level or monograph-level treatment of the recurrent bluff.
6. **Residual uncertainty.** Low on the facts. Moderate on how central the device is to the series ethic.
7. **Implications.**
   - `studies/KSOA_POLICING_PLACE_AND_NARRATION.md#the-cost-of-making-a-truth-public`.
   - `studies/KSOA_MYSTERY_FORM_AND_CAUSALITY.md#three-kinds-of-closure`: closures produced by bluffs.
   - `studies/KSOA_ASUMI_OGASAWARA.md#the-costs-and-uses-of-control`; KCMP-CHAR-006.
8. **Priority.** P2. The method is central to Asumi's portrait and to closure mechanics.
9. **Integration.** (f) new `KSOA-SER-CL-0007`; (g) policing study, mystery study and Asumi monograph.

#### KCMP-SERIES-010 — "Kechika" misromanization

1. **Passage.** V04 C01 p0150: 「…｜姪《めい》｜御《ご》さんの｜森《もり》｜岡《おか》｜恵《え》｜智《ち》｜花《か》さんのことです」.
2. **Speaker.** Dialogue with authorial ruby, which is decisive for the reading.
3. **Established.** The name reads Morioka Echika.
4. **Competing explanation.** None. The form is a transcription slip that the producer review caught only for the introduction (`audits/KSOA_PRODUCER_REVIEW_AND_RECEIVING_HANDOFF.md` l.68).
5. **Verdict.** CONFIRM. **Final disposition:** `GPT_ERROR`.
6. **Residual uncertainty.** None.
7. **Implications.** Occurrences:
   - `readings/KSOA_V04_DEEP_READING.md` l.89, 99, 103, 127, 129, 137 (twice), 139, 203, 205, 211;
   - `KSOA_CASE_EVIDENCE_LEDGER.md` l.162 and 166;
   - `KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md` l.134;
   - `KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md` l.138 (`KSOA-V04-ADJ-0002`).

   Retrieval by the correct name fails in all four.
8. **Priority.** P1, as a factual error in current canonical material. Its severity is low and the fix is mechanical.
9. **Integration.** (a) erratum; (c), (e) correction notes; (d) `KSOA-V04-ADJ-0003`. Wording in §3.

#### KCMP-SERIES-011 — The V07 introduction genders the anonymous prologue agent

1. **Passage.** V07 PRO p0004–p0036. Impersonal monologue, 「どうすればいいのだ」 (p0020) and 「そう簡単に自分のしわざとわかるわけはない」 (p0030), with no pronoun, name or gender marker.
2. **Focalizer and disclosure.** The agent is unnamed throughout V07. The eventual attribution to 江口 is Asumi's reconstruction (C04 p0598–p0601), never confessed.
3. **Established and inferred.** It is established that the source keeps the agent ungendered. The introduction l.36 ("He considers seeking help… His identity…") narrows the field at the prologue boundary, and does so on the strength of an attribution the book never proves.
4. **Strongest competing explanation.** English needs a pronoun, and the eventual suspect is a man, so the pronoun asserts nothing false within the novel's explanation.
5. **Verdict.** MODIFY. **Final disposition:** `GPT_ERROR` (low severity), confined to the V07 introduction.
   - The register says this contradicts the producer review's anonymity claim. In fact the review (l.69) certifies that the opening voices "remain unnamed", which is still true.
   - No correction of the review is required. At most it needs a scope note that anonymity includes ungendered reference where the source is ungendered.
6. **Residual uncertainty.** The register used in the 「〜のだ」 self-talk leans conventionally masculine in Japanese fiction, but it is not a gender marker. Low.
7. **Implications.** V07 introduction l.36 only. The deep reading is neutral ("focal consciousness").
8. **Priority.** P1 under the brief's definition (an attributional error in canonical material), at low severity.
9. **Integration.** (b) V07 introduction l.36.

#### KCMP-CHAR-001 — Asumi's キミ and 元哉くん to Motoya

1. **Passages.**
   - V01 C01 p0776–p0777 「あれぇ、キミに彼女なんていたっけぇ？」 (小馬鹿にしたような亜澄の声).
   - V01 C01 p0047 「勉強不足なんだよ、キミは」.
   - V02 C01 p0236 「あたしはキミの指導役なんだよ」.
   - V02 C03 p0234–p0235 「キミのこころは汚れておる」 (亜澄の本音のような気がした).
   - V07 C01 p0012 「ここにキミと来るのは久し振りだね」; V07 EPI p0124.
   - 元哉くん: V01 C01 p0584, p0811; V02 C01 p0327 「元哉くん、よだれ」, p0890; V04 C01 p0046.
2. **Speaker and focalizer.** Asumi's direct speech, attributed in the surrounding narration. Mechanical counts of dialogue lines containing キミ, all speakers, run 11/10/5/1/0/0/2 by volume. One V03 epilogue line (p0097) is addressed to someone else.
3. **Established and inferred.** It is established that キミ is a frequent teasing-senior address in V01–V03, rare in V04, absent in V05–V06 and back in V07, and that 元哉くん is occasional. What the V05–V06 gap means (anger, with あんた rising, or drift) is inferred.
4. **Strongest competing explanation.** None that would remove the omission. GPT's `KSOA-V01-VOICE-0001` reads "familiar address", which could be taken to cover these forms without naming them.
5. **Verdict.** CONFIRM. **Final disposition:** `GPT_OMISSION`. A whole-corpus search returns キミ 0 and 元哉くん 1 (V01 DEEP l.97).
6. **Residual uncertainty.** The exact counts depend on whether lines or occurrences are counted; the distribution does not.
7. **Implications.** `KSOA_ASUMI_OGASAWARA.md` l.43 (speech paragraph); `KSOA_POLICING_PLACE_AND_NARRATION.md` l.53; the readiness audit's `VOICE` judgment; §5.5.1 responsibility 6.
8. **Priority.** P2.
9. **Integration.** (e) `VOICE` rows; (g) Asumi monograph speech section (§3).

#### KCMP-CHAR-002 — Motoya's おまえ to Asumi and its fade

1. **Passages.**
   - V01 C01 p0040 「おまえ、蘆名さんの小説読んだことあるのかよ」. Motoya is the speaker: his reply follows at p0045, and the narration at p0041 is about his own reading.
   - V01 C01 p0778 「うるせぇな。おまえだってオトコなんていないくせに」.
   - V05 C02 p0788–p0789 「元哉は本気で腹を立てた。」 「おい、小笠原、おまえ頭大丈夫か？」.
2. **Speaker.** Every other おまえ in V04–V07 is spoken by a superior: V04 C03 p0355; V05 C01 p0387, p0396, p0695; V06 C01 p0112–p0239, p0564–p0610; V07 C01 p0573; C04 p0641.
3. **Established and inferred.** It is established that Motoya calls Asumi おまえ often in V01 and rarely afterwards, with one later instance, in real anger, in V05. Respect, maturity or authorial drift as the explanation is inferred and stays open.
4. **Strongest competing explanation.** None for the distribution.
5. **Verdict.** CONFIRM. **Final disposition:** `GPT_OMISSION`. The search returns おまえ 0.
6. **Residual uncertainty.** The cause of the fade.
7. **Implications.** `KSOA_MOTOYA_KITSUKAWA.md` l.43 ("`俺` and surname address"); `KSOA-V01-VOICE-0002`; responsibility 6.
8. **Priority.** P2.
9. **Integration.** (e) `VOICE` rows; (g) Motoya monograph.

#### KCMP-CHAR-003 — Motoya's 僕 is a register from V05 on

1. **Passages.**
   - V05 C01 p0091 「今日の自分は不自然にいい子を演じている。」
   - V05 C01 p0213 「シーグラスも知らない僕なので…」.
   - V07 C04 p0189 「残念ですが、僕は刑事です」.
   - V07 C03 p0492–p0494: 「県警刑事部の吉川です。僕はエチオピアの豆です」 is a single utterance to 長坂, who answers in 僕 himself (p0495).
2. **Speaker.** Motoya. A heuristic scan of every V01–V04 dialogue line containing 僕 next to a 元哉 narration line found no Motoya use, apart from the parody at V03 C01 p1033.
3. **Established and inferred.** It is established that 僕 appears from V05, first with 沙也香 and 英美里 and with a narrated self-awareness of performing, and that GPT's "official introduction uses 吉川です, the coffee conversation with Nagasaka uses 僕" splits one utterance into two contexts. That 僕 was available before V05 but went unsampled is a possibility the source cannot settle.
4. **Strongest competing explanation.** Earlier volumes give Motoya few civilian peers of his own age to speak to, so the absence before V05 may reflect missing occasions, not a change.
5. **Verdict.** CONFIRM. **Final disposition:** `GPT_COMPRESSION`.
6. **Residual uncertainty.** As in step 4.
7. **Implications.** `KSOA_MOTOYA_KITSUKAWA.md` l.43; responsibility 6.
8. **Priority.** P2.
9. **Integration.** (e) `KSOA-V05-VOICE-0001`, `KSOA-V07-VOICE-0002`; (g) Motoya monograph sentence (§3).

#### KCMP-CHAR-004 — Asumi's formal and audience registers

1. **Passages.**
   - V02 C01 p0943–p0944: 「…わたくし神奈川県警鎌倉警察署の小笠原亜澄と申しますが」, 鼻へ抜けるように猫なで声.
   - p0949 「わたくしどもの手落ちです」.
   - V01 C02 p0472–p0473 「お電話代わりました、小笠原です」 (よそゆき声).
   - V02 C03 p0845–p0846 「こんにちは、小笠原亜澄ですぅ」 (甘ったるい声).
2. **Speaker and focalizer.** Asumi's speech. The voice-quality labels are Motoya's focalized narration.
3. **Established.** Asumi has a formal わたくし register for official apology and calls, and a marked sugary register, alongside あたし (with Motoya) and わたし (with others).
4. **Strongest competing explanation.** None for the omission.
5. **Verdict.** CONFIRM. **Final disposition:** `GPT_OMISSION`. The search returns わたくし 0. The GPT monograph has only 「鎌倉署の小笠原」.
6. **Residual uncertainty.** How far わたくし runs across volumes. CB1's own erratum E-05 puts it at V01–V04. I did not count by speaker.
7. **Implications.** As for KCMP-CHAR-001.
8. **Priority.** P2.
9. **Integration.** (e) `KSOA-V02-VOICE-0001`, `KSOA-V02-VOICE-0003`; (g) Asumi monograph.

#### KCMP-CHAR-006 — Asumi's credo and her use of confidences

1. **Passages.**
   - The credo at V02 C03 p0378 (see KCMP-SERIES-006), and the conditional confidentiality at p0465.
   - V05 C03 p0691–p0694: 榎本 「ここだけの話にしてくれますか」; Asumi 「もちろんです」, unconditional.
   - p0842: at the public gathering, 「わたしは、一八年前の黒い噂が事件の根幹にあると思います」.
   - p0926–p0927: Motoya thinks 「亜澄は意地が悪い」 and asks whether everything needed exposing.
   - p0973: Asumi apologizes for her 「失礼なこと」.
2. **Speaker and focalizer.** Asumi's speech; Motoya's interior judgment. This is the climax of V05.
3. **Established and inferred.** It is established that Asumi gives an unconditional promise of discretion and later grounds a public confrontation on the rumour it protected. The text does not say whether she attributes the rumour to 榎本, or whether the use breaches her stated V02 condition (「捜査でどうしても必要となったら」). That is analytical judgment.
4. **Strongest competing explanation.** The public use rests on corroboration, not on 榎本's confidence. This is weak. 恵美子's confirmation comes only after Asumi raises the rumour (p0845 「奥さま、教えてください。製図が盗まれたことは事実なのですか」; V05 DEEP l.189), and Asumi does not name her source. She may also count investigative necessity as within her V02 condition.
5. **Verdict.** CONFIRM. **Final disposition:** `GPT_COMPRESSION`.
   - GPT records the confidence and the request to limit circulation (V05 DEEP l.183: "asks the pair to limit circulation").
   - It also records the gathering's audience cost (policing study l.39) and V03's "breach of a witness assurance" (`KSOA-V03-CL-0006`).
   - It never links promise and use, and paraphrases the credo only (V02 DEEP l.173).
6. **Residual uncertainty.** Whether V05 counts as a breach (step 4).
7. **Implications.** `KSOA_ASUMI_OGASAWARA.md#the-costs-and-uses-of-control`; `KSOA-SER-CL-0005`; responsibilities 3 and 5.
8. **Priority.** P2.
9. **Integration.** (e) `KSOA-V05-CH-0005`; (g) Asumi monograph (§3).

#### KCMP-CHAR-007 — V07 epilogue: addressee and state

1. **Passage.** V07 EPI p0131–p0149, as under KCMP-SERIES-003. The conversation is between 沙也香 and Asumi (p0135–p0143). こいつ (p0144) refers to Motoya in the third person.
2. **Speaker and focalizer.** Asumi, drunk (p0143), speaks to 沙也香. Motoya overhears after coming to (p0132).
3. **Established.** The addressee is 沙也香, and both women are drunk. The GPT introduction l.48, "Asumi tells Motoya that she can do the work because he is there", misstates the addressee.
4. **Strongest competing explanation.** 「吉川くん、」 could be a vocative addressed to him. Against that, こいつ in the same utterance and the two-way exchange with 沙也香 make the topic-fronted, third-person reading clearly better.
5. **Verdict.** CONFIRM. **Final disposition:** `GPT_ERROR` (V07 introduction) and `GPT_OMISSION` (intoxication, corpus-wide).
6. **Residual uncertainty.** Whether Asumi knew he was awake is unstated.
7. **Implications.** As under KCMP-SERIES-003, plus `KSOA_ASUMI_OGASAWARA.md` l.47.
8. **Priority.** P1, for the factual error in a canonical introduction.
9. **Integration.** (b) V07 introduction l.48; also the (a), (e), (f) and (g) actions under KCMP-SERIES-003.

#### KCMP-CHAR-008 — How much independent agency Motoya has

1. **Passages.**
   - V04 C03 p0406–p0410: Asumi points to the car, and Motoya identifies it, 「たしかに七条邸のカーポートに駐まっていたな」.
   - p0426 「反対方向もあるはずだ」, followed by his own route reasoning (p0427–p0431) and Asumi's brightening (p0432).
   - p0473–p0474: 「まずは、わたしと小笠原で直接、宮崎の事情聴取をしたいと思います」 (毅然とした態度で).
   - V06 C03 p0303: his taxi-firm check.
   - V07 C04 p0302: 「もっとちゃんと見なさいよ」, a prompted recognition.
   - V07 C04 p0645: 「すべては亜澄の功績だ。」
2. **Focalizer.** Motoya's close third person. The V04 route reasoning is narrated as his own thought.
3. **Established and inferred.** It is established that the V04 direction proposal, the request to interview and the V06 checks originate with him, while the decisive solutions are Asumi's. How much these contributions weigh is analytical.
4. **Strongest competing explanation (for CB1).** Motoya's moves are bounded and supporting, and he himself credits Asumi with everything (p0645). This is true as self-assessment, but it does not make the V04 proposal "prompted".
5. **Verdict.** CONFIRM. **Final disposition:** `INTERPRETIVE_DISAGREEMENT`, resolved toward GPT (`KSOA_MOTOYA_KITSUKAWA.md` l.31, l.33), with a minor `CLAUDE_ERROR`.
   - CB1 MM §12's "prompted" fits the Alto identification, not the direction proposal.
   - CB1 MM §0's "bounded supporting moves" is also inconsistent with CB1 PS §1 and §3.5, which call the reversed camera direction "decisive".
6. **Residual uncertainty.** Low.
7. **Implications.** CB1 MM §0 and §12; PS §1 and §3.5. No GPT change.
8. **Priority.** CB1-only.
9. **Integration.** (h).

#### KCMP-CHAR-010 — The GPT lead monographs measured against §5.5.1

1. **Evidence.**
   - Both GPT files read in full. Front matter: `artifact_type: character_monograph`, `status: canonical`, `created: "2026-11-13"`.
   - The scope lines are question-led ("Asumi's investigative judgment, register, professional authority and vulnerability…").
   - Policy v1.12, which adds §5.5.1, is dated 2026-11-14 (register §2A.1).
2. **Applicable rules.**
   - §5.5.1 Purpose: "Any document typed or presented as a character's canonical individual portrait is a substantive monograph for this standard."
   - §10: such a monograph, created before the standard, is grandfathered. Nonconformance "is not by itself a correction duty". The standard binds a general revision or a superseding monograph, and an erratum or selective update applies it only to the content changed.
3. **Established.**
   - Coverage. Speech (6) is one paragraph each. This is the listed failure "lists a few pronouns but leaves conversational style to another document", and the paragraph is also incomplete: see KCMP-CHAR-001 to -004.
   - Romance (9) is absent for Asumi and limited to the Emiri misreading for Motoya. Operational profile (12) is absent for both.
   - Personal history (2) is thin at monograph level. Asumi's mother's death (V03 DEEP l.153) and hospital fear (V01 DEEP l.105) are in the readings but not in her monograph.
   - Each relationship section ends by sending the reader to the partnership study, which approaches the second usability failure.
   - Strengths: cognition (4), evidence traceability (14) and thematic integration.
4. **Strongest competing explanation.** The register argues that the files are legitimate question-led studies outside the standard's responsibility. I reject that as an exemption. Their declared type and canonical status make them substantive monographs, so the §10 clause on "existing studies that carry a different legitimate analytical responsibility" does not cleanly apply. Grandfathering, not exemption, is the correct status.
5. **Verdict.** MODIFY. **Final disposition:** `GPT_COMPRESSION` plus `GPT_OMISSION` (responsibility 9 for Asumi; 12 for both). Two corrections to the register:
   - A missing profile is a coverage failure under responsibility 12. It is not the listed usability failure, which concerns profiles made of abstract adjectives.
   - The grandfathering rationale is as in step 4.
6. **Residual uncertainty.** Whether a Phase 4 integration that adds several sections amounts to a "general revision", which requires full conformance, or a "selective update", which applies the standard to the changed content only. The integrator must decide and record that before editing.
7. **Implications.**
   - Neither GPT monograph may be recorded `COMPLETE_AT_BOUNDARY`.
   - A readiness or release audit may not describe the character layer as complete (§5.5.1, production obligation).
   - Only one current portrait per character is allowed. CB1 material must enter through a GPT successor or a selective revision, never as a parallel current portrait.
8. **Priority.** P2.
9. **Integration.** (g) monographs, by bounded successor or deepening pass under long-series protocol §12, or by selective updates for KCMP-CHAR-001 to -007 and -012. Record the choice in the claim ledger (f) (§3).

#### KCMP-CHAR-011 — No qualification decisions in the GPT corpus

1. **Evidence.**
   - A whole-corpus search for `qualif`, `5.5.1` and `self-contained` finds ordinary usage only.
   - `KSOA_SYNTHESIS_ARCHITECTURE.md` l.73 ("Create monographs for subjects with distinct developmental or interpretive questions and sufficient independent evidence") is a pre-standard criterion.
   - `audits/KSOA_ARCHITECTURE_ROLE_GAP_AUDIT.md` l.47 assigns Ayane, Mitsuki, Shichijō and Shiobara to volume readings ("would need a separate, narrower question").
2. **Applicable rules.**
   - §5.5: where person-level synthesis is in scope, the architecture names where qualification decisions are recorded, and "may not exclude a character whom the evidence qualifies".
   - §10: an established project records decisions "when it next enters character or specialist synthesis, or at its next architecture review checkpoint".
3. **Established.** No record, outcome vocabulary, named home or triggers exist. The role-gap audit's treatment of Shichijō is a pre-standard routing judgment, not a §5.5.1 decision: it records no outcome, rationale with gaps, or trigger. Under §5.5 it cannot keep out a character whom the evidence qualifies (my verdict in §2B is QUALIFIED_PENDING).
4. **Strongest competing explanation.** No obligation has yet fallen due, because the project has not re-entered character synthesis since v1.12. This is correct; the omission is an outstanding obligation, not a breach. It falls due when the integrator revises any monograph.
5. **Verdict.** CONFIRM. **Final disposition:** `GPT_OMISSION`.
6. **Residual uncertainty.** None on the facts.
7. **Implications.** `CURRENT_STATE_AND_CORPUS_MAP.md` (no routing to an outstanding obligation); any readiness or release audit.
8. **Priority.** P2.
9. **Integration.** (g) qualification record plus an architecture home, as described in §3. The record must carry GPT's own evidenced judgments; §2B supplies source-checked seeds, not results to copy.

#### KCMP-CHAR-013 — V02 introduction: Ayane files no complaint about Asumi

1. **Passages.**
   - V02 C03 p0478: 石川's embezzlement.
   - p0480–p0482: 「被害届を出してくださいますか」; 「お約束を守ってくださるなら、被害届はもちろん出します」.
   - p0524–p0526: the 知能犯係 takes the 被害届.
   - Searches across V02 for 苦情, 抗議, 告訴 and 訴え find nothing directed at Asumi.
2. **Speaker.** 彩音 and Asumi; Motoya-focalized.
3. **Established.** 彩音 files a criminal complaint about 石川, conditional on the detectives keeping their promise.
4. **Strongest competing explanation.** "Complaint" in GPT is shorthand for the 被害届. That rescues V02 DEEP l.173 ("files a complaint") and the Asumi monograph l.37 ("later separate complaint"), but not the introduction's "complaint about Asumi".
5. **Verdict.** CONFIRM. **Final disposition:** `GPT_ERROR` (introduction). The other wording is ambiguous but correctable.
6. **Residual uncertainty.** None.
7. **Implications.** `KSOA-V02-CH-0004` ("pursues her own complaint") and `KSOA-V02-REL-0007` are correct. V02 DEEP l.173's "nonetheless" is misleading: she files on condition of the promise.
8. **Priority.** P1.
9. **Integration.** (b) V02 introduction l.42; (a) erratum to V02 DEEP l.173; (g) Asumi monograph l.37 wording.

#### KCMP-CHAR-014 — Character-ledger metadata and the VOICE layer

1. **Evidence.**
   - `KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md` front matter: `source_boundary` "… Narrative admission and inspection are pending."
   - l.22: "**Analytical rows at initialization: 0.**"
   - `VOICE` rows exist only as `KSOA-V01-VOICE-0001`/`0002`. A `CH` kind is used in V02–V07 (31 rows) but not defined in the schema table.
2. **Context.** `audits/KSOA_PRODUCER_REVIEW_AND_RECEIVING_HANDOFF.md` l.46: the ledgers "preserve the terminal bytes, including initialization headers", deliberately.
3. **Established.** The headers are stale but deliberately preserved. The `VOICE` layer stops after V01, and `CH` is undocumented.
4. **Strongest competing explanation.** Preserving the headers is a legitimate provenance choice. It is, but the misleading reading should still be neutralized.
5. **Verdict.** MODIFY. **Final disposition:** `GPT_OMISSION` (the VOICE layer for V02–V07) plus presentation (`CH` kind).
   - The stale headers are a documented preservation, not an error to fix in place. A neutralizing note is enough.
   - The register's call for a "metadata correction through the authorized route" is narrowed accordingly.
6. **Residual uncertainty.** None.
7. **Implications.** Readers of the ledger alone; readiness `VOICE`.
8. **Priority.** P3. The substantive speech omissions are graded P2 under KCMP-CHAR-001 to -004.
9. **Integration.** (e) a schema note defining `CH`; a header note; `VOICE` rows (§3).

#### KCMP-CHAR-015 — Errors in CB1's non-lead monographs

1. **Passages.**
   - *Shichijō.* V04 C02 p0698: 晶子 says she has not met 洋介 since her 1961 retirement except at his death. C02 p0713: 「一二年ぶりにお会いして」. The span is 1961 to his 1973 death (C01 p0818; C01 p0226). C03 p0716 gives the secret meeting, and C03 p0733 the narration: 「引退後、関川洋介には死んだときにしか会っていないと晶子は言っていたが、あれは偽りだった。」
   - *Satomi.* V02 C03 p0932: 「彼女も亜澄の計画を知っているとしか思えなかった」, Motoya's inference. Against it, `CB1_SATOMI_YOSHIHISA_MONOGRAPH.md` l.180: "Asumi told 彩音 of the trap in advance but not him".
   - *Gamō.* V01 C03 p1066: 秀之 himself renounces the succession to 敦司. At p1074–p1084 隆鄕 accepts this, keeps him on merit, and grounds his love partly in blood (「貴子の血を継いでいるのだぞ」). Against it, `CB1_GAMO_TAKASATO_MONOGRAPH.md` l.28: "His conduct refutes their expectation that a patriarch guards his bloodline."
2. **Speakers and focalizer.** 晶子's own testimony, with the narration's correction. Motoya's inference. 秀之's and 隆鄕's speech.
3. **Established.**
   - The "12 years" is the lie itself, not "one striking true detail" (`CB1_SHICHIJO_AKIKO_MONOGRAPH.md` l.93). The masked attendance at the wake may be true.
   - The Satomi sentence states Motoya's inference as fact.
   - The Gamō sentence overreaches: the bloodline expectation is in effect fulfilled, through 敦司, at 秀之's own initiative.
4. **Strongest competing explanation (Gamō).** 隆鄕's laughter and his embrace of a non-blood grandson do defeat the stereotype of the "proud tycoon". That supports a narrower claim about affection and dignity, not "refutes … guards his bloodline".
5. **Verdict.** CONFIRM. **Final disposition:** `CLAUDE_ERROR` (minor). The Shichijō evidence is stronger than the register gave: the narration says so explicitly at C03 p0733. The smaller items reported by the sub-agents were not re-verified.
6. **Residual uncertainty.** Low for the three items. The smaller items are unverified here.
7. **Implications.** A correction checklist for any GPT monograph seeded from CB1 (§2B).
8. **Priority.** CB1-only.
9. **Integration.** (h).

### 2B. Monograph standard (§5.5, §5.5.1, §10) and qualification verdicts

#### 2B.1 Adjudication of the CHAR register's §2A findings

| Register finding | Adjudication | Basis |
|---|---|---|
| §2A.1: the GPT studies are grandfathered; CB1 was written to the pending text | **CONFIRM, with a correction.** The GPT files are typed `character_monograph` and `status: canonical`, so under §5.5.1 they are substantive monographs, not studies outside the standard. They are grandfathered because they predate policy v1.12. A general revision or a superseding monograph must conform in full; errata and selective updates must conform for the content they change | §5.5.1 Purpose; §10 l.840–849 |
| §2A.2: the coverage table | **CONFIRM for GPT**, with four precisions: (6) the speech paragraphs are incomplete as well as brief (KCMP-CHAR-001 to -004), and Motoya's paragraph splits one utterance into two contexts; (2) history known to the readings is missing at monograph level (Asumi's mother's death, her hospital fear); (9) Asumi: absent, and Motoya: Emiri only (his V01 bodily response appears only in the ledger, `KSOA-V01-STATE-0005`); (12) absent. **CB1 "Full" ratings are confirmed only structurally.** Both CB1 lead monographs have a section for each of the fourteen responsibilities (section headings checked: Asumi §2–§17; Motoya §2–§16). I did not re-read them in full, and their fidelity remains unaccepted (row below) | GPT files read in full; CB1 headings and spot checks |
| §2A.2: single-document usability | **MODIFY.** GPT commits failure 3 (speech) and approaches failure 2 (relationships routed to the partnership study). A missing behavioural profile is a coverage gap under responsibility 12, not failure 4, which concerns profiles built from abstract adjectives. Failures 1 and 5 are not committed. CB1: no failure observed in its structure | §5.5.1 Single-document usability |
| §2A.2: acceptance properties | **CONFIRM.** GPT has no recorded acceptance review. CB1 recorded both properties for v1: Asumi self-containment CONDITIONAL and fidelity REVISE; Motoya self-containment PASS and fidelity FAIL (`05_monographs/review/`). The v2 texts carry only "Re-review pointers" (Motoya monograph l.1171) and were not re-reviewed. None of the seven non-lead CB1 monographs has any review file. **No monograph in either corpus can be recorded `COMPLETE_AT_BOUNDARY`** | §5.5.1 Acceptance |
| §2A.3: GPT records no qualification decisions | **CONFIRM** (KCMP-CHAR-011). The obligation is outstanding, not yet breached, and falls due when the project next enters character synthesis | §10 l.847 |
| §2A.4: non-lead outcomes | **CONFIRM all seven as QUALIFIED_PENDING** (verdicts below). I would not label 里見 "narrow" against the others. He is the closest to the threshold, but he passes on constraints | Source spot checks below |
| §2A.4: deferred list (宮崎, 彩音, 二階堂, 吉田) | **CONFIRM DEFERRED_EVIDENCE.** 宮崎 has a rich confession (V04 C03 p0937 「晶子さまは俺の女神さまなんだ」; p0941, his sister), but most of his portrait rests on one sequence. Reassess after a targeted re-read of the V04 C02 gate scene and the C03 cottage scene | QR §6.2; source |
| Closing line: neither GPT monograph meets §5.5.1 and the character layer cannot be called complete | **CONFIRM** | §5.5.1 production obligation |

#### 2B.2 Qualification verdicts for the nine characters

Test (§5.5.1): convergent evidence; meaningful variation across contexts or interlocutors; constraints or counterexamples that rule out a generic sketch. Prominence does not decide.

**Status note.** In the GPT corpus all nine are `QUALIFIED_PENDING`. The two lead studies exist but do not meet the standard, have not passed acceptance review, and are grandfathered, so the obligation remains outstanding. The seven non-leads have no GPT monograph at all. The CB1 monographs are noncurrent seeds, and the corrections in KCMP-CHAR-015 must be applied before reuse.

| # | Character | Verdict | Rationale (verified anchors) | Largest gaps | Next review trigger |
|---|---|---|---|---|---|
| 1 | 小笠原亜澄 Asumi Ogasawara (V01–V07) | **QUALIFIED_PENDING** (conforming monograph outstanding) | *Convergence:* seven volumes of investigative initiative, pressure and repair. *Variation:* あたし/わたし/わたくし; キミ/吉川くん/あんた/元哉くん by audience and mood (V01 C01 p0776; V02 C01 p0943; V06 C01 p0652); a sugary register (V02 C03 p0845). *Constraints:* a legal-limit credo (V02 C03 p0378) alongside habitual bluff (V06 C03 p0681) and kept limits (V02 C03 p0465); apology for her methods (V05 C03 p0973); a drunk truce (V07 EPI p0141–p0143) | Her interior is never narrated, so every motive is inference; the hospital fear (V01 C01 p0744) is never explained; there is no sober, direct statement about the partnership | Before any general revision of `KSOA_ASUMI_OGASAWARA.md`; on any erratum to her lead records |
| 2 | 吉川元哉 Motoya Kitsukawa (V01–V07) | **QUALIFIED_PENDING** | *Convergence:* the focalizer throughout, with certified sincerity (V01 C01 p0979 「これは元哉の本音だった。」). *Variation:* おまえ fading after V01 (V05 C02 p0789 the last); 僕 from V05 with civilian women (V05 C01 p0091, p0213); a mock rank title (V01 C01 p0057). *Constraints:* real independent moves (V04 C03 p0426, p0473) against self-effacement (V07 C04 p0645); a misjudgment of 英美里 corrected (V07 EPI p0088) | The V05 "old wound" (V05 C01 p0061) is never revisited; family appears only by report (V06 C02 p0515); career aims are thin | As for Asumi |
| 3 | 滝川沙也香 (V05–V07) | **QUALIFIED_PENDING** | *Convergence:* wit as pressure in three volumes and four settings. *Variation:* 吉川さん to Motoya, with 元哉くん used only to provoke Asumi (V06 EPI p0013); 小河原さん (V06 C01 p0291) and あんた (V07 C02 p0039) to Asumi. *Constraints:* she defeats a "rival" sketch by disclosing the alibi (V07 EPI p0122) and making the truce (p0139–p0142); she is opaque even to Motoya (V05 C01 p0057 「どこまで本気で話しているかわからなかった」). Nuance for a monograph: in V06 EPI it is Asumi who opens the 資格 quarrel (p0015) and 沙也香 who coins デートぉ (p0008) | She never appears without Motoya; she has no interior; her feelings toward him are unestablished; her history is minimal | Any admitted source featuring her; any erratum to the V06 or V07 epilogue readings |
| 4 | 波多野英美里 (V05–V07) | **QUALIFIED_PENDING** | *Convergence:* she withholds twice and then discloses through Motoya (V06, V07), giving her own reason (V06 C03 p0134 「警察は怖いという印象を抱いてしまった」) and a self-description (V06 C03 p0170 「…ひたすら困っているばかりだった」). *Variation:* lecturer, mourner, pleader, bride (V07 EPI p0088). *Constraints:* quiet anger and conviction under pressure (V07 C04 p0170–p0171 静かな怒り; p0198) rule out "soft and pliable" | Her relationship with 泉田 is off the page until V07 EPI; she has no interior; her family is thin | Any admitted source featuring her |
| 5 | 蒲生隆鄕 (V01) | **QUALIFIED_PENDING** (bounded, concentrated) | *Convergence:* candour, humour and loyalty across four scenes. *Variation:* 俺/おまえ only to the coffin (V01 C01 p0943); わたし to the police; 「馬鹿者」 and an embrace for 秀之 (C03 p1084–p1089). *Constraints:* a realist glad of tuberculosis (C03 p0063); laughter at the paternity reveal (p1051–p1055); a meritocrat who keeps a non-blood grandson on merit (p1074). The monograph must **not** claim he "refutes" bloodline succession: 秀之 renounces it (p1066), and 隆鄕 grounds his affection partly in blood (p1084) | One volume, one phase of life; his wartime history is self-reported; no interior | Only if new source features him |
| 6 | 里見義尚 (V02) | **QUALIFIED_PENDING** (bounded; the closest to the threshold) | *Convergence:* testimony and conduct agree on his dependence on 三浦 and his generosity. *Variation:* he admires the detectives (V02 C03 p0392); his address to the dead concertmaster changes (倫人くん from p0423); he urged 石川 three times to give himself up and kept it from 彩音 (p0503). *Constraints:* concealed deafness re-explains the "difficult maestro" reputation, which is a revelation, not development | Much of his pre-disclosure register is mediated by 彩音; the motive for his benefaction is unconfirmed; daily life is absent. Correct the CB1 seed on the trap (KCMP-CHAR-015) | Only if new source features him |
| 7 | 鰐淵一遥 (V03) | **QUALIFIED_PENDING** (bounded, concentrated) | *Convergence:* candour about his own vices and absolutism about art (V03 C01 p0854, p0981). *Variation:* avuncular to the police, a painter to Asumi (p0992), lament and judgement in C03 (p0412 「器がちいさい」). *Constraints:* a self-styled coward (C03 p0126) who also kept 茉莉子 in his studio (p0124); a change of view within the volume. The monograph must include GPT's power-asymmetry reading as a required competing interpretation (KCMP-CHAR-016) | One volume, and he is dying; his 1990–94 account is uncorroborated testimony | Only if new source features him |
| 8 | 七条晶子 (V04) | **QUALIFIED_PENDING** (bounded; the strongest case-local candidate) | *Convergence:* sixty years of concealment, attested by four witnesses. *Variation:* gracious, then curt (V04 C02 p0756), then confessing (C03 p0700). *Constraints:* she lies firmly to keep her own secret (C02 p0698, p0756; narration C03 p0733 「あれは偽りだった」) but confesses for another's fate, and judges herself severely (C03 p0768 「二つの大罪」) | One volume; her 1961 decisions are known only through her confession and her helpers. Correct the CB1 seed on 「一二年ぶり」 (KCMP-CHAR-015) | Only if new source features her. The pre-standard routing in the GPT role-gap audit (l.47) does not exclude her (§5.5) |
| 9 | 薬師寺国昭 (V06) | **QUALIFIED_PENDING** (bounded) | *Convergence:* possessive paternal love and the school above persons. *Variation:* commanding with the police; peremptory with his pupils (V06 C03 p0644). *Constraints:* he spreads the pupils' false story (p0444) yet judged 野中 fit to succeed (p0644); he lied to shield the killers (p0705) and recognizes his folly (p0739). His drugged sleep (C03 p0711, p0717; KCMP-SERIES-004) bears directly on what he witnessed and what he concealed, and must be in the portrait | One volume; the backstory comes through testimony; the aftermath is one sentence (EPI p0006) | Only if new source features him; on integration of KCMP-SERIES-004 |

### 2C. Short notes on the remaining records (all CONFIRM)

- **KCMP-SERIES-007 (P3).**
  - V03 PRO p0034 「いっそすべてを終わりにしたい」 and p0035 「今夜、この峠から澄んだ夜空に舞い上がりたい」 voice explicit suicidal ideation in 茉莉子's first person. GPT V03 DEEP l.81 calls this "a wish for escape".
  - The homicide revision is well supported. The hidden text (C03 p0339 「右手で茉莉子に罪を償わせ」) and 圭子's report of her father's letter (p0407: 父が…成就院の階段から突き落とした) both point to it, though the letter is reported, not shown.
  - Suicidal intent and a push are compatible. Keep "probable homicide" and name the ideation as a bounded competing reading.
- **KCMP-SERIES-008 (P3).** Confirmed at V02 C01 p0014 and p0165–p0170 (高梨's vantage), p0174 (back to Motoya); V05 C02 p0843–p0845 (Asumi's interior inferred by Motoya: 「勘違いしていた」); V04 C03 p0972–p0974 (a scene break withholds 宮崎's account). GPT handles these openings case by case (policing study l.51) but never states the rule.
- **KCMP-SERIES-009 (P3).** Confirmed by direct counts. 「悪魔が囁」 occurs only at V02 C03 p1019 and V03 C03 p0527. Name reuse: 野中兼司 (V03) / 野中重之 (V06); 若尾茉莉子 (V03) / 宇都宮茉莉子 (V04) / 若尾昌史 (V05); 相木 (V02, 126 occurrences) / 相木昌史 (V04). GPT uses "motif" only in its method file and has no name-reuse note.
- **KCMP-SERIES-012 (CB1-only).** Counts in V01: 遺書 ×7, 告白 ×15, 告解 ×15. GPT's distinction (`KSOA_INTEGRATED_SERIES_SYNTHESIS.md` l.30; policing study l.37) has no CB1 counterpart beyond scene facts (V01 readings; the `05_monographs/work` dossier). Preserve it as a GPT contribution.
- **KCMP-CHAR-005 (P3).**
  - V01 C01 p0899 「亜澄はイケメンに弱い。」 and V03 C01 p0280 「この女はとかくイケメンに弱い。」 are Motoya-focalized narration.
  - V03 C02 p0723–p0724 gives his taunt and her denial 「デレデレしたことなんて一回もないし」.
  - Record it as Motoya's narratorial view, recurring in V01–V03, never as an established trait of hers.
- **KCMP-CHAR-009 (P3).** V01 EPI p0067 「心地よく感じてしまった自分を元哉は呪った。」; V05 C01 p0060 (his narrated interest in 沙也香, held at a distance); V01 C01 p0024 (a qualified appraisal). GPT's conclusion (`KSOA_PARTNERSHIP.md` l.51) is sound. It omits the directional asymmetry: for Motoya toward Asumi, the counterevidence is affirmative.
- **KCMP-CHAR-012 (P3).** V04 C01 p0734; V07 C03 p0481 「豆を選んでから挽いてもらうスタイルは、亜澄も大変に気に入っている。」 (「も」 implies Motoya shares the taste). コーヒー occurs 9/8/4/17/14/7/15 times across the volumes; GPT has one "coffee".
- **KCMP-CHAR-016 (CB1-only).** GPT V03 DEEP l.226 ("a projection that displaces the young woman's creative gifts and material choices") rests on the source (V03 C03 p0111 「貧乏だった茉莉子」; p0124). It is an interpretation, not a stated fact, and should carry that label in any seeded monograph.

---

## 3. Integration action list (grouped by destination type)

Wording is proposed and may be adjusted to house style, but every locator was verified. Records KCMP-SERIES-004, -010 and -011, KCMP-CHAR-007 and -013 may also appear in the Group A–C volume registers; the integrator should apply each change once.

### (a) Frozen deep readings: errata only, never edited

| Target | Action | Proposed erratum text |
|---|---|---|
| `readings/KSOA_V07_DEEP_READING.md`, H-0015 and the paragraph at l.156 (KCMP-SERIES-003, KCMP-CHAR-007) | Erratum | "Context omitted at EPI p[0131]–p[0149]: Motoya had blacked out from drink (p[0131]) and came to after eleven (p[0132]). Asumi's line 「…あたし、こいつがいるから捜査やれるんだ」 (p[0144]) is said to Sayaka, about Motoya, while both women are drunk (p[0143] 「酔った二人」); it is marked 「まじめな顔で」 (p[0145]). Motoya overhears it, resolves privately to support her (p[0146]–p[0148]) and blacks out again (p[0149]). Whether Asumi knew he was awake is not stated." |
| `readings/KSOA_V06_DEEP_READING.md`, the paragraph at l.129, H-0010 (KCMP-SERIES-004) | Erratum | "Omitted mechanism: Yakushiji says he became overwhelmingly sleepy from about eight and slept past midnight (C03 p[0711]). Asumi charges Kume with putting a sleep-inducer in Yakushiji's champagne (p[0717]) and cites the treating doctor's testimony about Kume's prescription (p[0721]); Kume denies any link (p[0722]). Her earlier shouting test shows that Kosugi's upstairs room cannot hear the party room (p[0684]–p[0687]). The drugging is the investigation's finding, covered by the epilogue's summary confession (EPI p[0005]), not an independently shown fact." |
| `readings/KSOA_V04_DEEP_READING.md`, all "Kechika" occurrences (l.89, 99, 103, 127, 129, 137, 139, 203, 205, 211) (KCMP-SERIES-010) | Erratum | "Name correction: 森岡恵智花 is read Morioka **Echika** (ruby ｜恵《え》｜智《ち》｜花《か》, C01 p[0150]). Every occurrence of 'Kechika' in this reading refers to her." |
| `readings/KSOA_V03_DEEP_READING.md`, l.81 (live questions) and l.195 (KCMP-SERIES-007) | Erratum | "Precision: the prologue's last lines state a wish to end everything and to 'fly up into the clear night sky from this pass' (PRO p[0034]–p[0035]), an explicit suicidal ideation, not only 'a wish for escape'. The later homicide inference rests on Yuhara's hidden text (C03 p[0339]) and on Keiko's report that his letter says he pushed Mariko down the Jōju-in steps (C03 p[0407]). The prologue's intent and a push are compatible; the fall itself is never shown." |
| `readings/KSOA_V02_DEEP_READING.md`, l.173 (KCMP-CHAR-013; KCMP-SERIES-006) | Erratum | "Precision: the 'complaint' Ayane files is a criminal complaint (被害届) about Ishikawa's embezzlement, which she makes conditional on the detectives keeping their promise (C03 p[0480]–p[0482]); the station's fraud squad receives it (p[0525]). No complaint about Asumi is filed. Asumi's defence of her method is stated in full at p[0378], including that she will not hesitate even over acts 「人倫にもとる」, within the limit of legality." |
| `readings/KSOA_V01_DEEP_READING.md`, H-0012 (KCMP-SERIES-001) | Erratum (optional; ledger note preferred) | "Precision: the 'pressure on household staff' is a threat to expose Tomita's and Kazue's embezzlement (C03 p[0897]). Kazue quotes Tomita's stated reason for killing as fear of lifelong extortion: 「一生食いつかれて強請られるんだ。殺すしかない」 (p[0977])." |

### (b) Reading introductions (`active_provisional`): targeted edits

| Target | Current text | Proposed replacement |
|---|---|---|
| `readings/KSOA_V07_READING_INTRODUCTION.md` l.48 (KCMP-CHAR-007) | "Asumi and Sayaka shake hands. Asumi tells Motoya that she can do the work because he is there. Motoya hears her and privately resolves to keep supporting her." | "Asumi and Sayaka, both drunk, shake hands. Motoya, who has come to after passing out, hears Asumi tell Sayaka that she can do the work because he is there. He privately resolves to keep supporting her, then passes out again." |
| Same file, l.36 (KCMP-SERIES-011) | "an unnamed person injures Shigeyoshi Kawamura near a well. He considers seeking help and leaves. … His identity and the exchange…" | "an unnamed person stabs Shigeyoshi Kawamura near a well. The person considers seeking help and leaves. … The person's identity and the exchange…" (The source gives the agent no gender, PRO p[0004]–p[0036]. "Stabs" follows PRO p[0005]; this is optional.) |
| `readings/KSOA_V02_READING_INTRODUCTION.md` l.42 (KCMP-CHAR-013) | "She later files a complaint about Asumi, and the police separately take up the financial allegation." | "She agrees to file a criminal complaint about Ishikawa's embezzlement if the detectives keep their promise, and the station's fraud squad takes it up." |
| `readings/KSOA_V06_READING_INTRODUCTION.md` l.46 (KCMP-SERIES-004) | "He slept during the relevant interval…" | "He slept during the relevant interval, after drinking champagne into which, Asumi charges, Kume had put his prescribed sleep-inducer…" |
| `readings/KSOA_V05_READING_INTRODUCTION.md` l.46 (KCMP-SERIES-001) | "…meet Wakao near Koshigoe and press him about the hotel design." | "…meet Wakao near Koshigoe and threaten to expose the secret of the hotel design unless Wakao paid him." (The next sentence, "Her account of the demand and the route is a reconstruction", stays.) |

### (c) `KSOA_CASE_EVIDENCE_LEDGER.md`

| Target | Action | Proposed content |
|---|---|---|
| `## V06 case evidence`, new row `KSOA-V06-ACT-0005` (KCMP-SERIES-004) | New row | Enabling act: sleep-inducer in Yakushiji's champagne | H-0010 | C03 0711, 0717–0724; EPI 0005 | Asumi attributes the drugging to Kume. The treating doctor's testimony on Kume's prescription and Yakushiji's sleepiness from about eight support it; Kume denies a link in the scene, and the epilogue reports full confessions. It removes the host from the alibi without his knowledge. |
| `## V06 case evidence`, new row `KSOA-V06-EV-0011` (KCMP-SERIES-004) | New row | Shouting test and prescription evidence | H-0010 | C03 0684–0687, 0695, 0721 | Asumi demonstrates that Kosugi's upstairs room cannot hear the party room, and reports that investigators hold the doctor's statement on Kume's prescription. Together these undo the arrival-and-departure alibi. |
| `KSOA-V06-EV-0010` (KCMP-SERIES-004) | Correction note | "'Circumstantial support' = the prescription testimony and the shouting test; see EV-0011 and ACT-0005." |
| `KSOA-V01-RES-0003` (KCMP-SERIES-001) | Correction note | "Motive: Uehara threatened to expose the staff's embezzlement (C03 0897). Kazue reports Tomita's reason as fear of lifelong extortion (C03 0977)." |
| `KSOA-V05-RES-0002` (KCMP-SERIES-001) | Correction note | "Asumi's reconstruction: extortion of about ten million yen by threatening to expose the hotel-design secret (C03 0947, 0952). PRO 0022–0026 corroborates a 'demand' concerning Wakao's past; PRO 0045, the wooden sword was brought to threaten. Hani admits only the blow (C03 0954)." |
| Rows at l.162 and l.166 (KCMP-SERIES-010) | Correction note | "Kechika → Echika (森岡恵智花; C01 0150 ruby)." |

### (d) `KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md`: adjudication rows (frozen hypotheses untouched)

| New row | Content |
|---|---|
| `KSOA-V04-ADJ-0003` (KCMP-SERIES-010) | Name adjudication for `KSOA-V04-ADJ-0002`: the person written "Kechika" is 森岡恵智花, Morioka Echika (C01 p[0150]). |
| `KSOA-V06-ADJ-0003` (KCMP-SERIES-004) | Detectability: the drugging and the prescription are first disclosed at C03 p[0717]–p[0721]. The shouting test (p[0684]–p[0687]) is shown to the reader just before. Before the reveal, the reader had only the host's account of continuous presence and the arrival and departure corroboration. |
| `KSOA-V07-ADJ-0004` (KCMP-SERIES-003) | H-0015 context: intoxication (EPI p[0143]), the addressee (沙也香), and Motoya's blackouts before (p[0131]) and after (p[0149]) the exchange. Asumi's knowledge that he was awake is unknown. |
| `KSOA-V03-ADJ-0004` (KCMP-SERIES-007) | The prologue's suicidal ideation (PRO p[0034]–p[0035]) is a bounded competing reading for the 1992 death. Against it, the hidden text (C03 p[0339]) and the reported letter (p[0407]) support a push. |

### (e) `KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md`

| New or corrected row | Proposed content |
|---|---|
| `KSOA-V01-VOICE-0003` (KCMP-CHAR-001) | Asumi → Motoya: キミ as teasing-senior address (C01 0047, 0776; EPI 0004, 0015, 0050) and 元哉くん (C01 0584, 0811). Distribution of dialogue lines containing キミ, by volume: 11/10/5/1/0/0/2. |
| `KSOA-V01-VOICE-0004` (KCMP-CHAR-002) | Motoya → Asumi: おまえ in familiar quarrel (C01 0040, 0778), alongside the mock title デカチョウ (C01 0057). |
| `KSOA-V02-VOICE-0001` (KCMP-CHAR-004) | Asumi, formal: わたくし and わたくしども in an official apology call, with 猫なで声 (C01 0943–0949). Compare よそゆき声 at V01 C02 0472–0473. |
| `KSOA-V02-VOICE-0002` (KCMP-CHAR-001) | Asumi → Motoya: キミ (C01 0236 「あたしはキミの指導役なんだよ」; C03 0234) and 元哉くん (C01 0327). |
| `KSOA-V02-VOICE-0003` (KCMP-CHAR-004, -005) | Asumi's sugary self-introduction 「小笠原亜澄ですぅ」 with 甘ったるい声 (C03 0845–0846). The Motoya-focalized frame for it is the narratorial 「イケメンに弱い」 (V01 C01 0899; V03 C01 0280). |
| `KSOA-V05-VOICE-0001` (KCMP-CHAR-003) | Motoya: first 僕, with Sayaka and Emiri, alongside the narrated 「不自然にいい子を演じている」 (C01 0091, 0213). |
| `KSOA-V05-VOICE-0002` (KCMP-CHAR-002) | Motoya → Asumi: おまえ in real anger (C02 0788–0789), the only use after V03. All later おまえ in the series come from superiors. |
| `KSOA-V06-VOICE-0001` (KCMP-CHAR-001) | Asumi → Motoya: あんた as a sign of temper, glossed by Motoya (C01 0652). EPI 0013–0021: Sayaka's provocative 元哉くん, and Asumi's 「あんたに元哉くんなんて言う資格あるわけ？」. |
| `KSOA-V07-VOICE-0001` (KCMP-CHAR-001) | Asumi: キミ returns (C01 0012; EPI 0124); 相方の吉川くん to a civilian (C01 0316). |
| `KSOA-V07-VOICE-0002` (KCMP-CHAR-003) | Motoya: 「県警刑事部の吉川です。僕はエチオピアの豆です」 is one utterance to Nagasaka (C03 0493); 「残念ですが、僕は刑事です」 to Emiri (C04 0189). |
| `KSOA-V01-STATE-0009` (KCMP-CHAR-005) | Motoya-focalized narration attributes to Asumi a weakness for handsome men (C01 0899; V03 C01 0280). She denies it (V03 C02 0724). Class: narratorial view through Motoya. It never stops her investigating. |
| `KSOA-V04-CH-0006` (KCMP-CHAR-012) | Motoya's coffee discernment is narratorially generalized (C01 0734). Recurrence: the V07 bean café, whose style Asumi also likes (V07 C03 0481). |
| `KSOA-V05-CH-0005` (KCMP-CHAR-006) | Asumi promises Enomoto unconditional discretion (C03 0691–0694) and later grounds the public confrontation on the eighteen-year-old rumour (0842). Motoya privately finds her 意地が悪い and questions the need to expose everything (0926–0927). She apologizes (0973). Compare the V02 conditional pledge (V02 C03 0465). |
| `KSOA-V07-REL-0006` (successor qualification of `KSOA-V07-REL-0005`; KCMP-SERIES-003, KCMP-CHAR-007) | "Asumi's acknowledgement (EPI 0144) is said, drunk, to Sayaka (0135–0143), after Motoya has come to from a blackout (0131–0132). Motoya's resolve (0146–0148) is private and followed by a second blackout (0149). Professional reciprocity is supported; its durability and Asumi's awareness of the audience are untested." |
| Row at l.134 (KCMP-SERIES-010) | Correction note: Kechika → Echika. |
| Schema table and header (KCMP-CHAR-014) | Add the record kind `CH` (character conduct or state in a case context; fields as `STATE`). Add a note after l.22: "Initialization header preserved as terminal bytes (see producer review); rows for V01–V07 follow." |

### (f) `KSOA_CLAIM_REVISION_LEDGER.md`

| Revision | Transition | Proposed content |
|---|---|---|
| `KSOA-SER-CL-0004-R01` (KCMP-SERIES-003) | **DOWNGRADE** (High → Moderate–high) and REVISE | "The finale strengthens evidence of reciprocal professional reliance. Asumi's appreciation is spoken while drunk, to Sayaka, and overheard by Motoya after he comes to (V07 EPI 0131–0145). Motoya's pledge is private, made while drunk, and followed by another blackout (0146–0149). Future conduct and Asumi's awareness of the audience are open." |
| `KSOA-V07-CL-0006-R01` (KCMP-SERIES-003) | REVISE | "Asumi's acknowledgement is voiced drunk, to Sayaka, about Motoya ('こいつ'), marked 「まじめな顔で」. Motoya's commitment is internal. Two-way professional dependence is supported, with the V01-style discount for intoxication." |
| `KSOA-SER-CL-0001-R01` (KCMP-SERIES-004) | STRENGTHEN | Add V06 enabling conduct: Kume's drugging of the host removes a corroborator without his knowledge (`KSOA-V06-ACT-0005`). |
| `KSOA-SER-CL-0006` (new; KCMP-SERIES-001) | STRENGTHEN (new series claim from `KSOA-V04-CASE-0002`, `KSOA-V07-CASE-0003` and the V01/V05 notes) | "**Moderate–high.** Extortion is the immediate motive structure in four killings: the extortionist is killed in V01 and V04, and the extortionist kills a refuser in V05 and V07. Its evidential status varies: a report of the killer's words (V01), a confession (V04), the prologue's demand plus a reconstruction (V05), and a recording plus a reconstruction (V07)." |
| `KSOA-SER-CL-0007` (new; KCMP-SERIES-006, KCMP-CHAR-006) | STRENGTHEN | "**Moderate–high.** Asumi's method includes narrated bluffs (V01, V03, V04, V06; V06 'お得意'), justified by a stated ethic of any non-illegal means even against common decency (V02 C03 0378). Promised discretion is breached when the case requires it (V03; V05)." |
| `KSOA-V03-CL-0001-R02` (KCMP-SERIES-007) | PRESERVE (probable homicide), with REVISE of the limits | "Add the prologue's explicit suicidal ideation (PRO 0034–0035) as a bounded competing reading. The reported letter states a push (C03 0407); the fall is unseen." |
| Monograph scope note (KCMP-CHAR-010) | OPEN | Before editing either lead monograph, record whether the change is a selective update (the standard applies to changed content) or a general revision or successor (full §5.5.1 conformance). |

### (g) Studies (and the character-layer home)

| Target | Action | Proposed content |
|---|---|---|
| `studies/KSOA_ASUMI_OGASAWARA.md`, "Address, ordinary life and felt need" (l.43) (KCMP-CHAR-001, -004, -005) | Selective update (or successor) | Add: キミ as her habitual teasing-senior address to Motoya in V01–V03, absent in V05–V06 and returning in V07; 元哉くん as an occasional familiar form; あんた as Motoya's gauge of her temper, rising in V05–V06; わたくし and わたくしども with a 猫なで声 in formal apology calls; a sugary self-introduction that Motoya ties to her 'weakness for handsome men' (his narratorial view, which she denies). Make clear that written register is not performed voice. |
| Same, "The costs and uses of control" (l.37) (KCMP-SERIES-006, KCMP-CHAR-006, -013) | Selective update | Quote the credo's limit (legality) and its acceptance of acts 「人倫にもとる」. Add the habitual bluff, and the V05 promise of discretion followed by the public use of the rumour. Change "later separate complaint" to "the separate criminal complaint against Ishikawa". |
| Same, l.47 (KCMP-CHAR-007) | Selective update | "…her statement, made drunk to Sayaka and overheard by Motoya, `こいつがいるから`…" Add a one-line romance statement: what is evidenced, what is open. |
| `studies/KSOA_MOTOYA_KITSUKAWA.md`, "Registers, habits and the final resolve" (l.43–47) (KCMP-CHAR-002, -003, -012, -007) | Selective update | Add: おまえ to Asumi in V01, then one use in anger in V05; 僕 from V05 with the civilian women, with the narrated self-awareness 「不自然にいい子を演じている」. Replace the two-context sentence with "his self-introduction to Nagasaka combines 吉川です with 僕 in one utterance". Add the narratorially generalized coffee discernment. l.47: "after overhearing her drunken appreciation to Sayaka". |
| `studies/KSOA_PARTNERSHIP.md` l.25 and l.51 (KCMP-SERIES-003, KCMP-CHAR-009) | Targeted revision | l.25: "Asumi, drunk, tells Sayaka…; Motoya, just come to, overhears." l.51: replace "the explicit wording of their final exchange" with "the wording of Asumi's final remark about him". Add that Motoya's single narrated bodily response (V01 EPI p[0067]) is disowned, and that his appraisals of Asumi are formulaically qualified (V01 C01 p[0024]). |
| `studies/KSOA_INTEGRATED_SERIES_SYNTHESIS.md` l.40 (KCMP-SERIES-001) | Successor revision | Distinguish 羽仁's money-motivated extortion (Asumi's reconstruction) from the community's efforts at redress, and add a paragraph on extortion and silencing (`KSOA-SER-CL-0006`). |
| `studies/KSOA_MYSTERY_FORM_AND_CAUSALITY.md` l.43–49 and "Three kinds of closure" (KCMP-SERIES-004, -006, -008) | Revision | V06: name the drugging and the shouting test as the alibi's mechanism. Closure: bluff-induced admissions (V01, V03). Detectability: the focalization rule withholds Asumi's reasoning until the reveal. |
| `studies/KSOA_POLICING_PLACE_AND_NARRATION.md`, "Who speaks inside the prose" (l.51) and "The cost of making a truth public" (l.37–39) (KCMP-SERIES-005, -006, -008) | Revision | State the rule: outside the prologues, narration is Motoya's close third person, except the V02 opening through 高梨 (C01 p[0014]–p[0170]), and Asumi's interior is reached only through his inference. Add the credo and bluff device to the costs of disclosure. Optionally cite 佐竹's reputation remark (V04 C01 p[0893]) in "Who can act on a question". |
| Character-layer home: a qualification record (e.g. `audits/KSOA_MONOGRAPH_QUALIFICATION_RECORD.md`), named in `KSOA_SYNTHESIS_ARCHITECTURE.md` (item 2, l.73) and routed from `CURRENT_STATE_AND_CORPUS_MAP.md` (KCMP-CHAR-011; nearest type: g) | New governed artifact plus routing | One record per assessed character: identity, boundary, outcome, a rationale naming the largest gaps, a trigger and a monograph path. §2B.2 supplies source-checked seeds for nine `QUALIFIED_PENDING` characters and the deferred list. The GPT assessor must make and evidence its own judgments; no placeholder monographs (§5.5.1). |
| Motif and name-reuse aid (KCMP-SERIES-009) | New section in the integrated synthesis, or a non-sequential retrieval audit, plus a note in the entrypoint | Name-reuse warnings: 野中 (V03/V06), 茉莉子 (V03/V04), 若尾 (V03/V05), 相木 (V02/V04). Recurring phrases, e.g. 「悪魔が囁」 (V02 C03 p[1019]; V03 C03 p[0527]). |

### (h) CB1-only corrections (record here; the CB1 baseline stays frozen)

| CB1 item | Correction to record |
|---|---|
| `CB1-CL-038`, `CB1-U-18`, LS §3.2 V07 "Proof status" (KCMP-SERIES-002) | V07 C04 p0574 concerns the voice on the *extortion* call. p0575 defers the question to voiceprint analysis, and 江口's reactions (p0578, p0583, p0587–p0589) acknowledge the recording. Remove it as counterevidence to the homicide attribution. The remaining limits stand: no confession, an unnamed prologue agent, forensics not shown. |
| `CB1-CL-054`, LS §4.3 trajectory sentence (KCMP-SERIES-005) | Overgeneralized. V06 HQ indifference (V06 C02 p0718–p0719) follows the V04 wager, and 佐竹 appears only in V04. Restate as case-dependent reception with an end-state of adoption in V07. |
| CB1 MM §0 and §12 (KCMP-CHAR-008) | "Prompted" applies to the V04 Alto identification (V04 C03 p0406–p0410), not to the direction proposal, whose reasoning is his own (p0426–p0431). Reconcile §0's "bounded supporting moves" with PS §1 and §3.5. |
| `CB1_SHICHIJO_AKIKO_MONOGRAPH.md` §6 (l.93) (KCMP-CHAR-015) | 「一二年ぶりにお会いして」 (V04 C02 p0713) is part of the lie (C02 p0698; C03 p0716, p0733), not a true detail. |
| `CB1_SATOMI_YOSHIHISA_MONOGRAPH.md` l.180 (KCMP-CHAR-015) | Recast as Motoya's inference (V02 C03 p0932). |
| `CB1_GAMO_TAKASATO_MONOGRAPH.md` §1 (l.28) (KCMP-CHAR-015) | Withdraw "refutes… guards his bloodline". 秀之 renounces the succession himself (V01 C03 p1066), and 隆鄕 grounds his affection partly in blood (p1084). The other sub-agent items remain unverified checklist entries. |
| CB1 Ichiyō monograph (KCMP-CHAR-016) | Missing competing reading: the account as a projection that displaces 茉莉子's gifts and material choices (GPT V03 DEEP l.226). |
| CB1 V01 records (KCMP-SERIES-012) | Missing analysis: 遺書/告白/告解 as distinct audiences and obligations (GPT synthesis l.30; policing l.37). |

---

## 4. Counts

**By verdict on the register disposition (28 records):** CONFIRM 23 · MODIFY 5 (KCMP-SERIES-003, -006, -011; KCMP-CHAR-010, -014) · OVERTURN 0. The register was modified in 5 of 28 records (18%) and overturned in none.

**By final disposition (primary dimension):**

| Disposition | Count | Records |
|---|---:|---|
| GPT_OMISSION | 11 | SERIES-001, -003, -004, -009; CHAR-001, -002, -004, -005, -011, -012, -014 |
| GPT_COMPRESSION | 7 | SERIES-006, -007, -008; CHAR-003, -006, -009, -010 |
| GPT_ERROR | 4 | SERIES-010, -011; CHAR-007, -013 |
| CLAUDE_ERROR | 2 | SERIES-002; CHAR-015 |
| CLAUDE_OMISSION | 2 | SERIES-012; CHAR-016 |
| INTERPRETIVE_DISAGREEMENT | 2 | SERIES-005 and CHAR-008 (both resolved toward GPT) |

Secondary dimensions: GPT_COMPRESSION on SERIES-001 and -003; GPT_OMISSION on CHAR-007 and -010; minor CLAUDE_ERROR on CHAR-008; presentation on CHAR-014.

**By priority:** P1 4 (SERIES-010, SERIES-011 [low severity], CHAR-007, CHAR-013) · P2 11 (SERIES-001, -003, -004, -006; CHAR-001, -002, -003, -004, -006, -010, -011) · P3 7 (SERIES-007, -008, -009; CHAR-005, -009, -012, -014) · CB1-only 6 (SERIES-002, -005, -012; CHAR-008, -015, -016).

**Qualification verdicts (nine characters):** all nine are `QUALIFIED_PENDING`, two leads and seven bounded non-leads. None is `COMPLETE_AT_BOUNDARY` in either corpus. The four deferred characters stay `DEFERRED_EVIDENCE`.

**Blockers.** None. Two decisions are left to the integrator: whether lead-monograph changes are selective updates or a general revision (KCMP-CHAR-010), and where the qualification record lives, which needs an architecture amendment (KCMP-CHAR-011).
