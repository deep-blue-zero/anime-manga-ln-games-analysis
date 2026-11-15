---
title: "KCMP V01 comparative discrepancy register — 稲村ヶ崎の落日"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_CB1_KCMP_V01_REGISTER
artifact_type: comparative_discrepancy_register
generation: KSOA-CB1-COMPARISON
version: "1.0"
created: "2026-11-15"
status: historical_legacy
scope: "Phase 3 comparative register for V01 稲村ヶ崎の落日: dimension assessment, discrepancy records, agreement samples, omission searches, transfer candidates and compression note. Its proposed dispositions are superseded in effect by ADJ_A."
source_boundary: "Seven Japanese publisher EPUB witnesses KSOA-JP-V01-W01 to KSOA-JP-V07-W01 (all narrative sections); GPT corpus KSOA-G1 at 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a; KSOA-CB1 blind package frozen 2026-11-15T10:52:54Z, manifest SHA-256 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040."
canonical_home: series/kamakura-sho/audits/KSOA_CB1_COMPARISON/KCMP_V01_REGISTER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
do_not_use_as_literary_evidence: true
proposals_adjudicated_in: audits/KSOA_CB1_COMPARISON/ADJ_A.md
authority_note: "Historical comparison record. Its proposed dispositions, priorities and destinations are superseded in effect by the adjudication; cite the adjudication for any decision."
compared_generations: [KSOA-G1, KSOA-CB1]
gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
cb1_blind_package_manifest_sha256: 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040
source_record: "comparison/KCMP_V01_REGISTER.md in the KSOA-CB1 comparison workspace (outside Git)"
source_record_sha256: 95d14324e13490ac775fb611418b49387ec8f1253a56a56015331ce341db81ce
source_record_bytes: 53867
source_record_body_sha256: 74384cfe7da1f94f4bcf5bbc610de8f9315e877ddbcf3d2cdfc3b48b46fecdfc
copy_transformations:
  - "post-copy custodian scrub (2026-11-15): 2 mentions of the local KSOA-CB1 working-folder name replaced with 'KSOA-CB1:' where followed by a slash or backslash, otherwise with 'KSOA-CB1'; no other body byte changed; reversing the substitution reproduces the copied body"
path_rewrites: []
integration_date: "2026-11-15"
integrated_by: INT-6
source_record_front_matter: |
  title: "KCMP V01 comparative discrepancy register — 稲村ヶ崎の落日"
  artifact_type: comparative_discrepancy_register
  status: draft_noncurrent
  do_not_use_as_current_authority: true
  gpt_basis_commit: 7d8ece76cbefeea3eb1d7cd02d4ca99e41966d4a
  cb1_basis: "BLIND_PACKAGE_MANIFEST 35f7a16eddf07a6dffb0750e1146c34874d227a486886db36ca7bf9248113040"
  author_model: "Claude Opus 5.5 (claude-opus-5-5), Phase 3 Context B comparative reviewer"
  created: "2026-11-15"
  task: V01
  protocol: "comparison/COMPARISON_PROTOCOL.md (registered 2026-11-14)"
  work_notes: "comparison/work/V01_notes.md"
---

# KCMP V01 comparative discrepancy register

**Spoilers for all of V01.** This register compares the GPT corpus (pinned at `7d8ece76`) with the frozen CB1 baseline for volume V01. It names destinations for changes and writes no change to either corpus. Neither corpus was modified. No git command that changes the working tree was run.

