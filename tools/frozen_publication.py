"""Exact, owner-merged bindings for retrospective noncurrent publication.

This does not authorize source admission. Only grants already on fetched main
can distinguish their byte-bound publication files from new sequential work.
"""

from __future__ import annotations

import hashlib
import re
from typing import Any, Mapping

from character_index_core import (
    DomainError, GitSnapshot, _restricted_yaml_load, decode_json,
    validate_repository_path,
)


CONTROL = "governance/repository-controls/project-initiation-gate.json"
FIELD = "frozen_generation_publications"


def publication_grants(control: Mapping[str, Any]) -> tuple[dict, list[str]]:
    raw = control.get(FIELD, {})
    if not isinstance(raw, dict):
        return {}, [f"{CONTROL}.{FIELD} must be an object"]
    errors = []
    for manifest, grant in raw.items():
        label = f"{CONTROL}.{FIELD}[{manifest!r}]"
        try:
            validate_repository_path(manifest)
            if not isinstance(grant, dict):
                raise DomainError("grant must be an object")
            root = grant.get("project_root")
            if not isinstance(root, str) or not re.fullmatch(r"(?:series|studies)/[a-z0-9][a-z0-9-]*/", root):
                raise DomainError("invalid project root")
            entrypoint = grant.get("canonical_entrypoint")
            validate_repository_path(entrypoint)
            if not entrypoint.startswith(root):
                raise DomainError("entrypoint outside project")
            scopes = grant.get("scope_prefixes")
            if not isinstance(scopes, list) or not scopes or len(scopes) != len(set(scopes)):
                raise DomainError("distinct publication scope prefixes required")
            for scope in scopes:
                if not isinstance(scope, str) or not scope.endswith("/") or not scope.startswith(root) or scope == root:
                    raise DomainError("publication scope must be strictly below project root")
                validate_repository_path(scope[:-1])
                if entrypoint.startswith(scope) or any(other != scope and other.startswith(scope) for other in scopes):
                    raise DomainError("publication scopes overlap each other or the current entrypoint")
            for path in (manifest, grant.get("source_boundary")):
                validate_repository_path(path)
                if not any(path.startswith(scope) for scope in scopes):
                    raise DomainError("manifest/source boundary outside publication scope")
            for field in ("manifest_sha256", "source_boundary_sha256"):
                if not isinstance(grant.get(field), str) or not re.fullmatch(r"[0-9a-f]{64}", grant[field]):
                    raise DomainError(f"invalid {field}")
            for field in ("frozen_commit", "frozen_corpus_tree", "comparison_commit", "comparison_v1_boundary"):
                if not isinstance(grant.get(field), str) or not re.fullmatch(r"[0-9a-f]{40}", grant[field]):
                    raise DomainError(f"invalid {field}")
            generations = grant.get("generations")
            if not isinstance(generations, list) or not generations or any(not isinstance(g, str) or not g.strip() for g in generations) or len(generations) != len(set(generations)):
                raise DomainError("distinct nonempty generation identities required")
            for field in ("authorization", "manifest_schema"):
                if not isinstance(grant.get(field), str) or not grant[field].strip():
                    raise DomainError(f"missing {field}")
            provenance = grant.get("provenance_files")
            if not isinstance(provenance, dict):
                raise DomainError("provenance_files must be an object")
            for path, digest in provenance.items():
                validate_repository_path(path)
                if path == manifest or not any(path.startswith(scope) for scope in scopes) or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                    raise DomainError("invalid provenance file binding")
        except (DomainError, TypeError, ValueError) as exc:
            errors.append(f"{label}: {exc}")
    return ({} if errors else raw), errors


def _noncurrent(data: bytes, path: str, generations: list[str]) -> None:
    if path.endswith(".md"):
        text = data.decode("utf-8", "strict")
        parts = text.split("---", 2)
        if not text.startswith("---\n") or len(parts) != 3:
            raise DomainError(f"{path}: noncurrent publication front matter missing")
        metadata = _restricted_yaml_load(parts[1], path)
    else:
        metadata = decode_json(data, path)
    if (not isinstance(metadata, Mapping) or metadata.get("status") != "draft_noncurrent"
            or metadata.get("do_not_use_as_current_authority") is not True
            or metadata.get("supersedes") != [] or metadata.get("superseded_by") != []
            or metadata.get("generation") not in generations):
        raise DomainError(f"{path}: reviewed publication must remain noncurrent and generation-qualified")


