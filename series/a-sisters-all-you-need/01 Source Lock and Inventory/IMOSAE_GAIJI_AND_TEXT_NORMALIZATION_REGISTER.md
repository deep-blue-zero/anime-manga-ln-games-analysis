---
series: IMOSAE
artifact_type: source_normalization_register
scope: V01-V14_main_series
generation: V1
status: canonical
source_boundary: IMOSAE-JP-LN-RAW-1.0 Japanese numbered light-novel EPUBs
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
version: '1.0'
date: '2026-08-18'
gaiji_map_id: IMOSAE-GAIJI-MAP-1.0
normalization_spec_id: IMOSAE-NORM-SPEC-1.0
normalized_release_status: not_yet_frozen
---

# IMOSAE Gaiji and Text Normalization Register
## 『妹さえいればいい。』 / *A Sister's All You Need*

## 0. Status and purpose

This register closes the **gaiji identification and normalization-rule** portion of Phase 0 for the locked source set `IMOSAE-JP-LN-RAW-1.0`. It does **not** yet freeze the final normalized reading release. The future derived release identifier `IMOSAE-JP-LN-NORM-1.0` remains reserved until spine classification, illustration/paratext anchoring, locator generation, and round-trip validation have all passed.

The exhaustive census contains **651 gaiji occurrences represented by 65 distinct binary image hashes**. Every distinct asset has now been assigned a stable `IMOSAE-G###` identifier and a deterministic handling rule. The normalization prototype successfully handled **651/651 occurrences** without an unmapped gaiji.

Of the 651 occurrences, **280** can receive a direct text/symbol substitution in the normalized reading stream. The remaining **371** are intentionally preserved as explicit semantic tokens because flattening them to ordinary text would lose their role as scene ornaments, kaomoji/emoji, or a formally ambiguous title symbol.

> **No lexically meaningful gaiji remains unresolved.** The only deliberately non-literal cases are image-based expressive/structural elements where a fake Unicode transcription would be less faithful than an explicit source-linked token.

## 1. Authority and immutability rules

1. The raw EPUBs remain immutable and authoritative. Nothing in this register rewrites their bytes.
2. `IMOSAE-GAIJI-MAP-1.0` is the canonical mapping for the 65 gaiji hashes found in `IMOSAE-JP-LN-RAW-1.0`.
3. Stable gaiji IDs are never renumbered. If a later source generation or supplement introduces a new image gaiji, allocate the next unused ID after `IMOSAE-G065`.
4. Resolution is keyed by **full SHA-256 of the image bytes**, not by filename. Reused filenames such as `embed0006.jpg` do not imply identical semantic content across EPUBs.
5. Where the same semantic ornament has multiple binary renderings, the individual IDs remain separate for provenance but may share one normalized semantic token.
6. Any future change to a replacement requires an explicit register revision and delta; do not silently mutate the map.

## 2. Canonical normalized text model

The normalized layer will use a **loss-aware reading stream plus structured annotations**, rather than a single flattened TXT file pretending that all EPUB markup is ordinary prose.

### 2.1 Surface reading stream

The reading stream contains:

- ordinary Japanese Unicode text in source order;
- ruby **base text only** in the visible prose stream;
- high-confidence gaiji substitutions from this register;
- explicit semantic tokens for image elements that should not be falsified as ordinary text;
- paragraph boundaries preserved from the XHTML structure.

It must never concatenate ruby bases and readings into malformed forms such as `瞳ひとみ`.

### 2.2 Ruby annotation

Each ruby construction is stored separately as at least:

```json
{"base":"瞳","reading":"ひとみ"}
```

The current corpus contains **29,083 ruby constructions**. Ruby readings remain searchable evidence but are not duplicated into the canonical surface string.

### 2.3 Gaiji annotation

Every gaiji occurrence retains:

- `gaiji_id`;
- full asset SHA-256;
- source volume;
- XHTML member;
- original asset path;
- gaiji class;
- normalized replacement/token;
- confidence;
- occurrence context.

This makes a textual substitution reversible to its source image.

### 2.4 Typography/form annotation

The evidence layer must preserve markers for sesame emphasis, bold/strong text, size changes, tate-chū-yoko, centering, unusual spacing, and image-only textual constructions. A reading view may suppress some markup for legibility, but the evidence record may not discard it.

