---
title: "Silent Witch — Japanese LN V01 Source Lock"
artifact_id: SW_LNJP_V01_SOURCE_LOCK
artifact_type: technical_source_lock
series: "Silent Witch: Secrets of the Silent Witch"
series_id: silent-witch
generation: V1
version: "1.0"
status: canonical
scope: "Exact supplied V01 witness, usable source resources, faithful local derivatives and coverage routes"
source_boundary: "Japanese LN V01 technical source validation only; no narrative source unit analyzed."
created: "2026-10-13"
canonical_home: "series/silent-witch/01 Source Lock and Inventory/SW_LNJP_V01_SOURCE_LOCK.md"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
witness_id: SW-LNJP-V01
source_lock_state: BYTE_LOCKED_LOCATORS_LOCAL_ONLY
evidence_retention: LOCAL_ONLY_OWNER_REQUEST
sequential_analysis_lock: CLOSED
literary_inspection: NOT_STARTED
---

# Japanese LN V01 source lock

This locks the supplied witness `SW-LNJP-V01` to exact archive bytes and documents its technical preparation. It establishes neither literary coverage nor a frozen volume interpretation. The [current corpus map](../CURRENT_STATE_AND_CORPUS_MAP.md) remains PRE_V01; the [gate report](../08%20Audits%20and%20Manifests/SW_V01_READINESS_GATE_REPORT.md) records owner acceptance and the subsequent instruction to keep the derivatives local and leave the sequential gate CLOSED.

## Witness and edition

| Field | Verified value / qualification |
|---|---|
| Provider filename | Secrets of the Silent Witch - Volume 01 [Japanese].epub |
| Drive file ID | `132fYBc7_pAdS0Z0zI3NQW3QwjjQFYrG9` |
| Parent source folder | `1WNMgxj2Du9HCSkNkhq5cw7YCFufX1qQL`; provider title Silent Witch. |
| Provider modified time | 2026-10-12T22:43:54.633Z |
| Retrieved bytes | 17,235,698 |
| Independently computed SHA-256 | `d3d8cca8fc271f29cc96a56e7e92b898bfebe4f744b9f3fd424fd8789686968d` |
| OPF title | サイレント・ウィッチ　沈黙の魔女の隠しごと |
| OPF author / language | 依空 まつり / ja |
| Title-page and illustration credit | 依空まつり; 藤実なんな. The first printed title has no visible Roman numeral; the OPF filing title identifies 001 and the supplied inventory designates main-01. |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | B095XR7V9Y; this is the OPF identifier, not an asserted ISBN. |
| Electronic publication / revision | Colophon: 2021-06-10 / ver.003. |
| Declared print basis | Colophon identifies the first edition published 2021-06-10. |
| OPF modification / conversion credit | 2022-07-16T06:38:13Z / UnpackKindleS ver.20220126. |
| Retained audit comparison | Exact hash, byte size and all 36 spine paths match the currently retrieved schema-v2 audit manifest. Its SHA-256 is `2ddd2ec5721e77658ae25d2534e2e7b93ac1dd475ce015c8d82ccf9a2b9c26da`. |

The lock is on this converted, reflowable supplied witness. Publisher-original EPUB equivalence and an independent official-edition comparison remain unverified. No source bytes or metadata were repaired. ZIP CRC, source usability and conversion provenance do not establish a certified official EPUB release.

## Technical validation performed

On 2026-10-13 UTC, the authenticated original file and retained audit manifest were retrieved. Every ZIP member passed CRC; all 72 member names were unique and safe. The mimetype is correct, first, uncompressed and without a local extra field. No encryption descriptor is present.

The OPF is `OEBPS/content.opf`. All 69 manifest resources and 36 spine references resolve. All 37 XHTML documents and both navigation forms parse. Resource/fragment validation passed for 94 local references, including active CSS imports. A commented-out developer import of `style-check.css` is inactive, rather than a missing runtime resource. External links were counted without fetching them. All 24 JPEG resources fully decoded; the image index preserves their exact bytes, hashes, dimensions and source uses.

