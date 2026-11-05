---
generation: SW-G2-CODEX-20261019
artifact_id: SW-CG2-20261019-V06-SOURCE-REPAIR-RECHECK01-20261020
artifact_type: semantic_review
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
---

# V06 source repair recheck

**Disposition: bounded acceptance of the exact repaired V06 transaction below. M01, m01 and m02 resolve; no residual or new Critical, Major or Minor defect was found in this scope.**

Reviewer: the separately assigned Codex Japanese-source reviewer, independent of the principal author. Model familiarity remains unknown. The five approved normative files were read completely; the owner's simplified two-role directions govern. The [initial independent review's scope][initial-scope] and [sampling limits][initial-limits] remain part of this assessment. That report is preserved, not superseded. This recheck addresses its repair/dependencies, without claiming a fresh complete Japanese V06 rereading.

I established the abuse/breakdown scene, bat message and actual p328 reference image before opening the producer repair descriptions or repaired analytical files. I then read the complete repaired Reading (304 lines), complete current Master V06 layer (959–1129), both current changed banners, Run's V06/repair context (257–283), and every line of the supplied 114-line full repair diff and context. Claims 767–833 and affected earlier Master routes were inspected directly. Unchanged historical ledger bodies already covered by the initial full review were not rerun in full.

## Exact transaction

The four candidate SHA-256 values were independently calculated and match REPAIR_CONTEXT; both input hashes were independently calculated as well. Links below are absolute.

| Candidate / input | Bytes | SHA-256 |
|---|---:|---|
| [Reading][reading] | 88,599 | `f7797d17a525222706b060673fb44512334585591ad64620e7d3b0e7d650a655` |
| [Master][master] | 277,752 | `6d62296db529bd693a23218b39cdf9c6b21e196f8869c0e2c7ad80e7cb0003d8` |
| [Claims/history][claims] | 205,680 | `344c75303d9e25b48dc88228d5597d1410164e925d5ae96904218756661191fc` |
| [Run state][run] | 68,046 | `646d80dfe8f86a3f85ac9043dca3731a3135959436c212adfaa6ecc5a38b0497` |
| [FULL_REPAIR.diff][diff] | 30,103 | `99d28587a97bb6ed7eaf8ddc913d94a6f49c779f3c70177109d8c6dcf063b2ee` |
| [REPAIR_CONTEXT.txt][context] | 1,429 | `ea3068577ca4ba8e765cd2166309b80681298702c9a507118d45866da2db8b83` |

The preserved [initial report][initial] hashes to `1dc45c4f3711f8e91a3d1ce6c138a18ab3cb5c139324b07893e7c722bae3f3a1`. Claims/history exactly matches its initial candidate hash: no claim wording, support set/boundary, confidence or revision-history change occurred. The full diff changes only Reading, Master and Run: the synopsis; E029; E031; current S-BENJAMIN group/R048/K061 rows; two status banners; and separately dated repair records. Formatting preparation is disclosed in the context. No unexpected substantive change appears in the supplied complete delta. Preservation of the initial indexed candidate is supplied context, not an independently inspected Git fact.

## Original Japanese actually checked

Witness **SW-LNJP-V06**. Independently hashed original EPUB: `7909cd94b71063033b96b49ec1f7c6b686f49edb637a43b187e500ebad3a7242`, matching the initial review and package manifest. Original member hashes also match that manifest. Paragraphs count every original XHTML `<p>` one-based, including headings, blanks, separators and images. Inline ruby bases/readings, emphasis spans, punctuation and typography were inspected through reversible non-ASCII JSON escapes after the console's Japanese display proved lossy; no normalization or replacement-source paraphrase supplied evidence.

