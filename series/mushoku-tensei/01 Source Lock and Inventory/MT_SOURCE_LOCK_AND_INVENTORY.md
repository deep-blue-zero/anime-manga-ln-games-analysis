---
title: "Mushoku Tensei - Source Lock and Inventory"
artifact_id: MT_SOURCE_LOCK_AND_INVENTORY
artifact_type: source_lock
series: "Mushoku Tensei"
generation: "V1"
version: "1.7"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V05 prose, images and paratext inspected; maps retained/verified; V01–V04 published/audited, V05 candidate; V06–V26 not individually admitted."
---

# Source lock and inventory — through V05

This is the analytical source-admission record. The Drive folder `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug` and historical `audit_manifest.json` (Drive ID `1m_fRXGcBbYrPgbdv26DNuOTcUxC9iWGq`) hold the underlying file inventory. The previously inspected Drive-manifest snapshot had internal audit date 2026-09-04; those checks remain historical assertions. The owner-supplied local manifest inspected during this run is dated 2026-09-25; its V02–V05 rows agree with the freshly computed source hash. These are separate inventory observations, not fresh checks of every live file.

## Current folder and admission boundary

The 2026-09-25 live folder listing contained 25 numbered main EPUBs, V01–V11 and V13–V26, and five differently named supplements/bonuses plus the historical manifest. V12 was absent then. No exact duplicate was found by name in that listing; the manifest's archived duplicate belonged to its historical audit count and was not fetched. On 2026-09-26 UTC the restored file was reverified by Drive metadata: `Mushoku Tensei - Volume 12.epub`, ID `1RIKu1ira0Z6yYH2ILkL8BvlNPFSDi615`, 1,542,217 bytes, in the exact source folder. The owner-supplied local directory also lists V01–V26. These observations establish availability, not V12 edition identity, fresh hash/container integrity or narrative admission. The historical manifest's bonus and side-story type labels still require classification; do not treat them as main LN volumes by filename or imported `type` alone.

`LN_JP_MAIN` is the initial source family. V01 identity and text access were established in bootstrap, followed by complete declared narrative and visual inspection and owner content approval. Its required locator map is durably retained and freshly byte-verified; its closure was published and passed the final exact-head audit at `eaf159559c6fc76ddd820178d7588545f08c351d`. V02 is published and audited at final head `687a13ac1a661270ab566c9e1a6028acd607d846`. V03 is published and finally audited at `56e1daa4bdc287cb9f2f3e4abbbea30be494628d`. V04 is published and finally audited at `f3dfe47b549cf33fddc7d2128e2b6f0bba7a8e8e`. V05 has fresh local/Drive/manifest byte agreement, verified container/map, complete reading and analytical/evidence candidate. V06–V26 remain availability leads, not individually fresh-hash-verified or narratively admitted. No WN, supplement, adaptation, interview, review, or translation is admitted to the LN prospective reader.

| Witness | Family | Verified identity and access | Integrity and locator check | Narrative inspection | Analytical admission / limit |
| --- | --- | --- | --- | --- | --- |
| `MT-LNJP-V01` | `LN_JP_MAIN` | Drive ID `16ajoVMEswenPuSPmV-lInkYHGNa0XrPc`; internal title `無職転生 ～異世界行ったら本気だす～ 01 (MFブックス)`; creator `理不尽な孫の手`; language `ja`; publisher `KADOKAWA`; file size 2,329,909 bytes; colophon 2014-01-31 / EPUB ver.1.0 | Fresh SHA-256 `b58c6386ffebe5609c51d798ef74e7f5655fcc38910ec7c19bacee11b04651c2` equals historical manifest; ZIP CRC, EPUB container, OPF/spine references verified; 40 spine items | `INSPECTED_V01_PILOT`: 12 prose-bearing narrative spine items containing prologue, eleven episodes and Zenith extra read in order; cover/front and ten narrative plates, five design plates and other paratext classified/inspected | [V01 reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md) is owner-approved and its locator map is durably retained/byte-verified. Closure is branch-published and audited at `eaf159559c6fc76ddd820178d7588545f08c351d`. V02 has its separate record below; later units remain unadmitted. |

