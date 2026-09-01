---
series: OREGAIRU
artifact_type: SOURCE_AUDIT
scope: ANTHOLOGY_02_ON_PARADE
generation: V2
status: canonical
source_boundary: 'Official Japanese Anthology 02: On Parade; scan-backed OCR-derived EPUB and supplied provenance/validation sidecars'
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# OREGAIRU Anthology 02 — OCR Source Admission Audit

## Decision

**ADMIT WITH QUALIFIED AUTHORITY.**

`Oregairu - Anthology 02 - On Parade [Japanese] [OCR Draft].epub` is satisfactory for inclusion in the Oregairu V2 source corpus as a **scan-backed provisional primary-source package**. It is not equivalent to the clean publisher-derived EPUB witnesses used for the mainline novels and Anthologies 01/03/04.

The governing authority rule is:

> **Embedded source-page image = textual authority. OCR text = navigation/search/discovery layer unless the cited wording has been visually verified against the embedded page image.**

Any exact Japanese quotation, lexical count used as a substantive claim, speaker-sensitive wording, punctuation-sensitive reading, or source locator entering a canonical analysis must therefore be checked against the page image. Unverified OCR may be used to locate likely passages, never as silent quotation-grade evidence.

## Source identity

- Japanese title: `やはり俺の青春ラブコメはまちがっている。アンソロジー 2 オンパレード`
- Publisher metadata: 小学館
- Publication date encoded in EPUB metadata: 2020-03-23
- ISBN encoded in EPUB metadata: 9784094518368
- EPUB status label: OCR draft
- EPUB SHA-256: `30d677be54a559cd9ebb50e4c611ed928ae77d1c0ae48069bcaab74bed1ee708`
- EPUB bytes: 32,908,355

## Structural/provenance validation

The supplied validation package reports:

- 306 source pages
- 296 book pages
- 10 jacket pages
- 306 EPUB page documents
- 306 embedded page images
- 306 corpus pages
- all 306 source hashes reconciled
- 309 XML documents parsed
- ZIP/XML/resource validation errors: **0**
- source mutation: **none**
- reading-order policy: clean cover -> complete book block -> supplementary jacket scans

Independent local validation also found no bad ZIP member.

This is sufficient to treat the EPUB as a faithful **container for the scanned source witness**, even where its OCR transcription is imperfect.

## OCR quality boundary

Supplied corpus totals:

- machine-readable characters: 132,874
- human-reviewed text pages: 15
- unreviewed machine-text pages: 267
- unresolved flagged lines: 2,977
- review-queue lines: 3,190

Direct sampling confirms the distinction is real. Human-reviewed prose pages are generally clean. Unreviewed pages can contain spurious Latin characters, broken punctuation, kana/kanji substitutions, and layout leakage. High page-level confidence therefore does **not** by itself authorize verbatim quotation.

### Allowed analytical uses

1. Search OCR to identify candidate passages, names, motifs, chronology markers, and lexical clusters.
2. Use the embedded page image to verify any passage that materially supports analysis.
3. Cite stable book-page / source-page locators after visual confirmation.
4. Use visual pages directly for illustrations, contents, colophon, paratext, and layout.
5. Record OCR uncertainty explicitly where visual verification remains ambiguous.

### Disallowed analytical shortcuts

- Do not quote unreviewed OCR as if it were publisher text.
- Do not use raw OCR counts as exact linguistic statistics without verification/cleaning.
- Do not let OCR corruption decide speaker attribution, wording-sensitive humor, register, or Japanese-language analysis.
- Do not treat machine-transcribed punctuation as authoritative.

## Contents and provenance segmentation

The source scan establishes the following story order:

1. `やはり千葉のハニトラ男はまちがっている。` — 白鳥士郎; illustration: しらび; begins p. 12.
2. `幕張の野望・全国版` — 伊達康; illustration: 紅緒; begins p. 68.
3. `思いのほか比企谷八幡の受験指導は的を射ている。` — 田中ロミオ; illustration: 戸部淑; begins p. 112.
4. `平塚静と比企谷八幡の、ある休日の過ごし方` — 天津向; illustration: うかみ; begins p. 158.
5. `ぼくのかんがえたけんぜんなはやはち` — 丸戸史明; begins p. 200.
6. `やはり妹さえいればいい。` — 渡航; begins p. 240.
7. `あとがき` — begins p. 290.

### Authority tiers

**Tier A — Watari-authored supplementary material**

- `やはり妹さえいればいい。` by 渡航.
- May be used as authorial supplementary evidence after a dedicated story-chronology audit.
- It does **not** automatically govern mainline state merely because Watari wrote it; publication context and internal chronology must first be established.

**Tier B — Official guest-author anthology material**

- Stories by 白鳥士郎, 伊達康, 田中ロミオ, 天津向, 丸戸史明.
- These are officially published Oregairu derivative/guest-author works.
- They may support reception, comparative characterization, intertextual interpretation, genre-play, and how other professional writers read the cast.
- They must **not** override Watari's mainline prose or be silently cited as canonical character fact.

**Tier C — Illustration and paratext witnesses**

- Guest illustrations, contents pages, profiles, jacket material, and other visual paratext.
- Useful as publication/paratext evidence; cannot override prose.

## Chronology state

**OPEN.** No constituent story is assigned a mainline chronology position by this admission audit alone.

Before a story updates a longitudinal character or relationship ledger, perform a story-level chronology pass using explicit temporal markers, school-year state, known events, relationship state, and publication context. If chronology remains underdetermined, retain the story as supplementary without forcing it into the sequential state model.

## Corpus integration rule

Anthology 02 is now part of the Oregairu V2 **supplementary source inventory**. It should be analyzed after the mainline sequential reread reaches an appropriate supplementary-analysis phase, or earlier only when a specific story materially bears on an active question and its chronology/authority has first been audited.

The original Japanese scan images embedded in the OCR EPUB govern exact textual verification. If a clean publisher EPUB becomes available later, it should supersede the OCR transcription layer for linguistic authority while this scan-backed package remains valuable as provenance and visual witness.
