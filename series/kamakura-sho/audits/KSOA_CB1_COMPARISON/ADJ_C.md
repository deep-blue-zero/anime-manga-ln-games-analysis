---
title: "KSOA-CB1 Phase 4 discrepancy adjudication — Group C (V06 佐助ヶ谷の銀雫, V07 長谷の花舞)"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CB1_ADJ_C
artifact_type: discrepancy_adjudication
generation: KSOA-CB1-COMPARISON
version: "1.0"
created: "2026-11-15"
status: canonical
scope: "Source-decided Phase 4 adjudication of the 26 KCMP-V06 and KCMP-V07 records, with integration actions grouped by destination type (a)-(h)."
source_boundary: "Seven Japanese publisher EPUB witnesses KSOA-JP-V01-W01 to KSOA-JP-V07-W01 (all narrative sections); GPT corpus KSOA-G1 at 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a; KSOA-CB1 blind package frozen 2026-11-15T10:52:54Z, manifest SHA-256 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040."
canonical_home: series/kamakura-sho/audits/KSOA_CB1_COMPARISON/ADJ_C.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
compared_generations: [KSOA-G1, KSOA-CB1]
gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
cb1_blind_package_manifest_sha256: 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040
source_record: "comparison/ADJ_C.md in the KSOA-CB1 comparison workspace (outside Git)"
source_record_sha256: 998cf568e85e70f243bafbde7f034e9cc0c636e276ca57429c0f1fc4e66ce720
source_record_bytes: 89078
source_record_body_sha256: d531e69d5e9ad2d0c773dd54aaa0f0ee08e23aa72a10fc553ccdc2d2a997332a
copy_transformations: []
path_rewrites: []
integration_date: "2026-11-15"
integrated_by: INT-6
source_record_front_matter: |
  title: "KSOA-CB1 Phase 4 discrepancy adjudication — Group C (V06 佐助ヶ谷の銀雫, V07 長谷の花舞)"
  artifact_type: discrepancy_adjudication
  status: draft_noncurrent
  do_not_use_as_current_authority: true
  gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
  cb1_basis: "BLIND_PACKAGE_MANIFEST 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040"
  author_model: "Claude Opus 5.5 (claude-opus-5-5), Phase 4 independent adjudicator (Context B), Group C"
  created: "2026-11-15"
  registers_adjudicated:
    - "comparison/KCMP_V06_REGISTER.md sha256 4e911b32394fa8f1579a985fa046fa426418a113b3cc57613301dc79f75a20e0 (14 records)"
    - "comparison/KCMP_V07_REGISTER.md sha256 92d28984d4e6a0d125f62c5edbbac45067d0dcc57839813d6817c84040e7d0b1 (12 records)"
---

# Phase 4 adjudication — Group C (V06, V07)

