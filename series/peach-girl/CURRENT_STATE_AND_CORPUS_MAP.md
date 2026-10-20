---
title: "Peach Girl — Current State and Corpus Map"
artifact_id: PEACH_GIRL_CURRENT_STATE
artifact_type: corpus_map
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: "0.8"
status: active_provisional
scope: "Single current entrypoint, source/readiness boundaries and next permitted operation"
source_boundary: "Original Japanese manga; 新装版 V01–V18 byte- and package-verified; owner-authorized continuous run V01–V18 active"
canonical_home: series/peach-girl/CURRENT_STATE_AND_CORPUS_MAP.md
created: "2026-10-16"
review_status: OWNER_EXECUTION_AUTHORIZED_LOCAL_RESULT_UNREVIEWED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
project_initialization:
  status: active_provisional
  architecture_lifecycle: INITIAL
  bootstrap_generation: PEACH_GIRL_BOOTSTRAP_V1
  governing_method: "00 Frameworks and Methods/PEACH_GIRL_ANALYTICAL_METHOD.md"
  synthesis_architecture: "00 Frameworks and Methods/PEACH_GIRL_SYNTHESIS_ARCHITECTURE.md"
  method_status: active_provisional
  architecture_status: active_provisional
  source_reconnaissance_complete: true
  source_reconnaissance_scope: ALL_18_WITNESSES_BYTES_AND_PACKAGES_VERIFIED
  source_admission: AUTHORIZED_SEQUENTIALLY_V01_TO_V18
  required_day_one_infrastructure_initialized: true
  required_day_one_infrastructure:
    - "03 Longitudinal Ledgers/PEACH_GIRL_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md"
    - "03 Longitudinal Ledgers/PEACH_GIRL_RELATIONSHIP_AND_COMMITMENT_LEDGER.md"
    - "03 Longitudinal Ledgers/PEACH_GIRL_INFORMATION_AND_REPUTATION_LEDGER.md"
    - "03 Longitudinal Ledgers/PEACH_GIRL_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md"
  substantive_sequential_findings_at_bootstrap: false
  owner_review: EXECUTION_AUTHORIZED_RESULT_ACCEPTANCE_PENDING
  sequential_analysis_lock: OPEN
  next_permitted_operation: V10
sequential_execution:
  mode: continuous_sequential
  unit_type: volume
  authorized_start: V01
  terminal_boundary: V18
  committed_high_water_mark: V09
  next_candidate_operation: V10
  confirmation_between_units: false
  run_state: active
analytical_execution:
  authorization: OWNER_AUTHORIZED_FULL_SERIES_RUN_LOCAL_ONLY
  authorization_record: "07 Audits and Handoffs/PEACH_GIRL_EXECUTION_AUTHORIZATION_AND_INITIATION_RECORD.md"
  sequential_units_admitted: 9
  sequential_units_completed: 9
  committed_narrative_high_water_mark: V09
  character_reconstruction_readiness: UNASSESSED_MODELS_NOT_PROPOSED_NARRATIVE_EVIDENCE_PRESENT
  publication: PROHIBITED_FOR_THIS_RUN_LOCAL_COMMITS_ONLY
repository_state:
  stable_branch: series/peach-girl
  routing_input: series/peach-girl/.repository/series-registry.json
  materialization_status: PRESENT_UNREVIEWED
  main_integration: NOT_AUTHORIZED_PENDING_OWNER_REVIEW
  integration_hold_required: DRAFT_PR_OR_NIGHTLY_HOLD
---

# Peach Girl — current state and corpus map

This is the single current first-read surface for Miwa Ueda's ピーチガール at `series/peach-girl/`, on continuing branch `series/peach-girl`. Generation `PEACH_GIRL_BOOTSTRAP_V1` is the INITIAL foundation with provisional authority; the owner has authorized execution against it, while acceptance of results remains pending. Git is the analytical plane under live authority epoch 1; Drive collection ID `1kxx4orHjiHg_CEI1fZyifjt8_e9WNmMp` is the canonical primary/derived evidence route, resolved through the source map. No prior Peach Girl analytical root was discovered; existing source-ingestion infrastructure is preserved.

