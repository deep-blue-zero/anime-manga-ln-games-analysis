---
title: "Cosmic Princess Kaguya! — current state and corpus map"
series: cosmic-princess-kaguya
artifact_id: CURRENT_STATE_AND_CORPUS_MAP
artifact_type: current_state_and_corpus_map
generation: CPK-G1
version: "1.3.2"
status: canonical
authority_scope: "Single project entrypoint and post-CPK-R1 archive-integration surface qualified by post-audit erratum CPK_F01_R1_ERRATUM.md"
source_boundary: "Admitted Japanese feature witness CPK-W01-NF-WEBRIP-HEVC (F01, 00:00:00.000-02:22:03.207); primary continuous-AV candidate CPK-R1 frozen; independent bundle audit CPK-B1-SOL61 and bounded AV return CPK-AVRET-R1 completed, with source-contradiction errata recorded in audits/CPK_F01_R1_ERRATUM.md pending Stage-3 envelope publication"
canonical_home: series/cosmic-princess-kaguya/CURRENT_STATE_AND_CORPUS_MAP.md
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  governing_method: CPK_ANALYTICAL_METHOD.md
  method_status: canonical
  synthesis_architecture: CPK_SYNTHESIS_ARCHITECTURE.md
  architecture_status: canonical
  source_reconnaissance_complete: true
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - CPK_SOURCE_INVENTORY.md
    - CPK_OBSERVATION_LEDGER.md
    - CPK_CHARACTER_RELATIONSHIP_LEDGER.md
    - CPK_CLAIM_REVISION_LEDGER.md
    - CPK_RECONCILIATION_PROFILE.md
  sequential_analysis_lock: open
  next_permitted_operation: NONE
sequential_execution:
  mode: single_operation
  unit_type: film
  authorized_start: F01
  terminal_boundary: F01
  committed_high_water_mark: F01
  next_candidate_operation: NONE
  confirmation_between_units: true
  run_state: completed
---

# Current state

**SEQUENTIAL_ANALYSIS_LOCK = OPEN.** Owner-authorized single-operation primary continuous-AV run **`CPK-R1`** (`Gemini 4 Carbon`, `CONTINUOUS_AV`) for feature unit **`F01`** is **`completed`** (`committed_high_water_mark: F01`, `next_permitted_operation: NONE`, `next_candidate_operation: NONE`). Every interval of admitted primary witness `CPK-W01-NF-WEBRIP-HEVC` (`[00:00:00.000, 02:22:03.207]`, primary Japanese Audio Track 1 `0:a:0` and supporting Japanese `[SDH]` Subtitle Track 4 `0:s:3`) has been inspected across synchronized AV segments, high-bitrate reinspection clips, lossless `1920x1080` frames, and deterministic cut/loudness measurements.

> **Post-audit erratum.** The [erratum](audits/CPK_F01_R1_ERRATUM.md) qualifies the `v1.1` ledgers and frozen `v1.0` primary candidate. It records the actual scope and original freeze identities of the completed `CPK-B1-SOL61` bundle audit, the bounded `CPK-AVRET-R1` return, and source corrections. See §3 for the `犬DOGE`/`ウミウシ` distinction, the 28/12 observation split and the official source for Iroha’s age. Stage-3 reconciliation follows separate review and publication.

The independent primary candidate ([readings/CPK_F01_PRIMARY_DEEP_READING.md](readings/CPK_F01_PRIMARY_DEEP_READING.md)) remains **`draft_noncurrent`** (`do_not_use_as_current_authority: true`) and is frozen by exact byte count and SHA-256 in [audits/CPK_F01_RECONCILIATION_RECORD.md](audits/CPK_F01_RECONCILIATION_RECORD.md) (`comparison_v1_boundary`: `7c850af679471b74e36a8458985e448bc8191068`). No terminal project seal or operational character-reconstruction model exists.

Canonical root: `series/cosmic-princess-kaguya/`. Continuing branch: `series/cosmic-princess-kaguya`. Generation: `CPK-G1` for **超かぐや姫！ / Cosmic Princess Kaguya!**. Repository `main` remains analytical authority after owner/CI integration.

## Read and write routes

