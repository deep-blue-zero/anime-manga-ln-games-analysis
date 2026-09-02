from __future__ import annotations

import hashlib
import importlib.util
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
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

from character_index_core import (  # noqa: E402
    DomainError,
    GitSnapshot,
    SnapshotEntry,
    atomic_write_text,
)
from validate_repository import (  # noqa: E402
    CURRENT_MANIFEST,
    G3_BOUND_COMMIT,
    G3_BOUND_TREE,
    G3_MANIFEST,
    PROTECTED_HASHES,
    identity_revision_for_snapshot,
    read_manifest_from_snapshot,
    require_g3_selection,
    validate_audit_workflow,
    validate_commit_identities,
    validate_crosswalk_closure,
    validate_current_domain,
    validate_bytes,
    validate_exact_set,
    validate_markdown_links,
    validate_native_sheets,
    validate_named_whitespace_exceptions,
    validate_protected,
    worktree_paths,
    worktree_snapshot,
)


class PhaseValidationTests(unittest.TestCase):
    @staticmethod
    def p03_snapshot() -> GitSnapshot:
        snapshot = worktree_snapshot(ROOT, worktree_paths(ROOT))
        return GitSnapshot(
            ROOT,
            "IN_MEMORY_P03",
            {
                path: SnapshotEntry(entry.path, entry.mode, entry.data, tracked=True)
                for path, entry in snapshot.entries.items()
            },
        )

    @staticmethod
    def replace_entry(
        snapshot: GitSnapshot, path: str, data: bytes | None
    ) -> GitSnapshot:
        entries = dict(snapshot.entries)
        if data is None:
            entries.pop(path, None)
        else:
            entries[path] = SnapshotEntry(path, "100644", data, tracked=True)
        return GitSnapshot(ROOT, f"{snapshot.identity}_MUTATED", entries)

    @staticmethod
    def replace_jsonl_row(
        snapshot: GitSnapshot,
        path: str,
        predicate,
        mutate,
    ) -> GitSnapshot:
        rows = [
            json.loads(line)
            for line in snapshot.entries[path].data.decode("utf-8").splitlines()
            if line
        ]
        replacements = 0
        output = []
        for row in rows:
            if predicate(row):
                replacement = mutate(dict(row))
                replacements += 1
                if replacement is not None:
                    output.append(replacement)
            else:
                output.append(row)
        if replacements != 1:
            raise AssertionError(f"fixture predicate matched {replacements} rows")
        data = b"".join(
            json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode(
                "utf-8"
            )
            + b"\n"
            for row in output
        )
        return PhaseValidationTests.replace_entry(snapshot, path, data)

    @staticmethod
    def named_text_policy(path: str, data: bytes, *, threshold: int = 8) -> dict:
        return {
            "allowed_text_extensions": [".csv"],
            "review_threshold_bytes": threshold,
            "hard_exception_threshold_bytes": 4096,
            "named_text_exceptions": [
                {
                    "path": path,
                    "bytes": len(data),
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "exception_id": "TEST_REVIEWED_CSV",
                    "allow_utf8_bom": True,
                    "allow_carriage_returns": True,
                    "purpose": "Test a reviewed text tuple.",
                    "rights_basis": "Test fixture.",
                    "review_decision": "TEST_APPROVED",
                    "external_reference_insufficient": "Test fixture must remain queryable.",
                }
            ],
        }

    @staticmethod
    def one_entry_snapshot(path: str, data: bytes) -> GitSnapshot:
        return GitSnapshot(
            ROOT,
            "IN_MEMORY",
            {path: SnapshotEntry(path, "100644", data)},
        )

    def test_production_named_text_exception_is_exactly_bound(self) -> None:
        policy = json.loads(
            (ROOT / "governance/repository-controls/tracked-file-policy.json").read_bytes()
        )
        exceptions = policy["named_text_exceptions"]
        by_path = {row["path"]: row for row in exceptions}
        idoly_path = (
            "series/idoly-pride/V2 Analysis/02 Source Audits and Longitudinal "
            "Ledgers/02.01 Corpus Coverage and Priority Ledger/"
            "IDOLY_PRIDE_V2_SOURCE_TO_BUNDLE_PROVENANCE.csv"
        )
        crosswalk_paths = {
            "crosswalk/drive-to-git.jsonl",
            "crosswalk/materialization-results.jsonl",
            "crosswalk/path-plan.jsonl",
        }
        self.assertEqual(set(by_path), {*crosswalk_paths, idoly_path})
        for path, row in by_path.items():
            with self.subTest(path=path):
                data = (ROOT / path).read_bytes()
                self.assertEqual(row["bytes"], len(data))
                self.assertEqual(row["sha256"], hashlib.sha256(data).hexdigest())
        self.assertTrue(by_path[idoly_path]["allow_utf8_bom"])
        self.assertTrue(by_path[idoly_path]["allow_carriage_returns"])
        self.assertEqual(
            by_path[idoly_path]["exception_id"],
            "IDOLY_PRIDE_SOURCE_TO_BUNDLE_PROVENANCE_CSV",
        )
        for path in crosswalk_paths:
            with self.subTest(crosswalk=path):
                self.assertFalse(by_path[path]["allow_utf8_bom"])
                self.assertFalse(by_path[path]["allow_carriage_returns"])
                self.assertEqual(
                    by_path[path]["review_decision"],
                    "OWNER_AUTHORIZED_G7_AGGREGATE_PROVENANCE_CLOSURE",
                )

    def test_production_furina_commonmark_exception_is_exactly_bound(self) -> None:
        policy = json.loads(
            (ROOT / "governance/repository-controls/tracked-file-policy.json").read_bytes()
        )
        expected_lines = [*range(16, 20), *range(28, 59)]
        self.assertEqual(len(expected_lines), 35)
        self.assertEqual(
            policy["named_whitespace_exceptions"],
            [
                {
                    "path": "series/genshin-impact/05 Character Monographs/GENSHIN_FURINA_CHARACTER_MONOGRAPH.md",
                    "bytes": 106094,
                    "sha256": "f61db7d38eb980bf6906fccee93a78200048f6bd2cf6efcfe60788520918b356",
                    "exception_id": "GENSHIN_FURINA_COMMONMARK_HARD_BREAKS",
                    "attribute": "whitespace=-blank-at-eol",
                    "trailing_ascii_spaces": 2,
                    "line_numbers": expected_lines,
                    "purpose": "Preserve 35 intentional CommonMark hard breaks in the source-exact Furina monograph.",
                    "review_decision": "STANDING_AUTHORITY_G5_T03_COMMONMARK_HARD_BREAK_TUPLE",
                }
            ],
        )

        snapshot = worktree_snapshot(ROOT, worktree_paths(ROOT))
        self.assertEqual(validate_named_whitespace_exceptions(snapshot, policy), [])

    def test_furina_commonmark_exception_rejects_byte_or_line_shape_drift(self) -> None:
        policy = json.loads(
            (ROOT / "governance/repository-controls/tracked-file-policy.json").read_bytes()
        )
        snapshot = worktree_snapshot(ROOT, worktree_paths(ROOT))
        path = policy["named_whitespace_exceptions"][0]["path"]
        original = snapshot.entries[path].data
        mutated = original.replace(b"  \n", b" \n", 1)
        self.assertNotEqual(mutated, original)
        failures = validate_named_whitespace_exceptions(
            self.replace_entry(snapshot, path, mutated), policy
        )
        self.assertIn(f"named whitespace exception tuple mismatch: {path}", failures)
        self.assertTrue(
            any(
                failure.startswith(f"named whitespace exception line-shape mismatch: {path};")
                for failure in failures
            )
        )

    def test_furina_commonmark_exception_rejects_broader_attribute_rule(self) -> None:
        policy = json.loads(
            (ROOT / "governance/repository-controls/tracked-file-policy.json").read_bytes()
        )
        snapshot = worktree_snapshot(ROOT, worktree_paths(ROOT))
        attributes = snapshot.entries[".gitattributes"].data
        exact = (
            b'"series/genshin-impact/05 Character Monographs/'
            b'GENSHIN_FURINA_CHARACTER_MONOGRAPH.md" whitespace=-blank-at-eol'
        )
        self.assertIn(exact, attributes)
        broadened = attributes.replace(
            exact,
            b'"series/genshin-impact/**" whitespace=-blank-at-eol',
            1,
        )
        failures = validate_named_whitespace_exceptions(
            self.replace_entry(snapshot, ".gitattributes", broadened), policy
        )
        self.assertIn(
            ".gitattributes whitespace rules must equal the exact approved TSV and "
            "named byte-bound exception set",
            failures,
        )

        for bypass in (
            b'\n"series/genshin-impact/**" -whitespace\n',
            b'\n"series/genshin-impact/**" !whitespace\n',
            b'\n"series/genshin-impact/**" whitespace\n',
        ):
            with self.subTest(bypass=bypass):
                failures = validate_named_whitespace_exceptions(
                    self.replace_entry(snapshot, ".gitattributes", attributes + bypass),
                    policy,
                )
                self.assertIn(
                    ".gitattributes whitespace rules must equal the exact approved TSV and "
                    "named byte-bound exception set",
                    failures,
                )

        nested_path = "series/genshin-impact/.gitattributes"
        nested_entries = dict(snapshot.entries)
        nested_entries[nested_path] = SnapshotEntry(
            nested_path,
            "100644",
            b"** -whitespace\n",
            tracked=True,
        )
        failures = validate_named_whitespace_exceptions(
            GitSnapshot(ROOT, "IN_MEMORY_NESTED_ATTRIBUTES", nested_entries), policy
        )
        self.assertIn(
            f"nested .gitattributes files are prohibited: ['{nested_path}']",
            failures,
        )

    def test_p03_crosswalk_three_leg_closure_and_snapshot_hashes_pass(self) -> None:
        self.assertEqual(validate_crosswalk_closure(self.p03_snapshot()), [])

    def test_p03_crosswalk_rejects_a_missing_plan_leg(self) -> None:
        snapshot = self.p03_snapshot()
        path = "crosswalk/path-plan.jsonl"
        destination = (
            "studies/doujinshi-fanwork-comparative-taxonomy/"
            "DJFW_CURRENT_STATE_AND_CORPUS_MAP.md"
        )
        mutated = self.replace_jsonl_row(
            snapshot,
            path,
            lambda row: row.get("destination_path") == destination,
            lambda _row: None,
        )
        failures = validate_crosswalk_closure(mutated)
        self.assertTrue(
            any("three-leg destination closure failure (path-plan)" in item for item in failures)
        )

    def test_p03_crosswalk_rejects_duplicate_representation_id(self) -> None:
        snapshot = self.p03_snapshot()
        path = "crosswalk/drive-to-git.jsonl"
        destination = (
            "studies/doujinshi-fanwork-comparative-taxonomy/"
            "DJFW_CURRENT_STATE_AND_CORPUS_MAP.md"
        )
        duplicate = "repr-dfb9d63bdc2532d40f912a34"

        def change(row):
            row["representation_id"] = duplicate
            return row

        mutated = self.replace_jsonl_row(
            snapshot,
            path,
            lambda row: row.get("git_path") == destination,
            change,
        )
        failures = validate_crosswalk_closure(mutated)
        self.assertTrue(any("duplicate crosswalk representation_id" in item for item in failures))

    def test_g6_merged_source_group_rejects_nonidentical_source_tuple(self) -> None:
        snapshot = self.p03_snapshot()
        path = "crosswalk/drive-to-git.jsonl"
        destination = (
            "series/azur-lane/03 Character Reconstruction/ST_LOUIS_10213/"
            "ST_LOUIS_JP_ACOUSTIC_MEASUREMENT_MATRIX.csv"
        )

        def change(row):
            row["source_tuples"][1]["source_sha256"] = "0" * 64
            return row

        mutated = self.replace_jsonl_row(
            snapshot,
            path,
            lambda row: row.get("git_path") == destination,
            change,
        )
        failures = validate_crosswalk_closure(mutated)
        self.assertTrue(
            any("MERGE_IDENTICAL_BYTES_V1 sources are not byte-identical" in item for item in failures)
        )

    def test_p03_crosswalk_rejects_exact_committed_hash_drift(self) -> None:
        snapshot = self.p03_snapshot()
        path = "crosswalk/drive-to-git.jsonl"
        destination = (
            "studies/doujinshi-fanwork-comparative-taxonomy/"
            "DJFW_CURRENT_STATE_AND_CORPUS_MAP.md"
        )

        def change(row):
            row["git_sha256"] = "0" * 64
            return row

        mutated = self.replace_jsonl_row(
            snapshot,
            path,
            lambda row: row.get("git_path") == destination,
            change,
        )
        failures = validate_crosswalk_closure(mutated)
        self.assertTrue(any("committed-byte hash drift" in item for item in failures))

    def test_reference_only_crosswalk_rejects_a_destination(self) -> None:
        snapshot = self.p03_snapshot()
        path = "crosswalk/materialization-results.jsonl"

        def change(row):
            row["destination_path"] = "studies/forbidden.xlsx"
            return row

        mutated = self.replace_jsonl_row(
            snapshot,
            path,
            lambda row: row.get("drive_id")
            == "1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg"
            and row.get("result") == "REFERENCE_VERIFIED_NOT_MATERIALIZED",
            change,
        )
        failures = validate_crosswalk_closure(mutated)
        self.assertTrue(
            any("reference-only row contains destination fields" in item for item in failures)
        )

    def test_study_crosswalk_requires_source_revision_and_path_on_every_leg(self) -> None:
        snapshot = self.p03_snapshot()
        destination = (
            "studies/doujinshi-fanwork-comparative-taxonomy/"
            "DJFW_CURRENT_STATE_AND_CORPUS_MAP.md"
        )

        def remove_revision(row):
            row.pop("source_revision")
            return row

        missing_revision = self.replace_jsonl_row(
            snapshot,
            "crosswalk/path-plan.jsonl",
            lambda row: row.get("destination_path") == destination,
            remove_revision,
        )
        revision_failures = validate_crosswalk_closure(missing_revision)
        self.assertTrue(
            any(
                "plan leg missing bindings" in item and "source_revision" in item
                for item in revision_failures
            )
        )
        self.assertTrue(
            any("plan.source_revision must be a positive decimal string" in item for item in revision_failures)
        )

        def drift_path(row):
            row["source_path"] = "DOUJINSHI_FANWORK_COMPARATIVE_TAXONOMY/WRONG.md"
            return row

        path_drift = self.replace_jsonl_row(
            snapshot,
            "crosswalk/materialization-results.jsonl",
            lambda row: row.get("destination_path") == destination,
            drift_path,
        )
        path_failures = validate_crosswalk_closure(path_drift)
        self.assertTrue(
            any(
                "source_path/source_path mismatch between mapping and result" in item
                for item in path_failures
            )
        )

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_native_xlsx_reference_binds_source_revision_and_path(self) -> None:
        snapshot = self.p03_snapshot()
        drive_id = "1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg"

        def drift_revision(row):
            row["source_revision"] = "19"
            return row

        revision_drift = self.replace_jsonl_row(
            snapshot,
            "crosswalk/materialization-results.jsonl",
            lambda row: row.get("drive_id") == drive_id
            and row.get("result") == "REFERENCE_VERIFIED_NOT_MATERIALIZED",
            drift_revision,
        )
        revision_failures = validate_native_sheets(revision_drift, True)
        self.assertTrue(
            any("XLSX reference result binding drift" in item for item in revision_failures)
        )

        def remove_source_path(row):
            row.pop("source_path")
            return row

        missing_path = self.replace_jsonl_row(
            snapshot,
            "crosswalk/path-plan.jsonl",
            lambda row: row.get("drive_id") == drive_id
            and row.get("decision") == "REFERENCE_DRIVE",
            remove_source_path,
        )
        path_failures = validate_native_sheets(missing_path, True)
        self.assertTrue(
            any("XLSX reference plan binding drift" in item for item in path_failures)
        )

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_p03_native_sheet_schema_shape_hashes_and_crosswalk_pass(self) -> None:
        self.assertEqual(validate_native_sheets(self.p03_snapshot(), True), [])

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_native_sheet_discovery_ignores_unrelated_structure_json(self) -> None:
        snapshot = self.p03_snapshot()
        unrelated_path = "studies/unrelated/UNRELATED.structure.json"
        unrelated = self.replace_entry(
            snapshot,
            unrelated_path,
            b'{"schema":"unrelated/example/v1","value":true}\n',
        )
        self.assertEqual(validate_native_sheets(unrelated, True), [])

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_native_sheet_discovery_rejects_schema_id_orphan_manifest(self) -> None:
        snapshot = self.p03_snapshot()
        manifest_path = (
            "studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and "
            "Source Lock/DJFW_PROJECT_CONTROL_SHEET.structure.json"
        )
        orphan_path = (
            "studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and "
            "Source Lock/ORPHAN_NATIVE_SHEET.structure.json"
        )
        orphan = self.replace_entry(snapshot, orphan_path, snapshot.entries[manifest_path].data)
        failures = validate_native_sheets(orphan, True)
        self.assertTrue(
            any("drive-to-git closure failure" in item for item in failures)
        )

    def test_native_sheet_schema_allows_ordinals_longer_than_two_digits(self) -> None:
        schema = json.loads(
            (ROOT / "governance/schemas/native-sheet-structure.schema.json").read_bytes()
        )
        pattern = schema["$defs"]["worksheet"]["properties"][
            "tsv_destination_path"
        ]["pattern"]
        self.assertIn("[0-9]{2,}-", pattern)

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_p03_native_sheet_rejects_missing_and_orphan_tabs(self) -> None:
        snapshot = self.p03_snapshot()
        first_tab = (
            "studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and "
            "Source Lock/DJFW_PROJECT_CONTROL_SHEET.tabs/01-cases.tsv"
        )
        missing = self.replace_entry(snapshot, first_tab, None)
        missing_failures = validate_native_sheets(missing, True)
        self.assertTrue(any("native-sheet TSV is missing" in item for item in missing_failures))
        self.assertTrue(any("sibling TSV closure failure" in item for item in missing_failures))

        orphan_path = (
            "studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and "
            "Source Lock/DJFW_PROJECT_CONTROL_SHEET.tabs/18-orphan.tsv"
        )
        orphan = self.replace_entry(snapshot, orphan_path, b"orphan\n")
        orphan_failures = validate_native_sheets(orphan, True)
        self.assertTrue(any("sibling TSV closure failure" in item for item in orphan_failures))
        self.assertTrue(any("orphan native-sheet TSV paths" in item for item in orphan_failures))

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_p03_native_sheet_rejects_hash_and_rectangularity_drift(self) -> None:
        snapshot = self.p03_snapshot()
        first_tab = (
            "studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and "
            "Source Lock/DJFW_PROJECT_CONTROL_SHEET.tabs/01-cases.tsv"
        )
        data = snapshot.entries[first_tab].data
        first_lf = data.index(b"\n")
        changed = data[:first_lf] + b"\textra" + data[first_lf:]
        mutated = self.replace_entry(snapshot, first_tab, changed)
        failures = validate_native_sheets(mutated, True)
        self.assertTrue(any("TSV SHA-256 drift" in item for item in failures))
        self.assertTrue(any("TSV rectangularity failure" in item for item in failures))

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_p03_native_sheet_rejects_an_untracked_worktree_projection(self) -> None:
        snapshot = self.p03_snapshot()
        first_tab = (
            "studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and "
            "Source Lock/DJFW_PROJECT_CONTROL_SHEET.tabs/01-cases.tsv"
        )
        entries = dict(snapshot.entries)
        entry = entries[first_tab]
        entries[first_tab] = SnapshotEntry(
            entry.path, entry.mode, entry.data, tracked=False
        )
        mutated = GitSnapshot(ROOT, "UNTRACKED_P03_PROJECTION", entries)
        native_failures = validate_native_sheets(mutated, True)
        crosswalk_failures = validate_crosswalk_closure(mutated)
        self.assertTrue(
            any("not a tracked regular non-LFS Git blob" in item for item in native_failures)
        )
        self.assertTrue(
            any("not a tracked regular non-LFS blob" in item for item in crosswalk_failures)
        )

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_p03_native_sheet_rejects_name_collision_and_range_shape_drift(self) -> None:
        snapshot = self.p03_snapshot()
        manifest_path = (
            "studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and "
            "Source Lock/DJFW_PROJECT_CONTROL_SHEET.structure.json"
        )
        manifest = json.loads(snapshot.entries[manifest_path].data)
        manifest["worksheets"][1]["name"] = manifest["worksheets"][0]["name"].casefold()
        manifest["worksheets"][1]["address"] = "A1:M11"
        data = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        mutated = self.replace_entry(snapshot, manifest_path, data)
        failures = validate_native_sheets(mutated, True)
        self.assertTrue(any("worksheet name collision" in item for item in failures))
        self.assertTrue(any("declared range end/shape mismatch" in item for item in failures))

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_p03_native_sheet_rejects_path_traversal_and_tracked_xlsx(self) -> None:
        snapshot = self.p03_snapshot()
        manifest_path = (
            "studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and "
            "Source Lock/DJFW_PROJECT_CONTROL_SHEET.structure.json"
        )
        manifest = json.loads(snapshot.entries[manifest_path].data)
        manifest["worksheets"][0]["tsv_destination_path"] = (
            "studies/doujinshi-fanwork-comparative-taxonomy/01 Project Registry and "
            "Source Lock/DJFW_PROJECT_CONTROL_SHEET.tabs/../escape.tsv"
        )
        data = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        traversal = self.replace_entry(snapshot, manifest_path, data)
        traversal_failures = validate_native_sheets(traversal, True)
        self.assertTrue(
            any(
                "tsv_destination_path" in item and "validator=pattern" in item
                for item in traversal_failures
            )
        )

        xlsx_path = "studies/doujinshi-fanwork-comparative-taxonomy/source.xlsx"
        tracked_xlsx = self.replace_entry(snapshot, xlsx_path, b"PK\x03\x04")
        xlsx_failures = validate_native_sheets(tracked_xlsx, True)
        self.assertTrue(any("must remain REFERENCE_DRIVE" in item for item in xlsx_failures))

    def test_named_text_exception_allows_only_the_exact_large_bom_cr_tuple(self) -> None:
        path = "series/example/reviewed.csv"
        data = b"\xef\xbb\xbfleft,right\r\n1,2\r\n"
        policy = self.named_text_policy(path, data)
        self.assertEqual(validate_bytes(self.one_entry_snapshot(path, data), policy, "current"), [])

        changed = data[:-2] + b"3\n"
        failures = validate_bytes(
            self.one_entry_snapshot(path, changed), policy, "current"
        )
        self.assertIn(f"named text exception tuple mismatch: {path}", failures)
        self.assertTrue(any("exceeds 1 MiB review threshold" in item for item in failures))
        self.assertIn(f"UTF-8 BOM prohibited: {path}", failures)
        self.assertIn(f"non-LF line ending: {path}", failures)

    def test_named_text_exception_grants_no_capability_to_another_path(self) -> None:
        reviewed_path = "series/example/reviewed.csv"
        other_path = "series/example/other.csv"
        data = b"\xef\xbb\xbfleft,right\r\n1,2\r\n"
        policy = self.named_text_policy(reviewed_path, data)
        failures = validate_bytes(
            self.one_entry_snapshot(other_path, data), policy, "current"
        )
        self.assertTrue(any("exceeds 1 MiB review threshold" in item for item in failures))
        self.assertIn(f"UTF-8 BOM prohibited: {other_path}", failures)
        self.assertIn(f"non-LF line ending: {other_path}", failures)
        self.assertIn(f"unused named text exception: {reviewed_path}", failures)

    def test_named_text_exception_must_name_a_present_snapshot_path(self) -> None:
        path = "series/example/reviewed.csv"
        data = b"\xef\xbb\xbfleft,right\r\n1,2\r\n"
        policy = self.named_text_policy(path, data)
        snapshot = GitSnapshot(ROOT, "IN_MEMORY", {})
        self.assertEqual(
            validate_bytes(snapshot, policy, "current"),
            [f"unused named text exception: {path}"],
        )

    def test_named_text_exception_does_not_waive_content_safety_or_utf8(self) -> None:
        path = "series/example/reviewed.csv"
        data = (
            b"\xef\xbb\xbfhttps://" + b"drive." + b"google.com/example\r\n"
            + b"AIza"
            + b"A" * 31
            + b"\x00\xff"
        )
        policy = self.named_text_policy(path, data)
        failures = validate_bytes(self.one_entry_snapshot(path, data), policy, "current")
        self.assertFalse(any("exceeds 1 MiB review threshold" in item for item in failures))
        self.assertNotIn(f"UTF-8 BOM prohibited: {path}", failures)
        self.assertNotIn(f"non-LF line ending: {path}", failures)
        self.assertIn(f"possible Google API key in {path}", failures)
        self.assertIn(f"publication hazard (Google Drive URL) in {path}", failures)
        self.assertIn(f"NUL byte in text file: {path}", failures)
        self.assertTrue(any(item.startswith(f"invalid UTF-8 in {path}:") for item in failures))

    def test_named_text_exception_path_remains_hash_bound_below_threshold(self) -> None:
        path = "series/example/reviewed.csv"
        reviewed = b"\xef\xbb\xbfleft,right\r\n1,2\r\n"
        policy = self.named_text_policy(path, reviewed)
        failures = validate_bytes(
            self.one_entry_snapshot(path, b"small\n"), policy, "current"
        )
        self.assertEqual(failures, [f"named text exception tuple mismatch: {path}"])

    def test_malformed_named_text_exception_fails_closed(self) -> None:
        path = "series/example/reviewed.csv"
        data = b"\xef\xbb\xbfleft,right\r\n1,2\r\n"
        policy = self.named_text_policy(path, data)
        policy["named_text_exceptions"][0]["sha256"] = "A" * 64
        failures = validate_bytes(self.one_entry_snapshot(path, data), policy, "current")
        self.assertIn(
            "named_text_exceptions[0].sha256 must be exactly 64 lowercase hexadecimal characters",
            failures,
        )
        self.assertTrue(any("exceeds 1 MiB review threshold" in item for item in failures))
        self.assertIn(f"UTF-8 BOM prohibited: {path}", failures)
        self.assertIn(f"non-LF line ending: {path}", failures)

    def test_approved_repository_audit_workflow_is_non_mutating(self) -> None:
        snapshot = worktree_snapshot(ROOT, worktree_paths(ROOT))
        policy = json.loads(
            snapshot.entries[
                "governance/repository-controls/tracked-file-policy.json"
            ].data
        )
        self.assertEqual(validate_audit_workflow(snapshot, policy), [])

    def test_repository_audit_workflow_rejects_mutation_capability(self) -> None:
        path = ".github/workflows/repository-audit.yml"
        baseline = (ROOT / path).read_bytes()
        snapshot = GitSnapshot(
            ROOT,
            "IN_MEMORY",
            {
                path: SnapshotEntry(
                    path,
                    "100644",
                    baseline + b"\n# prohibited test token: git push\n",
                )
            },
        )
        policy = {"allowed_workflows": [path]}
        failures = validate_audit_workflow(snapshot, policy)
        self.assertIn(
            "repository-audit workflow contains prohibited capability: git push",
            failures,
        )

    def test_repository_audit_workflow_rejects_shallow_history(self) -> None:
        path = ".github/workflows/repository-audit.yml"
        baseline = (ROOT / path).read_bytes()
        complete_fetch = b'git fetch --no-tags origin "${GITHUB_SHA}"'
        shallow_fetch = b'git fetch --no-tags --depth=2 origin "${GITHUB_SHA}"'
        self.assertIn(complete_fetch, baseline)
        snapshot = GitSnapshot(
            ROOT,
            "IN_MEMORY",
            {
                path: SnapshotEntry(
                    path,
                    "100644",
                    baseline.replace(complete_fetch, shallow_fetch, 1),
                )
            },
        )
        failures = validate_audit_workflow(snapshot, {"allowed_workflows": [path]})
        self.assertIn(
            "repository-audit workflow contains prohibited capability: --depth",
            failures,
        )

    def test_repository_audit_workflow_requires_exact_whitespace_exclusions(self) -> None:
        path = ".github/workflows/repository-audit.yml"
        baseline = (ROOT / path).read_bytes()
        command = b'git show --check --format= "${GITHUB_SHA}" -- . \\\n'
        markdown = b"            ':(top,glob,exclude)**/*.md' \\\n"
        idoly = (
            b"            ':(top,literal,exclude)series/idoly-pride/V2 Analysis/02 "
            b"Source Audits and Longitudinal Ledgers/02.01 Corpus Coverage and Priority "
            b"Ledger/IDOLY_PRIDE_V2_SOURCE_TO_BUNDLE_PROVENANCE.csv'"
        )
        self.assertIn(command + markdown + idoly, baseline)

        missing = baseline.replace(
            command + markdown + idoly,
            b'git show --check --format= "${GITHUB_SHA}"',
        )
        broad = baseline.replace(
            markdown,
            b"            ':(top,glob,exclude)**/*' \\\n",
        )
        policy = {"allowed_workflows": [path]}
        expected = (
            "repository-audit workflow whitespace check must use only the exact approved "
            "Markdown glob and IDOLY PRIDE provenance CSV exclusions"
        )
        for label, content in (("missing", missing), ("broader", broad)):
            with self.subTest(label=label):
                snapshot = GitSnapshot(
                    ROOT,
                    "IN_MEMORY",
                    {path: SnapshotEntry(path, "100644", content)},
                )
                self.assertIn(expected, validate_audit_workflow(snapshot, policy))

    def test_historical_g3_commit_exact_set(self) -> None:
        snapshot = GitSnapshot.from_commit(ROOT, G3_BOUND_COMMIT)
        expected = read_manifest_from_snapshot(snapshot, G3_MANIFEST)
        self.assertEqual(validate_exact_set(sorted(snapshot.entries), expected, "g3"), [])

    def test_current_manifest_is_sorted_unique_and_complete(self) -> None:
        paths = worktree_paths(ROOT)
        snapshot = worktree_snapshot(ROOT, paths)
        expected = read_manifest_from_snapshot(snapshot, CURRENT_MANIFEST)
        self.assertEqual(
            validate_exact_set(sorted(snapshot.entries), expected, "current"), []
        )

    def test_protected_bootstrap_hashes_are_unchanged(self) -> None:
        snapshot = worktree_snapshot(ROOT, worktree_paths(ROOT))
        self.assertEqual(validate_protected(snapshot), [])
        for path, expected in PROTECTED_HASHES.items():
            self.assertEqual(hashlib.sha256(snapshot.entries[path].data).hexdigest(), expected)

    def test_untracked_worktree_file_cannot_materialize_evidence(self) -> None:
        entry = SnapshotEntry(
            "series/example/UNTRACKED.md",
            "100644",
            b"---\nstatus: canonical\nsupersedes: []\nsuperseded_by: []\ndo_not_use_as_current_authority: false\n---\n",
            tracked=False,
        )
        self.assertFalse(entry.qualifies_as_evidence)

    def test_basis_commit_rejects_abbreviation_uppercase_and_tree(self) -> None:
        head = subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True
        ).strip()
        tree = subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD^{tree}"], text=True
        ).strip()
        with self.assertRaises(DomainError):
            GitSnapshot.from_commit(ROOT, head[:12])
        with self.assertRaises(DomainError):
            GitSnapshot.from_commit(ROOT, head.upper())
        with self.assertRaises(DomainError):
            GitSnapshot.from_commit(ROOT, tree)

    def test_g3_cli_reads_historical_git_objects(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(TOOLS / "validate_repository.py"),
                "--phase",
                "g3",
                "--snapshot",
                "commit",
                "--repo",
                str(ROOT),
            ],
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("phase=g3", result.stdout)

    def test_g3_selection_is_immutable_and_tree_bound(self) -> None:
        self.assertEqual(
            require_g3_selection(ROOT, "commit", None, False),
            G3_BOUND_COMMIT,
        )
        actual_tree = subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", f"{G3_BOUND_COMMIT}^{{tree}}"],
            text=True,
        ).strip()
        self.assertEqual(actual_tree, G3_BOUND_TREE)
        with self.assertRaisesRegex(DomainError, "immutable bound commit"):
            require_g3_selection(ROOT, "commit", "0" * 40, False)
        for mode in ("worktree", "index"):
            with self.subTest(mode=mode), self.assertRaisesRegex(
                DomainError, "requires --snapshot commit"
            ):
                require_g3_selection(ROOT, mode, None, False)
        with self.assertRaisesRegex(DomainError, "prohibits an external manifest"):
            require_g3_selection(ROOT, "commit", None, True)

    def test_selected_non_head_commit_controls_identity_history(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value:
            self.skipTest("MANGA_ANIME_TEST_TMP is not set")
        base = Path(base_value).resolve(strict=True)
        temporary = Path(tempfile.mkdtemp(prefix="identity-history-", dir=base)).resolve(strict=True)
        self.assertTrue(temporary.is_relative_to(base))
        try:
            def git(*args: str) -> str:
                return subprocess.check_output(
                    ["git", "-C", str(temporary), *args],
                    text=True,
                    stderr=subprocess.PIPE,
                ).strip()

            git("init", "--quiet")
            git("config", "user.name", "Owner")
            git("config", "user.email", "owner@example.invalid")
            (temporary / "fixture.txt").write_text("owner\n", encoding="utf-8", newline="\n")
            git("add", "--", "fixture.txt")
            git("commit", "--quiet", "-m", "owner")
            owner_commit = git("rev-parse", "HEAD")
            git("config", "user.name", "Other")
            git("config", "user.email", "other@example.invalid")
            (temporary / "fixture.txt").write_text("other\n", encoding="utf-8", newline="\n")
            git("add", "--", "fixture.txt")
            git("commit", "--quiet", "-m", "other")
            policy = {
                "allowed_commit_identities": [
                    {"name": "Owner", "email": "owner@example.invalid"}
                ]
            }
            selected = identity_revision_for_snapshot("commit", owner_commit)
            self.assertEqual(selected, owner_commit)
            self.assertEqual(validate_commit_identities(temporary, policy, selected), [])
            self.assertTrue(
                validate_commit_identities(
                    temporary,
                    policy,
                    identity_revision_for_snapshot("worktree", None),
                )
            )
        finally:
            def clear_readonly(function, path, _exception):
                os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
                function(path)

            shutil.rmtree(temporary, onexc=clear_readonly)

    def test_percent_encoded_markdown_paths_decode_before_resolution(self) -> None:
        target = "series/example/A file (1)%.md"
        snapshot = GitSnapshot(
            ROOT,
            "IN_MEMORY",
            {
                "CHARACTER_ANALYSIS_INDEX.md": SnapshotEntry(
                    "CHARACTER_ANALYSIS_INDEX.md",
                    "100644",
                    b"[evidence](series/example/A%20file%20%281%29%25.md#section)\n",
                ),
                target: SnapshotEntry(target, "100644", b"# Evidence\n"),
            },
        )
        self.assertEqual(validate_markdown_links(snapshot), [])

    def test_schema_deferral_rejects_a_nonempty_registry(self) -> None:
        snapshot = GitSnapshot(
            ROOT,
            "IN_MEMORY",
            {
                "characters/registry.jsonl": SnapshotEntry(
                    "characters/registry.jsonl", "100644", b'{"invalid":true}\n'
                ),
                "series/registry.json": SnapshotEntry(
                    "series/registry.json", "100644", b'{"series":[]}\n'
                ),
                "governance/schemas/character-analysis-index.schema.json": SnapshotEntry(
                    "governance/schemas/character-analysis-index.schema.json",
                    "100644",
                    (ROOT / "governance/schemas/character-analysis-index.schema.json").read_bytes(),
                ),
                "governance/schemas/character-reconstruction-capability.schema.json": SnapshotEntry(
                    "governance/schemas/character-reconstruction-capability.schema.json",
                    "100644",
                    (
                        ROOT
                        / "governance/schemas/character-reconstruction-capability.schema.json"
                    ).read_bytes(),
                ),
            },
        )
        self.assertEqual(
            validate_current_domain(ROOT, snapshot, False),
            ["schema-engine deferral is permitted only for an empty character registry"],
        )

    def test_schema_failure_short_circuits_domain_assumptions(self) -> None:
        snapshot = GitSnapshot(
            ROOT,
            "IN_MEMORY",
            {
                "characters/registry.jsonl": SnapshotEntry(
                    "characters/registry.jsonl", "100644", b'{"invalid":true}\n'
                ),
                "series/registry.json": SnapshotEntry(
                    "series/registry.json", "100644", b'{"series":[]}\n'
                ),
                "governance/schemas/character-analysis-index.schema.json": SnapshotEntry(
                    "governance/schemas/character-analysis-index.schema.json",
                    "100644",
                    (ROOT / "governance/schemas/character-analysis-index.schema.json").read_bytes(),
                ),
                "governance/schemas/character-reconstruction-capability.schema.json": SnapshotEntry(
                    "governance/schemas/character-reconstruction-capability.schema.json",
                    "100644",
                    (
                        ROOT
                        / "governance/schemas/character-reconstruction-capability.schema.json"
                    ).read_bytes(),
                ),
            },
        )
        with mock.patch(
            "validate_repository.validate_schema_document"
        ), mock.patch(
            "validate_repository.schema_diagnostics", return_value=[object()]
        ), mock.patch(
            "validate_repository.render_schema_diagnostics",
            return_value=["schema invalid"],
        ), mock.patch(
            "validate_repository.validate_discovery_records",
            side_effect=AssertionError("domain validation must not receive schema-invalid data"),
        ):
            self.assertEqual(
                validate_current_domain(ROOT, snapshot, True), ["schema invalid"]
            )

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_schema_diagnostic_uses_physical_jsonl_line_after_blank_lines(self) -> None:
        record = {
            "analysis_subject_id": "example:alice@anime",
            "preferred_name": "SENSITIVE_PHYSICAL_LINE_VALUE\n",
        }
        registry = ("\n" + json.dumps(record, separators=(",", ":")) + "\n").encode(
            "utf-8"
        )
        snapshot = GitSnapshot(
            ROOT,
            "IN_MEMORY",
            {
                "characters/registry.jsonl": SnapshotEntry(
                    "characters/registry.jsonl", "100644", registry
                ),
                "series/registry.json": SnapshotEntry(
                    "series/registry.json", "100644", b'{"series":[]}\n'
                ),
                "governance/schemas/character-analysis-index.schema.json": SnapshotEntry(
                    "governance/schemas/character-analysis-index.schema.json",
                    "100644",
                    (
                        ROOT
                        / "governance/schemas/character-analysis-index.schema.json"
                    ).read_bytes(),
                ),
                "governance/schemas/character-reconstruction-capability.schema.json": SnapshotEntry(
                    "governance/schemas/character-reconstruction-capability.schema.json",
                    "100644",
                    (
                        ROOT
                        / "governance/schemas/character-reconstruction-capability.schema.json"
                    ).read_bytes(),
                ),
            },
        )
        failures = validate_current_domain(ROOT, snapshot, True)
        self.assertTrue(failures)
        rendered = "\n".join(failures)
        self.assertIn("characters/registry.jsonl:line=2:", rendered)
        self.assertNotIn("characters/registry.jsonl:line=1:", rendered)
        self.assertNotIn("SENSITIVE_PHYSICAL_LINE_VALUE", rendered)

    def test_atomic_write_failure_preserves_prior_index_and_own_temp_boundary(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value:
            self.skipTest("MANGA_ANIME_TEST_TMP is not set")
        base = Path(base_value).resolve(strict=True)
        temporary = Path(
            tempfile.mkdtemp(prefix="atomic-index-", dir=base)
        ).resolve(strict=True)
        self.assertTrue(temporary.is_relative_to(base))
        try:
            output = temporary / "CHARACTER_ANALYSIS_INDEX.md"
            sentinel = temporary / "UNRELATED_SENTINEL.txt"
            candidate = temporary / ".CHARACTER_ANALYSIS_INDEX.md.tmp"
            output.write_bytes(b"prior index\n")
            sentinel.write_bytes(b"unrelated\n")
            with mock.patch(
                "character_index_core.os.replace",
                side_effect=OSError("simulated atomic replacement failure"),
            ):
                with self.assertRaisesRegex(OSError, "simulated atomic"):
                    atomic_write_text(output, "replacement index\n")
            self.assertEqual(output.read_bytes(), b"prior index\n")
            self.assertEqual(sentinel.read_bytes(), b"unrelated\n")
            self.assertFalse(candidate.exists())

            candidate.write_bytes(b"preexisting candidate\n")
            with self.assertRaisesRegex(DomainError, "preexisting temporary"):
                atomic_write_text(output, "must not replace\n")
            self.assertEqual(output.read_bytes(), b"prior index\n")
            self.assertEqual(candidate.read_bytes(), b"preexisting candidate\n")
            self.assertEqual(sentinel.read_bytes(), b"unrelated\n")
        finally:
            def clear_readonly(function, path, _exception):
                os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
                function(path)

            shutil.rmtree(temporary, onexc=clear_readonly)

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_populated_index_generates_from_index_then_checks_after_staging(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value:
            self.skipTest("MANGA_ANIME_TEST_TMP is not set")
        base = Path(base_value).resolve(strict=True)
        temporary = Path(tempfile.mkdtemp(prefix="index-generate-", dir=base)).resolve(strict=True)
        self.assertTrue(temporary.is_relative_to(base))
        try:
            def git(*args: str) -> None:
                subprocess.run(
                    ["git", "-C", str(temporary), *args],
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.PIPE,
                )

            git("init", "--quiet")
            git("config", "user.name", "Character Index Test")
            git("config", "user.email", "character-index-test.invalid@example.invalid")
            evidence_path = "series/example/A file (1)%.md"
            evidence = temporary / Path(evidence_path)
            evidence.parent.mkdir(parents=True)
            evidence.write_text(
                "---\nstatus: canonical\nsupersedes: []\nsuperseded_by: []\n"
                "do_not_use_as_current_authority: false\n---\n# Analysis\n",
                encoding="utf-8",
                newline="\n",
            )
            schema = temporary / "governance/schemas/character-analysis-index.schema.json"
            schema.parent.mkdir(parents=True)
            schema.write_bytes(
                (ROOT / "governance/schemas/character-analysis-index.schema.json").read_bytes()
            )
            series = temporary / "series/registry.json"
            series.write_text(
                json.dumps({"series": [{"series_id": "example"}]}, separators=(",", ":"))
                + "\n",
                encoding="utf-8",
                newline="\n",
            )
            record = {
                "schema_version": 2,
                "character_entity_id": "example:alice",
                "analysis_subject_id": "example:alice@anime",
                "preferred_name": "Alice",
                "subject_label": "Anime",
                "series_id": "example",
                "franchise_id": None,
                "continuity_id": "anime",
                "incarnation_id": None,
                "state_id": None,
                "subject_kind": "SINGLE_CONTINUITY",
                "entity_aliases": [],
                "subject_aliases": [],
                "analytical_dimensions": ["PSYCHOLOGY"],
                "evidence": [
                    {
                        "evidence_id": "profile",
                        "repository_path": evidence_path,
                        "label": "Profile",
                        "anchor": None,
                        "review_state": "REVIEWED",
                        "dimensions": ["PSYCHOLOGY"],
                        "provenance_note": None,
                    }
                ],
                "analytical_coverage": [
                    {
                        "coverage_id": "episode-one",
                        "continuity_id": "anime",
                        "medium": "ANIME",
                        "unit": "EPISODE",
                        "scope_type": "DISCRETE",
                        "locators": ["1"],
                        "evidence_ids": ["profile"],
                    }
                ],
                "materialization_status": "PRESENT_REVIEWED",
                "curation_status": "INCLUDED",
                "inclusion_basis": "DEDICATED",
                "notes": None,
            }
            registry = temporary / "characters/registry.jsonl"
            registry.parent.mkdir(parents=True)
            registry.write_text(
                json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
                + "\n",
                encoding="utf-8",
                newline="\n",
            )
            output = temporary / "CHARACTER_ANALYSIS_INDEX.md"
            output.write_text("# stale\n", encoding="utf-8", newline="\n")
            git("add", "--", ".")

            def fingerprint() -> dict[str, tuple[int, int, str]]:
                result: dict[str, tuple[int, int, str]] = {}
                for path in temporary.rglob("*"):
                    if not path.is_file() or ".git" in path.relative_to(temporary).parts:
                        continue
                    stat_result = path.stat()
                    result[path.relative_to(temporary).as_posix()] = (
                        stat_result.st_size,
                        stat_result.st_mtime_ns,
                        hashlib.sha256(path.read_bytes()).hexdigest(),
                    )
                return result

            generate = [
                sys.executable,
                str(TOOLS / "generate_character_index.py"),
                "--repo",
                str(temporary),
                "--snapshot",
                "index",
            ]
            stale_before = fingerprint()
            stale_check = subprocess.run(
                generate + ["--check"], text=True, capture_output=True
            )
            self.assertNotEqual(stale_check.returncode, 0)
            self.assertIn("out of date", stale_check.stdout + stale_check.stderr)
            self.assertEqual(fingerprint(), stale_before)
            self.assertFalse(
                (temporary / ".CHARACTER_ANALYSIS_INDEX.md.tmp").exists()
            )

            result = subprocess.run(generate, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Alice", output.read_text(encoding="utf-8"))
            generated_bytes = output.read_bytes()
            generated_sha256 = hashlib.sha256(generated_bytes).hexdigest()
            repeated = subprocess.run(generate, text=True, capture_output=True)
            self.assertEqual(repeated.returncode, 0, repeated.stdout + repeated.stderr)
            self.assertEqual(output.read_bytes(), generated_bytes)
            self.assertEqual(hashlib.sha256(output.read_bytes()).hexdigest(), generated_sha256)
            git("add", "--", "CHARACTER_ANALYSIS_INDEX.md")
            clean_before = fingerprint()
            checked = subprocess.run(generate + ["--check"], text=True, capture_output=True)
            self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
            self.assertEqual(fingerprint(), clean_before)
            self.assertFalse(
                (temporary / ".CHARACTER_ANALYSIS_INDEX.md.tmp").exists()
            )
        finally:
            def clear_readonly(function, path, _exception):
                os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
                function(path)

            shutil.rmtree(temporary, onexc=clear_readonly)

    def test_current_worktree_cli_fails_closed_until_evidence_is_staged(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(TOOLS / "validate_repository.py"),
                "--phase",
                "current",
                "--snapshot",
                "worktree",
                "--repo",
                str(ROOT),
            ],
            text=True,
            capture_output=True,
        )
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("worktree bytes cannot establish materialization", result.stdout)


if __name__ == "__main__":
    unittest.main()
