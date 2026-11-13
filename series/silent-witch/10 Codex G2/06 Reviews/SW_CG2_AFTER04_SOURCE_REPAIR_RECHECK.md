---
generation: SW-G2-CODEX-20261019
artifact_id: SW-CG2-20261019-AFTER04-SOURCE-REPAIR-RECHECK01-20261020
artifact_type: semantic_review
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
---

# AFTER04 focused Japanese-source repair recheck

**Disposition: grant bounded AFTER04 transaction acceptance at the exact repaired hashes below. M01 and m01–m03 are resolved; no residual or new Critical, Major or Minor defect was identified in this assigned scope.** This completes the focused repair recheck, not final corpus acceptance, persistence, freeze or authority promotion.

## Commission, independence and exact scope

Separate original-Japanese reviewer; completed 2026-10-20. Read all five approved files under `urn:sw-g2:norm/`: RUN_INSTRUCTIONS.md, NORMATIVE_ANALYTICAL_METHOD_DRAFT.md, NORMATIVE_SYNTHESIS_ARCHITECTURE_DRAFT.md, NORMATIVE_RECONSTRUCTION_READINESS_DRAFT.md and NORMATIVE_VOLUME_TEMPLATE_DRAFT.md. The owner's simplified/two-role instruction governs obsolete choreography. No subordinate agent, additional role/framework, external source, producer conversation, repository/history access, Git, web, translation, adaptation, reception or future narrative was used. Model familiarity remains unknown. Candidate and source were read-only.

Read the complete initial independent report, then independently established the affected Japanese sequences before opening repaired analysis, producer repair descriptions or supplied repair inputs. Subsequently read the **entire repaired AFTER04 reading, both entire cumulative ledgers, entire run state, entire FULL_REPAIR.diff and entire REPAIR_CONTEXT.txt**. Truncated combined outputs were reissued; lost Japanese display was recovered by reversible non-ASCII JSON transport. Source inspection used original XHTML with ruby and typographic markup retained, without normalization or OCR.

Candidate root, absolute: `repository/series/silent-witch/10 Codex G2/`. “Reading,” “Master,” “Claims” and “State” below mean the following exact files; Markdown line numbers are one-based at these hashes.

| File beneath candidate root | Bytes | Repaired SHA-256 |
|---|---:|---|
| 01 Sequential Readings/SW_CG2_AFTER04_DEEP_READING.md | 84025 | `b32db8a4d3038d1a3ed1b18a1e491cf83f5a2919ad1367cc4878b6f5def778c6` |
| 02 Cumulative/SW_CG2_MASTER_LEDGER.md | 202949 | `fa7d481420cdf338f8816faf5d80cbc8b66af8b392ad360c2f1bc96bed3fae15` |
| 02 Cumulative/SW_CG2_CLAIMS_AND_REVISIONS.md | 150433 | `293c6a0f7c5091ab43667a81ebad566d902e4ff619d548f679a5bc60f0d140e7` |
| 00_RUN_STATE.md | 51873 | `3cd6304f10676e7f28d94ed3760c2ce95b07bd43f44ac12febd496fc8fa2a878` |

Independent file hashing matches REPAIR_CONTEXT. Exact input scope:

- `urn:sw-g2:review/AFTER04-RECHECK01/input/FULL_REPAIR.diff`: 91688 bytes; SHA-256 `8579d0c77dfb92aaee0af1b6cc8ce0b3327132c797299ef9c3edba9b41246e4a`.
- `urn:sw-g2:review/AFTER04-RECHECK01/input/REPAIR_CONTEXT.txt`: 1099 bytes; SHA-256 `5b28ed7da1e773275d12a39aefeac1af439fb13b290384cb2a1df4237f4bbdd2`.
- `repository/series/silent-witch/10 Codex G2/06 Reviews/SW_CG2_AFTER04_SEMANTIC_REVIEW.md`: 23591 bytes; SHA-256 `25e31a198f483ee8b816250f936321dd0364475ddd1e6bee9a18336ef00d8167`; preserved initial review, not overwritten.

FULL_REPAIR.diff changes precisely these four analytical files from the initially reviewed staged new-G2 candidate. Every hunk's resulting text matched the repaired file. Reversing those hunks in memory reproduced the initial report's four exact hashes:

| Initial file | Reconstructed initial SHA-256 |
|---|---|
| Reading | `c3d03afb475f5c3b188050a45d14d4315cbe0b8e6adf2c3ace2ca3055971868e` |
| Master | `9d75444b88f0d4435a313a9d03ebc983f4b9e394be6b535b1cb523eec3de2fcd` |
| Claims | `602cc0141070b0fd6e9bc0790560e116a00d65d9032da83f1673c608110fa7e7` |
| State | `fef6546508c1e47aefbb3ae127e45412e48e3a0f46408fb51ce5295333064506` |

