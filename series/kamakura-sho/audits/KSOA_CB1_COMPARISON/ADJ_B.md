---
title: "Phase 4 discrepancy adjudication — Group B (V04 竹寺の雪, V05 西御門の館)"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CB1_ADJ_B
artifact_type: discrepancy_adjudication
generation: KSOA-CB1-COMPARISON
version: "1.0"
created: "2026-11-15"
status: canonical
scope: "Source-decided Phase 4 adjudication of the 30 KCMP-V04 and KCMP-V05 records, with integration actions grouped by destination type (a)-(h)."
source_boundary: "Seven Japanese publisher EPUB witnesses KSOA-JP-V01-W01 to KSOA-JP-V07-W01 (all narrative sections); GPT corpus KSOA-G1 at 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a; KSOA-CB1 blind package frozen 2026-11-15T10:52:54Z, manifest SHA-256 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040."
canonical_home: series/kamakura-sho/audits/KSOA_CB1_COMPARISON/ADJ_B.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
compared_generations: [KSOA-G1, KSOA-CB1]
gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
cb1_blind_package_manifest_sha256: 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040
source_record: "comparison/ADJ_B.md in the KSOA-CB1 comparison workspace (outside Git)"
source_record_sha256: f17ee5b8a965d06efa15a033887fc567e2c1ec9017f3d004d3b68a3fe77556b0
source_record_bytes: 95728
source_record_body_sha256: fb3764af140e19625b212fcfbd086acc7f9e4961dd519c87beadfed9531039cb
copy_transformations:
  - "post-copy custodian scrub (2026-11-15): 2 mentions of the local KSOA-CB1 working-folder name replaced with 'KSOA-CB1:' where followed by a slash or backslash, otherwise with 'KSOA-CB1'; no other body byte changed; reversing the substitution reproduces the copied body"
  - "post-copy normalization (2026-11-15): 11 whitespace-only lines reduced to empty lines for the repository whitespace check; Markdown rendering unchanged"
path_rewrites: []
integration_date: "2026-11-15"
integrated_by: INT-6
source_record_front_matter: |
  title: "Phase 4 discrepancy adjudication — Group B (V04 竹寺の雪, V05 西御門の館)"
  artifact_type: discrepancy_adjudication
  status: draft_noncurrent
  do_not_use_as_current_authority: true
  gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
  cb1_basis: "BLIND_PACKAGE_MANIFEST 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040"
  author_model: "Claude Opus 5.5 (claude-opus-5-5), Phase 4 independent adjudicator (Context B), Group B"
  created: "2026-11-15"
  adjudicated_registers: ["comparison/KCMP_V04_REGISTER.md", "comparison/KCMP_V05_REGISTER.md"]
  work_notes: "comparison/work/ADJ_B_notes.md"
---

# Phase 4 adjudication — Group B

This report adjudicates every record of `KCMP_V04_REGISTER.md` (KCMP-V04-001 to -016) and `KCMP_V05_REGISTER.md` (KCMP-V05-001 to -014) under `comparison/PHASE4_BRIEF.md` and the binding `comparison/COMPARISON_PROTOCOL.md` (§6 adjudication rule). Each decision rests on the Japanese witness in `KSOA-CB1:01_source/V04/` and `/V05/`. It does not rest on the register's quotations, on agreement between the corpora, or on either corpus's confidence.

**Basis and integrity.** The GPT repository was confirmed at `7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a` with a clean working tree (`git status --short` empty). Only read-only git commands were run. No file in `repository/` or `KSOA-CB1:` was modified.

**What was read.** The Phase 4 brief, protocol, Phase 3 brief, comparison basis and both registers were read in full. The GPT corpus files read in full were `readings/KSOA_V04_DEEP_READING.md`, `readings/KSOA_V04_READING_INTRODUCTION.md`, `readings/KSOA_V05_DEEP_READING.md` (body and coverage table) and `readings/KSOA_V05_READING_INTRODUCTION.md`. The headers and the `## V04` and `## V05` sections of the case, disclosure and character ledgers were also read. From the claim revision ledger, the V04, V05 and series sections were read. The study paragraphs cited below were read in context. In CB1, each cited line was checked in the reading, exit state, freezes, section notes, claim inventory, longitudinal synthesis and Shichijō monograph. Every source passage named below was retrieved from the witness extraction and read with its surrounding context. Beyond the registers' spans, the context read included V04 C01 p0300–0416, p0527–0582, p0774–0845; C02 p0078–0113, p0160–0254, p0288–0300, p0380–0443, p0504–0510, p0676–0766, p0930–1000; C03 p0350–0470, p0568–0590, p0756–0810, p0862–0926, p0955–1132; EPI p0054–0068; and the whole of V05 PRO, plus V05 C01 p0118–0230, p0509–0563, p0725–0747; C02 p0001–0012, p0228–0266, p0387–0462, p0636–0640, p0712–0895; C03 p0218–0226, p0306–0309, p0688–0756, p0896–0977.

**Locators.** `C03 p1104` means witness paragraph ordinal p[1104] of the section member. GPT range locators and CB1 `[Vnn SEC pNNNN]` locators resolve to the same ordinals. I confirmed this on three samples. GPT V04 EV-0002 `C01 0304–0338` contains the 20:17 call at p0330. GPT V04 RES-0002 `C03 1030–1126` contains the alibi at p1034, the key admission at p1108 and the accompaniment request at p1120. GPT V05 RES-0002 `C03 0947–0977` contains the arrest at p0962. Japanese is quoted only as short verified phrases.

**Vocabulary.** Verdicts are CONFIRM, MODIFY or OVERTURN, and they apply to the register's proposed disposition. Final dispositions use the protocol §5 vocabulary. Priorities follow the brief:
- **P1**: an error in current canonical GPT material, or a misleading claim graded too confidently;
- **P2**: a material omission or compression;
- **P3**: enrichment;
- **CB1-only**: a correction needed only on the CB1 side.

---

## 1. Adjudication table

| ID | Register disposition | Verdict | Final disposition | Priority | One-line rationale (locators) |
|---|---|---|---|---|---|
| KCMP-V04-001 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | At the reveal the text records all of the following: the keys, 「合鍵も含めて」, were kept in the drawing room (C03 p1040) in a dial-lock case (p1044); a copy taken from Yūko's key is put to Hachiya (p1104); he answers 「そうだよ、鍵は俺が渡した」 (p1108). No GPT artifact records any of it. |
| KCMP-V04-002 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | Akao learned of the secret marriage from a 住民票 obtained by the 行政書士 曽根昌雄, which Asumi calls probably illegal (C03 p1100). Police obtained the 謄本 lawfully by 職権 (p1066). Neither appears anywhere in GPT. |
| KCMP-V04-003 | INTERPRETIVE_DISAGREEMENT (+ GPT_OMISSION) | MODIFY | GPT_OMISSION; residual INTERPRETIVE_DISAGREEMENT on salience | P2 | The parentage arithmetic was reader-available by H-0008/H-0009 (C01 p0578; C02 p0098, p0111, p0219, p0235, p0435, p0441, p0966). D-0003's "not yet entitled to infer" is defensible as "not warranted to conclude". The defect is the missing availability record, not an error in D-0003. |
| KCMP-V04-004 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P2 | Before the reveal, Shichijō names 蜂屋貞一 as Yūko's sworn partner, 「誓い合った殿方」 (C03 p0799, p0803–0804). GPT carries this span only inside locator ranges, never in prose. |
| KCMP-V04-005 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P2 | Asumi singles out one thin diamond chain bracelet, names Van Cleef & Arpels and then stops at the poster (C01 p0534–0541). The bracelet is matched at C03 p0887–0889 and p0902. Prospectively, GPT records only "jewelry". |
| KCMP-V04-006 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P2 | The figures are ¥5m withdrawn on 31 March (C03 p0576–0578), a further ¥3m demanded and the decision to kill (p0920), about ¥600m of debt and an estate of over ¥800m (p1084), and a possible one-third share for Shichijō (p1089). GPT's wording is accurate but gives no figures. |
| KCMP-V04-007 | GPT_ERROR | CONFIRM | GPT_ERROR | P1 | The ruby reads え・ち・か (C01 p0150). "Kechika" appears 13 times in the frozen reading and in the unfrozen rows EV-0002, EV-0006, ADJ-0002 and REL-0003. |
| KCMP-V04-008 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | A whole-volume search finds only two おまえ tokens, from 佐竹 (C01 p0893) and 吉田 (C03 p0355). Asumi says キミ once (C01 p0029) and 元哉くん once (p0046). Shichijō shifts from 関川洋介さん to 洋介さん, and Miyazaki from わたし to 俺 (C03 p0568). GPT has no V04 VOICE rows. |
| KCMP-V04-009 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | Ages and residence facts verified: C02 p0032, p0043; C01 p0070, p0111, p0152, p0583; C02 p0025; C03 p0025, p0213; EPI p0074. None appears in GPT. |
| KCMP-V04-010 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | Torii's portrait of Akao: his work showed no love for Yōsuke (C01 p0784); he was fixated, 「異常にこだわって」, on mid-Shōwa-30s films (p0789); he haggled over royalties (p0833, p0837); he was divorced and his body was refused (p0841, p0843). Motoya: 「多少は金には汚い」 (p0646). |
| KCMP-V04-011 | BOTH_INCOMPLETE | CONFIRM (reasoning refined) | BOTH_INCOMPLETE | P2 | Miyazaki says he decided to kill, 「殺すことにした」, after the April demand (C03 p0920), yet his withheld account opens 「三月の末」 (p0972). Neither corpus weighs both passages. CB1-CL-020 also over-grades the incitement. |
| KCMP-V04-012 | BOTH_INCOMPLETE | CONFIRM | BOTH_INCOMPLETE (GPT_OMISSION; CLAUDE_ERROR) | P3; CB1-only | The Yūko address route, 「訊き出したらしい」, sits inside the later-retracted fraud story (C03 p0586). CB1's Shichijō monograph states the hidden visit as fact. |
| KCMP-V04-013 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P3 | Akao asked for the screening only after 6 pm (C01 p0311). Nothing through EPI p0137 explains how Miyazaki knew. |
| KCMP-V04-014 | GPT_ERROR | CONFIRM | GPT_ERROR | P1 | The interview ran in the drawing room 「四時から二時間くらい」 (C01 p0306). The screening began after 6 (p0311). Dinner began about 6:30 without Akao (p0320; C02 p0163). |
| KCMP-V04-015 | GPT_ERROR (+ INTERPRETIVE_DISAGREEMENT) | OVERTURN | AGREE | P3 (optional note) | Asumi stops the frame (「見つけた！」, 「このクルマ」) before any face check (C03 p0402–0406, p0422–0424). Motoya's 「たしかに…カーポートに駐まっていたな」 (p0409) confirms her find. GPT's attribution is supported. |
| KCMP-V04-016 | CLAUDE_COMPRESSION | MODIFY (scope extended) | CLAUDE_COMPRESSION + CLAUDE_ERROR | CB1-only | "Unmistakable" overstates the narration (p0441) against 「確定はできません」 (p0462). "Renounces" overstates 「明言したらしい」 (EPI p0056) and recurs in the exit state. CB1-CL-020 grades the alleged incitement "established". |
| KCMP-V05-001 | CLAUDE_OMISSION | CONFIRM | CLAUDE_OMISSION | CB1-only | In the prologue the blow is followed at once by the splash (PRO p0058–0064). Asumi says 「殴って倒し、その身体を海に放り込んで」 (C03 p0952). The examiner speaks of a fall, 「転落」 (C01 p0746). CB1 holds both versions and never flags the difference. |
| KCMP-V05-002 | GPT_OMISSION (+ GPT_COMPRESSION) | CONFIRM | GPT_OMISSION (+ GPT_COMPRESSION) | P2 | The 木刀 was brought 「脅すために」 (PRO p0045). The bag's contents went into the sea (p0075), at a place chosen for being deserted (p0074). Watanabe estimates 「木刀くらいの棒」 (C01 p0511). GPT never mentions the weapon or the bag. |
| KCMP-V05-003 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | Motoya judges the chance that Hani is the culprit 「皆無」 (C02 p0370) and his alibi unproblematic (p0397). He finds Yuka without suspicion (p0187–0188). |
| KCMP-V05-004 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P3 | The only boat talk before the reveal is attached to Tanaka (C02 p0461). Hani volunteers an over-specified alibi at an inn he partly designed (p0395). No boat is attached to Hani before C03 p0951. The hints are weak. |
| KCMP-V05-005 | GPT_OMISSION | CONFIRM | GPT_OMISSION (cause UNRESOLVED) | P2 | Asumi dates the marriage after the 2008 award (C03 p0943). Emiko (p0224), Yuka and Hani (C02 p0424–0428) and Emiri's hearsay (p0639) all place it earlier. |
| KCMP-V05-006 | INTERPRETIVE_DISAGREEMENT (+ minor CLAUDE_ERROR) | MODIFY | INTERPRETIVE_DISAGREEMENT | P3 | The author stages the parallel (C03 p0932). Asumi marks it as conjecture and Hani's viewpoint (p0943). CB1's "omitted" is literally true (C02 p0231), so there is no error, only a wording caution. |
| KCMP-V05-007 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | Asumi says あんた to Motoya seven times in C02 (p0712…p0894). Motoya's only おまえ to Asumi is at p0789. Hani's 僕 (C03 p0949) becomes 俺 (p0954), echoing the prologue (PRO p0028). |
| KCMP-V05-008 | GPT_COMPRESSION | CONFIRM | GPT_COMPRESSION | P2 | The story year 2023 follows from C03 p0224. The season is the rainy season (C03 p0779; EPI p0005). The weekdays run Monday to Thursday (C02 p0187; C03 p0012, p0595, p0782). The arrest is at 16:02 (p0962) and the wake at 18:30 (p0788). |
| KCMP-V05-009 | GPT_OMISSION | CONFIRM | GPT_OMISSION | P2 | Every sampled item verified: C01 p0647, p0683, p0725, p0739, p0745; C02 p0727; C03 p0107, p0150, p0512, p0591, p0617. |
| KCMP-V05-010 | CLAUDE_ERROR | CONFIRM | CLAUDE_ERROR | CB1-only | CB1-CL-026 grades "from a boat" as established, though the boat exists only in Asumi's speech (C03 p0951). CB1's own longitudinal synthesis calls V05's route probable. |
| KCMP-V05-011 | BOTH_INCOMPLETE | CONFIRM (evidence added) | BOTH_INCOMPLETE | P3 | On Tuesday Enomoto says 「わかりません」 (C03 p0724) and 「すべてを話しました」 (p0750). On Thursday he says 「犯人は若尾しかあり得ない」 and admits gathering evidence (p0918). |
| KCMP-V05-012 | GPT_ERROR | CONFIRM | GPT_ERROR | P1 | Yuka, not Hani, names the three (C02 p0414) and calls them Atobe-office colleagues (p0420). They attended different universities (C03 p0308). Four architects are present in C03 (p0784). |
| KCMP-V05-013 | GPT_OMISSION | MODIFY | GPT_COMPRESSION | P2 | GPT records the confidence request (H-0013) and an abstract cost to witnesses with alibis. It omits the promise 「もちろんです」 (C03 p0693), its public use (p0900) and the hypothetical insinuation (p0904–0908). "Bluff" is the wrong term; it was an insinuation. |
| KCMP-V05-014 | GPT_ERROR | CONFIRM | GPT_ERROR | P1 | Sayaka designed the interview (C01 p0134). Motoya's basic questions came from ignorance (p0137–0139, p0213). There is no apology to Motoya anywhere; the only apology is at C03 p0973. |