`SEQUENTIAL_ANALYSIS_LOCK = OPEN`

`NEXT_PERMITTED_OPERATION = V10`

**New owner-authorized Route B continuation; pre-V05 source audit closed with corrections.** Work's substantive analytical corpus was not recovered. The [recovery receipt](07%20Audits%20and%20Handoffs/PEACH_GIRL_CODEX_RECOVERY_RECEIPT_20261019.md) preserves the earlier stop and input provenance; the [Codex source audit](07%20Audits%20and%20Handoffs/PEACH_GIRL_CODEX_V01_V04_SOURCE_AUDIT_20261019.md) records 177 directly checked V01–V04 images, findings, alternatives and successor ledger versions at PG-AUDIT-20261019. Historical PG-FR-V01…V04 remain unchanged. The audit was committed at `364ffc6f8cb4a01a56ad219761d867abaf7874b2` and independently restored from its verified outside-checkout backup before V05. New Codex V05 was committed at `15163c502663711b6a93b3c75a8bf1ab9d8721af` and its outside-checkout backup independently restored before V06. V06 was committed at `4f0f8b27650bb7a5757d9d61544846074baf5727`, with the openly dated own V05 perfume-selection correction, and independently restored before V07 admission. V07 was committed at `33e2adb495b6064f13f6a1f8c96c76f40ff3a841` and independently restored before V08 admission. V08 was committed at `c169ba0fac6c0ab688487359d46d327debcec1f9` and independently restored before V09 admission. V09 now closes after175 inspected/160 mainline images: Momo current dating and explicit romantic feeling, Kairi actual care plus explicit refusal violation, Misao situated loyalties, and distinct photo/message/necklace knowledge. Momo witnesses Kairi agree to Morika proposed hotel encounter/accept her phone-case gift, throws her own handmade gift and runs; future visit/explanation unshown. V10 is next only after the V09 coherent commit and verified outside-checkout backup. Source samples do not certify an independent full four-volume re-read.

The owner's 2026-10-16 instruction authorizes a `continuous_sequential` run over V01–V18 (one complete volume per unit, no confirmation between units) and the post-sequential program the architecture defines, as a local-only execution: no push, remote ref, pull request or Drive write. The [execution authorization and initiation record](07%20Audits%20and%20Handoffs/PEACH_GIRL_EXECUTION_AUTHORIZATION_AND_INITIATION_RECORD.md) holds the exact scope, the gate verification and the capability profile. Each volume closes as one atomic transaction before the next is opened. The high-water mark above advances only when that transaction's reading, ledgers, freeze and this entrypoint are committed together.

## Source and completion boundaries

| Boundary | Current verified or explicitly limited state |
| --- | --- |
| Proposed target | Original manga only, using Japanese 新装版 numbered witnesses; publisher records identify the original and new-edition V18 as terminal collected volumes |
| Drive availability | 18 EPUB objects labeled V01–V18 plus three provenance files; IDs, filenames, sizes and parents reconciled with live metadata; no missing number in that observed set |
| Byte/structure verification | All 18 witnesses downloaded read-only; byte length, SHA-256, ZIP integrity, OPF identity, RTL fixed layout and one-image-per-spine-wrapper linkage verified; spine counts equal the reported counts. Deterministic locator maps are staged locally pending authorized evidence-plane promotion |
| Unresolved source structure | Chapter boundaries, printed-page mapping and internal components/extras: navigation offers only 表紙/本編, so these are established by inspection at each volume's admission |
| Narrative admission / inspection | Volumes are admitted and closed one at a time; the committed high-water mark in the front matter and the table of closed readings below are authoritative |
| Longitudinal state | Four instruments carry source-derived rows through the committed high-water mark; each volume transaction appends to all four or records no material change |
| Character reconstruction | Contract specified in the architecture; subjects/models unassessed; no operational model or capability grade |
| Synthesis/release | All six completion gates NOT_STARTED; no specialist or full-series findings |

