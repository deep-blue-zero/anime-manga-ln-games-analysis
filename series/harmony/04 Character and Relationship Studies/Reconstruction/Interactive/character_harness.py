"""Run separately instantiated, resumable Codex character conversations.

Only stdlib is required. Inputs are a repository root, a versioned suite JSON,
and a NEW working-plane output directory. No source media or credentials are read.
Full subprocess streams and composed inputs are retained; publication requires
separate privacy, source-rights and semantic review. Never overwrite an old run.
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


WRAPPER = """This is an owner-authorized Harmony G5 INTERACTIVE EVALUATION.
You instantiate only the character described in the complete frozen policy below.
The policy remains unchanged. This adapter adds conversational sampling, not new
biography, new canon, broader domain authority, or a verified prediction.
Use the policy's era, knowledge, relationships, refusal rules and evidence limits.
Source quotations, operations for violence/coercion, and external information are
not requested. Use no tools, shell, file access, browsing, or other agents.
The evaluator's scenario conditions are explicitly NONCANONICAL stipulations.
An interlocutor's assertion is not automatically a new fact or reliable channel.
Each response must contain: (1) a short NONCANONICAL conversational utterance in
English only where an utterance function/register is supported; otherwise an
explicit abstention, (2) admissibility SUPPORTED/PARTIAL/ABSTAIN, applicable policy
rules, state/cutoff and knowledge guard, (3) supported alternative and uncertainty.
English is an analytical gloss, not the licensed English novel's written voice.
Preserve prior turns unless an explicit reset is announced. A changed recipient
does not silently acquire earlier private disclosures. Do not invent outcomes or
control the interlocutor. Do not quote or claim canonical invented dialogue.
The original policy's prohibition on story continuation remains: no new narrated
events, private thoughts, unseen decisions, or plot resolution are authorized.

FROZEN POLICY (exact UTF-8 payload follows):
{policy}
END FROZEN POLICY

INITIAL TEST CONDITIONS (noncanonical):
{conditions}