**Scope and method.** This report adjudicates all 26 records of `KCMP_V06_REGISTER.md` (KCMP-V06-001 to -014) and `KCMP_V07_REGISTER.md` (KCMP-V07-001 to -012) under `PHASE4_BRIEF.md` and the binding `COMPARISON_PROTOCOL.md`. Each record was decided against the Japanese witness in `KSOA-CB1:01_source\V06\` and `\V07\`, read in context, never from the register's quotation alone. The GPT side was read at the pinned commit (`git rev-parse HEAD` = `7d8ece76…`, working tree clean): the V06 and V07 deep readings and introductions in full, the V06 and V07 sections of all four ledgers, the claim-ledger series section, the V06/V07 parts of the source-completion audit, and every study passage cited below. The CB1 side was checked at each anchor the CLAUDE_ERROR records cite. GPT omission claims were re-run by grep over the whole `series\kamakura-sho\` tree. Neither corpus was modified. Working notes: `comparison\work\ADJ_C_notes.md`.

**Locator contract.** GPT `C03 0711` / `C03 p[0711]` and CB1 `[V06 C03 p0711]` resolve to line `p[0711]` of `V06_C03.txt`; confirmed on V06 PRO p0004–0039 (GPT H-0001 range), C03 p0618 and V07 C04 p0645.

**Independence note.** The adjudicator is a separate instance of the same model family that wrote CB1 and the Phase 3 registers. No decision below rests on either analysis's wording, confidence or length; each rests on the cited Japanese.

Quotations are short and verified against the extraction. Glosses are mine.

---

## 1. Adjudication table

| ID | Register disposition | Verdict | Final disposition | Priority | Rationale (locators) |
|---|---|---|---|---|---|
| KCMP-V06-001 | GPT_OMISSION | CONFIRM | GPT_OMISSION (evidence coverage; GPT keeps only the placeholder "circumstantial support") | P2 | Drug accusation and doctor's statement (C03 p0717–0724) absent corpus-wide; the champagne was planted twice before the reveal (C02 p0500; C03 p0284) |
| KCMP-V06-002 | GPT_COMPRESSION (+ GPT_OMISSION for the bluff) | CONFIRM | GPT_COMPRESSION + GPT_OMISSION (bluff) | P2 | Shout test p0684–0687, 中抜け p0691, distances p0695 and narrated bluff p0679–0681 reduced to "tests the house and accounts" (CH-0005) |
| KCMP-V06-003 | GPT_COMPRESSION, source-accuracy dimension | CONFIRM | GPT_COMPRESSION + source accuracy | P2 | PRO p0033 identifies the waiting person as the author of the couple's misfortune; H-0001 and intro §3 ¶1 say only "can explain the past" |
| KCMP-V06-004 | CLAUDE_ERROR | CONFIRM | CLAUDE_ERROR (evidence status) | CB1-only | C03 p0618 「その話」 is the stalker story only; Yakushiji never names who told him of the colourant switch (p0444; cf. p0503) |
| KCMP-V06-005 | GPT_OMISSION | MODIFY | GPT_COMPRESSION + GPT_OMISSION (address contest; 相方 demurral; intoxication) | P2 | REL-0004 keeps the bar scene but loses Asumi's 資格 challenge over 元哉くん (EPI p0015), her drunkenness (p0012), the rank jab (p0021) and Motoya's C01 p0110 demurral |
| KCMP-V06-006 | GPT_OMISSION (+ INTERPRETIVE_DISAGREEMENT) | MODIFY | GPT_OMISSION | P2 | C01 p0297 and C03 p0333–0334 uncited in GPT; but GPT's "apparent jealousy" plus Partnership l.51's explicit limit is not a contrary assertion, so no interpretive disagreement |
| KCMP-V06-007 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P2 | Yakushiji's school-first principle (C03 p0555), cover-up reason (p0705), the killers' 「先生と一門を守るために」 (p0711) and closing arc (p0733–0739) absent |
| KCMP-V06-008 | GPT_OMISSION | CONFIRM (qualified) | GPT_OMISSION (of a supplementary reading) | P3 | C03 p0421 is Motoya's hedged additive reading (〜からも…とも思えてきた), compatible with Asumi's p0649–0653 rather than rival to it |
| KCMP-V06-009 | GPT_ERROR | CONFIRM | GPT_ERROR (speaker attribution) | P1 | The timing observation is Motoya's (C02 p0525); the frozen reading credits Asumi |
| KCMP-V06-010 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | No V06 place, shrine, jurisdiction or exhibition is named anywhere in GPT (C01 p0030, p0149, p0300–0324, p0684, p0913–0914; C02 p0597; C03 p0312) |
| KCMP-V06-011 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | Rod-like weapon (C01 p0908; 棒 C03 p0711) unrecorded; house search (p0910), payphone (p0915), camera canvass (p0917) and contact means never closed or listed |
| KCMP-V06-012 | BOTH_INCOMPLETE | CONFIRM | BOTH_INCOMPLETE | P3 | C03 p0207: HQ had not researched Yakushiji's family; cited by neither corpus |
| KCMP-V06-013 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P3 | C02 p0363 with Motoya's 「ぼっち」 gloss (p0365); covert use of Emiri's information (C02 p0456–0459); residence 材木座 (C03 p0063) |
| KCMP-V06-014 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P3 | Clock times (C03 p0284, p0304, p0711) and the Saturday gathering (p0540) absent; the register's "Friday off-page work" is its own inference |
| KCMP-V07-001 | GPT_ERROR | CONFIRM | GPT_ERROR | P1 | Kawamura and Aonuma were 兄弟弟子 under one Ginza chef (C01 p0384; C03 p0331), Aonuma the senior (C04 p0465); intro §3 ¶2 says "former teacher" |
| KCMP-V07-002 | GPT_ERROR + GPT_COMPRESSION | CONFIRM | GPT_ERROR (introduction) + GPT_COMPRESSION | P1 | EPI p0131–0149: drunk truce, line said to Sayaka about Motoya in the third person, overheard after a blackout, second blackout; intro says "tells Motoya"; ledgers and SER-CL-0004 carry no intoxication bound |
| KCMP-V07-003 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | Knife (PRO p0005), autopsy weapon and survival interval (C03 p0743), car-navigation canvass (p0745–0746), weapon in the reconstruction (C04 p0601): none in GPT |
| KCMP-V07-004 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | Kawamura's reported complex toward his 兄弟子 (C04 p0465, doubly mediated and hedged) and wholesale adoption (p0460) absent; no Kawamura row |
| KCMP-V07-005 | CLAUDE_ERROR + INTERPRETIVE_DISAGREEMENT (sec. GPT_COMPRESSION) | CONFIRM | CLAUDE_ERROR + INTERPRETIVE_DISAGREEMENT; secondary GPT_COMPRESSION | CB1-only (GPT secondary P3) | C04 p0574 concerns the extortion tape and is resolved by p0578–0589; the homicide search has its own warrant (p0627); collapse p0630; 犯人逮捕 p0652 |
| KCMP-V07-006 | GPT_OMISSION (interpretive dimension) | CONFIRM | GPT_OMISSION (clue placement) | P2 | C03 p0100, p0209 (pays off at C04 p0623), p0417–0420, p0586: available, low-salience pointers unrecorded |
| KCMP-V07-007 | GPT_COMPRESSION | MODIFY | GPT_COMPRESSION + GPT_ERROR (introduction) | P1 (low consequence) | Inquiry calendar, 08:17 arrest, October wedding, lunar frame absent; intro's "evening interval" contradicts 01:00–03:00 on 1 August (C01 p0172; C03 p0742) |
| KCMP-V07-008 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | No V07 VOICE rows: キミ (C01 p0012; EPI p0124), no あんた to Motoya, Eguchi 僕→俺 (C04 p0539→p0589), 噓ですね (p0418) |
| KCMP-V07-009 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P2 | Custody chain (C04 p0576), demand (p0572), Shiobara's fee, mother's illness and death (p0445, p0449, p0478) |
| KCMP-V07-010 | GPT_OMISSION | MODIFY | GPT_COMPRESSION + GPT_OMISSION | P3 | Private credit and irritation at her protective tone are in CH-0003, REL-0005 and Partnership l.37; aesthetic appraisals (EPI p0019; C04 p0304) and sneers (EPI p0098, p0103) are not |
| KCMP-V07-011 | GPT_OMISSION + GPT_ERROR | MODIFY | GPT_OMISSION (structural; presentation dimension) | P3 | PRO is pronoun-free (self-reference only 自分のしわざ, p0030); the intro's "He" is a spoilered synopsis choice that obscures the device, not a story-fact error |
| KCMP-V07-012 | GPT_ERROR | MODIFY | GPT_OMISSION (misleading-framing dimension) | P2 | C02 p0403 (home alone in 常盤) against EPI p0116 (Emiri's 七里ヶ浜 flat) is recorded nowhere in GPT; no GPT sentence is false, but Mystery l.49 frames the matter as nondisclosure |

---

## 2. Full adjudication entries

Entries follow the brief's steps: (1) passage; (2) speaker, focalizer, chronology, disclosure; (3) established versus inferred; (4) strongest competing explanation; (5) verdict and final disposition; (6) residual uncertainty; (7) implications; (8) priority; (9) integration (cross-referenced to §3).

### KCMP-V06-001 — The host's drugged sleep and the doctor's statement

1. **Passage.** C03 p0711 (Yakushiji): 「八時頃から眠くて眠くて仕方なくなった」. p0713 (Kume): 「ずっと飲んでたじゃないですか」. p0717 (Asumi): 「薬師寺先生のシャンパンに睡眠導入剤を混入させましたね」. p0721: Kume's regular clinic is the 常盤総合病院 心療内科, and 「すでに担当医の証言は捜査員がもらってますよ」, on a prescription for a sleep-inducer. p0722 (Kume): 「それは薬師寺先生とは関係ない」. p0724 (Kasuya): 「状況証拠だ。物的証拠などなにもない」. Pre-reveal: C02 p0500 (Kume) 「わたしと糟屋さんがケーキやシャンパンを持参して」; C03 p0284 (Kosugi) 「二人はとってもいいシャンパーニュを買ってきてくれたのよ」.
2. **Speaker and disclosure.** Direct speech in a Motoya-focalized scene. The prescription and doctor's statement are an off-page investigative finding first disclosed at the confrontation (Saturday, C03 p0540). The champagne itself was available to the reader at H-0006 and H-0009, with no emphasis.
3. **Established versus inferred.** Established: Yakushiji's report of sudden sleepiness from about eight; Asumi's accusation; her report that investigators hold the doctor's statement about Kume's prescription; Kume's deflection; the champagne as the pupils' gift. Inferred: that Kume actually drugged the champagne. Kume does not admit it on the page; the epilogue's 「すべてを自供」 (EPI p0005) covers it only by implication.
4. **Competing explanation.** Yakushiji simply fell asleep from drink, and Asumi's accusation is pressure. Against it: Asumi's reported doctor's statement, and the narrative's acceptance at EPI p0005.
5. **Verdict.** CONFIRM. Final: `GPT_OMISSION`. GPT's EV-0010 and H-0010 ("cites circumstantial support") gesture at the evidence without stating it, so the omission has a compression dimension. A corpus-wide grep (sleep, drug, champagne, prescri, doctor, 睡眠) finds no V06 hit beyond "slept".
6. **Residual uncertainty.** Whether the drugging happened is reported accusation plus reported confession in summary. The register's own caution stands: the doctor's statement establishes only the prescription. CB1-CL-031's "a doctor's statement backs the drugging" slightly overstates for the same reason (§3 H-03).
7. **Implications.** GPT EV-0010, ACT-0002, H-0010, D-0005, RES-0003; the V06 reading's "Once he says he slept…" paragraph; Mystery study V06 detectability row (the reader cannot explain how the alibi failed); CL-0003-R01 (the host's withdrawal now has a mechanism). Premeditation bears on the 殺人 framing. CB1: EXIT rows 26 and 28, CB1-CL-031.
8. **Priority.** P2.
9. **Integration.** A-03, B-03, C-01, C-03, D-02, G-01.

### KCMP-V06-002 — Alibi-break mechanics and the narrated bluff

1. **Passage.** C03 p0679 (Asumi asks what Nonaka communicated to the two pupils); p0681 (narration): 「これは亜澄お得意のハッタリだろう」, with Motoya's reason that no such contact had been reported but that without it the crime would have been hard to carry out. p0684–0687: she shouts for Kosugi, gets no answer, and says 「二階の小杉さんの部屋には聞こえません」. p0691 「中抜けトリックもどき」. p0695: arrival and departure were certified by Kosugi and the taxi firm; after about an hour's service Kosugi withdrew; 「この家と現場は七〇〇メートルも離れていません」, a round trip under thirty minutes, five minutes for the act.
2. **Speaker and focalization.** Asumi's speech; the bluff label is Motoya's hedged inference (だろう). Disclosure H-0010.
3. **Established versus inferred.** The shout test, the argument and the distances are on the page. That the question was a bluff is Motoya's inference. The endpoint structure is also established earlier (C03 p0284, p0304).
4. **Competing explanation.** GPT's abstractions ("tests the house and accounts"; "turns the observation gap into a challenge") are accurate summaries; detail is a retrieval matter. But "tests the house" cannot be expanded back into the shout test or the distances, and no GPT file records the bluff.
5. **Verdict.** CONFIRM. Final: `GPT_COMPRESSION` + `GPT_OMISSION` (bluff). Grep for bluff, ハッタリ, 中抜け, 700, shout returns no V06 hit.
6. **Residual uncertainty.** Whether the question was a bluff rests on Motoya's だろう.
7. **Implications.** GPT CH-0005, EV-0010, CL-0003-R01; Policing study (the "geography as alibi-breaker" claim); Asumi study (any series claim about her bluffs, which GPT records only for V01, V03, V04). CB1 already holds the content (READING §E11, §H1; CB1-CL-077).
8. **Priority.** P2.
9. **Integration.** A-04, B-03, C-02, E-01 (CH-0005 element), G-06.

### KCMP-V06-003 — What the prologue says about the waiting figure

1. **Passage.** PRO p0030 「あいつはあずまやで待っているはずだ。」; p0033 「わたしたちを不幸に陥れた者の姿が見える。」; p0034–0035 「あの影は真実を語るはずだ。」「いや、真実を語らせなければならない。」. Framing doubt: p0004 「本当にわたしが考えていることが真実なのだろうか。」, p0005 「そうだとすれば、許すことはできない。」.
2. **Speaker and disclosure.** First-person unnamed speaker (later Nonaka). Reader-only at H-0001. The identification is the speaker's belief, conditioned by the opening doubt.
3. **Established versus inferred.** Established: the speaker sees the person he regards as having made them unhappy, uses the pejorative あいつ, and means to force the truth. Not established: that the belief is correct (the solution later supports it, C03 p0711).
4. **Competing explanation.** "Can explain the past" is compatible with p0034 alone and keeps the doubt of p0004. It drops p0030 and p0033, where the speaker casts the waiting person as the wrongdoer, not as an informant.
5. **Verdict.** CONFIRM. Final: `GPT_COMPRESSION` with a source-accuracy dimension. H-0001, intro §3 ¶1 and K-0001 ("a speaker suspecting an arranged wrong") all lose the identification.
6. **Residual uncertainty.** Low on the text. The opening doubt keeps the identification provisional.
7. **Implications.** Detectability: once Kasuya's account introduces the 2012 sabotage (H-0007) and Mizutani denies it (H-0009), a reader can infer that the shelter meeting was with the person Nonaka held responsible for the frame. This sharpens suspicion of the accuser, Kasuya. Affects GPT H-0001 (frozen), K-0001, intro §3 ¶1, CL-0001/-R01, Mystery V06 row. CB1 records the line (O-0008) but does not use it in its §F4 table either.
8. **Priority.** P2.
9. **Integration.** A-01, B-01, D-01, G-01.

### KCMP-V06-004 — CB1 extends Yakushiji's admission to the colourant switch

1. **Passage.** C03 p0616 (Asumi): 「水谷さんのストーカー行為など初めから存在しないのです。誰から聞いた話なんですか」. p0618 (Yakushiji): 「その話は糟屋と久米の二人から聞いている」. Earlier, C03 p0444: he expelled Mizutani on learning 「その卑しい事実」 of the switch, source unstated. C02 p0648 (Kasuya): 「わたしはそのことを、野中くんにも先生にもほかの誰にも言っていない」 (the preparation-room sighting). C03 p0503 (Mizutani relaying Nonaka): a single 「そいつ」 told the master both the switch lie and the stalker lie. p0633 (Kume): Kasuya did the switch, planned by both. p0646–0648: both men are silent when charged with staging the stalker story.
2. **Speaker and disclosure.** Direct speech at the confrontation (H-0010). 「その話」 refers back to the stalker story in p0616.
3. **Established versus inferred.** Established: both pupils were Yakushiji's source for the stalker story. Inferred: that they, or one of them, also told him Mizutani switched the colourant. The inference is strong (p0503's single informant, p0618, p0633, Asumi's summary at p0624) but it is not Yakushiji's admission. Kasuya's sighting is shown false by Kume's accusation (p0633), not by Yakushiji, and whether Kasuya told the master of the sighting is never stated.
4. **Competing explanation.** p0618 could be read loosely as "the slander", covering both lies. Against it: p0616 asks specifically about the stalking, and the switch accusation was never put to Yakushiji as a sourcing question.
5. **Verdict.** CONFIRM. Final: `CLAUDE_ERROR` (evidence status; inference presented as admission). GPT ACT-0001 ("less directly admitted") and the reading's first section are accurate.
6. **Residual uncertainty.** Who told the master about the switch, and when.
7. **Implications.** CB1 `CB1_V06_EXIT_STATE.md` row 9 and CB1-V06-K-02; `CB1_YAKUSHIJI_KUNIAKI_MONOGRAPH.md` §4 row "2012" (l.65) and l.194 ("On their word he expelled 水谷 [p0618]"; p0444 gives the switch as the ground); `CB1_V06_CHARACTER_EVIDENCE.md` Part 2 (l.260, "told no one — contradicted by 薬師寺"); `CB1_V06_READING.md` §E7 (l.78) and the §F4 row "糟屋's story may be deflection". No GPT change; preserve ACT-0001 and CL-0002-R01 wording. Any transfer of CB1 Yakushiji material into a canonical portrait must carry the correction.
8. **Priority.** CB1-only.
9. **Integration.** H-01.

### KCMP-V06-005 — The epilogue address contest and the partnership-label sequence

1. **Passage.** EPI p0008 (Sayaka) 「あらぁ、デートぉ？」; p0011 (Asumi) 「あら、性悪の沙也香ちゃん。そうよぉ、うらやましい？」; p0012 「すでにけっこう飲んでいる亜澄」; p0013 (Sayaka) 「今度はわたしが元哉くん誘っちゃおうかなぁ」; p0015 (Asumi) 「あんたに元哉くんなんて言う資格あるわけ？」; p0017 (Sayaka) 「どんな資格があって元哉くんとプライベートまで一緒にいるのよ。ただの仕事の相方に過ぎないでしょ」; p0019 「あたしたちはバディだもの」; p0021 (Sayaka) 「相手が階級が上だと嫌でもお酒につきあわなきゃならないの？」; p0025 (narration) 「別に元哉は「喜んで」ここへ来ているわけではない。」; p0026 and p0031 奸譎. Earlier: C01 p0103 (Masaki) 「吉川の相方だな……幼なじみの」; p0110 (Motoya) 「別に相方というわけでは……」; p0932 宿命的なもの.
2. **Speaker and focalization.** Direct speech; Motoya's interior at p0025 and p0035. Sayaka addresses him as 吉川さん everywhere else in V06 (C01 p0286; C03 p0014, p0018, p0236, p0238); her switch to 元哉くん at p0013 is the provocation that triggers Asumi's 資格 challenge. Asumi uses 元哉くん herself only in earlier volumes (latest V05 C01 p0313).
3. **Established versus inferred.** Established: Sayaka proposes "date" and Asumi accepts it; Asumi, already drunk, disputes Sayaka's right to the given-name address; Sayaka counter-challenges Asumi's entitlement and calls her a mere work partner; the rank jab; バディ; Motoya's denial and escape. Inferred: what the contest says about Asumi's feelings.
4. **Competing explanation.** It is drunken, adversarial banter, and the address term is a weapon in the women's feud rather than evidence of Asumi's attachment. That reading bounds, but does not erase, the fact that Asumi treats familiarity with Motoya as hers to police.
5. **Verdict.** MODIFY. GPT does record the scene, the バディ claim, an entitlement challenge (Sayaka's side) and Motoya's interior qualification (REL-0004, H-0011, CL-0005), so this is compression, not absence. What is absent from the whole corpus is the address contest (元哉くん, 資格), the rank jab (which supports the GPT Asumi study's own "draws on seniority", l.47), Asumi's intoxication and the C01 相方 demurral. Final: `GPT_COMPRESSION` + `GPT_OMISSION`. Also: H-0011 and intro §3 ¶7 say Asumi "calls" the outing a date; she accepts Sayaka's word (p0008, p0011).
6. **Residual uncertainty.** Weight to give drunken speech.
7. **Implications.** GPT REL-0004, CL-0005, SER-CL-0004 (which cites "V06's claim of partnership"), Partnership V06 row and l.43, Asumi study l.47, intro §3 ¶7. The intoxication bound parallels KCMP-V07-002 and GPT's own V01 practice (STATE-0005, REL-0003, CL-0005-R01).
8. **Priority.** P2.
9. **Integration.** B-04, E-02, E-03, F-03, G-06, G-07.

### KCMP-V06-006 — Evidence on the motive of Asumi's hostility to Sayaka and Emiri

1. **Passage.** C01 p0297, narratorial recap: 「そのときから、亜澄は元哉と沙也香の仲を疑い、彼女に出会うと攻撃的な態度をとる」. C03 p0315–0339: Asumi's tirade (「いい大人なのに付添が必要なわけ？」 p0324; 「性悪よ。結局、あんたが甘いから」 p0329); p0333 「人間には好き嫌いがあるんだよ」; p0334 「亜澄は開き直った。まさにこれがはっきりした理由だろう。」; p0335 「二人の相性は最悪のようだ」.
2. **Focalization.** Both narratorial statements come through Motoya. p0297 is recap narration stated as fact; p0334 is hedged (だろう). Asumi's interior is never directly narrated.
3. **Established versus inferred.** Established: the narration attributes to Asumi a suspicion about Motoya's relation with Sayaka; Asumi gives personal dislike as her reason; Motoya's narration accepts that as the clear reason. Inferred: jealousy as motive.
4. **Competing explanation.** Jealousy (supported by p0297), dislike (p0333–0334) and investigative suspicion of Emiri, who did lie (C03 p0120–0157), coexist. None is decided.
5. **Verdict.** MODIFY. The omission stands: no GPT file cites p0297 or p0315–0339, and no GPT row records the dislike explanation. The secondary `INTERPRETIVE_DISAGREEMENT` does not: GPT writes "Asumi's apparent jealousy" (Partnership l.47) and at l.51 says a romantic interpretation "has limited authority over her unspoken feelings". That is compatible with CB1's open question. Final: `GPT_OMISSION`.
6. **Residual uncertainty.** The motive is unnarrated and plural.
7. **Implications.** GPT REL-0001, REL-0003, Partnership l.47 and l.51, Asumi study §The costs and uses of control; any series claim about "jealousy scenes". CB1 READING §N.4, CB1-CL-089, CB1-U-02 already keep it open.
8. **Priority.** P2.
9. **Integration.** E-04, F-04, G-06, G-07.

### KCMP-V06-007 — Yakushiji's principle, the killers' stated motive and his closing arc

1. **Passage.** C03 p0426 (no personal feeling, but a loss to the craft); p0452 「捜査にも協力するつもりはない」; p0551 (did not expel Nonaka, to spare his daughter and the artist's name); p0555 (shielded Mizutani for the school and for 「水谷勝也というガラス工芸家」, not the person); p0705 「わたしは糟屋と久米を守りたかっただけなんだ」; p0706 (strikes his forehead on the table); p0711 (Kasuya, as relayed) 「先生と一門を守るために野中を殺しました」; p0733 「わたしも共犯だね」; p0737 「佐助ヶ谷工房を終わらせるときを迎えた方がよさそうだ」; p0739 「愛は盲目と言うが」.
2. **Speaker and disclosure.** Direct speech (Yakushiji); p0711 is Kasuya's words in Yakushiji's report. H-0009 to H-0010.
3. **Established versus inferred.** Established: the stated principles, the stated cover-up reason, the relayed motive formula, the self-reproach and the hedged inclination (〜方がよさそうだ) to end the workshop. Inferred: that the killers' formula echoes, and exploits, the master's own value, which plausibly explains his concealment.
4. **Competing explanation.** GPT's role-gap audit treats case-local figures architecturally (no dedicated monograph), and its reading gives the core distinction (pride in Nonaka's talent versus anger as a father). Against sufficiency: the motive formula is case evidence, and p0705 is the stated basis of ACT-0004's concealment.
5. **Verdict.** CONFIRM. Final: `GPT_COMPRESSION`. The Integrated synthesis (l.46) has the theme of mistaking artistic preservation for a claim on a life, but not this evidence.
6. **Residual uncertainty.** Whether p0737 states a decision; it does not. CB1's own monograph erratum 3 reads it correctly as an inclination.
7. **Implications.** GPT ACT-0002, ACT-0003, ACT-0004, Integrated synthesis l.42; a Yakushiji portrait if the CHAR qualification decision admits him. CB1 Yakushiji monograph is the ready source after the H-01 correction.
8. **Priority.** P2.
9. **Integration.** C-03, C-04, E-05, F-05, G-08.

### KCMP-V06-009 — The departure-timing inference is Motoya's

1. **Passage.** C02 p0518 (Motoya): one pupil left, one was expelled; why is the school unsettled? p0523 (Asumi): 「その薬師寺って大先生に問題があるんじゃないかな」. p0525 (Motoya): 「だけど、ほぼ同じ時期に二人は一門から出ている」, so strictness cannot explain it. p0527 (Asumi) takes up the point. p0531 (Asumi): 「事件の鍵は、そのあたりにあるような気がしてるんだよ」.
2. **Speakers.** Unambiguous direct speech after Kume's interview (H-0006 territory). A whole-volume grep finds no other statement of the coincidence.
3. **Established.** The timing point is Motoya's; Asumi supplies the master hypothesis and the intuition.
4. **Competing explanation.** "Notes" might mean she registers or agrees with the point. In context the sentence lists Asumi's investigative contributions, so a reader takes it as her observation.
5. **Verdict.** CONFIRM. Final: `GPT_ERROR` (speaker attribution) in the frozen reading, §Craft knowledge and police disclosure ¶3.
6. **Residual uncertainty.** None on attribution.
7. **Implications.** Weakens the evidence for Motoya's independent contributions that the GPT Motoya study (§A focalizer with a job of his own) argues for; H-0006 itself is neutral.
8. **Priority.** P1 (attributional error in canonical material; consequence low to moderate).
9. **Integration.** A-02, G-05.

### KCMP-V06-010 — Setting and exhibition never named in GPT

1. **Passage.** C01 p0030 (the north end of 源氏山公園); p0149 「源氏山公園はね、七方向から登ってこられるんだ」, with the arbour 50–60 m from 梶原五丁目; p0304 「あの神社の境内には、『縁結び石』があるんですよ」 (葛原岡神社, the reason Sayaka and Emiri are there); p0684 「梶原は鎌倉署の管轄だけど、山ノ内は大船署の管轄なんだ」; p0913–0914 the 全美展; C02 p0597 (Kasuya) 「おそらくは銭洗弁天の崖から流れ落ちる清水」 as the title work's subject; C03 p0312 薬師寺邸 east of 銭洗弁天; C03 p0711 「梶原側のあずまや」.
2. **Speaker.** Mostly Asumi and expository narration; the title referent is Kasuya's surmise (おそらく).
3. **Established.** All names are on the page.
4. **Competing explanation.** GPT keeps the abstract mechanism (plan-view distance against walking route) and the title as a succession claim. That does not let a user locate the scene, link the title to the spring, or see why the civilians are at the cordon.
5. **Verdict.** CONFIRM. Final: `GPT_OMISSION`. Grep for 源氏山, Genji, 銭洗, 葛原, 縁結び, 全美展, Yamanouchi returns nothing; "Kajiwara" appears once without naming the park.
6. **Residual uncertainty.** The spring as the title referent is Kasuya's hedged reading.
7. **Implications.** GPT CASE-0001 (no location field), Policing study §Places, intro §3 ¶2, Integrated synthesis l.42 (title as succession claim).
8. **Priority.** P2.
9. **Integration.** A-05, B-02, C-05, G-04.

### KCMP-V06-011 — Weapon and open threads

1. **Passage.** C01 p0908 (briefing) 「背後から棒状のもので二度殴られた」; p0910 「明日、被害者宅を捜索する予定だ」 (also the wallet thread); p0915 「市内公衆電話からの通話」; p0917 dashcam and camera canvass of the seven approaches; C03 p0711 「棒で背後から殴って」, and 「野中から糟屋に連絡があったらしい」 with the means unstated; p0726 Asumi lists evidence still to be collected.
2. **Speaker and disclosure.** Nikaidō at the first briefing (H-0004); Yakushiji's relay (H-0010).
3. **Established.** Rod-like weapon by the examiner; the planned search; unidentified payphone calls; none is followed up on the page.
4. **Competing explanation.** These are authorial loose ends, not clues. Even so, the case ledger's CASE schema requires "source-supported remaining ambiguities", and the weapon is a basic case fact.
5. **Verdict.** CONFIRM. Final: `GPT_OMISSION`. GPT H-0002's "There is no confirmed weapon" is accurate at its horizon; nothing later records the rod.
6. **Residual uncertainty.** None on the text; whether the payphone calls were Kasuya's or Nonaka's arrangements is never stated.
7. **Implications.** GPT CASE-0001, H-0004 (payphone left live), RES-0003, audit V06 residual column.
8. **Priority.** P2 (weapon); the loose ends alone would be P3.
9. **Integration.** A-06, C-05.

### KCMP-V07-001 — Kawamura and Aonuma were fellow apprentices

1. **Passage.** C01 p0384 (Tomonaga): 「兄弟弟子だったと聞いている」, both 「同じ料理人の弟子だったそうだ」 at a Ginza ryōtei. C03 p0331 (Hashio): 「河村さんとは兄弟弟子だったそうだが」. C04 p0465 (Shiobara): 「板長は兄弟子である青沼さんにコンプレックスを持っていたようです」. Aonuma is 師匠/板長 only to Izumida, Eguchi and Nagasaka (C02 p0255; C03 p0191, p0533). EPI p0032 calls Eguchi Izumida's 弟弟子.
2. **Speakers.** Three independent witnesses agree.
3. **Established.** Fellow apprentices under the same chef, Aonuma the senior.
4. **Competing explanation.** None in the text. The slip probably transfers the pupils' relation to Aonuma.
5. **Verdict.** CONFIRM. Final: `GPT_ERROR` (introduction §3 ¶2, "run by Kawamura's former teacher Aonuma"). The deep reading's "a former apprenticeship tie between the chefs" (H-0003) is ambiguous but not wrong.
6. **Residual uncertainty.** None.
7. **Implications.** The error inverts the rivalry that motivates the espionage (KCMP-V07-004): a junior who was bullied by his senior and wanted to overtake him, not a pupil against his teacher.
8. **Priority.** P1.
9. **Integration.** B-06, E-08.

### KCMP-V07-002 — The finale acknowledgment: addressee, intoxication and overhearing

1. **Passage.** EPI p0124 (Asumi) 「えっ、キミはいつ英美里さんと会ったのよ？」; p0128 「なんであたしに言わないのよ」; p0130 「面倒なので元哉は返事をしなかった」. p0131 「そのうちに元哉の意識はなくなっていた」; p0132 he comes to after eleven; p0133–0134 Izumida asleep, Emiri slumped; p0136 Sayaka slurring; p0143 「酔った二人は楽しそうに握手している」; p0144 (Asumi) 「吉川くん、いいとこいっぱいあるんだよ。あたし、こいつがいるから捜査やれるんだ」; p0145 「まじめな顔で亜澄は言った」; p0146–0148 the words sink in, 「こいつは本当に優秀な刑事だ」, and he vows support; p0149 「元哉の意識はふたたび飛んでいた」.
2. **Speaker, focalizer, disclosure.** Asumi speaks to Sayaka, continuing their truce, and refers to Motoya in the third person (吉川くん, こいつ). Motoya, focalizer, has just regained consciousness. Whether Asumi knew he was awake is unstated. Both speakers and the focalizer are drunk.
3. **Established versus inferred.** Established: content, serious face, addressee, the overhearing, the private vow and both blackouts. Inferred: sincerity, and any projection to later conduct.
4. **Competing explanation.** The serious face and the professional content support sincerity, and the core GPT claim (two directed professional commitments, one spoken and one private) survives. The text never marks the line as said for Motoya's ears.
5. **Verdict.** CONFIRM. Final: `GPT_ERROR` (intro §3 ¶7, "Asumi tells Motoya") + `GPT_COMPRESSION` (no GPT file mentions the intoxication, the blackouts or the overhearing; grep for drunk, intoxicat, unconscious, passed out has no V07 hit; the deep reading mentions only "sleeping customers"). GPT bounds the V01 epilogue for intoxication (STATE-0005, REL-0003, CL-0005-R01) but not this one. REL-0004 also compresses Asumi's キミ challenge and Motoya's silence into "Asumi learns of the private meeting".
6. **Residual uncertainty.** Asumi's awareness of her audience; how much drink discounts the statement.
7. **Implications.** GPT REL-0004, REL-0005, CL-0006, ADJ-0003, SER-CL-0004 ("High"), Partnership l.25 and V07 row, Motoya study l.47 ("after hearing her explicit appreciation"), Asumi study l.47, deep reading l.156 ("their clearest reciprocal acknowledgement"), the audit's longitudinal bullet. CB1 is already correct (CB1-CL-043, erratum N-1).
8. **Priority.** P1 (intro addressee error; series claim graded High without the bound GPT applies elsewhere).
9. **Integration.** A-07, B-07, D-06, E-10, F-06, F-07, G-05, G-06, G-07.

### KCMP-V07-003 — The weapon

1. **Passage.** PRO p0005 「右手にした包丁」. C03 p0742–0743: time 01:00–03:00 on 1 August; 「凶器は鋭利な刃物で、たとえば刺身包丁のようなもの」; traumatic shock; death within some tens of minutes. p0745–0746: car-navigation recordings collected from cars parked nearby, nothing found yet. C04 p0601 (Asumi): 「脅すつもりだったのか」 he brought a blade; 「司法解剖の結果、凶器は刺身包丁のような刃物と判明しました」.
2. **Disclosure.** Knife and right hand are reader-only at H-0001; the autopsy is team knowledge at H-0010; Asumi uses it at H-0014.
3. **Established.** Weapon type and survival interval by autopsy. Not established: the weapon itself, never recovered.
4. **Competing explanation.** The weapon type does not discriminate among the cook suspects, so GPT could treat it as non-diagnostic. But the prologue, the autopsy and the reconstruction all rely on it.
5. **Verdict.** CONFIRM. Final: `GPT_OMISSION`. The only GPT mention is H-0009's "No site, weapon or direct proof…".
6. **Residual uncertainty.** None on the text.
7. **Implications.** GPT EV-0001, EV-0008, ACT-0003, K-0001, H-0010.
8. **Priority.** P2.
9. **Integration.** A-08, C-08, C-09, D-04.

### KCMP-V07-004 — Kawamura's motive for the espionage

1. **Passage.** C04 p0462 (Asumi asks why); p0465 (Shiobara): 「板長は兄弟子である青沼さんにコンプレックスを持っていたようです」, could never match him, 「若い頃はずいぶんいじめられた」, perhaps hated him (あるいは), and was driven to catch up and overtake. p0460: Kawamura adopted the soda-water beef and 「片っ端から」 other techniques. p0439: instructions on ingredients, suppliers, processing, service. Contrast C01 p0152 (Mihara): conscientious, shrewd in business, gentle with staff.
2. **Speaker and status.** Shiobara reporting what Kawamura said, relayed to the police: doubly mediated and hedged (ようです; あるいは). Asumi glosses the overtaking in sales terms (p0467).
3. **Established versus inferred.** Established: Shiobara's report and Mihara's appraisal. Inferred: Kawamura's actual feelings.
4. **Competing explanation.** Commercial rivalry alone (Asumi's p0467 gloss). Compatible with the reported complex rather than rival to it.
5. **Verdict.** CONFIRM. Final: `GPT_OMISSION`. ACT-0001 and H-0013 give no reason; grep for complex, bully, 兄弟子 finds no V07 hit; the V07 character ledger has no Kawamura row.
6. **Residual uncertainty.** The double mediation.
7. **Implications.** GPT ACT-0001, CL-0001-R01 (targeted borrowing), Integrated synthesis l.44; corrects the "teacher" frame (KCMP-V07-001).
8. **Priority.** P2.
9. **Integration.** C-11, E-08.

### KCMP-V07-005 — Strength of the homicide attribution; CB1's use of C04 p0574

1. **Passage.** C04 p0570–0572 (the recording plays: a demand of a million yen by Monday). p0574 「ドスの利いた声は江口のものとは思えなかった」; p0575 「だが、声紋鑑定に出せば、すぐにわかる話だ」. p0578 「くそっ、あの女め」; p0583 「まさかこんな録音が残っているなんて」; p0587–0589 asked whether it is his voice, he answers 「俺は正義のためにやったんだ」. p0598–0602 Asumi's reconstruction; p0603 「作り話だ」; p0605–0607 Motoya: 「亜澄の言うことは間違いない」 on the evidence to come; p0608 「だ、だけど……」. p0615 extortion arrest; p0618–0620 he blanches and trembles; p0627 「恐喝容疑とは別に」, a second document for a homicide search; p0630 「終わりだ……すべては終わりだ」 immediately after that announcement; p0635; p0645; p0652 「犯人逮捕で捜査本部は解散する」.
2. **Focalization.** p0574–0575 is Motoya's perception about whose voice is on the extortion tape, resolved within the scene by Eguchi's own reaction. p0652 is Motoya's narration treating Eguchi as the culprit.
3. **Established versus inferred.** Established: the extortion (recording plus admission-by-justification); a judicially issued search warrant on suspicion of the killing; the narration's closure; no homicide confession, weapon or trace result on the page. Inferred: that Eguchi killed Kawamura.
4. **Competing explanation.** Eguchi extorted but did not kill. 「終わりだ」 could express ruin from the extortion charge alone (CB1 H-36 at F-11), and p0603 is an explicit denial. Against it: the sequencing (the collapse follows the homicide-search announcement, after he had only blanched at the extortion arrest), the warrant, the narration and the absence of any live alternative.
5. **Verdict.** CONFIRM. Final: `CLAUDE_ERROR` + `INTERPRETIVE_DISAGREEMENT`; secondary `GPT_COMPRESSION`. The CB1 errors: (i) p0574 used as counterevidence to the homicide, when it concerns the extortion tape and is resolved; (ii) "rests on Asumi's reconstruction alone" ignores the warrant, the collapse and the narrated closure; (iii) CB1-CL-040's "enables" misdescribes a separate warrant. The calibration gap (CB1-CL-038 "low/tentative" against GPT CL-0004 "STRENGTHEN narrative attribution") is a genuine interpretive difference; on the text, "narratively established, legally unadjudicated" is the better calibration, which CB1's own FREEZES (H-36: "supported, not established") and READING l.262 ("probable") come closer to than its inventory. GPT's "Eguchi still disputes the reconstruction" (deep reading l.142) and "Eguchi denies it" (ACT-0003) omit the falter, the collapse and 犯人逮捕. The register's suggested まさか echo (PRO p0018 and C04 p0583) is not evidential: まさか is a common word.
6. **Residual uncertainty.** The novel shows no homicide confession or forensic result; the epilogue reports only the arrest (EPI p0031).
7. **Implications.** CB1: CB1-CL-038, CB1-U-18, `CB1_LONGITUDINAL_SYNTHESIS.md` l.111 and l.131 (the "intended to threaten" series fact rests on Asumi's hedged 「脅すつもりだったのか」 plus PRO p0018, which supports only an unforeseen outcome), `CB1_V07_READING.md` §F.4 (l.127) and §N.1 (l.262), CB1-CL-040. GPT: ACT-0003, RES-0001, CL-0004, ADJ-0002, deep reading l.142.
8. **Priority.** CB1-only; the GPT secondary is P3.
9. **Integration.** C-13, F-08, H-02.

### KCMP-V07-006 — Pre-reveal pointers to Eguchi

1. **Passage.** C03 p0074 (Snow Blossom 「過大評価」); p0098 「顔をこわばらせて」 on Kawamura's death; p0100 「面識があった程度ですが」; p0132 the copying charge is 「牽強付会」; p0209 (narration) 「開店資金集めも苦労したのに違いないが、そのことには触れなかった」; p0417 (Hashio) his future was crushed too; p0420 Aonuma's verdict 「人はいいが、性根は据わっていない」 and 「変わり身が早い」; p0586 (Nagasaka) 「薄情なんですよ」.
2. **Focalization and disclosure.** p0209 is Motoya's narratorial inference, the one overt nudge. Payoffs: Nishina's 「この店の運転資金が焦げ付いていた」 (C04 p0623); Eguchi's reversal on the copying charge (C04 p0589); the "slight acquaintance" claim is belied by the extortion relationship (C04 p0557, p0576).
3. **Established versus inferred.** The lines are on the page; their status as clues is analytic. They characterize without discriminating and do not reveal blackmail.
4. **Competing explanation.** GPT's mechanism claim (the extortion depends on information reported in the confrontation; Mystery l.41) stands. The pointers are low-salience characterization, and treating them as clues is retrospective.
5. **Verdict.** CONFIRM. Final: `GPT_OMISSION` (clue placement), with an interpretive dimension. GPT's disclosure ledger has no row for them, though its header requires recording "whether each decisive clue was available, salient or obscured". EV-0005 records the "slight acquaintance" claim without noting it is later belied.
6. **Residual uncertainty.** Salience is a judgment; the funding remark is the most specific pointer.
7. **Implications.** GPT Mystery V07 row and l.41, EV-0005, H-0007 to H-0009, SER-CL-0002.
8. **Priority.** P2.
9. **Integration.** D-05, G-02.

### KCMP-V07-007 — Inquiry calendar, lunar frame and the "evening interval"

1. **Passage.** C01 p0024 (body found 昨朝); p0172 「死亡推定時刻は午前一時から三時頃」; p0174 staff left about 23:00. C02 p0403, C03 p0229, p0440 (31 July is a Monday; p0440 「七月三一日月曜日から八月一日に日付が変わった火曜日」). C03 p0742. C04 p0272 (Mihara met on Wednesday), p0309 and p0364 (一昨日), p0497 (翌朝), p0621 「八時一七分です」. EPI p0088 (a wedding in October). PRO p0004 小望月; EPI p0150 寝待ち月.
2. **Disclosure.** Explicit time anchors throughout.
3. **Established versus inferred.** Established: Monday 31 July, the 01:00–03:00 interval on 1 August, the Wednesday meeting, the 08:17 arrest, the October wedding, the two moon names. Derived: the inquiry dates (Wed 2 to Sat 5 August) by day arithmetic. The year (2023) is CB1's inference only.
4. **Competing explanation.** GPT's restraint on the year is defensible, and its audit row "overnight July 31–August 1" is accurate.
5. **Verdict.** MODIFY. The compression stands. The intro's "The evening interval and recent computer activity fit an encounter after other staff left" (§3 ¶1) is a factual error: the interval is the small hours, after staff left at about 23:00. Final: `GPT_COMPRESSION` + `GPT_ERROR` (introduction).
6. **Residual uncertainty.** None on the anchors.
7. **Implications.** GPT intro §3 ¶1, audit late chronology, EV-0001.
8. **Priority.** P1 for the introduction error (low consequence); the calendar alone would be P3.
9. **Integration.** B-05, C-15.

### KCMP-V07-008 — V07 register and address

1. **Passage (whole-volume grep, each line read).** Asumi キミ to Motoya: C01 p0012, EPI p0124. Asumi あんた: only to Sayaka or both women (C02 p0033 あんたら; EPI p0009, p0137). 吉川くん: C01 p0316 (introducing him as 「相方の吉川くん」), C03 p0660 (direct), EPI p0144 (reference). Motoya: 小笠原 in speech (C01 p0021, p0427; C03 p0678; EPI p0126); 俺 (C03 p0670, p0711); never おまえ (the only おまえ are Nikaidō's, C01 p0573, and Yoshida's, C04 p0641). Eguchi: 僕 through C03 and at C04 p0539, then 俺 at p0589 and p0635. Asumi 「噓ですね？」 (C04 p0418). こいつ: Asumi of Motoya (EPI p0144) and Motoya of Asumi in thought (p0147). あたし in 10 lines.
2. **Speaker.** Direct speech; p0147 is thought.
3. **Established.** All forms and counts.
4. **Competing explanation.** The absence of あんた toward Motoya may be a sampling effect (no angry exchange of the V06 kind occurs).
5. **Verdict.** CONFIRM. Final: `GPT_OMISSION`. The V07 character ledger has CH, REL and INST rows only; grep for キミ, 噓ですね, こいつ finds nothing in GPT. GPT does record 僕 with Nagasaka, 俺 plus surname with Asumi (Motoya study l.43) and 相方 (Partnership l.43).
6. **Residual uncertainty.** Interpretation of the dropped あんた.
7. **Implications.** GPT reconstruction spec use; Asumi and Motoya study register passages.
8. **Priority.** P2.
9. **Integration.** E-09, G-05, G-06.

### KCMP-V07-009 — The recording's provenance and Shiobara's particulars

1. **Passage.** C04 p0576 (Asumi): 「塩原さんが河村さんにＩＣレコーダーを持たせたのです」 when she heard he would meet Eguchi; 「ＳＤカードは、塩原さんが持っていました」; she also supplied recordings of Eguchi threatening her. p0572 the demand: 「月曜までに一〇〇万円を振り込めよ」. p0443 she photographed and sometimes recorded cooks' talk. p0445 「半年で三〇〇万円ほど」. p0449 her mother's 「胆管がん」 and uninsured treatment. p0471–0473 Asumi's tentative view: civil tort, possibly 不正競争防止法, a matter for the second division. p0478 her mother died right after she left Ugetsuan.
2. **Speaker.** Asumi's account of custody at the confrontation; Shiobara's self-report at H-0013.
3. **Established.** As reported. Off-page: the SD hand-over and the recording dates.
4. **Competing explanation.** GPT's H-0014 ("Recordings delivered by Shiobara") records provenance in one phrase; the rest is detail. But the case ledger's EV schema requires "provenance and custody if shown" (ledger l.30), and custody is shown.
5. **Verdict.** CONFIRM. Final: `GPT_COMPRESSION`.
6. **Residual uncertainty.** How Shiobara learned of the meeting and recovered the card.
7. **Implications.** GPT EV-0011, ACT-0001, ACT-0002, CASE-0003.
8. **Priority.** P2.
9. **Integration.** C-10, C-11, C-12, E-11.

### KCMP-V07-010 — Motoya's appraisals of Asumi

1. **Passage.** C03 p0796–0797 (her 姉さんぶった tone 「鼻につく」, despite her 「本当に優秀な頭脳」); C04 p0215–0216 (he is drawn to Emiri's softness: 「爪の垢でも煎じて、亜澄に飲ませたいくらいだ」); C04 p0304 「なんでこういう可愛くない物言いをするのだろう」; C04 p0645 「すべては亜澄の功績だ」; p0655 「あらためて、亜澄はたのもしい女だなと元哉は思った」; EPI p0019 「おとなしくしていれば、亜澄は可愛いし、沙也香も美しいのに」; p0098 「よくもしゃあしゃあと」 and p0103 「よくもぬけぬけと」 at the engaged couple, then p0104 shame and p0107 applause; p0147 「こいつは本当に優秀な刑事だ」.
2. **Focalization.** All Motoya's interior. They are evidence about his state, not Asumi's.
3. **Established.** The appraisals as thought.
4. **Competing explanation.** GPT already records the core: private credit (REL-0003, REL-0005, Partnership l.37), irritation at her protective register (CH-0003), and "Motoya's attention to Asumi's appearance" as part of the romantic reading (Partnership l.51).
5. **Verdict.** MODIFY. This is compression of a recorded pattern, with omission of the specific aesthetic appraisals, the Emiri comparison and the sneers. Final: `GPT_COMPRESSION` + `GPT_OMISSION`.
6. **Residual uncertainty.** What 可愛い-if-quiet implies about attraction; both corpora leave the romance open.
7. **Implications.** GPT REL-0003, REL-0005, Partnership V07 row, Motoya study.
8. **Priority.** P3.
9. **Integration.** E-12, G-07.

### KCMP-V07-011 — The prologue's pronoun-less design and the introduction's "He"

1. **Passage.** PRO p0004–p0036: no personal pronoun or gendered marker for the stabber; the only self-reference is 「そう簡単に自分のしわざとわかるわけはない」 (p0030).
2. **Focalization.** Unnamed focal consciousness; reader-only.
3. **Established.** The prologue withholds name and sex. Inferred: that this is a deliberate device (it keeps female staff, including Shiobara, formally open at H-0001).
4. **Competing explanation.** The introduction is spoiler-flagged through V07 and the culprit is male, so "He" (§3 ¶1) is a synopsis choice made with later knowledge, not a wrong story fact. The V06 introduction does the same for the わたし speaker of its prologue ("He remembers Mitsuki").
5. **Verdict.** MODIFY. The structural omission stands (no GPT file notes the pronoun-free design; H-0001 says "a focal consciousness", K-0001 "No name or dispute"). The `GPT_ERROR` component does not: nothing in the introduction misstates what happens, though "He" obscures the device for a reader using it to understand the prologue. Final: `GPT_OMISSION` with a presentation dimension.
6. **Residual uncertainty.** Authorial intent behind the device.
7. **Implications.** GPT K-0001, intro §3 ¶1, Policing study §Who speaks inside the prose (opening voices).
8. **Priority.** P3.
9. **Integration.** B-05, D-04.

### KCMP-V07-012 — Izumida's own account is contradicted by the late alibi

1. **Passage.** C02 p0403 (Izumida): prepped until about one, then 「自転車に乗って常盤の自宅まで帰って寝ました」, nobody to confirm, 「家に帰っても誰もいません」. EPI p0110–0116 (Sayaka): he was with Emiri, 「七里ヶ浜の英美里のアパートに」, on the night of 31 July; p0120 「泉田が小さく頭を下げた」; p0121 Motoya: 「恋人のアリバイ証言がどれほど信用されるかは別として」; p0122 Emiri was too embarrassed to say it.
2. **Speaker and disclosure.** Izumida's direct statement to the detectives (H-0006); Sayaka's late civilian report (H-0015), with Izumida's tacit acceptance.
3. **Established versus inferred.** Established: two incompatible location accounts for the same night. Inferred: that Izumida's was false (if Sayaka is right) and concealed the relationship.
4. **Competing explanation.** Sayaka's report is uncorroborated and gives no hour; GPT's caution about corroboration (RES-0002) is correct. Izumida might have gone to Emiri's after one; but he said he went home to sleep.
5. **Verdict.** MODIFY. No GPT sentence is literally false: Mystery l.49 contrasts the late account with "the case file's earlier absence of an alibi", and the deep reading says he "has no one to confirm his routine". But no GPT file records that the late account contradicts his own statement, and l.49's "compatible statements about who disclosed what" frames the matter as nondisclosure. Final: `GPT_OMISSION` with a misleading-framing dimension.
6. **Residual uncertainty.** The truth of Sayaka's report.
7. **Implications.** GPT RES-0002, EV-0004, H-0015, Mystery l.49, Partnership l.49. CB1-CL-042 ("His false account… established") presumes Sayaka's report true; it should be conditional (H-04).
8. **Priority.** P2.
9. **Integration.** A-09, C-14, E-13, G-03, H-04.

---

## 3. Integration action list

IDs are proposals; an integrator should confirm they do not collide. Revision IDs follow each ledger's append-only rule (`-RNN` with predecessor). Locators use GPT native form.

### (a) Frozen deep readings — errata (never edit the reading)

- **A-01** `readings/KSOA_V06_DEEP_READING.md#ksoa-v06-h-0001` (KCMP-V06-003). *Erratum:* "H-0001's 'The speaker sees someone they believe can explain the past' understates PRO p[0030]–p[0035]. The speaker calls the person waiting at the shelter あいつ, sees in that figure 「わたしたちを不幸に陥れた者」 and resolves to make that person tell the truth. The identification remains the speaker's belief under the doubt of p[0004]–p[0005]. Prospectively, once Kasuya's account (H-0007) and Mizutani's denial (H-0009) are available, a reader can infer that the meeting partner was the person Nonaka held responsible for the frame."
- **A-02** same file, `#craft-knowledge-and-police-disclosure`, third paragraph (KCMP-V06-009). *Erratum:* "'Asumi … notes the common timing of the two departures' misattributes the observation. Motoya makes it (C02 p[0525]); Asumi proposes the master as the problem (p[0523]), takes up Motoya's point (p[0527]) and voices her intuition that the key lies there (p[0531])."
- **A-03** same file, `#a-present-death-and-two-damaged-histories` ¶4 and `#ksoa-v06-h-0010` (KCMP-V06-001). *Erratum:* "After Yakushiji reports overwhelming sleepiness from about eight (C03 p[0711]), Asumi charges Kume with putting a sleep-inducer in Yakushiji's champagne (p[0717]) and says investigators already hold the doctor's statement on Kume's prescription from the 常盤総合病院 psychosomatic clinic (p[0721]). Kume deflects (p[0722]); Kasuya calls it circumstantial (p[0724]). This is the 'additional circumstantial support' of H-0010 and EV-0010. The drugging is Asumi's accusation; the doctor's statement as reported establishes the prescription. The champagne was the pupils' gift and available earlier (C02 p[0500]; C03 p[0284]); the prescription and statement are an off-page finding first disclosed at the confrontation."
- **A-04** same file, `#who-can-know-what-happened-at-the-party` ¶1 (KCMP-V06-002; agreement-sample A7). *Erratum:* "Asumi's challenge has three parts: a question about what Nonaka communicated to the two pupils, which Motoya's narration takes to be her characteristic bluff (C03 p[0679]–p[0681]); a shout test showing that a loud voice in the reception room does not reach Kosugi's upstairs room (p[0684]–p[0687]); and the 中抜け argument with distances: under 700 m, a round trip under thirty minutes, five minutes for the act (p[0691]–p[0695]). Also: Asumi asked Shinagawa only for the time (C01 p[0812]); the witness supplied the news-programme anchor herself (p[0814])."
- **A-05** same file, `#a-present-death-and-two-damaged-histories` ¶1 (KCMP-V06-010). *Erratum:* "The shelter is the 梶原-side (north) あずまや of 源氏山公園 (C01 p[0030], p[0908]; C03 p[0711]). The park has seven approaches and the arbour lies 50–60 m from 梶原五丁目 (C01 p[0149]). Sayaka and Emiri are at the cordon for a magazine shoot of the 縁結び石 at 葛原岡神社 (p[0300]–p[0324]). 梶原 is in 鎌倉署's jurisdiction, 山ノ内 in 大船署's (p[0684]). The exhibition at stake is the 全美展 (p[0913]–p[0914]). By Kasuya's surmise the title work depicts the spring falling from the cliff at 銭洗弁天 (C02 p[0597]); 薬師寺邸 lies in 佐助 east of 銭洗弁天 (C03 p[0312])."
- **A-06** same file, `#ksoa-v06-h-0004` and closing paragraph of `#a-present-death-and-two-damaged-histories` (KCMP-V06-011). *Erratum:* "The examiner attributes death to two blows from behind with a rod-like object (C01 p[0908]); Yakushiji's relay names a 棒 (C03 p[0711]). The planned search of Nonaka's house (C01 p[0910]), the city payphone calls (p[0915]), the camera and dashcam canvass of the seven approaches (p[0917]) and the means by which Nonaka contacted Kasuya (C03 p[0711]) are not followed up on the page."
- **A-07** `readings/KSOA_V07_DEEP_READING.md#final-disclosures-and-professional-dependence` ¶3 and `#ksoa-v07-h-0015` (KCMP-V07-002). *Erratum:* "The acknowledgement comes after Motoya has lost consciousness over drinks (EPI p[0131]) and come to after eleven (p[0132]). Asumi says it to Sayaka during their drunken truce (p[0136]–p[0143]), referring to Motoya in the third person (p[0144]), with a serious face (p[0145]). Motoya overhears; whether Asumi knew he was awake is unstated. His pledge (p[0146]–p[0148]) is followed at once by a second blackout (p[0149]). As in V01 (STATE-0005, REL-0003), the intoxicated setting limits projection to later conduct, while the serious face and the content support sincerity at the moment. 'Reciprocal acknowledgement' should be read as two separate acknowledgements, neither addressed to the other."
- **A-08** same file, `#ksoa-v07-h-0010` and `#a-solution-reached-through-a-person-the-first-inquiry-had-cleared` ¶1 (KCMP-V07-003). *Erratum:* "The autopsy gives a sharp blade such as a sashimi knife, traumatic shock and death within some tens of minutes, at 01:00–03:00 on 1 August (C03 p[0742]–p[0743]). The canvass is collecting car-navigation recordings from nearby parked cars, without result so far (p[0745]–p[0746]). The prologue's knife in the right hand (PRO p[0005]) is reader-only; Asumi cites the autopsy weapon type in her reconstruction (C04 p[0601]). The weapon is not recovered on the page."
- **A-09** same file, `#final-disclosures-and-professional-dependence` ¶1 and `#ksoa-v07-h-0015` (KCMP-V07-012). *Erratum:* "Izumida did not only lack a corroborator: he told the detectives he prepped until about one and cycled home to 常盤 to sleep, with no one at home (C02 p[0403]). Sayaka's late report puts him at Emiri's 七里ヶ浜 flat that night (EPI p[0116]), and he bows slightly (p[0120]). If her report is true, his earlier account was false and concealed the relationship. It remains uncorroborated, and Motoya notes the limited credibility of a lover's alibi (p[0121])."

