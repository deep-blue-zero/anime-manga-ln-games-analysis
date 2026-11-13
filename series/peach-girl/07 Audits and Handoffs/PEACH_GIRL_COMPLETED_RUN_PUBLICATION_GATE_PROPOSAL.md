---
title: Peach Girl — Completed-run publication gate proposal
artifact_id: PEACH_GIRL_COMPLETED_RUN_PUBLICATION_GATE_PROPOSAL
artifact_type: governance_proposal
series: Peach Girl / ピーチガール
series_id: peach-girl
generation: PEACH_GIRL_BOOTSTRAP_V1
version: '1.1'
status: draft_noncurrent
scope: Proposed separate reviewed governance repair; not an executable waiver
source_boundary: Preserved completed original-manga history;actual live-main publication
  preflight failure
canonical_home: series/peach-girl/07 Audits and Handoffs/PEACH_GIRL_COMPLETED_RUN_PUBLICATION_GATE_PROPOSAL.md
created: '2026-10-20'
review_status: REPAIR_PR_256_MERGED_ANALYTICAL_REVIEW_PENDING
supersedes: []
superseded_by: []
do_not_use_as_current_authority: true
do_not_use_as_literary_evidence: true
---

# Completed local run: publication gate conflict and proposed route

## Affected artifact and actual failure

The owner requested publication to series/peach-girl. The staged candidate preserves all 18 frozen readings, the completed/NONE run state, all analytical history and approved current main content. The unmodified current main validator rejects this first publication:

> new sequential admission requires an active authorized run; OPEN alone is insufficient

In tools/validate_repository.py, _validate_run_admission permits completion only when the prior main entry already records an active run. Live main c5646c50f8e7cc0b7ea6ac79204cd3e2558bb5a5 still has the closed, zero-reading bootstrap. The source branch instead contains real owner authorization/active-run history, per-volume atomic closures, then completion.

## Verified evidence

- Local release c8f5f9d8ff58207bdfc6459b9da2a3b49507f692 and its independently verified backup/portable ZIP remain unchanged.
- V18 first completed commit 0ee85e10ee4bf0cc5b04d0824c959e2509b9ec9f has actual active V17 parent af76e3b678a45b70634db805934ec8ddaa459ef5. Entering/terminal bounds are V01–V18; all 18 frozen reading bytes remain exact.
- G1/G2 verification binds every first-closure commit/reading/freeze, and G6 verifies their full preservation.
- Prior PR 177 source 589343261ea63f4d521c8fafac628f4dc24361cb and squash c37de60b5da7b80aee27d6a04658801e53f11632 have identical complete tree d9161f8ffac593b1755540833b4a8fc02de41a7a. Main has not edited the conflicting Peach Girl bootstrap files since integration.
- Eight add/add conflicts were resolved only after that proof; current main governance, tooling, curation and unrelated project content were preserved. No global control was authored or weakened.
- Before repair authorization, owner identity and live main/activation rulesets were verified and no remote write occurred. The subsequent governed repair publication is recorded below. No force push or history rewrite occurred.

## Ordinary remedies and their limits

Reconciliation and normal actual-main preflight were performed; the failure is not stale routing or unrelated source content. The earlier local predecessor replay checks do not certify publication and are not substituted for this failed real-main check.

Relabeling the completed run active, assigning a fictitious next narrative unit, rewriting freezes or changing the comparison ref for public validation would misrepresent the work. A project run-stop record cannot seal these unintegrated bytes because that route requires a completion commit already on main. Publishing an intermediate active tranche and integrating it first would require separate main-integration authority and serialize an incomplete tranche; the current request authorizes branch publication only.

## Proposed separate reviewed change

Authorize a narrow governance repair on the required temporary governance branch, then complete this branch publication after its reviewed integration:

1. Clarify completed-local-run publication in governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md without changing owner source authorization, freeze immutability or closure semantics.
2. Update tools/validate_repository.py to accept only a verifiable historical active-to-completed transition with unchanged bounds and exact frozen reading bytes. The route must work for both source preflight and post-squash main audit, fail closed on missing historical objects or inconsistent state, and reject added/altered post-completion readings.
3. Add regression coverage in tools/tests/test_project_initiation_gate.py for valid batched publication, missing active history, expanded bounds, altered/added readings, missing history and post-squash audit. An explicit immutable project binding may be needed; its exact format must be part of the reviewed design, not an ad hoc exception.

This bounded proposal is not a validation waiver. At proposal time no implementation or control edit had been applied. Subsequent owner authorization and implementation are recorded below. Reviewed integration, focused tests and the full executable-validation gate are required before using the repaired route. All existing negative admission and laundering tests remain required.

## Disposition before reviewed integration

PENDING_REVIEWED_GOVERNANCE_INTEGRATION. The owner answered “Yes” to implementing this repair through the reviewed route, with regression tests, then finishing the already authorized analytical push. The owner also specified a second-agent review/audit of the analytical outputs once admission is enabled. That review is not yet performed.

The separate codex/completed-run-publication branch changes the owning initiation policy, tools/validate_repository.py, tools/completed_run_publication.py, tools/tests/test_project_initiation_gate.py, tools/tests/test-catalog.json and the existing tools/tests/test_git_snapshot_io.py deletion fixture. That fixture clears a disposable Git object's Windows read-only attribute and confirms deletion, preserving its original missing-history/no-lazy-fetch assertions; it changes no runtime gate or test-selection rule. The optional project-local binding is self-contained textual Git evidence: two original commit objects, the required tree nodes and historical Markdown blobs. Its integrity and exact reading-set checks do not depend on source commit objects remaining available after a squash.

The actual Peach Girl proof binds active parent af76e3b678a45b70634db805934ec8ddaa459ef5 to completion 0ee85e10ee4bf0cc5b04d0824c959e2509b9ec9f. The real staged analytical candidate passed a private full author preflight with the proposed validator, including the ordinary actual-main comparison. This does not certify publication under accepted main controls. The reconciled full staged gate passed against main 4825fbc310c1192ba27fab58a16484a4f518f906: 391 tests, zero failures/errors, three existing Bash-unavailable skips. The exact Git tree is 1e44bcf5a1a820a2ad2fd33c5bc1c9095ce25066. Commit 18d2b3db5de9f9d57f1173d77d611ba4873de11f and all six published files were read back and byte-verified. [Governance PR 256](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/256) passed its [independent exact-head Ubuntu audit](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/actions/runs/39510663136): all 391 tests, zero failures/errors/skips, and successful Repository integration audit status. The owner must still perform its protected merge personally. Admission is not enabled on accepted main yet.

The repository integration policy reserves protected merges of governance/validator changes to the owner personally. After that reviewed merge and fresh ordinary preflight, publish the stable analytical branch, complete source/housekeeping/final audits, and preserve a draft/explicit hold for the second agent's review. No analytical main integration is authorized. The analytical merge/index and earlier exact release archive remain preserved; no source reading or freeze was edited.

## Reviewed integration — 2026-10-23 verification

[PR 256](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/pull/256) was merged on 2026-10-21 at 0a6888617e6eae89d835e3bba736073a0a44857b; its final reviewed source head 52df1e9b5a6cd9cc39c482dc89f4729a138bb8f5 has the same complete Git tree. The accepted repair additionally preserves main's active/blocked/interrupted/malformed run boundaries and parses commit parents using Git's LF/header semantics, with regression coverage. Its [post-merge audit](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/actions/runs/39537289532) passed 431 tests with no failures, errors or skips. Current main 297bc0d05040a24facbeb5440481b9c604de5568 contains the repair and has a [successful 459-test audit](https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/actions/runs/39927029229), also without failures, errors or skips. The previous pending-integration blocker is resolved. The analytical candidate incorporates current main; its ordinary author preflight, remote readback and exact-head publication audit remain required. This proposal remains noncurrent historical rationale, not an authorization or literary authority. The designated second-agent analytical audit and explicit integration hold remain pending.
