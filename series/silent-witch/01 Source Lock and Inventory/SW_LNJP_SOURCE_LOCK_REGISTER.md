---
title: "Silent Witch — Japanese LN Source Lock Register"
artifact_id: SW_LNJP_SOURCE_LOCK_REGISTER
artifact_type: technical_source_lock
series: "Silent Witch: Secrets of the Silent Witch"
series_id: silent-witch
generation: V1
version: "1.9"
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
locked_units: [V02, V03, V04, AFTER04, V05]
literary_inspection: "V02 COMPLETE_CLOSED_2026-10-14; V03 COMPLETE_CLOSED_2026-10-14; V04 COMPLETE_CLOSED_2026-10-14; AFTER04 COMPLETE_CLOSED_2026-10-14; V05 COMPLETE_CLOSED_2026-10-14"
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

**Use in the V03 reading.** Every admitted image was viewed at source resolution; the full jacket was first viewed after the narrative had been read. The [V03 reading](../02%20Sequential%20Readings/SW_V03_DEEP_READING.md) cites 362 distinct locators, all present in the element map, and quotes 121 short fragments, each verified in the base text of a cited block. The classes held under full reading; no member was reclassified. A batch display put the text of preview members S36–S39 on screen; it was not used, and the exclusion is unchanged.

## V04 — `SW-LNJP-V04`

*Locked 2026-10-14, before any V04 narrative member was rendered for reading. The inspection suppressed the opening text of narrative-length members. The technical-sample receipt was displayed during the lock, which put two prologue passages on screen; the V04 entry freeze discloses them.*

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 04 [Japanese].epub |
| Bytes / SHA-256 | 17,309,899 / `a80f90953d625d304ae724a9b05a8c93ad3392e8bfd23e9edaeb6d0f9642fcfc`; equal to the source-map row and the retained audit. |
| OPF title / creator | サイレント・ウィッチ IV　沈黙の魔女の隠しごと / 依空 まつり |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | `B0B7R87LDV`, an ASIN, not an ISBN. |
| Electronic publication / revision | Colophon: 2022-08-10, ver.001. |
| Declared print basis | First edition, 2022-08-10. |
| Package form | Converted witness, like V01 and V03: OPF credits UnpackKindleS ver.20220126 and records modification 2022-10-24. |
| Archive | 89 members, CRC pass. 86 manifest resources; 46 XHTML documents, 44 declaring Japanese and the image-only cover undeclared; 7 stylesheets; 115 local references resolved, none external; 32 images decoded. |
| Navigation | EPUB nav 16 entries; NCX 13; the in-book linked contents 16, the publisher contents a further 2. |

