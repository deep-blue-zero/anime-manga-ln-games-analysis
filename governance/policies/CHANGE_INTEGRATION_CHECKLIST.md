# Repository Pre-Commit Guidance

This is the mandatory pre-commit contract for every change to this repository, by a person or any agent. It complements `AGENTS.md` and the authority records; it does not expand repository, Drive, publication, or contributor authority.

## Before editing

1. Read `AGENTS.md`, `governance/AUTHORITY_STATE.yaml`, `governance/AUTHORITY_SCOPE.json`, and the applicable checklist sections selected below. The [task-dependent reading path](../CHATGPT_AUTHORITY_AND_ROUTING.md#6-mandatory-first-read-order) selects additional canonical context by responsibility.
2. Begin from an up-to-date branch based on `origin/main`. Follow `BRANCH_LIFECYCLE.md` for the branch name and eventual pruning.
3. Preserve the owner-only authorship policy, the Git/Drive authority boundary, artifact exclusions, and frozen migration records.
4. Declare the intended paths. Never use `git add .`, wildcard staging, force-push, or history rewriting.

For a stable series/study branch, read `AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md`. Author the named analytical root and required series/study routing descriptors; housekeeping owns five routing outputs. Character discovery belongs solely to the curation agent under `CHARACTER_DISCOVERY_MAINTENANCE.md`. It may supply a coordinated pre-merge repair on a source branch, but housekeeping may not write either character output. The reconstruction evaluator alone writes the two reconstruction outputs under `CHARACTER_RECONSTRUCTION_MAINTENANCE.md`; stable branches never carry them.

### Checklist acquisition by operation

Before any edit, read **Before editing**, **Maintained documents: targeted edits** (the seven numbered requirements), **Branch routing and cleanup**, and **Change obligations**. Before a commit or push, also read **Execution profiles** and the applicable **Local clone mode** or **GitHub API or connector mode**, **Before and after publication**, and either **Stable analytical branch profile** plus **Stable analytical publication sequence** or **Local or cross-cutting profile**. Read **Squash-merge reconciliation** before that operation, including conflict repair.

Read **Project-initiation architecture gate** before initiation, material restart or sequential admission; **Analytical corrections and procedural conflicts** before correcting analysis or resolving a control conflict; **Multi-session analytical candidates** before accepting transferred analysis; and **GitHub connector limits and failed writes** before connector mutation or recovery from an ambiguous write. Scope changes activate these sections before the new operation. This selects procedure from this contract; it does not replace or waive it.

## Project-initiation architecture gate

Before opening a new substantive analytical root, materially restarting a project, or staging a project's first substantive sequential reading, read Section 3 of `../source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md`. Its Section 3.8 covers the lock, run stops and terminal closures, and Section 3.9 states what the validator enforces through `../repository-controls/project-initiation-gate.json`. An absent, CLOSED, malformed or contradictory lock stops a new sequential reading.

## Analytical corrections and procedural conflicts

This procedure implements Section 4.2 of `../CHATGPT_AUTHORITY_AND_ROUTING.md`: analytical accuracy and source fidelity are the substantive objectives, and controls exist to preserve them. It adds no write, source, publication, or merge authority.

### Correcting analysis

1. **Use the ordinary route first.** Correct a current claim in its canonical home through the project's established claim-revision system or the archive transition vocabulary (`PRESERVE`, `STRENGTHEN`, `REVISE`, `DOWNGRADE`, `REJECT`, `OPEN`), keeping claim IDs, earlier formulations, and revision history recoverable. Correct a frozen reading, prospective freeze, source receipt, or closure-sealed artifact by an attributable erratum, claim revision, or superseding artifact, not by editing its bytes. Do not write retrospective corrections back as prospective knowledge.
2. **Show an error, not a preference.** A substantive correction records source locators and provenance, material counterevidence and competing readings, remaining uncertainty, and whether each statement is observation, inference, hypothesis, or value judgment. Another session's or model's conclusion, or the correcting agent's confidence, is not evidence of error. Unresolved disagreement stays recorded as disagreement.
3. **Record a blocked correction.** If a correction cannot be completed under the current authorization, do not leave the defective claim presented as unqualified current authority. Record the defect, affected claims, and exact blocker in the project's existing current-state, claim/revision, or audit home when the task's paths allow, and in the task report otherwise.

### Resolving a conflict between a control and a correction

A procedural conflict exists when a rule, validator check, or process demonstrably prevents an otherwise authorized, evidence-backed correction or forces a known error to persist. First determine whether the control is defective or is correctly requiring an authorization the task lacks; a scope or validation failure alone proves neither. A conflict proposal records:

1. **Affected artifact and claim** — exact path, claim or section ID, and the statement, model, or result requiring correction.
2. **Evidentiary basis** — supporting evidence, counterevidence, and uncertainty.
3. **Conflicting control** — the exact rule, validator check with its failure output, or process.
4. **Material consequence** — how compliance would degrade accuracy, preserve a known error, or prevent an otherwise authorized correction.
5. **Ordinary remedies considered** — why existing correction, supersession, or amendment routes are insufficient.
6. **Proposed remedy** — the narrowest sufficient change: an ordinary route, then an erratum or superseding version, then validator repair, then procedure amendment, and only then a bounded exception.
7. **Authorization** — who must approve the remedy and the exact paths, controls, and duration it covers.
8. **Preservation** — how existing evidence, historical records, and prior authority states remain recoverable.
9. **Validation** — the applicable checks, any justified check change with its regression tests, and how the result will be verified.
10. **Disposition** — corrected, superseded, blocked, or deferred, with remaining obligations and their owner.

Keep the proposal in an existing home: the project's audit or current-state blocker record for a project-scoped conflict, and the commit and pull-request description of a governance or control amendment. No separate exception registry or ledger is required.

**Proposal is not execution.** An agent may diagnose and propose within its current task scope. Executing a remedy requires owner authorization naming its exact scope; a diagnosis, a claim of improved accuracy, or a project-local declaration never grants it. An executed exception is narrow, bound to named paths and controls, reviewable, and preserves the original state; it is recorded with the authorizing change and validated like any other change. There is no general validation waiver: a machine-readable exception exists only as a reviewed, schema-bound control with regression tests, such as a `terminal_closures` record. Never weaken or suppress a failing check to pass a commit, or change tests merely to manufacture a passing result. A recurrent conflict calls for amending the procedure. When the remedy needs authorization the task lacks, preserve completed compliant work and report the exact blocker.

## Maintained documents: targeted edits

This rule applies to maintained analytical prose, rolling ledgers, readiness tables, project-local indexes, and other authored documents in both clone and GitHub connector workflows. Update the verified current document through targeted patches by default. Whole-document rewriting follows only the regeneration exceptions below. A filename containing "index" or "ledger" does not make the file a generated artifact.

1. **Establish the exact source.** Verify the intended repository, target branch, path, full base commit, and current blob identity. Obtain the complete current file through a verified read before submitting a full-file replacement. Search excerpts, previews, truncated responses, and selected line ranges are not a complete source. Preserve a trustworthy before-image in the authorized execution environment for comparison.
2. **Define the intended changes.** Identify the affected sections, rows, fields, headings, and cross-references. Apply explicit patches or bounded replacements with verified old text and expected match counts. If the target text is missing or ambiguous, re-read and resolve the discrepancy; do not silently broaden the replacement.
3. **Preserve unaffected content.** Keep unaffected prose, front matter, stable row/record IDs, table columns, ordering, headings, anchors, links, historical entries, encoding, and line endings byte-for-byte. Do not reflow paragraphs, normalize whitespace/Unicode, reorder tables, remove apparently redundant history, or rewrite unrelated sections as incidental cleanup. Apply any expressly required format migration as a separately identified transformation.
4. **Respect ledger semantics.** Append new events or observations where the ledger's history model requires it. Update existing current-state rows when evidence changes their meaning, preserving required historical records and explaining material corrections. Follow stricter append-only or frozen-artifact rules. Targeted editing must still update every affected claim and reference; it is not permission to omit necessary synchronization.
5. **Use the documented regeneration exceptions.** Explicitly generated artifacts must use their designated generator. A document-wide revision is permitted when the owner expressly requests it or an applicable reviewed transformation defines it; review its full scope and preserve required provenance. Neither file size nor a connector failure authorizes reconstruction from memory, summaries, or excerpts.
6. **Review the complete candidate diff.** Confirm every addition and deletion is intended, with no missing sections, rows, citations, authority fields, or history. Inspect unexpected size or line-count changes and formatting churn. Counts alone do not establish preservation, and an abbreviated provider diff is not sufficient if it omits changes. Require the applicable schema, link, evidence, and repository checks.
7. **Handle concurrency and verify publication.** Recheck the target head and blob before writing. If the source changed, retrieve the new version, reconcile and reapply the intended edits, and repeat affected review. After a write, retrieve the exact resulting commit's file and compare it with the reviewed candidate; verify the resulting changed-file set. A success message alone does not establish a correct edit.

### Multi-session analytical candidates

When integrating a substantial artifact produced in another session, apply `../source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md`. Verify full delivered contents, base/source boundary, target identity, integrity, required evidence coverage, and drift from current state before replacement. Preserve supported analysis and historical freezes; record material claim revisions and unresolved obligations.

Stage completion, semantic acceptance, repository validation, and authority promotion are distinct. The handoff does not expand approved paths, bypass exact-head/readback requirements, or transfer character curation or housekeeping ownership to the receiving author.

### GitHub connector limits and failed writes

A GitHub contents or tree API may require the full updated file as its payload. That transport is allowed, but construct the payload from complete verified source contents plus targeted edits, not by generating an approximate replacement. Use current blob SHAs for contents updates and exact base/parent commits with non-forced ref updates for Git-data operations. A blob SHA alone does not prove that the branch has not advanced.

If a read is truncated or a payload cannot be handled reliably, obtain a verified complete read or move the edit to an approved Git-capable environment within the user's access constraints. Do not switch to the owner's local drive when the task is cloud-only. If no available route can preserve the file, report the exact blocker and proposed patch without replacing the document. Continue independent authorized work where possible.

After a timeout, ambiguous response, or failed multi-file operation, inspect the remote branch, commit, and affected blobs before retrying. Determine whether no write, the complete intended write, or a partial/divergent result occurred. Retry only the missing operation against the verified current state; do not replay stale full-file contents or duplicate appended entries. Preserve concurrent work and repair through ordinary commits. When multiple files must remain consistent, prefer an atomic tree/commit and validate the entire resulting change.

These are authoring and verification requirements. Existing syntax and repository checks cannot by themselves prove that a regenerated document retained its analytical meaning.

## Branch routing and cleanup

Branch names, retention and pruning follow [`BRANCH_LIFECYCLE.md`](BRANCH_LIFECYCLE.md): continuing `series/<stable-slug>` and `studies/<stable-slug>` branches, the reusable `character-registry` and `character-reconstruction` branches, and temporary agent branches that are pruned only after their exact tips are verified on a green `main`.

## Change obligations

The machine-readable form of this table is `governance/repository-controls/change-obligations.json`.

| Change | Required synchronization |
| --- | --- |
| Any tracked add, delete, or rename | No global path-list projection. The final Git index/tree is the canonical live path inventory; evaluate the semantic obligations below. |
| Add, remove, or reroute a series root | On a stable series branch, provide `.repository/series-registry.json`; automation updates `series/registry.json`, `series/README.md`, and the corpus index. Elsewhere, update those outputs in the same reviewed change. Automatic removal is prohibited. |
| Add, remove, or reroute a study root | On a stable study branch, provide `.repository/study-registry.json`; automation updates `studies/registry.json`, `studies/README.md`, and the corpus index. Elsewhere, update those outputs in the same reviewed change. Automatic removal is prohibited. |
| Add new eligible character analysis | Daily curation may enroll it after merge if existing character references and generated output remain valid. Character-upsert inputs are no longer required or applied. |
| Change the character registry or already referenced evidence | The curation agent reviews affected records and regenerates `CHARACTER_ANALYSIS_INDEX.md`; evidence changes that invalidate existing discovery require its coordinated repair before source integration. |
| Change the reconstruction capability registry | Only the reconstruction evaluator, alone on `character-reconstruction`, regenerates `characters/CHARACTER_RECONSTRUCTION_INDEX.md`. Evidence or discovery changes that make an assessment effectively stale need no same-change capability update. |
| Add or change a Drive-only reference | Update the Drive artifact reference index and verify every referenced anchor. Do not rewrite frozen migration crosswalks. |
| Initiate or materially restart a substantive analytical project | Declare `project_initiation_gate: REQUIRED` in the root's routing descriptor and satisfy the state-sensitive project-initiation validator. This invariant creates no additional global-index output beyond ordinary root/routing topology obligations. |
| Change policy, schema, validation, workflow, or authority controls | Run the affected focused tests and review the governance effect. Use the explicit full gate for executable validation, workflow, schema, publication-safety, or authority changes. Authority-scope changes require separate owner authorization. |

Ordinary edits, additions, and deletions inside an existing registered analytical root do not require unrelated global registry or catalog churn solely because the path set changed. New or removed series/study roots and other semantic changes still activate the specific obligations above. `G3_BOOTSTRAP_TRACKED_PATHS.txt` remains immutable historical evidence; it is not the live inventory.

## Execution profiles

Both profiles start from the common workflow and preconditions in Section 8 of `../CHATGPT_AUTHORITY_AND_ROUTING.md` and end only when the post-integration `main` audit passes. Stable series/study branches also follow the [stable analytical branch profile](#stable-analytical-branch-profile) and the [publication sequence](#stable-analytical-publication-sequence).

### GitHub API or connector mode

1. fetch `main` and the exact target-branch head; confirm the selected branch is based on or explicitly reconciled with current `main`;
2. fetch the complete current contents and blob SHA for every existing path to be changed at the captured commit; verify completeness before constructing any full-file replacement;
3. confirm that the provider will record an author from `allowed_author_identities` and a committer from `allowed_committer_identities` in `governance/repository-controls/tracked-file-policy.json`; the GitHub server identity may be an allowed committer but is never an allowed author, and wildcard identity patterns are prohibited;
4. create or reuse `series/<stable-slug>` for continuing series work, `studies/<stable-slug>` for continuing study work, or a narrow temporary agent branch (`codex/<purpose>`, `chatgpt/<purpose>` or `claude/<purpose>`) for cross-cutting or one-shot work;
5. construct each candidate from the verified original plus targeted edits, review its complete diff, and write only the authorized paths using current blob SHAs for replacement safety and an atomic multi-file tree/commit when the connector supports it;
6. treat the exact candidate Git tree as the live path inventory and update only the semantic outputs required by the obligation map; an ordinary path change inside an existing registered root does not require a global path-list projection;
7. fetch the resulting commit and each changed file, compare remote contents with the reviewed candidates and the complete branch delta against the validated base; validate formatting, links, structured data, authority records, commit identity, generated outputs, and the exact changed-file set;
8. use the owner-controlled integration route authorized for the change: a pull request when required, or an explicitly authorized ordinary non-forced integration into `main`; never infer merge authority from this handoff or a branch name;
9. immediately before integration, recheck remote-head drift and confirm the reviewed branch delta is unchanged;
10. after integration, fetch the resulting `main` head, verify that its tree or reviewed patch corresponds to the approved change, and require the `main` repository audit to complete successfully before declaring the Git transaction closed.

This profile has no working tree or staging area. Complete verified source contents, exact base refs, blob identities, authorized path lists, commit and branch comparisons, any applicable PR diff, and post-integration `main` verification provide the equivalent safety controls.

Follow the [connector-failure procedure](#github-connector-limits-and-failed-writes) after truncated reads, payload failures, timeouts, or ambiguous writes: inspect remote state before retrying, preserve already applied and concurrent changes, and use an approved Git-capable environment or report a precise blocker when a complete safe replacement is unavailable. Never substitute a summary, omit untouched sections, or repeatedly overwrite from a stale before-image.

### Local clone mode

1. fetch the target branch and inspect `git status`, the current branch, upstream tracking, and the exact base commit; stop on unrelated or ambiguous worktree changes;
2. create or reuse `series/<stable-slug>` for continuing series work, `studies/<stable-slug>` for continuing study work, or a narrow temporary agent branch (`codex/<purpose>`, `chatgpt/<purpose>` or `claude/<purpose>`) for cross-cutting or one-shot work;
3. edit only the authorized paths through targeted patches against the current files, preserving unaffected bytes and document history under the maintained-document rules;
4. stage explicit paths with `git add -- <path>...`; never use `git add .`, a directory-wide add, or wildcard staging;
5. run `python tools/prepare_commit.py --base origin/main --write-generated`, review its outputs, and stage each required generated path explicitly;
6. run `python tools/prepare_commit.py --base origin/main --check`; add `--full` only when explicitly required or when changing executable validation, workflow, schema, publication-safety, or authority controls;
7. inspect `git diff --cached --check`, the exact staged path list, file sizes, and the complete staged diff;
8. commit the reviewed tree on the selected branch and recheck `origin/main` immediately before publication;
9. use the owner-controlled integration route authorized for the change: a pull request when required, or an explicitly authorized ordinary non-forced fast-forward or compare-and-swap update of `main`;
10. after integration, fetch the resulting `main` head, verify remote exactness, and require the `main` repository audit to complete successfully before declaring the Git transaction closed.

An integration that materializes successfully but fails the post-integration `main` audit is not a completed transaction. Preserve the integrated content, treat the repository state as remediation for that change, and repair forward through the applicable routed branch or a narrow temporary remediation branch; do not rewrite published history merely to erase the failed integration commit.

Do not create ordinary content directly on `main`, force-push, rewrite published history, delete protected refs, or broaden repository access. An owner-authorized integration may advance `main` normally from an exact reviewed branch; it may not bypass remote-drift checks or the final `main` audit.

If authenticated GitHub access is unavailable, request connection/authorization or return a proposed patch. Do not silently write the analytical change to Drive.

## Stable analytical branch profile

Stage only the declared analytical files and any required named routing descriptor. In an authorized Git execution environment, run author preflight against the staged index:

`python tools/validate_repository.py --phase current --snapshot index --routing-preflight series/<stable-slug> --repo .`

Use the matching `studies/<stable-slug>` argument for a study. This command validates a read-only projection of the five routing outputs; it does not stage or write them. Review the exact staged diff, approved identities, and applicable whitespace checks before publishing normally. A GitHub connector task follows the complete-read, atomic-commit, non-forced update, and remote-readback rules above and requires the exact published commit's CI preflight.

`AWAITING_SYNCHRONIZATION` permits publishing authored content to the stable branch while routing remains pending. It does not permit integration. A real new root requires its routing descriptor and a current-eligible entrypoint with complete authority metadata. Branch creation without a named root requires neither. For a noncurrent working draft, use the `draft_noncurrent` template in `../../characters/README.md`; do not promote it to current authority merely to pass a check.

Housekeeping synchronizes only its five routing outputs. Only the character curation agent may supply the two character files as a coordinated pre-merge repair; it must review against the exact proposed evidence tree. Character invariants and the generated index remain strict even during author preflight. Reconcile current `main`, require completed housekeeping and any generated child commit's full audit, and integrate only the exact final head with a successful `Repository integration audit` status. Full integration, `main`, character curation, reconstruction evaluation, and cross-cutting audits never defer routing.

## Local or cross-cutting profile

1. Stage only the declared content, registry, policy, and tool paths by exact pathname.
2. Generate deterministic outputs from that index:

   `python tools/prepare_commit.py --base origin/main --write-generated`

3. Review and stage only the generated files reported by the command.
4. Run the final gate once the worktree and index agree:

   `python tools/prepare_commit.py --base origin/main --check`

The default check is diff-aware. It evaluates the obligation map against the exact base and staged Git path sets, registered-root topology, generated catalogs, staged whitespace, focused integration tests, and character output when affected. It does not reread every unchanged corpus blob or run the complete unit suite.

Use `python tools/prepare_commit.py --base origin/main --check --full` when explicitly requested or when changing executable validation, workflow, schema, publication-safety, or authority controls. Routine analysis and documentation commits use the default targeted gate. Do not commit or push on any applicable failure.

The full gate uses the timed regression runner described in [Audit execution rollout](AUDIT_EXECUTION.md). Every discovered test remains mandatory. Shadow selection reports are advisory and cannot enable reduced execution or certify a commit.

## Before and after publication

1. Inspect the exact staged path list, diff, generated changes, and file sizes.
2. Confirm the commit uses an approved owner author identity and an approved committer identity.
3. Reread the main ruleset `25199066`, activation-tag ruleset `21946617`, and both remote heads. Verify their live semantics under `PUBLICATION_AND_CONTRIBUTION_POLICY.md` using ruleset details. Stop if any is absent or unverifiable. Collaborators, invitations and deploy keys are checked before integration by the nightly controller and by automated character discovery under [its bounded API access-check contract](PUBLICATION_AND_CONTRIBUTION_POLICY.md#automated-character-discovery-access-checks); every access surface is checked by the owner merging by hand (`PUBLICATION_AND_CONTRIBUTION_POLICY.md`).
4. Push normally without force. The primary EC2 steward and owner-invoked manual nightly fallback follow their shared invariants and exclusive execution contract in `NIGHTLY_ANALYTICAL_INTEGRATION.md`; the fallback retains clean-only reconciliation, protected PR integration and explicit post-merge validation. For a stable analytical branch, require the final housekeeping result and its generated-commit audit when an automated child commit was produced. For other branches and `main`, require the full repository audit and successful `Repository integration audit` status for the exact remote commit. A passing author preflight with pending routing is not a passing integration gate.
5. After integration, apply the verified branch-retention or pruning rule in `BRANCH_LIFECYCLE.md`.

### Stable analytical publication sequence

Apply this sequence to every author push on a continuing series/study branch, including connector/API publication. Publishing several commits together is one publication; a new push starts a new validation sequence.

1. **Serialize publication on the source branch.** Complete the preceding source audit, housekeeping, and final exact-head audit before publishing the next analytical tranche. Analysis preparation may continue separately while checks run. A diagnosed correction or explicitly coordinated superseding push may proceed before that sequence succeeds, but it must preserve intervening work and start a fresh validation sequence; an older run cannot certify its new head. A failed sequence blocks tranche closure and further integration until repaired.
2. **Refresh both histories.** Fetch current `origin/main` and the remote stable branch, or retrieve their exact current refs through the connector. Record both full SHAs. Incorporate intervening author commits, housekeeping children, and coordinated curation repairs into the candidate. If current `main` is not an ancestor, incorporate it through an ordinary merge. Preserve approved governance, routing, and character content arriving from `main`; importing it does not grant routine authorship of those files. Re-read governing instructions when controls change.
3. **Validate the reconciled candidate.** Use the exact-path staging allowlist, applicable author preflight, approved identities, and complete diff review above. Reconciliation that changes the candidate requires the affected checks again. Resolve conflicts only through the verified procedure below and within the task's authorized scope.
4. **Recheck immediately before every push.** Retrieve both remote heads again. If either differs from the recorded SHA, preserve the new work, reconcile, review, and rerun affected checks before publishing. Push normally without force or history rewriting. After publication, read back the resulting commit, tree, and changed-file set. If housekeeping or another writer has already advanced the branch, identify and preserve that descendant; do not overwrite it or claim that the earlier commit certifies the new head. Inspect ambiguous push results before retrying.
5. **Follow the complete validation sequence.** Track the source audit, completed housekeeping, and the successful `Repository integration audit` on the final source or verified housekeeping child. Inspect the actual audited SHA and status target; a dispatch's displayed `main` metadata is insufficient. Pending, superseded, missing, skipped, cancelled, or failed results do not close the tranche. If housekeeping reports that current `main` must be incorporated, repeat synchronization and validation, then publish the correction; rerunning the unchanged stale commit cannot repair its ancestry.
6. **Refresh again after integration.** A squash merge preserves content without making the source commit an ancestor of `main`. Before the next publication, fetch and reconcile again. Concurrent updates to `main` can still require another synchronization after a successful pre-push check; treat the workflow's exact-head checks as governing.

### Squash-merge reconciliation

The nightly controller may perform only clean merges. Its conflict deferral requires an authorized author/repair task to inspect the evidence; it does not authorize automatic conflict resolution. The owner-operated CI and PR Integration Steward is an authorized repair task within its [standing delegation](NIGHTLY_ANALYTICAL_INTEGRATION.md#ci-and-pr-integration-steward), including publication of verified reconciliation commits on eligible source branches. It must follow the evidence procedure below, preserve specialized writer ownership, and refer substantive ambiguity to the owner. Its primary-coordinator role, independent deterministic executor, shared integration invariants and exclusion of concurrent manual-fallback merges are defined in that same policy; this checklist grants no separate controller authority.

1. Identify the previous merged PR for the same repository, stable branch, and `main` target. Record its exact source-head and integration SHAs. Verify the integration commit is an ancestor of current `main` and the prior source is an ancestor of the current source. A matching title, closed PR, timestamp, or similar-looking excerpt is insufficient.
2. Compare the complete repository trees of that prior source and integration result. If they are identical, record that content-preservation proof, then inspect every change on both sides since those snapshots. If they differ, review the complete integration patch and resolve the discrepancy before choosing any conflict resolution; do not assume the squash included every source byte.
3. Resolve only what the evidence supports. A conflicted file may retain the current source bytes when the current-main blob is proven unchanged from the verified integrated baseline; the inverse requires the corresponding source-side proof. If both sides changed, reconcile the actual edits while preserving history, identifiers, and unrelated content. Respect housekeeping and character ownership: import verified approved outputs or use their designated writer/generator within its authorization. Never select `ours`/`theirs` across a file or subtree without those comparisons. Report unresolved semantic or provenance conflicts instead of guessing.
4. Review the entire combined tree and record the preservation evidence. Use an ordinary merge commit that retains both histories, rerun applicable validation, recheck remote heads, push without force, and await the complete final audit. If the exact current source was already fully integrated, no new analytical integration is needed; retain the stable branch and reconcile it before its next publication.

Do not routinely modify `governance/AUTHORITY_SCOPE.json`, authority-epoch records, bootstrap bindings, public-activation bindings, or the frozen Drive-to-Git migration crosswalks.
