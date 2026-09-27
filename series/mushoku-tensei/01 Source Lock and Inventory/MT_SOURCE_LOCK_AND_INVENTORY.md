---
title: "Mushoku Tensei - Source Lock and Inventory"
artifact_id: MT_SOURCE_LOCK_AND_INVENTORY
artifact_type: source_lock
series: "Mushoku Tensei"
generation: "V1"
version: "1.13"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
created: "2026-09-25"
adoption_basis_commit: "a2a1ab9a5ecd0512a5ac460c1b79655af1bca0bd"
source_boundary: "Japanese LN V01–V11 prose/images/paratext inspected; maps retained/verified; V01–V10 published/audited, V11 candidate; V12–V26 not individually admitted."
---

# Source lock and inventory — through V11

This is the analytical source-admission record. The Drive folder `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug` and historical `audit_manifest.json` (Drive ID `1m_fRXGcBbYrPgbdv26DNuOTcUxC9iWGq`) hold the underlying file inventory. The previously inspected Drive-manifest snapshot had internal audit date 2026-09-04; those checks remain historical assertions. The owner-supplied local manifest inspected during this run is dated 2026-09-25; its V02–V11 rows agree with the freshly computed source hash. These are separate inventory observations, not fresh checks of every live file.

## Current folder and admission boundary

The 2026-09-25 live folder listing contained 25 numbered main EPUBs, V01–V11 and V13–V26, and five differently named supplements/bonuses plus the historical manifest. V12 was absent then. No exact duplicate was found by name in that listing; the manifest's archived duplicate belonged to its historical audit count and was not fetched. On 2026-09-26 UTC the restored file was reverified by Drive metadata: `Mushoku Tensei - Volume 12.epub`, ID `1RIKu1ira0Z6yYH2ILkL8BvlNPFSDi615`, 1,542,217 bytes, in the exact source folder. The owner-supplied local directory also lists V01–V26. These observations establish availability, not V12 edition identity, fresh hash/container integrity or narrative admission. The historical manifest's bonus and side-story type labels still require classification; do not treat them as main LN volumes by filename or imported `type` alone.

`LN_JP_MAIN` is the initial source family. V01 identity and text access were established in bootstrap, followed by complete declared narrative and visual inspection and owner content approval. Its required locator map is durably retained and freshly byte-verified; its closure was published and passed the final exact-head audit at `eaf159559c6fc76ddd820178d7588545f08c351d`. V02 is published and audited at final head `687a13ac1a661270ab566c9e1a6028acd607d846`. V03 is published and finally audited at `56e1daa4bdc287cb9f2f3e4abbbea30be494628d`. V04 is published and finally audited at `f3dfe47b549cf33fddc7d2128e2b6f0bba7a8e8e`. V05 is published and finally audited at `3dc6b173b044abdafc013dc989bd96914620d13d`. V06 is published and finally audited at `0e72e531278055c0dbb7a6054285337a1cc37a93`. V07 is published and finally audited at `523625ec4a57b95dec7d5acbb217bae5cc7ba5d3`. V08 is published and finally audited at `210894fd2b5894b7e499bab80251e8f5ea761138`. V09 is published and finally audited at `40018b5caedfba456da199ed2fea613ec991015a`. V10 is published and finally audited at `4823e7f9cecff45d86f3045304b5825c79bcb628`. V11 has fresh local/Drive/manifest byte agreement, verified container/map, complete reading and analytical/evidence candidate. V12–V26 remain availability leads, not individually fresh-hash-verified or narratively admitted. No WN, supplement, adaptation, interview, review, or translation is admitted to the LN prospective reader.

