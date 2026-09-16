---
title: Manga / Anime Analytical Handoff and Integration Contract
artifact_id: MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT
artifact_type: analytical_handoff_integration_contract
version: "1.0"
status: canonical
scope: cross-session analytical transfer, evidence-state preservation, receipt, and integration acceptance
created: 2026-09-13
maintainer: ChatGPT + user
do_not_use_as_current_authority: false
do_not_use_as_literary_evidence: true
canonical_home: governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md
drafted_against_commit: b331a3b746622760db394ac1a79367263236336f
supersedes: null
superseded_by: null
---

# Manga / Anime Analytical Handoff and Integration Contract

> **Transfer the artifact, its evidence boundary, its unresolved obligations, and the exact state on which it was built. A prose summary alone is not an adequate transfer of substantial analysis.**

This contract defines cross-session transfer and acceptance. The [topology policy](MANGA_ANIME_EXECUTION_TOPOLOGY_AND_CAPABILITY_ROUTING_POLICY.md) allocates execution responsibilities; the [long-series protocol](MANGA_ANIME_LONG_SERIES_HYBRID_EXECUTION_PROTOCOL.md) defines phase readiness. Existing repository authority and [pre-commit guidance](../policies/CHANGE_INTEGRATION_CHECKLIST.md) continue to control publication.

The reusable [stage handoff template](templates/MANGA_ANIME_ANALYTICAL_STAGE_HANDOFF_TEMPLATE.md) implements this contract. Its headings and YAML are a documentation template, not a newly enforced repository schema. Equivalent established project formats are acceptable when the required information remains recoverable.

## 1. When a handoff is required

Use this contract when responsibility moves to a different session/environment and the receiving operation could otherwise lose scope, source provenance, analytical substance, unresolved evidence needs, or concurrency state. Important examples are architecture-to-local integration, local-to-cloud synthesis, cloud-to-local AV completion, and interrupted long-run recovery.

A trivial internal action need not create a new artifact. For substantial transfers, use one operational packet with one start-here surface. This packet does not become another current series entrypoint.

## 2. Identity, scope, and authority

Retain the analytical artifact's established ID and canonical target path across sessions. A transfer ID identifies the transaction; it does not replace the artifact ID. Different responsibilities may warrant distinct artifacts, but environment labels alone do not justify `CLOUD_ANALYSIS`, `LOCAL_ANALYSIS`, and `FINAL_ANALYSIS` as competing monographs.

Record current authority using the existing policy and eligibility rules. A working cloud copy is not canonical merely because its ID matches a canonical artifact. A local commit does not establish semantic validity merely by existing. Preserve the adopted version until its successor is explicitly accepted through the applicable process.

Use operational stage states separately:

| `stage_state` | Meaning |
|---|---|
| `PLANNED` | Assignment defined; work not begun |
| `IN_PROGRESS` | Assigned work underway; results may be incomplete |
| `READY_FOR_HANDOFF` | Producer's declared scope is finished or truthfully bounded; transfer prepared |
| `ACCEPTED` | Receiver has verified the transfer and accepted responsibility |
| `BLOCKED` | A named requirement prevents the next assigned action |
| `INTEGRATED` | Accepted changes incorporated into the designated target; exact result recorded |

These states are not replacements for CANONICAL, ACTIVE/PROVISIONAL, SUPERSEDED, or HISTORICAL/LEGACY. `READY_FOR_HANDOFF` does not imply full artifact readiness; `INTEGRATED` does not by itself mean merged to `main` or cleared of all later-stage work.

## 3. Minimum transfer contents

A substantial packet must make the following recoverable. It may use a single Markdown record plus the delivered documents rather than many sidecars.

| Field group | Required information |
|---|---|
| Identity | Transfer ID, project/root, canonical entrypoint, artifact IDs and target paths |
| Assignment | Producer/receiver roles, assigned stage, requested output responsibility, permitted changes, next action |
| Authorization | Recoverable current owner instruction, permitted source range, write scope, and continuation boundary |
| Base | Repository, branch when relevant, full commit, current target blob/hash where available, governing policy/method revisions |
| Evidence | Source inventory/version, language/edition/continuity, inspected corpus boundary, routes to relevant witnesses |
| Inputs | Required artifacts, exact paths/IDs, version/hash references, access/inspection status, missing inputs |
| Outputs | Exact delivered files, intended role, identity/path, bytes/hash and version where available |
| Analytical state | Main conclusions, counterreadings, claim changes, unresolved questions, evidence limitations |
| Remaining work | Mandatory versus optional work, claims affected, acceptable resolution, responsible next stage |
| Preservation | Existing prose/IDs/locators/freezes that must remain intact; work that must not be redone |
| Receipt | Receiver integrity check, base drift assessment, acceptance/blocker, integration result and unresolved items |

