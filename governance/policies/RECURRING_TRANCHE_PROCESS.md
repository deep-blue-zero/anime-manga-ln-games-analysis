# Recurring tranche process

This policy reduces approval repetition without reducing migration, publication, or authority controls. Each coherent migration tranche uses one owner-approved, SHA-256-bound package for its complete bounded lifecycle. Intermediate hashes and receipts are evidence, not additional approval gates.

## Single approval package

The package must freeze:

- a unique tranche ID and the SHA-256 of the approval package;
- the immutable source snapshot, source IDs or revisions, and SHA-256 hashes of exact source or exported bytes;
- an exhaustive per-artifact disposition: `MIGRATE`, `REFERENCE_DRIVE`, `VERIFIED_EXCLUDED`, or a named exception satisfying `ARTIFACT_ELIGIBILITY.md`;
- rights, privacy, size, binary, and publication-safety review;
- the complete source-to-destination crosswalk, declared transformations, exact writable and staged path allowlist, and any permitted mechanical corrective envelope;
- the base commit, expected `origin/main` object ID, target ref, sole-owner commit identity, commit message, and exact normal non-forced push refspec;
- the worktree, index, candidate-tree, commit, complete reachable-history, clean-clone, and CI validation contract; and
- the epoch-1 authority boundary, stabilization controls, and all separately governed operations that remain prohibited.

Final blob, tree, commit, remote, workflow-run, and receipt hashes are recorded after execution because they do not yet exist when the package is approved. Recording them does not create a new approval gate.

## Authorized lifecycle

If every frozen precondition remains true, the single approval authorizes this sequence without intermediate owner approvals:

1. Reverify the immutable source selection and its hashes, then materialize and transform only within the contained migration workspace.
2. Produce the crosswalk, inclusion and exclusion results, and exact path manifest. Preserve imported bytes unless the approved transformation contract says otherwise.
3. Validate the prospective worktree, exact staged set, candidate tree, and resulting commit. Run schema, generated-output, link, size, binary, secret, privacy, license, authority, identity, and complete-history checks.
4. Re-read live provider controls and access surfaces, and verify that `origin/main` still equals the package's expected object ID.
5. Create the sole-owner commit, advance local `main` only by fast-forward or an exact compare-and-swap, and use the package's ordinary non-forced push. Force, force-with-lease, history rewrite, and unapproved merge commits are prohibited.
6. Verify the exact remote head and a clean, full, non-shallow clone. Observe the read-only repository audit through a passing terminal result.
7. Seal an append-only completion receipt containing the source and exclusion hashes, path and transformation results, base/tree/commit/remote object IDs, validation results, CI run URL and conclusion, and any in-envelope correction. Advance the tranche high-water mark only after all checks pass.

CI runs after public disclosure, so the same full validation must pass locally on the exact commit before push. A successful push is not tranche closure until remote exactness, clean-clone validation, and CI are green.

## Corrections inside the package

A correction needs no new approval only when the package expressly allows its class and the correction is mechanical, non-semantic, confined to named paths, and does not alter source selection, artifact disposition, rights, authority, repository controls, or publication scope. After any correction, every affected validation layer must be rerun. A post-push CI failure blocks tranche closure and later tranches; any repair outside the frozen corrective envelope requires a focused replacement package.

## Fail-closed conditions

Stop without committing or pushing, or stop closure if publication already occurred, when any of these occurs:

- missing source, source-hash mismatch, inventory drift, or incomplete source visibility;
- an unclassified artifact, new binary or size exception, or unresolved rights, privacy, secret, local-path, or third-party-content risk;
- a path, case, or Unicode collision; an unapproved rename; or a semantic transformation outside the package;
- a staged path outside the allowlist or any validation, test, generated-output, identity, or history failure that cannot be corrected within the frozen envelope;
- validator weakening, workflow expansion, or provider-control change not expressly named in the package;
- unexpected upstream writer, collaborator, invitation, App, deploy key, Actions permission, branch/ruleset state, remote-head drift, or non-fast-forward condition;
- any need for force, history rewrite, provider-setting mutation, Drive mutation outside a declared native-authoring workflow, authority-epoch change, cleanup, or deletion.

These stops require an owner-reviewed corrected or replacement package. The single-package process never expands the active authority scope or creates a new authority epoch.
