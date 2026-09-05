# Repository Pre-Commit Guidance

This is the mandatory pre-commit contract for human, Codex, and ChatGPT changes to this repository. It complements `AGENTS.md` and the authority records; it does not expand repository, Drive, publication, or contributor authority.

## Before editing

1. Read `AGENTS.md`, `governance/AUTHORITY_STATE.yaml`, `governance/AUTHORITY_SCOPE.json`, and this checklist.
2. Begin from an up-to-date branch based on `origin/main`. Follow `BRANCH_LIFECYCLE.md` for the branch name and eventual pruning.
3. Preserve the owner-only authorship policy, the Git/Drive authority boundary, artifact exclusions, and frozen migration records.
4. Declare the intended paths. Never use `git add .`, wildcard staging, force-push, or history rewriting.

For a stable series/study branch, read `AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md`. Author the named analytical root and required series/study routing descriptors; housekeeping owns five routing outputs. Character discovery belongs solely to the curation agent under `CHARACTER_DISCOVERY_MAINTENANCE.md`. It may supply a coordinated pre-merge repair on a source branch, but housekeeping may not write either character output.

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

Push the owner-authored analysis and routing descriptors to the matching stable branch. Housekeeping synchronizes only its five routing outputs. Only the character curation agent may supply the two character files as a coordinated pre-merge repair; it must review against the exact proposed evidence tree. The read-only audit continues validating all character invariants and the generated index. Require any housekeeping child commit and its exact-commit audit, and integrate only the final green branch head.

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
3. Push normally without force. For a stable analytical branch, require the final housekeeping result and its generated-commit audit when an automated child commit was produced. For other branches and `main`, require the read-only repository audit for the exact remote commit.
4. After integration, apply the verified branch-retention or pruning rule in `BRANCH_LIFECYCLE.md`.

Do not routinely modify `governance/AUTHORITY_SCOPE.json`, authority-epoch records, bootstrap bindings, public-activation bindings, or the frozen Drive-to-Git migration crosswalks.
