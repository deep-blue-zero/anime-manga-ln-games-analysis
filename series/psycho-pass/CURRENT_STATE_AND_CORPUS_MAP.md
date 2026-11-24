---
title: "Psycho-Pass — Current state and corpus map"
artifact_id: PP_CURRENT_STATE_AND_CORPUS_MAP
artifact_type: current_state_and_corpus_map
series: psycho-pass
version: "1.2"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
authority_generation: PP-INITIAL
source_boundary: "Run PP-S01NE-RUN-20261123-E01-E11 authorizes PP-S01NE-E01–E11 sequentially; accepted through PP-S01NE-E02"
canonical_home: series/psycho-pass/CURRENT_STATE_AND_CORPUS_MAP.md
created: 2026-11-18
last_updated: 2026-11-23
recommended_reasoning_class: BOUNDED_STANDARD
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  governing_method: framework/PP_ANALYTICAL_METHOD.md
  synthesis_architecture: framework/PP_SYNTHESIS_ARCHITECTURE.md
  method_status: canonical
  architecture_status: canonical
  source_reconnaissance_complete: true
  required_day_one_infrastructure_initialized: true
  required_ledgers_initialized: true
  required_day_one_infrastructure:
    - source-inventory/PP_SOURCE_REGISTER.md
    - installments/s01-new-edit/PP_S01NE_EVIDENCE_AND_STATE_LEDGER.md
    - installments/s01-new-edit/PP_S01NE_CLAIM_AND_DISCLOSURE_LEDGER.md
    - franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md
    - franchise/ledgers/PP_CONTINUITY_AND_CLAIM_LEDGER.md
    - integration/PP_RECONCILIATION_PROTOCOL.md
  sequential_analysis_lock: OPEN
  next_permitted_operation: PP-S01NE-E03
sequential_execution:
  run_id: PP-S01NE-RUN-20261123-E01-E11
  mode: continuous_sequential
  unit_type: episode
  authorized_start: PP-S01NE-E01
  terminal_boundary: PP-S01NE-E11
  committed_high_water_mark: PP-S01NE-E02
  next_candidate_operation: PP-S01NE-E03
  confirmation_between_units: false
  run_state: active
source_admission: "PP-S01NE-E01–E11 Season 1 New Edit authorized; each episode admitted at its own frontier; accepted through PP-S01NE-E02"
run_authorization: PP-S01NE-RUN-20261123-E01-E11
execution_profile:
  role_configuration_status: VERIFIED_ACTIVE_MULTIAGENT_NATIVE
  method_family: ANIME_WITH_CONTINUOUS_AV_COMPANION
  project_reconciliation_profile: PP_AV_PRIMARY_CHARACTER_AND_FORM
  continuous_video: VERIFIED_1FPS_WITH_LOSSLESS_CLIPS_AND_1080P_STILLS
  direct_listening: VERIFIED_48KHZ_JAPANESE_AND_50MS_AM
  source_language_inspection: VERIFIED_JAPANESE_ASS_SRT_AND_AUDIO
  complete_episode_bundles: VERIFIED_AVAILABLE_E01_TO_E11
  source_filesystem_metadata: VERIFIED_BOUNDED_INVENTORY
---

# Psycho-Pass — Current state and corpus map

The canonical root and sole continuing analytical branch are `series/psycho-pass`. This is one franchise project with installment-local source work and a distinct franchise reconciliation layer. The first intended installment is **Season 1 New Edit / Extended Edition, eleven episodes**. The original twenty-two-episode version is a separate possible comparison witness of the same underlying continuity, with its own identifiers, disclosure order and clocks.

**SEQUENTIAL_ANALYSIS_LOCK = OPEN.** Owner authorization (`PP-S01NE-RUN-20261123-E01-E11`, 2026-11-23) authorizes one `continuous_sequential` run across Season 1 New Edit (`PP-S01NE-E01` through `PP-S01NE-E11`), pushing each completed episode transaction to `series/psycho-pass` without raising a PR until all eleven episodes are complete. **`PP-S01NE-E01` and `PP-S01NE-E02` have been accepted**, advancing `committed_high_water_mark` to **`PP-S01NE-E02`** and `next_permitted_operation` / `next_candidate_operation` to **`PP-S01NE-E03`**. Each subsequent episode is admitted strictly at its own frontier after its fresh prospective freeze (`PP-S01NE-PRE-####`). No narrative material from `E03–E11` has been inspected.

Metadata reconnaissance verified eleven numbered New Edit MKVs, one excluded menu, two BD-labelled ASS witnesses, ten TV-labelled SRT witnesses, eleven standalone lossless FLAC tracks, and eleven structurally validated episode bundles. All 24 archival source hashes remain unchanged. Full audiovisual playback, direct Japanese listening, lossless stream-copy reinspection, 1080p still inspection, and 50 ms `AM` calibration have been verified empirically through `PP-S01NE-E02`.

