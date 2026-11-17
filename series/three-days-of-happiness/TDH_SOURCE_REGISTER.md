---
title: "Three Days of Happiness — Source identity and admission register"
artifact_id: TDH_TDH_SOURCE_REGISTER
artifact_type: source_and_coverage_register
series: three-days-of-happiness
version: "1.1"
generation: INITIAL_BOOTSTRAP
status: canonical
scope: "Source identity and admission register"
authority_scope: source_identity_unit_map_admission_and_coverage_for_TDH-RUN-20261116-U01-U15
source_boundary: "TDH-JP-01 bound and admitted for the authorized run U01–U15 (native chapters 1–15 with front matter at U01); per-unit read and integration states recorded below"
last_updated: 2026-11-16
canonical_home: series/three-days-of-happiness/TDH_SOURCE_REGISTER.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Three Days of Happiness — source and coverage register

## Observed witness

| Public alias | Bibliographic/source metadata | Observation basis | Admission / coverage |
|---|---|---|---|
| `TDH-JP-01` (reserved, not yet fingerprint-bound) | 三日間の幸福; 三秋 縋; Japanese MediaWorks Bunko standalone EPUB | Live folder/file presence on 2026-11-07; historical audit dated 2026-08-30 reports 333,787 bytes, 40 archive entries, five images and passed CRC/container checks | `INVENTORIED`; `NOT_ADMITTED`; `NOT_READ`; chapter/spine map `UNRESOLVED` |
| `TDH-JP-01` — current binding from 2026-11-16 (supersedes the reserved row above as current state; that row is retained as the bootstrap observation) | 三日間の幸福 (メディアワークス文庫); 三秋 縋; publisher 株式会社KADOKAWA; language `ja`; electronic edition issued 2014-11-20 per colophon; ©2013 | Live bytes rehashed by this run on 2026-11-16: 333,787 bytes; SHA-256 equal to the historical audit's recorded digest (full digest and per-member digests in the private witness receipt); 40 ZIP entries, CRC test clean, `mimetype` first and stored | `BOUND`; `ADMITTED` for run `TDH-RUN-20261116-U01-U15`; unit map `RESOLVED` (below); read/integration states per unit row |

The earlier audit labels the main novel complete. This is a reported provenance claim, not independently verified page coverage. Its digest and restricted source location are retained in the private campaign/source records; no private identifiers or receipts belong in public Git. No remote checksum, byte comparison, rendered page inspection or narrative inspection was performed for this bootstrap. Five reported images do not prove five narrative illustrations. Technical packaging validity does not certify textual correctness, publication completeness or interpretive readiness.

## Admission obligations

| ID | Open obligation | Required resolution | Effect |
|---|---|---|---|
| SRC-01 | Immutable source binding | Retrieve the governed witness; verify content digest and bibliographic/language metadata; bind reserved alias to that identity and receipt | Blocks reliable source citation |
| SRC-02 | Internal unit/locator map | Enumerate spine resources, chapters/sections and stable paragraph convention without silently changing order; distinguish body, afterword and image resources | Blocks reading schedule and exact locators |
| SRC-03 | Completeness and perception | Check missing resources, textual continuity and legible rendering within proposed scope; record remaining uncertainty rather than assume the historical audit settles it | Blocks affected unit admission |
| SRC-04 | Edition/paratext boundary | Record edition/printing identifiers available, source publication order, paratext exposure and any translation/adaptation exclusions | Blocks unqualified whole-work or cross-source claims |

These are future admission tasks, not authorization to read narrative now. Metadata reconnaissance is complete for design; full source admission is not complete.