### (b) Reading introductions — targeted edits

- **B-01** `readings/KSOA_V06_READING_INTRODUCTION.md` §3 ¶1 (KCMP-V06-003). Replace "He sees someone he believes can explain what happened." with "He sees the figure of the person he holds responsible for their misfortune and resolves to make that person tell the truth."
- **B-02** same file, §3 ¶2 (KCMP-V06-010). Replace "At the shelter the police have" with "At a shelter on the 梶原 side of 源氏山公園 the police have"; replace "Emiri and Sayaka are at the cordon." with "Emiri and Sayaka, there for a magazine shoot at the 縁結び石 of nearby 葛原岡神社, are at the cordon."
- **B-03** same file, §3 ¶6 (KCMP-V06-001, -002). After "Asumi leads the questioning" insert: "She shows that a shout in the reception room does not reach the housekeeper upstairs and that the shelter is under 700 m away, within a half-hour round trip." After "He slept during the relevant interval and heard what they had done after they returned." insert: "Asumi then accuses Kume of putting his prescribed sleep-inducer in Yakushiji's champagne, citing a doctor's statement the investigators have obtained; Kume deflects and Kasuya calls the case circumstantial."
- **B-04** same file, §3 ¶7 (KCMP-V06-005). Replace "Over drinks Asumi calls the outing a date in her exchange with Sayaka and says she and Motoya are buddies." with "Over drinks Sayaka asks whether this is a date. Asumi, already well into her drink, says it is and challenges Sayaka's right to call him 元哉くん. Sayaka retorts that Asumi is only his work partner and suggests rank compels him to drink with her; Asumi answers that they are buddies."
- **B-05** `readings/KSOA_V07_READING_INTRODUCTION.md` §3 ¶1 (KCMP-V07-007, -011). Replace "He considers seeking help and leaves." with "The assailant considers seeking help and leaves."; "His identity and the exchange that led to the attack remain out of view." with "The assailant's name, and even sex, and the exchange that led to the attack remain out of view."; "The evening interval and recent computer activity" with "The 01:00–03:00 interval on 1 August and recent computer activity".
- **B-06** same file, §3 ¶2 (KCMP-V07-001). Replace "run by Kawamura's former teacher Aonuma" with "run by Aonuma, who had trained with Kawamura under the same Ginza chef as his senior fellow apprentice (兄弟子)".
- **B-07** same file, §3 ¶7 (KCMP-V07-002). Replace "Asumi tells Motoya that she can do the work because he is there. Motoya hears her and privately resolves to keep supporting her." with "Late in the evening, after Motoya has blacked out over drinks and come to, the drunk Asumi tells Sayaka with a serious face that she can do the work because he is there. Motoya overhears, privately resolves to keep supporting her and blacks out again."