| Original member / chapter | Actual inspection and purpose |
|---|---|
| [p-007.xhtml][p007], 四章　因縁の編入生達, `toc-007` | P1–143: complete past scene P36–114, especially P94–114/P102–110, plus present awakening/pain concealment. Distinguishes surviving reserves, panic, anger and unconsciousness from exhaustion; separates nightmare from current curse aftereffects. |
| [p-008.xhtml][p008], 五章　第三王子アルバートの、お友達大作戦, `toc-008` | Heading and P4–116: additional C022 dependency check of practical instruction, admitted haste, foundational learning and Monica's motives. |
| [p-014.xhtml][p014], 九章　真夜中の訪問者の物騒なお誘い, `toc-012` | Heading and P314–333: additional C005 dependency check of Will's report, Felix's approval and qualified private interpretation. |
| [p-016.xhtml][p016], 十一章　通りすがりの男達, `toc-014` | Heading, P100–124 and P180–273: concealed uniform-guided assistance, actual plant shielding, meeting/cover story, bat report at P258–259, Ray's operational expectation and Felix's subsequent appraisal. P125–179 were not reread. |
| [Original p328.jpg][p328] | Direct original-size visual/text inspection, especially lower-left Benjamin and lower-right Glen entries. This reference channel confirms completed composition/secondhand stimulus/Elliott's response and separately confirms Glen's expulsion. No other image or earlier-unit primary text was newly inspected. |

Inspected-member SHA-256 values:

| Member | SHA-256 |
|---|---|
| p-007.xhtml | `4803f6f104bbe40d6161993d28ba63c776ef68c28027dfc2139dca69234c5b2c` |
| p-008.xhtml | `0ab924a9218f4a3eacfe662a28778ab605c911a00b601b2a44a9edb8175563ee` |
| p-014.xhtml | `0be0bcfd352c809e726fd78cce77ad554e644e72155be5ea7a6bc5e9b6fe1bec` |
| p-016.xhtml | `f3210a93c4de6c04b48025e09b8ce48d7e51f2328c0ddef8f3ad9a1ef4ba71a0` |
| p328.jpg | `8f7c4117e9d289a0a9578019b99365e77bd95ced1c3c52bde8b1f7f47dda5245` |

## Findings and dependencies

**M01 — Major, resolved.** Reading line 90 now gives the source's causal order. The barrier prevents magical bodily injury but leaves pain and consumes reserves with damage. Glen wishes for depletion (P102); narration says 「簡単には魔力が尽きなかった」 (P103), and Hubard explicitly remarks on abundant remaining power (P106). Glen concentrates power in mixed fear/anger, puts all he has into an incoherent formula, and loses consciousness without knowing the fireball's consequences (P108–114). The repaired synopsis preserves these distinctions and retains the independently reference-supported expulsion. It does not substitute clinical trauma, innate violence or a complete incident aftermath for the narrated event.

Forward/backward routes remain coherent: **Reading E012/E015 → Master S-GLEN/R046/K054/W043/T030/L070 → Claims C022**, with R030/R039/R045 and Q024/Q035 retaining present learning/relationship limits. E012 (132–134), the named Master records (971/1006/1022/1036/1055/1067), and C022 (815–817) were already correct and remain so. Present pain is explicitly curse aftereffect; the remembered humiliation does not explain every cheerful act. The p-008 teaching scene preserves chosen growth alongside fear and guilt. Earlier V05 S-GLEN/R039/K042–043/W036/L056/L058/Q024 and the dated repair route (Master 811/848/860–861/874/896/898/936/957), plus AFTER04 S-GLEN/R030/K040/L046–047/Q024, retain distinct training/trust, attributed report/appraisal and interrupted-statement boundaries. V06's abuse scene and reference-confirmed expulsion are not backdated into them. A broad claim revision or rewritten freeze would be unwarranted.

**m01 — Minor, resolved.** Reading E029 line 214 and Master R048 line 1007 now describe one secretly dispatched familiar bat carrying 「行方不明者を保護」, a protection report (p-016:P258–259). Actual shielding is supplied by Raul's plants (P194–204); no bat shielding/rescue is invented. Ray's participation and reporting remain real. **E029 → R048**, and **S-FELIX/R006/R011/R047/K058/L074 → C005/RV040** retain independently narrated Will discretion and Felix's concealed assistance, checked against p-014:P314–333 and p-016:P100–124/P268–273. C005's registered support and the collective-help argument require no change; correcting the bat's action removes no causal basis for them.

