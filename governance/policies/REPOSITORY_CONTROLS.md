# Repository controls

The public, owner-maintained repository and its pre-G8 hardening candidate use these controls:

- GitHub repository ID `1352620662`, owned by `deep-blue-zero`, with verified G3 public-visibility activation evidence recorded in `../repository-controls/public-activation-bindings.json`;
- current visibility state of public, with `deep-blue-zero` as the sole upstream human writer and contributor;
- policy prohibits external pull-request merge, patch import, cherry-pick, non-owner collaborator, or pending invitation; G3 closure found none, and current provider state requires reread before any later public push;
- provider interfaces may permit issues, discussions, or pull-request proposals, but none confer upstream authority;
- the sole tracked automation is the read-only, non-mutating repository-content audit at `.github/workflows/repository-audit.yml`; every other workflow remains forbidden without separate review;
- default branch `main`;
- administrator-enforced `main` protection with linear history and force-push and branch deletion disabled, verified at G3 closure and requiring provider reread before every later public push;
- an active `refs/tags/activation/**` ruleset blocking deletion and non-fast-forward updates, verified at G3 closure and requiring provider reread before use;
- repository-local `core.longpaths=true`, `core.autocrlf=false`, and `core.safecrlf=true`;
- imported bytes are `-text` by default; generated controls are explicitly `text eol=lf`;
- exact-path staging from an approved manifest; wildcard staging and `git add .` are prohibited;
- tracked-path, Unicode/case collision, size, binary, secret, symlink, submodule, JSON, JSONL, and generated-index checks, with reviewed large text admitted only by an exact path/byte-length/SHA-256 tuple;
- the audit workflow uses no reusable Actions, receives no secret, installs only version- and hash-locked validation dependencies, and has read-only contents permission; hooks and write-capable automation remain prohibited;
- GitHub bootstrap initializers remain disabled; the reviewed repository artifacts are the sole first-commit source;
- complete-history publication checks for credentials, personal email, local absolute paths, Drive URLs, excluded content, and non-owner commit identities;
- clean, full, non-shallow clone verification before corpus content; and
- historical G3 validation against commit `e934c0a6f92ad16ba3305bd99f938aa6b3d97a1f` and tree `d0bb00fa5d7a8735892921ba3c0023b4855ac52e`, plus separate current-policy and optional manifest-bound validation for later candidates;
- immutable preservation of `bootstrap-bindings.json` and `G3_BOOTSTRAP_TRACKED_PATHS.txt` as historical private-bootstrap evidence; and
- current migration state of completed G3, G4 representative pilots, completed Character Index v2 hardening, and an integrated U149 first-tranche candidate.

Repository creation and public visibility did not activate Git analytical authority. Google Drive remains authoritative until separately approved and verified G8 activation. Each coherent recurring tranche requires one prior, SHA-256-bound owner approval package under `RECURRING_TRANCHE_PROCESS.md`; that package may authorize transformation through ordinary non-forced push and verification without repeated intermediate approvals. Exact-path staging, committed-blob and complete-history audit, live provider and remote reread, CI, and the fail-closed authority boundary remain mandatory. Original-content licensing is CC BY-NC 4.0 under the narrow root license scope.

The only current named large-text exception is the Idoly Pride source-to-bundle provenance CSV recorded in `tracked-file-policy.json`. Its existing UTF-8 BOM and carriage returns are tolerated only when the path, 1,377,633-byte length, and SHA-256 `7dde60c452627a694307dda68abfb0d4d434ec1c2ce934bf85a0b81db483c366` all match. Any drift revokes every part of that exception; secret, publication-hazard, NUL, and strict UTF-8 validation always remain active.

The CI Git-whitespace command checks every changed path except that one exact CSV through a top-anchored literal exclusion pathspec. No directory, wildcard, second path, or other named-text artifact is excluded. This narrow compatibility rule preserves the approved source bytes while the repository validator independently enforces their exact tuple and every non-whitespace publication control.
