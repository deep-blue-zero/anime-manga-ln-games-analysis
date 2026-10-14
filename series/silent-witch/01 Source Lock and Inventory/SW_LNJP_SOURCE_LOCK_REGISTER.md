---
title: "Silent Witch — Japanese LN Source Lock Register"
artifact_id: SW_LNJP_SOURCE_LOCK_REGISTER
artifact_type: technical_source_lock
series: "Silent Witch: Secrets of the Silent Witch"
series_id: silent-witch
generation: V1
version: "1.24"
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
locked_units: [V02, V03, V04, AFTER04, V05, V06, V07, V08, V09, EXTRA09, SW-LNJP-V10, SW-LNJP-V11, V12]
literary_inspection: "V02 COMPLETE_CLOSED_2026-10-14; V03 COMPLETE_CLOSED_2026-10-14; V04 COMPLETE_CLOSED_2026-10-14; AFTER04 COMPLETE_CLOSED_2026-10-14; V05 COMPLETE_CLOSED_2026-10-14; V06 COMPLETE_CLOSED_2026-10-14; V07 COMPLETE_CLOSED_2026-10-14; V08 COMPLETE_CLOSED_2026-10-14; V09 COMPLETE_CLOSED_2026-10-14; EXTRA09 COMPLETE_CLOSED_2026-10-14; V10 COMPLETE_CLOSED_2026-10-14; V11 COMPLETE_CLOSED_2026-10-14"
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

## V06 — `SW-LNJP-V06`

*Locked 2026-10-14, before any V06 narrative member was rendered for reading. The inspection suppressed the opening text of narrative-length members and printed the navigation's chapter titles, which the V06 entry freeze discloses. No narrative member was printed. The technical-sample receipt and the retained audit's stored samples were not displayed.*

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 06 [Japanese].epub |
| Bytes / SHA-256 | 21,414,746 / `7909cd94b71063033b96b49ec1f7c6b686f49edb637a43b187e500ebad3a7242`; equal to the source-map row and the retained audit. |
| OPF title / creators | サイレント・ウィッチ VI　沈黙の魔女の隠しごと / 依空 まつり, 藤実 なんな |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | `04075090A14827500000`, a store electronic code, not an ISBN. |
| Electronic publication / revision | Colophon: 2023-08-10, ver.001; OPF modification 2023-08-10. |
| Declared print basis | First edition, 2023-08-10. |
| Package form | The publisher's own layout, like IV -after- and V05. The OPF carries a third-party extraction credit. The `mimetype` member is uncompressed and correct but not first; the retained audit records the same deviation. |
| Archive | 92 members, CRC pass. 89 manifest resources; 49 XHTML documents, 48 declaring Japanese; 8 stylesheets; 121 local references resolved, none external; 32 images decoded. |
| Navigation | EPUB nav 23 entries; no NCX; the in-book linked contents 16. |

