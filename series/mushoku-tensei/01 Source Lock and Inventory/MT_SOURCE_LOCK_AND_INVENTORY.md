---
title: "Mushoku Tensei - Source Lock and Inventory"
artifact_id: MT_SOURCE_LOCK_AND_INVENTORY
artifact_type: source_lock
series: "Mushoku Tensei"
generation: "V1"
version: "1.2"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Drive listing, V01 verified EPUB, completed V01 Japanese prose and illustration inspection on 2026-09-25; no V02 narrative."
---

# Source lock and inventory — V01 pilot

This is the analytical source-admission record. The Drive folder `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug` and historical `audit_manifest.json` (Drive ID `1m_fRXGcBbYrPgbdv26DNuOTcUxC9iWGq`) hold the underlying file inventory. The manifest has internal audit date 2026-09-04; its earlier byte checks are historical assertions, not fresh checks of all live files.

## Current folder and admission boundary

The 2026-09-25 live folder listing contains 25 numbered main EPUBs, V01–V11 and V13–V26, and five differently named supplements/bonuses plus the historical manifest. **V12 is absent in the live listing.** The owner had already reported a likely transfer failure. Whether and when a replacement arrives is unknown. No exact duplicate was found in this folder listing by name; the manifest's one archived duplicate belongs to its historical audit count and was not fetched here. Bonus and side-story type labels in that manifest require further classification; do not treat them as main LN volumes by filename or imported `type` alone.

`LN_JP_MAIN` is the initial source family. V01 identity and text access were established in bootstrap, then its narrative and images were inspected for this pilot; its analytical transaction remains open pending durable locator mapping. V02–V11 and V13–V26 are inventory-visible, **not** individually fresh-hash-verified or narratively admitted. V12 blocks a later continuous main LN passage beyond V11. No WN, supplement, adaptation, interview, review, or translation is admitted to the LN prospective reader.

| Witness | Family | Verified identity and access | Integrity and locator check | Narrative inspection | Analytical admission / limit |
| --- | --- | --- | --- | --- | --- |
| `MT-LNJP-V01` | `LN_JP_MAIN` | Drive ID `16ajoVMEswenPuSPmV-lInkYHGNa0XrPc`; internal title `無職転生 ～異世界行ったら本気だす～ 01 (MFブックス)`; creator `理不尽な孫の手`; language `ja`; publisher `KADOKAWA`; file size 2,329,909 bytes; colophon 2014-01-31 / EPUB ver.1.0 | Fresh SHA-256 `b58c6386ffebe5609c51d798ef74e7f5655fcc38910ec7c19bacee11b04651c2` equals historical manifest; ZIP CRC, EPUB container, OPF/spine references verified; 40 spine items | `INSPECTED_V01_PILOT`: 12 prose-bearing narrative spine items containing prologue, eleven episodes and Zenith extra read in order; cover/front and ten narrative plates, five design plates and other paratext classified/inspected | [V01 pilot reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md) is a provisional Git candidate; durable locator-map placement is blocked and the sequential transaction remains open. Later units remain unadmitted. |

The V01 container points to `content.opf`, whose title/creator/language metadata agree with the historical manifest. All 40 OPF spine `idref`s resolve in its manifest. A bootstrap-only locator check parsed source item `text/part0008.html` (spine index 9, zero-based), extracted paragraph 3 among parser-selected paragraph/heading elements (105 characters; SHA-256 of the extracted UTF-8 text `52e24a67e98bf91886df770e3385734cc2532dea05ec4bafbd501fea6f0d35a2`), reopened that exact source item and reproduced the same extracted text. No passage content was displayed to the analyst. That earlier HTMLParser was only a diagnostic; the subsequent pilot used a separate `v01-lxml-p1` normalizer and actual source reading. Its locators are one-based `<p>` positions in source XHTML, including empty paragraphs; `<rt>`/`<rp>` ruby annotations are dropped while base text and separators remain. The prose coverage count is 117,875 trimmed, ruby-base Japanese characters across the 12 narrative spine items. The locator contract and selected round-trip checks are in the reading; the raw EPUB and normalized prose are evidence-plane material, not public Git content.

## Distinct verification dimensions

- Live folder presence: V01–V11 and V13–V26; V12 missing on 2026-09-25. This is metadata, not a current SHA check on the other 24 volumes.
- Historical manifest: reports 30 primary EPUBs, 31 audited including an archived duplicate, 25 numbered main volumes and file/container checks through its stated audit date. Its taxonomy of several bonuses is not accepted without verification.
- Fresh byte/container check: V01 only. Its prose is machine parseable and a source-to-extraction-to-source-item locator round trip worked.
- Narrative coverage and interpretation: V01 only, with 13 narrative units and six synchronized ledgers; no V02. Visual coverage: cover/front and all ten narrative-positioned plates, five design sheets and platform mark inspected; no claims of full-series visual coverage. Full-series bibliographic/supplemental completeness: not established.

The V01 source has been inspected and the owner approved the revised analytical content. A hash-only paragraph/ruby locator map was constructed locally, but automatic approval review rejected its upload to the Drive source folder as derivative metadata from a private EPUB going to an unverified destination without explicit approval of the payload and destination. The map remains in transient scratch, so the method's durable evidence-plane requirement is unmet and the sequential transaction is not closed. Do not copy the EPUB or raw normalized prose into Git. Exact historical editions and the missing V12 remain open obligations before claims that depend on them. V02 is an inventory item only until V01's durable evidence requirement and transaction closure are satisfied.
