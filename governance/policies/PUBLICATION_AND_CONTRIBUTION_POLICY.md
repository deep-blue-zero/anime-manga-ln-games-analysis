# Publication and contribution policy

## Upstream authority

`deep-blue-zero` is the sole upstream human writer and contributor. No other collaborator, invitation, team, external pull-request merge, imported patch, or cherry-picked external commit is permitted. Unexpected upstream write authority or a non-owner commit is a severity-1 stop condition.

The public may read, link to, and independently fork the repository. Platform visibility and forking capability do not grant a content license. An independent fork has no authority over upstream. Depending on GitHub settings, outsiders may be able to open issues, discussions, or pull-request proposals; none are accepted for merge, cherry-pick, or patch import. Feedback can inform later owner work, but any upstream result must be independently authored and committed by `deep-blue-zero` without copying an external patch.

## Provider controls

The repository completed its G3 public-visibility activation. The exact activation, post-activation provider-state, and independent-audit evidence hashes are recorded in `../repository-controls/public-activation-bindings.json`; that historical verification must not be represented as a live provider reread.

Active repository ruleset `25199066` governs exactly `refs/heads/main`, with target `branch` and no ref exclusions. It must permit no bypass actors, including the owner/admin, prohibit deletion and non-fast-forward updates, and require strict up-to-date `Repository integration audit` status from GitHub Actions app `15368`. It does not require linear history; pull requests integrate as merge commits. Verify it through the repository ruleset-detail endpoint `rulesets/25199066`: `current_user_can_bypass: never` is required, and `bypass_actors` must be empty whenever the credential can read it. Active activation-tag ruleset `21946617` must continue to prohibit deletion and non-fast-forward updates for `refs/tags/activation/**` without bypass actors. Before every later public push or activation-tag operation, the pusher rereads both ruleset details and both remote heads. If any of them is absent or cannot be verified, the state is `UNVERIFIED` and the operation stops. These operational checks use the rulesets rather than the classic branch-protection endpoint; this policy grants no authority to alter provider settings. The merge gate does not inspect collaborators, pending invitations, deploy keys, installed GitHub Apps or Actions permission settings. The owner reviews those surfaces when changing repository settings and checks them before merging a pull request by hand. An agent whose credential cannot read these surfaces records that it could not, and does not hold an ordinary branch push for them.

No non-owner collaborator or team may receive write authority. `.github/workflows/repository-audit.yml` validates with `contents: read` only. Its separate fixed reporter has `statuses: write` only, does not check out or execute repository code, and publishes only `Repository integration audit` on the exact audited SHA. It reports success for a complete passing audit, pending for authored content awaiting routing, and failure/error for unsuccessful validation. Two workflows write repository content. `.github/workflows/global-index-housekeeping.yml` runs from the trusted default-branch definition after an owner push audit, has `contents: write` only, and may append one ordinary non-forced commit to the same stable series/study branch containing only the five routing outputs listed in `AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md`. It cannot write analytical content, delete registry entries, push `main`, manage branches/tags, or write issues, pull requests, releases, or artifacts. `.github/workflows/nightly-integration.yml`, the owner-dispatched bulk-merge workflow, keeps a read-only repository token and supplies the owner credential `NIGHTLY_INTEGRATION_TOKEN` only to the merge gate, which may push one clean non-forced reconciliation merge to a stable series/study branch, open or reuse an owner-authored pull request, and merge it through protected `main` as a merge commit under `NIGHTLY_ANALYTICAL_INTEGRATION.md`. The scheduled CI and PR Integration Steward has the standing delegation in [the integration policy](NIGHTLY_ANALYTICAL_INTEGRATION.md#ci-and-pr-integration-steward), without per-PR reapproval for eligible work. It may publish verified repairs on PR branches under approved owner identities and merges only through the same gate. This is owner-operated automation, not an additional upstream contributor. Candidate code never receives write credentials. Other automation capabilities and changes to these boundaries require a separately reviewed owner amendment.

### Automated character discovery access checks

The owner-authorized curation agent's bounded `character-registry` integration under `CHARACTER_DISCOVERY_MAINTENANCE.md` is an automated integration route, including when executed through an authenticated API or CLI. It does not use the manual-merge requirement to inspect every access surface through the browser on each run. This provision applies only to an owner-authored PR from `character-registry` to `main` whose complete diff contains only `characters/registry.jsonl` and `CHARACTER_ANALYSIS_INDEX.md`; it does not extend to governance amendments, analytical source PRs, or reconstruction evaluation.

Before each such merge, the agent must:

1. Verify the live repository identity, approved author and committer identities, current source and base heads, and both ruleset details with all protections specified above, including explicit absence of bypass actors.
2. Use authenticated GitHub API access to retrieve the complete collaborator, pending invitation, and deploy-key lists, following all pagination. Require that every collaborator is `deep-blue-zero`, no invitation is pending, and no deploy key has write access. An unreadable, incomplete, missing, or ambiguous response is not an empty list: record the failure and stop integration. Any non-owner collaborator, pending invitation, or write-enabled deploy key also stops integration under the existing owner-only policy.
3. Complete semantic review, the two-file diff review, all applicable validation, and the full Repository audit with a successful `Repository integration audit` status for the exact current head. Recheck both heads immediately before the protected merge and reconcile/revalidate drift. Use an enabled merge method compatible with live protection and an expected-head SHA where supported; never push directly to `main` or bypass protections. Verify the integrated patch and the exact integration commit's audit on `main` afterward.
4. Record the access-check time and outcomes, reviewed base and source SHAs, required audit results, and integration SHA in the existing durable checkpoint or PR reporting mechanism. Do not record credentials or represent historical settings reviews as fresh API observations.

Installed GitHub App grants and Actions permission settings remain subject to owner review when those settings change. A reported or observed access anomaly requires renewed review before automated integration resumes. In the absence of such a change or anomaly, a fresh browser inspection of those settings and GitHub sudo-mode reauthentication are not prerequisites for each discovery run or merge. An expired browser sudo session alone is not an access anomaly and must not trigger repeated reauthentication requests. Missing or expired API credentials still block required API checks; this provision grants no new credentials, permissions, or authority to change provider settings.

The manual-merge access review, other integration routes, ordinary branch-publication rules, curation ownership and two-file allowlist remain unchanged. This provision takes effect only after this governance amendment is integrated through the existing authorized governance route; it cannot authorize its own merge.

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
