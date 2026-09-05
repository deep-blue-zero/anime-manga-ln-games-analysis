# Automated global index maintenance

The trusted default-branch workflow `.github/workflows/global-index-housekeeping.yml` maintains deterministic series/study routing for stable `series/<stable-slug>` and `studies/<stable-slug>` branches. It may write only these five exact paths:

- `series/registry.json`
- `studies/registry.json`
- `series/README.md`
- `studies/README.md`
- `governance/MANGA_ANIME_CORPUS_INDEX.md`

Every other path is read-only to housekeeping, including `characters/registry.jsonl` and `CHARACTER_ANALYSIS_INDEX.md`. The character curation agent exclusively maintains those two files under `CHARACTER_DISCOVERY_MAINTENANCE.md`. Housekeeping must not regenerate the character index, normalize the character registry, or apply character upserts.

The machine-readable boundary is `governance/repository-controls/global-index-automation-policy.json`, schema v2. The synchronizer produces only series/study registry outputs. The workflow stages only the five routing outputs, and the repository audit validates this boundary independently.

## Normal analytical change

For an existing registered root, commit analysis to its stable branch. If the change does not alter series/study routing, no routing descriptor or global routing edit is required. The read-only audit runs first; housekeeping confirms that routing projections are current and performs no commit when they are unchanged.

New character discoveries may wait for the curation agent's next review of `main`. Existing character references and generated output must remain valid. Changes that break them require the coordinated agent repair described in `CHARACTER_DISCOVERY_MAINTENANCE.md` before source integration.

## Declarative routing inputs

For new or changed routing, provide a complete desired row in the named analytical root:

- `series/<stable-slug>/.repository/series-registry.json`;
- `studies/<stable-slug>/.repository/study-registry.json`.

Each input is one JSON object whose ID, `stable_slug`, and `repository_path` match the branch slug exactly. Only deterministic upsert or replacement is authorized; automatic deletion remains prohibited.

Character-upsert files are retired as synchronization inputs. Existing `.repository/character-registry-upserts.jsonl` files are preserved as historical proposals or optional leads for independent agent review. They are neither required nor applied, and cannot overwrite curated character metadata.

## Execution and failure behavior

1. `.github/workflows/repository-audit.yml` audits the owner-authored branch commit.
2. After that run completes, housekeeping verifies the actor, branch form, exact remote head, current-`main` ancestry, and complete branch path boundary.
3. The branch may contain its named analytical root, the five housekeeping outputs, and an agent-authored two-file character repair for coordinated integration. Admitting those character files in the branch is not write authority for housekeeping.
4. Housekeeping reads routing descriptors, updates series/study registries, regenerates their navigation, and stages only the five allowlisted outputs.
5. If no output changed and the source audit passed, it exits without a commit.
6. If routing outputs changed, it runs the full staged-snapshot gate, including unchanged character validation, creates one child commit, rechecks the remote branch head, and pushes normally to that same stable branch.
7. Because repository-token pushes do not recursively start ordinary push workflows, it dispatches a separate read-only audit bound to the generated commit SHA. Integrate only the final green head.

A source audit failure caused solely by stale routing projections can be superseded by successful synchronization and the exact generated-commit audit. Character errors and other failures must not be bypassed or repaired by housekeeping. If validation fails, it stops without committing the generated changes.

The workflow token has `contents: write` only. It has no secret, artifact, issue, pull-request, release, tag, `main`, force-push, or branch-management authority. Its author is the approved owner identity and its committer is exact `GitHub <noreply@github.com>`.