---

## 2. Full adjudication entries

Full entries are given for every P1 or P2 record, every INTERPRETIVE_DISAGREEMENT, every MODIFY or OVERTURN, and every record with a CLAUDE_ERROR dimension: 26 records. The remaining four records (V04-013, V05-001, V05-004, V05-011) have short entries at the end of each volume. Steps follow the brief:
1. passage;
2. speaker, focalizer, chronology and disclosure;
3. what the text establishes and what is inferred;
4. strongest competing explanation;
5. verdict and final disposition;
6. residual uncertainty;
7. implications;
8. priority;
9. integration action.

The proposed wording for each action is in §3.

### V04 竹寺の雪

#### KCMP-V04-001 — Key custody and provenance

1. **Passage.** C03 p1035–1054 and p1104–1109; C03 p0956–0974; C01 p0354–0367 and p0408–0414.
2. **Context.** The reveal takes place in the Sekigawa drawing room on the Tuesday, narrated through Motoya. Asumi speaks, Echika objects and Hachiya answers. Disclosure is at KSOA-V04-H-0014. The copying took place at an unspecified earlier time, 「過去に」 (p1104). Earlier, Asumi had already suggested a key borrowed and copied from someone in the household (p0964), and Miyazaki fell silent.
3. **Established and inferred.** Established: Asumi cites forensic and other circumstances to say that Miyazaki entered with a duplicate (p1038). Echika says the keys, 「合鍵も含めて」, were kept in that room (p1040), in a 「ダイヤルロックのキーケース」 (p1044); compare the small key case at C01 p0362. Asumi asserts that a copy was used (p1042), obtained from an accomplice (p1046, p1054). She puts it to Hachiya that he had borrowed and copied Yūko's key (「由布子さんから借りてコピー」, p1104). He answers 「そうだよ、鍵は俺が渡した」 (p1108). Inferred: the copy's origin in Yūko's key rests on Asumi's account. Hachiya's 「そうだよ」 is an **explicit affirmative** to 「違いますか？」, not the "tacit assent" the register describes, but he itemizes only the handover.
4. **Strongest competing explanation.** Hachiya's assent may cover only the handover, with the duplicate made by another route, for example from the sideboard set during his frequent visits (C02 p0401–0404). No text supports a different route, and Miyazaki's own account is cut (C03 p0972→p0974).
5. **Verdict.** CONFIRM. **Final:** `GPT_OMISSION` (fact; evidence coverage). GPT KSOA-V04-EV-0003 ("without demonstrating custody of all copies"), EV-0014 and CL-0003-R02 stop at the "admitted transfer".
6. **Residual uncertainty.** The scope of 「そうだよ」, the date of copying, and whether Yūko knew.
7. **Implications.**
   - GPT: EV-0003's open question now has an endpoint answer. The CL-0003 chain needs a provenance revision: R01 left access unresolved, and R02 stops at the admitted transfer.
   - RES-0002, the V04 example in SER-CL-0001, and the "key gap" sentence in the mystery study all depend on this point.
   - CB1 already has it (exit state §2 K-01), so it needs no change.
8. **Priority.** P2.
9. **Integration.** (c) new KSOA-V04-EV-0015; (f) KSOA-V04-CL-0003-R03; (a) erratum ERR-V04-02.

#### KCMP-V04-002 — Akao's knowledge of the marriage through a 住民票

1. **Passage.** C03 p1066, p1075–1079, p1100.
2. **Context.** Asumi reports, at the restricted meeting (H-0014), findings made during the off-page day of inquiry (C03 p0985–0987).
3. **Established and inferred.** Established: police viewed the 戸籍謄本 at Kamakura city hall by 「職権」 (p1066). It shows a marriage 「およそ一ヶ月半前」, with Hachiya as head of the new register (p1079). Akao knew of the marriage from a 住民票 obtained under 「職務上の権限」 by the 行政書士 曽根昌雄 at Akao's request, an act Asumi calls 「違法と思われます」 (p1100). Inferred: that Sone's act was illegal is Asumi's characterization, and his conduct is not shown.
4. **Strongest competing explanation.** None that defeats the fact. Its status is a detective's report of verified records, not a scene.
5. **Verdict.** CONFIRM. **Final:** `GPT_OMISSION`. A search of the whole GPT corpus for 曽根, scrivener, 住民票 and residence certificate found nothing. GPT has only "a theory that Akao threatened Hachiya separately" (H-0014).
6. **Residual uncertainty.** Sone's legal exposure and how Akao knew him.
7. **Implications.** It completes the knowledge chain of KSOA-V04-CASE-0002. It pairs lawful 職権 access with unlawful access through a professional, which bears on the policing study's account of access and authority and on CB1 LS §5.5.
8. **Priority.** P2.
9. **Integration.** (c) new KSOA-V04-EV-0016, linked to CASE-0002; (d) new KSOA-V04-K-0004; (g) policing study.

#### KCMP-V04-003 — Reader-side availability of Yūko's parentage before C03

1. **Passage.** C01 p0578; C02 p0093–0098, p0107, p0111, p0219, p0235, p0252, p0431–0441, p0930, p0936, p0966, p0989; C03 p0188, p0704–0731.
2. **Context.** These are witness accounts in C02 (Hongō, Hachiya, Echika, Utsunomiya), narrated through Motoya.
   - No character voices the parentage link before Shichijō's own statement (C03 p0704). Motoya's 「関川洋介の実の娘だ」 (C02 p0299) concerns Yūko's relation to Yōsuke only.
   - GPT D-0003 sits at H-0008 (C02 p0781). Utsunomiya's depression report (p0966) and her concrete description of the first wife (p0936) fall later, at H-0009.
3. **Established and inferred.** By H-0008 the reader has these facts:
   - the film was made 「六二年前」, in 1961 (C01 p0578; C02 p0219), which gives a 2023 present;
   - Yūko is 61 (C02 p0111), so she was born in 1961 or 1962;
   - Shichijō vanished without telling anyone (p0235);
   - Yūko's mother died within a year of the birth, and Hongō never met her (p0098);
   - Yūko took a 「乳母役の女性」 for her mother (p0441).

   By H-0009 the reader also hears, at second hand, that Yōsuke was deeply depressed after Shichijō vanished (p0966). The convergence on Shichijō's maternity is an analyst's hypothesis and nothing more. CB1 froze it as H-12 at moderate confidence (`CB1_V04_FREEZES.md`, l.205).
4. **Strongest competing explanation.** The facts are equally compatible with an ordinary early death of the first wife. Two witnesses deny any affair (C02 p0252, p0936), and Utsunomiya describes the first wife concretely, with pearls from a location shoot (p0936). Read as "not warranted to conclude", D-0003's "not yet entitled to infer her maternity" is correct at H-0008.
5. **Verdict.** MODIFY. The register makes interpretive disagreement the primary disposition. On my reading the two corpora do not actually contradict each other. GPT says a conclusion was not warranted, and CB1 says a hypothesis was available. The substantive defect is that GPT never records that a parentage hypothesis was available, prospectively or in retrospect, although the disclosure-ledger schema requires that "whether each decisive clue was available, salient or obscured" be recorded. **Final:** `GPT_OMISSION` (detectability record), with a residual `INTERPRETIVE_DISAGREEMENT` about salience only. H-0007's "without resolving the film's clue" remains true. The mystery study's sentence that the bracelet-to-parentage link "depends on testimony disclosed late" is true of the bracelet route, but it is incomplete as an account of detectability.
6. **Residual uncertainty.** How salient the convergence is to an ordinary reader. CB1 itself rates it "moderate: arithmetic spread across three interviews".
7. **Implications.**
   - The V04 row of GPT's mystery study (`#what-a-reader-can-infer-before-the-solution`) is affected, and so is KSOA-SER-CL-0002, whose V04 support is the "selective view" alone.
   - The frozen D-0003 is not altered.
   - CB1 H-12 is confirmed at C03 p0704 and needs no change.
8. **Priority.** P2.
9. **Integration.** (d) new retrospective KSOA-V04-ADJ-0003; (g) the mystery study's V04 row; (f) optional KSOA-SER-CL-0002-R01 (STRENGTHEN).

#### KCMP-V04-004 — Shichijō names Hachiya as Yūko's sworn partner before the reveal

1. **Passage.** C03 p0789–0807; C02 p0399–0404; C01 p0211; C03 p0996.
2. **Context.** Shichijō speaks to the detectives at the station (H-0013). The narration through Motoya adds 「たしか…独身で通してきたはず」 (p0800) and 「だから見舞いにも来ていたのか」 (p0804).
3. **Established and inferred.** Established: Yūko had 「晩年をともに生きることを誓い合った殿方」 (p0799), named as 蜂屋貞一 (p0803). This is set against Echika's statement that her aunt is single (C01 p0211) and Hachiya's account of seven years of friendship and frequent visits (C02 p0401–0404). Hachiya is then present at the restricted meeting (C03 p0996). Inferred: that the vow points toward a marriage and an inheritance motive is a reader's inference.
4. **Strongest competing explanation.** A vow is not a legal marriage. The register, the debts and the 住民票 appear only at the reveal (p1066–1100). GPT's "withheld bridge" and CB1's "not fair-play in the strict sense" both survive.
5. **Verdict.** CONFIRM. **Final:** `GPT_COMPRESSION`. The span appears in GPT only inside the locator ranges of H-0013 ("C03 0652–0823") and REL-0004 ("C03 0793–0807"). GPT's prose never states it.
6. **Residual uncertainty.** How far the vow narrows the facilitator for a reader.
7. **Implications.** The detectability sentence in GPT H-0014 ("restricts how precisely a reader could solve the lock and role problem") stays true, but it understates what was available. REL-0004 is affected.
8. **Priority.** P2.
9. **Integration.** (d) new KSOA-V04-D-0006; (a) erratum ERR-V04-03 (H-0014 "Institution and form").

#### KCMP-V04-005 — Asumi's identification of the bracelet as a reader-side clue

