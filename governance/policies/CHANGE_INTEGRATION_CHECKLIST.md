# Repository Pre-Commit Guidance

This is the mandatory pre-commit contract for human, Codex, and ChatGPT changes to this repository. It complements `AGENTS.md` and the authority records; it does not expand repository, Drive, publication, or contributor authority.

## Before editing

1. Read `AGENTS.md`, `governance/AUTHORITY_STATE.yaml`, `governance/AUTHORITY_SCOPE.json`, and this checklist.
2. Begin from an up-to-date branch based on `origin/main`. Follow `BRANCH_LIFECYCLE.md` for the branch name and eventual pruning.
3. Preserve the owner-only authorship policy, the Git/Drive authority boundary, artifact exclusions, and frozen migration records.
4. Declare the intended paths. Never use `git add .`, wildcard staging, force-push, or history rewriting.

For a stable series/study branch, read `AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md`. Author the named analytical root and required series/study routing descriptors; housekeeping owns five routing outputs. Character discovery belongs solely to the curation agent under `CHARACTER_DISCOVERY_MAINTENANCE.md`. It may supply a coordinated pre-merge repair on a source branch, but housekeeping may not write either character output.

## Maintained documents: targeted edits

This rule applies to maintained analytical prose, rolling ledgers, readiness tables, project-local indexes, and other authored documents in both clone and GitHub connector workflows. Update the verified current document through targeted patches by default. Whole-document rewriting follows only the regeneration exceptions below. A filename containing "index" or "ledger" does not make the file a generated artifact.

1. **Establish the exact source.** Verify the intended repository, target branch, path, full base commit, and current blob identity. Obtain the complete current file through a verified read before submitting a full-file replacement. Search excerpts, previews, truncated responses, and selected line ranges are not a complete source. Preserve a trustworthy before-image in the authorized execution environment for comparison.
2. **Define the intended changes.** Identify the affected sections, rows, fields, headings, and cross-references. Apply explicit patches or bounded replacements with verified old text and expected match counts. If the target text is missing or ambiguous, re-read and resolve the discrepancy; do not silently broaden the replacement.
3. **Preserve unaffected content.** Keep unaffected prose, front matter, stable row/record IDs, table columns, ordering, headings, anchors, links, historical entries, encoding, and line endings byte-for-byte. Do not reflow paragraphs, normalize whitespace/Unicode, reorder tables, remove apparently redundant history, or rewrite unrelated sections as incidental cleanup. Apply any expressly required format migration as a separately identified transformation.
4. **Respect ledger semantics.** Append new events or observations where the ledger's history model requires it. Update existing current-state rows when evidence changes their meaning, preserving required historical records and explaining material corrections. Follow stricter append-only or frozen-artifact rules. Targeted editing must still update every affected claim and reference; it is not permission to omit necessary synchronization.
5. **Use the documented regeneration exceptions.** Explicitly generated artifacts must use their designated generator. A document-wide revision is permitted when the owner expressly requests it or an applicable reviewed transformation defines it; review its full scope and preserve required provenance. Neither file size nor a connector failure authorizes reconstruction from memory, summaries, or excerpts.
6. **Review the complete candidate diff.** Confirm every addition and deletion is intended, with no missing sections, rows, citations, authority fields, or history. Inspect unexpected size or line-count changes and formatting churn. Counts alone do not establish preservation, and an abbreviated provider diff is not sufficient if it omits changes. Require the applicable schema, link, evidence, and repository checks.
7. **Handle concurrency and verify publication.** Recheck the target head and blob before writing. If the source changed, retrieve the new version, reconcile and reapply the intended edits, and repeat affected review. After a write, retrieve the exact resulting commit's file and compare it with the reviewed candidate; verify the resulting changed-file set. A success message alone does not establish a correct edit.

### GitHub connector limits and failed writes

A GitHub contents or tree API may require the full updated file as its payload. That transport is allowed, but construct the payload from complete verified source contents plus targeted edits, not by generating an approximate replacement. Use current blob SHAs for contents updates and exact base/parent commits with non-forced ref updates for Git-data operations. A blob SHA alone does not prove that the branch has not advanced.

If a read is truncated or a payload cannot be handled reliably, obtain a verified complete read or move the edit to an approved Git-capable environment within the user's access constraints. Do not switch to the owner's local drive when the task is cloud-only. If no available route can preserve the file, report the exact blocker and proposed patch without replacing the document. Continue independent authorized work where possible.

After a timeout, ambiguous response, or failed multi-file operation, inspect the remote branch, commit, and affected blobs before retrying. Determine whether no write, the complete intended write, or a partial/divergent result occurred. Retry only the missing operation against the verified current state; do not replay stale full-file contents or duplicate appended entries. Preserve concurrent work and repair through ordinary commits. When multiple files must remain consistent, prefer an atomic tree/commit and validate the entire resulting change.

These are authoring and verification requirements. Existing syntax and repository checks cannot by themselves prove that a regenerated document retained its analytical meaning.

## Branch routing and cleanup

- Continuing series analysis is written to `series/<stable-slug>` and periodically integrated into `main`.
- Continuing cross-series or non-series study work is written to `studies/<stable-slug>` and periodically integrated into `main`.
- Different series or study branches may advance concurrently. Work on the same analytical root must be serialized or explicitly reconciled before integration.
- Cross-cutting governance or tooling work uses a narrowly named temporary branch such as `codex/<purpose>` or `chatgpt/<purpose>`.
- Bootstrap, migration, repair, audit-remediation, experiment, and one-shot automation branches are temporary.
- A temporary branch must be pruned after its intended content is verified on `origin/main`, the exact integration is recoverable, the `main` repository audit is green, and no intended artifact remains unique to the branch.
- Use ancestry to verify merges and fast-forwards. For an approved squash or rebase, compare the complete tree or reviewed patch before deletion. Never bulk-delete branches merely because they are old or their pull requests are closed.
- The reusable `character-registry` branch may remain while the recurring curation task is active; follow `CHARACTER_DISCOVERY_MAINTENANCE.md` for its two-file boundary and exact-head integration checks.
- Stable series and study branches may remain while actively used. Apply the same verified pruning rule when one is retired.

