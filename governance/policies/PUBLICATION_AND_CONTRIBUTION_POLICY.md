# Publication and contribution policy

## Upstream authority

`deep-blue-zero` is the sole upstream human writer and contributor. No other collaborator, invitation, team, external pull-request merge, imported patch, or cherry-picked external commit is permitted. Unexpected upstream write authority or a non-owner commit is a severity-1 stop condition.

The public may read, link to, and independently fork the repository. An independent fork has no authority over upstream. Feedback can inform later owner work, but any upstream result must be independently authored and committed by `deep-blue-zero`.

## Provider controls

Once the repository becomes public, GitHub must enforce `main` protection for administrators, require linear history, and prohibit force pushes and deletion. An active ruleset must prohibit deletion and non-fast-forward updates for `refs/tags/activation/**`. No activation tag or corpus publication is allowed while either control is absent or unverifiable.

Default GitHub Actions workflow permissions remain read-only. Adding a write-capable automation requires a separately hash-bound owner amendment.

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

No content license is currently selected. Public visibility does not select one. A recorded owner licensing and third-party-notice decision is required before the first substantive analytical corpus batch is published.
