---
title: "FX Fighter Kurumi-chan — Checkpoint errata"
artifact_id: FX_KURUMI_CHECKPOINT_ERRATA
artifact_type: checkpoint_errata
series: fx-fighter-kurumi-chan
version: "1.0"
status: canonical
authority_generation: FX_KURUMI-INITIAL
authority_scope: "Attributable errata and dispositions governing the frozen V01–V04 checkpoints: each role's exposure to covers, flaps and jackets, the class of V01 i0165, and the forecast credit and scoring that depend on them"
source_boundary: "FXK-JP-V01-W01 to FXK-JP-V04-W01 main narratives and classified apparatus (V01–V04); V04 unit-end knowledge; no later volume"
created: 2026-11-22
last_updated: 2026-11-22
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
run_id: FXK-RUN-20261119-V01-V10
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
---

# FX Fighter Kurumi-chan — Checkpoint errata

**Spoilers for V01–V04.**

The frozen checkpoints and entering states of V01–V04 remain byte-unchanged. This carrier governs their correction. Where an erratum and a frozen checkpoint differ, the erratum gives the current account, and the frozen text remains the record of what was written at its time. Read each erratum beside the checkpoint section it names. The consequences for current authority are carried in the mutable documents: the [source register](../FX_KURUMI_SOURCE_REGISTER.md), the [decision and evidence ledger](../FX_KURUMI_DECISION_AND_EVIDENCE_LEDGER.md) and the revision notes of the [V01](../readings/FX_KURUMI_V01_DEEP_READING.md), [V02](../readings/FX_KURUMI_V02_DEEP_READING.md), [V03](../readings/FX_KURUMI_V03_DEEP_READING.md) and [V04](../readings/FX_KURUMI_V04_DEEP_READING.md) deep readings.

**Attribution.** Written on 2026-11-22 (UTC−05:00) by the run coordinator's correction delegate for run FXK-RUN-20261119-V01-V10: a Claude Code subagent, launched by the run coordinator, with the model inherited from the coordinator's Claude Opus 5.5 session. It took no part in any V01–V04 reading. It answers the review of PR #695: Codex comments 4654829267 (V01 afterword) and 4654829272 (V01 cover exposure), and the owner's comments 7069996902, 7071612155, 7072226294 and 7073839467.

**Evidence.** Two kinds of evidence are used. First, each role's own V01–V04 working record: state files, page logs, freeze files, and the modification times of those files and of the role's crops. These records stay in the private working plane and are cited here by role, session and time. Second, the delegate's own inspection of the front covers and flaps of V01–V04 (i0001, i0002) and of V01 i0165 in reading copies. The jacket and under-jacket images are described from the roles' records. Times are local (UTC−05:00), and dates 11-19 to 11-22 are in November 2026. A file's modification time shows only its last write, and reading-copy opening times are not recoverable. A "first seen" time is therefore the earliest time the record supports: the start of the session in which the page was logged first, or the saved time of a crop of that page. Freeze times in the tables are the freeze files' saved times, truncated to the minute; a freeze's own stated time can be up to a minute earlier. Labels: OBSERVATION (on the page or in a role's record), INFERENCE, EXTERNAL_REFERENCE (excluded). No real exchange-rate history was used.

**Transitions** follow the repository's vocabulary.

| Transition | Use in this carrier |
| --- | --- |
| `STRENGTHEN` | Supplies facts the frozen record omitted, within its scope |
| `REVISE` | Changes a statement, a classification or a scope |
| `DOWNGRADE` | Narrows the credit or weight a frozen record gave |
| `PRESERVE` | The frozen statement or credit stands after the check |

**Append-only.** A published erratum is not rewritten. A later correction to it is a new erratum that names it.

<a id="summary"></a>
## 1. V01–V04 exposure summary

