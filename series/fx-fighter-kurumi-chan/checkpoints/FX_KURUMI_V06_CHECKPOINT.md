---
title: "FX Fighter Kurumi-chan V06 — Checkpoint"
artifact_id: FX_KURUMI_V06_CHECKPOINT
artifact_type: checkpoint
series: fx-fighter-kurumi-chan
version: "1.0"
status: canonical
checkpoint_state: frozen
authority_generation: FX_KURUMI-INITIAL
authority_scope: "Historical V06 closeout and pre-V07 knowledge boundary"
source_boundary: "FXK-JP-V06-W01 main narrative and classified apparatus (V06), with accepted state through V05; V06 unit-end knowledge; no later volume"
created: 2026-11-22
last_updated: 2026-11-22
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
run_id: FXK-RUN-20261119-V01-V10
recommended_reasoning_class: DEEP_SYNTHESIS
---

# V06 checkpoint

This checkpoint closes the V06 unit of run FXK-RUN-20261119-V01-V10 and fixes the knowledge boundary before V07. The V06 principal (Agent A) wrote it in the reconciliation session on November 22, 2026 (UTC−05:00). It records who read what, what each independent role found, how the principal disposed of every material finding and every reviewer challenge, which evidence obligations remain, the prospective freezes verbatim, the exposure record with each role's first sight of the deferred covers and jacket, the forecast tallies, the name-and-reference check, the architecture check and the exit state. The canonical reading is the [V06 deep reading](../readings/FX_KURUMI_V06_DEEP_READING.md); the pre-exposure boundary is the [V06 entering state](./FX_KURUMI_V06_ENTERING_STATE.md); the rows are in the [decision and evidence ledger](../FX_KURUMI_DECISION_AND_EVIDENCE_LEDGER.md); the witness record is the V06 coverage section of the [source register](../FX_KURUMI_SOURCE_REGISTER.md). The preceding closeout is the [V05 checkpoint](./FX_KURUMI_V05_CHECKPOINT.md).

## 1. Coverage and participation

Every role ran in its own execution context with the same source frontier (V06, with the accepted V01–V05 units as prior knowledge) and its own assignment. All V06 role sessions ran as separate Claude Code subagent contexts launched by the run coordinator, with the model inherited from the coordinator's Claude Opus 5.5 session; no reasoning-effort setting was recorded for them, and no other model setting was observed. No token counts or runtimes are recorded here because none were observed. Times are local (UTC−05:00) on 2026-11-22 and come from the roles' own records (shell `date` and file times). From V06 the entrypoint's component scope deferred the six cover and jacket occurrences (i0001, i0002, i0158, i0159, i0160, i0161) for every role until that role's release point (section 7).

| Role | Assignment | Sessions (time, pages, images) | Pages actually inspected | Exposure boundary |
| --- | --- | --- | --- | --- |
| **Principal analyst and integrator (Agent A)** | Entering state; whole-volume sequential reading with prospective freezes; candidate reading and ledger rows; reconciliation; repository transaction | S1 01:49–02:05: entering state (file time 01:53:57, before any V06 page), then i0003–i0039, 45 images (37 reading copies, 8 crops). S2 02:05–02:18, i0040–i0079, 45 (40, 5). S3 02:18–02:32, i0080–i0123, 45 (44, 1). S4 02:33–02:50, i0124–i0157, i0162–i0163 and, after MAIN_EXIT, the deferred i0001, i0002, i0158–i0161, 44 (42, 2). S5 (drafting) about 02:52–03:24, 6 reading copies re-opened. R1 (reconciliation) from 03:41, 7 reading copies and 1 crop | Every occurrence i0001–i0163 once at reading resolution, in spine order, the deferred six last; 16 crops in the reading sessions; re-openings listed above and in the reading's §A.1 | V06 and the accepted V01–V05 artifacts; deferred inputs after MAIN_EXIT (02:46) |
| **Financial, causal and information-state specialist (Agent B)** | Independent figures, decision episodes, information states, inconsistencies, money psychology; independent prospective freezes | S1 01:49–02:02, i0003–i0035, 44 images (33 reading copies, 11 crops). S2 02:02–02:16, i0036–i0073, 44 (38, 6 crop montages). S3 02:15–02:27, i0074–i0113, 44 (40, 4). S4 02:27–02:43, i0114–i0154, 44 (41, 3). S5 02:44–03:00: i0155–i0157, then after F06 (02:45:32) the deferred six, then i0162–i0163, 13 (11, 2). Freezes F00 (01:52) to F06 (02:45:32) | Every occurrence i0001–i0163 once at reading resolution, in spine order, the deferred six only after its closing freeze; figures enlarged in crops and montages | V06 and the accepted V01–V05 artifacts it read (its exposure record lists them); deferred inputs after F06 |
| **Character, relationship and Japanese-register specialist (Agent D)** | Independent per-person dossiers, speech register, directional relationships, owner hypotheses tested, counterexamples | S1 01:51–02:00, i0003–i0039, 44 (37, 7). S2 02:01–02:11, i0040–i0076, 44 (37, 7). S3 02:12–02:23, i0077–i0117, 45 (41, 2 crops, 2 stitched views). S4 02:24–02:46, i0118–i0157, i0162–i0163, 43 (42, 1 stitched view); page reading ended 02:37:20 (release point), findings §(b)–(g) drafted after it. S5 02:47–about 02:52, the deferred six, 10 (6, 4) | Every occurrence i0001–i0163 once at reading resolution, in spine order, the deferred six last | V06 and the accepted artifacts it read (the owner's brief, the method, the ledger's person section, parts of the V05 reading); deferred inputs after its release point |
| **Independent critical reviewer (Agent C)** | Stage 1: decisive pages inspected before any candidate existed. Stage 2: challenge the candidate and the specialist findings on the page | Stage 1 S1 01:49:56–02:01:25: contact sheets s01–s20 (i0003–i0082), 6 reading copies, 16 crops, 42 images. S2 02:03:26–02:19:19: sheets s21–s40, 6 crop composites, 2 reading copies, 4 crops and, after its write-up (02:15:41), the 2 deferred sheets, 34. Stage 2 03:24:53–about 03:41: 12 reading copies, 3 new crops, 2 re-views of its own crops, 17 | The whole volume on contact sheets; the decisive pages at reading resolution or in crops (its records list them) | V06 and the accepted artifacts it read; deferred sheets after its Stage 1 write-up |
| **Run coordinator** | Launches roles, holds run state, verifies and publishes | Claude Code coordinator throughout V06 | Not a reading role | Passed no page content to any role |

## 2. Execution history and repository contact

- **No interruption.** No V06 session is recorded as ending in a quota failure or restart; every role closed each session by updating its own state file. No session exceeded the 45-image cap.
- **Order of work.** Agent B completed its findings at about 03:00 and Agent D at about 02:52, in separate folders; the reviewer's Stage 1 closed at 02:19, before any candidate existed. The principal's drafting session ran from about 02:52 to 03:24 and did not open any other role's work. The reviewer's Stage 2 ran from 03:24:53 against the finished candidate and both specialists' findings. R1 began at 03:41:02.
- **Repository contact in this transaction.** The principal wrote the V06 entering state in S1, before any V06 page. In R1 it edited only the four authorized paths: the new deep reading, this new checkpoint, the ledger (targeted rows, person notes, the two boundary sentences and the front matter) and the source register (a new V06 coverage section at the end). It did not edit the entrypoint and ran no git command. A line-ending fault in the first write of the ledger and the reading (Windows line endings from the editing tool) was found by a byte comparison and corrected before read-back; the ledger's existing bytes are unchanged except the four authorized lines.

## 3. Independent findings: dispositions

Each disposition rests on the principal's own re-inspection in R1 (the seven reading copies i0010, i0044, i0115, i0124, i0137, i0147, i0154 and the crop i0143 [620,1760,1120,1980] ×2) or on the principal's own page record from the reading sessions ("own record": reading copies and crops logged in S1–S4), or on a targeted search of the accepted readings, as stated. "Agreement" marks a finding that matched the candidate and needed no change.

| ID | Finding (source) | Disposition | Reason and locator |
| --- | --- | --- | --- |
| B-1 | The complete money trail: Kurumi 21,213,915 → 19,470,915 → 18,339,915; Mebuki 2,621,530 at R = 120.450, then 0円 with an 11,000 gap; Mochiko 20,993,630 = 13,302,630 + 7,691,000; Kozue 1,005,144 → 498,302; "あと566万…とんで85円" exact (Agent B §c, §d.1) | ADOPTED (agreement) | Identical to the principal's crops (i0008, i0011, i0013, i0021, i0039, i0045–i0046, i0052, i0082, i0086, i0095–i0096) and to the reviewer's recomputation. Reading §F |
| B-2 | Kurumi's own 128円 "ありえる" scenario: CALC −25,107,000, more than her balance, unvoiced as ruin (Agent B K1 alternative (i)) | ADOPTED | R1 reading copy i0010: "ほんの一瞬だけ 128円になっちゃうみたいな…", "…ありえる!"; own record i0011 "だから今は耐えるべき…". Qualified: in her picture the spike is followed by the fall (a path risk inside her thesis). Reading §C, E006–E007, §F.1 row 1a, §G.1; C066 (reviewer C-04) |
| B-3 | The first cut is vindicated against the 121+ path of 5 Dec and regretted against 118 later (Agent B K1) | ADOPTED | R1 reading copy i0044 (NP "121円を超えてもなお 下落の気配を見せずにいた"); own crops i0045 (121.597), i0046 (callouts). CALC −5,898,000 vs −1,743,000. Reading §D.1, E008, §F.1 row 7a, §J, §L.5; C067 (reviewer C-01) |
| B-4 | Event risk used both ways in one evening: the reason to exit at 18:27 and the chance to re-enter at full size (Agent B K2 alternative (i)) | ADOPTED (EVAL MOD-HIGH) | Own record i0012 ("そんな危ない橋は渡れない"), i0031–i0034 ("絶対ここで取り返す", "全力で叩き売る"). Reading §C, E009; C068 (reviewer C-17) |
| B-5 | Her counterfactual on the V05 long reconciles exactly: 3,611,715 + (121.597 − 110.271) × 1,800,000 + 1,000,000 = 24,998,515 (Agent B K3) | ADOPTED (CALC) | Operands: accepted V05 (180枚, 120.05, +17,602,200 ⇒ average 110.271; 21,213,915 − 17,602,200 = 3,611,715) and own crop i0045; own record i0047 "なんの苦労もなく 目標(2000万円)達成できてたのに". Reading E014, §F.1 row 8; C069 (reviewer C-17) |
| B-6 | Kurumi knows Mebuki has a job (i0140) without a shown source (Agent B d.11) | ADOPTED | Own record i0140 ("あれ? 芽吹ちゃんは まだ仕事?"; Yasuko "終わったら来るってさ"); i0100 gave only "FX降りました". Reading §C, §I, §P; C070; V06-U13 (reviewer C-06) |
| B-7 | Kozue's "ここ1年 100円と90円の間" contradicts her own "103円突破" (Agent B d.4) | ADOPTED (reliability flag on her self-report) | Own record i0068 (journal 18 July 2008) and i0070 (2 September). Reading §C, E024, §F.10 (reviewer C-11) |
| B-8 | Kurumi's year curve starts in "5月" against V01's February start (Agent B d.6) | ADOPTED (kept as printed) | Own record i0048 (「30万」「5月」「12月」); accepted V01 i0044, balance 300,000 on 14 February 2014, by search of the V01 reading. Reading E014, §F.10 (reviewer C-11) |
| B-9 | The rate board's crosses are only approximate while every spread reconciles (Agent B d.3) | ADOPTED (LOW importance) | Own crop i0049; CALC 1.22867 × 121.581 = 149.383 vs 149.340; 1.55808 × 121.581 = 189.433 vs 189.355. Reading §F.10 |
| B-10 | Kozue's 10/6 settlement vs the gathered total: the caption counts the total loss, the screen one day's settlement (Agent B d.8) | ADOPTED (INF MOD; not decided) | Own record i0079–i0082; CALC 20,000,000 − 18,790,50x ≈ 1,209,49x against 1,005,144. Reading §F.10 |
| B-11 | "時価" for Kurumi's open long on a closed market can only be a pre-holiday price (Agent B C1) | ADOPTED (INF) | Own record i0140, i0144. Reading §F.8 |
| B-12 | Kurumi models path risk but not regime risk (the policy itself ending), which only Mochiko formulates, silently (Agent B K5, f.4) | QUALIFIED (INF LOW-MOD) | Own record i0127–i0135 and i0153: Kurumi's model never treats the policy as able to end (already E039, "single-point dependence"); what Mochiko's "万が一" covers is not specified. Adopted only as an omission in Kurumi's reasoning, with no outcome used (the principal declared knowledge of the policy's later history). Reading E054 |
| B-13 | The EUR/CHF action state: "発射" at i0117 vs "渡らない" at i0122; existence settled only by i0148 (Agent B d.9) | ADOPTED (agreement; strengthened by the reviewer's C-03) | R1 reading copies i0115 (announced away from the keyboard) and i0137 (decision); own record i0117–i0118, i0122. Reading §D.1, E040, §F.2 |
| B-14 | Narration order is not chronology for the narrated 8 December (Agent B d.10) | ADOPTED (agreement) | Reading E046, V06-U07 |
| B-15 | Mochiko's +7,691,000 implies the 2,000,000 loan did not leave her domestic account between V04's box and 8 December, or was offset (Agent B d.13) | OPEN | Not re-examined within reconciliation: when the loan was paid relative to the V04 box needs the V04 record. Listed in section 5 |
| B-16 | The flap's "ぴしゃぷりおじさん" most plausibly names the salon customer (Agent B d.14) | NOT USED (paratext, INF LOW-MOD) | Deferred flap i0002; the reading keeps paratext out of character evidence (E055) |
| B-17 | Agent B's own forecast dispositions (§g.3: 28 C, 19 D, 3 P of 50 non-exposure items) | QUALIFIED (re-scored literally) | Section 8: P items scored literally (F00-8 DISCONFIRMED; F00-15 and F03-3 CONFIRMED, strict DISCONFIRMED); F01-10 re-scored CONFIRMED (the customer reappears at i0035 and i0040–i0042 after the freeze at i0030; own record); F06-D literally DISCONFIRMED (the under-jacket strip's 「2020年 某月某日」, i0161) |
| D-1 | Kurumi's finger-tapping tic "トントン" (i0007) and the cutesy 「にゃんっ♪」 with "大丈夫だよ!" against her private panting (i0148 vs i0118) (Agent D b.1) | ADOPTED | Own record i0007 and i0148. Reading E006, E051, H.1 (reviewer C-16) |
| D-2 | Mother–daughter parallels are FORMAL, not causal (Agent D b.5, e.A) | ADOPTED | Matches the reviewer's C-02; the thesis no longer asserts a derivation. Reading §D.1, E030, §I |
| D-3 | "あえてしてない" contradicts her i0124 plan "こんな橋 損切りするだけ" (Agent D b.1, INF H) | REJECTED | R1 reading copy i0124: "そのときは" points back to i0123 (a clearer currency appearing in about a month); the plan is a discretionary switch-out, not a price stop, and a resting-stop refusal does not renounce it (reviewer C-18). Reading E042, E053 |
| D-4 | Yasuko "expects to be the winner": "あたしは絶対おごられるほうだしなー!" (Agent D b.4) | REJECTED | Own record i0141: the rule reads "一番勝った人から ご飯が奢ってもらえる!" (receive a treat from the winner), consistent with the accepted V03 rule that the winner treats; "おごられるほう" means she expects not to win (reviewer §2). Reading E047, H.4 |
| D-5 | "うわー "4桁万円"も儲かったんだー" / "FXって "簡単" なんだねー" have no secure speaker (Agent D b.3) | ADOPTED | R1 reading copy i0147: wavy tail-less balloons over Yasuko's face squeezed by hands, most likely Mochiko's; Yasuko MOD, Mochiko LOW-MOD. Reading E050, H.4, §I; V06-U14 (reviewer C-07) |
| D-6 | "忘却の彼方で吊るされてる記憶だね" is Mochiko's deflection (OBS H) (Agent D b.3) | QUALIFIED (INF MOD) | The drafting session re-opened i0143: balloon tails are not decisive. Kept as INF MOD Mochiko, attribution UNRESOLVED (V06-U08) |
| D-7 | Kurumi still seeks Mochiko's judgement despite the lie, "どう? 買いだと思わない?" (i0150) (Agent D b.1, d) | ADOPTED (INF MOD) | Own record i0150. Reading §I |
| D-8 | "One last trade" pattern: V05 "これで私の戦いはおしまい" and V06 "上がれば引退予定" (Agent D b.1) | ADOPTED (INF MOD-HIGH) | Own record i0148; accepted V05. Reading H.1 |
| D-9 | No enjoyment of Mebuki's misfortune by Mochiko; "ごちそうさまでした" follows her own close (Agent D b.3, e.C) | ADOPTED (agreement) | Reading E016, H.3 |
| D-10 | Mochiko's silence is a choice made with full understanding; negligence vs respect left open (Agent D e.E) | ADOPTED (agreement) | Reading E054, §I, §L.4 |
| D-11 | Mebuki's "死ぬんやな" and the bath carry self-harm connotations; UNRESOLVED, not over-read; the game idiom of exit (Agent D b.2) | ADOPTED (agreement) | Reading E004, E011, §L.2 |
| D-12 | The blurb's "FXのマイナスを取り戻すために" is not Mebuki's motive on the page (Agent D h.3; reviewer P1) | ADOPTED (agreement) | Reading E055 |
| D-13 | The loss-staging note (i0160) supports reading gag registers as framing (Agent D h.3) | NOT USED as evidence (paratext) | Recorded in the reading's apparatus classification only |
| D-14 | Ordinary-life detail for the four and Kozue (rooms, clothes, food, habits) (Agent D b.1–b.5) | ADOPTED (agreement; the reading already holds it) | Reading §H |
| D-15 | Kurumi's single "あたし" (i0153) and "やす子" / "やす子ちゃん" variation (Agent D g.9) | ADOPTED in part | "あたし" kept by placement (INF MOD-HIGH; the reviewer re-opened i0153 and agreed); the address variation not re-checked (minor) |
| D-16 | The full-resolution crop of i0158 is colour although the colour list omits it (Agent D h.2; reviewer §8) | RECORDED, not checked | Source register V06 coverage notes it as reported by two roles |

## 4. Reviewer challenges: dispositions

