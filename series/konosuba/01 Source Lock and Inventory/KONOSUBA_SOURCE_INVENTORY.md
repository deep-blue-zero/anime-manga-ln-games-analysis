---
series: KONOSUBA
artifact_type: source_inventory
scope: CURRENT_INGESTED_CORPUS
generation: V1
status: canonical
source_boundary: 41 live EPUB identities fixed at the 2026-10-16 snapshot; all 17 principal main narratives accepted; Gen05 frozen through V15 and preserved through V16–V17; V17 publication gate and separate final sequential checkpoint remain distinct; all nonprincipal and expanded components remain separately gated
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# KONOSUBA - Source Inventory

## 1. Primary-source root

Canonical source-folder ID: `1cCqwK0Bvd9OjcnN8jdsixAQrVOmlFfuw`.

The [source-coverage and admission matrix](KONOSUBA_SOURCE_COVERAGE_AND_ADMISSION_MATRIX.md) and its [41-object structured register](KONOSUBA_SOURCE_COVERAGE_AND_ADMISSION_MATRIX.json) govern the current inventory snapshot. They distinguish metadata/byte/structure verification, narrative admission, reading, analysis and validation. The older 21-book Git enumeration below has been reconciled against all eight live folders; it is not an exhaustive current source audit.

The former migrated `drive-ref` fragments did not resolve in the current reference index. The verified source-folder/object IDs in this inventory and matrix supply the source-plane route; no new analytical authority or modification of frozen migration crosswalks is implied.

## 2. Main Series

Folder:

Drive folder ID: `1EEgPj_i0bJSUUF6ZHCc5JUyCduMAigO8`.

Present:

- `Konosuba - Main Series - Volume 01.epub`
- `Konosuba - Main Series - Volume 02.epub`
- `Konosuba - Main Series - Volume 03.epub`
- `Konosuba - Main Series - Volume 04.epub`
- `Konosuba - Main Series - Volume 05.epub`
- `Konosuba - Main Series - Volume 06.epub`
- `Konosuba - Main Series - Volume 07.epub` — Drive ID `1UEwOHz8gu-cYgQOI2Yd7W6rd5joM8BWn`; SHA-256 `38c1fa428ba096cdc4c8b7a5df393dd5763b438e780ef2cef138860c608143c5`
- `Konosuba - Main Series - Volume 08.epub`
- `Konosuba - Main Series - Volume 09.epub`
- `Konosuba - Main Series - Volume 10.epub`
- `Konosuba - Main Series - Volume 11.epub`
- `Konosuba - Main Series - Volume 12.epub`
- `Konosuba - Main Series - Volume 13.epub`
- `Konosuba - Main Series - Volume 14.epub`
- `Konosuba - Main Series - Volume 15.epub`
- `Konosuba - Main Series - Volume 16.epub`
- `Konosuba - Main Series - Volume 17.epub`

Missing: **none**.

Main-series present count: **17 of 17**.

The former V07 continuity gap was closed on 2026-08-27 after the Drive object was reconciled against the updated manifest and passed a dedicated Japanese-language/integrity audit.

## 3. Short Stories

Folder:

Drive folder ID: `1y96b0Rxk3OWIfrF5BxvejB_Pyt13nIya`.

Present:

- `Konosuba - Short Stories - Yorimichi.epub`
- `Konosuba - Short Stories - Yorimichi 2.epub`
- `Konosuba - Short Stories - Yorimichi 3.epub`
- `Konosuba - Short Stories - Yorimichi 4.epub`

The first collection retains its pre-existing withheld-validation role. Collections 2–4 are post-validation supplementary prose. Individual stories and any edition-contained extras require component-level reading/disposition; compilation presence does not establish story coverage.

## 4. Spin-offs

Folder:

Drive folder ID: `1j6uNlVsgTpHBUhZUx8TrYG7y9A93pXuW`.

Present:

- `Konosuba - Spin-off - Consulting the Masked Devil.epub`
- `Konosuba - Spin-off - Explosions - Volume 01.epub`
- `Konosuba - Spin-off - Explosions - Volume 02.epub`
- `Konosuba - Spin-off - Explosions - Volume 03.epub`
- `Konosuba - Spin-off - Continued Explosions - Volume 01.epub`
- `Konosuba - Spin-off - Continued Explosions - Volume 02.epub`
- `Konosuba - Spin-off - Fantastic Days.epub`

