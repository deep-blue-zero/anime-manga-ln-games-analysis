---
title: Harmony / ハーモニー — Current state and sole first-read entrypoint
artifact_id: HARMONY_ENTRY
artifact_type: corpus_map
series: Harmony / ハーモニー
series_id: harmony
generation: HARMONY_BOOTSTRAP_V1
version: '0.1'
status: active_provisional
scope: Current state and sole first-read entrypoint
source_boundary: Original Japanese prose novel; candidate EPUB structurally inspected; zero narrative units admitted or read
canonical_home: series/harmony/CURRENT_STATE_AND_CORPUS_MAP.md
created: '2026-10-16'
review_status: OWNER_REVIEW_PENDING
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
project_initialization:
  status: active_provisional
  architecture_lifecycle: INITIAL
  governing_method: 00 Frameworks and Methods/HARMONY_ANALYTICAL_METHOD.md
  synthesis_architecture: 00 Frameworks and Methods/HARMONY_SYNTHESIS_ARCHITECTURE.md
  method_status: active_provisional
  architecture_status: active_provisional
  source_reconnaissance_complete: true
  source_reconnaissance_scope: BIBLIOGRAPHY_DRIVE_BYTES_PACKAGE_METADATA_AND_NAVIGATION_ONLY
  source_admission: NOT_ADMITTED
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
  - 03 Longitudinal Ledgers/HARMONY_ACTOR_RELATIONSHIP_AND_READINESS_LEDGER.md
  - 03 Longitudinal Ledgers/HARMONY_KNOWLEDGE_INSTITUTIONS_AND_COERCION_LEDGER.md
  - 03 Longitudinal Ledgers/HARMONY_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md
  substantive_sequential_findings_at_bootstrap: false
  owner_review: PENDING
  sequential_analysis_lock: CLOSED
  lock_reason: BOOTSTRAP_ONLY_OWNER_REVIEW_AND_SEPARATE_READING_AUTHORIZATION_REQUIRED
  next_permitted_operation: OWNER_BOOTSTRAP_REVIEW
analytical_execution:
  authorization: BOOTSTRAP_ONLY
  sequential_units_admitted: 0
  sequential_units_completed: 0
  committed_narrative_high_water_mark: null
repository_state:
  stable_branch: series/harmony
  routing_input: series/harmony/.repository/series-registry.json
  materialization_status: PRESENT_UNREVIEWED
  main_integration: NOT_AUTHORIZED
  integration_hold_required: DRAFT_PR_OR_NIGHTLY_HOLD
---

# Harmony / ハーモニー — current state and corpus map

This is the sole first-read entrypoint for the independent original prose-novel project at `series/harmony/`, on continuing branch `series/harmony`. The author is Project Itoh / 伊藤計劃. The foundation is current-eligible **provisional project guidance**, pending owner review; it contains no literary findings. No predecessor is superseded.

`SEQUENTIAL_ANALYSIS_LOCK = CLOSED`

The lock is closed because this instruction authorizes bootstrap only. Owner review, sufficient source verification, the initiation prerequisites and a **separate authorized source-reading operation** are all required before opening it. A valid scaffold, branch push, approved integration or passing audit does not itself admit a narrative unit.

## Independent progress states

| Responsibility | Present state |
| --- | --- |
| Bibliographic identity | Original Japanese print publication verified through NDL; digital and later print records kept distinct |
| Source inventory | One candidate Japanese EPUB in the governed Project Itoh collection; downloaded bytes, package metadata and navigation inspected |
| Authoritative reading witness | `SOURCE_NOT_YET_VERIFIED`: byte identity known; edition lineage, complete content classification and fidelity still unresolved |
| Narrative admission | `NOT_ADMITTED`; 0 units |
| Sequential reading | `NOT_STARTED`; 0 completed units; narrative high-water mark null |
| Longitudinal instruments | Three initialized schemas; 0 evidence, subject, relationship, institution, claim or prediction records |
| Reconciliation and synthesis | `NOT_STARTED`; coverage, specialist and novel-synthesis gates independently unmet |
| Character reconstruction | `UNASSESSED_NO_NARRATIVE_EVIDENCE`; specification exists, no subject selected, no model produced or validated |
| Owner review / publication permission | Owner review pending; branch publication authorized for review; main integration outside this task. Actual commit/PR/CI history belongs to the receipt and Git |

## Read order and current homes

1. This entrypoint, then [source and scope / witness map](00%20Frameworks%20and%20Methods/HARMONY_SOURCE_AND_SCOPE_MAP.md) for exact source keys, IDs, hash and unresolved source conditions.
2. [Analytical method](00%20Frameworks%20and%20Methods/HARMONY_ANALYTICAL_METHOD.md) for admission, locators, prose/form inspection and atomic prospective reading.
3. [Synthesis architecture](00%20Frameworks%20and%20Methods/HARMONY_SYNTHESIS_ARCHITECTURE.md) for ownership, completion gates and the complete character-reconstruction specification.
4. [Actor, directional relationship and readiness ledger](03%20Longitudinal%20Ledgers/HARMONY_ACTOR_RELATIONSHIP_AND_READINESS_LEDGER.md), [knowledge, institutions and coercion ledger](03%20Longitudinal%20Ledgers/HARMONY_KNOWLEDGE_INSTITUTIONS_AND_COERCION_LEDGER.md), and [claims, predictions and revisions ledger](03%20Longitudinal%20Ledgers/HARMONY_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md).
5. [Bootstrap receipt](07%20Audits%20and%20Handoffs/HARMONY_BOOTSTRAP_RECEIPT.md) for the exact authored path manifest, reconnaissance/validation record and review questions.

The source map owns the candidate witness; it is not a completed narrative source lock. Git contains methods, analytical state and compact provenance. Primary and deterministic derived evidence remain in the governed Drive evidence plane; this bootstrap neither changes Drive nor brings source payloads into Git.

## Next permitted action and boundaries

Next permitted action: **owner review of this foundation**. The source map specifies verification needed before a later first reading. No current sequential run is active, and no narrative high-water mark exists. The candidate first unit is a future routing proposal, not an admission.

This root owns only this novel. Genocidal Organ / 虐殺器官 is a different analytical project with separate source, observation, subject and claim identities. Common authorship and publication dates are bibliographic facts. Shared fictional continuity, sequel relations and shared argument remain unestablished here. No comparative study is created.

Adaptation films/scripts, manga, other Project Itoh fiction, essays, interviews, reception and English translations are unadmitted. The last category may become a separately identified comparison witness only under later authorization. Philosophical frameworks, including PACTRIH, cannot replace literary evidence and are not activated by this bootstrap.

## Governing operation and ownership

Live [repository instructions](../../AGENTS.md), [authority state](../../governance/AUTHORITY_STATE.yaml), [scope](../../governance/AUTHORITY_SCOPE.json), [routing](../../governance/CHATGPT_AUTHORITY_AND_ROUTING.md), [initiation policy](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md), [continuation policy](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md) and [integration checklist](../../governance/policies/CHANGE_INTEGRATION_CHECKLIST.md) govern. The architecture routes the remaining reasoning, capability, archive and handoff responsibilities.

Authored paths stay under `series/harmony/`. The local descriptor requests routing; [housekeeping](../../governance/policies/AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md) owns global catalogs. [Character curation](../../governance/policies/CHARACTER_DISCOVERY_MAINTENANCE.md) owns global discovery. A draft PR or `nightly-hold` is required by the [nightly policy](../../governance/policies/NIGHTLY_ANALYTICAL_INTEGRATION.md) for this owner-review publication.
