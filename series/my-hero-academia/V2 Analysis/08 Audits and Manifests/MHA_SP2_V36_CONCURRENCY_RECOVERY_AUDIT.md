---
series: MHA
artifact_type: audit
scope: V36
scope_detail: V36 closeout duplicate-write reconciliation
generation: V2
status: canonical
source_boundary: Japanese manga Volume 36 through frozen V36:p197; archival state only, no V37+ analytical evidence
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# MHA SP2 Volume 36 Concurrency Recovery Audit

## 1. Trigger

Two overlapping V36 closeout executions converged during the final Drive-persistence phase. A live master-index check exposed duplicate Drive artifacts with the same canonical filenames:

- two `MHA_SP2_V36_DEEP_READING.md` uploads;
- two `MHA_SP2_V36_UPDATE_MANIFEST.md` uploads.

The collision was detected **before** overwriting the already-live shared master index. Recovery therefore treated the live index and Drive artifacts as evidence and compared the duplicate packages before deciding authority.

## 2. Deep-reading comparison

### Retained canonical copy

- `MHA_SP2_V36_DEEP_READING.md`
- Drive: `1I2cycmjt71e9kjdCOk3q2h7UjvMLRWqO`
- Created: `2026-08-28T11:20:09.280Z`
- Size: **83,773 bytes**
- SHA-256: `964a838a5d52ecd08f9ab9f3f79dd4b71a03ee74a00ee095b9a43acc7b9e9ba1`

### Redundant later copy

- former Drive: `1m0ENOxWasFGv27YW-Pv2cghZRBbuJTER`
- Size at upload: **83,773 bytes**
- SHA-256: `964a838a5d52ecd08f9ab9f3f79dd4b71a03ee74a00ee095b9a43acc7b9e9ba1`
- Byte comparison against the retained copy: **identical (`cmp=0`)**.
- Post-recovery fetch: **404 / no longer present**.

**Adjudication:** genuine byte-identical redundancy. No analytical material is lost by deleting the later copy. Per corpus policy, it does not belong in Legacy/Superseded because it contains no distinct analysis or provenance content beyond the duplicate upload event documented here.

## 3. Manifest comparison

### Retained canonical manifest

- `MHA_SP2_V36_UPDATE_MANIFEST.md`
- Drive: `17tS1QDS7TE-MTKPCNRL2TG4SJdDsbuKN`
- Created: `2026-08-28T11:21:31.658Z`
- Modified during closeout: `2026-08-28T11:26:05.300Z`
- Size: **12,001 bytes**
- SHA-256 after canonical-ID binding: `bb2366b724ddb5622fdf1985d9191cb614934657e86b6de504c16bcdc0513b92`

### Redundant later manifest

- former Drive: `1x7UWqfEcv4bzk9A3Cb2Gtblkad58xs7K`
- Size at upload: **12,001 bytes**
- SHA-256 before cleanup: `38ac38a9a7df5b84e6c168b9d71851812f903321bda78493f07b836e171dc4e0`
- Textual diff against the retained canonical manifest: **one line only** — the deep-reading Drive ID (`1m0...` versus retained `1I2...`).
- Post-recovery Drive search no longer returns the redundant manifest.

**Adjudication:** semantically duplicate transaction record whose only difference routed to the duplicate deep-reading ID. Retain the earlier/live-master-routed manifest and delete the later redundant copy.

## 4. Cumulative-state comparison

The two executions were not analytically divergent. The retained manifest and the overlapping closeout package specify the same:

- V36 source lock and facing-spread locator rule;
- narrative endpoint `V36:p197`;
- governing transition;
- Bakugo endpoint caution;
- readiness transitions (`Jiro moderate -> strong`, `Tamaki moderate -> strong`, `Nejire insufficient/emerging -> moderate`);
- Mirio top-snapshot consistency repair to the already-canonical V17 `strong` state;
- cumulative target set;
- final local byte sizes and SHA-256 values for every MHA-owned mutable ledger/state file.

The in-place cumulative files were therefore written to the same intended final byte states. There is **no claim-level merge debt** and no need to preserve competing V36 analytical authorities.

## 5. Shared master-index state

The live `MANGA_ANIME_DRIVE_INDEX.md` had already advanced to **v5.17** with the earlier retained V36 IDs:

- deep reading `1I2cycmjt71e9kjdCOk3q2h7UjvMLRWqO`;
- update manifest `17tS1QDS7TE-MTKPCNRL2TG4SJdDsbuKN`.

That v5.17 transaction was retained rather than overwritten. It had been rebased on live v5.16 and therefore already preserved the concurrent Attack on Titan, Lycoris Recoil, DJFW and unrelated corpus state.

## 6. Current-state-map repair

The overlapping later execution briefly wrote `CURRENT_STATE_AND_CORPUS_MAP.md` with the now-deleted duplicate deep-reading ID `1m0ENOxWasFGv27YW-Pv2cghZRBbuJTER`.

Recovery repairs only that routing pointer to the retained canonical ID `1I2cycmjt71e9kjdCOk3q2h7UjvMLRWqO`, preserves all V36 analytical state, and records this audit as provenance.

## 7. Final authority

After recovery, the V36 authority set is:

- canonical deep reading: `MHA_SP2_V36_DEEP_READING.md` — Drive `1I2cycmjt71e9kjdCOk3q2h7UjvMLRWqO`;
- canonical closeout manifest: `MHA_SP2_V36_UPDATE_MANIFEST.md` — Drive `17tS1QDS7TE-MTKPCNRL2TG4SJdDsbuKN`;
- frozen boundary: **`V36:p197`**;
- exact Bakugo life/death/recovery state: **V37+ OPEN**;
- next sequential operation: `MHA_SP2_V37_DEEP_READING.md`.

No V37 evidence was used in this recovery audit.
