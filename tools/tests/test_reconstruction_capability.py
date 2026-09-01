from __future__ import annotations

import copy
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


REPOSITORY = Path(__file__).resolve().parents[2]
TOOLS = REPOSITORY / "tools"
sys.path.insert(0, str(TOOLS))

from character_index_core import (  # noqa: E402
    DomainError,
    GitSnapshot,
    evidence_set_digest,
    parse_evidence_ref,
    resolve_evidence_entries,
    schema_errors,
    validate_reconstruction_assessments,
)


SUBJECT = "example:alice@anime"
ENTITY = "example:alice"
EVIDENCE_ID = "profile"
EVIDENCE_REF = f"{SUBJECT}#{EVIDENCE_ID}"
EVIDENCE_PATH = "series/example/ALICE.md"
GOLDEN_ARTIFACT_SHA256 = (
    "b6a98d9ce9a2d9149288fa3df42d377c3e42737afdcdaf714e33c0a100b51060"
)
GOLDEN_EVIDENCE_SET_SHA256 = (
    "174c697bb3e87f75bb1fc56d6aec718328e9e6670dc33859919d3a82e2d387d7"
)
GOLDEN_SERIALIZED = (
    b'{"canonicalization":"CHARACTER_EVIDENCE_SET_V1","evidence":'
    b'[{"analysis_subject_id":"example:alice@anime","anchor":null,'
    b'"artifact_sha256":"b6a98d9ce9a2d9149288fa3df42d377c3e42737afdcdaf714e33c0a100b51060",'
    b'"evidence_id":"profile","repository_path":"series/example/ALICE.md"}],'
    b'"hash_algorithm":"SHA-256","unicode_version":"15.0.0"}'
)

DIMENSIONS = (
    "PSYCHOLOGICAL_MODEL",
    "LONGITUDINAL_STATE",
    "VOICE_REGISTER",
    "MUNDANE_BEHAVIOR",
    "RELATIONSHIP_CONDITIONING",
    "INTERIORITY",
    "CONFLICT_BEHAVIOR",
    "ETHICAL_DELIBERATION",
    "HUMOR_PLAY",
    "SOURCE_COMPLETENESS",
    "NEGATIVE_EVIDENCE",
    "TEMPORAL_SPECIFICITY",
)
SCENARIOS = (
    "DIALOGUE",
    "CROSS_SCENARIO",
    "MUNDANE_SOCIAL",
    "ETHICAL_DELIBERATION",
    "ROMANCE_RELATIONSHIP",
    "PROFESSIONAL_CONTEXT",
)


def golden_entry(**changes: object) -> dict[str, object]:
    entry: dict[str, object] = {
        "analysis_subject_id": SUBJECT,
        "anchor": None,
        "artifact_sha256": GOLDEN_ARTIFACT_SHA256,
        "evidence_id": EVIDENCE_ID,
        "repository_path": EVIDENCE_PATH,
    }
    entry.update(changes)
    return entry


def discovery_record(
    subject_id: str = SUBJECT,
    *,
    continuity_id: str | None = "anime",
    subject_kind: str = "SINGLE_CONTINUITY",
    evidence_path: str | None = EVIDENCE_PATH,
) -> dict[str, object]:
    evidence: list[dict[str, object]] = []
    if evidence_path is not None:
        evidence.append(
            {
                "evidence_id": EVIDENCE_ID,
                "repository_path": evidence_path,
                "label": "Profile",
                "anchor": None,
                "review_state": "REVIEWED",
                "dimensions": ["PSYCHOLOGY"],
                "provenance_note": None,
            }
        )
    return {
        "schema_version": 2,
        "character_entity_id": ENTITY,
        "analysis_subject_id": subject_id,
        "preferred_name": "Alice",
        "subject_label": subject_id.rsplit("@", 1)[1],
        "series_id": "example",
        "franchise_id": None,
        "continuity_id": continuity_id,
        "incarnation_id": None,
        "state_id": None,
        "subject_kind": subject_kind,
        "entity_aliases": [],
        "subject_aliases": [],
        "analytical_dimensions": ["PSYCHOLOGY"],
        "evidence": evidence,
        "analytical_coverage": [],
        "materialization_status": "PRESENT_REVIEWED" if evidence else "NOT_PRESENT",
        "curation_status": "CANDIDATE",
        "inclusion_basis": None,
        "notes": None,
    }


