---
title: "Shiboyugi — Source Register"
artifact_id: SBY_SOURCE_REGISTER
artifact_type: source_register
series: shiboyugi
version: "1.11"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: SBY-INITIAL
authority_scope: "Source identity, verification limits and future admission routing only"
source_boundary: "Byte-bound Japanese EPUBs V01–V10 with ordered narrative admission; other narrative outside the active scope"
created: 2026-11-13
last_updated: 2026-11-15
recommended_reasoning_class: BOUNDED_STANDARD
do_not_use_as_literary_evidence: true
---

# Source register

## Identity and witness responsibility

This register governs source identity for **Playing Death Games to Put Food on the Table / 死亡遊戯で飯を食う。**. The source library uses the alias Shiboyugi. Consult the canonical evidence-library inventory and the matching supplied-file audit through authorized evidence access; private object identifiers and receipt locations are deliberately not reproduced in Git. The November 13, 2026 live metadata reconciliation bound this identity to the canonical evidence root.

A witness slot below is a stable project identifier, not a certified hash lock. Its W01 suffix identifies the supplied witness candidate. Before first admission, resolve that slot to an exact immutable file receipt in the evidence plane and record the locator-producing extraction version. A different hash creates a new witness version; it never silently replaces W01. Hashes in the existing audit are reported evidence until the selected bytes and retrieval route are checked by the assigned source owner.

## Available units

At the November 13 metadata pass, every row was AVAILABLE_METADATA_MATCHED, NOT_ADMITTED and NOT_INSPECTED_BY_PROJECT. The activation record below supersedes those initial availability states. The unique live standardized name and byte size match the corresponding audit-manifest record. Numbering is observed source packaging, not verified publication or story chronology.

| Witness slot | Supplied unit | Recorded canonical Japanese title | Observed bytes | Reported package warning |
|---|---|---|---:|---|
| SBY-JP-V01-W01 | V01 | 死亡遊戯で飯を食う。【電子特典付き】 | 10,500,092 | None recorded |
| SBY-JP-V02-W01 | V02 | 死亡遊戯で飯を食う。２【電子特典付き】 | 6,742,817 | None recorded |
| SBY-JP-V03-W01 | V03 | 死亡遊戯で飯を食う。３ 【電子特典付き】 | 9,426,908 | mimetype is not the first ZIP entry |
| SBY-JP-V04-W01 | V04 | 死亡遊戯で飯を食う。４ 【電子特典付き】 | 7,586,149 | None recorded |
| SBY-JP-V05-W01 | V05 | 死亡遊戯で飯を食う。５ 【電子特典付き】 | 8,139,835 | None recorded |
| SBY-JP-V06-W01 | V06 | 死亡遊戯で飯を食う。６ 【電子特典付き】 | 10,804,062 | mimetype is not the first ZIP entry |
| SBY-JP-V07-W01 | V07 | 死亡遊戯で飯を食う。７ 【電子特典付き】 | 10,758,171 | mimetype is not the first ZIP entry |
| SBY-JP-V08-W01 | V08 | 死亡遊戯で飯を食う。８ 【電子特典付き】 | 5,918,751 | None recorded |
| SBY-JP-V09-W01 | V09 | 死亡遊戯で飯を食う。９【電子特典付き】 | 11,571,867 | None recorded |
| SBY-JP-V10-W01 | V10 | 死亡遊戯で飯を食う。10【電子特典付き】 | 8,342,773 | None recorded |

The audit's source-language fields are ja for all ten units. All ten titles mark electronic bonuses; the exact bonus scope and whether each component is narrative remain unknown. Publication dates, print equivalence, official release completeness and the ultimate series endpoint have not been verified. There is no claim that ten available files constitute a complete official collection.

The audit's filename metadata records the creator strings 鵜飼 有志 and, for volumes 02–10, ねこめたる, with 株式会社KADOKAWA and some MF文庫J labels. These are attributed metadata, not independently verified creator-role, edition-history or publisher-bibliography findings. Do not convert filename ordering into an author/illustrator assignment or use it as literary evidence.

## Verification layers

**Observed in this reconciliation.** The canonical folder and its parent placement were verified by metadata; all ten numbered EPUB names and byte sizes matched unique manifest units. The audit report and audit manifest were read. The pipeline audit directory was listed; its detailed inspection and rename-plan contents were not read.

