---
series: KONOSUBA
artifact_type: source_inventory
scope: CURRENT_INGESTED_CORPUS
generation: V1
status: canonical
source_boundary: 41 live EPUB witnesses reconciled at the 2026-10-16 inventory snapshot; main-series V01-V17 source-complete; principal main-series narrative analysis accepted through V12; V10–V12 checkpoint required before V13
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
