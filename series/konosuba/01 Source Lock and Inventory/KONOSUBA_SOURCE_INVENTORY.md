---
series: KONOSUBA
artifact_type: source_inventory
scope: CURRENT_INGESTED_CORPUS
generation: V1
status: canonical
source_boundary: "21 retained Japanese EPUB primary books; main-series V01-V17 complete after V07 acquisition and audit on 2026-08-27"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# KONOSUBA - Source Inventory

## 1. Primary-source root

`../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-0f70fc4c9766e347`

## 2. Main Series

Folder:

`../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-2d38c00a5f2fb83a`

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

`../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-1adb53eff36435c9`

Present:

- `Konosuba - Short Stories - Yorimichi.epub`

Initial analytical role: withheld validation source.

## 4. Spin-offs

Folder:

`../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-379ecb12db0187ea`

Present:

- `Konosuba - Spin-off - Consulting the Masked Devil.epub`

Initial analytical role: withheld validation source, subject to viewpoint/chronology audit.

## 5. Extra - Dust

Folder:

`../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-9083bd66d305adee`

Present:

- `Konosuba Extra - Dust - Volume 06.epub`
- `Konosuba Extra - Dust - Volume 07.epub`

Initial analytical role: withheld validation source, subject to character applicability and chronology audit.

## 6. Source Audit and Manifests

Folder:

`../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#drive-ref-b3e5aab2221be30e`

Present canonical/provenance infrastructure:

- `audit_manifest.json` — Drive ID `1pTShKS8hq34nhlKLsydHgxWx7ImjOdZW`; updated in place on 2026-08-27 from the manifest state dated 2026-08-26.
- `KONOSUBA_SOURCE_LANGUAGE_AUDIT.md` — historical canonical audit of the 20-book 2026-08-23 batch; its fixed scope is preserved.
- `KONOSUBA_V07_SOURCE_LANGUAGE_AND_INTEGRITY_AUDIT.md` — dedicated audit closing the former V07 gap.

The updated manifest records:

- 28 input EPUB files;
- 27 valid EPUB files;
- 1 zero-byte corrupt source;
- 21 retained primary books;
- 7 archived non-primary alternate/duplicate/corrupt files;
- main-series V01-V17 present;
- no main-series volume absent.

## 7. Authority notes

- Main-series Japanese novels are the canonical derivation corpus.
- The derivation corpus is now source-complete across V01-V17.
- Side material remains intentionally withheld from model construction until post-main-series validation.
- Sequential authority still advances in volume order. Source completeness does not license skipping prospective checkpoints or reading later volumes out of sequence.
- Packaging quirks recorded by source audits do not by themselves invalidate readable source authority; V07 itself passes conformant `mimetype` placement/storage checks.

## 8. Update rule

This inventory is mutable active infrastructure. Update it in place when source material is added, removed, replaced, or reclassified. Material changes must also propagate to the source lock, current-state map, and master Drive index.
