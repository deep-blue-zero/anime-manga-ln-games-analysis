---
series: IMOSAE
artifact_type: illustration_paratext_inventory
scope: V01-V14_main_series
generation: V1
status: canonical
source_boundary: "IMOSAE-JP-LN-RAW-1.0 Japanese numbered light-novel EPUBs"
supersedes: null
superseded_by: null
do_not_use_as_current_authority: false
version: "1.0"
date: "2026-08-18"
visual_index_id: "IMOSAE-VISUAL-INDEX-1.0"
normalized_release_status: "not_yet_frozen"
---

# IMOSAE Illustration and Paratext Inventory
## 『妹さえいればいい。』 / *A Sister's All You Need*

## 0. Status and purpose

This artifact closes the **illustration/paratext census and source-anchoring portion** of Phase 0 for the immutable raw source set `IMOSAE-JP-LN-RAW-1.0`. It does not yet close Phase 0 as a whole: complete normalized paragraph generation, full spine-item classification, stable paragraph locators, and round-trip extraction validation remain open.

The inventory is deliberately source-form conservative. It records where visual material sits in the EPUB spine and what publication role it performs before later literary interpretation is allowed to make stronger claims about staging, sexuality, comedy, intimacy, characterization, or thematic emphasis.

## 1. Corpus-level findings

- **666 raster image assets** are present across V01-V14.
- **562 non-gaiji visual/paratext assets** receive stable `Vxx|ILL:nnn|member:...` locators in `IMOSAE-VISUAL-INDEX-1.0`.
- **104 package image assets** are gaiji/inline-symbol resources and remain governed by `IMOSAE-GAIJI-MAP-1.0`; these asset files account for the previously frozen 651 gaiji occurrences.
- Two additional small images are afterword QR codes rather than gaiji and are classified separately as publication paratext.
- Every non-gaiji visual asset has a source member, dimensions, spine relation, color/monochrome estimate, nearest named TOC section when available, and preceding/following text-member anchors when applicable.
- Narrative illustrations are **Tier 1B primary paratextual evidence**: they establish licensed visual depiction, emphasis, placement, and editorial framing, but they do not automatically override contradictory prose.
- Publisher advertisements are retained for provenance but carry **publication-context-only** authority.

## 2. Stable visual locator and authority rules

Canonical visual locator:

```text
V09|ILL:012|member:OEBPS/Images/...
```

Rules:

1. `ILL` numbers are stable within `IMOSAE-JP-LN-RAW-1.0` and are assigned in first-spine/source order. They are not page numbers.
2. Gaiji do not receive `ILL` numbers; they retain their `IMOSAE-G###` identities.
3. A later replacement EPUB set must create a new source generation and a crosswalk rather than silently renumbering this index.
4. The image member path and SHA-256 remain the provenance key even when a visual is also tagged by narrative section.
5. Placement relative to surrounding prose is part of the evidence. Gallery extraction must never sever the prose anchors.
6. Character identity tags are intentionally conservative in Phase 0. When identity is not independently secure from the source context, the machine index leaves the tag empty for refinement during prospective volume reading rather than guessing from appearance alone.

## 3. Visual-role taxonomy

- **`COVER`** — OPF-designated or package-designated cover image.
- **`FRONT_TITLE_PAGE`** — Interior title/frontispiece page.
- **`FRONT_COLOR_ILLUSTRATION`** — Front color plate/spread. Placement is pre-narrative but the image may depict or editorially frame later scenes.
- **`FRONT_SERIES_MAP`** — Front-matter cast/relationship/map-style orientation graphic.
- **`FRONT_CHARACTER_PROFILE`** — Front-matter monochrome title/profile/cast page.
- **`NARRATIVE_ILLUSTRATION`** — Monochrome or color illustration placed within a narrative section and anchored to adjacent prose.
- **`NARRATIVE_QA_PARATEXT`** — Recurring in-volume “Q&Aコーナー”/question-answer page; internal paratext tied to the surrounding section rather than ordinary prose narration.
- **`NARRATIVE_CHARACTER_PROFILE`** — Character/profile or compatibility sheet embedded inside the volume; factual/parodic paratext whose claims require contextual reading.
- **`NARRATIVE_DOCUMENT`** — Document, manuscript, recipe, article, application/industry sheet, or other text-bearing graphic embedded in the narrative flow.
- **`NARRATIVE_GAME_OR_DIAGRAM`** — Game/TRPG board, character sheet, rules aid, or diagram functioning inside the narrative/game layer.
- **`IN_TEXT_PUBLISHING_ARTIFACT`** — Graphic publishing/obi mock-up explicitly embedded in the V11 “オビを考えよう” material; not a real publisher advertisement.
- **`WORK_WITHIN_WORK_GRAPHIC`** — Diegetic work-within-work visual (e.g. fictional movie/poster) embedded in the narrative.
- **`NARRATIVE_FORMAL_DEVICE`** — Graphic/formal page whose visual construction itself contributes to scene rhythm or closure.
- **`AUTHOR_AFTERWORD_DOCUMENT`** — Creator-process/project-proposal document placed inside the afterword/back-matter sequence.
- **`AUTHOR_AFTERWORD_ART`** — Author-afterword/signature illustration or creator portrait page.
- **`AFTERWORD_EXTERNAL_LINK_QR`** — QR-code image embedded in an author-afterword page; paratextual external-link artifact.
- **`RETAILER_EBOOK_BONUS_COVER`** — Gagaga 10th-anniversary electronic bonus cover-art gallery; licensed paratext, not narrative event evidence.
- **`PROMOTIONAL_AD`** — Publisher/back-of-book promotional material unrelated to the volume’s narrative continuity.
- **`GAIJI_INLINE_IMAGE`** — Inline gaiji/symbol image; governed by IMOSAE_GAIJI_AND_TEXT_NORMALIZATION_REGISTER.md rather than the illustration ledger.

## 4. Corpus role counts

| Role | Assets |
|---|---:|
| `NARRATIVE_ILLUSTRATION` | 139 |
| `PROMOTIONAL_AD` | 107 |
| `GAIJI_INLINE_IMAGE` | 104 |
| `NARRATIVE_QA_PARATEXT` | 70 |
| `FRONT_COLOR_ILLUSTRATION` | 40 |
| `NARRATIVE_DOCUMENT` | 39 |
| `NARRATIVE_GAME_OR_DIAGRAM` | 29 |
| `NARRATIVE_CHARACTER_PROFILE` | 25 |
| `RETAILER_EBOOK_BONUS_COVER` | 24 |
| `FRONT_TITLE_PAGE` | 14 |
| `FRONT_SERIES_MAP` | 14 |
| `FRONT_CHARACTER_PROFILE` | 14 |
| `AUTHOR_AFTERWORD_ART` | 14 |
| `COVER` | 14 |
| `IN_TEXT_PUBLISHING_ARTIFACT` | 9 |
| `AUTHOR_AFTERWORD_DOCUMENT` | 5 |
| `AFTERWORD_EXTERNAL_LINK_QR` | 2 |
| `NARRATIVE_FORMAL_DEVICE` | 2 |
| `WORK_WITHIN_WORK_GRAPHIC` | 1 |

## 5. Volume-level summary

| Vol. | Non-gaiji visuals | Narrative-related | Q&A/profile/doc/game | Afterword/process | Promo | 10th-anniv bonus covers |
|---:|---:|---:|---:|---:|---:|---:|
| V01 | 37 | 29 | 19 | 1 | 0 | 0 |
| V02 | 30 | 21 | 11 | 2 | 0 | 0 |
| V03 | 29 | 21 | 11 | 1 | 0 | 0 |
| V04 | 31 | 23 | 13 | 1 | 0 | 0 |
| V05 | 30 | 22 | 12 | 1 | 0 | 0 |
| V06 | 36 | 28 | 17 | 1 | 0 | 0 |
| V07 | 39 | 20 | 10 | 1 | 5 | 7 |
| V08 | 60 | 20 | 10 | 2 | 23 | 8 |
| V09 | 59 | 29 | 20 | 1 | 13 | 9 |
| V10 | 39 | 18 | 8 | 1 | 13 | 0 |
| V11 | 54 | 30 | 20 | 1 | 16 | 0 |
| V12 | 39 | 18 | 8 | 1 | 13 | 0 |
| V13 | 44 | 19 | 9 | 6 | 13 | 0 |
| V14 | 35 | 16 | 7 | 1 | 11 | 0 |

## 6. High-value paratext findings

### 6.1 Front matter is structurally recurrent, not disposable decoration

Across the run, the EPUBs repeatedly stage an interior title/frontispiece, color plates, a cast/relationship/map-style orientation page, and a monochrome title/profile page before the main narrative. These materials should be retained as a **front-matter visual layer** because they establish which characters, pairings, occupations, jokes, and visual motifs the edition chooses to foreground before prose reading begins.

### 6.2 The recurring Q&A pages form a genuine internal paratext system

V03-V10 especially use branded `Q&Aコーナー` pages between prose/illustration units. These are not ordinary narrative paragraphs, but they are also not external advertising. They are licensed in-volume character/world paratext and can provide characterization, joke framing, relationship commentary, and authorial/editorial emphasis. Claims derived from them should be marked as paratextual facts rather than silently merged into narrator-level fact.

### 6.3 Industry documents and in-world graphics are analytically central

The corpus repeatedly turns manuscripts, application/award material, recipes, interview sheets, character profiles, publishing documents, and other page-level graphics into evidence. This is unusually important for a series about writers, editors, illustrators, adaptation, and professional creative labor: the publication object often visually imitates the documents its characters themselves produce.

### 6.4 Games and TRPG material must stay graphically recoverable

V01-V06 and V09 contain game boards, TRPG character sheets, relationship/position diagrams, and related visual aids. These pages are not decorative inserts. They preserve rules/state information and social positioning that can be difficult to reconstruct from flattened prose alone. V11 additionally contains visual components for `妹が多すぎる。` inside the main-text sequence.

### 6.5 V11 contains publishing artifacts that must not be mistaken for real ads

The visual block inside `オビを考えよう` consists of mock publishing/obi materials used by the narrative itself. Their commercial graphic language resembles back-of-book advertising, but spine placement and section context establish them as **in-text publishing artifacts**. They remain narrative evidence.

### 6.6 V13 preserves creator-process documents in the afterword layer

Five project-proposal sheets (`企画書`) are positioned in the V13 afterword/back-matter sequence. They are documentary evidence about creative ideation and discarded/alternate concepts, not events in the novel continuity. They should become major evidence for the eventual creative-process/media-reflexivity synthesis.

### 6.7 Gagaga 10th-anniversary cover galleries are a distinct bonus-paratext class

V07-V09 append electronic bonus cover-art galleries after the core publication matter. These are useful for cross-volume visual history and branding, but they must not be treated as if their poses or configurations occurred in the story.

### 6.8 Back-of-book promotional payload grows substantially in later ebook packages

From V07 onward—and especially V08-V14—the EPUBs contain substantial publisher/catalog advertising. Those images are retained in the source index for provenance but excluded from narrative evidence by default. This separation is essential for preventing unrelated Gagaga titles or marketing copy from contaminating literary retrieval.

### 6.9 V14 uses page-level closure as formal evidence

The V14 graphic page carrying `かかってこい　完` is classified as a narrative formal device rather than a detachable illustration. The page’s typography, emptiness/graphic balance, and placement at the end of a sequence are part of how closure is staged and should be revisited during the final-volume deep reading.

## 7. Per-volume inventory

