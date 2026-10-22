# Automated global index maintenance

Housekeeping (`.github/workflows/global-index-housekeeping.yml`) keeps series/study routing current so analysis authors never edit it by hand. It writes only these five generated files:

- `series/registry.json`
- `studies/registry.json`
- `series/README.md`
- `studies/README.md`
- `governance/MANGA_ANIME_CORPUS_INDEX.md`

Everything else is read-only to it, including the character registry and index (maintained under `CHARACTER_DISCOVERY_MAINTENANCE.md`) and the reconstruction outputs (maintained under `CHARACTER_RECONSTRUCTION_MAINTENANCE.md`).

## How a push is certified

The repository audit of a `series/` or `studies/` push validates the authored content against a projection of the five routing outputs, and confines the branch to its own root, those outputs and a separately identifiable two-file character repair. If the committed routing outputs already match the projection, the audit reports success on that exact commit. Otherwise it reports pending, and housekeeping regenerates the outputs on a branch that contains current `main`, pushes one ordinary child commit, and dispatches the audit for that commit. Housekeeping never pushes `main`, force-pushes, writes analysis, deletes registry rows or touches character files.

## Declaring routing

A change that does not alter routing needs no descriptor. For a new or changed root, commit one complete row in the named root:

- `series/<stable-slug>/.repository/series-registry.json`, or
- `studies/<stable-slug>/.repository/study-registry.json`.

Its ID, `stable_slug` and `repository_path` match the branch slug exactly. A new substantive root, or a project entering a material analytical restart, also declares `project_initiation_gate: REQUIRED`. A new root needs a tracked current-eligible entrypoint with the authority quartet documented in `../../characters/README.md`, exposing the initialization state required by `MANGA_ANIME_PROJECT_INITIATION_AND_ARCHITECTURE_POLICY.md` (CLOSED by default, OPEN only once the gate is satisfied). A noncurrent draft cannot serve as that entrypoint. Rows are upserted or replaced, never deleted automatically.

An optional `catalog_note` describes the project (its scope, medium or analytical focus), never its progress: housekeeping copies it into four files, so progress text goes stale and makes a new child commit on every push. Current progress belongs in the project's entrypoint.

Retired `.repository/character-registry-upserts.jsonl` files are kept only as optional leads for the curation agent and are never applied.
