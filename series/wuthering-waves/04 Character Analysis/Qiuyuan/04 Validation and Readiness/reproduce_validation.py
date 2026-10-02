#!/usr/bin/env python3
"""Validate the Qiuyuan draft packet and, when supplied, its local evidence joins.

This checks structure and selected identities, not the truth of literary judgments.
It is read-only unless --write-report is passed. No media or raw text is copied.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent.parent
LANGUAGES = {"en", "ja", "ko", "zh"}
COMMIT = "353f2eaed119bc9f680eab92807d20ac75a79b40"
MEDIA_SUFFIXES = {".wav", ".flac", ".wem", ".mp3", ".mp4", ".png", ".webp", ".pak"}
COHORT_SHA256 = "6aa6d7e08e8428ff380de7e6d44824128fc70acb7b4bed03bee5ce5f42335d1c"
COHORT_SPECS = {
    "evacuation": (["9913/4", "9916/3"], 12, 48),
    "original_restraint": (["10738/2"], 13, 52),
    "fenrico_judgment": (["10735/2"], 12, 48),
    "fenrico_lantern": (["10736/2"], 16, 64),
    "scar_confrontation": (["11919/1"], 5, 20),
    "surface_defense": (["8882/5"], 20, 80),
    "postbattle_survivors": (["11982/1"], 6, 24),
    "harbor_home": (["9932/3"], 24, 96),
    "later_coda": (["17722/4"], 2, 8),
}




# Exact character-root-relative paths after the artifact-class migration.
PACKET_ARTIFACT_PATHS = {'AUDIO_MATCHED_SEMANTIC_CASES.json': '03 Audiovisual and Voice/AUDIO_MATCHED_SEMANTIC_CASES.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.json', 'CHARACTER_VISUAL_DESIGN_PROFILE.md': '03 Audiovisual and Voice/CHARACTER_VISUAL_DESIGN_PROFILE.md', 'CHARACTER_VISUAL_REFERENCE_MANIFEST.json': '03 Audiovisual and Voice/CHARACTER_VISUAL_REFERENCE_MANIFEST.json', 'FAVOR_WORD_ID_TEXT_KEY_CROSSWALK.json': '01 Evidence and Source-Facing/FAVOR_WORD_ID_TEXT_KEY_CROSSWALK.json', 'VALIDATION_REPORT.json': '04 Validation and Readiness/VALIDATION_REPORT.json', 'WUWA_QIUYUAN_ANALYSIS_PACKET_README.md': 'WUWA_QIUYUAN_ANALYSIS_PACKET_README.md', 'WUWA_QIUYUAN_AV_AND_HUMAN_RETRIEVAL_PLAN.md': '03 Audiovisual and Voice/WUWA_QIUYUAN_AV_AND_HUMAN_RETRIEVAL_PLAN.md', 'WUWA_QIUYUAN_AV_HUMAN_RETRIEVAL_CROSSWALK.md': '03 Audiovisual and Voice/WUWA_QIUYUAN_AV_HUMAN_RETRIEVAL_CROSSWALK.md', 'WUWA_QIUYUAN_CHARACTER_DEEP_DIVE_PRE_AV.md': '01 Evidence and Source-Facing/WUWA_QIUYUAN_CHARACTER_DEEP_DIVE_PRE_AV.md', 'WUWA_QIUYUAN_CHARACTER_MODEL_PACKAGE.json': '02 Reconstruction/WUWA_QIUYUAN_CHARACTER_MODEL_PACKAGE.json', 'WUWA_QIUYUAN_CLAIM_REVISION_LEDGER.md': '04 Validation and Readiness/WUWA_QIUYUAN_CLAIM_REVISION_LEDGER.md', 'WUWA_QIUYUAN_COMBAT_TRIGGER_SENSORY_AND_LIMIT_LANGUAGE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_QIUYUAN_COMBAT_TRIGGER_SENSORY_AND_LIMIT_LANGUAGE_PROFILE.md', 'WUWA_QIUYUAN_EVIDENCE_AND_FALSIFICATION_MATRIX.md': '01 Evidence and Source-Facing/WUWA_QIUYUAN_EVIDENCE_AND_FALSIFICATION_MATRIX.md', 'WUWA_QIUYUAN_HARBOR_SHEATH_AND_INVERTED_BOAT_MESSAGE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_QIUYUAN_HARBOR_SHEATH_AND_INVERTED_BOAT_MESSAGE_PROFILE.md', 'WUWA_QIUYUAN_HUT_SENSORY_PRACTICE_AND_ORDINARY_CARE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_QIUYUAN_HUT_SENSORY_PRACTICE_AND_ORDINARY_CARE_PROFILE.md', 'WUWA_QIUYUAN_JUDGMENT_COUNTERFACTUAL_GUILT_AND_SHEATH_PROFILE.md': '01 Evidence and Source-Facing/WUWA_QIUYUAN_JUDGMENT_COUNTERFACTUAL_GUILT_AND_SHEATH_PROFILE.md', 'WUWA_QIUYUAN_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md': '04 Validation and Readiness/WUWA_QIUYUAN_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md', 'WUWA_QIUYUAN_RECOGNITION_BLADE_WEIGHT_AND_CHOSEN_SERVICE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_QIUYUAN_RECOGNITION_BLADE_WEIGHT_AND_CHOSEN_SERVICE_PROFILE.md', 'WUWA_QIUYUAN_RECONSTRUCTIVE_PROFILE_PRE_AV.md': '02 Reconstruction/WUWA_QIUYUAN_RECONSTRUCTIVE_PROFILE_PRE_AV.md', 'WUWA_QIUYUAN_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_QIUYUAN_RELATIONSHIP_STATE_AND_ORDINARY_LIFE_PROFILE.md', 'WUWA_QIUYUAN_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md': '04 Validation and Readiness/WUWA_QIUYUAN_SOURCE_CENSUS_CHRONOLOGY_AND_IDENTITY_AUDIT.md', 'WUWA_QIUYUAN_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md': '04 Validation and Readiness/WUWA_QIUYUAN_SOURCE_DEFINED_AUDIO_COHORT_AUDIT.md', 'WUWA_QIUYUAN_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md': '03 Audiovisual and Voice/WUWA_QIUYUAN_SPEECH_AND_MACHINE_VOICE_PROFILE_PRE_AV.md', 'WUWA_QIUYUAN_TOWER_TRACE_DISGUISE_AND_INFERENCE_PROFILE.md': '01 Evidence and Source-Facing/WUWA_QIUYUAN_TOWER_TRACE_DISGUISE_AND_INFERENCE_PROFILE.md', 'reproduce_validation.py': '04 Validation and Readiness/reproduce_validation.py'}

def packet_artifact(root: Path, name: str) -> Path:
    return root / PACKET_ARTIFACT_PATHS.get(name, name)

def jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def require(condition: bool, message: str, checks: list[str]) -> None:
    if not condition:
        raise AssertionError(message)
    checks.append(message)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_action(locator: str) -> str | None:
    match = re.search(r"#/(\d+)/Actions!/(\d+)/Params/TalkItems/\d+$", locator)
    return f"{match[1]}/{match[2]}" if match else None


def source_render_tuple(line: dict, render: dict) -> tuple:
    return (
        line["semantic_voice_occurrence_id"], line["source_locator"], line["text_key"],
        render["voice_language"], render["render_analysis_id"],
        render["canonical_pcm_sha256"], render["flac_sha256"],
    )


def cohort_render_tuple(member: dict) -> tuple:
    return (
        member["semantic_voice_occurrence_id"], member["source_locator"], member["text_key"],
        member["voice_language"], member["render_analysis_id"],
        member["canonical_pcm_sha256"], member["flac_sha256"],
    )


def build_favor_word_id_key_crosswalk(source_root: Path) -> dict:
    """Preserve raw favor-word Id and Content key as separate source fields."""
    source = source_root / "ANALYSIS" / "Characters" / "Qiuyuan" / "character_source_package.json"
    voice = (source_root / "_voice_media" / "character" / "complete_voice_corpus"
             / "Qiuyuan" / "v0_1" / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
    package = json.loads(source.read_text(encoding="utf-8"))
    archive = package["favor_words"]
    lines = [row for row in jsonl(voice) if "/BinData/favor/favorword.json#/" in row["source_locator"]]
    by_locator = {row["source_locator"]: row for row in lines}
    if len(archive) != 73 or len(lines) != 73 or len(by_locator) != 73:
        raise AssertionError("favor-word archive/voice locator denominators changed")
    rows = []
    for word in archive:
        locator = word["source_locator"]
        line = by_locator[locator]
        content_key = word["content"]["text_key"]
        if (word["raw"]["Id"] != word["id"] or word["raw"]["Content"] != content_key
                or line["text_key"] != content_key):
            raise AssertionError(f"favor-word raw/normalized/voice key conflict at {locator}")
        renders = line["renders"]
        if (len(renders) != 4 or {r["voice_language"] for r in renders} != LANGUAGES
                or {r["event_path"] for r in renders} != {word["voice_asset"]}
                or len({r["event_id"] for r in renders}) != 1
                or any(r["event_id"] is None or r["numeric_media_id"] is None
                       or r["materialization_status"] != "flac_roundtrip_pcm_identical"
                       for r in renders)):
            raise AssertionError(f"favor-word four-dub event/media/PCM join changed at {locator}")
        rows.append({
            "raw_record_id": word["id"],
            "content_text_key": content_key,
            "title_text_key": word["title"]["text_key"],
            "source_locator": locator,
            "source_row_index": int(locator.rsplit("#/", 1)[1]),
            "voice_event_path": word["voice_asset"],
            "event_id": renders[0]["event_id"],
            "semantic_voice_occurrence_id": line["semantic_voice_occurrence_id"],
            "four_language_render_count": len(renders),
            "raw_id_matches_content_key_suffix": content_key == f"FavorWord_{word['id']}_Content",
        })
    if len({r["content_text_key"] for r in rows}) != 73:
        raise AssertionError("favor-word content keys are not unique")
    return {
        "schema_version": "wuwa.packet.favor-word-id-key-crosswalk.v0.1",
        "character": "Qiuyuan",
        "source_commit": COMMIT,
        "source_package_relative_path": "ANALYSIS/Characters/Qiuyuan/character_source_package.json",
        "voice_analysis_relative_path": "_voice_media/character/complete_voice_corpus/Qiuyuan/v0_1/COMPLETE_VOICE_LINE_ANALYSIS.jsonl",
        "join_basis": "exact pinned favorword source locator and raw Content field, never an Id-derived key",
        "row_count": len(rows),
        "raw_id_content_key_suffix_mismatch_count": sum(
            not row["raw_id_matches_content_key_suffix"] for row in rows),
        "rows": rows,
    }


def validate(source_root: Path | None) -> dict:
    checks: list[str] = []
    matrix = (packet_artifact(HERE, "WUWA_QIUYUAN_EVIDENCE_AND_FALSIFICATION_MATRIX.md")).read_text(encoding="utf-8")
    evidence_ids = set(re.findall(r"\| (QIU-E\d{2}) \|", matrix))
    claim_ids = set(re.findall(r"\| (QIU-C\d{2}) —", matrix))
    require(len(evidence_ids) == 38, "38 unique evidence bundles", checks)
    require(len(claim_ids) == 36, "36 unique claims", checks)
    require(not any(p.suffix.lower() in MEDIA_SUFFIXES for p in HERE.rglob("*") if p.is_file()), "no media in Git packet", checks)
    for path in HERE.rglob("*.md"):
        body = path.read_text(encoding="utf-8")
        if path.name.startswith("CHARACTER_VISUAL_"):
            continue  # Existing independently governed visual artifacts.
        if path.name.startswith("WUWA_QIUYUAN_"):
            require(body.startswith("---\n") and "\nstatus: draft_noncurrent\n" in body, f"draft authority: {path.name}", checks)
            require("\ndo_not_use_as_current_authority: true\n" in body, f"not-current flag: {path.name}", checks)
    model = json.loads((packet_artifact(HERE, "WUWA_QIUYUAN_CHARACTER_MODEL_PACKAGE.json")).read_text(encoding="utf-8"))
    require(model["authority"] == "draft_noncurrent" and model["source_commit"] == COMMIT, "model authority/source pin", checks)
    require(len(model["rules"]) == 16 and {x["id"] for x in model["rules"]}
            == {f"QIU-R{number:02d}" for number in range(1, 17)},
            "16 distinct model rules", checks)
    require(len(model["required_inputs"]) == 12, "12 model selection inputs", checks)
    require(all(set(rule["evidence_ids"]) <= evidence_ids for rule in model["rules"]), "all model rule evidence IDs resolve", checks)
    require(all(rule["probability"] is None for rule in model["rules"]), "no fabricated numeric behavioral probabilities", checks)
    probes = (packet_artifact(HERE, "WUWA_QIUYUAN_MODEL_FIDELITY_AND_STRESS_TEST_PRE_AV.md")).read_text(encoding="utf-8")
    require(set(re.findall(r"\| (QIU-P\d{2}) \|", probes)) ==
            {f"QIU-P{number:02d}" for number in range(1, 40)},
            "39 distinct non-blind probes", checks)
    require(set(re.findall(r"\| (QIU-R\d{2}) —", probes)) ==
            {f"QIU-R{number:02d}" for number in range(1, 17)},
            "sixteen-rule challenge map", checks)
    require(set(re.findall(r"### (QIU-I\d{2}) —", probes)) ==
            {f"QIU-I{number:02d}" for number in range(1, 9)},
            "eight interacting failure tests", checks)
    crosswalk_path = packet_artifact(HERE, "FAVOR_WORD_ID_TEXT_KEY_CROSSWALK.json")
    id_key_crosswalk = json.loads(crosswalk_path.read_text(encoding="utf-8"))
    require(id_key_crosswalk["source_commit"] == COMMIT and id_key_crosswalk["row_count"] == 73
            and id_key_crosswalk["raw_id_content_key_suffix_mismatch_count"] == 30,
            "73 source-row favor-word joins with 30 Id/key suffix differences", checks)
    trigger_rows = {row["raw_record_id"]: row for row in id_key_crosswalk["rows"]
                    if 141132 <= row["raw_record_id"] <= 141174}
    require(len(trigger_rows) == 42 and sum(row["four_language_render_count"]
                for row in trigger_rows.values()) == 168,
            "42 combat/traversal trigger rows and 168 four-dub render associations", checks)
    require(trigger_rows[141162]["content_text_key"] == "FavorWord_141157_Content"
            and trigger_rows[141167]["content_text_key"] == "FavorWord_141162_Content"
            and trigger_rows[141142]["content_text_key"] == "FavorWord_141172_Content",
            "raw Id and Content key differ at fallen, enemies-near and skill rows", checks)
    nominated_event_ids = {141141: 301856180, 141147: 3812360776, 141150: 3704763929,
                           141161: 3194019218, 141162: 121494393, 141164: 121494395,
                           141169: 883110658}
    require(all(trigger_rows[raw_id]["event_id"] == event_id
                for raw_id, event_id in nominated_event_ids.items()),
            "seven exact combat-trigger event IDs", checks)
    cases = json.loads((packet_artifact(HERE, "AUDIO_MATCHED_SEMANTIC_CASES.json")).read_text(encoding="utf-8"))
    require(cases["semantic_cases"] == 14 and len(cases["cases"]) == 14, "14 matched semantic cases", checks)
    crosswalk = (packet_artifact(HERE, "WUWA_QIUYUAN_AV_HUMAN_RETRIEVAL_CROSSWALK.md")).read_text(encoding="utf-8")
    require(all(f"`{case['text_key']}`" in crosswalk for case in cases["cases"]),
            "all 14 exact sound cases occur in AV crosswalk", checks)
    require("9927/2/0" in crosswalk and "false initial charge" in crosswalk,
            "identity and two-stage Geshu controls in AV crosswalk", checks)
    require(set(re.findall(r"\| (QIU-H\d{2})", crosswalk)) ==
            {f"QIU-H{number:02d}" for number in range(1, 6)},
            "five harbor/message retrieval nominations", checks)
    require(set(re.findall(r"\| (QIU-B\d{2}) \|", crosswalk)) ==
            {f"QIU-B{number:02d}" for number in range(1, 8)}
            and set(re.findall(r"\| (QIU-R\d{2}) \|", crosswalk)) ==
            {f"QIU-R{number:02d}" for number in range(1, 11)},
            "seven trigger nominations and ten runtime/identity controls", checks)
    require(sum(len(row["renders"]) for row in cases["cases"]) == 56, "56 selected render records", checks)
    require(all({r["language"] for r in row["renders"]} == LANGUAGES for row in cases["cases"]), "each case spans four languages", checks)
    require(all(len(r["wem_sha256"]) == 64 and len(r["canonical_pcm_sha256"]) == 64 and len(r["flac_sha256"]) == 64 for row in cases["cases"] for r in row["renders"]), "selected render hashes present", checks)
    require(sum(r["event_id"] is None and r["numeric_media_id"] is None for row in cases["cases"] for r in row["renders"]) == 32,
            "32 of 56 selected renders retain paired null event/media IDs", checks)
    ascension_cases = {row["text_key"]: row for row in cases["cases"] if row["text_key"] in {"FavorWord_141128_Content", "FavorWord_141131_Content"}}
    require(set(ascension_cases) == {"FavorWord_141128_Content", "FavorWord_141131_Content"}, "recognition and blade-weight cases selected", checks)
    require(all(render["event_id"] is not None and render["numeric_media_id"] is not None
                for row in ascension_cases.values() for render in row["renders"]),
            "ascension render event/media IDs explicit", checks)
    result = {"packet": "Qiuyuan", "scope": "QIUYUAN_PINNED_3_6_0_TEXT_AUDIO_PRE_AV", "checks": checks, "source_crosscheck": "not_requested"}
    if source_root is not None:
        require(id_key_crosswalk == build_favor_word_id_key_crosswalk(source_root),
                "favor-word Id/key crosswalk reproduces from pinned local source and voice analysis", checks)
        source = source_root / "ANALYSIS" / "Characters" / "Qiuyuan"
        voice = source_root / "_voice_media" / "character" / "complete_voice_corpus" / "Qiuyuan" / "v0_1"
        measurements = source_root / "_research" / "character_packets" / "Qiuyuan" / "audio_work" / "AUDIO_MEASUREMENT_SUMMARY.json"
        audit = json.loads((source / "COLLECTION_AUDIT.json").read_text(encoding="utf-8"))
        direct = audit["scopes"]["direct_character"]
        require(audit["valid"] and direct["voice_completeness_valid"], "selected collection audit valid", checks)
        require((direct["accepted_occurrences"], direct["source_voiced"], direct["source_unvoiced"], direct["candidate_occurrences"]) == (187, 182, 5, 188), "direct occurrence denominator", checks)
        require((direct["semantic_voice_lines"], direct["render_associations"], direct["unique_flac_objects"]) == (255, 1022, 1018), "voice line/association/object denominators", checks)
        decisions = jsonl(source / "occurrence_identity_crosswalk.jsonl")
        require(Counter(row["character_attribution"] for row in decisions) == {"accepted_solo": 187, "unresolved": 1}, "identity crosswalk state counts", checks)
        package = json.loads((source / "character_source_package.json").read_text(encoding="utf-8"))
        archive = {row["content"]["text_key"]: row for row in package["favor_words"]}
        stories = {row["content"]["text_key"]: row for row in package["favor_stories"]}
        hut_text = stories["FavorStory_141102_Content"]["content"]["values"]
        require("重新勾起" in hut_text["zh-Hans"]["content"]
                and "at least for a little while" in hut_text["en"]["content"]
                and "再び呼び覚ます" in hut_text["ja"]["content"]
                and "다시 불러일으킬" in hut_text["ko"]["content"],
                "hut medicine reawakening and EN-only open-ended timing clause", checks)
        require("必须用这种特殊的药" in archive["FavorWord_141111_Content"]["content"]["values"]["zh-Hans"]["content"]
                and "陷入迷狂" in archive["FavorWord_141111_Content"]["content"]["values"]["zh-Hans"]["content"],
                "later special-medicine dependency and mental-risk Chinese anchor", checks)
        ascension_keys = [f"FavorWord_{key}_Content" for key in range(141127, 141132)]
        require(all(key in archive for key in ascension_keys), "five ascension archive entries retained", checks)
        require(all(archive[key]["content"]["values"][language]["status"] == "resolved"
                    for key in ascension_keys for language in ("zh-Hans", "en", "ja", "ko")),
                "four-language ascension text witnesses resolved", checks)
        require("再造" in archive["FavorWord_141128_Content"]["content"]["values"]["zh-Hans"]["content"]
                and "重" in archive["FavorWord_141131_Content"]["content"]["values"]["zh-Hans"]["content"],
                "recognition and blade-weight Chinese semantic anchors", checks)
        require("这无关剑术" in archive["FavorWord_141131_Content"]["content"]["values"]["zh-Hans"]["content"]
                and "skill never falters" in archive["FavorWord_141131_Content"]["content"]["values"]["en"]["content"],
                "blade-weight technical localization boundary", checks)
        require("值得我为之出鞘" in archive["FavorWord_141105_Content"]["content"]["values"]["zh-Hans"]["content"]
                and "不会多问" in archive["FavorWord_141122_Content"]["content"]["values"]["zh-Hans"]["content"],
                "chosen cause versus short service invitation", checks)
        require("text-to-speech" in archive["FavorWord_141101_Content"]["content"]["values"]["en"]["content"]
                and "虚实寒热" in archive["FavorWord_141106_Content"]["content"]["values"]["zh-Hans"]["content"]
                and "不是酒，而是药" in archive["FavorWord_141111_Content"]["content"]["values"]["zh-Hans"]["content"],
                "read-aloud access, individual meals and medicine distinct from wine", checks)
        require("暂且栖身" in archive["FavorWord_141118_Content"]["content"]["values"]["zh-Hans"]["content"],
                "birthday shelter is explicitly temporary", checks)
        archive_by_raw_id = {word["id"]: word for word in package["favor_words"]}
        require("我听到你了" in archive_by_raw_id[141141]["content"]["values"]["zh-Hans"]["content"]
                and "你的性命" in archive_by_raw_id[141150]["content"]["values"]["zh-Hans"]["content"]
                and "舍身佯攻" in archive_by_raw_id[141161]["content"]["values"]["zh-Hans"]["content"],
                "combat source: hearing, lethal threat and bounded feint", checks)
        require("来世" in archive_by_raw_id[141162]["content"]["values"]["zh-Hans"]["content"]
                and "风" in archive_by_raw_id[141163]["content"]["values"]["zh-Hans"]["content"]
                and "黑暗" in archive_by_raw_id[141164]["content"]["values"]["zh-Hans"]["content"],
                "combat source: three distinct fallen texts", checks)
        line_rows = jsonl(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
        require(len(line_rows) == 255, "255 selected voice-line records", checks)
        tower_actions = {f"{row}/{action}" for row, action in
                         ((9917, 2), (9918, 1), (9919, 1), (9920, 1), (9921, 1),
                          (9922, 2), (9923, 1), (9924, 3), (9925, 1), (9926, 1))}
        tower_lines = [line for line in line_rows if source_action(line["source_locator"]) in tower_actions]
        tower_renders = [render for line in tower_lines for render in line["renders"]]
        require(len(tower_lines) == 21 and len(tower_renders) == 85
                and len({render["canonical_pcm_sha256"] for render in tower_renders}) == 85,
                "ten tower actions: 21 accepted lines and 85 distinct PCM renders", checks)
        require(all(render["materialization_status"] == "flac_roundtrip_pcm_identical"
                    and render.get("event_id") is None and render.get("numeric_media_id") is None
                    for render in tower_renders),
                "tower renders PCM-valid without invented numeric event/media IDs", checks)
        opening = [line for line in tower_lines if line["text_key"] == "HRT_Rinascita_Interludes_3_1"]
        require(len(opening) == 1
                and Counter(render["voice_language"] for render in opening[0]["renders"])
                == {"ja": 2, "en": 1, "ko": 1, "zh": 1}
                and len({render["canonical_pcm_sha256"] for render in opening[0]["renders"]}) == 5,
                "opening line has two distinct Japanese runtime render variants", checks)
        disguise_lines = [line for line in line_rows if source_action(line["source_locator"]) == "9927/2"]
        disguise_renders = [render for line in disguise_lines for render in line["renders"]]
        require(len(disguise_lines) == 9 and len(disguise_renders) == 36
                and len({render["canonical_pcm_sha256"] for render in disguise_renders}) == 36,
                "separate disguise action: nine accepted lines and 36 PCM renders", checks)
        harbor_lines = [line for line in line_rows if source_action(line["source_locator"]) == "9932/3"]
        harbor_renders = [render for line in harbor_lines for render in line["renders"]]
        require(len(harbor_lines) == 24 and len(harbor_renders) == 96
                and len({render["canonical_pcm_sha256"] for render in harbor_renders}) == 96,
                "harbor action: 24 accepted lines and 96 distinct PCM renders", checks)
        require(all(render["materialization_status"] == "flac_roundtrip_pcm_identical"
                    and render.get("event_id") is None and render.get("numeric_media_id") is None
                    for render in harbor_renders),
                "harbor PCM-valid with paired-null numeric event/media IDs", checks)
        line_index = {(row["text_key"], row["semantic_voice_occurrence_id"]): row for row in line_rows}
        for case in cases["cases"]:
            line = line_index[(case["text_key"], case["semantic_voice_occurrence_id"])]
            require(case["source_locator"] == line["source_locator"], f"source locator {case['text_key']}", checks)
            expected = {
                (r["runtime_render_variant_id"], r["canonical_pcm_sha256"], r["flac_sha256"])
                for r in line["renders"]
            }
            observed = {
                (r["render_variant_id"], r["canonical_pcm_sha256"], r["flac_sha256"])
                for r in case["renders"]
            }
            require(expected == observed, f"render join {case['text_key']}", checks)
        audio = json.loads(measurements.read_text(encoding="utf-8"))
        require((audio["manifest_objects"], audio["measured_objects"], audio["repeated_pcm_manifest_rows"]) == (1018, 1018, 4), "full local audio measurement counts", checks)
        require(not audio["failed_objects"], "no local audio measurement failures", checks)
        cohort_path = source_root / "_research" / "character_packets" / "Qiuyuan" / "audio_work" / "QIUYUAN_SOURCE_COHORT_AUDIT.json"
        cohort_audit = json.loads(cohort_path.read_text(encoding="utf-8"))
        require(sha256_file(cohort_path) == COHORT_SHA256, "private source-cohort audit SHA-256", checks)
        require(cohort_audit["source_commit"] == COMMIT and cohort_audit["source_generation"] == model["source_generation"],
                "source-cohort authority pin matches packet", checks)
        require(cohort_audit["line_analysis_sha256"] == sha256_file(voice / "COMPLETE_VOICE_LINE_ANALYSIS.jsonl")
                and cohort_audit["object_measurements_sha256"] == sha256_file(measurements.parent / "AUDIO_OBJECT_MEASUREMENTS.jsonl")
                and cohort_audit["measurement_summary_sha256"] == sha256_file(measurements),
                "source-cohort line and measurement inputs byte-pinned", checks)
        require(cohort_audit["whole_measured_object_count"] == 1018
                and cohort_audit["whole_measured_integrity_pass_count"] == 1018
                and not cohort_audit["human_perceptual_review_performed"]
                and not cohort_audit["video_review_performed"],
                "whole measurement integrity and unreviewed AV state", checks)
        cohorts = {row["name"]: row for row in cohort_audit["cohorts"]}
        require(len(cohorts) == len(cohort_audit["cohorts"]) == 9 and set(cohorts) == set(COHORT_SPECS),
                "nine distinct source-defined cohorts", checks)
        all_members: list[dict] = []
        for name, (selectors, semantic_count, render_count) in COHORT_SPECS.items():
            cohort = cohorts[name]
            members = cohort["members"]
            require(cohort["source_actions"] == selectors
                    and cohort["semantic_lines"] == semantic_count
                    and cohort["render_associations"] == render_count
                    and len(members) == render_count
                    and not cohort["semantic_lines_without_renders"],
                    f"cohort selector and counts: {name}", checks)
            expected_lines = [line for line in line_rows if source_action(line["source_locator"]) in selectors]
            expected = {source_render_tuple(line, render) for line in expected_lines for render in line["renders"]}
            observed = {cohort_render_tuple(member) for member in members}
            require(len(expected_lines) == semantic_count and len(expected) == render_count and observed == expected,
                    f"exact source-to-render cohort membership: {name}", checks)
            require(sum(cohort["language_statistics"][language]["integrity_pass_objects"] for language in LANGUAGES)
                    == render_count, f"cohort integrity: {name}", checks)
            all_members.extend(members)
        require((len({member["semantic_voice_occurrence_id"] for member in all_members}),
                 len({member["render_analysis_id"] for member in all_members}),
                 len({member["canonical_pcm_sha256"] for member in all_members}),
                 len(all_members)) == (110, 440, 440, 440),
                "disjoint source-cohort union: 110 semantic / 440 renders / 440 PCM", checks)
        require(sum(cohort["language_statistics"][language]["pitch_qualified_objects"]
                    for cohort in cohorts.values() for language in LANGUAGES) == 61,
                "cohort pitch-qualified denominator: 61/440", checks)
        scene_index = {(row["flow_state_row_index"], row["action_index"]): row
                       for row in jsonl(source / "SCENE_AND_EVIDENCE_LEDGER.jsonl")}
        quest_tree_path = (source_root / "_sources" / "Arikatsu_WutheringWaves_Data"
                           / "BinData" / "QuestTree" / "questtreenode.json")
        quest_tree = json.loads(quest_tree_path.read_text(encoding="utf-8"))
        qiuyuan_node = quest_tree[26]
        require(qiuyuan_node["Id"] == 212000
                and qiuyuan_node["QuestArray"] == [175000000]
                and qiuyuan_node["Summary"] == "QuestTree_Summary_212000",
                "QuestTree node 212000 pins Qiuyuan synopsis to quest 175000000", checks)
        rescue_summaries = [row for row in jsonl(source / "source_mentions.jsonl")
                            if row["text_key"] == "QuestTree_Summary_212000"]
        require(len(rescue_summaries) == 1
                and all(rescue_summaries[0]["localizations"][language]["status"] == "resolved"
                        and rescue_summaries[0]["localizations"][language]["source_locator"].endswith(
                            f"/Textmaps/{language}/multi_text/MultiText.json#/275411")
                        for language in ("zh-Hans", "en", "ja", "ko")),
                "Qiuyuan quest synopsis has four exact textmap witnesses", checks)
        rescue_text = {language: value["content"]
                       for language, value in rescue_summaries[0]["localizations"].items()}
        require("救下教士" in rescue_text["zh-Hans"]
                and "rescuing an Acolyte" in rescue_text["en"]
                and "侍祭を助けた" in rescue_text["ja"]
                and "성직자를 구한" in rescue_text["ko"],
                "four-witness retrospective confirms an earlier Acolyte rescue", checks)
        leon_intro = scene_index[(9913, 4)]["talk_items"][6]
        leon_thanks = scene_index[(9916, 3)]["talk_items"][6]
        qiuyuan_safety = scene_index[(9916, 3)]["talk_items"][1]
        require(leon_intro["technical_speaker_id"] == 1567
                and "Leon" in leon_intro["text_witnesses"]["en"]["content"]
                and leon_thanks["technical_speaker_id"] == 1567
                and qiuyuan_safety["technical_speaker_id"] == 1563
                and "Get to safety" in qiuyuan_safety["text_witnesses"]["en"]["content"]
                and "出手相助" in leon_thanks["text_witnesses"]["zh"]["content"]
                and "not have survived" in leon_thanks["text_witnesses"]["en"]["content"]
                and "助けに来て" in leon_thanks["text_witnesses"]["ja"]["content"]
                and "도와주지" in leon_thanks["text_witnesses"]["ko"]["content"],
                "Leon self-identifies and directly credits Qiuyuan's earlier rescue", checks)
        raw_states = {int(row["source_locator"].rsplit("#/", 1)[1]): row["raw"]
                      for row in jsonl(source / "RAW_RELEVANT_FLOW_STATES.jsonl")}
        harbor_raw = raw_states[9932]
        harbor_action = json.loads(harbor_raw["Actions"])[3]
        harbor_talks = harbor_action["Params"]["TalkItems"]
        require(harbor_raw["StateKey"] == "剧情_2_7_黎那汐塔主线_下半_5_4"
                and harbor_action["Name"] == "ShowTalk"
                and len(harbor_talks) == 39
                and harbor_action["Params"]["TalkSequence"] == [list(range(1, 40))]
                and not harbor_action["Params"]["SequenceTransitions"]
                and "Options" not in harbor_action["Params"],
                "harbor raw action is one 39-item sequence without retained options/jumps", checks)
        require(Counter(item["WhoId"] for item in harbor_talks) ==
                {1563: 24, 1650: 8, 750088: 7},
                "harbor raw speaker ownership: Qiuyuan/merchant/Rover", checks)
        quest_rows = [row for row in jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
                      if row["source_locator"].endswith("/BinData/QuestNodeData/questnodedata.json#/13480")]
        require(len(quest_rows) == 1 and str(quest_rows[0]["quest_id"]) == "175000000"
                and any(ref["state_key"] == harbor_raw["StateKey"]
                        for ref in quest_rows[0]["matching_references"]),
                "harbor quest-node source join: 175000000", checks)
        def zh(row_index: int, action_index: int, talk_index: int) -> str:
            return scene_index[(row_index, action_index)]["talk_items"][talk_index]["text_witnesses"]["zh"]["content"]
        require("带平民离开" in zh(9913, 4, 23) and "这里留给我" in zh(9913, 4, 24)
                and "还活着的人" in zh(11982, 1, 9),
                "interaction source: evacuation and survivor priority", checks)
        require("活要见人" in zh(11919, 1, 14) and "没打算带一个活人" in zh(11919, 1, 15),
                "interaction source: formal Scar order versus personal intent", checks)
        require("欺瞒" in zh(10738, 2, 16) and "剑不在杀" in zh(10738, 2, 23)
                and "当时" in zh(9932, 3, 29) and "后来" in zh(9932, 3, 29),
                "interaction source: false original charge and distinct later fall", checks)
        require("史笔如铁" in zh(10736, 2, 42) and "家人" in zh(9932, 3, 34),
                "interaction source: Fenrico judgment and Rover's home metaphor", checks)
        harbor_scene = scene_index[(9932, 3)]["talk_items"]
        def port_text(index: int, language: str) -> str:
            return harbor_scene[index]["text_witnesses"][language]["content"]
        require("必须" in port_text(31, "zh") and "what I must" in port_text(31, "en")
                and "해야만" in port_text(31, "ko")
                and "できるのは" in port_text(31, "ja")
                and "なければ" not in port_text(31, "ja"),
                "harbor lethal obligation has a narrower Japanese clause", checks)
        require("也许有一天" in port_text(35, "zh")
                and "Maybe one day" in port_text(35, "en")
                and "나도" in port_text(35, "ko")
                and "再び" in port_text(35, "ja")
                and harbor_scene[36]["technical_speaker_id"] == 750088,
                "harbor future-home witness fork and Rover response ownership", checks)
        require("气息" in zh(9917, 2, 0) and "异样" in zh(9917, 2, 1)
                and "似乎" in zh(9919, 1, 0) and "火铳的声音" in zh(9922, 2, 0)
                and "看来" in zh(9925, 1, 1),
                "tower source separates presence, tentative residue, heard shot and control inference", checks)
        require("我认得你的气息" in zh(9927, 2, 5)
                and "你杀了那个教士" in zh(9927, 2, 15)
                and "他可活得好好的" in zh(9927, 2, 16),
                "separate recognition and conflicting Acolyte testimony", checks)
        handbook_rows = [row for row in jsonl(source / "QUEST_CONTEXT_REFERENCES.jsonl")
                         if row["source_locator"].endswith("/PlotHandBook/plothandbookconfig.json#/58")]
        require(len(handbook_rows) == 1 and handbook_rows[0]["quest_id"] == 175000000,
                "tower handbook wrapper is the pinned quest reference", checks)
        require(any(ref["state_key"] == harbor_raw["StateKey"]
                    and ref["pointer"] == "/50/Flow"
                    for ref in handbook_rows[0]["matching_references"]),
                "harbor handbook pointer joins quest 175000000", checks)
        refs = {row["state_key"].rsplit("_", 2)[-2] + "_" + row["state_key"].rsplit("_", 2)[-1]: row["pointer"]
                for row in handbook_rows[0]["matching_references"]
                if row["state_key"].endswith(("_4_4", "_4_5"))}
        require(refs == {"4_5": "/35/Flow", "4_4": "/36/Flow"},
                "handbook pointers are nonmonotonic, not an executed route", checks)
        message_action = [scene_index[(14530, 1)]]
        require(len(message_action) == 1 and len(message_action[0]["talk_items"]) == 2
                and all(not item["play_voice"] for item in message_action[0]["talk_items"]),
                "14530/1 message negative control is source-unvoiced", checks)
        message_rows = [row for row in jsonl(source / "WAVESLINE_MESSAGES.jsonl")
                        if row["short_message_id"] == 30084]
        require(len(message_rows) == 1
                and message_rows[0]["source_locator"].endswith("/BinData/PhoneMsg/shortmessage.json#/83")
                and message_rows[0]["raw"]["WhichChat"] == 52
                and message_rows[0]["raw"]["QuestId"] == 0
                and message_rows[0]["raw"]["ListenQuestId"] == 0
                and message_rows[0]["content_extraction_status"] == "metadata_only_scope",
                "ShortMessage 30084 wrapper and metadata-only collector boundary", checks)
        message_raw = raw_states[14530]
        message_talks = json.loads(message_raw["Actions"])[1]["Params"]["TalkItems"]
        require(message_raw["StateKey"] == "剧情_1.0至2.8剧情回填_17_1"
                and [item["TidTalk"] for item in message_talks] ==
                ["phone_JL_15_1", "phone_JL_15_2"]
                and all(item["WhoId"] == 701111 and "PlayVoice" not in item for item in message_talks)
                and not {"phone_JL_15_1", "phone_JL_15_2"} &
                {line["text_key"] for line in line_rows},
                "two raw written-only message items have no selected audio line", checks)
        message_witnesses = {row["text_key"]: row["values"]
                             for row in jsonl(source / "CONTEXT_TEXT_WITNESSES.jsonl")
                             if row["text_key"] in {"phone_JL_15_1", "phone_JL_15_2"}}
        require(set(message_witnesses) == {"phone_JL_15_1", "phone_JL_15_2"}
                and all(message_witnesses[key][language]["status"] == "resolved"
                        and message_witnesses[key][language]["source_locator"].endswith(
                            f"/Textmaps/{language}/multi_text/MultiText.json#/10608{8 if key.endswith('_1') else 9}")
                        for key in message_witnesses for language in ("zh-Hans", "en", "ja", "ko")),
                "two message keys have exact four-language textmap witnesses", checks)
        boat = message_witnesses["phone_JL_15_1"]
        sea = message_witnesses["phone_JL_15_2"]
        require("平稳不少" in boat["zh-Hans"]["content"]
                and "steadier" in boat["en"]["content"]
                and "덜 흔들리" in boat["ko"]["content"]
                and "ずいぶんと揺れる" in boat["ja"]["content"]
                and "风平浪静" in sea["zh-Hans"]["content"]
                and "sea is calm" in sea["en"]["content"]
                and "잔잔" in sea["ko"]["content"]
                and "穏やか" in sea["ja"]["content"],
                "Japanese boat-motion inversion and four-witness calm sea", checks)
        result["source_crosscheck"] = "passed"
    result["result"] = "pass"
    result["check_count"] = len(checks)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, help="Extraction workspace root for deeper local evidence crosscheck")
    parser.add_argument("--write-report", action="store_true")
    parser.add_argument("--write-crosswalk", action="store_true",
                        help="Build the metadata-only raw Id to Content key crosswalk from pinned local evidence")
    args = parser.parse_args()
    if args.write_crosswalk:
        if args.source_root is None:
            parser.error("--write-crosswalk requires --source-root")
        (packet_artifact(HERE, "FAVOR_WORD_ID_TEXT_KEY_CROSSWALK.json")).write_text(
            json.dumps(build_favor_word_id_key_crosswalk(args.source_root),
                       indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    report = validate(args.source_root)
    if args.write_report:
        (packet_artifact(HERE, "VALIDATION_REPORT.json")).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({key: report[key] for key in ("packet", "source_crosscheck", "result", "check_count")}, indent=2))


if __name__ == "__main__":
    main()