The V01 container points to `content.opf`, whose title/creator/language metadata agree with the historical manifest. All 40 OPF spine `idref`s resolve in its manifest. A bootstrap-only locator check parsed source item `text/part0008.html` (spine index 9, zero-based), extracted paragraph 3 among parser-selected paragraph/heading elements (105 characters; SHA-256 of the extracted UTF-8 text `52e24a67e98bf91886df770e3385734cc2532dea05ec4bafbd501fea6f0d35a2`), reopened that exact source item and reproduced the same extracted text. No passage content was displayed to the analyst. That earlier HTMLParser was only a diagnostic; the subsequent pilot used a separate `v01-lxml-p1` normalizer and actual source reading. Its locators are one-based `<p>` positions in source XHTML, including empty paragraphs; `<rt>`/`<rp>` ruby annotations are dropped while base text and separators remain. The prose coverage count is 117,875 trimmed, ruby-base Japanese characters across the 12 narrative spine items. The locator contract and selected round-trip checks are in the reading; the raw EPUB and normalized prose are evidence-plane material, not public Git content.

## Distinct verification dimensions

- Live folder presence: V01–V11 and V13–V26 in the prior listing; V12 restored and metadata-reverified on 2026-09-26 UTC. Local filenames V01–V26 are present. Availability is not a current SHA/container check on later volumes.
- Historical manifest: reports 30 primary EPUBs, 31 audited including an archived duplicate, 25 numbered main volumes and file/container checks through its stated audit date. Its taxonomy of several bonuses is not accepted without verification.
- Fresh byte/container check: V01 under the accepted pilot; V02–V05 under the current sequential run as detailed below. On 2026-09-26 UTC the local V01 EPUB also reproduced the locked source hash; the downloaded Drive locator map reproduced its retained size and hash. No repeat narrative reading was performed.
- Narrative coverage and interpretation: V01 (13 units), V02 (12 units), V03 (15 units), V04 (12 units) and V05 (11 units), with six synchronized ledger histories. V01 visual coverage: cover/front and all ten narrative-positioned plates, five design sheets and platform mark inspected. V02 visual coverage: all 16 images, itemized in its reading. V03 visual coverage: all 12 images individually inspected in order. V04 visual coverage: all 16 images individually inspected in order. V05 visual coverage: all 16 images individually inspected in order. No claims of full-series visual coverage. Full-series bibliographic/supplemental completeness: not established.

The V01 source inspection and revised analytical content were approved by the owner. Retained derivative: `MT-LNJP-V01-locator-map.json`, Drive file ID `1VE1ti8fs90PHM0Ey4mvT7eQbMjUZm_u9`, retained in source folder `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`; 650,286 bytes; SHA-256 `6c782f0a8f5f30fb8a3c9d67d138185c2adae3e1b8b8d2f947424a16798c0e5c`. The earlier upload rejection was resolved by explicit authorization of that exact V01 file and destination; upload and readback succeeded in the prior session, and this session independently downloaded and hashed the retained bytes again. V01's evidence-retention condition is met. The V01 public closure is published and audited as recorded above; that result does not certify a later volume. Do not copy the EPUB, normalized prose, images or locator map into Git. Required V02–V15 locator-map uploads have separate current owner authorization as recorded in the current map; V12 still requires its individual witness verification. V06 remains unopened pending V05 publication and exact-head audit.

## V02 individually verified witness and derivative — preparation snapshot, 2026-09-26 UTC

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


## V03 individually verified witness and derivative — 2026-09-26 UTC

The prior V02 preparation limit is historical: authored commit `eba2064186272c17cf080a66bcbc9e409426c3a1` passed source audit `36218928824`, housekeeping `36219382710` and final audit `36219504894` on resulting head `687a13ac1a661270ab566c9e1a6028acd607d846`. That gate completed before V03 inspection.

