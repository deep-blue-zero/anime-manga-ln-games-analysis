# Repository operating boundary

Read `governance/AUTHORITY_STATE.yaml` and `governance/AUTHORITY_SCOPE.json` before proposing or applying changes.

Until an owner-approved G8 activation record changes the authority epoch, Google Drive remains authoritative and this repository is a nonauthoritative migration candidate. Do not represent repository content as active authority before that transition.

Never add raw acquisition evidence, source media, private migration evidence, credentials, unreviewed binaries, symlinks, submodules, hooks, or workflows. Stage only paths named by an approved batch manifest; do not use `git add .` or wildcard staging.

Series analysis belongs under `series/<stable-slug>/`; comparative, taxonomy, and other non-series work belongs under `studies/<stable-slug>/`. Preserve imported bytes unless a declared transformation authorizes a derivative.
