---
series: MHA
artifact_type: source_lock
scope: UA_UAN_UAG_ORIGINAL_EPUBS
generation: V2
status: canonical
source_boundary: Three owner-supplied Japanese original EPUBs; older CBZ objects and repaired EPUBs have comparison/derivative roles
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
recommended_reasoning_class: SUBSTANTIVE_ANALYSIS
---

# MHA SP2 — Official supplemental source lock

Verified 2026-09-10 for the authorized bounded continuation at baseline `99de1f40436728d974722dff0055193a5f63ec45`. These are source-identity and technical-access results, not certification of completed content review. Raw books, extracted images, repair tools and private working receipts remain outside analytical Git. The owner-supplied originals are preserved unchanged.

## Preferred primary objects

| Code | Exact original filename | Bytes | Original spine pages | Pixels per page | SHA-256 |
|---|---|---:|---:|---|---|
| UA | `My Hero Academia - Official Character Book - Ultra Archive [Japanese].epub` | 119,118,239 | 217 | 1019x1600 | `a087a83d458600d591b54ecd2b8756ea54843a82d8fefdb1ce3359e49a577de7` |
| UAN | `My Hero Academia - Official Character Book 2 - Ultra Analysis [Japanese].epub` | 142,651,117 | 297 | 1019x1600 | `5919e53bfe452ff1ffcebfb373140ee91623ea11a1dbf712805296aa61f269d2` |
| UAG | `My Hero Academia - Final Fanbook - Ultra Age [Japanese].epub` | 331,826,941 | 331 | 1304x2048 | `869031bf8c96805d3f68b68bdc0575084ef66c6ff78b7de9b0e581a59503deaa` |

The original EPUB is the canonical object for each code. All three archive integrity checks pass; every image decodes successfully. Each is an EPUB 3 image-based book with `OPS/standard.opf`, right-to-left page progression, a navigation XHTML/NCX and a direct-image spine. ZIP member order is not reading order. Body text is embedded in JPEGs, not searchable XHTML; extracting the table of contents is not reading the book.

The [complete spine map](MHA_SP2_SUPPLEMENTAL_SPINE_MAP.tsv) owns the deterministic locator `CODE:sNNNN`, original OPF idref, exact image member, image hash, byte count, dimensions and derivative wrapper. It has 845 rows: UA 217, UAN 297, UAG 331. Printed pagination is a separate visually verified field in each book's coverage record and must never be inferred solely from a filename suffix. No non-spine image was found. The seven other members in each original are package/navigation/rights/runtime resources; they are accounted as technical apparatus, not omitted character pages. Their markup was inspected for topology, not accepted as narrative evidence.

## Reading derivatives and package defect

The supplied originals have direct JPEG spine items. On the original UAN object, Calibre 9.13.0's viewer preparation failed in cover processing with `TypeError: Invalid input object: bytes`. Separate files whose names append ` [Calibre-compatible].epub` contain XHTML page wrappers and corrected navigation/cover/fixed-layout metadata. All three passed Calibre viewer preparation with the expected page counts and right-to-left order. This is a render-preparation test, not a claim of a native viewer UI test.

| Code | Current Calibre-compatible container SHA-256 | Original image byte/order equality |
|---|---|---|
| UA | `60fccd47d4c3b437decd5ab2292c61d72a25b5c8c767982504b02152adadb08f` | 217/217 identical, same order |
| UAN | `c23d51bb5e20117d9c0c7270a83fa29b8ec2d8e2c4ceb313746e349f726d73c0` | 297/297 identical, same order |
| UAG | `87bed1ce8ee04eb34604f0b5813467349ad9872baff6e0ee66ab6a1cfd3dfd06` | 331/331 identical, same order |

UAN's current derivative container hash differs from the earlier repair receipt quoted in the execution prompt (`e1c93b52eb526802fd6634f76a014d9b2a02f55a4106b1045038537c19f612e5`). Its original EPUB hash and all 297 image bytes/order remain verified. Container drift must be recorded separately; a changed derivative container is neither a new canonical witness nor evidence of changed character content. The other current derivative hashes match the earlier receipts.

## Earlier CBZ correspondence and edition caution

| Older comparison object | SHA-256 | Relationship to preferred EPUB |
|---|---|---|
| `My Hero Academia - Official Character Book - Ultra Archive [Japanese].cbz` | `6088d917b98f24a7cfdf3cf7acf0873aecc5913a75edd741e79ff5cd66f9a54a` | 217 images, 1020×1600; machine correspondence maps one-to-one in the same page order. None is byte-identical to the 1019×1600 EPUB pages. Visual checks establish some actual editorial differences, so this is not certified word-for-word equivalence. |
| `My Hero Academia - Official Character Book 2 - Ultra Analysis [Japanese].cbz` | `115f8afc24df2bd03d7f78bf5b1cb11a4633796246789494a2fc477dd2696f51` | 298 images; EPUB spine sN maps to CBZ numeric image N+1. The extra 884×1200 first image is a cover variant, not a missing interior page. Of 297 matched pairs, 290 decoded RGB images and 70 compressed image byte sequences are identical. |

UA:s0116 and UA:s0191 provide observed edition differences: the Nezu caption differs, and the Smash!! promotional footer changes its publication/volume framing. The EPUB remains owner-preferred, but dates and reprint/editorial revision must be attributed carefully. The 2016 title's initial publication date does not establish that every line of this supplied digital package is unchanged from its first printing. Matched page topology does not prove full textual identity. UAN's seven nonidentical decoded-image pairs remain subject to the technical comparison's explicit review limits.

## Publication dates and content cutoff

Publisher metadata distinguishes original print and digital releases: UA 2016-05-02 / 2016-07-04; UAN 2019-10-04 / 2019-10-18; UAG 2025-05-02 / 2025-05-02. Sources: [Shueisha UA](https://www.shueisha.co.jp/books/items/contents.html?isbn=978-4-08-880719-5), [Shueisha UAN](https://www.shueisha.co.jp/books/items/contents.html?isbn=978-4-08-882128-3), [Shueisha UAG](https://www.shueisha.co.jp/books/items/contents.html?isbn=978-4-08-884309-4). These dates are not universal narrative cutoffs or package conversion dates. Each book audit must reconcile its actual colophon, credited contributors, original/reprinted material and claim-specific reference time. Unknown original revision dates remain unknown.

## Boundaries

The manga V01–V42 source locks remain unchanged. This lock admits only UA/UAN/UAG for the named reconciliation and does not certify an exhaustive franchise supplement inventory. It confers no new authority on historical predictions, rewritten checkpoints or unrelated adaptations. The method, architecture and current map govern how actual review progresses and how admissible claims reach current analytical homes.
