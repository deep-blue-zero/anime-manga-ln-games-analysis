# Repository operating boundary

Read `governance/AUTHORITY_STATE.yaml` and `governance/AUTHORITY_SCOPE.json` before proposing or applying changes.

Until an owner-approved G8 activation record changes the authority epoch, Google Drive remains authoritative and this repository is a nonauthoritative migration candidate. Do not represent repository content as active authority before that transition.

Never add raw acquisition evidence, source media, private migration evidence, credentials, unreviewed binaries, symlinks, submodules, or hooks. The sole approved workflow is `.github/workflows/repository-audit.yml` under its read-only, non-mutating contract; every other workflow remains prohibited without a separately reviewed owner amendment. Stage only paths named by an approved batch manifest; do not use `git add .` or wildcard staging.

Series analysis belongs under `series/<stable-slug>/`; comparative, taxonomy, and other non-series work belongs under `studies/<stable-slug>/`. Preserve imported bytes unless a declared transformation authorizes a derivative.

Original content is covered only by the narrow CC BY-NC 4.0 scope in `LICENSE.md`. Third-party exclusions are described in `THIRD_PARTY_NOTICES.md`. The license grants no upstream contribution or write authority.