def assessment(
    basis_commit: str,
    digest: str,
    *,
    subject_id: str = SUBJECT,
    evidence_ref: str = EVIDENCE_REF,
) -> dict[str, object]:
    dimensions = []
    for dimension in DIMENSIONS:
        assessed = dimension == "PSYCHOLOGICAL_MODEL"
        dimensions.append(
            {
                "dimension": dimension,
                "grade": "B" if assessed else "NOT_ASSESSED",
                "evidence_refs": [evidence_ref] if assessed else [],
                "note": None,
            }
        )
    scenarios = [
        {
            "scenario": scenario,
            "state": "NOT_ASSESSED",
            "evidence_refs": [],
            "note": None,
        }
        for scenario in SCENARIOS
    ]
    return {
        "schema_version": 1,
        "assessment_id": "alice-anime-v1",
        "character_entity_id": ENTITY,
        "analysis_subject_id": subject_id,
        "assessment_status": "REVIEWED",
        "assessment_scope": {
            "continuity_id": "anime",
            "incarnation_id": None,
            "state_id": None,
            "source_boundary": "Reviewed profile only",
            "temporal_boundary": None,
            "basis_commit": basis_commit,
            "evidence_set_algorithm": "CHARACTER_EVIDENCE_SET_V1",
            "evidence_set_sha256": digest,
            "assessment_method": "Owner-reviewed rubric",
            "assessment_method_version": "1.0.0",
        },
        "overall_tier": "B",
        "dimensions": dimensions,
        "scenario_readiness": scenarios,
        "known_limits": [],
        "evidence_refs": [evidence_ref],
        "stale_reason": None,
        "supersedes_assessment_id": None,
        "superseded_by_assessment_id": None,
    }


def authority_artifact(body: bytes = b"# Analysis\n") -> bytes:
    return (
        b"---\n"
        b"status: canonical\n"
        b"supersedes: []\n"
        b"superseded_by: []\n"
        b"do_not_use_as_current_authority: false\n"
        b"---\n"
        + body
    )


class EvidenceSetContractTests(unittest.TestCase):
    def test_normative_golden_digest_and_exact_bytes(self) -> None:
        digest, serialized = evidence_set_digest([golden_entry()])
        self.assertEqual(digest, GOLDEN_EVIDENCE_SET_SHA256)
        self.assertEqual(serialized, GOLDEN_SERIALIZED)
        self.assertFalse(serialized.startswith(b"\xef\xbb\xbf"))
        self.assertFalse(serialized.endswith(b"\n"))

    def test_one_byte_crlf_path_and_anchor_changes_change_digest(self) -> None:
        baseline, _ = evidence_set_digest([golden_entry()])
        changed_payloads = (b"alphb\n", b"alpha\r\n")
        changed_digests = []
        for payload in changed_payloads:
            changed, _ = evidence_set_digest(
                [golden_entry(artifact_sha256=hashlib.sha256(payload).hexdigest())]
            )
            changed_digests.append(changed)
        changed_path, _ = evidence_set_digest(
            [golden_entry(repository_path="series/example/ALICE-2.md")]
        )
        changed_anchor, _ = evidence_set_digest([golden_entry(anchor="psychology")])
        self.assertEqual(len({baseline, *changed_digests, changed_path, changed_anchor}), 5)

    def test_evidence_reference_grammar_is_exact(self) -> None:
        self.assertEqual(parse_evidence_ref(EVIDENCE_REF), (SUBJECT, EVIDENCE_ID))
        for invalid in (
            f"{EVIDENCE_REF}#extra",
            EVIDENCE_REF.replace("#", "%23"),
            EVIDENCE_REF.replace("#", "/"),
            "Example:alice@anime#profile",
            EVIDENCE_REF + "\n",
        ):
            with self.subTest(invalid=invalid):
                with self.assertRaises(DomainError):
                    parse_evidence_ref(invalid)


@unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
class ReconstructionSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(
            (REPOSITORY / "governance/schemas/character-reconstruction-capability.schema.json")
            .read_text(encoding="utf-8")
        )
        cls.valid = assessment("a" * 40, GOLDEN_EVIDENCE_SET_SHA256)
        errors = schema_errors(cls.valid, cls.schema, "capability")
        if errors:
            raise AssertionError(f"valid schema fixture failed: {errors}")

    def assert_schema_invalid(self, instance: dict[str, object]) -> None:
        self.assertTrue(schema_errors(instance, self.schema, "capability"))

    def test_basis_commit_requires_a_full_lowercase_object_id_shape(self) -> None:
        for valid in ("a" * 40, "b" * 64):
            item = copy.deepcopy(self.valid)
            item["assessment_scope"]["basis_commit"] = valid  # type: ignore[index]
            self.assertEqual(schema_errors(item, self.schema, "capability"), [])
        for invalid in ("a" * 39, "a" * 41, "A" * 40, "HEAD", "deadbeef"):
            item = copy.deepcopy(self.valid)
            item["assessment_scope"]["basis_commit"] = invalid  # type: ignore[index]
            with self.subTest(invalid=invalid):
                self.assert_schema_invalid(item)

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

    def test_terminal_controls_fail_reconstruction_text_and_ids(self) -> None:
        for control in ("\n", "\r", "\x01", "\x85"):
            text_item = copy.deepcopy(self.valid)
            text_item["assessment_scope"]["source_boundary"] += control  # type: ignore[index,operator]
            id_item = copy.deepcopy(self.valid)
            id_item["assessment_id"] += control  # type: ignore[operator]
            for label, item in (("text", text_item), ("id", id_item)):
                with self.subTest(control=repr(control), label=label):
                    self.assert_schema_invalid(item)

    def test_terminal_lf_fails_every_reconstruction_string_grammar(self) -> None:
        mutations = {
            "entity_id": lambda item: item.__setitem__(
                "character_entity_id", ENTITY + "\n"
            ),
            "subject_id": lambda item: item.__setitem__(
                "analysis_subject_id", SUBJECT + "\n"
            ),
            "evidence_ref": lambda item: item["evidence_refs"].__setitem__(
                0, EVIDENCE_REF + "\n"
            ),
            "basis_commit": lambda item: item["assessment_scope"].__setitem__(
                "basis_commit", "a" * 40 + "\n"
            ),
            "evidence_set_hash": lambda item: item["assessment_scope"].__setitem__(
                "evidence_set_sha256", GOLDEN_EVIDENCE_SET_SHA256 + "\n"
            ),
            "method_version": lambda item: item["assessment_scope"].__setitem__(
                "assessment_method_version", "1.0.0\n"
            ),
        }
        for name, mutate in mutations.items():
            item = copy.deepcopy(self.valid)
            mutate(item)
            with self.subTest(name=name):
                self.assert_schema_invalid(item)

    def test_dimension_claim_conditionals_fail_closed(self) -> None:
        assessed_without_evidence = copy.deepcopy(self.valid)
        assessed_without_evidence["dimensions"][0]["evidence_refs"] = []  # type: ignore[index]
        self.assert_schema_invalid(assessed_without_evidence)

        unassessed_with_evidence = copy.deepcopy(self.valid)
        unassessed_with_evidence["dimensions"][1]["evidence_refs"] = [EVIDENCE_REF]  # type: ignore[index]
        self.assert_schema_invalid(unassessed_with_evidence)

    def test_scenario_conditionals_fail_closed(self) -> None:
        conditional_without_conditions = copy.deepcopy(self.valid)
        claim = conditional_without_conditions["scenario_readiness"][0]  # type: ignore[index]
        claim["state"] = "CONDITIONAL"
        claim["evidence_refs"] = [EVIDENCE_REF]
        self.assert_schema_invalid(conditional_without_conditions)

        nonconditional_with_conditions = copy.deepcopy(self.valid)
        claim = nonconditional_with_conditions["scenario_readiness"][0]  # type: ignore[index]
        claim["state"] = "READY"
        claim["evidence_refs"] = [EVIDENCE_REF]
        claim["conditions"] = ["Only after episode 4"]
        self.assert_schema_invalid(nonconditional_with_conditions)

    def test_known_limit_reference_conditionals_fail_closed(self) -> None:
        backed_without_evidence = copy.deepcopy(self.valid)
        backed_without_evidence["known_limits"] = [
            {
                "limit_id": "boundary",
                "statement": "Evidence is bounded.",
                "support_kind": "EVIDENCE_BACKED",
                "evidence_refs": [],
            }
        ]
        self.assert_schema_invalid(backed_without_evidence)

        gap_with_evidence = copy.deepcopy(self.valid)
        gap_with_evidence["known_limits"] = [
            {
                "limit_id": "gap",
                "statement": "No mundane-behavior evidence.",
                "support_kind": "EVIDENCE_GAP",
                "evidence_refs": [EVIDENCE_REF],
            }
        ]
        self.assert_schema_invalid(gap_with_evidence)

    def test_assessment_status_invariants_fail_closed(self) -> None:
        unassessed_with_grade = copy.deepcopy(self.valid)
        unassessed_with_grade["assessment_status"] = "UNASSESSED"
        self.assert_schema_invalid(unassessed_with_grade)

        reviewed_without_union = copy.deepcopy(self.valid)
        reviewed_without_union["evidence_refs"] = []
        reviewed_without_union["dimensions"][0]["evidence_refs"] = []
        self.assert_schema_invalid(reviewed_without_union)

        stale_without_reason = copy.deepcopy(self.valid)
        stale_without_reason["assessment_status"] = "STALE"
        self.assert_schema_invalid(stale_without_reason)

        superseded_without_successor = copy.deepcopy(self.valid)
        superseded_without_successor["assessment_status"] = "SUPERSEDED"
        self.assert_schema_invalid(superseded_without_successor)

        plus_grade = copy.deepcopy(self.valid)
        plus_grade["overall_tier"] = "A+"
        self.assert_schema_invalid(plus_grade)


@unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
class GitBoundCapabilityTests(unittest.TestCase):
    def setUp(self) -> None:
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value:
            self.skipTest("MANGA_ANIME_TEST_TMP is not set")
        base = Path(base_value)
        if not base.is_absolute() or not base.is_dir() or base.is_symlink():
            self.skipTest("MANGA_ANIME_TEST_TMP must name an existing absolute real directory")
        self.base = base.resolve(strict=True)
        self.temporary = tempfile.mkdtemp(prefix="character-capability-", dir=self.base)
        self.repository = Path(self.temporary).resolve(strict=True)
        if not self.repository.is_relative_to(self.base):
            self.fail("temporary repository escaped MANGA_ANIME_TEST_TMP")
        self._git("init", "--quiet")
        self._git("config", "user.name", "Character Index Test")
        self._git("config", "user.email", "character-index-test.invalid@example.invalid")
        self._git("config", "core.autocrlf", "false")
        self._git("config", "core.safecrlf", "true")
        artifact = self.repository / Path(EVIDENCE_PATH)
        artifact.parent.mkdir(parents=True)
        artifact.write_bytes(authority_artifact())
        self.record = discovery_record()
        registry = self.repository / "characters" / "registry.jsonl"
        registry.parent.mkdir(parents=True)
        registry.write_text(
            json.dumps(self.record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        schema = self.repository / "governance" / "schemas" / "character-analysis-index.schema.json"
        schema.parent.mkdir(parents=True)
        schema.write_bytes(
            (REPOSITORY / "governance/schemas/character-analysis-index.schema.json").read_bytes()
        )
        series = self.repository / "series" / "registry.json"
        series.parent.mkdir(parents=True, exist_ok=True)
        series.write_text(
            json.dumps({"series": [{"series_id": "example"}]}, separators=(",", ":"))
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self._git(
            "add",
            "--",
            EVIDENCE_PATH,
            "characters/registry.jsonl",
            "governance/schemas/character-analysis-index.schema.json",
            "series/registry.json",
        )
        self._git("commit", "--quiet", "-m", "test evidence")
        self.commit = self._git_output("rev-parse", "HEAD")
        snapshot = GitSnapshot.from_commit(self.repository, self.commit)
        entries = resolve_evidence_entries([EVIDENCE_REF], [self.record], snapshot)
        self.digest, _ = evidence_set_digest(entries)

    def tearDown(self) -> None:
        temporary = getattr(self, "temporary", None)
        repository = getattr(self, "repository", None)
        base = getattr(self, "base", None)
        if temporary and repository and base and repository.is_relative_to(base):
            def clear_readonly(function, path, _exception):
                os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
                function(path)

            shutil.rmtree(temporary, onexc=clear_readonly)

    def _git(self, *args: str) -> None:
        subprocess.run(
            ["git", "-C", str(self.repository), *args],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )

    def _git_output(self, *args: str) -> str:
        return subprocess.check_output(
            ["git", "-C", str(self.repository), *args],
            stderr=subprocess.PIPE,
            text=True,
        ).strip()

    def test_exact_claim_union_accepts_exact_set_and_rejects_extra_or_omitted(self) -> None:
        valid = assessment(self.commit, self.digest)
        self.assertEqual(
            validate_reconstruction_assessments([valid], [self.record], self.repository),
            [],
        )

        omitted = copy.deepcopy(valid)
        omitted["evidence_refs"] = []
        failures = validate_reconstruction_assessments(
            [omitted], [self.record], self.repository
        )
        self.assertTrue(any("canonical exact union" in item for item in failures), failures)

        extra = copy.deepcopy(valid)
        extra_ref = f"{SUBJECT}#secondary"
        extra["evidence_refs"] = [EVIDENCE_REF, extra_ref]
        failures = validate_reconstruction_assessments(
            [extra], [self.record], self.repository
        )
        self.assertTrue(any("canonical exact union" in item for item in failures), failures)

    def test_controlled_claim_coverage_and_limit_ids_are_unique(self) -> None:
        item = assessment(self.commit, self.digest)
        item["dimensions"][1]["dimension"] = item["dimensions"][0]["dimension"]
        item["scenario_readiness"][1]["scenario"] = item["scenario_readiness"][0]["scenario"]
        item["known_limits"] = [
            {
                "limit_id": "same",
                "statement": "First",
                "support_kind": "EVIDENCE_GAP",
                "evidence_refs": [],
            },
            {
                "limit_id": "same",
                "statement": "Second",
                "support_kind": "EVIDENCE_GAP",
                "evidence_refs": [],
            },
        ]
        failures = validate_reconstruction_assessments(
            [item], [self.record], self.repository
        )
        self.assertTrue(any("every controlled dimension" in error for error in failures), failures)
        self.assertTrue(any("every category" in error for error in failures), failures)
        self.assertTrue(any("duplicate known-limit" in error for error in failures), failures)

    def test_abbreviated_basis_commit_fails_before_resolution(self) -> None:
        item = assessment(self.commit[:12], self.digest)
        failures = validate_reconstruction_assessments([item], [self.record], self.repository)
        self.assertTrue(any("basis commit must be a full" in item for item in failures), failures)

    def test_full_blob_object_id_is_not_a_basis_commit(self) -> None:
        blob_id = self._git_output("rev-parse", f"HEAD:{EVIDENCE_PATH}")
        item = assessment(blob_id, self.digest)
        failures = validate_reconstruction_assessments([item], [self.record], self.repository)
        self.assertTrue(any("basis object is not a commit" in item for item in failures), failures)

    def test_composite_cannot_borrow_leaf_evidence(self) -> None:
        second_leaf_id = "example:alice@novel"
        leaf = discovery_record()
        second_leaf = discovery_record(
            second_leaf_id,
            continuity_id="novel",
            evidence_path=None,
        )
        composite_id = "example:alice@composite"
        composite = discovery_record(
            composite_id,
            continuity_id=None,
            subject_kind="COMPOSITE_MODEL",
            evidence_path=None,
        )
        composite["component_subject_ids"] = [SUBJECT, second_leaf_id]
        registry = self.repository / "characters" / "registry.jsonl"
        registry.write_text(
            "".join(
                json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
                + "\n"
                for item in (leaf, second_leaf, composite)
            ),
            encoding="utf-8",
            newline="\n",
        )
        self._git("add", "--", "characters/registry.jsonl")
        self._git("commit", "--quiet", "-m", "add composite subjects")
        self.commit = self._git_output("rev-parse", "HEAD")
        borrowed = assessment(
            self.commit,
            self.digest,
            subject_id=composite_id,
            evidence_ref=EVIDENCE_REF,
        )
        scope = borrowed["assessment_scope"]  # type: ignore[assignment]
        scope["continuity_id"] = None
        scope["component_subject_ids"] = [SUBJECT, second_leaf_id]
        failures = validate_reconstruction_assessments(
            [borrowed], [leaf, second_leaf, composite], self.repository
        )
        self.assertTrue(any("belongs to another subject" in item for item in failures), failures)

    def test_duplicate_subject_or_evidence_in_basis_registry_fails_closed(self) -> None:
        registry = self.repository / "characters" / "registry.jsonl"
        duplicate_subject = json.dumps(
            self.record, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        )
        registry.write_text(
            duplicate_subject + "\n" + duplicate_subject + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self._git("add", "--", "characters/registry.jsonl")
        self._git("commit", "--quiet", "-m", "duplicate subject")
        duplicate_subject_commit = self._git_output("rev-parse", "HEAD")
        item = assessment(duplicate_subject_commit, self.digest)
        failures = validate_reconstruction_assessments([item], [self.record], self.repository)
        self.assertTrue(
            any("duplicate analysis_subject_id" in error for error in failures), failures
        )

    def test_duplicate_evidence_id_in_basis_registry_fails_closed(self) -> None:
        duplicate = copy.deepcopy(self.record)
        second = copy.deepcopy(duplicate["evidence"][0])
        second["label"] = "Second label"
        duplicate["evidence"].append(second)
        registry = self.repository / "characters" / "registry.jsonl"
        registry.write_text(
            json.dumps(duplicate, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
        self._git("add", "--", "characters/registry.jsonl")
        self._git("commit", "--quiet", "-m", "duplicate evidence")
        duplicate_evidence_commit = self._git_output("rev-parse", "HEAD")
        item = assessment(duplicate_evidence_commit, self.digest)
        failures = validate_reconstruction_assessments([item], [duplicate], self.repository)
        self.assertTrue(any("duplicate evidence_id" in error for error in failures), failures)

    def test_historical_stale_assessment_reproduces_after_subject_removal(self) -> None:
        historical = assessment(self.commit, self.digest)
        historical["assessment_status"] = "STALE"
        historical["stale_reason"] = "The subject was removed from the comparison registry."
        registry = self.repository / "characters" / "registry.jsonl"
        registry.write_text("", encoding="utf-8", newline="\n")
        self._git("add", "--", "characters/registry.jsonl")
        self._git("commit", "--quiet", "-m", "remove subject")
        comparison = self._git_output("rev-parse", "HEAD")
        self.assertEqual(
            validate_reconstruction_assessments(
                [historical],
                [],
                self.repository,
                comparison_commit=comparison,
            ),
            [],
        )

    def test_historical_superseded_assessment_reproduces_after_subject_removal(self) -> None:
        predecessor = assessment(self.commit, self.digest)
        predecessor["assessment_id"] = "alice-historical"
        predecessor["assessment_status"] = "SUPERSEDED"
        predecessor["superseded_by_assessment_id"] = "alice-successor"
        successor = assessment(self.commit, self.digest)
        successor["assessment_id"] = "alice-successor"
        successor["assessment_status"] = "STALE"
        successor["stale_reason"] = "The subject was removed from the comparison registry."
        successor["supersedes_assessment_id"] = "alice-historical"
        registry = self.repository / "characters" / "registry.jsonl"
        registry.write_text("", encoding="utf-8", newline="\n")
        self._git("add", "--", "characters/registry.jsonl")
        self._git("commit", "--quiet", "-m", "remove superseded subject")
        comparison = self._git_output("rev-parse", "HEAD")
        self.assertEqual(
            validate_reconstruction_assessments(
                [predecessor, successor],
                [],
                self.repository,
                comparison_commit=comparison,
            ),
            [],
        )

    def test_authority_graph_only_change_requires_reviewed_assessment_to_be_stale(self) -> None:
        reviewed = assessment(self.commit, self.digest)
        basis_snapshot = GitSnapshot.from_commit(self.repository, self.commit)
        basis_artifact_hash = basis_snapshot.artifact_sha256(EVIDENCE_PATH)
        successor_path = "series/example/ALICE-NEW.md"
        successor = self.repository / Path(successor_path)
        successor.write_bytes(
            (
                "---\n"
                "status: canonical\n"
                f"supersedes: [{EVIDENCE_PATH}]\n"
                "superseded_by: []\n"
                "do_not_use_as_current_authority: false\n"
                "---\n# Successor\n"
            ).encode("utf-8")
        )
        self._git("add", "--", successor_path)
        self._git("commit", "--quiet", "-m", "add incoming supersession edge")
        comparison = self._git_output("rev-parse", "HEAD")
        comparison_snapshot = GitSnapshot.from_commit(self.repository, comparison)
        self.assertEqual(
            comparison_snapshot.artifact_sha256(EVIDENCE_PATH), basis_artifact_hash
        )
        comparison_entries = resolve_evidence_entries(
            [EVIDENCE_REF], [self.record], comparison_snapshot
        )
        comparison_digest, _ = evidence_set_digest(comparison_entries)
        self.assertEqual(comparison_digest, self.digest)
        failures = validate_reconstruction_assessments(
            [reviewed],
            [self.record],
            self.repository,
            comparison_commit=comparison,
        )
        self.assertTrue(any("requires STALE" in error for error in failures), failures)

    def test_provisional_to_canonical_committed_byte_change_changes_digest(self) -> None:
        artifact = self.repository / Path(EVIDENCE_PATH)
        artifact.write_bytes(
            authority_artifact().replace(b"status: canonical\n", b"status: active_provisional\n")
        )
        self._git("add", "--", EVIDENCE_PATH)
        self._git("commit", "--quiet", "-m", "provisional authority")
        provisional_commit = self._git_output("rev-parse", "HEAD")
        provisional_snapshot = GitSnapshot.from_commit(self.repository, provisional_commit)
        provisional_entries = resolve_evidence_entries(
            [EVIDENCE_REF], [self.record], provisional_snapshot
        )
        provisional_digest, _ = evidence_set_digest(provisional_entries)
        provisional_artifact_hash = provisional_snapshot.artifact_sha256(EVIDENCE_PATH)

        artifact.write_bytes(authority_artifact())
        self._git("add", "--", EVIDENCE_PATH)
        self._git("commit", "--quiet", "-m", "canonical authority")
        canonical_commit = self._git_output("rev-parse", "HEAD")
        canonical_snapshot = GitSnapshot.from_commit(self.repository, canonical_commit)
        canonical_entries = resolve_evidence_entries(
            [EVIDENCE_REF], [self.record], canonical_snapshot
        )
        canonical_digest, _ = evidence_set_digest(canonical_entries)
        self.assertNotEqual(
            provisional_artifact_hash,
            canonical_snapshot.artifact_sha256(EVIDENCE_PATH),
        )
        self.assertNotEqual(provisional_digest, canonical_digest)

    def test_reciprocal_supersession_rejects_incompatible_subject_scope(self) -> None:
        old = assessment(self.commit, self.digest)
        old["assessment_id"] = "alice-old"
        old["assessment_status"] = "SUPERSEDED"
        old["superseded_by_assessment_id"] = "alice-new"
        new = assessment(self.commit, self.digest)
        new["assessment_id"] = "alice-new"
        new["supersedes_assessment_id"] = "alice-old"
        new["assessment_scope"]["continuity_id"] = "novel"
        failures = validate_reconstruction_assessments(
            [old, new], [self.record], self.repository
        )
        self.assertTrue(
            any("supersession has incompatible subject scope" in error for error in failures),
            failures,
        )

    def test_assessment_supersession_cycle_fails(self) -> None:
        first = assessment(self.commit, self.digest)
        first["assessment_id"] = "alice-first"
        first["assessment_status"] = "SUPERSEDED"
        first["supersedes_assessment_id"] = "alice-second"
        first["superseded_by_assessment_id"] = "alice-second"
        second = assessment(self.commit, self.digest)
        second["assessment_id"] = "alice-second"
        second["assessment_status"] = "SUPERSEDED"
        second["supersedes_assessment_id"] = "alice-first"
        second["superseded_by_assessment_id"] = "alice-first"
        failures = validate_reconstruction_assessments(
            [first, second], [self.record], self.repository
        )
        self.assertTrue(any("supersession cycle" in error for error in failures), failures)

    def test_unresolved_and_one_sided_assessment_links_fail_closed(self) -> None:
        missing_successor = assessment(self.commit, self.digest)
        missing_successor["assessment_id"] = "alice-missing-successor"
        missing_successor["assessment_status"] = "SUPERSEDED"
        missing_successor["superseded_by_assessment_id"] = "not-present"
        failures = validate_reconstruction_assessments(
            [missing_successor], [self.record], self.repository
        )
        self.assertTrue(any("unresolved/nonreciprocal" in error for error in failures), failures)

        missing_predecessor = assessment(self.commit, self.digest)
        missing_predecessor["assessment_id"] = "alice-missing-predecessor"
        missing_predecessor["supersedes_assessment_id"] = "not-present"
        failures = validate_reconstruction_assessments(
            [missing_predecessor], [self.record], self.repository
        )
        self.assertTrue(any("unresolved/nonreciprocal" in error for error in failures), failures)

        old = assessment(self.commit, self.digest)
        old["assessment_id"] = "alice-one-sided-old"
        old["assessment_status"] = "SUPERSEDED"
        old["superseded_by_assessment_id"] = "alice-one-sided-new"
        new = assessment(self.commit, self.digest)
        new["assessment_id"] = "alice-one-sided-new"
        failures = validate_reconstruction_assessments(
            [old, new], [self.record], self.repository
        )
        self.assertTrue(any("unresolved/nonreciprocal" in error for error in failures), failures)

    def test_supersession_allows_revision_of_source_and_temporal_boundaries(self) -> None:
        old = assessment(self.commit, self.digest)
        old["assessment_id"] = "alice-old"
        old["assessment_status"] = "SUPERSEDED"
        old["superseded_by_assessment_id"] = "alice-new"
        new = assessment(self.commit, self.digest)
        new["assessment_id"] = "alice-new"
        new["supersedes_assessment_id"] = "alice-old"
        new["assessment_scope"]["source_boundary"] = "Expanded reviewed profile"
        new["assessment_scope"]["temporal_boundary"] = "Through episode 12"
        self.assertEqual(
            validate_reconstruction_assessments(
                [old, new], [self.record], self.repository
            ),
            [],
        )


class DeliberateNonpopulationTests(unittest.TestCase):
    def test_production_capability_surfaces_do_not_exist(self) -> None:
        for relative in (
            "characters/reconstruction_capabilities.jsonl",
            "characters/CHARACTER_RECONSTRUCTION_INDEX.md",
        ):
            path = REPOSITORY / relative
            self.assertFalse(path.exists() or path.is_symlink(), relative)


if __name__ == "__main__":
    unittest.main()
