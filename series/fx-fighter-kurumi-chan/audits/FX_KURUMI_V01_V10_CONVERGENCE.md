---
title: "FX Fighter Kurumi-chan — Convergence of the V01–V10 specialist studies"
artifact_id: FX_KURUMI_V01_V10_CONVERGENCE
artifact_type: convergence_audit
series: fx-fighter-kurumi-chan
version: "1.2"
status: canonical
authority_generation: FX_KURUMI-INITIAL
authority_scope: "Gate G3 convergence of Studies A, B and C: receipt and base drift, what each study argues, agreements, conflicts and their resolution (including the adjudication of the account-regime finding against the psychological and design readings), the FXK-SYN-C rows written or refused, the corrections made at publication, and the full-series-synthesis readiness check (initiation §5.13 item 4)"
source_boundary: "Accepted V01–V10 boundary (FXK-JP-V01-W01 to FXK-JP-V10-W01); V10 unit-end knowledge; no later volume"
created: 2026-11-23
last_updated: 2026-11-23
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
synthesis_id: FXK-SYN-20261123-V01-V10
snapshot_commit: bab0c32bd718f5c278cb8ebb40e3ccd94e7499b7
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
---

# FX Fighter Kurumi-chan — Convergence of the V01–V10 specialist studies

**Revision note (version 1.1).** Revised by the principal integrator at semantic validation (gate G4, transfer FXK-SYN-T-G4-ACCEPT) by targeted edits recorded in the [V01–V10 semantic validation audit](FX_KURUMI_V01_V10_SEMANTIC_VALIDATION.md) (section 3): the label of the account's identity added to AG-04 (V-04), and section 7.4 added to list the corrections made at G4 to the three studies and the integrated synthesis, including a sentence of Study A's section 7.5 that section 7.1 had not listed (V-01). No ruling, disposition or ledger row of this audit changes.

**Revision note (version 1.2, 2026-11-23).** At the G4 close-out of the synthesis (transfer FXK-SYN-T-G4-CLOSE) the front matter's recommended_reasoning_class became PREMIUM_QUALITY_FIRST, the class the [architecture and role-gap audit](FX_KURUMI_ARCHITECTURE_ROLE_GAP_AUDIT.md) (§5.5) assigns to the convergence review, of which this audit is the record, by the coordinator's decision on finding V-14 of the [semantic validation audit](FX_KURUMI_V01_V10_SEMANTIC_VALIDATION.md) (section 11). The two items section 8.5 routed for the reconciliation audit, K-22 and the regeneration of its navigation index, were applied in that audit's version 1.1. No ruling, disposition, row or other text of this audit changes.

This audit records the convergence step of gate G3 in the retrospective synthesis FXK-SYN-20261123-V01-V10, as the [architecture and role-gap audit](FX_KURUMI_ARCHITECTURE_ROLE_GAP_AUDIT.md) fixes it (sections 3.4, 5.2 G3 row, 5.4). Three specialist studies were written in separate fresh contexts at the frozen V01–V10 boundary, from the accepted G1/G2 records at snapshot commit bab0c32bd718f5c278cb8ebb40e3ccd94e7499b7:

- Study A, [Screens, institutions and the allocation of responsibility](../studies/FX_KURUMI_SCREENS_INSTITUTIONS_AND_RESPONSIBILITY.md): who appears to act.
- Study C, [Risk, loss and financial self-destruction across persons](../studies/FX_KURUMI_RISK_LOSS_AND_FINANCIAL_SELF_DESTRUCTION.md): why the actor chose as the page shows.
- Study B, [Obligations, relationships and where the cost of a choice lands](../studies/FX_KURUMI_OBLIGATIONS_RELATIONSHIPS_AND_COST.md): who pays.

After the three texts were frozen, the independent reviewer, in a fresh context, challenged them against one another, against the [decision and evidence ledger](../FX_KURUMI_DECISION_AND_EVIDENCE_LEDGER.md), the [source-completion and longitudinal reconciliation](FX_KURUMI_SOURCE_COMPLETION_AND_LONGITUDINAL_RECONCILIATION.md) and rows FXK-SYN-C001–C006, and adjudicated Study A's account-regime finding against Study C's psychological reading and the design reading. The principal integrator then received the studies, verified the reviewer's challenges on the accepted records and on re-opened pages, decided each conflict, wrote the decided transitions as ledger rows FXK-SYN-C007 to FXK-SYN-C028, published the three studies with the corrections listed in section 7, and recorded the full-series-synthesis readiness check (section 8). The integrated synthesis begins only after that check.

Challenge dispositions use ADOPT, QUALIFY, REJECT and OPEN; claim transitions use PRESERVE, STRENGTHEN, REVISE, DOWNGRADE, REJECT and OPEN. Paths are relative to the project root `series/fx-fighter-kurumi-chan/`. The reviewer's challenges are cited by their IDs K-01 to K-22, its verified agreements by AG-01 to AG-16, and the principal's own finding by P-01.

## 1. Receipt

### 1.1 The delivered texts

| Item | Transfer ID | Author (role, context) | Base named | Bytes | sha256 (recomputed at receipt) | Format | Matches its transfer record |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Study A | FXK-SYN-T-G3-STUDY-A | Financial, causal and information-state specialist, Study A context | bab0c32bd718f5c278cb8ebb40e3ccd94e7499b7 | 92,923 | cfee221be46badad3675af95ba16401343437a87e378f3f67104f19d26af2283 | UTF-8, no BOM, LF; ends with the completion marker; front matter draft_noncurrent, DEEP_SYNTHESIS | yes |
| Study B | FXK-SYN-T-G3-STUDY-B | Character, relationship and Japanese-register specialist | bab0c32bd718f5c278cb8ebb40e3ccd94e7499b7 | 113,031 | e02a993becb10a067bfb7e048ebb6b9c78c296dc4398f41c55c7dab3d8f2b460 | as A | yes |
| Study C | FXK-SYN-T-G3-STUDY-C | Financial specialist, in a fresh context separate from its Study A context | bab0c32bd718f5c278cb8ebb40e3ccd94e7499b7 | 98,311 | 1e3db8fdbd4f3a60cbe26f7893a64c190449bc32e93a146118528a69df96cae7 | as A | yes |
| Convergence challenges | FXK-SYN-T-G3-CONVERGENCE-REVIEW | Independent reviewer, fresh context | bab0c32bd718f5c278cb8ebb40e3ccd94e7499b7 | 63,419 | 1e7daf485646d02dff7e1ae0cbff8c86eab4fa4974a7c03e6b68313595956cd4 | as A | yes |