| Field | Verified V03 result |
| --- | --- |
| Witness / family | `MT-LNJP-V03` / `LN_JP_MAIN`; local source and fresh Drive file `1VvZMAjmv9CF8c1A7g7BjrxycOAVNPuiJ` byte-identical |
| Identity | `無職転生 ～異世界行ったら本気だす～ 03 (MFブックス)`; 理不尽な孫の手; `ja`; KADOKAWA |
| Bytes | 1,532,476; SHA-256 `ca635c479a6a0b2e871bfb17acf50c29a277af2485b54c1dac4988d508dddbf6`; local manifest dated 2026-09-25 agrees |
| Edition | Colophon `text/part0025.html` p3 and p20–23: 2014-05-31/ver.1.0, same-date first-edition/first-printing basis. OPF `2014-06-21T22:00:00+00:00` is separate metadata. |
| Container | Mimetype, ZIP CRC, container, manifest and all 29 spine references pass; all body text in paragraph descendants |
| Narrative | Episodes1–14 and internal “Asuran Princess and Miraculous Angel” extra: 15 units, ten narrative XHTML items including heading-only title; 144,603 trimmed ruby-base characters; actual ordered reading in 55 text chunks |
| Visual / paratext | All 12 images in order, including cover/front art, narrative plates and platform logo; title/TOC, epigraph, bio, credits, colophon and notices read; no ordering exception |
| Locator | `mt-lxml-p1`: one-based body-descendant `p`, empties included; omit ruby rt/rp retaining base/tails, concatenate and trim edges without Unicode normalization; no printed-page claim |
| Independent check | All 4,941 positions, lengths/hashes and 725 ruby nodes checked against original XHTML by a second parser; consequential passages reread |
| Private retained map | `MT-LNJP-V03-locator-map.json`, Drive `1KRv1vf_Nckq70FcOGlSC-1MSNP0x6lDk`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`; 1,105,143 bytes; SHA-256 `6d261e509711e3fec834b28c0e12999f7460c3705e3053cabf8c7603b7c4dee8` |
| Retention | Authorized upload `2026-09-26T05:14:46.157Z`; correct private folder/size confirmed; raw download matches exact bytes/hash |
| Analytical route | [V03 reading](../02%20Sequential%20Readings/MT_V03_DEEP_READING.md), 22 observations, unchanged pre-inspection recap/freeze; all six ledgers and first bounded Rudeus model synchronized |
| Publication limit | Candidate content/evidence complete; non-forced publication, remote readback and final exact-head audit required before V04. Main integration unclaimed. |

The extra's unnamed girl is not assigned a later identity. Superd history, Hitogami claims and local cultural generalizations retain their attributed status. No private EPUB, prose, image or paragraph-map payload is included here.


## V04 individually verified witness and derivative — 2026-09-26 UTC

V03's earlier preparation limit is historical: authored `80f2c0758e1fc70164068803fc8e3520bfcd8ca1`, source audit `36222201491`, housekeeping `36222684939`, and final audit `36222895568` all succeeded, ending at `56e1daa4bdc287cb9f2f3e4abbbea30be494628d`. That gate completed before V04 source inspection.

| Field | Verified V04 result |
| --- | --- |
| Witness/family | `MT-LNJP-V04` / `LN_JP_MAIN`; read-only local original, working copy and fresh Drive `11rU7IAAsGUK8MIQ7mCzeM6Lzwmff1unN` identical |
| Identity | `無職転生 ～異世界行ったら本気だす～ 4 (MFブックス)`; 理不尽な孫の手; `ja`; KADOKAWA / メディアファクトリー |
| Bytes | 1,848,117; SHA-256 `d06ed6f483a3f8c4135011789c1e6d36f8e3c7e9cdb6144a7b55db221814f5af`; local 2026-09-25 manifest row agrees |
| Edition | Colophon `text/part0031.html` p3 and p20–23: electronic 2014-08-31/ver.1.0, same-date first-edition/first-printing basis. OPF `2014-09-24T06:00:00+00:00` separate. |
| Container | EPUB mimetype, ZIP CRC, container, manifest and all 35 spine references pass; all body prose in paragraph descendants |
| Narrative | Episodes1–10, Roxy interlude and internal Fitts extra:12 units,12 narrative XHTML items including heading-only;129,847 trimmed ruby-base characters; all53 text chunks actually read |
| Visual/paratext | All16 images individually inspected in order; title/TOC, map, epigraph, author bio, credits, colophon, logo and rights/layout notices inspected; no ordering exception |
| Locator | `mt-lxml-p1`: one-based body-descendant `p` including empties; omit ruby `rt`/`rp`, keep bases/tails, concatenate/edge-trim without Unicode normalization; no printed-page claim |
| Independent check | Second original-XHTML parser verifies all4,694 paragraph positions/lengths/hashes and648 ruby nodes; consequential passages reread in semantic review |
| Private map | `MT-LNJP-V04-locator-map.json`, Drive `11Dyc2EzowOPvxmzq04NKZn60M0O_c2-Y`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`;1,051,680 bytes; SHA-256 `1c065fe28a3f47dd2164a9dbf993dec12643c3dea6aee693e9215f0cf516828c` |
| Retention | Authorized upload `2026-09-26T06:16:38.571Z`; metadata confirms private folder/size, raw downloaded bytes identical |
| Analytical route | [V04 reading](../02%20Sequential%20Readings/MT_V04_DEEP_READING.md),26 observations, synopsis, unchanged pre-inspection recap/freeze; six ledgers and Rudeus/Eris model packages synchronized |
| Publication boundary | Candidate content/evidence closure; containing commit and subsequent final exact-head audit required before V05. Main integration unclaimed. |