Thus this is the actual repair delta, not a historical-analysis comparison. The context's preceding accepted identity `d1a29fb34ca7c58b846a432d41e9bcd34451e926` is supplied attribution only; no Git history/index was accessed.

## Actual original-source inspection

Witness **SW-LNJP-AFTER04**, *サイレント・ウィッチ Ⅳ -after- 沈黙の魔女の事件簿*. Independently rehashed `urn:sw-g2:source/SW-LNJP-AFTER04/SW-LNJP-AFTER04.epub`: 23490806 bytes, SHA-256 **101a1341d139a593c284010da5fb83f524183528ff4199d563346cb3254fc24a**, matching the initial review and current-unit technical metadata. All six XHTML members actually used below independently match their package-manifest hashes.

Original XHTML root, absolute: `urn:sw-g2:source/SW-LNJP-AFTER04/primary/item/xhtml/`. **P counts every original XHTML p element in document order, including headings, empty/separator and image paragraphs.** The element counts equal the candidate's paragraph-line counts for these members; ruby remains within its parent paragraph. These are recoverable original locators, not printed pages.

| Original member | Actual ranges read in this recheck / purpose |
|---|---|
| p-009.xhtml, Case II | P120–170 and P640–783: kitchen appraisal/oath versus complete defensive/trust sequence, capture knowledge, interruption, closing appraisal and next-day reciprocity. |
| p-016.xhtml, 華麗なる悪役ファミリー会議 | P1–51, complete: attack interval, forthcoming assignment, Louis's instruction and family's elaboration. |
| p-020.xhtml, secret episode | P1–38, complete: requested labor, assent, interrupted calculation, actual card receipt and intended shopping. |
| p-015.xhtml, Case IV | P640–690: declined invitation, specified private tearoom, cake distribution and remembered care. |
| p-018.xhtml, epilogue | P125–157: incomplete custom knowledge, gratitude, praise demand, writing and stamp. |
| p-012.xhtml, Case III | P399–490 and P730–775: continued class doctrine, injury/history attribution, protective withholding and final tragedy rule. |

Dependency expansion also read **SW-LNJP-V04**, `urn:sw-g2:source/SW-LNJP-V04/primary/OEBPS/Text/p-010.xhtml` **P1–121**. Its EPUB independently matches `a80f90953d625d304ae724a9b05a8c93ad3392e8bfd23e9edaeb6d0f9642fcfc`; the inspected member hashes to `3085ac51802d78623325864ab493a0c3e430b72619b313e9b87605039d116335`. This tests the affirmative earlier qualification retained by C011, not a renewed V04 reading.

Actually viewed original images at `urn:sw-g2:source/SW-LNJP-AFTER04/primary/item/image/p145.jpg` and `urn:sw-g2:source/SW-LNJP-AFTER04/primary/item/image/p265.jpg`: respectively the rabbit biting distressed Monica with Cyril watching, and Monica holding the pouch beside tea/cake. Neither establishes Cyril's private deliberation or a domestic address; prose supplies those distinctions. No other image, reference leaf or afterword was newly inspected.

## Finding resolutions and dependency checks

**M01 — original Major, resolved.** P676–680 supplies injured shame and inability to pursue. Elliott's P681 taunt groups the former commoner with the apparently commoner juniors. P683 expressly prioritizes Cyril's anger for them; his P684 reply is 「私の後輩を侮辱するのは、やめてもらおうか」. P697 publicly affirms both, but P698 retains uncertainty and the self-directed ground 「それでも先輩の自分が信じなくてどうする」. P703 admits Glen's actual conduct problems; P706 immediately answers the trust question 「私の後輩ですから」. The Minerva remark and returning juniors follow. Cyril's choice therefore cannot be explained by knowledge of their already narrated success.

Reading **E010, lines140–144**, now preserves circumstance → self/other appraisal → defensive speech → private doubt → deliberate trust in substantive connected prose. **E009 line136/P144–153** keeps the different evidence-based poor-lying judgment. **E012 line152**, synopsis line222 and whole-volume argument line226 recover the reciprocal direction and contextualize MacLagan's concluding pleasure. The latter is a supported relational reading, not disclosure of Glen's unspoken history.

Forward routes are substantive: Master **S-CYRIL/S-GLEN/S-ELLIOTT lines661–664; R005 line682, R008 line684, R030–031 lines687–688; L046–048 lines736–738**. Search by Cyril, Glen, Monica/juniors, Elliott or class reaches the precise E010/P676–709 mechanism. The juniors' absence is retained; their knowledge of this defense is not invented. Neither Cyril's universal egalitarianism nor Elliott's apology, certainty, harmless severity or completed Minerva biography is inferred.

