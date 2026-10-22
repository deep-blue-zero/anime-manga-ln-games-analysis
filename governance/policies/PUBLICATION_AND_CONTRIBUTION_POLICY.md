# Publication and contribution policy

## Upstream authority

`deep-blue-zero` is the sole upstream human writer and contributor. No other collaborator, invitation, team, external pull-request merge, imported patch, or cherry-picked external commit is permitted. Unexpected upstream write authority or a non-owner commit is a severity-1 stop condition.

The public may read, link to, and independently fork the repository. Platform visibility and forking capability do not grant a content license. An independent fork has no authority over upstream. Outsiders may be able to open issues, discussions or pull-request proposals; none are accepted for merge, cherry-pick or patch import. Feedback can inform later owner work, but any upstream result must be independently authored and committed by `deep-blue-zero`.

The repository's agents are owner-operated automation, not additional contributors: they commit under approved owner identities, and candidate code never receives write credentials.

## Provider controls

The `main` ruleset must stay active with no bypass actors, block deletion and force-pushes, and require a strict, up-to-date `Repository integration audit` from GitHub Actions. It does not require linear history; pull requests integrate as merge commits. The activation-tag ruleset must keep blocking deletion and force-pushes on `refs/tags/activation/**`. The merge gate rechecks the `main` ruleset in code before each merge; the exact ruleset and app identifiers live in `tools/nightly_integration.py`. This policy grants no authority to change provider settings.

The merge gate confirms at the start of each apply run that there is no other collaborator, pending invitation or write-enabled deploy key, and halts otherwise. The owner reviews those, installed GitHub Apps and Actions permissions when changing repository settings, and before merging a pull request by hand. The G3 public-visibility activation evidence is archived in `../archive/migration/public-activation-bindings.json`; it is historical, not a live provider reading.

Three workflows are approved:

- `.github/workflows/repository-audit.yml` validates with `contents: read`; its separate reporter has only `statuses: write` and reports the exact audited commit.
- `.github/workflows/global-index-housekeeping.yml` may append one ordinary commit, containing only the five routing outputs in `AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md`, to a series or study branch.
- `.github/workflows/nightly-integration.yml` is the owner-dispatched bulk merge under `NIGHTLY_ANALYTICAL_INTEGRATION.md`.

Any other automation capability needs a separately reviewed owner amendment.

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
