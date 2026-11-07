from __future__ import annotations

import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from prepare_commit import (  # noqa: E402
    IDENTITY_ENVIRONMENT,
    commit_identity_errors,
    identity_configured,
    push_identity_errors,
    staged_size_errors,
)
from validate_repository import TRACKED_FILE_POLICY_PATH  # noqa: E402

APPROVED = {"name": "Approved Author", "email": "approved.invalid@example.invalid"}
SERVER = {"name": "GitHub", "email": "noreply@github.com"}
PLATFORM_DEFAULT = ("Claude", "noreply@anthropic.com")


class StagedSizeGateTests(unittest.TestCase):
    """The local commit gate applies the audit's review threshold to staged blobs."""

    def setUp(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value:
            self.skipTest("MANGA_ANIME_TEST_TMP is not set")
        base = Path(base_value).resolve(strict=True)
        self.root = Path(tempfile.mkdtemp(prefix="prepare-commit-", dir=base)).resolve(strict=True)
        self.assertTrue(self.root.is_relative_to(base))
        self.git("init", "--quiet")
        self.git("config", "user.name", "Prepare Commit Test")
        self.git("config", "user.email", "prepare-commit-test.invalid@example.invalid")
        policy = {
            "review_threshold_bytes": 4096,
            "hard_exception_threshold_bytes": 8192,
            "allowed_text_extensions": [".md", ".jsonl", ".json"],
            "named_text_exceptions": [],
        }
        self.write(TRACKED_FILE_POLICY_PATH, (json.dumps(policy, indent=2) + "\n").encode())
        self.git("add", "--", TRACKED_FILE_POLICY_PATH)

    def tearDown(self) -> None:
        def clear_readonly(function, path, _exception):
            os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
            function(path)

        root = getattr(self, "root", None)
        if root is not None:
            shutil.rmtree(root, onexc=clear_readonly)

    def git(self, *args: str) -> str:
        return subprocess.check_output(
            ["git", "-C", str(self.root), *args], stderr=subprocess.PIPE, text=True
        ).strip()

    def write(self, path: str, data: bytes) -> None:
        target = self.root / Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def staged(self) -> set[str]:
        return {item for item in self.git("ls-files", "--cached", "-z").split("\0") if item}

    def test_staged_blob_over_the_threshold_fails_and_one_under_passes(self) -> None:
        small = "characters/reconstruction_capabilities/example/alice@anime.jsonl"
        large = "characters/reconstruction_capabilities/example/bob@anime.jsonl"
        self.write(small, b'{"assessment_id":"alice-v1"}\n')
        self.write(large, b'{"assessment_id":"bob-v1","note":"' + b"x" * 4096 + b'"}\n')
        self.git("add", "--", small, large)
        errors = staged_size_errors(self.root, {small, large}, self.staged())
        self.assertEqual(len(errors), 1, errors)
        self.assertIn(f"staged file exceeds 1 MiB review threshold: {large} (", errors[0])
        self.assertEqual(staged_size_errors(self.root, {small}, self.staged()), [])

    def test_only_staged_bytes_are_measured(self) -> None:
        path = "characters/reconstruction_capabilities/example/alice@anime.jsonl"
        self.write(path, b'{"assessment_id":"alice-v1"}\n')
        self.git("add", "--", path)
        # A worktree edit that is not staged does not change the gate's verdict,
        # and a deleted path has no staged blob to measure.
        self.write(path, b"x" * 8192)
        self.assertEqual(staged_size_errors(self.root, {path}, self.staged()), [])
        self.git("rm", "--cached", "--force", "--quiet", "--", path)
        self.assertEqual(staged_size_errors(self.root, {path}, self.staged()), [])


class CommitIdentityGateTests(unittest.TestCase):
    """The local gates refuse the identities the repository audit would reject.

    A cloud sandbox recreated between turns comes back with the platform's
    default identity, so the gate must read what Git resolves at check time.
    """

    POLICY = {
        "allowed_author_identities": [APPROVED],
        "allowed_committer_identities": [APPROVED, SERVER],
        "allowed_commit_identities": [APPROVED, SERVER],
    }

    def setUp(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value:
            self.skipTest("MANGA_ANIME_TEST_TMP is not set")
        base = Path(base_value).resolve(strict=True)
        self.root = Path(tempfile.mkdtemp(prefix="identity-", dir=base)).resolve(strict=True)
        self.addCleanup(shutil.rmtree, self.root, onexc=self.clear_readonly)
        # Hide the developer's or runner's own identity from every Git child process.
        empty_global = self.root / "empty-global.gitconfig"
        empty_global.write_bytes(b"")
        isolated = {"GIT_CONFIG_GLOBAL": str(empty_global), "GIT_CONFIG_NOSYSTEM": "1"}
        environment = mock.patch.dict(os.environ, isolated)
        environment.start()
        self.addCleanup(environment.stop)
        for name in (*IDENTITY_ENVIRONMENT, "EMAIL"):
            os.environ.pop(name, None)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.git("init", "--quiet")

    @staticmethod
    def clear_readonly(function, path, _exception):
        os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
        function(path)

    def git(self, *args: str) -> str:
        return subprocess.check_output(
            ["git", "-C", str(self.repo), *args], stderr=subprocess.PIPE, text=True
        ).strip()

    def use_identity(self, name: str, email: str) -> None:
        self.git("config", "user.name", name)
        self.git("config", "user.email", email)

    def commit_as(self, name: str, email: str, message: str) -> str:
        self.git("-c", f"user.name={name}", "-c", f"user.email={email}",
                 "commit", "--quiet", "--allow-empty", "-m", message)
        return self.git("rev-parse", "HEAD")

    def test_only_a_configured_identity_is_checked(self) -> None:
        self.assertFalse(identity_configured(self.repo))
        with mock.patch.dict(os.environ, {"GIT_AUTHOR_NAME": APPROVED["name"]}):
            self.assertTrue(identity_configured(self.repo))
        self.use_identity(*PLATFORM_DEFAULT)
        self.assertTrue(identity_configured(self.repo))

    def test_the_next_commit_must_use_an_approved_author_and_committer(self) -> None:
        self.use_identity(APPROVED["name"], APPROVED["email"])
        self.assertEqual(commit_identity_errors(self.repo, self.POLICY), [])

        self.use_identity(*PLATFORM_DEFAULT)
        self.assertEqual(
            commit_identity_errors(self.repo, self.POLICY),
            [
                "disallowed Git author identity: Claude <noreply@anthropic.com>",
                "disallowed Git committer identity: Claude <noreply@anthropic.com>",
            ],
        )

        # The environment overrides config, and the server identity may only commit.
        server = {"GIT_COMMITTER_NAME": SERVER["name"], "GIT_COMMITTER_EMAIL": SERVER["email"]}
        approved = {"GIT_AUTHOR_NAME": APPROVED["name"], "GIT_AUTHOR_EMAIL": APPROVED["email"]}
        with mock.patch.dict(os.environ, {**server, **approved}):
            self.assertEqual(commit_identity_errors(self.repo, self.POLICY), [])
        as_server = {"GIT_AUTHOR_NAME": SERVER["name"], "GIT_AUTHOR_EMAIL": SERVER["email"]}
        with mock.patch.dict(os.environ, {**server, **as_server}):
            self.assertEqual(
                commit_identity_errors(self.repo, self.POLICY),
                ["disallowed Git author identity: GitHub <noreply@github.com>"],
            )

    def test_a_push_range_is_refused_while_it_holds_an_unapproved_commit(self) -> None:
        policy = self.repo / Path(TRACKED_FILE_POLICY_PATH)
        policy.parent.mkdir(parents=True)
        policy.write_bytes((json.dumps(self.POLICY, indent=2) + "\n").encode())
        self.git("add", "--", TRACKED_FILE_POLICY_PATH)
        base = self.commit_as(APPROVED["name"], APPROVED["email"], "policy")
        unapproved = self.commit_as(*PLATFORM_DEFAULT, "enroll a row")
        self.commit_as(APPROVED["name"], APPROVED["email"], "revise a row")

        self.assertEqual(
            push_identity_errors(self.repo, f"{base}..HEAD"),
            [
                "disallowed Git author identity: Claude <noreply@anthropic.com>",
                "disallowed Git committer identity: Claude <noreply@anthropic.com>",
            ],
        )
        self.assertEqual(push_identity_errors(self.repo, f"{unapproved}..HEAD"), [])
        with self.assertRaises(ValueError):
            push_identity_errors(self.repo, "--all")


if __name__ == "__main__":
    unittest.main()