A prototype scan found **2,357 nodes carrying one of the currently recognized formatting signals**. This is a routing count, not yet the final typography inventory; Phase 0.8 will refine it.

### 2.5 Unicode normalization

- Ordinary text should be retained as encoded unless a transformation is explicitly documented.
- Do not convert Japanese width/style distinctions globally merely for cosmetic consistency.
- Nonstandard dakuten gaiji are represented as base kana plus combining dakuten `U+3099` where no standard precomposed kana exists, while retaining the gaiji annotation. Example: `あ` + `U+3099`.
- Dice images may be rendered as Unicode die faces `⚀`–`⚅`, with the numeric value retained in the gaiji map.

## 3. Gaiji class census

| Class | Distinct IDs | Occurrences | Normalization rule |
|---|---:|---:|---|
| `LEXICAL_GLYPH` | 3 | 59 | Direct Unicode character. |
| `COMPOSITE_TEXT_GLYPH` | 1 | 3 | Direct textual expansion while preserving source-gaiji annotation. |
| `NONSTANDARD_DAKUTEN` | 11 | 35 | Base kana + combining dakuten; preserve image provenance. |
| `DIE_FACE` | 15 | 160 | Unicode die face plus numeric semantic value. |
| `DECORATED_TEXT` | 5 | 5 | Recover underlying text; retain decoration/form annotation. |
| `LOGOTYPE_TEXT` | 6 | 8 | Recover underlying characters; retain logotype/form annotation. |
| `EXPRESSIVE_MARK` | 2 | 2 | Direct textual mark where visually unambiguous. |
| `PROLONGATION_MARK` | 2 | 6 | Normalize segment to `―`; paired source segments remain provenance-visible. |
| `PUNCTUATION` | 1 | 2 | Direct punctuation substitute. |
| `TITLE_SYMBOL` | 2 | 6 | Preserve semantic token; search alias may be used separately. |
| `KAOMOJI_EMOJI` | 13 | 17 | Preserve explicit gaiji token; do not invent exact Unicode transcription. |
| `STRUCTURAL_ORNAMENT` | 4 | 348 | Preserve structural token in evidence view; may be suppressed in prose-only search view. |

## 4. Full gaiji register

Full 64-character hashes, all source paths, dimensions, and sample contexts are retained in `machine_readable/gaiji_map.json`. The Markdown table uses a 12-character hash prefix for readability.

