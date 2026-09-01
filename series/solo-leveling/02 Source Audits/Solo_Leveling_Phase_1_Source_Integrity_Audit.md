---
title: Solo Leveling — Phase 1 Source Integrity Audit
date: '2026-08-11'
project: Solo Leveling definitive Korean novel–English manhwa synthesis
phase: 1
source_status_label: CBZ audit complete; Korean omnibus corpus-boundary audit revalidated from preserved raw-source audit; current-session EPUB remount pending
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Solo Leveling — Phase 1 Source Integrity Audit
## Korean novel and official English manhwa Volumes 1–15

## 1. Audit disposition

**Manhwa:** Phase 1 is complete for all fifteen supplied CBZs. Every archive is readable, every compressed member passes ZIP integrity testing, every page image decodes successfully, and the natural logical page sequence contains no gaps or duplicate page numbers.

Across the fifteen CBZs there are **4,479 image files representing 4,635 logical pages**. The difference—**156 logical pages**—comes from two-page spread images encoded as one JPEG (for example `p014-p015`). The archives total **1191.8 MiB**.

**Korean omnibus:** the preserved raw-source audit from the previous deep-reading workspace establishes a structurally healthy, complete Korean omnibus and provides the exact corpus boundaries needed for the synthesis. The `@` link supplied in the present chat has not remounted the raw EPUB into the current `/mnt/data` runtime, so this document distinguishes (a) facts already established by that prior raw-file audit from (b) a byte-level recheck that remains pending in this runtime. No Korean boundary is being reconstructed from memory or external sources.

## 2. Audit method

For each CBZ the audit:

- opened the file as a ZIP/CBZ archive and ran an archive-member integrity test;
- enumerated only decodable image resources;
- parsed the embedded `pNNN` / `pNNN-pNNN` logical-page identifiers;
- natural-sorted by logical page number rather than trusting ZIP member order;
- checked for missing and duplicate logical page numbers;
- decoded every image with Pillow verification;
- recorded SHA-256 file identity;
- recorded `cXXX` / `c040#N` filename segment boundaries;
- visually inspected frontmatter, title/part cards, end-of-story pages, transition pages, advertisements, creator notes, and credits.

The ZIP member order is **not** treated as reading order. Some files store `p000`/`p001` late in the raw archive member list. The `p` identifiers provide the stable reading sequence.

The `c` identifiers are preserved exactly as supplied. They are not silently renumbered as volume-local chapters: `c003`, for example, begins in Volume 1 and continues into Volume 2.

## 3. Manhwa volume audit summary

