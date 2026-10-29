---
series: RE_ZERO
artifact_type: source_lock
scope: SOURCE_ADMISSION_CONTRACT_AND_CURRENT_INVENTORY_STATE
generation: V0.42
status: canonical
release_state: mutable_active
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# Re:Zero — source lock and inventory

## Current lock state

**PARTIALLY LOCKED — ACQUIRED JAPANESE MAIN-LN SPINE V01-V43.**

The governed evidence locations contain a continuous Japanese main-light-novel sequence from Volume 01 through Volume 43. Those 43 objects are admitted as `MAIN_LN` witnesses. Forty-two main-volume files retain exact agreement with the 2026-08-31 manifest; the current V41 object was replaced after that manifest and is admitted under the bounded 2026-09-08 point re-audit recorded below.

This is **not a claim that the acquired corpus is current-complete**. A bibliographic freshness check on 2026-09-04 against official KADOKAWA/Re:Zero publication surfaces establishes that Volume 44 was released on 2026-03-25 and Volume 45 on 2026-06-25. Neither appears in the audited 2026-08-31 Drive manifest. The known current main-spine acquisition gaps are therefore **V44 and V45**.

The gap does **not** block a prospective Volume 01 reading. It prohibits describing the present acquisition as a complete-to-date Re:Zero main-light-novel corpus.

## Authority responsibility

This file owns the Git-side record of **which Re:Zero source witnesses are admitted for analysis and what each witness is allowed to support**.

Primary-source binaries, extracted prose, and detailed per-object audit data remain in the governed evidence plane. Git records the current admission decision, deterministic source identifiers, provenance anchors, integrity summary, known gaps, and analytical horizons.

The detailed per-file SHA-256 values remain authoritative in the Drive audit manifest identified below for the 44 audited objects whose current bytes still match it. V41 is the sole exception and is governed by the exact point-re-audit record below. Duplicating the entire otherwise unchanged machine inventory in this mutable analytical file would create two competing audit surfaces.

## Governed evidence anchors

- Primary-source Drive root: `1tNJvglC-ri_AEGTkJupZ78WddyiCqQMy`
- Re:Zero evidence folder: `14WoHQWhJ4rCtvLrrZpiwVXgnSJh37YOo`
- Drive audit manifest file: `16-fjuvDSqFGRdSoOE-WJy3uFBRwCYmgK`
- Manifest title: `audit_manifest.json`
- Manifest audit date: `2026-08-31`
- Manifest size: `23,584` bytes
- Manifest SHA-256 as retrieved for this admission audit: `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314`
- Current V41 Drive file: `1t2ppNA9sPYT4OFwZK0nG1Px1b7nc0Aon`

Normalized English filenames are locators only. Embedded Japanese titles and Japanese prose remain the semantic anchor.

## Observed Drive audit

The manifest records:

- `43` primary Japanese EPUB files representing distinct numbered main volumes V01-V43;
- no missing number inside V01-V43;
- `1` English alternate-edition EPUB for Volume 21, stored separately;
- `1` archived byte-identical duplicate of Japanese Volume 31;
- `45` audited EPUB objects total;
- all `45` passing ZIP CRC and EPUB-container checks;
- `23` packaging-conformant objects and `22` non-fatal packaging-warning objects across the 45-object audit;
- no supplemental/EX/short-story, IF/alternate-route, web-novel, or audiovisual witness represented in the manifest.

A live 2026-09-08 rescan found no new EPUB, no V44/V45, no missing manifest path, and no extra path. Forty-four of the 45 current EPUB objects reproduce the manifest size and SHA-256. The one exception is Japanese V41, whose current Drive metadata and local governed source copy both report `14,208,152` bytes rather than the manifest's `14,207,851`; its bounded replacement audit is recorded below.

The manifest states that the packaging warnings are non-fatal and that affected books remain readable after CRC/container validation.

## Admitted main-light-novel set

The following range admission is deterministic and exhaustive for the current Japanese main-LN lock:

- source IDs: `RZ-MAIN-LN-JA-V01` through `RZ-MAIN-LN-JA-V43`;
- witness class: `MAIN_LN`;
- language: `ja`;
- folder-relative locators: `Re Zero - Volume 01.epub` through `Re Zero - Volume 43.epub`;
- integrity: exact per-file SHA-256 plus CRC/container audit in the anchored Drive manifest, except V41 which uses the 2026-09-08 point-re-audit override below;
- arc: `UNASSIGNED_PENDING_SOURCE_VERIFICATION`;
- publication dates: not supplied by the local audit manifest and not globally backfilled from memory;
- horizon: V01=`START`; each VNN after the frozen prospective analysis of VNN-1.

This ranged admission is allowed because the manifest explicitly enumerates all 43 objects, reports no missing volume in the range, and records one primary Japanese edition per numbered volume, while the sole current hash replacement has now received a bounded identity/integrity audit. Any future changed hash, replacement file, revised edition, or gap invalidates the affected admission until re-audited.

## Volume 41 post-manifest point re-audit

The live source audit on 2026-09-08 found that V41 was modified after `audit_manifest.json`. The manifest remains historical evidence of its audited snapshot but no longer supplies the current V41 hash.

Current V41 identity:

- source ID: `RZ-MAIN-LN-JA-V41` (stable source identity retained);
- Drive file ID: `1t2ppNA9sPYT4OFwZK0nG1Px1b7nc0Aon`;
- locator: `Re Zero - Volume 41.epub`;
- Drive size: `14,208,152` bytes;
- governed local-source size: `14,208,152` bytes;
- current SHA-256: `abd148204c4cdd2cc52bde40fa399910fcb83661902b3ae98d16d249a2c04120`;
- language: Japanese (`ja`);
- embedded title: `Re：ゼロから始める異世界生活 41`;
- embedded creators: `長月　達平` and illustrator `大塚　真一郎`;
- publisher/label: `株式会社ＫＡＤＯＫＡＷＡ` / `ＭＦ文庫Ｊ`;
- embedded BookWalker identifier: `04684890A21975100000`;
- electronic/print basis: `2025年6月25日`, `ver.001`, first edition dated the same day;
- container root: `item/standard.opf`;
- package: 61 ZIP files, 23 manifest image resources, reflowable Japanese EPUB;
- integrity: NanaZip full-archive test passed; EPUB container metadata and package document resolved;
- packaging: non-fatal warning remains because `mimetype` is stored but is not the first ZIP entry.

The current Drive object has one retained revision only, so the earlier manifest-hashed bytes are not available for a bytewise semantic comparison. The current object is nevertheless re-admitted as the same numbered Japanese MF Bunko J V41 witness because its exact present bytes, internal bibliographic identity, language, edition/version, publisher, container structure, and archive integrity were verified. This override is limited to V41. Any future size/hash change or a mismatch between a fresh Drive download and the recorded current hash reopens V41 admission.

## Known current main-spine acquisition gaps

These are bibliographic gap records, **not admitted witnesses**.

| volume | official publication date | official evidence | acquisition state | analytical state |
|---|---|---|---|---|
| V44 | 2026-03-25 | KADOKAWA product `322511001158`; ISBN `9784046858207` | `NOT_PRESENT_IN_2026-08-31_MANIFEST` | `UNREAD / NOT_ADMITTED` |
| V45 | 2026-06-25 | KADOKAWA product `322602000800`; ISBN `9784046602145` | `NOT_PRESENT_IN_2026-08-31_MANIFEST` | `UNREAD / NOT_ADMITTED` |

Official freshness-check surfaces:

- `https://www.kadokawa.co.jp/product/322511001158/`
- `https://www.kadokawa.co.jp/product/322602000800/`
- `https://www.re-zero.com/books/`

This external check establishes publication existence/date only. It does not substitute for acquisition, file identity, hashing, or source admission.

## Alternate edition and duplicate control

The Drive manifest records two non-primary objects.

### English Volume 21 alternate edition

- path: `English Editions/Re Zero - Volume 21 - English Edition.epub`
- language: `en`
- SHA-256: `2541ba1973ca9af00b0c726d816c5dd3af817d44d6f23a012595f81ac4890c38`
- role: retained convenience/comparison witness;
- current admission state: `NOT_ADMITTED_FOR_SEQUENTIAL_READING`.

It is semantically distinct from the Japanese Volume 21 primary witness and must never be merged into the Japanese text stream.

### Japanese Volume 31 archived duplicate

- path: `_duplicates/Re Zero - Volume 31 - duplicate.epub`
- SHA-256: `5de35db8f7eba4f307b3c12ce6326fd97eb50e0f97579f7ef6ec69f7200e0921`
- exact-byte match to canonical `Re Zero - Volume 31.epub`;
- role: provenance-only archived duplicate;
- current admission state: `ARCHIVED_DUPLICATE_NOT_SEPARATE_WITNESS`.

## Supplemental and alternate witness acquisition state

**No supplemental or alternate-route primary text is admitted by the current source audit.**

The 2026-08-31 manifest contains no Japanese short-story collection, EX volume, IF/alternate-route text, web-novel corpus, guidebook, bonus story, or audiovisual witness. Their existence in the broader Re:Zero publication ecosystem does not place them inside this lock.

As a freshness/horizon test only, the official catalog establishes that `Ｒｅ：ゼロから始める異世界生活　短編集１４` was released on 2026-07-24. It is not present in the audited folder and is not admitted. If later acquired, its **publication-safe horizon** is at least `AFTER_V45_FREEZE`; its final safe horizon remains `OPEN` until diegetic/route dependencies are independently established.

That example is not an exhaustive supplemental bibliography.

## Required admission record for future items

For a newly admitted source item record, directly or through an exact manifest-anchored range admission:

| Field | Requirement |
|---|---|
| `source_id` | stable analytical identifier |
| `witness_class` | class defined by `REZERO_ROUTE_AND_WITNESS_PROTOCOL.md` |
| `language` | source language |
| `edition/publisher` | verified identity or explicitly unknown |
| `title` | printed/encoded title |
| `main_volume` | global numbered volume when applicable |
| `arc` | source-verified arc identity when applicable |
| `publication_date` | verified or explicitly unknown |
| `provenance_anchor` | governed Drive/reference locator |
| `integrity` | exact hash/audit evidence when available |
| `analytical_horizon` | earliest prospective opening point |
| `notes` | ambiguity, duplicate, variant, or routing concern |

## Supplemental placement control

Acquisition does not authorize reading.

For every future non-spine witness record:

- `H_pub`: publication-safe main-volume horizon;
- `H_diegetic`: source-verified diegetic dependency horizon, if applicable;
- `H_route`: divergence/route dependency horizon for alternate-route material, if applicable;
- `H_final`: latest established dependency among them;
- placement confidence: `VERIFIED`, `PROVISIONAL`, or `OPEN`.

The governing calculation and abstention rules are in `00 Frameworks and Methods/REZERO_ROUTE_AND_WITNESS_PROTOCOL.md`.

If a material dependency may exceed the established horizon, leave the witness unopened and `OPEN`.

## Version and duplication control

If multiple files appear to represent the same work:

- compare edition metadata;
- compare hashes where available;
- distinguish true duplicates from revised editions, bonus-text variants, or extraction differences;
- do not silently deduplicate semantically distinct witnesses.

## Volume 01 readiness decision

`RZ-MAIN-LN-JA-V01` is **READY FOR PROSPECTIVE SOURCE-FACING ANALYSIS**.

Verified evidence:

- locator: `Re Zero - Volume 01.epub`
- language: `ja`
- embedded title: `Ｒｅ：ゼロから始める異世界生活 1`
- embedded creator: `長月達平`
- size: `8,923,805` bytes
- SHA-256: `aab6d2e98cc002101cba862ed21b3750891f5e8a291e37490a06b5ea500ed627`
- EPUB/container integrity: passed;
- packaging: non-fatal `mimetype` compression warning;
- no bundled later main volume is represented by the admitted object.

Therefore `02 Sequential Readings/REZERO_LN_V01_DEEP_READING.md` may now be created from this exact Japanese witness under the prospective-freeze method.

## Volume 03 consumption record

`RZ-MAIN-LN-JA-V03` has been consumed into the frozen prospective V03 reading and the source-verified V02–V03 estate-story checkpoint.

Verified identity at consumption:

- source ID: `RZ-MAIN-LN-JA-V03`;
- Drive file ID: `1i9yf4dFhwpKclUgZI5rxTmb3TDdcSKIo`;
- locator: `Re Zero - Volume 03.epub`;
- language: Japanese (`ja`);
- embedded title: `Ｒｅ：ゼロから始める異世界生活3`;
- embedded creator: `長月達平`;
- embedded UUID: `431773eb-f119-4374-9cf7-cafc120bce17`;
- publication basis: Japanese MF Bunko J edition, 2014;
- size: `5,631,534` bytes;
- SHA-256: `6cdeb6d1f04566bdda39c9ef951ad6a33251987531dd9ff7cf2bce423d6d86b6`;
- manifest relation: exact size/hash agreement with the anchored 2026-08-31 Drive audit manifest;
- integrity: full archive test passed; 77 ZIP entries, including 20 image resources;
- analytical products: `02 Sequential Readings/REZERO_LN_V03_DEEP_READING.md` and `02 Sequential Readings/REZERO_ARC_ESTATE_STORY_CHECKPOINT.md`.

No V04 prose or previewed non-spine story was opened as part of this transaction. V04 remains admitted but analytically unopened until the user resumes the sequential run.

## Volume 04 consumption and resumed-source verification

The preceding paragraph records the historical V03 transaction, not the present opening state. The user resumed sequential analysis on 2026-10-19. The local governed source directory still supplies all 43 admitted Japanese numbered EPUBs. Their metadata/hash scan reproduces 42 manifest identities plus the already-admitted V41 override. The English V21 alternate and archived V31 duplicate are also present and reproduce their recorded hashes; neither was opened narratively. No V44/V45 or additional numbered source was found locally. This is a local acquisition check, not a fresh claim to exhaustive October publication coverage.

`RZ-MAIN-LN-JA-V04` was consumed in OPF spine order through the final publisher notice, with all 19 image resources visually inspected:

- locator: `Re Zero - Volume 04.epub`;
- language / embedded title: `ja`; `Ｒｅ：ゼロから始める異世界生活 4`;
- creator / publisher: `長月達平`; KADOKAWA / メディアファクトリー;
- UUID: `a492835f-e3b0-4837-a14a-730595c522f1`;
- package: `item/standard.opf`, 74 ZIP entries, 19 images;
- size: `9,686,186` bytes;
- SHA-256: `0439aebb5675d39e6705216db345e2faf4f780c4f15a7bc1bc7d88a18a0ed2ff`;
- manifest relation: exact size/hash agreement; manifest bytes/hash also reproduced;
- integrity: full ZIP CRC test passed; nonfatal compressed-`mimetype` warning;
- publication basis: Japanese MF Bunko J, 2014-06-30, ver.1.0;
- provenance: existing range admission under the governed folder/manifest anchors above; individual V04 Drive ID not separately resolved during local consumption;
- analytical product: `02 Sequential Readings/REZERO_LN_V04_DEEP_READING.md`, with internal block-locator convention and full coverage;
- source framing: author names `再来の王都編` as beginning here; no numeric LN arc or endpoint established.