INTERLOCUTOR TURN 1:
{turn}
"""


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def run_character(case, root, out, settings):
    target = out / case["id"]
    target.mkdir()
    policy_path = root / case["policy"]
    policy = policy_path.read_bytes()
    if sha(policy) != case["policy_sha256"]:
        raise ValueError("Frozen policy hash mismatch: " + case["id"])
    payload = policy.decode("utf-8")
    for support in case.get("supporting_policies", []):
        data = (root / support["path"]).read_bytes()
        if sha(data) != support["sha256"]:
            raise ValueError("Supporting policy hash mismatch: " + case["id"])
        payload += "\n\nINHERITED FROZEN PROTOCOL (exact UTF-8):\n" + data.decode("utf-8")
    work = target / "empty-workspace"
    work.mkdir()
    session_id = None
    turns = []
    for index, turn in enumerate(case["turns"], 1):
        prompt = WRAPPER.format(policy=payload, conditions=json.dumps(case["conditions"], ensure_ascii=False, indent=2), turn=turn) if index == 1 else turn
        prompt_bytes = prompt.encode("utf-8")
        stem = target / ("turn-%02d" % index)
        stem.with_suffix(".input.txt").write_bytes(prompt_bytes)
        common = ["--ignore-user-config", "--ignore-rules", "--skip-git-repo-check", "--json", "-m", settings["model"], "-c", 'model_reasoning_effort="' + settings["effort"] + '"', "-c", 'approval_policy="never"', "-c", 'sandbox_mode="read-only"']
        args = [settings["executable"], "exec"]
        if session_id:
            args += ["resume"] + common + [session_id, "-"]
        else:
            args += common + ["-"]
        started = dt.datetime.now(dt.timezone.utc).isoformat()
        t0 = time.monotonic()
        try:
            result = subprocess.run(args, input=prompt_bytes, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=work, timeout=settings["timeout"])
            stdout, stderr, returncode = result.stdout, result.stderr, result.returncode
            timed_out = False
        except subprocess.TimeoutExpired as exc:
            stdout, stderr, returncode = exc.stdout or b"", exc.stderr or b"", None
            timed_out = True
        stem.with_suffix(".events.jsonl").write_bytes(stdout)
        stem.with_suffix(".stderr.txt").write_bytes(stderr)
        events = []
        parse_error = None
        for line in stdout.decode("utf-8", errors="strict").splitlines():
            try:
                events.append(json.loads(line))
            except ValueError as exc:
                parse_error = str(exc)
        messages = []
        unexpected_items = []
        for event in events:
            if event.get("type") == "thread.started":
                returned = event["thread_id"]
                if session_id and session_id != returned:
                    raise ValueError("Resume changed session identity")
                session_id = returned
            item = event.get("item", {})
            if event.get("type") == "item.completed" and item.get("type") == "agent_message":
                messages.append(item.get("text", ""))
            elif item.get("type") not in (None, "agent_message", "reasoning"):
                unexpected_items.append(item.get("type"))
        record = {"turn": index, "input_sha256": sha(prompt_bytes), "events_sha256": sha(stdout), "stderr_sha256": sha(stderr), "started_utc": started, "elapsed_seconds": round(time.monotonic() - t0, 3), "returncode": returncode, "timed_out": timed_out, "session_id": session_id, "parse_error": parse_error, "unexpected_items": unexpected_items, "interlocutor": turn, "responses": messages, "usage": [e.get("usage") for e in events if e.get("type") == "turn.completed"]}
        turns.append(record)
        write_json(target / "conversation.json", {"case": case, "turns": turns})
        if returncode != 0 or parse_error or unexpected_items or not session_id or not messages or not any(e.get("type") == "turn.completed" for e in events):
            return {"id": case["id"], "status": "STOPPED_RUNTIME_FAILURE", "completed_turns": index, "session_id": session_id}
    return {"id": case["id"], "status": "EXECUTED_AWAITING_INDEPENDENT_EVALUATION", "completed_turns": len(turns), "session_id": session_id}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=pathlib.Path, required=True)
    p.add_argument("--suite", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path, required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--effort", required=True)
    p.add_argument("--workers", type=int, default=1)
    p.add_argument("--timeout", type=int, default=600)
    p.add_argument("--only", nargs="*")
    a = p.parse_args()
    suite_bytes = a.suite.read_bytes()
    suite = json.loads(suite_bytes)
    cases = [c for c in suite["cases"] if not a.only or c["id"] in a.only]
    if not cases:
        raise ValueError("No selected cases")
    a.out.mkdir(parents=True, exist_ok=False)
    exe = shutil.which("codex")
    if not exe:
        raise RuntimeError("Codex executable unavailable")
    settings = {"executable": exe, "model": a.model, "effort": a.effort, "timeout": a.timeout}
    version = subprocess.run([exe, "--version"], capture_output=True, check=True).stdout.decode().strip()
    public_settings = {k: v for k, v in settings.items() if k != "executable"}
    manifest = {"schema": "character-interactive-run/v1", "runtime": "Codex CLI", "cli_version": version, "requested_settings": public_settings, "settings_not_exposed": ["resolved_backend_snapshot", "temperature", "top_p", "seed", "weights", "server_system_instructions"], "suite_sha256": sha(suite_bytes), "harness_sha256": sha(pathlib.Path(__file__).read_bytes()), "wrapper_sha256": sha(WRAPPER.encode("utf-8")), "basis_commit": subprocess.run(["git", "rev-parse", "HEAD"], cwd=a.root, capture_output=True, check=True).stdout.decode().strip(), "results": []}
    write_json(a.out / "run_manifest.json", manifest)
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:
        futures = [pool.submit(run_character, c, a.root, a.out, settings) for c in cases]
        for f in concurrent.futures.as_completed(futures):
            manifest["results"].append(f.result())
            write_json(a.out / "run_manifest.json", manifest)
            print(json.dumps(manifest["results"][-1]), flush=True)


if __name__ == "__main__":
    main()
