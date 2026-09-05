from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from character_index_core import (  # noqa: E402
    AuthorityGraph,
    DomainError,
    GitSnapshot,
    SnapshotEntry,
    decode_jsonl_with_lines,
    evidence_set_digest,
    fold,
    render_schema_diagnostics,
    require_nfc,
    schema_diagnostics,
    schema_errors,
    validate_discovery_records,
    validate_repository_path,
    validate_schema_document,
)
from generate_character_index import render  # noqa: E402
from validate_repository import validate_markdown_links  # noqa: E402


def authority_bytes(status: str = "canonical") -> bytes:
    veto = "false" if status in {"canonical", "active_provisional"} else "true"
    successor = "[]" if status != "superseded" else "[series/example/NEXT.md]"
    return (
        "---\n"
        f"status: {status}\n"
        "supersedes: []\n"
        f"superseded_by: {successor}\n"
        f"do_not_use_as_current_authority: {veto}\n"
        "---\n"
        "# Analysis\n"
    ).encode()


def snapshot(*paths: tuple[str, bytes]) -> GitSnapshot:
    return GitSnapshot(
        Path("."),
        "TEST",
        {path: SnapshotEntry(path, "100644", data) for path, data in paths},
    )


def alias(value: str, *, kind: str = "ALTERNATIVE") -> dict:
    return {
        "value": value,
        "language": "en",
        "kind": kind,
        "ambiguous": False,
        "note": None,
    }


def record(
    subject_id: str,
    *,
    entity_id: str = "example:alice",
    series_id: str = "example",
    continuity_id: str | None = "anime",
    kind: str = "SINGLE_CONTINUITY",
    evidence_path: str | None = None,
    included: bool = False,
) -> dict:
    evidence = []
    coverage = []
    if evidence_path is not None:
        evidence = [
            {
                "evidence_id": "profile",
                "repository_path": evidence_path,
                "label": "Profile",
                "anchor": None,
                "review_state": "REVIEWED",
                "dimensions": ["PSYCHOLOGY"],
                "provenance_note": None,
            }
        ]
        coverage = [
            {
                "coverage_id": "episode-one",
                "continuity_id": continuity_id,
                "medium": "ANIME",
                "unit": "EPISODE",
                "scope_type": "DISCRETE",
                "locators": ["1"],
                "evidence_ids": ["profile"],
            }
        ]
    return {
        "schema_version": 2,
        "character_entity_id": entity_id,
        "analysis_subject_id": subject_id,
        "preferred_name": "Alice",
        "subject_label": subject_id.rsplit("@", 1)[1],
        "series_id": series_id,
        "franchise_id": None,
        "continuity_id": continuity_id,
        "incarnation_id": None,
        "state_id": None,
        "subject_kind": kind,
        "entity_aliases": [alias("Alice Example")],
        "subject_aliases": [],
        "analytical_dimensions": ["PSYCHOLOGY"],
        "evidence": evidence,
        "analytical_coverage": coverage,
        "materialization_status": "PRESENT_REVIEWED" if evidence_path else "NOT_PRESENT",
        "curation_status": "INCLUDED" if included else "CANDIDATE",
        "inclusion_basis": "DEDICATED" if included else None,
        "notes": None,
    }