The tables below are the human-readable projection of `machine_readable/illustration_paratext_index.jsonl`. Every non-gaiji asset is listed once. `Anchor section` is the nearest preceding named TOC section at the asset’s spine position; blank values normally indicate front matter or package-level material.

### V01

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V01-ILL-001` | `COVER` | `OEBPS/Images/embed0050_HD.jpg` | 1121x1600 | color | 0 |  |
| `V01-ILL-002` | `FRONT_TITLE_PAGE` | `OEBPS/Images/embed0000_HD.jpg` | 1121x1600 | color | 2 |  |
| `V01-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0001_HD.jpg` | 1600x1144 | color | 3 |  |
| `V01-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0002_HD.jpg` | 1600x1145 | color | 4 |  |
| `V01-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0003_HD.jpg` | 1600x1148 | color | 5 |  |
| `V01-ILL-006` | `FRONT_SERIES_MAP` | `OEBPS/Images/embed0004_HD.jpg` | 1123x1600 | color | 6 |  |
| `V01-ILL-007` | `FRONT_CHARACTER_PROFILE` | `OEBPS/Images/embed0005_HD.jpg` | 1120x1600 | monochrome | 8 |  |
| `V01-ILL-008` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0008_HD.jpg` | 1120x1600 | monochrome | 10 | 小説家は妹キチ●イ |
| `V01-ILL-009` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0009_HD.jpg` | 1120x1600 | monochrome | 12 | 小説家は妹キチ●イ |
| `V01-ILL-010` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0011_HD.jpg` | 1120x1600 | monochrome | 14 | 天才で変態 |
| `V01-ILL-011` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0012_HD.jpg` | 1120x1600 | monochrome | 16 | 天才で変態 |
| `V01-ILL-012` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0013_HD.jpg` | 1119x1600 | monochrome | 18 | 天才で変態 |
| `V01-ILL-013` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0014_HD.jpg` | 1120x1600 | monochrome | 20 | 女子大生にもいろいろいる |
| `V01-ILL-014` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0015_HD.jpg` | 1120x1600 | monochrome | 22 | 女子大生にもいろいろいる |
| `V01-ILL-015` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0016_HD.jpg` | 1120x1600 | monochrome | 24 | 今回は男友達もいる |
| `V01-ILL-016` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0017_HD.jpg` | 1120x1600 | monochrome | 26 | 今回は男友達もいる |
| `V01-ILL-017` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0019_HD.jpg` | 1120x1600 | monochrome | 28 | メインテーマ |
| `V01-ILL-018` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0020_HD.jpg` | 1120x1600 | monochrome | 30 | ウミガメのスープ |
| `V01-ILL-019` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0023_HD.jpg` | 1120x1600 | monochrome | 32 | 赤裸々 |
| `V01-ILL-020` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0024_HD.jpg` | 1120x1600 | monochrome | 34 | 神 |
| `V01-ILL-021` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0025_HD.jpg` | 1120x1600 | monochrome | 36 | 神 |
| `V01-ILL-022` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0028_HD.jpg` | 1120x1600 | monochrome | 39 | バレンタイン |
| `V01-ILL-023` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0029_HD.jpg` | 1120x1600 | monochrome | 43 | くたばれ確定申告 |
| `V01-ILL-024` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0030_HD.jpg` | 1120x1600 | monochrome | 45 | くたばれ確定申告 |
| `V01-ILL-025` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0031_HD.jpg` | 1120x1600 | monochrome | 47 | クロニカクロニクル① |
| `V01-ILL-026` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0032_HD.jpg` | 1120x1600 | monochrome | 48 | クロニカクロニクル① |
| `V01-ILL-027` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0033_HD.jpg` | 1120x1600 | monochrome | 49 | クロニカクロニクル① |
| `V01-ILL-028` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0034_HD.jpg` | 1120x1600 | monochrome | 50 | クロニカクロニクル① |
| `V01-ILL-029` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0035_HD.jpg` | 1120x1600 | monochrome | 52 | クロニカクロニクル① |
| `V01-ILL-030` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0042_HD.jpg` | 1120x1600 | monochrome | 54 | クロニカクロニクル① |
| `V01-ILL-031` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0043_HD.jpg` | 1120x1600 | monochrome | 56 | クロニカクロニクル① |
| `V01-ILL-032` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0044_HD.jpg` | 1600x1143 | monochrome | 58 | クロニカクロニクル① |
| `V01-ILL-033` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0045_HD.jpg` | 1120x1600 | monochrome | 60 | クロニカクロニクル① |
| `V01-ILL-034` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0046_HD.jpg` | 1600x1143 | monochrome | 61 | クロニカクロニクル① |
| `V01-ILL-035` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0047_HD.jpg` | 1120x1600 | monochrome | 62 | クロニカクロニクル① |
| `V01-ILL-036` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0048_HD.jpg` | 1120x1600 | monochrome | 63 | クロニカクロニクル① |
| `V01-ILL-037` | `AUTHOR_AFTERWORD_ART` | `OEBPS/Images/embed0049_HD.jpg` | 1120x1600 | monochrome | 65 | クロニカクロニクル① |

### V02

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V02-ILL-001` | `COVER` | `OEBPS/Images/embed0052_HD.jpg` | 1121x1600 | color | 0 |  |
| `V02-ILL-002` | `FRONT_TITLE_PAGE` | `OEBPS/Images/embed0000_HD.jpg` | 1121x1600 | color | 2 |  |
| `V02-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0001_HD.jpg` | 1600x1143 | color | 3 |  |
| `V02-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0002_HD.jpg` | 1600x1142 | color | 4 |  |
| `V02-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0003_HD.jpg` | 1600x1144 | color | 5 |  |
| `V02-ILL-006` | `FRONT_SERIES_MAP` | `OEBPS/Images/embed0004_HD.jpg` | 1120x1600 | color | 6 |  |
| `V02-ILL-007` | `FRONT_CHARACTER_PROFILE` | `OEBPS/Images/embed0005_HD.jpg` | 1120x1600 | monochrome | 8 |  |
| `V02-ILL-008` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0007_HD.jpg` | 1120x1600 | monochrome | 10 | 小説家は妹キ●ガイⅡ |
| `V02-ILL-009` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0008_HD.jpg` | 1120x1600 | monochrome | 12 | キャット＆チョコレート　学園編 |
| `V02-ILL-010` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0010_HD.jpg` | 1120x1600 | monochrome | 15 | ＳＩＲＩ　ＡＳＳ |
| `V02-ILL-011` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0011_HD.jpg` | 1120x1600 | monochrome | 17 | ＳＩＲＩ　ＡＳＳ |
| `V02-ILL-012` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0012_HD.jpg` | 1120x1600 | monochrome | 19 | ドＳふたたび |
| `V02-ILL-013` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0015_HD.jpg` | 1120x1600 | monochrome | 21 | すべては小説のために |
| `V02-ILL-014` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0021_HD.jpg` | 1120x1600 | monochrome | 23 | 嫁（？）　ＶＳ　弟（？） |
| `V02-ILL-015` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0022_HD.jpg` | 1120x1600 | monochrome | 25 | 嫁（？）　ＶＳ　弟（？） |
| `V02-ILL-016` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0029_HD.jpg` | 1120x1600 | monochrome | 27 | 可児那由多の仕事風景 |
| `V02-ILL-017` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0030_HD.jpg` | 1120x1600 | monochrome | 30 | 言い訳メール |
| `V02-ILL-018` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0031_HD.jpg` | 1120x1600 | monochrome | 32 | 言い訳メール |
| `V02-ILL-019` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0032_HD.jpg` | 1120x1600 | monochrome | 34 | よくある感じのエンディング |
| `V02-ILL-020` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0033_HD.jpg` | 1120x1600 | monochrome | 36 | よくある感じのエンディング |
| `V02-ILL-021` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0034_HD.jpg` | 1120x1600 | monochrome | 38 | よくある感じのエンディング |
| `V02-ILL-022` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0037_HD.jpg` | 1120x1600 | monochrome | 40 | クロニカクロニクル② |
| `V02-ILL-023` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0042_HD.jpg` | 1120x1600 | monochrome | 42 | クロニカクロニクル② |
| `V02-ILL-024` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0043_HD.jpg` | 1120x1600 | monochrome | 44 | クロニカクロニクル② |
| `V02-ILL-025` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0044_HD.jpg` | 1600x1143 | monochrome | 46 | クロニカクロニクル② |
| `V02-ILL-026` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0045_HD.jpg` | 1600x1143 | monochrome | 47 | クロニカクロニクル② |
| `V02-ILL-027` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0046_HD.jpg` | 1120x1600 | monochrome | 50 | アニメ化は色々あるんですよ変な話 |
| `V02-ILL-028` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0049_HD.jpg` | 1120x1600 | monochrome | 52 | アニメ化は色々あるんですよ変な話 |
| `V02-ILL-029` | `AFTERWORD_EXTERNAL_LINK_QR` | `OEBPS/Images/embed0050.jpg` | 120x120 | monochrome | 55 | あとがき |
| `V02-ILL-030` | `AUTHOR_AFTERWORD_ART` | `OEBPS/Images/embed0051_HD.jpg` | 1120x1600 | monochrome | 56 | あとがき |

### V03

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V03-ILL-001` | `COVER` | `OEBPS/Images/i-000a.jpg` | 847x1200 | color | 0 | Start |
| `V03-ILL-002` | `FRONT_TITLE_PAGE` | `OEBPS/Images/i-0001_01.jpg` | 1120x1600 | color | 2 | Start |
| `V03-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/i-0002-0003_01.jpg` | 1600x1143 | color | 3 | Start |
| `V03-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/i-0004-0005_01.jpg` | 1600x1144 | color | 4 | Start |
| `V03-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/i-0006-0007_01.jpg` | 1600x1144 | color | 5 | Start |
| `V03-ILL-006` | `FRONT_SERIES_MAP` | `OEBPS/Images/i-0008_01.jpg` | 1120x1600 | color | 6 | Start |
| `V03-ILL-007` | `FRONT_CHARACTER_PROFILE` | `OEBPS/Images/i-0009_01.jpg` | 1120x1600 | monochrome | 8 | Start |
| `V03-ILL-008` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0023_01.jpg` | 1120x1600 | monochrome | 10 | ラブコメ（仮） |
| `V03-ILL-009` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0028_01.jpg` | 1120x1600 | color | 12 | ラブコメ（仮） |
| `V03-ILL-010` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0047_01.jpg` | 1120x1600 | monochrome | 14 | プレゼントを考えよう |
| `V03-ILL-011` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0049_01.jpg` | 1120x1600 | color | 16 | プレゼントを考えよう |
| `V03-ILL-012` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/i-0062_01.jpg` | 1120x1600 | monochrome | 18 | あらすじを考えよう |
| `V03-ILL-013` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0069_01.jpg` | 1120x1600 | color | 20 | 探求者 |
| `V03-ILL-014` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0073_01.jpg` | 1120x1600 | monochrome | 22 | ２１歳 |
| `V03-ILL-015` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0093_01.jpg` | 1120x1600 | color | 24 | ２１歳 |
| `V03-ILL-016` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0109_01.jpg` | 1120x1600 | monochrome | 26 | 遊園地 |
| `V03-ILL-017` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0111_01.jpg` | 1120x1600 | color | 28 | 遊園地 |
| `V03-ILL-018` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0121_01.jpg` | 1120x1600 | color | 30 | 動物園 |
| `V03-ILL-019` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0129_01.jpg` | 1120x1600 | monochrome | 32 | アルバイト |
| `V03-ILL-020` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0131_01.jpg` | 1120x1600 | color | 34 | アルバイト |
| `V03-ILL-021` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0140_01.jpg` | 1120x1600 | color | 36 | クロニカクロニクル設定資料 |
| `V03-ILL-022` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0145_01.jpg` | 1120x1600 | monochrome | 38 | 水族館 |
| `V03-ILL-023` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0153_01.jpg` | 1120x1600 | monochrome | 40 | 水族館 |
| `V03-ILL-024` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0156_01.jpg` | 1120x1600 | color | 42 | 水族館 |
| `V03-ILL-025` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0173_01.jpg` | 1120x1600 | monochrome | 44 | 主人公になりたい |
| `V03-ILL-026` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0187_01.jpg` | 1120x1600 | monochrome | 46 | 主人公になりたい |
| `V03-ILL-027` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0192_01.jpg` | 1120x1600 | color | 48 | 主人公になりたい |
| `V03-ILL-028` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0213_01.jpg` | 1120x1600 | monochrome | 50 | 番外編　羽島伊月の誕生 |
| `V03-ILL-029` | `AUTHOR_AFTERWORD_ART` | `OEBPS/Images/i-0229_01.jpg` | 1120x1600 | monochrome | 53 | あとがき |