**Reported by the supplied-file audit.** The report dated November 13, 2026 states that all extractable XHTML spine prose was screened excluding navigation and ruby readings, with three distributed samples per volume and Japanese grammar in all thirty. It reports no flagged Han-heavy low-kana windows, ZIP CRC/container/package/spine/referenced-resource checks passing, 208 raster images decoded, distinct EPUB and extracted-spine hashes, and original bytes preserved through renaming. Text embedded in images was outside its language review.

**Scope of the November 13 pass.** That pass ended at filename/size agreement. V03, V06 and V07 retain the reported ZIP order warnings. The activation record below distinguishes the fresh tests from inherited observations. Neither check is a full formal EPUBCheck certification.

The provenance route is a supplied-file audit. No Calibre-import, Kobo-purchase, individual receipt, acquisition legality or ownership certification is asserted. Internal acquisition names and raw receipts remain private. A public methodological description cannot replace the underlying evidence-plane provenance record.

## Component and admission boundaries

At an authorized preparation boundary, classify each actual spine component as main narrative, separately identified bonus narrative, illustration, afterword/creator statement, front/back matter, preview/advertisement or unresolved. Map embedded and linked illustrations to the prose boundary they may disclose. Do not expose later previews or a bonus whose disclosure frontier exceeds the allowed unit merely because the container is available.

The numbered main volumes are the initial proposed sequential backbone, subject to source verification and owner-authorized start/terminal scope. A volume file is not automatically one indivisible admission class. A bonus gets a component-qualified identity, for example a future SBY-JP-V03-W01/BONUS-01, only after it is actually identified. No such bonus identity or chapter count is invented now.

Japanese prose governs wording, register and narration claims. Illustrations are a separate inspected source layer; afterwords are creator statements. A translated, revised, print, manga or audiovisual witness requires its own identity and admission decision. Its account never fills a gap in this witness silently. Shared titles do not establish adaptation equivalence or continuity.

## Source obligations at the metadata baseline

| ID | Unresolved requirement and consequence | Owner and acceptance condition |
|---|---|---|
| SBY-SO-001 | Exact-byte witness binding is not independently verified; current metadata cannot anchor future load-bearing locators | Assigned source owner, before admission: resolve selected witness and private receipt, record hash/extraction identity and test retrieval |
| SBY-SO-002 | Spine, chapter, illustration and bonus boundaries are unmapped; blanket file admission could leak previews or extras | Source owner, within authorized preparation scope: component map with admission class and spoiler frontier |
| SBY-SO-003 | Japanese text/illustration access has not been exercised by this project; inherited language audit excludes image text | Future reader: verify selected TEXT route and required STILL_IMAGE route, preserve ruby/base distinctions and report inaccessible channels |
| SBY-SO-004 | V03/V06/V07 carry package-order warnings; usability and parser consequences remain untested | Source owner when a warned witness is selected: faithful-open check or documented unresolved failure; preserve original bytes |
| SBY-SO-005 | Numbered order, edition details and external collection completeness are not independently established | Metadata reviewer before any claim requiring them: verify necessary bibliographic facts; do not block a narrower justified source scope merely for unrelated completeness |
| SBY-SO-006 | No source run or electronic-bonus admission is authorized | Owner and run executor: recover explicit bounded mode/start/terminal and component decisions; only then satisfy/open the initiation gate |

These are source obligations, not narrative hypotheses. A later resolution appends its actual evidence, scope, date and responsible role; it must not silently turn inherited checks into fresh inspection. The source register changes availability or admission state only as far as the accompanying accepted transaction establishes.

## Locator and recovery contract

A future evidence ID resolves through its owning full reading to a witness slot, actual component, stable internal member/anchor or paragraph index and a readable chapter/scene label. The private receipt supplies exact file and extraction identity. Test a material quotation's locator against the witness. EPUB display pages are not print pagination.

Coverage records distinguish AVAILABLE, TRANSPORT_VERIFIED, BYTE_BOUND, ADMITTED, INSPECTED and CLOSED_FOR_DECLARED_SCOPE. Those stages are independent of architectural maturity. The initial metadata pass closed no narrative. The current entrypoint records the active frontier. Source updates do not rewrite historical receipts, earlier coverage or disclosure boundaries.

Start recovery at the [current entrypoint](CURRENT_STATE_AND_CORPUS_MAP.md) and the [method](SHIBOYUGI_ANALYTICAL_METHOD.md).

## Run activation verification