**Spine and admission classes.** Paths share the prefix `item/xhtml/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel. |
| 5 | p-caution | Publisher notice; excluded. |
| 6–10 | p-toc-001, p-titlepage, p-001 credits, p-toc-002 illustrated contents, p-toc-003 linked contents | Source-identifying paratext. |
| 11 | p-002 | Prologue. |
| 12 | p-003 | Narrative illustration. |
| 13–20 | p-004 to p-011 | Chapters one to eight. |
| 21 | p-012 | Image-only spread inside chapter eight; narrative illustration. |
| 22 | p-013 | Continuation of chapter eight, outside the linked contents; narrative by structure. |
| 23–26 | p-014 to p-017 | Chapters nine to eleven and the epilogue. |
| 27 | p-018 | Illustrated secret-episode heading. |
| 28 | p-019 | In-volume supplemental narrative, the secret episode, with one image. |
| 29 | p-020 | Image-only page after the secret episode; narrative illustration by structure, to be confirmed on viewing. |
| 30–38 | p-021 to p-029 | Image-only character reference. |
| 39 | p-030 | Afterword. |
| 40–44 | p-031 to p-035 | **Unrelated publisher preview**: 泡沫に神は微睡む 1, electronic trial edition. Exactly the five members in the retained audit; 282 blocks excluded. |
| 45 | p-allcover-001 | Full jacket; not viewed before reading. |
| 46 | p-colophon | Edition paratext. |
| 47–48 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** 9,008 body elements and 4,630 blocks round-tripped. The narrative projection holds 4,237 blocks and 162,162 characters, excluding line delimiters. 1,612 ruby elements are retained. Technical samples: S11:E000022, S11:E000013, S13:E000004, S26:E000316, S28:E000156. A second build reproduced the package SHA-256 with the revised driver.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-V06_FIDELITY_LOCATORS_V1.zip; 21,082,034 bytes | `60690bbc9da0a594040f69bc2d26314319537d187e42581fa5cdbb970040502a` |
| package-manifest.json | `fd50ea6bf57da2bbc0ecb57fc8395f7075af83570018655fb635e40bec2c149b` |
| normalizer.py (generalized driver, revised) | `5ddc140dc21eff0eb70a6d99eaf715b9865a34d6eb9ab3ebfc23a59ec906b0f7` |
| volume-config.json | `f17174705d808f8fb86bb26b3d4a9a07eb7ea3f47eea6b8d1aea8cb99b562deb` |
| narrative-base.txt | `d8ee87b1a3ae6b61667bd5f654a821b672d6263efa113cb75cdcb1aa5a6bdd9a` |
| block-map.jsonl | `a893f8137569672c2f15ed075e01547b65365faa6b16471a4b0ff15c61a9c975` |
| element-locators.jsonl | `46310602671bafc5a06bd6016e130451bdba0a41502ba53276a46430c231eb7c` |
| validation.json | `982f8933de50164cd1d9c7ec0eeb0d073543a5f9faf5ef9db7cfda20a611f9c6` |

**Use in the V06 reading.** Twenty-five of the thirty-two image resources were viewed at source resolution, including the full jacket after the narrative; the cover, title page, illustrated contents, store image, glyph and two preview images were not viewed. S29, left to be confirmed on viewing, is a one-line notice that the story continues in VII; its class is unchanged. The [V06 reading](../02%20Sequential%20Readings/SW_V06_DEEP_READING.md) cites 293 distinct locators, all present in the element map, and quotes 41 short fragments, each verified in the base text of a cited block. No member was reclassified.

## V07 — `SW-LNJP-V07`

*Locked 2026-10-14, before any V07 narrative member was rendered for reading. The inspection suppressed the opening text of narrative-length members and printed the navigation's chapter titles, which the V07 entry freeze discloses. It also printed the opening line of two members of the unrelated publisher preview. No V07 narrative member was printed. The technical-sample receipt and the retained audit's stored samples were not displayed.*

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 07 [Japanese].epub |
| Bytes / SHA-256 | 20,577,485 / `e586cacacab692e3ee530737d28170e5a06f74cfb8eb9437f0b1f94df9badd86`; equal to the source-map row and the retained audit. |
| OPF title / creators | サイレント・ウィッチ VII　沈黙の魔女の隠しごと / 依空 まつり, 藤実 なんな |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | `04075093A14827800000`, a store electronic code, not an ISBN. |
| Electronic publication / revision | Colophon: 2024-02-09, ver.001; OPF modification 2024-02-09. |
| Declared print basis | First edition, 2024-02-10. |
| Package form | The publisher's own layout, like V05 and V06. Unlike them, the `mimetype` member is first, uncompressed and correct; the retained audit agrees. |
| Archive | 102 members, CRC pass. 94 manifest resources; 53 XHTML documents, 52 declaring Japanese; 8 stylesheets; 130 local references resolved, none external; 33 images decoded. |
| Navigation | EPUB nav 25 entries; no NCX; the in-book linked contents 18. |

**Spine and admission classes.** Paths share the prefix `item/xhtml/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel. |
| 5 | p-caution | Publisher notice; excluded. |
| 6–10 | p-toc-001, p-titlepage, p-001 credits, p-toc-002 illustrated contents, p-toc-003 linked contents | Source-identifying paratext. |
| 11 | p-002 | Prologue, with one image. |
| 12 | p-003 | Narrative illustration. |
| 13–18 | p-004 to p-009 | Chapters one to six. |
| 19 | p-010 | Image-only spread after chapter six's first member; narrative illustration. |
| 20 | p-011 | Short text member outside the linked contents; narrative by structure. |
| 21 | p-012 | Image-only spread; narrative illustration. |
| 22 | p-013 | Text member outside the linked contents, with one image; narrative by structure. |
| 23–29 | p-014 to p-020 | Chapters seven to thirteen. |
| 30 | p-021 | Epilogue. |
| 31 | p-022 | Illustrated secret-episode heading. |
| 32 | p-023 | In-volume supplemental narrative, the secret episode. |
| 33 | p-024 | Image-only page after the secret episode; narrative illustration by structure, to be confirmed on viewing. |
| 34–42 | p-025 to p-033 | Image-only character reference. |
| 43 | p-034 | Afterword. |
| 44–48 | p-035 to p-039 | **Unrelated publisher preview**: 稀代の悪女、三度目の人生で【無才無能】を楽しむ, electronic trial edition. Exactly the five members in the retained audit; 299 blocks excluded. |
| 49 | p-allcover-001 | Full jacket; not viewed before reading. |
| 50 | p-colophon | Edition paratext. |
| 51–52 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** 8,218 body elements and 4,503 blocks round-tripped. The narrative projection holds 4,095 blocks and 147,096 characters, excluding line delimiters. 1,375 ruby elements are retained. Technical samples: S11:E000025, S11:E000013, S13:E000004, S30:E000318, S32:E000036. A second build reproduced the package SHA-256 with the revised driver.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-V07_FIDELITY_LOCATORS_V1.zip; 21,629,539 bytes | `9513343b9b088f2736bdb4358b8acfebaf621872c9414d15bc2cfa61fcf40ff1` |
| package-manifest.json | `a15d2860adcd52da4fde1ebd4094ea98c2d1bdc13d425007df7cada0649e1c5d` |
| normalizer.py (generalized driver, revised) | `5ddc140dc21eff0eb70a6d99eaf715b9865a34d6eb9ab3ebfc23a59ec906b0f7` |
| volume-config.json | `dd55965fd0d34eb9a7efb1279abfca8ab4b9dfc98cfd214ae7774d408f120307` |
| narrative-base.txt | `0c184c789c54630e43a9803908b453dddb3a115c4193347f1b714c3d7cdd6540` |
| block-map.jsonl | `4a6e55d0364cdb56ad99e4a9e9ecbf17aaf1dd07511c6ab4e2d636fd0d105fb0` |
| element-locators.jsonl | `404f38b27eaadf2d3c2b07810dae34494a0b903aedf89ff9e1162a15cd295371` |
| validation.json | `9585fb7e8ef4e0dab627b4b609964b3e5d1574e33f207534f47d4759c4dec676` |