Fitts's earlier name, Geese's unnamed former couple, Boreas servants' origins and the ultimate displacement cause are not supplied by foreknowledge. Narrated dream, public alias, reported history and observed action retain separate evidential status. Raw source prose, EPUBs, images and locator-map payloads remain outside Git.


## V05 individually verified witness and derivative — 2026-09-26 UTC

V04's earlier preparation limit is historical: authored/final `f3dfe47b549cf33fddc7d2128e2b6f0bba7a8e8e`, source audit `36225860394`, housekeeping `36226328148` (no changes) and final audit `36226338487` all succeeded. Both audits passed 276 tests; thirteen remote files matched. This gate completed before V05 inspection.

| Field | Verified V05 result |
| --- | --- |
| Witness/family | `MT-LNJP-V05` / `LN_JP_MAIN`; local original, working copy and fresh Drive `16o_T1ZGBhsKkKickK9GVZF5zovncxKEe` identical |
| Identity | `無職転生 ～異世界行ったら本気だす～ 5 (MFブックス)`; 理不尽な孫の手; `ja`; KADOKAWA / メディアファクトリー |
| Bytes | 1,750,510; SHA-256 `9d9e160205eb7a317e499697cfeca98799d4747af254823e6c2bbb00c30a0d41`; 2026-09-25 local manifest row agrees |
| Edition | Colophon `text/part0032.html` p3/p20–23: electronic 2014-10-31/ver.1.0, same-date first-edition/first-printing basis; OPF `2014-11-24T05:00:00+00:00` separate |
| Container | EPUB mimetype, ZIP CRC, container, manifest and all 36 spine references pass; no outside-paragraph body prose |
| Narrative | Seven episodes, two interludes and two extras: 11 units; 13 narrative XHTML items, two heading-only; 126,774 trimmed ruby-base characters; all 53 text chunks actually read |
| Visual/paratext | All 16 images inspected in order; title/TOC, epigraph, profile, credits, colophon, logo and rights/layout notices read; no ordering exception |
| Locator | `mt-lxml-p1`: one-based body-descendant `p` including empty positions; remove ruby `rt`/`rp`, retain bases/tails, concatenate/edge-trim without Unicode normalization; no printed-page assertion |
| Independent check | Second original-XHTML parser checked all 4,679 paragraph positions/lengths/hashes and 608 ruby nodes; targeted consequential rereview recorded with candidate verification |
| Private map | `MT-LNJP-V05-locator-map.json`, Drive `14RaaULS1ApqDHTdPqt4sU4KNfe01CaS3`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`; 1,048,716 bytes; SHA-256 `a36d67ffc0bfa8e54ccee5efde94d55bebef5e5590192c09d09e04498d173a1d` |
| Retention | Authorized upload `2026-09-26T07:28:08.079Z`; metadata confirms private folder/size, raw download identical |
| Analytical route | [V05 reading](../02%20Sequential%20Readings/MT_V05_DEEP_READING.md), 28 observations, synopsis, preserved recap/freeze; six ledgers, five bounded model packages and [V01–V05 checkpoint](../05%20Checkpoint%20Syntheses/MT_V01_V05_CHECKPOINT.md) synchronized |
| Publication limit | Candidate content/evidence closure; containing publication commit and successful exact-head final audit required before V06. Main integration unclaimed. |

V05 reports Sylphie's earlier education, not current whereabouts or Fitts's prior identity. Apparent Ariel death is corrected within this witness; the investigator's inferred disguise mechanism and announced future consequences remain bounded. Rounded ages/time and attributed domestic/rescue histories are preserved as such. No source prose, image, EPUB or locator-map payload is published here.
