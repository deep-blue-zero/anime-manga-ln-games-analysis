# Repository operating card

Start here. This card routes work; the linked documents own the rules. Acquire governance by the operation's actual responsibilities using the [task-dependent reading path](governance/AGENT_ROUTING.md#6-mandatory-first-read-order), including additional sections before scope changes. A role label does not exempt an operation from its controls.

## Every session

`main` of this repository is the analytical authority. Native Google Sheets remain controlled Drive authoring surfaces whose revisions become effective only after verified export and Git merge; reference-only artifacts and the primary-source/extraction workspace remain outside Git authority. The Drive-to-Git migration is complete (authority epoch 1, accepted 2026-10-15); its records are archived in `governance/archive/migration/` and are read only for a specific provenance question.

Read Sections 2-4, 6-7 and 12 of `governance/AGENT_ROUTING.md`. Its Section 6 selects the remaining context; a link alone does not require reading an unrelated policy in full.

Analytical accuracy and fidelity to source evidence are the substantive objective; repository controls exist to preserve them. Correct demonstrated errors through legitimate routes, and when a control appears to block an evidence-backed correction, follow Section 4.2 of `governance/AGENT_ROUTING.md` and the checklist's correction and conflict procedure. Diagnose and propose within scope; a diagnosis or claim of improved accuracy is never write, source, publication, or global-control authority.

## Roles

Any provider's agent may fill a role. Each role writes only its own paths, and only the CI agent and the owner merge.

