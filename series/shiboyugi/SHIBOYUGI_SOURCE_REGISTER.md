---
title: "Shiboyugi — Source Register"
artifact_id: SBY_SOURCE_REGISTER
artifact_type: source_register
series: shiboyugi
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: SBY-INITIAL
authority_scope: "Source identity, verification limits and future admission routing only"
source_boundary: "Metadata reconnaissance of supplied Japanese novel volumes 01–10; no narrative admitted"
created: 2026-11-13
last_updated: 2026-11-13
recommended_reasoning_class: BOUNDED_STANDARD
do_not_use_as_literary_evidence: true
---

# Source register

## Identity and witness responsibility

This register governs source identity for **Playing Death Games to Put Food on the Table / 死亡遊戯で飯を食う。**. The source library uses the alias Shiboyugi. Consult the canonical evidence-library inventory and the matching supplied-file audit through authorized evidence access; private object identifiers and receipt locations are deliberately not reproduced in Git. The November 13, 2026 live metadata reconciliation bound this identity to the canonical evidence root.

A witness slot below is a stable project identifier, not a certified hash lock. Its W01 suffix identifies the supplied witness candidate. Before first admission, resolve that slot to an exact immutable file receipt in the evidence plane and record the locator-producing extraction version. A different hash creates a new witness version; it never silently replaces W01. Hashes in the existing audit are reported evidence until the selected bytes and retrieval route are checked by the assigned source owner.

## Available units

Every row is AVAILABLE_METADATA_MATCHED, NOT_ADMITTED and NOT_INSPECTED_BY_PROJECT. The unique live standardized name and byte size match the corresponding audit-manifest record. Numbering is observed source packaging, not verified publication or story chronology.

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

**Not established by this project.** No EPUB was downloaded, reopened, independently hashed, text-extracted, fully language-audited, visually inspected or narratively read. Filename/size agreement is not byte identity. The audit is not a full formal EPUBCheck certification. The non-first mimetype warnings were preserved, not silently repaired. If a future reader cannot open a warned package faithfully, record the failure and preserve the original; any repaired derivative needs an explicit source-to-derivative map.

The provenance route is a supplied-file audit. No Calibre-import, Kobo-purchase, individual receipt, acquisition legality or ownership certification is asserted. Internal acquisition names and raw receipts remain private. A public methodological description cannot replace the underlying evidence-plane provenance record.

## Component and admission boundaries

At an authorized preparation boundary, classify each actual spine component as main narrative, separately identified bonus narrative, illustration, afterword/creator statement, front/back matter, preview/advertisement or unresolved. Map embedded and linked illustrations to the prose boundary they may disclose. Do not expose later previews or a bonus whose disclosure frontier exceeds the allowed unit merely because the container is available.

The numbered main volumes are the initial proposed sequential backbone, subject to source verification and owner-authorized start/terminal scope. A volume file is not automatically one indivisible admission class. A bonus gets a component-qualified identity, for example a future SBY-JP-V03-W01/BONUS-01, only after it is actually identified. No such bonus identity or chapter count is invented now.

Japanese prose governs wording, register and narration claims. Illustrations are a separate inspected source layer; afterwords are creator statements. A translated, revised, print, manga or audiovisual witness requires its own identity and admission decision. Its account never fills a gap in this witness silently. Shared titles do not establish adaptation equivalence or continuity.

## Open source obligations

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

Coverage records distinguish AVAILABLE, TRANSPORT_VERIFIED, BYTE_BOUND, ADMITTED, INSPECTED and CLOSED_FOR_DECLARED_SCOPE. Those stages are independent of architectural maturity. The present high-water mark is NONE and every witness remains unadmitted. Source updates do not rewrite historical receipts, earlier coverage or disclosure boundaries.

Start recovery at the [current entrypoint](CURRENT_STATE_AND_CORPUS_MAP.md), then this register and the [method](SHIBOYUGI_ANALYTICAL_METHOD.md). No inventory row, successful parser run or source-folder existence authorizes sequential work.
