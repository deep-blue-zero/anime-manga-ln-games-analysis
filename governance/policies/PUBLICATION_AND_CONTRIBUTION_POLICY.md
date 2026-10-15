# Publication and contribution policy

## Upstream authority

`deep-blue-zero` is the sole upstream human writer and contributor. No other collaborator, invitation, team, external pull-request merge, imported patch, or cherry-picked external commit is permitted. Unexpected upstream write authority or a non-owner commit is a severity-1 stop condition.

The public may read, link to, and independently fork the repository. Platform visibility and forking capability do not grant a content license. An independent fork has no authority over upstream. Depending on GitHub settings, outsiders may be able to open issues, discussions, or pull-request proposals; none are accepted for merge, cherry-pick, or patch import. Feedback can inform later owner work, but any upstream result must be independently authored and committed by `deep-blue-zero` without copying an external patch.

## Provider controls

The repository completed its G3 public-visibility activation. The exact activation, post-activation provider-state, and independent-audit evidence hashes are recorded in `../repository-controls/public-activation-bindings.json`; that historical verification must not be represented as a live provider reread.

GitHub must enforce `main` protection for administrators, require linear history, and prohibit force pushes and deletion. An active ruleset must prohibit deletion and non-fast-forward updates for `refs/tags/activation/**`. Before every later public push or activation-tag operation, the pusher rereads the provider controls its credential can read: `main` protection, the activation-tag ruleset, and both remote heads. If any of them is absent or cannot be verified, the state is `UNVERIFIED` and the operation stops. Collaborators and pending invitations are checked before integration instead: the nightly controller reads both lists with the owner credential on every run, and an apply run halts before any write if anyone other than `deep-blue-zero` has access, an invitation is pending, or either list is unreadable (`NIGHTLY_ANALYTICAL_INTEGRATION.md`). The owner checks them before merging a pull request by hand. An agent whose credential cannot read those lists records that it could not, and does not hold an ordinary branch push for them.

No non-owner collaborator or team may receive write authority. `.github/workflows/repository-audit.yml` validates with `contents: read` only. Its separate fixed reporter has `statuses: write` only, does not check out or execute repository code, and publishes only `Repository integration audit` on the exact audited SHA. It reports success for a complete passing audit, pending for authored content awaiting routing, and failure/error for unsuccessful validation. Two workflows write repository content. `.github/workflows/global-index-housekeeping.yml` runs from the trusted default-branch definition after an owner push audit, has `contents: write` only, and may append one ordinary non-forced commit to the same stable series/study branch containing only the five paths in `global-index-automation-policy.json`. It cannot write analytical content, delete registry entries, push `main`, manage branches/tags, or write issues, pull requests, releases, or artifacts. `.github/workflows/nightly-integration.yml` keeps a read-only repository token and supplies the owner credential `NIGHTLY_INTEGRATION_TOKEN` only to its hash-bound controller, which may push one clean non-forced reconciliation merge to a stable series/study branch, open or reuse an owner-authored pull request, merge it through protected `main`, and dispatch the post-merge audit under `NIGHTLY_ANALYTICAL_INTEGRATION.md`. Every other workflow or automation capability requires a separately reviewed owner amendment.

## Publication safety

Public disclosure is treated as irreversible. Before every public push, validation must cover the complete candidate change and reachable history as applicable and must reject:

- credentials, secret material, or personal email addresses;
- local absolute paths or local evidence locations;
- unresolved Google Drive or Google Docs links where a migrated repository-relative target is required;
- primary-source media, raw acquisition evidence, excluded binaries, and other non-Git artifact classes;
- content outside the approved manifest or repository topology;
- externally authored commits or imported patches; and
- unreviewed licensing or third-party-rights exposure.

A failed publication check stops the push. Content must not be published first and cleaned up afterward.

## License state

Covered original content is licensed under CC BY-NC 4.0 within the exact scope in `../../LICENSE.md`. Quoted source text, franchise assets and marks, third-party material, referenced Drive artifacts, migration evidence, and repository software/tooling are excluded. `../../THIRD_PARTY_NOTICES.md` describes the public third-party boundary. The license grants no upstream contribution, merge, or write authority.