class CanonicalizationTests(unittest.TestCase):
    def test_jsonl_decoder_preserves_physical_nonblank_line_numbers(self) -> None:
        payload = b'\n{"schema_version":2}\n   \n{"schema_version":2}\n'
        decoded = decode_jsonl_with_lines(payload, "characters/registry.jsonl")
        self.assertEqual([line_number for line_number, _record in decoded], [2, 4])

    def test_normative_evidence_golden_vector(self) -> None:
        digest, serialized = evidence_set_digest(
            [
                {
                    "analysis_subject_id": "example:alice@anime",
                    "anchor": None,
                    "artifact_sha256": "b6a98d9ce9a2d9149288fa3df42d377c3e42737afdcdaf714e33c0a100b51060",
                    "evidence_id": "profile",
                    "repository_path": "series/example/ALICE.md",
                }
            ]
        )
        self.assertEqual(
            digest,
            "174c697bb3e87f75bb1fc56d6aec718328e9e6670dc33859919d3a82e2d387d7",
        )
        self.assertEqual(
            serialized,
            b'{"canonicalization":"CHARACTER_EVIDENCE_SET_V1","evidence":[{"analysis_subject_id":"example:alice@anime","anchor":null,"artifact_sha256":"b6a98d9ce9a2d9149288fa3df42d377c3e42737afdcdaf714e33c0a100b51060","evidence_id":"profile","repository_path":"series/example/ALICE.md"}],"hash_algorithm":"SHA-256","unicode_version":"15.0.0"}',
        )

    def test_full_default_non_turkic_casefold(self) -> None:
        self.assertEqual(fold("Straße"), fold("STRASSE"))
        self.assertNotEqual(fold("I"), fold("İ"))

    def test_nfd_is_rejected(self) -> None:
        with self.assertRaises(DomainError):
            require_nfc("e\u0301", "fixture")

    def test_repository_paths_reject_raw_dot_empty_fragment_and_c1_segments(self) -> None:
        invalid = (
            "series/./x.md",
            "series/../x.md",
            "series//x.md",
            "series/x.md/",
            "series/x#fragment.md",
            "series/x\u0085y.md",
        )
        for path in invalid:
            with self.subTest(path=repr(path)):
                with self.assertRaises(DomainError):
                    validate_repository_path(path)

    @unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
    def test_all_reference_keywords_reject_remote_targets_without_network(self) -> None:
        for keyword in ("$ref", "$dynamicRef", "$recursiveRef"):
            schema = {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                keyword: "https://invalid.example/schema.json",
            }
            with self.subTest(keyword=keyword), mock.patch(
                "urllib.request.urlopen"
            ) as network:
                with self.assertRaisesRegex(DomainError, "remote or nonlocal"):
                    validate_schema_document(schema, "instrumented schema")
                network.assert_not_called()


class DiscoveryContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.series = {
            "series": [
                {"series_id": "example"},
                {"series_id": "other"},
            ]
        }

    def test_subject_alias_variance_does_not_create_entity_drift(self) -> None:
        anime = record("example:alice@anime")
        novel = record("example:alice@novel", continuity_id="novel")
        anime["subject_aliases"] = [alias("Anime Alice")]
        novel["subject_aliases"] = [alias("LN Alice")]
        self.assertEqual(validate_discovery_records([anime, novel], self.series), [])

    def test_entity_alias_variance_is_entity_drift(self) -> None:
        anime = record("example:alice@anime")
        novel = record("example:alice@novel", continuity_id="novel")
        novel["entity_aliases"] = [alias("Alice Variant")]
        failures = validate_discovery_records([anime, novel], self.series)
        self.assertTrue(any("entity-level drift" in item for item in failures), failures)

    def test_normalized_alias_overlap_across_scopes_fails(self) -> None:
        item = record("example:alice@anime")
        item["entity_aliases"] = [alias("Straße")]
        item["subject_aliases"] = [alias("STRASSE")]
        failures = validate_discovery_records([item], self.series)
        self.assertTrue(any("overlap" in failure for failure in failures), failures)

    def test_alias_note_boundary_whitespace_and_c1_control_fail(self) -> None:
        for bad_note in (" leading", "trailing ", "bad\u0085note"):
            with self.subTest(note=repr(bad_note)):
                item = record("example:alice@anime")
                item["entity_aliases"][0]["note"] = bad_note
                failures = validate_discovery_records([item], self.series)
                self.assertTrue(any("alias note" in failure for failure in failures), failures)

    def test_absent_evidence_paths_still_receive_strict_syntax_validation(self) -> None:
        for path in (
            "series/./x.md",
            "series//x.md",
            "series/x.md/",
            "series/x#fragment.md",
            "series/x\u0085y.md",
        ):
            with self.subTest(path=repr(path)):
                item = record("example:alice@anime", evidence_path=path)
                item["materialization_status"] = "NOT_PRESENT"
                failures = validate_discovery_records([item], self.series)
                self.assertTrue(
                    any("repository path" in failure or "unsafe" in failure or "control" in failure for failure in failures),
                    failures,
                )

    def test_present_reviewed_and_current_included_record_passes(self) -> None:
        path = "series/example/ALICE.md"
        snap = snapshot((path, authority_bytes()))
        authority = AuthorityGraph(snap)
        item = record("example:alice@anime", evidence_path=path, included=True)
        self.assertEqual(
            validate_discovery_records([item], self.series, snapshot=snap, authority=authority),
            [],
        )

    def test_mixed_materialization_is_rejected(self) -> None:
        first = "series/example/ALICE.md"
        item = record("example:alice@anime", evidence_path=first)
        item["evidence"].append(
            {
                "evidence_id": "missing",
                "repository_path": "series/example/MISSING.md",
                "label": "Missing",
                "anchor": None,
                "review_state": "REVIEWED",
                "dimensions": ["PSYCHOLOGY"],
                "provenance_note": None,
            }
        )
        snap = snapshot((first, authority_bytes()))
        failures = validate_discovery_records(
            [item], self.series, snapshot=snap, authority=AuthorityGraph(snap)
        )
        self.assertTrue(any("mixed present/absent" in failure for failure in failures), failures)

    def test_materialization_review_and_nonblob_permutations(self) -> None:
        path = "series/example/ALICE.md"
        reviewed = record("example:alice@anime", evidence_path=path)
        tracked = snapshot((path, authority_bytes()))
        self.assertEqual(
            validate_discovery_records(
                [reviewed], self.series, snapshot=tracked, authority=AuthorityGraph(tracked)
            ),
            [],
        )
        unreviewed = copy.deepcopy(reviewed)
        unreviewed["evidence"][0]["review_state"] = "UNREVIEWED"
        unreviewed["materialization_status"] = "PRESENT_UNREVIEWED"
        self.assertEqual(
            validate_discovery_records(
                [unreviewed], self.series, snapshot=tracked, authority=AuthorityGraph(tracked)
            ),
            [],
        )
        invalid_review = copy.deepcopy(reviewed)
        invalid_review["evidence"][0]["review_state"] = "APPROXIMATE"
        failures = validate_discovery_records(
            [invalid_review], self.series, snapshot=tracked, authority=AuthorityGraph(tracked)
        )
        self.assertTrue(any("unknown evidence review_state" in item for item in failures), failures)
        lfs = GitSnapshot(
            Path("."),
            "TEST",
            {
                path: SnapshotEntry(
                    path,
                    "100644",
                    b"version https://git-lfs.github.com/spec/v1\n",
                )
            },
        )
        absent = copy.deepcopy(reviewed)
        absent["materialization_status"] = "NOT_PRESENT"
        self.assertEqual(
            validate_discovery_records(
                [absent], self.series, snapshot=lfs, authority=AuthorityGraph(lfs)
            ),
            [],
        )

    def test_same_series_composite_and_projection(self) -> None:
        leaf_a = record("example:alice@anime-a", continuity_id="anime-a")
        leaf_b = record("example:alice@anime-b", continuity_id="anime-b")
        leaf_a["subject_aliases"] = [alias("Leaf A only")]
        path = "series/example/COMPOSITE.md"
        composite = record(
            "example:alice@composite",
            continuity_id=None,
            kind="COMPOSITE_MODEL",
            evidence_path=path,
            included=True,
        )
        composite["component_subject_ids"] = [
            "example:alice@anime-a",
            "example:alice@anime-b",
        ]
        composite["analytical_coverage"][0]["component_subject_id"] = "example:alice@anime-a"
        composite["analytical_coverage"][0]["continuity_id"] = "anime-a"
        snap = snapshot((path, authority_bytes()))
        authority = AuthorityGraph(snap)
        records = [leaf_b, composite, leaf_a]
        self.assertEqual(
            validate_discovery_records(records, self.series, snapshot=snap, authority=authority),
            [],
        )
        output = render(records, authority)
        self.assertIn("Composite analytical model (not a continuity)", output)
        self.assertIn("`anime-a`, `anime-b`", output)
        self.assertNotIn("Leaf A only", output)

    def test_cross_series_composite_fails(self) -> None:
        leaf_a = record("example:alice@anime-a", continuity_id="anime-a")
        leaf_b = record(
            "example:alice@anime-b",
            series_id="other",
            continuity_id="anime-b",
        )
        composite = record(
            "example:alice@composite", continuity_id=None, kind="COMPOSITE_MODEL"
        )
        composite["component_subject_ids"] = [leaf_a["analysis_subject_id"], leaf_b["analysis_subject_id"]]
        failures = validate_discovery_records([leaf_a, leaf_b, composite], self.series)
        self.assertTrue(any("cross-series composite" in failure for failure in failures), failures)

    def test_composite_cycle_fails(self) -> None:
        first = record("example:alice@first", continuity_id=None, kind="COMPOSITE_MODEL")
        second = record("example:alice@second", continuity_id=None, kind="COMPOSITE_MODEL")
        leaf = record("example:alice@leaf")
        first["component_subject_ids"] = [second["analysis_subject_id"], leaf["analysis_subject_id"]]
        second["component_subject_ids"] = [first["analysis_subject_id"], leaf["analysis_subject_id"]]
        failures = validate_discovery_records([first, second, leaf], self.series)
        self.assertTrue(any("cycle" in failure for failure in failures), failures)

    def test_nested_composite_duplicate_leaf_reachability_fails(self) -> None:
        leaf_a = record("example:alice@a", continuity_id="a")
        leaf_b = record("example:alice@b", continuity_id="b")
        nested = record("example:alice@nested", continuity_id=None, kind="COMPOSITE_MODEL")
        nested["component_subject_ids"] = [leaf_a["analysis_subject_id"], leaf_b["analysis_subject_id"]]
        outer = record("example:alice@outer", continuity_id=None, kind="COMPOSITE_MODEL")
        outer["component_subject_ids"] = [nested["analysis_subject_id"], leaf_a["analysis_subject_id"]]
        failures = validate_discovery_records([leaf_a, leaf_b, nested, outer], self.series)
        self.assertTrue(any("multiple branches" in item for item in failures), failures)

    def test_composite_cannot_inherit_leaf_evidence_or_inclusion(self) -> None:
        leaf_a = record("example:alice@a", continuity_id="a")
        leaf_b = record("example:alice@b", continuity_id="b")
        composite = record("example:alice@composite", continuity_id=None, kind="COMPOSITE_MODEL")
        composite["component_subject_ids"] = [leaf_a["analysis_subject_id"], leaf_b["analysis_subject_id"]]
        composite["curation_status"] = "INCLUDED"
        composite["inclusion_basis"] = "DEDICATED"
        failures = validate_discovery_records([leaf_a, leaf_b, composite], self.series)
        self.assertTrue(any("INCLUDED requires evidence" in item for item in failures), failures)

    def test_render_declares_scoped_post_cutover_git_authority(self) -> None:
        path = "series/example/A.md"
        authority = AuthorityGraph(snapshot((path, authority_bytes())))
        included = record("example:alice@anime", evidence_path=path, included=True)
        for records in ([], [included]):
            with self.subTest(included=bool(records)):
                output = render(records, authority)
                self.assertIn("Git repository is the primary analytical authority", output)
                self.assertIn("governance/AUTHORITY_SCOPE.json", output)
                self.assertIn("governance/AUTHORITY_STATE.yaml", output)
                self.assertIn("remain outside Git authority", output)
                self.assertNotIn("nonauthoritative migration candidate", output)
                self.assertNotIn("Google Drive remains the analytical authority", output)
                self.assertNotIn("Git candidate", output)

    def test_input_reordering_does_not_change_rendered_bytes(self) -> None:
        path_a = "series/example/A.md"
        path_b = "series/example/B.md"
        snap = snapshot((path_a, authority_bytes()), (path_b, authority_bytes("active_provisional")))
        authority = AuthorityGraph(snap)
        a = record("example:alice@a", continuity_id="a", evidence_path=path_a, included=True)
        b = record("example:bob@b", entity_id="example:bob", continuity_id="b", evidence_path=path_b, included=True)
        b["preferred_name"] = "Bob"
        b["entity_aliases"] = []
        self.assertEqual(render([a, b], authority), render([b, a], authority))
        self.assertIn("active provisional authority", render([b, a], authority))

    def test_entity_grouping_alias_once_and_segment_url_encoding(self) -> None:
        path_a = "series/example/A file (1)%.md"
        path_b = "series/example/B file.md"
        snap = snapshot((path_a, authority_bytes()), (path_b, authority_bytes()))
        authority = AuthorityGraph(snap)
        a = record("example:alice@a", continuity_id="a", evidence_path=path_a, included=True)
        b = record("example:alice@b", continuity_id="b", evidence_path=path_b, included=True)
        a["evidence"][0]["anchor"] = "section(1)%"
        output = render([b, a], authority)
        self.assertEqual(output.count("### Alice\n"), 1)
        self.assertEqual(output.count("Alice Example (en, ALTERNATIVE)"), 1)
        self.assertEqual(output.count("#### Subject:"), 2)
        self.assertIn(
            "series/example/A%20file%20%281%29%25.md#section%281%29%25",
            output,
        )
        linked = snapshot(
            (path_a, authority_bytes()),
            (path_b, authority_bytes()),
            ("governance/AUTHORITY_SCOPE.json", b"{}\n"),
            ("governance/AUTHORITY_STATE.yaml", b"{}\n"),
            ("CHARACTER_ANALYSIS_INDEX.md", output.encode("utf-8")),
        )
        self.assertEqual(validate_markdown_links(linked), [])

    def test_markdown_link_validator_rejects_malformed_and_separator_escapes(self) -> None:
        for target in (
            "series/example/bad%ZZ.md",
            "series/example/bad%2Fname.md",
            "series/example/bad%5Cname.md",
            "series/example/bad%FF.md",
        ):
            linked = snapshot(
                ("CHARACTER_ANALYSIS_INDEX.md", f"[bad]({target})\n".encode("utf-8"))
            )
            with self.subTest(target=target):
                self.assertTrue(validate_markdown_links(linked))

    def test_same_preferred_name_groups_follow_full_frozen_record_order(self) -> None:
        path_a = "series/example/A.md"
        path_b = "series/example/B.md"
        snap = snapshot((path_a, authority_bytes()), (path_b, authority_bytes()))
        authority = AuthorityGraph(snap)
        zeta = record(
            "example:alice@zeta",
            evidence_path=path_a,
            included=True,
        )
        alpha = record(
            "example:bob@alpha",
            entity_id="example:bob",
            evidence_path=path_b,
            included=True,
        )
        zeta["subject_label"] = "Zeta"
        alpha["preferred_name"] = "Alice"
        alpha["subject_label"] = "Alpha"
        alpha["entity_aliases"] = []
        output = render([zeta, alpha], authority)
        self.assertLess(output.index("#### Subject: Alpha"), output.index("#### Subject: Zeta"))


@unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
class DiscoverySchemaPathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(
            (TOOLS.parent / "governance/schemas/character-analysis-index.schema.json").read_text(
                encoding="utf-8"
            )
        )

    def test_raw_unsafe_path_forms_fail_schema(self) -> None:
        baseline = record("example:alice@anime", evidence_path="series/example/A.md")
        for path in (
            "series/./x.md",
            "series/../x.md",
            "series//x.md",
            "series/x.md/",
            "series/x#fragment.md",
            "series/x\u0085y.md",
        ):
            item = copy.deepcopy(baseline)
            item["evidence"][0]["repository_path"] = path
            with self.subTest(path=repr(path)):
                self.assertTrue(schema_errors(item, self.schema, "discovery"))

    def test_every_full_string_pattern_uses_absolute_end_guard(self) -> None:
        patterns: list[str] = []

        def collect(value: object) -> None:
            if isinstance(value, dict):
                pattern = value.get("pattern")
                if isinstance(pattern, str):
                    patterns.append(pattern)
                for child in value.values():
                    collect(child)
            elif isinstance(value, list):
                for child in value:
                    collect(child)

        collect(self.schema)
        full_string_patterns = [pattern for pattern in patterns if pattern.startswith("^")]
        self.assertTrue(full_string_patterns)
        for pattern in full_string_patterns:
            with self.subTest(pattern=pattern):
                self.assertTrue(pattern.endswith(r"$(?![\s\S])"), pattern)

    def test_terminal_controls_fail_human_text_and_ontology_ids(self) -> None:
        baseline = record("example:alice@anime", evidence_path="series/example/A.md")
        for control in ("\n", "\r", "\x01", "\x85"):
            human = copy.deepcopy(baseline)
            human["preferred_name"] = "Alice" + control
            ontology = copy.deepcopy(baseline)
            ontology["analysis_subject_id"] = "example:alice@anime" + control
            for label, item in (("human", human), ("ontology", ontology)):
                with self.subTest(control=repr(control), label=label):
                    self.assertTrue(schema_errors(item, self.schema, "discovery"))

    def test_terminal_lf_fails_every_discovery_string_grammar(self) -> None:
        mutations = {
            "entity_id": lambda item: item.__setitem__(
                "character_entity_id", "example:alice\n"
            ),
            "series_id": lambda item: item.__setitem__("series_id", "example\n"),
            "local_id": lambda item: item["evidence"][0].__setitem__(
                "evidence_id", "profile\n"
            ),
            "language": lambda item: item["entity_aliases"][0].__setitem__(
                "language", "en\n"
            ),
            "repository_path": lambda item: item["evidence"][0].__setitem__(
                "repository_path", "series/example/A.md\n"
            ),
            "anchor": lambda item: item["evidence"][0].__setitem__(
                "anchor", "section\n"
            ),
            "locator": lambda item: item["analytical_coverage"][0]["locators"].__setitem__(
                0, "1\n"
            ),
        }
        for name, mutate in mutations.items():
            item = copy.deepcopy(
                record("example:alice@anime", evidence_path="series/example/A.md")
            )
            mutate(item)
            with self.subTest(name=name):
                self.assertTrue(schema_errors(item, self.schema, "discovery"))

    def test_schema_diagnostics_are_numeric_stable_and_value_redacted(self) -> None:
        later = record("example:alice@anime", evidence_path="series/example/A.md")
        later["preferred_name"] = "SENSITIVE_LATER_VALUE\n"
        earlier = record("example:alice@anime", evidence_path="series/example/A.md")
        earlier["analysis_subject_id"] = "SENSITIVE_PRIVATE_SUBJECT"
        earlier["preferred_name"] = "SENSITIVE_EARLIER_VALUE\n"

        diagnostics = []
        diagnostics.extend(
            schema_diagnostics(
                later,
                self.schema,
                "characters/registry.jsonl",
                line_number=10,
            )
        )
        diagnostics.extend(
            schema_diagnostics(
                earlier,
                self.schema,
                "characters/registry.jsonl",
                line_number=2,
            )
        )
        rendered = render_schema_diagnostics(reversed(diagnostics))
        self.assertTrue(rendered)
        self.assertTrue(all("line=2:" in item for item in rendered[:2]))
        first_line_10 = next(index for index, item in enumerate(rendered) if "line=10:" in item)
        self.assertTrue(all("line=2:" in item for item in rendered[:first_line_10]))
        joined = "\n".join(rendered)
        for marker in (
            "SENSITIVE_LATER_VALUE",
            "SENSITIVE_EARLIER_VALUE",
            "SENSITIVE_PRIVATE_SUBJECT",
        ):
            self.assertNotIn(marker, joined)
        self.assertIn("subject=example:alice@anime", joined)
        self.assertIn("subject=<unavailable>", joined)
        self.assertIn("instance=/preferred_name", joined)
        self.assertIn("schema=", joined)


if __name__ == "__main__":
    unittest.main()