V04's own V05 advertisement remains promotional paratext, not a V04 narrative gate prognosis or V05 source opening. The mentioned non-spine story remains unadmitted/unread. At that historical transaction, V05 and later narrative remained unopened until V04's complete publication gate; V05 consumption below occurred only after that gate closed.

## Volume 05 consumption record

`RZ-MAIN-LN-JA-V05` was consumed in exact OPF spine order through `p-bookwalker`, including all frontmatter, narrative, afterword, image columns, biographies and colophon. All 19 image resources were visually inspected.

- locator / title: `Re Zero - Volume 05.epub`; `Ｒｅ：ゼロから始める異世界生活5`;
- language / creator / publisher: `ja`; `長月達平`; KADOKAWA / メディアファクトリー;
- UUID: `198647d7-20df-47b5-9183-aec14335bd71`;
- size / SHA-256: `10,175,861` bytes; `d6c15d91fb0e67f25c9a9e02e225067f1aeb43c29b8db8ea121aadfeddf9c4a4`;
- package / integrity: `item/standard.opf`; 74 ZIP entries; 19 images; CRC test passed; nonfatal compressed-`mimetype` warning;
- manifest relation: exact size/hash agreement with the anchored manifest;
- edition basis: Japanese MF Bunko J; 2014-10-31 ver.1.0, first printing same date; afterword dated August 2014 separately;
- provenance: existing governed folder/manifest range admission; individual V05 Drive ID not separately resolved, not invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V05_DEEP_READING.md`, with stable block locators, full coverage and bounded evidence planes.

At that historical V05 boundary no V06 source, supplement, IF, web-novel or audiovisual witness had been opened. V05's next-volume emphasis and promotional columns remain paratext, not later narrative evidence or a verified capital-section endpoint. V06 consumption below began only after the entire V05 atomic publication/audit gate succeeded. This record advances consumption, not admission or the historical publication-gap check.

## Volume 06 consumption record

`RZ-MAIN-LN-JA-V06` was consumed in exact OPF spine order through `p-bookwalker`: all 40 members, 3,669 nonempty text blocks in 20 prose members, all frontmatter, six chapters, afterword, image columns, biographies and colophon. All 20 source image resources were visually inspected.

- locator / title: `Re Zero - Volume 06.epub`; `Ｒｅ：ゼロから始める異世界生活６`;
- language / creator / publisher: `ja`; `長月達平`; KADOKAWA / メディアファクトリー;
- UUID: `07e0c98e-daf5-4dd3-a025-7dace78a6393`;
- size / SHA-256: `18,893,042` bytes; `924b0b2221b314911297a92579644bd9887c88bb7896625678150a3a88840ea5`;
- package / integrity: `item/standard.opf`; 74 ZIP entries, 40 spine members, 20 images; full CRC pass; nonfatal compressed-`mimetype` warning;
- manifest relation: exact size/hash match to anchored inventory;
- edition basis: Japanese MF Bunko J, 2015-03-31 ver.1.0/first-printing basis; author afterword February 2015;
- provenance: existing governed folder/manifest range admission; individual V06 Drive ID not separately resolved or invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V06_DEEP_READING.md`, with reproducible block locators/full source-plane coverage;
- structural limit: author marks an achievement/restart and continuing counterattack, not closure of the named capital section.

At the historical V06 boundary V07 and every non-spine narrative witness remained unopened. Rem's domestic future is conditional speech within this admitted main-LN witness, not an IF source. Promotional manga/collection/goods/next-volume columns admit no later plot or extra edition. V07 consumption below began only after the complete V06 atomic publication/audit gate succeeded. Earlier freezes and source records retain their historical horizons.

## Volume 07 consumption record

`RZ-MAIN-LN-JA-V07` was consumed in exact OPF spine order through `p-bookwalker`: all37 members and3,493 body-order blocks (3,472 text +21 image-reference blocks), including frontmatter, narrative, afterword, design/image/promotional columns, biographies and colophon. All20 distinct source image resources were visually inspected, including lettering not captured as text.

- locator / title: `Re Zero - Volume 07.epub`; `Ｒｅ：ゼロから始める異世界生活 7`;
- language / creators / publisher: `ja`; `長月達平` / `大塚真一郎`; KADOKAWA;
- UUID: `412eb340-5e6f-474a-a860-03cad7f107d2`;
- size / SHA-256: `16,596,507` bytes; `d12ccb3b4ceb23a99166b940fdf85b250effd43151a4496794a634b41ecb89f1`;
- package / integrity: `item/standard.opf`;72 ZIP entries,37 spine members,20 images; full CRC pass; nonfatal compressed-first-`mimetype` warning;
- manifest relation: exact size/hash match to the anchored inventory;
- edition basis: electronic publication and stated first-edition/first-printing basis `2015-09-30`; afterword August2015;
- provenance: existing governed folder/manifest range admission; individual V07 Drive ID not separately resolved or invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V07_DEEP_READING.md`; exact per-member coverage/block locators in §1;
- structural limit: one continuing V07-E1=V06-E2 state, no new Subaru death/return; Whale hunt ends, estate/Cult operation and private insurance/plan remain pending/withheld at dawn.

At the historical V07 boundary V08 and every non-spine narrative witness remained unopened. The design-page `モフっ子` note and `剣鬼恋歌` promotion remain bounded paratext. V08 below opened only after V07's complete source-audit, housekeeping and final actual exact-source full audit/status gate succeeded; earlier source records retain their horizons.

## Volume 08 consumption record

`RZ-MAIN-LN-JA-V08` was consumed in exact OPF spine order through `p-bookwalker`: all40 members and3,342 body-order blocks (3,320 text +22 image references), including all frontmatter, narrative, afterword, artist/promotional images, biographies, credits and colophon. All21 distinct image resources were visually inspected; repeated MFJ logo reference is not another distinct file.

- locator / title: `Re Zero - Volume 08.epub`; `Ｒｅ：ゼロから始める異世界生活 8`;
- language / creators / publisher: `ja`; `長月達平` / `大塚真一郎`; KADOKAWA / Media Factory;
- UUID: `dce9259f-d159-4958-af30-f0b2b657189f`;
- size / SHA-256: `20,623,478` bytes; `cd8c390f910aef162e4015398c66ece29fc074ad3f4c2ad33469831641e70321`;
- package / integrity: `item/standard.opf`;77 ZIP entries,40 spine members,21 images; full CRC pass; nonfatal compressed-first-`mimetype` warning;
- manifest relation: exact anchored size/hash match; manifest reverified unchanged;
- edition basis: electronic issue `2016-03-25`; stated underlying first edition/first printing `2016-03-31`; afterword February2016;
- provenance: existing governed folder/manifest range; individual V08 Drive ID not separately resolved or invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V08_DEEP_READING.md`, exact per-member coverage/block convention §1;
- prospective record: exact45 inherited questions/ten forecasts fixed before archive opening, record SHA-256 `bc11d128b96492cdcbceea79622a891ce09582df90ab45985f198cc94f001c62`;
- structural limit: V08-E1 continues V07-E1/V06-E2/RZ-E-011 until Subaru death eleven; world flow narrated without successor arrival/checkpoint, no capital-section closure.

At the historical V08 boundary V09 and all non-spine narrative remained unopened. In-volume artist/promotional pages are paratext, not current Rem/Beatrice appearances or admission of advertised WN/anime/manga. Source identity/image-byte/prospective/prior-freeze guards passed; consumption rests on ordered full reading and visual inspection, not structural parsing alone. All seven earlier volume freezes and estate checkpoint remained unchanged. V09 below opened only after the complete V08 publication gate closed; admitted range and historical bibliographic-gap check do not advance.

## Volume 09 consumption record

`RZ-MAIN-LN-JA-V09` has been consumed through `p-bookwalker`: all44 OPF spine members and3,830 body-order blocks (3,806 text +24 image references), including frontmatter, narrative, internal escape-family fragment, afterword, artist/promotional pages, biographies, credits and colophon. All22 distinct image resources were visually inspected. One reading-order exception is disclosed below rather than described as flawless spine order.

- locator / title: `Re Zero - Volume 09.epub`; `Ｒｅ：ゼロから始める異世界生活 9`;
- language / creators / publisher: `ja`; `長月達平` / `大塚真一郎`; KADOKAWA / Media Factory;
- UUID: `9d0da354-8c4c-48df-a2f6-40e5fb94fd28`;
- size / SHA-256: `16,078,989` bytes; `5dc5fb10375bdcde0772e14ecf388f49c7a96e1772fd16307868e12d46d8e951`;
- package / integrity: `item/standard.opf`;82 ZIP entries,44 spine members,22 distinct images; full CRC pass; nonfatal compressed-first-`mimetype` warning;
- manifest relation: exact anchored size/hash match; manifest SHA-256 `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314` unchanged;
- edition basis: electronic issue `2016-09-23`; stated underlying first edition/first printing `2016-09-30`; afterword August2016;
- provenance: existing governed folder/manifest range; individual V09 Drive ID not separately resolved or invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V09_DEEP_READING.md`, exact per-member coverage/block convention §1;
- prospective record: all50 inherited questions/ten forecasts fixed before archive opening, immutable record SHA-256 `072791ac49fbb1a2b2ac338b79f2f81387111002262bf9eae0a9b1c06a9e68a8`;
- structural boundary: council arrival RZ-E-012, actual death twelve/bedside arrival RZ-E-013; internal family not another return or current biography; explicit third-arc V04–V09 closure in afterword, not completed Rem restoration.

Reading-order exception: after the main-route nonrecognition line at `p-018#B0001`, `p275.jpg` was extracted/viewed before `p-019` prose. The exposure was immediately disclosed and interpretation quarantined; all209 `p-019` blocks were then read in order and the image reinspected at its actual `p-020` reference. No claim or prospective horizon was revised from the premature image; later argument rests on independently consumed prose. This is not an undisclosed perfect-order claim or an exposure to a later volume/non-spine source. The remaining ordered-consumption record accounts for all members/blocks/images, with no unresolved source gap.

Post-EOF exact source, manifest, image bytes, immutable prospect and all eight earlier freezes/estate-checkpoint guards passed. A structural guard does not prove reading; actual full text acquisition and visual inspection do. The internal married family is part of this MAIN_LN container under incompatible local premises, not admission of external IF/WN. Artist/promotional Rem/Emilia dialogue does not awaken current Rem or admit advertised anime/games/bonus witnesses. V10 and all separately acquired non-spine narrative remain unopened. At the V09 freeze the required next operation was the separately pending V04–V09 arc checkpoint, to be created only after V09's complete publication gate and closed before V10; its later completion record follows.

## Post-V09 third-arc checkpoint source boundary

`02 Sequential Readings/REZERO_ARC_03_CHECKPOINT.md` is a bounded synthesis of frozen V04–V09, created after V09 commit `ac38cbe884bdcd82919d34cfaea7fd3cacc4a46b` completed its exact-source publication gate. V09 `p-028#B0002–0004` verifies the third arc's V04 beginning and V09 closure; B0022 names the next arc. All six contributing EPUB SHA-256 identities were reverified read-only. The checkpoint uses their existing complete consumption/frozen evidence, not a new full reading or any additional witness. V09's image-order exception remains disclosed, not erased by synthesis.

No source is newly acquired/admitted/consumed, high-water remains V09, and all nine volume freezes/estate checkpoint remain unchanged. V09 §16's exact50-question/ten-forecast V10 prospect is retained, not hindsight-adjusted. The checkpoint's own approved commit/full-content remote readback, source audit, completed housekeeping and final actual exact-source full audit/status must pass before Japanese V10 opens. This record does not itself certify those future checks.

## Volume 10 consumption record

The separate third-arc checkpoint completed its exact-source publication gate at commit `ebd99a3cc5fe1806b094fbeddae5b6b2b37c0a06` before first V10 archive access. Its final actual full audit/status and completed housekeeping, not a dispatch's displayed branch label, controlled opening. The preceding checkpoint record preserves its then-pending future checks; they are now closed.

`RZ-MAIN-LN-JA-V10` was consumed in OPF spine order through `p-bookwalker`: all43 members/3,835 body-order blocks (3,812 text +23 image references). All22 distinct image resources were visually inspected at their references, including graphic text; repeated publisher logo reinspected at colophon. Actual acquired ranges/end cursors, reacquisition of lost output and visual inspection establish consumption; structural guards alone do not. One tiny informal artist-sketch mark is not reliably deciphered and supports no proposition; no narrative text gap remains.

- locator / embedded title: `Re Zero - Volume 10.epub`; `Ｒｅ：ゼロから始める異世界生活 10`;
- language / embedded creators / publisher: `ja`; `長月　達平` / `大塚　真一郎`; KADOKAWA / メディアファクトリー;
- UUID: `f0c1ea3f-bfae-419f-8287-3c870bbe1db5`;
- size / SHA-256:13,069,851 bytes; `92a5bbf737e25bac82e53ebaf4486d26ba89a97976d2ed21773a83e2c8f1a1b8`;
- package / integrity: `item/standard.opf`;81 ZIP entries; full CRC pass; nonfatal first-but-compressed `mimetype` warning;
- manifest: exact size/hash match to anchored manifest, unchanged SHA-256 `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314`;
- edition: electronic issue2016-10-25; stated first edition/first printing2016-10-31; afterword September2016 separately;
- provenance: governed folder/manifest range admission; individual V10 Drive ID unresolved, not invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V10_DEEP_READING.md`, exact member/block/image coverage and locator convention §1;
- pre-opening prospect: all50 inherited questions/ten forecasts sealed, immutable record SHA-256 `cfe4058aa3177c9aed98ab876c3e7ff498fe9c69e1005ee297eae1508b6c6276` unchanged;
- ending: V10-E1 continues E013 until death13; restart declared without represented arrival,13 arrived segments/no E014; no collateral fate census;
- structure: afterword verifies fourth-arc beginning, not ending; parent trial is memory-based construction, not actual Earth receipt or external IF;
- guards: post-EOF source/manifest/image bytes/prospect and all eleven earlier frozen artifacts unchanged; no raw source/private acquisition objects committed.

V11 and all separate non-spine narrative remain unopened. V10 §16 fixes55 V11 questions/ten forecasts now, before the earned Subaru V01–V10 model/separate first fidelity audit. That operation follows V10's complete publication gate and must close before V11, without altering the prospect or admitting another witness. The source high-water becomes V10 only after the gate; admission range and historical gap check do not advance.

## Post-V10 Subaru model and first fidelity-audit source boundary

V10's complete exact-source publication gate is verified at `ff4a7abec35fcb32c4b51be22c0033c1e172527c`, before this separate synthesis operation. Full remote content/identity readback, source and final full385-test audits, completed NOOP housekeeping and final success status targeted that exact source commit; dispatch metadata alone was not used as proof. The preceding V10 record preserves its then-future gate, now closed.

This operation creates two **derived analytical artifacts**, not newly acquired witnesses: `05 Character Analysis/REZERO_NATSUKI_SUBARU_V01_V10_CHARACTER_MODEL.md` and `08 Audits and Manifests/REZERO_CHARACTER_RECONSTRUCTION_FIDELITY_AUDIT.md`. It reuses the completed V01–V10 corpus/current owners with targeted analytical retrieval and required mature design references; no primary volume was newly reread, no V11/later source or non-spine narrative opened, and no raw media copied into Git. The separate19-dimension document-level author audit returns PASS_WITH_BOUND, not an independent benchmark or global capability grade. Exact source locators and hashed-witness routes remain in frozen readings/source lock; generated probes are not evidence.

All ten VNN freezes/two checkpoints, five specialist owners,110 current claims and exact55-question/ten-forecast V11 prospect remain unchanged. Source high-water stays V10. V11 is next only after this model/audit operation's own approved commit/full remote readback, source audit, completed housekeeping and final actual exact-source full audit/status. Local analytical acceptance does not certify those future publication checks. Default terminal E013/death13 and all real-parent/Rem/successor/IF/adaptation exclusions remain binding.

## Volume 11 consumption record

The corrected Subaru V01–V10 model/first-audit operation completed its own exact-source publication gate at `93f6656e02a61c73cb785f01f0c33c5efe27fc08` before first V11 archive access. Complete remote content/identity readback, source audit, completed NOOP housekeeping, final actual-source full385-test audit and exact-source success status—not the dispatch's displayed main-head metadata—controlled opening. The preceding model-operation record preserves its then-future checks; those checks are closed. No model/audit bytes are changed by this V11 transaction.

`RZ-MAIN-LN-JA-V11` was consumed in OPF spine order through `p-bookwalker`: all43 members/4,096 body-order blocks (4,071 TEXT +25 positioned IMAGE references), with all23 distinct resources actually visually inspected at their positions. Repeated gaiji and publisher-logo references were separately inspected. Actual acquired contiguous ranges, image views, reacquisition of lost output and EOF establish reading; ZIP/count/locator guards alone do not. A lost `p-003#B0119` attempt was reacquired before continuation; no source interval remains unresolved.

