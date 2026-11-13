---
generation: SW-G2-CODEX-20261019
artifact_id: SW-CG2-20261019-V11-SOURCE-REPAIR-RECHECK01-INDEPENDENT
artifact_type: semantic_review
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
---

# V11 source-repair recheck

**Bounded acceptance granted for the exact repaired V11 transaction below. Major M01, Minor m01 and the nonblocking navigation finding are resolved. No residual or new Critical, Major or Minor issue was identified within this recheck.**

Separate original-Japanese reviewer, 2026-10-20; no subordinate agents or producer conversation. Model familiarity remains unknown. All five approved norms were read, with the owner's simplified two-role directions governing. The complete [initial review](SW_CG2_V11_SEMANTIC_REVIEW.md) supplies the [initial scope record](SW_CG2_V11_SEMANTIC_REVIEW.md#exact-candidate-and-dependency-scope) and [limits](SW_CG2_V11_SEMANTIC_REVIEW.md#disposition-and-limits); those limits remain. This report completes the focused repair/dependency assignment, without reopening unrelated sound argument.

## Exact state and actual inspection

The independently established Japanese conclusions were fixed at **16:18:40 UTC**, after the norms and initial review and before opening the repaired reading, repair diff or repair context. I subsequently read the **entire 296-line repaired V11 reading**, **complete current master V11 layer (2005–2192)**, **complete claims V11 layer and correction (1305–1423)**, both ledger headers, current run-state headers and V11 entry/completion/repair dispositions, and every changed passage in full relevant context.

I read **all 224 lines** of FULL_REPAIR.diff (`urn:sw-g2:review/V11-RECHECK01/input/FULL_REPAIR.diff`) and **all 54 lines** of REPAIR_CONTEXT.txt (`urn:sw-g2:review/V11-RECHECK01/input/REPAIR_CONTEXT.txt`). Its four starting-file identities agree with the initial review's hash index. The complete supplied delta covers the four actual changed files; its changes agree with their current contents. No unexpected literary alteration appears. Run-state format normalization is separately declared in the context. Independent SHA-256 checks, repeated at **16:23:35 UTC**, were stable:

| Exact file | SHA-256 |
|---|---|
| [V11 reading (D)](../01%20Sequential%20Readings/SW_CG2_V11_DEEP_READING.md) | `cb1549a802dee1cb3f227620f16176a7dc237e3e09d06e62faba5f9b238db296` |
| [Master (M)](../02%20Cumulative/SW_CG2_MASTER_LEDGER.md) | `a2752e1642ce6033c393ee783c8f251ceaf94b34ee10b450cdb42af0305ea1cd` |
| [Claims/revisions (C)](../02%20Cumulative/SW_CG2_CLAIMS_AND_REVISIONS.md) | `3a0eac4ef019b3ac495237abe990477b4a735c364fea29c42da20235d3ba8a69` |
| [Run state](../00_RUN_STATE.md) | `353e048b468c9e9ac76c7624c25d3a6d71177f8e982c20a3bc90184bea604db4` |
| Full repair diff (`urn:sw-g2:review/V11-RECHECK01/input/FULL_REPAIR.diff`) — 73,089 bytes | `ba1cf1266f7079eaac6f119d84f4138f2edb99f1aaadfc0a1943c158a4912cb8` |
| Repair context (`urn:sw-g2:review/V11-RECHECK01/input/REPAIR_CONTEXT.txt`) — 2,138 bytes | `50db13c77e34f7add589bc05e32bbc2610607481b16186af8251da8b725a32a8` |
| [Preserved initial review](SW_CG2_V11_SEMANTIC_REVIEW.md) | `34874426f5553df1f80e4ce4292e2b5a8b09c2f443088098fb50bf209eb08a92` |

Earlier dependency recovery covered the complete operative formulations/classes/support/rivals for C001/RV009, C003/RV065, C004/RV066, C005/RV067, C009/RV068, C010/RV037, C012/RV056, C025/RV058 and C028's V10 origin, plus C005/RV054/RV063. Relevant earlier reading passages were [V10](../01%20Sequential%20Readings/SW_CG2_V10_DEEP_READING.md) E005/E018/E020/E023–024 and [EXTRA09](../01%20Sequential%20Readings/SW_CG2_EXTRA09_DEEP_READING.md) E007/E019/E026. These preserve honored incapacity, preexisting scholarly pleasure, particular attachment and the dependency rival. Unchanged unrelated history required no second whole-file reread.

## Original Japanese and evidence boundary

Witness **SW-LNJP-V11**. I independently hashed the EPUB (`urn:sw-g2:source/SW-LNJP-V11/SW-LNJP-V11.epub`): **18,283,771 bytes**, SHA-256 `cb81975b7967cf61f050a7fea53b39b13d627eb70af56e26af025e85c4207a4a`. V11 volume-config and package-manifest identities agree. Actual original-XHTML inspection was:

| Original member / chapter | Complete inspected range | Independently checked member SHA-256 |
|---|---|---|
| p-007.xhtml (`urn:sw-g2:source/SW-LNJP-V11/primary/item/xhtml/p-007.xhtml`), 四章 魔女の秘薬と紳士協定 | **P1–188**, including complete **P52–168**, before repair descriptions | `00e59d51e8e402ab7888a8474fbc68d8541d9fad7a46a55199e7c1e14fdf1e0a` |
| p-006.xhtml (`urn:sw-g2:source/SW-LNJP-V11/primary/item/xhtml/p-006.xhtml`), 三章 戦え、ホワイトハリケーン一号 | **P134–262**, including complete **P168–212**; P134–231 before repair descriptions | `dd5009fb8e9c84082b533b9cf1d67cadce3833508f7c5f1e028f5004269e0527` |
| p-015.xhtml (`urn:sw-g2:source/SW-LNJP-V11/primary/item/xhtml/p-015.xhtml`), 十二章 本気のお忍び | **P147–279**, collateral C005/C028/teacher-intervention check | `908a8a2dcc2e4768b7da5c28746ff9ca6d9aa1b6cfd1779c729679b3dd5540c8` |