**Use in the V07 reading.** Twenty-four of the thirty-three image resources were viewed at source resolution, including the full jacket after the narrative; the cover, title page, illustrated contents, store image, glyph and preview images were not viewed. S33, left to be confirmed on viewing, is a one-line notice that the story continues in VIII; its class is unchanged. The [V07 reading](../02%20Sequential%20Readings/SW_V07_DEEP_READING.md) cites 275 distinct locators, all present in the element map, and quotes 42 short fragments, each verified in the base text of a cited block. No member was reclassified.

## V08 — `SW-LNJP-V08`

*Locked 2026-10-14, before any V08 narrative member was rendered for reading. The inspection suppressed the opening text of narrative-length members and printed the navigation's chapter titles, which the V08 entry freeze discloses. It also printed the opening line of one short narrative member, S27, and of two members of the unrelated publisher preview; the entry freeze discloses both. The technical-sample receipt and the retained audit's stored samples were not displayed.*

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 08 [Japanese].epub |
| Bytes / SHA-256 | 19,650,208 / `89ff209d8fe16c76486772adb2fb926849ede965ebdc8e8a614bbf9dccb401e9`; equal to the source-map row and the retained audit. |
| OPF title / creators | サイレント・ウィッチ VIII　沈黙の魔女の隠しごと / 依空 まつり, 藤実 なんな |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | `04075563A18727900000`, a store electronic code, not an ISBN. |
| Electronic publication / revision | Colophon: 2024-08-09, ver.001; OPF modification 2024-08-09. |
| Declared print basis | First edition, 2024-08-10. |
| Package form | The publisher's own layout, like V05 to V07. As in V07, the `mimetype` member is first, uncompressed and correct; the retained audit agrees. |
| Archive | 94 members, CRC pass. 91 manifest resources; 50 XHTML documents, 49 declaring Japanese; 8 stylesheets; 127 local references resolved, none external; 33 images decoded. |
| Navigation | EPUB nav 25 entries; no NCX; the in-book linked contents 18. |

