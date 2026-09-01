# Repository structure

```text
README.md
CHARACTER_ANALYSIS_INDEX.md
characters/
  registry.jsonl
  RECONSTRUCTION_CAPABILITY_SPEC.md
governance/
  AUTHORITY_STATE.yaml
  AUTHORITY_SCOPE.json
  MANGA_ANIME_CORPUS_INDEX.md
  CHATGPT_AUTHORITY_AND_ROUTING.md
  policies/
  repository-controls/
    public-activation-bindings.json
  schemas/
series/
  registry.json
  <stable-slug>/
studies/
  <stable-slug>/
tools/
  tests/
```

`characters/registry.jsonl` contains discovery metadata only. Substantive character monographs belong in the canonical series or study tree. Future reconstruction assessments, if separately authorized, use `characters/reconstruction_capabilities.jsonl`; that production registry is deliberately absent from this bootstrap-hardening candidate. Series-local reconstruction manifests and empty symmetry folders are not required.

Stable slugs use the best-known English or official Latin-script title, lowercase ASCII, and hyphens. A Japanese-script Drive directory is not mechanically transliterated when an established title exists. Slugs are owner-reviewed and remain stable after publication; alternate titles belong in metadata.

The approved clarification slug is `the-idolmaster-cinderella-girls-2015-anime`.

No title-specific series or study tree has been committed yet. Google Drive remains the analytical authority until separately approved and verified G8 cutover.
