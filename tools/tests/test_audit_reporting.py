from __future__ import annotations

import contextlib
import io
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))
from character_index_core import GitSnapshot, SnapshotEntry, _restricted_yaml_load
from validate_repository import validate_audit_workflow

AUDIT = ".github/workflows/repository-audit.yml"
HOUSEKEEPING = ".github/workflows/global-index-housekeeping.yml"


def with_stubs(script: str, directory: Path, names: tuple[str, ...]) -> str:
    path = directory.as_posix()
    if os.name == "nt":
        path = "/" + directory.drive[0].lower() + path[2:]
    # Git Bash can prepend its own directories to the inherited Windows PATH.
    # Set the fixture boundary inside the shell and verify it before execution.
    prefix = "export PATH=" + shlex.quote(path) + ':"$PATH"\nhash -r\n'
    for name in names:
        prefix += 'test "$(command -v ' + name + ')" = ' + shlex.quote(path + "/" + name) + " || exit 99\n"
    return prefix + script


def workflow(path: str) -> dict:
    text = (ROOT / path).read_text(encoding="utf-8")
    return _restricted_yaml_load(text.replace("\non:", '\n"on":'), path)


class AuditReportingTests(unittest.TestCase):
    def report(self, result: str, state: str, *, sha: str = "a" * 40, source: bool = False) -> tuple[object, dict]:
        script = workflow(AUDIT)["jobs"]["report"]["steps"][0]["run"]
        program = script.split("python - <<'PY'\n", 1)[1].rsplit("\nPY", 1)[0]
        environment = {
            "AUDIT_COMMIT": sha, "GITHUB_SHA": "b" * 40,
            "GITHUB_REPOSITORY": "deep-blue-zero/anime-manga-ln-games-analysis",
            "GITHUB_RUN_ID": "123", "AUDIT_RESULT": result,
            "INTEGRATION_STATE": state, "GH_TOKEN": "test-token",
            "ANALYTICAL_SOURCE": "true" if source else "false",
        }
        with mock.patch.dict(os.environ, environment, clear=True):
            with mock.patch("urllib.request.urlopen") as urlopen:
                urlopen.return_value.__enter__.return_value.status = 201
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(compile(program, "isolated-status-reporter", "exec"), {})
                request = urlopen.call_args.args[0]
        return request, json.loads(request.data)

    def test_report_is_bound_to_audited_sha_not_dispatch_default_head(self) -> None:
        request, payload = self.report("success", "success")
        self.assertTrue(request.full_url.endswith("/statuses/" + "a" * 40))
        self.assertEqual(payload["context"], "Repository integration audit")
        self.assertEqual(payload["state"], "success")
        self.assertTrue(payload["target_url"].endswith("/actions/runs/123"))

    def test_preflight_pending_and_unsuccessful_runs_never_report_success(self) -> None:
        for result, state, expected in (
            ("success", "pending", "pending"),
            ("failure", "success", "failure"),
            ("success", "", "failure"),
            ("success", "unknown", "failure"),
            ("cancelled", "success", "error"),
            ("skipped", "", "error"),
        ):
            with self.subTest(result=result, state=state):
                _, payload = self.report(result, state)
                self.assertEqual(payload["state"], expected)

    def test_stable_source_is_pending_even_when_routing_is_current(self) -> None:
        for state in ("success", "pending"):
            _, payload = self.report("success", state, source=True)
            self.assertEqual(payload["state"], "pending")
            self.assertIn("housekeeping", payload["description"])
        _, failed = self.report("failure", "success", source=True)
        self.assertEqual(failed["state"], "failure")

    def test_invalid_target_is_rejected_before_a_status_write(self) -> None:
        with self.assertRaisesRegex(SystemExit, "invalid audited commit"):
            self.report("success", "success", sha="main")

    def test_reporter_and_validation_permission_boundaries_are_enforced(self) -> None:
        original = (ROOT / AUDIT).read_text(encoding="utf-8")
        entries = {
            path: SnapshotEntry(path, "100644", (ROOT / path).read_bytes())
            for path in (AUDIT, "governance/repository-controls/test-execution-policy.json", "tools/tests/test-catalog.json")
        }
        policy = {"allowed_workflows": [AUDIT, HOUSEKEEPING, ".github/workflows/nightly-integration.yml"]}
        self.assertEqual(validate_audit_workflow(GitSnapshot(ROOT, "TEST", entries), policy), [])
        variants = (
            original.replace("permissions:\n  contents: read", "permissions:\n  contents: read\n  statuses: write", 1),
            original.replace("      statuses: write", "      statuses: write\n      contents: write", 1),
            original.replace("/statuses/{sha}", "/statuses/{os.environ['GITHUB_SHA']}", 1),
            original.replace("    needs: audit", "    needs: unrelated", 1),
            original.replace("    runs-on: ubuntu-24.04", "    uses: owner/repo/workflow@ref", 1),
            original.replace("        shell: bash", "        uses: owner/action@ref\n        shell: bash", 1),
        )
        for changed in variants:
            with self.subTest(changed=changed[-100:]):
                snap = GitSnapshot(ROOT, "TEST", {**entries, AUDIT: SnapshotEntry(AUDIT, "100644", changed.encode())})
                failures = validate_audit_workflow(snap, policy)
                self.assertTrue(failures)

    def test_all_workflow_shell_steps_parse(self) -> None:
        if not shutil.which("bash"):
            self.skipTest("bash is unavailable")
        for path in (AUDIT, HOUSEKEEPING, ".github/workflows/nightly-integration.yml"):
            for job in workflow(path)["jobs"].values():
                for step in job.get("steps", []):
                    if step.get("shell") == "bash":
                        with self.subTest(path=path, step=step["name"]):
                            result = subprocess.run(
                                ["bash", "-n"], input=step["run"],
                                text=True, capture_output=True, check=False,
                            )
                            self.assertEqual(result.returncode, 0, result.stderr)

    def test_execution_summary_preserves_large_reports_in_bounded_log_lines(self) -> None:
        script = workflow(AUDIT)["jobs"]["audit"]["steps"][-1]["run"]
        program = script.split("python - <<'PY'\n", 1)[1].rsplit("\nPY", 1)[0]
        report = {
            "outcome": "success", "seconds": 1.5, "tests_run": 300, "skipped": 0,
            "shadow_plan": {
                "proposed_profile": "full", "excluded_ids": [],
                "selected_ids": [f"test_{i}_" + "fixture" * 40 for i in range(300)],
            },
        }
        self.assertGreater(len(json.dumps(report)), 65536)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            summary = root / "summary.md"
            (root / "test-timings.json").write_text(json.dumps(report), encoding="utf-8")
            output = io.StringIO()
            with mock.patch.dict(os.environ, {"RUNNER_TEMP": str(root), "GITHUB_STEP_SUMMARY": str(summary)}, clear=True), contextlib.redirect_stdout(output):
                exec(compile(program, "execution-summary", "exec"), {})
            emitted = output.getvalue()
            payload = emitted.split("AUDIT_EXECUTION_REPORT_BEGIN: test-timings.json\n", 1)[1].split("\nAUDIT_EXECUTION_REPORT_END:", 1)[0]
            self.assertEqual(json.loads(payload), report)
            self.assertLess(max(map(len, emitted.splitlines())), 1024)
            self.assertIn("Tests executed: 300; skipped: 0", summary.read_text())
            self.assertIn("Actual execution remained full", summary.read_text())
            self.assertIn("Archive validation: no completed report", summary.read_text())

    def test_unchanged_housekeeping_dispatches_only_after_current_head_checks(self) -> None:
        if not shutil.which("bash"):
            self.skipTest("bash is unavailable")
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value or not Path(base_value).is_dir():
            self.skipTest("MANGA_ANIME_TEST_TMP is not available")
        step = workflow(HOUSEKEEPING)["jobs"]["synchronize"]["steps"][-1]
        for branch_sha, main_sha, dispatched in (
            ("a" * 40, "b" * 40, True),
            ("c" * 40, "b" * 40, False),
            ("a" * 40, "c" * 40, False),
        ):
            with self.subTest(branch=branch_sha, main=main_sha):
                with tempfile.TemporaryDirectory(dir=base_value) as directory:
                    root = Path(directory)
                    binaries = root / "bin"
                    binaries.mkdir()
                    programs = {
                        "git": (
                            "import json, os, sys\n"
                            "from pathlib import Path\n"
                            "args = sys.argv[1:]\n"
                            "with open(os.environ['TEST_GIT_CALLS'], 'a') as output:\n"
                            "    output.write(json.dumps(args) + '\\n')\n"
                            "if args[0] == 'ls-remote':\n"
                            "    key = 'TEST_MAIN_SHA' if args[-1] == 'refs/heads/main' else 'TEST_BRANCH_SHA'\n"
                            "    print(os.environ[key] + '\\t' + args[-1])\n"
                            "elif args[0] == 'rev-parse':\n"
                            "    print('b' * 40)\n"
                        ),
                        "python": (
                            "import subprocess, sys\n"
                            "from pathlib import Path\n"
                            "if not sys.argv[1].startswith('tools/'):\n"
                            "    assert sys.argv[1] == '-'\n"
                            "    original = subprocess.check_output\n"
                            "    git_stub = str(Path(__file__).with_name('git.py'))\n"
                            "    def check_output(args, **kwargs):\n"
                            "        assert args[0] == 'git', args\n"
                            "        return original([sys.executable, git_stub, *args[1:]], **kwargs)\n"
                            "    subprocess.check_output = check_output\n"
                            "    sys.argv = sys.argv[1:]\n"
                            "    exec(compile(sys.stdin.read(), '<workflow-stdin>', 'exec'), {'__name__': '__main__'})\n"
                        ),
                        "curl": (
                            "import os\n"
                            "from pathlib import Path\n"
                            "Path(os.environ['TEST_DISPATCHED']).write_text('called')\n"
                        ),
                    }
                    for name, program in programs.items():
                        target = binaries / name
                        program_path = binaries / (name + ".py")
                        program_path.write_text(program, encoding="utf-8", newline="\n")
                        target.write_text(
                            "#!/bin/sh\nexec " + shlex.quote(Path(sys.executable).as_posix())
                            + " " + shlex.quote(program_path.as_posix()) + ' "$@"\n',
                            encoding="utf-8", newline="\n",
                        )
                        target.chmod(0o700)
                    calls = root / "git-calls"
                    marker = root / "dispatched"
                    environment = dict(
                        os.environ, PATH=str(binaries) + os.pathsep + os.environ["PATH"],
                        SOURCE_SHA="a" * 40, BRANCH_NAME="series/example",
                        SOURCE_AUDIT_CONCLUSION="success", GH_TOKEN="test-token",
                        GITHUB_REPOSITORY="deep-blue-zero/anime-manga-ln-games-analysis",
                        TEST_BRANCH_SHA=branch_sha, TEST_MAIN_SHA=main_sha,
                        TEST_GIT_CALLS=str(calls), TEST_DISPATCHED=str(marker),
                    )
                    result = subprocess.run(
                        ["bash", "-e", "-o", "pipefail"], input=with_stubs(step["run"], binaries, ("git", "python", "curl")), cwd=root,
                        env=environment, text=True, capture_output=True, check=False,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertEqual(marker.exists(), dispatched)
                    commands = [json.loads(line) for line in calls.read_text().splitlines()]
                    self.assertFalse(any(args[0] in {"commit", "push"} for args in commands))
                    if dispatched:
                        payload = json.loads((root / "dispatch.json").read_text())
                        self.assertEqual(payload["client_payload"], {
                            "commit_sha": "a" * 40, "branch": "series/example",
                        })
                    else:
                        self.assertFalse((root / "dispatch.json").exists())

    def test_superseded_housekeeping_exits_before_generation(self) -> None:
        if not shutil.which("bash"):
            self.skipTest("bash is unavailable")
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value or not Path(base_value).is_dir():
            self.skipTest("MANGA_ANIME_TEST_TMP is not available")
        job = workflow(HOUSEKEEPING)["jobs"]["synchronize"]
        acquire = next(step for step in job["steps"] if step.get("id") == "acquire")
        for step in job["steps"][1:]:
            self.assertEqual(step.get("if"), "steps.acquire.outputs.ready == 'true'")
        with tempfile.TemporaryDirectory(dir=base_value) as directory:
            root = Path(directory)
            stub = root / "git"
            stub.write_text(
                "#!/bin/sh\n"
                'if [ "$1" = "rev-parse" ]; then printf "%s\\n" "' + "b" * 40 + '"; fi\n',
                encoding="utf-8",
                newline="\n",
            )
            stub.chmod(0o700)
            output = root / "outputs"
            environment = dict(os.environ, PATH=str(root) + os.pathsep + os.environ["PATH"],
                               BRANCH_NAME="series/example", SOURCE_SHA="a" * 40,
                               GITHUB_REPOSITORY="deep-blue-zero/anime-manga-ln-games-analysis",
                               GITHUB_OUTPUT=str(output))
            result = subprocess.run(
                ["bash", "-e", "-o", "pipefail"], input=with_stubs(acquire["run"], root, ("git",)), cwd=root,
                env=environment, text=True, capture_output=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Superseded housekeeping run", result.stdout)
            self.assertEqual(output.read_text(), "ready=false\n")


if __name__ == "__main__":
    unittest.main()