### V04

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V04-ILL-001` | `COVER` | `cover.jpeg` | 887x1266 | color | 0 |  |
| `V04-ILL-002` | `FRONT_TITLE_PAGE` | `images/00001.jpeg` | 971x1388 | color | 2 |  |
| `V04-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `images/00002.jpeg` | 1030x729 | color | 3 |  |
| `V04-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `images/00003.jpeg` | 1030x726 | color | 4 |  |
| `V04-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `images/00004.jpeg` | 1030x727 | color | 5 |  |
| `V04-ILL-006` | `FRONT_SERIES_MAP` | `images/00005.jpeg` | 895x1279 | color | 6 |  |
| `V04-ILL-007` | `FRONT_CHARACTER_PROFILE` | `images/00006.jpeg` | 971x1388 | monochrome | 8 |  |
| `V04-ILL-008` | `NARRATIVE_DOCUMENT` | `images/00007.jpeg` | 971x1388 | monochrome | 10 | 小説家は妹キ●ガイⅢ |
| `V04-ILL-009` | `NARRATIVE_ILLUSTRATION` | `images/00011.jpeg` | 963x1376 | monochrome | 12 | ６月６日 |
| `V04-ILL-010` | `NARRATIVE_ILLUSTRATION` | `images/00012.jpeg` | 966x1381 | monochrome | 14 | ６月６日 |
| `V04-ILL-011` | `NARRATIVE_QA_PARATEXT` | `images/00013.jpeg` | 905x1294 | monochrome | 16 | ６月６日 |
| `V04-ILL-012` | `NARRATIVE_QA_PARATEXT` | `images/00014.jpeg` | 938x1340 | monochrome | 18 | コミカライズ |
| `V04-ILL-013` | `NARRATIVE_ILLUSTRATION` | `images/00015.jpeg` | 971x1388 | monochrome | 20 | 顔合わせ |
| `V04-ILL-014` | `NARRATIVE_QA_PARATEXT` | `images/00016.jpeg` | 912x1303 | monochrome | 22 | 顔合わせ |
| `V04-ILL-015` | `NARRATIVE_ILLUSTRATION` | `images/00017.jpeg` | 809x1156 | monochrome | 24 | マンガ家ＶＳイラストレーター |
| `V04-ILL-016` | `NARRATIVE_CHARACTER_PROFILE` | `images/00018.jpeg` | 958x1369 | monochrome | 26 | マンガ家ＶＳイラストレーター |
| `V04-ILL-017` | `NARRATIVE_ILLUSTRATION` | `images/00019.jpeg` | 971x1388 | monochrome | 28 | ニアミス |
| `V04-ILL-018` | `NARRATIVE_QA_PARATEXT` | `images/00020.jpeg` | 971x1388 | monochrome | 29 | ニアミス |
| `V04-ILL-019` | `NARRATIVE_ILLUSTRATION` | `images/00021.jpeg` | 945x1350 | monochrome | 31 | 逆襲の全裸 |
| `V04-ILL-020` | `NARRATIVE_DOCUMENT` | `images/00022.jpeg` | 945x1351 | monochrome | 33 | 逆襲の全裸 |
| `V04-ILL-021` | `NARRATIVE_ILLUSTRATION` | `images/00023.jpeg` | 971x1388 | monochrome | 36 | 税理士の気晴らし |
| `V04-ILL-022` | `NARRATIVE_GAME_OR_DIAGRAM` | `images/00024.jpeg` | 852x1217 | monochrome | 39 | クロニカクロニクル③ |
| `V04-ILL-023` | `NARRATIVE_GAME_OR_DIAGRAM` | `images/00032.jpeg` | 971x1388 | monochrome | 41 | クロニカクロニクル③ |
| `V04-ILL-024` | `NARRATIVE_ILLUSTRATION` | `images/00034.jpeg` | 800x1143 | monochrome | 43 | クロニカクロニクル③ |
| `V04-ILL-025` | `NARRATIVE_GAME_OR_DIAGRAM` | `images/00035.jpeg` | 820x1172 | monochrome | 45 | クロニカクロニクル③ |
| `V04-ILL-026` | `NARRATIVE_GAME_OR_DIAGRAM` | `images/00036.jpeg` | 764x1092 | monochrome | 46 | クロニカクロニクル③ |
| `V04-ILL-027` | `NARRATIVE_GAME_OR_DIAGRAM` | `images/00037.jpeg` | 778x1111 | monochrome | 47 | クロニカクロニクル③ |
| `V04-ILL-028` | `NARRATIVE_GAME_OR_DIAGRAM` | `images/00038.jpeg` | 780x1115 | monochrome | 48 | クロニカクロニクル③ |
| `V04-ILL-029` | `NARRATIVE_ILLUSTRATION` | `images/00039.jpeg` | 950x1357 | monochrome | 51 | 予兆 |
| `V04-ILL-030` | `NARRATIVE_ILLUSTRATION` | `images/00040.jpeg` | 971x1388 | monochrome | 54 | ぼーなすとらっく ラノベ作家の人生 |
| `V04-ILL-031` | `AUTHOR_AFTERWORD_ART` | `images/00042.jpeg` | 971x1388 | monochrome | 59 | あとがき |

### V05

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V05-ILL-001` | `COVER` | `OEBPS/Images/i-000a.jpg` | 1119x1600 | color | 0 | Start |
| `V05-ILL-002` | `FRONT_TITLE_PAGE` | `OEBPS/Images/i-0001_01.jpg` | 1120x1600 | color | 2 | Start |
| `V05-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/i-0002-0003_01.jpg` | 1600x1152 | color | 3 | Start |
| `V05-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/i-0004-0005_01.jpg` | 1600x1147 | color | 4 | Start |
| `V05-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/i-0006-0007_01.jpg` | 1600x1157 | color | 5 | Start |
| `V05-ILL-006` | `FRONT_SERIES_MAP` | `OEBPS/Images/i-0008_01.jpg` | 1119x1600 | color | 6 | Start |
| `V05-ILL-007` | `FRONT_CHARACTER_PROFILE` | `OEBPS/Images/i-0009_01.jpg` | 1120x1600 | monochrome | 8 | Start |
| `V05-ILL-008` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/i-0019_01.jpg` | 1120x1600 | monochrome | 10 | 小説家は妹キ●ガイⅣ |
| `V05-ILL-009` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0025_01.jpg` | 1120x1600 | monochrome | 12 | 面接 |
| `V05-ILL-010` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0033_01.jpg` | 1120x1600 | color | 14 | 面接 |
| `V05-ILL-011` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0042_01.jpg` | 1120x1600 | color | 16 | 羽島千尋の昼休み |
| `V05-ILL-012` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0047_01.jpg` | 1120x1600 | monochrome | 18 | 編集部のバイトはじめました |
| `V05-ILL-013` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0061_01.jpg` | 1120x1600 | monochrome | 20 | 編集部のバイトはじめました |
| `V05-ILL-014` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/i-0074_01.jpg` | 1120x1600 | monochrome | 22 | 編集部のバイトはじめました |
| `V05-ILL-015` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0085_01.jpg` | 1120x1600 | monochrome | 24 | 水着回１ |
| `V05-ILL-016` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0087_01.jpg` | 1120x1600 | color | 26 | 水着回１ |
| `V05-ILL-017` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0096_01.jpg` | 1120x1600 | monochrome | 29 | 水着回３ |
| `V05-ILL-018` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0113_01.jpg` | 1120x1600 | monochrome | 31 | 顔合わせ（アニメ編） |
| `V05-ILL-019` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0123_01.jpg` | 1120x1600 | color | 33 | 顔合わせ（アニメ編） |
| `V05-ILL-020` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0143_01.jpg` | 1120x1600 | monochrome | 36 | 実際にこういうミスが何度もあったので各編集部はもっと気をつけてくださいマジで |
| `V05-ILL-021` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/i-0146_01.jpg` | 1120x1600 | monochrome | 38 | 実際にこういうミスが何度もあったので各編集部はもっと気をつけてくださいマジで |
| `V05-ILL-022` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0161_01.jpg` | 1120x1600 | monochrome | 41 | 新人賞選考会 |
| `V05-ILL-023` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/i-0168_01.jpg` | 1120x1600 | monochrome | 43 | 新人賞選考会 |
| `V05-ILL-024` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/i-0169_01.jpg` | 1120x1600 | monochrome | 44 | 新人賞選考会 |
| `V05-ILL-025` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/i-0170_01.jpg` | 1120x1600 | monochrome | 45 | 新人賞選考会 |
| `V05-ILL-026` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/i-0186_01.jpg` | 1120x1600 | color | 47 | 新人賞選考会 |
| `V05-ILL-027` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0209_01.jpg` | 1120x1600 | monochrome | 49 | 凡人の星 |
| `V05-ILL-028` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/i-0210_01.jpg` | 1120x1600 | monochrome | 50 | 凡人の星 |
| `V05-ILL-029` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0221_01.jpg` | 1120x1600 | monochrome | 52 | 白川京 |
| `V05-ILL-030` | `AUTHOR_AFTERWORD_ART` | `OEBPS/Images/i-0229_01.jpg` | 1120x1600 | monochrome | 56 | あとがき |

### V06

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V06-ILL-001` | `COVER` | `OEBPS/Images/embed0043_HD.jpg` | 1120x1600 | color | 0 |  |
| `V06-ILL-002` | `FRONT_TITLE_PAGE` | `OEBPS/Images/embed0000_HD.jpg` | 1121x1600 | color | 2 |  |
| `V06-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0001_HD.jpg` | 1600x1143 | color | 3 |  |
| `V06-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0002_HD.jpg` | 1600x1143 | color | 4 |  |
| `V06-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0003_HD.jpg` | 1600x1144 | color | 5 |  |
| `V06-ILL-006` | `FRONT_SERIES_MAP` | `OEBPS/Images/embed0004_HD.jpg` | 1120x1600 | color | 6 |  |
| `V06-ILL-007` | `FRONT_CHARACTER_PROFILE` | `OEBPS/Images/embed0005_HD.jpg` | 1120x1600 | monochrome | 8 |  |
| `V06-ILL-008` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0008_HD.jpg` | 1120x1600 | monochrome | 10 | 人間力 |
| `V06-ILL-009` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0009_HD.jpg` | 1120x1600 | color | 12 | 人間力 |
| `V06-ILL-010` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0010_HD.jpg` | 1120x1600 | monochrome | 14 | 主人公ズ |
| `V06-ILL-011` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0011_HD.jpg` | 1120x1600 | color | 16 | 主人公ズ |
| `V06-ILL-012` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0012_HD.jpg` | 1120x1600 | color | 18 | 男友達 |
| `V06-ILL-013` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0013_HD.jpg` | 1120x1600 | monochrome | 20 | ちんこ |
| `V06-ILL-014` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0014_HD.jpg` | 1120x1600 | color | 22 | ちんこ |
| `V06-ILL-015` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0015_HD.jpg` | 1120x1600 | color | 24 | 新たなるケツ路 |
| `V06-ILL-016` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0016_HD.jpg` | 1120x1600 | color | 26 | 那由多の景色 |
| `V06-ILL-017` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0017_HD.jpg` | 1120x1600 | monochrome | 28 | 白川京さん送別会 |
| `V06-ILL-018` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0018_HD.jpg` | 1120x1600 | color | 30 | 白川京さん送別会 |
| `V06-ILL-019` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0022_HD.jpg` | 1120x1600 | monochrome | 32 | クロニカクロニクル④ |
| `V06-ILL-020` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0026_HD.jpg` | 1120x1600 | monochrome | 34 | クロニカクロニクル④ |
| `V06-ILL-021` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0027_HD.jpg` | 1120x1600 | monochrome | 36 | クロニカクロニクル④ |
| `V06-ILL-022` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0028_HD.jpg` | 1120x1600 | monochrome | 37 | クロニカクロニクル④ |
| `V06-ILL-023` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0029_HD.jpg` | 1120x1600 | monochrome | 38 | クロニカクロニクル④ |
| `V06-ILL-024` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0030_HD.jpg` | 1120x1600 | monochrome | 39 | クロニカクロニクル④ |
| `V06-ILL-025` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0031_HD.jpg` | 1120x1600 | monochrome | 41 | キャストオーディション |
| `V06-ILL-026` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0032_HD.jpg` | 1120x1600 | monochrome | 43 | パブロ・プリケッソ |
| `V06-ILL-027` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0033_HD.jpg` | 1120x1600 | color | 45 | パブロ・プリケッソ |
| `V06-ILL-028` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0034_HD.jpg` | 1120x1600 | monochrome | 47 | 妬心 |
| `V06-ILL-029` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0035_HD.jpg` | 1120x1600 | color | 49 | 妬心 |
| `V06-ILL-030` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0036_HD.jpg` | 1120x1600 | monochrome | 51 | 新人賞授賞式 |
| `V06-ILL-031` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0037_HD.jpg` | 1120x1600 | monochrome | 53 | 新人賞授賞式 |
| `V06-ILL-032` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0038_HD.jpg` | 1120x1600 | monochrome | 55 | 新人賞授賞式 |
| `V06-ILL-033` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0039_HD.jpg` | 1120x1600 | monochrome | 57 | 二次会 |
| `V06-ILL-034` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0040_HD.jpg` | 1120x1600 | monochrome | 58 | 二次会 |
| `V06-ILL-035` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0041_HD.jpg` | 1120x1600 | monochrome | 61 | メインヒロイン |
| `V06-ILL-036` | `AUTHOR_AFTERWORD_ART` | `OEBPS/Images/embed0042_HD.jpg` | 1120x1600 | monochrome | 64 | あとがき |

