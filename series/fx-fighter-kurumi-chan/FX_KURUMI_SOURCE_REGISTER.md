---
title: "FX Fighter Kurumi-chan — Source Register"
artifact_id: FX_KURUMI_SOURCE_REGISTER
artifact_type: source_register
series: fx-fighter-kurumi-chan
version: "1.1"
status: canonical
authority_generation: FX_KURUMI-INITIAL
authority_scope: "Bibliographic identity, witnessed reconnaissance and candidate corpus admission"
source_boundary: "Witnesses FXK-JP-V01-W01 to FXK-JP-V10-W01 verified for run FXK-RUN-20261119-V01-V10; each admitted only at its own frontier"
created: 2026-11-15
last_updated: 2026-11-21
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# FX Fighter Kurumi-chan — Source Register

## Identity and candidate range

KADOKAWA’s MF Comics Flapper releases identify **FX戦士くるみちゃん** with original story by Demunyan (でむにゃん) and manga by Tansan Daisuki (炭酸だいすき). The collected manga defines the candidate lane; publisher copy gives bibliographic context and the opening focus on a student and foreign-exchange trading. [KADOKAWA V01](https://www.kadokawa.co.jp/product/322104000251/), [KADOKAWA V10](https://www.kadokawa.co.jp/product/322605000254/).

| Candidate group | Ingest history | Admission |
| --- | --- | --- |
| Japanese manga V01–V09 | Nine existing EPUB candidates retained with standardized inventory names; exact editions pending | NONE |
| Japanese manga V10 | One Japanese publisher EPUB candidate added from the Calibre import | NONE |

The November 15 metadata reconciliation matched all ten numbered live candidates and their folder placement and file sizes to local layout receipts. The retained source audit and its ten-record manifest cover V01–V10, including V10. The audit reports a per-volume sample of visible Japanese pages, inspection of package, spine and resource structure, and distinct ordered image hashes. The November 15 import record for V10 reports ZIP CRC, container and mimetype checks, spine and resource parsing and SHA-256 match to the corresponding Calibre bytes. No full EPUBCheck run was reported. These are attributed preparation results; the reconciliation did not reread or rehash the live EPUBs. Sampled pages and distinct images do not establish verified reading order, legibility, missing-page status, or completeness of main and supplemental components. Only V10 has the new Calibre ingest lineage. The prior structural and sampled-page observations are attributed to that audit’s own boundary.

## Verify before admitting

Record edition, stable opaque witness, original and derived byte relationship and deterministic location binding in controlled storage. Check ordered spine/image positions, missing or duplicate occurrences, spreads and page labels. Classify covers, apparatus, main narrative, extras and previews before exposing analysts. Test the actual still-image inspection lane against both normal panels and dense inset figures. Source IDs, raw filenames, acquisition and mapping records, image bytes and OCR artifacts remain in the source or working plane. Report unreadable or unresolved numeric details separately from package integrity.

Web serial versions, other-language editions, adaptations and supplemental components have separate identity and scope. Any later comparison needs aligned loci and preserved variant evidence. An owner-authorized collected-manga run must give a start/terminal boundary and component scope even when more inventory exists. Approval of this foundation authorizes preparatory routing only.

## Run activation verification

On November 19, 2026, for run FXK-RUN-20261119-V01-V10, the run coordinator opened the ten supplied Japanese EPUBs in place and rehashed every package. The private witness receipt pins each package digest, its internal OPF path and the ordered map from spine item to image member. It also holds the package metadata, the source location and the per-image digests. The opaque public witness keys are `FXK-JP-V01-W01` to `FXK-JP-V10-W01`.

Every package passed a ZIP CRC test and resolved its container to one OPF. Each spine item is a fixed-layout page document that references exactly one raster image, and every image in each package is referenced from the spine. No image digest repeats within a volume. All 1,686 occurrences decoded as RGB rasters. Every OPF declares right-to-left page progression. The packages fall into two lineages. V01 and V03–V05 carry a Kindle-unpack tool signature, 1350×1920 pages and ASIN identifiers. V02 and V06–V10 have a different publisher-package layout with 1441×2048 pages and carry both creators (でむにゃん, 炭酸だいすき). The lineage difference does not affect page order. Each volume's checkpoint records whether it affects legibility or apparatus.

| Witness | Package title | Spine items = image occurrences | Page raster | Lineage |
| --- | --- | ---: | --- | --- |
| FXK-JP-V01-W01 | FX戦士くるみちゃん　1 | 171 | 1350×1920 | Kindle unpack |
| FXK-JP-V02-W01 | FX戦士くるみちゃん　2 | 171 | 1441×2048 | Publisher package |
| FXK-JP-V03-W01 | FX戦士くるみちゃん　3 | 171 | 1350×1920 | Kindle unpack |
| FXK-JP-V04-W01 | FX戦士くるみちゃん　4 | 163 | 1350×1920 | Kindle unpack |
| FXK-JP-V05-W01 | FX戦士くるみちゃん　5 | 171 | 1350×1920 | Kindle unpack |
| FXK-JP-V06-W01 | FX戦士くるみちゃん　6 | 163 | 1441×2048 | Publisher package |
| FXK-JP-V07-W01 | FX戦士くるみちゃん　7 | 163 | 1441×2048 | Publisher package |
| FXK-JP-V08-W01 | FX戦士くるみちゃん　８ | 171 | 1441×2048 | Publisher package |
| FXK-JP-V09-W01 | FX戦士くるみちゃん　9 | 171 | 1441×2048 | Publisher package |
| FXK-JP-V10-W01 | FX戦士くるみちゃん　10 | 171 | 1441×2048 | Publisher package |

**Locators.** `iNNNN` is the one-based image occurrence in spine order, including covers and apparatus. It is the same number as the spine position, because every spine item carries one image. Panel and balloon numbers are assigned by the analyst in Japanese reading order: right to left, then top to bottom. `p.visible` is recorded only where a printed folio is visible. A double-page spread is cited as both occurrences joined, `iNNNN+iNNNN`.

**Inspection lane.** The pages carry no text layer, so wording is transcribed directly from the images. A full-resolution V01 page with Japanese lettering and furigana and a 2.5× Lanczos-enlarged crop of small type were both legible in the coordinator's `STILL_IMAGE` route. Enlarged crops are the route for every dense screen, chart or small numeral. OCR, where used at all, is a retrieval aid and never a quotation source.

**Exposure control.** Images for V02–V10 were extracted and decoded only by script. They are held in a sealed working directory and released to analysts only when their volume is admitted. Beyond the V01 probe, no page of any volume was displayed during activation. Page classification, reading-order confirmation, spread detection and legibility for each volume belong to that volume's transaction.

| Obligation | State |
| --- | --- |
| FXK-SO-001 package identity and integrity | Resolved for all ten witnesses |
| FXK-SO-002 ordered image map and duplicate check | Resolved structurally for all ten; visual order confirmed per volume at admission |
| FXK-SO-003 component classification (main, apparatus, extras, previews) | Per volume, at admission, under the entrypoint's component scope |
| FXK-SO-004 legibility of dense screens and small numerals | Per volume; each unresolved value is recorded in that reading |
| FXK-SO-005 edition bibliography beyond package metadata (printing, revision state) | Open. Package metadata only; the V02 and V06–V10 packages carry no publication date |

## V01 coverage

Recorded by the V01 principal for run FXK-RUN-20261119-V01-V10 and accepted with the V01 transaction by the run coordinator on 2026-11-21. The [V01 deep reading](readings/FX_KURUMI_V01_DEEP_READING.md) holds the full receipt; the [V01 checkpoint](checkpoints/FX_KURUMI_V01_CHECKPOINT.md) records each role's coverage and every disposition.

- **Witness.** FXK-JP-V01-W01, package title 「FX戦士くるみちゃん　1」: 171 image occurrences at 1350×1920, right-to-left, Kindle-unpack lineage. The colophon (i0170) gives e-book ver.001, published 2021-07-21 by KADOKAWA, first serialized in 月刊コミックフラッパー 2021年3月号〜7月号. Colour occurrences: i0001, i0003–i0006, i0166, i0167, i0169.
- **Occurrences reviewed.** The principal opened every occurrence i0001–i0171 in spine order: the main narrative first, and the covers and apparatus only after the main-narrative exit freeze. Each of the two independent specialists also opened all 171 occurrences. The reviewer triaged every occurrence on contact sheets and opened the decisive pages at reading resolution or in crops.
- **Page order, folios and spreads.** The printed folio equals the occurrence number minus 2 throughout the p-NNN run (p.1 = i0003 to p.160 = i0162). Even occurrences are right-hand pages and odd ones left-hand pages, so openings are (even | odd); folio parity confirms this (p.8 = i0010 faces p.9 = i0011). Spreads with art across the gutter: i0004+i0005, i0012+i0013, i0076+i0077, i0160+i0161. No missing, duplicated or out-of-order page was found.

| Component | Occurrences | Notes |
| --- | --- | --- |
| Apparatus: front cover and flap | i0001, i0002 | Read after the main-narrative freeze; promotional, not diegetic |
| Main narrative | i0003–i0162 (160) | 第1話 i0003–i0050; 第2話 i0051–i0082; 第3話 i0083–i0110; 第4話 i0111–i0136; 第5話 i0137–i0162, ending "TO BE CONTINUED…". i0003 is a colour prologue page with the strip 「第1集 お祈り」; the 第1話 tab first appears on i0005, so whether i0003 belongs to 第1話 is unresolved |
| Apparatus: divider | i0163 | Logo page |
| Extra: artist's afterword strip | i0164 | Classified only; not narrative evidence |
| Apparatus: author's afterword | i0165 | Paratext |
| Apparatus: wraparound covers | i0166–i0167 | Publisher blurb; paratext |
| Extras: cover-underside strip and design notes | i0168–i0169 | Classified only; not narrative evidence |
| Apparatus: colophon | i0170 | Bibliographic |
| Advertising: vendor page | i0171 | Excluded |

Counts: main narrative 160, apparatus 7, extras 3, advertising 1. There is no next-volume preview and no blank occurrence.

- **Legibility and unresolved numerals.** All reading copies are legible. Dense screens and small numerals were checked in enlarged crops; the reading's receipt lists them. One value is unreadable by design: the glitched P/L tile at i0141, 「−3,[?]4[?],[4?]90」, which is not reconstructed. Lettering-level uncertainties (balloon attributions, wall-clock readings) are recorded in the reading. Discrepancies are kept as printed, not repaired: +24,000 vs +24,200 (i0049, i0050); a 95.410 diagram against a −105,000 box (i0084, i0083); a constant +10円 residual in every 300-lot P/L figure; 43.8 pips against +1,311,510 (rounded vs exact average); 330.4% against a computed 330.6% (i0098); an inverted phone-chart axis (i0062); and a flat account's ratio printed as 0% (i0067) but as *** (i0157).

| Obligation | V01 state |
| --- | --- |
| FXK-SO-002 ordered image map and duplicate check | Visual order confirmed for V01: every occurrence viewed in spine order, folio sequence continuous, no duplicates or gaps |
| FXK-SO-003 component classification | Completed for V01 as tabled above; extras and advertising classified by glance and not used as narrative evidence |
| FXK-SO-004 legibility of dense screens and small numerals | Completed for V01, with one value unreadable by design (i0141) recorded in the reading |

FXK-SO-001 and FXK-SO-005 are unchanged by V01.

## V02 coverage

Recorded by the V02 principal for run FXK-RUN-20261119-V01-V10 and accepted with the V02 transaction by the run coordinator on 2026-11-21. The [V02 deep reading](readings/FX_KURUMI_V02_DEEP_READING.md) holds the full receipt; the [V02 checkpoint](checkpoints/FX_KURUMI_V02_CHECKPOINT.md) records each role's coverage and every disposition.

- **Witness.** FXK-JP-V02-W01, the second collected volume of 「FX戦士くるみちゃん」 (原作 でむにゃん, 作画 炭酸だいすき): 171 image occurrences at 1441×2048, right-to-left, publisher-package lineage. The colophon (i0170) gives e-book ver.001, published 2022-01-21 by KADOKAWA (MFコミックス フラッパーシリーズ), first serialized in 月刊コミックフラッパー 2021年8月号・9月号、11月号・12月号、2022年1月号: five issues for the five chapters. Colour occurrences: i0001, i0003–i0006, i0166–i0169.
- **Occurrences reviewed.** The principal opened every occurrence i0001–i0171: the main narrative in spine order first, and the covers, flap, wraparound and under-jacket images only after the main-narrative exit freeze. Each of the two independent specialists also opened all 171 occurrences, in spine order. The reviewer triaged every occurrence on contact sheets and opened the decisive pages at reading resolution or in crops.
- **Page order, folios and spreads.** The printed folio equals the occurrence number minus 2 through the p-NNN run (p.1 = i0003 to p.163 = i0165; printed folios checked, for example "4" on i0006 and "159" on i0161). Even occurrences are right-hand pages and odd ones left-hand pages, so openings are (even | odd); the spine properties and art across the gutter confirm this. Spreads: i0004+i0005 (the title spread), i0128+i0129 (one sentence across the pair) and i0158+i0159 (the designed four-balance spread). No missing, duplicated or out-of-order page was found.

| Component | Occurrences | Notes |
| --- | --- | --- |
| Apparatus: front cover and flap | i0001, i0002 | Read after the main-narrative freeze; promotional, not diegetic |
| Main narrative | i0003–i0102, i0105–i0134, i0137–i0162 (156) | 第6話 i0003–i0040 (a colour opening i0003, "一週間後——", with the 第6話 box on i0005); 第7話 i0041–i0072; 第8話 i0073–i0102; 第9話 i0105–i0134; 第10話 i0137–i0162, ending "TO BE CONTINUED…". V02 has no "第N集" strip |
| Apparatus: separators | i0103–i0104, i0135–i0136, i0163 | Black grid pages with the series logo |
| Extra: author's afterword strip | i0164 | 「巻末のごあいさつ」; classified only; real-world paratext, not narrative evidence |
| Extra: candlestick tutorial | i0165 | 「巻末特典! 原作者によるローソク足講座!」; classified only |
| Apparatus: wraparound jacket | i0166–i0167 | Publisher blurb and a collage of V02 panels; paratext |
| Extras: under-jacket bonuses | i0168–i0169 | Mebuki design notes; the author's 2021 crypto strip; classified only; not narrative evidence |
| Apparatus: colophon | i0170 | Bibliographic |
| Advertising: vendor page | i0171 | Excluded |

Counts: main narrative 156, apparatus 10, extras 4, advertising 1. There is no next-volume preview and no blank occurrence.

- **Legibility and unresolved numerals.** All reading copies are legible. Every balance, trade and result box, chart axis and phone screen relied on was checked in enlarged crops; the reading's receipt lists them. Unreadable by design: the glitched recalled P/L digits of the 第9話 memory collage (i0105–i0106), of which i0106 shows only 「−3,[?][?]1,[?]90円」; they are not reconstructed. The i0073 wall lettering is unreadable and the i0162 abyss numerals are partial (「103.00」). Kept as printed, not repaired: the comma-for-decimal lettering of Mebuki's GBP/JPY rates (「170,897円」, 「170,702円」; i0070, i0087), which the box's own pips and yen settle as 170.897 → 170.702; the recalled tiles 「2,126,400」 and 「-1,265,300」 (i0133), which match no accepted V01 figure; and the unlabelled closing chart (axis 100.00–105.50, i0161), whose pair is not assigned.

| Obligation | V02 state |
| --- | --- |
| FXK-SO-002 ordered image map and duplicate check | Visual order confirmed for V02: every occurrence viewed in spine order, folio sequence continuous, no duplicates or gaps |
| FXK-SO-003 component classification | Completed for V02 as tabled above; extras and advertising classified by glance and not used as narrative evidence |
| FXK-SO-004 legibility of dense screens and small numerals | Completed for V02, with the glitched memory digits (i0105–i0106) unreadable by design and recorded in the reading |

FXK-SO-001 and FXK-SO-005 are unchanged by V02.
