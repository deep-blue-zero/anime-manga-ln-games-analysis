---
title: "Peach Girl — Execution Authorization and Initiation-Gate Record"
artifact_id: PEACH_GIRL_EXECUTION_AUTHORIZATION_AND_INITIATION_RECORD
artifact_type: initiation_gate_record
series: "Peach Girl / ピーチガール"
series_id: peach-girl
generation: PEACH_GIRL_EXECUTION_RUN_1
version: "1.0"
status: active_provisional
scope: "Owner execution authorization, initiation-gate verification, source acquisition, capability profile and run-state transition for the V01–V18 continuous run"
source_boundary: "Original Japanese 新装版 V01–V18; all 18 witnesses byte- and package-verified; no narrative page inspected at this record"
canonical_home: series/peach-girl/07 Audits and Handoffs/PEACH_GIRL_EXECUTION_AUTHORIZATION_AND_INITIATION_RECORD.md
created: "2026-10-16"
review_status: OWNER_EXECUTION_AUTHORIZED_LOCAL_RESULT_UNREVIEWED
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
---

# Execution authorization and initiation-gate record

This record is the attributable successor to the [bootstrap receipt](PEACH_GIRL_BOOTSTRAP_RECEIPT.md). The receipt is preserved unchanged as evidence of the provisional, owner-unreviewed state in which the foundation was created. This record documents what changed afterward, on what authority, and what was verified before narrative admission. It contains no narrative findings.

## 1. Owner instruction and its exact scope

On 2026-10-16 (UTC) the owner issued a written execution instruction for an independent, source-grounded full-series analysis of the original Peach Girl manga. The instruction:

- states that it constitutes the owner's authorization to begin the full analytical execution, subject to verification of the existing initiation requirements;
- authorizes the original manga only, Japanese 新装版, numbered volumes V01–V18, one complete numbered volume per sequential unit, terminal sequential boundary V18;
- selects `continuous_sequential` with `confirmation_between_units: false`;
- authorizes the post-sequential program the architecture defines (G2 reconciliation, character/relationship/specialist synthesis, reconstruction with internal source-grounded validation, full-series synthesis and local G6 validation);
- excludes independently published sequels (裏ピーチガール, ピーチガールNEXT), adaptations, unrelated franchise material, upstream publication and any comparative evaluation;
- prohibits every push, remote ref, pull request, GitHub file edit and Drive write for this execution, while permitting read-only GitHub and Drive retrieval.

The owner had not reviewed the bootstrap before this instruction, and this record does not claim otherwise. The instruction authorizes execution against the existing foundation. It is not owner acceptance of any analytical result: semantic acceptance, integration and release remain pending. An agent-written run state does not create permission; this section is the recoverable statement of the permission actually given.

## 2. Pinned baseline and local execution boundary

| Item | Value |
| --- | --- |
| Repository | `deep-blue-zero/anime-manga-ln-games-analysis` (remote identity verified) |
| Pinned starting commit | `589343261ea63f4d521c8fafac628f4dc24361cb` (equal to the `series/peach-girl` remote head when fetched) |
| Local analytical branch | `local/peach-girl-analysis`, created at the pinned commit; clean initial worktree |
| Publication guard | Local `.git/config` only: `remote.origin.pushurl` set to an invalid local URL, `push.default nothing`; fetch remains operable; no tracked file changed |
| Later upstream commits | Not incorporated. Remote-tracking `origin/main` was fetched read-only, and history was unshallowed so the local validator can resolve its activation baseline. No merge occurred |
| Commit identity | Owner-approved repository identity, used for local commits only |

Authority predicate (routing Section 2) verified at the pinned commit: routing `document_status: ACTIVE_ACCEPTED`; `governance/AUTHORITY_STATE.yaml` epoch 1, `GIT_ACTIVE_ACCEPTED`, cutover `g8-authority-epoch-1-20260902T134713Z`; `AUTHORITY_SCOPE.json` SHA-256 `008b7b2adf114c1f39dd86fae064344457dab5b9e45486623fc9237fb6ed0916`; tag `activation/authority-epoch-1` → `01561d0c9398917c1329501b798733041ab17e98`. No newer epoch was observed. The registry row `peach-girl` resolves to the present entrypoint.

