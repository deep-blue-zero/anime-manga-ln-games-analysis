---
series: TOMOZAKI
artifact_type: sequential_completion_audit
scope: V12_SOURCE_AND_SIX_OWNER_COMPLETION_VALIDATED_AND_PUBLISHED
source_boundary: "Admitted Japanese main V01–V12 plus separately routed V06.5/V08.5; this receipt audits the selected V12 witness, not a new fourteen-witness retrospective sweep"
source_audit_date: 2026-10-22
generation: V1.3_PUBLICATION_RECEIPT
status: canonical
release_state: mutable_active
review_state: SOURCE_TRANSACTION_AUTHOR_PUBLICATION_PASS_LATER_RECONCILIATION_AUDIT_SEPARATE
baseline_commit: 0a74e0403c3e32f438f61875142cc40c64a783e7
publication_base_commit: 4ffa438746869e28fdbd073eb933d4c0e7247ccd
canonical_entrypoint: "../CURRENT_STATE_AND_CORPUS_MAP.md"
source_lock: "../01 Source Lock and Inventory/TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md"
prospective_snapshot: TOMOZAKI_V12_PROSPECTIVE_ENTERING_SNAPSHOT.md
narrative_consulted: true
illustration_pixels_consulted: true
source_consultation_complete: true
sequential_completion_certified: true
certification_scope: V12_SOURCE_SIX_OWNER_AND_NAMED_SUBJECT_ACCEPTANCE_WITH_TESTED_SOURCE_PAYLOAD_AUTHOR_PREFLIGHT
repository_checks: FINAL_SOURCE_TRANSACTION_AUTHOR_PREFLIGHT_PASS_INDEX_9548
published_commit: 406b26c4591a9bce99c83a54600286f56a35678e
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Tomozaki V12 — source coverage and sequential-transaction completion audit

## 1. Decision, scope, and prospective gate

**V12 source consultation, six-owner substantive consistency, named-subject/reference review, final staged author preflight, publication at `406b26c4591a9bce99c83a54600286f56a35678e` and its exact-head CI audit have passed. The source transaction is certified at that declared scope, with V12/completed/NONE fields. §6.5 records actual publication and the later repository reconciliation; integration and any newer head require their own verified outcomes.** The integrating author and a separate social/voice source reviewer independently completed all 42 linear spine members, all 26 actual JPEG occurrences, the author afterword, colophon, and the non-spine navigation document. Section 6.4 preserves the earlier source-payload check; §6.5 records the completed final receipt/currentness recheck and actual published object. No later containing commit's self-hash is invented here.

The owner authorized `continuous_sequential`, start `V12`, terminal `V12`, followed by the separately governed retrospective campaign. Before first story or image access, the [prospective entering snapshot](TOMOZAKI_V12_PROSPECTIVE_ENTERING_SNAPSHOT.md) was committed at **`0a74e0403c3e32f438f61875142cc40c64a783e7`**. The snapshot's SHA-256 is **`8741334f47c5640fa446629ba5c06c58784479a9802f962bc49af61b43105e17`**. Source access began only after the integrating author confirmed the committed freeze and opened the content gate. Each guarded source-reading invocation required the selected EPUB's full corrected SHA-256 and a byte-identical canonical snapshot present in committed HEAD. The mechanical guard supported reproducibility; owner authorization and semantic gate acceptance remained separate requirements.

The [admission audit](TOMOZAKI_V12_SOURCE_ADMISSION_AUDIT.md) remains the unchanged pre-prose receipt: its `PENDING` content rows accurately describe that earlier checkpoint. This later audit owns the subsequent consultation result; it does not falsify what was known before reading. V01–V11 freezes, R01–R05 acceptances, and both supplements' story-local routing are preserved.

## 2. Exact witness and provenance