On November 15, 2026, the principal source owner retrieved and rehashed all ten attached EPUBs and all ten working copies. The digests match the supplied-file audit and historical replication receipt. The independent evidence specialist rehashed the ten originals separately. The historical Drive readback verified name, size and folder placement. The fresh identity test used the attached and working bytes. The private witness receipts pin the exact files, supplied provenance, extractor digest and ordered component maps.

The packages passed fresh ZIP CRC, package/manifest, Japanese metadata, XHTML and navigation-fragment checks. All 208 raster images decoded. V03, V06 and V07 opened with their original entry-order warnings and unchanged bytes. The TEXT route accounts for all main body prose using actual XHTML paragraphs and maps every ruby annotation to its base segment. A same-witness Japanese title locator at V01 S25 P0001 and JPEG transport/decode at V01 S11-I01 were verified. These checks establish source access before literary inspection.

`Sxx` is the 1-based OPF spine item, `Pxxxx` is the 1-based XHTML body paragraph in document order including layout paragraphs, and `Sxx-Ixx` is an image reference in that item. The witness receipt resolves every item to an actual internal member. Base rendering removes ruby readings from the display, keeps them retrievable as pairs, and marks XHTML line breaks. Exact quotations are checked against the XHTML.

The table reflects the corrected component mapping recorded below.

| Witness | Spine | Main paragraph blocks | Ruby readings in main text | Main image references |
|---|---:|---:|---:|---:|
| SBY-JP-V01-W01 | 27 | 2286 | 2751 | 8 |
| SBY-JP-V02-W01 | 29 | 2375 | 3798 | 5 |
| SBY-JP-V03-W01 | 35 | 2197 | 3754 | 7 |
| SBY-JP-V04-W01 | 31 | 2186 | 3096 | 5 |
| SBY-JP-V05-W01 | 31 | 2283 | 3502 | 5 |
| SBY-JP-V06-W01 | 31 | 2362 | 2929 | 5 |
| SBY-JP-V07-W01 | 34 | 2371 | 2316 | 6 |
| SBY-JP-V08-W01 | 29 | 2220 | 3312 | 4 |
| SBY-JP-V09-W01 | 36 | 2092 | 2692 | 7 |
| SBY-JP-V10-W01 | 37 | 2068 | 2877 | 7 |

SBY-SO-001 is resolved for all ten witnesses. SBY-SO-002 is resolved for the main allowlist and illustrated placements. The structurally marked bonus in each edition has a separate unresolved scope and spoiler obligation. Afterwords, navigation, notices and colophons stay outside narrative evidence. Explicit advertisements and uncertain back-matter images are withheld. Source-relevant front illustrations may be classified after the same unit's main prose freeze, with the bonus and preview firewall intact. SBY-SO-003's route tests passed. Actual source inspection belongs in each reading's coverage receipt. SBY-SO-004 is resolved for the verified parser. SBY-SO-005 remains open for external bibliography. SBY-SO-006 is resolved for the authorized main run. V01 main is admitted at activation and V02–V10 await their unit frontiers.

## V01 coverage and component correction

The principal source owner and three separately assigned specialists finished the Japanese text scope of SBY-JP-V01-W01. The principal inspected the original illustrations and text-bearing guide in the admitted spine and the current-volume front art after the prose-end freeze. The [deep reading](readings/SHIBOYUGI_V01_DEEP_READING.md) and [checkpoint](checkpoints/SHIBOYUGI_V01_CHECKPOINT.md) record the actual coverage, retrieval and exclusions. Only the V01 main and stated art scope is closed.

The first component map mistakenly included short members before the afterword. V01 S18–S19 have signed 解説 headings, independently observed by the character and language specialists. Their output exposure occurred after the principal's assignment release and is excluded from those specialists' findings. The principal and evidence specialist did not open those contents. The corrected private map and reader refuse these members and classify analogous signed headings in V02 S19–S20 and V03 S24–S26 by structure alone. The actual EPUBs and the remaining admitted paragraph/ruby locators are unchanged. Earlier receipt bytes were preserved. The current counts in the table reflect these corrections. No later narrative was opened for the correction. Bonus and unresolved back matter remain governed by SBY-SO-002 and excluded from the main reading lane.

## V02 coverage

The principal completed all 2,375 paragraph positions, the five at-position plates and six delayed original front and cover plates of SBY-JP-V02-W01. Two specialists completed independent main-prose passes, and the language specialist's selective pass reached 2,065 positions across all four narrative members. The [V02 reading](readings/SHIBOYUGI_V02_DEEP_READING.md) and [V02 checkpoint](checkpoints/SHIBOYUGI_V02_CHECKPOINT.md) route details and achieved source scope. All assigned V02 reading used the corrected component classification and witness receipt. Signed commentary S19–S20 and all afterword, bonus and unclassified material stay outside this unit's main evidence. V03 followed its independent committed frontier.