1. **Passage.** PRO p0034–0041; C01 p0529–0552; C03 p0880–0913.
2. **Context.** Asumi speaks in the memorial exhibition room (H-0004). Motoya's narration adds that the bracelet is very thin for a man's piece (p0540). The juxtaposition with the poster follows immediately (p0541–0551). In C03, Motoya's narration recalls her remark (p0888).
3. **Established and inferred.** Established:
   - In Yōsuke's 「プライベート写真」 Asumi singles out one bracelet, 「たぶん《ヴァンクリーフ＆アーペル》」, white gold or platinum, with a diamond (p0534, p0538).
   - She then stops at the 『竹寺の雪』 poster (p0541).
   - Miyazaki later names Yōsuke's platinum chain bracelet. Asked about the Van Cleef piece, he answers 「たぶんそれだ」 (C03 p0885–0889), and says it is on 「晶子さまの左腕」 in the film (p0902).

   Inferred: a reader can link the prologue's wrist to the bracelet before C03, by juxtaposition only. No character makes that link before p0902.
4. **Strongest competing explanation.** GPT does record that the novel later "connects it to the earlier display photographs" (`#a-visible-secret-an-invisible-route`), so the link is captured in retrospect. What is missing is its prospective availability and the specificity of Asumi's expertise.
5. **Verdict.** CONFIRM. **Final:** `GPT_COMPRESSION`. In GPT, H-0004 has "notices jewelry", and EV-0004's prose covers only the prologue, the disc and Torii, although its range includes C01 0511–0557.
6. **Residual uncertainty.** The register's claim that this is the "fairest in the series" is a cross-volume judgment and is not adjudicated here.
7. **Implications.** The V04 detectability account in the reading and the mystery study is affected. It also adds evidence of material expertise to GPT's Asumi study (`#from-noticing-a-difference-to-making-it-testable`) and KSOA-SER-CL-0003. The CL-0001 chain gains reader-side support.
8. **Priority.** P2.
9. **Integration.** (c) new KSOA-V04-EV-0018; (f) KSOA-V04-CL-0001-R03 (STRENGTHEN); (a) erratum ERR-V04-04; (g) Asumi study and mystery study.

#### KCMP-V04-006 — Sums, debt, estate and the one-third mechanism

1. **Passage.** C03 p0572–0580, p0760, p0916–0920, p1079, p1084, p1089, p1114.
2. **Context.** Motoya reads the passbook (p0576–0578). The rest comes from Miyazaki's confession and Asumi's reveal.
3. **Established and inferred.**
   - Established by the passbook: ¥5m was withdrawn at the counter of the Kamakura branch on 31 March (p0576–0578).
   - Miyazaki's statement: he paid ¥5m and, after a further ¥3m was demanded in April, decided to kill (p0920).
   - Asumi's reported verification: Hachiya's debt is about ¥600m and the estate is over ¥800m (p1084).
   - Asumi's legal claim within the fiction: if a family court corrected the register, a third of the estate could pass to Shichijō (p1089).
   - Shichijō will never declare her maternity (p1114).
4. **Strongest competing explanation.** GPT's qualitative wording ("a large withdrawal", "substantial debts", "possible implications of corrected maternity") is accurate. The issue is compression, not error.
5. **Verdict.** CONFIRM. **Final:** `GPT_COMPRESSION`.
6. **Residual uncertainty.** The debt and estate figures are reported findings, not shown documents.
7. **Implications.** GPT EV-0011, EV-0013, EV-0014 and RES-0002 are affected, and so is the motive structure of CL-0003-R02.
8. **Priority.** P2. Without the figures, detailed motive questions cannot be answered.
9. **Integration.** (c) new KSOA-V04-EV-0017.

#### KCMP-V04-007 — The heir's name: 恵智花 is Echika, not "Kechika"

1. **Passage.** C01 p0150 (ruby ｜恵《え》｜智《ち》｜花《か》); p0152.
2. **Context.** Haga Takayo names her as Yūko's niece.
3. **Established and inferred.** The reading えちか is established by ruby. "Kechika" has no textual basis.
4. **Strongest competing explanation.** None.
5. **Verdict.** CONFIRM. **Final:** `GPT_ERROR`. I verified the counts: 13 occurrences on 10 lines of the frozen reading (H-0002, H-0003, H-0006, H-0007, H-0014, H-0015). In the unfrozen ledgers it appears once each in KSOA-V04-EV-0002, EV-0006, ADJ-0002 and REL-0003. The introduction and the producer review already flag the error, but the ledgers were never amended.
6. **Residual uncertainty.** None.
7. **Implications.** Retrieval of the correct name fails in canonical rows. The introduction's parenthesis can stay as a pointer to the reading erratum.
8. **Priority.** P1.
9. **Integration.** (c), (d), (e) correction notes; (a) erratum ERR-V04-01; (b) introduction pointer (optional).

#### KCMP-V04-008 — V04 address and register data

1. **Passage.** All of V04 searched for おまえ, お前, キミ, 元哉くん, 吉川くん, あんた and わたくし. In context: C01 p0029, p0046, p0893; C02 p0035, p0529, p0575, p0581, p0678–0760, p1048; C03 p0355, p0501–0568, p0704–0731, p0845.
2. **Context.** Direct speech with identified speakers. Every token was checked in its own line.
3. **Established and inferred.**
   - The only おまえ tokens are 佐竹's 「おまえたち」 (C01 p0893) and 吉田's 「おまえは」 (C03 p0355); お前 does not occur. Motoya therefore never says おまえ to Asumi in V04.
   - Asumi says 「キミは」 once (C01 p0029) and 「元哉くん」 once (p0046), and introduces herself with わたくし (C02 p0581, p0591, p1048).
   - Motoya calls Asumi 「こいつ」 in front of Hongō (C02 p0035).
   - Miyazaki uses わたし (C02 p0529; C03 p0501, p0519, p0558), then 俺 from 「あいつは俺を騙した」 (C03 p0568), and calls Asumi 「あんた」 (p0845).
   - Shichijō says 関川洋介さん while concealing (C02 p0678, p0698, p0756) and 洋介さん after confessing (C03 p0710, p0716, p0731).
   - A nuance missing from both corpora: Asumi herself mostly uses 関川洋介さん in that interview (C02 p0711, p0720, p0754, p0758) and 洋介さん only once (p0680). Shichijō's shift partly tracks her interlocutor's usage, and it still marks a real change.

   Inferred: what the absence of おまえ means is a cross-volume question, assigned to the CHAR task.
4. **Strongest competing explanation.** None for the V04 facts.
5. **Verdict.** CONFIRM. **Final:** `GPT_OMISSION`. The V04 ledger section has no VOICE rows, and the GPT Asumi study uses V04 only for the exchange about rank.
6. **Residual uncertainty.** Cross-volume comparison is outside Group B.
7. **Implications.** GPT's character ledger, the Asumi and Motoya studies (register sections) and the readiness audit are affected. Coordinate with the CHAR adjudication, which may propose overlapping VOICE rows.
8. **Priority.** P2.
9. **Integration.** (e) new KSOA-V04-VOICE-0001 to -0004; (g) the register sections of the Asumi and Motoya studies.

#### KCMP-V04-009 — Identity facts, ages and residence

1. **Passage.** C01 p0070, p0111, p0152, p0583; C02 p0025, p0032, p0043, p0390–0394; C03 p0025, p0213; EPI p0074.
2. **Context.** Narration and statements by witnesses or the detectives. Hachiya's age is Motoya's estimate (C02 p0394).
3. **Established and inferred.**
   - Asumi is 「二九歳」 (C02 p0032). She came to 鎌倉署 from 本部 「一年ちょっと」 earlier (C01 p0070), lives in Kamakura and sleeps at home during the joint HQ (C03 p0025).
   - Motoya: 「三一歳になります」 (C02 p0043). He goes home to Yokohama (EPI p0074).
   - Akao is 38 (C01 p0111), Echika 21 (p0152), Shichijō 88 (p0583), Hongō 84 (C02 p0025) and Yūko 61 (p0111).
   - Hachiya is 「五〇代なかば」, Motoya's estimate (p0394). Miyazaki was 17 when he met Shichijō (C03 p0213).
4. **Strongest competing explanation.** None material.
5. **Verdict.** CONFIRM. **Final:** `GPT_OMISSION`. A search of the whole corpus for 歳, "years old", "-year-old" and digit-age patterns found no character age.
6. **Residual uncertainty.** None.
7. **Implications.** GPT's character ledger and the lead studies are affected, and the V04 chronology gains the 2023 anchor.
8. **Priority.** P2.
9. **Integration.** (e) new KSOA-V04-STATE-0001 and PERSON rows; (g) the lead studies.

#### KCMP-V04-010 — The victim's portrait and early pointers to money and period

1. **Passage.** C01 p0644–0647, p0778–0792, p0831–0845.
2. **Context.** Torii's testimony to the pair (H-0005), with Motoya's reading of Torii's coolness (p0780–0781). Motoya's own remark is at p0646.
3. **Established and inferred.**
   - Torii: Akao did not seem to love Yōsuke (p0784) and was 「昭和三〇年代の中頃の作品に異常にこだわって」 (p0789).
   - He pressed for even one percent more royalty (p0833) and was reputed to haggle over fees (p0837).
   - He was divorced, his son was with his ex-wife (p0841), and the family refused the body (p0843).
   - Motoya: 「多少は金には汚い」, with no money trouble found that could lead to murder (p0646).

   Inferred: that these are clues pointing to blackmail and to 1961 is the analyst's reading.
4. **Strongest competing explanation.** Torii is not warm toward Akao, and the reputation is hearsay. The pointers suggest but do not discriminate.
5. **Verdict.** CONFIRM. **Final:** `GPT_OMISSION`. GPT has only "conventional" (H-0005).
6. **Residual uncertainty.** How strongly a reader would weigh the fixation.
7. **Implications.** GPT's V04 detectability account is affected, as is any PERSON row for the victim.
8. **Priority.** P2. The pointers to money and period bear on the extortion solution, and the rest is enrichment.
9. **Integration.** (c) new KSOA-V04-EV-0019; (e) PERSON row for Akao.

#### KCMP-V04-011 — Causal weight of the alleged incitement

1. **Passage.** C03 p0914–0926, p0956–0987, p1104–1109, p1120.
2. **Context.**
   - Miyazaki's confession in the interview room (H-0013).
   - His account given in answer to 「その人物の名を答えてください」 (p0968) opens 「あれは、三月の末だった……。そう、桜が咲いている頃だ……」 (p0972) and is cut (p0974).
   - At the reveal Asumi says she obtained Hachiya's involvement from Miyazaki (p1104).
3. **Established and inferred.** Established:
   - Miyazaki paid ¥5m and, at the April demand for ¥3m, 「殺すことにした」 (p0920).
   - Asumi alleges that Hachiya incited him 「晶子さんの名誉を守るため」 (p1104).
   - Hachiya affirms the key handover (p1108).
   - Police hold him on suspicion of 「殺人教唆及び幇助」 (p1120).

   Inferred: what follows for timing from 「三月の末」. The account opens before the April decision, but it may date Akao's first approach rather than Hachiya's. The first demand came before 31 March, and cherry-blossom time also roughly coincides with the marriage about six weeks before the reveal (p1079).
4. **Strongest competing explanation.** Miyazaki's own framing (p0920, p0949) may minimize another person's influence, or the withheld account may concern only the key.
5. **Verdict.** CONFIRM, with refined reasoning. **Final:** `BOTH_INCOMPLETE`.
   - GPT keeps the allegation at the correct status ("Instigation remains the represented investigative theory", CL-0003-R02), but it never engages Miyazaki's own decision statement.
   - CB1 READING §N.3 and LS l.142 call the incitement's weight "doubtful" without weighing p0972. CB1-CL-020 grades "蜂屋 supplied a duplicate key and incited him, for money" as `established`, which is inconsistent with that doubt; the status error is recorded under V04-016.
6. **Residual uncertainty.** The text supports neither "the incitement was decisive" nor "it added only the key".
7. **Implications.** GPT CL-0003-R02, RES-0002, the V04 example in SER-CL-0001, and the mystery study's `#direct-action-enabling-action-and-knowledge` ("Asumi's account of the full inducement has more dependencies") are affected.
8. **Priority.** P2.
9. **Integration.** (f) KSOA-V04-CL-0003-R04 (OPEN); (c) a note on RES-0002's unresolved questions; (g) one sentence in the mystery study; (h) CB1 note.

#### KCMP-V04-012 — The Yūko address route and the status of Akao's visit

1. **Passage.** C02 p0715–0719, p0762–0764, p0979; C03 p0584–0588, p0875–0920.
2. **Context.**
   - Day 2: Shichijō denies any visit, 「ここの住所は知らないでしょうから」 (C02 p0717), and Motoya feels she is not lying (p0719).
   - Day 3: in his fraud story, Miyazaki says Akao called while Shichijō and 紀江 were at hospital and had got the address from Yūko, 「訊き出したらしい」 (C03 p0586).
   - The revised account replaces the investment story with extortion (p0877) and is silent about the visit.