### (c) `KSOA_CASE_EVIDENCE_LEDGER.md`

- **C-01** `## V06 case evidence`, new row `KSOA-V06-EV-0011` | Sleep-inducer accusation and doctor's statement | H-0010 | C03 0711–0724; C02 0500; C03 0284 | "Yakushiji reports sudden sleepiness from about eight. Asumi accuses Kume of putting a sleep-inducer in Yakushiji's champagne and reports that investigators hold the doctor's statement on Kume's prescription (常盤総合病院 心療内科). Kume deflects; Kasuya calls it circumstantial. The pupils had brought the champagne (earlier testimony of Kume and Kosugi). Status: accusation plus off-page finding first disclosed here; the statement establishes the prescription, not the act."
- **C-02** new row `KSOA-V06-EV-0010-R01` (predecessor EV-0010) | H-0010 | C03 0679–0727 | "Adds the components of Asumi's test: question to the pupils narrated as her probable bluff (0679–0681); shout test (0684–0687); 中抜け argument with distance under 700 m, round trip under 30 minutes, 5 minutes for the act (0691–0695). The 'circumstantial support' is EV-0011. No physical corroboration in the scene (unchanged)."
- **C-03** new row `KSOA-V06-ACT-0002-R01` (predecessor ACT-0002) | H-0010 | C03 0711, 0717–0724 | "Relayed account: Kume struck from hiding in the wood with a 棒 while Kasuya kept Nonaka talking; motive in Kasuya's reported words 「先生と一門を守るために」. Asumi additionally charges Kume with drugging the host (EV-0011), an enabling act not admitted on the page."
- **C-04** new row `KSOA-V06-ACT-0004-R01` (predecessor ACT-0004) | H-0010 | C03 0705–0739 | "Yakushiji's stated reason for concealment: 「糟屋と久米を守りたかっただけ」 (0705). He calls himself an accomplice (0733); Motoya answers that he would not be an accessory but 犯人隠避罪 may apply (0735). He leans toward ending the workshop (0737, inclination not decision)."
- **C-05** new row `KSOA-V06-CASE-0001-R01` (predecessor CASE-0001) | H-0011 | C01 0030, 0149, 0908–0917; C03 0711 | "Location: north (梶原-side) arbour of 源氏山公園. Remaining ambiguities: the rod-like weapon is never identified or recovered; the planned house search and the wallet are not reported; the city payphone calls are unexplained; the camera and dashcam canvass is unreported; the means by which Nonaka contacted Kasuya is unstated; the drugging is accused, not admitted."
- **C-06** new rows `KSOA-V06-EVT-0001` | Birthday gathering and killing | H-0010 | C03 0284, 0304, 0711; C01 0814 | "Mon 17 July: pupils arrive 19:07 by taxi; Kosugi serves about an hour then goes upstairs; host sleepy from about 20:00; appointment at the 梶原-side arbour at 21:30 (relayed); cry just before 22:00; host wakes after midnight; taxis collect the pupils 01:16." `KSOA-V06-EVT-0002` | Gathering | H-0010 | C03 0540 | "The confrontation at 薬師寺邸 takes place 「翌々日の土曜日の日暮れ前」, two days after the Mizutani re-interview."
- **C-07** `## V07 case evidence`, new row `KSOA-V07-EV-0012` | Autopsy and footage collection | H-0010 | C03 0741–0746 | "Interval confirmed as 01:00–03:00 on 1 August. Weapon: a sharp blade such as a sashimi knife; cause traumatic shock; death within some tens of minutes. Car-navigation recordings from nearby parked cars are being collected; no suspect found so far. Weapon not recovered."
- **C-08** new row `KSOA-V07-ACT-0003-R01` (predecessor ACT-0003) | H-0014 | PRO 0005, 0018; C04 0598–0608 | "The reconstruction cites the autopsy weapon type and hedges intent (「脅すつもりだったのか」). Eguchi calls it an invention (0603) and then falters (0608). Prologue knife in right hand is reader-only."
- **C-09** (reserved; folded into C-08).
- **C-10** new row `KSOA-V07-EV-0011-R01` (predecessor EV-0011) | H-0014 | C04 0570–0589 | "Provenance and custody: Shiobara had Kawamura carry an IC recorder when he was to meet Eguchi and kept the SD card; she also supplied recordings of Eguchi threatening her (0576). Recorded demand: ¥1,000,000 by Monday (0572). Motoya thinks the menacing voice does not sound like Eguchi's but a voiceprint would settle it (0574–0575); Eguchi's reaction and justification amount to acknowledgment (0578–0589). Off-page: recording dates and the hand-over."
- **C-11** new row `KSOA-V07-ACT-0001-R01` (predecessor ACT-0001) | H-0013 | C04 0439–0478 | "Kawamura's instructions covered ingredients, suppliers, timing, processing and service (0439). Payment about ¥3,000,000 for half a year (0445). Mother's bile-duct cancer and uninsured treatment (0449); she died right after Shiobara left Ugetsuan (0478). Kawamura's motive, as reported by Shiobara with hedges: a complex toward his 兄弟子 Aonuma, who bullied him when young, and a drive to overtake him (0465). Asumi's tentative legal view: civil tort, possibly unfair competition (0471–0473)."
- **C-12** new row `KSOA-V07-ACT-0002-R01` (predecessor ACT-0002) | H-0014 | C04 0572, 0623 | "Demand of ¥1,000,000 by Monday. Nishina: Fleur's operating funds had gone bad."
- **C-13** new row `KSOA-V07-RES-0001-R01` (predecessor RES-0001) | H-0014 | C04 0603–0652 | "Closure markers: Eguchi's denial (0603) gives way to a falter (0608); he blanches at the extortion arrest (0618–0620) and collapses with 「終わりだ」 immediately after the separate homicide-search warrant is announced (0627–0630); Motoya's narration speaks of 犯人逮捕 dissolving the HQ (0652). Still no homicide confession, weapon or trace result."
- **C-14** new row `KSOA-V07-RES-0002-R01` (predecessor RES-0002) | H-0015 | C02 0403; EPI 0110–0122 | "The late report contradicts Izumida's own account (home alone in 常盤 after prepping until about one). Izumida bows; if the report is true his account was false. Still uncorroborated; Motoya notes a lover's alibi carries limited weight."
- **C-15** new rows `KSOA-V07-EVT-0001`… | H-0015 | C01 0024, 0172, 0174; C02 0403; C03 0440, 0742; C04 0272, 0309, 0364, 0497, 0621; EPI 0088 | "Mon 31 July: staff leave about 23:00. 01:00–03:00 Tue 1 August: death. Morning of 1 August: discovery. Days derived from 31 July = Monday: Wed 2 detectives at the scene, Mihara and Shiobara seen; Thu 3 Eguchi, Hashio, Nagasaka; Fri 4 photographs and Shiobara visit; Sat 5 morning confrontation, arrest at 08:17, epilogue that evening. Wedding planned for October. Lunar frame 小望月 (PRO 0004) to 寝待ち月 (EPI 0150)." Year not stated.