### V07

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V07-ILL-001` | `COVER` | `OEBPS/Images/i-000a.jpg` | 1120x1600 | color | 0 | Start |
| `V07-ILL-002` | `FRONT_TITLE_PAGE` | `OEBPS/Images/i-0001_01.jpg` | 1099x1600 | color | 2 | Start |
| `V07-ILL-003` | `FRONT_SERIES_MAP` | `OEBPS/Images/i-0002_01.jpg` | 1124x1600 | color | 3 | Start |
| `V07-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/i-0003-0005_01.jpg` | 844x1600 | color | 4 | Start |
| `V07-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/i-0006-0008_01.jpg` | 1600x852 | color | 5 | Start |
| `V07-ILL-006` | `FRONT_CHARACTER_PROFILE` | `OEBPS/Images/i-0009_01.jpg` | 1120x1600 | monochrome | 7 | Start |
| `V07-ILL-007` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0019_01.jpg` | 1120x1600 | monochrome | 10 | 女友達の反応 |
| `V07-ILL-008` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0025_01.jpg` | 1120x1600 | monochrome | 12 | 女友達の反応 |
| `V07-ILL-009` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/i-0038_01.jpg` | 1120x1600 | monochrome | 14 | 担当の反応 |
| `V07-ILL-010` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0045_01.jpg` | 1120x1600 | color | 16 | 義弟の反応 |
| `V07-ILL-011` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0054_01.jpg` | 1120x1600 | color | 18 | 親友の反応 |
| `V07-ILL-012` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0061_01.jpg` | 1120x1600 | color | 20 | 税理士の反応 |
| `V07-ILL-013` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0087_01.jpg` | 1120x1600 | monochrome | 22 | 変わらないものと変わりゆくもの |
| `V07-ILL-014` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0095_01.jpg` | 1120x1600 | color | 24 | 変わらないものと変わりゆくもの |
| `V07-ILL-015` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0105_01.jpg` | 1120x1600 | color | 26 | ＬＥＶＥＬ４ |
| `V07-ILL-016` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0113_01.jpg` | 1120x1600 | monochrome | 28 | ライバル出現 |
| `V07-ILL-017` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0116_01.jpg` | 1120x1600 | color | 30 | ライバル出現 |
| `V07-ILL-018` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0133_01.jpg` | 1120x1600 | monochrome | 32 | 出会いと再会 |
| `V07-ILL-019` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0142_01.jpg` | 1120x1600 | color | 34 | 出会いと再会 |
| `V07-ILL-020` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0153_01.jpg` | 1120x1600 | monochrome | 36 | テンプレート・テンプテーション |
| `V07-ILL-021` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/i-0160_01.jpg` | 1120x1600 | monochrome | 38 | テンプレート・テンプテーション |
| `V07-ILL-022` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0173_01.jpg` | 1120x1600 | monochrome | 40 | ＴＨＥ ＬＡＳＴ ＣＲＹ ＩＮ ＨＡＤＥＳ |
| `V07-ILL-023` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0179_01.jpg` | 1120x1600 | monochrome | 42 | ＴＨＥ ＬＡＳＴ ＣＲＹ ＩＮ ＨＡＤＥＳ |
| `V07-ILL-024` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/i-0202_01.jpg` | 1120x1600 | monochrome | 44 | ＴＨＥ ＬＡＳＴ ＣＲＹ ＩＮ ＨＡＤＥＳ |
| `V07-ILL-025` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0209_01.jpg` | 1120x1600 | monochrome | 46 | 聖夜 |
| `V07-ILL-026` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0223_01.jpg` | 1120x1600 | monochrome | 48 | ぼーなすとらっく　妹のためのメルヒェン |
| `V07-ILL-027` | `AUTHOR_AFTERWORD_ART` | `OEBPS/Images/i-0257_01.jpg` | 1120x1600 | monochrome | 52 | あとがき |
| `V07-ILL-028` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzb_01.jpg` | 1133x1600 | color | 55 | 奥付 |
| `V07-ILL-029` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzb_02.jpg` | 1133x1600 | color | 56 | 奥付 |
| `V07-ILL-030` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzc_01.jpg` | 1600x752 | color | 57 | 奥付 |
| `V07-ILL-031` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzc_02.jpg` | 1600x749 | color | 58 | 奥付 |
| `V07-ILL-032` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzc_03.jpg` | 571x1600 | color | 59 | 奥付 |
| `V07-ILL-033` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_01.jpg` | 1120x1600 | color | 61 | ガガガ10周年電子特典　カバーイラスト |
| `V07-ILL-034` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_02.jpg` | 1120x1600 | color | 62 | ガガガ10周年電子特典　カバーイラスト |
| `V07-ILL-035` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_03.jpg` | 1120x1600 | color | 63 | ガガガ10周年電子特典　カバーイラスト |
| `V07-ILL-036` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_04.jpg` | 1120x1600 | color | 64 | ガガガ10周年電子特典　カバーイラスト |
| `V07-ILL-037` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_05.jpg` | 1120x1600 | color | 65 | ガガガ10周年電子特典　カバーイラスト |
| `V07-ILL-038` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_06.jpg` | 1120x1600 | color | 66 | ガガガ10周年電子特典　カバーイラスト |
| `V07-ILL-039` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_07.jpg` | 1120x1600 | color | 67 | ガガガ10周年電子特典　カバーイラスト |

### V08

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V08-ILL-001` | `COVER` | `OEBPS/Images/i-000a.jpg` | 1119x1600 | color | 0 | Start |
| `V08-ILL-002` | `FRONT_TITLE_PAGE` | `OEBPS/Images/i-0001_01.jpg` | 1120x1600 | color | 2 | Start |
| `V08-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/i-0002-0003_01.jpg` | 1600x1159 | color | 3 | Start |
| `V08-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/i-0004-0005_01.jpg` | 1600x1159 | color | 4 | Start |
| `V08-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/i-0006-0007_01.jpg` | 1600x1159 | color | 5 | Start |
| `V08-ILL-006` | `FRONT_SERIES_MAP` | `OEBPS/Images/i-0008_01.jpg` | 1119x1600 | color | 6 | Start |
| `V08-ILL-007` | `FRONT_CHARACTER_PROFILE` | `OEBPS/Images/i-0009_01.jpg` | 1120x1600 | monochrome | 8 | Start |
| `V08-ILL-008` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0026_01.jpg` | 1120x1600 | color | 11 | コミケにて |
| `V08-ILL-009` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0033_01.jpg` | 1120x1600 | monochrome | 13 | 新しい１年の始まり |
| `V08-ILL-010` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0039_01.jpg` | 1120x1600 | color | 15 | 新しい１年の始まり |
| `V08-ILL-011` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0053_01.jpg` | 1120x1600 | color | 18 | 干し芋 |
| `V08-ILL-012` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0067_01.jpg` | 1120x1600 | monochrome | 21 | 出逢ってしまった２人 |
| `V08-ILL-013` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/i-0073_01.jpg` | 1120x1600 | monochrome | 23 | 出逢ってしまった２人 |
| `V08-ILL-014` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0079_01.jpg` | 1120x1600 | monochrome | 25 | デビュー作発売 |
| `V08-ILL-015` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0086_01.jpg` | 1120x1600 | color | 27 | デビュー作発売 |
| `V08-ILL-016` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0097_01.jpg` | 1120x1600 | monochrome | 29 | ２代目ヤリチン王子 |
| `V08-ILL-017` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0113_01.jpg` | 1120x1600 | monochrome | 31 | ２代目ヤリチン王子 |
| `V08-ILL-018` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0129_01.jpg` | 1120x1600 | color | 33 | ２代目ヤリチン王子 |
| `V08-ILL-019` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/i-0139_01.jpg` | 1120x1600 | monochrome | 35 | 父 |
| `V08-ILL-020` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0167_01.jpg` | 1120x1600 | monochrome | 38 | ルームシェア |
| `V08-ILL-021` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0169_01.jpg` | 1120x1600 | color | 40 | ルームシェア |
| `V08-ILL-022` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0177_01.jpg` | 1120x1600 | monochrome | 43 | 今回さすがに下ネタが多すぎるんじゃないかと反省しています |
| `V08-ILL-023` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0195_01.jpg` | 1120x1600 | color | 46 | 職業病 |
| `V08-ILL-024` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0198_01.jpg` | 1120x1600 | color | 48 | 職業病 |
| `V08-ILL-025` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0207_01.jpg` | 1120x1600 | monochrome | 50 | 秋葉原デート |
| `V08-ILL-026` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/i-0211_01.jpg` | 1120x1600 | monochrome | 52 | 秋葉原デート |
| `V08-ILL-027` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/i-0215_01.jpg` | 1120x1600 | color | 54 | 秋葉原デート |
| `V08-ILL-028` | `AFTERWORD_EXTERNAL_LINK_QR` | `OEBPS/Images/i-0224_01.jpg` | 100x101 | monochrome | 56 | あとがき |
| `V08-ILL-029` | `AUTHOR_AFTERWORD_ART` | `OEBPS/Images/i-0225_01.jpg` | 1120x1600 | monochrome | 57 | あとがき |
| `V08-ILL-030` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzb_01.jpg` | 562x1600 | color | 60 | 奥付 |
| `V08-ILL-031` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzb_02.jpg` | 1114x1600 | color | 61 | 奥付 |
| `V08-ILL-032` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzb_03.jpg` | 1107x1600 | color | 62 | 奥付 |
| `V08-ILL-033` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzb_04.jpg` | 1108x1600 | color | 63 | 奥付 |
| `V08-ILL-034` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzb_05.jpg` | 1107x1600 | color | 64 | 奥付 |
| `V08-ILL-035` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzb_06.jpg` | 1109x1600 | color | 65 | 奥付 |
| `V08-ILL-036` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzb_07.jpg` | 1109x1600 | color | 66 | 奥付 |
| `V08-ILL-037` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzc_01.jpg` | 1600x1126 | color | 67 | 奥付 |
| `V08-ILL-038` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzc_02.jpg` | 1145x1600 | color | 68 | 奥付 |
| `V08-ILL-039` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzc_03.jpg` | 1143x1600 | color | 69 | 奥付 |
| `V08-ILL-040` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzc_04.jpg` | 1136x1600 | color | 70 | 奥付 |
| `V08-ILL-041` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzc_05.jpg` | 1141x1600 | color | 71 | 奥付 |
| `V08-ILL-042` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzc_06.jpg` | 1135x1600 | color | 72 | 奥付 |
| `V08-ILL-043` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzc_07.jpg` | 1120x1600 | color | 73 | 奥付 |
| `V08-ILL-044` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_01.jpg` | 1120x1600 | color | 75 | ガガガ10周年電子特典　カバーイラスト |
| `V08-ILL-045` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_02.jpg` | 1120x1600 | color | 76 | ガガガ10周年電子特典　カバーイラスト |
| `V08-ILL-046` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_03.jpg` | 1120x1600 | color | 77 | ガガガ10周年電子特典　カバーイラスト |
| `V08-ILL-047` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_04.jpg` | 1120x1600 | color | 78 | ガガガ10周年電子特典　カバーイラスト |
| `V08-ILL-048` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_05.jpg` | 1120x1600 | color | 79 | ガガガ10周年電子特典　カバーイラスト |
| `V08-ILL-049` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_06.jpg` | 1120x1600 | color | 80 | ガガガ10周年電子特典　カバーイラスト |
| `V08-ILL-050` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_07.jpg` | 1120x1600 | color | 81 | ガガガ10周年電子特典　カバーイラスト |
| `V08-ILL-051` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/i-zzzk_08.jpg` | 1120x1600 | color | 82 | ガガガ10周年電子特典　カバーイラスト |
| `V08-ILL-052` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzd_01.jpg` | 1141x1600 | color | 84 | ガガガ文庫ＰＲ |
| `V08-ILL-053` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzd_02.jpg` | 1600x1122 | color | 85 | ガガガ文庫ＰＲ |
| `V08-ILL-054` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzd_03.jpg` | 1600x1150 | color | 86 | ガガガ文庫ＰＲ |
| `V08-ILL-055` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzd_04.jpg` | 1600x1153 | color | 87 | ガガガ文庫ＰＲ |
| `V08-ILL-056` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzzd_05.jpg` | 1133x1600 | color | 88 | ガガガ文庫ＰＲ |
| `V08-ILL-057` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzze_01.jpg` | 1600x1110 | color | 89 | ガガガ文庫ＰＲ |
| `V08-ILL-058` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzze_02.jpg` | 1600x1193 | color | 90 | ガガガ文庫ＰＲ |
| `V08-ILL-059` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzze_03.jpg` | 1600x1127 | color | 91 | ガガガ文庫ＰＲ |
| `V08-ILL-060` | `PROMOTIONAL_AD` | `OEBPS/Images/i-zzze_04.jpg` | 1600x1138 | color | 92 | ガガガ文庫ＰＲ |