3. **Established and inferred.** Established: Miyazaki gives a hedged report of the Yūko route inside a cover story. Shichijō had passed her address to a few people after meeting Utsunomiya (C02 p0764), and Utsunomiya passed it to the Sekigawa family (p0979). Inferred: that the visit took place.
4. **Strongest competing explanation.** The visit may belong to the retracted cover. Even so, the Yūko route fits the address's documented circulation.
5. **Verdict.** CONFIRM. **Final:** `BOTH_INCOMPLETE`, with two diagnostic dimensions:
   - a GPT_OMISSION of the Yūko route (GPT H-0012 records the visit as alleged);
   - a CLAUDE_ERROR of status. `CB1_SHICHIJO_AKIKO_MONOGRAPH.md` l.65 states the visit as fact ("宮崎 sent him away and did not tell her"), and l.116 says she "was not [lying]; 宮崎 had hidden the visit", both resting on a detail from the retracted story. CB1's exit state row 19 and F-05 H-21 hedge it correctly.
6. **Residual uncertainty.** Whether the visit happened.
7. **Implications.** GPT EV-0011 and EV-0007 are affected. In CB1, the Shichijō monograph's "What she did not know" and "Mistakes" sections are affected; CB1 is frozen.
8. **Priority.** P3 for GPT; CB1-only for the monograph.
9. **Integration.** (d) KSOA-V04-K-0005; (h) CB1 correction.

#### KCMP-V04-013 — How Miyazaki knew Akao would be in the screening room (short entry)

C01 p0306 and p0311: Akao decided to watch the film 「六時過ぎに」, after the 4–6 pm interview. The dinner arose from an invitation made at the hospital the previous week (C02 p0082). Nothing after C03 p0988 or in EPI explains how Miyazaki knew; the off-page inquiry is a single sentence (C03 p0987). The answer may lie in the withheld account (p0972–0974). **CONFIRM**, `GPT_OMISSION` (analytical open question). **P3.** Integration: (c) a note on RES-0002's unresolved questions.

#### KCMP-V04-014 — The introduction places the Hongō interview at dinner

1. **Passage.** C01 p0301–0320; C02 p0078–0082, p0160–0166.
2. **Context.** Echika's chronology (H-0003), confirmed by Hongō (C02 p0163) and by the recorded call (C01 p0316–0317).
3. **Established and inferred.** The interview took place in the drawing room, 「四時から二時間くらい」 (p0306). Akao moved to the screening room after 6 (p0311). Hongō and Echika dined from 「六時半頃」 (p0320), without Akao. 「インタビューの後にお食事」 is confirmed (C02 p0163). Nothing here is inferred.
4. **Strongest competing explanation.** None. The frozen deep reading's H-0003 ("interviewed director Hongō, then requested") is correct.
5. **Verdict.** CONFIRM. **Final:** `GPT_ERROR`, confined to the introduction.
6. **Residual uncertainty.** None.
7. **Implications.** Only the introduction's synopsis (`#3-current-volume-story-synopsis`, paragraph 2).
8. **Priority.** P1. The introduction is current `active_provisional` material.
9. **Integration.** (b) targeted edit.

#### KCMP-V04-015 — Who matched the car to Shichijō's carport (OVERTURN)

1. **Passage.** C03 p0362–0393, p0394–0470; C02 p0508.
2. **Context.**
   - Asumi proposes treating Miyazaki as a key person and rechecking the footage (p0362, p0376), and 佐竹 approves (p0378–0380).
   - Narrated through Motoya: Asumi stops and rewinds a frame, 「見つけた！」 and 「このクルマ。ナンバーは読み取れないけど」 (p0401–0406).
   - Only then is the driver examined (p0422–0424).
3. **Established and inferred.**
   - Established: Asumi singled out "this car" in a search aimed at Miyazaki. Motoya replies 「銀色のアルト……。たしかに七条邸のカーポートに駐まっていたな」 (p0409). He proposes the opposite direction (p0426). Asumi reports the same-model match to 佐竹 (p0462).
   - Inferred: Asumi's recognition. It is left implicit, but her stop on the car itself, before any face check, together with Motoya's confirming 「たしかに」, makes recognition the natural reading.
4. **Strongest competing explanation.** The register's reading: Asumi stopped on the car for some other reason and the carport match is Motoya's alone. This is weaker, because her 「見つけた」 names the car as the object of the search, and 「たしかに」 marks agreement, not discovery.
5. **Verdict.** OVERTURN. **Final:** `AGREE`. GPT's "亜澄 recognizes a car matching one at 晶子's house, and 元哉 proposes looking for a clearer return direction" (`#how-the-two-roles-fit`) is source-supported, and so is the Asumi study's sentence. GPT omits that Motoya verbalizes the model and confirms the match, an optional enrichment.
6. **Residual uncertainty.** Whether Asumi recognized the Alto specifically or simply a car from the Shichijō household.
7. **Implications.** None for GPT. The argument for Motoya's independent contributions rests securely on p0426 and p0473.
8. **Priority.** P3, optional.
9. **Integration.** Optional (c) note on EV-0010. No erratum.

#### KCMP-V04-016 — CB1 status flattening (MODIFY: scope extended)

1. **Passage.**
   - Source: C03 p0441, p0462, p0470; C03 p0916; EPI p0056–0059; C03 p1104, p1108, p1120.
   - CB1: `CB1_V04_READING.md` l.51 and l.55; `CB1_V04_EXIT_STATE.md` l.57, l.66, l.83; `CB1_CLAIM_AND_UNCERTAINTY_INVENTORY.md` l.102 (CB1-CL-020).
2. **Context.**
   - p0441 (「特徴的なわし鼻は宮崎隆之に間違いない」) is narration focalized through Motoya.
   - At p0462 Asumi tells 佐竹 「確定はできません」, and a 科捜研 comparison is ordered (p0470).
   - p0916 is Miyazaki's 「調べまわったらしい」.
   - EPI p0056 is Motoya's hearsay, 「相続放棄をすることを明言したらしいな」.
3. **Established and inferred.** Established: the driver identification is Motoya's perception, not an institutional finding. Hachiya reportedly **declared** that he would renounce the inheritance. Instigation is an allegation, the stated ground of suspicion, and Hachiya's explicit affirmative covers only the key. Inferred: none of these as settled facts.
4. **Strongest competing explanation.** The CB1 summaries are labelled synopses and its row-level classes are mostly correct. Hachiya's 「そうだよ」 could be read as assent to Asumi's whole accusation.
5. **Verdict.** MODIFY. The register says CB1's exit state is "more careful". That holds only at l.57 ("declared he will renounce"); l.66 and l.83 repeat "renounces". The register also misses CB1-CL-020, which grades the alleged incitement `established`. **Final:** `CLAUDE_COMPRESSION` for the summary prose, plus `CLAUDE_ERROR` for the status label of CB1-CL-020.
6. **Residual uncertainty.** The scope of 「そうだよ」.
7. **Implications.** None for GPT. GPT's status wording (H-0011, H-0015, CL-0003-R02) should govern any canonical row built from CB1 material.
8. **Priority.** CB1-only.
9. **Integration.** (h).

### V05 西御門の館

#### KCMP-V05-001 — Fall in the prologue against "thrown into the sea" (short entry)

The prologue (reader-only, narrated in the first person) runs: blow (PRO p0058), last cry, then at once 「バシャーンという水音」 (p0064), 「しまった！」 (p0065) and 「こんなつもりじゃなかった」 (p0068). No act of throwing intervenes. Asumi's reconstruction places the talk on a boat, 「鎌倉沖で話し合い」, and asserts 「殴って倒し、その身体を海に放り込んで」 (C03 p0952). The examiner's opinion is a fall, 「海中に転落し溺死」 (C01 p0746), and Watanabe agrees (p0526). The arrest is for 傷害致死 (C03 p0962), while Motoya expects a murder charge on grounds of planning (p0966). CB1 reports Asumi's version (READING l.53), adopts the prologue's version (exit state row 26), and in its section notes (l.428) says "the boat explains … the splash". It never flags the difference. GPT flags it (H-0014 "Adjudication"; CL-0001-R01). **CONFIRM**, `CLAUDE_OMISSION`. **CB1-only.** Optionally (P3), add the two verified quotations to GPT EV-0012.

#### KCMP-V05-002 — Reader-only weapon and bag

1. **Passage.** PRO p0043–0082; C01 p0509–0512, p0526, p0554, p0563.
2. **Context.** The prologue is first-person and reader-only (H-0001). Watanabe's estimate (C01 p0511) is an investigator's statement at the scene, and no investigator mentions the weapon or the bag again.
3. **Established and inferred.** Established:
   - 「俺の右手には若尾を脅すために持ってきた木刀がある」 (PRO p0045), and the blow with it (p0058);
   - the narrator chose a place where nobody would be, 「誰もいない場所を選んだ」 (p0074);
   - 「若尾のバッグの中身も海に投じた」 (p0075);
   - 「目的は達せられなかった」 (p0082);
   - Watanabe: a wound like one from 「木刀くらいの棒で背後から」 (C01 p0511);
   - the wallet, licence and phone survived in zipped parka pockets (p0554, p0563).

   Inferred: that the investigators never recover the bag's contents. Its fate is simply untold.
4. **Strongest competing explanation.** GPT's abstract wording ("claim of intending intimidation", H-0001) keeps the inferential point without the objects. GPT's "disposition of belongings … remain open in the final text" (`#a-single-assault-amid-several-projects-of-redress`) can be read as "unverified by the investigation", but as written it blurs what the prologue establishes.
5. **Verdict.** CONFIRM. **Final:** `GPT_OMISSION`, with a `GPT_COMPRESSION` dimension for the sentence on the disposition of belongings.
6. **Residual uncertainty.** The bag's contents and the bag itself.
7. **Implications.** GPT EV-0001, EV-0012, K-0001 and the reader-side detectability account are affected. Watanabe's estimate is the strongest link from the prologue to the body.
8. **Priority.** P2.
9. **Integration.** (c) new KSOA-V05-EV-0013 and an amendment note on EV-0001; (d) new KSOA-V05-K-0003; (a) erratum ERR-V05-02.

#### KCMP-V05-003 — The focalizer rules Hani out

1. **Passage.** C02 p0187–0188, p0370, p0395–0397; C03 p0403, p0567.
2. **Context.** These are Motoya's own judgments, in narration and speech. He is the only consciousness the reader shares.
3. **Established and inferred.** Established:
   - 「羽仁が被疑者である可能性は皆無だと、元哉には感じられた」 (C02 p0370);
   - 「羽仁のアリバイも問題がなさそうだ」 (p0397);
   - on Yuka, 「アリバイは完璧」 and 「疑わしいところは少しも感じられない」 (p0187–0188);
   - on Kodera, 「真実を語っている」 (C03 p0567).

   Inferred: that the novel uses Motoya's judgment to misdirect. This is a structural reading, strongly supported.
4. **Strongest competing explanation.** His record is mixed, not uniformly wrong: he was right about Tanaka and Kodera. The point is Motoya's fallibility, not a rule of misdirection.
5. **Verdict.** CONFIRM. **Final:** `GPT_OMISSION`. GPT's own H-0011 entertains Tanaka as "a plausible prologue voice" but never records Motoya's exclusion of Hani.
6. **Residual uncertainty.** How much weight a reader gives his impressions.
7. **Implications.** GPT's V05 detectability paragraph, the mystery study's V05 row, and the Motoya study's account of his judgment (`#a-focalizer-with-a-job-of-his-own`) are affected.
8. **Priority.** P2.
9. **Integration.** (d) new KSOA-V05-K-0004 and KSOA-V05-ADJ-0004; (e) new KSOA-V05-STATE-0001; (g) Motoya study and mystery study.

#### KCMP-V05-004 — Clue inventory for the boat (short entry)

- The only boat talk among the suspects before the reveal is Hani's anecdote about Tanaka at the housewarming, 「田中は船を出すって騒いでた」 (C02 p0461). It misdirects.
- Hani volunteers a complete alibi unasked (「完璧ですよ」, check-in and check-out times, room service at 10). He adds that he had worked on part of the design of the inn (「一部の設計に携わったことがある宿」, p0395).
- Local maritime history and the marinas appear at C01 p0465–0467 and p0536.
- Asumi's remark that Hani and Hatano were the first to rush over (C02 p0864) was made against Emiri, and the narration calls it illogical.
- A search of the source finds no boat or marina attached to Hani before C03 p0951.

The hints are weak. Both corpora rightly judge the route late. GPT already notes Hani's defensiveness at the alibi question. **CONFIRM**, `GPT_OMISSION`. **P3.** Integration: (d) optional KSOA-V05-D-0005.