Thirty-five spine documents declare Japanese; the image-only cover has no declaration and inherits the package context. Mechanical kana/Han counts corroborate the Japanese witness but do not prove comprehension. EPUBCheck and whole-reader-app rendering were not run. Original XHTML/CSS and images remain the fidelity authority for layout, vertical writing, emphasis and image-only material. No printed page numbers are asserted.

## Source order and admission classes

The complete spine is accounted for below. Paths use the common prefix `OEBPS/Text/`. This is technical inventory and a future coverage contract; every literary-inspection state remains NOT_STARTED.

| Spine position | Member(s) | Class / future treatment |
|---|---|---|
| 1 | p-cover.xhtml | Source-identifying visual cover. |
| 2–4 | p-fmatter-001.xhtml through p-fmatter-003.xhtml | Front illustrations; distinct visual channel, no inferred prose or characterization. |
| 5 | p-titlepage.xhtml | Source-identifying visual title/credits. |
| 6 | p-caution.xhtml | Publisher notice; outside narrative projection. |
| 7 | p-001.xhtml | Illustration/design credits; source-identifying paratext. |
| 8–9 | p-toc-001.xhtml, p-toc-002.xhtml | Illustrated and linked text contents. |
| 10 | p-002.xhtml | Prologue opening and native anchor toc-001. |
| 11 | p-003.xhtml | Prologue illustration. |
| 12–13 | p-004.xhtml, p-005.xhtml | Prologue continuation; not separate invented chapters. |
| 14 | p-006.xhtml | Main-story illustrated chapter opener. |
| 15–24 | p-007.xhtml through p-016.xhtml | Ten main chapters, in order; native anchors toc-002 through toc-011. Embedded images retain their exact paragraph positions. |
| 25 | p-017.xhtml | Epilogue; native anchor toc-012. |
| 26 | p-018.xhtml | Illustrated secret-episode heading; native anchor toc-013. |
| 27 | p-019.xhtml | In-volume supplemental narrative, under the secret-episode heading. Include after the main epilogue when V01 reading is authorized. |
| 28–31 | p-020.xhtml through p-023.xhtml | In-volume illustrated character reference, beginning at toc-014. Separate reference/visual paratext; no text-only coverage claim. |
| 32 | p-024.xhtml | Afterword, author/production commentary; toc-015. |
| 33 | p-allcover-001.xhtml | Full-cover visual paratext. |
| 34 | p-colophon.xhtml | Edition/publisher-identifying paratext. |
| 35 | p-colophon2.xhtml | Publisher rights/production notice. |
| 36 | p-bookwalker.xhtml | Store/publisher notice image; outside narrative projection. |

The in-book linked contents lists 15 entries. EPUB nav and NCX index only the twelve main sections; the extra, illustrated reference and afterword are recoverable through the in-book contents and spine. Using EPUB navigation alone would omit source channels. Image title pages were visually checked only for identity/classification; the reference pages and story illustrations have not received literary inspection. One embedded decoration was checked to distinguish an image from a missing gaiji transcription.

No unrelated publisher-preview narrative section is identified in V01. The 14 main narrative text members, one in-volume supplemental narrative member, story/title images, four illustrated-reference members and afterword retain distinct channel/admission classifications. Later-volume publisher previews reported elsewhere remain outside this lock.

## Fidelity and deterministic locators

The local evidence package uses `SW_EPUB_FIDELITY_V1`. It retains every uncompressed source member byte-for-byte, full body trees, a block map, an element-locator map, image resources/uses, navigation, validation and the exact normalizer.