### V09

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V09-ILL-001` | `COVER` | `OEBPS/Images/embed0066_HD.jpg` | 1120x1600 | color | 0 |  |
| `V09-ILL-002` | `FRONT_TITLE_PAGE` | `OEBPS/Images/embed0000_HD.jpg` | 1121x1600 | color | 2 |  |
| `V09-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0001_HD.jpg` | 1600x1143 | color | 3 |  |
| `V09-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0002_HD.jpg` | 1600x1143 | color | 4 |  |
| `V09-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0003_HD.jpg` | 1600x1142 | color | 5 |  |
| `V09-ILL-006` | `FRONT_SERIES_MAP` | `OEBPS/Images/embed0004_HD.jpg` | 1119x1600 | color | 6 |  |
| `V09-ILL-007` | `FRONT_CHARACTER_PROFILE` | `OEBPS/Images/embed0005_HD.jpg` | 1120x1600 | monochrome | 9 | すっかり残念なおばちゃんキャラが定着しつつありますがそういえばこの人税理士でした |
| `V09-ILL-008` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0007_HD.jpg` | 1120x1600 | color | 11 | すっかり残念なおばちゃんキャラが定着しつつありますがそういえばこの人税理士でした |
| `V09-ILL-009` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0008_HD.jpg` | 1120x1600 | color | 14 | クリエイター２人とルームシェアすることになった女子大生の悩み |
| `V09-ILL-010` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0009_HD.jpg` | 1120x1600 | monochrome | 16 | 来年の桜 |
| `V09-ILL-011` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0010_HD.jpg` | 1120x1600 | monochrome | 18 | 来年の桜 |
| `V09-ILL-012` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0011_HD.jpg` | 1120x1600 | monochrome | 20 | 来年の桜 |
| `V09-ILL-013` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0012_HD.jpg` | 1120x1600 | monochrome | 23 | 新人作家とお兄ちゃん先輩 |
| `V09-ILL-014` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0013_HD.jpg` | 1120x1600 | monochrome | 25 | 新人作家とお兄ちゃん先輩 |
| `V09-ILL-015` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0014_HD.jpg` | 1120x1600 | color | 27 | ヤバいトラブル（何がヤバいってこのレベルがよくある話なのが一番ヤバい） |
| `V09-ILL-016` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0016_HD.jpg` | 1120x1600 | color | 29 | もしもの話 |
| `V09-ILL-017` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0017_HD.jpg` | 1120x1600 | monochrome | 31 | 天使降臨 |
| `V09-ILL-018` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0018_HD.jpg` | 1120x1600 | monochrome | 33 | 天使降臨 |
| `V09-ILL-019` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0019_HD.jpg` | 1120x1600 | monochrome | 36 | 千尋の焦り |
| `V09-ILL-020` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0020_HD.jpg` | 1120x1600 | color | 38 | 千尋の焦り |
| `V09-ILL-021` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0021_HD.jpg` | 1120x1600 | monochrome | 40 | 憧れの人 |
| `V09-ILL-022` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0022_HD.jpg` | 1120x1600 | monochrome | 42 | アフレコ |
| `V09-ILL-023` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0023_HD.jpg` | 1120x1600 | color | 44 | 千尋の人生相談 |
| `V09-ILL-024` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0024_HD.jpg` | 1120x1600 | color | 46 | シュウカツ！ |
| `V09-ILL-025` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0025_HD.jpg` | 1120x1600 | monochrome | 48 | 見えてきた道 |
| `V09-ILL-026` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0026_HD.jpg` | 1120x1600 | color | 50 | 見えてきた道 |
| `V09-ILL-027` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0027_HD.jpg` | 1120x1600 | color | 53 | おめでた |
| `V09-ILL-028` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0028_HD.jpg` | 1120x1600 | monochrome | 55 | シロバコ |
| `V09-ILL-029` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0029_HD.jpg` | 1120x1600 | monochrome | 57 | クロニカクロニクル最終章　～そして爆発へ～ |
| `V09-ILL-030` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0030_HD.jpg` | 1120x1600 | monochrome | 59 | クロニカクロニクル最終章　～そして爆発へ～ |
| `V09-ILL-031` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0031_HD.jpg` | 1120x1600 | monochrome | 60 | クロニカクロニクル最終章　～そして爆発へ～ |
| `V09-ILL-032` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0032_HD.jpg` | 1120x1600 | monochrome | 61 | クロニカクロニクル最終章　～そして爆発へ～ |
| `V09-ILL-033` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0037_HD.jpg` | 1120x1600 | monochrome | 63 | クロニカクロニクル最終章　～そして爆発へ～ |
| `V09-ILL-034` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0039_HD.jpg` | 1120x1600 | monochrome | 65 | クロニカクロニクル最終章　～そして爆発へ～ |
| `V09-ILL-035` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0040_HD.jpg` | 1120x1600 | monochrome | 67 | クロニカクロニクル最終章　～そして爆発へ～ |
| `V09-ILL-036` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0042_HD.jpg` | 1120x1600 | monochrome | 69 | クロニカクロニクル最終章　～そして爆発へ～ |
| `V09-ILL-037` | `AUTHOR_AFTERWORD_ART` | `OEBPS/Images/embed0043_HD.jpg` | 1120x1600 | monochrome | 74 | あとがき |
| `V09-ILL-038` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0044_HD.jpg` | 568x1600 | color | 77 | 奥付 |
| `V09-ILL-039` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0045_HD.jpg` | 1117x1600 | color | 78 | 奥付 |
| `V09-ILL-040` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0046_HD.jpg` | 1109x1600 | color | 79 | 奥付 |
| `V09-ILL-041` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0047_HD.jpg` | 1600x1112 | color | 80 | 奥付 |
| `V09-ILL-042` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0048_HD.jpg` | 1111x1600 | color | 81 | 奥付 |
| `V09-ILL-043` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0049_HD.jpg` | 1111x1600 | color | 82 | 奥付 |
| `V09-ILL-044` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0050_HD.jpg` | 1600x1114 | color | 83 | 奥付 |
| `V09-ILL-045` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0051_HD.jpg` | 1139x1600 | color | 84 | 奥付 |
| `V09-ILL-046` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0052_HD.jpg` | 1123x1600 | color | 85 | 奥付 |
| `V09-ILL-047` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0053_HD.jpg` | 1144x1600 | color | 86 | 奥付 |
| `V09-ILL-048` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0054_HD.jpg` | 1146x1600 | color | 87 | 奥付 |
| `V09-ILL-049` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0055_HD.jpg` | 1094x1600 | color | 88 | 奥付 |
| `V09-ILL-050` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0056_HD.jpg` | 1080x1600 | color | 89 | 奥付 |
| `V09-ILL-051` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/embed0057_HD.jpg` | 1120x1600 | color | 91 | ガガガ10周年電子特典　カバーイラスト |
| `V09-ILL-052` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/embed0058_HD.jpg` | 1120x1600 | color | 92 | ガガガ10周年電子特典　カバーイラスト |
| `V09-ILL-053` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/embed0059_HD.jpg` | 1120x1600 | color | 93 | ガガガ10周年電子特典　カバーイラスト |
| `V09-ILL-054` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/embed0060_HD.jpg` | 1120x1600 | color | 94 | ガガガ10周年電子特典　カバーイラスト |
| `V09-ILL-055` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/embed0061_HD.jpg` | 1120x1600 | color | 95 | ガガガ10周年電子特典　カバーイラスト |
| `V09-ILL-056` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/embed0062_HD.jpg` | 1120x1600 | color | 96 | ガガガ10周年電子特典　カバーイラスト |
| `V09-ILL-057` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/embed0063_HD.jpg` | 1120x1600 | color | 97 | ガガガ10周年電子特典　カバーイラスト |
| `V09-ILL-058` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/embed0064_HD.jpg` | 1120x1600 | color | 98 | ガガガ10周年電子特典　カバーイラスト |
| `V09-ILL-059` | `RETAILER_EBOOK_BONUS_COVER` | `OEBPS/Images/embed0065_HD.jpg` | 1120x1600 | color | 99 | ガガガ10周年電子特典　カバーイラスト |

### V10

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V10-ILL-001` | `COVER` | `OEBPS/Images/embed0039_HD.jpg` | 1120x1600 | color | 0 |  |
| `V10-ILL-002` | `FRONT_TITLE_PAGE` | `OEBPS/Images/embed0000_HD.jpg` | 1119x1600 | color | 2 |  |
| `V10-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0001_HD.jpg` | 1600x1159 | color | 3 |  |
| `V10-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0002_HD.jpg` | 1600x1159 | color | 4 |  |
| `V10-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0003_HD.jpg` | 1600x1159 | color | 5 |  |
| `V10-ILL-006` | `FRONT_SERIES_MAP` | `OEBPS/Images/embed0004_HD.jpg` | 1119x1600 | color | 6 |  |
| `V10-ILL-007` | `FRONT_CHARACTER_PROFILE` | `OEBPS/Images/embed0005_HD.jpg` | 1120x1600 | monochrome | 8 |  |
| `V10-ILL-008` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0006_HD.jpg` | 1120x1600 | monochrome | 10 | 番外編　羽島千尋の誕生 |
| `V10-ILL-009` | `NARRATIVE_CHARACTER_PROFILE` | `OEBPS/Images/embed0007_HD.jpg` | 1120x1600 | monochrome | 12 | 番外編　羽島千尋の誕生 |
| `V10-ILL-010` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0008_HD.jpg` | 1120x1600 | monochrome | 14 | 俺の弟が妹だった件について |
| `V10-ILL-011` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0010_HD.jpg` | 1120x1600 | monochrome | 17 | 彼女の不安 |
| `V10-ILL-012` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0011_HD.jpg` | 1120x1600 | monochrome | 19 | マンガ家は妹キ●ガイ |
| `V10-ILL-013` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0012_HD.jpg` | 1120x1600 | color | 22 | 原風景 |
| `V10-ILL-014` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0013_HD.jpg` | 1120x1600 | monochrome | 24 | 妹のいる生活 |
| `V10-ILL-015` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0014_HD.jpg` | 1120x1600 | monochrome | 27 | 義妹ＶＳ妹キャラ |
| `V10-ILL-016` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0015_HD.jpg` | 1120x1600 | color | 29 | 義妹ＶＳ妹キャラ |
| `V10-ILL-017` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0016_HD.jpg` | 1120x1600 | color | 31 | 京の選択 |
| `V10-ILL-018` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0017_HD.jpg` | 1120x1600 | monochrome | 33 | ２０歳 |
| `V10-ILL-019` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0018_HD.jpg` | 1120x1600 | color | 35 | 妹と買い物 |
| `V10-ILL-020` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0019_HD.jpg` | 1120x1600 | monochrome | 37 | 砂漠 |
| `V10-ILL-021` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0020_HD.jpg` | 1120x1600 | color | 38 | 砂漠 |
| `V10-ILL-022` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0021_HD.jpg` | 1120x1600 | monochrome | 40 | 謝謝台湾 |
| `V10-ILL-023` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0022_HD.jpg` | 1120x1600 | color | 42 | 謝謝台湾 |
| `V10-ILL-024` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0023_HD.jpg` | 1120x1600 | monochrome | 44 | 秋葉原デート２ |
| `V10-ILL-025` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0024_HD.jpg` | 1120x1600 | color | 46 | 秋葉原デート２ |
| `V10-ILL-026` | `AUTHOR_AFTERWORD_ART` | `OEBPS/Images/embed0025_HD.jpg` | 1120x1600 | monochrome | 51 | あとがき |
| `V10-ILL-027` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0026_HD.jpg` | 1600x1129 | color | 54 | 奥付 |
| `V10-ILL-028` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0027_HD.jpg` | 1600x1129 | color | 55 | 奥付 |
| `V10-ILL-029` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0028_HD.jpg` | 1124x1600 | color | 56 | 奥付 |
| `V10-ILL-030` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0029_HD.jpg` | 1127x1600 | color | 57 | 奥付 |
| `V10-ILL-031` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0030_HD.jpg` | 1123x1600 | color | 58 | 奥付 |
| `V10-ILL-032` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0031_HD.jpg` | 1123x1600 | color | 59 | 奥付 |
| `V10-ILL-033` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0032_HD.jpg` | 1600x1129 | color | 60 | 奥付 |
| `V10-ILL-034` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0033_HD.jpg` | 1145x1600 | color | 61 | 奥付 |
| `V10-ILL-035` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0034_HD.jpg` | 1145x1600 | color | 62 | 奥付 |
| `V10-ILL-036` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0035_HD.jpg` | 1171x1600 | color | 63 | 奥付 |
| `V10-ILL-037` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0036_HD.jpg` | 1115x1600 | color | 64 | 奥付 |
| `V10-ILL-038` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0037_HD.jpg` | 1132x1600 | color | 65 | 奥付 |
| `V10-ILL-039` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0038_HD.jpg` | 1139x1600 | color | 66 | 奥付 |

