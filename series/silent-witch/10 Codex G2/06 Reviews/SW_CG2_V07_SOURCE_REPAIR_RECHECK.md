---
generation: SW-G2-CODEX-20261019
artifact_id: SW-CG2-20261019-SEMANTIC-REVIEW-V07-SOURCE-REPAIR-RECHECK01
artifact_type: semantic_review
status: draft_noncurrent
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
---

# V07 focused Japanese-source repair recheck

**Disposition: bounded acceptance of the exact repaired V07 candidate below. M01 and M02 are resolved through their affected dependencies; m01 and the locator correction are checked. No residual or new Critical, Major or Minor issue was found in this assigned scope.**

The [initial semantic review](SW_CG2_V07_SEMANTIC_REVIEW.md) was read in full; its source-first selection, wider review and scope/limits remain the initial record. This recheck addresses its four repairs and actual dependencies, without reopening unrelated historical bodies. All five approved normative files were read; the owner's simplified two-role directions in RUN_INSTRUCTIONS.md (`urn:sw-g2:norm/RUN_INSTRUCTIONS.md`) govern obsolete choreography. I worked as the separate Japanese-source reviewer, with unknown model familiarity, no subordinate agents or producer conversation, and no external literary sources, future narrative, old analyses, original repository/history or Git. Candidate files and the initial review were not edited.

## Exact scope and integrity

I independently read the decisive Japanese scenes before opening the initial review or producer repair descriptions. Subsequently I read the **entire repaired Reading (lines 1–324), complete Master V07 layer (1135–1264), every changed passage and context in the complete FULL_REPAIR.diff and REPAIR_CONTEXT.txt**, and the current Run source-repair disposition (13; 293–310). I inspected affected unchanged Master routes and Claims formulations, support records and revision entries, including the complete Claims V07 layer (839–906). Earlier historical bodies already covered by the initial full review were not rerun.

Independently computed SHA-256 identities match REPAIR_CONTEXT.txt:

| File | Bytes | SHA-256 |
|---|---:|---|
| [Reading](../01%20Sequential%20Readings/SW_CG2_V07_DEEP_READING.md) | 92,943 | `e7ae6c5651f430468ee5dcd5510476775610aa40953eb971795e8f4d6a3210cb` |
| [Master](../02%20Cumulative/SW_CG2_MASTER_LEDGER.md) | 306,596 | `0e17558f8dc07bc72634d5435a32dc8b9a3b5a4b15ed3e6c9e0ee6e6cc0c0125` |
| [Claims/history](../02%20Cumulative/SW_CG2_CLAIMS_AND_REVISIONS.md) | 228,081 | `7b26e5284a03f912ffd5d44880b22648d69f3453e31b5dc3c71d599c33985091` |
| [Run](../00_RUN_STATE.md) | 73,425 | `acb6d43e602a2c0c4f64234514bac1bf22067b3cbe1b0c3f33e50da04fb3c8cc` |
| [Initial review](SW_CG2_V07_SEMANTIC_REVIEW.md) | 20,748 | `f0360d2c4a8986a940b8874ffc76d4f2f7522667d76c5ec379a181cd5a892e55` |
| FULL_REPAIR.diff (`urn:sw-g2:review/V07-RECHECK01/input/FULL_REPAIR.diff`) | 30,536 | `9ab0c10423823b46d8e4a21d240b534130c5ca5a1fa9c77ec9f0b3f29ad4f78a` |
| REPAIR_CONTEXT.txt (`urn:sw-g2:review/V07-RECHECK01/input/REPAIR_CONTEXT.txt`) | 1,393 | `77607904d8a6950c02a01683fc0b2b4ed2deda56f8ba4022caf39e3e00274198` |

Claims/history is **byte-identical to the initial report's recorded hash**, not merely described as unchanged. The supplied complete diff changes exactly Reading, Master and Run: three Reading replacements plus a dated repair disposition; three substantive Master replacements plus two status/routing updates; and Run's banner plus repair-completion entry. Its substantive replacements agree with the current files. No collateral factual, claim-support or historical rewrite appears in that comparison. REPAIR_CONTEXT identifies only CR/blank-line/terminal-LF formatting outside the Reading's substantive hunks. Supplied index/HEAD labels were not verified through Git.