#### KCMP-V05-005 — Contradiction in Asumi's dating of the marriage

1. **Passage.** C03 p0943, p0218–0225; C02 p0423–0434, p0636–0640, p0234.
2. **Context.** Asumi's reconstruction at the memorial, prefaced 「これはわたしの想像ですから、間違っているかもしれません」 (C03 p0943), set against three witnesses in earlier interviews.
3. **Established and inferred.** Established:
   - Asumi: after the 日本建築家連盟賞, Wakao left the Atobe office and 「結花さんと結婚した」 (C03 p0943).
   - Emiko: Wakao married and rented a house in 扇ガ谷, leaving the apartment early, and left the office 「もっと後」 (p0224).
   - Yuka recalls gatherings at 「前の扇ガ谷の家」, and Hani recalls watching mid-2000s films there (C02 p0424–0428).
   - Emiri's hearsay: in the Atobe-office years Yuka spoke of both of them working (「共働き」, p0639).

   Inferred: whether this is a characterized error or an authorial slip.
4. **Strongest competing explanation.** An authorial slip. The contradiction does not touch the culprit.
5. **Verdict.** CONFIRM. **Final:** `GPT_OMISSION`; the cause is `UNRESOLVED`. GPT's chronology row says only "The reasons for her later choice remain a detective's inference".
6. **Residual uncertainty.** The cause, and the exact year of the marriage, which is before 2008, probably in the mid-2000s or earlier.
7. **Implications.** GPT CL-0005 (the "taking a partner" analogy, whose timeline depends on this date), the V05 chronology table, REL-0001 and REL-0004 are affected.
8. **Priority.** P2.
9. **Integration.** (f) new KSOA-V05-CL-0007 (OPEN); (c) new KSOA-V05-EVT-0001.

#### KCMP-V05-006 — Yuka and the "stolen girlfriend" analogy (MODIFY)

1. **Passage.** C02 p0229–0240, p0248–0266; C03 p0932–0946.
2. **Context.**
   - Asumi stages the question 「あなたは若尾さんになにを盗まれたのですか」 (C03 p0932), then answers it: 「恋人の結花さんを盗まれたのです」 (p0936).
   - She then qualifies herself: 「わたしの想像」 and 「あなたからしたら…盗まれたようなものでしょう」 (p0943).
   - When Yuka told how she met Wakao, she said 「同じ写真サークル」 (C02 p0231). Hani was not yet present (he arrives at p0248) and was there later in the interview.
3. **Established and inferred.** Established: the author builds the parallel into Asumi's question. Asumi frames the "theft" as conjecture and as Hani's perspective. Yuka never mentions the student romance, and the page never shows her being asked about it. Inferred: whether her silence was a concealment.
4. **Strongest competing explanation.** One reader holds that Yuka knowingly withheld a fact relevant to motive. Another holds that the parallel is merely the detective's rhetoric. The text settles neither.
5. **Verdict.** MODIFY. The interpretive disagreement is real: CB1's thesis of "a mirrored pair of thefts" (READING l.63) treats the taking as a fact of the victim's life, while GPT CL-0005 cautions that read literally it obscures Yuka's decisions. The register's minor `CLAUDE_ERROR` dimension is not sustained. CB1's "omitted her student romance" is literally accurate, since she did not mention it when describing how she met Wakao. What outruns the page is the implication of concealment in "her omission of the romance was real" (READING l.180), a wording caution and not an error. **Final:** `INTERPRETIVE_DISAGREEMENT`.
6. **Residual uncertainty.** Yuka's reasons and agency.
7. **Implications.** GPT CL-0005 and REL-0004; CB1's §D thesis (frozen).
8. **Priority.** P3.
9. **Integration.** (f) KSOA-V05-CL-0005-R01 (REVISE); (h) CB1 wording note.

#### KCMP-V05-007 — V05 Japanese register

1. **Passage.** All of V05 searched for あんた, おまえ, お前, キミ, 元哉くん, 吉川くん, あたし and 俺. In context: C01 p0227, p0313, p0337, p0344, p0519, p0571, p0647; C02 p0015, p0549–0559, p0712–0895; C03 p0747, p0760, p0949, p0954, p0959; PRO p0014, p0028, p0052.
2. **Context.** Every token was checked against its speaker line.
3. **Established and inferred.** Established:
   - Asumi says あんた to Motoya seven times, all in the C02 quarrel (p0712, p0756, p0777, p0785, p0808, p0883, p0894). The two あんた in C01 are Watanabe's (p0519, p0571).
   - Asumi's あたし occurs only with Motoya (C01 p0647; C02 p0015; C03 p0760).
   - Asumi: 「元哉くんっ」 (C01 p0313); 「吉川くん、事件だよ」 (p0344); the in-group 「吉川がお世話になっております」 (p0337); bare 「吉川、手錠掛けて」 (C03 p0959).
   - Motoya says おまえ to Asumi once, 「おい、小笠原、おまえ頭大丈夫か？」 (C02 p0789). The other おまえ tokens belong to 正木, the quoted 跡部, and the prologue narrator. Motoya uses 僕 with civilians (C01 p0227).
   - Hani says 「僕にはアリバイがある」 (C03 p0949), then 「若尾が俺を馬鹿にするから」 (p0954), which echoes the prologue's 「どこまでも俺を馬鹿にしている」 (PRO p0028) and 「俺をバカにし続けてきた」 (p0052).

   Inferred: that Hani's 俺 serves as a textual identity link to the prologue voice. This is strongly supported.
4. **Strongest competing explanation.** 俺 under stress is ordinary male speech. The echo of 「馬鹿にする」 is the more specific link.
5. **Verdict.** CONFIRM. **Final:** `GPT_OMISSION`. There are no V05 VOICE rows, and the GPT studies cite あんた only for V06 and 僕 only for V07.
6. **Residual uncertainty.** None for V05.
7. **Implications.** GPT's character ledger, the register sections of the lead studies, and ADJ-0003 ("Hani's admission narrows the narrator") gain textual support. Coordinate with CHAR.
8. **Priority.** P2.
9. **Integration.** (e) new KSOA-V05-VOICE-0001 to -0003; (d) a note on ADJ-0003; (g) lead studies.

#### KCMP-V05-008 — Anchoring the chronology

1. **Passage.** C03 p0218–0224, p0012, p0595, p0661, p0779, p0782, p0788, p0912, p0962; C02 p0187, p0192, p0234, p0125, p0451, p0459; C03 p0501; EPI p0004–0005.
2. **Context.** Narration and testimony. The story year is derived by arithmetic and is not printed.
3. **Established and inferred.**
   - Emiko: Atobe retired 「一三年前…二〇一〇年の秋」 (C03 p0224), so the present is 2023 (derived).
   - Season: 「梅雨の晴れ間」 (p0779) and 「梅雨の中休み」 (EPI p0005).
   - The weekdays:
     - C02 is Monday (「一昨日の夜」 for Saturday, C02 p0187).
     - C03 opens Monday at 12:55 (C03 p0012), with Tanaka and Kodera the same day.
     - Enomoto is seen 「翌日の午前一〇時」, Tuesday (p0595, p0661).
     - The gathering is 「翌々日の午後三時」, Thursday (p0782), with the arrest at 16:02 (p0962) and the wake at 18:30 (p0788).
   - The student era is 「二〇世紀終わり頃」 (C02 p0234).
   - Independence: Wakao in 2008, Hani and Enomoto in 2009, Kodera in 2010 (C03 p0497, p0501).
4. **Strongest competing explanation.** GPT's relative chronology serves its horizon logic. An absolute year is an analyst's derivation, and that part is close to an architectural difference. The register also overstates one point: GPT's "Early 2000s" row describes a "prior relationship", so it does not literally date the student romance to the early 2000s.
5. **Verdict.** CONFIRM. **Final:** `GPT_COMPRESSION`. The table runs from "Saturday evening" to "Sunday and inquiry" to "Next Sunday", omitting the Thursday gathering and every anchor of day and season.
6. **Residual uncertainty.** None for the sequence. The year is derived.
7. **Implications.** The V05 deep-reading chronology table (frozen) and the case-ledger EVT rows are affected.
8. **Priority.** P2.
9. **Integration.** (a) erratum ERR-V05-03; (c) new KSOA-V05-EVT-0002.

#### KCMP-V05-009 — Ordinary life, setting, local history and institutions

1. **Passage.** C01 p0462, p0647, p0683, p0725, p0739, p0745; C02 p0727; C03 p0013, p0107, p0150, p0512, p0591, p0617.
2. **Context.** Narration through Motoya and witness speech.
3. **Established and inferred.**
   - Motoya washes down a burrito with iced coffee (C01 p0725), sleeps on the thin futon of the station 武道場 (C03 p0591), and is embarrassed by his ready-made suit, 「吊るしのスーツ」 (p0617).
   - Asumi orders lemon squash (C02 p0727) and wears high-cut sneakers (C01 p0462). Her apartment has 「北欧デザイン」 items (C03 p0150). Her father runs the kimono shop 《かつらや》 in Hiratsuka and is a well-known cosplay-costume maker (p0512).
   - 吉田 is away at a 修善寺 inn (C01 p0647), so 正木 sets the pairings: 「強行犯係長もいないんで、俺が勝手に」 (p0683).
   - The command is 福島 as head of the first investigation section (p0739) and 二階堂 as 管理官 (p0745).
   - The place name 西御門 comes from the west gate of the 大倉御所 (C03 p0013). The Atobe house is a 「昭和三年の建物」 (p0107).
4. **Strongest competing explanation.** Much of this is texture. The subset about character and institutions bears on reconstruction and on INST-0001.
5. **Verdict.** CONFIRM. **Final:** `GPT_OMISSION`.
6. **Residual uncertainty.** None.
7. **Implications.** GPT INST-0001 is affected: 吉田's absence explains 正木's discretion. Also affected are the "ordinary life" paragraph of the Asumi study and the policing study.
8. **Priority.** P2 for the subset about character and institutions; the meals and local history are P3.
9. **Integration.** (e) new KSOA-V05-STATE-0002 and -0003 and an amendment note on INST-0001; (g) Asumi study and policing study.

#### KCMP-V05-010 — CB1 grades the boat strike "established"

1. **Passage.** C03 p0951–0958, p0965. CB1: `CB1_CLAIM_AND_UNCERTAINTY_INVENTORY.md` l.51 (definition) and l.113 (CB1-CL-026); `CB1_LONGITUDINAL_SYNTHESIS.md` l.108 and l.546.
2. **Context.** The boat exists only in Asumi's speech, 「プレジャーボートを係留しておいたのですね」 (p0951). Hani admits the blow and that he had no intent to kill (p0954) and nods to 「認めるのですね」 (p0956–0958). Motoya: the physical evidence still has to be collected (p0965).
3. **Established and inferred.** Established: the blow, from the prologue and the admission, and Hani's identity. Inferred: the boat route. It is a reconstruction.
4. **Strongest competing explanation.** By genre convention and Motoya's acceptance, the route is the in-world solution, and the nod could be read as assent to the whole account.
5. **Verdict.** CONFIRM. **Final:** `CLAUDE_ERROR`. CB1 defines "established" as directly shown or confessed. The boat is neither, and CB1's own LS l.546 lists "V05's route" as probable rather than established. CB1-CL-026's counterevidence column already notes that the route was not confessed.
6. **Residual uncertainty.** None on the status point.
7. **Implications.** None for GPT. RES-0002 and CL-0001-R01 already have the correct calibration.
8. **Priority.** CB1-only.
9. **Integration.** (h).

#### KCMP-V05-011 — Enomoto's Tuesday statements against his Thursday admission (short entry)

On Tuesday Enomoto:
- answers who stole the drawings with 「わかりません」 (C03 p0722–0724);
- asks the pair to forget the story (p0730);
- says the widow probably does not know (p0747), which is sincere hearsay, since Kodera overheard Atobe telling her 「おまえも詮索するな」;
- says 「すべてを話しました」 (p0750).

On Thursday he says 「犯人は若尾しかあり得ないんです」 and admits that he and Kodera had been gathering material to expose Wakao (p0918). The register did not cite p0750, which is the clearest falsehood, since it hid the exposure project. Emiko did know (p0870). **CONFIRM**, `BOTH_INCOMPLETE`. **P3.** Integration: (c) a reliability note on EV-0009.

#### KCMP-V05-012 — Introduction says "student friends"; coverage table says "five architects"

