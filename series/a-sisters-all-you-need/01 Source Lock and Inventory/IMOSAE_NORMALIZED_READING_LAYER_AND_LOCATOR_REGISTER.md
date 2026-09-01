---
series: IMOSAE
artifact_type: normalized_reading_layer_register
scope: V01-V14_main_series
generation: V1
status: canonical
source_boundary: IMOSAE-JP-LN-RAW-1.0 Japanese numbered light-novel EPUBs
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
version: '1.1'
date: '2026-08-18'
normalization_spec_id: IMOSAE-NORM-SPEC-1.0
normalized_release_candidate: IMOSAE-JP-LN-NORM-1.0-RC1
normalized_release: IMOSAE-JP-LN-NORM-1.0
normalized_release_status: canonical_frozen
---

# IMOSAE Normalized Reading Layer and Locator Register
## 『妹さえいればいい。』 / *A Sister's All You Need*

## 0. Status and responsibility

This artifact records production of the complete loss-aware normalized reading layer for `IMOSAE-JP-LN-RAW-1.0`. It implements `IMOSAE-NORM-SPEC-1.0`, `IMOSAE-GAIJI-MAP-1.0`, and `IMOSAE-VISUAL-INDEX-1.0`.

The production pass first designated **`IMOSAE-JP-LN-NORM-1.0-RC1`** as a release candidate. `IMOSAE_PHASE0_SOURCE_LOCK_AND_NORMALIZATION_CLOSURE_AUDIT.md` subsequently verified the candidate and promoted its **unchanged 32-file payload** to the frozen canonical normalized authority **`IMOSAE-JP-LN-NORM-1.0`**.

## 1. Production result

| Measure | Result |
|---|---:|
| OPF spine items processed/classified | 981 / 981 |
| Normalized paragraph/block records | 34,766 |
| Ruby annotations | 29,083 |
| Gaiji annotations | 651 |
| Raw format/style annotations | 15,175 |
| Recognized semantic format annotations | 4,331 |
| Paragraph-level illustration anchors | 552 |
| Independent round-trip cases | 126 |
| Round-trip result | 126 PASS / 0 FAIL |
| Candidate manifest payload | 32 files / 69.14 MiB |

All 34,766 paragraph locators are unique. The layer reproduces the frozen corpus-wide counts of **29,083 ruby constructions** and **651 gaiji occurrences**, with 651/651 gaiji mapped and every annotation range valid.

## 2. Content-class inventory

| Content class | Spine items | Paragraph records |
|---|---:|---:|
| `MAIN_NARRATIVE` | 335 | 30,877 |
| `BONUS_FICTION` | 10 | 2,528 |
| `AUTHOR_AFTERWORD` | 44 | 264 |
| `ILLUSTRATION` | 305 | 305 |
| `TITLE_FRONTMATTER` | 124 | 380 |
| `COLOPHON` | 14 | 234 |
| `PROMOTIONAL` | 108 | 108 |
| `RETAILER_EBOOK_BONUS` | 27 | 27 |
| `OTHER_PARATEXT` | 14 | 43 |

### Explicit classification decisions

- Explicit `番外編`, `ぼーなすとらっく`, and V13 `妹さえいればいい。ＴＨＥ ＭＯＶＩＥ 妹・オブ・ザ・デッド` sections route to `BONUS_FICTION`. V13 itself states that the movie short is a prose rewrite of the special-edition drama-CD episode and is unrelated to the main story.
- V14 `青い小鳥たち` routes to `MAIN_NARRATIVE` despite following the first afterword because `あとがき２` explicitly reveals that the apparently extra episode became part of the main story.
- V07–V09 `ガガガ10周年電子特典 カバーイラスト` routes to `RETAILER_EBOOK_BONUS`; ordinary publisher advertisements and V08 `ガガガ文庫ＰＲ` route to `PROMOTIONAL`.
- Image-led narrative Q&A, document, profile, game/diagram, and illustration pages use the spine-level `ILLUSTRATION` class while their finer role remains in `IMOSAE-VISUAL-INDEX-1.0`.

## 3. Per-volume spine classification

