---
series: OPM
artifact_type: audit
scope: Handoff bootstrap steps 1-5; V27 administrative reconciliation and V28 readiness
generation: V2
status: canonical
source_boundary: Local holdings V01-V37; analytical boundary V27; V28 integrity only
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-12
workspace_state: local_staged_unintegrated
---

# One Punch Man — V28 Bootstrap Audit

## Result and scope

**PASS for requested bootstrap steps 1–5.** V27's missing administrative closeout is reconciled locally. The physical source run is V01–V37, including V35–V36. V28's complete mechanical integrity check passes. Its semantic source lock and sequential reading remain pending; step 6 was not started.

| Step | Result | Evidence / disposition |
|---|---|---|
| 1. Inspect existing V2 architecture/current map | PASS | Existing artifact identities and topical homes retained; current routing and governing method inspected |
| 2. Reconcile V27 administrative closeout | PASS | Frozen reading/audit preserved; 13 cumulative state ledgers, checkpoint validation, inventory, crosswalk and map advanced; missing manifest created |
| 3. Verify V28–V37 availability | PASS | All ten requested archives physically present and SHA-256 inventoried; former V35–V36 acquisition gap resolved |
| 4. Establish local staging corpus | PASS | All 132 tracked OPM baseline artifacts mirrored under the authorized root, with per-file baseline hashes |
| 5. Verify V28 integrity | PASS, mechanically | 217 entries / 216 JPEG images; CRC, complete decode, deterministic ordering and manifest comparisons pass; chapter/extra semantic ranges pending |

## Authority and workspace provenance

- Immutable input: `OPM_SOURCE_ROOT`.
- Sole analytical/output root: `OPM_ANALYSIS_ROOT`.
- Single current entrypoint: [CURRENT_STATE_AND_CORPUS_MAP.md](../CURRENT_STATE_AND_CORPUS_MAP.md).
- Read-only repository inspected: `OPM_REPOSITORY_CHECKOUT`; canonical OPM home `series/one-punch-man/`.
- Local repository HEAD: `61986f13c3e03b6d8937283c7f4e3d92cfe633e3`.
- GitHub main verified read-only at bootstrap: `de8ae99f0792b2c6d714f1f602b76be02a35803a`.
- OPM tree on both revisions: `70c84b23666cb9e75e515cb25e01da8e33b586ed`.

The checkout was behind main, so the OPM subtree was checked against remote main through read-only Git/GitHub queries without fetching or altering the checkout. Exact current governance/routing references were saved beneath `_staging/reference/repository/` with commit and SHA-256 provenance. Current governance preserves Git as effective authority. Local `status: canonical` retains each artifact's analytical role; `workspace_state: local_staged_unintegrated` and this map disclose that the edits have not become repository authority.

The baseline mirror contains 132 files and 4,949,016 bytes. `_staging/baseline_manifest.json` records each original repository path, staged path, size and hash. `_staging/reference_manifest.json` records the governance references. No alternative corpus or current-entrypoint file was created. `_staging/` is non-canonical tooling, receipts and cache, excluded from any eventual Git payload.

## Bootstrap reading boundary

The existing method, synthesis architecture, character schema, source inventory and relevant audits were read. V25, V26 and V27 canonical readings and V27's Japanese audit supplied the recent observational boundary. Current responsibilities, baseline/routing sections and recent transitions of every character, relationship, readiness and thematic ledger were inspected, with targeted historical checks where needed. The crosswalk's current table and relevant detailed maps were reconciled; checkpoint registry and recent adjudications were inspected and all result rows counted programmatically. Earlier ledger histories were retained, not recertified as a new substantive corpus-wide reading.

The frozen checkpoint and validation registry were visible during the explicitly requested bootstrap and in the handoff itself. A subsequent V28 pass must therefore be described honestly as source-first under the established freeze/reopen procedure, **not a newly blinded experiment**. Do not reopen predictions to steer the V28 observational pass. Later V1 files remain unopened until the relevant volume's prospective freeze. The inherited V37 source audit's metadata was inspected for identity/reconciliation; V29–V37 story images were not opened.

V27's original pass already records prospective freeze before V1 comparison/checkpoint scoring. This bootstrap preserved that receipt; it did not redo the pass or retrospectively manufacture blinding.

## Source availability and former gap

All archive filenames use `One Punch Man - Volume NN [Japanese].cbz` beneath the immutable input root. The recursive receipt includes full paths, sizes, modification timestamps and hashes for all source files. All 35 objects represented in the previous inventory match their stored byte sizes and hashes. V35–V36 are newly recorded and agree with their supplied build metadata.

