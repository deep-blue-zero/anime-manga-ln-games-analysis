"""Execute independent adaptive prompts against already instantiated sessions.

The JSON input has a cases array of id, session_id, prompt, policy_sha256 and
reviewer provenance. Use a new output directory for each wave. Initial frozen
policies and context remain in the same sessions; this does not create new models.
"""
import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import pathlib
import shutil
import subprocess
import time


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def execute(case, out, executable, model, effort):
    target = out / case["id"]
    target.mkdir()
    work = target / "empty-workspace"
    work.mkdir()
    prompt = case["prompt"].encode("utf-8")
    (target / "input.txt").write_bytes(prompt)
    args = [executable, "exec", "resume", "--ignore-user-config", "--ignore-rules", "--skip-git-repo-check", "--json", "-m", model, "-c", 'model_reasoning_effort="' + effort + '"', "-c", 'approval_policy="never"', "-c", 'sandbox_mode="read-only"', case["session_id"], "-"]
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    t0 = time.monotonic()
    try:
        r = subprocess.run(args, input=prompt, capture_output=True, cwd=work, timeout=600)
        stdout, stderr, returncode, timeout = r.stdout, r.stderr, r.returncode, False
    except subprocess.TimeoutExpired as e:
        stdout, stderr, returncode, timeout = e.stdout or b"", e.stderr or b"", None, True
    (target / "events.jsonl").write_bytes(stdout)
    (target / "stderr.txt").write_bytes(stderr)
    events = [json.loads(line) for line in stdout.decode("utf-8").splitlines()]
    messages = [e["item"]["text"] for e in events if e.get("type") == "item.completed" and e.get("item", {}).get("type") == "agent_message"]
    unexpected = [e["item"]["type"] for e in events if e.get("item", {}).get("type") not in (None, "agent_message", "reasoning")]
    actual_ids = [e["thread_id"] for e in events if e.get("type") == "thread.started"]
    passed = returncode == 0 and not unexpected and actual_ids == [case["session_id"]] and bool(messages) and any(e.get("type") == "turn.completed" for e in events)
    record = {"case": case, "started_utc": started, "elapsed_seconds": round(time.monotonic() - t0, 3), "returncode": returncode, "timed_out": timeout, "input_sha256": sha(prompt), "events_sha256": sha(stdout), "stderr_sha256": sha(stderr), "responses": messages, "usage": [e.get("usage") for e in events if e.get("type") == "turn.completed"], "unexpected_items": unexpected, "status": "EXECUTED_AWAITING_INDEPENDENT_EVALUATION" if passed else "STOPPED_RUNTIME_FAILURE"}
    save(target / "conversation.json", record)
    return {"id": case["id"], "status": record["status"]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path, required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--effort", required=True)
    p.add_argument("--workers", type=int, default=3)
    a = p.parse_args()
    raw = a.input.read_bytes()
    data = json.loads(raw)
    a.out.mkdir(parents=True, exist_ok=False)
    executable = shutil.which("codex")
    if not executable:
        raise RuntimeError("Codex executable unavailable")
    manifest = {"schema": "character-adaptive-wave/v1", "input_sha256": sha(raw), "harness_sha256": sha(pathlib.Path(__file__).read_bytes()), "model_requested": a.model, "effort_requested": a.effort, "cases": data["cases"], "results": []}
    save(a.out / "run_manifest.json", manifest)
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:
        futures = [pool.submit(execute, case, a.out, executable, a.model, a.effort) for case in data["cases"]]
        for f in concurrent.futures.as_completed(futures):
            result = f.result()
            manifest["results"].append(result)
            save(a.out / "run_manifest.json", manifest)
            print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