| Challenge | Severity | Disposition | Reason and locator |
| --- | --- | --- | --- |
| C-01 The thesis says the page punishes Kurumi's discipline in hindsight, omitting the same night's vindication | MATERIAL | ADOPTED | R1 i0044; own crops i0045–i0046. "Two clocks" in §D.1, E008, §F.1 row 7a, G.2, §J, §L.5, M.6 (V01-C011); C067 |
| C-02 The thesis asserts a derivation of Kurumi's goal, notebook and cognitions from the journal | MATERIAL | ADOPTED | The page shows parallels and frames the chapter as her reading (i0065, i0082, i0087, i0090); no page shows her taking a rule from it. "Inheritance" kept as EVAL MOD-HIGH on form. §D.1, E030, §I, M.6 (V05-C001); ledger C001, C036 |
| C-03 The EUR/CHF "commitment" placed at i0115 in the thesis and claim records | MATERIAL | ADOPTED | R1 i0115 (a pose away from the keyboard; no screen, click or fill) and i0137 (decision); own record i0117–i0118, i0122, i0148. §D.1, E040 (retitled), C020 (retitled), G.2, M.6 rows V05-C002, V03-C012, V02-C001 |
| C-04 The 128円 "ありえる" scenario missing from the synopsis, E006, §F.1 and §G.1 | MATERIAL | ADOPTED | R1 i0010. §C, E006–E007, §F.1 row 1a, §G.1; C066 |
| C-05 Rule mark misread as ⑩ | MINOR | ADOPTED | R1 crop i0143 [620,1760,1120,1980] ×2: a double circle ◎ with emphasis strokes. §A.3, §C, E048, §F.8, §P; V06-U11 first half RESOLVED; ledger D029, C024 |
| C-06 Knowledge map omits Kurumi's knowledge of Mebuki's job | MINOR | ADOPTED | Own record i0140. §C, §I, §P; C070; V06-U13 |
| C-07 "4桁万円 … 簡単" given to Yasuko without flagging the attribution | MINOR | ADOPTED | R1 i0147. E050, H.4, §I; V06-U14 |
| C-08 "first realized loss in the corpus" | MINOR | ADOPTED | Accepted V01 (no realized loss printed; V01 ends net profitable). "first printed realized loss" in §C, E007, C003; ledger D003, C003 |
| C-09 Mebuki's contest base is 613,200 (accepted V03); what is undefined is the treatment of deposits | MINOR | ADOPTED | Accepted V03 bases by search. §F.8 |
| C-10 "Chapter labels always fall on odd pages facing a separator" false for 第26話 | MINOR | ADOPTED | Own record i0004–i0005. §A.4 |
| C-11 Printed inconsistencies missing (i0048 "5月"; Kozue's range claim; i0049 as a check on 1.12) | MINOR | ADOPTED | Own records i0048, i0068, i0070, i0049. §C, E014, E024, §F.10 |
| C-12 Chronology inference rests on Mochiko's self-report | MINOR | ADOPTED | E036, E046, §F.1 row 10, §F.2, §N, C023 lowered to INF MOD |
| C-13 "minutes after Mebuki's capitulation": the close time is not printed | MINOR | ADOPTED | Own record i0051–i0052 (no time on the close or box). §D.1, §I, §P, M.6 (V05-C027); ledger C046 |
| C-14 "the first act after it is to reverse the morning's concealment" | MINOR | ADOPTED | R1 i0044; own record i0040–i0043. E012 |
| C-15 Clinical-flavoured wording ("compulsion-like", "persecutory") | MINOR | ADOPTED | E026, E030 reworded |
| C-16 Ordinary-life and self-presentation details dropped (tic; 「にゃんっ♪」) | MINOR | ADOPTED | Own records i0007, i0148. E006, E051, H.1 |
| C-17 Specialist evidence lost (the exact V05 counterfactual; event risk used both ways) | MINOR | ADOPTED | B-4, B-5 above. E009, E014, §F.1; C068, C069 |
| C-18 The i0124 exit is opportunity-conditioned, so "あえてしてない" does not reverse it | MINOR | ADOPTED | R1 i0124 with own record i0123. §C, §D.2, E042, E044 (form reading kept as EVAL), E051, E053, §F.2, §G.1, H.1, §P |
| C-19 V06-EN-10's headline CONFIRMED rests on a group-chat reply | MINOR | ADOPTED | Literal DISCONFIRMED, RELAXED CONFIRMED reported alongside; tallies recomputed (section 8). Reading §M.1; ledger F010 |
| C-20 MX06-5 should carry the EXPOSURE-SENSITIVE flag | MINOR | ADOPTED | Flag added at reconciliation; the freeze is unchanged. Reading §M, §M.4; ledger F112 |
| C-21 i0055: say whose phone it is likely to be | MINOR | ADOPTED | Own record i0055 (Mochiko's icon on a received message). §C, E020 |
| Reviewer §4 note: F09 carries no exposure declaration though the private association at i0108 preceded it | NOTE | ADOPTED | Section 7; reading §M, §Q |

No challenge was rejected. The reviewer's own Stage 1 errors, corrected in its Stage 2 review, were not imported: Yasuko's contest base (76,573, not 613,200), the speaker of "芽・吹・" (unidentified, not Mochiko) and Mebuki's implied rate at i0021 (120.450).

## 5. Unresolved evidence obligations

Carried from V01–V05 and new in V06 (reading §M.5). The V06 list is:

| ID | Obligation | Status at V06 exit |
| --- | --- | --- |
| V06-U01 | The EUR/CHF entry date, moment and rate (i0115–i0122, i0148) | OPEN; no ticket, fill, rate, tile or P/L printed; the position is attested by Kurumi's words on 25 December |
| V06-U02 | The speaker of "芽・吹・" (i0055) | OPEN |
| V06-U03 | The content of Mebuki's call home (i0044) | OPEN |
| V06-U04 | The digits hidden in "−18,790,50[…]" (i0079) | OPEN; not reconstructed |
| V06-U05 | The 11,000 gap in Mebuki's liquidation box (i0039) | OPEN; kept as printed |
| V06-U06 | The senior worker's aborted "あんたさぁ!" (i0043) | OPEN |
| V06-U07 | Whether Kurumi knew of the narrated 8 December announcement, and the order of that date relative to her night (i0138, E036, E046) | OPEN; her night is after 5 December, on or after 8 December only if Mochiko's "ノーポジ" is true |
| V06-U08 | The attributions of "忘却の彼方で吊るされてる記憶だね" / "吊るした木と一緒に持ってきて!" (i0143) | OPEN (INF MOD Mochiko / Kurumi) |
| V06-U09 | Whether Kozue's parents or 郁夫 learned of the losses before her death | OPEN |
| V06-U10 | Mochiko's withdrawals for the contest (i0144) | OPEN |
| V06-U11 | The hidden text after 「ごほうび!: 負」 (i0143) | OPEN; the mark before the new rule RESOLVED as ◎ at reconciliation |
| V06-U12 | The door-sign middle character (「ぱぱ・まま」 vs V01's 「ぱぱとまま」, i0061, i0081) | OPEN; not re-checked |
| V06-U13 | How Kurumi learned that Mebuki has a job (i0140) | OPEN; added at reconciliation |
| V06-U14 | The speaker of the "4桁万円" / "簡単" lines (i0147) | OPEN; added at reconciliation (Yasuko MOD, Mochiko LOW-MOD) |
| V06-U15 | Whether Mochiko's +7,691,000 shows that the loan never left her domestic account (Agent B d.13) | OPEN; added at reconciliation; not re-examined |
| V06-U16 | Whether the full-resolution i0158 is a colour page (two roles' report) | OPEN; structural only |

Obligations carried from earlier volumes keep the statuses in the reading's §M.5: V05-U01 and V05-U05 RESOLVED; U-05, U-06, V02-U03, V03-U03, V03-U04, V03-U09, V05-U04, V05-U08, V05-U09 and V05-U19 ADVANCED; the rest OPEN or without V06 bearing. No obligation was left unexamined for lack of images: the reconciliation session used 8 of its 45 images, and every reviewer challenge and material specialist finding received a disposition on the page or against the principal's own page record.

## 6. Prospective freezes, reproduced verbatim

The principal's freezes and the financial specialist's freezes are reproduced below exactly as written in the roles' working folders (appended by file concatenation, not retyped). They were never edited after writing. Dispositions are in the reading's §M (principal) and in section 8 and the ledger rows FXK-V06-F113–F190 (Agent B). The character specialist froze no prospect (none was required of it), and the reviewer's role has no freezes.

### 6.1 Principal freezes (Agent A)

#### Principal freeze file F01.md

# F01 — V06 principal prospective freeze (PRECAUTIONARY: possible end of 第26話 after i0025)

- Author: V06 principal (Agent A), chain session 1, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:00 (UTC−05:00) (shell `date` before writing: Sun Nov 22 01:59:56 EST 2026).
- Pages read before this freeze: i0003–i0025, each once, in spine order. NOT opened: i0026 onward; deferred i0001,
  i0002, i0158–i0161. Images this session so far: 30 (23 reading copies + 7 crops).
- Why now: i0025 (odd, left page) ends on a strong beat, "私はここで死ぬんやな…", after a visionary sequence. The next
  page (i0026, even, right) is a page turn. Whether 第26話 ends here is unknown; this freeze is precautionary and is
  written BEFORE opening i0026. No slip.

## What V06 has shown so far (i0003–i0025)
- i0003: colour opening, strip 「第6集 必勝」; i0004 colour title page; 「第26話」 label on i0005. Folio = occ − 2 (「13」 on
  i0015).
- Mebuki (named 「芽吹」 on her box, i0021), on a day near year-end (her mother asks about coming home for 年末): skips
  class, lies to her mother (school off; "就活"), says she may not come home; works a 17–24 shift at the salon as 「若葉」,
  now competent and preferring strangers' company ("今は知らん人と過ごすほうが気楽でええな"). On the night of 12月5日
  (the employment report; release ≈22:30 by the customer's "あと15分" at ≈22:15) a customer who calls himself a forex
  trader pitches FX to her; she feigns ignorance; sees >120 on his phone; her BOX: 「芽吹 FX口座残高(海外口座) 2,621,530円
  評価損益 −2,523,890円」 (43-lot short unchanged; R = 120.450 exactly; equity ≈97,640 CALC). A chart-tunnel vision; she is
  pierced by a candle; "ああ… そういうことか…"; "私はここで死ぬんやな…".
- Kurumi, on 12月5日 (phone), the day after her 120.05 fill: her 300-lot short @119.631 shows −1,752,000 (≈120.215), then
  −1,941,000 and −1,833,000; she rejects "Pattern D" (120 as waypoint) and first says "やっぱり 損切りはナシ…!" (echo of V01);
  at 18:25 her calendar flags "米雇用統計"; she argues herself into admitting the loss and at 18:27 CUTS: 「くるみ FX口座残高
  (国内口座) 19,470,915円 (−1,743,000円損切り)」 (exact). She consoles herself ("負けは経費みたいなもん", "相場で全勝なんて
  ありえない"); then a long black candle drops from above 120.3 to below 120.2: "ほら… 下がったじゃん…".
- No Mochiko or Yasuko scene yet. No dated caption box yet; dates come from Kurumi's phone (12月5日).

## Character / position states at i0025
| Person | Position / money | State |
|---|---|---|
| Kurumi | FLAT (300-lot short closed at a loss −1,743,000); balance 19,470,915円 | First realized loss in the corpus; normalizing self-talk; then sees the fall she predicted minutes after the cut (irony). Retirement talk of V05 not repeated yet. |
| Mebuki | 43-lot short (18 @112.102 + 25 @116.365), balance 2,621,530, open −2,523,890 at ≈120.45; equity ≈97,640 (CALC) | At work in the salon; has not watched the market; vision of being killed by a candle; "私はここで死ぬんやな…" (meaning UNRESOLVED: account death vs darker). Concealing FX from the customer, school-skipping and the year-end from her mother. |
| Mochiko | Long USD/JPY (V05 self-report); no V06 figure | Not yet shown in V06. |
| Yasuko | No position | Not yet shown in V06. |

## Open questions
1. Is Mebuki's short liquidated during the report (forced close, zero-cut), closed by her, or rescued by a deposit?
2. What does "私はここで死ぬんやな…" mean, and how does the page treat it (gag, account death, danger to her person)?
3. Does Kurumi re-enter (re-short) after seeing the fall? Does she retire, or re-frame her target (19.47M now)?
4. Mebuki's response to Mochiko's lie; the repayment envelope; Mochiko's and Yasuko's first V06 scenes.
5. When the chapter actually ends; whether a dated caption box appears.

## Testable forecasts (from i0003–i0025 only; literary, not market history)
Rate-path items are EXPOSURE-SENSITIVE (general real-world knowledge of December 2014 USD/JPY is held and excluded); they
are worded on page facts only.

| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F01-1 | The next page (i0026) does NOT carry a new chapter label (第27話); 第26話 continues. | MODERATE | A 「第27話」 label on i0026 or i0027. |
| F01-2 | Mebuki's 43-lot short is shown or stated as forcibly closed (ロスカット/強制決済/zero-cut, or a box showing the position gone with balance near zero) within V06. | MODERATE-HIGH (EXPOSURE-SENSITIVE) | The short is shown closed by her own choice at a price, or still open at a later printed figure after 5 December, or its fate never shown in V06. |
| F01-3 | The next printed Mebuki box (if any in V06) shows an account balance below 500,000円. | MODERATE (EXPOSURE-SENSITIVE) | Her next printed balance is 500,000円 or more. |
| F01-4 | Mebuki does not deposit her cash wages or any new money into the FX account before her short's fate is shown. | MODERATE | A deposit by Mebuki shown or stated before the short's fate is shown. |
| F01-5 | Kurumi opens a new FX position (any pair, any direction) within V06. | MODERATE | No new Kurumi position opened anywhere in V06. |
| F01-6 | Kurumi explicitly regrets the cut, or names the drop after it as bad luck/"もったいない", in speech or thought within the next 10 pages (by i0035). | LOW-MODERATE | No regret or complaint about the cut's timing by i0035. |
| F01-7 | Mochiko appears on the page (present time) within 第26話 or 第27話. | MODERATE | Mochiko absent from both chapters (present time). |
| F01-8 | The customer of i0018–i0021 does not reappear later in V06 (after this salon scene ends). | MODERATE | The same customer shown again in a later scene. |
| F01-9 | The page leaves Mebuki physically unharmed in V06 (no injury, hospitalization or self-harm act drawn or stated). | HIGH | Any drawn or stated self-harm act, injury or hospitalization of Mebuki in V06. |
| F01-10 | Kurumi learns, in V06, that Mebuki has been or is short USD/JPY. | LOW | No V06 page shows Kurumi learning of Mebuki's short. |

#### Principal freeze file F02.md

# F02 — V06 principal prospective freeze (chapter boundary, probable end of 第26話 after i0028)

- Author: V06 principal (Agent A), chain session 1, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:01 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:01:15 EST 2026).
- Pages read before this freeze: i0003–i0028, each once, in spine order. NOT opened: i0029 onward; deferred i0001, i0002,
  i0158–i0161. Images this session so far: 33.
- Why now: i0028 (even, right page) ends on Mebuki's "素人の勘です" and a black narrator panel 「雇用統計まで あと10分——」
  (caption ending "——" on an even page, the V01 chapter-end pattern). i0029 (odd, left) may carry 「第27話」. Written BEFORE
  opening i0029. No slip. F01 (after i0025) stands unedited; its F01-1 is already confirmed (no label on i0026).

## Additions since F01 (i0026–i0028)
- The customer predicts the report ends the buying turn and a "Niagara" crash, but holds his long for a spike first.
- Mebuki, after her vision, says calmly that USD/JPY will go up — against her own 43-lot short (equity ≈97,640 at
  R = 120.450, CALC) — "そんなもんありませんよ" (no evidence), "素人の勘です".
- Ten minutes to the report (≈22:20 on 12月5日, CALC from the clocks).

## Chapter map so far
- i0003 colour opening (strip 「第6集 必勝」; Mebuki wakes at 14:00); i0004 colour title page; 第26話 label on i0005;
  第26話 = i0003/i0004–i0028 if it ends here (26 pages). Folio = occ − 2 ("13" i0015, "25" i0027).

## States at the boundary
| Person | Position / money (latest printed) | State |
|---|---|---|
| Kurumi | Flat; balance 19,470,915円 after cutting the 300-lot short at −1,743,000 (18:27, 12月5日) | Realized her first loss; normalizing; saw the rate fall right after ("ほら… 下がったじゃん…"). Not yet shown deciding anything further. Target arithmetic now worse by her V05 reckoning (needs ≈4.5M more after tax if her V05 basis holds; CALC, her own figure not restated). |
| Mebuki | 43-lot short; 2,621,530 / −2,523,890 at 120.450; equity ≈97,640 (CALC) | At the salon with a customer, 10 minutes before the report; convinced the rate will rise; calm, smiling, fatalistic; "私はここで死ぬんやな…" (account death INF MOD-HIGH). |
| Mochiko, Yasuko | As at V05 exit | Not yet in V06. |

## Open questions
1. What happens to Mebuki's short at the report: liquidation, her own close, survival?
2. Does she act on her "hunch" (close the short, or even go long)? Does she deposit?
3. Kurumi's next move after the cut; does she learn anything of Mebuki?
4. Mochiko's and Yasuko's first V06 appearances; the repayment; Mebuki's response to the lie.

## Testable forecasts (from i0003–i0028; literary; rate-path items EXPOSURE-SENSITIVE)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F02-1 | 「第27話」 is printed on i0029 or i0030. | MODERATE-HIGH | No 第27話 label on i0029 or i0030. |
| F02-2 | 第27話 (or the pages after i0028) shows the result of the employment report for Mebuki's account (a box, tile or explicit statement of her position's fate) within its first 10 pages. | MODERATE | No statement or figure of her position's fate within the 10 pages after i0028. |
| F02-3 | Mebuki acts on her "hunch" by placing an order (closing the short, or buying) before or at the report. | LOW-MODERATE | No order by Mebuki shown or stated at or before the report. |
| F02-4 | Mebuki's account is shown at or near zero (balance under 100,000円, or "強制ロスカット"/zero-cut named) in V06. | MODERATE (EXPOSURE-SENSITIVE) | A later printed balance of 100,000円 or more with the short closed by her choice, or the short still open at V06's end, or no such statement. |
| F02-5 | Kurumi appears again on the night of 12月5日 after the report (a scene on the same night). | LOW-MODERATE | Kurumi's next scene is on a later day. |
| F02-6 | Mochiko appears (present time) within the first chapter after i0028. | MODERATE | Mochiko absent from that chapter. |
| F02-7 | Mebuki tells someone (Yasuko, Kurumi or Mochiko) about her account's fate in V06. | MODERATE | No such telling in V06. |
| F02-8 | Mebuki mentions or thinks about Mochiko's lie or the "アホ" remark in V06. | MODERATE | No reference by Mebuki to the lie/remark in V06 (same disconfirmer as V05-MX-5, here scoped to thought as well as speech). |

#### Principal freeze file F03.md

# F03 — V06 principal prospective freeze (PRECAUTIONARY: strong beat at i0039, 9 pages into 第27話)

- Author: V06 principal (Agent A), end of chain session 1, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:04 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:03:59 EST 2026).
- Pages read before this freeze: i0003–i0039, each once, in spine order (i0029–i0030 separators). NOT opened: i0040
  onward; deferred i0001, i0002, i0158–i0161. Session 1 used its full 45-image budget; i0040 will be opened by the next
  session, after this freeze.
- Why now: i0039 (odd, left page) ends on "終わった——" and Mebuki's forced liquidation to 0円. 第27話 began at i0031, so a
  chapter end here is improbable (LOW), but the beat is strong; this freeze is precautionary. No slip.

## Additions since F02 (i0029–i0039)
- i0029–i0030: black separator pages (logo bottom-left on the odd page, bottom-right on the even page). 第26話 =
  i0003/i0004–i0028. 「第27話」 on i0031 with V06's first caption date: 「2014年12月5日金曜日」「22時23分——」.
- Kurumi (flat, 19,470,915円): "170万円も負けてこのまま終わるわけにはいかない…", "絶対ここで取り返す"; "yesterday's"
  short was too early; the rise must end today; she expects an initial spike at the 22:30 report and means to "全力で
  叩き売る" into it (intended; no order shown yet). She imagines the spike as the death-cry of shorts and a "grave marker"
  before the crash — unknowingly including Mebuki.
- Salon (captions 22時28分, 22時29分): the customer backs Mebuki's hunch with 2 more long lots ("責任は僕にあるから"); the
  rate drops before the release, then at 22:30 a white candle shoots past 120.6 toward 121 ("神ktkr!!"). Mebuki had
  "hoped a little". BOX: 「芽吹 FX口座残高(海外口座) 0円 (−2,610,530円 強制ロスカット)」 — printed loss and prior balance
  differ by 11,000 (kept as printed). Image: Mebuki lying still, clothed, in a full bathtub in a ruined tiled room
  (symbolic register likely; UNRESOLVED), "終わった——".

## States at i0039
| Person | Position / money (latest printed) | State |
|---|---|---|
| Kurumi | Flat; 19,470,915円; poised to short all-out on the report's spike (no order yet) | Loss-chasing intent ("取り返す"); hindsight: right direction, wrong timing. Does not know about Mebuki. |
| Mebuki | Overseas account 0円 after a forced liquidation (−2,610,530); still owes 2,000,000 to Mochiko at 109.5% (6,000/day), cards ≈300,000, student loan 300,000 (accepted V04–V05); cash wages kept, not deposited (V05) | "終わった——"; at work in the salon; symbolic drowning image. Her "hunch" that the rate would rise was right. |
| The customer | 7 lots long (5 + 2, CALC) | Riding the spike; accepted "responsibility" for following her hunch. |
| Mochiko, Yasuko | As at V05 exit | Not yet in V06. |

## Open questions
1. Does Kurumi actually short the spike (size, price), and with what result?
2. What does Mebuki do now: quit FX, tell anyone, confront Mochiko, deal with the debt (the loan's repayment), go home for 年末?
3. Is the bathtub literal? How does the page treat Mebuki's welfare after "私はここで死ぬんやな…" and "終わった——"?
4. Mochiko's reaction to Mebuki's liquidation (her "元金回収" worry of V05).

## Testable forecasts (from i0003–i0039; literary; rate-path items EXPOSURE-SENSITIVE)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F03-1 | i0040 does not carry a chapter label; 第27話 continues. | HIGH | A 「第28話」 label on i0040 or i0041. |
| F03-2 | Kurumi submits a USD/JPY sell order at or after the 22:30 report, shown by an order box or explicit statement, within 第27話. | MODERATE-HIGH | No Kurumi sell order shown or stated in 第27話. |
| F03-3 | If Kurumi shorts on 5 December, her stated size is 300 lots or more. | LOW-MODERATE | A stated size below 300 lots (or no size printed counts as not triggered). |
| F03-4 | Mebuki tells Mochiko, in V06, that her account was wiped out or that she cannot repay on time. | MODERATE | No V06 scene in which Mebuki tells Mochiko of the wipe-out or of difficulty repaying. |
| F03-5 | Mochiko learns of Mebuki's forced liquidation in V06 (shown or stated). | MODERATE | No V06 page shows or states Mochiko knowing of it. |
| F03-6 | Mebuki states, in V06, that she will stop or has stopped trading FX (やめる/引退 or equivalent). | MODERATE | No such statement by Mebuki in V06. |
| F03-7 | Mebuki makes a new deposit into an FX account in V06. | LOW | No deposit by Mebuki shown or stated in V06. |
| F03-8 | Yasuko is shown in V06 present time learning of Mebuki's wipe-out (from Mebuki or another). | LOW-MODERATE | No V06 page shows Yasuko learning of it. |

#### Principal freeze file F04.md

# F04 — V06 principal prospective freeze (chapter boundary, probable end of 第27話 after i0054)

- Author: V06 principal (Agent A), chain session 2, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:10 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:09:34 EST 2026).
- Pages read before this freeze: i0003–i0054, each once, in spine order. NOT opened: i0055 onward; deferred i0001, i0002,
  i0158–i0161. Images this session so far: 19 (15 reading copies i0040–i0054 + 4 crops).
- Why now: i0054 (even, right page) is a full-page panel ending on Mochiko's "やっと人間(まとも)になったじゃん", 24 pages
  into 第27話 (i0031–i0054; 第26話 ran 26 pages). The next spread may begin with separators or a 「第28話」 label. Written
  BEFORE opening i0055. No slip. F01–F03 stand unedited.

## Additions since F03 (i0040–i0054)
- Mebuki (5 Dec, salon): calm after the liquidation — "肩の荷が下りて スッキリしたような——"; the customer takes profit,
  thanks "若葉ちゃん"; she spanks him (service gag, after an anger mark), "爆益 おめでとうございます"; "働くのも 案外ええもん
  やな…". Leaving, the long-haired senior worker starts "あんたさぁ!" and drops it. On the street Mebuki phones her mother:
  "お父さん起きとる? 話したいことがあんねんけど" (content not shown). Narrator: USD/JPY, past 121, showed no sign of falling.
- Kurumi (5 Dec, night): sold 300 lots USD/JPY at 121.220 after the release and cut at 121.597 (tile "現在値 121.597円"):
  BOX 「くるみ FX口座残高(国内口座) 18,339,915円 (−1,131,000円損切)」 (CALC ✓). "2日で280万円負け"; regret for taking the
  V05 profit ("1760万円程度の利益で喜ぶんじゃなかった", "目標(2000万円)達成できてたのに"); then "口座にはまだ1800万円",
  "私はまだお金持ち", "「損小利大」を間違いなく実現できている!", "次に大きく勝てば なにも問題ない", "ドル円ばかりにこだわる
  必要もない", "通貨(戦場)はほかにもあるんだよ" over a six-pair rate board (USD/JPY 121.581/121.584 etc.). No order yet.
- Mochiko (12月8日 月曜日 早朝): Mebuki's chat — earlier "今日3万円振り込みました"; today 8:08 "金曜にロスカットされて
  借りたお金全部溶かしました 退場です". Mochiko: "そっか 芽吹ちゃん死んじゃったか"; closes all buy positions: BOX 「萌智子
  FX口座残高(国内口座) 20,993,630円 (+7,691,000円利益確定)」 (= V04's 13,302,630 + 7,691,000, CALC ✓); replies "了解 お疲れ",
  "返済はゆっくりでいいからね"; worries Mebuki may have quit work and can't repay; Mebuki: "色々言いたいことはありますけど
  まずは本気で働いて借金返してからにします それまで待っていてくださいね"; Mochiko, hair let down, cat at heel: "やっと人間
  (まとも)になったじゃん".

## Chapter map so far
- i0003 colour opening (strip 「第6集 必勝」); i0004 colour title; 第26話 label i0005; 第26話 = i0003/i0004–i0028;
  separators i0029–i0030; 第27話 label i0031; 第27話 = i0031–i0054 if it ends here (24 pages). Folio = occ − 2.

## States at the boundary
| Person | Position / money (latest printed) | State |
|---|---|---|
| Kurumi | Flat; 18,339,915円 after two consecutive 300-lot USD/JPY short stop-losses (−1,743,000 on 5 Dec 18:27; −1,131,000 on 5 Dec night) | Regrets the V05 profit-take, not the cuts; reframes the cuts as "損小利大"; intends to win big next, possibly in another pair. Does not know of Mebuki's short or wipe-out, nor of Mochiko's close. |
| Mebuki | FX account 0円 (forced liquidation 5 Dec); debt to Mochiko 2,000,000 at 109.5% (accepted), one 30,000 transfer shown; cards / student loan (accepted) | "退場です"; commits to "本気で働いて借金返して"; relief; called her parents with "something to talk about" (unknown). Has not spoken of the lie explicitly. |
| Mochiko | Flat (all buys closed 8 Dec); 20,993,630円 (+7,691,000 realized) | Knows Mebuki is wiped out; lenient repayment message; private approval "やっと人間になったじゃん". |
| Yasuko | No position (accepted) | Not yet in V06. |
| Kurumi's father | Transfer "年明けから" (accepted) | Not yet in V06. |

## Open questions
1. What does Mebuki tell her parents? Does she go home, quit university or reveal the debt?
2. Kurumi's next trade: pair, direction, size, result; does she retire again or chase further?
3. Does Mochiko re-enter the market? Does she tell anyone of Mebuki's wipe-out?
4. Yasuko's first V06 appearance; her manga/design thread.
5. Whether the contest (to 25 Dec) or year-end/Christmas enters V06.

## Testable forecasts (from i0003–i0054; literary; no real-market knowledge used)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F04-1 | A 「第28話」 chapter label is printed on one of i0055, i0056 or i0057. | MODERATE-HIGH | No 「第28話」 label on any of i0055–i0057. |
| F04-2 | At least one black logo separator page falls between i0054 and the first page carrying 「第28話」. | MODERATE | The 「第28話」 label appears with no separator page between it and i0054, or no 第28話 label appears in V06. |
| F04-3 | Kurumi opens a position in a currency pair other than USD/JPY within V06 (order, box, chart annotation or explicit statement). | MODERATE | No non-USD/JPY position by Kurumi shown or stated in V06. |
| F04-4 | Kurumi's next opened position in V06 has a printed or stated size of 300 lots or more. | MODERATE | Her next opened position's printed or stated size is below 300 lots. (If she opens none, or no size is printed or stated, the item is scored OPEN, not confirmed.) |
| F04-5 | The next Kurumi balance printed in V06 after i0046 is lower than 18,339,915円. | MODERATE | The next printed Kurumi balance after i0046 is 18,339,915円 or higher. (No further printed balance → OPEN.) |
| F04-6 | Mebuki's call to her parents is shown or reported in V06 with content that includes her debt, her FX losses, or leaving university. | LOW-MODERATE | The call's content is shown or reported in V06 without any of these, or its content is never shown or reported in V06. |
| F04-7 | Mochiko opens a new FX position (any pair, any direction) in V06, shown or stated. | MODERATE | No new Mochiko position shown or stated in V06 after i0052. |
| F04-8 | Yasuko appears on the page in present time within the chapter that follows i0054. | MODERATE | Yasuko absent (present time) from that whole chapter. |
| F04-9 | Kurumi learns, in V06, that Mebuki's account was wiped out (shown or stated). | LOW-MODERATE | No V06 page shows or states Kurumi knowing of Mebuki's wipe-out. |
| F04-10 | Mochiko tells Kurumi or Yasuko, in V06, of Mebuki's wipe-out. | LOW | No V06 page shows Mochiko telling Kurumi or Yasuko of it. |

#### Principal freeze file F05.md

# F05 — V06 principal prospective freeze (SUPPLEMENTARY: actual end of 第27話 at i0055; before the next chapter)

- Author: V06 principal (Agent A), chain session 2, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:11 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:10:45 EST 2026).
- Pages read before this freeze: i0003–i0056, each once, in spine order. NOT opened: i0057 onward; deferred i0001, i0002,
  i0158–i0161. Images this session so far: 21.
- Why now: F04 was written after i0054, but 第27話 actually ended one page later, on i0055 (odd, left); i0056 is a black
  logo separator (logo bottom-right). i0057 may be a second separator or carry 「第28話」. This supplementary freeze records
  i0055 and is written BEFORE opening i0057. Disclosure: F04 preceded i0055, the last page of 第27話 — no next-chapter page
  had been opened, so this is not a slip. F04 stands unedited and remains the principal boundary freeze; F05 adds to it.

## Additions since F04 (i0055–i0056)
- i0055: a phone on a wooden surface shows Mochiko's reply "頑張ってね"; in a room with a shelf of small jars and a white-
  draped bed or table, an off-panel voice says, emphatically, "芽・吹・" (her real name, not 若葉). Speaker not shown.
- i0056: separator. 第27話 = i0031–i0055 (25 pages).

## States: as F04, plus
- Mochiko → Mebuki (chat): "了解 お疲れ", "返済はゆっくりでいいからね", "頑張ってね" (lenient, encouraging on the surface).
- Mebuki is being called by her real name by someone unidentified, in a room that may be the salon's treatment room
  (INF LOW-MOD) or elsewhere.

## Testable forecasts (supplementing F04; F04-1 and F04-2 remain as frozen)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F05-1 | i0057 is a second black logo separator page (logo bottom-left), and 「第28話」 is printed on i0058. | MODERATE | i0057 is not a separator, or 「第28話」 is not printed on i0058. |
| F05-2 | The speaker of 「芽・吹・」 (i0055) is identified in V06 as a member of Mebuki's family (mother, father or sibling). | LOW-MODERATE | The speaker is identified in V06 as someone outside Mebuki's family, or is never identified in V06. |
| F05-3 | The speaker of 「芽・吹・」 (i0055) is identified in V06 as Yasuko. | LOW | The speaker is identified as anyone other than Yasuko, or is never identified in V06. |
| F05-4 | The first chapter after i0055 opens on (or within its first five pages returns to) the 「芽・吹・」 scene. | LOW-MODERATE | The 「芽・吹・」 situation (same speaker addressing Mebuki in the same room) is not shown within the first five pages of the next chapter. |
| F05-5 | Mebuki repays Mochiko in full (principal 2,000,000 or a stated "全額"/"完済") within V06. | LOW | No full repayment shown or stated in V06. |

#### Principal freeze file F06.md

# F06 — V06 principal prospective freeze (PRECAUTIONARY: possible end of 第28話 after i0079; end of session 2)

- Author: V06 principal (Agent A), end of chain session 2, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:17 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:16:46 EST 2026).
- Pages read before this freeze: i0003–i0079, each once, in spine order. NOT opened: i0080 onward; deferred i0001, i0002,
  i0158–i0161. Session 2 used its full 45-image budget; i0080 will be opened by the next session, after this freeze.
- Why now: i0079 (odd, left page) ends the flashback's crash on "当日決済損益 −18,790,50[…]" beside the 「FXトレード日誌」,
  23 pages into 第28話 (label on i0057). 第26話 ran 26 pages and 第27話 25; a chapter end at i0079 or within the next few
  pages is possible. Precautionary; no slip. F01–F05 stand unedited.

## Additions since F05 (i0057–i0079)
- 第28話 (label i0057) is a flashback narrated by captions and by Kurumi's mother's journal. 1998年4月: the 外為法 amendment
  ("金融ビッグバン"); "FXの始まりである"; a small Kurumi asks "ママ なに買ったの?" about a 「Windowda 95」 PC. 2005年7月
  regulation; "空前のFXブーム". The mother scorns a poster "FX投資術 寝てるだけで、どんどん増える!" ("そんな美味しい話
  あるわけないでしょ") but buys the book.
- 2006年5月: Kurumi (middle school) finds goodbyes "ダサい"; the mother: "あらあら反抗期♡". Names: husband 「郁夫(いくお)さん」;
  mother 「梢(こずえ)」 (fantasy line, then narrator "くるみの母・梢"; passbook 「福賀 梢 様」). Motives: Kurumi now in middle
  school; "なにかやっときたい"; mum-friends' pressure; "お金はあるに越したことはない"; a second child, a house with a garden,
  a Sheltie; surprising 郁夫. Starts 「FXトレード日誌」 (the notebook Kurumi found in V01). Yen-carry: buy high-interest AUD.
- 2006–2008: steady profits (cake for Kurumi); TV "FX長者"; belief that rate gaps and yen weakness would last
  ("彼女は信じていた"). Journal 2008年7月18日: "豪ドル円、103円突破!", Kurumi's lunchbox made luxurious; "すごい…! FXすごい…!"
- 2008年9月2日: "初心者卒業かも!"; the fall to 90 a "バーゲンセール" (a year's 90–100 range); "ここで買えば みんな幸せに
  なれる"; plans to move all her pre-marriage savings into FX. 9月5日: 85円台, "90円台で買い過ぎてしまった", fears
  強制ロスカット, "家のお金を入金して耐えるしかない". 9月16日: 82円台, "リーマン・ブラザーズ破綻のせい?", 含み損 over 600万円,
  "こんなこと誰にも言えない… 息が苦しい…"; lies to Kurumi ("体調悪くて"); house neglected; buys more on a dip; craves
  ("買いたい…!!!"); passbook drained to *0. Gathers money: cancelled insurance, the home down-payment, cash taken from her
  parents' safe (inset; behind their backs, INF MOD-HIGH). 9月29日: "かき集めたお金を全て投入して豪ドルを買った…
  あとはもう、祈るだけだ". 10月6日: AUD/JPY 71.256/71.271; "80円から71円まで下落"; 「当日決済損益 −18,790,50[…]」.

## States at i0079
| Person | Position / money (latest printed) | State |
|---|---|---|
| Kozue (flashback, 6 Oct 2008) | AUD/JPY long(s) settled at a realized day loss of −18,790,50[…] (last digit(s) hidden); household account 0; insurance cancelled; parents' cash taken | Concealing everything from husband, daughter and parents; distressed. Accepted backdrop: dead since 13 Feb 2009. |
| Kurumi (present, last seen 5 Dec) | Flat; 18,339,915円 | Seeking a big win, perhaps in another pair (i0049). |
| Mebuki (present, last seen 8 Dec) | FX account 0; debt to Mochiko | Working; committed to repay; called by her real name ("芽・吹・") by someone unidentified (i0055). |
| Mochiko (present, 8 Dec) | Flat; 20,993,630円 | Knows of Mebuki's wipe-out; "やっと人間になったじゃん". |
| Yasuko | — | Not yet in V06. |

## Open questions
1. Does the flashback continue to Kozue's death (13 Feb 2009, accepted), or return to the present at the chapter end?
2. Who frames the flashback in the present — is Kurumi reading the 日誌, or is it pure narration?
3. Is Kozue's taking of her parents' money, and the realized loss, ever disclosed to 郁夫 or Kurumi on the page?
4. Present-time threads: Kurumi's next trade; Mebuki's caller; Yasuko's first V06 appearance.

## Testable forecasts (from i0003–i0079; literary; no real-market knowledge used; the accepted V01–V05 backdrop of the
mother's death is prior knowledge, not a forecast)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F06-1 | i0080 does not carry a chapter label and is not a separator page; 第28話 continues on i0080. | MODERATE | i0080 is a logo separator page, or a 「第29話」 label is printed on i0080. |
| F06-2 | The 第28話 flashback depicts or states Kozue's death, or the day of 13 February 2009, before 第28話 ends. | LOW-MODERATE | 第28話 ends without depicting or stating her death or that date. |
| F06-3 | Before 第28話 ends, the page shows Kozue telling (or being discovered by) 郁夫 about the FX loss. | LOW-MODERATE | 第28話 ends with no scene in which 郁夫 learns of the loss from her or discovers it. |
| F06-4 | 第28話 returns to present time (2014) before it ends, with Kurumi on the page. | MODERATE | 第28話's last page is still in the 2008–2009 past, or its present-time return shows no Kurumi. |
| F06-5 | In V06 present time, Kurumi reads or handles the 「FXトレード日誌」 on the page. | LOW-MODERATE | No V06 present-time panel shows Kurumi reading or handling the 日誌. |
| F06-6 | The exact final digit(s) of the "−18,790,50[…]" figure are printed legibly somewhere later in V06. | LOW | No later V06 page prints the full figure. |

#### Principal freeze file F07.md

# F07 — V06 principal prospective freeze (PRECAUTIONARY: possible end of 第28話 after i0088)

- Author: V06 principal (Agent A), chain session 3, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:21 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:20:54 EST 2026).
- Pages read before this freeze: i0003–i0088, each once, in spine order. NOT opened: i0089 onward; deferred i0001, i0002,
  i0158–i0161. Images this session so far: 9 (reading copies i0080–i0088; no crops).
- Why now: i0088 (even, right page) is a wordless full page — a journal page obliterated by black scribble and torn —
  following the journal entry "消えたい。。。" (i0087). 第28話 has run 32 pages since its label (i0057), longer than
  第26話 (26) and 第27話 (25). A chapter end here is possible. Precautionary; no slip. F01–F06 stand unedited.

## Additions since F06 (i0080–i0088)
- i0080: caption in Kozue's first person: "すべてのポジションが強制ロスカットされた。" / "私は1900万円もの大金を失ってしまった。"
  (F06-1: no label, not a separator — 第28話 continued.)
- i0081: Kurumi (middle school) bangs on the 「ぱぱ・ままのへや♡」 door: "ごはんまだー?", "今日もしんどいのー?"; silence;
  the room is littered; Kurumi will use the fridge herself.
- i0082: "取り返さなきゃ" ×6; tile 「口座残高 1,005,144円」; "かき集めた2000万円が たったの100万円に…", "郁夫さんにバレたら
  一家離散よ…", "もう悠長に金利狙ってる場合じゃないわ…".
- i0083–i0084: plan: short-term trading at up to 400× leverage ("100万円×400倍 = 4億円"; footnote: no leverage limit in
  Japan in 2008); heroic squid-hunt fantasy; "100枚売り" on AUD/JPY; "もう円安の時代は終わったのよ".
- i0085: Kurumi makes a failed "プリン雑炊", then a "普通の雑炊", and calls her mother.
- i0086: the rate climbs; tile 「口座残高 498,302円」 ("半分になっちゃった…", "50万円も大金なのに…").
  ANALYST CALC: 1,005,144 − 498,302 = −506,842.
- i0087: journal 10/13 (a win; "必ず2000万円取り返さなきゃ"), 10/14 ("損切りしなければ勝っていた。でも損切りしないと
  ダメらしい。"), 10/16 ("買うと下がる。売ると上がる。… 世界に監視されているとしか思えない!!"), 10/20 ("もう損切り
  したくない。家族になんて謝ればいいかわからない。消えたい。。。").
- i0088: a journal page scribbled over and torn; no text.

## States at i0088
| Person | Position / money (latest printed) | State |
|---|---|---|
| Kozue (flashback, late Oct 2008) | 口座残高 498,302円 (i0086); ≈1900万円 lost to forced liquidation (i0080); household account 0, insurance cancelled, parents' cash taken (i0075–i0077) | Repeated losses; resents stop-losses; guilt toward the family; concealment from 郁夫 ("バレたら一家離散"); "消えたい". Accepted backdrop: dead 13 Feb 2009 after ≈2000万円 household loss. |
| Kurumi (flashback) | — | Middle-schooler cooking for herself, irritated by her mother's absences; unaware of the losses. |
| Kurumi (present, last seen 5 Dec 2014) | Flat; 18,339,915円 | Seeking a big win, perhaps in another pair (i0049). |
| Mebuki (present, last seen 8 Dec) | FX account 0; debt to Mochiko | Working; committed to repay; called "芽・吹・" by someone unidentified (i0055). |
| Mochiko (present, 8 Dec) | Flat; 20,993,630円 | Knows of Mebuki's wipe-out. |
| Yasuko | — | Not yet in V06. |

## Open questions
1. Does the flashback reach Kozue's death, and is a cause stated or shown?
2. Is the flashback framed in the present (Kurumi reading the 日誌), and does the adult Kurumi react to it?
3. Do 郁夫 or Kozue's parents learn of the loss in the flashback?
4. Present threads as in F06.

## Testable forecasts (from i0003–i0088; literary; no real-market knowledge used; F06 items remain as frozen)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F07-1 | i0089 is neither a black logo separator page nor a page carrying a 「第29話」 label; 第28話 continues on i0089. | LOW-MODERATE | i0089 is a logo separator page, or 「第29話」 is printed on i0089. |
| F07-2 | Before 第28話 ends, a page shows Kozue's journal with an entry dated in 2009, or states the date 2009年2月13日. | LOW-MODERATE | 第28話 ends with no journal entry dated 2009 and no statement of 2009年2月13日. |
| F07-3 | Before 第28話 ends, the adult (2014) Kurumi appears on the page holding, reading or reacting to the 「FXトレード日誌」. | LOW-MODERATE | 第28話 ends with no panel of the adult Kurumi holding, reading or reacting to the 日誌. |
| F07-4 | Before 第28話 ends, Kozue's printed account balance (口座残高 tile, screen or caption) falls below 100,000円. | LOW | No printed Kozue balance below 100,000円 appears before 第28話 ends. |
| F07-5 | 第28話 ends without showing 郁夫 learning of Kozue's FX losses while she is alive. | MODERATE | A 第28話 page shows 郁夫 told of, or discovering, her FX losses while she is alive. |

#### Principal freeze file F08.md

# F08 — V06 principal prospective freeze (PRECAUTIONARY: possible end of 第28話 after i0090)

- Author: V06 principal (Agent A), chain session 3, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:22 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:21:42 EST 2026).
- Pages read before this freeze: i0003–i0090, each once, in spine order. NOT opened: i0091 onward; deferred i0001, i0002,
  i0158–i0161. Images this session so far: 11 (reading copies i0080–i0090; no crops).
- Why now: i0090 (even, right page) returns to the present: the adult Kurumi, in tears, holding the 「FXトレード日誌」,
  says "お母さん" / "次は絶対勝つからね". 第28話 has run 34 pages (label i0057). A chapter end here is plausible (第26話
  ended on an even page). Precautionary; no slip. F01–F07 stand unedited.

## Additions since F07 (i0089–i0090)
- i0089: journal 「2008年10月23日(木) 今日も負け 負け!負け!負け!! 負け!!」, then scribbled over (i0088|i0089 form an
  opening of defaced pages). F07-1 confirmed.
- i0090: present-time Kurumi reads the 日誌, weeping: "お母さん", "次は絶対勝つからね".

## States at i0090
| Person | Position / money (latest printed) | State |
|---|---|---|
| Kurumi (present; date not shown on i0090) | Flat; 18,339,915円 (last printed, i0046) | Has read (at least) her mother's 2008 journal; weeping; vows to win "next time". Seeking a big win, perhaps in another pair (i0049). |
| Kozue (flashback, last dated entry 23 Oct 2008) | 口座残高 498,302円 (i0086) | Losing daily; journal defaced. Accepted backdrop: dead 13 Feb 2009. |
| Mebuki (present, 8 Dec) | FX account 0; debt to Mochiko | Working; committed to repay; called "芽・吹・" (i0055). |
| Mochiko (present, 8 Dec) | Flat; 20,993,630円 | Knows of Mebuki's wipe-out. |
| Yasuko | — | Not yet in V06. |

## Open questions
1. Is the journal reading a new event (first reading of these entries) or a re-reading? (V01 accepted: Kurumi found the
   notebook earlier.)
2. What date in present time is i0090? Does the next present-time scene give a date?
3. Will Kurumi's "次は絶対勝つ" lead to a larger position or a different pair?

## Testable forecasts (from i0003–i0090; literary; no real-market knowledge used; F06–F07 items remain as frozen)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F08-1 | i0091 is a black logo separator page, or carries a 「第29話」 label (i.e., 第28話 ends at i0090). | MODERATE | i0091 is a 第28話 story page (neither a separator nor labelled 「第29話」). |
| F08-2 | The first present-time Kurumi trade shown after i0090 is a new position opened (not merely a plan) within the next chapter (第29話). | MODERATE | 第29話 shows no new Kurumi position opened (order, fill, box or explicit statement of an executed entry). |
| F08-3 | The first new Kurumi position shown after i0090 is in a pair other than USD/JPY. | LOW-MODERATE | The first new Kurumi position shown after i0090 is USD/JPY. (None shown in V06 → OPEN.) |
| F08-4 | The first new Kurumi position shown after i0090 has a printed or stated size of 300枚 or more. | MODERATE | Its printed or stated size is below 300枚. (None shown, or size not given → OPEN.) |
| F08-5 | No V06 page after i0090 shows the adult Kurumi deciding to stop FX trading (quitting, retiring or closing her account). | MODERATE | A V06 page after i0090 shows Kurumi deciding or declaring that she stops FX trading. |

#### Principal freeze file F09.md

# F09 — V06 principal prospective freeze (PRECAUTIONARY: possible end of 第29話 after i0110)

- Author: V06 principal (Agent A), chain session 3, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:27 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:26:30 EST 2026).
- Pages read before this freeze: i0003–i0110, each once, in spine order. NOT opened: i0111 onward; deferred i0001, i0002,
  i0158–i0161. Images this session so far: 32 (reading copies i0080–i0110 = 31; crop i0105 ×1).
- Why now: i0110 (even, right page) ends on a broken-off cliffhanger — "見つけた…! 必勝の通貨…!" / "ユーロ…" / "対…!!" —
  18 pages into 第29話 (label i0093). Shorter than earlier chapters, so a chapter end is not likely, but possible.
  Precautionary; no slip. F01–F08 stand unedited.

## Additions since F08 (i0091–i0110)
- i0091|i0092: two logo separators (bottom-left, bottom-right). 第28話 = i0057–i0090 (34 pages). F08-1 confirmed.
- 第29話 (label i0093): night, Kurumi's apartment. She closes the 日誌: "もしお母さんが勝ってたら 私たちは幸せになれてた
  のかな?"; an imagined middle-school self warns ("あんまり危ないことしないで…", "少しずつ壊れてきてるの わからないの?");
  the adult replies "こんな中途半端なところで撤退できるわけがない" and swats the image away (i0093–i0094).
- Goal restated: "母が失った2000万円を為替市場から奪い返すこと"; BOX 「くるみ FX口座残高(国内口座) 18,339,915円」 (i0095);
  after tax she needs about 2500万円 gross: "ゴールまであと566万…とんで85円" (CALC exact: 25,000,000 − 18,339,915 −
  1,000,000 withdrawn = 5,660,085) (i0096).
- "相場がわからない…", "ドル円売りで連敗してからだ…" (i0097); "相場観にズレが生じている——"; "結局ドル円も下がって現在
  118円", "やっぱ損切りいらなかったじゃん" (i0098); "勝率重視で含み損耐えるべきだった", "これから何年もFXで戦い続ける
  わけじゃないし" (i0099).
- Group chat (i0099–i0101): Yasuko asks about her next manga; Mochiko proposes a cat protagonist; Mebuki suggests "接客の
  お仕事" with "キモイ客"; Yasuko: "なんか芽吹闇深くなってないか?". Kurumi asks about FX: Yasuko busy; Mochiko "ノーポジ
  だけどわからん 新規ポジション持つ気もない" (reading an app-development book); Mebuki "実はFX降りました ごめんなさい";
  Kurumi "残念…". Kurumi revives the "投資バトル" ("芽吹ちゃん発案のやつ", "クリスマスに結果報告会!").
- Kurumi: "FXは勝てる!", "そもそも感覚でやろうとするなんて間違ってる", "探すんだ! 理詰めで解けるような期待値MAXの
  必勝の通貨を——" (i0102–i0103). Considers EUR/USD (chart, "ユーロは下がりすぎ…! 第一感は買いだ…!"; text "1・12ドル" vs
  graphic "€1.22" — inconsistency kept) but rejects it: "必勝じゃない", "今回もそうなる保証はどこにもない", "今の私は相場と
  ズレている" (i0105–i0106). "もっと確実ななにかがほしい——" (i0107). A flat chart near 1.20–1.25 (2012–2014) — "あまりにも
  平らすぎる——"; searches "2011年 ユーロ危機" (i0108–i0109). "見つけた…! 必勝の通貨…!" / "ユーロ…対…!!" (i0110).

## States at i0110
| Person | Position / money (latest printed) | State |
|---|---|---|
| Kurumi (present; date not shown since i0055's 8 Dec) | Flat; 18,339,915円 (i0095) | Target 2500万円 gross ("あと566万"); has found what she calls "必勝の通貨" ("ユーロ対…"); no order yet. Believes the stop-losses were unnecessary; now favours holding unrealized losses. |
| Mebuki | FX account 0; debt to Mochiko | Told the group she quit FX; did not mention the wipe-out or the debt. |
| Mochiko | Flat; 20,993,630円 | "No position", no intention of a new one; reading about app development. Silent about her profit and Mebuki's loss. |
| Yasuko | No position | Busy with her next manga. |

## Open questions
1. Which currency completes "ユーロ対…"? Is it the flat-chart pair?
2. Direction, size and timing of Kurumi's entry; does she use her whole balance?
3. Does the contest ("クリスマスに結果報告会") take place within V06?

## Testable forecasts (from i0003–i0110; literary; no real-market knowledge used; F06–F08 remain as frozen)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F09-1 | i0111 is a 第29話 story page (neither a logo separator nor a page labelled 「第30話」). | MODERATE-HIGH | i0111 is a logo separator page, or carries 「第30話」. |
| F09-2 | Within V06, Kurumi opens a position (order, fill, box or explicit statement of an executed entry) in the pair she names as "ユーロ対…" (the currency completing i0110's sentence). | MODERATE-HIGH | No V06 page shows or states Kurumi opening a position in that pair. |
| F09-3 | The first position Kurumi opens in that pair has a printed or stated size of 300枚 or more. | MODERATE | Its printed or stated size is below 300枚. (No position, or no size given → OPEN.) |
| F09-4 | Before V06's main narrative ends, a printed Kurumi balance or P/L line shows a loss (negative P/L, or a balance below 18,339,915円) attributable to the "ユーロ対…" position. | MODERATE | No printed Kurumi P/L or balance in V06 shows a loss on that position. (No position → OPEN.) |
| F09-5 | The "投資バトル" results meeting (クリスマス) is held on the page within V06. | LOW-MODERATE | No V06 page shows the four (or the contest participants) meeting to report results. |

#### Principal freeze file F10.md

# F10 — V06 principal prospective freeze (BOUNDARY: probable end of 第29話 after i0116)

- Author: V06 principal (Agent A), chain session 3, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:29 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:28:20 EST 2026).
- Pages read before this freeze: i0003–i0116, each once, in spine order. NOT opened: i0117 onward; deferred i0001, i0002,
  i0158–i0161. Images this session so far: 38 (reading copies i0080–i0116 = 37; crop i0105 ×1).
- Why now: i0116 (even, right page) is a wordless full page — Kurumi exultant at the keyboard after "必勝全力の300枚
  買い!!!" (i0115), a skeletal Death figure with lantern and scythe behind her — 24 pages into 第29話 (label i0093),
  matching the length of earlier chapters. A chapter end is probable. No slip: i0117 not opened. F01–F09 stand unedited.

## Exposure declaration (binding on how the forecasts below may be read)
- EXTERNAL_REFERENCE: the analyst has general real-world knowledge about the depicted Swiss franc policy and its later
  history. It is EXCLUDED. No forecast below is derived from it. Forecasts touching the outcome of Kurumi's EUR/CHF
  position are marked EXPOSURE-SENSITIVE: their rationale is limited to on-page signals (the Death figure on i0116,
  the 「必勝」 strip on i0003 and repeated "必勝" claims, Mebuki's death vision before her wipe-out i0022–i0025), and their
  scoring should be read with this exposure in mind.

## Additions since F09 (i0111–i0116)
- i0111: "スイスフラン!" (CHF; "Confoederatio Helvetica Franc 〜スイスフラン〜"); caption "時は2011年まで遡る——".
- i0112–i0113 (narrated 2011): franc bought amid euro-area unease from Greece's fiscal problems; strong franc hurting
  Swiss exporters; 9月6日 火曜日 the スイス国立銀行 announces "我々には外国通貨を無制限に買う用意がある" — caption
  "1ユーロ=1.20フランを上限とする 無限介入政策の始まりであった"; EUR/CHF jumps "1・10から1・20まで".
- i0114: "これ以上のスイスフラン高は許さない 断固たる意志で介入を続けると——"; Kurumi: "それから3年が経った今でも
  この政策は続いている…", "強烈な脅し文句が牽制となって 介入自体は少なく済んでるんだ…", "あとはユーロ安が止まるのを
  待つだけ…".
- i0115: "スイス国家が守ってくれている…!!"; "スイス国立銀行の無限の介入資金があるなら 対スイスフランは絶対下がらない!";
  "ゆえにユロスイは買(ロング)いしかありえない!"; "勝った!! 必勝全力の300枚買い!!!" (entry rate not printed; no ticket).
- i0116: wordless: Death figure, scythe around Kurumi's neck.

## States at i0116
| Person | Position / money (latest printed) | State |
|---|---|---|
| Kurumi (present, ≈2014; date not printed since 8 Dec) | EUR/CHF LONG 300枚 (spoken order, i0115; entry rate, margin and stop not shown); last printed balance 18,339,915円 (i0095) | Certain of a "必勝" trade backed by the central bank's commitment; target 2500万円 gross ("あと566万"). Believes stop-losses were unnecessary and favours holding unrealized losses (i0098–i0099). Has read her mother's journal; vowed "次は絶対勝つ". Revived the Christmas results meeting. |
| Mebuki | FX account 0; debt to Mochiko (2,000,000 principal accepted) | Told the group "FX降りました" without mentioning the wipe-out or debt. "芽・吹・" caller (i0055) still unidentified. |
| Mochiko | Flat; 20,993,630円 | "ノーポジ… 新規ポジション持つ気もない"; reading about app development. |
| Yasuko | No position | Busy with her next manga; noticed Mebuki's "闇". |
| Kozue (flashback) | Ruined (≈1900万円 lost; last balance 498,302円) | Journal ends in scribbles (23 Oct 2008). |

## Open questions
1. EUR/CHF entry rate, margin use and stop: will they be printed?
2. Does V06 show the position's outcome, or end with it open?
3. Who called "芽・吹・", and what did Mebuki tell her parents (i0044)?
4. Does the Christmas results meeting happen in V06?

## Testable forecasts (from i0003–i0116; literary; F06–F09 remain as frozen)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F10-1 | i0117 is a black logo separator page or carries a 「第30話」 label (i.e., 第29話 ends at i0116). | MODERATE-HIGH | i0117 is a story page without a 「第30話」 label. |
| F10-2 | A numerical EUR/CHF entry rate for Kurumi's 300枚 long is printed (screen, box, chart annotation or caption) somewhere in V06. | MODERATE | No V06 page prints a numerical entry rate for that position. |
| F10-3 | Kurumi tells at least one other named character (Mebuki, Mochiko, Yasuko or her father), on the page in V06, that she holds a EUR/CHF (ユロスイ / スイスフラン) position. | MODERATE | No V06 page shows Kurumi telling another named character of the EUR/CHF position. |
| F10-4 | The next present-time date shown in V06 (caption, phone or screen) is in December 2014. | MODERATE | The next present-time date shown in V06 is outside December 2014. (No further present-time date in V06 → OPEN.) |
| F10-5 | The chapter after 第29話 opens (its first page after any separators) on a present-time scene without Kurumi. | LOW-MODERATE | Kurumi appears on that chapter's first story page, or that page is a flashback. |
| F10-6 | EXPOSURE-SENSITIVE. Kurumi's EUR/CHF 300枚 long is still open (not closed by her, by a stop, or by forced liquidation) on V06's last main-narrative page on which it is mentioned or shown. | LOW-MODERATE | A V06 page shows or states that the position has been closed (by her, a stop, or forced liquidation). |
| F10-7 | Kurumi adds EUR/CHF lots (a further buy beyond the 300枚) in V06. | LOW-MODERATE | No further EUR/CHF buy by Kurumi shown or stated in V06. |

#### Principal freeze file F11.md

# F11 — V06 principal prospective freeze (SUPPLEMENTARY: possible end of 第29話 at i0117)

- Author: V06 principal (Agent A), chain session 3, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:30 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:29:27 EST 2026).
- Pages read before this freeze: i0003–i0117, each once, in spine order. NOT opened: i0118 onward; deferred i0001, i0002,
  i0158–i0161. Images this session so far: 39 (reading copies i0080–i0117 = 38; crop i0105 ×1).
- Why now: F10 (written after i0116) expected 第29話 to end at i0116, but i0117 is a further 第29話 page (F10-1
  disconfirmed). i0117 (odd, left page) ends on "発射——" with the Death figure over Kurumi — an odd-page cliffhanger like
  the end of 第27話 (i0055), 25 pages into 第29話. This supplement is written BEFORE opening i0118, which may be a separator
  or the next chapter. No slip. F10 stands unedited and remains the principal boundary freeze; F11 adds to it.

## Addition since F10 (i0117)
- i0117: Kurumi's blank, wide-eyed face beneath the grinning skull (shiver SFX); a barrel-like rod over her keyboard and
  the balloon "発射——" — the 300枚 EUR/CHF buy rendered as a launch. No rate, ticket or date.

## States: as F10 (no change in positions or figures).

## Testable forecasts (supplementing F10; F10-2…F10-7 remain as frozen; same exposure declaration as F10 applies)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F11-1 | i0118 is a black logo separator page (第29話 ends at i0117) and 「第30話」 is printed on i0119. | MODERATE | i0118 is not a separator page, or 「第30話」 is not printed on i0119. |
| F11-2 | The first story page of the chapter after 第29話 shows the EUR/CHF order's result (a fill, rate, box or P/L) or Kurumi watching the position. | LOW-MODERATE | That page shows neither an EUR/CHF figure nor Kurumi watching the position. |

#### Principal freeze file F12.md

# F12 — V06 principal prospective freeze (SUPPLEMENTARY: possible end of 第29話 at i0118)

- Author: V06 principal (Agent A), chain session 3, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:30 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:29:59 EST 2026).
- Pages read before this freeze: i0003–i0118, each once, in spine order. NOT opened: i0119 onward; deferred i0001, i0002,
  i0158–i0161. Images this session so far: 40 (reading copies i0080–i0118 = 39; crop i0105 ×1).
- Why now: i0118 (even, right page) is a further 第29話 page (F11-1 disconfirmed); it ends on Kurumi, panting and
  sweating at her desk, thinking "なにか重大な見落としが…?" — 26 pages into 第29話. A chapter end here is possible (V01
  showed chapters can begin mid-scene with only a small label). Written BEFORE opening i0119. No slip. F10 and F11 stand
  unedited; F12 adds to them.

## Addition since F11 (i0118)
- i0118: Kurumi slumped over her desk, panting; a sweat drop on the keyboard; "なに…? 今の感覚…"; heart pounding;
  "なにか重大な見落としが…?". The dread that F10/F11 recorded as non-diegetic (the Death figure) is now felt by Kurumi.

## States: as F10, plus
- Kurumi suspects she has overlooked something serious about the EUR/CHF trade just placed; no action on that suspicion
  shown yet. Position unchanged (EUR/CHF LONG 300枚, spoken order; rate not printed).

## Testable forecasts (supplementing F10–F11; same exposure declaration as F10 applies)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F12-1 | The page that names or explains what Kurumi "overlooked" (i0118) appears in V06. | MODERATE | No V06 page names or explains a specific overlooked factor connected to her EUR/CHF trade. |
| F12-2 | Kurumi does not close or reduce the EUR/CHF 300枚 long because of this suspicion within the scene that continues from i0118 (same night, same room). | MODERATE | Within that continuing scene, Kurumi closes or reduces the position (order, statement or box). |

#### Principal freeze file F13.md

# F13 — V06 principal prospective freeze (BOUNDARY: end of 第30話 at i0154; possible end of the main narrative)

- Author: V06 principal (Agent A), chain session 4, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:43 (UTC−05:00) (shell `date` before writing: Sun Nov 22 02:43:06 EST 2026).
- Pages read before this freeze: i0003–i0154, each once, in spine order (this session: i0124–i0154, plus crops of i0138
  and i0144). NOT opened: i0155 onward; deferred i0001, i0002, i0158–i0161. Images this session so far: 33 (31 reading
  copies + 2 crops).
- Why now: i0154 (even, right page) ends with 「TO BE CONTINUED...」 below the last panel — 34 pages into 第30話 (label
  i0121). This is a chapter end; it may also be the end of V06's main narrative (only i0155–i0157 remain before the
  deferred cover apparatus i0158–i0161). No slip: i0155 not opened. F01–F12 stand unedited.