| Vol. | Image files | Logical pages | First → last logical page | Frontmatter | Chapter / part title cards | Story-bearing range | Transition / ending | Backmatter | Integrity |
|---:|---:|---:|---|---|---|---|---|---|---|
| 01 | 314 | 321 | p000 → p320 | p000–p006 | p007 (c000 / prologue), p015 (c001), p123 (c002), p253 (c003) | p008–p313, with chapter-title cards at the listed boundaries | p313 includes the volume-continuation marker on the final narrative page | p314–p320 | Clean |
| 02 | 295 | 305 | p000 → p304 | p000–p006 | No new title at p007: c003 resumes from Volume 1; p063 (c004), p135 (c005) | p007–p297 | p297 is the final narrative page and includes “TO BE CONTINUED IN VOLUME 3…” | p298–p304 | Clean |
| 03 | 310 | 321 | p000 → p320 | p000–p006 | p007 (c006), p135 (c007), p187 (c008) | p008–p313, with chapter-title cards at the listed boundaries | p313 is the final narrative page and includes the continuation marker | p314–p320 | Clean |
| 04 | 315 | 329 | p000 → p328 | p000–p006 | p007 (c009), p193 (c010) | p008–p320, with title cards at the listed boundaries | p321 is a separate “TO BE CONTINUED IN VOLUME 5…” transition page | p322–p328 | Clean |
| 05 | 307 | 321 | p000 → p320 | p000–p004 | p005 (c011), p075 (c012), p229 (c013) | p006–p314, with title cards at the listed boundaries | p315 is a separate “TO BE CONTINUED IN VOLUME 6…” transition page | p316–p320 | Clean |
| 06 | 299 | 309 | p000 → p308 | p000–p004 | p005 (c014), p061 (c015), p145 (c016), p233 (c017) | p006–p302, with title cards at the listed boundaries | p303 is a separate “TO BE CONTINUED IN VOLUME 7…” transition page | p304–p308 | Clean |
| 07 | 298 | 305 | p000 → p304 | p000–p004 | p005 (c018), p075 (c019), p185 (c020), p249 (c021) | p006–p301, with title cards at the listed boundaries | p301 is the final narrative page and includes “TO BE CONTINUED IN VOLUME 8…” | p302–p304 | Clean |
| 08 | 300 | 309 | p000 → p308 | p000–p004 | p005 (c022), p151 (c023), p243 (c024) | p006–p302, with title cards at the listed boundaries | p303 is a separate “TO BE CONTINUED IN VOLUME 9…” transition page | p304–p308 | Clean |
| 09 | 304 | 313 | p000 → p312 | p000–p006 | p007 (c025), p139 (c026), p225 (c027) | p008–p307, with title cards at the listed boundaries | p306–p307 is the final two-page spread and contains the continuation marker | p308–p312 | Clean |
| 10 | 292 | 305 | p000 → p304 | p000–p006 | p007 (c028), p099 (c029), p203 (c030) | p008–p297, with title cards at the listed boundaries | p297 is the final narrative page and includes “TO BE CONTINUED IN VOLUME 11…” | p298–p304 | Clean |
| 11 | 299 | 313 | p000 → p312 | p000–p006 | p007 (c031), p085 (c032), p187 (c033) | p008–p306, with title cards at the listed boundaries | p307 is a separate “TO BE CONTINUED IN VOLUME 12…” transition page | p308–p312 | Clean |
| 12 | 287 | 305 | p000 → p304 | p000–p004 | p005 (c034), p071 (c035), p223 (c036) | p006–p299, with title cards at the listed boundaries | p299 is the final narrative page and includes the continuation marker | p300–p304 | Clean |
| 13 | 283 | 295 | p000 → p294 | p000–p004 | p005 (c037), p059 (c038), p159 (c039), p229 (c040) | p006–p288, with title cards at the listed boundaries | p289 is a separate “TO BE CONTINUED IN VOLUME 14…” transition page | p290–p294 | Clean |
| 14 | 307 | 311 | p000 → p310 | p000–p004 | p005 (c040#1 / Part 1), p123 (c040#2 / Part 2), p217 (c040#3 / Part 3) | p006–p306, with part-title cards at the listed boundaries | p307 is a separate “TO BE CONTINUED IN VOLUME 15…” transition page | p308–p310 | Clean |
| 15 | 269 | 273 | p000 → p272 | p000–p004 | p005 (c040#4 / Part 4), p061 (c040#5 / Part 5), p143 (c040#6 / Part 6) | p006–p267, with part-title cards at the listed boundaries | p267 is the final narrative page (“…WHATEVER LIES BEYOND THIS DOOR.”); no further narrative page follows | p268–p272 | Clean |

### Interpretation of the ranges

- **Frontmatter** includes the retail cover and the collected-volume title/character/contents/logo apparatus visible before the first title card or resumed story page.
- **Story-bearing range** excludes frontmatter and excludes the later commercial/editorial backmatter. Title cards themselves are listed separately.
- **Transition** is separated where the volume contains a standalone `TO BE CONTINUED...` page. Where that wording is printed on the final story page, it remains part of the story-bearing endpoint.
- **Backmatter** includes volume previews, advertisements, creator/production notes where applicable, logos/blanks, and publication credits.

## 4. Archive segment and logical-page boundaries

### Volume 01

- **File:** `Solo Leveling v01 (2021) (Digital) (1r0n).cbz`
- **SHA-256:** `c7e7470774a10a3cc21db3a00c8fe8fcc08c423dca15b05e350fc4f8d7df2ea4`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c000 (v01) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c003 (v01) - p320 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c000`: p000–p014 (15 image files)
  - `c001`: p015–p122 (105 image files)
  - `c002`: p123–p252 (128 image files)
  - `c003`: p253–p320 (66 image files)

### Volume 02

- **File:** `Solo Leveling v02 (2021) (Digital) (1r0n).cbz`
- **SHA-256:** `b0bc242f37bcc130f89c57ade76b1885989fc6657e7c976e2adbeee9b6c00591`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c003 (v02) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c005 (v02) - p304 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c003`: p000–p062 (59 image files)
  - `c004`: p063–p134 (69 image files)
  - `c005`: p135–p304 (167 image files)

### Volume 03

- **File:** `Solo Leveling v03 (2021) (Digital) (1r0n).cbz`
- **SHA-256:** `98658c08b3ab266e9a6bf965aacd948863d47b59d2e8b00b8a155a733a6c323d`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c006 (v03) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c008 (v03) - p320 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c006`: p000–p134 (132 image files)
  - `c007`: p135–p186 (51 image files)
  - `c008`: p187–p320 (127 image files)

### Volume 04

- **File:** `Solo Leveling v04 (2022) (Digital) (1r0n).cbz`
- **SHA-256:** `08f89c9b910c5961c26f5ae4e442c0b8e5d031c43e2cbf828be0d4cb6c5c85a8`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c009 (v04) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c010 (v04) - p328 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c009`: p000–p192 (185 image files)
  - `c010`: p193–p328 (130 image files)

### Volume 05

- **File:** `Solo Leveling v05 (2022) (Digital) (1r0n).cbz`
- **SHA-256:** `2a92e12951194ab9b239f608f7a43346ed4999543dbd1ce915dc6b4df2ceb217`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c011 (v05) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c013 (v05) - p320 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c011`: p000–p074 (72 image files)
  - `c012`: p075–p228 (146 image files)
  - `c013`: p229–p320 (89 image files)

### Volume 06

- **File:** `Solo Leveling v06 (2023) (Digital) (1r0n).cbz`
- **SHA-256:** `841306cf2a76da5f9ae329f048468de6381bbf625d660cf986e3eb79e3573968`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c014 (v06) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c017 (v06) - p308 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c014`: p000–p060 (59 image files)
  - `c015`: p061–p144 (76 image files)
  - `c016`: p145–p232 (88 image files)
  - `c017`: p233–p308 (76 image files)

### Volume 07

- **File:** `Solo Leveling v07 (2023) (Digital) (1r0n).cbz`
- **SHA-256:** `fd1819199dcd959c58eb7c5aa0867b3385d59135590b8efdfe5e35c42dadb8f9`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c018 (v07) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c021 (v07) - p304 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c018`: p000–p074 (74 image files)
  - `c019`: p075–p184 (106 image files)
  - `c020`: p185–p248 (63 image files)
  - `c021`: p249–p304 (55 image files)

### Volume 08

- **File:** `Solo Leveling v08 (2024) (Digital) (1r0n).cbz`
- **SHA-256:** `bdb40870042cdc93b2a73e2becbd80210dc1b67de60a4bbe3fbbed62c6dade3e`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c022 (v08) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c024 (v08) - p308 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c022`: p000–p150 (147 image files)
  - `c023`: p151–p242 (88 image files)
  - `c024`: p243–p308 (65 image files)

### Volume 09

- **File:** `Solo Leveling v09 (2024) (Digital) (1r0n).cbz`
- **SHA-256:** `063a6710d32d14767960c32d131e16aef1570a3792da3cc5a84cd9472b447db1`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c025 (v09) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c027 (v09) - p312 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c025`: p000–p138 (136 image files)
  - `c026`: p139–p224 (83 image files)
  - `c027`: p225–p312 (85 image files)

### Volume 10

- **File:** `Solo Leveling v10 (2024) (Digital) (1r0n) (f).cbz`
- **SHA-256:** `3a236d07a65d3cf960d0aaebd7191ae646d55cec4c973cd116b228a710d787d3`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c028 (v10) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c030 (v10) - p304 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c028`: p000–p098 (95 image files)
  - `c029`: p099–p202 (100 image files)
  - `c030`: p203–p304 (97 image files)

### Volume 11

- **File:** `Solo Leveling v11 (2025) (Digital) (1r0n) (f).cbz`
- **SHA-256:** `777cd101790f7a6a3dc069cccc756d0a910f5c6a47381d093213443edeb2bd41`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c031 (v11) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c033 (v11) - p312 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c031`: p000–p084 (84 image files)
  - `c032`: p085–p186 (98 image files)
  - `c033`: p187–p312 (117 image files)

### Volume 12

- **File:** `Solo Leveling v12 (2025) (Digital) (1r0n).cbz`
- **SHA-256:** `e8cd77ae490ac38a3ee62958dae781b4b0b4a57229cc0913d167d3e1d6fc3dea`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c034 (v12) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c036 (v12) - p304 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c034`: p000–p070 (67 image files)
  - `c035`: p071–p222 (143 image files)
  - `c036`: p223–p304 (77 image files)

### Volume 13

- **File:** `Solo Leveling v13 (2025) (Digital) (1r0n).cbz`
- **SHA-256:** `b5de45c1ea765ba8b38103eace6cbb0b6e6819bef1f26929359cdc7e98ff0962`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c037 (v13) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c040 (v13) - p294 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c037`: p000–p058 (58 image files)
  - `c038`: p059–p158 (94 image files)
  - `c039`: p159–p228 (67 image files)
  - `c040`: p229–p294 (64 image files)

### Volume 14

- **File:** `Solo Leveling v14 - Side Stories 1 (2025) (Digital) (1r0n).cbz`
- **SHA-256:** `baa4d77f1558d0eae28dd3d9e1093652accb93f071e8e9a2a9d87f7109414976`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c040#1 (v14) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c040#3 (v14) - p310 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c040#1`: p000–p122 (120 image files)
  - `c040#2`: p123–p216 (93 image files)
  - `c040#3`: p217–p310 (94 image files)

### Volume 15

- **File:** `Solo Leveling v15 - Side Stories 2 (2026) (Digital) (1r0n).cbz`
- **SHA-256:** `86d88310f8fb28de50bf517bab05f4851bfebab524791f840dc035c77155d5c4`
- **Archive readability:** clean (`zipfile.testzip()` returned no bad member).
- **Image decode failures:** 0.
- **Missing logical pages:** 0.
- **Duplicate logical pages:** 0.
- **First natural file:** `Solo Leveling - c040#4 (v15) - p000 [Yen Press] [Digital] [1r0n].jpg`
- **Last natural file:** `Solo Leveling - c040#6 (v15) - p272 [Yen Press] [Digital] [1r0n].jpg`
- **Filename segment boundaries:**
  - `c040#4`: p000–p060 (61 image files)
  - `c040#5`: p061–p142 (81 image files)
  - `c040#6`: p143–p272 (127 image files)

## 5. Corpus-wide CBZ integrity findings

- **15/15 archives readable.**
- **0 corrupt ZIP members.**
- **0 image-decode failures.**
- **0 missing logical pages.**
- **0 duplicate logical pages.**
- **0 unparsed page-image filenames.**
- **4,479 JPEG page images.**
- **4,635 logical pages.**
- **156 additional logical pages represented through two-page spread images rather than separate image files.**

This is strong evidence that the supplied English manhwa corpus is complete at the collected-volume file level. It does **not**, by itself, prove that Yen Press reproduced every webtoon panel from the Korean serialization; that is an adaptation/publication question rather than a CBZ-integrity question.

## 6. Korean omnibus — preserved raw-source audit

The earlier raw-file audit established the following directly from the Korean EPUB:

- ZIP/EPUB archive integrity passed with no damaged compressed entries.
- 33 sequential HTML body files.
- approximately 5.3 MB uncompressed EPUB content.
- approximately 1.61 million extracted text characters and roughly 59,600 text segments.
- Korean metadata naming **추공 / Chugong** as author and **파피루스 / Papyrus** as publisher.
- approximately 1,465,800 characters of main story.
- approximately 131,500 characters of `외전` material.
- approximately 12,400 characters of `후일담` material.

### 6.1 Main-story endpoint

The main narrative ends **inside `index_split_030.html`** and is followed by the explicit completion marker:

`[나 혼자만 레벨업 完]`

The remainder of split 030 then begins the side-story corpus. This is the formal main-story endpoint preserved by the omnibus itself.

### 6.2 `외전 1–21`

The preserved audit confirms all twenty-one numbered side stories. Their distribution is:

- **split 030 remainder:** `외전` 1–4;
- **split 031:** `외전` 5–14;
- **split 032:** `외전` 15–21, followed by the postscript block.

The sequence recorded by the prior raw-source audit is:

1. `나는 헌터협회 직원입니다`
2. `재회 (1)`
3. `재회 (2)`
4. `귀환`
5. `이그리트의 기억`
6. `너의 일상은 (1)`
7. `너의 일상은 (2)`
8. `너의 일상은 (3)`
9. `너의 일상은 (4)`
10. `너의 일상은 (5)`
11. `너의 일상은 (6)`
12. `결심`
13. `어금니의 하루`
14. `나 혼자만 만렙`
15. `지금 만나러 갑니다 (1)`
16. `지금 만나러 갑니다 (2)`
17. `지금 만나러 갑니다 (3)`
18. **Untitled in this EPUB**
19. `최종화. 12년 후 (1)`
20. `최종화. 12년 후 (2)`
21. `최종화. 12년 후 (완)`

After Side Story 21, the omnibus explicitly closes this block with:

`[나 혼자만 레벨업, 외전 完]`

This should remain a hard analytical boundary. The following two pieces are **not** to be silently relabeled as `외전 22–23`.

### 6.3 `후일담 1–2` and final prose endpoint

After the explicit `외전` completion marker, the omnibus introduces:

`나 혼자만 레벨업 후일담`

with two pieces:

1. `베르의 기억`
2. `다시 만날 때까지`

`다시 만날 때까지` is the **final prose work in the audited omnibus**. No later narrative work was recorded after it in the prior raw-file audit. This establishes the corpus endpoint for the definitive synthesis.

**Current-session limitation:** because the raw EPUB itself is not presently remounted, the exact final sentence/paragraph bytes of `다시 만날 때까지` have not been rechecked in this runtime. The terminal-work identity and ordering are established by the preserved raw-source audit; publication-grade quotation of the final sentence remains pending remount.

### 6.4 Packaging warning

The omnibus is a flattened/aggregated EPUB. Its 33 `index_split_XXX.html` bodies are arbitrary digital chunks and often break in the middle of scenes. The navigation is essentially non-literary (`Start`), and the file does not preserve reliable original Korean print-volume divisions.

> **HTML split ≠ chapter ≠ Korean print volume.**

Therefore the definitive synthesis must not invent claims such as “Korean Volume 4 = chapters X–Y” from these split files. Later correspondence work should map **manhwa scene → Korean prose passage** directly, using the split file only as a stable search/locator layer.

## 7. Exact source-boundary policy to carry forward

For all later synthesis work:

1. Treat the Korean main story as ending at `[나 혼자만 레벨업 完]` inside split 030.
2. Treat the following material through `[나 혼자만 레벨업, 외전 完]` as the twenty-one-part `외전` corpus.
3. Treat `나 혼자만 레벨업 후일담` as a distinct postscript block containing exactly `베르의 기억` and `다시 만날 때까지`.
4. Treat `다시 만날 때까지` as the final prose work of the supplied Chugong omnibus.
5. Do not infer Korean print-volume boundaries from `index_split_XXX.html`.
6. Preserve the distinction between the Chugong prose endpoint and the later manhwa-original adolescent-Suho continuation present in Volume 15.

## 8. Phase 1 status

**CBZ/manhwa source integrity: COMPLETE.**

**Korean corpus-boundary integrity: REVALIDATED from the preserved raw-source audit and sufficient to freeze the synthesis source boundary.**

**Remaining technical closure item:** remount the raw Korean EPUB in the current runtime before Phase 2/3 begins exact Korean passage recovery, so publication-grade quotations, terminal-sentence verification, and new primary-source locators can be generated directly rather than through the preserved audit.

No evidence of corruption, page loss, accidental volume omission, or chapter-segment discontinuity was found in the fifteen manhwa CBZs.