| Existing artifact | Current version & status | One responsibility |
|---|---|---|
| [Analytical method](CPK_ANALYTICAL_METHOD.md) | `v1.0` (`canonical`) | Film reading, lane permissions, Japanese evidence hierarchy, and observation discipline |
| [Synthesis architecture](CPK_SYNTHESIS_ARCHITECTURE.md) | `v1.0` (`canonical`) | Sixteen duties, cumulative homes, synthesis/freeze gates, and stage ownership |
| [Source inventory](CPK_SOURCE_INVENTORY.md) | `v1.1` (`canonical`) | Bound `F01` witness `CPK-W01-NF-WEBRIP-HEVC`, track map, calibrated clock, derivatives, and `CPK-R1` capability/coverage profile |
| [Observation ledger](CPK_OBSERVATION_LEDGER.md) | `v1.1` (`canonical`) | `CPK-R1` pre-audit `36`-scene map (`S0001`–`S0036`), `40` descriptive observations (`O0001`–`O0040`), `14` musical events (`M0001`–`M0014`), and interval coverage |
| [Character and relationship ledger](CPK_CHARACTER_RELATIONSHIP_LEDGER.md) | `v1.1` (`canonical`) | `15` established subjects, `24` state/knowledge horizons (`K0001`–`K0024`), `20` directed edges (`E0001`–`E0020`), `18` Japanese samples (`J0001`–`J0018`), and reconstruction gap audit |
| [Claim and revision ledger](CPK_CLAIM_REVISION_LEDGER.md) | `v1.1` (`canonical`) | `20` originating primary claims (`C0001`–`C0020`), rival readings, `8` open questions (`U0001`–`U0008`), and zero pre-audit adjudications |
| [Reconciliation profile](CPK_RECONCILIATION_PROFILE.md) | `v1.0` (`canonical`) | Mirror-route blind audit protocol, exposure allowlist, bounded escalation, and evaluation contract |
| [Primary deep reading candidate](readings/CPK_F01_PRIMARY_DEEP_READING.md) | `v1.0` (`draft_noncurrent`) | Frozen full-film `CONTINUOUS_AV` candidate monograph (`§§1–9`); noncurrent experimental candidate |
| [Historical blind verifier input packet](audits/CPK_F01_BLIND_INPUT_PACKET.md) | `v1.0` (`draft_noncurrent`) | Witness/clock/hash specifications and 24 questions used in Phase B2. See the erratum §2 for question cueing and derivative-hash limits. |
| [Post-audit CPK-R1 erratum](audits/CPK_F01_R1_ERRATUM.md) | `v1.1` (`canonical`) | Source corrections qualifying the `v1.1` ledgers and the scope and limits of the completed post-freeze audit and AV return. |
| [Reconciliation & freeze record](audits/CPK_F01_RECONCILIATION_RECORD.md) | `v1.0` (`draft_noncurrent`) | `READY_FOR_HANDOFF` transfer receipt, exact primary freeze hashes, §15.6 verification log, and **withheld adjudication mapping** |
| [Bootstrap review](CPK_BOOTSTRAP_REVIEW.md) | `v1.0` (`canonical`) | Architecture-bootstrap producer scope and provenance |
| [Routing descriptor](.repository/series-registry.json) | `canonical` | Project-local `ANIME` routing input for automated global index housekeeping |

Completed post-freeze records and prepared Stage-3 artifacts for subsequent review and publication after the primary completion and publication-envelope binding land on `main`.
- `independent/CPK-B1-SOL61/` & `audits/CPK_F01_BLIND_OBSERVATIONS.md` / `audits/CPK_F01_CLAIM_AUDIT.md` / `audits/CPK_F01_SELF_AUDIT.md` / `audits/CPK_F01_COMPARATIVE_EVALUATION.md` — Completed OpenAI `BUNDLE_MEDIATED` benchmark and post-exposure audit suite (see [audits/CPK_F01_R1_ERRATUM.md](audits/CPK_F01_R1_ERRATUM.md) §2).
- `audits/CPK_F01_PRIMARY_AV_RETURN.md` — Completed `1 of 1` primary continuous-AV and `5.1` PCM verification return (`AV-01`–`AV-10`).
- `synthesis/CPK_F01_INTEGRATED_SYNTHESIS.md` — Prepared full-film synthesis paired with the `v1.2` cumulative ledgers.

## Next stage and exposure firewall

1. **No further sequential source-unit admission is permitted without explicit new owner instruction** (`next_permitted_operation: NONE`, `next_candidate_operation: NONE`; `F01` is a single-unit feature).
2. **Next publication tranche.** After the primary archive snapshot and the `CPK-B1-SOL61` envelope binding merge to `main`, review the independent audit suite, bounded AV return, `v1.2` cumulative ledgers and integrated synthesis for publication.
3. **Immutable candidate rule**: Do not edit or overwrite `readings/CPK_F01_PRIMARY_DEEP_READING.md` to incorporate later audit revisions; record all post-audit transitions in `CPK_CLAIM_REVISION_LEDGER.md` and `audits/CPK_F01_RECONCILIATION_RECORD.md`.

## Resume requirements

An ordinary synthesis or integration reader starts at this entrypoint, reads `CPK_ANALYTICAL_METHOD.md`, `CPK_SYNTHESIS_ARCHITECTURE.md`, `CPK_RECONCILIATION_PROFILE.md`, and `audits/CPK_F01_RECONCILIATION_RECORD.md`, then acquires applicable live governance via [AGENT_ROUTING](../../governance/AGENT_ROUTING.md) and the [continuation policy](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md). A new blind verifier follows the [reconciliation profile](CPK_RECONCILIATION_PROFILE.md) and its exposure firewall. The [archived Phase B2 packet](audits/CPK_F01_BLIND_INPUT_PACKET.md) records the original questions.