1. **Passage.** C02 p0414–0423; C03 p0306–0308, p0783–0785.
2. **Context.** Yuka mentions the names in passing, 「田中さんや小寺さん、榎本くんにも連絡しなくっちゃね」 (C02 p0414). Asked who they are, she says 「若尾の跡部事務所時代の同僚です」 (p0420). Hani adds 「僕に続けて跡部事務所に入ったヤツら」 (p0422).
3. **Established and inferred.** The three were colleagues at the Atobe office, not fellow students. Wakao and Hani went to 武蔵美, Enomoto to 東京藝大 and Tanaka to 東大 (C03 p0308). Yuka names them first. In C03 four living architects take part (「田中正行、羽仁直人、榎本賢三、小寺隆則の四人」, p0784).
4. **Strongest competing explanation.** "Five architects" might mean the 五人衆 as a group whose history is told. It remains loose, because Wakao gives no account in C03.
5. **Verdict.** CONFIRM. **Final:** `GPT_ERROR`, minor. The deep reading's H-0007 has it right.
6. **Residual uncertainty.** None.
7. **Implications.** Only the introduction's synopsis and the deep-reading coverage table.
8. **Priority.** P1, minor in severity.
9. **Integration.** (b) targeted edit to the introduction; (a) erratum ERR-V05-01 for the coverage table.

#### KCMP-V05-013 — Asumi's promise to Enomoto, its public use, and the insinuation against Kodera (MODIFY)

1. **Passage.** C03 p0688–0696, p0750–0755, p0896–0911, p0926.
2. **Context.** Tuesday, at the hotel, and Thursday, at the memorial gathering, narrated through Motoya.
3. **Established and inferred.**
   - Enomoto asks 「ここだけの話にしてくれますか」 and Asumi answers 「もちろんです」 (p0691–0693), without conditions.
   - Enomoto restates his request conditionally: 「今回の事件に関係がないならば…胸にしまっておいてください」 (p0754).
   - In public Asumi uses the overheard conversation (p0900).
   - To Kodera: 「裏はとっています。でも、たとえば、その証言が真実でないとしたら……」 (p0904), then 「たとえばの話です。気にしないでください」 (p0908).
   - Motoya thinks 「亜澄は意地が悪い」 (p0926).

   Inferred: whether the confidence was breached. The condition Enomoto attached, relevance to the case, was arguably met. The Kodera remark is a hypothetical insinuation against an alibi she knows is corroborated. It is not a bluff, since she claims nothing she lacks.
4. **Strongest competing explanation.** GPT's general treatment covers the spirit of both acts: "In confidence" and "asks the pair to limit circulation" (H-0013), and "the act of testing alternative accusations leaves a cost to witnesses with already corroborated alibis" (`#design-recognition-and-care`).
5. **Verdict.** MODIFY. **Final:** `GPT_COMPRESSION`, not omission. The particulars are missing (the unconditional promise, its later public use, the insinuation), but the general point is present. The register's "bluff" should read "hypothetical insinuation". The same wording issue appears in CB1 READING §H.
6. **Residual uncertainty.** Whether the use breached the confidence or fell within Enomoto's condition.
7. **Implications.** GPT ACT-0002, CH-0004 and the Asumi study (`#the-costs-and-uses-of-control`) are affected, along with the GPT and CB1 lead portraits of Asumi's methods.
8. **Priority.** P2, for the ethics of the lead character.
9. **Integration.** (c) an amendment note on ACT-0002; (g) Asumi study; (h) CB1 wording note.

#### KCMP-V05-014 — Two overstated V05 summaries in the GPT studies

1. **Passage.** C01 p0118–0145, p0212–0230; C02 p0710–0902; C03 p0399–0422, p0973. Searched all of C02, C03 and EPI for ごめん, すまな, 悪かった, お詫び and 謝.
2. **Context.**
   - Sayaka hands Motoya the interview: 「吉川さんの好きなように質問して」 (p0128) and 「わたしが訊くよりナチュラルなインタビューになると思う」 (p0134).
   - Motoya means to show professional skill (p0137) but knows nothing about sea glass (p0138–0139). Afterwards he believes he could not ask proper questions (p0213).
   - Sayaka explains that his ignorance made the interview good (p0217, p0222).
3. **Established and inferred.** Established: the design was Sayaka's, and Motoya's basic questions came from ignorance, not from a decision taken on behalf of readers. Asumi never apologizes to Motoya. Her only apology is to the room at the memorial, for rudeness (C03 p0973). The café quarrel ends with Asumi back to her usual self, 「ふだんの姿を取り戻している」 (p0411).
4. **Strongest competing explanation.** In the partnership study's row, "the ensuing confrontation and her apology" might mean the memorial confrontation, which is how the GPT corpus uses "confrontation" in CH-0004 and in the Asumi study. Following the sentence about the Emiri encounter, however, it reads as an apology for the private quarrel.
5. **Verdict.** CONFIRM. **Final:** `GPT_ERROR`, minor. The error is attributional in `studies/KSOA_MOTOYA_KITSUKAWA.md#a-focalizer-with-a-job-of-his-own` ("deliberately asks basic questions on behalf of readers"). The partnership study's V05 row (`#directed-states-by-volume`) is misleading in presentation. The GPT deep reading (H-0002 and "Work and private obligations collide") has the interview right.
6. **Residual uncertainty.** What the partnership row's author meant.
7. **Implications.** The Motoya study's argument for his initiative should rest on other evidence: the handoff and the credit given to Asumi's estimate (C01 p0543). KSOA-SER-CL-0004's V05 support is not affected.
8. **Priority.** P1, minor in severity.
9. **Integration.** (g) Motoya study and partnership study.

---

## 3. Integration action list

All new row IDs are **provisional**. They take the next free number visible at commit `7d8ece76`. The Group D adjudication (SERIES/CHAR) may propose rows in the same ledger sections, especially V04 and V05 VOICE rows, so the integrator must renumber on collision and keep the cross-references below consistent. Every row is generation KSOA-G1. Disclosure horizons link to the owning frozen reading.

### (a) Frozen deep readings — errata (never edit; attach through the correction route)

**`readings/KSOA_V04_DEEP_READING.md`**

- **ERR-V04-01** (from KCMP-V04-007), anchors `#ksoa-v04-h-0002`, `#ksoa-v04-h-0003`, `#ksoa-v04-h-0006`, `#ksoa-v04-h-0007`, `#ksoa-v04-h-0014`, `#ksoa-v04-h-0015`. Erratum text: "For 'Kechika' read 'Echika' throughout (13 occurrences). 森岡恵智花 is glossed ｜恵《え》｜智《ち》｜花《か》 at C01 p[0150]; she is 21 (C01 p[0152])."
- **ERR-V04-02** (from KCMP-V04-001), anchors `#ksoa-v04-h-0014` and `#how-the-two-roles-fit`. Erratum text: "Add: Echika states that all memorial keys, the spare included, were kept in the drawing room in a dial-lock key case (C03 p[1040], p[1044]). Asumi says the culprit used a copy, obtained from an accomplice (p[1042], p[1046], p[1054]), and puts it to Hachiya that he had borrowed Yūko's key and copied it (p[1104]). Hachiya answers 「そうだよ、鍵は俺が渡した」 (p[1108]), an explicit affirmative that itemizes only the handover. The copy's origin is Asumi's account; Miyazaki's own key account is withheld (p[0972]–p[0974])."
- **ERR-V04-03** (from KCMP-V04-004), anchor `#ksoa-v04-h-0014` ("Institution and form"). Erratum text: "Before the reveal, Shichijō tells the detectives that Yūko had vowed to spend her last years with 蜂屋貞一 (C03 p[0799]–p[0804]; compare C01 p[0211], C02 p[0401]–p[0404]). This narrows the facilitator for the reader. The marriage register, debts and 住民票 still first appear at the reveal (C03 p[1066]–p[1100]), so the withheld-bridge limit stands."
- **ERR-V04-04** (from KCMP-V04-005), anchor `#a-visible-secret-an-invisible-route`. Erratum text: "Prospectively, Asumi singles out one thin diamond chain bracelet in Yōsuke's private photographs as probably Van Cleef & Arpels, and the narration notes it is very thin for a man's piece (C01 p[0534]–p[0540]). She then stops at the 『竹寺の雪』 poster (p[0541]). By juxtaposition, a reader can connect the prologue's wrist to this bracelet before Miyazaki identifies it (C03 p[0885]–p[0902]). No character makes the link earlier."

**`readings/KSOA_V05_DEEP_READING.md`**

- **ERR-V05-01** (from KCMP-V05-012), anchor `#witness-and-coverage`, row C03. Erratum text: "For 'accounts from the five architects' read 'accounts from the four surviving architects (田中, 羽仁, 榎本, 小寺; C03 p[0784])'."
- **ERR-V05-02** (from KCMP-V05-002), anchor `#a-single-assault-amid-several-projects-of-redress`. Erratum text: "The prologue establishes, for the reader only, that the narrator brought a 木刀 to threaten Wakao (PRO p[0045]), chose a deserted place (p[0074]) and threw the contents of Wakao's bag into the sea (p[0075]). Watanabe's estimate of a blow from behind with 'a rod about the size of a 木刀' (C01 p[0511]) links the prologue to the body. What remains open at the end is the investigators' recovery and forensic confirmation, not the fate of the contents."
- **ERR-V05-03** (from KCMP-V05-008), anchor `#the-coast-changes-what-can-be-recovered`, chronology table. Erratum text: "Anchors: story year 2023, derived from Atobe's retirement 「一三年前…二〇一〇年の秋」 (C03 p[0224]); the rainy season (C03 p[0779]; EPI p[0005]). The prior Hani–Yuka relationship belongs to the student era, late 1990s (「二〇世紀終わり頃」, C02 p[0234]). The investigation week runs as follows: Saturday night the act; Sunday the discovery (C01); Monday morning the Wakao house (C02; p[0187]); Monday afternoon Emiko, Tanaka and Kodera (C03 p[0012]–p[0592]); Tuesday 10:00 Enomoto (p[0595]); Thursday 15:00 the gathering (p[0782]), arrest at 16:02 (p[0962]), wake at 18:30 (p[0788]); the next Sunday the epilogue (EPI p[0004])."
- **ERR-V05-04** (from KCMP-V05-003), anchor `#a-single-assault-amid-several-projects-of-redress`, detectability paragraph. Erratum text: "Add: the focalizer actively discounts the eventual culprit. Motoya judges the chance that Hani is the culprit 「皆無」 (C02 p[0370]) and his alibi unproblematic (p[0397]), as he had earlier found Yuka beyond suspicion (p[0187]–p[0188])."

### (b) Reading introductions (`active_provisional`) — targeted edits

- **`readings/KSOA_V04_READING_INTRODUCTION.md#3-current-volume-story-synopsis`**, paragraph 2 (KCMP-V04-014). Replace "Akao interviewed director Hongō at dinner and asked to check something in Sekigawa's film." with: "Akao interviewed director Hongō in the drawing room from about four to six, then asked to check something in Sekigawa's film in the memorial screening room. Hongō and Echika dined from about half past six without him." Locators for the change log: C01 p[0306], p[0311], p[0320]; C02 p[0163].
- Same file, same paragraph (KCMP-V04-007), optional. After the ledgers are corrected, replace "(恵智花, rendered “Kechika” in the linked deep reading)" with "(恵智花, えちか; the linked deep reading's 'Kechika' is corrected by erratum ERR-V04-01)".
- **`readings/KSOA_V05_READING_INTRODUCTION.md#3-current-volume-story-synopsis`**, paragraph 3 (KCMP-V05-012). Replace "He remembers Wakao as his senior and mentor and names their student friends and colleagues Masayuki Tanaka, Kenzō Enomoto and Takanori Kodera." with: "He remembers Wakao as his senior at university and his mentor at Atobe's office. Yuka mentions Masayuki Tanaka, Takanori Kodera and Kenzō Enomoto, Wakao's colleagues from the Atobe office, and Hani describes them as having joined the office after him." Locators: C02 p[0414]–p[0422].

### (c) `KSOA_CASE_EVIDENCE_LEDGER.md`

**Section `## V04 case evidence`**

