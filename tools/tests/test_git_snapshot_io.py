from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import character_index_core as core


class BatchProtocolTests(unittest.TestCase):
    def test_binary_empty_and_duplicate_blobs_keep_exact_bytes(self) -> None:
        for data in (b"", b"a\0b\r\nc\n", b"\xff\xfe", b"blob 3\nabc\n"):
            oid = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            raw = f"{oid} blob {len(data)}\n".encode() + data + b"\n"
            with self.subTest(data=data), mock.patch.object(core, "run_git", return_value=raw) as run:
                self.assertEqual(core.read_blob_objects(Path("."), [oid, oid]), {oid: data})
                self.assertEqual(run.call_count, 1)
                self.assertEqual(run.call_args.kwargs["input_bytes"], (oid + "\n").encode())

    def test_bad_batch_responses_fail_closed(self) -> None:
        oid = hashlib.sha1(b"blob 3\0abc").hexdigest()
        header = f"{oid} blob 3\n".encode()
        responses = (
            b"", f"{oid} missing\n".encode(), f"{oid} tree 3\nabc\n".encode(),
            b"0" * 40 + b" blob 3\nabc\n", header + b"ab", header + b"abc",
            header + b"abc!", header + b"abc\nextra", header + b"abd\n",
            f"{oid} blob 999999999999999999999\n".encode(),
        )
        for raw in responses:
            with self.subTest(raw=raw), mock.patch.object(core, "run_git", return_value=raw):
                with self.assertRaises(core.DomainError):
                    core.read_blob_objects(Path("."), [oid])

    def test_invalid_requests_never_start_git_and_empty_requests_are_free(self) -> None:
        with mock.patch.object(core, "run_git") as run:
            self.assertEqual(core.read_blob_objects(Path("."), []), {})
            for oid in ("main", "a" * 39, "A" * 40, "a" * 40 + "\n", []):
                with self.subTest(oid=oid), self.assertRaises(core.DomainError):
                    core.read_blob_objects(Path("."), [oid])
            run.assert_not_called()

    def test_git_failure_is_not_an_empty_success(self) -> None:
        error = subprocess.CalledProcessError(1, ["git"], stderr=b"object unavailable")
        with mock.patch.object(core.subprocess, "check_output", side_effect=error):
            with self.assertRaises(core.DomainError):
                core.read_blob_objects(Path("."), ["a" * 40])


class SnapshotIOTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="snapshot-io-", ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "--quiet")
        self.git("config", "user.name", "Snapshot Test")
        self.git("config", "user.email", "snapshot@example.invalid")
        self.git("config", "core.autocrlf", "false")

    def git(self, *args: str, data: bytes | None = None) -> bytes:
        return subprocess.check_output(["git", "-C", str(self.root), *args], input=data, stderr=subprocess.PIPE)

    def stage(self, path: str, data: bytes, mode: str = "100644") -> str:
        oid = self.git("hash-object", "-w", "--stdin", data=data).decode().strip()
        self.git("update-index", "--add", "--cacheinfo", f"{mode},{oid},{path}")
        return oid

    def commit(self) -> str:
        tree = self.git("write-tree").decode().strip()
        return self.git("commit-tree", tree, data=b"test\n").decode().strip()

    def test_commit_and_index_match_individual_raw_reads_and_modes(self) -> None:
        for path, data, mode in (
            ("folder/spaced name.md", b"a\0b\r\nc\n", "100644"),
            ("unicode/caf\u00e9.md", b"\xff\xfe", "100644"),
            ("empty", b"", "100644"), ("executable", b"run\n", "100755"),
            ("link", b"folder/spaced name.md", "120000"),
            ("duplicate", b"a\0b\r\nc\n", "100644"),
        ):
            self.stage(path, data, mode)
        commit = self.commit()
        self.git("update-index", "--add", "--cacheinfo", f"160000,{commit},submodule")
        commit = self.commit()
        for snapshot in (core.GitSnapshot.from_commit(self.root, commit), core.GitSnapshot.from_index(self.root)):
            self.assertEqual(len(snapshot.entries), 7)
            for path, entry in snapshot.entries.items():
                expected = self.git("show", f"{commit}:{path}") if entry.mode != "160000" else b""
                self.assertEqual(entry.data, expected)
                self.assertEqual(entry.qualifies_as_evidence, entry.mode == "100644")

    def test_process_count_is_bounded_and_duplicate_blobs_are_read_once(self) -> None:
        for i in range(12):
            self.stage(f"file-{i}.md", b"shared\n")
        commit = self.commit()
        with mock.patch.object(core, "run_git", wraps=core.run_git) as run:
            core.GitSnapshot.from_commit(self.root, commit)
            self.assertEqual(run.call_count, 4)
            batch = [c for c in run.call_args_list if c.args[1:] == ("cat-file", "--batch")]
            self.assertEqual(len(batch), 1)
            self.assertEqual(len(batch[0].kwargs["input_bytes"].splitlines()), 1)
        with mock.patch.object(core, "run_git", wraps=core.run_git) as run:
            core.GitSnapshot.from_index(self.root)
            self.assertEqual(run.call_count, 3)

    def test_index_change_during_acquisition_is_rejected(self) -> None:
        self.stage("file", b"before")
        original = core.read_blob_objects
        def read_then_change(root, ids):
            blobs = original(root, ids)
            self.stage("file", b"after")
            return blobs
        with mock.patch.object(core, "read_blob_objects", side_effect=read_then_change):
            with self.assertRaisesRegex(core.DomainError, "index changed"):
                core.GitSnapshot.from_index(self.root)

    def test_unmerged_index_is_rejected_before_blob_acquisition(self) -> None:
        oid = self.stage("file", b"base")
        self.git("update-index", "--force-remove", "file")
        self.git("update-index", "--index-info", data=f"100644 {oid} 1\tfile\n".encode())
        with mock.patch.object(core, "read_blob_objects") as read:
            with self.assertRaisesRegex(core.DomainError, "unmerged"):
                core.GitSnapshot.from_index(self.root)
            read.assert_not_called()

    def test_new_index_snapshot_never_reuses_previous_staged_bytes(self) -> None:
        self.stage("file", b"before")
        first = core.GitSnapshot.from_index(self.root)
        self.stage("file", b"after")
        second = core.GitSnapshot.from_index(self.root)
        self.assertEqual(first.entries["file"].data, b"before")
        self.assertEqual(second.entries["file"].data, b"after")

    def test_sha256_object_format_is_supported(self) -> None:
        other = self.root / "sha256"
        other.mkdir()
        self.root = other
        self.git("init", "--quiet", "--object-format=sha256")
        self.git("config", "user.name", "Snapshot Test")
        self.git("config", "user.email", "snapshot@example.invalid")
        self.stage("file", b"sha256\n")
        snapshot = core.GitSnapshot.from_commit(self.root, self.commit())
        self.assertEqual(snapshot.entries["file"].data, b"sha256\n")
