---
title: "Kamakura Police Station — source and witness map"
series: "Kamakura Police Station: The Case Files of Asumi Ogasawara / 鎌倉署・小笠原亜澄の事件簿"
series_id: kamakura-sho
artifact_id: KSOA_SOURCE_AND_WITNESS_MAP
artifact_type: source_inventory
generation: KSOA-G1
version: "1.0"
created: "2026-11-12"
status: canonical
scope: "Bibliographic identity, witness bindings, structural coverage and source locator contract."
source_boundary: "Japanese publisher EPUBs V01–V07. Bibliography, bytes and package structure reconciled. Narrative admission and inspection are pending."
canonical_home: series/kamakura-sho/KSOA_SOURCE_AND_WITNESS_MAP.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
recommended_reasoning_class: BOUNDED_STANDARD
---

# Source and witness map

## Source routes and reconciliation

The canonical evidence folder in Google Drive is named **Kamakura Police Station: The Case Files of Asumi Ogasawara**, folder ID `1GhsceqbFUIZ4w1BE-WVLhEGqennFMwPJ`. Retrieve it in the authorized account. The owner's local source library has the corresponding `Main Series` collection. The import and propagation records in the source folder identify the exact local destinations and Drive files. The same records are held with the local collection, alongside historical pipeline records. This map binds analysis aliases to observed witnesses and links to publisher bibliography. The existing source records own acquisition and replication provenance.

| Source record | Verified responsibility |
|---|---|
| `CALIBRE_IMPORT_2026-11-11.md` | Describes the import and reports passing EPUB container/mimetype, referenced-resource, spine, ZIP CRC and copied-checksum checks. The report explicitly leaves full EPUBCheck unperformed. |
| `calibre_import_manifest_2026-11-11.json` | Carries the seven Japanese publisher EPUB records and the source/destination SHA-256 values. The legacy `volume` field is null for these rows, so the mapping was reconciled by Japanese title, destination basename and hash. |
| `drive_propagation_manifest_2026-11-11.json` | Carries the folder ID, per-file Drive ID, name, size and local SHA-256. Bootstrap matched those fields to the live listing and independently hashed the complete Drive downloads. |

The direct Drive listing returned seven EPUBs and those three records. The local tree contained all seven EPUBs under `Main Series`, the three current records, a local README and historical pipeline records. The three current records matched local and Drive SHA-256 and byte counts. Each EPUB's freshly computed local SHA-256 matched the import source and destination values, the propagation digest and the SHA-256 computed from its current Drive bytes. These checks bind the observed copies and records at reconnaissance. A later operator rechecks the digest before using any copy.

## Seven-work bibliography

The EPUB OPFs give the series name 鎌倉署・小笠原亜澄の事件簿 with the corresponding Japanese title, author 鳴神響一, publisher 文藝春秋 and language `ja`. Independent publisher listings confirm the titles and 文春文庫 imprint. The Vnn keys record the seven-work sequence of the identified releases. The publisher identifies V07 as the final volume. Each English label below is the middle of the filename `Kamakura Police Station - The Case Files of Asumi Ogasawara - Volume NN - {label} [Japanese].epub` and serves retrieval only.

