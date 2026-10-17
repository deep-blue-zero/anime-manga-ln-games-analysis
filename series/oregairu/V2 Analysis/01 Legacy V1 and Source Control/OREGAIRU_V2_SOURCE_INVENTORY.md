---
series: OREGAIRU
artifact_type: source_inventory
scope: V2_ADMITTED_SOURCE_IDENTITIES_AND_AUTHORITY
generation: V2
status: canonical
lifecycle: active_mutable
source_boundary: Existing admitted Japanese mainline V01-V14.5, story-qualified official anthologies, already-audited bonus-booklet genealogy, and Christmas drama/prose source identities; inventory verification does not admit unanalysed stories or expand fictional continuity
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: '2026-10-16'
verified_as_of: '2026-10-16'
verification_scope: Byte identity and specified container/metadata checks; no complete textual recollation, fresh audiovisual review, or new sequential reading
---

# Oregairu V2 — Source Inventory

## 1. Authority, ownership, and verification coverage

This inventory consolidates source identity and source-form authority. The [registered corpus map](../07%20Archive%20and%20Manifests/OREGAIRU_V2_DRIVE_CORPUS_MAP.md) remains the single current-state entrypoint. The [analytical method](../00%20Frameworks/OREGAIRU_V2_ANALYTICAL_METHOD.md), [architecture](../00%20Frameworks/OREGAIRU_V2_MULTI_DOCUMENT_SYNTHESIS_ARCHITECTURE.md), [primary locator ledger](../04%20Checkpoints%20and%20Longitudinal%20Ledgers/OREGAIRU_V2_PRIMARY_SOURCE_LOCATOR_LEDGER.md), and [Document 12](../05%20Specialist%20Synthesis/12_SUPPLEMENTARY_VOLUMES_DRAMA_CDS_AND_ORDINARY_LIFE.md) retain their existing methodological, narrative-authority, chronology, and interpretive responsibilities. This inventory does not supersede their literary findings. The two attributable source-record errata in §8 govern the identified hash and availability defects only.

The source root was enumerated live on **2026-10-16**: `1DX8dpvD2ZPtvaL1ogw7W5RIiwD5eLSXf`. It contains 24 EPUB payloads (18 mainline/.5, four anthologies, and two excluded `結` volumes), the historical collection manifest, and a PDF folder. This is the enumerated project source tree, not a claim to have searched all owner storage or to possess every Oregairu publication.

| Witness group | Fresh verification on 2026-10-16 | Retained or unperformed work |
|---|---|---|
| 18 mainline/.5 EPUBs | All downloaded; SHA-256, bytes, ZIP CRC, mimetype, XML parsing, OPF manifest resources and spine references checked; all pass and match the historical collection manifest | No second sequential reread, exhaustive first-print/electronic textual collation, or fresh decoding review of every image |
| Four anthology EPUBs | Same byte/container checks; all pass and match the historical collection manifest | Existing story-level chronology dispositions retained; Anthology 02 OCR remains qualified and its page images govern exact text |
| 17 governing mainline/.5 PDFs | All downloaded; byte hashes match the corresponding frozen deep-reading receipts; `pdfinfo` page counts recovered | No full fresh rendering or textual recollation; previous visual inspection remains historical inspection |
| Alternate two-page V7.5 PDF | Fresh byte hash, size, and physical-page count recorded | Not selected as governing pagination; equivalence with the governing single-page scan has not been freshly collated |
| 6.25/6.50/6.75 single-page ancestor PDFs | All downloaded; byte hashes, sizes, and physical-page counts match the V6.5 deep-reading receipts | Genealogy-only authority retained; omitted stories have not thereby received a new substantive reading or independent state admission |
| Christmas drama: ten MP3s | All downloaded; hashes match the existing drama deep reading and `ffprobe` durations agree to its displayed precision | No fresh listening, synchronized performance review, or verbatim audio transcript claimed |
| Other CD packages, alternate two-page 6.75, artwork/booklet subfolders | Live metadata/folder presence inspected as specified below | Payload hashes, delivery analysis, exhaustive artwork inventory, and any new authority admission remain unperformed |

The historical `Oregairu - Collection Manifest.txt` is Drive `1OViEPnWcCeVasnCWYwRwC9CGZeS7AQXV`, generated 2026-08-12 and updated 2026-08-15. Its readable contents were reopened for this reconciliation; this inventory does not assign an original-byte hash to the connector's readable projection. Its historical acquisition paths and extraction workspace are not republished here. Its August publication-availability statements are date-bound and must not be read as current October acquisition status.

## 2. Mainline Japanese EPUB witnesses

All eighteen books are by **渡航 / Watari Wataru**, illustrated by **ぽんかん⑧**, published by **小学館 / Shogakukan**. The governing source is the actual hashed electronic edition, not an assumed byte-identical first printing. Source filenames follow `Oregairu - Volume NN[.5] [Japanese].epub` exactly. Decimal volumes require the story chronology rules in §4.

