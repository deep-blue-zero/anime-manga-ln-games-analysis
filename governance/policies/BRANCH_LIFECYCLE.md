# Branch lifecycle

This repository uses named integration branches to isolate concurrent analytical work while keeping temporary branches from accumulating indefinitely. Branch names do not grant authorship, merge, or upstream write authority; the owner-only contribution policy remains controlling.

## Continuing analytical branches

- Continuing series work uses `series/<stable-slug>`.
- Continuing cross-series or non-series study work uses `studies/<stable-slug>`.
- Each branch carries owner/agent-authored work only for its named analytical root and optional `.repository/` declarative inputs. The bounded housekeeping workflow may append a child commit containing only its five exact series/study routing outputs. A coordinated pre-merge repair may include a separately identifiable character-agent commit over the two character outputs; housekeeping treats those files as read-only.
- Different series or study branches may advance concurrently. Changes to the same analytical root must be serialized or explicitly reconciled before integration.
- Before each integration cycle, incorporate the current `origin/main`. Require completed housekeeping and a successful `Repository integration audit` status on the exact final head; when generated surfaces changed, that is the housekeeping child commit plus its dispatched full audit. A passing author preflight with pending synchronization, or a superseded housekeeping no-op, is not integration approval. Merge through the repository's owner-controlled process. Periodic integration is preferred over an indefinitely divergent branch.

These branches may remain while their named corpus is actively receiving work. If a series or study branch is retired, apply the same verification and pruning procedure used for temporary branches.

## Continuing character curation

The sole character curation agent uses the exact reusable `character-registry` branch for recurring two-file discovery updates and at most one open PR to `main`. This is an explicit continuing-branch exception to the temporary cross-cutting convention. Retain it while active; recreate it from current `main` after any verified automatic deletion. Reconcile without force-pushing or rewriting history.

Follow `CHARACTER_DISCOVERY_MAINTENANCE.md` for semantic review, exact-head audits, protected automatic integration, and cloud checkpoints. Ordinary curation PRs contain only `characters/registry.jsonl` and `CHARACTER_ANALYSIS_INDEX.md`. Pre-merge evidence repairs are agent-authored on the exact source branch and integrated by the owner/source task as a combined validated change; this does not grant the daily agent authority to merge analysis.

## Temporary branches

Bootstrap, migration, repair, audit-remediation, experiment, and one-shot automation branches are disposable. A temporary branch has accomplished its purpose only after:

1. its intended changes are present on `origin/main`;
2. its exact tip and integration result have been recorded or are recoverable from the merged pull request;
3. `origin/main` passes the repository audit; and
4. no unique intended commit or artifact remains only on the temporary branch.

Verify preservation by content and history. For a merge or fast-forward, require the temporary tip to be an ancestor of `origin/main`. For an approved squash or rebased integration, compare the complete tree or reviewed patch because ancestry alone will not prove preservation.

After those checks, delete the remote temporary branch and then its local counterpart. Never bulk-delete branches based only on age, naming, or a closed pull request, and never delete an unmerged or unverified tip.

## Cross-cutting work

Except for the continuing character curation branch above, repository-wide governance, tooling, or index changes use a narrowly named temporary branch such as `codex/<purpose>` or `chatgpt/<purpose>`. It must be pruned after verified integration. Do not route unrelated analytical content through a cross-cutting branch merely to avoid its series or study integration branch.