### V11

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V11-ILL-001` | `COVER` | `OEBPS/Images/embed0056_HD.jpg` | 1119x1600 | color | 0 |  |
| `V11-ILL-002` | `FRONT_TITLE_PAGE` | `OEBPS/Images/embed0000_HD.jpg` | 1152x1600 | color | 2 |  |
| `V11-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0001_HD.jpg` | 1600x1159 | color | 3 |  |
| `V11-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0002_HD.jpg` | 1600x1159 | color | 4 |  |
| `V11-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `OEBPS/Images/embed0003_HD.jpg` | 1600x1159 | color | 5 |  |
| `V11-ILL-006` | `FRONT_SERIES_MAP` | `OEBPS/Images/embed0004_HD.jpg` | 1152x1600 | color | 6 |  |
| `V11-ILL-007` | `FRONT_CHARACTER_PROFILE` | `OEBPS/Images/embed0005_HD.jpg` | 1120x1600 | monochrome | 8 |  |
| `V11-ILL-008` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0007_HD.jpg` | 1120x1600 | monochrome | 11 | 小説家は妹キ●ガイ、だった |
| `V11-ILL-009` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0008_HD.jpg` | 1120x1600 | monochrome | 13 | 鎌倉旅行 |
| `V11-ILL-010` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0009_HD.jpg` | 1120x1600 | color | 15 | 鎌倉旅行 |
| `V11-ILL-011` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0010_HD.jpg` | 1120x1600 | monochrome | 18 | 妹が多すぎる。 |
| `V11-ILL-012` | `NARRATIVE_GAME_OR_DIAGRAM` | `OEBPS/Images/embed0011_HD.jpg` | 1120x1600 | monochrome | 19 | 妹が多すぎる。 |
| `V11-ILL-013` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0012_HD.jpg` | 1120x1600 | monochrome | 21 | 妹が多すぎる。 |
| `V11-ILL-014` | `NARRATIVE_QA_PARATEXT` | `OEBPS/Images/embed0013_HD.jpg` | 1120x1600 | color | 22 | 妹が多すぎる。 |
| `V11-ILL-015` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0015_HD.jpg` | 1120x1600 | monochrome | 24 | 堕天 |
| `V11-ILL-016` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0016_HD.jpg` | 1120x1600 | monochrome | 26 | 堕天 |
| `V11-ILL-017` | `IN_TEXT_PUBLISHING_ARTIFACT` | `OEBPS/Images/embed0017_HD.jpg` | 563x1600 | monochrome | 27 | オビを考えよう |
| `V11-ILL-018` | `IN_TEXT_PUBLISHING_ARTIFACT` | `OEBPS/Images/embed0018_HD.jpg` | 492x720 | monochrome | 27 | オビを考えよう |
| `V11-ILL-019` | `IN_TEXT_PUBLISHING_ARTIFACT` | `OEBPS/Images/embed0019_HD.jpg` | 492x720 | monochrome | 27 | オビを考えよう |
| `V11-ILL-020` | `IN_TEXT_PUBLISHING_ARTIFACT` | `OEBPS/Images/embed0020_HD.jpg` | 1120x1600 | monochrome | 27 | オビを考えよう |
| `V11-ILL-021` | `IN_TEXT_PUBLISHING_ARTIFACT` | `OEBPS/Images/embed0021_HD.jpg` | 494x720 | monochrome | 27 | オビを考えよう |
| `V11-ILL-022` | `IN_TEXT_PUBLISHING_ARTIFACT` | `OEBPS/Images/embed0022_HD.jpg` | 494x720 | monochrome | 27 | オビを考えよう |
| `V11-ILL-023` | `IN_TEXT_PUBLISHING_ARTIFACT` | `OEBPS/Images/embed0023_HD.jpg` | 563x1600 | monochrome | 27 | オビを考えよう |
| `V11-ILL-024` | `IN_TEXT_PUBLISHING_ARTIFACT` | `OEBPS/Images/embed0024_HD.jpg` | 563x1600 | monochrome | 27 | オビを考えよう |
| `V11-ILL-025` | `IN_TEXT_PUBLISHING_ARTIFACT` | `OEBPS/Images/embed0025_HD.jpg` | 563x1600 | monochrome | 27 | オビを考えよう |
| `V11-ILL-026` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0026_HD.jpg` | 1120x1600 | monochrome | 28 | オビを考えよう |
| `V11-ILL-027` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0027_HD.jpg` | 1120x1600 | monochrome | 30 | アンチテーゼ |
| `V11-ILL-028` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0028_HD.jpg` | 1120x1600 | monochrome | 33 | 初と京 |
| `V11-ILL-029` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0029_HD.jpg` | 1120x1600 | monochrome | 35 | 初と京 |
| `V11-ILL-030` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0030_HD.jpg` | 1120x1600 | monochrome | 36 | 初と京 |
| `V11-ILL-031` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0031_HD.jpg` | 1120x1600 | monochrome | 38 | シェリア |
| `V11-ILL-032` | `NARRATIVE_DOCUMENT` | `OEBPS/Images/embed0032_HD.jpg` | 1120x1600 | monochrome | 40 | シェリア |
| `V11-ILL-033` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0033_HD.jpg` | 1600x1159 | monochrome | 42 | 結果 |
| `V11-ILL-034` | `NARRATIVE_FORMAL_DEVICE` | `OEBPS/Images/embed0034.jpg` | 1600x1142 | color | 43 | 結果 |
| `V11-ILL-035` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0035_HD.jpg` | 1120x1600 | monochrome | 46 | 家族になる |
| `V11-ILL-036` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0037_HD.jpg` | 1120x1600 | monochrome | 49 | 幻影のシリウス |
| `V11-ILL-037` | `NARRATIVE_ILLUSTRATION` | `OEBPS/Images/embed0038_HD.jpg` | 1120x1600 | color | 52 | 他の誰が許そうとも、彼女だけはそれを許しはしない |
| `V11-ILL-038` | `AUTHOR_AFTERWORD_ART` | `OEBPS/Images/embed0039_HD.jpg` | 1120x1600 | monochrome | 56 | あとがき |
| `V11-ILL-039` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0040_HD.jpg` | 1600x1128 | color | 59 | 奥付 |
| `V11-ILL-040` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0041_HD.jpg` | 1125x1600 | color | 60 | 奥付 |
| `V11-ILL-041` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0042_HD.jpg` | 1131x1600 | color | 61 | 奥付 |
| `V11-ILL-042` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0043_HD.jpg` | 1157x1600 | color | 62 | 奥付 |
| `V11-ILL-043` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0044_HD.jpg` | 1125x1600 | color | 63 | 奥付 |
| `V11-ILL-044` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0045_HD.jpg` | 1105x1600 | color | 64 | 奥付 |
| `V11-ILL-045` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0046_HD.jpg` | 1124x1600 | color | 65 | 奥付 |
| `V11-ILL-046` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0047_HD.jpg` | 1600x1130 | color | 66 | 奥付 |
| `V11-ILL-047` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0048_HD.jpg` | 1119x1600 | color | 67 | 奥付 |
| `V11-ILL-048` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0049_HD.jpg` | 1133x1600 | color | 68 | 奥付 |
| `V11-ILL-049` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0050_HD.jpg` | 1160x1600 | color | 69 | 奥付 |
| `V11-ILL-050` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0051_HD.jpg` | 1103x1600 | color | 70 | 奥付 |
| `V11-ILL-051` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0052_HD.jpg` | 1133x1600 | color | 71 | 奥付 |
| `V11-ILL-052` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0053_HD.jpg` | 1146x1600 | color | 72 | 奥付 |
| `V11-ILL-053` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0054_HD.jpg` | 1600x1130 | color | 73 | 奥付 |
| `V11-ILL-054` | `PROMOTIONAL_AD` | `OEBPS/Images/embed0055_HD.jpg` | 1600x1130 | color | 74 | 奥付 |

### V12

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V12-ILL-001` | `COVER` | `cover.jpeg` | 944x1350 | color | 0 |  |
| `V12-ILL-002` | `FRONT_TITLE_PAGE` | `images/00001.jpeg` | 972x1388 | color | 2 |  |
| `V12-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `images/00002.jpeg` | 1030x736 | color | 3 |  |
| `V12-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `images/00003.jpeg` | 1030x736 | color | 4 |  |
| `V12-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `images/00004.jpeg` | 1030x735 | color | 5 |  |
| `V12-ILL-006` | `FRONT_SERIES_MAP` | `images/00005.jpeg` | 972x1388 | color | 6 |  |
| `V12-ILL-007` | `FRONT_CHARACTER_PROFILE` | `images/00006.jpeg` | 971x1388 | monochrome | 8 |  |
| `V12-ILL-008` | `NARRATIVE_CHARACTER_PROFILE` | `images/00011.jpeg` | 971x1388 | monochrome | 12 | 笠松青葉ルート（罠） |
| `V12-ILL-009` | `NARRATIVE_ILLUSTRATION` | `images/00013.jpeg` | 971x1388 | monochrome | 14 | グレる |
| `V12-ILL-010` | `NARRATIVE_CHARACTER_PROFILE` | `images/00014.jpeg` | 971x1388 | monochrome | 17 | ミッションインポッシブル |
| `V12-ILL-011` | `NARRATIVE_ILLUSTRATION` | `images/00016.jpeg` | 971x1388 | monochrome | 20 | 説得 |
| `V12-ILL-012` | `NARRATIVE_QA_PARATEXT` | `images/00017.jpeg` | 971x1388 | color | 22 | 説得 |
| `V12-ILL-013` | `NARRATIVE_ILLUSTRATION` | `images/00018.jpeg` | 930x1328 | monochrome | 25 | ロストマン |
| `V12-ILL-014` | `NARRATIVE_QA_PARATEXT` | `images/00019.jpeg` | 971x1388 | color | 27 | ロストマン |
| `V12-ILL-015` | `NARRATIVE_QA_PARATEXT` | `images/00021.jpeg` | 971x1388 | monochrome | 30 | クリスマス女子会 |
| `V12-ILL-016` | `NARRATIVE_ILLUSTRATION` | `images/00022.jpeg` | 943x1347 | monochrome | 32 | コミケにて② |
| `V12-ILL-017` | `NARRATIVE_ILLUSTRATION` | `images/00023.jpeg` | 971x1388 | monochrome | 35 | 正解のない道 |
| `V12-ILL-018` | `NARRATIVE_ILLUSTRATION` | `images/00024.jpeg` | 971x1388 | monochrome | 38 | 勇真が訊く！ 第１回：小説家、可児那由多 |
| `V12-ILL-019` | `NARRATIVE_CHARACTER_PROFILE` | `images/00025.jpeg` | 971x1388 | monochrome | 40 | 勇真が訊く！ 第１回：小説家、可児那由多 |
| `V12-ILL-020` | `NARRATIVE_ILLUSTRATION` | `images/00026.jpeg` | 971x1388 | monochrome | 42 | 神ケツ少女の憂鬱 |
| `V12-ILL-021` | `NARRATIVE_QA_PARATEXT` | `images/00027.jpeg` | 971x1388 | color | 44 | 神ケツ少女の憂鬱 |
| `V12-ILL-022` | `NARRATIVE_ILLUSTRATION` | `images/00028.jpeg` | 972x1388 | monochrome | 46 | 新しい恋 |
| `V12-ILL-023` | `NARRATIVE_ILLUSTRATION` | `images/00029.jpeg` | 971x1388 | monochrome | 49 | 栞 |
| `V12-ILL-024` | `NARRATIVE_ILLUSTRATION` | `images/00030.jpeg` | 971x1388 | monochrome | 51 | 蘇生 |
| `V12-ILL-025` | `NARRATIVE_CHARACTER_PROFILE` | `images/00031.jpeg` | 971x1388 | monochrome | 53 | 蘇生 |
| `V12-ILL-026` | `AUTHOR_AFTERWORD_ART` | `images/00032.jpeg` | 971x1388 | monochrome | 57 | あとがき |
| `V12-ILL-027` | `PROMOTIONAL_AD` | `images/00033.jpeg` | 1030x725 | color | 60 | 奥付 |
| `V12-ILL-028` | `PROMOTIONAL_AD` | `images/00034.jpeg` | 1030x725 | color | 61 | 奥付 |
| `V12-ILL-029` | `PROMOTIONAL_AD` | `images/00035.jpeg` | 911x1288 | color | 62 | 奥付 |
| `V12-ILL-030` | `PROMOTIONAL_AD` | `images/00036.jpeg` | 920x1301 | color | 63 | 奥付 |
| `V12-ILL-031` | `PROMOTIONAL_AD` | `images/00037.jpeg` | 981x1388 | color | 64 | 奥付 |
| `V12-ILL-032` | `PROMOTIONAL_AD` | `images/00038.jpeg` | 907x1282 | color | 65 | 奥付 |
| `V12-ILL-033` | `PROMOTIONAL_AD` | `images/00039.jpeg` | 940x661 | color | 66 | 奥付 |
| `V12-ILL-034` | `PROMOTIONAL_AD` | `images/00040.jpeg` | 737x1042 | color | 67 | 奥付 |
| `V12-ILL-035` | `PROMOTIONAL_AD` | `images/00041.jpeg` | 733x1036 | color | 68 | 奥付 |
| `V12-ILL-036` | `PROMOTIONAL_AD` | `images/00042.jpeg` | 857x1211 | color | 69 | 奥付 |
| `V12-ILL-037` | `PROMOTIONAL_AD` | `images/00043.jpeg` | 749x1059 | color | 70 | 奥付 |
| `V12-ILL-038` | `PROMOTIONAL_AD` | `images/00044.jpeg` | 616x871 | color | 71 | 奥付 |
| `V12-ILL-039` | `PROMOTIONAL_AD` | `images/00045.jpeg` | 713x1009 | color | 72 | 奥付 |

### V13

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V13-ILL-001` | `COVER` | `cover.jpeg` | 887x1268 | color | 0 |  |
| `V13-ILL-002` | `FRONT_TITLE_PAGE` | `images/00001.jpeg` | 971x1388 | color | 2 |  |
| `V13-ILL-003` | `FRONT_SERIES_MAP` | `images/00002.jpeg` | 972x1388 | color | 3 |  |
| `V13-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `images/00003.jpeg` | 1030x544 | color | 4 |  |
| `V13-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `images/00004.jpeg` | 1030x544 | color | 5 |  |
| `V13-ILL-006` | `FRONT_CHARACTER_PROFILE` | `images/00005.jpeg` | 952x1361 | monochrome | 7 |  |
| `V13-ILL-007` | `NARRATIVE_ILLUSTRATION` | `images/00006.jpeg` | 903x1290 | monochrome | 9 | 卒業旅行 |
| `V13-ILL-008` | `NARRATIVE_ILLUSTRATION` | `images/00008.jpeg` | 933x1333 | monochrome | 12 | 城ヶ峰信長 |
| `V13-ILL-009` | `NARRATIVE_CHARACTER_PROFILE` | `images/00009.jpeg` | 951x1358 | monochrome | 14 | 城ヶ峰信長 |
| `V13-ILL-010` | `NARRATIVE_ILLUSTRATION` | `images/00010.jpeg` | 921x1315 | monochrome | 16 | ワードウルフ |
| `V13-ILL-011` | `NARRATIVE_DOCUMENT` | `images/00011.jpeg` | 951x1358 | monochrome | 18 | ワードウルフ |
| `V13-ILL-012` | `NARRATIVE_ILLUSTRATION` | `images/00012.jpeg` | 971x1388 | monochrome | 20 | 作家転生 |
| `V13-ILL-013` | `NARRATIVE_QA_PARATEXT` | `images/00013.jpeg` | 972x1388 | color | 23 | オタサーの姫 |
| `V13-ILL-014` | `NARRATIVE_ILLUSTRATION` | `images/00014.jpeg` | 971x1388 | monochrome | 25 | アホ |
| `V13-ILL-015` | `NARRATIVE_DOCUMENT` | `images/00016.jpeg` | 971x1388 | monochrome | 29 | 変わりゆく者たち |
| `V13-ILL-016` | `NARRATIVE_ILLUSTRATION` | `images/00017.jpeg` | 971x1388 | monochrome | 32 | 暗黒騎士 |
| `V13-ILL-017` | `NARRATIVE_CHARACTER_PROFILE` | `images/00018.jpeg` | 971x1388 | monochrome | 34 | 暗黒騎士 |
| `V13-ILL-018` | `NARRATIVE_ILLUSTRATION` | `images/00020.jpeg` | 971x1388 | color | 36 | 君が好き |
| `V13-ILL-019` | `NARRATIVE_QA_PARATEXT` | `images/00021.jpeg` | 972x1388 | color | 37 | 君が好き |
| `V13-ILL-020` | `NARRATIVE_ILLUSTRATION` | `images/00022.jpeg` | 971x1388 | monochrome | 39 | １ｓｔ Ｐｒｉｏｒｉｔｙ |
| `V13-ILL-021` | `NARRATIVE_DOCUMENT` | `images/00023.jpeg` | 971x1388 | monochrome | 41 | １ｓｔ Ｐｒｉｏｒｉｔｙ |
| `V13-ILL-022` | `NARRATIVE_ILLUSTRATION` | `images/00024.jpeg` | 932x1332 | monochrome | 43 | 蒼穹の誓い |
| `V13-ILL-023` | `WORK_WITHIN_WORK_GRAPHIC` | `images/00025.jpeg` | 861x1230 | monochrome | 46 | 妹さえいればいい。ＴＨＥ ＭＯＶＩＥ 妹・オブ・ザ・デッド |
| `V13-ILL-024` | `NARRATIVE_ILLUSTRATION` | `images/00027.jpeg` | 970x1388 | monochrome | 48 | 妹さえいればいい。ＴＨＥ ＭＯＶＩＥ 妹・オブ・ザ・デッド |
| `V13-ILL-025` | `NARRATIVE_DOCUMENT` | `images/00028.jpeg` | 907x1296 | monochrome | 51 | あとがき |
| `V13-ILL-026` | `AUTHOR_AFTERWORD_DOCUMENT` | `images/00029.jpeg` | 915x1307 | monochrome | 52 | あとがき |
| `V13-ILL-027` | `AUTHOR_AFTERWORD_DOCUMENT` | `images/00030.jpeg` | 971x1388 | monochrome | 53 | あとがき |
| `V13-ILL-028` | `AUTHOR_AFTERWORD_DOCUMENT` | `images/00031.jpeg` | 913x1305 | monochrome | 54 | あとがき |
| `V13-ILL-029` | `AUTHOR_AFTERWORD_DOCUMENT` | `images/00032.jpeg` | 971x1388 | monochrome | 55 | あとがき |
| `V13-ILL-030` | `AUTHOR_AFTERWORD_DOCUMENT` | `images/00033.jpeg` | 916x1309 | monochrome | 56 | あとがき |
| `V13-ILL-031` | `AUTHOR_AFTERWORD_ART` | `images/00034.jpeg` | 971x1388 | monochrome | 57 | あとがき |
| `V13-ILL-032` | `PROMOTIONAL_AD` | `images/00035.jpeg` | 491x1388 | color | 60 | 奥付 |
| `V13-ILL-033` | `PROMOTIONAL_AD` | `images/00036.jpeg` | 931x1315 | color | 61 | 奥付 |
| `V13-ILL-034` | `PROMOTIONAL_AD` | `images/00037.jpeg` | 851x1202 | color | 62 | 奥付 |
| `V13-ILL-035` | `PROMOTIONAL_AD` | `images/00038.jpeg` | 895x1264 | color | 63 | 奥付 |
| `V13-ILL-036` | `PROMOTIONAL_AD` | `images/00039.jpeg` | 922x1302 | color | 64 | 奥付 |
| `V13-ILL-037` | `PROMOTIONAL_AD` | `images/00040.jpeg` | 907x1280 | color | 65 | 奥付 |
| `V13-ILL-038` | `PROMOTIONAL_AD` | `images/00041.jpeg` | 893x1262 | color | 66 | 奥付 |
| `V13-ILL-039` | `PROMOTIONAL_AD` | `images/00042.jpeg` | 1026x724 | color | 67 | 奥付 |
| `V13-ILL-040` | `PROMOTIONAL_AD` | `images/00043.jpeg` | 742x1048 | color | 68 | 奥付 |
| `V13-ILL-041` | `PROMOTIONAL_AD` | `images/00044.jpeg` | 704x994 | color | 69 | 奥付 |
| `V13-ILL-042` | `PROMOTIONAL_AD` | `images/00045.jpeg` | 1030x727 | color | 70 | 奥付 |
| `V13-ILL-043` | `PROMOTIONAL_AD` | `images/00046.jpeg` | 766x1082 | color | 71 | 奥付 |
| `V13-ILL-044` | `PROMOTIONAL_AD` | `images/00047.jpeg` | 703x993 | color | 72 | 奥付 |