Every hash in this table is a fresh SHA-256 of the complete fetched file, independently reconciled to the historical collection manifest. The deep reading for `NN[.5]` is `03 Volume Deep Readings/OREGAIRU_V2_VNN[_5]_DEEP_READING.md` under this same V2 root; its §1 and source-locator sections remain the route for earlier inspection, print/electronic differences, and scene recovery.

| Volume | Drive file ID | Bytes | Spine items | SHA-256 |
|---|---|---:|---:|---|
| 01 | `1b8MmyI1oFnwVubXOaI7fcJKPzDCAsCSz` | 8,861,594 | 47 | `a42934256694a6890791b63713f2c7ad3f8aeeb82f43a860f77f48288e564271` |
| 02 | `1txcGrDcsxatiQQov5Yg6FdhOblqVFz-q` | 1,802,434 | 43 | `d0cfe91780f75b6c3d8f5b5d4ceef9ef39cecb2097ed787ec1e1b99df032f624` |
| 03 | `1tQmnFex5JWv2PsoTR-0tnSqNWRaHAuCk` | 1,873,774 | 41 | `b4a8b1c2493dc9278d18252e5729d58079b51ff2f44e319e57e31f01326b6325` |
| 04 | `1680hv2-eXPwB6zxLx01vfrcogCejkKLr` | 9,426,008 | 47 | `cf4ab65c52815cd3d4763122054e11b1c7364c9d4810de722f2f26f9cd758d62` |
| 05 | `12d9wE7pkzfumEopm4Sgo54Et0DD9HaLy` | 1,733,278 | 42 | `23d4ab66b8b364e8e513f8efda6ea3da3a22538f42563a2cebb21f4548a09e29` |
| 06 | `1r7mh1-YCOZnGCsLZs8e2nJ6iwJsPY4n7` | 1,596,762 | 47 | `edede8423a7547b56855e0d5f13e70313072d3d236cd152c1d495079d3540989` |
| 06.5 | `1lNjwvTC5kjZCwMqdZFCxDE0Eozd8bNW-` | 1,349,152 | 40 | `bf8cbf94699f11d21233fd417e1e20bbad39a42d68eedd47358c706dedeb6bb2` |
| 07 | `19zITw1piseFl6UaX0UHvY53pvsTCA0ah` | 2,192,182 | 45 | `0fdab575b81352f02849f9181553874af03578fd4580f975c41e9e00f0a7fbf7` |
| 07.5 | `1jonTlBLuvYCSpN3mdzRbOFIpjFVpEDCL` | 1,719,884 | 35 | `092ed6998c1cbc16f9b2ffb5842690944bb09484534b876a597d5586274be31b` |
| 08 | `12GwpSkLd8-g-XCbdU6wK_Ne67NK654b-` | 5,487,909 | 36 | `44b65ca272039c0b6230331fdaacbe8af99111315e161463a0eaef6ea2a61312` |
| 09 | `1GwPO8tolUmpZetUvZ0JSf0fmjUvGDgM_` | 6,274,082 | 39 | `b1f652a331813438477fc5ffe8142a62bc1d30466d6799412fbc116b5492c469` |
| 10 | `1mQn3xHxkWrpl8DC1O46xutOIy2GJW5Bq` | 1,419,329 | 36 | `08c8bb6de45f8e6ab5cd2382ff947726ffd6bdea91aadaaf9178140813127879` |
| 10.5 | `107r8APQtkbxF4P1jKHrsQA2P4cZ59laM` | 982,995 | 26 | `1d2a44ce3d63932d849570834b4248c5674191375af6270c1e26d18ee212e3a5` |
| 11 | `1ULJg-JgvPRLo-volh-zLYusSOPp5xsUr` | 1,124,094 | 34 | `626e8b6754dc4073971f968b9704ee65234ff2b4ad6a01db24d7d0cf5bbcd733` |
| 12 | `1whreFwOClLkdvZmFpqVJ-7is9d4wZQzp` | 4,099,162 | 71 | `57fe65e7f4f1f3f9c3ec402ab20b9d52bf5c5b0a6a54f8fc7ad9b6f5058e6ce6` |
| 13 | `1FR6O80Ow-fCNifxe6ZENGXg08Qn8sD5Y` | 15,141,037 | 48 | `b482462a2c4a9aee947d42dba0a6d4cfd8e89d748944da5a309538be8e7272d4` |
| 14 | `1dPuouxGubc6esr7XEvFHmHjD7IW_-bpn` | 4,514,904 | 46 | `e83d8a2bb2014bf072e24053973f389f4fdfbfe531fd887fc9c2d5a31bd73d7c` |
| 14.5 | `1D7BV5n9LQJjODMQCRfq_Mb3zqEzrElft` | 3,045,132 | 40 | `1a1d6f1af3efe89c746a818ab1dab27096d91251e7aca8a2a8b4daaad4fd321f` |

### 2.1 Electronic-edition identity and colophon routes

These are bibliographic data reopened in the named EPUB colophon, not inferred from filesystem timestamps or OPF date strings. Dates that precede the corresponding print-base date are preserved as the witness states them. `2nd e-ed.` and `3rd e-ed.` below mean the colophon explicitly identifies the electronic revision; a missing note is not a claim that no later electronic state exists.