## V03 coverage

The principal completed all 2,197 paragraph positions in main prose, the seven at-position plates S11/S13/S14/S16/S18/S20/S22 I01 and six delayed cover/front plates S01–S06 I01 of SBY-JP-V03-W01. Evidence, character and language readers independently covered all 2,197 paragraph positions. The independent reviewer reopened diagnostic prose and checked all thirteen eligible plates. See the [V03 reading](readings/SHIBOYUGI_V03_DEEP_READING.md) and [V03 checkpoint](checkpoints/SHIBOYUGI_V03_CHECKPOINT.md) for the scope, name and reporting differences. Retrieval used the immutable v2 locator through an added wrapper gating access on Git's committed entrypoint. The supplied package retains a reported first-entry mimetype warning and passed retrieval and image verification. S24–S26 signed commentary, afterword, publisher notices, electronic bonus, advertisements and unresolved back artwork are excluded. V04 followed the committed frontier.

## V04 coverage and component correction

The principal completed all 2,186 main-prose positions in S13/S15/S17/S19/S21/S23, five same-volume plates S14/S16/S18/S20/S22 I01 at their narrative placements and nine delayed V04 cover/front images S01–S09 I01. Evidence, character and language readers independently read all 2,186. The independent reviewer reopened decisive prose and checked the fourteen eligible images. Delayed S11-I01 proved to be V04 navigation, with no literary testimony. S24-I01, previously counted as a sixth main illustration by package location, proved to be next-volume promotion when the principal encountered it after all prose. The allowed narrative image count above is five. The corrected local guard refuses S24-I01, including during delayed inspection. Original EPUB and receipt bytes and all paragraph locators remain unchanged. This graphic's contents are excluded and do not establish later evidence. The [V04 checkpoint](checkpoints/SHIBOYUGI_V04_CHECKPOINT.md) records the principal's loss of full prospective independence on affected V05 topics and the independent handoff for that boundary. See the [V04 reading](readings/SHIBOYUGI_V04_DEEP_READING.md) for actual literary scope. S10/S12 administrative and navigation text, S25–S31 afterword, bonus, other back matter and advertisements remain excluded. V05 awaited the verified committed frontier.

## V05 coverage and independent prospective remedy

The principal completed all 2,283 positions in S14/S16/S19/S21/S23. An interrupted response for S21 P0268–0407 was read again in full before advancing. Five original placed images S15/S17/S18/S20/S22-I01 were inspected at their disclosure positions, and ten delayed V05 images S01–10-I01 after the prose freeze. They include the same-volume cover, portraits and title page. S12-I01 was separately verified as navigation and stays out of literary evidence. The evidence, character and language roles each read all 2,283 positions independently. Critical review reopened decisive prose and verified the fifteen eligible originals. S11/S13 and S24–31 are outside the literary scope. S25 stays withheld. Precise qualification and evidence layering appear in the [V05 reading](readings/SHIBOYUGI_V05_DEEP_READING.md). The [V05 checkpoint](checkpoints/SHIBOYUGI_V05_CHECKPOINT.md) preserves a separately authored prospective record frozen before the independent evidence specialist opened this volume, and the principal’s more limited scope after the previously excluded promotion exposure. Release of the next Japanese main unit requires this volume's verified committed transaction.

## V06 coverage with embedded coda illustration

The principal read all 2,362 Japanese positions in S14/S16/S18/S20/S22, including all layout and the S22 P0139 image reference. S15/S17/S19/S21-I01 were read at their positions. S22-I01 is a same-story ending image inside the final prose member and was opened after the P0139 marker and the prose freeze. Its position is neither delayed front matter nor a separate trailing promotional member. Ten delayed front images S01–10-I01 were read at unit end. S12-I01 was inspected solely to classify it as navigation. The evidence, character and language readers independently read all 2,362 positions. Critical review reopened decisive original prose and checked all fifteen admitted images. The V06 ZIP retains its known non-first mimetype entry warning and the verified bytes. Genuine main-source reading and same-witness image decode succeeded without alteration. S11/S13 and S23–31 stay outside the literary argument. S24 and S25 remain unread. The [reading](readings/SHIBOYUGI_V06_DEEP_READING.md) and [checkpoint](checkpoints/SHIBOYUGI_V06_CHECKPOINT.md) supply the evidence, prospective scope and publication-independent committed frontier requirements.