- **Principal (Agent A).** In every volume the principal deferred the front cover, flap, wraparound jacket and under-jacket images until after its main-narrative exit freeze (MAIN_EXIT). Every entering state, every principal freeze and every MAIN_EXIT forecast of V01–V04 is free of this exposure, including the V01 MAIN_EXIT forecast FX-4 (OBSERVATION: the principals' page logs and state files).
- **Specialists (Agents B and D).** Their briefs told them to open every page of the volume in spine order; only the principal's brief deferred covers and flaps. Each specialist therefore opened the front cover (i0001) and the flap (i0002) first, within minutes of starting its first session and before any freeze or finding of its own. Each reached the wraparound jacket and under-jacket images at the end of the volume, after the main narrative and, for Agent B, after its last freeze of that volume (OBSERVATION: page logs, crop times, freeze times).
- **Reviewer (Agent C).** Its brief told it to triage the whole volume on contact sheets. Its first sheet, s01, holds i0001–i0004, so it saw the cover and flap at the start of Stage 1; the jacket images came on its last sheets. The reviewer sees the whole volume by design and is not a forecasting role, so the question for it is whether any review judgment rests on these images.
- **Root cause.** The entrypoint's component scope says that a cover "is read after the main-narrative freeze", and its multi-agent configuration opens every role "with the same source frontier". The role briefs applied the deferral to the principal alone. Each checkpoint's exposure record describes the principal's deferral; the V01 record states it as if it held for every role.
- **What the images carry** (OBSERVATION, §V01–§V04). V01: a portrait of three girls and two creator comments. V02: Kurumi alone at a desk at night, and the artist's comment that the FX warriors have gathered ("集まってきたFX戦士達") and that their aims cross ("それぞれの思いが交錯する"). V03: Mebuki and Yasuko in an armchair, and the artist's comment "楽しくFXしてた芽吹ちゃんだけど・・・?" ending "現実が突き刺さる!". V04: a figure with a white cat at a keyboard, and creator comments with no narrative content. None of V01–V04 has a next-volume preview, so no role was exposed to a later volume.
- **Dispositions.** V01: no prospective item is qualified ([FXK-ERR-V01-02](#fxk-err-v01-02)). V02: two confirmed Agent B rows lose predictive credit while their observed outcomes stand ([FXK-ERR-V02-02](#fxk-err-v02-02)). V03: the flap's hint about Mebuki had been realized on the page before Agent B's first V03 freeze, so no forecast item and no review judgment is affected ([FXK-ERR-V03-02](#fxk-err-v03-02)). V04: no item is affected ([FXK-ERR-V04-02](#fxk-err-v04-02)). Agent D froze no prospects in any volume. No review judgment in V01–V04 rests on a cover or flap.
- **Not changed.** Every observed outcome on the page; every principal forecast and its disposition; and V01's finding that the cover and afterword trio grouping is promotional and is not evidence of an on-page meeting.
- **Two further corrections** in this carrier do not concern exposure. V01 i0165 is reclassified as an authorial extra ([FXK-ERR-V01-03](#fxk-err-v01-03)). Agent B's V04 forecast B4-J01 is scored as frozen, which gives its V04 tally a literal result beside its relaxed one ([FXK-ERR-V04-03](#fxk-err-v04-03)).

| Erratum | Frozen record and section | Transition | Subject |
| --- | --- | --- | --- |
| [FXK-ERR-V01-01](#fxk-err-v01-01) | V01 checkpoint §7 "Apparatus"; §1 exposure boundaries | `REVISE` | Who saw the covers, and when |
| [FXK-ERR-V01-02](#fxk-err-v01-02) | V01 checkpoint §6, §7 | `PRESERVE` | Specialists' prospective work against the cover; FX-4's provenance |
| [FXK-ERR-V01-03](#fxk-err-v01-03) | V01 checkpoint §4 C-21 | `REVISE` | The class of i0165 and its use in the reading |
| [FXK-ERR-V02-01](#fxk-err-v02-01) | V02 checkpoint §7 "Apparatus" | `STRENGTHEN` | Timing against freezes; the reviewer's sheets |
| [FXK-ERR-V02-02](#fxk-err-v02-02) | V02 checkpoint §6.2; ledger FXK-V02-F095, F111 | `DOWNGRADE` | Predictive credit of two Agent B forecasts |
| [FXK-ERR-V02-03](#fxk-err-v02-03) | V02 checkpoint §6.2, §7 | `PRESERVE` | Every other item and review judgment |
| [FXK-ERR-V03-01](#fxk-err-v03-01) | V03 checkpoint §7 "Apparatus and paratext" | `STRENGTHEN` | Timing against freezes; the principal's freeze kept distinct |
| [FXK-ERR-V03-02](#fxk-err-v03-02) | V03 checkpoint §4, §6.2; ledger FXK-V03-F099–F125 | `PRESERVE` | Item-by-item dispositions |
| [FXK-ERR-V04-01](#fxk-err-v04-01) | V04 checkpoint §7 "Apparatus and paratext" | `STRENGTHEN` | Timing against freezes |
| [FXK-ERR-V04-02](#fxk-err-v04-02) | V04 checkpoint §4, §6.2; ledger FXK-V04-F091–F163 | `PRESERVE` | Item dispositions |
| [FXK-ERR-V04-03](#fxk-err-v04-03) | V04 checkpoint §3 B-22; ledger FXK-V04-F136 | `REVISE` | Literal score of B4-J01 and Agent B's V04 tally |

<a id="v01"></a>
## V01

Frozen checkpoint: [V01 checkpoint](FX_KURUMI_V01_CHECKPOINT.md). Images concerned: the front cover i0001, the flap i0002, the wraparound jacket i0166–i0167, the under-jacket extras i0168–i0169, and the story author's afterword i0165.

| Role | Cover and flap (i0001–i0002) first seen | Its freezes, saved | Jacket images (i0166–i0169) | Record |
| --- | --- | --- | --- | --- |
| Principal (Agent A) | 11-21, session 6, after MAIN_EXIT | F00 11-19 21:29 (before any image); F01 11-20 14:05; F02 18:45; F03 19:17; F04 19:33; F05 11-21 01:24; MAIN_EXIT 01:34. All before | Same session, after MAIN_EXIT; i0163–i0165 also after it | Page log section "Deferred covers / apparatus (opened after MAIN_EXIT.md, session 6)"; MAIN_EXIT text |
| Agent B | 11-19, at the start of session 1 (crop of i0001 saved 21:29:11) | F01 11-19 21:38; F02 11-20 14:05; F03 18:45; F04 19:16. All after | 11-21, session 7 (01:23–01:28), after F04 | First two page-log entries; crop time |
| Agent D | 11-19, at the start of session 1 (probe on i0001–i0002 recorded by 21:29:25) | None | 11-21, session 7 (about 01:23–01:34) | First two page-log entries; exposure record §5 |
| Reviewer (Agent C) | 11-19, Stage 1 session 1 (from 21:28), first sheet s01 | Not a forecasting role | 11-20, Stage 1 session 4 (from 18:57), sheets s42–s43 | Page log, session 1, sheet 1 |

**What the images carry** (OBSERVATION). i0001 shows three girls on sunflowers in front of candlestick glyphs, with the title, the volume number and the credits; it gives no name, figure, date or scene. The accepted reading identifies the three designs as Mochiko, Kurumi and あふぃちゃん. i0002 holds the story author's comment that Kurumi was born of the author's own FX defeat ("敗北の奇跡です") and the artist's comment about drawing from a newcomer's position. Agent B logged i0001 with "No names established", and Agent D logged its three figures as unnamed.

<a id="fxk-err-v01-01"></a>
**FXK-ERR-V01-01 — §7 "Apparatus" and the §1 exposure boundaries (`REVISE`).** The frozen §7 says that "Covers, flap and wraparound were opened only after the main-narrative exit freeze." That is true of the principal only. The correct account is the table above. The principal opened i0001, i0002 and i0163–i0171 only after MAIN_EXIT. Agents B and D opened i0001 and i0002 first, at the start of their first sessions on 11-19 and before any freeze or finding of theirs, and they opened the jacket images last. The reviewer saw i0001–i0002 on its first contact sheet. Read the §1 exposure-boundary cells for Agents B, D and C with these facts added. The rest of the §7 bullet stands. The trio grouping is promotional and is not counted as evidence of an on-page meeting, and the blurb (i0166) restates the premise without later-volume information.

<a id="fxk-err-v01-02"></a>
**FXK-ERR-V01-02 — prospective work against the cover (`PRESERVE`).**
- *The principal's FX-4* (ledger FXK-V01-F048; disposed of in V02 as FXK-V02-F018). It has its own provenance and is not grouped with the V02 rows of [FXK-ERR-V02-02](#fxk-err-v02-02). MAIN_EXIT was frozen on 11-21 (stated 01:35, saved 01:34:54), before the principal opened any apparatus or extra, including the three occurrences that show the trio (i0001, i0164, i0167). The principal opened no other role's work before its reconciliation session. FX-4's only input from outside the page is the one its own rationale names: the owner's brief, which named a "Yasuko". That entering exposure is recorded in V01 §7 and C-01. FX-4's V02 outcome (CONFIRMED, V02 i0147) and its credit stand.
- *Agent B* (freezes F01–F04; ledger FXK-V01-F051–F072). All 22 items were frozen after Agent B saw i0001–i0002. Twenty-one concern the mother's fate, the father, the 2014 time jump, the ¥20M target, the money "that cannot melt", account and margin screens, lot size, stops, averaging down, the cold-open loss, Mochiko's reaction and forced liquidation. Neither image bears on them; the "溶かせない" wording of B-F01-5 comes from i0003 itself. One note concerns B-F02-5 (FXK-V01-F061: a new named character supplies market information in 第2話, 0.55, CONFIRMED by Mochiko). It was written after the cover had shown two further girls beside a candlestick motif. INFERENCE: that is at most a generic hint that other traders matter. The owner's brief, which Agent B had read, already named Mochiko. The credit is unchanged.
- *Agent D.* It froze no prospects. It used the cover figures only as provisional labels, wrote in its state file that its third cover figure should not be identified "until a page does", and identified あふぃちゃん from the pages (i0144–i0152). There is nothing to qualify.
- *Reviewer.* No review judgment rests on i0001 or i0002. In Stage 1 the reviewer listed paratext as non-evidence, and its challenge C-21 opposed the use of paratext in §D and L.7.

<a id="fxk-err-v01-03"></a>
**FXK-ERR-V01-03 — the class of i0165 and challenge C-21 (`REVISE`).** C-21's frozen disposition kept §D's statement that author and publisher framing carries no weight between the theses and called the afterword link in §K INFERENCE LOW. The accepted reading and the register filed i0165 as apparatus. OBSERVATION: i0165 is a full page of handwritten text headed 「原作者あとがき」 and signed でむにゃん, about the web serialization, the creator's thanks and how the author hopes readers will take the work, with a sketch of Kurumi. The entrypoint's component scope names afterwords among the authorial extras inside a volume. Extras are inventoried and classified, and they are not narrative evidence while the supplemental lane is closed. Apparatus is limited to covers, flaps, title and chapter-title pages, contents and the colophon.

The correction is that i0165 is an authorial extra, and its content is not cited as support for any reading. The consequences are these: the register's V01 coverage reclassifies the component row, and its counts become apparatus 6 and extras 4; the V01 reading's revision 1.1 changes §A.2 and its counts, removes the afterword from §D and §K, and rests L.7 on the page (i0086), with the blurb (i0166) noted as apparatus that carries no weight, as §D says; and ledger FXK-V01-C017 records the transition. The competing thesis keeps its label (HYPOTHESIS, MODERATE), and the governing thesis is unchanged. INFERENCE: removing i0165 weakens no page-based argument in §D or L.7, because §D already gave paratext no weight. Supplemental admission is not changed; only the owner can open that lane.

<a id="v02"></a>
## V02

Frozen checkpoint: [V02 checkpoint](FX_KURUMI_V02_CHECKPOINT.md). Images concerned: i0001, i0002, the wraparound jacket i0166–i0167 and the under-jacket extras i0168–i0169.

| Role | Cover and flap (i0001–i0002) first seen | Its freezes, saved | Jacket images (i0166–i0169) | Record |
| --- | --- | --- | --- | --- |
| Principal (Agent A) | After MAIN_EXIT (saved 16:29) | Entering state 15:26 (before any image); F00 15:27 (no forecast of its own); F01 15:38; F02 15:49; F03 16:00; F04 16:02; F05 16:13; F06 16:14; MAIN_EXIT 16:29. All before | After MAIN_EXIT | Page log ("opened only after MAIN_EXIT"); state file |
| Agent B | Session 1, from 15:25 (crop of i0001 saved 15:25:31) | B-F06a 15:35; B-F07a 15:45; B-F08a 16:00; B-F09a 16:09; B-F10a 16:19. All after; the first three list the flap as exposure | Session 5, after B-F10a (16:19–16:21) | Page log; exposure record; freeze headers |
| Agent D | Session 1, 15:23–15:37 (crop of i0001 saved 15:25:34) | None | Session 5 (from 16:12) | Page log; state file |
| Reviewer (Agent C) | Stage 1 session 1 (from 15:23), first sheet s01 | Not a forecasting role | Stage 1 session 2 (from 15:41), sheets s42–s43 | Page log |

**What the images carry** (OBSERVATION). i0001 shows Kurumi curled in a gaming chair at a desk at night, one hand toward the mouse, with a wall clock, a calendar and a bunny-cake poster; no screen, figure or order is legible. On i0002 the story author jokes about a coin bought with V01's royalties, and the artist writes: "運命のいたずらか、集まってきたFX戦士達。それぞれの思いが交錯する第2巻お楽しみ下さい。" INFERENCE: the artist tells the reader that the volume's traders come together and that their aims cross; the comment names no person, pair or scene.

<a id="fxk-err-v02-01"></a>
**FXK-ERR-V02-01 — §7 "Apparatus" (`STRENGTHEN`).** The frozen §7 records that the principal deferred these images, that both specialists read them in spine order at the start (cover, flap) and end of the volume, and that the specialists recorded the flap as exposure. It omits that the reviewer saw i0001–i0002 on its first sheet and i0166–i0169 on s42–s43, the timing against each role's freezes (table above), and the consequence for two forecast rows ([FXK-ERR-V02-02](#fxk-err-v02-02)).

<a id="fxk-err-v02-02"></a>
**FXK-ERR-V02-02 — predictive credit of FXK-V02-F095 and F111 (`DOWNGRADE`).** These rows were credited as confirmed independent forecasts without qualifying the flap exposure (owner comment 7071612155). Outcome and credit are now recorded separately.

| Ledger row | Frozen forecast (Agent B; probability) | Written | Page basis at the freeze (OBSERVATION) | Exposure | Outcome (unchanged) | Predictive credit now |
| --- | --- | --- | --- | --- | --- | --- |
| FXK-V02-F095 | B-F06a-8: Mebuki is introduced to Kurumi in person in V02 (0.6) | 15:34:51, after i0039 and before i0040 | Mebuki on the page (i0004); a novice whose contact is Mochiko (i0007), Kurumi's friend; Agent B's rationale cites Mochiko's "学校の知り合い" / "戦士" | The flap, seen at 15:25 and listed by Agent B as exposure affecting these forecasts | CONFIRMED (i0048) | QUALIFIED. Kept as a frozen forecast written before its outcome, but not counted as clean independent foresight. The page had already put Mebuki in Mochiko's circle, and the principal's clean F01-5, "Mochiko introduces Mebuki to Kurumi" (FXK-V02-F025, MODERATE, saved 15:38), shows that the meeting was foreseeable from the page alone. That page-based credit belongs to F025; F095's own share cannot be separated from the flap's promise |
| FXK-V02-F111 | B-F08a-7: やす子 / あふぃちゃん meets Kurumi on the page in V02 (0.4) | 16:00:47, after i0103 and before i0104 | Yasuko named as the former あふぃちゃん (i0074); she knows Mebuki, hides her own trading from her and warns her; Kurumi advises Mebuki | The flap, listed by Agent B. Agent B also knew the V01 principal's FX-4 from the accepted ledger, which is admitted prior knowledge, not contamination | CONFIRMED (i0147) | NONE. Agent B rated the meeting below even odds (0.4), so as a probability the forecast leaned against what happened (squared error 0.36, against 0.25 for a constant 0.5), and it was written after the flap. The clean forecasts of this meeting are the principal's: V01 FX-4 (MODERATE; FXK-V02-F018), V02-EN-11 (LOW-MOD; F011) and F06-9 (LOW-MOD; F073) |

<a id="fxk-err-v02-03"></a>
**FXK-ERR-V02-03 — every other item and review judgment (`PRESERVE`).**
- *B-F06a-2* (FXK-V02-F089: Kurumi trades again on the page in V02, 0.8, CONFIRMED). The cover shows Kurumi at her desk at night (INFERENCE: consistent with continued trading). It shows no screen, chart, figure or order. By i0039 the page had shown the tempting voice and her "…うん", and the clean principal forecasts V01 FX-1 and V02-EN-1 (both HIGH) predicted the same. The credit is unchanged.
- *Items about the characters' paths*: B-F06a-10 (F097, DISCONFIRMED), B-F07a-6 (F104, PARTIAL), B-F09a-4 (F117, DISCONFIRMED) and B-F09a-6 (F119: Mochiko reappears and reacts, 0.5, CONFIRMED). The flap's promise could at most favour them. Three did not come true as worded, and Mochiko is a standing character on the page throughout the volume. The credit is unchanged.
- *The other 34 Agent B items* concern figures, balances, lot sizes, accounts, leverage, dates, the father, closes and stops (B-F06a-1, -3 to -7, -9, -11; B-F07a-1 to -5; B-F08a-1 to -6, -8, -9; B-F09a-1 to -3, -5, -7; B-F10a-1 to -7). Neither image bears on them. B-F10a-2 to -7 face V03 and carry nothing from the V02 flap about V03.
- *Agent D* froze no prospects (V02 checkpoint §6.2). It read the cover poster and the flap as paratext; Yasuko's identity rests on the caption at i0074. There is nothing to qualify.
- *Reviewer.* No review judgment rests on the cover or the flap. Its Stage 1 disposition of FX-4 cites i0147.

<a id="v03"></a>
## V03

Frozen checkpoint: [V03 checkpoint](FX_KURUMI_V03_CHECKPOINT.md). Images concerned: i0001, i0002, the wraparound jacket i0166–i0167 and the under-jacket extras i0168–i0169.

| Role | Cover and flap (i0001–i0002) first seen | Its freezes, saved | Jacket images (i0166–i0169) | Record |
| --- | --- | --- | --- | --- |
| Principal (Agent A) | After MAIN_EXIT (saved 19:00) | Entering state 17:52 (before any image); F01 18:04; F02 18:07; F03 18:16; F04 18:17; F05 18:18; F06 18:32; F07 18:44; F08 18:46; F09 18:47; MAIN_EXIT 19:00. All before | After MAIN_EXIT | Page log ("deferred; opened after MAIN_EXIT"); state file |
| Agent B | Session 1, 17:49–18:03 (crop of i0001 saved 17:51:09) | FREEZE_01 18:14; FREEZE_02 18:17; FREEZE_03 18:29. All after | Session 5 (18:41–18:54), after FREEZE_03 | Page log; findings §a; crop time |
| Agent D | Session 1, 17:49–18:03 (crop of i0001 saved 17:51:13) | None | Session 5 (from 18:38) | Page log; state file |
| Reviewer (Agent C) | Stage 1 session 1 (from 17:50), first image, sheet s01 | Not a forecasting role | Stage 1 session 4 (from 18:34), sheets s42–s43 | Page log |

**What the images carry** (OBSERVATION). i0001 shows two girls in a pink heart-backed armchair, by styling Mebuki and Yasuko, with no figure, date or scene. On i0002 the story author reports having resumed stock trading and is "早くもピンチ", and the artist writes: "楽しくFXしてた芽吹ちゃんだけど・・・? FX戦士たちがチャートのように上下しちゃう第3巻! 現実が突き刺さる!" INFERENCE: the comment tells the reader that Mebuki's enjoyment of FX meets "reality" and that the traders' fortunes swing. It names no amount, date, mechanism or end state.

<a id="fxk-err-v03-01"></a>
**FXK-ERR-V03-01 — §7 "Apparatus and paratext" (`STRENGTHEN`).** The frozen §7 states that the principal deferred these images and that Agents B, C and D read the flap at the start and recorded it as priming. It adds nothing wrong. This erratum adds the cover, read at the same moment, and the timing against each role's freezes (table above). As owner comment 7072226294 asks, the principal's freeze is kept distinct. The principal froze its entering state at 17:52 before opening any V03 image; it opened no cover, flap or jacket before MAIN_EXIT and no other role's work before its reconciliation session. The flap is within-volume priming; no V04 material existed in the witness.

<a id="fxk-err-v03-02"></a>
**FXK-ERR-V03-02 — item-by-item dispositions (`PRESERVE` for every item).** The decisive fact is an OBSERVATION. The flap's hint had been realized on the page before Agent B's first V03 freeze. On 13 August, in 第12話, Mebuki's 100-lot GBP/USD long falls to the tile "−693,661円" (i0045), and her account is diagrammed at 0円 with the original stake lost (i0051). Agent B wrote FREEZE_01 after logging i0064. At every Agent B freeze the page had therefore shown more than the flap said. The flap's "上下" clause names no character or direction.

| Ledger row | Agent B item (probability) | Outcome | Bearing of the cover and flap | Disposition |
| --- | --- | --- | --- | --- |
| FXK-V03-F099 | B-F1 Mebuki still holds the 10-lot short at the next chapter (0.70) | CONFIRMED | None; the flap names no position | `PRESERVE` |
| FXK-V03-F100 | B-F2 Mebuki ends V03 below her 600,000 redeposit (0.70); a second 0円 (0.35) | UNRESOLVED; NOT SHOWN | The flap's "現実" had been realized at i0045–i0051; nothing on a second loss | `PRESERVE` |
| FXK-V03-F101 | B-F3 Mebuki conceals the size of her losses (0.70); a disclosure scene (0.55) | DISCONFIRMED; CONFIRMED | None | `PRESERVE` |
| FXK-V03-F102 | B-F4 Kurumi's long shown in profit (0.65); more than 40 lots (0.55) | CONFIRMED; CONFIRMED | None; Kurumi is on neither image | `PRESERVE` |
| FXK-V03-F103 | B-F5 A scene sets Kurumi's gain against Mebuki's loss (0.40) | CONFIRMED | None | `PRESERVE` |
| FXK-V03-F104 | B-F6 The tuition obligation is raised again (0.60) | CONFIRMED | None | `PRESERVE` |
| FXK-V03-F105 | B-F7 Yasuko places a new trade (0.55); above 25× (0.05) | DISCONFIRMED; NOT SHOWN | None; the cover shows Yasuko posing, not trading | `PRESERVE` |
| FXK-V03-F106 | B-F8 The contest gets rules, a deadline or stakes (0.25) | CONFIRMED | None | `PRESERVE` |
| FXK-V03-F107 | B-F9 A forced-liquidation term is named on the page (0.45) | CONFIRMED as a term | None; the flap names no term | `PRESERVE` |
| FXK-V03-F108 | B-G1 Mebuki liquidated, or at or near 0円 (0.55) | NOT SHOWN | None beyond the first wipe-out already on the page | `PRESERVE` |
| FXK-V03-F109 | B-G2 Mebuki wakes to a large loss and closes manually (0.30) | DISCONFIRMED | None | `PRESERVE` |
| FXK-V03-F110 | B-G3 The price falls back and she exits at break-even or better (0.15) | DISCONFIRMED | "上下" could favour a rebound; Agent B gave 0.15, and no exit occurred | `PRESERVE` |
| FXK-V03-F111 | B-G4 A forced-liquidation term printed in 第13話 (0.45) | CONFIRMED | None | `PRESERVE` |
| FXK-V03-F112 | B-G5 Mebuki discloses to a friend (0.55); to her family (0.20) | CONFIRMED; DISCONFIRMED | None | `PRESERVE` |
| FXK-V03-F113 | B-G6 Kurumi profits from the rise (0.65) | CONFIRMED | None | `PRESERVE` |
| FXK-V03-F114 | B-G7 Short and long set against each other, noticed (0.35) | CONFIRMED | None | `PRESERVE` |
| FXK-V03-F115 | B-G8 Mebuki seeks a new source of money (0.40) | CONFIRMED by its wording | None | `PRESERVE` |
| FXK-V03-F116 | B-H1 Mebuki's short still open in 第14話 (0.65) | CONFIRMED | None | `PRESERVE` |
| FXK-V03-F117 | B-H2 Mebuki liquidated, or at or near 0円 (0.45) | NOT SHOWN | As B-G1 | `PRESERVE` |
| FXK-V03-F118 | B-H3 Mebuki closes the short herself (0.30) | DISCONFIRMED | None | `PRESERVE` |
| FXK-V03-F119 | B-H4 Mebuki adopts a "Kurumi method" (0.50) | DISCONFIRMED | None | `PRESERVE` |
| FXK-V03-F120 | B-H5 Mochiko's "secret" includes a factor outside skill (0.65) | CONFIRMED | None | `PRESERVE` |
| FXK-V03-F121 | B-H6 Kurumi learns the 700,000 is tuition (0.30) | DISCONFIRMED | None | `PRESERVE` |
| FXK-V03-F122 | B-H7 Mebuki's family learns (0.15) | DISCONFIRMED | None | `PRESERVE` |
| FXK-V03-F123 | B-H8 Mochiko's concealed +10.7% revealed (0.15) | DISCONFIRMED | None | `PRESERVE` |
| FXK-V03-F124 | B-H9 A date later than 2014-10-01 (0.85) | CONFIRMED | None | `PRESERVE` |
| FXK-V03-F125 | B-H10 Mebuki seeks a new money source (0.40) | CONFIRMED by its wording | None | `PRESERVE` |

- *Agent B's V03-facing V02 prospects* B-F10a-2 to -7 (FXK-V02-F122–F127, disposed of as FXK-V03-F027–F032) were frozen in V02 at 16:19 on 11-21, before any V03 image. The V03 flap could not reach them. `PRESERVE`.
- *The principal's forecasts.* The V03 entering-state forecasts, F01–F09 and the V02 MAIN_EXIT forecasts MX-1 to MX-13 are clean of the cover and flap. `PRESERVE`.
- *Review judgments on Mebuki's course,* the flap's subject. C-03 (the exit condition stated more firmly than the page) was decided on i0145 and i0147. C-04 ("ruin" and "holding through" an outcome the volume withholds) was decided on the last Mebuki print (i0158) and i0162, and it argued against the flap's direction. C-06 (the G8 and H10 scores) was decided on the forecasts' wording and on i0077 and i0123. C-09 (the order of Mebuki's panic, i0046) and C-17 (clinical-sounding wording) were decided on page order and on the wording standard. The reviewer's Stage 1 refusal to infer a forced close on 8/13, and its warning against saying that Mebuki took profit or recovered on 10/15, rest on the boxes. Each is not affected: `PRESERVE`.
- *The other review judgments* concern Kurumi, Mochiko, Yasuko, transcription, attribution, labelling and specialist imports (C-01, C-02, C-05, C-07, C-08, C-10 to C-16, C-18 to C-20 and the two import cautions). The cover and flap bear on none of them. `PRESERVE`.
- *Agent D* froze no prospects. Its findings label every paratext item, and no such item was adopted as story evidence. `PRESERVE`.

<a id="v04"></a>
## V04

Frozen checkpoint: [V04 checkpoint](FX_KURUMI_V04_CHECKPOINT.md). Images concerned: i0001, i0002, the wraparound jacket i0158–i0159 and the under-jacket boards i0160–i0161.

| Role | Cover and flap (i0001–i0002) first seen | Its freezes, saved | Jacket images (i0158–i0161) | Record |
| --- | --- | --- | --- | --- |
| Principal (Agent A) | After MAIN_EXIT (saved 21:21), in session 4 | Entering state 20:31 (before any image); F01 20:40; F02 20:41; F03 20:48; F04 20:51; F05 20:56; F06 21:00; F07 21:05; F08 21:09; F09 21:10; F10 21:10; MAIN_EXIT 21:21. All before | After MAIN_EXIT | Page log ("opened after MAIN_EXIT"); state file |
| Agent B | Session 1 (crop of i0001 saved 20:30:20) | FREEZE_00 20:30 (stated 20:29:58), written before any V04 image. FREEZE_01 20:40; FREEZE_02 20:51; FREEZE_03 21:00; FREEZE_04 21:13. These four after | Session 5 (21:25–21:42), after FREEZE_04 | Page log; crop times; freeze headers |
| Agent D | Session 1, from 20:28:53 (crop of i0001 saved 20:29:34) | None | Session 5 (from 21:13:54) | Page log; state file |
| Reviewer (Agent C) | Stage 1 session 1 (from 20:27:57), first image, sheet s01 | Not a forecasting role | Stage 1 session 2 (from 20:44:41), sheets s40–s41 | Page log |

**What the images carry** (OBSERVATION). i0001 shows a purple-haired woman with blue streaks holding a white cat at a lit keyboard, with candlestick glyphs behind her; it gives no figure, document, date or scene. INFERENCE: the figure is Mochiko, as the principal and both specialists read it; the reviewer's sheet note called her Kurumi and was used nowhere. On i0002 the story author reports having tried to save for six months, and the artist says that heat and humidity bring useful nightmares; neither comment has narrative content.

<a id="fxk-err-v04-01"></a>
**FXK-ERR-V04-01 — §7 "Apparatus and paratext" (`STRENGTHEN`).** The frozen §7 is accurate: the principal deferred these images, Agents B and D opened the cover and flap first and the back matter at the end, and the reviewer saw the whole volume on contact sheets in Stage 1. This erratum adds the timing of each role's first exposure against its freezes (table above), as owner comment 7072226294 asks for V04. The principal's entering state, F01–F10 and MAIN_EXIT are clean.

<a id="fxk-err-v04-02"></a>
**FXK-ERR-V04-02 — item dispositions (`PRESERVE` for every item).**
- *Agent B's FREEZE_00* (18 items: B4-F01 to B4-F16 with F07b and F11b; ledger FXK-V04-F091–F108) was written before any V04 image and is free of this exposure.
- *Agent B's FREEZE_01–04* (55 items: B4-G01 to B4-K14; ledger FXK-V04-F109–F163) were written after i0001–i0002. Sixteen of these name Mochiko or her loan: B4-G08, H07, H11, J01, J01b, J02, J03, J04, J08, J09, J10, J13, K02, K04, K11 and K13. The cover could at most suggest that Mochiko matters in V04. It shows no position, loan, condition, document, P/L or date, and the flap is silent. The remaining 39 concern Mebuki's account, loans, liquidation, deposits and work, Kurumi's position and balance, Yasuko, the families, the rate and dates; neither image bears on them. No item is affected.
- *The principal's forecasts* (the entering state, F01–F10, the V03 MAIN_EXIT forecasts disposed of in V04, and the V05-facing MAIN_EXIT forecasts) are clean.
- *Agent D* froze no prospects. It read the cover figure as Mochiko (INFERENCE MODERATE-HIGH), labelled as apparatus. None of its paratext items was adopted as story evidence.
- *Reviewer.* No review judgment rests on i0001–i0002. In Stage 1 the reviewer warned against importing the back-cover blurb (i0158) as a verdict on Mochiko's lending.

<a id="fxk-err-v04-03"></a>
**FXK-ERR-V04-03 — B-22: the literal score of B4-J01 (`REVISE`).** The frozen B-22 disposition adopts Agent B's scoring of its 73 prospects "with two notes", one of them that B4-J01's loan was executed at 2,000,000 and not at the 1,000,000 named. Owner comment 7073839467 asks for the literal score. Agent B froze B4-J01 at 21:00:24 as "Mochiko's 1,000,000 loan is shown executed (cash/transfer handed over, or a deposit attributed to it) in V04" (0.75). The page shows an IOU for "金 2,000,000 円也" (i0145) and a deposit of "+2,000,000円" (i0146) (OBSERVATION). Scored as frozen, B4-J01 is NO.

The correction narrows B-22's adoption. Agent B's scores stand as its reported result, which is a relaxed, event-only score: 28 confirmed and 45 disconfirmed of 73, Brier 0.20164 (published as 0.202). The literal result, with every other disposition held fixed, is 27 confirmed and 46 disconfirmed, Brier 0.20849. The delegate recomputed both independently from ledger rows FXK-V04-F091–F163 (ANALYST CALCULATION: Brier is the mean of (p − o)² over the 73 rows; the B4-J01 term moves from 0.0625 to 0.5625, which adds 0.5/73 ≈ 0.00685). Both results match the owner's figures. The conclusion against the 0.250 of a constant 0.5 is unchanged, and so is the plot finding: Mochiko lent Mebuki the money.

B4-J10 is YES as written, because its frozen parenthesis admits "any yen figure beyond the rate", and the projections "3,000円(日利)", "9万円" (i0100) and "月18万円" (i0105) are such figures. Scored on its head clause alone (an accrued or repayment amount), it would be NO, giving 26 confirmed and 47 disconfirmed, Brier 0.20575. That reading is recorded for transparency and is not adopted. No cumulative tally of Agent B's forecasts across volumes exists in the repository; the figures carried forward are those in V04 reading §M.8 and ledger FXK-V04-F136, both revised.

## Name-and-reference check (handoff contract §15.6)

Scope: this whole carrier. People are named where the page names them: Kurumi, Mochiko, Mebuki, and あふぃちゃん in V01, who becomes Yasuko from the V02 caption at i0074. The cover figures are identified only as INFERENCE where the cover itself gives no name. Agent A–D and "the coordinator" are process roles. The creators are named as credited (でむにゃん, 炭酸だいすき). No knowledge boundary is crossed: nothing here draws on a volume later than V04.