### (d) `KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md`

- **D-01** `## V06 disclosure history`, new row `KSOA-V06-K-0001-R01` (predecessor K-0001) | H-0001 | PRO 0004–0039 | "Reader knows the speaker identifies the person waiting at the shelter (あいつ, 0030) as 「わたしたちを不幸に陥れた者」 (0033) and means to make that person tell the truth (0034–0035), under the conditional doubt of 0004–0005."
- **D-02** new row `KSOA-V06-D-0006` | H-0010 | C03 0711–0724; prior C02 0500, C03 0284, 0288, 0296 | "Asumi discloses, as an off-page finding, the doctor's statement on Kume's prescription and accuses Kume of drugging the host's champagne. Possible prior clues: the pupils brought the champagne; the host reportedly drank all evening; the host called for the taxis by intercom. Available, low salience; it discriminates Kume's enabling act only with the off-page finding."
- **D-03** (none).
- **D-04** `## V07 disclosure history`, new row `KSOA-V07-K-0001-R01` (predecessor K-0001) | H-0001 | PRO 0004–0036 | "Reader also knows the weapon is a kitchen knife held in the right hand (0005) and that the assailant did not expect this outcome (0018). The prologue uses no personal pronoun for the assailant (self-reference only 自分のしわざ, 0030), so name and sex are withheld."
- **D-05** new row `KSOA-V07-ADJ-0004` (retrospective) | H-0014 | C03 0074, 0098–0100, 0132, 0209, 0417–0420, 0586; C04 0557, 0576, 0589, 0623 | "Pre-reveal pointers to Eguchi were available and low in salience: dismissal of the copying charge, later reversed; 'only slight acquaintance' with Kawamura, later belied by the extortion relationship; the narration's note that he avoided mentioning his funding, which pays off in Fleur's failing operating funds; Aonuma's verdict relayed by Hashio; Nagasaka's 薄情. They characterize without discriminating; the funding remark is the most specific."
- **D-06** new row `KSOA-V07-ADJ-0003-R01` (predecessor ADJ-0003) | H-0015 | EPI 0124–0149 | "Asumi's credit is spoken to Sayaka about Motoya in the third person, during a drunken truce; Motoya overhears after regaining consciousness and blacks out again after his private pledge. Whether Asumi knew he was awake is unstated."

