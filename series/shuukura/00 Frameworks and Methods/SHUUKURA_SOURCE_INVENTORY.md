---
title: "Shuukura V2 — source inventory and witness architecture"
artifact_id: SHUUKURA_V2_SOURCE_INVENTORY
artifact_type: source_inventory
series: "Shuukura / 週に一度クラスメイトを買う話"
series_id: shuukura
generation: SHUUKURA_V2
version: "0.2"
status: active_provisional
scope: "Exact acquired source identities, edition boundaries, supplemental provenance and future inventory freeze"
source_boundary: "Bootstrap and kickoff source preparation; zero V2 narrative units admitted or close-read"
canonical_home: series/shuukura/00 Frameworks and Methods/SHUUKURA_SOURCE_INVENTORY.md
created: "2026-10-17"
planning_date: "2026-10-16"
review_status: EXECUTION_KICKOFF_BLOCKED_BEFORE_ADMISSION
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Source inventory and edition/witness architecture

This is the canonical source-and-coverage home. Snapshot: **2026-10-17 UTC; initial planning date 2026-10-16**. No narrative unit is admitted or analyzed. Counts below are inventory and structural observations, not literary coverage. This metadata snapshot is **not an authorized run inventory freeze**.

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
| Admitted analytical coverage | Authorized unit transaction and accepted evidence/interpretation | Zero; CLOSED lock |

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

The supporting [candidate identity snapshot](SHUUKURA_V2_KICKOFF_CANDIDATES.json) binds the re-enumerated acquired objects, complete ordered Kakuyomu identity list and subsequent preparation objects. It is an inventory component, not another current-state surface. Snapshot SHA-256: `78e4987eb085e5d037a334706744b5bc60ea0d26296d6fe8f0f236f83de6b9e8`. Its bootstrap expected hashes are explicitly distinguished from newly reverified bytes.

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

V07 and V08 were also independently rehashed against the existing register and passed ZIP CRC. Their native colophons `item/xhtml/p-colophon.xhtml` assert electronic `ver.001`, with issue dates August 20, 2025 and December 19, 2025 respectively; V08's print basis is December 20. Both assert Japanese text only, while received OPF `dc:language` remains `zh-CN`. A full-spine XML-text probe including ruby/paratext counted 79,503 / 97,009 kana and 3,793 / 4,857 paragraph elements. Those counts use a different scope from the bootstrap probe and are not narrative reading or full fidelity certification. Received bytes and language tags remain unchanged. Conversion provenance still requires resolution.
