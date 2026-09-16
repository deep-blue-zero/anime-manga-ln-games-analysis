---
series: GKM
artifact_type: recovery_audit
scope: gakuen_idolmaster_recovered_release_integration
generation: V2
status: canonical
source_boundary: "Recovered analytical release packages and repository documentation; no new source-media inspection or measurements"
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
last_updated: "2026-09-09"
---

# Gakuen Idolmaster recovered-file integration — 2026-09-09

The recovery resolves **32 of 33 originally named support-file targets**, verified against their expected release SHA-256 values. Their repository representations are restored. The remaining Rinami name is now classified as a likely stale, unverified filename reference; existing R2 documents cover its substantive responsibility, and no further collection action is requested. **Hiro and Misuzu are prospective targeted documentation-rebuild candidates**, not assumed lost-file recoveries.

This audit concerns the recovered analytical packages. It does not certify a fresh audiovisual inspection, recalculate metrics, reopen completed textual readings, or declare planned Rinha work complete.

## Integrated artifacts

| Character | Originally missing targets restored | Integration result |
| --- | ---: | --- |
| Saki | 6 | Historical release guide and five metric exports restored; two metric derivatives omit copied source-dialogue text while preserving all 212 line locators, timestamps and measurements. |
| Temari | 1 | Missing current dialogue dataset restored; the current music JSON is also corrected to its matching release generation. |
| Mao | 10 | Source-object checksums and eight structured supporting exports restored. |
| Sumika | 8 | Historical backport manifest and seven supporting provenance/metric files restored, including the late-Dear surrogate evidence. |
| Ume | 5 | Audio, song-mix and visual metric exports restored. |
| Tsubame | 2 | Audio-envelope JSON and TSV restored. |
| Rinami | 0 of 1 originally listed | No separate deliverable established for `GKM_PHASE3_RINAMI_R2_HIGH_RESOLUTION_REINSPECTION_AUDIT.md`; reference corrected to existing R2 records. Removed from active collection work. |

The [integration manifest](GKM_RECOVERY_INTEGRATION_MANIFEST_20260909.json) preserves each integrated artifact's source member, original hash, recovery-time repository destination, resulting hash and declared transformation at `a38e6aa313324b399adc8e7681a21106f730c15d`. Its original unresolved-object entry is historical; the current Rinami disposition is stated above. The subsequent [AV path migration](GKM_AV_PATH_MIGRATION_20260909.tsv) maps those Git destinations to the consolidated character homes and records navigation changes without rewriting the earlier receipt. The [AV file index](../05_AUDIOVISUAL_ANALYSIS/GKM_AUDIOVISUAL_FILE_INDEX.md) routes all 13 characters without duplicating their analyses.

The eligible additions are original analytical prose, small derived-measurement tables, and source-engineering provenance cited by those analyses. They contain no source audio/video or frame assets. The two Saki dialogue-bearing originals remain recoverable in their external ZIP; only their measurement and locator projections enter Git. CRLF line endings in the two affected Saki TSVs are normalized to LF. The Saki guide receives historical authority metadata; the Sumika backport record retains its historical status while null relationship fields become empty arrays. One decomposed character in a Temari music source filename is normalized to Unicode NFC for valid repository JSON. Other restored current support bytes are preserved exactly, including historical execution-path strings. These formatting transformations change derivative hashes without changing measurements.

## Temari generation repair

- Current release: **131,808 bytes**, SHA-256 `af05ee2c76b35e2d84344e2070fb24b84c0c26e6e44a835d6835cd94bc4206d7`.
- `GKM_TEMARI_DIALOGUE_SCENE_SIGNAL_METRICS.json`: **26,342 bytes**, SHA-256 `0b73fb65d18669102a55cd24e6cebe67438fb9a361f142a3c2568bbe51aaf777`; 14 full episodes plus 31 phases. All 12 selected matrix rows agree at displayed precision.
- Recovered release original `GKM_TEMARI_MUSIC_SIGNAL_METRICS.json`: **21,189 bytes**, SHA-256 `828cbe7f52230689ca9f342a86b1c7a3cffc4da7d6c91e181f05e8a28fc6b2a0`. Its repository derivative is **21,186 bytes**, SHA-256 `bb03380149bff182affe05739e8965a454cc76e57b34706bee58e93d517f7251`, after NFC normalization of one source filename. All 15 music matrix rows agree at displayed precision.
- The displaced JSON is preserved unchanged in the [Temari predecessor archive](../90%20Legacy%20and%20Superseded/TEMARI_AV_PREDECESSOR_GENERATION_20260815/GKM_TEMARI_MUSIC_SIGNAL_METRICS.json). Its existing CSV companion is retained in Temari's AV `SUPPORTING_DATA/`, explicitly labeled historical by the current matrix and AV index. All 15 CSV rows and 17 shared fields match that predecessor JSON, not the restored current JSON.
- The distinct predecessor evidence matrix is recovered into the same archive. Its five already-present companion documents receive an explicit historical status, current-authority veto and successor path. Their analytical bodies are preserved.

