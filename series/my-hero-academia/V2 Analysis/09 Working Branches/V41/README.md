---
series: MHA
corpus: MHA_SP2
artifact_type: branch_tranche_entrypoint
scope: V41
authority_state: branch_working_draft_not_main
branch: chatgpt/my-hero-academia-analysis
source_boundary: Japanese manga Volume 41, narrative V41:p005-p195
---

# My Hero Academia SP2 Volume 41 — Branch Tranche Entrypoint

This directory is the single current entrypoint for the Volume 41 working tranche on `chatgpt/my-hero-academia-analysis`. It is review/staging authority on this feature branch only and does not supersede canonical `main` artifacts.

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

All 17 recorded base blob SHAs were re-verified against the current `main` tree before this tranche was committed; no MHA target had drifted.

## Authority boundary

This branch commit does **not** merge to `main`, rewrite canonical cumulative ledgers, advance canonical series state, mutate project-global routing/index state, or write to the evidence Drive. Those remain separate promotion operations requiring explicit authorization.
