# Branch lifecycle

Named branches isolate concurrent work and keep temporary branches from accumulating. A branch name grants no authorship, merge or upstream write authority.

## Continuing analytical branches

- Series work uses `series/<stable-slug>`; cross-series and non-series study work uses `studies/<stable-slug>`.
- Each branch carries work only for its named analytical root and optional `.repository/` routing inputs, plus any housekeeping child commit over the five routing outputs and any separately identifiable character repair that touches only discovery outputs. The repository audit enforces that scope.
- Different series or study branches may advance concurrently; changes to the same root must be serialized or reconciled before integration.
- Merge current `main` into the branch before each tranche. The CI agent integrates the branch's PR as a merge commit under `NIGHTLY_ANALYTICAL_INTEGRATION.md`; integrate periodically rather than letting a branch diverge indefinitely.

These branches remain while their corpus is active. A retired series or study branch is pruned like a temporary branch.

A repository ruleset blocks deleting or force-pushing every `series/` and `studies/` branch, `character-registry`, `character-reconstruction`, `agent/tooling` and `agent/governance`, with no bypass. Retiring one of them is an owner step: lift the rule, prune the branch, restore the rule.

## Continuing character curation

The discovery agent uses the reusable `character-registry` branch with at most one open PR; the repository audit rejects any path outside the discovery outputs: the registry partitions under `characters/registry/`, `CHARACTER_ANALYSIS_INDEX.md` and the namespace pages under `characters/index/`. Keep it while the agent is active, recreate it from current `main` if it is deleted after a verified integration, and update it without force. See `CHARACTER_DISCOVERY_MAINTENANCE.md`.

## Continuing reconstruction evaluation

The reconstruction evaluator uses the reusable `character-reconstruction` branch with at most one open PR; it may change only `characters/reconstruction_capabilities.jsonl` and `characters/CHARACTER_RECONSTRUCTION_INDEX.md`, and series or study branches never carry those files. The same retention rules apply. See `CHARACTER_RECONSTRUCTION_MAINTENANCE.md`.

## Continuing maintenance branches

Repository maintenance uses two continuing branches, open to any agent or the owner:

- `agent/tooling` for automation and tooling: `tools/`, the merge gate, workflows, schemas and validation;
- `agent/governance` for policy, governance and analytical frameworks: `AGENTS.md` and `governance/`, including routing, policies, analytical methods and source policies.

Choose the branch by what drives the change, not by which files it touches: a tooling change and the policy text that describes it land together on `agent/tooling`, and a policy decision with a small code change lands on `agent/governance`. Each branch has at most one open PR; merge current `main` into it before each change, keep each PR to one purpose, and update it without force. Its PR merges as a merge commit, so the branch is never pruned. An open PR that touches a guardrail path waits for the owner, and other work on that branch queues behind it.

## Temporary branches

Use a narrowly named `agent/<purpose>` branch only when work cannot wait for its maintenance branch's open PR, or for an experiment or one-shot task. The `codex/`, `chatgpt/` and `claude/` prefixes that tools create by default are also audited. A branch under any other prefix gets no repository audit and so can never carry the required status. Do not route unrelated analytical content through a temporary branch to avoid its series or study branch.

A temporary branch is finished only when:

1. its intended changes are on `origin/main`;
2. its exact tip and integration result are recorded or recoverable from the merged PR;
3. `origin/main` passes the repository audit; and
4. no unique intended commit or artifact remains only on the branch.

Verify preservation by history and content. With a merge commit or fast-forward, the branch tip is an ancestor of `origin/main`. For a branch integrated by squash or rebase, compare the complete tree or reviewed patch, because ancestry alone will not prove preservation.

Then delete the remote branch and its local counterpart. Never bulk-delete branches by age, name or a closed PR alone, and never delete an unmerged or unverified tip.