`Consulting the Masked Devil` retains its withheld-validation role. The other six books are supplementary prose, with their own sequence, chronology, narrator and continuity boundaries. `Fantastic Days` requires an explicit relationship-to-game/novel-continuity disposition rather than automatic main-series authority.

## 5. Extra - Dust

Folder:

Drive folder ID: `1KTRMed8wQLksId6ZOLqQq6iEWL-mMH6z`.

Present:

- `Konosuba Extra - Dust - Volume 01.epub`
- `Konosuba Extra - Dust - Volume 02.epub`
- `Konosuba Extra - Dust - Volume 03.epub`
- `Konosuba Extra - Dust - Volume 04.epub`
- `Konosuba Extra - Dust - Volume 05.epub`
- `Konosuba Extra - Dust - Volume 06.epub`
- `Konosuba Extra - Dust - Volume 07.epub`
- `Konosuba Extra - Dust - Motto Ano Orokamono ni mo Kyakkou wo - Himesama kara no Shoutaijou.epub`

Dust V06–V07 retain their withheld-validation role, subject to character applicability and chronology audit. V01–V05 and the unnumbered continuation are supplementary prose. The continuation is not assigned an invented V08 identity. Distinct writer/illustrator/original-creator roles and source continuity are recorded in the matrix.

## 6. Source Audit and Manifests

Folder:

Drive folder ID: `1jXYPrYNEfTbykoqru0O2yJMMfkuW-kwX`.

Present canonical/provenance infrastructure:

- `audit_manifest.json` — Drive ID `1pTShKS8hq34nhlKLsydHgxWx7ImjOdZW`; the live version covers 36 retained primary books. Its earlier 21-book state is historical provenance.
- `KONOSUBA_SOURCE_LANGUAGE_AUDIT.md` — historical canonical audit of the 20-book 2026-08-23 batch; its fixed scope is preserved.
- `KONOSUBA_V07_SOURCE_LANGUAGE_AND_INTEGRITY_AUDIT.md` — dedicated audit closing the former V07 gap.
- `CALIBRE_IMPORT.md` — five later imports; purchase provenance is user-reported, predominantly Rakuten Kobo, rather than independently receipt-verified.
- `calibre_import_manifest.json` — five import records plus the full 41-object current media inventory and seven historical alternate/corrupt records.
- `drive_propagation_manifest.json` — propagation of the five imports; it is not a 41-book propagation audit.

The historical 2026-08-27 manifest recorded:

- 28 input EPUB files;
- 27 valid EPUB files;
- 1 zero-byte corrupt source;
- 21 retained primary books;
- 7 archived non-primary alternate/duplicate/corrupt files;
- main-series V01-V17 present;
- no main-series volume absent.

The current reconciliation is **36 audited witnesses + 5 later Calibre imports = 41 live EPUBs**. All 41 live filename/size pairs match the Calibre full inventory; newly retrieved bytes match the recorded SHA-256 values. All five propagation records match live object identity, parent, name and size. Historical language audits retain their original 20-book and V07-only scopes; neither certifies the expanded corpus's reading or component completeness.

### Additional live folders

| Folder | Drive folder ID | EPUBs | Current responsibility |
|---|---|---:|---|
| Artbooks | `1ombnFOVXYsmqjqpXoEzFkIo_cGJ2f6_H` | 2 | `Cheers` and `Blessing`; inspect embedded prose separately from illustrations and captions |
| Fanbooks | `1HVZrp2RiNooSXxbkHHDt-SXvB1tAzsQF` | 1 | Official Memorial Fanbook; distinguish fiction, editorial/reference material and promotion |
| TRPG | `1_l8iODnU9uHQmofohRVAZ9vf2aBd4gx1` | 2 | Core and advanced rulebooks; distinguish narrative/scenario components, setting material and mechanics |

These five books have image-only reading spines. Metadata-language checks and navigation labels are insufficient to establish prose contents, narrative boundaries or completed inspection. Page-image inspection is a required later responsibility, not an automatic exclusion of their fiction.

## 7. Authority notes