| Volume | Colophon member | Electronic issue / explicit revision | Print base of supplied electronic text | ISBN |
|---|---|---|---|---|
| 01 | `OEBPS/Text/p-0046.xhtml` | 2012-10-01; 3rd e-ed. 2015-05-01 | 2015-03-20, 26th printing | 9784094512625 |
| 02 | `text/part0041.html` | 2012-10-01; 2nd e-ed. 2015-05-01 | 2015-03-20, 23rd printing | 9784094512861 |
| 03 | `text/part0039.html` | 2012-10-01; 2nd e-ed. 2015-05-01 | 2015-03-20, 20th printing | 9784094513042 |
| 04 | `OEBPS/Text/p-0046.xhtml` | 2012-10-01; 2nd e-ed. 2015-05-01 | 2015-03-20, 17th printing | 9784094513325 |
| 05 | `text/part0040.html` | 2012-10-01; 2nd e-ed. 2015-05-01 | 2015-03-20, 16th printing | 9784094513561 |
| 06 | `text/part0045.html` | 2013-02-22; 2nd e-ed. 2015-05-01 | 2015-03-20, 15th printing | 9784094513806 |
| 06.5 | `text/part0038.html` | 2014-07-25; 2nd e-ed. 2015-05-01 | 2015-03-20, 3rd printing | 9784094515015 |
| 07 | `EPUB/text00039.html` | 2013-05-31; 2nd e-ed. 2015-05-01 | 2015-03-20, 11th printing | 9784094514025 |
| 07.5 | `text/part0033.html` | 2013-08-30; 2nd e-ed. 2015-05-01 | 2015-03-20, 8th printing | 9784094514346 |
| 08 | `OEBPS/Text/p-0035.xhtml` | 2013-11-29; 3rd e-ed. 2015-05-01 | 2015-03-20, 6th printing | 9784094514513 |
| 09 | `OEBPS/Text/p-0038.xhtml` | 2014-04-25; 2nd e-ed. 2015-05-01 | 2015-03-20, 4th printing | 9784094514827 |
| 10 | `text/part0034.html` | 2014-11-28; 2nd e-ed. 2015-05-01 | 2015-03-20, 2nd printing | 9784094515237 |
| 10.5 | `text/part0024.html` | 2015-03-27 | 2015-03-23, first edition/first printing | 9784094515428 |
| 11 | `text/part0032.html` | 2015-06-26 | 2015-06-23, first edition/first printing | 9784094515589 |
| 12 | `text/part0029.html` | 2017-09-29 | 2017-09-25, first edition/first printing | 9784094516746 |
| 13 | `item/xhtml/p-0037.xhtml` | 2018-11-30 | 2018-11-25, first edition/first printing | 9784094517620 |
| 14 | `item/xhtml/p-0046.xhtml` | 2019-11-19 | 2019-11-24, first edition/first printing | 9784094517811 |
| 14.5 | `OEBPS/Text/part0027.xhtml` | 2021-04-20 | 2021-04-25, first edition/first printing | 9784094530049 |

Container metadata has known limits. The historical manifest records absent publisher fields in V6, V6.5, V10.5 and V11, non-publisher/extra-creator labels in V7, and V13's non-leading/non-uncompressed mimetype-member advisory. These do not identify a different literary author or authorize modifying the source files. OPF timestamps and creator arrays do not override the colophon or story byline. All 22 freshly verified EPUBs report Japanese language metadata and have the correct mimetype value; these structural checks alone do not certify the quality of every transcription or illustration.

## 3. Fixed-page verification witnesses

The PDF folder is `1b6VcJOY76Z7wbdfPF9xQbF_RqtPAiK29`. Files follow `(一般小説) やはり俺の青春ラブコメはまちがっている。第NN巻.pdf`, preserving the decimal labels below. **Physical PDF pages are not interchangeable with printed book pages.** All seventeen governing file hashes below freshly match the corresponding deep-reading receipts. This is file-identity verification, not a fresh visual re-review of their complete contents.