Locator grammar is `SW-LNJP-V01:S<two-digit spine>:E<six-digit element>`. E enumerates every XML element in the XHTML body in preorder, starting with body = 1. Empty elements, blank paragraphs, scene separators, ruby and image elements all count. The map supplies the exact spine member, one-based child-index path from body, original tag/attributes, exact chapter label and native IDs where present. Paragraph ordinal separately counts all p elements, including empties. A chapter's native toc anchor identifies its entry but does not falsely give every paragraph a native anchor.

The fidelity trees preserve original Unicode, text/tails, attributes, ruby rb/rt/rp and line breaks. Original XML and CSS retain lexical/typographic authority. The reading aid omits ruby rt/rp while retaining their reversible tree mapping, maps br to LF and image elements to U+FFFC, and inserts one explicit LF delimiter after each block. UTF-8 byte offsets recover each block exactly. It performs no NFKC conversion, punctuation simplification, OCR, translation, spelling correction or prose trimming. Image-only headings/reference material has no fabricated transcription.

All 8,934 mapped body elements and 3,976 blocks round-tripped to independently parsed original XHTML. The narrative aid contains 3,885 blocks and 141,166 content characters excluding its added per-block delimiters; this includes preserved breaks/image placeholders and is not a count of semantically read prose. Across all mapped blocks, 1,220 ruby elements are retained.

Limited technical checks covered ordinary dialogue, ruby-bearing wording, the first main-chapter boundary, the last main-story passage and the final in-volume narrative passage. Their wording was checked only for extraction fidelity; no literary observation, prediction or character record was authored. A second build reproduced the package SHA-256 exactly.

## Evidence seals and local retention

| Object | SHA-256 |
|---|---|
| SW-LNJP-V01_FIDELITY_LOCATORS_V1.zip; 18,275,961 bytes | `33fade35c657bd95b120878b613d999d61dad2569f1a10e9418a76a7bd656f1e` |
| package-manifest.json | `2018db3ed86e4025a15b94edc26d40ed3ccf3c4511ba99e172050fe712654d0d` |
| normalizer.py | `204892702a9947982d85f5c876280538081f265551a5624325cb54d329a6c7d4` |
| narrative-base.txt | `4a7e38a6572ffc301e0ef2bd27161122430c4f7d29e0bebd5a3abbaa599efca2` |
| block-map.jsonl | `bc9bf79015a20a3461397a9a43be0af0baf62ffc6308b5cad7638263ecb6d75b` |
| element-locators.jsonl | `9da786d49afa457c179b0e9b950b64b6138dae162f2d9b8b9e40662c4ca9d91e` |
| validation.json | `27fcbe6dca217edd591b7426871ccf52a1110c60d9aead50d8663fc20148df74` |

The owner explicitly selected **keep the package local and leave the gate CLOSED** after automatic approval review rejected a Drive upload lacking specific payload/destination approval. No upload occurred. These seals identify actual retained local files, not a remotely published locator package. The local delivery receipt supplies its path; public Git intentionally contains no private working path or raw extraction payload.

## Stable external evidence

Recover the source through the authenticated Google Drive connector using the observed IDs below. Referenced IDs establish identity, not public access or redistribution permission.

| Object | Stable Drive ID |
|---|---|
| Silent Witch source folder | `1WNMgxj2Du9HCSkNkhq5cw7YCFufX1qQL` |
| Locked original V01 EPUB | `132fYBc7_pAdS0Z0zI3NQW3QwjjQFYrG9` |
| Retained audit manifest | `12uKVr1bAXZKlhYBzlGntvN5kNLDetjzU` |
| Retained audit report | `1bXhAGOSzRO6BECVIG_cp4jDH-Oj57ysL` |

The [source map](SW_SOURCE_AND_CONTINUITY_MAP.md#recovery-and-future-ingestion-dependency) and [Drive reference index](../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#silent-witch-v01-source-lock-reference-routing) provide public-safe recovery routes. A future session must recover and verify the local package or obtain separately authorized evidence retention before using its locators. Gate opening and V01 deep reading remain separate owner decisions. No numbered unit has been read, accepted or closed.