- locator / embedded title: `Re Zero - Volume 11.epub`; `Ｒｅ：ゼロから始める異世界生活 11`;
- language / embedded creators / publisher: `ja`; `長月　達平` / `大塚　真一郎`; KADOKAWA / メディアファクトリー;
- UUID: `ecf9232a-0b4c-4d55-b5da-ea8b1228bada`;
- size / SHA-256:9,845,672 bytes; `6fbdc979332a3c51d8b85d01dc93b1b71714e8bbf875271bdef42dc46715275b`;
- package / integrity: `item/standard.opf`;82 ZIP entries; full CRC pass; known nonfatal first-but-compressed `mimetype` warning;
- manifest: unchanged23,584 bytes/SHA-256 `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314`, exact anchored V11 identity match;
- edition: electronic issue2016-12-23, based on MF first edition/first printing2016-12-25; afterword November2016 distinct;
- provenance: governed local read-only EPUB and manifest range admission; individual V11 Drive object ID unresolved, not invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V11_DEEP_READING.md`; complete member/block/image coverage and locator convention §1;
- entering prospect:55 questions/ten forecasts copied before model construction and V11 opening, unchanged private seal SHA-256 `38f61f29c0b039d6017e9d907754c5e3c94be9e21a17d36806f3ced150b49e7b`; all individually adjudicated;
- ending: actual E014/E015/E016, new deaths14/15,15 deaths/16 arrived segments; E016 alive-last-shown facing shadow, no death16/E017 or full missing-person census;
- structure: fourth arc continues; afterword's adaptation/rewrite/WN-divergence discussion is not an arc-ending certificate or a merged witness;
- preservation: all twelve predecessor freezes and V01–V10 model/audit byte-unchanged; no source binaries, extraction, images or private acquisition objects committed.

V12 and all separately acquired non-spine narrative remain unopened. V11 §16's60 V12 questions/ten forecasts were copied exactly into the private pre-reading seal after actual V11 EOF and before V12; SHA-256 `c0f8feb6ef89cb5c67dd68f881542a7ff8ca7da78e52df623142b79c54a975e0`. This transaction becomes current V11 authority only after its complete publication gate. Source admission and the dated V44/V45 acquisition-gap assessment do not advance.

## Volume 12 consumption record

V11's complete source-bound publication gate at `890ff364c8c8159fd74c5021fad6b316d0bcaa91` closed before first V12 archive access. Immutable full-file/identity readback, actual source full385-test audit, completed source-bound NOOP housekeeping, final actual-source full385-test audit and exact success reporting controlled opening; the final dispatch's displayed main commit was not mistaken for its audited source. The preceding V11 record retains its then-future conditions as historical, not still-pending work. The V01–V10 model/audit and thirteen prior freezes are unchanged.

`RZ-MAIN-LN-JA-V12` was consumed in OPF spine order through `p-bookwalker`: all43 members/3,939 body-order blocks (3,916 TEXT +23 positioned IMAGE references), with all22 distinct resources actually visually inspected. The publisher logo was inspected at both references. Actual contiguous deliveries, reacquisition of lost `p-009#B0281` output, full2,890-character single-block `p-023` speech, image views and EOF establish consumption, not ZIP enumeration. Invalid shortened end-member selectors returned no content and were replaced by successful exact OPF member reads; no unresolved text/image gap remains. The paired character-art/promotional dialogue pages are paratext, not newly admitted future narrative.

- locator / embedded title: `Re Zero - Volume 12.epub`; `Ｒｅ：ゼロから始める異世界生活 12`;
- language / embedded creators / publisher: `ja`; `長月　達平` / `大塚　真一郎`; KADOKAWA / メディアファクトリー;
- UUID: `3c0b1c5a-df07-4cac-a1f8-506534e1a0b7`;
- size / SHA-256:9,937,280 bytes; `c889d9bdd7af41cb4df227d5db29514113c56b78ac7617441bb239cf980783af`;
- package / integrity: `item/standard.opf`;81 ZIP entries/full CRC pass; known nonfatal first-but-compressed `mimetype` warning;
- manifest: unchanged23,584 bytes/SHA-256 `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314`, exact anchored V12 size/hash match;
- edition: electronic issue2017-03-25, based on MF first edition/first printing2017-03-25; afterword February2017;
- provenance: governed local read-only EPUB/existing range admission; individual V12 Drive object ID/ISBN not invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V12_DEEP_READING.md`; complete member/block/image coverage and locator convention §1;
- entering prospect:60 questions/ten forecasts sealed after V11 EOF/before V12, unchanged SHA-256 `c0f8feb6ef89cb5c67dd68f881542a7ff8ca7da78e52df623142b79c54a975e0`; all individually adjudicated;
- ending: E016 closes at self-stabbing16, actual E017 then Rabbit-wound death17/actual E018;17 deaths/18 segments, E018 alive at seventh-Witch arrival; no death18/E019 or post-tea bodily waking;
- representation: second-trial depictions are constructed, not extra deaths/current shared encounters or verified underlying RBD ontology; only first trial passed;
- structure: fourth arc continues; rejected formal offer/Beatrice rescue intention are not accepted contract/completed rescue or an arc ending;
- preservation: all thirteen predecessor freezes and V01–V10 model/audit byte-unchanged; no source media, extraction or private records committed.

V13 and all separate non-spine narrative remain unopened. V12 §16's60 V13 questions/ten forecasts were sealed after actual V12 EOF/before V13 and copied exactly into master; private seal SHA-256 `d940868792d5513313831eed4b0b105c500dcd25925e50e7a1a2298b8087d1bd`. V12 becomes current authority only with its complete publication gate. Admission range, manifest/V41 exception and dated V44/V45 gap assessment are unchanged.

## Volume 13 consumption record

V12's complete source-bound publication gate at `28c541b6c0f2c3c73a9f98f315424a58ce70348e` closed before first V13 archive access. Full immutable body/identity readback, actual-source full 385-test source audit, completed source-bound NOOP housekeeping, final actual-source full 385-test audit and exact success reporting controlled opening. The preceding V12 record preserves its then-future conditions historically, not still-pending work. Fourteen predecessor freezes and the V01–V10 Subaru model/audit remain unchanged.

`RZ-MAIN-LN-JA-V13` was consumed in OPF spine order through exact `p-bookwalker`: all 44 members/3,993 body-order blocks (3,971 TEXT +22 positioned IMAGE references), with all 21 distinct resources actually visually inspected. The shared publisher logo has two positioned references. Contiguous text deliveries and actual image views establish reading; the structural inventory explicitly does not prove consumption. Rejected shortened terminal selectors returned no content and were replaced by successful exact `p-credit`, `p-colophon` and `p-bookwalker` reads. No unresolved text/image gap remains. Character-art/promotional dialogue is paratext, not admission of an advertised witness.

- locator / embedded title: `Re Zero - Volume 13.epub`; `Re：ゼロから始める異世界生活 13`;
- language / embedded creators / publisher: `ja`; `長月　達平` / `大塚　真一郎`; KADOKAWA / メディアファクトリー;
- UUID: `d143d297-fb29-4d74-9cb9-250bb64f03bf`;
- size / SHA-256: 7,580,833 bytes; `f352e6bf101a26c3b0cfc35bec32677afc886315cf4082ead6bace727acb1a41`;
- package / integrity: `item/standard.opf`; 80 ZIP entries/full CRC pass; known nonfatal first-but-compressed `mimetype` warning;
- manifest: unchanged 23,584 bytes/SHA-256 `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314`; exact anchored V13 size/hash match;
- edition: electronic issue 2017-06-25, based on MF first edition/first printing 2017-06-25; afterword May 2017;
- provenance: governed local read-only EPUB/existing range admission; no individual V13 Drive object ID or ISBN invented;
- analytical product: `02 Sequential Readings/REZERO_LN_V13_DEEP_READING.md`; complete member/block/image coverage and locator convention §1;
- entering prospect: sixty questions/ten forecasts sealed after V12 EOF/before V13, unchanged SHA-256 `d940868792d5513313831eed4b0b105c500dcd25925e50e7a1a2298b8087d1bd`; all individually adjudicated;
- ending: E018 continues alive, seventeen deaths/eighteen segments; no physical tea-self-bite death, death18 or E019. Garfiel's first trial passes, Emilia's renewed first begins; no second/third pass;
- costs / receipt: Shima supplies the current miasma observation; Otto receives partial crisis knowledge, not RBD/tea. Subaru's gate collapses at his last self-cast Shamak; later healing is not gate repair. The new invisible fist has bounded observation and cost;
- structure: the fourth arc continues; accepted wager, promised apology, revised cooperation and rescue plans are not fulfilled wager, completed repair, barrier/mansion/Beatrice rescue or an arc ending;
- preservation: all fourteen predecessor freezes and historical Subaru model/audit remain byte-unchanged; no source media, extraction or private receipt enters the commit.

V14 and all separate non-spine narrative remain unopened. V13 §16's sixty V14 questions/ten forecasts were sealed after actual V13 EOF/before V14 and copied exactly into master; private seal SHA-256 `c851e05497b964d74e76480b50d0c4c2d150873c4b17e351b595a122cd069eb6`. Otto's earned V01–V13 model and separate fidelity review follow V13's complete publication gate and must complete their own full gate before V14 source; the prospect remains unchanged throughout. V13 becomes current authority only with its complete publication gate. Admission range, manifest/V41 exception and dated V44/V45 acquisition-gap assessment do not advance.

## Historical post-V13 Otto model and scoped fidelity-review source boundary

V13's complete source-bound publication gate closed before this earned separate construction. The integrated `05 Character Analysis/REZERO_OTTO_SUWEN_V01_V13_CHARACTER_MODEL.md` and `08 Audits and Manifests/REZERO_OTTO_SUWEN_V01_V13_FIDELITY_REVIEW.md` now compile admitted V01–V13 evidence. They add analytical use/review artifacts, not a primary witness, new volume consumption or narrative claim generation.

Targeted original-Japanese reconciliation checks the earlier V05/V06 fear/commercial/receipt counterexamples, V09 ordinary inventory and bargaining tension, V10 care/role/ordinary limits, V11 actual E015 friendship/terminal harm, V12 offered hearing and V13 newly enacted partial friendship. V13's complete EPUB/image consumption belongs to the prior reading; this operation does not claim another full V01–V13 reread. Every selected witness retains its admitted manifest hash; no ISBN, individual Drive ID or new edition is invented.

The model compiles 32 retrieval bundles/26 conditional rules/nine noncanonical probes. Its separately reported same-analyst, scoped nonblind nineteen-dimension documentary review is PASS_WITH_BOUND, not a blind benchmark, inherited Subaru grade or global capability assessment. Default is living E018 outside the tomb while Emilia begins the renewed first trial. Own cult-rescue debt, Subaru-only E015 history and current E018 reciprocity remain separate; undisclosed agreement contents, private preferences, infinite resources and unread outcomes remain bounded.

All thirteen VNN freezes/two checkpoints, historical Subaru model/first audit, five specialist owners and 216 current V13 claim formulations remain unchanged. Source high-water stays V13. Both next-operation fields route V14 only after this operation's own full publication gate. The exact sixty-question/ten-forecast V14 prospect remains unchanged; V14 and all separate nonspine narrative stay unopened. Admission range, manifest/V41 exception, dated V44/V45 acquisition-gap assessment and active terminal V43 do not advance.

## Volume 14 consumption record

V13's full source gate at `a49cac9a52002130a64939bbc9121fceeba5c76a` and Otto13's separate full gate at `636c3d1d084250c6e4efc4c8185479e5b7763541` both closed before first V14 archive access. Otto source audit39511361098, completed NOOP housekeeping39511785191, final actual-source full385-test audit39511838323 and exact-source success/status controlled opening. Displayed dispatch main metadata was not substituted for audited source. Both historical model/review pairs remain unchanged.

`RZ-MAIN-LN-JA-V14` was actually consumed in ordered OPF spine through final p-bookwalker:44members/3906nonemptypositions=3883TEXT+23positionedIMAGErefs/22distinctoriginalresources. Both logo positions were viewed. Narrative3826text/front-back57;48boundedtextdeliveries/23originalimage-positionviews/zero gaps. Late p024B255–301 was only credited after a context-truncated delivery was reacquired whole. Structural ZIP/OPF counts and CRC were separate identity checks, not reading proof. Source remained read-only; private notes/images/receipts remain untracked.

- file/title: `Re Zero - Volume 14.epub`; `Re：ゼロから始める異世界生活 14`;
- size/SHA256:10,009,892bytes / `1ec6f16a115b020b3239b41bcb0ec767c9f5528559c5fe4c4a76ac49026b7358`;
- package/language/creators/publisher: `item/standard.opf`; `ja`; 長月　達平 / 大塚　真一郎; KADOKAWA / メディアファクトリー;
- UUID:`37db7704-8a90-40ed-8d7c-b2a48f94aa27`;81ZIPentries/CRCpass/first compressed mimetype method8 observed nonfatal;
- manifest:unchanged23,584bytes/SHA256 `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314`, exact admitted size/hash/title match; no individual DriveID/ISBN/OPFdate invented;
- observed edition:p-colophonB4/B8 electronic issue/basis first edition-first print2017-09-25; p027afterwordAugust2017;
- analytical product:`02 Sequential Readings/REZERO_LN_V14_DEEP_READING.md`; §1 exact coverage/locators, §12claims, §13all216predecessors, §14all60incomingquestions, §2tenforecasts;
- incoming prospect:exact60questions/10forecasts fixed after V13EOF/before V14, SHA256 `c851e05497b964d74e76480b50d0c4c2d150873c4b17e351b595a122cd069eb6`, preserved through prior Otto operation and now adjudicated;
- reached state:E018alive/17deaths18segments, Emilia FIRST PASS/SECOND START, actual Petra/sibling/library contacts and both fights begun; no all-site rescue/evacuation, barrier, cast snow/Rabbit result, wager or Arc4end;
- outgoing prospect:exact60V15questions/10forecasts sealed after actualEOF/before anyV15opening, SHA256 `f1959a017cb1e123e40a4d193d9c1b99bf098038f948946db19bc4c7dfc2498c`.

V15 and separate nonspine narrative remain unopened. V14 becomes committed authority only with the full synchronized publication gate; then the earned EMILIA_V01_V14_MODEL_AND_FIDELITY_REVIEW must complete its own full gate before V15. Its reserved derived artifacts do not consume/admit source15 or silently change Subaru10/Otto13 scope. Admission range, manifest/V41exception, datedV44/V45gaps and activeterminalV43 remain unchanged. Advertised shortstories/artbook/WN/anime are not opened.

## Post-V14 Emilia reconstruction use — no new source admission

After V14's full gate at cfd5627ddc4cf26fe5bd05bb1fac3b7eeb23f960, the V01–V14 Emilia model and separate scoped review were implemented. Twenty-seven bounded direct Japanese deliveries reconciled already consumed V01/V03/V04/V09/V12/V13/V14 windows against exact manifest identities; this is not another complete fourteen-volume reread. The review is actual same-analyst nonblind nineteen-dimension documentary PASS_WITH_BOUND with two resolved traceability repairs, not independent runtime, a global grade or a new narrative source.

Default is living E018 FIRST PASS/SECOND START before contents; positive private warmth, still-hidden grief, ordinary mayonnaise liking, particular requested support and incomplete Ram-petition understanding remain bounded. All20 historical artifacts/five owner bytes/256 current narrative claims and the exact V15 seal remain unchanged. Only this separate operation's own complete publication gate permits V15. Source high-water stays V14, admission V01–V43/V41exception/datedV44–45gaps and active V43 authorization stay unchanged; no separate witness is opened.

## Volume 15 consumption record

Source15 was first opened2026-10-21T02:36:15Z only after V14's complete gate at cfd5627ddc4cf26fe5bd05bb1fac3b7eeb23f960 and Emilia14's separate complete gate at1a421296e69e547dd9bd017a83a00b9a5d7bc1de. The exact incoming60-question/10-forecast seal f1959a017cb1e123e40a4d193d9c1b99bf098038f948946db19bc4c7dfc2498c remained unchanged.

| responsibility | actual result / limit |
|---|---|
| admitted object | `RZ-MAIN-LN-JA-V15`; `Re Zero - Volume 15.epub`;9893538bytes;SHA256 `3d4e93eab533a513a49fe7a26f27aae8d2ae370a6d7eb5d6178698d5e3aa3d25` |
| package | `item/standard.opf`; ja;長月達平/大塚真一郎;KADOKAWA/メディアファクトリー;80entries/CRCpass; first mimetype compression8 nonfatal; no invented ISBN/DriveID |
| manifest |23584bytes/SHA256 `3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314` unchanged; no admission expansion |
| actual reading |45/45 OPF members,3995/3995positions=3974TEXT+21positionedIMAGEreferences/20distinct originals,52bounded text deliveries; zero gaps/duplicates; each original viewed in order including repeated logo/title/colophon/final BOOKWALKER |
| lost-delivery handling |p-001#B0286–0339 was fully reacquired after outer delivery loss before later members; inspection/cached existence alone was not credited |
| dates and endpoint |electronic issue/first-edition first-print basis2017-12-25, afterword composition2017-11; fourth arc explicitly concluded p-029#B0004/B0014/B0016; final source logo actually viewed by about03:21Z |
| closeout |292claims; all256predecessors/60incomingquestions/10forecasts; actual E018alive17deaths18segments at month-later ceremony/party; five owners/master synchronized;22 prior artifacts unchanged |
| next-source seal |60V16questions/10forecasts; UTF-8/LF SHA256 `279e4a504f39376b8b7083a95841ef28ee10416976c93bc9d69bb20b9bf1b413`; fixed through source-free derived operations |

The final contributing volume must pass its full synchronized publication gate before separate `ARC04_CHECKPOINT`. Then the four earned person constructions/reviews each need their own complete gate before V16. None consumes/adopts V16, the advertised collection/manga/WN, separate IF or adaptation. Source lock retains43-object admission/V41 exception/datedV44–45gaps; no global source curation or new acquisition is performed.

## Post-V15 fourth-arc checkpoint source boundary — no new admission

The full V15 publication gate closed at `98acb7201088307023f6007e2314b44dd8c72897` before this separate source-free checkpoint began. All six original V10–V15 files were rechecked read-only against each frozen reading's sourceSHA256 and passed full ZIP CRC. The [checkpoint](../02%20Sequential%20Readings/REZERO_ARC_04_CHECKPOINT.md) records those exact identities and six frozen Git blobs; it synthesizes their already consumed evidence rather than claiming six new raw-source readings. V15p029B4/14/16 explicitly closes the arc; V10's beginning and older V09 announcement remain separately attributed.

All23 earlier historical artifacts, all five owner files,292V15claim formulations and the exact V16seal279e4a504f39376b8b7083a95841ef28ee10416976c93bc9d69bb20b9bf1b413 remain unchanged. The checkpoint is a separate frozen comparison subject to its own complete gate, not source16 consumption or new model fidelity. That gate precedes Beatrice15; Garfiel10–15, Ram15 and Roswaal15 each then require their own construction/review/full gate before the next/source16. No supplement, advertisement, WN, IF, adaptation, replacement edition or new source is admitted. The43-object inventory/V41exception/datedV44–45gaps remain unchanged.

The complete replaced source-summary section follows verbatim from98acb720 as history, not current instructions:

```markdown
## Current source-state summary

