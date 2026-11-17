---
study: PACTRIH_ETHICAL_TOPOLOGY
artifact_type: study_entrypoint
scope: CSV_V12_AND_ATLAS_V3_VERIFIED_IMPORT
generation: V0.2
status: active_provisional
supersedes: []
superseded_by: []
do_not_use_as_current_authority: false
---

# PACTRIH Ethical Topology

This study root holds the PACTRIH ethical-topology framework, canonical machine-readable data, a verified interactive atlas, validation tooling, and audit material. The imported v12/v3 snapshot contains 100 subjects: 85 characters/entities, 7 factions, and 8 historical agents.

## Intended layout

- `methodology/` — framework definitions, scoring rubrics, self-report instrument specifications, and methodological notes.
- `data/` — canonical machine-readable datasets and schemas. The numerical dataset should be the source of truth for generated atlas artifacts.
- `interactive/` — generated human-facing interactive deliverables such as the atlas and self-report survey.
- `scripts/` — deterministic generation, validation, and analysis tooling.
- `audits/` — manifests, validation reports, and reproducibility checks.
- `CHANGELOG.md` — study-level version and milestone history.

## Materialized snapshot

- [Canonical CSV v12](data/pactrih_scores.csv) — all 100 supplied rows, scores, descriptions, classifications, and Unicode labels, unchanged. Only the encoding is converted from UTF-8 BOM/CRLF to repository-required UTF-8/LF; the validator reverses this conversion to verify the original source hash.
- [Interactive Ethical Atlas v3](interactive/atlas.html) — the supplied standalone HTML, unchanged. Download it and open the local file in a modern browser; GitHub's source viewer does not execute it. Initial use needs no server or network. Hosting is outside this import.
- [Source manifest](audits/source_manifest.json) and [import receipt](audits/IMPORT_RECEIPT.md) — versions, hashes, acceptance boundary, checks, and limitations.

This is the supplied historical v12/v3 boundary, not a claim that no later assessments exist. Interpretive scores remain provisional; the import verifies preservation and consistency, not independent evidentiary support for every assessment.

## Validation and future changes

From the repository root, run:

```sh
python studies/pactrih-ethical-topology/scripts/validate_scores.py
python -m unittest discover -s studies/pactrih-ethical-topology/scripts/tests -p 'test_*.py'
```

Python 3.10+ and Node.js are required. The read-only validator checks schema, counts, integer ranges, derived coordinates, exact CSV/HTML identity/order/score/description/unit parity, JavaScript syntax, and source/committed-byte pins and exact reconstruction of the original CSV bytes. Mutation tests demonstrate rejection of stale data and modified derived metadata. The repository's current global audit does not discover study-local tests; run these commands explicitly before every study update.

The CSV is the sole numerical authority for P/A/C/T/R/I/H and ethics-map coordinates. Atlas v3 is a **frozen verified projection**, with supplied PCA coordinates, Ward k=8/10/12 IDs, priority labels, and color mapping retained. The producer's exact PCA/Ward generator and dependency versions are absent, so this import does not claim a CSV-only rebuild. Any baseline edit fails validation, including matching CSV/HTML edits, until a reviewed successor establishes its provenance and metadata. See the [update procedure](scripts/README.md).

## Authority and versioning

The stable study path is `studies/pactrih-ethical-topology/`. Individual artifacts should use stable filenames and carry their own internal version metadata where needed; Git history and milestone tags should preserve longitudinal state rather than proliferating version-numbered filenames.

The canonical numerical dataset and the self-report instrument are related but independently versioned. Changes to one do not imply a version change to the other. The PACTRIH-SR questionnaire and respondent data are outside this import.

P/A/C/T/R/I/H are ordinal estimates on 0..10. High C (normative constraint) and T (transpersonal telos) are morally unsigned; R is moral reflexivity, not goodness. Higher I/H mean greater instrumentality/harm permissiveness. Humane Regard=(P+A)/2 and Moral Structure=(C+T)/2 are visualization aids; there is no aggregate good/evil score. Distances and supplied Ward clusters use raw, equally weighted, unstandardized seven-axis vectors, without reversing I/H. Historical-agent profiles are provisional broad-period agent assessments; faction profiles are group-level assessments. Neither is interchangeable with a fictional individual.
