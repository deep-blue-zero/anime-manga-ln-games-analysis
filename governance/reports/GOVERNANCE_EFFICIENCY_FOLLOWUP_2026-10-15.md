# Governance efficiency follow-up — 2026-10-15

This is an implementation and measurement record, not another policy or an authorization record. Canonical obligations remain in the linked owners. Publication is blocked as described below; no remote success is asserted here.

## Baseline and preserved implementation

The fetched implementation branch remained unmerged at `e328b34f4651593d066a22e1debd1b6352ba5688`. Current main `23f439fe7c9102760154def56ea7e50eca4b5984` was already its ancestor. Work therefore continues on `codex/governance-simplification`; no replacement branch, merge into main, or rewritten history is needed.

The original efficiency audit was read from its supplied Google Doc without modification. Existing implementation commits already supplied analytical fidelity/corrigibility (`8377ae2c`), accepted authority and historical activation separation (`05b14dd2`), audit/access consolidation (`27453f97`, `87f90dac`), project-local run stops (`c9968863`), complete regression execution and validator reuse (`7705306a`), policy ownership cleanup (`ff2eaf69`), and main-bound run-stop continuity/release fixes (`7f7c842a`, `7ac820b8`, `93d77f0b`). Those changes remain intact.

PR [#169](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/169) remains open/unmerged at `1301269c1c80a0531886a837856060e328beed37`. Its semantic-acceptance rule belongs to the handoff contract Section 15 and its existing stage-handoff template. This task does not copy or modify those provisions. Shared edits are confined to routing in `AGENTS.md` and `CHATGPT_AUTHORITY_AND_ROUTING.md`. A compatibility anchor preserves its link to former Section 8.4, now 8.2. Dry merge-tree review found no textual conflict; eventual integration must still review the resulting instructions together.

## A. Task-dependent acquisition

Changed owners: `AGENTS.md`, `governance/CHATGPT_AUTHORITY_AND_ROUTING.md` Section 6, and `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md` acquisition instructions. Previously, full-document reading and global catalog acquisition obscured the actual operation's prerequisites. Now universal context leads to canonical sections selected by responsibilities, with additional context acquired before a scope change. The operating card routes; it does not duplicate full policy rules.

The five scenarios include a local commit/publication preparation, an established stable analytical branch where appropriate, and no authority recovery, interrupted-run recovery, provider/model migration, or new multimodal obligation. Reconstruction includes producing a substantial handoff; publication includes semantic acceptance. Those additional operations activate their respective rows when present. Project-specific entrypoints, methods, architecture, admitted-source boundaries, source evidence and provenance remain required in full as applicable; their variable size is excluded from both columns. Code and test reading is also outside these document totals.

### Measured governance volume

Counts are Unicode characters decoded from UTF-8, expressed as decimal KB (1 KB = 1,000 characters), not tokens or observed LLM consumption. Before uses whole documents in the directed sets at `e328b34f`; after counts the union of selected heading spans in this candidate, including document identity/introduction. Repeated sections count once. A section includes its children unless marked “own text” below. The count ends at the next equal-or-higher heading, ignoring headings inside fenced code. These are reproducible static retrieval budgets, not a claim that every session previously consumed every byte.

| Workflow | Before characters | After characters | Reduction | Further characters avoided by selecting spans within the current document set |
|---|---:|---:|---:|---:|
| Established sequential continuation | 204,963 | 158,379 | 22.7% | 89,660 |
| Retrospective character reconstruction | 180,108 | 155,853 | 13.5% | 84,121 |
| New series and first reading | 259,460 | 209,389 | 19.3% | 50,332 |
| Analytical tranche acceptance/publication | 180,108 | 135,373 | 24.8% | 46,269 |
| Cross-cutting governance/validation | 202,626 | 203,373 | -0.4% | 0 |

Sequential continuation drops 46,584 characters (22.7%); the preferred 25% target is not reached. Mandatory source-admission and closure context, the full authority-scope record, substantial execution/evidence rules, and publication controls limit further safe reduction within this task. The new run-consistency instructions add necessary context. Cross-cutting work reads affected owners in full and consequently grows slightly.

All net savings come from narrower retrieval and avoiding unrelated workflow/catalog material, not deleted protections. The rightmost column isolates section selection against the current full-document set; it is not the net before/after reduction, because the sets differ (for example, continuation now explicitly includes initiation admission/closure sections and publication policy). No formerly required information is unreachable: every owning document remains at its stable path, exceptional-operation routes remain explicit, and historical records retain their archival homes. Full-policy retrieval remains required when a task cannot be bounded to the listed sections. An agent's chosen role cannot waive a responsibility.

Before sets for reproduction: common = full operating card, state, scope, routing, checklist, branch policy, change-obligations control and corpus index. The first four workflows add full reasoning, topology, long-series and handoff policies plus housekeeping; continuation adds the continuation policy, and initiation adds continuation plus initiation. The governance baseline adds initiation, continuation, gate control, repository controls, artifact eligibility, audit execution and publication policy to common. Exact after selections are recorded in the appendix.

## B. Admission and completion

Changed owners: `tools/validate_repository.py`, `tools/tests/test_project_initiation_gate.py`, the existing test catalog, initiation policy Sections 3.8/3.9.4 and continuation Section 12 with their existing checksum sidecars. No project entrypoint, run-closure record, terminal closure or authority-scope control was rewritten.

Before, an OPEN architecture gate could admit a reading after the run's recorded completion without a closure record. Now new/changed classified sequential bytes are compared with fetched main, independently of the immutable activation tree used for architecture adoption. The activation commit is pinned to its existing value. Caller-selected preparation `--base` cannot move the admission boundary. Exact-main commit audits replay the incoming transaction against the first parent, preserving source-branch/post-integration agreement. Accepted unchanged readings are not readmitted when a run later completes; retyping/replacing an old path cannot masquerade as an accepted unchanged reading.

A governed admission requires existing fields to agree: OPEN lock, active run, matching nonempty permitted/candidate operations, recognized mode and recoverable bounds. Single-operation bounds and next unit must agree. A final transaction can close a previously active run recorded on main while preserving bounds and reaching its terminal high-water mark. Missing, contradictory or malformed fields, inconsistent prior closing state, and independent conflicting YAML fences fail closed. An unchanged accepted legacy inconsistency may survive an unrelated retrospective correction, but does not justify a new admission. Mature legacy roots with no structured run declaration retain the existing architecture route; empty, partial or malformed declared execution is not an absence exemption. An explicit CLOSED/prose lock, malformed lock or NONE next-permitted operation also blocks legacy admission without a run block.

Ordinary completed runs may keep OPEN architecture with both next operations NONE without creating a byte-sealed run stop or global amendment. Existing CLOSED/REOPENED and terminal seals remain independently enforced. Editing an active field is never proof of owner authorization. Existing owner instructions, run/checkpoint/handoff records and source inventory supply reviewable permission/scope evidence; the validator verifies consistency, not human identity or arbitrary semantic source-range membership.

## C. Historical-seal cost

Changed owners: existing `GitSnapshot.from_commit()` in `tools/character_index_core.py`, its call in `_validate_sealed_readings`, and `tools/tests/test_git_snapshot_io.py`. Optional exact paths reuse the existing immutable commit/type checks and verified blob reader. No new cache or storage structure was introduced. Final review reproduced automatic restoration of a missing local historical blob through a configured promisor remote. The existing Git runner now uses `--no-lazy-fetch` and `--no-replace-objects` to reject implicit historical retrieval and ignore replacement refs; an unsupported Git version fails closed. Validation uses Git 2.51.1. These options follow the [Git command documentation](https://git-scm.com/docs/git). Admission history also uses the same reader for canonical entrypoints.

The actual corpus has one terminal completion commit and seven sealed artifacts totaling 165,452 bytes. Synthetic fixtures use 1, 4 and 8 distinct completion commits with the same full current corpus tree and seven seals per commit. Each measurement calls `_validate_sealed_readings(..., exact=True)` and requires zero errors. Distinct fixture commits are local unreachable `git commit-tree` objects, not ref updates or published history. Measurements bracket that call with `perf_counter` and reset the existing Git metrics; snapshot setup is outside the timed region.

| Fixture / distinct commits | Required artifact reads | Complete snapshots before → after | Historical blob reads before → after | Blob bytes before → after | Seconds before → after | Git processes before / after |
|---|---:|---:|---:|---:|---:|---:|
| Actual corpus / 1 | 7 | 1 → 0 | 5,704 → 7 | 235,662,735 → 165,452 | 1.7208 → 0.0186 | 4 / 4 |
| Synthetic / 1 | 7 | 1 → 0 | 7,644 → 7 | 366,996,785 → 165,452 | 2.6768 → 0.0262 | 4 / 4 |
| Synthetic / 4 | 28 | 4 → 0 | 30,576 → 28 | 1,467,987,140 → 661,808 | 10.2431 → 0.0703 | 16 / 16 |
| Synthetic / 8 | 56 | 8 → 0 | 61,152 → 56 | 2,935,974,280 → 1,323,616 | 20.0839 → 0.0879 | 32 / 32 |

Before, the actual historical full snapshot loaded 235.66 MB; synthetic full snapshots loaded 367.00 MB each. After, one partial snapshot per completion reads only 0.165 MB. Logical read counts are exact at the instrumented reader; Git process counts remain four per commit. Timings are single observations on this machine, with cache/order effects, not statistical latency guarantees. Eight distinct closures required 2.936 GB of complete snapshot blob reads before and 1.324 MB after, which justifies the narrow optimization without speculative caching.

The completion must still be a real full-ID commit; exact path/type, historical SHA-256, current SHA-256 and sealed-set checks remain. Missing local history fails. The implementation does not fetch history or substitute staged/current bytes. Tests cover literal pathspec characters, missing paths, directories, executable blobs, symlinks, submodules, LFS pointers, staged replacements, invalid commit objects and object loss after a prior success with an available local promisor remote, and commit replacement refs.

## D. Consistency and ownership

`tools/update_repository_indexes.py` now reads live `governance/AUTHORITY_STATE.yaml` from its selected snapshot and generates the existing `series/registry.json` status. The designated generation command changes only `GIT_PRIMARY_AUTHORITY_EPOCH_1_STABILIZING` to `GIT_ACTIVE_ACCEPTED`; every series row is preserved. Tests in `test_repository_indexes.py` bind the label to live selected authority and reject absent/malformed state; the existing governance assertion follows that owner. Frozen activation records, authority-scope hash and Drive pointer are untouched. The generator stays inside the existing five routing outputs.

Normative run semantics remain in initiation/continuation policies; checklist owns procedure; routing owns acquisition; validators own machine checks; this report records observations. No new registry, ledger, schema, control file, approval stage, workflow or signature mechanism was added. PR #169 retains ownership of named-subject and referential-clarity acceptance rules.

## Validation and preservation

The complete gate is `python tools/prepare_commit.py --base origin/main --check --full`, with pinned dependencies from `tools/requirements-validation.txt`. Every discovered test remains mandatory; selective execution stays disabled. Successful pre-final full gates: 324 discovered/executed after seal optimization (0 failures/errors/skips; 323.754 seconds total, 256.710 seconds unittest), then 334 after run-state enforcement (0 failures/errors/skips; 342.320 seconds total, 278.092 seconds unittest). The final candidate adds two authority-generator tests and a replacement-ref regression, plus a legacy-declaration regression, for 338 discovered tests. The subsequent 338-test review gate passed with no failures/errors/skips in 365.719 seconds; final review then added known-negative legacy lock/next-operation subcases. The final gate result and exact local head are supplied in the task closeout, rather than asserting an unexecuted result in its own candidate tree.

Focused checks passed for the new admission cases, seal reader, authority generator and reviewed closing/classification cases. The first final full attempt executed 337 tests in 209.781 seconds total (144.283 seconds unittest), with 1 failure, 9 errors and 0 skips: the shared preflight fixture lacked the now-required live authority input. Its fixture was repaired without relaxing the generator or assertions. Other development runs exposed run fixture assumptions and a mocked-generator accounting error; those were corrected and rerun. One targeted invocation used an incorrect test class name; its corrected invocation passed. No test was deleted, skipped or weakened to manufacture success. The initial default Python lacked jsonschema; validation used an available environment matching every pinned dependency instead.

Measured staged validator time: 62.120 seconds before implementation changes, 56.803 seconds on the candidate before the final no-lazy-fetch/replacement-ref hardening and this report (7,647 paths). Instrumented blob bytes fell from 602,659,520 to 369,815,430; unique blob reads from 13,348 to 7,704. These end-to-end single observations also include the new admission check, so the isolated seal benchmark is the stronger attribution. Remaining dominant stages include authority graph construction (15.03 seconds), character validation (14.36) and initiation (11.85); no migration or evidence checks were removed.

Regression evidence includes all ten `RunAdmissionTests`; existing completed/terminal and run-stop tests (including main-bound releases, nested roots, missing history and joint reading/hash replacement); `test_terminal_independent_execution_fences_cannot_hide_conflicts`; the four selected-history tests; and two authority-label tests. The current-repository compatibility test exercises all registered project examples. Tests distinguish pre-activation paths, already accepted artifacts, new/changed admissions, and active-to-completed transactions. Retrospective claim revisions remain possible without readmission. NTR's seven reviewed seals and supplemental source boundary remain unchanged.

## Residual limits and deferred owners

- **Authorization:** initiation Section 3.9.4 and continuation Sections 3-5/12 own the distinction between declared consistency and owner permission. Main must be fetched faithfully; local refs are not cryptographic proof of owner action. The protected exact-head audit provides the provider context. General prose/live-service source limits and unit identity still require evidence-based review.
- **Legacy state:** Medalist, Chiramune, Rent-a-Girlfriend, Sayonara Lara, Silent Witch, Tomozaki, Watayuri and Mushoku Tensei were the audit's completed-run examples. Their accepted state is not swept or normalized. Their canonical project entrypoints own later operational correction; new admission activates the applicable consistency checks.
- **Classification/preservation proposal (not executed):** the current control recognizes substantive deep readings, not every historical analytical artifact. NTR's six `NTR_V01`–`NTR_V06_PROSPECTIVE_FREEZE.md` files declare `reconstruction_checkpoint`; `NTR_LATEWINTER_POSTREAD_FREEZE.md` declares `supplemental_postread_freeze`. They retain project freeze obligations but are outside the seven-reading terminal seal set. The structured-role regression now explicitly distinguishes these roles from `supplemental_deep_reading`. Do not relabel freezes/checkpoints as readings just to seal them. If separate machine byte-preservation is required, the NTR project owner should enumerate those seven historical artifacts and their existing freeze purpose, verify their historical commits/digests, and propose a separately reviewed extension of preservation coverage under initiation Section 3.8 while retaining the current reading set and closed admission boundary. Review tests must then cover changed/missing/retyped freezes, preservation of existing reading seals, and permitted separate errata. No such closure amendment is authorized or applied here. Arbitrarily mislabeled prose outside the existing classifier remains a semantic review gap.
- **Performance/architecture:** no topology/long-series consolidation, selective regression activation or migration-validation removal was attempted. Their owning policies and `AUDIT_EXECUTION.md` retain those separate obligations. Project C8-C10 defects, analytical entrypoint reconstruction and Drive pointer changes remain separate work.
- **Review compatibility:** future integration of PR #169 requires semantic review of the combined routing instructions and successful validation of that exact candidate. Its four-file delta has not been merged or overwritten.

## Publication limitation

Remote heads were fetched again and remained unchanged. The active activation-tag ruleset `21946617` was readable and protects deletion/non-fast-forward changes with no bypass actors. The required `GET /repos/deep-blue-zero/anime-manga-ln-games-analysis/branches/main/protection` returned HTTP 403, `Resource not accessible by integration`, on both checks. The available GitHub installation connection lacks the administration read access this endpoint requires.

The checklist's **Before and after publication** item 3 and the publication policy require stopping when main protection cannot be verified. Consequently no push was attempted and no successful `Repository integration audit` exists for this follow-up head. This is an unfinished publication/access check, not an intentionally deferred implementation. Resume requires a permitted credential/provider route that can read protection, then head reconciliation, any affected revalidation, a normal push, remote tree/changed-file readback and successful exact-head audit. No permission to alter repository access or controls is inferred.

Main, Google Drive, authority scope, frozen activation evidence, NTR closure, protected refs and published history were not modified by this task.

## Appendix: exact selected after spans

All paths below name existing canonical owners. “Own text” stops before child sections; ordinary selections include subsections. The counting method includes document identity and the introduction preceding the first numbered section. Universal and task-specific spans are combined and deduplicated per workflow; project-specific required context remains outside these fixed governance totals.

### Established sequential continuation

| Document | Selected sections |
|---|---|
| `AGENTS.md` | full |
| `governance/AUTHORITY_STATE.yaml` | full |
| `governance/AUTHORITY_SCOPE.json` | full |
| `governance/repository-controls/change-obligations.json` | full |
| `governance/policies/PUBLICATION_AND_CONTRIBUTION_POLICY.md` | full |
| `governance/CHATGPT_AUTHORITY_AND_ROUTING.md` | 2; 3; 4; 6; 7; 8 (own text); 8.1; 10.1; 12; 13 |
| `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md` | Before editing; Maintained documents: targeted edits (own text); Branch routing and cleanup; Change obligations; Execution profiles (own text); Local clone mode; Before and after publication (own text); Stable analytical branch profile; Stable analytical publication sequence (own text); Project-initiation architecture gate |
| `governance/policies/BRANCH_LIFECYCLE.md` | Continuing analytical branches |
| `governance/policies/AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md` | full |
| `governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md` | 1; 2; 3; 4; 8; 9; 11; 12; 13; 14; 15; 16; 18; 19; 21 |
| `governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md` | 1; 2; 3; 4; 5; 6; 8; 9; 10; 11 |
| `governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md` | Governing rule; 1; 2; 3; 4; 5; 6; 8; 9; 10; 12; 13 |
| `governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md` | 2; 3.8; 3.9 |
| `governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md` | 1; 2; 5; 12; 13; 14 |

### Retrospective character reconstruction

| Document | Selected sections |
|---|---|
| `AGENTS.md` | full |
| `governance/AUTHORITY_STATE.yaml` | full |
| `governance/AUTHORITY_SCOPE.json` | full |
| `governance/repository-controls/change-obligations.json` | full |
| `governance/policies/PUBLICATION_AND_CONTRIBUTION_POLICY.md` | full |
| `governance/CHATGPT_AUTHORITY_AND_ROUTING.md` | 2; 3; 4; 6; 7; 8 (own text); 8.1; 10.1; 12; 13 |
| `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md` | Before editing; Maintained documents: targeted edits (own text); Branch routing and cleanup; Change obligations; Execution profiles (own text); Local clone mode; Before and after publication (own text); Stable analytical branch profile; Stable analytical publication sequence (own text); Analytical corrections and procedural conflicts; Multi-session analytical candidates |
| `governance/policies/BRANCH_LIFECYCLE.md` | Continuing analytical branches |
| `governance/policies/AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md` | full |
| `governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md` | 1; 2; 3; 4; 8; 9; 11; 12; 13; 14; 15; 16; 18; 19; 21 |
| `governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md` | 1; 2; 3; 4; 5; 6; 8; 9; 10; 11 |
| `governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md` | 2; 3.8 |
| `governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md` | 1; 2; 6; 7; 8; 10; 11; 12; 13; 14 |
| `governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md` | 1; 2; 3; 4; 5; 6; 7; 8; 10; 11; 12; 13; 14 |

### New series and first reading

| Document | Selected sections |
|---|---|
| `AGENTS.md` | full |
| `governance/AUTHORITY_STATE.yaml` | full |
| `governance/AUTHORITY_SCOPE.json` | full |
| `governance/repository-controls/change-obligations.json` | full |
| `governance/policies/PUBLICATION_AND_CONTRIBUTION_POLICY.md` | full |
| `governance/CHATGPT_AUTHORITY_AND_ROUTING.md` | 2; 3; 4; 6; 7; 8 (own text); 8.1; 10.1; 12; 13 |
| `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md` | Before editing; Maintained documents: targeted edits (own text); Branch routing and cleanup; Change obligations; Execution profiles (own text); Local clone mode; Before and after publication (own text); Stable analytical branch profile; Stable analytical publication sequence (own text); Project-initiation architecture gate |
| `governance/policies/BRANCH_LIFECYCLE.md` | Continuing analytical branches |
| `governance/policies/AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md` | full |
| `governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md` | 1; 2; 3; 4; 8; 9; 11; 12; 13; 14; 15; 16; 18; 19; 21 |
| `governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md` | 1; 2; 3; 4; 5; 6; 8; 9; 10; 11 |
| `governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md` | Governing rule; 1; 2; 3; 4; 5; 6; 8; 9; 10; 12; 13 |
| `governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md` | full |
| `governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md` | 1; 2; 3; 4; 5; 12; 13; 14 |
| `governance/MANGA_ANIME_CORPUS_INDEX.md` | full |

### Analytical tranche acceptance/publication

| Document | Selected sections |
|---|---|
| `AGENTS.md` | full |
| `governance/AUTHORITY_STATE.yaml` | full |
| `governance/AUTHORITY_SCOPE.json` | full |
| `governance/repository-controls/change-obligations.json` | full |
| `governance/policies/PUBLICATION_AND_CONTRIBUTION_POLICY.md` | full |
| `governance/CHATGPT_AUTHORITY_AND_ROUTING.md` | 2; 3; 4; 6; 7; 8 (own text); 8.1; 10.1; 12; 13 |
| `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md` | Before editing; Maintained documents: targeted edits (own text); Branch routing and cleanup; Change obligations; Execution profiles (own text); Local clone mode; Before and after publication (own text); Stable analytical branch profile; Stable analytical publication sequence (own text); Multi-session analytical candidates |
| `governance/policies/BRANCH_LIFECYCLE.md` | Continuing analytical branches |
| `governance/policies/AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md` | full |
| `governance/source-policies/MANGA_ANIME_REASONING_AND_MODEL_ROUTING_POLICY.md` | 1; 2; 3; 4; 8; 9; 11; 12; 13; 14; 15; 16; 18; 19; 21 |
| `governance/source-policies/MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md` | 1; 2; 3; 4; 5; 6; 8; 9; 10; 11 |
| `governance/source-policies/MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md` | 1; 2; 10; 11; 12; 13; 14 |
| `governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md` | full |

### Cross-cutting governance/validation

| Document | Selected sections |
|---|---|
| `AGENTS.md` | full |
| `governance/AUTHORITY_STATE.yaml` | full |
| `governance/AUTHORITY_SCOPE.json` | full |
| `governance/CHATGPT_AUTHORITY_AND_ROUTING.md` | full |
| `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md` | full |
| `governance/policies/BRANCH_LIFECYCLE.md` | full |
| `governance/repository-controls/change-obligations.json` | full |
| `governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md` | full |
| `governance/source-policies/MANGA_ANIME_SEQUENTIAL_EXECUTION_SCOPE_AND_CONTINUATION_POLICY.md` | full |
| `governance/repository-controls/project-initiation-gate.json` | full |
| `governance/policies/REPOSITORY_CONTROLS.md` | full |
| `governance/policies/ARTIFACT_ELIGIBILITY.md` | full |
| `governance/policies/AUDIT_EXECUTION.md` | full |
| `governance/policies/PUBLICATION_AND_CONTRIBUTION_POLICY.md` | full |