## Accepted units (`PP-S01NE`)

| Unit | Status | Deep Reading | Transaction Checkpoint |
| --- | --- | --- | --- |
| `PP-S01NE-E01` | `ACCEPTED` (`14/14` QC PASS) | [`PP_S01NE_E01_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E01_DEEP_READING.md) | [`PP_S01NE_E01_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E01_CHECKPOINT.md) |
| `PP-S01NE-E02` | `ACCEPTED` (`14/14` QC PASS) | [`PP_S01NE_E02_DEEP_READING.md`](installments/s01-new-edit/readings/PP_S01NE_E02_DEEP_READING.md) | [`PP_S01NE_E02_CHECKPOINT.md`](installments/s01-new-edit/checkpoints/PP_S01NE_E02_CHECKPOINT.md) |

| Need | Canonical home |
| --- | --- |
| Governing source-facing practice and adopted AV-primary scope | [Analytical method](framework/PP_ANALYTICAL_METHOD.md) |
| Local/master authority, specialist synthesis and monographs | [Synthesis architecture](framework/PP_SYNTHESIS_ARCHITECTURE.md) |
| Exact available bytes, edition uncertainty, clocks and missing routes | [Source register](source-inventory/PP_SOURCE_REGISTER.md) |
| S1 New Edit observations, source locators and local state | [Local evidence and state ledger](installments/s01-new-edit/PP_S01NE_EVIDENCE_AND_STATE_LEDGER.md) |
| S1 New Edit hypotheses, disclosure freezes and claim changes | [Local claim and disclosure ledger](installments/s01-new-edit/PP_S01NE_CLAIM_AND_DISCLOSURE_LEDGER.md) |
| Reconciled character, directed relationship and institution state; portrait obligations | [Franchise state ledger](franchise/ledgers/PP_FRANCHISE_STATE_LEDGER.md) |
| Three chronologies, cross-installment claims and audiovisual recurrence | [Franchise continuity and claim ledger](franchise/ledgers/PP_CONTINUITY_AND_CLAIM_LEDGER.md) |
| Independent source review, AV calibration, incremental integration and handoff | [Reconciliation protocol](integration/PP_RECONCILIATION_PROTOCOL.md) |
| Housekeeping's project-local routing input | [Series descriptor](.repository/series-registry.json) |

The franchise ledgers are initialized with contracts, ownership and explicitly zero accepted narrative records. Their separation is functional: one reconciles people, relationships and institutions; the other reconciles chronology, propositions and motifs. Neither substitutes for detailed local readings or a full character portrait. Only the first intended installment has a directory. Later verified catalogue families remain inventory entries until their sources and a bounded analytical responsibility justify a local home.

## First-start prerequisites and retrieval

After this foundation is integrated, an authorized agent begins here, reacquires current [routing](../../governance/AGENT_ROUTING.md), reads the governing pair and source register, and retrieves the actual current ledger bytes. The owner must authorize a bounded run with start, terminal boundary, mode and stop conditions. Opening the [initiation](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md) lock and recovering that authorization are separate requirements.

Before narrative admission, identify the actual first episode witness, verify edition and completeness, produce and QA the [episode-bundle](../../governance/source-policies/MANGA_ANIME_EPISODE_BUNDLE_SPECIFICATION.md) responsibilities, align source-language evidence and calibrate the chosen inspection routes. TV subtitle end times exceed the candidate video durations by roughly ten to eleven minutes. E04 lacks any external subtitle witness; E11 audio language is untagged. The two BD-labelled ASS files also require synchronization and text-fidelity checks. These gaps do not authorize invented dialogue or silent substitution of another edition.

The adopted future role configuration gives an accountable principal continuous AV responsibility for character performance and episode form, with independent source-language/evidence specialists, an independent critical reviewer and a named integrator. Gemini 4 Carbon High is the owner's preferred principal candidate; OpenAI and/or Anthropic are preferred independent specialist/reviewer candidates. Their current availability, context, supported media, sampling, audio access and transport limits remain **unverified**. The [method](framework/PP_ANALYTICAL_METHOD.md#governing-method-and-adopted-av-companion) and [protocol](integration/PP_RECONCILIATION_PROTOCOL.md) define the justified policy route without making a vendor name authoritative.

The first reading must inspect the complete admitted unit and preserve entering-state hypotheses before finalizing its beginning synopsis. No later-installment source material is licensed by this foundation. Metadata maintenance, evidence preparation under the applicable source rules, and framework corrections may continue within the existing bootstrap scope; substantive episode analysis awaits run authorization and verified first-start gates.