| Work | Japanese title | English retrieval label | Publisher print record | Publisher release |
|---|---|---|---|---|
| V01 | 稲村ヶ崎の落日 | Sunset at Inamuragasaki | [9784167919450](https://books.bunshun.jp/ud/book/num/9784167919450) | 2022-10-05 |
| V02 | 由比ヶ浜協奏曲 | Yuigahama Concerto | [9784167920425](https://books.bunshun.jp/ud/book/num/9784167920425) | 2023-05-09 |
| V03 | 極楽寺逍遙 | A Stroll Through Gokurakuji | [9784167921149](https://books.bunshun.jp/ud/book/num/9784167921149) | 2023-10-11 |
| V04 | 竹寺の雪 | Snow at the Bamboo Temple | [9784167922375](https://books.bunshun.jp/ud/book/num/9784167922375) | 2024-06-05 |
| V05 | 西御門の館 | The Nishimikado Mansion | [9784167922863](https://books.bunshun.jp/ud/book/num/9784167922863) | 2024-10-09 |
| V06 | 佐助ヶ谷の銀雫 | Silver Droplets of Sasuke-ga-yatsu | [9784167923013](https://books.bunshun.jp/ud/book/num/9784167923013) | 2024-11-06 |
| V07 | 長谷の花舞 | Hanamai of Hase | [9784167923785, series finale](https://books.bunshun.jp/ud/book/num/9784167923785) | 2025-06-04 |

All packages declare EPUB 3.0, one rootfile `item/standard.opf`, right-to-left page progression and the OPF unique identifier `unique-id`. The table gives the suffix of each `urn:uuid:` identifier and the UTC calendar date of `dcterms:modified` (each has time `00:00:00Z`). Dates and identifiers describe the EPUB packages. Print ISBNs above identify the publisher's paperbacks. The OPF exposes a UUID and supplies no ISBN binding or print-page crosswalk. The V03 OPF title sort key contains アズミ and the V05 sort key contains ニシゴモン. Treat these as observed metadata variations, and verify any reading claim against the Japanese witness or the specific bibliographic record it describes.

| Witness alias | Bytes | SHA-256 of local and Drive copy | OPF UUID suffix | Package modified |
|---|---:|---|---|---|
| KSOA-JP-V01-W01 | 901559 | `2b002b1e4854e6d72f6fc24963b50633f4f73d7a8bfcb22031f270afd49f898b` | `6f71c28e-23e8-435e-a00e-987785db0069` | 2022-09-12 |
| KSOA-JP-V02-W01 | 844396 | `d36084b9e0e5621e2d8d99577519956f69edca5b8c14999cbaf09d6fddd54f31` | `24274f95-90f0-4fc2-8081-360ab91c4bf6` | 2023-04-20 |
| KSOA-JP-V03-W01 | 921144 | `5525f841bb853873386228416725ade9a8fd540dcb9dacc3f52fbaf284886811` | `6c1def2b-21ba-4c49-9dd6-1565eb409593` | 2023-10-02 |
| KSOA-JP-V04-W01 | 891417 | `bfc818c532bec74d3d7c4344cd39e123e6996e1fe7c8c45c282f3bcb569f2341` | `acdec7b2-8ea6-443f-9c64-20632561a89e` | 2024-05-27 |
| KSOA-JP-V05-W01 | 831263 | `960beee524746bd39f5599f8210d5959b2a56be6a6c2ce34997ed94eec4f7e49` | `b8f60df0-5c4a-4959-9d1a-5a3f573215e9` | 2024-09-20 |
| KSOA-JP-V06-W01 | 915563 | `4851a03670c1306c0c554c6ad353ba1c88a997cde9f793a4b1628fb175764f5b` | `6808c365-5230-403d-b44a-fd09f6e9d226` | 2024-10-23 |
| KSOA-JP-V07-W01 | 661308 | `7702b7eedd36a262998f7cc3a7e5824a5fb45380cde3fd6cd400e6a1df94daf1` | `4163a90d-c5bd-4ecf-8b56-522726aa986c` | 2025-05-20 |

## Spine and literary boundaries

Across the seven witnesses, the first ZIP member is the stored EPUB mimetype. ZIP CRCs passed, manifest references exist, all spine XHTML parsed, and inspected navigation targets and fragments resolved. The observed spine has 100 occurrences in all, with no explicit `linear="no"` entries. The XHTML navigation member is `item/xhtml/p-toc.xhtml`. It has no page-list and the packages declare no spine NCX. This is package and navigation verification. Full EPUBCheck, rendered fidelity, completeness against a publisher master, and substantive source inspection remain outside that result.

The table accounts for all spine positions. Prefix the displayed basenames with `item/xhtml/` to obtain the exact archive member. Use `PRO`, `C01` through the last numbered chapter, and `EPI` as literary section keys under the volume. The titles of the chapter headings can be recorded at admission if needed and subject to the reader's boundary.

| Role | V01–V06 (14 occurrences each) | V07 (16 occurrences) |
|---|---|---|
| Cover, title page, caution and navigation | 1–4, `p-cover.xhtml`, `p-titlepage.xhtml`, `p-caution-001.xhtml`, `p-toc.xhtml` | Same positions and members |
| Additional front matter | 5, `p-001.xhtml`, series/work half-title markers | 5–6, `p-001.xhtml` (imprint/copyright markers), `p-002.xhtml` (half-title markers) |
| Prologue | 6, `p-002.xhtml#toc-001` | 7, `p-003.xhtml#toc-001` |
| Numbered chapters in order | 7–9, `p-003.xhtml#toc-002`, `p-004.xhtml#toc-003`, `p-005.xhtml#toc-004` | 8–11, `p-004.xhtml#toc-002`, `p-005.xhtml#toc-003`, `p-006.xhtml#toc-004`, `p-007.xhtml#toc-005` |
| Epilogue | 10, `p-006.xhtml#toc-005` | 12, `p-008.xhtml#toc-006` |
| Back matter | 11–14, `p-007.xhtml` (author bio markers), `p-008.xhtml` (imprint, rights and promotion markers), `p-colophon.xhtml`, `p-caution-002.xhtml` | 13–16, `p-009.xhtml` (author bio markers), `p-010.xhtml` (promotion markers), `p-colophon.xhtml`, `p-caution-002.xhtml` |

The nine or ten positions outside the listed narrative span are provisional paratext dispositions per volume. No dedicated afterword is labeled in the navigation or detected by the inspected paratext markers. If a future bounded inspection identifies an afterword, reference list, bonus prose or ambiguous continuation, classify the precise span and record its status before using it. Spoiler-bearing paratext stays outside prospective reading and any extra narrative requires a scope decision. Cover and colophon imagery are paratext. V03 C02 and V05 C02 each contain one image reference in `item/xhtml/p-004.xhtml`, at `el[0804]` for `item/image/cid-00260_m_r.png` and `el[0585]` for `item/image/sa00084-aa.png` respectively. Inspect those at their authorized disclosure positions using `STILL_IMAGE` and record their function and any analytical consequences. Their visual content remains uninspected.

## Witness-bound locator

Record `volume / witness_alias / section / member / anchor`, with the witness alias resolving to the full SHA-256 above. The same member name is used in several volumes, sometimes for different sections. A locator always carries the volume, witness and case-sensitive path inside the ZIP. For a repeated spine resource or a member shared by sections, record the occurrence and the bounding native fragments as well.

1. Verify the EPUB SHA-256, resolve the package through the container, and resolve the literary section through the navigation, member and fragment. The spine records ordered package occurrences. Verify the literary boundaries in the admitted text, including any heading or framing before the fragment and any continuation at the far end.
2. Parse the member as XML using the XHTML namespace and XML document order. Inside its single XHTML `body`, count all descendant XHTML `p` elements from 1, including headings encoded as paragraphs, blank lines and layout paragraphs. Record `p[NNNN]` (zero-padded to at least four digits). Never reset at an internal scene break. If the target has a verified unique native `id` or `xml:id`, record that fragment too. Each of the 36 listed narrative members has one native paragraph ID at its section start. Those IDs locate headings, so ordinary passage retrieval uses ordinals. Bootstrap round-tripped first, middle and last ordinals in all 36 members without exposing their text.
3. For ranges, give both endpoints explicitly. If a heading, figure or other relevant node lies outside a paragraph, use its unique native ID or `el[NNNN]`, the one-based ordinal over all descendant elements of the same `body` in document order, across namespaces. For a figure also record the exact resolved asset path. If a finer text span is necessary, add zero-based half-open Unicode code-point offsets within the anchor. Count decoded text nodes in order, including tails, excluding the content of ruby annotation elements `rt`, `rp` and `rtc`. Use the XML parser's line-ending handling, with no further normalization, whitespace collapse or trimming. Evidence specifically about a ruby annotation names its ruby element and annotation. Preserve the native markup and both ruby layers when verifying a wording claim.
4. Re-resolve consequential citations on the exact witness and inspect their intended span, speaker and context. Use the actual member/fragment and a recoverable paragraph or element address even if a reader app offers a CFI or location number. XHTML filename numbers, spine positions, device pagination and print ISBN metadata supply no printed page number. If locator resolution fails, log the failure with affected evidence IDs, and repair the witness crosswalk or qualify the claim before acceptance.

## Coverage and source changes

Record actual coverage per witness and spine occurrence as it accrues. Each update records volume, witness, source section, occurrence/member/anchor span, observed role, requirement, access/inspection state, actor, basis and outstanding debt. Capture both endpoints of every literary unit, relevant paratext dispositions, omitted spans and why they are omitted, and any image claims. Recheck source-language legibility, ruby, punctuation, dialogue formatting and reading order at the actual first authorized use of a witness. An unresolved boundary, missing member, misleading rendering or inaccessible required image blocks the affected completion claim.

New bytes receive a new witness alias even when the package UUID, title or filename is reused. Retain the original locator and add an explicit verified crosswalk or mark the equivalence unresolved. Any alternate edition, translation, adaptation or related work remains outside the seven-witness corpus until separately admitted. Store EPUBs, text derivatives, credentials, private acquisition details and absolute machine paths in the evidence environment. The [analytical method](KSOA_ANALYTICAL_METHOD.md) and [sole current entrypoint](CURRENT_STATE_AND_CORPUS_MAP.md) govern admission.

## V01 source coverage

[V01 witness and coverage](readings/KSOA_V01_DEEP_READING.md#witness-and-coverage) binds every narrative span and accounts for the excluded paratext. The local SHA-256 matched the selected Japanese witness at reading. The narrative is read through [KSOA-V01-H-0013](readings/KSOA_V01_DEEP_READING.md#ksoa-v01-h-0013). Verification applies to the exact witnessed source and described inspection route. Full EPUBCheck and publisher-master equivalence remain unverified.

## V02 source coverage

[V02 witness and coverage](readings/KSOA_V02_DEEP_READING.md#witness-and-coverage) binds every narrative span and accounts for the excluded paratext. The local SHA-256 matched the selected Japanese witness at reading. The narrative is read through [KSOA-V02-H-0015](readings/KSOA_V02_DEEP_READING.md#ksoa-v02-h-0015). Verification applies to the exact witnessed source and described inspection route. Full EPUBCheck and publisher-master equivalence remain unverified.
