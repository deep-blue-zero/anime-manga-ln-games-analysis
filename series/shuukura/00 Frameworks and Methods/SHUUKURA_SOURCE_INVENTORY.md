---
title: "Shuukura V2 — source inventory and witness architecture"
artifact_id: SHUUKURA_V2_SOURCE_INVENTORY
artifact_type: source_inventory
series: "Shuukura / 週に一度クラスメイトを買う話"
series_id: shuukura
generation: SHUUKURA_V2
version: "1.12"
status: active_provisional
scope: "Exact acquired source identities, edition boundaries, supplemental provenance and future inventory freeze"
source_boundary: "Frozen I1; LN01–09/four BOOKWALKER bonuses/KSS01–05 complete in atomic commits; later supplements/web/V1 unread; V10 excluded"
canonical_home: series/shuukura/00 Frameworks and Methods/SHUUKURA_SOURCE_INVENTORY.md
created: "2026-10-17"
planning_date: "2026-10-16"
review_status: VERIFIED_AVAILABLE_SOURCE_FREEZE_WITH_EXPLICIT_MANDATORY_GAPS
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Source inventory and edition/witness architecture

This is the canonical source-and-coverage home. Snapshot: **2026-10-17 UTC; initial planning date 2026-10-16**. The historical bootstrap tables below distinguish acquisition and structural checks from reading. The later **SHUUKURA-V2-20261017-I1** record at the end of this document is the authorized source freeze. Ordered LN inspection is admitted. The live coverage record below credits LN01–09, BW-JP-V03/BW-JP-V06/BW-JP-V07/BW-JP-V09 and KSS-01/KSS-02/KSS-03/KSS-04/KSS-05 only through their complete introducing atomic commits. Earlier bootstrap/candidate tables remain explicitly historical preparation and do not themselves establish current coverage.

## Evidence plane, access and state vocabulary

Canonical Drive evidence root ID: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`. Shuukura collection ID `1BMN3LgKylCFuCPllNsc9007_urMeHV-4`; Main Series `1rYuTUM_62GhmEEQx6c3xP-NmuxG_OW-m`; Bonus and Extras `1lgaBXAfAtrmWBEuIKF1A4Qa5QYIqqjrg`; BOOK WALKER Short Stories `1-zoOStzwZmB6srNJLT41POns0gTX6XLW`; Kakuyomu commemorative captures `1WzIFGdFsKvkdQGqdYQPAYh_ApHOqymjU`; their final archival derivatives `1DCnPSqXoPSUll0y_cpWh2KoVo4myk3bG`. Resolve files by stable ID through connected Drive, not filename search alone. Public Git routing uses stable IDs rather than private Drive URLs under the publication policy.

All observed folder listings were exhausted. The observed **43 objects** are nine main EPUBs, four bonus EPUBs, seventeen source PDFs, twelve final PDFs and one processing report. They represent nine collected volumes and sixteen separate supplemental story candidates, not 43 distinct stories. Internal novel extras remain parts of their parent volume. No complete web-serial export, V10, voice-drama recording/script or additional retailer asset was found in this enumerated collection. This is not a claim about every file elsewhere in the owner's Drive.

| State | Required evidence | Bootstrap result |
| --- | --- | --- |
| Publisher availability | Dated official catalog/author record | LN1–9 published; LN10 scheduled for October 20; separate web landing metadata observed |
| Drive inventory | Listed stable IDs, parent routes, names and sizes | 43 objects in the enumerated Shuukura collection |
| Verified source bytes | Complete download, independently computed SHA-256 and byte count | All 43 objects verified; size agrees with listing |
| Structural/extraction verification | Container, spine, TOC or PDF integrity and recoverable text | All 13 EPUB ZIP CRCs passed; OPF/spine/nav parsed; all 29 PDFs opened and have extractable text |
| Narrative inspection | Deliberate source-grounded reading with exact locators | None; metadata/TOC, bibliography and deterministic text-equivalence checks only |
| Admitted analytical coverage | Authorized unit transaction and accepted evidence/interpretation | Zero completed; later ordered-admission OPEN state is recorded below |

Primary bytes and deterministic derivatives stay in Drive. Git stores only this metadata, checksums, source locators and interpretations after authorization. Download caches, extraction scripts and temporary HTML are noncanonical and excluded from publication. No copyrighted narrative text, image or media is uploaded into Git. This bootstrap created no new permanent evidence derivative. Existing Drive objects were read without modification; acquisition rights or edition authenticity cannot be inferred from successful download.

## Published Japanese LN primary lane

Preferred witness: the Japanese KADOKAWA / 富士見ファンタジア文庫 novels by 羽田宇佐, illustrated by U35. V01–V04 subtitle: `ふたりの時間、言い訳の五千円`; V05 onward: `ふたりの秘密は一つ屋根の下`. This preference is justified by a complete numbered V01–V09 acquisition candidate, structurally recoverable packages and the separately acknowledged revised/expanded publication witness. It does not claim that all package revisions are retail-original or that the web text is dispensable.

The following ISBNs identify **publisher print catalog editions**, not the digital package UUIDs. Publisher release dates differ from conventional twentieth-day colophon dates in some acquired packages (V04 April 20 versus release April 19, V05 October 20 versus October 19, V08 December 20 versus December 19); keep both fields rather than treating them as a textual revision.

| Volume | Official release date | Print ISBN | Exact catalog | Acquisition / admission |
| --- | --- | --- | --- | --- |
| 01 | 2023-02-17 | 9784040748788 | [Publisher record](https://www.kadokawa.co.jp/product/322210001354/) | Acquired EPUB; hash verified; not narratively admitted |
| 02 | 2023-06-20 | 9784040750286 | [Publisher record](https://www.kadokawa.co.jp/product/322303000713/) | Acquired EPUB; hash verified; not narratively admitted |
| 03 | 2023-12-20 | 9784040751795 | [Publisher record](https://www.kadokawa.co.jp/product/322306000954/) | Acquired EPUB; hash verified; not narratively admitted |
| 04 | 2024-04-19 | 9784040753805 | [Publisher record](https://www.kadokawa.co.jp/product/322311000744/) | Acquired EPUB; hash verified; not narratively admitted |
| 05 | 2024-10-19 | 9784040755274 | [Publisher record](https://www.kadokawa.co.jp/product/322403000456/) | Acquired EPUB; hash verified; not narratively admitted |
| 06 | 2025-02-20 | 9784040757735 | [Publisher record](https://www.kadokawa.co.jp/product/322409001103/) | Acquired EPUB; hash verified; not narratively admitted |
| 07 | 2025-08-20 | 9784040759753 | [Publisher record](https://www.kadokawa.co.jp/product/322502001768/) | Acquired EPUB; hash verified; not narratively admitted |
| 08 | 2025-12-19 | 9784040761701 | [Publisher record](https://www.kadokawa.co.jp/product/322507001178/) | Acquired EPUB; hash verified; not narratively admitted |
| 09 | 2026-05-20 | 9784040763279 | [Publisher record](https://www.kadokawa.co.jp/product/322511000826/) | Acquired EPUB; hash verified; not narratively admitted |
| 10 | 2026-10-20 (scheduled) | 9784040765525 | [Publisher record](https://www.kadokawa.co.jp/product/322605000538/) | Scheduled, not yet published at cutoff; absent from inspected Drive collection |

V10 is not part of the acquired boundary. A preorder or forthcoming product page is not a source acquisition. Recheck the official [series page](https://promo.kadokawa.co.jp/fantasiabunko/special/202302shuichi/) and exact product record at a later authorized source freeze; never infer release from the current date alone.

### Exact acquired package identities and limitations

| Stable source unit | OPF identifier | Declared language | OPF member | Spine items | Image assets |
| --- | --- | --- | --- | --- | --- |
| LN-JP-V01 | `B0BTRWKGJF` | `ja` | `OEBPS/content.opf` | 29 | 21 |
| LN-JP-V02 | `urn:uuid:ce53bc03-016e-4cfe-9b9e-a022e356bb81` | `ja` | `item/standard.opf` | 27 | 19 |
| LN-JP-V03 | `urn:uuid:b7ebf0c5-e95f-4972-9f7d-cdef5d8eac84` | `ja` | `item/standard.opf` | 27 | 21 |
| LN-JP-V04 | `urn:uuid:d1cbd726-53e2-4773-a8db-91116e8f4f31` | `ja` | `item/standard.opf` | 28 | 21 |
| LN-JP-V05 | `urn:uuid:33eb742f-fab6-4f75-ba87-7dd75fd480e3` | `ja` | `item/standard.opf` | 30 | 22 |
| LN-JP-V06 | `04075773A20043700000` | `ja` | `item/standard.opf` | 31 | 20 |
| LN-JP-V07 | `04075975A21973900000` | `zh-CN` | `item/standard.opf` | 28 | 20 |
| LN-JP-V08 | `04076170A23275700000` | `zh-CN` | `item/standard.opf` | 28 | 19 |
| LN-JP-V09 | `urn:uuid:41b49992-da0c-4afc-9ee1-5ede50c0db36` | `ja` | `item/standard.opf` | 28 | 18 |
| BW-JP-V03 | `00034000A07605500000` | `ja` | `item/standard.opf` | 3 | 2 |
| BW-JP-V06 | `syuuniitidokurasumeito006` | `ja` | `item/standard.opf` | 3 | 2 |
| BW-JP-V07 | `syuuniitidokurasumeito007` | `ja` | `item/standard.opf` | 3 | 2 |
| BW-JP-V09 | `syuuniitidokurasumeito009` | `ja` | `item/standard.opf` | 3 | 2 |

These are exact acquired witnesses, bound further by the hashes below. OPF identifiers, retailer-style codes and UUIDs are not purchase receipts or proof of unchanged publisher bytes. V01 is retailer-ID-associated and packaged differently from later volumes. Packaging/normalization metadata in parts of the collection means original retail revision and conversion lineage remain unresolved. File upload/modification time, EPUB `dcterms:modified` and template timestamps do not establish publication dates; one bonus retains a 2018 template date and several share a February 2025 timestamp despite different associated volume releases.

V07 and V08 declare `zh-CN` while TOC labels and a nonsemantic script-count probe contain substantial Japanese kana (78,871 / 96,288 kana respectively). This supports a language-tag anomaly candidate, not a certification of every passage or original Japanese edition fidelity. Preserve the received bytes; verify title/colophon, readable Japanese rendering and provenance at admission. Do not silently repair metadata or substitute a translated witness. All image counts are packaged assets, not certified unique illustrations; covers, frontispieces and utility graphics are included. Visual completeness, legibility, ruby and illustration placement still require authorized source admission/reading.

### Numbered order and internal components

Proposed mainline atomic transactions: `LN-JP-V01` through `LN-JP-V09` in increasing order. Within each, obey the actual EPUB spine and navigation anchors, with chapter/subunit entering freezes. Covers, front matter and illustrations are separately marked visual/paratext evidence; main chapters, interludes and internal bonus fiction are narrative components; afterword/colophon are paratext, not automatic story facts. Read retrospective material when encountered, not at an invented chronological insertion point. Track image-only leaves as well as text spine members.

| Parent unit | Numbered main chapters in TOC | Internal narrative extras and native hrefs (relative to OPF directory) |
| --- | --- | --- |
| LN-JP-V01 | 10 | 幕間　まだ宮城が存在していなかった私のこと — `Text/part0015.xhtml#toc-006`; 番外編　仙台さんはきっと私の名前を知らない — `Text/part0023.xhtml#toc-013` |
| LN-JP-V02 | 10 | 幕間　雨の日の宮城が私にしたこと — `xhtml/p-010.xhtml#toc-008`; 番外編　仙台さんの放課後が五千円札になるまで — `xhtml/p-015.xhtml#toc-013` |
| LN-JP-V03 | 8 | 幕間　宮城がいる部屋 — `xhtml/p-008.xhtml#toc-006`; 番外編　仙台さんには似合わない — `xhtml/p-013.xhtml#toc-011` |
| LN-JP-V04 | 9 | 幕間　宮城は甘くて痛い — `xhtml/p-008.xhtml#toc-006`; 番外編　この部屋に春が来て仙台さんは — `xhtml/p-014.xhtml#toc-012` |
| LN-JP-V05 | 10 | 幕間　宮城に言うおかえり — `xhtml/p-010.xhtml#toc-007`; 番外編　仙台さんに言うおかえり — `xhtml/p-016.xhtml#toc-013` |
| LN-JP-V06 | 11 | 幕間　宇都宮舞香の戸惑い — `xhtml/p-008.xhtml#toc-005`; 番外編　ルームメイトであるべき私たちの朝 — `xhtml/p-017.xhtml#toc-014` |
| LN-JP-V07 | 9 | 幕間　遠い記憶、宮城との約束 — `xhtml/p-007.xhtml#toc-004`; 番外編　遠い記憶、仙台さんがいる今日 — `xhtml/p-015.xhtml#toc-012` |
| LN-JP-V08 | 11 | 番外編　日曜の午後、私たちが会うまでに — `xhtml/p-016.xhtml#toc-013` |
| LN-JP-V09 | 10 | 番外編　在りし日の私たち — `xhtml/p-015.xhtml#toc-012` |

All nine TOCs also identify afterword and colophon. Hrefs are structural locators, not evidence of literary inspection. Exact chapter headings, fragment targets, paragraph normalization and image-to-scene correspondence must be fixed in the future unit manifest. V1's standalone analyses of internal bonuses do not create additional primary texts or justify double counting.

## Supplemental candidates and provenance

### BOOK☆WALKER bonuses

| Unit | Package title metadata | Classification / remaining check |
| --- | --- | --- |
| BW-JP-V03 | 『週に一度クラスメイトを買う話３　～ふたりの時間、言い訳の五千円～』BOOK☆WALKER限定書き下ろしショートストーリー | Supplemental narrative; exact story title and release context pending source admission |
| BW-JP-V06 | 『週に一度クラスメイトを買う話６　～ふたりの秘密は一つ屋根の下～』BOOK☆WALKER限定書き下ろしショートストーリー | Supplemental narrative; exact story title and release context pending source admission |
| BW-JP-V07 | 『週に一度クラスメイトを買う話７　～ふたりの秘密は一つ屋根の下～』BOOK☆WALKER限定書き下ろしショートストーリー | Supplemental narrative; exact story title and release context pending source admission |
| BW-JP-V09 | 『週に一度クラスメイトを買う話９　～ふたりの秘密は一つ屋根の下～』BOOK☆WALKER限定書き下ろしショートストーリー | Supplemental narrative; exact story title and release context pending source admission |

Each has three spine items and two image assets, with Japanese metadata and intact ZIP structure. The sparse navigation does not expose a verified story title. Exact heading, issue/retailer entitlement, author attribution and location in publication context must be verified before admission. Do not fill missing titles from historical interpretations. Only V03, V06, V07 and V09 bonus packages were acquired; absence of other volume packages proves neither that none existed nor that the retailer set is complete.

### Kakuyomu commemorative stories

Stable story IDs below follow associated LN number, then the retained final-filename ordering. Release association and titles are **capture/report metadata**, not independently verified live author publication records. Multipart source order comes from the retained processing report. These are separate supplements, not the full Kakuyomu serialization.

| Story | Retained final title / release association | Source → derivative keys | Final pages |
| --- | --- | --- | --- |
| KSS-01 | LN01 Release SS - 宇都宮舞香は思考する | KSS-01-SRC01, KSS-01-SRC02 → KSS-01-FINAL | 8 |
| KSS-02 | LN02 Release SS - 宇都宮舞香の放課後 | KSS-02-SRC01, KSS-02-SRC02 → KSS-02-FINAL | 9 |
| KSS-03 | LN03 Release SS - 宇都宮舞香は下校する | KSS-03-SRC01 → KSS-03-FINAL | 5 |
| KSS-04 | LN04 Release SS - 宇都宮舞香の懐疑心 | KSS-04-SRC01, KSS-04-SRC02 → KSS-04-FINAL | 9 |
| KSS-05 | LN05 Release SS - ワニの憂鬱 | KSS-05-SRC01 → KSS-05-FINAL | 4 |
| KSS-06 | LN05 Release SS - 黒猫の期待 | KSS-06-SRC01 → KSS-06-FINAL | 5 |
| KSS-07 | LN06 Release SS - 不平と不満と白川亜美 | KSS-07-SRC01, KSS-07-SRC02 → KSS-07-FINAL | 9 |
| KSS-08 | LN07 Release SS - 宇都宮舞香の夏休み | KSS-08-SRC01, KSS-08-SRC02 → KSS-08-FINAL | 9 |
| KSS-09 | LN08 Release SS - カモノハシの苦悩 | KSS-09-SRC01 → KSS-09-FINAL | 5 |
| KSS-10 | LN08 Release SS - ワニの衝撃 | KSS-10-SRC01 → KSS-10-FINAL | 4 |
| KSS-11 | LN09 Release SS - 宇都宮舞香と面白ガール | KSS-11-SRC01 → KSS-11-FINAL | 5 |
| KSS-12 | LN09 Release SS - 小松澪と謎多き女 | KSS-12-SRC01 → KSS-12-FINAL | 5 |

The retained processing report is dated August 6, 2026 (Drive modification August 7). Its input/output hashes match all seventeen source and twelve final PDF bytes. Independently checked: each final page count equals its ordered source parts; extracted page-text sequence is identical; all 77 source pages correspond to 77 final pages. The outputs have different bytes from source PDFs because they were copied/combined and metadata-normalized. The report's additional claims about preserved graphics/no rasterization are provenance assertions; no visual narrative inspection or pixel equivalence certification was performed here.

Some original capture names identify draft-preview pages. That creates a provenance/release-status question: an owner-supplied capture is not automatically a verified public edition. Confirm author attribution, authorized access, exact issue, multipart completeness, public-versus-preview status and revisions before admission. Do not publish private preview URLs or tokens. The report's workstation paths are noncanonical and intentionally omitted.

### Mandatory, optional, inaccessible and excluded responsibilities

| Class | Architectural treatment | Current gap |
| --- | --- | --- |
| Main LN narrative, internal interludes and bonus fiction | Mandatory for the LN unit's complete reading | Narrative/component and visual checks pending |
| Acquired author-written external stories (4 BW, 12 commemorative) | Mandatory for the proposed comprehensive supplemental synthesis after provenance admission | Authorship/release/edition and safe insertion boundary unresolved; unadmitted |
| Other retailer/bookstore/author stories | Inventory responsibility mandatory; any verified distinct original fiction becomes mandatory for an unqualified comprehensive claim, or explicitly inaccessible/deferred | Retailer set and expiration history not exhaustively established |
| Original voice-drama story or script | Separate supplemental witness; original narrative content mandatory for a comprehensive all-original-narrative claim when verified and accessible | No source media/script acquired; V1 contains two analyses only, which are discovery leads |
| Voice performance, reused readings and dramatization changes | Optional performance/adaptation study unless a claim depends on them; no silent assimilation to LN | No listening or transcript verification |
| Afterwords, colophons, author/editorial comments | Bibliographic/provenance evidence mandatory where relevant; interpretive contextual evidence labeled separately | Cannot override what characters know or establish continuity by assertion alone |
| Manga, trailers, advertising, promotional character art | Separate adaptation/promotional identity; excluded from primary LN narrative admission | Optional later remit requires separate authorization |