**Spine and admission classes.** Paths share the prefix `item/xhtml/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel. |
| 5 | p-caution | Publisher notice; excluded. |
| 6–10 | p-toc-001, p-titlepage, p-001 credits, p-toc-002 illustrated contents, p-toc-003 linked contents | Source-identifying paratext. |
| 11 | p-002 | Prologue, with one image. |
| 12 | p-003 | Image-only page; narrative illustration. |
| 13–25 | p-004 to p-016 | Chapters one to thirteen. |
| 26 | p-017 | Epilogue, with one image. |
| 27 | p-018 | Short text member outside the linked contents; narrative by structure. Its opening line was printed at inspection. |
| 28–29 | p-019, p-020 | Image-only spread and page; narrative illustration by structure, to be confirmed on viewing. |
| 30 | p-021 | Image-only secret-episode heading; narrative illustration. |
| 31 | p-022 | In-volume supplemental narrative, the secret episode. |
| 32–40 | p-023 to p-031 | Image-only character reference. |
| 41 | p-032 | Afterword. |
| 42–45 | p-033 to p-036 | **Unrelated publisher preview**: 図書館の天才少女　～本好きの新人官吏は膨大な知識で国を救います！～, electronic trial edition. Exactly the four members in the retained audit; 311 blocks excluded. |
| 46 | p-allcover-001 | Full jacket; not viewed before reading. |
| 47 | p-colophon | Edition paratext. |
| 48–49 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** 8,270 body elements and 4,786 blocks round-tripped. The narrative projection holds 4,377 blocks and 157,808 characters, excluding line delimiters. 1,254 ruby elements are retained. Technical samples: S11:E000017, S11:E000028, S13:E000004, S26:E000295, S31:E000095. A second build reproduced the package SHA-256 with the revised driver.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-V08_FIDELITY_LOCATORS_V1.zip; 20,774,032 bytes | `7c78d938613bfc7ed40051b7d2fa2689c9d78e6ba4e8b9e97887ff0099af9c02` |
| package-manifest.json | `7b0c62047861caee52a92f58afd356eae1bd554913b845123ea80c4dae589305` |
| normalizer.py (generalized driver, revised) | `5ddc140dc21eff0eb70a6d99eaf715b9865a34d6eb9ab3ebfc23a59ec906b0f7` |
| volume-config.json | `c426e98298f1dc4fed9d6a44f3881c99bd77438967a442e4f075ac40bb7eba3b` |
| narrative-base.txt | `905b4ae0efed96ae726db3ec310400b8f982bf0e50aca0cfb9dfb8469197bbce` |
| block-map.jsonl | `163f526d735f817bdecfe7faae2f487c34990c01323d41cb9db7e2b17d28bfe5` |
| element-locators.jsonl | `d9bbd14a970be990216a950f4e3aee50749e6e573edba6fc0fdc21a5e6515830` |
| validation.json | `8d1e3b71fd8571b94990ecf661d4ca4595d246eaa2af6790deb7259ac7fd09a7` |

**Use in the V08 reading.** Twenty-five of the thirty-three image resources were viewed at source resolution, including the full jacket after the narrative; the cover, title page, illustrated contents, store image, glyph and three preview images were not viewed. S28 and S29, left to be confirmed on viewing, are a narrative plate of the robed Monica with Isabelle and a one-line notice that the story continues in IX; their classes are unchanged. The [V08 reading](../02%20Sequential%20Readings/SW_V08_DEEP_READING.md) cites 342 distinct locators, all present in the element map, and quotes 86 short fragments, each verified in the base text of a cited block. No member was reclassified.

## V09 — `SW-LNJP-V09`

*Locked 2026-10-14, before any V09 narrative member was rendered for reading. The inspection suppressed the opening text of narrative-length members and printed the navigation's chapter titles, which the V09 entry freeze discloses. It printed the opening line of the fan-letter notice S39 and no narrative text. The colophon date was read earlier, at V08 closure, to place IX -extra-. The technical-sample receipt and the retained audit's stored samples were not displayed.*

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 09 [Japanese].epub |
| Bytes / SHA-256 | 3,055,000 / `272d49df5b94927cacc2b7a6fa430a3b0af58228cb048541b46ebc29fcdaffb1`; equal to the source-map row and the retained audit. |
| OPF title / creators | サイレント・ウィッチ IX 沈黙の魔女の隠しごと / 依空 まつり, 藤実 なんな |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | `04075813A20788900000`, a store electronic code, not an ISBN; the OPF also carries `calibre:11` and a UUID. |
| Electronic publication / revision | Colophon: 2025-02-10, ver.001; OPF modification 2025-02-10. |
| Declared print basis | First edition, 2025-02-10. |
| Package form | A converted witness, unlike V05 to V08. The OPF is `item/volume.opf`, credits calibre 7.25.0 as book producer and carries Google Ebooks processing metadata, while keeping the KADOKAWA reflow metadata 1.3.1. The 27 images total about 2.9 MB, far smaller than in V08, so image resolution may be reduced. The `mimetype` member is first, uncompressed and correct; the retained audit agrees. |
| Archive | 84 members, CRC pass. 80 manifest resources; 44 XHTML documents, 43 declaring Japanese; 8 stylesheets; 108 local references resolved, none external; 27 images decoded. |
| Navigation | EPUB nav 22 entries; no NCX; the in-book linked contents 20. |
| Publisher preview | None; the retained audit lists no promotional section. |

**Spine and admission classes.** Paths share the prefix `item/xhtml/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel. |
| 5 | p-titlepage | Source-identifying title page. |
| 6 | p-caution | Publisher notice; excluded. |
| 7–9 | p-001 credits, p-toc-001 illustrated contents, p-toc-002 linked contents | Source-identifying paratext. |
| 10 | p-002 | Prologue. |
| 11 | p-003 | Image-only page; narrative illustration. |
| 12 | p-004 | Chapter one, with one image. |
| 13 | p-005 | Image-only spread; narrative illustration. |
| 14–20 | p-006 to p-012 | Chapters two to eight. |
| 21 | p-013 | Image-only spread; narrative illustration. |
| 22 | p-014 | Text member outside the linked contents; narrative by structure. |
| 23–26 | p-015 to p-018 | Chapters nine to twelve. |
| 27 | p-019 | Epilogue. |
| 28–36 | p-020 to p-028 | Image-only character reference. |
| 37 | p-029 | Afterword. |
| 38 | p-030 | Image-only advertisement; excluded, to be confirmed on viewing. |
| 39 | p-031 | Fan-letter address notice; excluded. |
| 40 | p-allcover-001 | Full jacket; not viewed before reading. |
| 41 | p-colophon | Edition paratext. |
| 42–43 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** 8,298 body elements and 3,786 blocks round-tripped. The narrative projection holds 3,665 blocks and 129,541 characters, excluding line delimiters. 1,064 ruby elements are retained. Technical samples: S10:E000034, S10:E000006, S12:E000006, S27:E000483. A second build reproduced the package SHA-256 with the revised driver.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-V09_FIDELITY_LOCATORS_V1.zip; 4,033,065 bytes | `96d54804937f7c61c94c00636c868b6b5c4cb46a3918f37e7f13032d1f695c89` |
| package-manifest.json | `a7ddd601350f8ab9c8616e13a7a62cac85139f9433c7122507b731017dca90bd` |
| normalizer.py (generalized driver, revised) | `5ddc140dc21eff0eb70a6d99eaf715b9865a34d6eb9ab3ebfc23a59ec906b0f7` |
| volume-config.json | `0199c56af7aa366094c403c05808de00fa67cf8aeb76cfb564a3edcc289da748` |
| narrative-base.txt | `e0b80c7fd58a61fe6363e5b080244710976016d73ea929281749916a2faecb80` |
| block-map.jsonl | `36e0103be6ab5f988d385572a86ffc76183483d765df3a33767f685956741d16` |
| element-locators.jsonl | `8cc6011eb86eddb457e6e923f1e2f8b524458d98e0ed752857a9dd4633110b6d` |
| validation.json | `3008ae829ba2e825a9446353079685b3e21095010ec9d4e339fdcce358d0bce4` |

**Use in the V09 reading.** Twenty-two of the twenty-seven image resources were viewed at the witness’s resolution, including the full jacket after the narrative, whose blurb is illegible. The cover, title page, illustrated contents, store image and S38 were not viewed. The afterword identifies S38 as the V10 preview page; it remains excluded and unviewed. The [V09 reading](../02%20Sequential%20Readings/SW_V09_DEEP_READING.md) cites 215 distinct locators, all present in the element map, and quotes 37 short fragments, each verified in the base text of a cited block. No member was reclassified.