## Exposure declaration (as F10, still binding)
- EXTERNAL_REFERENCE: the analyst has general real-world knowledge about the depicted Swiss franc policy, the SNB's
  December 2014 negative-rate decision and the policy's later history. It is EXCLUDED. No forecast below is derived from
  it; forecasts touching the EUR/CHF outcome are marked EXPOSURE-SENSITIVE and their rationale is limited to on-page
  signals. The printed date on i0138 (「2014年 12月8日 月曜日」) is recorded as printed and not compared with anything.

## Additions since F12 (i0119–i0154)
- Separators i0119|i0120; 「第30話」 label i0121 (odd page). 第29話 = i0093–i0118.
- Bridge vision (i0121–i0137): Kurumi first refuses to "cross" ("渡らない", i0122), finds EUR/CHF would be "ただの虚無"
  short-term (i0123), plans "そのときは こんな橋 損切りするだけ" (i0124), meets the "ロング騎士団" of fellow EUR/CHF longs
  (i0125–i0126), names the "悪寒の正体": crowded longs with stop-loss sells clustered at 1.20 (i0127–i0128); imagines a
  hedge-fund sell attack in the Japan early-morning "魔の時間", a stop cascade and "買い方(ロンガー)全滅" (i0129–i0132);
  back at her desk at night: "いや… それはない… のでは…" (i0133); reassures herself — SNB giants, "結局誰も無限には
  敵わない", "一度1・20を割ったことあるけど 暴落なんてしてない", instant repair (i0134–i0136); "霧は晴れた", "渡ろう
  みんなで", "ユロスイは「買い」だ…!" (i0137).