| Witness | Family | Verified identity and access | Integrity and locator check | Narrative inspection | Analytical admission / limit |
| --- | --- | --- | --- | --- | --- |
| `MT-LNJP-V01` | `LN_JP_MAIN` | Drive ID `16ajoVMEswenPuSPmV-lInkYHGNa0XrPc`; internal title `無職転生 ～異世界行ったら本気だす～ 01 (MFブックス)`; creator `理不尽な孫の手`; language `ja`; publisher `KADOKAWA`; file size 2,329,909 bytes; colophon 2014-01-31 / EPUB ver.1.0 | Fresh SHA-256 `b58c6386ffebe5609c51d798ef74e7f5655fcc38910ec7c19bacee11b04651c2` equals historical manifest; ZIP CRC, EPUB container, OPF/spine references verified; 40 spine items | `INSPECTED_V01_PILOT`: 12 prose-bearing narrative spine items containing prologue, eleven episodes and Zenith extra read in order; cover/front and ten narrative plates, five design plates and other paratext classified/inspected | [V01 reading](../02%20Sequential%20Readings/MT_V01_DEEP_READING.md) is owner-approved and its locator map is durably retained/byte-verified. Closure is branch-published and audited at `eaf159559c6fc76ddd820178d7588545f08c351d`. V02 has its separate record below; later units remain unadmitted. |

The V01 container points to `content.opf`, whose title/creator/language metadata agree with the historical manifest. All 40 OPF spine `idref`s resolve in its manifest. A bootstrap-only locator check parsed source item `text/part0008.html` (spine index 9, zero-based), extracted paragraph 3 among parser-selected paragraph/heading elements (105 characters; SHA-256 of the extracted UTF-8 text `52e24a67e98bf91886df770e3385734cc2532dea05ec4bafbd501fea6f0d35a2`), reopened that exact source item and reproduced the same extracted text. No passage content was displayed to the analyst. That earlier HTMLParser was only a diagnostic; the subsequent pilot used a separate `v01-lxml-p1` normalizer and actual source reading. Its locators are one-based `<p>` positions in source XHTML, including empty paragraphs; `<rt>`/`<rp>` ruby annotations are dropped while base text and separators remain. The prose coverage count is 117,875 trimmed, ruby-base Japanese characters across the 12 narrative spine items. The locator contract and selected round-trip checks are in the reading; the raw EPUB and normalized prose are evidence-plane material, not public Git content.

## Distinct verification dimensions

- Live folder presence: V01–V11 and V13–V26 in the prior listing; V12 restored and metadata-reverified on 2026-09-26 UTC. Local filenames V01–V26 are present. Availability is not a current SHA/container check on later volumes.
- Historical manifest: reports 30 primary EPUBs, 31 audited including an archived duplicate, 25 numbered main volumes and file/container checks through its stated audit date. Its taxonomy of several bonuses is not accepted without verification.
- Fresh byte/container check: V01 under the accepted pilot; V02–V11 under the current sequential run as detailed below. On 2026-09-26 UTC the local V01 EPUB also reproduced the locked source hash; the downloaded Drive locator map reproduced its retained size and hash. No repeat narrative reading was performed.
- Narrative coverage and interpretation: V01 (13 units), V02 (12 units), V03 (15 units), V04 (12 units), V05 (11 units), V06 (15 units), V07 (9 units), V08 (13 units), V09 (15 units), V10 (14 units) and V11 (16 units), with six synchronized ledger histories. V01 visual coverage: cover/front and all ten narrative-positioned plates, five design sheets and platform mark inspected. V02 visual coverage: all 16 images, itemized in its reading. V03 visual coverage: all 12 images individually inspected in order. V04 visual coverage: all 16 images individually inspected in order. V05 visual coverage: all 16 images individually inspected in order. V06 visual coverage: all 12 images individually inspected in order. V07 visual coverage: all 19 image occurrences (18 distinct files) individually inspected in order. V08 visual coverage: all 16 image occurrences (15 distinct files) individually inspected in order. V09 visual coverage: all14 occurrences of13 distinct files inspected in order. V10 visual coverage: all14 occurrences of13 distinct files individually inspected in order. V11 visual coverage: all14 occurrences/13 distinct files inspected; image13 one text chunk late as recorded. No claims of full-series visual coverage. Full-series bibliographic/supplemental completeness: not established.

