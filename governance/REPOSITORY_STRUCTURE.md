# Repository structure

```text
README.md
LICENSE.md
THIRD_PARTY_NOTICES.md
CHARACTER_ANALYSIS_INDEX.md
characters/
  registry/
    <namespace>.jsonl
  index/
    <namespace>.md
  RECONSTRUCTION_CAPABILITY_SPEC.md
  reconstruction_capabilities.jsonl
  CHARACTER_RECONSTRUCTION_INDEX.md
governance/
  AGENT_ROUTING.md
  MANGA_ANIME_CORPUS_INDEX.md
  analytical-methods/
  policies/
  repository-controls/
  schemas/
  archive/
    migration/
crosswalk/
  drive-to-git.jsonl
  materialization-results.jsonl
  path-plan.jsonl
provenance/
  drive-artifacts/
    DRIVE_ARTIFACT_REFERENCE_INDEX.md
series/
  registry.json
  <stable-slug>/
studies/
  registry.json
  <stable-slug>/
tools/
  tests/
```

`governance/analytical-methods/` is the canonical home for reusable corpus-level analytical reference methods. These opt-in references are not automatically project-local governing methods.

The partitions `characters/registry/<namespace>.jsonl` hold discovery metadata only, one partition per character ID namespace; `CHARACTER_ANALYSIS_INDEX.md` and the namespace pages `characters/index/<namespace>.md` are generated from them (`characters/README.md` specifies the layout). Substantive character monographs belong in the canonical series or study tree. Reconstruction capability assessments use `characters/reconstruction_capabilities.jsonl` and its generated `characters/CHARACTER_RECONSTRUCTION_INDEX.md`, written only by the reconstruction evaluator; neither holds analytical prose. Series-local reconstruction manifests and empty symmetry folders are not required.

Stable slugs use the best-known English or official Latin-script title, lowercase ASCII, and hyphens. A Japanese-script Drive directory is not mechanically transliterated when an established title exists. Slugs are owner-reviewed and remain stable after publication; alternate titles belong in metadata.

The approved clarification slug is `the-idolmaster-cinderella-girls-2015-anime`.

The first integrated series candidate was `series/the-idolmaster-cinderella-girls-u149/`. `main` is the analytical authority; Drive retains only its declared native-authoring and reference roles. The migration records are archived in `governance/archive/migration/`.