- **Correction notes** on `#ksoa-v04-ev-0002` and `#ksoa-v04-ev-0006` (KCMP-V04-007): "Name correction: for 'Kechika' read 'Echika' (恵智花, ruby えちか, C01 0150). Basis: KCMP-V04-007 / ADJ_B."
- **New KSOA-V04-EV-0015**, key custody and provenance (KCMP-V04-001). Disclosure H-0014. Locators C01 0354–0367; C03 0956–0974, 1035–1054, 1104–1109. Record: "Echika states that the memorial keys, the spare included, were kept in the drawing-room sideboard in a dial-lock key case. Asumi asserts entry with a copy obtained from an accomplice and puts it to Hachiya that he had borrowed and copied Yūko's key. Hachiya answers 'そうだよ、鍵は俺が渡した'. The copy's origin is the detective's account with Hachiya's explicit affirmative, which itemizes only the handover. The duplicate and Miyazaki's own account are not shown. Related: EV-0003, EV-0014, RES-0002."
- **New KSOA-V04-EV-0016**, Akao's knowledge of the marriage (KCMP-V04-002). Disclosure H-0014. Locators C03 1066, 1075–1079, 1100. Record: "Police obtained the 戸籍謄本 by 職権 at Kamakura city hall. It shows Yūko's marriage about six weeks earlier, with Hachiya as head of the new register. Asumi reports that Akao learned of the marriage from a Kamakura 住民票 obtained at his request by the 行政書士 曽根昌雄 under 職務上の権限, an act she calls probably illegal. These are reported off-page findings; Sone is not shown. Case: CASE-0002."
- **New KSOA-V04-EV-0017**, sums and inheritance mechanism (KCMP-V04-006). Disclosure H-0013/H-0014. Locators C03 0572–0580, 0916–0920, 1079–1094, 1114. Record: "The passbook shows ¥5m withdrawn at the counter of the Kamakura branch on 31 March. In his first account Miyazaki says it was handed to Akao in cash; in his revised account it was paid under threat, a further ¥3m was demanded in April, and he then decided to kill. Asumi reports verified debts of Hachiya of about ¥600m and an estate of over ¥800m, and states that a third could pass to Shichijō if a family court corrected the register. Shichijō says she will never declare her maternity. The figures are reported, not shown. Related: EV-0011, EV-0013, EV-0014."
- **New KSOA-V04-EV-0018**, bracelet identification (KCMP-V04-005). Disclosure H-0004. Locators C01 0529–0552; C03 0880–0913. Record: "Asumi singles out a thin diamond chain bracelet in Yōsuke's private photographs as probably Van Cleef & Arpels, white gold or platinum, then stops at the 『竹寺の雪』 poster. Miyazaki later confirms that piece ('たぶんそれだ') and places it on Shichijō's left wrist in the final take. The pre-reveal link to the prologue's wrist is available to the reader only by juxtaposition. Related: EV-0004, CL-0001."
- **New KSOA-V04-EV-0019**, victim portrait and early pointers (KCMP-V04-010). Disclosure H-0004/H-0005. Locators C01 0644–0647, 0778–0792, 0831–0845. Record: "Motoya notes Akao was somewhat grasping about money, with no homicidal money trouble found. Torii reports that Akao did not seem to love his subject, was abnormally fixated on mid-Shōwa-30s films, pressed for a higher royalty and had a reputation for haggling over fees; that he was divorced with a son living with his ex-wife; and that the family refused the body. This is hearsay from a cool witness. It suggests money and a period focus; it is not diagnostic."
- **Correction note** on `#ksoa-v04-res-0002` (KCMP-V04-001, -011, -013): "Independently unresolved questions:
  1. How Miyazaki knew Akao would be alone in the screening room after 18:00 (C01 0311). Not addressed through EPI 0137.
  2. The content of Miyazaki's withheld account, which opens in late March (C03 0972–0974).
  3. Whether the alleged instigation preceded or followed Miyazaki's April decision to kill (C03 0920 vs 0972).

  Key provenance: see EV-0015. Figures: EV-0017."
- **Optional note** on `#ksoa-v04-ev-0010` (KCMP-V04-015), P3: "Asumi stops the frame; Motoya names the silver Alto and confirms it matches the one at the Shichijō carport (C03 0402–0409)."

**Section `## V05 case evidence`**

- **New KSOA-V05-EV-0013**, reader-only weapon and bag (KCMP-V05-002). Disclosure H-0001. Locators PRO 0043–0082; C01 0509–0512, 0554, 0563. Record: "The narrator holds a 木刀 brought to threaten Wakao, strikes his head with it, chose a deserted place, and throws the contents of Wakao's bag into the sea. Watanabe's estimate of a blow from behind with a rod about the size of a 木刀 is the investigators' closest correlate. Wallet, licence and phone survived in zipped parka pockets. No investigator mentions the weapon or the bag again."
- **Amendment note** on `#ksoa-v05-ev-0001`: "Watanabe: wound like one from a 木刀-sized rod struck from behind (C01 0511). Valuables were retained because the parka pockets were zipped (0554, 0563)."
- **Amendment note** on `#ksoa-v05-ev-0009` (KCMP-V05-011): "Reliability limit. On Tuesday Enomoto answers 'わかりません' about the thief (C03 0724) and says 'すべてを話しました' (0750). On Thursday he says the thief can only be Wakao and admits a joint effort with Kodera to document and expose it (0918). His belief that the widow did not know rests on Kodera's overhearing (0747); she did know (0870)."
- **Amendment note** on `#ksoa-v05-act-0002` (KCMP-V05-013): "Asumi's unconditional promise to keep Enomoto's account between them ('もちろんです', C03 0691–0693). His later conditional restatement ('if unrelated to this case', 0754). Her public use of the overheard conversation (0900). Her hypothetical insinuation that Kodera's corroborated alibi witness might be untruthful, then withdrawn (0904–0908). Motoya privately calls it mean (0926)."
- **Optional amendment** on `#ksoa-v05-ev-0012` (KCMP-V05-001), P3. Quotation support: "PRO splash immediately after the blow (PRO 0064) vs Asumi's '殴って倒し、その身体を海に放り込んで' (C03 0952). The examiner's opinion is a fall (C01 0746)."
- **New KSOA-V05-EVT-0001**, Wakao–Yuka marriage, alternative chronology (KCMP-V05-005). Disclosure H-0014. Locators C02 0423–0434, 0639; C03 0224, 0943. Record: "Asumi places the marriage after the 2008 award. Emiko, Yuka and Hani, and Emiri's hearsay place it during the Atobe-office years, with the earlier home in 扇ガ谷. Status: contradiction; cause unresolved. See CL-0007."
- **New KSOA-V05-EVT-0002**, investigation-week anchors (KCMP-V05-008). Content as in ERR-V05-03.

### (d) `KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md` (adjudication rows only; frozen hypotheses untouched)

**Section `## V04 disclosure history`**

- **Correction note** on `#ksoa-v04-adj-0002` (KCMP-V04-007): name correction as in (c).
- **New KSOA-V04-ADJ-0003**, retrospective availability of the parentage hypothesis (KCMP-V04-003). Horizon H-0013; locators C01 0578; C02 0093–0098, 0111, 0219, 0235, 0435–0441, 0936, 0966; C03 0188, 0704–0731. Record: "Retrospective review. By H-0008 a reader can compute Yūko's birth year (1961/62) against Shichijō's 1961 retirement and disappearance, and has the mother who died within a year and whom Hongō never met, and Yūko's belief that a nurse was her mother. H-0009 adds Yōsuke's reported depression. A parentage hypothesis was available and salient to a careful reader, though no character voiced it and two reputation witnesses deny an affair. Outcome: confirmed at C03 0704. D-0003's 'not yet entitled to infer' remains correct as 'not warranted to conclude'."
- **New KSOA-V04-D-0006**, the vow (KCMP-V04-004). Horizon H-0013; locators C03 0789–0807. Prior clues: C01 0211; C02 0401–0404. Record: "Shichijō discloses that Yūko had vowed to spend her last years with Hachiya. Focalizer Motoya recalls she was thought single. Explicit, low emphasis. It points toward the facilitator before the register is shown."
- **New KSOA-V04-K-0004**, Akao's knowledge of the marriage (KCMP-V04-002). Actor: Akao. Acquisition before the April extortion of Hachiya. Established to the reader at H-0014. Route: a 住民票 obtained through a scrivener. Mode: confirmed by report (C03 1100).
- **New KSOA-V04-K-0005**, Akao's route to Shichijō's address (KCMP-V04-012). Actor: Akao. Route: obtained from Yūko, by Miyazaki's hedged report 「訊き出したらしい」 inside the later-retracted investment story (C03 0586). The address had circulated through Utsunomiya to the Sekigawa family (C02 0764, 0979). Mode: unknown or suspicion. Whether the visit took place is unverified.

**Section `## V05 disclosure history`**

- **New KSOA-V05-K-0003**, reader-only physical facts (KCMP-V05-002). Horizon H-0001; PRO 0045, 0074–0077. Actor: reader. Mode: access. The investigators never acquire these facts on the page.
- **New KSOA-V05-K-0004**, Motoya's belief about Hani (KCMP-V05-003). Horizon H-0007; C02 0370, 0397; also 0187–0188 on Yuka. Actor: Motoya. Mode: belief, an error regarding Hani.
- **New KSOA-V05-D-0005** (optional, KCMP-V05-004). Horizon H-0007: maritime references before the reveal (C01 0465–0467, 0536; C02 0395, 0461). The only boat talk is attached to Tanaka. Weak and misdirecting.
- **New KSOA-V05-ADJ-0004** (KCMP-V05-003, -004). Horizon H-0014: K-0004 is contradicted by the admission (C03 0954). A boat is first attached to Hani at C03 0951. D-0005's references did not discriminate.
- **Note** on `#ksoa-v05-adj-0003` (KCMP-V05-007): "Textual identity link. Hani's shift from 僕 (C03 0949) to 俺 in '若尾が俺を馬鹿にするから' (0954) echoes the prologue's 'どこまでも俺を馬鹿にしている' (PRO 0028)."

### (e) `KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md`

**Section `## V04 character and institutional state`**

- **Correction note** on `#ksoa-v04-rel-0003` (KCMP-V04-007): name correction.
- **New KSOA-V04-STATE-0001**, lead identity facts (KCMP-V04-009). Horizon H-0006 to H-0015. Locators C01 0070; C02 0032, 0043; C03 0025; EPI 0074. Record: "Asumi is 29 and moved from 本部 to Kamakura station a little over a year earlier. She lives in Kamakura and sleeps at home during the joint HQ. Motoya will turn 31 and returns to Yokohama."
- **New PERSON rows** (KCMP-V04-009, -010), one each:
  - KSOA-V04-PERSON-0001: 森岡恵智花 (もりおか えちか), 21, Yūko's niece (C01 0150–0152).
  - KSOA-V04-PERSON-0002: 赤尾冬彦, 38, nonfiction writer. Portrait as in EV-0019 (C01 0111).
  - KSOA-V04-PERSON-0003: 関川由布子, 61 (C02 0111).
  - KSOA-V04-PERSON-0004: 七条晶子, 88 (C01 0583).
  - KSOA-V04-PERSON-0005: 本郷, 84 (C02 0025).
  - KSOA-V04-PERSON-0006: 蜂屋貞一, mid-50s by Motoya's estimate (C02 0394).
  - KSOA-V04-PERSON-0007: 宮崎隆之, 17 when he met Shichijō in 1961 (C03 0213).
- **New KSOA-V04-VOICE-0001**, Motoya (KCMP-V04-008). Record: "No おまえ to Asumi anywhere in V04. The only tokens are 佐竹's おまえたち (C01 0893) and 吉田's おまえ (C03 0355). He calls her こいつ before Hongō (C02 0035)." Cross-volume weight is for the CHAR task.
- **New KSOA-V04-VOICE-0002**, Asumi. Record: "キミ once (C01 0029) and 元哉くん once (C01 0046) to Motoya. わたくし in formal self-introduction (C02 0581, 0591, 1048)."
- **New KSOA-V04-VOICE-0003**, Shichijō. Record: "関川洋介さん while concealing (C02 0678, 0698, 0756); 洋介さん after confessing (C03 0710, 0716, 0731). Asumi herself mostly uses 関川洋介さん in the Day-2 interview (C02 0711, 0720, 0754, 0758; 洋介さん once, 0680), so the shift is partly audience-conditioned. わたくし throughout."
- **New KSOA-V04-VOICE-0004**, Miyazaki. Record: "わたし (C02 0529; C03 0501, 0519, 0558), then 俺 from the start of the money story (C03 0568). あんた to Asumi (0845)."

**Section `## V05 character and institutional state`**