## IX -extra- — `SW-LNJP-EXTRA09`

*Locked 2026-10-14, before any IX -extra- narrative member was rendered for reading.*

- The inspection suppressed the opening text of narrative-length members.
- It printed the chapter labels from the NCX and the in-book contents, which the companion's entry freeze discloses. The labels include each chapter's placement note.
- It printed the opening line of the fan-letter notice.
- One provenance page, S55, was classified by counting fixed words in it. The counted words were 初出, 特典, 店舗 and 書き下ろし; none of its text was printed.
- The colophon date had been read at V08 closure.
- The technical-sample receipt and the retained audit's stored samples were not displayed.

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 09 Extra [Japanese].epub |
| Bytes / SHA-256 | 31,848,077 / `ec2157d37e9eb301ed6d2e2eebe2adee215c22a354189bed7485ea8485f1c943`; equal to the source-map row and the retained audit. |
| OPF title / creators | サイレント・ウィッチ IX -extra- 沈黙の魔女の短編集 / 依空 まつり, 藤実 なんな |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | A UUID only; no store code or ISBN in the OPF. |
| Electronic publication / revision | Colophon: 2025-06-10, read as text; the normalizer's colophon fields are empty for this markup. The OPF carries an implausible early `dc:date` and a modification date of 2025-06-10, as the source map warned. |
| Package form | A converted EPUB 2 witness: root `content.opf`, calibre 8.4.0 as book producer, a Sigil 2.4.2 marker, a calibre cover wrapper at the root, an NCX and no navigation document. 59 members reference a reader-specific script, `js/kobo.js`, that is absent from the archive. The `mimetype` member is first, uncompressed and correct; the retained audit agrees. |
| Archive | 109 members, CRC pass. 106 manifest resources; 60 XHTML documents, 59 declaring Japanese and the calibre wrapper English; 2 stylesheets; 176 local references resolved, none external; 59 dangling script references counted; 43 images decoded. |
| Navigation | No EPUB navigation document; NCX 15 entries; the in-book linked contents 12. |
| Publisher preview | None; the retained audit lists no promotional section. |

**Driver revision.** The generalized driver was revised a second time, for this witness only. Two changes were made:

- A missing EPUB navigation document now yields no navigation entries instead of a failure.
- Script references whose target is absent from the archive are counted and recorded as a limitation instead of failing; no text or image depends on them.

Earlier packages keep the driver copy sealed inside them and are unaffected.

**Spine and admission classes.** Paths share the prefix `item/xhtml/` except S01.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | titlepage.xhtml (root) | Calibre cover wrapper; source-identifying. |
| 2 | p-cover | Source-identifying cover. |
| 3–4 | p-fmatter-001, 002 | Colour frontispieces; visual channel. |
| 5 | p-titlepage | Source-identifying title page. |
| 6 | p-caution | Publisher notice; excluded. |
| 7 | p-toc-001 | Linked contents; source-identifying. |
| 8 | p-001 | Image-only page before the design materials; visual channel, to be confirmed on viewing. |
| 9–38 | p-002 to p-031 | Thirty image-only pages of character design materials; in-volume reference paratext. |
| 39 | p-032 | Image-only collection title page; narrative illustration. |
| 40 | p-033 | Prologue. |
| 41 | p-034 | Image-only short-story-collection heading; narrative illustration. |
| 42–48 | p-035, p-036, p-037 in two split members, p-038 to p-040 | Chapters one to five. |
| 49 | p-041 | Image-only epilogue heading; narrative illustration. |
| 50 | p-042 | Epilogue text. |
| 51 | p-043 | Image-only page; narrative illustration, to be confirmed on viewing. |
| 52 | p-044 | Image-only secret-episode heading; narrative illustration. |
| 53 | p-045 | In-volume supplemental narrative, the secret episode. |
| 54 | p-046 | Afterword. |
| 55 | p-047 | Provenance list of the collected stories; paratext, read after the narrative. |
| 56 | p-048 | Fan-letter notice; excluded. |
| 57 | p-allcover-001 | Full jacket; not viewed before reading. |
| 58 | p-colophon | Edition paratext. |
| 59–60 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** 15,885 body elements and 5,918 blocks round-tripped. The narrative projection holds 5,638 blocks and 154,075 characters, excluding line delimiters. 1,104 ruby elements are retained. Technical samples: S40:E000156, S40:E000017, S42:E000004, S50:E000352, S53:E000537. A second build reproduced the package SHA-256 with the twice-revised driver.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-EXTRA09_FIDELITY_LOCATORS_V1.zip; 33,196,194 bytes | `879b6dde8db56125f1289c73f91a33b1a8d9fd590a9b9d1e235ef6207219dc25` |
| package-manifest.json | `de0ef4e2a9cf6d96d54c0bc5ab420fe009d773ed9e1c936a3a99253f40e4d434` |
| normalizer.py (generalized driver, second revision) | `6500076874627f9e0739d9dd76e6c49e33667f7c88f72db42e58b536ca3371b5` |
| volume-config.json | `e696cdf972d668dac13af99b97b76526a7a3b125e405a6c4d9968eaa3110fe20` |
| narrative-base.txt | `4a550e5cf2989b097da6198bb01de51e6db40c99d23762be755da0d236ba76ce` |
| block-map.jsonl | `d88429177c976cdca35f78c9264b0d3a21bec2102a1e3c13c529b54e1099f6e9` |
| element-locators.jsonl | `33427aee87823ef3635bd17028001051191795289f1c80e1178ac5884116861c` |
| validation.json | `c33c6b70cae2af8b876939fcb7f619139b6ba90f8abaf33edc37158dc684d793` |

