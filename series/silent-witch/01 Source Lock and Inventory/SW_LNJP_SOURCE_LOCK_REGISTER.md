---
title: "Silent Witch — Japanese LN Source Lock Register"
artifact_id: SW_LNJP_SOURCE_LOCK_REGISTER
artifact_type: technical_source_lock
series: "Silent Witch: Secrets of the Silent Witch"
series_id: silent-witch
generation: V1
version: "1.2"
last_updated: "2026-10-14"
status: canonical
scope: "Exact supplied witness, usable resources, admission classes and local derivative seals for each Japanese LN unit locked after V01"
source_boundary: "Technical source validation only; literary findings live in the deep readings and the master ledger."
created: "2026-10-14"
canonical_home: "series/silent-witch/01 Source Lock and Inventory/SW_LNJP_SOURCE_LOCK_REGISTER.md"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
evidence_retention: LOCAL_ONLY_OWNER_REQUEST
locked_units: [V02, V03]
literary_inspection: "V02 COMPLETE_CLOSED_2026-10-14"
---

# Japanese LN source lock register

This register holds the technical source lock of every Japanese LN unit after V01, one section per unit, in the order the units are locked. V01 keeps its own [dedicated lock](SW_LNJP_V01_SOURCE_LOCK.md), which established the method used here. A lock fixes exact bytes, edition identity, the admission class of every spine member and the seals of the local evidence package. It is not a reading. The [source map](SW_SOURCE_AND_CONTINUITY_MAP.md) owns the inventory, witness lanes and admission decisions; the [current corpus map](../CURRENT_STATE_AND_CORPUS_MAP.md) owns the live run state.

## Shared procedure

Every unit in this register is locked the same way.

1. **Bytes.** The EPUB is copied from the owner’s local collection, which the owner named as the primary route. Its SHA-256 and size are computed locally and compared with the source-map row and the retained audit manifest, whose own SHA-256 is `2ddd2ec5721e77658ae25d2534e2e7b93ac1dd475ce015c8d82ccf9a2b9c26da`. Hash, size and the complete spine path list must match exactly.
2. **Archive and resources.** Every ZIP member passes CRC with a unique, safe name. The mimetype member is correct, first, uncompressed and has no local extra field. No encryption descriptor is present. Every manifest resource and spine reference resolves, every XHTML document parses with entity resolution and network access disabled, every local href, src and CSS url resolves with its fragment, and every raster image fully decodes.
3. **Classification.** Every spine member receives an explicit class and admission state from the method’s list, decided by technical inspection of structure, the publisher’s navigation and the image-only members. Classification does not read narrative prose. Publisher previews named in the retained audit’s `promotional_sections` must be classified as previews, and nothing else may be: the driver asserts both directions.
4. **Normalization.** The evidence package is built with `SW_EPUB_FIDELITY_V1`, the V01 normalizer’s rules run through a generalized driver whose only per-volume input is a configuration file of witness identity and classifications. On 2026-10-14, run against V01 with V01’s classifications, the driver reproduced V01’s original narrative projection, fidelity trees, image index and navigation byte for byte, and every element-locator and block-map field except the auxiliary chapter-label field, which V01 derived by hand. Locators, base text, element ordinals and round trips are therefore the same rules. The driver adds two technical cases V01 lacked: XML comments are not elements and are not counted, but their tail text is kept, as an independent ElementTree parse also does; and ZIP directory entries, which carry no bytes, are listed rather than copied.
5. **Round trips and determinism.** Every mapped element and block is recovered from an independently parsed copy of the original XHTML. Five technical samples, covering ordinary dialogue, ruby-bearing text, a chapter boundary, the last main passage and the final admitted passage, are checked for extraction fidelity only. A second build must reproduce the package SHA-256 exactly.
6. **Retention.** The EPUB copy, the package and every derivative stay in the local evidence directory. Nothing is uploaded to Git or Drive. Seals below identify those local files.

Locator grammar is the V01 grammar with the unit’s witness ID: `SW-LNJP-V<NN>:S<two-digit spine>:E<six-digit element>`.

Common limitations: each witness is a supplied reflowable EPUB whose equivalence with a publisher-original file is unverified; EPUBCheck and reader-app rendering are not run; image filenames that look like page numbers are resource names, not verified printed pagination; mechanical counts do not establish reading.