- **Acquired/admitted Japanese main LN:** V01-V43 continuous.
- **Known published but not acquired/admitted main LN:** V44-V45.
- **Admitted translations:** none.
- **Retained non-admitted translation:** English V21, local hash reverified on resumption.
- **Admitted supplemental/EX/short-story:** none.
- **Admitted IF/alternate route:** none.
- **Admitted web novel:** none.
- **Admitted anime/audiovisual:** none.
- **Consumed into prospective main-LN analysis:** V01–V15, with actual complete V15 source consumption; committed authority advances only on this synchronized transaction's full gate. Earlier Subaru10/Otto13/Emilia14 models/reviews retain exact historical scope and grade.
- **Next source acquisition priority:** Japanese V44 and V45 before the sequential read reaches that boundary.
- **Next analytical operation:** `ARC04_CHECKPOINT` after complete V15 publication; then Beatrice15, Garfiel10–15, Ram15 and Roswaal15 separate model/review operations, each full gate before the next/source16. V16 remains unopened with the exact60/10 seal above.
- **Current execution state:** active continuous terminalV43. E018alive/17deaths18segments after actual rescue, three trials, two-site local release, finite chosen contract/defense, plural settlement and accepted office; reader-only Omega coda. No death18/E019, Rabbit extinction, gate/reserve repair, Rem awakening, full camp RBD/tea, origin telling/old apology or held capital reward ceremony is implied. Sourceverified Arc04 end earns a separate checkpoint, not completed models or full-series synthesis.
```

## Post-Arc04 Beatrice15 reconstruction source boundary — no new admission

Arc04's complete gate at `6bce1604e7da9c688737568aaefb971abe4bc9a3` closed before construction. The [Beatrice15 model](../05%20Character%20Analysis/REZERO_BEATRICE_V01_V15_CHARACTER_MODEL.md) and [separate review](../08%20Audits%20and%20Manifests/REZERO_BEATRICE_V01_V15_FIDELITY_REVIEW.md) revisit already-consumed V01–V15 only. Forty-seven actual contextual Japanese windows/118868characters in V02/V03/V06/V09/V10/V11/V12/V14/V15 were delivered at their returned endpoints with exact admitted archive hash/CRC checks; search matches, shortened requests and truncated deliveries were not falsely credited. No new fifteen-volume reread or new primary unit is claimed. Four other series' designs are design references, not literary evidence.

All24 predecessor analytical artifacts, five owners/master narrative bodies and exact V16seal279e4a504f39376b8b7083a95841ef28ee10416976c93bc9d69bb20b9bf1b413 remain unchanged. Local same-analyst nonblind nineteen-dimension documentary PASS_WITH_BOUND does not admit a witness or close full publication. This pair's own gate precedes Garfiel10–15/Ram15/Roswaal15 separately/full-gated before source16. Admission43objects/V41exception/datedV44–45gaps/activeV43 remain; no nonspine, replacement edition, global curation or acquisition.

Complete entering summary from6bce1604, retained verbatim as history:

```markdown
## Current source-state summary

- **Acquired/admitted Japanese main LN:** V01-V43 continuous.
- **Known published but not acquired/admitted main LN:** V44-V45.
- **Admitted translations:** none.
- **Retained non-admitted translation:** English V21, local hash reverified on resumption.
- **Admitted supplemental/EX/short-story:** none.
- **Admitted IF/alternate route:** none.
- **Admitted web novel:** none.
- **Admitted anime/audiovisual:** none.
- **Consumed into prospective main-LN analysis:** V01–V15; full V15 gate verified at98acb720. The separate V10–V15 Arc04 checkpoint is a source-free derived transaction under its own complete gate, not another consumed source. Historical Subaru10/Otto13/Emilia14 models/reviews retain exact scope/defaults/grades.
- **Next source acquisition priority:** Japanese V44 and V45 before the sequential read reaches that boundary.
- **Next analytical operation:** `BEATRICE_V01_V15_MODEL_AND_FIDELITY_REVIEW` only after the Arc04 checkpoint's own complete gate; then separate Garfiel10–15, Ram15 and Roswaal15 constructions/reviews, each full gate before the next/source16. V16 remains unopened and its exact60/10 seal unchanged.
- **Current execution state:** active continuous terminalV43. E018alive/17deaths18segments after actual rescue, three trials, two-site local release, finite chosen contract/defense, plural settlement and accepted office; reader-only Omega coda. No death18/E019, Rabbit extinction, gate/reserve repair, Rem awakening, full camp RBD/tea, origin telling/old apology or held capital reward ceremony is implied. Sourceverified Arc04 end earns a separate checkpoint, not completed models or full-series synthesis.
```

## Post-Beatrice15 Garfiel reconstruction source boundary — no new admission

The [Garfiel V10–V15 model](../05%20Character%20Analysis/REZERO_GARFIEL_TINSEL_V10_V15_CHARACTER_MODEL.md) and [separate fidelity review](../08%20Audits%20and%20Manifests/REZERO_GARFIEL_TINSEL_V10_V15_FIDELITY_REVIEW.md) implement33bundles/28eight-field rules, all seven selector axes, ordinary/recipient/Japanese/knowledge/help/failure/refusal controls,19negativecontrols and14noncanonical applications. All nineteen dimensions were actually applied at same-analyst nonblind documentary level, yielding PASS_WITH_BOUND after attributable scoped corrections. Forty-six bounded Japanese windows/140445characters revisit already-consumed V10–V15; this is not six fresh complete novel rereads, independent/runtime/held-out validation, a global grade or cure.

**Operative source-identity correction:** model§0.1/review§2 identify V11 p-005#B0183–0207's speaking/partly healed full feline as **Frederica**, not Garfiel. M131 is the accurate route; inherited M178/M236/C116-ancestry “V11 speaking/healing full tiger” labels are not valid Garfiel evidence. Actual V11 p-013 is Subaru's failed transfer; V12 human Ram treatment/V13 nonhuman tiger address/V15 human reversion before speech remain distinct. Frozen records/five owners are preserved, not silently repaired. Require person/form/event and reject the old subject conflation without inventing universal future incapacity.

All26 predecessor artifacts/five owner files/master§§2–12/formal protocol§19–21/reserved schema tail/exact V16seal279e4a504f39376b8b7083a95841ef28ee10416976c93bc9d69bb20b9bf1b413 remain unchanged. V15 retains292claims/E018alive/17deaths18segments and K495/M317/I262/R086/RT181. Historical Subaru10/Otto13/Emilia14/Beatrice15 bytes/defaults/local grades remain exact; Beatrice's full gate at6be67f9 is complete, not pending again. One integrated model plus separate review is proportional; no new field, sixth owner, independent ordinary/voice/evidence/readiness home, final specialist or global evaluator/curation work.

This pair's own complete exact-commit publication gate precedes RAM_V01_V15_MODEL_AND_FIDELITY_REVIEW, then ROSWAAL_V01_V15_MODEL_AND_FIDELITY_REVIEW after Ram's own full gate, and only then source16. Local documentary PASS_WITH_BOUND is not publication. Active continuous terminalV43/EVOLVING remain; no routine checkpoint/model pause.

### Historical entering source-state summary — complete preimage

Complete entering text from6be67f9f7f4f9ae32238576ec3df1d6d7873187d; historical, not current routing or a pending predecessor gate:

````markdown
## Current source-state summary

- **Acquired/admitted Japanese main LN:** V01-V43 continuous.
- **Known published but not acquired/admitted main LN:** V44-V45.
- **Admitted translations:** none.
- **Retained non-admitted translation:** English V21, local hash reverified on resumption.
- **Admitted supplemental/EX/short-story:** none.
- **Admitted IF/alternate route:** none.
- **Admitted web novel:** none.
- **Admitted anime/audiovisual:** none.
- **Consumed into prospective main-LN analysis:** V01–V15; full V15 gate98acb720 and separate source-free Arc04 gate6bce1604 complete. Beatrice15 model/local scoped review now implemented under its own complete publication gate, not another consumed source. Historical Subaru10/Otto13/Emilia14 pairs retain exact scope/defaults/grades.
- **Next source acquisition priority:** Japanese V44 and V45 before the sequential read reaches that boundary.
- **Next analytical operation:** `GARFIEL_V10_V15_MODEL_AND_FIDELITY_REVIEW` only after the Beatrice15 pair's own complete gate; then Ram15/Roswaal15 separately, each construction/review/full gate before the next/source16. V16 remains unopened/exact60-question/ten-forecast seal unchanged.
- **Current execution state:** active continuous terminalV43. E018alive/17deaths18segments after actual rescue, three trials, two-site local release, finite chosen contract/defense, plural settlement and accepted office; reader-only Omega coda. No death18/E019, Rabbit extinction, gate/reserve repair, Rem awakening, full camp RBD/tea, origin telling/old apology or held capital reward ceremony is implied. The separate Arc04 checkpoint is fully gated; Beatrice15 has local documentary PASS_WITH_BOUND, not independent/global/runtime validation, new primary consumption or completed full-series synthesis.
````

## Post-Garfiel15 Ram reconstruction source boundary — no new admission

The [Ram V01–V15 model](../05%20Character%20Analysis/REZERO_RAM_V01_V15_CHARACTER_MODEL.md) and [separate fidelity review](../08%20Audits%20and%20Manifests/REZERO_RAM_V01_V15_FIDELITY_REVIEW.md) now implement35retrieval bundles/28eight-field rules, all seven selector axes,18ordinary/14recipient/20knowledge/18Japanese rows,19negativecontrols and14NONCANONICAL_PROBE applications. All nineteen dimensions were actually applied at same-analyst nonblind documentary level: PASS_WITH_BOUND after four attributable repair groups. Thirty-nine contextual Japanese windows/128450characters revisit already-consumed originals; no fifteen new complete rereads, independent/runtime/held-out/global grade or cure is claimed.

Default is living E018 at Ram's latest actual V15 month-later party, p-027#B0218, beside sleeping Rem rather than Roswaal in that instant. Present care/residual bond does not restore old Rem autobiography, import E014's new lesson/Petra appraisal or provide an awake reply. Original revenge, changed self-directed rescue wish, received-and-denied love declaration, dependency, real harm, costly incomplete activation, existing green log-fire and medical gratitude without lover-selection authority remain distinct. No RBD/private soul/warded threat/trial/coda receipt, horn regrowth, completed death/resurrection, infinite aid or reciprocal-romance certificate.

**Operative Ram chronology bound:** model§0.1/review§2 retain V03 p-023#B0004–0045's nearly-seven-year account and V14 p-024#B0219–0239's nine-year oath dating with attribution. No verified unified interval/age, two-year bridge, second attack, edition cause or retcon is invented; neither local assertion is erased. C01 remains OPEN. Frozen V03/V14/five owners/master§§2–12 are preserved, not repaired. The existing Garfiel correction also remains operative: M178/M236/C116-ancestry Frederica→Garfiel speaking/healing labels are not valid Garfiel evidence.

All28 predecessor artifacts/five owners/master§§2–12/formal protocol§§19–21/reserved schema tail/exact V16seal279e4a504f39376b8b7083a95841ef28ee10416976c93bc9d69bb20b9bf1b413 remain unchanged. V15 retains292claims/E018alive/17deaths18segments and K495/M317/I262/R086/RT181. Five historical model/review pairs retain exact bytes/defaults/local grades; Garfiel15's complete gatec6c8054c is closed, not pending again. No new field, sixth owner, source-bearing extract, independent evidence/ordinary/voice/readiness home, final specialist or global evaluator/curation work.

Only after this Ram pair's own complete exact-commit publication gate execute ROSWAAL_V01_V15_MODEL_AND_FIDELITY_REVIEW, with its own actual source/design reconciliation, construction, separate nineteen-dimension review and full gate before source16. Local documentary PASS_WITH_BOUND is not publication. Active continuous terminalV43/EVOLVING and no ordinary checkpoint/model pause remain.

The first Ram source guard stopped before text when acquisition metadata changed. Removing only the appended subsequent_calibre_imports note reconstructs the historical23584-byte manifest/SHA3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314 exactly; current23822-byte SHAa17ec23885bd4730457ea50f93cd55be1d9d1df896b8b141595b98fc0b55642d is separately pinned. All15locked actual EPUB sizes/hashes/CRCs were rechecked unchanged. The three-new-work note/report does not admit/open those works, update dated gaps automatically or extend terminal43; new report/contents remain unopened.

The historical inventory/availability statements above remain dated claims, not automatically re-audited results for the three unexamined imports. The raw current acquisition-metadata hash and exactly reconstructed historical hash are distinguished; all15 selected original source identities remain unchanged. No new witness, citation edition or title is admitted.


### Entering source-state summary — complete preimage

Complete entering text from c6c8054c02e34a4acaa9aeb9b11fff7ccba1669b; historical, not current routing or a pending predecessor gate:

`````markdown
## Current source-state summary