**Use in the IX -extra- reading.** Thirty-nine of the forty-three image resources were viewed, including all thirty pages of design materials and, after the narrative, the full jacket. The cover, the title page, the store image and an inline star glyph were not viewed. S08 proved to be a credits page and S51 a one-line continuation notice; neither was reclassified. The [IX -extra- reading](../02%20Sequential%20Readings/SW_EXTRA09_DEEP_READING.md) cites 205 distinct locators, all present in the element map, and quotes 12 short fragments, each verified in the base text of a cited block.

## V10 — `SW-LNJP-V10`

*Locked 2026-10-14, before any V10 narrative member was rendered for reading.*

The inspection did the following:

- It suppressed the opening text of narrative-length members.
- It printed the navigation labels and the in-book contents. These give the prologue, an interlude, ten chapters, the epilogue, the secret episode, a character list and the afterword; the entry freeze discloses them.
- It printed the publisher-preview boundary, with the preview's title and the opening of its blurb. The preview is an unrelated work.
- It printed the opening lines of the publisher notices.

The technical-sample receipt and the retained audit's stored samples were not displayed.

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 10 [Japanese].epub |
| Bytes / SHA-256 | 17,190,113 / `54d547b09f690895a0561104130bf088bd82d3a0c46734773a2c3c5a5a42c9c1`; equal to the retained audit. |
| OPF title / creators | サイレント・ウィッチ X　沈黙の魔女の隠しごと / 依空　まつり, 藤実　なんな |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | A store e-code; no ISBN in the OPF. |
| Electronic publication / revision | Colophon: 2025-07-10, ver.001, based on the first print edition of 2025-07-10; OPF modification date 2025-07-10. |
| Package form | Publisher layout, EPUB 3: `item/standard.opf`, a navigation document and an in-book linked contents. The `mimetype` member is first, uncompressed and correct. |
| Archive | 92 members, CRC pass. 84 manifest resources; 47 XHTML documents; 30 image members, 29 image uses decoded; 116 local references resolved, none external. |
| Navigation | Navigation document with 20 labels and 3 landmarks; in-book linked contents. |
| Publisher preview | S38–S42, a trial edition of an unrelated title; excluded by class `publisher_preview`, 442 blocks; it matches the retained audit's promotional section. |