- Main-series Japanese novels are the canonical derivation corpus.
- The derivation corpus is now source-complete across V01-V17.
- Side material remains intentionally withheld from model construction until post-main-series validation.
- The run's expanded source scope is frozen to the 41 objects and identifiable edition-contained components in the matrix. Only the known four books supply the initial holdout experiment; other supplementary witnesses are not retrospectively recruited as favorable validation tests.
- Main-series derivation, immutable-suite validation, expanded-corpus analysis and attributable post-validation reconstruction remain separate stages. No supplemental finding rewrites prospective main-series state.
- Sequential authority still advances in volume order. Source completeness does not license skipping prospective checkpoints or reading later volumes out of sequence.
- Packaging quirks recorded by source audits do not by themselves invalidate readable source authority; V07 itself passes conformant `mimetype` placement/storage checks.

## 8. Update rule

This inventory is mutable active infrastructure. Update it in place when source material is added, removed, replaced, or reclassified. Material changes must also propagate to the source lock, current-state map, and master Drive index.


## V16 principal-component reconciliation — 2026-10-17

The separate V15 gate closed on `f011d24aaaca31c95168ce05bed15ba1e9384056`; the V13–V15 checkpoint and main-only Gen05 freeze then completed their separate exact publication gate on `b4c4c61412e93f16a218dcacd9d700253f6aea19` at 2026-10-17T06:49:08.667886Z. This later reconciliation distinguishes the current published boundary from the historical pending wording of earlier authored receipts. Gen05 model/forecast bytes, all 25 original blank Outcome/Adjudication pairs, Gen04's original blanks and all earlier outcome histories remain preserved.

MAIN-16 matches Drive `1IDfx2vWkl8YzSpVVsl6Q-oPj2a-FwcYs`, 8,530,869 bytes, SHA256 `7d8b2f5152716e0351dc6919abaa347c8504562d49ab9a748fdf3dc8db522df1`. Japanese OPF/spine/navigation and exact principal components were checked before exposure. The admitted ordered C1/I1/C2/I2/C3/I3/C4/I4/F/Ep members are `item/xhtml/p-002.xhtml`–`p-011.xhtml`: 2,844 all-body paragraph slots, 2,657 nonempty, 111,788 base characters and 2,666 ruby occurrences. Full source reading, twelve-pass analysis, separate 25 local prediction records, ten current ledger responsibilities and bounded independent receiving are documented by the [V16 reading](../02%20Sequential%20Readings/KONOSUBA_V16_DEEP_READING.md) and [receiving review](../09%20Audits%20and%20Manifests/KONOSUBA_V16_RECEIVING_REVIEW.md). Those actual scopes, shared-evidence limits and externally attributable corrections govern the analytical acceptance; this source-register reconciliation is not another literary reading.

Completion applies only to those ten principal members. Afterword p012 and bonus **アクセルの街の名物女神** beginning p014 remain IDENTIFIED_NOT_READ; its full extent is unresolved. Image wrapper p013 is structure-only/unviewed. `MAIN16-POSTBONUS-p015` contains 2,299 base characters detected mechanically but remains UNCLASSIFIED_NOT_READ, with no assumption of a separate story, continuation or colophon. All 28 image resources, front/end/colophon/promotional components remain uninspected. No entire-EPUB or expanded-program completion is claimed. V17 exposure requires the separate successful V16 publication/readback, source audit, housekeeping and final exact-head audit, followed by fresh source/entering-state admission. Holdouts and all supplemental/bonus/mixed narrative remain closed until the main-only reconstruction freeze and the applicable subsequent validation/expanded gates.


## V17 principal-component reconciliation — 2026-10-17

The separate V16 publication gate subsequently closed on exact source `4343c8bb5c162a4b35406f590b783a5e1735abb2`, tree `c9a12d3d546949a5402d93aba6b0b7908893da4c`, at 2026-10-17T09:10:10.172553Z. Source audit 39019357818/job117357886208, no-op housekeeping 39019715353/job117358932274 and final exact-head audit 39019738383/job117359003026 all succeeded with actual logged AUDIT_COMMIT/SOURCE_SHA equal that source. Both full audits passed 352 tests across 8,004 paths; the actual exact Repository integration audit status is success. This reconciles authored pending wording without rewriting the failed earlier main-drift attempt or claiming protected-main integration.

