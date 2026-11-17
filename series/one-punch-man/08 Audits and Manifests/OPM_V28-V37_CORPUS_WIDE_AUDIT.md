---
series: OPM
artifact_type: corpus_completion_audit
scope: V28-V37 collected continuation completion and publication gate
generation: V2
status: canonical
source_boundary: Japanese tankobon V01-V37 physically contiguous, semantically locked, read and corpus-audited; official-web layer excluded
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
created: 2026-09-16
audit_result: PASS
workspace_state: local_complete_ready_for_governed_branch_publication
---

# One Punch Man — V28–V37 Corpus-Wide Completion Audit

## Result

**PASS.** The ten-volume continuation from V28 through V37 is complete and internally consistent. All ten immutable Japanese tankobon objects match their recorded sizes and SHA-256 identities; all ten semantic maps and sequential readings are closed; every per-volume freeze, retrospective comparison, checkpoint adjudication, propagation and final readback is present and ordered correctly. The collected analytical boundary is V01–V37. This audit closes the pre-publication corpus gate; it does not ingest or certify official-web narrative.

The noncanonical machine receipt is `_staging/verification/V28_V37_corpus_wide_audit.json`. It records 19 corpus checks, 410 passed per-volume closeout assertions and 110 V28–V37 checkpoint decisions with no failed check.

## Exact source identity and closeout state

| Volume | Images | Archive bytes | SHA-256 | Final checks |
|---|---:|---:|---|---:|
| V28 | 216 | 126,817,320 | `62d76b41823c35eb49e18229a4e28a89194088e496dc33db5140f00588605a28` | 35/35 |
| V29 | 199 | 132,639,923 | `7b31cb0fda3641ad926735233d18e93eb28d5f1f06e848866dfe9b07e980c02d` | 36/36 |
| V30 | 207 | 130,364,472 | `59135310fd0cd775a14a51f8885e8206f9348536b45cd6eb80cc3b8a3636cfd8` | 37/37 |
| V31 | 232 | 112,840,194 | `9bebff1e4e54613d7d471fcaec932c46804f5438807278f8294ed9ea0609eba1` | 39/39 |
| V32 | 231 | 152,226,910 | `9d19d62917c14878660a35bdf036fdded35234c13990dfa5a03b8a8b722b21d3` | 39/39 |
| V33 | 223 | 107,999,277 | `121d8b45e1c0be7fbd4fe4c0121161656ecaaa693e3b63786cc5d6596e8b76fd` | 41/41 |
| V34 | 224 | 97,684,009 | `2d5952153d956079fb04fe7137eb04d4b7b8ffe9dcfce6db78ba3ff21fce6bc7` | 41/41 |
| V35 | 207 | 87,519,794 | `160d07bd53253d99b32e168e5b388c608327c0c6c9aa974ec291da8f54e74c9d` | 43/43 |
| V36 | 247 | 198,284,447 | `4798a23e92395acbff507b63dd11bdd624a8c507c5143a6f45eca79eed454cdb` | 48/48 |
| V37 | 207 | 129,215,110 | `3e01ca4d5a3f7791df96b8cdb153707cd6995b22a01bcddfe373dc92578ef8b9` | 51/51 |

The audit freshly recomputed each archive hash from the immutable source root. The [source inventory](../01%20Source%20Lock%20and%20Inventory/OPM_SOURCE_INVENTORY.md), ten per-volume source audits, ten readings, ten language/register audits and ten update manifests agree on identity and PASS. V37 remains correctly distinguished from the V01–V36 supplied build manifest: its direct audit and fresh per-volume checks establish its authority without pretending that it was part of that build.

## Map and freeze consistency

The [tankobon chapter/extra crosswalk](../01%20Source%20Lock%20and%20Inventory/OPM_TANKOBON_CHAPTER_AND_EXTRA_CROSSWALK.md) has one mapped/canonical summary row and one semantic-lock section for each V28–V37 volume. Every per-volume final verifier contains a passed exact-map, coverage, crosswalk or span assertion. Chapter art, extras, bonus material, covers and publication/endmatter remain separately bounded; no archive image is silently promoted to narrative or left outside its locked map.

