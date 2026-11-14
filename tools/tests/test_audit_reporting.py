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


def install_stubs(binaries: Path, programs: dict[str, str]) -> None:
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


CURL_STUB = (
    "import os\n"
    "from pathlib import Path\n"
    "Path(os.environ['TEST_DISPATCHED']).write_text('called')\n"
)
ROUTING_OUTPUTS = (
    "governance/MANGA_ANIME_CORPUS_INDEX.md", "series/README.md", "series/registry.json",
    "studies/README.md", "studies/registry.json",
)


def workflow(path: str) -> dict:
    text = (ROOT / path).read_text(encoding="utf-8")
    return _restricted_yaml_load(text.replace("\non:", '\n"on":'), path)


class AuditReportingTests(unittest.TestCase):
    def report(
        self, result: str, state: str, *, sha: str = "a" * 40, counts: dict[str, int | str] | None = None,
    ) -> tuple[object, dict]:
        script = workflow(AUDIT)["jobs"]["report"]["steps"][0]["run"]
        program = script.split("python - <<'PY'\n", 1)[1].rsplit("\nPY", 1)[0]
        environment = {
            "AUDIT_COMMIT": sha, "GITHUB_SHA": "b" * 40,
            "GITHUB_REPOSITORY": "deep-blue-zero/anime-manga-ln-games-analysis",
            "GITHUB_RUN_ID": "123", "AUDIT_RESULT": result,
            "INTEGRATION_STATE": state, "GH_TOKEN": "test-token",
        }
        if counts is not None:
            environment.update({f"AUDIT_{key.upper()}": str(value) for key, value in counts.items()})
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

    def test_reporter_publishes_test_counts_in_the_status_description(self) -> None:
        counts = {"tests_run": 486, "failures": 0, "errors": 0, "skipped": 0}
        _, current = self.report("success", "success", counts=counts)
        self.assertEqual(
            current["description"],
            "Exact commit passed the repository audit: 486 tests, 0 failed, 0 errors, 0 skipped",
        )
        _, pending = self.report("success", "pending", counts=counts)
        self.assertIn("486 tests, 0 failed, 0 errors, 0 skipped", pending["description"])
        self.assertIn("housekeeping", pending["description"])
        self.assertLessEqual(len(pending["description"]), 140)
        _, failed = self.report("failure", "success", counts=counts)
        self.assertEqual(failed["state"], "failure")

        for unavailable in (None, {"tests_run": 486}, dict(counts, skipped="bad"), dict(counts, tests_run="9" * 141)):
            with self.subTest(counts=unavailable):
                _, payload = self.report("success", "success", counts=unavailable)
                self.assertTrue(payload["description"].endswith("test counts unavailable"))

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

    def test_execution_summary_keeps_full_reports_out_of_the_job_log(self) -> None:
        script = workflow(AUDIT)["jobs"]["audit"]["steps"][-1]["run"]
        program = script.split("python - <<'PY'\n", 1)[1].rsplit("\nPY", 1)[0]
        report = {
            "outcome": "success", "seconds": 1.5, "tests_run": 300, "skipped": 0,
            "errors": "malformed count " * 300,
            "tests": [{"id": f"test_{i}_" + "fixture" * 40, "seconds": 0.1} for i in range(300)],
        }
        self.assertGreater(len(json.dumps(report)), 65536)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            summary = root / "summary.md"
            outputs = root / "outputs"
            (root / "test-timings.json").write_text(json.dumps(report), encoding="utf-8")
            output = io.StringIO()
            environment = {"RUNNER_TEMP": str(root), "GITHUB_STEP_SUMMARY": str(summary), "GITHUB_OUTPUT": str(outputs)}
            with mock.patch.dict(os.environ, environment, clear=True), contextlib.redirect_stdout(output):
                exec(compile(program, "execution-summary", "exec"), {})
            emitted = output.getvalue()
            self.assertNotIn("AUDIT_EXECUTION_REPORT_BEGIN", emitted)
            prefix = "AUDIT_EXECUTION_SUMMARY: test-timings.json "
            payload = next(line.removeprefix(prefix) for line in emitted.splitlines() if line.startswith(prefix))
            self.assertEqual(json.loads(payload), {"outcome": "success", "seconds": 1.5, "tests_run": 300, "skipped": 0})
            self.assertLessEqual(max(map(len, emitted.splitlines())), 300)
            markdown = summary.read_text(encoding="utf-8")
            self.assertIn("Tests executed: 300; skipped: 0", markdown)
            self.assertIn("Archive validation: no completed report", markdown)
            self.assertIn(json.dumps(report, sort_keys=True, indent=2), markdown)
            self.assertEqual(set(outputs.read_text(encoding="utf-8").splitlines()), {"tests_run=300", "skipped=0"})

    def run_generation(
        self, *, routing_changed: bool, main_changed_routing: bool, merge_base: str = "c" * 40,
    ) -> tuple[subprocess.CompletedProcess, list, Path]:
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
                "    staged = '--cached' in args\n"
                "    sys.exit(int(os.environ['TEST_DIFF_CODE' if staged else 'TEST_MAIN_ROUTING_CODE']))\n"
                "if args[0] == 'merge-base' and os.environ['TEST_MERGE_BASE']:\n"
                "    print(os.environ['TEST_MERGE_BASE'])\n"
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
            "curl": CURL_STUB,
        }
        install_stubs(binaries, programs)
        calls = root / "calls"
        marker = root / "dispatched"
        environment = dict(
            os.environ, PATH=str(binaries) + os.pathsep + os.environ["PATH"],
            SOURCE_SHA="a" * 40, BRANCH_NAME="series/example", GH_TOKEN="test-token",
            GITHUB_REPOSITORY="deep-blue-zero/anime-manga-ln-games-analysis",
            TEST_DIFF_CODE="1" if routing_changed else "0",
            TEST_MAIN_ROUTING_CODE="1" if main_changed_routing else "0",
            TEST_MERGE_BASE=merge_base,
            TEST_GIT_CALLS=str(calls), TEST_DISPATCHED=str(marker),
        )
        result = subprocess.run(
            ["bash", "-e", "-o", "pipefail"], input=with_stubs(step["run"], binaries, ("git", "python", "curl")), cwd=root,
            env=environment, text=True, capture_output=True, check=False,
        )
        commands = [json.loads(line) for line in calls.read_text().splitlines()] if calls.exists() else []
        return result, commands, marker

    def test_current_routing_exits_without_dispatch_or_write(self) -> None:
        result, commands, marker = self.run_generation(routing_changed=False, main_changed_routing=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("routing outputs are current", result.stdout)
        self.assertFalse(marker.exists())
        self.assertFalse(any(args[0] in {"commit", "push", "ls-remote", "merge-base"} for args in commands))
        self.assertNotIn(["python", "tools/prepare_commit.py"], commands)

    def test_stale_routing_requires_current_main_before_any_write(self) -> None:
        # Main changed routing since the merge base, or no merge base can be read.
        for main_changed_routing, merge_base in ((True, "c" * 40), (False, "")):
            with self.subTest(main_changed_routing=main_changed_routing, merge_base=merge_base):
                result, commands, marker = self.run_generation(
                    routing_changed=True, main_changed_routing=main_changed_routing, merge_base=merge_base,
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("incorporate current main", result.stderr)
                self.assertFalse(marker.exists())
                self.assertIn(["merge-base", "--all", "origin/main", "HEAD"], commands)
                self.assertFalse(any(args[0] in {"commit", "push"} for args in commands))
                self.assertNotIn(["python", "tools/prepare_commit.py"], commands)

    def run_publication(self, *, main_changes: str | None, during_gate: bool) -> dict:
        """Run the publication step with real Git against a local origin.

        `main_changes` is the path a new commit on main changes, either before
        housekeeping starts or while its pre-commit gate runs.
        """
        if not shutil.which("bash"):
            self.skipTest("bash is unavailable")
        base_value = os.environ.get("MANGA_ANIME_TEST_TMP")
        if not base_value or not Path(base_value).is_dir():
            self.skipTest("MANGA_ANIME_TEST_TMP is not available")
        step = workflow(HOUSEKEEPING)["jobs"]["synchronize"]["steps"][-1]
        directory = tempfile.TemporaryDirectory(dir=base_value, ignore_cleanup_errors=True)
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        origin, seed, work, binaries = (root / name for name in ("origin.git", "seed", "work", "bin"))

        def git(repository: Path, *args: str) -> str:
            identity = ("-c", "user.name=Housekeeping Test", "-c", "user.email=housekeeping-test@example.invalid")
            return subprocess.check_output(
                ["git", "-C", str(repository), "-c", "core.autocrlf=false", *identity, *args],
                stderr=subprocess.PIPE, text=True,
            ).strip()

        def commit(path: str, content: str, message: str) -> str:
            target = seed / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8", newline="\n")
            git(seed, "add", "--", path)
            git(seed, "commit", "--quiet", "-m", message)
            return git(seed, "rev-parse", "HEAD")

        for repository in (origin, seed, work, binaries):
            repository.mkdir()
        git(origin, "init", "--quiet", "--bare")
        git(seed, "init", "--quiet")
        git(seed, "symbolic-ref", "HEAD", "refs/heads/main")
        git(seed, "remote", "add", "origin", origin.as_posix())
        for path in ROUTING_OUTPUTS:
            (seed / path).parent.mkdir(parents=True, exist_ok=True)
            (seed / path).write_text("routing\n", encoding="utf-8", newline="\n")
            git(seed, "add", "--", path)
        commit("notes.md", "notes\n", "main: base")
        git(seed, "checkout", "--quiet", "-b", "series/example")
        source = commit("series/example/.repository/series-registry.json", "{}\n", "branch: routing descriptor")
        git(seed, "checkout", "--quiet", "main")
        git(seed, "push", "--quiet", "origin", "main", "series/example")
        later_main = ""
        if main_changes is not None:
            later_main = commit(main_changes, "changed on main\n", "main: later change")
            # Either main already moved, or the commit waits in origin for the gate stub to publish it.
            git(seed, "push", "--quiet", "origin", "main:refs/heads/" + ("staged" if during_gate else "main"))

        git(work, "init", "--quiet")
        git(work, "config", "core.autocrlf", "false")
        git(work, "remote", "add", "origin", origin.as_posix())
        git(work, "fetch", "--quiet", "--no-tags", "origin",
            "+refs/heads/main:refs/remotes/origin/main",
            "+refs/heads/series/example:refs/remotes/origin/series/example")
        git(work, "checkout", "--quiet", "--detach", source)
        install_stubs(binaries, {
            "python": (
                "import os, subprocess, sys\n"
                "script = sys.argv[1]\n"
                "if script == 'tools/synchronize_global_registries.py':\n"
                "    with open('series/registry.json', 'ab') as output:\n"
                "        output.write(b'regenerated\\n')\n"
                "elif script == 'tools/prepare_commit.py' and os.environ['TEST_ADVANCE_MAIN']:\n"
                "    subprocess.check_call(['git', '-C', os.environ['TEST_ORIGIN'], 'update-ref',\n"
                "                           'refs/heads/main', os.environ['TEST_ADVANCE_MAIN']])\n"
                "elif script == '-':\n"
                "    sys.argv = sys.argv[1:]\n"
                "    exec(compile(sys.stdin.read(), '<workflow-stdin>', 'exec'), {'__name__': '__main__'})\n"
            ),
            "curl": CURL_STUB,
        })
        marker = root / "dispatched"
        environment = dict(
            os.environ, PATH=str(binaries) + os.pathsep + os.environ["PATH"],
            SOURCE_SHA=source, BRANCH_NAME="series/example", GH_TOKEN="test-token",
            GITHUB_REPOSITORY="deep-blue-zero/anime-manga-ln-games-analysis",
            TEST_ORIGIN=str(origin), TEST_ADVANCE_MAIN=later_main if during_gate else "",
            TEST_DISPATCHED=str(marker),
        )
        result = subprocess.run(
            ["bash", "-e", "-o", "pipefail"], input=with_stubs(step["run"], binaries, ("python", "curl")), cwd=work,
            env=environment, text=True, capture_output=True, check=False,
        )
        head = git(origin, "rev-parse", "refs/heads/series/example")
        published = head != source
        if published:
            self.assertEqual(git(origin, "rev-parse", head + "^"), source)
            self.assertEqual(git(origin, "diff", "--name-only", source, head), "series/registry.json")
            self.assertEqual(git(origin, "log", "-1", "--format=%an <%ae> / %cn <%ce>", head),
                             "deep-blue-zero <50891441+peipw@users.noreply.github.com> / GitHub <noreply@github.com>")
            if main_changes is not None:
                # Merging the commits the branch lacked keeps the regenerated outputs byte for byte.
                git(seed, "fetch", "--quiet", "origin", head)
                git(seed, "checkout", "--quiet", "--detach", head)
                git(seed, "merge", "--quiet", "--no-edit", later_main)
                self.assertEqual(git(seed, "diff", "--name-only", head, "HEAD", "--", *ROUTING_OUTPUTS), "")
        return {"result": result, "published": published, "dispatched": marker.exists()}

    def test_housekeeping_publishes_when_missing_main_commits_leave_routing_unchanged(self) -> None:
        for main_changes, during_gate in ((None, False), ("notes.md", False), ("notes.md", True)):
            with self.subTest(main_changes=main_changes, during_gate=during_gate):
                outcome = self.run_publication(main_changes=main_changes, during_gate=during_gate)
                result = outcome["result"]
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertTrue(outcome["published"], result.stdout + result.stderr)
                self.assertTrue(outcome["dispatched"])
                self.assertIn("PASS: dispatched the full audit for", result.stdout)

    def test_housekeeping_refuses_when_missing_main_commits_changed_routing(self) -> None:
        for path in ("series/registry.json", "governance/MANGA_ANIME_CORPUS_INDEX.md"):
            for during_gate, message in (
                (False, "FAIL: main changed routing outputs; incorporate current main"),
                (True, "FAIL: main changed routing outputs during housekeeping; incorporate current main"),
            ):
                with self.subTest(path=path, during_gate=during_gate):
                    outcome = self.run_publication(main_changes=path, during_gate=during_gate)
                    result = outcome["result"]
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    self.assertIn(message, result.stderr)
                    self.assertFalse(outcome["published"] or outcome["dispatched"])

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