The [source and scope map](00%20Frameworks%20and%20Methods/PEACH_GIRL_SOURCE_AND_SCOPE_MAP.md) owns exact keys/Drive IDs, manifest hashes, reported source hashes and limitations. Its inventory is not a source lock for an authorized narrative run. V01 structural verification does not establish chapter completeness, narrative admission or story understanding. Published volume counts are not used as proof of Drive availability.

裏ピーチガール and ピーチガールNEXT are separately published related manga and outside this mainline scope. Adaptations, novelizations, translation witnesses, promotional material and creator/editorial supplements remain unadmitted. Embedded extras have not been identified and must not silently enter the mainline.

## Closed sequential readings

Each row is a closed atomic transaction. Its freeze is recorded in the reading itself and is never edited afterward; later corrections go through the claims ledger or an attributable erratum.

| Volume | Freeze | Exit state (orientation only) |
| --- | --- | --- |
| [V01](02%20Sequential%20Readings/PEACH_GIRL_V01_DEEP_READING.md) | PG-FR-V01 | Momo and Tōji dating for three days but split by Sae's engineered misinformation; Momo refuses Tōji's kiss at the pergola; Kairi pursuing |
| [V02](02%20Sequential%20Readings/PEACH_GIRL_V02_DEEP_READING.md) | PG-FR-V02 | Sae's deceptions confirmed to the reader; Momo disbelieved by Tōji until a coerced hearing; Sae exposes the Kairi kiss and the 'practice' framing; Tōji proposes breaking up |
| [V03](02%20Sequential%20Readings/PEACH_GIRL_V03_DEEP_READING.md) | PG-FR-V03 | Tan report exposed as a friend's lie; Sae's method overheard by Tōji and exposed by class testimony; Momo publicly vindicated but refuses Tōji's request to restart; disavowed feelings for Kairi |
| [V04](02%20Sequential%20Readings/PEACH_GIRL_V04_DEEP_READING.md) | PG-FR-V04 | Momo chooses reunion after self-criticism and Tōji’s acknowledgment of fault; Kairi's hidden work revealed; the private sign; Sae servile in public, hostile in private; Jigoro misinformed about Momo and asks Sae out |
| [V05](02%20Sequential%20Readings/PEACH_GIRL_V05_DEEP_READING.md) | PG-FR-V05 | Sae's status and explicit Tōji desire coexist; Momo/Tōji deepen wanted intimacy, then Sae isolates/incapacitates Momo and impersonates her. Tōji detects deception, rejects false voluntary-choice account and searches; Momo wakes uncertain in hotel, Jigoro's final wish claim unverified |
| [V06](02%20Sequential%20Readings/PEACH_GIRL_V06_DEEP_READING.md) | PG-FR-V06 | Tōji reaches/rescues Momo; misheard self-blame causes crisis, explicit no-fault care restores intimacy. Trio overhears Sae drug admission, consciously chooses mirrored revenge; staged breakup hurts despite performance. Sae incapacitated/delivered to unintended threatening receiver, intended actor still waiting; both hotel outcomes unresolved |
| [V07](02%20Sequential%20Readings/PEACH_GIRL_V07_DEEP_READING.md) | PG-FR-V07 | Momo reverses revenge, leads Sae rescue and ends engagement without forgiveness. Sae retains destructive intent and weaponizes photos; Tōji refuses then conceals threat, declares actual breakup and fails recover genuine originals. Momo accurately infers blackmail; Tōji performs Sae kiss as misleading proof, Momo shocked. No press-image publication established |
| [V08](02%20Sequential%20Readings/PEACH_GIRL_V08_DEEP_READING.md) | PG-FR-V08 | Continued rejection/object harm and Tōji protective explanation to Misao. Kairi visits/helps/rescues; separate fan lie and Sae sign sabotage. Momo still loves Tōji, directly admits Kairi more important than friend but unsure love/comfort; he accepts continued proximity. Further kisses do not establish explicit reciprocal dating pact |
| [V09](02%20Sequential%20Readings/PEACH_GIRL_V09_DEEP_READING.md) | PG-FR-V09 | Public couple/explicit Momo love and secret gift; Kairi rescue coexists with actual coercion, prompted apology and divided attachments. Misao confidence/loyalties, photo/necklace mismatch and partial Morika account. Final witnessed encounter assent/commercial gift causes Momo flight; actual hotel visit, explanation and relationship outcome unshown |
<!-- sequential-readings-end -->