| Field | Verified identity / limit |
|---|---|
| Japanese title / language | `弱キャラ友崎くん　Ｌｖ．12` / `ja` |
| Selected normalized filename | `Bottom-Tier Character Tomozaki - Volume 12.epub` |
| Selected witness bytes | **10,165,455** |
| Owner-approved local SHA-256 | **`4b1b7242e5e92e015e0f9d138a43c6f7f06452761bd697ebc2df2c7195287c7c`** |
| Acquisition identity | Existing local Calibre library, ID **116**; original and normalized local copy independently hash-identical |
| Associated Drive object | `1JiEphan-hEtNiyBRIooarYbjoaDcerFh`, within series source folder `1YldXgz3sglS1CLD_CvUieUM_GOr-VElg` |
| Package | EPUB3; OPF `item/standard.opf`; UUID `00d6e4fc-ff3e-43a5-9b7b-6c6b7c6acd52`; creator 屋久ユウキ; publisher 株式会社小学館 |
| Local import receipt | `calibre_import_manifest_2026-10-22.json`, 3,807 bytes; SHA-256 `30428e6547dab10c85e09c05dcb756e39f87a2fd9fe289464edb60b6cc610188`; located Drive ID `12MUzeIMtgLLSG7pEtKd-9qIXGsm0hTxp` |
| Local propagation receipt | `drive_propagation_manifest_2026-10-22.json`, 1,720 bytes; SHA-256 `b380a4db7eb37a2cfba0ebdea835253f512ab0e31455d3d24e9d17cfa501b3f7`; located Drive ID `1N12TxxCjlhenJDHMTeyyv1va340PjKkm` |
| Import Markdown note | `CALIBRE_IMPORT_2026-10-22.md`; located Drive ID `1wA7MIfUkrF6OpoBQQ-vBwzlFxT8uOwXR`; remote note describes metadata-only verification |
| Remote-byte limitation | Raw Drive EPUB retrieval failed with `Transport closed`; no remote EPUB bytes independently hashed. Remote JSON text retrieval supplied no content. Located IDs and local receipt hashes do not certify remote byte identity. |
| Publication information read from colophon | `item/xhtml/p-0031.xhtml` P4: electronic issue **2026-10-16**; P14: print base first impression **2026-10-21**; P16: **ISBN978-4-09-453186-2** |

The pasted task digest ended `...5287c2c`; the independently verified digest ends `...5287c7c`. This discrepancy was reported before story access, and the owner expressly corrected and approved the verified local identity on **2026-10-22**. The admission audit retains both complete digests and independent PowerShell/Python checks. This is a documented correction, not a match to the erroneous input.

The historical thirteen-witness audit dated 2026-08-29, SHA-256 `64e5e9e722a24f578abc20b3de1b61269c1212e224b60786e7eab28d35b66257`, remains distinct. Its V07 Special Edition and V04/V11 packaging warnings are unchanged. This operation did not claim to repeat a whole-corpus literary audit.

## 3. Package and complete consultation accounting

The admission operation checked **79/79 unique ZIP members** with complete CRC PASS, safe paths, no encryption, first/stored exact `mimetype`, valid container/OPF/XML, **75 manifest resources**, **42 linear spine items**, and resolving checked local XML `src`/`href` references. The manifest comprises 43 XHTML, four CSS, 26 JPEG, one NCX and one JavaScript resource. All image dimensions were recorded there. The packaged `js/kobo.js` was **not executed**. No full EPUBCheck run is claimed; local-reference checks do not certify every CSS construct, external destination, or rendering behavior.

The reading convention is reproducible: **P** counts every HTML `<p>` one-based within its member, including empty/image paragraphs. **U** preserves complete source-ordered body units, including text outside paragraphs; **X** marks such text and **E** explicitly accounts for ruby annotations that occur outside a paragraph. Paragraph numbering does not change when ruby is displayed. Ruby bases remain intact; `--show-ruby` adds readings in `《》`, and layout `rp` is omitted. These display brackets are helper annotation, not an assertion that the source contains those brackets.

The source was read in small, untruncated, successive chunks with `--compact --show-ruby`; no search-based excerpt sampling substituted for full narration. The complete spine totals are **5,244 P**, **5,255 U**, and **148,658 visible base characters**. That character count excludes ruby readings, scripts/styles/layout whitespace and text embedded in JPEG pixels; actual images were separately inspected. It is a coverage diagnostic, not a word-count claim or proof of semantic correctness.

