# Repository controls

The binding forms of these controls are `tools/validate_repository.py` and `../repository-controls/tracked-file-policy.json`. This page explains what they protect; where it differs from them, they win.

## Ownership and automation

`deep-blue-zero` is the sole upstream writer; see `PUBLICATION_AND_CONTRIBUTION_POLICY.md` for upstream authority, provider controls and the three approved workflows. Agents act through owner identities, merge only through the gate in `NIGHTLY_ANALYTICAL_INTEGRATION.md`, and leave guardrail paths to the owner.

## What every audit checks

- Tracked paths enumerated directly from the Git tree or index, with Unicode/case collisions, size, binary, secret, symlink, submodule, JSON/JSONL and generated-index checks.
- Commit identities against the approved author and committer lists.
- Publication safety over the candidate and its reachable history: credentials, personal email, local absolute paths, Drive URLs, excluded content and non-owner commits.
- Markdown links, registered-root topology, project-initiation and closure seals, and character and reconstruction validation.
- Closure across the frozen migration ledgers (`crosswalk/drive-to-git.jsonl`, `materialization-results.jsonl`, `path-plan.jsonl`), bound to the archived migration baseline.
- Native-sheet structure manifests: Draft 2020-12 schema validation plus contiguous ordinals, unique names, declared shapes, exact `.tabs/` containment, rectangular UTF-8/LF TSVs and committed-byte hashes.
- Workflow permissions and triggers.

The Git tree or staged index is the only live path inventory; there is no separate path list.

## Local Git settings and staging

Use repository-local `core.longpaths=true`, `core.autocrlf=false` and `core.safecrlf=true`. Imported bytes are `-text` by default; generated controls are `text eol=lf`. Stage exact paths only; `git add .` and wildcard staging are prohibited.

## Exceptions

**Large text.** Six reviewed text files over 1 MiB are admitted, each by an exact path, byte length and SHA-256 tuple in `named_text_exceptions`. `ARTIFACT_ELIGIBILITY.md` gives each one's purpose. Any drift revokes the exception; secret, publication-hazard, NUL and strict UTF-8 checks always apply.

**Whitespace.** The CI whitespace check covers every changed non-Markdown path except the IDOLY PRIDE provenance CSV. Markdown is excluded because CommonMark uses two trailing spaces as a hard break. The validator binds that exact command shape. Two `.gitattributes` rules, both bound by the validator, exist:

- `"studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and Source Lock/DJFW_PROJECT_CONTROL_SHEET.tabs/*.tsv" whitespace=-blank-at-eol`: in those 17 rectangular TSV projections a terminal tab encodes a required empty final cell.
- `"series/genshin-impact/05 Character Monographs/GENSHIN_FURINA_CHARACTER_MONOGRAPH.md" whitespace=-blank-at-eol`: preserves intentional CommonMark hard breaks, bound to the file's exact reviewed bytes.

Nested `.gitattributes` files and any broader whitespace waiver are prohibited.

## History

The archived records in `../archive/migration/` hold the G3 public-visibility activation, the G3 bootstrap bindings (immutable, hash-protected) and the epoch-1 authority activation. `tools/validate_repository.py --phase g3` can still re-validate the bound G3 bootstrap commit.
