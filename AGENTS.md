# Repository operating boundary

Read `governance/AUTHORITY_STATE.yaml` and `governance/AUTHORITY_SCOPE.json` before proposing or applying changes.

Before staging or committing, read and follow `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md`. Classify the change with `governance/repository-controls/change-obligations.json`, update every required registry and generated surface, and run `python tools/prepare_commit.py --base origin/main --check` against the final staged index. A commit is incomplete while any required index, manifest, or navigation surface is stale.

Authority epoch 1 is active and stabilizing. This repository is the primary analytical authority only for the exact hashed scope in `governance/AUTHORITY_SCOPE.json`. Native Google Sheets remain controlled Drive authoring surfaces whose revisions become effective only after verified export and Git merge; reference-only artifacts and the primary-source/extraction workspace remain outside Git authority.

Never add raw acquisition evidence, source media, private migration evidence, credentials, unreviewed binaries, symlinks, submodules, or hooks. The sole approved workflow is `.github/workflows/repository-audit.yml` under its read-only, non-mutating contract; every other workflow remains prohibited without a separately reviewed owner amendment. Recurring tranches follow `governance/policies/RECURRING_TRANCHE_PROCESS.md`: one owner-approved package may cover the bounded transformation-to-non-forced-push lifecycle, while its exact path manifest remains the staging allowlist. Do not use `git add .` or wildcard staging. A correction stays inside that approval only when it is expressly allowed, mechanical, non-semantic, confined to named paths, and followed by complete revalidation.

Series analysis belongs under `series/<stable-slug>/`; comparative, taxonomy, and other non-series work belongs under `studies/<stable-slug>/`. Preserve imported bytes unless a declared transformation authorizes a derivative.

Concurrent title work follows `governance/policies/BRANCH_LIFECYCLE.md`. Use the stable `series/<stable-slug>` branch for continuing series analysis and `studies/<stable-slug>` for continuing study work. Temporary bootstrap, repair, migration, and automation branches must be pruned after their exact tips are verified as preserved on a green `main`; never delete an unverified or unmerged branch.

Original content is covered only by the narrow CC BY-NC 4.0 scope in `LICENSE.md`. Third-party exclusions are described in `THIRD_PARTY_NOTICES.md`. The license grants no upstream contribution or write authority.
