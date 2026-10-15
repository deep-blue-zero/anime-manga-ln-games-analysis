# Repository operating card

Start here. This card says what each role reads and may write; the linked documents own the rules.

## Every session

Read `governance/AUTHORITY_STATE.yaml` and `governance/AUTHORITY_SCOPE.json` before proposing or applying changes. Authority epoch 1 is active and owner-accepted; its activation record is `governance/cutovers/AUTHORITY_EPOCH_1_ACTIVATION_RECORD.md`. This repository is the primary analytical authority only for the exact hashed scope in `governance/AUTHORITY_SCOPE.json`. Native Google Sheets remain controlled Drive authoring surfaces whose revisions become effective only after verified export and Git merge; reference-only artifacts and the primary-source/extraction workspace remain outside Git authority.

Routing, trust boundaries and stop conditions are in `governance/CHATGPT_AUTHORITY_AND_ROUTING.md`, which applies to every agent despite its path.

Analytical accuracy and fidelity to source evidence are the substantive objective; repository controls exist to preserve them. Correct demonstrated errors through legitimate routes, and when a control appears to block an evidence-backed correction, follow Section 4.2 of `governance/CHATGPT_AUTHORITY_AND_ROUTING.md` and the checklist's correction and conflict procedure. Diagnose and propose within scope; a diagnosis or claim of improved accuracy is never write, source, publication, or global-control authority.

## Every commit and push

Before staging or committing, read and follow `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md`. Classify the change with `governance/repository-controls/change-obligations.json`. Stable analytical branches use the checklist's author preflight and may await housekeeping for five deterministic routing outputs; this is not integration readiness. Other changes use `python tools/prepare_commit.py --base origin/main --check` against the final staged index. Integration always requires the fully synchronized final commit and its successful `Repository integration audit` status. Character discovery may lag as expressly permitted by its maintenance policy.

Stage exact paths only: do not use `git add .` or wildcard staging. Push without force and never rewrite published history.

Maintain analytical documents, ledgers, readiness tables, and project-local indexes through targeted edits to verified current contents. Preserve unaffected bytes, structure, identifiers, links, and history; do not reconstruct a whole document from memory, excerpts, or summaries to work around tool limits. Full-file API submission must still contain the original contents plus the intended edits, with the complete diff and resulting remote content verified. Follow the maintained-document and connector-failure rules in `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md`; documented generated outputs continue to use their designated generators.

## By role

Concurrent title work follows `governance/policies/BRANCH_LIFECYCLE.md`.

### Series or study analysis

Use the stable `series/<stable-slug>` branch for continuing series analysis and `studies/<stable-slug>` for continuing study work. Series analysis belongs under `series/<stable-slug>/`; comparative, taxonomy, and other non-series work belongs under `studies/<stable-slug>/`. Preserve imported bytes unless a declared transformation authorizes a derivative.

Before substantial analytical execution, read the Analytical execution routing subsection of `governance/CHATGPT_AUTHORITY_AND_ROUTING.md` and follow its applicable reasoning, capability, long-series execution, and handoff policies. Resolve stage ownership and required evidence capabilities before starting the assigned work; existing project methods, initiation/continuation gates, and repository controls remain governing.

Before the first substantive sequential source-unit analysis of a newly initiated or materially restarted analytical project, read and satisfy `governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md`. Sequential analysis remains locked until a canonical/current-eligible analytical method and synthesis/corpus architecture exist, the canonical current-state/corpus-map entrypoint identifies both, architecture-required day-one infrastructure is initialized, and that entrypoint explicitly records `SEQUENTIAL_ANALYSIS_LOCK = OPEN`; scaffolding alone does not open the gate.

On these branches, author analysis and required routing descriptors; only the curation agent may supply a coordinated character repair before integration. Do not manually write housekeeping-owned routing outputs; the five-output boundary and routing inputs are defined by `governance/policies/AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md`.

Before pushing a stable analytical branch, follow the [publication sequence and squash-merge reconciliation procedure](governance/policies/CHANGE_INTEGRATION_CHECKLIST.md#stable-analytical-publication-sequence):

- Fetch current `main` and the remote source branch; preserve intervening author, housekeeping, and curation commits, and incorporate current `main` without rewriting history.
- Review the exact candidate and run author preflight. Recheck both remote heads immediately before every push; if either advanced, reconcile and repeat affected checks.
- Push without force and verify the published commit and changed files. Never resolve squash-history conflicts through an unverified whole-file `ours` or `theirs` choice.
- Complete source audit, housekeeping, and the final exact-head integration audit before publishing the next tranche. Preparing analysis may continue while checks run; a diagnosed repair or explicitly coordinated superseding push must reconcile current heads and restart validation for its new commit.

### Governance, tooling, and other cross-cutting work

Use a narrowly named temporary branch under an audited agent prefix: `codex/<purpose>`, `chatgpt/<purpose>` or `claude/<purpose>`. Changes to validation, workflows, schemas, publication safety, or authority controls use `python tools/prepare_commit.py --base origin/main --check --full`. Temporary bootstrap, repair, migration, and one-shot automation branches must be pruned after their exact tips are verified as preserved on a green `main`; never delete an unverified or unmerged branch.

### Character curation

The owner-authorized cloud curation agent is the sole routine writer of `characters/registry.jsonl` and generated `CHARACTER_ANALYSIS_INDEX.md`; follow `governance/policies/CHARACTER_DISCOVERY_MAINTENANCE.md`. Its recurring branch is exactly `character-registry` and may remain active. Housekeeping never writes either character file or applies character upserts.

## Never, without a separately reviewed owner amendment

Never add raw acquisition evidence, source media, private migration evidence, credentials, unreviewed binaries, symlinks, submodules, or hooks.

The approved workflows are the content-read-only `.github/workflows/repository-audit.yml` with its isolated status-only reporter, the default-branch, exact-output-allowlisted `.github/workflows/global-index-housekeeping.yml`, and `.github/workflows/nightly-integration.yml` under `governance/policies/NIGHTLY_ANALYTICAL_INTEGRATION.md`. The owner authorizes nightly mechanical integration of audited stable series/study branches, including clean reconciliation, protected PR merges, and explicit post-merge audits. Every other workflow remains prohibited without a separately reviewed owner amendment.

## License

Original content is covered only by the narrow CC BY-NC 4.0 scope in `LICENSE.md`. Third-party exclusions are described in `THIRD_PARTY_NOTICES.md`. The license grants no upstream contribution or write authority.