## Read order and canonical responsibilities

1. This entrypoint, then the [source map](00%20Frameworks%20and%20Methods/PEACH_GIRL_SOURCE_AND_SCOPE_MAP.md).
2. [Analytical method](00%20Frameworks%20and%20Methods/PEACH_GIRL_ANALYTICAL_METHOD.md): source inspection, evidence/interpretation distinctions, locators, prospective sequential transaction and visual/written-language discipline.
3. [Synthesis architecture](00%20Frameworks%20and%20Methods/PEACH_GIRL_SYNTHESIS_ARCHITECTURE.md): responsibility matrix, dependencies, specialist promotion, reconstruction contract and separate completion gates.
4. The four day-one instruments: [character development/readiness](03%20Longitudinal%20Ledgers/PEACH_GIRL_CHARACTER_DEVELOPMENT_AND_READINESS_LEDGER.md), [relationships/commitments](03%20Longitudinal%20Ledgers/PEACH_GIRL_RELATIONSHIP_AND_COMMITMENT_LEDGER.md), [information/reputation](03%20Longitudinal%20Ledgers/PEACH_GIRL_INFORMATION_AND_REPUTATION_LEDGER.md), [claims/predictions/revisions](03%20Longitudinal%20Ledgers/PEACH_GIRL_CLAIMS_PREDICTIONS_AND_REVISIONS_LEDGER.md). These are current-eligible provisional schemas, not completed analysis.
5. [Bootstrap receipt](07%20Audits%20and%20Handoffs/PEACH_GIRL_BOOTSTRAP_RECEIPT.md): exact authored manifest, reconnaissance, validation/publication evidence and owner-review questions, preserved as the historical provisional state.
6. [Execution authorization and initiation record](07%20Audits%20and%20Handoffs/PEACH_GIRL_EXECUTION_AUTHORIZATION_AND_INITIATION_RECORD.md): owner execution scope, gate verification, full source acquisition/verification, capability profile and publication limits for the current run.

No separate character reconstruction specification is needed at this scale: its full behavioral, temporal, knowledge, speech, failure and validation contract has one home in the architecture. No empty source-unit, specialist or model artifacts are created. Chronology, visual form, speech and standalone agency ledgers are deferred candidates under the architecture's recurrence rule.

## Governance, execution and repository state

The governing dependencies are [AGENTS](../../AGENTS.md), [authority state](../../governance/AUTHORITY_STATE.yaml), [scope](../../governance/AUTHORITY_SCOPE.json), [initiation/architecture policy](../../governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md), [machine initiation control](../../governance/repository-controls/project-initiation-gate.json), [continuation policy](../../governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md), [authority/supersession policy](../../governance/source-policies/ARCHIVE_AUTHORITY_AND_SUPERSESSION_POLICY.md), [reasoning classes](../../governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md), [capability routing](../../governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md), [long-series protocol](../../governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md), [handoff contract](../../governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md), [branch lifecycle](../../governance/policies/BRANCH_LIFECYCLE.md), [publication policy](../../governance/policies/PUBLICATION_AND_CONTRIBUTION_POLICY.md), [integration checklist](../../governance/policies/CHANGE_INTEGRATION_CHECKLIST.md), [housekeeping policy](../../governance/policies/AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md) and [character curation policy](../../governance/policies/CHARACTER_DISCOVERY_MAINTENANCE.md). The live versions govern.