Each frozen text was hashed at receipt and compared with the completion line of its transfer record; all four match. Each transfer record names its transfer ID, the base commit, the repository inputs it relied on, the working inputs the brief allowed (its own role's earlier dossier and the binding briefs) and its output path (handoff contract §3).

### 1.2 Scope and independence

- **Scope.** Each study stays inside its question and scope as the role-gap audit fixes them (A §3.1, B §3.2, C §3.3), and each maps every acceptance criterion of its record to a section (A §16, B §17, C §13); the mappings hold on reading, with the exceptions disposed of in section 5 (A did not apply the G3 row's rule on V06's mixed narrative authority, K-08; A's criterion 4 is met in substance, its tally corrected by K-01).
- **Routed claims.** No study decides another's routed claims: the agency strand of FXK-V02-C002 is argued only by C; the two Mebuki thesis pairs (FXK-V03-C001/-C002, FXK-V04-C001/-C002) only by B; A argues the account-regime finding and leaves C's models and B's question of who pays alone (AG-14).
- **Independence.** Each transfer record states that the study did not read the others; nothing in the three texts contradicts that (each names the others only through the role-gap record). Study C was written in a context separate from Study A's, as role-gap §3.3 and §5.3 require.
- **Boundaries.** Verified by reading and by search of the three texts (AG-12, AG-13): no forecast row (FXK-Vnn-Fnnn) is cited in any study; no item facing events after V10 is scored or anticipated; no method, method step or item of the V08–V09 crisis is named, and Kozue's death is named as suicide and nothing more; no clinical label is used (psychological terms are explanatory models); no paratext is used as evidence and the V05 bonus strip is not used (FXK-SYN-C003); no external reference; あふぃちゃん until V02 i0074, "Kurumi's mother" for V01–V05 and Kozue from V06 i0065; the father's given name appears only inside Kozue's quoted lines; the writer and the artist are never referred to by pronoun.

### 1.3 Base drift

The three studies and the challenge record name the same base commit, bab0c32bd718f5c278cb8ebb40e3ccd94e7499b7, which is also the snapshot of this audit. The current target was compared with that base on the records the studies rely on: the ledger is 868,518 bytes, the size the reconciliation audit (section 8.5) records after the G2 transaction; rows FXK-SYN-C001–C006 stand at the line positions all four texts cite (L2413–2418); every ledger row the studies name as a claim's last explicit transition was found as named (section 6); the entrypoint records the current gate as G3; no `studies/` or `characters/` document existed before this publication. No accepted record that the studies use changed between the base and the target. **Drift class: irrelevant, for all three studies and for the challenge record.** No claim is reopened on account of drift (handoff contract §10; long-series protocol §11).

## 2. What each study argues

### 2.1 Study A — who appears to act

Study A separates four things the page can attribute — who decided, who executed, who is the grammatical agent of the page's statement of the outcome, and who bears the loss — and shows the page giving them to different parties. It inventories fourteen classes of rendered value and institutional text with provenance (status boxes, platform screens, broker communications, liquidation wording, orders, documents, law as lecture, credit products, public authority, narrator verdicts, private institutions, wealth captions, charts, withheld figures), maps nine episodes (R1–R9) and four counter-cases (C1–C4), and argues five claims:

- **A1** Market institutions execute every printed account-ending loss and are never the grammatical agent of a decision; the broker addresses a named person once, to state her obligation; the only institutional decision printed is a court's release (V09 i0104).
- **A2** Institutional figures are exact where their operands are printed; error lives in persons' speech and self-made documents; page form gives the reader the figure before, or instead of, the character, and withdraws it from her at a nadir. What is missing on the page is the rule, not the number.
- **A3** The account regime decides the reach of a ruin, not whether it happens — the qualified survivor of the account-regime finding, tested episode by episode and against the psychological and design readings (adjudicated in section 4).
- **A4** Law and market rules reach the page as lecture, footnote, a friend's hedged speech or a machine's refusal; they appear as maxima that are used and as prices on exits (restricted at convergence, K-06).
- **A5** The narrator assigns the cause of ruin to the person and describes institutions as mechanism or impartial force; characters personify the market as a hostile agent; the narrator's irony loosens its verdicts without moving responsibility onto an institution.

A shared section follows one household's money across generations through the institutions that hold, label and move it (merged with Study B's B1 at convergence, K-09).

### 2.2 Study B — who pays

Study B traces ten obligations (O1–O10: the father's 300万, Kozue's household money, Mebuki's tuition, her card and student credit, Mochiko's 2,000,000 at 109.5%, Kurumi's broker debt, the 2014 tax, promises, the duty to warn, the V08 letter) from creation to their state at V10, records five refused obligations, maps who knew what and when, and grades conduct toward persons on the readings' scale (ignorance, negligence, recklessness, manipulation, cruelty), never a market outcome. Its four strands are Mochiko's ties in both directions per volume, with her two voices and their crossing; concealment and disclosure in the Fukuga family across two generations; the vocabulary of responsibility (自己責任, 責任, 迷惑, 大人); and Mebuki's agency (the V03 and V04 thesis pairs). Its claims:

- **B1** Concealment carries the first cost of a choice to people who do not know of it, deferring and enlarging it; the series turns when a disclosure is chosen (V09).
- **B2** Between friends, credit for trading is harm and care is not money; family money is harm when taken in concealment and help when offered openly.
- **B3** Responsibility borne alone and hidden disables help; shared, it becomes payable (proposed as the extension of FXK-V04-C015 with FXK-V07-C023).
- **B4** The largest sum lands on no one the page depicts; the costs the page dwells on are not money and land on the nearest.
- **B5** Mochiko changes as a person toward Kurumi (V07–V09), and her doctrine does not; the change is also one of narrative function; her motive stays open.
- **Strand (iv)** Mebuki's harm is self-authored throughout; Mochiko's conduct toward her is a confirmed and admitted wrong whose causal weight the page declines to fix.

### 2.3 Study C — why the actor chose as the page shows

Study C tabulates the decision episodes of eight persons with alternatives, information held and action status (intended, submitted, executed, realized, realized by the broker), tests thirteen explanatory models (never diagnoses) against confirming and disconfirming episodes, and argues one central finding in four claims:

- **SC-1** One visible sequence of self-destruction — a leveraged position held without a stop past a point the holder had named, funded from money labelled as protected, ended by the broker — recurs in Kurumi, Mebuki, Kozue and Yasuko with drivers the page differentiates.
- **SC-2** The hinge is sizing against a reference point (a target, a break-even, a sum owed to the dead), not only the failure to cut; in Kurumi the failure to cut changes kind, so that her V07 ruin follows a doctrine adopted after she had shown she could cut.
- **SC-3** Insight into one's own errors is usually accurate and usually inert at the moment of decision; restraint holds when something outside the trading moment carries it.
- **SC-4** Funding chains end by exhaustion or by outside hands, not by the trader's judgment of her position.

Its section 5 states what the psychological reading must concede to institutional co-production and what it holds against it; its section 7 argues the agency strand of FXK-V02-C002.

## 3. Agreements

The reviewer verified sixteen agreements against the accepted records (AG-01 to AG-16); the principal checked each against the record named and, where marked in section 9, on the page. They are adopted as common ground for the integrated synthesis:

| # | Agreement | Studies |
| --- | --- | --- |
| AG-01 | Seven account-ending losses: six realized by a broker (Mebuki 31 October and 5 December 2014; Kozue 6 October 2008; Kurumi 15 January 2015 and the V08 night; Yasuko 2013), one with no shown mechanism (Mebuki, 13 August 2014); none closed by its holder's order | A, C |
| AG-02 | The strong form of the account-regime finding is not supported | A, C |
| AG-03 | The person sets the exposure before any institution acts; no ruin shows an institution deciding | A, C |
| AG-04 | Kurumi chose the domestic account herself in V02, for less "即死リスク" and for tax (V02 i0017); the debt arose in the account chosen to lower risk (that the V07 account is that domestic account: INFERENCE HIGH; V06 i0013, i0046, i0095; FXK-SYN-C014) | A, C |
| AG-05 | Mebuki's and Kozue's ruins are as large as their own funding made them; a floor moved Mebuki's loss onto her lenders | A, B, C |
| AG-06 | What stopped Kurumi after the ruin was held by others and by an institution: the discharge, payment "地道に", her father's management of her wages (V09 i0104, i0106–i0107) | A, B, C |
| AG-07 | Kurumi's V06 losses were hand cuts, no stop order shown for the V05 short, followed by a repudiation of the stop rule argued from goal proximity | A, B, C |
| AG-08 | Mebuki's harm is self-authored; Mochiko's deception and the hedged loan are a confirmed, admitted wrong whose causal weight the page leaves undetermined | B; consistent with A and C |
| AG-09 | The household money's path (2008; V01; the V02 return; the V09 bankbook), the late revelation of the 300万's purpose, and the identical 1,005,144 as design, Kurumi's notice of it unstated | A, B, C |
| AG-10 | The 2014 tax is the one obligation shown surviving the bankruptcy, partly unpaid in April 2017 (V10 i0045); 3,807,983 is never a 2017 balance | A, B, C |
| AG-11 | The reconciliation audit's usage rules (sections 4.11 and 9) are stated and kept, with the exceptions of K-09 and K-11 | A, B, C |
| AG-12 | The boundary rules (V08–V09 crisis, the V01 death, clinical labels, forecasts, the vote, paratext, the V05 strip) are kept | A, B, C |
| AG-13 | Names and knowledge boundaries are kept | A, B, C |
| AG-14 | No conflict with FXK-SYN-C001–C006; routed claims argued only by the study assigned; FXK-V01-C011 never restated in its V01 wording | A, B, C |
| AG-15 | Strand (i) of Study B answers the question for which a standalone study of Mochiko's ties was proposed | B |
| AG-16 | Each study maps its acceptance criteria, with the exceptions recorded in section 5 | A, B, C |

Four further convergences matter for the integrated synthesis, and each was checked on the records cited:

1. **The funding regime.** Study A's "a floor does not stop debt; it moves it to whoever funded the refunding" (A §7.7; R3–R4), Study C's SC-4 and Study B's O4–O5 and B2 describe one Mebuki chain from three sides: the broker's 0円 floor did not bound her ruin, because cards, a student loan and Mochiko's 2,000,000 at 109.5% refunded the account after each zero (V04 i0016–i0020, i0056, i0088, i0145; reconciliation audit §4.5). It can be stated once, with all three cited.
2. **Restraint lodged outside the trading moment.** A's counter-case C3, B's B3 and C's SC-3 agree that what held Kurumi after V08 was disclosure and controls held by her father and an institution (V09 i0063, i0104–i0107), and that the restraints which held before a loss were acts that changed the money's structure at once (V03 i0124; V10 i0132).
3. **Mochiko's information position.** A (§13 item 4: knowledge of rules), B (§4: every party's figures, V03–V08) and C (§9 item 4: a friend's capitulation as a signal) supply the three inputs to the integrated synthesis's required section "Information as capital" (role-gap §3.5), qualified by K-10.
4. **Early reward postpones who pays.** B (§5.4), C (§9 item 2, as corrected by K-17) and A (§13 item 6) read the reconciliation audit's consolidated wording of FXK-V01-C011 ("an arc of early reward setting up later ruin", §5.5 row 1) from three sides: early rewards trained the sizing (C), let chance operate at leverage beyond the narrator's stated domestic cap (A), and let risk land on no one until the later volumes showed who had been carrying it (B).

## 4. Adjudication: Study A's account-regime finding against Study C's psychological reading and the design reading

### 4.1 The question

At G2 the financial specialist offered a finding — *the size of each ruin depends more on the account regime than on the trader's last decision* — which the role-gap audit did not adopt; it required Study A to argue it against two rivals, the psychological reading (Study C) and a design reading in which institutions are plot devices, and the convergence review to adjudicate (role-gap §3.1 criterion 4, §3.4, §7). Study A tested the strong form over nine episodes, did not adopt it and proposed a qualified claim A3 ("the account regime decides the *reach* of a ruin … while the person's sizing, stop policy and funding decide the stake and whether a ruin happens", A §7.7). Study C did not argue A's finding; it conceded magnitude, timing, leverage on offer and "equal shock, unequal exposure", held that exposure precedes the regime's action in every ruin, proposed a test (a ruin with modest exposure made by the regime alone) and offered a compatibility formula (C §5). The reviewer adjudicated all three readings (challenge record §3). The principal's ruling follows; each point was verified on the record or page cited.

### 4.2 What the page fixes

- **The ends.** The boxes labelled 海外口座 that show an end print exactly 0円 (V06 i0039; V08 i0020); Mebuki's V04 end is 0円 with no regime label in the accepted record (V04 i0012). The one negative end is Kurumi's V07 box, which prints no regime label: 「くるみ FX口座残高 -1億153万4644円 (-1億2028万4479円) 強制ロスカット」 (V07 i0118, re-opened for this audit). The account is domestic by the V06 boxes (「くるみ FX口座残高(国内口座)」, V06 i0013, re-opened; i0046, i0095) and continuity: INFERENCE HIGH.
- **The gap.** "一部のFX業者は 適切なレートを 提示できず", 「この区間 取引成立せず」 (V07 i0114, narrator). No gap is printed for the V08 night, whose fills and rates are unprinted (FXK-V08-C004).
- **The rule.** No stop-out level is printed for Kurumi's or Mebuki's broker (U-06, OPEN). One threshold is printed, for Yasuko's broker in the 2013 flashback: 「証拠金維持率が100%…」 beside 「自動ロスカットが執…」 (V10 i0076, re-opened). The only sentence on any page that a domestic account can end in debt is Mochiko's unspoken thought, after she tells Mebuki that Kurumi has certainly taken on a large debt: 「そういえば 芽吹は 国内口座の仕様を 知らないんだっけか」 (V08 i0106; V08 reading E037).
- **The choice.** Kurumi chose the domestic account in V02 as the lower-risk option and for tax: "これからは 即死リスクが 小さい 国内FX口座で 戦う…!" (V02 i0017, re-opened by Study A and by the reviewer). No page shows that she knew the account could go below zero (A §12 item 2).
- **The contrast case.** Kozue's 2008 account, regime unlabelled, ended positive after a forced close shown without any trading halt: 「口座残高 1,005,144円」 (V06 i0082).
- **The exposure.** Every ruin's exposure is set, and for Kurumi from V06 stated, before the broker acts: "あえて してない!" (V06 i0152); "読みが外れても 損切りとか 考えない", "ゼロになるか 1億円になるか" (V08 i0006); Mebuki's refundings (V04 i0015–i0032, i0103–i0119); Kozue's pots (V06 i0071–i0077).

### 4.3 Rulings

1. **The strong form is refused.** Corrected as K-01 requires, Study A's own episode test gives no episode in which the regime outweighs the person's decisions. R1 (V01: no loss realized) and R6 (V06: hand cuts that end nothing) are not account-ending losses and leave the tally. Over the seven that remain: for, none; joint, two (R7, R8); against, three (R3, R4, R5: each as large as the person's funding made it, reconciliation audit §4.5 and §4.8); undecidable, two (R2, R9). Study C's stricter test also finds nothing (C §5). The strong form holds for none of the seven account-ending losses. **REJECT** as a finding; recorded in FXK-SYN-C018.
2. **The psychological reading governs the stake and whether an adverse move can end the account.** **ADOPT** SC-2 (with its concession corrected, K-05): the person sets size, stop policy and funding before any institution acts, and the size is set against a reference point. Study A agrees (A §4 regularity 1; §7.5).
3. **A3 survives in a narrower decomposition.** **QUALIFY.** Three things, not two, fix the V07 figure: *exposure* (the person: 300 lots, no stop, chosen in December; ≈24.4× conditional, FXK-V06-C033), *discontinuity* (the market: the gap, V07 i0114) and *account terms* (whether a loss beyond the equity becomes the customer's). The 84.4% Study A assigned to the regime (101,534,644 ÷ 120,284,479, ANALYST CALCULATION) is an accounting split of the printed figures into equity lost and excess owed, not a causal share. The excess is as sensitive to size as to terms: ANALYST CALCULATION, conditional on a loss linear in lot count at the same unprinted fill and valid under either reading of the parenthetical, 18,749,835 ÷ (120,284,479 ÷ 300) = 46.8, so a position of 46 lots or fewer, filled as the 300 were, would have ended at or above zero. Size and gap decide *whether* a loss outruns the stake; the account's terms decide *who carries* what outruns it.
4. **Regime or gap: OPEN.** Behaviour does not explain why V07 ended in a debt and V08 at 0円: the V08 refusal of a stop is stated in advance and the size is larger (V06 i0152 against V08 i0006; 300 against 1000 lots). The residual rivals are the regime and the gap, and the page does not separate them: no gap is printed for V08, the one forced close shown without a halt left a positive balance (V06 i0082), and the specification is named only in a character's thought after the fact (V08 i0106). Study A's INFERENCE MODERATE-HIGH that "the regime, not the behaviour" explains the difference is lowered to **INFERENCE MODERATE** for the specification, rather than the gap alone, as the explanation.
5. **The funding regime is a shared finding.** **ADOPT** (section 3, item 1).
6. **Regime choice is endogenous in choice and exogenous in consequence.** Kurumi chose the domestic account herself, but to reduce "即死リスク" and for tax, under a belief no page corrects before V07 (V02 i0017). The choice was hers; the tail it carried was not chosen knowingly on any page. This refines Study C's "partly endogenous" and is why the psychological reading cannot absorb the regime: it explains why she held 300 lots without a stop, not why the account she chose to reduce risk turned the gap into a debt (C §5, "the regime's irony cuts both ways", says the same).
7. **The design reading is compatible, OPEN as to intent, and stronger than Study A allowed on one point.** Both studies are right that design does not dissolve causation inside the fiction and that any claim about real markets is EXTERNAL_REFERENCE. But Study A's main argument against design — that "the boxes label the regime whenever it matters" (A §7.6) — fails for the decisive box (V07 i0118, K-03). The page withholds three things exactly where the regime would decide the outcome: the broker's rule (U-06), the regime label on the ruin's box, and any statement of the specification until a later volume, where it arrives as one character's unspoken knowledge about another's ignorance (V08 i0106). That is how a plot that needs a protagonist's debt for V08–V09 would deliver one. Study A's sentence that "the work asks the reader to understand [the regime] as a cause" is lowered to EVALUATION MODERATE. The design reading stays weak where Study C says it is: it cannot remove the exposure, which every ruin prints and the persons reason out in advance; design and psychology share the premise that the plot tests the person's exposure.
8. **Consequence for who pays.** Read with A3 as qualified, Study B's B4 acquires its mechanism: the domestic terms made the V07 excess pass *through a person* — as Kurumi's debt of 101,534,644円, the V08 reckoning, the V08–V09 crisis and a bankruptcy whose costs came, by INFERENCE MODERATE-HIGH, from the father's 300万 (V09 i0074–i0075; V09-U14) — before the discharge (V09 i0104) moved it, by the page's only stated creditor's logic (V08 i0119), onto a creditor the page never shows. Where an overseas account ended at 0円, any excess would have stayed with the broker from the start; the page never shows that case (HYPOTHESIS). The regime's practical reach in V07–V09 is the passage of the excess through Kurumi's life, not its final resting place.

### 4.4 The adjudicated wording (written as FXK-SYN-C018)

> In V01–V10 the person sets the exposure — size, stop policy and funding — and so decides whether an adverse move can end the account and how large the stake is (Study C, SC-2; Study A, section 4). Whether a loss outruns the stake depends on that exposure together with a market discontinuity: the one shortfall on the page follows the gap of V07 i0114, while the one forced close shown without a halt (Kozue's, 6 October 2008, regime unlabelled) left a positive balance (V06 i0082). Who carries a loss that outruns the stake depends on the account's terms: in the one case the page shows, the customer, as a debt of 101,534,644円 (V07 i0118, i0130), under a specification named only in Mochiko's unspoken thought (V08 i0106). The accounts labelled overseas that are shown ending end at exactly 0円 (V06 i0039; V08 i0020), none shown meeting a gap; where an account is refunded after each zero, the floor moves the loss to whoever funded the refunding (Mebuki, V04–V06). Knowledge of the regime is held unequally and learned by losing, never from the institution (V03 i0046; V08 i0105–i0106). The strong form — that a ruin's size depends more on the account regime than on the trader's decisions — holds for none of the seven account-ending losses.

**Labels.** OBSERVATION HIGH for the printed ends, the gap narration and the thought; INFERENCE MODERATE for the specification, rather than the gap alone, as the V07/V08 difference; EVALUATION MODERATE-HIGH for the decomposition as the series' account of reach. **What would overturn it.** A page showing an overseas account below zero after a gap, or a domestic account stopping at or above zero after one; a printed rule for Kurumi's broker showing that the V07 debt arose without the gap; a page showing that Kurumi knew the domestic tail when she chose it in V02 (which would move the reach, too, into her decision). None exists within V10.

The integrated synthesis uses this wording, not Study A's original A3 sentence, A §13 item 7 as drafted, or Study C's compatibility formula. The character monographs that cite the account regime use it too.

## 5. Conflicts and challenges, disposed of

The reviewer raised no BLOCKING challenge, ten MATERIAL (K-01 to K-10) and twelve MINOR (K-11 to K-22). The principal verified each on the record or page named before deciding it, and adds one finding of its own (P-01). "Landed" names where the correction appears: the study section corrected at publication (section 7), the FXK-SYN-C row, or a routing.

| ID | Severity; studies | Point | Disposition and reason | Verified on | Landed |
| --- | --- | --- | --- | --- | --- |
| K-01 | MATERIAL; A against C | A's tally counts two non-ruins (R1, R6) and scores R7 "for" on an accounting split (84.4%) | ADOPT. Tally over the seven account-ending losses: for 0; joint 2; against 3; undecidable 2; R1 and R6 kept as illustrations outside it; the 84.4% described as the share of the parenthetical beyond her equity | A's own R1 ("No loss realized") and R6 rows; V07 i0118 re-opened; CALC in section 4.3 | A §2 item 3, §7.3, §7.7, §14 SA-5 cell; FXK-SYN-C018 |
| K-02 | MATERIAL; A | A §13 item 7 restates the strong form ("the regime decided the size of each") and says the reward and ruin occurred "in different regimes" | ADOPT. The sentence is removed; the V08 ruin's box is labelled 海外口座 (V08 i0020), the regime of the V01 reward (V01 i0075). Replacement mechanism per section 4 and K-17 | A's own R8 row and the V08 reading §F.1 | A §13 item 7 |
| K-03 | MATERIAL; A | "The boxes label the regime whenever it matters" is false for the decisive V07 box | ADOPT. The V07 account's domestic identity is INFERENCE HIGH (V06 boxes; continuity); its label is absent from i0118; the omission is evidence the design reading may use | V07 i0118 and V06 i0013 re-opened | A §2 item 3, §7.6; section 4.3 (7) |
| K-04 | MATERIAL; A, bearing on C | The V07/V08 comparison cannot separate regime from gap; SA-1 graded too high | ADOPT. The regime strand graded INFERENCE MODERATE; "regime or gap" recorded as the unresolved rival | V08 i0106 (V08 reading E037); V06 i0082; FXK-V08-C004 | A §7.4, §7.7; FXK-SYN-C014 |
| K-05 | MATERIAL; C against A | C §5 says no rule is printed for any broker, omits V08 i0106 and assigns the shortfall to the gap alone | ADOPT. C's concession corrected; none of C's claims changes | V10 i0076 re-opened; V08 reading E037 | C §5; FXK-SYN-C026 |
| K-06 | MATERIAL; A against C | A4's counter-cases: the unit rule refused a small order (not one "that would have taken most of her savings"), meeting A4's own overturn condition; the V03 reserve is Kurumi's own act before any ruin of hers | ADOPT. A4 restricted to what market and legal institutions do on the page; C1 reclassified as self-imposed and C4 as friction; EVALUATION MODERATE-HIGH; C's SC-3 classification of the V03 reserve and Nana's half rule adopted | V10 i0105 re-opened (100株 against 「売買単位:1000株」); V03 i0124 (re-opened by C); A §10 contrary evidence | A §2 item 4, §4 C1 and C4, §8; FXK-SYN-C019, C027 |
| K-07 | MATERIAL; C, with B | "Not a compulsion" in the agency strand is kept by silence against C's own evidence | QUALIFY (P-01). ADOPT the OPEN state of "not a compulsion" on the evidence of the V02 retirement reversed within weeks (V02 i0040 → i0102), the V02 assent to her father broken by the relapse (V02 i0038 → i0130) and the decided V01 cut she could not execute (V01 i0131, i0135; FXK-V01-C010). REJECT the V05 item (i0155 → i0158) as a reversed retirement: the resolution is conditional on a target never reached within V10 | V05 i0155 re-opened ("目標達成したら ちゃんと FX引退しなきゃ!"); V05 reading §G table ("retirement was conditional on the target … and she trades to reach it"); V06 i0096 (target not reached); V02 reading E010, §C | C §7; FXK-SYN-C007 |
| K-08 | MATERIAL; A, against B and C | A does not mark V06's mixed narrative authority (a binding G3 rule) and grades two 2008 facts too high | ADOPT. V06's authority marked once in A §1 and at each use; V06 i0080 described as a first-person caption in the journal-framed flashback; the parents' ignorance INFERENCE MODERATE-HIGH (V06 E026); the husband's as Kozue's SELF_REPORT (V06 i0082). A1's grammatical point survives: the sentence is first person in either channel | V06 i0080 re-opened (two first-person sentences in white type on black bands above and below Kozue's face, not a drawn journal page); role-gap §5.2 G3 row | A §1, §3 row 3.4, §4 R5, §5, §10, §15; FXK-SYN-C016, C021 |
| K-09 | MATERIAL; A and B | Overlapping new rows on the household money; "lender of last resort" frames unconsented takings as lending; A merges discovery and chosen disclosure | ADOPT (MERGE). One row hosted by B1 with A's institutional strand; "source of last resort — taken without consent in 2008 and 2014, offered with consent in 2015 (its use for the costs INFERENCE MODERATE-HIGH)"; "it returns only when its owner learns of it — by discovery in V02, by chosen disclosure in V09; Kozue's never returns" | Reconciliation audit §9 item 11 and §4.3; B §7.3 and O2; V09 i0074–i0075 | A §2 item 6, §10, §14 SA-8 cell; B §10 B1; FXK-SYN-C021 |
| K-10 | MATERIAL; C, with A and B | "Information as capital": the inputs are partial and C overstates Mochiko's uniqueness | ADOPT. The required section takes all three inputs (figures, B §4; rules, A §13 item 4; a friend's capitulation as a signal, C §9 item 4) and names Kurumi's V02 contrarian use of Mebuki (B §5.1, V02 reading §I grade) as the counter-case to uniqueness; motive stays with B §6 (FXK-V01-C005 OPEN) | V03 i0150 (re-opened by B); B §5.1 | C §9 item 4; section 8.6 |
| K-11 | MINOR; C, with the reconciliation audit | The domestic 25× cap is printed at V01 i0075, not i0074 | ADOPT for C; the G1 locator is routed (K-22) | Re-opened by Study A and by the reviewer (both i0074 and i0075); V01 reading "i0074–i0075" | C §1.2, §5 |
| K-12 | MINOR; C, A | "After the ruin she chooses the overseas account": the account existed from 7 January | ADOPT | V07 i0060 re-opened ("さっき海外口座に入れた10万円で勝負!") | C §5; A §7.5 |
| K-13 | MINOR; A | R1's "could exist only in the overseas regime" rests on the narrator's statement of the domestic cap and meets the V04 tension | ADOPT. Margin argument kept, labelled INFERENCE HIGH on the narrator's statement (≈59× and ≈74× against 25×), with V04-U02 noted | V01 i0075 (NARRATOR_PRESENTATION); reconciliation audit §9 item 4 | A §4 R1 |
| K-14 | MINOR; A | SA-2 extends FXK-V10-C014's scope; contest figures are reported among the persons, sometimes falsely | ADOPT. Written as REVISE (extend), EVALUATION HIGH as a format, with the contest caveat | Ledger L2208; V03 i0090 (verified by A) | FXK-SYN-C015 |
| K-15 | MINOR; C | The motive grade for FXK-V03-C012 is too uniform for V06 | ADOPT. HIGH for V05 and V07–V08; MODERATE-HIGH for the V06 size, with perceived control (C's model 6) as co-model | C §2.1 V06 row and model 6 (V06 i0115) | FXK-SYN-C010 |
| K-16 | MINOR; C | SC-4's overturn condition is met in substance by Yasuko's V04 exit | ADOPT. SC-4 confined to the four self-destructive chains; Yasuko's V04 exit recorded as its one counter-case (no protected-money chain shown behind it) | V04 i0046–i0047 per the V04 reading and reconciliation audit §4.6 | C §4.4; FXK-SYN-C028 |
| K-17 | MINOR; C | "The early rewards fixed the reference point" contradicts C's own model 4 | ADOPT. "Her mother's loss fixed the reference point; the early rewards trained the rule of sizing to it; the V07 ruin is that rule meeting a gap in an account whose excess fell on her" | C model 4 and SC-1 (V01 i0015–i0020; FXK-V01-E002) | C §9 item 2 |
| K-18 | MINOR; B, with C | Mochiko's December close: two wordings inside B | ADOPT (not a defect of fact). Harmonized: "closed in the scene of Mebuki's report, after her reply (V06 i0050–i0052; clock time unprinted); that the close answered the report as a contrary signal is INFERENCE MODERATE" | V06 i0052 re-opened (close and box 「萌智子 FX口座残高(国内口座) 20,993,630円」 after the reply, before a second message); V06 reading E015–E017 | B §6.2, §9.3 |
| K-19 | MINOR; B | The hedge that supersedes "her motive is unstated" is overstated in size | ADOPT. "A self-reported rationale, coherent in direction and overstated in size (reconciliation audit §4.4); any further motive OPEN" | Reconciliation audit §4.4; ledger L751 | B §9.4; FXK-SYN-C012 |
| K-20 | MINOR; A, C | Figural staging at the decisive order (the Death figure, V06 i0116–i0117; Mochiko's monster, i0151–i0153) is used by no study | ADOPT. No separate home (role-gap §3.6 holds); cited as contrary evidence to A5 and as evidence for SC-3, with the V06 reading's own rival that the figures are genre staging, not authorial verdicts | V06 reading E041, §D, §L | A §9; C §4.3; FXK-SYN-C020, C027; section 8.6 |
| K-21 | MINOR; B | "The whole of a 300-lot position's risk" | ADOPT. "Nearly all (about 94% of the equity at the deposit, ANALYST CALCULATION, conditional on the open loss at that moment)" | Reconciliation audit §4.2 (3,811,600; −629,000) | B §5.4 |
| K-22 | MINOR; for the coordinator | Two wording defects in the accepted G1 record: "never as a threshold" (§4.1) against V10 i0076, and the cap's locator V01 i0074 (§4.1, §4.11, §9 item 4) for i0075 | ADOPT as a finding; no edit here (the reconciliation audit is outside this transaction). Routed to the coordinator for a note or erratum line when the G1 record is next revised; the usage rules are unaffected and U-06 stays OPEN for Kurumi's and Mebuki's brokers | V10 i0076 re-opened; V01 i0075 as K-11 | Section 8.5 |
| P-01 | Principal; C, and K-07 | Study C's SC-3 lists "目標達成したら ちゃんと FX引退しなきゃ!" (V05 i0155 → i0158) among rules that promised a future act and failed, and K-07 counts it as a retirement reversed within hours | The resolution is conditional on reaching the target, which is never reached within V10 (V06 i0096: "あと566万…"); the 300-lot short that follows is sized to reach it (V05 E057). It never came due. Removed from the failed-promise list; SC-3 stands on its other four cases | V05 i0155 re-opened; V05 reading §G table and E056–E057 | C §4.3; FXK-SYN-C027, C007 |

No challenge was rejected whole. The one point on which the principal departs from the reviewer is the V05 item of K-07 (P-01).

## 6. Claim transitions written or refused

Twenty-three transitions were proposed (Study A eight, Study B nine, Study C six). Twenty-two rows are written, FXK-SYN-C007 to FXK-SYN-C028, appended after FXK-SYN-C006 in the ledger's claim-and-forecast table, each naming the claim's last explicit transition, its evidence and its disposition, and linking its study and this audit. One proposal (SA-8) is merged into another row rather than written alone. Every claim named as a last explicit transition was found in the ledger or the named reading section as the study states it.

| Row | Proposal | Claim (last explicit transition) | Proposed | Written | Reason |
| --- | --- | --- | --- | --- | --- |
| FXK-SYN-C007 | C §10 row 1 | FXK-V02-C002, agency strand (FXK-SYN-C004: agency OPEN pending G3) | REVISE | REVISE, with "not a compulsion" OPEN | K-07 as qualified by P-01 |
| FXK-SYN-C008 | B §14 row 1 | FXK-V03-C001 (FXK-V05-C049, STRENGTHEN; earlier FXK-V04-C028) | REVISE | REVISE as proposed | Self-authorship and the admitted wrong both on the page (V05 i0131, i0145; V07 i0014–i0019); causal weight undetermined (V03-U05) |
| FXK-SYN-C009 | B §14 row 2 | FXK-V03-C002 (V04 reading §M PRESERVE, OPEN; no row) | REVISE | REVISE as proposed | Decision strand strengthened; exclusivity downgraded; exogenous blow kept for 31 October only |
| FXK-SYN-C010 | C §10 row 2 | FXK-V03-C012 (FXK-V10-C065; reconciliation audit §5.5 row 4) | REVISE, motive EVALUATION HIGH (V05–V08) | REVISE; HIGH for V05 and V07–V08, MODERATE-HIGH for the V06 size; perceived control as co-model | K-15 |
| FXK-SYN-C011 | B §14 row 3 | FXK-V04-C001 (FXK-V05-C034, STRENGTHEN with refinement) | STRENGTHEN | STRENGTHEN as proposed | Debt and labour realized (V07 i0011–i0012; V09 i0114); the hedge already recorded in FXK-V05-C034 |
| FXK-SYN-C012 | B §14 row 4 | FXK-V04-C002 (V05 reading §M PRESERVE, OPEN; no row) | REVISE | REVISE, with the hedge's overstatement in size | K-19 |
| FXK-SYN-C013 | B §14 row 5 | FXK-V04-C015 with FXK-V07-C023 (FXK-V09-C065, REVISE) | REVISE (extend) | REVISE (extend) as proposed | Changes scope from motif to tested argument (claim B3), as role-gap §2.4 (b) requires for a row |
| FXK-SYN-C014 | A SA-1 | FXK-V07-C001, regime strand (FXK-V08-C041) | REVISE (extend), INFERENCE MODERATE-HIGH | REVISE (extend), regime strand INFERENCE MODERATE; "regime or gap" OPEN; the V07 box's missing label noted | K-03, K-04 |
| FXK-SYN-C015 | A SA-2 | FXK-V10-C014 (NEW in V10) | STRENGTHEN to HIGH, scope extended | REVISE (extend); EVALUATION HIGH as a format; contest caveat | K-14 |
| FXK-SYN-C016 | A SA-3 | NEW claim A1 | NEW, EVALUATION HIGH | NEW as proposed, V06 i0080 relabelled | K-08; overturn condition unmet (V07 i0118, V10 i0076 verified) |
| FXK-SYN-C017 | A SA-4 | NEW claim A2 | NEW | NEW as proposed | Rests on reconciliation audit §4.12; no conflict found |
| FXK-SYN-C018 | A SA-5 | NEW claim A3 | NEW, EVALUATION MODERATE-HIGH; strong form not proposed | NEW in the adjudicated wording of section 4.4; strong form recorded as refused (none of the seven) | Section 4; K-01 |
| FXK-SYN-C019 | A SA-6 | NEW claim A4 | NEW, EVALUATION HIGH | NEW, restricted; EVALUATION MODERATE-HIGH | K-06 |
| FXK-SYN-C020 | A SA-7 | NEW claim A5 | NEW, EVALUATION MODERATE-HIGH | NEW as proposed, with the form's figures of danger among the contrary evidence | K-20; bears on FXK-SYN-C006 without deciding it |
| FXK-SYN-C021 | B §14 row 6, with A SA-8 | NEW claim B1, merged with A's household chain | NEW, INFERENCE MODERATE-HIGH (B); NEW (A) | NEW, one merged row with A's institutional strand | K-09 |
| FXK-SYN-C022 | B §14 row 7 | NEW claim B2 | NEW, INFERENCE MODERATE | NEW, with the shared funding-regime finding cross-referenced | Section 3 item 1 |
| FXK-SYN-C023 | B §14 row 8 | NEW claim B4 | NEW | NEW, with the mechanism of section 4.3 (8) | B4's rival named Study A's question; answered here |
| FXK-SYN-C024 | B §14 row 9 | NEW claim B5 (related FXK-V01-C005 OPEN; FXK-V07-C075 PRESERVE) | NEW, INFERENCE MODERATE | NEW as proposed | No conflict with A or C |
| FXK-SYN-C025 | C §10 row 3 | NEW claim SC-1 | NEW | NEW as proposed | No conflict with A or B |
| FXK-SYN-C026 | C §10 row 4 | NEW claim SC-2 | NEW | NEW, with C's concession corrected and the interface of FXK-SYN-C018 | K-05; section 4.3 (2) |
| FXK-SYN-C027 | C §10 row 5 | NEW claim SC-3 | NEW | NEW; absorbs the V03 reserve and Nana's half rule as self-made structure; the V05 resolution removed from the failed promises | K-06; P-01 |
| FXK-SYN-C028 | C §10 row 6 | NEW claim SC-4 | NEW | NEW, scope confined to the four chains; Yasuko's V04 exit as its counter-case | K-16 |
| — | A SA-8 | NEW household chain | NEW | Not written alone: merged into FXK-SYN-C021 | K-09: same transfers; B's distinction between discovery and chosen disclosure; usage rule §9 item 11 |

**Refused as a finding, not as a proposal.** The strong form of the account-regime finding was proposed by no study; it is recorded as refused in FXK-SYN-C018 and in section 4.3 (1).

**Not proposed, and rightly so on the record.** FXK-V01-C005 (Mochiko's motive; OPEN in substance, unchanged); FXK-V01-C010 (stands as revised; SC-2 places it without changing its grade); FXK-V01-C011 (its standing is the integrated synthesis's question, starting from the reconciliation audit's §5.5 row 1; the arc's mechanism is offered by A and C as reconciled in K-02 and K-17); FXK-V02-C001 (PRESERVE; a rival in C §7); FXK-V03-C008 (relish; its state is recorded by FXK-V08-C063); FXK-V07-C075 (PRESERVE); FXK-V01-C012 and FXK-V05-C002 (governed by FXK-V09-C071 and FXK-V09-C068); FXK-SYN-C006 (V01's competing thesis; its standing is argued in the integrated synthesis); FXK-V09-C008 and FXK-V09-C032 (beyond V10; OPEN and untouched).

## 7. Corrections made at publication

Each study was published from its frozen text by a byte copy, then changed only by the edits below. Common to all three: front matter `status: canonical` and `do_not_use_as_current_authority: false` (`last_updated` 2026-11-23 and every other key unchanged); a short "Publication note" under the title; the trailing completion marker removed; the sibling studies linked as `./…` where each text names them, and this audit linked where a correction points to it; a one-line note at the head of the proposals section naming the rows written. No working-plane reference was present in any text. Every other sentence is the author's.

### 7.1 Study A

| Section | Correction | Decided by |
| --- | --- | --- |
| Introduction | Study C and Study B linked as siblings | Publication |
| §1 | A paragraph marking V06's mixed narrative authority (journal entries as Kozue's written self-report; captions a narrator's; scenes beyond a journal; framed as Kurumi's reading) | K-08 |
| §2 item 3 | Finding A3 restated: the V07 box's missing label; the strong form holds for none of the seven account-ending losses; the three-part decomposition | K-01, K-03, K-04 |
| §2 item 4 | Finding A4 restricted to maxima used, exits priced, a refusal and release after ruin; the V03 reserve as Kurumi's own act; the unit rule as friction | K-06 |
| §2 item 6 | "Lender of last resort" replaced by "source of last resort", with consent and inference marked; the tax reserve as a pot Kurumi made herself | K-09, K-06 |
| §3 row 3.4 | V06 i0080 described as a first-person caption with mixed authority | K-08 |
| §4 R1 | The margin argument labelled INFERENCE HIGH on the narrator's statement of the cap (≈59× and ≈74×), with V04-U02 | K-13 |
| §4 R5 | Mixed authority marked; the parents' ignorance INFERENCE MODERATE-HIGH; the husband's as Kozue's SELF_REPORT; i0080 as a first-person caption | K-08 |
| §4 C1, C4 | C1 reclassified as self-imposed; C4 as friction on a below-unit order | K-06 |
| §5 | "Kozue's journal" at V06 i0080 replaced by the first-person caption in the journal-framed flashback | K-08 |
| §7.3 | R1 and R6 marked outside the tally; R7's verdict changed to joint, the 84.4% described as an accounting split; the tally restated over the seven account-ending losses | K-01 |
| §7.4 | Mochiko's correction of Mebuki attributed precisely (spoken correction; specification in thought); the regime strand lowered to INFERENCE MODERATE with "regime or gap" unresolved | K-04 |
| §7.5 | The overseas account existed from 7 January (V07 i0060) | K-12 |
| §7.6 | "The boxes label the regime whenever it matters" corrected for V07 i0118; the evaluation lowered to MODERATE; the omissions named as evidence for the design reading | K-03 |
| §7.7 | Disposition and the A3 block restated with the corrected tally, the accounting split and the INFERENCE MODERATE grade; pointer to the adjudicated wording (FXK-SYN-C018) | K-01, K-03, K-04 |
| §8 | Claim, evidence bullet and overturn condition restricted; EVALUATION MODERATE-HIGH | K-06 |
| §9 | Contrary evidence: the form's figures of danger at the decisive order (V06 i0116–i0117; i0151–i0153), with the reading's genre-staging rival | K-20 |
| §10 | 2008 row: consent and inference marked, mixed authority; item 1 reworded (source of last resort; discovery against chosen disclosure; Kozue's never returns); item 3: the protective pot as Kurumi's own | K-08, K-09, K-06 |
| §13 items 1 and 7 | Item 1's "an account without a floor" replaced by "an account whose excess fell on the customer"; item 7's sentence restating the strong form removed and replaced by the adjudicated mechanism | K-02, K-04 |
| §14 | Note of the rows written; the SA-5 cell's tally corrected; the SA-8 cell's "lender" replaced by "source" | K-01, K-09 |
| §15 | Attribution of V06 i0080 corrected | K-08 |

### 7.2 Study B

| Section | Correction | Decided by |
| --- | --- | --- |
| Introduction | Study A and Study C linked as siblings | Publication |
| §5.4 | "The whole of a 300-lot position's risk" replaced by "nearly all (about 94% of the equity at the deposit, ANALYST CALCULATION)" | K-21 |
| §6.2 V06 row | Mochiko's close harmonized: in the scene of Mebuki's report, after her reply; clock time unprinted; the contrary-signal reading INFERENCE MODERATE | K-18 |
| §9.3 | The same harmonization | K-18 |
| §9.4 | FXK-V04-C002: the hedge as a self-reported rationale, coherent in direction and overstated in size | K-19 |
| §10 B1 | One sentence adding Study A's institutional strand (the broker's box records 入金, not whose), to which the merged row refers | K-09 |
| §10 B4 | One sentence recording the mechanism decided at convergence | Section 4.3 (8) |
| §14 | Note of the rows written | Publication |

### 7.3 Study C

| Section | Correction | Decided by |
| --- | --- | --- |
| §1.2 | The cap's locator V01 i0075 | K-11 |
| §1.4 | Study A and Study B linked as siblings | Publication |
| §4.3 | Evidence: the form's figures of dread at the EUR/CHF order (V06 i0116–i0118; i0151–i0153); the V05 resolution removed from the failed promises, with the reason | K-20, P-01 |
| §4.4 | Claim confined to the four chains; Yasuko's V04 exit recorded as the counter-case | K-16 |
| §5 | Magnitude bullet: the shortfall as the joint product of the gap and the account; Yasuko's printed 100% threshold; Mochiko's thought at V08 i0106; the cap's locator V01 i0075. Second bullet: the overseas account opened on 7 January | K-05, K-11, K-12 |
| §7 | Assessment and disposition: "not a compulsion" stays OPEN, with its evidence | K-07, P-01 |
| §9 items 2 and 4 | The arc's mechanism corrected; Mochiko's uniqueness restricted to using a friend's capitulation as a signal, with Kurumi's V02 contrarian use as the counter-case | K-17, K-10 |
| §10 | Note of the rows written; in the SC-3 proposal, V05 i0155 removed from the failed promises | Publication; P-01 |

### 7.4 Corrections made at semantic validation (G4)

Made by the principal integrator at gate G4 on the independent reviewer's findings, each verified on the accepted records and disposed of in the [V01–V10 semantic validation audit](FX_KURUMI_V01_V10_SEMANTIC_VALIDATION.md) (section 3). Each artifact named is now version 1.1. None changes a ruling of section 4, a disposition of section 5 or a row of section 6.

| Artifact and section | Correction | Finding |
| --- | --- | --- |
| Study A §7.5, *Adjudication* | The sentence "For the series' largest figure the regime is the larger determinant in magnitude" replaced by the adjudicated decomposition: the regime decides who carries what outran the stake (84.4%, an accounting split, not a causal share); size and the gap decided that it outran it; for the recurring ruins the person's funding decides the size. Section 7.1 above did not list this sentence | V-01 |
| Study A §5; integrated synthesis §9 item 3 | The V04 and V05 position panels described as equivalent (same heading, differently worded sentence, different platforms), not as the same panel in the same layout | V-06 |
| Study A §13 item 6 | "The fact" replaced by "the finding (INFERENCE HIGH on the narrator's statement of the cap …)" | V-10 |
| Study A §14, SA-1 and SA-6 | Each superseded proposal marked with the form written (FXK-SYN-C014; FXK-SYN-C019) | V-09 |
| Study B §3.1, O1 | "Discharged as a debt in V02" replaced by "Returned on discovery in V02 (V02 i0024–i0026)" | V-11 |
| Study C §3, model 7; integrated synthesis §3.4 | Unit and ANALYST CALCULATION label for the V06 same-night saving and the V01 150枚 share | V-07 |
| Study C §6.1 | "ideation and planning" replaced by "thoughts of death and a plan" | V-12 |
| Study C introduction | "Kozue's death (V01 …)" replaced by "the death of Kurumi's mother (V01; named Kozue from V06 i0065 …)" | V-13 |
| This audit §3, AG-04; integrated synthesis §1.2 | The identity of the V07 account with the V02 domestic account labelled INFERENCE HIGH (FXK-SYN-C014) | V-04 |
| Integrated synthesis §5, claim I-4 | Graded INFERENCE MODERATE by its weakest strands (FXK-SYN-C022, C023), with the per-strand grades stated | V-03 |
| Integrated synthesis §3.4, §15.4 | Nana's 368,000円 described as the planned amount it is (「Kani購入予定金額」), bought at 741 on 24 April (V10 i0142) | V-05 |
| Integrated synthesis §3.2, §15.1, §15.4 | The thinker of V10 i0044 named as Inago, as the V10 reading fixed the attribution | V-08 |
| Integrated synthesis §8.3, §10 row 3, §14.2 | Pointers stating that the proposed transitions P-1 to P-4 are not yet written and that the ledger still carries FXK-SYN-C006 OPEN | V-02 |
| Integrated synthesis §12 and where the persons are named | Links to the character monographs published at G4 | G4 publication |

## 8. Full-series-synthesis readiness check (initiation §5.13 item 4)

Role-gap §3.4 requires that, before the integrated synthesis begins, this audit record every proposed row as written or refused with a reason, every convergence disagreement, and the state of every QUALIFIED_PENDING monograph.

### 8.1 Proposed rows

All twenty-three proposals are disposed of (section 6): twenty-two written as FXK-SYN-C007 to FXK-SYN-C028, one (SA-8) merged into FXK-SYN-C021 with its reason. None was refused outright. The strong form of the account-regime finding, proposed by no study, is recorded as refused. No row was written for any claim no study proposed, and no forecast row was touched.

### 8.2 Disagreements, with their state

| # | Disagreement | Between | State at this audit | Where recorded |
| --- | --- | --- | --- | --- |
| D-1 | The account-regime finding against the psychological reading | Study A (and the financial specialist's G2 recommendation, role-gap §7) and Study C | Resolved: strong form refused; A3 qualified in a three-part decomposition; SC-2 adopted; C's concession corrected | Section 4; FXK-SYN-C018, C026 |
| D-2 | The design reading | Study A, Study C, the reviewer | OPEN as to the page's purpose; compatible with both readings inside the fiction; stronger than Study A allowed on the withheld label, rule and specification | Section 4.3 (7) |
| D-3 | Regime or gap as the reason V07 ended in a debt and V08 at 0円 | Study A and the reviewer | OPEN; the specification over the gap at INFERENCE MODERATE | Section 4.3 (4); FXK-SYN-C014, C018 |
| D-4 | Institutional protection (A4) against self-made restraint (SC-3) for the V03 reserve and Nana's purchase | Study A and Study C | Resolved for Study C's classification | K-06; FXK-SYN-C019, C027 |
| D-5 | "Not a compulsion" in the agency strand of FXK-V02-C002 | Study C and the reviewer | OPEN; no page after V09 tests it | K-07; FXK-SYN-C007 |
| D-6 | Whether the V05 resolution to retire at the target was reversed | The reviewer and Study C against the principal | Resolved on the V05 reading: conditional, never due | P-01 |
| D-7 | The household money: "lender" against unconsented taking; discovery against chosen disclosure | Study A and Study B | Resolved in one merged row | K-09; FXK-SYN-C021 |
| D-8 | Mochiko's uniqueness in using another trader's behaviour as information | Study C and Study B | Resolved by restriction, with Kurumi's V02 use as the counter-case | K-10 |
| D-9 | A standalone study of Mochiko's ties | The character specialist (G2) and the role-gap audit | Closed: Study B's strand (i) answers the question (AG-15); no new home | Role-gap §3.6, §7 |
| D-10 | A study of manga form | Role-gap §3.6 (reassess if a formal question went unanswered) | Closed: the one gap found, the figural staging of V06 i0116–i0118 and i0151–i0153, fits A5 and SC-3 | K-20 |
| D-11 | Kizuna's qualification (DEFERRED_EVIDENCE recommended against QUALIFIED_PENDING at MODERATE) | The character specialist and the qualification audit | Carried from G2, unchanged; the monograph obligation stands | Role-gap §7 |
| D-12 | The father's confidence (LOW-MODERATE against MODERATE) | The character specialist and the qualification audit | Carried from G2, unchanged | Role-gap §7 |
| D-13 | The V08 「すみませんでした」 sheet (recalled image or new note); the reading of the V07 parenthetical; the V10 confidence disagreements (Nana's +500 row; whether Kizuna lives alone) | Carried from G1 (reconciliation audit §1.5) | UNRESOLVED, unchanged; the 84.4% split holds under either reading of the parenthetical (A §12 item 3) | Reconciliation audit §1.5 |
| D-14 | Kurumi's motive: restitution against appetite; the narrator's "呪い" against her "根っからの欲張り" | Within the record, not between the studies | OPEN by design; the integrated synthesis may not settle it on either self-account (C §8, §9 item 3; reconciliation audit §5.5 rows 2 and 11) | Studies B and C |
| D-15 | Mochiko's motive (FXK-V01-C005); whether her V06–V07 silence was negligence or respect | Within the record | OPEN (B §6.5, §12) | Study B; FXK-SYN-C024 |

### 8.3 QUALIFIED_PENDING monographs

| Subject | Person | Intended path (plain text until accepted) | State at this audit |
| --- | --- | --- | --- |
| FXK-P001 | Fukuga Kurumi | characters/fukuga-kurumi-manga.md | In authoring or review in its own fresh context chain; not accepted; no document in the repository |
| FXK-P002 | Kurumi's father (福賀; 郁夫 by INFERENCE HIGH) | characters/fukuga-ikuo-manga.md | As FXK-P001 |
| FXK-P003 | Fukuga Kozue | characters/fukuga-kozue-manga.md | As FXK-P001 |
| FXK-P005 | Kogane Mochiko | characters/kogane-mochiko-manga.md | As FXK-P001 |
| FXK-P006 | Yamashi Mebuki | characters/yamashi-mebuki-manga.md | As FXK-P001 |
| FXK-P008 | Takane Yasuko | characters/takane-yasuko-manga.md | As FXK-P001 |
| FXK-P020 | Zenba Nana | characters/zenba-nana-manga.md | As FXK-P001 |
| FXK-P021 | Tsukimori Kizuna | characters/tsukimori-kizuna-manga.md | As FXK-P001 |

None of the eight is accepted; self-containment and fidelity are pending G4 in the ledger's qualification table, which this transaction does not change. The character layer is incomplete, and the integrated synthesis may not describe it as complete while any of the eight is unaccepted (role-gap §3.5). The monographs' directed-relationship duties draw on Study B and their decision duties on Study C; for their integration this audit adds: where a monograph cites the account regime it uses the wording of section 4.4, not A §13 item 7 as drafted; where it cites V06's 2008 chapter it marks the chapter's mixed authority (K-08); Kurumi's V05 resolution to retire is conditional and never came due (P-01); and the studies, now published, may be linked from `characters/` as `../studies/…`.

### 8.4 Ledger

Rows FXK-SYN-C007 to FXK-SYN-C028 are appended after FXK-SYN-C006, in the claim-and-forecast table's columns, with the table header, its explanatory paragraphs and every earlier row unchanged; the front-matter version moves from 1.13 to 1.14. The ledger moves from 868,518 bytes and 3,472 lines to 889,110 bytes and 3,494 lines (20,592 bytes added; ANALYST COUNT). The synthesis's additions across G2 and G3 stand at 29,496 of the 60,000-byte budget, and the file stays under the 1,000,000-byte threshold of the size rule (role-gap audit §2.5).

### 8.5 Routed to the coordinator (no edit made in this transaction)

- K-22: two wording defects in the accepted [reconciliation audit](FX_KURUMI_SOURCE_COMPLETION_AND_LONGITUDINAL_RECONCILIATION.md) — §4.1's "never as a threshold" (V10 i0076 prints 「証拠金維持率が100%…」 for Yasuko's 2013 broker) and the cap's locator V01 i0074 in §4.1, §4.11 and §9 item 4 (the cap is printed at V01 i0075) — for a note or erratum line when that record is next revised. The usage rules are unaffected; U-06 stays OPEN for Kurumi's and Mebuki's brokers.
- The reconciliation audit's ledger navigation index (§8) predates rows FXK-SYN-C007–C028 and is to be regenerated from IDs when that record is next revised (role-gap §2.5).
- The entrypoint's links to the three studies and to this audit, and its gate state, are the coordinator's to edit.

### 8.6 What the integrated synthesis takes from convergence

- The adjudicated wording of section 4.4 (FXK-SYN-C018) for the account regime, not Study A's original A3 sentence, A §13 item 7 as drafted, or Study C's compatibility formula.
- "Information as capital": all three inputs — every party's figures (B §4), knowledge of rules (A §13 item 4) and a friend's capitulation used as a signal (C §9 item 4) — with Kurumi's V02 contrarian use of Mebuki as the counter-case to uniqueness; motive questions referred to Study B and left OPEN.
- Manga form: the boxes, captions and withheld figures (A §§3, 6), with the figural staging of V06 i0116–i0118 and i0151–i0153 and its genre-staging rival.
- FXK-V01-C011 from the reconciliation audit's §5.5 row 1, with the mechanism reconciled in K-02 and K-17: her mother's loss fixed the reference point; the early rewards, at leverage beyond the narrator's stated domestic cap, trained the sizing; the V07 ruin's reach needed a gap and an account whose excess fell on her; the V08 ruin, in the reward's own regime, ended at 0円.
- The four convergences of section 3 and the agreements AG-01 to AG-16.
- Every item facing events after V10 named as NOT SCOREABLE IN THIS RUN and left alone; the forecast record used only as a process record in the limitations.

### 8.7 Readiness

Every proposed row is written or merged with its reason; every convergence disagreement is listed with its state; the state of every QUALIFIED_PENDING monograph is recorded. The full-series-synthesis readiness boundary of initiation §5.13 item 4 is recorded by this audit, and the integrated synthesis may begin. It begins with the character layer incomplete.

## 9. Transaction record

### 9.1 Files written

| File | Bytes | sha256 | Notes |
| --- | --- | --- | --- |
| [Study A](../studies/FX_KURUMI_SCREENS_INSTITUTIONS_AND_RESPONSIBILITY.md) | 99,679 | 9ebf4641ddb3581aa1513cb1192d1fc746b75ae81227fc739d0e0d5602733257 | Published from the 92,923-byte frozen text with the corrections of section 7.1 |
| [Study B](../studies/FX_KURUMI_OBLIGATIONS_RELATIONSHIPS_AND_COST.md) | 115,001 | fe0516396c15e1c52bfce1ad29be737163c230380e2daa541c48b61160e6dd42 | Published from the 113,031-byte frozen text with the corrections of section 7.2 |
| [Study C](../studies/FX_KURUMI_RISK_LOSS_AND_FINANCIAL_SELF_DESTRUCTION.md) | 102,101 | 2a7a1784a500682a117ea0c701fbaedb2265e9ce6c4c80a8b1eeb7f1279463ca | Published from the 98,311-byte frozen text with the corrections of section 7.3 |
| [Ledger](../FX_KURUMI_DECISION_AND_EVIDENCE_LEDGER.md) | 889,110 | — | Rows FXK-SYN-C007–C028; version 1.14 (section 8.4) |
| This audit | — | — | New |

All written files are UTF-8 without BOM, with LF line endings; each relative link was checked against the files that exist.

### 9.2 Pages re-opened for this audit

Eight reading copies, no crops (budget 45):

| Page | Why | Finding |
| --- | --- | --- |
| V07 i0118 | K-03: does the debt box label the regime? | 「くるみ FX口座残高 -1億153万4644円 (-1億2028万4479円) 強制ロスカット」, no regime label; "マイナス 1億2千万円!!!" above |
| V06 i0013 | K-03: the V06 label on Kurumi's account | 「くるみ FX口座残高(国内口座) 19,470,915円 (-1,743,000円損切り)」; 18:27, 12月5日 |
| V10 i0076 | K-05, K-22: a printed threshold | 「強制ロスカットのお知らせ」, 「証拠金維持率が100%…」, 「自動ロスカットが執…」 |
| V10 i0105 | K-06: what the unit rule refused | "カリフラワー 100株"; 「エラー 売買単位が誤っております。」; 株数 100 against 「売買単位:1000株」 |
| V06 i0080 | K-08: journal page or caption | Two first-person sentences in white type on black bands above and below Kozue's face |
| V07 i0060 | K-12: when the overseas account was funded | "さっき海外口座に入れた10万円で勝負!" (7 January) |
| V06 i0052 | K-18: the order of Mochiko's close | Close typed and boxed (「萌智子 FX口座残高(国内口座) 20,993,630円 (+7,691,000円利益確定)」) after her reply, then a second message dated 12月8日 |
| V05 i0155 | K-07, P-01: the V05 resolution | "目標達成したら ちゃんと FX引退しなきゃ!" — conditional on the target |

### 9.3 Records consulted

Role-gap audit §2–§10 (in particular §3.1–3.5, §5.2–5.5, §7); reconciliation audit §1.5–1.6, §4.1–4.3, §4.6, §5.5, §8.5; ledger rows FXK-SYN-C001–C006, the claim rows each study names as a last explicit transition (FXK-V02-C002 L444; FXK-V03-C001 L591; FXK-V03-C002 L592; FXK-V03-C012 L602; FXK-V04-C001 L750; FXK-V04-C002 L751; FXK-V04-C015 L764; FXK-V04-C028 L777; FXK-V05-C034 L993; FXK-V05-C049 L1008; FXK-V07-C001 L1406; FXK-V07-C023 L1428; FXK-V08-C041 L1694; FXK-V09-C065 L2004; FXK-V10-C014 L2208; FXK-V10-C065 L2259, base line numbers) and the qualification table; the V02 reading (§D, E010, §L.1), the V05 reading (§G, E055–E057), the V06 reading (E015–E017, E041, §D, §L), the V08 reading (E037) by search; the three frozen studies, their transfer records and the reviewer's challenge record in full.

## 10. Name-and-reference check (handoff contract §15.6)

- **Scope.** The introduction; sections 2, 4, 5 and 6; the ledger rows FXK-SYN-C007–C028, where several persons handle the same money and speech must be attributed.
- **KNOWLEDGE_BOUNDARY_REQUIRED, kept.** Kozue is named for her 2008 acts, which V06 shows and names (V06 i0065); the father is "the father" or "her father", and his inferred given name appears only in the qualification table's established form (section 8.3), never as a reference form; あふぃちゃん is not used for any act here; Yasuko's 2013 is marked as a V10 flashback; Nana is the reference form.
- **JUSTIFIED_ROLE_REFERENCE.** Principal integrator, reviewer, specialists, coordinator and owner name process roles; "the narrator" names a presentation channel; "the broker" and "the creditor" name institutions; "the lender" is not used for Mochiko without her name.
- **Attribution.** Mochiko's 「国内口座の仕様」 is her unspoken thought (V08 i0106); the V06 i0080 sentences are a first-person caption in a chapter of mixed authority; the V05 resolution is Kurumi's own (SELF_REPORT); Kurumi's V02 reasons for the domestic account are her caption and speech (V02 i0017); "この区間 取引成立せず" is the narrator's (V07 i0114); the creditor's logic of V08 i0119 is Mochiko's.
- **Result.** No AMBIGUOUS_REFERENT, UNNECESSARY_GENERICIZATION or INCORRECT_IDENTITY_OR_ATTRIBUTION found in the scope. The writer and the artist are not referred to.

## 11. Limits

- The principal re-opened eight pages and otherwise relied on the accepted readings, the reconciliation audit and the pages the studies and the reviewer re-opened; it sampled the load-bearing locators where the studies meet or conflict and did not re-verify every locator in the three studies.
- Base drift was classified on the content of the records the studies use (section 1.3), not by repository history.
- The state of the monograph chains is recorded as the run's dispatch reported it; their working records were not opened.
- The conditional calculation of section 4.3 (3) assumes a loss linear in lot count at the same unprinted fill; it shows that the 84.4% is not a causal share and does not reconstruct the V07 fill.
- Nothing here resolves an obligation the record keeps OPEN (U-06, V07-U01, V08's fills, V09-U14, FXK-V01-C005, FXK-V09-C008, FXK-V09-C032), and nothing faces an event after V10. No paratext was used. No external reference arose beyond what the studies already exclude.
