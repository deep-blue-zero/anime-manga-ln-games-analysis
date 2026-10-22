# Analytical integration

Pull requests reach `main` through one deterministic merge gate, `tools/nightly_integration.py`. Two callers use it:

- the **CI and PR Integration Steward** (the CI agent), a scheduled cloud agent of any provider, for open owner PRs;
- the owner, through the manual **Bulk merge analysis branches** workflow (`.github/workflows/nightly-integration.yml`), for every `series/<stable-slug>` and `studies/<stable-slug>` branch at once.

The gate enforces the mechanics below in code. This document states what the CI agent is for and what remains the owner's decision.

## CI and PR Integration Steward

The owner delegates routine integration to the CI agent. Each scheduled run it:

1. reviews every open, owner-authored, same-repository PR against `main`: the complete diff, its audit result and any CI failure evidence, including any routing `catalog_note` that records progress instead of describing the project;
2. reconciles a PR that is behind `main` by merging `main` into its branch, and fixes regressions in analysis, character data or code with ordinary commits on that branch;
3. merges only by running the gate from a fresh checkout of current `main`.

Candidates come from `series/`, `studies/`, `agent/` (and the older `codex/`, `chatgpt/` and `claude/`) branches and the `character-registry` and `character-reconstruction` branches. A branch name grants nothing: the gate checks each PR's paths. Character discovery and reconstruction PRs are ordinary candidates. The repository audit confines `character-registry` to its two files. The gate accepts reconstruction outputs only from `character-reconstruction`, which may change nothing else. Until the owner accepts reconstruction calibration (`publication_phase: ROUTINE`), the gate leaves every reconstruction PR for the owner.

### What waits for the owner

The gate refuses any PR that touches a guardrail path:

- `.github/`, the gate itself, this document and `AGENTS.md`;
- owner authorization records: `governance/repository-controls/` (publication grants, sealed-reading releases, the reconstruction phase gate, identities and tracked-file limits), and the archived migration records in `governance/archive/`;
- `crosswalk/`, `provenance/`, `LICENSE.md` and `THIRD_PARTY_NOTICES.md`.

The owner merges those personally, and that merge is what makes an authorization record count.

The CI agent also leaves a PR for the owner, by adding the `nightly-hold` label with a short comment, when it:

- removes or loosens a validation check, test or control value, or would need to in order to pass;
- changes source admission, rights or provenance boundaries;
- makes an interpretive or substantively ambiguous change that the evidence does not settle;
- is a substantive reconstruction PR (a new candidate, supersession or promotion) after calibration is accepted. Only the owner merges a promotion.

Never weaken a check or manufacture a green result. A failing PR is repaired or held, never merged.

### Holds

Draft status and the `nightly-hold` label are the only hold signals. A hold seen at any point in a run blocks that PR for the rest of the run. Only the owner releases a hold. The CI agent may add one but never removes one.

## Merge gate

For each candidate the gate:

- confirms the branch's owner-authored PR, approved commit identities and allowed paths (an analysis branch may change only its own root, the five housekeeping routing outputs and a separately identifiable two-file curation repair);
- waits for the trusted `Repository integration audit` to report success on the exact head (for an analysis branch whose routing outputs were stale, that is housekeeping's child commit);
- merges `main` into a stale branch only when Git merges cleanly, and otherwise leaves the conflict for the CI agent or author;
- merges through GitHub's protected PR endpoint with the exact audited head as a merge commit;
- checks that the merge commit's tree equals the audited head and waits for `main`'s own audit of it.

Before any write, an apply run confirms that the gate's bytes match current `main`, the token belongs to the owner, the `main` ruleset still blocks deletion and force-pushes and requires the strict audit, and `main`'s latest audit passed. It rechecks the ruleset immediately before each merge.

If `main` moves during a run, the remaining candidates wait for the next run. If `main`'s audit of a merge fails or does not finish, the change is integrated but unverified: the run stops, and every later run refuses to start until `main` is green again. Repair forward. Never revert, force-push or rewrite `main`.

## Running the CI agent

- Use one fine-grained owner token for this repository with Contents and Pull requests read/write, and Actions and Commit statuses read. Supply it as `OWNER_TOKEN`. Do not place it in files, PR text, logs or chat.
- Run `python tools/nightly_integration.py --mode apply --report <durable path>` from a fresh checkout of `main`. `--mode preview` makes no writes.
- Run one instance at a time per host. Concurrent writers are safe but waste effort, because GitHub's exact-head merge and strict up-to-date rule let only one succeed.

## Bulk merge workflow

The owner dispatches **Bulk merge analysis branches** on `main` with `preview` or `apply` and an optional single branch. It runs the same gate with `--candidates analysis-branches`, using the `NIGHTLY_INTEGRATION_TOKEN` secret. It opens a PR for an analysis branch that has none. The workflow token stays read-only, and the workflow runs only by manual owner dispatch.

The Actions step summary and run log hold each run's JSON receipt.