The governing documents were read at the pinned commit: AGENTS, authority state/scope, routing Sections 2–4, 6–7 and 12, the checklist's applicable sections, the initiation policy (Sections 2–3 in full), continuation policy (governing rule, Sections 1–2, 4–9, 12–13), handoff contract Section 15, topology Sections 1–11, long-series Sections 1–14 and reasoning Sections 1–4, 8–9 and 11–22. Material conflict with an indispensable external constraint: none in the analytical method. The only operational conflicts are the publication prohibition and the Drive no-write rule, treated in Sections 5 and 7.

## 3. Initiation-gate verification (policy Section 3)

| Requirement | Finding |
| --- | --- |
| 3.1 Canonical root resolved | `series/peach-girl/` is the registered root; no parallel root was created |
| 3.2 Reconnaissance | Medium, edition, unit and exclusions were established in the source map and are now strengthened by byte/package verification of all 18 witnesses (Section 4) |
| 3.3 Method | [Analytical method](../00%20Frameworks%20and%20Methods/PEACH_GIRL_ANALYTICAL_METHOD.md) covers witness admission, locators, evidence classes, claim labels, prospective transaction, character/relationship questions, manga form, revision and neutrality. It satisfies the section |
| 3.4 Architecture / Section 5 contract | [Synthesis architecture](../00%20Frameworks%20and%20Methods/PEACH_GIRL_SYNTHESIS_ARCHITECTURE.md) covers source model, canonical homes, responsibility matrix, state preservation, contradiction handling, specialist promotion, reconstruction contract, six gates, reasoning classes and amendment. It satisfies the contract |
| 3.5 Entrypoint | [Entrypoint](../CURRENT_STATE_AND_CORPUS_MAP.md) identifies both governing artifacts and the four instruments |
| 3.6 Day-one infrastructure | All four ledgers exist with complete schemas and zero source-derived rows |
| 3.7 Reasoning classes | Assigned in the architecture's execution section |

Locator convention: suitable. Every witness has one image per OPF spine wrapper, so `iNNNN` maps one-to-one to a spine occurrence. Wrapper `p-cover` is the first occurrence; wrappers `p-000`… follow. No subindex is needed in any volume.

Material architecture defects repairable within project-local files: none that block admission. Two operational clarifications are recorded instead of altering the method's contract:

1. **Evidence-plane staging.** The method assigns complete locator maps to the Drive evidence plane. This run is prohibited from writing to Drive. Complete deterministic locator maps are therefore staged locally with checksums (Section 4) and identified as pending authorized promotion. They are not claimed as published.
2. **Execution arrangement.** The long-series protocol's preferred owner split (local sequential reader, fresh cloud synthesis) is a preference, not a requirement. This run is a single hosted-container execution (`CLOUD_ONLY` arrangement in the topology vocabulary) with one designated operator for readings, ledgers and later synthesis. Synthesis is not handed to another session or language model, consistent with the run's independence constraint. Later stages begin from committed artifacts, not conversational memory.

## 4. Source acquisition and package verification

The Drive connector available to this execution could read collection metadata but refused file downloads above 10 MB. With the owner's temporary link-sharing and an owner-changed network policy, the 18 EPUBs and three provenance objects were retrieved read-only over HTTPS from the Drive download host. No Drive object was written, renamed or moved. The owner was told when collection finished so link-sharing could be withdrawn. The retrieved primary bytes remain in the execution's working plane, outside Git.

| Check | Result |
| --- | --- |
| Byte length and SHA-256 | All 18 witnesses equal the source-map values exactly (`PG-JP-NE-V01-W01` … `PG-JP-NE-V18-W01`) |
| Provenance objects | `calibre_import_manifest.json` SHA-256 `30d7a625…a8cbe8` and `drive_propagation_manifest.json` SHA-256 `b13bd21b…18d872` equal the recorded values; `CALIBRE_IMPORT.md` 3,240 bytes, SHA-256 `eff1f131…fcc42f0` (no prior recorded digest) |
| ZIP integrity | Python `zipfile.testzip` reports no bad member in any witness |
| OPF identity | Each title is `ピーチガール　新装版（N）` with the matching number; creator 上田美和; publisher 講談社; language ja |
| Layout | Every witness declares `page-progression-direction="rtl"`, `rendition:layout pre-paginated`, `rendition:spread landscape` |
| Spine/resources | Spine counts equal the source map's reported counts for all 18 (187, 175, 183, 179, 181, 175, 183, 177, 175, 179, 175, 177, 171, 175, 175, 171, 173, 187). Each wrapper references exactly one image; no referenced image is missing |
| Navigation | Each package has three navigation anchors, 表紙 ×2 → `p-cover` and 本編 → `p-000`. Navigation therefore supplies no chapter segmentation; chapter boundaries must be established by inspection at admission |

