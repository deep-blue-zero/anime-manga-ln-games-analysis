# Automated global index maintenance

Stable `series/<stable-slug>` and `studies/<stable-slug>` branches may contain only work for their named analytical root. The trusted default-branch workflow `.github/workflows/global-index-housekeeping.yml` reads those trees and may write only these exact global control-plane paths:

- `series/registry.json`
- `studies/registry.json`
- `characters/registry.jsonl`
- `series/README.md`
- `studies/README.md`
- `governance/MANGA_ANIME_CORPUS_INDEX.md`
- `CHARACTER_ANALYSIS_INDEX.md`

Every other path is read-only to the workflow. In particular, it cannot write analytical prose, project-local indexes, evidence, authority records, crosswalks, schemas, policy, tools, workflows, or source metadata. The machine-readable boundary is `governance/repository-controls/global-index-automation-policy.json`.

## Normal analytical change

For an existing registered root, commit the analysis only to its stable branch. If the change does not alter global discovery or routing semantics, no metadata input or global edit is required. The read-only repository audit runs first; housekeeping then confirms that the global projections are already current and performs no commit.

## Declarative inputs for semantic changes

Automation cannot infer titles, media types, identities, continuity, evidence meaning, or authority from prose. Put the relevant complete desired record in the named analytical root:

- new or changed series routing: `series/<stable-slug>/.repository/series-registry.json`;
- new or changed study routing: `studies/<stable-slug>/.repository/study-registry.json`;
- new or changed character discovery records: `series/<stable-slug>/.repository/character-registry-upserts.jsonl`.

The root registry input is one JSON object with the same fields as its desired global registry row. Its ID, `stable_slug`, and `repository_path` must match the branch slug exactly. Each character-upsert line is one complete Character Index v2 record; `series_id` and every evidence path must remain within the branch's named series.

These inputs authorize deterministic upsert or replacement only. Automatic deletion, cross-series evidence ownership, and inferred semantic metadata are prohibited. A registry deletion or identity transfer remains an explicit governance/tooling change.

## Execution and failure behavior

1. `.github/workflows/repository-audit.yml` audits the owner-authored branch commit.
2. After that run completes, the default-branch housekeeping workflow verifies the actor, branch form, remote head, ancestry from current `main`, and complete branch path boundary.
3. It reads any declarative inputs, updates registries, regenerates the human-facing catalogs and character index, and stages only the seven allowlisted outputs.
4. If no output changed and the source audit passed, it exits without a commit.
5. If outputs changed, it runs the full staged-snapshot gate, creates one child commit, rechecks the remote branch head, and performs an ordinary non-forced push to that same stable branch.
6. Because pushes made with the repository token do not recursively start ordinary push workflows, housekeeping dispatches a separate read-only audit bound to the generated commit SHA.

A source commit may receive a transient failed audit when a new root or registry input necessarily makes the old global projection stale. That failure is superseded only when housekeeping succeeds and the dispatched audit of the generated child commit is green. Any other failure stops without a write.

The workflow token has `contents: write` only. The workflow has no secret, artifact, issue, pull-request, release, tag, `main`, force-push, or branch-management authority. Its commit author is the approved owner identity and its committer is exact `GitHub <noreply@github.com>`.