Prospective hashes are present for all ten volumes. Recorded chronology is strictly monotonic within every closeout: prospective freeze precedes V1 reopen/comparison, which precedes Checkpoint A adjudication, propagation and final readback. V28's early audit format did not ordinalize its targeted language set; its Japanese audit and 35-check final verifier directly retain that earlier procedure. V29 records twenty targets, and V30–V37 freeze 64, 87, 80, 112, 139, 178, 226 and 186 distinct target ordinals respectively. Format evolution is not rewritten into false uniformity.

## Checkpoint arithmetic and cumulative propagation

| Volume | CONFIRM | PARTIAL | CONTRADICT | NON-DIAGNOSTIC | Cumulative C/P/X/N |
|---|---:|---:|---:|---:|---|
| V28 | 1 | 0 | 0 | 10 | 34 / 3 / 0 / 205 |
| V29 | 0 | 0 | 0 | 11 | 34 / 3 / 0 / 216 |
| V30 | 0 | 0 | 0 | 11 | 34 / 3 / 0 / 227 |
| V31 | 1 | 0 | 0 | 10 | 35 / 3 / 0 / 237 |
| V32 | 0 | 0 | 0 | 11 | 35 / 3 / 0 / 248 |
| V33 | 0 | 0 | 0 | 11 | 35 / 3 / 0 / 259 |
| V34 | 1 | 0 | 0 | 10 | 36 / 3 / 0 / 269 |
| V35 | 2 | 0 | 0 | 9 | 38 / 3 / 0 / 278 |
| V36 | 2 | 0 | 0 | 9 | 40 / 3 / 0 / 287 |
| V37 | 2 | 1 | 0 | 8 | 42 / 4 / 0 / 295 |

Each volume contributes exactly eleven decisions, for 110 decisions in this audit range. Entering totals chain exactly to the prior volume and each score sums to the next cumulative state. The final [Checkpoint A validation ledger](../03%20Longitudinal%20Ledgers%20and%20Checkpoints/Checkpoints/OPM_CHECKPOINT_A_VALIDATION_LEDGER.md) contains one adjudication section per V28–V37 volume and closes at **42 CONFIRM / 4 PARTIAL / 0 CONTRADICT / 295 NON-DIAGNOSTIC: 341 decisions across 31 held-out volumes**. No mismatch class activates.

Every volume propagated into the same fourteen established homes: thirteen state/readiness ledgers plus the checkpoint ledger. The changed-path set is stable across the ten propagations; histories and the immutable prediction registry remain intact. The audit does not create duplicate topical homes, alternate cumulative ledgers or a parallel corpus root.

## Authority, metadata and retrieval audit

All active nonlegacy Markdown artifacts have valid required YAML authority fields. Canonical files remain usable as current authority and have no active `superseded_by` pointer. Local Markdown links resolve. No case-insensitive path collision or byte-identical duplicate active artifact exists. Expected V28–V37 names are present once in their established homes.

Older closeouts and the immutable V01–V06 checkpoint retain acquisition-gap statements that were true at their dated boundaries. They are historical states, not current routing. The current entrypoint, inventory, crosswalk, bootstrap, publication manifest and continuation hand-off identify V01–V37 as physically contiguous or explicitly mark the V35–V36 gap as former/resolved. Three live V37-readback-pending sentences in the current entrypoint were corrected during this audit; no earlier analytical body or score was rewritten.

Physical holding and semantic authority remain distinct even though both now end at V37: physical continuity means the archive objects are present and hash-identified, while semantic completion means the images were mapped, read, language-audited, frozen, compared and propagated. The audit certifies both states without collapsing the distinction.

## Publication and continuation disposition

The corpus is locally complete through collected V37 and ready for governed publication to the existing `series/one-punch-man` branch under the owner's recorded authorization. Publication must still reread current repository governance and `CHANGE_INTEGRATION_CHECKLIST.md`, reconcile concurrent branch history, keep source media/caches/receipts outside Git and leave protected-main integration separate.

Official-web material remains a distinct `active_provisional` authority horizon. The technical Tonari pilot is preservation evidence only and supplies no narrative claim to this audit. After branch publication, continuation begins by establishing the exact collected-V37/web overlap, accounting for revisions, and reading the backlog sequentially rather than jumping to the newest release.