## Original evidence actually checked

Witness **SW-LNJP-V07**: independently recomputed EPUB SHA-256 `e586cacacab692e3ee530737d28170e5a06f74cfb8eb9437f0b1f94df9badd86` (20,577,485 bytes), matching the volume configuration and initial review. The ten consulted XHTML members below match their package-manifest hashes. Locators count one-based original `<p>` elements, including headings, blanks, separators and image paragraphs; inspected source layout agrees with the candidate's source-line paragraph rule. Original ruby/base, emphasis and typography were preserved through reversible escaped-JSON display, without source alteration.

| Absolute original route / native anchor | Actual contextual inspection |
|---|---|
| p-014.xhtml (`urn:sw-g2:source/SW-LNJP-V07/primary/item/xhtml/p-014.xhtml#toc-010`), chapter seven | P1–105: Bartholomeus's misreading, Lin's separate attention, landing, thanks, permission/contact and departure. P72–105 was established before candidate/repair exposure. |
| p-008.xhtml (`urn:sw-g2:source/SW-LNJP-V07/primary/item/xhtml/p-008.xhtml#toc-008`), chapter five | P98–252; P120–207 first, before candidate/repair exposure. Reflected attack, two barriers, Raul's intervention and subsequent plan. |
| p-017.xhtml (`urn:sw-g2:source/SW-LNJP-V07/primary/item/xhtml/p-017.xhtml#toc-013`) / p-018.xhtml (`urn:sw-g2:source/SW-LNJP-V07/primary/item/xhtml/p-018.xhtml#toc-014`), chapters ten/eleven | P135–202 / P215–288. Decisive P183–187 / P234–241/P287–288 and surrounding scenes were read before candidate/repair exposure. |
| p-004.xhtml (`urn:sw-g2:source/SW-LNJP-V07/primary/item/xhtml/p-004.xhtml#toc-004`), chapter one | P150–222, before candidate/repair exposure; especially P168–181/P208–215. |
| p-006.xhtml (`urn:sw-g2:source/SW-LNJP-V07/primary/item/xhtml/p-006.xhtml#toc-006`), chapter three | P1–209: armor identification, disclosure, earlier aftermath protection, spell slots and divided enhancement. |
| p-009.xhtml (`urn:sw-g2:source/SW-LNJP-V07/primary/item/xhtml/p-009.xhtml#toc-009`), chapter six; p-011.xhtml (`urn:sw-g2:source/SW-LNJP-V07/primary/item/xhtml/p-011.xhtml`); p-013.xhtml (`urn:sw-g2:source/SW-LNJP-V07/primary/item/xhtml/p-013.xhtml`) continuations | P1–169; P1–27; P1–11/P100–146 respectively: cooperation, expended defenses, Kara's seven spells, serial shields and split fourfold attack. |
| p-015.xhtml (`urn:sw-g2:source/SW-LNJP-V07/primary/item/xhtml/p-015.xhtml#toc-011`), chapter eight | P109–188: actual external prohibition, exhausted transport, Lin's return and Louis's accepted responsibility. |

Only **p304.jpg (`urn:sw-g2:source/SW-LNJP-V07/primary/item/image/p304.jpg`)** was freshly viewed as an image: its Lin reference states that, after recovery, she leaves exhausted Louis and goes to clean Kara's house. This is reference-channel support, distinct from the enacted embrace. Image SHA-256 `2e96e1aa92c05cf4408d352579b9c3827e50323591684e11fd6ecfa8b8768850` matches the manifest. No other illustration, afterword or earlier original unit was reinspected for this recheck.

## Finding-by-finding resolution

