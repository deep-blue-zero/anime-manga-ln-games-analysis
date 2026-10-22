# Repository Pre-Commit Guidance

This is the author's checklist for every change to this repository, by a person or any agent. It covers editing, validating and publishing a branch. Integration into `main` is the CI agent's job under `NIGHTLY_ANALYTICAL_INTEGRATION.md`; an author's task ends when its branch is pushed, its PR is open, and its exact-head audit has passed. This checklist grants no repository, Drive, publication or merge authority.

## Before editing

1. Read `AGENTS.md` and the sections of this checklist that the operation needs. The [task-dependent reading path](../AGENT_ROUTING.md#6-mandatory-first-read-order) selects any further policy by responsibility.
2. Start from a branch based on current `origin/main`, named under `BRANCH_LIFECYCLE.md`.
3. Declare the paths you intend to change. Never use `git add .`, wildcard staging, force-push or history rewriting.

On a `series/` or `studies/` branch, author the named analytical root and any routing descriptor; housekeeping owns the five routing outputs (`AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md`). The character and reconstruction files belong to their agents and are not edited by analysis authors.

### Checklist acquisition by operation

Every edit uses **Maintained documents: targeted edits** and **Change obligations**. Publishing uses **Execution profiles**, the matching **Local clone mode** or **GitHub API or connector mode**, and either the **Stable analytical branch profile** with the **Stable analytical publication sequence**, or the **Local or cross-cutting profile**. Read **Project-initiation architecture gate** before initiation, a material restart or sequential admission; **Analytical corrections and procedural conflicts** before correcting analysis; **Multi-session analytical candidates** before accepting transferred analysis; and **Squash-merge reconciliation** for a branch last integrated by squash.

## Project-initiation architecture gate

Before opening a new substantive analytical root, materially restarting a project, or staging a project's first substantive sequential reading, read Section 3 of `../source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md`. Its Section 3.8 covers the lock, run stops and terminal closures, and Section 3.9 states what the validator enforces through `../repository-controls/project-initiation-gate.json`. An absent, CLOSED, malformed or contradictory lock stops a new sequential reading.

## Analytical corrections and procedural conflicts

This implements Section 4.2 of `../AGENT_ROUTING.md`: analytical accuracy and source fidelity are the substantive objectives, and controls exist to preserve them. It adds no write, source, publication or merge authority.

### Correcting analysis

1. **Use the ordinary route first.** Correct a current claim in its canonical home through the project's claim-revision system or the archive transition vocabulary (`PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, `OPEN`), keeping claim IDs, earlier formulations and revision history recoverable. Correct a frozen reading, prospective freeze, source receipt or closure-sealed artifact by an attributable erratum, claim revision or superseding artifact, never by editing its bytes. Do not write retrospective corrections back as prospective knowledge.
2. **Show an error, not a preference.** A substantive correction records source locators and provenance, material counterevidence and competing readings, remaining uncertainty, and whether each statement is observation, inference, hypothesis or value judgment. Another session's or model's conclusion, or the correcting agent's confidence, is not evidence of error. Unresolved disagreement stays recorded as disagreement.
3. **Record a blocked correction.** If a correction cannot be completed under the current authorization, do not leave the defective claim presented as unqualified current authority. Record the defect, affected claims and exact blocker in the project's current-state, claim/revision or audit home when the task's paths allow, and in the task report otherwise.

### Resolving a conflict between a control and a correction

A procedural conflict exists when a rule, validator check or process demonstrably prevents an otherwise authorized, evidence-backed correction. A scope or validation failure alone does not prove the control defective; it may be correctly requiring authorization the task lacks. Propose the narrowest remedy (an ordinary route, then an erratum or superseding version, then a validator repair, then a procedure amendment, and only then a bounded exception) in the project's blocker record or the amending PR's description, stating the affected claim, the evidence, the conflicting control with its exact output, and who must authorize the remedy.

Proposing is not executing. Executing a remedy needs owner authorization naming its exact scope. Never weaken or suppress a failing check, or change tests, to manufacture a passing result.

## Maintained documents: targeted edits

These rules apply to maintained analytical prose, ledgers, readiness tables, project-local indexes and other authored documents, in clone and connector workflows alike. A filename containing "index" or "ledger" does not make a file generated.

- **Edit, don't regenerate.** Read the complete current file at a known commit before changing it. Search excerpts, previews and truncated reads are not a complete source. Apply targeted patches with verified old text; if the target is missing or ambiguous, re-read rather than broadening the replacement.
- **Preserve everything else byte-for-byte**: unaffected prose, front matter, record IDs, table columns, ordering, headings, anchors, links, history, encoding and line endings. No incidental reflow, normalization or cleanup.
- **Respect ledger semantics.** Append where the ledger's history model requires it, update current-state rows when evidence changes their meaning, and follow stricter append-only or frozen rules.
- **Generated files use their generators.** A document-wide rewrite needs an explicit owner request or a reviewed transformation. Neither file size nor a connector failure ever authorizes reconstructing a document from memory, summaries or excerpts.
- **Review the complete diff** for missing sections, rows, citations or history, and for unexpected size or line-count changes. After writing, read back the resulting file and changed-file set.

### Multi-session analytical candidates

When integrating a substantial artifact produced in another session, apply `../source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md`: verify the full delivered contents, base and source boundary, target identity, required evidence coverage, and drift from current state before replacement. Stage completion, semantic acceptance, repository validation and authority promotion are distinct steps.

### GitHub connector limits and failed writes

A contents or tree API may need the full updated file. Build that payload from the complete verified source plus targeted edits, use current blob SHAs and non-forced ref updates, and prefer one atomic commit for files that must stay consistent. If a read is truncated or a payload cannot be handled reliably, move the edit to a Git-capable environment or report the blocker with a proposed patch; never replace the document approximately. After a timeout or ambiguous response, inspect the remote branch before retrying, and retry only what is missing.

## Branch routing and cleanup

Branch names, retention and pruning follow [`BRANCH_LIFECYCLE.md`](BRANCH_LIFECYCLE.md).

## Change obligations

The machine-readable form of this table is `governance/repository-controls/change-obligations.json`.

| Change | Required synchronization |
| --- | --- |
| Any tracked add, delete, or rename | No global path list; the Git tree is the live inventory. Apply the semantic obligations below. |
| Add, remove, or reroute a series root | On a stable series branch, provide `.repository/series-registry.json`; housekeeping updates `series/registry.json`, `series/README.md` and the corpus index. Elsewhere, update those outputs in the same change. Automatic removal is prohibited. |
| Add, remove, or reroute a study root | On a stable study branch, provide `.repository/study-registry.json`; housekeeping updates `studies/registry.json`, `studies/README.md` and the corpus index. Elsewhere, update those outputs in the same change. Automatic removal is prohibited. |
| Add new eligible character analysis | The discovery agent enrolls it on a later run; nothing is required in the same change. |
| Change already referenced evidence | Existing character references must still validate; a break is repaired under `CHARACTER_DISCOVERY_MAINTENANCE.md` before merge. |
| Change the reconstruction capability registry | Only on `character-reconstruction`, regenerating `characters/CHARACTER_RECONSTRUCTION_INDEX.md`. Evidence changes that make an assessment stale need no same-change update. |
| Add or change a Drive-only reference | Update the Drive artifact reference index and verify every referenced anchor. Do not rewrite frozen migration crosswalks. |
| Initiate or materially restart a substantive analytical project | Declare `project_initiation_gate: REQUIRED` in the root's routing descriptor and satisfy the project-initiation validator. |
| Change policy, schema, validation, workflow or controls | Run the affected focused tests and the full gate (below). Guardrail paths are merged only by the owner. |

Ordinary edits inside an existing registered root need no unrelated registry or catalog churn.

## Execution profiles

Both profiles start from Section 8 of `../AGENT_ROUTING.md`. Series and study branches also follow the [stable analytical branch profile](#stable-analytical-branch-profile) and the [publication sequence](#stable-analytical-publication-sequence). Both end with a pushed branch, an open PR and a passing exact-head audit.

### GitHub API or connector mode

1. Fetch `main` and the exact target-branch head; the branch must be based on, or reconciled with, current `main`.
2. Fetch the complete contents and blob SHA of every path you will change.
3. Confirm the provider records an author from `allowed_author_identities` and a committer from `allowed_committer_identities` in `governance/repository-controls/tracked-file-policy.json`. The GitHub server identity may commit but never author.
4. Write only the declared paths, built from verified originals plus targeted edits, with current blob SHAs and an atomic multi-file commit where supported.
5. Read back the resulting commit, each changed file and the complete branch delta; open or update the PR.

### Local clone mode

1. Fetch the target branch, check `git status`, and stop on unrelated or ambiguous worktree changes.
2. Edit only the declared paths through targeted patches.
3. Stage exact paths with `git add -- <path>...`.
4. Run `python tools/prepare_commit.py --base origin/main --write-generated` and stage each generated path it reports.
5. Run `python tools/prepare_commit.py --base origin/main --check`, adding `--full` where the profiles below require it.
6. Inspect `git diff --cached --check` and the complete staged diff, commit, push without force, and open or update the PR.

If authenticated GitHub access is unavailable, request it or return a proposed patch. Never write the analytical change to Drive instead.

## Stable analytical branch profile

Stage only the declared analytical files and any routing descriptor, then run author preflight against the staged index:

`python tools/validate_repository.py --phase current --snapshot index --routing-preflight series/<stable-slug> --repo .`

Use `studies/<stable-slug>` for a study. Preflight validates a read-only projection of the five routing outputs and confines the branch to its own root, the routing outputs and a two-file character repair. `AWAITING_SYNCHRONIZATION` means housekeeping will regenerate routing after the push; it is not a failure. A real new root needs its routing descriptor and a current-eligible entrypoint with complete authority metadata. For a noncurrent working draft, use the `draft_noncurrent` template in `../../characters/README.md`; never promote a draft to current authority to pass a check.

## Local or cross-cutting profile

1. Stage only the declared paths by exact pathname.
2. Run `python tools/prepare_commit.py --base origin/main --write-generated` and stage only the generated files it reports.
3. Run `python tools/prepare_commit.py --base origin/main --check` once the worktree and index agree.

The default check is diff-aware: obligations, registered-root topology, generated catalogs, staged whitespace, focused tests and affected character output. Add `--full`, which runs every test through `tools/audit_execution.py`, when changing validation, workflows, schemas, publication safety or other controls, or when asked. Do not commit or push on any failure.

## Before and after publication

1. Inspect the exact staged path list, diff, generated changes and file sizes.
2. Confirm an approved author and committer identity.
3. Push without force. If the push is rejected, fetch, merge, revalidate and push again.
4. Wait for a successful `Repository integration audit` on the exact head (housekeeping's child commit when it regenerated routing). Pending, superseded, missing, skipped, cancelled or failed results do not finish the task.

### Stable analytical publication sequence

For every push to a continuing series or study branch, including connector publication:

1. **One validation at a time.** Wait for the previous push's exact-head audit before publishing the next tranche; analysis preparation may continue meanwhile. A coordinated correction may supersede a running audit, but its new head needs its own audit.
2. **Start from both current heads.** Fetch `origin/main` and the remote branch, keep any intervening author, housekeeping or curation commits, and merge `main` if it is not an ancestor.
3. **Validate the reconciled candidate** with author preflight and a complete diff review, repeating checks if reconciliation changed it.
4. **Push without force** and read back the resulting commit. If housekeeping or another writer advanced the branch, keep that work; never claim an older commit certifies a newer head.
5. **After integration**, merge current `main` into the branch before the next tranche. Integration uses merge commits, so the integrated tip is already part of `main`.

### Squash-merge reconciliation

Branches integrated by squash before merge commits were adopted are not ancestors of `main`, so their next merge may conflict. The merge gate never resolves conflicts; the branch's author or the CI agent does, once:

1. Find the branch's last merged PR, record its source head and integration commit, and confirm both are in the expected histories.
2. Compare the full trees of that source head and its integration commit. If they match, the squash preserved every byte, and each side's later changes can be reconciled normally. If they differ, review the integration patch before resolving anything.
3. Resolve only what that evidence supports; never choose `ours` or `theirs` across a file without it. Use an ordinary merge commit, revalidate, and push without force. Report semantic or provenance conflicts instead of guessing.

Do not modify the archived migration records in `governance/archive/migration/` or the frozen Drive-to-Git migration crosswalks.