The V01 source inspection and revised analytical content were approved by the owner. Retained derivative: `MT-LNJP-V01-locator-map.json`, Drive file ID `1VE1ti8fs90PHM0Ey4mvT7eQbMjUZm_u9`, retained in source folder `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`; 650,286 bytes; SHA-256 `6c782f0a8f5f30fb8a3c9d67d138185c2adae3e1b8b8d2f947424a16798c0e5c`. The earlier upload rejection was resolved by explicit authorization of that exact V01 file and destination; upload and readback succeeded in the prior session, and this session independently downloaded and hashed the retained bytes again. V01's evidence-retention condition is met. The V01 public closure is published and audited as recorded above; that result does not certify a later volume. Do not copy the EPUB, normalized prose, images or locator map into Git. Required V02–V15 locator-map uploads have separate current owner authorization as recorded in the current map; V12 still requires its individual witness verification. V12 remains unopened pending V11 publication and exact-head audit.

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


## V06 individually verified witness and derivative — 2026-09-26 UTC

V05's earlier preparation limit is historical: authored/final `3dc6b173b044abdafc013dc989bd96914620d13d`, source audit `36229399170`, housekeeping `36229685254` (no changes) and final audit `36229698214` all succeeded. Both audits passed 276 tests; twenty remote files matched. This gate completed before V06 inspection.

| Field | Verified V06 result |
| --- | --- |
| Witness/family | `MT-LNJP-V06` / `LN_JP_MAIN`; local original, working copy and fresh Drive `1CYS3psLrGOxye1yXXIn5h9dZfj5PrmFe` identical |
| Identity | `無職転生 ～異世界行ったら本気だす～ 6 (MFブックス)`; 理不尽な孫の手; `ja`; colophon KADOKAWA / メディアファクトリー / MFブックス; OPF publisher field absent |
| Bytes | 1,389,986; SHA-256 `209fe60c569035b9e786e024f8901fea44bc11a0412ce1f1001b45942a99059b`; 2026-09-25 local manifest row agrees |
| Edition | Colophon `text/part0025.html` p3/p20–23: electronic 2015-02-28/ver.1.0, same-date first-edition/first-printing basis; OPF `2015-03-25T06:00:00+00:00` separate |
| Container | EPUB mimetype, ZIP CRC, container, manifest and all 29 spine references pass; no outside-paragraph body prose |
| Narrative | Thirteen episodes, one interlude and one extra: 15 units; ten narrative XHTML items; 145,767 trimmed ruby-base characters; all 57 text chunks actually read |
| Visual/paratext | All 12 images inspected in order; title/TOC, epigraph, profile, credits, colophon, logo and rights/layout notices read; no afterword, no ordering exception |
| Locator | `mt-lxml-p1`: one-based body-descendant `p` including empty positions; remove ruby `rt`/`rp`, retain bases/tails, concatenate/edge-trim without Unicode normalization; no printed-page assertion |
| Independent check | Second original-XHTML parser checked all 5,020 paragraph positions/lengths/hashes and 636 ruby nodes; targeted consequential rereview recorded with candidate verification |
| Private map | `MT-LNJP-V06-locator-map.json`, Drive `12pNmHq5akEgbs4p04uwwKAdBei231wTA`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`; 1,122,380 bytes; SHA-256 `8fb10df78c8ab7fe2b603c6baf2a01b22653577edc7ca17b7e30c46f7714f632` |
| Retention | Authorized upload `2026-09-26T08:35:41.142Z`; metadata confirms private folder/size, raw download identical |
| Analytical route | [V06 reading](../02%20Sequential%20Readings/MT_V06_DEEP_READING.md), 31 observations, synopsis, preserved recap/freeze; six ledgers, five revised bounded model packages and [disclosure checkpoint](../05%20Checkpoint%20Syntheses/MT_V06_DISCLOSURE_CHECKPOINT.md) synchronized |
| Publication limit | Candidate content/evidence closure; containing publication commit and successful exact-head final audit required before V07. Main integration unclaimed. |

Retrospective interiority is newly available evidence, not a newly occurring past action. Eris's intended partnership and Rudeus's received rejection interpretation remain distinct. Supernatural explanations, search leads, political reports and chronology estimates retain their qualifiers. No source prose, image, EPUB or locator-map payload is published here.


## V07 individually verified witness and derivative — 2026-09-26 UTC

V06's prior preparation limit is historical: authored/final `0e72e531278055c0dbb7a6054285337a1cc37a93`, source audit 36232828869, housekeeping 36233305105 (no change) and final audit 36233317437 all succeeded before V07 freeze and inspection. Prior analytical content is also verified on main as recorded in the current map; this does not certify V07 publication.

| Field | Verified V07 result |
| --- | --- |
| Witness/family | `MT-LNJP-V07` / `LN_JP_MAIN`; local original, working copy and fresh Drive `1O_jNgJHYB0q2LVq6CDMPaQeUXFKRS0sI` byte-identical |
| Identity | `無職転生 ～異世界行ったら本気だす～ 07 (MFブックス)`; 理不尽な孫の手; ja; KADOKAWA |
| Bytes | 2,591,583; SHA-256 `9b242132a32ffe24547569e22bd6bcdca86e175d403d373ebea2d85c261de60f`; local 2026-09-25 manifest agrees |
| Edition | Colophon spine 33 `text/part0032.html` p1–14: 2015-08-31 electronic issue and same-date first-edition/first-printing basis; OPF `2015-09-24T22:00:00+00:00` is distinct metadata |
| Container | EPUB mimetype, ZIP CRC, container/manifest and all 35 spine references checked; no body prose outside paragraph descendants |
| Narrative | Prologue, episodes 1–6, epilogue and internal university extra: 9 units, 11 narrative XHTML items including heading-only; 133,290 trimmed ruby-base characters; actual ordered reading in 53 chunks |
| Visual/paratext | All 19 occurrences of 18 image files inspected in order, including repeated publisher logo, front art, narrative plates, four character sheets and platform mark; title/TOC, profile, credits and colophon read |
| Locator | `mt-lxml-p1`: one-based body-descendant p including empties; drop rt/rp, retain base/tails, concatenate/edge-trim without Unicode normalization; no printed-page claim |
| Independent check | All 4,277 paragraph positions/lengths/hashes and 418 ruby nodes checked against original XHTML with independent parser; semantic source review separate |
| Private retained map | `MT-LNJP-V07-locator-map.json`, Drive `1B5WiKfHXrywIKX_1O332mrhrrwEv4R4W`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`; 959,383 bytes; SHA-256 `26c0f5cba06dc96dbe3829174bc1cad2859d3c2e50760175d99de8aa594ea825` |
| Retention | Authorized upload `2026-09-26T09:46:46.687Z`; metadata private/correct parent/size; raw download matches exact bytes/hash |
| Analytical route | [V07 reading](../02%20Sequential%20Readings/MT_V07_DEEP_READING.md), 30 observations and complete synopsis/coverage; all six ledgers, Rudeus revision, first Sara package and [checkpoint](../05%20Checkpoint%20Syntheses/MT_V07_RECOGNITION_CHECKPOINT.md) |
| Publication limit | Content/evidence candidate; exact-path publication, remote readback, source audit, housekeeping and final exact-head audit required before V08 |