- Narrated: 「2014年 12月8日 月曜日——」 the スイス国立銀行 announces a negative-rate policy to restrain franc buying (Russia
  turmoil, oil fall) (i0138, crop); the governor: "1ユーロ1・2フランは 断固として防衛する…!" (i0139).
- Present time jumps to 「12月25日 木曜日」 Christmas (i0139); captions: FX market closed that day (i0140).
- Yakiniku 「牛の気もち」 (i0140–i0154): Kurumi, Mochiko, Yasuko; Mebuki "終わったら来る" (working). Results announcement
  postponed until all are present (i0141). Kurumi's rule sheet adds "嘘の申告は禁止"; she tells Mochiko "中間発表のとき嘘
  ついてたでしょ?" (i0143). Rules: withdrawals count; open positions at market value (i0144, crop of example diagram);
  Mochiko: "嘘はつかないよ". Yasuko: quit FX, aiming to be a professional manga artist (i0146–i0147). Kurumi: profit
  this year "1000は超えてる" (i0147). Yasuko: "引き際…とかさ…"; Kurumi: "今勝負してる通貨が上がれば 引退予定" and "ユロ
  スイ買い 300枚!" (i0148) — the position is HELD on 25 Dec (entry date/rate unprinted; fill timing unresolved between
  i0115/i0117 and i0137). Mochiko checks the chart: "妙なやつ", "なんだこの真っ平らなチャートは…!", private vision of a
  monster: "触りたくない…!", "こんなチャート 存在してはいけない…!" (i0149–i0151); asks "さすがに損切り注文くらいしてる
  よね?"; Kurumi: "あえてしてない!", a dip below 1・20 could trigger an intervention rise (i0152), "損切り注文してたら
  狩られて負けるだけ" (i0153). Mochiko (thought): "その根拠はどこにある? 万が一が起きたらどうするつもりだ…!?" (i0153);
  "私が気にすることじゃない", "全部 くるみが決めたことだろう?" (i0154). 「TO BE CONTINUED...」.

