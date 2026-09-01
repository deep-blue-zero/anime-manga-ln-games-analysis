# Manga and Anime Corpus Index

> Repository state: public; G3 closed; G4 representative pilots in progress; U149, the partial IDOLY PRIDE P02 ledger, and the partial DJFW P03 control-state slice are materialized candidates. The P04 archive control is reference-only.
>
> Analytical authority: Google Drive until a separately approved and verified G8 cutover. Git content remains a nonauthoritative migration candidate.

This is the Git-side candidate navigation index derived from the historical Drive index. It does not become the analytical authority merely because the repository is public. Later materialization must preserve the Drive source identity and pre-image in private evidence, document every path rewrite, and replace Drive links with verified repository-relative targets only when an equivalent Git object exists.

## Series

See `../series/registry.json`.

- [THE IDOLM@STER CINDERELLA GIRLS U149](../series/the-idolmaster-cinderella-girls-u149/V1%20Analysis/00_README_AND_CORPUS_MAP.md) — episode readings, a YonaiP character monograph, full-series synthesis, manifest, and historical conversation provenance.
- [IDOLY PRIDE — source-to-bundle provenance ledger](../series/idoly-pride/V2%20Analysis/02%20Source%20Audits%20and%20Longitudinal%20Ledgers/02.01%20Corpus%20Coverage%20and%20Priority%20Ledger/IDOLY_PRIDE_V2_SOURCE_TO_BUNDLE_PROVENANCE.csv) — one byte-preserved, machine-readable P02 pilot artifact. This is a partial slice, not a complete IDOLY PRIDE migration; internal relative paths do not imply that their targets are present in Git.

## Studies

- [Doujinshi/Fanwork Comparative Taxonomy — current state and corpus map](../studies/doujinshi-fanwork-comparative-taxonomy/DJFW_CURRENT_STATE_AND_CORPUS_MAP.md) — partial P03 control-state pilot containing one corpus map and [17 TSV worksheet projections with a structure manifest](../studies/doujinshi-fanwork-comparative-taxonomy/01%20Project%20Registry%20and%20Source%20Lock/DJFW_PROJECT_CONTROL_SHEET.structure.json). The native XLSX remains `REFERENCE_DRIVE`.

This is not a complete DJFW study migration. Names of absent sibling documents inside the corpus map remain unlinked source context and do not claim that those artifacts are present in Git.

## Reference-only artifacts

The G4 P04 ZIP/reference control records six hash-verified Gakuen Idolmaster ZIP identities in sanitized provenance and crosswalk metadata. All six have no Git destination. No ZIP bytes or Gakuen Idolmaster analysis tree are tracked, and archive membership does not imply that any member is available in Git. See the [Drive Artifact Reference Index](../provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md#p04-zipreference-boundary).