| Role | Job | Writes | Reaches `main` through | Policy |
| --- | --- | --- | --- | --- |
| Analysis author | Literary analysis, deep reading, character reconstruction | Its `series/` or `studies/` root and routing descriptor | PR merged by the CI agent | This card, the checklist and routing |
| CI agent | Review, reconcile, repair and merge open PRs | Repairs on PR branches | The merge gate | `governance/policies/NIGHTLY_ANALYTICAL_INTEGRATION.md` |
| Character discovery agent | Keep the character registry current | `characters/registry.jsonl`, `CHARACTER_ANALYSIS_INDEX.md` | PR on `character-registry` | `governance/policies/CHARACTER_DISCOVERY_MAINTENANCE.md` |
| Reconstruction evaluator | Grade how well evidence supports modeling each character | `characters/reconstruction_capabilities.jsonl`, `characters/CHARACTER_RECONSTRUCTION_INDEX.md` | PR on `character-reconstruction` | `governance/policies/CHARACTER_RECONSTRUCTION_MAINTENANCE.md` |
| Housekeeping (workflow) | Regenerate series/study routing | The five routing outputs | A child commit on the analysis branch | `governance/policies/AUTOMATED_GLOBAL_INDEX_MAINTENANCE.md` |
| Drive inventory agent | Keep the inventory of primary-source folders on Google Drive current | Nothing in Git | — | [Drive inventory](#drive-inventory) |
| Owner | Guardrail changes, holds, reconstruction review, settings and deployment | — | Merges personally | — |

A recorded reconstruction capability is not present readiness; verify currentness with `tools/reconstruction_status.py`.

## Every commit and push

Before editing, staging, committing or pushing, acquire the applicable sections of `governance/policies/CHANGE_INTEGRATION_CHECKLIST.md` and classify the change with `governance/repository-controls/change-obligations.json`. Analysis branches use the checklist's author preflight; other changes use `python tools/prepare_commit.py --base origin/main --check` against the final staged index. A change is ready for integration only when its exact head has a successful `Repository integration audit`.

Stage exact paths only: do not use `git add .` or wildcard staging. Push without force and never rewrite published history.

Maintain analytical documents, ledgers, readiness tables, and project-local indexes through targeted edits to verified current contents. Preserve unaffected bytes, structure, identifiers, links, and history; never reconstruct a whole document from memory, excerpts, or summaries to work around tool limits. Generated outputs use their designated generators.

## Series or study analysis

Use the stable `series/<stable-slug>` branch for continuing series analysis and `studies/<stable-slug>` for continuing study work. Series analysis belongs under `series/<stable-slug>/`; comparative, taxonomy, and other non-series work belongs under `studies/<stable-slug>/`. Preserve imported bytes unless a declared transformation authorizes a derivative. Concurrent title work follows `governance/policies/BRANCH_LIFECYCLE.md`.

Before substantial analytical execution, read the Analytical execution routing subsection of `governance/AGENT_ROUTING.md` and follow its applicable reasoning, capability, long-series execution, and handoff policies. Resolve stage ownership and required evidence capabilities before starting the assigned work; existing project methods, initiation/continuation gates, and repository controls remain governing. Write analytical prose to the named-subject and referential-clarity standard in section 15 of `governance/source-policies/MANGA_ANIME_ANALYTICAL_HANDOFF_AND_INTEGRATION_CONTRACT.md`, and perform its bounded name-and-reference check before semantic acceptance, authority promotion, or integration.

Before the first substantive sequential source-unit analysis of a newly initiated or materially restarted analytical project, read and satisfy `governance/source-policies/MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md`. Sequential analysis remains locked until a canonical/current-eligible analytical method and synthesis/corpus architecture exist, the canonical current-state/corpus-map entrypoint identifies both, architecture-required day-one infrastructure is initialized, and that entrypoint explicitly records `SEQUENTIAL_ANALYSIS_LOCK = OPEN`; scaffolding alone does not open the gate.

Author analysis and any required routing descriptor; never hand-write the housekeeping-owned routing outputs or the character and reconstruction files. A routing descriptor's `catalog_note` describes the project, never its progress; progress belongs in the project's entrypoint.

Publish through the [publication sequence](governance/policies/CHANGE_INTEGRATION_CHECKLIST.md#stable-analytical-publication-sequence): start from current `main` and the remote branch, run author preflight, push without force, and wait for the exact-head audit before publishing the next tranche. The CI agent merges the branch's PR.

## Governance, tooling, and other cross-cutting work

Use a narrowly named temporary `agent/<purpose>` branch; the older `codex/`, `chatgpt/` and `claude/` prefixes remain valid. Changes to validation, workflows, schemas, publication safety, or controls use `python tools/prepare_commit.py --base origin/main --check --full`. Prune a temporary branch only after its exact tip is verified as preserved on a green `main`.

## Scheduled agents

The CI agent, the discovery agent and the reconstruction evaluator run on a schedule in a cloud environment the owner configures; deploying them and issuing their credentials are owner operations. Each of them:

- runs one instance at a time and starts from the full current `main` SHA;
- keeps its checkpoint (reviewed SHA, coverage, deferred work, open PR, integration results) in its PR description (and in task storage where the platform has it), never in a disposable checkout, and advances completed coverage only to work verified on `main`;
- reuses its own branch, merges current `main` into it without force, keeps unexpected branch content, and opens at most one PR;
- stays quiet when nothing changed, with no empty commits or PRs;
- reports integrations, unresolved findings, blocked work, access or validation failures, and anything integrated but unverified; and
- never weakens a check to finish a run, and never reverts or rewrites `main`.

### Drive inventory

Digital copies of printed works are kept on Google Drive as primary sources. A separate scheduled agent maintains the inventory Doc of those evidence folders, so analysis agents can find their sources. It never writes to Git. The sources never enter Git; analyses cite them through their recorded provenance.

## Never, without a separately reviewed owner amendment

Never add raw acquisition evidence, source media, private migration evidence, credentials, unreviewed binaries, symlinks, submodules, or hooks.

The approved workflows are the content-read-only `.github/workflows/repository-audit.yml` with its isolated status-only reporter, the default-branch, exact-output-allowlisted `.github/workflows/global-index-housekeeping.yml`, and the owner-dispatched bulk-merge workflow `.github/workflows/nightly-integration.yml` under `governance/policies/NIGHTLY_ANALYTICAL_INTEGRATION.md`. The CI agent runs the same merge gate outside Actions. Scheduled workflow apply is prohibited. Every other workflow remains prohibited without a separately reviewed owner amendment.

## License

Original content is covered only by the narrow CC BY-NC 4.0 scope in `LICENSE.md`. Third-party exclusions are described in `THIRD_PARTY_NOTICES.md`. The license grants no upstream contribution or write authority.
