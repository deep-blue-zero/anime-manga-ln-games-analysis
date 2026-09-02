from __future__ import annotations

import hashlib
import json
import sys
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from tools.character_index_core import (  # noqa: E402
    AuthorityGraph,
    AuthorityMetadata,
    DomainError,
    GitSnapshot,
    SnapshotEntry,
    _restricted_yaml_load,
    load_json,
    parse_authority_front_matter,
)


ACTIVATION_EVIDENCE = [
    (
        "PUBLIC_ACTIVATION_RECEIPT",
        "83420b23a5243c8a53ea04d934c2362125f72bd64ae13041253ec1ddf2b80e2e",
    ),
    (
        "POST_ACTIVATION_PROVIDER_STATE",
        "1f56ba8415f9b54e8aa63b41070230779de369dac964c67252606407f1b43b2f",
    ),
    (
        "INDEPENDENT_PUBLIC_AUDIT",
        "ab5f23601f284bb60f9a0f4c7fec607130f6e99d19536f06557a4700f9d06c1e",
    ),
]


def authority_document(
    status: str,
    *,
    supersedes: tuple[str, ...] = (),
    superseded_by: tuple[str, ...] = (),
    do_not_use: bool = False,
    boolean_spelling: str | None = None,
) -> bytes:
    lines = ["---", f"status: {status}"]
    if supersedes:
        lines.append("supersedes:")
        lines.extend(f"  - {path}" for path in supersedes)
    else:
        lines.append("supersedes: []")
    if superseded_by:
        lines.append("superseded_by:")
        lines.extend(f"  - {path}" for path in superseded_by)
    else:
        lines.append("superseded_by: []")
    spelling = boolean_spelling
    if spelling is None:
        spelling = "true" if do_not_use else "false"
    lines.extend(
        [
            f"do_not_use_as_current_authority: {spelling}",
            "---",
            "# In-memory authority fixture",
            "",
        ]
    )
    return "\n".join(lines).encode("utf-8")


def snapshot(documents: dict[str, bytes]) -> GitSnapshot:
    entries = {
        path: SnapshotEntry(path=path, mode="100644", data=data)
        for path, data in documents.items()
    }
    return GitSnapshot(REPOSITORY_ROOT, "IN_MEMORY_TEST", entries)


class AuthorityFrontMatterTests(unittest.TestCase):
    def test_restricted_yaml_rejects_nonstring_complex_mapping_keys(self) -> None:
        for text in ("? [a]\n: b\n", "1: value\n"):
            with self.subTest(text=text):
                with self.assertRaisesRegex(DomainError, "mapping keys must be strings"):
                    _restricted_yaml_load(text, "complex-key fixture")

    def test_supersession_paths_reject_raw_dot_fragment_and_c1_forms(self) -> None:
        for target in (
            "series/./x.md",
            "series//x.md",
            "series/x.md/",
            "series/x#fragment.md",
            "series/x\u0085y.md",
        ):
            with self.subTest(target=repr(target)):
                with self.assertRaises(DomainError):
                    parse_authority_front_matter(
                        authority_document("canonical", supersedes=(target,)),
                        "series/example/current.md",
                    )

    def test_valid_status_metadata_and_exact_boolean_spellings(self) -> None:
        successor = "series/example/current.md"
        cases = [
            (
                "canonical",
                authority_document("canonical"),
                AuthorityMetadata("canonical", (), (), False),
            ),
            (
                "active_provisional",
                authority_document("active_provisional"),
                AuthorityMetadata("active_provisional", (), (), False),
            ),
            (
                "superseded",
                authority_document(
                    "superseded",
                    superseded_by=(successor,),
                    do_not_use=True,
                ),
                AuthorityMetadata("superseded", (), (successor,), True),
            ),
            (
                "historical_legacy",
                authority_document("historical_legacy", do_not_use=True),
                AuthorityMetadata("historical_legacy", (), (), True),
            ),
        ]
        for name, data, expected in cases:
            with self.subTest(name=name):
                self.assertEqual(
                    parse_authority_front_matter(data, f"series/example/{name}.md"),
                    expected,
                )

    def test_non_exact_opener_is_unclassified_legacy(self) -> None:
        valid = authority_document("canonical")
        cases = {
            "bom_prefix": b"\xef\xbb\xbf" + valid,
            "crlf_opener": b"---\r\n" + valid[len(b"---\n") :],
            "leading_blank": b"\n" + valid,
            "leading_text": b"historical preface\n" + valid,
            "invalid_byte_before_opener": b"\xff" + valid,
            "crlf_opener_with_invalid_body": (
                b"---\r\n" + valid[len(b"---\n") :] + b"\xff"
            ),
        }
        for name, data in cases.items():
            path = f"series/example/nonexact-{name}.md"
            with self.subTest(name=name):
                self.assertIsNone(parse_authority_front_matter(data, path))
                graph = AuthorityGraph(snapshot({path: data}))
                self.assertEqual(graph.errors, [])
                self.assertEqual(graph.classification(path), "UNCLASSIFIED_LEGACY")
                self.assertFalse(graph.current_eligible(path))

    def test_exact_opener_invalid_surfaces_fail_closed(self) -> None:
        valid = authority_document("canonical")
        complete_front = (
            b"---\nstatus: canonical\nsupersedes: []\nsuperseded_by: []\n"
            b"do_not_use_as_current_authority: false\n"
        )
        cases = {
            "cr_in_front_matter": valid.replace(
                b"status: canonical\n", b"status: canonical\r\n", 1
            ),
            "crlf_closing_fence": valid.replace(
                b"do_not_use_as_current_authority: false\n---\n",
                b"do_not_use_as_current_authority: false\n---\r\n",
                1,
            ),
            "cr_in_body": valid.replace(
                b"# In-memory authority fixture\n",
                b"# In-memory authority fixture\r\n",
                1,
            ),
            "invalid_utf8_front": b"---\nstatus: \xff\n---\n",
            "invalid_utf8_body": valid + b"\xff",
            "malformed_yaml": b"---\nstatus: [\n---\n",
            "missing_closing_fence": complete_front,
            "malformed_closing_fence": complete_front + b"--\n",
            "unterminated_closing_line": complete_front + b"---",
        }
        for name, data in cases.items():
            path = f"series/example/invalid-{name}.md"
            with self.subTest(name=name):
                with self.assertRaises(DomainError):
                    parse_authority_front_matter(data, path)
                graph = AuthorityGraph(snapshot({path: data}))
                self.assertTrue(graph.errors)
                self.assertEqual(graph.classification(path), "INVALID")
                self.assertFalse(graph.current_eligible(path))

    def test_restricted_yaml_constructs_fail_closed(self) -> None:
        fronts = {
            "duplicate_key": "title: one\ntitle: two\n",
            "anchor": "title: &title value\n",
            "alias": "title: &title value\ncopy: *title\n",
            "merge": "defaults: &defaults\n  title: value\n<<: *defaults\n",
            "explicit_tag": "title: !!str value\n",
            "custom_tag": "title: !custom value\n",
        }
        for name, front in fronts.items():
            path = f"series/example/restricted-{name}.md"
            data = f"---\n{front}---\n# Body\n".encode("utf-8")
            with self.subTest(name=name):
                with self.assertRaises(DomainError):
                    parse_authority_front_matter(data, path)
                graph = AuthorityGraph(snapshot({path: data}))
                self.assertTrue(graph.errors)
                self.assertEqual(graph.classification(path), "INVALID")
                self.assertFalse(graph.current_eligible(path))

    def test_wrong_type_status_fails_closed_without_value_echo(self) -> None:
        for name, literal in {
            "array": "[]",
            "mapping": "{}",
            "boolean": "true",
            "integer": "1",
            "null": "null",
            "unknown_string": "sensitive-status-marker",
        }.items():
            path = f"series/example/wrong-status-{name}.md"
            data = (
                "---\n"
                f"status: {literal}\n"
                "supersedes: []\n"
                "superseded_by: []\n"
                "do_not_use_as_current_authority: false\n"
                "---\n# Body\n"
            ).encode("utf-8")
            with self.subTest(name=name):
                with self.assertRaises(DomainError) as caught:
                    parse_authority_front_matter(data, path)
                if name == "unknown_string":
                    self.assertNotIn(literal, str(caught.exception))
                graph = AuthorityGraph(snapshot({path: data}))
                self.assertTrue(graph.errors)
                self.assertEqual(graph.classification(path), "INVALID")
                self.assertFalse(graph.current_eligible(path))

    def test_supersession_arrays_reject_wrong_types_members_and_duplicates(self) -> None:
        invalid_values = {
            "scalar": "series/example/old.md",
            "mapping": "{}",
            "null": "null",
            "integer_member": "[1]",
            "nested_member": "[[]]",
            "duplicate": (
                "[series/example/old.md, series/example/old.md]"
            ),
        }
        for field in ("supersedes", "superseded_by"):
            for name, value in invalid_values.items():
                path = f"series/example/invalid-{field}-{name}.md"
                values = {
                    "supersedes": "[]",
                    "superseded_by": "[]",
                }
                values[field] = value
                data = (
                    "---\n"
                    "status: canonical\n"
                    f"supersedes: {values['supersedes']}\n"
                    f"superseded_by: {values['superseded_by']}\n"
                    "do_not_use_as_current_authority: false\n"
                    "---\n# Body\n"
                ).encode("utf-8")
                with self.subTest(field=field, name=name):
                    with self.assertRaises(DomainError):
                        parse_authority_front_matter(data, path)
                    graph = AuthorityGraph(snapshot({path: data}))
                    self.assertTrue(graph.errors)
                    self.assertEqual(graph.classification(path), "INVALID")
                    self.assertFalse(graph.current_eligible(path))

    def test_boolean_spelling_is_exact_and_not_merely_yaml_truthy(self) -> None:
        invalid_spellings = (
            "True",
            "FALSE",
            "yes",
            "no",
            "on",
            "off",
            "1",
            "0",
            '"true"',
            '"false"',
            "false # comment",
            "false ",
        )
        for spelling in invalid_spellings:
            with self.subTest(spelling=spelling):
                with self.assertRaises(DomainError):
                    parse_authority_front_matter(
                        authority_document(
                            "canonical",
                            boolean_spelling=spelling,
                        ),
                        "series/example/invalid-boolean.md",
                    )

    def test_current_status_with_veto_or_successor_is_contradictory(self) -> None:
        successor = "series/example/successor.md"
        for status in ("canonical", "active_provisional"):
            cases = (
                authority_document(status, do_not_use=True),
                authority_document(status, superseded_by=(successor,)),
            )
            for data in cases:
                with self.subTest(status=status, data=data):
                    with self.assertRaisesRegex(DomainError, "current status contradicts"):
                        parse_authority_front_matter(
                            data,
                            f"series/example/{status}.md",
                        )

    def test_partial_authority_quartet_is_unclassified_legacy_not_current(self) -> None:
        fields = {
            "status": "status: canonical",
            "supersedes": "supersedes: []",
            "superseded_by": "superseded_by: []",
            "do_not_use_as_current_authority": (
                "do_not_use_as_current_authority: false"
            ),
        }
        path = "series/example/partial.md"
        for omitted in fields:
            lines = ["---"]
            lines.extend(value for key, value in fields.items() if key != omitted)
            lines.extend(["---", "# Partial", ""])
            data = "\n".join(lines).encode("utf-8")
            with self.subTest(omitted=omitted):
                self.assertIsNone(parse_authority_front_matter(data, path))
                graph = AuthorityGraph(snapshot({path: data}))
                self.assertEqual(graph.errors, [])
                self.assertEqual(graph.classification(path), "UNCLASSIFIED_LEGACY")
                self.assertFalse(graph.current_eligible(path))

    def test_missing_quartet_is_unclassified_legacy_not_current(self) -> None:
        documents = {
            "series/example/plain.md": b"# No front matter\n",
            "studies/example/other-front-matter.md": (
                b"---\ntitle: Historical note\n---\n# Body\n"
            ),
        }
        graph = AuthorityGraph(snapshot(documents))
        self.assertEqual(graph.errors, [])
        for path in documents:
            with self.subTest(path=path):
                self.assertEqual(graph.classification(path), "UNCLASSIFIED_LEGACY")
                self.assertFalse(graph.current_eligible(path))


class AuthorityGraphTests(unittest.TestCase):
    def test_canonical_provisional_historical_and_missing_classifications(self) -> None:
        documents = {
            "series/example/canonical.md": authority_document("canonical"),
            "series/example/provisional.md": authority_document(
                "active_provisional"
            ),
            "studies/example/historical.md": authority_document(
                "historical_legacy", do_not_use=True
            ),
        }
        graph = AuthorityGraph(snapshot(documents))
        self.assertEqual(graph.errors, [])
        self.assertEqual(
            graph.classification("series/example/canonical.md"),
            "CANONICAL_CURRENT",
        )
        self.assertEqual(
            graph.classification("series/example/provisional.md"),
            "ACTIVE_PROVISIONAL_CURRENT",
        )
        self.assertEqual(
            graph.classification("studies/example/historical.md"),
            "HISTORICAL_LEGACY",
        )
        self.assertEqual(graph.classification("series/example/missing.md"), "MISSING")
        self.assertTrue(graph.current_eligible("series/example/canonical.md"))
        self.assertTrue(graph.current_eligible("series/example/provisional.md"))
        self.assertFalse(graph.current_eligible("studies/example/historical.md"))
        self.assertFalse(graph.current_eligible("series/example/missing.md"))

    def test_reciprocal_supersession_has_one_current_sink(self) -> None:
        old = "series/example/old.md"
        current = "series/example/current.md"
        graph = AuthorityGraph(
            snapshot(
                {
                    old: authority_document(
                        "superseded",
                        superseded_by=(current,),
                        do_not_use=True,
                    ),
                    current: authority_document("canonical", supersedes=(old,)),
                }
            )
        )
        self.assertEqual(graph.errors, [])
        self.assertEqual(graph.edges, {(old, current)})
        self.assertEqual(graph.classification(old), "SUPERSEDED")
        self.assertEqual(graph.classification(current), "CANONICAL_CURRENT")
        self.assertFalse(graph.current_eligible(old))
        self.assertTrue(graph.current_eligible(current))

    def test_three_node_chain_and_independent_components_are_valid(self) -> None:
        old = "series/example/old.md"
        middle = "series/example/middle.md"
        current = "series/example/current.md"
        other_old = "studies/example/old.md"
        other_current = "studies/example/current.md"
        graph = AuthorityGraph(
            snapshot(
                {
                    old: authority_document(
                        "superseded",
                        superseded_by=(middle,),
                        do_not_use=True,
                    ),
                    middle: authority_document(
                        "superseded",
                        supersedes=(old,),
                        superseded_by=(current,),
                        do_not_use=True,
                    ),
                    current: authority_document("canonical", supersedes=(middle,)),
                    other_old: authority_document(
                        "superseded",
                        superseded_by=(other_current,),
                        do_not_use=True,
                    ),
                    other_current: authority_document(
                        "active_provisional",
                        supersedes=(other_old,),
                    ),
                }
            )
        )
        self.assertEqual(graph.errors, [])
        self.assertEqual(graph.classification(old), "SUPERSEDED")
        self.assertEqual(graph.classification(middle), "SUPERSEDED")
        self.assertEqual(graph.classification(current), "CANONICAL_CURRENT")
        self.assertEqual(
            graph.classification(other_current),
            "ACTIVE_PROVISIONAL_CURRENT",
        )
        self.assertTrue(graph.current_eligible(current))
        self.assertTrue(graph.current_eligible(other_current))

    def test_each_one_sided_supersession_orientation_is_invalid(self) -> None:
        old = "series/example/old.md"
        current = "series/example/current.md"
        cases = {
            "predecessor_only": {
                old: authority_document(
                    "superseded",
                    superseded_by=(current,),
                    do_not_use=True,
                ),
                current: authority_document("canonical"),
            },
            "successor_only": {
                old: authority_document("historical_legacy", do_not_use=True),
                current: authority_document("canonical", supersedes=(old,)),
            },
        }
        for name, documents in cases.items():
            with self.subTest(name=name):
                graph = AuthorityGraph(snapshot(documents))
                self.assertTrue(
                    any("nonreciprocal supersession edge" in error for error in graph.errors)
                )
                self.assertEqual(graph.classification(old), "INVALID")
                self.assertEqual(graph.classification(current), "INVALID")

    def test_cyclic_reciprocal_graph_is_invalid(self) -> None:
        first = "series/example/first.md"
        second = "series/example/second.md"
        graph = AuthorityGraph(
            snapshot(
                {
                    first: authority_document(
                        "superseded",
                        supersedes=(second,),
                        superseded_by=(second,),
                        do_not_use=True,
                    ),
                    second: authority_document(
                        "superseded",
                        supersedes=(first,),
                        superseded_by=(first,),
                        do_not_use=True,
                    ),
                }
            )
        )
        self.assertTrue(any("supersession cycle" in error for error in graph.errors))
        self.assertTrue(
            any("exactly one current sink" in error for error in graph.errors)
        )
        self.assertEqual(graph.classification(first), "INVALID")
        self.assertEqual(graph.classification(second), "INVALID")

    def test_self_edge_and_multiple_current_sinks_are_invalid(self) -> None:
        self_path = "series/example/self.md"
        self_graph = AuthorityGraph(
            snapshot(
                {
                    self_path: authority_document(
                        "superseded",
                        supersedes=(self_path,),
                        superseded_by=(self_path,),
                        do_not_use=True,
                    )
                }
            )
        )
        self.assertTrue(any("self supersession edge" in error for error in self_graph.errors))
        self.assertEqual(self_graph.classification(self_path), "INVALID")

        old = "series/example/old.md"
        first_head = "series/example/first-head.md"
        second_head = "series/example/second-head.md"
        sink_graph = AuthorityGraph(
            snapshot(
                {
                    old: authority_document(
                        "superseded",
                        superseded_by=(first_head, second_head),
                        do_not_use=True,
                    ),
                    first_head: authority_document("canonical", supersedes=(old,)),
                    second_head: authority_document("canonical", supersedes=(old,)),
                }
            )
        )
        self.assertTrue(
            any("exactly one current sink" in error for error in sink_graph.errors)
        )
        for path in (old, first_head, second_head):
            self.assertEqual(sink_graph.classification(path), "INVALID")

    def test_exact_case_mismatch_is_dangling_and_noncurrent(self) -> None:
        old = "series/example/old.md"
        declared = "series/example/current.md"
        actual = "series/example/Current.md"
        graph = AuthorityGraph(
            snapshot(
                {
                    old: authority_document(
                        "superseded",
                        superseded_by=(declared,),
                        do_not_use=True,
                    ),
                    actual: authority_document("canonical", supersedes=(old,)),
                }
            )
        )
        self.assertTrue(any("dangling successor path" in error for error in graph.errors))
        self.assertFalse(graph.current_eligible(old))
        self.assertFalse(graph.current_eligible(actual))
        self.assertEqual(graph.classification(declared), "MISSING")

    def test_dangling_predecessor_and_successor_are_invalid(self) -> None:
        existing = "series/example/existing.md"
        missing = "series/example/missing.md"
        cases = {
            "dangling_successor": {
                existing: authority_document(
                    "superseded",
                    superseded_by=(missing,),
                    do_not_use=True,
                )
            },
            "dangling_predecessor": {
                existing: authority_document("canonical", supersedes=(missing,))
            },
        }
        for name, documents in cases.items():
            with self.subTest(name=name):
                graph = AuthorityGraph(snapshot(documents))
                self.assertTrue(any("dangling" in error for error in graph.errors))
                self.assertEqual(graph.classification(existing), "INVALID")
                self.assertEqual(graph.classification(missing), "MISSING")


class PublicGovernanceInvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.scope = load_json(REPOSITORY_ROOT / "governance/AUTHORITY_SCOPE.json")
        cls.binding = load_json(
            REPOSITORY_ROOT
            / "governance/repository-controls/public-activation-bindings.json"
        )
        state_path = REPOSITORY_ROOT / "governance/AUTHORITY_STATE.yaml"
        cls.state = _restricted_yaml_load(
            state_path.read_text(encoding="utf-8"),
            str(state_path),
        )

    def test_public_visibility_is_separate_from_analytical_authority(self) -> None:
        self.assertEqual(
            self.scope["state"],
            "PUBLIC_REPOSITORY_PRE_CUTOVER_DRIVE_AUTHORITATIVE",
        )
        self.assertEqual(self.scope["repository"]["current_visibility"], "PUBLIC")
        self.assertEqual(
            self.scope["repository"]["visibility_model"],
            "PUBLIC_OWNER_MAINTAINED",
        )
        self.assertEqual(self.state["repository"]["visibility"], "PUBLIC")
        self.assertEqual(self.binding["repository"]["visibility"], "PUBLIC")

        self.assertEqual(
            self.scope["before_verified_g8_activation"]["analytical_authority"],
            "GOOGLE_DRIVE",
        )
        self.assertEqual(
            self.state["effective_authority"]["analytical_corpus"],
            "GOOGLE_DRIVE",
        )
        self.assertEqual(
            self.binding["analytical_authority_activation"]
            ["current_analytical_authority"],
            "GOOGLE_DRIVE",
        )
        self.assertEqual(self.state["effective_authority"]["git_candidate"], "NONAUTHORITATIVE")
        self.assertEqual(
            self.scope["analytical_authority_cutover"]["status"],
            "NOT_STARTED",
        )

    def test_publication_and_g8_activation_fields_are_distinct(self) -> None:
        self.assertNotIn("activation", self.scope)
        self.assertNotIn("activation", self.state)
        self.assertNotIn("activation", self.binding)
        self.assertEqual(
            self.scope["repository_publication_activation"]["status"],
            "VERIFIED_G3_PUBLICATION_ACTIVATION",
        )
        self.assertEqual(
            self.state["publication"]["visibility_activation"],
            "VERIFIED_G3_PUBLICATION_ACTIVATION",
        )
        self.assertEqual(
            self.scope["repository_publication_activation"]["evidence_binding"],
            "governance/repository-controls/public-activation-bindings.json",
        )
        self.assertEqual(
            self.state["publication"]["evidence_binding"],
            "governance/repository-controls/public-activation-bindings.json",
        )
        for document in (self.scope, self.state, self.binding):
            authority = document["analytical_authority_activation"]
            self.assertEqual(authority["required_gate"], "G8")
            self.assertEqual(authority["status"], "NOT_AUTHORIZED")

    def test_migration_and_withdrawal_state_is_consistent(self) -> None:
        current_expected = {
            "completed_gate": "G6",
            "current_gate": "G7_CUTOVER_PREPARATION",
            "current_subphase": (
                "G7_AWAITING_FRESH_OWNER_DRIVE_FREEZE_AND_DELTA_AUTHORIZATION"
            ),
            "integrated_candidates": [
                "THE_IDOLMASTER_CINDERELLA_GIRLS_U149",
                "IDOLY_PRIDE_P02_SINGLE_LEDGER",
                "DOUJINSHI_FANWORK_COMPARATIVE_TAXONOMY_P03_NATIVE_DOC_SHEET",
                "MAEBASHI_WITCHES_V1",
                "MASS_EFFECT_COMPARATIVE_MEDIA_CHARACTER_MONOGRAPHS",
                "GENSHIN_IMPACT_FURINA_MONOGRAPH_V1",
                "IDOLMASTER_CINDERELLA_GIRLS_MOBILE_GAME_CHARACTER_MONOGRAPHS_V1",
                "BLUE_ARCHIVE_PROLOGUE_CHAPTER_1_AND_LONGITUDINAL_ANALYSIS_V1",
                "YOUJO_SENKI_V2_ANALYTICAL_CORPUS_V1",
                "LEGEND_OF_THE_GALACTIC_HEROES_FULL_PREFIX_V1",
                "G5_FINAL_AGGREGATE_CORPUS",
            ],
            "integrated_reference_controls": [
                "GAKUEN_IDOLMASTER_P04_ZIP_REFERENCE_ONLY",
            ],
            "p01_p04_local_preparation": (
                "P04_COMPLETE_P01_P03_MATERIALIZED_P04_REFERENCE_ONLY"
            ),
            "p05_v1_tuple": "WITHDRAWN_UNAPPROVED_SCHEMA_OBSOLETED",
            "p05_v2_status": (
                "U149_YONAIP_MAEBASHI_SEVEN_MASS_EFFECT_TWO_GENSHIN_FURINA_"
                "CINDERELLA_GIRLS_MOBILE_NINE_AND_BLUE_ARCHIVE_ELEVEN_"
                "AND_LOGH_TWO_PRESENT_REVIEWED"
            ),
            "g4_phase_closure": {
                "status": "PASS_ALL_FIVE_ARCHETYPES_REMOTE_AND_CI_VERIFIED",
                "audit_id": (
                    "g4-representative-pilot-completion-audit-20260901T062038Z"
                ),
                "audit_sha256": (
                    "794b5071897418cad5bee3b5bb91a8b941b049d5b26dc822e73d22958022876c"
                ),
                "pilot_high_water_commit": (
                    "ec2829f3026a29a51985576017c45465cd59ba4b"
                ),
                "pilot_high_water_tree": (
                    "3a9107fa78e445d7e6b6f682405d019831d1e5dd"
                ),
            },
            "g5_progress": {
                "last_tranche": "G5_FINAL_AGGREGATE_CORPUS",
                "run_id": "g5-final-aggregate-20260901T190000Z",
                "reconciliation_receipt_sha256": "c262bf5e0569c6bea571d08dae170af4bc5bcf268a340e5911fd7bd3d9db8f6f",
                "exclusion_review_sha256": "8462bce2293aa06ee2ed92678272fff802c3e40fb1870d18a71691bcaac03ab8",
                "source_objects": 5402,
                "migrated_source_objects": 2650,
                "materialized_representations": 2665,
                "tracked_paths_after": 2710,
                "status": "MATERIALIZED_VALIDATED_AND_PUBLISHED_PRE_G8",
            },
            "g6_phase_closure": {
                "status": (
                    "PASS_FULL_CORPUS_RECONCILED_REMOTE_CI_CLONE_AND_MIRROR_VERIFIED"
                ),
                "closure_receipt_sha256": (
                    "e7add3955f73305ff95ad93bd71c8f1624cc046da25ff1c984a914c5024af91f"
                ),
                "reconciliation_audit_sha256": (
                    "59af523542f434a76bb72e147592f64e96595fc720f27bf9d2b00e0fe946b2e5"
                ),
                "validator_log_sha256": (
                    "f4a0a146cfab3adc0773f4bba04d8e95a87b616c56d8d5ec0505c8472825a7d2"
                ),
                "published_commit": (
                    "663df66eefe72acfc57d47076b836e6c7c0a5a2e"
                ),
                "published_tree": (
                    "55484898d65a5a4c95a6c5d3d755b42096c21393"
                ),
                "ci_workflow_run_id": "33551152778",
            },
        }
        for document in (self.scope, self.state):
            with self.subTest(schema=document["schema"]):
                for key, value in current_expected.items():
                    self.assertEqual(document["migration"][key], value)
        self.assertEqual(
            self.binding["migration"]["current_subphase"],
            "P05_BLOCKED_PENDING_CHARACTER_SCHEMA_HARDENING",
        )
        self.assertNotIn("p05_v2_status", self.binding["migration"])

    def test_g4_and_g6_closures_and_g7_entry_are_consistent(self) -> None:
        expected_closure = {
            "status": "PASS_ALL_FIVE_ARCHETYPES_REMOTE_AND_CI_VERIFIED",
            "audit_id": (
                "g4-representative-pilot-completion-audit-20260901T062038Z"
            ),
            "audit_sha256": (
                "794b5071897418cad5bee3b5bb91a8b941b049d5b26dc822e73d22958022876c"
            ),
            "pilot_high_water_commit": (
                "ec2829f3026a29a51985576017c45465cd59ba4b"
            ),
            "pilot_high_water_tree": (
                "3a9107fa78e445d7e6b6f682405d019831d1e5dd"
            ),
        }
        for document in (self.scope, self.state):
            with self.subTest(schema=document["schema"]):
                self.assertEqual(document["authority_epoch"], 0)
                self.assertEqual(document["migration"]["g4_phase_closure"], expected_closure)
                self.assertEqual(document["migration"]["completed_gate"], "G6")
                self.assertEqual(
                    document["migration"]["current_gate"],
                    "G7_CUTOVER_PREPARATION",
                )
                self.assertEqual(
                    document["migration"]["current_subphase"],
                    "G7_AWAITING_FRESH_OWNER_DRIVE_FREEZE_AND_DELTA_AUTHORIZATION",
                )
                self.assertEqual(
                    document["migration"]["g6_phase_closure"]["published_commit"],
                    "663df66eefe72acfc57d47076b836e6c7c0a5a2e",
                )
        self.assertEqual(
            self.scope["before_verified_g8_activation"]["analytical_authority"],
            "GOOGLE_DRIVE",
        )
        self.assertEqual(
            self.state["analytical_authority_activation"]["status"],
            "NOT_AUTHORIZED",
        )
        self.assertEqual(
            self.binding["migration"]["current_subphase"],
            "P05_BLOCKED_PENDING_CHARACTER_SCHEMA_HARDENING",
        )

        prose = {
            "README.md": ("complete approved G5 text materialization", "Google Drive remains authoritative"),
            "governance/CHATGPT_AUTHORITY_AND_ROUTING.md": (
                "complete approved G5 text boundary is materialized",
                "Google Drive remains the analytical authority",
            ),
            "governance/MANGA_ANIME_CORPUS_INDEX.md": (
                "materialized through the approved G7 COTE delta-repair boundary",
                "Analytical authority: Google Drive",
            ),
            "governance/policies/REPOSITORY_CONTROLS.md": (
                "completed G4 representative pilots",
                "complete G5 text-boundary materialization",
            ),
            "series/README.md": (
                "complete approved G5 text materialization",
                "NONAUTHORITATIVE_PRE_G8",
            ),
            "studies/README.md": (
                "complete approved G5 text materialization",
                "nonauthoritative before G8",
            ),
        }
        for relative_path, expected_phrases in prose.items():
            text = (REPOSITORY_ROOT / relative_path).read_text(encoding="utf-8")
            for phrase in expected_phrases:
                with self.subTest(path=relative_path, phrase=phrase):
                    self.assertIn(phrase, text)
            self.assertNotIn("full corpus is complete", text.casefold())

    def test_public_activation_evidence_tuple_is_exact(self) -> None:
        publication = self.binding["repository_publication_activation"]
        self.assertEqual(
            publication["status"],
            "VERIFIED_G3_PUBLICATION_ACTIVATION",
        )
        self.assertEqual(
            publication["verification_scope"],
            "VERIFIED_AT_G3_CLOSURE_REVERIFY_BEFORE_PUBLIC_PUSH",
        )
        actual = [
            (entry["kind"], entry["sha256"])
            for entry in publication["evidence"]
        ]
        self.assertEqual(actual, ACTIVATION_EVIDENCE)
        self.assertEqual(
            self.binding["repository"]["validated_commit"],
            "e934c0a6f92ad16ba3305bd99f938aa6b3d97a1f",
        )
        self.assertEqual(
            self.binding["repository"]["validated_tree"],
            "d0bb00fa5d7a8735892921ba3c0023b4855ac52e",
        )
        raw = (
            REPOSITORY_ROOT
            / "governance/repository-controls/public-activation-bindings.json"
        ).read_text(encoding="utf-8")
        self.assertNotRegex(raw, r"(?i)(?:[a-z]:\\|/home/|/users/)")

    def test_owner_only_license_and_integrated_candidate_boundaries(self) -> None:
        repository = self.scope["repository"]
        self.assertEqual(repository["upstream_human_writers"], ["deep-blue-zero"])
        self.assertEqual(repository["external_contributions"], "NOT_ACCEPTED")
        self.assertEqual(
            repository["license_status"], "CC_BY_NC_4_0_ORIGINAL_CONTENT_ONLY"
        )
        # The G3 public-activation binding remains immutable historical evidence.
        self.assertIs(self.binding["corpus_content_included"], False)
        self.assertEqual(
            self.binding["license_status"],
            "UNLICENSED_PENDING_OWNER_DECISION",
        )
        series_registry = load_json(REPOSITORY_ROOT / "series/registry.json")
        self.assertEqual(series_registry["status"], "G7_DELTA_REPAIR_CANDIDATE")
        series_ids = [row["series_id"] for row in series_registry["series"]]
        self.assertEqual(len(series_ids), len(set(series_ids)))
        self.assertTrue(
            {
                "the-idolmaster-cinderella-girls-u149",
                "idoly-pride",
                "maebashi-witches",
                "mass-effect",
                "genshin-impact",
                "the-idolmaster-cinderella-girls-mobile-games",
                "blue-archive",
                "youjo-senki",
                "legend-of-the-galactic-heroes",
            }.issubset(set(series_ids))
        )
        series_by_id = {row["series_id"]: row for row in series_registry["series"]}
        self.assertEqual(
            series_by_id["the-idolmaster-cinderella-girls-u149"]["series_id"],
            "the-idolmaster-cinderella-girls-u149",
        )
        self.assertEqual(
            series_by_id["idoly-pride"],
            {
                "series_id": "idoly-pride",
                "stable_slug": "idoly-pride",
                "canonical_title": "IDOLY PRIDE",
                "media": ["MOBILE_GAME"],
                "repository_path": "series/idoly-pride/",
                "materialization_status": "PRESENT_REVIEWED",
                "migration_scope": "PARTIAL_G4_P02_SINGLE_LEDGER",
                "authority_status": "NONAUTHORITATIVE_PRE_G8",
            },
        )
        self.assertEqual(
            series_by_id["maebashi-witches"],
            {
                "series_id": "maebashi-witches",
                "stable_slug": "maebashi-witches",
                "canonical_title": "Maebashi Witches",
                "media": ["ANIME"],
                "repository_path": "series/maebashi-witches/",
                "materialization_status": "PRESENT_REVIEWED",
                "migration_scope": "G5_T01_V1_ANALYSIS",
                "authority_status": "NONAUTHORITATIVE_PRE_G8",
            },
        )
        self.assertEqual(
            series_by_id["mass-effect"],
            {
                "series_id": "mass-effect",
                "stable_slug": "mass-effect",
                "canonical_title": "Mass Effect",
                "media": ["GAME"],
                "repository_path": "studies/comparative-media/Mass Effect/",
                "materialization_status": "PRESENT_REVIEWED",
                "migration_scope": "G5_T02_COMPARATIVE_MEDIA_CHARACTER_MONOGRAPHS",
                "authority_status": "NONAUTHORITATIVE_PRE_G8",
            },
        )
        self.assertEqual(
            series_by_id["genshin-impact"],
            {
                "series_id": "genshin-impact",
                "stable_slug": "genshin-impact",
                "canonical_title": "Genshin Impact",
                "media": ["GAME"],
                "repository_path": "series/genshin-impact/",
                "materialization_status": "PRESENT_REVIEWED",
                "migration_scope": "G5_T03_FURINA_MONOGRAPH_V1_COMPLETE",
                "authority_status": "NONAUTHORITATIVE_PRE_G8",
            },
        )
        self.assertEqual(
            series_by_id["the-idolmaster-cinderella-girls-mobile-games"],
            {
                "series_id": "the-idolmaster-cinderella-girls-mobile-games",
                "stable_slug": "the-idolmaster-cinderella-girls-mobile-games",
                "canonical_title": "THE IDOLM@STER CINDERELLA GIRLS (Mobile Games)",
                "media": ["MOBILE_GAME"],
                "repository_path": "series/the-idolmaster-cinderella-girls-mobile-games/",
                "materialization_status": "PRESENT_REVIEWED",
                "migration_scope": "G5_T04_MOBILE_GAME_CHARACTER_MONOGRAPHS_AND_AUDITS",
                "authority_status": "NONAUTHORITATIVE_PRE_G8",
            },
        )
        self.assertEqual(
            series_by_id["blue-archive"],
            {
                "series_id": "blue-archive",
                "stable_slug": "blue-archive",
                "canonical_title": "BLUE ARCHIVE",
                "media": ["MOBILE_GAME"],
                "repository_path": "series/blue-archive/",
                "materialization_status": "PRESENT_REVIEWED",
                "migration_scope": "G5_T05_BLUE_ARCHIVE",
                "authority_status": "NONAUTHORITATIVE_PRE_G8",
            },
        )
        self.assertEqual(
            series_by_id["youjo-senki"],
            {
                "series_id": "youjo-senki",
                "stable_slug": "youjo-senki",
                "canonical_title": "YOUJO SENKI",
                "media": ["LIGHT_NOVEL"],
                "repository_path": "series/youjo-senki/",
                "materialization_status": "PRESENT_REVIEWED",
                "migration_scope": "G5_T06_V2_ANALYTICAL_CORPUS",
                "authority_status": "NONAUTHORITATIVE_PRE_G8",
            },
        )
        self.assertEqual(
            series_by_id["legend-of-the-galactic-heroes"],
            {
                "series_id": "legend-of-the-galactic-heroes",
                "stable_slug": "legend-of-the-galactic-heroes",
                "canonical_title": "Legend of the Galactic Heroes",
                "media": ["LIGHT_NOVEL"],
                "repository_path": "series/legend-of-the-galactic-heroes/",
                "materialization_status": "PRESENT_REVIEWED",
                "migration_scope": "G5_T07_LOGH_FULL_PREFIX",
                "authority_status": "NONAUTHORITATIVE_PRE_G8",
            },
        )
        character_rows = [
            json.loads(line)
            for line in (REPOSITORY_ROOT / "characters/registry.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line
        ]
        self.assertEqual(
            len(character_rows),
            len({row["analysis_subject_id"] for row in character_rows}),
        )
        subject_ids = {row["analysis_subject_id"] for row in character_rows}
        self.assertTrue(
            {
                "maebashi-witches:azu@anime",
                "maebashi-witches:choco@anime",
                "maebashi-witches:eiko@anime",
                "mass-effect:commander-shepard@paragon-player-archetype",
                "mass-effect:commander-shepard@renegade-player-archetype",
                "maebashi-witches:keroppe@anime",
                "maebashi-witches:kyouka@anime",
                "maebashi-witches:mai@anime",
                "maebashi-witches:yuina@anime",
                "the-idolmaster:yonai-p@u149-anime",
                "genshin-impact:furina@game",
                "the-idolmaster:futaba-anzu@cinderella-girls-mobile-games",
                "the-idolmaster:hayami-kanade@cinderella-girls-mobile-games",
                "the-idolmaster:hisakawa-nagi@cinderella-girls-mobile-games",
                "the-idolmaster:hojo-karen@cinderella-girls-mobile-games",
                "the-idolmaster:kanzaki-ranko@cinderella-girls-mobile-games",
                "the-idolmaster:kobayakawa-sae@cinderella-girls-mobile-games",
                "the-idolmaster:ninomiya-asuka@cinderella-girls-mobile-games",
                "the-idolmaster:nitta-minami@cinderella-girls-mobile-games",
                "the-idolmaster:takagaki-kaede@cinderella-girls-mobile-games",
                "blue-archive:aru@game",
                "blue-archive:ayane@game",
                "blue-archive:haruka@game",
                "blue-archive:hifumi@game",
                "blue-archive:hoshino@game",
                "blue-archive:kayoko@game",
                "blue-archive:mutsuki@game",
                "blue-archive:nonomi@game",
                "blue-archive:sensei@game-player-variable",
                "blue-archive:serika@game",
                "blue-archive:shiroko@game",
            }.issubset(subject_ids)
        )
        furina = next(
            row
            for row in character_rows
            if row["analysis_subject_id"] == "genshin-impact:furina@game"
        )
        self.assertEqual(furina, json.loads('{"schema_version":2,"character_entity_id":"genshin-impact:furina","analysis_subject_id":"genshin-impact:furina@game","preferred_name":"Furina","subject_label":"Genshin Impact game","series_id":"genshin-impact","franchise_id":null,"continuity_id":"genshin-impact-game","incarnation_id":null,"state_id":null,"subject_kind":"SINGLE_CONTINUITY","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"evidence":[{"evidence_id":"furina-character-monograph","repository_path":"series/genshin-impact/05 Character Monographs/GENSHIN_FURINA_CHARACTER_MONOGRAPH.md","label":"Furina character monograph","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1bdGqSGEwzlclEe9c-2OmxMKJEh_W7S_D."}],"analytical_coverage":[{"coverage_id":"furina-v1-corpus","continuity_id":"genshin-impact-game","medium":"GAME","unit":"OTHER","scope_type":"DESCRIPTIVE","evidence_ids":["furina-character-monograph"],"scope_note":"Furina V1 synthesis centered on the Fontaine Archon Quest and Furina Story Quest within the Genshin Impact 7.0.0 Tier-A corpus; this describes the reviewed source boundary and does not claim exhaustive coverage of all events or audio performance evidence."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DEDICATED","notes":"Dedicated active-provisional Furina V1 monograph; nonauthoritative before G8."}'))

        cinderella_rows = [
            row
            for row in character_rows
            if row["series_id"] == "the-idolmaster-cinderella-girls-mobile-games"
        ]
        expected_cinderella_rows = [
            json.loads('{"analysis_subject_id":"the-idolmaster:futaba-anzu@cinderella-girls-mobile-games","analytical_coverage":[{"continuity_id":"the-idolmaster-cinderella-girls-mobile-games","coverage_id":"futaba-anzu-mobile-game-corpus","evidence_ids":["futaba-anzu-mobile-game-monograph","futaba-anzu-mobile-game-monograph-audit"],"medium":"GAME","scope_note":"Integrated Mobage and Starlight Stage character analysis; Starlight Stage text is complete against the released categorized inventory, Mobage is structurally incomplete, and adaptation continuities are excluded.","scope_type":"DESCRIPTIVE","unit":"OTHER"}],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS"],"character_entity_id":"the-idolmaster:futaba-anzu","continuity_id":"the-idolmaster-cinderella-girls-mobile-games","curation_status":"INCLUDED","entity_aliases":[],"evidence":[{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS"],"evidence_id":"futaba-anzu-mobile-game-monograph","label":"Futaba Anzu mobile-game character monograph","provenance_note":"Migrated from preserved Drive object 18-s1yon5DPtKbXXHqorhmPYBec6ZTddC.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/04 Specialist Synthesis/CINDERELLA_GIRLS_FUTABA_ANZU_CHARACTER_MONOGRAPH.md","review_state":"REVIEWED"},{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS"],"evidence_id":"futaba-anzu-mobile-game-monograph-audit","label":"Futaba Anzu mobile-game monograph audit","provenance_note":"Migrated from preserved Drive object 1MTgGe0oCawT4o3_F0kDWjOb6O1cZr-Bj.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/08 Audits and Manifests/CINDERELLA_GIRLS_FUTABA_ANZU_MONOGRAPH_AUDIT.md","review_state":"REVIEWED"}],"franchise_id":"the-idolmaster","incarnation_id":null,"inclusion_basis":"DEDICATED","materialization_status":"PRESENT_REVIEWED","notes":"Dedicated active-provisional monograph with a canonical audit; nonauthoritative before G8.","preferred_name":"Futaba Anzu","schema_version":2,"series_id":"the-idolmaster-cinderella-girls-mobile-games","state_id":null,"subject_aliases":[],"subject_kind":"SINGLE_CONTINUITY","subject_label":"Cinderella Girls mobile games"}'),
            json.loads('{"analysis_subject_id":"the-idolmaster:hayami-kanade@cinderella-girls-mobile-games","analytical_coverage":[{"continuity_id":"the-idolmaster-cinderella-girls-mobile-games","coverage_id":"hayami-kanade-mobile-game-corpus","evidence_ids":["hayami-kanade-mobile-game-monograph","hayami-kanade-mobile-game-monograph-audit"],"medium":"GAME","scope_note":"Integrated Mobage and Starlight Stage character analysis; Starlight Stage text is complete against the released categorized inventory, Mobage is structurally incomplete, audio is not acquired, and adaptation continuities are excluded.","scope_type":"DESCRIPTIVE","unit":"OTHER"}],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS"],"character_entity_id":"the-idolmaster:hayami-kanade","continuity_id":"the-idolmaster-cinderella-girls-mobile-games","curation_status":"INCLUDED","entity_aliases":[],"evidence":[{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS"],"evidence_id":"hayami-kanade-mobile-game-monograph","label":"Hayami Kanade mobile-game character monograph","provenance_note":"Migrated from preserved Drive object 1Y3mMCqxWg5Ns4kYVcR8IfrvaoLpwilnS.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/04 Specialist Synthesis/CINDERELLA_GIRLS_HAYAMI_KANADE_CHARACTER_MONOGRAPH.md","review_state":"REVIEWED"},{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS"],"evidence_id":"hayami-kanade-mobile-game-monograph-audit","label":"Hayami Kanade mobile-game monograph audit","provenance_note":"Migrated from preserved Drive object 1lOUMW_pkSgvsdRIQEWWRH1-mLXwzIhir.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/08 Audits and Manifests/CINDERELLA_GIRLS_HAYAMI_KANADE_MONOGRAPH_AUDIT.md","review_state":"REVIEWED"}],"franchise_id":"the-idolmaster","incarnation_id":null,"inclusion_basis":"DEDICATED","materialization_status":"PRESENT_REVIEWED","notes":"Dedicated active-provisional monograph with a canonical audit; nonauthoritative before G8.","preferred_name":"Hayami Kanade","schema_version":2,"series_id":"the-idolmaster-cinderella-girls-mobile-games","state_id":null,"subject_aliases":[],"subject_kind":"SINGLE_CONTINUITY","subject_label":"Cinderella Girls mobile games"}'),
            json.loads('{"analysis_subject_id":"the-idolmaster:hisakawa-nagi@cinderella-girls-mobile-games","analytical_coverage":[{"continuity_id":"the-idolmaster-cinderella-girls-mobile-games","coverage_id":"hisakawa-nagi-mobile-game-corpus","evidence_ids":["hisakawa-nagi-mobile-game-monograph","hisakawa-nagi-mobile-game-monograph-audit"],"medium":"GAME","scope_note":"Integrated Mobage and Starlight Stage character analysis; Starlight Stage text is complete against the released categorized inventory, Mobage is structurally incomplete, audio is not acquired, and adaptation continuities are excluded.","scope_type":"DESCRIPTIVE","unit":"OTHER"}],"analytical_dimensions":["PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"character_entity_id":"the-idolmaster:hisakawa-nagi","continuity_id":"the-idolmaster-cinderella-girls-mobile-games","curation_status":"INCLUDED","entity_aliases":[],"evidence":[{"anchor":null,"dimensions":["PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"evidence_id":"hisakawa-nagi-mobile-game-monograph","label":"Hisakawa Nagi mobile-game character monograph","provenance_note":"Migrated from preserved Drive object 12M6Vdyr0-_KLTpbwQJbIPpgWz1I8viQv.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/04 Specialist Synthesis/CINDERELLA_GIRLS_HISAKAWA_NAGI_CHARACTER_MONOGRAPH.md","review_state":"REVIEWED"},{"anchor":null,"dimensions":["PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"evidence_id":"hisakawa-nagi-mobile-game-monograph-audit","label":"Hisakawa Nagi mobile-game monograph audit","provenance_note":"Migrated from preserved Drive object 1iCw-5cBB-glP9hyDVOE6OlS4Py9oUclK.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/08 Audits and Manifests/CINDERELLA_GIRLS_HISAKAWA_NAGI_MONOGRAPH_AUDIT.md","review_state":"REVIEWED"}],"franchise_id":"the-idolmaster","incarnation_id":null,"inclusion_basis":"DEDICATED","materialization_status":"PRESENT_REVIEWED","notes":"Dedicated active-provisional monograph with a canonical audit; nonauthoritative before G8.","preferred_name":"Hisakawa Nagi","schema_version":2,"series_id":"the-idolmaster-cinderella-girls-mobile-games","state_id":null,"subject_aliases":[],"subject_kind":"SINGLE_CONTINUITY","subject_label":"Cinderella Girls mobile games"}'),
            json.loads('{"analysis_subject_id":"the-idolmaster:hojo-karen@cinderella-girls-mobile-games","analytical_coverage":[{"continuity_id":"the-idolmaster-cinderella-girls-mobile-games","coverage_id":"hojo-karen-mobile-game-corpus","evidence_ids":["hojo-karen-mobile-game-monograph","hojo-karen-mobile-game-monograph-audit"],"medium":"GAME","scope_note":"Integrated Mobage and Starlight Stage character analysis; Starlight Stage text is complete against the released categorized inventory, Mobage is structurally incomplete, audio is representative only, and adaptation continuities are excluded.","scope_type":"DESCRIPTIVE","unit":"OTHER"}],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"character_entity_id":"the-idolmaster:hojo-karen","continuity_id":"the-idolmaster-cinderella-girls-mobile-games","curation_status":"INCLUDED","entity_aliases":[],"evidence":[{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"evidence_id":"hojo-karen-mobile-game-monograph","label":"Hojo Karen mobile-game character monograph","provenance_note":"Migrated from preserved Drive object 1OTt8FEMAUy-efBDeCpTOgOm7m_NJ06bA.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/04 Specialist Synthesis/CINDERELLA_GIRLS_HOJO_KAREN_CHARACTER_MONOGRAPH.md","review_state":"REVIEWED"},{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"evidence_id":"hojo-karen-mobile-game-monograph-audit","label":"Hojo Karen mobile-game monograph audit","provenance_note":"Migrated from preserved Drive object 1FnVGaeDGKkjqy3sp_NDwM3PY9VJo7HB1.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/08 Audits and Manifests/CINDERELLA_GIRLS_HOJO_KAREN_MONOGRAPH_AUDIT.md","review_state":"REVIEWED"}],"franchise_id":"the-idolmaster","incarnation_id":null,"inclusion_basis":"DEDICATED","materialization_status":"PRESENT_REVIEWED","notes":"Dedicated active-provisional monograph with a canonical audit; nonauthoritative before G8.","preferred_name":"Hojo Karen","schema_version":2,"series_id":"the-idolmaster-cinderella-girls-mobile-games","state_id":null,"subject_aliases":[],"subject_kind":"SINGLE_CONTINUITY","subject_label":"Cinderella Girls mobile games"}'),
            json.loads('{"analysis_subject_id":"the-idolmaster:kanzaki-ranko@cinderella-girls-mobile-games","analytical_coverage":[{"continuity_id":"the-idolmaster-cinderella-girls-mobile-games","coverage_id":"kanzaki-ranko-mobile-game-corpus","evidence_ids":["kanzaki-ranko-mobile-game-monograph","kanzaki-ranko-mobile-game-monograph-audit"],"medium":"GAME","scope_note":"Integrated Mobage and Starlight Stage character analysis; Starlight Stage text is complete against the released categorized inventory, Mobage is structurally incomplete, audio is representative only, and adaptation continuities are excluded.","scope_type":"DESCRIPTIVE","unit":"OTHER"}],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS"],"character_entity_id":"the-idolmaster:kanzaki-ranko","continuity_id":"the-idolmaster-cinderella-girls-mobile-games","curation_status":"INCLUDED","entity_aliases":[],"evidence":[{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS"],"evidence_id":"kanzaki-ranko-mobile-game-monograph","label":"Kanzaki Ranko mobile-game character monograph","provenance_note":"Migrated from preserved Drive object 1CFghwDnA-7gR1rNT_Fghvliu2Pvo5NOg.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/04 Specialist Synthesis/CINDERELLA_GIRLS_KANZAKI_RANKO_CHARACTER_MONOGRAPH.md","review_state":"REVIEWED"},{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS"],"evidence_id":"kanzaki-ranko-mobile-game-monograph-audit","label":"Kanzaki Ranko mobile-game monograph audit","provenance_note":"Migrated from preserved Drive object 1Dd-tkAaW3Ld1ac04kdNvBaRXCH-JvKPF.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/08 Audits and Manifests/CINDERELLA_GIRLS_KANZAKI_RANKO_MONOGRAPH_AUDIT.md","review_state":"REVIEWED"}],"franchise_id":"the-idolmaster","incarnation_id":null,"inclusion_basis":"DEDICATED","materialization_status":"PRESENT_REVIEWED","notes":"Dedicated active-provisional monograph with a canonical audit; nonauthoritative before G8.","preferred_name":"Kanzaki Ranko","schema_version":2,"series_id":"the-idolmaster-cinderella-girls-mobile-games","state_id":null,"subject_aliases":[],"subject_kind":"SINGLE_CONTINUITY","subject_label":"Cinderella Girls mobile games"}'),
            json.loads('{"analysis_subject_id":"the-idolmaster:kobayakawa-sae@cinderella-girls-mobile-games","analytical_coverage":[{"continuity_id":"the-idolmaster-cinderella-girls-mobile-games","coverage_id":"kobayakawa-sae-mobile-game-corpus","evidence_ids":["kobayakawa-sae-mobile-game-monograph","kobayakawa-sae-mobile-game-monograph-audit"],"medium":"GAME","scope_note":"Integrated Mobage and Starlight Stage character analysis; Starlight Stage text is complete against the released categorized inventory, Mobage is structurally incomplete, audio is not acquired, and adaptation continuities are excluded.","scope_type":"DESCRIPTIVE","unit":"OTHER"}],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"character_entity_id":"the-idolmaster:kobayakawa-sae","continuity_id":"the-idolmaster-cinderella-girls-mobile-games","curation_status":"INCLUDED","entity_aliases":[],"evidence":[{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"evidence_id":"kobayakawa-sae-mobile-game-monograph","label":"Kobayakawa Sae mobile-game character monograph","provenance_note":"Migrated from preserved Drive object 1UchaatRPIc9BoxbXj-hvLGZajqvQ2NaY.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/04 Specialist Synthesis/CINDERELLA_GIRLS_KOBAYAKAWA_SAE_CHARACTER_MONOGRAPH.md","review_state":"REVIEWED"},{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"evidence_id":"kobayakawa-sae-mobile-game-monograph-audit","label":"Kobayakawa Sae mobile-game monograph audit","provenance_note":"Migrated from preserved Drive object 1AyXAE4uJ7QftjNAKl7RT7-jkmtpr9ng8.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/08 Audits and Manifests/CINDERELLA_GIRLS_KOBAYAKAWA_SAE_MONOGRAPH_AUDIT.md","review_state":"REVIEWED"}],"franchise_id":"the-idolmaster","incarnation_id":null,"inclusion_basis":"DEDICATED","materialization_status":"PRESENT_REVIEWED","notes":"Dedicated active-provisional monograph with a canonical audit; nonauthoritative before G8.","preferred_name":"Kobayakawa Sae","schema_version":2,"series_id":"the-idolmaster-cinderella-girls-mobile-games","state_id":null,"subject_aliases":[],"subject_kind":"SINGLE_CONTINUITY","subject_label":"Cinderella Girls mobile games"}'),
            json.loads('{"analysis_subject_id":"the-idolmaster:ninomiya-asuka@cinderella-girls-mobile-games","analytical_coverage":[{"continuity_id":"the-idolmaster-cinderella-girls-mobile-games","coverage_id":"ninomiya-asuka-mobile-game-corpus","evidence_ids":["ninomiya-asuka-mobile-game-monograph","ninomiya-asuka-mobile-game-monograph-audit"],"medium":"GAME","scope_note":"Integrated Mobage and Starlight Stage character analysis; Starlight Stage text is complete against the released categorized inventory, Mobage is structurally incomplete, audio is representative only, and adaptation continuities are excluded.","scope_type":"DESCRIPTIVE","unit":"OTHER"}],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","IDEOLOGY"],"character_entity_id":"the-idolmaster:ninomiya-asuka","continuity_id":"the-idolmaster-cinderella-girls-mobile-games","curation_status":"INCLUDED","entity_aliases":[],"evidence":[{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","IDEOLOGY"],"evidence_id":"ninomiya-asuka-mobile-game-monograph","label":"Ninomiya Asuka mobile-game character monograph","provenance_note":"Migrated from preserved Drive object 1Hg3BXJsk-e9zvar8vSOde3hgFsBwkiYX.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/04 Specialist Synthesis/CINDERELLA_GIRLS_NINOMIYA_ASUKA_CHARACTER_MONOGRAPH.md","review_state":"REVIEWED"},{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","IDEOLOGY"],"evidence_id":"ninomiya-asuka-mobile-game-monograph-audit","label":"Ninomiya Asuka mobile-game monograph audit","provenance_note":"Migrated from preserved Drive object 1EFxZFX9F4GVXowXEx5gug9c7FqXlEZT4.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/08 Audits and Manifests/CINDERELLA_GIRLS_NINOMIYA_ASUKA_MONOGRAPH_AUDIT.md","review_state":"REVIEWED"}],"franchise_id":"the-idolmaster","incarnation_id":null,"inclusion_basis":"DEDICATED","materialization_status":"PRESENT_REVIEWED","notes":"Dedicated active-provisional monograph with a canonical audit; nonauthoritative before G8.","preferred_name":"Ninomiya Asuka","schema_version":2,"series_id":"the-idolmaster-cinderella-girls-mobile-games","state_id":null,"subject_aliases":[],"subject_kind":"SINGLE_CONTINUITY","subject_label":"Cinderella Girls mobile games"}'),
            json.loads('{"analysis_subject_id":"the-idolmaster:nitta-minami@cinderella-girls-mobile-games","analytical_coverage":[{"continuity_id":"the-idolmaster-cinderella-girls-mobile-games","coverage_id":"nitta-minami-mobile-game-corpus","evidence_ids":["nitta-minami-mobile-game-monograph","nitta-minami-mobile-game-monograph-audit"],"medium":"GAME","scope_note":"Integrated Mobage and Starlight Stage character analysis; Starlight Stage text is complete against the released categorized inventory, Mobage is structurally incomplete, audio is representative only, and adaptation continuities are excluded.","scope_type":"DESCRIPTIVE","unit":"OTHER"}],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"character_entity_id":"the-idolmaster:nitta-minami","continuity_id":"the-idolmaster-cinderella-girls-mobile-games","curation_status":"INCLUDED","entity_aliases":[],"evidence":[{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"evidence_id":"nitta-minami-mobile-game-monograph","label":"Nitta Minami mobile-game character monograph","provenance_note":"Migrated from preserved Drive object 16_uez2i4Qdq5GepkWF0uO24qjMlJB9V_.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/04 Specialist Synthesis/CINDERELLA_GIRLS_NITTA_MINAMI_CHARACTER_MONOGRAPH.md","review_state":"REVIEWED"},{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"evidence_id":"nitta-minami-mobile-game-monograph-audit","label":"Nitta Minami mobile-game monograph audit","provenance_note":"Migrated from preserved Drive object 1Tno1Y_-ipFuokgTbHjJpc_qDvIyzA8i8.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/08 Audits and Manifests/CINDERELLA_GIRLS_NITTA_MINAMI_MONOGRAPH_AUDIT.md","review_state":"REVIEWED"}],"franchise_id":"the-idolmaster","incarnation_id":null,"inclusion_basis":"DEDICATED","materialization_status":"PRESENT_REVIEWED","notes":"Dedicated active-provisional monograph with a canonical audit; nonauthoritative before G8.","preferred_name":"Nitta Minami","schema_version":2,"series_id":"the-idolmaster-cinderella-girls-mobile-games","state_id":null,"subject_aliases":[],"subject_kind":"SINGLE_CONTINUITY","subject_label":"Cinderella Girls mobile games"}'),
            json.loads('{"analysis_subject_id":"the-idolmaster:takagaki-kaede@cinderella-girls-mobile-games","analytical_coverage":[{"continuity_id":"the-idolmaster-cinderella-girls-mobile-games","coverage_id":"takagaki-kaede-mobile-game-corpus","evidence_ids":["takagaki-kaede-mobile-game-monograph","takagaki-kaede-mobile-game-monograph-audit"],"medium":"GAME","scope_note":"Integrated Mobage and Starlight Stage character analysis; Starlight Stage text is complete against the released categorized inventory, Mobage is structurally incomplete, audio is representative only, and the 2015 television anime is excluded.","scope_type":"DESCRIPTIVE","unit":"OTHER"}],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"character_entity_id":"the-idolmaster:takagaki-kaede","continuity_id":"the-idolmaster-cinderella-girls-mobile-games","curation_status":"INCLUDED","entity_aliases":[],"evidence":[{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"evidence_id":"takagaki-kaede-mobile-game-monograph","label":"Takagaki Kaede mobile-game character monograph","provenance_note":"Migrated from preserved Drive object 1hDBbqyhsVOV3l54F66RhksX4SRXlPdjH.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/04 Specialist Synthesis/CINDERELLA_GIRLS_TAKAGAKI_KAEDE_CHARACTER_MONOGRAPH.md","review_state":"REVIEWED"},{"anchor":null,"dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"evidence_id":"takagaki-kaede-mobile-game-monograph-audit","label":"Takagaki Kaede mobile-game monograph audit","provenance_note":"Migrated from preserved Drive object 1uLlBexjsm8KKfa87c4zm8dcohgRnh8XE.","repository_path":"series/the-idolmaster-cinderella-girls-mobile-games/08 Audits and Manifests/CINDERELLA_GIRLS_TAKAGAKI_KAEDE_MONOGRAPH_AUDIT.md","review_state":"REVIEWED"}],"franchise_id":"the-idolmaster","incarnation_id":null,"inclusion_basis":"DEDICATED","materialization_status":"PRESENT_REVIEWED","notes":"Dedicated active-provisional monograph with a canonical audit; nonauthoritative before G8.","preferred_name":"Takagaki Kaede","schema_version":2,"series_id":"the-idolmaster-cinderella-girls-mobile-games","state_id":null,"subject_aliases":[],"subject_kind":"SINGLE_CONTINUITY","subject_label":"Cinderella Girls mobile games"}'),
        ]
        self.assertEqual(cinderella_rows, expected_cinderella_rows)

        blue_archive_rows = [
            row for row in character_rows if row["series_id"] == "blue-archive"
        ]
        expected_blue_archive_rows = [
            json.loads('{"schema_version":2,"character_entity_id":"blue-archive:aru","analysis_subject_id":"blue-archive:aru@game","preferred_name":"Aru","subject_label":"Blue Archive game","series_id":"blue-archive","franchise_id":null,"continuity_id":"blue-archive-game","incarnation_id":null,"state_id":null,"subject_kind":"SINGLE_CONTINUITY","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"evidence":[{"evidence_id":"chapter-1-checkpoint","repository_path":"series/blue-archive/02 Sequential Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md","label":"Countermeasures Committee Arc Chapter 1 canonical checkpoint","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1wgWdlnyNZL2cJez3cqbc961oSOETaxh2."},{"evidence_id":"character-state-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md","label":"Cumulative character-state ledger","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1E3LNlVElRpUft52mXGcW7dHhm7jQLqg9."},{"evidence_id":"voice-address-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md","label":"Cumulative Japanese voice and address ledger","anchor":null,"review_state":"REVIEWED","dimensions":["SPEECH"],"provenance_note":"Migrated from preserved Drive object 1u6GTcT3h4Lum0GBtQTHO1JdvrJLtXLsE."}],"analytical_coverage":[{"coverage_id":"aru-chapter-1-corpus","continuity_id":"blue-archive-game","medium":"GAME","unit":"STORY_CHAPTER","scope_type":"DESCRIPTIVE","evidence_ids":["chapter-1-checkpoint","character-state-ledger","voice-address-ledger"],"scope_note":"Reviewed distributed analysis within the Blue Archive Countermeasures Committee Arc, Volume 1 Chapter 1 through E020; this describes the current analytical boundary and does not claim coverage in every unit or full-game, event-story, MomoTalk, or exhaustive character-story coverage."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DISTRIBUTED_SUBSTANTIAL","notes":"Substantial distributed sequential and longitudinal analysis through the Chapter 1 checkpoint; no dedicated character monograph is claimed; nonauthoritative before G8."}'),
            json.loads('{"schema_version":2,"character_entity_id":"blue-archive:ayane","analysis_subject_id":"blue-archive:ayane@game","preferred_name":"Ayane","subject_label":"Blue Archive game","series_id":"blue-archive","franchise_id":null,"continuity_id":"blue-archive-game","incarnation_id":null,"state_id":null,"subject_kind":"SINGLE_CONTINUITY","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","SPEECH","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"evidence":[{"evidence_id":"chapter-1-checkpoint","repository_path":"series/blue-archive/02 Sequential Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md","label":"Countermeasures Committee Arc Chapter 1 canonical checkpoint","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1wgWdlnyNZL2cJez3cqbc961oSOETaxh2."},{"evidence_id":"character-state-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md","label":"Cumulative character-state ledger","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1E3LNlVElRpUft52mXGcW7dHhm7jQLqg9."},{"evidence_id":"voice-address-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md","label":"Cumulative Japanese voice and address ledger","anchor":null,"review_state":"REVIEWED","dimensions":["SPEECH"],"provenance_note":"Migrated from preserved Drive object 1u6GTcT3h4Lum0GBtQTHO1JdvrJLtXLsE."}],"analytical_coverage":[{"coverage_id":"ayane-chapter-1-corpus","continuity_id":"blue-archive-game","medium":"GAME","unit":"STORY_CHAPTER","scope_type":"DESCRIPTIVE","evidence_ids":["chapter-1-checkpoint","character-state-ledger","voice-address-ledger"],"scope_note":"Reviewed distributed analysis within the Blue Archive Countermeasures Committee Arc, Volume 1 Chapter 1 through E020; this describes the current analytical boundary and does not claim coverage in every unit or full-game, event-story, MomoTalk, or exhaustive character-story coverage."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DISTRIBUTED_SUBSTANTIAL","notes":"Substantial distributed sequential and longitudinal analysis through the Chapter 1 checkpoint; no dedicated character monograph is claimed; nonauthoritative before G8."}'),
            json.loads('{"schema_version":2,"character_entity_id":"blue-archive:haruka","analysis_subject_id":"blue-archive:haruka@game","preferred_name":"Haruka","subject_label":"Blue Archive game","series_id":"blue-archive","franchise_id":null,"continuity_id":"blue-archive-game","incarnation_id":null,"state_id":null,"subject_kind":"SINGLE_CONTINUITY","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"evidence":[{"evidence_id":"chapter-1-checkpoint","repository_path":"series/blue-archive/02 Sequential Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md","label":"Countermeasures Committee Arc Chapter 1 canonical checkpoint","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1wgWdlnyNZL2cJez3cqbc961oSOETaxh2."},{"evidence_id":"character-state-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md","label":"Cumulative character-state ledger","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1E3LNlVElRpUft52mXGcW7dHhm7jQLqg9."},{"evidence_id":"voice-address-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md","label":"Cumulative Japanese voice and address ledger","anchor":null,"review_state":"REVIEWED","dimensions":["SPEECH"],"provenance_note":"Migrated from preserved Drive object 1u6GTcT3h4Lum0GBtQTHO1JdvrJLtXLsE."}],"analytical_coverage":[{"coverage_id":"haruka-chapter-1-corpus","continuity_id":"blue-archive-game","medium":"GAME","unit":"STORY_CHAPTER","scope_type":"DESCRIPTIVE","evidence_ids":["chapter-1-checkpoint","character-state-ledger","voice-address-ledger"],"scope_note":"Reviewed distributed analysis within the Blue Archive Countermeasures Committee Arc, Volume 1 Chapter 1 through E020; this describes the current analytical boundary and does not claim coverage in every unit or full-game, event-story, MomoTalk, or exhaustive character-story coverage."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DISTRIBUTED_SUBSTANTIAL","notes":"Substantial distributed sequential and longitudinal analysis through the Chapter 1 checkpoint; no dedicated character monograph is claimed; nonauthoritative before G8."}'),
            json.loads('{"schema_version":2,"character_entity_id":"blue-archive:hifumi","analysis_subject_id":"blue-archive:hifumi@game","preferred_name":"Hifumi","subject_label":"Blue Archive game","series_id":"blue-archive","franchise_id":null,"continuity_id":"blue-archive-game","incarnation_id":null,"state_id":null,"subject_kind":"SINGLE_CONTINUITY","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"evidence":[{"evidence_id":"chapter-1-checkpoint","repository_path":"series/blue-archive/02 Sequential Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md","label":"Countermeasures Committee Arc Chapter 1 canonical checkpoint","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1wgWdlnyNZL2cJez3cqbc961oSOETaxh2."},{"evidence_id":"character-state-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md","label":"Cumulative character-state ledger","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1E3LNlVElRpUft52mXGcW7dHhm7jQLqg9."},{"evidence_id":"voice-address-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md","label":"Cumulative Japanese voice and address ledger","anchor":null,"review_state":"REVIEWED","dimensions":["SPEECH"],"provenance_note":"Migrated from preserved Drive object 1u6GTcT3h4Lum0GBtQTHO1JdvrJLtXLsE."}],"analytical_coverage":[{"coverage_id":"hifumi-chapter-1-corpus","continuity_id":"blue-archive-game","medium":"GAME","unit":"STORY_CHAPTER","scope_type":"DESCRIPTIVE","evidence_ids":["chapter-1-checkpoint","character-state-ledger","voice-address-ledger"],"scope_note":"Reviewed distributed analysis within the Blue Archive Countermeasures Committee Arc, Volume 1 Chapter 1 through E020; this describes the current analytical boundary and does not claim coverage in every unit or full-game, event-story, MomoTalk, or exhaustive character-story coverage."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DISTRIBUTED_SUBSTANTIAL","notes":"Substantial distributed sequential and longitudinal analysis through the Chapter 1 checkpoint; no dedicated character monograph is claimed; nonauthoritative before G8."}'),
            json.loads('{"schema_version":2,"character_entity_id":"blue-archive:hoshino","analysis_subject_id":"blue-archive:hoshino@game","preferred_name":"Hoshino","subject_label":"Blue Archive game","series_id":"blue-archive","franchise_id":null,"continuity_id":"blue-archive-game","incarnation_id":null,"state_id":null,"subject_kind":"SINGLE_CONTINUITY","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"evidence":[{"evidence_id":"chapter-1-checkpoint","repository_path":"series/blue-archive/02 Sequential Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md","label":"Countermeasures Committee Arc Chapter 1 canonical checkpoint","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1wgWdlnyNZL2cJez3cqbc961oSOETaxh2."},{"evidence_id":"character-state-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md","label":"Cumulative character-state ledger","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1E3LNlVElRpUft52mXGcW7dHhm7jQLqg9."},{"evidence_id":"voice-address-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md","label":"Cumulative Japanese voice and address ledger","anchor":null,"review_state":"REVIEWED","dimensions":["SPEECH"],"provenance_note":"Migrated from preserved Drive object 1u6GTcT3h4Lum0GBtQTHO1JdvrJLtXLsE."}],"analytical_coverage":[{"coverage_id":"hoshino-chapter-1-corpus","continuity_id":"blue-archive-game","medium":"GAME","unit":"STORY_CHAPTER","scope_type":"DESCRIPTIVE","evidence_ids":["chapter-1-checkpoint","character-state-ledger","voice-address-ledger"],"scope_note":"Reviewed distributed analysis within the Blue Archive Countermeasures Committee Arc, Volume 1 Chapter 1 through E020; this describes the current analytical boundary and does not claim coverage in every unit or full-game, event-story, MomoTalk, or exhaustive character-story coverage."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DISTRIBUTED_SUBSTANTIAL","notes":"Substantial distributed sequential and longitudinal analysis through the Chapter 1 checkpoint; no dedicated character monograph is claimed; nonauthoritative before G8."}'),
            json.loads('{"schema_version":2,"character_entity_id":"blue-archive:kayoko","analysis_subject_id":"blue-archive:kayoko@game","preferred_name":"Kayoko","subject_label":"Blue Archive game","series_id":"blue-archive","franchise_id":null,"continuity_id":"blue-archive-game","incarnation_id":null,"state_id":null,"subject_kind":"SINGLE_CONTINUITY","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"evidence":[{"evidence_id":"chapter-1-checkpoint","repository_path":"series/blue-archive/02 Sequential Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md","label":"Countermeasures Committee Arc Chapter 1 canonical checkpoint","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1wgWdlnyNZL2cJez3cqbc961oSOETaxh2."},{"evidence_id":"character-state-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md","label":"Cumulative character-state ledger","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1E3LNlVElRpUft52mXGcW7dHhm7jQLqg9."},{"evidence_id":"voice-address-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md","label":"Cumulative Japanese voice and address ledger","anchor":null,"review_state":"REVIEWED","dimensions":["SPEECH"],"provenance_note":"Migrated from preserved Drive object 1u6GTcT3h4Lum0GBtQTHO1JdvrJLtXLsE."}],"analytical_coverage":[{"coverage_id":"kayoko-chapter-1-corpus","continuity_id":"blue-archive-game","medium":"GAME","unit":"STORY_CHAPTER","scope_type":"DESCRIPTIVE","evidence_ids":["chapter-1-checkpoint","character-state-ledger","voice-address-ledger"],"scope_note":"Reviewed distributed analysis within the Blue Archive Countermeasures Committee Arc, Volume 1 Chapter 1 through E020; this describes the current analytical boundary and does not claim coverage in every unit or full-game, event-story, MomoTalk, or exhaustive character-story coverage."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DISTRIBUTED_SUBSTANTIAL","notes":"Substantial distributed sequential and longitudinal analysis through the Chapter 1 checkpoint; no dedicated character monograph is claimed; nonauthoritative before G8."}'),
            json.loads('{"schema_version":2,"character_entity_id":"blue-archive:mutsuki","analysis_subject_id":"blue-archive:mutsuki@game","preferred_name":"Mutsuki","subject_label":"Blue Archive game","series_id":"blue-archive","franchise_id":null,"continuity_id":"blue-archive-game","incarnation_id":null,"state_id":null,"subject_kind":"SINGLE_CONTINUITY","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","RELATIONSHIPS","DECISION_MAKING"],"evidence":[{"evidence_id":"chapter-1-checkpoint","repository_path":"series/blue-archive/02 Sequential Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md","label":"Countermeasures Committee Arc Chapter 1 canonical checkpoint","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","RELATIONSHIPS","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1wgWdlnyNZL2cJez3cqbc961oSOETaxh2."},{"evidence_id":"character-state-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md","label":"Cumulative character-state ledger","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","RELATIONSHIPS","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1E3LNlVElRpUft52mXGcW7dHhm7jQLqg9."},{"evidence_id":"voice-address-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md","label":"Cumulative Japanese voice and address ledger","anchor":null,"review_state":"REVIEWED","dimensions":["SPEECH"],"provenance_note":"Migrated from preserved Drive object 1u6GTcT3h4Lum0GBtQTHO1JdvrJLtXLsE."}],"analytical_coverage":[{"coverage_id":"mutsuki-chapter-1-corpus","continuity_id":"blue-archive-game","medium":"GAME","unit":"STORY_CHAPTER","scope_type":"DESCRIPTIVE","evidence_ids":["chapter-1-checkpoint","character-state-ledger","voice-address-ledger"],"scope_note":"Reviewed distributed analysis within the Blue Archive Countermeasures Committee Arc, Volume 1 Chapter 1 through E020; this describes the current analytical boundary and does not claim coverage in every unit or full-game, event-story, MomoTalk, or exhaustive character-story coverage."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DISTRIBUTED_SUBSTANTIAL","notes":"Substantial distributed sequential and longitudinal analysis through the Chapter 1 checkpoint; no dedicated character monograph is claimed; nonauthoritative before G8."}'),
            json.loads('{"schema_version":2,"character_entity_id":"blue-archive:nonomi","analysis_subject_id":"blue-archive:nonomi@game","preferred_name":"Nonomi","subject_label":"Blue Archive game","series_id":"blue-archive","franchise_id":null,"continuity_id":"blue-archive-game","incarnation_id":null,"state_id":null,"subject_kind":"SINGLE_CONTINUITY","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"evidence":[{"evidence_id":"chapter-1-checkpoint","repository_path":"series/blue-archive/02 Sequential Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md","label":"Countermeasures Committee Arc Chapter 1 canonical checkpoint","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1wgWdlnyNZL2cJez3cqbc961oSOETaxh2."},{"evidence_id":"character-state-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md","label":"Cumulative character-state ledger","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1E3LNlVElRpUft52mXGcW7dHhm7jQLqg9."},{"evidence_id":"voice-address-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md","label":"Cumulative Japanese voice and address ledger","anchor":null,"review_state":"REVIEWED","dimensions":["SPEECH"],"provenance_note":"Migrated from preserved Drive object 1u6GTcT3h4Lum0GBtQTHO1JdvrJLtXLsE."}],"analytical_coverage":[{"coverage_id":"nonomi-chapter-1-corpus","continuity_id":"blue-archive-game","medium":"GAME","unit":"STORY_CHAPTER","scope_type":"DESCRIPTIVE","evidence_ids":["chapter-1-checkpoint","character-state-ledger","voice-address-ledger"],"scope_note":"Reviewed distributed analysis within the Blue Archive Countermeasures Committee Arc, Volume 1 Chapter 1 through E020; this describes the current analytical boundary and does not claim coverage in every unit or full-game, event-story, MomoTalk, or exhaustive character-story coverage."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DISTRIBUTED_SUBSTANTIAL","notes":"Substantial distributed sequential and longitudinal analysis through the Chapter 1 checkpoint; no dedicated character monograph is claimed; nonauthoritative before G8."}'),
            json.loads('{"schema_version":2,"character_entity_id":"blue-archive:sensei","analysis_subject_id":"blue-archive:sensei@game-player-variable","preferred_name":"Sensei","subject_label":"Blue Archive game player-variable Sensei","series_id":"blue-archive","franchise_id":null,"continuity_id":"blue-archive-game","incarnation_id":null,"state_id":"player-variable","subject_kind":"PLAYER_ARCHETYPE","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","SPEECH","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"evidence":[{"evidence_id":"chapter-1-checkpoint","repository_path":"series/blue-archive/02 Sequential Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md","label":"Countermeasures Committee Arc Chapter 1 canonical checkpoint","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1wgWdlnyNZL2cJez3cqbc961oSOETaxh2."},{"evidence_id":"sensei-role-ethics-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_SENSEI_ROLE_AND_ETHICS_LEDGER.md","label":"Cumulative Sensei role and ethics ledger","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","SPEECH","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1JzZLF6xyNyhHPpEA9nRzp92f4_uGDs-e."}],"analytical_coverage":[{"coverage_id":"sensei-prologue-chapter-1-corpus","continuity_id":"blue-archive-game","medium":"GAME","unit":"STORY_CHAPTER","scope_type":"DESCRIPTIVE","evidence_ids":["chapter-1-checkpoint","sensei-role-ethics-ledger"],"scope_note":"Reviewed distributed analysis across the Blue Archive main-story Prologue and Countermeasures Committee Arc, Volume 1 Chapter 1 through E020; this describes the current analytical boundary and does not claim coverage in every unit or full-game, event-story, MomoTalk, or exhaustive character-story coverage."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DISTRIBUTED_SUBSTANTIAL","notes":"Substantial distributed sequential and longitudinal analysis through the Chapter 1 checkpoint; no dedicated character monograph is claimed; nonauthoritative before G8."}'),
            json.loads('{"schema_version":2,"character_entity_id":"blue-archive:serika","analysis_subject_id":"blue-archive:serika@game","preferred_name":"Serika","subject_label":"Blue Archive game","series_id":"blue-archive","franchise_id":null,"continuity_id":"blue-archive-game","incarnation_id":null,"state_id":null,"subject_kind":"SINGLE_CONTINUITY","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"evidence":[{"evidence_id":"chapter-1-checkpoint","repository_path":"series/blue-archive/02 Sequential Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md","label":"Countermeasures Committee Arc Chapter 1 canonical checkpoint","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1wgWdlnyNZL2cJez3cqbc961oSOETaxh2."},{"evidence_id":"character-state-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md","label":"Cumulative character-state ledger","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","IDEOLOGY","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1E3LNlVElRpUft52mXGcW7dHhm7jQLqg9."},{"evidence_id":"voice-address-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md","label":"Cumulative Japanese voice and address ledger","anchor":null,"review_state":"REVIEWED","dimensions":["SPEECH"],"provenance_note":"Migrated from preserved Drive object 1u6GTcT3h4Lum0GBtQTHO1JdvrJLtXLsE."}],"analytical_coverage":[{"coverage_id":"serika-chapter-1-corpus","continuity_id":"blue-archive-game","medium":"GAME","unit":"STORY_CHAPTER","scope_type":"DESCRIPTIVE","evidence_ids":["chapter-1-checkpoint","character-state-ledger","voice-address-ledger"],"scope_note":"Reviewed distributed analysis within the Blue Archive Countermeasures Committee Arc, Volume 1 Chapter 1 through E020; this describes the current analytical boundary and does not claim coverage in every unit or full-game, event-story, MomoTalk, or exhaustive character-story coverage."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DISTRIBUTED_SUBSTANTIAL","notes":"Substantial distributed sequential and longitudinal analysis through the Chapter 1 checkpoint; no dedicated character monograph is claimed; nonauthoritative before G8."}'),
            json.loads('{"schema_version":2,"character_entity_id":"blue-archive:shiroko","analysis_subject_id":"blue-archive:shiroko@game","preferred_name":"Shiroko","subject_label":"Blue Archive game","series_id":"blue-archive","franchise_id":null,"continuity_id":"blue-archive-game","incarnation_id":null,"state_id":null,"subject_kind":"SINGLE_CONTINUITY","entity_aliases":[],"subject_aliases":[],"analytical_dimensions":["BEHAVIOR","PSYCHOLOGY","SPEECH","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"evidence":[{"evidence_id":"chapter-1-checkpoint","repository_path":"series/blue-archive/02 Sequential Readings/MAIN/VOLUME_001_対策委員会編/BLUE_ARCHIVE_MAIN_V001_C001_CHECKPOINT.md","label":"Countermeasures Committee Arc Chapter 1 canonical checkpoint","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1wgWdlnyNZL2cJez3cqbc961oSOETaxh2."},{"evidence_id":"character-state-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_CHARACTER_STATE_LEDGER.md","label":"Cumulative character-state ledger","anchor":null,"review_state":"REVIEWED","dimensions":["BEHAVIOR","PSYCHOLOGY","ETHICS","RELATIONSHIPS","DECISION_MAKING"],"provenance_note":"Migrated from preserved Drive object 1E3LNlVElRpUft52mXGcW7dHhm7jQLqg9."},{"evidence_id":"voice-address-ledger","repository_path":"series/blue-archive/03 Longitudinal Ledgers/BLUE_ARCHIVE_JAPANESE_VOICE_AND_ADDRESS_LEDGER.md","label":"Cumulative Japanese voice and address ledger","anchor":null,"review_state":"REVIEWED","dimensions":["SPEECH"],"provenance_note":"Migrated from preserved Drive object 1u6GTcT3h4Lum0GBtQTHO1JdvrJLtXLsE."}],"analytical_coverage":[{"coverage_id":"shiroko-chapter-1-corpus","continuity_id":"blue-archive-game","medium":"GAME","unit":"STORY_CHAPTER","scope_type":"DESCRIPTIVE","evidence_ids":["chapter-1-checkpoint","character-state-ledger","voice-address-ledger"],"scope_note":"Reviewed distributed analysis within the Blue Archive Countermeasures Committee Arc, Volume 1 Chapter 1 through E020; this describes the current analytical boundary and does not claim coverage in every unit or full-game, event-story, MomoTalk, or exhaustive character-story coverage."}],"materialization_status":"PRESENT_REVIEWED","curation_status":"INCLUDED","inclusion_basis":"DISTRIBUTED_SUBSTANTIAL","notes":"Substantial distributed sequential and longitudinal analysis through the Chapter 1 checkpoint; no dedicated character monograph is claimed; nonauthoritative before G8."}'),
        ]
        self.assertEqual(blue_archive_rows, expected_blue_archive_rows)

        def rows(relative: str) -> list[dict[str, object]]:
            return [
                json.loads(line)
                for line in (REPOSITORY_ROOT / relative)
                .read_text(encoding="utf-8")
                .splitlines()
                if line
            ]

        mappings = [
            row
            for row in rows("crosswalk/drive-to-git.jsonl")
            if row.get("series_id") == "genshin-impact"
        ]
        self.assertEqual(len(mappings), 39)
        output_table = "".join(
            f"{row['git_path']}\t{row['git_bytes']}\t{row['git_sha256']}\n"
            for row in sorted(mappings, key=lambda item: item["git_path"].encode("utf-8"))
        ).encode("utf-8")
        self.assertEqual(
            hashlib.sha256(output_table).hexdigest(),
            "c30f22302d6be07a69957ca8f5542330d65feff2f2d6057284557888db26445d",
        )
        plans = [
            row
            for row in rows("crosswalk/path-plan.jsonl")
            if row.get("destination_path", "").startswith("series/genshin-impact/")
            or row.get("drive_id") == "1PpP4UJVp7EmFwhMO4tnOebhu0nm-Rzzh"
        ]
        results = [
            row
            for row in rows("crosswalk/materialization-results.jsonl")
            if row.get("run_id") == "g5-t03-genshin-impact-20260901T090435Z"
        ]
        self.assertEqual(len(plans), 40)
        self.assertEqual(len(results), 40)
        reference_plan = next(row for row in plans if row["drive_id"] == "1PpP4UJVp7EmFwhMO4tnOebhu0nm-Rzzh")
        reference_result = next(row for row in results if row["drive_id"] == "1PpP4UJVp7EmFwhMO4tnOebhu0nm-Rzzh")
        self.assertEqual(reference_plan["decision"], "REFERENCE_DRIVE")
        self.assertNotIn("destination_path", reference_plan)
        self.assertEqual(reference_result["result"], "REFERENCE_VERIFIED_NOT_MATERIALIZED")
        self.assertEqual(reference_result["source_sha256"], "ec5267566cd0cf7333d30c3aaa67f131f6c65cd9e5966f77a216c0d23d74687b")
        self.assertNotIn("destination_path", reference_result)

        cinderella_mappings = [
            row
            for row in rows("crosswalk/drive-to-git.jsonl")
            if row.get("series_id") == "the-idolmaster-cinderella-girls-mobile-games"
        ]
        self.assertEqual(len(cinderella_mappings), 23)
        cinderella_output_table = "".join(
            f"{row['git_path']}\t{row['git_bytes']}\t{row['git_sha256']}\n"
            for row in sorted(
                cinderella_mappings,
                key=lambda item: item["git_path"].encode("utf-8"),
            )
        ).encode("utf-8")
        self.assertEqual(
            hashlib.sha256(cinderella_output_table).hexdigest(),
            "db50bcda798c76090fd26a535e6e268066a2ee431ecbb6d11eedc3535b014404",
        )
        cinderella_plans = [
            row
            for row in rows("crosswalk/path-plan.jsonl")
            if row.get("destination_path", "").startswith("series/the-idolmaster-cinderella-girls-mobile-games/")
        ]
        cinderella_results = [
            row
            for row in rows("crosswalk/materialization-results.jsonl")
            if row.get("run_id") == "g5-t04-cinderella-girls-mobile-games-20260901T105439Z"
        ]
        self.assertEqual(len(cinderella_plans), 23)
        self.assertEqual(len(cinderella_results), 23)
        self.assertTrue(all(row["decision"] == "MIGRATE_TEXT" for row in cinderella_plans))
        self.assertTrue(
            all(row["result"] == "MATERIALIZED_AND_HASH_VERIFIED" for row in cinderella_results)
        )
        t04_structural_folder_ids = {'16xM-jDfd-HMBhuQW43AasjAw1UyU4XZ9', '19Sp8zzbkXW7KltGW3wh2Z7WFk9Qtw0eu', '1sOScrjWBHt0kmeqY0P-pWOdgfcwBUTp4'}
        for relative in (
            "crosswalk/drive-to-git.jsonl",
            "crosswalk/path-plan.jsonl",
            "crosswalk/materialization-results.jsonl",
        ):
            self.assertFalse(
                any(row["drive_id"] in t04_structural_folder_ids for row in rows(relative))
            )

        blue_archive_mappings = [
            row for row in rows("crosswalk/drive-to-git.jsonl")
            if row.get("series_id") == "blue-archive"
        ]
        self.assertEqual(len(blue_archive_mappings), 36)
        blue_archive_output_table = "".join(
            f"{row['git_path']}\t{row['git_bytes']}\t{row['git_sha256']}\n"
            for row in sorted(
                blue_archive_mappings,
                key=lambda item: item["git_path"].encode("utf-8"),
            )
        ).encode("utf-8")
        self.assertEqual(
            hashlib.sha256(blue_archive_output_table).hexdigest(),
            "87f970f29dc6db5a87793fd24cc4f2239404e4e32c73b35db8d811b6408fd38a",
        )
        blue_archive_plans = [
            row for row in rows("crosswalk/path-plan.jsonl")
            if row.get("destination_path", "").startswith("series/blue-archive/")
        ]
        blue_archive_results = [
            row for row in rows("crosswalk/materialization-results.jsonl")
            if row.get("run_id") == "g5-t05-blue-archive-20260901T122749Z"
        ]
        self.assertEqual(len(blue_archive_plans), 36)
        self.assertEqual(len(blue_archive_results), 36)
        self.assertTrue(all(row["decision"] == "MIGRATE_TEXT" for row in blue_archive_plans))
        self.assertTrue(all(row["result"] == "MATERIALIZED_AND_HASH_VERIFIED" for row in blue_archive_results))
        t05_folder_ids = {'1-R__ePH1tizFOI06gv6PQ-244wCGFjyy', '1719EaevVx4CLd1HaTxN1xZs5QCH2n6d0', '17uW_oKAX6jqyadKSVdHF7TSQzDOONVas', '1BncjmiGKIiFeHLss8TS6faLt7YpgKXw0', '1CkY1ZJxgmKke8F2fkfmPF8zrzo1ij373', '1GgJG8xQhgYlNS7P6ER7o1mdiecWYDCKz', '1be2qxffa15BKZrNssMOBvItFAjlg8FhB', '1e0V4jIN3izMQGZssoN1jp7X2dZx-MNi2', '1jJ-BNXRkXucUX2icXeS8kQ49aG9EH3ab', '1kIOCMVnDdTONH8vbcodKGhKPQU4uzTIr', '1lE4RvoccqZYfsMw-FBg1dwgNaJjc7Yqh', '1mM7rGDIxgboDSwLMH2mmm_bQEy14K9oT'}
        for relative in (
            "crosswalk/drive-to-git.jsonl",
            "crosswalk/path-plan.jsonl",
            "crosswalk/materialization-results.jsonl",
        ):
            self.assertFalse(any(row["drive_id"] in t05_folder_ids for row in rows(relative)))

        youjo_mappings = [
            row for row in rows("crosswalk/drive-to-git.jsonl")
            if row.get("series_id") == "youjo-senki"
        ]
        self.assertEqual(len(youjo_mappings), 16)
        youjo_output_table = "".join(
            f"{row['git_path']}\t{row['git_bytes']}\t{row['git_sha256']}\n"
            for row in sorted(youjo_mappings, key=lambda item: item["git_path"].encode("utf-8"))
        ).encode("utf-8")
        self.assertEqual(
            hashlib.sha256(youjo_output_table).hexdigest(),
            "e7c0639824ecff488019703993cf02029a5e34346f0b933839ef286fc3ce1db3",
        )
        youjo_plans = [
            row for row in rows("crosswalk/path-plan.jsonl")
            if row.get("destination_path", "").startswith("series/youjo-senki/")
        ]
        youjo_results = [
            row for row in rows("crosswalk/materialization-results.jsonl")
            if row.get("run_id") == "g5-t06-youjo-senki-20260901T132724Z"
        ]
        self.assertEqual(len(youjo_plans), 16)
        self.assertEqual(len(youjo_results), 16)
        self.assertTrue(all(row["decision"] == "MIGRATE_TEXT" for row in youjo_plans))
        self.assertTrue(all(row["result"] == "MATERIALIZED_AND_HASH_VERIFIED" for row in youjo_results))
        t06_reference_ids = {'13pEqvLZiv8Pc0SjvbsWSYpk_G4VMKZ0b', '140ow12czVj4J8Q_JR44MSWI98LUxj3uk', '16tMcTb0rZZ7U3gjidf6bzJ-TravNQcCh', '17UvtZCM9QBQdFtqKjDsebZfQXsuB2idH', '1AMNfngVWTSm_4O0XadlJjHWjR8hMw21X', '1B9k4mqImDwLNhZz4jrbXi85h5fSsN7dP', '1C95SxSuba7Fr9diTMyc1N8q58TbzxsLs', '1Eoz8hpJMoeksACmQgvJXntTEcYM-w20g', '1GZMXU-ulPFfKFKGrjl6GjXUYtqnorwg5', '1GlDNvT5spgIQk5VaUU5S2Qsk5dF174hR', '1JxHeRuCRltCmQsyIs2nQruzewx1U8Bmd', '1LRcSX-k739E4O4xQ2ImZnawzx6IylARo', '1LYRzJS4AL6jHAmIAjkaOC-HIWQQdBp51', '1TomsYaw1BmQMRp-JuMils2PeHzl375uo', '1Ul_BbZkw9UkSOrDik3hmWVfcK84WWGvW', '1VJj8j-KwC2ODJT7mkJcX1zvExrY4Cvl2', '1Z7UPnnWeFoO2tpXxv1NfvWtcMkPwt63V', '1aDiFqWjWHZ53xX-lBvjMLfA6eN89Z7SZ', '1d6vk6xFzkML17mwbUmBrWyxNxftptkv4', '1dPqF3RjqawccCi8LA59QVMXsp2KDvH63', '1i1Ov7u5yGciH55j-04LxIR4CWck61-KH', '1keRBa1MAecQmFefKgmnUMroSeOarf1B1', '1l8ok-FT2RMmDl-qeXJnVaj8hrS7pzKeu', '1q1xEv83Ld8KGENT_cZTN3OhAzjoFqzzs', '1v3oLyOSuwD9WgZX_TvAPekRo20g4m_Rh', '1whdImFw-vUblagWfpiqEmY58hT1vd3LZ', '1z-U_tluPeOwMuRIVzEbQOOxrI1cYlMK4', '1zWogK3vzZ0Tj1_92r3NaESIj1NzV1Biv'}
        for relative in (
            "crosswalk/drive-to-git.jsonl",
            "crosswalk/path-plan.jsonl",
            "crosswalk/materialization-results.jsonl",
        ):
            self.assertFalse(any(row["drive_id"] in t06_reference_ids for row in rows(relative)))
        self.assertFalse(any(row["series_id"] == "youjo-senki" for row in character_rows))

        logh_mappings = [
            row for row in rows("crosswalk/drive-to-git.jsonl")
            if row.get("series_id") == "legend-of-the-galactic-heroes"
        ]
        self.assertEqual(len(logh_mappings), 20)
        logh_output_table = "".join(
            f"{row['git_path']}\t{row['git_bytes']}\t{row['git_sha256']}\n"
            for row in sorted(logh_mappings, key=lambda item: item["git_path"].encode("utf-8"))
        ).encode("utf-8")
        self.assertEqual(
            hashlib.sha256(logh_output_table).hexdigest(),
            "2dcc15f46892ebf4f2b8681c5b8d15af03465d46cafafaa9fe067e81d54d3069",
        )
        logh_plans = [
            row for row in rows("crosswalk/path-plan.jsonl")
            if row.get("destination_path", "").startswith("series/legend-of-the-galactic-heroes/")
        ]
        logh_results = [
            row for row in rows("crosswalk/materialization-results.jsonl")
            if row.get("run_id") == "g5-t07-legend-of-the-galactic-heroes-20260901T133207Z"
        ]
        self.assertEqual(len(logh_plans), 20)
        self.assertEqual(len(logh_results), 20)
        self.assertTrue(all(row["decision"] == "MIGRATE_TEXT" for row in logh_plans))
        self.assertTrue(all(row["result"] == "MATERIALIZED_AND_HASH_VERIFIED" for row in logh_results))
        t07_reference_ids = {'157kfSOJFoSsrKSRBNOzd-Owh0stYW-wW', '16tUwWtNZYAGDuEkXKo8GUYB2hrYRrS_J', '194x1iUfaA-nZzetuqLtyc8wdtnUejyK3', '1CRxWpRwQexhj7xZHvHEc3TredmwOkUva', '1JGXiu3Hca8mzSEXJo9QekM43gxx2eHKl', '1KUJ2mugYPBTMZQ90xw_t3WG2LDtIzmOz', '1MaljNU7dotPtpKLarFt4MMQZn0252xEG', '1NfMpMzA00jOXoaZdjdYXkIEp_0MYHF-_', '1QZEzzoL0fFxZwjQKEJNlmMeiravgFeZN', '1VeLiZ-ZhEIJuWuphla3ndySbYrZKaTP4', '1arKCKniMDN2i5unIN4bpItlC1_gK53F5', '1cU4EAu8n1VtQ-tDEG6JGGEmYXjXi_mwu', '1rDCzTmvlV8kwLdSg-VUpyVw4QaCLR37V'}
        for relative in (
            "crosswalk/drive-to-git.jsonl",
            "crosswalk/path-plan.jsonl",
            "crosswalk/materialization-results.jsonl",
        ):
            self.assertFalse(any(row["drive_id"] in t07_reference_ids for row in rows(relative)))
        logh_subject_ids = {
            row["analysis_subject_id"]
            for row in character_rows
            if row["series_id"] == "legend-of-the-galactic-heroes"
        }
        self.assertEqual(
            logh_subject_ids,
            {
                "legend-of-the-galactic-heroes:reinhard-von-lohengramm@original-novels",
                "legend-of-the-galactic-heroes:yang-wen-li@original-novels",
            },
        )

    def test_g5_t01_maebashi_tuple_is_exact(self) -> None:
        drive_ids = {
            "1oS3WSBuGqIBweGj78r22X5-5dFDkVwe0",
            "1NXOWAQ85SlLj3uWF5Egw1lOyy2h-tcO-",
            "1mC0vJjRmBV3YzIWB1UK-KcknA1MFZCsm",
            "1jUUbLFAVHpaBHp9K8CWycG_esjtxRLJI",
            "1urCXJbXhdmAoZYXbSgkdUhD_m7-EfRn8",
            "1VlG5GCo3PbvK1jmZbfYQkHdVX6iCGp9t",
            "1ztx3DvgdG30PdGnBUDBUJbqIacY7hv6F",
            "1fNAM4WXmvEXycPZcx2o_oAFHfO6cv4bC",
            "1xupZMWBb79nrYn89ZnkQwj-UeRTPBZWo",
            "1fArHXGsRYsSUvuUsAvMnGFnGesctRrQB",
            "15eEqrgPqm4bsueJLimWr38KF0FQu7WGI",
            "1VUTIyTexR2Ch88JUYMHCnZLrlKfeeaKT",
            "1m_xF5IUZl0KAUUTcRTGgQ6mG5FDZXB5U",
            "1oWQn-Diriute5gEdCEo2fzh02wsk80iG",
            "1oIIffwFA2p8Lj7aHbyIlwoX-j1YOT79f",
            "1MTZ4e8yawR4BN_XVoc0M5BRqF58W0pHb",
            "12XohkkbKzZ9GNALwPI2VQeI44DIzlrOc",
            "1xk_yDNujJmVI89QHtHuJVUQ4kdmuV9kY",
        }

        def rows(relative: str) -> list[dict[str, object]]:
            return [
                json.loads(line)
                for line in (REPOSITORY_ROOT / relative)
                .read_text(encoding="utf-8")
                .splitlines()
                if line
            ]

        mappings = [row for row in rows("crosswalk/drive-to-git.jsonl") if row["drive_id"] in drive_ids]
        plans = [row for row in rows("crosswalk/path-plan.jsonl") if row["drive_id"] in drive_ids]
        results = [row for row in rows("crosswalk/materialization-results.jsonl") if row["drive_id"] in drive_ids]
        self.assertEqual(len(mappings), 18)
        self.assertEqual(len(plans), 18)
        self.assertEqual(len(results), 18)
        self.assertEqual({row["drive_id"] for row in mappings}, drive_ids)
        self.assertTrue(all(row["series_id"] == "maebashi-witches" for row in mappings))
        self.assertTrue(all(row["decision"] == "MIGRATE_TEXT" for row in plans))
        self.assertTrue(all(row["run_id"] == "g5-t01-maebashi-witches-v1-20260901T065630Z" for row in results))
        self.assertTrue(all(row["result"] == "MATERIALIZED_AND_HASH_VERIFIED" for row in results))
        self.assertTrue(all(row["destination_path"].startswith("series/maebashi-witches/V1 Analysis/") for row in results))

        transcript = next(row for row in results if row["destination_path"].endswith("Full Transcript.md"))
        self.assertIn("HISTORICAL_LEGACY_AUTHORITY_QUARTET", transcript["transformation"])
        self.assertFalse(transcript["body_preserved"])
        manifest = next(row for row in results if row["destination_path"].endswith("/MANIFEST.md"))
        self.assertEqual(manifest["destination_bytes"], 2706)
        self.assertEqual(manifest["destination_sha256"], "94c23fbbb6e040a64f8de1bfae8831912902661cdebba79393781bdf69f36101")

        character_rows = rows("characters/registry.jsonl")
        maebashi = [row for row in character_rows if row["series_id"] == "maebashi-witches"]
        self.assertEqual(len(maebashi), 7)
        self.assertTrue(all(row["materialization_status"] == "PRESENT_REVIEWED" for row in maebashi))
        self.assertTrue(all(row["curation_status"] == "INCLUDED" for row in maebashi))
        self.assertTrue(all(row["analytical_coverage"][0]["scope_type"] == "DESCRIPTIVE" for row in maebashi))
        self.assertFalse(any("SPEECH" in row["analytical_dimensions"] for row in maebashi))

    def test_g5_t02_mass_effect_tuple_is_exact(self) -> None:
        expected = {
            "10hQeUNs8alrGa72ejpwI6LHGi-7ocfNb": (
                "studies/comparative-media/Mass Effect/CURRENT_STATE_AND_CORPUS_MAP.md",
                "ecff3d3aa0f6164b0e689708c7664a8bcef52b324625fbfc0a4de5089e93a8a7",
            ),
            "1Mr0PMPv2PKNQQeE3CXqOUZoM9vYESCGO": (
                "studies/comparative-media/Mass Effect/01 Character Monographs/MASS_EFFECT_PARAGON_SHEPARD_CHARACTER_MONOGRAPH.md",
                "efe4cc45ea5f337dee517bef7eff9e3f4eb8fa807ad578da77d02ef27b78c2d7",
            ),
            "1djYkXGE68vHmP5oCR3LKCMoKfBT7dPUa": (
                "studies/comparative-media/Mass Effect/01 Character Monographs/MASS_EFFECT_RENEGADE_SHEPARD_CHARACTER_MONOGRAPH.md",
                "2ee902cee56b184582cb11d68ab411739380e844231cb5ab206cda198b3a5b0f",
            ),
        }
        revisions = {
            "10hQeUNs8alrGa72ejpwI6LHGi-7ocfNb": "5",
            "1Mr0PMPv2PKNQQeE3CXqOUZoM9vYESCGO": "7",
            "1djYkXGE68vHmP5oCR3LKCMoKfBT7dPUa": "6",
        }

        def rows(relative: str) -> list[dict[str, object]]:
            return [
                json.loads(line)
                for line in (REPOSITORY_ROOT / relative)
                .read_text(encoding="utf-8")
                .splitlines()
                if line
            ]

        for drive_id, (path, expected_sha) in expected.items():
            data = (REPOSITORY_ROOT / path).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), expected_sha)
            mapping = next(row for row in rows("crosswalk/drive-to-git.jsonl") if row["drive_id"] == drive_id)
            plan = next(row for row in rows("crosswalk/path-plan.jsonl") if row["drive_id"] == drive_id)
            result = next(row for row in rows("crosswalk/materialization-results.jsonl") if row["drive_id"] == drive_id)
            self.assertEqual(mapping["study_id"], "comparative-media")
            self.assertEqual(mapping["git_path"], path)
            self.assertEqual(mapping["git_sha256"], expected_sha)
            self.assertEqual(mapping["source_revision"], revisions[drive_id])
            self.assertEqual(plan["study_id"], "comparative-media")
            self.assertEqual(plan["decision"], "MIGRATE_TEXT")
            self.assertEqual(plan["source_revision"], revisions[drive_id])
            self.assertEqual(result["study_id"], "comparative-media")
            self.assertEqual(result["run_id"], "g5-t02-mass-effect-20260901T074800Z")
            self.assertEqual(result["result"], "MATERIALIZED_AND_HASH_VERIFIED")
            self.assertEqual(result["source_revision"], revisions[drive_id])

        mass_effect = [
            row
            for row in rows("characters/registry.jsonl")
            if row["series_id"] == "mass-effect"
        ]
        self.assertEqual(len(mass_effect), 2)
        self.assertTrue(all(row["subject_kind"] == "PLAYER_ARCHETYPE" for row in mass_effect))
        self.assertTrue(all(row["continuity_id"] == "mass-effect-trilogy-games" for row in mass_effect))
        self.assertTrue(all(row["materialization_status"] == "PRESENT_REVIEWED" for row in mass_effect))
        self.assertFalse(any("SPEECH" in row["analytical_dimensions"] for row in mass_effect))

    def test_g6_source_provenance_closure_is_exact(self) -> None:
        expected_source_ids = {
            "11tzDCqbg6Twy6KlYyrnavpwSqkwRpnWD",
            "15aeSFNRTkpq7NJcFelnb_4dt4Gsb-92P",
            "1EoVFHSupUds_ziA29HAwbNJ-Ll_5k__n",
            "1KTJoroDSVSnylV_vZJ6kjg1GbCxzewDh",
            "1O7ATkjdEX9CWo01-Opyn3nW0v6PlWNY9",
            "1UkyI6DpKDzOQe1FS_DfMCRw2osfS7Mwr",
            "1WlMff5RlZFEa3VSjWW1vShAJiFX07lOa",
            "1gjKepFqM--LJQyA6TtIQs8HaBmaUk7YC",
            "1igz8dtdgUnnCpRYrat4Bi5tjZn8kduJw",
            "1m6g1HyiLdVfi773EHw-q6084kDIG6eIE",
            "1ujr9mZ3bVATtwSBQt0w8Qj3qm3ry3f6i",
            "1z_zolsM8-FRoDitPh5wGXrWjsttcLh7Z",
        }

        def rows(relative: str) -> list[dict[str, object]]:
            return [
                json.loads(line)
                for line in (REPOSITORY_ROOT / relative)
                .read_text(encoding="utf-8")
                .splitlines()
                if line
            ]

        results = {
            row["representation_id"]: row
            for row in rows("crosswalk/materialization-results.jsonl")
            if row.get("run_id") == "g6-source-provenance-closure-20260901T190000Z"
        }
        mappings = {
            row["representation_id"]: row
            for row in rows("crosswalk/drive-to-git.jsonl")
            if row.get("representation_id") in results
        }
        plans = {
            row["representation_id"]: row
            for row in rows("crosswalk/path-plan.jsonl")
            if row.get("representation_id") in results
        }
        self.assertEqual(len(mappings), 10)
        self.assertEqual(set(mappings), set(results))
        self.assertEqual(set(mappings), set(plans))
        self.assertEqual(
            {
                drive_id
                for row in mappings.values()
                for drive_id in row["source_drive_ids"]
            },
            expected_source_ids,
        )
        self.assertEqual(
            sum(row.get("governance_id") == "repository" for row in mappings.values()),
            8,
        )
        self.assertEqual(
            sum(
                row["transformation"] == "MERGE_IDENTICAL_BYTES_V1"
                for row in mappings.values()
            ),
            2,
        )
        for representation_id, mapping in mappings.items():
            with self.subTest(representation_id=representation_id):
                result = results[representation_id]
                plan = plans[representation_id]
                self.assertEqual(mapping["source_drive_ids"], result["source_drive_ids"])
                self.assertEqual(mapping["source_drive_ids"], plan["source_drive_ids"])
                self.assertEqual(mapping["source_tuples"], result["source_tuples"])
                self.assertEqual(mapping["source_tuples"], plan["source_tuples"])
                data = (REPOSITORY_ROOT / mapping["git_path"]).read_bytes()
                self.assertEqual(len(data), mapping["git_bytes"])
                self.assertEqual(hashlib.sha256(data).hexdigest(), mapping["git_sha256"])

    def test_g6_all_materialized_representations_have_three_ledger_legs(self) -> None:
        def rows(relative: str) -> list[dict[str, object]]:
            return [
                json.loads(line)
                for line in (REPOSITORY_ROOT / relative)
                .read_text(encoding="utf-8")
                .splitlines()
                if line
            ]

        mappings = {
            row["representation_id"]: row
            for row in rows("crosswalk/drive-to-git.jsonl")
            if row.get("representation_id")
        }
        results = {
            row["representation_id"]: row
            for row in rows("crosswalk/materialization-results.jsonl")
            if row.get("representation_id")
        }
        plans = {
            row["representation_id"]: row
            for row in rows("crosswalk/path-plan.jsonl")
            if row.get("representation_id")
        }
        self.assertEqual(len(mappings), 2814)
        self.assertEqual(set(mappings), set(results))
        self.assertEqual(set(mappings), set(plans))
        for representation_id, mapping in mappings.items():
            with self.subTest(representation_id=representation_id):
                result = results[representation_id]
                plan = plans[representation_id]
                self.assertEqual(mapping["git_path"], result["destination_path"])
                self.assertEqual(mapping["git_path"], plan["destination_path"])
                self.assertEqual(mapping["git_bytes"], result["destination_bytes"])
                self.assertEqual(mapping["git_bytes"], plan["destination_bytes"])
                self.assertEqual(mapping["git_sha256"], result["destination_sha256"])
                self.assertEqual(mapping["git_sha256"], plan["destination_sha256"])
                self.assertEqual(mapping["transformation"], result["transformation"])
                self.assertEqual(mapping["transformation"], plan["transformation"])

        reference_results = [
            row
            for row in rows("crosswalk/materialization-results.jsonl")
            if not row.get("representation_id")
        ]
        reference_plans = [
            row
            for row in rows("crosswalk/path-plan.jsonl")
            if not row.get("representation_id")
        ]
        self.assertEqual(len(reference_results), 14)
        self.assertEqual(len(reference_plans), 14)
        self.assertTrue(all("destination_path" not in row for row in reference_results))
        self.assertTrue(all("destination_path" not in row for row in reference_plans))

    def test_p02_exact_copy_and_reference_only_rows_are_consistent(self) -> None:
        migrated_id = "1EySpUScZKZ2irfYamER1e8FCrnjniGjk"
        referenced_id = "1US_aDBA1ttPuUx-WlMfr7559PB8vq6we"
        migrated_sha256 = (
            "7dde60c452627a694307dda68abfb0d4d434ec1c2ce934bf85a0b81db483c366"
        )
        referenced_sha256 = (
            "ce3d0b9a6df171fdb5d52e7c509d08c35f49ddbc3cbb03e27ca12a079b247a37"
        )
        destination = (
            "series/idoly-pride/V2 Analysis/02 Source Audits and Longitudinal "
            "Ledgers/02.01 Corpus Coverage and Priority Ledger/"
            "IDOLY_PRIDE_V2_SOURCE_TO_BUNDLE_PROVENANCE.csv"
        )

        csv_bytes = (REPOSITORY_ROOT / destination).read_bytes()
        self.assertEqual(len(csv_bytes), 1_377_633)
        self.assertEqual(hashlib.sha256(csv_bytes).hexdigest(), migrated_sha256)

        def load_rows(relative: str) -> list[dict[str, object]]:
            return [
                json.loads(line)
                for line in (REPOSITORY_ROOT / relative)
                .read_text(encoding="utf-8")
                .splitlines()
                if line
            ]

        drive_rows = load_rows("crosswalk/drive-to-git.jsonl")
        migrated_drive_rows = [row for row in drive_rows if row["drive_id"] == migrated_id]
        self.assertEqual(len(migrated_drive_rows), 1)
        self.assertEqual(migrated_drive_rows[0]["git_path"], destination)
        self.assertEqual(migrated_drive_rows[0]["source_sha256"], migrated_sha256)
        self.assertEqual(migrated_drive_rows[0]["git_sha256"], migrated_sha256)
        self.assertFalse(any(row["drive_id"] == referenced_id for row in drive_rows))

        result_rows = load_rows("crosswalk/materialization-results.jsonl")
        migrated_results = [row for row in result_rows if row["drive_id"] == migrated_id]
        self.assertEqual(len(migrated_results), 1)
        self.assertEqual(migrated_results[0]["destination_path"], destination)
        self.assertEqual(migrated_results[0]["destination_sha256"], migrated_sha256)
        referenced_results = [row for row in result_rows if row["drive_id"] == referenced_id]
        self.assertEqual(len(referenced_results), 1)
        self.assertEqual(
            referenced_results[0]["result"],
            "REFERENCE_VERIFIED_NOT_MATERIALIZED",
        )
        self.assertEqual(referenced_results[0]["source_sha256"], referenced_sha256)
        self.assertNotIn("destination_path", referenced_results[0])

        plan_rows = load_rows("crosswalk/path-plan.jsonl")
        migrated_plans = [row for row in plan_rows if row["drive_id"] == migrated_id]
        self.assertEqual(len(migrated_plans), 1)
        self.assertEqual(migrated_plans[0]["destination_path"], destination)
        referenced_plans = [row for row in plan_rows if row["drive_id"] == referenced_id]
        self.assertEqual(len(referenced_plans), 1)
        self.assertEqual(referenced_plans[0]["decision"], "REFERENCE_DRIVE")
        self.assertNotIn("destination_path", referenced_plans[0])

    def test_p03_native_doc_sheet_candidate_is_exact_and_partial(self) -> None:
        doc_drive_id = "10hQeZP3j1AUQ00YsOmt4xYIJmUOant0NsdXXkbmfs3Y"
        sheet_drive_id = "1fDfRSY9oHovjAcO-YPItDfZlirPjlc3yL8IZQZMRRXg"
        study_id = "doujinshi-fanwork-comparative-taxonomy"
        study_root = f"studies/{study_id}"
        doc_path = f"{study_root}/DJFW_CURRENT_STATE_AND_CORPUS_MAP.md"
        structure_path = (
            f"{study_root}/01 Project Registry and Source Lock/"
            "DJFW_PROJECT_CONTROL_SHEET.structure.json"
        )
        doc_sha256 = (
            "4679e1ff5f14b0ffe780748c0397255ea01feaf700d48e88feaf6b4697488f65"
        )
        structure_sha256 = (
            "c58920ffb66a752f2566db5317f25dbba60a430e0091f3206740e80494dde675"
        )
        sheet_source_sha256 = (
            "45af93158093209fd43c451f800322808e5b5ef184e949af690089f65e46d57a"
        )
        doc_source_sha256 = (
            "df54471c1598e3637eb75e12f13c0565d942b8294c36c107b10920ee1cb07fad"
        )

        doc_bytes = (REPOSITORY_ROOT / doc_path).read_bytes()
        self.assertEqual(len(doc_bytes), 13_396)
        self.assertEqual(hashlib.sha256(doc_bytes).hexdigest(), doc_sha256)

        structure_bytes = (REPOSITORY_ROOT / structure_path).read_bytes()
        self.assertEqual(len(structure_bytes), 8_103)
        self.assertEqual(
            hashlib.sha256(structure_bytes).hexdigest(),
            structure_sha256,
        )
        structure = json.loads(structure_bytes.decode("utf-8"))
        self.assertEqual(structure["source_drive_id"], sheet_drive_id)
        self.assertEqual(structure["source_drive_revision"], "31")
        self.assertEqual(structure["source_byte_length"], 56_153)
        self.assertEqual(structure["source_sha256"], sheet_source_sha256)
        self.assertEqual(structure["worksheet_count"], 17)
        self.assertEqual(len(structure["worksheets"]), 17)

        tsv_paths: set[str] = set()
        for expected_index, worksheet in enumerate(structure["worksheets"]):
            with self.subTest(worksheet=worksheet["name"]):
                self.assertEqual(worksheet["index"], expected_index)
                tsv_path = worksheet["tsv_destination_path"]
                tsv_paths.add(tsv_path)
                data = (REPOSITORY_ROOT / tsv_path).read_bytes()
                self.assertEqual(
                    hashlib.sha256(data).hexdigest(),
                    worksheet["tsv_sha256"],
                )
                self.assertNotIn(b"\r", data)
                self.assertTrue(data.endswith(b"\n"))

        expected_destinations = {doc_path, structure_path, *tsv_paths}
        self.assertEqual(len(expected_destinations), 19)

        tracked_paths = (
            REPOSITORY_ROOT
            / "governance/repository-controls/CURRENT_TRACKED_PATHS.txt"
        ).read_text(encoding="utf-8").splitlines()
        self.assertGreaterEqual(
            len(tracked_paths),
            self.scope["migration"]["g5_progress"]["tracked_paths_after"],
        )
        self.assertEqual(tracked_paths, sorted(tracked_paths))
        self.assertTrue(expected_destinations.issubset(set(tracked_paths)))
        self.assertFalse(
            any(path.casefold().endswith(".xlsx") for path in tracked_paths)
        )

        def load_rows(relative: str) -> list[dict[str, object]]:
            return [
                json.loads(line)
                for line in (REPOSITORY_ROOT / relative)
                .read_text(encoding="utf-8")
                .splitlines()
                if line
            ]

        drive_rows = load_rows("crosswalk/drive-to-git.jsonl")
        p03_drive_rows = [
            row
            for row in drive_rows
            if row["drive_id"] in {doc_drive_id, sheet_drive_id}
        ]
        self.assertEqual(len(p03_drive_rows), 19)
        self.assertEqual(
            {row["git_path"] for row in p03_drive_rows},
            expected_destinations,
        )
        self.assertEqual(
            len({row["representation_id"] for row in p03_drive_rows}),
            19,
        )
        for row in p03_drive_rows:
            self.assertEqual(row["study_id"], study_id)
            data = (REPOSITORY_ROOT / row["git_path"]).read_bytes()
            self.assertEqual(len(data), row["git_bytes"])
            self.assertEqual(hashlib.sha256(data).hexdigest(), row["git_sha256"])
        sheet_drive_rows = [
            row for row in p03_drive_rows if row["drive_id"] == sheet_drive_id
        ]
        self.assertEqual(len(sheet_drive_rows), 18)
        self.assertTrue(
            all(row["source_revision"] == "31" for row in sheet_drive_rows)
        )
        self.assertTrue(
            all(
                row["source_sha256"] == sheet_source_sha256
                for row in sheet_drive_rows
            )
        )
        doc_drive_rows = [
            row for row in p03_drive_rows if row["drive_id"] == doc_drive_id
        ]
        self.assertEqual(len(doc_drive_rows), 1)
        self.assertEqual(doc_drive_rows[0]["source_revision"], "26")
        self.assertEqual(doc_drive_rows[0]["source_bytes"], 13_427)
        self.assertEqual(doc_drive_rows[0]["source_sha256"], doc_source_sha256)

        result_rows = load_rows("crosswalk/materialization-results.jsonl")
        p03_results = [
            row
            for row in result_rows
            if row["drive_id"] in {doc_drive_id, sheet_drive_id}
        ]
        materialized_results = [
            row for row in p03_results if "destination_path" in row
        ]
        reference_results = [
            row for row in p03_results if "destination_path" not in row
        ]
        self.assertEqual(
            {row["destination_path"] for row in materialized_results},
            expected_destinations,
        )
        self.assertEqual(len(reference_results), 1)
        self.assertEqual(reference_results[0]["drive_id"], sheet_drive_id)
        self.assertEqual(
            reference_results[0]["result"],
            "REFERENCE_VERIFIED_NOT_MATERIALIZED",
        )
        self.assertEqual(
            reference_results[0]["terminal_action"],
            "REFERENCE_DRIVE",
        )

        plan_rows = load_rows("crosswalk/path-plan.jsonl")
        p03_plans = [
            row
            for row in plan_rows
            if row["drive_id"] in {doc_drive_id, sheet_drive_id}
        ]
        migrated_plans = [row for row in p03_plans if "destination_path" in row]
        reference_plans = [
            row for row in p03_plans if "destination_path" not in row
        ]
        self.assertEqual(
            {row["destination_path"] for row in migrated_plans},
            expected_destinations,
        )
        self.assertTrue(
            all(row["decision"] == "MIGRATE_TRANSFORMED" for row in migrated_plans)
        )
        self.assertEqual(len(reference_plans), 1)
        self.assertEqual(reference_plans[0]["drive_id"], sheet_drive_id)
        self.assertEqual(reference_plans[0]["decision"], "REFERENCE_DRIVE")

    def test_p04_zip_references_are_exact_and_destination_free(self) -> None:
        run_id = "g4-p04-zip-reference-20260901T053758Z"
        expected_sources = [
            {
                "drive_id": "1KjeSZCwRGXuNn4Lyo1S-VmgIP3_PlDrd",
                "source_bytes": 122_672,
                "source_path": (
                    "Gakuen Idolmaster/10_RELEASE_MANIFEST_AND_ARCHIVE/"
                    "GAKUEN_IDOLMASTER_PHASE3_TEMARI_CHARACTER_CORE.zip"
                ),
                "source_sha256": (
                    "40b355004c1b176f39779303b60dbd33415a0bb88810d3132df7e22c86376a1b"
                ),
            },
            {
                "drive_id": "1_FOnm73lxvcx1QwLxS-1AA896C_2_1Ik",
                "source_bytes": 129_983,
                "source_path": (
                    "Gakuen Idolmaster/10_RELEASE_MANIFEST_AND_ARCHIVE/"
                    "GAKUEN_IDOLMASTER_PHASE3_LILJA_CHARACTER_CORE.zip"
                ),
                "source_sha256": (
                    "8b28d8a806763472826b800c2a0e5b34f749c86154cf5a251a82036ac81dadd2"
                ),
            },
            {
                "drive_id": "1j6EvtMB11kG3E1s-eoB6RcRWyhrfDZyc",
                "source_bytes": 131_808,
                "source_path": (
                    "Gakuen Idolmaster/10_RELEASE_MANIFEST_AND_ARCHIVE/"
                    "GAKUEN_IDOLMASTER_PHASE3_TEMARI_COMPLETE_AUDIOVISUAL_BASELINE.zip"
                ),
                "source_sha256": (
                    "af05ee2c76b35e2d84344e2070fb24b84c0c26e6e44a835d6835cd94bc4206d7"
                ),
            },
            {
                "drive_id": "1oVFv4UQJbqqhY1nCnG9wmkduSh7mgM8U",
                "source_bytes": 398,
                "source_path": (
                    "Gakuen Idolmaster/05_AUDIOVISUAL_ANALYSIS/"
                    "00_MUSICAL_IDENTITY_BASELINES/05_KATSURAGI_LILJA/"
                    "GAKUEN_IDOLMASTER_PHASE3_LILJA_INTEGRATED_AV_R1.zip"
                ),
                "source_sha256": (
                    "03a863418e09542118a4afed9f23d034b9f0ee6a4f83f755d79826d29c641b91"
                ),
            },
            {
                "drive_id": "1u3Yc2D3rhzUrhE1XKpTBdE0jj863xD6d",
                "source_bytes": 429_394,
                "source_path": (
                    "Gakuen Idolmaster/10_RELEASE_MANIFEST_AND_ARCHIVE/"
                    "GAKUEN_IDOLMASTER_PHASE3_TEMARI_COMPLETE_AUDIOVISUAL_BASELINE.zip"
                ),
                "source_sha256": (
                    "7656ee5e8fd5cdf4909da218f35138d8f074754b19cf04b282186656df727294"
                ),
            },
            {
                "drive_id": "1xajzp2rB8zhw0wcCykogJAKGahsPJdgA",
                "source_bytes": 246,
                "source_path": (
                    "Gakuen Idolmaster/05_AUDIOVISUAL_ANALYSIS/"
                    "00_MUSICAL_IDENTITY_BASELINES/05_KATSURAGI_LILJA/"
                    "GAKUEN_IDOLMASTER_PHASE3_LILJA_INTEGRATED_AV_R1.zip"
                ),
                "source_sha256": (
                    "cd71a44a4d598beb7138171e6c1ae2cfa28cb3da53fc900633f6e127e8d5b221"
                ),
            },
        ]
        expected_ids = {item["drive_id"] for item in expected_sources}

        def load_rows(relative: str) -> list[dict[str, object]]:
            return [
                json.loads(line)
                for line in (REPOSITORY_ROOT / relative)
                .read_text(encoding="utf-8")
                .splitlines()
                if line
            ]

        drive_rows = load_rows("crosswalk/drive-to-git.jsonl")
        self.assertFalse(any(row["drive_id"] in expected_ids for row in drive_rows))

        plans = [
            row
            for row in load_rows("crosswalk/path-plan.jsonl")
            if row["drive_id"] in expected_ids
        ]
        expected_plans = [
            {
                "decision": "REFERENCE_DRIVE",
                "drive_id": source["drive_id"],
                "path_status": "REFERENCE_VERIFIED_NOT_MATERIALIZED",
                "schema_version": 1,
                "source_path": source["source_path"],
            }
            for source in expected_sources
        ]
        self.assertEqual(plans, expected_plans)

        all_results = load_rows("crosswalk/materialization-results.jsonl")
        results = [
            row
            for row in all_results
            if row["drive_id"] in expected_ids
        ]
        expected_results = [
            {
                "drive_id": source["drive_id"],
                "result": "REFERENCE_VERIFIED_NOT_MATERIALIZED",
                "run_id": run_id,
                "schema_version": 1,
                "source_bytes": source["source_bytes"],
                "source_path": source["source_path"],
                "source_sha256": source["source_sha256"],
                "terminal_action": "REFERENCE_DRIVE",
                "transformation": "REFERENCE_NO_COPY",
            }
            for source in expected_sources
        ]
        self.assertEqual(results, expected_results)
        self.assertEqual(
            [row for row in all_results if row.get("run_id") == run_id],
            expected_results,
        )

        prohibited = {
            "destination_path",
            "destination_sha256",
            "destination_bytes",
            "representation_id",
            "series_id",
            "study_id",
        }
        for row in [*plans, *results]:
            self.assertFalse(prohibited & set(row))

        tracked_paths = (
            REPOSITORY_ROOT
            / "governance/repository-controls/CURRENT_TRACKED_PATHS.txt"
        ).read_text(encoding="utf-8").splitlines()
        self.assertGreaterEqual(
            len(tracked_paths),
            self.scope["migration"]["g5_progress"]["tracked_paths_after"],
        )
        self.assertFalse(any(path.casefold().endswith(".zip") for path in tracked_paths))
        self.assertTrue(
            any(path.startswith("series/gakuen-idolmaster/") for path in tracked_paths)
        )

        provenance = (
            REPOSITORY_ROOT
            / "provenance/drive-artifacts/DRIVE_ARTIFACT_REFERENCE_INDEX.md"
        ).read_text(encoding="utf-8")
        exclusion = (
            REPOSITORY_ROOT
            / "governance/reports/ARTIFACT_EXCLUSION_REPORT.md"
        ).read_text(encoding="utf-8")
        for source in expected_sources:
            for document in (provenance, exclusion):
                self.assertIn(source["drive_id"], document)
                self.assertIn(source["source_sha256"], document)

    def test_historical_private_bootstrap_bindings_are_unchanged(self) -> None:
        historical = {
            "governance/repository-controls/bootstrap-bindings.json": (
                "7ebb26e4cff22acbabe72905847f6efbbb6885c4a6be0b9e5297db22d654ae17"
            ),
            "governance/repository-controls/G3_BOOTSTRAP_TRACKED_PATHS.txt": (
                "75c6fe48adc719090828a2da02f3dc69e2334b8b20ee5f1c89e0f4c33ee6d191"
            ),
        }
        for relative, expected in historical.items():
            with self.subTest(path=relative):
                data = (REPOSITORY_ROOT / relative).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), expected)

    def test_p03_tsv_whitespace_exception_is_exact_and_not_broadened(self) -> None:
        tsv_rule = (
            '"studies/doujinshi-fanwork-comparative-taxonomy/'
            '01 Project Registry and Source Lock/'
            'DJFW_PROJECT_CONTROL_SHEET.tabs/*.tsv" whitespace=-blank-at-eol'
        )
        furina_rule = (
            '"series/genshin-impact/05 Character Monographs/'
            'GENSHIN_FURINA_CHARACTER_MONOGRAPH.md" whitespace=-blank-at-eol'
        )
        attributes = (REPOSITORY_ROOT / ".gitattributes").read_text(
            encoding="utf-8"
        )
        active_whitespace_rules = [
            line
            for line in attributes.splitlines()
            if line and not line.lstrip().startswith("#") and "whitespace=" in line
        ]
        self.assertEqual(active_whitespace_rules, [tsv_rule, furina_rule])

        controls = (
            REPOSITORY_ROOT / "governance/policies/REPOSITORY_CONTROLS.md"
        ).read_text(encoding="utf-8")
        self.assertIn(f"`{tsv_rule}`", controls)
        self.assertIn(f"`{furina_rule}`", controls)
        self.assertIn(
            "35 intentional CommonMark hard breaks on lines 16–19 and 28–58",
            controls,
        )
        self.assertIn(
            "106,094-byte length and SHA-256 "
            "`f61db7d38eb980bf6906fccee93a78200048f6bd2cf6efcfe60788520918b356`",
            controls,
        )
        for preserved_control in (
            "`blank-at-eof`",
            "schema validation",
            "exact-byte hashing",
            "TSV rectangularity",
            "strict UTF-8/LF validation",
            "content-safety checks",
            "Any broader path or whitespace waiver is prohibited.",
        ):
            with self.subTest(preserved_control=preserved_control):
                self.assertIn(preserved_control, controls)


if __name__ == "__main__":
    unittest.main()
