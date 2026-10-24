---
title: "Cornered Mouse — Source and Scope Map"
artifact_id: CORNERED_MOUSE_SOURCE_AND_SCOPE_MAP
artifact_type: source_scope_map
series: "The Cornered Mouse Dreams of Cheese / 窮鼠はチーズの夢を見る"
series_id: cornered-mouse
generation: CORNERED_MOUSE_BOOTSTRAP_V1
version: "0.1"
status: active_provisional
scope: "Canonical work, edition, component and evidence-availability map"
source_boundary: "Japanese manga continuity; AIO2020 structurally checked; no narrative admission or reading"
canonical_home: series/cornered-mouse/00 Frameworks and Methods/CORNERED_MOUSE_SOURCE_AND_SCOPE_MAP.md
created: "2026-10-24"
review_status: OWNER_BOOTSTRAP_AUDIT_PENDING
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Source and scope map

This is the single project source/scope authority. Verification date: 2026-10-24. Narrative admission is **NOT_ADMITTED** throughout. See the [entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md) for operational permission.

## Work identity and bibliographic witnesses

The reading order is 窮鼠はチーズの夢を見る, then 俎上の鯉は二度跳ねる, both manga by 水城せとな. English titles are *The Cornered Mouse Dreams of Cheese* and *The Carp on the Chopping Block Jumps Twice*. Japanese 二度 / ２度 and romanization variants are aliases, not new works.

| Edition key | Bibliographically established identity | Availability in the bounded source folder |
|---|---|---|
| JP-JC2006 | January 2006 first collected title work, Shogakukan Creative | Not located |
| JP-FCA2009 | May 2009 新装版 title work plus sequel, Shogakukan; original-form editorial category | Neither separate book located |
| JP-AIO2020 | Revised All-in-One combining both works and Hummingbird; publisher digital release 2020-04-10, JDCN `098710360000d0000000` | One EPUB byte-checked below |
| JP-RB2020-A / B | Two Reboot Editions, announced for 2020-04-10; separate ISBN identities | Neither located |
| EN-SS2019 / EN-SS2020 | Seven Seas, 2019-11-26 / 2020-02-11; ISBNs `9781642757590` / `9781642757606`; translation Jocelyne Allen | Neither located; textual/visual edition relationship unverified |

[Mizushiro's edition comparison, 2020-03-20][B01] distinguishes the 2006 collection, the 2009 新装版 issued alongside the sequel, and the two 2020 edition types. The 2009 title work adds 鼠、袋小路で考える, absent from 2006; 新装版 does not mean the later revision. The All-in-One combines both principal works and Hummingbird; Reboot is described as print-only. These are bibliographic findings, not evidence of acquisition. The [publisher's digital record][B03] explicitly identifies the All-in-One principal works as revised. The cached source's colophon carries ISBN `978-4-09-871036-2` and a first-print issue date of 2020-04-15; this is distinct from the publisher's release date and does not establish the digital file's acquisition date.

The official English [title-work record][B04] and [sequel record][B05] establish the pair's identities and translation credit. Their summaries motivate open methodological questions only. No synopsis-derived behavioral or ending claim is admitted.

## Canonical evidence and provenance

The evidence-root README (Drive Doc ID `1K5p3nbvCyNIkHrGID7iIp6KWx_k_yMZstEa6udHks1g`) and live series inventory (Drive Doc ID `1bfPi00AKmELjeXmdCudU_4HqOknTIOODANEi12GDJFw`) route the series evidence folder (Drive folder ID `1WXDzO2vyHsVtI76FoZlwCZsaNOg8MunI`). Complete direct-child listing returned one EPUB and three provenance files. No unrelated Drive collections were crawled; absence here is not a claim that the owner has no other copy.

| Local reference key | Canonical Drive object | Observed role / integrity |
|---|---|---|
| `CM-JP-AIO2020` | EPUB (Drive file ID `1lGL_hglSMP9EqNLLkdSCKRubf7VXzjO0`) | 109,599,529 bytes; retrieved SHA-256 `ce389cb785a37f6b271065c33a177bd8c9a62428e5c3c58c6bf2be756822b617` |
| `CM-PROV-IMPORT` | calibre_import_manifest_2026-09-28.json (Drive file ID `1BT4oZaMwfMvdFCS5lHD57bq9bUBdosFf`) | Retrieved SHA-256 `ebef7ccfe66c8ce318487d823ea6682cb12de66d6adb9efe544ab7dc729ebac0` |
| `CM-PROV-PROPAGATION` | drive_propagation_manifest_2026-09-28.json (Drive file ID `1ZkL3K82URe9iYoN0iUZBw5fdIWc9uX7k`) | Retrieved SHA-256 `9b12f3da93c7c021f703cd0b93c9d8ae69550601529a91e30c39c7958e3a24d8` |
| `CM-PROV-NOTE` | CALIBRE_IMPORT_2026-09-28.md (Drive file ID `1RRbiWCkvYy2G8uQFBMF5tJgU9AVkTIWU`) | Readable import/verification note consulted |