**Spine and admission classes.** Paths share the prefix `OEBPS/Text/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel. |
| 5 | p-caution | Publisher notice; excluded. |
| 6–10 | p-toc-001, p-titlepage, p-001 credits, p-toc-002 illustrated contents, p-toc-003 linked contents | Source-identifying paratext. |
| 11 | p-002 | Prologue. |
| 12 | p-003 | Narrative illustration. |
| 13–20 | p-004 to p-011 | Chapters one to eight, in order. |
| 21 | p-012 | Narrative illustration inside chapter eight. |
| 22 | p-013 | Narrative continuation of chapter eight. |
| 23–25 | p-014 to p-016 | Chapters nine to eleven. |
| 26 | p-017 | Epilogue. |
| 27 | p-018 | Illustrated secret-episode heading. |
| 28 | p-019 | In-volume supplemental narrative, the secret episode. |
| 29–34 | p-020 to p-025 | Image-only character reference. |
| 35 | p-026 | Afterword, with one image. |
| 36 | p-999 | Image-only back-matter page outside the retained audit’s preview boundary; classified as image paratext by structure and to be viewed after the narrative, when its class is confirmed or corrected. |
| 37–41 | p-027 to p-031 | **Unrelated publisher preview**: 異世界ウォーキング　～エレージア王国編～, electronic trial edition. Exactly the five members in the retained audit; 235 blocks excluded. |
| 42 | p-allcover-001 | Full jacket; source-identifying paratext, not viewed before reading. |
| 43 | p-colophon | Edition paratext. |
| 44–45 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** 10,509 body elements and 4,581 blocks round-tripped. The narrative projection holds 4,229 blocks, 158,062 characters including line breaks and image placeholders. 1,443 ruby elements retained. Technical samples: S11:E000120, S11:E000011, S13:E000004, S26:E000397, S28:E000291. A second build reproduced the package SHA-256.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-V04_FIDELITY_LOCATORS_V1.zip; 18,492,474 bytes | `5ca9e2fbe7229789a1e2bdf8d0630ab2f4469a480c184a4a377e71481ba79978` |
| package-manifest.json | `60d32c796c0a8d930ba4278cb2e4703c5ceef620b1e958316f005e9fe175a1f7` |
| normalizer.py (generalized driver) | `4bd298eb44220135ecc55311accc4b712b9b0ee13857d485ee090192254fd5ff` |
| volume-config.json | `b82e5e56b9a34865cf7e3eee95f0624ebdaa6dfbb743f608b93db77980d6a3bf` |
| narrative-base.txt | `a9f752817b9ac82d62dda961c9c7a9032a4d42566f936d391e9b6e6d400c75b7` |
| block-map.jsonl | `92ab20f3a3295863136592523800678ca224dedbfc215af414dcbe10427dc64c` |
| element-locators.jsonl | `c621adf1f98d33511e9b61dd27e458835912074a6ad91f7a0e50c0151f91921f` |
| validation.json | `5200c04630d633735be8b23243bebdd177dc8e7539ba46d4d8f6cc1c4e5637a4` |

**Use in the V04 reading.** Every admitted image was viewed at source resolution; the jacket and the S36 back-matter image were first viewed after the narrative had been read, and S36 proved to be a publisher advertisement for IV -after-, confirming its class as image paratext excluded from narrative. The [V04 reading](../02%20Sequential%20Readings/SW_V04_DEEP_READING.md) cites 248 distinct locators, all present in the element map, and quotes 105 short fragments, each verified in the base text of a cited block. No member was reclassified. A search listing put one phrase of preview member S41 on screen; it was not used.

## IV -after- — `SW-LNJP-AFTER04`

*Locked 2026-10-14, before any narrative member of the companion was rendered for reading. It is a supplemental unit of the Japanese LN lane, admitted at its publication point after V04 under the placement audit recorded in the source and continuity map, and the architecture review recorded in the synthesis architecture. Before the lock, a lookup of the retained audit record printed its stored text samples. Four were narrative excerpts (from members p-003, p-009, p-015 and p-018) and one came from the afterword (p-028). The companion's entry freeze discloses them. The technical-sample receipt of this lock was not displayed.*

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 04 After [Japanese].epub |
| Bytes / SHA-256 | 23,490,806 / `101a1341d139a593c284010da5fb83f524183528ff4199d563346cb3254fc24a`; equal to the source-map row and the retained audit. |
| OPF title / creators | サイレント・ウィッチ IV -after-　沈黙の魔女の事件簿 / 依空 まつり, 藤実 なんな |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | `04074629A12033700000`, a store electronic code, not an ISBN. |
| Electronic publication / revision | Colophon: 2022-10-07, ver.001; OPF modification 2022-10-07. |
| Declared print basis | First edition, 2022-10-10. |
| Package form | The publisher's own layout (`item/standard.opf`, KADOKAWA reflow metadata 1.3.1), unlike the converted V01 to V04 witnesses. The OPF also carries a third-party extraction credit. The `mimetype` member is stored uncompressed with the correct value, but is the last ZIP member rather than the first. The retained audit records the same deviation. It is a packaging deviation, not a decode failure. |
| Archive | 93 members, CRC pass. 90 manifest resources; 46 XHTML documents, 45 declaring Japanese; 8 stylesheets; 118 local references resolved, none external; 36 images decoded. |
| Navigation | EPUB nav 21 entries; no NCX; the in-book linked contents 14. |

**Spine and admission classes.** Paths share the prefix `item/xhtml/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel. |
| 5 | p-caution | Publisher notice; excluded. |
| 6–10 | p-toc-001, p-titlepage, p-001 credits, p-toc-002 illustrated contents, p-toc-003 linked contents | Source-identifying paratext. |
| 11 | p-002 | Prologue heading image; narrative illustration. |
| 12 | p-003 | Prologue. |
| 13 | p-004 | First interlude. |
| 14–15 | p-005 heading image, p-006 | Case I. |
| 16 | p-007 | Second interlude. |
| 17–18 | p-008 heading image, p-009 | Case II. |
| 19 | p-010 | Third interlude. |
| 20–21 | p-011 heading image, p-012 | Case III. |
| 22 | p-013 | Fourth interlude. |
| 23–24 | p-014 heading image, p-015 | Case IV. |
| 25 | p-016 | Fifth interlude. |
| 26–27 | p-017 heading image, p-018 | Epilogue. |
| 28 | p-019 | Illustrated secret-episode heading. |
| 29 | p-020 | In-volume supplemental narrative, the secret episode. |
| 30–36 | p-021 to p-027 | Image-only character reference. |
| 37 | p-028 | Afterword. |
| 38–41 | p-029 to p-032 | **Unrelated publisher preview**: 璃寛皇国ひきこもり瑞兆妃伝, electronic trial edition. Exactly the four members in the retained audit; 392 blocks excluded. |
| 42 | p-allcover-001 | Full jacket; source-identifying paratext, not viewed before reading. |
| 43 | p-colophon | Edition paratext. |
| 44–45 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** 8,433 body elements and 4,406 blocks round-tripped. The narrative projection holds 3,885 blocks and 136,483 characters, excluding line delimiters. 1,489 ruby elements retained. Technical samples: S12:E000017, S12:E000014, S15:E000009, S27:E000289, S29:E000064. A second build reproduced the package SHA-256.