Exact file hashes are required for substantial delivered files whenever their bytes are accessible. When bytes cannot be obtained, record the exact provider revision/ID and that integrity is not yet verified. The recipient must resolve that gap before applying a destructive replacement; never invent a checksum or mark an inaccessible file verified.

Do not include credentials, signed access tokens, unnecessary personal paths, raw media, or private acquisition material in a public receipt. A full private transport manifest and a sanitized public integration record may have different publication scopes; do not label both as interchangeable canonical analytical sources.

## 4. Source and knowledge boundaries

Specify the analyzed source boundary separately from the inventory that happens to be available. Include continuity, edition, language, release/build or inventory revision when material, and whether retrospective knowledge is allowed.

For prospective work, freeze entering and exiting knowledge boundaries. A recipient may have access to later documents but must not use them when the assignment excludes them. A new handoff does not authorize a new source range, adaptation, language witness, or live-service release.

A live-service assignment must use an exact locked inventory or other recoverable boundary rather than an indefinite description such as all current material. A later source release is a separate scope decision.

Distinguish primary evidence, deterministic derivatives, sequential interpretation, cumulative synthesis, and hypotheses. Availability in the same ZIP does not give these objects equal evidentiary status.

## 5. Input completeness and retrieval

The packet must contain the full produced analysis, not merely an abstract. It must provide sufficient source and corpus routes to test consequential claims without reconstructing the project from conversation history.

For large corpora, include a compact dispatch manifest and verified retrieval routes rather than insisting that every source fit in one upload. Mark inputs as fully inspected, partly inspected, available but not inspected, or inaccessible. These are inspection claims; a directory count is not proof of a reading.

The receiving session first reads governing state, scope, target contract, and unresolved questions, then retrieves the material needed for its analytical role. A source inventory is not itself evidence that the model consumed every listed item. Do not falsely report complete corpus coverage because search returned relevant snippets.

A useful small bootstrap can direct deep retrieval. A reductive bootstrap that removes contradiction, temporal state, or source distinctions cannot support a comprehensive synthesis by itself.

## 6. Coverage and unresolved evidence obligations

For each material evidence channel or source tranche, record requirement and inspection state independently:

| Requirement | Meaning |
|---|---|
| `REQUIRED` | Necessary to meet the artifact's approved responsibility |
| `OPTIONAL` | Useful enrichment that is not a completion prerequisite |
| `OUT_OF_SCOPE` | Excluded from this assignment; no implied coverage |

| Inspection state | Meaning |
|---|---|
| `COMPLETE_FOR_DECLARED_SCOPE` | Required inspection for the stated boundary completed, with an evidence route |
| `PARTIAL` | Some material inspected; remaining coverage explicitly identified |
| `PENDING` | Assigned but not yet inspected |
| `UNAVAILABLE` | A required access/processing/inspection route failed or does not exist here |
| `NOT_APPLICABLE` | No inspection claim because this channel is outside the responsibility |

Completeness must name a boundary. Do not use an unqualified `audio: COMPLETE` to describe a few sample clips, or `video: COMPLETE` for a set of sampled stills. Record the actual inspection method and sampling limitations.

Unresolved evidence obligations should identify affected claim IDs or stable section locators, the missing observation, source/interval, analytical consequence, next owner, and acceptance condition. Reuse existing claim IDs; do not rename an established claim system to satisfy this template.

For example, a pause may support a bounded timing observation while bodily hesitation remains unverified. The recipient should test the latter, not infer it from the former. A targeted AV question needs a source and interval when available; an unknown interval remains unknown until located.

Required unresolved evidence blocks the corresponding completion claim. Optional enrichment does not block an otherwise adequate scoped artifact. The producer may not silently convert REQUIRED into OPTIONAL to declare success. Scope changes require the authority applicable to the project and explicit recording.

## 7. Claim revision and preservation

Transfer enough of the argument to preserve its intellectual content: reasons, significant evidence, alternative explanations, disconfirming cases, developmental states, and limitations. Do not treat locators as decorative citations that can be dropped in a stylistic rewrite.

Use the archive policy's transition vocabulary:

| Claim/section | Earlier formulation | Transition | Proposed formulation | Evidence and counterevidence | Affected downstream homes |
|---|---|---|---|---|---|
| Existing ID or stable locator | Exact or faithful scoped statement | PRESERVE / STRENGTHEN / REVISE / DOWNGRADE / REJECT / OPEN | Revised bounded statement | Recoverable source route | Exact target paths |

The receiving analyst may revise supported conclusions, but must identify a reason beyond authorship preference or unfamiliarity. Preserve adequate incoming analysis and repair actual gaps. Do not gratuitously redo all prior readings, compress mature prose, discard unresolved disagreement, or convert retrospective corrections into false prospective knowledge.

## 8. Producer closeout