**m02 — Minor, resolved.** Reading E031 line 232, Master S-BENJAMIN group row 984 and K061 line 1029 now preserve secondhand duel knowledge and completed composition. The original Benjamin entry says 「曲を作った」 after describing his excitement about men dueling over a woman; Elliott then holds his head in dismay. That response does not establish an audition or Monica's reception. **S-BENJAMIN/K061/L077 → E031 → p328.jpg** remains recoverable; L077's “performed song” is a future reconsideration trigger, not an accomplished event. Older Benjamin art/performance routes (Master 339/451/494/526/665/689–690/738; R008/R032–033/L020/L048–049) concern other encounters and are preserved. No general claim or support revision is needed.

## Preservation and bounded acceptance

The complete repair diff leaves original PRE_V06/POST_V06, prospective questions, pre-V06 literary bodies and historical revision events intact. Reading's correction is separately dated **2026-10-20 07:51:31 UTC**; Run's completion record is separately dated **07:54:11 UTC**, following the initial report's stated completion. These are attributable correction records, not backdated improvements to PRE/POST. Their asserted producer activity chronology cannot be independently verified from snapshots and is not certified here.

Affected file/section destinations were opened and checked: Run and Master banners → Reading's dated disposition; disposition → initial review and Run repair section; Reading → Master V06 and Claims V06 review; and the observation/typed/local routes listed above → original members/image. The actual headings support the encoded fragments. No affected retrieval break or collateral semantic distortion was found. Current banners truthfully reserve acceptance to the separate reviewer; older pending statements remain historical. This report supplies bounded acceptance for the hashed repaired transaction and does not edit those banners or the candidate.

All three findings are closed **within the assigned transaction**. This decision combines the preserved initial review with the present targeted original-source/dependency checks. It does not certify every V06 paragraph/image, unrelated historical ledger bodies, producer reading chronology, Git persistence, later narrative, final corpus acceptance or freeze. No subordinate agents, additional framework/validator, producer conversation, excluded history, web/translation/adaptation/reception, Git, publication or authority promotion was used. No material source-access, integrity, independence or authority blocker remains. Candidate files and the initial report were left untouched.

Completed **2026-10-20 08:03:45 UTC**, following complete report readback and confirmation that all four candidate hashes and the initial-report hash remain as recorded above. Final wording refinements clarify hash provenance and the earlier-context distinction; they change no finding or disposition.

[reading]: ../01%20Sequential%20Readings/SW_CG2_V06_DEEP_READING.md
[master]: ../02%20Cumulative/SW_CG2_MASTER_LEDGER.md
[claims]: ../02%20Cumulative/SW_CG2_CLAIMS_AND_REVISIONS.md
[run]: ../00_RUN_STATE.md
[initial]: SW_CG2_V06_SEMANTIC_REVIEW.md
[initial-scope]: SW_CG2_V06_SEMANTIC_REVIEW.md#candidate-and-transaction-inspected
[initial-limits]: SW_CG2_V06_SEMANTIC_REVIEW.md#overall-literary-and-cumulative-judgment-limits
[diff]: <urn:sw-g2:review/V06-RECHECK01/input/FULL_REPAIR.diff>
[context]: <urn:sw-g2:review/V06-RECHECK01/input/REPAIR_CONTEXT.txt>
[p007]: <urn:sw-g2:source/SW-LNJP-V06/primary/item/xhtml/p-007.xhtml#toc-007>
[p008]: <urn:sw-g2:source/SW-LNJP-V06/primary/item/xhtml/p-008.xhtml#toc-008>
[p014]: <urn:sw-g2:source/SW-LNJP-V06/primary/item/xhtml/p-014.xhtml#toc-012>
[p016]: <urn:sw-g2:source/SW-LNJP-V06/primary/item/xhtml/p-016.xhtml#toc-014>
[p328]: <urn:sw-g2:source/SW-LNJP-V06/primary/item/image/p328.jpg>
