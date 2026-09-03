# PACTRIH Ethical Topology

This study root is reserved for the PACTRIH ethical-topology framework, its methodology, canonical machine-readable data, generated interactive artifacts, build/validation tooling, and audit material.

## Intended layout

- `methodology/` — framework definitions, scoring rubrics, self-report instrument specifications, and methodological notes.
- `data/` — canonical machine-readable datasets and schemas. The numerical dataset should be the source of truth for generated atlas artifacts.
- `interactive/` — generated human-facing interactive deliverables such as the atlas and self-report survey.
- `scripts/` — deterministic generation, validation, and analysis tooling.
- `audits/` — manifests, validation reports, and reproducibility checks.
- `CHANGELOG.md` — study-level version and milestone history.

No CSV dataset or HTML interactive artifact is materialized in this scaffold commit. Those should be added only when the canonical source files and generation/validation workflow are ready.

## Authority and versioning

The stable study path is `studies/pactrih-ethical-topology/`. Individual artifacts should use stable filenames and carry their own internal version metadata where needed; Git history and milestone tags should preserve longitudinal state rather than proliferating version-numbered filenames.

The canonical numerical dataset and the self-report instrument are related but independently versioned. Changes to one do not imply a version change to the other.