### (e) `KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md`

- **E-01** `## V06 character and institutional state`, new row `KSOA-V06-CH-0005-R01` (predecessor CH-0005) | H-0010 | C03 0679–0699 | "Asumi's test consists of a probable bluff (Motoya's narration), a shout test and a distance argument before she accuses Yakushiji of lying to her."
- **E-02** new row `KSOA-V06-REL-0004-R01` (predecessor REL-0004) | H-0011 | EPI 0008–0043; C01 0103–0111, 0932 | "Sayaka proposes 'date' and switches from 吉川さん to 元哉くん; Asumi, already drunk, accepts 'date' and challenges Sayaka's right to that address; Sayaka counter-challenges Asumi's entitlement, calls her a mere work partner and suggests rank compels him; Asumi answers バディ; Motoya inwardly denies coming gladly and escapes. Label sequence across the volume: Masaki's 相方 with Motoya's demurral (C01 0110), 宿命的 pairing (0932), バディ. Intoxication and the feud bound any inference about affection."
- **E-03** new row `KSOA-V06-VOICE-0001` | H-0011 | C01 0140, 0420, 0650–0652; C02 0263; C03 0315–0338; EPI 0013–0017 | "Asumi to Motoya: 吉川くん ×4; あんた ×5 (C01 0650; C03 0315, 0329 ×2, 0338), glossed by the narration as a sign of real anger (C01 0652); no キミ. Motoya uses no おまえ. Sayaka uses 吉川さん until the epilogue's provocative 元哉くん, which Asumi contests. Kume shifts わたし → 俺 under accusation (C03 0629)."
- **E-04** new row `KSOA-V06-REL-0003-R01` (predecessor REL-0003; cross-reference REL-0001) | H-0009 | C01 0297; C03 0313–0339 | "Evidence on the motive of Asumi's hostility: the narration's recap says she has suspected Motoya's relation with Sayaka since V05 (C01 0297); she gives personal dislike as her reason (0333) and Motoya's narration takes that as the clear reason (0334, hedged). Investigative suspicion of Emiri, who had lied, is a third reading. Unresolved."
- **E-05** new rows `KSOA-V06-PERSON-0001` | H-0004 | C01 0910 | "薬師寺国昭 (やくしじ くにあき), 75, glass master in 佐助, 全美展 会友; Nonaka's former teacher; Mitsuki's father." `KSOA-V06-STATE-0001` | H-0010 | C03 0426, 0444, 0452, 0551, 0555, 0705–0706, 0711, 0733–0740 | "States a principle of protecting the artist and the school over the person (0551, 0555); refuses cooperation (0452); covered for the pupils to protect them (0705); the killers framed their act in his value (0711, relayed); self-reproach, an inclination to end the workshop and 「愛は盲目と言うが」 (0737–0739). Register shifts from 君 to Asumi (0409, 0444) to 「小笠原さん、吉川さん」 (0733)."
- **E-06** new row `KSOA-V06-STATE-0002` | H-0009 | C02 0363–0365, 0456–0459; C03 0063 | "Asumi, to a witness, says she has no one to drink with, which Motoya inwardly reads as a confession of being alone (hypothetical framing, said in passing); presents Emiri's information to Kume as 'from a friend', which Motoya calls brazen; lives in a 材木座 apartment."
- **E-07** new row `KSOA-V06-INST-0002-R01` (predecessor INST-0002) | H-0008 | C03 0207; C02 0715–0719 | "The narration states that HQ did not regard Yakushiji as important and had not researched his family, which explains why Emiri's disclosure was new to the inquiry."
- **E-08** `## V07 character and institutional state`, new rows `KSOA-V07-PERSON-0001` | H-0003 | C01 0024, 0384; C03 0331; C04 0465 | "河村重良, 64, chef of 《山辺茶寮》; fellow apprentice (兄弟弟子) of Aonuma under the same Ginza chef, Aonuma the senior (兄弟子)." `KSOA-V07-STATE-0001` | H-0013 | C01 0152; C04 0439, 0460, 0465 | "Two images: Mihara's conscientious, shrewd, gentle-with-staff chef; Shiobara's doubly mediated, hedged report of a complex toward the 兄弟子 who bullied him and a drive to overtake him, enacted by wholesale adoption of Snow Blossom techniques."
- **E-09** new rows `KSOA-V07-VOICE-0001` (Asumi) | H-0015 | C01 0012, 0316; C03 0660; C04 0418; EPI 0009, 0124, 0137, 0144 | "キミ to Motoya twice; no あんた to Motoya (あんた only to Sayaka or both women); 相方の吉川くん when introducing him; 噓ですね？ under pressure; こいつ of Motoya to Sayaka." `KSOA-V07-VOICE-0002` (Motoya) | H-0015 | C01 0021, 0427; C03 0493, 0670, 0678, 0711; EPI 0126, 0147 | "小笠原 in speech ×4; 俺 ×2 with Asumi; 僕 with civilians; no おまえ; こいつ of Asumi in thought." `KSOA-V07-VOICE-0003` (Eguchi) | H-0014 | C03 passim; C04 0539, 0589, 0635 | "僕 through his interview and at first denial; 俺 once the recording is played."
- **E-10** new rows `KSOA-V07-REL-0004-R01` (predecessor REL-0004) | H-0015 | EPI 0122–0130 | "Asumi challenges Motoya with キミ over the undisclosed Emiri meeting; he does not answer." `KSOA-V07-REL-0005-R01` (predecessor REL-0005) | H-0015 | EPI 0131–0149 | "The acknowledgement is said to Sayaka in a drunken truce, about Motoya in the third person, overheard after a blackout; his pledge is followed by a second blackout. Bound projection as in V01 STATE-0005."
- **E-11** new row `KSOA-V07-STATE-0002` (Shiobara) | H-0013 | C04 0443–0485, 0576 | "Paid industrial espionage for Kawamura (about ¥3m in six months) during her mother's bile-duct cancer; mother died after she left; remorse; corroborated alibi; custodian of the SD card and other recordings."
- **E-12** new row `KSOA-V07-REL-0006` (Motoya → Asumi, appraisals) | H-0015 | C03 0796–0797; C04 0215–0216, 0304, 0645, 0655; EPI 0019, 0098–0107, 0147 | "Privately: irritation at her big-sister tone despite her ability; wishes she had Emiri's softness; resents her uncute phrasing; credits the solution to her; 'a dependable woman'; 'cute if she kept quiet'; 'truly an excellent detective'. Outwardly applauds the engagement while inwardly sneering. Evidence of his state only."
- **E-13** new row `KSOA-V07-STATE-0003` (Izumida) | H-0015 | C02 0403; EPI 0110–0122 | "If Sayaka's report is true, Izumida gave the police a false location (home alone in 常盤) to protect his private relationship with Emiri; he tacitly accepts the report."