Claims **CR-AFTER04-REPAIR01 lines633–649**, especially rows641–643, genuinely reviews **C004/C011/Q009**. Keeping C004's RV022 formulation and V01–V04 registered support is warranted: this local recovery adds specific evidence without contradicting its conditional care/intimidation account. C011 keeps RV029 and its existing V02–V04 + AFTER04 support set, including E014–015/E018; E010 remains an explicitly routed local comparison. Original V04 P117–118 affirms that Elliott cannot reject every boundary-crosser, while AFTER04 P469–470 and P773–775 retain his general rule. The new insult/defense supplies enacted counterpressure without cancelling that earlier qualification. No invented claim/RV event or silent support advance is needed.

Master **Q009's current pointer line758 and dated supplement line793** now register an actual trust-under-rank-pressure opportunity during Cyril's own failure. They preserve the original question and avoid a global survival verdict. C008/C010 comparisons remain bounded; no new general theory is smuggled through the routes.

**m01 — original Minor, resolved.** P16 measures two months since Worgan's black dragon and subordinate winged dragons attacked: 「襲撃から二ヶ月が過ぎた」. P31–36 still anticipates the autumn assignment. Reading **E023 line196** and Master **K040 line706** correct the interval's referent while preserving the pre-assignment placement. The family's role-making remains distinct from Louis's brief instruction. C019's role-origin comparison/support remains valid; no retrospective prediction is created.

**m02 — original Minor, resolved.** P14 demands cleanup/replacement; P15 accepts. P17 begins calculation, interrupted by the card. P30–38 actually narrates rereading, renewed demands, intended board/frame shopping and opening the door. Reading **E025 lines206–208** now preserves these states without completing cleanup or either purchase. Master **S-HILDA/S-MATILDA line672, W035 line715 and L052 line742** agree; **R038 line695** already distinguishes actual receipt from plans. Domestic care still carries practical obligation, with no fictitious performed labor. C012/RV030 requires no formulation/support change.

**m03 — both original Minor precisions resolved.** P664 specifies 「ラナに指定されたティールームは、大部屋ではなく個室だった」. Reading **E022 line190**, Master **S-LANA line668/L051 line741** now give that setting while preserving the family's cake custom. In p-018, P145–146 precedes P147–154: gratitude/praise demand → card-writing → unsolicited stamp. **E025 line206/L052 line742** now retain the order and Monica's eventual acceptance. C003/C012's reciprocity/gift arguments survive; neither incidental correction requires a claim revision.

## Preservation, qualifications and disposition limits

Inspected every substantive changed passage and its cross-file routes, not only the repair receipts. Changes beyond the four findings are their synopsis/argument integration, bounded qualifications, navigation, status updates and dated supplements. No collateral distortion or new unsupported generality was found. Material retained elsewhere in unchanged E009–012 and the supporting routes remains recoverable.

The diff and exact reconstructed hashes confirm unchanged **PRE_AFTER04**, original **POST_AFTER04**, all preceding Master layers apart from its current banner, and the entire original Claims body apart from its current banner. All C001–019 origins/current formulations, support boundaries, rivals and RV001–031 history remain. The dated V03 supplement stays historical. Reading **AFTER04-REPAIR01 line270** and **POST_AFTER04-REPAIR01 line285** explicitly add post-disclosure knowledge; Master line787 and Claims line633 date the corresponding dispositions. State **lines19–21, 193–214** distinguishes producer completion from pending independent acceptance/persistence. Original review withholding remains recoverable. The required noncurrent front matter persists.

The producer certifies full-volume reading, all-image coverage, historical preparation times and final personal readbacks. Those are **producer attestations**. My actual work is complete reading of the assigned analytical candidate and repair inputs, selective original reinspection listed above, exact hash/diff preservation checks and two viewed images. The initial independent report supplies its own larger source-first sample/full-initial-candidate/full-original-diff review and honest limits; I neither replace that completed work nor claim to have repeated it. RV031's previously accepted age correction and unrelated earlier work were unchanged and were not rerun. Historical activity/timing and every source passage are not independently certified by this recheck.

**Bounded disposition: accept this repaired AFTER04 transaction; no further substantive repair is required in the inspected scope.** M01's material loss and its dependencies are resolved, and m01–m03 are corrected in original context. No material source-access, integrity, independence or authority blocker was encountered. Remaining literary unknowns, including Glen's interrupted history and Elliott's withheld history, remain unknown. Whole-volume fresh coverage, exhaustive retention, later works/products, final corpus acceptance/freeze and authority remain separate.

AFTER04-RECHECK01_REVIEW_COMPLETE
