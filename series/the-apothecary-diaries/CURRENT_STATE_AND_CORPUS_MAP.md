---
title: "The Apothecary Diaries — Current State and Corpus Map"
artifact_id: AP_CURRENT_STATE
artifact_type: current_state_and_corpus_map
version: "1.0"
status: canonical
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
authority_generation: AP-INITIAL
authority_scope: "INITIAL bootstrap method, architecture, and administrative metadata only; no literary findings"
source_boundary: "Metadata reconnaissance: Japanese volumes 01–16 and separate simplified Chinese volume 15; no narrative admitted"
created: 2026-11-07
last_updated: 2026-11-07
project_initialization:
  status: canonical
  architecture_lifecycle: INITIAL
  governing_method: AP_ANALYTICAL_METHOD.md
  synthesis_architecture: AP_SYNTHESIS_ARCHITECTURE.md
  method_status: canonical
  architecture_status: canonical
  source_reconnaissance_complete: true
  required_day_one_infrastructure_initialized: true
  required_ledgers_initialized: true
  required_day_one_infrastructure:
    - SOURCE_WITNESS_AND_COVERAGE_MAP.md
    - CLAIM_EVIDENCE_AND_REVISION_LEDGER.md
    - SERIAL_CAUSAL_AND_KNOWLEDGE_LEDGER.md
    - CHARACTER_RELATIONSHIP_AND_REGISTER_LEDGER.md
    - CHECKPOINT_AND_INTEGRATION_LEDGER.md
  sequential_analysis_lock: CLOSED
  next_permitted_operation: NONE_AWAITING_RUN_AUTHORIZATION
recommended_reasoning_class: PREMIUM_QUALITY_FIRST
---

# The Apothecary Diaries: current entrypoint

This is the single current retrieval surface for **The Apothecary Diaries / 薬屋のひとりごと**, rooted at `series/the-apothecary-diaries/`. Authority is limited to an INITIAL analytical foundation and explicitly attributed source metadata. There are no sequential readings, character findings, monographs, reconstructions, or accepted narrative claims.

**SEQUENTIAL_ANALYSIS_LOCK = CLOSED.** No source-reading run has been authorized. No owner approval of the architecture or reconstruction readiness is claimed. Metadata verification, foundation review, and source-lock preparation may continue; opening or completing a bootstrap does not authorize narrative admission.

## First-read route

1. This entrypoint establishes authority and permitted scope.
2. [Analytical method](AP_ANALYTICAL_METHOD.md) governs future prose inspection and evidence discipline.
3. [Synthesis architecture](AP_SYNTHESIS_ARCHITECTURE.md) assigns accumulation, studies, review gates, reconstruction, and handoff responsibilities.
4. [Source witness and coverage map](SOURCE_WITNESS_AND_COVERAGE_MAP.md) preserves source identity and unresolved verification.
5. Use the following initialized state surfaces, then retrieve the full reading and primary witness behind any eventual claim. None is a substitute for those sources.

| Current artifact | Responsibility and initial state |
|---|---|
| [Claim/evidence/revision ledger](CLAIM_EVIDENCE_AND_REVISION_LEDGER.md) | Recoverable evidence routes, rival readings, claim transitions and prospective forecasts; administrative gaps only |
| [Serial causal/knowledge ledger](SERIAL_CAUSAL_AND_KNOWLEDGE_LEDGER.md) | Disclosure, chronology, knowledge, mechanisms and institutions without premature harmonization; no narrative state established |
| [Character/relationship/register ledger](CHARACTER_RELATIONSHIP_AND_REGISTER_LEDGER.md) | Distinct subject, directed relationship, ordinary-life and written-language evidence; no discovered subject roster |
| [Checkpoint/integration ledger](CHECKPOINT_AND_INTEGRATION_LEDGER.md) | Atomic reading closeout, freeze, role-gap review, dependencies and full-output handoff; all analytical gates unstarted |

No archived generation or specialist synthesis exists. Future artifacts obtain a current route here only after their scope and authority are reviewed.

## Actual source boundary

The reconnaissance supports a Japanese light-novel anchor inventory of **volumes 01–16**, with a **separate simplified Chinese volume 15**: seventeen reported EPUB witnesses. This range describes the supplied evidence, not the work's official completion or current publication extent. No manga or anime adaptation is admitted.

The historical source audit dated **2026-10-24** reports that a mislabeled Chinese V15 was corrected and a replacement Japanese V15 acquired. The two V15 files share an embedded UUID despite different language/content. They are different witnesses; UUID equality must never collapse them. Japanese V12–16 retain packaging warnings about ZIP `mimetype` order. The audit reports all seventeen containers/resources checked, but is not a full EPUBCheck, rendering, or exhaustive illustration inspection certificate. See the source map for exactly attributed checks and limitations.

`source_reconnaissance_complete: true` means that title, medium, inventory shape, and edition/language risks are sufficiently identified to design this foundation. It does **not** mean live remote checksums, byte identity, source lock, chapter boundaries, narrative inspection, linguistic comparison, or analytical source completion are verified. The 2026-11-07 campaign metadata reconciliation and historical audit are the basis; no primary narrative was read for this bootstrap.

## Review state and next work

The architecture is INITIAL and current for bootstrap rules. Independent semantic review found no unresolved bootstrap-design defects within the stated metadata-only boundary; owner architectural acceptance is not asserted. The next permitted *narrative* operation is **NONE_AWAITING_RUN_AUTHORIZATION**. Further foundation review can inspect depth, responsibility coverage, source partition, deterministic retrieval design, and truthful lock state without admitting prose.

Before a future run, bind every selected witness to immutable bytes and a public-safe local witness key; inspect container/spine and language; verify the intended numbered order and exact selected units; settle access and illustration capability; and record a bounded owner-authorized run under the [continuation policy](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md). Do not substitute Chinese V15 for Japanese V15, assume translation equivalence, or silently include a later acquisition.

Open source obligations are AP-SG-001 through AP-SG-005 in the source map. Narrative state and reconstruction coverage remain **NOT_ASSESSED**. A missing source, uncertain narrator, absent opportunity, and actual counterevidence are different conditions.

## Execution and durable resumption

Architecture and propagation-sensitive review use `PREMIUM_QUALITY_FIRST`: the intended gain is protection against edition conflation, erased epistemic states, and overcompressed longitudinal design, assessed by independent responsibility and counterexample review. Ordinary future sequential readings and interpretive ledger updates use `SUBSTANTIVE_ANALYSIS`; checkpoints, monographs, specialist integration and reconstruction use `DEEP_SYNTHESIS`; full-corpus convergence uses `PREMIUM_QUALITY_FIRST`. Mechanical hashes use `ROUTINE_FAST`; stable locator crosswalks use `BOUNDED_STANDARD`.

The preferred long-series arrangement is source-capable local sequential work and synchronized ledgers, fresh adequately grounded synthesis sessions, and a designated local integrator. This bootstrap uses bounded metadata and local document access; primary-source transport, parsing, text inspection, and still-image inspection have not been independently verified here. Textual voice requires TEXT inspection; illustration claims require STILL_IMAGE inspection. No audio or performed-voice capability is implied.

Resume from this entrypoint and its linked full files, not a chat summary. The checkpoint ledger governs full-output transfer, drift checks and freezes. Public Git holds analysis and sanitized references; primary EPUBs, private evidence receipts, access identifiers and extraction caches stay in their governed evidence/working planes. The local [registry descriptor](.repository/series-registry.json) identifies the root; designated housekeeping owns global routing.