MAIN-17 freshly matches Drive `1IIFWiOJ25qVMxlU10HxHDQl-m89ygoqz`, 2,197,695 bytes, SHA256 `5a7864c555955fc1536091c3ced10114b9cd521883236a2d016b074cafc1819c`. OPF `content.opf` declares Japanese; both package dates and opaque ASIN/UUID identifiers retain their original uncertainty. Principal processing/admission occurred at 2026-10-17T09:11:27.578013Z/09:11:27.640386Z, after V16's closed gate. Exactly five ordered principal members C1/C2/C3/F/Ep at `text/part0009.html`–`part0013.html` comprise 2,608 all-body paragraph slots, 2,327 nonempty, 89,511 base characters and 2,269 ruby occurrences. Base text excludes rt/rp while ruby is separately preserved; there is no non-whitespace narrative outside body p, and all 267 br elements occur in blank/whitespace-only paragraphs. Full ordered source reading, twelve-pass analysis, separate 25 local Gen05 records and ten ledger responsibilities are bounded by the [V17 reading](../02%20Sequential%20Readings/KONOSUBA_V17_DEEP_READING.md) and [receiving review](../09%20Audits%20and%20Manifests/KONOSUBA_V17_RECEIVING_REVIEW.md). Actual separate discovery/coding/receiving scopes and attributable corrections belong to those artifacts; this source-register reconciliation is not another literary reading.

Only the five principal prose members are complete. Afterword0014 and colophon0016 are identified but semantically unread. `MAIN17-PREFRONT-0006` and `MAIN17-POSTCOLOPHON-0017` remain unclassified/unread: mechanical body-base counts 122/187 include formatting whitespace and establish no content identity. All 25 actual images remain unviewed; wrapper XML received structural inspection only, while remaining front/end/promotional/bonus-if-present bodies remain semantically unread. Absence of a separate bonus NCX label does not establish absence of eligible fiction. The 41-object identity seal is unchanged. Gen05's exact model/forecasts and 25 original blank scoring pairs, Gen04 freezes and all earlier outcomes remain preserved. V17 publication and its full exact-head gate remain separate obligations before publication of the V16–V17 final sequential checkpoint/main-series evidence freeze. That checkpoint is not the main-only reconstruction-suite freeze: specialist syntheses, the complete reconstruction suite and its reproducible freeze must still precede all four holdout sources; expanded component work follows validation. No whole-EPUB, expanded-program or final archival completion is claimed.


## YORI01 frozen-model validation reconciliation — 2026-10-17T16:32:18.058252+00:00

The later main-series/checkpoint/specialist/reconstruction gates are now closed; historical pending wording above retains its authorship boundary. The main-only R1 suite was frozen before holdout exposure and its exact source publication gate closed on3b92 at2026-10-17T15:19:27.894053Z. The unchanged baseline governs all four predefined holdouts; this update adds no prospective main-series evidence or model revision.

YORI01 exact2,395,940bytes/SHA256`71bf144bb0cead076949ef195e773eadab84676c2d650935bb41786794fd3594` was separately admitted15:22:14.543481Z. Eight principal prose members(C01–C08 at text/part0010/0012/0014/0016/0018/0020/0022/0024.html) comprise2,748all-bodyP/108,300base characters/all2,603ruby; three continuing reader scopes each completed the ordered prose, without summing overlap. Root accepted the source-local all39 validation16:18:33.421393Z after independent/semantic receiving and attributable corrections. Dispositions13C/7P/1localF/2AMB/16NT are overlapping scopes, not accuracy. K08's newly received status-insult/direct-replyC04P34→35 is locally falsified; all original contracts/blank fields/earlier scores and the frozen main-only models remain unchanged. Four T constraints are generated-response-only N/A, not source wins.

The [withheld validation](../04%20Checkpoints%20and%20Model%20Validation/KONOSUBA_WITHHELD_SOURCE_VALIDATION.md) and its source/reading receipt identify exact member hashes, all39 results, current corrections and unresolved alternatives. Ten ledger appends are explicitly PhaseB observations outside derivation; original3b92 ledger versions remain independently retrievable. Source acquisition/hash verification, full principal reading, limited model validation, full literary analysis and complete EPUB coverage are separate states. All actual images, afterword image and other excluded/front/end/unclassified components remain unviewed/unread; YORI01's full StageC literary/component work is still open. No original source audit is rewritten.

