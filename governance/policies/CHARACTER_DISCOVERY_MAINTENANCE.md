# Character discovery maintenance

The character discovery agent keeps the character registry (the namespace partitions under `characters/registry/`) and its generated view (`CHARACTER_ANALYSIS_INDEX.md` and the namespace pages under `characters/index/`) current, so any agent can tell whether a character is written about in the repository without scanning every project. It follows the shared rules for scheduled agents in `AGENTS.md`.

## What it writes

Only those discovery outputs. The registry partitions are curated; the root index and namespace pages are produced only by `tools/generate_character_index.py` and never authored by hand. The layout is specified in [Registry storage](../../characters/README.md#registry-storage): a row lives in `characters/registry/<namespace>.jsonl` for the namespace of its `character_entity_id`, and a new namespace gets a new partition. Never recreate the retired `characters/registry.jsonl`. The agent never edits analytical prose, evidence or authority metadata, schemas, tools, workflows, other registries, the reconstruction outputs, or Drive files. It preserves unrelated records, including study-based entries. Deleting a record or moving an identity between series is an owner decision.

## Each run

1. Start from the full current `main` SHA. Review tracked analytical files under `series/` and `studies/` that were added, changed, renamed or deleted since the last completed review. Track coverage per root: a checkpoint from before `studies/` was in scope covers `series/` only, so review `studies/` from a documented baseline (the whole tree when none exists) until it catches up. Unmerged evidence is never effective.
2. Enroll or revise a record only for substantial, reviewed, dedicated or distributed analysis whose current evidence supports every claimed dimension, identity, alias, anchor and coverage range. Mentions, cast lists and filenames are not enough. Defer anything ambiguous without inventing metadata or repairing the source. Reassess affected existing records and keep deferred candidates for the next run.
3. Work on the reusable `character-registry` branch with at most one open PR. Merge current `main` into it without force. Add or revise rows in their partitions and run `python tools/character_registry.py normalize`; stage, by exact name, each `registry path to stage` it reports (every registry path whose worktree differs from the index, including rows revised in place and new partitions it did not need to rewrite). Run `python tools/generate_character_index.py --snapshot index`, stage each output path it reports, including removals, and run `python tools/prepare_commit.py --base origin/main --check`.
4. Push and open or update the PR. The repository audit confines this branch to the discovery outputs. The CI agent merges it under `NIGHTLY_ANALYTICAL_INTEGRATION.md`.

Structural checks cannot establish that an interpretation is correct; only evidence-supported changes are enrolled.

## Lag and broken references

Discovery may lag: new analysis merges without immediate enrollment, and the registry is not presumed exhaustive. Validation stays strict, though. If an analysis change would break an existing record's path, anchor, authority relationship, coverage claim or index digest, it cannot merge until the discovery outputs are repaired in a separately identifiable commit on that analysis branch that touches nothing else. The discovery agent makes repairs that need curation judgment. The CI agent may make a purely mechanical one, such as following a renamed path or regenerating the index. Otherwise it adds the `character-repair` label and a comment naming the record. Each run, the discovery agent repairs labeled PRs first, then removes the label and comments what it changed. If the repair needs an owner decision, it comments the question and leaves the label. Never weaken a check to wait for the next run.

Historical character-record fixtures in the tests describe an immutable checkpoint, not a freeze on the live registry.

A branch whose unmerged curation predates the 2026-10-24 partition migration changes the retired single file, so merging `main` would conflict on discovery outputs, and the merge gate rejects any merge that conflicts on them. Carry that curation across without a conflicted merge:

1. Note the branch head `H` and the merge base `B` of `H` and `origin/main`.
2. In a commit touching only discovery outputs, restore them to the merge base: `git checkout B -- characters/registry.jsonl CHARACTER_ANALYSIS_INDEX.md`.
3. Merge `origin/main`; it now applies cleanly and brings the partitions.
4. Run `python tools/character_registry.py replay --base B --head H`. It applies exactly the rows the branch added, revised or removed, and stops before writing if `main` also changed one of those rows; reconcile such a row by hand. Stage each `registry path to stage` it reports, regenerate the index, stage its reported outputs, and commit the discovery outputs as an ordinary curation commit.

Rows deferred only because the single file was full are enrolled through the ordinary evidence checks above.

## Related agents and inputs

The reconstruction evaluator derives its work from integrated Git state, so discovery changes never wait on reconstruction; an affected assessment becomes effectively stale and the evaluator reconciles it. Either agent may note leads for the other in its PR description; leads are unverified hints, never authority to enroll or assess.

`series/<stable-slug>/.repository/character-registry-upserts.jsonl` files are retired. They may be read as optional leads and are never applied.