**Driver revision.** This witness required one change to the generalized driver: it now finds the `mimetype` member by name and records whether that member is first, where it had previously required it to be first. It also names the package form in the limitations. A rebuild of V04 with the revised driver reproduced every V04 package member byte for byte, except the embedded copy of the driver. The V01 to V04 seals therefore stand under the driver recorded with each.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-AFTER04_FIDELITY_LOCATORS_V1.zip; 22,869,640 bytes | `2b79b5d0db643b4999483ca2e43fc57fe9ceb03fdf6e21830a6582c81c6876e6` |
| package-manifest.json | `a9993bddbfc6d6cce9755654f5b0052b2f1c32dcee733c66db55822b13559dd9` |
| normalizer.py (generalized driver, revised) | `5ddc140dc21eff0eb70a6d99eaf715b9865a34d6eb9ab3ebfc23a59ec906b0f7` |
| volume-config.json | `b9bed55dc85fd9e9e8b95e48a6c883993333e3238650638e2f217da8b7a2550c` |
| narrative-base.txt | `ebc125ee0aa2c90766500881fe0ecba0e65bd150a03b8097ea412043c0968563` |
| block-map.jsonl | `42995868dab9402fec2a0f47efe6d50ed5464f9fa1bebb628db0c7547fc06984` |
| element-locators.jsonl | `0a60ef75a2168eea504e33cf6f52b7dacac07577357ba91a98a94294ce25c486` |
| validation.json | `a9c5e7a4cfaf5a9f3fb78128448da5b71a6df20ef3f0fe4ed173ebfdc4a56348` |

**Use in the IV -after- reading.** Thirty-one of the thirty-six image resources were viewed at source resolution. The cover and the jacket were first viewed after the narrative had been read. The four preview images and the store image were not viewed. The [IV -after- reading](../02%20Sequential%20Readings/SW_AFTER04_DEEP_READING.md) cites 226 distinct locators, all present in the element map, and quotes 51 short fragments, each verified in the base text of a cited block. No member was reclassified. A search listing put one copyright line of preview member S41 on screen; it was not used.

## V05 — `SW-LNJP-V05`

*Locked 2026-10-14, before any V05 narrative member was rendered for reading. The inspection suppressed the opening text of narrative-length members. It did print the whole of the 45-character member S30, a single line about winter spirits' ice bells ringing in the winter sky, together with the navigation's chapter titles. The V05 entry freeze discloses both. The technical-sample receipt and the retained audit's stored samples were not displayed.*

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 05 [Japanese].epub |
| Bytes / SHA-256 | 20,217,305 / `6fd815a38aea9b8e4d9dd96cd01f9a0fbf8a8fc3ccdb5173ff90046f1e99ca64`; equal to the source-map row and the retained audit. |
| OPF title / creators | サイレント・ウィッチ V　沈黙の魔女の隠しごと / 依空 まつり, 藤実 なんな |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | `04074628A12033600000`, a store electronic code, not an ISBN. |
| Electronic publication / revision | Colophon: 2023-02-10, ver.001; OPF modification 2023-02-10. |
| Declared print basis | First edition, 2023-02-10. |
| Package form | The publisher's own layout, like IV -after-. The OPF carries a third-party extraction credit. The `mimetype` member is uncompressed and correct but not first; the retained audit records the same deviation. |
| Archive | 92 members, CRC pass. 89 manifest resources; 50 XHTML documents, 49 declaring Japanese; 8 stylesheets; 123 local references resolved, none external; 31 images decoded. |
| Navigation | EPUB nav 23 entries; no NCX; the in-book linked contents 16. |

