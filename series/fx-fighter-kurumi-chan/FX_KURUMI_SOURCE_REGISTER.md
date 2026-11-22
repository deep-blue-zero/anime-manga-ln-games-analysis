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
last_updated: 2026-11-22
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
- **Occurrences reviewed.** The principal opened every occurrence i0001–i0171 in spine order: the main narrative first, and the covers and apparatus only after the main-narrative exit freeze. Each of the two independent specialists also opened all 171 occurrences. The reviewer triaged every occurrence on contact sheets and opened the decisive pages at reading resolution or in crops. The specialists opened the cover and flap first and the reviewer saw them on its first contact sheet; the [checkpoint errata](checkpoints/FX_KURUMI_CHECKPOINT_ERRATA.md#v01) record each role's first sight of them against its freezes.
- **Page order, folios and spreads.** The printed folio equals the occurrence number minus 2 throughout the p-NNN run (p.1 = i0003 to p.160 = i0162). Even occurrences are right-hand pages and odd ones left-hand pages, so openings are (even | odd); folio parity confirms this (p.8 = i0010 faces p.9 = i0011). Spreads with art across the gutter: i0004+i0005, i0012+i0013, i0076+i0077, i0160+i0161. No missing, duplicated or out-of-order page was found.

| Component | Occurrences | Notes |
| --- | --- | --- |
| Apparatus: front cover and flap | i0001, i0002 | Read by the principal after the main-narrative freeze, by the specialists and the reviewer first ([errata](checkpoints/FX_KURUMI_CHECKPOINT_ERRATA.md#v01)); promotional, not diegetic |
| Main narrative | i0003–i0162 (160) | 第1話 i0003–i0050; 第2話 i0051–i0082; 第3話 i0083–i0110; 第4話 i0111–i0136; 第5話 i0137–i0162, ending "TO BE CONTINUED…". i0003 is a colour prologue page with the strip 「第1集 お祈り」; the 第1話 tab first appears on i0005, so whether i0003 belongs to 第1話 is unresolved |
| Apparatus: divider | i0163 | Logo page |
| Extra: artist's afterword strip | i0164 | Classified only; not narrative evidence |
| Extra: story author's afterword | i0165 | 「原作者あとがき」; classified only; not narrative evidence. Reclassified from apparatus on 2026-11-22: the component scope classes afterwords as authorial extras ([errata](checkpoints/FX_KURUMI_CHECKPOINT_ERRATA.md#fxk-err-v01-03)) |
| Apparatus: wraparound covers | i0166–i0167 | Publisher blurb; paratext |
| Extras: cover-underside strip and design notes | i0168–i0169 | Classified only; not narrative evidence |
| Apparatus: colophon | i0170 | Bibliographic |
| Advertising: vendor page | i0171 | Excluded |

Counts: main narrative 160, apparatus 6, extras 4, advertising 1. There is no next-volume preview and no blank occurrence.

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
- **Occurrences reviewed.** The principal opened every occurrence i0001–i0171: the main narrative in spine order first, and the covers, flap, wraparound and under-jacket images only after the main-narrative exit freeze. Each of the two independent specialists also opened all 171 occurrences, in spine order. The reviewer triaged every occurrence on contact sheets and opened the decisive pages at reading resolution or in crops. The specialists opened the cover and flap first and the reviewer saw them on its first contact sheet; the [checkpoint errata](checkpoints/FX_KURUMI_CHECKPOINT_ERRATA.md#v02) record each role's first sight of them against its freezes and the two forecast rows whose credit the flap changes.
- **Page order, folios and spreads.** The printed folio equals the occurrence number minus 2 through the p-NNN run (p.1 = i0003 to p.163 = i0165; printed folios checked, for example "4" on i0006 and "159" on i0161). Even occurrences are right-hand pages and odd ones left-hand pages, so openings are (even | odd); the spine properties and art across the gutter confirm this. Spreads: i0004+i0005 (the title spread), i0128+i0129 (one sentence across the pair) and i0158+i0159 (the designed four-balance spread). No missing, duplicated or out-of-order page was found.

| Component | Occurrences | Notes |
| --- | --- | --- |
| Apparatus: front cover and flap | i0001, i0002 | Read by the principal after the main-narrative freeze, by the specialists and the reviewer first ([errata](checkpoints/FX_KURUMI_CHECKPOINT_ERRATA.md#v02)); promotional, not diegetic |
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

## V03 coverage

Recorded by the V03 principal for run FXK-RUN-20261119-V01-V10 and accepted with the V03 transaction by the run coordinator on 2026-11-21. The [V03 deep reading](readings/FX_KURUMI_V03_DEEP_READING.md) holds the full receipt; the [V03 checkpoint](checkpoints/FX_KURUMI_V03_CHECKPOINT.md) records each role's coverage and every disposition.

- **Witness.** FXK-JP-V03-W01, package title 「FX戦士くるみちゃん　3」: 171 image occurrences at 1350×1920, right-to-left, Kindle-unpack lineage. The colophon (i0170) gives e-book ver.001, published 2022-08-23 by KADOKAWA, first serialized in 月刊コミックフラッパー 2022年3月号〜2022年7月号: five issues for the five chapters. Colour occurrences: i0001, i0003–i0006, i0166–i0169 (i0168–i0169 two-colour).
- **Occurrences reviewed.** The principal opened every occurrence i0001–i0171: the main narrative in spine order first, the back apparatus after the main-narrative exit freeze, and the covers, flap, wraparound and under-jacket images only after that freeze. Each of the two independent specialists also opened all 171 occurrences, in spine order. The reviewer triaged every occurrence on contact sheets and opened the decisive pages at reading resolution or in crops. The specialists opened the cover and flap first and the reviewer saw them on its first contact sheet; the [checkpoint errata](checkpoints/FX_KURUMI_CHECKPOINT_ERRATA.md#v03) record each role's first sight of them against its freezes and a disposition for every forecast item.
- **Page order, folios and spreads.** The printed folio equals the occurrence number minus 2 through the p-NNN run (p.1 = i0003 to p.163 = i0165; printed folios checked, for example "23" on i0025, "81" on i0083, "145" on i0147 and "158" on i0160). Even occurrences are right-hand pages and odd ones left-hand pages, so openings are (even | odd); the spine properties and art across the gutter confirm this. Spreads: i0004+i0005 (the title spread) and i0154+i0155 (one chart running across the gutter, read left page to right page in time). No missing, duplicated or out-of-order page was found.

| Component | Occurrences | Notes |
| --- | --- | --- |
| Apparatus: front cover and flap | i0001, i0002 | Read by the principal after the main-narrative freeze; promotional, not diegetic |
| Main narrative | i0003–i0162 (160) | A colour cold open i0003 with the strip 「第3集 火柱」, grouped with 第11話; 第11話 i0004–i0038 (label on the title spread); 第12話 i0039–i0070; 第13話 i0071–i0102; 第14話 i0103–i0136; 第15話 i0137–i0162, ending "TO BE CONTINUED…". No separator page inside the main run |
| Apparatus: separator | i0163 | Black grid page with the series logo |
| Extra: bonus strip | i0164 | 「3巻記念! やす子ちゃん初めてのコミチア」; classified only; not narrative evidence |
| Extra: order-types tutorial | i0165 | 「巻末特典! FXの注文方法」; classified only; its remark on 第15話 is not used as evidence |
| Apparatus: wraparound jacket | i0166–i0167 | Publisher blurb and a collage of V03 panels; repeats the cover and flap; paratext |
| Extras: under-jacket bonuses | i0168–i0169 | Design notes on Mebuki's family; the author's 2008 stock anecdote; classified only; not narrative evidence |
| Apparatus: colophon | i0170 | Bibliographic |
| Advertising: vendor page | i0171 | Excluded |

Counts: main narrative 160, apparatus 6, extras 4, advertising 1. There is no next-volume preview and no blank occurrence.

- **Legibility and unresolved numerals.** All reading copies are legible. Every balance, trade and result box, P/L tile, chart axis and phone screen relied on was checked in enlarged crops; the reading's receipt lists them. Unreadable by design: the glitched negative figure on Mochiko's i0104 diagram (only 「−3,」 and 「…49」 visible), not reconstructed. Partly legible: the 18:30:09 and 18:30:11 figures of the i0037 second-by-second sequence (occluded or cut by the panel edge), not reconstructed; the leading digit of the top axis labels at i0162, hidden by a caption box (110.4–110.2 by the ladder); the dripping digits at i0038, read as 「−9,897円」 at MODERATE-HIGH. Kept as printed, not repaired: 「73.5%増」 against a computed 73.59% (i0092); the axis label 「169.6」 (i0123) and the spacing of 「105.05」 (i0130); the 100-yen residuals at i0137 and i0158, consistent with an unprinted average of 106.6325; Mochiko's average 「106.832円」 (i0148) against 「106.382円」 (i0154), the two late-October tiles favouring 106.832; 「平均買値」 printed on Mebuki's short (i0155); both 「¥」 and 「円」 on one tile (i0144); 「約17倍」 against a computed 17.9 (i0007). No broker stop-out level or margin-maintenance threshold is printed; a domestic maximum of 25× is printed once (i0007).

| Obligation | V03 state |
| --- | --- |
| FXK-SO-002 ordered image map and duplicate check | Visual order confirmed for V03: every occurrence viewed in spine order, folio sequence continuous, no duplicates or gaps |
| FXK-SO-003 component classification | Completed for V03 as tabled above; extras and advertising classified by glance and not used as narrative evidence |
| FXK-SO-004 legibility of dense screens and small numerals | Completed for V03, with the glitched i0104 figure unreadable by design and the partial i0037 and i0162 figures recorded in the reading |

FXK-SO-001 and FXK-SO-005 are unchanged by V03; the V03 package metadata and colophon both give the date 2022-08-23.

## V04 coverage

Recorded by the V04 principal for run FXK-RUN-20261119-V01-V10 and accepted with the V04 transaction by the run coordinator on 2026-11-21. The [V04 deep reading](readings/FX_KURUMI_V04_DEEP_READING.md) holds the full receipt; the [V04 checkpoint](checkpoints/FX_KURUMI_V04_CHECKPOINT.md) records each role's coverage and every disposition.

- **Witness.** FXK-JP-V04-W01, package title 「FX戦士くるみちゃん　4」: 163 image occurrences at 1350×1920, right-to-left, Kindle-unpack lineage; every image is referenced from the spine and no image is duplicated. The colophon (i0162) gives e-book ver.001, published 2023-02-22 by KADOKAWA, first serialized in 月刊コミックフラッパー 2022年9月号〜12月号、2023年1月号: five issues for the five chapters. Colour occurrences: i0001, i0003–i0006, i0158–i0161.
- **Occurrences reviewed.** The principal opened every occurrence i0001–i0163: the main narrative in spine order first, and the separator after it, the extra, the covers, flap, wraparound, under-jacket images, colophon and vendor page only after the main-narrative exit freeze. Each of the two independent specialists also opened all 163 occurrences, in spine order. The reviewer triaged every occurrence on contact sheets and opened the decisive pages at reading resolution or in crops. The specialists opened the cover and flap first and the reviewer saw them on its first contact sheet; the [checkpoint errata](checkpoints/FX_KURUMI_CHECKPOINT_ERRATA.md#v04) record each role's first sight of them against its freezes.
- **Page order, folios and spreads.** The printed folio equals the occurrence number minus 2 through the p-NNN run (p.1 = i0003 to p.155 = i0157; printed folios checked, for example "4" on i0006, "29" on i0031, "60" on i0062, "85" on i0087, "124" on i0126 and "136" on i0138); separator pages carry no folio but are counted. Even occurrences are right-hand pages and odd ones left-hand pages, so openings are (even | odd); the separator logos (bottom-left on odd pages, bottom-right on even ones) and the folio positions confirm this. The only spread with art across the gutter is the colour title spread i0004+i0005. No missing, duplicated or out-of-order page was found.

| Component | Occurrences | Notes |
| --- | --- | --- |
| Apparatus: front cover and flap | i0001, i0002 | Read by the principal after the main-narrative freeze; promotional, not diegetic |
| Main narrative | i0003–i0032, i0035–i0062, i0065–i0088, i0091–i0122, i0125–i0150 (140) | A colour cold open i0003 with the strip 「第4集 博打」, grouped with 第16話; 第16話 i0004–i0032 (label on the title spread); 第17話 i0035–i0062; 第18話 i0065–i0088; 第19話 i0091–i0122; 第20話 i0125–i0150, ending "TO BE CONTINUED…" |
| Apparatus: separators inside the main run | i0033–i0034, i0063–i0064, i0089–i0090, i0123–i0124 | Black grid pages with the series logo, one pair between each two chapters |
| Apparatus: separator | i0151 | A single separator page before the extra |
| Extra: bonus strips | i0152–i0157 | 「巻末特典! やす子ちゃん誕生裏話!」: the writer's and the artist's production diaries and a cosplay gag page (i0155); classified only; not narrative evidence |
| Apparatus: wraparound jacket | i0158–i0159 | Publisher blurb and a collage of V04 panels; repeats the cover and flap; paratext |
| Apparatus: under-jacket boards | i0160–i0161 | Creators' notes and the writer's investing gag; paratext |
| Apparatus: colophon | i0162 | Bibliographic |
| Advertising: vendor page | i0163 | Excluded |

Counts: main narrative 140, apparatus 16 (nine separators, the cover, flap, wraparound, under-jacket boards and colophon), extras 6, advertising 1. There is no next-volume preview and no blank occurrence.

- **Legibility and unresolved numerals.** All reading copies are legible. Every balance, trade and result box, P/L tile, chart axis, phone screen and document relied on was checked in enlarged crops; the reading's receipt lists them. Partly legible: the day of the IOU dated 「2014年11[…]」 (i0145), cut by the panel edge, not reconstructed; the third digit of the carriage-ad quip 「たぶん152円までいくね、これは」 (i0137), read as 2 at MODERATE-HIGH (an authorial in-joke, not a story price); a few occluded glyphs in the cold-open newspaper (i0003). Kept as printed, not repaired: Mochiko's open P/L 「+4,729,000円」 at 「115.840円」 (i0144), exact for an average of 106.382 although 「+3,209,000」 (i0037) fits 106.832, against the accepted V03 average; the comma in the axis label 「112,2」 (i0022); the elided 「÷365」 in the interest diagram (i0100); the name field 「YAMASHO I」 against the card's 「YAMASHI MEBUKI」 (i0019). No broker stop-out level or margin-maintenance threshold is printed; a forced liquidation is printed as an event (「強制ロスカット」, i0012). No Mebuki position or P/L is printed after i0068.

| Obligation | V04 state |
| --- | --- |
| FXK-SO-002 ordered image map and duplicate check | Visual order confirmed for V04: every occurrence viewed in spine order, folio sequence continuous, no duplicates or gaps |
| FXK-SO-003 component classification | Completed for V04 as tabled above; extras and advertising classified by glance and not used as narrative evidence |
| FXK-SO-004 legibility of dense screens and small numerals | Completed for V04, with the IOU's day and the ad digit recorded as partly legible in the reading |

FXK-SO-001 and FXK-SO-005 are unchanged by V04; the V04 package metadata gives 2023-02-21 and the colophon 2023-02-22.

## V05 coverage

Recorded by the V05 principal for run FXK-RUN-20261119-V01-V10 and accepted with the V05 transaction by the run coordinator on 2026-11-22. The [V05 deep reading](readings/FX_KURUMI_V05_DEEP_READING.md) holds the full receipt; the [V05 checkpoint](checkpoints/FX_KURUMI_V05_CHECKPOINT.md) records each role's coverage and every disposition.

- **Witness.** FXK-JP-V05-W01, package title 「FX戦士くるみちゃん　5」: 171 image occurrences at 1350×1920, right-to-left; every occurrence was viewed once and logged once, with no gap or duplicate. The colophon (i0170) gives e-book ver.001, published 2023-07-22 by KADOKAWA, first serialized in 月刊コミックフラッパー 2023年3月号〜5月号、7月号・8月号: five issues for the five chapters. Colour occurrences: i0001, i0003–i0006, i0166–i0169.
- **Occurrences reviewed.** The principal opened every occurrence i0001–i0171: the main narrative in spine order first, and the back-matter separator, afterword, bonus explainer, colophon, covers, flap, wraparound, under-jacket images and vendor page only after the main-narrative exit freeze. Each of the two independent specialists also opened all 171 occurrences, in spine order. The reviewer triaged every occurrence on contact sheets and opened the decisive pages at reading resolution or in crops. The specialists opened the cover and flap first and the jacket images at the end; the reviewer saw all of them on its Stage 1 contact sheets. The [V05 checkpoint](checkpoints/FX_KURUMI_V05_CHECKPOINT.md#7-exposure-and-contamination-record) records each role's first sight of them against its freezes and judgments.
- **Page order, folios and spreads.** The printed folio equals the occurrence number minus 2 through the p-NNN run (p.1 = i0003 to p.160 = i0162; printed folios checked, for example "9" on i0011, "57" on i0059, "61" on i0063, "107" on i0109, "138" on i0140 and "151" on i0153); separator pages carry no folio but are counted. Even occurrences are right-hand pages and odd ones left-hand pages, so openings are (even | odd), as the package's spine-spread properties state; the separator logos (bottom-left on i0055 and i0163, bottom-right on i0056) agree. No drawn double-page spread was relied on; whether the colour pages i0004+i0005 form a title spread is left unresolved. No missing, duplicated or out-of-order page was found.

| Component | Occurrences | Notes |
| --- | --- | --- |
| Apparatus: front cover and flap | i0001, i0002 | Read by the principal after the main-narrative freeze, by the specialists and the reviewer first ([V05 checkpoint](checkpoints/FX_KURUMI_V05_CHECKPOINT.md#7-exposure-and-contamination-record)); promotional, not diegetic |
| Main narrative | i0003–i0054, i0057–i0162 (158) | A colour cold open i0003 with the strip 「第5集 糸」, grouped with 第21話; 第21話 i0004–i0054 (label on the colour title page i0005; Mochiko's past 2006–2014, then the present); 第22話 i0057–i0082; 第23話 i0083–i0102; i0103–i0104 (the dated コミチア scene opens before the 第24話 label, which stands on i0105) attributed to 第23話 or to a cold open of 第24話, unresolved; 第24話 i0105–i0140; 第25話 i0141–i0162, ending "TO BE CONTINUED..." |
| Apparatus: separators inside the main run | i0055–i0056 | Black grid pages with the series logo, the only pair, between 第21話 and 第22話 |
| Apparatus: separator | i0163 | Logo page before the back matter |
| Extra: afterword strip | i0164 | 「5巻 あとがき」; classified only; not narrative evidence |
| Extra: bonus explainer | i0165 | 「巻末特典! FX戦士くるみちゃんの嘘!」: short-term charts altered for drama; printed P/L excludes swap; used only as method paratext, not as narrative evidence |
| Apparatus: wraparound jacket | i0166–i0167 | Publisher blurb and a collage of V05 panels; repeats the cover and flap; paratext |
| Apparatus and extra: under-jacket boards | i0168–i0169 | The authors' note 「BL課長について」 and an investing gag; paratext, not used as story evidence |
| Apparatus: colophon | i0170 | Bibliographic |
| Advertising: vendor page | i0171 | Excluded |

Counts: main narrative 158, apparatus 9 (three separators, the cover, flap, wraparound pair, the under-jacket back board and the colophon), extras 3 (i0164, i0165, i0169), advertising 1. There is no next-volume preview and no blank occurrence.

- **Legibility and unresolved numerals.** All reading copies are legible. Every balance, trade and result box, P/L tile, chart axis, order box and document relied on was checked in enlarged crops or recorded as read at reading size; the reading's receipt lists them. Partly legible, not reconstructed: small memory-collage fragments at i0074–i0075 and i0153; small background asides at i0124 and i0126; the SNS post text and hashtag digit at i0105; the shaggy sound glyphs at i0162; the first word of a memory-inset line at i0070. Kept as printed, not repaired: the balloon 「救い玉1枚 利益確定!」 against a Before/After tile that reconciles only with all ten rescue lots closed (i0085); the comma in 「112,102円」 (i0067); the button 「建玉全決算」 (i0073); 「ちょくっと」 (i0136); the boot text 「Press Tab to Seitch Screen」 (i0156); the caption 「2014年 10月下旬」 for the FOMC move into the 118s, which the volume's own 17–19 November rates and 「その後10日ほど」 before 「12月2日 火曜日」 contradict (i0141); two different definitions of 「パターンA」 (i0077, i0078). No broker stop-out level or margin-maintenance threshold is printed. No Mebuki position or P/L is printed after i0091; no Mochiko balance or position figure is printed in V05; Kurumi's 300-lot short has no figure after its entry (i0158).

| Obligation | V05 state |
| --- | --- |
| FXK-SO-002 ordered image map and duplicate check | Visual order confirmed for V05: every occurrence viewed in spine order, folio sequence continuous, no duplicates or gaps |
| FXK-SO-003 component classification | Completed for V05 as tabled above, with the chapter attribution of i0103–i0104 left unresolved; extras and advertising classified by glance and not used as narrative evidence |
| FXK-SO-004 legibility of dense screens and small numerals | Completed for V05; the partly legible items above are recorded in the reading and none is reconstructed |

FXK-SO-001 and FXK-SO-005 are unchanged by V05; the V05 package metadata and the colophon both give 2023-07-22.

## V06 coverage

Recorded by the V06 principal for run FXK-RUN-20261119-V01-V10 and accepted with the V06 transaction by the run coordinator on 2026-11-22. The [V06 deep reading](readings/FX_KURUMI_V06_DEEP_READING.md) holds the full receipt; the [V06 checkpoint](checkpoints/FX_KURUMI_V06_CHECKPOINT.md) records each role's coverage and every disposition.

- **Witness.** FXK-JP-V06-W01, package title 「FX戦士くるみちゃん　6」: 163 image occurrences at 1441×2048, right-to-left; every occurrence was viewed once and logged once by the principal, with no gap or duplicate (verified by script). The colophon (i0162) gives e-book ver.001, published 2024-03-23 by KADOKAWA, first serialized in 月刊コミックフラッパー 2023年9月号〜12月号、2024年1月号: five issues for the five chapters. Colour occurrences: i0001, i0003–i0006, i0159 (the reviewer and the character specialist both report that a full-resolution crop of i0158 shows pink accents although the colour list omits it; not checked by the principal).
- **Occurrences reviewed.** The principal opened every occurrence i0001–i0163: the main narrative in spine order first, then the separator i0155 and the afterword i0156 (opened before the main-exit freeze to establish the end, disclosed), the author's strip, colophon and vendor page, and the deferred cover, flap, wraparound and under-jacket images (i0001, i0002, i0158–i0161) only after the main-exit freeze. From V06 the entrypoint's component scope deferred those six occurrences for every role: each specialist opened all 163 occurrences in spine order and the deferred six only at its own release point; the reviewer triaged every occurrence on contact sheets, opened the decisive pages at reading resolution or in crops, and opened the deferred sheets only after its Stage 1 write-up. The [V06 checkpoint](checkpoints/FX_KURUMI_V06_CHECKPOINT.md) records each role's first sight of them against its freezes and judgments.
- **Page order, folios and spreads.** The printed folio equals the occurrence number minus 2 through the p-NNN run (p.1 = i0003 to p.155 = i0157; printed folios checked, for example "13" on i0015, "25" on i0027 and "31" on i0033); separator pages carry no folio but are counted. Even occurrences are right-hand pages and odd ones left-hand pages, so openings are (even | odd), as the package's spine-spread properties state. No V06 story image crosses the gutter; several openings are composed as pairs (i0022|i0023, i0088|i0089, i0108|i0109) and none was relied on as a drawn spread. No missing, duplicated or out-of-order page was found.

| Component | Occurrences | Notes |
| --- | --- | --- |
| Apparatus: front cover and flap | i0001, i0002 | Deferred for every role; opened by the principal after the main-exit freeze; promotional, not diegetic |
| Main narrative | i0003–i0028, i0031–i0055, i0057–i0090, i0093–i0118, i0121–i0154 (145) | A colour opening with the strip 「第6集 必勝」 (i0003) and the colour title page (i0004), grouped with 第26話 (label on i0005); 第26話 i0003–i0028; 第27話 i0031–i0055; 第28話 i0057–i0090 (flashback 1998–2008, present-time close i0090); 第29話 i0093–i0118; 第30話 i0121–i0154, ending 「TO BE CONTINUED...」 |
| Apparatus: separators inside the main run | i0029–i0030, i0056, i0091–i0092, i0119–i0120 | Black grid pages with the series logo between the chapters |
| Apparatus: separator | i0155 | Logo page before the back matter |
| Extra: afterword gag page | i0156 | 「6巻あとがき」; classified only; not narrative evidence |
| Extra: author's strip | i0157 | 「でむにゃんの「遅筆」が深刻なようです。〜サボリ編〜」; classified only |
| Apparatus: wraparound jacket | i0158–i0159 | Deferred; publisher blurb and a collage of V06 panels (i0158); colour cover, spine and flap (i0159); paratext; the blurb's framing of Mebuki's work is not adopted |
| Extra: under-jacket boards | i0160–i0161 | Deferred; the creators' note 「負け演出こぼれ話」 and an author strip dated 「2020年 某月某日」; paratext, not used as story evidence |
| Apparatus: colophon | i0162 | Bibliographic |
| Advertising: vendor page | i0163 | Excluded |

Counts: main narrative 145, apparatus 13 (eight separator pages, the cover, flap, the wraparound pair and the colophon), extras 4 (i0156, i0157, i0160, i0161), advertising 1. There is no next-volume preview and no blank occurrence.

- **Legibility and unresolved numerals.** All reading copies are legible. Every balance, trade and result box, P/L tile, rate board, phone screen, passbook column and dated caption relied on was checked in enlarged crops or recorded as read at reading size; the reading's receipt lists them, and a reconciliation crop settled the mark before the new contest rule on i0143 as a double circle ◎, not a numeral. Partly legible, not reconstructed: the final digit(s) of Kozue's 「当日決済損益 −18,790,50[…]」, hidden by the panel edge (i0079); the hidden text after 「ごほうび!: 負」 (i0143); the ruby read as ウィッチングアワー [?] (i0129); digits under balloons on the rate board (i0049); the leading digits of the top passbook rows (i0075); the phone digits on the front cover (i0001). Kept as printed, not repaired: Mebuki's liquidation box, whose printed loss −2,610,530 leaves 11,000 of her prior 2,621,530 unexplained against a 0円 balance (i0039); the chart axis label 「115.5」 in a 0.5 sequence (i0046); the text 「1ユーロ 1・12ドル」 against the graphic 「€1.22」 and the board's EUR/USD 1.22867 (i0105, i0049); 「1ユーロ=1.20フランを上限とする」 (i0113); the knight's 「スイス政府」 against the narrator's 「スイス国立銀行」 (i0127); the rule example 「180万」 where 80% would be expected (i0144); Kurumi's year curve starting at 「30万」 in 「5月」 (i0048); Kozue's "ここ1年 100円と90円の間" against her own journal's "103円突破" (i0070, i0068); irregular schematic chart axes in the flashback (i0070, i0072, i0084, i0086). No broker stop-out level or margin-maintenance threshold is printed. No entry date, rate, fill, margin or P/L is printed for Kurumi's EUR/CHF position, which is attested only by her own words on 25 December (i0148).

| Obligation | V06 state |
| --- | --- |
| FXK-SO-002 ordered image map and duplicate check | Visual order confirmed for V06: every occurrence viewed in spine order, folio sequence continuous, no duplicates or gaps |
| FXK-SO-003 component classification | Completed for V06 as tabled above; the six cover and jacket occurrences were deferred for every role and classified after the main narrative; extras and advertising classified by glance and not used as narrative evidence |
| FXK-SO-004 legibility of dense screens and small numerals | Completed for V06; the partly legible items above are recorded in the reading and none is reconstructed |

FXK-SO-001 and FXK-SO-005 are unchanged by V06; the V06 package metadata and the colophon both give 2024-03-23.

## V07 coverage

Recorded by the V07 principal for run FXK-RUN-20261119-V01-V10 and accepted with the V07 transaction by the run coordinator on 2026-11-22. The [V07 deep reading](readings/FX_KURUMI_V07_DEEP_READING.md) holds the full receipt; the [V07 checkpoint](checkpoints/FX_KURUMI_V07_CHECKPOINT.md) records each role's coverage and every disposition.

- **Witness.** FXK-JP-V07-W01, package title 「FX戦士くるみちゃん　7」: 163 image occurrences at 1441×2048, right-to-left (publisher-package lineage, like V02 and V06); every occurrence was viewed once and logged once by the principal, with no gap or duplicate (verified by script). The colophon (i0162) gives e-book ver.001, published 2024-09-21 by KADOKAWA, first serialized in 月刊コミックフラッパー 2024年3月号〜2024年7月号: five issues for the five chapters. Colour occurrences: i0001, i0003–i0006, i0158–i0161.
- **Occurrences reviewed.** The principal opened every occurrence i0001–i0163: the main narrative in spine order first; after the main-exit freeze the separators i0151–i0152, the afterword i0153, the author's bonus essay i0154–i0157, the colophon and the vendor page; and the deferred cover, flap, wraparound and under-jacket images (i0001, i0002, i0158–i0161) last. The entrypoint's component scope deferred those six occurrences for every role: each specialist opened all 163 occurrences in spine order and the deferred six only at its own release point; the reviewer triaged every occurrence on contact sheets, opened the decisive pages at reading resolution or in crops, and opened the deferred sheets only after its Stage 1 write-up. The [V07 checkpoint](checkpoints/FX_KURUMI_V07_CHECKPOINT.md) records each role's first sight of them against its freezes and judgments.
- **Page order, folios and spreads.** The printed folio equals the occurrence number minus 2 through the p-NNN run (p.1 = i0003 to p.155 = i0157; printed folios checked at i0032 「30」, i0066 「64」, i0069 「67」, i0122 「120」 and i0125 「123」); separator pages carry no folio but are counted. Even occurrences are right-hand pages and odd ones left-hand pages, so openings are (even | odd), as the package's spine-spread properties state. One drawn spread crosses the gutter: the chart of i0102+i0103, whose printed time axis runs 「:45」 「18:00」 on i0103 and 「18:15」 「18:30」 on i0102; the falling candle of i0084 continues on the facing i0085. The label 「第31話」 is on an even page (i0004, the second colour page); 第32話–第35話 are labelled on odd pages facing a separator. No missing, duplicated or out-of-order page was found.

| Component | Occurrences | Notes |
| --- | --- | --- |
| Apparatus: front cover and flap | i0001, i0002 | Deferred for every role; opened by the principal after the main-exit freeze; promotional, not diegetic |
| Main narrative | i0003–i0032, i0035–i0066, i0069–i0095, i0097–i0122, i0125–i0150 (141) | A colour opening with the strip 「第7集 1月15日」 (i0003), grouped with 第31話 (label on i0004); 第31話 i0003–i0032 (30 pages); 第32話 i0035–i0066 (32); 第33話 i0069–i0095 (27); 第34話 i0097–i0122 (26); 第35話 i0125–i0150 (26), ending 「TO BE CONTINUED...」 |
| Apparatus: separators inside the main run | i0033–i0034, i0067–i0068, i0096, i0123–i0124 | Black grid pages with the series logo between the chapters (a single page after 第33話) |
| Apparatus: separators after the main run | i0151–i0152 | Logo pages before the back matter |
| Extra: afterword | i0153 | 「7巻あとがき」; classified only; not narrative evidence; its "20分…41%" and 150円 → 90円 analogy differ from the narrative's "わずか数分で約30%" (i0114) and are kept as paratext variance |
| Extra: author's bonus essay | i0154–i0157 | 「巻末特典!「スイスのアレ」裏話…!」 (the writer on planning the 第33話 chart pages); classified only |
| Apparatus: wraparound jacket | i0158–i0159 | Deferred; publisher blurb and a collage of V07 panels (i0158); colour cover, spine and flap (i0159); paratext, the blurb's ironic "ぜったい負けないに決まってるんだ!" not used as Kurumi's speech |
| Apparatus: under-jacket boards | i0160–i0161 | Deferred; the artist's three-extra-pages essay and the writer's IPO strip; paratext, not used as story evidence |
| Apparatus: colophon | i0162 | Bibliographic |
| Advertising: vendor page | i0163 | Excluded |

Counts: main narrative 141, apparatus 16 (nine separator pages, the cover, flap, the wraparound pair, the two under-jacket boards and the colophon), extras 5 (i0153–i0157), advertising 1. There is no next-volume preview and no blank occurrence.

- **Legibility and unresolved numerals.** All reading copies are legible. Every contest box, balance box, chart label, account and bank screen, e-mail and dated caption relied on was checked in enlarged crops or recorded as read at reading size because it is lettered large (the eight pages of fall labels i0087–i0094, Mochiko's estimate boxes i0115, the e-mail i0130, the bank screen i0144, the doubling ladder i0148); the reading's receipt lists them, and a reconciliation crop settled 「経済至上主義」 on i0138. Partly legible, not reconstructed: the contest sheet's reward line (「ごほうび!: 負けた[…]」, i0022; 「[…]けた人がご飯を[…]ごる」, i0021); the upper chart label 1.2[..]90 (i0081); one overdrawn digit of 「口座残高 -101,534,6[4]4円」 and the second digit of 「1.1[6?]880」 (i0125); the middle kana of 「まあ い[っ?]か…」, measured on an enlargement and still undecided (i0066); the field 「201」 on Mochiko's message screen (i0099); the taskbar clock when Kurumi closes the trading window (i0106, unreadable in the financial specialist's enlargement); the month digit of a recalled chart tag (i0073). Kept as printed, not repaired: the i0095 axis, stepping 0.00270 from 1.20000 to 1.17570 and then to 1.16880, a value that also breaks the glitched axis of i0125; 「政策金利を0.75%に引き下げ」 with no sign (i0098); the tile 「EUR/CHF」 「BID」 「ASE」 (i0098); 「証拠金維持率(%) 0円」 on Kurumi's overseas-account screen (i0060); the box parenthetical 「(-1億2028万4479円)」, whose reference is not stated (i0118); the remembered 「敢えてしてない!」 against V06's "あえてしてない!" (i0116). No broker stop-out rule, margin-maintenance level, entry date, entry rate, fill or liquidation rate is printed for Kurumi's EUR/CHF position; its close by 「強制ロスカット」 and the resulting balance of −101,534,644円 are printed (i0118, i0130).

| Obligation | V07 state |
| --- | --- |
| FXK-SO-002 ordered image map and duplicate check | Visual order confirmed for V07: every occurrence viewed in spine order, folio sequence continuous, no duplicates or gaps |
| FXK-SO-003 component classification | Completed for V07 as tabled above; the six cover and jacket occurrences were deferred for every role and classified after the main narrative; extras and advertising classified by glance and not used as narrative evidence |
| FXK-SO-004 legibility of dense screens and small numerals | Completed for V07; the partly legible items above are recorded in the reading and none is reconstructed |

FXK-SO-001 and FXK-SO-005 are unchanged by V07; the V07 package modification date and the colophon both give 2024-09-21.

## V08 coverage

Recorded by the V08 principal for run FXK-RUN-20261119-V01-V10 and accepted with the V08 transaction by the run coordinator on 2026-11-22. The [V08 deep reading](readings/FX_KURUMI_V08_DEEP_READING.md) holds the full receipt; the [V08 checkpoint](checkpoints/FX_KURUMI_V08_CHECKPOINT.md) records each role's coverage and every disposition.

- **Witness.** FXK-JP-V08-W01, package title 「FX戦士くるみちゃん　８」: 171 image occurrences at 1441×2048, right-to-left; every occurrence was viewed once and logged once by the principal, with no gap or duplicate (verified by script). The colophon (i0170) gives e-book ver.001, published 2025-05-22 by KADOKAWA (the print first edition bears the same date), first serialized in 月刊コミックフラッパー 「2024年8月号〜2024年12月号」, with 「2025年1月号」 on a second line: six issue designations for the five chapters (ANALYST COUNT; the page does not say whether every issue carried a chapter, and the mismatch is unresolved). Colour occurrences: i0001, i0003–i0006, i0166–i0169.
- **Occurrences reviewed.** The principal opened every occurrence i0001–i0171: the main narrative in spine order first; after the main-exit freeze the post-main separator i0159, the afterword i0160–i0161, the writer's bonus comic i0162–i0164 and the storyboard excerpt i0165; then the deferred cover, flap, wraparound and under-jacket images (i0166, i0167, i0168, i0169, i0001, i0002); then the colophon and the vendor page. The entrypoint's component scope deferred those six occurrences for every role: each specialist opened all 171 occurrences in spine order and the deferred six only at its own release point; the reviewer triaged every occurrence on contact sheets, opened the decisive pages at reading resolution or in crops, and opened the deferred sheets only after its Stage 1 write-up. The [V08 checkpoint](checkpoints/FX_KURUMI_V08_CHECKPOINT.md) records each role's first sight of them against its freezes and judgments.
- **Page order, folios and spreads.** The printed folio equals the occurrence number minus 2 through the p-NNN run (p.1 = i0003 to p.163 = i0165; printed folios checked at i0026 「24」, i0029 「27」, i0060 「58」, i0063 「61」, i0092 「90」, i0095 「93」, i0112 「110」, i0113 「111」, i0126 「124」, i0129 「127」, i0156 「154」 and i0158 「156」); separator pages carry no folio but are counted. Even occurrences are right-hand pages and odd ones left-hand pages, so openings are (even | odd), as the package's spine-spread properties state. Art crosses the gutter in i0004+i0005, i0014+i0015, i0020+i0021, i0038+i0039, i0074+i0075 and i0142+i0143. The label 「第36話」 is on i0005, after the colour opening (i0003) and the colour title page (i0004); 第37話–第40話 are labelled on odd pages (i0029, i0063, i0095, i0129) facing a separator. No missing, duplicated or out-of-order page was found.

| Component | Occurrences | Notes |
| --- | --- | --- |
| Apparatus: front cover and flap | i0001, i0002 | Deferred for every role; opened by the principal after the main-exit freeze; promotional, not diegetic |
| Main narrative | i0003–i0026, i0029–i0060, i0063–i0092, i0095–i0126, i0129–i0158 (148) | A colour opening with the strip 「第8集 友達」 (i0003) and a colour title page (i0004), grouped with 第36話 (label on i0005); 第36話 i0003–i0026 (24 pages); 第37話 i0029–i0060 (32); 第38話 i0063–i0092 (30); 第39話 i0095–i0126 (32; flashback 「数日前——」 i0096–i0114); 第40話 i0129–i0158 (30), ending 「TO BE CONTINUED...」 |
| Apparatus: separators inside the main run | i0027–i0028, i0061–i0062, i0093–i0094, i0127–i0128 | Black grid pages with the series logo between the chapters |
| Apparatus: separator after the main run | i0159 | A single logo page |
| Extra: afterword | i0160–i0161 | 「8巻あとがき」 (the artist); classified only; not narrative evidence |
| Extra: writer's bonus comic | i0162–i0164 | 「でむにゃんの「遅筆」が深刻なようです。〜単に描けない編〜」; classified only |
| Extra: storyboard excerpt | i0165 | Rough ネーム of the 第36話 trade sequence; its figures match the published boxes; draft material, not narrative evidence |
| Apparatus: wraparound jacket | i0166–i0167 | Deferred; the publisher blurb and a collage of V08 panels (i0166); colour cover, spine and flap (i0167); paratext |
| Apparatus: under-jacket boards | i0168–i0169 | Deferred; the artist's gag comic 「漫画の為に借金してみる」 and the writer's 「でむにゃんはポーカー戦士のようです」; paratext, not used as story evidence |
| Apparatus: colophon | i0170 | Bibliographic |
| Advertising: vendor page | i0171 | Excluded |

Counts: main narrative 148, apparatus 16 (nine separator pages, the cover, flap, the wraparound pair, the two under-jacket boards and the colophon), extras 6 (i0160–i0165), advertising 1. There is no next-volume preview and no blank occurrence.

- **Legibility and unresolved numerals.** All reading copies are legible. Every balance box, P/L tile, chart label, order dialog, calculator and legal citation relied on was checked in enlarged crops or recorded as read at reading size because it is lettered large (the nine 評価損益 tiles i0016–i0019, the 0円 box i0020, the error dialogs i0023, the notices i0056); the reading's receipt lists the crops, and reconciliation crops settled 「出ていって?」 (i0123), the bath inset of i0147, the stacked 「1460万」 blocks (i0031), the store poster (i0082) and the memory tile (i0089). Unreadable by design, not reconstructed: the glitched numeral strip ending in 円 at i0130 (enlarged ×1 and ×2). Partly legible, not reconstructed: the memory tile 「WIN」 「USD/JPY」 「101.889円 (+24.[…]」 (i0089); the fourth notice card 「…間30分前」 (i0056); a collage fragment 「2月 280…」 and axis labels 「1.20…」 (i0152) and a gag board (i0154), read only in the financial specialist's enlargements. Kept as printed, not repaired: 「利益1億円×0.45%=4500万」 (i0030; 45% intended by the result); Kurumi's "毎日4万円" and 「1460万/年」 against 14.6% of the V07 shortfall (her rounding, i0031); the overseas account's prior balance of 0 by calculation against V07's 100,000 and +90,000 (i0003); banded cash drawn beside an account-deposit box (i0003). No fill, entry or liquidation rate, leverage figure or margin rule is printed for any V08 trade; the three EUR/CHF orders, the close by 「強制ロスカット」 at 0円 and the rejected 100-lot order are printed (i0008–i0023). No present-time calendar date is printed anywhere in the main narrative.

| Obligation | V08 state |
| --- | --- |
| FXK-SO-002 ordered image map and duplicate check | Visual order confirmed for V08: every occurrence viewed in spine order, folio sequence continuous, no duplicates or gaps |
| FXK-SO-003 component classification | Completed for V08 as tabled above; the six cover and jacket occurrences were deferred for every role and classified after the main narrative; extras and advertising classified by glance and not used as narrative evidence |
| FXK-SO-004 legibility of dense screens and small numerals | Completed for V08; the unreadable strip at i0130 and the partly legible items above are recorded in the reading and none is reconstructed |

FXK-SO-001 and FXK-SO-005 are unchanged by V08; the V08 package modification date and the colophon both give 2025-05-22.