## States at i0154 (25 Dec, evening; market closed)
| Person | Position / money (latest printed or stated) | State |
|---|---|---|
| Kurumi | EUR/CHF LONG 300枚, NO stop-loss (stated i0148, i0152); entry rate/date not printed; last printed balance 18,339,915円 (i0095); says this year's profit "1000は超えてる" (i0147) | Certain the SNB floor protects her; welcomes even a dip below 1.20; plans to retire if EUR/CHF rises; target 2500万円 gross (i0096). Cheerful at the dinner; grills badly. Knows Mebuki "quit FX" and is working; not shown knowing of the wipe-out or the loan. |
| Mochiko | Flat (stated i0100); 20,993,630円 after closing her longs (i0052) | Sees Kurumi's trade as unnatural and baseless; asked about a stop; withholds her alarm, deciding it is Kurumi's own decision. Promised not to lie in the report; privately had forgotten the meeting. |
| Yasuko | No FX (quit; manga) | Host at the grill; gently raised "引き際" with Kurumi. |
| Mebuki | FX account 0 (i0039); debt to Mochiko | Working on Christmas; expected later; not on the page in 第30話. |

## Open questions
1. Do i0155–i0157 continue the main narrative (a 第31話), or are they extras/afterword?
2. Contest results: what will each report (Kurumi's start balance vs now, Mochiko's honesty, Mebuki's zero)?
3. When was the 300枚 EUR/CHF long filled, and at what rate? What happens to it?
4. Will Mebuki arrive, and will her wipe-out and the loan come out in front of Kurumi?

## Testable forecasts (from i0003–i0154; literary; same exposure declaration; F06–F12 remain as frozen)
Scope note: F13-1 is scored within V06. F13-2…F13-6 concern pages after V06's main narrative and are scored on the
first admitted pages that settle them (OPEN until then).
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| F13-1 | None of i0155–i0157 carries a 「第31話」 chapter label: V06's main narrative ends at i0154. | MODERATE-HIGH | A 「第31話」 label printed on any of i0155, i0156 or i0157. |
| F13-2 | EXPOSURE-SENSITIVE. The first page (after V06's main narrative) that shows what happened to Kurumi's 300枚 EUR/CHF long shows a loss on it (a printed negative P/L, a printed Kurumi balance below 18,339,915円, or forced liquidation). Rationale limited to on-page signals: the Death figure (i0116–i0117), the "重大な見落とし" (i0118), Mochiko's monster vision and "万が一" (i0151–i0153), no stop-loss (i0152), the 「必勝」 strip (i0003). | MODERATE | That first page shows a profit or a break-even close on the position, or the position still open with no loss printed. |
| F13-3 | Mochiko does not warn Kurumi aloud about the EUR/CHF trade (beyond the stop-loss question of i0151) before the first page that shows the position's fate. | MODERATE | A spoken (or messaged) Mochiko warning to Kurumi about the trade appears before that page. |
| F13-4 | When the contest results are first announced on the page, Mochiko's announced result is consistent with her printed figures (no thought balloon or later page reveals it as false). | MODERATE | A thought balloon, printed box or later page shows Mochiko's announced result to be false. |
| F13-5 | Mebuki is shown arriving at the Christmas yakiniku meeting on the page (in the chapter that continues the 25 Dec evening). | MODERATE | The continuation of the 25 Dec evening ends without Mebuki arriving, or no admitted page returns to that evening. |
| F13-6 | Before the position's fate is shown, no page shows Kurumi placing a stop-loss order on the EUR/CHF long. | MODERATE-HIGH | A page shows Kurumi placing (or stating she placed) a stop-loss on that position before its fate is shown. |

#### Principal freeze file MAIN_EXIT.md

# MAIN_EXIT — V06 principal exit freeze (end of the V06 main narrative)

- Author: V06 principal (Agent A), chain session 4, run FXK-RUN-20261119-V01-V10, witness FXK-JP-V06-W01.
- Timestamp: 2026-11-22T02:46 (UTC−05:00) (shell `date` immediately before writing: Sun Nov 22 02:46:05 EST 2026; a first
  write attempt by shell heredoc at 02:45 failed with a shell parse error and wrote nothing).
- Main narrative: 第26話–第30話, i0003–i0154 (last main page i0154, 「TO BE CONTINUED...」). All of i0003–i0156 have been
  opened once each in spine order. To establish where the main narrative ends I opened, after F13, i0155 (logo
  separator) and i0156 (「6巻あとがき」 afterword gag page, classified by a glance: Yasuko's yakiniku part-time-job backstory
  with all four characters lying on a bed; Mebuki appears in it). That afterword glance is the only post-main exposure
  before this freeze; it bears on no forecast below, and Mebuki's appearance there is NOT counted as a main-narrative
  appearance. NOT yet opened: i0157, i0162, i0163; deferred i0001, i0002, i0158–i0161 (still unopened in any form — no
  reading copy, crop or contact sheet).
- Exposure declaration (as F10/F13, binding): general real-world knowledge of the depicted Swiss franc policy, the SNB's
  December 2014 negative-rate decision and the policy's later history is EXTERNAL_REFERENCE, EXCLUDED; EUR/CHF-outcome
  forecasts are EXPOSURE-SENSITIVE with on-page rationale only. General awareness of the title/adaptation: excluded.
- F01–F13 stand unedited. This freeze adds no page content beyond i0154 except the classification noted above.

## Component map of the main narrative (for drafting)
- i0003 colour opening (strip 「第6集 必勝」), i0004 colour title, 第26話 label i0005 → 第26話 i0003–i0028; separators i0029|i0030.
- 第27話 i0031–i0055; separator i0056. 第28話 (flashback, Kozue 2006–2008; present close i0090) i0057–i0090; separators
  i0091|i0092.
- 第29話 i0093–i0118; separators i0119|i0120. 第30話 i0121–i0154; separator i0155; afterword i0156.
- Exactly five chapter labels seen, 第26話–第30話 (V06-EN-2 main-narrative part satisfied; colophon still to check).

## Present-time dates printed in V06
2014年12月5日金曜日 (i0031); 12月8日 月曜日 早朝 (i0050); narrated 「2014年 12月8日 月曜日——」 SNB negative-rate announcement
(i0138, crop); 12月25日 木曜日 Christmas (i0139), FX market closed that day (i0140). The night of Kurumi's EUR/CHF decision
(第29–30話) is undated (no later than 25 Dec, INF).

## Exit state — positions and money
| Person | Latest printed / stated | Provenance |
|---|---|---|
| Kurumi | EUR/CHF LONG 300枚, held on 25 Dec, NO stop-loss ("あえてしてない"); entry date and rate NOT printed (fill timing between i0115/i0117 and i0137 UNRESOLVED). Last printed balance 18,339,915円 (i0095; after two V06 USD/JPY short losses, −1,743,000 i0013 and −1,131,000 i0046). Says this year's profit "1000は超えてる" (i0147). Target ≈2500万円 gross, "あと566万…とんで85円" (i0096). Tax withdrawal (V03, 1,000,000) mentioned (i0144). | i0148, i0152 (speech); i0095 box; i0147 speech |
| Mochiko | Flat since 8 Dec: closed all longs, 20,993,630円 (+7,691,000) (i0052); "ノーポジ… 新規ポジション持つ気もない" (i0100); no V06 page shows a new position. | i0052 screen; i0100 chat |
| Mebuki | FX account wiped out, 0円 (i0039, 5 Dec); "FX降りました" (i0100); debt to Mochiko (accepted principal 2,000,000 @109.5%) + cards + student loan; working (works on Christmas, i0140). | i0039, i0100, i0140 |
| Yasuko | No FX ("FXやってたころ", "FXやってるあたしとはバイバイ", i0146–i0147); aiming at professional manga. | speech |
| Kozue (flashback) | 2008: forced liquidation, ≈1900万円 lost (i0080); 1,005,144円 → 498,302円 (i0082, i0086); journal ends 23 Oct 2008 in scribbles (i0089). Death (accepted, 13 Feb 2009) not shown in V06. | i0075–i0089 |

## Exit state — persons and relationships
- **Kurumi.** Has read her mother's 2008 journal (第28話) and wept: "次は絶対勝つからね" (i0090); refuses to withdraw
  ("こんな中途半端なところで撤退できるわけがない", i0094); goal "母が失った2000万円を為替市場から奪い返す" (i0095). Seeks a
  "理詰め" "必勝の通貨" (i0103); rejects EUR/USD; finds EUR/CHF under the SNB floor; "必勝全力の300枚買い" (i0115); Death figure
  and dread (i0116–i0118); a long vision in which she pauses, identifies stop-clustering at 1.20 as the danger, and then
  reassures herself that "unlimited" intervention cannot be beaten (i0121–i0137). At Christmas: cheerful convenor of the
  contest, confronts Mochiko's interim lie with a new rule, plans to retire "if the currency rises", holds 300枚 with no
  stop, treats a dip below 1.20 as an opportunity. Regards her earlier stop-losses as mistakes ("損切りいらなかった", i0098).
- **Mochiko.** Closed her longs at a large profit on 8 Dec; told Mebuki "やっと人間(まとも)になったじゃん" (i0054); silent to the
  group about her profit and about Mebuki's wipe-out. At Christmas: had forgotten the meeting (thought), promised not to
  lie, examined Kurumi's EUR/CHF chart and privately judged it unnatural and baseless ("触りたくない", "その根拠はどこに
  ある?", "万が一が起きたらどうするつもりだ"), asked only whether Kurumi had a stop, then chose silence: "私が気にすること
  じゃない", "全部 くるみが決めたことだろう?" (i0151–i0154). Teased Yasuko to return to FX (i0147).
- **Yasuko.** Quit FX; manga ambition; generous host at the grill (prepped garlic); noticed Mebuki's "闇" (i0100), said
  "あいつも変わったよなぁ" (i0140); gently urged Kurumi to consider "引き際" (i0147).
- **Mebuki.** Absent from the main narrative after the group chat (i0099–i0101) except as the working, expected-later member
  at the dinner. Her wipe-out and debt are not known to Kurumi or Yasuko on the page; Mochiko knows.
- **Kurumi's father.** Not shown in present time in V06; mentioned (i0093); framed family photo (i0107, INF).
- Directional notes: Kurumi→Mochiko: open, affectionate challenge about honesty. Mochiko→Kurumi: recognizes the danger,
  withholds the warning (understanding a vulnerability and choosing non-intervention; no exploitation shown). Yasuko→Kurumi:
  care. Mochiko→Mebuki: knowledge of the wipe-out kept from the group.

## Open questions at main exit
1. Fill date and rate of the EUR/CHF long; margin used; whether 300枚 is the "全力" of about 18.3 million yen.
2. The position's fate (EXPOSURE-SENSITIVE; on-page signals ominous: Death figure, Mochiko's vision, no stop).
3. Contest results: start balances vs now; Mochiko's honesty under the new rule; Mebuki's report of 0.
4. Will Mebuki arrive at the dinner; will her wipe-out and the loan come out to Kurumi and Yasuko?
5. Who called "芽・吹・" (i0055); what did Mebuki tell her parents (i0044)?
6. Exact digits of Kozue's "当日決済損益 −18,790,50[…]" (i0079) — not printed again in V06.

## Provisional forecast dispositions at main exit (final literal scoring belongs to drafting; listed for the record)
- V06-EN: EN-1, 3, 4, 5, 6 (i0139), 7, 8, 9, 11, 14, 15, 16, 17, 18 CONFIRMED; EN-2 main part satisfied (five labels 26–30),
  colophon pending; EN-10 candidate CONFIRMED (group-chat exchange i0099–i0100); EN-12 to be scored literally (i0054, and no
  Mochiko line about Mebuki's welfare at Christmas); EN-13 DISCONFIRMED (father never speaks in present time).
- V05-MX: MX-1–4, 6, 9 C; MX-5 lean D (i0053 oblique only); MX-7 D (Kurumi not told of the loan); MX-8 D (transfer not shown
  taking effect); MX-10 D (no Yasuko contact with the publisher/editor shown).
- F01: 8 C (customer not seen again — verify by log grep); 9 C; 10 D. F02-8 lean D (i0053 oblique — decide). F03: 6 C
  (i0051 "退場です", i0100 "FX降りました"); 7 D; 8 D. F04: 3 C (EUR/CHF, i0148); 4 C (300枚); 6 D; 7 D; 8 D; 9 D; 10 D.
  F05: 2 D; 3 D; 5 D. F06-6 D.
- F08: 2 UNRESOLVED (depends on whether the fill occurred in 第29話 — i0115/i0117 — or after i0137 in 第30話); 3 C; 4 C;
  5 lean C (only a conditional "引退予定", i0148 — not a decision to stop; score literally).
- F09: 2 C; 3 C; 4 D (no printed loss on the position in V06); 5 CONTESTED (participants met for the results meeting on
  25 Dec, i0140–i0154, but no results were reported before the volume ended — score literally against "meeting to report
  results").
- F10: 2 D (no entry rate printed); 3 C (i0148, told to Mochiko and Yasuko); 4 C (2014年12月8日, i0138); 6 C (position open
  at its last mention, i0152–i0153); 7 D. F11-2 D. F12: 1 C (i0128 "悪寒の正体"); 2 C.
- F13: 1 provisional C (i0155 separator, i0156 afterword; i0157 still to classify); 2–6 OPEN (post-V06 scope).

## Exit forecasts (for the next admitted volume; scored literally on the first admitted pages that settle them; F13-2…F13-6
remain as frozen and are not repeated)
| ID | Forecast | Confidence | Would disconfirm |
|---|---|---|---|
| MX06-1 | The next admitted main-narrative chapter's first present-time scene continues the 25 Dec yakiniku evening (same night: the restaurant or its immediate aftermath). | MODERATE | Its first present-time scene is set on another day, or elsewhere than the restaurant and its immediate aftermath. |
| MX06-2 | Kurumi's contest result, when first announced on the page, is a positive percentage gain. | MODERATE-HIGH | Her first announced result is zero or negative. (Never announced in the next admitted volume → OPEN.) |
| MX06-3 | Kurumi learns on the page, in the next admitted volume, that Mebuki's FX account was wiped out. | MODERATE | No page in the next admitted volume shows Kurumi learning of it. |
| MX06-4 | EXPOSURE-SENSITIVE. A numerical EUR/CHF rate tied to Kurumi's position (screen, chart label, box or caption) is printed in the next admitted volume. | MODERATE | No such rate is printed there. |
| MX06-5 | Mochiko is shown (thought or speech) regretting that she did not warn Kurumi about the EUR/CHF trade, in the next admitted volume. | LOW-MODERATE | No such Mochiko regret is shown there. |


### 6.2 Independent freezes of the financial specialist (Agent B)

Agent B's seven freeze files, reproduced verbatim. F00 was written before any V06 page, F02 and F04 inside a chapter at the end of a session's image budget, and F06 after every main-narrative page and before its first deferred image. Its exposure-sensitive (ES) items were declared by Agent B itself (real 2008 and late-2014 exchange-rate history; from i0108 the 1.20 currency floor's real history). Its F06 forecasts face the next admitted volume and are recorded as ledger rows FXK-V06-F177–F190.

#### Agent B freeze file F00_ENTERING.md

# Agent B V06 — F00 entering freeze (before any V06 page image)

Frozen: Sun Nov 22 01:52 EST 2026 (by `date`), after reading only the documents listed in exposure.md §1–§2. Never edited after.
Author: Agent B (V06 financial/causal/information-state specialist), independent lane.
EXPOSURE-SENSITIVE (ES) = depends on the depicted market path; I declared general awareness of real late-2014 USD/JPY history
(exposure.md §4), so ES items should be excluded from calibration. Non-ES items rest on page-grounded narrative structure.

| ID | Forecast (testable in V06) | Conf. | ES? | Rationale (page-grounded) |
|---|---|---|---|---|
| B6-F00-1 | V06's first chapter returns to Kurumi's 300枚 short (V05 i0158) and prints at least one figure for it (rate, P/L or balance) | MOD-HIGH | no | V05 ends on that open position and a candle against it (i0162) |
| B6-F00-2 | The short is shown at a printed unrealized loss at some point in V06 | MOD | ES | reversal candle; no stop shown |
| B6-F00-3 | The 118.6 take-profit is NOT shown filled in V06's first chapter | MOD | ES | V05 staging of the reversal |
| B6-F00-4 | Kurumi's stop status (whether a stop exists) is stated or shown on the page in V06 | MOD | no | the open question is foregrounded by the "no stop shown" staging |
| B6-F00-5 | Kurumi's printed balance or equity falls below 21,213,915 at some point in V06 | MOD | ES | follows from F00-2 |
| B6-F00-6 | Kurumi closes (realizes) the 300枚 short within V06, with a printed realized figure | MOD | ES | a 300枚 position is too large to stay unresolved for a whole volume in this series' pacing (V01 300枚 resolved within a volume) |
| B6-F00-7 | Mebuki's 43枚 short is shown closed or force-closed (ロスカット or similar) with a printed figure in V06 | MOD | ES | V05 left it near zero equity by CALC; the series has printed forced closes for her before (V04 i0139) |
| B6-F00-8 | Mebuki confronts or speaks to Mochiko about the overheard long (V05 i0145) in V06 | MOD-HIGH | no | V05 ends that thread at "え?" with her on the floor |
| B6-F00-9 | Kurumi learns of Mochiko's 2,000,000 loan to Mebuki within V06 | MOD | no | three-way information gap (Kurumi knows only the lie) is the volume's obvious lever |
| B6-F00-10 | A Mochiko account figure (balance or P/L tile) is printed in V06 | LOW-MOD | no | V05 printed none; she is "long" by self-report only |
| B6-F00-11 | The contest (to 12/25) is mentioned again in V06 | MOD | no | V06 should reach mid/late December; the deadline is due |
| B6-F00-12 | Kurumi does NOT stop trading by the end of V06 (no executed, stated retirement) | MOD | no | "もうちょっとだけ" motif (V05 i0161), 300枚 re-entry within hours of the retirement line |
| B6-F00-13 | Kurumi's father's transfer is referred to on the page (moving, packing, or departure) | LOW-MOD | no | "年明けから" (V05 i0069); V06 may not reach January |
| B6-F00-14 | At least one printed figure in V06 fails to reconcile under 1枚 = 10,000 units (an inconsistency to log) | LOW-MOD | no | V05 had one balloon/tile clash (i0085) among many exact tiles |
| B6-F00-15 | Mebuki's family (parents) learns of her debt or is contacted in V06 | LOW | no | security is their contact; no V05 movement toward it |

Method note: I will log each forecast's disposition with a locator in findings.md; ES items are reported but excluded from my
calibration claims.

#### Agent B freeze file F01_after_ch26.md

# Agent B V06 — F01 freeze at the 第26話 / 第27話 boundary

Frozen: Sun Nov 22 01:59 EST 2026 (by `date`). Pages opened before this freeze: i0003–i0030 only (plus crops of i0003, i0007,
i0008, i0011, i0013, i0015, i0021, i0026). Deferred inputs not opened. Never edited after.
ES = exposure-sensitive (depends on depicted market path; general awareness of real late-2014 USD/JPY declared).

## State frozen (page-grounded)
- Kurumi: cut the 300枚 short at 18:27 on 12月5日 (executed; −1,743,000; balance 19,470,915, i0013); she now holds NO position
  (INF HIGH from the whole-lot arithmetic). Rate then fell (≈120.15, chart, i0015). F00-2 CONFIRMED (printed unrealized losses
  −1,752,000 / −1,941,000 / −1,833,000 / −1,743,000); F00-3 CONFIRMED (118.6 not filled); F00-5 CONFIRMED (below 21,213,915);
  F00-6 CONFIRMED (closed with printed realized figure); F00-4 partly: no stop is shown — she explicitly decided "損切りはナシ"
  (i0009) and then cut manually (i0012–i0013).
- Mebuki: 43枚 short intact; balance 2,621,530, open −2,523,890 (implied 120.450, equity ≈97,640 CALC, i0021); ≈22:20 on
  12月5日, 10 minutes before the US jobs release (i0028); she has told the customer the rate will go up ("素人の勘", i0027–i0028)
  and imagined her position's death (i0024–i0025).

## Forecasts (testable in V06)
| ID | Forecast | Conf. | ES? |
|---|---|---|---|
| B6-F01-1 | 第27話 opens at (or returns within its first 6 pages to) the release moment on 12月5日 with Mebuki | HIGH | no |
| B6-F01-2 | Mebuki's 43枚 short is shown force-closed / liquidated (ロスカット, 強制決済 or equivalent wording, or a zero/near-zero balance) in V06 | MOD-HIGH | ES |
| B6-F01-3 | If liquidated, the printed balance after liquidation is below 300,000円 | MOD | ES |
| B6-F01-4 | Mebuki does NOT close the short voluntarily before the release (no manual close shown in the 10 minutes) | MOD | no |
| B6-F01-5 | The customer's "spike then crash" forecast is shown wrong in its crash leg within the chapter (no crash shown on 12月5日) | LOW-MOD | ES |
| B6-F01-6 | Kurumi opens a new position within V06 after the cut | MOD | no |
| B6-F01-7 | Kurumi's next printed balance (if any) in V06 is below 20,000,000 | MOD | ES |
| B6-F01-8 | Mebuki's debt to Mochiko (2,000,000 / repayment) is mentioned on the page within the next two chapters | MOD | no |
| B6-F01-9 | Kurumi and Mebuki meet or speak on the page in V06 | MOD | no |
| B6-F01-10 | The salon customer (self-styled trader, long 5枚) reappears later in V06 | LOW-MOD | no |

#### Agent B freeze file F02_mid_ch28_after_i0073.md

# Agent B V06 — F02 freeze inside 第28話 (after i0073)

Frozen: Sun Nov 22 02:13 EST 2026 (by `date`). Pages opened before this freeze: i0003–i0073 only (plus crops/montages of them,
listed in STATE.md). Deferred inputs (i0001, i0002, i0158–i0161) not opened. Not at a chapter boundary (第28話 runs on); written
here because the session's image budget ends here. Never edited after.
ES = exposure-sensitive (depends on a depicted market path; I declared general awareness of real 2008 and late-2014 FX history,
exposure.md §4, so ES items are excluded from calibration).

## State frozen (page-grounded)
- 12月5日 2014: Mebuki force-liquidated (0円, −2,610,530 強制ロスカット, i0039); Kurumi's second 300枚 short (121.220 → 121.597)
  cut, balance 18,339,915 (i0046); narrator: USD/JPY above 121 with no sign of a fall (i0044).
- 12月8日: Mebuki tells Mochiko she has lost all borrowed money and "退場" (i0051), will work and repay first (i0053); Mochiko closed
  all longs, 20,993,630 (+7,691,000, i0052).
- 第28話 = flashback of 梢 (Kurumi's mother): FX from 2006 (carry trade, AUD/JPY), diary; 2008-09-05 decides to deposit household
  money; 2008-09-16 unrealized loss > 6,000,000, AUD/JPY 82円台, concealment from Kurumi (i0057–i0073).
- Accepted V01 anchor: on 24 Oct 2008 Kurumi (15) found her mother screaming "2000万円 返せぇぇぇ!!"; father posted away.

## Forecasts (testable in i0074–i0157)
| ID | Forecast | Conf. | ES? |
|---|---|---|---|
| B6-F02-1 | The flashback reaches the accepted V01 scene of 24 Oct 2008 (Kurumi coming home to her mother at the chart) OR prints "2000万円" for the household money, within V06 | MOD-HIGH | no |
| B6-F02-2 | An AUD/JPY rate below 80 appears in 梢's flashback | MOD | ES |
| B6-F02-3 | A printed figure for 梢's account (balance, P/L tile, or deposit amount) beyond the diary's "600万円" appears in V06 | MOD | no |
| B6-F02-4 | 梢's account is shown force-liquidated (ロスカット wording) in the flashback | LOW-MOD | ES |
| B6-F02-5 | The father (郁夫) is shown leaving for, or already on, a posting away from home inside the 2008 flashback | LOW-MOD | no |
| B6-F02-6 | V06 returns to December 2014 after the flashback (before i0157) | HIGH | no |
| B6-F02-7 | Kurumi opens a new position after i0046 with a printed tile or box in V06 | MOD-HIGH | no |
| B6-F02-8 | That new position (if any) is in a pair other than USD/JPY | LOW-MOD | no |
| B6-F02-9 | Kurumi's next printed balance (if any) is below 18,339,915 | MOD | ES |
| B6-F02-10 | Kurumi learns, on the page, of Mebuki's liquidation in V06 | MOD | no |
| B6-F02-11 | The contest (to 12/25) is mentioned in V06 | MOD | no |
| B6-F02-12 | A new repayment figure from Mebuki to Mochiko (amount) is printed in V06 | LOW-MOD | no |

#### Agent B freeze file F03_after_ch28.md

# Agent B V06 — F03 freeze at the 第28話 / 第29話 boundary (after i0091)

Frozen: Sun Nov 22 02:20 EST 2026 (by `date`). Pages opened before this freeze: i0003–i0091 only (plus crops/montages of them,
listed in STATE.md). Deferred inputs (i0001, i0002, i0158–i0161) not opened in any form. Never edited after.
ES = exposure-sensitive (depends on a depicted market path; general awareness of real 2008 and late-2014 FX history declared,
exposure.md §4; ES items excluded from calibration).

## State frozen (page-grounded)
- 第28話 (i0057–i0090) = 梢's 2006–2008 flashback, closed by a frame in which short-haired (present-day, INF MOD-HIGH) Kurumi has
  read her mother's "FXトレード日誌" and says "次は…絶対勝つからね" (i0090).
- 梢 2008: 9/29 all gathered money (insurance surrender, house down-payment fund, parents' money) into AUD/JPY long (i0077);
  10/6 AUD/JPY 80→71 in a day, BID/ASK 71.256/71.271, 当日決済損益 −18,790,50x, ALL positions force-liquidated, "1900万円" lost
  (i0078–i0080); balance 1,005,144 of "かき集めた2000万円" (i0082); then 400× leverage plan, 100枚 AUD/JPY SHORT (i0084), balance
  498,302 (i0086); 10/13 one win; 10/14–10/23 losses, "もう損切りしたくない", "消えたい" (i0087–i0089). The 24 Oct scene itself not
  shown. Father not shown leaving in the flashback.
- Present (Dec 2014): Kurumi 18,339,915, flat after the 121.597 cut (i0046), plans other currencies (i0049); Mebuki liquidated
  (0円), working, owes Mochiko; Mochiko 20,993,630 flat (i0052).
- F02 dispositions so far: F02-1 CONFIRMED (i0082 "2000万円"); F02-2 CONFIRMED [ES] (71.256, i0078); F02-3 CONFIRMED (i0079,
  i0082, i0086 figures); F02-4 CONFIRMED [ES] (i0080); F02-5 not shown in the flashback (DISCONFIRMED within 第28話; stays testable
  only if the flashback resumes); F02-6..12 open.

## Forecasts (testable in i0092–i0157)
| ID | Forecast | Conf. | ES? |
|---|---|---|---|
| B6-F03-1 | 第29話 opens in December 2014 (a dated caption or present-day Kurumi in its first 4 pages) | HIGH | no |
| B6-F03-2 | Kurumi's next new position (if any) is in a pair other than USD/JPY (raised from F02-8's LOW-MOD after i0049 "通貨はほかにもある") | MOD | no |
| B6-F03-3 | Kurumi explicitly refers to her mother or the diary when making or justifying a trading decision in i0092–i0157 | MOD | no |
| B6-F03-4 | Mebuki appears again on the page in i0092–i0157 | MOD-HIGH | no |
| B6-F03-5 | The mother's present-day situation (where she is / her condition) is shown or stated in V06 | LOW-MOD | no |
| B6-F03-6 | Yasuko appears on the page in V06 | MOD | no |
| B6-F03-7 | Kurumi's target (20,000,000 or 25,000,000 or "あと…万円") is restated in i0092–i0157 | MOD | no |
| B6-F03-8 | Kurumi suffers a printed realized loss larger than 1,131,000 on a single trade in i0092–i0157 | LOW-MOD | ES |
| B6-F03-9 | Kurumi uses a printed stop-loss order (逆指値 / ストップ) set in advance in i0092–i0157 | LOW-MOD | no |
| B6-F03-10 | Mochiko opens a new position with a printed figure (rate, size or P/L) in i0092–i0157 | LOW-MOD | no |

#### Agent B freeze file F04_mid_ch29_after_i0113.md

# Agent B V06 — F04 freeze inside 第29話 (after i0113)

Frozen: Sun Nov 22 02:26 EST 2026 (by `date`). Pages opened before this freeze: i0003–i0113 only (plus crops/montages of them,
listed in STATE.md). Deferred inputs (i0001, i0002, i0158–i0161) not opened in any form. Not at a chapter boundary; written here
because the session's image budget ends here. Never edited after.
EXPOSURE: at i0108 I recorded an EXTERNAL_REFERENCE recognition (exposure.md, 02:24) concerning real-world history of a 2014 currency
level at 1.20. Therefore EVERY forecast below about the depicted EUR/CHF path, or the outcome/timing of a EUR/CHF position, is
EXPOSURE-SENSITIVE (ES) and excluded from calibration; I deliberately make no directional forecast of the depicted path.

## State frozen (page-grounded)
- Present (December 2014, exact date unprinted since 12/8): Kurumi flat; balance 18,339,915 (tile i0095); gross goal 25,000,000
  incl. 1,000,000 withdrawn; gap "566万…とんで85円" = 5,660,085 ✓ (i0096); goal re-sourced as "母が失った2000万円を奪い返す"
  (i0095). USD/JPY now "118円" (i0098); she regrets the cuts ("やっぱ損切りいらなかったじゃん") and states a new rule "勝率重視で
  含み損耐えるべきだった" (i0099). Friends: Yasuko inactive, Mochiko flat with no intent, Mebuki "FX降りました" (i0100); contest
  revived by Kurumi (Christmas report meeting, i0101).
- Search: euro dip-buy considered then rejected ("必勝じゃない", i0106); wants "もっと確実ななにか" (i0107); finds a flat 2014 chart
  just above 1.20 (i0108); "必勝の通貨…! ユーロ…対…!! スイスフラン!" (i0110–i0111); narrated 2011-09-06 SNB "外国通貨を無制限に
  買う用意", "1ユーロ=1.20フランを上限とする無限介入政策" with EUR/CHF 1.10→1.20 (i0112–i0113).

## Forecasts (testable in i0114–i0157)
| ID | Forecast | Conf. | ES? |
|---|---|---|---|
| B6-F04-1 | Kurumi opens a EUR/CHF position in V06 with a printed size, rate or balance tile | MOD-HIGH | no |
| B6-F04-2 | If opened, it is LONG EUR/CHF (buying euro against franc near the 1.20 level) | HIGH | no |
| B6-F04-3 | Her size is ≥100枚 (or stated as 全力 / maximum) | MOD | no |
| B6-F04-4 | She frames the trade on the page as (near-)riskless ("必勝", "負けない", "リスクがない" or equivalent) | HIGH | no |
| B6-F04-5 | The page states at least one quantitative risk element of the trade (pips to 1.20, maximum loss, margin, or swap) | MOD | no |
| B6-F04-6 | Another character questions or warns about the trade before V06 ends | LOW-MOD | no |
| B6-F04-7 | The EUR/CHF position remains open (no printed realized result) at the end of V06's main narrative | MOD | ES |
| B6-F04-8 | Kurumi links the trade to her mother/the 2000万 goal on the page while entering it | MOD | no |
| B6-F04-9 | The contest's Christmas report meeting is NOT depicted within V06 | MOD | no |

#### Agent B freeze file F05_after_ch29.md

# Agent B V06 — F05 freeze at the 第29話 / next-chapter boundary (after i0119)

Frozen: Sun Nov 22 02:29 EST 2026 (by `date`). Pages opened before this freeze: i0003–i0119 only (plus crops/montages of them,
listed in STATE.md). Deferred inputs (i0001, i0002, i0158–i0161) not opened in any form. Never edited after.
EXPOSURE: EXTERNAL_REFERENCE recognition at i0108 (exposure.md 02:24) concerns real-world history of the 1.20 EUR/CHF level.
Every forecast below about the depicted EUR/CHF path, or about the outcome/timing of Kurumi's EUR/CHF position, is EXPOSURE-SENSITIVE
(ES) and excluded from calibration. I deliberately make NO directional or outcome forecast for the depicted EUR/CHF path.

## State frozen (page-grounded)
- 第29話 = i0093–i0118. Kurumi (balance 18,339,915 at i0095) reasons that the SNB's unlimited intervention keeps EUR/CHF from
  falling below 1.20 ("絶対下がらない"), declares "必勝全力の300枚買い!!!" (i0115), fires the order ("発射——", i0117) under a reaper
  image (i0116–i0117), then panics: "なにか重大な見落としが…?" (i0118). No order screen, fill rate, or tile printed yet.
- F04 dispositions so far: -2 CONF (long), -3 CONF (300枚), -4 CONF ("必勝", "絶対下がらない", "勝った"); -1 PARTIAL (size printed in
  speech; execution not shown); -5 not yet (no quantitative risk element); -6 not yet; -8 not on the entry pages (no mother/2000万 link
  at i0115–i0117; the goal link was at i0095); -7, -9 open.

## Forecasts (testable in i0120–i0157)
| ID | Forecast | Conf. | ES? |
|---|---|---|---|
| B6-F05-1 | The next chapter (or its first 6 pages) shows an order screen, fill rate, or account tile establishing whether the 300枚 EUR/CHF long was executed | MOD | no |
| B6-F05-2 | Kurumi names the "重大な見落とし" on the page (what she thinks she overlooked) within V06 | MOD | no |
| B6-F05-3 | A EUR/CHF rate with ≥4 decimals (e.g. 1.20xx) is printed in V06 | MOD | no |
| B6-F05-4 | A margin, leverage or required-deposit figure for the EUR/CHF position is printed in V06 | LOW-MOD | no |
| B6-F05-5 | Swap (スワップ / interest) on the EUR/CHF position is mentioned in V06 | LOW-MOD | no |
| B6-F05-6 | Mochiko or another friend learns of the EUR/CHF position on the page within V06 | LOW-MOD | no |
| B6-F05-7 | Kurumi's mother or the 2008 diary is invoked again on the page in i0120–i0157 | MOD | no |
| B6-F05-8 | A dated caption (day/month 2014 or later) appears in i0120–i0157 | MOD-HIGH | no |

#### Agent B freeze file F06_CLOSING.md

# Agent B V06 — F06 CLOSING prospective freeze (after every main-narrative page is logged)

Frozen: Sun Nov 22 02:45:32 EST 2026 (by `date`). Pages opened before this freeze: i0003–i0157 only (plus crops/montages of them, listed in
STATE.md). Every main-narrative page (i0003–i0154) and the back matter i0155–i0157 (separator + two afterword strips) is logged.
Deferred inputs (i0001, i0002, i0158, i0159, i0160, i0161) NOT opened in any form; i0162 (colophon) and i0163 (vendor) not yet opened.
This is my release point: the deferred inputs are opened only AFTER this file is written. Never edited after.
EXPOSURE: EXTERNAL_REFERENCE recognitions at i0108 (real-world history of a 2014 1.20 currency level) and i0138 (the SNB
negative-rate event type) are logged in exposure.md. EVERY forecast about the depicted EUR/CHF path, or about the outcome/timing of
Kurumi's EUR/CHF position, is EXPOSURE-SENSITIVE (ES) and excluded from calibration. I make NO directional or outcome forecast for
that path; ES items below are structural only and are still excluded.

## State frozen (page-grounded; V06 main exit)
- Date of the final scene: 2014-12-25 (Thu) — caption i0139; FX market closed for the holiday (narrator, i0140).
- Kurumi: last printed balance 18,339,915円 (tile i0095 = i0046) after two USD/JPY 300枚 short cuts (−1,743,000 i0013; −1,131,000
  i0046); gross goal 25,000,000 incl. 1,000,000 withdrawn (gap 5,660,085, i0096 ✓). Holds, by her own word at the 12/25 dinner,
  "ユロスイ買い(ロング) 300枚" (i0148) — entry date, rate, fill and margin NEVER printed; NO stop-loss order, by choice
  ("あえてしてない", i0152); exit plan = retire if the currency rises (i0148). Thesis: SNB unlimited intervention at 1.20 (narrated
  2011-09-06, i0112–i0113) makes a fall below 1.20 temporary; a break would bring intervention and a sharp rise (i0152); stops would
  be "hunted" (i0153). She had named and then dismissed the stop-cluster / flash-crash risk at 1.200 (i0127–i0135).
- Reader-only (narrated, not shown known to Kurumi): 2014-12-08 SNB negative-rate policy and the head's vow to defend 1.2 (i0138–i0139).
- Mochiko: 20,993,630 flat (+7,691,000, i0052, 12/8); saw the flat chart, felt "触りたくない", thought "その根拠はどこにある?" /
  "万が一が起きたら…" but kept it unspoken (i0151–i0154).
- Mebuki: force-liquidated 12/5 (0円, −2,610,530; 11,000 gap unexplained, i0039); told Mochiko "退場", will work and repay first
  (i0051–i0053); paid 30,000 earlier (i0051); working at Christmas, absent from the dinner through i0154 ("終わったら来る", i0140).
  Kurumi knows only "FX降りました" (i0100) and that she has a job (i0140; source unshown); knows nothing of the loan on the page.
- Yasuko: out of FX, aiming at professional manga (i0147); first friend to suggest "引き際" (i0147).
- Contest: final meeting depicted (i0140–i0154) but NO results announced; rules: balance + withdrawals, % on start, open positions
  at 時価 (i0144); new rule ⑩ 嘘の申告は禁止 (i0143). Kurumi: profit this year "1000は超えてる" (i0147; consistent, CALC 16,683,225
  since contest start if unchanged).
- Back matter i0155–i0157: separator + "6巻あとがき" gag strip (Yasuko's yakiniku training; all four friends drawn together — PARATEXT,
  not an event) + author strip. No next-volume preview in i0003–i0157.

## Forecasts (testable in V07 unless stated)
| ID | Forecast | Conf. | ES? |
|---|---|---|---|
| B6-F06-1 | V07's first chapter opens on 2014-12-25 (the dinner) or within the following week (dated caption or continuous scene) | MOD-HIGH | no |
| B6-F06-2 | At least one contest result (a participant's reported amount or percentage) is printed in V07 | MOD | no |
| B6-F06-3 | Mebuki appears at the 12/25 gathering on the page in V07 | MOD | no |
| B6-F06-4 | Mochiko voices her EUR/CHF / no-stop concern to Kurumi aloud (speech, not thought) in V07 | LOW-MOD | no |
| B6-F06-5 | The EUR/CHF position's entry rate, or an account tile (balance / 評価損益) covering it, is printed in V07 | MOD | no |
| B6-F06-6 | A margin, leverage, required-deposit or swap figure for the EUR/CHF position is printed in V07 | LOW | no |
| B6-F06-7 | Kurumi learns, on the page, of Mebuki's liquidation or of Mochiko's 2,000,000 loan to Mebuki in V07 | LOW-MOD | no |
| B6-F06-8 | Kurumi's mother's present-day situation (where she is / her condition) is shown or stated in V07 | LOW-MOD | no |
| B6-F06-9 | Kurumi's father's transfer ("年明けから", V05) is referred to on the page in V07 | LOW-MOD | no |
| B6-F06-10 | Kurumi places no stop-loss order on the EUR/CHF long before any depicted change in that position in V07 | MOD | ES |
| B6-F06-11 | The EUR/CHF position shows a printed figure (rate, P/L, balance) in V07 that differs from entry-level conditions (structural: the position is revisited with a number) | MOD | ES |
| B6-F06-12 | Mebuki's repayment to Mochiko is shown with a new printed amount in V07 | LOW-MOD | no |
| B6-F06-13 | The content of Mebuki's call to her parents (i0044, "話したいことがあんねんけど") is shown or stated in V07 | LOW | no |
| B6-F06-D | (testable at once) The deferred inputs i0001, i0002, i0158–i0161 print no account figure, rate or date beyond those already printed in i0003–i0157 | MOD | no |

Method note: dispositions will be logged with locators in later work; ES items are reported but excluded from calibration.


## 7. Exposure and contamination record

- **Entering exposure (all roles).** Agent D read the owner's brief before any page; Agents B and C did not read it; the principal read it only at the start of its drafting session (S5), after every freeze had been written. The brief names Kurumi, Mebuki, Mochiko and Yasuko and states unverified hypotheses (a malicious Mochiko; a self-destructive trajectory). V06 tests both: no enjoyment of Mebuki's misfortune by Mochiko is shown, and Kurumi's discipline and her repudiation of it are both on the page (reading §D, §G, §H.3).
- **Structural metadata.** Every role saw the spine identifiers and the colour list before its first page. The principal's first inventory printout showed the cover's byte size (not used); Agent B's showed the package byte count (not used); the reviewer probed image dimensions only. No boundary judgment used byte sizes.
- **Freeze timing (principal).** No slip. Each boundary freeze (F02, F04, F08, F10, F12, F13) was written before the next chapter's first page was opened; F05 (after i0056) and F11 (after i0117) supplemented F04 and F10 when a chapter ran a page longer than expected; F01, F03, F06, F07 and F09 were precautionary. F13's header cites shell time 02:43:06 (file time 02:44:00). MAIN_EXIT (shell time 02:46:05) was written after the separator i0155 and the afterword i0156 were opened to establish the end of the main narrative, as MAIN_EXIT itself discloses; an earlier attempt at about 02:45 failed and wrote nothing. **F09 (02:26:30) carries no exposure declaration** although the principal's private real-world association at i0108 (a flat chart near 1.20 with the pair later named on i0111) preceded it; the declaration was first written in F10 (02:28:20). F09-4 was flagged EXPOSURE-SENSITIVE at drafting; its other items are assessed below.
- **Freeze timing checked by the reviewer.** The reviewer compared each freeze's internal shell time and file time with the file times of each role's crops (a crop can only exist after its page was opened). Every principal freeze is consistent with its stated position (internal times 10–45 s before file times); Agent B's F00–F06 are consistent (F06 at 02:45:32, before its first deferred exposure at 02:45:42); Agent D's release point (02:37:20) precedes its first deferred crop (02:47:54). The principal accepts the check.
- **Image caps.** No session of any role exceeded 45 images (principal 45, 45, 45, 44, 6 and, in R1, 8; Agent B 44, 44, 44, 44, 13; Agent D 44, 44, 45, 43, 10; reviewer 42, 34 and 17).
- **Apparatus and paratext.** The six cover and jacket occurrences were deferred for every role by the entrypoint's component scope. The principal also opened the separator i0155 and the afterword i0156 before MAIN_EXIT (disclosed) and the author's strip, colophon and vendor page after it. The back-cover blurb frames Mebuki's work as recovering her FX losses ("FXのマイナスを取り戻すために"); no role adopted it as evidence (reading E055; Agent D h.3; reviewer P1).

**Deferred covers and jacket: first exposure and dispositions.** What each deferred input carries, by the principal's own record (S4, after MAIN_EXIT): i0001, the colour front cover (the four friends in Kurumi's room, Kurumi upside-down on the bed with a phone chart, an onion-helmeted knight toy; the phone's figures were not read); i0002, the flap (the creators' comments, including 炭酸だいすき's list "芽吹ちゃん編がクライマックスに くるみちゃんのお母さん編、新通貨にぴしゃぷりおじさんに中世?"); i0158, the back cover and spine (a collage of V06 panels and the blurb, which leaves the contest winner open, "いったい、誰が勝つんだ〜!?"); i0159, the colour wraparound front (the cover and flap again); i0160, the under-jacket note 「負け演出こぼれ話」 (loss staging made "マイルド"); i0161, the author strip 「でむにゃんは 株を買って打ち切り回避したかったようです」, dated 「2020年 某月某日」. None carries a story event, figure, rate or date later than i0154; the flap's segment list (Mebuki arc climax, mother arc, new currency, the customer, "中世") and the blurb's "大詰め" are the only items that could bear on structural prospects.

| Role | First exposure | Relation to its freezes and judgments | Predictive credit |
| --- | --- | --- | --- |
| Principal (Agent A) | S4, after MAIN_EXIT (02:46:05); shell time 02:47:17 before the first opening; i0001, i0002, i0158, i0159, i0160, i0161 in that order, reading copies one at a time | After the entering state (01:53:57), every freeze F01–F13 and MAIN_EXIT. The drafting session (from about 02:52) and R1 (from 03:41) came after exposure; no drafting or reconciliation judgment uses the deferred content (the blurb's framing is explicitly not adopted, E055) | All 18 entering forecasts, 79 freeze items and the V05-MX dispositions: PRESERVE as to the deferred inputs |
| Financial specialist (Agent B) | S5, after F06 (02:45:32): i0001 02:45:42, i0002 02:45:48, i0158 02:45:54, i0159 02:46:03, i0160 02:46:07, i0161 02:46:13 | After every freeze F00–F06. Its findings were completed after exposure (to 03:00); its component map and §d.14 record the paratext as such, and its §g.4 summary notes that no deferred input carries later information | All 78 freeze items (F00–F06): PRESERVE as to the deferred inputs. B6-F06-D was testable at once after exposure and carries no predictive weight |
| Character specialist (Agent D) | S5: i0001 at 02:47:32, then i0002 (≈02:48), i0158 (≈02:49), i0159 (≈02:49), i0160 (≈02:50), i0161 (≈02:50) | Release point (every main-narrative page logged) 02:37:20; its findings §(b)–(g) were drafted before exposure (S4, to 02:46:36). §(h) and two notes marked "added after the deferred inputs" in §(e) were written after; they concern the paratext itself (the blurb is not Mebuki's motive; the loss-staging note) | D froze no prospect. Findings §(b)–(g): PRESERVE; the §(e) additions are records of paratext and support nothing in the reading |
| Reviewer (Agent C) | Stage 1 S2, 02:15:48: deferred sheets s01 (i0001–i0159) and s02 (i0160–i0161), plus crops of the blurb (i0158) and the flap (i0002) | After its Stage 1 main-narrative write-up (§1–§7, completed 02:15:41; the later §1–§7 edits were balloon and furigana checks of main-narrative pages i0062, i0065, i0141, i0153, i0154). Its §8 paratext cautions P1–P3 came after. Stage 2 (from 03:24:53) came after all exposure and uses no paratext | Stage 1 judgments J1–J14 and traps 1–27: PRESERVE |

**Other out-of-frontier material, item by item.** Outcomes are kept as observed; predictive credit is assessed separately.

- *Principal, post-main pages before MAIN_EXIT (i0155 separator, i0156 afterword).* i0156 shows the four friends lying side by side while Yasuko recounts a yakiniku part-time job (paratext, not a scene of the dinner). MX06-1 (the next chapter continues the 25 December dinner): credit QUALIFIED in advance, weakly touched by the afterword's yakiniku topic; MX06-2 (Kurumi's first announced result is positive): PRESERVE; MX06-3 (Kurumi learns of Mebuki's wipe-out): PRESERVE (the afterword says nothing of knowledge); MX06-4 and MX06-5: EXPOSURE-SENSITIVE for real-history reasons (below). F13 was written before i0155 and is untouched.
- *Principal, private real-world association at i0108 before F09.* F09-1 (i0111 a 第29話 story page): PRESERVE (structural). F09-2 (Kurumi opens a position in the "ユーロ対…" pair; outcome CONFIRMED): credit QUALIFIED — the page's own "見つけた…! 必勝の通貨…!" (i0110) grounds it, but knowledge of the policy's later history makes a dramatic entry expected and the association is not independent. F09-3 (size ≥300; CONFIRMED): PRESERVE (her 300-lot habit, V01 and V05). F09-4 (a printed loss before V06 ends; DISCONFIRMED): already EXPOSURE-SENSITIVE and excluded from calibration. F09-5 (the results meeting held; CONFIRMED, qualified): PRESERVE.
- *Principal, declared real-world knowledge of the policy's later history (F10 onward).* F10-6, F13-2 and MX06-4 were flagged EXPOSURE-SENSITIVE when frozen; MX06-5 is flagged at reconciliation (reviewer C-20) because regret over a withheld warning presupposes harm or its threat. All four are excluded from calibration. The other F10–F13 and MAIN_EXIT items concern page structure, disclosure, figures printed or a stop's absence and do not depend on the depicted market path: PRESERVE.
- *Principal, entering state.* V06-EN-8 (the 300-lot short closed within V06) was flagged EXPOSURE-SENSITIVE at freezing (real late-2014 USD/JPY path) and is excluded from calibration; V05-MX-1 to MX-4 and MX-6 carry their V05 flags.
- *Agent B, declared knowledge.* Real 2008 and late-2014 exchange-rate history (before any page) and the 1.20 floor's real history (at i0108, 02:24) and the negative-rate event (at i0138, 02:36). Its 14 ES items are excluded from calibration. Its F04 (02:26) and F05 (02:29) items on EUR/CHF were frozen after i0110–i0113 had named the pair and the policy on the page, so their page grounding is independent of the recognition: PRESERVE.
- *Agent D and the reviewer, declared knowledge.* Both recognized the 1.20 floor at i0108 or the surrounding sheets and declared it; the reviewer also declared a recollection that the real announcement date differs from the printed 「12月8日」 and did not use it. Neither froze a prospect.

- **EXTERNAL_REFERENCE.** Each role declared general awareness of the title and its adaptation and general knowledge of real 2014–2015 exchange-rate history before or when it arose; the principal, Agent B, Agent D and the reviewer each declared recognition of the real Swiss franc policy at or near i0108 and of the negative-rate event type at i0138. The printed date 「2014年 12月8日 月曜日」 is recorded as printed and was compared with no real date; calendar arithmetic (weekdays) is the only outside check used. Agent D's recognition of a 1998 catchphrase at i0057 is cultural, not title knowledge. No role used a translation, adaptation, wiki or web source.
- **Independence.** Agents B and D worked in their own folders and never opened another role's work; their findings were complete before the principal opened them in R1. The reviewer's Stage 1 closed before the candidate existed. The principal opened no other role's folder before R1. Contact sheets were used only by the reviewer.
- **Corrections of the principal's own record.** Reconciliation corrected these entries of the principal's draft, each on the page or against the principal's own page record: the rule mark is ◎, not "⑩ [?]" (i0143 crop); the "4桁万円" lines are not securely Yasuko's (i0147); the thesis's one-sided judgment of the first cut (i0044–i0046); the placement of the EUR/CHF "commitment" at i0115 (i0115, i0137); the i0124 exit read as a stop that "あえてしてない" reverses (i0123–i0124); "first realized loss"; "minutes after" for Mochiko's close; V06-EN-10's headline.
- **Reconciliation session.** The principal read its own state, component map, freezes and candidate, every independent output (both specialists' findings and exposure records, Agent B's freezes, the reviewer's exposure record, Stage 1 observations and review) and the roles' state files for sessions and pages. It did not open the sealed later volumes, any aborted-attempt folder or any earlier volume's working folder, and used no web source. Its searches of accepted artifacts were targeted: the V01 reading (the 14 February 2014 balance of 300,000, V01 i0044; the absence of a printed realized loss) and the V03 reading (the contest bases, including Mebuki's 613,200).

## 8. Forecast tallies

All tallies use the literal score (reading §M); RELAXED or STRICT results are labelled and reported alongside. Brier scores use the declared analyst convention (LOW 0.20, LOW-MODERATE 0.35, MODERATE 0.55, MODERATE-HIGH 0.70, HIGH 0.85; outcome 1 or 0; a constant 0.5 forecaster scores 0.250). Calibration tallies exclude EXPOSURE-SENSITIVE items. OPEN and NOT TRIGGERED items are outside every tally.

| Set | Literal (confirmed–disconfirmed of n; Brier) | Calibration (without ES items) | Labelled alternatives |
| --- | --- | --- | --- |
| Principal entering state V06-EN-1 to EN-18 | 15–3 of 18; 0.2271 | 14–3 of 17; 0.2285 | RELAXED EN-10 (group-chat reply): 16–2; 0.2438 (the draft's headline). RELAXED EN-10 and EN-12: 17–1; 0.2771 |
| V05 MAIN_EXIT forecasts V05-MX-1 to MX-10 (V05 principal) | 6–4 of 10; 0.2172 | 1–4 of 5; 0.2105 | RELAXED MX-5: 7–3; 0.2072 |
| Principal freezes F01–F13 (79 items; F08-2 OPEN, F12-2 NOT TRIGGERED, F13-2 to F13-6 OPEN) | 41–31 of 72; 0.2028 | 37–30 of 67; 0.1997 | RELAXED F01-6, F02-2, F02-8: 44–28; 0.2042. STRICT F09-5: 40–32; 0.1986 |
| All V06-made principal forecasts (entering state and freezes) | 56–34 of 90; 0.2077 | 51–33 of 84; 0.2056 | — |
| Agent B freezes F00–F05 (64 items) | 43–21 of 64; 0.2256 | 31–19 of 50; 0.2251 | STRICT F00-15 and F03-3: 41–23; 0.2178 (calibration 29–21; 0.2151). RELAXED F00-8: 44–20; 0.2193 (calibration 32–18; 0.2171). Agent B's own marks: 28 confirmed, 19 disconfirmed, 3 partial of the 50 |
| Principal MAIN_EXIT MX06-1 to MX06-5; F13-2 to F13-6; Agent B F06-1 to F06-13 | OPEN (next admitted volume) | MX06-4, MX06-5, F13-2, B6-F06-10 and B6-F06-11 are ES | — |

Predictive credit qualified separately (section 7): F09-2 (outcome CONFIRMED; credit QUALIFIED) and, when it resolves, MX06-1. Only one literal outcome changed at reconciliation, V06-EN-10 (CONFIRMED → DISCONFIRMED); no freeze item's outcome changed. Agent B's dispositions were re-scored literally by the principal: F00-8 (PARTIAL → DISCONFIRMED), F00-15 and F03-3 (PARTIAL → CONFIRMED), F01-10 (DISCONFIRMED → CONFIRMED: the customer reappears at i0035 and i0040–i0042, after the freeze at i0030) and F06-D (CONFIRMED → DISCONFIRMED on the creator-strip date of i0161; outside the tallies).

## 9. Name-and-reference check (handoff contract §15.6)

**Scope sampled.** In the deep reading: the status note and reconciliation summary, the receipt (§A) and the synopsis (§C) in full; the thesis (§D); Movements I, IV, V and XI of §E (E001–E005, E015–E031, E047–E054), because 第26–27話 alternate Mebuki, the customer and Kurumi, 第28話 alternates Kozue, Kurumi as a child, 郁夫 and Kozue's parents, and the Christmas scene alternates Kurumi, Mochiko and Yasuko with unattributed balloons; the character and relationship sections (§H, §I) in full; the exit freeze (§P). In this checkpoint: sections 1–8. In the ledger: the new person notes and rows D001–D032 by search for the same labels.

**Questions asked.** Are known people consistently identifiable? Do titles and role labels serve a purpose? Is anyone reduced to an archetype? Are pronouns unambiguous? Is concealment preserved? Are speaker, thinker and recipient attributed correctly? Does each description respect its knowledge boundary?

| Finding | Location | Classification | Action |
| --- | --- | --- | --- |
| "うわー "4桁万円"も儲かったんだー" / "FXって "簡単" なんだねー" given to Yasuko as settled "dry irony" | Draft E050, H.4, §I | INCORRECT_IDENTITY_OR_ATTRIBUTION (over-confident) | Repaired (C-07): speaker UNRESOLVED (Yasuko MOD, Mochiko LOW-MOD); V06-U14 |
| "a phone" at i0055 without its likely owner | Draft §C, E020 | AMBIGUOUS_REFERENT | Repaired (C-21): most likely Mebuki's (a received message with Mochiko's icon) |
| Kurumi credited with knowing only that Mebuki quit | Draft §I knowledge map, §P | KNOWLEDGE_BOUNDARY_REQUIRED (an omission) | Repaired (C-06): she knows Mebuki has a job (i0140), source unshown |
| Mochiko's last two lines (i0154): thought or speech | E054, §C | Attribution checked | None: re-opened; fuzzy thought bursts, then tail-less ovals with no listener reaction; thought (MOD-HIGH) |
| "Yasuko expects to be the winner" (Agent D) | Not in the reading | INCORRECT_IDENTITY_OR_ATTRIBUTION (of a meaning) | Not imported (D-4) |
| "the woman" before the name 梢 is printed | E021 | KNOWLEDGE_BOUNDARY_REQUIRED | None: the passage records how the page establishes her identity (i0058, i0061) and name (i0065, i0066, i0075) |
| "Kozue" in the 第28話 synopsis heading, before i0065 prints the name | §C | KNOWLEDGE_BOUNDARY_REQUIRED | None: a retrospective chapter heading; the name's arrival is stated in E021 |
| "a blonde girl … she is Mebuki (named on her account box at i0021)" | §C 第26話 | KNOWLEDGE_BOUNDARY_REQUIRED | None: identification by design stated, name's arrival stated |
| 郁夫 as Kurumi's father | §C, E021, H.6, §P; ledger father note | KNOWLEDGE_BOUNDARY_REQUIRED | None: marked INF HIGH throughout; surname by inference |
| "the girl" for the fifteen-year-old Kurumi | E028 | JUSTIFIED_ROLE_REFERENCE | None: Kurumi is named in the same passage |
| "the customer", "the senior worker", "the knight" (ニンニクさん), "the governor", Kozue's parents, Mebuki's mother and father | Throughout | SOURCE_REQUIRED_ANONYMITY | None: none is named on the page; the flap's "ぴしゃぷりおじさん" is paratext and is not applied |
| "the voice" of "芽・吹・" | §C, E020, H.7 | SOURCE_REQUIRED_ANONYMITY | None: never identified; V06-U02 |
| "若葉", "萌智子先輩", "あいつ", "やす子" | §C, E003, E018, E047 | JUSTIFIED_ROLE_REFERENCE | None: a stage name and quoted address forms whose use is the point |
| "disclosure to the creditor" | Reading §M.3 pattern note | JUSTIFIED_ROLE_REFERENCE | None: the lending relation is the point; Mebuki → Mochiko named in the same sentence |
| "あたし" in grill banter given to Kurumi | E054, §K | Attribution checked | None: by balloon placement (INF MOD-HIGH; the reviewer re-opened i0153 and agreed) |
| Process roles in this checkpoint (Agents A–D, coordinator) | Sections 1–8 | JUSTIFIED_ROLE_REFERENCE | None: process roles, not characters |

No unnecessary genericization of a named character remains in the sampled scope. Pronouns in the passages where Kozue, the child Kurumi and 郁夫 alternate (§C 第28話; E021–E031), where Mebuki and the customer alternate (E003–E012) and where Kurumi, Mochiko and Yasuko alternate at Christmas (E047–E054) were checked and resolve correctly. Knowledge boundaries hold: Kurumi is never credited with knowing of the wipe-out, the loan or the salon; Mochiko is never credited with speaking her private objection; the narrated 8 December announcement is never attributed to Kurumi's knowledge.

## 10. Architecture check

The single decision and evidence ledger still suffices. V06 adds 32 decision and evidence episodes (D001–D032), 70 claim records (35 new V06 claims, 30 linked transition records of accepted claims and 5 claims added at reconciliation, C066–C070) and 190 forecast records (112 principal, entering or linked records and 78 attributed to Agent B), and V06 notes for every person entry, with a new "Minor figures (V06)" entry; Kurumi's parents are now named (福賀梢, Kozue; 郁夫, Ikuo, INF HIGH) under their existing entries. The ledger is now large (about 1,900 lines); it remains navigable by ID prefix, but a later synthesis may want a per-volume index of row ranges. One explanatory paragraph of the claim-history section still describes the V01–V05 practice of letting specialists see covers first; from V06 the entrypoint deferred covers for every role. The paragraph is kept byte-identical under the ledger rules; this checkpoint and the source register record the change.

## 11. Exit state

The V06 exit state is the reading's §P. In brief, on Thursday 25 December 2014, evening, with the foreign-exchange market closed for Christmas (i0139–i0140): Kurumi holds, by her own words, a 300-lot EUR/CHF long with no stop order ("ユロスイ 買い(ロング) 300枚!", "あえてしてない!", i0148, i0152); its entry date, rate and fill were never printed; her last printed balance is 18,339,915円 after two USD/JPY cuts on 5 December (−1,743,000 at 18:27; −1,131,000 after the report); she needs "あと566万…とんで85円" for her after-tax target (i0096); she has read her mother's 2008 journal and vowed to win (i0090); she takes her stop-loss lesson from the later clock only, though the same night vindicated her first cut. Mebuki was force-liquidated to 0円 at the 5 December report (−2,610,530; an 11,000 gap kept), told Mochiko she is out and will repay by working (i0051, i0053), told the group only that she quit (i0100), and is working on Christmas, expected later (i0140). Mochiko closed all her longs on 8 December for +7,691,000 (20,993,630円), has no position, promised not to lie, judged Kurumi's trade baseless in thought and asked only whether she had a stop, then chose silence (i0151–i0154). Yasuko has left FX for professional manga and told Kurumi "引き際…とかさ…" (i0147). The contest meeting has convened without a result. Kurumi's parents are named in the flashback (福賀梢 and 郁夫); Kozue's death is not shown in V06; her father's transfer is not mentioned.

## 12. Next candidate operation

**V07** (FXK-JP-V07-W01), after the coordinator accepts this V06 transaction, advances the committed high-water mark to V06 and releases the V07 witness. The V07 principal must read this checkpoint and the V06 reading in full (and the V01–V05 artifacts as needed) and write the V07 entering state before opening any V07 page. The V07-facing forecasts are the principal's MX06-1 to MX06-5 (ledger FXK-V06-F108–F112; MX06-4 and MX06-5 EXPOSURE-SENSITIVE; MX06-1's credit pre-qualified, section 7), F13-2 to F13-6 (F103–F107; F13-2 EXPOSURE-SENSITIVE) and Agent B's B6-F06-1 to F06-13 (F177–F189; F06-10 and F06-11 EXPOSURE-SENSITIVE). Any V07 role that recognizes real-world history of the 1.20 floor must declare it before forecasting the EUR/CHF position.

## 13. Closeout

- Files in this transaction: `readings/FX_KURUMI_V06_DEEP_READING.md` (new), `checkpoints/FX_KURUMI_V06_CHECKPOINT.md` (new), `FX_KURUMI_DECISION_AND_EVIDENCE_LEDGER.md` (targeted rows, person notes, the two boundary sentences and the front matter; version 1.7) and `FX_KURUMI_SOURCE_REGISTER.md` (a new V06 coverage section at the end). The V06 entering state was written earlier, in S1, and is unchanged.
- Read-back: the principal re-read the front matter and spot-checked each changed file, compared the ledger and the source register byte for byte with their pre-edit versions (only the authorized lines changed), and searched the new files for working-plane references.
- Repository checks and validation: NOT_RUN by the principal; they belong to the coordinator. No commit was made and no git command was run.
- Acceptance: the run coordinator's decision.