**Spine and admission classes.** Paths share the prefix `item/xhtml/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel. |
| 5 | p-caution | Publisher notice; excluded. |
| 6–10 | p-toc-001, p-titlepage, p-001 credits, p-toc-002 illustrated contents, p-toc-003 linked contents | Source-identifying paratext. |
| 11 | p-002 | Prologue, with one embedded image. |
| 12 | p-003 | Narrative illustration. |
| 13–19 | p-004 to p-010 | Chapters one to seven. |
| 20–22 | p-011 to p-013 | Image-only narrative illustrations, the second a spread. |
| 23 | p-014 | Short narrative member, 720 characters, outside the linked contents; admitted as narrative by structure. |
| 24–27 | p-015 to p-018 | Chapters eight to eleven. |
| 28 | p-019 | Epilogue. |
| 29 | p-020 | Image-only spread; narrative illustration. |
| 30 | p-021 | One-line narrative member after the spread. |
| 31 | p-022 | Illustrated secret-episode heading. |
| 32 | p-023 | In-volume supplemental narrative, the secret episode. |
| 33–39 | p-024 to p-030 | Image-only character reference. |
| 40 | p-031 | Afterword. |
| 41–45 | p-032 to p-036 | **Unrelated publisher preview**: 魔術師クノンは見えている, electronic trial edition. Exactly the five members in the retained audit; 391 blocks excluded. |
| 46 | p-allcover-001 | Full jacket; source-identifying paratext, not viewed before reading. |
| 47 | p-colophon | Edition paratext. |
| 48–49 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** 8,698 body elements and 4,640 blocks round-tripped. The narrative projection holds 4,132 blocks and 156,313 characters, excluding line delimiters. 1,506 ruby elements are retained. Technical samples: S11:E000045, S11:E000012, S13:E000004, S28:E000379, S32:E000120. A second build reproduced the package SHA-256 with the revised driver recorded at IV -after-.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-V05_FIDELITY_LOCATORS_V1.zip; 19,799,818 bytes | `599a61bd1297ad35d30eb4059892edc2e1f7cbd8eb02fbfff6d8bf9a9d837201` |
| package-manifest.json | `24d0ae5f5aa754c314fd3f431410869202db4ec6adbf30457728605479cfc9a0` |
| normalizer.py (generalized driver, revised) | `5ddc140dc21eff0eb70a6d99eaf715b9865a34d6eb9ab3ebfc23a59ec906b0f7` |
| volume-config.json | `d1ebd26a58a315843443c3775288246f23a788ea3d78dc9bd114623192c6cff0` |
| narrative-base.txt | `30973baac3b13a1d5f2c070431511c1a25c4f9c67b7e50a2103f894aa51aa049` |
| block-map.jsonl | `78b373e9254a42b87dc20edfb00e87d8e44844e41853c451922e3c0470af4607` |
| element-locators.jsonl | `79deff191ecd2686d533ce7e0d52fc55c646d02ffd42ae87abce6c071ea4876f` |
| validation.json | `7bd58d40c1112e70724198511f4900e2502f9bfe45bccb0fa3d6225e8e2aa01a` |

**Use in the V05 reading.** Twenty-four of the thirty-one image resources were viewed at source resolution, including the three image-set narrative members S20–S22, whose printed prose was paraphrased; the cover, title page, illustrated contents, store image, glyph and two preview images were not viewed. The full jacket was first viewed after the narrative. The [V05 reading](../02%20Sequential%20Readings/SW_V05_DEEP_READING.md) cites 220 distinct locators, all present in the element map, and quotes 51 short fragments, each verified in the base text of a cited block. No member was reclassified.
