---
title: "Mushoku Tensei - Source and Scope Map"
artifact_id: "MT_SOURCE_AND_SCOPE_MAP"
artifact_type: "source_scope_method"
series: "Mushoku Tensei"
generation: "V1"
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
design_reference_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
adopted_on: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
canonical_home: "series/mushoku-tensei/00 Frameworks and Methods/MT_SOURCE_AND_SCOPE_MAP.md"
source_boundary: "Accepted bootstrap method or template; no sequential novel readings or validated character models as of adoption."
recommended_reasoning_class: "DEEP_SYNTHESIS"
---

# Source and scope map

## 1. Responsibility

This file defines source families, admission rules, and retrieval responsibilities. [MT_SOURCE_LOCK_AND_INVENTORY.md](../01%20Source%20Lock%20and%20Inventory/MT_SOURCE_LOCK_AND_INVENTORY.md) is the live Git **analytical admission record** established at bootstrap. The Drive manifest remains the evidence-file inventory; do not maintain two competing byte inventories.

The series entrypoint routes to the admission record. It must distinguish source availability, integrity, actual inspection, analytical admission, and completed readings. All current availability claims must be rechecked at bootstrap.

## 2. Seed evidence routes, not a new audit

The owner supplied the Mushoku Tensei evidence folder:

Drive folder ID `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`

The prior audit manifest has Drive file ID `1m_fRXGcBbYrPgbdv26DNuOTcUxC9iWGq` and an internal audit date of 2026-09-04. Its supplied contents record 25 numbered main volumes (1-11 and 13-26), five other primary EPUBs, and one separately archived duplicate. The main files use English filenames but report Japanese internal language metadata. These are **historical manifest assertions**. The bootstrap source-lock file records the separate fresh V01 byte check and current folder listing; the other EPUBs were not freshly hash-checked.

The owner subsequently reported that V12 probably failed to transfer and would be recopied. The live folder listing at adoption also lacks V12. Record it as currently missing, with restoration pending; do not treat this as permanent unavailability.

The manifest identifies a side-story file as Japanese Redundancy 1, a Recollection file, late-volume bonuses, and a Special Book purchase bonus. Several per-file `type` fields classify bonus/side material as `main_volume`; a file named only Short Story is not the full Special Book. Resolve internal titles and content before accepting any normalized filename as identity. The reported integrity totals include an archived duplicate and are not the same as the live main-volume count.

No main-series chapter/scene completeness audit, full supplemental bibliography, or new source lock is delivered here. No acquisition or automated extraction is authorized merely by listing a source.

## 3. Source families

| Family | Analytical role | Admission rule |
|---|---|---|
| `LN_JP_MAIN` | Principal published-Japanese prose continuity | Verify individual edition, then read sequentially within authorization. |
| `LN_JP_SUPPLEMENT` | Author-written side/after-stories or collected extras | Identify each story, publication placement, narrative placement, and continuity relation. |
| `RETAILER_BONUS` | Separately distributed textual witness | Identify parent purchase, actual author/title, edition, and reprint overlap. |
| `WN_CURRENT` | A dated snapshot of the currently hosted web text | Not automatically the original publication state or interchangeable LN canon. |
| `WN_HISTORICAL` | Authenticated prior snapshot, revision, or deleted material | Preserve capture date, origin, completeness, and authentication limits. |
| `LOCALIZATION` | Named translation witness | Claims remain edition/language-specific; do not invent Japanese nuance. |
| `ILLUSTRATION_PARATEXT` | Art, cover, appendix, advertising, or framing | Identify creator and role; not automatically an event in the fiction. |
| `CREATOR_COMMENTARY` | Dated first-party statements of process or intention | Read exact statement and context; separate contemporary from retrospective claims. |
| `PUBLISHER_PLATFORM_RECORD` | Bibliography, editorial statement, or moderation policy | Establishes only what its authority/scope supports. |
| `ADAPTATION` | Manga/anime or other incarnation | Separate project lane with explicit medium and edition. |
| `RECEPTION` | A named person's or community artifact's interpretation | Evidence of that response, not proof of canon, prevalence, or audience effects. |

Treat these as local source classes, not a new global registry schema.

## 4. Source-order protocol

Begin with verified Japanese LN V01. Do not acquire or inspect the entire franchise merely to open the gate. An intact authorized prefix can support a bounded run while later gaps remain disclosed.