Deterministic locator maps (`PG-JP-NE-VNN-W01.locmap.json`, generator `locmap.py` v1, Python standard library `zipfile`/`xml.etree`/`hashlib`) record, for every spine occurrence, the wrapper path, `idref`, viewBox and image member with its byte length and SHA-256. The 18 map files and their SHA-256 inventory are staged locally for the evidence plane: `LOCAL_STAGED_PENDING_AUTHORIZED_DRIVE_PROMOTION`. Image extraction for inspection re-verifies each member digest against its map before use.

Printed page numbers, chapter labels and components are not inferred from wrapper names (`p-NNN` is a packaging name, not a verified printed page). They are established at each volume's admission.

## 5. Execution capability profile

```yaml
execution_profile:
  product_surface: "hosted agentic coding environment (cloud container)"
  tool_runtime_location: "hosted, ephemeral Linux container"
  observation_date: "2026-10-16"
  capability_scope: "fixed-layout Japanese manga JPEG pages, 1042x1600 source images; Git; Python validation"
  source_transport: "HTTPS read-only download of owner link-shared Drive objects; byte/hash verified"
  filesystem_read: VERIFIED
  filesystem_write: VERIFIED
  image_inspection: VERIFIED
  audio_content_inspection: NOT_REQUIRED
  continuous_av_inspection: NOT_REQUIRED
  git_write: "VERIFIED_LOCAL_ONLY; publication prohibited for this run"
  inspection_method: "direct visual inspection of extracted page images by the executing analyst; no OCR route is used for quotation"
```

Capability probe: the V01 colophon (edition matter, `PG-JP-NE-V01-W01 / colophon / CUNKNOWN / i0187`) was rendered and read. Title, the electronic issue date `2017年3月31日発行（01）`, author and publisher were legible at source resolution. This probe inspected no narrative page. Reading spreads composed for inspection keep each page's `iNNNN` label, right-to-left order and unaltered aspect ratio. They are working derivatives, not source pages. When lettering is marginal in a spread, the single source page is inspected. Identity details of the executing system are kept in a separate owner-only record and are not part of analytical prose.

The repository validator needs Git ≥ 2.44 and the pinned validation wheels. A newer Git was installed into the container, and the validation dependencies were installed with hash checking outside the repository. Baseline author preflight (`validate_repository.py --phase current --snapshot index --routing-preflight series/peach-girl`) passed on the unchanged pinned tree.

## 6. Transition

On the basis of Sections 1–5, the initiation requirements are satisfied. The entrypoint records:

- `sequential_analysis_lock: OPEN`, `next_permitted_operation: V01`;
- `sequential_execution`: `mode: continuous_sequential`, `unit_type: volume`, `authorized_start: V01`, `terminal_boundary: V18`, `committed_high_water_mark: null`, `next_candidate_operation: V01`, `confirmation_between_units: false`, `run_state: active`.

The method and architecture remain the governing `active_provisional` pair at version 0.1 content. They are adopted for this owner-authorized execution and are not owner-accepted results. For each volume, `committed_high_water_mark` advances only in the commit that closes that volume's complete transaction.

## 7. Publication-stage limitations and pending obligations

- No push, housekeeping, exact-head integration audit, nightly integration or owner acceptance will occur in this run. Repository integration and G6 release remain pending external action.
- Locator maps and any derivative evidence remain locally staged until a separately authorized Drive promotion.
- The entrypoint's run-state fields are checked locally by the repository validator against fetched `origin/main`. Each admission commit records `run_state: active` with matching next operations. Completion is recorded in a separate non-admission commit after V18, as initiation Section 3.9.4 requires when `main` has not already recorded the run as active.

Revision history: 1.0 — initiation transition record, 2026-10-16 UTC.