**Spine and admission classes.** Paths share the prefix `item/xhtml/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel. |
| 5 | p-caution | Publisher notice; excluded. |
| 6 | p-toc-001 | Linked contents; source-identifying. |
| 7 | p-titlepage | Source-identifying title page. |
| 8 | p-001 | Credits; source-identifying. |
| 9 | p-toc-002 | Illustrated contents image; source-identifying. |
| 10 | p-toc-003 | Text contents; source-identifying. |
| 11 | p-002 | Prologue. |
| 12 | p-003 | Interlude. |
| 13 | p-004 | Image-only page; narrative illustration. |
| 14–21 | p-005 to p-012 | Chapters one to eight; chapter eight begins at S21. |
| 22 | p-013 | Image-only spread; narrative illustration. |
| 23 | p-014 | Continuation of chapter eight. |
| 24–25 | p-015, p-016 | Chapters nine and ten. |
| 26 | p-017 | Epilogue. |
| 27–28 | p-018, p-019 | Image-only pages; narrative illustration. The secret episode's label points to S28. |
| 29 | p-020 | In-volume supplemental narrative, the secret episode. |
| 30 | p-021 | Image-only page; narrative illustration, to be confirmed on viewing. |
| 31–36 | p-022 to p-027 | Image-only character list; in-volume reference paratext. |
| 37 | p-028 | Afterword. |
| 38–42 | p-029 to p-033 | Unrelated publisher preview; excluded. |
| 43 | p-allcover-001 | Full jacket; not viewed before reading. |
| 44 | p-colophon | Edition paratext. |
| 45–46 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** The second revision of the generalized driver was used unchanged.

- 7,638 body elements and 4,379 blocks round-tripped.
- The narrative projection holds 3,820 blocks and 136,706 characters, excluding line delimiters.
- 1,204 ruby elements are retained.
- A second build reproduced the package SHA-256.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-V10_FIDELITY_LOCATORS_V1.zip; 18,194,855 bytes | `626017a5f23e52cdbc05c5093c77814c612d4ec4a3d73a8950593e7a3e596579` |
| package-manifest.json | `a7afdd42e71370921c97743ea0d6d6e8ecbce7bc9b20f5dffa0cf7a0eae5fe0b` |
| normalizer.py (generalized driver, second revision) | `6500076874627f9e0739d9dd76e6c49e33667f7c88f72db42e58b536ca3371b5` |
| volume-config.json | `174fd5fd8aed07e03943cb6ecc2523e289e8bc405912756f63226954737b8140` |
| narrative-base.txt | `1492102acd33efb7c035b98e00c210821c377137f1fd19ba0fc220b22ec2ffe3` |
| block-map.jsonl | `aa131d7004a8579b4410b78739ab8a4f16d10224e49f4f95d56c3f59e0298f8f` |
| element-locators.jsonl | `987c441e000d3b35d979c18f92e6f49bd55a06e8d187130d01cc9a3388218b4e` |
| validation.json | `e081bbe32d778be9f85032588b5b0a1139b720e9d77cafbd2bce796ca761fa99` |

**Use in the V10 reading.** Twenty-three of the twenty-nine image resources were viewed, including the map, the character list and, after the narrative, the full jacket. The cover, title page, store image and the three preview images were not viewed. S30 proved to be a map of the kingdom and is used as paratext; it was not reclassified. The [V10 reading](../02%20Sequential%20Readings/SW_V10_DEEP_READING.md) cites 210 distinct locators, all present in the element map, and quotes 21 short fragments, each verified in the base text of a cited block.

## V11 — `SW-LNJP-V11`

*Locked 2026-10-14, before any V11 narrative member was rendered for reading.*

The inspection did the following:

- It suppressed the opening text of narrative-length members.
- It printed the navigation labels and the in-book contents. These give the prologue, twelve chapters, the epilogue, the secret episode, a character list and the afterword; the entry freeze discloses them.
- It printed the publisher-preview boundary, with the preview's title and the opening of its blurb. The preview is an unrelated work.
- It printed the opening lines of the publisher notices.

The technical-sample receipt and the retained audit's stored samples were not displayed.

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 11 [Japanese].epub |
| Bytes / SHA-256 | 18,283,771 / `cb81975b7967cf61f050a7fea53b39b13d627eb70af56e26af025e85c4207a4a`; equal to the retained audit. |
| OPF title / creators | サイレント・ウィッチ XI　沈黙の魔女の隠しごと / 依空　まつり, 藤実　なんな |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | A store e-code; no ISBN in the OPF. |
| Electronic publication / revision | Colophon: electronic 2026-01-09, ver.001, based on the first print edition of 2026-01-10. OPF modification date 2026-01-09. |
| Package form | Publisher layout, EPUB 3: `item/standard.opf`, a navigation document and an in-book linked contents. The `mimetype` member is first, uncompressed and correct. |
| Archive | 90 members, CRC pass. 82 manifest resources; 45 XHTML documents; 29 image uses decoded; 116 local references resolved, none external. |
| Navigation | Navigation document with 20 labels and 3 landmarks; in-book linked contents. |
| Publisher preview | S36–S40, a trial edition of an unrelated title; excluded by class `publisher_preview`, 362 blocks; it matches the retained audit's promotional section. |

**Spine and admission classes.** Paths share the prefix `item/xhtml/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel. |
| 5 | p-caution | Publisher notice; excluded. |
| 6 | p-toc-001 | Linked contents; source-identifying. |
| 7 | p-titlepage | Source-identifying title page. |
| 8 | p-001 | Credits; source-identifying. |
| 9 | p-toc-002 | Illustrated contents image; source-identifying. |
| 10 | p-toc-003 | Text contents; source-identifying. |
| 11 | p-002 | Prologue. |
| 12 | p-003 | Image-only page; narrative illustration. |
| 13–24 | p-004 to p-015 | Chapters one to twelve. |
| 25 | p-016 | Epilogue. |
| 26 | p-017 | Image-only secret-episode heading; narrative illustration. |
| 27 | p-018 | In-volume supplemental narrative, the secret episode. |
| 28 | p-019 | Image-only page; narrative illustration, to be confirmed on viewing. |
| 29–34 | p-020 to p-025 | Image-only character list; in-volume reference paratext. |
| 35 | p-026 | Afterword. |
| 36–40 | p-027 to p-031 | Unrelated publisher preview; excluded. |
| 41 | p-allcover-001 | Full jacket; not viewed before reading. |
| 42 | p-colophon | Edition paratext. |
| 43–44 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** The second revision of the generalized driver was used unchanged.

- 7,352 body elements and 4,320 blocks round-tripped.
- The narrative projection holds 3,837 blocks and 139,071 characters, excluding line delimiters.
- 1,068 ruby elements are retained.
- A second build reproduced the package SHA-256.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-V11_FIDELITY_LOCATORS_V1.zip; 19,274,462 bytes | `47bbefa0b90452380d688ddd910aa0b7bce34b2a36d9017352ac209236596650` |
| package-manifest.json | `8fcb715d70fe49193f24f7623d000cedfba7857b4432015660403c793359c689` |
| normalizer.py (generalized driver, second revision) | `6500076874627f9e0739d9dd76e6c49e33667f7c88f72db42e58b536ca3371b5` |
| volume-config.json | `e1a76719284cc07affc0afba1f440b36d11cfb98c9ff0f460dc5ba757e57b6cc` |
| narrative-base.txt | `f11fdce32e915e6ac8d4179df6cfbc3a950565a61c2f42f4eb6cf2d546b0eddd` |
| block-map.jsonl | `acc2a16fe200005e9d9f3cb6681f7e7f30aec2dbc44e9f6f82570227fa8bc6e2` |
| element-locators.jsonl | `23d11b682db061143291d40d93218f72b5a836db52587fd294e02d9b3cfb956e` |
| validation.json | `8ca09110bb909c0da20919c7fd4237ddb137994a7289e3ca783e1fdaa568c4ea` |

**Use in the V11 reading.** Twenty-four of the twenty-nine image resources were viewed, including the map, the character list and, after the narrative, the full jacket. The cover, title page, store image and the two preview images were not viewed. S28 proved to be a map of the kingdom and is used as paratext; it was not reclassified. The [V11 reading](../02%20Sequential%20Readings/SW_V11_DEEP_READING.md) cites 269 distinct locators, all present in the element map, and quotes 8 short fragments, each verified in the base text of a cited block.