## V02 — `SW-LNJP-V02`

*Locked 2026-10-14, before any V02 narrative member was opened.*

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 02 [Japanese].epub |
| Bytes / SHA-256 | 16,295,034 / `aafafc8ff6ea9c722f007e3f559364ca25e1d3c61addb747466ea986f8864ab6`; equal to the source-map row and the retained audit. |
| OPF title / creators | サイレント・ウィッチ II　沈黙の魔女の隠しごと / 依空 まつり, 藤実 なんな |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | `04074224A10353400000`, a store e-code, not an ISBN. |
| Electronic publication / revision | Colophon: 2021-10-08, ver.001. OPF modified 2021-10-08. |
| Declared print basis | First edition, 2021-10-10. |
| Package form | Publisher-structured EPUB 3 (`item/standard.opf`, KADOKAWA reflow metadata), unlike V01’s converted witness. |
| Archive | 88 members, CRC pass; 5 empty directory entries listed, not copied. 80 manifest resources; 43 XHTML documents, all declaring Japanese; 8 stylesheets; 112 local references resolved, none external; 29 images decoded. |
| Navigation | EPUB nav with 23 entries; no NCX. The in-book linked contents has 16 entries and the publisher contents a further 2. |

**Spine and admission classes.** Paths share the prefix `item/xhtml/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel, read as images. |
| 5 | p-caution | Publisher notice; excluded. |
| 6–10 | p-toc-001, p-titlepage, p-001 credits, p-toc-002 illustrated contents, p-toc-003 linked contents | Source-identifying paratext. |
| 11 | p-002 | Prologue. |
| 12 | p-003 | Narrative illustration. |
| 13–23 | p-004 to p-014 | Chapters one to eleven, in order. |
| 24 | p-015 | Narrative illustration, a two-page spread. |
| 25 | p-016 | Narrative continuation after the spread, opening with a scene break; part of chapter eleven, not a new unit. |
| 26 | p-017 | Epilogue. |
| 27 | p-018 | Illustrated secret-episode heading. |
| 28 | p-019 | In-volume supplemental narrative, the secret episode. |
| 29–33 | p-020 to p-024 | Image-only character reference; separate reference paratext channel. |
| 34 | p-025 | Afterword; author commentary. |
| 35–38 | p-026 to p-029 | **Unrelated publisher preview**: 百花宮のお掃除係, electronic trial edition. Exactly the four members in the retained audit; 373 blocks excluded from the narrative projection. The only gaiji image in the archive is inside this preview. |
| 39 | p-allcover-001 | Full jacket with blurb; source-identifying paratext. |
| 40 | p-colophon | Edition paratext. |
| 41–42 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** 9,453 body elements and 5,040 blocks round-tripped. The narrative projection holds 4,550 blocks, 169,672 characters including line breaks and image placeholders. 1,645 ruby elements retained. Technical samples: S11:E000030, S11:E000011, S13:E000004, S26:E000610, S28:E000248. A second build reproduced the package SHA-256.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-V02_FIDELITY_LOCATORS_V1.zip; 17,503,973 bytes | `61404a18dfb6fd197c33aef2a4c0aeda1df9b47868116930128174dd4ee6e9bf` |
| package-manifest.json | `2886ef2fde95ecf687bf2cefe9ad8480983b5c8d3e0d4b0f9b87c3937062ab01` |
| normalizer.py (generalized driver) | `4bd298eb44220135ecc55311accc4b712b9b0ee13857d485ee090192254fd5ff` |
| volume-config.json | `2d3662d5d9e132ff3ad7f3ab9ceeb6562d7f4c6b3178c41dfa968aa9d96555e1` |
| narrative-base.txt | `da66928b3568e979cef9d5577702927c17d6949293f051b7ead7774869e02964` |
| block-map.jsonl | `7e0264405c68739d2b62cfd8d37467284c629e05c75a9faa4772a2f459bda3fd` |
| element-locators.jsonl | `969d56d38700b6983b5032338a7a0a6aa93ba3f8c73073c44bf052a002298c3f` |
| validation.json | `2d36de183e56661ca09d18ddd2954570162cbf06502b0bd8fe9eb379261698a4` |

**Use in the V02 reading.** Every admitted image was viewed at source resolution; the [V02 reading](../02%20Sequential%20Readings/SW_V02_DEEP_READING.md) cites 479 distinct locators, all present in the element map, and quotes 29 short fragments, each verified in the base text of a cited block. The classes held under full reading; no member was reclassified.

## V03 — `SW-LNJP-V03`

*Locked 2026-10-14, before any V03 narrative member was rendered for reading. From V03 the technical inspection suppresses the opening text of narrative-length members; the V02 and V03 inspections did print 24-character heads, disclosed in each volume’s entry freeze.*

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 03 [Japanese].epub |
| Bytes / SHA-256 | 16,512,601 / `38989102ddc9848024e67fd9d241bb4a1d4b24db166d39b663c7311a2d86efa9`; equal to the source-map row and the retained audit. |
| OPF title / creator | サイレント・ウィッチ III　沈黙の魔女の隠しごと / 依空 まつり |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | `B09R957MLJ`, an ASIN, not an ISBN. |
| Electronic publication / revision | Colophon: 2022-02-10, ver.001. |
| Declared print basis | First edition, 2022-02-10. |
| Package form | Converted witness, like V01: OPF credits UnpackKindleS ver.20220126 and records modification 2022-07-16. |
| Archive | 87 members, CRC pass. 84 manifest resources; 45 XHTML documents, 43 declaring Japanese and the image-only cover undeclared; 7 stylesheets; 119 local references resolved, none external; 31 images decoded. |
| Navigation | EPUB nav 22 entries; NCX 19; the in-book linked contents 16, the publisher contents a further 2. |

**Spine and admission classes.** Paths share the prefix `OEBPS/Text/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel. |
| 5 | p-caution | Publisher notice; excluded. |
| 6–10 | p-toc-001, p-titlepage, p-001 credits, p-toc-002 illustrated contents, p-toc-003 linked contents | Source-identifying paratext. |
| 11 | p-002 | Prologue. |
| 12 | p-003 | Narrative illustration. |
| 13–23 | p-004 to p-014 | Chapters one to eleven, in order. |
| 24 | p-015 | Narrative illustration. |
| 25 | p-016 | Narrative continuation of chapter eleven. |
| 26 | p-017 | Epilogue. |
| 27 | p-018 | Illustrated secret-episode heading. |
| 28 | p-019 | In-volume supplemental narrative, the secret episode. |
| 29–34 | p-020 to p-025 | Image-only character reference. |
| 35 | p-026 | Afterword. |
| 36–40 | p-027 to p-031 | **Unrelated publisher preview**: 聖女じゃなかったので、王宮でのんびりご飯を作ることにしました, electronic trial edition. Exactly the five members in the retained audit; 331 blocks excluded. |
| 41 | p-allcover-001 | Full jacket; source-identifying paratext. |
| 42 | p-colophon | Edition paratext. |
| 43–44 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** 11,543 body elements and 5,036 blocks round-tripped. The narrative projection holds 4,620 blocks, 169,761 characters including line breaks and image placeholders. 1,618 ruby elements retained. Technical samples: S11:E000068, S11:E000013, S13:E000004, S26:E000740, S28:E000355. A second build reproduced the package SHA-256.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-V03_FIDELITY_LOCATORS_V1.zip; 17,795,276 bytes | `5110d9e3ef5e1272f3ee2e861abae78c46c62a0823fc70d07a64022f3ee16c84` |
| package-manifest.json | `91c86a9f1f960e3069c9093fe00cb2ce6e121f9f90be638ed3a31ee3f425cff1` |
| normalizer.py (generalized driver) | `4bd298eb44220135ecc55311accc4b712b9b0ee13857d485ee090192254fd5ff` |
| volume-config.json | `4e352223b56997b0368ff6e50a2cb7cc5d9e913020fc95151e531e13ad139b92` |
| narrative-base.txt | `77dd140c58402265f84b49435a0b439d51a12e7c20f9d33784040942721b4712` |
| block-map.jsonl | `35578e64cc69039648d00fae67214d71e35a68c466341c1d1d61884ff026cb64` |
| element-locators.jsonl | `f2c3f6849be534b48982d4349a7773f1f430f0dff47483a57cc0f849e0f1c2f6` |
| validation.json | `465a3e1055d5f7a7b2ca870c84f0c44cd42fbe1e835955de75bba94ea5182b3d` |