MASK has only package/metadata verification, with seven prospective principal continuations and separately identified electronic bonus/afterword; no narrative body or image has been opened or admitted. Both Dust holdouts and all other expanded/bonus/image bodies remain gated. The containing YORI01 publication/readback/sourceaudit/housekeeping/final actual-SHA gate is pending at authorship; the earlier3b92 gate cannot certify it. The fixed41 identity seal is unchanged. Four-book validation, all19 expanded books,17 main-edition excluded-component programs,five actual mixed/reference inspections and final synthesis/model/index/audit responsibilities remain unfinished.


## MASK unchanged-R1 validation and current admission reconciliation

The second designated source’s seven principal members were read completely. Source-local validation was accepted at 2026-10-17T17:53:18.365009+00:00. The exact object is 2,895,671 bytes, SHA256 `fea6f72fb35d1561ee736b1adae8cd396fc93adc3166e5bfa0eb3884a24fb127`. Pro, C01–C05 and Epi at text/part0009/0011/0013/0015/0017/0019/0021.html contain 2,862 all-body paragraphs, 111,130 base characters and all 2,915 ruby objects. The [source/reading receipt](../04%20Checkpoints%20and%20Model%20Validation/WITHHELD_SOURCE_VALIDATION_EVIDENCE/MASK_SOURCE_AND_READING_RECEIPT.json) provides exact native/member hashes, locators, source-language/package verification, reader/exposure chronology and exclusions. YORI01’s full publication gate at 0f8 closed before separate MASK admission at 16:49:53.455649Z. Earlier metadata-only and pending statements retain their historical boundary.

The [four-book validation](../04%20Checkpoints%20and%20Model%20Validation/KONOSUBA_WITHHELD_SOURCE_VALIDATION.md) records MASK’s 8C/9P/22NT and four generated-only N/A constraints. It preserves E08’s moderate-confidence functional C versus independent P dissent, mixed A01/A03/E06 cases, guard gaps and original initial histories. These overlapping dispositions are not independent trials or accuracy. YORI01’s 13C/7P/1localF/2AMB/16NT remains unchanged, especially K08’s local F. The main-only R1 models, 43 contracts, original synthetic responses/settings and all Gen01–05 histories remain frozen. Ten ledger appends are tagged Phase B, outside derivation; no post-holdout model revision has occurred.

Principal reading and limited validation leave the full literary and edition responsibilities unfinished. Electronic bonus text/part0023.html (57 paragraphs, 2,328 base characters) is structurally mapped; its narrative body remains closed. Afterword image0022 and all actual images remain unviewed; excluded front/end narrative bodies remain semantically unread and closed pending separate post-validation admission. Structural wrapper/package metadata inspection is a separate completed scope. Full Stage C literary/component analysis remains pending. Only MASK’s mutable admission/completion fields change; all other 40 objects/register rows, identity/edition/provenance fields and the fixed 41-object identity seal remain exact. Metadata, reading, analysis, validation and whole-edition states are separate.

The containing MASK publication gate remains pending at authorship; the last fully audited source remains 0f8. Dust06 then Dust07 require their preceding full publication gates before separate admission; both bodies remain closed now. The remaining four-book validation, 19-book expanded program, 17 main-edition excluded-component responsibilities, five mixed/reference inspections and later reconstruction/synthesis/index/audit work remain authorized and incomplete.


## DUST06 unchanged-R1 principal validation reconciliation — 2026-10-17T19:49:53.629486+00:00

The third designated source was accepted at 2026-10-17T19:39:07.686147+00:00: 4C (E03/E04/E05/E07), 1P (E08), 2AMB (E01/E06), 32NT (all 31 individual contracts plus E02), with four generated-only source N/A controls. These are overlapping dispositions, not accuracy. The exact EPUB is 4,582,670 bytes, SHA256 `d533fc314c5ecb86ff9316e372d2b4eb9747d65eb413e4d9a8b97a52b2fff4a1`. Five principal prose members C01–C04/Epi, item/xhtml/p-002.xhtml–p-006.xhtml, were fully read: 2,977 all-body paragraph slots, 2,862 nonempty, 97,693 base characters, 2,787 ruby objects and 4,308 rt nodes. Exact member identities, ruby/base locators, reader/exposure chronology and limits are in the [source receipt](../04%20Checkpoints%20and%20Model%20Validation/WITHHELD_SOURCE_VALIDATION_EVIDENCE/DUST06_SOURCE_AND_READING_RECEIPT.json) and [four-book validation](../04%20Checkpoints%20and%20Model%20Validation/KONOSUBA_WITHHELD_SOURCE_VALIDATION.md).

