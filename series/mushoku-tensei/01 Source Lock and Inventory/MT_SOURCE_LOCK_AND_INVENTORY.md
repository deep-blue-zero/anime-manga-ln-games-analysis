---
title: "Mushoku Tensei - Source Lock and Inventory"
artifact_id: MT_SOURCE_LOCK_AND_INVENTORY
artifact_type: source_lock
series: "Mushoku Tensei"
generation: "V1"
version: "1.4"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V02 prose, illustrations and paratext inspected; both maps retained and byte-verified; V01 published/audited, V02 closure candidate; V03–V26 not individually admitted."
---

# Source lock and inventory — through V02

This is the analytical source-admission record. The Drive folder `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug` and historical `audit_manifest.json` (Drive ID `1m_fRXGcBbYrPgbdv26DNuOTcUxC9iWGq`) hold the underlying file inventory. The previously inspected Drive-manifest snapshot had internal audit date 2026-09-04; those checks remain historical assertions. The owner-supplied local manifest inspected during this run is dated 2026-09-25; its V02 row agrees with the freshly computed source hash. These are separate inventory observations, not fresh checks of every live file.

## Current folder and admission boundary

The 2026-09-25 live folder listing contained 25 numbered main EPUBs, V01–V11 and V13–V26, and five differently named supplements/bonuses plus the historical manifest. V12 was absent then. No exact duplicate was found by name in that listing; the manifest's archived duplicate belonged to its historical audit count and was not fetched. On 2026-09-26 UTC the restored file was reverified by Drive metadata: `Mushoku Tensei - Volume 12.epub`, ID `1RIKu1ira0Z6yYH2ILkL8BvlNPFSDi615`, 1,542,217 bytes, in the exact source folder. The owner-supplied local directory also lists V01–V26. These observations establish availability, not V12 edition identity, fresh hash/container integrity or narrative admission. The historical manifest's bonus and side-story type labels still require classification; do not treat them as main LN volumes by filename or imported `type` alone.

`LN_JP_MAIN` is the initial source family. V01 identity and text access were established in bootstrap, followed by complete declared narrative and visual inspection and owner content approval. Its required locator map is durably retained and freshly byte-verified; its closure was published and passed the final exact-head audit at `eaf159559c6fc76ddd820178d7588545f08c351d`. V02 now has a fresh local/Drive source-byte match, verified container and map, complete declared reading, and an analytical/evidence closure candidate. V03–V26 remain availability leads, not individually fresh-hash-verified or narratively admitted. No WN, supplement, adaptation, interview, review, or translation is admitted to the LN prospective reader.

| Witness | Family | Verified identity and access | Integrity and locator check | Narrative inspection | Analytical admission / limit |
| --- | --- | --- | --- | --- | --- |
| `MT-LNJP-V01` | `LN_JP_MAIN` | Drive ID `16ajoVMEswenPuSPmV-lInkYHGNa0XrPc`; internal title `無職転生 ～異世界行ったら本気だす～ 01 (MFブックス)`; creator `理不尽な孫の手`; language `ja`; publisher `KADOKAWA`; file size 2,329,909 bytes; colophon 2014-01-31 / EPUB ver.1.0 | Fresh SHA-256 `b58c6386ffebe5609c51d798ef74e7f5655fcc38910ec7c19bacee11b04651c2` equals historical manifest; ZIP CRC, EPUB container, OPF/spine references verified; 40 spine items | `INSPECTED_V01_PILOT`: 12 prose-bearing narrative spine items containing prologue, eleven episodes and Zenith extra read in order; cover/front and ten narrative plates, five design plates and other paratext classified/inspected | [V01 reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md) is owner-approved and its locator map is durably retained/byte-verified. Closure is branch-published and audited at `eaf159559c6fc76ddd820178d7588545f08c351d`. V02 has its separate record below; later units remain unadmitted. |

The V01 container points to `content.opf`, whose title/creator/language metadata agree with the historical manifest. All 40 OPF spine `idref`s resolve in its manifest. A bootstrap-only locator check parsed source item `text/part0008.html` (spine index 9, zero-based), extracted paragraph 3 among parser-selected paragraph/heading elements (105 characters; SHA-256 of the extracted UTF-8 text `52e24a67e98bf91886df770e3385734cc2532dea05ec4bafbd501fea6f0d35a2`), reopened that exact source item and reproduced the same extracted text. No passage content was displayed to the analyst. That earlier HTMLParser was only a diagnostic; the subsequent pilot used a separate `v01-lxml-p1` normalizer and actual source reading. Its locators are one-based `<p>` positions in source XHTML, including empty paragraphs; `<rt>`/`<rp>` ruby annotations are dropped while base text and separators remain. The prose coverage count is 117,875 trimmed, ruby-base Japanese characters across the 12 narrative spine items. The locator contract and selected round-trip checks are in the reading; the raw EPUB and normalized prose are evidence-plane material, not public Git content.

## Distinct verification dimensions