| ID | Occ. | Volumes | Hash prefix | Class | Canonical replacement / token | Confidence | Notes |
|---|---:|---|---|---|---|---|---|
| `IMOSAE-G001` | 56 | V01, V06 | `38ce9af50e4d` | `LEXICAL_GLYPH` | `訊` | high | Ordinary kanji gaiji; e.g. 訊ねる. |
| `IMOSAE-G002` | 215 | V01, V02, V04, V06, V09, V10, V11, V12, V13, V14 | `7518e17eb1a7` | `STRUCTURAL_ORNAMENT` | `⟦ORNAMENT:IMOUTO_SEAL⟧` | high | Standalone centered section/scene divider; do not inject 妹 into prose. |
| `IMOSAE-G003` | 1 | V01 | `8ef6dc9accaf` | `NONSTANDARD_DAKUTEN` | `お゙` | high | Expressive nonstandard voiced kana. |
| `IMOSAE-G004` | 14 | V01, V02, V04, V11, V12, V14 | `62e1b9a23b2e` | `NONSTANDARD_DAKUTEN` | `あ゙` | high | Expressive nonstandard voiced kana. |
| `IMOSAE-G005` | 2 | V01, V14 | `553f0fe232d9` | `LEXICAL_GLYPH` | `吐` | high | Ordinary kanji gaiji. |
| `IMOSAE-G006` | 2 | V01 | `d4907093889c` | `NONSTANDARD_DAKUTEN` | `に゙` | high | Expressive/slurred nonstandard voiced kana. |
| `IMOSAE-G007` | 1 | V01 | `0a60785f5a9d` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G007⟧` | high | Semantics/function clear; exact Unicode transcription would be lossy. |
| `IMOSAE-G008` | 1 | V01 | `091bf1e54512` | `NONSTANDARD_DAKUTEN` | `オ゙` | high | Expressive nonstandard voiced katakana. |
| `IMOSAE-G009` | 11 | V01, V02, V04 | `fd06b555502d` | `DIE_FACE` | `⚃` | high | Unicode die-face replacement; numeric semantic value 4. |
| `IMOSAE-G010` | 8 | V01, V02, V04 | `2d0e33d765d5` | `DIE_FACE` | `⚄` | high | Unicode die-face replacement; numeric semantic value 5. |
| `IMOSAE-G011` | 2 | V01 | `74a9d17cbefb` | `DIE_FACE` | `⚂` | high | Unicode die-face replacement; numeric semantic value 3. |
| `IMOSAE-G012` | 10 | V01, V02, V04 | `fc558f046ae5` | `DIE_FACE` | `⚅` | high | Unicode die-face replacement; numeric semantic value 6. |
| `IMOSAE-G013` | 5 | V01, V02, V04 | `d0a0f92be56a` | `DIE_FACE` | `⚀` | high | Unicode die-face replacement; numeric semantic value 1. |
| `IMOSAE-G014` | 3 | V01 | `d0cf2f44566c` | `DIE_FACE` | `⚁` | high | Unicode die-face replacement; numeric semantic value 2. |
| `IMOSAE-G015` | 3 | V02 | `7eb17d1e5eb0` | `COMPOSITE_TEXT_GLYPH` | `（仮）` | high | Occurs inside ruby with reading かっこかり; normalize surface to （仮） and retain ruby sidecar. |
| `IMOSAE-G016` | 4 | V02, V04 | `aceb09ccd9df` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G016⟧` | high | Exact visual retained by asset hash; no forced transcription. |
| `IMOSAE-G017` | 1 | V02 | `df94b4c61e6a` | `DECORATED_TEXT` | `こ` | high | Part of decorated sequence こんなふう; preserve decoration annotation. |
| `IMOSAE-G018` | 1 | V02 | `ea468a9e2792` | `DECORATED_TEXT` | `ん` | high | Part of decorated sequence こんなふう; preserve decoration annotation. |
| `IMOSAE-G019` | 1 | V02 | `5a8b1a127cef` | `DECORATED_TEXT` | `な` | high | Part of decorated sequence こんなふう; preserve decoration annotation. |
| `IMOSAE-G020` | 1 | V02 | `7b6a415346a7` | `DECORATED_TEXT` | `ふ` | high | Part of decorated sequence こんなふう; preserve decoration annotation. |
| `IMOSAE-G021` | 1 | V02 | `4774aaf2015f` | `DECORATED_TEXT` | `う` | high | Part of decorated sequence こんなふう; preserve decoration annotation. |
| `IMOSAE-G022` | 1 | V02 | `ce83316f915f` | `LOGOTYPE_TEXT` | `小` | high | Styled publisher/imprint logotype; part of 小学館ガガガ文庫. |
| `IMOSAE-G023` | 1 | V02 | `f3e04555b2c1` | `LOGOTYPE_TEXT` | `学` | high | Styled publisher/imprint logotype; part of 小学館ガガガ文庫. |
| `IMOSAE-G024` | 1 | V02 | `687ee3bbb417` | `LOGOTYPE_TEXT` | `館` | high | Styled publisher/imprint logotype; part of 小学館ガガガ文庫. |
| `IMOSAE-G025` | 3 | V02 | `ef59e317ac44` | `LOGOTYPE_TEXT` | `ガ` | high | Styled publisher/imprint logotype; part of 小学館ガガガ文庫. |
| `IMOSAE-G026` | 1 | V02 | `5e446e27022b` | `LOGOTYPE_TEXT` | `ガ` | high | Styled publisher/imprint logotype; part of 小学館ガガガ文庫. |
| `IMOSAE-G027` | 1 | V02 | `87674b42850b` | `LOGOTYPE_TEXT` | `庫` | high | Styled publisher/imprint logotype; part of 小学館ガガガ文庫. |
| `IMOSAE-G028` | 6 | V02, V04 | `baf03d43a738` | `DIE_FACE` | `⚂` | high | Unicode die-face replacement; numeric semantic value 3. |
| `IMOSAE-G029` | 1 | V02 | `1acdbef0311e` | `DIE_FACE` | `⚁` | high | Unicode die-face replacement; numeric semantic value 2. |
| `IMOSAE-G030` | 1 | V02 | `7b759b032d8c` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G030⟧` | high | Exact visual retained by asset hash; no forced transcription. |
| `IMOSAE-G031` | 1 | V02 | `0809e5d3eca7` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G031⟧` | high | Exact visual retained by asset hash; no forced transcription. |
| `IMOSAE-G032` | 2 | V03 | `9ac581311ca8` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G032⟧` | high | Filename identifies emoji/kaomoji role; exact visual retained. |
| `IMOSAE-G033` | 103 | V03, V05, V07, V08 | `61134452c5ea` | `STRUCTURAL_ORNAMENT` | `⟦ORNAMENT:IMOUTO_SEAL⟧` | high | Same semantic ornament as G002, different binary rendering. |
| `IMOSAE-G034` | 1 | V04 | `879b2e78c189` | `EXPRESSIVE_MARK` | `///` | high | Inline expressive mark; literal three slash normalization is faithful enough. |
| `IMOSAE-G035` | 2 | V04 | `f6bc38fa1c6e` | `DIE_FACE` | `⚁` | high | Unicode die-face replacement; numeric semantic value 2. |
| `IMOSAE-G036` | 3 | V04 | `f28c1d5f512a` | `PROLONGATION_MARK` | `―` | high | Used paired with G037 after successive syllables; normalized pair yields ――. |
| `IMOSAE-G037` | 3 | V04 | `80198da03fe8` | `PROLONGATION_MARK` | `―` | high | Used paired with G036 after successive syllables; normalized pair yields ――. |
| `IMOSAE-G038` | 2 | V05 | `01475e3d5211` | `PUNCTUATION` | `－` | high | Vertical-rendered separator in postal code/address; normalize to fullwidth hyphen-minus. |
| `IMOSAE-G039` | 5 | V05, V07, V08 | `f8a19f544f5a` | `NONSTANDARD_DAKUTEN` | `あ゙` | high | Expressive nonstandard voiced kana. |
| `IMOSAE-G040` | 1 | V05 | `f70e2f6488c5` | `NONSTANDARD_DAKUTEN` | `ん゙` | high | Expressive nonstandard voiced kana. |
| `IMOSAE-G041` | 2 | V05 | `4fc96899d37f` | `NONSTANDARD_DAKUTEN` | `な゙` | high | Expressive nonstandard voiced kana. |
| `IMOSAE-G042` | 1 | V05 | `38095a050d48` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G042⟧` | high | Exact visual retained by asset hash; no forced transcription. |
| `IMOSAE-G043` | 1 | V05 | `4fc2aeeefd0f` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G043⟧` | high | Exact visual retained by asset hash; no forced transcription. |
| `IMOSAE-G044` | 1 | V05 | `6e98ae914221` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G044⟧` | high | Exact visual retained by asset hash; no forced transcription. |
| `IMOSAE-G045` | 15 | V06, V09 | `92eb55238927` | `DIE_FACE` | `⚄` | high | Unicode die-face replacement; numeric semantic value 5. |
| `IMOSAE-G046` | 23 | V06, V09 | `fa6606d23cea` | `DIE_FACE` | `⚃` | high | Unicode die-face replacement; numeric semantic value 4. |
| `IMOSAE-G047` | 26 | V06, V09 | `619ed0a11806` | `DIE_FACE` | `⚅` | high | Unicode die-face replacement; numeric semantic value 6. |
| `IMOSAE-G048` | 24 | V06, V09 | `fc2c046a3bf8` | `DIE_FACE` | `⚂` | high | Unicode die-face replacement; numeric semantic value 3. |
| `IMOSAE-G049` | 16 | V06, V09 | `28e90a2a9f05` | `DIE_FACE` | `⚁` | high | Unicode die-face replacement; numeric semantic value 2. |
| `IMOSAE-G050` | 8 | V06, V09 | `4ab38cd26aa6` | `DIE_FACE` | `⚀` | high | Unicode die-face replacement; numeric semantic value 1. |
| `IMOSAE-G051` | 1 | V07 | `76a5cc027d1e` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G051⟧` | high | Exact visual retained by asset hash; no forced transcription. |
| `IMOSAE-G052` | 1 | V07 | `493aaa299c10` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G052⟧` | high | Exact visual retained by asset hash; no forced transcription. |
| `IMOSAE-G053` | 1 | V07 | `453071d9a8e7` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G053⟧` | high | Exact visual retained by asset hash; no forced transcription. |
| `IMOSAE-G054` | 6 | V09, V12, V14 | `dfca51e24e5b` | `NONSTANDARD_DAKUTEN` | `い゙` | high | Expressive nonstandard voiced kana. |
| `IMOSAE-G055` | 1 | V11 | `a544cf47e668` | `NONSTANDARD_DAKUTEN` | `え゙` | high | Expressive nonstandard voiced kana. |
| `IMOSAE-G056` | 1 | V12 | `c924a8bf2aa3` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G056⟧` | high | Exact visual retained by asset hash; no forced transcription. |
| `IMOSAE-G057` | 1 | V12 | `609fef8e15b9` | `NONSTANDARD_DAKUTEN` | `ま゙` | high | Expressive nonstandard voiced kana. |
| `IMOSAE-G058` | 1 | V12 | `dbc18fe40be5` | `NONSTANDARD_DAKUTEN` | `み゙` | high | Expressive nonstandard voiced kana. |
| `IMOSAE-G059` | 1 | V12 | `97f30c3ec74f` | `KAOMOJI_EMOJI` | `⟦KAOMOJI:IMOSAE-G059⟧` | high | Social-post expressive image; exact visual retained. |
| `IMOSAE-G060` | 5 | V13 | `eb7ae2da222e` | `TITLE_SYMBOL` | `⟦SYMBOL:LR_BIDIRECTIONAL_ARROW⟧` | medium-high | Inside title ruby Ｌ[image]Ｒ / エルアール. Search alias: Ｌ⇔Ｒ; preserve source token because exact horizontal glyph cannot be proved solely from rotated gaiji. |
| `IMOSAE-G061` | 1 | V13 | `361953599974` | `EXPRESSIVE_MARK` | `!!!` | high | Image is three exclamation marks; inline after 神. |
| `IMOSAE-G062` | 12 | V13 | `324b68fffa3e` | `STRUCTURAL_ORNAMENT` | `⟦ORNAMENT:SKULL_CROSSBONES⟧` | high | Standalone centered section/scene divider; not prose. |
| `IMOSAE-G063` | 1 | V14 | `48dc4dcf3bcf` | `TITLE_SYMBOL` | `⟦SYMBOL:LR_BIDIRECTIONAL_ARROW⟧` | medium-high | Same title symbol semantics as G060; binary rendering differs in V14. Search alias: Ｌ⇔Ｒ. |
| `IMOSAE-G064` | 1 | V14 | `5e45e8bbbaea` | `LEXICAL_GLYPH` | `晦` | high | Inside 大[gaiji]日 with ruby みそか; normalize to 大晦日. |
| `IMOSAE-G065` | 18 | V14 | `e716ce04fa87` | `STRUCTURAL_ORNAMENT` | `⟦ORNAMENT:BLUE_BIRD⟧` | high | Standalone centered section/scene divider in V14 "青い小鳥たち" material; not prose. |

## 5. Important compound/structural resolutions

### 5.1 Scene-break ornaments

`IMOSAE-G002` and `IMOSAE-G033` are distinct binary renderings of the same circled-`妹` scene-break seal. They normalize to `⟦ORNAMENT:IMOUTO_SEAL⟧`, not to the prose character `妹`. Together they account for 318 occurrences. `IMOSAE-G062` is a skull-and-crossbones divider and `IMOSAE-G065` is a stylized bird divider. These are structural punctuation at the publication-design level and must remain available to scene segmentation.

### 5.2 Decorated `こんなふう`

`G017`–`G021` form the visually decorated sequence `こんなふう` in V02. The normalized reading text restores the five kana while the annotation layer records the image-based decorative treatment. This is a useful demonstration of why image gaiji cannot simply be dropped: the prose sentence otherwise becomes grammatically incomplete.

### 5.3 `小学館ガガガ文庫` logotype

`G022`–`G027` encode the styled publisher/imprint name `小学館ガガガ文庫`. The textual characters are restored for search and quotation; the logotype treatment remains paratextual/form evidence.

### 5.4 TRPG dice

Fifteen binary gaiji IDs represent die faces across multiple ebook package generations. They are normalized semantically to `⚀` through `⚅`. The map also records the numeric value so later TRPG/game analysis can recover rolls without image inspection.

### 5.5 V04 shouted prolongation

`G036` and `G037` occur as paired line segments three times in the single utterance encoded as `だ[G036][G037]か[G036][G037]ら[G036][G037]！`. The reading view therefore yields `だ――か――ら――！`; both source-image IDs remain attached in the evidence record.

### 5.6 `Ｌ↔Ｒ` title symbol

`G060` and `G063` are binary variants of the bidirectional-arrow symbol embedded between fullwidth `Ｌ` and `Ｒ`, with ruby reading `エルアール`. The **semantic relation is clear**, but the raw image is rotated for vertical composition and does not by itself prove whether the intended horizontal Unicode glyph should be `↔`, `⇔`, or a typographically equivalent arrow. Therefore the canonical evidence stream uses `⟦SYMBOL:LR_BIDIRECTIONAL_ARROW⟧`. A convenience/search alias may render the work title as `Ｌ⇔Ｒデイズ`, but that alias must not be presented as an exact source transcription unless separately verified.

### 5.7 Lexical recovery examples

The map restores ordinary lexical content where the EPUB had to supply an image glyph, including:

- `訊` in `訊ねる`;
- `吐`;
- `晦` in `大晦日`;
- the composite `（仮）`, which occurs inside ruby whose reading identifies the parenthesized provisional-title expression.

## 6. Prototype normalization validation

A full V01–V14 prototype pass traversed **34,232 paragraph/heading nodes**, **29,083 ruby constructions**, and all **651** gaiji occurrences. Result: **651 mapped / 0 unmapped**.

Representative recovered strings include:

```text
疲れた声で土岐が訊ねる。
文章をこんなふうに装飾したり…
…小学館ガガガ文庫…
だ――か――ら――！
〒３７●－●●●●
Ｌ⟦SYMBOL:LR_BIDIRECTIONAL_ARROW⟧Ｒデイズ
```

The prototype is **validation evidence for the mapping specification**, not yet the frozen normalized corpus. The final reading layer still requires content-class typing, illustration anchoring, stable locators, and deliberate round-trip samples against source XHTML.

## 7. Paragraph/locator implications

This register fixes what the later locator generator must expose for any paragraph containing gaiji or ruby. At minimum a paragraph record must carry:

```text
volume
spine_index
chapter_label
xhtml_member
paragraph_ordinal
surface_text
normalized_text_fingerprint
ruby_annotations[]
gaiji_annotations[]
format_annotations[]
illustration_anchor(s)
content_class
```

The architecture-defined locator grammar remains:

```text
V06|chapter:<label>|spine:NN|xhtml:<member>|p:NNNN
```

The locator generator should add a short normalized-text fingerprint, but the fingerprint must not replace the human-readable route back to the XHTML member.

## 8. Machine-readable companions

The following derivative files accompany this register:

- `machine_readable/gaiji_map.json` — canonical 65-entry hash-to-resolution map, including full hashes and source metadata;
- `machine_readable/gaiji_occurrences.jsonl` — one record for each of the 651 source occurrences;
- `machine_readable/normalization_validation.json` — per-volume prototype counts and all-gaiji mapping validation.

These are derived from `IMOSAE-JP-LN-RAW-1.0`; they are not replacements for the EPUBs.

## 9. Remaining Phase-0 work

Completion of this register changes Phase 0 from **gaiji-resolution open** to **gaiji-resolution complete**. The following gates remain:

1. finish full spine-member content classification;
2. create `IMOSAE_ILLUSTRATION_AND_PARATEXT_INVENTORY.md`;
3. generate the complete normalized paragraph layer using this mapping specification;
4. generate `machine_readable/locator_index.jsonl`;
5. anchor illustrations/paratext to prose locations;
6. perform deliberate beginning/middle/end, ruby-heavy, gaiji-heavy, typography-heavy, dialogue, and chapter-boundary round-trip checks in every volume;
7. issue the Phase-0 closure audit and freeze `IMOSAE-JP-LN-NORM-1.0` only if those checks pass.

**Canonical V01 deep reading remains gated.**

## 10. Change control

Use the project transition vocabulary for future modifications:

`PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN`

A replacement string may be changed only by a documented `REVISE`. A new ebook generation that changes the binary gaiji assets requires a new mapping comparison; identical-looking glyphs must not be assumed byte-identical.

## 11. Next architecture-defined artifact

Proceed to **`IMOSAE_ILLUSTRATION_AND_PARATEXT_INVENTORY.md`**, while using this register as the governing gaiji/normalization specification for subsequent normalized paragraph and locator generation.