### (f) `KSOA_CLAIM_REVISION_LEDGER.md`

- **F-01** (none).
- **F-02** `## V06 claim history`, new row `KSOA-V06-CL-0004-R01` (predecessor CL-0004) | H-0010 | C03 0421, 0649–0657 | "REVISE (scope): add the focalizer's hedged supplementary reading that Mitsuki also wanted to escape her father's excessive love, and his judgment that the father-daughter relation was 歪 (0421). Asumi's synthesis (0649–0657) remains one mediated account; the two are compatible."
- **F-03** new row `KSOA-V06-CL-0005-R01` (predecessor CL-0005) | H-0011 | EPI 0008–0035; C01 0103–0111 | "REVISE: the buddy label is claimed in a two-way entitlement contest over the address 元哉くん, by an already drunk Asumi, after Sayaka's rank jab; Motoya earlier demurred at 相方. The label gains an explicit user; direction of affection unresolved (unchanged)."
- **F-04** new row `KSOA-V06-CL-0006` | H-0009 | C01 0297; C03 0313–0339 | "OPEN: motive of Asumi's hostility to Sayaka and Emiri. Narration's recap supports suspicion of Motoya's relation with Sayaka; Asumi states dislike and the narration accepts it; investigative suspicion of Emiri is a third reading. No interior evidence decides it. Confidence: low for any single motive."
- **F-05** new row `KSOA-V06-CL-0007` | H-0010 | C03 0551, 0555, 0705, 0711 | "Moderate. The killers' reported motive formula, protecting the master and the school, reproduces Yakushiji's own stated priority of artist and school over person, and plausibly explains his cover-up. Counter: the formula is relayed by Yakushiji and is self-serving for the killers."
- **F-06** `## V07 claim history`, new row `KSOA-V07-CL-0006-R01` (predecessor CL-0006) | H-0015 | EPI 0124–0149 | "REVISE (bounds): Asumi's acknowledgement is voiced to Sayaka about Motoya, during a drunken truce, and overheard; Motoya's commitment is internal and followed by a blackout. Two-way professional dependence remains strengthened for the moment depicted; projection beyond the scene is limited as in V01-CL-0005-R01."
- **F-07** `## Series claim history`, new row `KSOA-SER-CL-0004-R01` (predecessor SER-CL-0004) | "**High** for the occurrence of a spoken acknowledgement and a private pledge; **moderate** for treating either as a stable commitment. Both occur in an intoxicated scene; the acknowledgement is addressed to Sayaka in the third person and overheard after a blackout; the pledge is followed by a second blackout." | REVISE, citing V07-CL-0006-R01 and V06-CL-0005-R01; V01-CL-0005-R01 as the precedent for the bound | Directed partnership.
- **F-08** new row `KSOA-V07-CL-0004-R01` (predecessor CL-0004) | H-0014 | C04 0603–0652 | "PRESERVE. Add closure markers (falter, collapse after the homicide-search announcement, separate warrant, narrated 犯人逮捕) as support for the narrative attribution; keep inference, arrest, physical proof and judgment separate."

