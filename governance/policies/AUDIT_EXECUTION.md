# Audit execution rollout

The first execution-refinement release retains the complete repository audit and every discovered regression test. It introduces batched raw Git reads, timing reports, an explicit test catalog, and an advisory selection plan. Neither a passing plan nor a timing report certifies a commit.

## Active behavior

`tools/validate_repository.py` continues to validate the complete selected snapshot. Its optional `--timings-json` output records stage durations and shared-reader Git operations in a file outside the repository. Generated repository catalogs are checked against that same snapshot; standalone generator CLIs retain their own checks and regression coverage.

`tools/audit_execution.py` discovers and runs the entire unittest suite. `--profile full` executes it with timings. `--profile shadow` additionally describes a possible future content selection, but executes the identical full suite. Scheduled audits use full; manual audits default to full; pushes and generated-commit dispatches use shadow. `prepare_commit.py --check --full` uses the same complete runner and executes the repository-index tests once rather than twice.

The three approved workflows, their privileges, the isolated status reporter, source-preflight pending state, five-file housekeeping boundary, final source certification, and mandatory fresh owner-dispatched post-merge audit remain unchanged. Housekeeping still requires its existing full staged gate. This release does not change merge eligibility.

## Selection remains disabled

`../repository-controls/test-execution-policy.json` requires `selection_enabled: false`. The runner also enforces that condition in code. There is no content execution command or environment bypass in this release; changing the flag alone fails validation.

`../../tools/tests/test-catalog.json` assigns every existing test an explicit responsibility, input description, and smoke designation. Tests inspecting real corpus state remain in the always-required group; mixed classes are conservatively retained there. The reconstruction production-absence assertion is a live-corpus guard, separate from its dormant synthetic assessment scenarios. The remaining assertion-level separation and dependency review are not claimed complete.

The shadow classifier compares complete Git deltas with rename detection disabled. Unknown paths, changed controls, missing/unusable baselines, unregistered roots, incompatible runtimes, or uncatalogued tests propose full execution. Ordinary registered data and routing changes may propose content execution. Every proposed exclusion is reported, and actual execution remains full.

Baseline ancestry and object availability are checked for planning, but successful baseline certification is not authenticated by this initial planner. Reports explicitly declare `advisory_only: true` and `baseline_authenticated: false`. A dispatch uses its actual selected commit, never its workflow-context main SHA, for snapshot validation. A comparison with a newer main can conservatively produce a full proposal. This is not the trusted selection mechanism needed for activation.

Uncatalogued discovered tests still run and force a full proposal. Stale IDs, duplicate discovery/catalog ownership, absent mandatory groups, import failures, or incomplete execution block success. The test catalog is maintained explicitly with new tests; no routine workflow rewrites it.

## Telemetry and interpretation

Reports are written outside the repository, summarized in the Actions step summary, and emitted as JSON in the run log. They record stage/test durations, runtime/dependency versions, exact selection inputs, catalog decisions, executed counts, skips, failures, and shared-reader process/blob counts. Shared-reader counters are scoped to the current process; they do not pretend to include child CLI processes or fixture setup Git commands. A test's duration includes its own setup/teardown; class setup is included in total regression duration.

Snapshot acquisition uses one `git cat-file --batch` process after metadata enumeration. Responses are checked for exact object identity, blob type, declared byte boundaries, content hash, and successful process exit. Identical blob requests are deduplicated within an acquisition. Index snapshots are reread on each acquisition and reject a changed index. No persistent success cache or cross-run object cache is introduced.

A local Windows comparison at main commit `72014aaf9446b3260acbd4dfc1a6c927ced57a35` covered 3,440 paths and found identical path order, modes, tracked flags, and SHA-256 content digests between old and new readers. One old-reader measurement took 224.327 seconds; one batched-reader measurement took 2.062 seconds and four Git processes. These are snapshot-only observations on one machine, not CI latency estimates or statistical performance guarantees.

## Remaining rollout gates

Before reduced execution is implemented and activated, complete the assertion/dependency review, authenticated successful-baseline handling, curated failure-mutation comparisons, at least seven days and twenty representative shadow audits, and all required stabilization full audits. Coordinate any changes to reporter outputs, nightly baseline dispatch fields, and workflow contracts as reviewed changes. Source/final/post-merge roles must retain their independent certification requirements.

Until then all coverage remains active. Rollback of the planner consists of selecting the full profile; rollback of reader behavior requires an ordinary reviewed code change. Timing thresholds are performance targets and do not cause correctness failures merely because a hosted runner is slow.
