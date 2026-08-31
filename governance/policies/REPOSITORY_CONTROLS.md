# Repository controls

The G3 bootstrap uses these controls:

- private owner-only GitHub repository owned by `deep-blue-zero`;
- default branch `main`;
- force-push and branch deletion disabled where supported;
- repository-local `core.longpaths=true`, `core.autocrlf=false`, and `core.safecrlf=true`;
- imported bytes are `-text` by default; generated controls are explicitly `text eol=lf`;
- exact-path staging from an approved manifest; wildcard staging and `git add .` are prohibited;
- tracked-path, Unicode/case collision, size, binary, secret, symlink, submodule, JSON, JSONL, and generated-index checks;
- no workflow or hook is tracked in G3; later automation requires separate review and immutable dependency pinning;
- GitHub bootstrap initializers remain disabled; the reviewed repository artifacts are the sole first-commit source;
- clean, full, non-shallow clone verification before corpus content; and
- independent G3 audit before G4.

Repository creation and bootstrap do not activate Git authority. Visibility must remain private until a separate publication gate is approved.
