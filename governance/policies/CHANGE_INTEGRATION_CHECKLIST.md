# Change integration checklist

This is the mandatory pre-commit contract for human, Codex, and ChatGPT changes to this repository. It complements `AGENTS.md` and the authority records; it does not expand repository, Drive, publication, or contributor authority.

## Before editing

1. Read `AGENTS.md`, `governance/AUTHORITY_STATE.yaml`, `governance/AUTHORITY_SCOPE.json`, and this checklist.
2. Begin from an up-to-date branch based on `origin/main`. Follow `BRANCH_LIFECYCLE.md` for the branch name and eventual pruning.
3. Preserve the owner-only authorship policy, the Git/Drive authority boundary, artifact exclusions, and frozen migration records.
4. Declare the intended paths. Never use `git add .`, wildcard staging, force-push, or history rewriting.

## Change obligations

The machine-readable form of this table is `governance/repository-controls/change-obligations.json`.

| Change | Required synchronization |
| --- | --- |
| Any tracked add, delete, or rename | Regenerate `governance/repository-controls/CURRENT_TRACKED_PATHS.txt` from the final staged index. |
| Add, remove, or reroute a series root | Update `series/registry.json`; regenerate `series/README.md` and the series catalog in `governance/MANGA_ANIME_CORPUS_INDEX.md`. |
| Add, remove, or reroute a study root | Update `studies/registry.json`; regenerate `studies/README.md` and the studies catalog in `governance/MANGA_ANIME_CORPUS_INDEX.md`. |
| Add or change character discovery or qualifying evidence | Update `characters/registry.jsonl`, verify exact-byte evidence hashes and authority eligibility, and regenerate `CHARACTER_ANALYSIS_INDEX.md`. |
| Add or change a Drive-only reference | Update the Drive artifact reference index and verify every referenced anchor. Do not rewrite frozen migration crosswalks. |
| Change policy, schema, validation, workflow, or authority controls | Run the complete test suite and review the governance effect. Authority-scope changes require separate owner authorization. |

Ordinary edits to an existing analytical file do not require unrelated registry churn. A newly added analysis file does change the tracked path set and therefore requires regeneration of `CURRENT_TRACKED_PATHS.txt`.

## Prepare the exact staged snapshot

1. Stage only the declared content, registry, policy, and tool paths by exact pathname.
2. Generate deterministic outputs from that index:

   `python tools/prepare_commit.py --base origin/main --write-generated`

3. Review and stage only the generated files reported by the command.
4. Run the final gate once the worktree and index agree:

   `python tools/prepare_commit.py --base origin/main --check`

The check evaluates the obligation map, exact tracked-path closure, registry-to-directory topology, generated catalogs, character discovery output, publication constraints, authority invariants, and the complete unit-test suite. Do not commit or push on failure.

## Before and after publication

1. Inspect the exact staged path list, diff, generated changes, and file sizes.
2. Confirm the commit uses an approved owner author identity and an approved committer identity.
3. Push normally without force. Confirm the exact remote commit and read-only repository audit pass before treating the change as complete.
4. After integration, apply the verified branch-retention or pruning rule in `BRANCH_LIFECYCLE.md`.

Do not routinely modify `governance/AUTHORITY_SCOPE.json`, authority-epoch records, bootstrap bindings, public-activation bindings, or the frozen Drive-to-Git migration crosswalks.