Default main reading excludes WN content, retrospective interviews, and adaptation knowledge as evidence. Optional isolated comparisons may proceed after a closed LN unit only within separately authorized source scope. Maintain separate high-water marks; `LN through V05` does not mean `WN fully compared through V05`.

For each supplemental story, record:

`story ID | source witness | earliest verified publication | reprint publication | diegetic placement | earliest spoiler-safe admission | actual admission | overlaps/variants | confidence`

Default uncertain or retrospective material to deferred admission. A main LN may include its own after-story at the volume boundary when verified non-future-facing. An afterword remains commentary, not objective character interiority.

Recollection, the Special Book, Redundancy, later bonuses, and optional web side works are research targets. Verify the actual current bibliography and distinctions before locking their membership. Do not carry forward earlier release schedules, number-of-stories claims, or purported author quotations as verified catalog data.

## 5. Witness identity and provenance

An exact witness needs at least a local ID, canonical title from the source, author/creator as credited, language, source family, edition/store/revision where material, file hash or immutable provider revision, acquisition/retrieval date, content coverage, and access/inspection state.

Keep the descriptive source record separate from the file's incidental filename. A new retailer copy may be the same textual edition with different packaging; a byte difference does not establish a literary revision. Conversely, matching titles do not establish identical text.

Public Git records must omit credentials, signed URLs, private receipts, device identifiers, and unnecessary personal paths. The stable Drive folder can be a retrieval route for an authorized reader without publishing its contents. Check the live policy before adding any new Drive-only reference entry.

## 6. EPUB verification and deterministic derivatives

Verify container/ZIP readability, spine/navigation order, parseable text, missing or duplicate narrative items, and representative visual rendering. File integrity is not narrative completeness. An apparently intact EPUB may have incomplete source text or faulty extraction.

Preserve paragraphs, headings, speaker/typographic cues, ruby associations, scene breaks, and image links. Document removed navigation, duplicated ruby readings, normalization, and any display-only characters. Do not silently replace original wording with machine translation or a cleaned paraphrase.

For the first unit, prove a retrieval round trip: exact source item -> normalized paragraph -> source item again. Spot-check the opening, middle, closing, interludes, and every consequential quoted passage when completing a volume. Scanned or fixed-layout pages require an appropriate visual/text route; OCR is a last resort and uncertainty must remain visible.

Never interpret a successful script run as model inspection. Save processing logs in the working/evidence plane, not as literary findings.

## 7. Completeness dimensions

Record these separately:

| Dimension | Example distinction |
|---|---|
| Bibliographic coverage | All declared main volumes versus selected supplements. |
| File integrity | Container readable versus broken transfer. |
| Narrative coverage | All spine narrative sections versus a missing chapter. |
| Text inspection | Entire declared prose read versus searched excerpts. |
| Visual inspection | Illustrations inspected versus prose-only pass. |
| Cross-version coverage | Complete aligned range versus targeted diagnostic sample. |
| Reception coverage | Declared purposive sample, not all fans. |
| Repository state | Drafted, branch-published, or integrated. |

A corpus can be complete for Japanese main-LN prose analysis and incomplete for the franchise, visual rhetoric, textual genetics, or reception. State the exact completion target.

## 8. Optional dependencies and blocking rules

Missing supplements do not prevent early main-LN analysis. They prevent claims that require them and any declared synthesis whose required scope includes them. Missing audiovisual access does not block a prose-only character model; it blocks a performed-voice or adaptation-framing claim.

Record each gap's affected claim/scope, severity, next responsible role, and closure criterion. Use `REQUIRED`, `OPTIONAL`, or `OUT_OF_SCOPE` separately from `PENDING`, `PARTIAL`, `UNAVAILABLE`, or `COMPLETE_FOR_DECLARED_SCOPE`. Do not demote a necessary source to optional just to close a gate.

## 9. Source conflicts

Do not harmonize conflicting versions silently. First test identity, edition, chronology, focalization, translation, and admission boundary. Then classify the discrepancy as a textual revision, contradiction within a witness, character error, or unresolved difference.

Later commentary may illuminate intention but cannot silently insert missing words into an earlier edition. A current Narou page proves current displayed wording, not when that wording first appeared. A historical editorial-direction claim needs dated witnesses or direct documentary support.

## 10. Bootstrap output

The source-lock record should contain a verified inventory reference, admitted primary family, next usable unit, known gaps, representation/locator capabilities, spoiler rules, and separately tracked optional lanes. Do not copy the historical manifest wholesale into Git or mark every file inspected. The bootstrap report must say precisely what was checked and what remains owner-reported.