## V12 — `SW-LNJP-V12`

*Locked 2026-10-14, before any V12 narrative member was rendered for reading.*

The inspection did the following:

- It suppressed the opening text of narrative-length members.
- It printed the navigation labels and the in-book contents. These give the prologue, thirteen chapters with an interlude after the eighth, the epilogue, the secret episode, a character list and the afterword; the entry freeze discloses them.
- It printed the publisher-preview boundary, with the preview's title and the opening of its blurb. The preview is an unrelated work.
- It printed the opening lines of the publisher notices, including a short letters-address page.

The technical-sample receipt and the retained audit's stored samples were not displayed.

| Field | Verified value |
|---|---|
| Collection filename | Secrets of the Silent Witch - Volume 12 [Japanese].epub |
| Bytes / SHA-256 | 20,781,154 / `91ed29af0e3031de6167f09952767a479ed87de5045d5fb11aec4b8060663c37`; equal to the retained audit. |
| OPF title / creators | サイレント・ウィッチ XII　沈黙の魔女の隠しごと / 依空　まつり, 藤実　なんな |
| Publisher / imprint | 株式会社ＫＡＤＯＫＡＷＡ / カドカワBOOKS |
| Identifier | A store e-code; no ISBN in the OPF. |
| Electronic publication / revision | Colophon: electronic 2026-06-10, ver.001, based on the first print edition of 2026-06-10. OPF modification date 2026-06-10. |
| Package form | Publisher layout, EPUB 3: `item/standard.opf`, a navigation document and an in-book linked contents. The `mimetype` member is first, uncompressed and correct. |
| Archive | 90 members, CRC pass. 87 manifest resources; 47 XHTML documents; 32 image uses decoded; 125 local references resolved, none external. |
| Navigation | Navigation document with 23 labels and 3 landmarks; in-book linked contents. |
| Publisher preview | S39–S42, a trial edition of an unrelated title; excluded by class `publisher_preview`, 221 blocks; it matches the retained audit's promotional section. |

**Spine and admission classes.** Paths share the prefix `item/xhtml/`.

| Spine | Member(s) | Class / admission |
|---|---|---|
| 1 | p-cover | Source-identifying cover. |
| 2–4 | p-fmatter-001 to 003 | Colour frontispieces; visual channel. |
| 5 | p-caution | Publisher notice; excluded. |
| 6 | p-toc-001 | Linked contents; source-identifying. |
| 7 | p-titlepage | Source-identifying title page. |
| 8 | p-001 | Credits; source-identifying. |
| 9 | p-toc-002 | Illustrated contents image; source-identifying. |
| 10 | p-toc-003 | Text contents; source-identifying. |
| 11 | p-002 | Prologue. |
| 12 | p-003 | Image-only page; narrative illustration. |
| 13–20 | p-004 to p-011 | Chapters one to eight. |
| 21 | p-012 | Interlude. |
| 22–26 | p-013 to p-017 | Chapters nine to thirteen. |
| 27 | p-018 | Epilogue. |
| 28 | p-019 | Image-only secret-episode heading; narrative illustration. |
| 29 | p-020 | In-volume supplemental narrative, the secret episode. |
| 30–35 | p-021 to p-026 | Image-only character list; in-volume reference paratext. |
| 36 | p-099 | Image-only back-matter page; in-volume reference paratext, to be confirmed on viewing. |
| 37 | p-027 | Afterword. |
| 38 | p-999 | Letters-address notice; excluded. |
| 39–42 | p-028 to p-031 | Unrelated publisher preview; excluded. |
| 43 | p-allcover-001 | Full jacket; not viewed before reading. |
| 44 | p-colophon | Edition paratext. |
| 45–46 | p-colophon2, p-bookwalker | Rights notice and store image; excluded. |

**Normalization.** The second revision of the generalized driver was used unchanged.

- 8,436 body elements and 4,507 blocks round-tripped.
- The narrative projection holds 4,140 blocks and 157,340 characters, excluding line delimiters.
- 1,412 ruby elements are retained.
- A second build reproduced the package SHA-256.

| Local object | SHA-256 |
|---|---|
| SW-LNJP-V12_FIDELITY_LOCATORS_V1.zip; 21,993,292 bytes | `0006b5eb48b33e768e471720edc1f753b039d77ede3e8cd903834fcbd40458e7` |
| package-manifest.json | `4b3a801c432611055a6fcf2ab18b0f3134f4ce56163bc27a6d4b193461d40de6` |
| normalizer.py (generalized driver, second revision) | `6500076874627f9e0739d9dd76e6c49e33667f7c88f72db42e58b536ca3371b5` |
| volume-config.json | `42c5baa4755a438a66ab093067486de7f52ec489a861eb03b944ef15ea47cbcb` |
| narrative-base.txt | `773a2de5e546130c61f066357b443558f8eda2649faceb14ed7f336f504573ff` |
| block-map.jsonl | `c7825bfbbf40c325ab9d34671f243edac2f73daba40ae1b123ea8170e906d5d4` |
| element-locators.jsonl | `347c5d23fe3310f6658babaeb60f5a124fa9095bb012a4f4517662a28541809b` |
| validation.json | `62931868cb19544393c4e96f33565130fd0e1a0d273d1912b2f9ba64d8761f8c` |