The full branch contract is `governance/policies/BRANCH_LIFECYCLE.md`.

## Change obligations

The machine-readable form of this table is `governance/repository-controls/change-obligations.json`.

| Change | Required synchronization |
| --- | --- |
| Any tracked add, delete, or rename | No global path-list projection. The final Git index/tree is the canonical live path inventory; evaluate the semantic obligations below. |
| Add, remove, or reroute a series root | On a stable series branch, provide `.repository/series-registry.json`; automation updates `series/registry.json`, `series/README.md`, and the corpus index. Elsewhere, update those outputs in the same reviewed change. Automatic removal is prohibited. |
| Add, remove, or reroute a study root | On a stable study branch, provide `.repository/study-registry.json`; automation updates `studies/registry.json`, `studies/README.md`, and the corpus index. Elsewhere, update those outputs in the same reviewed change. Automatic removal is prohibited. |
| Add new eligible character analysis | Daily curation may enroll it after merge if existing character references and generated output remain valid. Character-upsert inputs are no longer required or applied. |
| Change the character registry or already referenced evidence | The curation agent reviews affected records and regenerates `CHARACTER_ANALYSIS_INDEX.md`; evidence changes that invalidate existing discovery require its coordinated repair before source integration. |
| Add or change a Drive-only reference | Update the Drive artifact reference index and verify every referenced anchor. Do not rewrite frozen migration crosswalks. |
| Change policy, schema, validation, workflow, or authority controls | Run the affected focused tests and review the governance effect. Use the explicit full gate for executable validation, workflow, schema, publication-safety, or authority changes. Authority-scope changes require separate owner authorization. |

Ordinary edits, additions, and deletions inside an existing registered analytical root do not require unrelated global registry or catalog churn solely because the path set changed. New or removed series/study roots and other semantic changes still activate the specific obligations above. `G3_BOOTSTRAP_TRACKED_PATHS.txt` remains immutable historical evidence; it is not the live inventory.

## Stable analytical branch profile

Stage only the declared analytical files and any required named routing descriptor. In an authorized Git execution environment, run author preflight against the staged index:

`python tools/validate_repository.py --phase current --snapshot index --routing-preflight series/<stable-slug> --repo .`

Use the matching `studies/<stable-slug>` argument for a study. This command validates a read-only projection of the five routing outputs; it does not stage or write them. Review the exact staged diff, approved identities, and applicable whitespace checks before publishing normally. A GitHub connector task follows the complete-read, atomic-commit, non-forced update, and remote-readback rules above and requires the exact published commit's CI preflight.

`AWAITING_SYNCHRONIZATION` permits publishing authored content to the stable branch while routing remains pending. It does not permit integration. A real new root requires its routing descriptor and a current-eligible entrypoint with complete authority metadata. Branch creation without a named root requires neither. For a noncurrent working draft, use the `draft_noncurrent` template in `../../characters/README.md`; do not promote it to current authority merely to pass a check.

Housekeeping synchronizes only its five routing outputs. Only the character curation agent may supply the two character files as a coordinated pre-merge repair; it must review against the exact proposed evidence tree. Character invariants and the generated index remain strict even during author preflight. Reconcile current `main`, require completed housekeeping and any generated child commit's full audit, and integrate only the exact final head with a successful `Repository integration audit` status. Full integration, `main`, character curation, and cross-cutting audits never defer routing.

## Local or cross-cutting profile

1. Stage only the declared content, registry, policy, and tool paths by exact pathname.
2. Generate deterministic outputs from that index:

   `python tools/prepare_commit.py --base origin/main --write-generated`

3. Review and stage only the generated files reported by the command.
4. Run the final gate once the worktree and index agree:

   `python tools/prepare_commit.py --base origin/main --check`

The default check is diff-aware. It evaluates the obligation map against the exact base and staged Git path sets, registered-root topology, generated catalogs, staged whitespace, focused integration tests, and character output when affected. It does not reread every unchanged corpus blob or run the complete unit suite.

Use `python tools/prepare_commit.py --base origin/main --check --full` when explicitly requested or when changing executable validation, workflow, schema, publication-safety, or authority controls. Routine analysis and documentation commits use the default targeted gate. Do not commit or push on any applicable failure.

## Before and after publication

1. Inspect the exact staged path list, diff, generated changes, and file sizes.
2. Confirm the commit uses an approved owner author identity and an approved committer identity.
3. Push normally without force. The owner-authorized nightly controller follows `NIGHTLY_ANALYTICAL_INTEGRATION.md` for clean reconciliation, protected PR integration, and explicit post-merge validation. For a stable analytical branch, require the final housekeeping result and its generated-commit audit when an automated child commit was produced. For other branches and `main`, require the full repository audit and successful `Repository integration audit` status for the exact remote commit. A passing author preflight with pending routing is not a passing integration gate.
4. After integration, apply the verified branch-retention or pruning rule in `BRANCH_LIFECYCLE.md`.

Do not routinely modify `governance/AUTHORITY_SCOPE.json`, authority-epoch records, bootstrap bindings, public-activation bindings, or the frozen Drive-to-Git migration crosswalks.