The dragon encounter is hearsay, the mother message remains undelivered, and Fitts's recognition does not resolve prior identity. Sara's corrected motive does not make every imagined event true. Generic web-origin credit does not admit WN comparison. No private source payload appears in Git.


## V08 individually verified witness and derivative — 2026-09-26 UTC

V07's earlier preparation limits are historical: authored/final `523625ec4a57b95dec7d5acbb217bae5cc7ba5d3`, source audit 36270850776, housekeeping 36271366357(no changes) and final audit 36271379146 all succeeded before the immutable V08 freeze and source inspection. V07 main integration remains unestablished; earlier V01–V06 content verification does not certify V07 or V08 integration.

| Field | Verified V08 result |
| --- | --- |
| Witness/family | `MT-LNJP-V08` / `LN_JP_MAIN`; local original, working copy and fresh Drive `1fjytmS18iNQ9ajTqICZIHePoadvhlF02` byte-identical |
| Identity | `無職転生 ～異世界行ったら本気だす～ 8 (MFブックス)`; 理不尽な孫の手; ja; OPF publisher empty, colophon KADOKAWA/MF Books; identifier B016XJT8C2 |
| Bytes | 1,550,790; SHA-256 `b2a831efa2a2b03286bbbbf45029db4947088c1c45223a9f64fccd1be9bafb1d`; September 25 local manifest agrees |
| Edition | Colophon spine 28 `text/part0027.html` p1–14: 2015-10-31 electronic issue and same-date first printing; OPF date `2015-10-31T04:00:00+00:00` separately recorded |
| Container | EPUB mimetype, ZIP CRC, container, manifest and all 30 spine references checked; no body prose outside paragraph descendants |
| Narrative | Prologue, episodes 1–8, two Sylphiette interludes, epilogue and Juliette extra: 13 units; 9 narrative XHTML items including heading-only; 135,176 trimmed ruby-base characters; all 53 ordered chunks actually read |
| Visual/paratext | All 16 occurrences of 15 images individually inspected in order; front art, plates, designs, repeated logo and platform mark; title/contents/fictional epigraph/profile/credits/colophon read |
| Locator | `mt-lxml-p1`, one-based body descendant p including empty; remove rt/rp, preserve ruby bases/tails, concatenate/edge-trim, no Unicode normalization or printed-page claim |
| Independent check | Original-XHTML second parser verifies 4,545 paragraph positions/lengths/hashes and 497 ruby nodes; semantic source review remains separate |
| Retained private map | `MT-LNJP-V08-locator-map.json`, Drive `15NLBBlEYXb1UWgBgDEmgsXyr-GYuCYNr`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`; 1,017,824 bytes; SHA-256 `3081cd3e7efdb39b0774ade48a379f991e10a7db945fb7cac4a7cb276a8de676` |
| Retention | Authorized upload `2026-09-26T21:13:59.357Z`; private status, parent and size checked; fresh raw download byte-identical |
| Reading completion | `2026-09-26T21:20:58.664575+00:00`; complete declared scope, no order exception; extraction not treated as reading |
| Analytical route | [V08 reading](../02%20Sequential%20Readings/MT_V08_DEEP_READING.md), 30 observations; six ledgers, Rudy revision, first Zanoba/Sylphiette packages and [targeted checkpoint](../05%20Checkpoint%20Syntheses/MT_V08_CONSENT_AND_INSTITUTION_CHECKPOINT.md) |
| Publication limit | Content/evidence candidate; remote readback, source audit, housekeeping and final exact-head audit required before V09 |

Fitts/Sylphiette role clues are not a resolved identity map. The three-month epilogue anchor and earlier intervals remain unharmonized. Juli has no interior viewpoint; her visible pride and fear do not establish freely agreed ownership. No source payload is published in Git, and generic web-origin credits do not admit a WN comparison.


## V09 individually verified witness and derivative — 2026-09-26 UTC

V08 authored/final `210894fd2b5894b7e499bab80251e8f5ea761138`, source36274566635, housekeeping36274933387(no changes) and final36274949035 all succeeded before V09 freeze and source inspection. V07/V08 main integration remains unestablished; earlier content verification does not certify later integration.

| Field | Verified V09 result |
| --- | --- |
| Witness/family | `MT-LNJP-V09` / `LN_JP_MAIN`; local original, working copy and fresh Drive `1KLJn7gyLgExGho_5i2jeiycf-_iJgixW` byte-identical |
| Identity | `無職転生 ～異世界行ったら本気だす～ 9 (MFブックス)`; 理不尽な孫の手; ja; OPF publisher empty, colophon KADOKAWA/MF Books; B01AXD9RKM |
| Bytes |1,418,021; SHA-256 `549ac6eb074cca8d9a2d8eff78dd9b1fcfdc4845b24417d0319b26e7b5a0bb4c`; September25 manifest agrees |
| Edition | Colophon spine27 `text/part0026.html` p1–14:2016-01-25 electronic issue,2016-01-31 first-print basis; OPF `2016-01-25T00:00:00-05:00` separately recorded |
| Container | Mimetype, ZIP CRC, container/manifest and all29 spine references checked; no prose outside paragraph descendants |
| Narrative | Eleven episodes, three Sylphiette interludes and extra:15 units;10 narrative XHTML including heading-only;149,815 trimmed ruby-base characters;58 ordered chunks actually read |
| Visual/paratext |14 occurrences/13 distinct files individually inspected; covers/front art/plates/repeated logo/store mark; title/contents/fictional epigraph/profile/credits/colophon; no distinct afterword |
| Locator | `mt-lxml-p1`: one-based body descendant p including empty; remove rt/rp preserving bases/tails, edge-trim, no Unicode normalization or printed-page claim |
| Independent check | Original-XHTML second parser verifies4,985 paragraph positions/lengths/hashes and539 ruby nodes; semantic/source review separate |
| Retained private map | Drive `1aKLjglJL-alQrx9V-0MHO9VyxxY8sYKR`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`;1,114,993 bytes; SHA-256 `30435a447cd0ed77d4ad73cb213ab7d7b6b2ecd003173ec25e795b2619fd43f1` |
| Retention/completion | Upload `2026-09-26T22:13:28.774Z`; private/correct parent and fresh byte-identical readback. Reading complete `2026-09-26T22:27:21.993536+00:00`; no order exception |
| Analytical route | [V09 reading](../02%20Sequential%20Readings/MT_V09_DEEP_READING.md),35 observations; six ledgers, four revisions, two new models and [targeted checkpoint](../05%20Checkpoint%20Syntheses/MT_V09_DISCLOSURE_AND_RECOVERY_CHECKPOINT.md) |
| Publication gate | Candidate requires remote readback/source audit/housekeeping/final exact-head audit before V10 |

