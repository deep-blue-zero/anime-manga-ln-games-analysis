# Repository controls

The G3 bootstrap and publication candidate use these controls:

- GitHub repository owned by `deep-blue-zero`, still private until a separately hash-approved public activation;
- approved target state of public visibility with `deep-blue-zero` as the sole upstream human writer and contributor;
- no external pull-request merge, patch import, cherry-pick, collaborator, or pending invitation;
- default branch `main`;
- after publication, administrator-enforced `main` protection with linear history and force-push and branch deletion disabled;
- after publication, an active `refs/tags/activation/**` ruleset blocking deletion and non-fast-forward updates;
- repository-local `core.longpaths=true`, `core.autocrlf=false`, and `core.safecrlf=true`;
- imported bytes are `-text` by default; generated controls are explicitly `text eol=lf`;
- exact-path staging from an approved manifest; wildcard staging and `git add .` are prohibited;
- tracked-path, Unicode/case collision, size, binary, secret, symlink, submodule, JSON, JSONL, and generated-index checks;
- no workflow or hook is tracked in G3; later automation requires separate review, immutable dependency pinning, and read-only default workflow permissions;
- GitHub bootstrap initializers remain disabled; the reviewed repository artifacts are the sole first-commit source;
- complete-history publication checks for credentials, personal email, local absolute paths, Drive URLs, excluded content, and non-owner commit identities;
- clean, full, non-shallow clone verification before corpus content; and
- independent G3 audit before G4.

Repository creation and publication do not activate Git authority. Google Drive remains authoritative until verified G8 activation. Public visibility requires its own exact activation approval after the final governance commit and complete-history audit are bound.
