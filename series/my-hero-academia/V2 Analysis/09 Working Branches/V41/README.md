---
series: MHA
corpus: MHA_SP2
artifact_type: branch_tranche_entrypoint
scope: V41
status: PROVISIONAL
source_boundary: Japanese manga Volume 41, narrative V41:p005-p195
do_not_use_as_current_authority: true
---

# My Hero Academia SP2 Volume 41 — Provisional Working Tranche Entrypoint

This directory is the single current entrypoint for the Volume 41 provisional working tranche. It is tracked for review and promotion preparation, but it does not supersede the canonical MHA current-state surface or advance the canonical sequential high-water mark beyond Volume 40.

The packet was originally staged on the now-retired temporary branch `chatgpt/my-hero-academia-analysis`. Historical branch-provenance fields preserved inside the byte-locked deep-reading chunks describe that original staging event; they do **not** define current repository routing or authority. Continuing MHA work is routed by repository policy through `series/my-hero-academia`.

## Analytical artifacts

- [Deep-reading index](./MHA_SP2_V41_DEEP_READING_INDEX.md) — routes the complete five-part Volume 41 reading. The split is transport-only; the index records the integrity hash of the rejoined canonical-form draft.
- [Volume 41 update manifest](./MHA_SP2_V41_UPDATE_MANIFEST.md) — source closure, major state changes, readiness effects, promotion gates.

## Pre-promotion semantic diffs

The following files preserve all 17 proposed cumulative-ledger/index/state updates without mutating their canonical targets:

- `diffs/V41_DIFFS_01_02.md` — Class 1-A; U.A. staff
- `diffs/V41_DIFFS_03_04.md` — family/civilians; villains
- `diffs/V41_DIFFS_05_06.md` — relationships; readiness
- `diffs/V41_DIFFS_07_08.md` — power philosophy; Hero Society
- `diffs/V41_DIFFS_09_10.md` — recognition/failed rescue; villain formation
- `diffs/V41_DIFFS_11_12.md` — Japanese/voice; visual motifs
- `diffs/V41_DIFFS_13_14.md` — callbacks/payoffs; first-pass corrections
- `diffs/V41_DIFFS_15_16.md` — primary-source locator; source inventory
- `diffs/V41_DIFFS_17.md` — series current-state/corpus map

All 17 recorded base blob SHAs were re-verified against the then-current `main` tree before the original tranche was committed; no MHA target had drifted at that staging boundary.

## Authority boundary

Tracking this packet in the repository does **not** by itself rewrite canonical cumulative ledgers, advance canonical series state, mutate project-global routing/index state, or write to the evidence Drive. Those remain separate promotion operations requiring explicit owner authorization and the then-current integration controls.