P retains the one-based original paragraph contract, counting headings, blanks, separators and image paragraphs. Ruby bases/readings, emphasis, punctuation and layout markup remained visible through reversible Unicode transport; no normalization or source editing occurred. The source quotations and paragraph references in the repair agree with the original.

Actually viewed original images: p061.jpg (`urn:sw-g2:source/SW-LNJP-V11/primary/item/image/p061.jpg`) and p089.jpg (`urn:sw-g2:source/SW-LNJP-V11/primary/item/image/p089.jpg`). The first shows Monica's distressed entanglement; the second shows the dirty, sleeping cart passengers. They support bodily vulnerability and aftermath, while the prose establishes the rescue sequence and agency. No other image or earlier original-Japanese witness was reopened in this focused recheck; no additional material source dependency remained.

## Finding-by-finding resolution

**M01 — resolved through the operative argument and collateral routes.** P52–60 gives Isaac's recognition of the royal rose warning and Will's silent alert. P71–79 explicitly makes lifting the cup an act of evidence preservation and identification. P92–110 then gives permission to remove it, continued alliance and blackmail. The next scene identifies the confiscated bottle (P114–115). At P120 Isaac expressly says he cannot resist magical medicine and is glad he noticed **before drinking**. Ordinary poison tolerance is his stated capacity; it is neither a demonstrated trial here nor immunity to this preparation. Will's potency and dose-risk warnings are separately attributed (P117/P121).

D E008 now preserves that sequence, and M's S-FELIX/S-WILL, Baldia subject description, R064/R085, **R102**, K115, W087 and **L147** carry it accurately. **C005/RV076** corrects both the operative formulation and evidence classes: actions and the spoken refusal are observable textual events; Isaac's capacity/research statements and Will's technical assessments are attributed reports. No operative ingested-drug victory survives in the affected transaction.

The surviving ethical argument is warranted. P155–168 distinguishes research interest from use on another, and a spoken refusal from proven future conduct. Isaac's enjoyment rationale is supplemented by narration about being able to face Ark and Monica; Will's means/end objection and Isaac's inability to dismiss it resist a general redemption claim. Actual blackmail remains alongside this limited restraint. P147–279 of p-015 independently confirms continued criticism-management and a genuinely received scholarly exchange. C005 therefore retains its strongest dependency/approval rival without making either all care fraudulent or all coercion cured.

**Historical correction and dependencies — resolved.** The dated warning immediately above C's original RV073 paragraphs explicitly labels their completed-drugging/observable-resistance wording as historical error, despite the literally retained old “current” label. Their complete wording, class, support, rivals and original event remain recoverable. The append-only **CR-V11-REPAIR01 / RV076** quotes the error, identifies its producer ownership and gives the decisive P120 source reason. RV067 and earlier history remain unchanged in the full delta. C005 keeps the same registered witnesses/ranges, including p-007:P4–188; AFTER04 remains local only.

**C028/RV075** remains sound: its ethical question and agreed external complaint route do not depend on Isaac ingesting anything. Its exact V10 origin and V11 support remain intact. The recovered P52–79 practical warning is locally routed rather than silently added to C028's registered support. C003 and the other affected no-event claims retain their formulations and boundaries. **Only corrective RV076 is added**; no unrelated revision is manufactured.

**Minor m01 — resolved without disturbing C004/RV072 or L146.** P187 freezes only the vine surface around Monica. P188–196 specifies an unfamiliar hoe, work above Cyril's height, arm/waist fatigue, Raul's dominant-hand advice, sweaty grip and danger of injuring her. Raul restrains the pea; Cyril chips, tears the remaining vines, frees/catches Monica and carries her clear. Raul's later uprooting causes the soil disturbance (P206–212). D E007 now preserves these distinctions. S-CYRIL/R005/R048, **C004/RV072** and **L146** already express precise assisted labor and received help, with no false ground target. Their unchanged scope remains appropriate. The cart/wreath sequel and p089 support the retained reception/undelivered-gift distinctions.

**Current pointers and freezes — resolved.** Both ledger headers now identify V11-REPAIR01 and route to operative C005/RV076; older V10 notices remain literal history. Run state truthfully records repaired-producer-complete/source-recheck-pending rather than self-acceptance. The current endpoint is **C031/RV076/R104/K117/W089/T070/L159/Q061**. Complete PRE_V11 and POST_V11 contain neither erroneous immunity nor the false hoe target. POST's limited refusal and original RV075 endpoint remain truthful historical records. The later dated correction suffices: no freeze erratum or source-recovered exit supplement is needed merely because RV076 follows POST_V11. No prediction or earlier support boundary is rewritten.

## Disposition and limits

The initial Major hold is lifted **for this exact repaired V11 transaction and its checked dependencies**. Remaining/new findings: **Critical 0; Major 0; Minor 0** in the assigned scope. No further literary repair is required by this recheck.

Research/use of the retained sample, the daughter's own account, costly future restraint and an exercised complaint remain unshown. This grants no certification of producer chronology, exhaustive untouched-history/source rereading, final corpus acceptance, persistence or freeze. Initial sampling limits continue through the linked report. No future narrative, prohibited history, external literary source, web, translation/adaptation/reception, Git, publication, comparison or authority promotion was used. No material source-access, integrity, independence or authority blocker prevented completion. The candidate and initial review were read-only; only this report was authored.

V11-RECHECK01_REVIEW_COMPLETE