### V14

| Visual ID | Role | Member | Size | Render | Spine | Anchor section |
|---|---|---|---:|---|---:|---|
| `V14-ILL-001` | `COVER` | `cover.jpeg` | 807x1154 | color | 0 |  |
| `V14-ILL-002` | `FRONT_TITLE_PAGE` | `images/00001.jpeg` | 971x1388 | color | 2 |  |
| `V14-ILL-003` | `FRONT_COLOR_ILLUSTRATION` | `images/00002.jpeg` | 1030x735 | color | 3 |  |
| `V14-ILL-004` | `FRONT_COLOR_ILLUSTRATION` | `images/00003.jpeg` | 1030x735 | color | 4 |  |
| `V14-ILL-005` | `FRONT_COLOR_ILLUSTRATION` | `images/00004.jpeg` | 1030x735 | color | 5 |  |
| `V14-ILL-006` | `FRONT_SERIES_MAP` | `images/00005.jpeg` | 971x1388 | color | 6 |  |
| `V14-ILL-007` | `FRONT_CHARACTER_PROFILE` | `images/00006.jpeg` | 971x1388 | monochrome | 8 |  |
| `V14-ILL-008` | `NARRATIVE_ILLUSTRATION` | `images/00008.jpeg` | 971x1388 | monochrome | 10 | ３年後 |
| `V14-ILL-009` | `NARRATIVE_ILLUSTRATION` | `images/00010.jpeg` | 971x1388 | monochrome | 12 | ３年後 |
| `V14-ILL-010` | `NARRATIVE_QA_PARATEXT` | `images/00011.jpeg` | 971x1388 | color | 13 | ３年後 |
| `V14-ILL-011` | `NARRATIVE_ILLUSTRATION` | `images/00012.jpeg` | 971x1388 | monochrome | 17 | 北へ。 |
| `V14-ILL-012` | `NARRATIVE_QA_PARATEXT` | `images/00014.jpeg` | 971x1388 | color | 19 | 北へ。 |
| `V14-ILL-013` | `NARRATIVE_ILLUSTRATION` | `images/00015.jpeg` | 971x1388 | monochrome | 21 | 吸血鬼爆誕 |
| `V14-ILL-014` | `NARRATIVE_ILLUSTRATION` | `images/00016.jpeg` | 971x1388 | monochrome | 23 | 仁義なき業界 |
| `V14-ILL-015` | `NARRATIVE_QA_PARATEXT` | `images/00017.jpeg` | 971x1388 | color | 25 | 仁義なき業界 |
| `V14-ILL-016` | `NARRATIVE_DOCUMENT` | `images/00018.jpeg` | 971x1388 | monochrome | 27 | ママ友とパパ友 |
| `V14-ILL-017` | `NARRATIVE_ILLUSTRATION` | `images/00019.jpeg` | 896x1281 | monochrome | 29 | パンツをかぶる日 |
| `V14-ILL-018` | `NARRATIVE_DOCUMENT` | `images/00020.jpeg` | 971x1388 | monochrome | 31 | パンツをかぶる日 |
| `V14-ILL-019` | `NARRATIVE_ILLUSTRATION` | `images/00022.jpeg` | 971x1388 | monochrome | 33 | シリウス |
| `V14-ILL-020` | `NARRATIVE_DOCUMENT` | `images/00023.jpeg` | 971x1388 | monochrome | 35 | シリウス |
| `V14-ILL-021` | `NARRATIVE_FORMAL_DEVICE` | `images/00024.jpeg` | 1030x735 | monochrome | 37 | 報いの虹 |
| `V14-ILL-022` | `NARRATIVE_ILLUSTRATION` | `images/00026.jpeg` | 971x1388 | monochrome | 41 | 青い小鳥たち |
| `V14-ILL-023` | `NARRATIVE_ILLUSTRATION` | `images/00028.jpeg` | 971x1388 | monochrome | 43 | 青い小鳥たち |
| `V14-ILL-024` | `AUTHOR_AFTERWORD_ART` | `images/00030.jpeg` | 971x1388 | monochrome | 47 | あとがき２ |
| `V14-ILL-025` | `PROMOTIONAL_AD` | `images/00031.jpeg` | 487x1388 | color | 50 | 奥付 |
| `V14-ILL-026` | `PROMOTIONAL_AD` | `images/00032.jpeg` | 487x1388 | color | 51 | 奥付 |
| `V14-ILL-027` | `PROMOTIONAL_AD` | `images/00033.jpeg` | 1030x726 | color | 52 | 奥付 |
| `V14-ILL-028` | `PROMOTIONAL_AD` | `images/00034.jpeg` | 914x1291 | color | 53 | 奥付 |
| `V14-ILL-029` | `PROMOTIONAL_AD` | `images/00035.jpeg` | 954x1347 | color | 54 | 奥付 |
| `V14-ILL-030` | `PROMOTIONAL_AD` | `images/00036.jpeg` | 1030x727 | color | 55 | 奥付 |
| `V14-ILL-031` | `PROMOTIONAL_AD` | `images/00037.jpeg` | 801x1131 | color | 56 | 奥付 |
| `V14-ILL-032` | `PROMOTIONAL_AD` | `images/00038.jpeg` | 797x1126 | color | 57 | 奥付 |
| `V14-ILL-033` | `PROMOTIONAL_AD` | `images/00039.jpeg` | 1030x726 | color | 58 | 奥付 |
| `V14-ILL-034` | `PROMOTIONAL_AD` | `images/00040.jpeg` | 748x1056 | color | 59 | 奥付 |
| `V14-ILL-035` | `PROMOTIONAL_AD` | `images/00041.jpeg` | 730x1031 | color | 60 | 奥付 |