MASK's full gate closed at 18:20:00.931531Z on 404591ed before Dust06 principal admission 18:20:38.004420Z. Earlier package-only inspection 18:08:18.466249Z displayed no narrative or actual image; the original overbroad gate wording is externally corrected, not erased. The interposed main-only index publication 0d8067f1 subsequently completed its own full gate at 19:38:19.994444Z, before actual Dust06 acceptance. Original historical pending/metadata-only statements remain preserved; these later facts reconcile their current status.

Only Dust06's mutable reading/validation/component fields and register row advance. All other 40 objects/rows, identity, edition, publisher credits and provenance fields remain exact, with the fixed 41-object seal unchanged. Afterword p-007 (40 paragraph slots/1,673 base characters), excluded front/end, colophon and promotional bodies remain semantically unread; all 19 actual image resources remain unviewed. Principal validation does not certify absence of bonus fiction, whole-edition coverage or complete Stage C literary analysis. R1 models/43 contracts, prior scores and all prospective histories remain unchanged. Twenty separately tagged Phase B ledger observations do not enter main-only derivation.

Dust06's containing publication gate remains pending at this authorship; latest fully audited source is 0d8067f1. Close its separate readback/source audit/housekeeping/final exact-head audit before Dust07 admission. Full four-book validation, 19 supplemental prose books, 17 main-edition excluded-component programs, five actual mixed/reference inspections, expanded analysis, attributable revisions and final synthesis/index/audit responsibilities remain active. No final release or archival closure is asserted.


## Fourth holdout and four-book reconciliation — 2026-10-17T21:23:16.911562+00:00

DUST07 principal validation and all 39 four-source diagnoses were accepted at 2026-10-17T21:16:29.555881+00:00 under unchanged MAIN_ONLY_R1: DUST07 has 6 C(E01–E05/E07), 1 P(E08), 1 local F(E06), 31 NT(named principal contracts), plus four generated-only source N/A controls. These are overlapping source-specific dispositions, not accuracy or 156 independent trials. The [four-book report](../04%20Checkpoints%20and%20Model%20Validation/KONOSUBA_WITHHELD_SOURCE_VALIDATION.md) preserves YORI K08/DUST07 E06 failures, uncertain rivals and original scores; no baseline revision occurs.

Exact DUST07 EPUB is 4,740,436 bytes/SHA256 `cfec23e89118c06b6a83fdf4d4e5f4e5e68a00860f7520ca8ae6be12b33dc2f5`. Pro/C01/C02/C03/Epi, item/xhtml/p-002.xhtml through p-006.xhtml, were fully read: 2,881 all-body P slots, 2,769 nonempty, 100,169 base characters, 2,837 ruby and 4,367 rt nodes. [Source receipt](../04%20Checkpoints%20and%20Model%20Validation/WITHHELD_SOURCE_VALIDATION_EVIDENCE/DUST07_SOURCE_AND_READING_RECEIPT.json) binds exact native members/locators/exposure limits. DUST06 full gate closed 20:11:08.526739Z on 757c58fc before DUST07 principal admission 20:13:03.558500Z. Historical authored pending/metadata-only statements remain intact and reconciled here.

Only DUST07 current reading/validation/component fields and its narrative register advance; other 40 source objects/register rows and fixed 41 identity seal remain exact. Historical package counts/metadata statements, edition/provenance/creator-role distinctions and colophon-pending status are preserved. Afterword p-007 (35 P slots/1,769 base characters), all 19 actual image resources and excluded front/end/colophon/promotional bodies remain semantically unread/unviewed. No bonus-absence, whole-edition or complete Stage C literary claim follows. All four principal validations accepted does not mean all four entire editions analyzed.

The containing fourth-source/four-book publication gate remains pending; Stage C narrative admission is CLOSED until exact readback/source audit/housekeeping/final actual-SHA audit succeeds. Latest fully audited source is 757c58fc. After successful gate and fresh published reload, complete all 19 supplemental prose books/components, 17 main-edition excluded-component programs and five actual mixed/reference inspections, then expanded synthesis, attributable Stage D revisions, final synthesis/indexes/audit. The sole canonical current-state entrypoint remains active; no archival release is asserted.