- **New KSOA-V05-VOICE-0001**, Asumi (KCMP-V05-007). Record: "あんた to Motoya seven times in the C02 quarrel (0712, 0756, 0777, 0785, 0808, 0883, 0894). あたし only with Motoya (C01 0647; C02 0015; C03 0760). 元哉くん (C01 0313). 吉川くん (C01 0344, 0451, 0478, 0500). In-group 吉川がお世話になっております (C01 0337). 吉川の指導係です (C02 0549). Bare 吉川 at the arrest (C03 0959)."
- **New KSOA-V05-VOICE-0002**, Motoya. Record: "One おまえ to Asumi, in anger (C02 0789). 僕 with civilians (C01 0227). Silent non-correction of 指導係 (C02 0556–0559)."
- **New KSOA-V05-VOICE-0003**, Hani. Record: "僕 (C02 0258; C03 0949), then 俺 at the admission (C03 0954), echoing PRO 0028 and 0052."
- **New KSOA-V05-STATE-0001**, Motoya's judgments of witnesses (KCMP-V05-003). Record: "Yuka without suspicion (C02 0187–0188). Hani 'zero' chance (0370). Tanaka no big lie (C03 0403). Kodera truthful (0567). Right on Tanaka and Kodera, wrong on Hani."
- **New KSOA-V05-STATE-0002**, Motoya's ordinary life (KCMP-V05-009). Record: "Burrito with iced coffee (C01 0725); the station judo-hall futon (C03 0591); embarrassment at his ready-made suit (0617)."
- **New KSOA-V05-STATE-0003**, Asumi's ordinary life (KCMP-V05-009). Record: "Her father runs the kimono shop 《かつらや》 in Hiratsuka and is a well-known cosplay-costume maker (C03 0512). Nordic-design items in her apartment (0150). Lemon squash (C02 0727). High-cut sneakers at the beach (C01 0462)."
- **Amendment note** on `#ksoa-v05-inst-0001` (KCMP-V05-009): "Kamakura's 強行犯係長 吉田 is away at a 修善寺 inn (C01 0647), which is why 正木 sets areas and pairings himself (0683). Command: 福島, head of the first investigation section (0739); 管理官 二階堂 (0745)."

### (f) `KSOA_CLAIM_REVISION_LEDGER.md` (append revisions; predecessors preserved)

- **KSOA-V04-CL-0003-R03** — `STRENGTHEN` (KCMP-V04-001). Horizon H-0014; C03 1035–1054, 1104–1109. Proposition: "The locked-room endpoint is supplied at the reveal: a duplicate of the sideboard key, which Asumi says was copied from Yūko's key and handed over by Hachiya, who affirms the handover. Household custody of all keys, the spare included, in a dial-lock case is stated by Echika. The copy's origin is the detective's account with an explicit affirmative." Predecessor: R02. Affected: EV-0003, EV-0015, RES-0002.
- **KSOA-V04-CL-0003-R04** — `OPEN` (KCMP-V04-011). Horizon H-0014; C03 0920, 0968–0974, 1104, 1120. Proposition: "The causal weight of the alleged instigation is underdetermined. Miyazaki says he decided to kill at the April demand. His withheld account, given when asked to name the key supplier, opens in late March, before that decision. The text supports neither decisive instigation nor a contribution limited to the key." Affected: RES-0002, SER-CL-0001, the mystery study.
- **KSOA-V04-CL-0001-R03** — `STRENGTHEN` (KCMP-V04-005). Horizon H-0004, retrospective at H-0013; C01 0534–0541; C03 0885–0902. Proposition: "Reader-side availability of the bracelet clue rests on two cues: the prologue's wrist and Asumi's pre-reveal identification of the specific bracelet next to the poster. The link remains unvoiced until C03 0902."
- **KSOA-V05-CL-0005-R01** — `REVISE` (KCMP-V05-006). Horizon H-0014; C02 0231; C03 0932, 0936, 0943. Proposition: "The novel deliberately stages a parallel between the theft of the drawings and the 'theft' of Yuka (C03 0932), and the parallel is structurally meaningful. Asumi marks the personal 'theft' as her conjecture and Hani's viewpoint (0943). Yuka is never asked about the student relationship on the page, and her choices remain unreconstructed. Keep GPT's agency qualification."
- **New KSOA-V05-CL-0007** — `OPEN` (KCMP-V05-005). Horizon H-0014; C02 0424–0428, 0639; C03 0224, 0943. Proposition: "Asumi's dating of the Wakao–Yuka marriage after the 2008 award contradicts three witnesses who place it during the Atobe-office years. Whether this is the detective's error or an authorial slip is unresolved. It does not affect the attribution of the assault."
- **KSOA-SER-CL-0002-R01** — `STRENGTHEN` (optional; KCMP-V04-003). Add to the V04 support: "the parentage arithmetic reader-available by V04 H-0008/H-0009 (V04 ADJ-0003) and the bracelet identification (V04 CL-0001-R03)." The current proposition is otherwise preserved.

### (g) Studies

- **`studies/KSOA_MYSTERY_FORM_AND_CAUSALITY.md#what-a-reader-can-infer-before-the-solution`**.
  - V04 row, "Early grounds" column (KCMP-V04-003, -004, -005): add "Asumi's identification of the bracelet before the poster (C01 0534–0541); birth-year and disappearance arithmetic pointing to Yūko's parentage by H-0008/H-0009 (V04 ADJ-0003); Shichijō's naming of Hachiya as Yūko's sworn partner (C03 0799–0803)."
  - V05 row (KCMP-V05-003): add "The focalizer rules Hani out (C02 0370)."
  - Optional P3 wording, outside the register: the V05 row's "single violent intervention on the water" presupposes the boat, which the prologue does not show. Prefer "by the sea".
- **Same study, `#direct-action-enabling-action-and-knowledge`** (KCMP-V04-011): after "Asumi's account of the full inducement has more dependencies than the transfer itself", add "Miyazaki dates his own decision to kill to the April demand (C03 0920). The withheld account opens in late March (0972), so the instigation's weight stays open (V04 CL-0003-R04)."
- **`studies/KSOA_ASUMI_OGASAWARA.md`**:
  - `#from-noticing-a-difference-to-making-it-testable` (KCMP-V04-005): add that Asumi's material expertise extends to jewelry, with the V04 bracelet identification by maker and metal (C01 0534–0538) as the reader's second clue.
  - `#the-costs-and-uses-of-control` (KCMP-V05-013): add the V05 promise to Enomoto, its public use and the hypothetical insinuation against Kodera's corroborated alibi.
  - `#address-ordinary-life-and-felt-need` (KCMP-V04-008, KCMP-V05-007, KCMP-V05-009): add V04 キミ and 元哉くん once each; V05 あんた ×7 in the quarrel and the bare 吉川 at the arrest; her father's shop and costume-making.
- **`studies/KSOA_MOTOYA_KITSUKAWA.md`**:
  - `#a-focalizer-with-a-job-of-his-own` (KCMP-V05-014, KCMP-V05-003): replace "In V05, outside duty, he deliberately asks basic questions on behalf of readers unfamiliar with Emiri’s craft" with "In V05, outside duty, he takes over the interview at Sayaka's request; his ignorance of sea glass produces the basic questions she wanted (C01 0128–0139, 0217)". Add "In V05 he judges Hani's chance of being the culprit 'zero' (C02 0370), a misjudgment the reader shares."
  - `#registers-habits-and-the-final-resolve` (KCMP-V04-008, KCMP-V05-007): add no おまえ to Asumi in V04 and one, in anger, in V05 (C02 0789); 僕 with civilians (V05 C01 0227).
- **`studies/KSOA_PARTNERSHIP.md#directed-states-by-volume`**, V05 row, Asumi column (KCMP-V05-014): replace "The ensuing confrontation and her apology show an ability to register another cost." with "The ensuing quarrel with Motoya ends without apology (C03 0411). At the memorial she apologizes to the room for her rudeness (C03 0973), which shows an ability to register another cost."
- **`studies/KSOA_POLICING_PLACE_AND_NARRATION.md#who-can-act-on-a-question`** (KCMP-V04-002, KCMP-V05-009): add the V04 contrast between police 職権 access to the register (C03 1066) and Akao's 住民票 obtained through a scrivener's misuse of professional authority (C03 1100). Add that in V05 the Kamakura section chief's absence lets 正木 set the pairings (C01 0647, 0683).

### (h) CB1-only corrections (recorded here; the CB1 baseline stays frozen)

1. **KCMP-V04-012.**
   - `05_monographs/CB1_SHICHIJO_AKIKO_MONOGRAPH.md`, l.65: read "By 宮崎's later-retracted investment story, 赤尾 called while she and 紀江 were at hospital and had obtained the address from 由布子 (「訊き出したらしい」, [C03 p0586]); the visit is unverified."
   - Same file, l.116: read "sincere; whether she was wrong depends on an unverified visit".
2. **KCMP-V04-016.**
   - `CB1_V04_READING.md`, l.51, "the driver's aquiline nose unmistakable": read "Motoya is sure of the aquiline nose [p0441]; Asumi reports it cannot be confirmed [p0462]".
   - `CB1_V04_READING.md`, l.55, and `CB1_V04_EXIT_STATE.md`, l.66 and l.83, "renounces": read "is reported to have declared he will renounce [EPI p0056]".
   - `04_synthesis/CB1_CLAIM_AND_UNCERTAINTY_INVENTORY.md`, CB1-CL-020: split it. "Supplied the key" stands as admitted. "Incited him, for money" is an allegation and the ground of suspicion [C03 p1104, p1120], so its status should be "probable (allegation)", not "established".
3. **KCMP-V04-011.** CB1 READING §N.3 and LS l.142: the "doubtful" verdict on the incitement must also weigh the account opening in late March [C03 p0972]. The question remains open.
4. **KCMP-V05-001.** `CB1_V05_READING.md` §C (l.53) and `CB1_V05_EXIT_STATE.md` row 26: record that Asumi's 「殴って倒し、その身体を海に放り込んで」 [C03 p0952] differs from the prologue's immediate splash [PRO p0064] and from the examiner's opinion of a fall [C01 p0746]. The difference bears on intent and on the gap between the 傷害致死 arrest and Motoya's expected murder charge.
5. **KCMP-V05-006.** `CB1_V05_READING.md` l.103, l.180, l.188: "omitted her student romance" is literally accurate. "Her omission of the romance was real" should not imply concealment; read "did not mention it [C02 p0231]; never asked on the page".
6. **KCMP-V05-010.** `CB1_CLAIM_AND_UNCERTAINTY_INVENTORY.md` CB1-CL-026: split it. The blow and the identity of the assailant are established [PRO p0058; C03 p0954]. "From a boat" is a reconstruction [C03 p0951] and should be graded probable, consistent with LS l.546. LS l.108 should mark the route as Asumi's reconstruction.
7. **KCMP-V05-013.** `CB1_V05_READING.md` §H and the CB1 Asumi monograph: "bluff about 小寺's witness [p0904]" should read "hypothetical insinuation against a corroborated alibi [p0904–0908]". The promise to Enomoto was unconditional [p0693], but Enomoto later restated it on condition of irrelevance [p0754].

---

## 4. Counts

**Records adjudicated:** 30 (V04: 16; V05: 14).

**By final disposition (primary):**

| Final disposition | Count | Records |
|---|---|---|
| GPT_OMISSION | 13 | V04-001, 002, 003, 008, 009, 010, 013; V05-002, 003, 004, 005, 007, 009 |
| GPT_COMPRESSION | 5 | V04-004, 005, 006; V05-008, 013 |
| GPT_ERROR | 4 | V04-007, 014; V05-012, 014 |
| CLAUDE_OMISSION | 1 | V05-001 |
| CLAUDE_COMPRESSION | 1 | V04-016 (with a CLAUDE_ERROR dimension) |
| CLAUDE_ERROR | 1 | V05-010 |
| BOTH_INCOMPLETE | 3 | V04-011, 012; V05-011 |
| INTERPRETIVE_DISAGREEMENT | 1 | V05-006 |
| AGREE | 1 | V04-015 |
| UNRESOLVED / ARCHITECTURAL_DIFFERENCE_ONLY | 0 | none primary; these appear only as secondary dimensions: the cause in V05-005, and the absolute-year aspect of V05-008 |

Secondary dimensions:
- residual INTERPRETIVE_DISAGREEMENT: V04-003;
- GPT_COMPRESSION: V05-002;
- CLAUDE_ERROR: V04-012, V04-016;
- GPT_OMISSION: V04-012.

**By priority:**

| Priority | Count | Records |
|---|---|---|
| P1 | 4 | V04-007, 014; V05-012, 014 (all minor in severity) |
| P2 | 17 | V04-001, 002, 003, 004, 005, 006, 008, 009, 010, 011; V05-002, 003, 005, 007, 008, 009, 013 |
| P3 | 6 | V04-012 (GPT side), 013, 015 (optional); V05-004, 006, 011 |
| CB1-only | 3 | V04-016; V05-001, 010 |

In addition, CB1-side corrections arise from V04-011, V04-012, V05-006 and V05-013; see (h).

**Verdicts against the register:** CONFIRM 25, MODIFY 4 (V04-003, V04-016, V05-006, V05-013), OVERTURN 1 (V04-015). The register was modified or overturned in 5 of 30 records (17%). In four further CONFIRMs the reasoning or evidence was refined without changing the disposition:
- V04-001: Hachiya's 「そうだよ」 is explicit, not tacit;
- V04-011: the late-March account could date Akao's approach;
- V05-008: the GPT row says "prior relationship";
- V05-011: p0750 is the clearest falsehood.

**Blockers:** none. Two coordination notes:
- The proposed row IDs are provisional and must be reconciled with Group D, which may propose V04 and V05 VOICE rows.
- Errata to frozen readings need the repository's erratum vehicle under the claim-ledger correction route.