| Volume | Drive file ID | Bytes | Physical pages | SHA-256 |
|---|---|---:|---:|---|
| 01 | `1HTrN5UnW4ml5zXEY1Q2mZdG7kLTbcuaj` | 30,064,566 | 309 | `cdd77549b71c3f96a6c66a67a1fac42dfdb09531709d9181d9a1d76fcb053988` |
| 02 | `1JkNS9R1vuaMmW6ey-jcjzHy1X0wn83aw` | 27,981,092 | 266 | `59b587e12d8ab3574d1fadfbad7d78cadc3aae3f30f14074fcb0dc55c28c5855` |
| 03 | `1QdqKLxdGeWYnTFznUxBKiZKG0wcoS_U4` | 39,755,916 | 309 | `5402b85a2bcd0a5c1c383bd941efb87af74665e87af67a525f99c9bc1c8d4dc6` |
| 04 | `1tdTEp6zh-iL8gQVEdcYgUbAMobjEZTwx` | 32,040,979 | 300 | `c2f3aaa3b1d61748f3f4603079a375b55b341e0cb6ccef0f269cfe6357b811f3` |
| 05 | `11b2NZ57ofZ6mfdrqwAfR9n6YtL2Uc5_K` | 24,367,661 | 234 | `1655c97e7fe768f7ec494feb318e8f0c8f2a2597a1e412a8ae870fe3b7c6d83d` |
| 06 | `1Yo11NGLj86BEPt7U2Wwm_hJ8wQ91iIou` | 55,457,785 | 360 | `b1040ad07d2162b935039c7984999bc39df7b962ace73a626c20cac5f600c14d` |
| 06.5 | `1vSlLxhj1VaFCpsOAvgLWwLwqWJf2RBTS` | 47,331,302 | 492 | `a4f6eb9cdb214a745df3a2e5bcae3c5b12cf784fdb4f6c311c52b435359ae157` |
| 07 | `1XW91134uds9Zh8AdHcw0ZNsIpw13UiV3` | 53,838,170 | 337 | `f3b6665925ae9eab977d2e176e9774ec2b42ff4eca595c6a539f279d165d15ee` |
| 07.5 | `1lox1ed_aV9pweJ3YKGSW6bhOTA8WX-nC` | 43,234,651 | 262 | `51be8dbbb010ea0f72ee2e473afc1f39b354c5cda8959f48a5e09040f6a9eafc` |
| 08 | `13Sijm67bsuuepDeQyQzEGuI2CjqBe8UW` | 48,900,987 | 361 | `47bd5429dc909d01ffd1a7b6c7c392d13dcd459ca4283bb15ddd4f3c784229e5` |
| 09 | `1muTlvqQFfIGzVKwmJzKdxDLGvwMcjZ-V` | 58,652,492 | 431 | `e4564f99739a4a4311e9cc55f7c4f8ee0b642c0a05956200f666fa4fe2a61101` |
| 10 | `174BtBKPM9v2wdgVCXBQ4mCog9DjnDayg` | 55,812,039 | 344 | `b4846032c97515198b2c6eaf9e1a6a91086080dd33c439a99434fe77bbc76a9d` |
| 10.5 | `1Lo2zolGtXl4ckAXc0KD7suEmY5C-48qp` | 25,095,048 | 235 | `4b93d85b0cb00a86185ba00b55781722444f1dd351e766af8481cf2c764ce021` |
| 11 | `1koLLSqEMSz-fK_5FPdRmGv_lapADDQlK` | 84,273,654 | 320 | `e81e128de1c0ee3da00e3c1ff8f036db5f46eb9466471d3b6c09436a466a3d8f` |
| 12 | `1owSH7X4J3TCdKWmUkHNlxfsCpTyxWcod` | 86,557,425 | 360 | `3b98692440495ee0e80b1ac3669edaa091c2d7d0367f486f76e4254285f94ced` |
| 13 | `1sMuDOtDcSEor3hNJztGW5iQW_KXwGDT4` | 36,349,182 | 362 | `f30cfee5097ad5bff1d42e50e2848d7744a58c3a88f4b4575c79e0f65870418a` |
| 14 | `17BNSDu3WbkswnEECIDLkLwEiCMgF1BHG` | 52,615,674 | 536 | `d258a7bdf443023c749262065578913e3327cb844facb4d860e8e023085abca7` |

**V14.5:** no fixed-page PDF witness was present in the enumerated locked source tree. Its EPUB is the exact-text witness; manufactured print pagination is prohibited.

**V7.5 alternate layout:** the separately stored `(一般小説) やはり俺の青春ラブコメはまちがっている。第07.5巻 [2- page].pdf`, Drive `1UqJQGQbdpygfvAazboTIixhY8nZSNMvL`, freshly has 77,988,249 bytes, 139 physical pages, SHA-256 `8b9761c4b19abe83599a1e3878ca6a60eb2e4c00d457c3c89192b967306d85f6`. It is a separately identified layout witness, not the governing 262-physical-page PDF. No silent locator conversion or new edition-equivalence claim follows from the similar title.

The inherited deep readings distinguish first-print scans, drama-CD limited editions, and later electronic print bases. Those edition judgments remain attributed to their earlier source inspections; the fresh hash match identifies the same PDF payload without claiming that every colophon was rendered again.

## 4. Story boundaries and chronology controls

