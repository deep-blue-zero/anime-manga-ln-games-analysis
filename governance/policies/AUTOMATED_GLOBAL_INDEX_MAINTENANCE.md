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

For an existing registered root, commit analysis to its stable branch. If the change does not alter series/study routing, no routing descriptor or global routing edit is required. Author preflight runs first; housekeeping confirms that routing projections are current and performs no commit when they are unchanged. A branch created at `main` with no named analytical root is also a no-op; its name alone does not require a descriptor.

New character discoveries may wait for the curation agent's next review of `main`. Existing character references and generated output must remain valid. Changes that break them require the coordinated agent repair described in `CHARACTER_DISCOVERY_MAINTENANCE.md` before source integration.

## Declarative routing inputs

For new or changed routing, provide a complete desired row in the named analytical root:

- `series/<stable-slug>/.repository/series-registry.json`;
- `studies/<stable-slug>/.repository/study-registry.json`.

Each input is one JSON object whose ID, `stable_slug`, and `repository_path` match the branch slug exactly. Only deterministic upsert or replacement is authorized; automatic deletion remains prohibited. A new root needs a tracked current-eligible entrypoint with the complete authority quartet documented in `../../characters/README.md`. A noncurrent draft cannot serve as that entrypoint.

Character-upsert files are retired as synchronization inputs. Existing `.repository/character-registry-upserts.jsonl` files are preserved as historical proposals or optional leads for independent agent review. They are neither required nor applied, and cannot overwrite curated character metadata.

## Execution and failure behavior

1. On stable analytical push events, `.github/workflows/repository-audit.yml` validates authored content against an in-memory projection of exactly the five routing outputs. All source, character, link, schema, authority, identity, and publication checks remain applicable. If projected routing differs from the committed bytes, the job passes author preflight but publishes a pending `Repository integration audit` status with `AWAITING_SYNCHRONIZATION` in the log. It does not certify integration readiness or write files.
2. Only after successful author preflight does housekeeping verify the actor, branch form, exact remote head, current-`main` ancestry, and complete branch path boundary.
3. The branch may contain its named analytical root, the five housekeeping outputs, and an agent-authored two-file character repair for coordinated integration. Admitting those character files in the branch is not write authority for housekeeping.
4. Housekeeping reads routing descriptors, updates series/study registries, regenerates their navigation, and stages only the five allowlisted outputs.
5. If no output changed and the source audit passed, it exits without a commit.
6. If routing outputs changed, it runs the full staged-snapshot gate, including unchanged character validation, creates one child commit, rechecks the remote branch head, and pushes normally to that same stable branch.
7. Because repository-token pushes do not recursively start ordinary push workflows, it dispatches a separate full read-only audit bound to the generated commit SHA. This audit never uses routing preflight. Its isolated reporter publishes `Repository integration audit` on that actual SHA, even though GitHub associates the dispatch run's default metadata with `main`. Integrate only the final head with that successful status and completed housekeeping.

Stale routing alone is pending synchronization, not a failed authored-content check. An actual author-preflight failure stops housekeeping; character errors and other failures must not be bypassed or repaired by it. If staged validation fails, it stops without committing the generated changes.

Queued runs superseded by a newer branch head exit successfully with a notice and no publication. If the branch or `main` advances before publication, preserve the newer work and reconcile/revalidate the final head; a no-op is not validation of that newer commit. Use ordinary non-forced pushes and inspect ambiguous push results before retrying. An analytical branch behind current `main` must incorporate it before housekeeping can finalize the branch.

The audit's validation job has `contents: read` only. Its separate, fixed reporter has `statuses: write` only, never checks out or executes repository code, and can report only the exact audited SHA in the single `Repository integration audit` context. Missing, pending, failed, cancelled, or skipped results are not integration approval. Inspect the actual status target and audited SHA; the Actions list's displayed default-branch commit is insufficient.

The workflow token has `contents: write` only. It has no secret, artifact, issue, pull-request, release, tag, `main`, force-push, or branch-management authority. Its author is the approved owner identity and its committer is exact `GitHub <noreply@github.com>`.