Before handoff, the producer verifies that delivered files exist, their identities and target paths are explicit, scope and limitations match actual work, output hashes/counts match the package, and pending obligations have a next owner.

Read back the final delivered documents. Check for truncation, broken tables, missing sections, unresolved placeholders, corrupted names, unsupported locators, and accidental inclusion of internal operational material. Record known defects rather than passing them off as completed work.

A brief synopsis is useful as navigation, but must accompany rather than replace substantive outputs. The packet should say what must not be redone and what must still be tested.

## 9. Receiver acceptance

Before altering a live target, the receiver:

1. Verifies that this assignment is currently authorized and identifies the right repository/root and entrypoint.
2. Confirms the delivered file list and hashes or equivalent immutable revisions; inspects the actual full outputs.
3. Checks the source and knowledge boundary and the producer's coverage claims.
4. Compares the base snapshot with the current target state.
5. Accepts responsibility for named remaining work or records a precise blocker.

Receipt acceptance is not semantic approval of every claim. The receiver still performs its assigned analysis and the relevant acceptance review. Tool success or a model's own confidence cannot substitute for this check.

## 10. Concurrency and stale-base handling

Where the target has advanced since dispatch, compare the handed-off base, returned candidate, and current target. Do not overwrite newer ledger rows, later source progress, or concurrent specialist corrections with stale whole-file content.

Classify drift as irrelevant to the scope, mechanically reconcilable, semantically material, or unresolved. Document the classification and changed paths. Reassess affected claims when drift is material; do not force a nominally clean merge at the expense of meaning.

The exact-head check required for publication is separate from a file hash. A matching blob does not prove the branch has not advanced. After any ambiguous write, inspect remote state before retrying. The live checklist governs atomic commits, non-forced updates, approved identities, readback, and failure recovery.

## 11. Semantic acceptance criteria

Acceptance must evaluate the artifact's actual responsibility, not only syntax or length. At minimum check source-boundary accuracy, traceable consequential claims, epistemic distinctions, state/relationship specificity where relevant, counterevidence, required-channel closure, consistency with current eligible corpus state, and preservation of incoming analytical substance.

A full raw-source reread is not universally required. Verify the sources needed for high-impact new claims, quotations, contested conclusions, suspect locators, and representative checks appropriate to the artifact. Record the review scope; do not imply exhaustive verification when only a bounded audit was performed.

For AV integration, verify the actual inspection route and whether new findings change interpretation. For mature synthesis, check that it makes an argument rather than restates headings. For reconstruction, check its behavior/state constraints and prediction responsibilities separately from literary prose.

Passing a repository validator is necessary where required, but it is not a literary-quality certificate.

## 12. Publication receipt and promotion

The integration owner records accepted/rejected/deferred outputs, meaningful claim changes, exact target paths, remaining evidence obligations, checks performed and their actual results, resulting commit when one exists, and whether branch publication and main integration occurred.

Do not fabricate a commit ID, test result, or remote readback. A proposal package can legitimately have `published_commit: null` and `repository_checks: NOT_RUN`.

Respect the specialized owners of global indexes and character discovery. Coordinate their work when required; do not edit their outputs simply because this receipt lists them as downstream dependencies.

Promotion to current authority follows existing eligibility and archive rules. An optional open question can remain in a canonical scoped artifact; unresolved mandatory evidence cannot be hidden behind a canonical status label. Preserve a still-current prior version when a proposed replacement is not ready.

## 13. Retention and recovery

Store adopted conclusions in their established topical homes and current state in the canonical entrypoint. Retain a sanitized transfer/integration record only where it has a genuine provenance or recovery responsibility under the project architecture.

Do not commit bulky transport ZIPs or duplicate all input documents. Do not delete non-identical analysis merely because a handoff is over. Retire redundant handoff copies only after useful information is preserved and dependencies checked under the archive policy.

After interruption, recover actual current state and the last verified transfer or source-unit boundary. Distinguish drafted, handed off, accepted, integrated, and published. Never infer completion from the last conversational sentence.

## 14. Common invalid handoffs

A handoff is inadequate when it supplies only a summary of a substantial monograph; lists sources without their scope/versions; calls inaccessible audio inspected; treats frame extraction as continuous-video viewing; omits known contradictions; conceals a failed write; replaces a current entrypoint with a cloud copy; or claims that an unintegrated draft is canonical.

Repair the missing component or deliver truthfully bounded work. Do not solve a transfer defect by inventing evidence or flattening the analysis until it fits a convenient payload.

## Changelog

### v1.0 - 2026-09-13 - Proposed initial contract

Establishes stable identity across relays, source/knowledge boundaries, full-output transfer, requirement-versus-coverage separation, claim-level obligations, stale-base reconciliation, semantic acceptance, and truthful integration receipts.