| Source container | Governing narrative/component boundary | Required chronology separation |
|---|---|---|
| Numbered V01-V14 | Watari's mainline Japanese fiction; attached bonuses and afterwords remain distinct components | Preserve each prospective volume and checkpoint boundary; later knowledge belongs only in retrospective treatment |
| V03 attached birthday prose | Novel-form rewrite of the limited-edition drama; prose controls prose wording | Immediately after the V03 main story; audio-specific delivery requires the recording |
| Commercial V06.5 | Revised sports-festival reconstruction; separately appended Christmas bonus prose | Sports-festival material sits V06→V07; Christmas coda sits immediately after V09 |
| V07 attached `うぃー・うぃる・ろっく・ゆー` prose | Watari-script rewrite supplementary to its publication container | Immediately after V06, not post-Kyoto repair |
| V07.5 | Constituent-story chronology, not automatic placement after V07 | Follow the existing V07.5 constituent chronology ledger; do not import Kyoto hindsight into early stories |
| V10.5 | Late-January/February ordinary-life sequence | Post-V10, with the Checkpoint-D chronology controls |
| V14.5 Stories 1-2 | New Year stories | Post-V09/pre-V10 |
| V14.5 Story 3 | Festival story in late-V14 spring-break envelope | Corroborates the chosen relation without becoming post-new-term evidence |
| V14.5 Stories 4-5 | True post-mainline third-year ordinary life | Positive boundary for the Final Post-14.5 Checkpoint; Checkpoint E remains the separate final-choice freeze |
| Anthology Watari stories | Qualified official author-written supplements | Audited early-third-year post-V14 band; exact internal order remains open where Document 12 leaves it open |
| Anthology guest fiction | Official derivative/reception evidence | No automatic mainline state assignment or power to settle Watari-character interiority |
| Songs, illustrations, afterwords, packaging | Paratext, production, performance, or publication-history evidence | Do not convert package-level themes or retrospective statements into unqualified diegetic facts |

## 5. Official anthology witnesses

The four anthology files were all freshly verified against the historical collection manifest. Their file container, story authorship, and fictional authority are separate questions. Clean electronic text does not make a guest story mainline fact; Watari authorship does not remove Anthology 02's scan-verification requirement.

| Anthology / exact filename suffix | Drive file ID | Bytes | SHA-256 | Source-form authority |
|---|---|---:|---|---|
| `01 - Yukino Side [Japanese].epub` | `13ImOZw9VxvBPwwkQd6tkivn0qa-LzhWo` | 2,382,044 | `9ea7d2f8d2aec0e8d91c698d3cbd516ea55388b26ea45879c8dd355169fa9abc` | clean publisher-derived text witness; story bylines govern authorship |
| `02 - On Parade [Japanese] [OCR Draft].epub` | `11Gm51BHD42ZWhjDKTd6h02oemVooxkWL` | 32,908,355 | `30d677be54a559cd9ebb50e4c611ed928ae77d1c0ae48069bcaab74bed1ee708` | 306 scan-page images govern; OCR navigation only unless visually verified |
| `03 - Yui Side [Japanese].epub` | `1v-jlmuH87PkkSEVqboszd6m4jvrH-lbY` | 2,904,167 | `279a70586ab66f6d462e8568d3c1215912474ca15596924feb70440bbc87e44f` | clean publisher-derived text witness; story bylines govern authorship |
| `04 - All Stars [Japanese].epub` | `1K04TgobFMeZoZXpD_QCJmsc_NuYFxMLo` | 3,002,231 | `fcfc80b10a5a9f73fefea450f3a705d68b139f18b341146a65665eeca62c469c` | clean publisher-derived text witness; story bylines govern authorship |

A1's electronic colophon (`text/part0032.html`) records issue 2020-03-18, print base 2020-03-23, ISBN 9784094518351. A3 (`text/part0037.html`) records issue 2020-04-17, print base 2020-04-22, ISBN 9784094518450. A4 (`text/part0040.html`) records issue 2020-04-17, print base 2020-04-22, ISBN 9784094518467. These clean-text colophons were reopened. A2's metadata and existing admission audit identify 2020-03-23 and ISBN 9784094518368; its scanned colophon has not been freshly visually recertified in this inventory.

The A1/A3/A4 OPF creator arrays do **not** enumerate Watari, although each book contains a Watari story established by story-level bylines and the existing audit. An OPF author list is therefore not an exhaustive authorship inventory. Use Document 12 §8's complete story table for all guest bylines rather than attributing the entire anthology to one contributor or to Watari.

| Anthology | Watari-authored story | Existing qualified use retained |
|---|---|---|
| 1 | `斯くして、彼の前に新たな敵は現れる。` | Post-V14 family/housing/future and ordinary-life supplementary evidence; precise ordering inside the April band remains open |
| 2 | `やはり妹さえいればいい。` | Post-V14 Hachiman/Komachi final shared school year; exact wording requires embedded-page inspection |
| 3 | `いつか、その甘さを好きになることができる気がする。` | Post-V14 Yui's desire, practice, and family futurity without reciprocal-romance inference |
| 4 | `しかし、その言葉の裏には裏がある。` | Post-choice club continuity, institutional handoff, and negotiable pretext; no reset of romantic asymmetry |