The import manifest identifies Calibre item 107, preserves Japanese metadata, and reports a local import from the owner's Calibre library. It records the owner's general Kobo-purchase account while explicitly saying individual receipts were not inspected. The propagation manifest binds the source hash, byte size, edition and exact Drive ID. This bootstrap independently retrieved that object and matched its SHA-256 to both records. Provider metadata did not expose a checksum through this connector; the verification rests on downloaded bytes, not a claimed provider checksum or proof of individual purchase rights. Private paths and acquisition records remain external.

## Verification ladder and technical structure

| Level | `CM-JP-AIO2020` status |
|---|---|
| Bibliographically identified | Yes: author/publisher, Japanese title and edition |
| Listed in inventory | Yes: root inventory and dated series manifests |
| Located in Drive | Yes: direct listing plus exact-ID metadata/parent read |
| Bytes retrieved and integrity checked | Yes: full download, byte size and SHA-256 match |
| Internal structure verified | Bounded: ZIP CRC, mimetype, container/OPF, all manifest resources, 539 ordered XHTML/image pairs, image decoding; no full EPUBCheck claim |
| Narrative content inspected | No; zero narrative images viewed or OCRed |
| Explicitly admitted into sequential analysis | No |

The source has 1,086 archive entries, `item/standard.opf`, 539 spine entries and 539 distinct referenced JPEGs, all 847 × 1200 pixels, right-to-left progression, and no encryption descriptor. Embedded title, author, language (`ja`) and publisher agree with the declared source; UUID is `743805db-b45d-4117-bb89-3e29b824bacc`. These counts include covers/paratext and are **not** a narrative page count or completeness certification.

The existing source-side `bookwalker_capture/bookfab_ocr/epub_source.py` read-only `open_book` interface successfully parsed all 539 pages with no structure findings, alongside the independent container probe. Existing Calibre import/page-comparison tooling also owns import verification. No new generic acquisition framework is needed. Page extraction and local image viewing worked for the contents and colophon; narrative lettering/panel legibility must still be checked within an authorized unit. OCR quality is untested and OCR cannot replace image inspection.

Only two non-narrative images were visually read: `item/image/i-0008.jpg` (contents, spine 10; SHA-256 `068ec8b67e4d44bb8b6a9203948a8b04495c84b718a3cc1990df368316516ff9`) and `item/image/i-0535.jpg` (colophon, spine 537; SHA-256 `27ef3b34416b5011d3378119e9b754f757383d79f6e2b01b454fb5b440228972`). Navigation exposes cover/contents/colophon anchors, not a complete chapter graph. The contents labels below establish announced starts, not verified narrative page boundaries.

## Component candidates and four orders

For this witness, the proposed atomic unit is a **chapter or separately titled collected component**, including short interludes. A complete volume is not presumed to be one transaction. Keys are project identities; each future witness needs its own page mapping. None of these units has been admitted.

| Candidate | Contents label | Printed start shown in contents | Collection group / proposed disclosure |
|---|---|---:|---|
| `CM-U01` | キッシング・グーラミー | 009 | Title work, first |
| `CM-U02` | 楽園の蛇 | 049 | Title work, second |
| `CM-U03` | 黒猫、月を見る | 090 | Embedded short, third |
| `CM-U04` | 黒猫の冷えた指先 | 095 | Title work, fourth |
| `CM-U05` | 鼠、袋小路で考える | 136 | Embedded short, fifth |
| `CM-U06` | 窮鼠はチーズの夢を見る | 141 | Title work, sixth |
| `CM-U07` | 憂鬱バタフライ | 203 | Sequel, seventh |
| `CM-U08` | 黒猫、あくびをする | 254 | Embedded short, eighth |
| `CM-U09` | 梟 | 259 | Sequel, ninth |
| `CM-U10` | 俎上の鯉は二度跳ねる | 337 | Sequel, tenth; internal closing substructure unresolved |
| `CM-PARA-AFTERWORD` | あとがき | 498 | Paratext; not narrative admission |
| `CM-S01` | ハミングバード・ラプソディ | 501 | Later supplement, separate post-mainline admission |