def frozen_publication_paths(
    snapshot: GitSnapshot, main_commit: str, candidate_control: Mapping[str, Any],
    routes: Mapping[str, str],
) -> tuple[dict[str, set[str]], list[str]]:
    """Verify complete publication envelopes against grants already on main.

    The original commits need not be public ancestors: the owner first reviews
    their immutable identities and original/derivative mapping, then merges its
    exact manifest binding. No candidate-side grant can authorize itself.
    `main_commit` is main before the candidate: a post-integration audit of
    main itself passes its first parent, so a published grant stays bound.
    """
    accepted: dict[str, set[str]] = {}
    errors: list[str] = []
    try:
        main = GitSnapshot.from_commit(snapshot.root, main_commit, paths=(CONTROL,))
        control_entry = main.get(CONTROL)
        if control_entry is None:
            return accepted, []
        if not control_entry.qualifies_as_evidence:
            raise DomainError("main publication control is not regular")
        control = decode_json(control_entry.data, CONTROL)
        if not isinstance(control, Mapping):
            raise DomainError("main publication control is not an object")
        grants, malformed = publication_grants(control)
        errors.extend(malformed)
        if not grants:
            return accepted, errors
        main_manifests = GitSnapshot.from_commit(snapshot.root, main_commit, paths=grants)
        for manifest_path, grant in grants.items():
            root = grant["project_root"]
            label = f"{manifest_path}: frozen publication"
            try:
                published = main_manifests.get(manifest_path) is not None
                envelope = {p for p in snapshot.entries if any(p.startswith(s) for s in grant["scope_prefixes"])}
                if not envelope and not published:
                    # Reviewed grant is inert until publication. Its route binds
                    # once prior main publishes it or a candidate carries its
                    # envelope, so dropping or rerouting the root never escapes it.
                    continue
                if routes.get(root) != grant["canonical_entrypoint"]:
                    raise DomainError("registered canonical route differs from reviewed grant")
                if candidate_control.get(FIELD, {}).get(manifest_path) != grant:
                    raise DomainError("a publication grant cannot be removed or rewritten during or after import")
                manifest = snapshot.get(manifest_path)
                if manifest is None or not manifest.qualifies_as_evidence or hashlib.sha256(manifest.data).hexdigest() != grant["manifest_sha256"]:
                    raise DomainError("reviewed publication manifest missing, nonregular or changed")
                payload = decode_json(manifest.data, manifest_path)
                if not isinstance(payload, Mapping):
                    raise DomainError("publication manifest is not an object")
                _noncurrent(manifest.data, manifest_path, grant["generations"])
                identities = {
                    "schema": grant["manifest_schema"],
                    "independent_frozen_commit": grant["frozen_commit"],
                    "independent_frozen_corpus_tree": grant["frozen_corpus_tree"],
                    "original_comparison_commit": grant["comparison_commit"],
                    "comparison_V1_boundary_commit": grant["comparison_v1_boundary"],
                    "unchanged_source_boundary_sha256": grant["source_boundary_sha256"],
                }
                if any(payload.get(k) != value for k, value in identities.items()):
                    raise DomainError("immutable identity/source boundary differs from reviewed grant")
                artifacts = payload.get("artifacts")
                if not isinstance(artifacts, list) or not artifacts:
                    raise DomainError("complete original/publication digest mapping required")
                bindings = dict(grant["provenance_files"])
                for artifact in artifacts:
                    if not isinstance(artifact, dict):
                        raise DomainError("invalid artifact mapping")
                    path = artifact.get("path")
                    validate_repository_path(path)
                    if path in bindings or path == manifest_path or not any(path.startswith(s) for s in grant["scope_prefixes"]):
                        raise DomainError("duplicate or out-of-scope publication artifact")
                    if artifact.get("original_commit") not in (grant["frozen_commit"], grant["comparison_commit"]):
                        raise DomainError("artifact names an unreviewed original commit")
                    for key, size in (("original_blob", 40), ("original_sha256", 64), ("publication_sha256", 64)):
                        if not isinstance(artifact.get(key), str) or not re.fullmatch(r"[0-9a-f]{" + str(size) + "}", artifact[key]):
                            raise DomainError(f"invalid {key}")
                    for key in ("original_bytes", "publication_bytes"):
                        if type(artifact.get(key)) is not int or artifact[key] < 0:
                            raise DomainError(f"invalid {key}")
                    entry = snapshot.get(path)
                    if entry is None or len(entry.data) != artifact["publication_bytes"]:
                        raise DomainError(f"{path}: publication byte count changed")
                    bindings[path] = artifact["publication_sha256"]
                if envelope != set(bindings) | {manifest_path}:
                    raise DomainError("publication envelope has added or missing files")
                boundary = snapshot.get(grant["source_boundary"])
                if boundary is None or hashlib.sha256(boundary.data).hexdigest() != grant["source_boundary_sha256"]:
                    raise DomainError("source boundary missing or changed")
                for path, digest in bindings.items():
                    entry = snapshot.get(path)
                    if entry is None or not entry.qualifies_as_evidence or hashlib.sha256(entry.data).hexdigest() != digest:
                        raise DomainError(f"{path}: frozen publication bytes missing, nonregular or changed")
                    if path.endswith(".md"):
                        _noncurrent(entry.data, path, grant["generations"])
                accepted.setdefault(root, set()).update(bindings)
            except (DomainError, TypeError, ValueError, UnicodeDecodeError) as exc:
                errors.append(f"{label}: {exc}")
    except (DomainError, TypeError, ValueError, UnicodeDecodeError) as exc:
        errors.append(f"frozen publication main binding unavailable: {exc}")
    return accepted, errors
