# Authority epoch 1: activation and acceptance record

This is the durable record of how Git analytical authority epoch 1 was activated, stabilized and accepted. It is history, not a routing instruction: live routing is `governance/CHATGPT_AUTHORITY_AND_ROUTING.md`, live authority state is `governance/AUTHORITY_STATE.yaml`, and the frozen activation scope is `governance/AUTHORITY_SCOPE.json` with its machine cutover record `AUTHORITY_EPOCH_1.json` beside this file.

The sections under "Activation-era routing text" were moved verbatim from the routing document (revision 2.7) on 2026-10-15; their only change is one heading level. The routing document keeps the Drive master-index rule (its 10.2) and the state meanings (its 11), which still govern any later Drive pointer update, rollback or recovery. Git history holds every earlier revision.

## Acceptance

- **Accepted:** 2026-10-15, by the owner: "Daily stabilization ended and is accepted, migration is complete."
- **Effect:** `AUTHORITY_STATE.yaml` records `GIT_ACTIVE_ACCEPTED`, migration gate G9 complete, and daily stabilization ended. The routing document's `document_status` is `ACTIVE_ACCEPTED`.
- **Evidence in Git:** the owner's statement. No day-7 or day-14 audit record and no record of the other prerequisites in the stabilization section below (severity-0/1 defects, refresh tests per Drive-native class, rollback-readiness verification) exist in Git; the owner accepted the epoch without them.
- **Frozen records unchanged:** `AUTHORITY_SCOPE.json` and `AUTHORITY_EPOCH_1.json` keep their activation-time bytes and `GIT_ACTIVE_STABILIZING` state. They record the activation; the scope's SHA-256 is part of the activation tuple, so neither is rewritten for acceptance.
- **Owner follow-up:** the Drive master-index pointer still carries `GIT_ACTIVE_STABILIZING`. Until the owner updates it (and its checksum sidecar), a Drive revalidation that finds that state with an otherwise matching tuple is the expected pre-update state, not a mismatch.
- **Ongoing verification after acceptance:** exact-head integration audits, the post-merge `main` audit, the weekly scheduled full audit, unchanged-revision verification for Drive-native changes, and a triggered full audit on any anomaly.

## Activation-era routing text

**Supersession:** This revision supersedes `CHATGPT_GIT_AUTHORITY_AND_ROUTING_HANDOFF_DRAFT_INERT.md`. The earlier draft remains historical and must not be used as the live handoff.

### 10.3 Prepared Drive pointer template

The following is a template, not an instruction to edit Drive:

```yaml
authority_pointer_schema: 1
state: CUTOVER_PREPARED
repository: deep-blue-zero/anime-manga-ln-games-analysis
authority_epoch: <MONOTONIC_INTEGER>
cutover_id: <UNIQUE_ID>
candidate_commit: <FULL_COMMIT_OID>
activation_tag: <PROTECTED_ANNOTATED_TAG>
authority_scope_sha256: <SHA256>
effective_at: null
```

The active block must contain the same tuple with `state: GIT_ACTIVE_STABILIZING` and a verified effective timestamp. The pointer and checksum sidecar must agree before authority is effective.

### 13. Activation checklist

This document may be changed from `DRAFT_INERT` only through the migration framework.

- [x] Exact GitHub remote verified.
- [x] Hardened framework approved.
- [x] Inventory and classification reconciled by Drive ID.
- [x] Authority scope contains no in-scope blockers.
- [x] Candidate commit and protected annotated tag verified.
- [x] Drive master-index before-image preserved.
- [x] Drive pointer and SHA-256 sidecar updated and verified.
- [x] Git and Drive activation tuples match exactly.
- [x] Live handoff header populated with non-null cutover values.
- [x] Separate user authorization for cutover recorded.
- [x] Post-activation handoff commit reviewed and merged.

All activation conditions passed for epoch 1. Any later mismatch triggers the fail-closed recovery behavior above.

### 14. Approved stabilization operation

Git is live for `GIT_PRIMARY` work throughout the approved 14-day stabilization period. Stabilization is heightened observation, not a moratorium on new analysis.

Cadence:

- Day 0: full post-cutover baseline audit;
- Days 1–14: daily lightweight, read-only Drive/Git delta checks;
- Day 7: full ID-level reconciliation and repository integrity audit;
- Day 14: final full reconciliation and acceptance-readiness audit;
- after every Git integration: targeted local or exact-tree validation followed by remote-head verification and the single full `main` repository audit; the originating transaction remains open until that audit passes;
- after every Drive-native change: unchanged-revision export-and-merge verification;
- on any anomaly: immediate triggered full audit.

Daily audits distinguish expected Drive-native work, primary-source activity, evidence/binary storage, misrouted Git-primary analysis, and ambiguous changes. They do not require legitimate Drive activity to stop. Misrouted analysis is preserved and reconciled; it is never automatically deleted or overwritten.

Final `GIT_ACTIVE_ACCEPTED` status requires zero unresolved severity-0/1 defects, one verified Git-native analytical change, one refresh test per Drive-native artifact class, successful rollback-readiness verification, and explicit owner acceptance.

### 15. Active epoch-1 tuple

- Authority epoch: `1`
- Cutover ID: `g8-authority-epoch-1-20260902T134713Z`
- Activation commit: `01561d0c9398917c1329501b798733041ab17e98`
- Protected annotated tag: `activation/authority-epoch-1`
- Authority scope SHA-256: `008b7b2adf114c1f39dd86fae064344457dab5b9e45486623fc9237fb6ed0916`
- Effective timestamp: `2026-09-02T14:20:11Z`

The activation commit fixes the corpus boundary. Later commits on `main` may add governance records and authorized Git-primary analysis without changing that boundary; any new authority epoch requires a new protected activation tuple.