**Conventions.** Source locators are `[SEC pNNNN]` in witness `KSOA-JP-V01-W01`, read from `KSOA-CB1:01_source/V01/V01_<SEC>.txt`. GPT locators of the form `C01 p[0014]` and CB1 locators `[V01 C01 p0014]` resolve to the same paragraph. I confirmed this on C01 p0014 (元哉's rank sentence, cited by GPT `KSOA-V01-PERSON-0001` and CB1 §C) and PRO p0011 (the manuscript-handoff line, cited by GPT `KSOA-V01-CL-0002` and CB1 F3 O-0003). Japanese quotations are short fragments, re-read in the extraction for this task. Both corpora and the source write the 隆 of 隆鄕 as the compatibility ideograph U+F9DC. This register uses that code point too, so a search for 隆鄕 returns the same hits in all three places.

---

## 1. Files read

### 1.1 GPT corpus (blob prefixes verified with `git hash-object` against `HEAD:` at `7d8ece76`)

| File | Blob | Completeness |
|---|---|---|
| `readings/KSOA_V01_DEEP_READING.md` | `f7b5b3397a5b` | Complete, lines 1–222, in five chunks. This includes the closeout section, "Closeout and limits", lines 217–222. |
| `readings/KSOA_V01_READING_INTRODUCTION.md` | `3743a94bf6e0` | Complete, lines 1–54. |
| `KSOA_CASE_EVIDENCE_LEDGER.md` | `9ed33ab7ef26` | Header (lines 1–39) and `## V01 case evidence` (lines 40–87) read completely. |
| `KSOA_DISCLOSURE_AND_HYPOTHESIS_LEDGER.md` | `47c8a2cacccb` | Header (lines 20–39) and `## V01 disclosure history` (lines 40–76) read completely. |
| `KSOA_CHARACTER_AND_RELATIONSHIP_LEDGER.md` | `2fd1ab0763c6` | Header and institutional-practice sections (lines 20–46) and `## V01 character and institutional state` (lines 47–75) read completely. Row `KSOA-V02-CH-0001` was read for omission checking. |
| `KSOA_CLAIM_REVISION_LEDGER.md` | `2021f91059f7` | Header (lines 20–44) and `## V01 claim history` (lines 45–62) read completely. Every other row citing V01 was also read: `KSOA-V02-CL-0001-R03` (line 72), `KSOA-V02-CL-0004` (line 78) and `KSOA-SER-CL-0005` (line 178), with the series header at line 170. |
| `studies/*.md`, `audits/*.md` | per `COMPARISON_BASIS.md` | Searched in full for every V01 reference and every omission term in §5. Lines citing V01 were read in context. These files were not read end to end, because the brief does not assign them for V01. |

### 1.2 CB1 baseline (SHA-256 prefixes; each matches its `BLIND_PACKAGE_MANIFEST.sha256` entry)

| File | SHA-256 | Completeness |
|---|---|---|
| `02_readings/V01/CB1_V01_READING.md` | `9390dc387559` | Complete, lines 1–369. |
| `02_readings/V01/CB1_V01_EXIT_STATE.md` | `0ec60b68cd84` | Complete, lines 1–113. |
| `02_readings/V01/CB1_V01_CHARACTER_EVIDENCE.md` | `e8057952edd6` | Part 2 (lines 228–319) read completely. Part 1 rows were consulted by search: CE-035, 048, 049, 059–065, 100, 119, 143, 158, 176, 179. |
| `02_readings/V01/CB1_V01_SECTION_NOTES.md` | `8a1a641d7b4c` | Consulted by search: O-0045, O-0060, O-0092, O-0134, O-0183, O-0200, O-0201. |
| `02_readings/V01/CB1_V01_FREEZES.md` (+ `_FREEZE_LOG.tsv`) | `20e3998062c0` | Consulted: F-02 line 80, F-05 H-20/H-21 lines 210–211, F-06 line 235, F-09 line 413. Freeze log read completely. |
| `02_readings/V01/CB1_V01_ENTERING_RECORD.md` | `79bec735e05e` | §3 and §8 (exposure) read. |
| `04_synthesis/CB1_CLAIM_AND_UNCERTAINTY_INVENTORY.md` | `209329dcd719` | §0, §A.1 (CL-001–006), §E, §F (the errata register: N-1, N-2, C-01–C-20), §G and §H read. Every V01-citing row in §B–§D was read (CL-045–121, U-06, U-13, U-21, U-29). |
| `04_synthesis/CB1_LONGITUDINAL_SYNTHESIS.md` | `f43f158826bd` | V01 parts read: §1 V01 row (line 48) and §3.2 V01 K-01–K-03 rows (lines 101–103). The other V01 mentions were found by search. |
| `05_monographs/CB1_GAMO_TAKASATO_MONOGRAPH.md` | `1ecd29adc570` | §§1–17 read (lines 1–386). The §§18–19 traceability tables were spot-consulted. This monograph is wholly V01. |
| `05_monographs/CB1_MONOGRAPH_QUALIFICATION_RECORD.md` | `fd98c8fdffcc` | V01 rows in §6.2 and §7 (lines 205–265) read. |
| `05_monographs/CB1_ASUMI_OGASAWARA_MONOGRAPH.md`, `CB1_MOTOYA_KITSUKAWA_MONOGRAPH.md` | `628c6ed415b3`, `daf6aa5cfe2f` | Their V01 claims were consulted through the inventory rows homed in AM and MM (§C.1–C.3). These monographs were not read end to end. Lead-monograph portraits belong to the CHAR task. |

### 1.3 Japanese source

`01_source/V01/V01_PRO.txt` (`ca1fe737b8b2`), `V01_C01.txt` (`9bbef42dde08`), `V01_C02.txt` (`8b932633f349`), `V01_C03.txt` (`701f2b7941dc`) and `V01_EPI.txt` (`e47bd721dadc`). PRO and EPI were read completely. In C01–C03 I read the passages bearing on every record and sample check: about 640 paragraphs, listed in the work notes, including C01 p0129–0245, p0303–0320, p0396–0406, p0434, p0457–0501, p0565–0589, p0600–0838, p0865–1045; C02 p0017–0105, p0227–0295, p0370–0446, p0532–0745; C03 p0058–0216, p0255–0440, p0486–0532, p0580–1204.

---

## 2. Dimension assessment

| # | Dimension | Better served | Concrete example (locators) |
|---|---|---|---|
| 1 | Source coverage | **CB1** | CB1 names the poison (KCN, [C01 p0629]), the 伏龍 background ([C02 p0566–0579]) and the will's content ([C03 p0731, p1027]). The GPT corpus contains none of the three (KCMP-V01-001, -002). |
| 2 | Narrative reconstruction | **CB1** | CB1 `CB1_V01_EXIT_STATE.md` §1 gives 30 dated story-order events, including "Sat 4 June" for the call [C03 p0887] and "Mon 6 June" for the sake and the killing [C03 p1002]. The GPT "Closeout and limits" gives the chronology in one sentence, with the specifics left to ledger rows. |
| 3 | Mystery reasoning | **Comparable; different strengths** | GPT keeps alternatives open and records adjudications at named horizons (`KSOA-V01-HYP-0001…0007`, `ADJ-0001…0005`). CB1's clue-detectability table (§F5) is better at clue level. Its paternity row is correct where GPT's omits the decisive clue (KCMP-V01-003). |
| 4 | Psychological interpretation | **Comparable** | GPT is careful about perspectival judgment (`KSOA-V01-STATE-0001`: injured pride "can obscure her effort to invite"), which is correct at [C01 p0217]. CB1 is better on narrated motive: its "fear in V01" (CL-113) matches [EPI p0061], where GPT has "in-scene concern" (KCMP-V01-012). |
| 5 | Ordinary-life detail | **CB1** | CB1 records 《そば古藤》 [C01 p1025–1037], the Thai dinner and four bars [EPI p0008–0010], McIntosh/Altec A7 [EPI p0012], 『L-O-V-E』 [EPI p0075] and the habitual からみ酒 [EPI p0018]. GPT records the refused envelope and the lunch only in summary (H-0005). |
| 6 | Relationship modeling | **Comparable** (CB1 broader, GPT more strictly horizon-bound) | GPT's directed REL rows are bounded by horizon (`KSOA-V01-REL-0001…0007`). CB1 adds edges GPT lacks: Asumi → 秀之 [C01 p0892], Takasato → 秀之 [C03 p1084], 蘆名 → staff [C03 p0717]. |
| 7 | Japanese-language analysis | **CB1**, with one GPT strength | CB1 §K inventories self-reference and address per interlocutor, plus ruby glosses such as 被害者《ガイシヤ》 [C01 p0038] and 迷宮《おみや》 [C03 p0490]. GPT is stronger on the はず analysis of PRO and on the 遺書/告白/告解 lexicon (KCMP-V01-014). GPT's policing study misromanizes 姥ヶ谷 (KCMP-V01-015). |
| 8 | Longitudinal synthesis | **Comparable** | GPT carries V01 claims forward explicitly (`KSOA-V02-CL-0004` PRESERVE V01 CL-0005-R01). CB1 carries predictions P-33–P-37 and the series state after V01. |
| 9 | Thematic interpretation | **Comparable** | GPT: "three institutions that authorize different ways of knowing a person" (Interpretation, line 180). CB1: a governing thesis paired with a live competing thesis, plus five counterreadings (§D, §N). |
| 10 | Operational reconstruction | **CB1** | CB1 records the ranks and the composition of the 50-officer 特別捜査本部 [C02 p0227–0229], the 予備班, the warrant and caution practice [C03 p0516, p0664], and the rule that theft would fall to 盗犯係 [C02 p0599]. GPT has structured ACT/INST rows with less detail. |
| 11 | Evidence traceability | **Comparable** | CB1 locators are single paragraphs with verified exact quotations, for example [C03 p0970]. GPT locators are ranges (`C01 p[0007]–p[0079]`), but each row is tied to a disclosure horizon and a predecessor. |
| 12 | Retrieval completeness | **Comparable** (purpose-dependent) | For "who knew what at H-0008", GPT's horizon records are better (`KSOA-V01-K-0005`). For "what poison", "who was the heir" or "where the 8 June meeting was", CB1 answers and GPT does not. |

**Five aspects, reported separately.**
- *Literary completeness.* CB1 is more complete on represented fact, cast and texture. GPT is more complete on staged knowledge states: what reader, investigator and witness could know at each of 14 horizons.
- *Interpretive sophistication.* Both are high. GPT leads on the ethics and institutions of disclosure (the 遺書/告白/告解 analysis; the confidential diagnosis carried to the priest). CB1 leads on detectability and on paired competing theses.
- *Source accuracy.* Both are high. GPT has two attribution or presentation errors (KCMP-V01-004, -015). CB1 has two inflation or overstatement errors (KCMP-V01-011, -016). Neither has an error about a culprit, a confession's content or a case outcome.
- *Character-reconstruction coverage.* CB1 is markedly higher. It has a full bounded monograph for 蒲生隆鄕, the leads' V01 background facts, the narratorially asserted traits and a per-interlocutor register inventory (KCMP-V01-006, -007, -008).
- *Retrieval convenience.* The two are mixed. GPT's stable anchors and ledgers suit horizon-bounded queries. CB1's dense synopsis, exit state and inventory suit fact lookup.

No overall winner is named.

---

## 3. Discrepancy register

### KCMP-V01-001 — Content of the notarized will

- **Volume / locator.** V01 C03 p0722–0751, p1019–1029.
- **Subject.** Case K-02/K-03 mechanics: what Ashina's 25 April notarized will provides.
- **GPT claim or omission.** The corpus never states the will's content. `readings/KSOA_V01_DEEP_READING.md` §KSOA-V01-H-0011 has only "a later notarized will for his lawyer" and "her own stated interests in the newer will". §KSOA-V01-H-0012 has "秀之 rejects the proposed succession identity" without saying what was proposed. Case ledger `KSOA-V01-EV-0022` says only that 亜澄 "presents and explains the later will".
- **CB1 claim.** `CB1_V01_EXIT_STATE.md` §1 row 17: "Notarized will: all to Hideyuki except ¥10m to Marina". `CB1_V01_READING.md` §F2 and §J: the will disinherits Tomita and Kazue, and Ashina "Disinherited them by the 25 April will".
- **First-pass source check.** Marina: 「すべての財産を蒲生秀之さんに相続させる」 [C03 p0731]. The foundation and the staff bequests: 「すべて反故にされます」 [C03 p0746], and her own bequest rises from ¥3m to ¥10m [p0746–0748]. Asumi reads 「四月二五日付」 aloud [p1023] and the terms [p1027]. Verified.
- **Difference type.** Fact; evidence coverage.
- **Counterevidence / alternatives.** None on the fact. GPT may have omitted specifics as a matter of style. Even so, the will is the only document in which Ashina acknowledges 秀之 as an heir. It also voids the staff-run foundation that the old will funded [C01 p0873]. Without it, 秀之's renunciation [C03 p1066] and the narration's 「公正証書は秀之の意思で破却できるものではない」 [p1068] lose their object.
- **Disposition.** `GPT_OMISSION`. The search terms are in §5.
- **Confidence.** High.
- **Correction and destination.** Add a will-content evidence row at H-0011/H-0012 and revise `KSOA-V01-RES-0002` in the **case evidence ledger**. Add a **V01 reading erratum** for H-0011/H-0012.

### KCMP-V01-002 — The poison's identity and the 特攻/伏龍 background

- **Volume / locator.** V01 C01 p0626–0629, p0709; C02 p0539–0584; C03 p0332, p0713–0714.
- **Subject.** Case K-01 means and provenance; the meaning of the title and of the PRO.
- **GPT claim or omission.** §KSOA-V01-H-0004 has "acute poisoning, with the lab's specific identification" and "the implicated agent". §KSOA-V01-H-0008 has "connects it to wartime service, fear of death and his wish that 蒲生隆鄕 read it". §KSOA-V01-H-0011 has "the wartime origin of the substance". Nowhere does the GPT corpus name the poison, the special-attack status, 伏龍, or 稲村ヶ崎 as the sortie base.
- **CB1 claim.** `CB1_V01_READING.md` §C: "the autopsy found potassium cyanide [C01 p0629]"; "trained in the 伏龍 human-mine unit, whose base was at 稲村ヶ崎". §F1 K-01: "suicide by potassium cyanide kept since summer 1945". §H: wartime history row. Inventory CL-001.
- **First-pass source check.** 「シアン化カリウム、いわゆる青酸カリ」 [C01 p0629]. Asumi had already asked whether the clinic stocked cyanide medicines [C01 p0626]. The source of the cyanide is unexplained at that horizon [C01 p0709]. The article title has 「死に損ねた特攻隊員」 [C02 p0539]. 伏龍 is a human mine [C02 p0566], and 「伏龍隊の基地は稲村ヶ崎にあった」 [C02 p0579]. The priest names 「出撃する予定の稲村ヶ崎を望むホテル」 [C03 p0332]. Marina reports 「青酸カリの粉末を入手」 in summer 1945 [C03 p0713], kept for 七七年 [p0714]. Verified.
- **Difference type.** Fact; evidence coverage; interpretation, since the PRO's 出撃 and 御国への片道きっぷ [PRO p0020, p0029] and the title acquire their referents here.
- **Counterevidence / alternatives.** GPT's abstraction may be deliberate. But "wartime service" does not tell a reader that the cape was the planned point of death. That is the link that makes the title and the PRO cohere. One dependent claim follows. GPT reads 「今度は本当におまえが先に逝ってしまったな」 [C01 p0943] as inviting "inquiry into a shared earlier past" (H-0005). After [C02 p0539] the phrase has a plain referent: Morio, the special-attack volunteer, was the one expected to die first. CB1 Gamo monograph §17 G-5 reaches this reading.
- **Disposition.** `GPT_OMISSION`. The search terms are in §5.
- **Confidence.** High.
- **Correction and destination.** A **V01 reading erratum** for H-0004, H-0008 and H-0011, plus the interpretation paragraph "A death known from the inside and from the file". Revise `KSOA-V01-EV-0005`, `-EV-0011` and `-EV-0018` in the **case evidence ledger**. Treat the cape as a wartime site in **studies/KSOA_POLICING_PLACE_AND_NARRATION.md**.

### KCMP-V01-003 — Paternity was inferable from 隆鄕's own timeline

- **Volume / locator.** V01 C03 p0063–0076, p0106.
- **Subject.** Clue detectability for the K-02 secret.
- **GPT claim or omission.** The inference table under "What the ending lets the reader infer", row "The confession concerns a wartime relationship and family identity", lists as available evidence: "The remembered coast and girl in PRO, 隆鄕's public reluctance to narrate the past, the hotel's history, and the article's addressee." It does not list 隆鄕's own timeline. §KSOA-V01-H-0009 has only "Its romantic chronology and lineage claims remain his recollection."
- **CB1 claim.** `CB1_V01_READING.md` §F5 row "Hidesato was Ashina's son": "**Fair**; inferable before the priest's account (recorded prospectively as H-20)". §E11. `CB1_V01_FREEZES.md` F-05 CB1-V01-H-20 (line 210), frozen 2026-11-15T01:07:28Z. Gamo monograph §10 item 2.
- **First-pass source check.** Tuberculosis kept 隆鄕 from 貴子 for months [C03 p0072]. They reunited at 「昭和二〇年の八月頭」, and he adds the aside 「その前に長男の秀郷を授かった」 [p0074]. 元哉 infers 「昭和二〇年の夏には男女の仲だったのだろう」 [p0076]. Morio also loved 貴子 [p0106]. Torii has already recalled Morio's stay at the hotel just before the war's end [C02 p0665]. Verified.
- **Difference type.** Evidence coverage; inference (detectability).
- **Counterevidence / alternatives.** 隆鄕 tells the conception as comedy, so its salience is low (CB1 rates it "Moderate"). The inference also needs the reader to combine it with the hotel stay. Neither point removes its availability.
- **Disposition.** `GPT_COMPRESSION`. CB1 served the detectability judgment better.
- **Confidence.** High.
- **Correction and destination.** Add a D/K row at H-0009 for the timeline clue in the **disclosure ledger**. Add a **V01 reading erratum** to the inference table. Revise `KSOA-V01-CL-0004` or add a detectability claim in the **claim ledger**. Add the point to the detectability section of **studies/KSOA_MYSTERY_FORM_AND_CAUSALITY.md**.

### KCMP-V01-004 — Who supplies the names in the priest scene

- **Volume / locator.** V01 C03 p0329–0361.
- **Subject.** Attribution of the identifications of 姥ヶ谷ホテル, 里見貴子 and 蒲生隆鄕, and the 1942 first meeting.
- **GPT claim.** §KSOA-V01-H-0010: "The priest's nested testimony identifies 里見貴子 as 蘆名's lover and places a private encounter at 姥ヶ谷ホテル on Tanabata 1945." `readings/KSOA_V01_READING_INTRODUCTION.md` §3: "He says Ashina and Takako Satomi, Gamō's wife, met at Ubagaya Hotel in 1945."
- **CB1 claim.** `CB1_V01_READING.md` §I Motoya: "capable of a leap when facts converge (naming 里見貴子 before the priest does) [C03 p0344]". CB1 does not note that Asumi supplies the hotel name.
- **First-pass source check.** The priest names neither the woman nor the hotel. He says only 「稲村ヶ崎を望むホテルの一室」 [p0332], and that the two first met three years earlier 「鎌倉海浜ホテルのパーティーで出会った」 [p0329]. 隆鄕 confirms spring 1942 [p0106]. Asumi asks 「もしかするとそれは姥ヶ谷ホテルですか」 [p0334]. 元哉 asks whether the woman is 「里見貴子さん」 [p0344], 「いままでにわかっていた事実からほかにない」 [p0348], and the priest confirms [p0350]. Asumi supplies 蒲生隆鄕 [p0357]. Verified.
- **Difference type.** Fact (attribution); presentation (the introduction's "met").
- **Counterevidence / alternatives.** The priest's 「そのことはご存じだったのですか」 [p0336] tacitly confirms the hotel, so the reading's propositional content survives. What is lost is that both detectives inferred the identifications before confirmation. That bears on 元哉's independent contributions, which are a stated theme of `studies/KSOA_MOTOYA_KITSUKAWA.md`, and on detectability (KCMP-V01-003). In the introduction, "met at Ubagaya Hotel in 1945" misdates and misplaces the first meeting.
- **Disposition.** `GPT_ERROR`, attribution and presentation. CB1 is correct on 元哉. Both omit Asumi's naming of the hotel and of 隆鄕 as a detective act.
- **Confidence.** High.
- **Correction and destination.** A **V01 reading erratum** for H-0010. A correction to **V01 reading introduction** §3. A new 元哉 STATE row in the **character ledger**. The contributions list in **studies/KSOA_MOTOYA_KITSUKAWA.md**.

### KCMP-V01-005 — Asumi's false legal claim to the priest

- **Volume / locator.** V01 C03 p0269–0283.
- **Subject.** Asumi's investigative ethics: deception as method; Japanese narration.
- **GPT claim.** §KSOA-V01-H-0010: "亜澄 asserts that a court could compel him. 元哉 corrects her in the scene, and the priest objects." The interpretation section "Three meanings of disclosure" has "亜澄 presses the distinction between the writer's public wish and the priest's obligation. 元哉 checks her claim about compulsion". `KSOA-V01-STATE-0003` has "presses confidentiality and challenges institutional caution". No GPT artifact says that the narration calls the claim false or reads her apology as feigned.
- **CB1 claim.** `CB1_V01_READING.md` §C: "Asumi falsely claims Japanese law would not protect it; Motoya knows 刑訴法149条 does". §L6: "a lie about the law to a priest". §N2 counts it as a deception. `CB1_V01_CHARACTER_EVIDENCE.md` §2.1 hedges correctly: "whether she knew Japanese law protected confession (Motoya assumes she was playing dumb)".
- **First-pass source check.** Asumi: 「我が国の法律では、司祭さまの告解は保護されていません」 [p0273]. 元哉 tugs her sleeve [p0275]. Narration: 「亜澄の言っていることはでたらめだ」, citing 刑事訴訟法第一四九条 [p0276]. The priest: 「あなたは偽りを言っている」 [p0277]. 元哉, in a low voice: 「刑訴法一四九条だ」 [p0279]. Asumi: 「不勉強ですみません」 [p0281]. Narration: 「このとぼけ方にはあきれるほかはない」 [p0283]. Verified.
- **Difference type.** Interpretation; evidence coverage (the narratorial evaluation).
- **Counterevidence / alternatives.** 「とぼけ方」 is 元哉's focalized judgment, so a knowing lie is strongly suggested but not certified. CB1's unhedged "lie" in §L6 and §N2 slightly exceeds the evidence. Its Part 2 hedge is the right formulation. GPT's wording is not false. It drops the scene's most diagnostic datum about her method, which recurs across the series (CB1 CL-077).
- **Disposition.** `GPT_COMPRESSION`, with an `INTERPRETIVE_DISAGREEMENT` dimension on whether the falsehood was knowing. CB1 is better overall.
- **Confidence.** High on the compression; moderate on "knowing".
- **Correction and destination.** A **V01 reading erratum** for H-0010 and the interpretation paragraph. A revision of `KSOA-V01-STATE-0003` in the **character ledger**. The methods section of **studies/KSOA_ASUMI_OGASAWARA.md**.

### KCMP-V01-006 — 蒲生隆鄕: character-reconstruction coverage

- **Volume / locator.** V01 C01 p0877–0953; C03 p0007–0216, p0540–0646, p1011–1162.
- **Subject.** A substantive case-local character (qualification and evidence coverage).
- **GPT claim.** `KSOA-V01-STATE-0007`: "蒲生隆鄕. Previously expresses merit ideal and grief. Continues grandfather relation after public disclosure." `KSOA-V01-EV-0013`, and mentions in H-0005, H-0009 and H-0012. No GPT row records his tuberculosis, his realist creed, the 碧素, the 内孫/外孫 remark, his misjudgment of the staff, the afterlife idiom, the remark to 和枝, the reframing of honour, or the change in his address to the detectives. No qualification decision is recorded.
- **CB1 claim.** `05_monographs/CB1_GAMO_TAKASATO_MONOGRAPH.md`, a bounded monograph (QR §5.3, `QUALIFIED_PENDING`, bounded, concentrated) with its own errata G-1–G-6.
- **First-pass source check.** 「わたしはリアリストでね」 [C03 p0063]. 「内孫でも外孫でも孫というのはかわいいもんだな」 [p0091]. 「屋敷の者では絶対にないだろう」 [p0113], which events refute. The deadpan remark to 和枝 [p0961]. 「わたしはもう九五だ」 [p1054]. 「わたしが愛した貴子の血を継いでいるのだぞ」 [p1084]. Verified.
- **Difference type.** Evidence coverage (character facts).
- **Counterevidence / alternatives.** He appears only in V01 (CB1 verified his absence from V02–V07). GPT's "case-local actor's choices … can remain substantial" principle (character ledger header) supports more coverage, not less.
- **Disposition.** `GPT_COMPRESSION`. For several facts the absence is corpus-wide (`GPT_OMISSION` dimension).
- **Confidence.** High.
- **Correction and destination.** V01 rows for 蒲生隆鄕 (PERSON, STATE, VOICE, REL) in the **character ledger**. A qualification decision in **audits/KSOA_CHARACTER_RECONSTRUCTION_READINESS.md**, which is CHAR-task scope. A possible bounded **monograph**.

### KCMP-V01-007 — The leads' background facts first disclosed in V01

- **Volume / locator.** V01 C01 p0498, p0569, p0794, p0819–0830; C02 p0042–0044; C03 p0561.
- **Subject.** Every character fact for the two leads.
- **GPT claim or omission.** `KSOA-V01-PERSON-0001` and `-0002` give rank and unit only. The V01 reading records the childhood rescue and Asumi's hospital fear. The GPT corpus places the family kimono trade first at V02 (`KSOA-V02-CH-0001`: "Asumi's perception of color comes from the family kimono trade") and Hiratsuka only in V02/V03 rows. The following are absent from the entire corpus: 《吉川紙店》, 元哉's parents at city hall, 日蓮宗, 高野山真言宗, the bully 小倉, Asumi's transfer the previous month, and her time at 厚木署盗犯係.
- **CB1 claim.** `CB1_V01_CHARACTER_EVIDENCE.md` §2.1 and §2.2, identity facts (direct). `CB1_V01_READING.md` §I. Inventory CL-072.
- **First-pass source check.** 「《吉川紙店》という文房具屋の孫」, parents 市役所勤め, and 「《かつらや》という呉服店の一人娘」 [C01 p0824]. The bully 小倉, with rescue lasting only to about age ten [p0819, p0829–0830]. 「先月鎌倉署に異動したばかり」, also from 平塚 [p0498]. 「厚木署の盗犯係」 [p0569]. 「うちは日蓮宗だよ」 [p0794]. 元哉's family temple 「高野山真言宗」 [C03 p0561]. Verified.
- **Difference type.** Fact; evidence coverage; source boundary (first-disclosure horizon misplaced to V02).
- **Counterevidence / alternatives.** GPT covers the trade and Hiratsuka from V02 on, so a series-level reader is partly served. A horizon-bounded reconstruction at V01, which GPT's own spec requires, is not.
- **Disposition.** `GPT_OMISSION` for the listed facts. The search terms are in §5.
- **Confidence.** High.
- **Correction and destination.** Revisions of `KSOA-V01-PERSON-0001` and `-0002`, with a horizon note on `KSOA-V02-CH-0001`, in the **character ledger**. **studies/KSOA_ASUMI_OGASAWARA.md** and **studies/KSOA_MOTOYA_KITSUKAWA.md**.

### KCMP-V01-008 — Asumi's narratorially asserted weakness for handsome men

- **Volume / locator.** V01 C01 p0892–0899, p0914–0920, p0988–0993; C03 p0081–0082, p0152–0153, p0185–0187, p0214, p0406–0409; EPI p0042–0044.
- **Subject.** A character trait. It bears on her investigative judgment, since 元哉 mocks her doubt about 秀之, which proves right.
- **GPT claim or omission.** Absent corpus-wide. The only trace is §KSOA-V01-H-0009: "During the grandchildren's visit, 亜澄's expressive conduct contrasts with her formal voice to their grandfather".
- **CB1 claim.** `CB1_V01_READING.md` §I: "Holds a stated ethic of not being servile to the rich [C01 p0034] — which she herself breaks when smitten by Hideyuki [C03 p0185] (counterexample)". `CB1_V01_CHARACTER_EVIDENCE.md` §2.1 "Toward handsome men". Inventory CL-087.
- **First-pass source check.** Narration: 「亜澄はイケメンに弱い」 [C01 p0899]. 元哉: 「おまえ、イケメンに甘過ぎるんだよ」 [C03 p0408], said against her correct doubt about 秀之 [p0406]. EPI: 「ほんとにイケメンには弱いヤツだな」 [EPI p0042], answered by 「こころがイケメン」 [p0044]. Verified.
- **Difference type.** Fact (narratorial assertion plus repeated conduct).
- **Counterevidence / alternatives.** Comic convention. The trait is still stated by the narration and recurs across three sections, and CB1 traces it into V02–V03.
- **Disposition.** `GPT_OMISSION`. The search terms are in §5.
- **Confidence.** High.
- **Correction and destination.** A V01 STATE/VOICE row in the **character ledger**. **studies/KSOA_ASUMI_OGASAWARA.md**.

### KCMP-V01-009 — 和枝's account of 6 June, and the open question of premeditation

- **Volume / locator.** V01 C02 p0243–0244; C03 p0974–0987.
- **Subject.** Case K-03 mechanics and the adjudication of the impulsive-encounter hypothesis.
- **GPT claim.** `KSOA-V01-EV-0020`: "和枝 admits participation and identifies 富田 as the assailant". `KSOA-V01-RES-0003`: "implicating 富田 in the assault and 和枝 in participation and removal of evidence". `KSOA-V01-CAUSE-0002`: "connect possible financial exposure to an encounter". §KSOA-V01-H-0007 opened the hypothesis "An on-site object supports an impulsive encounter as one possibility". No adjudication row revisits it.
- **CB1 claim.** `CB1_V01_LONGITUDINAL_SYNTHESIS.md` §3.2, K-03: "blow to the back of the head with a cherry branch, pushed into the pond; rucksack taken, phone thrown in the pond … proposer of the killing disputed (三村 says 富田 [p0977])". CB1 froze the same hypothesis itself: CB1-V01-H-15, "The 6 June killing was unplanned (improvised weapon)", in `CB1_V01_FREEZES.md` F-03, line 144. It never disposed of it; H-15 is absent from `CB1_V01_READING.md` §O.
- **First-pass source check.** HQ inference: the weapon was not brought, so 「計画的な犯行ではなく」 is possible [C02 p0244]. 和枝 says 富田 proposed it beforehand: 「殺すしかない」 [C03 p0977]. 富田 deflects with 「な、なにをバカなことを……」 [p0979]. 和枝: 「リュックを取ってスマホを池に捨てただけ」, and 富田 「枝で殴って池に突き落とした」 [p0981]. Verified.
- **Difference type.** Evidence coverage; inference.
- **Counterevidence / alternatives.** 和枝's statement is self-exculpatory, and the source never resolves who proposed the killing. A prior intent to kill and an improvised weapon are compatible, if a planned weapon failed or was never chosen.
- **Disposition.** `GPT_COMPRESSION`, with a `BOTH_INCOMPLETE` dimension: neither corpus adjudicates the impulsive-versus-planned question (GPT H-0007; CB1 H-15) against 和枝's claim.
- **Confidence.** Moderate to high.
- **Correction and destination.** Revisions of `KSOA-V01-EV-0020` and `-RES-0003` in the **case evidence ledger**. An ADJ row closing the H-0007 hypothesis in the **disclosure ledger**.

### KCMP-V01-010 — The place and time of 上原's 8 June appointment with 麻里奈

- **Volume / locator.** V01 C03 p0897–0905; C02 p0242.
- **Subject.** Case K-03 mechanics.
- **GPT claim.** `KSOA-V01-EV-0019`: "麻里奈 recounts 上原's June 4 call and his June 8 appointment with her". §KSOA-V01-H-0012: "Her appointment was for June 8, after his death." The place and hour are not given.
- **CB1 claim.** `CB1_V01_EXIT_STATE.md` §1 row 25: "sets 8 June 21:30 at 夫婦池公園".
- **First-pass source check.** 「六月八日水曜日の夜九時半に夫婦池公園で待ってるぜ」 [C03 p0897]. Asumi confirms: 「八日に夫婦池公園と指定してきたのですね」 [p0899]. Compare the 21:37 camera image of 上原 on 6 June [C02 p0242]. Verified.
- **Difference type.** Fact; evidence coverage.
- **Counterevidence / alternatives.** None on the fact. Its weight: 上原 used the park near the house, in the evening, for household contacts. That supports Asumi's reading that 「ＵＢＡＧＡＹＡ６／６」 records a meeting, and it explains why 麻里奈 could initially look like a candidate.
- **Disposition.** `GPT_COMPRESSION`.
- **Confidence.** High on the fact; moderate on its consequence.
- **Correction and destination.** A revision of `KSOA-V01-EV-0019` in the **case evidence ledger**.

### KCMP-V01-011 — CB1 inflates the evidence status of K-03 details: "drugged", "recorded call", "arrested"

- **Volume / locator.** V01 C03 p0891–0892, p0907–0909, p0988–0994, p1000–1006.
- **Subject.** Case K-03 mechanics and evidentiary status.
- **GPT claim.** Correct. `KSOA-V01-EV-0021`: "金上 independently reports receiving a gift from 和枝 on June 6 and going to sleep early. The suggested purpose is inferred through 元哉." §KSOA-V01-H-0012: "His aggressive register comes through her recollection and imitation". The GPT corpus says the pair were "led away" or "taken away".
- **CB1 claim.** `CB1_V01_LONGITUDINAL_SYNTHESIS.md` §1 V01 row: "三村和枝 (accomplice: drugged the driver with sake, took the rucksack, threw the phone in the pond)". §3.2 K-03: "drugged the driver 金上 with sake [p1002]". `CB1_V01_READING.md` §F5 row "Kanagami was drugged", and §E16: "Uehara's recorded call [p0891–0897] gives the extortion motive". `CB1_V01_CHARACTER_EVIDENCE.md` §2.11: "voice on Marina's recording". `CB1_V01_EXIT_STATE.md` §4: "Arrested; embezzlement exposed". The Gamo monograph §6 has "are arrested for 上原's death".
- **First-pass source check.** 金上: 「新潟のうまい酒を一升瓶でもらいました」 [p1002], asleep before nine [p1005]. The purpose is 元哉's inference, 「工作だろう」 [p1006]. No drug is mentioned. 麻里奈 imitates 上原's words: 「上原の口まねをしている」 [p0892]. The recording exists, 「すべて録音してあります」 [p0909], but it is never played. The pair are 「鎌倉署にお連れする」 and 「連行されていった」 [p0988, p0994]. No 逮捕 is stated. Verified.
- **Difference type.** Fact ("drugged"); evidence status (the purpose is inferred; the recording is reported, not heard; legal status).
- **Counterevidence / alternatives.** CB1's own exit state, §1 row 26 ("Kazue gives Kanagami sake") and row 25 ("recording (not played)"), is accurate. The errors sit in summary layers that downstream readers retrieve first. 連行 is compatible with arrest, but the text does not say so.
- **Disposition.** `CLAUDE_ERROR`.
- **Confidence.** High.
- **Correction and destination.** No GPT change, since GPT is correct. The correction is recorded for the CB1 baseline through this register and the adjudication report (CB1 is frozen).

### KCMP-V01-012 — 元哉's narrated motive in the epilogue

- **Volume / locator.** V01 EPI p0059–0074.
- **Subject.** Psychological interpretation of 元哉 → 亜澄.
- **GPT claim.** §KSOA-V01-H-0013: "He registers comfort and embarrassment, disengages, and tries to wake her for the train" and "Longstanding familiarity and his in-scene concern are supported." `KSOA-V01-REL-0004`: "felt comfort coupled with embarrassment and practical concern". No GPT artifact records the narrated reason he stays.
- **CB1 claim.** Inventory CL-113: "His care for a drunk Asumi is reliable in outcome and reluctant in motive: fear in V01". `CB1_V01_READING.md` §E18: "a hug and Motoya's self-reproach [p0067]".
- **First-pass source check.** He considers leaving her: 「このまま放って帰ろうかと思った」. Then: 「報復が怖い」, because 「またいつ亜澄と組まされるかわからない」 [EPI p0060–0061]. 「心地よく感じてしまった自分を元哉は呪った」 [p0067]. 「終電なくなるぞ」 [p0072]. Verified.
- **Difference type.** Interpretation; evidence coverage.
- **Counterevidence / alternatives.** 「報復が怖い」 is comic self-presentation and may minimize real concern, as CB1 PS §4.5 itself notes. The last-train line does show practical care. Even so, "concern" should not displace the one motive the narration actually states, and "comfort" understates a pleasure he curses himself for. GPT `STATE-0005` does say "private attraction".
- **Disposition.** `GPT_COMPRESSION`, with an `INTERPRETIVE_DISAGREEMENT` dimension.
- **Confidence.** Moderate.
- **Correction and destination.** A **V01 reading erratum** for H-0013. A revision of `KSOA-V01-REL-0004` in the **character ledger**. The V01 row of **studies/KSOA_PARTNERSHIP.md**.

### KCMP-V01-013 — Asumi's use of 大浦's confidential diagnosis

- **Volume / locator.** V01 C01 p0635–0648; C03 p0313–0323, p1038.
- **Subject.** Disclosure ethics: a promise of confidentiality, then disclosure to the priest, then a public statement.
- **GPT claim.** §KSOA-V01-H-0004: "He agrees after checking intended use." §KSOA-V01-H-0010: "亜澄 also discloses the otherwise confidential diagnosis" and "The scene exposes an ethical tension in using a confidential revelation to obtain another." GPT does not cite her explicit promise, or her public statement of the diagnosis in the chapel.
- **CB1 claim.** The rows record both acts: CE-049 ("assures confidentiality") and CE-143 ("discloses the brain tumour (confidential medical information) to him"). The synthesis omits V01. Inventory CL-076 has "Confidentiality is promised, conditionally or unconditionally, but breached when that serves the case (V03, V05)".
- **First-pass source check.** 大浦: 「捜査以外にこの情報は使うことはありませんね」. Asumi: 「よそへ漏らすことはありません」 [C01 p0646–0647]. To the priest: 「悪性の脳腫瘍」 [C03 p0318]. In the chapel, before family, staff and editor: 「グリオーマという脳のがん」 [C03 p1038]. Verified.
- **Difference type.** Interpretation; evidence coverage.
- **Counterevidence / alternatives.** Telling the priest arguably falls within 捜査 use. The chapel statement serves the case's public closure. Whether either breaches the promise is a judgment the text does not make.
- **Disposition.** `BOTH_INCOMPLETE`. GPT has the stronger interpretation. CB1 has the rows but drops V01 from its synthesis claim.
- **Confidence.** Moderate.
- **Correction and destination.** Revisions of `KSOA-V01-STATE-0003` and `KSOA-V01-INST-0003` in the **character ledger**. The confidentiality discussion in **studies/KSOA_ASUMI_OGASAWARA.md**. A CB1 note through the adjudication report.

### KCMP-V01-014 — The 遺書 / 告白 / 告解 lexicon of disclosure

- **Volume / locator.** V01 C01 p0705; C02 p0539, p0584; C03 p0263–0302, p0726, p0765.
- **Subject.** Japanese-language and thematic analysis.
- **GPT claim.** "Three meanings of disclosure": "The lost novel is presented as a 遺書 in the magazine, a public 告白 by its writer, and a translation into fiction of something first spoken in 告解." `KSOA-V01-CL-0004`; studies/KSOA_POLICING_PLACE_AND_NARRATION.md line 37.
- **CB1 claim.** `CB1_V01_READING.md` §M "Wills" tracks 遺書 across the notebook, the article, both wills and the novel. CB1 §L1 discusses the right to disclose. 告解 appears only in CE rows and section notes. The READING and the LS never contrast 告白 with 告解.
- **First-pass source check.** 「この一行を蘆名盛雄の遺書だと考えていた」 [C01 p0705]. 「最後の告白をするつもりだ」 [C02 p0584]. 「正式な告解です」 [C03 p0302]. The notarized will is called a will whose 「遺書の効力を塗り替える」 [C03 p0726]. Verified.
- **Difference type.** Interpretation; Japanese-language analysis.
- **Counterevidence / alternatives.** CB1's "Wills" motif captures the 遺書 polysemy, which GPT treats more briefly.
- **Disposition.** `CLAUDE_COMPRESSION`.
- **Confidence.** Moderate.
- **Correction and destination.** No GPT change; this is a GPT strength to preserve. CB1 note through the adjudication report.

### KCMP-V01-015 — GPT presentation errors: romanization, a role label and a date

- **Volume / locator.** V01 C02 p0017, p0162, p0223, p0240, p0269, p0400–0430; C03 p0938.
- **Subject.** Place name and wordplay; the role of 横瀬; the date of 上原's death.
- **GPT claim.** (a) `studies/KSOA_POLICING_PLACE_AND_NARRATION.md` line 45: "At Ubagayatsu a plaque and present-day use sit alongside the absence of a recovered wartime record." (b) `readings/KSOA_V01_READING_INTRODUCTION.md` §3: "A researcher tells them about the hotel's wartime use." (c) §KSOA-V01-H-0006: "a new death at 夫婦池公園 on June 7 introduces 上原尚一".
- **CB1 claim.** 姥ヶ谷 is given without a romanization error. 横瀬 is "the manager of 西光学院大学's seminar house" (§C). 上原 was "murdered 6 June" (LS §1).
- **First-pass source check.** (a) The ruby is 「｜姥《うば》｜ヶ《が》｜谷《や》」 [C02 p0269], and the wordplay depends on 「ウバガヤーとなりますね」 [C03 p0938]. "Ubagayatsu" would break the clue, and the GPT introduction itself writes "Ubagaya". (b) 「当施設マネージャーの横瀬です」 [C02 p0400], who 「個人的に調べてみた」 from a 昭和四〇年代 local-history book [p0413, p0430]. (c) 「昨夜の事件」 [C02 p0223]. The examiner's window is 昨夜 21:00–23:00 [p0240]. The 7 June date is the discovery [p0017]. Verified.
- **Difference type.** Presentation; Japanese-language (a); fact (b, c).
- **Counterevidence / alternatives.** 谷 is often read やつ in Kamakura place names, but this witness's ruby decides the reading. GPT H-0007 rightly speaks of "横瀬's research", but the introduction's label overstates his standing.
- **Disposition.** `GPT_ERROR`, low consequence except (a).
- **Confidence.** High.
- **Correction and destination.** An erratum to **studies/KSOA_POLICING_PLACE_AND_NARRATION.md** for (a). A correction to **V01 reading introduction** §3 for (b). A **V01 reading erratum** for H-0006 (c), since the freeze is immutable.

### KCMP-V01-016 — CB1 overstates the absence of narrated statements of Asumi's intention

- **Volume / locator.** V01 C02 p0644; C03 p0612, p0926, p1024.
- **Subject.** A focalization claim.
- **GPT claim.** "Mainly close third through 吉川元哉" (coverage table); Asumi's motives are treated as perspectival. GPT makes no universal negative claim.
- **CB1 claim.** `CB1_V01_READING.md` §G: "**Asumi's interiority is never narrated.** Her motives reach the reader as her own statements or as Motoya's guesses … No exception was found in V01."
- **First-pass source check.** Unhedged narration of her intentions: 「亜澄はＵＢＡＧＡＹＡについて触れるつもりだ」 [C02 p0644]. 「…証拠にできる言葉を得ようとは思っていないのだ」 [C03 p0612]. 「亜澄はわざとふたりを挑発している」 [p0926]. 「亜澄は隆鄕の許可を得ようとしている」 [p1024]. Verified.
- **Difference type.** Interpretation (focalization classification); presentation.
- **Counterevidence / alternatives.** These lines can be read as 元哉's confident free indirect inference, so CB1's broader thesis survives. The claim "no exception" without hedges does not. CB1 erratum C-03 already corrects the same overstatement at series level with a V05 example. These V01 lines show the pattern from the first volume.
- **Disposition.** `CLAUDE_ERROR`, low consequence.
- **Confidence.** Moderate.
- **Correction and destination.** No GPT change. Optional: a note on how focalized narration states Asumi's intentions in **studies/KSOA_POLICING_PLACE_AND_NARRATION.md** (narration section). CB1 note through the adjudication report.

### Record counts by primary disposition

| Disposition | Count | Records |
|---|---|---|
| `GPT_OMISSION` | 4 | 001, 002, 007, 008 |
| `GPT_COMPRESSION` | 6 | 003, 005, 006, 009, 010, 012 |
| `GPT_ERROR` | 2 | 004, 015 |
| `CLAUDE_ERROR` | 2 | 011, 016 |
| `CLAUDE_COMPRESSION` | 1 | 014 |
| `BOTH_INCOMPLETE` | 1 | 013 |
| **Total** | **16** | |

Secondary dimensions: `BOTH_INCOMPLETE` (009); `INTERPRETIVE_DISAGREEMENT` (005, 012); `GPT_OMISSION` for specific facts (006). No `CLAUDE_OMISSION` is asserted (§5).

---

## 4. Agreement sample checks (protocol §7)

| # | Stratum | Claim held by both | GPT anchor | CB1 anchor | Source verification | Result |
|---|---|---|---|---|---|---|
| A1 | Case solution | 蘆名 died by his own hand by poison, and the suicide ruling stands. | `KSOA-V01-RES-0001`; `ADJ-0001` | §F1 K-01; CL-001 | 「この薬は、なんて苦いんだ」 [PRO p0038]. Ruling and dissolution [C01 p0748–0749]. 「この判断は変わらないはずです」 [C03 p0879]. Provenance [C03 p0713]. | AGREE, confirmed |
| A2 | Case solution | 富田's role as striker rests on 和枝's accusation and 富田's non-denial. No phone recovery or verdict is shown. | `KSOA-V01-EV-0020`; `RES-0003` | CL-003; LS §3.2 | Accusation [C03 p0977, p0981]. Outburst admits the money, not the blow [p0985]. Bluff 「亜澄のハッタリだ」 [p0970]. | AGREE, confirmed |
| A3 | Clue detectability | The second reading of ＵＢＡＧＡＹＡ depends on Okinawan words supplied only at the reveal. 和枝's face and 上原's origin were planted earlier. | §KSOA-V01-H-0012; `CL-0003-R01` | §F5 row `Kazue = "Uba"; she met Uehara on 6 June` | 「赤ら顔でいくぶん横に広い輪郭」 [C01 p0135]. 「沖縄県出身」 [C02 p0232]. TV prompt and ウバ/アガヤー [C03 p0935–0938]. 隆鄕 echoes the face [p0961]. | AGREE, confirmed |
| A4 | Register | Asumi: あたし, 吉川くん/あんた with 元哉, a formal self-identification to witnesses. 元哉: sulky デカチョウ, then mock-formal デカチョウどの in praise. | `KSOA-V01-VOICE-0001`, `-0002` | §K | 「あたしは主任だよ…あんたを指導する立場」 [C01 p0055]. 「わかりましたよ。デカチョウ」 [p0057]. 「神奈川県警の小笠原です」 [p0071]. 「デカチョウどの」 [EPI p0029]. | AGREE, confirmed |
| A5 | Ordinary life | After the funeral: the refused envelope, an apology for the lost day off, and a lunch she pays for. | §KSOA-V01-H-0005 | §E7; §I | 「公務員なんで、それはご遠慮します」 [C01 p0960]. 「ごめんね。せっかくの休みを…」 [p0975]. 「あたしがおごるよ」 [p1009]. 盛りそば and tempura [p1028]. | AGREE, confirmed |
| A6 | Chronology | Two schedule discrepancies, recorded and left unresolved: the planned Saturday funeral against the Sunday funeral, and "eight days" against 7 June. | "Closeout and limits", bullet 2 | F-02 item 14; O-0092 | 「今度の土曜日に予定されているお葬式」 [C01 p0434]. Sunday [p0790, p0838]. 「八日経った六月七日火曜日」 [C02 p0017]. | AGREE, confirmed. Both corpora caught both. |
| A7 | Focalization / disclosure | Close third through 元哉. Asumi's theory and plan at the cape are withheld from the reader. | §KSOA-V01-H-0010; `KSOA-V01-K-0007` | §G; F5 | 「亜澄は自分の推理を話した」 [C03 p0503], content omitted. Plan [p0523]. | AGREE, confirmed (see 016 for a CB1 overstatement) |
| A8 | Clue detectability | The recipient's identity was conjectural before the trap, only partly fair. | Inference table row 1: "Identity was conjectural before the staged response." | §F5 row "The recipient was Marina": "**Partly fair**" | 元哉: 「犯人候補の最有力者ではあったが、これで完全に特定できた」 [C03 p0600]. The reader never had the basis. | AGREE, confirmed |

---

## 5. Omission discipline

**GPT corpus searched.** The whole of `series/kamakura-sho/`: readings and introductions for V01–V07, all four ledgers, the method, architecture, witness map and spec, `studies/*.md` and `audits/*.md`. I used `grep -r` over the tree, both case-sensitive and case-insensitive.

| Record | Terms (zero hits unless noted) |
|---|---|
| 001 | `bequ`, `inherit`, `heir`, `estate to`, `leaves` (only unrelated hits), `legacy`, `公正証書`, `notarized` (V01 reading and intro only, without content), `ten million`, `million`, `yen` |
| 002 | `青酸`, `cyanide`, `シアン`, `KCN`, `伏龍`, `Fukury`, `特攻`, `special attack`, `kamikaze`, `予科練`, `碧素` |
| 007 | `平塚` (0), `Hiratsuka` (V02/V03 readings and V03 REL only), `かつらや`, `吉川紙店`, `stationer`, `市役所`, `city hall`, `only daughter`, `一人娘`, `日蓮`, `Nichiren`, `真言`, `Shingon`, `religio` (V01 reading, unrelated), `temple` (unrelated), `厚木`, `Atsugi`, `盗犯`, `theft squad`, `transferred`, `Ogura`, `小倉`, `boyfriend`, `kimono` (V02 CH-0001 and V03 reading only) |
| 008 | `handsome`, `イケメン`, `美男`, `infatuat`, `smitten`, `good-looking`, `crush`, `attractive` (V05 reading and mystery study only, unrelated), `looks`/`appearance` (V01 hit: "元哉's immediate assessments of personality from appearance", not Asumi) |
| Supporting checks | 006: `碧素`, `penicillin`, `realist`, `tuberc`, `結核` (0). 012: `reprisal`, `retaliat` (V07 only), `curse`, `呪` (0). 004/003: `before marriage`, `premarital`, `conceiv` (V06 only), `1945` (V01 H-0010 and intro only) |

**CB1 corpus searched for possible CLAUDE_OMISSION.** The whole of `KSOA-CB1:` (02–05): `告解` and `告白` (found in CE and section notes only, hence 014 is compression, not omission); `令状`, `warrant`, `p0643`, `p0314`, `p0318`, `confidential` (CE-049 and CE-143 record the acts, hence 013 is BOTH_INCOMPLETE); `八日`, `eight days`, `Saturday`, `土曜日に予定` (both recorded, see A6); `drugg` (confirms 011's error locations). No GPT-only fact was found missing from the entire CB1 corpus, so no `CLAUDE_OMISSION` is asserted.

---

## 6. Transfer candidates

### 6.1 From CB1 to the GPT corpus (ranked)

1. **The will's content and its effects**: universal heir 秀之, ¥10m to 麻里奈, the foundation and staff bequests voided, dated 4/25 [C03 p0731, p0746, p1023–1027]. (001)
2. **The poison's identity and the 特攻/伏龍 frame**: the title, the PRO's 出撃, the cyanide's provenance, and the referent of 「今度は本当に」 [C01 p0629; C02 p0539, p0579; C03 p0332, p0713]. (002)
3. **隆鄕's timeline as a pre-reveal paternity clue**, and the detectives' own identifications in the priest scene [C03 p0074–0076, p0334, p0344, p0357]. (003, 004)
4. **The bounded 蒲生隆鄕 portrait** (CB1 Gamo monograph), with its verified address-direction errata G-1–G-6 and a qualification candidate. (006)
5. **The narratorial evaluation of Asumi's false legal claim** (でたらめ, とぼけ方) [C03 p0276, p0283]. (005)
6. **The leads' V01 background facts** and **the handsome-men trait** [C01 p0498, p0569, p0794, p0824–0830, p0899; C03 p0408, p0561]. (007, 008)
7. **K-03 mechanics**: 和枝's proposer claim and the pond disposal; the 8 June 夫婦池公園 21:30 appointment [C03 p0897, p0977, p0981]. (009, 010)
8. **元哉's narrated epilogue motive and self-curse** [EPI p0061, p0067]. (012)
9. **Ordinary-life texture** for reconstruction: 《そば古藤》, the Fujisawa bars, McIntosh/Altec, 『L-O-V-E』, the habitual からみ酒, the Sunday-summons formula 「明日の日曜日ヒマでしょ？」 [C01 p0756–0760].
10. **Minor loose ends**, worth one ledger line each: the wastebasket 薬包紙 [C01 p0188, p0356], and 富田's 「三村と松本」 against 和枝's 「あたくしが」 [C01 p0164, p0167]. CB1 exit §3 records both. GPT §KSOA-V01-H-0002 describes the discovery account as "confirmed in his presence by the other staff" without noting the inconsistency.

### 6.2 From the GPT corpus to CB1 (ranked)

1. **Horizon-bounded knowledge records** that separate reader, investigator and witness access, with receipts. For example, the pair held the autopsy and notebook before the reader did (`KSOA-V01-K-0002`), and the editor received nonpublic evidence (`KSOA-V01-K-0005`). CB1's freezes carry predictions, not per-actor knowledge rows.
2. **The 遺書 / 告白 / 告解 lexicon** and the three-institution reading of disclosure (Interpretation, lines 180 and 194–198). (014)
3. **The ethics of carrying 大浦's confidence to the priest** as a connected argument (H-0004, H-0010). (013)
4. **Custody kept distinct from theft**: 麻里奈's 「盗んでなんかいません…お預かりした」 [C03 p0615] against Asumi's later 窃盗罪 framing [p1058] (`KSOA-V01-RES-0002`). CB1 labels K-02 "theft" in §F2.
5. **横瀬 as a model of inferential restraint**, and the byline seen while others discuss publication as an example of "professional divisions of attention" becoming pacing (Interpretation, lines 190–192).
6. **Correct evidence status in K-03** (gift, imitation, "taken away") as the template for repairing 011.

---

## 7. Compression note (V01)

The GPT V01 deep reading is not short (about 53 KB, with 14 freezes). Its losses are not caused by length. They come from a consistent abstraction policy. Specific agents, sums, documents and wartime referents are replaced with functional descriptions: "the implicated agent", "wartime service", "a later notarized will", "financial misconduct", "a researcher". Most of that is economical and harmless. In four places the policy removed evidence a reader or reconstructor needs: the poison and the 伏龍 frame (002), the will's terms (001), the paternity clue in 隆鄕's timeline (003), and the narratorial verdict on Asumi's legal claim (005). The CB1 reading is denser in fact but sometimes compresses evidence status in its summary layers (011). For V01, then, the GPT reading is economical in interpretation and lossy in concrete case evidence. The fix is targeted additions to ledger rows, not longer prose.

---

## 8. Self-check

- Every GPT phrase quoted above was re-matched as a fixed string in the pinned files. The one fixed-string miss resulted from the U+F9DC ideograph in 隆鄕; I re-matched that line after normalizing the code point.
- Every CB1 phrase quoted was copied from the files listed in §1.2. Their hashes match the frozen manifest.
- Every Japanese locator in §§3–4 was opened in `01_source/V01` during this task.
- No file in either corpus was modified.