Official discovery leads include the publisher's series page (manga and promotional/voice material), the [publisher's V04 voice announcement](https://prtimes.jp/main/html/rd/p/000014601.000007006.html), the [author's V07 release/bonus notice](https://kakuyomu.jp/users/hanedausa/news/16818792438020642036), and an [official editorial anniversary short-story notice](https://note.com/fujimi_fantasia/n/n4a0f47f766ff). They establish leads, not possession, exhaustive availability or narrative content. Assess edition and lawful access through normal sources; do not bypass expired campaigns or restrictions. No adaptation or promotion was watched/read as narrative evidence.

## Independently identified web witnesses

| Witness | Stable identity / observed metadata | Acquisition and analytical state |
| --- | --- | --- |
| Kakuyomu | [Work 1177354054894027232](https://kakuyomu.jp/works/1177354054894027232); ongoing; 431 episodes; 1,556,911 characters; latest update shown October 6, 2026 | Landing/TOC metadata inspected; complete episode bytes and per-episode hash/ID manifest not acquired; zero readings |
| Shōsetsuka ni Narō | [N0800GA](https://ncode.syosetu.com/n0800ga/); [work information](https://ncode.syosetu.com/novelview/infotop/ncode/n0800ga/); ongoing label, 290 episodes, 1,052,885 characters; first February 5, 2020, latest May 26, 2023 | Metadata only; complete text/revision history and episode correspondence not acquired; zero readings |

Kakuyomu's work description explicitly identifies revisions and additional material for the published books. This supports keeping witnesses separate; it does not identify all changed passages. Narō identifies the same author and simultaneous Kakuyomu publication, but its older endpoint and ongoing label do not prove either completed narrative status or text identity with the first 290 Kakuyomu episodes. Its promotional title is stale relative to current publisher records. Publisher inventory, web endpoint and work-completion status are separate facts.

### Provisional TOC crosswalk — not passage equivalence

Kakuyomu landing metadata exposes 151 group headings totaling 431 episodes. Matching LN main-chapter titles to group headings gives these **candidate** ranges. Matching counts below count exact title matches, not all chapters or complete textual coverage. Missing matches may reflect title variation, splitting, revision, addition or omission; none is adjudicated yet.

| LN unit | Exact main-title matches | Candidate Kakuyomu ordinal range | Limitation |
| --- | --- | --- | --- |
| V01 | 8 | 1–34 candidate; exact matched groups lie within 4–34 | Opening title variation and incomplete matching |
| V02 | 10 | 35–66 | Title correspondence only |
| V03 | 8 | 67–92 | Title correspondence only |
| V04 | 9 | 93–118 | Title correspondence only |
| V05 | 10 | 119–144 | Title correspondence only |
| V06 | 11 | 145–172 | Title correspondence only |
| V07 | 7 | 173–198 | Several main headings not exact matches |
| V08 | 10 | 199–229 | One main heading not exact match |
| V09 | 10 | 230–257 | Final main heading matches group 255–257 |

V09's final main heading `私とは違う仙台さん` matches Kakuyomu group 255–257; the following group begins at 258. Thus **258–431 (174 episodes)** is a candidate beyond-LN09 continuation interval inferred from TOC alignment. It is not yet verified as wholly uncollected text, a shared continuity, or a spoiler-safe reading start. A future LN10 may change the overlap without changing this dated reconnaissance fact. No equivalent Narō boundary is assigned.

Default responsibility: preserve a complete separate Kakuyomu lane in native episode order until inspected comparison justifies replacing specific overlapping segments with a rigorous crosswalk and selective rereading. Then the lane may combine documented LN overlap with fully read web continuation, with explicit skipped coverage and its justification. A continuation-only lane is currently insufficient because revisions/additions are known to exist but unmeasured. Narō begins with a completeness/revision inventory and systematic correspondence audit; selective rereading is justified only by demonstrated equivalence and coverage. Material independent omissions, revisions or failed equivalence expand it to a complete separate reading lane. These decisions require source evidence after independent LN freezes, not an assumption that versions are interchangeable.

### Edition divergence record schema — empty

| Divergence ID / version | Witness A exact locator / revision | Witness B exact locator / revision | Identical / wording / order / addition / omission / uncertain | Material interpretive or knowledge-state effect | Continuity hypothesis / counterevidence | Independent freeze and comparison authority | Open gap / decision |
| --- | --- | --- | --- | --- | --- | --- | --- |

Textual difference alone never establishes a different continuity. Keep witness-bounded claims and record continuity as an argued hypothesis. Absence from an incomplete extraction is not a verified omission.

## Complete acquired-object hash register

The keys bind the units and source/derivative relations above. Resolve each stable file ID through the governed Drive evidence plane and require this SHA-256 for this snapshot. Drive revision/checksum fields were not exposed reliably by the connected metadata response, so no undocumented Drive revision is asserted. A changed checksum creates a new witness version, never an unnoticed replacement.

| Object key | Drive file ID | Independently verified bytes | SHA-256 |
| --- | --- | --- | --- |
| BW-JP-V03 | `1fby4VCdim7QYgMPeqIrxsMztA8aoVe8z` | 636131 | `418c2c8efc7c4a92d57d3705142b6881aa5122b5edc9a0659d1cc22ebd2c0a10` |
| BW-JP-V06 | `1YPKxevk2nlULpEQBoYYvyzlPgSU7qCUF` | 636614 | `f33b45be05f32d03f0c2c9b91671cd6d75f1505d0ff488689268364a62b74d2d` |
| BW-JP-V07 | `1uczKmuZMDOV7-c5XuKFzhwDbt5PkW0n0` | 1045635 | `1e367715dc5d6c58309452208258ba146cab73e1416ccbf5403ae8f5846e57c6` |
| BW-JP-V09 | `1zijopum5J62bvyK_qg4tKmBqbSsa1ZdR` | 803180 | `300cf4532f744c790b1c5180f290752b36f59e3b5dc6f66629ad95cc58670329` |
| KSS-01-FINAL | `1vfAeEImXd4xiBppuh7dUMYMs94BgN_OC` | 745395 | `e4a98c59e630d8c5a801094efe5bfb33c3e0b06d7bce80020da96367b5930e8d` |
| KSS-01-SRC01 | `1Q07nGgkK6pOvpL-DKTScwqRjGfKs-1jJ` | 358990 | `d21fd43c740bd03c9e7d3227e9bdc2ce502710839044f7f09a257788d1d5605b` |
| KSS-01-SRC02 | `1k7R7hTE_alXHmu1DKsG5ZoQUwDjhyNaq` | 363974 | `14a17b78cee284a9c1b8cf07333d8e29876cef402633c5eef22a7af3ef255a93` |
| KSS-02-FINAL | `18CGDaIMD_Du-4LLH362zGlEMQeuMQByU` | 773422 | `ab4fc7e3968aa1dc5904cb905465104d13b503d4d948189caedadb173ca62103` |
| KSS-02-SRC01 | `1MfefmmwUr_8O8jhThZ0DLdQdR5pZ2p3E` | 357633 | `ab70eeaeeb1f24e614c5ed0fa966408201e738bf8c09d63093a1585bc0757091` |
| KSS-02-SRC02 | `1PY-KYJHkTCStOS9QlhiDEDeqBL1V79ne` | 390445 | `99d74e75dc4cd01bf9639728dd65118b76f3e6842cca9f026e673476b4610162` |
| KSS-03-FINAL | `1-p8aGaFr_wPHILRdhpU4RF_8wdj-N_3T` | 410849 | `abb9988dbea98387d3673d5ffaf1a0b76b6592fbc64c1c4ba49ba60b7606d7a7` |
| KSS-03-SRC01 | `1qFLk-PMPmTtLc9UWzCo58irV9byvENey` | 396696 | `c10d9441578fb069608fb3ec7a698de139caefc4ad06bfde1632938d136a0b41` |
| KSS-04-FINAL | `1_eLyVaWGIM-9k2UtyZoqtJomEfLKZpeb` | 745881 | `19d96fbecbffc9ede8af77bd8063264f1a701c54a25b5f937c07462286c8ad48` |
| KSS-04-SRC01 | `13sdx9LKIooFH8h-AwUKjw5H_nEi8Robr` | 348113 | `06aeb036b138624b3a7e4d61a26ea7f67b49dedf6627a84fce85d7f56bae8b5c` |
| KSS-04-SRC02 | `1qthxLSor3Zh1B5vehQOLPPFbBEB8xasI` | 372377 | `5c739880fb13902ab249284222f1252582ae70ed1f425fa37108c5c622e7b6b0` |
| KSS-05-FINAL | `12qqIxCHOLbneoBCP5YRc4z9ZPkVaZJXo` | 362979 | `22c964736be16b0fe3d1c2ef39a3b27576b45052f562746a9138b553163d1075` |
| KSS-05-SRC01 | `1pP-HLz_1ROGkppbTq1Ctr73dQkp0yGvu` | 351585 | `761c35a35995508951d3e499e4e86885ac538ebb0236f00b616c52ab81a2abbe` |
| KSS-06-FINAL | `1EQEzkTnP7QxEV_NMGRSXD8JrX-D6dPi7` | 383803 | `d17da8ee679446ee3086b30d712c7440abf33ce56b08beb2c258baa1de9188c7` |
| KSS-06-SRC01 | `1fVyfrPS--5Uo5JfNLigSIGvKALr5xtAL` | 369710 | `c16ad0db0af0aad2b569b2e0d0f27b3e655ddcf9b56e460c100cc6b8a425c376` |
| KSS-07-FINAL | `1g9hVjrBoD4tbqyMJtm_HHQXpOcH48_FV` | 755572 | `79238d4ca4a83ba77be91ae89326383a44451c5c87b4f6d9bd040546c5dbfcb2` |
| KSS-07-SRC01 | `1uD5ObOOI0gXv5icmVElUGmpnBhXvaFAT` | 384092 | `22b84b47623edda98e6f0ea97f22a5603cd1250423f3bf226446fc244be09ac2` |
| KSS-07-SRC02 | `1cYXtUXlCwJODC4lEwLzeCsVhC8bY_Nrr` | 346201 | `f425d304fc77c40d907251448763b3fbdea752ea952d0bf1bc75ed6456544370` |
| KSS-08-FINAL | `17MAsvOLNuJk8U_MAtxVNaFQIxTAam9gg` | 766266 | `7052921494133a26f571e71be3d0eb437cdcf885eae6e9097b7cba413eb63f7b` |
| KSS-08-SRC01 | `1ys4NG4U4afR-pK5DpLYm-M8TRAHu4-jR` | 387203 | `12ab455805b0b1a7999089b0f49e0f5d323353f2cafc8374131ceae0293e715c` |
| KSS-08-SRC02 | `1VjMwBxAFWTHhWyMI00P34tZQhcokbZ2Y` | 353831 | `9a0d2586e982ce595654387d62e14e2b6530975dfe0631caf687e6e173378461` |
| KSS-09-FINAL | `1IgqBrXohlONtZOYdwNdxHG5moOxvnNYV` | 390099 | `da903d275d426d35191ce3d4a35ca01273c6dfdba4f2f1353265d579897730bb` |
| KSS-09-SRC01 | `1vUVzSaN9ZeNogcscGo3XZkFQznFoaDo8` | 375868 | `70687abcde90abe155b5442ceef589ca2b276559b661160908642059a06d2757` |
| KSS-10-FINAL | `1eXVd-GPYAlzYaAmvPBSA_oU46EnRAytq` | 370153 | `d3fd484e7f6e5e8c67558944e7fe56589e6b4d0d24c69ba3c708cc18d3a7ea51` |
| KSS-10-SRC01 | `11-KKqSO-ZBm4TjubEDB5X7wDbwjDySKB` | 358759 | `47a0d37f53da3e8c995e10b6f28ddd8644007c51478e77354963990b7a359b49` |
| KSS-11-FINAL | `18a2qSLsX-XuIUBLVfLI0I_yrC_KEajQ7` | 394540 | `64bd1cec6ffa46df8bf1249f21e27385b43efab5df896cfcbc8b024141d96d1a` |
| KSS-11-SRC01 | `19D4NgjQUHTNpyEE5pPN4Fs0pVtXGSzX6` | 380265 | `49862127db1c43c6d0893b46b530e6887bef0d2c713a03980d7ca7c0078962fe` |
| KSS-12-FINAL | `1MwBqMCjTN_oMwirLQeBTqO3-0Y78R8GK` | 404316 | `20a02d043e176bac59e055737f2ca6a2bfdcc91835fbd15abf24f3498cbd88b4` |
| KSS-12-SRC01 | `1Yt7mhw24xuqeZjlMZO5LOp8tJ-bhz6ev` | 390057 | `0bd65edd4040c4703ed0a0c966304d5a3a4fa6ec8c2637d7a6dfab41c82345a2` |
| KSS-PROCESSING-REPORT | `1-m92UUMV_bCwO_p3UBaHQKfQHwYDG_oy` | 15916 | `bd298b535154ea8bd127f2879e51d0aea8eee9f42bc482b5b4f1ff7facecc76a` |
| LN-JP-V01 | `1yeja5_RYIyuk0b292Pf8yujZPHrNhwS2` | 9601679 | `375f9ff926f49c2db7c5cfda9bb4ea027acf3594b265c589c64d15cf3453bd63` |
| LN-JP-V02 | `1ADJHmHeOoqWm28fOwz_RqUzpBpKoEOwG` | 11419120 | `6e2fe3a2905dab5be2d1653b7821a77746b684e1a3cd13e4f5a5e6421719d86e` |
| LN-JP-V03 | `1-riDLu1t1xXnGonE6AYn_kV0AX9wGfhO` | 15283054 | `eba1ad0ba6baabeeb6a4f6c1a3cc80d364099d0a848ff36205ca883b9e2e241d` |
| LN-JP-V04 | `1C2bALN18lmmMNKTfLn01GYHd-IRJE9mF` | 9511489 | `57371b889a0f97f77003fb093857323445e06890b588739761c0d6694912dcea` |
| LN-JP-V05 | `1VITxPosvtVPTUelwqp2fATA9JAb1R5Zp` | 16161211 | `dccc06e60cf26f2a443839a4f1e8ba3ed918808ffd7f649aa4f8a9a5c8ccbdab` |
| LN-JP-V06 | `1MQTM3o3pXqzyigHtT5aSURWTy_dwQ1YF` | 17056253 | `1dd096de172fe0641021274591a29eadda563ded169f6d564cf02b53120fee2a` |
| LN-JP-V07 | `1tSe_PTxTct3pIIHFT_3n3-7cCnP76L_X` | 10844829 | `cb560da567093d94c7016c9b71e765b2ff808a933949c6dbb6e043e57927949b` |
| LN-JP-V08 | `1if9ljcOHNJvaLsmFYhD3_SuFChvTRR6F` | 8308796 | `a8f5a649c0797e71c2481d72123ce1ed64332f61bf39360309d7e57b45805642` |
| LN-JP-V09 | `1RK-HYY-C_iMlH7Tua_p-Pik1GP5XCri_` | 7701730 | `3201ae3ffd1230a526dd5d9a184d4a76ab7aff4a7b244160cbfc886acbb8086a` |

## Future source-freeze and ordered admission procedure

1. Obtain owner bootstrap approval, resolve the routing-control transition, and receive separate explicit sequential authorization with witness lane, start/terminal boundary and permitted supplemental/comparison scope. Documents alone cannot open the lock.
2. Re-enumerate the precise Drive folders and official publication/web endpoints at the authorization date. Preserve this inventory version; record additions/deletions/revisions separately. V10 or new episodes do not silently extend the run.
3. Fix an ordered unit list. Proposed first run is nine main LN volume transactions V01→V09, each in its actual internal spine order. Fix chapter-level freezes and every internal extra/illustration/paratext responsibility. External supplements are a later separately authorized ordered lane, conservatively after the independent V09 freeze, then by associated volume and verified release order; uncertain same-release order uses the stable inventory key and is labeled administrative, not narrative chronology. Web comparison/continuation follows relevant independent freezes in separate sessions.
4. Bind every source to Drive ID, byte count, SHA-256, exact edition/package identity and language; resolve V07/V08 language/provenance anomalies and all source access limits before admitting those units. Confirm edition-specific component completeness. Retain authorized deterministic extraction/locator manifests in Drive with tool/version/configuration and source hashes; Git stores the routing/provenance record, never the narrative dump.
5. Build complete native locators: EPUB OPF/spine/member/fragment plus reproducible paragraph ordinal; PDF file/page/part ordering; web work/episode IDs, publication/revision timestamps and snapshot hashes. Do not use the provisional ordinal crosswalk as a substitute for stable web episode IDs. Record missing/illegible components and mandatory-supplement obligations.
6. Record the frozen source-set ID/version, ordered-list hash, evidence-plane manifest route, complete admitted/excluded/deferred boundary, entering knowledge-state IDs, execution mode, atomic unit, terminal condition and quarter milestones in the authorized run declaration/current state. Preserve prior inventories. On every resume compare source hashes and repository state before reading.
7. If bytes, publication boundary or required capabilities change mid-run, stop before the affected unit, preserve the last endpoint and seek a bounded revised admission. Never count a failed or partial unit as completed. A new edition or later release is a new authorization decision, not automatic continuation.

## Coverage projection schema — empty

| Unit / witness version / frozen ordinal | Acquisition and hash state | Admission decision / provenance limits | Inspected components and exact endpoint | Deferred / excluded / inaccessible components | Reading artifact / entering freeze / endpoint freeze | Completion and audit state |
| --- | --- | --- | --- | --- | --- | --- |

Revision 0.1: metadata-only inventory, hashes and provisional edition architecture. All narrative coverage remains zero.

## Continuous-execution kickoff: identity recovery without admission

The owner's subsequent instruction authorizes `continuous_sequential` through every eligible source in the verified kickoff inventory across the admitted lanes, followed by all required analytical outputs. It does not waive the source checks above. This section preserves the new reconnaissance separately from the bootstrap snapshot. **No run inventory is yet finalized or admitted; all narrative coverage remains zero.**

The supporting [candidate identity snapshot](SHUUKURA_V2_KICKOFF_CANDIDATES.json) binds the re-enumerated acquired objects, complete ordered Kakuyomu identity list and subsequent preparation objects. It is an inventory component, not another current-state surface. Snapshot SHA-256: `1b94205f9701fa30ffa096564cd964921c1aaa9eecf6f900298aeeeb6f12f01c`. Its bootstrap expected hashes are explicitly distinguished from newly reverified bytes.

| Responsibility | Kickoff verification on October 17, 2026 UTC | Admission / remaining requirement |
| --- | --- | --- |
| Acquired collection | All six identified folder listings exhausted again; 43 original objects, with exactly the same stable IDs and byte sizes as the bootstrap register | V01/V07/V08 subsequently redownloaded and rehashed; the other 40 original objects were not redownloaded in this recovery pass. Two new preparation objects below are counted separately |
| LN-JP-V01 | Complete download, 9,601,679 bytes, SHA-256 `375f9ff926f49c2db7c5cfda9bb4ea027acf3594b265c589c64d15cf3453bd63`; ZIP CRC passes; OPF `B0BTRWKGJF`, `ja`, 29 spine items | No narrative reading. OPF records `UnpackKindleS ver.20220126`; original-to-extracted fidelity/lineage remains unestablished |
| V01 bibliographic identity | Colophon `OEBPS/Text/part0025.xhtml`: KADOKAWA / 富士見ファンタジア文庫, electronic issue February 17, 2023, `ver.002`; print basis February 20, 2023 | Confirms the received witness's bibliographic assertion, not a full source-equivalence certificate |
| LN10 | [Exact publisher record](https://www.kadokawa.co.jp/product/322605000538/) still gives October 20, 2026 and ISBN 9784040765525; no acquired object in the enumerated main-series folder | Future release excluded; a later publication does not automatically join this execution |
| Kakuyomu | Work `1177354054894027232`: RUNNING, 431 episodes, 1,556,911 characters. All 431 ordered IDs recovered from the native structured TOC; all 431 complete episode HTML snapshots and 88,232 paragraph locators subsequently captured and verified | Native source bytes acquired; no analyst narrative reading, equivalence judgment or source admission. Exact retained snapshot hashes identify the witness; publisher revision timestamps are not asserted |
| Narō mainline | Browser metadata still reports N0800GA, 290 episodes, last publication May 26, 2023; direct runtime metadata request returned HTTP 403 | Browser metadata access is not complete-source acquisition; correspondence/revision work remains required |
| Narō supplemental discovery | Author-linked collection [N7483HS, 彼女たちが知らない秘密のお話](https://ncode.syosetu.com/n7483hs/) exposes seven entries and identifies the main work and simultaneous Kakuyomu publication | Discovery lead only. Browser views are cached; fresh exact source identities, edition correspondence, duplication and spoiler-safe placement must be checked before admission. Do not count seven new distinct stories yet |
| Voice drama / other retailer originals | No new audio/script or retailer asset in the re-enumerated collection | The architecture's completeness responsibility and existing gaps remain open |

Kakuyomu candidate boundary: `KAK-JP-E0001` / episode `1177354054894027298` through `KAK-JP-E0431` / episode `11054822663977570070`. The ordered UTF-8 identity list uses `<unit_id>`, TAB, `<episode_id>`, LF; SHA-256 `f412a6bbeae58e78c31e684ac6c8c6af4508700bc5e08da1477350c08f1d34e9`. The retrieved work-landing bytes hash to `00a48dd3c076e3d9d0f3c9ef459b00384e1084c59a9430f5945dd7fe0d1e766f`. The native last-publication timestamp is `2026-10-05T19:10:31Z`, October 6 in Japan. These metadata identities do not claim that episodes were read or that a live body cannot later change.

The candidate set contains nine LN volume identities and sixteen acquired external-story identities, alongside the 431 Kakuyomu IDs. Internal LN extras remain within their parent volumes. Narō correspondence, the newly discovered supplemental collection and other mandatory supplements remain inventory obligations, not silent exclusions. The ordered acquired-supplement array is administrative; verified release order and final narrative placement are pending. There is no truthful full-run unit denominator or quarter milestone until these obligations and exact admission decisions are reconciled.

Before opening the first reading: recover the execution authorization from the receipt; resolve source fidelity/edition/component requirements, V07/V08 anomalies and supplemental provenance; acquire persistent complete locator/revision manifests; reconcile the supplemental discovery; then finalize the exact admitted, inaccessible and excluded boundary. Missing mandatory sources retain specific blockers. No source check is weakened to manufacture an OPEN lock. Revision 0.2 adds source preparation without narrative analysis.

### Completed source preparation within the blocked kickoff

These are new evidence-plane preparation objects, not additions to narrative scope or analytical high-water marks:

| Object | Stable Drive ID | Bytes / SHA-256 | Content and verified limits |
| --- | --- | --- | --- |
| V01 native locator candidate | `10uryej2sXfJem9tBqWjCaqORYk56LGOs` | 703,536 / `d7dab9d78d24a73659c94d8ccfa9b268c97e6940b84353c50574a54ef5543894` | 29 spine members, 3,784 paragraph anchors and 21 image-asset hashes. Full Drive download/readback hash verified. No narrative text in this locator object; no image inspection or source-fidelity admission |
| Kakuyomu 431-episode source/locator snapshot | `1Cm83bkfawOMdQWou1HCrk4BI-AAsPPvT` | 12,057,474 / `46fefa044e34596948548a49693c6a9b2b937b7f5b82cb61cc89e20a35b427b3` | Complete native HTML, native paragraph IDs/offsets/hashes, ordered identity manifest, landing snapshot, capture/QA scripts and QA record. Full Drive readback, ZIP CRC and manifest/count checks verified. Source archive stays outside Git; no narrative analyst inspection |

Kakuyomu archive member `manifest.json` has SHA-256 `c119aad7ac1dbbf820b21680ea2d28db954c17497b1b324b2a08dc1c5bd5ece2`; the ordered `<unit_id>`, TAB, `<episode_id>`, TAB, `<body_html_sha256>`, LF list hashes to `e9f8f07abb0e2a517901348822e635dabe805fea3c4f52ee4e2bd3ebc1fe5b02`. Every one of the 431 native canonical/OG URLs matches its expected identity; all complete-HTML hashes and 88,232 paragraph-fragment hashes were checked. A bounded markup probe found no body-image flags; this is not visual inspection. Capture-record times are not publisher revision times. The first episode reuses a same-day acquisition probe; its original snapshot-write time and the timing limitation are retained in `capture_qa.json`.

V07 and V08 were also independently rehashed against the existing register and passed ZIP CRC. Their native colophons `item/xhtml/p-colophon.xhtml` assert electronic `ver.001`, with issue dates August 20, 2025 and December 19, 2025 respectively; V08's print basis is December 20. Both assert Japanese text only, while received OPF `dc:language` remains `zh-CN`. A full-spine XML-text probe including ruby/paratext counted 79,503 / 97,009 kana and 3,793 / 4,857 paragraph elements. Those counts use a different scope from the bootstrap probe and are not narrative reading or full fidelity certification. Received bytes and language tags remain unchanged. Original conversion history remains unverified; the later admission disposition below distinguishes that limitation from an unresolved bibliographic identity.


## Authorized execution freeze I1 and admission disposition

**Frozen 2026-10-17T04:34:25Z.** The owner has authorized this continuous run and all later architectural deliverables. The [exact execution inventory](SHUUKURA_V2_EXECUTION_INVENTORY_20261017.json) is a component of this source inventory, not a second current entrypoint. Its SHA-256 is `6e78ec763843f0617a178ac8a8696e799cf2654b55a28d4011595459fe47c42b`; ordered available-unit identity digest `2e62f9bd57dd8f65a036d689917df36847affd7fc1d1f6a70dd85f6121da6b95`.

The fixed available set is **9 LN volumes, 18 external supplemental units and all 431 Kakuyomu episodes: 458 units**. The supplemental set comprises the previous four BW and twelve commemorative identities plus two independently acquired publisher SS pages. LN internal fiction stays within its volume. The JSON separately freezes **51 unavailable source identities**, the 290 Narō correspondence routes and **27 finite author-notice discovery obligations**. These are mandatory completion debts, not optional exclusions or additional completed stories. Several metadata-only identities still require title/deduplication verification. Discovery records can overlap source identities; never sum them as distinct stories. Unknown V01 retailer completeness and source entitlements remain within the discovery debt. This execution can advance through independent available units; it cannot claim comprehensive completion while the mandatory gaps remain.

Order: LN01–09 in spine order; the sixteen acquired supplemental identities by associated volume and stable key, then publisher SS01/02; the full Kakuyomu E0001–E0431 lane. Unavailable Narō supplemental content stays after the independent LN/web freezes; mainline Narō receives all 290 correspondence checks, with source reading where differences require. This order avoids importing later supplements into early LN readings. The source JSON preserves exact IDs, bytes, hashes, component/locator routes, placement, exclusions and blocked dependencies. No later release is silently admitted.

### Acquired LN identity is sufficient for witness-bounded reading

The previous hold conflated unknown retail conversion history with an unresolved bibliographic identity. The method requires a verified source identity, hash, allowed scope and complete locators; it does not require a purchase receipt or proof of retail-binary equality. All nine complete downloads now match the register; ZIP CRCs, all OPF/spine references and local linked resources pass; every text member parses with zero replacement characters. Native Japanese colophons name the work, author, publisher, issue date and electronic version. Their print bases agree with the publisher catalog, retaining the known release/colophon day differences.

Admit the **exact acquired digital witnesses `ACQUIRED-20261017-A1`** for ordered Japanese reading. Do not claim original retail-byte identity or undocumented conversion steps. V01's UnpackKindleS metadata remains recorded. V07/V08's unchanged `zh-CN` tags conflict with Japanese titles/colophons and 78,871/96,288 kana in spine body text; classify the tag as a package anomaly, with semantic Japanese/ruby/rendering confirmation at their actual reading boundary. No future narrative passage was read for this check. A substantive translation, missing content, unreadable component or conflicting edition identification still stops the affected unit. A decoded package is not a completed reading or a universal fidelity certificate.

| Unit | Colophon electronic version | Spine / paragraph / image counts | Locator member SHA-256 |
| --- | --- | --- | --- |
| LN-JP-V01 | 002 | 29 / 3784 / 21 | `f5028d390cdbf9a5d700bbca91d176f312ae0a48cbb6c5f9de75fc65aa68f00f` |
| LN-JP-V02 | 002 | 27 / 4036 / 19 | `f6ab1c514c0dc9ba59fb31c5a08e8e20ef0497d3d6d37ab89bf8c652f862c19c` |
| LN-JP-V03 | 002 | 27 / 3401 / 21 | `0c47c6d83b20b6649a6b80c259f30863bdc80346c703d965175644aeedddac0b` |
| LN-JP-V04 | 001 | 28 / 3908 / 21 | `b17ea7993bb9f3a2f252d344e50cad6937f6560390589b296707c102c09dbdc2` |
| LN-JP-V05 | 002 | 30 / 3895 / 22 | `ff4600a74fa3e9aa855562589d99d174de00ad619a87f3bec25932c624506cec` |
| LN-JP-V06 | 001 | 31 / 3857 / 20 | `94329098a1aeaba22d89c84ffa8237ac3b9cad4b1032fb322eb088e9f33189f9` |
| LN-JP-V07 | 001 | 28 / 3793 / 20 | `6d98463801c014779c0ff9a14948b4f63fee0db24478b4a98935d1023239f9b2` |
| LN-JP-V08 | 001 | 28 / 4857 / 19 | `cb391565c853ec1c65ae4f733bf281d2570e4aaaadea4beb4e659b6b1f8b9980` |
| LN-JP-V09 | 001 | 28 / 3949 / 18 | `e3355f5468a51f857a0a3e5cf22658fe5ca8313bda17c4e1c21d2cc94f2496fe` |

All nine complete native locator manifests and bibliographic checks are retained in Drive admission package `1pi7_hhGoTqMsyEfrju4c-mRFipt41_Ju`, **2,774,617 bytes**, SHA-256 `4cd8450e9627a1d46f5114d009a65b9f7ba3f2847a9f0f455245ba86e430ec3c`. Complete download/readback, all 57 member identities/hashes and ZIP CRC were verified. Member `<unit>_locator_manifest.json` records OPF/spine/member/paragraph anchors, ElementTree serialization hashes, Python version, exact source hash and image hashes. It supersedes the earlier V01 locator candidate for this run without deleting it. Native source paragraphs remain in the original EPUB; the locator contains no narrative text.

### Supplemental provenance resolved in part

The author's [public release notice](https://kakuyomu.jp/users/hanedausa/news/2912051600889515973) explicitly links all seventeen parts of the twelve commemorative stories. Each complete linked native HTML source was captured, identified by title and hashed without analyst narrative reading; 17 native part/paragraph maps are retained in `KSS_NATIVE_SOURCE_AND_LOCATOR_MANIFEST_PRIVATE.json` inside the admission package. A platform page called “draft preview” can be author-released; the earlier filename concern is therefore resolved as an access/publication-provenance question. The historical PDF captures remain distinct witnesses: full textual/rendering correspondence still requires checking before any edition-equivalence claim. Preview-link tokens stay in the evidence plane; public Git cites the author's notice and source hashes.

Two accessible official publisher stories were acquired completely as HTML plus the linked narrative PNG, without reading the image content:

| Unit | Publisher heading | Native image SHA-256 | Reading placement |
| --- | --- | --- | --- |
| OFF-JP-SS01 | 宮城は知らない入れ物のこと | `287a746a3aa3545e5a03834d86843f44f70e410c25700e5c8593f54bb6833457` | After independent LN09; direct image inspection |
| OFF-JP-SS02 | 仙台さんは知らない私の記憶 | `0aee84bd87a603ed0019b9efae9a08ced5338610d5eb717a2fd6c785da7156a5` | After independent LN09; direct image inspection |

Their native URLs, HTML hashes and image member names are in I1 and `official_SS_manifest.json` in the package. Do not presume these stories are distinct from every retailer witness until the duplication check. The four BW packages retain unit-level original-text/heading checks before their later admission. Author notices now identify many missing retailer originals; specific source IDs/titles and author-specified V09 paired-story order are retained in I1. An announced merchandise item is not itself an original story. The two V04 voice stories are identified as `VOICE-JP-V04-01/02`; complete original narrative/script access remains unverified, and a limited preview cannot satisfy it.

### Publication and remaining coverage

Available-set quarter boundaries are unit ordinals **115, 229, 344, 458**; lane-specific boundaries are LN **3/5/7/9**, Kakuyomu **108/216/324/431**, supplements **5/9/14/18**. Publish completed units more frequently. Percentages name their lane/set and never imply all-source or synthesis completion. An unresolved mandatory gap prevents the corresponding 100%/completed claim even after all available units are read.

LN10 and its bonuses remain future releases (October 20, 2026). The announced Birthday SS goods ship December 2026–January 2027 and are also future-source obligations outside I1. Kakuyomu stops at immutable episode `11054822663977570070`, E0431. Later sources require a separate extension.

Revision 0.4: source-admission correction and durable I1 freeze. Source reading coverage and all committed narrative high-water marks remain zero/NONE at this administrative boundary.

## Live sequential coverage — completed LN transactions

Transaction `SHUUKURA-TX-LN-JP-V01-20261017-A1` introduces the [frozen V01 deep reading](../02%20Sequential%20Readings/SHUUKURA_V2_LN_V01_DEEP_READING.md), all four reconciled ledger deltas, entering/exit states and the [source/semantic transaction audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_LN_V01_TRANSACTION_AUDIT.md). This coverage becomes committed high-water **LN-JP-V01** only in the complete introducing commit; source inspection or this draft table alone does not advance it. Recovery resolves that commit from this stable transaction identity and verifies its actual tree/audits. V01 committed as `f632bb9ee97e2af87c0388fb19d8bfea7268688c` and merged/audited through PR197. The subsequent complete V02 transaction `SHUUKURA-TX-LN-JP-V02-20261017-A1` adds its [frozen reading](../02%20Sequential%20Readings/SHUUKURA_V2_LN_V02_DEEP_READING.md), four reconciled instruments and [unit audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_LN_V02_TRANSACTION_AUDIT.md); committed high-water advances to V02 only in that complete introducing commit.

| Lane | Complete atomic units / frozen available units | Committed high-water after this transaction | Next source operation / remaining mandatory work |
| --- | --- | --- | --- |
| Japanese LN | 9 / 9 | LN-JP-V09 | LN100% CLOSED_ON_GREEN_MAIN/PR207; V10 excluded |
| External supplements | 9 / 18 | KSS-05 | Whole introducing commit required; required halfway publication, nextKSS-06 exact nativepart10 admission. PriorKSS04 CLOSED_ON_GREEN_MAIN/PR214 |
| Kakuyomu | 0 / 431 | NONE | E0001–E0431 after independent LN/supplement freezes; capture is not reading |
| Narō correspondence / supplemental gaps | 0 / 290 correspondence checks; no acquired gap completed | NONE | Exact source/correspondence and 27-record discovery audit remain unperformed; 51 unavailable identities not waived |

Available-set completion is **18/458**, not program completion; LN100% publicly closed via V09sourcef05e5ffbc52b2b24911e1b700df3a7845f665958/PR207/main108300099ba20305091a1050fcde33f203afb671/fulltreee4f247a787ca15f5bb5519e7cb6db2cdda06e0ca/source39049020760/house39049396593NO_OP/final39049426359/night39050040125/explicitowner main39050124564 allSUCCESS/full352tests. ExternalSS9/18 onlywholeKSS05commit; firstSSquarter5/18wholeKSS01source28f178a2 CLOSED_ON_GREEN_MAIN/PR210/main98ffb5d8, all required audits verified; overall115/458unreached. I1 exact membership/digests/51missing/27discovery/290Narōduties unchanged; later releases excluded. BW03sourcea41c6821da4a7c82154712f4d9f4914ad9fa2272/source39052329180/house39052565861/finalactual-source39052600867 allSUCCESS/352tests/trustedstatus; owner-onlynightly39053129915 completedSUCCESS/VERIFIED_OWNER_ONLY/merged_verified/PR208/main159644848f216c208367ecf5de822ec969debfbb/equalfulltree1798d7383495ab3febbc59cd23b0d09367c34d62/mandatoryownerexplicitmain39053218687SUCCESS(actual159644848/full352tests/trustedstatus). BW03 CLOSED_ON_GREEN_MAIN. BW06sourceb08d809faecd10884020d902b79fc0e200f35df8/PR209/main23064c95c652cafefea486e30d806ba858d0e1a9/equalfulltree041b726eb6aaae9ad5a41ea713444e618f48a885/source39054161159/house39054468152/finalactual-source39054497188/night39055177051/mandatoryownerexplicitmain39055268435 allSUCCESS/full352tests/trustedstatus/VERIFIED_OWNER_ONLY/merged_verified. BW06 CLOSED_ON_GREEN_MAIN; no later release admitted. BW07localwholecommitf62f8457d29694b815973f712a2d44dad7a3e392/treeea2d7eb0e155fd9aa8e6b94ff49b51bad86c7690/authorpreflight8071PASS; coherent BW07/BW09/KSS01tranche published and CLOSED_ON_GREEN_MAIN/PR210 atSS5/18. Local durability remains distinct from the verified public audit/integration receipt. BW09wholelocal386201e31b63cfafad3c6bd53fe03c2af7bac73a/tree7353693df604a7660f73cd2acfd85dbeffdcfc9c/preflight8091PASS; still unpublished at KSS01entry. Firstquartercoherenttranche requires actual new audit/integration, no older status substitution. KSS02 CLOSED_ON_GREEN_MAIN/PR212: sourceda0ed6b45dfe429a12505cc5a0f11bb31171e007/maind1021d6d8e5e9551d4ef518f9a5bff6e3bf79b27/equalfulltree4cc841e7f336581c8a94178718908fcfd87f4a50; source39064502111/house39064890893NO_OP/finalactualsource39064923640/owner-nightly39065572812/mandatory ownerexplicitmain39065669252 allSUCCESS/full352tests/trustedstatus/VERIFIED_OWNER_ONLY/merged_verified. Successful pushmain39065651442did not substitute for the mandatory dispatch. KSS03 CLOSED_ON_GREEN_MAIN/PR213: sourcee3603f3a7a818f4ae4313fe42acfb0df844d6192/main6197361b2d88a30f7cd9ce9bfab13b5f1827d802/equalfulltree9a4fb8096595c7c7662ad7bc9561d2987d80d3d6; source39067311514/house39067607805NO_OP/finalactualsource39067637207/owner-nightly39068170249/mandatory ownerexplicitmain39068262873 allSUCCESS/full352tests/trustedstatus/VERIFIED_OWNER_ONLY/merged_verified. Successful pushmain39068246067 did not substitute for the mandatory dispatch. KSS04 CLOSED_ON_GREEN_MAIN/PR214:source9e81ac8834b1f43eb6ca1c205c1dc9f4ff278217/maincce4eb7cb02867112afbe1b40fd17c074a666df2/equalfulltree421b0ee8879122f9719f0691723efb1a76616fe9;source39069161640/house39069396732NO_OP/finalactualsource39069422346/owner-nightly39069838269/mandatory ownerexplicitmain39069935058 allSUCCESS/full352tests/trustedstatus/VERIFIED_OWNER_ONLY/merged_verified. Successful pushmain39069912902 did not substitute for the mandatory dispatch.

### V01 actual component inspection

All rows bind the original source/locator hashes in the admission table. Counts include blank/structural native paragraphs; ordinal ranges are member-local, not display or print pages. Japanese text was deliberately read and each image actually viewed. The full-spine verification additionally found no substantive body text outside the paragraph/inspected-image flow; all581 ruby elements remain in the original/hash mapping. Base-text reading does not claim vocal performance. Historical bootstrap rows marked not read remain historical, superseded operationally only by this live coverage.

| Spine | Native member under OEBPS/ | Paragraph coverage | Directly inspected image assets under Images/ | Inspection / limitation |
| --- | --- | --- | --- | --- |
| 1 | `Text/cover.xhtml` | 0; image-only leaf | `embed0020_HD.jpg` | Complete |
| 2 | `Text/part0000.xhtml` | 0; image-only leaf | `embed0000_HD.jpg` | Complete |
| 3 | `Text/part0001.xhtml` | 0; image-only leaf | `embed0001_HD.jpg` | Complete |
| 4 | `Text/part0002.xhtml` | 0; image-only leaf | `embed0002_HD.jpg` | Complete |
| 5 | `Text/part0003.xhtml` | 0; image-only leaf | `embed0003_HD.jpg` | Complete |
| 6 | `Text/part0004.xhtml` | 0; image-only leaf | `embed0004_HD.jpg` | Complete |
| 7 | `Text/part0005.xhtml` | 1–4 | — | Complete |
| 8 | `Text/part0006.xhtml` | 1–16 | — | Complete |
| 9 | `Text/part0007.xhtml` | 1–4 | — | Complete |
| 10 | `Text/part0008.xhtml` | 0; image-only leaf | `embed0005_HD.jpg` | Complete |
| 11 | `Text/part0009.xhtml` | 1–218 | — | Complete |
| 12 | `Text/part0010.xhtml` | 0; image-only leaf | `embed0007_HD.jpg` | Complete |
| 13 | `Text/part0011.xhtml` | 1–367 | `embed0006_HD.jpg` | Complete |
| 14 | `Text/part0012.xhtml` | 1–403 | `embed0008_HD.jpg` | Complete |
| 15 | `Text/part0013.xhtml` | 1–429 | `embed0009_HD.jpg`, `embed0010_HD.jpg` | Complete; p130–154 recovered after image155/p156–321, no blind cooking test |
| 16 | `Text/part0014.xhtml` | 1–312 | `embed0011_HD.jpg` | Complete |
| 17 | `Text/part0015.xhtml` | 1–83 | — | Complete |
| 18 | `Text/part0016.xhtml` | 0; image-only leaf | `embed0012_HD.jpg` | Complete |
| 19 | `Text/part0017.xhtml` | 1–321 | `embed0013_HD.jpg` | Complete |
| 20 | `Text/part0018.xhtml` | 1–399 | `embed0014_HD.jpg` | Complete |
| 21 | `Text/part0019.xhtml` | 1–425 | — | Complete |
| 22 | `Text/part0020.xhtml` | 1–265 | `embed0015_HD.jpg` | Complete |
| 23 | `Text/part0021.xhtml` | 1–379 | `embed0016_HD.jpg` | Complete |
| 24 | `Text/part0022.xhtml` | 1–21 | — | Complete |
| 25 | `Text/part0023.xhtml` | 1–117 | `embed0017_HD.jpg` | Complete |
| 26 | `Text/part0024.xhtml` | 0; image-only leaf | `embed0018_HD.jpg` | Complete |
| 27 | `Text/part0025.xhtml` | 1–18 | — | Complete |
| 28 | `Text/part0026.xhtml` | 1–3 | — | Complete |
| 29 | `Text/part0027.xhtml` | 0; image-only leaf | `embed0019_HD.jpg` | Complete |

Totals: **29 spine members, 3,784 native paragraph anchors, 21 original image references**. Original bytes, all member/paragraph serialization hashes and image hashes reverify. The chapter4 local presentation-order exception is preserved in the reading, not concealed by the completeness total. All no-change source lanes and known gaps remain explicit. Source inspection is complete for the exact acquired witness; retail conversion lineage and cross-edition agreement are not thereby certified.

Revision0.5: V01 narrative/paratext inspection and atomic coverage only. Frozen I1 bytes and source-set membership are unchanged; no web/supplement completion, V1 comparison, mature monograph or model-validation claim is introduced.


### V02 actual component inspection

All rows bind LN-JP-V02 / ACQUIRED-20261017-A1, original SHA-256 `6e2fe3a2905dab5be2d1653b7821a77746b684e1a3cd13e4f5a5e6421719d86e` and locator SHA-256 `f6ab1c514c0dc9ba59fb31c5a08e8e20ef0497d3d6d37ab89bf8c652f862c19c` in the same verified Drive admission package. Every Japanese text interval and listed original image was actually inspected. The July interlude and June bonus were read in native placement, not inserted early. Afterword/colophon/jacket/retailer branding stay paratext; included fiction is not double-counted as an external supplement.

| Spine | Native member under item/ | Paragraph coverage | Directly inspected image assets under image/ | Inspection / limitation |
| --- | --- | --- | --- | --- |
| 1 | `xhtml/p-cover.xhtml` | 0; image-only leaf | `cover.jpg` | Complete |
| 2 | `xhtml/p-fmatter-001.xhtml` | 0; image-only leaf | `kuchie-001.jpg` | Complete |
| 3 | `xhtml/p-fmatter-002.xhtml` | 0; image-only leaf | `kuchie-002.jpg` | Complete |
| 4 | `xhtml/p-fmatter-003.xhtml` | 0; image-only leaf | `kuchie-003-004.jpg` | Complete |
| 5 | `xhtml/p-fmatter-004.xhtml` | 0; image-only leaf | `kuchie-005-006.jpg` | Complete |
| 6 | `xhtml/p-titlepage.xhtml` | 0; image-only leaf | `titlepage.jpg` | Complete |
| 7 | `xhtml/p-caution.xhtml` | 1–4 | — | Complete |
| 8 | `xhtml/p-toc-001.xhtml` | 1–16 | — | Complete |
| 9 | `xhtml/p-001.xhtml` | 1–4 | — | Complete |
| 10 | `xhtml/p-002.xhtml` | 0; image-only leaf | `i-003.jpg` | Complete |
| 11 | `xhtml/p-003.xhtml` | 1–277 | `i-023.jpg` | Complete |
| 12 | `xhtml/p-004.xhtml` | 1–318 | `i-039.jpg` | Complete |
| 13 | `xhtml/p-005.xhtml` | 1–490 | — | Complete |
| 14 | `xhtml/p-006.xhtml` | 1–461 | `i-131.jpg` | Complete |
| 15 | `xhtml/p-007.xhtml` | 1–392 | `i-165.jpg` | Complete |
| 16 | `xhtml/p-008.xhtml` | 1–419 | — | Complete |
| 17 | `xhtml/p-009.xhtml` | 1–431 | `i-235.jpg` | Complete |
| 18 | `xhtml/p-010.xhtml` | 1–182 | — | Complete |
| 19 | `xhtml/p-011.xhtml` | 1–409 | `i-285.jpg` | Complete |
| 20 | `xhtml/p-012.xhtml` | 1–270 | `i-297.jpg`, `i-313.jpg` | Complete |
| 21 | `xhtml/p-013.xhtml` | 1–207 | `i-333.jpg` | Complete |
| 22 | `xhtml/p-014.xhtml` | 1–26 | — | Complete |
| 23 | `xhtml/p-015.xhtml` | 1–109 | `i-349.jpg` | Complete |
| 24 | `xhtml/p-allcover-001.xhtml` | 0; image-only leaf | `allcover-001.jpg` | Complete |
| 25 | `xhtml/p-colophon.xhtml` | 1–18 | — | Complete |
| 26 | `xhtml/p-colophon2.xhtml` | 1–3 | — | Complete |
| 27 | `xhtml/p-bookwalker.xhtml` | 0; image-only leaf | `i-bookwalker.jpg` | Complete |

Totals: **27spines,4,036native paragraph anchors,19original image references**; all514ruby elements preserved in the unchanged witness/locator map. Whole-witness hash/ZIP CRC, every member/paragraph serialization hash and image hash reverify. Zero replacement characters or uninspected substantive body text outside the paragraph/image flow. One context-truncated chapter9p1–33 output was redelivered completely before image34; no skipped interval or credited future-first passage. These mechanical checks support fidelity and coverage, not interpretation by themselves.

V02 mainline exits earlySeptemberY3; final internal bonus adds earlierJune information at F12. Two narrow forecasts keep their failed action results and one narrowly supported privacy subdimension. The actual parent-return referent and same-scene sunny/cloudy detail discrepancy remain bounded uncertainties, not invented source identities. No V03+, external supplement or web narrative was read, no V1 claim opened, and no operational model certified.

Revision0.6 / SHUUKURA-TX-LN-JP-V02-20261017-A1: complete second parent-volume inspection and atomic coverage. I1 hash/membership, 458available units,51unavailable identities,27discovery obligations and290Narō correspondence routes unchanged. Available coverage2/458, LN2/9; no quarter milestone reached and no comprehensive completion claim.


### V03 actual component inspection and first LN-quarter review

Transaction SHUUKURA-TX-LN-JP-V03-20261017-A1 introduces the [complete V03 reading](../02%20Sequential%20Readings/SHUUKURA_V2_LN_V03_DEEP_READING.md), four cumulative deltas, dated candidate model/test updates and [unit/quarter audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_LN_V03_TRANSACTION_AUDIT.md). A draft or inspected witness alone does not advance committed V02; V03 becomes high-water only in the complete introducing commit.

All rows below bind LN-JP-V03 / ACQUIRED-20261017-A1 / Drive1-riDLu1t1xXnGonE6AYn_kV0AX9wGfhO / originalSHA eba1ad0ba6baabeeb6a4f6c1a3cc80d364099d0a848ff36205ca883b9e2e241d / locatorSHA0c47c6d83b20b6649a6b80c259f30863bdc80346c703d965175644aeedddac0b, retained in verified Drive admission package1pi7_hhGoTqMsyEfrju4c-mRFipt41_Ju. Native ordered text and applicable originals were actually inspected. Included interlude/bonus remain part of the parent volume, not external SS completion.

| Spine | Native member under item/ | Paragraph coverage | Original image assets under image/ actually viewed | State / limit |
| --- | --- | --- | --- | --- |
| 1 | `xhtml/p-cover.xhtml` | 0; image-only leaf | `cover.jpg` | Complete |
| 2 | `xhtml/p-fmatter-001.xhtml` | 0; image-only leaf | `kuchie-001.jpg` | Complete |
| 3 | `xhtml/p-fmatter-002.xhtml` | 0; image-only leaf | `kuchie-002.jpg` | Complete |
| 4 | `xhtml/p-fmatter-003.xhtml` | 0; image-only leaf | `kuchie-003-004.jpg` | Complete |
| 5 | `xhtml/p-fmatter-004.xhtml` | 0; image-only leaf | `kuchie-005-006.jpg` | Complete |
| 6 | `xhtml/p-titlepage.xhtml` | 0; image-only leaf | `titlepage.jpg` | Complete |
| 7 | `xhtml/p-caution.xhtml` | 1–4 | — | Complete |
| 8 | `xhtml/p-toc-001.xhtml` | 1–14 | — | Complete |
| 9 | `xhtml/p-001.xhtml` | 1–4 | — | Complete |
| 10 | `xhtml/p-002.xhtml` | 0; image-only leaf | `i-003.jpg` | Complete |
| 11 | `xhtml/p-003.xhtml` | 1–354 | `i-031.jpg` | Complete |
| 12 | `xhtml/p-004.xhtml` | 1–323 | `i-049.jpg` | Complete |
| 13 | `xhtml/p-005.xhtml` | 1–429 | `i-079.jpg` | Complete |
| 14 | `xhtml/p-006.xhtml` | 1–530 | `i-127.jpg` | Complete |
| 15 | `xhtml/p-007.xhtml` | 1–338 | `i-147.jpg` | Complete |
| 16 | `xhtml/p-008.xhtml` | 1–190 | `i-189.jpg` | Complete |
| 17 | `xhtml/p-009.xhtml` | 1–382 | `i-209.jpg` | Complete |
| 18 | `xhtml/p-010.xhtml` | 1–370 | `i-243.jpg` | Complete |
| 19 | `xhtml/p-011.xhtml` | 1–325 | `i-285.jpg` | Complete |
| 20 | `xhtml/p-012.xhtml` | 1–29 | — | Complete |
| 21 | `xhtml/p-013.xhtml` | 1–88 | `i-299.jpg` | Complete |
| 22 | `xhtml/p-014.xhtml` | 0; image-only leaf | `i-300.jpg` | Complete |
| 23 | `xhtml/p-015.xhtml` | 0; image-only leaf | `i-301.jpg` | Complete |
| 24 | `xhtml/p-allcover-001.xhtml` | 0; image-only leaf | `allcover-001.jpg` | Complete |
| 25 | `xhtml/p-colophon.xhtml` | 1–18 | — | Complete |
| 26 | `xhtml/p-colophon2.xhtml` | 1–3 | — | Complete |
| 27 | `xhtml/p-bookwalker.xhtml` | 0; image-only leaf | `i-bookwalker.jpg` | Complete |

Totals:27spines/3401native paragraph anchors/21original image references, all475ruby elements recoverable; original/member/paragraph/image hashes and ZIP CRC reverify. Zero replacement characters or uninspected substantive text outside paragraph/image flow. A context-truncated p-006p116–250 attempt was credited only after complete redelivery. No credited narrative source-order gap remains. F5's exit note was recorded after the next interlude's first75paragraphs and explicitly labeled a source-bounded reconstruction, not a falsely pre-exposure freeze; no intervening prediction depended on it. Original note/erratum history is preserved. All V04+ fiction remains unread; final future-volume advertisement is paratext exposure, not completed plot.

First LN-quarter scope review: frozen I1 still9LN/18accessible supplements/431Kakuyomu units (458available); separate51unavailable identities,27finite discovery duties and290Narō correspondence routes. Nothing is silently admitted or optionalized. LN10/bonuses and later serialization remain outside freeze. Missing full V04 voice narratives/modality evidence and other required bonus gaps block their dependent comprehensive claims, not ordered V04 reading. No source-order/synthesis architecture amendment is needed from this tranche. Character/epistemic/relationship distinctions remain adequate; operational model acceptance still requires independent semantic review and further meaningful tests. Full-corpus monographs, specialists, reconciliation, V1 comparison and integrated argument remain required.

Revision0.7: complete third LN transaction; available3/458, LN3/9, externalSS0/18, Kakuyomu0/431, Narō0/290. First LN-quarter publication/review is this coherent unit, subject to its exact Git audit/integration closure. First available-set milestone115/458 remains pending. I1 bytes/membership and all earlier accepted source/reading records unchanged.


### V04 actual component inspection

Transaction SHUUKURA-TX-LN-JP-V04-20261017-A1 introduces the [complete V04 reading](../02%20Sequential%20Readings/SHUUKURA_V2_LN_V04_DEEP_READING.md), all four cumulative deltas, versioned model/test appendices and [unit audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_LN_V04_TRANSACTION_AUDIT.md). V04 advances high-water only in that whole verified introducing commit; inspected source or a drafted reading alone cannot advance V03. Internal interlude/packing bonus remain parent-volume components, not additional external supplements.

Witness LN-JP-V04 / ACQUIRED-20261017-A1 / Drive1C2bALN18lmmMNKTfLn01GYHd-IRJE9mF /9,511,489bytes/originalSHA57371b889a0f97f77003fb093857323445e06890b588739761c0d6694912dcea/locatorSHAb17ea7993bb9f3a2f252d344e50cad6937f6560390589b296707c102c09dbdc2. Native manifest remains in verified Drive admission package1pi7_hhGoTqMsyEfrju4c-mRFipt41_Ju. OPF Japanese UUIDd1cbd726-53e2-4773-a8db-91116e8f4f31; electronicver0012024-04-19/printbasis2024-04-20, no retail conversion-lineage certificate.

| Spine | Native member under item/ | Paragraph coverage | Original image assets under image/ actually viewed | State / limit |
| --- | --- | --- | --- | --- |
| 1 | `xhtml/p-cover.xhtml` | 0; image-only leaf | `cover.jpg` | Complete |
| 2 | `xhtml/p-fmatter-001.xhtml` | 0; image-only leaf | `kuchie-001.jpg` | Complete |
| 3 | `xhtml/p-fmatter-002.xhtml` | 0; image-only leaf | `kuchie-002.jpg` | Complete |
| 4 | `xhtml/p-fmatter-003.xhtml` | 0; image-only leaf | `kuchie-003-004.jpg` | Complete |
| 5 | `xhtml/p-fmatter-004.xhtml` | 0; image-only leaf | `kuchie-005-006.jpg` | Complete |
| 6 | `xhtml/p-titlepage.xhtml` | 0; image-only leaf | `titlepage.jpg` | Complete |
| 7 | `xhtml/p-caution.xhtml` | 1–4 | — | Complete |
| 8 | `xhtml/p-toc-001.xhtml` | 1–15 | — | Complete |
| 9 | `xhtml/p-001.xhtml` | 1–4 | — | Complete |
| 10 | `xhtml/p-002.xhtml` | 0; image-only leaf | `i-003.jpg` | Complete |
| 11 | `xhtml/p-003.xhtml` | 1–199 | — | Complete |
| 12 | `xhtml/p-004.xhtml` | 1–273 | `i-041.jpg` | Complete |
| 13 | `xhtml/p-005.xhtml` | 1–403 | `i-059.jpg` | Complete |
| 14 | `xhtml/p-006.xhtml` | 1–458 | `i-095.jpg` | Complete |
| 15 | `xhtml/p-007.xhtml` | 1–522 | `i-133.jpg` | Complete |
| 16 | `xhtml/p-008.xhtml` | 1–114 | `i-171.jpg` | Complete |
| 17 | `xhtml/p-009.xhtml` | 1–575 | `i-219.jpg` | Complete |
| 18 | `xhtml/p-010.xhtml` | 1–358 | — | Complete |
| 19 | `xhtml/p-011.xhtml` | 1–419 | `i-269.jpg`, `i-287.jpg` | Complete |
| 20 | `xhtml/p-012.xhtml` | 1–383 | `i-317.jpg` | Complete |
| 21 | `xhtml/p-013.xhtml` | 1–23 | — | Complete |
| 22 | `xhtml/p-014.xhtml` | 1–137 | `i-335.jpg` | Complete |
| 23 | `xhtml/p-015.xhtml` | 0; image-only leaf | `i-338.jpg` | Complete |
| 24 | `xhtml/p-016.xhtml` | 0; image-only leaf | `i-339.jpg` | Complete |
| 25 | `xhtml/p-allcover-001.xhtml` | 0; image-only leaf | `allcover-001.jpg` | Complete |
| 26 | `xhtml/p-colophon.xhtml` | 1–18 | — | Complete |
| 27 | `xhtml/p-colophon2.xhtml` | 1–3 | — | Complete |
| 28 | `xhtml/p-bookwalker.xhtml` | 0; image-only leaf | `i-bookwalker.jpg` | Complete |

Totals28spines/3908native paragraph anchors/21original images/482ruby elements recoverable. All ZIP CRC/source/member/p/image hashes reverified, zero replacement characters or uninspected substantive outside-flow text. Original encounter journalSHA93189512960ff2f33092d8b7ab82f51bd48a592d79c34dd90fd583f2639a627e preserves125observations, two before-outcome model/time packets and unchanged original scoring. No credited source-order exception; one failed jacket filename delivered no content and was corrected before continuing. The V05 advertisement exposes university/cohabitation/rule-change promotion; it does not constitute V05 fictional reading or current proof of all new household rules.

Mainline ends after March graduation/four-year roommate assent; internal bonus advances to packing before move/university entry. The December23–24 interlude disclosed after January4 does not roll latest time backward. Voice story title 仙台さんと卒業式のその後で matches chapter9 but its missing script/audio remains a distinct uninspected witness: no equivalence or modality waiver. Afterword commemorative-story references do not complete publisher SS01/02, which stay in the postLN09 lane.

Revision0.8: complete fourth LN transaction; available4/458, LN4/9, externalSS0/18, Kakuyomu0/431, Narōcorrespondence0/290. V03 first novel-quarter publication is verified on green main; next novel review V05, then V07/V09. Available115/458 not reached. I1 bytes/membership,51unavailable identities/27discovery duties, later-release exclusions and every earlier accepted source record remain unchanged. Automatically continue V05 after exact V04 transaction recovery; all required cumulative/specialist/model/comparison/final gates remain.


### V05 actual component inspection and half-LN source review

Transaction **SHUUKURA-TX-LN-JP-V05-20261017-A1** introduces the [complete V05 reading](../02%20Sequential%20Readings/SHUUKURA_V2_LN_V05_DEEP_READING.md), all four cumulative deltas, preserved historical model/test records/new exit candidates and [unit/half-LN audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_LN_V05_TRANSACTION_AUDIT.md). Only the complete introducing commit advances high-water toV05. Source inspection or a drafted reading alone cannot advance V04. Internal interlude/bonus belong to their parent volume, not the18external supplements.

Witness LN-JP-V05/ACQUIRED-20261017-A1/Drive1VITxPosvtVPTUelwqp2fATA9JAb1R5Zp/16,161,211bytes/sourceSHA dccc06e60cf26f2a443839a4f1e8ba3ed918808ffd7f649aa4f8a9a5c8ccbdab/locatorSHA ff4600a74fa3e9aa855562589d99d174de00ad619a87f3bec25932c624506cec, in verified Drive admission package1pi7_hhGoTqMsyEfrju4c-mRFipt41_Ju. OPF Japanese UUID33eb742f-fab6-4f75-ba87-7dd75fd480e3; electronicver.0022024-10-19/printbasis2024-10-20, no retail conversion-lineage certificate.

| Spine | Native member under item/ | Complete paragraph coverage | Original image assets under image/ actually viewed | Inspection state |
| --- | --- | --- | --- | --- |
| 1 | `xhtml/p-cover.xhtml` | 0; image-only leaf | `cover.jpg` | Complete |
| 2 | `xhtml/p-fmatter-001.xhtml` | 0; image-only leaf | `kuchie-001.jpg` | Complete |
| 3 | `xhtml/p-fmatter-002.xhtml` | 0; image-only leaf | `kuchie-002.jpg` | Complete |
| 4 | `xhtml/p-fmatter-003.xhtml` | 0; image-only leaf | `kuchie-003-004.jpg` | Complete |
| 5 | `xhtml/p-fmatter-004.xhtml` | 0; image-only leaf | `kuchie-005-006.jpg` | Complete |
| 6 | `xhtml/p-titlepage.xhtml` | 0; image-only leaf | `titlepage.jpg` | Complete |
| 7 | `xhtml/p-caution.xhtml` | 1–4 | — | Complete |
| 8 | `xhtml/p-toc-001.xhtml` | 1–16 | — | Complete |
| 9 | `xhtml/p-001.xhtml` | 1–4 | — | Complete |
| 10 | `xhtml/p-002.xhtml` | 0; image-only leaf | `i-003.jpg` | Complete |
| 11 | `xhtml/p-003.xhtml` | 0; image-only leaf | `i-004-005.jpg` | Complete |
| 12 | `xhtml/p-004.xhtml` | 1–279 | `i-023.jpg` | Complete |
| 13 | `xhtml/p-005.xhtml` | 1–487 | `i-055.jpg`, `i-065.jpg` | Complete |
| 14 | `xhtml/p-006.xhtml` | 1–377 | — | Complete |
| 15 | `xhtml/p-007.xhtml` | 1–385 | `i-125.jpg` | Complete |
| 16 | `xhtml/p-008.xhtml` | 1–448 | `i-169.jpg` | Complete |
| 17 | `xhtml/p-009.xhtml` | 1–397 | `i-195.jpg` | Complete |
| 18 | `xhtml/p-010.xhtml` | 1–144 | `i-221.jpg` | Complete |
| 19 | `xhtml/p-011.xhtml` | 1–355 | `i-253.jpg` | Complete |
| 20 | `xhtml/p-012.xhtml` | 1–217 | — | Complete |
| 21 | `xhtml/p-013.xhtml` | 1–417 | `i-277.jpg` | Complete |
| 22 | `xhtml/p-014.xhtml` | 1–175 | `i-329.jpg` | Complete |
| 23 | `xhtml/p-015.xhtml` | 1–25 | — | Complete |
| 24 | `xhtml/p-016.xhtml` | 1–144 | — | Complete |
| 25 | `xhtml/p-017.xhtml` | 0; image-only leaf | `i-348.jpg` | Complete |
| 26 | `xhtml/p-018.xhtml` | 0; image-only leaf | `i-349.jpg` | Complete |
| 27 | `xhtml/p-allcover-001.xhtml` | 0; image-only leaf | `allcover-001.jpg` | Complete |
| 28 | `xhtml/p-colophon.xhtml` | 1–18 | — | Complete |
| 29 | `xhtml/p-colophon2.xhtml` | 1–3 | — | Complete |
| 30 | `xhtml/p-bookwalker.xhtml` | 0; image-only leaf | `i-bookwalker.jpg` | Complete |

Totals30spines/3895native paragraph anchors/22original images/518ruby elements. CRC/source/member/paragraph-serialization/image hashes reverified, zero replacement characters or substantive outside-flow omission. One wholly context-truncated p-006request from133 was creditedZERO and redelivered in full before advancing; no missing credited range. Original journal111,540bytes/SHA16e6c9368ec888ba607200620946033ffa7490fad78e6c776ec8247466191fb0 preserves114observations/F0–F12 and the pre-outcome S0.5packet. Native-ruby name clarification after freeze confirms Mio/みお and Hanamaki Kikyō/はなまきききょう without editing original pending notes. V06 advertisement is declared exposure, not narrative inspection.

Mainline terminal time is the Monday after a late-May Sunday, with Miyagi at Maika's home and tonight-away notice sent. No completed overnight duration/return is credited. The interlude rewinds to move-day early afternoon, the internal bonus to after deliveries; neither is a terminal return from Maika. Actual move, classes and tutoring are new coverage, not assumed from promotional recap. Source-lane distinctions and original V01–V04 readings remain intact.

The half-LN source audit preserves **5/9** versus **5/458**, externalSS0/18/Kakuyomu0/431/Narōcorrespondence0/290. I1 bytes and458ordered IDs remain unchanged, as do the51known missing identities and27finite discovery records. A concrete lead requires reconciliation: V05afterwordp-015p8–12 and the already captured V04 author notice describe THREE authored voice scripts, while I1 names two blocked V04 voice identities and separately freezes the notice-discovery obligations. V07 notices likewise mention public/limited audio. Map the thirdV04 identity/V07 records within those finite debts after LN09, preserve duplicate/adaptation distinctions, and actually verify full scripts/audio/capability; do not equate a preview or matching chapter title with coverage. This is existing-source discovery, not silent admission of a future release or alteration of the frozen denominator.

Revision0.9: V05complete atomic transaction and half-LN review; continue automatically toV06 after committed recovery, then all remaining inventory/reconciliation/monograph/specialist/model/V1/integrated/release duties. No optionalized source debt or comprehensive completion claim; later publications stay excluded.


### V06 actual component inspection

Transaction **SHUUKURA-TX-LN-JP-V06-20261017-A1** introduces the [complete V06 reading](../02%20Sequential%20Readings/SHUUKURA_V2_LN_V06_DEEP_READING.md), all four cumulative deltas, preserved model/test histories, new exit candidates and [unit audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_LN_V06_TRANSACTION_AUDIT.md). Only its complete introducing commit advances high-water fromV05 toV06. Internal interlude/dual-view bonus remain components of one LN transaction, not external supplements.

Witness LN-JP-V06/ACQUIRED-20261017-A1/Drive`1MQTM3o3pXqzyigHtT5aSURWTy_dwQ1YF`/17,056,253bytes/sourceSHA`1dd096de172fe0641021274591a29eadda563ded169f6d564cf02b53120fee2a`/locatorSHA`94329098a1aeaba22d89c84ffa8237ac3b9cad4b1032fb322eb088e9f33189f9`, in verified admission package`1pi7_hhGoTqMsyEfrju4c-mRFipt41_Ju`. OPFitem/standard.opf/ja/catalog identifier04075773A20043700000 is distinct from Drive identity; electronicver.001/printfirst2025-02-20. Retail conversion lineage remains unverified.

| Spine | Native member under item/ | Complete paragraph coverage | Original image assets under image/ actually viewed | Inspection state |
| --- | --- | --- | --- | --- |
| 1 | `xhtml/p-cover.xhtml` | 0; image-only leaf | `cover.jpg` | Complete |
| 2 | `xhtml/p-fmatter-001.xhtml` | 0; image-only leaf | `kuchie-001.jpg` | Complete |
| 3 | `xhtml/p-fmatter-002.xhtml` | 0; image-only leaf | `kuchie-002.jpg` | Complete |
| 4 | `xhtml/p-fmatter-003.xhtml` | 0; image-only leaf | `kuchie-003-004.jpg` | Complete |
| 5 | `xhtml/p-fmatter-004.xhtml` | 0; image-only leaf | `kuchie-005-006.jpg` | Complete |
| 6 | `xhtml/p-titlepage.xhtml` | 0; image-only leaf | `titlepage.jpg` | Complete |
| 7 | `xhtml/p-caution.xhtml` | 1–4 | — | Complete |
| 8 | `xhtml/p-toc-001.xhtml` | 1–17 | — | Complete |
| 9 | `xhtml/p-001.xhtml` | 1–4 | — | Complete |
| 10 | `xhtml/p-002.xhtml` | 0; image-only leaf | `i-003.jpg` | Complete |
| 11 | `xhtml/p-003.xhtml` | 0; image-only leaf | `i-004-005.jpg` | Complete |
| 12 | `xhtml/p-004.xhtml` | 1–218 | `i-019.jpg` | Complete; local image order exception below |
| 13 | `xhtml/p-005.xhtml` | 1–284 | — | Complete |
| 14 | `xhtml/p-006.xhtml` | 1–222 | `i-065.jpg` | Complete |
| 15 | `xhtml/p-007.xhtml` | 1–398 | `i-103.jpg` | Complete |
| 16 | `xhtml/p-008.xhtml` | 1–157 | — | Complete |
| 17 | `xhtml/p-009.xhtml` | 1–377 | `i-139.jpg` | Complete |
| 18 | `xhtml/p-010.xhtml` | 1–382 | `i-157.jpg` | Complete |
| 19 | `xhtml/p-011.xhtml` | 1–347 | `i-187.jpg` | Complete |
| 20 | `xhtml/p-012.xhtml` | 1–235 | — | Complete |
| 21 | `xhtml/p-013.xhtml` | 1–278 | `i-247.jpg` | Complete |
| 22 | `xhtml/p-014.xhtml` | 1–558 | — | Complete |
| 23 | `xhtml/p-015.xhtml` | 1–196 | `i-325.jpg` | Complete |
| 24 | `xhtml/p-016.xhtml` | 1–31 | — | Complete |
| 25 | `xhtml/p-017.xhtml` | 1–128 | — | Complete |
| 26 | `xhtml/p-018.xhtml` | 0; image-only leaf | `i-342.jpg` | Complete |
| 27 | `xhtml/p-019.xhtml` | 0; image-only leaf | `i-343.jpg` | Complete |
| 28 | `xhtml/p-allcover-001.xhtml` | 0; image-only leaf | `allcover-001.jpg` | Complete |
| 29 | `xhtml/p-colophon.xhtml` | 1–18 | — | Complete |
| 30 | `xhtml/p-colophon2.xhtml` | 1–3 | — | Complete |
| 31 | `xhtml/p-bookwalker.xhtml` | 0; image-only leaf | `i-bookwalker.jpg` | Complete |

Totals **31spines/3857native paragraph anchors/20original images/589ruby annotations**. Original bytes/ZIP CRC/all spine-member and paragraph serialization/image hashes reverified; zero replacement characters or substantive outside-flow omission. All listed Japanese text and images actually inspected. One wholly lost combined frontmatter response received ZERO credit and was fully redelivered before fiction. At p-004image135, prose136–145 had been delivered before viewing the embedded image; original O003 records this local order exception and no prediction earns blind credit there. Source completeness does not erase that qualification.

Entering A1 preserves the mistaken catalog-ID acquisition-register label, corrected solely by A2 before all fiction/images; original source bytes and original-source hash were always correct. Original journal137,309bytes/SHA`8c8744323e56b3623b43f90e51efe93db57f7f9a85e10c5d4286965cc2a84a44` contains49observations/F0–F16 and both original prospective ordinary-decision packets. Ruby helper initially omitted rt-tail text from its auxiliary base labels; paragraph reading retained all tails. The complete589-ruby audit used corrected labels after the encounter freeze and preserves the faulty derivative separately. No source text or historical prospective note was changed.

Mainline advances from the fourth morning after three nights at Maika's to the morning after a later-July post-exam encounter. Miyagi has returned, both eat together and accept a future summer outing, with Miyagi delegating the destination to Sendai; the outing is not yet performed. The Thursday Maika interlude and last dual-view bonus rewind to earlier May events; bonus speech to an empty room never becomes a received notice. V07 advertisement exposure is declared, not V07 narrative coverage. Original V05p-004197–224 was narrowly reinspected to verify the disputed notification rule's actual wording; this is claim correction support, not another completed unit.

Revision1.0: sixth complete atomic LN transaction, LN6/9 and available6/458. V05half-LN publication is CLOSED_ON_GREEN_MAIN; next LN review isV07/9. ExternalSS0/18, Kakuyomu0/431 and Narō0/290 unchanged. I1 bytes/458ordered identities,51known unacquired identities/27finite discovery duties, required audio mapping and future-release exclusions remain intact. Continue automatically toV07 after verified complete commit, then every remaining source and synthesis responsibility.


### V07 actual component inspection and novel three-quarter review

Transaction **SHUUKURA-TX-LN-JP-V07-20261017-A1** introduces the [complete V07 reading](../02%20Sequential%20Readings/SHUUKURA_V2_LN_V07_DEEP_READING.md), four reconciled instruments, preserved models/tests, new exit candidates and [unit audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_LN_V07_TRANSACTION_AUDIT.md). High-water advances only in the complete introducing commit, never from source reading alone. Native interlude/bonus remain parts of one LN transaction.

Witness **LN-JP-V07/ACQUIRED-20261017-A1**, Drive`1tSe_PTxTct3pIIHFT_3n3-7cCnP76L_X`,10,844,829bytes/sourceSHA`cb560da567093d94c7016c9b71e765b2ff808a933949c6dbb6e043e57927949b`, locatorSHA`6d98463801c014779c0ff9a14948b4f63fee0db24478b4a98935d1023239f9b2`, complete map in verified package`1pi7_hhGoTqMsyEfrju4c-mRFipt41_Ju`. Native OPFitem/standard.opf/catalog04075975A21973900000 **declares zh-CN**; complete actual text/kana/ruby/colophon are Japanese. Retain this bounded packaging anomaly and unknown conversion lineage without changing source labels/bytes. Colophonver.001/print first2025-08-20/Japanese text only. V08 has the same declared-language flag and must be checked at its boundary.

| Spine | Native member under item/ | Complete paragraph coverage | Original images actually viewed under image/ | Inspection state |
| --- | --- | --- | --- | --- |
| 1 | `xhtml/p-cover.xhtml` | 0; image-only leaf | `cover.jpg` | Complete |
| 2 | `xhtml/p-fmatter-001.xhtml` | 0; image-only leaf | `kuchie-001.jpg` | Complete |
| 3 | `xhtml/p-fmatter-002.xhtml` | 0; image-only leaf | `kuchie-002.jpg` | Complete |
| 4 | `xhtml/p-fmatter-003.xhtml` | 0; image-only leaf | `kuchie-003-004.jpg` | Complete |
| 5 | `xhtml/p-fmatter-004.xhtml` | 0; image-only leaf | `kuchie-005-006.jpg` | Complete |
| 6 | `xhtml/p-titlepage.xhtml` | 0; image-only leaf | `titlepage.jpg` | Complete |
| 7 | `xhtml/p-caution.xhtml` | 1–4 | — | Complete |
| 8 | `xhtml/p-toc-001.xhtml` | 1–15 | — | Complete |
| 9 | `xhtml/p-001.xhtml` | 1–4 | — | Complete |
| 10 | `xhtml/p-002.xhtml` | 0; image-only leaf | `i-003.jpg` | Complete |
| 11 | `xhtml/p-003.xhtml` | 0; image-only leaf | `i-004-005.jpg` | Complete |
| 12 | `xhtml/p-004.xhtml` | 1–126 | — | Complete |
| 13 | `xhtml/p-005.xhtml` | 1–367 | `i-035.jpg` | Complete |
| 14 | `xhtml/p-006.xhtml` | 1–418 | `i-059.jpg`, `i-081.jpg` | Complete |
| 15 | `xhtml/p-007.xhtml` | 1–135 | — | Complete |
| 16 | `xhtml/p-008.xhtml` | 1–355 | `i-129.jpg` | Complete |
| 17 | `xhtml/p-009.xhtml` | 1–383 | `i-159.jpg` | Complete |
| 18 | `xhtml/p-010.xhtml` | 1–613 | `i-195.jpg` | Complete |
| 19 | `xhtml/p-011.xhtml` | 1–443 | — | Complete |
| 20 | `xhtml/p-012.xhtml` | 1–400 | `i-255.jpg` | Complete |
| 21 | `xhtml/p-013.xhtml` | 1–360 | `i-293.jpg` | Complete |
| 22 | `xhtml/p-014.xhtml` | 1–13 | — | Complete |
| 23 | `xhtml/p-015.xhtml` | 1–136 | `i-329.jpg` | Complete |
| 24 | `xhtml/p-016.xhtml` | 0; image-only leaf | `i-332-333.jpg` | Complete |
| 25 | `xhtml/p-allcover-001.xhtml` | 0; image-only leaf | `allcover-001.jpg` | Complete |
| 26 | `xhtml/p-colophon.xhtml` | 1–18 | — | Complete |
| 27 | `xhtml/p-colophon2.xhtml` | 1–3 | — | Complete |
| 28 | `xhtml/p-bookwalker.xhtml` | 0; image-only leaf | `i-bookwalker.jpg` | Complete |

Totals **28spines/3793native paragraph anchors/20original images/541ruby elements**, all inspected;158unique ruby guides separately checked postread. CRC/source/member/paragraph serialization/image hashes verified; zero replacements or uncovered substantive outside-flow text. All image anchors were viewed before following prose. Ch2lastparagraph367 initially not delivered was recovered before advancing. Completely lost p-010467–546 response received ZERO credit and was safely redelivered before new prose. The original journal records both recoveries.

Entering A1@11:02:22.819643UTC contains Ami surname kanji白河 corrected solely to白川 by A2@11:02:50.247949UTC BEFORE images/fiction, stable identity unchanged. MainlineF10@11:54:03.766230UTC freezes3623anchors/16images before afterword/bonus/tail; journal prefix152080bytes/SHA`c622bce0d07bf0815029567a73199d6fd27e42cf0e7605b87a0322ebf98c41ab`. Original full journal162711bytes/SHA`0b3d3633fcc5e1715066170546b80e00ad685ebcc0f22cf1775a1083760c8f26`,56observations/F0–F14, frozen11:58:36.750829UTC. Lexical correction of a too-specific household-agency inference is attributable and does not edit the original note. All284literal/source checks pass; draft-checker lexical mismatches were inspected/corrected against unchanged originals and retained separately.

Mainline terminal time is lateSeptember27 after the two birthdays; it does not become ninthbirthday childhood or adultAugust24 because the bonus is read last. Current year wholecake promise is fully performed, Sendai ears actually pierced by separate prior grants, and the new late-contact vow remains OPEN. Café interest/announced October busyness is not an actual first shift/employer acceptance. Native V08 teaser reveals future job outline AFTER F10, so later job-outcome forecasts cannot claim blindness to it. No other-lane/V1 conclusion is fit.

Novel75% review keeps7/9 distinct from7/458, SS0/18/Kakuyomu0/431/Narō0/290; method/architecture/reconstruction0.2 remain appropriate. Every51missing source identity/27finite discovery duty/audio responsibility remains mandatory. No thirdV04 script/V07 voice recording was heard or completed from matching prose. Maika monograph responsibility remains strong; Mio/Ami/pupil/family figures receive differentiated substantial bounded treatment unless later source justifies monographs. Current models M0.9/S0.10 are untested/noncurrent; nine earlier cases retain fourfailures/oneexposure-qualifiedgiftmatch/fourbaseline-tiednarrowmatches. No independently validated domain or completed later analytical phase is claimed.

Revision1.1: seventh complete LN transaction only in its introducing commit; audited visible LN75% publication required now, then continue automatically toV08–09, all frozen later sources and every reconciliation/monograph/specialist/reconstruction/V1/integrated/release duty. I1 denominator, gaps and future exclusions remain intact.


### V08 actual component inspection

Transaction **SHUUKURA-TX-LN-JP-V08-20261017-A1** introduces the [complete V08 reading](../02%20Sequential%20Readings/SHUUKURA_V2_LN_V08_DEEP_READING.md), four reconciled instruments, append-preserved reconstruction records and [unit audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_LN_V08_TRANSACTION_AUDIT.md). High-water advances only in the whole introducing commit. Eleven chapters and the dual-focalizer native bonus are one LN transaction.

Exact witness: V08/ACQUIRED-20261017-A1/Drive1if9ljcOHNJvaLsmFYhD3_SuFChvTRR6F/8308796bytes/sourceSHAa8f5a649c0797e71c2481d72123ce1ed64332f61bf39360309d7e57b45805642/locatorSHAcb391565c853ec1c65ae4f733bf281d2570e4aaaadea4beb4e659b6b1f8b9980; mappackage1pi7_hhGoTqMsyEfrju4c-mRFipt41_Ju; catalog04076170A23275700000/electronic2025-12-19ver.001/printfirst2025-12-20. OPFdeclareszh-CN, actual complete Japanese base/kana/ruby/colophon verified; packaging anomaly/unknownconversionlineage retained. The electronic and print dates are distinct.

| Spine | Native member under item/ | Complete paragraph coverage | Original images actually viewed under image/ | Inspection state |
| --- | --- | --- | --- | --- |
| 1 | `xhtml/p-cover.xhtml` | 0; image-only leaf | `cover.jpg` | Complete |
| 2 | `xhtml/p-fmatter-001.xhtml` | 0; image-only leaf | `kuchie-001.jpg` | Complete |
| 3 | `xhtml/p-fmatter-002.xhtml` | 0; image-only leaf | `kuchie-002.jpg` | Complete |
| 4 | `xhtml/p-fmatter-003.xhtml` | 0; image-only leaf | `kuchie-003-004.jpg` | Complete |
| 5 | `xhtml/p-fmatter-004.xhtml` | 0; image-only leaf | `kuchie-005-006.jpg` | Complete |
| 6 | `xhtml/p-titlepage.xhtml` | 0; image-only leaf | `titlepage.jpg` | Complete |
| 7 | `xhtml/p-caution.xhtml` | 1–4 | — | Complete |
| 8 | `xhtml/p-toc-001.xhtml` | 1–16 | — | Complete |
| 9 | `xhtml/p-001.xhtml` | 1–4 | — | Complete |
| 10 | `xhtml/p-002.xhtml` | 0; image-only leaf | `i-003.jpg` | Complete |
| 11 | `xhtml/p-003.xhtml` | 0; image-only leaf | `i-004-005.jpg` | Complete |
| 12 | `xhtml/p-004.xhtml` | 1–318 | `i-023.jpg` | Complete |
| 13 | `xhtml/p-005.xhtml` | 1–478 | `i-063.jpg` | Complete |
| 14 | `xhtml/p-006.xhtml` | 1–341 | — | Complete |
| 15 | `xhtml/p-007.xhtml` | 1–374 | `i-123.jpg` | Complete |
| 16 | `xhtml/p-008.xhtml` | 1–606 | — | Complete |
| 17 | `xhtml/p-009.xhtml` | 1–527 | `i-187.jpg` | Complete |
| 18 | `xhtml/p-010.xhtml` | 1–290 | `i-231.jpg` | Complete |
| 19 | `xhtml/p-011.xhtml` | 1–288 | `i-249.jpg` | Complete |
| 20 | `xhtml/p-012.xhtml` | 1–240 | — | Complete |
| 21 | `xhtml/p-013.xhtml` | 1–307 | `i-293.jpg` | Complete |
| 22 | `xhtml/p-014.xhtml` | 1–793 | `i-325.jpg`, `i-365.jpg` | Complete |
| 23 | `xhtml/p-015.xhtml` | 1–33 | — | Complete |
| 24 | `xhtml/p-016.xhtml` | 1–217 | — | Complete |
| 25 | `xhtml/p-allcover-001.xhtml` | 0; image-only leaf | `allcover-001.jpg` | Complete |
| 26 | `xhtml/p-colophon.xhtml` | 1–18 | — | Complete |
| 27 | `xhtml/p-colophon2.xhtml` | 1–3 | — | Complete |
| 28 | `xhtml/p-bookwalker.xhtml` | 0; image-only leaf | `i-bookwalker.jpg` | Complete |

Totals28spines/4857nativeanchors/19originalimages/723ruby/175uniqueguides, all deliberately inspected. CRC/source/member/paragraphserialization/imagehashes pass; zero replacements/uncovered outside-flow text. Native image order held. Lost source deliveries received zero credit until full bounded redelivery. All1088nonempty literal/locator checks pass after47draft expectation/inflection/nearby-locator corrections against unchanged originals; the failed checker draft is retained and no source/packet/journal edited.

EnteringA1@12:32:43.807356UTC binds23442ad7/tree2b3da1/teninputs; A2@12:33:35.428699UTC clarifies edition/base colophon BEFOREfiction/images. MainlineF11@13:28:56.525143UTC freezes4586anchors/17images, prefix160488bytes/SHA4e51d2e5cc7c9dedebb205ec8afe845b5a36b301813af23cf36786ad6fff5c3d BEFOREafterword/rewoundbonus. FullinspectionF14@13:33:49.169916UTC coversall4857/19, prefix172635bytes/SHAfe6a21d574aa13d89c1230059903fedce959d1b84b30e2874cff1e248e5415f1. Original journal177940bytes/SHA13eb8bf7568c2356e4163cda1bcdae8ed093ca20e8562eabd8d1a6ec429de717/63observations/F0–F15/sealed13:39:32.428420UTC. O041/O063 correct draft piercing references toSep25, notSep27; unchanged earlier notes remain visible. MainlineDec25night is not reset by the first-Sunday bonus.

Autumn café work actually starts and ends; the separate winter offer is explicitly approved but its first shift is unshown. Festival and both Christmas occasions occur; zoo remains unperformed. Photo-permission vow is breached, concealment and origin-secrecy vows fulfilled. M names possessiveness without a complete LOVE account; S public postgrad hope does not become a mutual extension. Both ordinary competence and local ignored limits/actual accommodations are retained.

V08afterword corroborates publicV07-related voice material and two limited recordings including Maika, not actual audio inspection. All51missingidentities/27finite notices/290Narōduties remain mandatory; no matching prose is automatically a faithful recording substitute. No V09/other-lane/V1fiction or future release is admitted.

Revision1.2: eighth complete LN transaction only in its whole introducing commit. ContinueV09andall frozen later lanes and cumulative/reconstructive/comparative/synthesis/release requirements. The run remains active.


### V09 actual component inspection and LN100% review

Transaction **SHUUKURA-TX-LN-JP-V09-20261017-A1** advances only in its whole introducing commit. [Complete reading](../02%20Sequential%20Readings/SHUUKURA_V2_LN_V09_DEEP_READING.md), four ledgers/two preserved model homes and [unit audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_LN_V09_TRANSACTION_AUDIT.md) form one transaction. Ten chapters/native two-part middle-school bonus/paratext/images are components, not separate units.

Exact witness: V09/ACQUIRED-20261017-A1/Drive1RK-HYY-C_iMlH7Tua_p-Pik1GP5XCri_/7701730bytes/sourceSHA3201ae3ffd1230a526dd5d9a184d4a76ab7aff4a7b244160cbfc886acbb8086a/locatorSHAe3355f5468a51f857a0a3e5cf22658fe5ca8313bda17c4e1c21d2cc94f2496fe; mappackage1pi7_hhGoTqMsyEfrju4c-mRFipt41_Ju; OPFja/UUID41b49992-da0c-4afc-9ee1-5ede50c0db36/electronicandprintfirst2026-05-20ver.001. No V08 language/date anomaly is propagated. Static native Kobo resource references were not executed or counted as images.

| Spine | Native member under item/ | Complete paragraph coverage | Original image viewed under image/ | Inspection |
| --- | --- | --- | --- | --- |
| 1 | `xhtml/p-cover.xhtml` | 0/image-only leaf | `cover.jpg` | Complete |
| 2 | `xhtml/p-fmatter-001.xhtml` | 0/image-only leaf | `kuchie-001.jpg` | Complete |
| 3 | `xhtml/p-fmatter-002.xhtml` | 0/image-only leaf | `kuchie-002.jpg` | Complete |
| 4 | `xhtml/p-fmatter-003.xhtml` | 0/image-only leaf | `kuchie-003-004.jpg` | Complete |
| 5 | `xhtml/p-fmatter-004.xhtml` | 0/image-only leaf | `kuchie-005-006.jpg` | Complete |
| 6 | `xhtml/p-titlepage.xhtml` | 0/image-only leaf | `titlepage.jpg` | Complete |
| 7 | `xhtml/p-caution.xhtml` | 1–4 | — | Complete |
| 8 | `xhtml/p-toc-001.xhtml` | 1–15 | — | Complete |
| 9 | `xhtml/p-001.xhtml` | 1–4 | — | Complete |
| 10 | `xhtml/p-002.xhtml` | 0/image-only leaf | `i-003.jpg` | Complete |
| 11 | `xhtml/p-003.xhtml` | 0/image-only leaf | `i-004-005.jpg` | Complete |
| 12 | `xhtml/p-004.xhtml` | 1–363 | `i-031.jpg` | Complete |
| 13 | `xhtml/p-005.xhtml` | 1–371 | `i-043.jpg` | Complete |
| 14 | `xhtml/p-006.xhtml` | 1–353 | — | Complete |
| 15 | `xhtml/p-007.xhtml` | 1–395 | `i-103.jpg` | Complete |
| 16 | `xhtml/p-008.xhtml` | 1–388 | `i-161.jpg` | Complete |
| 17 | `xhtml/p-009.xhtml` | 1–296 | — | Complete |
| 18 | `xhtml/p-010.xhtml` | 1–252 | `i-197.jpg` | Complete |
| 19 | `xhtml/p-011.xhtml` | 1–410 | — | Complete |
| 20 | `xhtml/p-012.xhtml` | 1–338 | `i-253.jpg` | Complete |
| 21 | `xhtml/p-013.xhtml` | 1–405 | `i-293.jpg` | Complete |
| 22 | `xhtml/p-014.xhtml` | 1–14 | — | Complete |
| 23 | `xhtml/p-015.xhtml` | 1–320 | — | Complete |
| 24 | `xhtml/p-016.xhtml` | 0/image-only leaf | `i-344-345.jpg` | Complete |
| 25 | `xhtml/p-allcover-001.xhtml` | 0/image-only leaf | `allcover-001.jpg` | Complete |
| 26 | `xhtml/p-colophon.xhtml` | 1–18 | — | Complete |
| 27 | `xhtml/p-colophon2.xhtml` | 1–3 | — | Complete |
| 28 | `xhtml/p-bookwalker.xhtml` | 0/image-only leaf | `i-bookwalker.jpg` | Complete |

Totals28spines/3949paragraphs/18originalimages/567ruby/162uniqueguides/967nonempty material literalchecks. Source/member/paragraphserialization/imagehash/CRC/UTF8/outsideflow verification passes. First-checker221paraphrase/inflection/nearby-anchor mismatches were all reinspected and corrected only in the checker; failed draft retained, source/journal/packets unchanged. Lostp0111–80output had zero credit until verified recovery/redelivery. Original image order held.

EnteringA1@14:28:28.061691UTC binds299cc6df/treece0c5717/teninputs/opening10780bytesSHA0527e5cd68cb7143f8ccd0da4e733e8362e0dcde25f555f3dae2121cb64210db. Typo-onlyA2@14:28:54.414869UTC before allfiction/images has combinedopeningSHAb8bd6aa0d44841caff0ab6c32a2a760e1bae237d36a4438e38a2cc950a9cfdd1. F5@15:09:44.864274UTC/1893p/12images freezes106382bytesSHA2d44155d4e12b7ea4df635d0ebf07979979f5a866786dd12ba85ad818082eda6. MainlineF10@15:37:00.291465UTC/3594p/15images freezes158329bytesSHAed22147780caa9f57c2d8afc9f7f3bdb508cd7fd383dfa6443f5596f94be7952 BEFORE afterword/middle-schoolbonus/tail. Journal173510bytes/SHA5813aef79c1eb4b51c5b9b9f439e79814f06531805ae03f7bd07f2269a7a9f31/51observations/sealed2026-10-17T15:44:18.018414Z. Late bonus does not reset late-February endpoint.

Actual developments: winter work/zoo/NewYear meals/truffles; lip bought/cream used/pen case at university; one-off right consumed without original intrusive performance. Particular no respected beside exact entry/border/photo failures. M says interest/fun and names jealousy; S genuine relational likes remain partly unrecognized and specific family meal history reaches M. No formal romance, indefinite household or complete mutual knowledge. Planned trio outing/March visit/WhiteDay/result/future aqua-zoo/nextValentine remain unperformed; old stew/borrowed-skirt return/weather/parent-ellipsis uncertainties persist. Bird-photo transfer unshown. Family bonus gives new context, not proof of parental motives/maternal fate or adult exact recall.

LN100% review: all nine admitted originals independently read as complete units, with four cumulative instruments and preserved actual test history; later cross-lane reconciliation still required. Support-role gaps, baseline-discriminating tests, narrator-specific private access and overconfident psychological causation remain priorities. No new primary narrative source has been silently admitted. Next **BW-JP-V03** is already in I1 at ordinal10 but still requires its exact unit/placement/admission check before substantive reading; then all frozen later duties continue. ExternalSS0/18, Kak0/431, Narō0/290. Voices/51knownmissing/27discovery notices remain mandatory; no audio was heard and no V1/web/externalSS fiction read. Runactive; LN10 excluded.


### BW03 actual component inspection — first external supplement

[Complete historical reading](../03%20Web%20and%20Supplemental%20Readings/SHUUKURA_V2_BW_JP_V03_DEEP_READING.md), four ledger deltas/model evidence addenda and [unit audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_BW_JP_V03_TRANSACTION_AUDIT.md) form **SHUUKURA-TX-BW-JP-V03-20261017-A1**. HWM advances only in the whole introducing commit. BW-JP-V03/Drive1fby4VCdim7QYgMPeqIrxsMztA8aoVe8z/636131bytes/SHA418c2c8efc7c4a92d57d3705142b6881aa5122b5edc9a0659d1cc22ebd2c0a10; locatorSHAfd247540fc7a3d09e3572af966f5a50ac539c7983f20d60318378f53dc135572; navSHAcfa771cdeefa1eff6b79a38b3c61d57fa31b5ac6d42a0330be8f96b4f3d46d1b; evidenceDrive1YWFdbKdwOxSf5sAhCtoAWrJW6MKFRIhs/29612bytes/SHA6f30cf169e5b492b5c14f032798124a21ba654dc25c048baf5d3c6e1b6855100/readbackverified.

| Complete component | Actual inspection |
| --- | --- |
| spine1 / cover.jpg | Original cover viewed before fiction |
| spine2 / item/xhtml/p-001.xhtml | All185paragraph anchors; Miyagi then Sendai; one story |
| spine3 / i001.jpg | Original image colophon read; issue2023-12-20/authorHanedaUsa/KADOKAWA/BookWalker |
| nonspine / item/navigation-documents.xhtml | Entire538bytes inspected after strict extra-XHTML failure; Navigation/Guide coverlinks only, no fiction |

3spines/185p/2images plusnav;76literalchecks/0ruby; CRC/source/member/serialization/image/UTF8/outsideflow verified. Initial locator map unchanged; explicit nav companion records the later completeness finding. Full private evidence package13members contains no raw primary media. Entering16:22:36.893234UTC binds priorf05e5ffb/teninputs; F2@16:25:32.784373UTC/8036bytesSHA476993f10be9130174ad7bf0d8dba3d3c18642009dd0fcbef7d7ab9e6a5041b0 beforecolophon; journalQ1@16:28:45.347526UTC/10970bytesSHAc7384a1ce17e3ced581caa1b0ce6f2187811aa799c848680465df0b613055300.

Source is retrospectively placed after LN09; depicted highschoolY3festivalDAY2/exactage-date unresolved. Adult M/S-V09-EXIT unchanged. No blind forecast/new modeltest/V1 reading/cross-witness equivalence asserted. Next BW-JP-V06 automatically; all remaining sources and architecture outputs required.

BW03-C1 later chronology refinement: distinctive original LN03/BW03 café/qualified-remark/final-year correspondence places day2 in October (early October approximate; exact day/year/numeric ages not assigned here). See the [post-seal addendum](../03%20Web%20and%20Supplemental%20Readings/SHUUKURA_V2_BW_JP_V03_DEEP_READING.md#post-seal-chronology-and-novel-correspondence--bw03-c1). Frozen original BW03 journal and all LN01–09 accepted bytes unchanged; one additional version of PROP-BW-JP-V03-001 and EPI-BW-JP-V03-016, no new claim/test.


### BW06 actual component inspection — second external supplement

Transaction **SHUUKURA-TX-BW-JP-V06-20261017-A1** binds the [complete reading](../03%20Web%20and%20Supplemental%20Readings/SHUUKURA_V2_BW_JP_V06_DEEP_READING.md), four reconciled ledgers/model-evidence addenda and [unit audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_BW_JP_V06_TRANSACTION_AUDIT.md). Coverage advances only in the whole introducing commit. I1 membership/order/exclusions remain unchanged.

| Component / identity | Complete inspection and limit |
| --- | --- |
| Source | Drive1YPKxevk2nlULpEQBoYYvyzlPgSU7qCUF/636614bytes/SHA`f33b45be05f32d03f0c2c9b91671cd6d75f1505d0ff488689268364a62b74d2d`; OPFja/identifier syuuniitidokurasumeito006 |
| Native leaves | Cover.jpg viewed before fiction; all132p of item/xhtml/p-001.xhtml; i001.jpg imagecolophon viewed after story |
| Extra navigation | Complete538bytes/SHAcfa771cdeefa1eff6b79a38b3c61d57fa31b5ac6d42a0330be8f96b4f3d46d1b; cover navigation only, originally mapped and actually read |
| Metadata | BOOKWALKER limited author-written volume6 bonus/羽田宇佐/KADOKAWA/BookWalker/issue2025-02-20; no fictional date or retail-binary certification |
| QA | All3spines/132p/2images/navigation;70material literal checks,0ruby; CRC/source/member/serializedparagraph/image/UTF8/outside-flow checks PASS |
| Locator/evidence | MapSHA`551c9cedb70466b86bb3e8d2ef44e8b8d1ebcc8f71c1d0f68b6a1594786426ae`; verified Drive package1KxZgBZi9SglSubehU3p24-5OruiVuJB-/28933bytes/SHA b0c40368a981af917f8e77b2b5bbf8031e6abb9ac599a81577cb1b2e8312c00d/13members/upload-download/allmemberhashes verified |
| Prospective records | Entry2026-10-17T17:07:02.301800+00:00/priora41c6821/tenfullinputs; F1first67p and F2all132p preserve prefixes before later disclosure; journal15656bytes/SHA`bb5db9bd4bc5a3bd709680251589b1f7ad2ca95ee9ad8823f5383f4591f369cb`/four observations sealed2026-10-17T17:09:55.909246+00:00 |

The story depicts their university/shared-home interval after kettle purchase/tutoring start, first evening and following represented shopping occasion. Exact calendar placement/numeric ages and correspondence/deduplication with the novel's separate stew offer remain unresolved. Actual tea preparation, groceries in cart and arm/cart detour are distinguished from completed drinking/payment/cooking. Presence at the shop does not verify a general five-minute or silence-assent policy. Current adult M/S-V09-EXIT and all prior freezes remain intact. No new test/formal forecast/V1/web/audio reading.

ExternalSS2/18/available11/458 only in the complete unit commit. Next **BW-JP-V07** exact original/admission check and reading automatically; all remaining sources and architectural outputs persist. LN10/later releases excluded; runactive/gateOPEN.


### BW07 actual component inspection — third external supplement

**SHUUKURA-TX-BW-JP-V07-20261017-A1** binds the [reading](../03%20Web%20and%20Supplemental%20Readings/SHUUKURA_V2_BW_JP_V07_DEEP_READING.md), four ledger deltas/model evidence addenda and [audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_BW_JP_V07_TRANSACTION_AUDIT.md); coverage advances only with the entire introducing commit. This is a separate textual witness with strong same-event overlap, not automatically another unique fictional event.

| Component / identity | Actual inspection and limit |
| --- | --- |
| Primary source | BW-JP-V07/Drive1uczKmuZMDOV7-c5XuKFzhwDbt5PkW0n0/1045635bytes/SHA`1e367715dc5d6c58309452208258ba146cab73e1416ccbf5403ae8f5846e57c6`; OPFja/identifier syuuniitidokurasumeito007 |
| Native components | Cover viewed before fiction, all108paragraph anchors of item/xhtml/p-001.xhtml, original imagecolophon after story;3spines/2images |
| Additional navigation | Complete538bytes/SHAcfa771cdeefa1eff6b79a38b3c61d57fa31b5ac6d42a0330be8f96b4f3d46d1b; Navigation/Guide/coverlinks only, actually read |
| Colophon | Issue2025-08-20/author羽田宇佐/KADOKAWA/producer株式会社ドワンゴ(Dwango)/BOOKWALKER bonus; not fictional date or retail-binary certification |
| QA |70native material literal checks+35original LN correspondence checks PASS;0ruby; source/member/serializedparagraph/image/CRC/UTF8/outside-flow checks PASS |
| Locator/evidence | MapSHA`1e95b7ef89832da99979f6e4bf374b9f7c74338ed83fb466f4bc1572af9a05ae`; Drive17XVliD1tbuqQevhWnHPT_w8N2m6ef1Gk/40985bytes/SHA7667bf9792c365bd8ee0d685f7cf76df8c7f9a9b8108e6a2646a1e6d9aedcfd5/16members/upload-download/allhashes verified |
| Prospective records | Entry2026-10-17T17:31:53.267168+00:00/priorb08d809f/tenfullinputs/0fiction0images; F1prefix7344bytes/55p, F2prefix13079bytes/108p beforecolophon/navigation/C1; journal19995bytes/SHA`7166be84bdae51cb2b943ea866931a10f471b9ac7712d5476e07deed2e418564`/5observations/sealed2026-10-17T17:43:51.266283+00:00 |

O005/C1 strongly identifies the LN07morning: original LN06p00758–59 gives M September25/S August23 birthdays; LN07p01311 gives two-day interval andp49–96 matches the home/door sequence. The clock is September27 after summer break, no fictional year. SS adds M account/road continuation; original LN scope/omitted preapplication act/later evening remain separately routed. Existing R076 common-sense bargain is not duplicated or reopened as another adult entitlement. A shorter quote is no repeal of the qualifier.

Morning application, broken grip and a shared route begun are actual; no cat/aquarium visit/station or class arrival/actual lateness/truancy/next-day walk occurs inside this witness. Prior birthday use in LN07p01354 and current adult used-up/replacement history remain intact. Adult M/S-V09-EXIT unchanged; no new model test/formal forecast/V1/web/audio reading. SS3/18/available12/458 onlywholecommit; next **BW-JP-V09** automatically after exact source recovery. All remaining sources and architectural outputs persist; runactive/gateOPEN, I1 unchanged.


### BW09 actual component inspection — fourth external supplement

**SHUUKURA-TX-BW-JP-V09-20261017-A1** binds the [reading](../03%20Web%20and%20Supplemental%20Readings/SHUUKURA_V2_BW_JP_V09_DEEP_READING.md), four instruments/model-evidence addenda and [audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_BW_JP_V09_TRANSACTION_AUDIT.md); coverage advances only with the entire introducing commit. No distinctive same-event novel correspondence is established; limited lexical absence does not prove different continuity.

| Component / identity | Actual inspection and limit |
| --- | --- |
| Primary source | BW-JP-V09/Drive1zijopum5J62bvyK_qg4tKmBqbSsa1ZdR/803180bytes/SHA`300cf4532f744c790b1c5180f290752b36f59e3b5dc6f66629ad95cc58670329`; OPFja/identifier syuuniitidokurasumeito009 |
| Native components | Cover before fiction/all105nativeparagraphs/imagecolophon after story;3spines/2originalimages; entire image inventory matches viewed set |
| Extra navigation | Entire538bytes/SHA cfa771cdeefa1eff6b79a38b3c61d57fa31b5ac6d42a0330be8f96b4f3d46d1b; Navigation/Guide/two coverlinks, no fiction |
| Colophon |2026-05-20/羽田宇佐/KADOKAWA/producerDwango/BOOKWALKERbonus; not fictional date or retail-byte certificate |
| QA |68native+17original-context literal checks PASS/0ruby; source/member/paragraph/image/CRC/UTF8/outside-flow/completeimageinventory verified |
| Map/evidence | MapSHA`5878df47151083d1d7a95e33e5c92bd4cd427366e3b2e0fd555bf86b62187933`;Drive1FFOAO3-XeXVXdP-tVfVtqsO0R5Ig1JEA/43616bytes/SHA`0ed99ecc3b94d0ff2ff20c26649fd168dc873f4335ff69197996c341ff32ae6f`/17members/upload-download/allhashes/CRC verified |
| Actual freezes | Entry2026-10-17T18:21:46.968158+00:00/priorf62f8457/tenfullinputs/0fiction0images; midpointF1p1–65 includesSopening64–65, not beforeS;6984bytesSHA86a9b669d5e024f6d74c83584456fe89fd99b4190cab87c166ad73eb1ecaa8f2; F2all105p beforecolophon/C1,12464bytesSHAf8e3d3d3d7e92a889f747a8775b7cfecf8c1ae50042169c9e003219e383c986e |
| Original journal |17317bytes/SHA`6497fb180c0ec0d6851d45f2e4eae322d5e45687be966cf14af787914443d622`/5observations/sealed2026-10-17T18:26:10.245434+00:00; reading suffix verbatim; p64speakerM clarified outside seal |

Spring-break night23:21onward fits later university context, exact date/year and before/after relation to mainline late-Febendpoint unresolved. M/S-BW09-NIGHT separate from last precisely located M/S-V09-EXIT; no forced historical slot or dated successor. M game strategy and S conveniently qualified permission belief retain distinct access; strong-grip context, actual removal/push and accepted finite midnight condition coexist. Promise performance/sleep/oil/overnight unshown. Older plumeria meaning remains S-only; older Maika oil context does not identify an unshown current product.

All4BOOKWALKERavailable stories complete onlywholecommit; SS4/18/available13/458. No new model/test/forecast/web/V1/audio inspection; originalM0.13/S0.14 identities unchanged. Next**KSS-01** original multipart story automatically after exact source admission; coherent firstquarterSS5/18publication planned. All mandatory later duties/I1exclusions remain.


### KSS01 actual component inspection — fifth external supplement / first supplement quarter

**SHUUKURA-TX-KSS-01-20261017-A1** binds the [reading](../03%20Web%20and%20Supplemental%20Readings/SHUUKURA_V2_KSS_01_DEEP_READING.md), four instruments/supporting-role readiness/model-evidence addenda and [audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_KSS_01_TRANSACTION_AUDIT.md). One complete named story has two native parts and three PDFderivatives; these are not five separate source units. Whole introducing commit alone advances coverage.

| Component / identity | Verified actual inspection / limit |
| --- | --- |
| Preferred native witness | AUTHOR_RELEASE_CAPTURE-20261017-A1; part16→part17 exact I1; source-parts identitySHA`6d5ecea538edf8d5d2aa19f81d30ae252a9637bfe22ccd2945b097b126de3d4f` |
| Part16/前編 |11341bytes/SHA91efcad3253ecac9bf74ff2e946cb5aadb7b1565fa42757516998806ee13655c/43anchors26nonempty; complete original inspected |
| Part17/後編 |12267bytes/SHAbc0d46161fe0c234757963cef73a4ddd530282ba3e0c6d27a22bf348f15ac355/52anchors34nonempty; complete original inspected afterF1 |
| Maps |Parent native fullmapSHA57a97e968efa2bd77f8dace83618cbe35a06243c30bcd3d2ab5c106b50f67127;unitmapSHA`43bcfae392fd860727aad36c1ce327830b89641b2d0cadd414a7db8230a01610`; exact lxmlHTMLserialization, native IDs/ordinals preserved |
| UI/brand |Complete outside-story UI inspected/no extra narrative; author羽田宇佐/part revisions2023-02-13 19:18 and2023-02-22 17:37, not fictional dates. One unique platform-logo asset viewed; two later PDFpagebreak crops viewed, no narrative illustration/audio claim |
| PDFidentities |FINALDrive1vfAeEImXd4xiBppuh7dUMYMs94BgN_OC/745395bytes/e4a98c59e630d8c5a801094efe5bfb33c3e0b06d7bce80020da96367b5930e8d;SRC01Drive1Q07nGgkK6pOvpL-DKTScwqRjGfKs-1jJ/358990/d21fd43c740bd03c9e7d3227e9bdc2ce502710839044f7f09a257788d1d5605b;SRC02Drive1k7R7hTE_alXHmu1DKsG5ZoQUwDjhyNaq/363974/14a17b78cee284a9c1b8cf07333d8e29876cef402633c5eef22a7af3ef255a93 |
| C1qualified correspondence |26/26SRC01,33/34SRC02,59/60FINALcontiguous normalized nativeparagraph matches;17p39accounted across clipped/repeated final glyph and fixed UI/pagebreak. All60nonempty accounted, not60rawcontiguous or whole-text identity.8merged pages equal ordered4+4source pages in fulltext/renderedpixels |
| QA/C2 |95anchors/60nonempty/35blank,60materialnative checks firstpass/0ruby/hash/UTF8/bodyflow PASS;6originalLN08checks distinguish early Maika expectation and later direct gift interaction; no new heldout result |
| Evidence archive |Drive1BwKE9IGEw-MC0-J2bUzTG1t6eeY8zCSL/61843bytes/SHA`fb14022272c72fcfe74ab2c73deb8e9a680f9ffcb69026083f4aed3f1e139ca1`/20members/upload-download/allmemberhashes/CRC verified; no primary media |
| Freezes/journal |Entry2026-10-17T18:43:53.419090+00:00/prior386201e3/tenfullinputs/0fiction0images;F1firstpart7431bytesSHA530f37205108e41858af3a30fdbd82975d9aad55867fd8648a0620f34d2d576c;F2allnative13079bytesSHA9811d7787d4b14b2384195255d631e4b15e6b02c467d121b597d349e6745750c beforePDFcomparison;wholejournal18698bytes/SHA`c4298d93573aeafbf19d27ed98ad554d0209df4d8239cec3b3c8447ad74b07d6`/5observations/sealed2026-10-17T18:50:56.171068+00:00 |

Historical interval: springbreak before high-schoolyear3; exact date/year/ages unprovided. Maika narrates both parts. Honda's claimed sighting/service, speculation, Maika known uncertainty and later-reader contradiction are separately routed. M messages are actual; last alternate timing is typed, no explicit delivery/acceptance. No completed film/conversation/next-year roster, underlying M diagnosis, actual S restaurant work or objective popularity ranking. Native originals remain preferred; preview tokens stay private. Prior adult states and separately indexed BW09night unchanged.

KSS01completes SS5/18/available14/458 onlywholecommit; first supplement quarter publication is due through coherent BW07/BW09/KSS01tranche controls. Next**KSS-02**full original multipart story automatically; remaining13availableSS/431Kak/mandatorygaps/discovery/voices and all architecture outputs persist. No new model/test/forecast/V1/web/audio reading; I1unchanged, no future release admitted.


### KSS02 actual component inspection — sixth external supplement

**SHUUKURA-TX-KSS-02-20261017-A1** binds the [reading](../03%20Web%20and%20Supplemental%20Readings/SHUUKURA_V2_KSS_02_DEEP_READING.md), four ledgers, two historical model-evidence addenda and [audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_KSS_02_TRANSACTION_AUDIT.md). Two ordered native parts and three PDFderivatives are one complete named story, not five units. Coverage advances only in the whole introducing commit.

| Component / identity | Actual verified inspection and limit |
| --- | --- |
| Preferred witness |KSS-02/AUTHOR_RELEASE_CAPTURE-20261017-A1/宇都宮舞香の放課後/author羽田宇佐; frozenI1ordinal15 |
| Native part14/前編 |11918bytes/SHA371a4bb8a614fe077d14d150ba84375d1fe16d7a819e986f66ef753cdb704247/61anchors36nonempty, completely read before F1 |
| Native part15/後編 |12788bytes/SHAd97db4c11bea5ab408c5d45e6194e2f3033e7b9dfb3cb4dec12ec80956039fc9/67anchors39nonempty, completely read after F1 |
| Maps |Parts identitySHA467ac2166e241768c4c0f2c74a98d41822c0c40d656128ad452208d2a692f0a7;parentmapSHA57a97e968efa2bd77f8dace83618cbe35a06243c30bcd3d2ab5c106b50f67127;unitmapSHA`45dd908c7f248a9a3a9aa027b01ef7739eeb7f838a2eb56441931e8653fd9fcb`; exact native HTML serialization/ordinals retained |
| UI and images |All outside-story UI read, no extra narrative;2023-06-28 20:52/20:54revisions not fictional dates. One platform logo and two later PDFjoin crops actually viewed, no all-page visual/audio certification |
| PDFidentities |FINALDrive18CGDaIMD_Du-4LLH362zGlEMQeuMQByU/773422bytes/ab4fc7e3968aa1dc5904cb905465104d13b503d4d948189caedadb173ca62103;SRC01Drive1MfefmmwUr_8O8jhThZ0DLdQdR5pZ2p3E/357633/ab70eeaeeb1f24e614c5ed0fa966408201e738bf8c09d63093a1585bc0757091;SRC02Drive1PY-KYJHkTCStOS9QlhiDEDeqBL1V79ne/390445/99d74e75dc4cd01bf9639728dd65118b76f3e6842cca9f026e673476b4610162 |
| Qualified C1 |36/36SRC01,38/39SRC02,74/75FINALraw contiguous native matches.15p22exact two-fragment join across fixed UI; next-page header obscures line visually, no deleted/repeated narrative glyph. All75nonempty accounted;9mergedpages equal ordered4+5source text/pixels. No false75raw-contiguous or wholesale textual identity |
| Source QA and C2 |128anchors/75nonempty/53blank,75native checks first-pass/0ruby/hash/UTF8/bodyflow PASS;20original LN01–02checks/176serializedparagraph bindings. Exact practice question, Takahashi alias and perspective/access contrasts, no new heldout result |
| Evidence archive |Drive1N421XTKAnNizVpBri2Q-HpYGEUtrmCF1/78212bytes/SHA`2cb49638bcf4eb3d957d8f5ba80fd863a7214c9e57075961bbf75e416dc2aa4a`/22members, upload-download equality/all hashes/CRC verified; no primary media |
| Entering freeze |SHUUKURA-KSS02-ENTER-20261017-A1@2026-10-17T19:26:44.124558+00:00;prior28f178a2/ten full inputs/0fiction0images; later KSS/publisher/web/V1unread |
| F1/F2 |Firstpart5613bytesSHA d2e76e8a9d463f5fbe29e86f413a8758242cb5cf3f69a235d5ddb03d4d75c4b7 before allpart15; fullstory10601bytesSHA072ebf36d9b41451b1bfaf05dc4c123ccf989ea049d8a613150f76876dbcc419 before PDF/C2prose |
| Original journal |15660bytes/SHA`c34cd812f5f386b0a58f8b1dddb5adc3c522d3998b472b01dc5e15b62c169e48`/5observations/sealed2026-10-17T19:31:48.623946+00:00; exact reading suffix, no prefix alteration |

Historical placement is high-schoolyear3 at the sports-practice event aligned to LN02p003247; no exact calendar date. Maika narrates both parts; Ami has her own consequential speech/actions. M/S remain absent discussed subjects, with reader-only novel originals kept separate. Frequent interest talk differs personal consultation; voiced trust has private doubt; reported invitation refusals coexist with independent exam/cram costs. Maika's waiting is a unilateral decision with uncertain result, not a M promise. Ami's own weight disclosure and volume apology retain their actual subject/scope; stop/release is one bounded event, no general advance permission.

KSS02wholecommit alone advances SS6/18/available15/458; next**KSS-03**automatically. First-quarter priortranche28f178a2 source39062430164/house39062793268NO_OP/finalactualsource39062820445 allSUCCESS/full352tests; owner-nightly39063271917and mandatory ownerexplicitmain39063355408completedSUCCESS/main98ffb5d8/PR210/full352tests/trustedstatus/equalfulltree60173da7; first-quarter tranche CLOSED_ON_GREEN_MAIN. Every remaining source and architecture duty persists; I1 unchanged, no later release admitted.

BW07/BW09/KSS01 first supplement-quarter CLOSED_ON_GREEN_MAIN/PR210: source28f178a21cd0b68158f7d5fbb14cf56f528ab96b/main98ffb5d8a1488f211f2def8d84f478e15749765a/equalfulltree60173da745c72627c640a970db6b427929f995bd; source39062430164/house39062793268NO_OP/finalactualsource39062820445/owner-nightly39063271917/mandatory ownerexplicitmain39063355408 allSUCCESS/full352tests/trustedstatus/VERIFIED_OWNER_ONLY/merged_verified. Pushmain39063338489is separately successful and does not substitute for the mandatory dispatch.


### KSS03 actual component inspection — seventh external supplement

**SHUUKURA-TX-KSS-03-20261017-A1** binds the [reading](../03%20Web%20and%20Supplemental%20Readings/SHUUKURA_V2_KSS_03_DEEP_READING.md), four instruments, two historical model-evidence addenda and [audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_KSS_03_TRANSACTION_AUDIT.md). One author part, two processing ranges and two PDFderivatives remain one complete named story. Coverage advances only in the whole introducing commit.

| Component / identity | Actual verified inspection and limit |
| --- | --- |
| Preferred witness |KSS-03/AUTHOR_RELEASE_CAPTURE-20261017-A1/I1ordinal16/宇都宮舞香は下校する/author羽田宇佐 |
| Native part13 |13820bytes/SHA7ca55da8ec17303601d0397be5fc429785d2109c0a2b9654485025104c3c611d/78anchors45nonempty33blank; complete ordered inspection, no separate source units for internal ranges |
| Maps |Parts identitySHA835b5f8cca4accc5a96098f03a3f955323b069c63e4d949744eb4633312a08a4;parent native mapSHA57a97e968efa2bd77f8dace83618cbe35a06243c30bcd3d2ab5c106b50f67127;unitmapSHA`6f6f5fcd1138a2129a36a4955f91aa517d525271a0cd3c03c302f3a536263418`; exact HTML serialization/UTF8/ordinals retained |
| UI/images |Complete outside-story UI read/no extra narrative;2023-12-28 18:12revision and1573declaredcharacters are metadata. One logo and two join crops actually viewed, no all-page visual/audio certification |
| PDFs |FINALDrive1-p8aGaFr_wPHILRdhpU4RF_8wdj-N_3T/410849bytes/SHAabb9988dbea98387d3673d5ffaf1a0b76b6592fbc64c1c4ba49ba60b7606d7a7;SRC01Drive1qFLk-PMPmTtLc9UWzCo58irV9byvENey/396696/c10d9441578fb069608fb3ec7a698de139caefc4ad06bfde1632938d136a0b41 |
| Qualified C1 |Each PDF44/45rawcontiguous native matches;13p25exact prefix/suffix across fixed page UI, sticky header obscures next-page line visually. All45accounted without deleted/repeated narrative glyph or primary repair. All5FINALpages equal corresponding5SRC01text/pixels; binary hashes distinct, no wholesale native-text identity claim |
| Source QA/C2 |45native material checks first-pass/0ruby/hash/UTF8/flow PASS;18original LN03checks/65serializedparagraph bindings. Same event aligns OctoberHSyear3after final festivalday2/cleanup, no exact date. Private sender/destination and participant-known repair kept distinct |
| Private evidence |Drive1u0PPivSGqdxmeeEidzZwLBSdmByWj-g0/63075bytes/SHA`2b0575e87751164d5cc8e2c3f97432f00d965a5a0f4e589e81ed0b869e39c19e`/22members; upload-download equality/all member hashes/CRC verified; no primary media |
| Entering freeze |SHUUKURA-KSS03-ENTER-20261017-A1@2026-10-17T19:56:01.347978+00:00;prior da0ed6b4/ten full inputs/0fiction0images; later KSS/publisher/web/V1fiction unread |
| F1/F2 |First40anchors6032bytesSHAae493876a841bcbe253a8768bee1924a546a8dbe2437fa8e1ae55b4df75a19a6 before41–78; whole78anchors10597bytesSHA71c9c65773973232ba16bd30e89dc0a14b2f4622674f623f5b464b2699b6b6a2 beforePDF/C2prose |
| Original journal |16060bytes/SHA`8cc8ef23167bfa8e3ef08f4f5cb78c5d18a40c89c12b89e8788cbb1c234138ef`/5observations/sealed2026-10-17T20:02:09.890455+00:00; exact reading suffix, no prospective prefix rewritten |

Same previously registered REL-LN-JP-V03-007cancellation receives v2peer perspective and original apology/deferral, not a second occurrence. R150indexes its prior agreement/cancellation/postponement once; R151registers friends planned teasing with absent M uptake/performance unknown. Maika deliberate doubt management, conditional partner interest and bounded teasing desire differ from a universal privacy principle. Ami has her own roleplay and amusement agenda. Boyfriend彼氏/partner恋人/no apparent liked person are distinct propositions; female private contact does not automatically falsify no-boyfriend belief. Native omission of repair does not erase original participant knowledge.

OnlywholeKSS03commit advances SS7/18/available16/458; next**KSS-04**exact native parts11→12after unit admission. Remaining11accessibleSS/431parallelKak/290Narō/51knownmissing/27finite discovery/mandatoryvoices and all required synthesis/reconstruction/comparison/release duties remain active. I1unchanged, no later release admitted.

KSS02 CLOSED_ON_GREEN_MAIN/PR212: sourceda0ed6b45dfe429a12505cc5a0f11bb31171e007/maind1021d6d8e5e9551d4ef518f9a5bff6e3bf79b27/equalfulltree4cc841e7f336581c8a94178718908fcfd87f4a50; source39064502111/house39064890893NO_OP/finalactualsource39064923640/owner-nightly39065572812/mandatory ownerexplicitmain39065669252 allSUCCESS/full352tests/trustedstatus/VERIFIED_OWNER_ONLY/merged_verified. Successful pushmain39065651442did not substitute for the mandatory dispatch.


## KSS04 actual component inspection — eighth external supplement

**SHUUKURA-TX-KSS-04-20261017-A1** binds the [reading](../03%20Web%20and%20Supplemental%20Readings/SHUUKURA_V2_KSS_04_DEEP_READING.md), four instruments, two historical model-evidence addenda and [audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_KSS_04_TRANSACTION_AUDIT.md). Coverage advances only through the whole introducing commit.

| Component / identity | Actual verified inspection and limit |
| --- | --- |
| Preferred witness | KSS-04/AUTHOR_RELEASE_CAPTURE-20261017-A1/I1ordinal17/宇都宮舞香の懐疑心/author羽田宇佐; exact authorparts11→12, one story/transaction |
| Native parts | 11:11352bytes/SHA74f47c62990fdcf03f475fd8c3526e096d4a42d009656b7945a50a80d1f2cb53/49anchors;12:12163bytes/SHAca04abd798340b0f216591bf2076903fe099d9b934fd2e09a7a6ee9a0780b707/70anchors;119total68nonempty51blank |
| Maps | Parts identitySHAe61e5ea57639a0b325afd86d8fca7d8b6b1cdbe115a31f6ee2ed065fb58361ab;parentmapSHA57a97e968efa2bd77f8dace83618cbe35a06243c30bcd3d2ab5c106b50f67127;unitmapSHA`9281e6b4619c960e90a90c587f7e68e07188719aef46f9981ebf5d494e68e558`; exact serialized paragraph hashes/UTF8/source order retained |
| UI/images | Both complete outside-story UIs read,2024-04-29 18:18/18:20revisions/991+1088declaredchars are metadata; one logo actually viewed, no full-page visual/audio certification |
| PDFderivatives | FINALDrive1_eLyVaWGIM-9k2UtyZoqtJomEfLKZpeb/745881/SHA19d96fbecbffc9ede8af77bd8063264f1a701c54a25b5f937c07462286c8ad48;SRC01Drive13sdx9LKIooFH8h-AwUKjw5H_nEi8Robr/348113/06aeb036b138624b3a7e4d61a26ea7f67b49dedf6627a84fce85d7f56bae8b5c;SRC02Drive1qthxLSor3Zh1B5vehQOLPPFbBEB8xasI/372377/5c739880fb13902ab249284222f1252582ae70ed1f425fa37108c5c622e7b6b0 |
| C1 | 68/68FINAL,27/27SRC01,41/41SRC02ordered rawcontiguous normalized nativeparagraph matches;9FINALpages equal ordered4+5SRCfulltext/pixels. No discrepancy/repair; binary/whole-document native-text identity not claimed |
| Source QA/C2 | 68native material checks first-pass/0ruby/hash/UTF8/flow PASS;52original LN03–04checks/284serializedparagraph bindings. Existing November transfer, Mprior bare-contact knowledge and later winterbreak apology distinct; exact classroom date inferred/unprovided |
| Private evidence | Drive1XNNlrDaGiR3LoTon3ZBGFNVdhsKx7uNe/89516bytes/SHA`1b9f68034ffab39a5abad7a4e6db68ad7fefd36d28b99750bb280d99a7229cda`/22members; upload-download exact/member hashes/CRC verified; no primary media |
| Entering freeze | SHUUKURA-KSS04-ENTER-20261017-A1@2026-10-17T20:35:41.027830+00:00;priore3603f3a7a818f4ae4313fe42acfb0df844d6192/tenfullinputs/0fiction0images; laterKSS/publisher/web/V1fictionunread |
| F1/F2 | Firstpart49anchors/7047bytesSHAe440f96f759a4383f2dbedceafb9969287e6b4491f70c1062d1028a8120bb515 beforeALLpart12; whole119anchors/13287bytesSHA83a2a603812633146edf7c4f061d59c665bcac9f43c95becba2985216926d0af beforePDF/C2prose |
| Original journal | 19497bytes/SHA`0f8e976bd7ed3f029185385ffcca4bc29a437673e594f7af8547eba306dacc36`/five observations/sealed2026-10-17T20:40:06.157034+00:00; exact reading suffix, both prospective prefixes preserved |

Mknows the earlier Maika/Scontact; university contents, not bare contact, remain withheld at SSexit. Maika private regret/deferred apology differs later actually performed LN04repair. Mown-recipient claim differs actual Squalified knowledge and Amisecret framing. Existing REL-LN-JP-V03-018/REL-LN-JP-V04-005get contextual versions, not duplicate occurrences. No new model/test/heldout success; adult states and all previous prospective freezes retained.

OnlywholeKSS04commit advances SS8/18/available17/458; next**KSS-05**exact native part09/ワニの憂鬱. Remaining10accessibleSS/431parallelKak/290Narō/51knownmissing/27finite discovery/mandatoryvoices and every reconciliation/monograph/specialist/reconstruction/V1comparison/integrated/adversarialrelease duty remain mandatory. I1unchanged, later releases excluded.

KSS03 CLOSED_ON_GREEN_MAIN/PR213: sourcee3603f3a7a818f4ae4313fe42acfb0df844d6192/main6197361b2d88a30f7cd9ce9bfab13b5f1827d802/equalfulltree9a4fb8096595c7c7662ad7bc9561d2987d80d3d6; source39067311514/house39067607805NO_OP/finalactualsource39067637207/owner-nightly39068170249/mandatory ownerexplicitmain39068262873 allSUCCESS/full352tests/trustedstatus/VERIFIED_OWNER_ONLY/merged_verified. Successful pushmain39068246067 did not substitute for the mandatory dispatch.


## KSS05 actual component inspection — ninth external supplement

[Reading](../03%20Web%20and%20Supplemental%20Readings/SHUUKURA_V2_KSS_05_DEEP_READING.md) and [audit](../08%20Audits%20and%20Handoffs/SHUUKURA_V2_KSS_05_TRANSACTION_AUDIT.md) bind the entire unit transaction and separate attributable routing correction.

| Component | Verified state and limitation |
| --- | --- |
| Authority/run | Epoch1/GIT_ACTIVE_ACCEPTED; method/architecture/reconstruction0.2; continuous_sequential/active/startLN01/terminalI1plusalloutputs/gateOPEN |
| Exact unit | KSS-05/AUTHOR_RELEASE_CAPTURE-20261017-A1/I1ordinal18/ワニの憂鬱/author羽田宇佐; native part09,11892bytes/SHAe274756c998e901365b6aacc285e7467f22596ee9b94dbec4d5d652ea8c53e12;50anchors29nonempty21blank |
| Maps | Parts identitySHA5fc4ce96caba08aad2f36384de1c497b47796372c13ef7887f672e30b296e06f;parentmapSHA57a97e968efa2bd77f8dace83618cbe35a06243c30bcd3d2ab5c106b50f67127;unitmapSHA8a416b4f90945ca1b779679a8c14b6424c8eeabbcd45abe757571354ee2effe6;exact native serialization/order/0ruby/29literal checks PASS |
| Native/metadata | Complete preferred author-release native read;1191declaredchars/revision2024-10-27 20:16 are metadata. Native p37 apparent missingで preserved, no correction |
| C1 | 25/29rawNFKC contiguous matches in each derivative; two comparison-only glyph folds→28/29, p41 reconstructed from documented split/29-character overlap. All4FINAL/SRCpages equal full extracted text/pixels; actual bottom clipping/sticky header qualified, not full visual readability |
| Actual images | One platform logo before fiction; four postF2glyph/pagebreak crops actually viewed with exact locators/matrix/hash. No narrative illustration/full-page visual/audio certification |
| C2 | LN04p0141–60,108–137:28literal checks/90serialized bindings;137total anchors. Strong postgraduation/pre-university packing-phase correspondence, exact instant/date unestablished; object inference not human inner access |
| Evidence | Drive1dS5RjfMecaJajSjoCY5XY5y5rFUfh-LG/64365bytes/SHA6c29c6fbb4221405ba582e634551d330ef8fc77ef8512f236ea511a8dd70d5f9/24members; upload-download/memberhash/CRC PASS; primary media excluded |
| Entry/frozen journal | SHUUKURA-KSS05-ENTER-20261017-A1@2026-10-17T21:02:10.408253+00:00;prior9e81ac8834b1f43eb6ca1c205c1dc9f4ff278217;tenfullinputs/0fiction0images; Q116113bytes/SHAad598cd7d1186d017dde03fd43eb632c1c8cc59e94602ab81698023817a34f55@2026-10-17T21:11:39.775057+00:00;first25/whole50prefixes unchanged |
| Historical exit | Crocodile still boxed; accepts Shiori choice, resents lost watching time, considers care alternative, wants comfort. M-KSS05-PACKING-IMAGE/S-KSS05-ATTRIBUTED-CAUSE remain source images; no human dialogue/hearing/new rule/actual comfort/unpacking/arrival |
| Material delta | 2human-image events/2historical projections/2readiness;4relationshiprows(3new+1older)/3directions/no new or older-rule versions;14propversions(2older+12new)/12access/5tensions;1older source claim+3new and separately2routing-correction versions.108claims/414forms/484props/153rules |
| Correction | ERRATUM-KSS-05-001 restores housing04005.v6 and existing privacy05001.v6. v5 and frozen references preserved with explicit redirects.54LN09older-claim identity pairs screened/onebreak/53routes preserved; not full semantic reacceptance |
| Correction provenance | Separate postQ1 LN09sourceSHA3201ae3ffd1230a526dd5d9a184d4a76ab7aff4a7b244160cbfc886acbb8086a/mapSHAe3355f5468a51f857a0a3e5cf22658fe5ca8313bda17c4e1c21d2cc94f2496fe;29checks/94bindings. Drive1jPfqrZ-YBItGzDXZb4idOJ_-OH4vAZbf/28459bytes/SHA08662e0d6c186bcd3a68fc026a8fbe3fd3320565ff19c301a9d651ef9001a53b/4members exact readback/CRC |
| Reconstruction | Original M0.13/S0.14adultfit/time/UNTESTED/noncurrent prefixes and all13attempts/18forecasts unchanged. No new operational packet/test or validated domain; object rhetoric not human speech sample |
| HWM/next | Only wholeKSS05commit advances LN9/9;SS9/18;KakNONE0/431;NarōNONE0/290;available18/458. Required SShalfway publication. NextKSS-06/I1ordinal19/黒猫の期待/nativepart10/69anchors after exact admission; no ordinary confirmation |
| Boundary | I1JSONSHA6e78ec763843f0617a178ac8a8696e799cf2654b55a28d4011595459fe47c42b;ordered458digest2e62f9bd57dd8f65a036d689917df36847affd7fc1d1f6a70dd85f6121da6b95. LN10/later releases excluded |
| Remaining | 9accessibleSS/431parallelKak/290Narō/51knownmissing/27bounded notices/mandatoryvoices and all dedicated reconciliation/monographs/roleaudit/specialists/reconstruction/V1comparison/integrated/adversarialrelease remain mandatory |
| Prior publication | KSS04 CLOSED_ON_GREEN_MAIN/PR214:source9e81ac8834b1f43eb6ca1c205c1dc9f4ff278217/maincce4eb7cb02867112afbe1b40fd17c074a666df2/equalfulltree421b0ee8879122f9719f0691723efb1a76616fe9;source39069161640/house39069396732NO_OP/finalactualsource39069422346/owner-nightly39069838269/mandatory ownerexplicitmain39069935058 allSUCCESS/full352tests/trustedstatus/VERIFIED_OWNER_ONLY/merged_verified. Successful pushmain39069912902 did not substitute for the mandatory dispatch. |

Only the whole introducing commit advances coverage; source inspection and drafted prose are insufficient. Frozen inventory unchanged; new releases require later admission.
