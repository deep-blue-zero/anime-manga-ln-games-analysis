# Character Index v2 Backfill Audit

> This is an owner-review candidate set, not a registry mutation. No character record was added, inferred from incidental prose, or promoted without authority qualification.

## Scope and method

The audit examined every repository Markdown artifact under `series/` and `studies/` after the final G7 stale-disposition repair. It selected dedicated character-analysis filenames and series-level character-model readiness indexes, reconciled them against all evidence paths already cited by `characters/registry.jsonl`, and evaluated them with the repository's machine-readable supersession authority graph.

The machine-readable candidate set contains 96 rows and has SHA-256 `3f0f024452aa8124b622700d4060d197040f2ea1f0231cd0194a56aa6bebb126`.

## Results

| Disposition | Count | Meaning |
|---|---:|---|
| `ALREADY_REGISTERED` | 16 | Already represented by at least one reviewed registry record. |
| `READY_FOR_OWNER_REGISTRY_REVIEW` | 47 | Current-eligible evidence; owner must confirm identity, continuity, coverage, aliases, and inclusion basis. |
| `BLOCKED_AUTHORITY_METADATA` | 23 | Potential evidence exists, but its authority quartet/status requires explicit repair or adjudication. |
| `EXCLUDED_NONCURRENT_AUTHORITY` | 10 | Explicit legacy path or recognized noncurrent authority state. |

## Ready-for-review scopes

| Scope | Candidate artifacts/indexes |
|---|---:|
| `86-eighty-six` | 16 |
| `a-sisters-all-you-need` | 2 |
| `attack-on-titan` | 1 |
| `azur-lane` | 5 |
| `kimishinu` | 3 |
| `my-hero-academia` | 1 |
| `one-punch-man` | 1 |
| `oreimo` | 1 |
| `shine-post` | 6 |
| `shokugeki-no-soma` | 1 |
| `solo-leveling` | 6 |
| `sound-euphonium` | 1 |
| `the-idolmaster-cinderella-girls-mobile-games` | 3 |

## Blocked scopes

| Scope | Blocked artifacts/indexes |
|---|---:|
| `idoly-pride` | 8 |
| `my-hero-academia` | 2 |
| `oregairu` | 8 |
| `sound-euphonium` | 4 |
| `youjo-senki` | 1 |

## Owner-review contract

A `READY_FOR_OWNER_REGISTRY_REVIEW` row is evidence that a registration decision is now possible; it is not an instruction to add a record. Before adding any record, the owner or a later authorized curation pass must confirm the entity/subject split, stable IDs, continuity, entity- versus subject-scoped aliases, analytical dimensions, evidence anchors, coverage limits, review state, and inclusion basis. Distributed-corpus rows require an explicit character selection and must not be expanded by name matching alone.

Blocked rows remain fail-safe noncurrent evidence until their authority metadata is explicitly adjudicated. Explicit legacy/superseded rows are excluded from current-evidence qualification. This audit intentionally leaves `characters/registry.jsonl` and generated discovery artifacts unchanged.