| Spine | Member | P | U | Visible base characters | JPEG occurrences | Consultation |
|---:|---|---:|---:|---:|---:|---|
| 1 | `item/xhtml/p-0001.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 2 | `item/xhtml/p-0002.xhtml` | 4 | 4 | 34 | 0 | COMPLETE |
| 3 | `item/xhtml/p-0003.xhtml` | 2 | 2 | 70 | 0 | COMPLETE |
| 4 | `item/xhtml/p-0004.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 5 | `item/xhtml/p-0005.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 6 | `item/xhtml/p-0006.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 7 | `item/xhtml/p-0007.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 8 | `item/xhtml/p-0008.xhtml` | 8 | 8 | 167 | 0 | COMPLETE |
| 9 | `item/xhtml/p-0009.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 10 | `item/xhtml/p-0010.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 11 | `item/xhtml/p-0011.xhtml` | 543 | 544 | 16694 | 0 | COMPLETE |
| 12 | `item/xhtml/p-0012.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 13 | `item/xhtml/p-0013.xhtml` | 591 | 592 | 16642 | 0 | COMPLETE |
| 14 | `item/xhtml/p-0014.xhtml` | 483 | 484 | 16471 | 0 | COMPLETE |
| 15 | `item/xhtml/p-0015.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 16 | `item/xhtml/p-0016.xhtml` | 1308 | 1308 | 37814 | 0 | COMPLETE |
| 17 | `item/xhtml/p-0017.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 18 | `item/xhtml/p-0018.xhtml` | 432 | 432 | 13307 | 0 | COMPLETE |
| 19 | `item/xhtml/p-0019.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 20 | `item/xhtml/p-0020.xhtml` | 66 | 66 | 1148 | 0 | COMPLETE |
| 21 | `item/xhtml/p-0021.xhtml` | 433 | 439 | 11528 | 0 | COMPLETE |
| 22 | `item/xhtml/p-0022.xhtml` | 979 | 980 | 23208 | 0 | COMPLETE |
| 23 | `item/xhtml/p-0023.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 24 | `item/xhtml/p-0024.xhtml` | 16 | 17 | 532 | 0 | COMPLETE |
| 25 | `item/xhtml/p-0025.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 26 | `item/xhtml/p-0026.xhtml` | 284 | 284 | 7007 | 0 | COMPLETE |
| 27 | `item/xhtml/p-0027.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 28 | `item/xhtml/p-0028.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 29 | `item/xhtml/p-0029.xhtml` | 43 | 43 | 3574 | 0 | COMPLETE |
| 30 | `item/xhtml/p-0030.xhtml` | 4 | 4 | 113 | 0 | COMPLETE |
| 31 | `item/xhtml/p-0031.xhtml` | 22 | 22 | 349 | 0 | COMPLETE |
| 32 | `item/xhtml/p-0032.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 33 | `item/xhtml/p-0033.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 34 | `item/xhtml/p-0034.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 35 | `item/xhtml/p-0035.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 36 | `item/xhtml/p-0036.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 37 | `item/xhtml/p-0037.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 38 | `item/xhtml/p-0038.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 39 | `item/xhtml/p-0039.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 40 | `item/xhtml/p-0040.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 41 | `item/xhtml/p-0041.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |
| 42 | `item/xhtml/p-0042.xhtml` | 1 | 1 | 0 | 1 | COMPLETE |

All rows were completed in spine order. In particular, `p-0011`, `p-0013`, `p-0014`, `p-0022` and `p-0024` have non-p chapter-heading text; `p-0021` includes four source-ordered heading text units and two ruby-reading units before P1. None was silently skipped. The separate `item/navigation-documents.xhtml` has **0 P / 14 U**, was read after the spine, and repeats navigation/guide labels rather than adding a narrative supplement. The earlier metadata count of twelve anchors and nine NCX navPoints is a different structural measure, not an unconsulted chapter count.

The local Windows runtime used Python **3.12.4**, Beautiful Soup and Pillow, with PowerShell available for independent hashes. The temporary helper was reviewed before first content access; its full-source and freeze guards ran on each reading invocation. The audit records actual execution rather than claiming a selectable model/reasoning control was verified. No raw source text dump, EPUB, illustration or helper is made an analytical Git artifact.

## 4. Actual illustration and paratext role audit

All **26 JPEG occurrences** were viewed from actual extracted pixels, at their source positions. Filename inference and image headers alone were not treated as visual consultation. The following role classification supersedes only the admission receipt's deliberately unclassified image roles, not its historical header observations.

| Spine / image | Role established by actual review | Evidentiary restriction |
|---|---|---|
| p0001 `i-000a.jpg`; p0004 `i-0001_01.jpg` | Cover variants: **Kikuchi Fuka**, offered palm and colorful cloth. Author afterword p0029 P29–33 explicitly identifies Kikuchi and explains the comparison with V01. | Not Hinami. Cover framing is not a new diegetic event. The author's V01 comparison is attributed paratext; this V12 audit did not reopen V01 pixels. |
| p0005 `i-0002_01.jpg` | Decorative paired paper birds/game motifs and design credit. | Symbolic/front-matter framing, not proof a later action already occurred. |
| p0006 `i-0003-0005_01.jpg` | Color Kikuchi/star-trails frontispiece. | Anticipatory literary visual, not a separate narrated historical scene. |
| p0007 `i-0006-0008_01.jpg` | Color fantasy/manuscript ensemble under the embedded-novel motif. | Distinguish fictional modeling from real character biography. |
| p0009 `i-0009_01.jpg` | Cast/relationship introduction with character labels. | Publisher summary, including Mizusawa's hairdresser aspiration, is distinct from a newly witnessed career decision. |
| p0010 `i-0010_01.jpg` | Pictorial six-chapter contents and print-page starts. | Navigational paratext, no extra story. |
| p0012 `i-0051_01.jpg` | Four-person writing-party portrait grouping Mizusawa, Mimimi, Kikuchi and Fumiya. | Supports the assembled scene without giving all four identical motives or complete shared knowledge. |
| p0015 `i-0135_01.jpg` | Mitsu in kimono/dark glasses, stern and physically present. | No diagnosis, spouse status or invented identity follows. |
| p0017 `i-0233_01.jpg` | Kikuchi attending to a damaged paper bird. | Careful observation is not proof she has already solved authorship. |
| p0019 `i-0269_01.jpg` | Kikuchi writing on a rock by the night sea. | Following prose overturns Fumiya's initially godlike aesthetic impression with her distress; beauty does not certify wellbeing. |
| p0023 `i-0373_01.jpg` | Child Nagisa's smiling/pointing presence in the reader-fiction identification sequence. | Not a photograph, actual resurrection or independent deceased-person testimony. |
| p0025 `i-0377_01.jpg` | Tearful Hinami with manuscript on the bench. | Present vulnerability, not durable clinical recovery. |
| p0027 `i-0397_01.jpg` | Formal English series-name/`Fin.` closing page. | No additional episode. |
| p0028 `i-0398-0399_01.jpg` | Smiling uniformed Hinami and Fumiya raising fists toward each other. | Closing rivalry/reciprocity framing; no match result or future romance certified. |
| p0032–p0036 `i-zzzb_01`–`05.jpg` | Gaho No234/October2026 cover and book promotional cards. p0034 repeats V12 Kikuchi cover, blurb and author comment. | Promotional wording is not an additional scene or independent psychological corroboration. Other advertised fiction is outside the Tomozaki boundary. |
| p0037–p0042 `i-zzzc_01`–`06.jpg` | Anime advertisements, unrelated horror promotion, publisher lineup, prize recruitment, media-mix headlines and editorial notices. | Publication/advertising paratext only; no hidden Tomozaki story supplement. No QR/site was opened or adaptation admitted. |

The 15 pre-advertising images comprise seven cover/front-matter images, six narrative illustrations, a `Fin.` page and a closing spread; eleven trailing advertising images complete the 26. This classification does not count frontispiece fantasy as actual testimony or a pictured imagined Nagisa as an independent source.

`p-0029.xhtml` P1–43 was read fully as **author afterword**. Yaku calls this the present final numbered volume for his thematic answer while allowing another series book with no promised date. His mention of still-writable classmates' futures, Tsugumi, Rena, Ashigaru, Kikuchi's dream, Mizusawa's feelings and professional Fumiya does not add those future events to the admitted narrative. `p-0030.xhtml` P1–4 is an author-profile joke, not character evidence. `p-0031.xhtml` P1–22 is colophon/publication/legal notice. Neither supplies a further story.

## 5. High-propagation attribution and limit checks

| Check | Result required in reading and cumulative owners | Controlling primary locators |
|---|---|---|
| Focalizer | p0022's first-person `私` is **Hinami**; p0024 returns to Fumiya's `俺`. Reader access to Hinami's private thoughts does not become Fumiya/peer knowledge. | p0022 P3–110, P114–135; p0024 P3–16 |
| Osaka trigger | Hinami identifies the room/scroll image as the acute reminder, while already familiar with mother/Haruka's faces. Her recollection after the trigger is incomplete. No named religion is justified. | p0022 P42–78 |
| Model, fiction and model-subject | Kikuchi's Alcia/Chris/Nana/Sharif scenes, the fictional Nagisa and performed improvisation remain authored/acted representations. Their detail does not certify private Hinami/Nagisa history. | p0013 P200–277, P366–482; p0022 P746–979 |
| Semantic ruby | Alcia/`私`, real-name/fictional-name overlays and `魔法` read as story stage identification. Preserve base/reading distinction without treating a ghost as a new witness. | p0022 P867–871, P947–979 |
| Nagisa cause | Death intention and final experience remain explicitly unknowable; guilt and desired gratitude do not resolve accident versus intent. The pre-existing V10/V11 school-year discrepancy is not harmonized. | p0022 P504–512, P825–845, P874–932; p0026 P117 |
| Distress at sea | Kikuchi is cold, distressed, and calf-deep in water; Fumiya brings her back. No explicit suicidal intent or diagnosis is given. | p0021 P23–61 |
| Consent and delivery | Contributors consent to particular acts; Hinami refuses the delivered manuscript before Haruka reads and urges her to take it. Continued reading and tears establish engagement/effect without retroactive blanket consent. | p0011 P240–291, P374–507; p0022 P124–226, P230–284 |
| Narrative ethics | Kikuchi expressly states Hinami's tears do not make the novel right or verify real Nagisa's feelings. Her owned prayer after observation does not abolish uncertainty. | p0021 P324–433; p0026 P114–119 |
| Distributed labor and cost | Peers contribute different capacities, resist, and redirect. The council program is underplanned while Fumiya/Mimimi focus on the novel; Ashigaru supplies live recovery. | p0013 P9–82; p0014 P30–154; p0022 P124–226; p0026 P177–234 |
| Ordinary and institutional return | Hinami appears at school, sits among peers, responds to familiar teasing and chooses to play. This does not certify full office restoration, complete repair, or sustainable labor allocation. | p0026 P209–239 |
| Final correctness reply | Hinami says she has stopped clinging to correctness. This is her self-description, not an instruction that Fumiya stop; the reply alone does not prove permanence. | p0026 P266–268 |
| Temporal outcome | A little self-liking is direct present speech; permanence is explicitly uncertain. No final match result, career success, graduation, marriage or sequel event is narrated. | p0026 P15–23, P239–284; p0029 P9–19 |
| Earlier replay gap | The opening 31-frame Boxman input blank is observed, but its motive is not resolved. Do not explain the V11 win as intentional mercy or sabotage. | p0011 P3–25 |

All short member forms in this table denote `item/xhtml/p-NNNN.xhtml` in the witness bound in §2. **DIRECT** observations, attributed reports, **CORROBORATED INFERENCE**, **INTERPRETIVE HYPOTHESIS**, **VALUE JUDGMENT** and **OPEN** conclusions must remain labeled in their analytical owners. This audit constrains attribution; it does not substitute for the full literary argument or inherited-claim adjudication.

## 6. Atomic transaction and validation gate receipt

| Responsibility | Actual state at V1.2 |
|---|---|
| Owner digest correction and local package identity | VERIFIED at admission; unchanged |
| Pre-prose prospective freeze | COMMITTED before content at the exact commit/hash in §1 |
| Full Japanese narrative in source order | COMPLETE, independently read by integrating author and source reviewer |
| Non-p text and semantic ruby | COMPLETE at the stated P/U convention; all visible base text accounted |
| Actual illustrations and all ending paratext | COMPLETE; 26/26 pixels and full afterword/profile/colophon classified |
| Canonical V12 deep reading / inherited-claim adjudication | COMPLETE and ACCEPTED; canonical/immutable-freeze reading and exit state included in the source-payload author preflight PASS. Publication remains separate |
| Character-state ledger | V12 §19 substantively accepted after independent full-extension review and included in the combined source-payload preflight PASS |
| Relationship-state ledger | V12 §17 substantively accepted after independent full-extension review and included in the combined source-payload preflight PASS |
| Effort/competition/goal ledger | V12 §§79–84 accepted after integrating-author complete readback; all 29 hypotheses preserved |
| Claim-revision/evidence index | V12 §18 accepted after integrating-author complete readback; 40/14/15 crosswalks and 359/154 universe verified |
| Social atmosphere/group-systems ledger | V12 patch substantively REVIEWED and ACCEPTED; combined semantic/name review and source-payload author preflight PASS; publication separate |
| Japanese voice/register/key-terms ledger | V12 patch substantively REVIEWED and ACCEPTED; combined semantic/name review and source-payload author preflight PASS; publication separate |
| Six-owner atomic consistency / substantive review | PASS; all six owners changed and accepted together with the source-facing reading. Source-payload preflight PASS; final receipt-metadata recheck required before commit; publication separate |
| Active V12 admission checkpoint on main | MERGED through PR 281 at `4ffa438746869e28fdbd073eb933d4c0e7247ccd`; exact admission-head and main audits SUCCESS, as recorded in §6.3 |
| Bounded named-subject/reference audit | PASS at combined V12 reading/six-owner scope after integrating-author acceptance; no material unresolved referent or attribution defect retained in that scope |
| Stable-branch staged author preflight / link and structural checks | PASS for all sixteen source-payload paths in the tested 9,533-path INDEX snapshot at tree `40993f96775f24b18b490bf130c2396d2648b958`; final receipt/currentness metadata recheck REQUIRED before commit |
| V12 high-water mark / source-run completion | SOURCE TRANSACTION CERTIFIED at V12/completed/NONE within the declared scope. Publication base `4ffa438746869e28fdbd073eb933d4c0e7247ccd` retains its historical V11/active state; completion commit/publication not asserted here |
| Completion transaction's exact published head / successful Repository integration audit / main merge | PENDING; `published_commit: null`. The merged admission checkpoint does not certify the later completion transaction |
| Fourteen-witness retrospective character/omission audit and R06 | NOT COMPLETED by this source pass |
| Relationships, seven thematic responsibilities, convergence and final synthesis | NOT CERTIFIED by this receipt |
| Derived reconstruction and formal terminal governance closure | NOT CERTIFIED; separate governed stages remain |

The integrating author owns the combined review, all Git/index/ref operations, high-water-mark change and publication. This audit's author may report completed source consultation but cannot predeclare those later outcomes. The pending rows must be updated only from actual completed evidence, with exact validation and publication results where they exist.

### 6.1 Assigned-path review performed before handoff

The completion-audit author read both complete SOC/JVL originals at the baseline in §1 and reviewed every original-to-candidate deletion/replacement: current metadata/routing labels, the historical-V11 direction to the new SOC overlay, and JVL-15's source-grounded V12 answer. **All22 SOC-C identities and all24 JVL identities remain.** Accepted dated R04/R05 enrichments and the historical SOC revision-history text remain unchanged. No historical source freeze or admission receipt was edited.

The bounded name/reference check covered this audit's opening, image-role table, high-propagation table and closing gate statement; the full new SOC §17, including each contributor and Mitsu/Andi witnesses; and the full new JVL §13, including all recipient/layer tables and the ending limitation. Known actors are named. Anonymous innkeeper, local fish/shop witnesses and children are **SOURCE_REQUIRED_ANONYMITY** with **JUSTIFIED_ROLE_REFERENCE** describing their access. The Alcia/Nagisa/ruby distinctions are **KNOWLEDGE_BOUNDARY_REQUIRED**; the imagined Nagisa is not collapsed into a direct real-world witness. No material **UNNECESSARY_GENERICIZATION**, **AMBIGUOUS_REFERENT** or unresolved **INCORRECT_IDENTITY_OR_ATTRIBUTION** remained in this assigned scope. The cover identification is Kikuchi, as the afterword explicitly states.

On 2026-10-22, final assigned-candidate UTF-8/LF, YAML metadata, rectangular Markdown tables, local file-link existence and paragraph-address bounds were checked. The full final scan covered **73 SOC paragraph-address occurrences in §17, 79 JVL occurrences in §13, and 38 occurrences across this audit**, against the independently counted source members. Each explicit P address/range is counted once per occurrence, including repeated references and the single JVL address whose member is named later in its table row. The earlier 72/75/30 checkpoint and subsequent eighteen changed-line range checks remain historical verification receipts; these final totals replace them for the current candidates. Bounds checks establish address validity, not interpretation by themselves. `git diff --check` passed for the two tracked ledger patches. A console-encoding failure during the first preservation-opcode display was rerun with UTF-8 stdout; it was a diagnostic-display failure, not source or document corruption. None of these checks constitutes the root's final staged author preflight, combined semantic acceptance, exact-head repository audit or publication result.

### 6.2 Historical preintegration acceptance of the prepared source transaction — 2026-10-22

This subsection records the accepted source candidate and the admission blocker **before PR 281 was integrated**. Its OPEN/unmerged, unapplied-metadata and failing-diagnostic statements are historical checkpoint observations. The current resolution and still-pending completion gates are recorded separately in §6.3.

All three source readers completed the whole verified witness before exchanging findings. The integrating author then read the complete contributions and independent reviews. The source-facing reading, all 40 inherited dispositions, 14 prospective answers, 40 new claims, 36 corpus families, 15 standing OQ families, 29 effort hypotheses, 30 CS identities, 16 REL identities, 22 SOC identities and 24 JVL identities have substantively consistent current dispositions. No ledger-wide NO CHANGE was used.

Review produced and propagated four material precision controls: Hinami's final correctness remark is her present self-description rather than an instruction to Fumiya; Ashigaru carries an underprepared event without a proven extemporaneous-talk claim; the final exhibition is accepted and Found selected but its match/result are unnarrated; Mimimi's separation fear concerns her own self-regard while she trusts the continuing Tama tie. Reluctant once-only role-play assent, actual delivery pressure, and Tama's observed cake-sharing remain distinguished from unproven willingness or interior pleasure. The underlying positive developments and unresolved ethical tensions are preserved.

The integrating-author mechanical review found zero new-table-width, orphan-ID, proposed-claim drift, checked-local-link or explicit preceding-member paragraph-bound errors. It independently verified exact agreement of all 40 DR12/CRI new propositions and routes, all stable owner ID sets, and 22 unchanged historical/accepted artifacts: thirteen earlier readings, seven existing character files, the entering snapshot and the original admission audit. Those checks support preservation and retrieval; they do not replace source interpretation or the final repository validator. The six owner additions preserve their original accepted historical spans as separately checked by their authors/reviewers.

**External admission dependency:** admission PR 281 was last verified OPEN/READY/UNMERGED, with its exact head `0a74e0403c3e32f438f61875142cc40c64a783e7` green. Actual main was `bded61febd88a2c27ddbe15da2fe9babb80319f3` and did not yet contain that active V12 run. Initiation policy §3.9.4 permits completed new-reading admission when main already records the same active run, or through a legitimate proof exported from an existing completed commit. The current candidate has no such completion commit/proof. No failing completion commit, artificial history, active relabeling of completed work, comparison-ref substitution, or classification change is used to bypass the requirement. The analysis author cannot merge its own PR.

The canonical committed map therefore remains HWM V11 with the active authorized V12 run. Seven targeted completion metadata candidates are prepared separately for the later atomic transaction; they are not applied and do not advance that committed boundary. Final staged author preflight has not been represented as PASS. After actual admission integration, preserve current heads, apply the reviewed metadata, promote/freeze the accepted reading within the complete transaction, run the actual staged author preflight and inspect the full diff, then publish normally and await the exact-head audit. The fourteen-witness retrospective audit remains downstream of that V12 freeze; none has been started by this receipt.

A read-only targeted invocation of the repository's actual `_validate_run_admission` function confirmed the dependency against the fetched main bytes and proposed completed/NONE metadata: `new sequential admission requires an active authorized run; OPEN alone is insufficient`. The same function reports no run-state error only in the explicitly conditional comparison where the committed active admission checkpoint has first been accepted. This diagnostic is not full staged author preflight, does not substitute another ref for actual main, changes no index/ref, and creates no completion commit. No successful repository-completion result is claimed.

At that prepared checkpoint, the [V12 path and validation manifest](TOMOZAKI_V12_PATH_AND_VALIDATION_MANIFEST.json) bound the sixteen-path proposed transaction, reviewed working files, separately prepared metadata, stable-ID accounting and exact preservation digests. Its prepared/noncurrent state certified neither application of those metadata candidates nor a new published head. Those original review digests remain historical receipts in the updated manifest.

### 6.3 Historical admission-resolution checkpoint before staged preflight — 2026-10-22

This subsection preserves the state after guarded application and **before the successful source-payload author preflight**. Its pending-preflight and uncertified-source statements describe that earlier checkpoint; §6.4 records their subsequent resolution. Publication, exact-head CI and integration remain separate pending gates.

Admission **[PR 281](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/281)** was merged from final published head **`857a9c54839e2652a496d4b44588fa0172e58ebe`** into main at **`4ffa438746869e28fdbd073eb933d4c0e7247ccd`**. Its final-head **[Repository integration audit run 39893103762](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/actions/runs/39893103762)** and the merge commit's **[main audit run 39893494098](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/actions/runs/39893494098)** both succeeded. The earlier `0a74e0403c3e32f438f61875142cc40c64a783e7` remains the prospective-freeze/admission baseline and initial published head, not the final reconciled admission head. The analysis author did not merge its own PR.

The local analytical branch was fast-forwarded to the integrated main commit, preserving all sixteen prepared payloads. The incoming accepted governance/tooling changes did not change any Tomozaki path. The repository's actual `_validate_run_admission` function then reported **zero admission errors** against that real main entrypoint and the reviewed V12/completed/NONE candidate. Main now contains the same authorized active V12 run required by initiation policy §3.9.4; no comparison-ref substitution or manufactured completion proof was used. This targeted diagnostic is PASS at admission scope and is **not** final staged author preflight.

The guarded application subsequently verified the seven original/candidate metadata hash pairs and the reviewed reading hash, then applied those seven completion metadata files and exactly the accepted reading's authority-header/exit-title promotion. The applied map records HWM V12, `run_state: completed` and next operation `NONE` **in the uncommitted worktree**. The committed admission HEAD still records HWM V11 and the active V12 run. The manifest's fifteen-file applied-payload hash map includes this updated audit and excludes the manifest itself to avoid a self-hash cycle; its older reviewed/prepared digest dictionaries remain historical review receipts.

**Final staged author preflight remains PENDING.** No completion commit, completion publication, completion exact-head audit or integration is certified here; `sequential_completion_certified` remains false and `published_commit` remains null. The integrating author must inspect and stage the complete declared sixteen-path transaction, run the actual repository author preflight and required checks, inspect the complete final diff, and publish only after PASS. Admission's successful audits certify the admission checkpoint, not this later uncommitted completion payload.

The four campaign closure states therefore remain distinct: **source-run completion awaits final validation and publication; literary closure has not passed; derived-model work has not passed; formal terminal governance closure has not passed.** The fourteen-witness retrospective character/omission audit, R06, principal updates, relationship/ensemble and seven thematic responsibilities, adversarial convergence, final synthesis LAST, literary release and justified derived models all remain downstream. This resolution removes the admission dependency without shrinking the continuous campaign.

### 6.4 Source transaction and staged source-payload validation accepted — 2026-10-22

The integrating author staged the exact sixteen-path completion allowlist and ran the governing validator, without a substitute comparison ref, configuration change or suppressed check. The core invocation was:

```text
python tools/validate_repository.py --phase current --snapshot index --routing-preflight series/tomozaki --repo .
```

The actual invocation additionally supplied `--result-json` and `--timings-json` destinations outside the Git repository. It **PASSED** in `phase=current`, `snapshot=INDEX`, covering **9,533 paths**, with tested index tree **`40993f96775f24b18b490bf130c2396d2648b958`**. Result telemetry records `integration_state: success`, no deferred routing paths and no reconstruction-currentness notices; `audited_commit` is null because the validated object was the index. An earlier attempt to place telemetry under the repository's private working directory was rejected before validation; the corrected external destinations produced the actual PASS. No rejected invocation is counted as successful, and no local absolute execution path is published here.

At this source boundary, complete consultation, independent source review, all six longitudinal owners, inherited/fresh claim adjudication, and the integrating author's combined named-subject/reference semantic acceptance have passed. The current source transaction therefore records **HWM V12, `run_state: completed`, next operation `NONE`**. This audit's `sequential_completion_certified: true` is confined to those source, semantic and tested source-payload validation responsibilities. It does not mean the entire literary campaign, derived models or terminal governance has passed.

After that tested index, narrow currentness edits recorded the achieved SOC/JVL combined acceptance and the architecture's `PASS_AT_V12_BOUNDARY`. This audit and manifest now record the actual gate result and refresh the applied-payload digests. These changes introduce no new source claim or retrospective knowledge. **The final containing index, including all receipt/currentness metadata, must be restaged, fully reviewed and rerun through the same actual author preflight before commit.** The recorded tested tree identifies the completed earlier check; it is not presented as a hash of these later bytes or of a future containing commit.

The containing completion commit, completion PR, published head, new exact-head `Repository integration audit` and completion merge remain **UNKNOWN/PENDING**, with `published_commit: null`. The final commit cannot contain its own hash; these receipts do not invent one. Publication results must be verified and recorded separately from source certification. Literary release, fourteen-witness character/R06 and specialist/convergence/synthesis work, justified derived models and formal terminal governance closure remain unpassed.

### 6.5 Published source transaction and later reconciliation — 2026-10-23

After reconciling with actual main `33c79435b797dfa0cff96b9e07211bbc7117233f`, the integrating author restaged and reviewed all sixteen declared paths, including the final receipt/currentness edits. The governing author preflight **PASSED in phase=current, snapshot=INDEX, 9,548 paths**. The committed source transaction is **`406b26c4591a9bce99c83a54600286f56a35678e`**, parent `33c79435b797dfa0cff96b9e07211bbc7117233f`, tree **`7eb3fe45c1079d0ee442be2d4cf3fcd531af0a6e`**, matching the final validated index. Normal push and remote readback confirmed all sixteen payload hashes. The branch was clean apart from private untracked execution aids.

The author opened **[PR 288](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/288)**. Its source head's required **[Repository integration audit, run 39896985254](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/actions/runs/39896985254)** completed SUCCESS; the exact commit's required status independently reads success. This resolves the pre-publication unknowns in §§6–6.4. Those sections retain their historical tested objects and checkpoint statements; the null fields described within their prose are not present-day publication claims. This later receipt can name the earlier published commit without inventing a containing self-hash.

A subsequent repository reconciliation advanced the remote series branch to **`609991ad72ebff8646d8753f4c349808fc6560b6`**, an ordinary merge of main **`c407408f120143cef678a4dab65f821db56d4368`**. The only incoming paths are specialist-owned reconstruction capability data and its generated index, with six non-Tomozaki assessments. A full Tomozaki tree comparison is byte-identical. The integrating author preserved that commit by fast-forward, without editing the incoming outputs. Its **[new-head audit, run 39897839573](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/actions/runs/39897839573)** was cancelled during validation and reported an error status; the explicit full rerun, **attempt 2, completed SUCCESS** on that exact head, and its required commit status reads success. This actual result certifies the reconciled head separately from the earlier source-head result.

PR 288 was subsequently verified **MERGED** at **`73717d42aefa394207ab23bf98e774ed5cdecfb6`**, on 2026-10-23 at 04:37:37 UTC. The integrating author fetched both heads and fast-forwarded to that main merge; its full tree matches the reconciled source head. The merge commit's own required status was still absent at the receipt check, so no main-head audit success is invented. The analysis author did not merge its own PR. Later corrections and analytical tranches require their own final staged validation and exact published-head audit.

The validated source freeze enabled the authorized fourteen-witness retrospective audit, which is now active. Local omission corrections and R06 drafts are separate work; they do not retroactively invalidate the source-order freeze or certify aggregate character, relationship, thematic, convergence, literary release, derived-model or terminal-governance completion. No further narrative source is admitted by completed/NONE.

## 7. Preservation and downstream routing

The [current map](../CURRENT_STATE_AND_CORPUS_MAP.md), [source lock](../01%20Source%20Lock%20and%20Inventory/TOMOZAKI_SOURCE_LOCK_AND_INVENTORY.md), unchanged admission receipt and prospective freeze remain recoverable. The source-facing reading belongs at `02 Sequential Readings/TOMOZAKI_V12_DEEP_READING.md`; all six cumulative owners belong under `03 Longitudinal Ledgers/`. They must be accepted together before V12 becomes the committed analytical high-water mark. Historical V11 open states remain valid as earlier knowledge, even where V12 now adjudicates them.

Original EPUBs, raw/extracted novel text, illustrations and acquisition data remain outside Git. The temporary reading notebook/helper/image copies are execution aids, not canonical evidence owners or deliverables to stage. Canonical prose uses selective paraphrase, short diagnostic terms and reproducible witness/member/P locators rather than a copyrighted text dump.

**No formal series closure follows from `Fin.`, an author calling V12 final, completed source consultation, or a status label.** The authorized retrospective character coverage, R06 scope decisions, relationship/thematic specialists, adversarial convergence, final synthesis, release validation and justified reconstruction work remain distinct responsibilities. Formal terminal governance sealing requires its separately authorized owner-merged transaction.