| Volume | Images | Bytes | SHA-256 | Current verification scope |
|---|---:|---:|---|---|
| V28 | 216 | 126,817,320 | `62d76b41823c35eb49e18229a4e28a89194088e496dc33db5140f00588605a28` | Fresh full mechanical PASS; front matter inspected |
| V29 | 199 | 132,639,923 | `7b31cb0fda3641ad926735233d18e93eb28d5f1f06e848866dfe9b07e980c02d` | Hash/size match inherited inventory |
| V30 | 207 | 130,364,472 | `59135310fd0cd775a14a51f8885e8206f9348536b45cd6eb80cc3b8a3636cfd8` | Hash/size match inherited inventory |
| V31 | 232 | 112,840,194 | `9bebff1e4e54613d7d471fcaec932c46804f5438807278f8294ed9ea0609eba1` | Hash/size match inherited inventory |
| V32 | 231 | 152,226,910 | `9d19d62917c14878660a35bdf036fdded35234c13990dfa5a03b8a8b722b21d3` | Hash/size match inherited inventory |
| V33 | 223 | 107,999,277 | `121d8b45e1c0be7fbd4fe4c0121161656ecaaa693e3b63786cc5d6596e8b76fd` | Hash/size match inherited inventory |
| V34 | 224 | 97,684,009 | `2d5952153d956079fb04fe7137eb04d4b7b8ffe9dcfce6db78ba3ff21fce6bc7` | Hash/size match inherited inventory |
| V35 | 207 | 87,519,794 | `160d07bd53253d99b32e168e5b388c608327c0c6c9aa974ec291da8f54e74c9d` | New hash/size checked; image count/integrity from supplied build metadata |
| V36 | 247 | 198,284,447 | `4798a23e92395acbff507b63dd11bdd624a8c507c5143a6f45eca79eed454cdb` | New hash/size checked; image count/integrity from supplied build metadata |
| V37 | 207 | 129,215,110 | `3e01ca4d5a3f7791df96b8cdb153707cd6995b22a01bcddfe373dc92578ef8b9` | Hash/size match inherited separate audit |

Except V28's fresh check, image counts above are inherited inventory/build metadata, not new visual reading. Fresh complete checks for V29–V37 occur at their sequential turns. Physical availability does not close any later semantic or analytical boundary.

The supplied build manifest dated `2026-09-12T20:03:15+00:00` now covers V01–V36, reports `ok: true`, 7,773 input images, 7,770 retained images and three duplicate removals. V37 remains outside that manifest; its earlier direct audit applies to its unchanged object. Historical V01–V34 and V37 audits retain dated acquisition statements with explicit current routing notes. Current inventory, crosswalk and map now record the resolved physical gap. Drive and official-web holdings were not re-audited.

## Administrative reconciliation and global-index delta

The [V27 update manifest](OPM_V27_UPDATE_MANIFEST.md) owns the propagation receipt. Its checkpoint result is 1 CONFIRM and 10 NON_DIAGNOSTIC; cumulative totals are 33 / 3 / 0 / 195 across 231 decisions. No readiness promotion or new V27 interpretation was inferred merely to fill an administrative cell.

The global registry and corpus index already route `one-punch-man` to `series/one-punch-man/CURRENT_STATE_AND_CORPUS_MAP.md`. **Prepared global-index delta: NO CHANGE.** Stable slug, canonical home, entrypoint, materialization and media have not changed. The staged map carries the new volume boundary; no duplicate per-volume prose belongs in global routing. Global housekeeping and any future registry validation remain part of the post-V37 integration gate. No global index was manually edited.

Nineteen existing staged artifacts were updated: the seventeen V27 cumulative/routing homes enumerated in its manifest plus dated routing notes in the two inherited source audits. Three artifacts were created: this bootstrap audit, the V27 manifest and V28 source audit. No V28 deep-reading file was created.

## Readback receipt and next operation

The final local readback verifies exact preserved baseline files, source hashes, repository OPM hashes, changed-file scope, YAML metadata, new local links, the copied V27 map and checkpoint table, cumulative arithmetic, current-map routing and the absence of a V28 reading. Receipts beneath `_staging/verification/`:

- `source_inventory.json` — immutable-input inventory at verification start.
- `V28_integrity.json` — all 216 image checks and metadata.
- `V27_changed_paths.json` — nineteen existing corpus paths edited.
- `closeout_readback.json` — final checks and hashes for changed/new artifacts.
- `staged_changes.patch` — reviewable textual changes against the read-only baseline.

Source and repository content remain unchanged by this work. Existing V01–V27 readings, the V27 Japanese audit, immutable checkpoint, methods and legacy artifacts retain their original bytes. All generated files remain under the authorized analytical root. No git add, commit, fetch, checkout or push was performed.

**Next operation: V28 semantic source lock and prospective deep reading from the frozen V27 boundary.** Source integrity is ready; no narrative reading has started. Complete V28 and each later volume in order, then the complete V37 closeout and V28–V37 corpus-wide audit. Only then re-read `CHANGE_INTEGRATION_CHECKLIST.md`, current governance and current main before considering Git integration. No push is authorized by this bootstrap.