| Vol. | Spines | Main | Bonus | Ill. | Afterword | Front | Colophon | Promo | Retail | Other |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V01 | 68 | 26 | 0 | 29 | 2 | 9 | 1 | 0 | 0 | 1 |
| V02 | 59 | 25 | 0 | 21 | 2 | 9 | 1 | 0 | 0 | 1 |
| V03 | 56 | 20 | 2 | 21 | 2 | 9 | 1 | 0 | 0 | 1 |
| V04 | 62 | 22 | 2 | 23 | 4 | 9 | 1 | 0 | 0 | 1 |
| V05 | 59 | 23 | 0 | 22 | 3 | 9 | 1 | 0 | 0 | 1 |
| V06 | 67 | 26 | 0 | 28 | 2 | 9 | 1 | 0 | 0 | 1 |
| V07 | 68 | 20 | 2 | 20 | 3 | 8 | 1 | 5 | 8 | 1 |
| V08 | 93 | 27 | 0 | 20 | 2 | 9 | 1 | 24 | 9 | 1 |
| V09 | 100 | 33 | 0 | 29 | 4 | 9 | 1 | 13 | 10 | 1 |
| V10 | 67 | 21 | 2 | 18 | 2 | 9 | 1 | 13 | 0 | 1 |
| V11 | 75 | 24 | 0 | 21 | 3 | 9 | 1 | 16 | 0 | 1 |
| V12 | 73 | 27 | 0 | 18 | 4 | 9 | 1 | 13 | 0 | 1 |
| V13 | 73 | 22 | 2 | 19 | 7 | 8 | 1 | 13 | 0 | 1 |
| V14 | 61 | 19 | 0 | 16 | 4 | 9 | 1 | 11 | 0 | 1 |

`machine_readable/spine_content_index.jsonl` holds all 981 rows. `spine_index` is zero-based OPF order; `spine_ordinal` is one-based.

## 4. Paragraph record and locator grammar

Full paragraph records live in `normalized_reading_layer/IMOSAE_VXX_NORMALIZED_PARAGRAPHS.jsonl` and carry source-block hashes, surface text, ruby, gaiji, format, and illustration arrays. Human/LLM-facing `IMOSAE_VXX_NORMALIZED_SOURCE.md` files preserve source order and locator comments.

```text
VXX|chapter:<label>|spine:NNN|xhtml:<member>|p:NNNN|fp:<12-char-SHA-prefix>
```

Example:

```text
V01|chapter:小説家は妹キチ●イ|spine:009|xhtml:OEBPS/Text/p-0009.xhtml.xhtml|p:0003|fp:7e55ba4d52a4
```

`spine` is zero-based, `p` is one-based within the emitted nonempty blocks of that XHTML member, and `fp` verifies the normalized surface string. `machine_readable/locator_index.jsonl` is the lean routing layer and points to the exact per-volume sidecar line containing the full record.

## 5. Loss-aware behavior

- **Ruby:** base text only in the surface stream; readings remain offset-addressed annotations.
- **Gaiji:** normalized by the frozen gaiji map while retaining ID/hash/class/replacement/confidence.
- **Non-gaiji images:** explicit `ILL` tokens and/or image-only visual locators preserve placement.
- **Typography:** raw class/style/tag carriers are retained; semantic labels distinguish analytically meaningful formatting from conversion plumbing.

### Recognized formatting signals

| Signal | Count |
|---|---:|
| `bold` | 1,482 |
| `tate_chu_yoko` | 1,181 |
| `centered` | 539 |
| `upright` | 507 |
| `size_change` | 479 |
| `sesame_emphasis` | 148 |

## 6. Validation

All structural invariants pass: 981/981 spines classified, 34,766/34,766 locators unique, 29,083 ruby annotations recovered, 651/651 gaiji mapped, no empty surface records, and all annotation offsets in range.

Independent round-trip validation uses **nine modes in every volume**: beginning, middle, end, ruby-heavy, gaiji-heavy, typography-heavy, dialogue, illustration-anchor, and chapter-boundary. For each sample the validator reopens the immutable EPUB, verifies the stored source-block SHA-256, then performs an independent BeautifulSoup-based text normalization and compares the resulting surface SHA-256 with the production record.

**Result: 126 PASS / 0 FAIL.** Detailed evidence is in `machine_readable/normalization_roundtrip_validation.json`.

## 7. Frozen normalized package

`IMOSAE-JP-LN-NORM-1.0` is the canonical frozen normalization release. Its 32-file payload is byte-identical to `IMOSAE-JP-LN-NORM-1.0-RC1`: fourteen normalized Markdown source files, fourteen full paragraph JSONL sidecars, the spine and locator indexes, and the two validation records. The payload totals **72,498,234 bytes**. `normalized_layer_checksums.sha256` remains the immutable payload checksum ledger.

The normalized layer is a retrieval/reading derivative and does **not** replace `IMOSAE-JP-LN-RAW-1.0` as primary textual authority. Exact disputes ultimately escalate to the frozen Japanese EPUBs.

The per-volume normalized Markdown files retain their generation-time `status: active_provisional` front-matter values so that RC1 can be promoted without mutating its verified bytes. Current authority is therefore resolved by `normalized_layer_manifest.json`, this register, the closure audit, and `CURRENT_STATE_AND_CORPUS_MAP.md`.

## 8. Phase-0 closure

`IMOSAE_PHASE0_SOURCE_LOCK_AND_NORMALIZATION_CLOSURE_AUDIT.md` reports **41/41 independent local closure checks PASS**, verifies the complete Drive mirror by name/byte size, and exact-byte re-fetches critical Drive artifacts. Phase 0 is **CLOSED**.

**`IMOSAE_V01_DEEP_READING.md` is now authorized as the next architecture-defined artifact.**
