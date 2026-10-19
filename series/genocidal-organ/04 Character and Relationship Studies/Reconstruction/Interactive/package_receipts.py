"""Project complete retained runs into public, byte-checkable receipts.

No source media, auth files or full host session files are read. Review resulting
text for privacy and rights before publication. Output files must not exist.
"""
import argparse
import hashlib
import json
import pathlib


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_bytes())


def write_new(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--initial", type=pathlib.Path, nargs="+", required=True)
    p.add_argument("--adaptive", type=pathlib.Path, nargs="+", required=True)
    p.add_argument("--out", type=pathlib.Path, required=True)
    a = p.parse_args()
    conversations = {}
    streams = []
    manifests = []
    for run in a.initial:
        manifests.append({"run": run.name, "manifest": load(run / "run_manifest.json")})
        for path in sorted(run.glob("*/conversation.json")):
            data = load(path)
            cid = data["case"]["id"]
            if cid in conversations:
                raise ValueError("Duplicate initial session")
            conversations[cid] = {"case": data["case"], "initial": data["turns"], "adaptive": []}
            if len(data["turns"]) != 5:
                raise ValueError("Incomplete initial conversation")
            for turn in data["turns"]:
                stem = path.parent / ("turn-%02d" % turn["turn"])
                payload = stem.with_suffix(".events.jsonl").read_bytes()
                stderr = stem.with_suffix(".stderr.txt").read_bytes()
                authored_input = stem.with_suffix(".input.txt").read_bytes()
                assert sha(payload) == turn["events_sha256"]
                assert sha(stderr) == turn["stderr_sha256"]
                assert sha(authored_input) == turn["input_sha256"]
                streams.append({"id": cid, "phase": "initial", "turn": turn["turn"], "stdout_jsonl": payload.decode("utf-8"), "stderr": stderr.decode("utf-8"), "stdout_sha256": sha(payload), "stderr_sha256": sha(stderr)})
    for wave, run in enumerate(a.adaptive, 1):
        manifests.append({"run": run.name, "manifest": load(run / "run_manifest.json"), "runtime_observation": load(run / "runtime_observation.json")})
        for path in sorted(run.glob("*/conversation.json")):
            data = load(path)
            cid = data["case"]["id"]
            assert data["status"] == "EXECUTED_AWAITING_INDEPENDENT_EVALUATION"
            assert conversations[cid]["initial"][0]["session_id"] == data["case"]["session_id"]
            payload = (path.parent / "events.jsonl").read_bytes()
            stderr = (path.parent / "stderr.txt").read_bytes()
            authored_input = (path.parent / "input.txt").read_bytes()
            assert sha(payload) == data["events_sha256"]
            assert sha(stderr) == data["stderr_sha256"]
            assert sha(authored_input) == data["input_sha256"]
            conversations[cid]["adaptive"].append({"wave": wave, **data})
            streams.append({"id": cid, "phase": "adaptive", "wave": wave, "stdout_jsonl": payload.decode("utf-8"), "stderr": stderr.decode("utf-8"), "stdout_sha256": sha(payload), "stderr_sha256": sha(stderr)})
    for c in conversations.values():
        if len(c["adaptive"]) != len(a.adaptive):
            raise ValueError("Incomplete adaptive wave")
    stream_list = sorted(streams, key=lambda v: (v["id"], 0 if v["phase"] == "initial" else 1, v.get("turn", v.get("wave"))))
    write_new(a.out / "interactions.json", {"schema": "character-interactive-transcript/v1", "conversations": [conversations[k] for k in sorted(conversations)]})
    write_new(a.out / "runtime_receipt.json", {"schema": "character-interactive-runtime-receipt/v1", "projection": "Complete raw stdout/stderr strings; no stream editing, source inputs reconstructable from exact policy+wrapper+case and recorded hashes", "manifests": manifests, "streams": stream_list})
    print(json.dumps({"sessions": len(conversations), "responses": len(streams), "output_hashes": {n: sha((a.out / n).read_bytes()) for n in ["interactions.json", "runtime_receipt.json"]}}))


if __name__ == "__main__":
    main()