[Anthology 02's existing admission audit](OREGAIRU_ANTHOLOGY_02_OCR_SOURCE_ADMISSION.md) remains governing for its scan/OCR distinction. Its supplied receipt records 306 source-page images, 296 book pages plus ten jacket pages, 309 parsed XML documents, and zero validation errors. The fresh container pass also found 306 spine page documents and 306 image resources with no XML/resource/CRC failure; it did not revalidate every source-image hash or visually approve all machine text. The earlier admission audit's `Chronology state: OPEN` is its historical admission-stage boundary; Document 12 subsequently completed the Watari story's chronology audit. Retain that later disposition without rewriting the earlier audit.

## 6. Bonus-booklet genealogy and availability

The live source route is PDF → `Specials` (`18L9NR0Xdh3pnGVA4hH0_ESGbsQHsyoYD`) → `特典 specials やはり俺の青春ラブコメはまちがっている。第6.25, 6.50, 6.75巻` (`1LOO38Xl5Vh0p3aOjK813Dc88whL8qTCb`). The three single-page PDFs were freshly retrieved and match the exact receipts already present in V06.5 §1/YAML.

| Ancestor | Drive file ID | Bytes | Physical pages | SHA-256 | Inherited release date |
|---|---|---:|---:|---|---|
| 6.25 | `1_bo8_k-7OVEBG4wSl49QhX1tLP7MK0EV` | 23,463,679 | 156 | `666bf7a7c26301c7642a8e6a4afa63cbd1ae5140439ab745e0b288e1fe13c3fc` | 2013-06-26 |
| 6.50 | `1FGssWdr4GojsvugQZnhemMA1qww6-vyB` | 23,286,691 | 156 | `fd0b4be05af4fe58738118c88abaf3baa8910a38109f9994bb1574d0208c760a` | 2013-08-28 |
| 6.75 | `1BHHiHpHlKcYHavEWtoH7xNlqt0Yj8Pmd` | 26,239,126 | 150 | `df244b3b95332c67b07957e1dfd09351d2e490ff6721d41b8d12d4224ae57509` | 2013-10-23 |

The alternate `第06.75巻 [2-page].pdf` is also present as Drive `1Pxl-zpQrn6Zvw8vN9XDKQGSyMOzAIcGT`, metadata size 57,999,924 bytes. Its payload was not freshly fetched or hashed and it is not substituted for the governing genealogy witness.

Commercial 6.5 **selectively reconstructs and revises** its ancestors. Its contents do not exhaust the original booklets. V06.5 §1.3 already identifies three omitted stories: 6.50's `だから、比企谷小町は頑張れる。` and `存外、由比ヶ浜結衣は人気がある。`, and 6.75's `密やかに、川崎沙希は問いかける。`. This is a verified existing genealogy route, not a completed new analysis of those stories. Before an omitted story updates a longitudinal state or reconstruction, perform its bounded primary reading, exact source/chronology/continuity audit, and explicit admission through the current project controls. The original eight-model suite is not silently redefined by this discovery.

## 7. Drama, prose rewrites, and performance authority

The inspected audio route is PDF → `Bonus CDs` (`1Fa4oo9Br-oLB_8BFnqi1i7nthMdn-OMg`) → `ドラマCD` (`1rtQURahfaNrtT2bexWInP-QZ4Wyt7guQ`). Audio availability is not interchangeable with completed perceptual review.

| Package | Drive folder ID | Live payload observation | Current authority use |
|---|---|---|---|
| V03 birthday drama | `101amyyaUGvQXWyYfk5x-1IY0E0MA0XP0` | Twelve MP3 files including the separately named song, plus jacket folder | Attached Watari prose rewrite controls quoted prose; fresh audio transcription/delivery audit not performed here |
| V07 rock drama | `1lhxOQHvQLvqY0hUu0nsSeExbxBTWjQ1C` | Ten MP3 tracks and image folder | Prose rewrite with immediate post-V06 chronology remains the textual route; audio performance is separate |
| Event CD `比企谷小町の計略` | `1AAI_MS20buJhr8UUA-ZE4mNF6ke-FBpA` | Four MP3 files plus artwork/booklet folders | Metadata availability only in this inventory; do not infer new mainline state or script authorship without the required source audit |
| Christmas drama, folder labelled V06.5 | `12z-TcXbzS6-kr7wolpP7aXPBeOydRHhi` | Ten MP3 files and image folder | Existing [Christmas drama deep reading](../03%20Volume%20Deep%20Readings/OREGAIRU_V2_V06_5_DRAMA_CD_DEEP_READING.md) controls source roles and post-V09 chronology |

The Christmas recording package is labelled by commercial V6.5 in the source folder, but the prose provenance identifies its script as the **V09 limited-edition drama**, with story chronology immediately after V09. Folder labels do not change that finding. The existing package audit records Watari's original/script credit. The **recording governs the performance as performed**; V6.5's prose rewrite (`text/part0032.html`, provenance note near its opening) governs exact prose wording and textual locators. The source warns that rewrite and recording differ. This inventory does not infer audio-word equivalence from the crosswalk.

All ten recording files below freshly match the existing drama audit's hashes; durations are rounded here to three decimals as in that audit. Hash/metadata verification does not claim a new direct-listening pass.

| Track | Drive file ID | Seconds | SHA-256 |
|---|---|---:|---|
| 01 — Prologue | `1LHwk9ySKs-0-Me7Jf-bgbL88WEVR8S2t` | 145.102 | `4892ceb46970eac4731b26fc43564b3ec700701440edf6fdd1095fb917385431` |
| 02 — Scene 1 | `19_Yo2HnzRU2tD5nhY1cxFXCab85o-F9v` | 550.575 | `ee30b933702f0d8655b67b5d41d6dfc5b11ace8aeb4209a04edce83b30af5b00` |
| 03 — Scene 2 | `1s-tJhNJCmdBYPOGqV-lvFVCiiOoa0VQ2` | 237.183 | `79267d64e1b1525697c5791807170ec0c2490f1957d8c2ca034e34f7334609aa` |
| 04 — Scene 3 | `1vM6dI9Do4rViTKPbhkqD5zU8V3h3Ps3j` | 385.292 | `a3f66776da79e0d0fc7c8ffef48ef37e27b16b642086184a33f53b4ce811881a` |
| 05 — Scene 4 | `1-uPOJCJ2iSCll7SlP6AO3xAJ-gcF9Fck` | 570.316 | `8f865a64f809500f5f4f72063251dc6342b41d79f7bbc900f272ba78cbff2751` |
| 06 — Scene 5 | `1bp9xs6Ztw1Wo_Ni3Pbgj9hONNF2qfr53` | 608.561 | `3657b143351ecc92d9aec61c56e289ca484251ad48ad0a68ab3796e209af556f` |
| 07 — Scene 6 | `1B5eETRfEX4fGDgS70ytS7uR-_zbl1QB1` | 626.506 | `bd8e284c6dfe5f75aa2a386becffc132e3f4f4db9a5cfc6c61e87201a0d9f5ef` |
| 08 — Scene 7 | `1Uj2Rt0vVRmg7ZnIwfKIb_Xcb9gew6J5D` | 674.675 | `66164dfd977eb65d62e3b46c094ca0e5f34fce0bf6da08ecbbd825862cbaf069` |
| 09 — 君とMerryChristmas | `1YIrqIRE47r72wuTIDQy2M4_Qa058FUvL` | 306.741 | `cda9607e7d00eabeec0048a0d418f495904634a72c475f513598fbaa5c120ec5` |
| 10 — Epilogue | `1ZuCwa-wQ16lW7tT-IvsMz1B6KV_2Bd-O` | 242.061 | `28a2ad2c4df0d3eaaf91ed2406b7a4da20e0364710ac59e107db1a2cca06be59` |

`君とMerry Christmas` is separately credited song paratext (lyrics rino; composition 増谷賢; arrangement 長田直之 in the existing packaging audit), not unfiltered Yukino/Yui prose interiority. The Christmas image subfolder is `1X9yOMFd3qekDFGfGJvtTcbl6pEIVUieH`; its existence was confirmed, but its complete image inventory and previously recorded packaging hashes were not freshly reconciled here. Do not describe that remaining paratext verification as completed.

## 8. Attributable source-record errata

These corrections are authored by the **2026-10-16 Oregairu continuation/source-inventory pass**. They preserve frozen readings, admission receipts, prospective freezes, and migration crosswalks. Their narrow authority is source identity/availability, not retrospective rewriting of literary conclusions.

### OREGAIRU-SRC-ERR-001 — V12 truncated SHA-256

- **Affected artifact/sections:** `03 Volume Deep Readings/OREGAIRU_V2_V12_DEEP_READING.md`, YAML `primary_text_sha256` and §1.1.
- **Recorded defect:** `57fe65e7f4f1f3f9c3ec402ab20b9d52bf5c5b0a6a54f8fc7ad9b6f5058e6` contains **61**, not 64, hexadecimal characters.
- **Correct current source identity:** `57fe65e7f4f1f3f9c3ec402ab20b9d52bf5c5b0a6a54f8fc7ad9b6f5058e6ce6`, 4,099,162 bytes, Drive `1whreFwOClLkdvZmFpqVJ-7is9d4wZQzp`.
- **Evidence/countercheck:** complete fresh fetched bytes produce the corrected digest; the separately preserved August collection manifest already records the same full digest. The historical string is its exact prefix, missing terminal `ce6`. No contrary source hash or evidence of source mutation was found.
- **Disposition:** **REVISE source-identity transcription only.** Use the full digest in this inventory and new reproducibility receipts. Frozen V12 bytes remain unchanged; no literary claim or chronology is revised.

### OREGAIRU-SRC-ERR-002 — Booklet availability was incorrectly collapsed into non-admission

- **Affected artifacts/sections:** Document 12 §2.1–2.2 and source-boundary wording describe original 6.25/6.50/6.75 as unavailable; the August EPUB collection manifest also says original bonus booklets are absent. Those statements are not a correct current account of the enumerated PDF tree.
- **Evidence:** live file metadata and freshly fetched complete PDFs in §6 match **the same three IDs, sizes, hashes and physical-page counts already recorded by the frozen V06.5 deep reading**. V06.5 §1.3 already uses them to establish selective commercial reconstruction and identifies three omitted stories.
- **Counterevidence/limit:** neither PDF availability nor genealogy inspection proves a completed separate substantive reading of omitted stories. The collection manifest is an EPUB-focused historical inventory; its absence statements cannot override observed PDF witnesses. No claim is made about when the contradiction first arose or why later synthesis lost the earlier route.
- **Disposition:** **REVISE availability; PRESERVE bounded genealogy authority.** These three witnesses are available and already documented for genealogy. Do not cite their absence as an acquisition blocker. Omitted stories remain a separate bounded source-analysis/admission question before they can change character-state authority. This inventory does not silently amend the initial reconstruction suite or the frozen prospective corpus.
- **Analytical consequence:** Kawasaki, Komachi and Yui have exact available supplementary-source routes worth evaluating; neither invented missing content nor universal retrospective expansion is warranted.

## 9. Exclusions, unavailable witnesses, and OPEN verification

| Object or question | Current source/authority disposition | Required next action if pursued |
|---|---|---|
| `Shin` | **EXCLUDED by owner scope.** Availability is not an analytical completion requirement | No acquisition, reconstruction, or incorporation under this task |
| `結` / Ketsu 1–2 | Source files are present in the enumerated EPUB folder (`1Rrc2-oeNfJ-qxf6phJ5VUQmQMstRt5_b`, `130O2Es1wAqnyFpO-3AuW6mmU6BIkixBB`); alternate continuity excluded from mainline V2 authority; not fetched for this pass | Separate approved alternate-continuity scope before substantive analysis |
| `結 3` | Acquisition lead; no payload in the enumerated project source root on verification date | Owner acquisition, validated identity and distinct continuity/scope decision; existing V2 release must not wait for it |
| `－刻－` | Acquisition lead for production-history/paratext; no payload in the enumerated root | Verify acquired edition/components; retrospective author statements do not automatically override published fiction |
| JR Central four-story campaign | Acquisition/access lead, not admitted narrative content in this inventory | Respect official conditions and reproduction limits; route current official availability through the corpus map's acquisition record |
| `Another` original booklets | Not found in the enumerated source tree; not mainline authority | No reconstruction from adaptations or Ketsu substitutes |
| V14.5 fixed-page witness | Not present in the enumerated locked PDF tree | Retain EPUB-only locators; do not manufacture pagination |
| Omitted ancestor-booklet stories | PDFs available; separate chronology/authority/substantive coverage uncompleted here | Bounded source inspection and explicit admission before state-changing claims |
| Audio/paratext beyond the specified Christmas files | Package metadata observed; fresh payload/inspection coverage is limited as in §7 | Do not inflate file availability into completed auditory or visual analysis |
| Exact anthology ordering inside early third year | Retained OPEN where Document 12 leaves it OPEN | Do not invent a total story sequence from publication dates |
| First-print/electronic textual equivalence | Same locked witnesses recovered, not exhaustively collated | Reopen EPUB plus rendered PDF at any disputed wording-sensitive locus |

## 10. Reproduction and retrieval rules

1. Resolve the current corpus map and the relevant claim/ledger/volume route before opening source payloads. The deterministic chain remains **claim → Document 13/specialist/ledger → checkpoint/deep reading → source member or printed-page anchor → Japanese witness**.
2. Retrieve the exact admitted Drive ID with authenticated source access. Compare complete-file bytes and SHA-256 with the table, rather than filename alone. Keep source payloads and extraction outputs outside analytical Git and analytical release ZIPs.
3. EPUB verification used SHA-256 and byte count of the complete file, ZIP `testzip`, `mimetype`, XML parsing, OPF-relative manifest-resource resolution and spine-ID resolution. All 22 tested EPUBs had zero failures for these checks. This pass did not repeat the old image-decoding, language-detection, or exhaustive source-image provenance tests.
4. PDF verification used the complete-file hash and byte count plus `pdfinfo` physical-page count. A matching hash identifies the earlier inspected witness; it does not convert a fresh metadata operation into a new visual reading.
5. MP3 verification used complete-file SHA-256 and `ffprobe` duration. It does not establish a new perceptual observation or verbatim transcript.
6. Source-retrieval helpers may index actual XHTML `<p>` elements with 1-based counts and remove ruby reading tags for searching. Fresh synthetic paragraph numbers must not silently replace historical synthetic locators. Recover exact member/element IDs and Japanese anchors, check surrounding context, and preserve each volume's recorded locator convention. Ruby, punctuation, typography or OCR uncertainty requires the actual primary witness, not normalized search output.
7. This inventory contains source metadata and analytical routing only. It grants no right to reproduce primary novels, scans, audio, screenshots or restricted campaign content. Public archival packages contain analysis and sanitized reproducibility metadata only.

## 11. Completion boundary

The present inventory reconciles **22 EPUB identities, 17 governing fixed-page identities, three already-documented genealogy PDFs, ten Christmas audio identities, and one explicitly non-governing alternate V7.5 PDF** through fresh byte checks. All previously recorded complete governing hashes in that set match; the V12 transcription erratum is separately resolved above. Other package/availability observations are explicitly labelled metadata-only.

This closes the missing consolidated identity route for those witnesses. It does **not** certify Phase 8.5 behavioral audit success, complete new supporting-character analysis, approve an archival freeze, or create new global character discovery/capability records. Those outcomes remain governed by their named artifacts and the registered corpus map.