SPECIAL COLORS is listed at 002; it is uninspected illustration/paratext material. Component end pages, opening-page identity, missing/duplicate pages, and the boundary of the original sequel's final closing material are **unverified**. Do not infer an end as next start minus one or equate a filename number with printed pagination. Before each unit, reconcile a bounded structural range without consuming later narrative; splitting a long titled component needs an explicit prospective checkpoint plan before reading it.

Publication order is separately recorded by edition and first-publication evidence, not inferred from this collection. [Mizushiro's January announcement][B06], corroborated by the [publisher's magazine record][B07], identifies Hummingbird in *flowers* March 2020, released January 28, before its All-in-One collection. Individual original chapter serialization dates remain unresolved.

[Mizushiro's Reboot announcement, 2020-03-20][B02] identifies wording changes and visual revisions, and places the two parts of 黒猫、海へ行く in the title-work and sequel Reboot books respectively. The edition comparison identifies the parts as 1日目・夜 and 最終日・明け方. Both remain unavailable here; no complete Reboot coverage is claimed. The author gives story chronology as sequel ending → Hummingbird → Black Cat two-part story → original sequel's カシスオレンジ closing material. This is an authorial chronology account, not inspected narrative evidence or permission to rearrange the original closing sequence.

Thus physical Reboot placement would expose a late short in book one, while the intended analytical disclosure keeps it after the frozen mainline and separately admitted Hummingbird. AIO collection order and chronological placement are not interchangeable. Later supplements can belong to manga continuity while remaining barred from earlier prospective knowledge. Do not infer noncanon status from late publication. No exhaustive all-extras claim is made; additional discovered manga must be identified, mapped and reviewed before admission.

## Edition choice, conflict rules and admission

Recommend `CM-JP-AIO2020` as the practical **available candidate** for a revised-edition Japanese pass. Owner review must accept that basis or defer selection pending a verified original-form 2009 pair. That pair is a useful comparison strategy, not an available witness. Reboot should supply its exclusive short and identified editorial variants if later available; official English can support wording comparison after identity/coverage checks. No definitive primary witness is selected at bootstrap.

Evidence retrieval uses the stable Drive IDs above through the connected Drive metadata/fetch tools; these identify evidence objects, not migrated analytical artifacts. Every claim must bind its actual witness. A byte change requires a new witness key and preserved prior digest; never replace the bytes behind an existing source identity silently. Record an edition variant as `(original locator, revised locator, observed difference, interpretation impact)`; record translation disagreements with Japanese text, English witness and locators separately. Do not silently harmonize images, wording, pagination or chapter order. Author commentary can explain an editorial operation but cannot replace direct comparison or outrank the manga on motive. Adaptation events, endings, performances and dialogue remain outside this continuity.

Before admission: owner-approved witness and bounded unit/run; fresh exact-ID retrieval/hash check; component starts/ends and physical-to-spine mapping; legible page inspection route; missing/duplicate/resource audit; prospective entering freeze and disclosure quarantine; current eligible method/architecture and four ledgers; truthful OPEN lock and authorized continuation fields. Record evidence obligations as required/optional/out-of-scope and pending/partial/complete-for-declared-scope. Availability, technical parsing and source admission are separate states.

No full source images, extracted dialogue corpus, raw acquisition manifests or cache files enter Git. Git retains these public-safe IDs, hashes and interpretive routes; Drive owns evidence, and local working copies confer no authority.

[B01]: https://www.mizushilog.com/『窮鼠はチーズの夢を見る』オールインワンエデ/
[B02]: https://www.mizushilog.com/『窮鼠はチーズの夢を見る』『俎上の鯉は２度跳/
[B03]: https://shogakukan-comic.jp/book?jdcn=098710360000d0000000
[B04]: https://sevenseasentertainment.com/books/the-cornered-mouse-dreams-of-cheese/
[B05]: https://sevenseasentertainment.com/books/the-carp-on-the-chopping-block-jumps-twice/
[B06]: https://www.mizushilog.com/『窮鼠はチーズの夢を見る』書き下ろし読み切り/
[B07]: https://e-comi.shogakukan.co.jp/books/09Y750030000d0000000