- Live folder presence: V01–V11 and V13–V26 in the prior listing; V12 restored and metadata-reverified on 2026-09-26 UTC. Local filenames V01–V26 are present. Availability is not a current SHA/container check on later volumes.
- Historical manifest: reports 30 primary EPUBs, 31 audited including an archived duplicate, 25 numbered main volumes and file/container checks through its stated audit date. Its taxonomy of several bonuses is not accepted without verification.
- Fresh byte/container check: V01 under the accepted pilot; V02 under the current sequential run as detailed below. On 2026-09-26 UTC the local V01 EPUB also reproduced the locked source hash; the downloaded Drive locator map reproduced its retained size and hash. No repeat narrative reading was performed.
- Narrative coverage and interpretation: V01 (13 units) and V02 (12 units), with six synchronized ledger histories. V01 visual coverage: cover/front and all ten narrative-positioned plates, five design sheets and platform mark inspected. V02 visual coverage: all 16 images, itemized in its reading. No claims of full-series visual coverage. Full-series bibliographic/supplemental completeness: not established.

The V01 source inspection and revised analytical content were approved by the owner. Retained derivative: `MT-LNJP-V01-locator-map.json`, Drive file ID `1VE1ti8fs90PHM0Ey4mvT7eQbMjUZm_u9`, retained in source folder `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`; 650,286 bytes; SHA-256 `6c782f0a8f5f30fb8a3c9d67d138185c2adae3e1b8b8d2f947424a16798c0e5c`. The earlier upload rejection was resolved by explicit authorization of that exact V01 file and destination; upload and readback succeeded in the prior session, and this session independently downloaded and hashed the retained bytes again. V01's evidence-retention condition is met. The V01 public closure is published and audited as recorded above; that result does not certify a later volume. Do not copy the EPUB, normalized prose, images or locator map into Git. Required V02–V15 locator-map uploads have separate current owner authorization as recorded in the current map; V12 still requires its individual witness verification. V03 remains unopened.

## V02 individually verified witness and derivative — 2026-09-26 UTC

| Field | Verified result |
| --- | --- |
| Witness / family | `MT-LNJP-V02` / `LN_JP_MAIN`; fresh local source and Drive file `1bI6zvLG7pRv-9TE-ZUaksdOHpeSlq0JX` agree byte for byte |
| Identity | `無職転生 ～異世界行ったら本気だす～ 02 (MFブックス)`; 理不尽な孫の手; language `ja`; KADOKAWA |
| Source bytes | 1,861,079 bytes; SHA-256 `9b8c4e654779cc792224d514cca8907379586e9dcc58bf11c3bcf86580fabd7b`, also matches the local 2026-09-25 manifest row |
| Edition dimensions | Colophon records electronic issue 2014-03-31/ver.1.0 and same-date first-printing basis; OPF date `2014-06-21T22:00:00+00:00` is distinct package metadata |
| Container | EPUB mimetype and ZIP CRC pass; container and all 35 manifest/spine references resolve; all body prose occurs in `<p>` descendants |
| Narrative coverage | 12 units: prologue, episodes 1–2, interlude, episodes 3–8, epilogue and internal “Forest Goddess” extra; 12 narrative-bearing XHTML items, including one heading-only item; 117,517 trimmed ruby-base characters; complete ordered reading, not inferred from extraction |
| Other coverage | All 16 images individually inspected; title/TOC, epigraph, bio, credits, colophon and usage notice inspected; one plate viewed immediately after the first following prose chunk, disclosed in the reading |
| Locator convention | `mt-lxml-p1`: one-based body-descendant `<p>` positions including empties; discard `rt`/`rp` readings, retain base text/tails, concatenate and trim edges without Unicode normalization; no asserted printed pagination |
| Source validation | Independent second parser checked all 4,895 paragraph positions/lengths/hashes and 574 ruby nodes against original XHTML; selected high-impact source ranges rereviewed |
| Retained private map | `MT-LNJP-V02-locator-map.json`, Drive ID `1FUJVaE3aL3-MgsTE9HUQQzIbUJssQDRL`, same source folder; 1,096,232 bytes; SHA-256 `213f8c674769fbe9ca77db4f638060ac2876556114f04ce9bc007756d386eba1` |
| Retention check | Authorized upload at `2026-09-26T04:27:07.094Z`; metadata confirms private folder and size; raw downloaded bytes reproduce exact size/hash |
| Analytical route | [V02 reading](../02%20Sequential%20Readings/MT_V02_DEEP_READING.md), 19 diagnostic observations, immutable pre-inspection recap/freeze, all six ledgers updated |
| Transaction limit | Analytical/evidence closure prepared; containing publication commit and successful final exact-head audit must follow before V03 admission; no main integration claimed |

V02's east/west anomaly descriptions and the extra's commander-name variation are retained as source irregularities rather than silently repaired. The century-later cult frame belongs to this numbered volume; it does not authorize later-volume knowledge. Unverified fates, reported family conditions and unreceived messages retain their epistemic limits. No private prose, image, EPUB or paragraph-map payload is included in this public record.
