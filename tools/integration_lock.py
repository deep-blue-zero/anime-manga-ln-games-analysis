"""Non-expiring, fail-closed shared ownership for the integration executor.

The coordination ref is never deleted, force-updated, stolen or reclaimed by time.
Each transition is a single-parent fast-forward. Contending claims are siblings,
so the Git server can accept only one. An uncertain run leaves ownership held.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import re
import uuid
from pathlib import Path

LOCK_REF = "heads/integration-executor-lock"
LOCK_SCHEMA = "repository-integration-lock/v1"
LOADED_SHA256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


class LockError(RuntimeError):
    """Ownership is busy, uncertain or lost; no further apply is permitted."""


class IntegrationLock:
    def __init__(self, api, *, role, controller_sha, author, committer):
        self.api, self.role, self.controller_sha = api, role, controller_sha
        self.author, self.committer = author, committer
        self.run_id = uuid.uuid4().hex
        self.owned_sha = None
        self.tree = None

    def read(self):
        try:
            ref = self.api.request("GET", "git/ref/" + LOCK_REF)
        except Exception as exc:
            if getattr(exc, "status", None) == 404:
                return None
            raise
        try:
            sha = ref["object"]["sha"]
            if (ref["ref"] != "refs/" + LOCK_REF or ref["object"]["type"] != "commit"
                    or not re.fullmatch(r"[0-9a-f]{40}", sha)):
                raise ValueError("Invalid ref")
        except (KeyError, TypeError, ValueError) as exc:
            raise LockError("Integration lock ref is malformed") from exc
        commit = self.api.request("GET", "git/commits/" + sha)
        try:
            record = json.loads(commit["message"])
            if (not isinstance(record, dict)
                    or set(record) != {"schema", "state", "run_id", "role", "controller_sha", "at"}
                    or record["schema"] != LOCK_SCHEMA or record["state"] not in {"held", "released"}
                    or record["role"] not in {"primary", "fallback"}
                    or not re.fullmatch(r"[0-9a-f]{32}", record["run_id"])
                    or not re.fullmatch(r"[0-9a-f]{40}", record["controller_sha"])
                    or commit["sha"] != sha or not re.fullmatch(r"[0-9a-f]{40}", commit["tree"]["sha"])
                    or len(commit["parents"]) != 1
                    or not re.fullmatch(r"[0-9a-f]{40}", commit["parents"][0]["sha"])
                    or datetime.datetime.fromisoformat(record["at"]).utcoffset() != datetime.timedelta(0)):
                raise ValueError("Invalid lock state")
            for field, identity in (("author", self.author), ("committer", self.committer)):
                if any(commit[field].get(key) != value for key, value in identity.items()):
                    raise ValueError("Invalid lock identity")
        except (KeyError, TypeError, ValueError, AttributeError) as exc:
            raise LockError("Integration lock state is unreadable; owner recovery required") from exc
        return sha, commit["tree"]["sha"], record

    def transition(self, parent, tree, state, *, create=False):
        record = {"schema": LOCK_SCHEMA, "state": state, "run_id": self.run_id,
                  "role": self.role, "controller_sha": self.controller_sha,
                  "at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        commit = self.api.request("POST", "git/commits", {
            "message": json.dumps(record, sort_keys=True), "tree": tree,
            "parents": [parent], "author": self.author, "committer": self.committer,
        })
        candidate = commit["sha"]
        if not re.fullmatch(r"[0-9a-f]{40}", candidate):
            raise LockError("Lock transition returned an invalid commit")
        try:
            if create:
                self.api.request("POST", "git/refs", {"ref": "refs/" + LOCK_REF, "sha": candidate})
            else:
                self.api.request("PATCH", "git/refs/" + LOCK_REF, {"sha": candidate, "force": False})
        except Exception as exc:
            # One readback, never a second write. A delayed/uncertain request may
            # strand ownership, but cannot justify another claimant's takeover.
            observed = self.read()
            if observed is None or observed[0] != candidate:
                raise LockError("Lock transition unconfirmed; do not retry or reclaim automatically") from exc
        observed = self.read()
        if observed is None or observed[0] != candidate or observed[1] != tree or observed[2] != record:
            raise LockError("Lock transition lost ownership")
        return candidate

    def acquire(self, base):
        current = self.read()
        if current is not None and current[2]["state"] != "released":
            raise LockError("Integration lock is held; stalled runs require drained-owner recovery, never expiry")
        parent = current[0] if current else base
        self.tree = current[1] if current else self.api.request("GET", "git/commits/" + base)["tree"]["sha"]
        self.owned_sha = self.transition(parent, self.tree, "held", create=current is None)
        self.assert_owned()

    def assert_owned(self):
        if not self.owned_sha:
            raise LockError("Apply requires exclusive integration ownership")
        current = self.read()
        if (current is None or current[0] != self.owned_sha
                or current[2]["state"] != "held" or current[2]["run_id"] != self.run_id):
            raise LockError("Integration ownership lost; further writes are prohibited")

    def release(self):
        self.assert_owned()
        self.transition(self.owned_sha, self.tree, "released")
        self.owned_sha = None

    def receipt(self):
        return {"ref": "refs/" + LOCK_REF, "run_id": self.run_id,
                "ownership_commit": self.owned_sha, "automatic_expiry": False}
