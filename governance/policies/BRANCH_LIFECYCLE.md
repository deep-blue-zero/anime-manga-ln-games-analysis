# Branch lifecycle

This repository uses named integration branches to isolate concurrent analytical work while keeping temporary branches from accumulating indefinitely. Branch names do not grant authorship, merge, or upstream write authority; the owner-only contribution policy remains controlling.

## Continuing analytical branches

- Continuing series work uses `series/<stable-slug>`.
- Continuing cross-series or non-series study work uses `studies/<stable-slug>`.
- Each branch carries owner/agent-authored work only for its named analytical root and optional `.repository/` declarative inputs. The bounded housekeeping workflow may append a child commit containing only its five exact series/study routing outputs. A coordinated pre-merge repair may include a separately identifiable character-agent commit over the two character outputs; housekeeping treats those files as read-only.
- Different series or study branches may advance concurrently. Changes to the same analytical root must be serialized or explicitly reconciled before integration.
- Before each integration cycle, incorporate the current `origin/main`. Require a successful `Repository integration audit` status on the exact final head; when routing outputs were stale, that is the housekeeping child commit and its dispatched full audit. A pending status is not integration approval. Merge through the merge gate in `NIGHTLY_ANALYTICAL_INTEGRATION.md`, run by the CI agent or the owner's bulk-merge workflow. It may incorporate current main through a clean merge without rewriting source history, creates or reuses owner-authored PRs, integrates them as merge commits, and verifies `main`'s audit after each merge. Periodic integration is preferred over an indefinitely divergent branch.

These branches may remain while their named corpus is actively receiving work. If a series or study branch is retired, apply the same verification and pruning procedure used for temporary branches.

## Continuing character curation

The sole character curation agent uses the exact reusable `character-registry` branch for recurring two-file discovery updates and at most one open PR to `main`. This is an explicit continuing-branch exception to the temporary cross-cutting convention. Retain it while active; recreate it from current `main` after any verified automatic deletion. Reconcile without force-pushing or rewriting history.

Follow `CHARACTER_DISCOVERY_MAINTENANCE.md` for semantic review, exact-head audits, protected automatic integration, and cloud checkpoints. Ordinary curation PRs contain only `characters/registry.jsonl` and `CHARACTER_ANALYSIS_INDEX.md`; every audit of unmerged `character-registry` history, however started, rejects any other path changed against `main`. Pre-merge evidence repairs are agent-authored on the exact source branch and integrated by the owner/source task as a combined validated change; this does not grant the daily agent authority to merge analysis.

## Continuing reconstruction evaluation

The sole reconstruction evaluator uses the exact reusable `character-reconstruction` branch for recurring two-file capability updates and at most one open PR to `main`. Like `character-registry`, this is an explicit continuing-branch exception to the temporary cross-cutting convention: retain it while active, recreate it from current `main` after any verified automatic deletion, and reconcile without force-pushing or rewriting history.

Follow `CHARACTER_RECONSTRUCTION_MAINTENANCE.md` for review, exact-head audits, owner merge of substantive changes, and its bounded mechanical-maintenance merge authority. Its PRs contain only `characters/reconstruction_capabilities.jsonl` and `characters/CHARACTER_RECONSTRUCTION_INDEX.md`; the validator rejects any other path changed beside them. Series and study branches never carry these files: a source change that makes an assessment stale is reconciled later by the evaluator, not repaired on the source branch.

## Temporary branches

Bootstrap, migration, repair, audit-remediation, experiment, and one-shot automation branches are disposable. A temporary branch has accomplished its purpose only after:

1. its intended changes are present on `origin/main`;
2. its exact tip and integration result have been recorded or are recoverable from the merged pull request;
3. `origin/main` passes the repository audit; and
4. no unique intended commit or artifact remains only on the temporary branch.

Verify preservation by content and history. For a merge or fast-forward, require the temporary tip to be an ancestor of `origin/main`. For an approved squash or rebased integration, compare the complete tree or reviewed patch because ancestry alone will not prove preservation.

After those checks, delete the remote temporary branch and then its local counterpart. Never bulk-delete branches based only on age, naming, or a closed pull request, and never delete an unmerged or unverified tip.

## Steward maintenance across branch categories

The [CI and PR Integration Steward delegation](NIGHTLY_ANALYTICAL_INTEGRATION.md#ci-and-pr-integration-steward) covers routine technical maintenance and integration of owner-authored PRs: continuing `series/<stable-slug>` and `studies/<stable-slug>` branches, temporary `agent/<purpose>` branches (or the older `codex/`, `chatgpt/` and `claude/` prefixes), and the `character-registry` and `character-reconstruction` PRs. Branch form alone grants no eligibility: the merge gate confines analysis branches to their own root and leaves guardrail paths, and reconstruction PRs before calibration is accepted, to the owner. Character curation and reconstruction evaluation remain the writers of their outputs; the CI agent integrates their PRs without regenerating those files. Source synchronization preserves intervening commits through ordinary merges. All exact-head validation, explicit holds, protected integration, post-merge verification and retention/pruning rules remain applicable.

## Cross-cutting work

Except for the continuing character curation and reconstruction branches above, repository-wide governance, tooling, or index changes use a narrowly named temporary `agent/<purpose>` branch (the older `codex/`, `chatgpt/` and `claude/` prefixes are also audited). A branch under any other prefix receives no repository audit and so can never carry the required status. It must be pruned after verified integration. Do not route unrelated analytical content through a cross-cutting branch merely to avoid its series or study integration branch.
