# Branch lifecycle

This repository uses named integration branches to isolate concurrent analytical work while keeping temporary branches from accumulating indefinitely. Branch names do not grant authorship, merge, or upstream write authority; the owner-only contribution policy remains controlling.

## Continuing analytical branches

- Continuing series work uses `series/<stable-slug>`.
- Continuing cross-series or non-series study work uses `studies/<stable-slug>`.
- Each branch carries work only for its named analytical root plus the global registries, generated indexes, manifests, and governance surfaces that the change-integration contract requires.
- Different series or study branches may advance concurrently. Changes to the same analytical root must be serialized or explicitly reconciled before integration.
- Before each integration cycle, incorporate the current `origin/main`, run the complete staged-snapshot gate, and merge through the repository's owner-controlled process. Periodic integration is preferred over an indefinitely divergent branch.

These branches may remain while their named corpus is actively receiving work. If a series or study branch is retired, apply the same verification and pruning procedure used for temporary branches.

## Temporary branches

Bootstrap, migration, repair, audit-remediation, experiment, and one-shot automation branches are disposable. A temporary branch has accomplished its purpose only after:

1. its intended changes are present on `origin/main`;
2. its exact tip and integration result have been recorded or are recoverable from the merged pull request;
3. `origin/main` passes the repository audit; and
4. no unique intended commit or artifact remains only on the temporary branch.

Verify preservation by content and history. For a merge or fast-forward, require the temporary tip to be an ancestor of `origin/main`. For an approved squash or rebased integration, compare the complete tree or reviewed patch because ancestry alone will not prove preservation.

After those checks, delete the remote temporary branch and then its local counterpart. Never bulk-delete branches based only on age, naming, or a closed pull request, and never delete an unmerged or unverified tip.

## Cross-cutting work

Repository-wide governance, tooling, or index changes use a narrowly named temporary branch such as `codex/<purpose>` or `chatgpt/<purpose>`. It must be pruned after verified integration. Do not route unrelated analytical content through a cross-cutting branch merely to avoid its series or study integration branch.
