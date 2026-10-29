from __future__ import annotations

import contextlib
import copy
import hashlib
import io
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
    RECONSTRUCTION_INDEX_PATH,
    RECONSTRUCTION_POLICY_PATH,
    RECONSTRUCTION_REGISTRY_PATH,
    RECONSTRUCTION_SCHEMA_PATH,
    AssessmentCurrentness,
    AuthorityGraph,
    DomainError,
    GitSnapshot,
    ReconstructionEvaluation,
    SnapshotEntry,
    decode_reconstruction_registry,
    evaluate_reconstruction_assessments,
    evidence_set_digest,
    is_discovery_output,
    load_reconstruction_policy,
    parse_evidence_ref,
    read_discovery_registry,
    reconstruction_registry_changes,
    resolve_evidence_entries,
    schema_errors,
    validate_evidence_path,
    validate_reconstruction_assessments,
)
from generate_reconstruction_index import (  # noqa: E402
    load_and_render,
    render as render_reconstruction_index,
)
from prepare_commit import active_rules, missing_required_output_paths  # noqa: E402
from reconstruction_status import (  # noqa: E402
    _discovery_at,
    deferred_evidence_changes,
    main as reconstruction_status_main,
    work_queue,
)
from validate_repository import (  # noqa: E402
    RECONSTRUCTION_OUTPUTS,
    discovery_branch_candidate,
    discovery_confinement_errors,
    validate_audit_workflow,
    validate_discovery_branch_confinement,
    validate_reconstruction_domain,
    validate_routing_branch_scope,
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
    curation_status: str = "CANDIDATE",
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
        "curation_status": curation_status,
        "inclusion_basis": "DEDICATED" if curation_status == "INCLUDED" else None,
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


class GitRepositoryFixture(unittest.TestCase):
    """A disposable repository with one reviewed canonical evidence artifact."""

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
        self.record = discovery_record(curation_status="INCLUDED")
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

    def _write_registry(self, records: list[dict[str, object]]) -> None:
        registry = self.repository / "characters" / "registry.jsonl"
        registry.write_text(
            "".join(
                json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
                for item in records
            ),
            encoding="utf-8",
            newline="\n",
        )

    def _commit(self, message: str, *paths: str) -> str:
        self._git("add", "--", *paths)
        self._git("commit", "--quiet", "-m", message)
        return self._git_output("rev-parse", "HEAD")

    def _migrate_registry(self) -> str:
        """Commit the fixture's move from the retired single file to its partition."""

        legacy = self.repository / "characters" / "registry.jsonl"
        partition = self.repository / "characters" / "registry" / "example.jsonl"
        partition.parent.mkdir(parents=True, exist_ok=True)
        partition.write_bytes(legacy.read_bytes())
        legacy.unlink()
        return self._commit(
            "partition the discovery registry",
            "characters/registry.jsonl",
            "characters/registry/example.jsonl",
        )


@unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
class GitBoundCapabilityTests(GitRepositoryFixture):
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


def candidate(basis_commit: str, digest: str, assessment_id: str = "alice-anime-v1") -> dict[str, object]:
    item = assessment(basis_commit, digest)
    item["assessment_id"] = assessment_id
    item["assessment_status"] = "CANDIDATE"
    return item


def unassessed(basis_commit: str) -> dict[str, object]:
    item = assessment(basis_commit, EMPTY_EVIDENCE_SET_SHA256)
    item["assessment_status"] = "UNASSESSED"
    item["overall_tier"] = "NOT_ASSESSED"
    item["evidence_refs"] = []
    for claim in item["dimensions"]:  # type: ignore[union-attr]
        claim["grade"] = "NOT_ASSESSED"
        claim["evidence_refs"] = []
    return item


EMPTY_EVIDENCE_SET_SHA256 = (
    "50dc6ac299e4602ee01b3b702a11e64c69cf52fe50182911eca4a377468b30d2"
)


@unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
class EffectiveCurrentnessTests(GitRepositoryFixture):
    """Historical validity is reproducible; currentness is derived per snapshot."""

    def _evaluate(
        self,
        item: dict[str, object],
        comparison_commit: str,
        records: list[dict[str, object]] | None = None,
    ):
        comparison = GitSnapshot.from_commit(self.repository, comparison_commit)
        return evaluate_reconstruction_assessments(
            [item],
            self.repository,
            comparison=comparison,
            comparison_records=[self.record] if records is None else records,
        )

    def _write_evidence(self, path: str, data: bytes) -> None:
        target = self.repository / Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def test_unrelated_commit_leaves_reviewed_assessment_current(self) -> None:
        self._write_evidence("series/example/UNRELATED.md", authority_artifact(b"# Other\n"))
        comparison = self._commit("unrelated analysis", "series/example/UNRELATED.md")
        result = self._evaluate(assessment(self.commit, self.digest), comparison)
        self.assertEqual(result.errors, [])
        self.assertEqual(result.currentness[0].effective_state, "CURRENT_REVIEWED")
        self.assertEqual(result.currentness[0].reasons, ())

    def test_partition_migration_keeps_single_file_basis_assessments_current(self) -> None:
        migrated = self._migrate_registry()
        current = read_discovery_registry(GitSnapshot.from_commit(self.repository, migrated))
        self.assertEqual(current.records, [self.record])
        result = self._evaluate(assessment(self.commit, self.digest), migrated, current.records)
        self.assertEqual(result.errors, [])
        self.assertEqual(result.currentness[0].effective_state, "CURRENT_REVIEWED")
        self.assertEqual(result.currentness[0].reasons, ())
        # A basis commit in the partitioned layout binds the same evidence set.
        rebased = self._evaluate(assessment(migrated, self.digest), migrated)
        self.assertEqual(rebased.errors, [])
        self.assertEqual(rebased.currentness[0].effective_state, "CURRENT_REVIEWED")

    def test_checkpoint_reads_follow_the_registry_layout_of_each_commit(self) -> None:
        migrated = self._migrate_registry()
        for commit in (self.commit, migrated):
            with self.subTest(commit=commit):
                self.assertEqual(_discovery_at(self.repository, commit), {SUBJECT: self.record})

    def test_candidate_is_current_but_visibly_provisional(self) -> None:
        result = self._evaluate(candidate(self.commit, self.digest), self.commit)
        self.assertEqual(result.errors, [])
        self.assertEqual(result.currentness[0].effective_state, "CURRENT_PROVISIONAL")
        self.assertTrue(result.currentness[0].effectively_current)

    def test_referenced_byte_change_is_stale_while_history_stays_valid(self) -> None:
        self._write_evidence(EVIDENCE_PATH, authority_artifact(b"# Revised analysis\n"))
        comparison = self._commit("revise evidence", EVIDENCE_PATH)
        result = self._evaluate(assessment(self.commit, self.digest), comparison)
        self.assertEqual(result.errors, [])
        self.assertEqual(result.currentness[0].effective_state, "EFFECTIVELY_STALE")
        self.assertIn("EVIDENCE_BYTES_CHANGED", result.currentness[0].reasons)

    def test_evidence_path_and_anchor_changes_are_location_changes(self) -> None:
        moved = copy.deepcopy(self.record)
        moved["evidence"][0]["repository_path"] = "series/example/ALICE-MOVED.md"  # type: ignore[index]
        anchored = copy.deepcopy(self.record)
        anchored["evidence"][0]["anchor"] = "psychology"  # type: ignore[index]
        for label, record in (("path", moved), ("anchor", anchored)):
            with self.subTest(label=label):
                result = self._evaluate(assessment(self.commit, self.digest), self.commit, [record])
                self.assertEqual(result.errors, [])
                self.assertIn("EVIDENCE_LOCATION_CHANGED", result.currentness[0].reasons)
                self.assertIn("EVIDENCE_MEMBERSHIP_CHANGED", result.currentness[0].reasons)

    def test_authority_edge_without_byte_change_is_stale(self) -> None:
        successor_path = "series/example/ALICE-NEW.md"
        self._write_evidence(
            successor_path,
            (
                "---\nstatus: canonical\n"
                f"supersedes: [{EVIDENCE_PATH}]\n"
                "superseded_by: []\ndo_not_use_as_current_authority: false\n---\n# Successor\n"
            ).encode("utf-8"),
        )
        comparison = self._commit("supersede evidence", successor_path)
        result = self._evaluate(assessment(self.commit, self.digest), comparison)
        self.assertEqual(result.errors, [])
        self.assertEqual(result.currentness[0].reasons, ("EVIDENCE_AUTHORITY_NONCURRENT",))

    def test_subject_scope_removal_and_membership_changes_are_stale(self) -> None:
        rescoped = copy.deepcopy(self.record)
        rescoped["continuity_id"] = "novel"
        expanded = copy.deepcopy(self.record)
        extra = copy.deepcopy(expanded["evidence"][0])  # type: ignore[index]
        extra["evidence_id"] = "secondary"
        expanded["evidence"].append(extra)  # type: ignore[union-attr]
        excluded = copy.deepcopy(self.record)
        excluded["curation_status"] = "EXCLUDED_REVIEWED"
        cases = (
            ("scope", [rescoped], "SUBJECT_SCOPE_CHANGED"),
            ("removed", [], "SUBJECT_ABSENT"),
            ("membership", [expanded], "EVIDENCE_MEMBERSHIP_CHANGED"),
            ("curation", [excluded], "SUBJECT_CURATION_CHANGED"),
            ("not-included", [excluded], "SUBJECT_NOT_INCLUDED"),
        )
        for label, records, reason in cases:
            with self.subTest(label=label):
                result = self._evaluate(assessment(self.commit, self.digest), self.commit, records)
                self.assertEqual(result.errors, [])
                self.assertIn(reason, result.currentness[0].reasons)
                self.assertFalse(result.currentness[0].effectively_current)

    def test_current_claims_require_an_included_basis_subject(self) -> None:
        candidate_subject = discovery_record()
        self._write_registry([candidate_subject])
        basis = self._commit("subject is only a discovery candidate", "characters/registry.jsonl")
        snapshot = GitSnapshot.from_commit(self.repository, basis)
        entries = resolve_evidence_entries([EVIDENCE_REF], [candidate_subject], snapshot)
        digest, _ = evidence_set_digest(entries)
        for item in (candidate(basis, digest), assessment(basis, digest)):
            with self.subTest(status=item["assessment_status"]):
                result = evaluate_reconstruction_assessments([item], self.repository)
                self.assertTrue(
                    any("requires an INCLUDED basis discovery subject" in error for error in result.errors),
                    result.errors,
                )
        historical = assessment(basis, digest)
        historical["assessment_status"] = "STALE"
        historical["stale_reason"] = "The subject was never enrolled."
        self.assertEqual(evaluate_reconstruction_assessments([historical], self.repository).errors, [])

    def test_unreferenced_discovery_metadata_edit_is_not_stale(self) -> None:
        relabeled = copy.deepcopy(self.record)
        relabeled["evidence"][0]["label"] = "Profile, relabeled"  # type: ignore[index]
        relabeled["notes"] = "Discovery note revised without changing evidence."
        result = self._evaluate(assessment(self.commit, self.digest), self.commit, [relabeled])
        self.assertEqual(result.currentness[0].effective_state, "CURRENT_REVIEWED")

    def test_recorded_stale_assessment_remains_reproducible_and_historical(self) -> None:
        self._write_evidence(EVIDENCE_PATH, authority_artifact(b"# Revised analysis\n"))
        comparison = self._commit("revise evidence", EVIDENCE_PATH)
        item = assessment(self.commit, self.digest)
        item["assessment_status"] = "STALE"
        item["stale_reason"] = "Referenced evidence changed after the basis commit."
        result = self._evaluate(item, comparison)
        self.assertEqual(result.errors, [])
        self.assertEqual(result.currentness[0].effective_state, "RECORDED_STALE")
        self.assertFalse(result.currentness[0].effectively_current)

    def test_basis_must_belong_to_the_integrated_history(self) -> None:
        self._git("switch", "--quiet", "-c", "series/example")
        self._write_evidence(EVIDENCE_PATH, authority_artifact(b"# Unmerged analysis\n"))
        unmerged = self._commit("unmerged evidence", EVIDENCE_PATH)
        self._git("switch", "--quiet", "-")
        snapshot = GitSnapshot.from_commit(self.repository, unmerged)
        entries = resolve_evidence_entries([EVIDENCE_REF], [self.record], snapshot)
        digest, _ = evidence_set_digest(entries)
        result = evaluate_reconstruction_assessments(
            [candidate(unmerged, digest)], self.repository, basis_ancestor_of=self.commit
        )
        self.assertTrue(any("not an ancestor" in error for error in result.errors), result.errors)


class RegistryContractTests(unittest.TestCase):
    def _record(self, assessment_id: str, status: str = "CANDIDATE") -> dict[str, object]:
        item = candidate("a" * 40, GOLDEN_EVIDENCE_SET_SHA256, assessment_id)
        item["assessment_status"] = status
        return item

    def _line(self, record: dict[str, object]) -> bytes:
        return json.dumps(record, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"

    def test_empty_bootstrap_registry_is_valid_and_unpopulated(self) -> None:
        self.assertEqual(decode_reconstruction_registry(b"", "registry"), [])

    def test_registry_layout_is_ordered_unique_and_lf_terminated(self) -> None:
        first, second = self._record("a-first"), self._record("b-second")
        self.assertEqual(
            len(decode_reconstruction_registry(self._line(first) + self._line(second), "registry")), 2
        )
        invalid = {
            "order": self._line(second) + self._line(first),
            "duplicate": self._line(first) + self._line(first),
            "blank": self._line(first) + b"\n" + self._line(second),
            "terminal": self._line(first).rstrip(b"\n"),
        }
        for label, data in invalid.items():
            with self.subTest(label=label), self.assertRaises(DomainError):
                decode_reconstruction_registry(data, "registry")

    def test_published_records_are_preserved_and_claims_immutable(self) -> None:
        base = [self._record("alice-v1")]
        touched, errors = reconstruction_registry_changes(base, base)
        self.assertEqual((touched, errors), (set(), []))
        _touched, errors = reconstruction_registry_changes(base, [])
        self.assertTrue(any("was removed" in error for error in errors), errors)
        mutated = copy.deepcopy(base[0])
        mutated["overall_tier"] = "A"
        touched, errors = reconstruction_registry_changes(base, [mutated])
        self.assertEqual(touched, {"alice-v1"})
        self.assertTrue(any("immutable" in error for error in errors), errors)

    def test_lifecycle_transitions_are_bounded(self) -> None:
        allowed = (("CANDIDATE", "REVIEWED"), ("CANDIDATE", "STALE"), ("REVIEWED", "STALE"), ("STALE", "SUPERSEDED"))
        prohibited = (("REVIEWED", "CANDIDATE"), ("STALE", "REVIEWED"), ("SUPERSEDED", "STALE"))
        for before, after in allowed + prohibited:
            with self.subTest(before=before, after=after):
                previous = self._record("alice-v1", before)
                current = copy.deepcopy(previous)
                current["assessment_status"] = after
                touched, errors = reconstruction_registry_changes([previous], [current])
                self.assertEqual(touched, {"alice-v1"})
                self.assertEqual(bool(errors), (before, after) in prohibited, errors)
        stale = self._record("alice-v1", "STALE")
        stale["stale_reason"] = "First reason."
        edited = copy.deepcopy(stale)
        edited["stale_reason"] = "Rewritten reason."
        _touched, errors = reconstruction_registry_changes([stale], [edited])
        self.assertTrue(any("without a status transition" in error for error in errors), errors)

    def test_new_records_enter_only_as_candidates(self) -> None:
        touched, errors = reconstruction_registry_changes([], [self._record("alice-v1")])
        self.assertEqual((touched, errors), ({"alice-v1"}, []))
        for status in ("REVIEWED", "STALE", "SUPERSEDED"):
            with self.subTest(status=status):
                _touched, errors = reconstruction_registry_changes([], [self._record("alice-v1", status)])
                self.assertTrue(any("must enter as CANDIDATE" in error for error in errors), errors)
        old = self._record("alice-v0", "SUPERSEDED")
        old["superseded_by_assessment_id"] = "alice-v1"
        new = self._record("alice-v1")
        new["supersedes_assessment_id"] = "alice-v0"
        _touched, errors = reconstruction_registry_changes([], [old, new])
        self.assertTrue(any("must enter as CANDIDATE, not SUPERSEDED: alice-v0" in error for error in errors), errors)

    def test_publication_gate_requires_owner_calibration_record_for_routine(self) -> None:
        def snapshot(document: object, extra: dict[str, bytes] | None = None) -> GitSnapshot:
            entries = {
                RECONSTRUCTION_POLICY_PATH: SnapshotEntry(
                    RECONSTRUCTION_POLICY_PATH, "100644", json.dumps(document).encode("utf-8")
                )
            }
            for path, data in (extra or {}).items():
                entries[path] = SnapshotEntry(path, "100644", data)
            return GitSnapshot(REPOSITORY, "IN_MEMORY", entries)

        base = {
            "schema": "anime-manga-ln-games-analysis/reconstruction-capability-policy/v1",
            "publication_phase": "CALIBRATION",
            "calibration_acceptance_record": None,
        }
        self.assertEqual(load_reconstruction_policy(snapshot(base)), ("CALIBRATION", []))
        routine = dict(base, publication_phase="ROUTINE")
        self.assertTrue(load_reconstruction_policy(snapshot(routine))[1])
        record = "governance/reports/RECONSTRUCTION_CALIBRATION_ACCEPTANCE.md"
        accepted = dict(routine, calibration_acceptance_record=record)
        self.assertTrue(load_reconstruction_policy(snapshot(accepted))[1])
        self.assertEqual(
            load_reconstruction_policy(snapshot(accepted, {record: b"# Accepted\n"})),
            ("ROUTINE", []),
        )
        for invalid in (dict(base, publication_phase="OPEN"), dict(base, extra=True)):
            with self.subTest(invalid=invalid):
                self.assertTrue(load_reconstruction_policy(snapshot(invalid))[1])

    def test_index_projection_is_deterministic_provisional_and_link_safe(self) -> None:
        first = candidate("a" * 40, GOLDEN_EVIDENCE_SET_SHA256, "alice-v1")
        first["assessment_scope"]["source_boundary"] = "See [notes](series/missing.md) *only*"  # type: ignore[index]
        second = copy.deepcopy(first)
        second["assessment_id"] = "alice-v0"
        second["assessment_status"] = "STALE"
        second["stale_reason"] = "Evidence changed."
        entry = golden_entry()
        rendered = render_reconstruction_index([second, first], {0: [entry], 1: [entry]})
        self.assertEqual(rendered, render_reconstruction_index([first, second], {0: [entry], 1: [entry]}))
        self.assertIn("**provisional; not human-reviewed**", rendered)
        self.assertIn("provisional `B`", rendered)
        self.assertIn("historical `B`", rendered)
        self.assertLess(rendered.index("alice-v1"), rendered.index("alice-v0"))
        self.assertIn(
            "https://github.com/deep-blue-zero/anime-manga-ln-games-analysis/blob/"
            + "a" * 40
            + "/series/example/ALICE.md",
            rendered,
        )
        self.assertNotIn("](series/missing.md)", rendered)
        self.assertTrue(rendered.endswith("\n") and "\r" not in rendered)
        empty = render_reconstruction_index([], {})
        self.assertIn("No reconstruction capability assessments have been published", empty)
        self.assertNotIn("Recorded totals", empty)


class WorkDiscoveryTests(unittest.TestCase):
    def _discovery(self, subject: str, *, status: str = "INCLUDED") -> dict[str, object]:
        record = discovery_record(subject)
        record["curation_status"] = status
        return record

    def _queue(self, assessments, currentness, discovery, **kwargs):
        evaluation = ReconstructionEvaluation(
            errors=[], basis_entries={}, basis_records={}, currentness=currentness
        )
        return work_queue(assessments, discovery, evaluation, **kwargs)

    def test_git_derived_queue_needs_no_referrals_or_peer_checkpoint(self) -> None:
        stale_subject, fresh_subject, old_subject = (
            "example:alice@anime", "example:alice@novel", "example:alice@manga"
        )
        discovery = [self._discovery(item) for item in (stale_subject, fresh_subject, old_subject)]
        stale = candidate("a" * 40, GOLDEN_EVIDENCE_SET_SHA256)
        currentness = {
            0: AssessmentCurrentness(
                "alice-anime-v1", stale_subject, "CANDIDATE", "EFFECTIVELY_STALE",
                ("EVIDENCE_BYTES_CHANGED",),
            )
        }
        since = {
            subject: record for subject, record in
            ((stale_subject, discovery[0]), (old_subject, discovery[2]))
        }
        queue = self._queue([stale], currentness, discovery, since_records=since)
        self.assertEqual(
            [(item["analysis_subject_id"], item["kind"]) for item in queue["items"]],
            [
                (stale_subject, "EFFECTIVELY_STALE_ASSESSMENT"),
                (fresh_subject, "NEWLY_ELIGIBLE"),
                (old_subject, "BACKFILL_UNASSESSED"),
            ],
        )
        self.assertEqual(queue["items"][0]["reasons"], ["EVIDENCE_BYTES_CHANGED"])
        self.assertFalse(any(item["advisory_hint"] for item in queue["items"]))

    def test_duplicate_hints_never_duplicate_work_or_create_it(self) -> None:
        subject = "example:alice@anime"
        queue = self._queue(
            [], {}, [self._discovery(subject), self._discovery("example:bob@anime", status="CANDIDATE")],
            hints=[subject, subject, "example:bob@anime", "example:carol@anime"],
        )
        self.assertEqual([item["analysis_subject_id"] for item in queue["items"]], [subject])
        self.assertTrue(queue["items"][0]["advisory_hint"])
        self.assertEqual(queue["unenrolled_hints"], ["example:carol@anime"])

    def test_deferred_subjects_return_only_after_material_change(self) -> None:
        subject = "example:alice@anime"
        current = self._discovery(subject)
        changed = copy.deepcopy(current)
        changed["evidence"][0]["repository_path"] = "series/example/ALICE-V2.md"  # type: ignore[index]
        unchanged_queue = self._queue([], {}, [current], since_records={subject: current}, deferred=[subject])
        self.assertEqual(unchanged_queue["items"], [])
        self.assertEqual(unchanged_queue["subject_state_counts"], {"DEFERRED": 1})
        changed_queue = self._queue([], {}, [changed], since_records={subject: current}, deferred=[subject])
        self.assertEqual(changed_queue["items"][0]["kind"], "DEFERRED_EVIDENCE_CHANGED")

    def test_derived_states_distinguish_reviewed_pending_and_historical(self) -> None:
        reviewed = assessment("a" * 40, GOLDEN_EVIDENCE_SET_SHA256)
        pending = candidate("a" * 40, GOLDEN_EVIDENCE_SET_SHA256, "bob-v1")
        pending["analysis_subject_id"] = "example:bob@anime"
        historical = candidate("a" * 40, GOLDEN_EVIDENCE_SET_SHA256, "carol-v1")
        historical["analysis_subject_id"] = "example:carol@anime"
        historical["assessment_status"] = "SUPERSEDED"
        currentness = {
            0: AssessmentCurrentness("alice-anime-v1", SUBJECT, "REVIEWED", "CURRENT_REVIEWED", ()),
            1: AssessmentCurrentness("bob-v1", "example:bob@anime", "CANDIDATE", "CURRENT_PROVISIONAL", ()),
        }
        discovery = [self._discovery(item) for item in (SUBJECT, "example:bob@anime", "example:carol@anime")]
        queue = self._queue([reviewed, pending, historical], currentness, discovery)
        self.assertEqual(
            queue["subject_state_counts"],
            {"HISTORICAL_ONLY": 1, "HUMAN_REVIEWED_CURRENT": 1, "PENDING_PROVISIONAL": 1},
        )
        self.assertEqual(
            [(item["analysis_subject_id"], item["kind"]) for item in queue["items"]],
            [("example:carol@anime", "REASSESSMENT_NEEDED")],
        )


@unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
class ProductionRepositoryFixture(GitRepositoryFixture):
    """A disposable history with activated, empty production surfaces."""

    def setUp(self) -> None:
        super().setUp()
        for path in (RECONSTRUCTION_SCHEMA_PATH,):
            target = self.repository / Path(path)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((REPOSITORY / path).read_bytes())
        self._write_policy("CALIBRATION")
        self._publish([])
        self.main = self._commit(
            "activate production surfaces",
            RECONSTRUCTION_SCHEMA_PATH,
            RECONSTRUCTION_POLICY_PATH,
            RECONSTRUCTION_REGISTRY_PATH,
            RECONSTRUCTION_INDEX_PATH,
        )
        self._advance_main()

    def _advance_main(self) -> None:
        self.main = self._git_output("rev-parse", "HEAD")
        self._git("update-ref", "refs/remotes/origin/main", self.main)

    def _write_policy(self, phase: str) -> None:
        record = None
        if phase == "ROUTINE":
            record = "governance/reports/RECONSTRUCTION_CALIBRATION_ACCEPTANCE.md"
            target = self.repository / Path(record)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b"# Owner calibration acceptance\n")
        target = self.repository / Path(RECONSTRUCTION_POLICY_PATH)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(
                {
                    "schema": "anime-manga-ln-games-analysis/reconstruction-capability-policy/v1",
                    "publication_phase": phase,
                    "calibration_acceptance_record": record,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )

    def _publish(self, records: list[dict[str, object]], *, render: bool = True) -> None:
        registry = self.repository / Path(RECONSTRUCTION_REGISTRY_PATH)
        registry.parent.mkdir(parents=True, exist_ok=True)
        registry.write_bytes(
            b"".join(
                json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
                + b"\n"
                for item in records
            )
        )
        if render:
            evaluation = evaluate_reconstruction_assessments(records, self.repository)
            self.assertEqual(evaluation.errors, [])
            (self.repository / Path(RECONSTRUCTION_INDEX_PATH)).write_bytes(
                render_reconstruction_index(records, evaluation.basis_entries).encode("utf-8")
            )

    def _commit_outputs(self, message: str) -> str:
        return self._commit(message, RECONSTRUCTION_REGISTRY_PATH, RECONSTRUCTION_INDEX_PATH)

    def _validate(self) -> tuple[list[str], list[str]]:
        head = self._git_output("rev-parse", "HEAD")
        snapshot = GitSnapshot.from_commit(self.repository, head)
        return validate_reconstruction_domain(self.repository, snapshot, "commit", head, None)

    def _revise_evidence_on_main(self) -> None:
        (self.repository / Path(EVIDENCE_PATH)).write_bytes(authority_artifact(b"# Revised analysis\n"))
        self._commit("series analysis revises referenced evidence", EVIDENCE_PATH)
        self._advance_main()



@unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
class ProductionRepositoryTests(ProductionRepositoryFixture):
    """The repository validator's production contract on a disposable history."""

    def test_empty_bootstrap_state_validates(self) -> None:
        self.assertEqual(self._validate(), ([], []))

    def test_production_surfaces_are_required_and_index_drift_fails(self) -> None:
        self._git("rm", "--quiet", "--", RECONSTRUCTION_INDEX_PATH)
        self._git("commit", "--quiet", "-m", "remove index")
        errors, _ = self._validate()
        self.assertTrue(any("index is missing" in error for error in errors), errors)
        self._git("revert", "--no-edit", "HEAD")
        self._git("switch", "--quiet", "-c", "character-reconstruction")
        self._publish([candidate(self.commit, self.digest)], render=False)
        self._commit_outputs("registry without regenerated index")
        errors, _ = self._validate()
        self.assertTrue(any("is out of date" in error for error in errors), errors)

    def test_evaluator_candidate_publication_is_two_file_confined(self) -> None:
        self._git("switch", "--quiet", "-c", "character-reconstruction")
        self._publish([candidate(self.commit, self.digest)])
        self._commit_outputs("publish candidate")
        self.assertEqual(self._validate(), ([], []))
        edited = copy.deepcopy(self.record)
        edited["notes"] = "An evaluator must not edit discovery records."
        self._write_registry([edited])
        self._commit("evaluator also edits discovery", "characters/registry.jsonl")
        errors, _ = self._validate()
        self.assertTrue(any("must change alone" in error for error in errors), errors)

    def test_calibration_phase_rejects_reviewed_and_placeholders(self) -> None:
        self._git("switch", "--quiet", "-c", "character-reconstruction")
        self._publish([assessment(self.commit, self.digest)])
        self._commit_outputs("premature reviewed grade")
        errors, _ = self._validate()
        self.assertTrue(any("requires the ROUTINE phase" in error for error in errors), errors)
        self._publish([unassessed(self.commit)])
        self._commit_outputs("placeholder")
        errors, _ = self._validate()
        self.assertTrue(any("UNASSESSED" in error for error in errors), errors)

    def test_delayed_evaluator_maintenance_does_not_block_series_publication(self) -> None:
        self._publish([candidate(self.commit, self.digest)])
        self._commit_outputs("integrated candidate")
        self._advance_main()
        self._git("switch", "--quiet", "-c", "series/example")
        (self.repository / Path(EVIDENCE_PATH)).write_bytes(authority_artifact(b"# Revised analysis\n"))
        self._commit("series analysis revises referenced evidence", EVIDENCE_PATH)
        errors, notices = self._validate()
        self.assertEqual(errors, [])
        self.assertTrue(any("effectively stale" in notice for notice in notices), notices)

    def test_new_or_promoted_claims_must_be_current_and_stale_reconciles(self) -> None:
        self._write_policy("ROUTINE")
        self._commit(
            "owner accepts calibration",
            RECONSTRUCTION_POLICY_PATH,
            "governance/reports/RECONSTRUCTION_CALIBRATION_ACCEPTANCE.md",
        )
        published = candidate(self.commit, self.digest)
        self._publish([published])
        self._commit_outputs("integrated candidate")
        self._advance_main()
        self._revise_evidence_on_main()
        self._git("switch", "--quiet", "-c", "character-reconstruction")
        promoted = copy.deepcopy(published)
        promoted["assessment_status"] = "REVIEWED"
        self._publish([promoted])
        self._commit_outputs("promote a stale candidate")
        errors, _ = self._validate()
        self.assertTrue(any("not effectively current" in error for error in errors), errors)
        stale = copy.deepcopy(published)
        stale["assessment_status"] = "STALE"
        stale["stale_reason"] = "Referenced evidence changed after the basis commit."
        self._publish([stale])
        self._commit_outputs("record staleness")
        self.assertEqual(self._validate(), ([], []))

    def test_main_integration_audit_compares_with_the_pre_push_parent(self) -> None:
        self._revise_evidence_on_main()
        self._publish([candidate(self.commit, self.digest)])
        self._commit_outputs("integrated stale candidate")
        self._advance_main()
        errors, _ = self._validate()
        self.assertTrue(any("not effectively current" in error for error in errors), errors)
        self._publish([])
        self._commit_outputs("integrated deletion")
        self._advance_main()
        errors, _ = self._validate()
        self.assertTrue(any("was removed" in error for error in errors), errors)

    def test_published_history_cannot_be_deleted(self) -> None:
        self._publish([candidate(self.commit, self.digest)])
        self._commit_outputs("integrated candidate")
        self._advance_main()
        self._git("switch", "--quiet", "-c", "character-reconstruction")
        self._publish([])
        self._commit_outputs("delete history")
        errors, _ = self._validate()
        self.assertTrue(any("was removed" in error for error in errors), errors)

    def test_reconstruction_generation_never_writes_discovery_outputs(self) -> None:
        discovery = (self.repository / "characters/registry.jsonl").read_bytes()
        self._publish([candidate(self.commit, self.digest)], render=False)
        self._git("add", "--", RECONSTRUCTION_REGISTRY_PATH)
        subprocess.run(
            [
                sys.executable,
                str(TOOLS / "generate_reconstruction_index.py"),
                "--repo",
                str(self.repository),
                "--snapshot",
                "index",
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual((self.repository / "characters/registry.jsonl").read_bytes(), discovery)
        self.assertFalse((self.repository / "CHARACTER_ANALYSIS_INDEX.md").exists())
        self.assertIn(b"alice-anime-v1", (self.repository / Path(RECONSTRUCTION_INDEX_PATH)).read_bytes())


class IntegrationControlTests(unittest.TestCase):
    def test_registry_change_requires_its_generated_index(self) -> None:
        obligations = json.loads(
            (REPOSITORY / "governance/repository-controls/change-obligations.json").read_text(encoding="utf-8")
        )
        rules = active_rules(obligations, {RECONSTRUCTION_REGISTRY_PATH}, set(), set())
        self.assertEqual([rule["id"] for rule in rules], ["character-reconstruction"])
        self.assertEqual(
            missing_required_output_paths(rules, {RECONSTRUCTION_REGISTRY_PATH}),
            [RECONSTRUCTION_INDEX_PATH],
        )
        discovery_rules = active_rules(
            obligations, {"characters/registry/example.jsonl"}, set(), set()
        )
        self.assertEqual([rule["id"] for rule in discovery_rules], ["character-discovery"])
        self.assertEqual(
            missing_required_output_paths(discovery_rules, {"characters/registry/example.jsonl"}),
            ["CHARACTER_ANALYSIS_INDEX.md"],
        )

    def test_audit_recognizes_reconstruction_branch_without_housekeeping_pending(self) -> None:
        path = ".github/workflows/repository-audit.yml"
        source = (REPOSITORY / path).read_bytes()
        line = b"      - character-reconstruction\n"
        self.assertIn(line, source)
        # The reporter publishes the validator's state for every branch; only stale
        # routing on an analysis branch is pending, so this branch never waits on housekeeping.
        self.assertNotIn(b"ANALYTICAL_SOURCE", source)
        self.assertIn(b"state = integration\n", source)
        changed = source.replace(line, b"", 1)
        snapshot = GitSnapshot(REPOSITORY, "IN_MEMORY", {path: SnapshotEntry(path, "100644", changed)})
        failures = validate_audit_workflow(snapshot, {"allowed_workflows": [path]})
        self.assertIn(
            "repository-audit workflow missing required contract:       - character-reconstruction",
            failures,
        )

    def test_reconstruction_outputs_stay_outside_discovery_and_housekeeping(self) -> None:
        self.assertFalse(any(is_discovery_output(path) for path in RECONSTRUCTION_OUTPUTS))
        housekeeping = (REPOSITORY / ".github/workflows/global-index-housekeeping.yml").read_text(encoding="utf-8")
        for path in RECONSTRUCTION_OUTPUTS:
            self.assertNotIn(path, housekeeping)
            with self.assertRaises(DomainError):
                validate_evidence_path(path)

    def test_live_production_registry_and_index_follow_the_activation_contract(self) -> None:
        snapshot = GitSnapshot.from_index(REPOSITORY)
        phase, policy_errors = load_reconstruction_policy(snapshot)
        self.assertEqual(policy_errors, [])
        rendered = load_and_render(snapshot, REPOSITORY)
        self.assertEqual(snapshot.get(RECONSTRUCTION_INDEX_PATH).data, rendered.encode("utf-8"))  # type: ignore[union-attr]
        registry = decode_reconstruction_registry(
            snapshot.get(RECONSTRUCTION_REGISTRY_PATH).data, RECONSTRUCTION_REGISTRY_PATH  # type: ignore[union-attr]
        )
        statuses = {record["assessment_status"] for _line, record in registry}
        self.assertNotIn("UNASSESSED", statuses)
        if phase != "ROUTINE":
            self.assertNotIn("REVIEWED", statuses)


def run_status(*argv: str) -> tuple[int, dict[str, object] | None, str]:
    stdout, stderr = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        try:
            code = reconstruction_status_main(list(argv))
        except SystemExit as exc:
            code = int(exc.code) if isinstance(exc.code, int) else 2
    text = stdout.getvalue()
    return code, (json.loads(text) if text.strip() else None), stderr.getvalue()


@unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
class ReadinessCertificationTests(ProductionRepositoryFixture):
    """Strict readiness verification fails closed and never certifies nothing."""

    def _currentness(self, *extra: str) -> tuple[int, dict[str, object] | None, str]:
        head = self._git_output("rev-parse", "HEAD")
        return run_status(
            "currentness", "--repo", str(self.repository), "--snapshot", "commit", "--commit", head, *extra
        )

    def _publish_reviewed(self) -> dict[str, object]:
        self._write_policy("ROUTINE")
        self._commit(
            "owner accepts calibration",
            RECONSTRUCTION_POLICY_PATH,
            "governance/reports/RECONSTRUCTION_CALIBRATION_ACCEPTANCE.md",
        )
        published = candidate(self.commit, self.digest)
        self._publish([published])
        self._commit_outputs("candidate")
        reviewed = copy.deepcopy(published)
        reviewed["assessment_status"] = "REVIEWED"
        self._publish([reviewed])
        self._commit_outputs("owner-reviewed promotion")
        self._advance_main()
        return reviewed

    def test_empty_selection_never_certifies_readiness(self) -> None:
        code, output, _ = self._currentness()
        self.assertEqual(code, 0)
        self.assertEqual(output["assessments"], [])  # type: ignore[index]
        self.assertNotIn("current_reviewed_certified", output)  # type: ignore[operator]
        code, output, stderr = self._currentness("--require-current-reviewed")
        self.assertEqual(code, 1)
        self.assertIs(output["current_reviewed_certified"], False)  # type: ignore[index]
        self.assertIn("empty selection never certifies readiness", stderr)

    def test_only_a_current_reviewed_selection_certifies(self) -> None:
        reviewed = self._publish_reviewed()
        selected = ("--assessment", str(reviewed["assessment_id"]), "--require-current-reviewed")
        code, output, _ = self._currentness(*selected)
        self.assertEqual(code, 0)
        self.assertIs(output["current_reviewed_certified"], True)  # type: ignore[index]
        code, _output, _ = self._currentness("--assessment", "missing-id", "--require-current-reviewed")
        self.assertEqual(code, 2)
        self._revise_evidence_on_main()
        code, output, _ = self._currentness(*selected)
        self.assertEqual(code, 1)
        self.assertIs(output["current_reviewed_certified"], False)  # type: ignore[index]

    def test_deferred_work_requires_a_checkpoint(self) -> None:
        head = self._git_output("rev-parse", "HEAD")
        code, _output, stderr = run_status(
            "work-queue", "--repo", str(self.repository), "--commit", head, "--deferred", SUBJECT
        )
        self.assertEqual(code, 2)
        self.assertIn("--deferred requires --since", stderr)

    def test_deferred_subject_returns_after_evidence_bytes_change(self) -> None:
        checkpoint = self._git_output("rev-parse", "HEAD")
        self._revise_evidence_on_main()
        code, output, _ = run_status(
            "work-queue", "--repo", str(self.repository), "--commit", self.main,
            "--since", checkpoint, "--deferred", SUBJECT,
        )
        self.assertEqual(code, 0)
        self.assertEqual(
            [(item["analysis_subject_id"], item["kind"], item["reasons"]) for item in output["items"]],  # type: ignore[index]
            [(SUBJECT, "DEFERRED_EVIDENCE_CHANGED", ["EVIDENCE_BYTES_CHANGED_SINCE_CHECKPOINT"])],
        )


@unittest.skipUnless(importlib.util.find_spec("jsonschema"), "jsonschema is not installed")
class DeferredEvidenceChangeTests(GitRepositoryFixture):
    """Deferred subjects return when evidence changes without a discovery edit."""

    def _changes(self, since: str) -> dict[str, list[str]]:
        before = GitSnapshot.from_commit(self.repository, since)
        now = GitSnapshot.from_commit(self.repository, self._git_output("rev-parse", "HEAD"))
        return deferred_evidence_changes(
            [SUBJECT], [self.record], {SUBJECT: self.record},
            before, AuthorityGraph(before), now, AuthorityGraph(now),
        )

    def _write(self, path: str, data: bytes) -> None:
        target = self.repository / Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    def test_byte_change_without_discovery_edit_is_detected(self) -> None:
        self._write(EVIDENCE_PATH, authority_artifact(b"# Revised analysis\n"))
        self._commit("revise evidence only", EVIDENCE_PATH)
        changes = self._changes(self.commit)
        self.assertEqual(changes, {SUBJECT: ["EVIDENCE_BYTES_CHANGED_SINCE_CHECKPOINT"]})
        queue = work_queue(
            [], [self.record],
            ReconstructionEvaluation(errors=[], basis_entries={}, basis_records={}, currentness={}),
            since_records={SUBJECT: self.record}, deferred=[SUBJECT], deferred_changes=changes,
        )
        self.assertEqual(queue["items"][0]["kind"], "DEFERRED_EVIDENCE_CHANGED")

    def test_authority_change_without_byte_change_is_detected(self) -> None:
        successor = "series/example/ALICE-NEW.md"
        self._write(
            successor,
            (
                "---\nstatus: canonical\n"
                f"supersedes: [{EVIDENCE_PATH}]\n"
                "superseded_by: []\ndo_not_use_as_current_authority: false\n---\n# Successor\n"
            ).encode("utf-8"),
        )
        self._commit("supersede evidence elsewhere", successor)
        self.assertEqual(self._changes(self.commit), {SUBJECT: ["EVIDENCE_AUTHORITY_CHANGED_SINCE_CHECKPOINT"]})

    def test_unrelated_change_does_not_requeue_a_deferred_subject(self) -> None:
        self._write("series/example/UNRELATED.md", authority_artifact(b"# Other\n"))
        self._commit("unrelated analysis", "series/example/UNRELATED.md")
        self.assertEqual(self._changes(self.commit), {})
        queue = work_queue(
            [], [self.record],
            ReconstructionEvaluation(errors=[], basis_entries={}, basis_records={}, currentness={}),
            since_records={SUBJECT: self.record}, deferred=[SUBJECT], deferred_changes={},
        )
        self.assertEqual(queue["items"], [])


class DiscoveryBranchConfinementTests(GitRepositoryFixture):
    """The curation branch carries only discovery outputs."""

    def setUp(self) -> None:
        super().setUp()
        (self.repository / "CHARACTER_ANALYSIS_INDEX.md").write_bytes(b"# Index\n")
        self._commit("discovery index", "CHARACTER_ANALYSIS_INDEX.md")
        self._git("update-ref", "refs/remotes/origin/main", self._git_output("rev-parse", "HEAD"))
        self._git("switch", "--quiet", "-c", "character-registry")

    def _confinement(self) -> list[str]:
        return validate_discovery_branch_confinement(
            self.repository, "commit", self._git_output("rev-parse", "HEAD")
        )

    def _edit_discovery(self) -> None:
        edited = copy.deepcopy(self.record)
        edited["notes"] = "A curation revision."
        self._write_registry([edited])
        (self.repository / "CHARACTER_ANALYSIS_INDEX.md").write_bytes(b"# Index\n\nRevised.\n")

    def test_two_file_curation_delta_passes(self) -> None:
        self._edit_discovery()
        self._commit("curate", "characters/registry.jsonl", "CHARACTER_ANALYSIS_INDEX.md")
        self.assertEqual(self._confinement(), [])

    def test_partitioned_curation_delta_and_the_migration_pass(self) -> None:
        self._migrate_registry()
        self.assertEqual(self._confinement(), [])
        edited = copy.deepcopy(self.record)
        edited["notes"] = "A curation revision."
        (self.repository / "characters/registry/example.jsonl").write_text(
            json.dumps(edited, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        page = self.repository / "characters/index/example.md"
        page.parent.mkdir(parents=True)
        page.write_bytes(b"# Example\n")
        (self.repository / "CHARACTER_ANALYSIS_INDEX.md").write_bytes(b"# Index\n\nRevised.\n")
        self._commit(
            "curate",
            "characters/registry/example.jsonl",
            "characters/index/example.md",
            "CHARACTER_ANALYSIS_INDEX.md",
        )
        self.assertEqual(self._confinement(), [])
        (self.repository / "characters/README.md").write_bytes(b"# Not a discovery output\n")
        self._commit("outside the outputs", "characters/README.md")
        failures = self._confinement()
        self.assertTrue(any("characters/README.md" in item for item in failures), failures)

    def test_any_other_path_on_the_curation_branch_fails(self) -> None:
        self._edit_discovery()
        (self.repository / Path(EVIDENCE_PATH)).write_bytes(authority_artifact(b"# Repaired\n"))
        self._commit("curate and edit analysis", "characters/registry.jsonl", "CHARACTER_ANALYSIS_INDEX.md", EVIDENCE_PATH)
        failures = self._confinement()
        self.assertTrue(any("other changed paths" in item and EVIDENCE_PATH in item for item in failures), failures)

    def test_staged_index_is_checked_before_commit(self) -> None:
        (self.repository / "tools").mkdir()
        (self.repository / "tools" / "helper.py").write_bytes(b"print(1)\n")
        self._git("add", "--", "tools/helper.py")
        failures = validate_discovery_branch_confinement(self.repository, "index", None)
        self.assertTrue(any("tools/helper.py" in item for item in failures), failures)

    def _curation_commit_with_extra_path(self, body: bytes = b"# Repaired\n") -> str:
        self._edit_discovery()
        (self.repository / Path(EVIDENCE_PATH)).write_bytes(authority_artifact(body))
        return self._commit(
            "curate and edit analysis", "characters/registry.jsonl", "CHARACTER_ANALYSIS_INDEX.md", EVIDENCE_PATH
        )

    def _publish_curation_ref(self, commit: str) -> None:
        self._git("update-ref", "refs/remotes/origin/character-registry", commit)

    def test_dispatch_style_audit_confines_unmerged_curation_history(self) -> None:
        head = self._curation_commit_with_extra_path()
        self._publish_curation_ref(head)
        self.assertTrue(discovery_branch_candidate(self.repository, "commit", head))
        failures = discovery_confinement_errors(self.repository, "commit", head, requested=False)
        self.assertTrue(any("other changed paths" in item for item in failures), failures)

    def test_older_unmerged_curation_commit_is_still_confined(self) -> None:
        older = self._curation_commit_with_extra_path()
        (self.repository / "CHARACTER_ANALYSIS_INDEX.md").write_bytes(b"# Index\n\nLater.\n")
        self._publish_curation_ref(self._commit("later curation", "CHARACTER_ANALYSIS_INDEX.md"))
        failures = discovery_confinement_errors(self.repository, "commit", older, requested=False)
        self.assertTrue(any("other changed paths" in item for item in failures), failures)

    def test_curation_history_already_on_main_is_not_confined(self) -> None:
        head = self._curation_commit_with_extra_path()
        self._publish_curation_ref(head)
        self._git("update-ref", "refs/remotes/origin/main", head)
        self.assertFalse(discovery_branch_candidate(self.repository, "commit", head))
        self.assertEqual(discovery_confinement_errors(self.repository, "commit", head, requested=False), [])

    def test_other_branches_and_a_missing_curation_ref_are_not_confined(self) -> None:
        head = self._curation_commit_with_extra_path()
        self.assertFalse(discovery_branch_candidate(self.repository, "commit", head))
        self.assertEqual(discovery_confinement_errors(self.repository, "commit", head, requested=False), [])
        self._git("switch", "--quiet", "-c", "series/example", "refs/remotes/origin/main")
        (self.repository / Path(EVIDENCE_PATH)).write_bytes(authority_artifact(b"# Series work\n"))
        series_head = self._commit("series analysis", EVIDENCE_PATH)
        self._publish_curation_ref(head)
        self.assertFalse(discovery_branch_candidate(self.repository, "commit", series_head))
        self.assertTrue(discovery_confinement_errors(self.repository, "commit", series_head, requested=True))

    def test_audit_fetches_live_curation_ref_and_fails_closed(self) -> None:
        path = ".github/workflows/repository-audit.yml"
        source = (REPOSITORY / path).read_bytes()
        for fragment in (
            b"if git ls-remote --exit-code --heads origin character-registry > /dev/null; then",
            b"git fetch --no-tags origin refs/heads/character-registry:refs/remotes/origin/character-registry",
            b'test "${status}" -eq 2',
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, source)
                changed = source.replace(fragment, b"", 1)
                snapshot = GitSnapshot(REPOSITORY, "IN_MEMORY", {path: SnapshotEntry(path, "100644", changed)})
                failures = validate_audit_workflow(snapshot, {"allowed_workflows": [path]})
                self.assertIn("repository-audit workflow missing required contract: " + fragment.decode(), failures)

    def test_audit_applies_confinement_only_to_the_curation_branch(self) -> None:
        path = ".github/workflows/repository-audit.yml"
        source = (REPOSITORY / path).read_bytes()
        guard = b'if [[ "${AUDIT_BRANCH}" = "character-registry" && "${AUDIT_EVENT}" != "repository_dispatch" ]]; then'
        self.assertIn(guard, source)
        for fragment in (guard, b"audit_args+=(--discovery-branch-confinement)"):
            with self.subTest(fragment=fragment):
                changed = source.replace(fragment, b"", 1)
                snapshot = GitSnapshot(REPOSITORY, "IN_MEMORY", {path: SnapshotEntry(path, "100644", changed)})
                failures = validate_audit_workflow(snapshot, {"allowed_workflows": [path]})
                self.assertIn(
                    "repository-audit workflow missing required contract: " + fragment.decode(), failures
                )
        # An analysis branch may still carry a coordinated curation repair.
        self._edit_discovery()
        head = self._commit("coordinated repair", "characters/registry.jsonl", "CHARACTER_ANALYSIS_INDEX.md")
        self.assertEqual(validate_routing_branch_scope(self.repository, "commit", head, "series/example"), [])


if __name__ == "__main__":
    unittest.main()
