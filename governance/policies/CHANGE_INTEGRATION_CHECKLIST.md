# Repository Pre-Commit Guidance

This is the mandatory pre-commit contract for human, Codex, and ChatGPT changes to this repository. It complements `AGENTS.md` and the authority records; it does not expand repository, Drive, publication, or contributor authority.

## Before editing

1. Read `AGENTS.md`, `governance/AUTHORITY_STATE.yaml`, `governance/AUTHORITY_SCOPE.json`, and this checklist.
2. Begin from an up-to-date branch based on `origin/main`. Follow `BRANCH_LIFECYCLE.md` for the branch name and eventual pruning.
3. Preserve the owner-only authorship policy, the Git/Drive authority boundary, artifact exclusions, and frozen migration records.
4. Declare the intended paths. Never use `git add .`, wildcard staging, force-push, or history rewriting.

## Branch routing and cleanup

- Continuing series analysis is written to `series/<stable-slug>` and periodically integrated into `main`.
- Continuing cross-series or non-series study work is written to `studies/<stable-slug>` and periodically integrated into `main`.
- Different series or study branches may advance concurrently. Work on the same analytical root must be serialized or explicitly reconciled before integration.
- Cross-cutting governance or tooling work uses a narrowly named temporary branch such as `codex/<purpose>` or `chatgpt/<purpose>`.
- Bootstrap, migration, repair, audit-remediation, experiment, and one-shot automation branches are temporary.
- A temporary branch must be pruned after its intended content is verified on `origin/main`, the exact integration is recoverable, the `main` repository audit is green, and no intended artifact remains unique to the branch.
- Use ancestry to verify merges and fast-forwards. For an approved squash or rebase, compare the complete tree or reviewed patch before deletion. Never bulk-delete branches merely because they are old or their pull requests are closed.
- Stable series and study branches may remain while actively used. Apply the same verified pruning rule when one is retired.

The full branch contract is `governance/policies/BRANCH_LIFECYCLE.md`.

## Change obligations

The machine-readable form of this table is `governance/repository-controls/change-obligations.json`.

| Change | Required synchronization |
| --- | --- |
| Any tracked add, delete, or rename | No global path-list projection. The final Git index/tree is the canonical live path inventory; evaluate the semantic obligations below. |
| Add, remove, or reroute a series root | Update `series/registry.json`; regenerate `series/README.md` and the series catalog in `governance/MANGA_ANIME_CORPUS_INDEX.md`. |
| Add, remove, or reroute a study root | Update `studies/registry.json`; regenerate `studies/README.md` and the studies catalog in `governance/MANGA_ANIME_CORPUS_INDEX.md`. |
| Add or change character discovery or qualifying evidence | Update `characters/registry.jsonl`, verify exact-byte evidence hashes and authority eligibility, and regenerate `CHARACTER_ANALYSIS_INDEX.md`. |
| Add or change a Drive-only reference | Update the Drive artifact reference index and verify every referenced anchor. Do not rewrite frozen migration crosswalks. |
| Change policy, schema, validation, workflow, or authority controls | Run the affected focused tests and review the governance effect. Use the explicit full gate for executable validation, workflow, schema, publication-safety, or authority changes. Authority-scope changes require separate owner authorization. |

Ordinary edits, additions, and deletions inside an existing registered analytical root do not require unrelated global registry or catalog churn solely because the path set changed. New or removed series/study roots and other semantic changes still activate the specific obligations above. `G3_BOOTSTRAP_TRACKED_PATHS.txt` remains immutable historical evidence; it is not the live inventory.

## Prepare the exact staged snapshot

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
3. Push normally without force. The read-only GitHub workflow is the single full post-publication repository audit; confirm that the exact remote commit passes it before treating the change as complete.
4. After integration, apply the verified branch-retention or pruning rule in `BRANCH_LIFECYCLE.md`.

Do not routinely modify `governance/AUTHORITY_SCOPE.json`, authority-epoch records, bootstrap bindings, public-activation bindings, or the frozen Drive-to-Git migration crosswalks.
