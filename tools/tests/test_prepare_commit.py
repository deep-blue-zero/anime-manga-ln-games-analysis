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

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from prepare_commit import staged_size_errors  # noqa: E402
from validate_repository import TRACKED_FILE_POLICY_PATH  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