- **Acquired/admitted Japanese main LN:** V01-V43 continuous.
- **Known published but not acquired/admitted main LN:** V44-V45.
- **Admitted translations:** none.
- **Retained non-admitted translation:** English V21, local hash reverified on resumption.
- **Admitted supplemental/EX/short-story:** none.
- **Admitted IF/alternate route:** none.
- **Admitted web novel:** none.
- **Admitted anime/audiovisual:** none.
- **Consumed into prospective main-LN analysis:** V01–V15; full V15 gate98acb720 and separate source-free Arc04 gate6bce1604 complete. Beatrice15 complete gate6be67f9 is closed; Garfiel15 model/local scoped review now implemented under its own complete publication gate, not another consumed source. Historical Subaru10/Otto13/Emilia14/Beatrice15 pairs retain exact scope/defaults/grades.
- **Next source acquisition priority:** Japanese V44 and V45 before the sequential read reaches that boundary.
- **Next analytical operation:** `RAM_V01_V15_MODEL_AND_FIDELITY_REVIEW` only after the Garfiel15 pair's own complete gate; then Roswaal15 separately, each construction/review/full gate before the next/source16. V16 remains unopened/exact60-question/ten-forecast seal unchanged.
- **Current execution state:** active continuous terminalV43. E018alive/17deaths18segments after actual rescue, three trials, two-site local release, finite chosen contract/defense, plural settlement and accepted office; reader-only Omega coda. No death18/E019, Rabbit extinction, gate/reserve repair, Rem awakening, full camp RBD/tea, origin telling/old apology or held capital reward ceremony is implied. The separate Arc04 checkpoint is fully gated; Garfiel15 has local documentary PASS_WITH_BOUND and a mandatory source-subject correction, not independent/global/runtime validation, new primary consumption or completed full-series synthesis.
`````

## Post-Ram15 Roswaal reconstruction source boundary — no new admission

The [Roswaal V01–V15 model](../05%20Character%20Analysis/REZERO_ROSWAAL_L_MATHERS_V01_V15_CHARACTER_MODEL.md) and [separate fidelity review](../08%20Audits%20and%20Manifests/REZERO_ROSWAAL_L_MATHERS_V01_V15_FIDELITY_REVIEW.md) now implement34retrieval bundles/26eight-field rules, all seven selector axes,18ordinary/14recipient/25knowledge/18Japanese rows,22negativecontrols and12NONCANONICAL_PROBE applications. All nineteen dimensions were actually applied at same-analyst nonblind documentary level: PASS_WITH_BOUND after four attributable repairs. Forty-six contextual Japanese windows/150137characters revisit already-consumed originals; no fifteen fresh complete novel rereads, independent/runtime/held-out/global grade or cure is claimed.

Default is living E018, V15 p-027#B0118–0120, returning from the isolated Subaru conversation to the month-later Milord party. Historical A16, injured A, successive bodies, E017 deaths, acute book-loss collapse and current L remain distinct. Tactical adaptability, genuine care and an actual group apology/oath do not erase the continued private teacher-restoration aim and destructive threat. Roswaal knows redo, not the death trigger; current soul continuity does not provide Subaru's discarded-loop memories, descendant consent or everyone else's private experience.

The actual review repairs neighboring frozen section/claim routes, A16's own naming preference, unsupported wine specificity and the settlement's eleven-person audience. V15 Petra/oath locators are narrowed without rewriting frozen findings. Beatrice alone receives the private soul disclosure; Subaru receives the warded threat; no general camp/villager receipt is invented. Care/dependency is not injury consent or reciprocal romance; a visible sanction is not a proved action lock.

All30 predecessor artifacts/five owners/master§§2–12/formal protocol§§19–21/reserved schema tail/exact V16seal279e4a504f39376b8b7083a95841ef28ee10416976c93bc9d69bb20b9bf1b413 remain unchanged. V15 retains292claims/E018alive/17deaths18segments and K495/M317/I262/R086/RT181. Six historical pairs retain exact bytes/defaults/local grades. Ram's nearly-seven-year/nine-year chronology remains OPEN and Garfiel's Frederica-subject correction remains mandatory. No new field, sixth owner, source-bearing extract, independent evidence/ordinary/voice/readiness home, final specialist or global evaluator/curation work is earned.

Ram15's complete gate atc6388791f678f24d21f33ed83553fc192666e499 is closed: actual full459-test exact-source audit, trusted success status, routing-current housekeeping no-op without a redundant child/audit and later clean native checks are verified. Roswaal15's own complete exact-commit publication gate still precedes V16. Local documentary PASS_WITH_BOUND is not publication. Both current map operation fields select V16 conditionally on that gate; high-waterV15/active terminalV43/EVOLVING and no ordinary checkpoint/model pause remain.

All15 actual locked originals were size/SHA/CRC rechecked unchanged; the46windows/150137characters are targeted rereads of consumed sources, not new complete-volume/image consumption. The metadata append remains exactly reconciled under both pinned hashes; new works/report remain unopened. Historical availability statements remain dated and no new edition/witness is admitted.

### Entering source-state summary — complete preimage

Complete entering text from c6388791f678f24d21f33ed83553fc192666e499; historical, not current routing or a pending predecessor gate:

``````markdown
## Current source-state summary

- **Acquired/admitted Japanese main LN:** V01-V43 continuous.
- **Known published but not acquired/admitted main LN:** V44-V45.
- **Admitted translations:** none.
- **Retained non-admitted translation:** English V21, local hash reverified on resumption.
- **Admitted supplemental/EX/short-story:** none.
- **Admitted IF/alternate route:** none.
- **Admitted web novel:** none.
- **Admitted anime/audiovisual:** none.
- **Consumed into prospective main-LN analysis:** V01–V15; full V15 gate98acb720 and separate source-free Arc04 gate6bce1604 complete. Beatrice15 complete gate6be67f9 and Garfiel15 complete gatec6c8054c are closed; Ram15 model/local scoped review now implemented under its own complete publication gate, not another consumed source. Historical Subaru10/Otto13/Emilia14/Beatrice15/Garfiel15 pairs retain exact scope/defaults/grades.
- **Next source acquisition priority:** Japanese V44 and V45 before the sequential read reaches that boundary.
- **Next analytical operation:** `ROSWAAL_V01_V15_MODEL_AND_FIDELITY_REVIEW` only after the Ram15 pair's own complete gate; its separate construction/review/full gate precedes source16. V16 remains unopened/exact60-question/ten-forecast seal unchanged.
- **Current execution state:** active continuous terminalV43. E018alive/17deaths18segments after actual rescue, three trials, two-site local release, finite chosen contract/defense, plural settlement and accepted office; reader-only Omega coda. No death18/E019, Rabbit extinction, gate/reserve repair, Rem awakening, full camp RBD/tea, origin telling/old apology or held capital reward ceremony is implied. The separate Arc04 checkpoint is fully gated; Ram15 has local documentary PASS_WITH_BOUND and an OPEN chronology bound; Garfiel's mandatory source-subject correction remains operative, not independent/global/runtime validation, new primary consumption or completed full-series synthesis.
``````

## Volume 16 consumption record — same admitted original, no new source admission

| field | exact consumed witness and boundary |
|---|---|
| source | RZ-MAIN-LN-JA-V16; Japanese mainLN; Re Zero - Volume 16.epub;10591363bytes;SHA81695f7fdb01767a705daf3011f84a20c2ec7cbba658efe173dd5fb32b7756c8;CRCpass |
| OPF/identity | item/standard.opf; ja; UUID2a614301-5660-4b20-a737-4b3866078987;77ZIPentries/23archive images; no inventedISBN/Driveobject |
| dates | electronic/first-printbasis2018-03-25; afterword2018-03 writingdate |
| source gate | structural inspection08:32:13Z followed Roswaal15's completed08:28:29Z fullgate; actual ordered reading/receipt proof completed12:25:12Z on2026-10-22, not a claim structure inspection was consumption |
| actual EOF |39/39OPFmembers,77actual windows,3805positions=3773TEXT+32orderedIMAGEreferences;22distinct original spineassets;175738returnedtextcharacters; zero missing/duplicatedpositions; narrativep-020#B0215, whole-spinep-bookwalker#B0001 |
| packaging | unreferenced23rdimage distribution advert separately inspected/excluded; no links/instructions followed or narrative admission |
| prospective boundary | exact incoming60Q/10P seal279e4a504f39376b8b7083a95841ef28ee10416976c93bc9d69bb20b9bf1b413 unchanged; outgoingV17seal53ac9eb4456e84f00e1e2c8fbeef9b2d4910dd2f873f93143652cbc3854c724e fixed before V17 |
| source-facing result | V16freeze/master/owners:340claims,292individualdispositions/60Q/10P; E019/18deaths19segments; new50K/28M/32I/18R/58RT; no inherited old model grade |
| integrity/admission | historical23584-byte manifestSHA3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314 still reconstructs exactly by removing only metadataappend from23822-byte currentSHAa17ec23885bd4730457ea50f93cd55be1d9d1df896b8b141595b98fc0b55642d; no new works/report opened |

The V16freeze§1 owns complete member coverage/locator convention. Private receipts/images remain outside staging. Actual source consumption, source-facing semantic acceptance and complete publication gate are separate. Ram chronologyOPEN/currentC116/M344 source-subject correction remain binding;32old artifacts/seven pairs exact. No V17 opening through four subsequent earned constructions/reviews/full gates.

### Exact entering source-state summary — historical preimage

````````markdown
## Current source-state summary

- **Acquired/admitted Japanese main LN:** V01-V43 continuous.
- **Known published but not acquired/admitted main LN:** V44-V45.
- **Admitted translations:** none.
- **Retained non-admitted translation:** English V21, local hash reverified on resumption.
- **Admitted supplemental/EX/short-story:** none.
- **Admitted IF/alternate route:** none.
- **Admitted web novel:** none.
- **Admitted anime/audiovisual:** none.
- **Consumed into prospective main-LN analysis:** V01–V15; full V15 gate98acb720 and separate source-free Arc04 gate6bce1604 complete. Beatrice15 gate6be67f9, Garfiel15 gatec6c8054c and Ram15 gatec6388791 are closed; Roswaal15 model/local scoped documentary review is implemented under its own complete publication gate, not another consumed source. All six historical pairs retain exact scope/defaults/grades.
- **Next source acquisition priority:** Japanese V44 and V45 before the sequential read reaches that boundary.
- **Next analytical operation:** `V16` only after Roswaal15's own complete gate; consume its admitted Japanese original in OPF order through complete text/image EOF. V16 remains unopened/exact60-question/ten-forecast seal unchanged.
- **Current execution state:** active continuous terminalV43. E018alive/17deaths18segments after actual rescue, three trials, two-site local release, finite chosen contract/defense, plural settlement and accepted office; reader-only Omega coda. No death18/E019, Rabbit extinction, gate/reserve repair, Rem awakening, full camp RBD/tea, origin telling/old apology or held capital reward ceremony is implied. The separate Arc04 checkpoint is fully gated; Roswaal15 has local documentary PASS_WITH_BOUND after four repairs; Ram's OPEN chronology and Garfiel's mandatory source-subject correction remain operative, not independent/global/runtime validation, new primary consumption or completed full-series synthesis.
````````

## Volume 17 consumption record — original admitted witness, no new admission

| field | verified source-facing state |
|---|---|
| source | RZ-MAIN-LN-JA-V17; original Japanese EPUB, Re：ゼロから始める異世界生活 17 / 長月 達平;23970413bytes/SHA063327017f7b28665388610ee7853ef11b93ad4d6a356d633c368c87792f0dc9; CRCpass,59archive entries |
| prior gate / protected boundary | Ferris16's complete gate38bfed019a665455599792a7a5da22156d930fff preceded the first V17 opening;41protected prior analytical artifacts/eleven model-review pairs remain exact |
| actual sequential coverage |21/21OPFmembers;78actually acknowledged contiguous deliveries;3780positions=3756TEXT+24orderedIMAGEreferences;167232base-text characters; no gaps/duplicates |
| visual coverage |23unique original spine image assets actually viewed; one gaiji appears twice among24references, not a duplicate new image; no unreferenced image member |
| supplemental packaging/wording coverage | separate nonspine navigation1329bytes/SHA5fcb5510636ccb78fadda8e97f9be337e56022b38f15884c91c1677cd1509f6e:13labels/104characters actually read;802unique ruby base/reading pairs in nine actual deliveries cover2769groups/3745labels, exact native reconciliation after text/image EOF |
| wording-sensitive controls | p-006#B0615 僕 is readしもべ, Capella's servants, not first-personboku; Roy's 虎爪 isこそう/finger weapon, not a newly inferred beast transformation |
| whole-source boundary | narrative ends p-006#B1105; afterword/design/promotional/jacket/colophon and final publisher asset consumed in their source positions. Historical release/promo text is not current instruction, later narrative or source admission |
| prospective integrity | exact incoming60Q/10P V17seal53ac9eb4456e84f00e1e2c8fbeef9b2d4910dd2f873f93143652cbc3854c724e unchanged; all60questions/10forecasts separately adjudicated; outgoing V18seal3cb3c253cb4ea264a72b9dc376c6d40f7aec608648c5e5a2fac97a229bcbac7d fixed after full source/review and before V18 |
| source-facing result |371claims after340individual dispositions218PRESERVE/94STRENGTHEN/20REVISE/8OPEN+31NEW; E021/20deaths21arrived segments; K601/M382/I325/R125/RT288; no Subaru death21/E022 or Arc5-end closure |
| manifest / admission | only the already recorded metadata append distinguishes current manifestSHAa17ec23885bd4730457ea50f93cd55be1d9d1df896b8b141595b98fc0b55642d from reconstructable historical23584bytes/SHA3daa190cefda6ab894f5d62ff547a93856c8133f2d4fc1cbc552b99d73c73314. No newly imported narrative/report is admitted or read |

The [V17 reading](../02%20Sequential%20Readings/REZERO_LN_V17_DEEP_READING.md) §1 owns the complete member/locator table, while its §§3–15 own source-facing argument and adjudication. Structural enumeration, assistant consumption, semantic review and full publication gate remain distinct. The reading and five specialist ledgers are synchronized with master; canonical drafting alone is not a completed V17 exact-commit gate.

### V17 bounded V13 chronology check — earlier admitted evidence only

The original V13 witness is7580833bytes/SHAf352e6bf101a26c3b0cfc35bec32677afc886315cf4082ead6bace727acb1a41, CRCpass. Actual bounded retrieval p-025#B0183–0257 and p-027#B0040–0082 checks the mother's departure/trial/scar context and Ram's explicit statement that Garfiel is fourteen that year. The ten-year references concern the earlier trial/scar experience, not an independently certified maternal-departure date. V17's agefifteen is compatible with the common year; no exact birthday, retcon, second departure or invented full chronology is supplied. This is not a complete V13 reread, new source admission or alteration of its frozen reading. Ram's separate OPEN chronology and currentC116/M344's Frederica-subject correction stay binding.

### Exact entering source-state summary — historical Ferris16 boundary

````````markdown
## Current source-state summary

- **Acquired/admitted Japanese main LN:** V01–V43 continuous; V41 bounded replacement unchanged.
- **Known dated published but unadmitted gaps:** V44–V45; no new freshness claim.
- **Admitted translation/supplement/EX/IF/WN/anime:** none. EnglishV21/archivedV31 remain nonadmitted/unopened.
- **Consumed into prospective main-LN analysis:** V01–V16; V16 source-facing/Julius16/Wilhelm16/Crusch16 complete gates are closed, latest Crusch9131ffb6. Ten prior pairs retain exact scopes/defaults/local grades. Ferris's derived model/review adds no consumed unit or current narrative claim generation; its own publication gate remains separate.
- **Next analytical operation:** V17 only after the implemented Ferris V01–V16 pair's own complete publication gate. Its separately actually applied nineteen-dimension same-analyst nonblind documentary result is PASS_WITH_BOUND, not independent/held-out/runtime/global validation. All four V16-earned constructions are implemented; exact60Q/10P seal53ac9eb4456e84f00e1e2c8fbeef9b2d4910dd2f873f93143652cbc3854c724e remains fixed.
- **Derived-use source reconciliation:** Ferris revisits51bounded Japanese deliveries/3560uniqueTEXTpositions/154558characters in already-consumed V04/V05/V06/V07/V08/V09/V10/V12/V16, original hashes/CRC checked, no image/duplicate credit. One initially context-truncated V07 delivery was reread completely in two contiguous windows before its single credit. This is not nine fresh complete novel rereads, new admission, changed original or additional current narrative claim generation. Source high-water remainsV16; all39older artifacts/five owners/current340claims/formal/reserved tails and exact V17seal remain protected. Earlier Crusch reconciliation remains historical.
- **Current execution:** active continuous terminalV43; E019 alive after square death18/19segments. Common year/travel/family history survives, later atrocity Subaru-only; narrator short-point timing not yet recognized by him. No decodedWrath, complete family repair, crystal/Puck/Rem/Gate result or full campRBD. Award/medal now retrospectively confirmed without exact enrollment/date/type.
- **Source admission and acquisition priority:** unchanged43-original lock/V41exception; V44/V45 acquisition before authorized boundary is reached, not done here. New metadata/report does not admit unread works. V17+/nonspine/new import narratives remain unopened.
````````

## Volume 18 consumption record — original admitted witness, no new admission

- **Identity:** RZ-MAIN-LN-JA-V18, Re Zero - Volume 18.epub (normalized filename is a locator);20485268bytes/SHA7cfdbbfd68d1141500df35f6cd0065545accdc50f0bb88dcbe471c2165a54584;58ZIPentries/originalCRCpass. Japanese title/edition/semantic source remain the locked original, not an advertisement's instructions.
- **Actual consumption:**21OPFmembers/73bounded actual deliveries/3772positions=3751TEXT+21IMAGEreferences/166433base-text characters, zero gaps/duplicates. All21OPFimages and one extra packaging-ad image were actually viewed:22packaged images. Narrative p-007#B0209《了》and final p-bookwalker#B0001 are reached; all afterword/design/promotional/jacket/colophon/logo text is paratext.
- **Navigation/ruby:** full1400-byte navigation/SHA700838839b0bf16985a9338ba7b89de8ec8f2d38d9deb3a398ced14dabd4d598,12labels/96characters; all571unique base/reading pairs in6actual deliveries cover1939groups/2636labels and match original raw text. Early deliveries2–6 retain honest actual-delivery acknowledgments, not a false claim that all original transient raw output was saved; no reconstructed/duplicate reading credit.
- **Entering gate:** Mimi17 source/finala453ba89260ef5d1d00a7c89fd8719f686a8add0 completed actual459discovered/executed tests, trusted exact-head reporter, source-specific completed routing-current housekeeping no-op and later native/source/protected/seal proof before V18 opening. V17's earliercfad8d70gate is independently closed. These do not certify a later V18publication head.
- **Prospective/state boundary:** exact incoming15685-byte60Q/10Pseal3cb3c253 remains literal; current377claims adjudicate371predecessors223P/110S/30R/8O+6NEW, all60Q/10P separately. LivingE021continues20deaths21arrived segments; connected leg/waking/focal shifts/independent departure add no return. No death21/E022, all-city safety, completed tower victory or restored resource is supplied.
- **Current source-facing limits:** actual pre-speech英雄幻想warning529–0569 and earlier child/adult shelter restraint582–0603 are not the later speech's universal effect. Named Fredo/sister life does not supply every parent's fate. Public Kurgan/private Theresia, contested Tome responsibility/private motives, patient refusal/hidden retry and separate mirror1003–1022allocation keep actors/audiences distinct. Literalリブレ・フエルミ/屍兵reading and Frederica-subject control remain.
- **No opening/admission through paratext:** V19/OVA/collection/booklet/rehost references were read as packaged paratext, not their advertised narrative or directions. JapaneseV01–V43/V41exception and datedV44/V45gaps stay unchanged. The metadata-only subsequent-import note is append-only against the historical manifest and does not admit/open those works. This is not a fresh all43object audit or complete-to-date bibliography.

## V19 actual source consumption — RZ-MAIN-LN-JA-V19

Exact admitted original `Re Zero - Volume 19.epub`,23535212bytes/SHA256 `d05c621e02a9767a6ca44e792f03dbec33c62db62467f3c1f3386eb65fc1db5d`, ZIP CRCpass; Japanese/KADOKAWA/長月達平/大塚真一郎,2019-03-27colophon. Actual full correspondence covers23OPFmembers/3710positions=3671TEXT+39IMAGEreferences,55TEXTdeliveries/165170base characters,25distinct original assets actually viewed in29calls,2navigation resources and all2187ruby groups/2877reading labels occurrence-by-occurrence after their base contexts. Sixty incoming questions/ten forecasts and377claims are individually reconciled;393current claims/five-owner state and qualitative readiness require this transaction's complete gate.

Regulus's private descent and later wife waking are different focalizations: private terminal irony ends p-008#B0158, wife waking beginsB0160. The declined caravan marriage invitation differs from a counterfactual returned-home family, earlier paid-tip amulet from later illness. Narrator names Anastasia; incomplete mechanics is no alternative operator. Advertisements/design/afterword remain packaged paratext, without V20/adaptation/supplement admission or current release-data claims. No all43fresh object audit or newly read import report is implied.

## V20 actual source consumption — RZ-MAIN-LN-JA-V20

The exact Japanese V20 original is23273776bytes/SHAd9959f536e55ad096a5fcd2b86670d25391230034fa9361438a76f0893e7f7a7, ZIP CRCpass. Actual reading reaches25OPFmembers/3992positions=3969TEXT+23IMAGEreferences/155377basecharacters,58original offers including48TEXT-containing,22distinct packaged original assets actually viewed,2navigation resources and2192contextual ruby groups/3039rt labels/598unique pairs in11deliveries. Clipped output was recovered before actual-read credit. Correspondence SHA0beb7f06e8e98318fe8c8d0db09d2baa34311765e103d74ebba4185bbcf03a65 binds original XML/base/image/nav/ruby; identity/count proof does not certify semantic attention. Narrow postEOF checks revisit already consumed V20 only; no fresh whole-volume credit.

The Pristella fronts conclude, Kurgan dissolves and Theresia briefly actually recognizes/touches/answers Wilhelm before ashes, while the family rupture worsens. Beatrice/Mimi are awake with resource/injury limits; Ricardo's right forearm and Julius's public name remain lost. True partial farewell does not inform Subaru of the whole family catastrophe. Anastasia's body/current scarf operator/human mind have different knowledge and agency; the emergency promise has positive narrative support, but the fifth return is stuck. Al's private counts stay attributed, Puck lacks sufficient mana and Rem has no new waking. Custody is local; escort, new ice preservation and five-person Sage journey remain unperformed. Emilia's consultation promise is prospective, with no unshown later breach.

The inspected original afterword explicitly completes Arc5. Advertisements, design notes, jacket/colophon and nav remain their own source planes. No supplement/adaptation/new import, later novel, fresh all43object audit or current publication-freshness check is claimed.

## Current source-state summary

- **Admitted:** unchanged Japanese mainLN V01–V43/V41exception; datedV44–V45gaps, no extra witness.
- **Actually consumed / gate:** Verified integrated sequential high-water remains V20; V20/PR360 and Arc05/PR363 full gates are CLOSED. Theresia20 full publication/integration gate CLOSED through PR364: source865c7b2aefe8ea4f304940737fb56dd7c60d897f, actual merge172738f4faaa3fabdf5e2a12098b9f893cb96469. Source/main audits40646416400/40654705975 each actually executed all479discovered unique tests with zero nonpasses and trusted statuses57444563696/57448538103. Source-specific housekeeping40647268558 completed every step with the actual source865c7b2a and a verified no-op. Later original/project/protected/seal/native verification passed; input main6e50c633339b9e2b2d569d0f0eea53a7290cdc16 retains exact Re:Zero/control correspondence without a separately claimed exact6e50audit.
- **Current state:** V20 is actually source-complete at423claims:393individual predecessors208PRESERVE/141STRENGTHEN/36REVISE/8OPEN plus30NEW; all60incoming questions/10forecasts separately adjudicated. Five sole owners: eventV2.7/E021/20Subaru deaths/21arrived segments, knowledgeV2.7/K761, mechanicsV1.16/M482, institutionV1.20/I403, relationshipV1.14/R171/RT406. New56K/40M/24I/16R/43RT;155individual relationship decisions advance65/preserve90literally, retain all363oldRT/ancestry/full affected preimages. MasterV1.40owns current claims,37advanced person rows/16new differentiated person-or-phase rows,22ordinary/23Japanese observations, prospects and qualitative readiness. Counts identify traceability rather than maturity or fidelity.
- **Protected / use:** All57entering protected artifacts and sixteen historical model scopes/defaults/local documentary grades remain exact. The complete current423claim rows remain byte-exact in the already corrected Arc05 citation state; no narrative claim generation, owner, field or global grade is added. The sealed17606-byte V21 whole body and older incomingV19/V20 prospects remain exact. V20 TEXT p-011afterword, V19 Subaru-pause attribution and Garfiel's denial of kinship to Gallek remain binding; Ram chronologyOPEN, C116/M344Frederica and Roswaal source/recipient/agency bounds are retained. Reinhard-specific recovery revisited15already-consumed originals in216actually read bounded deliveries,9386unique positions/5420contextual ruby groups and15viewed original illustrations. This is targeted reuse, not15new whole-volume readings or a new witness admission; source pins/counts do not certify semantic attention.
- **Prospective / next:** IncomingV20whole body17355bytes/SHAbc9edf56ab9f39d8c87eab9a2f152df6c1f329c9bc3713339ded080669aac718 and older incomingV19c69body remain exact. The complete outgoing60V21questions/10forecasts were sealed after actual saved-content/name-reference acceptance. Finalized2026-10-27T08:16:54.938443Z, whole body17606bytes/SHA256fb062dd9b5672f52332bccf035cd72c2a40aacbcbf1bbfe89d6a1ae737b85926; literal once in master section12 and frozenV20 section16. All60questions/10forecasts stay unchanged through the Arc5, Theresia, Reinhard and Felt gates. Preserve the sealed body through every intervening earned derived operation. V21+/nonspine/import narratives remain unopened; source43/V41exception/datedgaps are unchanged. The seventeenth model, REINHARD_V01_V20_MODEL_AND_FIDELITY_REVIEW, is IMPLEMENTED at local PASS_WITH_BOUND_SAME_ANALYST_NONBLIND_DOCUMENTARY after complete saved-content/name-reference acceptance and actually applied19dimensions/36controls/10NONCANONICAL_PROBE families/3matched-recipient variants, with18saved-model repairs read back. Its own full publication/integration gate remains PENDING. The next permitted step is that gate; only after closure: FELT_V01_V20_MODEL_AND_FIDELITY_REVIEW/own full gate → sealed V21. Felt remains EARNED_UNIMPLEMENTED/UNGRADED. Continue through admittedV43 and the mandatory terminal architecture/state/role-gap/acquisition review; CI owns merges.
- **Storage / controls:** exact historical claim generations have original-heading archive routers, unchanged relative-link base and native inverses; no new owner, field, formal dimension or relaxed limit.

### Exact entering V17/Mimi source summary — historical

````markdown
## Current source-state summary

- **Acquired/admitted Japanese main LN:** V01–V43 continuous; the bounded V41 replacement is unchanged.
- **Known dated published but unadmitted gaps:** V44–V45; no new complete-to-date or freshness claim.
- **Admitted translation/supplement/EX/IF/WN/anime:** none. Retained EnglishV21/archivedV31 remain nonadmitted/unopened.
- **Verified committed consumed horizon:** V01–V17. V17 full text/image/navigation/ruby/371claim transaction completed its exact full gate atcfad8d70e5371e86ca73611100aa3d605106a6f2; the map now records verifiedV17. Eleven earlier model/review full gates and42 entering protected artifacts remain exact.
- **Derived operation now implemented:** [Mimi V01–V17 model](../05%20Character%20Analysis/REZERO_MIMI_V01_V17_CHARACTER_MODEL.md) and [separate review](../08%20Audits%20and%20Manifests/REZERO_MIMI_V01_V17_FIDELITY_REVIEW.md), actually applied19dimensions at PASS_WITH_BOUND_SAME_ANALYST_NONBLIND_DOCUMENTARY.35bounded earlier-source deliveries/1289positions=1288TEXT/55669base characters plus one image reference; not six new whole-volume reads, a new image view, new claim generation or source admission. Six original size/hash/CRC rechecks preserve the admitted identities.
- **Next source operation:** V18 only after this Mimi pair's own complete publication/readback/exact-head full audit/housekeeping/later-native gate; no independent/runtime/global result is implied by local documentary acceptance.
- **Prospect:** exact60Q/10P V18 body15685UTF-8bytes/SHA3cb3c253cb4ea264a72b9dc376c6d40f7aec608648c5e5a2fac97a229bcbac7d remains fixed. Derived retrieval does not alter it or admit later source.
- **Current execution:** active continuous terminalV43; E021/20deaths21arrived segments. Subaru's severed thigh/black-blood/flame aftermath and Emilia's coercive captivity remain unresolved. Mimi remains living/unconscious under nonclosing-wound treatment/physical hemostasis/risky sharing, not stable/cured or available for a new reply/assent.
- **Controls and exclusions:** current371claims/five owners, all42 entering freezes/eleven earlier scopes/defaults/grades, Ram chronologyOPEN, C116/M344 Frederica-subject and Roswaal qualifiers remain. Garfiel's V17 reconciliation does not rewrite his V10–V15 pair. V18+/nonspine/new import narrative remains unopened; acquisition/report is not admission or automatic extension beyondV43.
````

### V19 source maintenance preserves the entering postV18 current summary — exact historical input

Earlier current/pending labels retain their V18/input date; they are not current V19 work orders.

````````````````markdown
- **Actual consumed source horizon:** verified V18; source4f6a7dafc097f4194b20c7f2868bbc85534b8bb8 completed its full gate through PR323/integratedmain10576e0dace0d2fe888f28357e9ed6dc95846c15. Source/main479-test audits, completed source-specific housekeeping and later native/source/protected/seal checks passed. All45entering protected artifacts/twelve earlier pair scopes/defaults/local grades remain exact; earlier source/model gates are closed.

- **Current owners/readiness:**377claims, E021/20deaths21segments, K654/M408/I353/R138/RT327; five specialist owners keep exact analytical records/history while their current-status paragraphs are synchronized; master owns person/ordinary/Japanese/questions/readiness. The thirteenth pair, [Priscilla V01–V18 model](../05%20Character%20Analysis/REZERO_PRISCILLA_V01_V18_CHARACTER_MODEL.md)/[separate review](../08%20Audits%20and%20Manifests/REZERO_PRISCILLA_V01_V18_FIDELITY_REVIEW.md), is implemented at MONOGRAPH_READY/local PASS_WITH_BOUND_SAME_ANALYST_NONBLIND_DOCUMENTARY after13grouped findings; own publication gate pending, no independent/held-out/runtime/global grade.

- **Bounded reconciliation, no admission:**66contextual deliveries in already-consumed Japanese originals cover3302unique positions=3300TEXT+2IMAGEreferences/145613base-text/5855ruby-reading characters; five selected original images were actually viewed. Exact size/hash/CRC and locus correspondence were checked. This is neither fresh whole-volume consumption nor a new source unit/admission/claim generation. Actual19dimensions/28controls/8NONCANONICAL_PROBE applications and complete saved-content/name-reference review support only the scoped local result.

- **Next operation:** close the implemented Priscilla pair's own complete publication gate, then V19. Default remains accepted Fourth assignment/collective departure with Liliana; no separate Priscilla tower arrival/battle/result shown. OutgoingV19body60Q/10P/17236bytes/SHAc69ce35c1af024204a354e95692137007d52b10c7b3d3613d13da13ef50c5ede stays prospective. V19+/nonspine/new import narratives remain unopened.

- **Execution/controls:** activecontinuousV43/terminal review; no ordinary pause, source extension, global grade or final specialist. Ram chronologyOPEN, C116/M344Frederica-subject/Roswaal qualifications and all protected history/seals remain. Native size/inverse and later publication checks remain distinct from semantic acceptance.
````````````````


## Liliana V01-V19 routing maintenance - superseded entering fragments

These exact fragments record the entering V19/pending-source status. They are historical preimages, not current work orders, grades or permission to open V20. The live replacements above govern this derived operation.

### Entering fragment: complete live source-state summary

````````````````markdown
## Current source-state summary

- **Admitted:** unchanged Japanese mainLN V01–V43; boundedV41replacement; no admitted translation/supplement/EX/IF/WN/adaptation. DatedV44/V45gaps are not a new freshness claim.
- **Actual consumed source horizon:** V19 fully consumed and individually analyzed; own complete transaction gate remains required. Verified integrated sequential high-water remainsV18; Priscilla thirteenth pair completed PR326/source8a6a6f85/integratedmain6c181f53dbdfc857bf3994c10459c5819da130ea with actual exact-source/main479-test audits, completed source-specific housekeeping and later native proof. All47entering artifacts/thirteen historical scopes/defaults/local grades remain exact.
- **Current owners/readiness:** 393claims; eventV2.3/E021/20Subaru deaths/21segments, knowledgeV2.3/K705, mechanicsV1.12/M442, institutionV1.16/I379, relationshipV1.10/R155/RT363. All138entering relationships have24advance/114literal-preserve decisions;17newR/36newRT preserve all327older transitions/ancestry/preimages. Master owns32advanced person rows/one bounded Dainas case/24ordinary/21Japanese/prospects/readiness. Liliana V01–V19 and Regulus V01–V19 earn integrated constructions/separate actually applied19-dimension reviews, neither implemented/graded here. No independent/runtime/global result or new field/owner/index follows.
- **Consumption versus bounded revisits:** V19actual23OPFmembers/3710positions=3671TEXT+39IMAGEreferences/165170base-text characters/55TEXTdeliveries,25distinct assets actually viewed/29calls,2navigation resources and2187ruby groups/2877labels occurrence-by-occurrence are complete. Subsequent source-local checks revisit only already consumed originals and add no fresh whole-volume credit or new admission; native identity/count proof does not certify semantic attention.
- **Next operation and prospect:** V19complete publication/integration gate → LILIANA_V01_V19_MODEL_AND_FIDELITY_REVIEW/own full gate → REGULUS_V01_V19_MODEL_AND_FIDELITY_REVIEW/own full gate → unchanged final prospective V20 → sequential admitted units throughV43 → mandatory terminal architecture/state/role-gap/acquisition review. Neither earned new construction/review is implemented or graded here. CI handles merges; no ordinary unit/model pause. IncomingV19body17236bytes/SHAc69ce35c1af024204a354e95692137007d52b10c7b3d3613d13da13ef50c5ede stays literal; outgoing60V20Q/10Pseal follows actual complete saved-content acceptance and remains fixed through both derived gates. V20+/nonspine/import narratives stay unopened.
- **Execution/controls:** activecontinuousV43plus mandatory terminal architecture/state/role-gap/acquisition review. Source43/V41exception/datedgaps unchanged; Ram chronologyOPEN, C116/M344Frederica/C095Gallek/Roswaal bounds and historical grades/seals remain. No Arc5end/final specialist or published-series completion; semantic/native/publication gates are distinct.


````````````````


## PR341 review corrections - exact entering current fragments

These complete fragments are superseded historical preimages of the first PR341 source. Current V1.1/reassessment routing above governs; neither its old verdict nor old pending work order certifies the corrected head.

### Entering fragment: current model1.1 confidence/reassessment binding

````````````````markdown
- **Current owners/readiness:** 393claims; eventV2.3/E021/20Subaru deaths/21segments, knowledgeV2.3/K705, mechanicsV1.12/M442, institutionV1.16/I379, relationshipV1.10/R155/RT363. All138entering relationships have24advance/114literal-preserve decisions;17newR/36newRT preserve all327older transitions/ancestry/preimages. Master owns32advanced person rows/one bounded Dainas case/24ordinary/21Japanese/prospects/readiness. The fourteenth pair, Liliana V01-V19, is IMPLEMENTED at local PASS_WITH_BOUND_SAME_ANALYST_NONBLIND_DOCUMENTARY after an actual separate19-dimension review,26individual negative controls,8NONCANONICAL_PROBE applications and3matched-recipient variants; two grouped model findings produced five exact substantive edits, plus one review-only independence-wording clarification. Its own complete publication/integration gate remains PENDING.
````````````````


## Regulus V01-V19 routing maintenance - superseded entering fragments

These exact entering fragments are historical preimages at their original relative-link base. Their earlier pending/unimplemented instructions do not govern current work. The live replacements above record Liliana closure, Regulus local acceptance and its own still-pending full gate before unopened V20.

### Entering fragment: current Liliana closure / Regulus local-result binding and work order

````````````````markdown
- **Next operation and prospect:** Close the complete publication/integration gate for the implemented Liliana pair, then REGULUS_V01_V19_MODEL_AND_FIDELITY_REVIEW with its separate full gate, then the unchanged final prospective V20, sequential admitted units throughV43, and the mandatory terminal architecture/state/role-gap/acquisition review. Regulus remains earned but unimplemented/ungraded. CI handles merges; no ordinary unit/model pause. IncomingV19body17236bytes/SHAc69ce35c1af024204a354e95692137007d52b10c7b3d3613d13da13ef50c5ede stays literal; outgoing60V20Q/10Pwhole body17355bytes/SHAbc9edf56ab9f39d8c87eab9a2f152df6c1f329c9bc3713339ded080669aac718 remains fixed through both derived gates. V20+/nonspine/import narratives stay unopened.
````````````````

### Entering fragment: current Liliana closure / Regulus local-result binding and work order

````````````````markdown
- **Current owners/readiness:** 393claims; eventV2.3/E021/20Subaru deaths/21segments, knowledgeV2.3/K705, mechanicsV1.12/M442, institutionV1.16/I379, relationshipV1.10/R155/RT363. All138entering relationships have24advance/114literal-preserve decisions;17newR/36newRT preserve all327older transitions/ancestry/preimages. Master owns32advanced person rows/one bounded Dainas case/24ordinary/21Japanese/prospects/readiness. The fourteenth model, Liliana V01-V19 generationV1.1, is IMPLEMENTED at local PASS_WITH_BOUND_SAME_ANALYST_NONBLIND_DOCUMENTARY under the [current scoped reassessment](../08%20Audits%20and%20Manifests/REZERO_LILIANA_V01_V19_FIDELITY_REASSESSMENT_01.md). Initial F1/F2 produced five source-route/knowledge edits; publication findingF3 added explicit Confidence/rationale to all22rules (19HIGH/3MEDIUM). The reassessment actually reapplied all19dimensions/26original controls/eight original NONCANONICAL probe families and added three NONCANONICAL calibration cases; the three matched-recipient variants remain. The original frozen review stays byte-exact and binds modelV1.0, whose assessment missed this contract defect. Its old result does not certify V1.1. The corrected-head full publication/integration gate remains PENDING.
````````````````

### Entering fragment: current Liliana closure / Regulus local-result binding and work order

````````````````markdown
- **Actual consumed source horizon:** Verified integrated sequential high-water is V19: PR332/source298adfed8db47742692bb0a81bd9a8bf74603bfe/integratedmain2f77b3877760403413fd45de6564ce018cedaf66 completed exact source/main479-test audits, source-specific housekeeping and later native/source/protected/seal proof. All48entering protected artifacts/thirteen historical pair bytes, source scopes, defaults and local documentary grades remain exact. The new Liliana result is local same-analyst nonblind documentary acceptance, with no independent, held-out, runtime or global grade.
````````````````

## V20 source maintenance exact entering summary

Complete changed entering fragments retain their original source/input horizon and link base. Historical pending labels do not reopen subsequently closed gates.

### V20 current consumption and complete live source summary

````````````````markdown
## Current source-state summary

- **Admitted:** unchanged Japanese mainLN V01-V43; boundedV41replacement; no admitted translation/supplement/EX/IF/WN/adaptation. DatedV44/V45gaps are not a new freshness claim.
- **Actual consumed source horizon:** Verified integrated sequential high-water is V19: PR332/source298adfed8db47742692bb0a81bd9a8bf74603bfe/integratedmain2f77b3877760403413fd45de6564ce018cedaf66 completed exact source/main479-test audits, source-specific housekeeping and later native/source/protected/seal proof. All51entering protected artifacts/fourteen preceding person-model scopes, defaults and local documentary grades remain exact. The new Regulus result is local same-analyst nonblind documentary acceptance, with no independent, held-out, runtime or global grade.
- **Current owners/readiness:** 393claims; eventV2.3/E021/20Subaru deaths/21segments, knowledgeV2.3/K705, mechanicsV1.12/M442, institutionV1.16/I379, relationshipV1.10/R155/RT363. All138entering relationships have24advance/114literal-preserve decisions;17newR/36newRT preserve all327older transitions/ancestry/preimages. Master owns32advanced person rows/one bounded Dainas case/24ordinary/21Japanese/prospects/readiness. The fourteenth model, Liliana V01-V19 generationV1.1, is IMPLEMENTED at local PASS_WITH_BOUND_SAME_ANALYST_NONBLIND_DOCUMENTARY under the [current scoped reassessment](../08%20Audits%20and%20Manifests/REZERO_LILIANA_V01_V19_FIDELITY_REASSESSMENT_01.md). Initial F1/F2 produced five source-route/knowledge edits; publication findingF3 added explicit Confidence/rationale to all22rules (19HIGH/3MEDIUM). The reassessment actually reapplied all19dimensions/26original controls/eight original NONCANONICAL probe families and added three NONCANONICAL calibration cases; the three matched-recipient variants remain. The original frozen review stays byte-exact and binds modelV1.0, whose assessment missed this contract defect. Its old result does not certify V1.1. The corrected Liliana full publication/integration gate is CLOSED through PR341: final source6bf3e58671f9f8b1435e7fc8d546e9f17b3f2221, actual merge2557b34b6828a44dd29096be6f2d30ac7b32c107; source/main audits40268284204/40268824063 actually executed all479discovered tests with zero nonpasses, source-specific housekeeping40268809148 completed, and later native/source/protected/seal verification passed. Captured input main33ff979c retains exact Re:Zero/control correspondence; no exact33ff audit is claimed. The fifteenth model, Regulus V01-V19 generationV1.0, and [separate applied review](../08%20Audits%20and%20Manifests/REZERO_REGULUS_V01_V19_FIDELITY_REVIEW.md) are IMPLEMENTED at local PASS_WITH_BOUND_SAME_ANALYST_NONBLIND_DOCUMENTARY. The [integrated model](../05%20Character%20Analysis/REZERO_REGULUS_V01_V19_CHARACTER_MODEL.md) has22conditional rules with explicit Confidence/rationale (19HIGH/3MEDIUM); the review actually applies all19dimensions/28controls/six NONCANONICAL_PROBE families after two draft repairs. Both expose frozen V19-B11 attribution erratumH1: Subaru supplies the pause analogy, not Regulus; frozen reading bytes remain exact. Default `V19_E021_TERMINAL_DROWNING_NARRATED_NO_CURRENT_LIVING_REPLY` permits no current living answer. Regulus own full publication/integration gate remains PENDING before unchanged V20; no independent, held-out, runtime or global grade follows.
- **Consumption versus bounded revisits:** V19actual23OPFmembers/3710positions=3671TEXT+39IMAGEreferences/165170base-text characters/55TEXTdeliveries,25distinct assets actually viewed/29calls,2navigation resources and2187ruby groups/2877labels occurrence-by-occurrence remain complete. Liliana-specific initialization actually revisited3392unique selected positions=3370TEXT+22IMAGEreferences in44received/read deliveries across already-consumed V04/V10/V16-V19, including2036contextual ruby groups; six distinct source assets were actually viewed. These are bounded revisits, not six fresh whole-volume readings, additional source consumption or admission; count/hash correspondence does not certify semantic attention.
- **Next operation and prospect:** Close the complete publication/integration gate for the implemented Regulus V01-V19 model and separate review, then open V20 against the unchanged finalized prospective body and continue sequentially through V43 plus the mandatory terminal architecture/state/role-gap/acquisition review. Regulus is locally PASS_WITH_BOUND_SAME_ANALYST_NONBLIND_DOCUMENTARY; its own full gate remains PENDING. CI handles merges; no ordinary unit/model pause. IncomingV19body17236bytes/SHAc69ce35c1af024204a354e95692137007d52b10c7b3d3613d13da13ef50c5ede stays literal; outgoing60V20Q/10Pwhole body17355bytes/SHAbc9edf56ab9f39d8c87eab9a2f152df6c1f329c9bc3713339ded080669aac718 remains fixed through both derived gates. V20+/nonspine/import narratives stay unopened.
- **Execution/controls:** Ram chronologyOPEN, C116/M344Frederica/C095Gallek/Roswaal bounds and historical grades/seals remain. No Arc5end/final specialist or published-series completion; semantic/native/publication gates are distinct.

````````````````

## Arc05 routing and citation maintenance — exact entering fragments, 2026-10-28

These complete prior lines are historical preimages from input2c4dee68. They retain their original relative-link base and do not govern current gate status or source routing. The V20 afterword image route below is an explicitly superseded locator; Arc05 section0 and the live TEXT p-011 route govern. No historical formula, decision or seal is silently repaired.

```text
generation: V0.39
- **Actually consumed / gate:** Entering verified integrated sequential high-water is V19. The Liliana19 and Regulus19 full gates CLOSED before V20 source opening. Regulus PR351 final sourceeedd65c31b35f060a5fe744b1689dadb7569bfef/actual mergee4d8b828a35c4ec8043fae0d6f1bdeaacdadd5da completed all479discovered/actually executed tests on source/main, zero nonpasses, trusted status and completed source-specific housekeeping; later native/source/protected/seal verification passed. Base81ec13bbdce71fdbb44d6bbad45f680925781f84 preserves the Re:Zero/control projection without a claimed exact81ec audit. V20 requires its own full gate.
- **Current state:** V20 is actually source-complete at423claims:393individual predecessors208PRESERVE/141STRENGTHEN/36REVISE/8OPEN plus30NEW; all60incoming questions/10forecasts separately adjudicated. Five sole owners: eventV2.4/E021/20Subaru deaths/21arrived segments, knowledgeV2.4/K761, mechanicsV1.13/M482, institutionV1.17/I403, relationshipV1.11/R171/RT406. New56K/40M/24I/16R/43RT;155individual relationship decisions advance65/preserve90literally, retain all363oldRT/ancestry/full affected preimages. MasterV1.37owns current claims,37advanced person rows/16new differentiated person-or-phase rows,22ordinary/23Japanese observations, prospects and qualitative readiness. Counts identify traceability rather than maturity or fidelity.
- **Protected / use:** All53entering protected analytical artifacts and fifteen historical model scopes/defaults/local documentary grades remain exact. Liliana1.1/current reassessment remains distinct from its original frozen1.0review; Regulus19 retains terminal no-current-living-reply and visible H1 attribution correction: Subaru offers the pause analogy. V20 reconciliation does not extend an older grade. Ram chronology remainsOPEN; C116/M344 identifies Frederica as the old full-feline speaker/healing subject, C095 retains Gallek's actual private denial, and Roswaal source/recipient/agency qualifications remain binding.
- **Prospective / next:** IncomingV20whole body17355bytes/SHAbc9edf56ab9f39d8c87eab9a2f152df6c1f329c9bc3713339ded080669aac718 and older incomingV19c69body remain exact. The complete outgoing60V21questions/10forecasts were sealed after actual saved-content/name-reference acceptance. Finalized2026-10-27T08:16:54.938443Z, whole body17606bytes/SHA256fb062dd9b5672f52332bccf035cd72c2a40aacbcbf1bbfe89d6a1ae737b85926; literal once in master section12 and frozenV20 section16. All60questions/10forecasts stay unchanged through the Arc5, Theresia, Reinhard and Felt gates. Preserve the sealed body through every intervening earned derived operation. V21+/nonspine/import narratives remain unopened; source43/V41exception/datedgaps are unchanged. After the complete V20 publication/integration gate: ARC_05_CHECKPOINT/own full gate → THERESIA_V01_V20_MODEL_AND_FIDELITY_REVIEW/own full gate → REINHARD_V01_V20_MODEL_AND_FIDELITY_REVIEW/own full gate → FELT_V01_V20_MODEL_AND_FIDELITY_REVIEW/own full gate → sealed V21. All four derived duties are EARNED_UNIMPLEMENTED/UNGRADED. Continue the admitted sequence throughV43 and the mandatory terminal architecture/state/role-gap/acquisition review; CI owns merges.
```

## Theresia20 routing maintenance — exact entering fragments, 2026-10-28

These complete prior lines are historical preimages from actual merge1dc0e53de, retained at their original relative-link base. They do not govern current gate/model status. No older narrative row, grade, seal or source record is silently rewritten.

```text
generation: V0.40
- **Actually consumed / gate:** Verified integrated sequential high-water is V20. Its full publication/integration gate CLOSED through PR360: final source968b75ea75394fc3eed2976456b21ab6b005bd12, actual merge70efdcaf6ace3fd53fd94fb9c082c4abe9808fd1; source/main audits40473399291/40502066721 actually executed all479discovered unique tests with zero nonpasses and trusted status. Source-specific housekeeping40474402558 completed every step with actual SOURCE_SHA968b75ea75394fc3eed2976456b21ab6b005bd12 and a verified no-op. Later native/source/protected/seal checks passed. Input2c4dee68a5be9dd7a4f14ec83028b9a9c4a6f83e preserves the Re:Zero/control projection without a claimed exact2c4 audit.
- **Current state:** V20 is actually source-complete at423claims:393individual predecessors208PRESERVE/141STRENGTHEN/36REVISE/8OPEN plus30NEW; all60incoming questions/10forecasts separately adjudicated. Five sole owners: eventV2.5/E021/20Subaru deaths/21arrived segments, knowledgeV2.5/K761, mechanicsV1.14/M482, institutionV1.18/I403, relationshipV1.12/R171/RT406. New56K/40M/24I/16R/43RT;155individual relationship decisions advance65/preserve90literally, retain all363oldRT/ancestry/full affected preimages. MasterV1.38owns current claims,37advanced person rows/16new differentiated person-or-phase rows,22ordinary/23Japanese observations, prospects and qualitative readiness. Counts identify traceability rather than maturity or fidelity.
- **Protected / use:** All54entering protected artifacts, fifteen historical model scopes/defaults/local documentary grades and the sealed V21 whole body remain exact. The current423 formulations/dispositions/reasons/older ancestry remain unchanged; five declared V20 afterword citation slices are corrected with full prior rows preserved. Event's arc-boundary row and K760 receive the same TEXT p-011#B0001–B0006 correction. FrozenV20 stays exact; its nonexistent p320 image reference is superseded by the attributable Arc05§0 erratum. Garfiel denies kinship to Gallek, who supplies no exclusion order; Ram chronologyOPEN, C116/M344Frederica and Roswaal source/recipient/agency bounds remain binding.
- **Prospective / next:** IncomingV20whole body17355bytes/SHAbc9edf56ab9f39d8c87eab9a2f152df6c1f329c9bc3713339ded080669aac718 and older incomingV19c69body remain exact. The complete outgoing60V21questions/10forecasts were sealed after actual saved-content/name-reference acceptance. Finalized2026-10-27T08:16:54.938443Z, whole body17606bytes/SHA256fb062dd9b5672f52332bccf035cd72c2a40aacbcbf1bbfe89d6a1ae737b85926; literal once in master section12 and frozenV20 section16. All60questions/10forecasts stay unchanged through the Arc5, Theresia, Reinhard and Felt gates. Preserve the sealed body through every intervening earned derived operation. V21+/nonspine/import narratives remain unopened; source43/V41exception/datedgaps are unchanged. ARC_05_CHECKPOINT is IMPLEMENTED with local saved-content/name-reference acceptance and28bounded consolidation propositions; its own publication/integration gate remains PENDING. After that complete gate: THERESIA_V01_V20_MODEL_AND_FIDELITY_REVIEW/own full gate → REINHARD_V01_V20_MODEL_AND_FIDELITY_REVIEW/own full gate → FELT_V01_V20_MODEL_AND_FIDELITY_REVIEW/own full gate → sealed V21. The three person constructions/reviews remain EARNED_UNIMPLEMENTED/UNGRADED. Continue through admittedV43 and the mandatory terminal architecture/state/role-gap/acquisition review; CI owns merges.
```

## Reinhard20 routing maintenance — exact entering fragments, 2026-10-28

These complete prior fragments are historical inputs at6e50c633, preserved at the same relative-link base. Old pending gates/counts and the old Gallek-subject wrapper do not govern current use. New current routing records the verified Theresia closure and bounded Reinhard acceptance; older source facts/grades/seals stay exact.

```text
generation: V0.41
- **Actually consumed / gate:** Verified integrated sequential high-water remains V20; its PR360 full gate is CLOSED. ARC_05_CHECKPOINT full publication/integration gate CLOSED through PR363: final source01c54c2a8b44a818d7269511701368e437da0aae, actual merge1dc0e53de055fea465497919fd9896f74a555a3a; source/main audits40619126526/40630673297 each actually executed all479discovered unique tests with zero nonpasses and trusted statuses57431889162/57437199885. Source-specific housekeeping40619787025 completed every step with actual SOURCE_SHA01c54c2a8b44a818d7269511701368e437da0aae and a verified no-op. Later native/original/project/protected/seal verification passed at actual merge/current main1dc0e53de.
- **Current state:** V20 is actually source-complete at423claims:393individual predecessors208PRESERVE/141STRENGTHEN/36REVISE/8OPEN plus30NEW; all60incoming questions/10forecasts separately adjudicated. Five sole owners: eventV2.6/E021/20Subaru deaths/21arrived segments, knowledgeV2.6/K761, mechanicsV1.15/M482, institutionV1.19/I403, relationshipV1.13/R171/RT406. New56K/40M/24I/16R/43RT;155individual relationship decisions advance65/preserve90literally, retain all363oldRT/ancestry/full affected preimages. MasterV1.39owns current claims,37advanced person rows/16new differentiated person-or-phase rows,22ordinary/23Japanese observations, prospects and qualitative readiness. Counts identify traceability rather than maturity or fidelity.
- **Protected / use:** All55entering protected artifacts and fifteen historical model scopes/defaults/local documentary grades remain exact. The complete current423claim rows remain byte-exact in the already corrected Arc05 citation state; no narrative claim generation, owner, field or global grade is added. The sealed17606-byte V21 whole body and older incomingV19/V20 prospects remain exact. Existing V20 TEXT p-011 afterword/V19 Subaru-pause attribution/Garfiel-denial-to-Gallek corrections remain binding; Ram chronologyOPEN, C116/M344Frederica and Roswaal source/recipient/agency bounds are retained. Theresia-specific checks revisited already-consumed V07/V08/V09/V16/V20 without fresh whole-volume or new admission credit; V18/V19 identity pins did not open their narrative.
- **Prospective / next:** IncomingV20whole body17355bytes/SHAbc9edf56ab9f39d8c87eab9a2f152df6c1f329c9bc3713339ded080669aac718 and older incomingV19c69body remain exact. The complete outgoing60V21questions/10forecasts were sealed after actual saved-content/name-reference acceptance. Finalized2026-10-27T08:16:54.938443Z, whole body17606bytes/SHA256fb062dd9b5672f52332bccf035cd72c2a40aacbcbf1bbfe89d6a1ae737b85926; literal once in master section12 and frozenV20 section16. All60questions/10forecasts stay unchanged through the Arc5, Theresia, Reinhard and Felt gates. Preserve the sealed body through every intervening earned derived operation. V21+/nonspine/import narratives remain unopened; source43/V41exception/datedgaps are unchanged. The sixteenth model, THERESIA_V01_V20_MODEL_AND_FIDELITY_REVIEW, is IMPLEMENTED at local PASS_WITH_BOUND_SAME_ANALYST_NONBLIND_DOCUMENTARY after complete saved-content/name-reference acceptance, applied19dimensions/28controls/eight NONCANONICAL_PROBE families and repaired findings. Its own complete publication/integration gate remains PENDING. Only after that gate: REINHARD_V01_V20_MODEL_AND_FIDELITY_REVIEW/own full gate → FELT_V01_V20_MODEL_AND_FIDELITY_REVIEW/own full gate → sealed V21. Reinhard/Felt remain EARNED_UNIMPLEMENTED/UNGRADED. Continue through admittedV43 and the mandatory terminal architecture/state/role-gap/acquisition review; CI owns merges.
```
