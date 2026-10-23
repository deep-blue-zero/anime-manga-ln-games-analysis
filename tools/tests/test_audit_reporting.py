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
    def report(self, result: str, state: str, *, sha: str = "a" * 40) -> tuple[object, dict]:
        script = workflow(AUDIT)["jobs"]["report"]["steps"][0]["run"]
        program = script.split("python - <<'PY'\n", 1)[1].rsplit("\nPY", 1)[0]
        environment = {
            "AUDIT_COMMIT": sha, "GITHUB_SHA": "b" * 40,
            "GITHUB_REPOSITORY": "deep-blue-zero/anime-manga-ln-games-analysis",
            "GITHUB_RUN_ID": "123", "AUDIT_RESULT": result,
            "INTEGRATION_STATE": state, "GH_TOKEN": "test-token",
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

    def test_reporter_publishes_the_validated_routing_state_directly(self) -> None:
        _, current = self.report("success", "success")
        self.assertEqual(current["state"], "success")
        _, stale = self.report("success", "pending")
        self.assertEqual(stale["state"], "pending")
        self.assertIn("housekeeping", stale["description"])
        _, failed = self.report("failure", "success")
        self.assertEqual(failed["state"], "failure")

    def test_invalid_target_is_rejected_before_a_status_write(self) -> None:
        with self.assertRaisesRegex(SystemExit, "invalid audited commit"):
            self.report("success", "success", sha="main")

    def test_reporter_and_validation_permission_boundaries_are_enforced(self) -> None:
        original = (ROOT / AUDIT).read_text(encoding="utf-8")
        entries = {
            path: SnapshotEntry(path, "100644", (ROOT / path).read_bytes())
            for path in (AUDIT,)
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
            # The reporter must target the audited commit, not the dispatch run's default head.
            original.replace(
                "          AUDIT_COMMIT: ${{ github.event_name == 'repository_dispatch' && github.event.client_payload.commit_sha || github.sha }}\n          AUDIT_RESULT",
                "          AUDIT_COMMIT: ${{ github.sha }}\n          AUDIT_RESULT", 1),
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
            "tests": [{"id": f"test_{i}_" + "fixture" * 40, "seconds": 0.1} for i in range(300)],
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
            self.assertIn("Archive validation: no completed report", summary.read_text())

    def run_generation(self, *, routing_changed: bool, contains_main: bool) -> tuple[subprocess.CompletedProcess, list, Path]:
        if not shutil.which("bash"):
            self.skipTest("bash is unavailable")
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value or not Path(base_value).is_dir():
            self.skipTest("MANGA_ANIME_TEST_TMP is not available")
        step = workflow(HOUSEKEEPING)["jobs"]["synchronize"]["steps"][-1]
        directory = tempfile.TemporaryDirectory(dir=base_value)
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        binaries = root / "bin"
        binaries.mkdir()
        programs = {
            "git": (
                "import json, os, sys\n"
                "args = sys.argv[1:]\n"
                "with open(os.environ['TEST_GIT_CALLS'], 'a') as output:\n"
                "    output.write(json.dumps(args) + '\\n')\n"
                "if args[0] == 'diff' and '--quiet' in args:\n"
                "    sys.exit(int(os.environ['TEST_DIFF_CODE']))\n"
                "if args[0] == 'merge-base':\n"
                "    sys.exit(int(os.environ['TEST_ANCESTOR_CODE']))\n"
                "if args[0] == 'rev-parse':\n"
                "    print('b' * 40)\n"
            ),
            "python": (
                "import json, os, subprocess, sys\n"
                "from pathlib import Path\n"
                "with open(os.environ['TEST_GIT_CALLS'], 'a') as output:\n"
                "    output.write(json.dumps(['python', sys.argv[1]]) + '\\n')\n"
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
        calls = root / "calls"
        marker = root / "dispatched"
        environment = dict(
            os.environ, PATH=str(binaries) + os.pathsep + os.environ["PATH"],
            SOURCE_SHA="a" * 40, BRANCH_NAME="series/example", GH_TOKEN="test-token",
            GITHUB_REPOSITORY="deep-blue-zero/anime-manga-ln-games-analysis",
            TEST_DIFF_CODE="1" if routing_changed else "0",
            TEST_ANCESTOR_CODE="0" if contains_main else "1",
            TEST_GIT_CALLS=str(calls), TEST_DISPATCHED=str(marker),
        )
        result = subprocess.run(
            ["bash", "-e", "-o", "pipefail"], input=with_stubs(step["run"], binaries, ("git", "python", "curl")), cwd=root,
            env=environment, text=True, capture_output=True, check=False,
        )
        commands = [json.loads(line) for line in calls.read_text().splitlines()] if calls.exists() else []
        return result, commands, marker

    def test_current_routing_exits_without_dispatch_or_write(self) -> None:
        result, commands, marker = self.run_generation(routing_changed=False, contains_main=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("routing outputs are current", result.stdout)
        self.assertFalse(marker.exists())
        self.assertFalse(any(args[0] in {"commit", "push", "ls-remote", "merge-base"} for args in commands))
        self.assertNotIn(["python", "tools/prepare_commit.py"], commands)

    def test_stale_routing_requires_current_main_before_any_write(self) -> None:
        result, commands, marker = self.run_generation(routing_changed=True, contains_main=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("incorporate current main", result.stderr)
        self.assertFalse(marker.exists())
        self.assertFalse(any(args[0] in {"commit", "push"} for args in commands))
        self.assertNotIn(["python", "tools/prepare_commit.py"], commands)

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