This bootstrap used a hosted Work execution environment for Git/text authoring, metadata/provenance inspection and a V01 package probe. Image narrative inspection was not performed. Future source and synthesis stages must verify their own capabilities, record actual observed execution configuration and preserve exact source/method/freeze lineage. No model-specific analytical rule or anticipated comparison outcome is included. The inherited run's hosted-container profile is historical in the initiation record. The current Codex receiver uses the owner's Windows desktop, directly inspected local EPUB images, a verified complete local checkout and the unchanged pinned governance; its profile and exposure are in the recovery receipt and source audit. One operator owns readings, ledgers and later synthesis, without a cross-session synthesis handoff.

All authored changes stay under this series root on continuing branch `series/peach-girl`. The local routing descriptor declares `project_initiation_gate: REQUIRED`, `PRESENT_UNREVIEWED` materialization and a verified present provisional entrypoint. Housekeeping alone synchronizes global routing outputs; character curation files are untouched. Exact starting and reconciled bases are historical receipt facts; Git history and audit statuses own publication verification.

Publication and exact-head CI facts are recorded in the bootstrap receipt and external immutable commit/status history; this file cannot predeclare its own eventual commit SHA. Main integration is withheld pending owner review. Under the [nightly integration policy](../../governance/policies/NIGHTLY_ANALYTICAL_INTEGRATION.md), a published bootstrap must have a draft PR or `nightly-hold` label so scheduled structural integration does not bypass that review. A green author preflight is not a final integration audit or semantic approval.

Revision history: 0.1 — bootstrap foundation for owner examination, 2026-10-16 UTC; lock CLOSED, no narrative findings. 0.2 — owner execution authorization recorded; all 18 witnesses verified; lock OPEN; continuous run V01–V18 active, 2026-10-16 UTC. 0.3 — run stopped after V04 by owner election (prose stop notice; structured fields unchanged pending integration); high-water mark V04, 2026-10-19 UTC.

Revision history addendum: 0.3 — newly authorized local Route B recovery and bounded source audit closed with corrective ledger versions, 2026-10-19 owner date; historical freezes preserved.

Revision history: 0.4 — new Route B V05 direct inspection of all 181 images, 51 evidence rows, four-ledger successor transaction and PG-FR-V05; next candidate V06 after commit/verified backup, 2026-10-19 owner date. V01–V04 remain inherited full readings with 177-image recipient audit; V05 is newly read in full. G1/G2–G6 not yet performed.

Revision history:0.5 — new Route B V06, all175 images/159 mainline,51 evidence rows, four-ledger successors/PG-FR-V06 and dated own V05 gift-steering erratum. V01–V05 frozen readings preserved. V07 next after commit/verified backup; G1/G2–G6 remain unperformed, owner date2026-10-19.

Revision history0.6 — new Route B V07,183 inspected/166 mainline,55 evidence rows, four-ledger successors/PG-FR-V07. V01–V06 frozen bytes retained. V08 next after commit/verified external restore; G1/G2–G6 still unperformed, closure owner date2026-10-20.

Revision history0.7 — new Route B V08,177 inspected/159 mainline,47 evidence rows, four-ledger successors/PG-FR-V08. V01–V07 frozen bytes retained. V09 next after commit/verified external restore; G1/G2–G6 pending,2026-10-20 owner date.

Revision history0.8 — V09 new Route B,175 inspected/160 mainline,39 evidence observations, four-ledger successors/PG-FR-V09. V01–V08 frozen bytes preserved, V10 next only after commit/verified outside restore, G1–G6 pending,2026-10-20 owner date.