The older selected-scene prosody and timing-estimate exports remain bounded supplementary material. They do not substitute for the restored complete dialogue dataset. Original release checksum manifests are retained as frozen package provenance; they are not regenerated to describe derivative Git bytes or new repository paths.

## Archive and collection closure

All 13 character-core ZIPs have now been recovered. Their core readings and evidence matrices were already represented in Git, so importing their historical ledger snapshots would regress or duplicate maintained documents. The four formerly pending Ume, Misuzu, Sena and Tsubame core containers all pass their outer sidecar and internal payload checks.

The exact current Sena AV ZIP is **44,934 bytes**, supplied locally with `(1)` in its filename. All 11 members are already represented; no replacement analytical body is necessary. The earlier **47,031-byte** copy is an alternate release.

The full Lilja R1 ZIP is **78,522 bytes**, SHA-256 `9218bf3fede11e5280985ab2af38a42e374099b9724d5036b8f41f79fb5cf4aa`, and matches the supplied sidecar. It is distinct from the small 246-byte and 398-byte historical Drive wrappers. The frozen migration records for those wrappers are left intact.

Phase-1 and Phase-2 releases were also inspected. The Phase-1 package's 36 additional source/work files, including dialogue extracts and historical analysis scripts, remain external. The Phase-2 package does not replace the newer maintained continuity state. The original Rinami core package has a checksum-manifest self-entry defect; its independently hashed payload entries pass, and the original archive is preserved unchanged.

ZIPs, media, the Temari spectrogram image, raw dialogue and redundant release snapshots remain external under the repository's [artifact policy](../../../governance/policies/ARTIFACT_ELIGIBILITY.md). This recovery adds provenance and eligible text representations; it does not upload, mutate or delete any external artifact. The local-collection catalog identifies recovered archive copies by name, size and hash without adding a Drive-only locator or changing an existing external-reference disposition. The [historical Drive reference index](../../../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md) and frozen crosswalks retain their established reference tuples. Recovery provenance stays within this analytical root.

## Remaining work

| Item | Status and next action |
| --- | --- |
| Hiro technical support and late-Dear materialization | Prospective targeted rebuild. Determine whether usable measurements can be recovered; otherwise create documented replacements and review only dependent claims. |
| Misuzu technical tables and 27-row materialization manifest | Prospective targeted rebuild. Reconcile the empty technical surfaces and unmaterialized manifest with any recoverable acquisition evidence. |
| Rinami named high-resolution audit | **REFERENCE CORRECTED; NO COLLECTION ACTION.** Separate file existence is unverified; use the R2 README, delivery audit and technical appendix. |
| Kotone source qualifications | Retain the explicitly text-aligned Dear 011–020 and remote-metadata-only `GO MY WAY!!` boundaries; they are not newly discovered missing documentation. |
| Kaya Rinha AV baseline and dossier | Planned Phase-6 work, not a lost release or a rebuild of a completed baseline. |
| Folder organization and governing metadata | AV consolidation is implemented as recorded in the [organization audit](../01_CORPUS_AUDIT_AND_SOURCE_LOCK/GKM_FILE_ORGANIZATION_AUDIT_20260909.md). Governing-metadata review before future sequential work remains separate. |

The [rebuild register](../01_CORPUS_AUDIT_AND_SOURCE_LOCK/GKM_TARGETED_REBUILD_CANDIDATES.md) defines the evidence, affected filenames and completion criteria. No rebuild was performed during this integration.
