"""Mutation tests for stale-atlas and frozen-metadata safeguards (stdlib only)."""

import copy
import csv
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import validate_scores as validator

ROOT = Path(__file__).resolve().parents[2]


class SnapshotValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.csv_data = (ROOT / "data/pactrih_scores.csv").read_bytes()
        cls.html_data = (ROOT / "interactive/atlas.html").read_bytes()
        cls.rows, cls.records, cls.script = validator.validate_pair(cls.csv_data, cls.html_data)

    def csv_bytes(self, rows, columns=None):
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream, fieldnames=columns or validator.COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        return stream.getvalue().encode("utf-8")

    def html_bytes(self, records):
        text = self.html_data.decode("utf-8")
        match = validator.RAW_PATTERN.search(text)
        return (text[:match.start(1)] + json.dumps(records, ensure_ascii=False) + text[match.end(1):]).encode("utf-8")

    def test_baseline_pins_parity_and_manifest(self):
        result = validator.validate_snapshot(ROOT, javascript=False)
        self.assertEqual(result["subjects"], 100)
        self.assertEqual(result["unit_counts"], validator.COUNTS)

    def test_original_csv_bytes_are_recoverable(self):
        source = b"\xef\xbb\xbf" + self.csv_data.replace(b"\n", b"\r\n")
        self.assertEqual((len(source), validator.sha256(source)), validator.SOURCE_CSV_PIN)

    def test_schema_and_integer_range(self):
        with self.assertRaisesRegex(validator.ValidationError, "headers differ"):
            validator.load_csv(self.csv_bytes(self.rows, list(reversed(validator.COLUMNS))))
        for value in ("-1", "11", "7.5", "NaN", "True"):
            with self.subTest(value=value):
                rows = copy.deepcopy(self.rows)
                rows[0]["R"] = value
                with self.assertRaisesRegex(validator.ValidationError, "integer in 0..10"):
                    validator.load_csv(self.csv_bytes(rows))

    def test_duplicate_and_added_subject(self):
        rows = copy.deepcopy(self.rows)
        rows[1]["Character"] = rows[0]["Character"]
        with self.assertRaisesRegex(validator.ValidationError, "Duplicate subjects"):
            validator.load_csv(self.csv_bytes(rows))
        with self.assertRaisesRegex(validator.ValidationError, "Expected 100"):
            validator.load_csv(self.csv_bytes(self.rows + [self.rows[0]]))

    def test_derived_fields_and_unit_counts(self):
        for field, value, message in (("Humane Regard", "9.0", "Humane Regard mismatch"),
                                      ("Moral Structure", "NaN", "Moral Structure mismatch"),
                                      ("Unit", "Faction", "Unexpected unit counts")):
            rows = copy.deepcopy(self.rows)
            rows[0][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(validator.ValidationError, message):
                validator.load_csv(self.csv_bytes(rows))

    def test_stale_csv_score_and_unicode_description(self):
        for field, value, message in (("R", "8", "R mismatch"),
                                      ("Type", self.rows[0]["Type"] + " — altered", "description mismatch")):
            rows = copy.deepcopy(self.rows)
            rows[0][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(validator.ValidationError, message):
                validator.validate_pair(self.csv_bytes(rows), self.html_data)

    def test_embedding_order_unit_and_missing_entry(self):
        for mutation, message in ((lambda r: r.reverse(), "identity/order mismatch"),
                                   (lambda r: r[0].__setitem__(14, 2), "unit mismatch"),
                                   (lambda r: r.pop(), "entry count differs")):
            records = copy.deepcopy(self.records)
            mutation(records)
            with self.assertRaisesRegex(validator.ValidationError, message):
                validator.validate_pair(self.csv_data, self.html_bytes(records))

    def test_invalid_pca_and_cluster_fields(self):
        for offset, value, message in ((9, float("nan"), "invalid PCA"),
                                       (11, 9, "invalid cluster"), (12, True, "invalid cluster"),
                                       (15, 2, "invalid priority")):
            records = copy.deepcopy(self.records)
            records[0][offset] = value
            with self.subTest(offset=offset), self.assertRaisesRegex(validator.ValidationError, message):
                validator.validate_pair(self.csv_data, self.html_bytes(records))

    def test_valid_but_changed_pca_is_rejected_even_if_manifest_is_repinned(self):
        records = copy.deepcopy(self.records)
        records[0][9] += 0.1
        changed_html = self.html_bytes(records)
        validator.validate_pair(self.csv_data, changed_html)  # parity alone cannot detect this
        with tempfile.TemporaryDirectory(prefix="pactrih-test-") as directory:
            root = Path(directory)
            for name in ("data", "interactive", "audits"):
                (root / name).mkdir()
            (root / "data/pactrih_scores.csv").write_bytes(self.csv_data)
            (root / "interactive/atlas.html").write_bytes(changed_html)
            manifest = json.loads((ROOT / "audits/source_manifest.json").read_text(encoding="utf-8"))
            manifest["artifacts"]["interactive/atlas.html"].update(
                bytes=len(changed_html), sha256=validator.sha256(changed_html))
            (root / "audits/source_manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(validator.ValidationError, "Frozen baseline changed"):
                validator.validate_snapshot(root, javascript=False)

    def test_external_resources_and_corrupt_encoding_fail(self):
        for data in (b"\xef\xbb\xbf" + self.csv_data, self.csv_data.replace(b"\n", b"\r\n"), b"\xff" + self.csv_data):
            with self.assertRaises(ValueError):
                validator.load_csv(data)
        changed = self.html_data.replace(b"<script>", b'<script src="https://example.invalid/atlas.js">')
        with self.assertRaisesRegex(validator.ValidationError, "standalone"):
            validator.load_atlas(changed)

    def test_inline_network_dependencies_fail(self):
        for marker, injection in ((b"<script>", b"<script>fetch('https://example.invalid/x');"),
                                  (b"<script>", b"<script>new Image().src='//example.invalid/p';"),
                                  (b"<script>", b"<script>import('./mod.js');"),
                                  (b"<style>", b"<style>body{background:url(https://example.invalid/b.png)}"),
                                  (b"<style>", b"<style>@import 'theme.css';"),
                                  (b"<body", b'<body style="background:url(b.png)"')):
            with self.subTest(injection=injection):
                self.assertIn(marker, self.html_data)
                changed = self.html_data.replace(marker, injection, 1)
                with self.assertRaisesRegex(validator.ValidationError, "standalone"):
                    validator.load_atlas(changed)

    def test_node_is_required_and_syntax_failure_propagates(self):
        with patch.object(validator.subprocess, "run", side_effect=FileNotFoundError):
            with self.assertRaisesRegex(validator.ValidationError, "Node.js is required"):
                validator.check_javascript(self.script)
        with self.assertRaisesRegex(validator.ValidationError, "JavaScript syntax check failed"):
            validator.check_javascript("const = invalid;")


if __name__ == "__main__":
    unittest.main()
