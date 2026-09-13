"""Small, local-only audit telemetry; never a source of certification."""
from __future__ import annotations

import json
import os
import platform
import sys
import time
from collections import Counter
from importlib import metadata
from pathlib import Path
from typing import Callable, Any


def git_metrics() -> dict:
    total = Counter()
    seen = set()
    # unittest can load the core both as a script module and as tools.core.
    for name in ("character_index_core", "tools.character_index_core"):
        counters = getattr(sys.modules.get(name), "GIT_METRICS", None)
        if counters is not None and id(counters) not in seen:
            total.update(counters)
            seen.add(id(counters))
    return dict(total)


def runtime_metadata() -> dict:
    versions = {}
    for package in ("attrs", "jsonschema", "jsonschema-specifications", "PyYAML", "referencing", "rpds-py", "typing-extensions"):
        try:
            versions[package] = metadata.version(package)
        except metadata.PackageNotFoundError:
            versions[package] = None
    return {
        "python": platform.python_version(), "platform": sys.platform,
        "dependencies": versions,
        "runner_image": os.environ.get("ImageOS"),
        "runner_image_version": os.environ.get("ImageVersion"),
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
    }


def report_path(root: Path, path: Path) -> Path:
    resolved = path.resolve()
    if resolved.is_relative_to(root.resolve()):
        raise ValueError("audit telemetry must be written outside the repository")
    return resolved


def write_report(root: Path, path: Path, value: dict) -> None:
    target = report_path(root, path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8", newline="\n")


class AuditTimer:
    def __init__(self) -> None:
        self.started = time.perf_counter()
        self.before = git_metrics()
        self.stages: list[dict] = []

    def call(self, name: str, function: Callable[..., Any], *args, **kwargs):
        started = time.perf_counter()
        row = {"name": name, "completed": False}
        try:
            result = function(*args, **kwargs)
            row["completed"] = True
            if isinstance(result, list):
                row["returned_items"] = len(result)
            return result
        finally:
            row["seconds"] = time.perf_counter() - started
            self.stages.append(row)

    def report(self) -> dict:
        after = git_metrics()
        return {
            "seconds": time.perf_counter() - self.started,
            "stages": list(self.stages),
            "git_in_process": {key: value - self.before.get(key, 0) for key, value in after.items()},
            "git_scope": "shared reader calls in this process; excludes child processes and fixture Git commands",
            "runtime": runtime_metadata(),
        }
