# Publication and contribution policy

## Upstream authority

`deep-blue-zero` is the sole upstream human writer and contributor. No other collaborator, invitation, team, external pull-request merge, imported patch, or cherry-picked external commit is permitted. Unexpected upstream write authority or a non-owner commit is a severity-1 stop condition.

The public may read, link to, and independently fork the repository. Platform visibility and forking capability do not grant a content license. An independent fork has no authority over upstream. Depending on GitHub settings, outsiders may be able to open issues, discussions, or pull-request proposals; none are accepted for merge, cherry-pick, or patch import. Feedback can inform later owner work, but any upstream result must be independently authored and committed by `deep-blue-zero` without copying an external patch.

## Provider controls

The repository completed its G3 public-visibility activation. The exact activation, post-activation provider-state, and independent-audit evidence hashes are recorded in `../repository-controls/public-activation-bindings.json`; that historical verification must not be represented as a live provider reread.

GitHub must enforce `main` protection for administrators, require linear history, and prohibit force pushes and deletion. An active ruleset must prohibit deletion and non-fast-forward updates for `refs/tags/activation/**`. Before every later public push or activation-tag operation, provider controls and access surfaces must be reread. If they are absent or cannot be verified, the state is `UNVERIFIED` and the operation stops.

No non-owner collaborator or team may receive write authority. The sole tracked workflow, `.github/workflows/repository-audit.yml`, uses read-only contents permission and may only report audit success or failure. It has no secret, artifact-upload, auto-fix, commit, issue, pull-request, release, tag, or push authority. Every other workflow and every write-capable automation requires a separately hash-bound owner amendment.

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