## V07 coverage and the narrative text plate

The principal, evidence, language and character readers each independently covered all 2,371 Japanese paragraph and layout positions in S14/S16/S19/S21/S23/S25, and the six placed originals S15/S17/S18/S20/S22/S24 in presentation order. S17-I01 is an all-text narrative plate, visually read in full at its location between the apartment chapter and the next captioned frontispiece. The ten same-volume covers, profiles and title originals S01–10 were delayed to unit end. S12 was then identified as contents navigation. Independent critical review reopened original prose and checked the sixteen eligible assets and the S12 boundary. The verified unchanged EPUB retains its non-first mimetype warning with all rasters decodable. S11/S13 and S26–34 are outside the literary reading, including excluded navigation artwork and withheld indeterminate S27/S28. The [V07 reading](readings/SHIBOYUGI_V07_DEEP_READING.md) and [checkpoint](checkpoints/SHIBOYUGI_V07_CHECKPOINT.md) route the evidence findings and cover their exposure boundaries.

## V08 coverage and delayed apparatus

Four full reading roles each independently covered all 2,220 numbered Japanese paragraph/layout positions in S14/S16/S18/S20/S22 and the four original interleaves S15/S17/S19/S21 at their positions. Their independent exits precede inspection of ten delayed cover, profile and title originals at S01–10. S12 was classified at exit as graphical contents. The critical role reopened decisive Japanese with the same admitted visual boundaries and reviewed the exact staged transaction. The unchanged archive has mimetype first and all nineteen rasters decode. S11/S13 and S23 onward are outside the literary boundary, including withheld indeterminate S26, afterword and bonus material. The [V08 reading](readings/SHIBOYUGI_V08_DEEP_READING.md) and [checkpoint](checkpoints/SHIBOYUGI_V08_CHECKPOINT.md) give the specific evidence and custody bounds.

## V09 coverage and two placed text plates

Four independent whole-text reading roles covered all 2,092 original Japanese or layout positions in S14/S16/S18/S21/S24/S26, including seven placed original assets in disclosure order S15/S17/S19/S20/S22/S23/S25. S19 (recruitment patterns) and S22 (high clearing counts and motivation) are full-text assets read in place with their claims and evidentiary scope identified. Ten same-volume covers, profiles and title originals S01–10 were delayed until separate prose and placed-image freezes, followed by classification of S12 as graphical contents. The critical lane reopened decisive native passages and viewed the same eligible originals with exact isolation from the staged text, then tested the staged reading. The unchanged witness has mimetype first and all 26 rasters decoded. S11/S13 and S27–36 are excluded, including unresolved S28–30 and S33 and bonus and advertising text. Consult the [V09 deep reading](readings/SHIBOYUGI_V09_DEEP_READING.md) and [checkpoint](checkpoints/SHIBOYUGI_V09_CHECKPOINT.md) for the accepted provenance and remaining uncertainty.

## V10 coverage and authorized source end

Four principal/specialist roles read all 2,068 Japanese prose or layout positions in S14, S16, S19, S21, S23 and S26, and seven placed originals in order S15/S17/S18/S20/S22/S24/S25. S17 is the in-position unattributed scale exposition, S24 the in-position unattributed retirement exposition. Both text-bearing originals were completely read where placed. Ten same-volume cover, profiles and title originals S01–10 were delayed until separate prose and placed-material freezes. S12 proved graphical contents and contributed only navigation. The independent critical reviewer checked decisive native windows and all eligible originals before exact-unit review. The unchanged witness has mimetype first and all 25 packaged rasters decoded technically. S11, S13 including its navigation image and S27–37 remain excluded, including unresolved S28–31 and S34 and the bonus, afterword and advertising material. No scope anomaly occurred in V10.

The [V10 reading](readings/SHIBOYUGI_V10_DEEP_READING.md), [entering freeze](checkpoints/SHIBOYUGI_V10_ENTERING_STATE.md) and [checkpoint](checkpoints/SHIBOYUGI_V10_CHECKPOINT.md) complete the V01–V10 source tract following the nine preserved unit transactions. The high-water mark is V10, with no authorized next candidate and no authorized supplemental narrative. Current synthesis, qualification and evidence-limited reconstruction judgments may proceed across these ten readings without acquiring another witness. Remaining external bibliography and bonus/preview component questions have no authority over the completed Japanese primary boundary.