Source credit to web origin does not admit WN. Role revelation does not attribute every Fitts occurrence; reported cosmology, curse lead and immediate health outcome retain their separate limits. Source payloads remain private.


## V10 individually verified witness and derivative — 2026-09-26 UTC

V09 authored/final `40018b5caedfba456da199ed2fea613ec991015a`, source36278156334, housekeeping36278653531(no changes) and final36278686182 all succeeded before the V10 freeze and source inspection. The separate automatic final36278669762 also succeeded. V07–V09 main integration remains unestablished.

| Field | Verified V10 result |
| --- | --- |
| Witness/family | `MT-LNJP-V10` / `LN_JP_MAIN`; local original, working copy and fresh Drive `13wT0EKO51PmpMlYhusk3c6Q98E9tTU8N` byte-identical |
| Identity | `無職転生 ～異世界行ったら本気だす～ 10 (MFブックス)`; 理不尽な孫の手; ja; KADOKAWA; identifiers `ca7edcb2-9ced-4f18-ae79-6b67d9551ac5`, `96372dd4-834e-46c0-9716-31655f56c051`, `B01D9FYV70` |
| Bytes |1,499,457; SHA-256 `d6cae30a23a5dc24f57485a5a8bbe6a6954eb85450d3eb6fb97fd7b59fa01419`; September25 manifest agrees |
| Edition | Colophon spine27 `text/part0026.html` p1–15: electronic2016-03-25, first-print basis2016-03-31; OPF `2016-03-25T04:00:00+00:00` separately recorded |
| Container | Mimetype, ZIP CRC, container/manifest and all29 spine references checked; no prose outside paragraph descendants |
| Narrative | Twelve episodes, Eris interlude and internal child-care extra:14 units;10 narrative XHTML items including heading-only;135,183 trimmed ruby-base characters;63 chunks actually read in order |
| Visual/paratext |14 image occurrences/13 distinct files individually inspected in order; front art, narrative plates, logo/store mark; title/contents/fictional epigraph/profile/credits/colophon read; no distinct afterword |
| Locator | `mt-lxml-p1`: one-based body-descendant p including empty positions; remove rt/rp preserving bases/tails, edge-trim without Unicode normalization; no printed-page claim |
| Independent check | Original-XHTML second parser verifies4,887 paragraph positions/lengths/hashes and535 ruby nodes; semantic/source review separate |
| Retained map | `MT-LNJP-V10-locator-map.json`, Drive `1hDPpz_ai0HaggK0ZaSrb7dbKs7GFoeQN`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`;1,093,044 bytes; SHA-256 `5cd0d06e15a06d7b158364a6b17d579c6d8755567e41afbca2c033d56ff6d81b` |
| Retention/completion | Upload `2026-09-26T23:23:48.776Z`; private/correct parent and exact raw readback. Actual reading complete `2026-09-26T23:37:30.605112+00:00`; display truncation sp10p131–138 immediately recovered by rereading p125–142, no skipped source interval |
| Analytical route | [V10 reading](../02%20Sequential%20Readings/MT_V10_DEEP_READING.md),34 observations; six ledgers, nine revised models, new Elinalise package, Rudeus monograph and [cumulative checkpoint](../05%20Checkpoint%20Syntheses/MT_V01_V10_CHECKPOINT.md) |
| Publication gate | Candidate requires remote readback/source audit/housekeeping/final exact-head audit before V11 |

The earlier escort history and explicit future rank statement belong to V10's inspected narrative with their own times. Bottle summoning is not human return; reported artifact history, curse theory and catastrophe explanation retain their limits. Generic web-origin credit admits no WN witness. No private source payload enters Git.


## V11 individually verified witness and derivative — 2026-09-27 UTC

V10 authored/final `4823e7f9cecff45d86f3045304b5825c79bcb628`, source36282513960, housekeeping36282995329(no changes) and final36283008039 all succeeded before V11 freeze/inspection. V07–V10 main integration remains unestablished.

| Field | Verified V11 result |
| --- | --- |
| Witness/family | `MT-LNJP-V11` / `LN_JP_MAIN`; read-only local original, working copy and fresh Drive `184mrGtLmjjzUWZW-DPV1QsAu2RQ41R1t` byte-identical |
| Identity | `無職転生 ～異世界行ったら本気だす～ 11 (MFブックス)`; 理不尽な孫の手; ja; KADOKAWA; identifiers `f9de2248-1b84-402a-8b42-1c5835f3cf1e`, `4c9807eb-f5dd-451a-94de-48771f71b4d4`, `B01FVG07PK` |
| Bytes |1,312,879; SHA-256 `aa3c553fa2119770243a9768ba1f2393ea3d3ce73507d26bb11d90eb7b7b34b9`; September25 manifest agrees |
| Edition | Colophon spine27 `text/part0026.html` p1–15: electronic2016-05-25, first-print basis2016-05-31; OPF `2016-05-25T04:00:00+00:00` distinct |
| Container | Mimetype, ZIP CRC, container/manifest and29 spine references checked; no prose outside paragraph descendants |
| Narrative | Fourteen episodes, doll/master-servant interlude and internal Norn/Millis extra:16 units;10 narrative XHTML items including heading-only;150,978 trimmed ruby-base characters;65 chunks actually read |
| Visual/paratext |14 image occurrences/13 files inspected; title, front art, contents, fictional epigraph, narrative plates, profile/credits/colophon and store mark; no separate afterword |
| Order/coverage exception | Image13 inspected one chunk late after spine14p1–83. Truncated sp14p11–12 recovered immediately throughp1–20. No omitted source interval/image; repeated logo inspected with colophon. |
| Locator | `mt-lxml-p1`: one-based body-descendant p including empties; omit rt/rp retaining base/tails; edge-trim, no Unicode normalization or printed pagination |
| Independent check | Original-XHTML second parser verifies4,377 paragraph positions/lengths/hashes and514 ruby nodes; semantic review separate |
| Retained map | `MT-LNJP-V11-locator-map.json`, Drive `1fJuAgFUN1Tw6o7ombUytxfOrrVFk0Gdq`, parent `1bx_IkoTqVZy9I8SmcyGvgRmj3JX0Rjug`;979,891bytes; SHA-256 `ea0fc6e2741cab4f5fa7c360dd7b3c7467ba6c594cbb255869bb5b9e56200f18` |
| Retention/completion | Upload `2026-09-27T00:47:34.668Z`; private/correct parent, byte-identical readback; actual reading completed `2026-09-27T01:00:20.548330+00:00` |
| Analytical route | [V11 reading](../02%20Sequential%20Readings/MT_V11_DEEP_READING.md),35 observations; six ledgers, six model revisions, first Norn/Aisha pairs and [knowledge/duty checkpoint](../05%20Checkpoint%20Syntheses/MT_V11_KNOWLEDGE_AND_DUTY_CHECKPOINT.md) |
| Publication gate | Candidate requires remote readback/source audit/housekeeping/final exact-head audit before V12 |

Norn's account, Nanahoshi's retained records and later corrections have separate reader/character knowledge times. Rapan arrival is not completed rescue; only this transit pair is tested. Book-origin credit admits no WN witness, and no private source payload enters Git.