## 8. Machine-readable companion and anchor fields

`machine_readable/illustration_paratext_index.jsonl` is the exhaustive per-asset authority surface. Each row includes:

- stable visual ID and locator;
- source member path and SHA-256;
- byte size and dimensions;
- color/monochrome estimate;
- role classification;
- first spine position and referring XHTML member(s);
- nearest TOC section;
- nearest preceding and following text-bearing spine members with short evidence excerpts;
- scene-context note;
- conservative character-tagging status;
- authority class and whether the asset can support narrative-event claims.

The prose excerpts are navigation aids only. Exact quotation must still resolve through the eventual paragraph-level locator index and original Japanese XHTML.

## 9. Evidence-use rules for later deep readings

1. A narrative illustration may support claims about **visual emphasis, licensed depiction, staging, costume, bodily relation, facial expression, erotic/comic/dramatic framing, and editorial salience**.
2. It does not automatically settle an ambiguity that the prose leaves open.
3. A Q&A/profile page should be cited as paratextual fact (`PF`) unless the prose independently establishes the same proposition.
4. Game/diagram pages may establish state/rules/layout directly when they are the publication’s explicit visual representation of those facts.
5. Mock advertisements or publishing documents embedded inside a narrative section remain narrative/paranarrative evidence; actual back-of-book publisher ads do not.
6. 10th-anniversary cover galleries are visual-history evidence, not continuity evidence.
7. Afterword project proposals are creator-process evidence, not discarded canon waiting to be imported into continuity.
8. Cover/color-plate eroticization or romantic framing must be distinguished from what the prose narrator says or what characters themselves perceive.
9. When a later deep reading identifies depicted characters with high confidence, add tags without changing the stable visual ID or source locator.

## 10. Phase-0 impact

This inventory completes the required **illustration/paratext inventory and image-to-spine anchoring** step. The remaining Phase-0 blockers are:

1. complete classification of every spine member by content type;
2. generation of the loss-aware normalized Japanese paragraph layer under `IMOSAE-NORM-SPEC-1.0`;
3. full typography/emphasis annotations;
4. stable paragraph-level locator generation (`locator_index.jsonl`);
5. all-volume round-trip extraction validation;
6. Phase-0 closure audit and issuance of `IMOSAE-JP-LN-NORM-1.0`.

**Canonical V01 deep reading remains gated until those steps pass.**
