# Character discovery maintenance

The character discovery agent keeps `characters/registry.jsonl` and its generated view `CHARACTER_ANALYSIS_INDEX.md` current, so any agent can tell whether a character is written about in the repository without scanning every project. It follows the shared rules for scheduled agents in `AGENTS.md`.

## What it writes

Only those two files. The registry is curated; the index is produced only by `tools/generate_character_index.py` and never authored by hand. The agent never edits analytical prose, evidence or authority metadata, schemas, tools, workflows, other registries, the reconstruction outputs, or Drive files. It preserves unrelated records, including study-based entries. Deleting a record or moving an identity between series is an owner decision.

## Each run

1. Start from the full current `main` SHA. Review tracked analytical files under `series/` and `studies/` that were added, changed, renamed or deleted since the last completed review. Track coverage per root: a checkpoint from before `studies/` was in scope covers `series/` only, so review `studies/` from a documented baseline (the whole tree when none exists) until it catches up. Unmerged evidence is never effective.
2. Enroll or revise a record only for substantial, reviewed, dedicated or distributed analysis whose current evidence supports every claimed dimension, identity, alias, anchor and coverage range. Mentions, cast lists and filenames are not enough. Defer anything ambiguous without inventing metadata or repairing the source. Reassess affected existing records and keep deferred candidates for the next run.
3. Work on the reusable `character-registry` branch with at most one open PR. Merge current `main` into it without force. Stage the registry, run `python tools/generate_character_index.py --snapshot index`, stage the index, and run `python tools/prepare_commit.py --base origin/main --check`.
4. Push and open or update the PR. The repository audit confines this branch to the two files. The CI agent merges it under `NIGHTLY_ANALYTICAL_INTEGRATION.md`.

Structural checks cannot establish that an interpretation is correct; only evidence-supported changes are enrolled.

## Lag and broken references

Discovery may lag: new analysis merges without immediate enrollment, and the registry is not presumed exhaustive. Validation stays strict, though. If an analysis change would break an existing record's path, anchor, authority relationship, coverage claim or index digest, it cannot merge until the two character files are repaired in a separately identifiable commit on that analysis branch. The discovery agent makes repairs that need curation judgment. The CI agent may make a purely mechanical one, such as following a renamed path or regenerating the index. Otherwise it adds the `character-repair` label and a comment naming the record. Each run, the discovery agent repairs labeled PRs first, then removes the label and comments what it changed. If the repair needs an owner decision, it comments the question and leaves the label. Never weaken a check to wait for the next run.

Historical character-record fixtures in the tests describe an immutable checkpoint, not a freeze on the live registry.

## Related agents and inputs

The reconstruction evaluator derives its work from integrated Git state, so discovery changes never wait on reconstruction; an affected assessment becomes effectively stale and the evaluator reconciles it. Either agent may note leads for the other in its PR description; leads are unverified hints, never authority to enroll or assess.

`series/<stable-slug>/.repository/character-registry-upserts.jsonl` files are retired. They may be read as optional leads and are never applied.
