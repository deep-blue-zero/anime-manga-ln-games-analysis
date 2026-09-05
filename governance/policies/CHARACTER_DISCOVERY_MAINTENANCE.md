# Character discovery maintenance

## Ownership and execution

The owner-authorized character curation agent is the sole routine writer of `characters/registry.jsonl` and `CHARACTER_ANALYSIS_INDEX.md`. It interprets analytical evidence and curates the structured registry; it invokes `tools/generate_character_index.py` to produce the deterministic Markdown view. The index must never be independently authored.

The recurring task runs in a cloud environment with Git, Python, the hash-locked validation dependencies, and authenticated GitHub access. Its schedule and credentials are configured externally by the owner. This policy does not install or activate a scheduled task and requires no owner computer, local drive, local clone, or migration directory.

GitHub Actions remains responsible for independent read-only validation. Global index housekeeping owns only the five series/study routing outputs in `AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md`; neither that workflow nor its synchronizer may read character proposals as replacement inputs, rewrite the character registry, or generate the character index.

The two-file allowlist applies to the agent's authored delta. It grants no authority to modify analytical prose, evidence or authority metadata, schemas, tools, workflows, other registries, or Drive files. Preserve unrelated character records, including study-based entries. Deletion, identity transfer between series, and reconstruction assessment remain outside routine curation authority.

## Daily discovery on main

1. Read the live repository instructions, authority records, integration checklist, character README and schema. Verify the exact repository identity and approved commit identities.
2. Capture the full current `main` SHA. Review added, changed, renamed, and deleted tracked analytical files under `series/` since the last trustworthy completed review. Reassess affected existing records and retain deferred candidates. Routine discovery never treats unmerged evidence as effective.
3. Read candidate prose and the relevant entrypoint or ledger. Include substantial reviewed dedicated or distributed analysis only when current evidence is eligible and supports every claimed dimension, identity, alias, anchor, and coverage range. Mentions and filenames are insufficient. Defer ambiguity without inventing metadata or repairing the source.
4. Use the reusable `character-registry` branch and at most one open curation PR to `main`. Reconcile current `main` and pending branch work without overwriting concurrent changes, force-pushing, or rewriting published history. The complete ordinary curation PR diff may contain only the two character outputs.
5. Stage `characters/registry.jsonl`; run `python tools/generate_character_index.py --snapshot index`; stage `CHARACTER_ANALYSIS_INDEX.md`; then run `python tools/prepare_commit.py --base origin/main --check`. Apply additional live obligations and inspect the entire diff. Required checks must pass without weakening validation.
6. Publish normally under approved identities. The existing Repository audit runs on pushes to `character-registry`. If a token-originated push does not start a run, use the existing exact-commit dispatch or manual workflow dispatch and verify the audited SHA.
7. The owner authorizes the configured curation agent to merge its bounded PR after semantic review, all applicable checks, and the Repository audit succeed for the exact current head. Recheck both heads and reconcile/revalidate any drift. Use an enabled merge method compatible with live protection, including linear-history requirements, and an expected-head SHA where supported. Do not push directly to `main`, bypass protections, or treat a missing, skipped, pending, or older check as success.
8. Verify the integrated patch and the Repository audit for the exact integration commit on `main`. A post-merge failure must be reported as already integrated but unverified; do not automatically revert or rewrite `main`.

Structural checks are necessary but cannot establish the correctness of textual interpretation. Only evidence-supported, reviewed changes may be automatically integrated.

## Delayed discovery versus existing-reference integrity

New eligible analysis may merge without immediate character enrollment when the existing registry and generated index still validate. Discovery is intentionally allowed to lag until the next agent run; the registry is not presumed exhaustive.

Changes to already referenced evidence can invalidate a path, anchor, authority relationship, coverage claim, or generated digest before the daily run. Such changes must not merge with a broken character registry or stale index. Keep the existing strict validation and coordinate with the same curation agent before integration.

For this bounded on-demand mode:

- The owner/source task supplies the exact analytical branch and reviewed source commit. This is separate from ordinary main-only discovery; unmerged evidence remains proposed.
- The curation agent reviews the affected records against that proposed tree and authors only the two character outputs in a separately identifiable commit on the source branch, preserving the source author's work and identities.
- The source branch may carry that agent-authored repair alongside its own analytical changes. Housekeeping's branch-confinement check admits the two character files for this purpose but its write/staging allowlist does not.
- Reconcile current `main`, validate the entire prospective integration, require the final exact-head audit and any housekeeping child-commit audit, and have the owner/source integration task merge the combined change atomically. The curation agent's ordinary automatic-merge authority does not extend to analytical changes.
- If either source or base advances, repeat the affected review and validation. If the agent is unavailable or the repair is ambiguous, leave the source change blocked. Never disable an integrity check to wait for tomorrow's scan.
- Verify the combined integration on `main`. Do not count unrelated source-branch content as completed daily main review.

## Retired declarative character inputs

`series/<stable-slug>/.repository/character-registry-upserts.jsonl` is no longer an authoritative input or required authoring surface. Housekeeping ignores it, including malformed or stale proposals, and cannot replay its values over curated global records.

Preserve any existing proposal files and Git history as provenance. The agent may read them as optional leads, but must independently verify their assertions against eligible analysis. Their disagreement with the global registry is not a synchronization obligation. Do not create or maintain these files merely to drive character enrollment.

Series/study routing descriptors retain their existing deterministic housekeeping role.

## Coverage, concurrency, and reporting

Serialize curation runs, including on-demand repairs, so they do not compete over the same records or branch. Preserve pending PR work between runs and inspect unexpected branch content before any write.

Keep durable coverage and unresolved-candidate records in cloud task storage and relevant PR descriptions, never in a disposable checkout or container cache. Record reviewed base SHA, reviewed/deferred coverage, PR head, integration SHA, and validation outcomes. Track review completion separately from publication and integration; never advance completed coverage beyond unfinished work.

If no trustworthy checkpoint is available, use the existing repository audit records to establish a documented baseline and review missing coverage explicitly. Do not silently assume completeness or skip changes.

Do not create empty commits or PRs. Successful no-change runs remain quiet. Report verified integrations, substantive unresolved findings, access/validation failures, blocked integration, post-merge failure, or incomplete review.

Retain `character-registry` while the recurring task is active. If it was deleted after a verified integration, recreate it from current `main`. Reuse it without force; retire it only after its intended content and exact integration are verified and no pending work remains.