*Status note, 2026-11-16:* the paragraph above records the bootstrap boundary. The four obligations were resolved for the authorized run on 2026-11-16 as recorded in [Admission resolution](#admission-resolution-2026-11-16); the table above is retained unchanged as the original obligation statement.

## Admission resolution (2026-11-16)

Admission was performed by the run's principal under the owner authorization recorded in the [entrypoint](CURRENT_STATE_AND_CORPUS_MAP.md#owner-run-authorization). It used technical inspection only: package structure, metadata, navigation labels, paragraph and character counts, encoding checks, image decodability, and the colophon's bibliographic lines. No chapter prose was displayed during admission; each chapter file was checked only for its blank first paragraph and its title paragraph against the navigation label. The two-paragraph front text at `text/part0002.html` and the afterword/end matter at `text/part0019.html`–`text/part0021.html` were deliberately left unread (see SRC-04).

| ID | Resolution | Residual limit |
|---|---|---|
| SRC-01 | **Resolved.** The single EPUB in the governed source folder was rehashed on 2026-11-16; size and SHA-256 equal the 2026-08-30 audit's recorded values. OPF 2.0 package metadata: title 三日間の幸福 (メディアワークス文庫), creator 三秋 縋, publisher 株式会社KADOKAWA, language `ja`, `primary-writing-mode` vertical-rl, spine `page-progression-direction` rtl. The package was produced by a Calibre 3.47.0 conversion. Private receipt: witness digest, per-member digests, normalized-text manifest digests and the extraction scripts. Public Git carries none of the private path or library identifiers. | Calibre conversion means the package is a derivative of the publisher's electronic edition rather than the publisher's own container; the publisher text is assumed carried through unchanged except where a later reading finds a defect. |
| SRC-02 | **Resolved.** 25 spine items in this order: S01 `titlepage.xhtml` (cover image), S02 `text/part0000.html` (image `images/00001.jpeg`), S03 `text/part0001.html` (image `images/00002.jpeg`), S04 `text/part0002.html` (two text paragraphs), S05 `text/part0003.html` (contents page), S06–S20 `text/part0004.html`–`text/part0018.html` (native chapters 1–15, one per file), S21 `text/part0019.html` (afterword, navigation label あとがき), S22 `text/part0020.html` and S23 `text/part0021.html` (short unlabeled end texts), S24 `text/part0022.html` (colophon, label 奥付), S25 `text/part0023.html` (image `images/00004.gif`). NCX navigation has 18 points, matching these chapter, afterword, colophon and contents boundaries. Chapters carry no heading elements; each chapter file opens with a blank P0001 and its title as P0002. The fifteen titles match the NCX labels. Paragraph normalization `TDH-NORM-v1` is defined in the [locator grammar](#locator-grammar). | Scene breaks inside chapters are marked by blank paragraphs; their analytical status is decided at reading, not here. |
| SRC-03 | **Resolved for admission.** All 33 manifest items are present; all five image resources decode (cover 525×751 JPEG; 00001 and 00002 526×751 JPEG; 00003 187×187 GIF; 00004 526×751 GIF). Normalized text has no replacement characters, mojibake signatures or control characters. Chapter files contain 82–263 paragraphs and roughly 4,100–14,900 normalized characters each (ruby readings included). Ruby (`<ruby>/<rt>`), sesame-dot emphasis (`em-sesame`) and tate-chū-yoko (`tcy`) markup are preserved in the normalized text as recorded in TDH-NORM-v1. Image-inspection capability was probed on the non-narrative colophon logo (`images/00003.gif`). | Prose continuity across file boundaries, and rendered vertical-layout typography, are checked by the principal during each reading. Plain extraction does not verify rendered typography; any typographic claim needs a rendering check. The four narrative-position images are inspected in their reading units, not at admission. |
| SRC-04 | **Resolved.** The colophon identifies this as the electronic edition (電子版), issued 2014-11-20 by KADOKAWA under the MediaWorks Bunko label, produced by ASCII Media Works and based on the seventh printing of the MediaWorks Bunko book dated 2014-09-12, with some additions and corrections for the electronic edition. Copyright 2013. Therefore `TDH-JP-01` is not a first-printing print witness, and no claim about print-edition variants is supported. **Inclusion decisions:** S01–S05 front matter is read at its disclosure position at the start of U01 and classified there. Its two front images and the cover are inspected in the `STILL_IMAGE` lane at U01. S06–S20 are the narrative units. S21 (afterword, navigation label あとがき) is creator paratext. S22–S23 (short unlabeled end texts, not yet inspected) are classified only provisionally as end paratext, from their spine position after the afterword. All three are inspected only after U15 closes, carry no narrative-evidence authority unless that inspection finds narrative material in them, and receive a recorded disposition in the completion audit; narrative material found there needs a recorded admission decision under the owner authorization before the completion audit closes. S24 colophon is bibliographic evidence only. S25's image is inspected after U15 and classified then. **Exclusions:** no translation, print witness, manga, audio, film or other adaptation is admitted; none may supply evidence or fill a gap. | Whether S04's two paragraphs are an epigraph, a blurb or narrative is unknown until U01. Whether S22–S23 contain narrative material is unknown until their inspection after U15. |

## Coverage transaction contract

On admission, add one row per mapped source unit with `unit_id`, witness alias/fingerprint, native start/end, published heading if safe, body/paratext classification, disclosure ordinal, depicted time if known, admission authority, inventory/inspection/read/integration states, reading path, unresolved gaps and next operation. Preserve distinct fields: an inventoried unit is not a read unit, and a read unit is not integrated until its notebook transaction is accepted.

At bootstrap (2026-11-07) there were no unit rows, no chapter count or ordinal was invented from EPUB resource count, and `ANALYSIS_CURRENT = EMPTY` and `RECONSTRUCTION_CURRENT = EMPTY`. From 2026-11-16 the unit rows below are current. Ordinals follow verified native chapters: each chapter is a coherent authorial unit of about 4,100–14,900 characters, so it is neither an arbitrary fragment nor the whole book. Depicted time is left unknown until a reading establishes it. `RECONSTRUCTION_CURRENT` remains `EMPTY`.

### Unit map and coverage

All rows use witness `TDH-JP-01` (bound; see above) and admission authority `TDH-RUN-20261116-U01-U15`. State fields: inventory / inspection / read / integration. Density is the expected analytical density for scheduling, not a finding.

| Unit | Spine and member | Native boundary (TDH-NORM-v1) | Published heading | Class | Disclosure ordinal | Depicted time | State | Reading path | Density / gaps / next |
|---|---|---|---|---|---|---|---|---|---|
| U01 | S01–S05 `titlepage.xhtml`, `text/part0000.html`–`text/part0003.html`; S06 `text/part0004.html` | S01–S05 whole members; S06 P0001–P0098 | １．十年後の約束 | front matter + body | 1 | Childhood flashback at age 10; narrating present ~20 (unfixed relative to the sale) | INVENTORIED / INSPECTED (text + 3 images) / READ / INTEGRATED 2026-11-17 | [U01](readings/TDH_U01_DEEP_READING.md) | S04 = publisher rights notice; S03 image = print contents page (chapter starts 004…277; no afterword entry); S02 = frontispiece without the cover's young woman, credit E9L; no gaps |
| U02 | S07 `text/part0005.html` | P0001–P0196 | ２．終わりの始まり | body | 2 | Summer at twenty: collapse, three days, then one day of referrals, appraisal and sale | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U02](readings/TDH_U02_DEEP_READING.md) | No gaps |
| U03 | S08 `text/part0006.html` | P0001–P0128 | ３．三角座りの監視員 | body | 3 | Day one after the sale (morning to night) | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U03](readings/TDH_U03_DEEP_READING.md) | No gaps |
| U04 | S09 `text/part0007.html` | P0001–P0082 | ４．答えあわせといきましょう | body | 4 | Most likely the night of day one; spring backstory | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U04](readings/TDH_U04_DEEP_READING.md) | No gaps |
| U05 | S10 `text/part0008.html` | P0001–P0082 | ５．これから起こることすべて | body | 5 | Night of day one continued, to the small hours (rain) | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U05](readings/TDH_U05_DEEP_READING.md) | No gaps |
| U06 | S11 `text/part0009.html` | P0001–P0123 | ６．変わってしまった人、変われなかった人 | body | 6 | Day two (rainy morning; outing; night) | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U06](readings/TDH_U06_DEEP_READING.md) | Witness note: P0009 「この部屋を現れた」 (に expected), no interpretive weight |
| U07 | S12 `text/part0010.html` | P0001–P0091 | ７．タイムカプセル荒らし | body | 7 | Day three (probably morning; home town; night at the school; station) | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U07](readings/TDH_U07_DEEP_READING.md) | ≈6,600 chars |
| U08 | S13 `text/part0011.html` | P0001–P0092 | ８．不適切な行動 | body | 8 | Night three into day four (before the first train to dawn) | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U08](readings/TDH_U08_DEEP_READING.md) | Witness notes: P0025 「組み伏せして」, P0069 「吐いてしましたが」, P0088 近付け/近づけ variation; no interpretive weight |
| U09 | S14 `text/part0012.html` | P0001–P0148 | ９．できすぎた話 | body | 9 | Days after the station night (five days of cranes; the next day to the festival night) | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U09](readings/TDH_U09_DEEP_READING.md) | ≈8,400 chars |
| U10 | S15 `text/part0013.html` | P0001–P0263 | 10．私の、たった一人の幼馴染へ | body | 10 | Festival night to the morning after the dinner (~days 10–12) | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U10](readings/TDH_U10_DEEP_READING.md) | Long (≈12,600 chars) |
| U11 | S16 `text/part0014.html` | P0001–P0215 | 11．自販機巡りのすすめ | body | 11 | From ~day 13 through some days of rounds to the lake night and the next morning (count unstated) | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U11](readings/TDH_U11_DEEP_READING.md) | Longest (≈14,900 chars) |
| U12 | S17 `text/part0015.html` | P0001–P0215 | 12．嘘つきと小さな願い | body | 12 | ~Days 30–32 (the substitute's two days; Miyagi's return; the night confrontation) | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U12](readings/TDH_U12_DEEP_READING.md) | Long (≈10,300 chars) |
| U13 | S18 `text/part0016.html` | P0001–P0163 | 13．確かなこと | body | 13 | ~Day 32 onward, span unstated; under two months left (deliberation, advisers, outings, the visit to Miyagi's home town) | INVENTORIED / INSPECTED / READ / INTEGRATED 2026-11-17 | [U13](readings/TDH_U13_DEEP_READING.md) | Long (≈10,100 chars) |
| U14 | S19 `text/part0017.html` | P0001–P0201 | 14．青の時代 | body | 14 | Unknown | INVENTORIED / NOT_INSPECTED / NOT_READ / NOT_INTEGRATED | — | Long (≈11,000 chars) |
| U15 | S20 `text/part0018.html` | P0001–P0127 | 15．賢者の贈り物 | body (final narrative unit) | 15 | Unknown | INVENTORIED / NOT_INSPECTED / NOT_READ / NOT_INTEGRATED | — | ≈4,100 chars; terminal boundary |
| PX-END | S21–S25 `text/part0019.html`–`text/part0023.html` | whole members | あとがき; (unlabeled); (unlabeled); 奥付; (image) | paratext (not a reading unit; S22–S23 provisional until inspected) | after U15 | n/a | INVENTORIED / colophon S24 inspected for bibliography only / NOT_READ / n/a | — | Disposition in completion audit after U15 |

Every unit uses the architecture's standing multi-agent configuration ([architecture §8.1](TDH_SYNTHESIS_ARCHITECTURE.md#81-multi-agent-reading-configuration)): principal A, specialists B (Japanese language, narration, form) and C (character, relationship, epistemic and ordinary-life evidence), and independent reviewer D. A unit-specific departure is recorded in that unit's transaction. Each unit's exposure limit is the [frontier rule](TDH_SYNTHESIS_ARCHITECTURE.md#81-multi-agent-reading-configuration): participants see only TDH-JP-01 front matter and chapters up to and including the current unit, plus accepted earlier readings.

Record each changed source identity as an appended witness event with predecessor/successor alias, reason, digest comparison, affected locators and reinspection obligations. Do not silently update a bound alias. The source register is mutable control state with append-only events; frozen receipts remain intact. Source-related contradictions link to Notebook Claims if they change an analytical assertion, but technical defects alone do not create fictional events.

## Locator grammar

Text: `TDH-JP-01::<spine-href>#<stable-fragment-or-paragraph>::<chapter/section>`. Use actual XHTML member names; one-based paragraph indices only under a recorded normalization rule. Preserve paragraph offsets and short context anchors in the private locator map when needed, without uploading bulk text. A public brief quotation may resolve an ambiguity when necessary.

Images: `TDH-JP-01::<image-resource>@<spine-position>` with inspection lane `STILL_IMAGE` and actual inspection status. Record printed pages where observed, but never treat reflow-reader page numbers as edition-stable. A unit-only locator can route work but cannot bear a precise linguistic claim. Unresolved coordinates stay explicitly unresolved until mapped.

**Normalization `TDH-NORM-v1` (recorded 2026-11-16).** Paragraph `Pnnnn` is the *n*th `<p>` element of the member's `<body>`, in document order, counted from one. Blank spacer paragraphs (only `<br/>` or whitespace) keep their index. Chapter files therefore begin with blank P0001 and the chapter title at P0002. The private normalized text keeps ruby as base《reading》, marks sesame-dot emphasis, flattens `tcy` spans, and renders an inline `<br/>` inside a non-empty paragraph as a separator. It applies no Unicode compatibility folding. A public quotation gives the base text, adding a reading only when the reading matters. Example locator: `TDH-JP-01::text/part0004.html#P0012::Ch01`. Indices do not renumber; any change of normalization requires a new version label and a crosswalk.

## Control history

| Date | Event | Scope / consequence |
|---|---|---|
| 2026-11-07 | Metadata-only reconnaissance recorded | One prior-audited Japanese EPUB present; four admission obligations open; no source unit admitted |
| 2026-11-16 | Witness bound and admitted for owner-authorized run `TDH-RUN-20261116-U01-U15` | SRC-01–SRC-04 resolved by technical inspection only; 15 native-chapter units plus end-paratext row mapped under `TDH-NORM-v1`; no prose read during admission |
| 2026-11-17 | SRC-04 end-text classification qualified after integration review | S22–S23 marked provisional end paratext pending their post-U15 inspection, since admission left them unread; no unit, boundary or admission state changed |