### (g) Studies

- **G-01** `studies/KSOA_MYSTERY_FORM_AND_CAUSALITY.md#what-a-reader-can-infer-before-the-solution`, V06 row (KCMP-V06-001, -003). Early grounds: add "The prologue's speaker casts the person waiting at the shelter as the author of the couple's misfortune (PRO p[0033])." Later discrimination: add "The host's sleep acquires a mechanism only through Asumi's accusation and an off-page doctor's statement (C03 p[0717]–p[0721]); the champagne itself was planted earlier (C02 p[0500]; C03 p[0284])."
- **G-02** same section, V07 row and the following paragraph (KCMP-V07-006, -003). Add: "Low-salience pointers characterize Eguchi before the confrontation: his avoided mention of opening funds (C03 p[0209]), later matched by Fleur's failing operating funds (C04 p[0623]); a claimed slight acquaintance belied by the extortion; and others' verdicts (C03 p[0420], p[0586]). They do not discriminate him." Add the autopsy weapon type to the scene evidence.
- **G-03** same file, `#direct-action-enabling-action-and-knowledge` ¶4 (l.49) (KCMP-V07-012). Replace "That late account and the case file’s earlier absence of an alibi are compatible statements about who disclosed what." with "That late account contradicts Izumida's own statement that he went home alone to 常盤 (C02 p[0403]); if it is true, he concealed the relationship by giving a false location, not merely by withholding an alibi. The report itself is uncorroborated."
- **G-04** `studies/KSOA_POLICING_PLACE_AND_NARRATION.md#places-media-and-the-reach-of-a-witness` ¶2 (KCMP-V06-010) and `#who-can-act-on-a-question` (KCMP-V06-012). In ¶2 replace "V06 places the detectives above and then below a cliff" with "V06 places the detectives on 源氏山's north lawn by the 梶原-side arbour and then below its cliff, on a lane where 梶原 (鎌倉署) faces 山ノ内 (大船署)". In the institutional section add: "The narration states that HQ had not even researched Yakushiji's family (V06 C03 p[0207])."
- **G-05** `studies/KSOA_MOTOYA_KITSUKAWA.md`: `#a-focalizer-with-a-job-of-his-own` ¶3 add "After the Kume interview he notices that the two pupils left at about the same time, which strictness cannot explain (V06 C02 p[0525])" (KCMP-V06-009). `#discretion-and-the-risk-of-being-accommodating` ¶2: replace "His later recommendation to defer independent checks follows a resource judgment" with "His later recommendation to defer independent checks rests on the women's thin connection and an overstated claim that their alibis are solid; Masaki supplies the resource reason (V06 C01 p[0599]–p[0605])" (agreement-sample A8). `#registers-habits-and-the-final-resolve` ¶1 add V07 VOICE-0002 forms (KCMP-V07-008); ¶3 replace "after hearing her explicit appreciation" with "after overhearing her appreciation, spoken to Sayaka in a drunken scene, and just before he blacks out again" (KCMP-V07-002).
- **G-06** `studies/KSOA_ASUMI_OGASAWARA.md`: `#address-ordinary-life-and-felt-need` ¶1 add the V06 元哉くん contest and V07 キミ with no あんた toward Motoya (KCMP-V06-005, V07-008); ¶2 add "no one to drink with" (V06 C02 p[0363]) (KCMP-V06-013); ¶3 add after the V07 sentence "said to Sayaka in a drunken truce and overheard by Motoya" (KCMP-V07-002). `#the-costs-and-uses-of-control`: add the V06 narrated bluff (C03 p[0679]–p[0681]) and the textual anchors on her hostility (C01 p[0297]; C03 p[0333]–p[0334]) (KCMP-V06-002, -006).
- **G-07** `studies/KSOA_PARTNERSHIP.md`: l.25 replace "Asumi tells those still awake at the counter that she can do the work because he is there." with "Late at the counter, the drunk Asumi tells Sayaka that she can do the work because he is there; Motoya, just come to, overhears." (KCMP-V07-002). `#directed-states-by-volume` V06 row add "disputes Sayaka's right to call him 元哉くん"; V07 row replace "with Sayaka present" with "to Sayaka, while both are drunk, overheard by Motoya after a blackout" and add his private sneers at the engagement (KCMP-V06-005, V07-002, -010). `#sayaka-and-emiri-have-their-own-stakes` l.47 add after "Asumi’s apparent jealousy": "(the narration's recap supports suspicion, V06 C01 p[0297]; Asumi herself cites dislike and Motoya accepts it, C03 p[0333]–p[0334])" (KCMP-V06-006).
- **G-08** `studies/KSOA_INTEGRATED_SERIES_SYNTHESIS.md#the-work-people-leave-behind` ¶3 (l.42) (KCMP-V06-007). After "Yakushiji, like Marina, acts on a belief about how best to protect another person’s future." add "By his own account he protected the artist and the school above the person (V06 C03 p[0555]), the value in which the killers framed their act (p[0711])."

### (h) CB1-only corrections (record in the adjudication report; the baseline is frozen)

- **H-01** (KCMP-V06-004). `CB1_V06_EXIT_STATE.md` row 9 and CB1-V06-K-02; `CB1_YAKUSHIJI_KUNIAKI_MONOGRAPH.md` §4 row "2012" and l.194; `CB1_V06_CHARACTER_EVIDENCE.md` Part 2 (糟屋, "told no one — contradicted by 薬師寺"); `CB1_V06_READING.md` §E7 and the §F4 row. *Correction:* "Yakushiji admits only that both pupils told him the stalker story (C03 p[0618]). Who told him of the colourant switch, for which he expelled Mizutani (p[0444]), is never stated; that the pupils did is an inference from Mizutani's relay of a single informant (p[0503]), Kume's accusation (p[0633]) and Asumi's summary (p[0624]). Kasuya's sighting is shown false by Kume's accusation, not by Yakushiji, and whether Kasuya told anyone of it is unstated."
- **H-02** (KCMP-V07-005). CB1-CL-038, CB1-U-18, `CB1_LONGITUDINAL_SYNTHESIS.md` l.111, `CB1_V07_READING.md` §F.4 (l.127) and §N.1 (l.262), CB1-CL-040, LS l.131. *Correction:* "C04 p[0574] concerns whose voice is on the extortion recording and is resolved in the scene by Eguchi's reaction and justification (p[0578]–p[0589]); it is not evidence against the homicide attribution. The attribution rests on more than the reconstruction: a separate homicide-search warrant (p[0627]), Eguchi's collapse immediately after it (p[0630]), the narrated 犯人逮捕 (p[0652]) and the absence of a live alternative. Calibrate as narratively established, legally unadjudicated (no confession, weapon or trace result shown), not 'low'. The extortion arrest does not 'enable' the search; the search has its own warrant. LS l.131's 'intended to threaten' rests on Asumi's hedged question and should read 'did not foresee the outcome (PRO p[0018]); Asumi conjectures an intent to threaten (C04 p[0601])'."
- **H-03** (KCMP-V06-001, side finding). CB1-CL-031. *Correction:* "The doctor's statement, as reported, backs Kume's prescription; the drugging of the champagne is Asumi's accusation, covered only by the epilogue's summary of full confessions."
- **H-04** (KCMP-V07-012, side finding). CB1-CL-042. *Correction:* "'His false account to the police' is conditional on Sayaka's uncorroborated report; status should be 'probable', not 'established'."
- **H-05** (KCMP-V06-004, side finding). `CB1_YAKUSHIJI_KUNIAKI_MONOGRAPH.md` l.194: "On their word he expelled 水谷 [p0618]" should cite p0444 (expulsion for the switch, informant unnamed) and keep p0618 for the stalker story only.

---

## 4. Counts

**By verdict.** CONFIRM 20; MODIFY 6 (KCMP-V06-005, V06-006, V07-007, V07-010, V07-011, V07-012); OVERTURN 0. The register was modified in 6 of 26 records (23%) and overturned in none. Of the modifications, two re-labelled an omission as compression (V06-005, V07-010), one removed a secondary interpretive disagreement (V06-006), one added an introduction error (V07-007), and two removed a GPT_ERROR label in favour of omission (V07-011, V07-012).

**By final primary disposition.**

| Disposition | Count | Records |
|---|---|---|
| `GPT_OMISSION` | 11 | V06-001, 006, 008, 010, 011; V07-003, 004, 006, 008, 011, 012 |
| `GPT_COMPRESSION` | 9 | V06-002, 003, 005, 007, 013, 014; V07-007, 009, 010 |
| `GPT_ERROR` | 3 | V06-009; V07-001, 002 |
| `CLAUDE_ERROR` | 2 | V06-004; V07-005 |
| `BOTH_INCOMPLETE` | 1 | V06-012 |
| Others | 0 | — |

Secondary dimensions: `GPT_OMISSION` in V06-002, V06-005, V07-010; `GPT_ERROR` in V07-007; `GPT_COMPRESSION` in V07-002 and V07-005; `INTERPRETIVE_DISAGREEMENT` in V07-005; source accuracy in V06-003; presentation in V07-011; misleading framing in V07-012.

**By priority.** P1: 4 (V06-009; V07-001, 002, 007). P2: 14 (V06-001, 002, 003, 005, 006, 007, 010, 011; V07-003, 004, 006, 008, 009, 012). P3: 6 (V06-008, 012, 013, 014; V07-010, 011). CB1-only: 2 (V06-004; V07-005, with a P3 GPT secondary).

---

## 5. Supplementary observations (outside the 26 records)

These came up while verifying the registers' agreement samples and context. They are recorded so an integrator does not lose them; they are not counted above.

1. **V06 agreement sample A7.** The GPT reading's "asks a witness to relate a cry to a regular news broadcast" overstates Asumi's prompting: she asked only the time (C01 p0812), and Shinagawa supplied the news anchor (p0814). EV-0003 is accurate. Folded into A-04. Suggested priority P1 by the brief's definition, trivial consequence.
2. **V06 agreement sample A8.** The GPT Motoya study's "His later recommendation to defer independent checks follows a resource judgment" misplaces the reason. Motoya argues the thin connection and claims the women's alibis are solid after only their self-reports (C01 p0599–0604; p0600 「自信のある声を出すしかなかった」); Masaki gives the manpower reason (p0605). The overstatement strengthens GPT's own theme of accommodating discretion. Folded into G-05. Suggested priority P1 (minor).
3. **V06 introduction "He".** The V06 introduction genders its prologue's わたし speaker ("He remembers Mitsuki"), the same synopsis choice as KCMP-V07-011. The speaker is male (Nonaka), so this is presentation only (P3).
4. **Eguchi's "slight acquaintance".** GPT EV-0005 records Eguchi's claim to have known Kawamura only slightly (C03 p0100) without noting that the extortion relationship belies it (C04 p0557, p0576). Folded into D-05.
5. **Sayaka's address switch.** Sayaka addresses Motoya as 吉川さん throughout V06 until the epilogue's provocative 元哉くん (EPI p0013), which triggers Asumi's 資格 challenge. Neither corpus remarks on the switch. Folded into E-03.