**M01 — Major, resolved.** [Master S-LIN/S-KARA:1153](../02%20Cumulative/SW_CG2_MASTER_LEDGER.md#L1153) and [R060:1191](../02%20Cumulative/SW_CG2_MASTER_LEDGER.md#L1191) now distinguish four actions/states. Lin adjusts the landing to hover above the ground (p-014:P81–82); she stops further spoken thanks because Kara dislikes excessive praise (P89–92); Kara opens her arms, Lin recognizes permission from books and stands against her, and Kara embraces/pats her back (P96–99); Lin regrets lacking a human's body temperature (P100–101). The last is a felt bodily limitation alongside desired closeness, not performed temperature accommodation or withheld contact. Agency and recipients are accurate. Unchanged Reading E013 (148–150), E014/E024, R018/R019/R050, K063 and W052 preserve separate attachments, mistaken courtship, depletion and reference boundaries. No generalized humanization or invented shared past results.

**M02 — Major, resolved.** [Synopsis:70](../01%20Sequential%20Readings/SW_CG2_V07_DEEP_READING.md#L70) and [W051:1213](../02%20Cumulative/SW_CG2_MASTER_LEDGER.md#L1213) now correctly assign **two maximum-strength defensive barriers to Monica and the fourfold-enhanced reflected fireball to Bradford**. P174 gives 「最高強度の防御結界を二重にして」; one shatters, the second cracks (P174/P176), fire escapes and Raul's vines intervene (P180–186). P172 explicitly contrasts earlier aftermath defense, whose narrow successful protection and wider failure are recoverable at p-006:P157–169 and unchanged E006. E011 (140–142) remains coherent. Further dependencies retain the two-maintained-spell limit and divided attack (p-006:P187–203; p-013:P134–140), serial narrow shields (p-011:P16–27), and the coordinated mirror defeat/Kara exception (p-009:P119–169; p-011:P1–15). Correcting the defense count neither weakens supported conditional competence nor attributes victory to one interchangeable power.

**m01 — Minor, resolved.** [E018:182](../01%20Sequential%20Readings/SW_CG2_V07_DEEP_READING.md#L182) correctly makes Agatha reassure **Monica** and follow **Isabel** (p-017:P183–187). Byron independently comes to return his friend Conrad's book (p-018:P234–241); the narrative explicitly marks simultaneity with Monica's tea. His reluctance to leave the book lying there as an impolite act keeps him until dismissal (P286–288). Removing the invitation restores independent agency while retaining the actual comic mechanism. E018's later explanation, Master ensemble row (1161), L085 (1240), and the open Byron/Sheila question remain coherent; no new friendship, recruitment or romantic outcome is supplied.

**Locator — corrected, nonblocking.** [E006:110–114](../01%20Sequential%20Readings/SW_CG2_V07_DEEP_READING.md#L110) adds **p-004:P150–222, especially P168–181/P208–215**, while retaining **p-006:P4–180**. The former supplies presumed-human restraint, empty armor/weight/breathing inference and initial core sealing; the latter supplies subsequent identification of spirits, selected disclosure, resource-sensitive cooperation and aftermath protection. This repairs recovery of already accurate explanation rather than inventing a new rescue intention before Louis has that knowledge.

## Dependencies, history and limits

Affected Claims **C001/RV009, C003/RV038, C006/RV042, C010/RV037, C012/RV030, C015/RV044 and C020–024**, their operative support/qualification records, and CR-V07's local comparisons were inspected. None requires temperature alteration, an unperformed embrace refusal, four defensive layers or Agatha recruiting Byron. In particular, C006's registered E006 now has the corrected locator without a new proposition or support-set expansion; C001's V07 comparisons remain local rather than newly registered support. C015's E013 retains Mary's separate leverage, and C023's E018 retains differentiated valuations. No genuine claim mechanism/boundary change is concealed and **no RV045 is warranted merely for these corrections**.

Affected file targets and section routes were checked, including the reading correction disposition, complete V07 Master/Claims layers and source-member links. The full diff leaves the original **PRE_V07 (08:11:03 UTC)** and **POST_V07 (08:34:03 UTC), 2026-10-20**, intact. The correction is separately dated **09:14:17 UTC**, followed by Run's **09:18:29 UTC** completion record. Neither freeze contains the corrected false wording; no exit supplement is needed. Run and Master continue to describe producer completion with separate source recheck pending, without self-acceptance. These are artifact dates and preserved dispositions, not independent proof of the producer's activity chronology.

Acceptance is confined to **the identified source repairs, their affected dependencies and the exact hashed candidate**, supplementing the initial review. Reading the full repaired analytical document does not certify an exhaustive fresh reading of the Japanese volume, all images, unrelated histories or the producer's complete readback. This report grants no whole-corpus acceptance/freeze, persistence, publication or authority promotion. No material source-access, integrity, independence or authority blocker was encountered.
